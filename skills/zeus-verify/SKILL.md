---
name: zeus-verify
description: >
  Construct bulletproof invariant and boundary verification tests for critical functions.
  Tests adversarial inputs, empty states, concurrency, and error handling.
  Use for "verify this function", "write edge-case tests", "stress test", /zeus-verify.
argument-hint: "[file or function to verify]"
license: MIT
---

# Zeus Verify: The Aegis Invariant Suite

Produce high-leverage, deterministic tests designed to prove system correctness under stress and adversarial conditions.
Focus on boundary failure modes, state transitions, and edge cases rather than trivial happy-path coverage.

---

## 1. Verification Vectors

When tasked with verifying a component or function, generate tests covering:

1. **Boundary & Nil Conditions**:
   - Empty lists, null / nil / undefined inputs, zero numbers, maximum integer values, malformed UTF-8 strings.
2. **Adversarial & Fault Injection**:
   - Payloads with unexpected schemas, hostile input characters, path traversal attempts, SQL metacharacters.
   - Network simulation: simulated timeouts, partial reads, and transient HTTP errors.
3. **State & Concurrency Invariants**:
   - Rapid consecutive invocations, out-of-order execution, idempotency verification.
4. **Failure Propagation**:
   - Ensure exceptions are emitted with correct error types and actionable context rather than being masked.

---

## 2. Test Construction Guidelines

- **Zero Flakiness**: Tests must be 100% deterministic. Avoid non-deterministic `sleep()` calls; use explicit event synchronization or mocks.
- **Fast Execution**: Tests should execute in milliseconds using the project's native test runner (pytest, vitest, jest, cargo test, go test).
- **Self-Contained**: Do not require elaborate live databases or external network connectivity unless explicitly instructed.
- **Clear Assertions**: Assert specific properties and invariants rather than vague truthiness.
