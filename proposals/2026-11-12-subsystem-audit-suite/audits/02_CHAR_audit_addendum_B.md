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
