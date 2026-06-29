#!/usr/bin/env python3
"""
tools/observability/build_archive_xref.py — archive→open-item relevance cross-referencer.

Combs the archived / deprecated / superseded material and asks, for each item currently
flagged OPEN: "has this already been answered somewhere we stopped reading?"

Two matchers:
  A. ID match (high confidence): an open item references ED-NNN / PP-NNN. If that ID is
     RESOLVED in the active or an archived ledger, the decision already exists — surface it.
  B. Topical match (lead): an open item shares distinctive terms with a resolved ledger
     entry or an archived handoff, even without an ID reference.

Sources:
  active:   canon/editorial_ledger.jsonl, canon/patch_register_active.yaml
  archived: deprecated/canon/editorial_ledger_archive_*.yaml,
            archives/patches/*.yaml, archives/handoffs/*.yaml, archives/session/*,
            params/*_superseded.md and other *superseded*/*archive* docs
  open:     tools/observability/decisions.json   (run build_decisions.py first)

Output: ARCHIVE_RELEVANCE.md, archive_xref.json
Run:    python tools/observability/build_decisions.py && python tools/observability/build_archive_xref.py
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
ID_RE = re.compile(r"\b((?:ED|PP|J)-\d+)\b")
RESOLVED_WORDS = {"closed", "resolved", "applied", "ratified", "landed"}
PENDING_WORDS = ("pending", "[open", "awaiting", "tbd", "unresolved", "not yet", "open —", "open-")
STOP = set("the a an of to in on for and or is are be with by as at from this that it its their "
           "open jordan pending ruling per via not no into onto over under new old via must may "
           "system systems key keys value values per-".split())


def rel(p): return str(p.relative_to(REPO)).replace("\\", "/")


def load_jsonl(p):
    out = []
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                try: out.append(json.loads(line))
                except json.JSONDecodeError: pass
    return out


def tokens(s):
    return {w for w in re.findall(r"[a-z_]{4,}", (s or "").lower()) if w not in STOP}


def main():
    # ---------- build the RESOLVED index (the "answers") ----------
    resolved = {}   # id -> {kind, status, text, source, resolved}

    def put(id_, kind, status, text, source):
        st = (status or "").lower()
        txt_l = (text or "").lower()
        pending = any(w in txt_l for w in PENDING_WORDS)
        # RESOLVED only if the status field says so AND the decision text isn't itself "pending"
        is_res = any(w in st for w in RESOLVED_WORDS) and not pending
        prev = resolved.get(id_)
        if prev and prev["resolved"] and not is_res:
            return
        resolved[id_] = {"kind": kind, "status": status or "", "text": (text or "").strip()[:400],
                         "source": source, "resolved": is_res}

    # active ED ledger (jsonl)
    for e in load_jsonl(REPO / "canon" / "editorial_ledger.jsonl"):
        if e.get("id"):
            put(e["id"], "ED", e.get("status", ""),
                e.get("decision") or e.get("description", ""), "canon/editorial_ledger.jsonl")
    # archived ED ledgers
    for p in (REPO / "deprecated" / "canon").glob("editorial_ledger_archive*.yaml"):
        try:
            raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            continue
        for e in (raw.get("entries") or []):
            if isinstance(e, dict) and e.get("id"):
                put(e["id"], "ED", e.get("status", ""),
                    e.get("jordan_decision") or e.get("decision") or e.get("description", ""), rel(p))
    # patch registers (active + archive)
    patch_files = [REPO / "canon" / "patch_register_active.yaml"] + \
                  list((REPO / "archives" / "patches").glob("*.yaml"))
    for p in patch_files:
        if not p.exists():
            continue
        try:
            raw = yaml.safe_load(p.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            continue
        entries = raw if isinstance(raw, list) else (raw.get("patches") or raw.get("entries") or []) if isinstance(raw, dict) else []
        for e in entries:
            if isinstance(e, dict) and e.get("id"):
                put(e["id"], "PP", e.get("status", ""), e.get("description", ""), rel(p))

    # ---------- archived narrative material (handoffs / sessions / superseded) ----------
    archive_docs = []   # {file, title, text, ids}
    arch_globs = [
        (REPO / "archives" / "handoffs", "*"),
        (REPO / "archives" / "session", "*"),
        (REPO / "archives" / "editorial", "*"),
        (REPO / "archives" / "editorials", "*"),
        (REPO / "archives" / "propagation", "*"),
    ]
    superseded_extra = list(REPO.glob("params/*superseded*.md")) + \
        [REPO / "session_log_archive.md"] + \
        list((REPO / "references").glob("propagation_map_archive*.md"))
    files = []
    for base, pat in arch_globs:
        if base.exists():
            files += [f for f in base.rglob(pat) if f.is_file()]
    files += [f for f in superseded_extra if f.exists()]
    for p in files:
        if p.suffix.lower() not in (".md", ".yaml", ".yml", ".txt", ".json"):
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        archive_docs.append({"file": rel(p), "text": txt,
                             "ids": set(ID_RE.findall(txt)), "tok": tokens(txt[:6000])})

    # ---------- load OPEN items ----------
    dj = OUT / "decisions.json"
    if not dj.exists():
        print("decisions.json missing — run build_decisions.py first", file=sys.stderr)
        sys.exit(1)
    D = json.loads(dj.read_text(encoding="utf-8"))
    opens = D["decisions"]

    # ---------- match ----------
    id_hits, topical_hits, unresolved_refs, docket = [], [], [], []
    for o in opens:
        refs = set(ID_RE.findall(o["text"]))
        matched_any = False
        for rid in sorted(refs):
            if rid.startswith("J-"):
                docket.append({"id": rid, "open": o["text"][:200], "loc": o["locations"][:2]})
                continue
            r = resolved.get(rid)
            if r and r["resolved"]:
                id_hits.append({"ref": rid, "open": o["text"][:240], "open_loc": o["locations"][:2],
                                "priority": o["priority"], "resolution": r["text"],
                                "resolution_source": r["source"], "kind": r["kind"]})
                matched_any = True
            elif r is None:
                unresolved_refs.append({"ref": rid, "open": o["text"][:160], "loc": o["locations"][:1]})
        # topical (only for P1/P2 items with no id resolution, to stay high-signal)
        if not matched_any and o["priority"] <= 2:
            otok = tokens(o["text"])
            if len(otok) >= 3:
                best = []
                for d in archive_docs:
                    ov = otok & d["tok"]
                    if len(ov) >= 4:
                        best.append((len(ov), d["file"], sorted(ov)[:8]))
                best.sort(reverse=True)
                if best:
                    topical_hits.append({"open": o["text"][:200], "priority": o["priority"],
                                         "open_loc": o["locations"][:1],
                                         "candidates": [{"file": f, "shared": sh} for _, f, sh in best[:3]]})

    # dedupe id_hits by (ref, resolution_source)
    seen = set(); uid = []
    for h in id_hits:
        k = (h["ref"], h["resolution_source"], h["open"][:60])
        if k not in seen:
            seen.add(k); uid.append(h)
    id_hits = sorted(uid, key=lambda h: (h["priority"], h["ref"]))

    payload = {
        "meta": {
            "resolved_index_size": len(resolved),
            "archive_docs": len(archive_docs),
            "open_items": len(opens),
            "id_hits": len(id_hits),
            "topical_hits": len(topical_hits),
            "unresolved_refs": len({u["ref"] for u in unresolved_refs}),
            "docket_items": sorted({d["id"] for d in docket}),
        },
        "id_hits": id_hits, "topical_hits": topical_hits[:60],
        "unresolved_refs": unresolved_refs[:80], "docket": docket,
    }
    (OUT / "archive_xref.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    # ---------- report ----------
    md = ["# Valoria — Archive Relevance Report\n",
          "> Auto-generated by `tools/observability/build_archive_xref.py`. "
          "Combs archived / deprecated / superseded material for content that **already answers** "
          "items currently flagged OPEN.\n",
          f"**Resolved-decision index:** {len(resolved)} IDs (active + archived ledgers & patch registers). "
          f"**Archived narrative docs scanned:** {len(archive_docs)}. **Open items checked:** {len(opens)}.\n",
          f"\n- **{len(id_hits)} open items reference a decision that is ALREADY resolved** (see §1) — "
          "these may be closable now.\n"
          f"- **{len(topical_hits)} open items have topical matches** in the archive (leads, §2).\n"
          f"- **{payload['meta']['unresolved_refs']} referenced IDs are genuinely unknown** (in no ledger, §3).\n"
          f"- **Live Jordan docket:** {', '.join(payload['meta']['docket_items']) or '—'} (§4).\n"]

    md.append("\n---\n\n## §1 Open items already answered elsewhere (ID match — high confidence)\n")
    if not id_hits:
        md.append("_None found._")
    cur = None
    for h in id_hits:
        if h["priority"] != cur:
            cur = h["priority"]; md.append(f"\n### P{cur}\n")
        md.append(f"- **{h['ref']}** is **{ 'resolved' }** in `{h['resolution_source']}` — "
                  f"decision: _{h['resolution'] or '(see source)'}_  \n"
                  f"  but is still cited as open here: “{h['open']}”  \n"
                  f"  ↳ `{(h['open_loc'][0] if h['open_loc'] else '')}`")

    md.append("\n---\n\n## §2 Topical leads (archive may contain the answer)\n")
    if not topical_hits:
        md.append("_None._")
    for t in topical_hits[:40]:
        cand = "; ".join(f"`{c['file']}` (shares: {', '.join(c['shared'][:5])})" for c in t["candidates"])
        md.append(f"- **P{t['priority']}** “{t['open']}”  \n  ↳ candidates: {cand}")

    md.append("\n---\n\n## §3 Referenced IDs in no ledger (genuinely unaccounted)\n")
    seenu = set()
    for u in unresolved_refs:
        if u["ref"] in seenu: continue
        seenu.add(u["ref"])
        md.append(f"- **{u['ref']}** — “{u['open']}” ↳ `{u['loc'][0] if u['loc'] else ''}`")

    md.append("\n---\n\n## §4 Live Jordan docket (these are genuinely open by design)\n")
    seend = set()
    for d in docket:
        if d["id"] in seend: continue
        seend.add(d["id"])
        md.append(f"- **{d['id']}** — “{d['open']}”")

    (OUT / "ARCHIVE_RELEVANCE.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    m = payload["meta"]
    print("Archive relevance cross-reference built:")
    print(f"  resolved-index={m['resolved_index_size']} ids  archive-docs={m['archive_docs']}  open-items={m['open_items']}")
    print(f"  ID hits (already answered)={m['id_hits']}  topical leads={m['topical_hits']}"
          f"  unknown refs={m['unresolved_refs']}  docket={len(m['docket_items'])}")
    print(f"  -> {OUT/'ARCHIVE_RELEVANCE.md'}  /  archive_xref.json")
    return payload


if __name__ == "__main__":
    main()
