# apex-vita-ui.skill

**A drop-in design-token reference for Oracle APEX Universal Theme 42 — the "Vita" style family — so any AI or any developer can produce HTML/CSS that looks and behaves like a real APEX app, without needing an APEX instance running.**

🔗 **Live demo / landing page:** open [`index.html`](./index.html) locally, or enable GitHub Pages on this repo (Settings → Pages → root) and visit `https://raju-bd.github.io/apex-vita-ui.skill/`.

⭐ **If this saves you time, star the repo:** [github.com/raju-bd/apex-vita-ui.skill](https://github.com/raju-bd/apex-vita-ui.skill)

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
apex-vita-ui.skill/
├── index.html                  ← landing page / live demo (this repo, rendered)
├── README.md                   ← you are here
├── LICENSE                     ← MIT (see note on Oracle's own terms inside)
├── SKILL.md                    ← the skill itself — usage guide + token map + workflow
├── components-reference.md     ← real APEX class names + markup patterns
├── example.html                ← minimal dashboard demo with a live style switcher
└── tokens/
    ├── vita-light.css          ← baseline Vita (light/default), ~300 resolved tokens
    ├── vita-dark.css           ← Vita Dark deltas (load after vita-light.css)
    ├── vita-red.css            ← Vita Red deltas (official Oracle variant)
    ├── vita-emerald.less       ← NEW custom Theme Style — Theme-Roller-ready LESS source
    └── vita-emerald.css        ← NEW custom Theme Style — browser-ready resolved tokens
```

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

## The four Theme Styles included

| Style | Accent | Nav | Notes |
|---|---|---|---|
| Vita (light) | `#056AC8` blue | dark | Oracle default |
| Vita Dark | `#056AC8` blue | dark | Oracle official dark mode |
| Vita Red | `#DA1B1B` red | light | Oracle official variant |
| **Vita Emerald** | `#0E9F6E` green | dark | **New — built for this repo**, softer 6px radii |

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
