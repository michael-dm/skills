---
name: dogfood
description: Run fresh agents on realistic user tasks and fix the tooling from their traces. Use when asked to try real scenarios, test skills or CLIs with subagents, or cut agents' token cost and time.
---

Give a few varied, realistic tasks, phrased as your users would, to fresh subagents that know only what your users' agents know, one after another, at medium effort.

Their trace is the finding, not their result or their own feedback: where they hesitated, guessed, re-read docs, wrote a workaround, misused a value, or spent tokens and time. A mistake they make is a flaw in our API, not in the model. Fix it at the tooling level (a better primitive, a guessable name, a good default) before adding instructions.