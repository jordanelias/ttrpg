"""The measured duel table is cooked into `engine/engine_params/mb_contact.json` and `systems/mass_battle/sim/contact_table_data.py`
behind a blocking round trip, and a stale calibration, a missing cell and a hand edit each red it (B19a.03, MBA-03).

Each test can observe the failure it excludes (CLAUDE.md §0.1 pt 3): the check is run on a copy of the heads and artifacts under
`tmp_path` (the exporter's path constants are patched), the untouched copy is green, and the mutated copy is red for the named reason.
The committed pair is read at its real paths (`test_round_trip_is_clean`, `test_interpolation_hits_the_check_cells`).
"""
import json
import os
import shutil
import sys
from pathlib import Path

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, ROOT)

import calibrate_mb_contact as cmc  # noqa: E402
import export_mb_contact as ex  # noqa: E402
from systems.mass_battle.sim import contact_table  # noqa: E402


@pytest.fixture
def heads(tmp_path, monkeypatch):
    """A copy of the two heads and the two artifacts, the exporter pointed at it."""
    copies = {}
    for name, src in (('TROOPS', ex.TROOPS), ('TABLE', ex.TABLE), ('OUT', ex.OUT), ('OUT_PY', ex.OUT_PY)):
        dst = tmp_path / Path(src).name
        shutil.copy(src, dst)
        monkeypatch.setattr(ex, name, str(dst))
        copies[name] = dst
    return copies


def test_round_trip_is_clean(capsys):
    """The committed pair is what the heads derive, the two artifacts are one document, and the module reads that document."""
    assert ex.main(['--check']) == 0, capsys.readouterr().out
    doc = json.loads(Path(ex.OUT).read_text(encoding='utf-8'))
    assert doc == contact_table._data()
    assert doc['engine_fingerprint'] == cmc.engine_fingerprint()


def test_a_hand_edit_fails_check(heads, capsys):
    assert ex.main(['--check']) == 0, 'the control: the untouched copy is clean'
    good, good_py = heads['OUT'].read_text(encoding='utf-8'), heads['OUT_PY'].read_text(encoding='utf-8')
    doc = json.loads(good)
    key = next(iter(doc['pairs']))
    doc['pairs'][key]['h'][0] = round(doc['pairs'][key]['h'][0] + 0.01, 4)
    heads['OUT'].write_text(ex.render(doc), encoding='utf-8')
    assert ex.main(['--check']) == 1
    out = capsys.readouterr().out
    assert 'DRIFT' in out and 'mb_contact.json' in out
    heads['OUT'].write_text(good, encoding='utf-8')
    assert ex.main(['--check']) == 0
    heads['OUT_PY'].write_text(good_py.replace("'K': 6", "'K': 7", 1), encoding='utf-8')      # the literal is pinned too
    assert ex.main(['--check']) == 1
    assert 'contact_table_data.py' in capsys.readouterr().out


def test_a_changed_duel_engine_fails_check(heads, tmp_path, monkeypatch, capsys):
    """One byte in a copy of each fingerprinted source group: the control is the unplanted copy, whose fingerprint is the tree's."""
    tree = tmp_path / 'tree'
    (tree / 'engine' / 'engine_params').mkdir(parents=True)
    (tree / 'engine' / 'season' / 'queries').mkdir(parents=True)
    shutil.copy(cmc.PARAMS, tree / 'engine' / 'engine_params' / 'combat_engine_v1.json')
    shutil.copy(cmc.INPUTS, tree / 'engine' / 'season' / 'queries' / 'inputs.py')
    for name, src, dst in (('COMBAT_DIR', cmc.COMBAT_DIR, tree / 'modules' / 'combat'), ('DICE_DIR', cmc.DICE_DIR, tree / 'engine' / 'dice_engine')):
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns('__pycache__'))
        monkeypatch.setattr(cmc, name, str(dst))
    monkeypatch.setattr(cmc, 'REPO', str(tree))
    monkeypatch.setattr(cmc, 'PARAMS', str(tree / 'engine' / 'engine_params' / 'combat_engine_v1.json'))
    monkeypatch.setattr(cmc, 'INPUTS', str(tree / 'engine' / 'season' / 'queries' / 'inputs.py'))
    assert ex.main(['--check']) == 0, capsys.readouterr().out
    for target in (sorted((tree / 'modules' / 'combat').glob('*.py'))[0], sorted((tree / 'engine' / 'dice_engine').glob('*.py'))[0],
                   tree / 'engine' / 'season' / 'queries' / 'inputs.py'):
        original = target.read_bytes()
        target.write_bytes(original + b'#')
        assert ex.main(['--check']) == 1, target
        out = capsys.readouterr().out
        assert 'STALE CALIBRATION' in out and ex.REMEDY in out and 'CHUNKING THE GRID' in out
        target.write_bytes(original)


def test_interpolation_hits_the_check_cells():
    """MBA §2.5: the module's log-odds interpolation between skill 1, 3 and 5, read at the twelve check cells (skill 2 and 4 against 3,
    each arm, light armour; two mirrors), lands inside each measured `h_1` interval for all but at most one cell. A cell is outside
    when either of its sides is. If more than one is outside, skill 2 and 4 join the grid and the close says so."""
    table = json.loads(Path(ex.TABLE).read_text(encoding='utf-8'))
    check, outside = 0, []
    for c in table['cells']:
        if not {c['a']['skill'], c['b']['skill']} & set(cmc.CHECK_SKILLS):
            continue
        check += 1
        for side, other in (('a', 'b'), ('b', 'a')):
            d, a = c[side], c[other]
            h = contact_table.felling_chance(a['arm'], d['armour'], a['skill'], d['skill'], 1, arm_d=d['arm'], armour_a=a['armour'])
            row = c['sides'][side]
            if not row['h_lo'][0] <= h <= row['h_hi'][0]:
                outside.append((c['a'], c['b'], side, h, row['h_lo'][0], row['h_hi'][0]))
                break
    assert check == 12, f'{check} check cells read'
    assert len({(json.dumps(o[0]), json.dumps(o[1])) for o in outside}) <= 1, outside
