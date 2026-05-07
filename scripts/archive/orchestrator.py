#!/usr/bin/env python3
"""
orchestrator.py — 3-Agent checkpoint-based workflow for CalcToWork batches.

Phases:
  plan      → initialize batch state, select blocks
  generate  → Agent Alpha designs calculator schemas
  content   → Agent Beta writes long-form content
  audit     → Agent Gamma runs deep audit
  fix       → auto-fix or re-dispatch for issues found
  build     → run generate_calctowork.py
  deploy    → firebase deploy --only hosting

Usage:
  python scripts/orchestrator.py --batch 4 --start-id 1050 --count 50 --mode manual
  python scripts/orchestrator.py --batch 4 --resume
"""
import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Force UTF-8 on Windows terminals so emojis and accents print correctly
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except AttributeError:
    pass

sys.path.insert(0, str(Path(__file__).parent))

from agents.shared_state import SharedState
from llm_harness import LLMHarness

ROOT = Path(__file__).parent.parent
MISSIONS_DIR = ROOT / "scripts" / "missions"
SRC = ROOT / "src"
CALCS_FILE = SRC / "calculators" / "calculators.json"
I18N_DIR = SRC / "i18n"
CONTENT_DIR = SRC / "content"
AGENTS_DIR = ROOT / "scripts" / "agents"

PHASES = ["plan", "generate", "content", "audit", "fix", "build", "deploy"]


