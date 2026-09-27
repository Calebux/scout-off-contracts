#!/usr/bin/env python3
"""
One-off codemod: update test files to use new error enum variants.
NOT safe to re-run — do not use.
"""
import re, pathlib

for path in pathlib.Path(".").glob("**/*.rs"):
    src = path.read_text()
    if "VerificationError::NotFound" in src:
        src = src.replace("VerificationError::NotFound", "VerificationError::ValidatorNotFound")
        path.write_text(src)
        print(f"Patched {path}")
