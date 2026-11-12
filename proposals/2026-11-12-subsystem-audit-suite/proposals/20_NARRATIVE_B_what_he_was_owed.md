# NARRATIVE-B — what he was owed: a due that lapses unmet is a grievance against the one he believes owed it

## Status: PROPOSED

Source: `audits/20_NARRATIVE_CHURN.md` F-NARR-02 (an omission has no author), F-NARR-03 (an office owes
nothing), §2 edges B2 to B6, B10; §7.2 generator G1. Reference only (`CLAUDE.md` §0.05). Not ratified by
being written.

## What it changes in `engine/season/` at runtime

`person_q.regard(p, x, fx)` gains one term, `− dues_valence × dues_unmet(p, x)`. At `dues_valence 0` (the
control, shipped in the first commit) the function is today's exactly and every hash is EQUAL. At a live
value it is a **declared hash mover** for every world in which a termed oath has lapsed unpaid and the
sworn person holds a belief about who held the seat (which needs `20_NARRATIVE_C_who_holds_what.md`;
without it `dues_unmet` is 0 for everyone and nothing moves). No Event, carrier, verb or write is
added; MATTER's lapse is untouched (T-n stands).

## The problem, with evidence

A demand unmet, a duty failed and an oath not kept are the absence of an act. The log holds acts.

- An unpaid `oblige` closes at MATTER with `subject = the edge's id` and `causes = [the oath]`
  (`loop/matter.py:428-435`): it cites the sworn man's own act and names nobody who owed him.
- A docket item lapses with `matter.lapsed`, cause the Event that docketed it (`:437-…`, CR-55).
- WITNESS deposits a non-`hold` edge by its Tenure id (`queries/world_q.py:5403-5406`), and an actorless
  Event's sighting names no one (`epistemic.py:1049-1066`), so `person_q.deed_doer` can pair a lapse with
  no doer; `deeds_judged` says of this very case "THE SWORN-TO HALF IS NOT BUILT … what is missing is the
  PAIRING, not the edge" (`person_q.py:121-126`).
- S19.3 (`state/carriers.py:276-290`) rules that an Event carries no actor and no target: attribution is a
  per-witness claim. So the door a lapse is laid at cannot be a field of the Event.
- Read over three seeds, four seasons (audit E-N04): 46 / 39 / 89 oaths sworn in play, `term.renewed` 0,
  `transfer` executed 2 / 3 / 7 of 98 / 129 / 108; petitions filed 35 / 44 / 44, determined 0 / 2 / 0;
  writs 40 / 23 / 47, complied 0. At season five the oaths lapse together (`tenure.closed` 27 and 27 at
  seeds 0 and 1, WR addendum §3.2). Nobody is blamed for any of it, by construction.
- The plan's own owner of grievance, CR-88's `person_q.grievance_against(p, q)` (design-first, B10-17b),
  counts "the deeds by `q` … that `p`'s `deeds_judged` scores against" him: acts only.

## The resolution, decided

**The wronged man does the attributing, from what he himself holds.** His own oath is in `p.tenures`
and outlives the lapse; whether it ended by its own term is on the edge; who sat in the seat is what he
believes (`held_by`, proposal C). So "my lord let my service lapse" is a person-side reading of own
state, lawful under AX-2 and S19.3 both, and needs no new Event and no world read.

Ladder: step 3 (ED-IN-0345, ruled: a clock is an accumulation of world events, and nothing may move from
the bare absence of an act; FA's adjudication of ARC-01 and ARC-03 restates "inaction" on the Events
that already mark it, `06_FA_audit.md` §13) for *what counts*: the lapse Event MATTER already writes.
Step 4 for *where it is read*: `regard`'s `judged` half is the precedent for a derived, never-stored
judgement of a person. Step 5 for the form: one pure function with two callers.

Nothing here decides an outcome. The term moves how the aggrieved man ranks acts toward one person;
which act he takes is his sampled choice (`choose.py::_sample_order`), and whether a petition, a
challenge or a hearing then goes his way is that act's draw (`13_SC_draw_for_unrolled_contests.md`,
`14_VERBS_BINDING`). A lord in good standing who misses a payment is resented and usually forgiven by
the dice of what follows; one who is already hated may find it the last straw. Neither is certain.

## Exact edits, by owner

**1. `engine/season/queries/person_q.py` — new, beside `held_against`.**

```python
def dues_unmet(p: Person, x: str) -> int:
    """HOW MANY OF `p`'S OWN DUES LAPSED UNMET AT `x`'S DOOR: his own `oblige` edges (`p.tenures`) that
    carry a `term` and ended at or after it (`until >= term.matures_at`: MATTER's closure; a `release`
    ends an edge before its term and is his own act, not a due unmet), whose seat he BELIEVED `x`
    held when it lapsed -- his newest `held_by` claim on that seat with `when <= until`
    (`believed_holder`, proposal C's reader). Each edge once. 0 for a seat he holds no such belief
    of: a man who does not know who failed him blames no one. Person-side, own state and own ledger
    only (AX-2); nothing is stored (T-a)."""
```

**2. `person_q.regard`** (`:424-453`): after the `judged`/`told` block,

```python
    dv = float(fx.get("dues_valence"))
    if dv:
        stored -= dv * dues_unmet(p, referent)
```

with the `>= 0` refusal the other gains carry. The docstring's formula gains the term.

