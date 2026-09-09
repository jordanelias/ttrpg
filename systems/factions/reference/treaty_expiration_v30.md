# VALORIA — Treaty Expiration

## Status: CANONICAL — Pass 2h authoring 2026-05-17

## Scope: canonical specification for the Treaty Expiration mechanic. Universal (applies to all Crown Treaties regardless of faction party). v12c balance-validated at N=1000 (primary Crown-nerf lever — without this mechanic Crown achieves 55-90% win-rate dominance via Treaty-compounding hegemony).

## GD constraints: GD-1 binding (treaty expiration produces faction-relationship delta, not victory trigger).

## Source authority:
- `designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md` §4.5 (mechanic spec) + §5 (balance validation) + §6.5 (rationale)
- `designs/audit/2026-05-14-balance-audit/part13_integrated_balance_solution_2026-05-14.md` RC-v1 (prior iteration)
- `designs/audit/2026-05-14-balance-audit/part10_crown_initiative_design_2026-05-14.md` Mode III — Senator Outward (re-binding mechanism)
- `params/factions.md` (Crown Treaty stat semantics)

## Sim module: `sim/provincial/treaty.py`

---

## §1. Mechanic Specification

### §1.1 Expiration check

At each **arc boundary** (4 seasons per arc), each active Crown Treaty independently rolls for lapse.

| Field | Value |
|---|---|
| **Trigger** | Arc boundary (end of season 4, 8, 12, …) |
| **Check** | Per-Treaty independent roll |
| **Lapse rate** | `TREATY_LAPSE_RATE` ∈ [0.90, 0.95] (canonical default: **0.90**) |

