# FA-P4 — a governance scenario that plays: three situations on the spine, a digest, three endings

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-08 — the heir's `succeed` and the tick-0 set-up acts are draws; a set-up that fails is reported, not forced.

Reconciled: 2026-11-12, U5d closure — folded **A-19** (the crown by the deed race), **A-10** and **A-21**. The `succession` situation no longer assumes one title and a first valid claim: `successions` is a set of titles (`22_HAPPENINGS_B_the_throne_is_never_stranded.md` edit 2 as reconciled) and the claim is a draw whose odds read what others hold of each claimant's deeds; the scenario-local mapping in `play` is a tuple of titles and the digest reports every claimant and the band. The `order` situation is A-21's proclaimed decree as written. A-10 confirms the form (a scenario on the season loop; no governance module), so the audit's §11 item 2 no longer hangs over this file. Steps rewritten: the `succession` row of the situation table and the last paragraph of the edits (the mapping's value shape). The gate gains one arm: with two listed titles held, the seat goes to each in at least one seed of the swept set.

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-28) — all three readers of `SUCCESSIONS` hold the one dict by `from`-import; an in-place change reaches them and a rebinding does not.

Source: `audits/06_FA_audit.md` F-FA-07, §9, §6.2 R-19, §13 (NPC-020, NPC-031, NPC-083), §15 (b), (d).

## What it changes in `engine/season/` at runtime

