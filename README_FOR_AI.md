# README_FOR_AI.md
> **Document Role**: This document is the project's single master specification — the "S" (Specification) in SDD — authorized by `docs/adr/0005-engineering-sdd-atdd.md`. It defines the specification-driven development direction for the transmedia pipeline (novel → script → storyboard → comic → animation → film) and the schema for development plans (defined in Section 15), so the project can be developed zero-from-scratch, phase by phase, from this document alone without copying the entire repository.

> **Purpose**: This document is a meta-instruction set. It directs an AI agent to generate a complete, production-grade **GitHub Novel Serialization Skill** project. Every section below is a mandatory generation directive — follow them precisely.
>
> **Document Metadata**:
> - **Version**: 1.2.0
> - **Status**: Approved
> - **Last Updated**: 2026-10-22
> - **Scope**: v1.1 baseline of the Skill specification; where this document and the repository disagree, the repository wins.
>
> **File Naming Note**: Keep this file named `README_FOR_AI.md`. The underscore form matters: the hygiene allow-list (`README_FOR_AI.md` in `scripts/dev.py`, CI and `.pre-commit-config.yaml`) matches on the exact filename, and a space-separated variant silently drops the 500-line exemption.


---

## 0. Generation Directives

### 0.1 Target Output

You are to generate a **complete Skill project** — not a single file, but a full directory tree of interlocking Markdown files that together form a modular, harness-engineered Skill for AI-assisted novel serialization on GitHub.

### 0.2 Language Policy

| Layer | Language | Rationale |
|-------|----------|-----------|
| SKILL.md frontmatter & body | **English** | Universal compatibility across all AI coding tools (Claude Code, Copilot, Cursor, etc.) |
| `references/*.md` | **English** | Technical templates must be language-agnostic at the structural level |
| `prompts/*.md` | **English** (with `{{OUTPUT_LANGUAGE}}` placeholder) | Prompts are templates; the placeholder is replaced at runtime |
| `.github/` community files | **English** | GitHub standard convention |
| All other project files | **English** | Consistency |
| `LICENSE` / `NOTICE` / `COPYING` | **Fixed text (GPL-3.0 / CC BY-NC-SA 4.0)** | License text must not be translated; must use official original text |

### 0.3 Runtime Output Language (Single Authority)

> **AUTHORITATIVE DECLARATION**: All generated novel content (chapters, character sheets, world-building docs) MUST be output in the language specified by the user via the `{{OUTPUT_LANGUAGE}}` variable.
>
> - **Variable**: `{{OUTPUT_LANGUAGE}}`
> - **Default**: `English`
> - **Supported**: Any language the underlying LLM supports
> - **Scope**: Applies to all generated narrative content, NOT to Skill infrastructure files
> - **Infrastructure files** (SKILL.md, references/, module definitions) remain in English to ensure cross-tool compatibility
>
> **Every prompt template in `prompts/` MUST include this block near the top:**
>
> ```
> ## Output Language Instruction
>
> All novel content you generate MUST be written in: {{OUTPUT_LANGUAGE}}
>
> If {{OUTPUT_LANGUAGE}} is set to "Chinese (简体中文)", write all narrative text,
> dialogue, character names (if appropriate), and world-building descriptions in Chinese.
> Structural labels (e.g., "Chapter 1", "Character Sheet") may remain in English
> or be translated — author's discretion.
>
> Default value: English
> ```
>
> **Each module's SKILL.md MUST include in its Constraints section:**
>
> ```
> - All generated content MUST be output in {{OUTPUT_LANGUAGE}} (default: English)
> - Infrastructure and metadata remain in English
> ```

### 0.4 Core Constraints

1. **SKILL.md is index + quick-reference ONLY** — no code templates, no long-form methodology. It points to `references/` and `prompts/` for depth.
2. **All code templates, structural patterns, and long-form methodology live in `references/method-patterns.md`** (or its split modules if >500 lines).
3. **`prompts/` folder is DUAL-MODE** — files inside are NOT for agent auto-invocation. They are standalone prompt templates for humans to copy-paste into any AI chat window.
4. **Harness Engineering compliance** — the Skill must embody: constraint-before-generation, structured memory, verification gates, modular decomposition, and feedback loops.
5. **Standardization, generalization, modularization, miniaturization, automation** — every module must be independently usable, composable, and under 500 lines.
6. **Split permission** — any file exceeding 500 lines MUST be split into sub-modules under the same directory.

> **NOTE**: This document (`README_FOR_AI.md`) is the project's master specification — the "S" (Specification) in SDD — not a SKILL.md. It is exempt from the 500-line limit because it consolidates the specification-driven development direction and the development-plan schema for the transmedia pipeline (novel → script → storyboard → comic → animation → film), enabling zero-from-scratch development from this document alone. It should still strive for conciseness and refer to external resources (`specs/`, `references/`) where possible.

