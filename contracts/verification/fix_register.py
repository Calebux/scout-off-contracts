#!/usr/bin/env python3
"""
One-off codemod: patch register_validator signature after type refactor.
NOT safe to re-run — do not use.
"""
import re, pathlib

LIB = pathlib.Path("src/lib.rs")
src = LIB.read_text()
src = re.sub(
    r"pub fn register_validator\(env: Env, wallet: Address\)",
    "pub fn register_validator(env: Env, wallet: Address, credentials: String)",
    src,
)
LIB.write_text(src)
print("register_validator signature patched")
