# Chronos Academy — Site Map & Information Architecture

**Document:** 02-site-map.md
**Role:** Red-Orange Designer Agent
**Date:** 2026-03-03
**Status:** Design Specification (no build)

---

## 1. Site Map — Full Multi-Page Architecture

```
CHRONOS ACADEMY WEBSITE
│
├── HOME (Landing Page)
│   ├── Hero Section (motto, CTA to Apply / Explore)
│   ├── Academy Overview (mission teaser)
│   ├── Featured Campuses carousel
│   ├── Faculty highlights (3-4 portraits)
│   └── CTA: Apply Now / Explore Eras
│
├── ABOUT
│   ├── Origin Story (The Eclipse of 1923, The Horologists, Thingvellir)
│   ├── Mission & Three Pillars
│   ├── The Charter of Chronos (7 Principles summary)
│   ├── The Meridian (how time travel works)
│   ├── Governance — Council of Hours & Keeper of the Threshold
│   ├── Key Dates Timeline (interactive)
│   └── Academy Motto
│
├── ERAS & CAMPUSES
│   ├── Overview / Campus Map (visual grid of all 8)
│   ├── Alexandria Campus (3rd c. BCE)
│   ├── Shaolin Campus (7th c. CE)
│   ├── Timbuktu Campus (14th c. CE)
│   ├── Florence Campus (15th c. CE)
│   ├── Varanasi Campus (5th c. CE)
│   ├── Manchester Campus (19th c. CE)
│   ├── Tomorrow Campus — Nairobi Station (22nd c. CE)
│   └── Pangaea Campus (68M BCE)
│       [Each sub-page: description, academic focus, signature
│        experience, risks, photo/illustration]
│
├── FACULTY
│   ├── Overview / Department Grid
│   ├── Individual Faculty Profiles (x16)
│   │   [Each: name, title, dept, era, courses, teaching style,
│   │    quote, office hours note]
│   └── Inter-Departmental Collaborations sidebar
│
├── ACADEMICS
│   ├── Degree Programs (B.T.E., B.C.D., M.P.S., B.C.S.)
│   ├── Departments Overview (6 departments)
│   ├── Course Catalog
│   │   ├── TEMP courses
│   │   ├── PHIL courses
│   │   ├── HIST courses
│   │   ├── DIPL courses
│   │   ├── PARA courses
│   │   └── ARTL courses
│   ├── Academic Calendar & Trimester Structure
│   └── Academic Policies (grading, integrity, health & safety)
│
├── STUDENT LIFE
│   ├── Housing (Pods, Era Dormitories, Host Family Program)
│   ├── A Typical Week
│   ├── Dining Across Eras (The Big Seven)
│   ├── Clubs & Organizations (9+ clubs)
│   ├── Traditions & Events
│   │   ├── Arrival Day
│   │   ├── Temporal Fair
│   │   ├── Midwinter Gathering
│   │   ├── Paradox Day
│   │   ├── The Reckoning
│   │   └── The Unmooring (Graduation)
│   ├── Social Dynamics (era identity, slang, fashion, dating)
│   └── Campus Safety (TSD, paradox prevention, emergency protocols)
│
├── APPLY (CTA Page)
│   ├── Admissions Requirements
│   ├── Application Form / Portal Link
│   └── FAQ
│
└── FOOTER NAV
    ├── About
    ├── Contact
    ├── Privacy / Temporal Oath
    ├── Social Links
    └── Academy Motto: "Tempus docet. Nos discimus."
```

### Primary Navigation (Desktop)

| Position | Label | Links To |
|----------|-------|----------|
| 1 | **About** | /about |
| 2 | **Eras & Campuses** | /eras (with dropdown showing 8 campuses) |
| 3 | **Faculty** | /faculty |
| 4 | **Academics** | /academics (with dropdown: Programs, Courses, Calendar) |
| 5 | **Student Life** | /student-life |
| 6 | **Apply** (button, accent color) | /apply |

Logo at far left links to Home.

### Footer Navigation

- About | Eras | Faculty | Academics | Student Life
- The Charter | The Temporal Oath | Contact | Privacy
- Motto: *"Tempus docet. Nos discimus."* / *"Time teaches. We learn."*

---

## 2. Page Inventory

### HOME

| Attribute | Detail |
|-----------|--------|
| **Purpose** | First impression; convey the wonder and gravity of Chronos Academy |
| **Key Sections** | Hero (motto + dramatic visual), Mission teaser (1 paragraph), Campus cards (3-4 featured), Faculty spotlights (3-4 portraits with quotes), Student testimonial pull-quote, CTA block |
| **Primary CTA** | "Begin Your Journey" / "Apply Now" |
| **MVP Priority** | MUST HAVE |

