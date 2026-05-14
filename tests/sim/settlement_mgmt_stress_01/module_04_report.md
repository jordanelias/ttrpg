# Module 04 Report — Church / parish / pastoral

**Date:** 2026-05-13
**Session:** Mode G Module 4 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_04_church.py`

**Canonical sources read at full depth:**
- `designs/territory/settlement_layer_v30.md` §1.5, §1.6, §1.7

## Summary

Module 4 adds Church's four-axis settlement infrastructure (§1.5), the Geneva-trap Parish Stability bonus (§1.6), and the Pastoral Assumption Domain Action (§1.7) to the player-action loop. **Six new improvement actions** land in the action surface:

- `install_religious_building(Chapel | Church | Cathedral)` — Axis 1 (mutually exclusive; upgrade replaces prior tier)
- `install_templar_station` — Axis 2 (binary)
- `install_inquisitor_base` — Axis 3 (binary)
- `install_church_governor` — Axis 4 (binary)
- `install_church_governor(is_pastoral_assumption=True)` — §1.7 special path with Ob 1 preconditions
- `accrue_parish_bonus_per_season` — Module 9 timeline hook for §1.6 Chapel half-Order accumulator

## Isolation tests — 25/25 PASS

| # | Test | Result |
|---|------|--------|
| T1 | Four axes default None / False / False / False | PASS |
| T2 | ReligiousBuilding enum has exactly 4 tiers | PASS |
| T3 | PT half-unit table matches §1.5 (Chapel 1, Church 2, Cathedral 4) | PASS |
| T4 | Cathedral adjacent-territory PT bonus exists | PASS |
| T5 | Chapel install — no installation Order delta | PASS |
| T6 | Church install — +1 Order one-time at installation | PASS |
| T7 | Cathedral install — +1 Order one-time + order-decay-reduction structural | PASS |
| T8 | Order clamps at STAT_MAX on install | PASS |
| T9 | Reject same-tier install (already_installed) | PASS |
| T10 | Upgrade Church → Cathedral applies new Cathedral bonuses | PASS |
| T11 | Templar install (binary) | PASS |
| T12 | Templar double-install rejected | PASS |
| T13 | Inquisitor install (binary) | PASS |
| T14 | §1.5 seizure-Ob modifier caps at −4 (Cathedral 2 + Templar 1 + Inquisitor 1 + Governor 2 = 6 → 4) | PASS |
| T15 | Partial stack does not cap (Chapel 0 + Templar 1 + Inquisitor 1 = 2) | PASS |
| T16 | Pastoral Assumption succeeds (no governor + Chapel present) | PASS |
| T17 | Pastoral Assumption blocked when governor present | PASS |
| T18 | Pastoral Assumption blocked without Chapel/Church/Cathedral | PASS |
| T19 | Non-pastoral church-governor install has no precondition | PASS |
| T20 | Chapel 1 season — 1 half-unit accumulated, no tick | PASS |
| T21 | Chapel 2 seasons — accumulator hits threshold, +1 Order, drains | PASS |
| T22 | Church/Cathedral have no per-season Order accrual | PASS |
| T23 | Install action carries faction_standing + renown signals | PASS |
| T24 | CI=100 Mass Seizure Declaration threshold canonical | PASS |
| T25 | §1.7 Pastoral Assumption Ob is canonically 1 | PASS |

## Findings NEW this session

### F8 — §1.5 ↔ §1.6 semantic asymmetry (Religious Building effect models)

§1.5 Axis 1 expresses PT (Piety Track) generation as a **uniform per-season rate** for all three Religious Building tiers (Chapel +0.5/season, Church +1/season, Cathedral +2/season + adjacent-territory +0.5/season).

§1.6 expresses Stability (Order) bonus **with three different semantic patterns**:

- **Chapel** → per-season recurring (+0.5 Order/season, accumulator: rounds up to +1 every other season)
- **Church** → one-time at installation (+1 Order at installation)
- **Cathedral** → one-time at installation (+1 Order) PLUS structural modifier (Order decay −1, persistent)

This is canonically mixed — three different effect timing models within one table. Module 4 encodes all three patterns explicitly in `ParishBonus(installation_order_delta, per_season_half_order_units, order_decay_reduction)`. Module 13 Mode B chains must test that the player-visible feedback is proportionate across timing models: installation is one-time and visible immediately; per-season effect should be legible across many seasons; decay modifier should be persistent state that the player sees as "this Cathedral makes my Order resilient to drain."

**No editorial decision needed** — the asymmetry appears intentional (different infrastructure tiers carry different effect profiles). Surfaced for transparency and Module 13 testing.

### Half-fractional encoding choice

§1.5 uses `+0.5 PT/season` and §1.6 uses `+0.5 Order/season` — fractional rates. Module 1's Order stat is integer (0–5). Module 4 encodes fractional rates as **half-units** (Chapel: 1 half-PT-unit/season, accumulator triggers +1 every 2 seasons). This preserves integer arithmetic throughout while honoring the canonical "every other season" rounding rule for Chapel. `HALF_PT_UNITS_PER_PT = 2` and `HALF_ORDER_UNITS_PER_ORDER = 2` are exposed as canonical-cited constants.

**Module 4 stance:** the accumulator drains regardless of whether the underlying stat could absorb the gain (i.e., if Order is at STAT_MAX, the +1 still consumes 2 half-units but doesn't tick the stat). This prevents perpetual accumulator buildup that would tick instantly the moment Order drops. Module 13 Mode D should stress-test the cap case.

## Findings from prior sessions revisited

- **F1, F2:** unchanged.
- **F3 RESOLVED** (M2).
- **F4 PARTIALLY RESOLVED** (M2) — geography YAML `settlements:` block.
- **F5 unchanged** — edge-count comment math.
- **F6 unchanged (Mode-C blocker)** — intra-YAML S-ID granularity drift.
- **F7 unchanged** — §1.4.1 matrix omits §2.1 extra types. Note: Cathedral row IS in §1.4.1, so S-036 Himmelenger's Cathedral-City type would still need a §1.4 capacity interpretation, but §1.5/§1.6/§1.7 use `religious_building` tier rather than settlement type, so **Module 4 itself does not require F7 resolution** — Cathedral-City still gets §1.5 Axis-1 Cathedral effects via its own canonical Cathedral building.

## Module 4 data model (downstream contract)

```
ReligiousBuilding (enum)                 # NONE, CHAPEL, CHURCH, CATHEDRAL
HALF_PT_UNITS_PER_PT = 2
RELIGIOUS_BUILDING_PT_HALF_UNITS         # per-season PT generation half-units
CATHEDRAL_ADJACENT_PT_HALF_UNITS = 1     # per-adjacent-territory bonus

