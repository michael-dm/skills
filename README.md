<p align="center"><img src="assets/cover.png" alt="Skills for agents that rebuild, not layer" width="100%"></p>

Most agent skills are slop: long rulebooks that make your agent worse. These are the opposite. At [Miroir](https://miroir.co) we build Miroir OS with frontier coding agents every day, and we kept a skill only where the models needed steering again and again: a few hundred words each, written for senior-level models.

## Skills

| Skill | Use it to | Try |
|---|---|---|
| [`/reshape`](skills/reshape/SKILL.md) | rebuild working code from first principles, with less of it | `/reshape −30% cyclomatic complexity, same perf` |
| [`/review-architectural-design`](skills/review-architectural-design/SKILL.md) | list the design changes a clean sheet would make | `review the architectural design of the sync layer` |
| [`/iterate`](skills/iterate/SKILL.md) | harden a branch with fresh-context reviewers and QA until A− | `/iterate the new export flow` |
| [`/brief`](skills/brief/SKILL.md) | get caught up on a branch as if you had zero context | `catch me up, can we merge?` |
| [`/dogfood`](skills/dogfood/SKILL.md) | watch fresh agents use your tool, fix it from their traces | `dogfood the CLI on 3 real tasks` |
| [`/resolve-issue`](skills/resolve-issue/SKILL.md) | go from issue to root cause to draft PR | `resolve #412` |
| [`/clean-copy`](skills/clean-copy/SKILL.md) | cut UI text that shouldn't exist | `/clean-copy the settings page` |
| [`/session-digest`](skills/session-digest/SKILL.md) | find where your agents needed steering | `where did agents struggle this week?` |
| [`/commit`](skills/commit/SKILL.md) | split work into clean conventional commits | `commit all` |

[`CLAUDE.md`](CLAUDE.md) holds the design rules they lean on: purity over layering, net-negative diffs, invalid states unrepresentable, commands first.

We also use, and recommend, [Matt Pocock's skills](https://github.com/mattpocock/skills) (`grill-me`, `domain-modeling`, `writing-for-agents`, `wait-what`) and the visual summaries from [HumanLayer](https://github.com/humanlayer/humanlayer)'s skills in our PR bodies.

## Install

```sh
git clone https://github.com/michael-dm/skills ~/.agent-skills
ln -s ~/.agent-skills/skills/* ~/.claude/skills/
```

Then take what fits from `CLAUDE.md` into your own `CLAUDE.md` or `AGENTS.md`.

## What we learned

- **The first version always layers.** Ask for a rebuild once it works, at high effort.
- **Numbers beat adjectives.** "−30% on every perf metric" gets a redesign; "faster" gets polish.
- **The tool matters more than the skill text.** A sharp CLI and a short pointer beat a long manual.
- **When an agent misuses your tool, the tool is wrong.**
- **Guide softly.** Detailed rules overfit and override a frontier model's judgement.
- **Keep the original words.** A paraphrased rule drifts from its intent.

## License

MIT
