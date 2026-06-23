#!/usr/bin/env python3
"""
tools/observability/build_decisions.py — Valoria open-decision register.

Centralizes the "loose ends": every open ruling, naming collision, unratified
provisional, flagged assumption, and structural gap that is scattered across the
corpus from many sessions — into ONE deduplicated, categorized, prioritized list
so you can see (and clear) the decisions you actually still owe.

Sources:
  - corpus sweep (designs/ canon/ params/ references/ sim/) for explicit markers:
        [OPEN — Jordan] · ruling pending · pending ratification · awaiting ratification
        [GAP …] · F1/F2 class · registry §10 candidate · [ASSUMPTION …]
  - references/module_contracts.yaml  (gap_notes, with affected systems)
  - tools/observability/lexicon.json  (abbreviation collisions, placeholders, censured)
  - canon/supersession_register.yaml  (what's already settled — shown for reassurance)

Output: decisions.json, decisions_data.js (window.VALORIA_DECISIONS), DECISIONS.md
Run:    python tools/observability/build_decisions.py
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    print("PyYAML required", file=sys.stderr); sys.exit(1)

REPO = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SWEEP_DIRS = ["designs", "canon", "params", "references", "sim", "engine"]

# lines that mention a marker but are ALREADY settled — do not list as open
RESOLVED_SKIP = re.compile(
    r"ratified|RESOLVED|resolved by|resolved\)|\bLANDED\b|superseded by|SUPERSED|STRUCK|"
    r"closed|settled|decided 20|ruling 20|✓|DONE\b|no longer", re.I)

# marker -> (category, priority, plain label).  P1 = genuine decisions you owe.
MARKERS = [
    (re.compile(r"\[OPEN\s*[—\-–]\s*Jordan", re.I), "ruling", 1, "Open ruling (awaiting Jordan)"),
    (re.compile(r"\[OPEN\s*[—\-–]", re.I), "ruling", 1, "Open item"),
    (re.compile(r"rename ruling pending|ruling pending", re.I), "naming", 1, "Ruling pending"),
    (re.compile(r"\bNAME COLLISION\b|name collision", re.I), "naming", 1, "Naming collision"),
    (re.compile(r"pending ratification|awaiting ratification|pending Jordan ratif|Jordan-vetoable|PROVISIONAL pending", re.I), "ratification", 1, "Awaiting ratification"),
    (re.compile(r"\bF2 class\b|F2-class|registry §10 candidate|NOT in registry", re.I), "mechanics", 2, "Unregistered Key (F2 / registry §10)"),
    (re.compile(r"\bF1 class\b|derived-write guard|direct aggregate write", re.I), "mechanics", 2, "Write-protection (F1)"),
    (re.compile(r"missing handoff|out-of-band|no §3 rule defined", re.I), "mechanics", 2, "Missing cross-scale handoff"),
    (re.compile(r"vocabulary unification|attribution conflict", re.I), "naming", 2, "Vocabulary / attribution conflict"),
    (re.compile(r"\[GAP[: \]]", re.I), "gap", 3, "Documented gap"),
    (re.compile(r"\[ASSUMPTION", re.I), "assumption", 3, "Flagged assumption (verify)"),
    (re.compile(r"\[STUB[: \]]|status:\s*stub", re.I), "stub", 3, "Stub / pointer only"),
    (re.compile(r"\bTODO\b|\bFIXME\b", re.I), "todo", 3, "TODO / FIXME"),
]

CATEGORY_LABEL = {
    "ruling": "Open rulings", "naming": "Naming & collisions", "ratification": "Ratifications",
    "mechanics": "Mechanical wiring", "gap": "Documented gaps", "assumption": "Flagged assumptions",
    "stub": "Stubs", "todo": "TODO / FIXME",
}


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())[:200]


def classify(line):
    for pat, cat, prio, label in MARKERS:
        if pat.search(line):
            return cat, prio, label
    return None


def main():
    decisions: dict[str, dict] = {}   # norm-text -> record

    def add(text, cat, prio, label, where, system=""):
        text = text.strip()
        if len(text) > 320:
            text = text[:317] + "…"
        k = norm(text)
        if not k:
            return
        rec = decisions.setdefault(k, {"text": text, "category": cat, "priority": prio,
                                       "label": label, "locations": [], "systems": [], "count": 0})
        rec["count"] += 1
        rec["priority"] = min(rec["priority"], prio)
        if where and where not in rec["locations"]:
            rec["locations"].append(where)
        if system and system not in rec["systems"]:
            rec["systems"].append(system)

    # ---- 1. corpus sweep ----
    files = 0
    for d in SWEEP_DIRS:
        base = REPO / d
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.suffix.lower() not in (".md", ".yaml", ".yml", ".py") or not p.is_file():
                continue
            files += 1
            rel = str(p.relative_to(REPO)).replace("\\", "/")
            try:
                for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    if "[" not in line and not any(w in line.lower() for w in
                            ("ruling pending", "collision", "ratification", "f2 class", "todo", "fixme")):
                        continue
                    if RESOLVED_SKIP.search(line) and "[OPEN" not in line.upper():
                        continue
                    c = classify(line)
                    if c:
                        cat, prio, label = c
                        add(line.strip().lstrip("#>-* "), cat, prio, label, f"{rel}:{i}")
            except Exception:
                continue

    # ---- 2. module_contracts gap_notes (structured, with systems) ----
    mc = REPO / "references" / "module_contracts.yaml"
    if mc.exists():
        try:
            raw = yaml.safe_load(mc.read_text(encoding="utf-8")) or {}
            for m in raw.get("modules", []):
                sysname = m.get("module", "")
                for note in (m.get("gap_notes") or []):
                    if RESOLVED_SKIP.search(note) and "[OPEN" not in note.upper():
                        continue
                    c = classify(note)
                    if c:
                        cat, prio, label = c
                        add(note, cat, prio, label, "references/module_contracts.yaml", sysname)
                for lp in (m.get("loops") or []):
                    if isinstance(lp, dict) and lp.get("open"):
                        add(f"{sysname}: feedback loop open — damper/cap unconfirmed",
                            "mechanics", 2, "Unannotated feedback loop",
                            "references/module_contracts.yaml", sysname)
        except yaml.YAMLError:
            pass

    # ---- 3. lexicon collisions / placeholders / censured ----
    lex = OUT / "lexicon.json"
    if lex.exists():
        L = json.loads(lex.read_text(encoding="utf-8"))
        for c in L.get("collisions", []):
            add(f"Abbreviation '{c['token']}' collides — owner '{c.get('expands_to','')}'. {c.get('note','')}",
                "naming", 1, "Abbreviation collision (ruling pending)",
                "references/name_collision_database.yaml")
        for ph in L.get("placeholders", []):
            if ph.get("status") != "expired":
                add(f"Placeholder name '{ph.get('placeholder_name','')}' (was '{ph.get('prior_name','')}') — needs canonical name [{ph.get('status','')}]",
                    "naming", 2, "Placeholder name (rename pending)", "canon/placeholder_names.yaml")

    # ---- 4. supersessions (settled — for reassurance / stale-vs-fresh) ----
    resolved = []
    sr = REPO / "canon" / "supersession_register.yaml"
    if sr.exists():
        try:
            raw = yaml.safe_load(sr.read_text(encoding="utf-8")) or {}
            for e in (raw.get("entries") or []):
                if isinstance(e, dict) and e.get("superseded_id"):
                    resolved.append({"id": e.get("superseded_id"),
                                     "scope": e.get("scope", ""),
                                     "superseded_by": e.get("superseded_by", ""),
                                     "date": e.get("superseded_date") or e.get("date", ""),
                                     "replacement": (e.get("replacement") or "")[:160]})
        except yaml.YAMLError:
            pass

    items = sorted(decisions.values(), key=lambda r: (r["priority"], -len(r["locations"]), r["category"]))
    by_cat, by_prio, by_file = {}, {1: 0, 2: 0, 3: 0}, {}
    for r in items:
        by_cat[r["category"]] = by_cat.get(r["category"], 0) + 1
        by_prio[r["priority"]] = by_prio.get(r["priority"], 0) + 1
        for loc in r["locations"]:
            f = loc.rsplit(":", 1)[0]
            by_file[f] = by_file.get(f, 0) + 1
    hotspots = sorted(by_file.items(), key=lambda kv: -kv[1])[:15]

    payload = {
        "meta": {"files_scanned": files, "total_open": len(items),
                 "by_category": by_cat, "by_priority": by_prio,
                 "hotspots": hotspots, "resolved_count": len(resolved)},
        "decisions": items, "resolved": resolved[:200],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "decisions.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (OUT / "decisions_data.js").write_text(
        "// AUTO-GENERATED — do not hand-edit.\nwindow.VALORIA_DECISIONS = "
        + json.dumps(payload, separators=(",", ":")) + ";\n", encoding="utf-8")

    # ---- DECISIONS.md (the readable register) ----
    md = []
    md.append("# Valoria — Open Decision Register\n")
    md.append("> Auto-generated by `tools/observability/build_decisions.py`. The scattered "
              "loose ends from every session, deduplicated and prioritized into one list.\n")
    md.append(f"**{len(items)} open items** across {files} files "
              f"· P1 {by_prio.get(1,0)} · P2 {by_prio.get(2,0)} · P3 {by_prio.get(3,0)} "
              f"· {len(resolved)} already settled (supersessions).\n")
    md.append("\n## By category\n")
    for cat, n in sorted(by_cat.items(), key=lambda kv: -kv[1]):
        md.append(f"- **{CATEGORY_LABEL.get(cat,cat)}** — {n}")
    md.append("\n## Hotspot files (where the loose ends cluster)\n")
    for f, n in hotspots:
        md.append(f"- `{f}` — {n}")

    PER_CAT_CAP = 60

    def section(title, prio):
        rows = [r for r in items if r["priority"] == prio]
        if not rows:
            return
        md.append(f"\n---\n\n## {title}  ({len(rows)})\n")
        cur = None
        shown = 0
        for r in rows:
            if r["category"] != cur:
                cur = r["category"]
                catrows = [x for x in rows if x["category"] == cur]
                md.append(f"\n### {CATEGORY_LABEL.get(cur,cur)} ({len(catrows)})\n")
                shown = 0
            if shown >= PER_CAT_CAP:
                if shown == PER_CAT_CAP:
                    md.append(f"- _…and more in this category — see `decisions.json`._")
                    shown += 1
                continue
            sysnote = f" _(systems: {', '.join(r['systems'])})_" if r["systems"] else ""
            loc = r["locations"][0] if r["locations"] else ""
            more = f" +{len(r['locations'])-1} more" if len(r["locations"]) > 1 else ""
            md.append(f"- {r['text']}{sysnote}  \n  ↳ `{loc}`{more}")
            shown += 1
    section("P1 — decide first (the real rulings you owe)", 1)
    section("P2 — decide soon (structural & naming)", 2)
    # P3 = hygiene tail — summarize, don't enumerate
    p3 = [r for r in items if r["priority"] == 3]
    if p3:
        md.append(f"\n---\n\n## P3 — cleanup backlog ({len(p3)})  — summarized\n")
        md.append("_Flagged assumptions, documented gaps, stubs, and TODOs. Not decisions per se — "
                  "verification/hygiene work. Full list in `decisions.json`._\n")
        p3cat = {}
        for r in p3:
            p3cat[r["category"]] = p3cat.get(r["category"], 0) + 1
        for c, n in sorted(p3cat.items(), key=lambda kv: -kv[1]):
            md.append(f"- **{CATEGORY_LABEL.get(c,c)}** — {n}")
    md.append("\n---\n\n## Already settled (recent supersessions)\n")
    md.append("_These are NOT open — shown so stale references don't read as live decisions "
              "(your “stale vs fresh” problem). Before treating any old ED/PP as authoritative, "
              "check `canon/supersession_register.yaml`._\n")
    for r in resolved[:40]:
        md.append(f"- **{r.get('id','')}** — {r.get('scope','')[:120]} → _{r.get('replacement','') or r.get('superseded_by','')}_")
    (OUT / "DECISIONS.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print("Valoria decision register built:")
    print(f"  open={len(items)}  (P1={by_prio.get(1,0)} P2={by_prio.get(2,0)} P3={by_prio.get(3,0)})"
          f"  resolved={len(resolved)}  files_scanned={files}")
    print(f"  by category: {by_cat}")
    print(f"  -> {OUT/'DECISIONS.md'}  /  decisions.json  /  decisions_data.js")
    return payload


if __name__ == "__main__":
    main()
