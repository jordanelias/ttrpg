"""The subsystem flow skeletons must be TRACED, not recalled.

A flow skeleton (`systems/<x>/<x>_flow_skeleton_v1.md`, format owned by
`systems/_architecture/subsystem_flow_skeletons_v1.md`) is a structural description of one
subsystem assembled by reading its code. The failure mode that matters is not a typo — it is a
skeleton that *reads* correct, cites plausible files, and was never traced. Prose cannot
distinguish the two, and neither can a reviewer skimming it.

The anchor rule is what makes the difference observable. Every factual line ends with
`` `path:line symbol` ``, and this module asserts three things per anchor:

  1. the file exists,
  2. the line exists,
  3. **the named symbol really occurs within ±3 lines of the cited line.**

(3) is the load-bearing one and the reason the format demands a symbol at all. A path alone is
cheap to guess and a line number alone is unfalsifiable; a *line number that must land on its
symbol* cannot be produced without opening the file. Recall degrades to wrong line numbers long
before it degrades to wrong file names, so this is the assertion that can observe the failure it
excludes (CLAUDE.md §0.1 point 2).

It is also the assertion that rots on purpose: edit the traced code and the anchors drift off
their symbols, and this test says so. That is intended. A skeleton is a claim about the tree at a
commit, and a stale claim should fail rather than mislead.

Mutation-verified 10/10 — each of these was applied to a real skeleton and observed to turn the
suite red:
  M1a an anchor's line moved outside the named function   -> test_anchors_resolve
  M1b an anchor's symbol renamed to a plausible non-symbol-> test_anchors_resolve
  M1c an anchor's span moved into a different function    -> test_anchors_resolve
  M2  an anchor's path pointed at a non-existent file     -> test_anchors_resolve
  M3  a required section heading deleted from a skeleton  -> test_required_sections_present_and_ordered
  M4  two section headings transposed                     -> test_required_sections_present_and_ordered
  M5  a roster row's skeleton file removed                -> test_every_roster_subsystem_has_a_skeleton
  M6  a skeleton stripped of all anchors                  -> test_skeletons_carry_anchors
  M7  a Contracts name replaced by a Python module path   -> test_contract_names_resolve_in_the_generated_index
  M8  a Contracts name replaced by a source-file path     -> test_contract_names_resolve_in_the_generated_index

**What this does NOT catch, stated because a guard's blind spot is worse when implied to be
absent:** line drift *within* the named definition. Shifting a body-region anchor by a few lines
while it stays inside its own function passes — that was measured (an earlier draft asserting
otherwise was wrong, and this note replaces it). The property actually enforced is "the cited
line falls inside the definition this anchor names", which cannot be produced without opening
the file, but which tolerates edits interior to that definition. Sub-line precision is not
claimed and should not be relied on.
"""
import os
import re

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SPEC = os.path.join(ROOT, 'systems', '_architecture', 'subsystem_flow_skeletons_v1.md')

# The format spec's §2 section contract, in order. A skeleton that drops or reorders one of
# these has diverged in shape, which is the failure the doctrine calls shape divergence.
REQUIRED_SECTIONS = [
    '## 1. Entry points',
    '## 2. IN',
    '## 3. Flow',
    '## 4. OUT',
    '## 5. State touched',
    '## 6. Seams',
    '## 7. Traced gaps',
]

# `path/to/file.py:123 symbol`  ·  `path:123-140`  ·  `path:123`
ANCHOR_RE = re.compile(
    r'`([A-Za-z0-9_./+-]+\.(?:py|gd|md|yaml|yml|json|jsonl|tres|js|cfg|toml|txt))'
    r':(\d+)(?:-(\d+))?'
    r'(?:\s+([A-Za-z_][A-Za-z0-9_.]*)(?:\(\))?)?`'
)

# How far from the cited line the symbol may sit. Small enough that a guessed line fails;
# large enough to tolerate a decorator, a multi-line signature, or a leading comment.
SYMBOL_WINDOW = 3

# A skeleton this thin was not traced. Deliberately low — `ui` may legitimately be near-empty
# and prove an absence instead (spec §2 standing rule 2), so this floor is a smoke threshold,
# not a coverage target.
MIN_ANCHORS_PER_SKELETON = 3

# Below this, the parse broke and the suite is asserting nothing. Guards against a silent
# regex/roster failure turning every test green (§0.1 point 2).
MIN_TOTAL_ANCHORS = 150


