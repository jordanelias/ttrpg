# Coverage Matrix Archive — v17 Modules M1-M5 (2026-05-16)

Detailed per-module testing surface for M1-M5 of the v17 strategic-sim integration plan. Archived from `tests/coverage_matrix.md` to keep the active file under the 8k-token coverage_matrix size cap.

Active coverage matrix retains M6 + M7 detail (most recent modules) plus 1-line summaries for M1-M5.

Companion: integration_plan_v3 §5 Phase 1 (M1-M5 source spec).

---

### M1 Church Settlement Infrastructure (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest (74b7f29) — Module 1 of 7 in strategic-sim integration plan; canonical primitives for four-axis Church infrastructure |
| Module scope | Settlement dataclass, 37-settlement registry from settlement_layer §2.1, Seizure Ob formula (10 − PT − infra, floor 1, −4/settlement cap), SW-weighted Piety Yield, Mass Seizure declaration P((CI−60)/40)^3.3, Parish Order yields, Pastoral Assumption eligibility, Ascendant PT drift, Unification phase tracking |
| Test groups | T1 registry integrity (24 checks) / T2 starting state (38) / T3 Seizure Ob boundaries (9) / T4 PT generation (12) / T5 CI generation (8) / T6 Inquisitor/Parish/Pastoral (9) / T7 Mass Seizure mechanics (7) / T8 Unification (7) / T9 PT drift (10) |
| Result | **128 PASSED, 0 FAILED** |
| Canonical sources verified | settlement_layer_v30 §1.5 §1.6 §1.7 §2.1 §2.2 (full read), ci_political_v30 §1 §2.1 §2.2 (full read), victory_v30 §3.2 (full read), mc_v15.py PT_MAP + ADJACENCY (full read), campaign_architecture_v30 (full read), params/bg/victory.md (full read) |
| Ledger | 49 entries citing each constant to canonical source + section + quoted text |
| Provisional assumptions held | 6 (ASSUMPTION_ONE..ASSUMPTION_SIX corresponding to GAP-A..GAP-F): registry source-of-truth, starting infrastructure seeding, playable territory count, Cathedral adjacency stacking rules, PT drift granularity, Warden Cooperation gate. All documented in ledger.provisional_assumptions; held for Jordan ratification before integration sim runs. |
| Known canonical conflicts | (A) settlement_layer_v30 §2.1 vs valoria_geography_v30.yaml — different settlement-registry schemas; M1 sourced from §2.1; geography YAML needs editorial migration. (B) Compliance shows canon/editorial_ledger.yaml auto-fixable but cc052aa landed clean (likely cache/eventual-consistency artifact). |
| Files | tests/sim/v17-integration/m1_church_infrastructure.py + m1_church_infrastructure_tests.py + m1_sim_verification_ledger.json |
| Next module | M2 CI Political Revision (depends M1) — CI milestones 55/65 verification, revised Mass Seizure cross-territory, ±5/season CI cap audit |

### M2 CI Political Revision (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest (74b7f29) — Module 2 of 7; CI cap mechanics, milestone effects, political legitimacy modifiers |
| Module scope | Seasonal CI cap (±5/season total, ±3 from Domain Actions), CI milestones 28/40/55/65/80/100 with effect queries, Bonus Dice floor(CI/20) and Obstacle Modifier floor(CI/30), Hafenmark suppress (-1 at L≥4), Unification simultaneous-seizure target-list generator (Chapel+ ∩ Church Prominent), Accord-on-Seizure-success formula |
| Test groups | T1 constants (11 checks) / T2 seasonal cap (5) / T3 DA sub-cap (5) / T4 mixed sources (6) / T5 hard bounds (3) / T6 Bonus Dice + Obstacle Modifier (15) / T7 milestone effects (17) / T8 Hafenmark + Unification targets (10) / T9 Accord (6) |
| Result | **78 PASSED, 0 FAILED** |
| Canonical sources verified | ci_political_v30 §2 + §3 + §4.1 + §7.1 (full read), victory_v30 §3.2 (full from M1 session), faction_layer_v30 §5 (full read for default slot cost), mc_v15 mass_seizure_check (Accord formula source) |
| Ledger | 26 entries; cross-references M1 module constants for Religious-Building / Prominence / PLAYABLE_TERRITORIES |
| Provisional assumptions held | 5 (ASSUMPTION_ONE..ASSUMPTION_FIVE): source classification by caller, sub-cap precedence ordering, threshold-inclusive milestone semantics, action-classification responsibility, Unification target composition |
| Dependencies | Module 1 (settlement registry, has_any_church_building, PLAYABLE_TERRITORIES, SPIRITUAL_WEIGHT) |
| Files | tests/sim/v17-integration/m2_ci_political_revision.py + m2_ci_political_revision_tests.py + m2_sim_verification_ledger.json |
| Next module | M4 Unit State Management (foundational, no deps) or M5 Settlement-Territory Aggregation (depends M1); per manifest M3 depends on M4 |

