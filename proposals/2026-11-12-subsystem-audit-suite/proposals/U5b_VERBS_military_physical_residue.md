# U5b · VERBS — the MILITARY and PHYSICAL rows under the rulings: the shape of a drawn act, the one sampler, `march` and `raze` under the land ruling, and what no file carried

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Author: U5b closure lane (Fable), 2026-11-12. Read at `6910680`. Applies to
`14_VERBS_MILITARY_A…D_*.md` and `14_VERBS_PHYSICAL_A…D_*.md` (each carries a `Reconciled:` line pointing
here). Carries Jordan's A-5, A-6, A-7, A-25, A-57, A-58 and the ladder-closed D-25 and D-36; the Layer 1
row those proposals crossed (`04` §B.13 invariant 12 and §C.4); and three items of
`audits/14_VERBS_PHYSICAL.md` that were grounded after writing and had no edit. The land ruling's owners
are `U5d_FA_land_and_seats_pass_on_a_won_march.md` (the title write, consent) and
`26_MASS_BATTLE_aggression_and_land.md` (the end state); they are cited, not restated. Reference only
(CLAUDE.md §0.05).

## What it changes in `engine/season/` at runtime

§1: the shape in which eighteen rows declare their draw, with no change to which band does what, except
where a row says so. §2: a march on a neighbour who is not yet an enemy is opposed by that neighbour
(today it would arrive unopposed once `sides_of` reads `march_defender`). §3: a commander may ruin a town
he took by force. §4: a detained man musters nowhere.

## §1 · The shape of a drawn act with nobody opposite (Layer 1; U5a's and U5c's decision, applied here)

**The rule.** A row whose `writes:` or `emits:` is keyed by band declares `contests:`
(`architecture/meta/04_CODE_ARCHITECTURE.md` §B.13 invariant 12, §C.4;
`engine/season/data/verbs.py:848-851`, `:872-876` refuse the other shape at load). U5a decided
(`18_DETERMINISM_task_draw_for_uncontested_verbs.md` as reconciled) and U5c applied
(`unified/U5_FINDINGS_CLOSURE_U5c.md` Part 4, its C-22 and C-23) two lawful shapes:

- **(a) a task row:** on the route roster (one name, `graded_tasks`); **flat** `writes:` and `emits:`;
  the magnitude scaled by the one share table `task_fraction` (1 / 1 / 0.5 / 0); the failed draw is the
  keyed `emits_on_refusal` clause `draw`, the form the three inquiries already have.