def _read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def _roster():
    """The subsystem roster, parsed from the format spec's §3 table — its single owner.

    Adding a row there is what makes this suite demand a new skeleton; there is no second list.
    """
    text = _read(SPEC)
    start = text.index('## 3. Roster')
    end = text.index('## 4. ', start)
    rows = []
    for line in text[start:end].splitlines():
        m = re.match(r'\|\s*`([a-z_]+)`\s*\|\s*([A-Z]{2})\s*\|\s*`([^`]+)`\s*\|', line.strip())
        if m:
            rows.append((m.group(1), m.group(2), m.group(3)))
    return rows


ROSTER = _roster()
SUBSYSTEM_IDS = [r[0] for r in ROSTER]

# The authored master consolidation. It carries anchors copied from the skeletons, and copies rot
# exactly like originals do — a review found ~178 of them checked by nothing, because this suite
# was parameterized over the 15-row roster alone. Anchor-bearing files get anchor checks; the
# roster decides which SUBSYSTEMS exist, not which files are guarded.
ATLAS = 'systems/_architecture/engine_atlas_v1.md'
ANCHORED_DOCS = [(r[0], r[1], r[2]) for r in ROSTER] + [('engine_atlas', 'IN', ATLAS)]
ANCHORED_IDS = SUBSYSTEM_IDS + ['engine_atlas']


def test_roster_parses():
    """If the roster parse breaks, every parameterized test below silently vanishes."""
    assert len(ROSTER) >= 15, f"roster parsed only {len(ROSTER)} rows from {SPEC}"
    for name, lane, path in ROSTER:
        assert path == f'systems/{name}/{name}_flow_skeleton_v1.md', \
            f"roster row {name!r} names an off-convention path: {path}"


@pytest.mark.parametrize('subsystem,lane,relpath', ROSTER, ids=SUBSYSTEM_IDS)
def test_every_roster_subsystem_has_a_skeleton(subsystem, lane, relpath):
    assert os.path.isfile(os.path.join(ROOT, relpath)), \
        (f"{subsystem} is on the roster in {os.path.relpath(SPEC, ROOT)} §3 but has no "
         f"skeleton at {relpath}. Either trace it or remove the roster row.")


@pytest.mark.parametrize('subsystem,lane,relpath', ROSTER, ids=SUBSYSTEM_IDS)
def test_required_sections_present_and_ordered(subsystem, lane, relpath):
    path = os.path.join(ROOT, relpath)
    if not os.path.isfile(path):
        pytest.skip('missing skeleton — reported by test_every_roster_subsystem_has_a_skeleton')
    text = _read(path)

    assert re.search(r'^## Status:', text, re.M), \
        f"{relpath}: no `## Status:` line (the per-doc currency signal)"

    positions = []
    for heading in REQUIRED_SECTIONS:
        idx = text.find('\n' + heading)
        assert idx != -1, f"{relpath}: required section {heading!r} is missing"
        positions.append(idx)

    assert positions == sorted(positions), (
        f"{relpath}: sections are out of the order the format spec fixes. Found: "
        + ' then '.join(h for _, h in sorted(zip(positions, REQUIRED_SECTIONS)))
    )


@pytest.mark.parametrize('subsystem,lane,relpath', ROSTER, ids=SUBSYSTEM_IDS)
def test_skeletons_carry_anchors(subsystem, lane, relpath):
    path = os.path.join(ROOT, relpath)
    if not os.path.isfile(path):
        pytest.skip('missing skeleton — reported by test_every_roster_subsystem_has_a_skeleton')
    anchors = ANCHOR_RE.findall(_read(path))
    assert len(anchors) >= MIN_ANCHORS_PER_SKELETON, (
        f"{relpath}: {len(anchors)} anchors. A skeleton with no anchors is prose, and prose is "
        f"exactly what the format forbids — every factual line carries `path:line symbol`."
    )


