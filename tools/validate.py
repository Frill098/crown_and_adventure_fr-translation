"""Validate French translations against the English source chunks.

Usage:
  python tools/validate.py c001          # one chunk
  python tools/validate.py --all         # every translated chunk
Exit code 0 when everything checked is valid. Run from the repo root.
"""
import collections
import json
import os
import re
import sys

SRC = os.path.join("source", "chunks")
OUT = "translations"
# Codes the game interprets; they must survive translation unchanged.
TOKEN = re.compile(
    r"#C\([^)]*\)"            # colour start  #C(FF5AACDB)
    r"|#p\{\{.*?\}\}"         # inline icon   #p{{...}}
    r"|#[A-Za-z]"             # #n #N #r #R #Q #Y ...
    r"|\{[^{}]*\}"            # variables     {ware} {Name}
    r"|\[(?:player|Player|plyaer|Area|Goods)\]"
    r"|</?[A-Za-z]+>"         # <strong> ...
    r"|\n"
)
ENGLISH_HINT = re.compile(r"\b(the|and|you|your|with|have|this|that|will|from)\b", re.I)


def tokens(text):
    return collections.Counter(TOKEN.findall(text))


def check_chunk(name):
    src_path = os.path.join(SRC, f"{name}.json")
    out_path = os.path.join(OUT, f"{name}.fr.json")
    with open(src_path, encoding="utf-8") as fh:
        src = json.load(fh)
    if not os.path.exists(out_path):
        return [f"{name}: missing {out_path}"], []
    try:
        with open(out_path, encoding="utf-8") as fh:
            fr = json.load(fh)
    except json.JSONDecodeError as exc:
        return [f"{name}: invalid JSON: {exc}"], []
    errors, warnings = [], []
    for key, en in src.items():
        tr = fr.get(key)
        if not isinstance(tr, str) or not tr.strip():
            errors.append(f"{name}/{key}: missing or empty translation")
            continue
        if tokens(en) != tokens(tr):
            errors.append(f"{name}/{key}: codes differ EN={dict(tokens(en))} FR={dict(tokens(tr))}")
        if tr == en and len(en) > 25:
            warnings.append(f"{name}/{key}: identical to English")
        elif len(ENGLISH_HINT.findall(tr)) >= 3:
            warnings.append(f"{name}/{key}: looks untranslated: {tr[:60]!r}")
    for key in fr:
        if key not in src:
            errors.append(f"{name}/{key}: unknown ID (not in source chunk)")
    return errors, warnings


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--all":
        names = sorted(f[:-8] for f in os.listdir(OUT) if f.endswith(".fr.json"))
    else:
        names = [n.replace(".json", "") for n in sys.argv[1:]]
    all_errors = 0
    for name in names:
        errors, warnings = check_chunk(name)
        for line in errors:
            print("ERROR  ", line)
        for line in warnings:
            print("WARNING", line)
        all_errors += len(errors)
        print(f"{name}: {'OK' if not errors else f'{len(errors)} error(s)'}"
              f"{f', {len(warnings)} warning(s)' if warnings else ''}")
    sys.exit(1 if all_errors else 0)


if __name__ == "__main__":
    main()
