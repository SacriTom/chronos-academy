# Chronos Academy — Project State

## Vision
A fictitious time-travel university where students enroll to learn by traveling to historical periods. Historical figures serve as professors, campuses exist across multiple eras, and the curriculum spans all of human history. Built using Octopus multi-agent orchestration.

## Project Goals
1. **Worldbuilding**: Rich lore — university charter, era-based campuses, faculty, courses, student life
2. **Website**: A functional recruitment/marketing site for the Academy
3. **Campaign**: A full enrollment marketing campaign with copy, landing pages, and outreach
4. **Orchestration Demo**: Showcase all five Octopus agents working in pipeline and parallel

## Orchestration Framework
**Framework**: [Octopus Multi-Agent Orchestration OS](https://github.com/victordelrosal/octopus)
**Local repo**: `../octopus/`
**Reference files**: `../octopus/octopus.md` (agent definitions, spawn templates, orchestration patterns)

| Octopus Agent | Color | How We Use It |
|---------------|-------|---------------|
| Researcher | Yellow | Phase 1 — Worldbuilding research (parallel fan-out) |
| Designer | Red-Orange | Phase 2 — Brand, wireframes, site architecture |
| Maker | Blue | Phase 3 — Build the website |
| Marketer | Green | Phase 4 — Enrollment campaign |
| Manager | Purple | All phases — Orchestrates, delegates, synthesizes |

## Architecture
```
chronos-academy/
├── PROJECT_STATE.md      # This file — planning and progress tracking
├── CHANGELOG.md          # All changes logged for rollback
├── QUICKSTART.md         # Session resume prompt
├── research/             # Yellow Researcher output
├── design/               # Red-Orange Designer output
├── build/                # Blue Maker output (website, assets)
└── marketing/            # Green Marketer output
```

## Phases

### Phase 1: Research & Worldbuilding
- [x] University origin story and charter — `research/01-origin-story.md`
- [x] Historical eras and campus locations (8 eras) — `research/02-eras-and-campuses.md`
- [x] Faculty roster (16 professors, 6 departments) — `research/03-faculty-roster.md`
- [x] Course catalog (22 courses, 4 degrees) — `research/04-course-catalog.md`
- [x] Student life and culture — `research/05-student-life.md`

### Phase 2: Design
- [ ] Brand identity (logo concept, color palette, typography)
- [ ] Site map and information architecture
- [ ] Wireframes for key pages (Home, About, Faculty, Courses, Apply)
- [ ] Campus visual concepts per era

### Phase 3: Build
- [ ] Static site (HTML/CSS/JS)
- [ ] Home / landing page
- [ ] Faculty directory page
- [ ] Course catalog page
- [ ] Application / enrollment page

### Phase 4: Marketing & Launch
- [ ] Positioning and tagline
- [ ] Enrollment campaign copy
- [ ] Social media assets and strategy
- [ ] Email sequence for prospective students

## Current Status
**Phase**: 1 COMPLETE — Research & Worldbuilding delivered
**Last updated**: 2026-03-03
**Next action**: Begin Phase 2 — Design (brand identity, site map, wireframes)
