#!/usr/bin/env python3
"""Per-subsystem glossary + master term index — GENERATED, never hand-edited.

WHY THIS IS GENERATED AND THE OLD ONE WAS NOT.

`references/glossary.md` is hand-maintained, its stated maintainer (the `valoria-orchestrator`
skill) was retired to `deprecated/skills/` on 2026-06-28, and its own header records the content as
"last swept 2026-04-30". A curated glossary with no live maintainer is the rot pattern this repo
keeps re-finding. That file is NOT replaced here — it stays the authority for *curated definitions*,
because a scanner cannot write a definition. What it could never do by hand is answer **"where does
this term actually appear?"** across a corpus that moved 1,700 files in one week. That is what this
generates.

Its own header even filed the work: *"Building a real glossary mirror into names_index + the
consistency checker is a follow-on tooling change."*

WHAT IT COMPOSES ON (§0: find the single-owner primitive, do not re-implement).

  names_index.yaml          canonical display names, aliases, legacy spellings, category
  glossary.md               curated term -> expansion/description tables (11 parts)
  descriptor_registry.yaml  the descriptor roster
  mechanics_index.yaml      named mechanics
  systems/*/_identifier_census.yaml
                            per-subsystem identifiers WITH their source docs and a
                            built/unbuilt disposition — `tools/build_identifier_census.py`,
                            authored on Jordan's 2026-08-04 direction. This is the closest
                            existing primitive and the reason this file is a VIEW, not a scanner.

No term list is invented here. Every entry traces to one of the five sources above via its
`sources` field.

THE MATCHING HAZARD, AND WHY THIS DOES NOT REPEAT IT.

The 2026-08-06 vector audit's Mode C reported 97.5% of all citation edges as "notional" because
ubiquitous common nouns (`Crown`, `Standing`, `Church`) co-occur with everything. A glossary built
on naive substring matching produces exactly that failure with a friendlier face: `Mind` matches
"reminded", `CI` matches "specific".

So: matching is word-boundary anchored and case-sensitive, single-character and digit-only terms are
refused outright, and **every term carries its raw hit count**. Terms whose breadth exceeds
AMBIGUITY_FLOOR files are marked `ambiguous: true` and rendered with a warning rather than silently
presented as meaningful. Breadth is reported, never hidden — a term in 200 files is a fact about the
term, and the reader is told so instead of being handed a tidy number.

OUTPUTS
  references/glossary/GLOSSARY_<subsystem>.md   one per subsystem; repetitions intended — a term
                                                used by three subsystems appears in all three,
                                                each with a cross-reference to the others
  references/glossary/MASTER_GLOSSARY.md        every term once, with EVERY location
  references/glossary/glossary.json             machine-readable

Run: python3 tools/observability/build_glossary.py [--check]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import obs_core as core  # noqa: E402

OUT_DIR = REPO / "references" / "glossary"

# Corpus scanned for term LOCATIONS. Design + code surfaces only: audit prose and workplans are
# discussion, not places a term is defined or used normatively.
SCAN_ROOTS = ("systems", "canon", "engine", "godot", "proposals")
SCAN_SUFFIXES = (".md",)

# A term matching in more than this many files is reported but flagged: at that breadth the match
# is telling you about English, not about Valoria.
AMBIGUITY_FLOOR = 60

# Terms too short to word-boundary match safely. Refused, and REPORTED as refused (see `refused`
# in the JSON) so the exclusion is visible rather than silent — the audit doctrine is surface,
# never cull.
#
# WHY 2 AND NOT 3. The first cut used 3 and silently refused MS, CI, IP, PI, TS, CP, TD, RS, DD —
# i.e. the repo's NINE most-used abbreviations. glossary.md's own usage rules name `Thread
# Sensitivity (TS)` and `CI` explicitly; MS is Mending Stability, RS is Rendering Stability. A
# glossary that omits those is not a glossary. Two-character terms are admitted ONLY when
# uppercase, because matching is case-sensitive and word-boundary anchored: `\bCI\b` finds the
# abbreviation and not "specific". Measured before lowering the floor — MS 503 hits/51 files,
# CI 702/68, TS 683/78, RS 233/41, DD 0/0 — plausible breadth, no runaway.
MIN_TERM_LEN = 2


def _subsystem_of(rel: str) -> str:
    """Which subsystem does a repo-relative path belong to?"""
    parts = rel.split("/")
    if parts[0] == "systems" and len(parts) > 1:
        return parts[1]
    return parts[0]


# ── sources ───────────────────────────────────────────────────────────────────────────────────

def _from_names_index() -> dict[str, dict]:
    p = REPO / "references" / "names_index.yaml"
    out: dict[str, dict] = {}
    if not p.exists():
        return out
    data = yaml.safe_load(p.read_text()) or {}
    for ident, e in (data.get("entries") or {}).items():
        if not isinstance(e, dict):
            continue
        canon = e.get("canonical")
        if not canon:
            continue
        out.setdefault(canon, {}).update({
            "term": canon,
            "category": e.get("category"),
            "aliases": [a for a in (e.get("aliases") or []) if a],
            "legacy": [l for l in (e.get("legacy") or []) if l],
            "registry_id": ident,
        })
        out[canon].setdefault("sources", set()).add("names_index")
    return out


def _from_glossary_md() -> dict[str, dict]:
    """Parse the curated tables. Definitions come from here and nowhere else.

    COLUMN-COUNT AGNOSTIC ON PURPOSE. The first cut of this parser required >=4 columns and
    silently captured 31 of ~130 rows, because the file mixes 3-, 4- and 7-column tables (93 rows
    are 3-column). A parser that quietly reads a quarter of its source is the same defect class as
    a gate reporting clean over nothing. Term = first cell, description = last cell, abbreviation =
    the middle cell only when it is short enough to be one.
    """
    p = REPO / "references" / "glossary.md"
    out: dict[str, dict] = {}
    if not p.exists():
        return out
    part = None
    for line in p.read_text().splitlines():
        if line.startswith("## PART"):
            part = line.lstrip("# ").strip()
            continue
        s = line.strip()
        if not s.startswith("|") or not s.endswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 2:
            continue
        term, desc = cells[0], cells[-1]
        if (not term or not desc
                or term.lower() in ("full term", "term", "name", "identifier")
                or set(term) <= set("-: ")):        # separator row
            continue
        abbr = None
        if len(cells) >= 3:
            mid = cells[1]
            if mid and mid != "—" and len(mid) <= 8:
                abbr = mid
        e = out.setdefault(term, {"term": term})
        e["definition"] = desc
        e["abbreviation"] = abbr
        e["glossary_part"] = part
        e.setdefault("sources", set()).add("glossary.md")
    return out


def _from_identifier_census() -> dict[str, dict]:
    """Per-subsystem identifiers, with the docs that name them and a built/unbuilt disposition."""
    out: dict[str, dict] = {}
    for p in sorted(REPO.glob("systems/*/_identifier_census.yaml")):
        data = yaml.safe_load(p.read_text()) or {}
        sub = data.get("subsystem") or p.parent.name
        for term, e in (data.get("identifiers") or {}).items():
            if not isinstance(e, dict):
                continue
            entry = out.setdefault(term, {"term": term})
            entry.setdefault("sources", set()).add("identifier_census")
            entry.setdefault("census", {})[sub] = {
                "disposition": e.get("disposition"),
                "purpose": (e.get("purpose") or None),
                "built_in": e.get("built_in") or [],
                "docs": e.get("docs") or [],
            }
    return out


def _from_mechanics_index() -> dict[str, dict]:
    p = REPO / "registers" / "mechanics_index.yaml"
    out: dict[str, dict] = {}
    if not p.exists():
        return out
    data = yaml.safe_load(p.read_text()) or {}
    mechs = data.get("mechanics") or data
    if isinstance(mechs, dict):
        for name, e in mechs.items():
            if not isinstance(name, str):
                continue
            entry = out.setdefault(name, {"term": name})
            entry.setdefault("sources", set()).add("mechanics_index")
            if isinstance(e, dict) and e.get("notes"):
                entry.setdefault("definition", str(e["notes"])[:400])
    return out


def _from_descriptor_registry() -> dict[str, dict]:
    p = REPO / "references" / "descriptor_registry.yaml"
    out: dict[str, dict] = {}
    if not p.exists():
        return out
    data = yaml.safe_load(p.read_text()) or {}

    def walk(node):
        """Descriptor entries are `{key: attr.body.strength, name: Strength, aliases: [...]}`.

        The first cut looked for `canonical`/`range` — fields this file does not use — and
        contributed ZERO terms while still being advertised as a source. Fixed and guarded by
        _assert_every_source_contributes().
        """
        if isinstance(node, dict):
            nm = node.get("name") or node.get("canonical")
            if isinstance(nm, str) and nm and ("key" in node or "aliases" in node):
                e = out.setdefault(nm, {"term": nm})
                e.setdefault("sources", set()).add("descriptor_registry")
                if node.get("key"):
                    e.setdefault("registry_id", node["key"])
                al = [a for a in (node.get("aliases") or []) if a]
                if al:
                    e.setdefault("aliases", al)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(data)
    return out


def _assert_every_source_contributes(per_source: dict[str, int]) -> None:
    """A declared source that yields nothing is a dead reader advertising coverage it lacks.

    Both original defects in this tool were of exactly that shape: descriptor_registry read the
    wrong field names and returned 0, and glossary.md's parser required >=4 columns and captured
    31 of ~130 rows. Neither announced itself. This makes the next one fail loudly instead.
    """
    dead = sorted(name for name, n in per_source.items() if n == 0)
    if dead:
        raise SystemExit(
            "[glossary ✗] declared source(s) contributed ZERO terms: " + ", ".join(dead)
            + "\n    Either the registry moved/emptied, or the reader is looking at the wrong "
              "fields. Fix the reader or drop the source — do not ship a source that reads nothing."
        )


def collect_terms() -> tuple[dict[str, dict], list[dict]]:
    sources = {
        "names_index": _from_names_index(),
        "glossary.md": _from_glossary_md(),
        "identifier_census": _from_identifier_census(),
        "mechanics_index": _from_mechanics_index(),
        "descriptor_registry": _from_descriptor_registry(),
    }
    _assert_every_source_contributes({k: len(v) for k, v in sources.items()})

    merged: dict[str, dict] = {}
    for src in sources.values():
        for term, e in src.items():
            tgt = merged.setdefault(term, {"term": term, "sources": set()})
            srcs = tgt["sources"] | e.pop("sources", set())
            for k, v in e.items():
                if k == "census":
                    tgt.setdefault("census", {}).update(v)
                elif v not in (None, [], {}) and not tgt.get(k):
                    tgt[k] = v
            tgt["sources"] = srcs

    refused = []
    keep: dict[str, dict] = {}
    for term, e in merged.items():
        if len(term) < MIN_TERM_LEN:
            refused.append({"term": term, "why": f"shorter than MIN_TERM_LEN={MIN_TERM_LEN}"})
        elif term.isdigit():
            refused.append({"term": term, "why": "digit-only"})
        elif len(term) == 2 and not term.isupper():
            refused.append({"term": term, "why": "2 chars and not uppercase — unsafe to match"})
        else:
            keep[term] = e
    return keep, refused


# ── location scan ─────────────────────────────────────────────────────────────────────────────

def scan_locations(terms: dict[str, dict]) -> dict[str, dict[str, int]]:
    """term -> {relpath: hit_count}. One pass per FILE, not per term."""
    patterns = {t: re.compile(r"\b" + re.escape(t) + r"\b") for t in terms}
    hits: dict[str, dict[str, int]] = defaultdict(dict)
    for root in SCAN_ROOTS:
        base = REPO / root
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if p.suffix not in SCAN_SUFFIXES or not p.is_file():
                continue
            rel = p.relative_to(REPO).as_posix()
            try:
                text = p.read_text(errors="ignore")
            except OSError:
                continue
            for term, rx in patterns.items():
                # Cheap C-level substring reject BEFORE the regex. Without it this is
                # 465 files x 1537 patterns of regex work (~160s); with it, the regex only runs
                # on the handful of terms actually present in each file (~10s). `in` cannot
                # produce a false NEGATIVE for a \b-anchored pattern of the same literal, so the
                # result is identical — pinned by test_substring_prefilter_matches_regex_only.
                if term not in text:
                    continue
                n = len(rx.findall(text))
                if n:
                    hits[term][rel] = n
    return hits


# ── render ────────────────────────────────────────────────────────────────────────────────────

_HDR = ("<!-- GENERATED by tools/observability/build_glossary.py — DO NOT HAND-EDIT.\n"
        "     Curated DEFINITIONS live in references/glossary.md; this view adds LOCATIONS.\n"
        "     Re-run the tool after any doc move. -->\n")


MAX_FILES_SHOWN = 3          # per term, in markdown. Full lists live in glossary.json.
MAX_DEF_CHARS = 300


def _short(text: str | None) -> str:
    if not text:
        return ""
    t = " ".join(str(text).split())
    return t if len(t) <= MAX_DEF_CHARS else t[:MAX_DEF_CHARS].rstrip() + " …"


def _term_row(term: str, e: dict, here: str, by_sub: dict[str, list[str]]) -> str:
    """ONE compact row per term.

    The first cut rendered a multi-line block per term and produced 5.2 MB across 20 files, one of
    them 414 KB. That is a concordance dump, not a glossary — nobody reads it, and it would swamp
    the repo's own size warnings. Markdown is the READING surface and stays skimmable; glossary.json
    is the COMPLETE surface and carries every location.
    """
    bits = [f"**{term}**"]
    if e.get("abbreviation"):
        bits.append(f"(`{e['abbreviation']}`)")
    head = " ".join(bits)

    defn = _short(e.get("definition")) or "_no curated definition_"

    local = by_sub.get(here, [])
    loc = ", ".join(f"`{Path(f).name}`" for f in local[:MAX_FILES_SHOWN])
    if len(local) > MAX_FILES_SHOWN:
        loc += f" +{len(local) - MAX_FILES_SHOWN}"

    others = sorted(s for s in by_sub if s != here)
    also = (", ".join(f"[{s}](GLOSSARY_{s}.md)" for s in others)) if others else "_local only_"

    extra = []
    cen = (e.get("census") or {}).get(here)
    if cen and cen.get("disposition"):
        extra.append(cen["disposition"])
    if e.get("aliases"):
        extra.append("alias: " + ", ".join(e["aliases"][:3]))
    if e.get("legacy"):
        # COUNT, never the spelling. names_index marks legacy names `enforce: block` and
        # tools/ci_naming_check.py fails on the deprecated token appearing anywhere outside its
        # registry home — reprinting `Galbados` here propagated exactly what that gate exists to
        # stop. The reader still learns a deprecated form exists and where to look it up.
        n = len(e["legacy"])
        extra.append(f"{n} legacy spelling{'s' if n > 1 else ''} — see names_index.yaml")
    if e.get("ambiguous"):
        extra.append(f"⚠️ broad ({e['file_count']} files)")
    tail = f" · {'; '.join(extra)}" if extra else ""

    return f"| {head} | {defn} | {loc} | {also}{tail} |"


def render(terms: dict[str, dict], hits: dict, refused: list[dict]) -> dict[str, str]:
    files: dict[str, str] = {}
    per_sub: dict[str, dict[str, dict[str, list[str]]]] = defaultdict(dict)
    for term, e in terms.items():
        by_sub: dict[str, list[str]] = defaultdict(list)
        for rel in hits.get(term, {}):
            by_sub[_subsystem_of(rel)].append(rel)
        e["file_count"] = len(hits.get(term, {}))
        e["subsystems"] = sorted(by_sub)
        e["ambiguous"] = e["file_count"] > AMBIGUITY_FLOOR
        for sub in by_sub:
            per_sub[sub][term] = dict(by_sub)

    # per-subsystem glossaries — repetitions intended
    for sub in sorted(per_sub):
        rows = sorted(per_sub[sub], key=str.lower)
        defined = sum(1 for t in rows if terms[t].get("definition"))
        L = [_HDR, f"# Glossary — `{sub}`", "",
             f"**{len(rows)} terms** appear in this subsystem; **{defined}** carry a curated "
             "definition. A term used by several subsystems is listed in each, with "
             "cross-references — the repetition is the point.", "",
             "Files column shows this subsystem's docs only (basenames). Full paths for every "
             "term are in [`glossary.json`](glossary.json). Master index: "
             "[MASTER_GLOSSARY.md](MASTER_GLOSSARY.md).", "",
             "| Term | Definition | In this subsystem | Also in |",
             "|---|---|---|---|"]
        for term in rows:
            L.append(_term_row(term, terms[term], sub, per_sub[sub][term]))
        L.append("")
        files[f"GLOSSARY_{sub}.md"] = "\n".join(L)

    # master
    located = {t: e for t, e in terms.items() if e["file_count"]}
    unlocated = sorted(t for t, e in terms.items() if not e["file_count"])
    M = [_HDR, "# Master Glossary — every term, every location", "",
         f"**{len(terms)} terms** from 5 registries. **{len(located)}** are located in the live "
         f"corpus (`{'`, `'.join(SCAN_ROOTS)}`); **{len(unlocated)}** are registered but appear in "
         "no scanned design doc.", "",
         "Per-subsystem views: " + ", ".join(f"[{s}](GLOSSARY_{s}.md)" for s in sorted(per_sub)),
         "",
         "**Every location** is listed below as the subsystems a term appears in, with its total "
         "file count. The exhaustive path list per term is in [`glossary.json`](glossary.json) "
         "under `terms.<term>.locations` — kept there rather than inline so this file stays "
         "readable.", "", "---", "", "## Terms", "",
         "| Term | Definition | Subsystems | Files | Sources |", "|---|---|---|---:|---|"]
    for term in sorted(located, key=str.lower):
        e = terms[term]
        subs = ", ".join(f"[{s}](GLOSSARY_{s}.md)" for s in e["subsystems"])
        flag = " ⚠️" if e["ambiguous"] else ""
        M.append(f"| **{term}**{flag} | {_short(e.get('definition')) or '_no curated definition_'} "
                 f"| {subs} | {e['file_count']} | {', '.join(sorted(e['sources']))} |")
    M.append("")
    if unlocated:
        M += ["---", "", "## Registered but not located", "",
              "Named in a registry, matched in no scanned design doc. Either the term moved, the "
              "registry entry is stale, or it is code-only vocabulary. Surfaced, not dropped.", ""]
        for t in unlocated:
            M.append(f"- `{t}` — sources: {', '.join(sorted(terms[t]['sources']))}")
        M.append("")
    if refused:
        M += ["---", "", "## Refused from matching", "",
              f"Too short (<{MIN_TERM_LEN}) or digit-only to word-boundary match without false "
              "positives. Listed so the exclusion is visible.", ""]
        for r in refused:
            M.append(f"- `{r['term']}` — {r['why']}")
        M.append("")
    files["MASTER_GLOSSARY.md"] = "\n".join(M)
    return files


def build() -> tuple[dict[str, str], dict]:
    terms, refused = collect_terms()
    hits = scan_locations(terms)
    files = render(terms, hits, refused)
    payload = {
        "generated_by": "tools/observability/build_glossary.py",
        "schema_version": 1,
        "scan_roots": list(SCAN_ROOTS),
        "ambiguity_floor": AMBIGUITY_FLOOR,
        "counts": {
            "terms": len(terms),
            "located": sum(1 for e in terms.values() if e["file_count"]),
            "ambiguous": sum(1 for e in terms.values() if e["ambiguous"]),
            "refused": len(refused),
        },
        "refused": refused,
        # `legacy` is replaced by a COUNT for the same reason as in the markdown: those spellings
        # are `enforce: block` in names_index and a blocking naming gate fails on them anywhere
        # else. names_index.yaml remains the single home for the actual strings.
        "terms": {t: {**{k: v for k, v in e.items() if k not in ("sources", "legacy")},
                      "legacy_count": len(e.get("legacy") or []),
                      "sources": sorted(e["sources"]),
                      "locations": hits.get(t, {})}
                  for t, e in sorted(terms.items())},
    }
    return files, payload


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="fail if the committed output differs from a fresh build")
    args = ap.parse_args()

    files, payload = build()
    js = json.dumps(payload, indent=1, sort_keys=True) + "\n"

    if args.check:
        stale = []
        for name, body in files.items():
            p = OUT_DIR / name
            if not p.exists() or p.read_text() != body:
                stale.append(name)
        p = OUT_DIR / "glossary.json"
        if not p.exists() or p.read_text() != js:
            stale.append("glossary.json")
        if stale:
            print("[glossary ✗] stale (re-run tools/observability/build_glossary.py):")
            for s in stale:
                print("   ", s)
            return 1
        print(f"[glossary ✓] {payload['counts']['terms']} terms, "
              f"{payload['counts']['located']} located — output current")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, body in files.items():
        (OUT_DIR / name).write_text(body)
    (OUT_DIR / "glossary.json").write_text(js)
    c = payload["counts"]
    print(f"[glossary] {c['terms']} terms | {c['located']} located | "
          f"{c['ambiguous']} flagged broad | {c['refused']} refused")
    print(f"   -> {OUT_DIR.relative_to(REPO)}/ ({len(files)} markdown + glossary.json)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
