#!/usr/bin/env python3
"""Refresh the local solution archive and print a factual progress inventory."""
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "Git command failed")
    return result.stdout


def main():
    if git("status", "--porcelain").strip():
        raise RuntimeError("Checkout has uncommitted changes. Preserve or finish them before refreshing; nothing was changed.")
    refresh = git("pull", "--ff-only").strip()
    paths = git("ls-files", "-z").split("\0")
    problems = {}
    for path in paths:
        if not re.search(r"/submission-\d+\.[A-Za-z0-9]+$", path):
            continue
        parent, filename = path.rsplit("/", 1)
        record = problems.setdefault(parent, {"problem_path": parent, "submission_files": 0, "extensions": set()})
        record["submission_files"] += 1
        record["extensions"].add(filename.rsplit(".", 1)[1])
    inventory = []
    for parent in sorted(problems):
        record = problems[parent]
        record["extensions"] = sorted(record["extensions"])
        inventory.append(record)
    latest = []
    for line in git("log", "-10", "--format=%H%x09%cI%x09%s").splitlines():
        sha, synced_at, message = line.split("\t", 2)
        latest.append({"commit": sha, "synced_at": synced_at, "message": message})
    print(json.dumps({
        "repository": "algorithmsareforsuckers/neetcode-submissions",
        "refresh": refresh,
        "head": git("rev-parse", "HEAD").strip(),
        "unique_problem_paths": len(inventory),
        "submission_files": sum(x["submission_files"] for x in inventory),
        "date_note": "Commit timestamps are sync times. Native exports do not preserve original solve dates.",
        "coverage_note": "Counts describe currently exported files. An incomplete backfill or failed sync can omit solved problems.",
        "problems": inventory,
        "recent_commits": latest,
    }, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError) as error:
        print(f"Refresh failed: {error}", file=sys.stderr)
        sys.exit(1)
