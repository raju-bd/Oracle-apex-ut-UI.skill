# Oracle APEX Universal Theme skill — Single-File Bundle
> **This is a single-file, all-in-one version of the skill.** Everything that normally
> lives across `SKILL.md`, `components-reference.md`, and the `tokens/` folder is inlined
> below as labeled code blocks. Upload or paste *just this one file* into any AI
> (Claude, ChatGPT, Gemini, a Claude Project, a Cursor rules file, etc.) and it has the
> complete Oracle APEX Universal Theme 42 (Vita) design-token reference — no separate
> file uploads needed.
>
> For a browser/dev environment instead of an AI, use the companion single-file bundle
> `Oracle-apex-ut-UI.skill.bundle.js` — one `<script>` tag, no separate CSS requests.
>
> Generated from Oracle-apex-ut-UI.skill · https://github.com/raju-bd/Oracle-apex-ut-UI.skill

---
## Table of contents
1. [`SKILL.md`](#part-1-skillmd)
2. [`components-reference.md`](#part-2-components-referencemd)
3. [`tokens/vita-light.css`](#part-3-tokensvita-lightcss)
4. [`tokens/vita-dark.css`](#part-4-tokensvita-darkcss)
5. [`tokens/vita-red.css`](#part-5-tokensvita-redcss)
6. [`tokens/vita-slate.css`](#part-6-tokensvita-slatecss)
7. [`tokens/iris.css`](#part-7-tokensiriscss)
8. [`tokens/redwood.css`](#part-8-tokensredwoodcss)
9. [`tokens/standard.css`](#part-9-tokensstandardcss)
10. [`tokens/vita-emerald.less`](#part-10-tokensvita-emeraldless)
11. [`tokens/vita-emerald.css`](#part-11-tokensvita-emeraldcss)

---

## Part 1: `SKILL.md`

---
name: oracle-apex-ut-ui
description: "Use this skill whenever the user wants to generate, style, or reference HTML/CSS that matches Oracle APEX's Universal Theme 42 design system (Vita, Vita Dark, Vita Red, Vita Slate, Iris, Redwood, or Standard Theme Styles). Triggers include: any mention of 'Oracle APEX', 'APEX theme', 'Universal Theme', 'Vita', 'Vita Emerald', 'Theme Roller', 'APEX region/component' (Alert, Card, Interactive Report, Wizard, etc.), or requests to build a dashboard, admin UI, or component that should 'look like APEX' or use APEX design tokens. Also use when asked to create a new custom APEX Theme Style, when styling should use var(--ut-*) / var(--a-*) CSS custom properties instead of hardcoded colors, or when working with files under tokens/ (vita-light.css, vita-dark.css, vita-red.css, vita-slate.css, iris.css, redwood.css, standard.css, vita-emerald.css/.less) or components-reference.md from this package. Do NOT use for generic web design requests with no APEX/Universal Theme context."
license: MIT — see LICENSE in this repository. Oracle APEX and Universal Theme 42 remain Oracle's property; token values here are an independent, hand-derived reference.
---

# Oracle APEX Universal Theme skill

*(Package / repo slug: `Oracle-apex-ut-UI.skill`)*

**Purpose:** A pre-reference package any AI (Claude, GPT, Gemini, local LLM, etc.) can be
given so it produces HTML/CSS/layouts that visually and structurally match Oracle APEX's
Universal Theme 42, "Vita" style family — without needing an actual APEX instance.

**Source of truth (official, live):**
- Getting Started / live component gallery: `https://oracleapex.com/ords/r/apex_pm/ut/getting-started`
- Theme Style LESS sources (Oracle CDN, APEX 26.1 / Theme 42 26.1):
  - Vita (light, default): `https://static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/less/theme/Vita.less`
  - Vita Dark: `https://static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/less/theme/Vita-Dark.less`
  - Vita Red: `https://static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/less/theme/Vita-Red.less`
  - Vita Slate: `https://static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/less/theme/Vita-Slate.less`
  - Iris: `https://static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/less/theme/Iris.less`
  - Redwood: `https://static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/less/theme/Redwood.less` and `Redwood-Theme.less`
  - Legacy Theme Standard (pre-Theme-42, different architecture): `https://static.oracle.com/cdn/apex/26.1.2/app_ui/css/Core.css` and `Theme-Standard.css`
  - Icon font: `https://static.oracle.com/cdn/apex/26.1.2/libraries/font-apex/2.5.1/css/font-apex.css`
  - Theme JS (sticky widgets, nav behavior): `https://static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/js/theme42.js`, `https://static.oracle.com/cdn/apex/26.1.2/libraries/apex/minified/widget.stickyWidget.min.js`

Keep those four links handy — they are the canonical, always-current definition. This
skill distills them into something usable directly in a browser (plain CSS custom
properties) plus a class/component cheat-sheet, because the .less files require Oracle's
build pipeline (Theme Roller) to compile correctly (they use LESS functions like
`contrast()`, `mix()`, `desaturate()`, `fade()` and an override pattern that only resolves
correctly inside APEX's own LESS compiler).

---

## 1. How Vita's token system actually works

Universal Theme 42 is a **two-layer CSS variable system**:

1. **`--a-*` variables** — low-level "Application UI" component tokens (buttons, cards,
   checkboxes, menus, grid views, chips, dialogs, spinners, etc.). These rarely change
   between Theme Styles; they define spacing, sizing, radii, font-sizes.
2. **`--ut-*` variables** — "Universal Theme" tokens that carry the actual *brand identity*
   (header color, region color, body background, primary palette, shadows, borders). These
   are what changes between Vita / Vita Dark / Vita Red / Vita Slate / your own custom style.
3. A small set of **`@g_*` LESS "Theme Roller" variables** are the *only* things a human
   (or Theme Roller) edits. Everything else is derived from them via LESS color functions
   (`contrast`, `mix`, `lighten`, `darken`, `desaturate`, `fade`). This is the mechanism
   used to create "a new style to the same standard" — see §4.

### Golden rule for any AI generating Vita-style UI
Never hard-code colors in component markup. Always reference the CSS custom property
(e.g. `var(--ut-palette-primary)`, `var(--a-button-background-color)`), the same way real
APEX-rendered pages do. That's what makes the output swappable across Vita / Vita Dark /
Vita Red / Vita Slate / a custom style just by swapping the `:root` block.

---

## 2. Core token map (Vita — light, default)

Use `tokens/vita-light.css` in this package — a ready-to-`<link>` (or inline `<style>`)
stylesheet containing the full resolved `:root { --ut-...; --a-...; }` variable set for
baseline Vita. Load it first, then layer component CSS on top using `var(--token-name)`.

Key tokens an AI will reach for constantly:

| Token | Meaning | Vita (light) value |
|---|---|---|
| `--ut-palette-primary` | Brand accent / primary action color | `#056AC8` |
| `--ut-palette-primary-contrast` | Text color on primary | `#FFFFFF` |
| `--ut-header-background-color` | Top header bar | `#056AC8` |
| `--ut-header-text-color` | Header text/icons | `#FFFFFF` |
| `--ut-body-background-color` | Page background | `#FDFDFD` |
| `--ut-body-text-color` | Default body text | `#1A1A1A` |
| `--ut-region-background-color` | Card/region surface | `#FFFFFF` |
| `--ut-region-header-background-color` | Region title bar | `#F7FBFF` |
| `--ut-component-border-color` | Generic hairline border | `rgba(0,0,0,.10)` |
| `--ut-component-border-radius` | Corner radius (regions/cards) | `.25rem` (4px) |
| `--ut-shadow-sm` / `--ut-shadow-md` / `--ut-shadow-lg` | Elevation shadows | see file |
| `--ut-palette-success` / `-warning` / `-danger` / `-info` | Status colors | `#278701` / `#FFC628` / `#CB1100` / `#056AC8` |
| `--ut-link-text-color` | Hyperlink color | `#056AC8` |
| `--ut-focus-outline-color` | Focus ring | `#056AC8` |
| `--a-button-background-color` | Default button fill | `#F0F0F0`-ish (mixed with region bg) |
| `--a-button-border-radius` | Button corner radius | `.125rem` (2px) |
| `--a-button-padding-y` / `-x` | Button padding | `.5rem .75rem` |
| `--a-field-input-border-radius` | Input corner radius | `.125rem` |
| `--a-field-input-background-color` | Input fill | slightly tinted off-white |
| `--ut-nav-width` | Left nav tree width | `15rem` |
| `--ut-header-height` | Header bar height | `3rem` |

Full list (300+ tokens covering buttons, cards, chips, checkboxes, date pickers, faceted
search, file drop, grid view, menus, popup LOV, splitter, star rating, switches, toolbars,
tree view, dialogs, tooltips, diagrams, chat, QR code, calendar, etc.) is in
`tokens/vita-light.css`.

---

## 3. Component class cheat-sheet (Universal Theme 42 naming conventions)

When generating markup, use these real APEX class prefixes so the HTML is structurally
authentic (and portable back into an actual APEX page template):

- `t-Body`, `t-Body-nav`, `t-Body-content`, `t-Body-actions` — page shell
- `t-Header`, `t-Header-logo`, `t-Header-nav`, `t-Header-search` — top bar
- `t-Region`, `.t-Region--card`, `.t-Region-header`, `.t-Region-headerItems`,
  `.t-Region-body`, `.t-Region-buttons` — region/card container
- `t-Button`, `.t-Button--hot`, `.t-Button--warning`, `.t-Button--success`,
  `.t-Button--danger`, `.t-Button--primary`, `.t-Button--simple`, `.t-Button--link`,
  `.t-Button--noUI`, `.t-Button--header`, `.t-Button--icon` — buttons & states
- `t-Alert`, `.t-Alert--success`, `.t-Alert--warning`, `.t-Alert--danger`, `.t-Alert--info` — alerts
- `t-Badge` — status pill
- `t-Form-fieldContainer`, `t-Form-label`, `t-Form-inputContainer`,
  `apex-item-text`, `apex-item-select`, `apex-item-textarea` — form items
- `t-Card`, `a-CardView`, `.a-CardView-card`, `.a-CardView-title`,
  `.a-CardView-icon` — card views
- `t-Report`, `a-IRR`, `t-Report-header`, `t-Report-wrap` — interactive reports
- `t-TreeView`, `a-TreeView`, `.a-TreeView-content` — nav tree / hierarchy widgets
- `t-Breadcrumb`, `t-Breadcrumb-item` — breadcrumbs
- `t-Tabs`, `.t-Tabs-item`, `.is-active` — tabs
- `t-Dialog`/`ui-dialog` — modal dialogs (jQuery UI-based)
- `t-WizardProgress` — wizard step indicator
- `a-Icon`, `fa-*` / `icon-*` — icon font hooks

Full markup patterns and working examples of each are in `components-reference.md`.

---

## 4. Making "a new style to the same standard" (custom Theme Style)

Oracle's own approach (see `Vita-Red.less`) is deliberately minimal: **override only 5–10
of the `@g_*` "Theme Roller" LESS variables at the top of the file**, then re-import the
base Vita file. Everything else (buttons, forms, IRs, shadows, states, spacing) cascades
automatically from those few variables via LESS color math. That is the "standard" to
replicate for a new style.

The variables that matter, in order of visual impact:

```less
@g_Accent-BG:        #0E9F6E;  // primary brand color — drives header, links, focus ring,
                                 // hot buttons, primary state, nav accent, badges
@g_Link-Base:         @g_Accent-BG;  // hyperlink color (often left = accent)
@g_Focus:             @g_Accent-BG;  // focus ring color
@g_Nav_Style:          dark;    // 'dark' or 'light' left nav / header menu
@g_Body-Title-BG:      #ffffff; // breadcrumb/title bar background (optional)
@g_Container-BorderRadius: .375rem; // region/card corner radius
@g_Button-BorderRadius:    .375rem; // button corner radius
@g_Form-BorderRadius:      .375rem; // input corner radius
```

This package includes a working example new style: **"Vita Emerald"**
(`tokens/vita-emerald.less` + a browser-ready `tokens/vita-emerald.css`), built exactly
the way `Vita-Red.less` is built — an emerald/teal accent (`#0E9F6E`), same navigation and
layout mechanics as base Vita, slightly more rounded corners (6px vs Oracle's default 2–4px)
for a softer, modern feel.

**To use it for real inside APEX:** paste `vita-emerald.less` into
*Theme Roller → Style → (create new / edit custom LESS)*, or add it as a new Theme Style's
custom LESS file, then let APEX's Theme Roller compile it — that guarantees pixel-perfect,
fully-computed colors (contrast-checked automatically by Oracle's `contrast()` function).

**To use it outside APEX (plain HTML/CSS, prototypes, other AI tools):** load
`tokens/vita-emerald.css` — the colors have been pre-resolved by hand following the same
LESS math Oracle uses (`contrast`, `mix`, `desaturate`, `darken`/`lighten`), so it's ready
to `<link>` directly with no build step. Treat it as a close approximation for prototyping;
re-verify exact hex values against Theme Roller before shipping to production.

---

## 5. Recommended workflow for an AI given only this skill

1. Load `tokens/vita-light.css` (or `vita-dark.css` / `vita-red.css` / `vita-emerald.css`)
   as the `:root` variable layer.
2. Build markup using the class names in §3 / `components-reference.md`.
3. Style everything with `var(--token-name)` — never literal hex codes — so the same
   markup automatically re-skins if the `:root` block is swapped.
4. For anything not covered (a token that doesn't exist yet), fall back to the nearest
   semantically-equivalent `--ut-component-*` or `--a-*` token rather than inventing a new
   hardcoded color, to stay consistent with the design system.
5. When asked for "a new style", follow §4: pick a new `@g_Accent-BG` (and optionally
   radius/nav-style), derive the rest the same way `vita-emerald.css` does, rather than
   redesigning the whole system from scratch.

---

## 6. Files in this package

```
Oracle-apex-ut-UI.skill/
├── SKILL.md                       ← this file
├── components-reference.md        ← class names + markup patterns + usage notes
├── example.html                   ← live demo: header, nav, region/cards, buttons,
│                                     alerts, badges, form, table — using the tokens
├── docs/                          ← GitHub Pages landing/demo site (see repo README)
└── tokens/
    ├── vita-light.css             ← baseline Vita (light) — full resolved token set
    ├── vita-dark.css              ← Vita Dark deltas (official)
    ├── vita-red.css               ← Vita Red deltas (official)
    ├── vita-slate.css             ← Vita Slate deltas (official)
    ├── iris.css                   ← Iris deltas (official, Redwood-family "Sky" pillar)
    ├── redwood.css                ← Redwood deltas (official, flagship design system)
    ├── standard.css                ← Legacy Theme Standard — best-effort approximation only
    ├── vita-emerald.less           ← NEW custom style, Oracle Theme-Roller-ready LESS source
    └── vita-emerald.css            ← NEW custom style, browser-ready resolved tokens
```

All delta files (everything except `vita-light.css` and the `vita-emerald.*` pair) load
**after** `vita-light.css` and only override what changes for that style — same markup,
different `:root` values. `standard.css` is the one exception: it approximates a
pre-Theme-42 legacy theme that doesn't actually share Theme 42's token architecture, so
treat it as a rough visual reference rather than an authoritative source.


---

## Part 2: `components-reference.md`

# Universal Theme 42 — Component Markup Reference

Real Oracle APEX class names + minimal markup patterns. Style everything with the CSS
custom properties from `tokens/*.css` — never literal colors.

## Page shell
```html
<body class="t-Body t-Body--noBoxBody">
  <header class="t-Header" style="background:var(--ut-header-background-color); color:var(--ut-header-text-color);">
    <div class="t-Header-logo">My App</div>
    <nav class="t-Header-nav">...</nav>
  </header>
  <nav class="t-Body-nav" style="background:var(--ut-body-nav-background-color); color:var(--ut-body-nav-text-color); width:var(--ut-nav-width);">
    <ul class="a-TreeView">...</ul>
  </nav>
  <main class="t-Body-content" style="background:var(--ut-body-background-color); color:var(--ut-body-text-color);">
    <div class="t-Body-title" style="background:var(--ut-body-title-background-color);">
      <nav class="t-Breadcrumb">...</nav>
      <h1>Page Title</h1>
    </div>
    <!-- regions go here -->
  </main>
</body>
```

## Region / Card container
```html
<div class="t-Region t-Region--card"
     style="background:var(--ut-region-background-color);
            border:var(--ut-region-border-width) solid var(--ut-region-border-color);
            border-radius:var(--ut-region-border-radius);
            box-shadow:var(--ut-region-box-shadow);">
  <div class="t-Region-header"
       style="background:var(--ut-region-header-background-color);
              border-bottom:1px solid var(--ut-region-header-border-color);
              padding:var(--ut-region-body-padding-y) var(--ut-region-body-padding-x);">
    <h3 class="t-Region-title">Region Title</h3>
    <div class="t-Region-headerItems"><!-- toolbar buttons --></div>
  </div>
  <div class="t-Region-body" style="padding:var(--ut-region-body-padding-y) var(--ut-region-body-padding-x);">
    ...content...
  </div>
  <div class="t-Region-buttons" style="padding:var(--ut-region-buttons-padding-y) var(--ut-region-buttons-padding-x);">
    <button class="t-Button t-Button--hot">Save</button>
  </div>
</div>
```

## Buttons
```html
<button class="t-Button">Default</button>
<button class="t-Button t-Button--hot">Hot (accent)</button>
<button class="t-Button t-Button--primary">Primary (alt)</button>
<button class="t-Button t-Button--success">Success</button>
<button class="t-Button t-Button--warning">Warning</button>
<button class="t-Button t-Button--danger">Danger</button>
<button class="t-Button t-Button--simple">Simple (outline)</button>
<button class="t-Button t-Button--link">Link style</button>
<button class="t-Button t-Button--noUI">No-UI</button>
```
All driven by `--a-button-*` tokens; state variants swap `--a-button-background-color`
/ `--a-button-text-color` to the relevant `--ut-palette-*` pair.

## Alerts
```html
<div class="t-Alert t-Alert--success" role="alert">
  <span class="t-Alert-icon"></span>
  <div class="t-Alert-wrap">
    <h3 class="t-Alert-title">Success</h3>
    <div class="t-Alert-body">Record saved.</div>
  </div>
</div>
<!-- variants: t-Alert--info / t-Alert--warning / t-Alert--danger -->
```

## Badges
```html
<span class="t-Badge" style="background:var(--ut-component-badge-background-color);
      color:var(--ut-component-badge-text-color); border-radius:var(--ut-component-badge-border-radius);">
  New
</span>
```

## Form field
```html
<div class="t-Form-fieldContainer">
  <label class="t-Form-label" for="P1_NAME">Name</label>
  <div class="t-Form-inputContainer">
    <input type="text" id="P1_NAME" class="apex-item-text"
           style="background:var(--a-field-input-background-color);
                  border:var(--a-field-input-border-width) solid var(--a-field-input-border-color);
                  border-radius:var(--a-field-input-border-radius);">
  </div>
</div>
```

## Card view (a-CardView)
```html
<div class="a-CardView" style="display:grid; gap:var(--a-cv-grid-gap); grid-template-columns:repeat(auto-fill,minmax(var(--a-cv-item-width),1fr));">
  <div class="a-CardView-card" style="background:var(--ut-region-background-color); border-radius:var(--a-cv-border-radius); box-shadow:var(--a-cv-shadow);">
    <div class="a-CardView-header" style="padding:var(--a-cv-header-padding-y) var(--a-cv-header-padding-x);">
      <div class="a-CardView-icon" style="width:var(--a-cv-icon-container-size); height:var(--a-cv-icon-container-size); background:var(--ut-component-icon-background-color); color:var(--ut-component-icon-color); border-radius:100%;"></div>
      <div class="a-CardView-title" style="font-size:var(--a-cv-title-font-size); line-height:var(--a-cv-title-line-height);">Card Title</div>
      <div class="a-CardView-subtitle" style="font-size:var(--a-cv-subtitle-font-size); color:var(--ut-component-text-muted-color);">Subtitle</div>
    </div>
    <div class="a-CardView-body" style="padding:var(--a-cv-body-padding-y) var(--a-cv-body-padding-x); font-size:var(--a-cv-maincontent-font-size);">
      Card content goes here.
    </div>
  </div>
</div>
```

## Interactive Report style table
```html
<table class="a-IRR-table" style="border-color:var(--a-gv-border-color); font-size:var(--a-gv-font-size);">
  <thead>
    <tr style="background:var(--ut-report-header-background-color); height:var(--a-gv-header-cell-height);">
      <th style="padding:var(--a-gv-header-cell-padding-y) var(--a-gv-header-cell-padding-x);">Column</th>
    </tr>
  </thead>
  <tbody>
    <tr style="height:var(--a-gv-cell-height);">
      <td style="padding:var(--a-gv-cell-padding-y) var(--a-gv-cell-padding-x); border-bottom:1px solid var(--ut-report-cell-border-color);">Value</td>
    </tr>
  </tbody>
</table>
```

## Tabs
```html
<div class="t-Tabs">
  <ul class="t-Tabs-list">
    <li class="t-Tabs-item is-active"><a class="t-Tabs-link" style="color:var(--ut-tabs-item-active-text-color); font-weight:var(--ut-tabs-item-active-font-weight);">Tab 1</a></li>
    <li class="t-Tabs-item"><a class="t-Tabs-link" style="color:var(--ut-tabs-item-text-color);">Tab 2</a></li>
  </ul>
</div>
```

## Icons
Universal Theme uses an icon font (`a-Icon`, classes like `icon-edit`, `icon-add`, or
Font Awesome `fa-*` if that library is loaded). For prototyping outside APEX, swap in
any icon set (Lucide, Font Awesome) and just size/color it with `--a-icon-size` and
`currentColor`.

## Notes for AI-generated output
- Always wire `background`, `color`, `border`, `border-radius`, `box-shadow`, `padding`
  to the matching CSS custom property rather than literal values.
- Prefer real class names above so markup is portable back into an actual APEX app
  (Custom PL/SQL region, static HTML, or a plugin template) with minimal changes.
- Status semantics: success = green, info = accent-blue (unless a style ties info to its
  own accent), warning = amber, danger = red — always via `--ut-palette-*` tokens, never
  hardcoded.


---

## Part 3: `tokens/vita-light.css`

```css
/*
  Oracle APEX Universal Theme 42 — "Vita" (light, default) Theme Style
  Resolved CSS custom properties, hand-derived from the official LESS source:
  https://static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/less/theme/Vita.less

  This is a practical, browser-ready distillation (no LESS build step required).
  For pixel-perfect production values, compile the .less through APEX Theme Roller.
*/

:root {
  color-scheme: light;

  /* ===== Base scale (derived from #000 on #fff) ===== */
  --base-shade-0: #ffffff;
  --base-shade-1: #f8f8f8;
  --base-shade-2: #f2f2f2;
  --base-shade-3: #e5e5e5;
  --base-shade-4: #d9d9d9;
  --base-shade-5: #cccccc;
  --base-alpha-1: rgba(0,0,0,.025);
  --base-alpha-2: rgba(0,0,0,.05);
  --base-alpha-3: rgba(0,0,0,.075);
  --base-alpha-4: rgba(0,0,0,.10);
  --base-alpha-5: rgba(0,0,0,.15);
  --base-alpha-6: rgba(0,0,0,.20);
  --base-alpha-10: rgba(0,0,0,.65);
  --base-alpha-11: rgba(0,0,0,.85);
  --base-shadow-4: rgba(0,0,0,.10);
  --base-shadow-5: rgba(0,0,0,.15);
  --base-shadow-7: rgba(0,0,0,.30);

  /* ===== Brand / Global Colors (Theme Roller "Global Colors" group) ===== */
  --ut-palette-primary: #056AC8;
  --ut-palette-primary-contrast: #FFFFFF;
  --ut-palette-primary-shade: #e8f1fb;
  --ut-palette-primary-text: var(--ut-palette-primary);
  --ut-link-text-color: #056AC8;
  --ut-focus-outline-color: #056AC8;

  /* ===== Header ===== */
  --ut-header-background-color: #056AC8;
  --ut-header-text-color: #FFFFFF;
  --ut-header-border-color: var(--base-alpha-4);
  --ut-header-box-shadow: var(--ut-shadow-sm);
  --ut-header-height: 3rem;
  --ut-header-item-spacing: .75rem;
  --ut-header-padding: .75rem;
  --ut-header-logo-height: 2rem;

  /* ===== Body ===== */
  --ut-body-background-color: #FDFDFD;
  --ut-body-text-color: #1a1a1a;
  --ut-body-content-max-width: 100%;

  /* ===== Body Navigation (left tree) — dark style (Oracle default) ===== */
  --ut-body-nav-background-color: #2b333c;
  --ut-body-nav-text-color: #d7dade;
  --ut-nav-width: 15rem;
  --ut-body-nav-border-color: var(--ut-component-border-color);
  --ut-navtabs-background-color: #2b333c;
  --ut-navtabs-text-color: #d7dade;
  --ut-navtabs-item-active-background-color: #21272e;
  --ut-navtabs-item-hover-background-color: #21272e;
  --ut-header-menubar-background-color: #2b333c;
  --ut-header-menubar-item-text-color: #d7dade;
  --ut-header-menubar-item-current-background-color: #21272e;
  --ut-header-menubar-item-current-text-color: #d7dade;

  /* ===== Body Title / breadcrumb bar ===== */
  --ut-body-title-background-color: #FFFFFF;
  --ut-body-title-text-color: #262626;
  --ut-body-title-border-width: 0px;
  --ut-body-title-box-shadow: 0 1px 0 0 var(--base-alpha-4);
  --ut-body-title-backdrop-filter: saturate(180%) blur(8px);
  --ut-breadcrumb-item-text-color: rgba(38,38,38,.65);
  --ut-breadcrumb-item-active-text-color: var(--ut-body-title-text-color);
  --ut-breadcrumb-region-spacing: .5rem;
  --ut-hero-region-title-text-color: var(--ut-body-title-text-color);

  /* ===== Body Side / Actions column ===== */
  --ut-body-sidebar-background-color: #FDFDFD;
  --ut-body-sidebar-text-color: #1a1a1a;
  --ut-body-sidebar-width: 15rem;
  --ut-body-actions-background-color: #FCFCFC;
  --ut-body-actions-text-color: #1a1a1a;
  --ut-body-actions-width: 12.5rem;

  /* ===== Standard Region / Card surface ===== */
  --ut-region-background-color: #FFFFFF;
  --ut-region-text-color: #1a1a1a;
  --ut-region-header-background-color: #F6FAFF;
  --ut-region-header-text-color: #1a1a1a;
  --ut-region-header-border-color: var(--base-alpha-3);
  --ut-region-border-width: 1px;
  --ut-region-border-color: var(--base-alpha-4);
  --ut-region-border-radius: .25rem;
  --ut-region-box-shadow: var(--ut-shadow-sm);
  --ut-region-margin: 1rem;
  --ut-region-font-size: .875rem;
  --ut-region-line-height: 1.25rem;
  --ut-region-body-padding-y: 1rem;
  --ut-region-body-padding-x: 1rem;
  --ut-region-buttons-padding-y: .5rem;
  --ut-region-buttons-padding-x: .75rem;
  --ut-button-region-box-shadow: var(--ut-shadow-sm);

  /* ===== Generic component surface (buttons/inputs live on this) ===== */
  --ut-component-background-color: #FFFFFF;
  --ut-component-border-color: var(--base-alpha-4);
  --ut-component-border-width: 1px;
  --ut-component-border-radius: .25rem;
  --ut-component-box-shadow: var(--ut-shadow-lg);
  --ut-component-highlight-background-color: var(--base-alpha-1);
  --ut-component-toolbar-background-color: var(--base-alpha-1);
  --ut-component-inner-border-width: 1px;
  --ut-component-inner-border-color: var(--base-alpha-2);
  --ut-component-text-default-color: #1a1a1a;
  --ut-component-text-title-color: #1a1a1a;
  --ut-component-text-subtitle-color: rgba(26,26,26,.85);
  --ut-component-text-muted-color: rgba(26,26,26,.65);
  --ut-component-icon-background-color: var(--ut-palette-primary);
  --ut-component-icon-color: var(--ut-palette-primary-contrast);
  --ut-component-badge-background-color: var(--base-alpha-2);
  --ut-component-badge-text-color: var(--ut-component-text-default-color);
  --ut-component-badge-border-radius: .25rem;
  --ut-component-pre-background-color: var(--base-alpha-2);

  /* ===== Shadows & radii scale ===== */
  --ut-shadow-sm: 0 .125rem .25rem -.125rem rgba(0,0,0,.10);
  --ut-shadow-md: 0 .75rem 1.5rem -.75rem rgba(0,0,0,.30);
  --ut-shadow-lg: 0 1.5rem 3rem -1.5rem rgba(0,0,0,.30);
  --ut-border-radius-sm: .125rem;
  --ut-border-radius-md: .25rem;
  --ut-border-radius-lg: .5rem;
  --ut-border-radius: var(--ut-border-radius-md);

  /* ===== Status palette ===== */
  --ut-palette-success: #278701;
  --ut-palette-success-contrast: #FFFFFF;
  --ut-palette-success-shade: #eaf5e2;
  --ut-palette-info: #056AC8;
  --ut-palette-info-contrast: #FFFFFF;
  --ut-palette-info-shade: #e8f1fb;
  --ut-palette-warning: #FFC628;
  --ut-palette-warning-contrast: #000000;
  --ut-palette-warning-shade: #fff6e0;
  --ut-palette-danger: #CB1100;
  --ut-palette-danger-contrast: #FFFFFF;
  --ut-palette-danger-shade: #fbe9e7;
  --ut-palette-primary-alt: #4A6A82;   /* g_Primary-BG derived from accent contrast */
  --ut-palette-primary-alt-contrast: #FFFFFF;
  --ut-palette-generic: var(--base-shade-2);
  --ut-palette-generic-contrast: #000000;
  --ut-palette-generic-shade: var(--base-shade-1);

  /* ===== Chart / categorical palette (u-color-1 .. 15) ===== */
  --u-color-1: #309FDB;  --u-color-2: #13B6CF;  --u-color-3: #2EBFBC;
  --u-color-4: #3CAF85;  --u-color-5: #81BB5F;  --u-color-6: #DDDE53;
  --u-color-7: #FBCE4A;  --u-color-8: #ED813E;  --u-color-9: #E95B54;
  --u-color-10: #E85D88; --u-color-11: #CA589D; --u-color-12: #854E9B;
  --u-color-13: #5A68AD; --u-color-14: #AFBAC5; --u-color-15: #6E8598;

  /* ===== Footer / Tabs / Links / Login ===== */
  --ut-footer-background-color: var(--base-shade-2);
  --ut-footer-border-color: var(--base-alpha-2);
  --ut-footer-item-spacing: .75rem;
  --ut-tabs-item-text-color: var(--ut-component-text-default-color);
  --ut-tabs-item-active-text-color: var(--ut-link-text-color);
  --ut-tabs-item-active-font-weight: 700;
  --ut-login-page-background-color: var(--base-shade-3);
  --ut-login-region-background-color: rgba(255,255,255,.65);
  --ut-login-region-filter: blur(4px);
  --ut-login-region-box-shadow: var(--ut-shadow-lg);

  /* ============================================================
     --a-*  Application UI component tokens (mostly style-agnostic)
     ============================================================ */

  /* Buttons */
  --a-button-background-color: #F0F0F0;
  --a-button-text-color: #333333;
  --a-button-border-color: var(--base-alpha-3);
  --a-button-border-radius: .125rem;
  --a-button-border-width: 1px;
  --a-button-shadow: 0 2px 4px -3px rgba(0,0,0,.10);
  --a-button-padding-y: .5rem;
  --a-button-padding-x: .75rem;
  --a-button-font-size: .75rem;
  --a-button-line-height: 1rem;
  --a-button-gap-x: .25rem;
  --a-button-icon-spacing: .375rem;
  --a-button-icon-size: 1rem;
  --a-button-hover-background-color: #FAFAFA;
  --a-button-hover-border-color: var(--base-alpha-3);
  --a-button-active-background-color: var(--base-shade-3);
  --a-button-focus-border-color: var(--ut-palette-primary);
  --a-button-count-background-color: var(--ut-palette-primary);
  --a-button-count-text-color: var(--ut-palette-primary-contrast);

  /* Cards (a-CardView) */
  --a-cv-grid-gap: 1rem;
  --a-cv-item-width: 20rem;
  --a-cv-border-radius: .25rem;
  --a-cv-shadow: var(--ut-shadow-sm);
  --a-cv-header-padding-y: 1rem;
  --a-cv-header-padding-x: 1rem;
  --a-cv-header-item-spacing-x: .75rem;
  --a-cv-icon-size: 1rem;
  --a-cv-icon-container-size: 2rem;
  --a-cv-title-font-size: 1rem;
  --a-cv-title-line-height: 1.25rem;
  --a-cv-subtitle-font-size: .75rem;
  --a-cv-subtitle-line-height: 1rem;
  --a-cv-badge-font-size: .75rem;
  --a-cv-badge-background-color: var(--base-alpha-4);
  --a-cv-body-padding-x: 1rem;
  --a-cv-body-padding-y: 1rem;
  --a-cv-maincontent-font-size: .875rem;
  --a-cv-maincontent-line-height: 1.25rem;
  --a-cv-actions-padding-y: 1rem;
  --a-cv-actions-padding-x: 1rem;

  /* Checkboxes & Radios */
  --a-checkbox-size: 1rem;
  --a-checkbox-label-font-size: .75rem;
  --a-checkbox-border-radius: .125rem;
  --a-checkbox-background-color: #F5F5F5;
  --a-checkbox-border-color: var(--base-alpha-5);
  --a-checkbox-checked-background-color: var(--ut-palette-primary);
  --a-checkbox-checked-text-color: #FFFFFF;
  --a-checkbox-hover-background-color: var(--base-alpha-2);
  --a-checkbox-icon-size: .75rem;
  --a-checkbox-label-spacing-y: .125rem;
  --a-checkbox-label-spacing-x: .375rem;

  /* Form / Field inputs */
  --a-field-input-background-color: #F5F5F5;
  --a-field-input-text-color: #1a1a1a;
  --a-field-input-border-color: var(--base-alpha-4);
  --a-field-input-border-radius: .125rem;
  --a-field-input-border-style: solid;
  --a-field-input-border-width: 1px;
  --a-field-input-hover-background-color: #FAFAFA;
  --a-field-input-focus-background-color: #FFFFFF;
  --a-field-input-focus-border-color: var(--ut-palette-primary);
  --ut-field-label-text-color: #1a1a1a;
  --ut-field-input-focus-icon-color: var(--ut-palette-primary);
  --a-field-select-background-size: 2rem 1rem;
  --a-field-select-arrow-padding: 2rem;
  --ut-checkbox-item-spacing: 1rem;

  /* Grid View / Interactive Report */
  --a-gv-font-size: .75rem;
  --a-gv-line-height: 1rem;
  --a-gv-border-color: var(--ut-component-border-color);
  --a-gv-background-color: #FFFFFF;
  --a-gv-cell-padding-y: .25rem;
  --a-gv-cell-padding-x: .5rem;
  --a-gv-cell-height: 2rem;
  --a-gv-row-hover-background-color: var(--base-shade-1);
  --a-gv-header-cell-padding-y: .25rem;
  --a-gv-header-cell-padding-x: .5rem;
  --a-gv-header-cell-height: 2.5rem;
  --a-gv-header-background-color: var(--ut-region-header-background-color);
  --ut-report-cell-alt-background-color: var(--base-alpha-2);
  --ut-report-header-background-color: var(--base-alpha-1);
  --ut-report-cell-border-color: var(--base-alpha-4);
  --ut-report-cell-hover-background-color: var(--base-alpha-1);

  /* Menu / Menubar */
  --a-menu-padding-y: .5rem;
  --a-menu-padding-x: 0rem;
  --a-menu-font-size: .75rem;
  --a-menu-line-height: 1rem;
  --a-menu-text-color: #1a1a1a;
  --a-menu-background-color: #FFFFFF;
  --a-menu-border-radius: .25rem;
  --a-menu-border-color: var(--base-alpha-4);
  --a-menu-focused-background-color: var(--ut-palette-primary);
  --a-menu-focused-text-color: var(--ut-palette-primary-contrast);
  --a-menu-sep-border-color: var(--ut-component-border-color);
  --a-menu-icon-size: 1rem;
  --a-menubar-item-padding-y: .5rem;
  --a-menubar-item-padding-x: .5rem;

  /* Toolbar */
  --a-toolbar-background-color: var(--ut-region-header-background-color);
  --a-toolbar-border-color: var(--ut-component-border-color);
  --a-toolbar-item-spacing: .5rem;
  --a-toolbar-sep-border-color: var(--ut-component-inner-border-color);
  --a-toolbar-small-button-padding-y: .25rem;
  --a-toolbar-small-button-padding-x: .5rem;

  /* Tree View */
  --a-treeview-toggle-size: 1rem;
  --a-treeview-node-icon-size: 1rem;
  --a-treeview-node-font-size: .75rem;
  --a-treeview-node-line-height: 1rem;
  --a-treeview-node-padding-y: .25rem;
  --a-treeview-node-padding-x: .25rem;
  --a-treeview-node-selected-background-color: #21272e;
  --a-treeview-node-selected-text-color: #FFFFFF;
  --a-treeview-node-focused-background-color: #21272e;
  --a-treeview-node-focused-text-color: #FFFFFF;

  /* Chips / Smart Filters */
  --a-chip-padding-y: .125rem;
  --a-chip-padding-x: .25rem;
  --a-chip-font-size: .75rem;
  --a-chip-line-height: 1rem;
  --a-chip-border-radius: .125rem;
  --a-chip-border-color: var(--a-field-input-border-color);
  --a-chip-hover-background-color: var(--base-alpha-1);
  --a-chip-active-background-color: var(--base-alpha-2);
  --a-chip-applied-background-color: var(--base-alpha-3);
  --a-combo-select-item-selected-background-color: var(--ut-palette-primary-shade);

  /* Switch */
  --a-switch-width: 2.75rem;
  --a-switch-padding-y: .125rem;
  --a-switch-padding-x: .125rem;
  --a-switch-toggle-width: 1.25rem;
  --a-switch-toggle-height: 1.25rem;

  /* Badges (used by a-CardView, filedrop counts, etc.) */
  --a-filedrop-count-badge-font-size: .625rem;
  --a-filedrop-heading-font-size: 1.25rem;

  /* Dialogs (jQuery UI) */
  --jui-dialog-background-color: var(--ut-region-background-color);
  --jui-dialog-text-color: var(--ut-region-text-color);
  --jui-dialog-border-color: var(--ut-region-border-color);
  --jui-dialog-border-radius: var(--ut-region-border-radius);
  --jui-dialog-shadow: var(--ut-shadow-lg), 0 0 0 1px var(--ut-region-border-color);
  --jui-dialog-titlebar-padding-y: .75rem;
  --jui-dialog-titlebar-padding-x: 1rem;
  --jui-dialog-titlebar-text-color: var(--ut-component-text-title-color);
  --jui-dialog-titlebar-border-color: var(--ut-region-border-color);
  --jui-dialog-title-font-size: 1rem;
  --jui-dialog-title-line-height: 1.5rem;
  --jui-dialog-content-padding-y: 0rem;
  --jui-dialog-content-padding-x: 0rem;
  --jui-dialog-buttonpane-content-padding-y: .75rem;
  --jui-dialog-buttonpane-content-padding-x: 1rem;

  /* Tooltip */
  --a-tooltip-font-size: .6875rem;

  /* Alerts */
  --ut-alert-title-font-weight: 600;
  --ut-alert-box-shadow: var(--ut-shadow-sm);

  /* Card list / Link list */
  --ut-cardlist-box-shadow: var(--ut-shadow-sm);
  --ut-linkslist-arrow-color: var(--base-alpha-6);
}
```

---

## Part 4: `tokens/vita-dark.css`

```css
/*
  Oracle APEX Universal Theme 42 — "Vita Dark" Theme Style
  DELTA file — load AFTER vita-light.css. Overrides only what changes for dark mode.
  Derived from: .../theme/Vita-Dark.less
*/

:root {
  color-scheme: dark;

  --base-shade-0: #1a1a1a;
  --base-alpha-2: rgba(255,255,255,.10);
  --base-alpha-4: rgba(255,255,255,.15);

  --ut-palette-primary: #056AC8;
  --ut-palette-primary-contrast: #FFFFFF;
  --ut-link-text-color: #6fb3f2; /* lighten(accent, 19%) for dark contrast */
  --ut-focus-outline-color: #056AC8;

  --ut-header-background-color: #056AC8;
  --ut-header-text-color: #FFFFFF;

  /* Body: dark, desaturated, slightly blue-tinted charcoal derived from accent */
  --ut-body-background-color: #14181c;
  --ut-body-text-color: #e6e6e6;

  --ut-body-title-background-color: #171c21;
  --ut-body-title-text-color: #e6e6e6;

  --ut-region-background-color: #101418;
  --ut-region-text-color: #e6e6e6;
  --ut-region-header-background-color: #0c1013;
  --ut-region-header-text-color: #e6e6e6;

  --ut-component-background-color: #101418;
  --ut-component-text-default-color: #e6e6e6;
  --ut-component-text-title-color: #ffffff;
  --ut-component-text-muted-color: rgba(255,255,255,.65);
  --ut-component-border-color: rgba(255,255,255,.15);

  --a-button-background-color: #262b30;
  --a-button-text-color: #e6e6e6;
  --a-button-hover-background-color: #2e343a;
  --a-button-active-background-color: #1c1f23;

  --a-field-input-background-color: #1b1f24;
  --a-field-input-text-color: #e6e6e6;
  --a-field-input-border-color: rgba(255,255,255,.20);
  --a-field-input-hover-background-color: #21262b;
  --a-field-input-focus-background-color: #262b31;

  --a-gv-background-color: #101418;
  --a-gv-row-hover-background-color: #181d22;

  --ut-palette-success: #388729;
  --ut-palette-info: #006BD8;
  --ut-palette-warning: #FBCE4A;
  --ut-palette-danger: #EE0701;

  --ut-footer-background-color: #14181c;
  --ut-login-page-background-color: #0a0d10;
  --ut-login-region-background-color: rgba(0,0,0,.65);
}
```

---

## Part 5: `tokens/vita-red.css`

```css
/*
  Oracle APEX Universal Theme 42 — "Vita Red" Theme Style
  DELTA file — load AFTER vita-light.css.
  This is the *official* Oracle minimal-override pattern (see Vita-Red.less):
  only accent, link, focus, and nav colors are overridden — everything else
  cascades from the base Vita tokens automatically.

  Source: .../theme/Vita-Red.less
    @g_Accent-BG:   #da1b1b;
    @g_Link-Base:   #2370c2;
    @g_Focus:       #2370c2;
    @g_Nav-BG:      #f0f0f0;
    @g_Nav-Active-BG: #dadada;
    @g_Body-Title-BG: #ffffff;
    @g_Nav-FG:      #606060;
*/

:root {
  --ut-palette-primary: #da1b1b;
  --ut-palette-primary-contrast: #FFFFFF;
  --ut-link-text-color: #2370c2;
  --ut-focus-outline-color: #2370c2;

  --ut-header-background-color: #da1b1b;
  --ut-header-text-color: #FFFFFF;

  --ut-body-title-background-color: #FFFFFF;

  /* Vita Red uses a LIGHT nav style, not the dark default */
  --ut-body-nav-background-color: #f0f0f0;
  --ut-body-nav-text-color: #606060;
  --ut-navtabs-background-color: #f0f0f0;
  --ut-navtabs-text-color: #606060;
  --ut-navtabs-item-active-background-color: #dadada;
  --ut-navtabs-item-hover-background-color: #dadada;
  --ut-header-menubar-background-color: #f0f0f0;
  --ut-header-menubar-item-text-color: #606060;
  --ut-header-menubar-item-current-background-color: #dadada;
  --ut-header-menubar-item-current-text-color: #606060;

  --a-treeview-node-selected-background-color: #dadada;
  --a-treeview-node-selected-text-color: #606060;
  --a-treeview-node-focused-background-color: #dadada;
  --a-treeview-node-focused-text-color: #606060;

  --a-field-input-focus-border-color: #2370c2;
  --ut-field-input-focus-icon-color: #2370c2;
  --a-checkbox-checked-background-color: #2370c2;
  --a-button-focus-border-color: #da1b1b;
  --a-button-count-background-color: #da1b1b;
}
```

---

## Part 6: `tokens/vita-slate.css`

```css
/*
  Oracle APEX Universal Theme 42 — "Vita Slate" Theme Style
  DELTA file — load AFTER vita-light.css.
  Source: .../theme/Vita-Slate.less
    @g_Nav_Style:    dark;
    @g_Accent-BG:    #505f6d;
    @g_Accent-OG:    #ececec;
    @g_Body-Title-BG:#dee1e4;
    @g_Link-Base:    #337ac0;
    @g_Body-BG:      #f5f5f5;
*/

:root {
  --ut-palette-primary: #505f6d;
  --ut-palette-primary-contrast: #FFFFFF;
  --ut-link-text-color: #337ac0;
  --ut-focus-outline-color: #505f6d;

  --ut-header-background-color: #505f6d;
  --ut-header-text-color: #FFFFFF;

  --ut-body-background-color: #f5f5f5;
  --ut-body-text-color: #1a1a1a;

  --ut-body-title-background-color: #dee1e4;
  --ut-body-title-text-color: #1a1a1a;

  --ut-region-background-color: #FFFFFF;
  --ut-region-header-background-color: #F7F7F7;

  /* Dark nav, desaturated/darkened from the slate accent */
  --ut-body-nav-background-color: #2c3339;
  --ut-body-nav-text-color: #d7dade;
  --ut-navtabs-background-color: #2c3339;
  --ut-navtabs-text-color: #d7dade;
  --ut-navtabs-item-active-background-color: #232830;
  --ut-navtabs-item-hover-background-color: #232830;
  --ut-header-menubar-background-color: #2c3339;
  --ut-header-menubar-item-text-color: #d7dade;
  --ut-header-menubar-item-current-background-color: #232830;
  --ut-header-menubar-item-current-text-color: #d7dade;

  --a-treeview-node-selected-background-color: #232830;
  --a-treeview-node-selected-text-color: #FFFFFF;
  --a-treeview-node-focused-background-color: #232830;
  --a-treeview-node-focused-text-color: #FFFFFF;

  --a-field-input-focus-border-color: #505f6d;
  --ut-field-input-focus-icon-color: #505f6d;
  --a-checkbox-checked-background-color: #505f6d;
  --a-button-focus-border-color: #505f6d;
  --a-button-count-background-color: #505f6d;
}
```

---

## Part 7: `tokens/iris.css`

```css
/*
  Oracle APEX Universal Theme 42 — "Iris" Theme Style
  DELTA file — load AFTER vita-light.css.
  Iris is Oracle's Redwood-family "pillar" style — default pillar "Sky" (#00688C),
  a dark neutral header/nav, white region surfaces, and slightly larger radii/header.
  Source: .../theme/Iris.less (pillar: sky, header style: dark)
*/

:root {
  --ut-palette-primary: #00688C;
  --ut-palette-primary-contrast: #FFFFFF;
  --ut-palette-primary-shade: #E4F1F7;
  --ut-link-text-color: #0e7295;
  --ut-focus-outline-color: #00688C;

  --ut-header-height: 3.5rem;
  --ut-header-background-color: #302D2A;
  --ut-header-text-color: #FFFFFF;

  --ut-body-background-color: #FBF9F8;
  --ut-body-text-color: #161513;

  --ut-body-title-background-color: #F1EFED;
  --ut-body-title-text-color: #161513;
  --ut-breadcrumb-item-text-color: rgba(22,21,19,.7);

  --ut-body-nav-background-color: #302D2A;
  --ut-body-nav-text-color: #FFFFFF;
  --ut-navtabs-background-color: #302D2A;
  --ut-navtabs-text-color: #FFFFFF;
  --ut-navtabs-item-active-background-color: rgba(255,255,255,.08);
  --ut-navtabs-item-hover-background-color: rgba(255,255,255,.08);
  --ut-header-menubar-background-color: #302D2A;
  --ut-header-menubar-item-text-color: #FFFFFF;
  --ut-header-menubar-item-current-background-color: rgba(255,255,255,.08);
  --ut-header-menubar-item-current-text-color: #FFFFFF;

  --a-treeview-node-selected-background-color: #00688C;
  --a-treeview-node-selected-text-color: #FFFFFF;
  --a-treeview-node-focused-background-color: #00688C;
  --a-treeview-node-focused-text-color: #FFFFFF;

  --ut-region-background-color: #FFFFFF;
  --ut-region-header-background-color: #FFFFFF;
  --ut-region-header-text-color: #161513;
  --ut-region-text-color: #161513;
  --ut-component-background-color: #FFFFFF;

  --ut-component-border-radius: .25rem;
  --ut-region-border-radius: .25rem;
  --a-button-border-radius: .25rem;
  --a-field-input-border-radius: .25rem;

  --a-button-background-color: rgba(22,21,19,.08);
  --a-button-text-color: #161513;
  --a-button-hover-background-color: rgba(22,21,19,.12);
  --a-button-active-background-color: rgba(22,21,19,.16);

  --a-field-input-background-color: #FFFFFF;
  --a-field-input-text-color: #161513;
  --a-field-input-border-color: rgba(22,21,19,.5);
  --a-field-input-focus-border-color: #00688C;
  --ut-field-input-focus-icon-color: #00688C;
  --a-checkbox-checked-background-color: #00688C;

  --ut-palette-primary-alt: #227E9E;
  --ut-palette-primary-alt-contrast: #FFFFFF;
  --ut-palette-success: #436B1D;
  --ut-palette-success-contrast: #FFFFFF;
  --ut-palette-success-shade: #E4F5D3;
  --ut-palette-info: #227E9E;
  --ut-palette-info-contrast: #FFFFFF;
  --ut-palette-info-shade: #E4F1F7;
  --ut-palette-warning: #8F520A;
  --ut-palette-warning-contrast: #FFFFFF;
  --ut-palette-warning-shade: #FCEDDC;
  --ut-palette-danger: #B3311F;
  --ut-palette-danger-contrast: #FFFFFF;
  --ut-palette-danger-shade: #FFEBE8;

  --a-button-count-background-color: #00688C;
  --a-button-count-text-color: #FFFFFF;
}
```

---

## Part 8: `tokens/redwood.css`

```css
/*
  Oracle APEX Universal Theme 42 — "Redwood" Theme Style
  DELTA file — load AFTER vita-light.css.
  Oracle's flagship design system look: warm neutral surfaces, a light nav rail,
  brand-green primary accent, larger type/spacing, dashed focus outline.
  Source: .../theme/Redwood.less (light mode, "brandlight" primary pillar)
*/

:root {
  --ut-palette-primary: #5F7D4F;
  --ut-palette-primary-contrast: #FFFFFF;
  --ut-palette-primary-shade: #F7FCF3;
  --ut-link-text-color: #00688C;
  --ut-focus-outline-color: #161513;

  --ut-header-height: 3.5rem;
  --ut-header-background-color: #F5F4F2;
  --ut-header-text-color: #161513;
  --ut-header-border-color: rgba(22,21,19,.1);

  --ut-body-background-color: #F5F4F2;
  --ut-body-text-color: #161513;

  --ut-body-title-background-color: #FFFFFF;
  --ut-body-title-text-color: #161513;
  --ut-breadcrumb-item-text-color: #00688C;

  --ut-body-nav-background-color: #FFFFFF;
  --ut-body-nav-text-color: #161513;
  --ut-navtabs-background-color: #F1EFED;
  --ut-navtabs-text-color: rgba(22,21,19,.7);
  --ut-navtabs-item-active-background-color: transparent;
  --ut-navtabs-item-hover-background-color: transparent;
  --ut-header-menubar-background-color: #F1EFED;
  --ut-header-menubar-item-text-color: #161513;
  --ut-header-menubar-item-current-background-color: #4E4137;
  --ut-header-menubar-item-current-text-color: #FFFFFF;

  --a-treeview-node-selected-background-color: rgba(22,21,19,.08);
  --a-treeview-node-selected-text-color: #161513;
  --a-treeview-node-focused-background-color: transparent;
  --a-treeview-node-focused-text-color: #161513;

  --ut-region-background-color: #FFFFFF;
  --ut-region-header-background-color: #FFFFFF;
  --ut-region-header-text-color: #161513;
  --ut-region-text-color: #161513;
  --ut-region-border-radius: .5rem;
  --ut-component-background-color: #FFFFFF;
  --ut-component-border-radius: .375rem;

  --a-button-border-radius: .25rem;
  --a-button-background-color: rgba(22,21,19,.08);
  --a-button-text-color: #161513;
  --a-button-hover-background-color: rgba(22,21,19,.12);
  --a-button-active-background-color: rgba(22,21,19,.16);
  --a-button-padding-y: .375rem;
  --a-button-padding-x: 1rem;
  --a-button-font-size: .875rem;

  --a-field-input-border-radius: .25rem;
  --a-field-input-background-color: #FFFFFF;
  --a-field-input-text-color: #161513;
  --a-field-input-border-color: rgba(22,21,19,.5);
  --a-field-input-focus-border-color: #227E9E;
  --ut-field-input-focus-icon-color: #227E9E;
  --a-checkbox-checked-background-color: #161513;

  --ut-palette-primary-alt: #7A736E;
  --ut-palette-primary-alt-contrast: #FFFFFF;
  --ut-palette-success: #508223;
  --ut-palette-success-contrast: #FFFFFF;
  --ut-palette-success-shade: #F4FCEB;
  --ut-palette-info: #227E9E;
  --ut-palette-info-contrast: #FFFFFF;
  --ut-palette-info-shade: #F6FAFC;
  --ut-palette-warning: #AC630C;
  --ut-palette-warning-contrast: #FFFFFF;
  --ut-palette-warning-shade: #FEF9F2;
  --ut-palette-danger: #D63B25;
  --ut-palette-danger-contrast: #FFFFFF;
  --ut-palette-danger-shade: #FFF8F7;

  --a-button-count-background-color: #5F7D4F;
  --a-button-count-text-color: #FFFFFF;

  --ut-shadow-sm: 0 .25rem .5rem -.25rem rgba(0,0,0,.16);
  --ut-shadow-md: 0 .375rem .75rem -.375rem rgba(0,0,0,.20);
  --ut-shadow-lg: 0 .5rem 1rem -.5rem rgba(0,0,0,.24);
}
```

---

## Part 9: `tokens/standard.css`

```css
/*
  Oracle APEX "Theme Standard" (legacy, pre-Universal-Theme) — approximation
  DELTA file — load AFTER vita-light.css.

  IMPORTANT: Theme Standard (app_ui/css/Theme-Standard.css + Core.css) predates
  Theme 42's CSS-custom-property system entirely — it uses fixed class-based CSS,
  not design tokens, and its layout (fixed tabs, breadcrumb-less title bar, classic
  region templates) doesn't map 1:1 onto Universal Theme markup. This file is a
  best-effort visual approximation using Theme 42's token names, for quick
  side-by-side comparison / nostalgia only — it is NOT a faithful reproduction.
  For the real thing, reference app_ui/css/Core.css + Theme-Standard.css directly.
*/

:root {
  --ut-palette-primary: #2178B4;
  --ut-palette-primary-contrast: #FFFFFF;
  --ut-link-text-color: #2178B4;
  --ut-focus-outline-color: #2178B4;

  --ut-header-background-color: #2E3D4E;
  --ut-header-text-color: #FFFFFF;
  --ut-header-height: 2.75rem;

  --ut-body-background-color: #E3E6E9;
  --ut-body-text-color: #1a1a1a;

  --ut-body-title-background-color: #F2F3F4;
  --ut-body-title-text-color: #333333;

  --ut-body-nav-background-color: #3B4B5C;
  --ut-body-nav-text-color: #D6DBE0;
  --ut-navtabs-background-color: #3B4B5C;
  --ut-navtabs-text-color: #D6DBE0;
  --ut-navtabs-item-active-background-color: #2E3D4E;
  --ut-navtabs-item-hover-background-color: #2E3D4E;

  --ut-region-background-color: #FFFFFF;
  --ut-region-header-background-color: #EDEFF1;
  --ut-region-header-text-color: #333333;
  --ut-region-border-radius: 0rem;
  --ut-component-border-radius: 0rem;
  --ut-shadow-sm: 0 1px 2px rgba(0,0,0,.15);
  --ut-shadow-md: 0 2px 4px rgba(0,0,0,.20);
  --ut-shadow-lg: 0 4px 8px rgba(0,0,0,.25);

  --a-button-border-radius: .1875rem;
  --a-button-background-color: #F4F4F4;
  --a-button-text-color: #333333;
  --a-button-border-color: #B7BEC4;
  --a-button-hover-background-color: #E9EBEC;

  --a-field-input-border-radius: 0rem;
  --a-field-input-background-color: #FFFFFF;
  --a-field-input-text-color: #1a1a1a;
  --a-field-input-border-color: #B7BEC4;
  --a-field-input-focus-border-color: #2178B4;

  --ut-palette-success: #4C8B3A;
  --ut-palette-success-contrast: #FFFFFF;
  --ut-palette-info: #2178B4;
  --ut-palette-info-contrast: #FFFFFF;
  --ut-palette-warning: #D6A428;
  --ut-palette-warning-contrast: #000000;
  --ut-palette-danger: #C0392B;
  --ut-palette-danger-contrast: #FFFFFF;

  --a-button-count-background-color: #2178B4;
  --a-button-count-text-color: #FFFFFF;
}
```

---

## Part 10: `tokens/vita-emerald.less`

```less
/*!
 Custom Theme Style built on Oracle APEX Universal Theme 42, "Vita" family.
 Author pattern follows Oracle's own official variant files exactly
 (compare to Vita-Red.less / Vita-Dark.less / Vita-Slate.less):
 override a small set of @g_* "Theme Roller" variables, then import the
 base Vita.less — every other token (buttons, forms, IRs, shadows, states,
 nav, badges, focus rings, hot/primary/danger/success buttons, chart colors)
 is re-derived automatically by Oracle's LESS color functions.
 ========================================================================== */
/* ==========================================================================
   Universal Theme: Vita Emerald Theme Style (custom)
   ========================================================================== */

// ---- Apply Overrides ----------------------------------------------------

// Primary brand accent — drives header, links (via @g_Link-Base below),
// focus ring, hot/primary buttons, nav accent, badges, primary state.
@g_Accent-BG: #0E9F6E;

// Hyperlink color — left equal to accent for a clean single-accent brand.
@g_Link-Base: @g_Accent-BG;

// Focus ring color — left equal to accent.
@g_Focus: @g_Accent-BG;

// Keep Oracle's default dark left-nav (auto-derives a desaturated,
// darkened version of the accent — no need to hand-pick nav colors).
@g_Nav_Style: dark;

// Softer, more modern corner radii than stock Vita (2–4px) across
// regions, buttons and form fields.
@g_Container-BorderRadius: .375rem;
@g_Button-BorderRadius:    .375rem;
@g_Form-BorderRadius:      .375rem;

// LESS_IGNORE_END

// ---- Import Default Vita Style ------------------------------------------
// In a real Theme Roller / build pipeline this is an actual @import of the
// base Vita.less file (Oracle CDN link below). Paste this whole file into
// Theme Roller's custom LESS editor for a Theme Style, or reference both
// files from your build tool in this order.
//
// @import "https://static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/less/theme/Vita.less";
```

---

## Part 11: `tokens/vita-emerald.css`

```css
/*
  "Vita Emerald" — new custom Oracle APEX Universal Theme 42 Theme Style.
  Built to the same standard as Oracle's own Vita-Red / Vita-Dark / Vita-Slate:
  a minimal override of accent + radius, everything else cascades from
  vita-light.css. Load order:

    <link rel="stylesheet" href="tokens/vita-light.css">
    <link rel="stylesheet" href="tokens/vita-emerald.css">   <!-- this file -->

  Source of the override logic: tokens/vita-emerald.less (Theme-Roller-ready).
  Hex values below are hand-resolved approximations of Oracle's LESS color
  functions (contrast/mix/desaturate/darken) — verify exact values via
  Theme Roller before shipping to production APEX pages.
*/

:root {
  /* ---- Brand accent: emerald green ---- */
  --ut-palette-primary: #0E9F6E;
  --ut-palette-primary-contrast: #FFFFFF;
  --ut-palette-primary-shade: #e5f6ef;
  --ut-link-text-color: #0E9F6E;
  --ut-focus-outline-color: #0E9F6E;

  --ut-header-background-color: #0E9F6E;
  --ut-header-text-color: #FFFFFF;

  /* ---- Left nav: auto-derived dark, desaturated emerald-charcoal ---- */
  --ut-body-nav-background-color: #232b28;
  --ut-body-nav-text-color: #d9ddda;
  --ut-navtabs-background-color: #232b28;
  --ut-navtabs-text-color: #d9ddda;
  --ut-navtabs-item-active-background-color: #1a201d;
  --ut-navtabs-item-hover-background-color: #1a201d;
  --ut-header-menubar-background-color: #232b28;
  --ut-header-menubar-item-text-color: #d9ddda;
  --ut-header-menubar-item-current-background-color: #1a201d;
  --ut-header-menubar-item-current-text-color: #d9ddda;

  --a-treeview-node-selected-background-color: #1a201d;
  --a-treeview-node-selected-text-color: #FFFFFF;
  --a-treeview-node-focused-background-color: #1a201d;
  --a-treeview-node-focused-text-color: #FFFFFF;

  /* ---- Softer corner radii (6px vs stock 2–4px) ---- */
  --ut-component-border-radius: .375rem;
  --ut-region-border-radius: .375rem;
  --a-button-border-radius: .375rem;
  --a-field-input-border-radius: .375rem;
  --a-checkbox-border-radius: .375rem;
  --a-cv-border-radius: .375rem;
  --jui-dialog-border-radius: .375rem;

  /* ---- Focus / primary-derived states ---- */
  --a-field-input-focus-border-color: #0E9F6E;
  --ut-field-input-focus-icon-color: #0E9F6E;
  --a-checkbox-checked-background-color: #0E9F6E;
  --a-checkbox-checked-text-color: #FFFFFF;
  --a-button-focus-border-color: #0E9F6E;
  --a-button-count-background-color: #0E9F6E;
  --a-button-count-text-color: #FFFFFF;
  --a-combo-select-item-selected-background-color: #e5f6ef;

  /* ---- Primary (alt) state used by .t-Button--primary ---- */
  --ut-palette-primary-alt: #0C7F5A;
  --ut-palette-primary-alt-contrast: #FFFFFF;
}
```

---

*Bundle generated 2026-07-22. Canonical multi-file source: https://github.com/raju-bd/Oracle-apex-ut-UI.skill*
