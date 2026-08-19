---
name: cv-coverletter-evaluator
description: >
  Evaluate a CV and/or cover letter from three independent perspectives — hiring manager, Danish job-market
  expert, language/AI-tells reviewer — and deliver a structured Markdown report with pros, cons,
  prioritized recommendations, a success-potential rating, and a brainstorming kickoff. Trigger when the
  user asks to review, critique, evaluate, score, or improve a CV, resume, cover letter, or full
  application — or shares one and asks "is this any good?", "fit for the Danish market?", "any AI tells?"
---

# CV & Cover Letter Evaluator

The stakes are real: a good evaluation can change an outcome. Take the work seriously.

## Integration with job-application skill

**Default trigger:** Run automatically after `job-application` step 7 (pre-send checklist), unless the user explicitly skips review.

When running in the Awesome-eik repo:

- Find CV source at `examples/Rades_CV_<Company>_<Language>.tex` (or compiled `.pdf`) on the current company branch
- Find cover letter at `examples/Rades_CoverLetter_<Company>_<Language>.tex`
- Use `jobdescription.txt` as the job posting
- Use `application_checklist.md` as the formatting and content rules reference — flag violations

If the user provides files or pasted text directly, use those instead.

## Inputs

**Required (at least one):** CV and/or cover letter — as files (`.pdf`, `.tex`, `.md`, `.txt`), pasted text, or a URL. If only one document is provided, evaluate what's there and note what's missing.

If the user pastes a mixed blob, segment by content: bullet-heavy reverse-chronological → CV; flowing paragraphs addressed to a person → cover letter; "We are looking for" / "Ansvarsområder" → job posting. Ask one focused question only if genuinely ambiguous.

**Optional:** Job posting (file, pasted text, or `jobdescription.txt`). If present, anchor the evaluation to it.

## Workflow

Read everything before writing anything.

1. Read all inputs. Detect language per document (Danish or English).
2. Run the three perspectives independently — do not blend findings until synthesis.
3. Run cross-cutting checks.
4. Synthesize into the report.
5. Save or present the report (see Output below).

---

## 1. Three perspectives

Run each independently. The value is that different lenses catch different things.

### Perspective A — Hiring manager

Read as a busy hiring manager from the respective company: 30 seconds for the cover letter, 60 for the CV, then decide interview / pass / maybe.
- Can I understand what he claims to have achieved?
- Does the opening sentence make me want to keep reading, or could it have been written about anyone?
- In the first 5 seconds of the CV, can I tell what this person does and what level they're at?
- Are achievements concrete and quantified, or vague ("responsible for", "involved in", "helped with")?
- Is there a clear value proposition — what does this person bring that the next applicant doesn't?
- Are claims credible, or inflated?
- Would I want to meet this person? Why or why not?
- If changing fields, is the pivot clearly motivated and transferable skills made obvious?

Write 4–8 specific bullet findings.

### Perspective B — Danish job-market expert

- **Format & length:** CV 1–2 pages; cover letter 1 page (3–5 paragraphs). Flag bloat.
- **Personal info:** photo + date of birth are still common in DK (unlike US/UK). Note presence/absence neutrally.
- **Tone:** flat hierarchy, directness, humility — candidate as colleague, not superstar. Flag American-style superlatives ("world-class", "rockstar", "passionate game-changer").
- **Salutation:** "Kære [Navn]" when known; "Kære rekrutteringsansvarlig" if not. Sign-off: "Med venlig hilsen" / "Bedste hilsner".
- **Language fit:** if the role is Danish-speaking and the application is in English (or vice versa), flag it — major signal.
- **Structure:** profile/summary → experience (reverse chronological) → education → skills → languages → hobbies. Flag missing or out-of-order sections.
- **Personlighed paragraph:** many Danish cover letters expect a brief personal-character paragraph. Note if present and whether it lands.
- **Self-promotion calibration:** slightly understated confidence > loud confidence. Public sector → societal impact framing; private sector → business outcomes.

Write 4–8 specific bullet findings.

### Perspective C — Language & AI-tells

**Mechanics:** spelling errors (quote the wrong word + correction), grammar issues, punctuation, capitalization (Danish capitalizes nouns far less than German), date/number formatting consistency.

