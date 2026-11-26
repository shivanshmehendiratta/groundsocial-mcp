# Platforms and endpoints

Generated from `GET https://api.groundsocial.dev/v1/platforms` (free, no key). 77 platforms plus 5 cross-platform tool groups, 589 endpoints in all. Status is `live` or `beta`. Credits are per call; one credit is $0.001 on the Starter pack and failed calls are refunded.

Platform names are trademarks of their owners. Groundsocial is not affiliated with or endorsed by them.

## Platforms

### Reddit (live)

Public subreddits, posts with their comment trees, users and search, in Reddit’s own Thing and Listing JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/reddit/subreddits/{name}` | `reddit_subreddit_get` | 1 | A subreddit: description, rules, member count, flags. |
| `GET /v1/reddit/subreddits/{name}/posts` | `reddit_subreddit_posts` | 1 | Posts in a subreddit, by hot, new, top, rising or controversial. |
| `GET /v1/reddit/posts/{id}` | `reddit_post_get` | 1 | One post with its full comment tree. |
| `POST /v1/reddit/posts/{id}/more` | `reddit_post_comments` | 1 | Comments on a post, paginated, with "more" threads expanded. |
| `GET /v1/reddit/users/{name}` | `reddit_user_get` | 1 | A public user profile: karma, age, flags. |
| `GET /v1/reddit/users/{name}/posts` | `reddit_user_posts` | 1 | Posts a user submitted. |
| `GET /v1/reddit/users/{name}/comments` | `reddit_user_comments` | 1 | Comments a user wrote. |
| `GET /v1/reddit/search/posts` | `reddit_search_posts` | 2 | Search posts across Reddit or in one subreddit. |
| `GET /v1/reddit/search/subreddits` | `reddit_search_subreddits` | 1 | Find subreddits by name or topic. |
| `GET /v1/reddit/subreddits/{name}/rules` | `reddit_subreddit_rules` | 1 | A subreddit's posting rules, plus Reddit's site-wide rules. |
| `GET /v1/reddit/subreddits/{name}/widgets` | `reddit_subreddit_widgets` | 1 | A subreddit's sidebar widgets: rules, flairs, bookmarks, related communities, events, text. |
| `GET /v1/reddit/subreddits/{name}/sidebar` | `reddit_subreddit_sidebar` | 1 | A subreddit's old-style sidebar text (its about description). |
| `GET /v1/reddit/subreddits/{name}/wiki` | `reddit_subreddit_wiki` | 1 | A page of a subreddit's wiki: rendered HTML, markdown source, last revision. |
| `GET /v1/reddit/subreddits/{name}/comments` | `reddit_subreddit_comments` | 1 | The newest comments across a whole subreddit. |
| `POST /v1/reddit/subreddits/batch` | `reddit_subreddit_batch` | 5 | Up to 25 subreddits in one call, by name. |
| `GET /v1/reddit/subreddit-directories/{where}` | `reddit_subreddits_directory` | 1 | Reddit's community directories: popular, new or default subreddits. |
| `GET /v1/reddit/posts/{id}/duplicates` | `reddit_post_duplicates` | 1 | Other discussions: every other submission of the link a post shares, and crossposts. |
| `GET /v1/reddit/posts/{id}/transcript` | `reddit_post_transcript` | 2 | A video post's captions: WebVTT, plain text and timed segments. |
| `GET /v1/reddit/posts/{id}/thread` | `reddit_post_thread` | 5 | A post's full comment tree with collapsed replies read in. |
| `GET /v1/reddit/posts/{id}/visibility` | `reddit_post_visibility` | 2 | Whether a post is still publicly visible or quietly removed. |
| `POST /v1/reddit/posts/batch` | `reddit_post_batch` | 5 | Up to 25 posts in one call, by id. |
| `GET /v1/reddit/posts/{id}/comments/{comment}` | `reddit_comment_get` | 1 | One comment, by post and comment id. |
| `POST /v1/reddit/comments/verify` | `reddit_comment_verify` | 5 | Whether up to 25 comments are still live, deleted or removed. |
| `GET /v1/reddit/users/{name}/overview` | `reddit_user_overview` | 1 | A user's posts and comments together, newest first. |
| `GET /v1/reddit/users/{name}/trophies` | `reddit_user_trophies` | 1 | A user's public trophies. |
| `GET /v1/reddit/search/comments` | `reddit_search_comments` | 2 | Search comments across Reddit or in one subreddit: the comments themselves, with their post. |
| `GET /v1/reddit/search/users` | `reddit_search_users` | 1 | Find users by name. |
| `GET /v1/reddit/search/media` | `reddit_search_media` | 2 | Search image, video and gallery posts. |
| `GET /v1/reddit/search/typeahead` | `reddit_search_typeahead` | 1 | Search-as-you-type: query suggestions and communities, or post titles in one subreddit. |
| `GET /v1/reddit/search/omni` | `reddit_search_omni` | 5 | One keyword across Reddit: posts, top comments of the leading threads, and the communities they come from. |
| `GET /v1/reddit/political-ads` | `reddit_ads_political` | 1 | Reddit's political ad disclosures, parsed: advertiser, spend, impressions, targeting, dates. |

### X (live)

Public posts (tweets) with view counts and top replies, profiles and recent timelines, in the shape of X’s own v2 Tweet and User objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/x/tweets/{id}` | `x_tweet_get` | 1 | One post (tweet) with its author, metrics incl. views, media, quoted post and top replies. |
| `GET /v1/x/users/{username}` | `x_user_get` | 1 | A public X profile: bio, follower and post counts, verification, pinned post. |
| `GET /v1/x/users/{username}/tweets` | `x_user_tweets` | 1 | The latest posts of an X account, newest first (about 20). |
| `GET /v1/x/users/{username}/tweets/next` | `x_user_tweets_next` | 2 | The next page of an X account’s posts, from a next_token (beta). |
| `GET /v1/x/search/tweets` | `x_search_tweets` | 10 | Search recent X posts with X’s search operators (needs logged-in sessions). |
| `GET /v1/x/tweets/{id}/replies` | `x_tweet_replies` | 5 | Replies to an X post, paginated (needs logged-in sessions). |
| `GET /v1/x/users/{username}/followers` | `x_user_followers` | 10 | Accounts that follow an X account, paginated (needs logged-in sessions). |
| `GET /v1/x/tweets/{id}/transcript` | `x_tweet_transcript` | 2 | The transcript of the video in an X post, from the captions X serves with it. |
| `GET /v1/x/communities/{id}` | `x_community_get` | 1 | An X community: name, description, members, rules, creator. |
| `GET /v1/x/communities/{id}/tweets` | `x_community_tweets` | 1 | The top or media posts of an X community (one page). |
| `GET /v1/x/search/users` | `x_search_users` | 1 | X accounts matching a name, handle or keyword, paginated. |
| `GET /v1/x/users/{username}/full` | `x_user_full` | 2 | An X profile with its latest posts and engagement stats computed from them. |
| `GET /v1/x/users/{username}/highlights` | `x_user_highlights` | 1 | The posts an X account highlights on its profile, paginated. |
| `GET /v1/x/trends/tweets` | `x_trends_tweets` | 1 | The posts trending on X today. |

### Bluesky (live)

Public Bluesky profiles, posts and threads, followers, likes, reposts, quotes, search, custom feeds, lists, starter packs and trends, in the AT Protocol’s own app.bsky lexicon JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/bluesky/profiles/{actor}` | `bluesky_profile_get` | 1 | A public Bluesky profile: bio, follower, follow and post counts, pinned post. |
| `GET /v1/bluesky/profiles` | `bluesky_profile_batch` | 2 | Up to 25 Bluesky profiles in one call. |
| `GET /v1/bluesky/profiles/{actor}/posts` | `bluesky_user_posts` | 1 | A Bluesky account’s posts and reposts, newest first, with filters and a date window. |
| `GET /v1/bluesky/profiles/{actor}/followers` | `bluesky_user_followers` | 1 | Accounts that follow a Bluesky account, paginated. |
| `GET /v1/bluesky/profiles/{actor}/follows` | `bluesky_user_follows` | 1 | Accounts a Bluesky account follows, paginated. |
| `GET /v1/bluesky/profiles/{actor}/feeds` | `bluesky_user_feeds` | 1 | Custom feeds a Bluesky account created. |
| `GET /v1/bluesky/profiles/{actor}/lists` | `bluesky_user_lists` | 1 | Curation and moderation lists a Bluesky account created. |
| `GET /v1/bluesky/profiles/{actor}/starter-packs` | `bluesky_user_starter_packs` | 1 | Starter packs a Bluesky account created. |
| `GET /v1/bluesky/profiles/{actor}/similar` | `bluesky_user_similar` | 1 | Accounts Bluesky suggests alongside a given account. |
| `GET /v1/bluesky/handles/{handle}` | `bluesky_handle_resolve` | 1 | The permanent DID behind a Bluesky handle. |
| `GET /v1/bluesky/post` | `bluesky_post_get` | 1 | One Bluesky post with its author, media and like, repost, reply and quote counts. |
| `GET /v1/bluesky/posts` | `bluesky_posts_batch` | 2 | Up to 25 Bluesky posts in one call. |
| `GET /v1/bluesky/post/thread` | `bluesky_post_thread` | 1 | A Bluesky post with its parent chain and nested replies. |
| `GET /v1/bluesky/post/likes` | `bluesky_post_likes` | 1 | Accounts that liked a Bluesky post, paginated. |
| `GET /v1/bluesky/post/reposts` | `bluesky_post_reposts` | 1 | Accounts that reposted a Bluesky post, paginated. |
| `GET /v1/bluesky/post/quotes` | `bluesky_post_quotes` | 1 | Posts quoting a Bluesky post, paginated. |
| `GET /v1/bluesky/search/posts` | `bluesky_search_posts` | 1 | Search Bluesky posts by text, author, language, date, domain or hashtag. |
| `GET /v1/bluesky/search/users` | `bluesky_search_users` | 1 | Search Bluesky accounts by name, handle or bio. |
| `GET /v1/bluesky/search/starter-packs` | `bluesky_search_starter_packs` | 1 | Search Bluesky starter packs. |
| `GET /v1/bluesky/feed` | `bluesky_feed_get` | 1 | A Bluesky custom feed’s details: name, creator, likes. |
| `GET /v1/bluesky/feed/posts` | `bluesky_feed_posts` | 1 | The posts in a Bluesky custom feed, paginated. |
| `GET /v1/bluesky/feeds/popular` | `bluesky_feeds_popular` | 1 | The most liked Bluesky custom feeds, optionally by keyword. |
| `GET /v1/bluesky/list` | `bluesky_list_get` | 1 | A Bluesky list and its members, paginated. |
| `GET /v1/bluesky/list/posts` | `bluesky_list_posts` | 1 | Recent posts from the members of a Bluesky list. |
| `GET /v1/bluesky/starter-pack` | `bluesky_starter_pack_get` | 1 | A Bluesky starter pack: its members sample, feeds and join counts. |
| `GET /v1/bluesky/trends` | `bluesky_trends_get` | 1 | What is trending on Bluesky now, with post counts. |
| `GET /v1/bluesky/trends/topics` | `bluesky_trends_topics` | 1 | Bluesky’s trending topics list. |

### Hacker News (beta)

Hacker News stories, comments, feeds, users and full-text search, from Hacker News’s own public APIs, in their own item and search-hit shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/hackernews/search` | `hackernews_search_stories` | 1 | Search Hacker News stories or comments, by relevance or date. |
| `GET /v1/hackernews/stories` | `hackernews_stories_get` | 1 | A Hacker News feed: top, new, best, ask, show or job. |
| `GET /v1/hackernews/items/{id}` | `hackernews_story_get` | 1 | One Hacker News item: story, comment, job or poll. |
| `GET /v1/hackernews/items/{id}/comments` | `hackernews_story_comments` | 1 | Every comment under a Hacker News story, flattened in reading order. |
| `GET /v1/hackernews/users/{username}` | `hackernews_user_get` | 1 | A Hacker News user: karma, about, submissions. |

### Facebook (beta)

