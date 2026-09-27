#!/usr/bin/env python3
"""
One-off script: inject get_diversity_config into lib.rs via regex rewriting.
NOT safe to re-run — do not use.
"""
import re, pathlib

LIB = pathlib.Path("contracts/verification/src/lib.rs")
src = LIB.read_text()
src = re.sub(r"(pub fn health)", "pub fn get_diversity_config(env: Env) -> bool { false }\n\n    \\1", src)
LIB.write_text(src)
print("patched lib.rs")
