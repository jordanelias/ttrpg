#!/usr/bin/env python3
"""Cook the measured duel table and the troop file into the artifact the mass-battle contact draw reads, and refuse a stale one.

WHY THIS EXISTS (B19a.03, MBA-03). The mass-battle contact draw reads the felling chance of a man in a given duel (`h`), measured
by `tools/calibrate_mb_contact.py` over the duel engine into `references/mb_contact/duel_grid.json`. A value the engine reads lives
in a typed artifact behind an exporter with a blocking `--check` (CLAUDE.md §5): this tool writes
`engine/engine_params/mb_contact.json` (the port's) and `modules/mass_battle/core/contact_table_data.py` (the same document as a Python
literal, because a registered module opens no file, A-25; the precedent is `export_troops.py`'s `troops_data.py`). The module that
reads it is `modules/mass_battle/core/contact_table.py`. A hand edit of either artifact fails `--check`.

WHAT IT HOLDS. `pairs`: for each ORDERED pair of grid fighter types `(arm, armour, skill)`, keyed `attacker>defender`, the row of
the DEFENDER's man: `h` (K felling chances, rounds 1..K, rounded to 4 significant digits), `beta`, `flags`. A cell of the measured
table gives both orders (side `b`'s row is `a>b`, side `a`'s row is `b>a`); in a mirror cell the two sides measure one quantity and
the pair holds their mean (flags united). `beta` is the slope of `logit(h_1)` per step of the ATTACKER's skill, holding the rest of
the pair fixed, from the pair's two skill neighbours on the grid (1, 3, 5): at skill 3 it is `(L(5) - L(1)) / 4`, at skill 1
`(L(3) - L(1)) / 2` and at skill 5 `(L(5) - L(3)) / 2` (one-sided at an edge), `L` = `logit(h_1)` of the same pair with only the
attacker's skill changed. [ASSUMPTION: one step of the defender's skill moves the logit by `-beta` (the ladder is the skill
difference, MBA §1.4) -- basis: the contact draw's named levels are in skill steps on one ladder; reversible: measure beta from the
defender's neighbours too.] The twelve interpolation check cells (skill 2 and 4) are not exported: they test the interpolation
(`tests/valoria/test_export_mb_contact.py`) and the module never reads them. Beside `pairs`: `contact` (the troop file's exposure,
levels and K), `missile`, `matchups` with their status tags, `arms` (the arm-to-duel-key map) and the header (`engine_fingerprint`,
`K`, `schema_version`, `_generated`).

WHAT `--check` REFUSES, each naming the row and the remedy: (a) `mb_contact.json` or `contact_table_data.py` missing, or differing
from what the two heads (the table and the troop file) derive; (b) a STALE CALIBRATION: `calibrate_mb_contact.engine_fingerprint()`
(the one owner of the fingerprint) differs from the table's, so a personal-combat change that would move a felling chance cannot ship
with an old table; (c) a troop arm whose duel weapon (`duel_key`, or a missile arm's `sidearm`) the table lacks, a pair of fighter
types the troop file can field with no cell, and any other cell of the grid (`Grid.cells()`, the instrument's own list, so the two
cannot disagree) the table lacks; a table whose `K` is not the troop file's `contact.K`.

Usage:
    python3 tools/export_mb_contact.py           # write both artifacts
    python3 tools/export_mb_contact.py --check   # re-derive and diff vs committed (exit 1 on drift or a stale calibration)
"""
from __future__ import annotations

import json
import math
import os
import pprint
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402
import calibrate_mb_contact as cmc  # noqa: E402

REPO = ci_common.REPO
if REPO not in sys.path:
    sys.path.insert(0, REPO)

TABLE = cmc.TABLE
TROOPS = cmc.TROOPS
OUT = os.path.join(REPO, 'engine', 'engine_params', 'mb_contact.json')
OUT_PY = os.path.join(REPO, 'modules', 'mass_battle', 'core', 'contact_table_data.py')
SCHEMA_VERSION = 1
SIG_DIGITS = 4          # `h` and `beta` are kept to this many significant digits
EPS = 1e-6              # logit's clamp: a felling chance of 0 or 1 is read as EPS or 1 - EPS
REMEDY = 'python tools/calibrate_mb_contact.py run references/mb_contact/duel_grid.json --workers 4'


