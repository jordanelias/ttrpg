# SC — contest and verb interrogation: census, dimensions, baseline, tuning surface

## Status: REFERENCE (an audit; resolves nothing at runtime)

Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: d7bd4ab (working tree; `engine/`, `modules/` and `systems/` unchanged since `601e715`, checked by `git diff --stat`)

Charge (Jordan, 2026-11-12): *"we will need to interrogate each contest type and verbs and tune for
venues and personalities affiliations etc etc etc."* With it: the social obstacle is the difficulty of
the task plus every associated modifier, never a flat 2. The implementation lane is building that form
(`IMPLEMENTATION_BRIEF_A.md`; the form is `proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`, SC-B
below). This file measures what the roll does today, finds the cells where tuning cannot act, and
designs the tuning surface and its calibration that sit on SC-B. It does not repeat SC's audit and
addendum, DICE's one-score proposal, FI's evidence interface or CHAR's NPC reconciliation; it cites them.

Proposals written by this lane: `proposals/13_SC_tuning_tables.md`, `proposals/13_SC_calibration.md`.

---

## 0. Verdict

**Today no tuning dimension reaches the social roll except two: the counterparty's held score, which
almost nobody holds, and a hearing bench's reception, which reaches one verb; every other dimension
Jordan names (venue, judge, temperament, conviction, affiliation, office, relationship, stakes,
publicity, season) is present in the world and read by nothing that rolls.** Measured: 284 rolled
social acts over seeds 0 and 1 (two seasons each) are all pool 2, and 270 of them roll the same
obstacle 2.0 (the fourteen others are seven `speak` rolls before a bench and seven forged-record
inquiries); a planted
grid of 54 cells per verb (3 venues × 2 temperaments × 3 affiliation relations × 3 stances) moves no
verb's obstacle at all, while the control dimension (a held score of 6) moves `tell`, `argue` and
`speak` and moves nothing for `lie`, `determine`, `interrogate` and `arrest`, which have no capability
key and therefore no opposition channel. The single largest obstacle to tuning is not a missing number
but a missing *seat for numbers*: the roll's record (`SocialContestInput`) has no field for the task,
the room's standard, the stakes or the hearer's regard, and the obstacle's bounds (the per-pool ceiling
above, `OB_MIN` below) already saturate the two modifiers that do exist, so a dimension added on
today's composition would be clipped flat in most cells. SC-B supplies the seats; this file supplies
the tables, their first values and the calibration that would set them, and finds that SC-B's proposed
difficulty ladder (`routine` = 1) puts a contest between equals at P(Failure) 0.71–0.74 and makes its
two upper levels indistinguishable at the cap. A half-step ladder (0 / 0.5 / 1 / 1.5) meets the targets.

## 1. Census

### 1.1 Contest types the tree names, and what the engine runs for each

Fourteen contest types are named in the charge or the tree. The engine has three carriers for them:
the three prize rows (`rosters.yaml: contest_subsystems`: `a standing`, `a proposition`, `a matter`,
`heard_by: bench` on the last), the nine arrangement rows (`arrangements.yaml`: `arbitration`,
`parliamentary_debate`, `council_of_state`, `legal_trial`, `tribunal`, `interrogation`,
`inquisition_hearing`, `excommunication_deliberation`, `negotiation`), and the kernel's eight
proceedings and thirteen venue presets (`systems/social_contest/sim/contest/modes.py:84, :485`), which
the loop never runs (SC audit §1(b)).

