"""Emit the fixed entry as exact UTF-8 bytes, with no trailing newline.

Psithurism is a rare, vivid sound-image: its sibilants whisper like wind
through leaves, making the word itself echo the experience it names.
"""
from pathlib import Path


WORD = "psithurism"

if not isinstance(WORD, str) or not 1 <= len(WORD) <= 24 or any(
    character.isspace() for character in WORD
):
    raise ValueError("entry must be a 1-24 character word with no whitespace")

output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_bytes(WORD.encode("utf-8"))
