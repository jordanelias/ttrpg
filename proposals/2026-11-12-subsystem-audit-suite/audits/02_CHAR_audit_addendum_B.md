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

## B3. §0A-B — the NPC and AI-chooser intent, read from the whole design set

The first audit's §0A states the intent **as built and ruled** (I-1 to I-14). All fourteen stand and
are not restated. This section adds the other half: what the design documents say a person is and how
he should choose, each paired with its ruled successor in code, then set against `decision/`. The
design is ARCHIVED-NOT-CANON: it is cited for what was meant, and where it and the code differ the
code is what the game does.

### B3.1 What the design says a person is, and what became of each part

| the design's facet | its statement (source) | ruled or built successor | state in the build | gap |
|---|---|---|---|---|
| **Conviction**: what he takes to ground value; one to three primaries and a cultural background | *"Determines what the NPC wants to do"* (`npc_behavior_v30_infill` §1.1); structured concentration over a template (`conviction_taxonomy_v30` §4, §5) | fifteen pursuits on seven axes, all fifteen authored per person (ED-IN-0261; `data/cast.py` refuses fewer) | built, read by every ranking; 46 of 46 | none in kind |
| **Ethical Framework**: what his institution rewards | *"For officers and functionaries … this filter IS the decision"* (§4.1 step 1); a leader who departs from it pays a Leadership Deviation check | organization goals (`goals.yaml`, ED-IN-0293) and role templates (loyalty from the cosine, `data/cast.py::loyalty`); duty of office is ruled (ED-IN-0335, ED-IN-0338) | goals order attention and stop (F-CHAR-01); loyalty is one seeded stance row; duty unbuilt (CR-88) | the institution has no voice in the ranking, so it cannot disagree with the person |
| **Resonant Style**: the form of argument that reaches him | Evidence, Consequence, Authority, Solidarity; primary and secondary; a wrong style penalised; discovered by Appraise (§1.3, §6) | none | authored on 18 cast rows, read by nothing (F-CHAR-16); `argue` moves any hearer's pursuits alike (H-268) | `02_CHAR_which_ground_moves_whom.md` |
| **Beliefs**: two or three first-person commitments, *"Conviction-derived commitment + situation-specific application"* | revised only by a decisive contest, in his style, on that belief; the old belief becomes a Scar (§3.1, §3.2) | a live `commit` to an OUGHT Proposition: ambitions, creeds, goals (I-4) | 148 commits among 46 cast; the want's text is unread (H-185); only a rung goal can be met (AM-B-09) | a commit that can be broken by argument is SC's (H-268); nothing ties a scar to a belief |
| **Scars and crisis** | per conviction; 1 destabilises, 2 shifts weight and exposes a second style, 3 is crisis; rare by a triple gate and a per-person season cap (`conviction_track_v1` §2, §3) | `Person.scar` counts; thresholds ruled (ED-IN-0261); crisis built (G-Q6) | a tally of every disagreeable act seen (F-CHAR-17); two of three readers dormant | `02_CHAR_scar_is_a_wound.md` |
| **Self-Other orientation**: for whom he acts | a scalar beside the convictions, drifting with outcomes: *"the Macbeth arc … emerges from accumulated outcomes"* (`conviction_taxonomy_v30` §3) | the `selfish_selfless` axis, projected from pursuits (ED-IN-0261); `beneficiary:` on every verb row | the axis has 2 non-zero alignment cells of 45 rows (parse); `benefits_me` has no production caller (NPC research lane M-NPC-12) | whether it is built is already put to Jordan by that lane; not re-raised |
| **Temper and flaw** | every supporting NPC has *"a named flaw that produces suboptimal play and creates consequences the players can exploit"* (`npc_roster_v30`); combat `disp`; Companion priorities | risk appetite and horizon ruled (ED-IN-0304); the personality layer ratified as design, build held (CL-PERSON) | no carrier; the only departure from the best act is one realm-wide draw (F-CHAR-02) | first audit's temper hook; `02_CHAR_what_an_act_risks.md` |
| **Relations** | toward the player, Disposition −5 to +5 and Knots with strain; between NPCs, six typed edges with strength, strain, capacity, inheritance; *"Disposition is a reading of the edge graph, not separately authored"* (`npc_relational_graph_v30` §4.7) | one stance row type and `regard` computed at read, for every pair, the player included (I-9; ED-IN-0301) | the derived-not-stored principle is the same; 5 of 90 directed pairs among ten leaders hold a row; no row has a kind; `tie` and `knot` have no opener | `02_CHAR_relations_have_a_ground.md` |
| **History** | lifepath in four stages, each granting skills, a Knot, a Truth shift, a Belief shape; *"textural hooks"*: a memory, a place, a person the engine can cite later (`character_generation_questionnaire_v30` §2.1) | `lifepath:` and `heritage:` on the cast row; the ledger | 5 lifepaths, 4 heritages; a handful of seeded claims; no hook | B4; hooks are claims about one's own past and need no new carrier |
| **Capacities** | attributes 1 to 7; derived resources; Thread Sensitivity, Coherence, Spirit, Truth as independent axes (`character_canon_v30` §7) | ten attributes (ED-IN-0328); Thread Sensitivity as the one gate (#353 §9.2) | attributes carried and switched off; Thread Sensitivity on 10; Coherence and Truth have no reader | B4 |
| **What he knows and hides** | Beliefs revealed by Appraise or observation; counsel given in private and ruptured by public citation (§3.5); Hooks as leverage | the ledger, told chains, `visibility`, the lie | built; the confidence-break path is unreached (H-204) | FI and SC; cross-listed |
| **Arc** | authored maps A, B, C with branch conditions on world state (§5.2) | none, and refused: an arc is what an observer reads (ED-IN-0225; first audit) | registry `arc_trajectory` on 36 rows, unread | the branch conditions are state predicates and are usable as instrument readings (CR-90), never as rules |
| **Initiative toward others** | outreach when well disposed and concerned, demands when hostile and in authority; a leader assigns Duties (`npc_behavior_v30` §8.11; `player_agency_v30` §3) | every person runs `choose`; an act on the player is an act with the player as subject (I-1) | built in kind; the Scene Slate's successor is `questions_for` and `attention_key`'s five tiers | none in kind; volume is the question lanes' |
| **Who gets a full interior** | Active, Passive, Background tiers; non-named NPCs *"have no Conviction, no Resonant Style, no Beliefs"* (§4.2) | a closed cast of full persons and cohorts at weight above one (ED-WR-0011, ED-IN-0255) | 46 and 37; one chooser for all | none; Jordan's *"local actors should be NPCs"* (2026-08-09) is consistent with it |
| **How he is read** | a state panel per NPC (Disposition, scar count, *"next-expected-action"*); cut scenes on a scar, a knot, a revised belief; an annual chronicle (`articulation_layer_v30`, on the retired Key substrate) | `decision/sheet.py::chronicle`; the storybar | present values only; no event for a scar or a crisis; no reason (H-343) | first audit's reason trail; B5 |

### B3.2 How the design turns a person into a choice

Three generations of the design say the same thing in three forms.

1. **The Decision Procedure** (`npc_behavior_v30` §4.1, with its infill). Step 1: what does the
   institution favour. Step 2: if that agrees with his conviction, *"NPC takes it without
   hesitation"*. Step 3, the **Decision Fork**, only where they diverge: unscarred, he follows his
   conviction and his institution pays; scarred once, he follows whichever conviction the scar did
   not touch; scarred further, crisis; and if survival is at stake, survival, *"regardless of
   Conviction"*. Step 4: a contest with the player suspends the fork.
2. **The synthesis** (`2026-09-16-conviction-decision-layer/synthesis.md` §1.3, REFERENCE, its rulings
   absorbed into ED-IN-0251 and ED-IN-0261): `score = pull − cost`, the pull being what he is trying
   to reach, what he takes to be right, who it is done to and for whose good, and *"exactly one term
   carries a minus sign"*: what the act *"will take out of me"*, scaled by courage.
3. **Jordan, 2026-11-05** (AR-04, ED-IN-0347): *"these attributes capabilities are to be combined
   with pursuits convictions ambitions goals obligations demands etc to provide weighting for best
   course of actions available to that character."*

Read together they ask ten things of a chooser. Each is set against `decision/`:

| | the property the design wants | in `decision/` today | evidence |
|---|---|---|---|
| P1 | **Two oughts that can diverge.** His own and his institution's are separate inputs, and their disagreement is the drama (*"The game does not resolve this tension. The player does."* `player_agency_v30` §3.5) | one ought. A goal chooses the question and is then silent; obligations and demands have no term | F-CHAR-01; `score_terms` returns `(pursuit, stance)` |
| P2 | **Learnable, with a named way of failing.** A person is predictable in the main and errs in his own way | reversed. The order of verbs is fixed per person whatever the situation, and the departure from it is one realm-wide draw | F-CHAR-01, F-CHAR-02 |
| P3 | **Rare pressure changes him.** A wound to a conviction brings out a second self | the wound is not rare and its readers are off | F-CHAR-17 |
| P4 | **He looks after himself.** Danger to him counts against an act, by his nerve | no term | F-CHAR-20 |
| P5 | **He can be moved, in his own way, and that way must be found out** | any argument moves anyone by the same roll | F-CHAR-16; H-268 |
| P6 | **Whom an act is done to matters by what they are to him**, and breaking with them costs | regard enters the score and dominates where it is non-zero; rows are few and have no kind | F-CHAR-08, F-CHAR-18 |
| P7 | **He acts on others unprompted**, the player included | built: one chooser, one act shape | I-1 |
| P8 | **The world does not wait**: what the player leaves alone resolves by the NPC's own rule | built | first audit §1 |
| P9 | **He can be read**: what is at stake, who is acting and why, what changed | absent after the decision | H-343 |
| P10 | **He acts on what he can observe**, never on the engine's knowledge | built, structurally | I-2 |

Four of ten are built (P7, P8, P10 whole; P6 in part). The six that are not are the six that make a
person *characterful* in the brief's sense: P1, P2, P4 and P5 make two people choose differently for
reasons that are theirs; P3 lets one person become different; P9 lets anyone tell.

### B3.3 Where this reading differs from the first audit's §0A

1. **"Prose only" is too short a list and too flat a label.** Most of what §0A files there has a ruled
   successor that §0A names elsewhere without pairing: the Ethical Framework became goals, role
   templates and the ruled duty of office; Beliefs became commits; the Scene Slate became the question
   stream; Disposition and Knots became stance and regard; Duties became organization goals. B3.1 is
   the pairing. What is left with **no** successor is short and specific: Resonant Style, the ground
   of a relation, self-preservation, the flaw, and the rarity of a scar.
2. **The evidence row is refined, not reversed.** §0A sets *"presented evidence can crack a
   conviction"* against #353 §9.3 (evidence moves claims; only argument and consequence move the
   moral layer). Read whole, the Evidence style is a fact about the **hearer**: which support an
   argument needs before it reaches him. It survives the ruling as an advantage on `argue`, whose
   effect is still the only mover. The conflict with the ruling is named in the proposal and is
   absent on this reading.
