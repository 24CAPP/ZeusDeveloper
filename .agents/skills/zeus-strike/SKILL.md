---
name: zeus-strike
description: >
  Surgically strip bloat, collapse convoluted abstraction layers, remove redundant dependencies,
  and refactor complex functions into clean, high-performance native code.
  Use for "refactor this", "clean up this mess", "remove bloat", "simplify", /zeus-strike.
argument-hint: "[target file or function]"
license: MIT
---

# Zeus Strike: Bloat & Complexity Eradication

Execute a surgical strike against bloated, over-engineered, or convoluted code.
The objective is to maximize readability, maintainability, and runtime performance while reducing total surface area.

---

## 1. Strike Assessment

Before modifying the target code, perform a rapid triaging pass:

1. **Dead Weight Scan**: Identify unused variables, dead methods, redundant helper abstractions, and unused imports.
2. **Layer Collapse**: Identify wrapper classes that do nothing except forward calls. Flatten unnecessary indirection.
3. **Dependency Purge**: Detect third-party libraries imported for single-line operations (e.g. left-pad, is-even, lodash for native array methods). Replace with standard language primitives.
4. **God Function Decoupling**: Where sprawling multi-hundred-line functions exist, isolate the core domain calculation from external I/O without introducing ceremonial design patterns.

---

## 2. Refactoring Protocol

1. **Safety First**: Verify that existing tests pass or establish an initial invariant benchmark before altering code.
2. **Collapse from the Inside**: Replace convoluted loops, nested callbacks, and redundant state machines with idiomatic language constructs (comprehensions, native stream/map/filter, pattern matching, async/await).
3. **Preserve Trust Boundaries**: Retain all existing security checks, input sanitization, error propagation, and edge-case handling.
4. **Unified Diff**: Deliver the refactored code in the most direct, readable diff possible.

---

## 3. Strike Report Format

Present the refactoring results concisely:

```markdown
### Zeus Strike Summary
- **Lines Eliminated**: X lines removed (-Y%)
- **Dependencies Purged**: [List of packages eliminated, or "None"]
- **Abstractions Collapsed**: [Summary of flattened layers]
- **Invariant Preserved**: [Explanation of how safety & correctness was verified]
```
