# CHAR — voices and the room: a person's own choice read back as the parts that argued over it, and the regard of those who saw it

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-15) — Edit 5's `present_at(w, event_id)` carries its rule itself; the clause *"`witnessed` is rewritten to call it"* is dropped, because `world_q.witnessed` is deleted with the person projection (`17_CENSUS_C1A_01_deletion_batches.md` D2). `the_room` is a host-side reading for the surface and is not a per-person client read. The term tuple this file attributes grows with `aim` and `risk` and, where a seat's row declares one, the beneficiary arm (`17_CENSUS_C1A_02_wires_and_corrections.md` W4).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.2 row (`voices`/`heard` CONFORM; **`the_room` VIOLATES**), §2 row A-83, §7, §7b-5, §7b-17, §7b-T; `unified/U1_GLOSSARY.md` *voice*, *room*; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger S-15; `unified/U3_CONFLICT_LEDGER.md` C3-D7, C3-L4; `unified/U3_DEPENDENCY_ORDER.md` node B10, §4.1 row 2). Layer 1 rewrite (`04` §C.11: the engine owes the arithmetic of what the character already holds, and nothing else; §B.2/AX-2: no Query hands one person another's ledger): the room a person is shown is the **believed room**, `person_q.room_as_held(p: PersonInterior, event_id, fx)`, read from his own ledger and stance rows (what he holds of how those present regard him); the witnesses' true regard is a resolver-side reading renamed `world_q.witness_regard` (glossary) and is for the chronicle (a harness observer) only; A-83 agrees (pressure is read from what the person believes). Vocabulary: "voice" stays on the surface only; in code the parts are **score parts** (`decision/score_parts.py`, `ScorePart`, `score_parts`), per the glossary. `ATTRIBUTED_TERMS` names all four terms (`pursuit`, `stance`, `aim`, `risk`; C3-D7). `present_at` no longer cites the deleted `witnessed`. Named tests, lands-it and tier.

**Lands in batch:** B10, after `02_CHAR_goal_lean_on_its_own_question.md` and `02_CHAR_what_an_act_risks.md` (C3-D7). **Depends on:** `02_CHAR_reason_trail_and_small_edits.md` Part A (B09, `watch`), `17_CENSUS_C1A_01_deletion_batches.md` D2 (B03; `witnessed` deleted).

## Status: PROPOSED

Written by the CHAR audit lane, addendum B (`audits/02_CHAR_audit_addendum_B.md`, §B5, B6.2 rows 19
and 20). Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).
Ratifies nothing. Reference under `CLAUDE.md` §0.05. It composes on the first CHAR audit's reason
trail (`02_CHAR_reason_trail_and_small_edits.md` Part A, the `watch` hook), on `score_terms` as the
one owner of the score's formula, and on `regard` as the one owner of how one person holds another.
It adds no store, no carrier, no Event, no field on `Person` or `Act`, and no roster of voices.

## What this changes in `engine/season/` at runtime

Nothing. Both readings are observers (ED-IN-0225): they are called by a `watch` callback or by a
surface after the fact, read what the chooser and the ledger already hold, and write nothing. The
hash is EQUAL with them called or not; that is the gate's first reading.

## The problem, with evidence

**The precedent the design names has no mechanism behind it.** `character_generation_questionnaire_v30`
§1 takes from Disco Elysium *"24 skills as voiced inner life … Personality is surfaced through inner
voices, not stat labels"*, and its open item 6 asks that a voice *"reference the hook that produced
the Conviction weight"*; `player_agency_v30` §1.6 takes from Pentiment *"investigation as social act
with social cost"* (both ARCHIVED-NOT-CANON; intent only). No design document says what a voice is
(B5). The FI audits (`08_FI_audit.md` line 974; `08_FI_audit_addendum_B.md` line 245) list the voices
as named only and leave them to this lane.

