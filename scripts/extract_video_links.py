#!/usr/bin/env python3
"""Extract and deduplicate video links from a Markdown file or directory."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

URL_RE = re.compile(r"https?://[^\s<>\]\)\"']+")
VIDEO_HOSTS = (
    "douyin.com", "iesdouyin.com", "tiktok.com", "xiaohongshu.com",
    "xhslink.com", "bilibili.com", "b23.tv", "kuaishou.com", "weibo.com",
)


def markdown_files(source: Path):
    if source.is_file():
        if source.suffix.lower() != ".md":
            raise ValueError(f"Not a Markdown file: {source}")
        yield source
        return
    if not source.is_dir():
        raise FileNotFoundError(source)
    yield from sorted(source.rglob("*.md"))


def clean_url(url: str) -> str:
    return url.rstrip(".,;:!?，。；：！？）】》")


def extract(source: Path, include_all: bool):
    seen = set()
    results = []
    for path in markdown_files(source):
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for raw in URL_RE.findall(line):
                url = clean_url(raw)
                if not include_all and not any(host in url.lower() for host in VIDEO_HOSTS):
                    continue
                if url in seen:
                    continue
                seen.add(url)
                results.append({
                    "id": len(results) + 1,
                    "url": url,
                    "source_file": str(path),
                    "line": line_no,
                    "context": line.strip()[:500],
                })
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Markdown file or directory")
    parser.add_argument("--all-links", action="store_true", help="Include non-video URLs")
    parser.add_argument("--format", choices=("json", "tsv"), default="json")
    args = parser.parse_args()
    rows = extract(args.source.expanduser().resolve(), args.all_links)
    if args.format == "json":
        print(json.dumps({"count": len(rows), "links": rows}, ensure_ascii=False, indent=2))
    else:
        print("id\turl\tsource_file\tline\tcontext")
        for row in rows:
            values = [str(row[key]).replace("\t", " ") for key in ("id", "url", "source_file", "line", "context")]
            print("\t".join(values))


if __name__ == "__main__":
    main()