### M4 Unit State Management (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest — Module 4 of 7; foundational module, blocks M3 |
| Module scope | Per-faction unit roster (defaultdict[territory_id][unit_class] = count), 9-class schema with semantics-partial split (3 active: Levy/LightInf/HeavyInf, 6 reserved: Cavalry/Archer/Crossbow/Sling/Artillery/KnightsTemplar), UNIT_STATS dict baked from §B.2 (Martial/Endurance/Discipline/Health/BG_Dmg/TTRPG_Dmg/Armour/Anti-Armour/Volley per class), Muster mints Levy in single territory, commit_to_battle with adjacent-to-target adjacency model (option b), apply_battle_losses with auto-prune zero counts, JSONL-safe to_dict/from_dict/to_json/from_json round-trip, pool_contribution helper (Σ count×Martial) for M3's resolve_battle §B.3 Step 3 |
| Test groups | T1 schema (16 checks) / T2 canonical stat values (14) / T3 anti_armour+volley flags (11) / T4 basic ops (12) / T5 adjacency commitment (11) / T6 serialization round-trip (9) / T7 pool_contribution (8) |
| Result | **95 PASSED, 0 FAILED** |
| Canonical sources verified | mass_battle_v30 §B.2 (BG Unit Stats table, full read 63.1k) + §B.3 Step 3 (pool formula), integration_plan_v3 §5 Phase 2c (defaultdict schema, active/reserved split, option-b movement model, JSON serialization), params/mass_combat.md (33.0k full read) |
| Ledger | 22 entries; per-class stat-block citations to §B.2 rows, schema/active/reserved citations to integration_plan §5 Phase 2c |
| Provisional assumptions held | 5 (M4_ASSUMPTION_ONE..FIVE): adjacent-to-target movement model (option b), active-class-only Muster/Commit enforcement, single-territory single-class Muster default Levy, per-faction roster (not per-world), aggregate-count loss semantics (no per-token identity) |
| Dependencies | none (foundational) — Module 3 (Mass Battle Resolution) will consume this |
| Files | tests/sim/v17-integration/m4_unit_state.py + m4_unit_state_tests.py + m4_sim_verification_ledger.json |
| Next module | M3 Mass Battle Resolution (now unblocked) or M5 Settlement-Territory Aggregation (depends M1 ✓) |

