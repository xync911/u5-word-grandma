"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one word and nothing else: the single word our
grandma would text about AI, at most 30 characters.
Witchcraft: the word a grandma reaches for when a machine talks
back, writes poems, and knows her birthday. One word, one
generation gap, and the whole joke is in the spelling.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
