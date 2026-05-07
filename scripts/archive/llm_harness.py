"""
llm_harness.py — Abstraction layer for dispatching prompts to LLMs.
Supports manual (file-based), API, and future subagent modes.
"""
import os
import sys
import json
from pathlib import Path
from typing import Literal, Optional

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except AttributeError:
    pass

Mode = Literal["manual", "api", "subagent"]


class LLMHarness:
    def __init__(self, mode: Mode = "manual", api_key: Optional[str] = None):
        self.mode = mode
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("OPENAI_API_KEY")
        if self.mode == "api" and not self.api_key:
            raise RuntimeError("API mode requested but no ANTHROPIC_API_KEY or OPENAI_API_KEY found.")

    def dispatch(
        self,
        agent_persona_path: Path,
        task_context: str,
        output_path: Path,
        state_context: Optional[str] = None,
    ) -> dict:
        """
        Dispatches a task to an LLM.
        Returns a result dict with keys:
          - mode: how it was handled
          - prompt_file: path to generated prompt (manual mode)
          - output_file: expected output path
          - message: human-readable instruction
        """
        persona = agent_persona_path.read_text(encoding="utf-8")
        full_prompt = self._build_prompt(persona, task_context, state_context)

        if self.mode == "manual":
            return self._handle_manual(full_prompt, output_path, agent_persona_path.stem)

        if self.mode == "api":
            return self._handle_api(full_prompt, output_path)

        if self.mode == "subagent":
            return self._handle_subagent(full_prompt, output_path)

        raise ValueError(f"Unknown mode: {self.mode}")

    def _build_prompt(self, persona: str, task_context: str, state_context: Optional[str]) -> str:
        parts = [persona, "\n---\n", "# TASK\n", task_context]
        if state_context:
            parts.extend(["\n---\n", "# SHARED STATE\n", state_context])
        parts.append("\n---\n# INSTRUCTIONS\nProduce the requested output exactly as specified. Do not add conversational filler. Write only the required artifacts.\n")
        return "".join(parts)

    def _handle_manual(self, prompt: str, output_path: Path, agent_name: str) -> dict:
        prompt_file = output_path.parent / f"{agent_name}_prompt.md"
        prompt_file.write_text(prompt, encoding="utf-8")
        return {
            "mode": "manual",
            "prompt_file": str(prompt_file),
            "output_file": str(output_path),
            "message": (
                f"\n🤖 MANUAL MODE: Agent '{agent_name}' needs execution.\n"
                f"   Prompt file: {prompt_file}\n"
                f"   Expected output: {output_path}\n"
                f"   Action: Feed the prompt to an LLM and save the output to the expected path.\n"
            ),
        }

    def _handle_api(self, prompt: str, output_path: Path) -> dict:
        # Placeholder for actual API integration
        # When implemented, this calls anthropic.Client() or openai.Client()
        raise NotImplementedError("API mode is not yet implemented. Please use manual mode or set up API keys and implement _handle_api.")

    def _handle_subagent(self, prompt: str, output_path: Path) -> dict:
        # Placeholder for subprocess-based agent dispatch (e.g., claude -p)
        raise NotImplementedError("Subagent mode is not yet implemented.")
