#!/usr/bin/env python3
"""
validate_ed_citations.py — citation-integrity guard for the editorial register.

WHY THIS EXISTS
---------------
The 2026-05-31 P1 resolver incident (ED-883): engine/params/factions/stats_1_7_scale.md
asserted the Domain Action resolver "CANONICAL (ED-865/874, ratified 2026-05-29)"
and extended it (treaty positioning, unique actions, bare-stat supersession) on the
same authority — but ED-874 and ED-885 were never written to the ledger, and ED-865
was OPEN and its text *strikes* the resolver's justification rather than ratifying it.
Nothing caught this: existing hooks check ID uniqueness and JSONL validity WITHIN the
ledger, but nothing verified that ED references in canon/design docs RESOLVE to real,
non-open entries. This tool closes that gap.

WHAT IT FLAGS (both are errors; exit 1 in CI)
---------------------------------------------
  NONEXISTENT   — a cited ED-NNN is absent from the ledger universe (active + archives).
  OPEN_AS_BASIS — a cited ED-NNN is OPEN (not resolved/struck) AND the surrounding text
                  claims it as a basis: canonical / ratified / applied / extension /
                  superseded / per ED / closes / approved.

A bare reference to an open item *without* a ratification claim is allowed (you may
discuss open work) and reported only at INFO level (--info).

SCOPE (v1): ED citations only. PP/patch-register support is a follow-on (needs the
active + archived patch registers loaded the same way). See checked_prefixes.

LANE-TAGGED IDS (2026-07-02, ED-IN-0001): new EDs use ED-<LANE>-NNNN (e.g. ED-MB-0001)
alongside the flat ED-NNNN format, which is FROZEN (no new allocations) but stays
permanently valid for existing citations. See references/id_reservations.yaml for the
lane roster and allocation protocol, CLAUDE.md section 3 for the format contract. Both
formats resolve through the same universe/audit path below.

USAGE (reads the local working tree — no PAT, no network):
    python3 tools/validate_ed_citations.py                     # full scan, exit 1 on violations
    python3 tools/validate_ed_citations.py --path PATH ...     # scan only these repo paths
    python3 tools/validate_ed_citations.py --info              # also print INFO open-refs

The pure core (audit_citations / build_status_map / _is_resolved) is import-testable
with no network — see tests/valoria/test_ed_citation_integrity.py (moved there from
tests/hooks/ on 2026-08-01, ED-IN-0119: it was live and passing and nothing ran it).
"""
import os, re, sys, json, argparse

# (Removed 2026-08-12, ED-IN-0165: a dead `REPO = 'jordanelias/ttrpg'` GitHub slug —
# a THIRD meaning of the name `REPO` in a tier where it now means the repo root, with
# no reader. G7 edited this file and did not notice; an adversarial pass did.)

# Lane roster for the ED-<LANE>-NNNN namespace (references/id_reservations.yaml is the
# source of truth for allocation; kept here too since the regex needs the closed set).
# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

# ONE OWNER: ci_common.LANE_CODES (plan G7, ED-IN-0159 §8.3). Was a verbatim
# copy of the 9-code tuple; obs_core's header records that one such copy once
# silently omitted GO, undercounting a whole lane.
LANE_CODES = ci_common.LANE_CODES
_LANE_ALT = '|'.join(LANE_CODES)

# Captures compact groups (ED-865/874) and inclusive ranges (ED-844-856 / ED-844–856),
# with an optional lane tag (ED-MB-0001) restricted to the closed LANE_CODES set so a
# stray two-uppercase-letter token elsewhere never false-positives as a lane. The
# numeric grammar (group 3) is IDENTICAL whether or not a lane tag is present, so
# _expand_nums / range handling below is untouched by the lane-tag addition.
CITE_RE = re.compile(
    rf'\b(ED|PP)-(?:({_LANE_ALT})-)?(\d{{1,4}}(?:/\d{{1,4}})*(?:[-–]\d{{1,4}})?)\b')

