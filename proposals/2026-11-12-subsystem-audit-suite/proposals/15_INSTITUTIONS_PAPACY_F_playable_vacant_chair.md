# PAPACY-F — the first playable Church scenario: *The Vacant Chair*

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_PAPACY.md` §11 (batch 3), §9 items 1 and 2, §10 (NPC-039, NPC-040,
NPC-034); the standing requirement of `AUDIT_BRIEF.md` (playable alone, one code path, integrated, no GM).
Composes on FA-P4 (`06_FA_playable_scenario.md`: the `play` entry, the `vacancy` situation made by a real
act at tick 0, the per-season digest), PAPACY-A, PAPACY-B, the verb lane's `confer` draw
(`audits/14_VERBS_BINDING.md` §1) and CR-88's vacancy duty.

## What it changes in `engine/season/` at runtime

Nothing on the game path. FA-P4's harness entry gains one world (`realm`) and its `vacancy` situation
takes a seat id. A run's `content_hash` equals the same seasons run through `populated.run` with the same
chooser on the same world after the same tick-0 act (the control FA-P4 already states).

## The problem (evidence)

- No scenario exercises the Church. FA-P4's three situations sit on the generic spine, which has no
  Church, no body and no creed.
- The vacancy already happens by itself and nothing follows: at seed 1 the Cardinal of Prudence died in
  three seasons and his seat was empty at the end (audit E-1; FA audit E-5 saw the same seat). `confer`
  formed 5 times and was attempted 0 at seed 0 (FA audit E-3).
- Two provided characters are defined by candidacy for a named Church seat (NPC-039, NPC-040,
  `npcs.yaml:332-345`) and the engine has no candidacy.

## The resolution, decided

**Situation.** `build_realm(seed)`; before season 1 the holder of `off_cardinal_prudence` `release`s his
seat through the real fold (FA-P4's pattern: a world the loop could have produced; if the verb lane makes
`release` a draw the scenario reports the band and a failed resignation is the opening situation). The
chair of the Church's treasury is empty at Himmelenger.

**Who the player may be** (one seat-holder; everyone else the shipped chooser; `play_surface.py::
dispatching_chooser`):

| seat | the choices offered (the aperture the engine computes; nothing scripted) | what makes them real |
|---|---|---|
| the Confessor | `confer` the chair on any person he knows (or wait); answer a candidate's `petition`; accept or refuse a `covenant` a candidate or the King offers; `issue` to the other Cardinals | the appointment is a draw: reception of the seat's body toward the conferee, standing, the incumbent if any (verb lane). A man raised too high may not take |
| a candidate (a Church person without the chair; the scenario offers each seated or sworn Church person) | `petition` the Confessor; `argue` to the Cardinals; `covenant` (a promise for the gift); `tell` of a rival's deeds | his petition is a claim in the Confessor's ledger, weighed by regard; a promise is a Record others can find |
| the King | `covenant` with the Confessor; `petition`; and, in the **control arm only** (no `patronage:` on the row), `confer` the chair himself | with PAPACY-B the Crown's `confer` is refused at `may_fill`; without it the Crown may fill the Church's treasury seat, which is the as-built state the arm exists to show |

**Stakes.** Whoever holds the chair holds `issue` over the Church's stores and, after PAPACY-E, the tithe
writ; he is the Confessor's creature or the Crown's; the loser holds a grievance in his own ledger.

**End.** (a) the chair is held on a hold that is not provisional: *filled*, with by whom and through which
seat; (b) it is held provisionally at the last season: *contested*; (c) three seasons pass with it empty:
*the long vacancy*. A stable continuation in every case: the world runs on.

**Legibility.** FA-P4's digest, per season: who holds which Church seat; each `petition`, `covenant`,
`confer` formed, attempted and its band; for each resolved `confer` the obstacle's term list (the SC
obstacle returns the terms it summed); the reason trail from the conferral to the question that occasioned
it (`01_CORE_reason_trail_in_the_act_store.md`).

**One code path.** The acts are the season loop's; the scenario adds a set-up act and a reader. Entered
from a running season the same situation is a death or a resignation at Himmelenger, and its outcome is a
`hold` every later act reads.

## Exact edits

1. `engine/season/harness/governance_spine.py` (FA-P4's `play` entry): `--world {spine, realm}` (default
   `spine`); `realm` builds through `harness/populated.py::build_realm`. `--situation vacancy:<seat id>`
   (default FA-P4's spine seat). `--as <seat id | case id>` selects the player's person.
2. The digest's seat filter takes a faction name (`Church of Solmund`) so the reader prints one
   institution's seats.
3. No edit under `loop/`, `state/`, `queries/`, `decision/`, `data/`.

## Gate (execution artifacts)

- `PYTHONHASHSEED=0 python -m engine.season.harness.governance_spine play --world realm --situation
  vacancy:off_cardinal_prudence --seasons 3 --seed s`, `s` in 0-4, all-NPC: each run ends in one of the
  three endings and prints which. Across the five seeds at least two different endings or two different
  holders occur (if every seed ends alike, the scenario shows no politics and the finding goes back to
  the `confer` draw and CR-88's duty, not to this file).
- With a player-proxy as the Confessor choosing a fixed conferee by policy: over 200 seeds the conferee is
  seated in some, seated provisionally in some and resisted in some (the draw), and the share seated is
  higher for a conferee the Cardinals regard well than for one they do not (two arms, exact odds printed).
- Control 1: the same seeds with no vacancy planted: no `tenure.opened` on the seat.
- Control 2: `content_hash` of each all-NPC run equals `populated.run` on the same world after the same
  tick-0 act.
- Control arm (patronage): the row's `patronage:` removed: at some seed the Crown's seat fills the chair.
  With it: never.

## Falsifier

A run whose ending is fixed by the seat-holder's identity alone (the same holder in every seed whatever
the draw). A digest line that cannot name the `Act.via` of a conferral. The scenario needing any act the
season loop cannot form.

## What is missing today, in order

1. `confer` is formed and never attempted (FA F-FA-02): CR-88's duty term, or until it lands a planted
   question carrying the vacancy (the scenario may plant the *question*, never the outcome).
2. `confer` is certain once admitted: the verb lane's draw.
3. The Crown may fill the chair: PAPACY-B's `patronage:`.
4. A candidate's `petition` naming a seat reaches the conferrer as a classed referent
   `[UNVERIFIED: whether a held petition's `terms` naming a seat puts the petitioner among the conferrer's
   candidates today; if not, it is the social verb lane's `petition` build-out]`.

## NERS reading

N: without a scenario the Church cannot be judged as play at all; this is the smallest one in which its
own people decide something that lasts. R: three seats to play, each with a different lever (the gift, the
suit, the bargain), and a world that fills or fails to fill the chair with nobody playing. S: it enters
and leaves by the loop's own acts and pauses nothing. E (last): one harness option and one filter over
FA-P4's entry.

## Cost class

Small build (harness only), after FA-P4.
