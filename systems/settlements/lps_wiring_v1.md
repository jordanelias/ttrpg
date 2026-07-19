# L/PS Wiring — Buildable Spec (E5 execution)

## Status: PROPOSED (buildable spec) — 2026-07-14 · Lane: SE · executes E5 / ED-FA-0004 Stratum-B / ED-SE-0007

**What this is.** The worked, buildable design for wiring the **inert** per-settlement Legitimacy/Popular-Support
(L/PS) into `sim/` — the #1 item from the `2026-07-13-cross-scale-governance-grounding` decision queue and the
"single highest-priority open item in the whole governance/generation thread" (`scale_hierarchy_v1 §4`; E5 in
`governance_consolidation_v1`). It turns three things that exist only as prose/schema into one live pipeline:
the LPS-2e aggregation (`settlement_layer_v30 §1.8`, ruled 2026-05-30), the **consent-gate** (`scale_hierarchy_v1
§4`, *concept only — no formula*, designed here), and the per-settlement write-side (`§1.8a`, PROPOSED).

**Ground truth this is built against** (read, not assumed):
- `sim/territory/registry.py` — `Settlement.legitimacy:int=0`, `Settlement.popular_support:int=0`, range **0–7**
  (`L_PS_MIN/MAX`); explicitly *"NEVER READ OR WRITTEN anywhere in sim/ (zero non-definition references)"*. The
  aggregation idiom already in the file: `province_accord = floor(mean settlement Order)` over real members;
  `province_effective_prosperity = Σ Prosperity`. **We mirror that idiom exactly.**
- `settlement_layer_v30 §1.8` — the LPS-2e formulas (below), specified as prose, never wired.
- `scale_hierarchy_v1 §4` — the consent-gate concept, no formula.
- `governance_consolidation_v1` E5 + `tools/sim_harness/ lps_inert_check` (100/100 inert — the red test this flips).

**Doctrine.** This is a **[COMPLETE-THE-CHAIN]** for the aggregation + write-side (the formulas are ruled; we
wire them) and a **[GENUINE-GAP → designed]** for the consent-gate function (§4 gives no formula; §3 below is
the design). Per ED-1050 we do **not** import CK3 — the gate is derived from the corpus's own q_s/Weight/Order
grammar. Precedent (CK3-Administrative broadcast+attenuation; EU4 estate-loyalty bands) is confirmatory only.

---

## §1 · State (canonical, already on `Settlement`)

Per settlement `s`, toward its **controlling faction** `f = s.owner_faction` (Church-Governor settlements,
`settlement_layer §1.2` Axis-4, key toward the Church faction):

| field | type | range | axis (Weber, §1.8a) | mutability |
|---|---|---|---|---|
| `s.legitimacy` (L) | int | 0–7 | traditional + legal-rational (slow) | write-side §4 only |
| `s.popular_support` (PS) | int | 0–7 | charismatic / performance (fast) | write-side §4 only |

L/PS are **canonical per-settlement state**; Mandate and the faction aggregates are **pure derived** (never
stored — recomputed each read, like `province_accord`). No new fields are added to `Settlement`; the two inert
fields become live. A new module `sim/territory/legitimacy.py` holds the pure functions + the Accounting step
(store-router idiom, `world` optional, exactly like `registry.py`).

---

## §2 · Aggregation — pure functions (wire LPS-2e verbatim)

Mirrors `registry.province_*` (iterate `province_members` / a new `faction_settlements(f, world)`), all pure:

```
base(stype):  # Weight base by type — candidate table, CALIBRATION-FLAGGED (§7 Q1)
  Seat/Cathedral(-City) = 4 ; City/Fortress-City = 3 ; Town/Fortress/Port = 2 ;
  Village/Mine/Outpost = 1                          # every legal type has base ≥ 1

W(s)      = base(s.stype) + s.prosperity + s.facility_tier            # §1.8 Settlement Weight
q(s)      = 0.5*s.legitimacy + 0.5*s.popular_support                  # §1.8 acceptance, 0–7
faction_settlements(f) = [s for s in store if s.owner_faction == f]

def faction_mandate(f, world=None):                                  # §1.8 LPS-2e
    S = faction_settlements(f, world)
    T = sum(W(s) * (q(s)/7.0) for s in S)                            # weighted legitimacy mass
    return clamp(round(7.0 * T / (T + 6.0)), 0, 7)  if S else 0      # K = 6 (ruled)

def faction_aggregate_L(f, world=None):                              # weight-weighted mean, 0–7
    S = faction_settlements(f, world); Wtot = sum(W(s) for s in S)
    return (sum(W(s)*s.legitimacy for s in S)/Wtot) if Wtot else 0.0
# faction_aggregate_PS: identical over popular_support
```