# Words that turn a citation into a *claim of authority* on the citing doc.
BASIS_KEYWORDS = (
    'canonical', 'ratif', 'applied', 'apply', 'closes', 'closed by',
    'resolved by', 'approved', 'extension', 'superseded', 'per ed', 'per pp',
)
# Planning / negation context: the citation is being discussed or proposed, not
# asserted as a firm canonical basis. Demotes an OPEN_AS_BASIS hit to OPEN_INFO.
NONBASIS_MARKERS = (
    'execution pending', 'pending', 'proposed', 'awaiting', 'new ed',
    'not re-filed', 'do not apply', "don't apply", 'contradiction',
    'flagged', 'flag for', 'spun out',
)
CONTEXT = 90  # chars of context captured each side of a citation

# Lane-split active ledger (2026-07-08 atomization pass): entries whose id already
# declares a lane (ED-<LANE>-NNNN) live in their own registers/editorial_ledger_<lane>.jsonl
# file instead of the flat registers/editorial_ledger.jsonl, mirroring the registers/handoffs/
# HANDOFF_<LANE>.md split. Pre-cutover flat-ID entries are NOT retrofitted (same
# no-retrofit precedent as the ED-<LANE>-NNNN cutover itself) and stay in the main file.
LANE_LEDGER_PATHS = tuple(
    f'registers/editorial_ledger_{lane.lower()}.jsonl' for lane in LANE_CODES
)

# Source-of-truth registers are never scanned as "citing docs".
REGISTER_PATHS = {'registers/editorial_ledger.jsonl', 'registers/patch_register_active.yaml',
                  *LANE_LEDGER_PATHS}
# Frozen history: citations there are records, not live claims.
SKIP_PREFIXES = ('deprecated/archives/', 'deprecated/', 'references/atoms_pending/')
# Working documents (audits, workplans) PROPOSE and TRACK EDs — they do not
# assert canon, so they are out of the validator's mandate (which is canonical
# surfaces only). Excluded from scanning entirely. See _is_working_doc.
WORKING_PREFIXES = ('designs/audit/', 'workplans/')
# Provenance registers RECORD where an ED applies; a citation there is a record,
# never a canonical-basis claim. Demoted to OPEN_INFO. See _is_provenance.
PROVENANCE_PATHS = {
    'references/roadmap_state.yaml',
    'references/synonym_registry.yaml',
    'registers/supersession_register.yaml',
    # The vocab fold (ED-IN-0078): the source + its generated register views record ED provenance
    # (authority/patch/source fields) — RECORDS of where an ED applied, not canonical-basis claims,
    # same rationale as synonym_registry above (already provenance; it is one of the folded views).
    'references/definitions/vocab_source.yaml',
    'references/censured_vocabulary.yaml',
    'references/deprecated_terms_registry.yaml',
    'references/alias_registry.yaml',
}
PROVENANCE_PREFIXES = ('references/splits/',)
# Live docs that can make canonical claims.
SCAN_PREFIXES = ('canon/', 'designs/', 'systems/', 'references/')  # engine/params/ evacuated 2026-08-05
SCAN_SUFFIXES = ('.md', '.yaml', '.yml')

# ── Burn-down tier (2026-08-01, ED-IN-0117) ───────────────────────────────────────────────────
# Repairing _walk_repo_files() took this gate from 45 files to 293 and surfaced 10 pre-existing
# OPEN_AS_BASIS findings in trees that were in the declared mandate but unreachable. Those 10 are
# NOT this fix's debt to pay, and turning a blocking gate red on them would punish the repair.
#
# They are reported LOUDLY and separately, and they are RATCHETED: the count may fall, never rise.
# A new open-ED-as-basis in these trees fails the build like any other. This is deliberately not a
# suppression list — a list you can add to is how "report-only until burned down" becomes forever.
#
# Inspected, not waved through: the 10 are concentrated in 3 files and are mostly CHANGELOG
# parentheticals ("+#11/#12 combat pair added 2026-07-29 per ED-IN-0004") and one DRAFT-FOR-RULING
# status line citing its own open ED by design — i.e. the OPEN_AS_BASIS heuristic over-fires on
# provenance prose. Narrowing that heuristic would be a semantics change to a blocking gate, made
# to lower a number I produced, so it is filed for a ruling rather than taken here (§0.1 point 4:
# asymmetric skepticism is a bias, not a defence).
#
# KEYED BY IDENTITY, NOT BY COUNT — a count alone was launderable. Adversarial review found it:
# with a ceiling of 10 and 10 findings, one changeset could FIX an existing finding and ADD a
# brand-new open-ED-as-basis claim, keep the count at 10, and pass both the gate and its own test.
# `git mv`ing a doc from canon/ (blocking) into systems/ laundered the same way. Nothing pinned
# WHICH findings were deferred. Now nothing but these five exact (path, id) pairs is ever
# deferred; anything else is a build failure wherever it appears.
BURN_DOWN_PREFIXES = ('systems/',)  # engine/params/ evacuated 2026-08-05
BURN_DOWN_ALLOW = frozenset({
    ('systems/_architecture/decision_policy_v1.md', 'ED-IN-0113'),
    ('systems/_architecture/key_type_registry_v30.md', 'ED-IN-0014'),
    ('systems/_architecture/key_type_registry_v30.md', 'ED-IN-0091'),
    ('systems/articulation/articulation_layer_v30.md', 'ED-IN-0004'),
    ('systems/articulation/articulation_layer_v30.md', 'ED-IN-0091'),
})
BURN_DOWN_MAX = 10  # occurrences across those 5 pairs; measured 2026-08-01, a test pins it both ways

