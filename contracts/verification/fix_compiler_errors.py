#!/usr/bin/env python3
"""
One-off codemod: fix compiler errors introduced during refactor.
NOT safe to re-run — do not use.
"""
import re, pathlib

for path in pathlib.Path("src").glob("*.rs"):
    src = path.read_text()
    src = re.sub(r"use soroban_sdk::contracttype;", "use soroban_sdk::{contracttype, contract, contractimpl};", src)
    path.write_text(src)
    print(f"Fixed {path}")
