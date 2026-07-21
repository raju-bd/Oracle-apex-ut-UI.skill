#!/usr/bin/env python3
"""
build-bundles.py — regenerate the two single-file bundles from the canonical
multi-file source (SKILL.md, components-reference.md, tokens/*.css, tokens/*.less).

Run this after editing anything under tokens/, SKILL.md, or components-reference.md,
so Oracle-apex-ut-UI.skill.md and Oracle-apex-ut-UI.skill.bundle.js stay in sync.

Usage:
    python3 build-bundles.py

No dependencies beyond the Python 3 standard library.
"""
import datetime
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def write(path, content):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(content)


def build_markdown_bundle():
    md_files = ["SKILL.md", "components-reference.md"]
    css_files = [
        ("tokens/vita-light.css", "css"),
        ("tokens/vita-dark.css", "css"),
        ("tokens/vita-red.css", "css"),
        ("tokens/vita-slate.css", "css"),
        ("tokens/iris.css", "css"),
        ("tokens/redwood.css", "css"),
        ("tokens/standard.css", "css"),
        ("tokens/vita-emerald.less", "less"),
        ("tokens/vita-emerald.css", "css"),
    ]

    out = []
    out.append("# Oracle APEX Universal Theme skill — Single-File Bundle\n")
    out.append(
        "> **This is a single-file, all-in-one version of the skill.** Everything that "
        "normally\n> lives across `SKILL.md`, `components-reference.md`, and the "
        "`tokens/` folder is inlined\n> below as labeled code blocks. Upload or paste "
        "*just this one file* into any AI\n> (Claude, ChatGPT, Gemini, a Claude "
        "Project, a Cursor rules file, etc.) and it has the\n> complete Oracle APEX "
        "Universal Theme 42 (Vita) design-token reference — no separate\n> file "
        "uploads needed.\n>\n> For a browser/dev environment instead of an AI, use "
        "the companion single-file bundle\n> `Oracle-apex-ut-UI.skill.bundle.js` — one "
        "`<script>` tag, no separate CSS requests.\n>\n> Generated from "
        "Oracle-apex-ut-UI.skill · https://github.com/raju-bd/Oracle-apex-ut-UI.skill\n"
    )
    out.append("\n---\n")

    part_num = 1
    parts = []
    bodies = []

    for fname in md_files:
        parts.append((part_num, fname))
        bodies.append((part_num, fname, read(fname).strip() + "\n", None))
        part_num += 1

    for fname, lang in css_files:
        parts.append((part_num, fname))
        bodies.append((part_num, fname, read(fname).strip(), lang))
        part_num += 1

    out.append("## Table of contents\n")
    for num, fname in parts:
        anchor = f"part-{num}-{fname.lower().replace('.', '').replace('/', '')}"
        out.append(f"{num}. [`{fname}`](#{anchor})\n")
    out.append("\n---\n")

    for num, fname, content, lang in bodies:
        out.append(f"\n## Part {num}: `{fname}`\n\n")
        if lang:
            out.append(f"```{lang}\n{content}\n```\n")
        else:
            out.append(content + "\n")
        out.append("\n---\n")

    out.append(
        f"\n*Bundle generated {datetime.date.today().isoformat()}. "
        f"Canonical multi-file source: https://github.com/raju-bd/Oracle-apex-ut-UI.skill*\n"
    )

    write("Oracle-apex-ut-UI.skill.md", "".join(out))
    print("Wrote Oracle-apex-ut-UI.skill.md")


def build_js_bundle():
    styles = [
        ("vita-light", "tokens/vita-light.css"),
        ("vita-dark", "tokens/vita-dark.css"),
        ("vita-red", "tokens/vita-red.css"),
        ("vita-slate", "tokens/vita-slate.css"),
        ("iris", "tokens/iris.css"),
        ("redwood", "tokens/redwood.css"),
        ("standard", "tokens/standard.css"),
        ("vita-emerald", "tokens/vita-emerald.css"),
    ]
    data = {key: read(path) for key, path in styles}
    js_data = json.dumps(data, ensure_ascii=False, indent=2)

    template = read("build-templates/bundle.template.js") if os.path.exists(
        os.path.join(ROOT, "build-templates/bundle.template.js")
    ) else DEFAULT_JS_TEMPLATE

    write("Oracle-apex-ut-UI.skill.bundle.js", template.replace("__TOKENS_JSON__", js_data))
    print("Wrote Oracle-apex-ut-UI.skill.bundle.js")


DEFAULT_JS_TEMPLATE = '''/*!
 * Oracle APEX Universal Theme skill — single-file browser bundle
 * Oracle APEX Universal Theme 42 (Vita) design tokens, self-contained.
 *
 * Usage — one script tag, nothing else to load:
 *   <script src="Oracle-apex-ut-UI.skill.bundle.js"></script>
 *   <script>
 *     ApexVitaSkill.use('vita-emerald'); // or 'vita-light', 'vita-dark', 'vita-red',
 *                                        // 'vita-slate', 'iris', 'redwood', 'standard'
 *   </script>
 *
 * API:
 *   ApexVitaSkill.use(styleName)   Switch the active Theme Style (default: vita-light)
 *   ApexVitaSkill.list()           Array of available style names
 *   ApexVitaSkill.current()        Currently active style name
 *   ApexVitaSkill.css(styleName)   Raw CSS text for a style, if you want to use it yourself
 *
 * Source / docs / full multi-file version:
 *   https://github.com/raju-bd/Oracle-apex-ut-UI.skill
 */
(function (root) {
  "use strict";

  var TOKENS = __TOKENS_JSON__;

  var BASE_ID = "apex-vita-base";
  var DELTA_ID = "apex-vita-delta";
  var current = null;

  function ensureTag(id) {
    var el = document.getElementById(id);
    if (!el) {
      el = document.createElement("style");
      el.id = id;
      document.head.appendChild(el);
    }
    return el;
  }

  function use(styleName) {
    styleName = styleName || "vita-light";
    if (!TOKENS[styleName]) {
      console.warn(
        "[ApexVitaSkill] Unknown style '" + styleName + "'. Available: " +
        Object.keys(TOKENS).join(", ")
      );
      return;
    }
    ensureTag(BASE_ID).textContent = TOKENS["vita-light"];
    var deltaTag = ensureTag(DELTA_ID);
    deltaTag.textContent = styleName === "vita-light" ? "" : TOKENS[styleName];
    current = styleName;
    document.dispatchEvent(
      new CustomEvent("apex-vita-skill:change", { detail: { style: styleName } })
    );
  }

  function list() { return Object.keys(TOKENS); }
  function css(styleName) { return TOKENS[styleName] || null; }
  function currentStyle() { return current; }

  if (typeof document !== "undefined") {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", function () { use("vita-light"); });
    } else {
      use("vita-light");
    }
  }

  root.ApexVitaSkill = { use: use, list: list, css: css, current: currentStyle };
})(typeof window !== "undefined" ? window : this);
'''


if __name__ == "__main__":
    build_markdown_bundle()
    build_js_bundle()
    print("Done. Both bundles regenerated from the canonical multi-file source.")
