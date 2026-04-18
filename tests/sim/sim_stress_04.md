# Simulation Report: SIM-STRESS-04
## Date: 2026-04-04
## Scenarios (randomized): hybrid_tc_seizure_at_limit, combat_feint_chain_initiative_steal,
##   combat_stamina_breath_decision, hybrid_pi_revolt_cascade, combat_group_fibonacci_three_way,
##   mass_battle_command_1_edge_cases
## Simulator Modes: A, C, D, G, M

---

## FINDINGS

### Scenario 1: TC Seizure at Limit
| F-S4-01 | Design note | Piety DA (PP-263) breaks TC lock; ~2-3 TC/season; intended |
| F-S4-02 | Design note | Parliamentary counter (70%) vs Church seizure (32%); high-value territories near-impregnable |
| F-S4-03 | Design note | Valorsplatz effective seizure rate ~9.5%/season with active resistance |
| F-S4-04 | Note | Stability 4 = reduced capacity; Piety DA still available; consistent |

### Scenario 2: Feint Chain Initiative
| F-S4-05 | P2 → PP-276 | Initiative stays with holder when both succeed at different priorities |
| F-S4-06 | P2 → PP-277 | Feint -2D = ceiling on Defence allocation, not pool reduction |
| F-S4-07 | Design note | Feint chain risk profile correct; PP-238 sound |

### Scenario 3: Stamina Breath Decision
| F-S4-08 | P2 → PP-275 | Stamina max not stated; capped at base value |
| F-S4-09 | Design note | Preemptive Breath suboptimal; tactical tension working |
| F-S4-10 | Design note | Out-of-Breath recovery is correct use case; design correct |

### Scenario 4: PI Revolt Cascade
| F-S4-11 | Design note | 84% failure rate at Stability 3, Ob 2, 2-die pool; deliberate |
| F-S4-12 | P2 | Positive PI feedback loop; no internal brake |
| F-S4-13 | P2 | Recovery condition near-impossible during crisis |
| F-S4-14 | Design note | PI=10 GM event correct for systemic collapse |

### Scenario 5: Fibonacci Three-Way
| F-S4-15 | Design note | Fibonacci Config 1 dominates; correct incentive structure |
| F-S4-16 | P2 → PP-274 | Multi-engagement target pool split unspecified |
| F-S4-17 | Design note | Defensive split vs two attackers: near-zero damage; correct |
| F-S4-18 | Design note | Fibonacci correctly incentivizes concentrated force |

### Scenario 6: Command=1 Edge Cases
| F-S4-19 | Design note | Command 1 = 2-dice flat pool; design axiom confirmed |
| F-S4-20 | Design note | Command 1 vs Command 5 = one-exchange battle; confirmed |
| F-S4-21 | P1 → PP-273 | No minimum mass battle pool; Discipline penalty can hit 0 |
| F-S4-22 | P1 → PP-273 | Command=0 post-death: 0-dice pools; reinforces ED-176 |

---

## RESOLVED THIS SESSION: PP-273–277 (5 patches applied)
## PROVISIONAL: ED-174 (PI cascade brake — user confirmation needed)
## SIM-DEBT: SIM-DEBT-05 CLOSED (prior session), SIM-DEBT-06 open (Dissonant effects)