The Meta Ad Library (ads on Facebook, Instagram, Messenger, WhatsApp, Threads and Audience Network): ad search with filters, advertisers, their ads, and one ad with its EU transparency details, in the library’s own JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/facebook/ads/search` | `facebook_ads_search` | 2 | Search the Meta Ad Library by keyword: 30 ads a page with country, status, media, category, language, placement and date filters. |
| `GET /v1/facebook/ads/company` | `facebook_ads_company` | 2 | Every ad of one advertiser (Facebook Page) in the Meta Ad Library, 30 a page, filterable. |
| `GET /v1/facebook/ads/advertisers/search` | `facebook_ads_search_advertisers` | 1 | Find advertisers (Facebook Pages) in the Meta Ad Library by name. |
| `GET /v1/facebook/ads/advertisers/{page}` | `facebook_ads_advertiser` | 2 | An advertiser’s Meta Ad Library profile: Page and Instagram details, political spend, top ad. |
| `GET /v1/facebook/ads/{id}` | `facebook_ads_get` | 2 | One Meta Ad Library ad with its details panel (EU reach by age and gender, payer, beneficiary). |
| `GET /v1/facebook/marketplace/locations` | `facebook_marketplace_locations` | 1 | Find Facebook Marketplace places (cities, neighbourhoods, postcodes) with coordinates. |
| `GET /v1/facebook/marketplace/search` | `facebook_marketplace_search` | 1 | Search Facebook Marketplace listings near a place, with price, condition, delivery, date and sort filters. |
| `GET /v1/facebook/marketplace/items/{id}` | `facebook_marketplace_item` | 1 | One Facebook Marketplace listing: price, description, location, attributes, photos. |
| `GET /v1/facebook/pages/{page}` | `facebook_page_get` | 2 | A Facebook Page or public profile: name, category, verified, follower counts, photos, intro (contact, website). |
| `GET /v1/facebook/events/search` | `facebook_event_search` | 1 | Search public Facebook events by keyword. |
| `GET /v1/facebook/events/city` | `facebook_event_city` | 1 | The events a city’s Facebook events page shows (logged out). |
| `GET /v1/facebook/events/{id}` | `facebook_event_get` | 1 | A public Facebook event: when, venue, description, hosts, tickets, responses. |
| `GET /v1/facebook/pages/{page}/events` | `facebook_page_events` | 1 | The events on a Facebook Page’s Events tab (first grid, logged out). |
| `GET /v1/facebook/pages/{page}/photos` | `facebook_page_photos` | 1 | The latest photos on a Facebook Page’s Photos tab (first grid, logged out). |
| `GET /v1/facebook/posts` | `facebook_post_get` | 2 | A public Facebook post: message, author, attachments, reactions, comments, shares, views, top comments. |
| `GET /v1/facebook/posts/comments` | `facebook_post_comments` | 2 | A Facebook post’s comments, paginated, ranked or all. |
| `GET /v1/facebook/comments/replies` | `facebook_comment_replies` | 2 | Replies to a Facebook comment, paginated. |

### npm (beta)

npm packages and registry search, from the public npm registry, in the registry’s own search-result and package-manifest shapes, with download counts.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/npm/search` | `npm_search_all` | 1 | Search npm packages, with downloads and scores. |
| `GET /v1/npm/package` | `npm_package_get` | 1 | One npm package version: manifest, dist-tags, downloads. |

### PyPI (beta)

Python packages on PyPI: project metadata, a release’s files, versions and known vulnerabilities, from PyPI’s public JSON API in its own shape.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/pypi/project` | `pypi_project_get` | 1 | One PyPI project release: metadata, files, versions, vulnerabilities. |

### Truth Social (live)

Public Truth Social profiles, account posts and single posts, in Truth Social’s own Mastodon-style Account and Status JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/truthsocial/profiles/{username}` | `truthsocial_profile_get` | 1 | A public Truth Social profile: bio, follower, following and post counts. |
| `GET /v1/truthsocial/profiles/{username}/posts` | `truthsocial_user_posts` | 1 | A Truth Social account’s posts, newest first, paginated, with reply and media filters. |
| `GET /v1/truthsocial/posts/{id}` | `truthsocial_post_get` | 1 | One Truth Social post with its media and reply, repost, like counts. |

### TikTok (beta)

Public TikTok profiles, videos with stats and caption tracks, comments and replies, transcripts, followers, hashtags, sounds, keyword search and the trending feed, in TikTok’s own web JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/tiktok/users/{handle}` | `tiktok_user_get` | 1 | A public TikTok profile: bio, links, verification, follower, like and video counts. |
| `GET /v1/tiktok/users/{handle}/videos` | `tiktok_user_videos` | 1 | A TikTok account’s videos, latest, most popular or oldest first (about 35 a page). |
| `GET /v1/tiktok/users/{handle}/followers` | `tiktok_user_followers` | 1 | Accounts that follow a TikTok account, 30 a page. |
| `GET /v1/tiktok/users/{handle}/following` | `tiktok_user_following` | 1 | Accounts a TikTok account follows, 30 a page (when the list is public). |
| `GET /v1/tiktok/videos/{id}` | `tiktok_video_get` | 1 | One TikTok video or photo post with stats, author, music, hashtags and caption tracks. |
| `GET /v1/tiktok/videos/{id}/comments` | `tiktok_video_comments` | 1 | Comments on a TikTok video, 20 a page. |
| `GET /v1/tiktok/videos/{id}/comments/{comment_id}/replies` | `tiktok_comment_replies` | 1 | Replies to a TikTok comment, 20 a page. |
| `GET /v1/tiktok/videos/{id}/transcript` | `tiktok_video_transcript` | 1 | What is said in a TikTok video, from its caption track: WebVTT, text and timed segments. |
| `GET /v1/tiktok/hashtags/{name}` | `tiktok_hashtag_get` | 1 | A TikTok hashtag with its video and view counts. |
| `GET /v1/tiktok/hashtags/{name}/videos` | `tiktok_search_hashtag` | 1 | Videos with a TikTok hashtag, about 30 a page. |
| `GET /v1/tiktok/songs/{id}` | `tiktok_song_get` | 1 | A TikTok sound: title, author, duration and how many videos use it. |
| `GET /v1/tiktok/songs/{id}/videos` | `tiktok_song_videos` | 1 | Videos using a TikTok sound, about 30 a page. |
| `GET /v1/tiktok/search/suggestions` | `tiktok_search_suggestions` | 1 | What TikTok’s search box suggests for a partial query. |
| `GET /v1/tiktok/search/videos` | `tiktok_search_videos` | 1 | TikTok videos for a keyword, 16 a page. |
| `GET /v1/tiktok/trending` | `tiktok_trending_feed` | 1 | The TikTok feed a new visitor in a region sees: about 30 popular videos. |
| `GET /v1/tiktok/users/{handle}/similar` | `tiktok_user_similar` | 1 | Accounts TikTok suggests alongside a profile, about 30. |
| `GET /v1/tiktok/users/{handle}/playlists` | `tiktok_user_playlists` | 1 | The playlists a TikTok creator made. |
| `GET /v1/tiktok/users/{handle}/liked` | `tiktok_user_liked` | 1 | Videos a TikTok account liked, when its likes are public. |
| `GET /v1/tiktok/users/{handle}/live` | `tiktok_user_live` | 1 | Whether a TikTok account is live, with its live room. |
| `GET /v1/tiktok/users/{handle}/region` | `tiktok_user_region` | 1 | The country a TikTok account posts from. |
| `GET /v1/tiktok/users/{handle}/full` | `tiktok_user_full` | 2 | A TikTok profile, its latest videos and computed analytics in one call. |
| `GET /v1/tiktok/live/{room_id}` | `tiktok_live_get` | 1 | A TikTok live room: status, title, viewers, host and stream. |
| `GET /v1/tiktok/playlists/{id}/videos` | `tiktok_playlist_videos` | 1 | Videos in a TikTok playlist, 30 a page. |
| `GET /v1/tiktok/places/{id}/videos` | `tiktok_location_posts` | 1 | Videos tagged at a TikTok place, 30 a page. |
| `GET /v1/tiktok/effects` | `tiktok_effect_get` | 1 | TikTok effects by id: name, creator and how many videos use them. |
| `GET /v1/tiktok/effects/{id}/videos` | `tiktok_effect_videos` | 1 | Videos made with a TikTok effect, 30 a page. |
| `GET /v1/tiktok/videos/{id}/comments/{comment_id}` | `tiktok_comment_get` | 2 | One TikTok comment by id, with its current likes and replies. |
| `GET /v1/tiktok/trending/hashtags` | `tiktok_hashtags_popular` | 1 | TikTok’s trending-hashtag board for a market and period. |
| `GET /v1/tiktok/trending/videos` | `tiktok_videos_popular` | 1 | TikTok’s top-videos board for a market and period. |
| `GET /v1/tiktok/shop/products/{id}` | `tiktok_shop_product` | 1 | A TikTok Shop product: price, sold count, SKUs, seller, shipping and ratings. |
| `GET /v1/tiktok/shop/products/{id}/reviews` | `tiktok_shop_product_reviews` | 1 | A TikTok Shop product’s rating breakdown and its first reviews. |
| `GET /v1/tiktok/shop/stores/{seller_id}/products` | `tiktok_shop_products` | 1 | The products of a TikTok Shop store, best sellers first. |
| `GET /v1/tiktok/shop/search` | `tiktok_shop_search` | 1 | TikTok Shop products for a keyword. |
| `GET /v1/tiktok/collections/{id}/videos` | `tiktok_collection_videos` | 1 | Videos in a public TikTok collection, 30 a page. |
| `GET /v1/tiktok/shop/sales` | `tiktok_shop_sales` | 1 | Top TikTok Shop listings for a keyword by units sold, with estimated sales. |

### Telegram (live)

Public Telegram channels: profile with exact subscriber count, posts with views, reactions and media, single posts and their comments, in the shape of the Telegram Bot API’s Chat and Message objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/telegram/channels/{handle}` | `telegram_channel_get` | 1 | A public Telegram channel, group or bot: title, bio, exact subscribers, media counts. |
| `GET /v1/telegram/channels/{handle}/posts` | `telegram_channel_posts` | 1 | A page of a public channel’s posts (20, newest first), or posts matching words. |
| `GET /v1/telegram/posts` | `telegram_post_get` | 1 | One public Telegram post: text, views, reactions, media, forward and reply. |
| `GET /v1/telegram/posts/comments` | `telegram_post_comments` | 1 | Comments on a Telegram channel post, 50 a page, from its discussion group. |

### App Store (live)