### 0.5 License Policy (Dual Licensing)

> **DUAL LICENSING MODEL**: This Skill project employs a dual-licensing strategy to separate code infrastructure from creative content:
>
> | Component | License | Scope |
> |-----------|---------|-------|
> | **Skill Infrastructure** (code, templates, prompts, SKILL.md files, GitHub workflows, configuration files) | **GNU General Public License v3.0 (GPL-3.0)** | All Skill infrastructure files including SKILL.md, references/, prompts/, modules/, .github/, .gitignore, .editorconfig, etc. |
> | **Generated Novel Content** (chapters, character sheets, world-building docs produced by the Skill) | **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** | All narrative content generated by the Skill, including chapters, character descriptions, world-building documents, and story outlines |
>
> **Key Rules**:
> - Every generated novel file MUST begin with a CC BY-NC-SA 4.0 license header block
> - The `LICENSE` file at project root MUST contain the full GPL-3.0 text
> - The `LICENSES/` directory (if present) MAY contain the full CC BY-NC-SA 4.0 license text
> - SKILL.md YAML frontmatter MUST declare both licenses: `license: GPL-3.0` and `novel_content_license: CC-BY-NC-SA-4.0`
> - Prompt templates MUST instruct the AI to include the CC BY-NC-SA 4.0 header in all generated novel content
> - The GitHub Actions release workflow MUST verify license compliance before publishing
>
> **GPL-3.0 Summary**: Users are free to use, modify, and distribute the Skill infrastructure under the terms of GPL-3.0. Any modified version of the Skill infrastructure must also be released under GPL-3.0.
>
> **CC BY-NC-SA 4.0 Summary**: Users are free to share and adapt the novel content for non-commercial purposes, provided they give appropriate credit, indicate if changes were made, and distribute contributions under the same license.


## 1. Project Directory Structure

Generate the following complete directory tree. Every file listed is **mandatory**.

```text
github-novel-serialization-skill/
│
├── README.md                           # Project overview, quick start, architecture diagram
├── README_FOR_AI.md                   # THIS FILE — generation spec (seed file)
├── .gitignore                          # Git ignore rules
├── .editorconfig                       # Editor configuration
├── LICENSE                             # GNU General Public License v3.0 (GPL-3.0)
├── LICENSES/                           # Additional license texts
│   └── CC-BY-NC-SA-4.0.txt             # Full CC BY-NC-SA 4.0 license text
├── CODE_OF_CONDUCT.md                  # Community behavior standards
├── CONTRIBUTING.md                     # Contribution guidelines
├── SECURITY.md                         # Security policy & vulnerability reporting
├── CHANGELOG.md                        # Version history (Keep a Changelog format)
│
├── SKILL.md                            # Index + quick-reference (≤500 lines)
│
├── references/                         # Deep documentation & code templates
│   ├── method-patterns.md              # Master template file (split if >500 lines)
│   ├── method-patterns-worldbuilding.md    # [Split module] World-building templates
│   ├── method-patterns-character.md        # [Split module] Character design templates
│   ├── method-patterns-chapter.md          # [Split module] Chapter writing templates
│   ├── method-patterns-continuity.md       # [Split module] Continuity tracking templates
│   ├── method-patterns-publishing.md       # [Split module] Publishing & release templates
│   ├── glossary.md                         # Domain terminology & conventions
│   └── examples/                           # Concrete worked examples
│       ├── example-worldbuilding.md
│       ├── example-character-sheet.md
│       └── example-chapter-draft.md
│
├── prompts/                            # Dual-mode prompt templates (human copy-paste)
│   ├── README.md                       # How to use these prompts
│   ├── 01-implement-method.md          # Core implementation prompt
│   └── 02-robustness-checks.md         # Validation & quality-check prompt
│
├── modules/                            # Functional modules (independently usable)
│   ├── worldbuilding/
│   │   └── MODULE.md                   # World-building module contract (never SKILL.md)
│   ├── character-design/
│   │   └── MODULE.md                   # Character design module contract
│   ├── chapter-writing/
│   │   └── MODULE.md                   # Chapter writing module contract
│   ├── continuity-check/
│   │   └── MODULE.md                   # Continuity & consistency verification contract
│   ├── publishing-workflow/
│   │   └── MODULE.md                   # GitHub publishing & release contract
│   └── continuity-tracker/
│       └── MODULE.md                   # State tracking & memory persistence contract
│
└── .github/                            # GitHub community health files
    ├── ISSUE_TEMPLATE/
    │   ├── bug-report.yml
    │   ├── feature-request.yml
    │   └── config.yml
    ├── PULL_REQUEST_TEMPLATE.md
    ├── FUNDING.yml
    ├── dependabot.yml
    └── workflows/
        └── novel-release.yml           # Automated release workflow template
```

---

## 2. SKILL.md — Index & Quick-Reference Specification

