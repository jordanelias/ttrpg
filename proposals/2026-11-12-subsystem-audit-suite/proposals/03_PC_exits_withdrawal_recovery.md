# PC — a priced withdrawal, the beaten fighter's exit, and recovery that takes more than one act

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-04, D-05 — Part B decided by the standing rule (a felling's death is `14_VERBS_PHYSICAL_A` A3's mortal-wound draw, adopted, not restated; terms follow context); Part C's `tend` becomes a graded draw.

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.1, §1.3, §1.4) — three further changes. (1) Part A's ground is restated (addendum C-2, C-3; A-1): the breach is that a played person holds an unpriced choice an NPC lacks (one kind of agent), and equal plans must agree **exactly** (Layer 1 §C.4), not in expectation; the quarantined duality note is PROPOSED in its ledger row (25 G-12) and is not the reason. (2) Part B's `Problem` and `two options` text is history: the standing rule and A-16 decided it, the yield is a draw under every term (`16_PESSIMIST_PC_A_the_yield_is_a_draw.md`), and its tables move with A-31's damage scale (`U5b_PC_rulings_in_the_fight.md` §4). (3) Part C's patient-side term is A-8's: the wound a `tend` mends is the level the season charges him, on the one sampler (A-5).

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.1 Part B (the `Problem` and `two options` text is history: removed, the decided form kept), §2 rows A-8/A-24 (Part C's obstacle is `tend_ob` only; the patient's headroom scales the band, not the obstacle), A-31 (Part A's and B's tables re-read after UPR §4), A-81 and `U3_CONFLICT_LEDGER.md` C3-C11 (a clean withdrawal and a Failure name their durable write), 7b-14 (Part C tests, corrected at the tree to the existing `test_cp_t03_08_tend_on_the_wounded.py`); `U3_CONFLICT_LEDGER.md` C3-C8 (the mortal-wound draw runs in `modules/combat/`, keyed `H(seed, tick, subject, "fight.mortal")`, operands from `22_HAPPENINGS_A`'s `mortal_terms`; Part B is a pointer to `14_VERBS_PHYSICAL_A` A3); `U3_DEPENDENCY_ORDER.md` §4.1 rows 47 and 55 and `U5_CONFLICTS_U5c.md` C-32 / U1 §4 P-12 (the `tend` row is owned by `14_VERBS_MATERIAL_A_mending.md` §6; Part C's text is its input and lands there; the yield is `16_PESSIMIST_PC_A`'s); A-30 (Part A's withdrawal draw is keyed); D-U1-08 (the pursuit strike's pool and obstacle by the one pool rule and `opposed_ob`). The Status paragraph's "Part B is Jordan's" sentence is replaced: Part B was decided by the standing rule. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "task difficulty" → "difficulty" (glossary *difficulty*).

**Depends on:** `03_PC_duel_round_and_approach_B.md` steps 1–2 (B16: per-party deciders, the round key); `14_VERBS_PHYSICAL_A_custody_and_force.md` A3 (B15: the mortal-wound draw); `16_PESSIMIST_PC_A_the_yield_is_a_draw.md` (B15); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (B07) and `14_VERBS_MATERIAL_A_mending.md` §6 (B12) for Part C.
**Lands in batch:** Part A in B16 (`B16-pc-round`, with PB step 4); Part B lands nothing of its own (A3 in B15); Part C is carried by `14_VERBS_MATERIAL_A_mending.md` §6 in B12.

## Status: PROPOSED

Lane: PC (Part C touches `_eff_tend`, whose hole row H-304 is filed with SE). Source:
`audits/03_PC_audit.md` F-PC-04, F-PC-05; resolutions R-PC-11, R-PC-14; §11 item 1. Read at `601e715`.
Reference only (CLAUDE.md §0.05); not ratified by being written. *(Reconciled, W3-1:)* Part B was
decided by the standing rule (A-24) and A-16; it adopts `14_VERBS_PHYSICAL_A` A3 and adds nothing.

## What it changes in `engine/season/` at runtime

Part A: nothing in an AUTOMATED run (`decide=None` is byte-identical); a PLAYABLE fight in which the
played person withdraws now draws a contest. Part B: through `14_VERBS_PHYSICAL_A` A3's mortal-wound
draw, a declared mover of every season in which a fight reaches `Felled`. Part C: nothing at the shipped value; a swept arm makes
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
  1. `clean = u < S.disengage_clean_p(W, P, cfg, TR)`, `u` the draw keyed `(t, 'withdraw', W)` under the
     round's key (A-30; `03_PC_duel_round_and_approach_B.md` §2).
  2. Clean: emit `withdraw(turn=t, by=W, clean=True)`; the fight ends, result 0, no upset draw (as now).
     *(Reconciled, A-81 / C3-C11:)* the band still writes: the withdraw Event is witnessed and WITNESS
     deposits it (`co_located` firsthand to those present; the withdrawer's own claim of his act), so the
     no-null-scene reading counts it.
  3. Read: emit `withdraw(turn=t, by=W, clean=False)`; `P` strikes once with
     `core.resolve(pool_of(P.score, P.addends, pool_add, pool_floor), S.pursuit_sigma(P, W, fat_P, fat_W, cfg, TR),
     u_strike, core.ob_from_defender(W))` (the one pool rule and `opposed_ob` on W's skill score, D-U1-08,
     A-79), wounding through the one damage site (`_wound('pursuit', P, W, d)`).
     If `W` is felled the fight is decided. Otherwise the turn is then fought as an engaged turn with
     `P` as `first` (he holds the tempo, as `wrapper.py:219` gives the pursuer).
- No new constant: both probabilities and the strike are existing functions on existing coefficients.

**Who may withdraw.** *(Reconciled:)* every party, through his decider (`03_PC_duel_round_and_approach_B.md`
§5); an NPC's decider returns `withdraw` only where a response row authors it.

**Gate.** The table above re-run on the same seeds: "both stand" under withdraw-at-first-wound falls
below 50.7%, and the withdrawer takes a pursuit wound in some seeds (count reported). REM-31's
equality (a scripted decider that always engages ends at the AUTOMATED `content_hash`) is unchanged.
*(Reconciled, A-31:)* the table's figures were taken before UPR §4's damage scale; re-read after it.

**Tests (W3-1, test 9).** In `engine/season/tests/test_combat_module.py`:
`test_a_read_withdrawal_draws_one_pursuit_strike` (`disengage_clean_p` forced to 0: one `withdraw(clean=False)`
event and one `pursuit` wound event follow), `test_a_clean_withdrawal_ends_the_fight_and_emits_the_event`
(forced to 1.0: one `withdraw(clean=True)`, result 0, today's table reproduced: the planted-failure control);
REM-31's equality stays in `test_rem31_grid_suspension.py`. The 300-seed table is a one-time reading in the
commit body (`R1_READ.md` 7b-20). Hash movers: none in an AUTOMATED run; PLAYABLE fights with a withdrawal.
Lands: B16 with PB step 4; `sonnet`.

**Falsifier.** A withdrawal that still ends every scene it is called in; or an AUTOMATED fight whose
draw sequence moved. Planted failure: `disengage_clean_p` forced to 1.0 reproduces today's table.

## Part B — the beaten fighter's exit

*(Reconciled, W3-1: the first draft's `Problem` (a plain `fight` killing in 200 of 200 hand-built season
fights, H-263; the per-term table of 99.8% / 3.0% / 0 felled at `death` / `yield` / `blood`, to be re-read
after UPR §4) and its two options (A: a fight is to the death outside a duel or arrest; B: `duel_terms` gains
`fight: yield`) were decided by the standing rule and A-16, and are removed as instruction. Research
precedent stays cited: `research/game_precedent_suite/dispositions/D_T03.md` rows 17, 27, 33, 36.)*

### Part B, decided by the standing rule (Reconciled 2026-11-12, `audits/18_DETERMINISM_SWEEP.md` D-04)

Jordan's ruling of 2026-11-12 (*"we do not do deterministic"*, `AUDIT_BRIEF.md`) is a later ruling
that answers §11 item 1 (ladder step 1): a fight may not kill with certainty. Neither A nor B above
is enough alone (B removes the death by default; A keeps it certain). Decided:

- **A felling is not a death; the death is a draw.** The draw is specified ONCE, at
  `14_VERBS_PHYSICAL_A_custody_and_force.md` A3 (the mortal-wound draw, run in `modules/combat/` and
  returned on the typed outcome, never in `seam/wrappers/combat.py` (`04` §A.2: an adapter writes
  nothing; `U3_CONFLICT_LEDGER.md` C3-C8); keyed `H(seed, tick, subject, "fight.mortal")` (A-30); its
  operands from `22_HAPPENINGS_A`'s `mortal_terms`, passed by the caller; Failure dies, Partial left for
  dead with the lasting mark, Success and better lives). This part adopts it and adds nothing to it, so
  there is one rule, not two. The yield itself is `16_PESSIMIST_PC_A_the_yield_is_a_draw.md`'s (U3 §4.1
  row 55).
- **The term follows the context** (B's finer form): A3's `context_terms` roster, keyed on
  `violence_contexts`' names, is that form; this part adopts it.
- **Gate** (A3's, restated as this part's acceptance): the F-PC-04 probe's deaths fall strictly below
  200 of 200 and above 0; the control `mortal_wound_ob` at an unreachable value reproduces 200 of 200.
  Hash movers: every season in which a `fight`, `accept` or `capture` reaches `Felled`.

## Part C — recovery is a swept fraction (decided; ships at today's value)

*(Reconciled, W3-1, C-32 / U1 P-12:)* the `tend` row is owned by `14_VERBS_MATERIAL_A_mending.md` §6; this
Part's rule, fixture and gate are inputs that land there (B12), not a second row.

*(Reconciled 2026-11-12, D-05: under the standing rule a `tend` that heals with certainty is a
deterministic outcome; it becomes a draw. Corrected rule below; the fraction stays as the
`Success` band's size.)* `tend` rolls through the one task draw
(`proposals/18_DETERMINISM_task_draw_for_uncontested_verbs.md`): pool = the tender's `healing`
skill (or `pool_default`), obstacle = `tend_ob` (difficulty, proposed 1) only; the patient's
headroom scales the band's share (`ceil(tend_fraction × headroom)`), not the obstacle (A-8: a wound is a
level against a roller, and the tender is the roller; a wound-marks obstacle term would count the headroom
twice). `Failure`: no change, `tend.failed` (a new band kind on the row), witnessed and deposited to the
tender and the patient (A-81); `Partial`: `ceil(tend_fraction/2 × headroom)`; `Success`:
`ceil(tend_fraction × headroom)`; `Overwhelming`: to the ceiling.

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

**Tests (W3-1, `R1_READ.md` 7b-14, corrected at the tree).** In the existing
`engine/season/tests/test_cp_t03_08_tend_on_the_wounded.py`: `test_failure_changes_nothing`,
`test_success_restores_the_fraction_of_headroom`, `test_fraction_one_reproduces_the_old_tend`. Control:
`tend_fraction = 1.0` with an always-`Overwhelming` roll reproduces today's hash. Lands with
`14_VERBS_MATERIAL_A_mending.md` §6 in B12; `sonnet`.

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
