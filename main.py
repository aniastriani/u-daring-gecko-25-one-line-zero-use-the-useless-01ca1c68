import os

# One original line, at most 200 chars: a hilariously useless superpower.
# The twist lands cold with no setup, and the short text wins ties on size.
LINE = "I can read minds, but only the minds of people trying to decide what to have for lunch."
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