### 2.1 YAML Frontmatter

```yaml
---
name: github-novel-serialization
description: >
  Orchestrates AI-assisted novel writing and GitHub-based serialization.
  Use when the user asks to write a novel, create characters, build worlds,
  draft chapters, check continuity, or publish chapters to a GitHub repository.
  Covers the full lifecycle: world-building → character design → chapter drafting →
  continuity verification → GitHub publishing.
license: GPL-3.0
novel_content_license: CC-BY-NC-SA-4.0
license_note: >
  Skill infrastructure is licensed under GNU General Public License v3.0 (GPL-3.0).
  Generated novel content (chapters, character sheets, world-building docs) is licensed
  under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
compatibility: Works with any LLM-backed coding agent (Claude Code, GitHub Copilot, Cursor, etc.)
metadata:
  author: community
  version: 1.0.0
  output_language_default: English
---
```

### 2.2 Body Structure (≤500 lines)

The SKILL.md body must contain ONLY the following sections:

| Section | Content | Max Lines |
|---------|---------|-----------|
| `## Overview` | One-paragraph mission statement | 5 |
| `## Output Language` | Reference `{{OUTPUT_LANGUAGE}}` (see Section 0.3 for authoritative declaration) | 5 |
| `## Quick Start` | 5-step numbered workflow | 15 |
| `## Module Index` | Table mapping module name → one-line purpose → file path | 20 |
| `## Workflow Pipeline` | DAG-style pipeline: Plan → Build → Draft → Verify → Publish | 30 |
| `## Quick Reference: File Conventions` | Naming rules, directory structure for novel repos | 20 |
| `## Quick Reference: Git Conventions` | Branch naming, commit format, tag format | 15 |
| `## Quick Reference: Continuity State` | What state files to maintain and where | 15 |
| `## Verification Gates` | Checklist of mandatory checks before publish | 15 |
| `## Cross-References` | Pointers to `references/` and `prompts/` | 10 |
| `## Constraints & Boundaries` | Hard rules the agent must never violate | 20 |

**Total target: ~170 lines. Hard ceiling: 500 lines.**

### 2.3 Critical Rule

> **NEVER embed code templates, long-form methodology, or step-by-step procedural instructions in SKILL.md.** All such content belongs in `references/method-patterns.md` or its split modules. SKILL.md only says WHAT exists and WHERE to find it.


---

## 3. references/ — Deep Documentation & Code Templates

### 3.1 `method-patterns.md` — Master Template

This is the **single source of truth** for all structural templates, code patterns, and long-form methodology. It must contain:

| Section | Content |
|---------|---------|
| `## World-Building Templates` | Structured templates for magic systems, geography, politics, technology, history, culture |
| `## Character Design Templates` | Character sheet format: identity, psychology, arc, relationships, voice profile |
| `## Chapter Writing Templates` | Scene structure, POV rules, pacing formula, dialogue formatting, chapter header format |
| `## Continuity Tracking Templates` | State file format: timeline, character states, location states, unresolved threads |
| `## Publishing Workflow Templates` | Git tag format, release note template, chapter file naming convention |
| `## Style Consistency Rules` | Voice register, tense conventions, terminology lock, forbidden patterns |

**Split Rule**: If `method-patterns.md` exceeds 500 lines, split into:
- `method-patterns-worldbuilding.md`
- `method-patterns-character.md`
- `method-patterns-chapter.md`
- `method-patterns-continuity.md`
- `method-patterns-publishing.md`

The master file then becomes an index pointing to each split module. See **Section 7** for the splitting protocol.

### 3.2 `glossary.md`

Define all domain-specific terms used across the Skill:
- Novel serialization terminology (arc, chapter, scene, beat, POV)
- Git terminology as used in this context (tag, release, branch)
- State tracking terminology (continuity file, state snapshot, thread ledger)

### 3.3 `examples/` — Worked Examples

Each example file must demonstrate a complete, concrete instantiation of the corresponding template:
- `example-worldbuilding.md` — A fully filled-out world-building document for a sample novel
- `example-character-sheet.md` — A fully filled-out character sheet
- `example-chapter-draft.md` — A complete sample chapter with annotations

---

## 4. prompts/ — Dual-Mode Prompt Templates

### 4.1 Design Philosophy

Files in `prompts/` are **NOT** for agent auto-invocation. They are **standalone, self-contained prompt templates** that a human user can:
1. Open in any text editor
2. Copy the entire content
3. Paste into ANY AI chat window (ChatGPT, Claude, Gemini, Copilot, etc.)
4. Get immediate, structured output

### 4.2 `prompts/README.md`

Must explain:
- What "dual-mode" means (agent-assisted vs. human copy-paste)
- How to use each prompt file
- How to customize the `{{OUTPUT_LANGUAGE}}` placeholder (see Section 0.3 for authoritative declaration)
- How to combine prompts for complex workflows

