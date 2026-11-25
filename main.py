import os


def build_entry():
    parts = [
        "Day 47: he said 'just fix it' like 'it' was one thing.",
        "I fixed seven things.",
        "He meant the eighth, which he has never once described.",
    ]
    return " ".join(parts)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    entry = build_entry()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
