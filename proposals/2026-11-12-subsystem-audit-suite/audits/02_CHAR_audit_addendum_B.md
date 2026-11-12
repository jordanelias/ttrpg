# CHAR — adversarial steelman audit, addendum B: the full design reading

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: ad07a9a (working tree)

This addendum does not replace `02_CHAR_audit.md`; it reads what that audit lists as NOT READ (its §12,
last paragraph) and corrects, confirms or extends it. Finding numbers continue from F-CHAR-15. Section
numbers here are the addendum's own (B1 to B7); where a section answers one of the first audit's, it
says which. `.designs/` and `.audit/` are ARCHIVED-NOT-CANON: cited below as referents for intent,
vocabulary and history, never as the reason a behaviour is correct (`CLAUDE.md` §0.05).

## B0. Verdict of the addendum

(written at the end of the reading; see the foot of this section once filled)

## B1. What was read

(appended as the reading proceeds; the final table is at the end of this section)

### B1.1 The `challenge` row, settled

The first audit's F-CHAR-07 says `challenge` does not carry the `individual` conjunct and marks the
claim as inferred. Opened at `engine/season/verb_table.yaml:923-949`: `requires_typed.all` holds three
conjuncts, `existence` of `subject` (`kind: Person`), `relation` of `subject` `with`, and `relation` of
`subject` `dispute` (v11 CR-87). There is no `individual` conjunct on either party, where `fight`
(`:749-752`), `capture` (`:883-886`) and `accept` (`:976-979`) each carry two. **The claim holds.** A
cohort is a `Person`, so `existence … kind: Person` admits it on both sides. Two things the first audit
did not have: (i) `with` and `dispute` are both WORLD-ONLY by the row's own note, so the challenger
*"forms the Candidate on anyone he knows and the fold refuses a challenge with no wrong behind it"*:
the row is itself the largest single producer of F-CHAR-05's refusals; (ii) the row's `writes_note`
states that the minted challenge Record *"reaches the challenged only by a `give`"*, `give` is
unreached in the realm (H-229), *"so in computed play a challenge mints and no `accept` forms on it"*.
The duel pair is therefore closed at both ends for a computed person: most challenges are refused, and
one that mints is never answered.

### B1.2 `.designs/` — the character, NPC and articulation sets

Paths are under `.designs/systems/`. "Full" means read to the last line; "part" names what was read.

