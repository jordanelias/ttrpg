#!/usr/bin/env python3
"""
handoff_atomize.py — the single owner of the handoff skeleton/infill/archive structure.

Jordan's 2026-07-28 ruling (ED-IN-0085) set the handoff contract:

  • Each HANDOFF_<LANE>.md is a SKELETON: an executive summary (~60 words, bullet-point
    phrasing — prose costs too much) plus ONE LINE per open item. The summary exists so a
    session does not have to open the infill for basic orientation.
  • Detail lives in HANDOFF_<LANE>_infill.md (CLAUDE.md §4 co-filing).
  • Items whose most recent activity is older than 30 days are ARCHIVED.
  • Every infill and every archive document holds at most 10,000 tokens — parts are split
    (_infill_2.md, _archive_2.md, …) rather than allowed to grow.

Why a tool and not nine hand-edits: CLAUDE.md §8 — every rule lives once. The classification
(closed / stale / live), the caps, and the split points are all HERE, so the lanes cannot
drift from each other and `tests/valoria/test_handoff_structure.py` has one thing to pin.

WHAT IS AUTHORED, NOT GENERATED: the executive summary. A generated summary would be a
restatement of the first bullet, which is exactly the "search the infill for context" problem
the ruling is aimed at. The tool PRESERVES an existing `## Executive summary` block verbatim
across runs and emits a TODO placeholder (plus a warning) when one is missing.

Usage:
    python tools/handoff_atomize.py --lane IN            # rewrite one lane
    python tools/handoff_atomize.py --all                # rewrite every lane
    python tools/handoff_atomize.py --all --check        # report only, exit 1 on violation
    python tools/handoff_atomize.py --all --today 2026-07-28
"""
import argparse
import datetime
import pathlib
import re
import sys

HANDOFF_DIR = pathlib.Path(__file__).resolve().parent.parent / "registers" / "handoffs"
LANES = ("MB", "PC", "FI", "SC", "FA", "WR", "IN", "GO", "SE")

MAX_TOKENS = 10_000          # per infill / archive document (Jordan 2026-07-28)
STALE_DAYS = 30              # "older than a month"
SUMMARY_MAX_WORDS = 60

# ── STATUS TAG CONVENTION (ED-IN-0085, Jordan 2026-07-28) ────────────────────────────────
# Every handoff bullet opens with ONE tag from a CLOSED three-value vocabulary:
#
#     - [OPEN] item …                     work not finished
#     - [PART] item — residual: …         partly finished; the residue MUST be named inline
#     - [DONE 2026-07-26] item …          finished; date optional but preferred
#
# Why a tag and not prose. Status was being written as free text with an unbounded vocabulary
# (DONE / RATIFIED / RESOLVED / LANDED / EXECUTED / DELIVERED / PARTIALLY RATIFIED / FILED /
# STAGED / UNRULED …), so every consumer had to GUESS with a regex. That guessing is the direct
# cause of the defect this tool found: five lanes carry LIVE items whose prose matches
# build_decisions.RESOLVED_SKIP, so the SessionStart banner counts them as settled and they are
# invisible. A closed vocabulary at a fixed position makes the read exact instead of heuristic.
#
# Cost: ~3 tokens per bullet — about 130 tokens across the whole IN lane. That is the cheapest
# element in the file and it removes an entire defect class.
#
# PART is the one that earns its keep only if disciplined: "partly done" without naming what
# remains is just OPEN with extra words, so the residual is required on the same line.
# Leading emphasis is tolerated: `- **[OPEN] …**` is how a human naturally writes it, and a
# convention that only matches unbolded text would be quietly bypassed by ordinary formatting.
STATUS_TAG = re.compile(r'^[*_\s]*\[(OPEN|PART|DONE)(?:\s+(20\d\d-\d\d-\d\d))?\]\s*')