Public Apple App Store data: app search, app details with ratings histograms and privacy labels, reviews, top charts, search suggestions.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/appstore/apps/search` | `appstore_app_search_get` | 2 | Search App Store apps by keyword, with full metadata per app. |
| `GET /v1/appstore/apps/suggestions` | `appstore_search_suggestions_get` | 1 | App Store search suggestions for a partial keyword. |
| `GET /v1/appstore/apps/{app_id}` | `appstore_app_info_get` | 2 | One App Store app: metadata, ratings histogram, privacy labels, in-app purchases. |
| `GET /v1/appstore/apps/{app_id}/reviews` | `appstore_app_reviews_get` | 2 | App Store reviews of an app, newest or most helpful, up to 500. |
| `GET /v1/appstore/charts` | `appstore_app_list_get` | 2 | An App Store top chart (free, paid, grossing, new), optionally by category. |
| `GET /v1/appstore/listings/search` | `appstore_app_listings_search_get` | 3 | Search App Store listings by title and description with field filters, paged. |
| `GET /v1/appstore/categories` | `appstore_categories_get` | 1 | App Store categories (genres) with their ids. |
| `GET /v1/appstore/locations` | `appstore_locations_get` | 1 | App Store storefront countries. |
| `GET /v1/appstore/languages` | `appstore_languages_get` | 1 | Languages App Store metadata can be requested in. |

### YouTube (beta)

Public videos and Shorts with transcripts, comments, sponsors and related videos; channels with their videos, Shorts, live streams, playlists and posts; search, hashtags and autocomplete, shaped like YouTube Data API v3 resources.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/youtube/videos/{id}` | `youtube_video_get` | 1 | A YouTube video or Short: details, exact views, likes and comments, channel, chapters, captions, paid-promotion flag, up next. |
| `POST /v1/youtube/videos/batch` | `youtube_video_batch` | 5 | Up to 50 YouTube videos by id in one call: details and exact counts. |
| `GET /v1/youtube/videos/{id}/related` | `youtube_video_related` | 1 | The videos YouTube shows beside a video (“up next”). |
| `GET /v1/youtube/videos/{id}/transcript` | `youtube_video_transcript` | 2 | A YouTube video’s transcript: timestamped segments and full text, in a chosen language. |
| `POST /v1/youtube/transcripts/batch` | `youtube_video_transcript_batch` | 15 | Transcripts of up to 10 YouTube videos in one call. |
| `GET /v1/youtube/videos/{id}/subtitles` | `youtube_video_subtitles` | 2 | A YouTube video’s captions as a subtitle file: srt, vtt, ttml, json3 or srv1. |
| `GET /v1/youtube/videos/{id}/thumbnails` | `youtube_video_thumbnails` | 1 | Every thumbnail size of a YouTube video. |
| `GET /v1/youtube/videos/{id}/sponsors` | `youtube_video_sponsors` | 3 | Sponsors of a YouTube video, inferred from the paid-promotion label, description and transcript. |
| `GET /v1/youtube/videos/{id}/comments` | `youtube_video_comments` | 1 | Comments on a YouTube video, top or newest first, paginated. |
| `GET /v1/youtube/comments/replies` | `youtube_comment_replies` | 1 | Replies to a YouTube comment, paginated. |
| `GET /v1/youtube/channels/{channel}` | `youtube_channel_get` | 1 | A YouTube channel: about, subscriber, video and view counts, country, links, join date. |
| `POST /v1/youtube/channels/batch` | `youtube_channel_batch` | 5 | Up to 25 YouTube channels by id in one call. |
| `GET /v1/youtube/channels/{channel}/full` | `youtube_channel_full` | 5 | A YouTube channel with its latest uploads in full and metrics computed over them. |
| `GET /v1/youtube/channels/{channel}/videos` | `youtube_channel_videos` | 1 | A YouTube channel’s videos, latest, popular or oldest first, paginated. |
| `GET /v1/youtube/channels/{channel}/shorts` | `youtube_channel_shorts` | 1 | A YouTube channel’s Shorts, newest, popular or oldest first, paginated. |
| `GET /v1/youtube/channels/{channel}/lives` | `youtube_channel_lives` | 1 | A YouTube channel’s live streams and past broadcasts, paginated. |
| `GET /v1/youtube/channels/{channel}/playlists` | `youtube_channel_playlists` | 1 | A YouTube channel’s playlists, paginated. |
| `GET /v1/youtube/channels/{channel}/podcasts` | `youtube_channel_podcasts` | 1 | A YouTube channel’s podcasts. |
| `GET /v1/youtube/channels/{channel}/posts` | `youtube_channel_community_posts` | 1 | A YouTube channel’s community posts, paginated. |
| `GET /v1/youtube/channels/{channel}/search` | `youtube_channel_search` | 1 | Search inside one YouTube channel’s videos. |
| `GET /v1/youtube/posts/{id}` | `youtube_community_post_get` | 1 | One YouTube community post: text, images, poll, attached video, likes. |
| `GET /v1/youtube/playlists/{id}` | `youtube_playlist_get` | 1 | A YouTube playlist and its videos, 100 a page. |
| `GET /v1/youtube/search` | `youtube_search_videos` | 1 | Search YouTube: videos, Shorts, channels or playlists, with sort, date, duration and feature filters. |
| `GET /v1/youtube/hashtags/{tag}` | `youtube_search_hashtag` | 1 | Videos or Shorts tagged with a YouTube hashtag, paginated. |
| `GET /v1/youtube/search/suggestions` | `youtube_search_suggestions` | 1 | YouTube search autocomplete suggestions. |
| `GET /v1/youtube/trending/shorts` | `youtube_shorts_trending` | 5 | About 45 popular YouTube Shorts with full details, a fresh batch each call. |
| `GET /v1/youtube/trending/videos` | `youtube_videos_trending` | 2 | The videos on YouTube’s trending shelves for music, sports, news or gaming. |

### Pinterest (live)

Public Pinterest pins with save counts, search, profiles, boards and their pins, topics, URL save counts and Pinterest Trends, in Pinterest’s own pin, board and user objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/pinterest/search/pins` | `pinterest_search_pins` | 1 | Search Pinterest pins by keyword, paginated. |
| `GET /v1/pinterest/pins/{id}` | `pinterest_pin_get` | 1 | One Pinterest pin with its save, reaction and comment counts. |
| `GET /v1/pinterest/users/{username}` | `pinterest_user_get` | 1 | A public Pinterest profile: followers, following, pins, boards, monthly views. |
| `GET /v1/pinterest/users/{username}/boards` | `pinterest_user_boards` | 1 | A Pinterest account’s public boards, paginated. |
| `GET /v1/pinterest/users/{username}/pins` | `pinterest_user_pins` | 1 | The pins a Pinterest account created, newest first, paginated. |
| `GET /v1/pinterest/board` | `pinterest_board_get` | 1 | A Pinterest board: pin, follower and section counts, owner. |
| `GET /v1/pinterest/board/pins` | `pinterest_board_pins` | 1 | The pins on a Pinterest board, with save counts, paginated. |
| `GET /v1/pinterest/topic` | `pinterest_topic_get` | 1 | A Pinterest topic (ideas page) with its best pins. |
| `GET /v1/pinterest/url-stats` | `pinterest_url_stats` | 1 | How many times up to 10 web pages were saved to Pinterest. |
| `GET /v1/pinterest/trends` | `pinterest_trends_get` | 3 | Pinterest Trends for a country: growing, seasonal, top monthly or yearly terms. |

### Steam (live)

The public Steam store: apps by id (descriptions, price, developers, genres, release date, screenshots) and store search, per country and language, in Steam’s own JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/steam/apps/{app_id}` | `steam_app_get` | 1 | A Steam app by id: descriptions, price, developers, genres, release date, media. |
| `GET /v1/steam/search` | `steam_search_all` | 1 | Search the Steam store by title: ids, prices, platforms, metascore. |

### Stack Overflow (beta)

Stack Overflow questions, answers, comments and search, from the public Stack Exchange API, in its own item and wrapper shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/stackoverflow/search` | `stackoverflow_search_all` | 1 | Search Stack Overflow questions by text, tags and date. |
| `GET /v1/stackoverflow/questions/{id}` | `stackoverflow_question_get` | 1 | One Stack Overflow question with its body, tags and counts. |
| `GET /v1/stackoverflow/questions/{id}/answers` | `stackoverflow_question_answers` | 1 | Answers to a Stack Overflow question, by votes, activity or date. |
| `GET /v1/stackoverflow/questions/{id}/comments` | `stackoverflow_question_comments` | 1 | Comments on a Stack Overflow question. |

### Polymarket (beta)

Polymarket prediction-market events, markets with live prices and volumes, tags and trader profiles, from Polymarket’s public search API in its own shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/polymarket/search` | `polymarket_search_all` | 1 | Search Polymarket events, markets, tags and profiles. |
| `GET /v1/polymarket/research` | `polymarket_research_get` | 3 | Polymarket research: a topic fanned out into several searches, merged. |

### US Congress trades (beta)

Stock trades disclosed by members of the US House and Senate (periodic transaction reports), with politicians, issuers and aggregate stats, as compiled on Capitol Trades’ public site.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/uscongresstrades/trades` | `uscongresstrades_trades_get` | 1 | Congressional stock trades, filtered by ticker, member, party, chamber, sector, type and dates. |
| `GET /v1/uscongresstrades/trades/latest` | `uscongresstrades_trades_latest` | 1 | The most recently disclosed congressional trades. |
| `GET /v1/uscongresstrades/trades/recent` | `uscongresstrades_trades_recent` | 1 | The most recently made congressional trades, by trade date. |
| `GET /v1/uscongresstrades/members` | `uscongresstrades_members_get` | 1 | Members of Congress who trade, with their trading stats. |
| `GET /v1/uscongresstrades/politicians/{handle}` | `uscongresstrades_politician_get` | 1 | One member of Congress: party, state, committees, trading stats. |
| `GET /v1/uscongresstrades/politicians/{handle}/trades` | `uscongresstrades_politician_trades` | 1 | A member of Congress’s disclosed trades. |
| `GET /v1/uscongresstrades/tickers/{keyword}` | `uscongresstrades_ticker_get` | 1 | A traded issuer: sector, price performance, congressional trading stats. |
| `GET /v1/uscongresstrades/tickers/{keyword}/trades` | `uscongresstrades_ticker_trades` | 1 | Congressional trades in one ticker. |
| `GET /v1/uscongresstrades/states/{state}/trades` | `uscongresstrades_state_trades` | 1 | Trades by the members from one US state. |
| `GET /v1/uscongresstrades/stats` | `uscongresstrades_stats_get` | 1 | Overview: trades, members, issuers, buys and sells. |
| `GET /v1/uscongresstrades/stats/party` | `uscongresstrades_stats_party` | 1 | Trading by party: trades, buys, sells, members, volume. |
| `GET /v1/uscongresstrades/stats/sectors` | `uscongresstrades_stats_sectors` | 1 | Trades per sector. |
| `GET /v1/uscongresstrades/stats/issuers` | `uscongresstrades_stats_issuers` | 1 | Most traded issuers by volume. |
| `GET /v1/uscongresstrades/stats/politicians` | `uscongresstrades_stats_politicians` | 1 | Members who trade the most, by volume. |
| `GET /v1/uscongresstrades/stats/tickers` | `uscongresstrades_stats_tickers` | 1 | Most bought or most sold tickers. |
| `GET /v1/uscongresstrades/stats/volume` | `uscongresstrades_stats_volume` | 2 | Trade counts and value over time, per day, week or month. |
| `GET /v1/uscongresstrades/stats/unusual` | `uscongresstrades_stats_unusual` | 2 | The largest trades of the last days. |
| `GET /v1/uscongresstrades/stats/buy-sell` | `uscongresstrades_stats_buy_sell` | 1 | Buys against sells over a window, by party or sector. |
| `GET /v1/uscongresstrades/stats/reporting-gaps` | `uscongresstrades_stats_reporting_gaps` | 1 | Trades disclosed the longest after they were made. |

### SoundCloud (live)

Public SoundCloud profiles (followers, track counts, bio), their tracks and single tracks (plays, likes, reposts, comments, genre, tags), in SoundCloud’s own API v2 JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/soundcloud/users/{handle}` | `soundcloud_artist_get` | 1 | A public SoundCloud profile: followers, following, track and playlist counts, bio. |
| `GET /v1/soundcloud/users/{handle}/tracks` | `soundcloud_artist_tracks` | 1 | A SoundCloud profile’s tracks, newest first, 20 a page, with play counts. |
| `GET /v1/soundcloud/tracks` | `soundcloud_track_get` | 1 | One SoundCloud track by URL: plays, likes, reposts, comments, genre, tags. |

### Snapchat (live)

Public Snapchat profiles (subscribers, bio, live story, highlights, recent Spotlight snaps with counts), Spotlight snaps and their comments, in Snapchat’s own JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/snapchat/users/{handle}` | `snapchat_user_get` | 1 | A public Snapchat profile: subscribers, bio, story, highlights and recent Spotlight snaps. |
| `GET /v1/snapchat/spotlights` | `snapchat_spotlight_get` | 1 | One Snapchat Spotlight snap: media, view/like/comment/share counts, creator, description. |
| `GET /v1/snapchat/spotlights/comments` | `snapchat_spotlight_comments` | 1 | Comments on a Snapchat Spotlight snap, paginated. |

### Linktree (live)

Public Linktree pages: the profile, every link with its type, and social links, in Linktree’s own account and link JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/linktree/pages` | `linktree_page_get` | 1 | A Linktree page: profile, links with their types, and social links. |

### Komi (live)

Public Komi creator pages: the talent profile, social links and every module (links, products, music, videos), in Komi’s own JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/komi/pages` | `komi_page_get` | 1 | A Komi creator page: profile, social links and every module. |

### Pillar (live)

Public Pillar creator pages: banner profile with socials and contact, links, products, videos and page blocks, in Pillar’s own JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/pillar/pages` | `pillar_page_get` | 1 | A Pillar creator page: profile, socials, contact, links, products and videos. |

### Lnk.Bio (live)

Public Lnk.Bio pages: profile, bio, every link with its image, social icons and contact links.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/linkbio/pages` | `linkbio_page_get` | 1 | A Lnk.Bio page: profile, bio, links, social icons and contact links. |

### Linkme (live)

Public Linkme profiles: bio, visit count, verified flag and every link group (socials, music, contact, custom), in Linkme’s own JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/linkme/pages` | `linkme_page_get` | 1 | A Linkme profile: bio, visit count and every link group. |

### Finance (beta)