# Editorial-archive locations (the ED universe is the active JSONL + these).
ARCHIVE_GLOBS = ('deprecated/archives/editorial/', 'deprecated/archives/editorials/', 'deprecated/canon/')

# JSONL archive siblings of the active ledger (registers/editorial_ledger.jsonl's own overflow
# chunks, per the register-size cap in tools/ci_register_size_check.py — mirrors the
# patch_register_active.yaml / patch_register_archive.yaml co-location convention, not the
# older ARCHIVE_GLOBS directories which predate the 2026-05-28 JSONL migration).
# [ED-MB-0051, 2026-07-29] Per-LANE archive siblings are derived from LANE_CODES rather than
# listed, so a lane that overflows its 50k cap keeps its archived ids inside the ED universe
# automatically. This also closes a pre-existing gap found while writing it: the IN lane already
# had registers/editorial_ledger_in_archive.jsonl (size-registered in ci_register_size_check) and
# it was NOT in this tuple, so every id archived out of the IN ledger was invisible to the
# citation-integrity gate. Deriving covers both by construction; enumerating covered neither.
ARCHIVE_JSONL_PATHS = ('registers/editorial_ledger_archive.jsonl',) + tuple(
    f'registers/editorial_ledger_{lane.lower()}_archive.jsonl' for lane in LANE_CODES
)


# ── Pure core (network-free; unit-tested) ─────────────────────────────────────

def _canon_id(prefix: str, num: str, lane: str = None) -> str:
    """Normalise ED-017 / ED-17 -> 'ED-17' (flat) or ED-MB-0001 / ED-MB-1 -> 'ED-MB-1'
    (lane-tagged) so zero-padding never mismatches either format."""
    if lane:
        return f"{prefix}-{lane}-{int(num)}"
    return f"{prefix}-{int(num)}"


def _is_resolved(status) -> bool:
    """A citation basis is satisfied by any terminal/decided entry. Accepts the
    canonical statuses plus their legitimate synonyms (ratified/confirmed) and
    terminal states (deprecated) so a genuinely-decided ED is never a violation."""
    if status is None:
        return False
    s = str(status).strip().lower()
    return (s.startswith('resolved') or s.startswith('ratif')   # ratified / ratified-...
            # 'landed' added 2026-07-30 (ED-IN-0098). It was already in live use by ED-IN-0095/0096
            # and was NOT accepted here, so the first citation of a `landed` ED from a scanned
            # prefix turned a blocking gate red for a bookkeeping-vocabulary reason rather than a
            # citation-integrity one. That happened during W4 (ED-IN-0097) and was patched by
            # editing the ENTRY's status instead of this vocabulary — the wrong end, because it left
            # the trap armed for 0095/0096 and any future entry using the same word. 'landed' means
            # the work shipped: terminal and decided, exactly what this function's own docstring
            # says it accepts. Fixed at the vocabulary end now.
            or s == 'landed'
            or s in ('struck', 'applied', 'superseded', 'closed', 'confirmed', 'deprecated'))


def _is_working_doc(path: str) -> bool:
    """Audits/workplans propose & track EDs; they don't assert canon — out of mandate."""
    if any(path.startswith(p) for p in WORKING_PREFIXES):
        return True
    return 'workplan' in path.rsplit('/', 1)[-1].lower()


