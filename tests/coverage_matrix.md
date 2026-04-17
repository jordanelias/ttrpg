# Coverage Matrix — Active
# Full archive: tests/coverage_matrix_archive.md
# Last updated: 2026-04-16
# Total sim runs completed: 29 (see archive for full history)

## Open SIM-DEBT

## SIM-DEBT Register

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-DEBT-02 | SIM-D-04 | **STRUCK** — superseded by PP-234 (Social Contest System v2 redesign). Corroboration mechanics rebuilt. Subsumed by SIM-DEBT-03. |

*(old SIM-DEBT register entries above)*


| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-DEBT-01 | Debate system | RESOLVED. Mode C (SIM-D-02) confirmed: resistance dominates track movement; genre weight > pool size adjustments; 3-exchange Formal Debate → Compromise ~95%. CLASH strain calibration (2-3/exchange) analytically confirmed, scenario validation pending forced-CLASH run. | RESOLVED |
| AUD-TTRPG-01 | Modes A–G: Formula, Number Systems, Interaction Chains, Gap Detection, Core Principles, Playtest Burden, Cross-Mode | TTRPG | — | All tracks | All factions | All named NPCs | Full TTRPG mode | Complete | 11 P1s, 14 P2s, 4 P3s — see tests/aud_ttrpg_01.md |
| SIM-NPC-01 | npc_behavior_v30 §11 | Full BG simulation with all NPC priority trees active. Validate multi-faction interaction under priority tree model. | OPEN — sim_open_items_2026-04-16 §B covers partial; full 6-faction BG sim pending |
| SIM-NPC-02 | npc_behavior_v30 §11 | Contest simulation: Resonant Style +1D stacking with genre/audience/Recall bonuses. Validate pool sizes and Conviction Track movement rates. | COVERED — SIM-02 chain contest convergence confirms convergence ≤5 exchanges |
| SIM-NPC-03 | npc_behavior_v30 §11 | Arc emergence simulation: run 3-season TTRPG campaign with Almud and Himlensendt arc triggers. | OPEN — pending |
| SIM-NPC-04 | npc_behavior_v30 §11 | Framework Drift simulation: run 6-season BG game with all drift mechanics active. | OPEN — pending |
| SIM-NPC-05 | npc_behavior_v30 §11 | Belief Scar cascade: validate 3+ Scars on single NPC. | OPEN — pending |


## Open P1 Findings

## P1 Findings — Editorial Decisions Required

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-11 | X-03 | W-33 broken for Size≤2 units: Cohesion=2 insufficient when Size is binding constraint | RESOLVED — ST-TW-02 applied to threadwork_redesign_v25.md |
| F-27 | X-07 | Mass battle deadlock (HeavyCut vs HeavyArmour): no stalemate resolution rule | PATCHED — Add to mass_battle_v3: at 3+ consecutive turns with 0 damage dealt, units with no tactical option may withdraw one zone (costs movement, does not trigger pursuit). |
| F-30/F-33 | X-07/08 | Coup Counter: no successor rule on Grandmaster death | PROVISIONAL — On Grandmaster death with Coup Counter ≥ 1: Löwenritter selects highest-CR surviving named officer as acting Grandmaster. Coup Counter resets to 0. Provisional pending user approval. |
| F-43 | X-10 | Two Domain Actions can drop TC by 4+ in one season; no seasonal cap on TC | PROVISIONAL — TC change cap: ±3 per season from Domain Actions (±5 from all sources combined). Provisional pending user approval. |
| F-45 | X-10 | Church Stability brake scope — suppresses Mandate-based TC only or all TC sources? | EDITORIAL — ED-049 added to ledger |
| F-52 | X-12 | No Stability recovery mechanic for externally damaged faction Stability | PROVISIONAL — Stability recovery: +1 Stability per season of no hostile Domain Actions targeting that faction + Stability ≤ 3 (slow natural recovery). Provisional pending user approval. |
## New P1 Findings (SIM-X-13 through X-16)

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-58 | X-14 | RS 22 is 2 points from Dormant (Leap-disabled) threshold — any failed Weaving crosses the line globally | Open — campaign awareness item |

