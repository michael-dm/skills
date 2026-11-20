---
name: brief
description: Brief the user on a branch, PR or thread as if they had zero context. Use when asked to catch them up, explain a PR or its decisions, give confidence levels, or flag anything odd before merging.
---

The reader decides, has no context and little time. Write in plain language and the project's own domain words, with the names the code uses.

Read everything before writing: the diff against main, commits, the PR and its comments, related threads, and what the user actually asked, so you can tell asked work from unasked.

- **State**: ready to merge or not, what blocks, what needs the user.
- **Decisions**: one standalone card per debatable call: two lines of context, what we chose, the strongest alternative, why, confidence, diff size and breadth, from both the product and the code-rules angle. Each card reads alone.
- **Worth knowing**: changes nobody asked for, suspicious bits, untested paths, assumptions.
- **Diff**: where the net lines went, whether that is expected, and what could go at low tradeoff.

State the final state, not the journey.