| document | read | what it is, in one line |
|---|---|---|
| `npcs/reference/npc_behavior_v30.md` (1,266 lines) and `_infill.md` (190) | full | the Stance Triangle (Conviction, Ethical Framework, Resonant Style), per-NPC triangles and Beliefs (§2), Belief revision and Scars (§3), the advisor confidentiality boundary (§3.5), the Decision Procedure (§4), arc maps (§5), Resonant Style in a contest (§6), Framework Drift (§7), two generations of faction priority trees (§8 and a second "§7"), outreach and demand generation (§8.11), recruitment, Hooks and defection (§9.5), roster tiers (a second "§11") |
| `npcs/reference/npc_behavior_v30_index.md`, `npc_behavior_system_v1.md` and its index | headings only | section maps, and the SUPERSEDED predecessor of the above |
| `npcs/reference/npc_relational_graph_v30.md` (689) | full | PP-724: six typed NPC-to-NPC edges with strength, strain, capacity, break, rupture, inheritance, distance scaling, defection cascade; NPC-to-NPC Disposition DERIVED from edges (§4.7) |
| `npcs/reference/npc_foils_v30.md` and `_infill.md` | full | the Ruler Diamond: four axes, six pairings, each ruler's view of the other three and what each cannot see, four triangles |
| `npcs/reference/character_canon_v30.md` (447) | full | the consolidated per-NPC sheet schema (§2), the four personal axes (§7), tiers (§9), prose-feedstock dimensions (§10), and a decision log of the conflicts between the sources (§11) |
| `npcs/reference/npc_roster_v30.md` (427) | full | thirteen supporting NPCs, each with a structural compromise, a named Behavioural-AI flaw and its mechanical consequence; a mode-interface matrix |
| `npcs/reference/npc_roster_v30_infill.md` | part (design principle and entries 1 to 5) | the prose of the same |
| `npcs/reference/npc_character_analyses_v30.md`, `_infill.md` | outline, and the opening and closing entries of the infill | literary analyses with historical parallels |
| `npcs/reference/companion_specification_v30.md` (231) | full | Companion eligibility, stats, a five-row combat priority tree, mass-combat role by Disposition, departure conditions |
| `npcs/reference/edeyja_npc.md`, `baralta_v30.md` | most (Edeyja to "Player Character Access"; Baralta whole) | two individual sheets |
| `npcs/reference/npcs_flow_skeleton_v1.md`, `characters/…/characters_flow_skeleton_v1.md`, `articulation/…/articulation_flow_skeleton_v1.md` | outline and §7 (traced gaps) | traces of the retired `mc_v18` engine; history only |
| `characters/reference/conviction_taxonomy_v30.md` (358) | full | PP-684: thirteen Convictions, Self-Other orientation, structured concentration, eight cultural templates |
| `characters/reference/conviction_axis_matrix_v30.md` | full | the 13 × 4 projection with a rationale per cell |
| `characters/reference/conviction_migration_roster_v30.md` | full | PP-685: per-character primaries, template and Self-Other |
| `characters/reference/conviction_track_v1.md` | full | the scar ladder per Conviction (PP-718), the crisis table, the Thread-event scar matrix with its season cap |
| `characters/reference/conviction_track_v1_pp718_vetting.md` | head and outline | a vetting walkthrough of PP-718 |
| `characters/reference/conviction_track_v30.md`, `_index`, `_infill` | outline only | **misfiled for this lane**: it is the territory Piety Track and Church victory redesign (PP-406 to PP-418), not a character document |
| `characters/reference/character_histories_v30.md` (551) | full | the lifepath (Origin, Formation, Vocation, Catalyst): about 150 named skills with domain, effect, unique or shared, spark lists, levels 1 to 3, Recall-gated equip slots, a Knot and a Belief shape per stage |
| `characters/reference/character_histories_v30_infill.md` | head | prose of the same |
| `characters/reference/character_generation_questionnaire_v30.md` | full | creation by 12 to 16 scenario questions; "textural hooks"; names Ogre Battle, Disco Elysium, Darklands |
| `articulation/reference/articulation_layer_v30.md` (408) | full | PP-688: the protagonist lens, thirteen cut-scene triggers with a significance function, the annual chronicle |
| `_architecture/reference/player_agency_v30.md` (609) | full | Convictions as authored statements, Duties, the Scene Slate, Stature, Renown, the scene budget, Legacy and Lineage |
| `_architecture/reference/player_agency_v30_index.md`, `derived_stats_v30_index.md` | not opened | section maps of documents read in full |
| `_architecture/reference/derived_stats_v30.md` (614) | full | one attribute × one multiplier; the four buckets (derived values, tracks, clocks, pools); Inspiration; the conversion registry |
| `_architecture/reference/generational_transition_v30.md` | full | what a successor preserves, transforms, resets, breaks and transfers |

### B1.3 `.audit/` — entries that bear on persons, the narrative engine and world churn

