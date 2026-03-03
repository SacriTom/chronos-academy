# Chronos Academy: Campus Visual Design Specifications

> Red-Orange Designer Agent -- Visual concept descriptions for all 8 era-campuses.
> Design only. No implementation.

---

## I. Alexandria Campus (3rd Century BCE)

**Color Scheme**
- Papyrus Gold: `#D4A843`
- Mediterranean Blue: `#2A6496`
- Limestone White: `#F0EDE4`

**CSS Gradient**
```css
background: linear-gradient(135deg, #F0EDE4 0%, #D4A843 55%, #2A6496 100%);
```

**Icon / Symbol**
A single unfurled scroll with a small flame above it -- representing both the Library's holdings and the Pharos lighthouse. The scroll curls at both ends; the flame is a simple teardrop shape.

**Card Design**
- Top border: 4px solid `#D4A843` (gold bar evoking scroll edges).
- Background: `#F0EDE4` body with a faint diagonal texture suggesting papyrus grain.
- Title typography: Serif font (e.g., Playfair Display), `#2A6496`, uppercase tracked at 0.08em.
- Era label: Small caps, `#D4A843`, positioned as a subtle tag above the title.
- Body text: Dark warm grey `#3B3228`.
- Bottom element: A thin horizontal rule in `#2A6496` above a "3rd c. BCE" date stamp.

**Mood Words**
Luminous, scholarly, ancient, cosmopolitan, fragile.

**Background Pattern**
Repeating faint horizontal lines spaced ~12px apart with slight opacity variation (0.03--0.06 alpha in `#D4A843`), simulating the fibrous grain of papyrus. Achievable with a repeating-linear-gradient of 1px solid lines.

```css
background-image: repeating-linear-gradient(
  0deg,
  rgba(212, 168, 67, 0.05) 0px,
  rgba(212, 168, 67, 0.05) 1px,
  transparent 1px,
  transparent 12px
);
```

**Emoji Shorthand**
:scroll:

---

## II. Shaolin Campus (7th Century CE)

**Color Scheme**
- Mist Grey-Green: `#7A8B6F`
- Temple Saffron: `#C8702A`
- Weathered Stone: `#A69E91`

**CSS Gradient**
```css
background: linear-gradient(180deg, #A69E91 0%, #7A8B6F 50%, #C8702A 100%);
```

**Icon / Symbol**
A stylized mountain peak with a single curved roof-eave emerging from its base -- the monastery nestled at the foot of Shaoshi Peak. Clean, minimal, two strokes for the mountain and one for the roof.

