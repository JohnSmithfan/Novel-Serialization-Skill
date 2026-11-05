# Stage 4 — Comic (SDD)

> Conforms to: `README_FOR_AI.md` §14.4 and §13.

## 1. Goal
Render the storyboard into sequential art panels, locking character and style.

## 2. Upstream inputs
- Storyboard (`assets/storyboard/`).
- Character/style guide derived from novel state.

## 3. Downstream outputs
- Comic panels (images) under `assets/comic/`.
- Asset naming following the convention.

## 4. Acceptance criteria (ATDD)
- [ ] Character-face / style consistency check script passes.
- [ ] Panels conform to the storyboard spec.
- [ ] Asset naming follows the convention.

## 5. Generation method
Lock character/style → render panels → visual consistency review → human gate.

## 6. Tool maturity & go/no-go
Medium — image generation is available but character consistency is the key risk; the consistency script is a hard go/no-go gate.

## 7. Risks & mitigations
- Face/style drift → character-reference lock + automated consistency check.
- High render cost → cap panels per batch; gate on cost.
