#!/usr/bin/env python3
"""Fail closed on obvious secret material in the public REHT standards tree.

Protected research-vocabulary and derivation policy are intentionally enforced
outside this public repository. A public checker must not enumerate private
research terms, project names, architecture candidates, or other pointers that
would themselves reduce the search space for protected work.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".toml", ".tex", ".xml"}
EXCLUDE = {"scripts/ip_public_surface_gate.py"}

SECRETS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{30,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
]

violations: list[str] = []
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
        continue
    rel = path.relative_to(ROOT).as_posix()
    if rel in EXCLUDE or path.stat().st_size > 2_000_000:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for pattern in SECRETS:
        if pattern.search(text):
            violations.append(f"possible secret material: {rel}: {pattern.pattern}")

if violations:
    print("Public-surface hygiene failed:", file=sys.stderr)
    for violation in violations:
        print(f"- {violation}", file=sys.stderr)
    raise SystemExit(1)

print("public_surface_hygiene=pass")