### ABOUT

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Tell the founding story; establish credibility and world depth |
| **Key Sections** | Origin narrative (condensed from research doc 01), Mission & Three Pillars, Charter principles (accordion or summary cards), The Meridian (visual explainer), Governance overview, Timeline of key dates |
| **Primary CTA** | "Explore Our Campuses" |
| **MVP Priority** | MUST HAVE (condensed) |

### ERAS & CAMPUSES (Hub + 8 Sub-Pages)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Showcase the 8 campuses — the most visually compelling content |
| **Key Sections** | Hub: visual grid/map of all 8 with era, location, difficulty. Each sub-page: campus description, academic focus, signature experience, risks & challenges |
| **Primary CTA** | "See the Full Course Catalog" or "Apply Now" |
| **MVP Priority** | Hub: MUST HAVE. Sub-pages: NICE TO HAVE (summarize on hub for MVP) |

### FACULTY

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Introduce the legendary faculty roster |
| **Key Sections** | Department grid, individual profile cards (name, era, title, quote, 1-line teaching style), expandable full bios |
| **Primary CTA** | "View Course Catalog" |
| **MVP Priority** | MUST HAVE (grid with cards; full bios NICE TO HAVE) |

### ACADEMICS

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Present degree programs, departments, and courses |
| **Key Sections** | 4 degree programs (cards), 6 departments, course listings by department, academic calendar, policies |
| **Primary CTA** | "Apply Now" |
| **MVP Priority** | Degree overview: MUST HAVE. Full course catalog: NICE TO HAVE |

### STUDENT LIFE

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Make prospective students feel what it is like to attend |
| **Key Sections** | Housing options, typical week narrative, dining halls, clubs (cards), traditions/events timeline, social dynamics, campus safety |
| **Primary CTA** | "Apply Now" |
| **MVP Priority** | Condensed highlights: MUST HAVE. Full detail: NICE TO HAVE |

### APPLY

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Convert interested visitors |
| **Key Sections** | Requirements summary, application portal link/form, FAQ |
| **Primary CTA** | "Submit Application" |
| **MVP Priority** | MUST HAVE (even if placeholder) |

---

## 3. Navigation Design

### Desktop Navigation

- **Sticky top bar** with logo (left), 5 text links (center), Apply button (right, accent gold/amber)
- **Dropdown menus** for "Eras & Campuses" (8 campus links) and "Academics" (Programs, Courses, Calendar)
- All other items are single-click direct links

### Mobile Navigation

- **Hamburger menu** (top right), logo (top left)
- Full-screen overlay on tap, with stacked nav items
- "Apply" button pinned at bottom of overlay for persistent access
- Eras and Academics sections expand as accordions within the overlay
- No dropdown hovers on mobile; all tap-driven

### Key User Journeys

**Journey 1: The Curious Visitor**
```
HOME (hero) --> ABOUT (origin story) --> ERAS (campus grid)
--> 1-2 campus sub-pages --> FACULTY --> APPLY
```
Estimated time: 5-8 minutes. This is the primary funnel.

**Journey 2: The Academically Motivated**
```
HOME --> ACADEMICS (degree programs) --> Course Catalog
--> FACULTY (find instructors) --> APPLY
```
Estimated time: 4-6 minutes.

**Journey 3: The Lifestyle Explorer**
```
HOME --> STUDENT LIFE (housing, clubs, traditions)
--> ERAS (campus details) --> APPLY
```
Estimated time: 5-7 minutes.

**Journey 4: The Quick Scanner**
```
HOME (scroll full page) --> APPLY
```
Estimated time: 2-3 minutes. The single-page layout supports this.

---

## 4. Content Priority Matrix

### MUST HAVE for MVP (Build First)

| Content | Rationale |
|---------|-----------|
| **Hero section** with motto, mission teaser, CTA | First impression; communicates identity instantly |
| **Origin story** (condensed to 2-3 paragraphs) | The founding lore is the emotional hook |
| **Campus overview grid** (all 8 campuses, summary cards) | The most visually compelling and unique content |
| **Faculty roster** (grid of 16 with name, era, title, quote) | Star power; instantly communicates the premise |
| **Degree programs** (4 cards with brief descriptions) | Answers "what would I study?" |
| **Student life highlights** (housing, dining, 2-3 traditions) | Makes the world feel lived-in |
| **Apply CTA** (persistent, visible) | Conversion point |
| **The Temporal Oath** (honor code text) | Short, powerful, encapsulates the ethos |
| **Academy motto** in footer | Branding anchor |

### NICE TO HAVE (Build If Time Permits)

