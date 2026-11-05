# Specs Index — Transmedia Pipeline SDD Layer

> Conforms to: `README_FOR_AI.md` §14 (Specification Hub) and §13 (SDD + ATDD + gate).

This directory holds the detailed executable specifications (the "S" in SDD) for
each stage of the transmedia pipeline. `README_FOR_AI.md` §14 is the hub: it
inlines a concise skeleton per stage and points here for the full spec. Each file
stays ≤500 lines (per `README_FOR_AI.md` §7).

## Index

| Stage | Spec | Tool maturity |
|-------|------|---------------|
| 0 — Governance | `00-governance.md` | n/a |
| 1 — Novel | `01-novel.md` | High (already built) |
| 2 — Script | `02-script.md` | High |
| 3 — Storyboard | `03-storyboard.md` | High |
| 4 — Comic | `04-comic.md` | Medium |
| 5 — Animation | `05-animation.md` | Medium-low |
| 6 — Film | `06-film.md` | Low |

## Conventions

- Every spec declares `Conforms to: README_FOR_AI.md §14 + §13` at the top.
- Acceptance criteria are written as checkable ATDD items (`- [ ]`).
- Stages consume upstream facts only from `state/`; no separate state is introduced.
- Stages with immature tooling state gaps honestly and rely on the go/no-go gate.
- Every stage follows the Section 13 lifecycle:
  `Spec (SDD) → Acceptance Tests (ATDD) → Implement → Run Tests → STOP: human gate → (approve → next | reject → fix)`.
