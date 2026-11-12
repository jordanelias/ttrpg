# COLONIAL-B — distance: one obstacle term, four acts that become draws, a border news does not cross, and the superior beyond the map

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-13, X-14, X-20, X-24, X-26 to X-28) — the four rows of §2 belong to their verb lanes and this file supplies `remove` to each: `requisition` and `transfer` are `14_VERBS_MATERIAL_B_stores.md`'s (so `levy_ob`, the `stewardship` rows, the half-amount Partial and the reuse of `requisition.refused` for a failed levy are withdrawn; the Failure kind is `requisition.resisted`; every `transfer` is drawn, at the floor obstacle in the room); `seize` is `14_VERBS_MATERIAL_D_paper.md`'s; `issue` is `14_VERBS_BINDING_D_orders.md`'s one roll, whose `force` band this file's four delivery outcomes read; `oath_step` is the term `obligation`. `carriage` (the MATERIAL lane) and `distance` (the SOCIAL1 lane) are the same quantity as `remove` and are listed for those lanes. The far superior is one seat shared with `15_INSTITUTIONS_BYZANTINE_D`: `off_altonian_court` as written here, with a placeholder post (not "Logothete"), the Doux as its hand, and `factions.head_seat.Altonia`. `remove`, `world_q.remove`, its two fixtures, the reach rows, the border rule and the ending row stand. Every finding below stands.

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_COLONIAL.md` §3, §8, §12 batch C-2, §13 (M-ABROAD:
`audits/12_ARCS_adjudication.md` rank 13 and §6 row 12, "none written"). Depends on and does not redo:
SC-B (`proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`, the obstacle form and its closed
`obstacle_terms` roster); CR-29 (`workplans/valoria_master_workplan_v11_part4.md:118-129`, the reach
channel); FA-P6 (`06_FA_office_capabilities.md`, how a vocation is added); the MATERIAL and BINDING verb
lanes for the final row text of `requisition`, `transfer`, `seize` and `issue`. Nothing is ratified by
being written.

**Standing rule honoured (AUDIT_BRIEF, "We do not do deterministic"):** each of the four acts below can
go either way for the people in the fiction and is therefore a draw; state sets the odds. The control
arms reproduce today's *odds inputs*, not today's certainty: **these rows are declared hash movers.**

## What it changes in `engine/season/` at runtime

1. `requisition`, `transfer` between two places, `seize`, and `issue` to an addressee who is not where
   the issuer is, are rolled on the one roll form and have four graded outcomes.
2. Every roll made through a seat on something in another territory carries one more obstacle term,
   `remove`.
3. No reach row admits a person under a different root rung from the Event; inside a root, a binding
   decision reaches the exercised seat's purview. (Rows for CR-29's map; inert until CR-29 lands.)
4. `build_realm(foreign=True)` seats one more foreign seat, above the Katepano and the Kommerkiarios, at
   a second foreign settlement; their two seats become `appointed` and strippable from it.
5. The `endings` roster gains one non-victory row.

## The problem (evidence)

- `epistemic.py::_ch_chronicle` (`:649-686`): "when it fires it fires for everyone alive"; the only
  `told_by` source in the realm (879 claims a season, 0 with it off, measured in its own docstring).
- `verb_table.yaml` (audit E-3): `requisition`, `transfer`, `seize`, `issue` have no `contests:` and a
  flat `emits:`. A levy three territories from the actor is as certain as one in the room.
- Altonia's two seats: `conferral: None`, `revocation: None` (`offices.yaml:607-632`; audit E-1); the
  empire's persons answer to nobody; ARCS: "the home authority above them is not a person".
- `goals.yaml:466-483`: the Katepano's march "arrives `field.unopposed`" at the chokepoint, and
  `workplans/…v11_part5.md:140-141` holds "perception channels at the border" open on CR-29.

## The resolution, decided

### 1. `remove` (ladder step 5; SC-B's roster is the precedent for the shape)

`engine/season/queries/world_q.py::remove(w, place_a, place_b) -> int`: territory hops on the shortest
path over `data/geography.py::adjacent_territories()` between the territory rung containing `place_a` and
the one containing `place_b` (0 within one territory), plus `border_hops` when the two places lie under
different root rungs. A foreign root with no edge in the geography file is entered at the nearest
territory the file's `altonian_passes` names (for `terr_ALT`: T3 or T10, whichever is nearer `place_a`);
`terr_T16` has its own `coastal` edge to T1. Cached per process as `adjacent_territories` is (the graph
is repository content). The pass lookup reads `geography()["altonian_passes"]`, never a literal.

`rosters.yaml: obstacle_terms` (SC-B edit 1) gains `remove` after `stakes`. `modules/social_contest/
roll.py::obstacle` sums it inside the bound as a hostile term; the host carries the raw hop count
(`queries/inputs.py::SocialContestInput` gains `remove: int = 0`, set by `seam/wrappers/sigma.py::
contest_input` from the **actor's** `place_of` and the place of the act's subject or `to`
[UNVERIFIED: the wrapper's present signature; SC-B's implementation lane fixes it]).

`data/fixtures.py`: `remove_step = 0.25` (Ob per hop; sweep {0, 0.25, 0.5}); `border_hops = 2` (hops;
sweep {1, 2, 3}); table `levy_ob` beside SC-B's `stakes_ob` (keyed by the share of the source store an
act moves: `quarter` 0, `half` 0.5, `more` 1.0; sweep each entry ×{0, 1, 2}). Each a NUMBER row in
`hole_register.yaml`, graded `assumption`.

### 2. The four graded rows

Each row gains `difficulty:` (SC-B's column), a `capability:` by FA-P6's pattern, band-keyed `writes:`
and `emits:` (the table's own band-keyed cell shape, as `tell`'s), and enters `rosters.yaml:
graded_inquiries`' route to `social_contest.roll` (the roster's name is inquiry-specific; DICE's
`10_DICE_one_roller_one_fraction_rule.md` is the proposal that generalises the route, and this file
follows whatever name it lands [UNVERIFIED: not opened]).

| row | `difficulty` | `capability` | terms beyond difficulty | Overwhelming | Success | Partial | Failure |
|---|---|---|---|---|---|---|---|
| `requisition` | routine | `stewardship` | `remove`; `stakes` = `levy_ob[share]`; `regard` of the levied place's cohort toward the actor (`stance_toward`, SC-B's term, the cohort being a Person); − `evidence`: a held `faction_sheet` naming the place among its holdings; a live instrument conferring the exercised seat that the cohort's ledger holds a claim of | `amount` moves; `requisition.taken`; the actor is deposited a firsthand claim of the store's remaining size | `amount` moves; `requisition.taken` | `amount // 2` moves; `requisition.taken` | nothing moves; `requisition.refused` (the existing kind), witnessed as any Event |
| `transfer` where `remove(from, to) ≥ 1` | plain | `stewardship` | `remove(from, to)`; `stakes` = `levy_ob[share]`; + 1.0 if any territory on the shortest path holds a faction `world_q.at_war` with the actor's | `amount` arrives | `amount` arrives | `amount // 2` arrives; the rest stays at `from` | nothing moves; `transfer.refused` |
| `seize` | demanding | `stewardship` | `remove`; `regard` of the present holder; `stakes` = `stakes_ob[the Tenure kind it closes]`; − `evidence`: the warrant held (`warrant_sourced`) | as today's effect | as today's effect, and the dispossessed is deposited a content claim of the warrant (a ground to `petition` on) | the subject's present `hold` gains a term of one season (`Tenure.term`, the existing clock) and nothing changes hands | `seize.refused` [UNVERIFIED: the row's present refusal kind] |
| `issue` where the addressee is not co-located with the actor | routine | `copying` | `remove`; `opposition` (addressee's score ÷ 2, SC-B); `regard` of the addressee toward the issuer; − `oath_step` (0.5; sweep {0, 0.5, 1}) if the addressee holds a live sworn `oblige` to `Act.via` | the terms are deposited to the addressee (FA-P1 edit 2's deposit) **and** to every person co-located with him, so a later answer is attested | the terms are deposited to the addressee | the terms are deposited and `construe` forms for the addressee on this writ (its row's existing formation, keyed on the claim) | the addressee is deposited that a writ exists and not its terms |

Conservation holds in every band (`_shift`'s arithmetic is untouched; a Partial moves a smaller amount).
A `transfer` with `remove` 0 (inside one territory) and an `issue` to a co-located addressee are **not**
rolled: handing over in the room is bookkeeping. Upkeep renewal (`_renewals`) counts what **arrived**.

`stewardship`: `rosters.yaml: verb_capability` rows `requisition`, `transfer`, `seize` → `stewardship`;
`vocation_attribute: stewardship → attr.mind.focus` `[ASSUMPTION; medium; Jordan to correct; the name and
the attribute; revert: the three rows and this one together]`. With nobody holding the key each rolls
`pool_default`, FA-P6's shipping state.

**For FA (owner of `06_FA_decree_binds.md`):** that proposal's edit 2 is unconditional. The `issue` row
above gates it on the band. This file does not edit FA's; it states the form.

### 3. Reach rows (content for CR-29's kind→reach map; no code here)

- A reach value `purview`: persons at a place the exercised seat's purview reaches
  (`state/gate.py::purview_reaches`, asked of `Act.via`). Proposed for `dispensation.issued`,
  `order.given`, `date.scheduled`, `office.established`, `requisition.taken`, `rung.seized`.
- CR-29's own text keeps realm reach for `tenure.closed` and `person.died`. Proposed narrowing: realm
  reach **within the Event's root**.
- The border: no reach value admits a person whose place is under another root than the Event's place.
  `engine/season/epistemic.py`'s reach predicate asks `world_q.root_of(place)` equality first
  [UNVERIFIED: whether a root reader exists by that name; `foreign_cast`'s note defines the root as the
  territory with no `contain` edge into `r_valoria`].

### 4. The superior beyond the map (M-ABROAD)

- `rosters.yaml: foreign_cast.by_faction.Altonia` gains `capital: {code: ALT-0, hops: 3}`, a second
  settlement under `terr_ALT`, with its distance from the frontier settlement **declared in the roster
  that mints it** (the geography file has no Altonian interior, and adding edges to canon's map for a
  place canon does not name would forge canon). `world_q.remove` reads `hops` when one place is that
  settlement and the other is not `[ASSUMPTION; the code and the 3; Jordan names the place; sweep
  {1, 3, 5}]`.
- `offices.yaml: foreign_seats` gains

```yaml
  - id:         off_altonian_court
    post:       "Logothete"            # [ASSUMPTION; a placeholder; the post's name is Jordan's]
    rung:       {territory: "ALT"}     # the root rung, so `rung_above_same_faction` can reach the two
                                       # settlement-rung seats (`seated_on_the_rung_above` needs the PARENT rung)
    body:       null
    faction:    "Altonia"
    remit_acts: [issue, confer, revoke]
    conferral:  null
    revocation: null
    holder:     "NPC-091"              # a new registry row, `status: proposed`
    obligees:   ["NPC-089", "NPC-090"]
    source:     "audits/12_ARCS_adjudication.md §6 row 12 (\"the superior is one seated person with one seat outside the map's rungs\"); ARC-38 N2, NPC-089 N6"
```

  and the two existing rows change `conferral: null → appointed`, `revocation: null →
  rung_above_same_faction`. `rosters.yaml: faction_leaders.Altonia` stays NPC-089 `[ASSUMPTION: the
  empire's head *on this frontier*; the court seat is her superior, not the faction's `head_seat`]`.
- `references/npc_registry.yaml`: one row, NPC-091, `faction: Altonia`, the fifteen pursuits and the
  three concern affiliations as `data/cast.py` requires, `status: proposed` `[ASSUMPTION; whole row]`.
- `goals.yaml`: `goal_altonian_court_frontier_quiet`, `org: {seat: off_altonian_court}`, `object:
  {kind: orientation}`, `pursuits: {stability: 0.6, wealth: 0.4}`, `derives: {from:
  goal_altonia_conquer_valoria, kind: influences}`: a court that wants revenue and quiet above a governor
  who wants honour is the structural conflict, authored as two persons' pursuits and nothing else.
- The holder **resides at `ALT-0`** (the cast row's placement), so every order he issues to the frontier
  is rolled at `remove` 3 and every report reaches him only by a person who travels: the seat's rung
  gives the authority, the holder's place gives the distance. NPC-091 is the next free cast id (the
  registry's last row is NPC-090; 46 rows, checked).
- The `[UNVERIFIED]` root reader in §3 has no existing owner (`grep "def root_of" queries/world_q.py`:
  none); it is the last element of an `ancestry(place)` walk (a method of that name is at
  `queries/world_q.py:4960`; its class was not opened) and should be written once, beside `place_of`.

### 5. A non-victory ending

`rosters.yaml: endings.members` gains `reabsorption: {victory: false, holds: {post: King}, under:
Altonia, source: "by `theocracy`'s precedent (#457 D6): an endpoint, not a victory"}`
`[ASSUMPTION; medium; Jordan to correct; revert: drop the row]`. No reader changes: `endings_reached`
already evaluates a `{post:}` selector under a faction.

## Gate (execution artifact)

- `engine/season/tests/test_remove.py`: `remove` is 0 within a territory, symmetric, equals the
  breadth-first distance on the file's edges for three hand-checked pairs (T1–T2 1; T1–T13 by the file;
  T3–`ALT-1` `border_hops`), and is independent of `radiation_bands` (IN-35's control, kept).
- **The draw is a draw:** for one hand-built levy, 400 seeded rolls at `remove` 0 and 400 at `remove` 4
  (`PYTHONHASHSEED=0`, seeds 0–399). Printed: band shares for each arm. Pass: Failure's share is higher
  at 4 than at 0, **and each arm contains at least three of the four bands** (state sets odds, never the
  outcome). Control: `remove_step: 0` makes the two arms' shares equal within sampling.
- Border: `build_realm(0, foreign=True)`, one season (after CR-29): no person at `set_alt_1` or `ALT-0`
  holds a claim of a realm Event of this tick whose `chain` is empty and whose source is `told_by`.
- M-ABROAD: over seeds 0–4, four seasons, the report prints every `dispensation.issued` through
  `off_altonian_court`, the band it rolled, and the Katepano's next act. Pass: at least two different
  bands occur across the seeds.

## Falsifier

- Planted: make `remove` read the seat's rung instead of the actor's place; a king standing in Oastad
  then levies it at the capital's odds and the hand-built "progress" assertion reddens.
- Planted: force the roll's band to Success; the "three of four bands" assertion reddens in both arms.
- Crowd-out (rule V2, as FA-P1 states it): executed counts of `requisition`, `transfer`, `issue` pooled
  over realm seeds 0–2 are printed before and after; a fall is reported, not asserted against.

## What it does not do

No transit time, no message queue, no road speed, no loss of matter in transit (a failed convoy stays
home), no piracy, no weather. No change to `march` (a field is already a draw). No Schoenland seat (the
merchant-republic lane's and IN-36's residue).

## NERS reading

- **N.** From above: a ruler must travel or delegate. From below: a far village is harder to squeeze.
  Lateral: two neighbours trade more surely than two ends of the realm. Diagonal: an Altonian order
  to a frontier governor may arrive open to reading. Remove `remove` and distance costs nothing.
- **R.** Strategy (where to stand, whom to seat, how much to ask); the world generates the governor who
  did not get the letter with no player; complete at the extremes (0 hops is today's act; the bound caps
  the far end so nothing is impossible).
- **S.** One term on SC-B's one form; the same four bands; zooms from a hearth's transfer to a realm's
  tribute; pauses nothing. It **removes** an S defect: certain material acts beside rolled social ones.
- **E, last.** One Query, one roster member, three fixtures, four row edits, some content. Against it:
  four hash movers and a dependency on SC-B. The ratio holds only if SC-B lands first.

## Cost class

Small build (the Query and term); the four rows are a second small build with declared re-pins; content
edits for the reach rows, the court seat and the ending.
