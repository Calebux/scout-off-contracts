#!/usr/bin/env python3
"""
One-off codemod: run all fix_* scripts in sequence.
NOT safe to re-run — do not use.
"""
import subprocess, sys

for script in ["fix_compiler_errors.py", "fix_register.py", "fix_tests.py"]:
    print(f"Running {script}...")
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)
print("All fixes applied.")
