# Module 11 Report — Provincial Authority + Domain Echo chain + cross-system bindings

**Date:** 2026-05-13
**Session:** Mode G Module 11 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_11_provincial_authority.py`

**Canonical sources read at full depth:**
- `designs/territory/settlement_layer_v30.md` §3.1, §3.3, §8.1

## Summary

Module 11 closes three deferred items:

1. **Provincial Authority side of §3.1** — M5 owned the *subnational management* receive-side (Governor slot); M11 owns the *Provincial Authority issuer-side* (the national-faction-level controller of military deployment, taxation, legal framework, and province-level Domain Actions).
2. **§3.3 grant/revoke from the issuer perspective** — M5's `grant_subnational_management` and `revoke_subnational_management` mutated the receive-side state. M11's `issue_grant_management` and `issue_revoke_management` are the canonical Domain-Action wrappers that gate on Influence-pool vs Ob and apply the canonical penalty schedule.
3. **The Domain Echo chain** — §8.1 explicitly catalogues "Governor → Province → National as Domain Echo chain" as the S17 Scale Transitions impact. M11 implements the chain as pure functional composition: settlement-event → province-effect → national-effect, with each step a pure function of the prior.

## Isolation tests — 30/30 PASS

Highlights:
- T1–T5: Two-tier authority model + alignment predicate (efficient vs tension)
- T6–T9: Grant Ob fixed at 1; Revoke Ob = Influence ÷ 2 round up (validated with Influence 1, 4, 5)
- T10–T14: Domain-Action issuer mechanics — natural-alignment flagging, pool-vs-Ob gating, canonical penalty schedule, failed-action no-cost behavior
- T15–T23: Domain Echo chain — three scale layers; settlement-event echo magnitudes per event type; province-to-national dampening by controlled-province count
- T24–T26: Provincial-Authority tension index — accumulates with negative disposition, decays when aligned, fires transition threshold
- T27: Cross-system surface — every module M1-M11 covers at least one §8.1 system
- T28–T29: Throughline + meta-throughline coverage queryable
- T30: **Emergent revolt-to-national chain.** Crown-controlled REVOLT at S-001 (Valorsmark) with Crown holding 2 provinces: settlement-magnitude -2 → province-effect -2 → national-effect floor(-2 / 2) = -1. **The chain composes from pure functions; the dampening emerges from the province-count divisor.**

## Throughline bindings — М-5 SCALES CONNECT extended

Module 11 produces the strongest М-5 binding so far. The Domain Echo chain IS the canonical scale-connecting mechanism at the institutional-action layer — and unlike M5/M8 which connected scales via *progression accumulation*, M11 connects via *event propagation*.

| Throughline | Title | Module 11 mechanism |
|---|---|---|
| T-15 | Player Progression | Provincial-Authority rung of Stature ladder (Standing 4+ Seat → Domain Actions) |
| T-23 | NPC Arc Emergence | Domain Echo chain IS the canonical "personal arc → faction Domain Echo → political shift → new arc" |
| T-20 | Two Contests | Revoke Management trades Order/Disposition for political control |
| T-26 | Recursion as Setting Structure | Domain Echo chain IS recursion-of-dynamic-across-scales |

Plus meta:
- **М-5 SCALES CONNECT** — PRIMARY (extends M5/M8/M9). Strongest binding.
- **М-4 INSTITUTIONS STAKE POSTURES** — SECONDARY (extends M3/M4/M5). PA IS the institutional-posture slot per faction.

## Cumulative throughline coverage after M11

| T-NN | Title | Primary М | Modules binding | Strength |
|---|---|---|---|---|
| T-01 | Everything Is Thread | М-3 | M6 | primary |
| T-03 | Inseparability | М-3 | M10 | secondary |
| T-04 | MS Decay | М-1 | M9 | primary |
| T-05 | CI Accumulation | М-1 | M9 | primary |
| T-06 | IP Accumulation | М-1 | M9 | primary |
| T-07 | Turmoil | М-1 | M9 | primary |
| T-08 | Church Rendering Reinforcement | М-4 | M4 | primary |
| T-11/15a/15b/15c | Faction substrate-postures | М-4 | M5 | primary |
| T-15 | Player Progression | М-5 | M5, M8, **M11** | primary + extension |
| T-18 | Radiation Gradient | М-2 | M1, M2 | secondary |
| T-19 | Southernmost Hidden Front | М-2 | M2, M7 | secondary |
| T-20 | Two Contests | М-6 | M7, M8, **M11** | secondary throughout |
| T-22 | Belief Lattice | М-6 | M4 | secondary |
| T-23 | NPC Arc Emergence | М-5 | M6, M8, **M11** | primary mechanism wired |
| T-25 | Generational Arc | М-5 | M8, M9 | substrate + clock |
| T-26 | Recursion as Setting Structure | М-5 | **M11 NEW** | secondary |
| T-27 | Effects Real Explanation Wrong | М-4 | M10 | primary |
| T-30 | Information Asymmetry | М-8 | M6, M10 | secondary |

**Total: 18 distinct throughlines bound across 11 modules.** Module 11 added T-26 as a new binding (Recursion as Setting Structure) and extended T-15, T-20, T-23.

## Meta-throughline status after M11

| Meta | Primary bindings | Status |
|---|---|---|
| М-1 PRESSURE IS CONTINUOUS | M9 | bound |
| М-2 GEOGRAPHY HOLDS PRESSURE | M2, M7 | covered |
| М-3 SUBSTRATE GROUNDS ALL | M1, M2, M6 | covered |
| М-4 INSTITUTIONS STAKE POSTURES | M3, M4, M5, M11 | strongest tally |
| **М-5 SCALES CONNECT** | M5, M8, **M11** | strongest binding (Domain Echo chain) |
| М-7 BORROWINGS OPERATIONAL EXTENSIONS | M10 | bound |
| М-6 CHOICE IS FORCED | — secondary in M7/M8/M11 | character-layer; structurally expected gap |

**Only М-6 remains primary-unbound** — structurally expected, since М-6 is character-layer scope (forced-choice personal-scale throughlines T-12/T-13/T-17). Module 13 audit will confirm this is appropriately covered by another sim.

## §3.3 grant/revoke mechanics — issuer-side data model

```
GRANT_MANAGEMENT_DOMAIN_ACTION_OB = 1            # §3.3 administrative Ob
REVOKE_MANAGEMENT_OB_DIVISOR = 2                 # §3.3 "Influence ÷ 2, round up"
REVOKE_MANAGEMENT_ORDER_PENALTY = 1              # §3.3 "Order -1"
REVOKE_MANAGEMENT_DISPOSITION_PENALTY = 2        # §3.3 "Disposition -2"