# Legacy prose inference. MIGRATION ONLY — used when a bullet carries no tag, and always
# reported so the untagged backlog is visible rather than silently guessed at forever.
# DELIVERED counts as closed because Jordan ruled it does (2026-07-28). AMBIG beats CLOSER:
# "PARTIALLY RATIFIED" and "(open, execution pending)" are not closures.
CLOSER = re.compile(r'(✅|\bDONE\b|\bRATIFIED\b|\bRESOLVED\b|\bLANDED\b|\bEXECUTED\b|\bDELIVERED\b)')
AMBIG = re.compile(r'PARTIALLY|UNRULED|STAGED|execution pending|\(open')
RESIDUAL = re.compile(r'STAGED|UNRULED|pending|TODO|residual|follow-up|not yet|blocked', re.I)
DATE = re.compile(r'20\d\d-\d\d-\d\d')

SUMMARY_HEAD = "## Executive summary"
SUMMARY_TODO = ("<!-- TODO(ED-IN-0085): author a ~60-word executive summary. Bullet-point "
                "phrasing, not prose. It must answer 'what is this lane's state right now' "
                "without opening the infill. -->")


def tokens(text: str) -> int:
    """Repo convention: characters // 4 (matches ci_register_size_check and compliance_check).
    NB characters, not bytes — a byte count overstates unicode-heavy files."""
    return len(text) // 4


def split_bullets(section: str) -> list[str]:
    """Top-level '- ' bullets. Nested sub-bullets stay with the item above them."""
    return [b.rstrip() for b in re.split(r'\n(?=- )', section) if b.strip().startswith('- ')]


def last_activity(bullet: str):
    """Most recent date mentioned anywhere in the item — the best available proxy for when
    it was last touched. MIN would misdate an old item that has recent follow-on notes."""
    found = []
    for d in DATE.findall(bullet):
        try:
            found.append(datetime.date.fromisoformat(d))
        except ValueError:
            pass
    return max(found) if found else None


def status_tag(bullet: str):
    """-> ('OPEN'|'PART'|'DONE', date|None) if the bullet is tagged, else None."""
    m = STATUS_TAG.match(bullet.split('\n')[0][2:].strip())
    if not m:
        return None
    when = None
    if m.group(2):
        try:
            when = datetime.date.fromisoformat(m.group(2))
        except ValueError:
            pass
    return (m.group(1), when)


def classify(bullet: str, cutoff: datetime.date) -> tuple[str, bool]:
    """-> (('closed'|'stale'|'live'), tagged). The tag is AUTHORITATIVE when present; prose is
    only consulted for untagged legacy bullets, and the caller reports how many those are."""
    tag = status_tag(bullet)
    if tag is not None:
        kind, _ = tag
        if kind == 'DONE':
            return 'closed', True
        seen = last_activity(bullet)
        return ('stale' if seen is not None and seen < cutoff else 'live'), True
    first = bullet.split('\n')[0][2:].strip()
    if CLOSER.search(first) and not AMBIG.search(first):
        return 'closed', False
    seen = last_activity(bullet)
    return ('stale' if seen is not None and seen < cutoff else 'live'), False


def tag_problems(lane: str, bullets: list[str]) -> list[str]:
    """Consistency checks on the tag itself. A tag that can lie without anything noticing is
    no better than the prose it replaced, so: DONE must not sit on top of unfinished residue,
    and PART must name what remains (otherwise it is OPEN wearing a different hat)."""
    out, untagged = [], 0
    for b in bullets:
        tag = status_tag(b)
        if tag is None:
            untagged += 1
            continue
        kind, _ = tag
        first = b.split('\n')[0]
        if kind == 'DONE' and RESIDUAL.search(b):
            out.append(f"{lane}: [DONE] item still describes residual work: {one_line(b, 60)}…")
        if kind == 'PART' and 'residual' not in first.lower():
            out.append(f"{lane}: [PART] item does not name its residual inline: {one_line(b, 60)}…")
    if untagged:
        out.append(f"{lane}: {untagged}/{len(bullets)} bullets carry no [OPEN|PART|DONE] tag "
                   f"— status inferred from prose (migration debt, ED-IN-0085)")
    return out


