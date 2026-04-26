# Topic 06 — Mechanical Review & Audit — Sub-decomposition

**Source:** `06_mechanical_review_audit` (83 atoms, single-source from `valoria_master_document.md`)
**Strategy:** group by section-prefix in `source_section` field. Each sub-topic becomes its own audit unit.

## Proposed sub-topics

| sub-topic | section prefix | atoms | sample sections |
|---|---|---|---|
| `06_1` | `^1\.` | 3 | 1.1 Die Face Rule (d10) / 1.3 Obstacle Scale / 1.4 Degrees of Success |
| `06_3` | `^3\.` | 9 | 3.1 Pool Split (Off/Def) / 3.2 Initiative / 3.3 Weapon System (3 Binary Axes) / 3.4 Armour |
| `06_4` | `^4\.` | 5 | 4.1 Adjudicator → Pool Rotation / 4.2 Styles (2×2) / 4.3 Interaction Types / 4.4 Conviction Track (0–10) |
| `06_5` | `^5\.` | 7 | 5.2 Three-Axis Ob / 5.3 Operations / 5.4 Opposing Operations (PP-653) / 5.5 Gap Self-Closure |
| `06_6` | `^6\.` | 5 | 6.2 Fieldwork Pool and Attribute Rotation / 6.3 Evidence Track / 6.4 Socializing / Disposition / 6.5 Exposure System |
| `06_7` | `^7\.` | 3 | 7.1 Core Formula (PP-233) / 7.3 Key Mechanics / 7.4 PROVISIONAL Count |
| `06_8` | `^8\.` | 2 | 8.2 Scene Lifecycle / 8.3 Scene Budget and Scene Slate |
| `06_9` | `^9\.` | 6 | 9.1 Card-Hand Economy / 9.2 Action Ob Formulas / 9.4 Faction Starting Stats / 9.5 Global Tracks |
| `06_10` | `^10\.` | 1 | 10.3 Zoom In / Zoom Out |
| `06_11` | `^11\.` | 1 | 11.2 Hybrid Phase Structure |
| `06_12` | `^12\.` | 3 | 12.2 CI (Church Influence) / 12.3 IP (Invasion Pressure) / 12.4 PI (Parliament Integrity) |
| `06_13` | `^13\.` | 4 | 13.1 Universal Victory — Peninsular Sovereignty / 13.2 Faction Toolkits (NOT Alternate Endpoints) / 13.3 Co-Victory (6 Pairings) / 13.4 World-State Transitions |
| `06_14` | `^14\.` | 6 | 14.1 Architecture / 14.2 Dual-Authority Governance / 14.3 Church 4-Axis Infrastructure / 14.4 Faction Emergence (5 Stages) |
| `06_15` | `^15\.` | 5 | 15.1 Unit Representation / 15.2 Muster / 15.3 TC Competitive Formula / 15.4 Accord → Military |
| `06_16` | `^16\.` | 8 | 16.2 Named NPC Profiles (12 core) / 16.3 Decision Procedure / 16.3 Mending Community / 16.5 BG Priority Trees (All Factions) |
| `06_20` | `^20\.` | 2 | 20.1 Formula Consistency / 20.2 The Complete Pipeline |
| `06_misc` | `^misc\.` | 2 | (preamble) / Conversation Date: 2026-04-24 to 2026-04-25 | Comp |
| `06_II` | `^II\.` | 3 | II.2 Open Decisions Requiring Jordan (16 items) / II.5 Rating Corrections Applied / II.6 Mechanics Flagged for Removal |
| `06_III` | `^III\.` | 2 | III.1 Findings Register (14 items) / III.4 Claims That Are Speculative/Hypothesis-Level |
| `06_IV` | `^IV\.` | 2 | IV.2 Claims I Cannot Currently Verify / IV.3 Recursive Drift Risk |
| `06_V` | `^V\.` | 4 | V.3 Derived Stats (GAP-07) / V.4 Caste / Social Structure / V.5 Royal Assassination Fuse / V.6 Other Likely Unreviewed Items |

## Recommendation

Replace single 83-atom topic 06 with 21 sub-topics. Each sub-topic re-audited independently. Sub-topics smaller than 5 atoms can be merged with adjacent sub-topics.

No code action required at Stage 4 — sub-decomposition only changes the audit unit, not the underlying atoms. Update `_topic_decomposition.yaml` to reflect the split before any canon ingestion of topic 06 content.