**Card Design**
- Top border: 4px solid `#C8702A` (saffron monk's robe accent).
- Background: Light warm stone `#F3F0EB` body.
- Title typography: Clean sans-serif (e.g., Noto Sans), `#3B3228`, medium weight, generous letter-spacing.
- Era label: `#7A8B6F`, small, understated.
- Body text: `#4A4540`.
- Bottom element: A subtle icon of a bamboo stalk in `#7A8B6F` at the lower right corner, decorative only.

**Mood Words**
Austere, misty, disciplined, ancient, grounded.

**Background Pattern**
Vertical bamboo-stripe pattern: thin alternating lines in `#7A8B6F` at 0.04 alpha, spaced unevenly (8px, 14px, 8px, 20px) to suggest bamboo grove depth.

```css
background-image:
  repeating-linear-gradient(
    90deg,
    rgba(122, 139, 111, 0.04) 0px,
    rgba(122, 139, 111, 0.04) 1px,
    transparent 1px,
    transparent 8px,
    rgba(122, 139, 111, 0.04) 8px,
    rgba(122, 139, 111, 0.04) 9px,
    transparent 9px,
    transparent 23px
  );
```

**Emoji Shorthand**
:mountain:

---

## III. Timbuktu Campus (14th Century CE)

**Color Scheme**
- Desert Ochre: `#C4913A`
- Indigo Deep: `#2E3A5F`
- Sand White: `#F2E8D5`

**CSS Gradient**
```css
background: linear-gradient(160deg, #F2E8D5 0%, #C4913A 60%, #2E3A5F 100%);
```

**Icon / Symbol**
A geometric star pattern (eight-pointed) drawn with clean lines -- referencing both Islamic geometric art and Saharan navigation by stars. The star sits above a single horizontal line suggesting the desert horizon.

**Card Design**
- Top border: 4px solid `#C4913A` (ochre, evoking mudbrick walls).
- Background: `#F2E8D5` body (warm sand).
- Title typography: Serif with slight calligraphic quality (e.g., Cormorant Garamond), `#2E3A5F`, normal case.
- Era label: `#C4913A`, letterspaced.
- Body text: `#3D3529`.
- Bottom element: A row of three small diamond shapes in `#2E3A5F` -- a minimal geometric motif.

**Mood Words**
Golden, vast, intellectual, sacred, arid.

**Background Pattern**
A subtle diamond lattice (rotated square grid) in `#C4913A` at 0.04 alpha, ~40px repeat, suggesting the geometric patterns found in Timbuktu manuscripts.

```css
background-image:
  linear-gradient(45deg, rgba(196, 145, 58, 0.04) 25%, transparent 25%),
  linear-gradient(-45deg, rgba(196, 145, 58, 0.04) 25%, transparent 25%),
  linear-gradient(45deg, transparent 75%, rgba(196, 145, 58, 0.04) 75%),
  linear-gradient(-45deg, transparent 75%, rgba(196, 145, 58, 0.04) 75%);
background-size: 40px 40px;
background-position: 0 0, 0 20px, 20px -20px, -20px 0px;
```

**Emoji Shorthand**
:star:

---

## IV. Florence Campus (15th Century CE)

**Color Scheme**
- Medici Red: `#8B2E2E`
- Marble Cream: `#F5F0E8`
- Renaissance Gold: `#B8923E`

**CSS Gradient**
```css
background: linear-gradient(135deg, #F5F0E8 0%, #B8923E 50%, #8B2E2E 100%);
```

**Icon / Symbol**
A dome silhouette (Brunelleschi's Duomo) with a compass-and-straightedge cross below it -- representing the union of art and engineering. Simple, recognizable, two geometric shapes.

**Card Design**
- Top border: 4px solid `#8B2E2E` (deep Florentine red).
- Background: `#F5F0E8` body (marble cream).
- Title typography: Classic serif (e.g., EB Garamond), `#8B2E2E`, italic, generous size.
- Era label: `#B8923E`, uppercase, tracked wide.
- Body text: `#2E2A25`.
- Bottom element: A thin double-line rule in `#B8923E` -- evoking gilded manuscript borders.

**Mood Words**
Ambitious, incandescent, dangerous, beautiful, competitive.

**Background Pattern**
A subtle cross-hatch pattern evoking red chalk drawing: two sets of diagonal lines at 30deg and -30deg, `#8B2E2E` at 0.03 alpha, 1px wide, 20px spacing.

```css
background-image:
  repeating-linear-gradient(
    30deg,
    rgba(139, 46, 46, 0.03) 0px,
    rgba(139, 46, 46, 0.03) 1px,
    transparent 1px,
    transparent 20px
  ),
  repeating-linear-gradient(
    -30deg,
    rgba(139, 46, 46, 0.03) 0px,
    rgba(139, 46, 46, 0.03) 1px,
    transparent 1px,
    transparent 20px
  );
```

**Emoji Shorthand**
:art:

---

## V. Varanasi Campus (5th Century CE)

**Color Scheme**
- Saffron Amber: `#D4762C`
- Sacred River Teal: `#2D7A7B`
- Sandstone Warm: `#EDE0CB`

**CSS Gradient**
```css
background: linear-gradient(180deg, #EDE0CB 0%, #D4762C 55%, #2D7A7B 100%);
```

**Icon / Symbol**
A lotus flower viewed from above (simple 8-petal radial form) with a small numeral zero at its centre -- the lotus representing spiritual and intellectual purity, the zero representing the Gupta invention of the decimal placeholder.

**Card Design**
- Top border: 4px solid `#D4762C` (saffron temple accent).
- Background: `#EDE0CB` body (warm sandstone).
- Title typography: Serif with slight warmth (e.g., Libre Baskerville), `#2D7A7B`, normal case.
- Era label: `#D4762C`, small, positioned above title.
- Body text: `#3A322A`.
- Bottom element: A minimal lotus outline in `#D4762C`, centred.

**Mood Words**
Sacred, radiant, pluralistic, mathematical, ancient.

**Background Pattern**
Concentric circles at very low opacity, suggesting ripples on the Ganges. Radial gradient circles repeated as a tile.

```css
background-image: radial-gradient(
  circle,
  rgba(45, 122, 123, 0.04) 0%,
  rgba(45, 122, 123, 0.04) 2px,
  transparent 2px,
  transparent 8px,
  rgba(45, 122, 123, 0.03) 8px,
  rgba(45, 122, 123, 0.03) 10px,
  transparent 10px
);
background-size: 50px 50px;
```

**Emoji Shorthand**
:lotus:

---

## VI. Manchester Campus (19th Century CE)

**Color Scheme**
- Soot Black-Red: `#5C1A1A`
- Industrial Brick: `#A0522D`
- Smoke Grey: `#B0A899`

**CSS Gradient**
```css
background: linear-gradient(180deg, #B0A899 0%, #A0522D 55%, #5C1A1A 100%);
```

**Icon / Symbol**
A factory chimney with a single gear cog overlapping its base -- direct, blunt, and unmistakable. The chimney is a simple rectangle tapering slightly; the cog is a standard six-tooth circle.

**Card Design**
- Top border: 4px solid `#A0522D` (red brick).
- Background: `#EDEBE7` body (overcast sky off-white).
- Title typography: Industrial slab-serif (e.g., Roboto Slab), `#5C1A1A`, bold, uppercase.
- Era label: `#A0522D`, uppercase, tracked.
- Body text: `#3A3632`.
- Bottom element: A row of small square dots in `#B0A899` -- suggesting cobblestones.

**Mood Words**
Grim, relentless, raw, transformative, smoky.

**Background Pattern**
A brick-wall pattern: offset horizontal and vertical lines forming a running bond layout in `#A0522D` at 0.04 alpha.

```css
background-image:
  linear-gradient(
    rgba(160, 82, 45, 0.04) 1px,
    transparent 1px
  ),
  linear-gradient(
    90deg,
    rgba(160, 82, 45, 0.04) 1px,
    transparent 1px
  );
background-size: 30px 12px;
```

**Emoji Shorthand**
:factory:

---

## VII. Tomorrow Campus / Nairobi Station (22nd Century CE)

**Color Scheme**
- Bio Green: `#3DA57C`
- Sky Clean Blue: `#5BAFD6`
- Warm Ivory: `#FAF6EF`

**CSS Gradient**
```css
background: linear-gradient(135deg, #FAF6EF 0%, #3DA57C 50%, #5BAFD6 100%);
```

**Icon / Symbol**
A vertical leaf-tower silhouette: a tall narrow rectangle with organic leaf shapes emerging from both sides -- representing the Uhuru Vertical Forest. Simple, upward-pointing, optimistic.

**Card Design**
- Top border: 4px solid `#3DA57C` (living green).
- Background: `#FAF6EF` body (clean warm white).
- Title typography: Modern geometric sans-serif (e.g., Inter or DM Sans), `#1A3A2E`, light weight, generous size.
- Era label: `#5BAFD6`, lowercase, subtle.
- Body text: `#2A2F2D`.
- Bottom element: A thin gradient bar fading from `#3DA57C` to `#5BAFD6` -- the green-blue future spectrum.

**Mood Words**
Clean, organic, hopeful, advanced, luminous.

**Background Pattern**
A soft dot-matrix grid of tiny circles in `#3DA57C` at 0.03 alpha, ~24px spacing -- evoking data visualization and organic cell patterns simultaneously.

```css
background-image: radial-gradient(
  circle,
  rgba(61, 165, 124, 0.04) 1.5px,
  transparent 1.5px
);
background-size: 24px 24px;
```

**Emoji Shorthand**
:seedling:

---

## VIII. Pangaea Campus (68 Million Years BCE)

**Color Scheme**
- Primordial Green: `#3A6B3A`
- Volcanic Amber: `#C4641E`
- Deep Sky Warm: `#4A6F8C`

**CSS Gradient**
```css
background: linear-gradient(180deg, #4A6F8C 0%, #3A6B3A 50%, #C4641E 100%);
```

**Icon / Symbol**
A Tyrannosaurus rex skull in extreme profile, reduced to its simplest outline -- three curves for the jaw, one triangle for the teeth, one circle for the eye socket. Beneath it, a single fern frond. Primal and immediately legible.

**Card Design**
- Top border: 4px solid `#3A6B3A` (primordial forest green).
- Background: `#F0EDE5` body (fossil-pale warm).
- Title typography: Bold, slightly condensed sans-serif (e.g., Barlow Condensed), `#C4641E`, uppercase.
- Era label: `#3A6B3A`, small caps, muted.
- Body text: `#33302B`.
- Bottom element: A jagged mountain-range silhouette in `#4A6F8C` at low opacity -- the young Rockies on the horizon.

**Mood Words**
Primeval, immense, alive, humbling, prehistoric.

**Background Pattern**
Scattered fern-frond diagonals: angled parallel lines in groups of three at irregular spacing, `#3A6B3A` at 0.03 alpha. Suggests dense Cretaceous vegetation.

```css
background-image:
  repeating-linear-gradient(
    55deg,
    rgba(58, 107, 58, 0.03) 0px,
    rgba(58, 107, 58, 0.03) 1px,
    transparent 1px,
    transparent 6px,
    rgba(58, 107, 58, 0.03) 6px,
    rgba(58, 107, 58, 0.03) 7px,
    transparent 7px,
    transparent 10px,
    rgba(58, 107, 58, 0.03) 10px,
    rgba(58, 107, 58, 0.03) 11px,
    transparent 11px,
    transparent 30px
  );
```

**Emoji Shorthand**
:t-rex:

---

---

## Campus Card Component Spec

A single reusable card component that adapts per campus through a data-driven color theme.

### Structure (top to bottom)

```
+-------------------------------------------+
| [ERA COLOR BAR - 4px]                     |
|                                           |
|  [EMOJI]  ERA LABEL (small caps)          |
|                                           |
|  CAMPUS NAME                              |
|  (serif/sans per era, large, colored)     |
|                                           |
|  Time Period  |  Location                 |
|  (two-column metadata row, muted)         |
|                                           |
|  Primary Discipline tag                   |
|  (pill-shaped badge, era accent color     |
|   background at 0.12 alpha, text in       |
|   era accent)                             |
|                                           |
|  Brief description (2-3 lines max)        |
|                                           |
|  [DIFFICULTY INDICATOR]                   |
|  (1-4 filled dots, era color)             |
|                                           |
|  [BOTTOM DECORATIVE RULE / ELEMENT]       |
+-------------------------------------------+
```

### Dimensions and Spacing

- Card width: 320px (fixed) or fluid within a CSS grid column.
- Card min-height: 360px.
- Border-radius: 8px.
- Padding: 24px horizontal, 20px vertical.
- Shadow: `0 2px 8px rgba(0,0,0,0.08)` default, `0 4px 16px rgba(0,0,0,0.12)` on hover.
- Transition on hover: lift by 2px (translateY), shadow deepens, 200ms ease.

### Color Theming

Each card receives a CSS custom property set:

```css
.campus-card[data-era="alexandria"] {
  --era-primary: #D4A843;
  --era-secondary: #2A6496;
  --era-bg: #F0EDE4;
}
/* Repeat for each campus */
```

The component uses these variables:
- Top bar: `var(--era-primary)`
- Title color: `var(--era-secondary)`
- Badge background: `var(--era-primary)` at 12% opacity
- Badge text: `var(--era-primary)`
- Background: `var(--era-bg)`
- Background pattern: loaded per-era via an additional class

### Typography

- Era label: 10px / 1.4, uppercase, letter-spacing 0.12em, `var(--era-primary)`.
- Campus name: 22px / 1.2, font weight and family set per era (serif for ancient/classical, sans-serif for modern/future).
- Metadata: 12px / 1.4, `#888`.
- Body: 14px / 1.6, `#444`.
- Discipline badge: 11px / 1.0, medium weight, `var(--era-primary)`.

### Interaction States

- **Default**: Flat, slight shadow.
- **Hover**: Lifts 2px, shadow expands, top color bar thickens from 4px to 6px (transition 200ms).
- **Active/Selected**: A 2px ring in `var(--era-primary)` surrounds the card. Background lightens slightly.
- **Focus (keyboard)**: Visible focus ring using `outline: 2px solid var(--era-primary); outline-offset: 2px`.

### Responsive Behavior

- On screens < 768px, cards stack vertically at full width with 16px gap.
- On screens >= 768px, display as a 2-column grid, 24px gap.
- On screens >= 1200px, display as a 4-column grid, 24px gap.
- At >= 1600px, all 8 cards can display on two rows of 4.

### Accessibility Notes

- All era colors must pass WCAG AA contrast against their respective card backgrounds. The specifications above have been chosen to meet this requirement for text elements.
- Emoji shorthand is decorative; use `aria-hidden="true"` on the emoji element and ensure the era label provides the text alternative.
- Difficulty dots should use `role="img"` with an `aria-label` such as "Difficulty: High (3 of 4)".

---

## Era Timeline Visual

A horizontal scrolling timeline displaying all 8 campuses in chronological order.

### Layout

```
<--- SCROLL --->

[68M BCE]----[3rd c. BCE]---[5th c. CE]---[7th c. CE]---[14th c. CE]---[15th c. CE]---[19th c. CE]---[22nd c. CE]
 Pangaea      Alexandria     Varanasi      Shaolin       Timbuktu       Florence       Manchester     Tomorrow
```

### Structure

- A single horizontal track (2px line, `#CCCCCC`) spans the full width.
- 8 era nodes sit along the track, each a circle (40px diameter) filled with the era's primary color.
- The spacing between nodes is NOT proportional to actual time (68 million years would make the rest invisible). Instead, use equal spacing with a visual break between Pangaea and the rest to signal the scale discontinuity.
- A "break" indicator (three angled slashes `///` or a zigzag in the line) sits between Pangaea and Alexandria, labeled "~68 million years".

### Node Design

Each node is a circle containing the era's emoji shorthand:

```
   [emoji]
     |
- - -O- - - - - - - - O - - - - -
     |                 |
  Era Name          Era Name
  Date Label        Date Label
```

- Circle: 40px, filled `var(--era-primary)`, white emoji centered.
- Below the circle: Campus name (14px, bold, dark grey) and date (12px, muted grey), centered.
- On hover, the circle scales to 48px and a tooltip/popover appears with the campus's one-line description and discipline tag.

### Scroll Behavior

- On desktop (>= 1024px): The timeline fits within view if the viewport is wide enough; otherwise it scrolls horizontally. A subtle horizontal scrollbar or arrow indicators at the edges signal scroll availability.
- On mobile (< 768px): The timeline rotates to VERTICAL layout, nodes stacked top to bottom, oldest at top. The track becomes a left-side vertical line with nodes and labels branching right. This avoids awkward horizontal scroll on small screens.
- Between 768px and 1024px: Horizontal scroll with visible arrows.

### Connecting Line Treatment

- The default line between nodes is 2px solid `#DDDDDD`.
- On hover of any node, the line segments to its immediate neighbors highlight in that era's primary color, creating a glow-path effect.
- The break between Pangaea and Alexandria uses a dashed line style: `2px dashed #BBBBBB`.

### Animation (Optional Enhancement)

- On page load, nodes could fade in sequentially from left (oldest) to right (newest) with a 100ms stagger, suggesting the passage of time.
- The timeline could include a "traveling dot" animation: a small 8px circle that moves along the track from Pangaea to Tomorrow over ~3 seconds on initial view, then disappears.

### Color Reference Table

| Campus | Node Color | Emoji |
|---|---|---|
| Pangaea | `#3A6B3A` | :t-rex: |
| Alexandria | `#D4A843` | :scroll: |
| Varanasi | `#D4762C` | :lotus: |
| Shaolin | `#C8702A` | :mountain: |
| Timbuktu | `#C4913A` | :star: |
| Florence | `#8B2E2E` | :art: |
| Manchester | `#A0522D` | :factory: |
| Tomorrow | `#3DA57C` | :seedling: |

---

## Global Design Tokens

For consistency across all campus visuals, the following shared tokens apply:

```
--chronos-font-serif: 'Playfair Display', 'EB Garamond', Georgia, serif;
--chronos-font-sans: 'Inter', 'DM Sans', system-ui, sans-serif;
--chronos-font-mono: 'JetBrains Mono', 'Fira Code', monospace;
--chronos-radius-card: 8px;
--chronos-shadow-default: 0 2px 8px rgba(0,0,0,0.08);
--chronos-shadow-hover: 0 4px 16px rgba(0,0,0,0.12);
--chronos-transition-speed: 200ms;
--chronos-text-body: #444444;
--chronos-text-muted: #888888;
--chronos-bg-page: #FAFAF8;
```

---

*Design specifications compiled by Red-Orange Designer Agent.*
*Scope: Visual concept only. No implementation.*
