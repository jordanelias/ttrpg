# SE — the harvest is of what is grown and is on the record, a second wall adds, and the supply arm ships only where armies can eat

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-06) — `World.write` takes no `spec=` today (`state/world.py:1138-1148`); the receipt edit the proposal named as its fallback is required.

Source: `audits/16_PESSIMIST_SE.md` F-PES-SE-05, -07, -08, -09; §1.2 A-2, A-3; resolutions R-PES-SE-06,
-10, -11, -12. Read at `d161a61`. Reference only (`CLAUDE.md` §0.05). Lane SE; edit 3's consumer is MB.

Four small edits at four owners. None adds a verb, an Event kind or a store.

## What it changes in `engine/season/` at runtime

1. The season factor multiplies only the matter kinds the roster marks as **grown**. Shipped
   (`season_factor_draw=()`, factor 1.0) nothing moves; with the weather arm on, ore and timber stop
   following the weather.
2. `yield.taken`'s receipt carries **what was yielded**, so the record of a season says how much a place
   brought in. No reader in the loop branches on it; hashes move wherever a yield is written (a declared
   mover), behaviour does not.
3. `settlements.fortification` returns the **complement of the product of the garrisons' shortfalls**
   in place of their mean. A settlement with one garrison reads exactly what it reads today, so
   `build_realm` does not move (every settlement there has one).
4. `field_provisioning` gains a **load-time refusal**: the arm may be on only in a world where some
   treasury the field reads can ration a man. Shipped (off) nothing moves.

## The problem, with evidence

All runs under `…/scratchpad/runs/PES_SE/`, `PYTHONHASHSEED=0`.

- `pes_noacts.py harvest 0 8` (weather arm `((0.5, 1.0, 2.0),)*4`): realm ore yield 2,375 → 1,688 →
  1,806 while grain goes 1,900 → 1,343 → 1,436; `produce.py` applies `factor[rung]` to every Site on the
  rung. A `yield.taken` Event carries one receipt with `delta=None` and `observed=()`; across the run no
  Event or Observation names a factor (count 0). `Rung.yield` is written 37 times a season and read by
  nothing outside `harness/` and tests.
- `kernel.py` K4: garrison conditions (1000) → 1.0; (1000, 1000) → 1.0; (1000, 0) → 0.5; `build` mints a
  Site at condition 0 (`loop/effects_founding.py:234`).
- `pes_supply.py`: after two seasons of yield, 0 of 34 offices sit at a rung that could ration one man
  and the defender's treasury of 37 of 37 settlements is a territory rung holding nothing; 9,250 units
  lie at settlement rungs. With the arm on, `provision` returns 0 troops for both sides of every field,
  lifted to the crash floor (`modules/mass_battle/massbattle.py:212`, `:328`).

## The resolution (decided)

**R1. Weather is of the field, not the mine.** `rosters.yaml` gains `grown_kinds: [grain]`
`[ASSUMPTION; medium; Jordan to correct: salt by evaporation and timber by felling are arguable
members]`. `settlements.produce` multiplies by the rung's factor only for a kind in the set; other
kinds take factor 1. Ladder step 5. The rejected alternative is a per-Site-kind flag: a harbour yields
both grain and salt, so the property is the kind's.

**R2. A yield is a fact with a size.** The `yield` write's receipt carries the produced map. This gives
`Rung.yield` its first reader (the receipt) and lets a chronicle print *Auerheim brought in 20 grain
where it brought in 40 the year before*. Whether persons should also *learn* a harvest (an Observation
deposited to witnesses) is not decided here: it multiplies claims by 37 a season and belongs with the
first lane's `unrest` reader.

