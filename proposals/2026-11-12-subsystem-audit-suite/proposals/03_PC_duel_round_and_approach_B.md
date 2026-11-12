# PC — the duel round and the approach, B: one round, an approach per phase of the engagement, a chooser for every party

Folded: 2026-11-12, lane 29 (`audits/29_ONE_OPPOSED_RULE.md` §4, §7; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md` edit 3), on Jordan's A-71 — two changes; the round, the approach and the deciders stand. (1) `DuelRoundInput` carries `opposition_rate`, `pool_add` and `pool_floor` raw, as `PersonalCombatInput` does, so a round called from a field (A-4) is opposed by the one function at the one rate and the caller composes nothing. (2) Every reading taken on the half-score obstacle (§3's transfer row: mean rounds 2.34 / 3.50 / 6.16, undecided up to 7.9% with both defensive; `audits/03_PC_audit_addendum_B.md` E-B10 to E-B14, as `U5b_PC_rulings_in_the_fight.md` §5 cites them) is re-read after that proposal's gate 2, at `0.4 × the defender's trained score` and the A-31 scale. Measured there on whole fights: 4.27 turns, 4.50 wounding blows, a lead change in 45.2%, 0.1% undecided, and the same at every rank; a lean that makes both sides defensive is the one place a stall can re-enter, so step 3's added gate reads the undecided share of the both-defensive cell against the 2% bound.

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-11 — the upset flip is no longer left on the unread integer; it becomes a tracked riposte (`18_DETERMINISM_no_certain_matchup.md`).

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.3, §1.4) — five rulings folded. A-4: a duel inside a field or a skirmish is a nested contest counted against a cap of 1, and callables supplied for persons are one declared class of adapter input (§4, §8 items 4–5, step 5; the cap and the seam function are `U5b_PC_rulings_in_the_fight.md` §1). A-9: a turn is a short sequence, which admits the in-round consult (§8 item 3; one sentence owed to the ratified suspension). A-31 and D-40: steps 3a–3e land after the damage scale and the commit window, the transfer ships at a coefficient of 0, and step 3 gains the pessimist's gate (§3, §7). A-6, A-7, A-8: `faculties` on the record is the trained score, talent is the module's attribute sigma, a carried wound is a level (`U5b_PC_rulings_in_the_fight.md` §2–§3). The yield is a draw for every party (`16_PESSIMIST_PC_A_the_yield_is_a_draw.md`), so §5's last bullet is answered.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.1 (PB stream row VIOLATES A-30: §1, §2 and step 2 rewritten to the per-round key; `approach_of` AMBIGUOUS: takes a `PersonInterior`, and the decider closure captures a frozen snapshot, not a `Person`; `CombatTurnView` field list stated closed, Option B (REM-31 precedent, CONVENTION) taken; `approach_responses` loader refusal added), §2 row A-30, 7b-2 (key, tests, lands-it), 7b-3 / `U1_OWNERS_AND_VOCABULARY.md` D-U1-08 (`faculties` replaced by `scores` + `addends`; the U5b line above that calls `faculties` "the trained score" is superseded by D-U1-08), D-U1-11b (`NESTING-CAP` → the typed `Refusal(depth_cap)`; `nested_entry` kept as U1 §2 names it, so 7b-12's Option A is not applied), §6.1 (a) and `U3_CONFLICT_LEDGER.md` C3-N4 (§3's readings captioned as half-score history), test 9 (the scratch probe `pI_approach2.py` becomes a written workbench file; `Depends on:` / `Lands in batch:` from `U3_DEPENDENCY_ORDER.md`). §8's conflicts and the author's measurements are kept. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "typed record" → "dataclass" (glossary *record*).

**Depends on:** `11_GO_one_draw_owner.md` (B06: the key function); `U5a_CORE_owed_edits.md` §E row 1 (B03: the frozen `PersonInterior`); `02_CHAR_choice_alignment.md` (B10: the `choices: approach:` cells); `U5b_PC_rulings_in_the_fight.md` §2–§5, `16_PESSIMIST_PC_A_the_yield_is_a_draw.md`, `16_PESSIMIST_PC_B_the_commit_window.md`, `18_DETERMINISM_no_certain_matchup.md` (B15: calibration before steps 3a–3e; U3 §4.1 rows 56–58 reverse those edges). Step 5 depends on `U5b_PC_rulings_in_the_fight.md` §1 (`nested_entry`, B30).
**Lands in batch:** steps 1–4 in B16 (`B16-pc-round`, PC); step 5 in B30 (`B30` MB nested, after UPR §1).

## Status: PROPOSED

Lane: PC, with CORE (the suspension, the adapter row), MB (the cell field at weight 1, a duel inside a
field) and CHAR (the alignment cells, temperament). Supersedes
`03_PC_duel_round_and_approach.md` (the first PC lane's proposal 5) **where the two differ**; §1 lists
what stands and what changes. Source: Jordan's intent of 2026-11-12 (`AUDIT_BRIEF.md`, "Design intent …
personal combat"), his sentence of 2026-09-30 quoted at
`proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11`, and
`audits/03_PC_audit_addendum_B.md` (F-PC-16 to F-PC-19, §B3 to §B6). Read at `2c24c81`. Reference only
(CLAUDE.md §0.05); not ratified by being written. §8 names the conflicts with ruled, ratified or
recorded items and resolves none of them.

## What it changes in `engine/season/` at runtime

In build order: steps 1 and 3 change nothing (equality controls; every approach `normal`); step 2
re-seeds each fight per round, one declared mover of every season fight; step 3e changes nothing in a
season (every person fights at disposition 4, lean 0) and moves the workbench's disposition table;
step 4 adds callers and changes nothing while no alignment cell and no response row is authored; step 5
adds a caller in the field's adapter.

## 1. What stands from the first proposal, and what this one changes

**Stands, unchanged:** the round is the unit and `wrapper.engagement` is that unit; `fight` becomes a
loop over it; the three dataclasses; the second composition row; per-round draws that do not depend on
the fight's earlier draws (now a per-round **key**, A-30, §2); one
decider per party with the played person's and the NPC's supplied through one parameter; `decide=None`
is today's fight; the falsifiers of its §8.

| # | the first proposal | this proposal | why (evidence in the addendum) |
|---|---|---|---|
| 1 | a "phase" is one whole round; the decider is asked once per round | a phase is one of the engagement's own three phases (`measure`, `exchange`, `bind`); the decider is consulted when a phase is entered; a grid attack gives one answer for the whole round | the design set gives "phase" a referent (the state graph's player-facing moments, the phase-slots) and Jordan's two sentences ask for a choice "each phase" in the duel and one choice per attack on the grid (§B3) |
| 2 | the approach is a lean added to `disp_lean`, moving all three disposition hooks; the three existing costs are swept until no approach dominates | the approach has its own coefficients and moves commit depth, counter selection and the bind-or-break inclination; it **never** moves the initiative drift; an optional conserved transfer between a fighter's own attack and defence supplies intensity | the whole monotone advantage of aggression is the drift hook: with `DISP_INIT_K` at 0 aggressive reads 52.4 and defensive 47.5 against a mirror control of 50.3 (n 2,000; F-PC-17) |
| 3 | `DuelState` is held by the host or the adapter between calls; four fields | `DuelState` lives in the frame of whichever loop calls `round`, inside one provider call; five fields (the weapon form is carried) | Layer 1 §44.3: a wrapper holds no state; the field is one provider call (`seam/wrappers/mass_battle.py:446`), so its adapter cannot hold anything between field turns; the half-sword form crosses engagements and moves the next opening (F-PC-16, F-PC-19) |
| 4 | the NPC's policy is "one function in `decision/`", `normal` until CHAR supplies temperament | the function is specified: `choose.approach_of`, built on `score_terms`' pursuit dot over CHAR's alignment cells for the `approach` values, sampled by `_sample_order`'s rule at the person's own temper; no fan at DELIBERATE | §5; `decision/choose.py` and `options.py` read in full |
| 5 | step 4's gate is a fidelity reading in expectation | the gate is exact: equal plans give the identical outcome and hash whoever supplied them | Layer 1 `03_VERBS_AND_LOOPS.md` §C.4: "They agree exactly, because they are the same slice" |
| 6 | five conflicts named | two dissolve (the grid reading; the quarantined zones text), three stand, two are new (§8) | §B2 corrections C-4, C-5 |

## 2. The round (structure)

```python
# engine/season/queries/inputs.py
@dataclass(frozen=True)
class DuelState:                 # what one party carries from round to round. It lives in the FRAME of the loop
                                 # that calls `round` (the duel's `fight`, a skirmish's or a field's own loop),
                                 # for one provider call. No adapter, module attribute or World field holds it.
    cumulative_damage: int = 0
    stamina: Optional[float] = None      # None: start of a fight (the module derives the maximum)
    conc: Optional[float] = None
    poise: float = 1.0
    form: Optional[str] = None           # the weapon record in hand when the last round ended. None: the kit's
                                         # own record. (W3-1, 7b-4:) after `03_PC_weapon_form_at_round_start.md`
                                         # (B14, before this file) the half-sword grip no longer crosses a round,
                                         # so `form` carries the selected weapon (primary or secondary) for the
                                         # switch of `03_PC_loadout_and_carry.md` item 5

@dataclass(frozen=True)
class DuelRoundInput:
    fighters: PersonalCombatInput        # who they are: ends, attributes, kits, terms, and the roll's numbers raw:
                                         # `scores`, `addends`, `pool_add`, `pool_floor`, `opposition_rate`
                                         # (D-U1-08; carried once, here, not repeated on the round input)
    states: tuple                        # (DuelState, DuelState), in claimant order
    plans: tuple                         # per party: {phase: approach}; a missing phase is `normal`
    round: int                           # 1-based
    prev_closed: bool = False            # the measure the last round ended in

@dataclass(frozen=True)
class DuelRoundOutcome:
    states: tuple
    wounds: Mapping                      # id -> the lifted wound quantities, as the fight returns them
    felled: Optional[str]
    yielded: Optional[str]
    closed: bool
    trace: tuple                         # this round's events, each `approach` consult among them
```

- `modules/combat/fight.py` gains `round(inp: DuelRoundInput, rng, deciders=None) -> DuelRoundOutcome`:
  build the two Combatants; apply each `DuelState` (damage, stamina, concentration, poise, form);
  draw `first` (the coin `wrapper.fight` draws at `wrapper.py:593`, moved inside the round so the
  round's stream is complete); call `wrapper.engagement` once; apply the between-round recovery
  (`wrapper.py:613-615`); lift the states. It keeps nothing.
- `fight(inp, rng, deciders)` is the loop over `round` with the states in its own frame. Round `r`
  draws from the key `H(fight_key, 'round', r)`; each draw inside the round is keyed `(r, phase, purpose)`;
  no draw depends on another round's count (A-30). The function that makes a key into a draw is
  `11_GO_one_draw_owner.md`'s `Draw.u`. Round `r` is recomputable from `(fight_key, r)`.
- The carried set is exactly what a probe finds differing at a later `turn_start`
  (`probe_round_state.txt`): damage, stamina, concentration, poise and the weapon form. Initiative,
  grip, lunge, facing, swing room and the selected mode are reset or re-derived inside the round
  (`wrapper.py:89-90`, `:127`, `:161-172`).

## 3. The approach (the choice surface)

**Vocabulary, owned by `modules/combat/vocabulary.py`** beside `DEFENCE_MODES`:

```python
APPROACHES = ('defensive', 'normal', 'aggressive')    # the lean is the position minus one: -1, 0, +1
PHASES     = ('measure', 'exchange', 'bind')          # the engagement's three phases a fighter can lean in
```

`measure` is the open-measure phase (the state graph's `Approach` node; the word "approach" is left to
Jordan's dial so one word does not name two things). `exchange` is the closed, tempo-gated exchange.
`bind` is the hold-or-break decision of a closed beat. Each is a state the engine already resolves
through and `state_graph.py::INJECTION_POINTS` already names; no state is added.

**What a lean does, phase by phase.** An approach is a prior on a gate the engine already rolls; it
selects no outcome and adds no branch (the held Plan-layer rule; ED-PC-0023). A `normal` lean draws
nothing and reorders nothing.

| phase | gate leaned | form | cost side | built? |
|---|---|---|---|---|
| `exchange` | commit depth | `g += COMMIT_BETA_K · APPROACH_COMMIT_K · lean` inside `combat_systems.commit_depth` (`:1122-1124`), spread floor kept | deep commit pays exposure, initiative loss, poise, tempo debt and legibility; shallow commit gives up attack σ | **yes**, both ends |
| `exchange` | counter selection | `× (1 − APPROACH_COUNTER_K · lean)` in `counter_select` (`:1162`) | a missed single-time counter eats the attack undefended (`wrapper.py:363-369`) | **yes** |
| `bind` | the fighting withdrawal | `disengage_attempt_p × (1 − APPROACH_BREAK_K · lean)` (`combat_systems.py:979`) | a read withdrawal is pursued and the pursuer takes the tempo (`wrapper.py:211-219`) | **yes** |
| `exchange` | attack against own defence | `net_sigma += APPROACH_SIGMA_K · (lean of aggressor + lean of defender)` in `assemble_net_sigma` (`:1097`) | conserved by construction: what a fighter adds to his own attacks he gives to attacks on him | **new term**, shipped at 0 |
| `measure` | closing and the stop-hit | the held proposal's I1 (`close_rate`, `stophit_p`) | pressing must raise stop-hit exposure; a missed stop-hit must cost the longer weapon | **no**: ship only when both costs exist |

`APPROACH_COMMIT_K` and `APPROACH_COUNTER_K` start at the values of `DISP_COMMIT_K` (0.8) and
`DISP_COUNTER_K` (0.5), so a lean of ±1 on those two gates is what disposition 7 and 1 give today and
the measurements below apply as taken. All are `[SIM-CALIBRATE]` and live in `CFG`.

**What was measured (all `PYTHONHASHSEED=0`; scripts and outputs in the scratchpad named in the
addendum §B11).** *(Half-score fight; superseded by `29_DICE` gates 2–5; re-read at UPR §5 row 7
(`U3_CONFLICT_LEDGER.md` C3-N4). The figures are the record of the first measurement, not the shipped
reading.)*

| reading | result |
|---|---|
| the three hooks as built, leaning fighter against a normal one, n 2,000 | aggressive 58.2%, defensive 43.1% (mirror control 50.3%); aggressive against defensive 63.5%. Strictly ordered, no cycle |
| one hook zeroed | drift (`DISP_INIT_K`) zeroed: 52.4 and 47.5. Commit zeroed: 56.0 and 42.5. Counter zeroed: 58.6 and 42.4. The drift alone live: 56.1 |
| commit and counter only, ±1, eleven named matchups, n 1,500 | every cell within about 3 points of `normal`; no lean best by more than its interval |
| commit and counter only, ±2, n 1,500 | mace mirror: aggressive 43.2, defensive 51.5. Rapier mirror: aggressive 50.9, defensive 45.9. Arming mirror: 49.4 and 46.8. The sign follows the weapon's recoverability, which is the design's own claim ("a rapier can feint and a mace can't") |
| the conserved transfer at 0.30σ, arming mirror, n 1,500 | A's share 49.6 to 52.2 in all nine cells (normal against normal reads 52.1 at the same seeds, 49.2 at disjoint seeds). Mean rounds 2.34 (both aggressive), 3.50 (sum 0), 6.16 (both defensive); undecided 0.0%, 0.4%, 7.9%; the winner's damage 44%, 35%, 33% of his Health |
| the same, named matchups, the leaning fighter against a normal one | aggressive best with a dagger against an arming sword (13.6, against 10.3 normal and 9.3 defensive) and against a low-Endurance opponent (69.7, 67.9, 64.9); normal best when the leaning fighter is himself low in Endurance (34.3, 37.0, 34.2); defensive best for a lightly armoured fighter against plate (5.5, 5.4, 6.5, with 10.0% of his fights undecided). Differences of two points or less are inside the interval at this n |

So: the lean on commit and counter is a small, weapon-conditional trade, which is what the held
proposal's acceptance band asks of an intent (aggregate within 2 points, texture above the floor); the
conserved transfer is what makes intensity change the things a season and a grid read (how long, how
bloody for the winner, whether it ends undecided) while leaving a mirror level by construction. The
transfer is the tabletop design's Offence and Defence pool split in the engine's unit
(`combat_reference_v1.md` §1; `videogame_mode_spec.md` §1.1 "Pool-split offence/defence: Use";
ED-PC-0007's "Full Guard + Dodge DISTILL (base offence/defence pool-split)"). Its coefficient is not
recommended here; 0.30 is a probe value.

**The case against the transfer, stated so the choice is visible.** It is a term in the σ sum that no
primitive produces. The mass-battle formation design records Jordan's principle that instructions
"modulate primitives — never add a flat number" (`proposals/pc_formation_system.md` §3.5), and
ED-PC-0023 retired a mechanism for imposing rather than emerging. The leans in the first three rows
of the table satisfy that principle (they move a draw the engine already makes); the transfer does
not, though it is conserved and decides nothing by itself. *(Reconciled, D-40, closed by the ladder:
leans now; the transfer behind a dial at zero, set after A-31's damage scale has landed. So step 3c
builds the term and ships `APPROACH_SIGMA_K = 0`; no coefficient is chosen before the calibration batch.)*
Steps 3a and 3b do not depend on it.

**The same dial exists one scale up.** The army doctrine of that design is Aggression: Cautious,
Balanced, Pressing. A person's approach, a unit's instruction and an army's doctrine are then one
three-valued lean at three scales, each acting through its own scale's primitives.

**The drift hook is retired with this change.** `DISP_INIT_K` (0.10 per beat per unit of lean,
`wrapper.py:164`, `config.py:286`) is a standing initiative bonus for aggression with no cost: the
comment beside it says "BOTH poles cost" and the engine charges only caution. It is the same shape as
`ATTACKER_BIAS`, which ED-PC-0037 deleted because first-mover advantage "now lives ONLY in the Vor,
where it is earned" (`combat_systems.py:1109`). Set it to 0. No season fight moves (every person
is at lean 0).

**Skills as levers.** The approach leans gates that a fighter's skills and learned techniques already
modulate, which is the sense of "a suite of skills that correspond to levers": `anti_overcommit` and
the balance axis lower the price of a deep commit; `counter_select` and `counter_success` raise the
return of a defensive lean; the bind skill and the leverage levers raise the return of holding the
bind (the one measured synergy in the corpus is aggression with bind skill,
`.audit/2026-07-23-combat-combinatorial-audit/findings_v1.md`). Nothing new is needed for this; the
record must carry the skills (the first lane's `03_PC_person_inputs_content.md`).

## 4. When the decider is consulted, and the modes

The decider's signature stays `(CombatTurnView) -> str`. It is consulted:

1. at the top of each round, with `phase=None`: an approach (the fighter's standing approach for the
   round) or `withdraw`;
2. inside the round, each time a phase is **entered**: when the measure is open at the round's start
   or re-opens (`wrapper.py:189`, `:208`), when it closes (`:256`, `:390`), and when a bind is entered
   (`:420`). It returns an approach for that phase.

The wrapper stores the answers as live state on the Combatant (`c.lean[phase]`, written only by the
wrapper, like `initiative`). A decider that returns the standing approach at every consult is a plan
of one value, and `plans` on the round input is that plan given in advance, so a round with no decider
needs none. Every consult emits one `approach` trace event carrying the view the decider read.

`CombatTurnView` gains `phase`, `round`, `closed`, the fighter's own leans in force and both parties'
lifted wound quantities (as now). It still carries no `Combatant` and no `World`. *(Reconciled, W3-1,
`R1_READ.md` §1.1:)* its fields are this closed list and nothing else: `phase, round, closed, own_leans,
own_wounds, foe_wounds` plus the fields it carries today; each is what a fighter can see of the fight.
Nothing checks that the list holds only perceivable fields (Layer 1 grade CONVENTION); the REM-31
precedent is followed (R1's Option B) and no scan is added (CLAUDE.md §0.1 pt 5).

| mode | the loop that calls `round` | who answers a consult | where `DuelState` lives |
|---|---|---|---|
| AUTOMATED fight | `fight`, from the season's provider | each party's decider (§5) | `fight`'s frame |
| duel, moment by moment | the same `fight`; the played person's decider is the host's call-out (REM-31), consulted at each phase; the trace of each exchange is rendered between consults | the player for his fighter, §5 for the other | `fight`'s frame |
| grid attack | the skirmish's loop (the cell field at weight 1, Layer 1 `04:811`); one `round` per attack action | the attacking unit's player or decider gives **one** approach; it is the plan for every phase | the skirmish module's loop frame |
| a duel inside a field | the field module's loop; one `round` per window per officer contact (`04_MB_manager_battle_one_resolver.md` §7). *(Reconciled, A-4:)* a nested contest at depth 1, counted against `contest_nesting_cap` (1); at the cap the callable returns the typed `Refusal(depth_cap)` (D-U1-11b; at the tree `seam/contest.py::ContestError`, `U5b_PC_rulings_in_the_fight.md` §1 edit 2) and the contact stays unresolved | each fighter's decider or standing order | the field module's loop frame |

For the last two, the module that owns the grid or the field does not name `modules/combat/`. Its host
adapter resolves the `combat.round` composition role and passes the module a `duel` callable
(`(DuelRoundInput, rng) -> DuelRoundOutcome`), as `decide` is passed today. The calling module holds
the states in its loop and hands them in and out. The first proposal's "carried on the adapter's side"
cannot be built: the field is one provider call and its adapter runs before and after it, not between
its turns.

## 5. The chooser: how an NPC picks an approach

**Where.** `engine/season/decision/choose.py`, beside `score_terms`, because the function reads the
two bare names that file owns (`deliberation_memo`, `_sample_order`); `decision/` takes no `World`
(AX-2), and this function takes none.

```python
def approach_of(p: PersonInterior, view: "CombatTurnView", fx, draw=None) -> str:   # a frozen snapshot (04 §C.3)
    """THE APPROACH `p` TAKES AT THIS CONSULT. Candidates: `normal`, and each other APPROACHES value that
    carries an authored cell or a matching response row. Score: `score_terms`' pursuit dot, with the
    alignment of the VALUE in place of the verb's (`data.verbs.align_choice('approach', value, axis)`),
    plus the response rows that match the view. One candidate (the shipped state): `normal`, no draw.
    Otherwise ordered by `_sample_order`'s rule at `choice_temperature x temper(p)`, the draw keyed
    `approach:<value>` on a stream of its own, never the fight's."""
```

- **Temperament term.** `Σ_axis axis_w[axis] · align_choice('approach', value, axis)`, with `axis_w`
  from `deliberation_memo(p, fx)`. The cells are the `choices: approach:` block that
  `02_CHAR_choice_alignment.md` adds to `tables.alignment`; the block and `align_choice` are that
  proposal's, used here unchanged. `approach` is declared in `data/verbs.py::CHOICE_RANGES` as a
  pointer to the module's `APPROACHES` (the way `retreat_at` points at the battle module's set) and is
  **not** listed under any verb in `rosters.yaml: choice_sourced`, so `_fanned_choices` forms no
  extra Candidate at DELIBERATE: the approach is chosen in the fight, each phase, by the person,
  not drawn as one of three equally scored acts (the roster's own note records the fan as a draw, and
  H-361 its cost). One amendment to that proposal follows: its loader rule "refuse a key that is not
  `choice_sourced`" must read "refuse a key outside `CHOICE_RANGES`", or the `approach` block is
  refused; it is named here for the CHAR lane and edited nowhere.
- **Situational term.** `rosters.yaml: approach_responses`, a new optional table, shipped empty:
  rows of `{phase, own: <band>, foe: <band>, value, weight}` over the wound bands the view carries
  (`Untouched`, `Wounded`). A matching row adds its weight to that value's score. It is content a
  designer authors (a fighter presses a wounded man; a wounded fighter guards); the engine ships none.
  A row is data about how persons respond, read person-side from what the person can see; no person,
  faction or outcome is named in it. The loader (`data/rosters.py`) reads the table at load even while
  it is empty (ID-13) and refuses, naming the row, a `value` outside `APPROACHES`, a `phase` outside
  `PHASES` and a band outside the view's wound bands.
- **Departure from the optimum.** `_sample_order`'s Gumbel rule at the person's own temper
  (`02_CHAR_resolve_and_temper.md`), so two persons of one temperament differ by their steadiness and
  nothing else. The noise is keyed by the value, not the round (the precedent's reason: a person's
  taste is stable while his situation moves).
- **No outcome model.** The function scores what the person is like and what he sees. It does not
  estimate the fight. If believed odds are wanted later, the only lawful source is the resolver itself
  sampled on a private stream (the `estimate` provider's shape, `seam/wrappers/combat.py:235-296`),
  as a swept arm that ships off; an analytic table of approach against approach would be a second
  formula (Layer 1 §27.2).
- **Who builds the decider.** `seam/wrappers/combat.py::resolve` builds one decider per claimant:
  `host.decide` for a claimant in `host.persons`, otherwise a closure over that claimant's frozen
  `PersonInterior` snapshot (built by its one builder before the call, `U5a_CORE_owed_edits.md` §E row 1;
  never the live `Person`, `hol` §44.3) calling `approach_of`. The module entry receives a mapping of
  callables and cannot tell them apart. A
  standing order (a squad member's, MB's) is a third supplier of the same callable, evaluated
  host-side from a dataclass on the input, as `FieldOrder` is for a side
  (`queries/inputs.py:195-201`).
- **Reason trail.** The `approach` trace event carries the view; the decider's closure adds the
  winning value's two terms (temperament, response), so a telling can say why he pressed.
- **Concession and withdrawal.** *(Reconciled: both are settled.)* Concession is not a decider's answer
  at all: whether a wounded party fights on is a draw on his own Spirit at the end of a turn in which
  he crossed a wound gate, under every term (`16_PESSIMIST_PC_A_the_yield_is_a_draw.md`; the standing
  rule answered the first audit's §11 item 1). `withdraw` stays in the top-of-round set and is priced
  for every party (`03_PC_exits_withdrawal_recovery.md` Part A); `approach_of` may return it when a
  response row authors it, and returns it never while `approach_responses` ships empty.

## 6. One resolver (Layer 1 §27.2, §44.3; `03_VERBS_AND_LOOPS.md` §C.4)

The automatic duel round is not an auto-resolve formula. It is `wrapper.engagement`, the one function
that resolves any round, called with the approach supplied by a chooser instead of by a hand. The
duel, the grid attack, the field contact and the unwatched fight differ in who supplies the plan and
in how much of the trace is shown; equal plan, state and seed give the identical outcome, which is
§C.4's "they agree exactly". Four places where a second formula could enter, and the rule for each:

| risk | rule |
|---|---|
| an approach applied by the host as a modifier on a result (a grid adding damage for "aggressive") | forbidden; the approach enters only as `plans` on the round input and is read inside `combat_systems` |
| a table of approach against approach used by the grid, the field or the chooser to skip the round | forbidden; the round always runs; an estimate is the resolver sampled |
| the adapter keeping round state or deciding for a person | forbidden by §44.3; state is in the calling loop's frame, the decision is the person's decider |
| the upset flip (`wrapper.py:622-624`), which reverses a decided fight after the fact | *(Reconciled, D-11)* leaving it on an integer the fold does not read keeps every season matchup certain, which the standing rule forbids (ladder step 1 answers §11 item 3's "whether"). Replaced by `18_DETERMINISM_no_certain_matchup.md`: at the deciding felling the blow may be turned (same `UPSET_FLOOR`, same draw position) through the one damage site, so the trackers — and a round, which carries them — see it |

Where this cannot be made to fit, it is named in §8 (items 4 and 5).

## 7. Build order and gates

| step | change | gate (execution artifact) |
|---|---|---|
| 1 | `fight.round`; `fight` as a loop over it on the one stream; `DuelState` with `form`; `first` drawn inside the round | every combat test and season hash unchanged; twelve `round` calls by hand equal `fight` at three seeds, including a longsword against plate (the case in which the form is carried) |
| 2 | the per-round key `H(fight_key, 'round', r)` (A-30) | a fight in one call and the same fight as separate `round` calls from `(fight_key, r)` are identical; season pins re-recorded once, declared |
| — | *(Reconciled, A-31, pessimist R-6.)* Steps 3a to 3e land **after** the combat calibration batch (`U5b_PC_rulings_in_the_fight.md` §5 row 5: the damage scale, then `16_PESSIMIST_PC_B_the_commit_window.md`), because every reading in §3 was taken on a three-blow fight with an unreachable deep tier. Step 3 as a whole gains one gate: a state-reading policy (press the wounded; guard when hurt) beats never-lean by more than the interval in some named matchup, or the menu is not shipped. *(W3-1, test 9:)* the pessimist's scratch `pI_approach2.py` is not in the tree, so this step first writes it as `systems/combat/combat_engine_v1/workbench/approach_policy_probe.py` (beside `build_levers.py`) | the probe's printed table: per named matchup, the state-reading policy's win share, never-lean's, and the disjoint-seed interval at n ≥ 2,000; expected reading: at least one matchup where the difference exceeds the interval (else the menu is not shipped) |
| 3a | `APPROACHES`, `PHASES`, the lean as live state, the consult points; the `exchange` lean on commit and counter | all-`normal` byte-identical to step 2; `build_levers.py`-style table at n ≥ 2,000: each approach within 3 points of `normal` in the arming mirror; the mace and rapier mirrors show opposite signs |
| 3b | the `bind` lean on `disengage_attempt_p` | all-`normal` byte-identical; `disengage` events per fight rise under `defensive` and fall under `aggressive` for a spear against an arming sword |
| 3c | the conserved transfer, `APPROACH_SIGMA_K` *(ships at 0, D-40)* | at 0, byte-identical; at the chosen value the nine-cell arming mirror is level within the control band, mean rounds are monotone in the summed lean, and the undecided share is reported |
| 3d | the `measure` lean | only together with both of its costs; not specified here |
| 3e | `DISP_INIT_K = 0` | `build_levers.py disposition 2000`: disposition 7 and 1 inside 50 ± 3 against neutral (they read 57.7 and 40.8 today); season hash EQUAL |
| 4 | per-party deciders, the widened view, `choose.approach_of`, the `CHOICE_RANGES` pointer, the empty `approach_responses` table | equal plans supplied by a constant, by a host callback and by `approach_of` give identical outcomes and one `World.content_hash()` (REM-31's test, extended); a differing script moves it; with one cell authored, two hand-built persons opposed on that axis answer differently at temperature 0; with none authored `build_realm(0)` is hash EQUAL |
| 5 | the `duel` callable built by the field's (or skirmish's) adapter through `nested_entry` and handed to the module *(Reconciled, A-4: nested, cap 1; lands in B30)* | a seeded field with two planted officers in contact shows one round per window in the trace; with no contact reported the field's hash is unchanged; with the cap at 0 the contact is reported unresolved with `Refusal(depth_cap)` and the field's draw count is unchanged |

**Implementation (test 9; `R1_READ.md` 7b-2, checked against the tree).**

- *Tests* (existing files): `engine/season/tests/test_rem31_grid_suspension.py::test_twelve_round_calls_equal_one_fight`
  and `::test_a_fight_in_one_call_equals_the_same_fight_as_separate_round_calls_from_the_key` (steps 1–2);
  `engine/season/tests/test_combat_module.py::test_round_keeps_no_state_between_calls` and
  `::test_all_normal_plans_draw_the_same_count_as_today` (steps 1, 3a); step 4's equality test extends REM-31's
  in `test_rem31_grid_suspension.py`; `approach_responses`' refusals in the roster loader's test beside the other
  `rosters.yaml` refusals. Steps 3a/3b/3e read `systems/combat/combat_engine_v1/workbench/build_levers.py`'s
  tables (in the tree; the artifact).
- *Falsifier and control:* §9; the control for every step is the all-`normal` byte-identity.
- *Hash movers:* step 2 (every season fight, once, declared); step 3e (the workbench disposition table only);
  steps 1, 3a–3d, 4 hash EQUAL with nothing authored; step 5 with no contact reported EQUAL.
- *Lands:* an IN-lane implementation session under `/methodology-execute` with PC review; steps 1–2 `sonnet`;
  step 3 `sonnet` with the workbench sweep run by `haiku` (`valoria-measure`) and read by `opus` (a calibration
  judgment); step 4 `sonnet`; step 5 `sonnet` in B30.

## 8. Conflicts with ruled, ratified or recorded items (named, not resolved)

*(Reconciled 2026-11-12. Item 1: the reopen condition is met by Jordan's own intent; D-40 sets the order.
Item 2: A-4 keeps round state in the calling frame and A-8 makes a carried wound a level, so the held
seeded-damage step is not decided by this build. Item 3: A-9 admits the in-round consult; one sentence
is owed to the ratified suspension (CORE's). Items 4 and 5: answered by A-4, as one declared class of
adapter input and a nested contest under a cap of 1; the Layer 1 text is drafted, not applied, in
`U5b_PC_rulings_in_the_fight.md` §1. Item 6 stays CHAR's open ask. Item 7: a battle stays one act
(A-4); the unwatched duel is as recorded. The author's text follows unchanged.)*

1. **ED-PC-0007** (deferred; reopen "only if `combat_engine_v1` grows a discrete player-action
   menu"). Three approaches over three phases are such a menu. Stands as the first proposal named it.
2. **CR-85 §4 step 2** (held; ED-IN-0351). `DuelState` carries damage into a call. Stands.
3. **The ratified suspension** (`proposals/2026-10-07-grid-mode-suspension.md`, REM-31): one
   suspension per provider call, a decider that draws nothing and mutates nothing, asked per turn.
   With round state frame-local a grid skirmish is one provider call and fits it. What is new is the
   **in-round consult**: the same decider under the same contract, called at phase entries inside
   `engagement`. The ratified text does not cover a call-out inside a round.
4. **Layer 1 `04` §A.2, the adapter row.** `host` is already a declared departure from "the
   projection" (`seam/wrappers/combat.py:331-332`, B4 third disposition). A decider for every
   claimant and a `duel` callable handed to another module are two more inputs of that kind. Either
   the row is read to admit person-supplied callables as a class, or each is a departure to be
   declared. Layer 1 is not edited here.
5. **Layer 1 §43/§45 and one module calling another's resolver.** A field or skirmish module that
   invokes a callable which runs `combat.round` is nested resolution through a parameter. §39.3
   (`holonic_ARCHITECTURE.md:1397-1402`) gives nested contests a depth cap with no default and warns
   that "a nested instance is an instance" is not a bound. Whether the
   `duel` callable counts as a nested contest under that cap is the Layer-1 owner's reading.
6. **ED-IN-0304** (risk appetite and horizon, ruled, no carrier; open ask M40). It is the natural
   source of the temperament the alignment cells express; this proposal reads pursuits and names no
   new carrier.
7. **J-15** (whether an unwatched fight is one act or spans scenes). Unchanged.

Dissolved since the first proposal: its conflict 2 (R-04's grid reading) and conflict 5 (the
quarantined zones text) are answered by Layer 1's own row "grid squad combat: the same thing one scale
down, every combatant a `Person`" (`architecture/meta/04_CODE_ARCHITECTURE.md:811`).

## 9. Falsifier

A grid attack whose outcome differs from the same round inside a duel at the same plan, state and
seed; an approach best in every matchup of the step-3 table; an all-`normal` fight that draws one
more or one fewer random number than today's; an NPC's approach chosen by a rule inside
`modules/combat/` or the adapter; `DuelState` found on an adapter attribute, a module global or a
`World` field; a fight resumed from a `DuelState` without its `form` that equals the uninterrupted
fight for a half-swording weapon (it should not: that is step 1's control).

## 10. NERS reading

- N: from above, the stated intent's central choice has no carrier, and the one axis that resembles
  it has a single right answer; from the player's side, a duel in which nothing is chosen between
  exchanges is a film; from below, the engine already resolves through the three phases and already
  owns the cost side of two of them; laterally, a grid, a field and an unwatched fight need the same
  call. Narrowed in one direction: the `measure` lean has no cost machinery and is withheld.
- R: strategy (a lean that pays against one weapon and costs against another; intensity that trades
  the winner's blood against time and against the chance of no decision); customization (skills and
  temperament decide what a lean is worth to this fighter); the no-player half (two NPCs of different
  temperament fight differently and the trace says why); completeness (every lean has both ends or is
  not shipped).
- S: one round at every scale; the scales pause at a consult; one decider interface; one table for
  temperament (CHAR's); the approach uses the engine's σ and gate methods and no second aggression
  axis remains once the drift is retired.
- E, last, against what N and R found: two closed sets, three records, one entry, one `decision/`
  function, four coefficients and one retired; no new state, no new resolver. High, on the condition
  that step 3's tables are run before any coefficient ships.

## 11. Cost class

Steps 1, 2, 3a, 3b, 3e, 4: small builds. Step 3c: small build plus a calibration pass on the
workbench and a ruling on its coefficient. Step 3d: design-first. Step 5: small build here,
design-first in MB for what a contact is and what its result does to a unit.