Stock, index, fund, currency and futures quotes, price history, financial statements, option chains, fundamentals, market overviews and finance news, from Yahoo Finance’s public web data.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/finance/quote` | `finance_quote_get` | 2 | A live quote: price, change, volume, ranges, market cap, ratios. |
| `GET /v1/finance/ticker-search` | `finance_ticker_search_get` | 1 | Find tickers by name or symbol: stocks, indices, funds, currencies, futures. |
| `GET /v1/finance/markets` | `finance_markets_get` | 1 | Market overview: major indices, currencies, commodities and crypto. |
| `GET /v1/finance/news` | `finance_news_get` | 1 | Finance news about a company or topic. |
| `GET /v1/finance/history` | `finance_history_get` | 1 | Price history between two dates, daily to quarterly. |
| `GET /v1/finance/statements` | `finance_statements_get` | 2 | Income statement, balance sheet and cash flow, annual, quarterly or trailing. |
| `GET /v1/finance/options` | `finance_options_get` | 2 | An option chain: calls and puts for an expiry. |
| `GET /v1/finance/fundamentals` | `finance_fundamentals_get` | 1 | Key statistics, financial data and earnings history. |

### Amazon (beta)

Public Amazon data in 13 marketplaces: products with prices, ratings and review summaries, search, every offer on a product, Best Sellers lists, deals, seller profiles, search suggestions and creator shops.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/amazon/products/{asin}` | `amazon_product_get` | 3 | One Amazon product by ASIN: price, rating, review summary, details, rank, images, seller. |
| `GET /v1/amazon/search` | `amazon_product_search_get` | 1 | Search Amazon products by keyword in any of 13 marketplaces. |
| `GET /v1/amazon/products/{asin}/offers` | `amazon_sellers_get` | 1 | Every offer on an Amazon product: price, condition, seller and delivery. |
| `GET /v1/amazon/best-sellers` | `amazon_best_sellers_get` | 1 | Amazon Best Sellers, New Releases, Movers & Shakers, Most Wished For or Gift Ideas in a category. |
| `GET /v1/amazon/deals` | `amazon_deals_get` | 1 | Current Amazon deals with deal price, list price and badge. |
| `GET /v1/amazon/sellers/{seller_id}` | `amazon_seller_get` | 1 | An Amazon seller profile: rating, feedback breakdown, business details, recent feedback. |
| `GET /v1/amazon/search/suggestions` | `amazon_search_suggestions` | 1 | Amazon search-box suggestions for a partial query. |
| `GET /v1/amazon/shop` | `amazon_shop_get` | 1 | An Amazon creator shop or list: profile, lists and products. |

### Google Play (live)

Public Google Play data: app search, app details with installs and ratings histograms, reviews, books and films search, search suggestions.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/googleplay/books/search` | `googleplay_books_search` | 1 | Search Google Play books and audiobooks, or browse a books category. |
| `GET /v1/googleplay/movies/search` | `googleplay_movies_search` | 1 | Search Google Play films, TV shows and episodes, or browse a films category. |
| `GET /v1/googleplay/apps/search` | `googleplay_app_search_get` | 2 | Search Google Play apps by keyword. |
| `GET /v1/googleplay/apps/suggestions` | `googleplay_search_suggestions_get` | 1 | Google Play search suggestions for a partial keyword. |
| `GET /v1/googleplay/apps/{app_id}` | `googleplay_app_info_get` | 2 | One Google Play app: installs, score, ratings histogram, price, developer, version. |
| `GET /v1/googleplay/apps/{app_id}/reviews` | `googleplay_app_reviews_get` | 2 | Google Play reviews of an app, newest or most relevant, up to 600, by star. |
| `GET /v1/googleplay/listings/search` | `googleplay_app_listings_search_get` | 2 | Search Google Play listings by title and description with field filters, paged. |
| `GET /v1/googleplay/categories` | `googleplay_categories_get` | 1 | Google Play app and game categories. |
| `GET /v1/googleplay/locations` | `googleplay_locations_get` | 1 | Google Play storefront countries. |
| `GET /v1/googleplay/languages` | `googleplay_languages_get` | 1 | Languages Google Play data can be requested in. |

### Spotify (live)

The public Spotify catalogue: artists (followers, monthly listeners, top cities, top tracks with play counts, discography), albums, tracks with play counts, playlists, podcasts and their episodes, and search, in the shape of the Spotify Web API’s own objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/spotify/artists/{id}` | `spotify_artist_get` | 1 | A Spotify artist: followers, monthly listeners, top cities, top tracks, discography. |
| `GET /v1/spotify/albums/{id}` | `spotify_album_get` | 1 | A Spotify album with its tracks, label, release date and play counts. |
| `GET /v1/spotify/tracks/{id}` | `spotify_track_get` | 1 | A Spotify track: artists, album, duration and all-time play count. |
| `GET /v1/spotify/playlists/{id}` | `spotify_playlist_get` | 1 | A public Spotify playlist: followers, owner and its tracks, 100 a page. |
| `GET /v1/spotify/shows/{id}` | `spotify_podcast_get` | 1 | A Spotify podcast: publisher, description, episode count, rating, topics. |
| `GET /v1/spotify/shows/{id}/episodes` | `spotify_podcast_episodes` | 1 | A Spotify podcast’s episodes, newest first, 50 a page. |
| `GET /v1/spotify/search` | `spotify_search_all` | 1 | Search Spotify: artists, albums, tracks, playlists, podcasts and episodes. |

### Twitch (live)

Public Twitch channels with follower counts and live status, their videos (past broadcasts, highlights, uploads) and stream schedules, and clips, in the shape of Twitch’s Helix API objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/twitch/users/{handle}` | `twitch_user_get` | 1 | A Twitch channel: bio, followers, partner status, live stream, last broadcast, socials. |
| `GET /v1/twitch/users/{handle}/videos` | `twitch_user_videos` | 1 | A Twitch channel’s videos (past broadcasts, highlights, uploads), up to 100, by date or views. |
| `GET /v1/twitch/users/{handle}/schedule` | `twitch_user_schedule` | 1 | A Twitch channel’s stream schedule: upcoming segments, categories, vacation. |
| `GET /v1/twitch/clips` | `twitch_clip_get` | 1 | A Twitch clip: title, views, duration, broadcaster, clipper, game, VOD offset, MP4 renditions. |

### Kick (live)

Public Kick channels (followers, live stream, bio and socials) and clips, in Kick’s own JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/kick/channels/{handle}` | `kick_channel_get` | 1 | A Kick channel: followers, verified, live stream, bio and social links. |
| `GET /v1/kick/clips` | `kick_clip_get` | 1 | A Kick clip: title, views, duration, channel, creator, category, playlist URL. |

### Economy (beta)

Economic data from official public sources: household and tourism spending in Europe (Eurostat), US federal spending and contract awards (USAspending.gov), and a US importer’s suppliers and shipments from customs bills of lading (as compiled by ImportYeti).

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/economy/consumer-spend` | `economy_consumer_spend_get` | 1 | Household spending by country and category, from Eurostat. |
| `GET /v1/economy/tourism-spend` | `economy_tourism_spend_get` | 1 | Travel spending by country, purpose, destination and category, from Eurostat. |
| `GET /v1/economy/government-spend` | `economy_government_spend_get` | 1 | US federal spending by state, county or country, from USAspending. |
| `GET /v1/economy/government-contracts` | `economy_government_contracts_get` | 1 | US federal contract awards by recipient, keyword or industry code. |
| `GET /v1/economy/imports` | `economy_imports_get` | 5 | A US importer’s suppliers and recent shipments, from customs records. |

### Apple Music (live)

The public Apple Music catalogue: artists with albums and top songs, albums with tracks, songs and music videos with preview links, search, and each country’s most-played charts, in Apple’s own iTunes Search API and RSS chart JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/applemusic/artists/{id}` | `applemusic_artist_get` | 1 | An Apple Music artist with up to 50 albums and the top 25 songs. |
| `GET /v1/applemusic/albums/{id}` | `applemusic_album_get` | 1 | An Apple Music album with every track, release date, genre and copyright. |
| `GET /v1/applemusic/tracks/{id}` | `applemusic_track_get` | 1 | An Apple Music song or music video with a 30-second preview link. |
| `GET /v1/applemusic/search` | `applemusic_search_all` | 1 | Search Apple Music for artists, albums, songs and music videos. |
| `GET /v1/applemusic/charts` | `applemusic_charts_get` | 1 | A country’s Apple Music most-played chart: songs, albums, videos or playlists. |

### Rumble (live)

Public Rumble videos: search, channel videos with exact views and votes, single videos with description, top-level comments and published caption transcripts, in Rumble’s own listing fields.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/rumble/search/videos` | `rumble_search_videos` | 1 | Search Rumble videos by words, with sort, date and duration filters. |
| `GET /v1/rumble/channels/{handle}/videos` | `rumble_channel_videos` | 1 | A Rumble channel’s videos, newest first, with exact views, votes and comments. |
| `GET /v1/rumble/videos` | `rumble_video_get` | 1 | One Rumble video by URL: exact views, votes, description, channel. |
| `GET /v1/rumble/videos/comments` | `rumble_video_comments` | 1 | The top-level comments on a Rumble video, with likes and reply counts. |
| `GET /v1/rumble/videos/transcript` | `rumble_video_transcript` | 3 | A Rumble video’s published captions as timed segments and text. |

### Gab (beta)

Public Gab profiles, posts, comment threads and post search, from Gab’s logged-out web API, in its own Mastodon-style account and status shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/gab/users/{handle}` | `gab_user_get` | 1 | A Gab profile: bio, follower and post counts. |
| `GET /v1/gab/users/{handle}/posts` | `gab_user_posts` | 1 | A Gab account’s posts, newest first, paginated. |
| `GET /v1/gab/posts/{id}` | `gab_post_get` | 1 | One Gab post with its counts and media. |
| `GET /v1/gab/posts/{id}/comments` | `gab_post_comments` | 1 | Comments under a Gab post, newest, oldest or top first. |
| `GET /v1/gab/search` | `gab_search_posts` | 1 | Search Gab posts. |

### LinkedIn (beta)

Public LinkedIn profiles, company and showcase pages with their posts, single posts and video transcripts, Pulse articles, job search and postings, and the Ad Library, read logged out from LinkedIn’s public pages and kept in their own schema.org JSON-LD.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/linkedin/profiles/{profile}` | `linkedin_profile_get` | 5 | A public LinkedIn profile: headline, about, experience, education, followers, recent posts, similar profiles. |
| `GET /v1/linkedin/companies/{company}` | `linkedin_company_get` | 5 | A LinkedIn company or showcase page: about, size, followers, locations, similar and affiliated pages, latest posts. |
| `GET /v1/linkedin/companies/{company}/posts` | `linkedin_company_posts` | 5 | A LinkedIn company page’s posts, newest first, paginated. |
| `GET /v1/linkedin/posts/{post}` | `linkedin_post_get` | 5 | One public LinkedIn post with its author, reaction and comment counts and visible comments. |
| `GET /v1/linkedin/posts/{post}/transcript` | `linkedin_post_transcript` | 10 | The captions of a LinkedIn video post, as text and timed segments. |
| `GET /v1/linkedin/articles/{article}` | `linkedin_article_get` | 5 | A LinkedIn Pulse article with its body, author and like and comment counts. |
| `GET /v1/linkedin/jobs` | `linkedin_jobs_search` | 5 | LinkedIn job search by keywords, location, company and date posted, paginated. |
| `GET /v1/linkedin/jobs/{job}` | `linkedin_job_get` | 5 | One LinkedIn job posting: description, salary range, seniority, type, applicants. |
| `GET /v1/linkedin/ads` | `linkedin_ads_search` | 5 | LinkedIn Ad Library search by company, advertiser, keyword, country and dates, paginated. |
| `GET /v1/linkedin/ads/{ad}` | `linkedin_ad_get` | 5 | One LinkedIn Ad Library ad: creative, advertiser, payer, run dates, impressions and targeting. |
| `GET /v1/linkedin/search/locations` | `linkedin_search_locations` | 1 | LinkedIn location ids (geo ids) matching a place name. |
| `GET /v1/linkedin/search/companies` | `linkedin_search_companies` | 1 | LinkedIn company ids matching a company name. |

### Walmart (beta)

Public Walmart data: products with prices, availability and specifications, reviews, search, category listings and seller offers.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/walmart/products/{product_id}` | `walmart_product_get` | 3 | One Walmart product: price, availability, rating, seller, specifications. |
| `GET /v1/walmart/products/{product_id}/reviews` | `walmart_reviews_get` | 2 | Walmart reviews of a product, paged, with sort and star filters. |
| `GET /v1/walmart/search` | `walmart_search_all` | 2 | Search Walmart with sort, price range, store and facet filters. |
| `GET /v1/walmart/categories/{category_id}` | `walmart_category_get` | 2 | The items in a Walmart category, with sort and filters. |
| `GET /v1/walmart/products/{product_id}/offers` | `walmart_offers_get` | 2 | Who sells a Walmart item: the primary offer, the seller and other offers. |

### eBay (live)

