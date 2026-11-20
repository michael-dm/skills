Answer decision-first, proportionate to the question, in the project's own domain words. Use subagents only when the user asks for them: low or medium effort to implement, high or x-high for optimisations, reshapes, reviews and hard problems.

## Design rules

Aim for **purity**, not the status quo: agents default to *layering* (keeping what exists and adding on top). Reshape instead.

- **Surface is the main cost.** Every new API, module, type, parameter, state variant, or branch must earn its place: nothing existing already does the job, no better invariant or ownership model makes it unnecessary, and it is worth maintaining forever. Keep related logic together: single-caller abstractions and premature file splits never earn their place.
- **Reshape** (/reshape): remove, move, and edit existing code until the change looks designed in, after checking its history (log, blame, PR) for intended behavior; look for removals that offset additions, with a **net-negative** diff as the ideal. Break interfaces and update every call site rather than keep shims or hybrids.
- **Commands first**: every capability is a command line tool in the Unix spirit (composable, many targets a call, plain lines or `--json`, a few goal-oriented presets and good defaults rather than open-ended settings), so agents can script and parallelise it; a UI is a thin layer over the same functions, only where a human has to see and decide.
- **Skills** rely on the model's intelligence: frontier models work like senior leads from well-built primitives (Unix-style CLIs, "code modes" in their native Python) and are held back by detailed instructions. Keep each skill to 100–2,000 tokens of its most useful, general intents and directions, pointing to where deeper knowledge lives rather than restating it. Write rules that hold for tasks you can't predict, not for the case at hand; when an agent misuses a command, fix the command before adding instructions (/dogfood).
- Rank maintainability and minimal surface / cyclomatic complexity first; efficiency, coverage, and security second.
- Value predictability as much as compute efficiency: avoid on-demand resources that start and stop with their consumers, and never degrade gracefully: run exactly as configured, or report the issue.
- **Key by full identity**: a key, lookup or event carries everything that makes its target unique, not a name that only happens to be unique today.
- **Invalid states unrepresentable**: enums and variants over optional fields; typed errors at boundaries, reusing existing error types; fail fast on impossible internal states.
- **Ownership**: policy lives in the subsystem that owns it, and consumers go through its public abstractions. Only the owner changes its state: when a command would leave another owner's state invalid, reject it with an error and let that owner fix it.
- Intent lives in names, types, and structure: write no comments beyond a *why* that names cannot carry (a hardware quirk, an upstream bug), and delete ones that restate code. Spell names in full (`percentage`, not `pct`).
- For API details, read the dependency's source (`node_modules/`, `~/.cargo/registry/src/`, site-packages) rather than guessing.

## Git

- Never discard changes you did not make; report validation failures they cause.
- Stay in the current worktree unless asked; set work aside with WIP commits, since the stash is shared across sessions.

## Validation

Back performance and root-cause claims with measurements, before and after; a likely cause is a lead, not a finding. Harden finished work with fresh-context reviewers (/iterate).

Scale validation to risk: a typecheck covers a small, confident edit; keep e2e for behavior you are unsure of, narrowed to the tests that exercise it. Add e2e tests only where nothing covers the change; write unit tests only when asked.