### 4.3 `prompts/01-implement-method.md`

A comprehensive prompt template that, when pasted into any AI chat, instructs the AI to:
1. Accept novel parameters (genre, setting, themes, target length)
2. Generate a complete world-building document
3. Generate character sheets for all major characters
4. Produce a chapter-by-chapter outline
5. Draft the first chapter
6. Output everything in `{{OUTPUT_LANGUAGE}}`

Must include:
- Clear role assignment ("You are a professional novel architect...")
- Structured output format specifications
- `{{OUTPUT_LANGUAGE}}` placeholder (see Section 0.3 for authoritative declaration)
- Variable placeholders for user customization: `{{GENRE}}`, `SETTING}}`, `{{THEMES}}`, `{{TARGET_CHAPTERS}}`, `{{TONE}}`, `{{POV_STYLE}}`
- **Novel Content License Header**: Every generated novel file MUST begin with the following CC BY-NC-SA 4.0 license block:

```
# [Novel Title]

This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/
or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license,
  and indicate if changes were made.
- NonCommercial — You may not use the material for commercial purposes.
- ShareAlike — If you remix, transform, or build upon the material, you must distribute
  your contributions under the same license as the original.
```

### 4.4 `prompts/02-robustness-checks.md`

A comprehensive prompt template that, when pasted into any AI chat, instructs the AI to:
1. Accept a draft chapter or world-building document as input
2. Run a multi-dimensional quality check:
   - Continuity consistency (character names, locations, timeline)
   - Style consistency (voice, tense, register)
   - Plot logic (causality, motivation, foreshadowing payoff)
   - Pacing analysis (scene-to-sequel ratio, tension curve)
   - Dialogue authenticity (voice differentiation per character)
   - **License compliance**: Verify that the generated content includes the CC BY-NC-SA 4.0 license header
3. Output a structured report with severity levels (Critical / Warning / Suggestion)
4. Output in `{{OUTPUT_LANGUAGE}}`


---

## 5. modules/ — Functional Sub-Skills

### 5.1 Design Principles

Each module is an **independently usable sub-skill** that:
- Has its own `MODULE.md` with proper YAML frontmatter (including `license: GPL-3.0` and `novel_content_license: CC-BY-NC-SA-4.0`)
- Is named `MODULE.md`, never `SKILL.md`: skill loaders discover skills by filename, and a `SKILL.md` in each module directory registers every module as a separate, unwanted skill
- Can be loaded independently by an agent when referenced explicitly
- Follows the same index-only pattern as the root SKILL.md
- References `references/` for templates
- Is under 500 lines

### 5.2 Module Specifications

#### `modules/worldbuilding/MODULE.md`
- **name**: `novel-worldbuilding`
- **Purpose**: Generate and maintain world-building documents
- **Triggers**: "build a world", "create setting", "design magic system"
- **References**: `../../references/method-patterns-worldbuilding.md`

#### `modules/character-design/MODULE.md`
- **name**: `novel-character-design`
- **Purpose**: Generate and maintain character sheets
- **Triggers**: "create character", "design protagonist", "character relationships"
- **References**: `../../references/method-patterns-character.md`

#### `modules/chapter-writing/MODULE.md`
- **name**: `novel-chapter-writing`
- **Purpose**: Draft chapters following established style and continuity
- **Triggers**: "write chapter", "draft next scene", "continue story"
- **References**: `../../references/method-patterns-chapter.md`

#### `modules/continuity-check/MODULE.md`
- **name**: `novel-continuity-check`
- **Purpose**: Verify consistency across all chapters and state files
- **Triggers**: "check continuity", "verify consistency", "find plot holes"
- **References**: `../../references/method-patterns-continuity.md`

#### `modules/publishing-workflow/MODULE.md`
- **name**: `novel-publishing-workflow`
- **Purpose**: Manage Git-based publishing pipeline for serialized chapters
- **Triggers**: "publish chapter", "create release", "tag version"
- **References**: `../../references/method-patterns-publishing.md`

#### `modules/continuity-tracker/MODULE.md`
- **name**: `novel-continuity-tracker`
- **Purpose**: Maintain persistent state files (timeline, character states, thread ledger)
- **Triggers**: "update state", "track timeline", "log character status"
- **References**: `../../references/method-patterns-continuity.md`

---

## 6. Harness Engineering Compliance Matrix

Every generated file must satisfy the following Harness Engineering principles:

