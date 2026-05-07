#!/usr/bin/env python3
"""
run_batch_agents.py — Convenience wrapper for the 3-agent orchestrator.

Usage:
  # Start a new batch (auto-detect next ID)
  python scripts/run_batch_agents.py --batch 4

  # Specify exact ID range
  python scripts/run_batch_agents.py --batch 4 --start-id 1050 --count 50

  # Resume a paused batch
  python scripts/run_batch_agents.py --batch 4 --resume

  # Start from a specific phase
  python scripts/run_batch_agents.py --batch 4 --phase content

  # Auto mode (requires API keys)
  python scripts/run_batch_agents.py --batch 4 --mode api
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
ORCHESTRATOR = ROOT / "scripts" / "orchestrator.py"


def main():
    parser = argparse.ArgumentParser(description="Run a CalcToWork batch via 3 LLM agents")
    parser.add_argument("--batch", type=int, required=True, help="Batch number")
    parser.add_argument("--start-id", type=int, default=None, help="First calculator ID")
    parser.add_argument("--count", type=int, default=50, help="Number of calculators")
    parser.add_argument("--mode", choices=["manual", "api", "subagent"], default="manual")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--phase", type=str, default=None, help="Start from phase")
    args = parser.parse_args()

    cmd = [
        sys.executable,
        str(ORCHESTRATOR),
        "--batch", str(args.batch),
        "--count", str(args.count),
        "--mode", args.mode,
    ]
    if args.start_id is not None:
        cmd.extend(["--start-id", str(args.start_id)])
    if args.resume:
        cmd.append("--resume")
    if args.phase:
        cmd.extend(["--phase", args.phase])

    print("=" * 60)
    print(f"🚀 CalcToWork 3-Agent Batch Runner")
    print(f"   Batch:    {args.batch}")
    print(f"   Count:    {args.count}")
    print(f"   Mode:     {args.mode}")
    print(f"   Resume:   {args.resume}")
    print(f"   Phase:    {args.phase or 'auto'}")
    print("=" * 60)
    print()

    subprocess.run(cmd)


if __name__ == "__main__":
    main()
