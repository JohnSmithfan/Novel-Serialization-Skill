# Multimedia Production Pipeline — Project Plan

Basis: conclusions of the local engineering assessment report (not committed to the
repository per ADR-0001) — phased, gate-driven, SDD + ATDD; the novel's continuity
state is the single source of truth across media; text stages go first, later stages
may be halted at any time.

Agile methodology is specified in `README_FOR_AI.md` §13 and
`docs/adr/0005-engineering-sdd-atdd.md`.

This plan document declares `conforms to` `README_FOR_AI.md` §14 (specification hub)
and §15 (plan schema).

## 1. Core Principles

- **SDD (Specification-Driven)**: each stage writes its spec (inputs / outputs /
  acceptance criteria) before generation; the spec is the contract, generation obeys it.
- **ATDD (Acceptance-Test-Driven)**: each stage defines executable acceptance tests
  first; implementation is "done" only when tests pass.
- **Phase Gate**: after acceptance tests pass, STOP and wait for human review sign-off
  before the next stage; never auto-advance.
- **Single Source of Truth**: the novel's continuity state (`state/`) is consumed by
  every stage; downstream stages introduce no separate state.

## 2. Stage Design

### Stage 0 — Planning & Governance
- **SDD**: branch strategy, module/subproject boundaries, asset directory convention
  (`assets/{stage}/`), cost ceiling.
- **ATDD**: repository passes `scan_hygiene` + `check_refs`; new pipeline directory
  structure passes scaffolding check.
- **Gate**: ADR and branch strategy review pass.
- Branch: `feat/pipeline-governance` | Outputs: `docs/adr/0005-engineering-sdd-atdd.md`,
  directory skeleton.

### Stage 1 — Script & Storyboard (text)
- Inputs: novel chapters + continuity state.
- **SDD**: per chapter → script beat sheet; storyboard = shot spec (shot size / camera /
  duration / visual description / dialogue).
- **ATDD**: per chapter produce beat sheet + storyboard (structured JSON); pass existing
  text reviews (humanizer / continuity / punctuation).
- **Gate**: human review of script and storyboard.
- Branch: `feat/pipeline-script-storyboard`.

### Stage 2 — Comic
- Inputs: storyboard + character/style guide derived from novel state.
- **SDD**: character-consistency spec, style lock, panel-render spec, asset naming.
- **ATDD**: character-face / style-consistency check script passes; panels conform to spec.
- **Gate**: human review of visual consistency.
- Branch: `feat/pipeline-comic`.

### Stage 3 — Animation
- Inputs: storyboard + comic assets.
- **SDD**: shot-animation spec, duration/pacing, asset reuse, render parameters.
- **ATDD**: sample reel passes visual-consistency + pacing checks.
- **Gate**: human review (go/no-go).
- Branch: `feat/pipeline-animation`.

### Stage 4 — Film
- Inputs: animation clips.
- **SDD**: edit script, dubbing/score, post, A-V sync spec.
- **ATDD**: finished film passes duration/structure/A-V-sync checks.
- **Gate**: human final review (go/no-go).
- Branch: `feat/pipeline-movie`.

## 3. Alignment with Existing Process

- Text stages reuse the existing three-stage review and verification gates as quality gates.
- Each stage gate = extension of the existing "final-review sign-off": STOP and wait,
  not a soft checkpoint.
- `README_FOR_AI.md` §13 defines the SDD + ATDD + gate lifecycle and is the normative
  basis of this plan.
- Each `feat/pipeline-{stage}` branch merges to `main` only after gate sign-off.

## 4. Exit Criteria

If any stage fails its gate with no acceptable fix → HALT that stage and all subsequent
ones, preserve produced assets, do not pollute `main`.

## 5. Lifecycle Loop

```
Spec (SDD) → Acceptance Tests (ATDD) → Implement → Run Tests
           → STOP: human gate → (approve → next stage | reject → fix/rework)
```
