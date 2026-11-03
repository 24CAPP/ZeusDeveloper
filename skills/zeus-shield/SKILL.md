---
name: zeus-shield
description: >
  Aegis-grade security audit and threat modeling for codebases, APIs, and AI agents.
  Hunts concrete vulnerabilities across trust boundaries (injection, auth bypass, IDOR, SSRF,
  TOCTOU races, prompt injection, and memory safety) and delivers the minimal effective fix.
  Use for "security audit", "penetration test", "find vulnerabilities", "check security", /zeus-shield.
argument-hint: "[target file, directory, or endpoint]"
license: MIT
---

# Zeus Shield: Enterprise Security & Vulnerability Audit

Conduct an unsparing, Aegis-grade security review.
Focus exclusively on verified trust boundary violations that expose real principals or assets to concrete harm.
Speculative warnings and generic linter complaints are forbidden; every finding requires source evidence and an exploitable path.

---

## 1. The 7 Sovereign Attack Classes

Analyze the target scope across the relevant attack vectors:

### A. Injection & Dangerous Sinks
- **SQL / NoSQL / Command**: String concatenation into query runners, shells, or template engines.
- **Path Traversal**: File reads/writes using user-controlled filenames, zip-slip, or unvalidated symlinks.
- **SSRF**: Server-side requests fetching user-supplied URLs without private IP filtering (127.0.0.1, 169.254.169.254, RFC 1918).
- **Client DOM**: Unsanitized HTML insertion, prototype pollution, cross-window messaging (`postMessage` wildcard targets).

### B. Access Control & Authorization (IDOR)
- **Object-Level Gating**: Endpoints checking authentication but failing to verify that the authenticated user owns the accessed object ID.
- **Mass Assignment**: Direct binding of HTTP request bodies into ORM models allowing callers to elevate privileges (e.g. `is_admin: true`).
- **Inconsistent Auth Paths**: Secondary routes, webhooks, or batch endpoints that bypass middleware security checks.

### C. Concurrency & State Hazards (TOCTOU)
- **Check-Then-Act**: Time-of-check to time-of-use race conditions in file systems or databases without atomic transactions or row-level locks.
- **Distributed State Races**: In-memory rate limiters or mutexes running across multi-replica deployments.

### D. Cryptography, Tokens & Secrets
- **Broken Randomness**: Use of `Math.random()` or standard PRNGs instead of cryptographic CSPRNG for tokens, salts, or passwords.
- **Timing Side-Channels**: Non-constant-time comparison of HMACs, signatures, or passwords (`===` vs `crypto.timingSafeEqual`).
- **Secret Leaks**: Hardcoded API keys, bearer tokens in error responses, query strings, or verbose logs.

### E. AI & Agent Specific Vectors
- **Prompt Injection**: Untrusted user inputs directly interpolated into system prompts allowing directive override.
- **Tool Parameter Tampering**: Agent executing file/shell/network tools using unsanitized model completions.
- **Memory & State Poisoning**: Unverified third-party content written into persistent agent memory or RAG vector stores.

### F. Resource Exhaustion & Availability
- **ReDoS**: Catastrophic backtracking in regular expressions matched against user input.
- **Unbounded Buffers**: Memory, JSON, or file uploads parsed without explicit byte length boundaries.
- **Resource Leaks**: Missing `finally` blocks or context managers leading to leaked database connections or file descriptors.

### G. Supply Chain & Dependencies
- **Dependency Tampering**: Untrusted packages, typosquatting vectors, or build scripts with arbitrary remote code execution.

---

## 2. Finding Qualification Standard

A candidate finding is only reported if it satisfies all 3 criteria:
1. **Trust Boundary**: A specific boundary where untrusted input crosses into a trusted execution domain.
2. **Affected Asset**: A tangible asset (data disclosure, privilege escalation, remote code execution, financial manipulation).
3. **Exploitation Mechanism**: A clear sequence demonstrating how the vulnerability triggers under real-world input.

---

## 3. Zeus Shield Report Format

```markdown
# Zeus Shield Security Findings

### [CRITICAL / HIGH / MEDIUM / LOW] - <Title of Vulnerability>
- **Target**: `[path/to/file.ext#L10-L25](file:///path/to/file.ext)`
- **Attack Class**: [Injection | Access Control | TOCTOU | Crypto | AI Vector | Resource Exhaustion]
- **Trust Boundary**: [Where untrusted data enters and which sink receives it]
- **Mechanics of Exploit**: Concise description of how a hostile caller triggers the flaw.
- **Sovereign Remedy**: Minimal effective patch (the shortest diff that completely neutralizes the attack vector).
```

