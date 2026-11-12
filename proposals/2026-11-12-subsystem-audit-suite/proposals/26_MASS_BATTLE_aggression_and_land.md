# MB · a march into land another holds is the aggression; only its win takes the land, and the seats go with it

## Status: PROPOSED

Lane MB (the row and effect edits are IN's; the title body belongs to the `seize` row's owner; the consent and
war edges are FA's and are named, not designed). Carries Jordan's rulings **A-57** and **A-58**
(`unified/DECISIONS_ANSWERED.md:69`, `:71`, 2026-11-12; D-20 superseded at `:87`):

- *"a won battle takes land if and only if the aggressor marched in an effort to take land (as opposed to
  battle in a neutral location or a defending army wins)"*;
- *"Seats pass with holdings."* *"Draw on land taking march means defender retains land."*
- *"Usually there will be a casus belli or some other act, but generally, sending your military into another's
  territory is a pretty clear sign of aggression"*.

Row R-10 of `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`. An earlier draft of this file gave the march a
declared purpose; A-58 withdrew that, and the draft is gone. Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Every `march` folded `Won` at a place another faction holds and defended. Today it writes presence and never
title (`engine/season/loop/effects_combat.py:532-536`, as `proposals/06_FA_war_lives_in_seats_B.md:37-38`
quotes it). After this change the same fold also moves the place's `hold`, and closes the seats seated at it,
through the one function that writes a Rung's title. `Lost`, `Drawn`, `Unopposed` and `Invested` write no
title. A declared hash mover wherever such a field is won; in natural play today no field is won
(`audits/04_MB_audit.md` §0).

## The problem

- Code and suite follow the reading the rulings replace: presence on a won field, title by a second act,
  `seize`, licensed by occupation (`loop/effects_information.py:1038-1071`; `loop/effects_shared.py:149-161`;
  `audits/04_MB_audit.md:617`, `:781`, `:821`).
