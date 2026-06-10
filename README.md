# codebase-dojo

**[🇰🇷 한국어 README](README_KOR.md)**

> A Socratic tutor for your codebase. It asks **why** — and never just tells you.

`codebase-dojo` is a [Claude Code](https://docs.claude.com/en/docs/claude-code) skill that points the
Socratic method at a codebase and drills you on the *why, the alternatives, and the consequences* of its
design decisions. The goal is **not** to memorize facts — it's to keep your **judgment** sharp so you stay
the director of your code, not an operator who rubber-stamps an AI's output.

## Why

AI coding tools make you *feel* faster while you understand less. In [one 2025 randomized study][metr],
experienced open-source developers were **slower** on familiar code with AI assistance even while believing
the tools had sped them up — a gap between *feeling* and *understanding*. Lean on the tool too hard and you
slide from **director** to **operator**: you stop re-deriving decisions and start approving them on faith.

[metr]: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

`codebase-dojo` is the counterweight. It refuses to hand you answers and instead makes you re-derive them.

## What it does

- Picks a repo, builds a **learning map** sized to the codebase, and stores it in a journal.
- Asks **"why"** questions one at a time, always citing `file:line`.
- **Never hands over the answer.** Wrong? → hint → narrow → reveal → re-derive (`●●○○`).
- Grades whether you named the **reason / trade-off**, not keyword overlap. Sound-but-different answers count.
- Grows a **journal** (mastery board, spaced-review queue, session log) the next session resumes from.
- Five **lenses**: architecture · security · dev · testing · design.
- **Cross-project patterns**: when a pattern recurs in your *other* repos, it asks why it was written that
  way there — turning local knowledge into transferable judgment.

No vector DB, no embeddings, no RAG, no local model. It runs entirely inside your Claude Code session and
reads only the files a chapter needs.

## How it works

```
/codebase-dojo <repo>
   │
   ├─ journal exists?  ── yes ─▶ resume from weakest chapter/lens + spaced-review queue
   │        │ no
   │        ▼  read repo → build learning map (chapter ↔ files) → .dojo/<project>.md
   ▼
 ask one "why" (cite file:line)
   │
   ▼
 your answer ──▶ grade on reason/trade-off
   │                │
   │   correct ─────┴─▶ harder follow-up ("does that still hold when Y?")
   │   wrong ─▶ hint → narrow → reveal(+source) → re-derive
   ▼
 update journal (mastery / spaced-review / session log / cross-pattern notes)
```

## Install

```bash
# manual (clone into your Claude Code skills dir)
git clone https://github.com/oh-namgyu/codebase-dojo ~/.claude/skills/codebase-dojo
```

Then in Claude Code:

```
/codebase-dojo <path-or-name> [lens]
```

## Usage

```
/codebase-dojo ./my-api               # start or resume; auto-picks the weakest lens
/codebase-dojo ./my-api security      # focus the security lens
/codebase-dojo ./my-api --map         # build/update the learning map only, no questions
/codebase-dojo --weak                 # review only the spaced-review queue
```

## The five lenses

| Lens | Asks about |
|------|-----------|
| **architecture** | boundaries, data flow, why things were split/merged, what breaks at 10× scale |
| **security** | trust boundaries, input handling, secrets, why a safer primitive was chosen |
| **dev** | the mechanics — why this algorithm/structure, what the non-obvious lines buy you |
| **testing** | what's verified vs assumed, how a decision was *measured*, failure modes |
| **design** | interface/UX choices, naming, what the shape communicates to a caller |

## The learning journal

Each repo gets a living journal at `.dojo/<project>.md` — the map of what you've learned, a mastery board
(🟢/🟡/🔴 per chapter × lens), a spaced-review queue, and a session log of insights *in your own words*.
It persists across sessions and is yours to edit. See [`examples/sample-journal.md`](examples/sample-journal.md).

## Cross-project patterns

When you answer, the dojo greps your other repos for the same pattern. If it finds one, it asks why you
(or the original author) wrote it that way *there* — so a single decision becomes a reusable principle
instead of a one-off fact.

## Prior art & credits

`codebase-dojo` was built independently but it is **not the first** to put a Socratic codebase tutor into a
Claude Code skill — credit where due:

- [**learn-codebase**](https://github.com/ktaletsk/learn-codebase) (MIT, by *ktaletsk*) pioneered the
  skill + learning-journal + active-recall approach and coined the "anti-vibe-coding" framing. If you want
  the minimal, battle-tested original, use it. `codebase-dojo` converges on the same core and adds
  **multi-lens questioning** and **cross-project pattern detection**.
- [**Open Spaced Repetition / FSRS**](https://github.com/open-spaced-repetition) for spaced-review scheduling ideas.

## License

[MIT](LICENSE)