def _symbol_covers(lines, start, end, leaf):
    """True if `leaf` names the cited lines, in either of the two legitimate anchor forms.

    **Definition-site anchor** — `path:215 generate_npc` points at where the symbol is declared.
    Satisfied by the symbol appearing within ±SYMBOL_WINDOW lines.

    **Body-region anchor** — `path:250-259 generate_npc` points at a region *inside* the symbol,
    which is how a flow step cites the specific branch it describes rather than the whole
    function. Satisfied when the nearest preceding `def`/`class` of that name encloses the
    region, block extent taken from indentation.

    The second form is why this is not a substring search over the file: the region must fall
    inside *that* definition's block, so an invented line range still fails. Only the anchor's
    granularity is relaxed, not its falsifiability.
    """
    lo = max(0, start - 1 - SYMBOL_WINDOW)
    hi = min(len(lines), start + SYMBOL_WINDOW)
    if any(leaf in ln for ln in lines[lo:hi]):
        return True

    decl = re.compile(r'^(\s*)(?:async\s+)?(?:def|class)\s+' + re.escape(leaf) + r'\b')
    for i in range(min(start, len(lines)) - 1, -1, -1):
        m = decl.match(lines[i])
        if not m:
            continue
        indent = len(m.group(1))
        block_end = len(lines)
        for j in range(i + 1, len(lines)):
            ln = lines[j]
            if not ln.strip():
                continue
            if len(ln) - len(ln.lstrip()) <= indent:
                block_end = j
                break
        return end <= block_end
    return False


def _anchor_failures(relpath):
    """Return (failures, checked) for one skeleton. `checked` counts symbol assertions only."""
    failures, checked = [], 0
    for filepath, start_s, end_s, symbol in ANCHOR_RE.findall(_read(os.path.join(ROOT, relpath))):
        target = os.path.join(ROOT, filepath)
        where = f"{relpath} -> `{filepath}:{start_s}{'-' + end_s if end_s else ''}"
        where += f" {symbol}`" if symbol else "`"

        if not os.path.isfile(target):
            failures.append(f"{where}: file does not exist")
            continue
        lines = _read(target).splitlines()
        start = int(start_s)
        if not 1 <= start <= len(lines):
            failures.append(f"{where}: line {start} is out of range (file has {len(lines)})")
            continue
        if end_s and not 1 <= int(end_s) <= len(lines):
            failures.append(f"{where}: range end {end_s} is out of range (file has {len(lines)})")
            continue
        if not symbol:
            continue

        leaf = symbol.rsplit('.', 1)[-1]
        checked += 1
        end = int(end_s) if end_s else start
        if not _symbol_covers(lines, start, end, leaf):
            failures.append(
                f"{where}: symbol {leaf!r} is neither within ±{SYMBOL_WINDOW} lines of line "
                f"{start} nor the definition enclosing lines {start}-{end}. Either the anchor "
                f"was never opened, or the traced code moved and this skeleton is now stale.")
    return failures, checked


@pytest.mark.parametrize('subsystem,lane,relpath', ANCHORED_DOCS, ids=ANCHORED_IDS)
def test_anchors_resolve(subsystem, lane, relpath):
    if not os.path.isfile(os.path.join(ROOT, relpath)):
        pytest.skip('missing skeleton — reported by test_every_roster_subsystem_has_a_skeleton')
    failures, _ = _anchor_failures(relpath)
    assert not failures, f"{len(failures)} unresolvable anchor(s):\n  " + "\n  ".join(failures)


def test_the_suite_actually_checked_symbols():
    """An assertion that never ran is not a passing assertion (CLAUDE.md §0.1 point 2).

    If the anchor regex stops matching — a format drift, an escaping change — every per-file
    test above passes vacuously on an empty match list. This is the tripwire for that.
    """
    total_anchors = 0
    total_symbol_checks = 0
    for _, _, relpath in ROSTER:
        if not os.path.isfile(os.path.join(ROOT, relpath)):
            continue
        _, checked = _anchor_failures(relpath)
        total_symbol_checks += checked
        total_anchors += len(ANCHOR_RE.findall(_read(os.path.join(ROOT, relpath))))

    assert total_anchors >= MIN_TOTAL_ANCHORS, (
        f"only {total_anchors} anchors parsed across {len(ROSTER)} skeletons — the regex or the "
        f"corpus regressed; the per-file assertions above are running on near-empty input")
    assert total_symbol_checks >= MIN_TOTAL_ANCHORS // 2, (
        f"only {total_symbol_checks} of {total_anchors} anchors carried a symbol. The symbol is "
        f"the falsifiable half of the anchor; path+line alone is guessable")


# A backtick span that contains `<path-with-extension>:<digits>` is an anchor by intent. If the
# strict ANCHOR_RE does not match the WHOLE span, the span is a near-miss and the guard silently
# ignores it — the exact "assertion that cannot observe the failure it excludes" that §0.1 point 2
# names. Found in review: §5 rows written as `path.py:113,196,212-213` (a comma list) parsed as
# zero anchors, so eleven state-table claims carried the document's stated guarantee while being
# checked by nothing.
_SPAN_RE = re.compile(r'`([^`\n]+)`')
_LOOKS_LIKE_ANCHOR_RE = re.compile(
    r'[A-Za-z0-9_./+-]+\.(?:py|gd|md|yaml|yml|json|jsonl|tres|js|cfg|toml|txt):\d')


