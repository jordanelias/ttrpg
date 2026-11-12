# PC — a priced withdrawal, the beaten fighter's exit, and recovery that takes more than one act

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-04, D-05 — Part B decided by the standing rule (a felling's death is `14_VERBS_PHYSICAL_A` A3's mortal-wound draw, adopted, not restated; terms follow context); Part C's `tend` becomes a graded draw.

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.1, §1.3, §1.4) — three further changes. (1) Part A's ground is restated (addendum C-2, C-3; A-1): the breach is that a played person holds an unpriced choice an NPC lacks (one kind of agent), and equal plans must agree **exactly** (Layer 1 §C.4), not in expectation; the quarantined duality note is PROPOSED in its ledger row (25 G-12) and is not the reason. (2) Part B's `Problem` and `two options` text is history: the standing rule and A-16 decided it, the yield is a draw under every term (`16_PESSIMIST_PC_A_the_yield_is_a_draw.md`), and its tables move with A-31's damage scale (`U5b_PC_rulings_in_the_fight.md` §4). (3) Part C's patient-side term is A-8's: the wound a `tend` mends is the level the season charges him, on the one sampler (A-5).

## Status: PROPOSED

Lane: PC (Part C touches `_eff_tend`, whose hole row H-304 is filed with SE). Source:
`audits/03_PC_audit.md` F-PC-04, F-PC-05; resolutions R-PC-11, R-PC-14; §11 item 1. Read at `601e715`.
Reference only (CLAUDE.md §0.05); not ratified by being written. **Part B is a design choice that
survives the five-step ladder and is Jordan's; it is specified here so it can be built the day it is
ruled and changes nothing until then.**

## What it changes in `engine/season/` at runtime

Part A: nothing in an AUTOMATED run (`decide=None` is byte-identical); a PLAYABLE fight in which the
played person withdraws now draws a contest. Part B (if ruled): the terms a plain `fight` is fought
under, a declared mover of every season fight. Part C: nothing at the shipped value; a swept arm makes
`tend` restore part of a body.

## Part A — withdrawal is contested (decided; takeable)

**Problem.** `modules/combat/wrapper.py:586-592`: on `withdraw` the loop breaks with result 0. No
draw, no pursuit. Measured through the registered entry (300 world seeds, tiny_world, lethal terms):

| policy for the played fighter | he is felled | his opponent is felled | both stand |
|---|---|---|---|
| engage every turn (equals AUTOMATED) | 52.0% | 47.7% | 0.3% |
| withdraw at his first wound | 14.3% | 35.0% | 50.7% |
| withdraw when behind | 17.0% | 42.7% | 40.3% |

The engine already owns the act one level down: a reach weapon's fighting withdrawal inside an
engagement is an attempt, a read contest (`combat_systems.py:1000-1004`, `disengage_clean_p`) and, when
read, a pursuing strike (`wrapper.py:206-219`, `pursuit_sigma` at `combat_systems.py:1357-1378`). Two
exits for one act, one of them free. *(Reconciled:)* the ground is Layer 1, not the quarantined duality
note: a played person holds a choice an NPC lacks and it is unpriced (one kind of agent, CHAR §0A I-1),
and a played and an automatic fight with equal plans agree exactly (`03_VERBS_AND_LOOPS.md:146-153`;
A-1). The table above shows the unpriced choice; no expectation test is needed to see it.

**Resolution** (ladder rung 5; CLAUDE.md §0, compose on the single owner). The turn-level withdrawal
resolves through the same two functions.

- The decider says who withdraws. `fight(inp, rng, decide=None)` keeps its signature; the host's
  adapter passes a decider per played claimant, and the module asks each in claimant order
  (`deciders: Mapping[str, Callable[[CombatTurnView], str]]` replaces the single callable inside
  `fight.py`; `PlayHost` is unchanged). The first to answer `withdraw` is the withdrawer `W`; the other
  party is `P`.