Public eBay listings on 19 eBay sites: search with eBay's own filters (condition, format, sold listings, price, aspects) and item pages with item specifics and seller feedback.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/ebay/search` | `ebay_search_all` | 2 | Search eBay listings with eBay's filters, including sold listings. |
| `GET /v1/ebay/items/{product_id}` | `ebay_product_get` | 2 | One eBay item: price, condition, quantity sold, item specifics, seller feedback. |

### Cosmos (beta)

Public Cosmos profiles, their saved elements (images, videos, links, products), collections (clusters) and element search, from the GraphQL API Cosmos’s logged-out web app reads, in its own shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/cosmos/users/{handle}` | `cosmos_user_get` | 1 | A Cosmos profile with element and collection counts. |
| `GET /v1/cosmos/users/{handle}/posts` | `cosmos_user_posts` | 1 | A Cosmos user’s saved elements, newest first, paginated. |
| `GET /v1/cosmos/users/{handle}/clusters` | `cosmos_user_clusters` | 1 | A Cosmos user’s top public collections. |
| `GET /v1/cosmos/posts` | `cosmos_post_get` | 1 | One Cosmos element: media, source, owner. |
| `GET /v1/cosmos/clusters` | `cosmos_cluster_get` | 1 | A Cosmos collection: name, owner, counts, cover. |
| `GET /v1/cosmos/clusters/posts` | `cosmos_cluster_posts` | 1 | The elements in a Cosmos collection, paginated. |
| `GET /v1/cosmos/search` | `cosmos_search_posts` | 1 | Search Cosmos elements, paginated. |

### Etsy (live)

Etsy search suggestions (keyword research). Listing, shop and similar-item pages need a browser challenge Etsy shows every logged-out visitor, so they are not offered.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/etsy/search/suggestions` | `etsy_search_suggestions` | 1 | Etsy search-box suggestions for a partial query. |

### Target (live)

Public Target data: items with prices, specifications and ratings, reviews with rating statistics, and the store finder.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/target/products/{tcin}` | `target_product_get` | 2 | One Target item: price, specifications, images, ratings, variations. |
| `GET /v1/target/products/{tcin}/reviews` | `target_reviews_get` | 2 | Target reviews of an item, with rating statistics. |
| `GET /v1/target/stores` | `target_stores_get` | 1 | Target stores near a place. |
| `GET /v1/target/categories` | `target_categories_get` | 1 | Target categories and their subcategories. |

### IKEA (live)

IKEA product search per country site, as IKEA's own search service returns it.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/ikea/search` | `ikea_search_all` | 1 | Search IKEA products in a country. |

### Sephora (live)

Public Sephora (US) data: catalog search and category listings with prices and ratings, product records, and reviews with rating statistics.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/sephora/products/{product_id}` | `sephora_product_get` | 1 | A Sephora product record: brand, description, category, EANs, review statistics. |
| `GET /v1/sephora/products/{product_id}/reviews` | `sephora_reviews_get` | 2 | Sephora reviews of a product with sort, star filter and statistics. |
| `GET /v1/sephora/search` | `sephora_search_all` | 2 | Search Sephora's catalog with price filters. |
| `GET /v1/sephora/categories/{category_id}` | `sephora_category_get` | 2 | The products of a Sephora category. |

### Gumtree (live)

Public Gumtree (UK classifieds) ads: search with Gumtree's filters, ad pages and similar ads.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/gumtree/search` | `gumtree_search_all` | 2 | Search Gumtree ads by keyword, category and location with filters. |
| `GET /v1/gumtree/products` | `gumtree_product_get` | 2 | One Gumtree ad: price, description, attributes, images, seller. |
| `GET /v1/gumtree/products/similar` | `gumtree_product_similar` | 2 | The ads Gumtree recommends with an ad. |
| `GET /v1/gumtree/sellers` | `gumtree_seller_get` | 2 | A Gumtree seller's public profile and ads. |
| `GET /v1/gumtree/sellers/listings` | `gumtree_seller_listings` | 2 | The ads a Gumtree seller lists. |
| `GET /v1/gumtree/trending` | `gumtree_trending_get` | 1 | Trending Gumtree searches in a location. |
| `GET /v1/gumtree/categories` | `gumtree_categories_get` | 1 | Gumtree categories and their children. |
| `GET /v1/gumtree/locations` | `gumtree_locations_get` | 1 | Gumtree location suggestions with ids and coordinates. |

### Kwai (beta)

Public Kwai profiles, their videos and single videos, from the pages and JSON Kwai’s logged-out web app uses, in its own user and photo shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/kwai/user` | `kwai_user_get` | 1 | A Kwai profile: bio, followers, likes, video counts. |
| `GET /v1/kwai/user/posts` | `kwai_user_posts` | 1 | A Kwai account’s videos, newest first, paginated. |
| `GET /v1/kwai/post` | `kwai_post_get` | 1 | One Kwai video: caption, counts, media, author. |

### Best Buy (beta)

Best Buy product pages: price and every marketplace offer, availability, rating and review count, brand and model.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/bestbuy/products` | `bestbuy_product_get` | 2 | A Best Buy product: offers, price, availability, rating. |

### idealo (live)

idealo price comparison on six country sites (DE, AT, IT, ES, FR, GB): product search with lowest prices and offer counts, and product offer lists.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/idealo/search` | `idealo_search_all` | 1 | Search idealo: products with lowest price and number of offers. |
| `GET /v1/idealo/products` | `idealo_product_get` | 1 | An idealo product with every shop's offer. |

### H&M (live)

H&M catalogue search on its country sites: prices, sale and member prices, colours, stock flags and facets.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/hm/search` | `hm_search_all` | 3 | Search H&M's catalogue on one country site. |

### AliExpress (beta)

AliExpress product search: sale prices and discounts, units sold, ratings.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/aliexpress/search` | `aliexpress_search_all` | 2 | Search AliExpress products. |

### Weibo (beta)

Public Weibo profiles, posts, comment threads and replies, post and user search and the real-time hot search list, from the JSON Weibo’s logged-out mobile web app reads, in its own user, mblog and comment shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/weibo/user` | `weibo_user_get` | 1 | A Weibo profile: bio, followers, following, post counts, verification. |
| `GET /v1/weibo/user/posts` | `weibo_user_posts` | 2 | A Weibo account’s posts, newest first, paginated. |
| `GET /v1/weibo/post` | `weibo_post_get` | 1 | One Weibo post with its counts, pictures and video. |
| `GET /v1/weibo/post/comments` | `weibo_post_comments` | 2 | Comments on a Weibo post, hot or latest first. |
| `GET /v1/weibo/comment/replies` | `weibo_comment_replies` | 2 | Replies to a Weibo comment. |
| `GET /v1/weibo/search` | `weibo_search_posts` | 2 | Search Weibo posts: all, latest, hot, original, verified, videos or images. |
| `GET /v1/weibo/search/users` | `weibo_search_users` | 2 | Search Weibo users. |
| `GET /v1/weibo/trending` | `weibo_trending_get` | 2 | Weibo’s real-time hot search list. |

### Douyin (beta)

Douyin’s hot search board, single videos with play and like counts, and creator pages with their latest videos, from Douyin’s logged-out share and Douyin Select (抖音精选) pages, in their own shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/douyin/user` | `douyin_user_get` | 2 | A Douyin creator page: name, bio, video count. |
| `GET /v1/douyin/user/posts` | `douyin_user_posts` | 2 | A Douyin creator’s latest videos. |
| `GET /v1/douyin/post` | `douyin_post_get` | 2 | One Douyin video: title, author, plays, likes, media. |
| `GET /v1/douyin/trending` | `douyin_trending_get` | 2 | Douyin’s hot search board. |

### Xiaohongshu (beta)

Xiaohongshu (rednote) profiles, their latest notes and the explore feed, from the pages its logged-out web app renders for guests, in its own shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/xiaohongshu/user` | `xiaohongshu_user_get` | 2 | A Xiaohongshu profile: bio, followers, likes and saves. |
| `GET /v1/xiaohongshu/user/posts` | `xiaohongshu_user_posts` | 2 | A Xiaohongshu account’s latest notes. |
| `GET /v1/xiaohongshu/trending` | `xiaohongshu_trending_get` | 2 | Xiaohongshu’s explore feed for guests. |

### Instagram (beta)

Public Instagram profiles, posts and reels with like, comment and play counts, comments, similar accounts and post counts, in the shape of Instagram’s own media and user objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/instagram/users/{username}` | `instagram_user_get` | 1 | A public Instagram profile: bio, links, follower and post counts, highlights, and its latest posts. |
| `GET /v1/instagram/users/by-id/{user_id}` | `instagram_user_basic` | 1 | An Instagram profile looked up by numeric account id. |
| `GET /v1/instagram/users/{username}/post-count` | `instagram_user_post_count` | 1 | The exact number of posts on an Instagram profile. |
| `GET /v1/instagram/users/{username}/embed` | `instagram_user_embed` | 1 | The embed page Instagram serves for a profile (HTML), with its counts. |
| `GET /v1/instagram/users/{username}/posts` | `instagram_user_posts` | 1 | An Instagram account’s posts, newest first (12 a page) with like, comment and view counts. |
| `GET /v1/instagram/users/{username}/reels` | `instagram_user_reels` | 1 | An Instagram account’s reels (12 a page) with play, like and comment counts. |
| `GET /v1/instagram/posts/{shortcode}` | `instagram_post_get` | 1 | One Instagram post or reel: caption, counts incl. plays, media, tags, audio and location. |
| `GET /v1/instagram/posts/{shortcode}/comments` | `instagram_post_comments` | 2 | Comments on an Instagram post or reel, paginated (about 24 a page). |
| `GET /v1/instagram/users/{username}/similar` | `instagram_user_similar` | 3 | Accounts Instagram suggests as similar to an account. |
| `GET /v1/instagram/users/{username}/highlights` | `instagram_user_highlights` | 1 | The story highlights on an Instagram profile. |
| `GET /v1/instagram/highlights/{id}` | `instagram_highlight_get` | 1 | Every story in an Instagram highlight, with media and link stickers. |
| `GET /v1/instagram/reels/trending` | `instagram_trending_reels` | 2 | The reels Instagram’s public reels feed is showing right now. |
| `GET /v1/instagram/audio/{audio_id}/reels` | `instagram_audio_reels` | 1 | Reels that use an Instagram audio, with the audio’s reel count. |
| `GET /v1/instagram/search/popular` | `instagram_search_popular` | 1 | Instagram’s popular-search page for a topic: top posts, summary, related searches. |
| `GET /v1/instagram/search/reels` | `instagram_search_reels` | 1 | Instagram reels about a keyword, with captions and counts. |
| `GET /v1/instagram/search/hashtag` | `instagram_search_hashtag` | 1 | Instagram posts and reels carrying a hashtag. |
| `GET /v1/instagram/search/profiles` | `instagram_search_profiles` | 1 | Instagram profiles matching a name or topic, with counts. |
| `GET /v1/instagram/search` | `instagram_search_all` | 1 | Instagram accounts, hashtags and places matching a name. |
| `GET /v1/instagram/users/{username}/engagement` | `instagram_user_engagement` | 2 | Engagement metrics over an Instagram account’s latest posts. |
| `GET /v1/instagram/users/{username}/full` | `instagram_user_full` | 2 | An Instagram profile, a page of its posts with plays, and engagement metrics. |
| `GET /v1/instagram/users/{username}/posts/full` | `instagram_user_posts_full` | 2 | An Instagram account’s posts with reel play counts, up to 50 in one call. |
| `GET /v1/instagram/users/{username}/reels/full` | `instagram_user_reels_full` | 3 | An Instagram account’s reels loaded in full, with captions and play counts. |
| `GET /v1/instagram/posts/{shortcode}/comments/find` | `instagram_comment_get` | 2 | Find an Instagram comment by id, author or text. |
| `GET /v1/instagram/users/{username}/mentions` | `instagram_search_mentions` | 1 | Instagram posts by others that mention an account. |
| `GET /v1/instagram/locations/{location_id}` | `instagram_location_get` | 1 | An Instagram place: name, category, coordinates, address and post count. |
| `GET /v1/instagram/locations/{location_id}/posts` | `instagram_location_posts` | 2 | The top Instagram posts tagged at a place. |

### Yelp (beta)

Public Yelp businesses (details, hours, amenities, photos) and their reviews, incl. the not-recommended feed and date-window history, in the shape of Yelp Fusion’s Business and Review objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/yelp/businesses/{business}` | `yelp_business_info` | 1 | A Yelp business: rating and distribution, categories, price, contact, address, hours, amenities, photos. |
| `GET /v1/yelp/businesses/{business}/reviews` | `yelp_business_reviews` | 2 | A page of a Yelp business’s reviews (up to 49): sort, star filter, search, language, not-recommended feed. |
| `POST /v1/yelp/businesses/{business}/reviews/history` | `yelp_business_reviews_history` | 10 | Every review of a Yelp business in a date window, newest first (up to 500). |

