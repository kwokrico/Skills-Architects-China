"""Backward-compatible entry point; delegates to scripts/dispatcher.py."""
import runpy
import os

if __name__ == "__main__":
    runpy.run_path(
        os.path.join(os.path.dirname(__file__), "scripts", "dispatcher.py"),
        run_name="__main__",
    )