def get_next_id():
    with open(CALCS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not data.get("calculators"):
        return 1
    return max(int(c["id"]) for c in data["calculators"]) + 1


def validate_schemas(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    cals = data.get("calculators", [])
    errors = []
    seen_ids = set()
    seen_slugs = set()
    for c in cals:
        cid = c.get("id")
        slug = c.get("slug")
        if cid in seen_ids:
            errors.append(f"Duplicate ID: {cid}")
        seen_ids.add(cid)
        if slug in seen_slugs:
            errors.append(f"Duplicate slug: {slug}")
        seen_slugs.add(slug)
        if not c.get("formula"):
            errors.append(f"{cid}: missing formula")
        for i in c.get("inputs", []):
            if i.get("id") not in c.get("formula", ""):
                errors.append(f"{cid}: input '{i.get('id')}' not in formula")
        for o in c.get("outputs", []):
            if o.get("id") not in c.get("formula", ""):
                errors.append(f"{cid}: output '{o.get('id')}' not in formula")
    return errors


def validate_audit(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    summary = data.get("summary", {})
    if summary.get("critical", 0) > 0 or summary.get("high", 0) > 0:
        return False, f"Audit found {summary.get('critical')} critical and {summary.get('high')} high issues."
    if data.get("adsense_score", 0) < 85:
        return False, f"AdSense score {data.get('adsense_score')} < 85."
    return True, "Audit clean."


class Orchestrator:
    def __init__(self, batch: int, start_id: int, count: int, mode: str):
        self.batch = batch
        self.start_id = start_id
        self.count = count
        self.mode = mode
        self.mission_dir = MISSIONS_DIR / f"batch_{batch}"
        self.state = SharedState(self.mission_dir)
        self.harness = LLMHarness(mode=mode)

    def run(self, resume: bool = False, from_phase: str = None):
        if resume:
            current = self.state.state.get("current_phase")
            if current:
                idx = PHASES.index(current) if current in PHASES else 0
                phases = PHASES[idx:]
                print(f"Resuming from phase '{current}'...")
            else:
                phases = PHASES
        elif from_phase:
            phases = PHASES[PHASES.index(from_phase):]
        else:
            phases = PHASES

        for phase in phases:
            handler = getattr(self, f"phase_{phase}")
            self.state.set_phase(phase, "running")
            try:
                result = handler()
                if result == "pause":
                    self.state.set_phase(phase, "paused")
                    print(f"\n⏸️  Phase '{phase}' paused. Run again with --resume to continue.\n")
                    return
                self.state.set_phase(phase, "done", {"result": result})
            except Exception as e:
                self.state.set_phase(phase, "failed", {"error": str(e)})
                raise

        print(f"\n🎉 Batch {self.batch} complete!\n")

    # ── Phase: plan ────────────────────────────────────────────────────────────
    def phase_plan(self):
        print("[PLAN] Initializing batch...")
        self.state.write_json("plan.json", {
            "batch": self.batch,
            "start_id": self.start_id,
            "count": self.count,
            "end_id": self.start_id + self.count - 1,
            "mode": self.mode,
        })
        return "ok"

    # ── Phase: generate ────────────────────────────────────────────────────────
    def phase_generate(self):
        schemas_file = self.mission_dir / "schemas.json"

        # Resume check: if schemas already exist, validate and skip
        if schemas_file.exists():
            print("[GENERATE] Found existing schemas.json. Validating...")
            errors = validate_schemas(schemas_file)
            if errors:
                print("Validation failed:")
                for e in errors:
                    print(f"  - {e}")
                print("Fix schemas.json and resume, or delete it to regenerate.")
                return "pause"
            print("  Schemas valid. Skipping generation prompt.")
            return "ok"

        print("[GENERATE] Dispatching Agent Alpha (Calculator Generator)...")
        task = f"""Design {self.count} new calculators for Batch {self.batch}.
IDs must range from {self.start_id} to {self.start_id + self.count - 1}.

Steps:
1. Read {CALCS_FILE} to avoid duplicate concepts or slugs.
2. Read {AGENTS_DIR / 'generator.md'} for your full persona and rules.
3. Produce a JSON file exactly like the example in your persona.
4. Save it to: {schemas_file}

Critical:
- Every formula must be mathematically correct.
- All 6 languages must have complete i18n.
- Units with conversions must have unit_options + unit_category.
"""
        result = self.harness.dispatch(
            agent_persona_path=AGENTS_DIR / "generator.md",
            task_context=task,
            output_path=schemas_file,
            state_context=json.dumps(self.state.state, indent=2),
        )

        if result["mode"] == "manual":
            print(result["message"])
            return "pause"

        errors = validate_schemas(schemas_file)
        if errors:
            raise RuntimeError(f"Schema validation failed:\n" + "\n".join(errors))
        return "ok"

    # ── Phase: content ─────────────────────────────────────────────────────────
    def phase_content(self):
        schemas_file = self.mission_dir / "schemas.json"
        manifest_file = self.mission_dir / "content_manifest.json"
        if not schemas_file.exists():
            raise FileNotFoundError(f"schemas.json not found. Run generate phase first.")

        # Resume check: if manifest exists and all expected content files exist, skip
        if manifest_file.exists():
            with open(manifest_file, "r", encoding="utf-8") as f:
                manifest = json.load(f)
            expected = manifest.get("expected_files", [])
            missing = [p for p in expected if not Path(p).exists()]
            if not missing:
                print("[CONTENT] Content manifest found and all files present. Skipping.")
                return "ok"
            print(f"[CONTENT] Content manifest found but {len(missing)} files missing. Regenerating prompt...")

        print("[CONTENT] Dispatching Agent Beta (Content Writer)...")
        with open(schemas_file, "r", encoding="utf-8") as f:
            schemas = json.load(f)

        calc_list = "\n".join(
            f"- ID {c['id']}: {c.get('slug')} (block: {c.get('block')})"
            for c in schemas.get("calculators", [])
        )

        task = f"""Write expert-level HTML content for all calculators in Batch {self.batch}.

Schemas file: {schemas_file}
Output directory: {CONTENT_DIR}

Calculator list:
{calc_list}

Steps:
1. Read {AGENTS_DIR / 'content_writer.md'} for your full persona and rules.
2. For each calculator, read its schema to understand the concept.
3. Write 6 language versions (es, en, fr, pt, de, it) to:
   {CONTENT_DIR}/{{lang}}/calc_{{id}}.html
4. Save a manifest JSON to {manifest_file} listing every file you created.

Critical:
- NO generic boilerplate. Every sentence must be concept-specific.
- Include Common Mistakes, References, and calculator-specific FAQ.
- Minimum 400 words per language.
"""
        result = self.harness.dispatch(
            agent_persona_path=AGENTS_DIR / "content_writer.md",
            task_context=task,
            output_path=manifest_file,
            state_context=json.dumps(self.state.state, indent=2),
        )

        if result["mode"] == "manual":
            print(result["message"])
            return "pause"
        return "ok"

    # ── Phase: audit ───────────────────────────────────────────────────────────
    def phase_audit(self):
        schemas_file = self.mission_dir / "schemas.json"
        audit_file = self.mission_dir / "audit_report.json"

        # Resume check: if audit report exists, validate directly
        if audit_file.exists():
            print("[AUDIT] Found existing audit_report.json. Validating...")
            passed, msg = validate_audit(audit_file)
            if not passed:
                print(f"\n⚠️  Audit validation failed: {msg}")
                self.state.set_phase("audit", "failed", {"message": msg})
                return "pause"
            print("  Audit valid. Skipping generation prompt.")
            return "ok"

        print("[AUDIT] Dispatching Agent Gamma (Auditor)...")
        task = f"""Run a deep audit on Batch {self.batch}.

Input files:
- Schemas: {schemas_file}
- All calculators: {CALCS_FILE}
- i18n dir: {I18N_DIR}
- Content dir: {CONTENT_DIR}
- Tools config: {ROOT / 'scripts' / 'tools_config.py'}

Steps:
1. Read {AGENTS_DIR / 'auditor.md'} for your full persona and checklist.
2. Run ALL checks (math, structure, inputs, content quality, i18n, SEO).
3. Save the audit report JSON to: {audit_file}

Critical:
- Flag ANY duplicate paragraphs across content files.
- Verify every formula references all inputs and outputs.
- AdSense score must be >= 85 to pass.
"""
        result = self.harness.dispatch(
            agent_persona_path=AGENTS_DIR / "auditor.md",
            task_context=task,
            output_path=audit_file,
            state_context=json.dumps(self.state.state, indent=2),
        )

        if result["mode"] == "manual":
            print(result["message"])
            return "pause"

        passed, msg = validate_audit(audit_file)
        if not passed:
            print(f"\n⚠️  Audit failed: {msg}")
            self.state.set_phase("audit", "failed", {"message": msg})
            return "pause"
        return "ok"

    # ── Phase: fix ─────────────────────────────────────────────────────────────
    def phase_fix(self):
        print("[FIX] Evaluating audit results...")
        audit_file = self.mission_dir / "audit_report.json"
        if not audit_file.exists():
            print("No audit file found. Skipping fix.")
            return "ok"

        with open(audit_file, "r", encoding="utf-8") as f:
            audit = json.load(f)

        issues = audit.get("issues", [])
        if not issues:
            print("No issues found. Skipping fix.")
            return "ok"

        critical_high = [i for i in issues if i.get("severity") in ("critical", "high")]
        if not critical_high:
            print(f"Only {len(issues)} medium/low issues. Proceeding with build.")
            return "ok"

        fix_plan = self.mission_dir / "fix_plan.json"
        self.state.write_json("fix_plan.json", {"issues": critical_high})

        print(f"\n🔧 {len(critical_high)} critical/high issues found. Fix plan written to {fix_plan}")
        print("Action required: Review fix_plan.json, apply fixes manually or re-run generate/content for affected calculators.")
        return "pause"

    # ── Phase: build ───────────────────────────────────────────────────────────
    def phase_build(self):
        print("[BUILD] Running static site generator...")
        schemas_file = self.mission_dir / "schemas.json"

        # Merge schemas into calculators.json
        with open(CALCS_FILE, "r", encoding="utf-8") as f:
            calcs_data = json.load(f)
        with open(schemas_file, "r", encoding="utf-8") as f:
            batch_data = json.load(f)

        existing_ids = {c["id"] for c in calcs_data["calculators"]}
        new_cals = [c for c in batch_data.get("calculators", []) if c["id"] not in existing_ids]
        calcs_data["calculators"].extend(new_cals)

        with open(CALCS_FILE, "w", encoding="utf-8") as f:
            json.dump(calcs_data, f, indent=2, ensure_ascii=False)
        print(f"  Merged {len(new_cals)} calculators into {CALCS_FILE}")

        # Merge i18n
        for lang in ["es", "en", "fr", "pt", "de", "it"]:
            i18n_file = I18N_DIR / f"{lang}.json"
            with open(i18n_file, "r", encoding="utf-8") as f:
                i18n_data = json.load(f)
            calc_keys = i18n_data.setdefault("calculators", {})
            for c in new_cals:
                calc_i18n = c.get("i18n", {}).get(lang, {})
                if calc_i18n:
                    calc_keys[str(c['id'])] = calc_i18n
            with open(i18n_file, "w", encoding="utf-8") as f:
                json.dump(i18n_data, f, indent=2, ensure_ascii=False)
            print(f"  Merged i18n for {lang}")

        # Run generator
        print("  Running generate_calctowork.py...")
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "generate_calctowork.py")],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(result.stdout)
            print(result.stderr)
            raise RuntimeError("generate_calctowork.py failed")
        print("  Build complete.")
        return "ok"

    # ── Phase: deploy ──────────────────────────────────────────────────────────
    def phase_deploy(self):
        print("[DEPLOY] Deploying to Firebase...")
        result = subprocess.run(
            ["firebase", "deploy", "--only", "hosting"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(result.stderr)
            raise RuntimeError("Firebase deploy failed")
        print("  Deployed!")
        return "ok"


def main():
    parser = argparse.ArgumentParser(description="CalcToWork 3-Agent Orchestrator")
    parser.add_argument("--batch", type=int, required=True, help="Batch number (e.g., 4)")
    parser.add_argument("--start-id", type=int, default=None, help="First calculator ID")
    parser.add_argument("--count", type=int, default=50, help="Number of calculators")
    parser.add_argument("--mode", choices=["manual", "api", "subagent"], default="manual", help="LLM dispatch mode")
    parser.add_argument("--resume", action="store_true", help="Resume from last checkpoint")
    parser.add_argument("--phase", type=str, choices=PHASES, help="Start from a specific phase")
    args = parser.parse_args()

    start_id = args.start_id or get_next_id()
    orch = Orchestrator(batch=args.batch, start_id=start_id, count=args.count, mode=args.mode)
    orch.run(resume=args.resume, from_phase=args.phase)


if __name__ == "__main__":
    main()
