"""The campaign's opening position: that it is AUTHORED, that it is VALIDATED, and that moving it
out of `engine/autoload/game_state.py` changed none of it (plan S5b, 2026-08-22; `game_state.py` itself was
deleted at plan position `29b`, and the three tests that read it went with it).

SUBJECT, under `CLAUDE.md` §0.1 pt 5: `references/world_initial_state.yaml` is a runtime input —
`engine/substrate/world_initial_state.py` reads its cooked artifact AT IMPORT. Delete the artifact and
every reader of the leaf fails to import. This is the game, and the same distinction that kept
`engine/engine_params/*.json` tracked through culling wave 5 while the rest of the generated layer
was untracked.

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
    # The two columns added at S5b's adversarial pass, transcribed from the inline expressions they
    # replaced: `prosperity=2 if tid in {T1,T2,T3,T8,T9,T14} else 1` and `templar=(tid == 'T9')`.
    assert {t for t, v in w.STARTING_PROSPERITY.items() if v == 2} == {
        'T1', 'T2', 'T3', 'T8', 'T9', 'T14'}
    assert set(w.STARTING_PROSPERITY.values()) == {1, 2}
    assert {t for t, v in w.STARTING_TEMPLAR.items() if v} == {'T9'}


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
    ('owner: "Varfell", accord: 2, pt: 2', 'owner: "Varfelll", accord: 2, pt: 2',
     'faction_starting_stats does not declare'),
    # An Accord outside the 0-4 canon buckets — ACCORD_MAP has no key for it.
    ("accord: 4, pt: 5", "accord: 9, pt: 5", 'outside the canonical 0-4'),
    # A PT outside the 0-5 canon buckets.
    ("accord: 4, pt: 5", "accord: 4, pt: 8", 'outside the canonical 0-5'),
    # A dropped column: the value would silently default and move the opening position.
    ('{owner: "Church", accord: 4, pt: 5, garrison: true,', '{owner: "Church", accord: 4, pt: 5,',
     "missing 'garrison'"),
    # A non-boolean flag — YAML makes this easy to do by accident.
    ('garrison: true, playable: true, prosperity: 2, templar: true}',
     'garrison: yes-please, playable: true, prosperity: 2, templar: true}',
     'must be booleans'),
    # A prosperity value the opening table never declares — added with the column at S5b's
    # adversarial pass, since Territory.prosperity has no declared scale anywhere in the corpus.
    ('prosperity: 2, templar: true}', 'prosperity: 9, templar: true}', 'only ever declares 1 or 2'),
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

    The authored `faction_starting_stats` order is the order of every loop that iterates the leaf's
    `STARTING_STATS`. It used to become `game_state.create_world`'s `world.factions` order, and so the
    RNG draw sequence of a seeded campaign: the first draft of the exporter sorted factions
    alphabetically — the most unremarkable "for determinism" habit there is — and moved the campaign
    goldens (Church win-share 0.0 -> 50.0) without altering one value.

    `create_world` and `game_state.py` were deleted at plan position `29b`, and the campaign goldens
    went at `28-iii`, so the second assertion this test carried (the order the engine ended up with)
    went with them. What survives is the authored order itself, which the exporter's own rejection
    test below still guards; any reader that iterates `STARTING_STATS` still sees this sequence.
    """
    from engine.substrate import world_initial_state as w

    assert list(w.STARTING_STATS) == ['Crown', 'Church', 'Hafenmark', 'Varfell']


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


@pytest.mark.parametrize('old,new,expected', [
    # An emptied block — the shape of a bad merge resolution, not a typo.
    ('faction_starting_stats:', 'faction_starting_stats_DISABLED:', 'no faction_starting_stats'),
    # A dropped stat on one faction. Faction(**stats) would raise, but only when a world is built.
    ('Crown: {L: 5.0, Sta: 4.0, W: 4.0, I: 5.0, Mil: 4.0}',
     'Crown: {L: 5.0, Sta: 4.0, W: 4.0, I: 5.0}', "missing starting stat 'Mil'"),
    # A stat that is not numeric — trivially easy in YAML, and it survives to a TypeError deep in
    # the first roll rather than at world-gen.
    ('Church: {L: 5.0', 'Church: {L: five', 'is not numeric'),
])
def test_a_broken_faction_stats_block_is_rejected_at_export_time(tmp_path, old, new, expected):
    """Added 2026-08-22 after an adversarial pass observed that the territory columns had
    falsifiers and the faction-stats block had none — so "each check can observe the defect it
    excludes" was true of half the exporter."""
    mod, src = _authored(tmp_path)
    _mutate(src, old, new)
    with pytest.raises(SystemExit) as exc:
        mod.build()
    assert expected in str(exc.value), f'rejected, but not for the stated reason: {exc.value}'


def test_an_empty_territory_block_is_rejected(tmp_path):
    """The remaining unfalsified `_fail` path: a campaign with no map."""
    mod, src = _authored(tmp_path)
    _mutate(src, 'territories:', 'territories_DISABLED:')
    with pytest.raises(SystemExit) as exc:
        mod.build()
    assert 'no territories declared' in str(exc.value)


def test_the_committed_artifact_matches_the_authored_source():
    """`--check` in CI proves this too, but only in CI. Running it here means a session that edits
    the YAML and forgets to re-export finds out from the suite it already runs."""
    mod = _exporter()
    # TEXT, not parsed dicts. Dict equality ignores key ORDER, and this file's whole argument is
    # that faction order sets the RNG draw sequence — so the parsed comparison this test used until
    # 2026-08-22 would have passed on an alphabetized artifact, the exact defect two tests above
    # exist to catch. `--check` compares text; so does this.
    fresh = json.dumps(mod.build(), indent=2, sort_keys=False) + '\n'
    committed = (REPO / 'engine' / 'engine_params' / 'world_initial_state.json').read_text(
        encoding='utf-8')
    assert fresh == committed, 'artifact is stale — run: python3 tools/export_world_initial_state.py'
