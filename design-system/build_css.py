#!/usr/bin/env python3
"""Generate tokens.css from tokens.json.

Usage: python3 design-system/build_css.py
Reads design-system/tokens.json and writes design-system/tokens.css.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
tokens = json.loads((HERE / "tokens.json").read_text(encoding="utf-8"))

themes = [t["id"] for t in tokens["color"]["themes"]]
first = themes[0]


def ref(v):
    """Turn a {alias} into var(--alias)."""
    m = re.fullmatch(r"\{([A-Za-z0-9_.-]+)\}", v)
    return f"var(--{m.group(1)})" if m else v


def per_theme(entries):
    out = {t: [] for t in themes}
    for e in entries:
        v = e["value"]
        if isinstance(v, str):
            out[first].append((e["name"], ref(v)))
            continue
        base = v.get(first)
        out[first].append((e["name"], ref(base)))
        for t in themes[1:]:
            if t in v and v[t] != base:
                out[t].append((e["name"], ref(v[t])))
    return out


colors = per_theme(tokens["color"]["tokens"])
shadows = per_theme(tokens.get("shadow", {}).get("tokens", []))


def block(selector, pairs, indent="  "):
    body = "\n".join(f"{indent}--{n}: {v};" for n, v in pairs)
    return f"{selector} {{\n{body}\n}}\n"


lines = ["/* KDBS design tokens — generated from tokens.json by build_css.py. Do not edit by hand. */\n"]

# Fonts
for f in tokens["type"]["fonts"]:
    lines.append(
        "@font-face {\n"
        f"  font-family: \"{f['family']}\";\n"
        f"  src: url(\"{f['file']}\") format(\"woff2\");\n"
        f"  font-weight: {f['weight']};\n"
        "  font-style: normal;\n"
        "  font-display: swap;\n"
        "}\n"
    )

# Theme-invariant scales
static = [(n, v) for n, v in [(e["name"], e["value"]) for e in tokens["spacing"]["tokens"] + tokens["radius"]["tokens"]]]
static += [(f"font-{k}", v) for k, v in tokens["type"]["families"].items()]
lines.append(block(":root", static))

# Colors + shadows: first theme on :root, others by data-theme and by system preference
lines.append(block(f":root,\n[data-theme=\"{first}\"]", colors[first] + shadows[first]))
for t in themes[1:]:
    pairs = colors[t] + shadows[t]
    lines.append(block(f"[data-theme=\"{t}\"]", pairs))
    inner = block(f"  :root:not([data-theme])", pairs, indent="    ").replace("}\n", "  }\n")
    lines.append(f"@media (prefers-color-scheme: {t}) {{\n{inner}}}\n")

# Type styles as utility classes
for g in tokens["type"]["groups"]:
    for s in g["styles"]:
        fam = s.get("family", g["family"])
        props = [f"font-family: var(--font-{fam})", f"font-size: {s['fontSize']}",
                 f"line-height: {s['lineHeight']}", f"font-weight: {s['fontWeight']}"]
        if "letterSpacing" in s:
            props.append(f"letter-spacing: {s['letterSpacing']}")
        lines.append(f".kd-type-{s['name']} {{ " + "; ".join(props) + "; }\n")

(HERE / "tokens.css").write_text("\n".join(lines), encoding="utf-8")
print("wrote", HERE / "tokens.css")
