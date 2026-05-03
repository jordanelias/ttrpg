

<!-- [SUPERSEDED 2026-04-19] CULTURAL REFORMATION STRUCK + VTM STRUCK -->
<!-- Per Jordan decision 2026-04-19 (session): Cultural Reformation was incompatible with Vaynard's identity. -->
<!-- Vaynard is a military conqueror. He does not convert populations ideologically. Varfell expansion is purely military. -->
<!-- VTM (Vaynard Thread Mastery) was also STRUCK — placeholder mechanic with no canonical advancement. -->
<!-- Tribune intel (reveals enemy stats for target selection) remains. Thread operations remain as personal-scale actions -->
<!-- available to Varfell first due to southern TS baseline + RM proximity, NOT as BG-layer combat/territorial bonuses. -->
<!-- See commits: 297f892 (engine), 13b8f30 (workplan), 13b8f30 (canon audit workplan). -->

## NPC Faction Priority Trees (from npc_behavior_system_v1.md §8)
<!-- Source: designs/systems/npc_behavior_system_v1.md. Canonical. -->
<!-- Ministry Priority Tree (existing, PP-564) retained above. Trees below cover all other NPC factions. -->

### Priority Tree Template (7 levels)
| Priority | Name | Description |
|---|---|---|
| 1 | Survival | Stability ≤ 2: raise Stability or remove threat. Overrides all. |
| 2 | Conviction-critical | Game-state threatens leader's primary Conviction: address it. |
| 3 | Framework-aligned | Framework-aligned action (−1 Ob) available + produces stat improvement: take it. |
| 4 | Institutional Tendency | Faction default behavior (stage6). |
| 5 | Conviction-secondary | Secondary Conviction relevant + no higher priority fired. |
| 6 | Reactive | Attacked/threatened: respond proportionally. |
| 7 | Pass | No action. Bank Standing or accumulate. |

### Church Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward highest-PT territory. Suspend CI Assert if Stability = 1. |
| 2 | Open Thread op in Church territory OR practitioner public OR Piety −2 | Heresy Investigation. If target = faction leader: Excommunication. |
| 3 | CI < 75 AND Church L ≥ 4 | Assert (CI +1). Piety DA if Assert used. |
| 4 | Default | Expand Piety. Consul Inward lowest-PT territory with Church presence. |
| 5 | AER maintenance | Temperance declaration if Cardinal active + Church controls T9. |
| 6 | Attacked | Templar deployment if Fortitude active + Stability ≥ 2. |
| 7 | Default | Pass. |
Post-CI 75: P3 → Territorial Seizure (highest-value targets first).

### Crown Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward capital. Royal Decree own Stability if available. |
| 2 | 2+ territories changed OR Löwenritter Autonomy = Restless OR PI ≥ 8 | Military response. Legionary in threatened territory. |
| 3 | Royal Decree available + framework-aligned target | Decree: +1 weakest-stat ally or −1 strongest-stat rival. |
| 4 | Default | Maintain treaties. Defend territory. Govern. Consul/Senator. If T2 Kronmark is ungarrisoned AND any Varfell unit is active in T4: deploy minimum garrison to T2 (1 unit, Legionary Inward). Crown's breadbasket must not be left exposed when Varfell has forward-deployed forces. |
| 5 | Torben Loyalty ≤ 3 | Senator Outward targeting Torben. |
| 6 | Attacked | Military proportional. Crown covert (Influence +1 Ob). |
| 7 | Default | Pass. Thread Liaison if allied faction identified. |

### Hafenmark Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward capital. |
| 2 | Church seizes territory OR constitutional bypass | Sovereign Authority Doctrine or Parliamentary objection. |
| 3 | Suppress available (Church M ≥ 4, Baralta M ≥ 4) | Suppress CI. |
| 4 | Default | Maintain order. Consul Inward. Diplomatic Senator to Crown/Guilds. |
| 5 | Trade Compact conditions met | Pursue Compact activation. |
| 6 | Attacked | Parliamentary Manoeuvre. Legionary defensive only. |
| 7 | Default | Pass. Wealth Sink if W > 5. |

