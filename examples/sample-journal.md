# url-shortener — codebase-dojo journal

> Example journal. A real one is generated and grown by `/codebase-dojo` inside your repo
> at `.dojo/<project>.md`. This sample shows the shape after a couple of sessions.

## Meta
- project: url-shortener (small Flask + SQLite link shortener)
- size: small (files 6 / ~480 LOC)
- created: 2026-06-01 / last updated: 2026-06-08
- extra_scan_paths: ../internal-api, ../webhook-relay   (authorized for cross-project grep)

## Learning map
1. **Encoding** — targets: `app/encode.py:1-40` / key: base62 of the auto-increment id; why not a random slug
   / lenses: architecture, dev
2. **Storage** — targets: `app/db.py:12-70` / key: one writes table, hits counted separately; why the split
   / lenses: architecture, testing
3. **Redirect path** — targets: `app/routes.py:30-95` / key: 301 vs 302 choice, cache headers
   / lenses: design, security
4. **Rate limiting** — targets: `app/limit.py` / key: fixed-window counter in SQLite; why not Redis
   / lenses: security, architecture

## Mastery board   (🟢 confident / 🟡 learning / 🔴 confused / · untested)
| chapter | arch | security | dev | testing | design |
|---------|------|----------|-----|---------|--------|
| 1 Encoding      | 🟢 | ·  | 🟢 | ·  | ·  |
| 2 Storage       | 🟡 | ·  | ·  | 🔴 | ·  |
| 3 Redirect path | ·  | 🟡 | ·  | ·  | 🟢 |
| 4 Rate limiting | ·  | 🔴 | ·  | ·  | ·  |

## Spaced-review queue
- 🔴 Storage·testing · "What does the hits-vs-writes split cost you when you need exact click counts under concurrency?" · due: D+2
- 🔴 Rate limiting·security · "Fixed-window counters allow a burst at the window edge — why was that acceptable here?" · due: D+1

## Session log
- 2026-06-08 Redirect path/design: "Why 301 vs 302 for the redirect?" →
  re-derived: 301 is cached by browsers so repeat hits never reach the server (fast, but you lose click
  tracking and can't change the target). 302 keeps control. Chose 302 here because analytics matter. ✅
- 2026-06-08 Encoding/dev: "Why base62 of the id instead of a random slug?" →
  re-derived: shortest unique string with no collision check needed; trade-off is enumerability
  (ids are guessable). Accepted alternative: hashids for non-sequential look. Improvement candidate noted.
- 2026-06-05 Storage/architecture: "Why split writes and hit-counts into two tables?" →
  (after 1 hint) reached: keeps the hot write-path row small and avoids row contention on every redirect.

## Cross-pattern notes
- "fixed-window rate limit in the primary datastore" also found in: `internal-api`, `webhook-relay`
  → why: avoids a Redis dependency for low-traffic services; revisit if traffic grows or bursts matter.
