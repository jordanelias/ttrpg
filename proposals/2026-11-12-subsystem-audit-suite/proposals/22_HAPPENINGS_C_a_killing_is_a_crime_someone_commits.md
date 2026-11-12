# HAPPENINGS-C — a killing is a crime someone commits: the doer's side of the `crime` context, guarded against, noticed by a draw

## Status: PROPOSED (design-first; one ruled item touched, listed in `audits/22_HAPPENINGS.md` §4 with two readings)

Source: `audits/22_HAPPENINGS.md` §1.5 row 5, §2 rows H-03, H-21. Lane PC with FI (owners:
`rosters.yaml: violence_contexts`, `decision/options.py::VIOLENCE_CONTEXT_READERS`). Reference only
(`CLAUDE.md` §0.05).
Binds on, and does not redo: `14_VERBS_PHYSICAL_A_custody_and_force.md` (A1 warrants, A3 `context_terms`
and the mortal-wound draw), `18_DETERMINISM_notice_is_a_draw.md` (whether a deed is seen),
`16_PESSIMIST_CHAR_C_the_stop_is_the_mans.md` (the drawn refusal), `08_FI_06_testimony-names-a-hand.md`
and `08_FI_07_shortest-playable-case.md` (what an inquiry reads), `22_HAPPENINGS_B` (who is a rival for a
seat), `02_CHAR_relations_have_a_ground.md`.

## What it changes in `engine/season/` at runtime

`fight` gains one context, `enmity`: a person may form an attack on someone he has a recorded reason to
want dead **and** is hostile to. The attempt must first get past whoever guards the target, by a draw
that can end with the attacker taken. Nothing else changes: the scene, its terms, the mortal-wound draw
and the notice draw are other proposals'. A declared mover wherever the context is met; at build it is
met by nobody `[UNVERIFIED: no person at `build_realm(0)` holds both conjuncts; the gate's first reading
says]`.

## The problem (evidence)

- ED-IN-0337 (ruled, 2026-11-05): fighting *"can occur during civil war or criminal contexts"*. The built
  `crime` context (`rosters.yaml: violence_contexts`, note at `:2754-2758`) is the **officer's** side
  only: the subject is named by a warrant addressed to the actor, or is his detainee. The criminal's own
  act has no reader. So in the shipped realm nobody can commit the crime that a warrant would name.
- `fight` formed 0 at three seeds (`hole_register.yaml` row at `:5321`, cited by PHYSICAL_A); resolved 0
  in this lane's nine seed-seasons (`runs/HAPPEN/king_*.out`).
- The violence that does occur is the kind with no reason: `capture`, ungated, kills the King at seed 2
  and a Cardinal at seeds 1 and 2 (audit §1.3). PHYSICAL_A A2 closes that. Once it does, no named person
  can be killed by another for a reason of his own, at all.
- The world's own history holds the event the engine cannot produce: the first king's death in a
  hunting accident, *"perpetrator undefined"* (`audits/15_INSTITUTIONS_PAPACY.md:157`).
- FI's intent is the detective game (`AUDIT_BRIEF.md`, the noir section). FI's pessimist premise *"a
  crime leaves traces"* does not hold, and upstream of that there is no crime: every case an inquiry
  could open must be planted.
- At `51d7b05` the opposite held and was absurd (audit §1.2). The repair is not to return to it: it is
  to give violence a reason, a risk and a witness.

## The resolution, decided (for Jordan's reading; §4 item 2)

A context is one reader over the actor's own state (AX-2). `enmity` holds between actor `p` and subject
`r` when **both**:

1. *a reason*: `p` holds a dispute against `r` (`person_q.holds_dispute`, the reader `challenge` uses:
   a deed of `r`'s that `p`'s own `deeds_judged` scores against him), **or** `r` holds a seat that a
   title `p` holds may claim (`SUCCESSIONS`, in HAPPENINGS-B's list form: a rival for the seat);
2. *hostility*: `p`'s own stance toward `r` is against him (`person_q.held_against`, the reader
   `own_stance_declines` uses) at or below a fixture band `enmity_floor`.

No new relation is stored. Both readers exist; the context composes them. A man with a grievance and no
hatred, or hatred and no grievance, forms nothing.

**Getting to him is a draw.** Before the scene, where the target's place has a guard
(`world_q.guard_weight(w, rung) > 0`, IN-60), the attacker makes one graded roll through the task
route: pool his own covert faculty (the capability `conceal` reads), obstacle `guard_ob` plus the guard's
weight in steps.

