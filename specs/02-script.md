# Stage 2 — Script (SDD)

> Conforms to: `README_FOR_AI.md` §14.2 and §13.

## 1. Goal
Adapt novel chapters into shootable scripts (scenes, dialogue, action, beats).

## 2. Upstream inputs
- Novel chapters (`chapters/`).
- Continuity state (`state/`).

## 3. Downstream outputs
- Per-chapter beat sheet.
- Structured script under `assets/script/`.

## 4. Acceptance criteria (ATDD)
- [ ] A beat sheet produced for every chapter.
- [ ] Passes existing text reviews (humanizer / continuity / punctuation).
- [ ] Character motivation consistent with the novel.
- [ ] Script stored under `assets/script/` with stable naming.

## 5. Generation method
Chapter → beat sheet → script draft → text review → human gate.

## 6. Tool maturity & go/no-go
High — text-only; reuses the novel skill's text-review gates.

## 7. Risks & mitigations
- Loses novel nuance → human gate with author sign-off.
- Over-long scripts → enforce a beat budget per chapter.
