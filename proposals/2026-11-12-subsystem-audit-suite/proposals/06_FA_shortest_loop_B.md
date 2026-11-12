# FA-B4 — the shortest playable loop: one governance scenario a player can play, one realm that governs itself, and a line that says whether the loop closed

Reconciled: 2026-11-12, U5d closure — folded **A-10** and **A-47**. A-10 (governance is the loop's own verbs) confirms that the subsystem's exit is this instrument reading and no module. In the `recall` scenario the threshold opens the Duke's question; whether the player is revoked is the Duke's choice and then `revoke`'s resistible draw, so `loop_closed`'s `responded` counts attempts and reports their bands. `vacated` gains the cause `conquest` (A-58: seats pass with holdings when a place is seized) beside death, release, revocation and term.

## Status: PROPOSED

Source: `audits/06_FA_audit_addendum_B.md` §B3.5, §B6.1; the standing requirement of `AUDIT_BRIEF.md`
("each subsystem is a playable game"). **Extends** `06_FA_playable_scenario.md` (the first lane's
FA-P4), which it does not edit: it adds one situation composed of that file's two, one world option
and one reader. Depends on FA-P4 for `play`, `situation`, `digest` and `offered`.

## What it changes in `engine/season/` at runtime

Nothing on the game path. Three additions to the instrument `harness/governance_spine.py` that FA-P4
turns into a scenario runner. No file under `loop/`, `state/`, `queries/`, `decision/` or `data/`
changes, and a run's `content_hash` equals the same seasons run through `populated.run` with the same
chooser (FA-P4's control, unchanged).

## The problem (evidence)

- FA-P4 offers three situations (`vacancy`, `order`, `succession`), each a separate run. The loop the
  whole design set returns to is one sentence: an office receives an order it cannot fully satisfy,
  answers it, and is kept, recalled or replaced for the answer (addendum §B3.1, §B3.5: the Directive
  and its three answers, D5/D6/E11; the ladders' Required Obligations and Demotion Trigger; Leadership
  Deviation). No single run plays that sentence.
- The loop has five links and the verb table has a verb for each: `issue`; `comply`, `evade / defy` or
  `construe`; `revoke`, `open_case` or `arrest`; a seat's `hold` closing; `confer` or `succeed`.
- In computed play the realm closes one of the five at seed 0 and two at seeds 1 and 2: 29, 21 and 41
  writs issued over three seasons; 0 answers by an addressee; 0 responses; 0, 1 and 1 seats vacated,
  each by a death; 0 fillings (first audit E-5).
- No instrument says this in one line. `aperture` prints a funnel per verb; the first audit had to
  write a probe to read it.

## The resolution, decided

One scenario, one arm, one line. Ladder step 5: the pieces are FA-P4's and the three mechanism
proposals'; the alternative, a second runner for the realm, would be the second code path the standing
requirement forbids.

**The player's scenario, `recall`.** The player is the Count of chain `a` on the spine. At tick 0 the
Sovereign `issue`s a writ addressed to him (FA-P4's `order` situation). Each season he is offered his
answers beside everything else his seat opens. If he withholds for the recall threshold's seasons, the
Duke's question carries his seat; the Duke, run by the shipped chooser, revokes or does not. If he is
revoked the run does not end: he is offered what an unseated person is offered, and the Duke's later
questions carry the vacancy. The run ends on FA-P4's three endings, with one change: "the player holds
no seat" ends the run two seasons later, so that the filling of his seat is seen.

**The self-governing realm.** `play` with no player (`pick=None` for everyone) on the built realm
instead of the spine. It is `populated.run` with the digest printed; it exists so that the same
instrument that plays the scenario also reads the realm.

**The line.** After the last season, one reader prints the five links and whether each closed.

## Exact edits, by owner (all in `engine/season/harness/governance_spine.py`, the instrument's one owner)

**1. `situation(w, "recall", player)`.** FA-P4's `order` situation, unchanged; the name selects the
ending rule above. No new act.

**2. `play(..., world="spine")`.** A keyword `world: "spine" | "realm"`. `"realm"` builds
`populated.build_realm(seed)` and requires `situation=None` and `player=None`: the realm is read as it
is built, with no hand-made opening. The CLI gains `--world realm`. No default for seed or seasons
(the file is inside `tools/ci_sim_fabrication_check.py`'s scope, as FA-P4 notes).

**3. `loop_closed(w, since: int) -> dict`.** A pure reader over `w.log[since:]`, `w.acts` and
`w.tenures`, naming no Event kind literally (each is read off `data/verbs.py::VERB_TABLE`'s `emits`
for the verb named):

| key | counts |
|---|---|
| `ordered` | Events of `issue`'s kind |
| `answered` | Events of `comply`'s, `evade / defy`'s or `construe`'s kind whose actor is an addressee of the writ named (`person_q.addressed_to`) |
| `responded` | executed `revoke`, `open_case` or `arrest` acts whose actor issued a writ the act's subject (or the holder of the seat it names) withheld compliance on, earlier in the log |
| `vacated` | closes of a `hold` on an Office, by cause: death, release, revocation, term |
| `filled` | opens of a `hold` on an Office after a close of a `hold` on the same Office |
| `persons` | distinct actors over the five |

It returns the counts and `closed = all five > 0`. `play` prints it after the digest. It writes
nothing.

## Gate (execution artifact)

Three commands at `PYTHONHASHSEED=0`:

1. `governance_spine play 0 8 recall --pick <evade / defy each season>` (after FA-P1 and FA-P3): the
   digest shows the writ, a withheld answer each season, the Duke's `revoke` or its absence, and the
   line reads `ordered ≥ 1, answered ≥ 1`; if the Duke revoked, `responded ≥ 1, vacated ≥ 1`. Whether
   the Duke revokes is the chooser's and is reported, not asserted.
2. The same with `--pick <comply each season>`: `answered ≥ 1`, `responded 0`, and the player still
   seated at the end. The two runs differ in the line, which is the scenario's proof that the choice
   changes what happens.
3. `governance_spine play SEED 8 --world realm` at seeds 0, 1 and 2. **Before** any mechanism proposal
   lands this prints `ordered > 0`, `answered 0`, `responded 0`, `filled 0`, `closed False`: the first
   audit's verdict as one line, and the baseline. **The subsystem's exit** is `closed True` at all
   three seeds with `persons ≥ 3`, on the realm, with no player.

## Falsifier

- The control: `--world realm` reproduces `populated.run`'s `content_hash` for the same seed and
  seasons. If it does not, the instrument moved the game.
- `loop_closed` on a planted log: one `issue` Event and nothing else reads `ordered 1` and four zeros;
  a planted `comply` by a non-addressee does not count as `answered`.
- A realm that closes the loop only through one person's five acts fails `persons ≥ 3`: a loop one
  officer closes on himself is a script, not a realm.

## What it does not do

It adds no rule, no situation the fold could not have produced and no test of a realm count (the
exit is an instrument reading at named seeds, in the instrument's output). It does not include war,
treaty or vote in the loop: none of them executes yet, and a loop that waits on them never closes.

## NERS reading

- **N.** From the player's side, one run in which a refusal has a face and a cost. From the realm's
  side, the same five links with nobody watching. Remove it and "plays alone" is three demonstrations
  and no game.
- **R.** The player may comply, bargain by `petition`, defy, or misread; the superior may ignore,
  recall or prosecute; the seat may be filled by a rival. The no-player half is the exit itself.
- **S.** One instrument at two fidelities, the ruled doctrine (ED-SC-0013).
- **E, last.** One keyword, one situation name, one reader of thirty lines.

## Cost class

Small build (harness only). No mover. Depends on `06_FA_playable_scenario.md`; its gate 1 and the
exit depend on `06_FA_decree_binds.md` and `06_FA_seat_terms_and_turnover.md`.
