# Oracle APEX Universal Theme skill (`Oracle-apex-ut-UI.skill`)

**A drop-in design-token reference for Oracle APEX Universal Theme 42 — the "Vita" style family — so any AI or any developer can produce HTML/CSS that looks and behaves like a real APEX app, without needing an APEX instance running.**

🔗 **Live demo / landing page:** open [`docs/index.html`](./docs/index.html) locally, or enable GitHub Pages on this repo (Settings → Pages → Deploy from branch → `main` / `/docs`) and visit `https://raju-bd.github.io/Oracle-apex-ut-UI.skill/`.

⭐ **If this saves you time, star the repo:** [github.com/raju-bd/Oracle-apex-ut-UI.skill](https://github.com/raju-bd/Oracle-apex-ut-UI.skill)

---

## Fastest path: single-file bundles

Don't want to clone the whole repo? Two files, each fully self-contained — no other files needed:

| File | For | How |
|---|---|---|
| **[`Oracle-apex-ut-UI.skill.md`](./Oracle-apex-ut-UI.skill.md)** | Feeding an AI | Upload/paste this **one file** into Claude, ChatGPT, Gemini, a Claude Project, a Cursor rules file, etc. It has `SKILL.md`, `components-reference.md`, and all 9 token/style files inlined as labeled code blocks. |
| **[`Oracle-apex-ut-UI.skill.bundle.js`](./Oracle-apex-ut-UI.skill.bundle.js)** | A live web page | `<script src="Oracle-apex-ut-UI.skill.bundle.js"></script>` — that's the whole install. All 8 Theme Styles are embedded as strings inside the script; it injects the CSS itself. Switch styles at runtime with `ApexVitaSkill.use('vita-emerald')`. See [`bundle-demo.html`](./bundle-demo.html) for a working example. |

Both are generated from the canonical multi-file source below and kept in sync — if you
only need one file, grab one of these two and skip everything else in this repo.
(Maintainer note: after editing anything in `tokens/`, `SKILL.md`, or
`components-reference.md`, run `python3 build-bundles.py` to regenerate both.)

---

## What this is

Oracle APEX's Universal Theme 42 ("Vita") is a two-layer CSS custom-property design
system (`--ut-*` brand tokens + `--a-*` component tokens), normally only fully resolved
by Oracle's Theme Roller / LESS build. This repo distills that system into:

- **Plain, browser-ready CSS** you can `<link>` directly — no build step, no APEX instance.
- **A written skill (`SKILL.md`)** you can paste into any AI's context (Claude, GPT,
  Gemini, a local model, a Claude Project, a Cursor rules file, etc.) so it generates
  markup and CSS that's actually consistent with real Oracle APEX output.
- **A worked example of authoring a brand-new Theme Style** ("Vita Emerald"), built the
  same way Oracle builds `Vita-Red` / `Vita-Dark` / `Vita-Slate` — override a handful of
  accent variables, let the rest cascade.

## Why

Prompting a general-purpose AI to "make it look like Oracle APEX" produces something
close but subtly wrong — different radii, different shadow depth, invented class names,
colors that don't match any real Theme Style. This repo exists so the AI has the actual
tokens and class names to work from instead of guessing.

## What's inside

```
Oracle-apex-ut-UI.skill/
├── README.md                   ← you are here
├── LICENSE                     ← MIT (see note on Oracle's own terms inside)
├── Oracle-apex-ut-UI.skill.md       ← single-file bundle for AI use (everything inlined)
├── Oracle-apex-ut-UI.skill.bundle.js← single-file bundle for the browser (everything inlined)
├── bundle-demo.html            ← proof the .bundle.js file works completely standalone
├── SKILL.md                    ← the skill itself — usage guide + token map + workflow
├── components-reference.md     ← real APEX class names + markup patterns
├── example.html                ← minimal dashboard demo with a live style switcher
├── tokens/                     ← the skill's source-of-truth tokens
│   ├── vita-light.css          ← baseline Vita (light/default), ~300 resolved tokens
│   ├── vita-dark.css           ← Vita Dark deltas (official)
│   ├── vita-red.css            ← Vita Red deltas (official)
│   ├── vita-slate.css          ← Vita Slate deltas (official)
│   ├── iris.css                ← Iris deltas (official, Redwood-family "Sky" pillar)
│   ├── redwood.css             ← Redwood deltas (official, flagship design system)
│   ├── standard.css            ← Legacy Theme Standard — approximation only, see note
│   ├── vita-emerald.less       ← NEW custom Theme Style — Theme-Roller-ready LESS source
│   └── vita-emerald.css        ← NEW custom Theme Style — browser-ready resolved tokens
└── docs/                       ← GitHub Pages site — the marketing/demo landing page
    ├── index.html              ← animated landing page, accordion, prompt demos, dark mode
    └── tokens/                 ← copy of the *.css files above, kept in sync, used by index.html
```