### Varfell Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward capital. |
| 2 | TK opportunity: Expedition OR Collection OR practitioner contact | Collection deployment or Tribune Investigate (Thread intel). |
| 3 | Intel action with measurable outcome | Tribune Investigate vs highest-hidden-stat rival. |
| 4 | Default | Maximise info advantage. Senator Outward. |
| 5 | WR advancement conditions met | Pursue Warden Recognition. If no Varfell unit in T15: March to T15 (Legionary Outward) as immediate priority. (PP-664: VTM gating struck with VTM track.) |
| 6 | Attacked | Intel response: reveal attacker's hidden stat. No military first-strike. |
| 7 | Default | Pass. Patience Protocol (+2D future). |

### Guilds Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward highest-Favour territory. |
| 2 | — | No single-leader Conviction. Priority 2 does not fire. |
| 3 | Economic Leverage available (Favour ≥ 5) | Wealth vs lowest-Wealth target in eligible territory. |
| 4 | Default | Protect commerce. Consul Inward trade hubs. |
| 5 | — | No secondary Conviction. |
| 6 | Attacked | Economic Leverage vs attacker if eligible. Else Senator ally-seek. |
| 7 | Default | Pass. Favour accumulation. |

### Löwenritter Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Military Consolidation. |
| 2 | Löwenritter Autonomy = Restless + trigger imminent | Prepare: pre-position Legionary T14. |
| 3 | Sovereignty defence available (border, Altonian) | Legionary border territory (−1 Ob Martial Honour). |
| 4 | Bordering faction Military > Löwenritter | Military Consolidation (PP-238). |
| 5 | Crown M < 3 or Torben Loyalty < 3 | Riskbreaker activation vs faction threatening Crown. |
| 6 | Attacked | Full Military response. No negotiation under military threat. |
| 7 | Default | Pass. Maintain garrison. |
Post-Coup: all priorities → Martial Law → consolidate → Reconstitution (PI = 0).

<!-- §Niflhel Priority Tree deleted 2026-04-30 — was STRUCK per conflict_architecture_proposal §Niflhel Dissolution. Functions distributed to settlement-level phenomena (settlement_layer §4.7-4.9). -->

### Restoration Movement Priority Tree (Post-Founding)
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Community Organising, most-Presence territory. |
| 2 | PT ≤ 1 in 3+ territories | Community Organising in lowest-PT adjacent. |
| 3 | Stability ≥ 3 | Presence spread to adjacent territory. |
| 4 | Default | Founding Agent protection. |
| 5 | RS ≤ 60 + TS 30+ practitioner available | Community Weaving. |
| 6 | Attacked | Non-violent. Diplomatic appeal to ally. |
| 7 | Default | Pass. Presence maintained. |

### Edeyja/Wardens Priority Tree (Post-Emergence)
| P | Condition | Action |
|---|---|---|
| 1 | Gap or Shifting Object detected | Emergency Mend at Gap site. |
| 2 | Thread exploitation site disturbance detected | Investigate. Intercept operatives. |
| 3 | RS ≤ 40 | Peninsula-wide Weaving. RS +1/Warden (max +2/season). |
| 4 | Faction performing Thread restoration | Cooperation: +1D allied Thread ops (WC ≥ 1). |
| 5 | New practitioner enters Southernmost | Assessment. TS ≤ 20: dismissed. TS 40+: useful. |
| 6 | Attacked | Thread operations at scale rendering force irrelevant. |
| 7 | Default | Containment. Hold the Southernmost. |


### Priority Tree Template (7 levels)
| Priority | Name | Description |
|---|---|---|
| 1 | Survival | Stability ≤ 2: raise Stability or remove threat. Overrides all. |
| 2 | Conviction-critical | Game-state threatens leader's primary Conviction: address it. |
| 3 | Framework-aligned | Framework-aligned action (−1 Ob) available + produces stat improvement: take it. |
| 4 | Institutional Tendency | Faction default behavior (stage6). |
| 5 | Conviction-secondary | Secondary Conviction relevant + no higher priority fired. |
| 6 | Reactive | Attacked/threatened: respond proportionally. |
| 7 | Pass | No action. Bank Standing or accumulate. |