def one_line(bullet: str, width: int = 112) -> str:
    """A single skeleton line. Bold markers are stripped rather than balanced — truncating
    inside a `**` pair renders as literal asterisks for the rest of the file."""
    t = re.sub(r'\s+', ' ', bullet.split('\n')[0][2:].strip()).replace('**', '')
    if len(t) <= width:
        return t.rstrip(' .,;:—-')
    return t[:width].rsplit(' ', 1)[0].rstrip(' .,;:—-') + '…'


def parse(path: pathlib.Path) -> dict:
    text = path.read_text(encoding='utf-8')
    parts = re.split(r'\n(?=## )', text)
    preamble, sections, summary = parts[0], {}, None
    for p in parts[1:]:
        head = p.split('\n')[0].strip()
        if head == SUMMARY_HEAD:
            summary = '\n'.join(p.split('\n')[1:]).strip()
            continue
        sections[head] = p
    return {'preamble': preamble, 'summary': summary, 'sections': sections}


def _pack(blocks: list[str], header: str, stem: str) -> list[tuple[str, str]]:
    """Fill documents to at most MAX_TOKENS, overflowing into _2, _3… A single block larger
    than the cap gets its own document rather than being truncated: losing content to satisfy
    a size rule is strictly worse than one oversized part (the caller reports it)."""
    docs, cur = [], []
    for b in blocks:
        if cur and tokens(header + "\n\n" + "\n\n".join(cur + [b])) > MAX_TOKENS:
            docs.append(cur)
            cur = [b]
        else:
            cur.append(b)
    if cur:
        docs.append(cur)
    out = []
    for i, blocks_i in enumerate(docs, 1):
        name = f"{stem}.md" if i == 1 else f"{stem}_{i}.md"
        part = "" if len(docs) == 1 else f"\n\n_Part {i} of {len(docs)}._"
        out.append((name, header + part + "\n\n" + "\n\n".join(blocks_i) + "\n"))
    return out


def paginate_archive(items: list[tuple], header: str, stem: str,
                     lane: str) -> list[tuple[str, str]]:
    """Archives are named by DATE RANGE and accompanied by an index (Jordan, 2026-07-28).

    Items are ordered oldest-first and packed to the cap, so each document covers a
    contiguous window named `<first>_<last>`. The NEWEST document is the one still being
    appended to, so it has no closing date and is named `<first>_open` — reopening it is
    unambiguous, and a closed range never changes again.

    Deliberately not fill-order-with-numbers: "part 2 of 3" satisfies the size cap while
    making a lookup open every part. The range in the name makes the search directed, and
    `HANDOFF_<LANE>_archive_index.md` maps every item to its file so a lookup needs no
    guessing at all — a one-line-per-item index costs far less than the miss it prevents.

    `items` is (bullet, date-or-None). Undated items ride in the open document: they cannot
    be placed in a closed range honestly, and inventing a date for them would be worse.
    """
    dated = sorted([i for i in items if i[1]], key=lambda x: x[1])
    ordered = dated + [i for i in items if not i[1]]

    docs, cur = [], []
    for it in ordered:
        if cur and tokens(header + "\n\n" + "\n\n".join(b for b, _ in cur + [it])) > MAX_TOKENS:
            docs.append(cur)
            cur = [it]
        else:
            cur.append(it)
    if cur:
        docs.append(cur)

    out, index_rows = [], []
    for idx, doc in enumerate(docs):
        ds = [d for _, d in doc if d]
        start = min(ds).isoformat() if ds else 'undated'
        is_open = (idx == len(docs) - 1)
        name = f"{stem}_{start}_open.md" if is_open else f"{stem}_{start}_{max(ds).isoformat()}.md"
        window = (f"{start} → open (still accepting new items)" if is_open
                  else f"{start} → {max(ds).isoformat()} (closed)")
        out.append((name, f"{header}\n\n_Window: {window}._\n\n"
                          + "\n\n".join(b for b, _ in doc) + "\n"))
        for bullet, when in doc:
            index_rows.append((when.isoformat() if when else '—', one_line(bullet, 88), name))

    idx_md = [f"# Handoff — {lane} · Archive index", "",
              f"Which archive holds which item. Generated by `tools/handoff_atomize.py`; the",
              f"`_open` file is the only one still accepting items. Skeleton:",
              f"[`HANDOFF_{lane}.md`](HANDOFF_{lane}.md).", "",
              "| Last activity | Item | Archive |", "|---|---|---|"]
    for when, text, name in sorted(index_rows, key=lambda r: (r[0] == '—', r[0])):
        safe = text.replace('|', r'\|')      # a raw pipe would break the table row
        idx_md.append(f"| {when} | {safe} | [{name}]({name}) |")
    out.append((f"{stem}_index.md", "\n".join(idx_md) + "\n"))
    return out


