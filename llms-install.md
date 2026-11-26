# Installing the Groundsocial MCP server

Groundsocial is a hosted, remote MCP server. There is nothing to clone, build or install.

1. Ask the user for a Groundsocial API key (it starts with `gs_live_`). They can create one at
   https://groundsocial.dev/app/sign-in?new=1 and get 100 free credits with no card. An agent can also get a key
   on its own with `POST https://api.groundsocial.dev/v1/agent/signup`
   (see https://groundsocial.dev/docs/authentication#agent-self-signup).
2. Add this entry to the MCP settings file (for Cline: `cline_mcp_settings.json`), replacing the key:

```json
{
  "mcpServers": {
    "groundsocial": {
      "type": "streamableHttp",
      "url": "https://api.groundsocial.dev/mcp",
      "headers": { "Authorization": "Bearer gs_live_..." },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

3. Check it works by calling the free tool `utility_quickstart_get`, or `reddit_subreddit_get` with `{"name": "typescript"}`
   (1 credit).

Notes:
- Every tool is read-only and returns public data only.
- Each tool's description states its price in credits. Failed calls are refunded.
- If a client cannot use Streamable HTTP, use the stdio bridge:
  `npx -y mcp-remote https://api.groundsocial.dev/mcp --header "Authorization: Bearer gs_live_..."`.
- Do not install npm packages named `@groundsocial/...`; they are not published by Groundsocial yet.
