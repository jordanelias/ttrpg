"""Render results.json into a readable stress-matrix report (markdown + console)."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "results.json")))
m = d["meta"]
L = []
def p(s=""): L.append(s)

p(f"# Personal-Combat Stress Matrix — Results")
p(f"_N={m['n_per_position']}/position (×2 swapped), max_bouts={m['max_bouts']}, seed={m['seed']}; "
  f"mirror baseline = {m['mirror_sanity']['win']}% win / {m['mirror_sanity']['draw']}% draw. "
  f"Baseline: uniform-4, arming, light armour, tradition none._")
p()
p("> Read every cell as a **marginal vs the same-config baseline** (the @4 / ×1.0 / full-engine cell), "
  "not an absolute — the single-seed mirror sits at "
  f"{m['mirror_sanity']['win']}%, so the fair point is there, not 50.")

# ── BLOCK 1 ──
b1 = d.get("block1_attributes", {})
if b1:
    base = b1["history"]["4"]
    p("\n## Block 1 — Attribute impact (win% vs uniform-4, swept 1→7)\n")
    p("| Attribute | @1 | @2 | @3 | @4 | @5 | @6 | @7 | swing(7−1) |")
    p("|---|--|--|--|--|--|--|--|--|")
    order = sorted(b1, key=lambda a: -(b1[a]["7"] - b1[a]["1"]))
    for a in order:
        r = b1[a]
        swing = round(r["7"] - r["1"], 1)
        p(f"| **{a}** | {r['1']} | {r['2']} | {r['3']} | {r['4']} | {r['5']} | {r['6']} | {r['7']} | {swing:+} |")

# ── BLOCK 2 ──
b2 = d.get("block2_derived", {})
if b2:
    p("\n## Block 2 — Derived-score leverage (one fighter's derived value ×0.5 / ×1.5, attributes equal)\n")
    p("| Derived score | ×0.5 win% | ×1.5 win% | spread | leverage |")
    p("|---|--|--|--|--|")
    rows = sorted(b2, key=lambda k: -(b2[k]["1.5"] - b2[k]["0.5"]))
    for k in rows:
        lo, hi = b2[k]["0.5"], b2[k]["1.5"]
        spread = round(hi - lo, 1)
        tag = "★★★ dominant" if spread >= 50 else ("★★ strong" if spread >= 25 else ("★ moderate" if spread >= 10 else "· minor"))
        p(f"| `{k}` | {lo} | {hi} | {spread:+} | {tag} |")

# ── BLOCK 3 ──
b3 = d.get("block3_state_graph", {})
if b3:
    full = b3.get("_full_baseline", {})
    p("\n## Block 3 — State-graph component ablation (Δwin% vs full engine, by matchup)\n")
    p(f"_Full-engine panel baseline (A win%): mirror {full.get('mirror')} · reach {full.get('reach')} · "
      f"skill {full.get('skill')} · armour {full.get('armour')}. Δ = ablated − full; "
      f"large |Δ| = load-bearing, ~0 = inert in that matchup._\n")
    p("| Component (ablated) | mirror Δ | mirror draw Δ | reach Δ | skill Δ | armour Δ | max\\|Δ\\| |")
    p("|---|--|--|--|--|--|--|")
    comps = [c for c in b3 if c != "_full_baseline"]
    def maxabs(c):
        r = b3[c]
        return max(abs(r.get(k, 0)) for k in ("mirror", "reach", "skill", "armour"))
    for c in sorted(comps, key=lambda c: -maxabs(c)):
        r = b3[c]
        p(f"| `{c}` | {r.get('mirror',0):+} | {r.get('mirror_draw_delta',0):+} | {r.get('reach',0):+} | "
          f"{r.get('skill',0):+} | {r.get('armour',0):+} | {maxabs(c)} |")

out = os.path.join(HERE, "results.md")
open(out, "w", encoding="utf-8").write("\n".join(L))
print("\n".join(L))
print(f"\n[wrote {out}]")