**AI-tells** — flag concentration, not isolated cases:
- Em dashes used stylistically and repeatedly (— like this —)
- "Not just X, but Y" rhetorical patterns; tricolons
- Words/phrases: "leverage", "navigate", "ensure", "passionate", "delve", "robust", "comprehensive", "tapestry", "bridge the gap", "synergy", "in today's fast-paced world"
- Generic openers: "I am writing to express my interest in…"
- Overly perfect parallel bullet structures
- Hedge + abstract claim combinations: "various", "numerous", "a range of" instead of specifics

Write 4–8 findings with quoted text where applicable.

---

## 2. Cross-cutting checks

### ATS compatibility

- No tables/multi-column layouts holding key info; no images for text; contact info in the body not a header image
- Standard section headings ("Experience" / "Erfaring", "Education" / "Uddannelse", "Skills" / "Kompetencer")
- Dates in consistent parseable format; file format is `.pdf` (text-based) or `.docx`
- If a job posting was provided: list 5–10 keywords from it and note which appear in the CV — missing keywords are a real ATS risk

### Consistency: CV ↔ Cover letter

- Dates, titles, and employer names match exactly
- Cover letter claims are backed by CV entries ("led a team of 8" → CV reflects it)
- Tone and register match
- Cover letter curates the most relevant CV experiences and explains *why this role* — the CV is the catalog, the cover letter is the argument

### Red flags & quantification

- **Employment gaps:** note any gap > 4 months. If the cover letter doesn't address it, recommend a one-line framing.
- **Frequent moves:** multiple jobs each < 12 months — worth pre-empting.
- **Quantification:** for each role, count bullets with a number (people, %, currency, time, scale). Goal: at least 1–2 per role. Flag roles with zero.
- **Vague verbs:** "responsible for", "involved in", "helped with", "assisted in" — suggest stronger replacements ("led", "shipped", "owned", "delivered", "reduced X by Y%").

---

## 3. Report

Produce one Markdown report with exactly this structure. If a section has nothing to flag, write "No issues identified." — do not drop the heading.

```
# CV & Cover Letter Evaluation — [Candidate Name] / [Target Role or "Generic"]

**Date:** YYYY-MM-DD
**Documents reviewed:** [list]
**Job posting:** [filename / "Not provided"]
**Languages detected:** [CV: DA/EN, Cover letter: DA/EN]

## Executive summary
2–4 sentences. Lead with the headline finding.

## Success-potential rating
Strong / Solid / Mixed / Weak — one sentence justification.
If a job posting was provided: fit score (e.g. "7/10") with reasoning.

## Pros — what's working
4–8 specific bullets.

## Cons — what's holding it back
4–8 specific bullets.

## Perspective A — Hiring manager
4–8 bullets.

## Perspective B — Danish job market
4–8 bullets.

## Perspective C — Language & AI-tells
4–8 bullets with quoted text.

## Cross-cutting checks
### ATS compatibility
### Consistency CV ↔ Cover letter
### Red flags & quantification

## Recommendations — prioritized
1. **[Critical]** Highest-impact fixes first — what to change, why, concrete rewrite where possible.
2. **[Important]** Medium-impact.
3. **[Polish]** Nice-to-haves.

## Brainstorming kickoff
3–5 open questions designed to surface things the candidate hasn't thought to put on the page.
End by inviting the user to pick one or two to dig into next.
```

---

## Output

- **In the Awesome-eik repo:** save report as `examples/evaluation_<Company>_<YYYY-MM-DD>.md` on the current branch. Print the path.
- **Otherwise:** render the full report inline in chat.

Either way: lead the conversational response with the headline finding and success-potential rating in 2–3 sentences, then point to the file or note the report is below.

## Rules

- Write to the candidate in second person ("you"), not about them.
- Be direct and specific. "Bullet 3 in role 2 has no number" is useful. "Add more numbers" is not.
- Quote actual text when flagging something — vague feedback can't be acted on.
- Don't rewrite the entire CV unless asked. Evaluation first; rewrites are a separate request.
- Don't moralize about AI use — flag concentration of tells, not isolated cases.
- Don't refuse to evaluate due to missing context — evaluate generically and note where role context would help.
