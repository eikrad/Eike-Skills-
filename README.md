# Agent Skills

Self-built, opinionated skills for AI coding agents — a TDD feature workflow, a Socratic design interviewer, and a three-lens CV reviewer.

[![Validate Skills](https://github.com/eikrad/Eike-Skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/eikrad/Eike-Skills/actions/workflows/validate-skills.yml)
[![Skills](https://img.shields.io/badge/skills-3-3d8c40)](#the-skills)
[![License](https://img.shields.io/badge/license-Apache_2.0-blue)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/eikrad/Eike-Skills)](https://github.com/eikrad/Eike-Skills/commits)

A **skill** is a folder with a `SKILL.md` inside: YAML frontmatter that tells an agent *when* to reach for it, and Markdown that tells it *how* to do the work. Nothing is compiled, nothing is installed — it is plain text an agent reads at the moment it becomes relevant.

Everything here is written from scratch for my own daily work, then sharpened through use. No forks of the skills that ship with an agent. The format is deliberately vendor-neutral: these were built and tested in Claude Code, but any agent that can load a skill directory can read them as-is.

## The skills

| Skill | What it does | Reaches for it when |
| --- | --- | --- |
| [**feature-workflow**](skills/feature-workflow/SKILL.md) | Drives a feature from idea to committed, tested code through a strict red-green-refactor loop | You want to build a feature, ask what's next on the roadmap, need a feature branch, or say TDD |
| [**socratic-interviewer**](skills/socratic-interviewer/SKILL.md) | Interviews you about a design decision without ever offering an opinion, then writes up a design brief | You're wrestling with an architecture or UX question and haven't reached an answer yet |
| [**cv-coverletter-evaluator**](skills/cv-coverletter-evaluator/SKILL.md) | Reviews a CV and cover letter through three independent lenses and returns a prioritized report | You want an application critiqued, scored, or checked for AI tells |

### feature-workflow

`idea → scan → requirements → branch → phased plan → TDD loop → commit → PR`

The scan comes first and is not optional: conventions files are treated as law, the affected modules get read before anything is planned, and a red test suite stops the workflow before a line is written. The plan is then broken into phases flagged 🟢 isolated / 🟡 shared logic / 🔴 public interface, one commit per phase, so the history stays bisectable.

Its sharpest rule is about tests: they live at seams and go through public interfaces. A test that reaches into private state or pins an implementation detail gets rejected rather than written — which is what keeps a suite from sprawling as the feature grows.

### socratic-interviewer

An interview, not a consultation. One reflection sentence and one question per turn, cycling through six question types — clarification, assumptions, evidence, perspectives, implications, and the question behind the question. The agent holds back opinions completely: no suggesting, no evaluating, not even an encouraging "great point," since praise steers as effectively as advice does.

When your thinking stabilizes, it offers to close and produces a **Design Brief**: the problem, the decision reached, the assumptions it rests on, the tensions left open, and the next steps — grounded strictly in what you actually said.

### cv-coverletter-evaluator

Three lenses, run independently so they don't blur into each other: a **hiring manager** reading for signal, a **Danish job-market expert** reading for local convention, and a **language reviewer** reading for AI tells. On top come cross-cutting checks for ATS compatibility, CV ↔ cover letter consistency, and unquantified claims.

The output is a full Markdown report — executive summary, success-potential rating, pros and cons, per-perspective findings, recommendations tiered Critical / Important / Polish, and a set of open questions to surface what you haven't thought to put on the page. Feedback is quoted and specific, because "add more numbers" cannot be acted on and "bullet 3 in role 2 has no number" can.

## Install

Skills are just directories. Put them where your agent looks for them.

**Claude Code — all projects**

```bash
git clone https://github.com/eikrad/Eike-Skills.git /tmp/eike-skills
cp -r /tmp/eike-skills/skills/* ~/.claude/skills/
```

**Claude Code — one project**

```bash
mkdir -p .claude/skills
cp -r /tmp/eike-skills/skills/feature-workflow .claude/skills/
```

**Any other agent** — copy the skill folder into whatever directory your agent scans, or point it at the `SKILL.md` directly. There is no runtime, no dependency, and no lock-in: the file is the whole skill.

Restart your agent session afterwards so the new skills are picked up, then confirm the agent lists them.

## Writing your own

A skill is one folder, one `SKILL.md`, and frontmatter with two required keys:

```markdown
---
name: my-skill
description: >
  What the skill does, then the phrases and situations that should trigger it.
---

# My Skill

Instructions for the agent, in Markdown.
```

`name` must match the folder name and use `lowercase-hyphenated` words. `description` is the only part an agent reads before deciding whether to load the skill, so it carries the entire triggering burden — say what the skill does *and* name the situations and phrasings that should pull it in. Keep it under 1024 characters.

Then write the body for an agent, not for a human reader: concrete steps, real commands, explicit rules about what not to do. Skip the motivational framing and the background explanation. Anything the agent cannot act on is context it has to carry for nothing.

## Validation

Every push runs [`scripts/validate_skills.py`](scripts/validate_skills.py), which checks that each skill parses, that `name` matches its directory, that `description` exists and fits the limit, that relative links resolve, and that the README table above hasn't fallen out of sync with `skills/`.

```bash
pip install pyyaml
python3 scripts/validate_skills.py
```

## Contributing

Issues and pull requests are welcome — especially reports of a skill triggering when it shouldn't, or failing to trigger when it should, since that feedback is hard to get any other way. For a new skill, run the validator before opening the PR and add a row to the table above.

## License

[Apache 2.0](LICENSE)