### Church Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward highest-PT territory. Suspend CI Assert if Stability = 1. |
| 2 | Open Thread op in Church territory OR practitioner public OR Piety −2 | Heresy Investigation. If target = faction leader: Excommunication. |
| 3 | CI < 75 AND Church L ≥ 4 | Assert (CI +1). Piety DA if Assert used. |
| 4 | Default | Expand Piety. Consul Inward lowest-PT territory with Church presence. |
| 5 | AER maintenance | Temperance declaration if Cardinal active + Church controls T9. |
| 6 | Attacked | Templar deployment if Fortitude active + Stability ≥ 2. |
| 7 | Default | Pass. |
Post-CI 75: P3 → Territorial Seizure (highest-value targets first).


### Crown Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward capital. Royal Decree own Stability if available. |
| 2 | 2+ territories changed OR Löwenritter Autonomy = Restless OR PI ≥ 8 | Military response. Legionary in threatened territory. |
| 3 | Royal Decree available + framework-aligned target | Decree: +1 weakest-stat ally or −1 strongest-stat rival. |
| 4 | Default | Maintain treaties. Defend territory. Govern. Consul/Senator. If T2 Kronmark is ungarrisoned AND any Varfell unit is active in T4: deploy minimum garrison to T2 (1 unit, Legionary Inward). Crown's breadbasket must not be left exposed when Varfell has forward-deployed forces. |
| 5 | Torben Loyalty ≤ 3 | Senator Outward targeting Torben. |
| 6 | Attacked | Military proportional. Crown covert (Influence +1 Ob). |
| 7 | Default | Pass. Thread Liaison if allied faction identified. |


### Hafenmark Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward capital. |
| 2 | Church seizes territory OR constitutional bypass | Sovereign Authority Doctrine or Parliamentary objection. |
| 3 | Suppress available (Church M ≥ 4, Baralta M ≥ 4) | Suppress CI. |
| 4 | Default | Maintain order. Consul Inward. Diplomatic Senator to Crown/Guilds. |
| 5 | Trade Compact conditions met | Pursue Compact activation. |
| 6 | Attacked | Parliamentary Manoeuvre. Legionary defensive only. |
| 7 | Default | Pass. Wealth Sink if W > 5. |


### Varfell Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward capital. |
| 2 | TK opportunity: Expedition OR Collection OR practitioner contact | Collection deployment or Tribune Investigate (Thread intel). |
| 3 | Intel action with measurable outcome | Tribune Investigate vs highest-hidden-stat rival. |
| 4 | Default | Maximise info advantage. Senator Outward. |
| 5 | WR advancement conditions met | Pursue Warden Recognition. If no Varfell unit in T15: March to T15 (Legionary Outward) as immediate priority. (PP-664: VTM gating struck with VTM track.) |
| 6 | Attacked | Intel response: reveal attacker's hidden stat. No military first-strike. |
| 7 | Default | Pass. Patience Protocol (+2D future). |


### Guilds Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Consul Inward highest-Favour territory. |
| 2 | — | No single-leader Conviction. Priority 2 does not fire. |
| 3 | Economic Leverage available (Favour ≥ 5) | Wealth vs lowest-Wealth target in eligible territory. |
| 4 | Default | Protect commerce. Consul Inward trade hubs. |
| 5 | — | No secondary Conviction. |
| 6 | Attacked | Economic Leverage vs attacker if eligible. Else Senator ally-seek. |
| 7 | Default | Pass. Favour accumulation. |


### Löwenritter Priority Tree
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Military Consolidation. |
| 2 | Löwenritter Autonomy = Restless + trigger imminent | Prepare: pre-position Legionary T14. |
| 3 | Sovereignty defence available (border, Altonian) | Legionary border territory (−1 Ob Martial Honour). |
| 4 | Bordering faction Military > Löwenritter | Military Consolidation (PP-238). |
| 5 | Crown M < 3 or Torben Loyalty < 3 | Riskbreaker activation vs faction threatening Crown. |
| 6 | Attacked | Full Military response. No negotiation under military threat. |
| 7 | Default | Pass. Maintain garrison. |
Post-Coup: all priorities → Martial Law → consolidate → Reconstitution (PI = 0).