| Principle | Implementation Requirement |
|-----------|--------------------------|
| **Constraint before generation** | SKILL.md `## Constraints & Boundaries` section must list hard rules before any workflow steps |
| **Structured memory** | `modules/continuity-tracker/` defines state file formats; state is persisted in structured Markdown files, not in conversation context |
| **Verification gates** | `## Verification Gates` in SKILL.md + `prompts/02-robustness-checks.md` — no chapter publishes without passing checks |
| **Modular decomposition** | Each `modules/*/MODULE.md` is independently loadable; no circular dependencies between modules |
| **Feedback loops** | `02-robustness-checks.md` produces structured feedback that feeds back into the next drafting iteration |
| **Progressive disclosure** | SKILL.md (Layer 1: index) → references/ (Layer 2: templates) → examples/ (Layer 3: worked examples) |
| **Context budget management** | SKILL.md ≤500 lines; each module `MODULE.md` ≤500 lines; references split at 500-line boundary |
| **Human-in-the-loop** | `prompts/` folder enables human oversight; publishing workflow requires manual Git tag creation |
| **Error recovery** | Continuity tracker maintains state snapshots; if a chapter breaks continuity, the system can identify the exact divergence point |
| **Role isolation** | Each module has a single responsibility; worldbuilding module does not write chapters; chapter module does not design characters |
| **License compliance** | All generated files must include appropriate license headers; novel content must include CC BY-NC-SA 4.0 header |


---

## 7. File Size & Splitting Rules

### 7.1 Hard Limit

