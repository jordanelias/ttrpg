"""The mass-battle engine reads one explicit config, never the process (B17.12; `04_MB_typed_outcome_and_one_path` §3).

`config.EngineConfig` holds every switch and global coefficient; `config.DEFAULT` is the shipped instance;
`resolve_field(inp, rng, cfg=...)` takes a config as an argument. A variant is an engine tree BUILT from a config
(`systems/mass_battle/sim/variant.py`), because the modules read their constants as module names. Each claim below is shown
against its control: a variant that differs does differ in outcome, and the shipped tree refuses it by name instead of
running it as if it were its own.
"""
import dataclasses
import hashlib
import importlib
from engine.dice_engine import draw

import pytest
import yaml

from engine.season.data import files
from engine.season.queries.inputs import MassBattleInput
from modules.mass_battle import config
from systems.mass_battle.sim import variant

_GEO = yaml.safe_load(open(files.GEOGRAPHY_YAML, encoding='utf-8'))
# Sides large enough that the field is fought for ticks rather than routing on contact (the module test's own field).
_FIELD = MassBattleInput(weights=((180.0, 120.0), (240.0,)), territory="T9", fort_level=1.0, stances=(-1.0, 0.5),
                         walls_dr=None, origin=None, loyalties=(1.5, -0.5), loyalty_gain=0.4, geography=_GEO,
                         condition_scale=1000)
_LEGACY = dict(PER_CELL=False, FIELD_MOVEMENT=False, MB_NODE_COHESION=False, MB_FRICTION=False)


def _digest(resolve, **kw):
    h = hashlib.sha256()
    for seed in (1, 2, 3):
        h.update(repr(dataclasses.asdict(resolve(_FIELD, draw.seeded(draw.H2("test_mass_battle_variant", seed)), **kw))).encode())
    return h.hexdigest()


def test_the_shipped_engine_refuses_a_config_that_is_not_its_own():
    from modules.mass_battle import massbattle
    legacy = dataclasses.replace(config.DEFAULT, **_LEGACY)
    with pytest.raises(ValueError) as e:
        massbattle.resolve_field(_FIELD, draw.seeded(draw.H2("test_mass_battle_variant", 1)), cfg=legacy)
    assert 'variant' in str(e.value)
    # the control: its own config, stated or not, is the same field
    assert _digest(massbattle.resolve_field, cfg=config.DEFAULT) == _digest(massbattle.resolve_field)


def test_a_variant_engine_resolves_the_field_its_config_describes():
    from modules.mass_battle import massbattle
    shipped = _digest(massbattle.resolve_field)
    legacy = dataclasses.replace(config.DEFAULT, **_LEGACY)
    with variant.built(legacy) as cfg_mod:
        engine = importlib.import_module('modules.mass_battle.massbattle')
        assert engine is not massbattle and cfg_mod is not config
        assert cfg_mod.PER_CELL is False and cfg_mod.MB_FRICTION is False and config.PER_CELL is True
        assert engine._config.DEFAULT == legacy
        moved = _digest(engine.resolve_field, cfg=legacy)       # the variant's own resolve_field takes the config it was built from
        with pytest.raises(ValueError):
            engine.resolve_field(_FIELD, draw.seeded(draw.H2("test_mass_battle_variant", 1)), cfg=config.DEFAULT)   # and refuses the shipped one, the same way
    assert moved != shipped, 'the variant fought the same field as the shipped engine, so the config did not reach the arithmetic'
    # the shipped tree is back, name by name, and fights as it did
    assert importlib.import_module('modules.mass_battle.config') is config
    assert importlib.import_module('modules.mass_battle.massbattle') is massbattle
    assert _digest(massbattle.resolve_field) == shipped


def test_the_variant_reader_takes_a_workbench_scripts_variables():
    """The module is deaf to the process (the subprocess falsifier is in test_field_golden_pins); the variant reader is not:
    `cfg_from_environ` is how a workbench script turns its caller's variables into a config, and `SIGMA_HEAD` is the one
    field whose variable is not its own name."""
    flipped = variant.cfg_from_environ({'PER_CELL': '0', 'SIGMA_HEAD': '0', 'K_LINEAR': '5', 'MB_VOLLEYS_START': '7', 'JUNK': 'x'})
    assert (flipped.PER_CELL, flipped.SIGMA_HEAD_ENABLED, flipped.K_LINEAR, flipped.MB_VOLLEYS_START) == (False, False, 5.0, 7.0)
    assert dataclasses.replace(flipped, PER_CELL=True, SIGMA_HEAD_ENABLED=True, K_LINEAR=config.DEFAULT.K_LINEAR,
                               MB_VOLLEYS_START=config.DEFAULT.MB_VOLLEYS_START) == config.DEFAULT   # nothing else moved
    assert variant.cfg_from_environ({}) == config.DEFAULT
