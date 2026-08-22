"""The campaign's opening position: that it is AUTHORED, that it is VALIDATED, and that moving it
out of `engine/autoload/game_state.py` changed none of it (plan S5b, 2026-08-22).

SUBJECT, under `CLAUDE.md` §0.1 pt 5: `references/world_initial_state.yaml` is a runtime input —
`engine/substrate/world_initial_state.py` reads its cooked artifact AT IMPORT, and `game_state.py`
imports that leaf at module load. Delete the artifact and the engine does not start. This is the
game, and the same distinction that kept `engine/engine_params/*.json` tracked through culling
wave 5 while the rest of the generated layer was untracked.

TWO CLAIMS, AND THEY FAIL DIFFERENTLY ON PURPOSE:

  1. The VALUES did not move. S5b is a relocation, and the seeded campaign goldens are its control
     — but a golden only says "something moved", never "T4 changed hands". These pin the opening
     position itself, so a transcription error names the territory it broke.
  2. The exporter's validations can each OBSERVE the defect they exclude (§0.1 pt 2). An export-time
     check that cannot fail is not a check, and this exporter's whole justification for being
     blocking is that a bad table reds CI rather than producing a silently wrong world.
"""
from __future__ import annotations

import importlib.util
import json
import pathlib
import shutil

import pytest

REPO = pathlib.Path(__file__).resolve().parents[2]


