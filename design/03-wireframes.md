# Chronos Academy — Single-Page Website Wireframes

**Document Type:** ASCII Wireframes & Layout Specification
**Approach:** Single-page scrolling website with 8 distinct sections
**Target:** Desktop-first (~80 char width), responsive to mobile
**Design Agent:** Red-Orange Designer

---

## Section 1: Hero

```
+------------------------------------------------------------------------+
|  [Logo: Hourglass]   CHRONOS ACADEMY             [Menu Icon / Hamburger]|
|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                        |
|                                                                        |
|                    C H R O N O S   A C A D E M Y                       |
|                                                                        |
|                  ~~~ The World's First Institution ~~~                  |
|                  ~~~   of Temporal Education      ~~~                   |
|                                                                        |
|                                                                        |
|              "Tempus docet. Nos discimus."                              |
|               Time teaches. We learn.                                   |
|                                                                        |
|                                                                        |
|               [ EXPLORE THE ACADEMY ]    [ APPLY NOW ]                 |
|                  (primary CTA btn)       (secondary btn)               |
|                                                                        |
|                                                                        |
|                         |                                              |
|                         |  <-- scroll indicator                        |
|                         V     (animated bouncing arrow)                 |
+------------------------------------------------------------------------+
```

### Content Notes
- **Background:** Full-viewport parallax background. A dark, cinematic image
  of the amber-gold temporal aperture (the Meridian's golden sphere) against
  basalt rock, with bismuth crystals glowing. Subtle particle/light effects.
- **Logo:** Stylized hourglass mark with "CHRONOS ACADEMY" wordmark.
  The hourglass subtly animates (sand trickling) on load.
- **Heading:** Large display typeface. "CHRONOS ACADEMY" — letter-spaced,
  all caps. Consider an amber-gold gradient on the text.
- **Subheading:** "The World's First Institution of Temporal Education" in
  a lighter serif or italic style, slightly smaller.
- **Motto:** "Tempus docet. Nos discimus." in italic, with English
  translation below in smaller text.
- **CTAs:** Two buttons side by side.
  - Primary: "EXPLORE THE ACADEMY" — solid amber/gold fill, dark text.
  - Secondary: "APPLY NOW" — outlined, gold border, transparent fill.
- **Scroll indicator:** Animated chevron/arrow at bottom center.

### Responsive Notes (Mobile)
- Stack heading and subheading vertically; reduce font size ~40%.
- CTAs stack vertically, full-width buttons.
- Menu collapses to hamburger icon (already shown).
- Background image crops to center; reduce parallax intensity or disable.

### Interaction Notes
- **On load:** Fade-in sequence: background first, then title, then motto,
  then CTAs. Stagger ~200ms each.
- **Parallax:** Background scrolls at 0.5x rate relative to content.
- **Hover (CTAs):** Primary button glows amber; secondary fills with gold.
- **Scroll indicator:** Gentle bounce animation (CSS keyframe, 2s loop).
- **Sticky nav:** After scrolling past hero, the top bar becomes a fixed
  nav with semi-transparent dark background and section links.

---

## Section 2: About / Origin Story

```
+------------------------------------------------------------------------+
|                                                                        |
|                        OUR ORIGIN                                      |
|                   ___________________                                  |
|                   (decorative divider)                                  |
|                                                                        |
|   +------------------------------+  +-------------------------------+  |
|   |                              |  |                               |  |
|   |   [Illustration/Image:      |  |  In 1923, Dr. Elara Voss      |  |
|   |    Dr. Elara Voss in her    |  |  experienced eleven seconds    |  |
|   |    Cambridge laboratory,    |  |  of frozen time. Thirty years  |  |
|   |    bismuth crystals         |  |  later, she and four fellow    |  |
|   |    glowing amber]           |  |  Horologists opened the first  |  |
|   |                              |  |  temporal aperture at          |  |
|   |                              |  |  Thingvellir, Iceland.         |  |
|   |                              |  |                               |  |
|   |                              |  |  They asked: what if time      |  |
|   |                              |  |  travel was not a weapon, but  |  |
|   |                              |  |  an education?                 |  |
|   |                              |  |                               |  |
|   +------------------------------+  +-------------------------------+  |
|                                                                        |
|   +------------------------------------------------------------------+ |
|   |                     THE THREE PILLARS                            | |
|   |                                                                  | |
|   |   [Icon: Eye]          [Icon: Lamp]        [Icon: Water]         | |
|   |   WITNESS, NEVER       KNOWLEDGE IN        HUMILITY BEFORE       | |
|   |   INTERFERE            SERVICE OF           THE STREAM            | |
|   |                        THE FUTURE                                | |
|   |   The past is not      Everything learned   Time is larger than   | |
|   |   ours to edit.        serves the present   any institution.      | |
|   |                        and future.                                | |
|   +------------------------------------------------------------------+ |
|                                                                        |
|   +------------------------------------------------------------------+ |
|   |                     THE MERIDIAN                                 | |
|   |                                                                  | |
|   |  [Animated illustration: golden sphere / temporal aperture       | |
|   |   with amber light radiating outward, bismuth crystal lattice    | |
|   |   surrounding it]                                                | |
|   |                                                                  | |
|   |  "11,111 bismuth crystals. A golden sphere of light.            | |
|   |   A window through time itself."                                 | |
|   |                                                                  | |
|   |   [ LEARN MORE ABOUT THE MERIDIAN ]  (text link / subtle btn)   | |
|   +------------------------------------------------------------------+ |
|                                                                        |
+------------------------------------------------------------------------+
```

### Content Notes
- **Section title:** "OUR ORIGIN" centered, with decorative line divider
  (could be a thin gold line or a stylized clock-hand motif).
- **Two-column layout:** Left column is an atmospheric illustration of Dr.
  Elara Voss (or an artistic representation of the 1923 Frozen Moment).
  Right column is a concise retelling of the founding story (~80 words max).
- **Three Pillars:** Three-column sub-section with icons and short
  descriptions. Each pillar from the mission statement.
- **The Meridian:** A visual feature block. Could be an animated SVG or
  WebGL illustration of the golden temporal aperture. Accompanied by a
  poetic one-liner and an optional "learn more" link.
- **Data points to include:** Founded 1953. Five founders (The Horologists).
  73 years of operation. Located at Thingvellir, Iceland.

### Responsive Notes (Mobile)
- Two-column layout stacks to single column (image on top, text below).
- Three Pillars stack vertically (icon + title + description per row).
- The Meridian illustration scales down; animation simplifies.

### Interaction Notes
- **Scroll-triggered:** Content fades in as user scrolls into view.
  Left column slides in from left, right from right.
- **Three Pillars:** Icons animate on scroll-in (e.g., eye blinks,
  lamp flickers, water ripples). Subtle, 1-2 second animation.
- **Meridian illustration:** Continuous gentle animation (pulsing glow,
  slowly rotating crystal lattice). Intensifies slightly on hover.
- **Number counter:** If showing stats (73 years, 11,111 crystals, 5
  founders), animate them counting up on scroll-in.

---

## Section 3: Campuses / Eras

```
+------------------------------------------------------------------------+
|                                                                        |
|                    EIGHT ERAS. EIGHT CAMPUSES.                         |
|           Study where history happened. Stand where it stood.          |
|                                                                        |
|   +------------------+  +------------------+  +------------------+     |
|   | //////////////// |  | //////////////// |  | //////////////// |     |
|   | / [Image:       /|  | / [Image:       /|  | / [Image:       /|     |
|   | / Alexandria    /|  | / Shaolin       /|  | / Timbuktu     /|     |
|   | / lighthouse]  / |  | / misty peaks] / |  | / mosque]      / |     |
|   | //////////////// |  | //////////////// |  | //////////////// |     |
|   |                  |  |                  |  |                  |     |
|   |  ALEXANDRIA      |  |  SHAOLIN         |  |  TIMBUKTU        |     |
|   |  3rd c. BCE      |  |  7th c. CE       |  |  14th c. CE      |     |
|   |  Egypt           |  |  China           |  |  Mali            |     |
|   |  ~~~~~~~~~~~~~~  |  |  ~~~~~~~~~~~~~~  |  |  ~~~~~~~~~~~~~~  |     |
|   |  Knowledge       |  |  Embodied        |  |  Trade & Legal   |     |
|   |  Systems         |  |  Learning        |  |  Studies         |     |
|   |                  |  |                  |  |                  |     |
|   |  Difficulty:     |  |  Difficulty:     |  |  Difficulty:     |     |
|   |  ** [Moderate]   |  |  *** [High]      |  |  ** [Moderate]   |     |
|   +------------------+  +------------------+  +------------------+     |
|                                                                        |
|   +------------------+  +------------------+  +------------------+     |
|   | //////////////// |  | //////////////// |  | //////////////// |     |
|   | / [Image:       /|  | / [Image:       /|  | / [Image:       /|     |
|   | / Florence     /|  | / Varanasi     /|  | / Manchester   /|     |
|   | / duomo]       / |  | / ghats]       / |  | / chimneys]    / |     |
|   | //////////////// |  | //////////////// |  | //////////////// |     |
|   |                  |  |                  |  |                  |     |
|   |  FLORENCE        |  |  VARANASI        |  |  MANCHESTER      |     |
|   |  15th c. CE      |  |  5th c. CE       |  |  19th c. CE      |     |
|   |  Italy           |  |  India           |  |  England         |     |
|   |  ~~~~~~~~~~~~~~  |  |  ~~~~~~~~~~~~~~  |  |  ~~~~~~~~~~~~~~  |     |
|   |  Art & Political |  |  Mathematics &   |  |  Industrial      |     |
|   |  Science         |  |  Philosophy      |  |  Studies         |     |
|   |                  |  |                  |  |                  |     |
|   |  Difficulty:     |  |  Difficulty:     |  |  Difficulty:     |     |
|   |  *** [High]      |  |  **** [V. High]  |  |  ** [Moderate]   |     |
|   +------------------+  +------------------+  +------------------+     |
|                                                                        |
|   +------------------+  +------------------+                           |
|   | //////////////// |  | //////////////// |                           |
|   | / [Image:       /|  | / [Image:       /|                           |
|   | / Nairobi      /|  | / Cretaceous   /|                           |
|   | / skyline]     / |  | / T-rex]       / |                           |
|   | //////////////// |  | //////////////// |                           |
|   |                  |  |                  |                           |
|   |  TOMORROW        |  |  PANGAEA         |                           |
|   |  (NAIROBI)       |  |  68M BCE         |                           |
|   |  22nd c. CE      |  |  Laramidia       |                           |
|   |  ~~~~~~~~~~~~~~  |  |  ~~~~~~~~~~~~~~  |                           |
|   |  Future Studies  |  |  Deep-Time       |                           |
|   |  & Ethics        |  |  Ecology         |                           |
|   |                  |  |                  |                           |
|   |  Difficulty:     |  |  Difficulty:     |                           |
|   |  *** [High]      |  |  ***** [Extreme] |                           |
|   +------------------+  +------------------+                           |
|                                                                        |
+------------------------------------------------------------------------+
```

### Content Notes
- **Section title:** "EIGHT ERAS. EIGHT CAMPUSES." centered, bold.
- **Subtitle:** Evocative one-liner beneath the title.
- **Card grid:** 8 campus cards in a 3-3-2 layout (desktop).
  Each card contains:
  - **Image area:** Atmospheric illustration or photo representing the era.
    Color-graded with an amber/sepia overlay to maintain visual cohesion.
  - **Campus name:** Bold, uppercase.
  - **Era / date range:** Smaller text beneath the name.
  - **Location:** Geographic location.
  - **Primary discipline:** One-line descriptor of the academic focus.
  - **Difficulty rating:** Star-based or pip-based visual indicator.
- **Data source:** From the campus reference table in 02-eras-and-campuses.md.
- **Signature experiences:** Not shown on cards to keep them compact, but
  revealed on hover/click (see interaction notes).

### Responsive Notes (Mobile)
- Cards go to single-column, full-width, stacked vertically.
- Consider a horizontal scroll / carousel on tablet (2 visible at a time).
- Images become shorter (landscape ratio) on mobile to save vertical space.
- Difficulty rating remains visible on all breakpoints.

### Interaction Notes
- **Hover on card:** Card lifts slightly (translateY -4px, box-shadow
  increase). Image zooms subtly (scale 1.05). A short "signature
  experience" tagline fades in over the image.
  Example: Alexandria card shows "The Scroll Hunt" on hover.
- **Click/tap on card:** Expands into a modal or slides open an overlay
  with full campus description, signature experience, risks, and a
  larger image. Close button returns to grid.
- **Scroll animation:** Cards fade in staggered (left-to-right, top-to-bottom)
  as user scrolls into the section. ~100ms stagger between cards.
- **Optional enhancement:** A horizontal timeline bar above the cards showing
  the eras arranged chronologically (68M BCE to 22nd c. CE), with dots
  marking each campus. Scrolling the cards highlights the corresponding
  dot on the timeline.

---

## Section 4: Faculty Highlights

```
+------------------------------------------------------------------------+
|                                                                        |
|                    LEARN FROM EVERY ERA                                 |
|          "We do not hire the best minds of a generation.               |
|           We hire the best minds of every generation."                  |
|                                                                        |
|   +------+  +------+  +------+  +------+  +------+  +------+          |
|   |[img] |  |[img] |  |[img] |  |[img] |  |[img] |  |[img] |          |
|   | Ein- |  |Hypa- |  | Leo- |  |Marie |  | Sun  |  |Frida |          |
|   |stein |  | tia  |  |nardo |  |Curie |  | Tzu  |  |Kahlo |          |
|   |      |  |      |  |      |  |      |  |      |  |      |          |
|   |TEMP  |  |NSCI  |  |ENGR  |  |NSCI  |  |LEAD  |  |ARTS  |          |
|   +------+  +------+  +------+  +------+  +------+  +------+          |
|                                                                        |
|   +------+  +------+  +------+  +------+  +------+  +------+          |
|   |[img] |  |[img] |  |[img] |  |[img] |  |[img] |  |[img] |          |
|   |Tesla |  |Cleo- |  | Ada  |  |Marc. |  |Mura- |  | Ibn  |          |
|   |      |  |patra |  | Love |  |Aurel |  | saki |  | al-H |          |
|   |      |  |      |  |lace  |  | ius  |  |      |  |      |          |
|   |ENGR  |  |LEAD  |  |ENGR  |  |PHIL  |  |ARTS  |  |NSCI  |          |
|   +------+  +------+  +------+  +------+  +------+  +------+          |
|                                                                        |
|                     (remaining 4 shown on expansion)                   |
|                                                                        |
|   +------+  +------+  +------+  +------+                               |
|   |[img] |  |[img] |  |[img] |  |[img] |                               |
|   |Harr- |  |Pytha-|  |Mary  |  |Srin- |                               |
|   | iet  |  |goras |  |Woll- |  |ivasa |                               |
|   |Tubmn |  |      |  |stone |  |Raman |                               |
|   |LEAD  |  |TEMP  |  |PHIL  |  |TEMP  |                               |
|   +------+  +------+  +------+  +------+                               |
|                                                                        |
|   +------------------------------------------------------------------+ |
|   |  FEATURED FACULTY DETAIL (expanded card state)                   | |
|   |                                                                  | |
|   |  +----------+  ALBERT EINSTEIN                                   | |
|   |  | [larger  |  Distinguished Professor of Temporal Sciences      | |
|   |  |  portrait |  Era: 20th C. Zurich (1905)                       | |
|   |  |  image]  |                                                    | |
|   |  |          |  "Imagination is more important than knowledge     | |
|   |  |          |   -- especially when you've left your textbook     | |
|   |  +----------+   in the 18th century."                            | |
|   |                                                                  | |
|   |  Courses:                                                        | |
|   |  - TEMP 301: Relativistic Chrononautics                         | |
|   |  - TEMP 415: The Fabric of Spacetime                            | |
|   |  - TEMP 210: Thought Experiments for the Reckless               | |
|   +------------------------------------------------------------------+ |
|                                                                        |
+------------------------------------------------------------------------+
```

### Content Notes
- **Section title:** "LEARN FROM EVERY ERA" centered.
- **Subtitle:** The quote from the Office of the Provost.
- **Faculty grid:** Show the first 12 faculty in a 6x2 grid (desktop).
  Remaining 4 appear after a "Show All Faculty" toggle.
  Each mini-card contains:
  - **Portrait:** Circular or rounded-square avatar (illustrated/stylized,
    not photographic, since these are historical figures). Consistent art
    style across all portraits.
  - **Name:** Bold, abbreviated if needed for space.
  - **Department code:** Color-coded badge (TEMP=gold, NSCI=green,
    ENGR=blue, ARTS=magenta, LEAD=red, PHIL=silver).
- **Expanded detail card:** When a faculty member is selected, an expanded
  view appears below the grid (or as an inline expansion) showing:
  - Larger portrait
  - Full title and department
  - Era/campus
  - Signature quote (repurposed)
  - Top courses taught
- **Data source:** From 03-faculty-roster.md.

### Responsive Notes (Mobile)
- Grid becomes 3x columns on tablet, 2x columns on mobile.
- Expanded detail card goes full-width on mobile.
- Consider a horizontal scrollable row on mobile instead of a grid.

### Interaction Notes
- **Hover on mini-card:** Card scales slightly (1.05). A colored border
  matching the department appears. Name and department fade in if they
  were truncated.
- **Click/tap:** Selected card highlights with a gold ring. The expanded
  detail card slides open below the grid with a smooth animation.
  Clicking another card swaps the content with a crossfade.
- **Scroll animation:** Portraits fade in with a stagger effect, each
  one popping in with a slight scale-up (~100ms delay between cards).

---

## Section 5: Course Catalog Preview

```
+------------------------------------------------------------------------+
|                                                                        |
|                    COURSES ACROSS TIME                                  |
|              4 Degree Programs. 6 Departments. Every Era.              |
|                                                                        |
|   +------------------------------------------------------------------+ |
|   | DEPARTMENT TABS                                                   | |
|   |                                                                  | |
|   |  [TEMP]  [PHIL]  [HIST]  [DIPL]  [PARA]  [ARTL]                 | |
|   |  ~~~~~~                                                          | |
|   |  (active tab underlined)                                         | |
|   +------------------------------------------------------------------+ |
|                                                                        |
|   +------------------------------------------------------------------+ |
|   | TEMPORAL ENGINEERING (TEMP)                 Head: Nikola Tesla    | |
|   | Hub: Industrial Revolution Campus (1890s London)                 | |
|   |                                                                  | |
|   |  +----------------------------+  +----------------------------+  | |
|   |  | TEMP 101                   |  | TEMP 205                   |  | |
|   |  | Foundations of Slip Gate   |  | Chrono-Navigation &        |  | |
|   |  | Mechanics                  |  | Anchor Calibration         |  | |
|   |  |                            |  |                            |  | |
|   |  | Level: Intro               |  | Level: Intermediate        |  | |
|   |  | Instructor: Tesla          |  | Instructor: Banneker       |  | |
|   |  | Prereqs: None              |  | Prereqs: TEMP 101          |  | |
|   |  +----------------------------+  +----------------------------+  | |
|   |                                                                  | |
|   |  +----------------------------+  +----------------------------+  | |
|   |  | TEMP 310                   |  | TEMP 450                   |  | |
|   |  | Temporal Shielding &       |  | Advanced Slip Gate         |  | |
|   |  | Containment Architecture   |  | Design & Construction      |  | |
|   |  |                            |  |                            |  | |
|   |  | Level: Intermediate        |  | Level: Advanced            |  | |
|   |  | Instructor: Curie          |  | Instructor: Tesla          |  | |
|   |  | Prereqs: TEMP 101, PARA 150|  | Prereqs: TEMP 205, 310,   |  | |
|   |  |                            |  |          PARA 320          |  | |
|   |  +----------------------------+  +----------------------------+  | |
|   |                                                                  | |
|   +------------------------------------------------------------------+ |
|                                                                        |
|   +------------------------------------------------------------------+ |
|   |  DEGREE PROGRAMS                                                 | |
|   |                                                                  | |
|   |  [B.T.E.]          [B.C.D.]         [M.P.S.]        [B.C.S.]    | |
|   |  Temporal           Cross-Era        Paradox         Chrono-     | |
|   |  Engineering        Diplomacy        Sciences        Cultural    | |
|   |  4 years            4 years          2 years (grad)  4 years     | |
|   +------------------------------------------------------------------+ |
|                                                                        |
|   +------------------------------------------------------------------+ |
|   |  CORE TEMPORAL CURRICULUM (Required of All Students)             | |
|   |  ______________________________________________________________ | |
|   |  PHIL 110   |  HIST 101   |  DIPL 200   |  PARA 150             | |
|   |  Ethics of  |  Surviving  |  Non-Inter- |  Intro to             | |
|   |  Temporal   |  Your First |  ference    |  Chrono-              | |
|   |  Interfer.  |  Displace.  |  Charter    |  physics              | |
|   +------------------------------------------------------------------+ |
|                                                                        |
+------------------------------------------------------------------------+
```

### Content Notes
- **Section title:** "COURSES ACROSS TIME" centered.
- **Subtitle:** Summary stat line.
- **Department tabs:** Horizontal tab row with 6 department codes. Each tab,
  when active, displays that department's courses below. Default active
  tab: TEMP (Temporal Engineering).
- **Course cards:** 2-column grid of course cards within each department tab.
  Each card shows:
  - Course code (e.g., TEMP 101)
  - Course title (full name)
  - Level indicator (Intro / Intermediate / Advanced / Graduate)
  - Instructor name
  - Prerequisites
- **Degree Programs:** A compact row of 4 degree program badges below the
  course area, showing program name, abbreviation, and duration.
- **Core Curriculum:** A highlighted bar at the bottom showing the 4
  required courses for all students. Visually distinct (gold background
  or bordered box) to emphasize universal requirements.
- **Data source:** From 04-course-catalog.md.

### Responsive Notes (Mobile)
- Department tabs become a horizontal scrollable row or a dropdown select.
- Course cards stack to single column.
- Degree programs stack to 2x2 or single column.
- Core Curriculum row stacks vertically.

### Interaction Notes
- **Tab switching:** Clicking a department tab slides in the corresponding
  course list with a horizontal slide or crossfade transition. Active tab
  gets an underline + color highlight matching department color.
- **Course card hover:** Subtle lift + border glow. A "Student Warning"
  tooltip or popover appears with the humorous warning text from the catalog.
- **Degree program badges:** Clicking opens a brief overlay/tooltip with
  the degree description and required department breakdown.
- **Scroll animation:** Tabs and course cards fade in on scroll-into-view.

---

## Section 6: Student Life

```
+------------------------------------------------------------------------+
|                                                                        |
|                    LIFE ACROSS TIME                                     |
|         "Monday could literally be in a different century              |
|          than Friday. Buckle up."                                       |
|                                                                        |
|   +------------------------------------------------------------------+ |
|   |  A WEEK AT CHRONOS         (horizontal timeline visual)          | |
|   |                                                                  | |
|   |  MON         WED            FRI           SAT                    | |
|   |   |           |              |              |                     | |
|   |   o-----------o--------------o--------------o                    | |
|   |   |           |              |              |                     | |
|   | Ethics      Field Study    Seminar &      Explore                | |
|   | lecture     in Florence    clubs meet     your era               | |
|   | (Nexus,     (1497)         Tavern Night   or rest                | |
|   |  2185)                     @ Undercroft                          | |
|   +------------------------------------------------------------------+ |
|                                                                        |
|   +--------------------+  +--------------------+  +----------------+   |
|   | CLUBS & ORGS       |  | TRADITIONS         |  | HOUSING        |   |
|   |                    |  |                    |  |                |   |
|   | [Icon] Paradox     |  | [Icon] Arrival Day |  | [Icon] Temporal|   |
|   |   Society          |  |   & First Transit  |  |   Pods (1st yr)|   |
|   |                    |  |                    |  |                |   |
|   | [Icon] Anachronism |  | [Icon] Temporal    |  | [Icon] Era     |   |
|   |   Appreciation     |  |   Fair (7 eras)    |  |   Dormitories  |   |
|   |                    |  |                    |  |   (7 options)  |   |
|   | [Icon] Chrono-     |  | [Icon] Paradox Day |  |                |   |
|   |   Relay League     |  |   (puzzle hunt)    |  | [Icon] Host    |   |
|   |                    |  |                    |  |   Family       |   |
|   | [Icon] Temporal    |  | [Icon] Lantern     |  |   Immersion    |   |
|   |   Tones (a cap.)   |  |   Send-Off         |  |                |   |
|   |                    |  |                    |  |                |   |
|   | [Icon] Epoch       |  | [Icon] The         |  |                |   |
|   |   Fencing Club     |  |   Unmooring        |  |                |   |
|   |                    |  |   (graduation)     |  |                |   |
|   | +6 more clubs...   |  |                    |  |                |   |
|   +--------------------+  +--------------------+  +----------------+   |
|                                                                        |
|   +------------------------------------------------------------------+ |
|   |  DINING ACROSS ERAS                                              | |
|   |                                                                  | |
|   |  [Icon]        [Icon]        [Icon]        [Icon]                | |
|   |  The Hearth    Mrs.          Eddie's       Hikari                | |
|   |  Alexandria    Cavendish's   NYC 1962      Dining                | |
|   |  280 BCE       London 1888   Burgers &     Tokyo 2045            | |
|   |  Lentil stew   Full English  milkshakes    Ramen &               | |
|   |  & honeyed     & treacle     & cheesecake  sushi                 | |
|   |  figs          tart                                              | |
|   |                                                                  | |
|   |  [Icon]        [Icon]        [Icon]                              | |
|   |  Mead Bench    Canopy        Le Caveau                           | |
|   |  Vinland 1005  Kitchen       Paris 1789                          | |
|   |  Smoked fish   Nairobi 2301  Onion soup                          | |
|   |  & mead        Pan-African   & cassoulet                        | |
|   |               fusion                                             | |
|   +------------------------------------------------------------------+ |
|                                                                        |
+------------------------------------------------------------------------+
```

### Content Notes
- **Section title:** "LIFE ACROSS TIME" centered.
- **Subtitle:** Quote from Dean Ashcroft's convocation address.
- **Week timeline:** A compact horizontal timeline illustrating a sample
  week at Chronos. 4 key moments with brief descriptions. Visual is a
  dotted/solid line with node points.
- **Three-column highlights:**
  - **Clubs & Orgs:** List of 5-6 featured clubs with small icons. Include
    the motto/tagline if space allows. Link to "+6 more" for the full list.
  - **Traditions:** Key annual events: Arrival Day, Temporal Fair, Paradox
    Day, Lantern Send-Off, The Unmooring (graduation).
  - **Housing:** Three housing tiers: Temporal Pods, Era Dormitories (list
    the 7 dorm names), Host Family Immersion.
- **Dining row:** Horizontal scroll or grid of the 7 dining halls, each
  with a small food icon, name, era, and 1-2 signature dishes.
- **Data source:** From 05-student-life.md.

### Responsive Notes (Mobile)
- Week timeline becomes vertical (top-to-bottom).
- Three-column layout stacks to single column (Clubs, then Traditions,
  then Housing).
- Dining row becomes a horizontal scroll carousel on mobile.

### Interaction Notes
- **Week timeline:** Hovering/tapping a node expands a short tooltip with
  the full day description from the sample week.
- **Club items:** Hover highlights the club name and shows its motto in a
  tooltip or inline expansion.
- **Tradition items:** Hover or click reveals a 1-2 sentence description
  (e.g., "Every student writes a worry on a paper lantern and releases it.
  The lanterns vanish. It's beautiful.").
- **Dining icons:** Hover shows a small "food card" with description and
  the vibe note from the research doc. Consider a playful animation
  (steam rising from food icon, mead foaming, etc.).
- **Scroll animation:** Staggered fade-in. The week timeline animates its
  connecting line drawing left-to-right.

---

## Section 7: Apply / CTA

```
+------------------------------------------------------------------------+
|  ////////////////////////////////////////////////////////////////////  |
|  //                                                                //  |
|  //                                                                //  |
|  //         "ALL TIMES ARE ONE."                                   //  |
|  //                                                                //  |
|  //                                                                //  |
|  //         Begin your journey across time.                        //  |
|  //         Applications for Year-Cycle 28 are now open.           //  |
|  //                                                                //  |
|  //                                                                //  |
|  //              +-------------------------------+                 //  |
|  //              |        APPLY NOW              |                 //  |
|  //              |     (large primary CTA)       |                 //  |
|  //              +-------------------------------+                 //  |
|  //                                                                //  |
|  //              +-------------------------------+                 //  |
|  //              |   REQUEST MORE INFORMATION    |                 //  |
|  //              |     (secondary CTA)           |                 //  |
|  //              +-------------------------------+                 //  |
|  //                                                                //  |
|  //                                                                //  |
|  //  +----------------------------+  +---------------------------+ //  |
|  //  | [Icon: Clock]             |  | [Icon: Shield]            | //  |
|  //  | Applications close:       |  | The Temporal Oath         | //  |
|  //  | Spring Equinox, AR-28     |  | awaits your pledge.       | //  |
|  //  +----------------------------+  +---------------------------+ //  |
|  //                                                                //  |
|  //                                                                //  |
|  ////////////////////////////////////////////////////////////////////  |
+------------------------------------------------------------------------+
```

### Content Notes
- **Background:** Amber/gold gradient or a subtle animated texture
  reminiscent of the temporal aperture glow. Visually distinct from
  other sections to create a sense of urgency and culmination.
- **Headline:** "ALL TIMES ARE ONE." (the Academy motto / graduation
  phrase) in large, display-weight type. White or cream text on the
  amber background.
- **Subtext:** "Begin your journey across time." followed by an
  application cycle note.
- **Primary CTA:** "APPLY NOW" -- large, high-contrast button (dark
  background on gold, or gold on dark). Full-width on mobile.
- **Secondary CTA:** "REQUEST MORE INFORMATION" -- outlined button,
  lighter weight.
- **Info badges:** Two small info blocks below the CTAs:
  - Application deadline (themed to the in-world calendar).
  - A reference to the Temporal Oath to add emotional weight.
- **Tone:** This section should feel like an invitation, not a hard sell.
  The Academy is exclusive and prestigious but welcoming.

### Responsive Notes (Mobile)
- All content centers and stacks vertically.
- CTAs become full-width buttons.
- Info badges stack vertically.
- Background gradient/animation simplifies for performance.

### Interaction Notes
- **CTA buttons:** Primary button has a subtle pulsing glow effect
  (amber/gold). On hover, the glow intensifies and the button text
  shifts slightly (letter-spacing expands by 1px).
- **Scroll-triggered:** The section background gradient animates from
  dark to amber as the user scrolls into view, creating a "dawn" effect.
- **Parallax text:** The headline may have a slight parallax offset from
  the background for depth.
- **Optional:** A countdown timer to application deadline (if we want
  to add urgency). Style it with an analog clock aesthetic.

---

## Section 8: Footer

```
+------------------------------------------------------------------------+
|  ===================================================================== |
|                                                                        |
|   CHRONOS ACADEMY                                                      |
|   Thingvellir, Iceland | Est. 1953                                     |
|                                                                        |
|   +-----------------+  +------------------+  +---------------------+   |
|   | EXPLORE         |  | ACADEMICS        |  | STUDENT LIFE        |   |
|   | About / Origin  |  | Departments (6)  |  | Housing             |   |
|   | Campuses (8)    |  | Course Catalog   |  | Clubs               |   |
|   | Faculty         |  | Degree Programs  |  | Traditions          |   |
|   | The Meridian    |  | Core Curriculum  |  | Dining              |   |
|   | Governance      |  | Academic Calendar|  | The Temporal Oath   |   |
|   +-----------------+  +------------------+  +---------------------+   |
|                                                                        |
|   +-----------------+  +--------------------------------------------+  |
|   | CONNECT         |  |                                            |  |
|   | Apply           |  |  "Tempus docet. Nos discimus."             |  |
|   | Request Info    |  |   Time teaches. We learn.                   |  |
|   | Contact         |  |                                            |  |
|   | [Temporal       |  |  [Hourglass logo, small, centered]         |  |
|   |  Message Portal]|  |                                            |  |
|   +-----------------+  +--------------------------------------------+  |
|                                                                        |
|   -----------------------------------------------------------------    |
|   (c) Chronos Academy, Year-Cycle 28 (Absolute Reckoning)             |
|   All times are one.         [Back to Top arrow]                       |
|                                                                        |
+------------------------------------------------------------------------+
```

### Content Notes
- **Footer background:** Dark (near-black or deep navy), contrasting with
  the amber CTA section above. Subtle texture (basalt grain or bismuth
  crystal pattern at very low opacity).
- **Academy identity:** "CHRONOS ACADEMY" wordmark, location, founding year.
- **Link columns:** Four columns of in-page navigation links:
  - **Explore:** Links to About, Campuses, Faculty, The Meridian, Governance.
  - **Academics:** Links to Departments, Course Catalog, Degree Programs,
    Core Curriculum, Academic Calendar.
  - **Student Life:** Links to Housing, Clubs, Traditions, Dining,
    The Temporal Oath.
  - **Connect:** Apply, Request Info, Contact, "Temporal Message Portal"
    (a playful in-world name for a contact form).
- **Motto block:** The Academy motto in Latin and English, with the
  hourglass logo.
- **Copyright line:** In-world copyright using the Absolute Reckoning
  calendar system. "All times are one." as a sign-off.
- **Back to top:** Subtle arrow/button to scroll back to the hero.

### Responsive Notes (Mobile)
- Link columns stack vertically (accordions or stacked lists).
- Motto block remains centered.
- Copyright line wraps as needed.
- "Back to top" button becomes a floating action button (FAB) in the
  bottom-right corner, visible on all sections after scrolling past hero.

### Interaction Notes
- **Footer links:** Standard hover underline + color shift (text goes from
  muted gray to amber/gold on hover).
- **Back to top:** Smooth-scroll to top of page. Button has a subtle
  upward arrow animation on hover.
- **Logo:** On hover, the hourglass logo does a brief flip animation.
- **Temporal Message Portal link:** Opens a modal with a styled contact
  form. Form fields are playfully labeled (e.g., "Your Name (in this
  timeline):", "Your Era of Origin:", "Your Message:").

---

## Global Design Notes

### Navigation (Sticky Header)

```
+------------------------------------------------------------------------+
| [Logo]  About  Campuses  Faculty  Courses  Life  Apply     [hamburger] |
+------------------------------------------------------------------------+
```

- **Behavior:** After scrolling past the hero section, a sticky nav bar
  appears at the top with a semi-transparent dark background.
- **Links:** Each link scrolls smoothly to the corresponding section.
- **Active state:** The current section's link is underlined in amber/gold.
- **Mobile:** Collapses to hamburger menu. Opens a full-screen overlay
  with vertically stacked nav links.

### Color Palette (Reference)

| Role             | Color                      | Usage                         |
|------------------|----------------------------|-------------------------------|
| Primary          | Amber/Gold (#D4A017)       | CTAs, accents, active states  |
| Background Dark  | Deep Charcoal (#1A1A2E)    | Hero, footer, nav             |
| Background Light | Warm Ivory (#FAF3E0)       | Content sections              |
| Text Primary     | Off-White (#F5F5F0)        | On dark backgrounds           |
| Text Secondary   | Dark Slate (#2C2C3A)       | On light backgrounds          |
| Dept: TEMP       | Gold (#D4A017)             | Temporal Sciences badge       |
| Dept: PHIL       | Silver (#A8A8B8)           | Philosophy badge              |
| Dept: HIST       | Earth Brown (#8B6914)      | Historical Immersion badge    |
| Dept: DIPL       | Royal Purple (#7851A9)     | Diplomacy badge               |
| Dept: PARA       | Electric Blue (#4169E1)    | Paradox Sciences badge        |
| Dept: ARTL       | Magenta (#C71585)          | Arts & Culture badge          |

### Typography (Reference)

| Role            | Style                                                  |
|-----------------|--------------------------------------------------------|
| Display/Hero    | Serif display face (e.g., Playfair Display), uppercase |
| Section Heads   | Serif, large, sentence case                            |
| Body Text       | Clean sans-serif (e.g., Inter or Source Sans)          |
| Motto/Quotes    | Italic serif                                           |
| UI Elements     | Sans-serif, medium weight, slightly letter-spaced      |
| Course Codes    | Monospace (e.g., JetBrains Mono)                       |

### Animation & Performance Notes

- All scroll-triggered animations use `IntersectionObserver` for performance.
- Animations respect `prefers-reduced-motion` media query. Users with
  motion sensitivity get instant transitions instead of animations.
- Parallax effects are GPU-accelerated (transform-based, not scroll-event).
- Image loading uses `loading="lazy"` for all below-the-fold images.
- Target page weight: under 3MB total (with optimized images).
- Target Lighthouse performance score: 90+.

### Accessibility Notes

- All interactive elements are keyboard-navigable.
- Color contrast ratios meet WCAG AA minimum (4.5:1 for text).
- Images have descriptive alt text.
- Section headings use proper semantic hierarchy (h1 > h2 > h3).
- ARIA labels on interactive components (tabs, modals, carousels).
- Skip-to-content link at top of page for screen reader users.

---

*This wireframe document serves as the layout and interaction specification
for the Chronos Academy single-page website. It is a design artifact only.
No code has been written.*

*Designed by the Red-Orange Designer Agent for Octopus multi-agent orchestration.*
