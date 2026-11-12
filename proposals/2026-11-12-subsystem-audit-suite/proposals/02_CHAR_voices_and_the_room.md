# CHAR — voices and the room: a person's own choice read back as the parts that argued over it, and the regard of those who saw it

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

**Measured: the parts disagree, almost always a little and rarely a lot.** `probe_voices.py`
(`build_realm`, no season, the score-top candidate of each formed set over the common referents, the
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
is one owned part of one person's score for one candidate, attributed and selected. A **room** is the
regard, split by its four parts, of the persons who witnessed an act, for its actor, with its change
since the surface last read it. Neither is a new subsystem; both are readings over owners that exist.

## Exact edits, by file and owner

1. **The attribution** (`engine/season/decision/voices.py`, new, person-side, no `World`, AX-2):

   ```python
   @dataclass(frozen=True)
   class Voice:
       kind: str      # "pursuit" | "stance"; later "goal", "risk", "capability" as their terms land
       owner: str     # the pursuit key, the subject id, ...
       pull: float    # its signed share of the candidate's score

   def voices(p, c, fx, memo, odds=None) -> tuple[Voice, ...]:
       """Every owned part of `score_terms(p, c, fx, memo, odds)`, exactly once. The pursuit term is
       split by held pursuit: `damp * Σ_axis to_axes({e: w_e})[axis] * align(c.verb, axis) * odds_weight`,
       `w_e` from `crisis_weights(p, fx.get("scar_weight_shift"))`, the weights `project` uses; the
       stance term is one Voice owned by `c.subject`. Sorted by |pull| descending, then owner."""
   ```

   It calls `score_terms` and `deliberation_memo` and re-derives neither factor (`CLAUDE.md` §8):
   `damp` is read from the memo, `odds_weight` once per candidate as `score_terms` asks it.

2. **One structural tie, in the same module**: a constant `ATTRIBUTED_TERMS = ("pursuit", "stance")`
   and a test (`tests/` beside `decision/`'s own) that `len(score_terms(...)) == len(ATTRIBUTED_TERMS)`
   and that the voices of a candidate sum to its score. A term added to `score_terms` by
   `02_CHAR_goal_lean_on_its_own_question.md` or `02_CHAR_what_an_act_risks.md` then fails the test
   until it names its owner. This earns its place under §0.1 pt 5: its output crosses into the
   player's surface (the port).

3. **The selection** (same module), the curation rule B5 requires, so that a voice is rare:

   ```python
   def heard(chosen_voices, total, runner_up_voices=None, floor=0.5) -> tuple[Voice, ...]:
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

5. **The room** (`engine/season/queries/world_q.py`, beside `witnessed`, whose rule it shares):

   ```python
   def present_at(w, event_id) -> tuple[str, ...]:
       """The persons who hold a claim deposited with `event_id` among its causes: `witnessed`'s rule
       read from the Event's side. One helper serves both; `witnessed` is rewritten to call it."""

   def the_room(w, event_id, fx) -> tuple[tuple[str, dict], ...]:
       """For each person present, his regard for the event's actor split as `regard` adds it:
       {"stored", "judged", "told", "heritage"}. `regard` gains a `regard_parts` sibling returning the
       four addends it already computes, and `regard` returns their sum (one owner of the formula)."""
   ```

   The change since the last scene is the surface's to compute, by keeping its own previous reading;
   the World keeps nothing (ED-IN-0225). The Pentiment flag *"this will be remembered"* is then the
   room's `judged` part moving on a deed the person just did, which is already the model.

6. **The surface** (GO's, cross-listed): the person panel shows `heard(...)` for the act taken and the
   room after it, in words built from `Voice.kind`, `owner` and `gloss` (`02_CHAR_capability_definitions.md`),
   never the totals alone.

7. **Not built here: a faculty's voice and a voice that was wrong.** A faculty speaks when a
   capability use fires (`capability_uses`; the DICE map's `capability` advantage source reports
   which). A faculty that was wrong needs a held claim to record which faculty admitted it, and a
   missed finding to be recordable as missed; both are FI's (`08_FI_audit_addendum_B.md`, line 245)
   and a write, so they are not observers and do not belong here. Until then the voices are a
   person's ends and his relations, which is half of the precedent and the half the engine already
   holds.

## The gate (an execution artifact)

(a) `build_realm(0)`, one and two seasons, with a `watch` that calls `voices` and `heard` on every
deliberation and `the_room` on every act: `content_hash` EQUAL to the run without it. (b) For every
candidate scored in (a), the voices sum to `sum(score_terms(...))` within a bound stated as summation
reorder (n·ulp of the largest part; the probe reads 1.1e-16), and every held pursuit with a non-zero
part appears once. (c) `regard_parts` sums to `regard` exactly (same addition order). (d) The share of
deliberations with a dissent heard at `floor` 0.5 is reported at seeds 0 to 2.

## The falsifier

(a) moves the hash: a voice is steering, and the reading is wrong in kind. (b) fails: the voices are
not the score's parts, and a player would be shown reasons that did not decide. (d) reads near 100%:
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

Small build (one module, two functions in `world_q`, one sibling of `regard`), after the reason
trail's `watch` hook; the surface is GO's.
