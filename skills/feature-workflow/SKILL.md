---
name: feature-workflow
description: >
  Take a feature from idea or roadmap item to committed, tested code: scan, requirements, branch,
  phased TDD, PR. Use when the user wants to build or start a feature, asks what's next on the
  roadmap, needs a feature branch, or mentions TDD or /tdd.
---

# Feature Workflow

idea → scan → requirements → branch → phased plan → TDD loop → commit → PR

## 1. What to Build

Roadmap file (`ROADMAP.md`, `TODO.md`, `docs/roadmap.md`) → show next uncompleted item, confirm.
User described it → use that. Neither → ask.

## 2. Scan First

Never plan without reading the code.

**Conventions** — `CLAUDE.md`, `.cursorrules`, `CONVENTIONS.md`, `CONTRIBUTING.md`, README arch sections. Extract naming, folders, test framework, import style, linting. These are law.

**Structure** — `find . -type f | grep -vE 'node_modules|\.git|dist' | head -80`

**Affected modules** — read the files this feature touches. Note public interfaces at risk, shared utilities, established patterns (errors, data fetching, test structure). Pick up the codebase's domain language — tests get named in it.

**Baseline** — run the suite. Red baseline → stop, report, fix before anything else.

Report back: conventions, affected modules, baseline status.

## 3. Requirements

One message, everything at once. Skip what the scan already answered.

- **Scope** — does / doesn't do, acceptance criteria, non-goals
- **Seams** — which public boundaries does this feature expose? Name them explicitly and confirm. Tests live here and nowhere else; this is what keeps the suite from sprawling into every edge case.
- **Data** — input/output shapes with example values, API contracts, existing structures touched
- **Edges** — invalid input, failure modes, races, retry/fallback
- **Integration** — interface changes, new dependencies
- **Constraints** — latency/memory/platform, auth/permissions/sanitisation

Wait for answers.

## 4. Branch

Propose the name, then `git checkout -b feature/<short-kebab-description>`

## 5. Phased Plan

Distinct phases, real file paths from the scan, one flag each:

🟢 new/isolated · 🟡 touches shared logic · 🔴 changes public interfaces or shared state

```
Phase N: <title> 🟢/🟡/🔴
  Builds: <what>
  Files: <paths>
  Depends on: <phases/modules>
  Commit: "feat(<scope>): <description>"
```

Confirm before starting.

## 6. TDD Loop — per phase

**Red** — one seam, one test. Name it as a capability in domain language ("user can checkout with valid cart"), not as a mechanism. Assert on behaviour observable at the seam, never on internals. Run it, show the failure.

**Green** — minimum code to pass. Project conventions. Run, confirm green. No speculative generality.

**Refactor** — clarity, naming, duplication. 🔴 phases: verify callers and interface compatibility. Tests stay green.

**Commit**
```bash
git add -A && git commit -m "feat(<scope>): <description>"
# 🟡/🔴 also get a body: why this approach, alternatives, known gaps
```
Prefixes: `feat` `fix` `refactor` `test` `chore`

**Report** — `✅ Phase N done — <what changed>. Remaining: X, Y, Z.`

### Reject these tests
- **Implementation-coupled** — mocking internals, asserting on private methods. Breaks on every refactor, proves nothing.
- **Tautological** — expected value recomputed the way the code computes it. Passes even when the logic is wrong.
- **Horizontally sliced** — all tests written up front, then all code. Go vertical: one seam through to green, then let what you learned shape the next.

## 7. Wrap-Up

```bash
git diff main --unified=0 | grep -E '^\+.*(TODO|FIXME|HACK|XXX)'
git log main..HEAD --oneline
```
Surface TODOs — resolve or track deliberately. Draft the PR: what & why, key decisions, phases, testing, known gaps. Show the next roadmap item.

## Principles

- Read before planning.
- Never build on a red suite.
- Red → Green → Refactor. No implementation before a failing test.
- Test at seams, through public interfaces. A good test reads like a specification and survives refactoring.
- Each cycle is a tracer bullet — it responds to what the last one revealed.
- One phase = one commit. Bisectable history.
- Conventions are law.
- 