3. **§0A's list of what an NPC needs to be characterful is score-side** (situation, temper, a moving
   interior, a reason). The design's own list is longer by three that are person-side data and one
   that is a rule: a susceptibility, relations with a ground, an appetite for risk, and a wound that
   is rare. They are P5, P6, P4 and P3.
4. **The arc row gains a use.** §0A says an NPC rule keyed on an arc stage is scripting drift, and
   that stands. The arc maps' branch conditions (*"Almud's Truth reaches 1 or 0 AND Löwenritter
   Autonomy = Loyal"*) are predicates over state; as readings of an instrument they are the designed
   answer to "did this run produce the story the authors hoped was possible", which is CR-90's job.
5. **The legibility loss is larger than §0A's "only the occasion survives".** The ratified 2026-07-04
   audit judged NPC behaviour the most legible part of the design, because a priority tree and an
   arc menu can be read off a page. Replacing them with a sampled score was right for emergence
   (P8, P10) and removed the one property the design had in full. The reason trail is therefore not
   a convenience: it is the replacement for something deliberately given up.

### B3.4 The intent, in the form other lanes can cite

**A person in Valoria has ends (pursuits), allegiances he has committed to and offices he holds,
relations to particular people each with a ground, a history that left him capacities and a few
beliefs about named others, a temper (how much danger he will accept and how steadily he keeps to his
best judgement), a particular way of being moved by others, and wounds that are few and that change
him. A chooser must (1) rank acts by his ends and by his institution's, as separate terms, so that
their divergence can be seen and paid for; (2) weigh the person an act is done to by what that person
is to him; (3) count what an act risks to himself, by his appetite; (4) depart from his own best by
his own steadiness and nobody else's; (5) change his ends only by a rare wound or by an argument of
the kind that reaches him; and (6) leave, for every choice, a reason a reader can follow. He reads
only what he holds (I-2), and the player is a person of the same kind whose choices come from outside
(I-1).** Items (1), (4) and (6) are the first audit's proposals; (2), (3) and (5) are this
addendum's. Nothing in it needs a second chooser, a name in a branch, or a stored opinion.

### B3.5 What each lane should take from it

| lane | what the reading asks of its NPC-facing surface |
|---|---|
| SC | a contest input for the hearer's susceptibility, fed by what was cited (its SC-P8) and by who is speaking; a result that can depend on the hearer and not only on the pools |
| PC, MB | the opening approach and the standing order are chosen by the same appetite that prices any dangerous act; inside a bout, the module's default policy takes that appetite as typed input (the first audit's §14; `Combatant.disp` has no registry key) |
| FA | duty as a second term in the ranking (CR-88), not a decline, so that an officer can act against his office and be seen to |
| FI | a finding about a person's susceptibility or relations is a claim like any other and is what "learning how to reach him" consists of |
| WR | arc branch conditions as readings (CR-90); a scar and a crisis as Events an observer can list |
| GO | the person panel of the design (relations, wounds, the reason for the last act) is the reason trail and the sheet, not a new model |
