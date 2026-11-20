---
name: session-digest
description: Condense recent Claude Code sessions from every worktree of this repo into a token-light digest of user messages and the replies they answer. Use when asked to review past agent conversations, e.g. to find where agents needed steering.
---

`python3 -I <this skill folder>/digest.py [count] > /tmp/session-digest.md` prints the `count` (default 15) most recent sessions over 50 KB, skipping the current one: each user message, the assistant reply before it, the tool calls in between, and rejected tool calls. Read the file in pages.
