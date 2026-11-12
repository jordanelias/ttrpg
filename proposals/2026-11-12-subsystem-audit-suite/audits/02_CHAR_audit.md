# CHAR — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Scope: `engine/season/decision/` (`budget`, `choose`, `options`, `questions`, `sheet`),
`queries/person_q.py`, `goals.yaml`, `npcs.yaml`, `cohorts.yaml`, `data/{cast,goals,pursuits}.py`, the
`conviction_spread`, `decision_spread` and `heir_hears` harnesses, `systems/characters/`, the
character-layer, attribute and character-sheet proposals, and the pursuit-basis worksheet. Every run
below is `PYTHONHASHSEED=0`; outputs are in the scratchpad folder named in §12. Probes are scratch
scripts and are not repository artifacts.

## 0. Verdict

The character and decision layer is a sound structural basis for a dynamic emergent-narrative game and
is not yet a behavioural one, and the single largest obstacle is that a person's ranking of acts reads
the verb and nothing about what the act would do: 36 of 46 cast persons hold one top verb across six
different situations, goals pick whom a person attends to and then stop, and the only thing that makes
a person depart from that fixed order is one realm-wide draw that makes two identical characters
disagree in seven decisions of ten. What is sound is real and executes: no `World` under `decision/`,
an option set computed from the verb table, one owner of the score, a draw keyed by candidate, a belief
filter that declines about 4% of candidates, and a score that does separate characters (two persons
with near-identical values rank fifteen candidates at Kendall +0.88, two with opposed values at −0.20).
What is missing is motion and consequence inside the person: over two played seasons stored stance
moved for 0 of 83 persons at both seeds, pursuits for 1 and 0, the scar counter passed its three-rung
ladder thirteen-fold for everyone, and four in ten resolved acts were refusals. R-06, R-07 and R-08
are each `partial` in the register for reasons narrower than these; the residues they name (a tie
broken by inclination; an `ambitions(p)` reader) are closed or nearly moot, and the live residues are
the ones measured here.

## 0A. NPC and AI-chooser design intent, as established

The other lanes cite this section. It states the intent that can be established from **code plus
ruling**, marks what is **prose only**, and names where the sources disagree. Where they disagree the
ruled and built wins (§0.05).

### Established (built, and ruled or registered)

| # | intent | where it is the mechanism | ruling or register row |
|---|---|---|---|
| I-1 | **Every person decides, and only persons act.** A faction is a view; its act is a person's act through a seat. The player is a person whose choices come from outside | `loop/deliberate.py:202`; `Act.via`; `harness/play_surface.py::dispatching_chooser` | ED-IN-0201; Layer 1 PART D; H-60 (everyone runs `choose`) |
| I-2 | **A person decides on his own state and nothing else**: his claims, edges, pursuits, stance, convictions, scars, attributes; a `View` of at most twelve claim ids; the question he was handed; his believed odds | `decision/` (no `World` by path scan), `queries/person_q.py`, `View.odds` | AX-2; Jordan 2026-09-02 (*"our understanding of all other words and actions is subjective and singular"*); H-03 |
| I-3 | **What a person is after is a weighted vector over fifteen pursuits on seven bipolar axes; religious affiliation is a separate intensity** | `Person.pursuits`, `Person.conviction`; `rosters.yaml: tables.pursuit_projection`, `alignment` | ED-IN-0261; ED-IN-0251; ED-IN-0293 (1), (2) |
| I-4 | **An ambition is a standing commitment that raises a question every season**; organizations author goals that orient their members' attention | a live `commit` to an OUGHT; `world_q.questions_for` Q4; `attention_key`; `goals.yaml` | H-04; ED-IN-0293 (8), (10) |
| I-5 | **The option set is computed, never authored**, from the verb table, the person's eligibility, the question's referents and what he does not believe false | `options.opening_set` | H-03, H-94; D2 |
| I-6 | **A choice is a ranking by values and regard, sampled**: pursuit · alignment (times the believed chance on a contested act) plus regard for the subject, drawn at a temperature | `choose.score_terms`, `_sample_order` | H-66 (the table is invented and swept), H-96, H-194, H-202, H-248 |
| I-7 | **The person triages against a budget he asks for**; the engine never truncates. Office raises it, wounds and travel lower it | `budget`, `release`, `pack_scenes` | Jordan 2026-09-02 (five scene actions); S26.3; H-28, H-74 |
| I-8 | **What is true is moved by evidence; what is right is moved by argument and consequence, never by evidence** | WITNESS writes claims only; `argued_pursuits`, `consequence_pursuits` write at RESOLVE | #353 §9.3; AX-3 |
| I-9 | **Regard is computed when read** from stored stance, judged deeds, told deeds and believed descent; nothing stores an opinion | `person_q.regard` | IN-18 G1; H-192, H-193; ED-IN-0301 |
| I-10 | **Hearsay is graded when read, by the hearer's relation to the teller** | `options.teller_weight`, `LedgerReader` | CAT-3 |
| I-11 | **Capability supplies dice and gates nothing** (one declared exception: the Thread Sensitivity gate) | `seam/wrappers/pool.py::faculty`; `OwnStateReader` | #353 §9.2; H-85, H-239 |
| I-12 | **A population is one person at weight above one**, and subsistence is its concern, not a lord's | `cohorts.yaml`; `Person.is_cohort` | ED-IN-0255; S9 |
| I-13 | **The cast is closed and authored; nobody is generated on a clock** | `references/npc_registry.yaml` → `data/cast.py` | ED-WR-0011 |
| I-14 | **The player's sheet ranks and selects; it never forms and never writes** | `decision/sheet.py` | A-25; ED-IN-0349 |

### Ruled, and not yet built (intent with authority and no mechanism)

Deontology as a refusal (ED-IN-0261; built, shipped unarmed). The scar's weight shift at threshold 2
(ED-IN-0261; built, shipped at 0). Risk appetite and a short, medium or long horizon (ED-IN-0304; no
carrier). Duty of office and the cost of betrayal (ED-IN-0335, ED-IN-0338; CR-88, design-first).
Attributes in a person's own choice and on others (ED-IN-0347; CR-93, CR-92, design-first). The ten
attributes on a person (ED-IN-0328; the carrier ships off).

### Prose only (quarantined design; vocabulary and history, not intent the code follows)

From `npc_behavior_v30.md`, read at §1, §3, §4, §5.0b to §5.1, §8.1, §8.11 and §9: the Stance Triangle
(Conviction, Ethical Framework, Resonant Style); the four Resonant Styles as a hearer's vulnerability;
Belief structure and revision; the Decision Procedure and its Decision Fork by scar count; a
seven-level priority tree per faction; an authored arc map per named NPC; coherence thresholds for
practitioners; NPC outreach and demand entries addressed to the player. From
`npc_relational_graph_v30.md` (head only): named edge types between NPCs with strain, capacity and
rupture. From `player_agency_v30.md` (outline only): Duties, the Scene Slate, Stature progression.

### Where the sources disagree (the ruled and built wins)

