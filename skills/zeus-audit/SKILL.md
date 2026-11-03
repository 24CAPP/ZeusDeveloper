---
name: zeus-audit
description: >
  Rigorous principal engineer audit of a repository or feature: exposes critical bugs,
  vulnerabilities, concurrency hazards, missing invariant tests, latency bottlenecks, and structural bloat.
  Generates an actionable, prioritized report without altering files. Use for "audit this codebase",
  "review entire repo", "find vulnerabilities and bloat", /zeus-audit.
argument-hint: "[scope or path]"
license: MIT
---

# Zeus Audit: Comprehensive Engineering Review

Conduct a comprehensive architectural, security, and performance audit across the designated scope.
Do not modify any files during this audit; produce an unsparing, prioritized diagnostic report.

---

## 1. Audit Dimensions

Examine the target files across five critical axes:

### A. Reliability & Concurrency Invariants
- Unhandled rejections, silent exception swallowing, or orphaned background tasks.
- Check-then-act race conditions (TOCTOU) and unsafe shared mutable state.
- Leaking resources (unclosed database handles, unmanaged sockets, unbounded memory collections).

### B. Security & Attack Surface
- Injection vulnerabilities (SQL, NoSQL, command injection, path traversal, SSRF).
- Authentication, authorization bypasses, or missing session expiration.
- Unsanitized user inputs crossing trust boundaries.
- Hardcoded credentials, insecure crypto algorithms, or weak randomness.

### C. Scalability & Operational Hotspots
- N+1 query patterns and unindexed database queries.
- CPU hotspots: accidental $O(N^2)$ iterations over incoming user data.
- Blocking operations within asynchronous event loops.

### D. Architectural Bloat & Redundancy
- Dead code paths, abandoned features, and duplicate implementations.
- Third-party packages easily replaced by runtime standard libraries.
- Sprawling abstraction towers that obscure business logic.

### E. Verification Vacuum
- Critical business rules or authorization checks lacking deterministic automated tests.

---

## 2. Audit Report Format

Structure the findings in descending order of severity:

```markdown
# Zeus Engineering Audit

**Scope Analyzed**: `<path or module>`  
**Assumed Load Profile**: `<single-user / high-concurrency cloud / edge>`

---

### [CRITICAL / HIGH / MEDIUM / LOW] - <Title of Finding>
- **File & Line**: `[path/to/file.ext#L10-L25](file:///path/to/file.ext)`
- **Mechanism**: Clear explanation of how the bug, vulnerability, or failure triggers under real-world conditions.
- **Consequence**: Data loss, security breach, thread stall, or resource exhaustion.
- **Sovereign Remedy**: The minimal, most robust correction to eliminate the vulnerability.

---

### Bloat & Deletion Ledger
- **Candidate Files / Modules for Removal**: List of dead code with justification.
- **Dependency Elimination Targets**: Packages that can be substituted with native code.
```
