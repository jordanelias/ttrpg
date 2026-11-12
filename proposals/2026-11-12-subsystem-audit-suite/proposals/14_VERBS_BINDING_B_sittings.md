# VB-B — the room: one sitting per seat, a judge asked only about the parties before him, mercy only for the restrained and only by a draw

## Status: PROPOSED

Source: `audits/14_VERBS_BINDING.md` §0.1, §0.2, §2 (`convene`), §3 (`determine`), §9 (`pardon`); batch B.
Binds on: `05_SC_acquittal.md` (SC-P6), `05_SC_arrangement_rows_that_bind.md` (SC-P4),
`05_SC_playable_hearing_B.md`, `05_SC_obstacle_difficulty_and_modifiers_B.md` (SC-B). Those own the room,
the bands and the obstacle; this file edits none of their content.

## What it changes in `engine/season/` at runtime

1. A convened Date's id salts the exercised seat, so one man convening one venue through two seats in a
   tick makes two sittings, not a collision refused as a no-op.
2. `determine` forms only on a party docketed at a fired sitting before the asker's bench (a named class
   `Party`). Today it forms on any plain referent, a Rung included.
3. `pardon` forms only on a person restrained (`detain` or `ban`) on a seat the asker holds granting
   `determine` (a named class `Restrained`), and becomes contested: the restraint ends by a draw.

Each is a declared hash mover where it bites; (1) moves only where the collision occurs (one act at seed 1
realm in two seasons).

## The problem (evidence)

- `convene`: `aperture 2 1` refused 1; the probe: `p_npc_020` convened `set_s_015` through
  `off_duke_valorsmark`, then through `off_king`, same tick; `_eff_convene` (`loop/effects_governance.py:450`)
  salts `H(seed, tick, actor, "convene:{venue}")`, so the second finds the first and moves nothing.
- `determine`: seed 0 refused 2 at `docket`; seed 1 refused 3 (`docket` 2, `party` 1); the probe: a
  Rung (`b_s_003_market`) taken as party, a man not yet docketed, and the Widow Regent determining the
  Confessor. The row declares no `referent_class` and forms on plain referents.
- `pardon`: seed 0 formed 8, attempted 0; seed 1 realm 1 refused after admission (the Cardinal of Justice
  on a man restrained nowhere); spine 5 refused. The row forms on any person.
- `pardon` frees with certainty once admitted, which the standing rule forbids.

## The resolution, decided

Formation from the occasion that makes the act meaningful, on `Detainee`'s precedent (ladder step 4: a
named class stamped by the one standing occasion that computes the world fact). The bench's own
`sittings_before` (`queries/world_q.py:308`) already computes who is before whom; the gate's own
`restrained` (`world_q`) already says what a restraint is. **CR-56's RL2 caution is taken**: narrowing a
verb whose score is matter-blind can lower its executions; each gate below measures executions, not only
refusals.

`pardon` is drawn (audit §0.2): prize `a matter` (the existing row), obstacle `difficulty` `routine` +
`stakes` (the restraint kind, SC-B's `stakes_ob`) + `standard` (the disposing arrangement's) +
`reception` (the bench). Partial commutes.

## Exact edits, by owner

**Commit B1 — `convene`.**

1. `loop/effects_governance.py::_eff_convene`: `did = H(w.world_seed, w.tick, a.actor,
   f"convene:{a.via or '-'}:{venue or '-'}")`. Docstring: the G4 paragraph's *"a SECOND identical
   convening by the same person at the same venue"* gains *"through the same seat"*.

**Commit B2 — `determine` formation.**

2. `data/verbs.py`: `PARTY_CLASS = "Party"`, checked against `REFERENT_CLASSES` as `DETAINEE_CLASS` is.
3. `rosters.yaml: referent_classes`: add `Party`; note: *"`Party` (VB-B): a person on the docket of a
   fired sitting before the asker's bench (`world_q.sittings_before`); stamped explicitly;
   `determine` declares it."*
4. `queries/world_q.py`: `parties_before(w, p) -> tuple`: the persons in the matters of
   `sittings_before(w, p)`, in docket order, deduplicated. `questions_for`: append `((m, PARTY_CLASS) for m
   in parties_before(w, p))` to the classed tuple.
