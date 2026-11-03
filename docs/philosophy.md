# Design Principles of ZeusDeveloper

## Unnecessary code in AI generation
AI models reflect the code they were trained on, which often includes layers of boilerplate, speculative wrappers, and redundant dependencies:
- Classes wrapped around single functions.
- Configuration schemas for values that never change.
- New third-party packages installed for basic date formatting or string manipulation.

## Limits of passive or lazy prompts
Telling an AI agent to write as little code as possible solves one problem while introducing others:
1. **Unstructured growth**: Reluctance to create separate files can lead to large, tangled functions that mix data processing with I/O.
2. **Missing operational detail**: Overly terse code frequently drops input validation, structured error logs, and defensive boundary checks.
3. **Premature pushback**: Questioning every request wastes time when the user needs straightforward implementation.

## The Zeus approach
ZeusDeveloper aims for minimal changes without compromising structure:
- **Small diffs**: Modify only what the task requires, using the shortest readable logic.
- **Native runtime leverage**: Prefer standard libraries and existing codebase utilities over new packages.
- **Hardened boundaries**: Keep input checks, authorization guards, and error handling intact.
- **Maintainable separation**: Keep business logic separate from transport and storage layers so components remain easy to update or remove.
