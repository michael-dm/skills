---
name: resolve-issue
description: Fix a repository issue end to end, from reproduction to draft PR. Use when the user asks to fix or handle an issue.
---

# Resolve Issue

The issue is evidence of a bug, not a design brief: its suggested fix is a symptom-level guess until the code proves otherwise.

1. **Reproduce.** Run the reported reproduction unchanged until it goes _red_. If hardware or environment blocks it, name the blocker.
2. **Find the root cause.** Read the issue thread, linked PRs, and the history of the code involved until you can say why the failing machinery exists and what changed. A throwaway spike that turns the reproduction green is a fine way to prove a cause; delete it afterwards.
3. **Design from a clean baseline.** Weigh the obvious patch against a fix where the invalid state cannot exist, and prefer deleting the cause over adding recovery. Hold it to the design rules in `CLAUDE.md`.
4. **Validate.** The original reproduction goes green, and the checks covering every caller of changed code pass.
5. **Publish** a draft PR with the root cause, the fix, and `Closes #<issue>`, following the [commit](../commit/SKILL.md) skill and your PR conventions. Merging, marking ready, or closing the issue waits for the user.