**No single file shall exceed 500 lines.** This applies to:
- SKILL.md (root and all modules)
- references/method-patterns.md (and its split modules)
- prompts/*.md
- Any other Markdown file in the project

> **Exception**: `README_FOR_AI.md` (this document) is the project's master specification (the "S" in SDD) and is exempt from the 500-line limit, as it consolidates the specification-driven development direction and the development-plan schema for the transmedia pipeline.

### 7.2 Splitting Protocol

When a file approaches 500 lines:
1. Identify logical section boundaries
2. Extract each section into its own file with a descriptive name
3. Replace the extracted section with a one-line pointer: `See [filename](filepath) for details.`
4. Update all cross-references

### 7.3 Split Example

If `method-patterns.md` exceeds 500 lines:

```text
references/
├── method-patterns.md                  # Now an INDEX only (~30 lines)
├── method-patterns-worldbuilding.md    # Extracted: world-building templates
├── method-patterns-character.md        # Extracted: character design templates
├── method-patterns-chapter.md          # Extracted: chapter writing templates
├── method-patterns-continuity.md       # Extracted: continuity tracking templates
└── method-patterns-publishing.md       # Extracted: publishing workflow templates
```

The master `method-patterns.md` becomes:

```markdown
# Method Patterns — Index

This file is an index. Detailed templates are split into sub-modules.

| Module | File | Content |
|--------|------|---------|
| World-Building | [method-patterns-worldbuilding.md](method-patterns-worldbuilding.md) | Magic systems, geography, politics |
| Character Design | [method-patterns-character.md](method-patterns-character.md) | Character sheets, arcs, voice |
| Chapter Writing | [method-patterns-chapter.md](method-patterns-chapter.md) | Scene structure, pacing, dialogue |
| Continuity | [method-patterns-continuity.md](method-patterns-continuity.md) | State tracking, timeline, ledger |
| Publishing | [method-patterns-publishing.md](method-patterns-publishing.md) | Git workflow, release format |
```

---

## 8. Versioning Strategy

The project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html):

- **MAJOR** version: Increment for incompatible API/skill contract changes
- **MINOR** version: Increment for backwards-compatible functionality additions
- **PATCH** version: Increment for backwards-compatible bug fixes

Version tags follow the format `v{major}.{minor}.{patch}` (e.g., `v1.2.3`).

---

## 9. Quality Assurance Checklist

Before finalizing the generated project, verify:

- [ ] SKILL.md has valid YAML frontmatter with `name` and `description`
- [ ] SKILL.md body is ≤500 lines
- [ ] SKILL.md contains NO code templates or long-form methodology
- [ ] All code templates are in `references/method-patterns.md` (or split modules)
- [ ] `prompts/` files are self-contained and copy-pasteable
- [ ] `prompts/` files include `{{OUTPUT_LANGUAGE}}` placeholder
- [ ] All module SKILL.md files have valid YAML frontmatter
- [ ] All module SKILL.md files are ≤500 lines
- [ ] No file exceeds 500 lines (see Section 7.1 for exceptions)
- [ ] All GitHub standard files are present and properly formatted
- [ ] Cross-references between files are valid
- [ ] `{{OUTPUT_LANGUAGE}}` instruction appears in SKILL.md, all prompts, and all module SKILLs (see Section 0.3 for authoritative declaration)
- [ ] Harness Engineering compliance matrix is fully satisfied
- [ ] `.gitignore` covers all necessary patterns
- [ ] `CHANGELOG.md` follows Keep a Changelog format
- [ ] `LICENSE` file contains full GPL-3.0 text
- [ ] `LICENSES/CC-BY-NC-SA-4.0.txt` contains full CC BY-NC-SA 4.0 license text
- [ ] SKILL.md frontmatter declares `license: GPL-3.0` and `novel_content_license: CC-BY-NC-SA-4.0`
- [ ] Generated novel content includes CC BY-NC-SA 4.0 license header
- [ ] `.editorconfig` covers both `*.yml` and `*.yaml`
- [ ] `.github/dependabot.yml` is present

---

## 10. Automated Verification

To ensure generated projects meet all requirements, run the following verification steps:

1. **Line count check**: Verify no file exceeds 500 lines (excluding exempt files)
2. **File presence check**: Verify all mandatory files from Section 1 directory tree exist
3. **YAML validation**: Validate all `.yml` files are syntactically correct
4. **Link check**: Verify all internal cross-references resolve
5. **Language check**: Verify `{{OUTPUT_LANGUAGE}}` placeholder appears in all required locations
6. **Frontmatter check**: Verify the root `SKILL.md` and every `modules/*/MODULE.md` have valid YAML frontmatter
7. **License check**: Verify `LICENSE` file contains "GNU GENERAL PUBLIC LICENSE" and version "3"
8. **Novel content license check**: Verify `LICENSES/CC-BY-NC-SA-4.0.txt` exists and contains "Creative Commons"
9. **SKILL.md license field check**: Verify `license: GPL-3.0` and `novel_content_license: CC-BY-NC-SA-4.0` are present in SKILL.md frontmatter

---

## 11. Anti-Patterns — What NOT To Do

| Anti-Pattern | Why It's Wrong | Correct Approach |
|-------------|---------------|-----------------|
| Embedding full templates in SKILL.md | Bloats context, violates progressive disclosure | Put templates in `references/`, SKILL.md only indexes |
| Making `prompts/` files auto-invocable | Defeats the dual-mode design | Keep them as standalone copy-paste templates |
| Writing prompts in a specific language | Limits portability | Write in English with `{{OUTPUT_LANGUAGE}}` placeholder |
| Creating monolithic modules | Violates modularization principle | Each module = one responsibility, ≤500 lines |
| Hardcoding output language | Prevents multilingual use | Always use `{{OUTPUT_LANGUAGE}}` variable (see Section 0.3) |
| Skipping verification gates | Breaks harness engineering | Every chapter must pass continuity check before publish |
| Putting state in conversation context | Loses state across sessions | Persist state in structured Markdown files |
| Ignoring `.gitignore` | Commits temp files, leaks secrets | Include comprehensive ignore rules |
| Missing license headers | Violates dual licensing model | Every novel file must include CC BY-NC-SA 4.0 header; all infrastructure files must comply with GPL-3.0 |

> **NOTE**: Sections 0.4 (Core Constraints) and this Anti-Patterns table serve complementary purposes: Section 0.4 states the positive rules, while this table illustrates common violations. Together they form the complete constraint specification.

---

## 12. Final Note

This Skill project is not just a collection of prompts. It is a **harness-engineered system** that transforms a raw LLM into a reliable, stateful, multi-session novel-writing agent. Every file exists to constrain, guide, and verify. The goal is deterministic quality — not lucky outputs.

**Dual Licensing Notice**:
- The Skill infrastructure (code, templates, prompts, configuration) is licensed under **GNU General Public License v3.0 (GPL-3.0)**. See the `LICENSE` file for full terms.
- Generated novel content (chapters, character sheets, world-building documents) is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**. See the `LICENSES/CC-BY-NC-SA-4.0.txt` file for full terms.

Generate all files now. Follow every specification above. Do not improvise structure.

## 13. Agile Development Lifecycle — SDD + ATDD with Phase-Gated Review

This skill applies two agile practices to any multi-stage generation effort,
including the optional transmedia pipeline (novel -> script/storyboard -> comic
-> animation -> film). They are specified in `docs/adr/0005-engineering-sdd-atdd.md`
and the project plan `docs/multimedia-pipeline-plan.md`.

### 13.1 Specification-Driven Development (SDD)

Every task phase begins with a written specification before any content or code
is generated. The spec defines inputs, outputs, and acceptance criteria. The
spec is the contract; generation follows it.

### 13.2 Acceptance Test-Driven Development (ATDD)

Before implementation, each phase declares executable acceptance tests. A phase
is "done" only when its acceptance tests pass. Tests are checked mechanically
where possible (for example `scan_hygiene`, `check_refs`, consistency scripts)
and by checklist where not.

### 13.3 Phase-Gated Review (stop and wait)

After a phase's acceptance tests pass, the pipeline STOPS and waits for explicit
human review and sign-off. It does NOT auto-advance to the next phase. This
extends the existing three-stage review and verification gates: the gate
is a hard stop, not a soft checkpoint.

### 13.4 Branch strategy for multi-stage work

- One `feat/pipeline-{stage}` branch per stage.
- `main` is protected; a stage merges only after its gate sign-off.
- The novel's continuity state (`state/`) remains the single source of truth
  consumed by every downstream stage.

### 13.5 Lifecycle loop

```
Spec (SDD) -> Acceptance Tests (ATDD) -> Implement -> Run Tests -> STOP: human gate -> (approve -> next stage | reject -> fix/rework)
```

## 14. Transmedia Pipeline Specification Direction (SDD Specification Hub)

> **Role**: This file (`README_FOR_AI.md`) is the project's master specification — the "S" (Specification) in SDD — authorized by `docs/adr/0005-engineering-sdd-atdd.md`. This chapter is the specification hub: it defines the specification-driven development direction for the transmedia pipeline — novel → script → storyboard → comic → animation → film.

> **How to use**: This chapter inlines a concise skeleton for each stage (goal / inputs / outputs / acceptance criteria / generation method) so the project can be developed zero-from-scratch, phase by phase, from this document alone. The full executable specs live in the `specs/` directory (each file ≤500 lines, per Section 7). A concrete roadmap instance is in `docs/multimedia-pipeline-plan.md` (declared `conforms to` this Section 14). All stages follow the SDD + ATDD + gate lifecycle in Section 13.

### 14.1 Novel (baseline — already built, single source of truth)
- **Goal**: High-quality, continuity-controlled long-form web novel — the core capability of this repository.
- **Inputs**: Author intent, world-building, character design.
- **Outputs**: Chapter drafts, character sheets, world-building docs, continuity state (`state/`).
- **Acceptance**: Passes three-stage review + `check_refs` / `scan_hygiene`; zero continuity conflicts.
- **Generation method**: Existing novel skill flow (worldbuilding → character-design → chapter-writing → continuity-check → publishing-workflow).
- **Detailed spec**: `specs/01-novel.md`.
- **Transmedia position**: Downstream script / storyboard / comic / animation / film all consume `state/`; no separate state is introduced.

### 14.2 Script
- **Goal**: Adapt novel chapters into shootable scripts (scenes, dialogue, action, beats).
- **Inputs**: Novel chapters + continuity state.
- **Outputs**: Per-chapter beat sheet + structured script.
- **Acceptance**: A beat sheet produced per chapter; passes existing text reviews (humanizer / continuity / punctuation); character motivation consistent with the novel.
- **Generation method**: Chapter → beat sheet → script draft → text review → human gate.
- **Detailed spec**: `specs/02-script.md`.

### 14.3 Storyboard
- **Goal**: Turn the script into shot specifications (shot size / camera / duration / visual description / dialogue).
- **Inputs**: Script + novel state.
- **Outputs**: Storyboard table (structured JSON: shot no., shot size, camera, duration, visual, dialogue).
- **Acceptance**: Storyboard covers every script scene; shot-duration budget is shootable; consistent with character/style.
- **Generation method**: Script → storyboard spec → consistency check → human gate.
- **Detailed spec**: `specs/03-storyboard.md`.

### 14.4 Comic
- **Goal**: Render the storyboard into sequential art panels, locking character and style.
- **Inputs**: Storyboard + character/style guide derived from novel state.
- **Outputs**: Comic panels (images) + asset naming.
- **Acceptance**: Character-face / style consistency check script passes; panels conform to spec.
- **Generation method**: Lock character/style → render panels → visual consistency review → human gate.
- **Detailed spec**: `specs/04-comic.md`.
- **Tool maturity**: Medium; the consistency script is a key go/no-go gate.

### 14.5 Animation
- **Goal**: Animate the storyboard + comic assets into a sample reel.
- **Inputs**: Storyboard + comic assets.
- **Outputs**: Animation clips (video).
- **Acceptance**: Sample reel passes visual-consistency + pacing checks; asset reuse rate meets target.
- **Generation method**: Shot-animation spec → render → pacing/consistency review → human gate (go/no-go).
- **Detailed spec**: `specs/05-animation.md`.
- **Tool maturity**: Medium-low; large cost/quality gap — state it honestly.

### 14.6 Film
- **Goal**: Edit animation clips into a finished film (dubbing / score / post / A-V sync).
- **Inputs**: Animation clips.
- **Outputs**: Finished film.
- **Acceptance**: Finished film passes duration / structure / A-V-sync checks.
- **Generation method**: Edit script → dubbing/score → post → A-V-sync review → human final gate (go/no-go).
- **Detailed spec**: `specs/06-film.md`.
- **Tool maturity**: Low; least mature tooling, highest risk — may be halted at any time.

### 14.7 Governance & Asset Conventions (Stage 0)
- **Branches**: One `feat/pipeline-{stage}` branch per stage; `main` is protected and merges only after gate sign-off.
- **Asset directory**: `assets/{stage}/` (script / storyboard / comic / animation / film).
- **Cost ceiling**: A cost cap per stage; exceeding it triggers a go/no-go gate decision.
- **Detailed spec**: `specs/00-governance.md`.

### 14.8 Conventions for zero-from-scratch development using README alone
- This hub chapter (Section 14) + the existing Sections 0–13 (novel skill, SDD/ATDD, gates) + `specs/` form a complete specification; `docs/multimedia-pipeline-plan.md` is one concrete roadmap instance. The format of every plan document is governed by the Plan Schema in Section 15; each plan document MUST declare `Conforms to: README_FOR_AI.md §15` (and §14 for pipeline work).
- Every stage follows the Section 13 lifecycle: `Spec (SDD) → Acceptance Tests (ATDD) → Implement → Run Tests → STOP: human gate → (approve → next stage | reject → fix/rework)`.
- Downstream stages MUST consume upstream facts within `state/` and must not introduce separate state.
- Stages with immature tooling (comic / animation / film) state gaps honestly; the gate decides go/no-go. If a stage fails its gate with no acceptable fix → halt that stage and all subsequent ones, preserve assets, and do not pollute `main`.

## 15. Development Plan Specification (Plan Schema)

> **Role**: Defines the normative schema for any development-plan document in this project. A concrete instance is `docs/multimedia-pipeline-plan.md`. A plan document makes the Section 13 lifecycle executable: it binds the Section 14 specification direction to a sequenced set of gated stages with explicit acceptance tests. With this schema, the project can be planned and built from `README_FOR_AI.md` alone, without copying the repository.

### 15.1 Relationship to other sections
- Section 13 defines the lifecycle (SDD + ATDD + phase-gated review).
- Section 14 defines per-stage specification direction (the "what" to build).
- This Section 15 defines the plan-document format (the "how to write the plan").
- Every plan document MUST open with a `Conforms to` declaration referencing this Section 15, and — for pipeline work — Section 14.

### 15.2 Plan document metadata
Each plan document begins with a metadata block identifying it and its conformance:

```yaml
plan:
  id: <short-id>                  # e.g. multimedia-pipeline
  title: <human-readable title>
  conforms_to:
    - "README_FOR_AI.md §15"      # plan schema (mandatory)
    - "README_FOR_AI.md §14"      # pipeline direction (if pipeline work)
  status: draft | active | done
  created: <YYYY-MM-DD>
  owner: <role or person>
  cost_ceiling: <amount | "TBD">