| contest type | engine carrier today | roll it uses | who judges | what it writes | computed play reaches it? |
|---|---|---|---|---|---|
| hearing | docket item + `speak` (filing) + `determine` (verdict) | `speak`: social roll, prize `a matter`, room = actor's place; `determine`: social roll, prize `a proposition` | `speak`: the bench `judging_set(place)` through `reception`; `determine`: no judge, the determiner rolls | `speak`: nothing (band picks the emit); `determine`: the disposal Tenure at Partial+ | `speak` 12 rolls / 4 seed-seasons; `determine` 1 roll (tap, §3.2) |
| petition | `petition`, `carry` | none (uncontested) | — | a Record; a docket item | yes, uncontested (SC audit §1: 20 filed, 2 seasons) |
| plea | self-plea: `speak {subject: himself}` (CP-T05-02) | social roll with opposition forced `None` (`sigma.py:207-211`) | bench | as `speak` | not observed in the tap |
| debate | `parliamentary_debate`, `council_of_state` rows; `argue` | `argue`: social roll, `a proposition`, no room | nobody: the hearer is the opponent | `Person.pursuits` at Success+ | `argue` 21 rolls |
| accusation | `open_case`, `petition` | none | — | a case, a docket item | yes, uncontested |
| interrogation | `interrogate` verb; `interrogation` row | social roll, `a proposition` | the actor (`remit:determine`) | nothing in any band | never attempted (corpus run, tap) |
| persuasion | `argue` | as debate | — | pursuits | as debate |
| lie / deception | `lie` | social roll, `a standing`, no capability key | — | nothing (band picks the emit) | 13 rolls |
| argument | `argue` | as above | — | pursuits | as above |
| appeal | `appeal_basis:` column on four arrangement rows | none: no verb reads the column | — | — | no |
| vote | `disposal: declared` (`excommunication_deliberation`); `world_q.declared_votes` | none: counted commits, not a roll | the seated bench by ballot | — | no `declared` row docketed (every item's `arrangement` is `None`, SC audit §1) |
| negotiation | `negotiation` row (`disposal: mutual`); `covenant`, `exchange` | none: `covenant` and `exchange` are uncontested | the two parties | an offer; a trade | `covenant` only refused (corpus run) |
| trial | `legal_trial`, `tribunal`, `inquisition_hearing` rows | as hearing | bench | as hearing | no row ever docketed |
| sparring / trial by combat | `challenge` → `accept` → `fight` | combat module (out of this lane) | — | body, tenure | PC lane (`IMPLEMENTATION_BRIEF_A` step 1–2) |

Read across: **four contest types roll** (hearing via `speak`/`determine`, debate/persuasion/argument
via `argue`, lie, interrogation), **six resolve with no roll at all** (petition, accusation, appeal,
vote, negotiation, the arrangement rows themselves), and the arrangement row, which is the only place a
venue's character is written, never reaches a roll because no computed docket item names one.

### 1.2 Verbs that resolve through a social, informational or political roll

Ten verbs reach `modules/social_contest/roll.py` (`VERB_TABLE` and `GRADED_INQUIRIES`, prior lane's
`runs/SC_INT/census_rows.txt`; the three `the body` verbs are combat's). The obstacle today is
`roll.py:141-154`: `opposition/2` or `obstacle_default` (2), minus the room
(`reception_gain·reception + proof_step·proofs`, floored at `OB_MIN`), plus `forgery_quality`, capped by
the per-pool ceiling. The pool is `pool.py::faculty`: the larger of the held vocation attribute and the
held capability key, else `pool_default` (2), plus practice.

| verb | prize / route | capability key (`verb_capability`) | pool from | obstacle from today | room read? | writes | rolls observed (seeds 0+1, 2 seasons) |
|---|---|---|---|---|---|---|---|
| `tell` | a standing | copying | faculty(copying) | counterparty's copying/Focus ÷ 2, else 2 | no | `[]` (WITNESS deposits) | 26 |
| `lie` | a standing | **none** | `pool_default` | **always 2** (no key → no opposition) | no | `[]` | 13 |
| `arrest` | a standing | **none** | `pool_default` | **always 2** | no | `Tenure.since` (detain) | 0 |
| `argue` | a proposition | argue | faculty(argue → Presence) | counterparty's argue/Presence ÷ 2, else 2 | no | `Person.pursuits` (Success+) | 21 |
| `determine` | a proposition | **none** | `pool_default` | **always 2** | no | disposal Tenure, pursuits | 1 |
| `interrogate` | a proposition | **none** | `pool_default` | **always 2** | no | `[]` | 0 |
| `speak` | a matter, `heard_by: bench` | copying | faculty(copying) | as `tell`, minus the room | **yes** | `[]` | 12 |
| `research` | graded inquiry | inquiry | faculty(inquiry → Reason) | 2 + the Record's `forgery_quality` | no | `[]` (finding) | 166 |
| `examine` | graded inquiry | inquiry | as above | as above | no | `[]` | 0 |
| `surveil` | graded inquiry | inquiry | as above | 2 | no | `[]` | 45 |

Twenty-nine further social, informational and political verbs resolve **with no roll** — their
outcome is decided by eligibility and `requires:` alone (`VERB_TABLE`, stratum read at the prior lane's
run): social `carry`, `challenge`, `commit`, `comply`, `conceal`, `construe`, `covenant`,
`evade / defy`, `forgive`, `give`, `interview`, `oblige`, `open_case`, `petition`, `tie / knot`,
`utter`; binding `confer`, `convene`, `dispatch`, `establish`, `issue`, `marshal`, `pardon`, `release`,
`revoke`, `succeed`, `surrender`; informational `forge`, `thread_read`. Three of these are contests in
all but code and are named in §4: **`interview`** questions a witness and returns `finding.made` with no
resistance from the witness; **`covenant`** is the negotiation's offer and cannot be refused by a roll;
**`conceal`** assumes a cover whose quality nothing grades. (Deciding which of the twenty-nine should
roll is the verb lanes' — `audits/14_VERBS_*` — not this one's; this file supplies the difficulty
column they would fill.)

## 2. Dimensions

| dimension | owner file (the fact) | read by the roll today? | what it should do (direction · shape) | where it enters (SC-B term) |
|---|---|---|---|---|
| **task** (the verb itself) | none: no column exists | no | + obstacle · a named level per verb row | `difficulty` (`verb_table.yaml` column) |
| **venue — the room's standard** | `arrangements.yaml` row (no key for it) | no | + obstacle · a named level per arrangement row | `standard` |
| **venue — the place** | `venues.yaml` buildings (`serves:` tags), `world_q.place_of` | only as the rung whose bench is read for `speak` | none of its own; the place matters through *who sits there* (the bench) and *what is admitted* (the row). Decided: no building-kind term (§6 R-3) | via `reception` and `standard` |
| **venue — what is admitted** | `arrangements.yaml: proofs:` | **no** (`world_q.proofs` reads every attributed deed, H-216's named limit) | filters `evidence`: a proof of a kind the row does not admit counts 0 | `evidence` |
| **the judge / bench** | `world_q.judging_set` → `reception` | `speak` only | − for favour, + for hostility · linear in reception, bounded | `reception` |
| **the counterparty's capacity** | `Person.capability` / `Person.attributes`, through `faculty`'s base | yes, for `tell`, `argue`, `speak`; **no** for `lie`, `arrest`, `determine`, `interrogate` (no key) | + obstacle · score × 0.5 (ruled) | `opposition` |
| **personality / temperament** | `Person.pursuits` (cohort temperament via `data/pursuits.py::temperament_pursuits`); `npc_registry.yaml: resonant_style` (18 rows); CHAR's `temper` (`02_CHAR_resolve_and_temper.md`) | no | the hearer's *susceptibility*: an appeal on the ground he is moved by gives the actor advantage; not an obstacle term (it is about the match of approach to person, which is the actor's choice) | leverage, by CHAR's `02_CHAR_which_ground_moves_whom.md` |
| **conviction and stance** | `Person.conviction`, `Person.stance` → `person_q.regard` | no (H-267) | − for regard toward the actor, + for hostility · clamped, linear | `regard` |
| **affiliation and faction ties** | `data/affiliations.py` (creed intensity, `INCOMPATIBLE`); faction by commit and office | no | **through regard only**: `person_q.heritage_regard` already folds creed and caste into regard (CR-31). No second term (§6 R-4) | `regard` |
| **office and standing** | Tenure (office holds), `rosters.yaml: rung_kinds` rank | no | + dice to the actor (*"Rank supplies dice and gates nothing"*, `verb_capability`'s source line) · one die when he holds a seat of the body the venue's bench belongs to | pool addend (`pool.register_pool_addend`) |
| **relationship** | `Person.stance` rows, CHAR's `relations:` ground (`02_CHAR_relations_have_a_ground.md`) | no | as conviction and stance: one quantity, `regard` | `regard` |
| **evidence held and cited** | `Claim`, `Record.forgery_quality`, `world_q.proofs` | `speak` (proofs), inquiries (forgery) | − for standing cited items, + for the other side's standing answers | `evidence`, `subject` |
| **stakes** | the Tenure kind a verdict or act opens (`disposes:`, `detain`) | no | + obstacle · by Tenure kind | `stakes` |
| **publicity and witnesses** | `arrangements.yaml: floor:` (open / closed / admitted), `records_dissent` | no | authored into the row's `standard` (an open floor is a harder room), not a separate term (§6 R-5) | `standard` |
| **season and territory conditions** | hunger bands, strife, stability | no | **none**, by decision: a hungry or rebellious season reaches a contest through the persons it has moved (their regard and reception), never as a global modifier (§6 R-6) | — |

## 3. Baseline measurements

All exact odds are `band_odds` / `record_odds` through the module's own `obstacle` (no draw). Realm
runs: `PYTHONHASHSEED=0`, `build_realm(seed)`, shipped chooser, seeds 0 and 1, two seasons each.
Scripts and full output under `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/SC_INT/`.

### 3.1 The composition's own grid (exact; `grid_odds.txt`)

Shipped fixtures: `obstacle_default` 2, `obstacle_ceiling` 2 with `ceiling_per_pool` (caps 2.0, 2.842,
3.6, 4.23, 5.508, 6.679 at pools 1, 2, 3, 4, 6, 8), `reception_gain` 1.0, `proof_step` 0.25, `OB_MIN` 1.

- **Equal parties (pool = held score) drift toward failure with size**: P(F) 0.42, 0.46, 0.49, 0.53,
  0.56 at 2, 3, 4, 6, 8 (the score/2 rate against `MU_PER_DIE` 0.4 per die).
- **A held score of 0 gives Ob 0.0**, below `OB_MIN`: P(F) 0.10 at pool 1, 0.11 at pool 2 — a person
  who holds the key at 0 is easier to persuade than nobody at all (2.0, P(F) 0.74). H-127's inversion
  at its extreme.
- **Opposition above the cap moves nothing**: at pool 2, scores 6, 8 and 12 all compose 2.842 (P(F)
  0.90); at pool 4, 12 and anything above compose 4.23.
- **The room saturates both ways at pool 2**: with no score, reception +2 and +4 and any proofs all
  compose 1.0 (the `OB_MIN` floor); reception −2 and −4 both compose 2.842 (the cap). The room has three
  states, not a scale.
- **Forgery saturates** at pool 2: quality 1, 2 and 3 all 2.842.
- **Effort is the one dimension that moves smoothly**: pool 2 at the default obstacle, effort 0–3:
  P(F) 0.74, 0.57, 0.42, 0.33 (`moderate` per level).

### 3.2 The realm (tap on `sigma.contest_input`; `tap_summary.txt`)

| seed | rolled acts | distinct pools | obstacles | realised bands (all verbs) | world hash after 2 seasons |
|---|---|---|---|---|---|
| 0 | 118 | {2} | 2.0 ×114 (one a `speak`); 2.842 ×3 (forged records); 1.536 ×1 (`speak`) | Failure 80, Partial 27, Success 11, Overwhelming 0 | `bacd687f…` |
| 1 | 166 | {2} | 2.0 ×156 (four `speak`); 2.842 ×4; `speak` 1.0–2.54 (6 distinct) | Failure 128, Partial 29, Success 9, Overwhelming 0 | `8aae8412…` |

Per verb, the exact mean odds equal the default pair's (F 0.74, P 0.19, S 0.07, O 0.00) for `tell`,
`lie`, `argue`, `determine`, `surveil`; `research` 0.747 (the forged three); `speak` 0.67–0.69 (the
room). **Zero Overwhelming in 284 rolls**, as the default pair predicts (0.00 to two places,
`band_odds(2, 2.0)`). The counterparties of person-subject acts hold convictions (23 of 25 rolls at
seed 0, 45 of 48 at seed 1) and carry regard toward the actor from −0.36 to +12.5; the obstacle does
not co-vary with either, since nothing reads them. In 18 person-subject rolls the counterparty held a
capability key, and it was `inquiry` in every one, which no person-subject verb reads; so no
counterparty in 284 rolls opposed with a score. No person holds an attribute
(`cast_attributes=False` ships).

### 3.3 The planted grid (`planted_grid.txt`)

`build_realm(0)`, one real co-present pair (`p_npc_005` → `p_npc_009` at `b_s_001_court`); for each
rolled person-verb, 54 cells = venue {own place (hearth, bench 2), the largest bench (territory, 5), no
room} × counterparty temperament {deontological, instrumental} (`temperament_pursuits(1,0)`, `(0,1)`) ×
affiliation relation {same creed at 5, incompatible creed at 5, none} × counterparty stance toward the
actor {−4×5, none, +4×5}; then the control: the counterparty holding the verb's key at 6.

| verb | distinct (Ob, P(F)) over 54 cells, no score | with the control (score 6) |
|---|---|---|
| `tell`, `argue`, `speak` | one: (2.0, 0.74) | one: (2.842, 0.90) — the control moves it |
| `lie`, `determine`, `interrogate`, `arrest` | one: (2.0, 0.74) | one: (2.0, 0.74) — **the control moves nothing** |

The venue does not move `speak` here because no bench member at either place holds an attributed deed
of the speaker at build (reception 0, proofs 0); the room is a channel that the world fills only after
deeds are witnessed, which is why the realm's `speak` rolls in §3.2 do vary.

### 3.4 Calibration sweep of the proposed form (`calibrate.txt`)

`Ob = max(min(difficulty + 0.5·score + hostile, cap(pool)) − favour, OB_MIN)`, the SC-B form. Pools 2,
3, 4, 6, 8; "equals" = counterparty score equal to the pool, "overmatched" = twice it.

| ladder (plain/routine/demanding/hard) | equals at `routine` | equals at `demanding` | equals at `hard` | overmatched at `routine` | unopposed at `demanding` |
|---|---|---|---|---|---|
| SC-B 0 / 1 / 2 / 3 | 0.74, 0.71, 0.72, 0.72, 0.72 | 0.90, 0.89, 0.88, 0.86, 0.85 | 0.90 at every pool | 0.90 at every pool | 0.74, 0.60, 0.49, 0.33, 0.23 |
| this lane 0 / 0.5 / 1 / 1.5 | **0.58, 0.60, 0.60, 0.62, 0.64** | 0.74, 0.71, 0.72, 0.72, 0.72 | 0.83, 0.83, 0.80, 0.79, 0.78 | 0.83, 0.89, 0.90, 0.90, 0.90 | 0.42, 0.32, 0.25, 0.17, 0.11 |
| this lane, opposition rate 0.4 (swept arm only) | 0.52, 0.52, 0.51, 0.51, 0.51 | 0.68, 0.65, 0.63, 0.61, 0.59 | 0.80 … 0.67 | 0.76 … 0.90 | as above |

The floor binds below everything: at `OB_MIN` 1 a pool-2 actor fails 0.42 of the easiest act (pool 1:
0.60). The ruled rate 0.5 leaves the equals drift (+0.06 from pool 2 to 8 at `routine`); the 0.4 arm
flattens it to ±0.01. The rate is ruled (Jordan, 2026-08-14) and SC-B already carries 0.4 as a swept arm
only; this file records the measurement and does not re-raise it.

## 4. Degenerate cells, ranked

Worst first. Each has its control.

1. **`lie`, `arrest`, `determine` and `interrogate` cannot be opposed.** No `verb_capability` row, so
   `_opposition_of` returns `None` and the obstacle is 2 against anyone: a liar faces a sage and a
   child alike. Control: the same counterparty holding a score of 6 moves `tell` (2.0 → 2.842) and
   leaves `lie` at 2.0 (§3.3). Fix: SC-P7's rows (`05_SC_capability_surface.md` edits 1–2) plus a
   `difficulty` per row; table T1 below.
2. **No dimension but score and bench reaches any roll; 270 of 284 realm rolls are one cell** (pool 2,
   Ob 2.0, P(F) 0.74, P(Overwhelming) 0.00). Control: `speak`'s room and the forged records are the
   only variation, and both are visible in the tap (§3.2). Fix: SC-B's seats plus tables T1–T5.
3. **A held score of 0 is near-certain success for the actor** (Ob 0.0, P(F) 0.10 at pool 1) while no
   score is 2.0. Control: score 2 → Ob 1.0, P(F) 0.42. Fix: SC-B's bound floors the composed obstacle at
   `OB_MIN` (`roll.py:118-120` says nothing floors it today); table T1's floor note.
4. **The room has three states, not a scale** (pool 2: favour ≥ 1 unit all compose 1.0; hostility ≥ 1
   all compose 2.842). Control: proofs 2 at reception 0 composes 1.5 — a half unit still moves. Fix: SC-B
   orders the bound (hard terms capped, favour after); the saturation that remains at small pools is the
   floor's, and calibration step 3 below measures how much of the scale survives.
5. **Opposition stops mattering above two to three times the actor's pool** (pool 2: scores 6, 8, 12 →
   2.842; P(F) 0.90 flat). This is the chance floor doing its job (10% Partial-or-better kept); stated,
   not a defect, but it means "overmatched" and "hopeless" are one cell, and a tuning of opposition
   above that line moves nothing.
6. **SC-B's ladder makes `demanding` and `hard` one cell for equals** (P(F) 0.85–0.90 versus 0.90
   everywhere) and puts equals at `routine` at 0.71–0.74. Control: the half-step ladder separates the
   four levels at pool 2 as 0.42 / 0.58 / 0.74 / 0.83 (§3.4).
7. **No roll ever lands Overwhelming** (0 of 284). Overwhelming needs Ob well under the pool's mean net;
   at pool 2 that is 0.00 at Ob 2 and 0.01 at Ob 1 (`band_odds`). A dimension that only Overwhelming writes
   (none of the ten rows today: `argue` writes the same at Success and Overwhelming) would be dead. Not a
   fix for this lane; recorded for the verb lanes, whose band maps should not hang anything on
   Overwhelming at pool 2.
8. **`interview` questions a witness with no roll.** A witness cannot resist questioning, so testimony
   is free. Control: `interrogate`, the bench's questioning, is a roll. Decision in §6 R-7.

## 5. Tuning surface

Five tables, one per kind of thing a designer tunes, each extending an existing owner; full keys,
units, first values, sweeps and falsifiers are in `proposals/13_SC_tuning_tables.md`.

| table | owner (single) | keys | unit | first values (basis) |
|---|---|---|---|---|
| T1 verb base difficulty | `verb_table.yaml` `difficulty:` column → `rosters.yaml: difficulty_levels` → fixture table `difficulty_ob` | the ten rolled verbs | obstacle units | `plain` 0, `routine` 0.5, `demanding` 1, `hard` 1.5 (§3.4); `tell`, `argue`, `speak`, `lie`, `determine`, `arrest` routine; `interrogate`, `research`, `examine`, `surveil` demanding |
| T2 venue standard | `arrangements.yaml` `standard:` key on each row, naming a `difficulty_levels` member | the nine rows | as T1 | `arbitration`, `interrogation`, `negotiation` plain; `parliamentary_debate`, `council_of_state`, `legal_trial` routine; `tribunal`, `excommunication_deliberation` demanding; `inquisition_hearing` hard (first reading: one level per formal layer the row interposes — `procedure`, `office`, `document`, `ceremony`; `person`, an advocate, is no layer; authored per row, so a designer overrides it) |
| T3 hearer disposition (regard) | fixture `regard_step` on `person_q.regard`, clamped at CHAR's `STANCE_MAX` unit | — | Ob per unit of regard ÷ `STANCE_MAX` | `regard_step` 1.0 per full `STANCE_MAX` (±1.0 Ob at the clamp), control 0 |
| T4 standing and stakes | fixture table `stakes_ob` (by Tenure kind); pool addend `standing_dice` | Tenure kinds; seat-of-the-bench test | Ob; whole dice | `oblige` 0, `detain` 0.5, `ban` 1.0 (SC-B's values kept); `standing_dice` 1 |
| T5 evidence | fixture `proof_step` (existing) and the arrangement row's `proofs:` admission | proof kinds | Ob per remove-weighted item | `proof_step` 0.25 kept; inadmissible kinds weigh 0 |

Temperament and susceptibility are **not** a sixth table here: they enter as advantage through CHAR's
`02_CHAR_which_ground_moves_whom.md` (a matched appeal ground is one named level of leverage), on the
existing `advantage_sources` roster. Affiliation enters through regard (T3) by `heritage_regard`.

## 6. Calibration plan

Full method and gates: `proposals/13_SC_calibration.md`. In brief:

- **What a calibrated table looks like on the four-band ladder**: for a contest between equals at
  `routine` in a `plain` room with neutral regard, P(F) in [0.50, 0.65] and P(Success or better) in
  [0.15, 0.30] at every pool from 2 to 8 (the half-step ladder reads 0.58–0.64 and 0.165–0.216); each
  difficulty step moves P(F) by 0.05–0.20 at equals; an overmatched side (opponent twice the pool)
  P(F) in [0.80, 0.90]; an underdog opponent (half the pool) P(F) ≤ 0.45; one unit of favour (a
  friendly hearer at the clamp, a favourable room) moves equals by ≥ 0.12; no two adjacent difficulty
  levels, and no two regard values a unit apart, produce the same cell at equals for pools 2–6.
- **Sweeps**: exact grids first (no draw, seconds), then one-season realm reads at seeds 0–2 for
  distribution only, never to set a value.
- **Order**: T1 alone; then T2 and T4 at fixed T1; then T3 and T5; each value moved alone against its
  control.

## 7. A playable contest catalogue

Every contest type is offered the same way the personal-combat duel round is (Jordan's PC intent):
the player chooses an **approach** and what he brings; the engine runs **one automatic round** from the
choice by the one roll; the NPC side chooses by the same interface through the chooser. One path: the
automatic round is the season loop's act, and the player's choice is a Candidate variant of it
(`05_SC_playable_hearing_B.md`; `08_FI_05_evidence-interface_B.md` edit 3 forms cited-item variants).

| contest | the player's choice surface | the automatic round | the other side (NPC, through the chooser) |
|---|---|---|---|
| persuasion / argument (`argue`) | the proposition (an uttered one); the **appeal ground** (one of the `resonant_style` values the registry authors: Evidence, Consequence, Solidarity, Authority); items to cite; effort | one draw: pool (argue → Presence) + leverage (effort, a matched ground) against `routine` + hearer's score/2 + regard + evidence | the hearer does not choose inside the round; he is moved or not. His standing answers (held contradicting items) enter `evidence` |
| telling / lie (`tell`, `lie`) | what to tell, to whom; for `lie`, the slant; effort | one draw against `routine` + hearer's score/2 (with SC-P7's `lie` row) + regard | the hearer's later trust is the consequence (WITNESS, `confidence.broken`); no in-round choice |
| hearing / plea / trial (`speak` + `determine`) | which matter; the items to file; concede a rung (a plea); effort; for a self-plea, no opponent | `speak`: one draw against `routine` + standard(row) + opponent's score/2 + reception − evidence; `determine`: the bench's draw against `routine` + standard + stakes(disposal kind) − the filed board | the opposing party files and answers by the same `speak`; the bench's `determine` is its own act (SC addendum B4.4's decider for the sitting, when the sitting is built) |
| interrogation (`interrogate`) | the questions as cited items (what he holds against the detainee); effort | one draw against `demanding` + the detainee's score/2 (SC-P7's row) + regard (the detainee's hostility) − evidence | the detainee resists by his score and his stance; a confession band deposits claims (FI) |
| debate (`argue` in a `parliamentary_debate` / `council_of_state` sitting) | as persuasion, before a bench | as persuasion, with `standard(row)` and reception in place of regard | each member's vote is his own `declared` commit; no averaging (SC addendum F-SC-20) |
| negotiation (`covenant`) | the terms (an uttered Proposition), the concession offered | **no roll by decision** (§8 R-8): acceptance is the counterparty's choice, scored by the chooser | the counterparty accepts or refuses as a Candidate scored by his pursuits against the terms |
| inquiry (`research`, `examine`, `surveil`) | which record, site or place; effort | one draw against the verb's difficulty + the subject's forgery/cover | none: the subject resists only through what it is |

What the round reports back, in every row: the band, and SC-B's term list (`Ob 2.5 = routine 0.5 +
opposition 1.5 + standard 0.5`), so the outcome is legible to the player and the chronicle alike.

## 8. Resolutions decided

| # | item (inconsistency · gap · unclear) | resolution | ladder step | carried by |
|---|---|---|---|---|
| R-1 | SC-B's level sizes (0/1/2/3) put equals at P(F) 0.71–0.74 and merge `demanding`/`hard` | ship SC-B's sizes as the **control arm** in the implementing commit (it reproduces today's 2 for unscored opponents); the half-step ladder is the first calibrated arm, a separate declared mover | 5 (architecture: a bytes-preserving landing, then a declared mover) | `13_SC_tuning_tables.md` T1 |
| R-2 | a held score of 0 composes below `OB_MIN` | floor the composed obstacle at `OB_MIN` (SC-B's bound already says so; PP-232's floor) | 2–3 (superseded by SC-B; `OB_MIN` is the dice engine's floor) | SC-B; T1 note |
| R-3 | is "venue" the building, the bench or the row? | the row (standard, admission) and the bench (reception); the building kind gets no term — a moot hall and an inn differ by who sits there and what is docketed, which the engine already knows | 5 | §2; T2 |
| R-4 | affiliation as its own modifier, or through regard? | through regard only (`heritage_regard`, CR-31, already reads creed and caste) | 4 (precedent: CR-31) | T3 |
| R-5 | publicity (`floor:`) as a term? | authored into the row's `standard` value; no formula over `floor:` | 5 (one table, not two) | T2 |
| R-6 | season and territory conditions as a modifier? | none; they reach the roll through persons' regard and reception | 5 (no global modifier is scripting by aggregate; `04:237` forbids social aggregates on a Rung) | §2 |
| R-7 | `interview` resolves with no roll | it stays unrolled as the **cooperative** questioning (a witness who wants to talk); resistance is `interrogate`'s (bench) and, outside a bench, `argue` to make him speak. Recorded for the verb lanes, not edited here | 4 (precedent: `interview` is `own`, `interrogate` is `remit:determine`, the row's own eligibility note) | — |
| R-8 | negotiation has no roll | correct as built: acceptance is a choice of the counterparty, not a draw; the tuning is the chooser's scoring of terms | 5 | §7 |
| R-9 | temperament: an obstacle term or an advantage? | advantage, through CHAR's susceptibility rows; the obstacle reads only what stands against the act, not the match of approach to hearer | 4 (precedent: `advantage_sources`, CP-T01-05) | T-note in `13_SC_tuning_tables.md` |
| R-10 | office and standing: dice or obstacle? | dice (*"Rank supplies dice and gates nothing"*, `verb_capability`'s source line); one die for a seat-holder of the body whose bench hears | 3–4 | T4 |
| R-11 | `05_SC_negotiation_scene.md` and `05_SC_evidence_and_rebuttal_B.md` are cited by SC's addendum and SC-B but do not exist in `proposals/` | cite the existing `05_SC_evidence_and_rebuttal.md`; the negotiation row is §7 here | 1 (the unsuffixed file is the live one) | this file |

**Survivors for Jordan: none.** The opposition rate (0.5 ruled vs 0.4 flat) is a ruled item and stays
a swept arm, not a question.

## 9. NPC and chooser side; evidence and argument

- **Who decides, on what**: the actor is whoever's chooser formed the act; the counterparty is the row's
  operand (`loop/sides.py::sides_of`); every term in §5 reads the counterparty's or the room's own state,
  so an NPC-versus-NPC contest takes its obstacle by the same function (SC-B, "How an NPC-versus-NPC
  contest gets its obstacle"). Nothing in the tables names a player or a person.
- **What the chooser sees**: `believed_input` fills the public terms (difficulty, standard, stakes)
  always and the private ones (opposition, regard, the other side's answers) from claims, per
  `10_DICE_believed_odds_have_a_prior.md`. A person therefore picks easier venues and friendlier hearers
  only to the extent he knows them — the characterful part (CHAR's reconciliation, `02_CHAR_audit.md`).
- **Evidence and argument** (the detective/noir charge): the tables give evidence one seat (T5, on SC-B's
  `evidence` term) whose weight is set by what is cited and left standing (SC-P8,
  `05_SC_evidence_and_rebuttal.md`) and filtered by what the room admits (`proofs:`), which is the L.A.
  Noire / Ace Attorney shape (a held item, a room's rules of admission) and nothing more. Argument
  (skill against a person) and evidence (deterministic weight) stay separate terms on the one roll.

## 10. Capability authoring (§14 of the brief, for this lane's interface)

The ten rolled verbs take capability at two points: the actor's pool (`faculty`, via `verb_capability` →
`vocation_attribute`) and the counterparty's opposition (`_opposition_of`, via the same rows and
`opposed_by`). Both are data-driven; the gap is the four verbs with no row (degenerate cell 1). The
tables here add no capability system: T1–T5 are fixture and roster rows on the owners SC-B names, and a
designer defines a new contest by giving its verb a `difficulty:` level and a `verb_capability` row, and
a new venue by an arrangement row with a `standard:`. The interface this lane needs from the holistic
merge is SC-B's term list on `Margin` (so every roll says which capability fed it).

## 11. Evidence log

| # | command / probe | seed, seasons | outcome |
|---|---|---|---|
| 1 | prior lane: `VERB_TABLE` / `GRADED_INQUIRIES` census → `runs/SC_INT/census_rows.txt` | — | 14 contested or graded rows (10 social roll, 3 body, 1 field) |
| 2 | prior lane: stratum listing (`VERB_TABLE` by `stratum`) | — | social 21, binding 12, contested_physical 9, material 23, movement 2 |
| 3 | `git diff --stat 7289ef2 HEAD -- engine modules` and the prior lane's `601e715..HEAD` | — | empty: code unchanged |
| 4 | `python runs/SC_INT/grid_odds.py` → `grid_odds.txt` | exact | §3.1 |
| 5 | `python runs/SC_INT/realm_tap.py 0 2` → `realm_tap_s0.json` | 0, 2 | 118 rolls, pool {2}, hash `bacd687f1470883b412be9638d0b0f88`, 23 s |
| 6 | `python runs/SC_INT/realm_tap.py 1 2` → `realm_tap_s1.json` | 1, 2 | 166 rolls, pool {2}, hash `8aae8412c221edb44ffd45d91bae2671`, 21 s |
| 7 | `python runs/SC_INT/analyse_tap.py` → `tap_summary.txt` | 0, 1 | §3.2; every tapped input matches the graded pair (asserted) |
| 8 | counterparty capability keys in the tap | 0, 1 | `inquiry: 2` only (10 cases); no attribute held |
| 9 | `python runs/SC_INT/planted_grid.py` → `planted_grid.txt` | build 0 | §3.3 |
| 10 | `python runs/SC_INT/calibrate.py` → `calibrate.txt` | exact | §3.4 |
| 11 | read: `modules/social_contest/roll.py`, `seam/wrappers/sigma.py`, `pool.py`, `world_q.reception`/`proofs`, `data/affiliations.py`, `arrangements.yaml`, `venues.yaml`, `rosters.yaml: verb_capability`, `vocation_attribute`, `affiliation_engagement`; SC audit §0–1 and addendum B4; SC-B; heads of SC-P4, SC-P7, SC-P8, CHAR resolve/relations/ground/regard-unit, DICE believed-odds | — | cited above |
| 12 | earlier lanes' readings reused (not re-run): `runs/SC/corpus_run.txt` (143 cases, seed 0), `runs/DICE/rollers_4_0.txt` and `rollers_2_1.txt`, `runs/SC_B/difficulty_odds.txt` | 0, 1 | `lie`/`argue`/`tell` corpus bands; 564 of 568 realm rolls pool 2 Ob 2 (DICE) |

No pytest run; nothing tracked was written but this file and the two proposals.