Nothing on the game path. It adds a `play` entry to the instrument `harness/governance_spine.py`, which
today prints a census, and gives the spine fixture's offices the conferral and revocation bases they lack
(a declared mover of the fixture's own hash, and of nothing else). No file under `loop/`, `state/`,
`queries/`, `decision/` or `data/` changes; a run's `content_hash` equals the same seasons run through
`populated.run` with the same chooser on the same built world (the control).

## The problem (evidence)

- `python -m engine.season.harness.governance_spine` builds the 13-seat world and prints its shape; it runs
  no season (`harness/governance_spine.py:249-251`).
- The dispatch seam exists (`harness/play_surface.py::dispatching_chooser`) and so does the development
  space that ranks and selects from the candidate set (`decision/sheet.py::development_space`). Nothing
  joins them to a governance situation.
- The spine as built has no situation: at seeds 0 to 4 over four seasons no seat was vacant, no writ was
  held by an addressee, no oath was released (audit E-4).
- No reader prints, per season, who holds what and what was ordered and answered. A refusal of `confer` or
  `establish` records no clause (H-252).
- The ruled doctrine is one engine at two fidelities, with a slate of specific events and a budget of scene
  actions (ED-SC-0013). The engine has the budget and the chooser; FA has no slate a person could look at.

## The resolution, decided

One harness entry, composed of pieces that exist. The player is one seat-holder of the spine; everyone else
is the shipped chooser. Each scenario begins with a situation **made by the game's own effects at tick 0**,
never by a branch on an id and never by writing a carrier directly, so every scenario world is one the loop
could have produced.

| situation | how it is made (real acts through the real fold, before season 1) | what it exercises |
|---|---|---|
| `vacancy` | the Count of chain `a` `release`s his seat | the player, as Duke of `a`, is offered `confer` onto it; with FA-P3, a termed seat does the same on a clock |
| `order` | the Sovereign `issue`s a writ addressed to the player's seat-holder | with FA-P1: `comply`, `evade / defy`, `construe`, and the recall that follows defiance |
| `succession` | the Sovereign holds a second seat registered in a scenario-local `successions` row to a title the player holds, then `release`s it | the heir's `succeed` (a draw with graded bands, `14_VERBS_BINDING_C_turnover.md`: the claim may be contested, delayed or fail); a banned heir is refused (eligibility) |

*(Reconciled, D-08: under the standing rule `release`, `issue`, `confer` and `succeed` resolve by a
draw once their verb lanes land, so a set-up act at tick 0 can come out otherwise. The scenario does
not force it: it reports the band its set-up act reached, and a set-up that failed is itself the
scenario's opening situation (a Count who could not lay his seat down; a writ botched). No seed is
selected for the outcome.)*

Ladder step 5. The alternative, a second world builder with situations written into state, would be a fork
of `build` and the thing the standing requirement forbids.

## Exact edits, by owner

**`engine/season/governance_spine.yaml` and `harness/governance_spine.py::build`** (the one edit that moves
a hash, the fixture's own). Every spine office is built today with no conferral and no revocation basis, so
`may_fill` is false for every pair and no seat on the spine can be filled, stripped or claimed (probe at
`601e715`: thirteen offices, all `(None, None)`; `may_fill` of the Duke over the Count beneath him False).
Each `rungs:` row gains `conferral:` and `revocation:`; `build` passes them to `Office`. Values: the realm
row `conferral: null`, `revocation: null` (nothing stands above it); every other row `conferral:
appointed`, `revocation: rung_above_same_faction`, the generic case of ED-IN-0256 (2) and (3)
`[ASSUMPTION; medium; Jordan to correct; revert: drop the two keys]`. The file's closing note, which says
the two bases have "no code-readable owner yet", is replaced by a pointer to `rosters.yaml:
conferral_bases` and `revocation_bases`. The spine's `content_hash` moves at build (`Office.conferral` and
`.revocation` are hashed) and is re-recorded; the realm does not move.

**`engine/season/harness/governance_spine.py`** (the fixture's one owner).

- `situation(w, name, player) -> list[Act]`: the hand-built acts of the table, resolved through
  `SeasonDriver`'s own fold at tick 0. It returns the acts so the digest can cite them. It refuses a
  situation whose opening act the fold refuses, naming the Event, so a scenario cannot start from a state
  the engine did not produce.
- `digest(w, since: int) -> list[str]`: a pure reader over `w.log[since:]` and `w.tenures`, one line per
  occurrence of: a seat opened or closed (who, which seat, by which act and through which seat); a writ
  issued (issuer, addressees) and each answer to it; a ban or custody opened or ended; an oath taken or
  released; stores moved by `requisition`. It reads the Event kinds off `data/verbs.py::VERB_TABLE`'s
  `emits`, so it names no kind literally. It writes nothing.
- `offered(p, v, s, ask_budget, auto) -> list[str]`: for the player's deliberation, the seat-gated
  candidates `opening_set` formed (through the same `make_ranker` call `development_space` uses), grouped by
  the remit act that opens them, each with the seat it would be exercised through.
- `play(seed, seasons, situation, player, pick=None)`: builds the spine, makes the situation, and runs
  `seasons` seasons with `dispatching_chooser(auto, {player: callback})`. `callback` prints `offered` and
  takes `pick`'s indices through `development_space`; `pick=None` is the shipped chooser for everyone (the
  control arm). After each season it prints `digest`. It stops at the first of three endings, each a Query:
  the player holds no seat (`w.seat_holds(player)` empty); `world_q.endings_reached(w)` is non-empty; the
  season count is reached.
- `__main__`: `governance_spine play SEED SEASONS {vacancy|order|succession} [--player ID] [--pick I,I,…]`,
  with no default for seed or seasons (the file sits inside `tools/ci_sim_fabrication_check.py`'s scope, as
  `harness/storybar.py` notes for the same shape). The bare invocation still prints the census.

The `succession` situation needs a title that passes a seat. `rosters.yaml: successions` is keyed on
`offices.yaml` row ids, which the spine does not use; `play` therefore passes the gate a scenario-local
mapping through the same indirection the tests use (`monkeypatch` of `SUCCESSIONS` in
`test_in61_succession.py`), scoped to the run. [GROUNDED, 25 G-28: all three readers hold a
`from`-import of the one dict object and read it at call time: `state/gate.py:54` (`:743`, `:782`),
`decision/options.py:34` (`:240`), `loop/effects_governance.py:16` (`:164`). An in-place change reaches all
three, which is what the test does (`monkeypatch.setitem(SUCCESSIONS, …)`, `test_in61_succession.py:161`);
rebinding `data.rosters.SUCCESSIONS` would reach none. The scenario must mutate in place; no reader is edited.]

## Gate (execution artifact)

Three commands, each printing a digest that contains the scenario's beat, at seed 0:

1. `play 0 2 vacancy --pick <the confer candidate>`: a `tenure.opened` line naming the vacant Count's seat
   and the conferee; then the same command with no `--pick` (the control) prints whatever the chooser did,
   and its `content_hash` equals `populated.run`'s for the same world and seasons.
2. `play 0 3 succession --pick <the succeed candidate>`: a `succession.claimed` line; with the player's
   person banned first, the pick is refused and the digest says `succession.refused`.
3. `play 0 4 order` (after FA-P1): an answer line for the writ either way. Before FA-P1 this scenario
   prints the writ and no answer, which is the audit's F-FA-01 made visible; it is still shipped, because a
   scenario that shows an absence is an instrument doing its job.

Each ending is reached once: a pick that `release`s the player's only seat ends the run on "holds no seat".

## Falsifier

- The control: `pick=None` reproduces `populated.run`'s hash. If it does not, the harness moved the game.
- A situation the fold refuses stops the run with the refusing Event, never a silent fallback.
- `digest` on a world with no governance Event prints nothing (a planted empty log), and on a planted
  `tenure.opened` prints exactly one line.

## What it does not do

It is not a client, a UI or a save format. It adds no rule and validates no pick beyond what
`development_space` already refuses. It does not make the realm playable as a faction game; it makes one
seat's season of rule runnable, observable and endable, which is what "plays alone" asks of this subsystem.

## NERS reading

- **N.** From the player's side there is at last something to look at; from the engine's side nothing is
  added. Removing it returns FA to a subsystem that can only be judged by counting Events.
- **R.** The three situations are the three things the charge asks about (a vacancy, a decree, a
  succession), and each can go more than one way.
- **S.** It zooms in on one seat and pauses nothing: the other twelve persons run on the shipped chooser in
  the same seasons. It is the played fidelity of the same engine.
- **E, last.** Four functions in an existing instrument, reading existing owners. No new module.

## Cost class

Small build. One declared mover (the spine fixture's build hash). Depends on nothing; FA-P1 and FA-P3 make
scenarios 3 and 1 richer.
