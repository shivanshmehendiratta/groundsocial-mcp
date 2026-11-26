#!/usr/bin/env python3
"""Regenerate PLATFORMS.md from the live, keyless platform list.

    python3 scripts/platforms.py > PLATFORMS.md
"""
import json
import urllib.request

URL = "https://api.groundsocial.dev/v1/platforms"
META = {"utility", "search", "tools", "prism", "contentanalysis"}

with urllib.request.urlopen(URL, timeout=60) as r:
    data = json.load(r)

plats = data["platforms"]
real = [p for p in plats if p["id"] not in META]
cross = [p for p in plats if p["id"] in META]
n_end = sum(len(p["endpoints"]) for p in plats)

print("# Platforms and endpoints\n")
print(f"Generated from `GET {URL}` (free, no key). "
      f"{len(real)} platforms plus {len(cross)} cross-platform tool groups, {n_end} endpoints in all. "
      "Status is `live` or `beta`. Credits are per call; one credit is $0.001 on the "
      "Starter pack and failed calls are refunded.\n")
print("Platform names are trademarks of their owners. Groundsocial is not affiliated with or endorsed by them.\n")


def section(title, items):
    print(f"## {title}\n")
    for p in items:
        print(f"### {p['name']} ({p['status']})\n")
        desc = p["description"].split(" Not affiliated")[0]
        print(desc + "\n")
        print("| Endpoint | MCP tool | Credits | What it returns |")
        print("| --- | --- | --- | --- |")
        for e in p["endpoints"]:
            summ = e["summary"].replace("|", "\\|")
            print(f"| `{e['method']} {e['path']}` | `{e['mcp_tool']}` | {e['credits']} | {summ} |")
        print()


section("Platforms", real)
section("Cross-platform tools", cross)
