"""Show translation progress and the next chunks nobody has claimed.

Usage: python tools/status.py   (run from the repo root)
"""
import json
import os

SRC = os.path.join("source", "chunks")
OUT = "translations"
CLAIMS = "claims.json"


def main():
    chunks = sorted(f[:-5] for f in os.listdir(SRC) if f.endswith(".json"))
    done = {f[:-8] for f in os.listdir(OUT) if f.endswith(".fr.json")}
    claims = json.load(open(CLAIMS, encoding="utf-8")) if os.path.exists(CLAIMS) else {}
    texts = sum(len(json.load(open(os.path.join(SRC, c + ".json"), encoding="utf-8"))) for c in chunks)
    done_texts = sum(len(json.load(open(os.path.join(SRC, c + ".json"), encoding="utf-8"))) for c in done)
    print(f"chunks: {len(done)}/{len(chunks)} translated, texts: {done_texts}/{texts}")
    free = [c for c in chunks if c not in done and c not in claims]
    print("claimed, not finished:", ", ".join(c for c in chunks if c in claims and c not in done) or "-")
    print("next free chunks:", ", ".join(free[:10]) or "-")


if __name__ == "__main__":
    main()