5. `verb_table.yaml`, `determine`: `referent_class: Party`, with a `referent_class_note` naming VB-B and
   its revert (delete the column). The typed cell is unchanged: `party` and `docket` stay conjuncts (the
   fold's check against the world it left; a matter disposed earlier in the round still refuses).

**Commit B3 — `pardon` formation.**

6. `data/verbs.py`: `RESTRAINED_CLASS = "Restrained"`, checked as above.
7. `rosters.yaml: referent_classes`: add `Restrained`; note: *"`Restrained` (VB-B): a living person with a
   live restraint (`RESTRAINT_KINDS`) whose object is a seat the asker holds granting `determine`;
   `pardon` declares it. `Detainee` stays `detain`-only, for `interrogate`."*
8. `queries/world_q.py`: `restrained_on_seats(w, p) -> tuple`, `detainees_held`' body with
   `t.kind in RESTRAINT_KINDS` for `t.kind == DETAIN_KIND`; `questions_for` appends its pairs to the
   classed tuple.
9. `verb_table.yaml`, `pardon`: `referent_class: Restrained`, note naming VB-B and the revert.

**Commit B4 — `pardon` drawn.**

10. `verb_table.yaml`, `pardon`:
    ```yaml
    contests:    "a matter"
    difficulty:  routine
    writes:
      Overwhelming: ["Tenure.until"]
      Success:      ["Tenure.until"]
      Partial:      ["Tenure.until"]
      Failure:      []
    emits:
      Overwhelming: ["detention.ended", "ban.ended"]
      Success:      ["detention.ended", "ban.ended"]
      Partial:      ["detention.ended"]
      Failure:      ["pardon.denied"]
    ```
    `emits_on_refusal: ["pardon.refused"]` stays. The man pardoned is no opponent: the row declares no
    `counterparty` and SC-B's `opposition` term is absent.
11. `loop/effects_governance.py::_eff_pardon`: at `Partial`, close only the `detain` edges (a ban
    stands: commutation); else unchanged. `_RESTRAINT_ENDED` is read per band from the row's `emits`
    (the `Partial` list has one kind), so no kind is spelt in the effect.
12. `seam/wrappers/sigma.py::contest_input`: `stakes` keyed by the restraint kind being closed (the
    heaviest live one on the seat), `standard` from the arrangement that disposed it when the docket
    records it, else `plain`; `reception` over the seat's bench (`judging_set`).

Order: B1 (independent), B2 and B3 (independent of SC), B4 after SC-B. SC-P6 and SC-P4 land on
`determine` in their own order; nothing here waits on them.

## Gate (execution artifact)

- B1: `aperture 2 1` realm: `convene.refused` 1 → 0, `date.scheduled` 12 → 13, the new Date's `holder`
  `off_king`.
- B2: `aperture 2 0` and `2 1`: `determine.refused` keyed `party` and `docket` → 0; `matter.determined`
  not below 0/1. If executions fall (RL2's mode), the reading is recorded and B2 is held, not shipped.
- B3: same: `pardon` formed → 0 persons and `pardon.refused` → 0 while no restraint is live.
- B4: hand-built world with one `detain` and one `ban` on a bench seat (the `interrogate` tests'
  fixture), 40 seeds: Partial ends the custody and keeps the ban; Failure ends nothing and emits
  `pardon.denied`; the act re-forms next scene.

## Falsifier

- B1: revert the salt: the collision returns.
- B2: stamp every plain referent as `Party`: refusals at `party` return.
- B3: widen `restrained_on_seats` to every person: refusals return.
- B4: pin the roll: one band only.

## What it does not do

It does not build the room (hearing B), the bands' consequences (SC-P4), the acquittal (SC-P6) or the
obstacle (SC-B). It does not decide when a standing court stops sitting (`sittings_before`'s *"ONE CONVENE
IS A STANDING COURT"*), which is SC's.

## NERS reading

N: without B2 and B3 a judge spends scenes on men not before him; without B4 mercy is a switch. R:
commutation is a third outcome that the world can produce unwatched. S: two named classes on the one
`Detainee` route; one roll owner; one restraint reader. E (last): three formation reads and one band map
remove every observed refusal in three rows.

## Cost class

Small: one salt, two classes and their stamps, one band-keyed row, one effect branch.
