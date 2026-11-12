# CHAR — adversarial steelman audit, addendum B: the full design reading

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: ad07a9a (working tree)

This addendum does not replace `02_CHAR_audit.md`; it reads what that audit lists as NOT READ (its §12,
last paragraph) and corrects, confirms or extends it. Finding numbers continue from F-CHAR-15. Section
numbers here are the addendum's own (B1 to B7); where a section answers one of the first audit's, it
says which. `.designs/` and `.audit/` are ARCHIVED-NOT-CANON: cited below as referents for intent,
vocabulary and history, never as the reason a behaviour is correct (`CLAUDE.md` §0.05).

## B0. Verdict of the addendum

The first audit's verdict stands, and its account of the intent is half of the intent. Read whole, the
design set says a person is ends, allegiances, relations with a ground, a history, a temper, a
particular way of being moved, and a few wounds, and asks ten things of a chooser; four are built and
the six that are not are the ones that make two people differ for reasons that are theirs (B3.2). The
single largest obstacle the first audit named (the ranking reads the verb and nothing else) is
confirmed from the design's side by a probe it did not run: the foils the design sets against each
other choose alike, and the pair it calls opposed in method is the most alike of the four rulers
(F-CHAR-18). Three things the first audit could not see without the design: the cast registry already
authors, on eighteen persons, the fact that should make each of them reachable in a different way,
and nothing reads it (F-CHAR-16); the first audit's own scar cap leaves every person in crisis by the
third season, because the trigger is a tally where the design had a rare wound (F-CHAR-17, measured at
two seeds); and four in five of the designed skill effects are specialisations that the DICE lane's
capability map can carry as rows once their conditions are keys (B4 (b)). The `challenge` claim is
settled: the row has no `individual` conjunct (B1.1). One survivor for Jordan, unchanged. Six
proposals; twenty-four resolutions.

## B1. What was read

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