- In `wrapper.fight`, on a withdrawal by `W` at turn `t`:
  1. `clean = rng.random() < S.disengage_clean_p(W, P, cfg, TR)`.
  2. Clean: emit `withdraw(turn=t, by=W, clean=True)`; the fight ends, result 0, no upset draw (as now).
  3. Read: emit `withdraw(turn=t, by=W, clean=False)`; `P` strikes once with
     `core.resolve(resolution_pool(P.faculty), S.pursuit_sigma(P, W, fat_P, fat_W, cfg, TR), rng,
     core.ob_from_defender(W))`, wounding through the one damage site (`_wound('pursuit', P, W, d)`).
     If `W` is felled the fight is decided. Otherwise the turn is then fought as an engaged turn with
     `P` as `first` (he holds the tempo, as `wrapper.py:219` gives the pursuer).
- No new constant: both probabilities and the strike are existing functions on existing coefficients.

**Who may withdraw.** *(Reconciled:)* every party, through his decider (`03_PC_duel_round_and_approach_B.md`
§5); an NPC's decider returns `withdraw` only where a response row authors it.

**Gate.** The table above re-run on the same seeds: "both stand" under withdraw-at-first-wound falls
below 50.7%, and the withdrawer takes a pursuit wound in some seeds (count reported). REM-31's
equality (a scripted decider that always engages ends at the AUTOMATED `content_hash`) is unchanged.

**Falsifier.** A withdrawal that still ends every scene it is called in; or an AUTOMATED fight whose
draw sequence moved. Planted failure: `disengage_clean_p` forced to 1.0 reproduces today's table.

## Part B — the beaten fighter's exit (Jordan's; see §11 item 1 of the audit)

**Problem.** A plain `fight` kills in 200 of 200 hand-built season fights (H-263), and in the 143
case worlds all eight fought `fight` scenes were graded `Felled`. Non-lethal endings exist only where
`rosters.yaml: duel_terms` names the verb (`capture: yield`, `accept: blood`). The engine's own
readings for the season-default mirror, 1,000 fights per term:

| term | a fighter is felled | ends in a yield | undecided |
|---|---|---|---|
| `death` (`fight` today) | 99.8% | 0 | 0.2% |
| `yield` (stops at half Health) | 3.0% | 96.8% | 0.2% |
| `blood` (stops at the first wound) | 0 | 100% | 0 |

**The two options, as games.** A (as coded): outside a duel or an arrest a fight is to the death.
B: every fight carries a concession rule and the victor decides what follows.

**B's smallest faithful form, if ruled.**

- `engine/season/rosters.yaml: duel_terms` gains `fight: yield`. That is the whole of the mechanism:
  `combat_input` already carries the term (`seam/wrappers/combat.py:155-177`), `_eff_kill` already
  writes a yielder by his own band, and `Event.ending` already names him `yielded`.
- The `fight` row's `Wounded` band declares `duel.yielded`, earned by the yielder alone as on `accept`
  (`loop/effects_combat.py:234-238`).
- What the victor may do with a man who has yielded is his next act through verbs that exist: `fight`
  him again under the `defence` or `crime` context if one holds, `capture` him through a seat, or
  nothing. No new verb.
- A finer form (the term set by the context that licensed the fight: `war` → `death`, `crime` and
  `defence` → `yield`) is a second roster, keyed on `violence_contexts`' names; it is named here and
  not designed.

**Gate, if built.** The 200-seed season probe: deaths fall from 200 to the term's share; every yield
emits `duel.yielded`; with the roster line removed the pre-change hash returns.

**Research.** Four independent games put a state between standing and dead and make the victor's
disposition the consequence (Griftlands' surrender and spare-or-kill; Jagged Alliance 2 and Kenshi
capture; Wildermyth's mortal choice: `research/game_precedent_suite/dispositions/D_T03.md` rows 17, 27,
33, 36). Research informs and does not settle (`research/00_INDEX.md` §1).

### Part B, decided by the standing rule (Reconciled 2026-11-12, `audits/18_DETERMINISM_SWEEP.md` D-04)

