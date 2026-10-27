# 0004. Engineering hygiene — no messy/crappy code, no historical burden

Date: 2026-10-27
Status: Accepted

## Context

An audit of the skill repository found concrete instances of crappy code and
historical burden that violated the project's *own* stated rules:

- Text writes in `_promote_draft.py`, `_sync_draft.py`, and `humanizer_check.py`
  omitted `newline='\n'`, producing CRLF on Windows and directly breaking the
  hard LF rule documented in `references/subproject-playbook.md` §7.
- `sys.stdout.reconfigure(encoding='utf-8')` ran at **module import time** in
  `_review_lib.py`, `_promote_draft.py`, and `_sync_draft.py`, mutating global
  process state as a hidden side effect of a harmless import. `_sync_draft.py`
  additionally executed its entire body at import time, so importing it ran the
  sync.
- `check_refs.py` documented "七档" (seven buckets) while implementing eight.

The repository had no single, authoritative statement forbidding this class of
problem, so it recurred. The defects were fixed (see the `[HISTORICAL BURDEN]`
annotations left at the removed lines), but the *rule* had to be written down
so reviewers could cite it.

## Decision

Adopt an explicit Engineering Hygiene policy (authoritative text in
`CONTRIBUTING.md`, reinforced in `scripts/README.md` and
`references/subproject-playbook.md` §7):

- **No messy or crappy code** — obey the project's own rules (notably the LF
  rule), no global side effects at import, no dead or commented-out code, single
  responsibility and the 500-line budget.
- **No historical burden** — do not reintroduce a pattern that was deliberately
  removed; when removing a legacy pattern, leave a `[HISTORICAL BURDEN — removed
  YYYY-MM]` note explaining what and why; never commit `.pyc` / `__pycache__` /
  tool caches; generated/seed files stay generated.
- **UTF-8 console output** is enabled by calling
  `_review_lib._enable_utf8_console()` explicitly in each entry point, never at
  module scope.

## Consequences

- The LF-rule violations and import-time side effects are removed; the canonical
  helper centralises the correct behaviour, and the review scripts call it from
  `main()`.
- Reviewers have an explicit rule to cite when a change reintroduces these
  smells; the pre-commit hooks, `scripts/dev.py all`, and CI enforce the
  file-level consequences.
- Cost: a small amount of boilerplate (one `_enable_utf8_console()` call per
  entry point) and sustained discipline in review.