| Content | Rationale |
|---------|-----------|
| Individual campus sub-pages (8 pages) | Rich content but the grid summary covers the essence |
| Full faculty bios with teaching style, office hours | Entertaining but not essential for first impression |
| Full course catalog (20+ courses) | Deep content; summary by department suffices for MVP |
| Academic policies, calendar, grading details | Important for enrolled students, not for marketing site |
| Complete clubs listing (9 clubs with full descriptions) | Fun but secondary; 3-4 featured clubs is enough |
| Social dynamics section (slang, dating, fashion) | Charming world-building but lowest conversion impact |
| Full Charter of Chronos (7 principles, expanded) | Accordion or linked page; the summary is sufficient |
| Campus safety & emergency protocols detail | Internal/operational feel; a brief mention suffices |
| Interactive timeline of key dates | Visual polish; a static list works for MVP |
| The Meridian deep-dive | Fascinating lore but secondary to the campus/faculty hook |

### Build Order Recommendation

```
Phase 1 (MVP - within 45 min):  Single-page scrolling layout (see Section 5)
Phase 2 (if time remains):      Break into multi-page with campus sub-pages
Phase 3 (polish):               Full bios, course catalog, interactive elements
```

---

## 5. Single-Page Scrolling Layout (MVP Recommendation)

Given the 45-minute constraint, a single-page scrolling site is the recommended MVP. Every section below maps to a defined scroll section with a clear visual break.

### Section Order & Content Spec

