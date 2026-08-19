# ATS (Applicant Tracking System) Compatibility — Reference

Many medium-to-large Danish employers use ATS software (Workday, Greenhouse, Lever, HR-Skyen, HR-On, Emply, Talentech, etc.) to parse CVs into structured fields before a human ever sees them. A poorly parseable CV gets dropped or scored low even if the content is strong.

## Format checklist

Run through these against the CV:

### Section headings
Use standard, recognizable headings. ATS look for these as anchors.

| Standard EN | Standard DA | Avoid |
|-------------|-------------|-------|
| Experience / Work Experience / Professional Experience | Erfaring / Erhvervserfaring | "Where I've been", "My journey" |
| Education | Uddannelse | "Schools" |
| Skills | Kompetencer / Færdigheder | "What I do well" |
| Certifications | Certifikater | "Wall of fame" |
| Languages | Sprog | (just don't be cute) |
| Summary / Profile | Profil / Kort om mig | "About me" is OK |

### Dates
- [ ] Consistent format throughout: `2022–Present`, `Jan 2020 – Dec 2022`, `2018-2021`. Don't mix `2020` with `January 2020` with `01/2020`.
- [ ] Use real hyphens or en-dashes; avoid weird Unicode separators.
- [ ] In Danish: `2020-2023` or `jan. 2020 – dec. 2022` is fine; avoid mixing.

### Contact information
- [ ] Full name, phone (with country code +45 for DK), email, city (or city + country), LinkedIn URL.
- [ ] Photo is fine for DK CVs but should be embedded as image *outside* the parsing-critical area (top-right corner is typical).
- [ ] Plain text email — no fancy formatting, no email-as-image.

### File format
- **PDF (text-based)** — best, as long as it's not a scanned image. Test: can you select and copy text from the PDF? If yes, parseable.
- **DOCX** — also good, sometimes preferred by older ATS.
- **TEX / LaTeX source** — never submit. Submit the rendered PDF.
- **Scanned PDF / image** — bad. Always use the text-based version.

### Filename
- [ ] Format: `Firstname_Lastname_CV.pdf` or `Firstname_Lastname_CV_CompanyName.pdf`.
- [ ] No spaces if possible (use underscores), no special characters, no Danish letters in filenames if international ATS.

## Keyword matching

ATS rank applications by keyword overlap with the job posting. If a posting was provided, do this:

1. Extract the top 8–12 hard skills, tools, and qualifications from the posting (e.g., "Python", "GDPR", "stakeholder management", "Pharma", "B2B SaaS", "MSc", "5+ years", "Danish C1").
2. Search the CV for each. Note presence (verbatim or near-match) or absence.
3. Recommend incorporating missing keywords *if they're true of the candidate* — never invent. Suggest natural placements (skills section, role bullet, or summary).

A good fit hits 60–80% of the keywords; below 40% the CV will likely score low regardless of quality.

## Cover letter ATS

Cover letters are parsed less aggressively than CVs, but the same principles apply:
- Plain text body, single column.
- Address block at top.
- No text-in-image elements.

## Special considerations for awesome-cv / LaTeX-rendered CVs

The `awesome-cv` LaTeX template (and similar) produces beautiful CVs but can have ATS pitfalls:
- Font rendering may embed glyphs as paths, not text — check by selecting and copying text.
- Sidebar/timeline visualizations can confuse parsers.
- Custom heading styles may not match standard "Experience"/"Education" anchors — check that the underlying text is still standard words.

If the candidate uses awesome-cv or similar: confirm that copy-paste from the rendered PDF gives clean, ordered text. If not, suggest a plainer template for ATS-heavy applications.

## Summary advice for the report

Always include in the ATS section:
1. Single line on overall parseability ("Likely parses well" / "Some risk" / "Significant risk").
2. If a posting was provided: list of matched keywords and missing keywords.
3. One-line recommendation if any major issues found.
