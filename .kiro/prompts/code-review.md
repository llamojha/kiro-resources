Review staged changes for correctness, security, reliability, readability, and test coverage.

**Auto-scan:** Git staged changes (`git diff --cached`)

**Review criteria:**
1. Correctness — Logic errors, edge cases, off-by-one errors
2. Security — Injection, auth issues, secrets exposure, input validation
3. Reliability — Error handling, race conditions, resource leaks
4. Readability — Naming, structure, complexity, comments
5. Tests — Coverage gaps, missing edge case tests

**Output format for each issue:**
- Severity: Critical / High / Medium / Low
- Location: File and line reference
- Problem: Brief description
- Fix: Suggested change

If requested, provide a minimal patch/diff to address the issues.