| band | outcome | writes |
|---|---|---|
| Overwhelming, Success | he reaches the target; the scene is fought | as `fight` |
| Partial | he reaches him and is seen coming: the target fights at no disadvantage and the notice draw is taken as certain for those present | as `fight` |
| Failure | he is stopped. The guard's seat opens a `detain` on him (`capture`'s custody write, the same owner) | `person.captured` |

A place with no guard takes no draw. `build_realm`'s `guards` default is `False` today, so in the
shipped realm every place is unguarded until that default flips (CP-T09-07); the gate's guarded arm
builds with `guards=True`. Terms: `context_terms` gains `enmity: death` (PHYSICAL_A A3's
roster). So a ruler dies by a hand only when a rival or an injured man hates him enough, chooses it over
everything else he could do, passes his own scruple (CHAR-C), gets past the guard, wins the scene, and
the wound proves mortal (A3). Each step is a draw, and each failure is a story: a taken assassin, a
wounded king, a death with witnesses, a death with none.

## Exact edits, by owner

1. `engine/season/rosters.yaml: violence_contexts`: `fight: [war, crime, defence, enmity]` (PHYSICAL_A
   A3 having dropped `duel`); note gains the two conjuncts above and *"the doer's side of ED-IN-0337's
   criminal context (HAPPENINGS-C) [ASSUMPTION; medium; Jordan to correct; revert: drop the member]"*.
2. `engine/season/decision/options.py::VIOLENCE_CONTEXT_READERS`: one reader, `enmity`, composing
   `holds_dispute` or the rival-title test, and `held_against` against `enmity_floor`. Person-side.
3. `engine/season/rosters.yaml: context_terms` (PHYSICAL_A A3): `enmity: death`.
4. `engine/season/loop/encounter.py`, where a declared `fight` is fought: when the act's payload
   `context` is `enmity` and `guard_weight` of the subject's place is above 0, the access roll first;
   Failure writes the custody through `effects_combat._eff_capture`'s `detain` write with the guard
   seat as holder `[UNVERIFIED: which seat `guard_weight` attributes a guard to; `seat_guards` in
   `harness/populated.py` builds them per seat]` and ends the act.
5. `engine/season/data/fixtures.py`: `enmity_floor` (control: a value no stance reaches, so the context
   never holds and every base hash stands), `guard_ob` (proposed 1; sweep {0, 1, 2}). NUMBER rows in
   `hole_register.yaml`.
6. `engine/season/verb_table.yaml`, row `fight`: `emits` gains `person.captured` on the refusal side of
   the access roll; `requires_typed_note` gains one sentence.

## Gate (execution artifacts)

`engine/season/tests/test_cr87_violence_contexts.py` (the file covering the contexts):

- formation: a person with a dispute and a hostile stance forms `fight` on its subject; with either
  conjunct removed he does not (two negative controls); a rival title-holder with a hostile stance
  forms it; the same man with a neutral stance does not.
- the access roll, 200 seeded attempts on a guarded target: all three outcomes occur; with
  `guard_weight` 0 no roll is taken.
- realm, seeds 0 to 7, four seasons, the context on: the count of `fight` formed under `enmity` is read
  and reported. **Acceptance is a band, not a floor: fewer than one attempt per seed-season on average,
  and more than zero across the eight seeds.** Zero means the context is dead and the floor is wrong;
  one a season means §1.2 of the audit has returned.
- no death of a seat-holder in season 0 at any of the eight seeds.

## Falsifier

Set `enmity_floor` to admit every stance: the realm gate's upper bound fails (the instrument can see
the old regicide). Remove the access roll: the 200-attempt arm shows no `person.captured`.

## What it does not do

It writes no plot (several persons acting together is `conspire`, unbuilt, and not proposed here), no
poison, no accident and no hired hand. It does not name a ruler: a guard is whatever `guard_weight`
reads for any place.

## NERS reading

- **N.** Cut it and there is no crime to investigate and no ruler who fears for his life; FI's cases and
  the succession lanes' crises have no natural beginning. Top-down: the ratchet toward civil war
  (ED-IN-0339) has a step between a hard word and a march. Lateral: the officer's half of `crime`
  gets its other half.
- **R.** Guards become worth posting and enmities worth mending: both are things a player can do about
  it. Unwatched, the world produces attempts, captures and a few deaths that differ by seed.
- **S.** One more reader in a closed set; one roll on the task route; custody by the existing owner.
- **E, last.** One context, one roll, two fixtures.

## Cost class

Design-first, then a small build. Lands after PHYSICAL_A A3 and A1, CHAR-C, and HAPPENINGS-B edit 2.