- Occupation is presence, however it came about (`effects_shared.py:157-159`: "people placed on a territory by
  other means (a `move`) occupy it as well … named in `HANDOFF_MB.md`, not closed here"). An invited ally
  standing on a friend's land therefore holds the licence to seize it.
- The gate admits no seizure of an Office ("A SEAT IS NEVER SEIZED", `effects_information.py:1015-1020`), so
  nothing can make a seat follow its land.
- The PHYSICAL lane forms `march` only against a faction the marcher is at war with
  (`proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` B1), which makes a war a precondition of the act.

## The resolution, decided

### 1. Aggression is read from the act, by one predicate

No operand, no payload key, no declaration. New in `engine/season/queries/world_q.py`, the one owner:

```python
def aggression_against(w, via, rung) -> Optional[str]:
    """The faction whose land a march by seat `via` on `rung` is an aggression against, or None.
    None when: nobody holds the place (neutral ground: outside the rule); the marcher's own faction
    holds it; or the marcher's faction has the holder's leave to be there (section 4)."""
```

It reads `holder_faction_of`, `seat_faction` and `has_leave`, each an existing or named single owner. It does
not read `at_war`: a casus belli, a claim or a declaration is context that the owners of legitimacy and regard
read (FA, CHAR), and is no conjunct here.

### 2. What each end state writes (ruling A-3's bands, read by the effect)

`loop/effects_combat.py::_eff_march`, after what each band writes today:

| band | the place's title and seats |
|---|---|
| `Won` | **pass** to the marcher's side when `aggression_against(w, a.via, target)` is the faction whose defence was beaten (section 3); otherwise nothing |
| `Lost` | nothing, in either direction: a defender's win takes none of the aggressor's land |
| `Drawn` | nothing: the defender retains the land (A-58) |
| `Unopposed` | nothing by this rule: no battle was won. Presence as today |
| `Invested` | nothing |

`seam/ladder.py::field_degree` still returns the band only, and `modules/mass_battle/` sees none of this: the
resolver is the same whoever marched and why (ruling A-1).

### 3. Whose defence was beaten: how relief and pursuit across a border are classed

The land passes only when the side the marcher beat was **defending for the holder**: it is the holder's
faction, or stands there by the holder's leave. One predicate, `defends_for(w, defender_faction, rung)`,
beside the one above. Classed from the facts, with nothing declared:

| the march | holder | marcher has leave | beaten side | title on `Won` | class |
|---|---|---|---|---|---|
| into another's land, against its holder | other | no | the holder, or his ally by leave | **passes, with its seats** | aggression |
| into another's land, against its holder, though the marcher was a guest | other | yes | the holder | **passes**: leave covers entering, not fighting one's host | aggression (treachery; regard's owner reads the broken leave) |
| into an ally's land, against the ally's enemy standing on it | other | yes | an intruder | nothing | relief of an ally |
| into another's land after a beaten enemy, or to drive off a third party, uninvited | other | no | an intruder | nothing by this battle; the marcher is now himself there without leave | pursuit across a border; uninvited relief |
| onto his own land, against an enemy standing on it | own | — | the intruder | nothing to take | defence |
| through another's land by agreement, meeting nobody | other | yes | — | nothing | passage |
| onto land nobody holds | none | — | anyone | outside the rule | neutral ground |

The fourth row is the one a reader may dispute. The plain words of A-58 make any march in force into another's
land an aggression; this table agrees that it is one (for regard, and as a reason for the holder to march on
the intruder) and holds that the *battle won there* was not won against the land's defence, so the "won
battle" of A-57 has not happened yet. If Jordan reads it the other way, the change is one line: drop
`defends_for` and pass the land on any `Won` at a place held by another without leave.

### 4. Consent (the record's ASSUMPTION): how leave is read

`world_q.has_leave(w, guest_faction, holder_faction, rung) -> bool`, the one owner. True when **a standing
commitment between the two exists and is live**: a covenant (the `dispensation` Record the `covenant` verb
mints through a seat, `engine/season/verb_table.yaml:300-322`) drawn up by a seat of the holder's faction
whose purview reaches the place, addressed to a person of the guest faction, to whose terms both parties hold
a live `commit`, and whose terms are leave to stand at that place or a rung above it.

- An invitation and an agreed passage are both this: one instrument, the holder's seat's writ addressed across
  purview. No new verb and no new Record kind.
- Leave ends as any commitment ends: either party closes his `commit` (peace's shape,
  `world_q.py:3576-3579`). A guest who stays after that is there without leave from the next read.
- Leave is never implied: a common enemy is not consent. A rescuer nobody asked for is classed by row four.
- `[UNVERIFIED: what a covenant's terms Proposition can say. The row was read; the Proposition mood roster
  was not. If no member fits "leave to stand at a place", one joins it, named `leave`.]`
- **Presence by leave is not occupation.** `world_q.occupies` (the one reading `seize` and `raze` share, via
  `occupying_faction`) declines a faction that `has_leave`. This closes the weakness the code names at
  `effects_shared.py:157-159` for the guest's case; a person who merely moved there without an army is the
  same weakness as before and is not closed here.

### 5. One owner of the title write; seats pass with it

`_seize_rung` (`loop/effects_information.py:1038`) splits, with no change to what `seize` does on a Rung
except the seats:

- `transfer_title(w, act, rid) -> Change`: closes the place's live `hold` and opens the taker's (the opened
  edge's id salted with the act, as now), **and closes the live `hold` on every seat seated at that place or
  beneath it that belongs to the dispossessed holder's faction**. One Change, so the fold never sees the land
  under one faction and its seats under another. Kind earned by the place: `rung.seized`, the tree's one kind
  for a place taken without consent.
- `_seize_rung` keeps its licence and calls it. `_eff_march` calls it under sections 2 and 3.
- The gate gains one named clause: a seat's `hold` may be closed by `transfer_title`, with the title of the
  place it is seated at, and by nothing else. `[UNVERIFIED: `state/gate.py`'s `seizure` clause was read only
  through `may_seize`'s docstring (`:1005-1019`), whose second conjunct asks the seat's grant for the seizure
  act. A seat that grants `dispatch` and not `issue` would be refused there; the builder widens that one
  predicate with an arm for a won aggression, not a second path. How an Office records its place was seen at
  `engine/season/offices.yaml:189-241` (`rung:`) and not traced to its reader.]`
- **Who receives the land** is `_seize_rung`'s present rule (the act's actor, marked ASSUMPTION there): for a
  march, the person who exercised the dispatching seat. **Who sits the seats that passed** is not written
  here: they are closed under their old holders and are the new holder's to fill by the acts that fill a
  vacant seat (FA's `06_FA_seat_terms_and_turnover.md`). "Pass" is read as: they leave the old faction with
  the land. Whether the taker is also seated in them by the same fold is the one point of A-58 this proposal
  does not settle, and it says so.

### 6. A march need not wait for a war, and makes one

- `sides_of` fields the holder as the defender whenever `aggression_against` names him, at war or not. A
  hand-built or played `march` on a neighbour therefore fights; `requires_typed` already asks only for a Rung.
- **Formation stays the PHYSICAL lane's**: a person forms `march` on the places of those he knows he is at war
  with (`fields_in_reach`, `_wars_known`). That is an occasion for thinking of it, not a precondition of the
  act, and keeping it bounds formation. The alternative (every held place a Field for every dispatching seat)
  is named for that lane and not taken: ladder step 5, formation counts.
- A march that is an aggression against a faction the marcher is not at war with **is the act of war**. The
  fold that folds it should leave `at_war` true between the two, by the dispatching seat-holder's `commit` to a
  WAR Proposition (war lives in the seats that wage it, A-20). That edge is FA's
  (`06_FA_war_lives_in_seats_B.md`) and is owed there; until it lands, `at_war` and the fact of an army on the
  land disagree for such a march, and this proposal's gates do not exercise it.

## Exact edits

| file (owner) | edit |
|---|---|
| `engine/season/queries/world_q.py` | `aggression_against`, `defends_for`, `has_leave`; `occupies` declines a faction with leave |
| `engine/season/loop/effects_information.py` | `transfer_title` factored out of `_seize_rung`; the seats' closure inside it |
| `engine/season/loop/effects_combat.py::_eff_march` | the `Won` call of section 2; the comment "a won field writes PRESENCE, never title" replaced by a pointer to A-57 and A-58 |
| `engine/season/loop/sides.py::sides_of` | the defender is `aggression_against`'s faction (with the PHYSICAL lane's `march_defender` reading the same predicate for its first arm, so the two never disagree) |
| `engine/season/state/gate.py` | the one clause of section 5 |
| `engine/season/verb_table.yaml`, row `march` (`:1064`, `:1073`) | `Won` gains the place's `Tenure.until`, `Tenure.since` pair and the seats' `Tenure.until`; `emits.Won` gains `rung.seized`; `writes_note` cites A-57, A-58. `[verify at landing: whether the loader requires each declared write on every fold of a band; `data/verbs.py::KIND_VERB`'s rule for a kind with two emitters]` |
| `engine/season/hole_register.yaml` | the rows that record presence-not-title as an assumption (R-6's) close as superseded by A-57, A-58 |

## Open, named

1. Whether the taker is seated in the seats that passed, or they fall vacant to be filled (section 5).
2. Whether an unopposed entry in force, with no battle, ever takes land. The rulings speak of a won battle;
   today's `seize` by occupation is left as the only route and is not widened.
3. Whether a drawn aggressor stays on the ground. `04_MB_headcount_grade_and_scale.md` writes "nobody
   arrives" on `Drawn`; A-58 says only that the defender keeps the land. That proposal's write stands.
4. Row four of section 3 (pursuit and uninvited relief).
5. What a casus belli is, to the owners of regard and legitimacy. Not a field here.
6. H-166: who holds an unheld place. Outside the rule by A-58.

## Gate (execution artifacts)

1. `build_realm(0)`, one season: content hash equal (no field is won there).
2. A two-faction fixture world, the target held and defended by B: over seeds 0 to 59, every `Won` fold leaves
   `holder_faction_of(target)` A's, emits one `rung.seized`, and leaves no live `hold` by a B person on a seat
   seated at or beneath the target; every `Lost` and `Drawn` fold leaves holder and seats as they were, and
   A's own holdings unchanged. `assert checked >= N` per band.
3. Relief: B holds the target, C stands on it, A holds a live covenant of leave from B: A's `Won` over C
   moves no title; with A's `commit` to the covenant closed, the same fold still moves none (row four), and
   `occupies` now reads A as an occupier where with leave it did not.
4. Treachery: A, with leave, marches on B's own force and wins: the title passes.
5. Neutral ground: a planted unheld Rung: no title is written on any band.
6. `seize` on an occupied settlement: its existing tests, with one added assertion that the seats there
   closed with it.
7. Same seed twice: equal `content_hash`.

## Falsifier

Title or a seat moving on `Lost`, `Drawn`, `Unopposed` or `Invested`; title moving while a seat at the place
stays with the old faction; a second site that closes a Rung's `hold`; `aggression_against` reading a stored
purpose, or reading `at_war`; a guest with live leave passing `occupies`.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From the campaign: a war is won on the map by beating the land's defenders, and by nothing less. From
  the defender: a drawn field keeps the land, so holding is worth something. From the ally: help can be asked
  for and given without handing over the keys. Laterally: `seize` and conquest are one write. Cut `defends_for`
  and a pursuer takes a bystander's province; cut `has_leave` and no faction can safely call for aid.
- **R.** Why an army is where it is can be read by everyone from where it is and whom it fights; treachery,
  rescue and trespass are three different stories from one rule; with no player, borders move when someone
  beats someone on his own ground.
- **S.** No new operand, verb, Record kind or band; the resolver untouched; consent is an existing instrument
  ended the way every commitment ends.
- **E, against that.** Three small readers, one function split and called twice, one gate clause.

## Cost class

Small build, after the PHYSICAL lane's B1 and the MB lane's `Drawn` band. Section 6's war edge is FA's.

## History, for what it is worth

A ruling is not grounded in research. The pages read add one thing: a place usually changed hands by what
followed the field, terms offered to its defenders or a storm
(`research/historical/mass_battle_maneuver_sequences_grounding.md` §11). That bears on open item 2 and on
whether a walled place should pass on a won field without its `Invested` band; it is not decided here.
