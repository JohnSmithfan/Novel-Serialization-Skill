# GitHub Novel Serialization Skill

> **AI-Assisted Novel Serialization Skill** — A modular, harness-engineered system for writing, managing, and publishing serialized novels on GitHub.

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License--Novel%20Content-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSES/CC-BY-NC-SA-4.0.txt)
[![Skill Version](https://img.shields.io/badge/Skill%20Version-1.4.0-orange)](SKILL.md)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Bootstrap from the Spec](#bootstrap-from-the-spec)
- [Directory Structure](#directory-structure)
- [Development](#development)
- [Modules](#modules)
- [Subprojects](#subprojects)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

---

## Overview

**github-novel-serialization-skill** is a production-grade, modular Skill that orchestrates AI-assisted novel writing and GitHub-based serialization. It covers the full creative lifecycle: **world-building -> character design -> chapter drafting -> continuity verification -> GitHub publishing**. Built on harness-engineering principles (constraint-before-generation, structured memory, verification gates, modular decomposition, and feedback loops), this Skill transforms a raw LLM into a reliable, stateful, multi-session novel-writing agent.

Every module is independently usable, composable, and under 500 lines — designed for compatibility with any LLM-backed coding agent (Claude Code, GitHub Copilot, Cursor, etc.).

> **Note:** This Skill project is a harness-engineered system, not just a collection of prompts. Every file exists to constrain, guide, and verify — the goal is deterministic quality, not lucky outputs.

---

## Architecture

```
+------------------------------------------------------------------+
|                        SKILL.md (Index)                          |
|  Overview | Output Language | Quick Start | Module Index         |
|  Workflow Pipeline | Quick Refs | Verification Gates             |
+----------------------+-------------------------------------------+
                       | references
                       v
+------------------------------------------------------------------+
|                     references/                                  |
|  method-patterns.md (master) | glossary.md | examples/           |
+----------------------+-------------------------------------------+
                       | modules
                       v
+------------------------------------------------------------------+
|                      modules/                                    |
|  +---------------+ +---------------+ +---------------+           |
|  | worldbuilding | | character-    | | chapter-      |           |
|  |               | | design        | | writing       |           |
|  +---------------+ +---------------+ +---------------+           |
|  +---------------+ +---------------+ +---------------+           |
|  | continuity-   | | publishing-   | | continuity-   |           |
|  | check         | | workflow      | | tracker       |           |
|  +---------------+ +---------------+ +---------------+           |
+------------------------------------------------------------------+
                       |
                       v
+------------------------------------------------------------------+
|                      prompts/                                    |
|  README.md | 01-implement-method.md | 02-robustness-checks.md    |
+------------------------------------------------------------------+
```

> **Note:** The architecture diagram above shows the logical layering of the Skill (progressive disclosure): SKILL.md (index) → references/ (templates) → modules/ (functional sub-skills) → prompts/ (human copy-paste templates). In the file system, `references/`, `modules/`, and `prompts/` are peer directories under the project root.

---

## Quick Start

### Step 1 — Clone the Skill

```
git clone https://github.com/JohnSmithfan/github-novel-serialization-skill.git
cd github-novel-serialization-skill
```

### Step 2 — Install into Your Agent

Add the Skill to your agent's skills directory:

#### For Claude Code

```
ln -s $(pwd) ~/.claude/skills/github-novel-serialization-skill
```

#### For GitHub Copilot / Cursor / Other Agents

```
# Copy the repo into your agent's skills directory
# Note: The skills directory path varies by agent. Consult your agent's documentation
# for the correct skills directory location. Common paths include:
#   - Claude Code: ~/.claude/skills/
#   - Cursor: check Cursor settings for custom skills directory
#   - Other agents: refer to their respective documentation
cp -r . <AGENT_SKILLS_DIR>/github-novel-serialization-skill
```

### Step 3 — Start Writing

Open your AI chat window and use any trigger phrase:

| Action | Prompt Example |
|--------|---------------|
| Build a world | "Build a world with magic systems and feudal politics" |
| Create characters | "Create a protagonist with a tragic backstory" |
| Write a chapter | "Write Chapter 1: The Awakening" |
| Check continuity | "Check continuity across all chapters" |
| Publish | "Publish chapter 1 as release v1.0" |

---

## Bootstrap from the Spec

Every other section assumes you use this repository as it is. This one is for the
opposite case: you want the **whole project regenerated** — a fork with your own
naming, a rebuild from scratch, or a variant for a different agent — and you would
rather hand the job to an AI than copy forty-odd files by hand.

`README_FOR_AI.md` is the generation spec: 1,490 lines of directives that tell an
agent which files to create, what each must contain, and in which order. It ends
with "Generate all files now. Do not improvise structure." — that is the intended
use.

### Step 1 — Start from an empty directory

```
mkdir my-skill && cd my-skill
```

Do **not** run the generation inside a repository you care about. The spec
describes a full tree; an agent following it will create or overwrite files at
the output root.

### Step 2 — Hand the spec to your agent

```
Read README_FOR_AI.md and generate the complete project it specifies.
Output root: ./  (currently empty)
Follow the generation sequence in Section 12. Do not improvise structure.
When a file is not covered by the spec, mirror this reference implementation:
https://github.com/JohnSmithfan/github-novel-serialization-skill
```

Feed the file whole. An excerpt drops the constraints that make the output
consistent.

### Step 3 — Expect to reconcile

The spec is a **v1.1 baseline**. This repository is the reference implementation
at a later version, and where the two disagree, the repository wins. Known gaps
the spec does not cover: `tests/`, `docs/adr/`, `scripts/dev.py`, `.refsignore`,
`pyproject.toml`, `requirements-dev.txt`, `Makefile`, and four of the five
workflows in `.github/workflows/`. Treat generated files that differ from this
repository as review items, not as errors.

### Step 4 — Run the gates before trusting the result

```
python -m pip install -r requirements-dev.txt
python scripts/dev.py all
```

Without this step you have plausible files, not a working Skill. The spec's own
Section 11 checklist is static — line counts, file presence, links; `dev.py`
executes the same checks plus the reference gate and the test suite.

> **Why module contracts are not named `SKILL.md`.** Skills are discovered by
> filename. A `SKILL.md` in every subdirectory is registered as a separate skill
> by most loaders — this repository shipped that way once, and the six module
> contracts surfaced as six extra skills. Keep them named `MODULE.md`; a
> generated tree that writes `modules/*/SKILL.md` reintroduces the bug.

---

## Directory Structure

```
github-novel-serialization-skill/
|
+-- README.md                           # This file
+-- README_FOR_AI.md                    # Generation spec — bootstrap a new tree from it (seed file)
+-- SKILL.md                            # Index + quick-reference
+-- CHANGELOG.md                        # Version history
+-- SUBPROJECTS.md                      # Registered independent novel subprojects
+-- CONTRIBUTING.md                     # Contribution guidelines
+-- CODE_OF_CONDUCT.md                  # Community standards
+-- SECURITY.md                         # Security policy
+-- SUPPORT.md                          # Where to go with which question
+-- GOVERNANCE.md                       # Roles, decision process, release policy
+-- CITATION.cff                        # Machine-readable citation metadata
+-- security.txt                        # RFC 9116 contact for security tooling
+-- pyproject.toml                      # Metadata + pytest / ruff configuration
+-- requirements-dev.txt                # Development-only dependencies
+-- Makefile                            # Thin proxy to scripts/dev.py
+-- LICENSE                             # GPL-3.0
+-- LICENSES/                           # Additional licenses
|   +-- CC-BY-NC-SA-4.0.txt
+-- .editorconfig / .gitattributes / .gitignore
+-- .markdownlint.json / .pre-commit-config.yaml
|
+-- docs/                               # Engineering documentation
|   +-- README.md                       # Index
|   +-- adr/                            # Architecture decision records
|
+-- tests/                              # Regression tests for scripts/
|
+-- scripts/                            # Shared automation scripts (consumed by subprojects)
|   +-- README.md                       # Script catalog & invocation conventions
|   +-- dev.py                          # One entry point for every local gate
|   +-- humanizer_check.py              # De-AI-tone self-check (PASS/WARN/FAIL)
|   +-- _list_hits.py                   # List flagged sentences for manual rewrite
|   +-- _promote_draft.py               # Draft -> release sync (snapshot, gates)
|   +-- _sync_draft.py                  # Release -> draft write-back (errata only)
|   +-- review_all.py                   # Review: every gate; --stage for the 3-stage review
|   +-- review_scale.py                 # Scale review (word-count targets & gaps)
|   +-- review_continuity.py            # Consistency review (names, timeline, titles)
|   +-- review_rationality.py           # Rationality review (logic, pacing, outline cover)
|   +-- review_punctuation.py           # Punctuation & orthography review
|   +-- _review_lib.py                  # Shared library for the review scripts
|   +-- check_refs.py                   # Reference integrity (six buckets)
|   +-- scan_hygiene.py                 # CRLF / mojibake / junk / line-budget scan
|   +-- init_subproject.py              # Subproject scaffold generator
|
+-- references/                         # Deep documentation & templates
|   +-- method-patterns.md              # Master template file
|   +-- method-patterns-worldbuilding.md
|   +-- method-patterns-character.md
|   +-- method-patterns-chapter.md
|   +-- method-patterns-continuity.md
|   +-- method-patterns-publishing.md
|   +-- subproject-playbook.md          # Field-tested subproject conventions
|   +-- glossary.md
|   +-- examples/                       # Worked examples
|   |   +-- example-worldbuilding.md
|   |   +-- example-character-sheet.md
|   |   +-- example-chapter-draft.md
|
+-- prompts/                            # Dual-mode prompt templates (human copy-paste)
|   +-- README.md
|   +-- 01-implement-method.md
|   +-- 02-robustness-checks.md
|
+-- modules/                            # Functional modules (contracts, NOT skills)
|   +-- worldbuilding/MODULE.md          # not SKILL.md — loaders would register each as a skill
|   +-- character-design/MODULE.md
|   +-- chapter-writing/MODULE.md
|   +-- continuity-check/MODULE.md
|   +-- publishing-workflow/MODULE.md
|   +-- continuity-tracker/MODULE.md
|
+-- .github/                            # GitHub community health files
    +-- CODEOWNERS
    +-- ISSUE_TEMPLATE/
    |   +-- bug-report.yml
    |   +-- feature-request.yml
    |   +-- errata.yml
    |   +-- docs.yml
    |   +-- config.yml
    +-- PULL_REQUEST_TEMPLATE.md
    +-- PULL_REQUEST_TEMPLATE/content.md
    +-- FUNDING.yml
    +-- dependabot.yml
    +-- labels.yml
    +-- release.yml
    +-- workflows/
        +-- ci.yml
        +-- codeql.yml
        +-- novel-release.yml
        +-- label-sync.yml
        +-- stale.yml
```

## Development

The runtime scripts need nothing but the standard library. The gates need a
little more:

```bash
python -m pip install -r requirements-dev.txt
pre-commit install && pre-commit install --hook-type commit-msg
```

| Command | What it runs |
|---|---|
| `python scripts/dev.py all` | hygiene, references, lint, tests — everything CI runs |
| `python scripts/dev.py hygiene` | CRLF, encoding damage, junk files, 500-line budget |
| `python scripts/dev.py refs` | every reference resolves; release files stay inside the release tree |
| `python scripts/dev.py lint` | byte-compile, plus ruff when installed |
| `python scripts/dev.py test` | the `tests/` suite |
| `python scripts/dev.py scaffold --name "书名" --root ../my-novel` | new subproject |

`make all` does the same where make is available.

> **Note:** generation-compliance audit reports (`README_FOR_AI_Audit_Report*.md`) are produced on
> demand and are **not** committed — `.gitignore` excludes them. Do not expect them in the tree.

---

## Modules

| Module | Purpose |
|--------|---------|
| **worldbuilding** | Generate and maintain world-building documents (magic systems, geography, politics, culture) |
| **character-design** | Generate and maintain character sheets (identity, psychology, arcs, relationships, voice profiles) |
| **chapter-writing** | Draft chapters following established style guides and continuity constraints |
| **continuity-check** | Verify consistency across all chapters and state files (plot holes, timeline errors) |
| **publishing-workflow** | Manage Git-based publishing pipeline (tagging, releases, automated checks) |
| **continuity-tracker** | Maintain persistent state files (timeline, character states, thread ledger) |

---

## Subprojects

Concrete novels live as **independent subprojects** — each keeps its own git repository and remote,
commits and releases on its own, and only borrows shared capability (scripts) from this repo.

| Subproject | Location | Remote | Scripts |
|------------|----------|--------|---------|
| **-1928** (《奉天1928》, Republican-era Northeast alternate history) | `C:\Users\Admin\-1928` | `https://github.com/JohnSmithfan/-1928.git` | In progress: 5 volumes / 1008 chapters planned; **288 chapters released** (Vol.1 1–88, Vol.2 89–288) as of 2026-10-07 | `scripts/` — all of the above, invoked from the subproject root |

Rules: scripts stay in this repo's `scripts/` (never copied into a subproject as `tools/`), and are
invoked from the subproject root — the subproject root is the script's working directory.
See [SUBPROJECTS.md](SUBPROJECTS.md), [scripts/README.md](scripts/README.md) and the
[Subproject Playbook](references/subproject-playbook.md).

Design decisions that shape this repository — why reports are not committed, why
release files may only reference release files, why two chapter naming schemes are
legal — are recorded in [docs/adr/](docs/adr/README.md).

---

## Installation

### For GitHub Skills

Add the Skill to your GitHub repository's skills directory:

```
# Clone the repository into your project's .github/skills directory
mkdir -p .github/skills
git clone https://github.com/JohnSmithfan/github-novel-serialization-skill.git .github/skills/github-novel-serialization-skill
```

### For Claude Code

```
# Clone the repository
git clone https://github.com/JohnSmithfan/github-novel-serialization-skill.git
cd github-novel-serialization-skill

# Create a symlink in your Claude Code skills directory
mkdir -p ~/.claude/skills
ln -s $(pwd) ~/.claude/skills/github-novel-serialization-skill
```

### For Cursor / Other Agents

```
# Clone the repository
git clone https://github.com/JohnSmithfan/github-novel-serialization-skill.git
cd github-novel-serialization-skill

# Copy the repository into your agent's skills directory
# Note: The skills directory path varies by agent. Consult your agent's documentation
# for the correct skills directory location. Common paths include:
#   - Claude Code: ~/.claude/skills/
#   - Cursor: check Cursor settings for custom skills directory
#   - Other agents: refer to their respective documentation
cp -r github-novel-serialization-skill <AGENT_SKILLS_DIR>/github-novel-serialization-skill
```

---

## Usage Examples

### Example 1: Build a World

Use the prompt template in `prompts/01-implement-method.md`:

```
You are a professional novel architect. Build a world for a:
- Genre: {{GENRE}} (e.g., "high fantasy")
- Setting: {{SETTING}} (e.g., "a archipelago of floating islands")
- Themes: {{THEMES}} (e.g., "power, corruption, redemption")
- Target chapters: {{TARGET_CHAPTERS}} (e.g., 50)
- Tone: {{TONE}} (e.g., "grimdark")
- POV style: {{POV_STYLE}} (e.g., "third-person limited")

Output everything in: {{OUTPUT_LANGUAGE}}
```

### Example 2: Check Continuity

Use the prompt template in `prompts/02-robustness-checks.md`:

```
Review the following chapter draft for:
1. Continuity consistency (character names, locations, timeline)
2. Style consistency (voice, tense, register)
3. Plot logic (causality, motivation, foreshadowing payoff)
4. Pacing analysis (scene-to-sequel ratio, tension curve)
5. Dialogue authenticity (voice differentiation per character)

Output a structured report with severity levels (Critical / Warning / Suggestion).
```

### Example 3: Publish a Release

```
# Tag a release
git tag -a v1.0.0 -m "Release v1.0.0: Chapters 1-5"
git push origin v1.0.0

# The GitHub Actions workflow will:
# 1. Validate chapter file formats
# 2. Verify license compliance
# 3. Run continuity checks
# 4. Create a GitHub Release with release notes
```

---

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting pull requests.

- **Bug Reports**: [Open an Issue](https://github.com/JohnSmithfan/github-novel-serialization-skill/issues/new?template=bug-report.yml)
- **Feature Requests**: [Open a Feature Request](https://github.com/JohnSmithfan/github-novel-serialization-skill/issues/new?template=feature-request.yml)
- **Docs & Errata**: [Open a Docs Issue](https://github.com/JohnSmithfan/github-novel-serialization-skill/issues/new?template=docs.yml)
- **Security Issues**: [View Security Policy](SECURITY.md)
- **Not sure where to go**: [SUPPORT.md](SUPPORT.md)
- **How decisions are made**: [GOVERNANCE.md](GOVERNANCE.md)
- **Pull Requests**: Follow our branch naming and commit format conventions

---

## Credits

- Built with principles from Harness Engineering
- Inspired by the [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/) standards
- Community-driven project — built by and for novelists, writers, and AI enthusiasts

---

## License

This project uses a **dual-licensing** model:

| Component | License |
|-----------|---------|
| **Skill Infrastructure** (code, templates, prompts, SKILL.md files, GitHub workflows, configuration files) | [GNU General Public License v3.0 (GPL-3.0)](LICENSE) |
| **Generated Novel Content** (chapters, character sheets, world-building docs) | [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](LICENSES/CC-BY-NC-SA-4.0.txt) |

See the [LICENSE](LICENSE) file for full GPL-3.0 terms and the [LICENSES/CC-BY-NC-SA-4.0.txt](LICENSES/CC-BY-NC-SA-4.0.txt) file for full CC BY-NC-SA 4.0 terms.
