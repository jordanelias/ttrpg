"""The subsystem flow skeletons must be TRACED, not recalled.

A flow skeleton (`systems/<x>/<x>_flow_skeleton_v1.md`, format owned by
`.designs/systems/_architecture/reference/subsystem_flow_skeletons_v1.md`) is a structural description of one
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
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import pathres  # noqa: E402  the single owner of "where did this path go" (CLAUDE.md §8)
SPEC = os.path.join(ROOT, '.designs', 'systems', '_architecture', 'reference', 'subsystem_flow_skeletons_v1.md')

# ED-IN-0231 (2026-09-16): the spec and the skeletons it rosters are quarantined under
# `.designs/`, which MIRRORS the tree — an archived path is `.designs/` + its original path and
# nothing else changes. The roster rows inside the spec still name the pre-quarantine paths, and
# they are left that way on purpose: an archived document is frozen, and rewriting its body to
# chase a move is how a "historical record" stops being one. The reader resolves instead.
ARCHIVE = '.designs'

# The two hidden quarantine trees, as (old_prefix, new_prefix). THEY HAVE DIFFERENT SHAPES:
# `.designs/` PREPENDS to the original path (documents gathered from several trees), while
# `.audit/` REPLACES a prefix (that tree was renamed whole). Spelled the same way in
# `tools/ci_claim_provenance_check.py`; a single "prepend" rule silently yields `.audit/audit/x`,
# which never exists, so every affected anchor reads as a dead file while looking handled.
QUARANTINE_MIRRORS = (('', '.designs/'), ('audit/', '.audit/'))


def archived(relpath):
    """Where a path named INSIDE an archived document actually lives now.

    Returns the candidate that EXISTS; falling back to the `.designs/` form so a genuinely
    missing file still produces a readable failure rather than the original path.
    """
    if relpath.startswith(('.designs/', '.audit/')):
        return relpath
    fallback = None
    for old, new in QUARANTINE_MIRRORS:
        if not relpath.startswith(old):
            continue
        cand = new + relpath[len(old):]
        if fallback is None:
            fallback = cand
        if os.path.isfile(os.path.join(ROOT, cand)):
            return cand
    return fallback if fallback is not None else relpath

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
ATLAS = '.designs/systems/_architecture/reference/engine_atlas_v1.md'
ANCHORED_DOCS = [(r[0], r[1], r[2]) for r in ROSTER] + [('engine_atlas', 'IN', ATLAS)]
ANCHORED_IDS = SUBSYSTEM_IDS + ['engine_atlas']


def test_roster_parses():
    """If the roster parse breaks, every parameterized test below silently vanishes."""
    assert len(ROSTER) >= 15, f"roster parsed only {len(ROSTER)} rows from {SPEC}"
    for name, lane, path in ROSTER:
        assert path == f'systems/{name}/reference/{name}_flow_skeleton_v1.md', \
            f"roster row {name!r} names an off-convention path: {path}"


@pytest.mark.parametrize('subsystem,lane,relpath', ROSTER, ids=SUBSYSTEM_IDS)
def test_every_roster_subsystem_has_a_skeleton(subsystem, lane, relpath):
    resolved = archived(relpath)
    assert os.path.isfile(os.path.join(ROOT, resolved)), \
        (f"{subsystem} is on the roster in {os.path.relpath(SPEC, ROOT)} §3 but has no "
         f"skeleton at {resolved}. Either trace it or remove the roster row.")


@pytest.mark.parametrize('subsystem,lane,relpath', ROSTER, ids=SUBSYSTEM_IDS)
def test_required_sections_present_and_ordered(subsystem, lane, relpath):
    path = os.path.join(ROOT, archived(relpath))
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
    path = os.path.join(ROOT, archived(relpath))
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


#: Artifacts the `generated_layer` fixture REBUILDS from the live tree on every run, taken from that
#: fixture's own roster so the two cannot drift. Their line numbering is a property of the last
#: build, not of the claim being cited: touch campaign-reachable engine code and
#: `execution_trace.json` renumbers, and an authored citation that says nothing wrong goes red.
#: The mass-battle engine swap (2026-08-24) did exactly that to three citations in three documents.
#:
#: So for these targets the SYMBOL is binding and the LINE is advisory. That is not a weakening:
#: a symbol that must occur in a regenerated file is falsifiable against the current tree, while a
#: line number is falsifiable only against the build that produced it — and there is no such build
#: to check against, because the file is untracked and rebuilt per run. A generated-file citation
#: with no symbol asserts nothing at all and is a HARD failure here, which is stricter than before.
#:
#: This takes the durable fix the earlier docstring flagged for Jordan rather than re-anchoring the
#: three citations to today's build (they would rot on the next campaign-code change, which is the
#: recurrence signature §0.1 pt 5 names). It is answered by architecture, not escalated: CLAUDE.md
#: §0 test 5 — where the design surfaces are silent and one option is clearly right for the code.
from .conftest import _GENERATED_LAYER  # noqa: E402  the single owner of "which files are rebuilt"

GENERATED_TARGETS = frozenset(a for _builder, arts in _GENERATED_LAYER for a in arts)

#: The per-subsystem census sidecars, REBUILT by `build_identifier_census.py` exactly like the
#: `references/identifier_census.json` the layer tuple names — but the tuple names only that one
#: file, so the sidecars were being line-checked as if authored. Measured 2026-09-16: editing
#: `references/module_contracts.yaml` re-numbered `systems/ui/_identifier_census.yaml` and broke an
#: anchor in a frozen skeleton that says nothing wrong.
#:
#: They join the LINE-ADVISORY set below rather than `GENERATED_TARGETS`, for the reason that set
#: records: `GENERATED_TARGETS` REJECTS a bare line number, and one skeleton cites
#: `systems/ui/_identifier_census.yaml:1-2` — a header citation that is both bare and perfectly
#: stable. Rejecting it would red a frozen document over a true claim.
#: ⚠ THE SUBSYSTEM LIST IS THE UNION OF `systems/` AND `.designs/systems/`, AND THE UNION IS THE
#: WHOLE FIX. This read `os.listdir(systems)` alone until 2026-09-17 and was RED ON `main`
#: (`ef56acb`, the `.designs/` quarantine; its parent `b178fd0` was green). ED-IN-0231 moved every
#: `.md` out of `systems/`, and git does not track an empty directory — so **five subsystem
#: directories no longer exist in a fresh clone at all**: measured, `_architecture`, `articulation`,
#: `npcs`, `ui` and `victory` have ZERO tracked files under `systems/`. This frozenset is computed
#: at IMPORT, before the fixture runs the builder that re-creates those directories, so in CI the
#: five were silently omitted and their sidecars were line-checked as if authored. On a developer's
#: tree the directories already exist from an earlier build and the same code passes — which is why
#: it read green locally and red in CI, on the same commit.
#:
#: `tools/build_identifier_census.py` had already solved this, at its own `:197-200`: it unions the
#: two roots for exactly this reason. Taking the same union here is §8's rule — the answer lives
#: once and this is the second caller of it, not a second answer. `.designs/systems/<sub>/` IS
#: tracked, so the union is stable on a fresh clone.
_CENSUS_SIDECARS = frozenset(
    'systems/%s/_identifier_census.yaml' % _sub
    for _sub in sorted(set(os.listdir(os.path.join(ROOT, 'systems')))
                       | (set(os.listdir(os.path.join(ROOT, ARCHIVE, 'systems')))
                          if os.path.isdir(os.path.join(ROOT, ARCHIVE, 'systems')) else set()))
    if os.path.isdir(os.path.join(ROOT, 'systems', _sub))
    or os.path.isdir(os.path.join(ROOT, ARCHIVE, 'systems', _sub))
)

# Files whose LINE NUMBERS are not a stable anchor, though their CONTENT is. Checked by symbol,
# exactly like a generated artifact, because that is the half that stays true.
#
# ED-IN-0231 (2026-09-16): `references/canonical_sources.yaml` joined this set when the design-prose
# quarantine deleted 102 doc pins from it and the file went 584 lines -> 292. Every line-numbered
# anchor into it was instantly out of range — through no fault of the skeletons, which are archived
# and frozen. This module's own docstring already named the durable fix ("cite those files by symbol
# without a line"); this applies it to the one file where the tax actually came due, rather than
# editing frozen documents to chase a line count.
LINE_UNSTABLE_TARGETS = frozenset({'references/canonical_sources.yaml'})

# Files the Key-substrate retirement gutted (ED-IN-0232, 2026-09-16). Their line numbers moved by
# tens to hundreds of lines and EVERY archived anchor into them went out of range at once.
#
# ⚠ THESE DO NOT JOIN `LINE_UNSTABLE_TARGETS`, AND THE REASON IS A MEASUREMENT, NOT A PREFERENCE.
# That set demands a symbol in place of the line, which worked for `canonical_sources.yaml` because
# every anchor into it carried one. Measured across `.designs/` for the files below: **281 of the
# 587 anchors are BARE LINE NUMBERS** — 132 into `mc_v18.py` alone. Adding these files to that set
# would fail all 281 with "cite a symbol", in documents that are ARCHIVED and frozen and therefore
# cannot be corrected. An unsatisfiable requirement is not a stricter gate; it is a red one.
#
# So a bare-line anchor into one of these is recorded as UNVERIFIABLE rather than failed, and a
# symbolled anchor is still checked by symbol — the half that stays true, which is the durable fix
# this module's own docstring named. What is lost is real and is stated rather than buried: a line
# number cited from a frozen archive into live code is a claim nothing can keep true, and 281 of
# them are now unchecked. What is kept: the file must still resolve (live, archived, or FORKED),
# and 306 symbol claims are still asserted.
RETIREMENT_SHIFTED = frozenset({
    'engine/mc_v18.py',
    'engine/autoload/engine_clock.py',
    'engine/cross_scale/scene_dispatch.py',
    'engine/cross_scale/zoom_in_out.py',
    'engine/substrate/__init__.py',
    'systems/factions/sim/faction_action.py',
    'systems/factions/sim/parliamentary_transfer.py',
    'references/module_contracts.yaml',
    'tools/build_execution_map.py',
    # 39 archived anchors cite this file by line; ED-IN-0232 cut 15 Key-delivery test functions
    # out of it, so every line below the first cut moved.
    'engine/tests/test_pipeline_reach.py',
    # Both carry golden re-pins whose recorded-old-values blocks added lines above every anchor.
    'engine/tests/test_f7_smoke_oracle.py',
    'engine/tests/test_mc_v18_regression.py',
}) | _CENSUS_SIDECARS

# Symbols the Key retirement DELETED (ED-IN-0232). An archived skeleton citing one of these is not
# stale — it is correct about a tree that no longer exists, which is the same situation a `FORK:`
# row describes for a whole file. The citation resolves at `FORK:c6e82105`, where the symbol is
# still there. Listed explicitly, one line each, rather than matched by pattern: a pattern would
# also swallow a symbol that went missing by accident, which is the failure this test is for.
#
# ⚠ FOUR ENTRIES WERE REMOVED FROM THIS SET after an adversarial pass, and the reason is the
# difference between "explicit" and "narrow". The first cut listed `accounting_boundary`,
# `next_tick`, `echo_scheduler` and `Key` — none of which is a deleted symbol:
#   * `accounting_boundary` is LIVE. `engine/autoload/engine_clock.py` still defines
#     `PHASE_ACCOUNTING_BOUNDARY = "accounting_boundary"`; the boundary was DEMOTED from a call to a
#     position, not deleted. An archived anchor citing it would have passed its symbol check, and
#     the skip would have silenced that check for good.
#   * `next_tick` still occurs as a live token in `engine/autoload/engine_clock.py`, so anchors
#     citing it resolve on their own.
#   * `Key` is matched by a raw substring test over the whole file, and every one of these files
#     contains the word in its own retirement commentary — so the entry did nothing except disarm
#     any anchor whose symbol leaf is exactly `Key`.
# `echo_scheduler` was removed in that same correction AND PUT BACK, which is worth recording
# because the correction was itself half wrong: the token does survive, but ONLY inside four
# comments that describe its retirement (`scene_dispatch.py:228,:388` and the two golden re-pin
# notes). Every anchor citing it points at `faction_action.py` or `mc_v18.py`, where the identifier
# is genuinely gone. A symbol whose last occurrences are prose about its own deletion is retired.
# Every entry below was grepped across `engine/`, `systems/` and `tools/` and occurs nowhere.
RETIRED_SYMBOLS = frozenset({
    'key_log_hash', 'keys_emitted', 'subscribe_all', 'run_parliamentary_scene',
    'echo_scheduler', '_emit_battle_concluded', '_emit_public_governance_transfer',
    'KeyLog', 'TickScheduler', 'TypeRegistry', 'EmittedAt', 'emit_scene_echo',
    'make_scheduler', '_echo_transport_on',
    '_battle_key_seq', '_parl_key_seq',
    # the articulation bus subscriber and the one test that exercised it end-to-end
    'evaluate_articulation_triggers',
    'test_combat_pair_key_reaches_articulation_subscriber_under_flag_on',
    # `UNREACHABLE` was a marker word inside `_emit_public_governance_transfer`'s docstring, cited
    # by the factions skeleton. It went with the function.
    'UNREACHABLE',
})

# Generated artifacts the retirement took with their builders (ED-IN-0232). These get no `FORK:`
# row — they were UNTRACKED, so no ref holds them and a row would promise content that is not
# there (see the ledger's own note). Their builders ARE forked, which is the stronger provenance:
# re-run `build_key_graph.py` or `build_contract_index.py` at `c6e82105` and the file comes back.
RETIRED_GENERATED = frozenset({
    'references/key_graph.json',
    'references/KEY_INDEX.md',
    'references/CONTRACT_INDEX.md',
})


def _is_retired(filepath):
    """Does the ledger record this exact path as FORKED?

    ⚠ `pathres.resolve` MATCHES DIRECTORY PREFIXES, so it answers FORKED for any invented filename
    under a forked directory (CLAUDE.md §8 records that hazard by name). Here that is the WANTED
    behaviour and the narrow one: an anchor cites a real path that was deleted, and the rows written
    for ED-IN-0232 are exact file rows, not a directory prefix. An anchor citing a path that never
    existed still fails, because no row covers it.
    """
    try:
        return pathres.resolve(filepath).status == pathres.FORKED
    except Exception:
        return False


def _anchor_failures(relpath):
    """Return (failures, checked) for one skeleton. `checked` counts symbol assertions only."""
    failures, checked = [], 0
    for filepath, start_s, end_s, symbol in ANCHOR_RE.findall(_read(os.path.join(ROOT, archived(relpath)))):
        # An anchor written before the quarantine names the pre-quarantine path; the archive
        # mirrors the tree, so the same prefix rule resolves it (ED-IN-0231). The skeleton's own
        # text is left alone — an archived document records what was true when it was written.
        target = os.path.join(ROOT, filepath)
        if not os.path.isfile(target):
            candidate = os.path.join(ROOT, archived(filepath))
            if os.path.isfile(candidate):
                target = candidate
        where = f"{relpath} -> `{filepath}:{start_s}{'-' + end_s if end_s else ''}"
        where += f" {symbol}`" if symbol else "`"

        if not os.path.isfile(target) and filepath in RETIRED_GENERATED:
            continue

        if not os.path.isfile(target):
            # A RETIRED path is resolvable, not broken (CLAUDE.md §1: retiring means deleting and
            # writing a `FORK:` row). The archived skeleton's own text is left alone — it records
            # what was true when it was written — and the anchor resolves through the ledger to the
            # ref that still holds the file. NEITHER the line number NOR the symbol can be checked
            # against a deleted file, and that is stated rather than silently skipped: this branch
            # buys resolvability, not currency. `pathres.resolve` is the single owner of the answer
            # (§8); an unretired missing file still fails below.
            if _is_retired(filepath):
                continue
            failures.append(f"{where}: file does not exist")
            continue

        if filepath in RETIREMENT_SHIFTED:
            # Line advisory, symbol still binding. See RETIREMENT_SHIFTED for why this is not the
            # `LINE_UNSTABLE_TARGETS` treatment.
            if not symbol:
                continue
            leaf = symbol.rsplit('.', 1)[-1]
            if leaf in RETIRED_SYMBOLS:
                continue
            checked += 1
            if leaf not in _read(target):
                failures.append(
                    f"{where}: symbol {leaf!r} does not occur anywhere in {filepath}. The line is "
                    f"advisory for a file the Key retirement re-numbered (ED-IN-0232); the symbol "
                    f"is not, and this one is absent.")
            continue

        if filepath in GENERATED_TARGETS or filepath in LINE_UNSTABLE_TARGETS:
            if not symbol:
                failures.append(
                    f"{where}: {filepath} is REBUILT every run, so a bare line number cites a build "
                    f"rather than a claim. Cite a symbol — that is the half that stays checkable.")
                continue
            leaf = symbol.rsplit('.', 1)[-1]
            checked += 1
            if leaf not in _read(target):
                failures.append(
                    f"{where}: symbol {leaf!r} does not occur anywhere in {filepath}. The line is "
                    f"advisory for a regenerated file; the symbol is not, and this one is absent.")
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
def test_anchors_resolve(subsystem, lane, relpath, generated_layer):
    """Every anchor must name a file that exists, a line in range, and a symbol that covers it.

    REQUESTS `generated_layer` BECAUSE TWELVE ANCHORS POINT INTO UNTRACKED GENERATED FILES.
    Measured 2026-08-22 after CI flaked on `[ui]`: `systems/ui/` cites
    `systems/ui/_identifier_census.yaml` three times, `systems/world/` and `systems/factions/`
    cite `references/execution_{map,trace}.json` nine times between them. Culling wave 5 untracked
    all of those, so on a clean checkout the target is absent until some builder runs — and under
    `-n auto` whether it has run yet is a scheduling accident. The gate then reports "file does not
    exist" for an anchor that is perfectly correct.

    ⚠ THIS MAKES THE TEST DETERMINISTIC; IT DOES NOT MAKE THE ANCHORS SOUND, and the difference is
    worth stating rather than papering over. A line-numbered citation into a REGENERATED file is a
    claim that rots whenever the generator's input changes: touch campaign-reachable engine code and
    `execution_trace.json` renumbers, breaking an authored design doc that says nothing wrong. That
    is the document tax culling wave 5 removed, re-entering through a different door. The durable
    fix is to cite those files by symbol without a line, which needs a checker change plus edits to
    twelve citations in four design docs — a design-surface call, flagged for Jordan rather than
    taken here while fixing a red gate.
    """
    if not os.path.isfile(os.path.join(ROOT, archived(relpath))):
        pytest.skip('missing skeleton — reported by test_every_roster_subsystem_has_a_skeleton')
    failures, _ = _anchor_failures(relpath)
    assert not failures, f"{len(failures)} unresolvable anchor(s):\n  " + "\n  ".join(failures)


def test_the_suite_actually_checked_symbols(generated_layer):
    """An assertion that never ran is not a passing assertion (CLAUDE.md §0.1 point 2).

    If the anchor regex stops matching — a format drift, an escaping change — every per-file
    test above passes vacuously on an empty match list. This is the tripwire for that.
    """
    total_anchors = 0
    total_symbol_checks = 0
    for _, _, relpath in ROSTER:
        if not os.path.isfile(os.path.join(ROOT, archived(relpath))):
            continue
        _, checked = _anchor_failures(relpath)
        total_symbol_checks += checked
        total_anchors += len(ANCHOR_RE.findall(_read(os.path.join(ROOT, archived(relpath)))))

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
    path = os.path.join(ROOT, archived(relpath))
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


MODULE_CONTRACTS = os.path.join(ROOT, 'references', 'module_contracts.yaml')
_CONTRACTS_HEADER_RE = re.compile(r'^\*\*Subsystem:\*\*.*?\*\*Contracts:\*\*(.*)$', re.M)
#: ⚠ THE ROSTER MOVED SOURCE 2026-09-16 (ED-IN-0232), and it moved because the old one is gone
#: rather than because a better one appeared. This read `### <module>` headings out of
#: `references/CONTRACT_INDEX.md`, the rendered view `tools/build_contract_index.py` generated —
#: deliberately, so the roster had ONE owner and this test composed on it instead of re-deriving.
#: Both the tool and its output retired with the Key substrate (half that renderer's job was the
#: registry<->Key-type join), so the index can never be rebuilt.
#:
#: It now reads `module_contracts.yaml` directly. That IS a re-derivation, and CLAUDE.md §8 would
#: normally object — but the index was itself derived from this file, so with the index gone there
#: is exactly one owner again and reading it is composing on the owner, not minting a second answer.
#: The alternative was the `pytest.skip` an adversarial pass caught here: absent index -> skip ->
#: EVERY parametrized case skipped, and the file's own `len(known) >= 20` anti-vacuity guard
#: short-circuited with it. A permanently-skipping test is worse than a re-derived roster.
_YAML_MODULE_RE = re.compile(r'^  - module: ([a-z_]+)\s*$', re.M)

#: Module contracts retired by ruling rather than renamed away. Listed one per line for the same
#: reason `RETIRED_SYMBOLS` is: a pattern would also swallow a row someone deleted by accident.
RETIRED_CONTRACTS = frozenset({'articulation_layer'})


@pytest.mark.parametrize('subsystem,lane,relpath', ROSTER, ids=SUBSYSTEM_IDS)
def test_contract_names_resolve_in_the_generated_index(subsystem, lane, relpath):
    """A skeleton's `Contracts:` header must name real module contracts.

    `references/module_contracts.yaml` owns the module roster. See the note on `_YAML_MODULE_RE`
    for why this reads the registry directly rather than the generated index it used until
    2026-09-16.

    It exists because the drift it guards already happened: at first join, `social_contest`'s
    header named Python module paths instead of its contract, and four more headers carried a
    source-file path in the contract slot. Both read as citations and neither was checkable until
    there was a roster to resolve against.
    """
    path = os.path.join(ROOT, archived(relpath))
    if not os.path.isfile(path):
        pytest.skip('missing skeleton — reported by test_every_roster_subsystem_has_a_skeleton')

    known = set(_YAML_MODULE_RE.findall(_read(MODULE_CONTRACTS)))
    assert len(known) >= 20, (
        f"parsed only {len(known)} `- module:` rows from module_contracts.yaml — the registry "
        f"shape changed and this check is now vacuous")

    m = _CONTRACTS_HEADER_RE.search(_read(path))
    assert m, f"{relpath}: no `**Contracts:**` field in the header block"
    named = re.findall(r'`([^`]+)`', m.group(1))
    # A contract RETIRED out of the registry is not a mis-named header. `articulation_layer`'s
    # `sim_module` was `engine/cross_scale/articulation.py`, the Key-bus subscriber, so the row went
    # with the substrate (ED-IN-0232) — and the archived skeleton that names it is frozen and
    # correct about the tree it was written against. This is the same distinction the anchor checker
    # draws with `RETIRED_SYMBOLS`: gone-by-ruling resolves, gone-by-typo still fails.
    unknown = [n for n in named if n not in known and n not in RETIRED_CONTRACTS]
    assert not unknown, (
        f"{relpath}: `Contracts:` names {unknown}, which are not module contracts — "
        f"module_contracts.yaml has no `- module:` row for them. Name the contract "
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
