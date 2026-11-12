# U5c · SC — one obstacle form: one roster, one composer, and a leverage channel for what a party brings

Folded: 2026-11-12, lane 29 (`audits/29_ONE_OPPOSED_RULE.md`; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md` edit 4), on Jordan's A-71 — §2's form gains one leading term and fixes one operand; the roster, the composer, the record and the order stand. `hard = even + difficulty + opposed_ob(score, opposition_rate) + Σ raw_i × step_i`, where `even = MU_PER_DIE × pool_add` (derived in the module from two carried fields; roster member `even`, first, with no host reader) and `opposed_ob` reads the **trained score** of the person opposite, or the ordinary score (`pool_default`) where nobody is. This is the same number as "0.4 × the opponent's pool" in the conformance table above; it is written this way because the fight reads the same `opposed_ob` at the same rate and has no even line. The floor `max(OB_MIN, …)` no longer binds on any social roll (the even line is above it) and is left as written.

## Status: PROPOSED (a reconciliation written by the U5c closure lane; a plan for a later implementation lane, executed by nobody here; not ratified by being written, `CLAUDE.md` §2)

Carries: `unified/U5_CONFLICTS_U5c.md` C-01 to C-06, C-21, C-23 (the obstacle half); findings F-SC-03,
F-SC-16, F-PES-SC-04, 13 §4 cells 2 to 6; resolutions G-41, G-57 to G-64, G-68, 13 R-1 to R-6, PES-SC res. 1
and 3. It replaces nothing as a file. It states the one form that eight proposals each state part of, and
each of those carries a `Reconciled:` line pointing here: `05_SC_obstacle_difficulty_and_modifiers_B.md`
(SC-B), `13_SC_tuning_tables.md` (T13), `13_SC_calibration.md` (CAL), `10_DICE_one_score_two_roles.md`,
`16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage.md` (PES-A), `05_SC_contest_record_on_event.md`
(SC-P1), `05_SC_evidence_and_rebuttal_B.md` (EVID), and the verb proposals that add terms. Cross-family
files it depends on and does not edit: `16_PESSIMIST_DICE_task_difficulty_and_throughput.md` (PES-DICE),
`10_DICE_capability_axiom_map.md` (the DICE map).

## Conformed to Jordan's answers (`unified/DECISIONS_ANSWERED.md`, 2026-11-12)

The answers landed while this was being written. The form below needs none of them changed; the numbers do.

| answer | what it does here |
|---|---|
| A-25 (favourable circumstances raise the speaker; hostile ones raise the obstacle) | confirms the split this file is built on (§2, §3) |
| A-26 (an equal opponent costs 0.4 per point) | the opposition term's rate. `opposed_ob` stays the one owner (§1); its value changes from half the score to 0.4 per point, and `05_SC_opposed_obstacle_parity.md` is the carrier. Steps 0 to 4 of §4 land at the rate in force today (half the score), which is what keeps them hash-equal: the "1.0" and "2.0" written below are that rate's figures. The rate changes once, at step 5, as a declared mover (the stand-in becomes `0.4 × pool_default`) |
| A-5 (the bell curve everywhere), A-6 (score plus a base, floor five), A-7 (two inputs) | the sampler and the pool rule under the form. The pool and the opposing score are read through `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §4 as U5a rewrote it; this file names no formula for either. Every probability quoted below (§4 step 5, §6, the gate's exact-odds rows) is whole-dice arithmetic and is recomputed against the re-centred sampler in the one calibration step (§4 step 5), together with A-26's rate |
| A-12 (a seat carries a modifier) | `rank_gap` (§2 member 6) is the half that stands against an act; the half that helps is declared once, as the source `office` (§3), whose first member is T13 T4's bench die. It does not double-count with `regard`: `regard` reads stance rows only, never rank or heritage (§2 member 7). The Layer 1 amendment text for `04` §B.7 is owed by the unification stage and is not applied here |
| A-14 (a vote is a draw on the voter) | the `lean` source (§3) |

What does not move: the roster, the composer, the record, the landing order, the falsifier. Steps 0 to 4 of
§4 are sampler-independent (each is hash-equal or a declared mover by construction). Step 5 is the
calibration, and it is now one joint step over A-5, A-6, A-7 and A-26, read against CAL's criteria, which
are stated on outcomes and stand.

## What it changes in `engine/season/` at runtime

Every rolled act composes its obstacle in one function from one closed roster of terms, each of which
stands against the act; everything a party brings (effort, cited items, a well-disposed hearer or bench, a
trait) reaches the roll as named levels on the existing leverage channel. At the control arm the composed
obstacle is today's 2.0 for every act whose counterparty holds no score. Declared movers are listed in §4.

## The problem, with evidence

1. **Three lanes compose one obstacle three ways.** SC-B subtracts favourable terms after the ceiling.
   PES-A makes them named levels. T13 and the verb proposals add terms of either sign. The module today
   subtracts and clamps (`modules/social_contest/roll.py:142-143`).
2. **The subtracting form is the one the tree retired for this engine.** `ED-884` (resolved): advantage as
   an obstacle reduction violated the Ob floor and was reformulated as a shift of the expected net.
   `ED-934` (approved by Jordan) re-ratified it for combat. `ED-1037` (resolved) fixed the same defect in
   the contest engine itself: *"applied sigma-leverage as a clamped Ob-reduction (effective_ob floored at
   OB_MIN=1), reintroducing 1/sqrt(N) impact non-uniformity"*. `rosters.yaml: advantage_sources`' source
   line: advantage reaches a roll *"only as named levels … never a flat bonus on the net and never an Ob
   reduction"*. Measured cost of the subtracting form (PES-A, exact): four firsthand proofs before a
   hostile bench leave P(Failure) at 0.90; two slots of effort take it to 0.69.
3. **Two rosters named `obstacle_terms`** (SC-B's ten members; the DICE map's `[capability]`), and
   fourteen more members proposed by the verb lanes, six of them in private per-verb tables
   (`tell_obstacle`, `interview_obstacle`, `construe_obstacle`, `oblige_obstacle`, `tie_obstacle`,
   `interrogate_obstacle`, `proof_obstacle_step`).
4. **Three sets of row values.** SC-B: `speak`, `research`, `examine`, `surveil` `demanding`. PES-DICE:
   `routine` plus a stand-in. T13: `interrogate` and the inquiries `demanding`, `speak` `routine`. Only one
   reproduces today's obstacle at the control arm once the opposition term is never absent.
5. **Two readers for the hearer's disposition.** SC-B reads `person_q.stance_toward`; T13 reads
   `person_q.regard(counterparty, actor, fx)`, whose judged, told and heritage halves read the
   counterparty's own ledger (`queries/person_q.py:424-453`, `:468-482`). The fold may read the actor's
   own ledger and no other (`04` §B.2, the F8 carve-out).

## The resolution, decided

**What stands against the act is the obstacle. What a party brings is leverage.** Ladder: step 1 for the
split (`ED-884`, `ED-934`, `ED-1037`; the roster's own law), with Jordan's sentence of 2026-11-12 (*the
obstacle is the task's difficulty plus all modifiers*) read as every modifier that stands against the act,
which is how `AUDIT_BRIEF.md` lists `leverage` beside the obstacle; step 3 for the stand-in (PES-DICE (a),
on the ruled *"score/2 plus whatever specific modifiers"*); step 3 for the reader (`04` §B.2); step 5 for
the roster's shape.

### §1 The owners

| fact | single owner |
|---|---|
| the composition | `modules/social_contest/roll.py::obstacle(inp) -> (ob, terms)` (`ED-SC-0033` cl. 3) |
| the closed, ordered set of terms | `engine/season/rosters.yaml: obstacle_terms` |
| which host function reads each term | `engine/season/seam/wrappers/sigma.py::OBSTACLE_TERMS` (member → one function; refused at import for a member with no function or a function with no member, as `ADVANTAGE_SOURCES` is) |
| each term's size | one fixture per term in `engine/season/data/fixtures.py`, control 0, with a NUMBER row in `hole_register.yaml` |
| the ruled divisor | `engine/dice_engine/sigma_leverage.py::opposed_ob` (DICE map §G edit 5), shared with combat |
| the score a person rolls and opposes with | `engine/season/seam/wrappers/pool.py::score` (`10_DICE_one_score_two_roles.md` edit A) |
| the set of leverage sources | `rosters.yaml: advantage_sources` and `sigma.py::ADVANTAGE_SOURCES` (existing) |

The typed record carries the terms as one field, not one field per term:
`SocialContestInput.obstacle_operands: tuple[tuple[str, float, float], ...]` — `(name, raw operand, step)`
in roster order, built by `sigma.py::obstacle_operands(w, act, row)` through `OBSTACLE_TERMS`. `difficulty`
and `opposition` keep named fields (`difficulty: float`, `opposition: Optional[float]`, `pool_default: int`)
because they are not step products. This replaces SC-B edit 4's field list and the DICE map's
`.obstacle_terms` float; a verb proposal that adds a term adds a roster member, one host function and one
fixture, and never a field.

### §2 The form

```
hard   = difficulty + opposed_ob(opposition if a person opposes else pool_default) + Σ raw_i × step_i
ob     = max(OB_MIN, min(hard, cap(pool)))            # the existing ceiling rule (H-213), then the floor
terms  = ((name, value), …) in roster order, + ("ceiling", −clip) and ("floor", +lift) where a bound acted
```

Every `raw_i × step_i` is non-negative; the module raises `ValueError` on a negative term (nothing lowers
the obstacle). The values in `terms` sum exactly to `ob`.

- **`opposition` is never absent** (PES-DICE (a)). A person counterparty opposes with `score()` of the
  capability the verb's capability row names as `opposed_by`, else the same capability. Where no person
  stands opposite (a `DocketItem`, a Record, a site, a task), where the capability row's `opposed_by` is the
  explicit `none`, and for a self-plea, the term is `opposed_ob(pool_default)` (1.0 at the shipped
  fixture). `copying.opposed_by: none` is one cell on the capability surface: a hearer's skill at
  reproduction is not resistance to being told (PES-SC res. 3). No verb is named in code.
- **`obstacle_default` is deleted** with its fixture and H-127's row. `10_DICE_one_score_two_roles.md`'s
  `opposition_fallback` fixture is not added: its `stand_in` arm is this form's control (§4, commit 1a),
  and its sentence *"a non-person subject … is opposed at `obstacle_default`, as today"* is superseded.
- **The roster, in order.** Each member is listed once, with the proposal that first states it. A member
  lands with its reader, in that proposal's own commit.

| # | member | what stands against the act | read from (single owner) | applies to | first stated |
|---|---|---|---|---|---|
| 1 | `difficulty` | the act itself | the verb row's `difficulty:` level → fixture table `difficulty_ob` | every rolled act | SC-B; T13 T1 |
| 2 | `opposition` | the one acted against, or the ordinary score | `pool.py::score`, `opposed_ob` | every rolled act | SC-B; DICE; PES-DICE |
| 3 | `standard` | what the room demands | the docketed arrangement row's `standard:` level | acts an audience hears on a docketed matter | SC-B; T13 T2 |
| 4 | `subject` | what the thing examined puts in the way | `Record.forgery_quality`; a cover's `quality` | inquiries | SC-B; S1-C §3 |
| 5 | `stakes` | the weight of what the act would take or impose | fixture table `stakes_ob` by Tenure kind or share | acts that restrain or take | SC-B; M-B §4 |
| 6 | `rank_gap` | how far the person acted on or for stands above the actor's exercised seat | the gate's rank reader over `rung_kinds`; `rank_step` | governance and person-to-person acts across rank | VB-C (as `standing`); S1-D; S2-B |
| 7 | `regard` | the counterparty's hostility to the actor | `person_q.stance_toward(counterparty, actor)`, clamped at `STANCE_MAX`, hostile half; `regard_step` | one person counterparty, no audience | SC-B; T13 T3 |
| 8 | `reception` | the audience's hostility | `world_q.reception` as plan SC-02 re-sources it, over the audience the prize row names (`heard_by`), hostile half; `reception_gain` | audience-heard acts; never with `regard` | SC-B; VB-A, -C, -E |
| 9 | `capability` | a circumstance that punishes a want | the `circumstance` rows of the capability uses table, summed | per row `when:` | DICE map |
| 10 | `plea` | an inapt speech's price | CR-62's `plea_step` | `speak` | SC-B |
| 11 | `first_heard` | answering an item entered at Overwhelming | the case-file stage's `first` mark; `first_heard_ob` | an answering `speak` or move | ADM |
| 12 | `commitment` | the hearer's live commit to the contrary | his `commit` Tenures × `degree_weight`; `commitment_ob` | `argue` | S1-C §1 |
| 13 | `dissent` | hearers the actor believes hold the contrary | the actor's own ledger; `dissent_step` | `utter`, `tell` | S2-B §1; S2-C §4 |
| 14 | `violated` | the terms' lean against the actor's own pursuits | his pursuits and the terms; `violated_step` | `comply`, `commit` | S1-B §2; S1-D §4 |
| 15 | `cross_pressure` | the actor's own live commits to the contrary | his Tenures; `cross_pressure_step` | `commit` | S1-D §4 |
| 16 | `grievance` | the size of what he holds against the referent | `person_q.deeds_judged` over the actor's own ledger; `grievance_step` | `forgive` | S1-D §2 |
| 17 | `scar` | his scar shift against the referent | `02_CHAR_scar_is_a_wound.md`'s owner | `forgive` | S1-D §2 |
| 18 | `divergence` | how far the maker believes the terms lean against the counterparty | the maker's own claims; `divergence_step` | `covenant` | S1-B §3 |
| 19 | `unwelcome` | the document's terms against the receiver's pursuits | the receiver's pursuits and the Record; `unwelcome_step` | `give` | S1-B §1 |
| 20 | `distance` | how far apart two rungs are | the count of `contain` edges on the ladder path; `distance_step` | `comply`, `transfer` | S1-B §2; M-B §2 (as `carriage`) |
| 21 | `purview` | the issuing seat's reach over the actor's place | `state/gate.py::purview_reaches` | `evade / defy` | S1-B §2 |
| 22 | `watch` | who is there to see or stop it | the presence cache at the act's place less the actor, or the sworn weight there where the row says `guard`; `watch_step` | `conceal`, `evade / defy`, `sabotage`, `destroy_record`, `seize` of a Rung | M-A; M-D; S1-B (as `witnesses`); S1-C (as `notoriety`) |
| 23 | `backlog` | matters already on that docket | the docket; `backlog_step` | `carry` | S1-D §1 |
| 24 | `clarity` | terms that leave little room to bend | the terms Proposition has a predicate and a value | `construe` | S2-B §2 |
| 25 | `deference` | the actor holds the issuer above him | the actor's own stance rows toward the issuer | `construe` | S2-B §2 |
| 26 | `establishment` | a full household | `world_q.establishment_of` size; `establishment_step` | `oblige` | S2-B §4 |
| 27 | `ruin` | band floors above the fabric's condition | `band_floors` | `restore` | M-A §3 |
| 28 | `wound` | body band floors above the patient's body | `band_floors.body` | `tend` | M-A §6 |

  Refused as members, each for a reason: `evidence` (it is leverage, §3); `standing` (the word already
  names a prize, a Sensation field, T13's `standing_dice` and two content keys; the quantity is
  `rank_gap`); `contradiction` and `notoriety` as S1-C wrote them (each reads another person's ledger at
  RESOLVE, `04` §B.2; the first is done at WITNESS by `16_PESSIMIST_SC_E` edit 1, the second is `watch`);
  `carriage`, `witnesses` (second names for `distance`, `watch`); every per-verb obstacle table (their keys
  are members above). Two members proposed by the institutions lanes, `obligation` and `remove`
  (`15_INSTITUTIONS_VENICE_A`, `15_INSTITUTIONS_COLONIAL_B`), are that family's to place; `remove` reads as
  the same quantity as `distance` and should be one member.

### §3 Leverage: everything a party brings

`rosters.yaml: advantage_sources`, in order: `effort` (existing), `capability` (the DICE map's `edge` rows,
which absorb `05_SC_capability_surface.md`'s `trait_advantages` once the capability surface names their
home), `proofs`, `favour`, `approach`, `custody`, `office`, `lean`. Each source returns two lists of `LEVEL_SIGMA` names,
the actor's and the other side's; `levels_to_net_sigma(aggressor, defender)` nets them; `net_boost` applies
the soft cap. Bounded, monotone and uniform at every pool.

| source | aggressor levels | defender levels | fixture |
|---|---|---|---|
| `proofs` | one `proof_level` per whole unit of weight standing for the actor's side (EVID's `standing`; before EVID lands, `world_q.proofs`); for `reconstruct`, per independent origin beyond the first | the same for the other side's standing items | `proof_level` (first value `minor`; control `None`). `proof_step` is deleted |
| `favour` | one `favour_level` per whole unit of: the audience's favourable `reception × reception_gain`; the counterparty's favourable stance (`clamp(stance_toward / STANCE_MAX) × regard_step`); a live `tie` of the actor to the counterparty; a favourable plea | — | `favour_level` (first value `major`; control `None`) |
| `approach` | `press` on `interview` or `interrogate`: one `press_level` for the questioner in the engagement draw | one against the questioned person's answering `lie` | `press_level` (first value `minor`; control `None`) |
| `custody` | one level per season the prisoner has been held, capped by the soft cap | — | `custody_level` |
| `office` | the seat the actor exercises carries a modifier (Jordan, A-12): one `office_level` where the row's audience is a bench or body he sits on or presides over | the same for a seated counterparty acting through his seat | T13 T4's `standing_dice` is this source's first and only member and stands (A-12). T13 states it as a die; the calibration step (§4 step 5) restates it once in the unit the re-centred sampler uses (a die or an `office_level`), never both |
| `lean` | a bench member's own ballot: one `lean_level` per live public commit of his for the motion | one per commit of his against it | `lean_level` (`U5c_SC_proceedings_residue.md` §6) |

Units round half up. A source with nothing to say returns two empty lists. `believed_input` fills the
believer's own sources and leaves the other side's `None` without a claim.

### §4 Row values, arms and order

| step | lands | hash |
|---|---|---|
| 0 | `10_DICE_one_score_two_roles.md` edits A and C (`score()`; the four `verb_capability` rows, with `lie: deception` and `determine: law` once `05_SC_hearing_capabilities.md`'s rows exist); DICE map §G edit 5 (`opposed_ob`) | equal (no caller changes) |
| 1a | this form at the control arm: the roster with members 1 and 2 only; `difficulty_ob` 0 / 1 / 2 / 3; **every one of the ten rolled rows `routine`** (`tell`, `lie`, `argue`, `speak`, `determine`, `arrest`, `interrogate`, `research`, `examine`, `surveil`), so each composes 1 + 1.0 = 2.0; `obstacle_default` deleted; `Margin.terms` | moves only for an act whose counterparty holds a score in a capability the verb reads (none observed at seeds 0 and 1: the held keys are `inquiry`, which no person-subject row reads) |
| 1b | PES-A edits 1 to 5 (the favourable room as `proofs` and `favour` levels; the hostile half stays the `reception` term) | declared mover: every `speak` that rolled with `proofs > 0` or `reception > 0` (seven rolls in four seed-seasons, 13 §3.2) |
| 2 | SC-P1 as reconciled: `margin_endings` values `[pool, ob, net, margin, terms, levels, leverage]` | declared mover (every Event of a social roll gains the tuple) |
| 3 | T13 commit 1 (members 3, 5, 7 with every step at 0, every `standard` `plain`, `standing_dice` 0, admission off) | equal to step 2 |
| 4 | CAL's test file, read red against step 3 on C1 and C8 | no hash |
| 5 | T13 commit 2: `difficulty_ob` 0 / 0.5 / 1 / 1.5; `interrogate` → `demanding`; the inquiries stay `routine` (1.5 unopposed: P(Failure) 0.58 at pool 2, inside C6; `demanding` would be today's 2.0 and fail C6); row standards; `regard_step` 1.0; `standing_dice` 1; admission on | declared mover; CAL green |
| 6+ | each verb proposal's members, one commit per proposal, each with its step at control 0 first | equal at control; a declared mover when the step ships |

Lanes: SC (the module, `sigma.py`), IN and CORE (the roster, the verb column, the loader, fixtures), DICE
(`score`, `opposed_ob`), FA (arrangement `standard:` values). No step waits on Jordan.

### §5 What a roll records

`Margin` gains `terms` (§2). `sigma.resolve`'s result gains `levels: ((source, aggressor n, defender n), …)`.
SC-P1's roster carries both, so a log line reads *Ob 2.5 = difficulty 0.5 + opposition 1.5 + rank_gap 0.5;
leverage: proofs +2, favour +1, effort +1*.

### §6 Two constraints on every band map that sits on this form

- No row hangs its only effect on Overwhelming: at pool 2 it is dealt 0.00 at Ob 2 and 0.01 at Ob 1 (13 §4
  cell 7; 0 of 284 realm rolls).
- The default share of a scalar effect by band is one table under one name (C-23): `task_fraction`
  (`18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 4, as U5a reconciled it), first values
  1 / 1 / 0.5 / 0 for Overwhelming / Success / Partial / Failure, read by
  `loop/effects_shared.py::graded_amount` (M-A §2, which called it `effect_share`). A row that departs from
  it (a delivery, a price, an outlay) names its own table in its own band map, as M-B and M-C do.

### §7 Stale citations repointed

T13 and `audits/13_SC_contest_interrogation.md` cite `05_SC_evidence_and_rebuttal.md` (SC-P8) for cited
items; the live file is `05_SC_evidence_and_rebuttal_B.md`. 13's R-11 (two SC files "do not exist") is false
at HEAD.

## Gate (execution artifacts)

1. Unit, over a lattice of quarter-step operands: `terms` sum exactly to `ob`; every name is a roster
   member; a planted negative term raises; a roster member with no host function refuses at import.
2. Exact odds through the module (no draw): PES-A's table of levels reproduced row for row
   (`runs/PES_SC/n1_favour_two_ladders.py`); F-SC-16's rows (pool 2 against a score of 8, proofs 0, 1, 2, 4)
   give four different odds; PES-DICE's gate 2 (four levels, four obstacles on an unopposed row).
3. Step 1a, `build_realm(0)` and `(1)`, two seasons: a printed count of rolled acts whose obstacle differs
   from the base commit, each with its terms; expected zero, or only acts against a holder of the read key.
4. Step 5: CAL's test green; the realm tap (`runs/SC_INT/realm_tap.py` shape) shows more than two obstacle
   values for every rolled verb with five or more rolls.
5. A hand-built fold, two NPCs, one `argue`, the hearer holding one stance row toward the arguer at
   `(arguer, +4, 5)` in one arm and `(arguer, −4, 5)` in the other: the hostile arm's `terms` show `regard`
   0.8 × `regard_step`; the friendly arm's `levels` show `favour` and its `terms` show no `regard`.

## Falsifier

A rolled act whose `terms` hold a negative entry other than `ceiling`. A cell at any pool from 1 to 8 in
which adding a standing proof or a unit of favour leaves the exact odds unchanged. A rolled act with no
`opposition` entry. An obstacle that moves when a cited item is added. Two adjacent difficulty levels
composing one obstacle on any row at the calibrated arm. A host function that opens a ledger other than
the actor's.

## Layer 1 reading (`skills/layer-conformance`, Lens B)

`04` §A.2, the provider row (*owns nothing; reads a projection; returns a `Margin`*): conforms; the module
composes from a typed record and names no `engine/season` module. `04` §B.2 (the ledger is never read by
another person; F8): every host function above reads the actor's own ledger, a person's interior fields
(stance rows, pursuits, Tenures), a Record or the docket; grade MECHANICAL only where a test plants a
ledger read (gate 1's sibling in `test_sc02_reception.py`), otherwise CONVENTION, stated. `04` PART D row 30
(two degree ladders): one ladder; conforms. Columns of §A.2 read: owns, may read, emits, token.

## NERS reading

- **N**: without it every later table is tuned on a composition that clips what a speaker brings; top-down
  a designer names a level and a term; bottom-up each member reads one fact; lateral combat already
  separates the obstacle from advantage; diagonal a room's standard and a friend's regard reach one roll by
  two channels that do not interfere.
- **R**: complete at its extremes (bounded above by the cap, below by the floor, and leverage by the soft
  cap); characters, rooms and cases differ and each difference is in the record.
- **S**: one ladder for advantage in the social roll, the one combat uses; one roster; one composer.
- **E**, last: one field in place of a field per term; one sentence a player can say (*what stands against
  me is the obstacle; what I bring is my edge*).

## Cost class

Small build for steps 1a to 3 (one module function, one host table, one roster, the record). Edits
thereafter. Declared movers at 1b, 2, 5 and each shipped step.
