# Chronos Academy — Changelog

All notable changes to this project are documented here. Entries are in reverse chronological order (newest first). Use this log for rollback decisions and change tracking.

---

## [1.0.0] — 2026-03-03
### Added
- Deployed live site to GitHub Pages: https://sacritom.github.io/chronos-academy/
- `build/index.html` — Complete 1,978-line single-page website (65KB, zero dependencies)
- `index.html` — Root copy for GitHub Pages deployment
- Full REPORT.md with orchestration flow diagram, metrics, and observations

### Phase 3: Build (Blue Maker)
- Single-page scrolling site with 8 sections
- Dark mode, Meridian Gold accents, Google Fonts (Cinzel, Libre Baskerville, Orbitron)
- 8 campus cards with era-specific colors, 16 faculty cards, 4 degree programs
- Sticky nav, mobile hamburger, scroll animations, fully responsive
- Pattern: **Sequential Pipeline** (research > design > build)

### Phase 4: Deployment (Purple Manager)
- Created GitHub repo: SacriTom/chronos-academy
- Enabled GitHub Pages on master branch
- Live URL: https://sacritom.github.io/chronos-academy/

### Status
- v1.0 complete — site live and shareable

---

## [0.2.0] — 2026-03-03
### Added
- Completed Phase 2: Design (parallel fan-out, 4 agents)
- `design/01-brand-identity.md` — Logo, colors (Deep Basalt/Meridian Gold/Parchment), typography, CSS variables
- `design/02-site-map.md` — Full site map, single-page MVP layout, content priority matrix
- `design/03-wireframes.md` — ASCII wireframes for all 8 sections, responsive specs
- `design/04-campus-visuals.md` — Per-campus color schemes, gradients, card component spec

### Orchestration
- Pattern: **Parallel Fan-Out** (4 Red-Orange Designers simultaneously)
- Wall clock time: ~4 minutes for all 4 design docs

### Status
- Phase 2 complete — ready for build

---

## [0.1.0] — 2026-03-03
### Added
- Created REPORT.md — orchestration report for class presentation
- Completed Phase 1: Research & Worldbuilding (parallel fan-out, 5 agents)
- `research/01-origin-story.md` — Founding lore, Dr. Elara Voss, the Meridian, Council of Hours
- `research/02-eras-and-campuses.md` — 8 campuses from 68M BCE to 22nd century
- `research/03-faculty-roster.md` — 16 historical figures as professors, 6 departments
- `research/04-course-catalog.md` — 22 courses, 4 degree programs, academic calendar
- `research/05-student-life.md` — Housing, 9 clubs, traditions, temporal ethics, safety

### Orchestration
- Pattern used: **Parallel Fan-Out** (5 Yellow Researchers simultaneously)
- Wall clock time: ~4 minutes for all 5 research briefs

### Status
- Phase 1 complete — all worldbuilding delivered
- Ready for Phase 2: Design

---

## [0.0.1] — 2026-03-03
### Added
- Initialized project folder structure
- Created PROJECT_STATE.md with full 4-phase plan
- Created CHANGELOG.md (this file)
- Created QUICKSTART.md with session resume prompt
- Defined project vision: time-travel university built with Octopus multi-agent orchestration

### Status
- Phase 0 complete — project scaffolding in place
- Ready to begin Phase 1: Research & Worldbuilding