ParishBonus(installation_order_delta, per_season_half_order_units, order_decay_reduction)
PARISH_BONUS_BY_BUILDING                 # the four-row §1.6 mapping
HALF_ORDER_UNITS_PER_ORDER = 2

TEMPLAR_CI_PER_SEASON, TEMPLAR_INTERRUPT_OB_DELTA, TEMPLAR_INTERRUPT_CI_COST
INQUISITOR_RM_GOVERNANCE_OB_DELTA, INQUISITOR_CHURCH_ATTENTION_PER_SEASON
SEIZURE_OB_MODIFIER_*  (six per-axis constants)
SEIZURE_OB_MODIFIER_CAP = 4
CI_MASS_SEIZURE_DECLARATION_THRESHOLD = 100
PASTORAL_ASSUMPTION_OB = 1
PASTORAL_REVOCATION_ORDER_COST = 1
PASTORAL_REVOCATION_DISPOSITION_COST = 2

@dataclass ChurchInfrastructure                                    # MUTABLE state per settlement
@dataclass GovernorState                                           # M5 supplies the full version

seizure_ob_modifier(infra) -> int                                  # §1.5 stacking, capped
install_religious_building(infra, stats, new_building) -> ActionResult
install_templar_station(infra) -> ActionResult
install_inquisitor_base(infra) -> ActionResult
install_church_governor(infra, gov, is_pastoral_assumption) -> ActionResult
accrue_parish_bonus_per_season(infra, stats) -> (acc, triggered)   # M9 hook
```

## Player-action loop — six more improvement actions live

Module 4 brings the cumulative improvement-action handler count to **seven**:

| Module | Action | Notes |
|--------|--------|-------|
| M3 | `expand_institutional_capacity` | Treasury −300, +1 Wing |
| M4 | `install_religious_building(Chapel)` | +0.5 PT/season + 0.5 Order/season |
| M4 | `install_religious_building(Church)` | +1 PT/season + 1 Order one-time |
| M4 | `install_religious_building(Cathedral)` | +2 PT/season + adjacent PT + 1 Order one-time + order-decay −1 structural |
| M4 | `install_templar_station` | +1 CI/season + interrupt capability |
| M4 | `install_inquisitor_base` | +1 Ob to RM governance + Church Attention generation |
| M4 | `install_church_governor` | De facto Church territory + seizure-Ob −2 |

The seventh action — `install_church_governor` — has **two modes**: normal install (no preconditions; Ob is Module 5 territory) and **Pastoral Assumption** install (Ob 1, requires governor==None AND religious_building != NONE per §1.7). This is the first multi-precondition action; Module 13 Mode B chains test the precondition lattice.

### Geneva trap mechanic (player-readable feedback)

§1.6 design intent: theocracies grow through helpfulness, not hostility. The mechanical embodiment:

```
Crown player governs settlement with Order 2 (decaying)
   |
   v
