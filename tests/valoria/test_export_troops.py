"""The troop file (`references/troops.yaml`) is exported to `engine/engine_params/troops.json` behind a blocking round trip,
and the loader (`modules/mass_battle/troop_types/table.py`) refuses what it must refuse, by name (B17.10).

Each test can observe the failure it excludes (CLAUDE.md §0.1 pt 3): a hand-edited artifact reds `--check` and its control
(the untouched copy) is green; each refusal is shown against a one-key mutation of the real file, which loads clean
beforehand, so the red is that key. The transcription test compares the arms' classes with the reach the tree keeps per
troop type today, so the claim "reach derives from the arm with no result moving" (B17.11) is read, not assumed.
"""
import copy
import json
import os
import sys
from pathlib import Path

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, ROOT)

import export_troops as et  # noqa: E402
from modules.mass_battle.troop_types import registry, table  # noqa: E402


def _artifact():
    return json.loads(Path(et.OUT).read_text(encoding='utf-8'))


def test_round_trip(tmp_path, monkeypatch):
    assert et.main(['--check']) == 0
    # a hand edit of the artifact reds the check; the untouched copy, same logic, is green (the control)
    art = _artifact()
    intact = tmp_path / 'intact.json'
    intact.write_text(json.dumps(art, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    art['troops']['pike']['power'] += 1
    edited = tmp_path / 'edited.json'
    edited.write_text(json.dumps(art, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    monkeypatch.setattr(et, 'OUT', str(edited))
    assert et.main(['--check']) == 1
    monkeypatch.setattr(et, 'OUT', str(intact))
    assert et.main(['--check']) == 0


def test_the_module_reads_the_document_the_port_reads(tmp_path, monkeypatch):
    """The module's literal (a registered module opens no file, A-25) and the port's JSON are one document; a stale literal
    reds `--check` and its control, the untouched copy, is green."""
    from modules.mass_battle.troop_types import troops_data
    assert troops_data.DATA == _artifact() == table._data()
    stale = tmp_path / 'troops_data.py'
    stale.write_text(Path(et.OUT_PY).read_text(encoding='utf-8').replace("'power': 4,", "'power': 9,", 1), encoding='utf-8')
    monkeypatch.setattr(et, 'OUT_PY', str(stale))
    assert et.main(['--check']) == 1
    stale.write_text(Path(table.__file__).with_name('troops_data.py').read_text(encoding='utf-8'), encoding='utf-8')
    assert et.main(['--check']) == 0


def test_the_loaded_file_checks_clean():
    data = _artifact()
    table.check(data)                       # the control for every refusal below: the real file is accepted
    assert data['troops'] and data['arms']


def test_unknown_arm_key_refused_by_name():
    data = _artifact()
    for column in ('primary', 'secondary'):
        bad = copy.deepcopy(data)
        bad['troops']['pike'][column] = 'warhammer'
        with pytest.raises(table.TroopFileError) as e:
            table.check(bad)
        assert 'troops.pike' in str(e.value) and 'warhammer' in str(e.value), column


def test_mass_stated_twice_refused():
    data = _artifact()
    assert 'mass_kg' not in data['arms']['spear'], 'the control: spear is in personal combat\'s roster and states no mass here'
    bad = copy.deepcopy(data)
    bad['arms']['spear']['mass_kg'] = 1.0
    with pytest.raises(table.TroopFileError) as e:
        table.check(bad)
    assert 'arms.spear' in str(e.value) and 'twice' in str(e.value)


def test_the_other_refusals_are_named():
    data = _artifact()
    cases = [
        ('an unknown troop column', lambda d: d['troops']['pike'].update(reach=0.3), 'reach'),
        ('a missing troop column', lambda d: d['troops']['pike'].pop('upkeep'), 'upkeep'),
        ('an unknown arm column', lambda d: d['arms']['bow'].update(weight=1), 'weight'),
        ('an armour tier outside the set', lambda d: d['troops']['pike'].update(armour='mithril'), 'mithril'),
        ('a role outside the set', lambda d: d['troops']['pike'].update(roles=['Charge']), 'Charge'),
        ('a site kind outside the set', lambda d: d['troops']['pike'].update(training_site='forge'), 'forge'),
        ('a secondary equal to the primary', lambda d: d['troops']['pike'].update(secondary='pike'), 'equals the primary'),
        ('an arm of a class that is not one', lambda d: d['arms']['bow'].update(**{'class': 'whip'}), 'whip'),
    ]
    checked = 0
    for what, mutate, needle in cases:
        bad = copy.deepcopy(data)
        mutate(bad)
        with pytest.raises(table.TroopFileError) as e:
            table.check(bad)
        assert needle in str(e.value), what
        checked += 1
    assert checked == len(cases)


def test_a_site_kind_the_season_does_not_have_is_refused(tmp_path, monkeypatch):
    src = Path(et.SRC).read_text(encoding='utf-8').replace('site_kinds: [barracks, archery_range, stable, siege_workshop]',
                                                          'site_kinds: [barracks, archery_range, stable, siege_workshop, forge]')
    assert 'forge' in src
    bad = tmp_path / 'troops.yaml'
    bad.write_text(src, encoding='utf-8')
    monkeypatch.setattr(et, 'SRC', str(bad))
    assert et.main(['--check']) == 1


def test_reach_and_support_derive_from_the_arm_with_no_result_moving():
    """The proposal's claim, read: for every troop row, the class of its primary arm gives the reach and support depth the
    tree kept per type before B17.11 (`TROOP_TYPE_REACH`, deleted there, and `support_ranks_for`); a row with no weapon
    takes the melee default. B17.11 made the loader's read the only owner, so this is the artifact against the reads."""
    data = _artifact()
    checked = 0
    for t, row in data['troops'].items():
        if row['primary'] is None:
            expect_reach = registry.REACH_MELEE_DEFAULT
            expect_ranks = 1
        else:
            cls = data['classes'][data['arms'][row['primary']]['class']]
            expect_reach, expect_ranks = cls['reach'], cls['support_ranks']
        assert registry.reach_for(t) == expect_reach, t
        assert registry.support_ranks_for(t) == expect_ranks, t
        checked += 1
    assert checked == len(data['troops']) >= 15


def test_the_transcribed_rows_read_as_the_old_tables_did():
    """The rows that carry a decision, pinned by value: the knights keep today's behaviour (`mounted: false`, a 100-troop
    cell), the unmustered body has no stat preset and no loadout, a levy has no site, and the two elite sites need half."""
    assert not registry.is_mounted('knights_templar') and registry.is_mounted('light_cavalry')
    assert sorted(registry.MOUNTED_TYPES) == ['cavalry', 'light_cavalry', 'mounted_archers']
    from modules.mass_battle import config
    assert config.cell_cap_for('knights_templar') == 100 == config.cell_cap_for('cavalry')
    assert config.cell_cap_for('pike') == config.CELL_CAP == config.cell_cap_for('infantry') == config.cell_cap_for('zzz')
    assert registry.stats_for('infantry') is None and 'infantry' not in registry.TROOP_TYPE_STATS
    from modules.mass_battle.equipment import loadout_for
    assert loadout_for('infantry') == (None, None) and loadout_for('pike')[0].name == 'pike'
    from modules.mass_battle.troop_types import recruitment
    assert recruitment.training_site_for('levy') is None
    assert recruitment.training_site_for('knights_templar') == ('stable', 0.5) == recruitment.TRAINING_SITE['knights_templar']
    assert registry.roles_for('levy') == ['Support', 'Reserve'] == registry.roles_for('no_such_type')
    assert table.row_of('infantry')['power'] == 4 and table.row_of('infantry')['discipline'] == 5
    assert all(r['secondary'] is None for r in _artifact()['troops'].values())