def _is_provenance(path: str) -> bool:
    """Provenance registers record where an ED applies — never a basis claim."""
    return path in PROVENANCE_PATHS or any(path.startswith(p) for p in PROVENANCE_PREFIXES)


def _expand_nums(group: str) -> list:
    """Expand a citation's numeric group into individual ED numbers.

    Handles slash groups (865/874 -> [865, 874]) and inclusive ranges
    (844-856 / 844–856 -> [844..856]). Ranges wider than 200 are not expanded
    (only the low bound is checked) to guard against pathological spans.
    """
    nums = []
    for token in group.split('/'):
        rng = re.match(r'^(\d{1,4})[-–](\d{1,4})$', token)
        if rng:
            lo, hi = int(rng.group(1)), int(rng.group(2))
            if lo <= hi <= lo + 200:
                nums.extend(str(n) for n in range(lo, hi + 1))
            else:
                nums.append(rng.group(1))
        else:
            nums.append(token)
    return nums


def build_status_map(entries) -> dict:
    """entries: iterable of {'id','status'} dicts -> {canon_id: status}."""
    out = {}
    for e in entries:
        i = (e or {}).get('id')
        if not i:
            continue
        m = re.match(rf'^(ED|PP)-(?:({_LANE_ALT})-)?(\d+)$', str(i).strip())
        if m:
            out[_canon_id(m.group(1), m.group(3), m.group(2))] = e.get('status')
    return out


def audit_citations(docs: dict, status_map: dict, checked_prefixes=('ED',)) -> list:
    """
    docs:        {path: text}
    status_map:  {canon_id: status}  (canon_id missing => nonexistent)
    Returns list of violation dicts: {path,line,id,kind[,status],ctx}.
    """
    out = []
    checked = set(checked_prefixes)
    for path, text in docs.items():
        prov = _is_provenance(path)
        for m in CITE_RE.finditer(text):
            prefix = m.group(1)
            if prefix not in checked:
                continue
            lane = m.group(2)
            line = text.count('\n', 0, m.start()) + 1
            ctx = text[max(0, m.start() - CONTEXT): m.end() + CONTEXT].replace('\n', ' ').strip()
            # Basis detection uses the citation's OWN line only — a 90-char window
            # bleeds across table-row / list-item boundaries and counts a neighbour
            # row's "RESOLVED"/"canonical" as if it qualified this citation (false
            # OPEN_AS_BASIS). The display ctx above stays wide for human context.
            ls = text.rfind('\n', 0, m.start()) + 1
            le = text.find('\n', m.end())
            ctx_l = text[ls:(le if le != -1 else len(text))].lower()
            for num in _expand_nums(m.group(3)):
                raw = f"{prefix}-{lane}-{num}" if lane else f"{prefix}-{num}"
                key = _canon_id(prefix, num, lane)
                if key not in status_map:
                    out.append({'path': path, 'line': line, 'id': raw, 'kind': 'NONEXISTENT', 'ctx': ctx})
                elif not _is_resolved(status_map[key]):
                    # A basis claim requires a basis keyword AND a non-provenance file
                    # AND no planning/negation marker that recasts it as discussion.
                    is_basis = (not prov
                                and any(k in ctx_l for k in BASIS_KEYWORDS)
                                and not any(n in ctx_l for n in NONBASIS_MARKERS))
                    kind = 'OPEN_AS_BASIS' if is_basis else 'OPEN_INFO'
                    out.append({'path': path, 'line': line, 'id': raw, 'kind': kind, 'status': status_map[key], 'ctx': ctx})
    return out


# ── Local working-tree layer (default; no network, no PAT) ───────────────────

def _walk_entries(obj):
    """Yield dicts that look like ledger entries ({'id': 'ED-..'} or {'id': 'ED-MB-..'})
    anywhere in a YAML structure."""
    if isinstance(obj, dict):
        if 'id' in obj and re.match(rf'^(ED|PP)-(?:(?:{_LANE_ALT})-)?\d+$', str(obj.get('id')).strip()):
            yield obj
        for v in obj.values():
            yield from _walk_entries(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk_entries(v)


def _read(path):
    try:
        with open(path, encoding='utf-8', errors='replace') as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError):
        return None


