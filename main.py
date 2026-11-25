#!/usr/bin/env python3
"""bew: smallest possible entry courier.

Reads the sibling entry.txt, enforces the 1..24 gate, drops the line in
$MAKEFUN_OUTPUT_DIR (or ./out) and reports what happened as JSON.
"""

import json
import os
from pathlib import Path

GATE_HI = 24
GATE_LO = 1


def courier():
    src = Path(__file__).resolve().parent / "entry.txt"
    try:
        all_text = src.read_text(encoding="utf-8")
    except OSError as oops:
        print(json.dumps({"sent": False, "oops": str(oops)}))
        return 2
    picked = ""
    for each in all_text.replace("\r\n", "\n").split("\n"):
        if each.strip():
            picked = each
            break
    size = len(picked)
    if not (GATE_LO <= size <= GATE_HI) or not picked.strip():
        print(json.dumps({"sent": False, "size": size, "hi": GATE_HI}))
        return 1
    home = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    home.mkdir(parents=True, exist_ok=True)
    (home / "entry.txt").write_text(picked, encoding="utf-8", newline="\n")
    print(json.dumps({"sent": True, "size": size}))
    return 0


if __name__ == "__main__":
    raise SystemExit(courier())
