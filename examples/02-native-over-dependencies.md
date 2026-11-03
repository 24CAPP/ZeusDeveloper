# Example 2: Native Runtime Sovereignty vs Dependency Bloat

## Task
Parse an ISO timestamp, format it into an internationalized human-readable format, and calculate time elapsed.

---

### Without ZeusDeveloper
The agent installs `moment`, `moment-timezone`, or `date-fns` (adding thousands of transitively installed files to `node_modules`), writes custom wrappers around them, and exports a helper class with 8 unused utility methods.

---

### With ZeusDeveloper
Zeus uses the native `Intl.DateTimeFormat` and standard `Date` math available in all modern browsers and Node/Deno/Bun runtimes:

```typescript
export function formatElapsed(timestamp: string, locale = 'en-US'): string {
  const date = new Date(timestamp);
  if (Number.isNaN(date.getTime())) throw new RangeError(`Invalid timestamp: ${timestamp}`);
  
  const diffSec = Math.round((Date.now() - date.getTime()) / 1000);
  const rtf = new Intl.RelativeTimeFormat(locale, { numeric: 'auto' });
  
  if (Math.abs(diffSec) < 60) return rtf.format(-diffSec, 'seconds');
  if (Math.abs(diffSec) < 3600) return rtf.format(-Math.round(diffSec / 60), 'minutes');
  return new Intl.DateTimeFormat(locale, { dateStyle: 'medium', timeStyle: 'short' }).format(date);
}
```

- **Dependencies**: 0
- **Bundle size overhead**: 0 KB
- **Security Audit Vulnerabilities**: 0
