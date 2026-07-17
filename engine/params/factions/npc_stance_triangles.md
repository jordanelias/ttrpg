## NPC Stance Triangles (PP-NEW — from npc_behavior_system_v1.md)

<!-- Source: designs/systems/npc_behavior_system_v1.md §2. Canonical. -->

### Conviction Taxonomy
| Conviction | Grounding Claim |
|---|---|
| Faith | Value is revealed through divine authority |
| Order | Value is maintained through structure |
| Reason | Value is discovered through evidence |
| Equity | Value is distributed justly |
| Precedent | Value is inherited from what has been established |
| Autonomy | Value is chosen by the actor |
| Continuity | Value is sustained through practice |

NPCs hold primary + secondary Conviction. Secondary activates under pressure (Belief Scars, Stability ≤ 1).

### Resonant Style Taxonomy
| Style | Vulnerable to | Contest mapping |
|---|---|---|
| Evidence | Verifiable facts contradicting operative belief | Memory + Revealing (Precedent) |
| Consequence | Outcomes the framework fails to prevent | Projection + Revealing (Vision) |
| Authority | Appeals from a recognised binding source | Memory + Obscuring (Suppression) |
| Solidarity | Relational obligation via active Knot | Any + Revealing; requires Knot |

TS Gate: Thread-level evidence invalid as Evidence targeting vs TS 0 NPCs (P-08 compliance). Ontical evidence only.

### Named NPC Stance Triangles
| NPC | Faction | Primary Conviction | Secondary | Primary Resonant Style | Secondary MS | TS | Certainty |
|---|---|---|---|---|---|---|---|
| Almud | Crown | Order | Reason | Consequence | Solidarity | 28 | 3 |
| Himlensendt | Church | Faith | Order | Evidence | Authority | 0 | 5 |
| Baralta | Hafenmark | Precedent | Faith | Evidence | Consequence | 0 | 4 |
| Vaynard | Varfell | Reason | Autonomy | Consequence | Evidence | 14 | 3 |
| Ehrenwall | Löwenritter | Order | Autonomy | Consequence | Solidarity | 0 | 4 |
| Vossen | Restoration | Equity | Continuity | Solidarity | Consequence | 0 | 2 |
| Hann | Restoration | Equity | Autonomy | Consequence | Evidence | 0 | 3 |
| Torben | Crown (heir) | Blank (contested) | Autonomy | Solidarity | Authority | 0 | 3 |
| Edeyja | Wardens | Continuity | Reason | Evidence | Consequence | 75–80 | 0 |
| Maret Uln | Varfell (succession) | Equity | Reason | Evidence | Solidarity | 0 | 2 |

Torben: first faction at Loyalty ≥ 5 sets primary Conviction. Default Autonomy at Year-End Year 2.

### Framework Drift
| Framework | Faction | Drift | Frequency | Cap |
|---|---|---|---|---|
| Faith | Church | Influence +1 if: no hostile DA vs Church + Stability ≥ 4 + CI advanced | Per year (Year-End) | Stat ceiling 7 (PP-NPC-03) |
| Virtue | Crown | Crown NPCs Certainty ≥ 3: +1 Certainty/year unchallenged | Per year | Certainty 5 |
| Categorical Imperative | Hafenmark | Influence +1 per season all actions framework-aligned | Per season (conditional) | Stat ceiling 7 |
| Utility-driven Pragmatism | Varfell | TK +0.5/season active investigation; caps TK 3 without PC | Per season | TK 3 |
| Equity Social Contract | RM | Presence +1 adjacent territory/season when Stability ≥ 3 | Per season (conditional) | — |
| Moral Relativism | Guilds | Guild Favour +1 in highest-Favour territory/Year-End | Per year | Favour 7 |
<!-- Amoral Consequentialism / Niflhel row deleted 2026-04-30 — Niflhel struck. No faction holds this disposition post-strike. -->
| Martial Honour | Löwenritter | If Military < 5: redirect all non-survival to consolidation | Continuous | Military 5 |

Drift is passive (not a Domain Action). Does not count toward ±2 DA seasonal cap. Subject to stat ceiling (7) and floor (1).

### NPC Knot Formation (ED-522)
| Knot level | Requirement |
|---|---|
| Distant | 2+ scenes of cooperative interaction + Bonds check (Bonds, TN 7, Ob 1) |
| Close | 1 full season of active relationship + Bonds check Ob 2 |
| Intimate | 1 full arc of sustained relationship + Bonds check Ob 3 + mutual Belief alignment |

### NPC Belief Revision
Trigger: decisive Contest outcome (Piety Track ≥ 7 or ≤ 3) + winning argument used NPC's Resonant Style + argument specifically engaged the Belief. Old Belief → Scar (permanent). New Belief forms.

Scar effects: 1 Scar = secondary Conviction activates. 2 Scars = primary may shift to secondary; secondary MS activates. 3+ Scars = Conviction crisis (d6 table per major decision).