- **(b) a contest row:** where two bands write different cells or emit different kinds, `contests: "a
  task"` (the prize U5c's verb residue defines once; not on disk at this head, cited from its closure).

Every row of the two families, placed by that test. The bands' meanings are each proposal's and stand.

| verb (proposal) | as written | shape | what changes |
|---|---|---|---|
| `move` (MIL-A) | band-keyed `writes:` (no leg / leg / two legs / leg only), two kinds | (b) | `contests: "a task"`; nothing else |
| `migrate` (MIL-A) | band-keyed; three kinds | (b) | as `move` |
| `train` (MIL-B) | a rank on two bands; `training.practised` on Partial; `training.fruitless` on Failure | (b) | three kinds across bands, so a contest row; the pool is the teacher's score in the vocation (unchanged) |
| `recruit`, `discharge_troops` (MIL-C) | one cell on three bands, `share` 1.0 / 1.0 / 0.5; a Failure kind | (a) | flat `writes: ["Record.subject_matter"]`, flat `emits: ["army.recruited"]` (`army.discharged`); the `share` **is** `task_fraction`, read from the roster and not restated in the effect; `levy.shirked` and `discharge.balked` are the `draw` clause of `emits_on_refusal` |
| `form_unit`, `assign_troops`, `order_unit` (MIL-D) | one cell on three bands; a Failure kind | (a) | flat columns; `unit.unformed`, `assign.balked`, `order.unheeded` are the `draw` clause. The band still reaches the module (`args['band']`) for `raw` and for a partial order: one cell, different contents |
| `disband_unit` (MIL-D) | Partial emits two kinds | (a) | flat `emits: ["army.disbanded"]`; the half that goes home on Partial is `task_fraction` applied to the men returned to the pool and rides the Event as an Observation (`discharged`, a count), not as a second kind; `unit.balked` is the `draw` clause |
| `raze` (PHY-B) | band-keyed cells (`Rung.exists` / `Site.condition`), four kinds; a new roster name `graded_routes`; a new route key `pool_from: mustered_headcount` | (b) | `contests: "a task"`. The roster rename is dropped. **The pool is not a headcount**: it is the one pool rule on the commander's `command` score (U1 §4); the army's size against the town's fabric enters as named levels for the roller and the Site count as a hostile obstacle term (A-25), both rows of data |
| `arrest`, `fight`, `capture`, `accept`, `march` | already `contests:` rows | — | none |
| `examine`, `surveil` (PHY-C) | the inquiries' own form | (a), writing nothing | `surveil`'s Failure kinds (`finding.none`, `watcher.seen`) are both in its `draw` clause |
| `thread_read` (PHY-D) stage 1 | the inquiries' form | (a), writing nothing | the roster is `graded_tasks`, not `graded_routes` |
| `thread_read` stage 2 | `Person.coherence` written on every band, Failure included | (b) | a failed read that still writes is a contest row, bound to the threadwork provider that stage already re-points to |

**Three rules that apply to every row above** (each decided elsewhere; applied, not re-decided):

1. **One sampler** (A-5; `U5a_DICE_owed_edits.md` §1): "the one roller" in these proposals is
   `roll_net_continuous`; `10_DICE_one_roller_one_fraction_rule.md` is cited for its owner, not its dice.
2. **One pool rule, two inputs** (A-6, A-7; U1 §4): the pool is `max(pool_floor, score + addends +
   pool_add)` on the actor's trained score; the governing attribute gives talent levels. `command` and
   `wayfaring` (MIL S2) are definition rows on U1's surface (`references/descriptor_registry.yaml`), from
   which `verb_capability` derives; `command` is the same row `U5b_MB_rulings_in_the_field.md` §1 reads.
3. **A favourable circumstance is a level for the roller, never an obstacle subtraction** (A-25; U5c's
   C-01). The rows written with a minus sign become named levels on the leverage channel:
   `sworn_there` (`migrate`), `cohort_committed`, `footing_war` (`recruit`), `levy` (`discharge_troops`),
   `disciplined` (`order_unit`), `learner_regards_teacher` (`train`). Hostile rows stay obstacle terms.
   All are members of the one roster U5c's `U5c_SC_one_obstacle_form.md` §1 defines.

**Gate.** The loader accepts every row (the two refusals at `data/verbs.py:848-851`, `:872-876` never
fire); for each (a) row, 200 seeds of one hand-built act show the three magnitudes of `task_fraction` and
the `draw` kind; for each (b) row, the proposal's own four-band gate. **Falsifier.** A band-keyed column
on a row with no `contests:`; a second share table in an effect; a subtracted favourable term.
**Movers.** As each proposal declares; the shape adds none.

## §2 · `march` under the land ruling (A-57, A-58): who defends, who thinks of marching, and the three classes

`14_VERBS_PHYSICAL_B_field_and_ruin.md` B1 makes one reader, `march_defender`, answer both "is this a
field for this seat, and against whom" and "may this person think of marching there", and it answers
`None` unless the two factions are at war. B1 also has `sides_of` take its `subject` from that reader. Under
A-58 a casus belli is *"not a precondition"*: an army marched in force onto land another holds **is** the
aggression. With B1 as written, a played or hand-built march on a neighbour with whom there is no war
would get `None`, and the holder would not defend his own ground.

| # | owner | exact edit (amends B1's first two rows) |
|---|---|---|
| 1 | `engine/season/queries/world_q.py` | `field_defender(w, via, rung) -> Optional[str]`, **the one owner of who defends this ground against this seat**, with no war test: `None` unless the rung is a `MARCH_TARGET_KINDS` kind; the holder faction when it is not the marcher's and no leave stands (`world_q.passage_granted`, U5d's decision 5); when the holder is the marcher's own faction or has given leave, the faction mustered there that the marcher's faction is `at_war` with, if any (relief); else `None`. `sides_of` reads this. It is the same predicate U5d's title test reads (holder other than the marcher's, no leave), so the field and the title cannot disagree about who the aggressor is |
| 2 | same | `fields_in_reach(w, p)` (the stamp, B1's second row) keeps its occasion: a rung his ledger names for which `field_defender` is not `None` **and** a war he knows of puts the defender among his enemies (`_wars_known`). That is a rule about when a person thinks of marching, and it keeps formation bounded (`26_MASS_BATTLE_aggression_and_land.md` §5 reads it the same way). It is not a rule about whether the act may be done |
| 3 | `engine/season/verb_table.yaml`, row `march`, `referent_class_note` | B1's sentence "A war-less world forms none (ED-IN-0337)" becomes "A person forms it only against a faction he knows he is at war with; a played or hand-built march onto land another holds is opposed by the holder whether or not a war exists, and is itself the aggression (A-58)" |
| 4 | named for FA (U5d), not built here | the fold of such a march leaves the two factions at war (`06_FA_war_lives_in_seats_B.md` as reconciled: a land-taking march is a war act; A-20: war lives in the seats that wage it) |

**The three classes the record asks to be proposed** (A-58's marked ASSUMPTION), each read from the act
with nothing declared. They are U5d's decisions 5 and 6 and lane 26's §3–§4, adopted, with the verb-side
reading each needs:

| class | the act | holder of the ground | what `field_defender` answers | on `Won` |
|---|---|---|---|---|
| aggression | a march onto land another holds, no leave | another | the holder | the land and its seats pass |
| by leave (passage; an invited ally) | a march onto land whose holder has a live `covenant` with the marcher's seat naming his faction or the rung | another, consenting | the holder's enemy mustered there, if the marcher is at war with it; else `None` (he arrives) | nothing passes |
| relief of one's own | a march onto one's own land with an enemy on it | own | that enemy | nothing to take |
| pursuit across a border, unasked | a march after a beaten enemy onto land a third party holds | another, not consenting | **the holder** (it is his ground the army enters in force) | by the ruling's words, the land passes |

**Open, named and not assumed** (each is recorded by its owner and listed in this lane's receipt only
where it is this family's):

1. Leave covers entering; whether it covers attacking one's host is not stated (26's §4; U5d's).
2. Presence by leave should not license `seize` (`occupying_faction` reads presence however it arose):
   one conjunct at `world_q.occupies`, proposed to U5d by lane 26.
3. The fourth row's consequence: an uninvited rescuer who beats the invader takes the land he rescued.
   Unreachable until allied relief exists; recorded by lane 26 for Jordan when it does.
4. **Whether a person may think of marching without a war** (edit 2). Kept at "a known war" because no
   other occasion has a reader today (no faction-scale claim or grievance reader exists; `holds_dispute`
   is person-scale). A-58 says a casus belli *"or some other act"* will usually be there; which acts
   count as an occasion is FA's to name when one has a reader.
5. An `Unopposed` entry onto held land: no ruling; today's presence, then `seize` (U5d's decision 8).

**Gate.** `14_VERBS_PHYSICAL.md` §5.7's war-world test, unchanged, plus: the same world **without** the
war and with one hand-built `march` on the neighbour's defended settlement: the Event is a field band and
not `field.unopposed`; a hand-built march onto a rung whose holder has a live covenant with the marcher's
seat arrives with no field. **Falsifier.** A march on a defended neighbour folding `Unopposed`; `sides_of`
and the title tail naming different defenders for one act. **Movers.** None in the war-less realm beyond
B1's own (26 formations to 0).

## §3 · `raze` and `seize` after a won march passes the land

`14_VERBS_PHYSICAL_B` B2 licenses `raze` by occupation: the seat's faction stands in a town **another
faction holds** (`occupying_faction`, which returns `None` when the holder is the seat's own faction).
Under A-57 and A-58 a won march onto held land passes the title in the same fold, so the victor **holds**
the town and the occupation licence is false. As written, the one route the audit names to a razing
("a won field or an unopposed arrival has put his army in a town another faction holds") loses its first
half, and `raze` forms only after an `Unopposed` entry.

**Proposed** `[ASSUMPTION; medium; Jordan to correct; revert: occupation only]`: the licence gains one
arm, at its one owner (`queries/world_q.py`, beside the moved `occupying_faction`):

```python
def may_ruin(w, via, rid) -> bool:
    """The licence `raze` asks, for formation (`towns_occupied`) and for the effect, one owner: the
    seat's faction is mustered at `rid` AND EITHER it occupies it (`occupying_faction`) OR the actor's
    own live `hold` on `rid` was opened by a `rung.taken` Event (he took it by a won march and still
    holds it himself; read through the act store, `causing_act`, so no new state and no clock)."""
```

Once he confers the place onward, or it passes from him, the arm closes. The sack still precedes the
ruin and its stores go to the exercised seat's rung. `seize` is unchanged in rule and narrower in use:
after U5d's edit it keeps its Record half, unheld land, and a held place entered `Unopposed`;
`_seize_rung` declines a place the seat's faction already holds, which is what a won march now leaves.
`14_VERBS_PHYSICAL_A` A1's move of `_eff_seize` onto `warrants_for` is its Record half and is untouched.

**The two options, since the ruling does not speak to ruin:** (A, proposed) a commander may ruin what he
took by force while it is still in his own hand: conquest can end in a sack, and the taker's choice
between keeping and ruining is the strategic one the audit describes; (B) `raze` stays an occupier's act
only: a won march gives title and nothing else, and a town can be ruined only by an army that entered it
unopposed without title. Under B the verb is close to unreachable.

**Gate.** `14_VERBS_PHYSICAL.md` §6.7's test with the march forced to `Won` under U5d's edit: the victor's
opening set holds `raze` on the town he took and on no other rung he holds; after he confers it, it holds
none. **Falsifier.** `raze` forming on a town the actor inherited or was given. **Movers.** Formation.

## §4 · A detained man musters nowhere (`audits/25_GROUNDING_ENGINE.md` G-32; `14_VERBS_PHYSICAL.md` §2.4)

The audit's sentence (a captive's `detain` edge is read by `world_q.mustered` through `restrained`) was
grounded false: `mustered` (`queries/world_q.py:2132-2149`) never calls `restrained`, so a detained
member still musters, and proposal A's gate "fails until it lands". No file carried the edit.

1. `engine/season/queries/world_q.py::mustered`: a member for whom `restrained(w, pid)` is true is not
   counted. One conjunct at the one owner. A-23 (custody suspends acts through the seat) is the ruling
   it agrees with; the seat-side check is FA's.
2. `loop/sides.py` and `seam/wrappers/mass_battle.py::_order_of_battle` read `mustered` and need no edit;
   an army whose holder is detained is fielded as a headcount line (the first MB audit's NPC-072 gate).

**Gate.** A hand-built world with one captured commander: `mustered` at his rung excludes him and the
field's sides are built without his weight. **Falsifier.** A detained person's `body` scaled by a field he
could not have stood in. **Movers.** Fields in which a mustered member is detained (none in shipped play).

## §5 · Smaller items

| item | decision | owner |
|---|---|---|
| D-25: does an arrest need the officer beside the prisoner | closed by the ladder: no; the court's reach suffices (`unified/DECISIONS_QUICKSHEET.md`, D-25 A). `arrest` gains no `with` conjunct | `14_VERBS_PHYSICAL_A` A1, unchanged |
| D-36: three organising verbs or one | closed by the ladder: three (`DECISIONS_ANSWERED.md`) | `14_VERBS_MILITARY_D`, unchanged |
| A-21 (a decree is proclaimed; challenges stay in person) | consistent: a warrant addressed and heard needs no paper in hand (A1); a challenge is issued with the challenged present (`with`) and answered once heard (A4) | — |
| A-22 (command, not territory) | the seat that addresses a warrant to an officer must be one that may order him; the check is FA's, read where the writ is formed | U5d |
| A-16 (murder) and `fight`'s contexts | `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` adds the occasion; A3's `context_terms` gains its term there; the opener's edge is `U5b_PC_rulings_in_the_fight.md` §6 | U5d; U5b |
| the `with` deposit (MIL-A Edit 6) | one owner: MIL-A carries it once; PHY-A and the SOCIAL verbs cite it (U5c's C-19 names the one reader of "who I believe is with me", `person_q.present_persons`, which the deposit feeds) | MIL-A |
| the placeless after a razing | `[UNVERIFIED in the audit: whether migrate forms for a person with no live reside]`; A-56 makes `migrate` one of the common people's heavy moves, so the dependency is U5d's commons carrier; `raze` gains no re-homing (Layer 1 §B.8) | U5d |
| `thread_read`'s Site half | "waits on the Thread substrate, which has no carrier": A-40 rules the Thread is ground, one site a territory, no new entity kind; the half is unblocked and is WR's to plan (`09_WR_*`, U5d's) | U5d |
| a commander's death | A-15 turns natural death on, so MIL-C Edit 6 (the successor takes up the roll; the dispersal draw) is reached in ordinary play; nothing changes in it | MIL-C |
| H-309 | absence is not vacancy (MIL-A's note); A-23 adds that custody, not absence, suspends a seat's acts | — |

## Who lands it, and dependencies

§1 is applied when each verb proposal lands (the proposal's own batch), after
`18_DETERMINISM_task_draw_for_uncontested_verbs.md` step 2 (the loader) and U5c's task prize. §2 and §3
land with `14_VERBS_PHYSICAL_B` and U5d's land proposal. §4 lands with `14_VERBS_PHYSICAL_A`.

## NERS reading (E last)

N: without §1 none of the eighteen rows loads; without §2 a neighbour does not defend his land against an
undeclared march; without §3 the land ruling quietly removes ruin from the game. R: three classes of
march, read from what the army did. S: one shape for a drawn act across all six verb families; one
predicate for the defender and for the title. E: one reader renamed and split, one licence arm, one
conjunct, and a table.

## Cost class

Edits (§1, §4, §5); small builds (§2, §3) inside their proposals' batches.