### Tripadvisor (beta)

Public hotels, restaurants, attractions, tours and cruise ships: search, details, lists with filters and recent reviews, in Tripadvisor’s own GraphQL objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/tripadvisor/search` | `tripadvisor_search_all` | 1 | Search Tripadvisor places (hotels, restaurants, attractions, cities, ships) with full details. |
| `GET /v1/tripadvisor/autocomplete` | `tripadvisor_autocomplete_get` | 1 | Tripadvisor place suggestions for a partial name: ids, types and links. |
| `GET /v1/tripadvisor/place` | `tripadvisor_place_get` | 1 | Any Tripadvisor place by link or id: name, type, address, description, rating, tags. |
| `GET /v1/tripadvisor/reviews` | `tripadvisor_reviews_get` | 1 | Recent reviews Tripadvisor features for a place (up to 20), with author and trip info. |
| `GET /v1/tripadvisor/hotels` | `tripadvisor_hotels_get` | 1 | Hotels in a destination with Tripadvisor’s filters, sorts and prices, paginated. |
| `GET /v1/tripadvisor/hotel` | `tripadvisor_hotel_get` | 1 | A Tripadvisor hotel: rating, sub-ratings, amenities, price range, contact, description. |
| `GET /v1/tripadvisor/restaurants` | `tripadvisor_restaurants_get` | 1 | Restaurants in a destination with cuisine, meal, price and diet filters, paginated. |
| `GET /v1/tripadvisor/restaurant` | `tripadvisor_restaurant_get` | 1 | A Tripadvisor restaurant: cuisines, price range, hours, sub-ratings, contact, menu link. |
| `GET /v1/tripadvisor/restaurant/reviews` | `tripadvisor_restaurant_reviews` | 1 | Recent reviews Tripadvisor features for a restaurant (up to 20). |
| `GET /v1/tripadvisor/attractions` | `tripadvisor_attractions_get` | 1 | Tours and things to do in a destination with duration, rating and price filters, paginated. |
| `GET /v1/tripadvisor/attraction` | `tripadvisor_attraction_get` | 1 | A Tripadvisor attraction: categories, rating, description, address, visit length, tours. |
| `GET /v1/tripadvisor/attraction/reviews` | `tripadvisor_attraction_reviews` | 1 | Recent reviews Tripadvisor features for an attraction (up to 20). |
| `GET /v1/tripadvisor/experience-types` | `tripadvisor_experience_types_get` | 1 | The kinds of tours and experiences on offer in a destination, with counts and prices. |
| `GET /v1/tripadvisor/cruise` | `tripadvisor_cruise_get` | 1 | A cruise ship on Tripadvisor: rating, review count, description, photo. |
| `GET /v1/tripadvisor/cruise/reviews` | `tripadvisor_cruise_reviews` | 1 | Recent reviews Tripadvisor features for a cruise ship (up to 20). |

### Threads (beta)

Public Threads profiles, posts with like, reply, repost and quote counts, replies, and keyword and account search, in the shape of Threads’ own post and user objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/threads/users/{username}` | `threads_user_get` | 1 | A public Threads profile: bio, links, follower count, verification. |
| `GET /v1/threads/users/{username}/posts` | `threads_user_posts` | 1 | A Threads account’s posts, newest first (20 a page), with like, reply, repost and quote counts. |
| `GET /v1/threads/posts/{shortcode}` | `threads_post_get` | 1 | One Threads post with its counts, media, quoted post and the author’s thread. |
| `GET /v1/threads/posts/{shortcode}/replies` | `threads_post_comments` | 1 | Replies to a Threads post, top or newest first. |
| `GET /v1/threads/search/posts` | `threads_search_posts` | 1 | Search Threads posts by keyword, top or newest first. |
| `GET /v1/threads/search/users` | `threads_search_users` | 1 | Search Threads accounts by username or name. |

### Trustpilot (beta)

Public Trustpilot business profiles by website domain: TrustScore, star counts and the newest reviews, in the shapes Trustpilot’s own review widgets read.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/trustpilot/reviews` | `trustpilot_reviews_get` | 2 | A business on Trustpilot by its website domain: TrustScore, star counts and up to 100 newest reviews. |

### G2 (beta)

G2 software reviews (the newest reviews of a product, filterable by stars) and the full G2 category tree.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/g2/reviews` | `g2_reviews_get` | 1 | The newest reviews of a G2 product (about 25), with stars, reviewer and answers. |
| `GET /v1/g2/categories` | `g2_categories_get` | 1 | Every G2 software category, as a tree with parents and top-level groups. |

### Airbnb (beta)

Public Airbnb stays: search with dates, guests and filters, listing details, guest reviews and the availability calendar, as Airbnb’s own web app shows them logged out.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/airbnb/search` | `airbnb_search_all` | 1 | Search Airbnb stays by place or map box, with dates, guests and filters (18 a page). |
| `GET /v1/airbnb/listing` | `airbnb_listing_get` | 1 | One Airbnb listing: description, amenities, rules, host, photos, ratings, location. |
| `GET /v1/airbnb/listing/reviews` | `airbnb_listing_reviews` | 2 | Guest reviews of an Airbnb listing, newest first or by rating (up to 50 a page). |
| `GET /v1/airbnb/listing/availability` | `airbnb_listing_availability` | 2 | An Airbnb listing’s availability calendar: bookable days and stay limits, up to 12 months. |

### GitHub (live)

Public GitHub users, repositories, issues, pull requests, releases, contribution calendars, search and trending, in GitHub’s own REST v3 JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/github/users/{handle}` | `github_user_get` | 1 | A public GitHub user: name, bio, company, location, followers, following, public repo count. |
| `GET /v1/github/users/{handle}/repos` | `github_user_repos` | 1 | A GitHub user’s public repositories, sorted and paginated, with stars and languages. |
| `GET /v1/github/users/{handle}/activity` | `github_user_activity` | 1 | A GitHub user’s recent public activity: pushes, pull requests, issues, stars. |
| `GET /v1/github/users/{handle}/contributions` | `github_user_contributions` | 1 | A GitHub user’s contribution calendar for a year: daily counts and the total. |
| `GET /v1/github/users/{handle}/followers` | `github_user_followers` | 1 | Accounts that follow a GitHub user, paginated. |
| `GET /v1/github/users/{handle}/following` | `github_user_following` | 1 | Accounts a GitHub user follows, paginated. |
| `GET /v1/github/users/{handle}/pull-requests` | `github_user_pull_requests` | 1 | Pull requests a GitHub user opened, newest first, with since/until. |
| `GET /v1/github/users/{handle}/velocity` | `github_user_profile_velocity` | 5 | How fast a GitHub user ships: contributions, commits, PRs and repos over time. |
| `GET /v1/github/repos/{owner}/{repo}` | `github_repo_get` | 1 | A public GitHub repository: stars, forks, watchers, language, topics, license. |
| `GET /v1/github/repos/{owner}/{repo}/readme` | `github_repo_readme` | 1 | A GitHub repository’s README as text. |
| `GET /v1/github/repos/{owner}/{repo}/releases` | `github_repo_releases` | 1 | A GitHub repository’s releases, newest first, with since/until. |
| `GET /v1/github/repos/{owner}/{repo}/issues` | `github_repo_issues` | 1 | Issues and pull requests of a GitHub repository, filtered by state, labels and date. |
| `GET /v1/github/repos/{owner}/{repo}/top-issues` | `github_repo_top_issues` | 3 | The most-reacted open issues of a GitHub repository: top requests and complaints. |
| `GET /v1/github/repos/{owner}/{repo}/dossier` | `github_repo_dossier` | 3 | One-call dossier of a GitHub repository: details, README, releases, top issues, contributors. |
| `GET /v1/github/repos/{owner}/{repo}/issues/{number}` | `github_issue_get` | 1 | One GitHub issue or pull request with its body, labels and reactions. |
| `GET /v1/github/repos/{owner}/{repo}/issues/{number}/comments` | `github_issue_comments` | 1 | Comments on a GitHub issue or pull request, paginated, with since. |
| `GET /v1/github/search/issues` | `github_search_issues` | 1 | Search GitHub issues and pull requests with GitHub’s query syntax. |
| `GET /v1/github/search/repos` | `github_search_repos` | 1 | Search GitHub repositories by keyword, language, stars and more. |
| `GET /v1/github/trending/repositories` | `github_trending_repositories` | 1 | Trending GitHub repositories today, this week or this month, by language. |
| `GET /v1/github/trending/developers` | `github_trending_developers` | 1 | Trending GitHub developers today, this week or this month, by language. |

### Zillow (beta)

US homes for sale, for rent and recently sold: search with Zillow’s own filters, full property records (price and tax history, Zestimate, facts, photos) and location lookup, in Zillow’s own listing and property JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/zillow/search` | `zillow_search_all` | 1 | Zillow homes for sale, for rent or sold in a place or map box, with filters (41 a page). |
| `GET /v1/zillow/property` | `zillow_property_get` | 1 | One Zillow property: price, Zestimate, facts, photos, agent, price history. |
| `GET /v1/zillow/locations` | `zillow_locations_get` | 1 | Zillow places and addresses matching a query, with region ids and zpids. |

### Booking.com (beta)

Public Booking.com properties: search with dates and guests, property details, guest reviews and room types with the best available price, as Booking.com’s own web app shows them logged out.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/booking/search` | `booking_search_all` | 1 | Search Booking.com properties by place, with dates, guests and rooms (25 a page). |
| `GET /v1/booking/hotel` | `booking_hotel_get` | 1 | One Booking.com property: address, stars, review score, facilities, rooms and photos. |
| `GET /v1/booking/hotel/reviews` | `booking_hotel_reviews` | 2 | Guest reviews of a Booking.com property, with scores, stay details and replies (up to 25 a page). |
| `GET /v1/booking/hotel/rooms` | `booking_hotel_rooms` | 2 | A Booking.com property’s room types for a stay, with the best available price and nightly prices. |

### Jobs (beta)

Public job boards in their own shapes: a company’s open jobs on Greenhouse, Lever, Ashby and Workday, Levels.fyi jobs with pay, Xing job search and postings, and salary ranges by title and country (Talent.com).

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/jobs/greenhouse/search` | `jobs_greenhouse_search` | 1 | A company’s open jobs on its Greenhouse board, 50 a page. |
| `GET /v1/jobs/greenhouse/job` | `jobs_greenhouse_get` | 1 | One Greenhouse job with its full description, departments, offices and pay ranges. |
| `GET /v1/jobs/lever/search` | `jobs_lever_search` | 1 | A company’s open jobs on Lever, 50 a page, with descriptions and salary ranges. |
| `GET /v1/jobs/ashby/search` | `jobs_ashby_search` | 1 | A company’s open jobs on Ashby, 20 a page, with descriptions and compensation. |
| `GET /v1/jobs/workday/search` | `jobs_workday_search` | 1 | Search a company’s Workday careers site, 20 jobs a page. |
| `GET /v1/jobs/levels/search` | `jobs_levels_search` | 1 | Levels.fyi jobs with pay, grouped by company, with filters for level, pay and workplace. |
| `GET /v1/jobs/xing/search` | `jobs_xing_search` | 2 | Search Xing job postings (Germany, Austria, Switzerland) with salary, by keywords and filters. |
| `GET /v1/jobs/xing/job` | `jobs_xing_get` | 1 | One Xing job posting with its full description, salary, company and how to apply. |
| `GET /v1/jobs/salary/titles` | `jobs_salary_titles` | 1 | Job titles that match a partial title in a country, for a salary lookup. |
| `GET /v1/jobs/salary` | `jobs_salary_get` | 1 | Salary distribution for a job title in a country: median, percentiles, hourly, by region. |

### Redfin (beta)

US homes for sale and recently sold from Redfin’s map search, and a property’s facts, estimate and neighbourhood scores, in Redfin’s own JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/redfin/search` | `redfin_search_all` | 1 | Redfin homes for sale or sold in a region or map box, with filters (up to 350). |
| `GET /v1/redfin/property` | `redfin_property_get` | 1 | One Redfin property: facts, listing, estimate, parcel and walk/transit scores. |

### Goodreads (beta)

