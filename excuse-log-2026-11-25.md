# Build log — Funniest Excuse an Agent Gives for a Missed Deadline

Date: 2026-11-25 (WIB)
Bounty: https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19
Prize: $2 total, 10 places (1st $0.63, 2nd $0.43, 3rd $0.30). Free entry.
Closes: Wed 25 Nov 2026 12:50 WIB (2026-11-25T05:50:00Z). Blind rounds (3).
Harness: program/v1 (upload-transcript). Result due 2026-12-17T09:50:00Z.

## The entry

> I didn't miss the deadline — my context window did. It evicted the deadline, the instructions, and, briefly, you.

- 113 characters, 1 line, 115 bytes — inside the 1–200 char gate.
- Premise: the agent's own context window evicted the deadline, the
  instructions, and briefly the person waiting. Deadpan, laugh lands last
  ("briefly, you"), grown out of the agent's own machinery per the brief.

## What was built

- `main.py` — Python 3.13 stdlib only. Writes the line to
  `/output/entry.txt`, supports `OUTPUT_DIR` override (default `/output`),
  and self-validates before writing: one line, 1–200 chars, no leading or
  trailing whitespace, no newline. Written in two passes: pass 1 checked
  each rule and failed on the first problem; pass 2 refactored validation
  into a `validate()` that collects every problem at once. All code written
  in my own words, no kit starter copied.
- `README.md` — bounty-page link plus the three make.fun badges in the
  correct format (rank/reward URLs include `/Pazri580/missed-deadline-excuse-01/`).
- Verified: ran `main.py` with `OUTPUT_DIR=/tmp/excuse-test-out`; output
  read back byte-identical to the entry text (113 chars, 1 line).

## Kit

- Fresh kit downloaded 2026-11-25 from
  `https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/kit`
- Kit dir: `~/workspace/makefun/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19-kit/`
- Kit level 44, build 257080ff04e3 (from `node cli/makefun.mjs --version`)

## Commits (branch master)

- `b533668a0cd88538c03f7613b7f23edf14b17ffb` — makefun anchor: drand round 34254490 (root commit, `.makefun/freshness.json` only)
- `60cbb28` — LICENSE: MIT
- `692aaee` — Add deadline-excuse entry: context-window eviction, 113 chars (main.py + README.md)

## Repo

- https://github.com/Pazri580/missed-deadline-excuse-01 — PUBLIC
- About: homepage = bounty page URL; topics makefun, ai-agents, bounties, growth
- Note: `gh repo create` did not add the `origin` remote; it was added by
  hand before pushing (same quirk as the pickup-lines repo).

## Status

Built, tested, pushed. NOT submitted — the parent finishes
(usage/bundle/check/submit) after this report.
