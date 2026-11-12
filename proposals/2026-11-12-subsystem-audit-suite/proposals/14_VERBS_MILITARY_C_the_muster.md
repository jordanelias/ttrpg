# VERBS · MILITARY · C — the muster: `recruit`, `discharge_troops`, and a commander who is a person

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Parts 3–4; `U5b_VERBS_military_physical_residue.md`) — (1) **Layer 1**: `recruit` and `discharge_troops` write one cell on every band, so they are task rows with **flat** `writes:` and `emits:` (residue §1, shape (a)): the `share` 1.0 / 1.0 / 0.5 is the roster `task_fraction`, read and not restated; `levy.shirked` and `discharge.balked` are the keyed `emits_on_refusal` clause `draw`; the roster is `graded_tasks`. (2) **A-5, A-6, A-7**: one sampler; the pool is the one pool rule on the commander's `command` score, the same definition row the field reads (`U5b_MB_rulings_in_the_field.md` §1). (3) **A-25**: `cohort_committed`, `footing_war` and `levy` are named levels for the roller. (4) Edit 7's `armies_at_build` is the **one** fixture for armies at build (`04_MB_playable_field_scenario.md`'s `army_presets` yields to it), and Edit 5's opportunity-key digest is the one such edit. (5) A-22 and A-23 bear on who may levy and whether a detained commander commands: both are read where the seat's act is formed (FA's; `06_FA_levy_through_the_seat_B.md`). A-15 (natural death on) makes Edit 6's successor and dispersal reachable in ordinary play. A-2: the roll is a Record a person holds.

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-04) — a typed conjunct cannot be waived by a payload key (`data/requires.py:1027-1030`); the proposal's stated fallback for `room` is now the edit. `14_VERBS_MILITARY_D_the_order_of_battle.md:128` carries the same mark and takes the same answer.

Batch M-C of `audits/14_VERBS_MILITARY.md` (§1 S3, §3.1, §3.2, §5.3). Source: F-VM-02, F-VM-03,
F-VM-06; `audits/04_MB_audit.md` F-MB-03, F-MB-13, F-MB-16; `AUDIT_BRIEF.md` "Standing rule". It
**adopts** `06_FA_levy_through_the_seat_B.md` (who may levy) and builds on it; it carries the mechanism
proposal D's four rows share. The army Record and its rule stay ED-IN-0306's and the module's. Nothing
is ratified by being written.

## 1. What it changes in `engine/season/` at runtime

1. A person who holds an `army` Record forms `recruit` and `discharge_troops` on it through the one
   chooser, when the army has room to raise or men to spare. Nobody else forms them.