Public Goodreads books, community reviews and their comments, editions, search, authors, series, quotes and Listopia lists, in Goodreads’ own GraphQL objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/goodreads/book` | `goodreads_book_get` | 1 | A Goodreads book by id, link or ISBN: work stats, rating distribution, genres, series, awards. |
| `GET /v1/goodreads/book/reviews` | `goodreads_book_reviews` | 2 | Community reviews of a Goodreads book (up to 30 a page): sort, stars, language, keyword, dates. |
| `GET /v1/goodreads/review/comments` | `goodreads_review_comments` | 1 | Comments on a Goodreads review. |
| `GET /v1/goodreads/book/editions` | `goodreads_book_editions` | 1 | Every edition of a Goodreads book: format, pages, publisher, ISBNs, language. |
| `GET /v1/goodreads/search` | `goodreads_search_all` | 1 | Search Goodreads books by title, author or ISBN (20 a page). |
| `GET /v1/goodreads/author` | `goodreads_author_get` | 1 | A Goodreads author: bio, born/died, genres, ratings, followers, top books. |
| `GET /v1/goodreads/author/books` | `goodreads_author_books` | 1 | A Goodreads author’s works (30 a page), sorted by popularity, title, year, rating or pages. |
| `GET /v1/goodreads/quotes` | `goodreads_quotes_get` | 1 | Goodreads quotes by book, author, tag or words (30 a page). |
| `GET /v1/goodreads/series` | `goodreads_series_get` | 1 | A Goodreads series with every work in reading order. |
| `GET /v1/goodreads/lists` | `goodreads_lists_get` | 1 | Goodreads Listopia: a list’s ranked books, lists by tag, or the lists a book is on. |

### Realtor.com (beta)

US listings for sale, for rent and sold from Realtor.com’s search, and full property records, in Realtor.com’s own GraphQL shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/realtor/search` | `realtor_search_all` | 1 | Realtor.com listings for sale, for rent or sold in a place, with filters. |
| `GET /v1/realtor/property` | `realtor_property_get` | 1 | One Realtor.com property: listing, facts, price and tax history, schools, photos. |

### Apple Maps (beta)

Places and addresses from Apple Maps: search near a point or in a box, and place details by id, in Apple’s own place objects.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/applemaps/search` | `applemaps_search_all` | 1 | Search Apple Maps places and addresses, near a point or in a box. |
| `GET /v1/applemaps/places` | `applemaps_places_get` | 1 | Apple Maps places by id (up to 20): address, category, phone, website, timezone. |

### Google Ads Transparency Center (beta)

The Google Ads Transparency Center (ads on Google Search, YouTube, Google Play, Maps and Shopping): advertiser search, verified advertisers, an advertiser’s or website’s ads with region, platform, format and date filters, and one ad with its versions and regions.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/googleads/advertisers/search` | `googleads_advertisers_search` | 1 | Find advertisers and advertised websites in the Google Ads Transparency Center. |
| `GET /v1/googleads/advertisers/{advertiser}` | `googleads_advertiser_get` | 1 | A Google advertiser’s verified identity: name, legal name, region. |
| `GET /v1/googleads/ads` | `googleads_ads_list` | 2 | The ads of a Google advertiser or website, 40 a page, by region, platform, format and dates. |
| `GET /v1/googleads/ads/{creative}` | `googleads_ad_get` | 2 | One Google ad: every version and the regions it ran in. |

### Google (beta)

Google Search results (web with knowledge graph, answer box, top stories, people also ask and related searches; images, videos, news, shopping and local places, with country, language, location and time filters), public Google Maps places (search, place cards with hours, attributes and photos, their rating summaries and the reviews shown to logged-out visitors), Google Hotels search with nightly rates, Google search suggestions and Google Patents search.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/google/business/search` | `google_business_search` | 2 | Search Google Maps businesses: names, addresses, ratings, phones, hours, ids. |
| `GET /v1/google/business/info` | `google_business_info` | 1 | A Google Maps place card: address, rating, hours, attributes, contact, photos. |
| `GET /v1/google/business/reviews` | `google_business_reviews` | 1 | A Google Maps place’s rating histogram and the reviews shown logged out. |
| `GET /v1/google/business/photos` | `google_business_photos` | 1 | The photos on a Google Maps place card, full size. |
| `GET /v1/google/autocomplete` | `google_search_autocomplete` | 1 | Google’s search suggestions for a partial query (web, YouTube, News, Shopping). |
| `GET /v1/google/patents` | `google_search_patents` | 1 | Search Google Patents: titles, dates, inventors, assignees, PDFs. |
| `GET /v1/google/hotels/search` | `google_hotels_search` | 1 | Search Google Hotels: names, classes, ratings, nightly rates for your dates. |
| `GET /v1/google/hotels/info` | `google_hotels_info` | 2 | One Google Hotels listing: ratings by category, rate, times, description. |
| `GET /v1/google/search` | `google_search_web` | 1 | Google web search: organic results, knowledge graph, answer box, top stories, PAA, related. |
| `GET /v1/google/search/images` | `google_search_images` | 1 | Google image search: image and thumbnail URLs, sizes, source page; up to 100. |
| `GET /v1/google/search/videos` | `google_search_videos` | 1 | Google video search: title, link, thumbnail, duration, channel, date. |
| `GET /v1/google/search/news` | `google_search_news` | 1 | Google Search news tab: headlines, publishers, times, links. |
| `GET /v1/google/search/shopping` | `google_search_shopping` | 2 | Google Shopping: products, prices, sellers, ratings, catalog ids. |
| `GET /v1/google/search/places` | `google_search_places` | 1 | Google local results: places with address, rating, category and Maps ids. |
| `GET /v1/google/search/scholar` | `google_search_scholar` | 1 | Google Scholar: papers with authors, venue, year, citations and PDF links. |

### Google News (beta)

Google News search: the articles Google News finds for a query in an edition, with headline, publisher, publish time and link.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/googlenews/search` | `googlenews_search_all` | 1 | Search Google News: headlines, publishers, publish times, links; up to 100. |

### Web (beta)

Any public web page read into clean Markdown, HTML, text, links and metadata, a site’s URL map from its sitemaps and links, small synchronous crawls and batches, fetched as the server sends it through a residential pool.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/web/scrape` | `web_scrape_get` | 1 | Any public web page as Markdown, HTML, text, links and metadata. |
| `GET /v1/web/map` | `web_map_get` | 1 | A site’s URLs from its sitemaps and links. |
| `POST /v1/web/crawl` | `web_crawl_get` | 5 | Crawl a site from a URL: up to 10 pages as Markdown in about 25 s, with a cursor. |
| `POST /v1/web/batch-scrape` | `web_batch_scrape_get` | 5 | Up to 10 web pages as Markdown in one call. |
| `GET /v1/web/search` | `web_search_all` | 2 | Search the web: titles, URLs, snippets and news, optionally with page content. |

### Wikipedia (beta)

Wikipedia articles as plain text with description, image, categories and last revision, and full-text search, in any language edition, in the MediaWiki API’s own shapes.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/wikipedia/article` | `wikipedia_article_get` | 1 | A Wikipedia article as plain text, with description, image, categories. |
| `GET /v1/wikipedia/search` | `wikipedia_search_all` | 1 | Search a Wikipedia edition: titles, snippets, sizes, last edits. |

### Bing (beta)

Bing web results with markets, safe search and time ranges, rank checks up to 200 deep, image search with Bing’s filters, video search and suggestions, as Bing shows them to a logged-out visitor.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/bing/search` | `bing_search_all` | 1 | Bing web results: titles, URLs, snippets, dates, related searches. |
| `GET /v1/bing/rank` | `bing_rank_get` | 5 | Where a domain or URL ranks on Bing for a query, up to 200 deep. |
| `GET /v1/bing/images` | `bing_images_get` | 1 | Bing image search with size, type, color, aspect and license filters. |
| `GET /v1/bing/videos` | `bing_videos_get` | 2 | Bing video search: titles, URLs, durations, views, creators. |
| `GET /v1/bing/suggestions` | `bing_suggestions_get` | 1 | Bing’s search suggestions for a partial query. |
| `GET /v1/bing/shopping/search` | `bing_shopping_search` | 1 | Search Bing Shopping: products, prices, sellers, images. |
| `GET /v1/bing/shopping/product` | `bing_shopping_product` | 1 | A Bing Shopping product’s offers by seller, and its specs. |

### DuckDuckGo (beta)

DuckDuckGo web results with regions, safe search, time ranges and paging, rank checks up to 200 deep, news and video search, Instant Answers and autocomplete, from DuckDuckGo’s own logged-out pages and JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/duckduckgo/search` | `duckduckgo_search_all` | 1 | DuckDuckGo web results: titles, URLs, snippets, with paging. |
| `GET /v1/duckduckgo/rank` | `duckduckgo_rank_get` | 5 | Where a domain or URL ranks on DuckDuckGo for a query, up to 200 deep. |
| `GET /v1/duckduckgo/news` | `duckduckgo_news_get` | 1 | DuckDuckGo News: titles, excerpts, sources, dates, images. |
| `GET /v1/duckduckgo/videos` | `duckduckgo_videos_get` | 1 | DuckDuckGo Videos: URLs, durations, publishers, view counts. |
| `GET /v1/duckduckgo/instant-answer` | `duckduckgo_instant_answer_get` | 1 | DuckDuckGo’s Instant Answer for a topic: abstract, infobox, related topics. |
| `GET /v1/duckduckgo/suggestions` | `duckduckgo_suggestions_get` | 1 | DuckDuckGo’s search suggestions for a partial query. |

### Baidu (beta)

Baidu web search: titles, target URLs, snippets and card types, as Baidu’s mobile results page shows them to a logged-out visitor.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/baidu/search` | `baidu_search_all` | 1 | Baidu web results: titles, URLs, snippets, card types. |

### Google Trends (beta)

Google Trends interest over time for up to five keywords, related and rising queries and topics, and Trending Now per country with volumes and growth, from the Trends web app’s own JSON.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/googletrends/explore` | `googletrends_explore_get` | 3 | Google Trends interest over time (0-100) for up to five keywords. |
| `GET /v1/googletrends/rising` | `googletrends_rising_get` | 3 | A keyword’s top and rising related queries and topics on Google Trends. |
| `GET /v1/googletrends/trending` | `googletrends_trending_get` | 3 | Google Trends Trending Now for a country: volume, growth, related terms. |

### On-page SEO (beta)

An on-page SEO audit of any public URL: status and timing, title and description, headings, canonical and robots, links, images without alt, structured data, social tags and hreflang, with pass/fail checks and a score.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/onpage/page` | `onpage_page_get` | 1 | On-page SEO audit of one URL: tags, headings, links, schema, checks, score. |

### Naver (beta)

Naver (Korea) search: blog posts, news and cafe articles with sort, date range and paging, in the shapes of Naver’s own Search Open API, read from its logged-out search pages.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/naver/blog/search` | `naver_blog_search` | 1 | Search Naver Blog: titles, links, snippets, bloggers, dates. |
| `GET /v1/naver/news/search` | `naver_news_search` | 1 | Search Naver News: titles, links, snippets, publishers, times. |
| `GET /v1/naver/cafearticle/search` | `naver_cafearticle_search` | 1 | Search Naver Cafe articles: titles, links, snippets, cafes, dates. |
| `GET /v1/naver/kin/search` | `naver_kin_search` | 1 | Search Naver KnowledgeiN: questions, links, top answers, dates. |
| `GET /v1/naver/blog` | `naver_blog_get` | 1 | A Naver blog’s card: name, description, post count, visitor counter. |
| `GET /v1/naver/blog/posts` | `naver_blog_posts` | 1 | Every post of a Naver blog, newest first, 30 a page. |
| `GET /v1/naver/image/search` | `naver_image_search` | 1 | Search Naver Images: original URLs, thumbnails, sizes, source pages. |
| `GET /v1/naver/webkr/search` | `naver_webkr_search` | 1 | Search Naver Web documents: titles, links, descriptions. |
| `GET /v1/naver/local/search` | `naver_local_search` | 1 | Search Naver Local in the Open API shape: names, categories, addresses, phones. |
| `GET /v1/naver/brief` | `naver_brief_get` | 5 | One query across Naver blog, news, cafe, KnowledgeiN and web. |
| `GET /v1/naver/errata` | `naver_errata_get` | 1 | Naver’s correction of a mistyped Korean query (오타변환). |
| `GET /v1/naver/adult` | `naver_adult_get` | 1 | Whether Naver treats a query as adult-only. |
| `GET /v1/naver/place/search` | `naver_place_search` | 2 | Search Naver Map places for a keyword, in Naver’s order. |
| `GET /v1/naver/place/rank` | `naver_place_rank` | 4 | Where a place ranks on Naver’s local results for up to 10 keywords. |
| `GET /v1/naver/place` | `naver_place_get` | 2 | A Naver Place card: addresses, review totals, menus, hours. |
| `GET /v1/naver/place/reviews` | `naver_place_reviews` | 3 | The newest or recommended visitor reviews of a Naver Place. |