| entry | read | what it gives this lane |
|---|---|---|
| `2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` (RATIFIED 2026-07-05, ED-IN-0011; its substrate retired by ED-IN-0232) | full | the Light Function (selection, never injection), R-AI (*"NPCs anticipate via diegetic heuristics over observable state"*, never a forecast object), the claim grammar (an argument is a move bound to a ledger object; an unbound claim is *bluster*), intent-grammar dialogue (*"players choose intents/styles, never sentences"*), the anti-slop properties |
| same directory, `integration_with_ners_audit.md` | §1 and §2 | the standing constraint that an arc-recognition surface stays internal (Jordan's veto, "Doc-12") |
| same directory, `narrative_engine_design_v1.md`, `_workings_joined.md` | outline only; not opened | — |
| `2026-08-08-world-churn-audit/00_findings.md` | full | D5 (*"zero person-scale state changes in a seeded campaign"*), D6 (the conviction gate silently no-ops), D11 (the relational graph is DOC-ONLY) |
| same directory, `03_causal_model.md` | §5 and §6 | *"there is no Scar decay anywhere … converges every long-lived NPC to permanent crisis"*; the proposed mirror, vindication |
| same directory, `06_master_synthesis.md` | Part IV P4 and P5, Part VI | Jordan, 2026-08-09: *"local actors should be NPCs"*; the do-not-build list (a world director; a unified bond primitive; an invented population count) |
| same directory, `01_plan`, `02_adversarial_review`, `04`, `05` | not opened | — |
| `2026-07-04-ners-qualitative-audit/ners_qualitative_audit_v1.md` (RATIFIED 2026-07-05) | §0 and §2 | the per-subsystem verdict on NPC behaviour: *"best dramatic legibility in the corpus; 'myriad options' under-delivered"* |
| `2026-08-11-world-schema-gap-audit/` | outline of `02_verdict_and_residuals.md` only | — |
| the other thirty entries (contest, combat, mass battle, morphology, governance, leanness, degree) | not opened | not this lane's subject |

Every finding in these entries describes the retired `mc_v18` campaign and the retired Key substrate.
Each is used below as a lead and re-verified against `engine/season/` (B2, "returning findings").

### B1.4 The 38 hole-register rows

All 38 were extracted from `engine/season/hole_register.yaml` at their `id:` lines and read to the last
character of `cite:` and `source:` (180 KB): H-38, H-46, H-58, H-85, H-117, H-121, H-128, H-136, H-148,
H-160, H-165, H-170, H-171, H-175, H-201, H-203, H-204, H-205, H-224, H-229, H-233, H-240, H-270, H-271,
H-273, H-277, H-280, H-282, H-286, H-300, H-313, H-316, H-317, H-322, H-328, H-329, H-343, H-361. Their
disposition is B6.1.

### B1.5 Proposals

| proposal | read |
|---|---|
| `2026-11-05-attribute-rulings-by-subject.md` (AR-01 to AR-58, ED-IN-0347) | full |
| `2026-11-05-attribute-rulings-adjudication.md` (ED-IN-0348) | full |
| `2026-11-05-verb-attribute-map.md` | §1, §2, the PC and NP tables of §3, §4, §5 (findings 1 to 27), §6; the eight other lane tables of §3 not read |
| `2026-11-05-verb-attribute-map_part2.md` | not opened |
| `2026-10-24-character-layers-v2.md` | full |
| `2026-10-24-character-layers-capability-ambition-values-personality.md` | §1 to §6 (to line 150) |
| `2026-10-16-character-template.md` | §0, §1, §2 (the 21-field table); §3 onward, `_part2`, `_part3` not read |
| `2026-10-16-attribute-derivation_aptitudes.md` | full |
| `2026-10-16-attribute-derivation.md`, `_part2`, `_part3`, `_divergence`, `_equivalences`; `2026-10-16-attributes-from-scratch` and parts 2 to 5 | Status lines only; superseded in their conclusion by Jordan's ten (ED-IN-0328) and the rulings of 2026-11-05 |
| `2026-09-16-conviction-decision-layer/synthesis.md` | §1 (the three fusions and the score) |
| same directory, `formal_analysis.md`, `adjudication_register.yaml`, `candidate_basis_v1.json` | Status lines only |
| `2026-09-12-emergent-narrative-primitives-v2/00_INDEX.md` | §1 (the first 60 lines); `01` to `04` Status lines only |
| `2026-09-20-pursuit-basis-worksheet.yaml` | not re-read (the first audit read its head; its values landed) |
| `2026-08-18-fieldwork-architecture-and-nonadversarial-play.md` | §2.2 P2 (the deduction-locus table) by search |

### B1.6 Research

| source | read |
|---|---|
| `research/by_lane/NPC_npc_cast.md` | §8 (missing areas) and §10 (key recommendations) in full, beyond the first audit's §0, §2.2, §2.3, §7; §1, §3 to §6, §9 not read |
| `research/game_precedent_suite/tables/R8_npc_life_economy.md` | The Sims 4 and Wildermyth rows in full; Anno 1800 and Patrician IV rows read and found not to bear on persons |
| `…/tables/R4_combat_social_rpgs.md` | the Disco Elysium block in full; the other three games' headings |
| `…/tables/R5_investigation_information.md` | the Pentiment and Disco Elysium blocks in full |
| `…/tables/R9_policy_court_sims.md` | headings only |
| `research/emergent_narrative_literature/02_…md` | entries T10 (choice poetics) and T13 (Wardrip-Fruin 2008) in full |
| `research/emergent_narrative_literature/04_…md` | entry E12 (Short on Ryan) in full; E17 was the first audit's |
| the other five parts of the literature review; `THROUGHLINES.md`; the companion parts | searched for the named games only |

### B1.7 Code, other lanes and instruments

Read: `engine/season/verb_table.yaml:923-949` and the typed conjuncts of ten rows by parse;
`rosters.yaml:1498-1632` (`verb_capability`, `vocation_attribute`, `opposed_by`, `lifepaths`) and
`:3593-3660` (`lifepath_templates`, the note and 28 of its 34 cells); `decision/choose.py:165-221`;
`decision/sheet.py:60-209`; the field lists of `Person`, `CreationRow`, `DevelopmentSheet` and `Chronicle`
by `dataclasses.fields`; `references/npc_registry.yaml` by parse; the first audit and the heads of its
seven proposals; `audits/10_DICE_audit.md` §14 and `10_DICE_audit_addendum_B.md` (head and §3); the heads
of `proposals/05_SC_evidence_and_rebuttal.md` and `05_SC_capability_surface.md`. Ran: two probes (B7).

### B1.8 Still not read

The 25 test files of the dossier (the suite's tests lane is `01_CORE_audit_addendum_C_tests.md`; this
addendum makes no claim about test strength); `registers/handoffs/` beyond a search of `HANDOFF_IN.md`
for person, chooser and attribute rows (one hit, the cohorts' decision surface, already in the first
audit); the parts marked "not opened" or "Status lines only" above. Nothing below rests on an unread
part; where a claim leans on a document read in part, the sentence says so.

## B2. Corrections to the first audit, and new findings

### B2.1 Corrections and confirmations

| # | first audit | reading here | effect |
|---|---|---|---|
| C-1 | F-CHAR-07: `challenge` lacks the `individual` conjunct (inferred) | **Confirmed** at the row and by parsing every row's `requires_typed` (B1.1). `forge` and `create_record` carry no typed conjunct at all; `sabotage` and `train` carry two, neither `individual` | the finding stands; the row's two world-only conjuncts add a cause to F-CHAR-05 |
| C-2 | §0A "prose only" lists the Stance Triangle, Belief revision, the Decision Fork, priority trees, arc maps, outreach, the relational graph's head, Duties, the Scene Slate, Stature | **Incomplete.** The design set also carries Self-Other orientation and its drift, cultural templates, the four personal axes (Thread Sensitivity, Coherence, Spirit, Truth), a named Behavioural-AI flaw with a mechanical consequence per supporting NPC, the structural compromise, typed edges with strain, capacity, inheritance and a defection cascade, roster tiers, the Companion, Inspiration, the lifepath skills, textural hooks, Renown, Legacy and Lineage | B3 restates the intent from the whole set |
| C-3 | "thirteen Convictions over four axes (`npc_behavior_v30` §1.2)" | True of the taxonomy file. The per-NPC values in `npc_behavior_v30` §2 are in the older vocabulary (Order, Reason, Autonomy, Continuity), `conviction_track_v1` §1 lists nine, and `character_canon_v30` §11 D1 records the three-way conflict as unresolved | the first audit's conclusion (no design conviction name is a key code reads) is stronger than it said: the design never had one roster |
| C-4 | the disagreement row *"one scar per season from witnessing"* against *"uncapped"*, resolved by a cap per (person, element) per season | The design's cap (`conviction_track_v1` §3) is *"Max 1 Scar per season from Thread witnessing per NPC"*: per person, not per element, and for one of two triggers; the other trigger is a Belief revised by a decisive contest won in the hearer's Resonant Style on that Belief (`npc_behavior_v30` §3.2, a triple gate). The proposed cap bounds the rate and not the stock (F-CHAR-17) | `02_CHAR_scar_cap_and_regard_unit.md` item 1 is necessary and not sufficient; amended by `02_CHAR_scar_is_a_wound.md` |
| C-5 | §7 null: no file under `research/` surveys how a simulated person chooses | Stands for the chooser's functional form. It does not stand for the chooser's legibility: `emergent_narrative_literature` carries tests the first audit did not cite (T13.Q1, the Tale-Spin effect: a decision that *"looks like a random number"*; T13.Q4: every shown trait is a decision input and nothing else moves behaviour; E12.Q2: enabling conditions stored with the event, not *"a weighted sum with no single inspectable chain"*) | they are the precedent for the reason trail, and T13.Q4 is the test F-CHAR-16 applies |
| C-6 | F-CHAR-13: the loader's counts are of keys, not values | **Confirmed** by parse (`stats` present 29, non-null 1; `ts` 32, 10; `goals` 30, 17; `lifepath` 5; `heritage` 4), and extended: six further keys are authored and read by nothing (F-CHAR-16) | — |
| C-7 | §14 (d): *"backgrounds grant starting skills: implemented (lifepath templates), authored on 5 of 46"* | True and understated. The table's own note calls itself *"A CUT, NOT A TRANSCRIPTION. Every authored dice magnitude … is DROPPED"*; by parse, of its 34 rows 21 hold nothing, 7 hold `inquiry`, 6 hold `argue`. Of the five cast rows with a lifepath, three (`3-VA1`, `3-LO3` twice) grant nothing | F-CHAR-19; B4 |
| C-8 | §11's one survivor (can a person be wrong about himself?) | Kept, and narrowed by a source the first audit had not read: `npc_roster_v30` §4 (Sæmund: *"does not know he is Thread Sensitive. He attributes his 'hunches' to investigative instinct"*) and Jordan's AR-49 (*"unaware of their impact on others (attunement)"*) both describe self-knowledge that can be wrong. The NPC research lane dropped the same item as permitted, not required (its §8.5 item 8). It remains Jordan's; this addendum adds the evidence and no new option | B6.3 |

### B2.2 Returning findings (the surviving audit corpus, re-verified against the season engine)

| earlier finding (retired engine) | now, in `engine/season/` | verdict |
|---|---|---|
| world-churn D5, 2026-08-08: *"zero person-scale state changes in a seeded campaign"*; every producer a stub; no Key reaches a person | Persons exist (83), deliberate, witness and hold ledgers; the producers are real. Stored stance moved for 0 of 83 and pursuits for 1 and 0 over two seasons (first audit, probe 2) | **Returned in a narrower form**: the edge exists and carries almost nothing. F-CHAR-03 is the same finding one engine later |
| world-churn `03_causal_model` §6: *"there is no Scar decay anywhere … converges every long-lived NPC to permanent crisis"* | True of `Person.scar` today: a count only rises, and the crisis at 3 is the one live reader | **Returned.** Measured here: F-CHAR-17 |
| world-churn D6: the scar gate silently no-ops on an unknown conviction name | Closed 2026-08-24 in the retained oracle (`characters_flow_skeleton_v1` §7 row 7); the season loop has its own writer and one roster | **False now** |
| world-churn D11: the relational graph is DOC-ONLY; "BUILT" in `npc_relational_graph_v30` §7 means design-written | Still true: no typed edge exists. `tie` and `knot` are tenure kinds with no opener in play (`rosters.yaml:130-144`); `npcs.yaml`'s `tie:` records how a concern was chosen at build (`named`, `institution`, `roof`, `neighbour`), not a relation | **Returned.** F-CHAR-18 |
| NERS audit 2026-07-04: NPC behaviour has *"best dramatic legibility in the corpus"* (priority trees and arc menus the player could read) | The trees and arcs were retired for a sampled score; nothing replaced their legibility (`Act.reads` empty, H-343) | **Reversed**: the most legible subsystem of the design is the least legible of the build |
| churn design v2 R-AI: NPCs act on observable state, never on engine forecasts | Holds by construction: `decision/` has no `World`, and believed odds are the person's own | **Holds** |

### B2.3 New findings

Numbering continues the first audit's. Severity as there: **B** blocks a requirement, **D** degrades
narrative, **H** hygiene.

#### F-CHAR-16 · D · a character is authored in more dimensions than any process reads, and the surplus is the legible part

- **Claim.** The cast registry carries six authored facts per person that no code reads, and they are
  the ones the design uses to tell one person from another: how he can be moved, where his story
  bends, what culture formed him.
- **Evidence.** Parse of `references/npc_registry.yaml` (46 rows), non-null counts: `arc_trajectory`
  36, `resonant_style` 18 (Evidence 7, Consequence 5, Solidarity 4, Authority 2), `cultural_label` 17,
  `certainty` 8, `self_other_initial` 2, `coherence` 1. `grep` of `engine/`, `modules/`, `tools/` and
  `systems/` (non-test `.py`) for each key: one hit, a comment (`data/cast.py:220`). The NPC research
  lane found three of these and proposed deleting them (K-NPC-11).
- **Falsifier.** T13.Q4 (`research/emergent_narrative_literature/02`): *"does every character trait
  the audience is shown correspond to an input to the decision process?"* Run in reverse on the data:
  a reader of any of the six would appear in the grep. None does.
- **Touches.** R-06, R-07.
- **Narrative consequence.** The facts an author wrote to make Himlensendt reachable only by evidence
  and Vossen only by solidarity sit in a file beside persons who are all moved alike by any argument
  (H-268).
- **Minimal fix.** Read or delete, key by key (B6.2 rows 3 to 6): `resonant_style` gains its reader
  (`02_CHAR_which_ground_moves_whom.md`); `arc_trajectory` stays prose and leaves the registry for
  the case file, because an arc is an observer's reading (ED-IN-0225); `cultural_label` and
  `self_other_initial` are superseded by the fifteen pursuits and are deleted; `certainty` and
  `coherence` wait on threadwork and are marked unread at the loader.

#### F-CHAR-17 · B · the scar's ladder cannot discriminate under any cap on its rate

- **Claim.** With the first audit's proposed cap of one count per (person, element) per season, every
  person in the realm reaches the terminal rung in season three, on a median of nine elements at once.
  The defect is the breadth of the trigger and the absence of an outflow, not the rate.
- **Evidence.** `probe_scar_stock.py`, `build_realm(0)`, shipped chooser, four seasons (hashes after
  seasons 1 and 2, `5ab73af2` and `bacd687f`, equal the first audit's). Seasons in which a (person,
  element) count rose, which is what the cap would leave: maximum per person 1, 2, 3, 4 after seasons
  1 to 4 for 83 of 83 persons; persons with some element at 3 or more: 0, 0, 83, 83; median elements
  at 3 or more per person: 9 after season 3, 11 after season 4; a median of 13 of 19 elements scarred
  at all. Raw counts for comparison: median maximum 25, 41, 60, 82. The writer's predicate is a sign
  test (`person_q.elements_violated_by`; H-128's cite calls it *"a CANDIDATE READING under review,
  unswept"*): any witnessed act whose alignment opposes a held element's projection, at any size.
- **Falsifier.** A ladder that discriminates leaves some persons below 3 after four seasons under the
  cap. None is left. First-order limit, stated: the reading holds decisions fixed; a capped run would
  differ where a crisis fires.
- **Touches.** R-06, R-07; the first audit's §8 step 3 and its gate (*"median per-person maximum after
  four seasons ≤ 4"* passes at exactly this reading while everyone is in crisis).
- **Narrative consequence.** A scar is meant to be the rare wound that bends a life (the design gates
  it three ways and caps it per person). As a tally of every disagreeable thing seen, it says nothing
  about anyone, and arming its readers (H-187, H-146) would move everyone together.
- **Minimal fix.** `02_CHAR_scar_is_a_wound.md`: a size floor on the violation, the cap per person,
  and an outflow.

#### F-CHAR-18 · D · the designed foils are not foils in the built realm, and no relation between two persons has a kind

- **Claim.** The pairs the design sets against each other choose alike, the pairs it allies are no
  closer than strangers, and almost none of them holds any stance toward another.
- **Evidence.** `probe_foils.py`, `build_realm(0)` and `(1)` (identical output), ten named persons,
  six common referents, temperature 0. Lenneth and Vaynard (design: *"Diagnosis Without Agreement on
  Treatment"*, build-up against tear-down) are the most alike pair of the Ruler Diamond: cosine
  +0.858, Kendall of score orders +0.819, the same top verb. Lenneth and Baralta (*"the campaign's
  defining confrontation"*): cosine +0.811, and neither holds a stance row toward the other. Baralta
  and Vaynard (*"Total Opposition"*): cosine +0.635. Of the 90 directed pairs among the ten, five hold
  a stored stance (Ehrenwall to Almud +6, Himlensendt to Vossen −4, Baralta to Himlensendt −3, Torben
  to Almud +2, Lenneth to Almud +1). Edeyja holds no stance row and no claim. Score-top verb over the
  six referents: the King `create_record` six times, the Warden-Chief `create_record` six times, the
  heir `forge` six times, the Queen and the Duke of Varfell `surveil` six times.
- **Falsifier.** If the foils were expressed, designed-opposed pairs would rank below designed-allied
  pairs on Kendall. The highest Kendall among the Diamond's six pairs belongs to an opposed pair.
- **Why.** (a) The foil axes of `npc_foils_v30` are relations to specific things (the settlement, the
  caste, the Church, the basis of authority); a pursuit vector holds general ends, and `score_terms`
  reads the verb alone (F-CHAR-01), so *"reform it"* and *"destroy it"* have nowhere to differ. (b)
  Each ruler's view of the other three (Part Two of that document) is a set of beliefs and attitudes
  about persons; world-gen seeds one loyalty row per member and no claim about anyone. (c) There is no
  typed relation: rivalry, kinship, patronage, oath and feud have no carrier.
- **Touches.** R-06, R-07, R-02.
- **Minimal fix.** Content first (the stances and the commits to opposed propositions that the foil
  document already states), on a carrier that can say what a relation is:
  `02_CHAR_relations_have_a_ground.md`. The first audit's goal lean is what lets a commit to
  *"the settlement stands"* against *"the settlement falls"* change the act chosen.

#### F-CHAR-19 · D · the design's skill is a conditional effect with a level; the build's is a key held at the default

- **Claim.** About 150 named skills in `character_histories_v30`, each with a domain, a condition, an
  effect and three levels, became three vocation keys, and the keys change no roll.
- **Evidence.** `rosters.yaml:3600-3606`: *"Every authored dice magnitude (+1D, +2D, TS +3, Ob and
  strain changes) is DROPPED … A key is held at `pool_default`, so the grant changes no pool."* By
  parse: 34 templates, 21 hold nothing. `verb_capability` has nine rows over four values (`copying`,
  `argue`, `inquiry`, `arms`). The combat module's ability primitives reach no person (first audit
  §14 (b)).
- **Touches.** R-06 (skills), R-09.
- **Minimal fix.** B4 and `02_CHAR_capability_definitions.md`.

#### F-CHAR-20 · D · nothing a person risks reaches his choice

- **Claim.** The design gives every decider a self-preservation rule (faction Stability at or below 1
  collapses any conviction to survival; a Companion at one wound from the limit goes to full guard; a
  practitioner at Coherence 5 self-limits, at 3 stops, at 2 withdraws), and Jordan rules that persons
  differ in risk appetite (ED-IN-0304) and that an opponent's emotional state colours what he does
  (AR-38). The score has no term in which a candidate's danger to its actor appears.
- **Evidence.** `decision/choose.py:193-221`: two terms, neither reads `Person.body` or the row's
  exposure. `odds_weight` multiplies a contested candidate's value by the chance of its writing
  bands, so a likely loss lowers the value of winning and never prices losing. First audit: `fight`
  resolved 0 times in two seasons at seed 0 while `challenge` was refused 84 times, so the absence is
  hidden today by formation, not supplied by judgement.
- **Falsifier.** Two persons identical but for body band 1 and band 4 would rank `fight` on one
  subject differently. By reading, they cannot: `body` enters `budget` alone (F-CHAR-14).
- **Touches.** R-08, R-06; PC's per-phase approach and MB's retreat rule (an NPC has nothing to
  choose them by).
- **Minimal fix.** `02_CHAR_what_an_act_risks.md`, an input to CL-PERSON's M40.

#### F-CHAR-21 · H · the player's development sheet shows less of his person than the creation sheet

- **Evidence.** `dataclasses.fields`: `CreationRow` carries `attributes`; `DevelopmentSheet` carries
  `capability`, `pursuits`, `stance`, `conviction`, `scar`, `body` and no `attributes`,
  `thread_sensitivity`, `heritage` or tenures (seats, oaths, commits). `Chronicle` carries the ledger
  and the scars.
- **Fix.** Add the three own fields and the person's live tenures to `DevelopmentSheet`
  (`02_CHAR_capability_definitions.md`, edit 5); a copy, as the others are.

#### F-CHAR-22 · H · three files of the dossier's character set are not character documents

- `conviction_track_v30.md`, its `_index` and `_infill` are the territory Piety Track and Church
  victory redesign (PP-406 to PP-418). The three `*_flow_skeleton_v1.md` files trace `mc_v18`, which
  is deleted. Neither is a source for a person. No edit: they are quarantined and stay; the dossier
  generator's path rule is the cause.
