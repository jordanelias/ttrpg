"""`engine/mc_v18.py` is SUPERSEDED and its importer set may only SHRINK.

THE RULING. Jordan, 2026-09-07: *"#371 EXISTS. `engine/season/` IS THE HEAD. THE DECOMPOSITION WAS
DONE ON THE PROTOTYPE."* `ED-IN-0204` adopted the season loop in full. Jordan again, 2026-09-13:
*"Make engine/season/ the head ... Retire mc_v18"*, then — decisively for what this file does —
*"We don't have to delete mc_v18 — we just deprecate it and archive it."*

WHY A RATCHET AND NOT A DELETION. Deleting the module was measured and refused on its cost, not
its difficulty: **78 of the 136 test functions in `engine/tests/` — 57% of CI's blocking
`sim-regression` job — import it**, covering echo transport, the combat bridge seam, parliamentary
transfer, accord drift and pipeline reach. Deleting first would not retire a prototype; it would
delete 78 tests of campaign-scale behaviour. Deprecation in place keeps every one of them running.

⚠ AND `CLAUDE.md` §1 FORBIDS THE OBVIOUS ALTERNATIVE: *"There is no `deprecated/` tree ... Do not
recreate the directory."* So "archive" here cannot mean moving the file, and moving it would break
sixteen importers to no benefit. It is deprecated WHERE IT SITS, and this test is what makes that
more than a docstring.

WHAT THIS GUARD IS FOR, and why it earns its existence under `CLAUDE.md` §0.1 pt 5. The predicate
there asks whether the defective artifact is load-bearing on THE GAME or on A JORDAN DECISION.
Both, and it is not hypothetical: `tools/m1_acceptance.py` — the one instrument §0.2 accepts for
*"does the milestone run"* — probed this superseded module for six days, so the milestone gate
reported NOT-MET on the strength of deferrals inside code nobody intends to ship (`ED-IN-0226`).
The failure mode is a session building on the prototype because nothing stopped it. This stops it.

⚠ SHRINK-ONLY, THE SAME DISCIPLINE `PATH_SEAM_ALLOWED` USES. A new importer FAILS. A removed one
fails too, loudly, and is meant to — the fix is to delete its line here, which makes every step of
the migration a visible diff rather than a silent drift.

⚠ WHAT THIS DOES **NOT** ASSERT, said plainly so the roster is not misread as a to-do list: it does
not claim the sixteen should be ported, nor that porting them is scheduled. Deprecation means
nothing NEW builds here. Whether the existing sixteen ever move is a separate decision nobody has
taken.
"""
import ast
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# The importer set MEASURED 2026-09-13, by the AST scan below rather than by grep — a docstring
# mentioning `mc_v18` is not an import, and the 71-file grep count that first framed this work
# was overwhelmingly mentions. Sixteen modules actually import it.
#
# ⚠ NOT ONE OF THEM IS PRODUCTION CODE. No module under `engine/` outside its own tests, nothing
# under `systems/`, and nothing in the composition spine: `composition.json` and
# `module_contracts.yaml` name `mc_v18` only in `needed_by:` DOCUMENTATION fields, which say who
# consumes a role, not what a role resolves to. The prototype is a consumer of the engine, never a
# dependency of it — which is why deprecating it in place costs nothing at runtime.
ALLOWED_IMPORTERS = {
    # engine/tests — CI job `sim-regression`. 78 test functions; the coverage the deletion would
    # have cost, and the reason this is a ratchet.
    'engine/tests/test_accounting_accord_drift_probe.py',
    'engine/tests/test_combat_bridge_seam.py',
    'engine/tests/test_f7_smoke_oracle.py',
    'engine/tests/test_mc_v18_regression.py',
    'engine/tests/test_pipeline_reach.py',
    'engine/tests/test_world_population.py',
    # tools
    'tools/balance_oracle.py',
    'tools/campaign_output_probe.py',
    'tools/trace_execution_phases.py',
    # ─────────────────────────────────────────────────────────────────────────────────────────
    # SIX LINES DELETED 2026-09-16 (ED-IN-0232), which is the visible migration record the
    # assertion below demands rather than a quiet trim. None of the six was PORTED off mc_v18 —
    # all six RETIRED with the Key substrate under Jordan's ruling *"anything key-based gets
    # retired"*, so the roster shrank for a reason that is not progress toward the port:
    #   engine/tests/test_echo_transport.py          - the bus's own oracle
    #   engine/tests/test_parliamentary_bridge.py    - the bus-gated §10 vote
    #   tests/valoria/test_contract_runtime_conformance.py - instrumented the bus
    #   tests/valoria/test_public_governance_transfer_key.py - a log-only emitter's test
    #   tools/contract_runtime_conformance.py        - the instrument itself
    # and `tests/valoria/test_engine_clock_phases.py`, which SURVIVES as a file but stopped
    # importing mc_v18: its four scheduler-phase cases went with the substrate and the ordering
    # cases it kept build a world directly.
    #
    # A SEVENTH LINE WENT ON THE SECOND PASS: `tests/valoria/_campaign.py`, the seeded-campaign
    # helper. All three of ITS callers were among the retired modules, so it became a module with
    # no importers whose docstring justified keeping two inert parameters "because three callers
    # unpack three values" — a reason that stopped being true in the same commit that wrote it. An
    # adversarial pass caught it; the file is deleted, not kept as a convenience nobody uses.
    #
    # ROSTER 16 -> 9, counted from this tuple rather than from arithmetic; the AST scan below finds
    # the same 9. None of the three non-test importers that remain (`balance_oracle`,
    # `campaign_output_probe`, `trace_execution_phases`) is shipped engine code — they are tools.
    # ─────────────────────────────────────────────────────────────────────────────────────────
}


