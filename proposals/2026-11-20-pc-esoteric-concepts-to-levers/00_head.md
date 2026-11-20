# Personal combat: the esoteric martial concepts, tied to the engine's levers, skills and gates

## Status: PROPOSED — design reference, nothing built. Lane PC. No ID allocated. No file outside this directory is edited. **Merging this directory ratifies NOTHING**: the ED-1094 default (a merge ratifies PROPOSED content) is held back for every part; see "Held back".

---

## Verdict

**Seventy-five concepts from seven clusters, each derived from its own source to the engine quantity that plays its role, land on six live mechanisms — the read, the readiness race, the counter, one's own commitment, the bind and Concentration — and on host-side composition; only a minority are techniques at all.** Most of what the traditions call mind, stillness, fury and lightness is not a board entry: stillness and fury are **temperament** (`disp`), the unstopped mind and courage are **Concentration**, lightness and speed are **Agility**. The traditions' variety lives in **which door a school opens and which price it accepts**, far more than in which factor it sharpens.

Three findings the derivations forced, each run on the live module:

1. **The counter family is behind a door that is nearly shut.** In a closed exchange the swing room caps the commit at 4.03-4.09 against a `DEEP_COMMIT` of 4.0, so about 1% of commits (0.1-1.2% across Part 7 §7.1's cells) open the counter, the open Indes steal, the displace-and-step-inside and the lunge (Part 7 §7.1). Three levels of `mezzo_tempo` move a fight by about 0 points with the door as it is and by +1 to +4 once it can open. Workplan v12 **B15.04** already owns this ("the deep tier follows the window"); this proposal corroborates it.
2. **Concentration is the right quantity for the "mind" concepts, and it barely acts.** A defender's read after a wound is within 0.3 points of his read before it, and switching the drains off moves nothing measurable, because the reserve's effect on the read is multiplied by stamina fatigue (Part 7 §7.3). Takuan's mind stops on the first blow, fresh; the engine's only once the body tires. **PC-22**'s single Concentration function owns the fix.
3. **The engine disagrees with three claims, and the run shows it**: the still temper finishes behind the neutral one against every opponent temper tried (stillness pays its price and gets no payoff); the engine's feel in the bind is a constant that does not grow with the opponent's force (the four ounces have no lever to stand on); and the formless fighter of the wuxia novels is, in the engine, the *easiest* to read.

**The one new mechanism worth Jordan's decision is a memory within the engagement** (D-1): it alone would carry the largest family the engine cannot express — the feint, the lure, the lull and the pattern (seven rows, five clusters).

## The recommendation, ranked

| rank | proposal | part | one line |
|---|---|---|---|
| 1 | **File by derivation, not by name** | 1, 2 | a concept that lands on temperament, Concentration or an attribute is never a board entry; the board holds what lands on a lever or a gate; re-file *kiri-otoshi* from `guard_prior_parry` to the counter route |
| 2 | **Make the two landing quantities act before selling techniques on them** | 7, 8 §8.2 | the counter door (B15.04) and Concentration on a fresh body (PC-22's function); this proposal supplies the evidence to both owners and builds neither |
| 3 | **D-1: memory within an engagement** | 6, 8 | the one new mechanism; scheduled after B15.04 and B16 |
| 4 | **Vows narrow, they do not grant** | 5 | a vow is a set run backwards: it closes doors the engine offers (the decider's `withdraw`, the terms, the fighting withdrawal); the engine carries only the narrowing |
| 5 | **No charm, possession or invulnerability is ever a combat handle** | 5 | forbidden targets (agency proposal §5 Class A) with no canon carrier (P-07, P-08, P-13) |

## The counts

**75 rows** (Japan 18, Chinese philosophy 12, Chinese myth 7, Europe 15, South Asia 7, Southeast Asia and Persia 7, Africa, the Americas and the Pacific 9).

| status of the whole row | rows |
|---|---|
| EXISTS (a live lever, attribute, axis, rule or host-side composition; 8 of them flagged near-inert, door-shut or held by ruling) | 23 |
| EXISTS-PHYS (everyone's already, through physics or the contest structure) | 5 |
| NEEDS-LEVER | 5 |
| NEEDS-GATE | 1 |
| NEEDS-BEHAVIOUR | 0 |
| NO-HANDLE (6 forbidden, 1 without canon carrier, 3 where the engine models the situation differently, 1 not a fight claim, 2 outside the bout, 7 awaiting a Part 6 addition) | 20 |
| **split** (one half exists, the other does not: 17 NO-HANDLE halves, 2 NEEDS-BEHAVIOUR, 1 NEEDS-LEVER, 1 NEEDS-GATE) | 21 |

Rows run on the live module: JP-01, JP-03, JP-05, CP-04, CP-05, CP-06, CP-12 (the worked examples), CM-04, CM-07, JP-06 (discriminators), and the counter rows through §7.1's door figures. Every other choice between two nearest quantities is marked UBR in its row.

## Words used in every part (each defined once, here)

| word | means |
|---|---|
| **concept** | one idea from a research sheet, with its own source passage |
| **handle** | the engine quantity a concept's derivation lands on: a lever, an attribute, a skill axis, a gate, a state, a member of the choice set, or a host-side input |
| **the door** | the `if read_win and commit >= DEEP_COMMIT` gate at `wrapper.py:325` behind which the counter and the open Indes steal sit |
| **temperament** | the `disp` attribute (`combat_systems.py:171-174`), B18.02's `temper` slot; aggressive above 4, cautious below |
| **UBR** | "unverified by run": the choice between the two nearest quantities was argued, not measured |
| **N-1 … N-15** | the missing things of Part 6, each with the function it would hook |

Board, set, gate, lever, technique, tradition and attention are the jobs set's words (`proposals/2026-11-20-pc-tradition-jobs-growth/00_head.md`); "loadout" keeps its repo meaning (weapons and armour carried).

## What is in each part

| part | file | holds |
|---|---|---|
| 1 | `01_mapping_table.md`; `01_mapping_table_part2.md` | the 75-row table; every row's six-step derivation chain |
| 2 | `02_families.md` | sixteen families by structural role; the one mechanism of each; how traditions differ inside it; one refused name-match each; two smoothness findings |
| 3 | `03_kinds_of_strength.md` | the engine's strength-like quantities; every cluster's kinds mapped; what is missing |
| 4 | `04_stages_of_mastery.md` | every ladder in the clusters; what changes between rungs, mapped to the jobs set's growth path; what a stage unlocks and costs |
| 5 | `05_vows_taboos_ritual_fury.md` | the canon's position; each kind of obligation; vows as sets run backwards; the fury hypothesis tested |
| 6 | `06_no_handle_ledger.md` | the missing things, ranked by rows unlocked, each with its hook; NO-HANDLE rows with no addition and why |
| 7 | `07_worked_examples.md` (generated by `examples.py`); `07_worked_examples_part2.md` | stillness, yielding and the stopping mind run end to end, plus three discriminating runs; the reading of each table |
| 8 | `08_decisions_for_jordan.md` | the one escalated decision; the candidates answered without escalation, with their owners |

**Regenerate and check:** `python -I proposals/2026-11-20-pc-esoteric-concepts-to-levers/examples.py > proposals/2026-11-20-pc-esoteric-concepts-to-levers/07_worked_examples.md` (about 75 seconds; 600 keyed fights per arm; two consecutive runs produced identical tables) and `examples.py --check` (28 assertions: every technique used is live and gated to the tradition it is used with; an empty technique argument fights byte-identically to none over 20 seeds; the stub bisection recovers the neutral counter reach exactly; the drain overlay is not a no-op). The script imports `modules.combat` by its package path, adds nothing to the engine's tables, and uses one configuration overlay through `fight.fight`'s own `cfg` argument.

## What this means for the jobs set (`proposals/2026-11-20-pc-tradition-jobs-growth/`)

- **Supported by the sources:** the rule that a technique at level 6 or more costs one attention less (four ladders say drilled technique "falls away"); G-1's split of taught depth from fought breadth (four traditions say the top rung is fought, not taught); the Filipino `flow` on `tempo` (SE-06).
- **Contradicted by the derivation:** `kiriotoshi` on `guard_prior_parry` (JP-15).
- **Changed in weight by the runs:** the sets that open `counter_shallow` (S-IT-1, S-JP-1, S-ZH-1) open the only door the counter family has today; after B15.04 they open much less.

## Decisions for Jordan (detail in Part 8)

1. **D-1** Should a fight remember, within one engagement, what each fighter has done? (Recommended: yes, one per-engagement record in the orchestrator, after B15.04 and B16.)

## Held back (nothing here is ratified by merging)

Every mapping, every status, every N-addition and the one decision need Jordan's separate sign-off. The concepts are the research sheets' and carry the sheets' grades; MODERN-SYNCRETIC and POPULAR-MYTH rows are labelled so and their use as content is the jobs set's D-6. No technique, value or set is proposed.

## Reading status (stated so a reader can weigh the claims)

**Read in full:** the brief; the cross-cluster sections (recurring ideas, kinds of strength, stages, prohibitions, critical scholarship) of all seven sheets; `modules/combat/` `ability_primitives.py`, `traditions.py`, `tradition.py`, `attributes.py`, `combatant.py`, `contact.py`, `fight.py`, `wrapper.py`; `combat_systems.py` lines 1-450 and 640-1306; `state_graph.py` lines 1-135; the jobs set's parts 00, 02, 03, 04; the agency proposal §3-§5; `canon/philosophy/02_threads.md`; the P-01…P-15 table of `canon/philosophy/10_constraints.md`; the HEMA sheet §3 and §4.

**Read in part:** the sheet entries each row cites (the entry, not its neighbours; listed by line range in the receipt); `combat_systems.py` 450-640 (by grep); `core.py` 25-124 and by grep; `config.py` by grep; `weapon_physics.py` and `geometry.py` (function lists); `canon/00_philosophical_foundations.md` lines 1-240 of 472 (the file is superseded by its own banner); `sheets.py` lines 1-80 and 200-340; workplan v12 part 18 (B15.04), part 23 (B16.08 lines), part 44 (B98.26 line), part 2 (row 32).

**Not read:** `.designs/systems/threadwork/reference/threadwork_v30.md`; `repo_extract_B_morphology.md` beyond its headings; `brief_loadout_design.md` (the brief cites its Addendum 6); the sheets' "NOT FOUND" lists and every uncited entry; the jobs set's parts 01, 05-09; the agency proposal §1-§2 and §6-§23; `capabilities.py`.

**Not verified:** every row marked UBR; the provenance grade of SE-07 (taken from the sheet's cluster section, entry not read); whether B16.08's transfer at a non-zero coefficient gives the still temper its payoff (not run: the coefficient does not exist yet); any season hash (no season was run).

**Fan-out:** none. The verdicts depend on one reader holding the engine's sites and the sources' claims together; a parallel reader would have re-crawled the same 1.1 MB for each verdict, which is the reading cost §10 says not to duplicate.