2. A command with no payload is carried out to the army's doctrine and footing by the module; a
   command with a payload is unchanged (the menu's).
3. A levy and a discharge are each one draw: how many answer, how many go.
4. A dead commander's roll is taken up by his successor; a leaderless army, and troops an army may no
   longer keep, face a dispersal draw at MATTER.
5. With `armies_at_build: off` (shipped) no `army` Record exists, so nothing forms and the realm,
   spine and corpus hashes are EQUAL but for one declared mover (Edit 3's kind narrowing).

## 2. The problem (evidence)

- `data/fixtures.py:1157`: the six army verbs are withheld; `rosters.yaml:2671-2680` gives the reason
  (the command is payload, no Candidate carries it). `aperture 2 0`: formed 0, the six `army.*` kinds
  never emitted.
- `harness/army_presets.py:12-20`: the unplayed commander's army is folded between seasons, outside
  DELIBERATE and outside anyone's budget, from a plan that "draws nothing"; nothing calls it.
- `probe_army_s0.txt` (`build_realm(0)`, hand-built acts through `SeasonDriver.resolve`): the verbs
  execute; a levy of 60 raises exactly 60; after the commander's death through the gate `army_of`
  is `None`, `other_army_records` still returns his army, and
  `armyrecord.cohort_claims` counts its 40 levy against the successor's new army
  (`queries/world_q.py:2198-2203` has no holder test where `army_of`, `:2278-2287`, has one).
- `armyrecord.py:303-311`: the cap is asked at `recruit` only; a cohort whose `weight` falls, or
  that leaves the faction's ground, keeps its men under arms.
- An army costs nothing to keep (`07_SE_campaign_supply_and_muster.md` §2), so `discharge_troops`
  has no motive; SE's three arms supply it and are cited, not redone.

## 3. Exact edits, by owner, in landing order

**Edit 1 — the module: doctrine step, footing, state** (`modules/mass_battle/armyrecord.py`;
owner MB, reviewed by it).

- `KEYS = ('faction', 'strategy', 'trained', 'subformations', 'doctrine', 'footing')`;
  `new(faction, strategy='line', doctrine=DEFAULT_DOCTRINE, footing='peace')`; `validate` accepts a
  record lacking the two new keys as carrying the defaults (no minted Record exists in any shipped
  world; `rosters.yaml: record_kinds.army` mirrors the six).
- `target(record, cohorts, full, others) -> {(cohort, troop_type): count}`: the doctrine's shares
  (`troop_types/presets.py::ARM_SHARES` today; `references/troops.yaml: doctrines` when MB's troop
  file lands) of each cohort's `under_arms_cap`, times the footing's share (`FOOTING_SHARE =
  {'peace': 0.25, 'war': 1.0}`, `[ASSUMPTION; medium; Jordan to correct; revert: 1.0 for both]`),
  each entry bounded by `recruit_limit`.
- `step(record, op, facts) -> ((op, args), ...)`: the primitive commands a payload-less `op` stands
  for. `recruit`: `target − by_type`, per cohort, positive entries. `discharge`: `by_type − target`,
  plus every trooper of a cohort absent from `facts.cohorts`, plus the excess over a cohort's
  present cap; unassigned first, then released from the largest subformation.
- `_apply`: an op whose `args` carry no command key runs `step` and folds its commands in order;
  `args['share']` (0.5 or 1.0, the host's, from the band) scales each count, rounding up.
- `options(q)` gains three keys beside `raise` and `advisories`: `muster_room` (bool: `step('recruit')`
  is non-empty), `surplus` (bool: `step('discharge')` is non-empty), and the three booleans proposal
  D reads. One function decides what the menu shows and what the cell asks.

**Edit 2 — `engine/season/queries/world_q.py`.**

```python
def army_state(w: World, rid: str, actor: str) -> dict:
    """The module's `options` for the army `rid` as `actor` may command it: `ArmyOptionsQuery(record,
    cohorts the actor may levy (state/gate.py::may_levy through his muster seat), full, others)`.
    The one reader the six army rows' third conjunct asks; `harness/military_menu.py::menu` calls it."""
```

`other_army_records` is unchanged (an unheld army's men are still under arms until they disperse or
are taken up; Edit 6). `data/requires.py: REQUIRES_STEMS` gains the relation stems `muster_room` and
`surplus`, asked `of: subject` and the actor (`room`'s shape), answered by `army_state`; neither is
world-only, so a refusal's read is deposited to the actor.

**Edit 3 — formation** (`engine/season/decision/options.py::opening_set`; mover).

- After `refs = row.referents_of(q)`: for a row whose class is `Record` and whose cell asks
  `existence` of a record sub-kind and `held_by` of `subject` (read off the cell,
  `data/verbs.py::_asks_subject_held`, never a verb name), keep only the referents whose
  `content:<kind>` claim in the person's own ledger is of an asked kind. New helper beside
  `held_record_claims`: `held_record_kinds(p) -> {record id: kind}` (the same read without the
  `record_sourced_operands` filter). **Declared mover** for `carry`, `comply`, `found`, `build`:
  REM-25's wrong-kind residue (2 / 3 / 2 refusals a season at seeds 0 to 2) stops.
- `[UNVERIFIED: that a minter's ledger receives `content:army` in season (WITNESS's fourth deposit,
  `loop/witness.py:823-846`, reads `newly_held`); the probe folds between seasons, where WITNESS does
  not run.]` If it does not, the mint's Event is added to `newly_held`'s sources; no other deposit
  is proposed.

**Edit 4 — the rows** (`engine/season/verb_table.yaml`). `recruit`, final text of the changed
columns (`discharge_troops` is the same with the substitutions listed under it):

```yaml
  - verb:        "recruit"
    stratum:     "uncontested_material"
    eligibility: ["remit:dispatch"]
    beneficiary: "none"
    referent_class: Record
    referent_class_note: "14-VM-C: FORMED ONLY ON AN `army` RECORD THE PERSON HOLDS -- `records_held_for_holding_rows` stamps it (`HOLDING_RECORD_KINDS` derives `army` off this cell), and `opening_set` keeps a held Record only where his own `content:` claim is of the asked kind. REVERT: delete this column; the row is hand-built only, as before."
    requires:    "the subject is an army record the actor holds, and the army may raise more men from cohorts his seat may levy"
    requires_typed:
      all:
        - form:      existence
          of:        subject
          kind:      army
          conjunct:  army
        - form:      relation
          of:        subject
          relation:  held_by
          conjunct:  command
        - form:      relation
          of:        subject
          relation:  muster_room
          conjunct:  room
    writes:
      Overwhelming: ["Record.subject_matter"]
      Success:      ["Record.subject_matter"]
      Partial:      ["Record.subject_matter"]
      Failure:      []
    writes_note: "14-VM-C: `armyrecord.apply` with `share` 1.0 (Overwhelming, Success) or 0.5 (Partial); Failure writes nothing and emits `levy.shirked`. A payload naming `cohort`, `troop_type`, `count` is one levy; none is the doctrine's step (`armyrecord.step`). The seat's right over the cohort is `state/gate.py::may_levy` (FA). [ASSUMPTION; medium; Jordan to correct; revert: the flat write.]"
    emits:
      Overwhelming: ["army.recruited"]
      Success:      ["army.recruited"]
      Partial:      ["army.recruited"]
      Failure:      ["levy.shirked"]
    emits_on_refusal:
      eligibility: ["recruit.unauthorized"]
      army:        ["recruit.refused"]
      command:     ["recruit.refused"]
      room:        ["recruit.refused"]
      write:       ["recruit.refused"]
    refusal_note: "KEYED PER CLAUSE. `room`'s read `(army, muster_room:<actor>, False)` rides the Event and is deposited to the actor, so a commander at strength does not call the levy again until he learns otherwise (REM-29's limit applies and is `01_CORE_claim_fade_as_read.md`'s to lift). `write`: a payload the module refuses (an unknown kind, a count over the cap), or a cohort the seat may not levy."
    grade:       "assumption"
```

**The `room` conjunct binds a doctrine step.** A spoken command (a payload naming cohort, kind and
count) is bounded by the cap alone, in the effect, as now: a player may raise beyond his doctrine's
shares. `[GROUNDED, 25 G-04: it cannot. A typed clause is a `form` from the closed `requires_forms`
roster with that form's fields and nothing else (`data/requires.py:1027-1030`; the classes at `:292-558`);
no clause carries a waiver or a payload condition. So `room` is asked at formation (`belief_contradicts`) and by the effect for a payload-less act,
and its refusal key is `write`. Proposal D states the same for its four rows.]`

`discharge_troops`: the same row with `relation: surplus` for `muster_room`; emits
`army.discharged` on the three upper bands and `discharge.balked` on Failure; refusal kinds
`discharge_troops.unauthorized` and `discharge_troops.refused`.

**Edit 5 — the draw and the effects.**

- `rosters.yaml: graded_inquiries.values` gains `recruit` and `discharge_troops`;
  `verb_capability` gains `recruit: command`, `discharge_troops: command`; `army_verbs` is unchanged.
- Obstacle rows (SC-B's table; `[ASSUMPTION; medium; Jordan to correct]` each):

  | verb | difficulty | modifiers |
  |---|---|---|
  | `recruit` | the kind's `muster_difficulty` (a column of the troop table; until it lands, 1 for a kind with no training Site, 2 for one with, 3 where `TRAINING_SITE`'s floor is above 0) | `cohort_resents` +1 (the cohort holds a negative stance row toward the faction; for a doctrine step, any cohort in the step) · `larder_short` +1 · `half_under_arms` +1 · `cohort_committed` −1 · `footing_war` −1 |
  | `discharge_troops` | 1 | `arrears` +1 (a live ration `shortfall` on the army's treasury) · `on_foreign_ground` +1 · `levy` −1 |

- `loop/effects_army.py`: `_eff_recruit(w, a, res)` and `_eff_discharge_troops(w, a, res)`: on
  `Failure` the band's kind is emitted and nothing is written (not a refusal: `research`'s
  `finding.none` shape); on the other bands they build `args` as now, adding
  `share` from the band and, when the payload names no command, `cohorts` (`may_levy`'s set with
  weights and sites). Every army Event carries `Observation(rid, "muster_room:<actor>", bool)` and
  `Observation(rid, "surplus:<actor>", bool)` read from `army_state` after the write, so the
  commander's belief follows his own acts.
- `data/verbs.py::act_key` and `opportunity_key`: for a verb in `ARMY_VERBS` whose operands carry a
  command key, the key gains a digest of the command (the choice suffix's shape), so the menu may
  give several spoken commands a season; a doctrine step carries none and is once a season
  (MB R-17's disposition, built).

**Edit 6 — the roll outlives its holder.**

- `loop/effects_information.py::_eff_create_record`, the `army` branch: where an unheld `army`
  Record of the minter's faction exists (lowest id), the effect opens the minter's `hold` on it and
  mints nothing (`record.taken_up`); `_army_mintable` admits it under the same conjuncts.
- `loop/matter.py`, one pass after the bodies pass, over `army` Records: for an unheld one, and for
  a held one whose `army_state(...)['surplus']` is true for troops the army may no longer keep (a
  cohort gone or shrunk), one hazard draw a Record (the bodies pass's draw shape, rate
  `Fixtures leaderless_dispersal`, swept): hold · half of the affected troops go home · all go;
  written through `armyrecord.apply('discharge', ...)`, emitting `army.dispersed` (no act). An army
  nobody plays or holds therefore melts over seasons, by chance, and not at once.

**Edit 7 — fixtures** (`data/fixtures.py`).

- `armies_at_build: "off"` (shipped) | `"empty"` (each faction's first `may_wage` leader mints an
  empty army through the fold at build, `harness/populated.py`) | `"mustered"` (today's
  `army_presets.install`, kept as a world-gen arm and no longer the unplayed commander's only path).
- `withheld_verbs` drops `recruit` and `discharge_troops` in this batch and the other four in M-D.
  With `armies_at_build: off` no one holds an army, so nothing forms.

## 4. Gate and falsifier

- **Execution artifact.** `aperture 2 s`, s = 0 to 2, `armies_at_build: empty`: `army.recruited`
  emitted by an act that passed through DELIBERATE (the act store names a chooser round, not a
  hand-built id), at every seed; `recruit`'s refusals on `room` are not repeated by the same actor
  the next season. A hand-built run on `build_realm(0)`, 200 seeds of the draw, one levy of 60: all
  four bands occur; the counts on the roll are 60, 60, 30, 0 by band.
- **State sets the odds.** The same levy by a seat whose cohort holds a negative stance row toward
  the faction, against the same seat with none, n 200 each, same-run control: the share of
  `levy.shirked` is higher for the first beyond sampling error. A reading of mechanism, not balance.
- **The successor.** The probe's death sequence re-run: after the commander's death the next
  `may_wage` leader's mint emits `record.taken_up`, `army_of` returns the old id, and the cohort's
  room is 60 less the troops still on the roll (20 in the probe), not 0 and not 60.
- **Dispersal.** A leaderless army of 600 over 8 seasons at 50 seeds: its strength at the end takes
  more than two values across seeds, and is 600 at some seed and below 600 at another.
- **Downstream read.** `seam/wrappers/mass_battle.py::_order_of_battle` returns an order of battle
  for a faction whose army an NPC raised and (proposal D) organised.
- **Control.** `armies_at_build: off`: hashes EQUAL to the base but for Edit 3's declared mover.
  The route rows removed: every levy raises its whole count (today's certainty).
- **Falsifier (planted).** `share` ignored in `_apply`: Partial raises 60. The `muster_room`
  Observation dropped: the same commander is refused on `room` in consecutive seasons.
  `may_levy` replaced by `raisable_by`: FA's seatless-member probe executes again.

## 5. What it does not do

It does not decide who goes to war or where (`march`'s formation on a defended enemy place is
PHYSICAL's and CHAR's). It writes no stores and no `weight` (J-C-2 stands; the cost is SE's three
arms). It does not add troop experience or upkeep (MB R-42). It does not lift the realm's
levy-only condition (SE's `training_endowment`).

## 6. NERS reading (E last)

- **N.** From above: armies exist because persons raised them. From below: a cohort is asked and
  answers. Laterally: `requisition`'s authority and the inquiry's roller. Diagonally: a field's
  grudge rows make the next levy harder, so a war has a memory. Remove it and force is a constant.
- **R.** Whom to call, how hard, and when to stand down are choices with a loser; a commander's
  `command` and his people's regard change what he fields; with no player, armies rise, shirk,
  balk and melt. Complete at the extremes: no seat, no levy; no commander, a slow dispersal.
- **S.** One state function for the menu and the cell; one cap; one journey of a trooper (raise,
  assign, release, discharge); the draw is the route every graded act uses.
- **E, against that.** Two record keys, two module functions, one reader, two stems, one class
  column, one mint branch, one MATTER pass. "Call the levy; a loved lord gets his men" is a
  sentence a player can use.

## 7. Cost class

Small build across three owners (MB module, FA gate, the season rows). One declared mover at the
shipped fixtures (Edit 3); the rest move only under `armies_at_build`.
