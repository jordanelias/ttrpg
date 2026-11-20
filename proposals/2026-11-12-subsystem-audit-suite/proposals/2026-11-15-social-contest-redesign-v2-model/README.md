# sc_model — an executable transcription of the social-contest proceeding (RD + PLAN B24p)

Scratch model for stress-testing the spec by running it. Not repository code. Where the spec is wrong it is
implemented as written; every guess is in `SPEC_GAPS.md` (ids `Gnn`, cited in the code).

Spec: `proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-14-social-contest-redesign.md` (+ `_part2`,
`_part5` F.6) and `workplans/valoria_master_workplan_v12_part22_b24p.md` / `_cont.md` (the PLAN governs).
Live code imported from the repo (`VALORIA_REPO`, default `/home/user/ttrpg`): `sigma_leverage` (`net_boost`,
`roll_net_continuous`, `LEVEL_SIGMA`, `MU_PER_DIE`, `SD_PER_DIE`, `OB_MIN`, `level`), `dice_engine.degree_from_net`,
and (self-check only) `modules/social_contest/roll.py`.

## Run

```sh
cd /tmp/claude-0/-home-user-ttrpg/2a1f4990-cd7a-5bdc-982c-435886385374/scratchpad/sc_model
PYTHONHASHSEED=0 python -m scmodel.demo              # the 13 types once each (shipped dials), then tell/lie/speak
PYTHONHASHSEED=0 python -m scmodel.demo --controls   # the same at B24p.04's controls
PYTHONHASHSEED=0 python -m scmodel.demo --n 400      # plus run_many(400) per type
PYTHONHASHSEED=0 python selfcheck.py [--n 4000]      # every falsifier number the spec asserts; exit code = FAILs
PYTHONHASHSEED=0 python probe_readings.py 400        # bands/ends per type, shipped and controls
PYTHONHASHSEED=0 python probe_findings.py            # the numbers quoted in SPEC_GAPS (G13, G39, G42, G44)
```

## Layout

| file | holds |
|---|---|
| `scmodel/records.py` | the frozen records of RD A.3 + B24p.02 (`Speaker`, `Decider`, `Room`, `Move`, `ProceedingType` with `base_disposal`, `struck_ends`, `ProceedingInput`, `SideState`, `ProceedingState`, `ExchangeView`, `Choice`, `Exchange`, `ProceedingOutcome`) |
| `scmodel/data.py` | the 13 rows (C.3), rites (C.4), moves (C.4 + B24p.01 cells), grounds, content classes, venue bias (B.2 a), audience kinds (C.5), case_rows (C.6), authorities, difficulty/standard/stakes tables |
| `scmodel/dials.py` | `shipped()` (B24p.23), `controls()` (B24p.04), `rd_shipped()` (the RD's literal column where the plan departs, G17); each takes keyword overrides |
| `scmodel/dice.py` | derived primitives the tree lacks (`pool_of`, `opposed_ob`, `even_line`, `weighted_tenth`, `governing_mean`, closed-form `band_odds`, the B05.14 composer `obstacle`, the B05.02 `roll`), each quoting its plan line |
| `scmodel/rng.py` | `Draw`: keyed `random.Random(sha256((seed, actor, label)))`, standard normals, counted |
| `scmodel/proceeding.py` | `proceed`, `_start`, `_mover`, `_legal`, `_auto`, `_read`, `_hold`, `_exchange`, `LEVERAGE`/`TERMS`/`BALLOT`, `_ballot_input`, `_close`, `exchange_odds`, `closing_odds`, `act_margin` |
| `scmodel/host.py` | `build_input`, `abridged`, `audience_kind`, `row_for_case`, `person_moved_by`, `strain_carried` |
| `scmodel/demo.py` | `default_people`, `run_one`, `run_many`, the demo |

## API

```python
from scmodel import dials
from scmodel.host import build_input, abridged
from scmodel.proceeding import proceed, act_margin, closing_odds, exchange_odds
from scmodel.rng import draw
from scmodel.demo import run_many, run_one, default_people

people = {"a": {"id": "a", "attributes": {"reason": 6, "presence": 3}, "ranks": {"argue": 1}, "proofs": 2},
          "b": {"id": "b", "attributes": {"will": 6}, "regard": {"a": -0.5}}}
inp = build_input(people, "conversation", "full", actor="a", addressed="b", dials=dials.shipped(), effort=2)
out = proceed(inp, draw(0, "a", "roll:proceeding"), decide=None)   # decide(view: ExchangeView) -> Choice, or None
margin, veto = act_margin(out, inp.type, inp)                        # the act's one Margin (B24p.14)
run_many(1000, "legal_trial", D=dials.shipped(), people_fn=default_people, effort=2)
#   -> {'band': Counter, 'ended': Counter, 'exchanges': mean, 'marks': mean, 'moves': Counter}
```

`build_input(people, row, form, move, *, actor, addressed, bench, present, effort, difficulty_level, dials, order)`:
`row` an arrangement id; `form` `full|abridged`; `bench` the seats over the venue (filtered here by the row's
authority); `present` everyone else at the venue (filtered by `floor`; the one addressed is never a hearer, G35);
`order="written_only"` for a filed petition. Person dict keys are listed in `host.py`'s docstring.

Draw discipline (asserted in `proceed`/`_close`): G+5 normals per exchange in the order [reading, xi per ground,
xi_0, hold, speech, steadiness]; three per balloted decider [hold, detection, ballot]; none under `exchange`.