class Refused(Exception):
    """A head the exporter will not cook; the message names the row and the remedy."""


def _sig(x: float) -> float:
    return float(f'{x:.{SIG_DIGITS}g}')


def _logit(h: float) -> float:
    h = min(max(h, EPS), 1 - EPS)
    return math.log(h / (1 - h))


def _key(t: tuple) -> str:
    return '/'.join(str(x) for x in t)


def _load(path: str) -> dict:
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def _rows(table: dict) -> dict:
    """`{(attacker type, defender type): (h list, flags set)}` for every ordered pair the table's cells give (the check cells too)."""
    out = {}
    for c in table['cells']:
        ta, tb = (c['a']['arm'], c['a']['armour'], c['a']['skill']), (c['b']['arm'], c['b']['armour'], c['b']['skill'])
        ra, rb = c['sides']['a'], c['sides']['b']          # ra: a's man taken, attacker b
        if ta == tb:                                       # a mirror: two measurements of one chance
            h = [(x + y) / 2 for x, y in zip(ra['h'], rb['h'])]
            out[(ta, ta)] = (h, set(ra['flags']) | set(rb['flags']))
        else:
            out[(tb, ta)] = (ra['h'], set(ra['flags']))
            out[(ta, tb)] = (rb['h'], set(rb['flags']))
    return out


def _refuse_unfielded(grid: 'cmc.Grid', table: dict, rows: dict) -> None:
    """(c): an arm the table lacks, a fielded pair with no cell, then any cell of the grid the table lacks."""
    have_arms = {c[side]['arm'] for c in table['cells'] for side in ('a', 'b')}
    for arm in grid.arms:
        if arm not in have_arms:
            raise Refused(f'the troop file names the duel weapon {arm!r} (a `duel_key`, or a missile arm\'s `sidearm`) and the table '
                          f'has no cell for it; the table was measured for {sorted(have_arms)}. Re-measure: {REMEDY}')
    # a fielded type of skill 2 or 4 is read by interpolation between its two grid skills, so it needs the cells of both neighbours
    need = {}
    for t in grid.types_fielded:
        near = [s for s in cmc.GRID_SKILLS if s == t[2]] or [max(s for s in cmc.GRID_SKILLS if s < t[2]), min(s for s in cmc.GRID_SKILLS if s > t[2])]
        need[t] = [(t[0], t[1], s) for s in near]
    fielded = sorted(need, key=grid.sortkey)
    for i, t1 in enumerate(fielded):
        for t2 in fielded[i:]:
            for g1 in need[t1]:
                for g2 in need[t2]:
                    if (g1, g2) not in rows and (g2, g1) not in rows:
                        raise Refused(f'the troop file can field {_key(t1)} against {_key(t2)}; the table has no cell for {_key(g1)} against '
                                      f'{_key(g2)}, which its interpolation reads. Re-measure: {REMEDY}')
    missing = [k for k in grid.cells() if (k[0], k[1]) not in rows and (k[1], k[0]) not in rows]
    if missing:
        raise Refused(f'the table lacks {len(missing)} of the grid\'s {len(grid.cells())} cells, the first {grid.key_text(missing[0])}. '
                      f'Re-measure: {REMEDY}')