Kept separate on purpose: `tokens/`, `SKILL.md`, and `components-reference.md` at the repo root are
what you actually clone or paste into an AI's context — no marketing page, no JS, no animation code
in the way. `docs/` is only for the browsable demo site.

**Canonical upstream sources** (always check these for anything newer than this repo):
- Live component gallery: <https://oracleapex.com/ords/r/apex_pm/ut/getting-started>
- `Vita.less` · `Vita-Dark.less` · `Vita-Red.less` · `Vita-Slate.less` on
  `static.oracle.com/cdn/apex/26.1.2/themes/theme_42/26.1/less/theme/`

## Quick start

**1. Give it to an AI as reference.** Paste the contents of `SKILL.md` (and optionally
`components-reference.md`) into your prompt, system prompt, or Claude Project knowledge,
then ask for APEX-style UI. Example prompt:

> Using the Vita Emerald design tokens, build an HTML customer dashboard: a header,
> a left nav, three stat cards, an alert, and a report table. Use `var(--token-name)`
> for every color/spacing value — no hardcoded hex.

**2. Use it directly in a browser prototype.**
```html
<link rel="stylesheet" href="tokens/vita-light.css">
<link rel="stylesheet" href="tokens/vita-emerald.css"> <!-- optional style delta -->
```
Then build markup with the class names documented in `components-reference.md`.

**3. Use the new style for real, inside APEX.** Paste `tokens/vita-emerald.less` into
Theme Roller's custom LESS editor (or wire it into a Theme Style's LESS files) for a
pixel-perfect, fully-computed compile.

## The eight Theme Styles included

| Style | Accent | Nav | Notes |
|---|---|---|---|
| Vita (light) | `#056AC8` blue | dark | Oracle default |
| Vita Dark | `#056AC8` blue | dark | Oracle official dark mode |
| Vita Red | `#DA1B1B` red | light | Oracle official variant |
| Vita Slate | `#505F6D` blue-gray | dark | Oracle official variant |
| Iris | `#00688C` teal | dark | Redwood-family "Sky" pillar |
| Redwood | `#5F7D4F` green | light | Oracle's flagship design system |
| Standard | `#2178B4` blue | dark | Legacy pre-Theme-42 — approximation, not pixel-exact |
| **Vita Emerald** | `#0E9F6E` green | dark | **New — built for this repo**, softer 6px radii |

Vita, Vita Dark, Vita Red, Vita Slate, Iris, and Redwood are all resolved from Oracle's
own official LESS source files (see links above). Standard predates Theme 42's token
system entirely and is included as a rough visual reference only.

## Credits

- **[Oracle APEX](https://apex.oracle.com/)** — Universal Theme 42 and the "Vita" style
  family this skill is derived from. All trademarks and the underlying theme belong to
  Oracle; see [`LICENSE`](./LICENSE) for how that interacts with this repo's MIT terms.
- **[Claude (Anthropic)](https://www.anthropic.com/claude)** — used to research, distill,
  and author this skill package and landing page.
- **Developer:** Md. Mahfuzul Amin (Raju), IT Manager & Oracle APEX Developer, OCP —
  [github.com/raju-bd](https://github.com/raju-bd)

## License

MIT for the original content in this repository — see [`LICENSE`](./LICENSE). Oracle
APEX and Universal Theme 42 remain Oracle's property and are governed by Oracle's own
licensing terms.