# id + (optionally) nearby status, tolerant of malformed/garbled YAML indentation.
# Flat ED-\d+ only, by design: archives under ARCHIVE_GLOBS predate the lane-tagged
# namespace (2026-07-02) and can never contain an ED-<LANE>-NNNN id.
_SALVAGE_ID = re.compile(r'(?:^|[\s"\'-])id["\']?\s*:\s*["\']?(ED-\d+)', re.M)
_SALVAGE_STATUS = re.compile(r'status["\']?\s*:\s*["\']?([A-Za-z][\w-]*)')


def _salvage_entries(raw: str) -> list:
    """Recover {'id','status'} entries from an archive whose YAML won't parse.

    Frozen archive fragments carry orphaned/mixed-indent lines that defeat
    yaml.safe_load. Rather than silently lose every ID in the file (or hand-edit
    frozen history), pull each `id: ED-NNN` and the `status:` in its block so the
    universe still includes archived IDs. Status is read from the window up to the
    next `id:` (its own block); absent => None (still registers ID existence)."""
    out = []
    hits = list(_SALVAGE_ID.finditer(raw))
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(raw)
        block = raw[m.end():end]
        sm = _SALVAGE_STATUS.search(block)
        out.append({'id': m.group(1), 'status': sm.group(1) if sm else None})
    return out


def _walk_repo_files():
    """Walk exactly the trees SCAN_PREFIXES declares — one source of truth, not two.

    THIS FUNCTION SILENTLY SHRANK THIS GATE TO 15% OF ITS DECLARED SCOPE. It walked a hardcoded
    `('canon', 'designs', 'params', 'references', 'archives', 'deprecated')`. Three of those six
    no longer exist: `designs/` retired 2026-07-19, `params/` moved to `engine/params/`
    2026-07-16, `archives/` merged into `deprecated/archives/` 2026-07-16. Meanwhile `systems/`
    and `engine/params/` were correctly added to SCAN_PREFIXES — but SCAN_PREFIXES only FILTERS
    what this function yields, so the 205 subsystem design docs and 43 engine/params docs were
    never produced in the first place. Measured 2026-08-01: 45 files scanned, 293 in mandate. A
    blocking CI gate believed it covered the canonical corpus and covered canon/ + references/.

    Two lists, one updated and one not — CLAUDE.md §0.1 point 5 exactly. The fix is to delete the
    second list rather than repair it: the walk roots ARE the scan prefixes. `deprecated/` was
    also being walked purely to be discarded by SKIP_PREFIXES a moment later.

    `tests/valoria/test_ed_citation_scope.py` fails if the scanned set collapses again.

    SPLIT FROM THE ARCHIVE WALK, and that split is the point. One walker served two unrelated
    questions — "which docs do I audit?" and "where do I load the ED universe from?" — which
    happened to work only because the old hardcoded list was a superset of both. Deriving this
    one from SCAN_PREFIXES immediately starved the other: the universe fell 1167 -> 1107 and 110
    valid citations became NONEXISTENT, because `deprecated/archives/editorials/` left the walk.
    Caught by measuring against a pre-change control rather than reading the diff. Archive
    loading now walks ARCHIVE_GLOBS itself (see _walk_archive_files).
    """
    return _walk(SCAN_PREFIXES)


# A GENERATED INVENTORY QUOTES CITATIONS; IT DOES NOT MAKE THEM (ED-IN-0142, 2026-08-04).
#
# `systems/<sub>/_identifier_census.yaml` records, for every identifier a design doc names, the
# table row or sentence the doc uses it in — quoted VERBATIM, because summarising would be
# authorship. Those quotes carry the docs' own `ED-NNN` references, and this gate then read the
# inventory as though it were asserting an open ED as its basis: 17 OPEN_AS_BASIS findings, every
# one a quotation of a finding the gate had already counted in the source doc. Double-counting a
# citation because a generated file echoed it is noise, and noise in a blocking gate is how the
# gate stops being read.
#
# The predicate is deliberately NARROW — both conditions required, so it cannot become a general
# escape hatch: (1) the basename starts with `_`, the repo's marker for a generated sidecar, AND
# (2) the file carries the literal `GENERATED by tools/` provenance banner. A hand-authored doc
# cannot acquire the exemption by being renamed, and a generated file cannot acquire it by
# dropping its banner. Anything failing either test is scanned exactly as before.
_GENERATED_BANNER = 'GENERATED by tools/'


