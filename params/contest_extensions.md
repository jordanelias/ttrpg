# params_contest.md — Social Contest System (v2) Extensions

Companion to `params/contest.md`. Holds post-v2 canonical additions and integration rules.
Filed here for size-cap discipline (params/contest.md core kept under 4000 token threshold per hook).

## PP-NEW-A — TIE/Cross-Time no-strain exception (SIM-DB-STRESS-01 D-04)
TIE row in Interaction Types table updated to include Cross-Time exception.
In Cross-Time + TIE: no strain to either orator (PP-236 takes precedence). Persuasion Track +1 toward first-to-speak holder as normal.
Source: SIM-DB-STRESS-01 D-04 finding. 2026-04-09.

## PP-NEW-D — Concentration maximum (SIM-DB-STRESS-01 D-08b; updated PP-716)
Concentration maximum = Focus × 3 (= starting value at contest setup; per `designs/scene/derived_stats_v30.md` §5.2).
Restoration (from Regroup or other effects) cannot raise Concentration above this maximum.
Source: SIM-DB-STRESS-01 D-08b finding. 2026-04-09.

## Evidence Track Findings in Contest (PP-636)

Findings from completed fieldwork investigations may be cited in Contest opening (§9.1).

| Findings cited | Exchange 1 bonus |
|---|---|
| 1 Finding | +1D |
| 2+ Findings | +2D (cap) |

Findings are **not consumed** by citation — remain on Evidence Track. Must be declared at contest setup. GM determines scope relevance (Finding must relate to contest subject). Stacks with §9.1 preparation bonus (+1D), for maximum Exchange 1 pool bonus of +3D when both available.

Source: fieldwork_investigation.md §2.3 / F-TRANS-11. social_contest_system_v2.md §9.1.

## Resonant Style Targeting (from npc_behavior_system_v1.md §6)
<!-- Source: designs/systems/npc_behavior_system_v1.md. Canonical. -->

### Appraise Revelation
| Appraise net | Resonant Style info |
|---|---|
| Overwhelming (3+) | Primary Resonant Style revealed (in addition to one Belief per existing rules) |
| Overwhelming (4+) | Both primary and secondary Resonant Style revealed |

### Targeting Declaration
Before Argue roll (Step 3): player declares "targeting Resonant Style." GM confirms match.
Requires: (a) argument uses Contest style mapping to the declared MS, (b) content addresses a known Belief, (c) player has previously discovered the MS.

### Targeting Effects
| MS | Required form | On confirmed targeting |
|---|---|---|
| Evidence | Past + Direct. Must cite specific named verifiable claim. | +1D Argue. On win: Persuasion Track +1 additional (bypasses 1 resistance). |
| Consequence | Future + Direct. Must project specific outcome framework fails to prevent. | +1D Argue. On win: NPC +2 strain. |
| Sanction | Invoke specific binding authority contradicting NPC's position. | +1D Argue. Suspicion Token placed regardless of outcome. |
| Solidarity | Requires active Knot with NPC. Must invoke the relationship. | +1D Argue. On win: no strain, NPC Belief revision Ob −1. |

### TS Gate (P-08 compliance)
Thread-level evidence invalid as Evidence targeting vs TS 0 NPCs. Ontical evidence only. Exception: TS 30+ NPCs accept Thread-level evidence.

### Wrong-Style Penalty (Church Martyrdom extension)
Wrong MS vs Church institutional NPC (Himlensendt, Olafsson, Klapp, Cardinals) in public venue with Failure/Partial: Church Stability +1 (PP-259 fires).

### Stacking
Max positional bonus: +5D (genre +1, audience +1, MS targeting +1, Recall +2). Each prerequisite independently costly. Practical pools 12–18D; 25D+ extreme.

## Temporal Axis Conflict (PP-351 — canonical)

If a practitioner initiates a Thread operation on a temporal axis that opposes
the contest's primary temporal orientation, the Thread operation's co-movement
effects apply to the contest's Persuasion Track (±1 shift per co-movement
card drawn during the contest scene).

## Church Self-Investigation Exception (PP-349 — canonical)

The Church does not file Heresy Investigation against its own ordained members
who are supporting Church institutional interests (CI advancement, PT increase,
infrastructure expansion). Self-investigation only triggers when an ordained
member acts against Church interests (supporting RM, lowering PT, aiding
Varfell Thread programs).

