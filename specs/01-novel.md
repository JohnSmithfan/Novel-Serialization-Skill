# Stage 1 — Novel (SDD)

> Conforms to: `README_FOR_AI.md` §14.1 and §13.

## 1. Goal
Produce a high-quality, continuity-controlled long-form web novel. This is the
repository's core capability and the single source of truth for all downstream
stages.

## 2. Upstream inputs
- Author intent (theme, tone, target length).
- (Optional) existing world-building / character notes.

## 3. Downstream outputs
- Chapter drafts (`chapters/`).
- Character sheets (`characters/`).
- World-building docs (`world/`).
- Continuity state (`state/`) consumed by every downstream stage.

## 4. Acceptance criteria (ATDD)
- [ ] Each chapter passes the three-stage review: humanizer / continuity / punctuation.
- [ ] `check_refs` and `scan_hygiene` pass.
- [ ] Zero continuity conflicts recorded in `state/`.
- [ ] Continuity state updated after each chapter.

## 5. Generation method
Existing novel skill flow:
worldbuilding → character-design → chapter-writing → continuity-check → publishing-workflow.

## 6. Tool maturity & go/no-go
High — the tooling is mature and already built.

## 7. Risks & mitigations
- Continuity drift → enforce `state/` as single source of truth; run continuity-check every chapter.
- Inconsistent voice → humanizer review gate before publish.
