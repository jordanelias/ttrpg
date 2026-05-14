# Module 10 Report — Dissolution emergence + POI templates + system impact catalogue

**Date:** 2026-05-13
**Session:** Mode G Module 10 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_10_dissolution.py`

**Canonical sources read at full depth:**
- `designs/territory/settlement_layer_v30.md` §4.6, §4.7, §4.8, §4.9, §8.1, §8.2

## Summary

Module 10 closes two structural gaps in one session:

1. **Emergence-from-governance-failure surface** — the §4.7/§4.8/§4.9 "Niflhel Dissolution" mechanics. When governance fails, the substrate produces NEW emergent surfaces (black markets, intel brokers, thread sites), not just degradation. The player retains an option set even from failure. This is the canonical case of **М-7 BORROWINGS ARE OPERATIONAL EXTENSIONS** (now primary-bound for the first time).

2. **§8.1/§8.2 audit catalogue as queryable data** — Module 13's integration audit needs the 11 system-impact predictions + 6 invariants surfaced as queryable Python structures, not just design-doc prose. M10 supplies both.

Plus the §4.6 Settlement POI Template depth-axis content for downstream fieldwork integration.

## Isolation tests — 27/27 PASS

Highlights:
- T1–T6: Black market emergence/disappearance predicates + half-unit accrual
- T7–T10: Intel broker placement predicates (Prosperity ≥ 3 AND (no governor OR governor stability ≤ 2))
- T11–T14: Thread Exploitation Site presence + harvest mechanics (RS −0.5 / Wealth +1)
- T15–T20: POI template canonical coverage + F18 fallback handling
- T21–T24: §8.1/§8.2 audit catalogue queryability
- T25–T26: Throughline + meta-throughline coverage tables
- **T27: Emergent cross-module chain — governance failure → black market emergence.** Starting at Order=2 with governor, sim runs M9's `unmanaged_settlement_tick` twice (Order 2→1→0). M10's `predicate_black_market_emerges` was False at the start (Order 2, has_governor=True) and True at the end (Order 0, has_governor=False). **Pure-predicate composition across M9 and M10 with no authored coupling.**

## Throughline bindings — М-7 primary closes second meta-throughline gap

| Throughline | Title | Module 10 mechanism |
|---|---|---|
| **T-27** | Effects Real, Explanation Wrong | Black markets + intel brokers: official institutional framing (governance crisis) vs underground operational reality (Wealth +0.5 from illicit trade) |
| **T-30** | Information Asymmetry as Core Mechanic | Intel broker placement extends M6's `attempt_niflhel_detection` |
| **T-03** | Inseparability | Thread Exploitation Sites: peninsula-level RS affected by site-level harvest |

### Meta-throughline progression

After M10, the meta-throughline primary-binding map looks like:

| Meta | Primary bindings | Status |
|---|---|---|
| М-1 PRESSURE IS CONTINUOUS | M9 | bound (M9) |
| М-2 GEOGRAPHY HOLDS PRESSURE | M2, M7 | covered |
| М-3 SUBSTRATE GROUNDS ALL | M1, M2, M6 | covered |
| М-4 INSTITUTIONS STAKE POSTURES | M3, M4, M5 | covered |
| М-5 SCALES CONNECT | M5, M8 | covered |
| **М-7 BORROWINGS ARE OPERATIONAL EXTENSIONS** | **M10** | **NEWLY BOUND** |
| М-6 CHOICE IS FORCED | — | character-layer; structurally expected gap |

**Only М-6 remains primary-unbound.** This is structurally appropriate for the settlement-management sim — М-6 is the character-layer scope (forced-choice personal-scale: Practitioner Arc, Certainty Journey, Companion Moral Mirror — all T-12/T-13/T-17).

## F18 NEW — POI template gap (seventh type-taxonomy drift surfacing)

§4.6 Settlement POI Templates table contains exactly 8 rows: Seat / City / Town / Fortress / Port / Cathedral / Mine / Outpost. The §2.1 extra types (Village / Fortress-City / Cathedral-City) have **no canonical POI template**.

Module 10 provisionally maps Village → Town POI template (closest semantic match); Fortress-City and Cathedral-City are left **unmapped** (`effective_poi_template_for` returns None) rather than silently reconciled.

**This is the SEVENTH distinct surfacing of the type-taxonomy drift family** (F1, F7, F10, F11, F12, F14, **F18**). The audit pattern crystallizes further:

| Surfacing | Document section | What's missing |
|---|---|---|
| F1 | settlement_layer_v30 §1.2 vs §2.1 | Extra types not in canonical-eight |
| F7 | §1.4.1 facility capacity matrix | Extra types absent |
| F10 | §3.2 governor eligibility table | Extra types absent |
| F11 | §3.3 subnational alignment | Extra types + Guilds market reference |
| F12 | §4.5 Local Actor counts | Extra types absent |
| F14 | §5.1 + adjacency §3 examples | Pre-PP-726 S-IDs |
| **F18** | **§4.6 POI templates** | **Extra types absent** |

**One editorial pass closes all seven findings.** This is now the highest-impact pending editorial.

## §8.1 system impact catalogue — surfaced as data

Module 10 encodes the §8.1 11-row table as `SYSTEM_IMPACTS_FROM_SETTLEMENT_LAYER: List[SystemImpact]`. Each entry includes the system name, impact description, and `ImpactSeverity` enum value (LOW/MODERATE/SIGNIFICANT).

Severity distribution:
- **Significant:** 1 (S09 Military)
- **Moderate:** 7 (S03 Geography, S06 Faction Layer, S07 Victory, S10 NPC, S15 Mass Combat, S17 Scale Transitions, Player Agency)
- **Low:** 3 (S04 Clocks, S14 Fieldwork, Companions)

Module 13 will consume this catalogue to verify that **each of the 11 systems' actual impact in the simulation matches the canonical §8.1 prediction**. The match is itself an audit signal — divergence indicates a design-doc / simulation drift.

## §8.2 invariants — surfaced as data

Module 10 encodes the §8.2 six-item invariant list as `SYSTEM_INVARIANTS: List[str]`. Each invariant is a constraint Module 13 will verify the sim respects:

1. Province-level mechanics operate at province level
2. Personal-scale mechanics operate at individual level
3. Dice engine / pool construction / Ob system / degree table unchanged
4. NPC Stance Triangles, Resonant Styles, Conviction Scars unchanged
5. MS/CI/IP function unchanged (only IP rate adjusted)
6. Calamity radiation operates at province level

These are **architectural commitments** the sim must not violate. Module 13's integration audit will check each.

## Bottom-up emergent pattern continued

Module 10's three dissolution mechanics follow the same atomic-predicate pattern established in M6 + reinforced in M7/M9:

- `predicate_black_market_emerges(stats, has_governor) -> bool` — pure function of state
- `predicate_black_market_disappears(stats) -> bool` — pure inverse predicate
- `predicate_intel_broker_emerges(stats, has_governor, governor_stability) -> bool`
- `predicate_thread_exploitation_site_present(thread_proximity) -> bool`

No "dissolution manager" object owns the emergence; the predicates are evaluated independently and the effects (half-unit accrual, harvest yields) are pure-state mutators. Module 9's per-season Accounting hook will integrate these in Module 13 by adding the dissolution-tick step.

## Findings status after M10

| ID | Status | Module | Type |
|----|--------|--------|------|
| F1 | open | M1 | Canonical type drift |
| F2 | open | M1 | Stats schema |
| F3 | resolved | M2 | (PP-726 §2.1) |
| F4 | partial | M2 | Granularity (F6 blocks) |
| F5 | open | M2 | Edge-count math |
| F6 | open (Mode-C blocker) | M2 | Intra-YAML S-ID drift |
| F7 | open | M3 | §1.4.1 omits extras |
| F8 | open (info) | M4 | §1.5/§1.6 asymmetry |
| F9 | open (info) | M5 | Pacify formula |
| F10 | open | M5 | §3.2 omits extras |
| F11 | open | M5 | §3.3 Guilds Market ref |
| F12 | open | M6 | §4.5 omits extras |
| F13 | open | M6 | §4.5 prose pre-rebuild |
| F14 | open | M7 | §5.1 stale S-IDs |
| F15 | open | M7 | §2.2 omits City |
| F16 | open (info) | M8 | §4.5/§4.6 stale T-NN |
| F17 | open (info) | M9 | clock_registry vs §7.1 IP rate |
| **F18** | **open** | **M10** | **§4.6 omits extras (7th type-taxonomy surfacing)** |

**Type-taxonomy drift family: 7 surfacings (F1, F7, F10, F11, F12, F14, F18) — one editorial pass closes all seven.**
**Documentation drift family: 5 surfacings (F2, F13, F14, F16, F17) — one refresh pass closes all five.**

## Cumulative status after M10

- **10 modules verified · 307 isolation tests · ~215 ledger entries · 18 findings (1 resolved, 1 partial, 16 open)**
- **All committed to GitHub at `jordanelias/ttrpg/main`**
- **5 of 6 primary meta-throughlines now primary-bound** (М-1, М-2, М-3, М-4, М-5, М-7); only М-6 remains primary-unbound (structurally expected)
- **3 modules remaining** before Module 13 integration runner

## Next session — Module 11 (Provincial Authority + cross-system bindings)

Force-full read: settlement_layer_v30 §3.1 (Provincial Authority side that M5 deferred), faction_politics_expanded_v1 (PP-660 ladder cross-reference). Module 11 will:
- Wire the Provincial Authority (national-faction-level) side of §3.1 dual-tier governance — M5 owned the subnational side; M11 owns the national side
- Bind S03..S17 cross-system surface that §8.1 catalogues
- Provincial Authority Domain Action interface (deferred from M5)
- settlement_to_province aggregation deeper than M2's `province_accord_from_settlements`

**2 modules remaining after M11** (M12 faction integration + M13 integration runner).