### M3 Mass Battle Resolution (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest — Module 3 of 7; canonical 6-step BG battle resolution + tactic cards + Fort dice |
| Module scope | Pure primitives 6-step resolution per mass_battle_v30 §B.3 + military_layer §2.1-§2.2: compute_pool (Σ Martial + floor(Mil/2) + Fort), apply_tactic_cards (disposition routing for 4 shared cards mechanically + 16 faction-specific registered for M6 routing), roll_pool (d6 ≥4 BW success per mc_v15 convention), check_route (BW Discipline check Ob 2), apply_damage_lowest_martial_first (deterministic weakest-first AI policy), resolve_battle (full BattleResult dataclass), validate_tactic_card + cards_available_to_faction |
| Test groups | T1 constants (8 checks) / T2 pool computation (7) / T3 tactic card dispositions (9) / T4 roll mechanics (8) / T5 margin outcomes (8) / T6 damage allocation (5) / T7 tactic card registry (10) / T8 full resolve integration (8) |
| Result | **63 PASSED, 0 FAILED** |
| Canonical sources verified | mass_battle_v30 §B.1 + §B.3 + §B.4 (full read), military_layer_v30 §2.1 + §2.2 (full read 26.7k), integration_plan_v3 §5 Phase 2b BattleResult schema, mc_v15 quasibinomial_successes convention (BW d6 ≥4 success threshold) |
| Ledger | 23 entries; canonical citations for TN, MARGIN_DECISIVE, accord/military/stability deltas, pool formula, Fort-dice-to-defender rule, all 20 tactic cards with disposition routing |
| Provisional assumptions held | 5 (M3_ASSUMPTION_ONE..FIVE): faction-specific card mechanical effects deferred to M6, RNG explicit for determinism, weakest-first damage policy, pool-modifier disposition simplification, every-loss-checks-route morale trigger (compatible with M4 aggregate-count semantics) |
| Dependencies | Module 4 (UnitRoster, UNIT_STATS, pool_contribution) — now unblocked |
| Files | tests/sim/v17-integration/m3_mass_battle.py + m3_mass_battle_tests.py + m3_sim_verification_ledger.json |
| Theoretical route rates verified | Levy (D=1) always routes; LightInf (D=3) ~50%; HeavyInf (D=4) ~31% per Binomial(4, 0.5) tail; Cavalry (D=5) ~19%; KnightsTemplar (D=6) ~11% |
| Outstanding for M6 integration | Faction-specific tactic card mechanical effects (Crown Royal Guard +3D, Church Crusade Fervour Discipline-exempt, Varfell Stratagem initiative-inversion, Hafenmark Mercenary Surge +2 units, etc.) require overlay/hook architecture not present in M3 primitives layer |
| Next module | M5 Settlement-Territory Aggregation (depends M1 ✓) or M6 Faction Action Expansion (depends M1-5) |

### M5 Settlement-Territory Aggregation (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest — Module 5 of 7; settlement governance state, §3.2 governance actions, §4.3 events, ED-683 RM cell resilience, settlement → territory aggregation |
| Module scope | SettlementGovernance + SettlementEvent dataclasses (separate from M1.Settlement per M5_ASSUMPTION_ONE); §3.2 governance_action_ob formulas for Develop/Fortify/Pacify/Administer; full §4.3 events table (Famine on P=0, Revolt on O=0 with garrison-suppression, Raid on D=0+hostile, Flourishing at O=5+P=4, Mine surplus at P=3+, Fortress garrison-check Ob 2 on hostile, Cathedral religious event on CV change, Governance Transition 3-mode choice on RM takeover, Consensus Delay on RM-governed emergency); ED-683 RM Cell Resilience (3-settlement threshold → +1 Ob suppression); aggregate_order_to_accord floor-mean policy + aggregate_prosperity_to_wealth continuous rate; province_mine_treasury_contribution flat-per-Mine; province_settlement_summary helper |
| Test groups | T1 constants (16 checks) / T2 §3.2 Ob formulas (18) / T3 SettlementGovernance dataclass + bounds + apply_governance_action (15) / T4 Famine (4) / T5 Revolt + garrison suppression (8) / T6 Mine/Fortress/Flourishing/Cathedral events (10) / T7 RM Cell Resilience boundary tests (5) / T8 aggregation Order→Accord + Prosperity→Wealth (6) / T9 Governance Transition 3-mode + Consensus Delay (12) / T10 province_settlement_summary (6) |
| Result | **95 PASSED, 0 FAILED** |
| Canonical sources verified | settlement_layer_v30 §3.1 (Two-Tier Authority), §3.2 (Governor Assignment table with Pool/Ob/Effect), §3.3 (Subnational governance + RM Cell Resilience ED-683), §4.3 (Settlement Events table — full); integration_plan_v3 §5 Phase 5 (settlement state integration) |
| Ledger | 28 entries; per-event-row citations to §4.3 table, governance-action Ob formulas to §3.2 table, RM resilience to §3.3 ED-683 |
| Provisional assumptions held | 5 (M5_ASSUMPTION_ONE..FIVE): governance state in separate dataclass (preserves M1 narrow scope), floor-mean aggregation policy for Order→Accord (canon doesn't specify), boolean RM Presence marker, event records (not state mutation), dual Prosperity→Wealth surfaces (continuous rate + flat-per-Mine) |
| Dependencies | Module 1 (SETTLEMENT_REGISTRY, territory_settlements, PLAYABLE_TERRITORIES, RB_CATHEDRAL constants) |
| Files | tests/sim/v17-integration/m5_settlement_aggregation.py + m5_settlement_aggregation_tests.py + m5_sim_verification_ledger.json |
| Next module | M6 Faction Action Expansion (depends M1-5) — now unblocked |

