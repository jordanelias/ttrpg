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
    art['troops']['pike']['skill'] += 1
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
    stale.write_text(Path(et.OUT_PY).read_text(encoding='utf-8').replace("'skill': 4,", "'skill': 9,", 1), encoding='utf-8')
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


def test_every_arm_has_a_duel_key_or_a_sidearm():
    """B19a.01: an arm is read in the duel through its `duel_key` (a key of personal combat's weapon export) or, a missile arm
    having none, through its `sidearm`. Control: every real arm carries one (counted, so the loop is not vacuous) and the file
    checks clean; each refusal is then one mutation of the real file, named by its row."""
    data = _artifact()
    table.check(data)
    weapons = table.combat_weapon_keys()
    assert len(data['arms']) >= 11
    for name, arm in data['arms'].items():
        assert (arm['duel_key'] or arm.get('sidearm')) in weapons, name
        assert arm['duel_key_status'] in ('exact', 'proxy', 'none'), name
    assert data['arms']['pike']['duel_key'] == 'spear' and data['arms']['bow']['sidearm'] == 'dagger'
    cases = [
        ('neither a duel key nor a sidearm', lambda d: d['arms']['bow'].pop('sidearm'), 'arms.bow'),
        ('a status outside its closed set', lambda d: d['arms']['spear'].update(duel_key_status='roughly'), 'roughly'),
        ('a duel key personal combat has no weapon for', lambda d: d['arms']['spear'].update(duel_key='warhammer'), 'warhammer'),
        ('a sidearm personal combat has no weapon for', lambda d: d['arms']['bow'].update(sidearm='warhammer'), 'warhammer'),
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


def test_an_unstatused_contact_value_is_refused():
    """B19a.01: every value of `contact` (exposure, levels, K, missile) carries a `status`; only `exposure.base` may be null.
    Control: the real file has no value without a status and has a null `base` (so the null rule is observed, not assumed)."""
    data = _artifact()
    table.check(data)
    assert data['contact']['exposure']['base'] == {'value': None, 'status': 'seed'}
    cases = [
        ('a value with no status', lambda d: d['contact']['exposure']['posture_k'].pop('status'), 'contact.exposure.posture_k'),
        ('a bare number', lambda d: d['contact']['levels'].update(intent_offense=0.5), 'contact.levels.intent_offense'),
        ('a nested missile value with no status', lambda d: d['contact']['missile']['hit']['bow']['close'].pop('status'),
         'contact.missile.hit.bow.close'),
        ('a status outside its closed set', lambda d: d['contact']['K'].update(status='guess'), 'guess'),
        ('a null that is not `exposure.base`', lambda d: d['contact']['levels']['intent_defense'].update(value=None),
         'contact.levels.intent_defense'),
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


def test_a_matchup_row_outside_the_closed_sets_is_refused():
    """B19a.01: a matchup row names a class and a situation of the closed sets, a `closes` of its four, a `status` of its
    three. The file ships `matchups: []`, so the control plants one valid row (accepted) and each refusal is that row with one
    key moved out of its set, named by the row."""
    data = _artifact()
    assert data['matchups'] == []
    row = {'a': 'horse_shock', 'd': 'foot_pike', 'situation': 'charge_front_braced', 'closes': 'draw', 'close_ob': 2,
           'first_tick': {'exposure_a': 2.0, 'exposure_d': 1.0, 'levels_a': 0, 'levels_d': 0}, 'stand': 0.05, 'status': 'seed'}
    ok = copy.deepcopy(data)
    ok['matchups'] = [copy.deepcopy(row)]
    table.check(ok)
    checked = 0
    for key, wrong in (('a', 'chariot'), ('d', 'chariot'), ('situation', 'at_dawn'), ('closes', 'maybe'), ('status', 'hunch')):
        bad = copy.deepcopy(ok)
        bad['matchups'][0][key] = wrong
        with pytest.raises(table.TroopFileError) as e:
            table.check(bad)
        assert 'matchups[0]' in str(e.value) and repr(wrong) in str(e.value), key
        checked += 1
    assert checked == 5


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
    """The rows that carry a decision, pinned by value: the knights keep today's behaviour (`mounted: false`, the horse
    cell of 50 troops, half of `CELL_CAP`: B17.15), the unmustered body has no stat preset and no loadout, a levy has no
    site, and the two elite sites need half."""
    assert not registry.is_mounted('knights_templar') and registry.is_mounted('light_cavalry')
    assert sorted(registry.MOUNTED_TYPES) == ['cavalry', 'light_cavalry', 'mounted_archers']
    from modules.mass_battle import config
    assert config.cell_cap_for('knights_templar') == 75 == config.cell_cap_for('cavalry') == config.CELL_CAP * 3 // 4
    assert config.cell_cap_for('pike') == config.CELL_CAP == config.cell_cap_for('infantry') == config.cell_cap_for('zzz')
    assert registry.stats_for('infantry') is None and 'infantry' not in registry.TROOP_TYPE_STATS
    from modules.mass_battle.equipment import loadout_for
    assert loadout_for('infantry') == (None, None) and loadout_for('pike')[0].name == 'pike'
    from modules.mass_battle.troop_types import recruitment
    assert recruitment.training_site_for('levy') is None
    assert recruitment.training_site_for('knights_templar') == ('stable', 0.5) == recruitment.TRAINING_SITE['knights_templar']
    assert registry.roles_for('levy') == ['Support', 'Reserve'] == registry.roles_for('no_such_type')
    assert table.row_of('infantry')['skill'] == table.row_of('infantry')['power'] == 4      # `power` is the alias of `skill` (B19a.01)
    assert table.row_of('infantry')['discipline'] == 5
    assert all(r['secondary'] is None for r in _artifact()['troops'].values())


def test_a_name_in_both_owners_is_refused():
    """B17.12: a switch or coefficient is a field of the engine's `EngineConfig` (exported to `mass_battle_v1.json`) OR a
    column of a troop-file row, never both. Control: the real file and the real config share no name (`check` accepts it, and
    the config's fields are named, so the claim is not vacuous); each section and column name, upper-cased, is then planted
    as a config field and refused by name."""
    from dataclasses import fields
    from modules.mass_battle import config
    names = {f.name for f in fields(config.EngineConfig)}
    assert len(names) >= 90 and 'PER_CELL' in names
    data = _artifact()
    table.check(data, config_names=names)                       # the control: no shared name
    schema = (table.HEADER_KEYS + table.ROLE_COLUMNS + table.ARM_COLUMNS + table.CLASS_COLUMNS + table.TROOP_COLUMNS)
    checked = 0
    for column in schema:
        with pytest.raises(table.TroopFileError) as e:
            table.check(data, config_names=names | {column.upper()})
        assert repr(column) in str(e.value) and 'EngineConfig' in str(e.value), column
        checked += 1
    assert checked == len(schema) >= 30
