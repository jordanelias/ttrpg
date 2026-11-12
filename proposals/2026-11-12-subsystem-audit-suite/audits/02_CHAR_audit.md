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
  persons at seed 0 and 0 of 83 at seed 1; pursuits for 1 and 0; `fight` 0, `forgive` 0. Probe 3:
  regard differs from stored stance in 656 of 2,070 cast pairs, with a median computed half of 0.051
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
- **Fix.** `budget` counts holds whose object is an office (the person's own `granted_acts` snapshot
  is non-empty), an edit at the owner.

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

<!-- part two follows -->
