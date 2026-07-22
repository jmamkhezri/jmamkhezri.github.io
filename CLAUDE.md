# CLAUDE.md — jmamkhezri.github.io

Personal website of Jamal Mamkhezri, Professor of Economics at New Mexico State University. Static site served by GitHub Pages from the `main` branch; pushing to `main` publishes the live site immediately, so confirm content is ready before pushing.

NOTE: this repository is PUBLIC. Never put private information in it, including in this file: no client names, case or docket numbers, contract details, billing rates, or phone numbers.

## Structure and conventions

- Five standalone pages: `index.html`, `publications.html`, `projects.html`, `teaching.html`, `cv.html`. No build step, no shared templates or includes.
- Each page carries its own complete `<style>` block. Shared look: CSS custom properties (`--primary` navy, `--accent` burnt orange), Playfair Display for headings, Source Sans 3 for body.
- The nav is hardcoded separately in all five files; any nav change must be repeated in every file. Subpages prefix in-page anchors with `index.html` (e.g., `index.html#consulting`); index.html uses bare hashes (`#consulting`).
- `index.html` sections are numbered 01–06: Research Interests, Selected Publications, Current Funded Projects, Consulting, About, Contact. The numbers are hardcoded strings, so inserting a section means renumbering everything after it.
- Reusable patterns on index.html: `.section-container`/`.section-header` for section shells, `.research-grid`/`.research-card` for card grids, `.publications-list`/`.pub-item` for list rows, `.view-all-link` for primary pill buttons, `.hero-link` for secondary buttons.

## Writing style (owner preference)

- Never use em dashes anywhere in site prose; use commas, semicolons, colons, parentheses, or split the sentence.
- Site copy should read as flowing sentences, not bullet fragments, except inside card/list UI patterns.

## Consulting section (added July 2026)

- Section 04 on `index.html` presents Mamkhezri Consulting LLC (Las Cruces, NM): a credentials intro, two service cards (Energy & Utility Regulation; Litigation Support & Economic Damages), and a CTA row (mailto button plus `Mamkhezri_Consulting_Resume.pdf`).
- Consulting is also surfaced in the hero (a Consulting position line and a hero-link button, both anchored to `#consulting`) and as a nav item on all five pages.
- Contact identities are deliberately separate: `jmamkhezri@gmail.com` for consulting, `jamalm@nmsu.edu` (Contact section) for academic matters. Jamal's cell number is intentionally kept off the site and out of the hosted resume PDF.
- `Mamkhezri_Consulting_Resume.pdf` is compiled from the resume `.tex` kept in Jamal's OneDrive CONSULTING folder, with the phone number line removed for the web copy. To update it, recompile from the current `.tex` (pdflatex, then delete build byproducts) and overwrite the PDF here.
- Engagement publishing policy: the site describes consulting work generically (venues and subject matter only). Specific clients, cases, and docket numbers are added only when they are public record AND Jamal explicitly approves. As of July 2026 no engagement specifics appear because active matters are still pending. The planned format for later is a "Representative engagements" list inside the consulting section, and possibly a dedicated `consulting.html` page once there is enough public material (filed testimony, client list) to fill one.
- Detailed engagement notes live locally in Jamal's OneDrive CONSULTING folder, not in this repo. Do not copy from there into this repo without checking sensitivity.

## Other notes

- Jamal returned to NMSU (College of Business, Room BC 338) in summer 2026 after a 2025–2026 sabbatical at Georgia Tech's EPIcenter; the site should not describe Georgia Tech as a current affiliation.
- Promotion to Full Professor is effective August 2026; the hero currently says "Professor (effective Aug. 2026)". After that date the qualifier can be dropped site-wide.
- Design reference consulted for the consulting section: tahoeconomics.com (a colleague's consulting site). The takeaways adopted were content ideas (credibility bio, clear CTA, eventually a client/engagement list), not its design.