Invariants (become seeded tests, §6): `T=0 ⇒ Mandate=0`; monotone non-decreasing in each `q(s)`; bounded 0–7
for any holding (the `T/(T+6)` saturation, "Lesson-5 bound"); a faction of few large-developed settlements
out-Mandates one of many tiny ones at equal accepted-population (the ruled intent, §1.8).

---

## §3 · The consent-gate (the designed piece — §4 gives no formula)

§4: *"a tier can impose a governance type, but whether it sticks — whether the ruling faction keeps effective
power at that tier — depends on whether the settlements underneath accept it, measured by L/PS."* Two things
must become mechanical: **(a) a graded compliance yield** that throttles what an accepted-vs-resented settlement
actually delivers, and **(b) a slip mechanic** by which a chronically-unaccepted settlement stops sticking.

### §3.1 Compliance yield (continuous, replaces the binary "controlled?")
Derived from the corpus's own `q(s)` — **not** an imported band table:
```
compliance(s) = clamp((q(s) - Q_FLOOR) / (Q_FULL - Q_FLOOR), 0.0, 1.0)   # 0 at Q_FLOOR, 1 at Q_FULL
   with Q_FLOOR = 1.0, Q_FULL = 6.0   (CALIBRATION-FLAGGED §7 Q2)
```
`compliance ∈ [0,1]` is the **local attenuation** factor (the CK3-Administrative shape realized as a formula):
a uniform manager-type is broadcast down by the cascade (`§3`), but each settlement realizes it only in
proportion to its own consent. It multiplies the settlement's **realized contributions** to its faction:
- **Treasury** — `derived_stats §8.1` gives `faction income = Σ settlement Prosperity × M`, **ungated by L/PS**.
  Wire: `realized_income(s) = M * s.prosperity * compliance(s)`. *This is what makes L/PS load-bearing on the
  economy, not decoration.* (The base multiplier `M` is a **separate open conflict — ED-SE-0045, ×10 vs ×50**;
  the `× compliance(s)` throttle composes with whichever base is ruled, so this spec does not depend on it.)
- **Administration Points** — `s.ap` (`registry.py`) becomes `floor(s.ap * compliance(s))` for the controlling
  faction's use (a resented settlement obeys its governor sluggishly).
- **Mandate weight** — already handled by `q(s)` inside `T` (§2); compliance does **not** re-multiply it (avoids
  double-counting q).

### §3.2 Slip — the "does it stick" state machine (the E5→GD-3 bridge)
Per settlement, an ordinal `control_state ∈ {HELD, CONTESTED, SLIPPING}` derived from `q(s)` each Accounting,
plus a persistent `slip_counter` (a ledger tag, `registry.Settlement.add_tag`):
```
HELD       if q(s) >= Q_CONTEST (=3)          # imposition holds; compliance≈full
CONTESTED  if Q_SLIP <= q(s) < Q_CONTEST       # partial resistance: +Suspicion, +Pressure, governor Ob +1
SLIPPING   if q(s) < Q_SLIP (=1.0)             # imposition failing to stick
```
While `SLIPPING`, increment `slip_counter`; on **2 consecutive Accountings** SLIPPING (mirrors
`insurgency_pipeline_v30 §4.1`'s 2-season formation trigger, so this composes with the *built* GD-3 spine rather
than inventing a parallel one), the settlement **rolls an Independence check** (`scale_hierarchy §5.2`): it breaks
from `owner_faction` and becomes eligible for cross-scale claim (RM etc.). Recovery: any Accounting at `q ≥
Q_SLIP` resets `slip_counter = 0` (collapse is a **dial**, per the Fable/RimWorld-DF finding — the counter is the
E11/E7 dampener made concrete). This is the *only* place L/PS produces a topology change; everything else is a
throttle.

**Why this is the chain-completion, not an import:** `q(s)`, Order, Suspicion, Pressure, the ledger, and the
§5.2 independence mechanic all already exist; the gate is three thresholds over `q(s)` plus a counter reusing the
insurgency-pipeline's own cadence. Nothing foreign is added.

