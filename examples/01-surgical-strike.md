# Example 1: Surgical Strike vs Bloated Scaffolding

## Task
Add an API rate-limiter check per user ID for a web route handling sensitive actions.

---

### Without ZeusDeveloper (Standard AI Agent)
The agent installs an external Redis middleware library, configures a factory abstraction, creates an interface `IRateLimiterStrategy`, adds 4 configuration files, introduces asynchronous connection pooling wrappers, and modifies 9 files across the repository.
- **Lines Added**: +340 lines
- **Dependencies Added**: +2 packages (`ioredis`, `express-rate-limit`)
- **Risk**: New failure points, latency overhead, extra environment variables to manage.

---

### With ZeusDeveloper (The Lightning Strike)
Zeus recognizes the application already runs behind a reverse proxy (or has a fast local cache / token bucket primitive in stdlib). It writes a 12-line in-memory token bucket directly in the route handler middleware, bounded to prevent memory growth, and adds a test for the 429 status code.

```typescript
// Bounded in-memory sliding window rate limiter
const hits = new Map<string, { count: number; resetAt: number }>();

export function rateLimit(userId: string, limit = 10, windowMs = 60_000): boolean {
  const now = Date.now();
  const record = hits.get(userId);
  if (!record || now > record.resetAt) {
    hits.set(userId, { count: 1, resetAt: now + windowMs });
    return true;
  }
  if (record.count >= limit) return false;
  record.count++;
  return true;
}
```

- **Lines Added**: +14 lines
- **Dependencies Added**: 0
- **Operational Edge**: Bounded memory map; suitable for single-node / container replicas.
- **Result**: Done in seconds, zero new runtime dependencies, easily replaceable when enterprise multi-node syncing is explicitly requested.
