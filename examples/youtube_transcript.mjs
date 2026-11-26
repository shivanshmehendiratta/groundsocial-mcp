// Fetch a YouTube transcript with plain fetch (Node 18+).
//   export GROUNDSOCIAL_API_KEY=gs_live_...
//   node youtube_transcript.mjs dQw4w9WgXcQ
const id = process.argv[2] ?? 'dQw4w9WgXcQ'
const res = await fetch(
  `https://api.groundsocial.dev/v1/youtube/videos/${id}/transcript?language=en`,
  { headers: { Authorization: `Bearer ${process.env.GROUNDSOCIAL_API_KEY}` } },
)
const body = await res.json()
if (!res.ok) {
  // Errors carry code, hint and retryable
  console.error(body)
  process.exit(1)
}
console.log(JSON.stringify(body, null, 2).slice(0, 2000))
console.log('credits charged:', res.headers.get('x-credits-charged'))