**Procedure (per active Treaty):**
1. At arc boundary, before any other arc-boundary processing, iterate active Crown Treaties.
2. For each Treaty: roll uniform [0, 1).
3. If roll < `TREATY_LAPSE_RATE`: Treaty lapses (clear from both factions' treaty registers).
4. Lapsed Treaty effects (territorial protections, stat modifiers, action eligibility gates) cease immediately at arc-boundary.

### §1.2 Lapse consequences

When a Treaty lapses:

| Consequence | Effect |
|---|---|
| **Treaty cleared** | Both factions' treaty registers update; Treaty no longer protects territory or grants alliance. |
| **CB generation** | Lapsed Treaty generates **no** CB (canonical: peaceful expiration, not violation). For violation-driven termination, see §3 below. |
| **Standing impact** | No automatic Standing delta for peaceful lapse. |
| **Renewal path** | Crown may re-bind the relationship via Senator Outward action (per `part10_crown_initiative_design §3.4` Mode III — Senator Outward). |

### §1.3 Treaty stack invariants

- Multiple Crown Treaties may exist simultaneously (one per non-Crown faction).
- Treaty expiration is **independent per Treaty** — the lapse roll for Treaty (Crown, Hafenmark) is uncorrelated with the lapse roll for Treaty (Crown, Varfell).
- Treaty expiration is **memoryless** — a Treaty that survived 3 arcs has the same lapse probability at arc-boundary 4 as a Treaty just formed.

---

## §2. Re-binding via Senator Outward

Per `part10_crown_initiative_design §3.4` (Mode III — Senator Outward; see Pass 2h amendment to part10 for ED-840 closure):

| Field | Value |
|---|---|
| **Action** | Senator Outward (Crown faction; 1 per season) |
| **Cost** | Wealth −2 |
| **Pool** | Influence + Standing modifier |
| **Ob** | Target faction Sta (lower-stability targets are receptive) |

| Degree | Effect |
|---|---|
| Overwhelming | New Treaty bound (Crown, target). Target faction Standing +1. |
| Success | New Treaty bound (Crown, target). |
| Partial | Diplomatic overture acknowledged; CB-blocking effect for 1 arc. No Treaty. |
| Failure | Standing −1 (snub). No Treaty. |

Senator Outward is the canonical renewal path. Strategic implication: Crown that wants to maintain a Treaty against the 90% lapse rate must invest a season-action plus W−2 every arc per Treaty held. With 3 Treaties active, that's 3 season-actions per arc just on Treaty maintenance.

[PROVISIONAL: Senator Outward Ob = target faction Sta is part10 canon; consult part10 directly if Pass 2h amendments change this.]

---

## §3. Treaty Violation (distinct from lapse)

Treaty violation is a separate mechanic from lapse. Violation occurs when:

- A treaty-bound faction attacks (Military Conquest, Mass Battle invasion) a territory of the other treaty party
- A treaty-bound faction supports an external CB against the other party (Adjacent Instability CB granted, etc.)
- A treaty-bound faction initiates Parliamentary Transfer (per `parliamentary_transfer_v30.md`) against the other party's territory

**Violation consequences:**

| Effect | Magnitude |
|---|---|
| Treaty immediately voided | Cleared from both registers; effect cease immediately |
| Treaty-violation CB generated | Wronged party gains CB vs violator (consumable, per parliamentary_transfer §3) |
| Violator Standing delta | Standing −2 (public reputation damage) |
| Wronged party Standing delta | Standing +1 (sympathy / moral high ground) |

Violation does NOT consume the arc-boundary lapse roll for that Treaty (the Treaty is already cleared by violation).

[PROVISIONAL: Treaty violation specification is Pass 2h derived from v12c §4.4.1 ("Treaty-violation CB" is listed as a CB source for Parliamentary Transfer); v12c does not separately spec the violation mechanic. Pass 2k editorial-ledger entry recommends formalizing this in Pass 2k or a separate Pass.]

---

## §4. Design Intent and Narrative

Per v12c §4.5 design note:

> "90-95% lapse rate is mechanically functional but narratively extreme. Almost every Treaty breaks every arc. This is the primary Crown-nerf lever."

Without Treaty Expiration, Crown achieves 55-90% win-rate dominance because:
1. Crown can bind Treaties freely (1/season Senator Outward action)
2. Treaty-bound territories are protected from Crown intervention by other factions
3. Without expiration, bound territories compound — Crown locks in alliance hegemony

With Treaty Expiration at 90-95%/arc, Crown must continuously invest in re-binding. Treaty maintenance becomes opportunity cost, not free entrenchment.

**Canonical anchors:**

- Roman *foedera* required periodic renewal (oath at each coronation, treaty restatement at envoy exchanges)
- Medieval treaties required oath renewal at coronation of new monarch
- Diplomatic relationships are *actively maintained* rather than legally permanent

**Alternative considered (v12c §8.3, deferred):**

The 90-95% lapse rate is "narratively extreme" — every Treaty effectively breaks every arc. An alternative is Treaty stability tied to Crown diplomatic investment: maintaining each Treaty requires ongoing Senator Outward actions, creating opportunity cost without the all-or-nothing lapse roll. This alternative is deferred — would require sim re-validation of balance.

Pass 2h canonizes the 90%/arc rate as the implemented mechanic with `[PROVISIONAL: narrative-extremity-flag]` for Pass 2k consideration of the active-maintenance alternative.

---

## §5. Balance Validation

Per v12c §5 at N=1000 with Treaty Expiration active alongside other v12c mechanics:

| Faction | Win % | Notes |
|---|---|---|
| Crown | 24.7% | Reduced from 55-90% (Treaty-compounding nerfed) |
| Church | 28.6% | Stable per EA throttle every-arc |
| Hafenmark | 24.2% | Stable with Altonian Reinforcements |
| Varfell | 22.5% | Stable with Einhir Revival |

Sensitivity per v12c §7:
- `TREATY_LAPSE_RATE` +0.05 → Crown −1pp, distributed to others

The mechanic is in the second-highest sensitivity tier (after EA throttle, after consent rate). Lapse rate values 0.90, 0.92, 0.95 produce statistically equivalent balance (all configs within 7-10pp deviation at N=1000).

---

## §6. Tier-of-Test Status

**Tier 0 (Jordan-directed, v12c balance-validated):** ✓ Per `canon/mechanics_index.yaml` entry `treaty_expiration`, `test_status: validated_n1000_v12c`.

**Implementation pending:** `sim/provincial/treaty.py` is a Pass 2l armature stub. Pass 2h canonization unblocks implementation.

---

## §7. Cross-references

### Canon

- `designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md` §4.5 + §6.5 + §8.3
- `designs/audit/2026-05-14-balance-audit/part10_crown_initiative_design_2026-05-14.md` §3.4 (Senator Outward — re-binding mechanism)
- `designs/audit/2026-05-14-balance-audit/part13_integrated_balance_solution_2026-05-14.md` RC-v1 (prior iteration)
- `designs/provincial/parliamentary_transfer_v30.md` (Pass 2h companion — Treaty-violation CB source per §3)
- `canon/02_canon_constraints.md` §B GD-1 (no victory trigger)
- `params/factions.md` (Crown Treaty stat semantics)

### Sim

- `sim/provincial/treaty.py` — primary module
- `sim/peninsular/accounting.py` — Treaty lapse check integrated into arc-boundary accounting cascade
- `sim/provincial/crown_initiative.py` — Senator Outward (Mode III) re-binding action

### Mechanics index

`canon/mechanics_index.yaml` → `mechanics.treaty_expiration` — `canon_authoring_target` field updated from "(Pass 2h, pending)" to canonized path in companion commit.

---

## §8. Forward-flag (Pass 2k editorial-ledger batch)

| ID | Description | Resolution required |
|---|---|---|
| **TREATY-VIOLATION-001** | §3 Treaty violation mechanic is Pass 2h derived from v12c §4.4.1 reference; v12c does not separately spec violation magnitudes. | Jordan ratify magnitudes (Standing −2 / +1, violator/wronged) or revise. |
| **TREATY-NARRATIVE-001** | §4 v12c §8.3 alternative (active-maintenance instead of 90% lapse) is deferred. Mechanically canonized 90%/arc per v12c §4.5; narratively extreme. | Pass 2k consider whether to keep 90% lapse or revise to active-maintenance model. |
| **TREATY-MEMORYLESS-001** | §1.3 memoryless invariant (no aging effect on Treaties) is Pass 2h-stated, derived from "independent per-arc roll" framing in v12c. | Confirm. |

---

## §9. Status Declaration

[STATUS: CANONICAL — Pass 2h 2026-05-17. v12c-validated mechanic core (lapse rate 90-95%/arc, arc-boundary trigger, independent per-Treaty roll, Senator Outward re-binding path) is canonized. Treaty violation (§3) and active-maintenance alternative (§4) flagged [PROVISIONAL] for Pass 2k ratification.]

---

## §10. Changelog

- **v30 init (2026-05-17, Pass 2h):** Initial canonization. Consolidates v12c §4.5 + design rationale §6.5 + open item §8.3 into formal canon doc. Cross-references Senator Outward (re-binding) and Treaty-violation CB (parliamentary_transfer_v30). Forward-flags 3 derivation items to Pass 2k editorial-ledger.