def paginate_infill(groups: dict[str, list[str]], header: str, stem: str) -> list[tuple[str, str]]:
    """Infills split by SECTION, not overflow order — a session that needs detail should know
    which file to open from the skeleton line alone. Overflow within a section still numbers."""
    out = []
    for section, blocks in groups.items():
        if not blocks:
            continue
        suffix = re.sub(r'[^a-z0-9]+', '-', section.lower()).strip('-') or 'detail'
        out += _pack(blocks, f"{header}\n\n_Section: {section}._", f"{stem}_{suffix}")
    return out


def build(lane: str, cutoff: datetime.date, write: bool) -> list[str]:
    problems = []
    src = HANDOFF_DIR / f"HANDOFF_{lane}.md"
    if not src.exists():
        return problems
    doc = parse(src)
    pend_head = next((h for h in doc['sections'] if h.lower().startswith('## pending')), None)
    pend = split_bullets(doc['sections'][pend_head]) if pend_head else []
    other = {h: split_bullets(s) for h, s in doc['sections'].items() if h != pend_head}

    live, closed, stale = [], [], []
    for b in pend:
        kind, _tagged = classify(b, cutoff)
        {'live': live, 'closed': closed, 'stale': stale}[kind].append(b)
    problems += tag_problems(lane, pend)
    # Non-Pending sections (Decisions / Next actions) are a record, not in-flight work:
    # age them out on the same 30-day rule, keep the rest as detail.
    other_live, other_old = {}, []
    for head, bl in other.items():
        keep = []
        for b in bl:
            (other_old if classify(b, cutoff)[0] in ('closed', 'stale') else keep).append(b)
        other_live[head] = keep

    summary = doc['summary'] or SUMMARY_TODO
    if doc['summary'] is None:
        problems.append(f"{lane}: no executive summary — placeholder written")
    else:
        words = len(re.sub(r'<!--.*?-->', '', summary, flags=re.S).split())
        if words > SUMMARY_MAX_WORDS:
            problems.append(f"{lane}: executive summary is {words} words (max {SUMMARY_MAX_WORDS})")

    # ── skeleton ─────────────────────────────────────────────────────────────
    sk = [f"# Handoff — {lane}", "",
          f"Lane-scoped continuity for `{lane}`, per the `ED-<LANE>-NNNN` namespace. Root `HANDOFF.md`",
          "is the cross-lane index.", "",
          "**This file is the SKELETON** (CLAUDE.md §4 co-filing): an executive summary plus one line",
          f"per open item. Detail → [`HANDOFF_{lane}_infill.md`](HANDOFF_{lane}_infill.md).",
          f"Closed and >30-day-old items → [`HANDOFF_{lane}_archive.md`](HANDOFF_{lane}_archive.md).",
          "Generated by `tools/handoff_atomize.py` — do not append narrative here.", "",
          SUMMARY_HEAD, "", summary, "", "## Pending", ""]
    if live:
        for b in live:
            sk.append(f"- {one_line(b)}")
    else:
        sk.append("_No open items._")
    for head, bl in other_live.items():
        sk += ["", head, ""]
        sk += [f"- {one_line(b)}" for b in bl] or ["_None._"]
    skeleton = "\n".join(sk) + "\n"

    # A live item whose skeleton line matches build_decisions.RESOLVED_SKIP is invisible to
    # the SessionStart banner — it would be counted as settled. Report, never auto-reword.
    try:
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "observability"))
        import build_decisions
        for b in live:
            if status_tag(b) is not None:
                continue   # tagged: session_open_work reads the tag, prose can't mislead it
            line = one_line(b)
            if build_decisions.RESOLVED_SKIP.search(line):
                problems.append(f"{lane}: skeleton line would be banner-filtered as settled: {line[:70]}…")
    except Exception:
        pass

    infill_groups = {'pending': [f"### {one_line(b, 80)}\n\n{b}" for b in live]}
    for head, bl in other_live.items():
        infill_groups[head.lstrip('# ').strip()] = [f"### {one_line(b, 60)}\n\n{b}" for b in bl]
    archive_items = [(b, last_activity(b)) for b in (closed + stale + other_old)]

    inf_header = (f"# Handoff — {lane} · Infill (detail)\n\n"
                  f"Prose companion to the [`HANDOFF_{lane}.md`](HANDOFF_{lane}.md) skeleton. Open this only "
                  f"when a skeleton line is not enough.")
    arc_header = (f"# Handoff — {lane} · Archive\n\n"
                  f"Closed items, and items untouched for more than {STALE_DAYS} days, pruned from "
                  f"[`HANDOFF_{lane}.md`](HANDOFF_{lane}.md). Moved verbatim, never deleted. Anything still "
                  f"genuinely open is tracked in `registers/editorial_ledger_{lane.lower()}.jsonl`, which is the "
                  f"permanent tracker — this file is provenance. **Do not resume work from here.**")

    outputs = [(f"HANDOFF_{lane}.md", skeleton)]
    outputs += paginate_infill(infill_groups, inf_header, f"HANDOFF_{lane}_infill")
    if archive_items:
        outputs += paginate_archive(archive_items, arc_header, f"HANDOFF_{lane}_archive", lane)

    for name, content in outputs:
        n = tokens(content)
        if name != f"HANDOFF_{lane}.md" and n > MAX_TOKENS:
            problems.append(f"{name}: {n} tokens exceeds the {MAX_TOKENS} cap (single oversized item)")
        if write:
            (HANDOFF_DIR / name).write_text(content, encoding='utf-8')
    if write:
        print(f"  {lane}: skeleton {tokens(skeleton)} tok · "
              f"{len(live)} live / {len(closed)} closed / {len(stale)} stale · "
              + " · ".join(f"{n}={tokens(c)}" for n, c in outputs[1:]))
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--check', action='store_true', help='report only; exit 1 on violation')
    ap.add_argument('--today', default=None, help='YYYY-MM-DD (default: system date)')
    a = ap.parse_args()
    today = datetime.date.fromisoformat(a.today) if a.today else datetime.date.today()
    cutoff = today - datetime.timedelta(days=STALE_DAYS)
    lanes = LANES if a.all else ([a.lane] if a.lane else [])
    if not lanes:
        ap.error("pass --lane <LANE> or --all")
    print(f"handoff_atomize: cutoff {cutoff} (>{STALE_DAYS}d), cap {MAX_TOKENS} tok/doc")
    problems = []
    for lane in lanes:
        problems += build(lane, cutoff, write=not a.check)
    if problems:
        print("\n[HANDOFF STRUCTURE: %d issue(s)]" % len(problems))
        for p in problems:
            print(f"  ! {p}")
        return 1 if a.check else 0
    print("\nHandoff structure OK.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
