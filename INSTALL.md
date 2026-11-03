# ZeusDeveloper Installation Guide

ZeusDeveloper is designed for seamless portability across all leading AI coding assistants. Choose your platform below.

---

## 1. Antigravity & Google Gemini CLI

### Direct Workspace Installation (Recommended)
Copy `AGENTS.md` to your project root. Antigravity automatically detects and enforces it across all sessions.
For slash-command support, clone or copy the `skills/` directory into your project's `.agents/skills/`.

### CLI Extension
```bash
agy plugin install https://github.com/24Capp/ZeusDeveloper
# or for Gemini CLI
gemini extensions install https://github.com/24Capp/ZeusDeveloper
```

---

## 2. Claude Code

Install directly via the marketplace command:

```text
/plugin marketplace add 24Capp/ZeusDeveloper
/plugin install zeus@zeus
```

Switch operating tiers anytime in chat:
```text
/zeus titan
/zeus hermes
/zeus
```

---

## 3. Cursor & Windsurf

### Cursor
Add `.cursor/rules/zeus.mdc` to your workspace, or copy `AGENTS.md` directly into your project root. Cursor automatically includes project-level rules in agent context.

### Windsurf
Copy `AGENTS.md` to the workspace root or add `.windsurf/rules/zeus.md`.

---

## 4. OpenCode & Kilo

Add ZeusDeveloper to your project's `opencode.json`:

```json
{
  "plugins": ["@zeusdeveloper/zeus"]
}
```

Or from a local clone:
```json
{
  "plugins": ["./skills"]
}
```

---

## 5. Codex & Copilot CLI

```bash
codex plugin marketplace add 24Capp/ZeusDeveloper
codex plugin add zeus@zeus
```

For GitHub Copilot CLI:
```bash
copilot plugin marketplace add 24Capp/ZeusDeveloper
copilot plugin install zeus@zeus
```

---

## Universal Fallback (Any AI Agent)

Any agent that respects standard workspace rules (Aider, CodeWhale, Devin, Cline, Roo Code, Hermes) automatically picks up `AGENTS.md` from the project root with **zero installation needed**.
Just drop `AGENTS.md` into the root of your repository.