```

If YAML is unsuitable, use a Markdown table; the required fields are `id`, `conforms_to`, and `status`.

### 15.3 Stage block schema
A plan is an ordered list of stages. Each stage block MUST contain:

- **Stage id / name** — e.g. `S1-novel`.
- **Goal** — one sentence, mirroring the matching Section 14.{n} Goal.
- **Inputs / Outputs** — concrete artifacts (files, `assets/{stage}/`, `state/`).
- **Specification pointer** — the Section 14.{n} entry or `specs/*.md` file that defines the stage. If neither exists, the plan MUST first create the spec (SDD: spec before implementation).
- **Acceptance tests (ATDD)** — explicit, checkable list. Prefer mechanical checks (`scan_hygiene`, `check_refs`, consistency scripts) with pass criteria; fall back to checklists.
- **Gate** — explicit human review / stop point; record sign-off (approve / reject) and date.
- **Cost / risk note** — tool maturity and go/no-go triggers, especially for comic / animation / film (see §14.4–§14.6).

### 15.4 Acceptance-test block format

```
- [ ] <test-id> <description>            (mechanical | checklist)
    pass criterion: <observable condition>
    tool: <script or checklist name> | manual
```

A stage is "done" only when every mechanical test passes, every checklist item is verified, and the gate (§13.3) is signed off.

### 15.5 Halt and rollback rule
If a stage fails its gate with no acceptable fix, the plan MUST state: halt that stage and all downstream dependent stages, preserve produced assets, do not merge to `main`, and open a remediation or close-out record. This mirrors §14.8.

### 15.6 Condensed example (instantiate from README alone)
A minimal plan that demonstrates the schema:

```markdown
# Plan: Transmedia Pipeline (mini)

Conforms to: README_FOR_AI.md §15, §14

plan:
  id: multimedia-pipeline
  status: active

## S1 — Novel (baseline)
Goal: continuity-controlled web novel (§14.1).
Inputs: author intent. Outputs: chapters + state/.
Spec: specs/01-novel.md.
Acceptance:
  - [ ] AT1 scan_hygiene clean          (mechanical) tool: scripts/scan_hygiene.py
  - [ ] AT2 check_refs no broken refs   (mechanical) tool: scripts/check_refs.py
  - [ ] AT3 three-stage review sign-off (checklist)
Gate: STOP — human sign-off before S2.

## S2 — Script
Goal: adapt chapters into scripts (§14.2).
...
```

This shows that, using §14 direction plus the §15 schema, a complete plan can be drafted from `README_FOR_AI.md` without copying the repository.
