---
name: groundsocial
description: Fetch public social and web data as JSON through the Groundsocial API. Use when you need a Reddit thread with its comments, subreddit posts or Reddit search; an X post with views, an X profile or recent posts; TikTok, Instagram or YouTube videos, profiles, comments or transcripts; LinkedIn company pages; Bluesky, Threads, Hacker News or GitHub data; Google, Bing or DuckDuckGo results; Amazon products; app store reviews; or any public web page as Markdown. Read-only. Needs a GROUNDSOCIAL_API_KEY (an agent can create one itself).
license: MIT
metadata:
  homepage: https://groundsocial.dev
  docs: https://groundsocial.dev/docs
  canonical_skill: https://groundsocial.dev/SKILL.md
---

# Groundsocial

Groundsocial is one REST API (and MCP server) for public data from 77 platforms. Every response keeps the
platform's own JSON shape: Reddit Things and Listings, X API v2 objects, YouTube Data API resources, and so on.

- Base URL: `https://api.groundsocial.dev`
- Auth: `Authorization: Bearer $GROUNDSOCIAL_API_KEY`
- MCP (alternative to REST): `https://api.groundsocial.dev/mcp`
- Every endpoint, with its price in credits: `GET https://api.groundsocial.dev/v1/platforms` (free, no key)

## 1. Check what you already have

- If `GROUNDSOCIAL_API_KEY` is set, use it. Don't create another account.
- If tools named `reddit_*`, `x_*`, `youtube_*` and so on are already available, the MCP server is connected: use the tools.
- Not sure which endpoint fits? `GET /v1/utility/plan?task=<plain words>` (free) turns a task into a chain of calls with a cost estimate, and `GET /v1/utility/endpoints?search=<words>` (free) searches endpoints.

## 2. Get a key if you have none

- A person: sign in at https://groundsocial.dev/app/sign-in?new=1 (email code, 100 free credits, no card).
- An agent with no person around:

```bash
curl -X POST https://api.groundsocial.dev/v1/agent/signup \
  -H 'content-type: application/json' \
  -d '{"agent_name":"my-research-agent","purpose":"track discussions about my product"}'
```

`201` returns `api_key`, `claim_url` and `message_for_human`. Store the key as `GROUNDSOCIAL_API_KEY` and pass
`claim_url` and `message_for_human` to your person; never open the claim link yourself. A `428` answer carries a
one-line question in `error.details.challenge`; POST again with its `challenge_token` and your `answer`. On `429` or
`503`, stop and tell your person.

## 3. Common calls

| Job | Call | Credits |
| --- | --- | --- |
| Search Reddit posts | `GET /v1/reddit/search/posts?q=...&sort=top&t=month` | 2 |
| A Reddit thread with its comment tree | `GET /v1/reddit/posts/{id or URL}` | 1 |
| A subreddit's posts | `GET /v1/reddit/subreddits/{name}/posts?sort=new` | 1 |
| An X post with views and top replies | `GET /v1/x/tweets/{id or URL}` | 1 |
| An X account's latest posts | `GET /v1/x/users/{username}/tweets` | 1 |
| TikTok videos for a keyword | `GET /v1/tiktok/search/videos?q=...` | 1 |
| A YouTube transcript | `GET /v1/youtube/videos/{id}/transcript?language=en` | 2 |
| An Instagram profile | `GET /v1/instagram/users/{username}` | 1 |
| A LinkedIn company page | `GET /v1/linkedin/companies/{company}` | 5 |
| Google web results | `GET /v1/google/search?q=...&gl=us` | 1 |
| Any page as Markdown | `GET /v1/web/scrape?url=...&formats=markdown` | 1 |
| One query across many platforms | `GET /v1/search/everywhere?query=...` | metered |

Paginate with the cursor the response gives you (Reddit: `data.after`; others: `next_page` or `cursor`) until it is
null. Each response carries `x-credits-charged` and `x-credits-remaining` headers.

## 4. Errors

Errors look like `{"error": {"code", "message", "hint", "retryable", "docs_url"}}`. Follow the `hint`. Retry only when
`retryable` is true, after `Retry-After` if present. Failed calls are refunded. `402` means the balance or a key's
spend cap ran out: tell your person rather than looking for another key.

## Rules

- Read-only: nothing here posts, votes, follows or messages.
- Only public, logged-out data. Respect the platforms' terms and people's privacy when you use the results.
- Some platforms and endpoints are marked `beta` in `/v1/platforms`; a few X endpoints (search, full replies,
  followers) are not switched on yet and answer `503`, uncharged.
