<p align="center">
  <img src="assets/Capp_Zeus.png" width="260" alt="ZeusDeveloper Logo">
</p>

<h1 align="center">ZeusDeveloper</h1>

<p align="center">
  <em>Minimal code. Native runtime first. Cloud-grade security boundaries.</em>
</p>

<p align="center">
  <a href="README.md"><strong>English</strong></a> &middot;
  <a href="i18n/README.it.md">Italiano</a> &middot;
  <a href="i18n/README.es.md">Español</a> &middot;
  <a href="i18n/README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/release-v1.2.0-111827?style=flat-square" alt="Release">
  <img src="https://img.shields.io/badge/works%20with-20%2B%20agents-111827?style=flat-square" alt="Works with 20+ agents">
  <img src="https://img.shields.io/badge/license-MIT-111827?style=flat-square" alt="License">
</p>

---

## Benchmark Results

<p align="center">
  <img src="assets/chart-overview.svg" width="880" alt="ZeusDeveloper Benchmark Overview">
</p>

<p align="center">
  <img src="assets/chart-tests.svg" width="880" alt="ZeusDeveloper Reliability and Tests">
</p>

<p align="center">
  <img src="assets/chart-tiers.svg" width="880" alt="ZeusDeveloper Token Savings by Tier">
</p>

---

## Case Study: Before &amp; After

<p align="center">
  <img src="assets/chart-before-after.svg" width="880" alt="Before and After case study">
</p>

AI coding assistants tend to write too much ceremony:
- You ask for a rate limiter, and they install third-party middleware with multiple configuration files.
- You ask for a bugfix, and they introduce multiple wrapper classes and interfaces.
- They spend tokens on greetings, apologies, and conversational filler before showing code.

ZeusDeveloper keeps diffs small while maintaining clean module boundaries, native standard library usage, and strict input checks.

---

## Core Guidelines

1. **Smallest working change**: Solve the requirement with minimal edits to existing code. Avoid speculative parameters, extra config flags, or wrapper utilities nobody asked for.
2. **Native standard library first**: Use built-in runtime features and existing repository utilities before adding any dependency.
3. **Hardened trust boundaries**: Never skip input sanitization, error propagation, or auth checks. Treat all external input (HTTP, CLI, RPC, AI outputs) as untrusted.
4. **Direct answers**: Lead with the concrete change (`[Target] [Action] [Reason]`) and the diff. Cut conversational preamble and pleasantries.
5. **Clean separation**: Avoid god-functions. Keep domain rules separate from network and I/O logic.
6. **Invariant checks**: Accompany non-trivial state changes, parsers, or calculations with a focused unit or boundary test.

---

## Operating Tiers

You can adjust the prompt intensity depending on the task:

| Tier | Command | Usage |
| :--- | :--- | :--- |
| **Hermes** | `/zeus hermes` | Fast, direct bugfixes with minimal friction. Mentions any deferred debt in one line. |
| **Zeus** | `/zeus` | Default mode. Enforces minimal diffs, native APIs, and boundary checks. |
| **Titan** | `/zeus titan` | Questions flawed assumptions or bloated requirements before writing code. |
| **Oracle** | `/zeus oracle` | High-density responses. Cuts all non-essential prose for maximum token efficiency (-78%). |

---

## Included Skills

* **`/zeus`**: Main mode and tier switching.
* **`/zeus-shield`**: Security review across 7 attack classes (Injection, IDOR, TOCTOU, Crypto, AI vectors, Resource limits, Supply chain).
* **`/zeus-strike`**: Surgical refactoring to remove dead code, unnecessary wrappers, and redundant packages.
* **`/zeus-audit`**: Codebase audit for concurrency bugs, performance bottlenecks, and architectural bloat.
* **`/zeus-verify`**: Generates deterministic unit and boundary tests for critical logic.
* **`/zeus-debt`**: Scans for `// zeus-debt:` and `TODO:` tags to compile a debt ledger.
* **`/zeus-help`**: Quick reference guide.

---

## Local Monitoring Board

ZeusDeveloper includes a standalone dashboard to monitor agent sessions, token savings, and test coverage:

```bash
python board.py
```

Opens a local dashboard on `http://localhost:3000` with session breakdowns and metrics.

---

## Installation

### Any AI Tool (Universal)
Download [`AGENTS.md`](AGENTS.md) into your project root:
```bash
curl -o AGENTS.md https://raw.githubusercontent.com/24Capp/ZeusDeveloper/main/AGENTS.md
```
Antigravity, Cursor, Windsurf, OpenCode, Devin, Aider, and Claude Code automatically read project rules from `AGENTS.md`.

### Antigravity & Gemini CLI
```bash
agy plugin install https://github.com/24Capp/ZeusDeveloper
```

### Claude Code
```text
/plugin marketplace add 24Capp/ZeusDeveloper
/plugin install zeus@zeus
```

See [INSTALL.md](INSTALL.md) for Cursor, Windsurf, Copilot, OpenCode, and Hermes.

---

## License
MIT © 2026 Luca Quagliozzi (24Capp)