def _exporter(monkeypatch=None):
    spec = importlib.util.spec_from_file_location(
        'export_world_initial_state', REPO / 'tools' / 'export_world_initial_state.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ── 1. The values did not move ────────────────────────────────────────────────────────────────

def test_the_opening_position_is_exactly_what_the_goldens_were_recorded_under():
    """The literals these tables replaced, transcribed here ONCE from the pre-S5b source so this
    file is an independent witness rather than a second read of the same data. If a future edit is
    a deliberate change to the opening position, this test is where it gets acknowledged — and the
    seeded goldens will move in the same commit."""
    from engine.substrate import world_initial_state as w

    assert w.STARTING_OWNER == {
        'T1': 'Crown', 'T2': 'Crown', 'T3': 'Crown', 'T4': 'Varfell',
        'T5': 'Crown', 'T6': 'Crown', 'T7': 'Hafenmark', 'T8': 'Hafenmark',
        'T9': 'Church', 'T10': 'Hafenmark', 'T11': 'Varfell', 'T12': 'Varfell',
        'T13': 'Varfell', 'T14': 'Crown', 'T15': None, 'T17': 'Hafenmark',
    }
    assert w.STARTING_ACCORD == {
        'T1': 3, 'T2': 3, 'T3': 3, 'T4': 2, 'T5': 2, 'T6': 2, 'T7': 2, 'T8': 3,
        'T9': 4, 'T10': 2, 'T11': 2, 'T12': 2, 'T13': 1, 'T14': 3, 'T15': 0, 'T17': 2,
    }
    assert w.STARTING_PT == {
        'T1': 3, 'T2': 3, 'T3': 3, 'T4': 2, 'T5': 3, 'T6': 1, 'T7': 3, 'T8': 3,
        'T9': 5, 'T10': 3, 'T11': 2, 'T12': 2, 'T13': 1, 'T14': 3, 'T15': 3, 'T17': 3,
    }
    assert w.STARTING_GARRISON == {'T1': True, 'T8': True, 'T9': True, 'T12': True}
    assert w.STARTING_STATS == {
        'Crown':     {'L': 5.0, 'Sta': 4.0, 'W': 4.0, 'I': 5.0, 'Mil': 4.0},
        'Church':    {'L': 5.0, 'Sta': 5.0, 'W': 5.0, 'I': 6.0, 'Mil': 4.0},
        'Hafenmark': {'L': 4.0, 'Sta': 4.0, 'W': 5.0, 'I': 4.0, 'Mil': 3.0},
        'Varfell':   {'L': 4.0, 'Sta': 4.0, 'W': 4.0, 'I': 4.0, 'Mil': 4.0},
    }
    assert w.ALL_PLAYABLE == frozenset({
        'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10',
        'T11', 'T12', 'T13', 'T14', 'T17'})


def test_game_state_still_exposes_the_names_the_corpus_cites():
    """The literals moved; the vocabulary did not. `STARTING_OWNER` and friends are cited by name
    across flow skeletons, design docs and tests, so `game_state` re-exports them. If a rename is
    ever wanted, it is its own change with its own citation sweep."""
    from engine.autoload import game_state as gs
    from engine.substrate import world_initial_state as w

    assert gs.STARTING_OWNER is w.STARTING_OWNER
    assert gs.STARTING_ACCORD is w.STARTING_ACCORD
    assert gs.STARTING_PT is w.STARTING_PT
    assert gs.STARTING_GARRISON is w.STARTING_GARRISON
    assert gs.STARTING_STATS is w.STARTING_STATS
    assert gs.ALL_PLAYABLE_15 is w.ALL_PLAYABLE


def test_the_engine_no_longer_carries_the_opening_position_as_literals():
    """The point of the step, asserted rather than assumed. A future session restoring one of these
    tables into `game_state.py` — as a 'quick fix', or by resolving a merge the lazy way — puts the
    world back in the engine and gives the authored file a silent second owner."""
    src = (REPO / 'engine' / 'autoload' / 'game_state.py').read_text(encoding='utf-8')
    for needle, name in (("'T1': 'Crown'", 'STARTING_OWNER'),
                         ("'Crown':     {", 'STARTING_STATS'),
                         ("'T1': True", 'STARTING_GARRISON')):
        assert needle not in src, (
            f'{name} looks like it is a literal in game_state.py again. It is authored in '
            f'references/world_initial_state.yaml — edit that, and re-run '
            f'tools/export_world_initial_state.py.'
        )


def test_mults_is_still_a_literal_and_still_says_why():
    """The ONE table S5b deliberately did not move, pinned so the reason survives the session that
    wrote it. `MULTS` belongs in `descriptor_registry.yaml`, but authoring `L` as a faction-stat row
    there would answer Q1 — the open Jordan ruling on whether Legitimacy is a base descriptor or
    derived like Mandate. When Q1 is ruled, this test is the work-list entry: delete it, move MULTS,
    and the ruling is recorded by the move."""
    src = (REPO / 'engine' / 'autoload' / 'game_state.py').read_text(encoding='utf-8')
    assert "MULTS = {'L': 20" in src, 'MULTS moved — if Q1 was ruled, say so here and delete this test'
    assert 'Q1' in src, (
        'the MULTS literal lost the note explaining why it is still a literal. Without it the next '
        'session reads an unexplained holdout and either moves it (pre-empting a Jordan ruling) or '
        'leaves it forever.'
    )


# ── 2. Every export-time validation can observe its own failure ───────────────────────────────

def _authored(tmp_path):
    """A working copy of the real authored file, and an exporter pointed at it."""
    src = tmp_path / 'world_initial_state.yaml'
    shutil.copy(REPO / 'references' / 'world_initial_state.yaml', src)
    mod = _exporter()
    mod.SRC = str(src)
    return mod, src


def _mutate(path, old, new):
    text = path.read_text(encoding='utf-8')
    assert old in text, f'fixture assumption broken: {old!r} not in the authored file'
    path.write_text(text.replace(old, new, 1), encoding='utf-8')


def test_the_unmutated_copy_exports_cleanly(tmp_path):
    """The control. Without it, every rejection below could be the fixture failing rather than the
    check firing — which is the §0.1 pt 2 defect one level up."""
    mod, _ = _authored(tmp_path)
    assert mod.build()['territories'], 'the unmutated authored file must export'


@pytest.mark.parametrize('old,new,expected', [
    # An owner nobody declares — the shape of a faction rename applied to one table and not the other.
    ("owner: \"Varfell\", accord: 2, pt: 2, garrison: false, playable: true}",
     "owner: \"Varfelll\", accord: 2, pt: 2, garrison: false, playable: true}",
     'faction_starting_stats does not declare'),
    # An Accord outside the 0-4 canon buckets — ACCORD_MAP has no key for it.
    ("accord: 4, pt: 5", "accord: 9, pt: 5", 'outside the canonical 0-4'),
    # A PT outside the 0-5 canon buckets.
    ("accord: 4, pt: 5", "accord: 4, pt: 8", 'outside the canonical 0-5'),
    # A dropped column: the value would silently default and move the opening position.
    ("{owner: \"Church\", accord: 4, pt: 5, garrison: true, playable: true}",
     "{owner: \"Church\", accord: 4, pt: 5, playable: true}",
     "missing 'garrison'"),
    # A non-boolean flag — YAML makes this easy to do by accident.
    ("garrison: true, playable: true}", "garrison: yes-please, playable: true}",
     'must be booleans'),
])
def test_a_broken_table_is_rejected_at_export_time(tmp_path, old, new, expected):
    """Each of these produces a WORKING but WRONG world if it reaches runtime. The exporter is
    blocking precisely so they cannot."""
    mod, src = _authored(tmp_path)
    _mutate(src, old, new)
    with pytest.raises(SystemExit) as exc:
        mod.build()
    assert expected in str(exc.value), f'rejected, but not for the stated reason: {exc.value}'


def test_a_faction_with_no_territory_is_rejected(tmp_path):
    """The likeliest real corruption of this file is a deleted or mistyped territory row, and the
    symptom is a faction that starts landless — which the engine would happily run."""
    mod, src = _authored(tmp_path)
    for tid in ('T9',):
        _mutate(src, f'  {tid}: {{owner: "Church"', f'  {tid}: {{owner: null')
    with pytest.raises(SystemExit) as exc:
        mod.build()
    assert 'hold no territory' in str(exc.value)


def test_faction_order_is_preserved_because_it_drives_the_rng():
    """THE TRAP THIS STEP FELL INTO, PINNED SO THE NEXT SESSION DOES NOT.

    `create_world` iterates `faction_starting_stats` to build `world.factions`, so this table's
    order becomes that dict's order, becomes the order of every `world.factions.items()` loop, and
    becomes the RNG draw sequence of a seeded campaign. The first draft of the exporter sorted
    factions alphabetically — the most unremarkable "for determinism" habit there is — and moved
    the campaign goldens (Church win-share 0.0 -> 50.0) without altering one value.

    Two assertions, because they fail for different reasons: the exporter must REJECT a reordering
    (so it cannot happen silently), and the order the engine actually ends up with must be the
    authored one (so the rejection is guarding the right thing).
    """
    from engine.substrate import world_initial_state as w
    from engine.autoload import game_state as gs

    assert list(w.STARTING_STATS) == ['Crown', 'Church', 'Hafenmark', 'Varfell']
    assert list(gs.create_world(seed=42).factions) == ['Crown', 'Church', 'Hafenmark', 'Varfell'], (
        'world.factions is no longer in authored order. Every seeded golden in engine/tests is '
        'recorded against this sequence.'
    )


def test_a_reordered_faction_table_is_rejected_at_export_time(tmp_path):
    """§0.1 pt 2 for the check above: it must be able to observe the reordering it excludes."""
    mod, src = _authored(tmp_path)
    text = src.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)
    crown = next(i for i, ln in enumerate(lines) if ln.startswith('  Crown:'))
    church = next(i for i, ln in enumerate(lines) if ln.startswith('  Church:'))
    lines[crown], lines[church] = lines[church], lines[crown]
    src.write_text(''.join(lines), encoding='utf-8')

    with pytest.raises(SystemExit) as exc:
        mod.build()
    assert 'MOVES THE GOLDENS' in str(exc.value)


def test_the_committed_artifact_matches_the_authored_source():
    """`--check` in CI proves this too, but only in CI. Running it here means a session that edits
    the YAML and forgets to re-export finds out from the suite it already runs."""
    mod = _exporter()
    assert json.loads(json.dumps(mod.build())) == json.loads(
        (REPO / 'engine' / 'engine_params' / 'world_initial_state.json').read_text(encoding='utf-8')
    ), 'artifact is stale — run: python3 tools/export_world_initial_state.py'
