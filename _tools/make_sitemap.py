#!/usr/bin/env python3
"""Regenerate sitemap.xml from the pages in this repo.

lastmod is the date of the last git commit that touched each page, or
today's date if the page has uncommitted changes. Run from the repo root
before committing page changes, then run _tools/indexnow.sh after the
deploy finishes. (Folders starting with "_" are not published by GitHub Pages.)
"""
import datetime, subprocess

BASE = "https://packandnap.com"
PAGES = {"/": "index.html", "/privacy/": "privacy/index.html", "/delete-account/": "delete-account/index.html"}

def lastmod(path):
    dirty = subprocess.run(["git", "status", "--porcelain", "--", path], capture_output=True, text=True).stdout.strip()
    if dirty:
        return datetime.date.today().isoformat()
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path], capture_output=True, text=True).stdout.strip()
    return out or datetime.date.today().isoformat()

rows = "".join(f"  <url>\n    <loc>{BASE}{loc}</loc>\n    <lastmod>{lastmod(f)}</lastmod>\n  </url>\n" for loc, f in PAGES.items())
with open("sitemap.xml", "w") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "</urlset>\n")
print(open("sitemap.xml").read())