def is_generated_sidecar(path: str) -> bool:
    """True for a generated inventory that QUOTES citations rather than making them."""
    if not os.path.basename(path).startswith('_'):
        return False
    try:
        with open(path, encoding='utf-8', errors='ignore') as fh:
            return _GENERATED_BANNER in fh.read(4000)
    except OSError:
        return False


def _walk(prefixes):
    out = []
    for prefix in prefixes:
        base = prefix.rstrip('/')
        if not os.path.isdir(base):
            continue  # a retired tree is not an error; it just yields nothing
        for root, _dirs, files in os.walk(base):
            for fn in files:
                full = os.path.join(root, fn).replace('\\', '/')
                if is_generated_sidecar(full):
                    continue
                out.append(full)
    return out


def is_deferred(v):
    """Is this finding pre-existing debt in a burn-down tree, rather than a build-failing error?

    MODULE-LEVEL ON PURPOSE. This started as a closure inside main(), and the test for it had to
    re-implement the rule inline — so the test passed while the real predicate was mutated to defer
    NONEXISTENT as well. An assertion against your own copy of the logic is not an assertion about
    the code (§0.1 point 2). Importable now, and the test calls this.

    A NONEXISTENT id is NEVER deferred: it is a broken reference, not an undecided one, and it
    fails wherever it appears. Neither is anything outside BURN_DOWN_ALLOW — deferral is granted to
    five named pre-existing findings, not to a region of the tree with a spare-capacity budget.
    """
    return (v['kind'] == 'OPEN_AS_BASIS'
            and v['path'].startswith(BURN_DOWN_PREFIXES)
            and (v['path'], v['id']) in BURN_DOWN_ALLOW)


def _walk_archive_files():
    """Where the ED universe is loaded from — ARCHIVE_GLOBS, its own declared constant.

    Deliberately NOT SCAN_PREFIXES: the audit scope is canonical surfaces, while the universe
    must include retired/archived ledgers precisely because a citation to an archived ED is
    legitimate (ED-IN-0075 established that). The two sets are near-disjoint, and sharing a
    walker between them silently coupled the gate's verdicts to the gate's scope.
    """
    return _walk(ARCHIVE_GLOBS)


def load_ed_universe(warn=True) -> dict:
    """Active JSONL ledger + editorial archive YAMLs/JSONLs on disk -> {canon_id: status}.

    The active ledger is AUTHORITATIVE. Archive entries are loaded FIRST and the
    active JSONL LAST, so that build_status_map's last-write-wins ordering lets a
    current active-ledger status override any stale archived copy of the same ID
    (e.g. an archived 'ED-864: open' must not shadow the active 'ED-864: struck').

    Archive YAML parse failures are SURFACED (stderr) and counted, never silently
    swallowed — otherwise the 'active + archives' universe would quietly shrink to
    active-only and start emitting false NONEXISTENTs for archive-only IDs.
    """
    import yaml
    archive_entries = []
    dropped = []
    for ap in _walk_archive_files():
        if (any(ap.startswith(g) for g in ARCHIVE_GLOBS)
                and 'editorial_ledger' in ap and ap.endswith(('.yaml', '.yml'))):
            raw = _read(ap)
            if not raw:
                continue
            try:
                data = yaml.safe_load(raw)
                parsed = list(_walk_entries(data))
            except Exception as e:
                # Don't lose the file: salvage its IDs via regex, but record that
                # it is malformed so the breakage stays visible.
                salvaged = _salvage_entries(raw)
                dropped.append((ap, (str(e).splitlines()[0] if str(e) else type(e).__name__), len(salvaged)))
                archive_entries.extend(salvaged)
                continue
            archive_entries.extend(parsed)
    # flat overflow archive (ARCHIVE_JSONL_PATHS) + per-lane archives
    # (registers/editorial_ledger_<lane>_archive.jsonl — the lane-split mirror of the flat
    # overflow convention; the IN lane's was the first, ED-IN-0075). Globbed so every lane's
    # archive joins the ED universe automatically and archived-ED citations never NONEXIST.
    import glob as _glob
    _jsonl_archives = list(dict.fromkeys([
        *ARCHIVE_JSONL_PATHS,
        *sorted(_glob.glob('registers/editorial_ledger_*_archive.jsonl')),
    ]))
    for ap in _jsonl_archives:
        raw = _read(ap)
        if not raw:
            continue
        bad_lines = 0
        for ln in raw.splitlines():
            ln = ln.strip()
            if not ln:
                continue
            try:
                archive_entries.append(json.loads(ln))
            except Exception:
                bad_lines += 1
        if warn and bad_lines:
            dropped.append((ap, f"{bad_lines} malformed JSONL line(s)", 0))
    active_entries = []
    for active_path in ('registers/editorial_ledger.jsonl', *LANE_LEDGER_PATHS):
        led = _read(active_path) or ''
        for ln in led.splitlines():
            ln = ln.strip()
            if ln:
                try:
                    active_entries.append(json.loads(ln))
                except Exception:
                    pass
    if warn and dropped:
        sys.stderr.write(
            f"WARNING: {len(dropped)} editorial-archive file(s) failed YAML parse; "
            f"IDs salvaged via regex fallback (fix the source YAML to silence this):\n")
        for ap, msg, n in dropped:
            sys.stderr.write(f"  - {ap}: {msg} (salvaged {n} id(s))\n")
    # archives first, active last → active status is authoritative on conflict.
    return build_status_map(archive_entries + active_entries)


