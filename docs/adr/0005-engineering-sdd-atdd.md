# 0005. SDD + ATDD phase-gated lifecycle for multi-stage generation

Date: 2026-11-05
Status: Accepted

## Context

The skill is extending toward a multi-stage transmedia pipeline (novel → script →
comic → animation → film). The existing text-only verification gates cannot cover
image/video stages, and each downstream stage compounds consistency drift. A
discipline was needed so that every stage is specified up front, testable, and
cannot auto-advance without explicit human sign-off.

## Decision

Adopt Specification-Driven Development (SDD) and Acceptance Test-Driven
Development (ATDD) for all multi-stage generation work, with a mandatory
phase-gated human review between stages:

1. **SDD** — write a specification (inputs, outputs, acceptance criteria) before
   generating any content or code.
2. **ATDD** — declare executable acceptance tests before implementation; a stage
   is "done" only when its tests pass.
3. **Phase Gate** — after tests pass, the pipeline STOPS and waits for explicit
   human review and sign-off; it does not auto-advance.

The novel's continuity state (`state/`) remains the single source of truth
consumed by every downstream stage. Branch strategy: one `feat/pipeline-{stage}`
branch per stage; `main` is protected and merges only after gate sign-off.

## Consequences

- Stages are contract-first and testable; scope creep is bounded by specs.
- The human stays in the loop at every boundary (extends the existing 三审
  three-stage review and verification gates).
- Visual stages get explicit go/no-go gates where automated checks are weak.
- Cost: more upfront spec and test writing — accepted as the price of control.
