#!/usr/bin/env python3
"""Batch-rename image files in a folder.

Example:
    python rename.py ./photos trip --prefix trip --dry-run
"""

import argparse
from pathlib import Path

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def collect(folder):
    return sorted(
        path for path in folder.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    )


def main():
    parser = argparse.ArgumentParser(description="Batch rename images")
    parser.add_argument("folder", type=Path)
    parser.add_argument("prefix", nargs="?", default="image")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = collect(args.folder)
    if not files:
        print("no images found")
        return

    for index, path in enumerate(files, 1):
        target = args.folder / f"{args.prefix}-{index:03d}{path.suffix.lower()}"
        if args.dry_run:
            print(f"{path.name} -> {target.name}")
        else:
            path.rename(target)
            print(f"renamed {path.name} -> {target.name}")


if __name__ == "__main__":
    main()