---

## §4 · Write-side — what moves L/PS (bottom-up feeders, deferred-apply)

L/PS change **only** through these sources, all accrued into a per-settlement `pending_dLPS` during the season
and applied **once** at the Accounting boundary (§5), clamped 0–7:

1. **Scene-conduct echo (`compute_accord_echo`, currently zero callers — GAP-A2).** Settlement-locus scene
   outcomes already produce an Accord echo; extend the same echo to carry a `ΔPS` (fast/charismatic — visible
   local outcomes) and, for institution-grade outcomes (tribunals, charters), a smaller `ΔL`. This *is* the
   wiring of A2 — one function, one call site, no new bookkeeping track.
2. **Mission-outcome cascade (PP-686, already specified).** Faction-level cascade-fidelity/procedural/violation
   ΔL/ΔPS apply **uniformly** to the faction's controlled settlements (unchanged from §1.8; now actually lands
   because L/PS is live).
3. **§1.8a settlement-grain event table (PROPOSED, ED-SE-0007).** Adopt its event→ΔL/ΔPS map as the enumerated
   source list (dearth, charter grant, garrison abuse, etc.). Ratifying §1.8a is **§7 Q3**.
4. **Mandate→L mean-reverting drift (routinization of charisma, §1.8a).** `ΔL_drift = sign(M_prev − L) · 1` when
   `|M_prev − L| ≥ DRIFT_BAND (=2)`, where `M_prev` is **last** Accounting's Mandate (see §5 for why *last*, not
   this one — the D.6 disjointness rule). Slow: at most ±1/Accounting.
5. **Init / conquest (Entry Terms, §5.3 SE-5).** World-gen seeds L/PS from generation (`generation_sourcebook`
   R9). On conquest: **Confirm** preserves the prior L (and sets PS to a low post-conquest value); **Impose
   Administration** sets **L := L_IMPOSE (=1)** — so an imposed manager-type starts SLIPPING/CONTESTED and must
   *earn* consent, which is exactly the §4 dynamic and the G2 "suppression is never consequence-free" hook.

---

## §5 · Data-flow — the Accounting-boundary sequence (D.6-disjoint)

L/PS lives entirely at the **Accounting boundary** (the existing deferred-apply seam, `echo_transport` idiom),
in this fixed order each season, so the up-read and the down-write never touch the same value in the same tick
(resolving the `governance_consolidation` **D.6** double-count / OF-3 oscillation risk, and satisfying the A4
cross-tick contraction condition):

```
0. SNAPSHOT   M_prev[f] = faction_mandate(f)              # read BEFORE any write this season
1. ACCRUE     pending_dLPS[s] += (scene echoes, mission cascade, §1.8a events,
                                  drift toward M_prev[f], conquest inits)   # all sources, additive
2. APPLY      s.legitimacy = clamp(s.L + pending_dLPS[s].dL, 0,7);  (same for PS);  clear pending
3. AGGREGATE  recompute (pure) faction_mandate / aggregate_L / aggregate_PS from POST-write L/PS
4. GATE       for each s: compliance(s); control_state(s); slip_counter update; Independence roll on 2×SLIP
5. CONSUME    Treasury/AP throttled by compliance; vote pool = Mandate; strictness = aggregate_L  (§6)
```
**Disjointness argument (why it converges).** Step 4's Mandate→L drift *reads* `M_prev` (step 0, pre-write) and
*writes* into **next** season's step 1 accrual — the up-aggregate (step 3, this season) and the down-drift
(applied next season) are separated by a full Accounting, so no value is both summed-up and written-down within
one tick. The drift is a bounded mean-reversion (`|ΔL|≤1`, only when the gap ≥2), i.e. strictly contractive
toward the Mandate fixed point → the composed map is a contraction (the A4 termination artifact, instantiated).

---

## §6 · Consumer rewire (make the live values actually read)

| consumer | today (bypasses settlement grain) | wire to |
|---|---|---|
| Parliamentary vote pool | `parliamentary_bridge._derive_vote` keys on raw `world.factions[n].L` (GAP-B1 evidence; verify call site at build) | `faction_mandate(f, world)` |
| Public-Expectation Strictness | raw faction L | `faction_aggregate_L(f, world)` |
| `compliance(L)` yield (Treasury/AP) | ungated (`Σ Prosperity×10`) | `× compliance(s)` per §3.1 |
| Governance-cascade "does it stick" | undefined | `control_state(s)` / slip (§3.2) |