@pytest.mark.parametrize('subsystem,lane,relpath', ANCHORED_DOCS, ids=ANCHORED_IDS)
def test_no_unparseable_anchor_lookalikes(subsystem, lane, relpath):
    """Every citation that LOOKS like an anchor must BE one the guard can check.

    Without this, malformed anchors degrade silently to unguarded prose instead of failing —
    the worst possible direction for a rot detector to fail in.
    """
    path = os.path.join(ROOT, relpath)
    if not os.path.isfile(path):
        pytest.skip('missing skeleton — reported by test_every_roster_subsystem_has_a_skeleton')

    bad = []
    for span in _SPAN_RE.findall(_read(path)):
        if not _LOOKS_LIKE_ANCHOR_RE.search(span):
            continue
        if not ANCHOR_RE.fullmatch('`' + span + '`'):
            bad.append(span)
    assert not bad, (
        f"{relpath}: {len(bad)} citation(s) look like anchors but do not parse as one, so the "
        f"guard cannot check them. Split multi-location citations into one backtick span each "
        f"(`path:line symbol`); a comma list is not an anchor:\n  "
        + "\n  ".join('`' + b + '`' for b in bad))


CONTRACT_INDEX = os.path.join(ROOT, 'references', 'CONTRACT_INDEX.md')
_CONTRACTS_HEADER_RE = re.compile(r'^\*\*Subsystem:\*\*.*?\*\*Contracts:\*\*(.*)$', re.M)
_INDEX_MODULE_RE = re.compile(r'^### ([a-z_]+)$', re.M)


@pytest.mark.parametrize('subsystem,lane,relpath', ROSTER, ids=SUBSYSTEM_IDS)
def test_contract_names_resolve_in_the_generated_index(subsystem, lane, relpath):
    """A skeleton's `Contracts:` header must name real module contracts.

    `references/CONTRACT_INDEX.md` (generated by `tools/build_contract_index.py`, ED-IN-0151) is
    the rendered, always-fresh view of `module_contracts.yaml`. It owns the module roster; this
    test composes on it rather than re-deriving one, so the two artifacts cannot drift apart in
    the one place they overlap.

    It exists because they already had: at first join, `social_contest`'s header named Python
    module paths instead of its contract, and four more headers carried a source-file path in the
    contract slot. Both read as citations and neither was checkable until the index gave this
    check something to resolve against.
    """
    path = os.path.join(ROOT, relpath)
    if not os.path.isfile(path):
        pytest.skip('missing skeleton — reported by test_every_roster_subsystem_has_a_skeleton')
    if not os.path.isfile(CONTRACT_INDEX):
        pytest.skip(f'{os.path.relpath(CONTRACT_INDEX, ROOT)} absent — nothing to resolve against')

    known = set(_INDEX_MODULE_RE.findall(_read(CONTRACT_INDEX)))
    assert len(known) >= 20, (
        f"parsed only {len(known)} module headings from CONTRACT_INDEX.md — the heading format "
        f"changed and this check is now vacuous")

    m = _CONTRACTS_HEADER_RE.search(_read(path))
    assert m, f"{relpath}: no `**Contracts:**` field in the header block"
    named = re.findall(r'`([^`]+)`', m.group(1))
    unknown = [n for n in named if n not in known]
    assert not unknown, (
        f"{relpath}: `Contracts:` names {unknown}, which are not module contracts — "
        f"CONTRACT_INDEX.md has no `### <module>` heading for them. Name the contract "
        f"(e.g. `social_contest`), not a Python module path or a source file.")


def test_format_spec_is_the_single_owner_of_the_roster():
    """No second roster. If one appears, this points at it."""
    strays = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, 'systems')):
        dirnames[:] = [d for d in dirnames if d not in {'sim', '__pycache__'}]
        for fn in filenames:
            if not fn.endswith('_flow_skeleton_v1.md'):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
            if rel not in {r[2] for r in ROSTER}:
                strays.append(rel)
    assert not strays, (
        "flow skeleton(s) exist that the format spec's §3 roster does not list — the roster is "
        "the single owner and the guard only checks what it lists:\n  " + "\n  ".join(strays))
