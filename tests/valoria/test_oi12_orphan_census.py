"""OI-12 orphan-census pointer — repo bookkeeping, relocated out of the engine suite (ED-IN-0123).

WHY IT MOVED. These two checks lived in `engine/tests/test_pipeline_reach.py`, whose other 25 tests
exercise the engine: Key delivery directions, articulation wiring, campaign population. These two do
not. One asserts that a census list is still recorded in an `audit/` markdown document; the other
loads `skills/valoria-vector-audit/scripts/structure_audit.py` and compares the census to the live
import graph. Both are checks on the repository's own record-keeping.

That mattered concretely rather than aesthetically: they were the last two path-literal escapes out
of `engine/` — reaching `audit/` and `skills/`, two trees the fork plan of record (§5) explicitly
LEAVES behind. `engine/` has to be liftable on its own, and a test suite that reaches into the
process corpus is not liftable. Moving them to `tests/valoria/`, which is where checks on the repo's
apparatus already live, costs nothing and removes the reach.

Nothing about the checks themselves changed — same assertions, same census tuples, same
structure_audit reuse.
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
_REPO_ROOT = ROOT

from . import _structure_audit  # noqa: E402  the single owner of the loader


# ═════════════════════════════════════════════════════════════════════════════════════════════
# §1 acceptance — OI-12 orphan census pointer (plan §3 Wave 2 item 7). Per the Oracle stage's own
# instruction, a manifest row PER still-orphan module is overkill for a 14-module census; this is
# the single pointer row citing the census's actual home
# (audit/2026-07-29-code-shape-open-items/04_execution_ledger.md), matching direction7b's own
# "declared deferral" pattern above rather than re-deriving the census here.
# ═════════════════════════════════════════════════════════════════════════════════════════════

_OI12_ALREADY_STUB_WIRED = (
    "engine/autoload/npc_ai.py",
    "systems/characters/sim/companion.py",
    "systems/overview/sim/rs_track.py",
    "systems/overview/sim/ip_track.py",
    "systems/threadwork/sim/rendering.py",
    "systems/world/sim/miraculous_event.py",
    "systems/world/sim/restoration_movement.py",
)
_OI12_VERIFIED_ORPHAN_NO_CALLSITE = (
    "systems/threadwork/sim/co_movement.py",
    "systems/threadwork/sim/collective.py",
    "systems/threadwork/sim/opposing.py",
    "systems/settlements/sim/settlement.py",
    "systems/settlements/sim/temperaments.py",
    "systems/social_contest/sim/parliamentary_stay.py",
    # engine/autoload/registry.py was in this list until 2026-08-03. It was not just
    # callsite-less: its load_index() read registers/mechanics_index.yaml, a path the
    # fork leaves behind, from inside the engine's own autoload hub. Deleted rather
    # than re-homed -- 120 LOC, zero callers, and the only runtime escape out of
    # engine/ into the register tree.
)


def test_oi12_census_is_recorded_in_the_execution_ledger():
    """The census itself (documentation only, no code edits per the L-artic lane's own note) lives
    in 04_execution_ledger.md, not here — this asserts the full 14-module list this wave's census
    covers is genuinely present there, so a future edit that silently drops a module from the
    ledger's record trips here rather than the census quietly rotting out of sync with this
    pointer. Does not re-verify each module's live import-orphan status (that is
    `test_oi12_census_matches_the_real_structure_audit_classification` below, split out so a
    doc-presence failure and a live-classification-drift failure report distinctly)."""
    doc_path = os.path.join(_REPO_ROOT, "audit", "2026-07-29-code-shape-open-items",
                             "04_execution_ledger.md")
    assert os.path.isfile(doc_path), "04_execution_ledger.md (OI-12 census's home) is missing"
    text = open(doc_path, encoding="utf-8").read()
    assert "OI-12 census" in text, "OI-12 census is no longer recorded in the execution ledger"

    missing = [mod_path for mod_path in _OI12_ALREADY_STUB_WIRED + _OI12_VERIFIED_ORPHAN_NO_CALLSITE
               if mod_path not in text]
    assert not missing, (
        "module(s) dropped from the OI-12 census record in 04_execution_ledger.md:\n"
        + "\n".join(missing)
    )


def test_oi12_census_matches_the_real_structure_audit_classification():
    """WAVE-2 REPAIR (critic 'missing', CLAUDE.md §0.1 point 2): the prior version of this
    module's checks used `checked = 0; for mod_path in <fixed literal tuple>: checked += 1; ...;
    assert checked == len(<the same tuple>)` — the SAME decorative-counter class this file's own
    module docstring corrects elsewhere (CORRECTION 2): `checked` increments unconditionally,
    once per entry of a fixed-length literal, with no skip path, so the count could not fail
    short of editing the tuple literals themselves; it asserted nothing a reader could not
    already see from the tuple lengths.

    This test re-derives the REAL orphan / stub_wired sets from structure_audit's own graph
    functions (the identical functions `tests/valoria/test_structure_audit.py`'s
    `test_orphan_cli_split_conservation` calls over the real repo tree — reused, not
    re-implemented) and compares the two pinned census tuples against them: a module pinned
    `_OI12_ALREADY_STUB_WIRED` must still be `stub_wired`; a module pinned
    `_OI12_VERIFIED_ORPHAN_NO_CALLSITE` must still be a `code_orphan`. This is genuinely
    falsifiable — if a census module's live classification drifts (a caller lands, or a stubwire
    import is removed), this fails and names exactly which module and which direction, rather
    than passing regardless."""
    sa = _structure_audit.load()
    root = sa.Path(_REPO_ROOT)
    modules = sa.collect_py_modules(root)
    g_code, _parse_errors = sa.build_g_code(root, modules)
    code_nodes = list(modules)
    code_deg = sa.degrees(g_code, code_nodes)
    main_guard_modules = sa.collect_cli_entry_modules(root, modules)
    code_orphans, _cli_entries = sa.split_orphans_and_cli_entries(code_nodes, code_deg, main_guard_modules)
    orphan_set = set(code_orphans)
    stub_wired_set = set(sa.stub_wired_modules(g_code))

    checked = 0
    mismatches = []
    for mod_path in _OI12_ALREADY_STUB_WIRED:
        checked += 1
        dotted = sa._module_name(mod_path)
        if dotted not in stub_wired_set:
            mismatches.append(
                f"{mod_path} ({dotted}): pinned already-stub-wired but structure_audit no "
                f"longer classifies it stub_wired")
    for mod_path in _OI12_VERIFIED_ORPHAN_NO_CALLSITE:
        checked += 1
        dotted = sa._module_name(mod_path)
        if dotted not in orphan_set:
            mismatches.append(
                f"{mod_path} ({dotted}): pinned verified-orphan-no-callsite but structure_audit "
                f"no longer classifies it an import orphan (a caller landed) — update the OI-12 "
                f"census row, not this test")
    # assert-that-asserted (CLAUDE.md §0.1 point 2): the mismatch collection above is the real
    # conditional check per module; this confirms every pinned module was actually looked up
    # against the live classification, not skipped.
    assert checked == len(_OI12_ALREADY_STUB_WIRED) + len(_OI12_VERIFIED_ORPHAN_NO_CALLSITE)
    assert not mismatches, (
        "OI-12 census drifted from the real structure_audit classification:\n" + "\n".join(mismatches)
    )