| design says | ruled and built | consequence for every lane |
|---|---|---|
| thirteen Convictions over four axes (`npc_behavior_v30` §1.2, marked CANONICAL in its own header) | fifteen pursuits over seven axes (ED-IN-0261, the 2026-10-06 row) | no conviction name from the design corpus is a key anything reads |
| a faction takes a faction-level action each season from a seven-level priority tree (§8) | no faction acts; a seat-holder's own ranking is the faction's conduct (ED-IN-0201) | a per-faction precedence list in any subsystem is scripting drift |
| named NPCs follow authored arc maps (§5.2) | no arc, story or thread carrier exists (ED-IN-0225); an arc is something an observer reads off the log | an NPC rule keyed on a name or an arc stage is scripting drift |
| a Decision Fork resolved by scar count, with a crisis table a GM rolls (§4.1, §3.3) | scars shift weights (dormant) and the crisis is a rule that rolls nothing (G-Q6); there is no GM | no lane may assume a referee's judgement |
| survival overrides conviction when Stability is low (§4.1, §8.1 priority 1) | no term reads need or danger; `urgency` was deleted (REM-44); condition changes the scene count only | an NPC does not save himself; a lane that needs it must say so |
| officers and functionaries *"do whatever the institution incentivises"* (§4.1) | everyone runs `choose` on his own vector; a cohort holds its territory's temperament | there is no second, simpler chooser for minor persons |
| presented evidence can crack a conviction (the Evidence style) | evidence moves claims; only argument and consequence move the moral layer (#353 §9.3) | a contest that turns evidence into a changed value must do it through `argue` |
| Disposition and Knots for the player; a relational graph for NPCs | one stance row type and one `regard` for every pair, the player included | no lane keeps a player-only relationship store |
| one scar per season from witnessing (`conviction_track` §3, as the retained oracle encodes it) | uncapped | F-CHAR-04; the cap is proposed |
| `decision_policy_v1.md` is listed as a chooser source | it is the repository's own precedence order for editorial rulings (DRAFT FOR RULING); it says nothing about how an NPC decides | not a source for this intent |

### One chooser interface for a player-proxy and an NPC

**At the season's scale, yes, and it executes.** One signature, `choose(p, v, s, ask_budget) -> Scene[]`.
`make_chooser` is the NPC; `dispatching_chooser` routes a named person to a callback;
`development_space` shows the player `make_ranker`'s own list and packs his picks through `release`,
the NPC's own packing step; `take_ranked` is the control under which the player is the NPC.
Closed-set options on an act (`choice_sourced`: an order's role and retreat rule, a march's posture)
reach both through the same candidate list.

**Three limits.** (1) The callback receives the live `Person`, where Layer 1 specifies a frozen copy
(F-CHAR-12). (2) Inside a contest the interface is a different one: a played person's per-turn
`decide(view)` at the grid suspension (REM-31); an NPC has no decider there, only the module's default.
(3) Nothing but tests calls the sheet; there is no client (§9).

### What an NPC needs to be characterful, and legible afterwards

Distinguishable choices need the score to read the situation (F-CHAR-01), the departure from it to be
the person's (F-CHAR-02), and an interior that moves (F-CHAR-03, F-CHAR-04). Legibility needs a reason
trail: today only the occasion survives a decision (the question on the `Scene`); `Act.reads` is empty
(H-343) and `why` was cut from `Candidate`. Proposals: `02_CHAR_goal_lean_on_its_own_question.md`,
`02_CHAR_resolve_and_temper.md`, `02_CHAR_scar_cap_and_regard_unit.md`, `02_CHAR_choice_alignment.md`,
`02_CHAR_reason_trail_and_small_edits.md`.

### Scripting drift inside this lane's own scope

None found in `decision/`: every branch reads a row's column or a roster, never a verb or a person by
name (read in full). Named roster members held as checked literals: `person_q.DOCTRINE_PURSUIT`,
`RELIGIOUS_CONCERNS`, `data/pursuits.TEMPERAMENT_AXIS`, `options.COMPETENCE_ATTRIBUTE`. The instrument
`harness/heir_hears.py` names `off_king` and `off_heir`; it is a reader, not a rule.

## 1. What it is, as coded

**Modules and entry points.**

| module | what it owns | reached from |
|---|---|---|
| `decision/questions.py` | `assemble` (the `View`), `aggregate_questions` (rule `first` ships), `view_ids` | `loop/deliberate.py` |
| `decision/options.py` | `opening_set` (§F1: candidates from `VERB_TABLE`, in sorted verb order), operand derivation (`operand_bags`, `_derive_operand`), person-side eligibility and seats, `project`, the refusal gate, `standing_of`, refraction (`refracted_confidence`, `dissents`, `competence`), hearsay weighting (`teller_weight`, `record`, `rank`) | `choose.make_ranker`; `loop/witness.py` and `loop/matter.py` for the readers |
| `decision/choose.py` | `score_terms` → `(pursuit, stance)`, `stance_term`, `odds_weight`, `settle_efforts`, `score_order`, `_sample_order` (Gumbel at `choice_temperature`), `make_ranker`, `release`, `pack_scenes`, `declare_intents`, `make_chooser` | built by the caller (`harness/probes.py::chooser`, `headless`, `populated`), handed to `SeasonDriver.season` |
| `decision/budget.py` | `budget` = base + office bonus × live holds − body bands − travel legs, floor 1 | `loop/deliberate.py` (`ask_budget`) |
| `decision/sheet.py` | the player's three spaces: `creation_sheet`/`seat`, `development_space`, `chronicle` | tests only (see §9) |
| `queries/person_q.py` | asker-first readers: `stance_toward`, `regard`, `deeds_judged`, `legitimacy`, `stability`, `opinion`, `crisis_weights`, `confliction`, `conviction_after_crisis`, `LedgerReader`, `OwnStateReader`, `said_of`, `lie_said_of`, `known_persons`, the pursuit movers (`consequence_pursuits`, `argued_pursuits`) | `decision/`, `world_q`, the fold |
| `data/cast.py`, `data/goals.py`, `data/pursuits.py` | loaders and validators for `references/npc_registry.yaml` (46 rows), `goals.yaml` (38 rows, no `goal_stages`), the pursuit projection | world-gen (`harness/populated.py`) |
| `npcs.yaml`, `cohorts.yaml` | 46 authored persons' homes and ties; 37 population cohorts at weight 2 | `build_realm` only |
| `systems/characters/sim/conviction.py` | a second scar model (module-level store, thresholds 1/2/3, a season cap of 1) | `systems/fieldwork/sim/knots.py` (a late import) and two tests; never the season loop |

**How the loop reaches it.** `loop/deliberate.py:202` calls `choose(p, v, s, ask_budget)` once per
person per round. The questions are produced world-side (`queries/world_q.py:4031 questions_for`: a
claim that landed within the person's reach, and one standing `need` question per live `commit` to an
OUGHT) and ordered by `world_q.py:3857 attention_key` (five tiers, salience inside tiers 0 and 3). At
the shipped `question_aggregation_rule: first` one question reaches the chooser per deliberation.

**The score, as coded** (`decision/choose.py:193-221`):
`pursuit = damp · Σ_axis project(p)[axis] · align(c.verb, axis) · odds_weight`, and
`stance = (1 + stance_gain) · ±regard(p, c.subject)` (negated where the subject is the contested
opponent; `hostile_stance_gain` on violent rows). The `Sensation` is passed and read by no term since
REM-44.

**State it owns.** None. It reads `Person.pursuits`, `conviction`, `scar`, `stance`, `tenures`,
`ledger`, `attributes`, `thread_sensitivity`, `body`, `travel_leg`. The writers are acts at RESOLVE.

**Shipped fixture values that decide what is live** (read from `DEFAULT_FIXTURES`): temperature 0.05;
`stance_polarity` declared; `stance_gain` 1; `hostile_stance_gain` 2; `odds_weighting` believed;
`npc_effort` on; `judged_gain`, `told_valence_gain`, `heritage_gain` 0.5; `pursuit_shift` 0.1;
`lie_offered` True. At their control (off): `refusal_axis` None, `scar_weight_shift` 0,
`confliction_weight` 0, `intent_disclosure` 0, `competence_gain` 0, `said_slant` newest,
`telling_privacy` 0, `scar_excludes_actor` False, `build_realm(cast_attributes=False)`.

**Execution evidence.**

- `conviction_spread`: 4 of 15 pursuits within 60° of the mean direction; 3.93 effective axes of 7.
- `decision_spread --persons` (seed 0): 83 persons (46 cast, 37 cohorts), all with a vector; 11 cast
  pairs above cosine 0.99; 0 identical cast profiles; every territory's cohorts share one vector.
- `decision_spread --decisions` (seed 0): 498 readings, deciding term draw 223, pursuit 265, stance
  10; outvoted 219 at a median lead of 0.0590. This reproduces the figures `requirements.yaml` R-08
  records for the same seed (223, 0.0590), so the instrument and the tree are deterministic across
  sessions.
- `decision_spread --season` (seed 0): 749 resolved acts by 83 actors; answered questions:
  `claim_landed` 312, creed 13, own want 11, other need 45, two organization goals 1 each.
- Probes 1 to 3 (§12): the figures used in §3.
- `headless --case NPC-088 --seasons 2 --seed 0`: 16 and 17 acts, hash `5405522c`.

## 2. Steelman

Ranked by the weight each bears. Each was attacked by the cheapest observation that could break it.

1. **The score separates characters, and the separation is the persons' own.** Attack: give everyone
   one vector and see whether variety survives. Result (probe 1, cast only, temperature 0): score-top
   disagreement between two persons rises with the angle between their vectors (0.106 at cosine
   > 0.99; 0.179; 0.485; 0.719; 0.952 at cosine < 0), Kendall of their full orders falls from +0.876
   to −0.198, and under the control every person takes one top (`create_record`, 46 of 46). **Holds.**
   The pursuit basis is a working discriminator between people.
2. **No decision reads world truth (AX-2).** The package names no `World`; three path scans exist
   (`test_season_shape.py:1020`, `:2927`, `:3220`). Attack: find a route by which the chooser reaches
   more than a person's own state. Two found: Layer 1 says `choose` receives *"a `PersonInterior` — a
   frozen copy with no store handle"* (`04_CODE_ARCHITECTURE.md:249`, `:1027`), no such class exists
   in `engine/`, and `loop/deliberate.py:202` hands the live `Person`; and `View.odds` is a callable
   closed over the `World` (`decision/sheet.py`, its docstring, calls this a CONVENTION). **Holds as
   "no `World` name in scope"; fails as "a frozen copy"** (F-CHAR-12).
3. **The option set is computed, not authored.** No roster of options reaches `opening_set`. Attack:
   is it reached and non-trivial? 45,520 candidates formed over 774 deliberations in two seasons
   (probe 2, seed 0). **Holds.**
4. **Imperfect knowledge is structural and shapes choice.** Attack: is clause 4 inert?
   `belief_contradicts` was asked 98,542 and 98,480 times over two seasons at seeds 0 and 1 and
   declined 3,806 and 3,808 candidates. **Holds** for declining on what a person believes. It does not
   show that anybody believes something false (F-CHAR-09).
5. **One owner per rule, and instruments call the owner.** `score_terms`, `score_order`,
   `sample_order`, `to_axes`, `LedgerReader._best`, `deed_term` each have one definition, and
   `decision_spread.attribute_top` calls the chooser's own functions. Attack: look for a second copy.
   Found: the dot product is summed in two orders (H-362), and the person-side decline exists nine
   times (F-CHAR-11). **Holds for the score; fails for the declines.**
6. **The draw is keyed by candidate, so a fork is attributable.** `choose.py:462` seeds
   `choice:<verb>:<subject>` per person. Attack: none cheaper than the tree's own (W-D); not re-run.
   **Holds as read** `[UNVERIFIED by a run here]`.
7. **Every invented magnitude is declared, defaulted and swept, with a control that reproduces the
   base.** Attack: count how many of the mechanisms that would move a person's interior ship at the
   control. Seven of nine (§1's list). **The discipline holds and its product is a tree whose interior
   mechanisms are off** (F-CHAR-03, F-CHAR-04; `research/by_lane/NPC_npc_cast.md` T-NPC-5 reached the
   same reading independently).
8. **The player and the automated chooser share one path.** `development_space` ranks with
   `make_ranker` and packs with `release`; `take_ranked` is the control. Attack: is anything but a
   test a caller? No (`grep`: `test_g2_token.py`, `test_cr20_attributes.py`,
   `test_rem30_character_sheet.py`). **Holds as one code path; fails as a playable surface** (§9).

## 3. Adversarial findings

Ranked worst first. Severity: **B** blocks a requirement, **D** degrades narrative, **H** hygiene.

### F-CHAR-01 · B · the ranking does not read what an act would do

- **Claim.** A person's order of verbs is the same in every situation. A goal selects a subject and
  then has no say in what is done about it.
- **Evidence.** `decision/choose.py:215`: the pursuit term reads `c.verb` only. Probe 3, built realm,
  cast, six common referents, temperature 0: 36 of 46 persons have one top verb across all six, 10
  have two; 23 of 46 hold one full verb order across all six; `create_record` is the top for 25 to 28
  of 46 at every referent. The stance term's variance across candidates is zero in 253 of 276
  readings. `decision_spread --season`: organization goals account for 5 of 749 resolved acts.
  H-283 (register line 5565) and H-289 (line 5643: `succeed` formed every season, executed 0 times in
  9 heir-seasons, score near 0.022 against a top near 4.05) are instances.
- **Falsifier run.** If situations mattered, the count of persons with one top verb across six
  referents would be small. It is 36 of 46.
- **Touches.** R-06 (goals, ambitions), R-04 (an office's business), R-02 (a later decision differs
  only by subject).
- **Narrative consequence.** The realm's commonest act is the same paperwork whatever happened. An
  heir does not take a vacant throne; an officer does his office's business exactly as he does his
  own.
- **Minimal fix at the owner.** `score_terms` gains a term scoped to the question a goal raised
  (`proposals/02_CHAR_goal_lean_on_its_own_question.md`, an input to CR-88's design item (3)).
  Valuing an act by its declared writes against a goal's aim is design-first and belongs to
  `goal_stages` (CL-THRUST B2.2, unauthored).

### F-CHAR-02 · B · the departure from the optimum is the realm's, not the person's

- **Claim.** R-08's built half is one realm-wide temperature. It makes identical characters disagree
  more often than conviction makes similar ones disagree, and its effective size varies sixfold
  between persons by an accident of authoring.
- **Evidence.** `choose.py:431` (`tau = fx.get("choice_temperature")`, no person input). Probe 1,
  seeds 0 and 1: the sampled top is not the score's top in 46% and 42% of 276 cast readings; pairs
  with cosine > 0.99 take different sampled tops in 56% and 62%; under the control (one vector for
  all) 74% and 70%; opposed pairs 95%. Per-person outvote rate against the length of the projected
  vector: r = −0.63 and −0.48, the length running 0.14 to 0.89.
- **Falsifier run.** The control arm: with identical persons, disagreement should be near zero if
  character drove it. It is 70 to 74%.
- **Touches.** R-08, R-06.
- **Narrative consequence.** One observed decision says nothing about who a person is. Boldness,
  steadiness and rashness do not exist as properties anyone can learn.
- **Minimal fix.** Name the quantity (`person_q.resolve`) and put the per-person factor where CR-93
  item (2) already plans it (`proposals/02_CHAR_resolve_and_temper.md`).

### F-CHAR-03 · B · the interior does not move

- **Claim.** Over two played seasons nothing a person feels toward another, wants, or can do changes
  by an amount that could alter a choice.
- **Evidence.** Probe 2, `build_realm`, two seasons, shipped chooser: stored stance moved for 0 of 83
  persons at seed 0 and 0 of 83 at seed 1; pursuits for 1 and 0. Probe 3 (seed 0): `fight` 0 and
  `forgive` 0 resolved; regard differs from stored stance in 656 of 2,070 cast pairs, with a median computed half of 0.051
  on a ±25 scale. At build, of 46 cast: attributes 0 (the switch ships off, and the registry authors
  one `stats:` row), capability 2, thread sensitivity 10, heritage 4.
- **Falsifier run.** A stance writer reached by ordinary play would show a non-zero count. Two seeds
  read 0.
- **Touches.** R-07 (feelings, attitudes, relationships), R-06 (development).
- **Narrative consequence.** Loyalty is a build-time constant; a witnessed betrayal weighs a
  five-hundredth of one authored loyalty step. No friendship forms and no grudge is earned in a realm
  at peace.
- **Minimal fix.** `regard`'s judged and told halves in the stance unit, on `heritage_regard`'s own
  precedent (`proposals/02_CHAR_scar_cap_and_regard_unit.md`). A stored opinion is CR-83's question
  and is not pre-empted.

### F-CHAR-04 · D · the scar runs away and its live reader fires on noise

- **Claim.** The count ruled on a 1/2/3 ladder reaches a median per-person maximum of 41 in two
  seasons; the terminal rung's reader is live and rewrote convictions for 6 of 46 cast at one seed.
- **Evidence.** `loop/resolve.py:617 _scar_witnesses` (one count per observer per violated element
  per act, no bound; its docstring calls the predicate *"A CANDIDATE READING, NOT A RULING"*).
  Probe 3, seed 0: 83 of 83 scarred, median maximum 41, maximum 61, 19 elements. Probe 2:
  `Person.conviction` changed for 0 of 46 cast at seed 0 and 6 of 46 at seed 1.
  `systems/characters/sim/conviction.py` carries `SCAR_SEASON_CAP_THREAD = 1`, the closer the season
  loop dropped.
- **Falsifier run.** A ladder that discriminates would leave some persons below 3 after two seasons.
  None is.
- **Touches.** R-06 (convictions), R-07.
- **Narrative consequence.** A creed is folded or destroyed as background noise; when the dormant
  weight shift (H-187) is armed it will hit everyone at once.
- **Minimal fix.** A season cap of one count per (person, element) behind a fixture (same proposal).

### F-CHAR-05 · D · four in ten resolved acts are refusals the actor could have foreseen

- **Evidence.** Probe 2: 656 `.refused` events against 1,529 resolved acts (seed 0); 620 against
  1,519 (seed 1); `challenge`, `train`, `tell`, `transfer`, `migrate`, `exchange`, `sabotage`, `forge`
  lead at both seeds. H-346 (line 6386) found ten verbs with zero successes over 4,089 releases and
  the same with pursuits cleared.
- **Falsifier.** H-346's own: clear every pursuit; the refusals persist, so character is not the
  cause.
- **Touches.** R-05, R-08 (a refusal is not a mistake of belief; it teaches nothing), the play
  surface.
- **Minimal fix.** One person-side decline read off the row's own cell
  (`proposals/02_CHAR_offer_what_can_be_done.md`). `[UNVERIFIED: which conjunct fails for each of the
  ten; the proposal's gate measures it.]`

### F-CHAR-06 · D · the instrument's headline cannot fail

- **Evidence.** `decision_spread --season`, seed 0: distinct per-person resolved verb multisets 83 of
  83 shipped (`5ab73af2`), 83 of 83 under `--control` (`c90e4a6c`), 83 of 83 under `--null`
  (`ef134b29`). `--decisions`: distinct tops 83 shipped, 79 control, 90 null, so the all-draw arm
  scores highest.
- **Touches.** R-06's and R-08's `measure:` lines (§0.1 pt 2).
- **Minimal fix.** A temperature-0 column and the pairwise table (`02_CHAR_resolve_and_temper.md`,
  edit 4).

### F-CHAR-07 · D · a population takes an individual's acts

- **Evidence.** Probe 2, the 37 cohorts over two seasons: `create_record` 115 and 118, `challenge` 60
  and 60, `forge` 47 and 51 (seeds 0, 1). `fight`, `capture` and `accept` carry the `individual`
  conjunct (`verb_table.yaml:749-752`, `:883-886`, `:976`); it is world-only, so the person side forms
  the candidate, and `challenge`, `forge`, `sabotage`, `train`, `create_record` do not carry it.
- **Touches.** R-04 (scales), R-05.
- **Minimal fix.** `02_CHAR_offer_what_can_be_done.md`, items 4 and 5.

### F-CHAR-08 · D · two scales in one sum, one of them unbounded and signed by the wrong column

- **Evidence.** Probe 3: variance across one person's candidates, pursuit term 0.008, stance term
  1.88 where non-zero. H-339 (line 6264): rows stack past the type's bound. H-337 (line 6240) and
  H-282 (line 5552): a grudge lowers `sabotage`, `forge`, `petition`, `open_case` on its object,
  because the sign is inferred from who is contested.
- **Touches.** R-07; NERS S (*calculations consistent in methodology*).
- **Minimal fix.** A clamp at `STANCE_MAX` and a `regard_sign` column on the row whose default
  reproduces today (`02_CHAR_scar_cap_and_regard_unit.md`, item 3 and addendum).

### F-CHAR-09 · D · knowledge is partial and almost never second-hand

- **Evidence.** Probe 2: of 22,958 claims held after two seasons, 12 carry a chain, none at two hops
  (seed 0); 5 of 21,469 (seed 1). `teller_weight`'s five fixtures and `record`, `rank` (always 0,
  `options.py:1713`), stake (absent) act on that fraction. H-272 (line 5423) and H-237 (line 4955)
  record the same.
- **Touches.** R-07 (*imperfect knowledge*), R-08.
- **Narrative consequence.** Nobody acts on a rumour. A person is ignorant of much and mistaken about
  almost nothing.
- **Owner.** The telling lane (FI); cross-listed. No CHAR edit: the weighting is built and waits on
  volume.

### F-CHAR-10 · H · the score's dot product sums in set order

- **Evidence.** `choose.py:215` and `person_q.py:696-697` iterate `PURSUIT_AXES`, a frozenset;
  `person_q._lean` and `data/pursuits.py:145` iterate the sorted `_AXES`. H-362 (line 6554) measured
  no divergence on today's cells.
- **Fix.** Iterate `_AXES` (edit 3 of `02_CHAR_resolve_and_temper.md`).

### F-CHAR-11 · H · nine person-side declines keyed by verb

- **Evidence.** `decision/options.py:136-267`: `withheld_verbs`, `lie_verbs`, `OWN_STATE_STEMS`,
  `held_document_declines`, `held_edge_declines`, `own_stance_declines`, `violence_contexts`,
  `own_hold_declines`, `own_title_declines`, each a roster with a loader; the function body runs 345
  lines.
- **Fix.** One decline through one reader (`02_CHAR_offer_what_can_be_done.md`).

### F-CHAR-12 · H · Layer 1's frozen `PersonInterior` is not built

- **Evidence.** `04_CODE_ARCHITECTURE.md:171`, `:249`, `:1027` against `loop/deliberate.py:202`; no
  class of that name in `engine/`. A client's callback through `play_surface.dispatching_chooser`
  receives the live `Person`.
- **Fix.** Change the code, not the specification (§0.05): a frozen snapshot built at DELIBERATE.
  Owner: `state/carriers.py` and `loop/deliberate.py` (the CORE lane); cross-listed.

### F-CHAR-13 · H · the authored character is thinner than its loader says

- **Evidence.** `data/cast.py:4-9` counts 29 `stats`, 32 `ts`, 30 `goals`; parsed non-null values are
  1, 10 and 17 (and `lifepath` 5, `heritage` 4).
- **Fix.** Correct the docstring to non-null counts or drop the figures (§1 forbids a count in a
  pointer surface; a docstring is not one, but a wrong count is worse than none).

### F-CHAR-14 · H · condition reaches a choice only as a scene count

- **Evidence.** `budget.py`: body bands subtract scenes, floor 1. No score term reads `Sensation`.
  H-330 (line 6156): any live `hold`, a survey sheet included, earns the office bonus.
- **Fix.** `budget` counts holds on a seat, read off the grant snapshot on the person's own Tenure
  (`02_CHAR_reason_trail_and_small_edits.md` B1; `[UNVERIFIED: that a seat with an empty remit is
  stamped]`).

### F-CHAR-15 · H · stale text at the owners

- `options.py:529 project` and `choose.py:544-545`: *"thirteen conviction weights, in the four-axis
  basis"*; the basis is fifteen over seven.
- `decision/sheet.py` docstring: the design is *"PROPOSED and HELD BACK"*; the proposal's Status reads
  RATIFIED (2026-11-05, ED-IN-0349).
- `requirements.yaml` R-08 `disposition:` cites `engine/season/decision.py::make_chooser`, a path
  that no longer exists, and its `measured:` opens with two sentences later paragraphs retract.
- `proposals/2026-09-20-pursuit-basis-worksheet.yaml` says it is deleted once its values land; they
  landed (the live roster reads `doctrine` and `stewardship` where it reads `faith` and `warden`).

## 4. Code matters

- **Ownership.** Sound for the score and the ledger comparator. Doubled: the dot's summation order
  (F-CHAR-10); the person-side decline (F-CHAR-11); the scar model (`Person.scar` in the loop and a
  module-level store in `systems/characters/sim/conviction.py`, which is retained by ED-IN-0283 and
  reached only by the fieldwork oracle and two tests).
- **Dead or unreached.** `options.rank` returns 0 (declared, H-181). `refusal_tolerance` is dormant
  (`refusal_axis` None). `violated_pursuits` and `violated_affiliations` have no production caller
  (they say so). `entrenchment` is called by fixtures and a probe only. `legitimacy` and `stability`
  are read by `harness/storybar.py` alone. `beneficiary_of` has no caller outside its own module
  `[UNVERIFIED beyond a grep of non-test files]`. `pack_scenes`' `by_subject` rule orders chunks by
  subject id (`choose.py:793-797`); it is not shipped.
- **Seam fidelity.** `references/module_contracts.yaml` carries no row for the decision layer; it is
  not a registered module and is not meant to be (it is `04` §A.2's island, called by the loop). The
  two departures from Layer 1 are in F-CHAR-12.
- **Determinism.** Seeded and reproducible under `PYTHONHASHSEED=0` (the R-08 figures reproduced). The
  set-order sum is latent. `pack_scenes`, `opening_set` and `known_persons` sort.
- **Test strength.** Not run (the suite is a close step). By reading: `test_in62_decision_spread.py`
  pins the attribution to the chooser's own top, which is strong; nothing asserts that the season
  uniqueness reading can fall, which is the defect in F-CHAR-06.
- **Performance.** `opening_set` formed 45,520 candidates and asked `belief_contradicts` 98,542 times
  over two seasons; one season of 83 persons took about 9 CPU-seconds. Not a concern at this size.

## 5. Design matters

**Rulings accepted as binding, not re-raised.** ED-IN-0261 (fifteen pursuits over seven axes; *"two
people with identical pursuits ARE identically disposed"*; deontology is a refusal; scar thresholds 1,
2, 3). ED-IN-0255 (a cohort stands for a population; subsistence is territorial). ED-WR-0011 (a closed
authored cast). #353 §9.2 (capability supplies dice and gates nothing) and §9.3 (the moral layer is
moved by argument and consequence, never by evidence). CAT-3 (hearsay graded when read). AM-B-09 (aim
states narrowed to rung goals). ED-IN-0293 (organization goals). ED-IN-0304 (persons differ in risk
appetite and horizon; its residue is M40). ED-IN-0335 and ED-IN-0338 (duty of office).

**Where intent, ruling and code agree.** The person-side wall; pursuits as what a person is after;
goals as attention; regard computed at read; a closed cast.

**Where they disagree, and which the game follows.**

| subject | ruling or design | code (what the game does) | cost |
|---|---|---|---|
| scar accrual | thresholds 1/2/3; the quarantined design caps one per season | uncapped; median 41 in two seasons | the ladder is decorative and its crisis fires on noise |
| R-08 | *may not make the optimal decision based upon their knowledge and inclinations* | a realm-wide draw | met in the letter, not as character |
| `choose`'s input | a frozen `PersonInterior` (Layer 1) | the live `Person` | a client callback can write |
| deontological refusal | ruled a refusal (ED-IN-0261) | built, shipped unarmed | no person refuses anything on principle |
| ED-IN-0304 | persons differ in risk appetite and horizon | no carrier; CL-PERSON held | nobody is bold or patient |
| attributes | ten ruled (ED-IN-0328) | the carrier ships off; one row authored | capability never differs between persons |

**NERS cuts (definitions: `CLAUDE.md` §0.06; E scored last).**

- *The scar count as shipped* fails N: remove it and play differs only by the crisis noise. With the
  cap it survives; what a cut would then lose is the only multi-season pressure on a conviction.
- *The realm-wide draw* survives N (cut it and the alphabet returns as the tie-break, measured at U4)
  and fails R's half about the player feeling a person is someone. It is kept and given an owner.
- *`teller_weight`'s stack* (four gains, two absent factors) is poor on E as a ratio today, five
  fixtures over 0.05% of claims, and is not cut: CAT-3 rules the behaviour and the volume is another
  lane's defect.
- *Goals as attention only* passes S (it pauses cleanly) and fails R: no strategy can be read from an
  officer's goal because it changes nothing he does once he attends.
- *`decision/sheet.py`* passes N from the player's direction only; nothing but tests calls it, so it
  is narrowed, not established (§9).

**Design that exists only as prose and is not yet game.** Risk appetite and horizon (ED-IN-0304);
the personality layer (CL-PERSON); attributes in a choice (CR-93) and on others (CR-92); duty (CR-88);
goal stages (CL-THRUST B2.2: the loader exists, `goal_stages` is empty); the deed lie (H-198 rule ii);
intent reconciliation (H-191); threshold-1 destabilisation (no mechanism anywhere, H-187).

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Disposition

Rows marked ● were read at the register line (head, owner, default, site and the opening of `cite:`;
the longest were not read to their last character). Rows marked ○ were read at the dossier's excerpt
and checked against code or a run where the table says so. `needs_jordan` was set on none of them.

| item | listed | verified | evidence | action |
|---|---|---|---|---|
| H-03 ○ | closed? | closed | `make_chooser`'s four properties read in code; inputs person-side | none |
| H-54 ○ | open? | open (assumption) | `question_aggregation_rule` ships `first`; `questions.aggregate_questions` | none; F-CHAR-01 bears on which question matters |
| H-60 ○ | open? | closed | the player's space calls `ask_budget()` and `release` (`sheet.py`) | mark closed on the row |
| H-66 ○ | open? | open (assumption) | `--null` (uniform alignment) reads draw 488 of 498, so the table is not a zero matrix | none; the cells are Jordan's |
| H-71 ○ | closed? | closed | `options._admitted_through`, remit read off the Tenure | none |
| H-73 ● | open? | superseded | its own last sentence: deleted by REM-44; no term reads `Sensation` | read as closed; F-CHAR-14 records what replaced it (nothing) |
| H-94, H-134 ○ | closed? | closed | `operand_bags`, per-seat candidates read in code | none |
| H-96 ● | open? | open | temperature 0.05; outvoted 219 of 498 | `02_CHAR_resolve_and_temper.md` edit 5 |
| H-146 ● | open? | open, dormant | `refusal_axis` None | arm after the scar cap's reading |
| H-177/178/179/183 ○ | mixed | open, almost unreached | gains 0.5; 12 and 5 chained claims of ~22,000 | none in this lane (F-CHAR-09) |
| H-180, H-181, H-191, H-195, H-198 ○ | open?/closed? | open (absent, declared) | the `ABSENT:` markers at `options.py:1821`, `:1723`, `:1764`, `choose.py:82`, `person_q.py:1196` | none; a declared absence |
| H-187 ● | open? | open, dormant | `scar_weight_shift` 0 | arm after the cap |
| H-188 ○ | open? | open, dormant | `confliction_weight` 0 | none |
| H-189 ● | open? | open; newly measured | conviction rewritten for 0 and 6 of 46 cast (seeds 0, 1) | text edit, `02_CHAR_reason_trail_and_small_edits.md` C |
| H-190 ○ | open? | open, dormant | `intent_disclosure` 0 | none |
| H-192, H-193 ○ | open? | open; size measured | computed half median 0.051 | `02_CHAR_scar_cap_and_regard_unit.md` item 2 |
| H-194, H-202, H-255, H-256 ○ | mixed | closed as built | `declared`, gain 1, hostile 2.0, `loyalty_toward_creed` True read from fixtures | none |
| H-196, H-199, H-200 ○ | mixed | open at shipped arms | `newest`, 0.5, 0 | H-200's literal moves to a table (`02_CHAR_capability_uses_table.md`) |
| H-221 ○ | closed? | closed, rarely reached | pursuits moved for 1 and 0 of 83 | none |
| H-237 ○ | open? | premise superseded at seed 0 | 12 chained claims after two seasons | text edit (C) |
| H-239 ○ | open? | open (assumption) | gate 30 | table row (`capability_uses`) |
| H-248, H-249 ○ | open?/closed? | built, shipped on | `believed`, `on` | none |
| H-253 ○ | open? | open | `heir_hears --seeds 0 --seasons 2`: throne not vacated, control clean | none |
| H-264 ○ | open? | open; reproduced | `fight` 0 in two seasons at seed 0 | PC lane |
| H-268 ● | open? | open | not re-run | SC lane; cross-listed in §13 |
| H-272 ○ | open? | open; reproduced | 0 claims at two hops, both seeds | FI lane |
| H-283 ● | open? | open | F-CHAR-01 | `02_CHAR_goal_lean_on_its_own_question.md` |
| H-289 ● | open? | open | not re-run; the mechanism is F-CHAR-01's | same, with FA |
| H-330 ● | open? | open | `budget.py` counts every live `hold` | edit B1 |
| H-334 ● | open? | open | not re-run | answered in part by the `regard_sign` column |
| H-337, H-339 ● | open? | open | not re-run; the term read in code | scar proposal, addendum and item 3 |
| H-346 ● | open? | open; reproduced | 656 and 620 refusals | `02_CHAR_offer_what_can_be_done.md` |
| H-347 ● | open? | open | `forge` is 5 of 46 cast's score-top | none; the cells are Jordan's |
| H-357, H-358 ○ | closed? | closed as built | `lie` resolved 6 times at seed 0; `heritage_gain` 0.5 | none |
| H-362 ● | open? | open | set-order sums read in code | edit 3 of the resolve proposal |
| the other primary rows of the dossier (H-38, H-46, H-58, H-85, H-117, H-121, H-128, H-136, H-148, H-160, H-165, H-170, H-171, H-175, H-201, H-203, H-204, H-205, H-224, H-229, H-233, H-240, H-270, H-271, H-273, H-277, H-280, H-282, H-286, H-300, H-313, H-316, H-317, H-322, H-328, H-329, H-343, H-361) | as listed | `[UNVERIFIED]` | dossier excerpt only | none taken here |
| CR-88 (B10-17b) | design-first | open | plan entry read | input: goal-lean proposal |
| CR-89, CR-90, CR-91 | build / measure | open | plan entries read; not this lane's mechanism | none |
| CR-93, CR-92 (B10-19) | design-first | open | CR-93 read; CR-92 title only | temper hook and the uses table precede their builds |
| CL-PERSON | ratified design, build held | held | plan entry read | probe 1 is evidence for M35 (identical persons already differ, by the draw) |
| CL-ATTR | held on M24 | held | title only | none |

### 6.2 Inconsistencies, gaps and unclear passages: decided resolutions

| # | item | kind | decided resolution | ladder step | proposal file |
|---|---|---|---|---|---|
| 1 | scar count unbounded against a 1/2/3 ladder | inconsistency | one count per (person, element) per season, behind `scar_season_cap` | 3, 4 | `02_CHAR_scar_cap_and_regard_unit.md` |
| 2 | `regard` sums one addend in stance steps and two in raw dot products | inconsistency | each deed counted as a cosine, at most one step | 4, 3 | same |
| 3 | stance term unbounded (H-339) | gap | clamp at `STANCE_MAX` | 5 | same |
| 4 | sign of regard on non-contest adversarial rows (H-337, H-282, H-334) | unclear | a `regard_sign` column on the row; default reproduces today; values are content | 4 | same (addendum) |
| 5 | what `choice_temperature` is measured against | unclear | keep; name `person_q.resolve`; say so at the fixture and H-96 | 5 | `02_CHAR_resolve_and_temper.md` |
| 6 | the departure from the optimum belongs to nobody | gap | `temper(p)` at CR-93 (2)'s site, gain 0 | 3 | same |
| 7 | `decision_spread`'s season reading cannot fail | gap | a temperature-0 column and the pairwise table | 5 | same |
| 8 | two summation orders for one dot (H-362) | inconsistency | iterate `_AXES` | 4 | same |
| 9 | nine person-side declines keyed by verb | two owners | one decline through the own-state reader | 4, 5 | `02_CHAR_offer_what_can_be_done.md` |
| 10 | acts offered that the actor could know will be refused (H-346) | gap | decline where his own state answers `False` | 3 | same |
| 11 | a cohort forms an individual's acts | gap | the actor's `individual` answered person-side; the conjunct on eight rows | 4 | same |
| 12 | where CR-88's goal term applies | unclear | on the question the goal raised, nowhere else | 3, 5 | `02_CHAR_goal_lean_on_its_own_question.md` |
| 13 | ambition is a switch, not a weight (H-283) | gap | answered by 12 for organization goals; a person's own want stays a switch until a want carries a lean (content) | 3 | same |
| 14 | attribute names as literals under `decision/` | two owners of a mapping | one `capability_uses` table | 4 | `02_CHAR_capability_uses_table.md` |
| 15 | a fanned choice is ordered by the draw alone | gap | alignment cells on choice values | 4 | `02_CHAR_choice_alignment.md` |
| 16 | no record of why a decision was taken (H-343) | gap | an observer hook on the chooser; terms on the player's sheet; no carrier | 5 | `02_CHAR_reason_trail_and_small_edits.md` A |
| 17 | `budget` pays the office bonus for any held object (H-330) | inconsistency | count seats | 5 | same, B1 |
| 18 | `by_subject` orders scenes by subject id | gap (unshipped arm) | first appearance in the ranked list | 4 | same, B2 |
| 19 | docstrings say thirteen over four | stale | fifteen over seven | 1 | same, C |
| 20 | `sheet.py` says its design is held back | stale | ratified, ED-IN-0349 | 1 | same, C |
| 21 | `cast.py` counts keys, not values | unclear | non-null counts or none | 5 | same, C |
| 22 | R-08's `measured:` opens with retracted sentences and cites a dead path | unclear | restate the head; the residue is F-CHAR-02 | 1 | same, C |
| 23 | R-06's `measured:` says `ambitions(p)` is absent, then that it exists | unclear | restate the head; the residue is F-CHAR-01 | 1 | same, C |
| 24 | H-189 unmeasured; H-237's premise moved | stale | record this audit's readings | 1 | same, C |
| 25 | the pursuit worksheet outlived its landing and `CURRENT.md` names it as the head | inconsistency | point `CURRENT.md` at the owners; delete the worksheet with a `FORK:` row | 1 | same, C |
| 26 | Layer 1's frozen `PersonInterior` against the live `Person` | doc against code | change the code: a frozen snapshot at DELIBERATE | 3 (Layer 1 answers) | none here: `state/carriers.py` and `loop/deliberate.py` are the CORE lane's; cross-listed |
| 27 | a second scar model in `systems/characters/sim/conviction.py` | two owners | keep: retained by ED-IN-0283, unreached by the loop; its cap is item 1's precedent | 1 | none needed |
| 28 | H-73 reads `open?` in the index | stale index | closed by REM-44, by the row's own text | 1 | none needed |
| 29 | NPC-071's and NPC-034's "UNCLEAR: no goal authored" needs | wrongly stated need | not an engine need; an authoring gap in the cast (`goals:` is non-null on 17 of 46 rows) | 2 | §13 |
| 30 | `decision_policy_v1.md` listed as an NPC-chooser source | wrong referent | it is the repository's editorial precedence draft | 2 | §0A |

Thirty resolutions; twenty-five carried by a proposal file.

## 7. Research transfer

Read: `research/00_INDEX.md` (§1 and the function and verb tables), `research/by_lane/NPC_npc_cast.md`
(§0, §2.2, §2.3, §7 in full; the rest by heading), `research/emergent_narrative_literature/00_README.md`
and entry E17 of `04`. Not read: the companion parts, `game_precedent_suite/`, `rise_to_power`,
`historical/`, `governance/` (§12 lists them as skipped).

**Changes what to build.**

- **T-NPC-9, accrual without a closer runs away** (two independent sources, per the lane file).
  Confirmed in code by probe 3 (median 41). It is the reason the scar cap is the first interior edit
  and the weight shift is armed only after it.
- **T-NPC-8, tracking is not expressing** (Nemesis cut its faction display; the teardown's *"record
  only what can be surfaced"*). It sets the order in §8: a mechanism that moves an interior nobody can
  read is built after the reader that shows it (the reason trail, the terms on the sheet).
- **T-NPC-5, every mechanism that changes values, capacity or body ships at its control.** An
  independent reading that matches §2 item 7; it is why the proposals each state the live value and
  the reading rule for flipping it, not another control.
- **RimWorld, memory matters only where it is read at a decision** (the lane file's row; IN-72 was the
  tree re-learning it). It is the test F-CHAR-03 applies to regard.
- **Old World, ambitions from a person crossed with the houses around him.** Already the shape of
  IN-66 to IN-69. What it adds here is the half the plan lacks: an ambition that expires or is met.
  AM-B-09 narrowed that to rung goals, so it is noted and not re-raised.
- **E17 (Adams), Q1: every simulated variable names its player-visible effect.** Applied in §5's NERS
  cuts to the scar count and to `rank`.

**Tried and did not transfer.**

- **Triangle Strategy's hidden conviction axes.** Named once in the companion, unsourced, and its
  roster is fixed and authored; it says nothing about a sampled chooser.
- **Kremlin and John Company, holder against controller** (X1). Over-claimed convergence by the lane
  file's own grading, and the mechanism is FA's.
- **Crusader Kings council-seat denial as a grudge tag.** The tree computes regard at read and stores
  no tag; a stored tag is CR-83's question.
- **Jagged Alliance, publish a band, not the number.** Sound for a display; there is no display.

**Nulls.**

- **No file under `research/` surveys how a simulated person chooses**: a search for utility scoring,
  bounded rationality, satisficing, a temperature or risk appetite returns one line, in
  `by_lane/IN_infrastructure.md`, which records that zero literature backs the chooser's form. CR-93
  and CL-PERSON are therefore designed without precedent in the tree. That is a finding, not a
  comfort: the per-person temper and the goal lean rest on the tree's own measurements.
- **N-2, no shipped game has an expression channel for interior state** (stands, per the lane file).
  The reason trail is the tree's own answer and has no precedent to copy.
- **N-9, no NPC acts on knowingly false information** is graded CONTRADICTED by the lane file (Talk of
  the Town). In code a held claim can be stale and a lie on a cell value is built; a mistaken belief
  from hearsay is almost unreachable (F-CHAR-09).

## 8. Best path forward

Ordered. Cost class: E edit, S small build, D design-first. "Alone" is what the subsystem needs to run
well by itself; "compose" is what it needs from or gives to others.

| # | step | file | gate (an execution artifact) | unblocks | cost | alone / compose |
|---|---|---|---|---|---|---|
| 1 | the reason trail: `watch` on the chooser, terms on the sheet | `decision/choose.py`, `sheet.py`, three harnesses | hash EQUAL with and without a watcher; deciding-term counts equal through the hook | legibility for every later step | E | alone |
| 2 | instrument repair: temperature-0 column, pairwise table; `_AXES` order | `harness/decision_spread.py`, `choose.py`, `person_q.py` | under `--control` the temperature-0 column reads fewer distinct multisets than the shipped arm | R-06, R-08 measures | E | alone |
| 3 | scar season cap | `loop/resolve.py`, fixtures | median per-person maximum after four seasons ≤ 4, seeds 0–2 | R-06, R-07; H-187, H-146 can then be armed | S | alone |
| 4 | regard in stance steps; clamp; `regard_sign` column | `person_q.py`, `choose.py`, `verb_table.yaml` | median computed half ≥ 0.5 among pairs holding one; H-337's probe changes sign | R-07; CR-83, CR-88 | S | compose (SC, FA) |
| 5 | offer what can be done: one decline, cohort conjunct | `options.py`, `person_q.py`, `verb_table.yaml` | `aperture 2 0`: attempts fall and executions do not, for H-346's ten verbs | R-05, R-08; the play surface | D then S | compose (every verb owner) |
| 6 | `resolve` named; `temper` hook at gain 0; `capability_uses` table | `person_q.py`, `choose.py`, `rosters.yaml` | hash EQUAL; two hand-built persons differ only at a non-zero gain | R-08; CR-93 | E, S | alone |
| 7 | the goal's lean on its own question | `choose.py` (inside CR-88's design) | persons with one top verb across a `need` and a `claim_landed` question fall below 36 of 46 | R-06, R-04 | S | compose (FA) |
| 8 | alignment cells on choice values | `rosters.yaml`, `data/verbs.py`, `choose.py` | opposite temperaments rank two `retreat_at` values oppositely | R-04; MB orders, PC approach | S | compose (MB, PC) |
| 9 | a playable character entry point (§9) | `harness/` (a reader-shaped driver over `sheet.py`) | a scripted pick moves the hash; `take_ranked` does not | the standing requirement | S | alone |
| 10 | arm `scar_weight_shift`, then `refusal_axis` | fixtures | W-D's divergence reading moves in the ruled direction at seeds 0–2 | R-06, R-02 | E (a flip) after 3 | alone |
| 11 | the frozen `PersonInterior` | `state/carriers.py`, `loop/deliberate.py` | the G2 spy cannot be made to pass with a writing callback | AX-2 as Layer 1 states it | S | compose (CORE) |
| 12 | means and ends: a verb's declared writes against a goal's aim | `goal_stages` content, then design | an heir executes `succeed` on a vacant throne in a seeded run (H-289) | R-06, R-04 | D | compose (FA, WR) |

Deletions: the decline rosters that step 5's reading shows redundant; the pursuit worksheet; three
harness wrappers (step 1).

## 9. Playable standalone and integrated

**What exists today.**

| piece | state |
|---|---|
| entry point | none that plays. `decision/sheet.py` has the three spaces; `harness/play_surface.py` has the dispatch and the heir re-bind (`carry_on`). Their only callers are `test_g2_token.py`, `test_cr20_attributes.py` and `test_rem30_character_sheet.py` |
| fixture | `harness/headless.py::build_world` (three persons, NPC-088's season; ran here, hash `5405522c`); `populated.build_realm` (83 persons) |
| choice surface | `DevelopmentSheet.candidates`, the ranked option set, picked by index; budget shown. 39 to 43% of those options resolve as refusals (F-CHAR-05) |
| outcome legibility | `chronicle(p)`: the person's claims and present scar and conviction values. No reason for an NPC's act, no event for a scar or a crisis (the sheet's docstring says so), no terms on the options |
| stakes | a seat, a body, a larder, a record. An ambition can be laid down or die with its holder; only a rung goal can be met (AM-B-09) |
| end condition | death, then `carry_on` to a living tie, or the line extinct. No arc end and no win |
| instrument | `decision_spread`, `conviction_spread`, `heir_hears`, the tests named above |

**One code path.** Yes at the season's scale: the player's space and the NPC share `make_ranker` and
`release`, and the control (`take_ranked`) is the automated run. There is no standalone fork. The
decision layer is not a registered module and should not be one: it is `04` §A.2's island, holds no
token, and is reached by the loop's own call.

**Layer 1 conformance.** Conforms on "no `World` in scope" (path scan). Departs on the frozen
`PersonInterior` and on `View.odds` (F-CHAR-12).

**Integration.** Executed edges in §10. The scale transition this lane owns is the hand-off of a
person to a contest: it is clean in (typed inputs built by the seam wrappers from the person) and
thin out (a wound, a death, a stance row on a lost field; no scar event, no changed regard of a size
that matters).

**No GM.** Everything a referee would rule is either resolved by the engine or absent; the absences
are the survival instinct, the reading of another's intent kept or broken (H-191), and the crisis's
restabilise branch.

**Ordered work to close the gaps.** (a) §8 step 1, so a watcher can say why. (b) A harness entry
point, `python -m engine.season.harness.<name> --seat <person> --seasons N --seed S [--script file]`,
that seats one person through `creation_sheet`/`seat`, runs `development_space` with a scripted or
replayed `pick`, prints the sheet, the chronicle and the reasons each round, and exits on death with
the continuation offer; a reader over existing functions, no new rule. Gate: `take_ranked` reproduces
the automated hash; any other script moves it. (c) §8 step 5, so the options shown can succeed. (d)
§8 steps 3, 4 and 7, so that what the player does to an NPC changes what the NPC later does.

## 10. Interfaces

| edge | direction | real (executed here) or designed |
|---|---|---|
| questions: `world_q.questions_for`, `attention_key` → `assemble` | WR/CORE → CHAR | real: 774 deliberations in two seasons |
| the verb table, alignment and rosters → `opening_set`, `score_terms` | CORE (data) → CHAR | real |
| `View.odds` (believed chance) → `odds_weight` | SC (sigma seam) → CHAR | real; the tree records it reaches `determine` only in the realm |
| scenes of acts → DELIBERATE → the fold | CHAR → CORE | real: 1,529 resolved acts |
| `teller_weight`, `refracted_confidence`, `dissents` → WITNESS | CHAR → FI | real in code; reached on 12 and 5 claims |
| `standing_of`, `budget.bands_below` → `loop/matter.py` | CHAR → SE/WR | real `[UNVERIFIED by a run]` |
| `regard`, `opinion`, `legitimacy`, `stability` → `world_q`, `storybar` | CHAR → FA, instruments | real for `regard`; `legitimacy` and `stability` have one harness caller |
| the person → `PersonalCombatInput` (ends, kits, faculties, attributes, terms) | CHAR/CORE → PC | real for `end` and `faculty`; kits and attributes are empty by content |
| the person → mass battle (`fit` from a cohort's body; power and command) | CHAR → MB | real for `fit`; no officer attribute reaches a unit |
| `choice_sourced` values on an act (an order's role, `retreat_at`; `posture`) | CHAR → MB, PC | real as a fan; `marshal` is withheld; the value is chosen by the draw |
| acts at RESOLVE → `Person.scar`, `conviction`, `pursuits`, `stance`, `capability` | CORE, PC, SC → CHAR | real for `scar` and the crisis; `pursuits` 1 and 0 of 83; `stance` 0 of 83 |
| goals (`goals.yaml`) → commits at world-gen → `need` questions | FA (content) → CHAR | real: 148 commits among 46 cast |
| duty, attributes in a choice, risk appetite, a contest decider for an NPC | FA, PC, MB ↔ CHAR | designed |

**What the mass-battle intent needs from this lane.** A commander is a person holding a seat; his
orders are `choice_sourced` values on `marshal` and `march`, set through the one chooser interface by
a player or an NPC. Three things are missing: the value is unjudged (`02_CHAR_choice_alignment.md`);
the believed chance of a field by its order is not served through `View.odds`; and an officer's
attributes do not reach a unit (the registry's ten are the owner; `Person.attributes` is the carrier;
the mass-battle input must name which it reads, as the combat input does). Adjusting orders during a
battle is not the season chooser's: it is a suspension like REM-31's for a played commander, and a
module-side policy on typed input for an NPC.

## 11. Survivors for Jordan

One item survives the five-step ladder.

**Can a person be wrong about himself?** NPC-004's core need is a man with a perceptual capacity he
does not know he has and misattributes. In code a person's own state is known to him by construction:
`opening_set`'s own-state branch reasons that *"his sensitivity is not a belief about the world he can
be wrong about"*, and `OwnStateReader` answers it from the field. Not superseded; not irrelevant (it
is a `core` need of a provided case); the design documents are silent on self-knowledge as a belief;
the only precedent in the tree is the one that excludes it; and the architecture admits either.

- **Option A, own state is known (today).** Simple and already built. Self-deception, an unrecognised
  gift and a person talked into a false view of himself cannot be played; NPC-004 is simulated only
  as a gate he passes without knowing why.
- **Option B, self-knowledge is a claim like any other.** A person reads his own capacities from his
  ledger, can lack the claim, can hold a false one, and can be told. It makes NPC-004, NPC-012 (a
  motive its holder does not recognise) and NPC-021 playable as written, and it costs a second answer
  for every own-state read and a rule for how a person learns what he is.

These are different games: in A character is transparent to itself and drama is between people; in B
part of the drama is inside one.

## 12. Evidence log

All `PYTHONHASHSEED=0`, tree `601e715`. Outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/CHAR/`.

| command or probe | seed, seasons | outcome |
|---|---|---|
| `python -m engine.season.harness.conviction_spread` | none (reads the table) | 4 of 15 within 60°; 3.93 effective axes of 7 |
| `decision_spread --persons --decisions` | 0, no season | 83 persons; 11 cast pairs above 0.99; deciders draw 223, pursuit 265, stance 10; outvoted 219, median lead 0.0590 |
| `decision_spread --decisions --control` | 0 | draw 251, pursuit 247; distinct tops 79 |
| `decision_spread --decisions --null` | 0 | draw 488 (all ties), stance 10; distinct tops 90 |
| `decision_spread --season` | 0, 1 | 749 acts; 83 distinct multisets; hash `5ab73af2` |
| `decision_spread --season --control` | 0, 1 | 683 acts; 83 distinct multisets; hash `c90e4a6c` |
| `decision_spread --season --null` | 0, 1 | 583 acts; 83 distinct multisets; hash `ef134b29` |
| `decision_spread --persons --control` | 0 | every pair above 0.99, as built |
| `probe1.py` (same question, cast, with and without the draw) | 0 and 1, no season | §3 F-CHAR-02's table; control: one score-top for all 46 |
| `probe2.py` (belief filter, hearsay, refusals, interior change) | 0, 2 | hash `bacd687f`; figures in F-CHAR-03, -05, -07, -09 |
| `probe2.py` | 1, 2 | hash `8aae8412`; conviction moved for 6 of 46 cast |
| `probe3.py` (situation sensitivity, authored interior, regard, scars) | 0, 2 | 36 of 46 with one top verb; regard median 0.051; scar median maximum 41 |
| `python -m engine.season.harness.corpus_run` | 0 | 143 cases; NPC checks R1, R3, R4, R5 46 of 46; R2 not computable; 23 of 67 verbs executed; claims firsthand 93,696, told 64; 16 cases wait on a player |
| `register --requirements` | — | met 3, partial 5, not met 1 |
| `heir_hears --seeds 0 --seasons 2` | 0, 2 | 10 heir question sets; throne not vacated; control 0 |
| `headless --case NPC-088 --seasons 2 --seed 0` | 0, 2 | 16 and 17 acts; hash `5405522c` |
| registry parse (`references/npc_registry.yaml`) | — | non-null: `stats` 1, `lifepath` 5, `ts` 10, `heritage` 4, `goals` 17 of 46 |

Not run: `pytest` (by instruction); H-337's, H-268's and H-289's own probes; W-D.

**Not read, or read in part** (the reading budget ran out before the corpus did):
`.designs/` beyond `npc_behavior_v30.md` §1, §3, §4, §5.0b–§5.1, §8.1, §8.11, §9, the head of
`decision_policy_v1.md`, the head of `npc_relational_graph_v30.md`, the outline of
`player_agency_v30.md` and one line of `conviction_track_v1.md`; all of `.audit/`; the character,
attribute and template proposals beyond their Status lines (the dossier's 28), except
`2026-09-20-pursuit-basis-worksheet.yaml` (head) and the Status lines of
`2026-10-07-character-sheet-spaces.md` and `2026-09-30-character-and-play-surface/` 03, 05, 09; the
38 register rows listed in §6.1's last line; the lane handoff files; `harness/populated.py`,
`world_q.py` and `modules/combat/` beyond the passages cited; the 25 test files (named, not opened).

## 13. Provided arcs and characters — adjudication

Read: `cases/chain/CASE_BRIEF.md` in full; the 46 NPC cases' `core` needs through the repository's own
loader (`run_cases.load_cases("NPC")`: 126 core, 180 important, 40 flavour); `corpus_run` once (§12).
The ARC cases and `proposals/2026-08-30-arc-reachability/` were not read; arcs are adjudicated by the
lanes that own their mechanisms. The table holds the core needs whose mechanism is a person's
interior or choice. "Represented" means the code path is reached in a run, not that the case file
says so. Proposal files are named by their slug.

| case | need (short) | hardness | represented today? | evidence | change required | owner | proposal | gate |
|---|---|---|---|---|---|---|---|---|
| NPC-088 Carin | a season of tracked state a player can change | core | yes | `headless --case NPC-088` runs two seasons from her own choices | none | CHAR | — | the run |
| NPC-012 Rikard | an unstated motive biases every decision in one direction | core | yes | the pursuit vector enters every ranking; probe 1's Kendall by cosine | none; *unrecognised by him* is §11 | CHAR | — | probe 1 |
| NPC-012 | his employer's evaluation stays positive because of the state he prolongs | core | in mechanism, not in size | `regard` reads judged deeds; median 0.051 | regard in stance steps | CHAR | scar_cap_and_regard_unit | regard gate |
| NPC-082 Njal | loyalty attaches to a cause; a leader's self-serving conduct erodes it | core ×2 | in mechanism, not in size | creed stance rows at build; stance moved for 0 of 83 | regard in stance steps; then CR-88's grievance | CHAR, then FA | same | a seeded run in which a member's regard for his head falls by a step after witnessed deeds |
| NPC-035 Theodor | loyalty bound to one named person, not the institution | core | yes, as data | 42 of 79 cast stance rows name a person; `stance_term` reads them | none here; what happens when that person changes is CR-88 | CHAR, FA | — | probe 3 (b) |
| NPC-020 Almud | a private doubt that persists for seasons and counts | core | no | threshold 1 has no mechanism; the count passes 3 in a season | scar cap, then a reading of counts 1 and 2 | CHAR | scar_cap_and_regard_unit | cap gate |
| NPC-020, NPC-070 | an armed institution reassesses its loyalty in stages | core | no | no staged loyalty; duty unbuilt | CR-88 on regard in steps | FA | (edge: CHAR step 4 first) | CR-88's falsifier |
| NPC-021 Arne | faith privately challenged by facts, with a real chance it cracks | core | partly | `argue` moves pursuits (947 resolved in the corpus); conviction does not resist (H-268); facts may not move the moral layer (#353 §9.3) | wrongly stated as *facts*: read as argument; then H-268 | SC | — | H-268's probe |
| NPC-075 Orm | continuing unrewarded labour is a season-to-season choice; he may stop, burn out or die | core | partly | a standing question and a sampled order; no fatigue, no stopping for a reason | scar cap, then arm the weight shift (the design's route to giving up) | CHAR | scar_cap_and_regard_unit | his rate of `restore`/`work` falls after scars in a seeded run |
| NPC-002 Maret | as condition degrades the range of action narrows in a fixed order to withdrawal | core | partly | `budget` narrows scenes monotonically, floor 1 | *range of actions* is wrongly stated against #353 §9.2 (nothing gates a verb); read as the budget; withdrawal at the floor is unbuilt | CHAR, WR | — | — |
| NPC-005 Sigrid | a capability active and unknown to her institution | core | yes | `Person.thread_sensitivity` is read by its holder alone | none | CHAR, FI | — | code |
| NPC-004 Sæmund | a capacity he does not know he has | core | no | own state is known by construction | §11 | CHAR | — | — |
| NPC-008 Peder | institutional memory nobody else holds | core | yes | a held Record's content is in his ledger only (`held_record_claims`); it dies with him | none | CHAR, FI | — | code |
| NPC-089 Zoe | one governor is the decision-point among graduated postures | core | partly | a person acts through a seat; `posture` has one value; H-233 | choice alignment; more than one posture (MB content) | CHAR, MB, FA | choice_alignment | its falsifier |
| NPC-090 Stephanos | two officials' individual choices shape one relationship | core | partly | each ranks by his own vector; nothing reads the treaty when choosing | goal lean (the treaty as an office's goal) | CHAR, FA | goal_lean_on_its_own_question | its gate |
| NPC-031 Torben | the heir's relation to the regent ranges from deference to a contest for the seat | core | no | `succeed` forms and is not chosen (H-289) | §8 step 12; IN-61 | FA | (edge: CHAR step 7) | an heir executes `succeed` |
| NPC-034, NPC-071 | UNCLEAR: no goal authored | core | not an engine need | `goals` non-null on 17 of 46 registry rows | author the rows | content | — | the loader |
| NPC-086 Joren | evidence shown to an audience changes belief, and the belief spreads | core | first half | told claims deposit; none retold (0 at two hops) | FI | FI | — | H-272 |
| 16 cases (NPC-086, -075, -002, -008, -013, …) | wait on a player the engine does not supply | — | no | `corpus_run`: WAITS-ON-PLAYER 16 | the seated-person entry point (§9 (b)) | CHAR | (§8 step 9) | a scripted seat run |

Not adjudicated here: NPC-083, NPC-007, NPC-010, NPC-011, NPC-085 (settlement, faction, trade and
advocacy mechanisms; SE, FA, WR, SC).

**Arcs this lane can bring up soonest, in order.**

1. NPC-088 and NPC-012's first need run today.
2. NPC-035, NPC-005, NPC-008 are representable today as data and reads; each needs only a seeded run
   that shows the read reached.
3. After the scar cap and regard in steps: NPC-082, NPC-012's second need, NPC-020, NPC-075.
4. After the seated-person entry point: the 16 cases that wait on a player become runnable with a
   scripted seat.
5. After another lane: NPC-070 and NPC-020's institution (CR-88, FA), NPC-021 (H-268, SC), NPC-031
   (IN-61 and means-ends, FA), NPC-089 (postures, MB), NPC-086 (retelling, FI).

Dependency edges: CHAR step 4 → CR-83 and CR-88 (FA); CHAR step 7 inside CR-88's design; CHAR step 8
→ MB orders and PC approach; FI's retelling → every hearsay weight in this lane.

## 14. Capability authoring surface

### (a) Where this subsystem takes a character capability as input

| site | what it reads | from where |
|---|---|---|
| `choose.odds_weight` → `View.odds` → `seam/wrappers/pool.py::faculty` | the pool for a contested act: the larger of the vocation's attribute and the held vocation key, plus registered addends | `rosters.yaml: verb_capability`, `vocation_attribute` (and `opposed_by`); `Person.attributes`, `Person.capability`; fixture `pool_default` |
| `options.competence` (credit for a told claim) | Attunement | a literal in the module, `options.py:1627`; gain fixture 0 |
| `person_q.OwnStateReader` (the gate on `thread_read`) | Thread Sensitivity against a fixture threshold | its own `Person` field and two wired stems |
| `options.opening_set`, vocation fan (`train`) | the list of vocations | the values of `verb_capability` |
| `choose.settle_efforts` | effort, priced by believed chance | the same pool, through `View.odds` |
| `budget` | the body band, held seats, travel legs | `band_floors`; not a capability in the sheet's sense |
| `score_terms` | pursuits, affiliations, scars: the traits that weigh a choice | `descriptor_registry.yaml: pursuit_roster`, `axis_roster`, `affiliation_roster`; `rosters.yaml: tables.pursuit_projection`, `alignment`, `affiliation_engagement` |
| `data/cast.py` (world-gen) | `stats:`, `lifepath:`, `ts:`, `heritage:`, the pursuit and affiliation blocks | `references/npc_registry.yaml`; `rosters.yaml: lifepaths`, `tables.lifepath_templates` |
| `seam/wrappers/combat.py::combat_input` (the hand-off, cited for the interface) | `end` from Endurance less the body band; `faculties`; `kits` from the stores of the rungs he holds; the attributes whole | `rosters.yaml: arms_kinds`, `arms_at_build` (both empty by content); `modules/combat/attributes.py` maps by `registry_key` |

### (b) Data-driven, hard-coded or doubled

- **Data-driven and closed both ways**: verb → vocation → attribute → pool; lifepath → vocation keys;
  arms kind → combat field; the trait tables for choice. A new vocation is refused until it has an
  attribute row. This half is already the target shape.
- **Hard-coded**: the Attunement literal; `DOCTRINE_PURSUIT`, `RELIGIOUS_CONCERNS`,
  `TEMPERAMENT_AXIS` (checked names of roster members in modules).
- **Doubled**: Thread Sensitivity is a registry entry (`prac.thread_sensitivity`) and a separate
  `Person` field with its own reader. `Combatant.disp` and `faculty` are combat attributes with
  `registry_key: None` (the module's spec says so). Abilities and traditions are defined inside
  `modules/combat/ability_primitives.py` and reach no person: `PersonalCombatInput` has no field for
  them, and 22 lifepath rows record a combat ability with *"no key"*.
- **Authored and unread**: the carrier ships off (`cast_attributes=False`); one registry row holds
  `stats:`; 2 of 46 persons hold a capability key. Every capability read above is dormant in the
  shipped realm.

### (c) Target shape for this subsystem

A capability is defined once, by key, in **`references/descriptor_registry.yaml`** (the existing owner:
name, aliases, scale; attributes and practitioner stats today). What it does in a person's choice is
one row per use in **`engine/season/rosters.yaml`**: `vocation_attribute` for pools (exists) and
`capability_uses` for every other entry into a choice (`02_CHAR_capability_uses_table.md`). A
definition must say, for this subsystem to use it: its **key**; its **scale** (floor, ceiling, and so
a mid-point); for each use the **site** (a member of a closed roster of reader sites), the **form**
(`about_mid` or `at_least`) and the **gain fixture**. Growth and loss are the verb table's (`train`
writes `Person.capability`); the decision layer reads and never writes.

**The interface this subsystem needs from the merged surface.**

```
capability_factor(p, use, fx) -> float | None        # a factor about the scale's mid-point; None = none held
capability_admits(p, use, fx) -> bool | UNKNOWN       # a threshold gate on the actor's own state
View.odds(act, bands) -> float | None                 # pools and opposition, including a module's own estimate
choice_range(key) -> tuple                            # the closed set an option on an act ranges over
align_choice(key, value, axis) -> float               # how a temperament leans on a value
```

No attribute name, scale constant or pool arithmetic under `decision/`.

**Equipment and skills (personal combat).** Weapons and armour are already capability data of the
right shape: an arms kind is a matter kind, a person's kit is what his rungs store, and the roster maps
a kind to the combat field and key it sets. The content is empty, so everyone fights at the default
kit. Skills that correspond to levers exist as data inside the combat module (an ability targets a
named lever with an operator and a level) and have no route from a person. The edge this lane needs
stated for the holistic stage: a person-side carrier for invested abilities (the natural home is
`Person.capability`, whose keys are vocations today, widened by a declared key class; that is CORE's
and PC's decision), a `lifepath_templates` column that grants them, and a field on
`PersonalCombatInput`. An ability modulates a lever and does not gate a verb, so it sits inside
*"capability supplies dice and gates nothing"*; a tradition that gates ACCESS to a kit does not, and
that conflict is named and not resolved here.

**Per-phase approach (personal combat) and orders (mass battle).** The character model and chooser can
carry the OPENING approach or order today, as a `choice_sourced` value on the act, through the one
interface a player's sheet and an NPC share; they cannot yet judge it (the fan is ordered by the draw;
`02_CHAR_choice_alignment.md`). They cannot carry a per-phase choice and should not: the chooser runs
at DELIBERATE and a contest resolves inside a module. For a played person the per-turn choice is the
suspension's `decide(view)` (REM-31). For an NPC it needs a policy inside the module driven by a
person-side disposition on the typed input. That disposition has no owner: `Combatant.disp` carries no
registry key, and the ruled source for it, ED-IN-0304's risk appetite, has its carrier open at M40.
Officers and soldiers: an officer is a person with attributes and a seat; a soldier is part of a
cohort and has none. For individuals' roles and attributes to feed a unit, the mass-battle input must
declare which registry keys it reads from the commanding person, as the combat input does.

**Troop types, loadouts and a character's kit as one interface (mass battle).** The existing owner of
"an arm" is `rosters.yaml: arms_kinds`: a matter kind mapped to the combat field and key it sets, with
a rank. A character's kit is read from it (`world_q.kit_of`: the best-ranked arm his rungs store). A
unit's loadout should be the same fact at a different weight, not a second table: a troop type is a
declared bundle of `arms_kinds` members (several, for a mixed-weapon unit), and the unit's stores, like
a person's, are what its rung holds. For that to be one authoring surface the holistic stage needs
three things stated. (i) One definition of an arm, carrying what both scales read: the duel's field
and key (exists) and the unit-scale costs a carried arm imposes, as columns of the same row (its
burden toward fatigue and movement), so that carrying two arms is priced from data and a troop type
is a list of kinds, never a constant in `modules/mass_battle/config.py` (`TROOP_TYPE_ROLES` and
`ROLE_SPEC` live there today, per H-361; `[UNVERIFIED: this lane did not read that module]`). (ii) One
rule for who is a soldier: a cohort is a person at weight above one and holds no attributes, so a
troop's capability is its type's, while an officer is a person whose registry attributes and vocation
keys the mass-battle input names, as `PersonalCombatInput` names them. (iii) One formation hierarchy
whose leaves are those two things: army and unit are seats and holdings a person commands (`Act.via`),
a subformation is a `choice_sourced` assignment, and the cell is the module's. This lane's part is
(ii) and the chooser's half of (iii); the columns in (i) are MB's content on CORE's roster.

**Detective precedent (voices, held knowledge, a community's opinion).** Three capability
consequences. (i) *An internal chorus of faculties*: the tree's only per-faculty read in a choice is a
factor on a draw. A faculty that "speaks" is an observer reading of which capability's term moved a
choice or a finding, which is the reason trail's `terms` extended by the capability uses that fired;
it needs no new store. (ii) *Held knowledge as the basis of what one can cite*: already the model. A
person can say only what his ledger holds (`said_of`), act only on a held Record's content
(`held_record_claims`), and name only persons he knows (`known_persons`); what is missing is retelling
and checking (H-271, H-272; FI). (iii) *A community's changing opinion of the investigator*: `regard`
per person, and `opinion` and `legitimacy` computed at read, exist; a cohort is the community and
holds a ledger. It moves by hundredths today (F-CHAR-03); regard in stance steps is the edit that
makes it visible.

### (d) The RPG axioms this subsystem implements, lacks or contradicts

| axiom, in the tradition's words | here |
|---|---|
| attribute and skill make a dice pool | implemented, as the LARGER of the two (a default-to-attribute rule), not their sum |
| untrained use is allowed at a default | implemented (`pool_default`); nothing is trained-only |
| a prerequisite gates an ability | contradicted by ruling, except Thread Sensitivity ≥ 30 for one verb |
| opposed tests | implemented (`opposed_by`, half the opposing score) |
| advancement by training | half: `train` raises a key already held; nothing opens a new skill; attributes never advance |
| advancement by use | built and off (`practice` addend at cap 0) |
| wounds impose penalties | on the number of scenes, not on a roll or a choice |
| alignment, passions or drives steer behaviour | implemented and central (pursuits × alignment) |
| a code or vow forbids certain acts | ruled, built, unarmed (the refusal axis) |
| traits, tags, edges and flaws as discrete descriptors | lacking: `Person.marks` was dropped; heritage is the one tag |
| a personality or nerve stat (courage, composure under pressure) | lacking: no per-person manner (F-CHAR-02) |
| a character knows his own sheet | assumed; NPC-004 asks for the opposite (§11) |
| backgrounds grant starting skills | implemented (lifepath templates), authored on 5 of 46 |
| derived statistics | placeholders (`aggregates`), unwired |
| gear modifies resolution | implemented in mechanism, empty in content |

### (e) Proposals, ordered

1. `02_CHAR_capability_uses_table.md` — the table and the interface (edit).
2. `02_CHAR_resolve_and_temper.md` — Focus on the temperature, as the table's second row (edit, then
   small build with CR-93).
3. `02_CHAR_choice_alignment.md` — temperament on a closed-set option (small build).
4. `02_CHAR_reason_trail_and_small_edits.md` Part A — which terms and capabilities moved a choice
   (edit).

Not proposed here, and owed by another lane: the ability carrier and its `PersonalCombatInput` field
(PC, CORE); the registry key for a combat disposition (M40); the mass-battle input's attribute reads
(MB).