## New P1/P2 Findings (sim_open_items_2026-04-16)

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-59 | SIM-SETT-04 | Altonian Vanguard priority tree missing Assault entry — cannot siege garrisoned Fort territories under NPC AI | Open — ED-551 |
| F-60 | SIM-COMP | companion_specification_v30.md forward-referenced but does not exist; companion stat gen, AI, mass combat role all undefined | Open — ED-555, 557, 559, 571 |
| F-61 | SIM-ED137 | Panel Adjudicator type undefined — blocks social_contest_v30 Panel mechanic and UI-07 | Open — ED-562 |
| F-62 | SIM-03 | IP passive advancement overproduces Vanguard deployments in 30-year (120-season) games | Open — ED-565, 566 |
| F-63 | SIM-04 | NPC leader mortality absent — all named leaders immortal in 30-year games; generational shift cannot emerge without Longevity mechanic | Open — ED-567, 568, 569 |


## Provisional Decisions Pending Application

## Provisional Decisions (from coverage matrix findings)

| Finding | Provisional Rule | Status |
|---------|-----------------|--------|
| F-27 | Mass battle stalemate: 3+ turns 0 damage → may withdraw one zone | Provisional — apply to mass_battle_v3 |
| F-30/F-33 | Coup Counter successor: highest-CR officer, Counter resets | Provisional — apply to designs/combat |
| F-43 | TC change cap: ±3/season Domain Actions, ±5 all sources | Provisional — apply to stage5_clocks or designs |
| F-52 | Stability recovery: +1/season with no hostile actions when Stability ≤ 3 | Provisional — apply to faction rules |
| SIM-02 | Social contest stalemate: 5-exchange cap → forced Partial in current Track direction | Provisional — ED-564; apply to social_contest_v30 |
| SIM-03 | IP recalibration: passive IP ×0.5 after season 40; ×0.25 after season 80; 3-season Vanguard cooldown | Provisional — ED-565/566; apply to params_board_game |
| SIM-04 | Longevity Track + Year-End mortality roll; Succession Procedure on death | Provisional — ED-567/568/569; apply to npc_behavior_v30 |


## New P1/P2 Findings (sim_stress_batch_2_2026-04-16)

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-64 | ST-01 | 2x Senator Assert engine: Church reaches TC 40 S4, victory S18 — 7+ seasons too fast | Open — ED-572 |
| F-65 | ST-01 | TC 80 PT drift neutralises Varfell Cultural Reformation in all target territories | Open — ED-573 |
| F-66 | ST-01 | Hafenmark Dynastic Proclamation on Crown structurally impossible (Mandate cap PP-174) | Open — ED-583 |
| F-67 | ST-07 | NPC tactic selection formation-unaware; Iron Discipline chosen over Shield Wall vs Cavalry | Open — ED-574 |
| F-68 | ST-06 | Post-combat fieldwork when player fled: access undefined | Open — ED-576 |
| F-69 | ST-07 | Co-Movement Cards 1-15 content not in canonical docs | Open — ED-577 |
| F-70 | ST-07 | TTRPG mass battle melee damage formula not explicitly stated | Open — ED-578 |
| F-71 | ST-05 | Charity Advantage (Church Wealth ≥ rival+2) rarely activates in competitive games | Open — ED-580 |
| F-72 | ST-03 | RS targeting essential for Resistance-2 Chain Contests; not documented | Open — ED-582 |

## New Confirmed Working (sim_stress_batch_2_2026-04-16)

