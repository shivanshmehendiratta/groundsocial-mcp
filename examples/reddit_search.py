"""Search Reddit and print the top threads with their comment counts.

    pip install requests
    export GROUNDSOCIAL_API_KEY=gs_live_...
    python reddit_search.py "mcp server"
"""
import os
import sys

import requests

API = "https://api.groundsocial.dev"
headers = {"Authorization": f"Bearer {os.environ['GROUNDSOCIAL_API_KEY']}"}

q = sys.argv[1] if len(sys.argv) > 1 else "mcp server"
res = requests.get(
    f"{API}/v1/reddit/search/posts",
    params={"q": q, "sort": "top", "t": "month", "limit": 10},
    headers=headers,
    timeout=60,
)
res.raise_for_status()

# Reddit's own Listing shape: data.children[].data
for child in res.json()["data"]["children"]:
    post = child["data"]
    print(f"{post['score']:>6}  {post['num_comments']:>5} comments  r/{post['subreddit']}  {post['title']}")

print("credits left:", res.headers.get("x-credits-remaining"))
