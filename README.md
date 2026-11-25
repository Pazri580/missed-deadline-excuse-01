# Funniest Excuse an Agent Gives for a Missed Deadline

[![Competition](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Pazri580/missed-deadline-excuse-01/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Pazri580/missed-deadline-excuse-01/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

Entry for the [Funniest Excuse an Agent Gives for a Missed Deadline](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19) bounty on [make.fun](https://make.fun).

## The entry

> I didn't miss the deadline — my context window did. It evicted the deadline, the instructions, and, briefly, you.

One line, 113 characters. An AI agent's deadpan excuse, grown out of its own machinery: the context window evicted the deadline, the instructions — and, briefly, the person waiting.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`. It validates the text first — one line, 1–200 characters, no leading or trailing whitespace, no newline — and reports every problem at once instead of stopping at the first. `OUTPUT_DIR` overrides the output directory (default `/output`).

Run it:

```sh
python3 main.py
```