| System | Source | Status |
|--------|--------|--------|
| TC milestone political effects (all five) | ST-01 | ✓ All produce correct effects |
| Obligation → NPC priority tree behavioral constraint | ST-03/09 | ✓ Elegant |
| Zoom In at Phase 3 legal entry point | ST-02 | ✓ Clean |
| BG → TTRPG unit conversion | ST-02 | ✓ Correct |
| General duel (3 exchanges, decisive) | ST-02 | ✓ Calibrated |
| RS targeting breaks Resistance-2 stalls | ST-03 | ✓ Mechanically essential |
| Church TC + RS Rupture pyrrhic collision | ST-10 | ✓ Brilliant design validated |
| Warden expedition as RS stabiliser | ST-10 | ✓ Correctly designed save-world arc |
| Wedge + HeavyCut Cavalry vs Heavy armour | ST-07 | ✓ Shield Wall as correct counter |
| NPC Arc B + Arc A synergistic pressure | ST-08 | ✓ Emergent crisis as intended |

## Provisional Decisions (sim_stress_batch_2_2026-04-16)

| Finding | Provisional Rule | Status |
|---------|-----------------|--------|
| SIM2-01 | Assert → Pontifex-exclusive (ED-572) | Provisional — requires tc_political_redesign_v30 §5.2 revision |
| SIM2-05 | Post-combat fieldwork requires site control (player can't flee and investigate) | Provisional — ED-576 |
| SIM2-08 | Obligation fulfillment: Disposition +1 toward imposing party | Provisional — ED-579 |
| SIM2-12 | Hafenmark Proclamation on Crown impossible under Mandate cap — confirm intended (ED-583) | Provisional — awaiting user |


## New Findings — sim_batch_3_2026-04-16

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM3-01 | TC+TCV compound | Church TCV ≥ 8 met in Seasons 2-4 — not meaningful constraint. Fix: Accord ≥ 3 in 3 non-capital territories added to Church victory. | Open — ED-585 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Assert-Pontifex: TC 40 in Season 12 (vs S4 old system) | SIM-NPC-01 | ✓ 8-season delay confirmed |
| Hafenmark Suppress stalls TC at 41-43 ceiling (max suppression) | SIM-NPC-01 | ✓ Correct structural counter |
| Varfell Cultural Reformation OW reduces TC −1 directly | SIM-NPC-01 | ✓ Working cross-pressure |
| Evidence RS + Authority Doubt Marker combo optimal vs Faith NPCs | SIM-NPC-03 | ✓ Confirmed strategy |
| Social victories → Mandate 3 → Priority 6 → TC clock halts | SIM-NPC-03 | ✓ Cross-system chain works |
| Parliamentary Censure window at Mandate 3 (no TC-65 barrier) | SIM-NPC-03 | ✓ Political domino as intended |
| Companion spec: 9D pool at Military 4, WI=9, Max Wounds 2 | Companion spec | ✓ Calibrated — fragile as intended |
| Departure scene mandatory on non-voluntary departure | Companion spec | ✓ |

### P2 Gaps

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM3-04 | NPC-03 | Arc behavioral state vs Priority 6 override contradiction at Mandate < 3 | Open — ED-586 |
| SIM3-07 | Zoom In | Stability Crisis Zoom In trigger absent | Open — ED-587 |

### Resolved SIM-DEBT

| ID | Description | Status |
|----|-------------|--------|
| SIM-NPC-01 | 6-faction BG simulation with all priority trees | RESOLVED — see sim_batch_3_2026-04-16 §C |
| SIM-NPC-03 | Almud/Himlensendt 3-season arc emergence | RESOLVED — see sim_batch_3_2026-04-16 §D |

### Resolved P1s (per sim_batch_3_2026-04-16)

| ED | Description |
|----|-------------|
| ED-539 | TC + TCV compound validated — Accord ≥ 3 condition added to Church victory |
| ED-545 | Zoom In triggers: 11+ categories, sufficient. New Stability Crisis trigger proposed. |
| ED-551 | Vanguard Assault entry: Priority 2b added |
| ED-555 | companion_specification_v30.md created |
| ED-557 | Companion stat generation formula defined |
| ED-559 | Companion combat AI priority tree defined |
| ED-571 | Companion vs recruited NPC distinction formalized |
| ED-572 | Assert → Pontifex-exclusive confirmed and documented |
| ED-583 | Hafenmark Mandate cap: intended; Grand Contest +1 Mandate (cap 6) as growth path |


## New Findings — sim_batch_4_2026-04-16

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM4-01 | ST-14 | RM Phase 2 T9 holding condition (PT ≤ 1) unreachable — T9 PT 5 maintained by Church | Open — ED-588 |
| SIM4-02 | ST-14 | RM Presence marker mechanics undefined | Open — ED-589 |
| ED-585 | ST-11 applied | Church victory: Accord ≥ 3 condition + TC ≥ 65 gate | Open — ED-590 (apply) |

### Resolved P1

| ED | Status |
|----|--------|
| ED-585 | Resolved — Church victory revision confirmed by simulation |

### Confirmed Working (sim_batch_4)

| System | Source |
|--------|--------|
| Fieldwork structural investigation (4 scenes, Structural) | ST-11 |
| Varfell path ordering: B < A < C (correct timelines) | ST-13 |
| Löwenritter coup: 7 cascading consequences clean | ST-15 |
| Strain 7 Crisis band mass Revolt cascade | ST-16 |
| FR Lock Pull Reversal strategy | ST-17 |
| Companion departure arc: 3 Scars → appeal | ST-18 |
| 30-season generational campaign structure | ST-19 |
| 5-system simultaneous cross-system stress: no conflicts | ST-20 |

### New P2 Gaps

| ID | Description |
|----|-------------|
| SIM4-03 | Accord 3 passive erosion rule absent |
| SIM4-04 | Church Lock trivially reversible (TS 0) — design note needed |
| SIM4-05 | Pull Reversal vs Dissolution not documented as strategy |
| SIM4-06 | Uprising roll TN unspecified — propose TN 7 |
| SIM4-07 | Strain 7 → RS −10 from mass Revolts — add warning |
| SIM4-08 | Church Tribunal halved-resistance too strong for high-pool players |
| SIM4-09 | OW departure appeal → Companion arc transformation not specified |


## New Findings — sim_companions_2026-04-16

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-C-01 | Companion sim | Officer companions near-certain recruited away (Ob 1) without advisory-role counter-incentive | Open — ED-600 |
| SIM-C-15 | Companion sim | 7 of 12 playable NPCs lack arc maps — S20+ behavior entirely GM-emergent | Open — ED-591, ED-592 |

### P2 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-C-06 | Torben sim | Companionship vs BG Loyalty paradox if Coup fires while Torben is companion | Open — ED-594 |
| SIM-C-10 | Almud sim | Almud companion may grant de facto Crown faction control | Open — ED-593 |
| SIM-C-14 | All companions | ~75% companion departure rate by S30 — validate if intended | Open — SIM-COMP-03 |
| SIM-C-16 | Practitioner pairs | Multi-source Knot strain stacking undefined | Open — ED-596 |

### Confirmed Working (sim_companions_2026-04-16)

| System | Source | Status |
|--------|--------|--------|
| Edeyja acquisition structurally coupled to Arc B | SIM-C-11 | ✓ Elegant |
| Vossen departure tied to Church TC 65 — structural anti-Church incentive | SIM-C-03 | ✓ Works |
| Baralta Arc B near-certain when acquired via Evidence | SIM-C-08 | ✓ Correct |
| Dual Hann+Vossen Belief divergence under pressure | SIM-C-04 | ✓ Best social pair |
| Ehrenwall 12D combat validates hard acquisition barrier | SIM-C-07 | ✓ Cost/benefit correct |
| Edeyja Arc C: RS solution and RS drain simultaneously | SIM-C-12 | ✓ Brilliant design |
| Himlensendt companion = controlled/uncontrolled theological bomb | SIM-C-09 | ✓ Intentional |
| Torben blank Conviction = uniquely shapeable | SIM-C-05 | ✓ Only malleable named NPC |

### New SIM-DEBT

| ID | Description | Status |
|----|-------------|--------|
| SIM-COMP-01 | Arc profile sims for Vossen, Hann, Torben, Ehrenwall, Maret Uln (pending ED-592) | OPEN |
| SIM-COMP-02 | Multi-companion Knot strain stacking stress test — 2 practitioner companions concurrent | OPEN |
| SIM-COMP-03 | Companion departure rate calibration: validate ~75% S30 rate | OPEN |
| SIM-COMP-04 | Torsvald full sim (pending ED-591 §2 entry) | OPEN |


## New Findings — sim_npc_as_player_2026-04-16

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| POL-SIM-01 | All faction leaders | Delegation-filtering: delegate reports carry Conviction bias — no mechanic | Open — ED-601 |
| POL-SIM-13 | Vossen | RM has no rank ladder, founding trigger, movement tracker, or pre-founding BG economy | Open — ED-603 |
| POL-SIM-17 | Edeyja | Pre-emergence: no BG economy; warden count tracking absent | Open — ED-604, ED-609 |

### P2 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| POL-SIM-22 | Faction leaders | Scene slate overload at Standing 5 | Open — ED-602 |
| POL-SIM-19 | Torsvald | Expected playable lifespan 12–15 seasons from TS accumulation | Open — ED-605 |
| POL-SIM-18 | Maret Uln | SUC-03 2-season window insufficient for post-Arc-C succession | Open — ED-606 |

### Confirmed Working (NPC-as-player)

| System | Source | Status |
|--------|--------|--------|
| Conviction-obligation loop self-reinforces in calm, breaks in crisis | All faction leaders | ✓ |
| Baralta Suppress obligation mandatory from inside (correct lock-in) | POL-SIM-10 | ✓ |
| Ehrenwall Coup Counter as ethical player tool | POL-SIM-16 | ✓ |
| Torben blank Conviction formation via scene choice | POL-SIM-15 | ✓ |
| Himlensendt Arc C inverts Inquisition tools against himself | POL-SIM-08 | ✓ |
| Vaynard Discovery Events probabilistically unavoidable | POL-SIM-12 | ✓ |
| FAC-02 Torben timeline produces Figurehead gap — POW-01 is expected outcome | POL-SIM-24 | ✓ |

### New SIM-DEBT

| ID | Description | Status |
|----|-------------|--------|
| SIM-POL-01 | Ministry competence decay calibration | OPEN |
| SIM-POL-02 | Torben generational clock vs Coup Counter timing | OPEN |
| SIM-POL-03 | Hann-as-player dual-agenda 30-season sim | OPEN |
| SIM-POL-04 | Edeyja pre-emergence warden season structure | OPEN |


## Arc Expansion v1 — 2026-04-16 (ED-591 through ED-609)

19 arc design proposals — all provisional. Full document: designs/systems/arc_expansion_v1_2026-04-16.md

| Category | Coverage added |
|----------|---------------|
| Cardinal Officers (4) | Full A/B/C arcs for Fortitude/Justice/Prudence/Temperance |
| Ehrenwall (LR) | Full A/B/C + 6-criteria coup evaluation + succession |
| Torsvald (Riskbreakers) | Full A/B/C + TS development arc |
| Vossen / Hann (RM) | Full arc expansions + 3-trajectory Arc C for Vossen |
| Orm (Second Warden) | Full A/B/C including self-sacrifice Arc C |
| Niflhel operatives | Quartermaster + The Quiet One full arcs |
| Almud / Vaynard | Arc skeleton fills + Arc C 3-trajectory (Almud) |
| Environmental conditioners | RS/TC/Strain → systematic NPC arc effects |
| Cross-NPC conditioners | 4 dependency chains across faction boundaries |
| Obligation conditioners | 6 Obligation-event arc triggers |
| Zoom In triggers | 6 new Mandatory + 5 new World-State |
| New mechanics | Mediation contest type; Torben Conviction emergence |