**R3. Walls add.** `fortification = 1 − Π (1 − cᵢ / scale)` over the settlement's garrisons. One
garrison at condition c reads c/scale (today's value). A second never lowers the first; a new one at
condition 0 adds nothing until it is raised; two at half strength read 0.75. The value stays in
`[0, 1]`, which was the mean's stated reason (`fortification.py`: *"keeps the value in [0.0, 1.0]"*).
Ladder step 5.

**R4. The supply arm cannot be flipped into a realm that cannot eat.** With `field_provisioning` true,
the fixtures check at driver construction refuses a world in which no office's rung and no
`governing_hold` rung holds one ration of every eaten kind. The first lane's `07_SE_treasury_granary_B.md`
(R-SE-28: the stock at the seat rungs) is what makes the check pass; this is the loader's refusal for
that data family (`CLAUDE.md` §0.05: licensed, the loader's refusal per data family), not a guard over
the tree. It also fixes the order of work: the granary moves before the arm flips.

## Edits

### 1 · `engine/season/rosters.yaml`, `queries/inputs.py::ProduceInput`, `queries/world_q.py::produce_input`, `modules/settlements/produce.py`

Roster row:

```yaml
grown_kinds:
  source: "audits/16_PESSIMIST_SE.md F-PES-SE-07: the season factor is weather, and weather bears on what is grown."
  note: "The matter kinds a season's factor multiplies. A kind outside the set yields at factor 1."
  values: [grain]
```

checked at load as a subset of `matter_kinds`. `ProduceInput` gains `grown: frozenset`. In `produce`:

```python
f = factor[rung] if k in inp.grown else 1
produced[k] = produced.get(k, 0) + int(base * (max(0, condition) / inp.scale) * f)
```

At factor 1.0 the float expression is operand for operand today's, so no truncation moves.

### 2 · `loop/matter.py` (the `yield` write, `:781-785`)

The write passes the produced map as the receipt's `spec` (the Receipt already has the field:
`Receipt(subject, mode, driver, field, delta, spec, serial)`), e.g. `spec=tuple(sorted(produced.items()))`
`[GROUNDED, 25 G-06: it does not. `World.write`'s parameters are `thing, token, apply, record_kind,
fieldname, driver, caused_person_exists, emits, causes, subject, actor, via, change, matured_term,
observed` (`state/world.py:1138-1148`); its two mint sites pass no `spec` (`:1442`, `:1494`), though
`Gate.mint` takes one (`state/gate.py:1905-1906`) and `StateChange` has the field
(`state/carriers.py:197-205`). The edit is a `spec` parameter on `write` passed through at `:1442`]`.

### 3 · `modules/settlements/fortification.py`

```python
def fortification(inp: FortInput) -> float:
    """A settlement's defensive strength, `0.0` to `1.0`: the complement of the product of each
    garrison's shortfall, so a second wall never weakens the first."""
    breach = 1.0
    for c in inp.conditions:
        breach *= 1.0 - max(0, min(c, inp.scale)) / inp.scale
    return 1.0 - breach
```

No garrison gives `1.0 − 1.0 = 0.0`, as today.

### 4 · `data/fixtures.py` (the `field_provisioning` row) and the driver's construction check

Beside the existing refusals at driver construction (`manifest/registrar.py::require_entries`'s
neighbours), when `fixtures.get("field_provisioning")` is true:

```python
ration = {k: r for k, r in fixtures.get("subsistence_weight").items() if r > 0}
rungs = {o.rung for o in w.offices.values() if o.rung in w.rungs}
rungs |= {t.object for s in settlements if (t := world_q.governing_hold(w, s)) and t.object in w.rungs}
if ration and not any(all((w.rungs[r].stores or {}).get(k, 0) >= n for k, n in ration.items()) for r in rungs):
    raise Unspecified("`field_provisioning` is on and no treasury the field reads holds one ration",
                      "H-241", needs="stock at a seat rung or a held rung (07_SE_treasury_granary_B R-SE-28)",
                      law="IN-52: a levied treasury provisions a field")
```

`H-241`'s sweep arm *"True on empty treasuries"* becomes a test of this refusal.

## Gate (execution artifacts)

1. `engine/season/tests/test_season_weather_per_territory.py`: weather arm on, eight seasons at seed 0:
   realm ore and timber yield equal the weather-off run season for season; grain differs. Control: the
   weather-off run is hash-equal to base.
2. A planted `yield` write: its Event's receipt carries the produced map; `World.content_hash()` of a
   world with no Site is unchanged.
3. `kernel.py` K4 re-run: (1000,) → 1.0; (1000, 1000) → 1.0; (1000, 0) → 1.0; (500, 500) → 0.75;
   () → 0.0. `build_realm(0)` barrier-only, three seasons: hash equal to base.
4. `build_realm(0)` with `field_provisioning=True` and no other change: construction refuses, naming
   H-241. With the first lane's seat-rung stock applied: construction passes and a seeded march fields
   more than the floor on both sides.

## Falsifier

For edit 3: any consumer in `modules/mass_battle/` that relies on the mean's property that a ruined
second garrison *lowers* the value (a siege that wears one of two garrisons expecting the settlement's
strength to fall by half). `besiege` *"wears the garrison"* (`rosters.yaml:1160`); with one garrison per
settlement the two formulas agree, and the MB lane should read this edit before any settlement gains a
second.

## NERS (`CLAUDE.md` §0.06; E last)

- **N.** Cut R1 and a bad harvest is also a bad year underground, which no player would predict from
  the word. Cut R2 and a season's product stays a write nobody reads. Cut R3 and building a wall is
  self-harm. Cut R4 and one fixture flip makes army size meaningless.
- **R.** R3 makes `build` of a garrison a choice with a return; R1 lets a mining town and a farming town
  differ under one sky once the endowment lands.
- **S.** R3 keeps the `[0, 1]` reading MB already takes. R4 states an order two lanes' proposals depend
  on. R1's set is a roster, read by the one module that yields.
- **E.** One roster row, one input field, two one-line changes, one function body, one refusal. The
  vocabulary gains one word (`grown_kinds`), defined at its roster row.

## Not in this proposal

Which method the weather draws by (the audit's §6.2 J-2); a harvest season within the year (the
`season_factor_draw` table already takes one entry per season of the year, so a winter of `(0,)` for
grown kinds is content once R1 lands); `field` and `woodland` Site kinds (R-PES-SE-13, with the first
lane's endowment).

## Cost

Small. Edit 4 depends on nothing; edits 1 to 3 are independent of each other.
