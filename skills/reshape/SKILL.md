---
name: reshape
description: Rebuild recent work from first principles so the same results come from less complexity. Use when asked to rethink or reshape something, cut cyclomatic complexity, verbosity or loc, or whether a problem could "not exist in the first place".
---

A first version makes things work by layering. This pass treats it as disposable and asks which design makes the same results fall out with fewer states, branches, owners, parameters and files: keep our perf and fixes, make things more elegant from scratch, and avoid branching issues in the first place.

**Baseline.** Measure what the result will be judged on before touching anything: cyclomatic complexity of the touched code (`lizard`), net diff, loc, and the product's own metrics (speed, quality, footprint). The user usually names a target; without one, aim for -30% at zero regression, and aim past it.

**History.** If you are not the author, read the log, blame, PR and related threads to learn why the current shape exists and which choices were deliberate, so the reshape keeps intent rather than just code.

**Root, not symptom.** Each awkward spot (a special case, a flag, a fallback, two things kept in sync, a helper with one caller, a parallel way to do the same thing) is a symptom. Go up the abstractions until you find the invariant, ownership move or small product tradeoff that makes it impossible, then hunt the cascading simplifications it unlocks. Small tradeoffs that delete whole branches are welcome ("latest OS only", "one aspect ratio"); name each one, and bring the ones that change what users see to the user.

**Second opinion.** Before building, have a fresh-context reviewer at high effort judge the proposed shape from the goal and user words, not from your conclusion.

**Done** when the metrics reach the target with no regression, or what remains is shown to be essential domain complexity. Report only numbers you measured, and a root cause only once reproduced. Commit, and report before → after numbers, the tradeoffs taken, and what you examined and chose to keep.