Player accepts Chapel install (no Order delta at install, but +0.5/season)
   |
   v
After 4 seasons: Chapel has ticked +2 Order; settlement at Order 4 (stable)
   |
   v
But Chapel has also generated 2 PT/season to Church faction
   |
   v
Church's PT accumulates → CI grows → §1.5 mass-seizure threshold approaches
   |
   v
Player faces choice: tolerate Church infrastructure (Geneva trap) or attempt
seizure (Cathedral seizure-Ob −2 makes high-tier infrastructure expensive
to remove)
```

This is exactly the closed feedback loop Jordan specified: action → state mutation → faction-level cascade → player-visible standing change → new actions become attractive or expensive.

## Module 4 contribution summary

**State surfaces added:** `ChurchInfrastructure(religious_building, templar_station, inquisitor_base, church_governor, half_order_accumulator, order_decay_reduction)` — six fields per settlement, mutable.

**Hook surfaces added:** `accrue_parish_bonus_per_season` for Module 9's per-season Accounting cycle; `seizure_ob_modifier` for Module 6/7's seizure-action resolution.

**Signal direction:** all install actions return `faction_standing_delta=+1, renown_delta=+1` (provisional placeholders). The signal direction is the canonical-friendly part; magnitudes route to Modules 5/8/12 rebinding.

## Ledger entries this session

22 new (70 total cumulative). Coverage:

- 3 PT generation values for Religious Building tiers (Chapel/Church/Cathedral)
- 1 PT half-unit ratio (2)
- 1 Cathedral adjacent PT bonus value
- 1 half-Order ratio (2)
- 3 installation Order deltas (Chapel 0, Church 1, Cathedral 1)
- 1 Cathedral order-decay-reduction value (1)
- 1 Chapel per-season half-Order units (1)
- 6 seizure-Ob per-axis values (Chapel 0, Church 1, Cathedral 2, Templar 1, Inquisitor 1, Governor 2)
- 1 seizure-Ob cap (4)
- 1 CI mass-seizure threshold (100)
- 1 Pastoral Assumption Ob (1)
- 2 Pastoral revocation costs (Order −1, Disposition −2)

## Next session — Module 5 (dual-authority governance)

Force-full read: settlement_layer_v30 §3.1 (two-tier authority), §3.2 (governor assignment), §3.3 (subnational faction governance). Module 5 supplies:

- Governor-assignment Ob lookup (the non-Pastoral case for `install_church_governor`)
- Full `GovernorState` (Module 4's stub becomes Module 5's canonical type)
- §3.3 revocation rules (Pastoral Assumption can be revoked)
- Dual-authority resolution: when does the province faction's authority override the settlement governor's actions?

Module 5 also **rebinds the provisional faction_standing_delta values** from Modules 3 + 4 to canonical scalars derived from governance mechanics.
