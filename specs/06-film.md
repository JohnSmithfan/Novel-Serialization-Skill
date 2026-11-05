# Stage 6 — Film (SDD)

> Conforms to: `README_FOR_AI.md` §14.6 and §13.

## 1. Goal
Edit animation clips into a finished film (dubbing / score / post / A-V sync).

## 2. Upstream inputs
- Animation clips (`assets/animation/`).

## 3. Downstream outputs
- Finished film under `assets/film/`.

## 4. Acceptance criteria (ATDD)
- [ ] Finished film passes duration / structure / A-V-sync checks.
- [ ] Dubbing and score conform to the script's tone.

## 5. Generation method
Edit script → dubbing/score → post → A-V-sync review → human final gate (go/no-go).

## 6. Tool maturity & go/no-go
Low — tooling is the least mature and risk is highest; the stage may be halted at any time if the gate fails.

## 7. Risks & mitigations
- A-V desync → automated sync check.
- Unacceptable quality → human final gate; halt without polluting `main`.