**3. `engine/season/data/fixtures.py`.** `dues_valence=0.0`, swept `0` (control) / `2` / `4` (a stance
row's valence is −5 to +5 at weight 1; 2 is a moderate grievance per lapsed oath, 4 a heavy one), with a
`hole_register.yaml` NUMBER row, `[ASSUMPTION; medium; Jordan to correct; revert: 0.0]`.

**4. CR-88's design file, when it is drafted** (not an edit to code here): `grievance_against(p, q)`
adds `dues_unmet(p, q)` to its count of distinct origins (one lapsed edge is one origin, ED-IN-0322),
so an unpaid oath can help clear the betrayal band exactly as a deed can. One function, both callers.

**5. Not edited here, owed and named.**
- *Petitions.* The same count should read a petition that lapsed unanswered against the believed holder
  of the seat it waited on. It needs the lapse to reach the filer as a claim about his petition Record
  (`matter.lapsed`'s write names the docket item; what its deposit's subject is was not opened,
  `[UNVERIFIED]`). Interface for SC (`13_SC_*`, WR `_B` step 3 "a matter about to lapse is an
  occasion"): the lapse's deposit names the petition Record. Then `dues_unmet` gains a second clause.
- *Writs.* A writ ignored is the issuer's grievance, and `06_FA_decree_binds.md` already folds it from
  the issuer's own claims of defied writs into a recall. No second rule.
- *The debtor's side.* That the bill reaches the one who must pay it before it lapses is
  `15_INSTITUTIONS_BYZANTINE_B_the_roga_and_the_fisc.md` (a shortfall claim on the holder) and
  `01_CORE_unmet_need_is_attended_first.md` (he attends to it first). With those, neglect is a choice he
  made; without them it is an accident, and this proposal still blames him for it.

## The gate that shows it worked (execution artifacts)

Seeds 0, 1, 2, six seasons (the shipped terms are four), `PYTHONHASHSEED=0`, with proposal C live:

1. Control: `dues_valence 0` reproduces the base hashes.
2. At `dues_valence 2`: persons with `dues_unmet(p, x) > 0` for some `x`: more than zero at every seed;
   the holders blamed number at least three at two seeds, and no holder draws a larger share of the
   grievances than his share of the seats sworn to plus the seed spread (a non-degenerate distribution:
   it follows who was sworn to, not one name).
3. A **paid arm**: the same world with half the lapsing oaths renewed by a planted `transfer` the season
   before. Grievances appear only among the unpaid half. (The term reads the due, not the seat.)
4. Executed acts by an aggrieved person whose subject is the holder he blames, in the two seasons after
   the lapse, by verb, against the control arm: at least one of `petition`, `speak`, `tell`, `challenge`,
   `release` differs by more than the control's seed-to-seed spread.
5. The story reading of `20_NARRATIVE_F` prints class G1 (a due unmet, answered) above zero at two seeds
   and zero in the control.

## The falsifier

- Gate 2 at zero: nobody sworn believes anything about who held his seat (C did not land, or its
  seeding reached nobody), which is a finding about C.
- Gate 4 with no verb moved: the grievance has nothing to ride. That is the closing verbs' refusals
  (`challenge` 0 of 152 / 180 / 174, audit E-N04; PC and SC own them), and this term then ships at 0
  until one executes.
- Gate 2 with every grievance on one holder at every seed: the oaths of the built realm all point at one
  seat, and the content (who is sworn to whom) is what is degenerate.

## NERS reading

- **N.** Cut it and three of Jordan's five crossings (a demand unmet, a duty failed, an obligation
  meeting a new holder) leave no mark on anyone: the realm's commonest ending stays nobody's fault.
  Bottom-up it is one man's memory of one oath; top-down it is how an institution's decay becomes
  politics; lateral, CR-88 reads the same count; diagonal, it is what makes BYZ's stipend matter.
- **R.** No player is needed: a lord who cannot pay loses standing with nobody watching. Complete at
  the extremes: no oaths, no term, or no belief about the holder each read 0.
- **S.** One methodology with `regard`'s other terms (a derived number, a gain, a control at 0); no
  second ladder of grievance beside CR-88's.
- **E, last.** One function, one line in `regard`, one fixture; against the absence of any consequence
  for neglect. High. It makes a complex outcome ("the unpaid households turned on him") follow from a
  simple, legible fact a player can act on (pay your men).

## Cost class

Edit. After `20_NARRATIVE_C`. One session with its sweep and the paid arm.

## Dependency edges

- **Needs:** `20_NARRATIVE_C_who_holds_what.md` (`believed_holder`).
- **Feeds:** CR-88 (B10-17b); `20_NARRATIVE_F` class G1.
- **FA:** `06_FA_seat_terms_and_turnover.md`, `06_FA_seat_terms_by_body_B.md` (a seat that changes
  hands changes whom the next lapse is laid on); `06_FA_decree_binds.md` (the writ half).
- **INSTITUTIONS:** `15_INSTITUTIONS_BYZANTINE_B` (what is owed and the bill), `15_INSTITUTIONS_VENICE_A`
  (the same live edge as an obstacle term while it holds: arrears there, a grievance here once lapsed).
- **CHAR:** `02_CHAR_relations_have_a_ground.md` (its `service` and `oath` grounds seed a stance row at
  build; this term is what service unpaid later does to it).
- **SC:** the petition clause (edit 5).