```
┌─────────────────────────────────────────────────┐
│  SECTION 1: HERO                                │
│                                                 │
│  Full-viewport hero with ambient background     │
│  (dark, starfield or amber light texture)       │
│                                                 │
│  "Tempus docet. Nos discimus."                  │
│  Time teaches. We learn.                        │
│                                                 │
│  CHRONOS ACADEMY                                │
│  The world's first institution of               │
│  temporal education.                            │
│                                                 │
│  [Begin Your Journey]  [Explore Eras]           │
│                                                 │
├─────────────────────────────────────────────────┤
│  SECTION 2: ORIGIN STORY                        │
│                                                 │
│  Heading: "It Started with Eleven Seconds"      │
│                                                 │
│  2-3 paragraph condensed origin:                │
│  - The Eclipse of 1923 / Elara Voss             │
│  - The Horologists                              │
│  - The Breakthrough at Thingvellir, 1953        │
│  - The question: "What if we learn from it?"    │
│                                                 │
│  Pull quote: Mission statement                  │
│                                                 │
│  The Three Pillars (3 icon cards):              │
│  1. Witness, Never Interfere                    │
│  2. Knowledge in Service of the Future          │
│  3. Humility Before the Stream                  │
│                                                 │
├─────────────────────────────────────────────────┤
│  SECTION 3: ERAS & CAMPUSES                     │
│                                                 │
│  Heading: "Eight Campuses Across Time"          │
│                                                 │
│  Grid of 8 campus cards (2x4 or responsive):    │
│  Each card shows:                               │
│  - Campus name                                  │
│  - Era & location                               │
│  - Primary discipline                           │
│  - Difficulty rating                            │
│  - 1-sentence signature experience              │
│                                                 │
│  Example card:                                  │
│  ┌──────────────────────┐                       │
│  │ ALEXANDRIA            │                       │
│  │ 3rd c. BCE · Egypt    │                       │
│  │ Knowledge Systems     │                       │
│  │ ★★★ Moderate          │                       │
│  │ "The Scroll Hunt"     │                       │
│  └──────────────────────┘                       │
│                                                 │
│  Comparative table below (from research doc)    │
│                                                 │
├─────────────────────────────────────────────────┤
│  SECTION 4: FACULTY                             │
│                                                 │
│  Heading: "Learn from Every Generation"         │
│                                                 │
│  Scrollable row or grid of faculty cards (16):  │
│  Each card:                                     │
│  - Name                                         │
│  - Title & Department                           │
│  - Era/Campus                                   │
│  - Signature quote                              │
│                                                 │
│  Highlight 4-5 with larger cards:               │
│  Einstein, Hypatia, da Vinci, Cleopatra, Tubman │
│                                                 │
│  Department summary (6 depts in a small table)  │
│                                                 │
├─────────────────────────────────────────────────┤
│  SECTION 5: ACADEMICS                           │
│                                                 │
│  Heading: "Four Paths Through Time"             │
│                                                 │
│  4 degree program cards:                        │
│  - B.T.E. (Temporal Engineering)                │
│  - B.C.D. (Cross-Era Diplomacy)                 │
│  - M.P.S. (Paradox Sciences)                    │
│  - B.C.S. (Chrono-Cultural Studies)             │
│                                                 │
│  Core Curriculum callout box:                   │
│  "Every student completes: Ethics, Survival,    │
│   Non-Interference Law, and Chronophysics."     │
│                                                 │
│  Trimester structure (brief visual)             │
│                                                 │
├─────────────────────────────────────────────────┤
│  SECTION 6: STUDENT LIFE                        │
│                                                 │
│  Heading: "Life Across Seven Eras"              │
│                                                 │
│  Sub-sections (compact):                        │
│                                                 │
│  HOUSING: 3 options described in 1 line each    │
│  + era dormitory table (7 dorms)                │
│                                                 │
│  DINING: "The Big Seven" — 1-line per hall      │
│                                                 │
│  CLUBS: 4-5 featured clubs as small cards       │
│  (Paradox Society, AAS, Chrono-Relay,           │
│   Temporal Tones, Butterfly Watchers)           │
│                                                 │
│  TRADITIONS: Horizontal scroll or list          │
│  (Arrival Day, Temporal Fair, Paradox Day,      │
│   The Reckoning, The Unmooring)                 │
│                                                 │
├─────────────────────────────────────────────────┤
│  SECTION 7: THE TEMPORAL OATH                   │
│                                                 │
│  Full text of the oath, centered, large type,   │
│  on a dark/amber background.                    │
│                                                 │
│  This is the emotional climax of the page.      │
│                                                 │
│  "I accept the privilege of moving through      │
│   time and the weight of responsibility         │
│   it carries..."                                │
│                                                 │
├─────────────────────────────────────────────────┤
│  SECTION 8: APPLY / CTA                         │
│                                                 │
│  Heading: "Your Timeline Starts Here"           │
│                                                 │
│  Brief admissions text                          │
│  [Apply Now] large button                       │
│                                                 │
│  Enrollment quote from Student Handbook:        │
│  "Chronos Academy does not simulate history.    │
│   It does not approximate it... We send you     │
│   there."                                       │
│                                                 │
├─────────────────────────────────────────────────┤
│  FOOTER                                         │
│                                                 │
│  Logo · Nav links · Motto                       │
│  "Tempus docet. Nos discimus."                  │
│  "Time teaches. We learn."                      │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Single-Page Navigation (Sticky Header)

For the single-page layout, the sticky nav becomes anchor links:

| Nav Item | Scrolls To |
|----------|-----------|
| Origin | Section 2 |
| Eras | Section 3 |
| Faculty | Section 4 |
| Academics | Section 5 |
| Student Life | Section 6 |
| **Apply** (button) | Section 8 |

On mobile, this collapses to a hamburger with the same anchor links.

### Content Cuts for Single-Page MVP

Content from the research that is intentionally **excluded** from the single-page MVP to keep scope manageable:

- Full Charter principles text (include only the Three Pillars)
- The Meridian deep-dive (mention it exists in the origin story; skip the technical detail)
- Council of Hours governance table (mention the Keeper; skip the 12 seats)
- Individual campus sub-pages (the grid cards cover the essence)
- Full faculty bios, teaching styles, office hours (the quote + title is sufficient)
- Full course catalog (mention departments and 4 example courses)
- Academic policies, grading, integrity rules
- Complete clubs listing (feature 5 of 9)
- Social dynamics (slang, dating, fashion, hierarchies)
- Full campus safety & emergency protocols
- The Anchor System technical detail
- Typical week narrative (charming but space-consuming)

All of this content is preserved in the research docs and can be added as sub-pages in Phase 2.

---

## Design Notes for the Builder Agent

1. **Color palette cue:** Amber/gold is the signature color of the Meridian and should be the accent throughout. Dark backgrounds (basalt, night sky) for contrast. The world-building references amber light, bismuth crystals, and the Icelandic landscape.

2. **Typography cue:** The Academy feels scholarly but not stuffy. A serif for headings (gravitas), a clean sans-serif for body (modernity). The motto appears in five languages in the lore — consider using the Latin on-screen.

3. **Visual rhythm:** Alternate between dark sections (hero, oath) and light sections (campuses, academics) to create scroll momentum.

4. **The Temporal Oath section** should be treated as a full-bleed, cinematic moment — large typography, dark background, amber accent. It is the emotional peak of the page.

5. **Campus cards** are the most visually flexible element. If time permits, give each a distinct color or texture that hints at its era (papyrus for Alexandria, red brick for Manchester, green for Pangaea, etc.).

6. **Faculty quotes** are gold. Use them. Every single faculty entry has a witty, memorable quote that sells the personality of the Academy.

7. **The enrollment quote** from the Student Handbook ("We send you there. The past is not a museum...") is the best closing copy in the research. Use it near the Apply CTA.

---

*Document prepared by the Red-Orange Designer Agent for Octopus orchestration.*
*All content sourced from Chronos Academy research files 01-05.*