grant_ob() -> int = 1
revoke_ob(subnational_influence) -> int    # ceil-divide

issue_grant_management(...) -> DomainActionResult
issue_revoke_management(...) -> DomainActionResult
```

The issue_* functions:
- Roll the Influence-pool vs Ob
- On success: mutate TwoTierAuthority's governor slot
- On failure: return DomainActionResult with reason; **no penalties applied** (validated by T14)
- On Revoke success: apply Order -1 and Disposition -2 per §3.3

## Domain Echo chain — pure functional composition

```
domain_echo_settlement_to_province(event, sid, province_id) -> Optional[Step]
domain_echo_province_to_national(magnitude, province_id, faction_id, province_count) -> Optional[Step]
domain_echo_chain(...) -> List[Step]
```

Echo magnitudes (settlement → province):
- LOCAL_REVOLT: −2
- FAMINE_ECONOMIC_COLLAPSE: −1
- FLOURISHING_FESTIVAL: +2
- RAID_OR_SIEGE: −1
- GOVERNANCE_TRANSITION_RM: 0 (neutral, no echo)

National-scale dampening: `national_magnitude = province_magnitude // controlled_provinces_count`. Single-province factions feel province events directly; multi-province factions average.

This is **pure functional composition** — no Domain Echo manager object. Each step is a function of the prior; the chain is just `[settlement_step, national_step]` filtered for None.

## Cross-system surface bindings (M11 supplies for Module 13)

Each module M1-M11 maps to at least one §8.1 system:

