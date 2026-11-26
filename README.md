<img src="assets/logo.svg" width="56" alt="Groundsocial logo">

# Groundsocial MCP server

Public social and web data for your AI agent, over MCP. One key, one credit balance, 77 platforms and 580+ read-only
tools: Reddit, X, TikTok, Instagram, YouTube, LinkedIn, Bluesky, Threads, Hacker News, GitHub, Google Search, Amazon,
App Store, Google Play, Spotify, Twitch, Trustpilot, Zillow and more. Every response keeps the platform's own JSON shape
(Reddit Things and Listings, X API v2 objects, YouTube Data API resources), so there is no new schema to learn.

- Remote MCP server: `https://api.groundsocial.dev/mcp` (Streamable HTTP, OAuth 2.1 or an API key as a Bearer token)
- REST API: `https://api.groundsocial.dev/v1/<platform>/...` ([OpenAPI](https://api.groundsocial.dev/openapi.json))
- Website and docs: [groundsocial.dev](https://groundsocial.dev) · [MCP docs](https://groundsocial.dev/docs/mcp) ·
  [llms.txt](https://groundsocial.dev/llms.txt)
- Free to try: 100 credits on sign-up, no card. Listing tools needs no sign-in at all.

This repo holds the client configs, examples and registry metadata for the hosted server. The server itself runs on
our infrastructure; there is nothing to install.

## Connect

Get a key at [groundsocial.dev/app](https://groundsocial.dev/app/sign-in?new=1) (keys start with `gs_live_`), or use
OAuth in clients that support it and skip the key.

### Claude Code

```bash
# OAuth in the browser
claude mcp add --transport http groundsocial https://api.groundsocial.dev/mcp

# or with a key
claude mcp add --transport http groundsocial https://api.groundsocial.dev/mcp \
  --header "Authorization: Bearer $GROUNDSOCIAL_API_KEY"
```

### Claude Desktop and Claude.ai

Settings → Connectors → Add custom connector → `https://api.groundsocial.dev/mcp`, then sign in when asked.

For a Claude Desktop config file with a key, bridge the remote server with `mcp-remote`:

```json
{
  "mcpServers": {
    "groundsocial": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.groundsocial.dev/mcp",
        "--header",
        "Authorization: Bearer ${GROUNDSOCIAL_API_KEY}"
      ],
      "env": { "GROUNDSOCIAL_API_KEY": "gs_live_..." }
    }
  }
}
```

### Cursor

`~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "groundsocial": {
      "url": "https://api.groundsocial.dev/mcp",
      "headers": { "Authorization": "Bearer gs_live_..." }
    }
  }
}
```

Leave out `headers` to sign in with OAuth instead.

### VS Code (GitHub Copilot)

`.vscode/mcp.json`:

```json
{
  "inputs": [
    { "type": "promptString", "id": "groundsocial-key", "description": "Groundsocial API key", "password": true }
  ],
  "servers": {
    "groundsocial": {
      "type": "http",
      "url": "https://api.groundsocial.dev/mcp",
      "headers": { "Authorization": "Bearer ${input:groundsocial-key}" }
    }
  }
}
```

### Cline

`cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "groundsocial": {
      "type": "streamableHttp",
      "url": "https://api.groundsocial.dev/mcp",
      "headers": { "Authorization": "Bearer gs_live_..." }
    }
  }
}
```

### Windsurf, Zed and other clients

Any client that speaks Streamable HTTP can use the URL above with an `Authorization: Bearer <key>` header. Clients
that only speak stdio can use `npx -y mcp-remote https://api.groundsocial.dev/mcp --header "Authorization: Bearer <key>"`.
More configs are in [`examples/`](examples).

### ChatGPT

Add a connector with the URL `https://api.groundsocial.dev/mcp` and sign in when asked.

## What you can ask

Once connected, ask in plain words and the agent picks the tools:

- "Find the most discussed Reddit threads about Cursor vs Windsurf this month and summarise the complaints."
- "Get the transcript of youtube.com/watch?v=dQw4w9WgXcQ and the top 50 comments."
- "Pull the last 20 posts from @vercel on X with view counts."
- "Search TikTok for 'easy dinner recipes' and list the creators with over 100k followers."
- "What do Trustpilot reviews say about linear.app?"
- "Google 'best crm for startups' in the US and scrape the top 3 results as Markdown."

Some of the 590+ tools:

| Tool | Credits | Returns |
| --- | --- | --- |
| `reddit_search_posts` | 2 | Search posts across Reddit or in one subreddit |
| `reddit_post_get` | 1 | One post with its full comment tree |
| `x_tweet_get` | 1 | A post with author, metrics incl. views, media and top replies |
| `x_user_tweets` | 1 | The latest posts of an X account |
| `tiktok_search_videos` | 1 | TikTok videos for a keyword |
| `instagram_user_get` | 1 | A public Instagram profile |
| `youtube_video_transcript` | 2 | A video's transcript with timestamps |
| `linkedin_company_get` | 5 | A public LinkedIn company page |
| `google_search_web` | 1 | Google web results with knowledge graph and People Also Ask |
| `web_scrape_get` | 1 | Any public page as Markdown, HTML, links and metadata |
| `amazon_product_search_get` | 1 | Amazon search in 13 marketplaces |
| `search_everywhere_get` | metered | One query across Reddit, X, Bluesky, TikTok, YouTube, HN and more, merged |
| `utility_plan_get` | 0 | A task in plain words turned into a chain of calls with a cost estimate |

The full list, with every endpoint and price, is in [PLATFORMS.md](PLATFORMS.md). You can also list the tools
yourself without a key:

```bash
curl -s https://api.groundsocial.dev/mcp \
  -H 'content-type: application/json' -H 'accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

## Same data over REST

```bash
export GROUNDSOCIAL_API_KEY="gs_live_..."

# Reddit search, in Reddit's own Listing JSON
curl "https://api.groundsocial.dev/v1/reddit/search/posts?q=mcp+server&sort=top&t=month" \
  -H "Authorization: Bearer $GROUNDSOCIAL_API_KEY"

# A YouTube transcript
curl "https://api.groundsocial.dev/v1/youtube/videos/dQw4w9WgXcQ/transcript?language=en" \
  -H "Authorization: Bearer $GROUNDSOCIAL_API_KEY"

# Any web page as Markdown
curl "https://api.groundsocial.dev/v1/web/scrape?url=https://example.com&formats=markdown" \
  -H "Authorization: Bearer $GROUNDSOCIAL_API_KEY"
```

Each response carries `x-credits-charged` and `x-credits-remaining` headers. Python and TypeScript versions are in
[`examples/`](examples). `GET https://api.groundsocial.dev/v1/platforms` lists every platform, endpoint and price, free
and without a key.

## Platforms

Social: Reddit, X, TikTok, Instagram, YouTube, LinkedIn, Facebook (incl. Meta Ad Library), Threads, Bluesky, Pinterest,
Snapchat, Telegram, Truth Social, Gab, Rumble, Twitch, Kick, Kwai, Weibo, Douyin, Xiaohongshu, Cosmos.
Communities and dev: Hacker News, Stack Overflow, GitHub, npm, PyPI.
Search and web: Google (web, images, news, shopping, Maps, Patents), Google News, Google Trends, Google Ads
Transparency Center, Bing, DuckDuckGo, Baidu, Naver, Wikipedia, any web page (scrape, map, crawl), on-page SEO audit.
Commerce and reviews: Amazon, Walmart, eBay, Etsy, Target, Best Buy, IKEA, Sephora, H&M, AliExpress, idealo, Gumtree,
Trustpilot, G2, Yelp, Tripadvisor, App Store, Google Play, Steam.
Music and media: Spotify, Apple Music, SoundCloud, Goodreads.
Travel and property: Airbnb, Booking.com, Zillow, Redfin, Realtor.com, Apple Maps.
Creator pages: Linktree, Komi, Pillar, Lnk.Bio, Linkme.
Finance and public data: market quotes and statements, Polymarket, US Congress trades, Eurostat and US federal
spending, job boards (Greenhouse, Lever, Ashby, Workday).

About 30 platforms are marked `live` and the rest `beta`; [PLATFORMS.md](PLATFORMS.md) shows which.

## Pricing

Pay as you go with credit packs. No subscription, credits never expire, and failed calls are refunded in the same
request.

| Pack | Credits | Price |
| --- | --- | --- |
| Free | 100 | $0, no card |
| Starter | 10,000 | $10 |
| Builder | 60,000 | $49 |
| Scale | 350,000 | $199 |
| Volume | 2,000,000 | $799 |

One credit is one standard read; some calls cost more (Reddit search is 2, X search is 10). Every tool's price is in
its description and in [PLATFORMS.md](PLATFORMS.md). Per-key daily and monthly spend caps are available in the
dashboard. Details: [groundsocial.dev/pricing](https://groundsocial.dev/pricing).

## For agents

- [llms.txt](https://groundsocial.dev/llms.txt) and [SKILL.md](https://groundsocial.dev/SKILL.md)
- Agents can sign themselves up: `POST https://api.groundsocial.dev/v1/agent/signup` returns a key
  ([docs](https://groundsocial.dev/docs/authentication#agent-self-signup)).
- Errors say what to do next: every error has a `code`, a `hint` and a `retryable` flag.
- The `utility_*` tools are free: endpoint search, plain-words task planning and cost estimates.

## Agent skill

[`skills/groundsocial/SKILL.md`](skills/groundsocial/SKILL.md) is an Agent Skill for Claude Code, Codex and other
skill-aware agents that use the REST API instead of MCP. Copy the folder into your skills directory, for example
`~/.claude/skills/groundsocial/`.

## Notes

- Read-only, public data only. Nothing here posts, votes, follows or messages, and we never use your accounts or
  cookies.
- Platform names are trademarks of their owners. Groundsocial is not affiliated with or endorsed by them.
  See [compliance](https://groundsocial.dev/docs/compliance).
- The SDK, CLI and stdio server are not on npm yet. Don't install packages named `@groundsocial/...` from npm until
  this README links them; they are not ours.

## Support

support@groundsocial.dev, or open an issue in this repo.

## License

The configs and examples in this repo are MIT licensed. The hosted service has its own
[terms](https://groundsocial.dev/legal/terms).
