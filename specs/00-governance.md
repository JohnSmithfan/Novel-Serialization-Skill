# Stage 0 — Governance & Asset Conventions (SDD)

> Conforms to: `README_FOR_AI.md` §14.7 (Governance & Asset Conventions) and §13 (SDD + ATDD + gate).

## 1. Goal
Establish the branch, asset, and cost governance baseline for the transmedia
pipeline so downstream stages are independent, reversible, and auditable.

## 2. Upstream inputs
- Existing repository structure (`SKILL.md`, `references/`, `modules/`, `scripts/`).
- This specification hub `README_FOR_AI.md` §14.

## 3. Downstream outputs
- Branch strategy and `feat/pipeline-{stage}` naming convention.
- Asset directory `assets/{stage}/`.
- Cost ceilings and go/no-go gate decision records.

## 4. Acceptance criteria (ATDD)
- [ ] Repository passes `scan_hygiene` + `check_refs` (`dev.py all` green).
- [ ] New pipeline directory structure passes scaffolding validation.
- [ ] ADR-0005 (SDD + ATDD) and the branch strategy are reviewed and signed off.
- [ ] `assets/{stage}/` directory skeleton is in place.

## 5. Generation method
1. Review ADR-0005 and the branch strategy → sign off.
2. Establish the `assets/{stage}/` skeleton and naming conventions.
3. Set a per-stage cost cap (increasing with tool maturity).
4. Run `dev.py all` to confirm the baseline is green.

## 6. Tool maturity & go/no-go
Not applicable (governance stage); its outputs define the gate trigger conditions for later stages.

## 7. Risks & mitigations
- Cost overrun → hard per-stage cap; over cap triggers a gate decision.
- State fragmentation → force downstream to consume only `state/`; no separate state.