Jordan's ruling of 2026-11-12 (*"we do not do deterministic"*, `AUDIT_BRIEF.md`) is a later ruling
that answers §11 item 1 (ladder step 1): a fight may not kill with certainty. Neither A nor B above
is enough alone (B removes the death by default; A keeps it certain). Decided:

- **A felling is not a death; the death is a draw.** The draw is specified ONCE, at
  `14_VERBS_PHYSICAL_A_custody_and_force.md` A3 (the mortal-wound draw in `seam/wrappers/combat.py`
  after the scene: pool from the felled man's body band, obstacle `Fixtures.mortal_wound_ob[terms]`
  plus named modifiers, one roller; Failure dies, Partial left for dead with the lasting mark, Success
  and better lives). This part adopts it and adds nothing to it, so there is one rule, not two.
- **The term follows the context** (B's finer form): A3's `context_terms` roster, keyed on
  `violence_contexts`' names, is that form; this part adopts it.
- **Gate** (A3's, restated as this part's acceptance): the F-PC-04 probe's deaths fall strictly below
  200 of 200 and above 0; the control `mortal_wound_ob` at an unreachable value reproduces 200 of 200.
  Hash movers: every season in which a `fight`, `accept` or `capture` reaches `Felled`.

## Part C — recovery is a swept fraction (decided; ships at today's value)

*(Reconciled 2026-11-12, D-05: under the standing rule a `tend` that heals with certainty is a
deterministic outcome; it becomes a draw. Corrected rule below; the fraction stays as the
`Success` band's size.)* `tend` rolls through the one task draw
(`proposals/18_DETERMINISM_task_draw_for_uncontested_verbs.md`): pool = the tender's `healing`
capability (or `pool_default`), obstacle = `tend_ob` (task difficulty, proposed 1) `+` the patient's
wound marks below his ceiling. `Failure`: no change, `tend.failed` (a new band kind on the row);
`Partial`: `ceil(tend_fraction/2 × headroom)`; `Success`: `ceil(tend_fraction × headroom)`;
`Overwhelming`: to the ceiling.

**Problem.** `loop/effects_combat.py:766-790`: one `tend` restores a body to its ceiling in one act.
The function's own note calls that an assumption and names the revert: "a swept fixture fraction of
the headroom — #453's 'fast partial and slow full form', C-48". H-304 measures the cost on the larder
side (a starving cohort restored whole by resting). The case corpus asks for two recoveries of
different speed (SCN-03) and for a wound that lasts until someone spends a scene on it (ARC-53).

**Resolution** (rung 3: the design document's own phrase, already quoted at the owner).

- `engine/season/data/fixtures.py`: `tend_fraction`, a number in (0, 1], shipped `1.0` (today's
  behaviour, hash EQUAL), swept `1.0 / 0.5 / 0.25`; a hole-register row graded `assumption` with that
  site and sweep.
- `_eff_tend`: `whole = p.body + ceil(tend_fraction × (max(p.body, p.body_ceiling) − p.body))`.
- The shipped value is not changed here: choosing it is a balance call and the campaign-level
  instrument has no live successor (CLAUDE.md §7).

**Gate.** At 0.5 a body of 400 under a ceiling of 1000 reads 700 after one `tend` and 850 after two;
at 1.0 the existing `tend` tests and the season hashes are unchanged.

**Falsifier.** A second `tend` at 0.5 that moves nothing; a hash that moves at 1.0.

## NERS reading

- N: from above, R-09 asks for graded and recoverable chains and the plain fight has one ending;
  from the player's side, the only in-fight choice is free; laterally, the engine has a contested
  withdrawal and a yield term that the fight does not use. Each part removes a doubled or missing rule.
- R: a beaten enemy who lives is a person with a grievance, a ransom or a debt; a wound that takes
  seasons to mend is a standing fact others can act on; a withdrawal that can fail is a decision.
- S: one withdrawal rule at both cadences; one term roster for every verb contesting `the body`.
- E, last: Part A and Part B add no constant and no verb; Part C adds one fixture. High for A and B;
  moderate for C until its value is chosen.

## Cost class

Part A: small build. Part B: an edit (two data lines), after a ruling. Part C: an edit.
