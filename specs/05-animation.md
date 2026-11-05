# Stage 5 — Animation (SDD)

> Conforms to: `README_FOR_AI.md` §14.5 and §13.

## 1. Goal
Animate the storyboard + comic assets into a sample reel.

## 2. Upstream inputs
- Storyboard (`assets/storyboard/`).
- Comic assets (`assets/comic/`).

## 3. Downstream outputs
- Animation clips (video) under `assets/animation/`.

## 4. Acceptance criteria (ATDD)
- [ ] Sample reel passes visual-consistency + pacing checks.
- [ ] Asset reuse rate meets target.
- [ ] Clips conform to shot durations from the storyboard.

## 5. Generation method
Shot-animation spec → render → pacing/consistency review → human gate (go/no-go).

## 6. Tool maturity & go/no-go
Medium-low — tooling gaps in motion consistency and cost are significant; state honestly and gate on cost/quality.

## 7. Risks & mitigations
- Motion inconsistency → reference-locked assets + per-clip review.
- Cost overrun → hard per-stage cap; over cap triggers gate decision.
