# Kiro Prompt Pack

A collection of 12 reusable prompts for the [Kiro CLI](https://kiro.dev/cli/).

## Installation

### Option 1: Clone for a single project (local prompts)

```bash
# In your project root
git clone https://github.com/llamojha/kiro-prompts.git .kiro-prompts-temp
cp -r .kiro-prompts-temp/.kiro/prompts .kiro/prompts
rm -rf .kiro-prompts-temp
```

### Option 2: Install globally (available in all projects)

```bash
git clone https://github.com/llamojha/kiro-prompts.git
cp -r kiro-prompts/.kiro/prompts ~/.kiro/prompts
rm -rf kiro-prompts
```

### Option 3: Cherry-pick individual prompts

```bash
# Copy just the prompts you want
curl -o ~/.kiro/prompts/code-review.md https://raw.githubusercontent.com/llamojha/kiro-prompts/main/.kiro/prompts/code-review.md
```

## Usage

In Kiro CLI chat, invoke any prompt with `@prompt-name`:

```bash
@code-review
@security-checklist
@debug-helper
```

## Prompts

### commit-message

Generate a commit message for staged changes.

- **Input:** Auto-scans git staged changes
- **Format:** Conventional Commits (feat/fix/docs/style/refactor/test/chore)
- **Output:** One-line summary (max 72 chars), optional body for complex changes

---

### code-review

Review staged changes for correctness, security, reliability, readability, and test coverage.

- **Input:** Auto-scans git staged changes
- **Output:** Issues with severity, location, problem description, and fix suggestions

---

### mock-testing

Generate a test plan with mocks/stubs strategy and sample tests.

- **Input:** Paste code or reference with @filename
- **Framework:** Auto-detects from project config (package.json, pyproject.toml). Asks if not found.
- **Output:** Test plan, mocking strategy, and working test implementations

---

### daily-next-step

Summarize current status and output next actions for today.

- **Input:** Auto-scans `.kiro/specs/` and `TODO.md`
- **Output:** Status summary (done/blocked/in-progress) and 1-3 concrete next actions

---

### security-checklist

Security-focused review of staged changes.

- **Input:** Auto-scans git staged changes
- **Reviews:** Secrets, auth/authz, input validation, least privilege, sensitive data logging, dependency risks
- **Output:** Findings with risk level and mitigation recommendations

---

### debug-helper

Debug helper for errors, stack traces, and logs.

- **Input:** Paste error, or auto-scans terminal output and log files (`*.log`, `logs/`, `.kiro/logs/`, `tmp/`)
- **Output:** Likely root causes, clarifying questions, debugging actions, safe fix with rollback notes

---

### prompt-builder

Turn a rough goal into a polished, reusable prompt.

- **Input:** Describe your rough goal or idea
- **Output:** Clarifying questions, then a polished prompt with clear objective, constraints, and output format

---

### refactor-code

Refactor staged changes for clarity, structure, and performance.

- **Input:** Auto-scans git staged changes
- **Output:** List of changes with rationale, before/after diff, verification steps

---

### generate-documentation

Generate documentation for code.

- **Input:** Reference file/folder with @filename, paste code, or say "staged changes"
- **Doc style:** Auto-detects (JSDoc, docstrings, etc.) or specify preferred format
- **Output:** Overview, API docs, examples, edge cases and gotchas

---

### codebase-search

Find or change code in the codebase.

- **Input:** Describe what you want to find or change
- **Output:** Search targets (symbols, patterns, regex), likely locations, step-by-step execution plan

---

### seo-meta-sitemap-robots

Generate or improve SEO and crawler assets.

- **Input:** Auto-scans existing SEO files. Asks for URL if not found.
- **Output:** Social tags (Open Graph/Twitter), sitemap.xml, robots.txt, llms.txt with exact file edits

---

### refresh-foundational-steering-and-docs

Refresh foundational steering documents and docs.

- **Input:** Auto-scans `.kiro/steering/`, `docs/`, and `README.md`
- **Output:** Audit of outdated guidance, revised structure, updated conventions, PR checklist

## Quick Reference

| Prompt | Input | Description |
|--------|-------|-------------|
| `commit-message` | Auto: staged changes | Generate conventional commit message |
| `code-review` | Auto: staged changes | Review for correctness, security, reliability, readability |
| `mock-testing` | Code input | Generate test plan with mocks/stubs |
| `daily-next-step` | Auto: specs + TODO.md | Status summary and next actions |
| `security-checklist` | Auto: staged changes | Security review |
| `debug-helper` | Paste or auto: logs | Root cause analysis and fix suggestions |
| `prompt-builder` | Describe goal | Turn rough goals into polished prompts |
| `refactor-code` | Auto: staged changes | Refactor with before/after diff |
| `generate-documentation` | File, paste, or staged | Generate docs |
| `codebase-search` | Describe target | Search targets and execution plan |
| `seo-meta-sitemap-robots` | Auto or URL input | SEO and crawler assets |
| `refresh-foundational-steering-and-docs` | Auto: steering + docs | Refresh steering docs |

## Contributing

Contributions welcome! Feel free to:
- Submit new prompts via PR
- Improve existing prompts
- Report issues

## License

MIT License - see [LICENSE](LICENSE) for details.
