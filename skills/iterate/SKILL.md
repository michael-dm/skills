---
name: iterate
description: Iterate on the branch with fresh-context reviewers.
disable-model-invocation: true
---

Handle this end to end with care, following any sidenotes given with the command.

After each work iteration, commit all and ask a subagent with fresh context (`high` effort unless specified) to review our work with the following prompt:

"[the goal, in my words] how would you rate implementation in current branch? any awkward things suggest underlying changes ? sidenote: we can often accept small tradeoffs & invariants if they help reduce cyclomatic complexity & verbosity"

When the work touches what users see, also ask a fresh QA & ux polish subagent:

"[the goal, in my words] verify & use our recent work in this branch, and rate on A-F the ui/ux polish level vs rest of app - clarity, missing states that will realistically happen, kb support, responsiveness, tiny visual bugs & inconsistencies vs app & design system etc - as well as a list of the net diff reduction & elegance improvements"

Be opinionated in what to do with the feedback, given history, similar decisions and team taste. Iterate until you get at least A-, or bring me what's left once grades plateau.

Once you reach that, do a final small elegance cleanup/trim sweep to reduce loc and commit all. When asked for a PR, make it ready & run CI. If a review bot comments on the ready PR, check its comments as a bonus final guard, never in place of the subagent reviews.