def select_docs(only_paths=None):
    if only_paths:
        return list(only_paths)
    return [p for p in _walk_repo_files()
            if p not in REGISTER_PATHS
            and any(p.startswith(s) for s in SCAN_PREFIXES)
            and not any(p.startswith(s) for s in SKIP_PREFIXES)
            and not _is_working_doc(p)
            and p.endswith(SCAN_SUFFIXES)]


def main():
    ap = argparse.ArgumentParser(description='Validate ED citations against the editorial ledger universe (reads the working tree).')
    ap.add_argument('--path', nargs='*', default=None, help='Scan only these repo paths.')
    ap.add_argument('--info', action='store_true', help='Also print INFO-level open references.')
    args = ap.parse_args()

    status_map = load_ed_universe()
    print(f'ED universe: {len(status_map)} ids loaded (active + archives)')

    paths = select_docs(args.path)
    docs = {}
    for p in paths:
        c = _read(p)
        if c is not None:
            docs[p] = c
    print('Mandate: canonical surfaces only — audits/workplans excluded '
          '(designs/audit/, workplans/, *workplan*); provenance registers '
          'reported as INFO, not basis.')
    print(f'Scanning {len(docs)} doc(s) for ED citations...\n')

    viols = audit_citations(docs, status_map, checked_prefixes=('ED',))
    all_errors = [v for v in viols if v['kind'] in ('NONEXISTENT', 'OPEN_AS_BASIS')]
    infos = [v for v in viols if v['kind'] == 'OPEN_INFO']

    burn = [v for v in all_errors if is_deferred(v)]
    errors = [v for v in all_errors if not is_deferred(v)]

    for v in sorted(errors, key=lambda x: (x['kind'], x['path'], x['line'])):
        extra = f" (status={v.get('status')})" if 'status' in v else ''
        print(f"[{v['kind']}] {v['path']}:{v['line']} cites {v['id']}{extra}")
        print(f"    …{v['ctx']}…")
    for v in sorted(burn, key=lambda x: (x['path'], x['line'])):
        print(f"[BURN-DOWN] {v['path']}:{v['line']} cites {v['id']} (status={v.get('status')})")
    if args.info:
        for v in infos:
            print(f"[OPEN_INFO] {v['path']}:{v['line']} references {v['id']} (status={v.get('status')})")

    over = len(burn) > BURN_DOWN_MAX
    if burn:
        print(f"\n[BURN-DOWN] {len(burn)} pre-existing open-ED-as-basis finding(s) in "
              f"{', '.join(BURN_DOWN_PREFIXES)} (ceiling {BURN_DOWN_MAX}, ED-IN-0117). "
              f"{'CEILING EXCEEDED — this changeset adds new debt.' if over else 'Not gating.'}")
    print(f"\n{len(errors)} citation-integrity violation(s); {len(burn)} deferred; "
          f"{len(infos)} open-reference info.")
    sys.exit(1 if errors or over else 0)


if __name__ == '__main__':
    main()