def _imports_mc_v18(path):
    """AST, not a substring. `from engine import mc_v18`, `import engine.mc_v18` and
    `from engine.mc_v18 import x` all count; a docstring naming it does not."""
    try:
        tree = ast.parse(open(path, encoding='utf-8', errors='ignore').read())
    except (SyntaxError, UnicodeDecodeError):
        return False
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom):
            if n.module and 'mc_v18' in n.module:
                return True
            if n.module == 'engine' and any(a.name == 'mc_v18' for a in n.names):
                return True
        elif isinstance(n, ast.Import):
            if any('mc_v18' in a.name for a in n.names):
                return True
    return False


_SCANNED = None


def _scan():
    """EVERY `.py` IN THE TREE, AST-PARSED -- ONCE PER PROCESS, NOT ONCE PER TEST.

    ⚠ MEMOISED BECAUSE THREE TESTS BELOW ASK THE SAME QUESTION and this is a whole-repository walk
    that parses every Python file in it. Unmemoised it ran three times on the blocking shipping
    gate for one answer that cannot change between them -- the tests do not write, and a scan is a
    pure function of the tree. `CLAUDE.md` §0.4 is about not paying for a verdict twice; this is
    the same arithmetic inside one file."""
    global _SCANNED
    if _SCANNED is not None:
        return _SCANNED
    found = set()
    for base, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__', 'node_modules'}]
        for f in files:
            if not f.endswith('.py'):
                continue
            full = os.path.join(base, f)
            rel = os.path.relpath(full, REPO_ROOT).replace(os.sep, '/')
            if rel == 'engine/mc_v18.py':
                continue
            if _imports_mc_v18(full):
                found.add(rel)
    _SCANNED = found
    return found


def test_no_new_module_imports_the_superseded_campaign_driver():
    """THE RATCHET. A new importer is a session building on a tree the repo replaced."""
    found = _scan()
    added = found - ALLOWED_IMPORTERS
    assert not added, (
        f'{len(added)} NEW importer(s) of the superseded engine/mc_v18.py: {sorted(added)}.\n'
        'engine/season/ is the head (Jordan, 2026-09-07; ED-IN-0204 adopted the season loop in '
        'full) and mc_v18 is deprecated in place (ED-IN-0227). Build against the head. If you are '
        'porting coverage OFF mc_v18 you are removing lines from ALLOWED_IMPORTERS, never adding '
        'them — see this file\'s docstring for why the module was deprecated rather than deleted.'
    )


def test_the_importer_roster_has_not_gone_stale():
    """The other half, and it fails LOUDLY on purpose.

    A roster that lists modules which no longer import the thing is the declared-but-unread defect
    one register over: it reads as a live dependency set while overstating it, and every future
    reader then plans against a surface that is already smaller than the file says. Removing a line
    is the deliverable of a port, so it should show up as a diff here."""
    found = _scan()
    gone = ALLOWED_IMPORTERS - found
    assert not gone, (
        f'{len(gone)} roster entr(y/ies) no longer import mc_v18: {sorted(gone)}. '
        'If you ported them off, DELETE those lines from ALLOWED_IMPORTERS in this file — that '
        'deletion is the visible record of the migration step.'
    )


def test_production_code_does_not_import_it_at_all():
    """THE PROPERTY THAT MAKES DEPRECATION-IN-PLACE SAFE, asserted rather than assumed.

    Sixteen importers sounds like entanglement. It is not: every one is a test or a tool. If a
    module under `engine/` (outside its own tests) or under `systems/` ever imports the prototype,
    the campaign driver has become a runtime dependency of the head, and deprecating it in place
    stops being free."""
    prod = {p for p in _scan()
            if (p.startswith('engine/') and not p.startswith('engine/tests/'))
            or p.startswith('systems/')}
    assert not prod, (
        f'production code imports the superseded campaign driver: {sorted(prod)}. '
        'engine/season/ is the head; the prototype must remain a consumer of the engine, never a '
        'dependency of it'
    )
