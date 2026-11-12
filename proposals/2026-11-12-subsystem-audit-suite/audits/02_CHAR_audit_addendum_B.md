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