| Module | §8.1 Systems Touched |
|---|---|
| M1 | S03 Geography |
| M2 | S03 Geography, S07 Victory |
| M3 | S03 Geography, S06 Faction Layer |
| M4 | S08 CI, S10 NPC, S06 Faction Layer |
| M5 | S06 Faction Layer, S10 NPC, Player Agency |
| M6 | S10 NPC, S04 Clocks |
| M7 | S09 Military, S15 Mass Combat |
| M8 | Player Agency, S17 Scale Transitions |
| M9 | S04 Clocks, S07 Victory |
| M10 | S10 NPC, S14 Fieldwork, S17 Scale Transitions |
| M11 | S06 Faction Layer, S17 Scale Transitions, Player Agency |

**§8.1 coverage gap remaining:** S08 CI is touched only by M4. Module 12 (faction integration) will deepen the CI binding by wiring Mass Seizure Declaration cascade at CI=100. S15 Mass Combat is M7-only; Module 12 wires the cross-system surface to mass_battle_v30 sim.

## Findings status after M11

No new findings this session. M11's bottom-up approach reused canonical mechanics from M5 (`grant/revoke_subnational_management`) and M6 (`SettlementEvent` enum) — no fresh design-doc reads surfaced new drift.

| Family | Surfacings | Status |
|---|---|---|
| Type-taxonomy drift | F1, F7, F10, F11, F12, F14, F18 | 7 surfacings, one editorial pass closes all |
| Documentation drift | F2, F13, F14, F16, F17 | 5 surfacings |
| Intentional asymmetries | F8, F9 | informational |
| Other | F3 (resolved), F4 (partial), F5, F6 (Mode-C blocker), F15 | misc |

## Module 11 data model

```
AuthoritySlot (enum)                            # PROVINCIAL_AUTHORITY, SETTLEMENT_GOVERNOR
PROVINCIAL_AUTHORITY_DOMAINS = [...]            # 4 canonical domains
SETTLEMENT_GOVERNOR_DOMAINS = [...]             # 4 canonical domains

@dataclass TwoTierAuthority                     # settlement authority state
authority_alignment(authority) -> 'efficient' | 'tension'

grant_ob() -> int                               # always 1
revoke_ob(subnational_influence) -> int        # ceil(influence / 2)
issue_grant_management(...) -> DomainActionResult
issue_revoke_management(...) -> DomainActionResult

ScaleLayer (enum)                               # SETTLEMENT, PROVINCE, NATIONAL
@dataclass DomainEchoStep
domain_echo_settlement_to_province(...) -> Optional[Step]
domain_echo_province_to_national(...) -> Optional[Step]
domain_echo_chain(...) -> List[Step]            # pure functional composition

@dataclass ProvincialAuthorityRelationship      # disposition + tension_index
PA_TENSION_TRANSITION_THRESHOLD = 3
accumulate_tension_per_season(rel) -> bool      # returns True on threshold crossing

systems_affected_by_module(idx) -> List[str]    # cross-system surface for M13 audit

THROUGHLINE_COVERAGE_BY_THIS_MODULE              # T-15, T-23, T-20, T-26
META_THROUGHLINE_COVERAGE_BY_THIS_MODULE         # М-5 primary, М-4 secondary
```

## Cumulative status after M11

- **11 modules verified · 337 isolation tests · ~225 ledger entries · 18 findings (1 resolved, 1 partial, 16 open)**
- **All committed to GitHub at `jordanelias/ttrpg/main`**
- **18 distinct throughlines bound across 11 modules**
- **5 of 6 primary meta-throughlines primary-bound; only М-6 remains primary-unbound (character layer)**
- **2 modules remaining**: M12 (faction integration), M13 (integration runner + NERS audit)

## Next session — Module 12 (Faction integration)

Module 12 wires the cross-system surface §8.1 catalogues but did not deeply bind in M1-M11. Specifically:

- **Mass Seizure Declaration cascade at CI=100** (S08 CI deep binding)
- **mass_battle_v30 Part E consequences** (S15 Mass Combat — MS/Strain/IP peninsula-wide effects from battles)
- **Altonian Vanguard advance mechanics** (S09 Military — currently surfaced only at constant level by M9)
- **faction stat-sheet integration** — bind Module 8's provisional renown_delta + faction_standing_delta signals to canonical Mandate/Influence/Wealth/Military/Stability changes
- **Domain Action resolution layer** — full Domain Action pool/Ob system; M11 surfaced Grant/Revoke as Domain Actions but the broader Domain Action system is M12

Likely to surface 1-2 more findings as we cross into Module 12's broader canonical surface. **1 module remaining (M13 integration runner)** after M12.