**Completion (Opus, after the Fable lane stopped).** The Fable lane had written B0 to B7 and five of
the six proposals; `02_CHAR_voices_and_the_room.md`, which B5 and B6.2 rows 19 and 20 cite, did not
exist. The completion read, for it: `decision/choose.py:56-221` (`stance_term`, `deliberation_memo`,
`odds_weight`, `score_terms`), `decision/options.py:529-565` (`project`), `data/pursuits.py:60-85`
(`to_axes`), `queries/person_q.py:424-453` (`regard`) and `:620-634` (`opinion`), the callers of
`opinion`, `legitimacy` and `stability` by search, `queries/world_q.py:4374-4396` (`witnessed`),
`state/carriers.py:600-690` (`Scene`, `Act`), `decision/sheet.py:150-210`, the first audit's
detective paragraph (§14 (c)) and `02_CHAR_reason_trail_and_small_edits.md`; and ran one probe (B7).
It read nothing further from the list above, re-ran none of the Fable lane's probes, and found no
earlier statement to correct. The rows still not read stay not read.

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
  36, `resonant_style` 18 (Evidence 7, Consequence 5, Solidarity 4, Authority 2), `cultural_label` 43
  (17 at the row's top level, 26 inside its `convictions:` block), `self_other_initial` 28 (2 and
  26), `certainty` 8, `coherence` 1. `grep` of `engine/`, `modules/`, `tools/` and `systems/`
  (non-test `.py`) for each key: one hit, the loader's own comment where it steps over the two nested
  keys by name (`data/cast.py:220`). The NPC research
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
  at all. Raw counts for comparison: median maximum 25, 41, 60, 82. Seed 1 reads the same shape (82
  of 82 living persons at 3 or more in season three, on a median of 11 elements; season-two hash
  `8aae8412`, the first audit's). The writer's predicate is a sign
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
  bands, so a likely loss lowers the value of winning and never prices losing; and for the rows that
  contest the body or a field the believed-chance query answers `None` (their bands are the combat
  module's and the field's, which `seam/wrappers/sigma.py::believed_chance` does not speak for), so
  a fight is weighed with no odds at all. First audit: `fight`
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

## B4. §14-B — the character sheet and capability authoring, with `derived_stats_v30` and the attribute proposals

**The map is the DICE lane's and is not redone here.** `proposals/10_DICE_capability_axiom_map.md`
(written during this lane; read to its §F) fixes ten roles a capability may play, each one RPG axiom
feeding one resolver input (`dice`, `addend`, `opposes`, `edge`, `circumstance`, `resource`,
`threshold`, `rate`, `judgement`, `gate`), one definition row (`capabilities`: `kind`, `base`,
`opposed_by`, `scale`, `untrained`, `grows_by`) and one uses table (`capability_uses`, which is the
first CHAR lane's table with a `role` column). `proposals/01_CORE_capability_authoring_surface.md`
proposes the same row in `references/descriptor_registry.yaml` and a `capability:` column on the verb
row; the two differ only in the file, which the DICE map leaves to the holistic stage. This lane takes
no third position on the file. What follows is the character's side of that surface: what the design
and Jordan's rulings require a definition to say that the row does not yet carry, which designed
capabilities fit the ten roles, and the choice-side rows this lane owns.

### (a) Further places a capability enters or is shown (beyond the first audit's §14 (a))

| site | reads | from | data or code |
|---|---|---|---|
| `decision/sheet.py::CreationRow` | `capability`, `pursuits`, `conviction`, `attributes` | the `Person` | a copy; no definition is shown, only keys and numbers |
| `decision/sheet.py::DevelopmentSheet` | `capability`, `pursuits`, `stance`, `conviction`, `scar`, `body` | the `Person` | omits `attributes`, `thread_sensitivity`, `heritage`, tenures (F-CHAR-21; CORE's edit 6 adds `attributes`) |
| `data/cast.py::capability_of` | `lifepath:` expanded through `tables.lifepath_templates` | `references/npc_registry.yaml`, `rosters.yaml` | data; a grant is the key at `pool_default`, so it changes no pool (`rosters.yaml:3600-3606`) |
| `data/cast.py::attributes_of`, `thread_sensitivity_of`, `heritage_of` | `stats:`, `ts:`, `heritage:` | the registry | data; 1, 10 and 4 rows |
| nothing | `resonant_style`, `cultural_label`, `self_other_initial`, `certainty`, `coherence` | the registry | authored, unread (F-CHAR-16) |

### (b) What the design defines, and how much of it the map's roles can carry

`derived_stats_v30` §14 sorts every number on a character into four buckets. Each has a home on the
map or outside it:

| the design's bucket | its members | on the map | state |
|---|---|---|---|
| **Pools** (dice computed at action time) | Combat, Argue, Thread, Fieldwork, Knot: *(primary × 2) + History + 3* | `dice`, `addend` | superseded by ruling: the score is the pool, attribute or skill whichever is higher (CR-20); History eliminated (ED-IN-0330) |
| **Derived values** (attribute × multiplier, drain and refill) | Health, Stamina, Composure, Concentration, Thread Fatigue, the Inspiration cap | `resource` | Health and Stamina live inside the combat module per scene (`combatant.py`); `Person.body` is the season's one drained value; Composure, Concentration (outside a fight), Thread Fatigue and Inspiration have no carrier |
| **Tracks** (bounded counters of relation, character and perception) | Disposition, Truth, Coherence, Thread Sensitivity, Renown, Standing | not capabilities | Disposition is stance and regard; Thread Sensitivity is the one `gate`; Renown and Standing are computed readings (`opinion`, `legitimacy`, seats); Truth and Coherence unbuilt |
| **Clocks** | world and scene progress | not a character's | WR and FA |

The lifepath's skills are the design's capability content. A count of effect forms over the 106
skill-bearing table rows of `character_histories_v30` (a regular-expression count over the archived
text, a reading aid and not a census; B7):

| effect form in the design | occurrences | the map's role for it | expressible as a row? |
|---|---|---|---|
| bonus dice under a condition (*"+1D in formal proceedings"*) | 83 | `edge` with a `when` (a specialisation is advantage, a named level; a flat die is not the ruled form) | yes, once the `when` key for the condition exists |
| a changed target number (*"TN 6 instead of TN 7"*) | 7 | none: excluded by ruling (ED-IN-0196) | re-expressed as `edge` |
| an obstacle moved (*"−1 Ob"*, *"+1 Ob once per contest"*) | 11 | `circumstance` when it is the other side's or the situation's; an actor lowering his own obstacle is excluded | partly |
| an immunity (*"immune to the first Rattled mark"*) | 13 | `circumstance` with a negative gain against one named term (the map's AR-44 row) | yes for terms that exist; most of the named conditions (Rattled, Doubt, Morale) have no carrier |
| a strain or resource size (*"Stamina base +1"*, *"−1 strain"*) | 13 | `resource` | not yet: a `resource` row is keyed by an attribute and has no amount for a held trait |
| a limited use (*"once per arc"*) | 6 | none | no: there is no counter for a spent ability; the built analogue of a spend is `effort` |
| a new action or an automatic result (*"switch weapon between exchanges"*) | 9 | none in the season (*capability gates nothing*); inside a fight, a lever | combat abilities are the module's; see (c) |
| a Thread Sensitivity grant | 2 | a cast-row value | yes (`ts:`) |

So roughly four in five of the designed effects are specialisations, and the map carries them by
data once the conditions they name are `when` keys. The lifepath table cut all of them (C-7) because
no such door existed when it was written.

### (c) What a definition must carry, by kind

The exact fields, the tradition's name for each, and their owner on the map. Fields marked **new**
are this lane's additions to the DICE row or its `when` keys; everything else is the map's.

| field | skill | ability | aptitude | trait | the tradition's word | owner and reader |
|---|---|---|---|---|---|---|
| `id` | ✓ | ✓ | ✓ | ✓ | the name on the sheet's left column | `capabilities` row key; the key of `Person.capability` |
| `kind` | `skill` | `trait` or `aptitude` (below) | `aptitude` | `trait` | skill; talent or feat; knack; edge or flaw | the row; the loader refuses a `dice` use of a trait |
| `gloss` **new** | ✓ | ✓ | ✓ | ✓ | the rulebook's one-line description | the row; read by `decision/sheet.py` and the reason trail; refused if empty. Without it a sheet can list `copying: 3` and cannot say what copying is |
| `base` | ✓ | — | optional | — | the governing attribute | the row; `pool.py` |
| `opposed_by` | optional | — | — | — | the resisting attribute | the row; `pool.py::_opposing_attribute` |
| `scale` | 0 to 7 | 0 to 1, or ranks | ranks | 0 to 1 | rating; ranks; has it or not | the row; `data/cast.py`, `_eff_train` |
| `untrained` | `default` or `attribute` | `none` | `none` | `none` | unskilled use | the row; `pool.py::score` |
| `grows_by` | `train`, `practice`, `use` | `fixed` | `train` or a derived rule | `fixed` | advancement by training, by use; a fixed advantage | the row; `_eff_train`, `world_q.practice`, `_grown` |
| which verbs test it | ✓ | — | — | — | *"roll X for …"* | `verb_capability` (or CORE's column) |
| a use row: `use`, `role`, `key`, `side` | implied by the verb | ✓ | ✓ | ✓ | what it does | `capability_uses`; one reader per site |
| `when` | — | ✓ | ✓ | ✓ | *"… when fighting in the dark"*: the specialisation's condition | `capability_uses`; closed keys |
| `when.rank_at_least` **new** | — | ✓ | ✓ | — | a skill's level unlocking a better effect (the design's levels 1, 2, 3) | a `when` key; one comparison in the uses reader |
| `level`, `per`, `against` | — | ✓ | ✓ | ✓ | advantage or disadvantage, and how much | `capability_uses`; `sigma.py::advantage_sigma` |
| `gain` | — | ✓ | ✓ | ✓ | the size of a situational modifier | a fixture named on the row |
| granted by | reverse index | reverse index | reverse index | reverse index | background, school, heritage | not authored on the row: read off the bundle tables that list the id (`tables.lifepath_templates`; a tradition's bundle, AR-43a) |
| held by | ✓ | ✓ | ✓ | ✓ | the number on the sheet | `Person.capability` from the cast row's `capabilities:` (CORE's edit 5) or a bundle |

**An ability** in the tradition is a discrete trained manoeuvre: held or not, sometimes ranked, and
it changes one thing in one kind of scene. On the map it is not a fifth kind. It is a `trait` (or an
`aptitude` where it has ranks) whose use row names the scene's site. For a social or inquiry scene
that is an `edge` or `circumstance` row and is expressible today. For a fight it is a row whose target
is one of the combat module's levers, and that roster lives inside `modules/combat/ability_primitives.py`
and is not exported; until it is (the PC lane's `03_PC_person_inputs_content.md`, by title; not read),
a combat ability cannot be authored as data. That is the one kind the brief names that the surface
does not yet carry, and the gap is the export, not the row.

**What a definition must not say** (each excluded by a ruling the map already lists): a flat bonus to
the net, a changed target number, an actor lowering his own obstacle, a requirement to attempt. And
one this lane adds from the design side: **a loss rule.** The design keeps every learned skill
permanently and the rulings are silent, so `grows_by` has no opposite; a capability ends with its
holder. A designer who wants a skill to fade wants a new growth rule, which is code and a decision.

### (d) The choice-side rows (this lane's content on the map)

| use site | role | key | what it is, in the tradition's words | state |
|---|---|---|---|---|
| `told_claim_credit` | `judgement` | Attunement (persons), Reason (offices), Perception (facts): ED-IN-0326, AR-24 to AR-26a | insight: whose word to credit | one row built at gain 0; the split by matter is CR-83's design |
| `choice_temper` | `judgement` | Focus (AR-23) | composure in deciding: how often he strays from his own best | first audit's `02_CHAR_resolve_and_temper.md` |
| `choice_exposure` **new site** | `judgement` | Spirit as nerve (adjudication §2.2 (iv)), or a trait | courage: how much a danger to himself weighs | `02_CHAR_what_an_act_risks.md`; gain 0 |
| `social_roll` | `edge`, `side: subject` | four susceptibility traits | what kind of appeal reaches him | `02_CHAR_which_ground_moves_whom.md` |
| not a capability | — | appetite for risk and time horizon (ED-IN-0304), the six manner offsets of the personality layer | temperament | CL-PERSON; these pass the layer test *"no pole always wins"* and so are personality, not capability, and do not belong in `capabilities` |

### (e) The character-sheet axioms, in the tradition's vocabulary

The DICE map's §A names the axioms of the roll. These are the axioms of the sheet, with the state of
each (the first audit's §14 (d) rows are not repeated):

| axiom | here | source |
|---|---|---|
| attributes are few, innate and bounded | ten, 1 to 7, floor 1; fixed in play | ED-IN-0328; AR-05 |
| a skill sits on one attribute | one `base` per skill; no second pool attribute | adjudication §3.1 item 11 |
| a specialisation is a narrow bonus on a skill | `edge` under a `when`; none authored | the map §E |
| a background is a package | a lifepath grants ids; today at the default rank, changing no roll | C-7 |
| a school is a package of manoeuvres | *"martial traditions are also bundles of skills"* (AR-43a); the bundle is inside the combat module | PC |
| familiarity is knowledge of a matchup, earned | *"grown outside the subsystem, fixed when the subsystem uses it"* (AR-45 to AR-48); derived from the holder's own past fights, on `world_q.practice`'s precedent | adjudication §2.2 (viii); unbuilt |
| derived statistics follow from attributes by one written rule | one attribute, one multiplier, exceptions named (`derived_stats_v30` §1) | built inside combat only |
| a wound is a penalty on the difficulty, not a lost die | a fractional obstacle term per wound (ED-PC-0005) | the map's `circumstance`; first audit: wounds cost scenes only |
| willpower can be spent | the design's Inspiration and Momentum; the built spend is `effort` | DICE |
| a flaw is a trait that costs its holder under a condition | an `edge` row with `against: true` on the holder, or a `judgement` row at a choice site | expressible; none authored |
| a drive or passion steers and is not a skill | pursuits | I-3 |
| a bond is a relation, not a stat | stance and regard; Bonds was dropped from the ten | ED-IN-0328; B3 |
| reputation is what others hold, never a number on the sheet | `regard`, `opinion`, `legitimacy`, computed at read | I-9 |
| a character knows his own sheet | assumed | first audit §11; B6.3 |
| a prerequisite gates a power | Thread Sensitivity only | #353 §9.2; whether any other may is CORE's held question |

### (f) Proposals, ordered

1. `10_DICE_capability_axiom_map.md` and `01_CORE_capability_authoring_surface.md` (theirs): the row,
   the roles, the uses table.
2. `02_CHAR_capability_definitions.md` (this lane): `gloss`, `rank_at_least`, the registry's unread
   keys read or removed, the sheet's missing fields.
3. `02_CHAR_which_ground_moves_whom.md`: the first trait rows with a reader.
4. `02_CHAR_what_an_act_risks.md`: the `choice_exposure` site.
5. The first audit's `02_CHAR_capability_uses_table.md` and `02_CHAR_resolve_and_temper.md`, unchanged
   (the map adopts both).

## B5. Internal voices and a community's opinion (the detective and noir precedent)

**What the sources say, read.** `character_generation_questionnaire_v30` §1 names Disco Elysium for
*"24 skills as voiced inner life … Personality is surfaced through inner voices, not stat labels"* and
draws from it: *"Convictions gate REACTIONS (DE-derived interior gate). Histories gate ACTIONS."* Its
open item 6 asks that *"the voice intrusion should reference the hook that produced the Conviction
weight"*. `player_agency_v30` §1.3 takes from the same game the scene as *"interpretive invitation"*
and §1.6 takes from Pentiment *"investigation as social act with social cost"*: asking changes what
people think you are doing, and time is finite. The fieldwork architecture proposal (§2.2) places
Disco Elysium at the *character* end of the deduction locus: *"Skills are interlocutors that
interpret for you — and can be wrong."* The precedent tables add what the shipped games do
(`R4`, `R5`): a passive check has no dice (skill + 6 against a difficulty) and decides only *whether
a line appears*; high skill has drawbacks; the Thought Cabinet is an ideology taken on over time for a
standing modifier; one companion's opinion is a hidden count; in Pentiment persuasion is a
deterministic threshold over prior choices and background, *"This will be remembered"* flags make
later people react, and the world answers the accusation, not the truth.

**Is the precedent understood or only named?** Named, with one exception. The design documents use
Disco Elysium for a creation interface and a slate of scenes, not for a mechanism by which a faculty
speaks; no document specifies what a voice is. Pentiment is understood: its two properties (asking
costs standing; time is short) are exactly `regard` moved by witnessed conduct and the scene budget,
both built.

**What the engine already has that the voices need.** Three things, none built for the purpose:

| the precedent's part | the engine's existing quantity | what is missing |
|---|---|---|
| a faculty that notices (a passive check: no dice, a threshold on a rating) | the `gate` and `judgement` roles read a rating against a mid-point or a floor with no draw (`capability_factor`, `capability_admits`); Perception at WITNESS is the ruled site (AR-24 to AR-26a; CR-83) | the reading is not attributed: a claim does not say which of the holder's faculties let him hold it |
| competing voices arguing over what to do | the score's terms. A person's ranking is already a sum of separately computed pulls (his ends; his regard for the subject; with the proposals, his office's goal, the risk to himself) that can and do disagree | the disagreement is discarded when the terms are added; `Act.reads` is empty |
| a voice that can be wrong | refraction and hearsay weighting make a held claim differ from the truth by channel, teller and prior (AX-7); believed odds are his own | which faculty misled him is not recorded |
| a voice with a history (*"reference the hook"*) | a pursuit's weight, a scar count on an element, a held claim about his own past | no link from a term to the scar or claim behind it |
| a community's opinion of the investigator, moved by each conversation | `regard` per person and `opinion`, `legitimacy` computed at read; a cohort is the community and holds a ledger | it moves by hundredths (F-CHAR-03); nothing shows it to the person it is about |
| time is finite | the scene budget (I-7) | built |

**The implication.** An internal voice is not a new subsystem and not a 24-skill roster. It is a
**reading of the terms of one person's own choice**, attributed: each term of the score and each
capability use that fired has an owner (a pursuit, an allegiance, a regard for someone, a fear, a
faculty), and a voice is that owner speaking for or against a candidate with the size of its pull.
The dissenting voice is the largest term that pointed away from the act taken. The voice that was
wrong is the capability use behind a belief the fold later contradicted. A community's opinion is the
same construction turned outward: the regard of the persons present for the one acting, summed by
ground, and its change since the last scene. Both are observers (ED-IN-0225): they read the reason
trail the first audit proposed and store nothing. `02_CHAR_voices_and_the_room.md` specifies them.

**What this asks of the other lanes** (the brief's questions, from the character's side): for SC,
that a contest report which faculty and which susceptibility carried it, so the hearer's inner
reading can be shown (*"the document reached him; the appeal to his oath did not"*); for FI, that a
finding name the faculty that surfaced it and that a missed finding be recordable as missed, because
a voice that stays silent is half of Disco Elysium's effect and the engine today cannot say what a
person failed to notice; for GO, that the surface show terms and not totals.

**Nulls, marked.** No shipped game in the tables attributes an NPC's choice to competing faculties;
Disco Elysium does it for one authored protagonist with about ten thousand hand-written passive
checks (`R4`). A generated voice from a score term is the tree's own construction and has no
precedent to lean on. And the Tale-Spin effect (C-5) cuts both ways: showing every term of every
choice is a debugging console, not a voice. The reading must select (the largest pull against, the
one that changed since last time), which is a curation rule and is specified as one.

## B6. Dispositions and resolutions

### B6.1 The 38 hole-register rows

Status "as the row states" means read in full and not re-run; "verified" names the code or run.

| row | listed | status after reading | basis | action |
|---|---|---|---|---|
| H-38 | closed? | closed as corrected: `Person.body` is banded for the budget only; no verb gate | the row's own 2026-10-26 correction; `budget.py::body_band_penalty` | none; F-CHAR-20 is the missing second reader |
| H-46 | closed? | closed by supersession (ED-IN-0261) | fifteen over seven in code (first audit's `conviction_spread`) | the row's last sentence (*"`rosters.yaml` still carries the OLD thirteen"*) is stale; text edit |
| H-58 | open? | open: `exchange` built, executes 0 in the realm | as the row states (127 attempted, 127 refused); fixture `default_return_kind` reads `salt` | SE and FA; an instance of F-CHAR-05 |
| H-85 | open? | half closed: the verb gate is built (verified: `thread_sensitivity_gate` 30; ten cast values); the knowledge-kind gate is not | row and fixtures | none here; FI |
| H-117 | open? | superseded in its headline by its own cite: the budget binds at 5 slots and not at the shipped 15 (`scene_budget` 5 × `interactions_per_scene` 3, verified) | the row | none; a person's triage is real only where the budget is narrowed |
| H-121 | — | open (assumption): `default_store_kind` `grain`, verified | fixtures | SE |
| H-128 | open? | open (assumption): the actor is scarred by his own act at the shipped arm | the row; its sweep counts 260 against 241 | answered inside `02_CHAR_scar_is_a_wound.md` (the floor makes the question matter) |
| H-136 | open? | open: a `transfer` to one's own hearth is formed and refused | as the row states | first audit's `02_CHAR_offer_what_can_be_done.md` covers the class |
| H-148 | open? | changed by a ruling: casualties on both sides (Jordan, 2026-11-08), built at CR-24 (`field_winner_casualties` reads `engine`, verified) | row and fixtures | MB; the row's head still describes the world before |
| H-160 | open? | limits 1 and 2 lifted, 3 ruled a balance number, 4 open (H-54) | as the row states | SE; the limit-4 half is the question-aggregation rule this lane reads |
| H-165 | open? | open; its limit 1 "lift" was withdrawn 2026-10-26 | as the row states | SE |
| H-170 | open? | open (assumption): cohort weight 2. The row's readings say `body_step` ships 0; the fixture reads 10 today | fixtures | the row's measurements predate that flip `[UNVERIFIED: when it moved]`; SE to re-read |
| H-171 | open? | limits 1, 2, 4 open; 3 closed by REM-44 | as the row states | limit 4 (a cohort deliberates and acts) is F-CHAR-07's subject |
| H-175 | open? | narrowed: `march` executes in the realm; a fought field is 1 of 32 | as the row states | MB, FA |
| H-201 | open? | **closed** (built 2026-10-09), wired and inert: the limb answered True 0 of 1,857 asks | the row | none; an instance of F-CHAR-09 |
| H-203 | open? | open: no claim names an office; a writ reaches its addressee only by `give` | as the row states; ED-IN-0292 (1) ruled no | FA; the same closed end as `challenge` (B1.1) |
| H-204 | open? | open: the confidence-break path is unreached at `said_slant` `newest` (verified fixture) | fixtures | FI |
| H-205 | open? | **closed** as an assumption: the vow-break has its own deed cells (CR-21) | the row; `rosters.yaml` deed cells not re-opened | none |
| H-224 | open? | open (assumption): window 20, verified; `stability` reads 0 for every pair | fixtures; the row | B5: these are the "community opinion" readers and have one harness caller |
| H-229 | open? | open: a Rung `give` executes 0 | as the row states | FA |
| H-233 | open? | open: the conqueror's `march` is chosen at witness seeds only | as the row states | an instance of F-CHAR-01 (the row gives the scores: 0.0207 against 0.159) |
| H-240 | open? | **closed** as to PC-10b (built, route 1); its limit 2 stands | the row; the `accept` row's conjuncts by parse | B1.1 |
| H-270, H-322, H-300, H-329 | open? | open: acts formed for absent hearers, absent addressees and the place one already stands | as the rows state | first audit's offer proposal; these four are its measured instances |
| H-271 | open? | open: nothing lets a hearer check a told claim | as the row states | FI; B5's "a voice that can be wrong" needs it |
| H-273 | open? | open: being found a forger raises the finder's regard for 8 of 15 pursuits | as the row states | the alignment cells are Jordan's; the first audit's `regard_sign` column does not reach a deed |
| H-277 | open? | open, intent undetermined: a seat-holder opens a case on himself | as the row states | SC |
| H-280 | open? | open: every petition is addressed to its object | as the row states | SC, FA |
| H-282 | open? | open | first audit (F-CHAR-08) | first audit's `regard_sign` |
| H-286 | open? | open: `argue` does not require holding what is argued | as the row states | SC; bears on `02_CHAR_which_ground_moves_whom.md` (an argument for a thing one does not hold) |
| H-313 | open? | open | as the row states | FI |
| H-316, H-317 | open? | open: a forgery is never handed on; a lead lapses unmarked | as the rows state | FI; H-317 is the attention rule read from the investigator's side |
| H-328 | open? | open: a move costs one leg at any distance | as the row states | WR |
| H-343 | open? | open | first audit | first audit's reason trail |
| H-361 | open? | open: an order's role moves the field against its orderer; `marshal` withheld (verified) | fixtures | MB; the first audit's choice alignment cannot help until a role is a lever |

Of the 38: 4 closed or closed-as-built (H-46, H-201, H-205, H-240), 1 superseded in its headline
(H-117), 33 open or open in part. None is flagged for Jordan by this lane.

### B6.2 Inconsistencies, gaps and unclear passages: decided resolutions

| # | item | kind | decided resolution | ladder step | proposal |
|---|---|---|---|---|---|
| 1 | a scar cap per (person, element) still puts everyone in crisis by season three | gap in a proposed fix | a size floor on the violation, the cap per person, and an outflow; the first audit's cap is kept as the middle arm | 3 (the design's own gate and cap), 5 | `02_CHAR_scar_is_a_wound.md` |
| 2 | whether the actor is scarred by his own act (H-128) | unclear | yes, at the floor: a man who does what violates what he holds is the first witness of it; the arm stays swept | 5 | same |
| 3 | `resonant_style` authored on 18 rows and unread | orphan | read it, as four susceptibility traits on the hearer | 3 (the design), 4 (SC-P7's trait advantage) | `02_CHAR_which_ground_moves_whom.md` |
| 4 | `arc_trajectory` authored on 36 rows and unread | orphan | not an engine fact (ED-IN-0225); move the text to the case file's prose, delete the key | 1 | `02_CHAR_capability_definitions.md` edit 4 |
| 5 | `cultural_label` (43 rows), `self_other_initial` (28 rows) | orphan | superseded by the fifteen authored pursuits (ED-IN-0261); delete | 1 | same |
| 6 | `certainty` (8), `coherence` (1) | orphan | keep, marked unread at the loader, until threadwork has a reader; do not delete a fact a planned lane names | 2, 4 | same |
| 7 | evidence *"can crack a conviction"* (design) against #353 §9.3 | apparent conflict | none on a whole reading: the style is the hearer's and acts on `argue` | 3 | `02_CHAR_which_ground_moves_whom.md` |
| 8 | relations have no kind; `npcs.yaml`'s `tie:` says how a concern was picked, not what the person is to him | gap | an authored relation seeds a stance row and a held claim of its ground; no new carrier | 4 (the loyalty row), 5 | `02_CHAR_relations_have_a_ground.md` |
| 9 | whether kin is a ground the heir title reads | unclear | not decided here: it is the NPC research lane's K-NPC-6, Jordan's; `kin` is a ground with no eligibility reader | — | same (named, not resolved) |
| 10 | the designed foils choose alike | doc against content | content: the stances and opposed commits the foil document states; no rule | 5 | same |
| 11 | nothing a person risks reaches his choice | gap | a cost term from the row's own declared writes to the actor's body, at gain 0 | 3 (ED-IN-0304; the synthesis's one minus sign), 5 | `02_CHAR_what_an_act_risks.md` |
| 12 | appetite: capability or personality | unclear | personality (no pole always wins); nerve, as Spirit, is the capability half | 3 (the layer test of `character-layers`), AR-44 | same |
| 13 | a capability definition has no display text | gap | `gloss` on the row | 5 | `02_CHAR_capability_definitions.md` |
| 14 | the design's skill levels 1 to 3 | gap | a `when` key, `rank_at_least` | 4 (the map's `per: rank`) | same |
| 15 | a loss rule for capabilities | unclear | none: permanent, as the design has it | 3 | B4 (c); no edit |
| 16 | `ability` as a kind | unclear | not a fifth kind: a trait or aptitude with a use row at its scene's site | 4 (the DICE map) | B4 (c); no edit |
| 17 | combat abilities cannot be authored as data | gap | the lever roster's export is PC's; named, not built here | — | cross-listed |
| 18 | the development sheet omits own fields | inconsistency | add `thread_sensitivity`, `heritage`, live tenures (CORE adds `attributes`) | 5 | `02_CHAR_capability_definitions.md` edit 5 |
| 19 | what an internal voice is | unclear | a reading of one choice's terms, attributed and selected; an observer | 5 (ED-IN-0225) | `02_CHAR_voices_and_the_room.md` |
| 20 | a community's opinion of one person | gap | a reading of the regard of those present, by ground, with its change | 5 | same |
| 21 | the file for the capability definition (CORE: registry; DICE: rosters) | two proposals | not taken here; the row is identical; the holistic stage picks | — | none |
| 22 | H-46's stale last sentence; H-148's and H-170's heads | stale | text edits at the register | 1 | `02_CHAR_capability_definitions.md` edit 6 |
| 23 | `conviction_track_v30.md` filed as a character document | wrongly filed | no edit; noted | 2 | none |
| 24 | the lifepath grant changes no roll | gap | a bundle may grant at a rank; the rank is content | 4 (CORE edits 5 and 9) | `02_CHAR_capability_definitions.md` edit 3 |

Twenty-four resolutions; nineteen carried by a proposal file of this lane, two cross-listed, three
needing no edit.

### B6.3 For Jordan

No new survivor. The first audit's one item (can a person be wrong about himself?) stands, with the
added evidence of C-8: the design twice writes a person who is (Sæmund's unrecognised sensitivity;
AR-49's man *"unaware of their impact on others"*). Option B there would also be what makes B5's
"a voice that was wrong about oneself" possible. Not re-argued.

## B7. Evidence log

All `PYTHONHASHSEED=0`. Scratch scripts and outputs:
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/CHAR_B/`. The
tree was read at `ad07a9a`; the orchestrator committed during the lane (`46500d4` at the probes).

| command or probe | seed, seasons | outcome |
|---|---|---|
| parse of `verb_table.yaml` typed conjuncts, ten rows | — | `challenge`: existence Person, `with`, `dispute`; `fight`, `capture`, `accept` carry `individual` twice; `forge`, `create_record` none |
| parse of `references/npc_registry.yaml` | — | 46 rows; non-null `resonant_style` 18, `arc_trajectory` 36, `cultural_label` 17 top-level and 26 nested under `convictions:`, `self_other_initial` 2 and 26, `certainty` 8, `coherence` 1, `stats` 1, `ts` 10, `goals` 17, `lifepath` 5, `heritage` 4 |
| `grep` of non-test `.py` under `engine`, `modules`, `tools`, `systems` for the six unread keys | — | one hit, a comment (`data/cast.py:220`) |
| parse of `rosters.yaml: tables.lifepath_templates` | — | 34 rows: 21 hold nothing, 7 `inquiry`, 6 `argue` |
| `ALIGNMENT` non-zero cells per axis | — | `selfish_selfless` 2; the others 8 to 25 |
| `DEFAULT_FIXTURES` read for 20 names | — | as cited in B6.1 (`body_step` 10, `scene_budget` 5, `interactions_per_scene` 3, `stance_polarity` `declared`, `marshal` withheld) |
| `dataclasses.fields` of `Person`, `CreationRow`, `DevelopmentSheet`, `Chronicle` | — | 17, 6, 11, 7 fields; F-CHAR-21 |
| `probe_foils.py` (ten named persons, six referents, temperature 0) | 0 and 1, no season | identical at both seeds; F-CHAR-18's figures |
| `probe_scar_stock.py` (seasons in which each (person, element) count rose) | 0, 4 | hashes `5ab73af2`, `bacd687f`, `52ff67bc`, `abbde715`; capped maximum 1, 2, 3, 4 for 83 of 83; median elements at 3 or more: 9 then 11 |
| regular-expression count over the skill-bearing table rows of `character_histories_v30.md` | — | 106 rows; bonus dice 83, target number 7, obstacle 11, immunity 13, limited use 6, strain and resource 13, new action 9, sensitivity grant 2 |

| `probe_scar_stock.py` | 1, 4 | hashes `aa58ef0b`, `8aae8412`, `26d2091b`, `25d23448`; capped maximum 1, 2, 3, 4; 82 of 82 at 3 or more from season three; median elements at 3 or more: 11 then 12 |

Not run: `pytest`; `aperture`; `corpus_run` (the first audit's reading stands). The scar probe's
capped reading is first-order (B2.3, F-CHAR-17).
