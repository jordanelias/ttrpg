#!/usr/bin/env python3
"""
tools/observability/build_lexicon.py — Valoria canonical lexicon extractor.

Makes the *terminological* opacity transparent: every definition, abbreviation,
name / alias / synonym / legacy name, every abbreviation COLLISION, every
deprecated / censured / placeholder term, and every cross-scale HANDSHAKE
(the inter-container ripples) — assembled from the canonical registries into one
searchable dataset that the System Transparency Console renders alongside the
propagation graph.

Sources (canon — nothing invented):
  references/alias_registry.yaml          mechanical names: canonical/abbr/aliases/legacy/category
  references/name_collision_database.yaml  abbreviation owners + silos + COLLISION notes
  references/synonym_registry.yaml         different words for the same concept
  references/deprecated_terms_registry.yaml renamed/retired terms
  references/censured_vocabulary.yaml      do-not-use terms + replacements
  references/proper_noun_registry.yaml     world entities (characters/territories/factions…)
  registers/placeholder_names.yaml             placeholder vs prior/canonical names
  references/descriptor_registry.yaml      attributes/stats/axes/styles + legacy aliases
  references/glossary.md                   authoritative definitions (term/abbr/range/desc)
  designs/architecture/scale_transitions_v30.md  the cross-scale handshakes (§3/§5/§12)

Output: tools/observability/lexicon.json and lexicon_data.js (window.VALORIA_LEXICON).
Run:    python tools/observability/build_lexicon.py
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
REF = REPO / "references"


def load_yaml(p: Path):
    if not p.exists():
        return None
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        print(f"  ! yaml error in {p.name}: {e}", file=sys.stderr)
        return None


def listify(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def strip_md(s):
    return re.sub(r"[*`]", "", str(s)).strip()


def src_rel(p: Path):
    return str(p.relative_to(REPO)).replace("\\", "/")


def main():
    terms: dict[str, dict] = {}        # key=lower(canonical) -> term record
    abbreviations: dict[str, dict] = {}
    collisions: list[dict] = []
    deprecated: list[dict] = []
    censured: list[dict] = []
    placeholders: list[dict] = []
    handshakes: list[dict] = []
    silo_of: dict[str, str] = {}

    def term(canon, **kw):
        if not canon:
            return None
        k = strip_md(canon).lower()
        rec = terms.setdefault(k, {"canonical": strip_md(canon), "type": "", "category": "",
                                   "silo": "", "abbreviations": [], "aliases": [], "legacy": [],
                                   "definition": "", "range": "", "status": "canonical",
                                   "replacement": "", "collision_note": "", "sources": []})
        for f in ("abbreviations", "aliases", "legacy", "sources"):
            if f in kw:
                for x in listify(kw.pop(f)):
                    x = strip_md(x)
                    if x and x not in rec[f]:
                        rec[f].append(x)
        for f, v in kw.items():
            if v and not rec.get(f):
                rec[f] = strip_md(v) if isinstance(v, str) else v
        return rec

    # ---- alias_registry.yaml (recursive: any dict carrying 'canonical') ----
    ar = load_yaml(REF / "alias_registry.yaml")
    s_ar = src_rel(REF / "alias_registry.yaml")

    def walk_alias(node, group=""):
        if isinstance(node, dict):
            if "canonical" in node and isinstance(node.get("canonical"), str):
                term(node["canonical"], abbreviations=node.get("abbreviations"),
                     aliases=node.get("aliases"), legacy=node.get("legacy"),
                     category=node.get("category", group), range=node.get("range", ""),
                     collision_note=node.get("collision_note", ""), type="mechanic", sources=s_ar)
            else:
                for kk, vv in node.items():
                    walk_alias(vv, group if not isinstance(vv, dict) else kk)
    if isinstance(ar, dict):
        for g, v in ar.items():
            if isinstance(v, dict):
                walk_alias(v, g)

    # ---- name_collision_database.yaml: abbreviation owners + silos + collisions ----
    ncd_path = REF / "name_collision_database.yaml"
    ncd = load_yaml(ncd_path)
    s_ncd = src_rel(ncd_path)
    # harvest inline COLLISION/NOTE comments by raw line (yaml drops comments)
    comment_by_abbr = {}
    if ncd_path.exists():
        for ln in ncd_path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*([A-Za-z0-9]+):\s*\{.*?\}\s*#\s*(.+)$", ln)
            if m:
                comment_by_abbr[m.group(1)] = m.group(2).strip()
    if isinstance(ncd, dict):
        for abbr, info in (ncd.get("abbreviations") or {}).items():
            if not isinstance(info, dict):
                continue
            note = comment_by_abbr.get(abbr, "")
            rec = {"abbr": abbr, "expands_to": info.get("term", ""), "silo": info.get("silo", ""),
                   "status": info.get("status", ""), "scope": info.get("scope", ""),
                   "exempt": bool(info.get("exempt")), "note": note, "sources": [s_ncd]}
            abbreviations[abbr] = rec
            if info.get("term"):
                t = term(info["term"], abbreviations=abbr, silo=f"§{info.get('silo','')}", sources=s_ncd)
            if "COLLISION" in note.upper():
                collisions.append({"token": abbr, "kind": "abbreviation",
                                   "owner": info.get("term", ""), "note": note,
                                   "status": info.get("status", ""), "source": s_ncd})
        # silo term registry
        for sk, sv in (ncd.get("terms") or {}).items():
            if isinstance(sv, dict) and sv.get("terms"):
                sname = f"{sk} · {sv.get('name','')}"
                for t in sv["terms"]:
                    silo_of[strip_md(t).lower()] = sname
                    term(t, silo=sname, sources=s_ncd)

    # ---- synonym_registry.yaml ----
    syn = load_yaml(REF / "synonym_registry.yaml")
    s_syn = src_rel(REF / "synonym_registry.yaml")
    if isinstance(syn, dict):
        for e in syn.get("entries", []) or []:
            if not isinstance(e, dict):
                continue
            term(e.get("canonical"), aliases=e.get("aliases___synonyms"),
                 definition=e.get("concept", ""), type="concept", sources=s_syn)

    # ---- deprecated_terms_registry.yaml ----
    dep = load_yaml(REF / "deprecated_terms_registry.yaml")
    s_dep = src_rel(REF / "deprecated_terms_registry.yaml")
    if isinstance(dep, dict):
        for sec, val in dep.items():
            if isinstance(val, list):
                for e in val:
                    if isinstance(e, dict) and (e.get("old") or e.get("term")):
                        old, new = e.get("old") or e.get("term"), e.get("new", "")
                        deprecated.append({"old": strip_md(old), "new": strip_md(new),
                                           "patch": e.get("patch", ""), "section": sec})
                        if new:
                            term(new, legacy=old, sources=s_dep)
                        t = term(old, legacy=old, status="deprecated", replacement=new, sources=s_dep)

    # ---- censured_vocabulary.yaml ----
    cen = load_yaml(REF / "censured_vocabulary.yaml")
    s_cen = src_rel(REF / "censured_vocabulary.yaml")
    if isinstance(cen, dict):
        for e in cen.get("terms", []) or []:
            if not isinstance(e, dict):
                continue
            censured.append({"term": strip_md(e.get("term", "")), "reason": e.get("reason", ""),
                             "replacement": e.get("replacement") or "", "authority": e.get("authority", ""),
                             "canonical_full": e.get("canonical_full", "")})
            term(e.get("canonical_full") or e.get("term"), aliases=e.get("term"),
                 status="censured", replacement=e.get("replacement") or "",
                 collision_note=e.get("reason", ""), sources=s_cen)

    # ---- proper_noun_registry.yaml ----
    pn = load_yaml(REF / "proper_noun_registry.yaml")
    s_pn = src_rel(REF / "proper_noun_registry.yaml")
    if isinstance(pn, dict):
        for cat, entries in pn.items():
            if not isinstance(entries, dict):
                continue
            for _id, e in entries.items():
                if isinstance(e, dict) and e.get("canonical"):
                    term(e["canonical"], aliases=e.get("aliases"), type=cat.rstrip("s"),
                         category=cat, definition=e.get("role", ""),
                         sources=e.get("source", s_pn))

    # ---- placeholder_names.yaml ----
    ph = load_yaml(REPO / "registers" / "placeholder_names.yaml")
    s_ph = "registers/placeholder_names.yaml"
    if isinstance(ph, dict):
        for e in ph.get("placeholders", []) or []:
            if not isinstance(e, dict):
                continue
            placeholders.append({"placeholder_name": e.get("placeholder_name", ""),
                                 "prior_name": e.get("prior_name", ""),
                                 "status": e.get("status", ""), "id": e.get("id", "")})
            if e.get("placeholder_name"):
                term(e["placeholder_name"], aliases=e.get("prior_name"),
                     status="placeholder", type="module", sources=s_ph)

    # ---- descriptor_registry.yaml ----
    dr = load_yaml(REF / "descriptor_registry.yaml")
    s_dr = src_rel(REF / "descriptor_registry.yaml")

    def walk_desc(node):
        if isinstance(node, dict):
            nm = node.get("name") or node.get("canonical")
            if nm and isinstance(nm, str):
                term(nm, aliases=node.get("aliases"), type=node.get("kind", "descriptor"),
                     category=node.get("domain", node.get("kind", "")), sources=s_dr)
            for v in node.values():
                walk_desc(v)
        elif isinstance(node, list):
            for v in node:
                walk_desc(v)
    walk_desc(dr)

    # ---- glossary.md markdown tables (definitions + abbreviations + ranges) ----
    gl = REPO / "references" / "glossary.md"
    s_gl = "references/glossary.md"
    if gl.exists():
        part = ""
        in_tbl = False
        cols = []
        for ln in gl.read_text(encoding="utf-8").splitlines():
            h = re.match(r"^#{2,4}\s+(.*)", ln)
            if h:
                part = strip_md(h.group(1)); in_tbl = False; continue
            if ln.strip().startswith("|"):
                cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                if re.search(r"abbr", ln, re.I) and not in_tbl:
                    cols = [c.lower() for c in cells]; in_tbl = True; continue
                if set(ln.replace("|", "").strip()) <= {"-", ":", " "}:
                    continue
                if in_tbl and len(cells) >= 2:
                    full = strip_md(cells[0])
                    abbr = cells[1].replace("—", "").replace("*", "").strip()
                    rng = cells[2].strip() if len(cells) > 2 else ""
                    desc = strip_md(cells[-1])
                    if full and not full.lower().startswith("full term"):
                        term(full, abbreviations=(abbr if abbr and len(abbr) <= 6 else None),
                             definition=desc, range=rng, category=part, sources=s_gl)
            else:
                in_tbl = False

    # ---- handshakes: scale_transitions_v30.md §3 handoffs + §5 Domain Echo ----
    st = REPO / "systems" / "_architecture" / "scale_transitions_v30.md"
    s_st = "designs/architecture/scale_transitions_v30.md"
    if st.exists():
        lines = st.read_text(encoding="utf-8").splitlines()
        h_re = re.compile(r"^###\s+§(3\.\d+)\s+(.+)")
        arrow = re.compile(r"(.+?)\s*(?:→|↔|->)\s*(.+)")
        for i, ln in enumerate(lines):
            m = h_re.match(ln)
            if m:
                sec, title = m.group(1), strip_md(m.group(2))
                # first non-empty prose line after the heading = the rule gist
                gist = ""
                for j in range(i + 1, min(i + 8, len(lines))):
                    t = lines[j].strip()
                    if t and not t.startswith("#") and not t.startswith("|") and not t.startswith(">"):
                        gist = strip_md(t); break
                am = arrow.match(re.sub(r"\([^)]*\)", "", title))
                handshakes.append({"id": f"§{sec}", "name": title,
                                   "from": strip_md(am.group(1)) if am else "",
                                   "to": strip_md(am.group(2)) if am else "",
                                   "gist": gist[:300], "source": f"{s_st} §{sec}"})

    # ---- cross-link terms to graph nodes (best effort) ----
    graph_path = OUT / "graph.json"
    if graph_path.exists():
        g = json.loads(graph_path.read_text(encoding="utf-8"))
        sys_ids = {s["id"] for s in g["systems"]}
        key_ids = {k["id"] for k in g["keys"]}
        scalar_names = {}
        for sc in g["scalars"]:
            scalar_names.setdefault(re.sub(r"[^a-z0-9]", "", sc["name"].lower()), []).append(sc["id"])
        for rec in terms.values():
            cands = [rec["canonical"]] + rec["aliases"] + rec["abbreviations"]
            links = []
            for c in cands:
                norm = re.sub(r"[^a-z0-9]", "_", c.lower()).strip("_")
                flat = re.sub(r"[^a-z0-9]", "", c.lower())
                if norm in sys_ids:
                    links.append({"kind": "system", "id": norm})
                if norm in key_ids:
                    links.append({"kind": "key", "id": norm})
                if flat in scalar_names:
                    for sid in scalar_names[flat]:
                        links.append({"kind": "scalar", "id": sid})
            if links:
                seen = set(); uniq = []
                for l in links:
                    if (l["kind"], l["id"]) not in seen:
                        seen.add((l["kind"], l["id"])); uniq.append(l)
                rec["links"] = uniq

    # ---- name index (reverse lookup: any alias/abbr/legacy -> canonical) ----
    name_index = {}
    for k, rec in terms.items():
        for nm in [rec["canonical"], *rec["aliases"], *rec["abbreviations"], *rec["legacy"]]:
            name_index.setdefault(strip_md(nm).lower(), [])
            if rec["canonical"] not in name_index[strip_md(nm).lower()]:
                name_index[strip_md(nm).lower()].append(rec["canonical"])

    term_list = sorted(terms.values(), key=lambda t: t["canonical"].lower())
    payload = {
        "meta": {
            "generated_from": [s_ar, s_ncd, s_syn, s_dep, s_cen, s_pn, s_ph, s_dr, s_gl, s_st],
            "stats": {
                "terms": len(term_list),
                "abbreviations": len(abbreviations),
                "collisions": len(collisions),
                "deprecated": len(deprecated),
                "censured": len(censured),
                "placeholders": len(placeholders),
                "handshakes": len(handshakes),
                "with_definition": sum(1 for t in term_list if t["definition"]),
                "linked_to_graph": sum(1 for t in term_list if t.get("links")),
            },
        },
        "terms": term_list,
        "abbreviations": sorted(abbreviations.values(), key=lambda a: a["abbr"]),
        "collisions": collisions,
        "deprecated": deprecated,
        "censured": censured,
        "placeholders": placeholders,
        "handshakes": handshakes,
        "name_index": name_index,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "lexicon.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    data = "window.VALORIA_LEXICON = " + json.dumps(payload, separators=(",", ":")) + ";"
    (OUT / "lexicon_data.js").write_text("// AUTO-GENERATED — do not hand-edit.\n" + data + "\n",
                                         encoding="utf-8")
    s = payload["meta"]["stats"]
    print("Valoria lexicon built:")
    print(f"  terms={s['terms']} ({s['with_definition']} defined, {s['linked_to_graph']} linked to graph)")
    print(f"  abbreviations={s['abbreviations']}  collisions={s['collisions']}"
          f"  deprecated={s['deprecated']}  censured={s['censured']}"
          f"  placeholders={s['placeholders']}  handshakes={s['handshakes']}")
    print(f"  -> {OUT / 'lexicon.json'}")
    return payload


if __name__ == "__main__":
    main()
