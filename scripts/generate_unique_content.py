#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate truly unique, high-quality HTML content for each calculator using Claude Haiku via REST API.
Each calculator gets custom content based on its specific inputs, outputs, and domain.
Run: py scripts/generate_unique_content.py [--dry-run] [--start-id NNN]
"""
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).parent.parent
CALC_DIR = ROOT / "src" / "calculators"
LANGS = ["en", "es", "de", "fr", "it", "pt"]

API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not API_KEY:
    print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
    sys.exit(1)

SYSTEM_PROMPT = """You are an expert technical writer creating HTML content for calculator tools.
Generate concise, practical, domain-specific content that explains how to use a specific calculator.

Requirements:
- Return ONLY the HTML content between <section class="long-content"> tags (inclusive)
- Structure: intro paragraph, how-it-works explanation, step-by-step guide, formula explanation, FAQs
- Use the specific input/output field names provided
- Reference the actual formula if given
- Include relevant examples and practical use cases
- Keep tone professional but accessible
- FAQ items should use format: <div class="faq-item"><button class="faq-q" aria-expanded="false">Q?</button><div class="faq-a"><p>A</p></div></div>
- Escape HTML special characters appropriately
- No markdown, only HTML tags"""


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"  [ERROR reading {path}]: {e}")
        return {}


def get_language_name(lang: str) -> str:
    names = {"en": "English", "es": "Spanish", "de": "German", "fr": "French", "it": "Italian", "pt": "Portuguese"}
    return names.get(lang, lang)


def build_prompt(calc_id: str, lang: str, calc_data: dict, lang_data: dict) -> str:
    name = lang_data.get("name", calc_data.get("slug", "Calculator"))
    desc = lang_data.get("desc") or lang_data.get("seo_description", "")
    inputs = lang_data.get("inputs", {})
    outputs = lang_data.get("outputs", {})
    example = lang_data.get("example_label", "")
    formula = lang_data.get("formula_display", "")
    mistakes = lang_data.get("mistakes", [])
    block_slug = calc_data.get("block_slug", "")

    inputs_text = "\n".join(f"- {k}: {v}" for k, v in list(inputs.items())[:6])
    outputs_text = "\n".join(f"- {k}: {v}" for k, v in list(outputs.items())[:4])
    mistakes_text = "\n".join(f"- {m}" for m in mistakes[:3]) if mistakes else "(None)"

    prompt = f"""Create HTML content for this calculator:

**Calculator Details:**
- ID: {calc_id}
- Name: {name}
- Description: {desc}
- Domain/Block: {block_slug}

**Input Fields:**
{inputs_text}

**Output Fields:**
{outputs_text}

**Formula/Calculation:**
{formula if formula else "(Not provided)"}

**Example Use Case:**
{example if example else "(Not provided)"}

**Common Mistakes:**
{mistakes_text}

**Content Requirements:**
1. Write in {get_language_name(lang)}
2. Create an engaging intro paragraph explaining what this calculator does
3. Provide a "How it works" section explaining the calculation
4. Create 5-6 step-by-step instructions using the actual input field names
5. Explain the formula in simple terms
6. Add 3-4 relevant FAQs
7. Keep content concise (400-600 words total)

Return ONLY the HTML section with no extra text."""
    return prompt


def generate_content(calc_id: str, lang: str, calc_data: dict, lang_data: dict) -> str:
    """Generate HTML using Claude Haiku REST API."""
    prompt = build_prompt(calc_id, lang, calc_data, lang_data)

    payload = {
        "model": "claude-3-5-haiku-20241022",
        "max_tokens": 1500,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "x-api-key": API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
        )
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result.get("content", [{}])[0].get("text", "")
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"    [API ERROR {e.code}]: {error_body[:100]}")
        return ""
    except Exception as e:
        print(f"    [ERROR]: {e}")
        return ""


def process_calculator(calc_dir: Path, dry_run: bool = False) -> int:
    calc_data = load_json(calc_dir / "calc.json")
    if not calc_data:
        return 0

    calc_id = calc_data.get("id", calc_dir.name)
    written = 0

    for lang in LANGS:
        lang_data = load_json(calc_dir / f"{lang}.json")
        if not lang_data:
            continue

        html = generate_content(calc_id, lang, calc_data, lang_data)
        if not html.strip():
            continue

        if not dry_run:
            out_path = calc_dir / f"{lang}.html"
            out_path.write_text(html, encoding="utf-8")

        written += 1

    return written


def main() -> None:
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    start_id = 1

    if "--start-id" in args:
        idx = args.index("--start-id")
        if idx + 1 < len(args):
            try:
                start_id = int(args[idx + 1])
            except ValueError:
                pass

    if not CALC_DIR.exists():
        print(f"ERROR: {CALC_DIR} not found.")
        sys.exit(1)

    if dry_run:
        print("DRY RUN MODE\n")

    total_calcs = total_files = 0
    calc_dirs = sorted(d for d in CALC_DIR.iterdir() if d.is_dir())

    print(f"Generating content for {len(calc_dirs)} calculators...")

    for i, calc_dir in enumerate(calc_dirs, 1):
        try:
            calc_id_int = int(calc_dir.name)
            if calc_id_int < start_id:
                continue
        except ValueError:
            pass

        n = process_calculator(calc_dir, dry_run)
        if n > 0:
            total_calcs += 1
            total_files += n
            status = "[DRY]" if dry_run else "[OK]"
            print(f"{status} {calc_dir.name:3s} — {n} files")

            if i % 50 == 0:
                print(f"  Progress: {total_calcs} calcs, {total_files} files...")

    print()
    label = "would generate" if dry_run else "generated"
    print(f"DONE. {label} {total_files} files for {total_calcs} calculators.")


if __name__ == "__main__":
    main()