## Cross-platform tools

### Utility (beta)

Free discovery for agents, across every platform here: quickstart, endpoint search and detail, plain-words task planning, URL and handle resolution, cost estimates, error explanations, recipes, docs search and an llms.txt-style context payload. Needs no API key.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/utility/quickstart` | `utility_quickstart_get` | 0 | Get started in one call: how to authenticate, pay and make a first call, for one platform or all. |
| `GET /v1/utility/endpoints` | `utility_endpoints_list` | 0 | Every callable endpoint, filterable by platform, method and words, with price and inputs. |
| `GET /v1/utility/endpoint` | `utility_endpoint_get` | 0 | How to use one endpoint (by id, tool name or a URL): inputs with types, example call, price. |
| `GET /v1/utility/capabilities` | `utility_capabilities_get` | 0 | The parameters that work across endpoints (cursors, date windows, limits) and where each is accepted. |
| `GET /v1/utility/plan` | `utility_plan_get` | 0 | A task in plain words turned into a chain of calls, with inputs filled in and a cost estimate. |
| `GET /v1/utility/find` | `utility_find_get` | 0 | The endpoints that fit a task, ranked. |
| `GET /v1/utility/resolve` | `utility_resolve_get` | 0 | Identifies URLs, @handles and ids: the platform, the endpoint to call and its inputs. |
| `GET /v1/utility/estimate` | `utility_estimate_get` | 0 | Quotes the credits and keyless USD of a call, a list of calls or a plan. |
| `GET /v1/utility/explain-error` | `utility_explain_error_get` | 0 | Explains a failed response (status or error body): what it means and what to do next. |
| `GET /v1/utility/recipes` | `utility_recipes_list` | 0 | Ready-made multi-call recipes for common jobs, with their cost. |
| `GET /v1/utility/docs-search` | `utility_docs_search_get` | 0 | Searches the API docs: platforms, endpoints and their guidance. |
| `GET /v1/utility/llms` | `utility_llms_get` | 0 | An AI-agent context payload (llms.txt style) for one platform or all. |

### Cross-platform search (beta)

One query asked of each platform’s own search at once (Reddit, X, Bluesky, Threads, TikTok, YouTube, Hacker News, Pinterest, Stack Overflow and more), side by side or merged into one ranked list, with a status per platform; only platforms that answer are charged, at their own prices.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/search/multi` | `search_multi_get` | 30 | One query, each platform’s own search results side by side, with a status per platform. Metered: each platform that answers at its own price. |
| `GET /v1/search/everywhere` | `search_everywhere_get` | 20 | One query (or up to 5 keywords) across platforms, merged into one ranked list with a date window. Metered per platform that answers. |
| `POST /v1/search/everywhere` | `search_everywhere_batch` | 100 | Up to 5 search-everywhere requests in one call. Metered per platform that answers. |
| `GET /v1/search/forums` | `search_forums_get` | 10 | Reddit, Hacker News and Stack Overflow searched together, with top comments on the most discussed threads. Metered. |
| `GET /v1/search/creators` | `search_creators_get` | 15 | Accounts matching a niche on X, Bluesky, Threads, YouTube and TikTok, ranked by followers. Metered. |

### Creator tools (beta)

A creator’s other social profiles and their publicly listed business emails, read from their own bio, profile links and link-in-bio pages on the platforms here. Only what the creator published; nothing guessed.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/tools/find-social-profiles` | `tools_creator_find_profiles` | 10 | A creator’s accounts on other platforms, from the links in their bio and link-in-bio pages. Metered per page read. |
| `GET /v1/tools/find-creator-emails` | `tools_creator_find_emails` | 10 | Business emails a creator lists publicly in their bio or link-in-bio pages, with where each was found. Metered per page read. |

### Prism composites (beta)

Composite jobs over the platforms here, in one call: any link to its detail, every comment on a post, a video’s detail with transcript and comments, one handle across platforms, creator vetting, mentions, share of voice, leads, audience questions, app and product reviews, developer buzz. Built from each platform’s own endpoints, metered so only reads that answer are charged.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/prism/lookup` | `prism_lookup_get` | 5 | Any post, video, profile, product or app link → the right detail endpoint, at that endpoint’s own price. |
| `GET /v1/prism/comments` | `prism_comments_get` | 50 | Every comment on a post or video link, page after page. Metered per page read. |
| `GET /v1/prism/video-intel` | `prism_video_intel_get` | 15 | One video link → detail, stats, transcript, top comments and a commenter sample. Metered. |
| `POST /v1/prism/post-stats` | `prism_post_stats_get` | 500 | Up to 100 post links → current engagement each; failed links not charged. Metered. |
| `POST /v1/prism/post-comments` | `prism_post_comments_get` | 250 | Up to 25 post links → each post’s comments. Metered per page read. |
| `POST /v1/prism/comment-lookup` | `prism_comment_lookup_get` | 50 | Re-check up to 25 known comments: current text, score, still there. Metered. |
| `GET /v1/prism/creator-card` | `prism_creator_card_get` | 8 | One handle on TikTok, Instagram, YouTube, X and more: one card per platform found. Metered. |
| `GET /v1/prism/handle-audit` | `prism_handle_audit_get` | 8 | Scores a handle across platforms and ranks the accounts found. Metered. |
| `POST /v1/prism/profiles` | `prism_profiles_get` | 250 | Up to 50 (platform, handle) pairs → one profile card each. Metered. |
| `GET /v1/prism/voice` | `prism_voice_get` | 5 | One handle’s posts on X, Threads, Bluesky, Truth Social and Gab, merged newest first. Metered. |
| `GET /v1/prism/profile/comments` | `prism_user_comments` | 60 | New comments on a profile’s recent posts, in one list, newest first. Metered. |
| `GET /v1/prism/format-lift` | `prism_format_lift_get` | 4 | Which post format works for a creator, against their own median. Metered. |
| `GET /v1/prism/creator-vet` | `prism_creator_vet_get` | 50 | Engagement quality, cadence and comment authenticity signals for a creator. Metered. |
| `GET /v1/prism/audience-language` | `prism_audience_language_get` | 26 | Language mix of the comments on a creator’s recent posts. Metered. |
| `GET /v1/prism/audience-overlap` | `prism_audience_overlap_get` | 20 | How much two creators’ commenter audiences overlap (Jaccard). Metered. |
| `GET /v1/prism/truthsocial-pulse` | `prism_truthsocial_pulse_get` | 20 | A Truth Social handle: profile, posts, top posts in detail and the echo elsewhere. Metered. |
| `GET /v1/prism/mentions` | `prism_mentions_get` | 9 | Public posts that mention a handle, name or link, from the first page of each platform’s search. Metered. |
| `GET /v1/prism/brand-mentions` | `prism_brand_mentions_get` | 50 | Brand mention series, sentiment split, top sources and recent mentions for one keyword. Metered. |
| `GET /v1/prism/share-of-voice` | `prism_share_of_voice_get` | 100 | Engagement-weighted share of voice for 2-5 brands, with sentiment and ESOV. Metered. |
| `GET /v1/prism/leads` | `prism_leads_get` | 50 | Public posts where people look for alternatives to, or switch from, a competitor. Metered. |
| `GET /v1/prism/comment-leads` | `prism_comment_leads_get` | 60 | Buyer leads from the comments under a keyword search’s most discussed posts. Metered. |
| `GET /v1/prism/audience-questions` | `prism_audience_questions_get` | 30 | The questions a topic’s audience asks on Reddit, YouTube, Hacker News and Stack Overflow. Metered. |
| `GET /v1/prism/campaign` | `prism_campaign_get` | 35 | A hashtag or phrase before, during and after a campaign: volume, lift, amplifiers. Metered. |
| `GET /v1/prism/crisis-radar` | `prism_crisis_radar_get` | 45 | Stateless crisis check: z-scores on daily mention volume and negative share. Metered. |
| `GET /v1/prism/crisis-postmortem` | `prism_crisis_postmortem_get` | 35 | Crisis timeline: who said what first, per platform, with daily volume and sentiment. Metered. |
| `GET /v1/prism/earliness` | `prism_earliness_get` | 25 | How early a term was seen on each platform and in the Meta Ad Library. Metered. |
| `GET /v1/prism/trend-board` | `prism_trend_board_get` | 30 | What is rising in one country today: TikTok, YouTube, Pinterest, X and Bluesky trends. Metered. |
| `GET /v1/prism/employer-brand` | `prism_employer_brand_get` | 30 | What people say about working at a company, across Reddit, Hacker News, YouTube and LinkedIn. Metered. |
| `GET /v1/prism/creators` | `prism_creators_get` | 100 | Creators who post about a niche, with followers, bio and public contact, filtered and ranked. Metered. |
| `GET /v1/prism/discover` | `prism_discover_get` | 30 | Search many platforms and keep only rows passing your filters (views, likes, words, languages). Metered. |
| `GET /v1/prism/find-accounts` | `prism_find_accounts_get` | 29 | A company’s or brand’s candidate accounts on X, Bluesky, Threads, YouTube, LinkedIn and GitHub. Metered. |
| `POST /v1/prism/discover/inputs` | `prism_discover_inputs` | 0 | Stores an author or exclude list for 30 days, for prism discover and creators. Free. |
| `GET /v1/prism/apps-lookup` | `prism_apps_lookup_get` | 30 | One app across the App Store and Google Play, title-matched and compared. Metered. |
| `GET /v1/prism/app-reviews` | `prism_app_reviews_get` | 15 | An app’s recent reviews on both stores: ratings, star sentiment, velocity, praised and complained words. Metered. |
| `GET /v1/prism/reputation` | `prism_reputation_get` | 30 | A brand’s reputation blended from Trustpilot, app stores, G2 and Reddit. Metered. |
| `GET /v1/prism/product-reviews` | `prism_product_reviews_get` | 30 | A product’s reviews across Amazon, Walmart and Trustpilot, folded into one rating. Metered. |
| `GET /v1/prism/review-integrity` | `prism_review_integrity_get` | 30 | Statistical integrity signals for a product’s or app’s reviews, with a verdict. Metered. |
| `POST /v1/prism/reviews/bulk` | `prism_reviews_bulk` | 100 | Reviews for up to 20 businesses or apps on Yelp, Tripadvisor, app stores, Trustpilot or G2. Metered. |
| `GET /v1/prism/devtool-pulse` | `prism_devtool_pulse_get` | 20 | A developer tool’s GitHub dossier, Hacker News reaction, Reddit chatter, Stack Overflow and npm. Metered. |
| `GET /v1/prism/launch-echo` | `prism_launch_echo_get` | 20 | How a launch landed on Hacker News, Reddit and Bluesky, with the repo’s releases. Metered. |
| `GET /v1/prism/org-radar` | `prism_org_radar_get` | 51 | A GitHub organization’s repositories, with the top ones expanded into dossiers. Metered. |
| `GET /v1/prism/brief-check` | `prism_brief_check_get` | 15 | Checks a creator post against a brief: talking points, forbidden claims, disclosure. Metered. |
| `GET /v1/prism/demand-signals` | `prism_demand_signals_get` | 30 | Demand nowcast for a keyword: mention velocity, app review velocity, Amazon search. Metered. |

### Content analysis (beta)

Citations of a keyword in posts, videos and forum threads on the platforms here (not the open web), each with lexicon sentiment, and the summaries, sentiment breakdowns and phrase trends built from them.

| Endpoint | MCP tool | Credits | What it returns |
| --- | --- | --- | --- |
| `GET /v1/contentanalysis/search` | `contentanalysis_search_all` | 20 | Citations of a keyword in posts, videos and forum threads, each with lexicon sentiment. Metered. |
| `GET /v1/contentanalysis/summary` | `contentanalysis_summary_get` | 20 | Aggregate summary of a keyword’s citations: sentiment, platforms, authors, languages, terms. Metered. |
| `GET /v1/contentanalysis/sentiment` | `contentanalysis_sentiment_get` | 20 | Sentiment breakdown of a keyword’s citations, overall and per platform. Metered. |
| `GET /v1/contentanalysis/phrase-trends` | `contentanalysis_phrase_trends_get` | 20 | A keyword’s citations and sentiment per day, week or month. Metered. |
| `GET /v1/contentanalysis/languages` | `contentanalysis_languages_get` | 0 | The language codes content analysis tells apart. |
| `GET /v1/contentanalysis/locations` | `contentanalysis_locations_get` | 0 | The country codes the platforms here accept, and the endpoints that take one. |
| `GET /v1/contentanalysis/filters` | `contentanalysis_filters_get` | 0 | The fields the content analysis filters accept. |

