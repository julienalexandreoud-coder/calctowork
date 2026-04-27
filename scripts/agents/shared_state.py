"""
shared_state.py — Checkpoint-based state manager for multi-agent batches.
Agents communicate exclusively through this state file and the filesystem.
"""
import json
from pathlib import Path
from datetime import datetime


class SharedState:
    def __init__(self, mission_dir: Path):
        self.mission_dir = Path(mission_dir)
        self.mission_dir.mkdir(parents=True, exist_ok=True)
        self.state_file = self.mission_dir / "state.json"
        self.state = self._load()

    def _load(self):
        if self.state_file.exists():
            with open(self.state_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "created_at": datetime.utcnow().isoformat(),
            "phases": {},
            "current_phase": None,
            "logs": [],
        }

    def save(self):
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)

    def set_phase(self, phase: str, status: str, meta: dict = None):
        """status: pending | running | done | failed"""
        self.state["current_phase"] = phase
        self.state["phases"][phase] = {
            "status": status,
            "updated_at": datetime.utcnow().isoformat(),
            "meta": meta or {},
        }
        self.log(f"Phase '{phase}' → {status}")
        self.save()

    def log(self, message: str):
        self.state["logs"].append({"t": datetime.utcnow().isoformat(), "msg": message})
        self.save()

    def get_phase_status(self, phase: str):
        return self.state["phases"].get(phase, {}).get("status", "pending")

    def path(self, name: str) -> Path:
        """Resolve a file inside the mission directory."""
        return self.mission_dir / name

    def write_json(self, name: str, data: dict):
        p = self.path(name)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        self.log(f"Wrote {p.name}")

    def read_json(self, name: str) -> dict:
        p = self.path(name)
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