`Faction.L` / `Faction.PS` (the raw faction scalars) are **retired as inputs** — they become *display mirrors*
of `faction_aggregate_L/PS`, never the source (the DF "don't invent a parallel ledger" principle: one canonical
grain — the settlement — read by every scale).

---

## §7 · Numbers & the calibration surface (needs_jordan)

Ruled/fixed: `K=6`; ranges 0–7; slip cadence = 2 Accountings (insurgency-pipeline parity). **Calibration-flagged**
(defaults given so it is *buildable now*, Stage-4 sim tunes them):
- **Q1 · `base(Type)`** — the Weight base table above (Seat 4 … Outpost 1). Ties to `settlement_layer §1.2` Population (§9 PENDING).
- **Q2 · consent-gate anchors** — `Q_FLOOR=1, Q_FULL=6` (compliance slope); `Q_CONTEST=3, Q_SLIP=1` (state thresholds); `L_IMPOSE=1`; `DRIFT_BAND=2`.
- **Q3 · ratify `§1.8a`** (the settlement-grain event→ΔL/ΔPS table) — the enumerated write-side source #3.
- **Q4 · Treasury throttle magnitude** — full `×compliance` vs a floored `×(0.5+0.5·compliance)` (does a resented settlement pay *nothing* or *half*?). Default: full (makes consent maximally load-bearing; the G2 backfire wants teeth).

---

## §8 · Edge cases

- **No controlled settlements** → `faction_mandate=0`, `aggregate_L=0` (guarded, matches `province_accord`'s empty case).
- **Zero-Prosperity/zero-FacilityTier settlement** → `W ≥ base ≥ 1`; contributes `base·(q/7)`; never divides by zero (`Wtot>0` guarded).
- **Church-Governor settlement (Axis-4)** → L/PS keyed toward the Church faction; same pipeline.
- **Conquered-then-abandoned** → Impose sets `L=1` → SLIPPING → 2 Accountings → Independence → feeds `insurgency_pipeline`; a genuinely emergent RM settlement, not a scripted one.
- **Simultaneous succession** (§1.8b, PROPOSED) → succession changes *leadership not control*; applies a ΔL only, through the same accrual — no special path.
- **Cross-scale-claimed settlement (§5.2)** → post-claim it aggregates into its claimant's Mandate normally; only its claim *origin* was exceptional.

---

## §9 · Test plan (the deliverable's proof)

1. **`lps_inert_check` flips 100/100 → green** (`tools/sim_harness/`) — L/PS now have non-definition read+write sites. *This is the headline pass/fail.*
2. **Closed-form Mandate** — seeded holding, assert `faction_mandate` == `clamp(round(7T/(T+6)),0,7)` by hand-calc; assert monotonicity and the 0–7 bound.
3. **Consent-gate** — a q=7 settlement yields `compliance=1.0`, full Treasury; a q=1 settlement yields `compliance=0`, enters SLIPPING, and triggers Independence after exactly 2 Accountings; recovery resets the counter.
4. **Convergence** — from any seed, the Mandate→L drift reaches a fixed point within N Accountings (no oscillation) — the A4/D.6 disjointness made a passing assertion.
5. **Consumer parity** — the parliamentary vote pool equals `faction_mandate` (not raw `Faction.L`); a settlement-grain L/PS change moves the vote next season.

---

## §10 · Scope & follow-ons

This spec is **buildable as written** (defaults fill every calibration hole). It is **PROPOSED** — it does not
itself edit `sim/` or flip any `## Status:`; §7 Q1–Q4 are the `needs_jordan` calibration picks. The natural next
step is the implementation PR (`sim/territory/legitimacy.py` + the `parliamentary_bridge`/Treasury/AP rewires +
the §9 tests), which — because §5 is D.6-disjoint and every formula is closed-form — is a bounded, oracle-safe
change (it adds read/write sites to a dead field; it does not "correct" the Python oracle, per the ED-1050
port↔oracle rule). Companion gaps it unblocks: **A2** (the `compute_accord_echo` call site is write-source #1),
**B2/E2** (the Mandate-collapse collision consumes this Mandate + the slip mechanic), **B4** (the Mandate→L drift
is the first concrete `decay()`-family term), and the whole `scale_hierarchy` cascade (which §4 says is inert
until this lands).
