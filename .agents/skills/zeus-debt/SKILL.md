---
name: zeus-debt
description: >
  Scan the workspace for tagged architectural debt, temporary compromises, and `zeus-debt:` annotations.
  Outputs a prioritized ledger with recommended actions and upgrade triggers.
  Use for "list technical debt", "zeus debt", "what did we defer", /zeus-debt.
argument-hint: "[optional path]"
license: MIT
---

# Zeus Debt: Technical Debt & Shortcut Ledger

Scan the codebase to enumerate all acknowledged technical debt, deliberate compromises, and deferred optimizations.
Provides an unvarnished audit of where future maintenance liabilities reside.

---

## 1. Detection Protocol

Search the codebase across standard debt comment tags:
- `// zeus-debt:` or `# zeus-debt:`
- `// shortcut:` or `# shortcut:`
- `TODO:`, `FIXME:`, `HACK:`, `XXX:`

---

## 2. Output Ledger Format

Output a markdown table grouping findings by urgency:

```markdown
# Zeus Technical Debt Ledger

| Location | Tag Type | Stated Rationale & Limit | Upgrade Trigger |
| :--- | :--- | :--- | :--- |
| `src/auth.ts:42` | `zeus-debt` | In-memory token store used for MVP | When horizontal scaling > 1 node |
| `src/parser.py:118` | `TODO` | Recursive parser lacks depth guard | Input payload > 100KB |

### Next Actions
1. **Immediate Risk**: Debt items that threaten security or data integrity under production load.
2. **Acceptable Deferred**: Items safe to leave intact until business scale demands upgrade.
```
