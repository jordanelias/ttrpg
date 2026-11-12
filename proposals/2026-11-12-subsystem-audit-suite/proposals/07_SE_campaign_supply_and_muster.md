# 07 · SE — what the settlement layer owes the campaign: hands under arms, the standing ration, and somewhere to train

Reconciled: 2026-11-12, U5d closure — folded **A-57 / A-58** and the pessimist's constraint. R-SE-34 ("an army whose holder stands on land his faction does not hold eats from his seat's treasury") is read once a season, not per field (R-PES-SE-14). After a won march onto another's land the land is the aggressor's (`U5d_FA_land_and_seats_pass_on_a_won_march.md`), so from the next season the army stands on land its faction holds and the place's own ladder feeds it; R-SE-36 ("nothing, by rule … living off the occupied place is a `requisition`") therefore covers only an `Unopposed` entry or a drawn or lost field, where the land stays the defender's.

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/24_GROUNDING_GAMES.md` (GM-09; GC-4) — the precedent paragraph's "Bannerlord's wages are memory-grade" corrected: they are page-read at `research/game_precedent_suite/tutorials/T02_warband.md:17`. No edit of the proposal changed.

Carries findings F-SE-19 and F-SE-20 and resolutions R-SE-33 to R-SE-36 of
`audits/07_SE_audit_addendum_B.md` (its §4). It answers Jordan's mass-battle intent (2026-11-12: *"a
campaign layer that feeds the battle and receives its result"*; Bannerlord's *"troops recruited, trained,
tiered, upkept and lost"*) from the settlement side only. The battle, the orders and who may march are
the MB and FA lanes' (`audits/04_MB_audit.md` §10, §17; `audits/06_FA_audit.md` F-FA-03, F-FA-04), cited
and not redone. It closes hole-register row H-212's direction. Nothing is ratified by being written.

## 1. What changes in `engine/season/` at runtime

With the shipped fixtures: nothing. Three arms, each off:

1. **Hands under arms do not work.** Under CP-T08-01's `labour_mode` (planned, shipped `off`), a rung's
   labour is read net of the troops raised from the cohorts there.
2. **The standing ration** (`standing_ration`, new, shipped `off`). At MATTER an army whose holder stands
   at a place his faction does not hold eats from the treasury it marched on, by the arithmetic
   `settlements.provision` already has; the heads it took are not fed a second time at home.
3. **Somewhere to train.** Under `endowment_mode: ground` (the first lane's fixture, shipped `uniform`),
   world-gen stands a `barracks` at each settlement the canon geography file types as a fortress.

No verb is added. The registered modules gain nothing but one read-only query on the army module
(owner: MB).

## 2. The problem, with evidence

- **The realm can raise only levy.** `build_realm(0)` holds no `barracks`, `archery_range`, `stable` or
  `siege_workshop` (addendum §8, E-2: `training kinds present: {}`), and every troop type but levy is
  trained at a Site of one of those kinds (`modules/mass_battle/troop_types/recruitment.py:55-69`). The
  reader is built (`queries/world_q.py::training_sites`) and reads nothing.
- **Raising troops costs the place nothing.** `loop/effects_army.py::_eff_recruit` writes the army
  Record. It moves no stores and leaves `Person.weight` alone (uncoupled by decision: CR-08's entry,
  *"raising a troop does not draw down cohort weight"*), and yield reads no person.
- **An army in the field eats at home.** The troops are counts in a Record; the cohort they were drawn
  from stays where it lives and draws its full want from its home ladder. The only ration is one debit
  at the instant of a field (`settlements.provision`, IN-52, shipped off). H-212 (register line 4629):
  *"An occupied town's stores are therefore untouched by the army standing in it, and a besieged one
  does not starve"*, graded `absent` since 2026-10-16 with the direction undecided.
- **One town cannot raise a unit.** `under_arms_cap(2)` is 60; the module's own comment says a unit
  under the 100-troop block *"routs at once"* (`recruitment.py:38-44`). Named for the MB lane; not
  resolved here (the weights are CR-107's).
- **The precedent, as sourced** (`research/game_precedent_suite/tables/R6`, Rome II manual pages read in
  body): units muster to a general standing in a region *from that region's troop types only*; upkeep
  leaves the treasury every turn; replenishment only on friendly ground; a siege starves. Songs of Syx
  (`tables/R3a`, developer patch notes read in body): rations mandatory, supply anywhere in one's own
  territory. Bannerlord's wages are memory-grade in `tables/R2` and are not relied on `[CORRECTED
  2026-11-12, audits/24_GROUNDING_GAMES.md GC-4: they are page-read in the tree at
  research/game_precedent_suite/tutorials/T02_warband.md:17 [V3 B2] (daily wages; the unpaid lose morale,
  then desert), a guide page and so good for the shape only. The proposal did not rely on them and still
  does not need to]`. The tree's own
  historical pass kept one flat rule (*"Campaign Supply … for any units in hostile territory"*) and cut
  per-unit costs and service timers as bookkeeping (`research/historical/precedents_warfare.md` §8).

## 3. The resolution, decided

**R-SE-33. A soldier is not a farmer while he is a soldier.** The labour of a rung is the hands present
less the hands under arms. Ladder step 4: CP-T08-01 already makes yield read hands; this is one
subtraction in its reader, and it leaves `Person.weight` uncoupled as decided.

**R-SE-34. Away from home an army eats from its holder's treasury, every season.** One flat rule, the
one the historical pass committed and the manual and patch notes agree on. "Away" is the occupation
Query the engine already has (a faction's force at a place it does not hold). "Its treasury" is the rung
of the office its last march was exercised through, which is where `requisition` puts stock and where
the field's ration is read. Ladder steps 3 and 4.

**R-SE-35. A fortress trains foot.** A settlement whose canon `type` is `Fortress` or `Fortress-City`
(S-007 Lowenskyst Fortress, S-014 Ehrenfeld, S-021 Spartfell Fortress) is built with a `barracks`. Ladder
step 4: `venues.yaml` already keys what a settlement is built with on that field; step 3 for the content
(the historical pass kept *"Settlement Muster (Fortress only)"*; the archived design names an Ehrenfeld
barracks district). Horse, missile troops and engines are trained nowhere until someone builds a stable,
a range or a workshop, which is a works row (content, Jordan's) and a reason to `build`.

**R-SE-36. H-212's direction: the occupier pays, the occupied larder is not touched by rule.** Living off
an occupied place is a *taking*, and the engine's verb for a taking is `requisition` (through a seat
whose purview reaches the place, or after `seize`). MATTER does not take from a town on an army's behalf.

**Not proposed.** Movement over the settlement graph (the geography file's 55 edges, cost matrix and
march budget have no reader: first audit F-SE-06): design-first, unchanged. Troop experience, wages by
type, mercenaries: the historical pass cut the first two as bookkeeping and nothing sourced here revives
them. A draw-down of cohort weight at muster: decided against (J-C-2) and not re-raised.

## 4. The exact edits, by owner

**(a) Army module (owner: MB lane) — one query entry.** `mass_battle.under_arms`: input the `army`
Records' `subject_matter` in id order; output `((cohort id, weight units), ...)`, the troops each cohort
has under arms rounded *up* to whole weight units by the module's own `TROOPS_PER_WEIGHT`. The module
owns its record shape and its constant; the host learns neither. `[UNVERIFIED: the Record's per-cohort
field; `world_q.other_army_records` and `recruit_limit`'s `raised` argument show the data is held, the
field's name was not read.]` Registered as a composition row, kind `query`.

**(b) `engine/season/queries/world_q.py` — two readers.**

```python
def under_arms(w: World) -> dict:          # {cohort id: weight units}; {} when no army holds troops
def away(w: World) -> dict:                # {cohort id: (weight units, treasury rung)}: the part of
                                           # `under_arms` in an army whose holder's `march_origin` is a
                                           # place `holder_faction_of` gives to another faction, with the
                                           # treasury of the march that brought it there
```

The treasury is read off the log on the pattern `world_q.siege_pressed_by` already uses (the latest
Event of a `march` kind whose causing act is a `march` by this holder; that act's `via` office's rung,
which is what `seam/wrappers/mass_battle.py::_seat_treasury` returns at field time). `siege_pressed_by`
itself reads this season's sieges only and is not reused; no state is added to the army Record.

**(c) CP-T08-01's `labour(w, rung)`** (planned; `queries/world_q.py`): the sum over presence becomes
`(weight − under_arms.get(pid, 0)) × body / body_scale`, floored at 0. One term in one planned function.

**(d) `larder_input`** (`queries/world_q.py::_larder_parts`): when `standing_ration` is on, an `Eater`'s
weight is `person.weight − away.get(pid, (0, None))[0]`. The module (`larder_draw`) is unchanged.

**(e) `engine/season/loop/matter.py`**, after the subsistence pass and before yield, when
`standing_ration` is on: group `away` by treasury; for each, `p = provision(provision_input(w, Σ weight
units, treasury))` (the existing entry, by role string) and debit `p.consumed` from the treasury through
the owner of debits, emitting `stores.changed`; where `p.troops < Σ weight units` the write carries a
`shortfall:<kind>` Observation exactly as a drained larder's does. Nothing else is written: an unfed army
is bounded at its next field by the same `provision` call, which is already built.

**(f) `engine/season/rosters.yaml`** — beside the first lane's `site_endowment`, one table read by the
same loader:

```yaml
  training_endowment:
    source: "proposals/2026-11-12-subsystem-audit-suite/proposals/07_SE_campaign_supply_and_muster.md; ED-IN-0306"
    keys: [settlement types (the geography file's `type`), site_kinds]
    uniform: {}                                   # the control: today's realm, no training Site
    ground:                                       # [ASSUMPTION; medium; Jordan to correct; revert: {}]
      Fortress:      [barracks]
      Fortress-City: [barracks]
```

`harness/populated.py::build_realm` mints one Site per entry at full condition in the loop that mints
garrisons, under `endowment_mode == "ground"`. The loader refuses a type the geography file does not
use and a kind outside `site_kinds`.

**(g) `engine/season/data/fixtures.py`**: `standing_ration=False` (H-212's row gains the arm and stops
reading `absent`).

## 5. The gate, and the falsifier

- **Execution artifact** (a hand-built world, as `test_levy_feed.py` builds its own; new file
  `engine/season/tests/test_standing_ration.py`): a cohort of weight 6 at a field town, 300 troops
  raised from it into an army (one weight unit), marched to a settlement another faction holds and left
  there two seasons, with `labour_mode` and `standing_ration` on. Each MATTER: the treasury falls by one
  weight unit's ration; the home cohort's `want` is five units' worth; the home rung's labour is five
  units. March it home: the treasury stops falling, the want and the labour return to six.
- **Conservation.** In every season of that run the units eaten at home plus the units eaten from the
  treasury equal the whole cohort's want when both are stocked. A head eats once.
- **Falsifier.** A season in which the sum is more (a head eating twice) or less with both stocked; a
  debit from the *occupied* settlement's stores; a debit while the army stands on its own faction's
  land. Mutation: read `under_arms` where `away` is meant in (d), and the army at home goes unfed.
- **Control.** All three arms off reproduce the shipped hashes. On the realm no pin moves in any case,
  because `build_realm` holds no army (probe) and the muster verbs are never attempted in computed play
  (`audits/04_MB_audit.md` §1.3).
- **For (f):** under `ground`, `training_sites` for the cohort at S-014 returns a `barracks` at scale and
  `recruit_limit('spearmen', …)` there is positive, while at a town it is 0; under `uniform` both are 0.

## 6. What this does not cross

ED-IN-0255 (only cohorts eat): the army's ration is the cohort's own heads eating elsewhere, by the
cohort's own ration. J-C-2 (muster does not write weight): honoured. ED-SE-0053's standing order (no
delivery across `contain`): MATTER consumes at the treasury; it moves nothing. IN-52's flip
(`field_provisioning`): untouched; with both on, a field's ration and the standing ration are two calls
to one entry on one stock, and the field-time call already nets what was eaten.

## 7. NERS reading (definitions: `CLAUDE.md` §0.06; E last)

- **N.** Cut (c) and an army costs its people nothing to raise; cut (d) and (e) and it costs nothing to
  keep abroad; cut (f) and there is one kind of soldier. Each is a decision every named referent turns
  on. Bottom-up: three host reads and one roster. Top-down: the treasury proposal's one stock acquires
  its third claimant. Lateral: FA's `declare` and occupation become costly to sustain, which is the
  response F-FA-04 says is missing. Across scales: a duel's outcome can empty a town of hands by way of
  a march.
- **R.** Whether to raise, how long to stay and where to raise from become choices with a loser. With
  no player: a long occupation drains the occupier's treasury, his towns lose hands, and his sworn men
  compete with his army for the same grain. Completeness: an army with no treasury eats nothing and
  fields nobody at its next field (the built floor lifts it to one); an army at home costs only labour.
- **S.** One ration arithmetic for the hungry, the field and the standing army (`provision`); one
  occupation Query; labour read once. It pauses nothing and adds no scale-local dialect.
- **E, last, against N and R.** Two readers, two subtractions, one MATTER pass over a set that is empty
  in the shipped realm, one roster table. "An army away from home eats its lord's grain and leaves the
  fields short" is a sentence a player can use.

## 8. Cost class

Small build, split across lanes: (a) is MB's edit; (c) rides CP-T08-01; (f) rides the endowment build.
Hash EQUAL at every shipped arm; each flip a declared mover in its own commit.