<!-- §Niflhel Priority Tree deleted 2026-04-30 — was STRUCK per conflict_architecture_proposal §Niflhel Dissolution. Functions distributed to settlement-level phenomena (settlement_layer §4.7-4.9). -->

### Restoration Movement Priority Tree (Post-Founding)
| P | Condition | Action |
|---|---|---|
| 1 | Stability ≤ 2 | Community Organising, most-Presence territory. |
| 2 | PT ≤ 1 in 3+ territories | Community Organising in lowest-PT adjacent. |
| 3 | Stability ≥ 3 | Presence spread to adjacent territory. |
| 4 | Default | Founding Agent protection. |
| 5 | RS ≤ 60 + TS 30+ practitioner available | Community Weaving. |
| 6 | Attacked | Non-violent. Diplomatic appeal to ally. |
| 7 | Default | Pass. Presence maintained. |


### Edeyja/Wardens Priority Tree (Post-Emergence)
| P | Condition | Action |
|---|---|---|
| 1 | Gap or Shifting Object detected | Emergency Mend at Gap site. |
| 2 | Thread exploitation site disturbance detected | Investigate. Intercept operatives. |
| 3 | RS ≤ 40 | Peninsula-wide Weaving. RS +1/Warden (max +2/season). |
| 4 | Faction performing Thread restoration | Cooperation: +1D allied Thread ops (WC ≥ 1). |
| 5 | New practitioner enters Southernmost | Assessment. TS ≤ 20: dismissed. TS 40+: useful. |
| 6 | Attacked | Thread operations at scale rendering force irrelevant. |
| 7 | Default | Containment. Hold the Southernmost. |


## PP-NPC-01 — Crown Royal Decree Gate (SIM-NPC-01 F-01)
Crown Priority Tree P3 (Royal Decree): do NOT attempt if Crown L ≤ 2 (institutional weakness). At L ≤ 2, Crown defaults to P4.
Royal Decree failure cost (L −1) applies only at L ≥ 3. At L ≤ 2: failure produces no L loss (institution too weak for additional reputational damage).


## PP-NPC-02 — Crown CI Awareness + Löwenritter Autonomy Refinement (SIM-NPC-01 F-02/F-03; ED-781 migration)
Crown Priority Tree P2: insert trigger "If CI ≥ 35: Crown takes CI-reducing action (Senator Outward to Hafenmark for coordinated Suppress, OR direct DA targeting Church L — institutional procedural-authority suppression). This fires BEFORE the standard P2 triggers (territory loss, coup, PI)."
Löwenritter Autonomy advance to Restless via CI ≥ 40 trigger requires BOTH conditions: (a) CI ≥ 40, AND (b) Church actively Asserted this season. Passive CI advance alone does not advance the Autonomy stage. Crown must have failed to prevent active Church expansion, not merely failed to counter institutional drift. (ED-781: 'Coup Counter increment' migrated to 'Löwenritter Autonomy advance to Restless'.)


## PP-NPC-03 — Church Framework Drift Revision (SIM-NPC-01 F-02)
Church Framework Drift (Influence +1) conditions revised:
- (a) No faction targeted Church with any hostile DA this season, AND
- (b) Church Stability ≥ 4, AND
- (c) CI advanced this season (Influence drift IS the CI advance — same institutional process).
- Frequency: per year (at Year-End Accounting), not per 2 seasons.
Replaces prior unconditional 2-season drift.


## PP-NPC-04 — Varfell Collection Cooldown (SIM-NPC-01 F-06)
Varfell Priority Tree P2: fires only if Private Collection not yet used this season. After P2 fires, mark Collection as used (state flag). Flag resets at Accounting. If Collection used, skip to P3 (Tribune Investigate).
Aligns with canonical stage6 §8.5 once-per-season limit.