**The material exists and is thrown away.** `decision/choose.py:193-221`: `score_terms` returns the
score as separately computed terms, `(pursuit, stance)`, and the pursuit term is itself a sum over the
person's held pursuits, because the axis weights are `to_axes` of `crisis_weights(p, shift)`
(`data/pursuits.py:60`, linear in each pursuit's weight; `decision/options.py:560-565`). The parts are
added and the addends lost; `Act.reads` is empty for every act (H-343).

**Measured: the parts disagree, almost always a little and rarely a lot.** `probe_voices.py` (a scratch
script, not in the repository; its readings are restated by gates (b) and (d) below) (`build_realm`, no season, the score-top candidate of each formed set over the common referents, the
pursuit term split by held pursuit; B7). Of 498 deliberations, the act ranked first had at least one
held pursuit pulling against it in 493 (99.0%), a median of six such pursuits; the largest of them
was a median 0.16 of the act's total, at or above half of it in 2.2% of deliberations and never
larger than it. The stance term opposed the act taken in none. The split reproduces `score_terms`'
pursuit term to 1.1e-16 (summation order only). Seeds 0 and 1 read identically.

Two consequences decide the design. Disagreement is not scarce, so a voice that speaks whenever a
part points the other way would speak in every scene, which is the Tale-Spin effect from the other
side (T13.Q1; a console, not a voice). And a dissent large enough to matter is rare, about one
deliberation in fifty, which is the rarity a voice needs to be heard.

**The community's opinion is computed and shown to nobody.** `queries/person_q.py:424` `regard` is the
stored stance plus judged deeds plus told deeds plus the caste estimate, computed at read;
`opinion` and `legitimacy` likewise. A person cannot see what the people who watched him think of him
now, or what changed it; `legitimacy` and `stability` have one caller, the storybar harness
(`harness/storybar.py:280-281`; H-224).

## The resolution, decided

Ladder: step 5 (what the architecture makes plain), under the observer rule of ED-IN-0225. A **voice**
(the surface's word; in code a **score part**) is one owned part of one person's score for one candidate,
attributed and selected. A **room** is what the acting person **holds** of how those present regard him
(his own claims and stance rows), with its change since the surface last read it; never the witnesses'
own ledgers. Neither is a new subsystem; both are readings over owners that exist.

## Exact edits, by file and owner

1. **The attribution** (`engine/season/decision/score_parts.py`, new, person-side, no `World`, AX-2):

   ```python
   @dataclass(frozen=True)
   class ScorePart:   # shown on the surface as a "voice"
       kind: str      # "pursuit" | "stance" | "aim" | "risk"; later "capability" as its term lands
       owner: str     # the pursuit key, the subject id, the goal id, ...
       pull: float    # its signed share of the candidate's score

   def score_parts(p, c, fx, memo, odds=None) -> tuple[ScorePart, ...]:
       """Every owned part of `score_terms(p, c, fx, memo, odds)`, exactly once. The pursuit term is
       split by held pursuit: `damp * Σ_axis to_axes({e: w_e})[axis] * align(c.verb, axis) * odds_weight`,
       `w_e` from `crisis_weights(p, fx.get("scar_weight_shift"))`, the weights `project` uses; the
       stance term is one ScorePart owned by `c.subject`; `aim` one owned by the goal, `risk` one owned
       by the prize. Sorted by |pull| descending, then owner."""
   ```

   It calls `score_terms` and `deliberation_memo` and re-derives neither factor (`CLAUDE.md` §8):
   `damp` is read from the memo, `odds_weight` once per candidate as `score_terms` asks it.

2. **One structural tie, in the same module**: a constant `ATTRIBUTED_TERMS = ("pursuit", "stance", "aim",
   "risk")` (this file lands after both terms, C3-D7) and a test that `len(score_terms(...)) ==
   len(ATTRIBUTED_TERMS)` and that the parts of a candidate sum to its score. A further term added to
   `score_terms` then fails the test until it names its owner. This earns its place under §0.1 pt 5: its output crosses into the
   player's surface (the port).

3. **The selection** (same module), the curation rule B5 requires, so that a voice is rare:

   ```python
   def heard(chosen_parts, total, runner_up_parts=None, floor=0.5) -> tuple[ScorePart, ...]:
       """At most two voices: the one that CARRIED the act (the largest pull with the total's sign)
       and, only if one exists at or above `floor * |total|`, the one that DISSENTED (the largest
       pull against it). With the draw's departure known (`watch`'s `sampled` differs from `ranked`
       at the head), a third, kind "draw", says the person did not take his own best."""
   ```

   `floor` is a display parameter of the surface, not a fixture: it changes what is shown, never what
   is chosen. 0.5 is `[ASSUMPTION; medium; GO and Jordan to correct]`; at it, a dissent is heard in
   2.2% of the deliberations measured. While choice temperature is realm-wide (F-CHAR-02) the "draw"
   voice says nothing about the person; `02_CHAR_resolve_and_temper.md` makes it his.

4. **The history a voice cites** (open item 6, *"reference the hook"*): a pursuit voice carries, by
   read, that pursuit's scar count (`Person.scar[e]`) and the newest claim in his ledger whose deed
   `deeds_judged` scored on that pursuit's axes; a stance voice carries `regard`'s four parts for its
   subject (item 5). Read at the call; nothing is stored.

5. **The room** — two readings, one per side of the line `04` §C.11 draws:

   ```python
   # queries/person_q.py  (person-side; asker first; no World)
   def room_as_held(p: PersonInterior, event_id: str, fx) -> tuple[tuple[str, dict], ...]:
       """For each person p's own ledger names as present at `event_id` (a claim deposited with that
       Event among its causes, held by p), p's reading of that person's regard for p's act:
       {"told", "seen", "bond"} from p's own claims (bond:<ground>, told regards, what p saw).
       Nothing about anyone else's ledger."""

   # queries/world_q.py  (resolver-side; for the chronicle, a harness observer, only)
   def present_at(w, event_id) -> tuple[str, ...]:
       """The persons who hold a claim deposited with `event_id` among its causes (the rule the
       deleted `witnessed` had, read from the Event's side)."""
   def witness_regard(w, event_id, fx) -> tuple[tuple[str, dict], ...]:
       """For the chronicle only: each present person's regard for the actor split as `regard` adds
       it, {"stored", "judged", "told", "heritage"}. `regard` gains a `regard_parts` sibling returning the
       four addends it already computes, and `regard` returns their sum (one owner of the formula).
       Never handed to `decision/` or to the player's surface."""
   ```

   The person's surface calls only `room_as_held`. The change since the last scene is the surface's to
   compute, by keeping its own previous reading; the World keeps nothing (ED-IN-0225). The Pentiment flag
   *"this will be remembered"* is then the actor's own claim that the deed was witnessed (what he saw of
   who saw him), not the witnesses' regard: a man may not know he was seen.

6. **The surface** (GO's, cross-listed): the person panel shows `heard(...)` for the act taken as voices and
   `room_as_held(...)` after it, in words built from `ScorePart.kind`, `owner` and `gloss`
   (`02_CHAR_capability_definitions.md`), never the totals alone.

7. **Not built here: a faculty's voice and a voice that was wrong.** A faculty speaks when a
   capability use fires (`capability_uses`; the DICE map's `capability` advantage source reports
   which). A faculty that was wrong needs a held claim to record which faculty admitted it, and a
   missed finding to be recordable as missed; both are FI's (`08_FI_audit_addendum_B.md`, line 245)
   and a write, so they are not observers and do not belong here. Until then the voices are a
   person's ends and his relations, which is half of the precedent and the half the engine already
   holds.

## The gate (an execution artifact)

(a) `build_realm(0)`, one and two seasons, with a `watch` that calls `score_parts` and `heard` on every
deliberation and `room_as_held` and `witness_regard` on every act: `content_hash` EQUAL to the run without
it. (b) For every candidate scored in (a), the parts sum to `sum(score_terms(...))` within a bound stated as summation
reorder (n·ulp of the largest part; the probe reads 1.1e-16), and every held pursuit with a non-zero
part appears once. (c) `regard_parts` sums to `regard` exactly (same addition order). (d) The share of
deliberations with a dissent heard at `floor` 0.5 is reported at seeds 0 to 2. (e) `room_as_held` on a
world in which a witness holds a hostile regard the actor holds no claim of returns no hostile entry for
him (the flag cannot tell the actor what he does not know).

**Named tests** (new, `engine/season/tests/test_voices.py`): `test_score_parts_sum_to_the_score` (b);
`test_attributed_terms_equals_score_terms_length`; `test_regard_parts_sum_to_regard` (c);
`test_room_as_held_names_only_what_the_actor_holds` (e); `test_watching_the_parts_leaves_the_hash_equal` (a);
`test_no_decision_or_surface_module_calls_witness_regard` (a source scan).

## The falsifier

(a) moves the hash: a voice is steering, and the reading is wrong in kind. (b) fails: the voices are
not the score's parts, and a player would be shown reasons that did not decide. (e) fails: the surface
reads world truth. (d) reads near 100%:
the selection is a console; near 0% over four seasons: the dissent is never heard and the second voice
is dead weight, and `floor` is the knob to report, not to tune silently.

## NERS reading (`CLAUDE.md` §0.06; E last)

- **N.** From the player's side it is the only way to learn why a person did what he did and what he
  nearly did instead; from a computed person's side it shows two people differing for reasons that are
  theirs, which is what B3.2 found most absent; from the world's side the room is where conduct has a
  cost someone can see (Pentiment's lesson). Removing it leaves the reason trail as numbers.
- **R.** Strategy: a dissent heard is a lever (argue to that pursuit; befriend that subject). The
  no-player half: an NPC's choices read in the chronicle as conflicted or whole, unobserved.
- **S.** One owner for the formula (`score_terms`), one for regard, one for witnessing; the voices are
  their parts, so the methodology is the score's own and cannot diverge from it.
- **E.** Two pure functions and one split of an existing sum, for the design's most-cited precedent.
  A player can intuit it: *he took the post; the part of him that loves his brother did not want to.*

## Cost class

Small build (one module, one function in `person_q`, two in `world_q`, one sibling of `regard`), after the
reason trail's `watch` hook; the surface is GO's.

**Lands it and tier.** The B10 batch, last of the chooser group, an IN `valoria-author` session on `sonnet`
(`high`), closed by B10's `methodology-close` once. **Hash movers.** None (observers; gate (a) is the
control).
