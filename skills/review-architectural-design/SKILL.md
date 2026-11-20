---
name: review-architectural-design
description: Review the architectural design of an implementation.
---

Treat the current implementation and its abstractions as disposable. Aim for pure design and the smallest coherent system, then list the concrete architectural changes to make.

List design changes derived from first principles. Ask whether this is the design we would choose on a clean sheet, whether ownership and invariants are clear, and which states, layers, APIs, branches or failure paths could simply not exist in the first place under a better model. Prefer designs that make invalid states unrepresentable. Bias toward substantial simplification and coherent breaking changes when they produce a materially better result. Accept small or negligible tradeoffs when they enable significant complexity reductions.

List deletions and simplifications that reduce total authored lines of code, cognitive complexity and cyclomatic complexity. Find complexity created by the implementation rather than the product: machinery that compensates for another design choice, policy split across owners, concepts that must stay synchronized, and abstractions that add more surface than they remove. Prefer the deeper change that deletes code and its underlying causes instead of polishing, moving or hiding symptoms. Preserve essential domain complexity that genuinely earns its place.
