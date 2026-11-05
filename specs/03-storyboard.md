# Stage 3 — Storyboard (SDD)

> Conforms to: `README_FOR_AI.md` §14.3 and §13.

## 1. Goal
Turn the script into shot specifications (shot size / camera / duration / visual description / dialogue).

## 2. Upstream inputs
- Script (`assets/script/`).
- Novel state (`state/`).

## 3. Downstream outputs
- Storyboard table: structured JSON (shot no., shot size, camera, duration, visual, dialogue) under `assets/storyboard/`.

## 4. Acceptance criteria (ATDD)
- [ ] Storyboard covers every script scene.
- [ ] Shot-duration budget is shootable.
- [ ] Consistent with character and style.
- [ ] JSON validates against the storyboard schema.

## 5. Generation method
Script → storyboard spec → consistency check → human gate.

## 6. Tool maturity & go/no-go
High — structured text/JSON; no image generation required at this stage.

## 7. Risks & mitigations
- Missing scenes → coverage check against the script.
- Inconsistent shot language → fixed shot-type vocabulary.