def build(table_path: str | None = None, troops_path: str | None = None) -> dict:
    """The artifact, from the two heads, behind the refusals above. Raises `Refused`."""
    table_path, troops_path = table_path or TABLE, troops_path or TROOPS
    if not os.path.exists(table_path):
        raise Refused(f'no measured table at {os.path.relpath(table_path, REPO)}. Measure it: {REMEDY}')
    table = _load(table_path)
    if table.get('schema') != cmc.SCHEMA:
        raise Refused(f'the table\'s schema {table.get("schema")!r} is not the instrument\'s {cmc.SCHEMA}. Re-measure: {REMEDY}')
    fp = cmc.engine_fingerprint()
    if table.get('engine_fingerprint') != fp:
        raise Refused(f'STALE CALIBRATION: the duel engine\'s fingerprint {fp[:12]} is not the table\'s '
                      f'{str(table.get("engine_fingerprint"))[:12]} (a change to engine/engine_params/combat_engine_v1.json or '
                      f'modules/combat/*.py can move a felling chance). Re-measure: {REMEDY}   '
                      f'(to run it in chunks and merge them, see the instrument\'s docstring, "CHUNKING THE GRID")')
    import yaml
    with open(troops_path, encoding='utf-8') as fh:
        troops = yaml.safe_load(fh)
    grid = cmc.Grid(troops_path)
    if table.get('K') != grid.K:
        raise Refused(f'the table holds K = {table.get("K")!r} rounds and the troop file\'s contact.K is {grid.K}. Re-measure: {REMEDY}')
    rows = _rows(table)
    _refuse_unfielded(grid, table, rows)

    def row(attacker: tuple, defender: tuple) -> tuple:
        return rows[(attacker, defender)]

    pairs = {}
    for ta in grid.types():
        for td in grid.types():
            h, flags = row(ta, td)
            arm, armour, skill = ta
            lo, hi = [s for s in cmc.GRID_SKILLS if s < skill][-1:], [s for s in cmc.GRID_SKILLS if s > skill][:1]
            a0, a1 = (lo[0] if lo else skill), (hi[0] if hi else skill)
            beta = (_logit(row((arm, armour, a1), td)[0][0]) - _logit(row((arm, armour, a0), td)[0][0])) / (a1 - a0)
            pairs[f'{_key(ta)}>{_key(td)}'] = {'h': [_sig(x) for x in h], 'beta': _sig(beta), 'flags': sorted(flags)}
    contact = {k: v for k, v in troops['contact'].items() if k != 'missile'}
    return {
        '_generated': 'tools/export_mb_contact.py -- do not hand-edit; edit references/troops.yaml, or re-measure with tools/calibrate_mb_contact.py',
        'schema_version': SCHEMA_VERSION,
        'source': ['references/mb_contact/duel_grid.json', 'references/troops.yaml'],
        'engine_fingerprint': table['engine_fingerprint'],
        'K': table['K'],
        'precision': f'h and beta to {SIG_DIGITS} significant digits; a pair is `attacker>defender`, its row the defender\'s man',
        'arms': {name: {k: a[k] for k in ('duel_key', 'duel_key_status', 'sidearm') if k in a} for name, a in troops['arms'].items()},
        'contact': contact,
        'missile': troops['contact']['missile'],
        'matchups': troops['matchups'],
        'pairs': pairs,
    }


def render(data: dict) -> str:
    """The JSON, one pair a line (reviewable) and every other block indented."""
    head = json.dumps({k: v for k, v in data.items() if k != 'pairs'}, indent=2, ensure_ascii=False)
    body = ',\n'.join(f'    {json.dumps(k)}: {json.dumps(v)}' for k, v in data['pairs'].items())
    return head[:-2] + ',\n  "pairs": {\n' + body + '\n  }\n}\n'


def literal(data: dict) -> str:
    """The module-side artifact: the document as a Python literal, `DATA`."""
    return ('"""GENERATED by tools/export_mb_contact.py from references/mb_contact/duel_grid.json and references/troops.yaml -- do not hand-edit.\n\n'
            'The measured felling chances as a Python literal, read by `contact_table.py`: a registered module opens no file (A-25).\n'
            'engine/engine_params/mb_contact.json is the same document for the port; `export_mb_contact.py --check` pins them equal."""\n'
            f'DATA = {pprint.pformat(data, width=140, sort_dicts=False, compact=True)}\n')


def main(argv):
    try:
        data = build()
    except Refused as exc:                                        # a refusal is named and exits non-zero, never a traceback
        print(f'[mb_contact] REFUSED -- {exc}')
        return 1
    want = {OUT: render(data), OUT_PY: literal(data)}
    if '--check' in argv:
        for path, text in want.items():
            if not os.path.exists(path):
                print(f'[mb_contact] MISSING {os.path.relpath(path, REPO)} -- run without --check.')
                return 1
            with open(path, encoding='utf-8') as fh:
                if fh.read() != text:
                    print(f'[mb_contact] DRIFT -- {os.path.relpath(path, REPO)} is stale. Run: python3 tools/export_mb_contact.py')
                    return 1
        print(f'[mb_contact] OK -- {len(data["pairs"])} pairs, K = {data["K"]}, fingerprint {data["engine_fingerprint"][:12]}.')
        return 0
    for path, text in want.items():
        with open(path, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text)
        print(f'[mb_contact] wrote {os.path.relpath(path, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
