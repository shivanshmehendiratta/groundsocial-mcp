#!/usr/bin/env sh
# List every tool on the hosted MCP server. No key needed.
curl -s https://api.groundsocial.dev/mcp \
  -H 'content-type: application/json' \
  -H 'accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' |
  python3 -c 'import json,sys; [print(t["name"]) for t in json.load(sys.stdin)["result"]["tools"]]'
