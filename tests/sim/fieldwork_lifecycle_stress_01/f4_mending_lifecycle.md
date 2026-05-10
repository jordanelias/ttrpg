# F4 — Mending Lifecycle + PP-716 Propagation Audit
## fieldwork_lifecycle_stress_01 sub-module F4

**Date:** 2026-05-10
**Mode:** A coverage + B (interaction chains) + PP-716 propagation re-validation
**Scope:** Mending operation lifecycle (threadwork §3 Mending), Mending Stability track (§5.1–5.5), board-game Mend order (§7.1), PP-716 wound-penalty propagation through Mending operations.
**Source authority:** threadwork_v30; PP-716 (commit 6e3a8aed); R1 v2 Chain 2 prior validation (commit 13e288a8).

This completes the F-bundle with F2 (Knot Lifecycle, commit `ddccbf9a`), F3 (Heresy Investigation, commit `8de82dbb`).

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| F4-L01 | mending_pool_formula | (Spirit × 2) + History + TPS; PP-616/625 strikes Attunement+Focus from pool | designs/threadwork/threadwork_v30.md | §3 Mending | "**Pool:** (Spirit × 2) + relevant History bonus + Thread Pool Score (PP-616, PP-625 — Attunement and Focus struck from pool dice; Focus still governs Contact Rounds)" |
| F4-L02 | mending_tn | TN 7 | designs/threadwork/threadwork_v30.md | §3 Mending | "**TN:** 7" |
| F4-L03 | mending_requirements | TS 50+; target = Gap, Shifting Object, or Locked Zone border | designs/threadwork/threadwork_v30.md | §3 Mending | "**Requirements:** Thread Sensitivity 50+ · Target must be a Gap, Shifting Object, or Locked Zone border" |
| F4-L04 | mending_ob_table | Gap severity → Ob (Shifting 2, Micro 3, Standard 5, Entrenched 6, Catastrophic 7, Locked 8+) | designs/threadwork/threadwork_v30.md | §3 Mending | "**Ob by Gap severity:**" |
| F4-L05 | mending_outcomes | Overwhelming +2 MS; Success +1 MS; Partial Gap reduced; Failure −2 MS | designs/threadwork/threadwork_v30.md | §3 Mending | "Overwhelming \| Substrate restored. Gap closes cleanly. Mending Stability +2 (strain released). Coherence: 0 (Mending is aligned work — no rendering damage). Mended area +1 Ob to future Gap formation in this zone for 1 season." |
| F4-L06 | mending_coherence_asymmetry | Mending never costs Coherence; aligned-work distinction | designs/threadwork/threadwork_v30.md | §3 Mending | "**Mending Coherence Asymmetry:** Mending never costs Coherence." |
| F4-L07 | seasonal_mending_fatigue | +1 Ob cumulative per consecutive same-season Mend; resets each season | designs/threadwork/threadwork_v30.md | §3 Mending | "**Seasonal Mending Fatigue:** Each consecutive Mending in the same season (not scene — season) adds +1 Ob cumulative." |
| F4-L08 | ms_range_thresholds | 100 → 0; 6 bands (Stable/Strained/Fragile/Fractured/Critical/Rupture) | designs/threadwork/threadwork_v30.md | §5.1 + §5.3 | "**Range:** 100 (fully stable) → 0 (the Rupture)." |
| F4-L09 | ms_cumulation_p14 | P-14: lower-band effects include all higher-band effects | designs/threadwork/threadwork_v30.md | §5.3 | "**Mending Stability threshold cumulation (P-14):** Mending Stability threshold effects are cumulative." |
| F4-L10 | ms_seasonal_cap | ±10 per season net | designs/threadwork/threadwork_v30.md | §5.5 | "No double-counting; seasonal cap on Mending Stability change is ±10 per season." |
| F4-L11 | ms_critical_endgame | MS 19–1 Critical = 2–4 season endgame; Rupture is legitimate ending | designs/threadwork/threadwork_v30.md | §5.3 design note | "**Design note — Mending Stability Critical as endgame:** Once Mending Stability enters the Critical band (19–1), the campaign is in a 2–4 season endgame without dramatic intervention." |
| F4-L12 | board_mend_order | Mend order: Intelligence vs Ob by Gap category; +1/−1 MS, draw Co-Movement | designs/threadwork/threadwork_v30.md | §7.1 | "**Mend** \| Intelligence (or faction-specific) vs Ob by Gap category (see below) \| Success: Gap closed. Mending Stability +1. Failure: Mending Stability −1. Draw Co-Movement Card." |
| F4-L13 | board_mend_ob | Gap → board Ob (Shifting 1, Standard 2, Entrenched 3, Catastrophic 4) | designs/threadwork/threadwork_v30.md | §7.1 | "**Board game Mend Ob** (lower than TTRPG — faction-level effort abstracts collective resources):" |

---

## 2. Mending operation lifecycle state machine

```
[Gap exists in territory]
      │
      │ Practitioner has TS ≥ 50 + target accessible
      ▼
[Mending operation declared]
      │ Pool = (Spirit × 2) + History + TPS
      │ TN = 7
      │ Ob = Gap severity table (F4-L04) + seasonal-fatigue
      │       cumulative + chronic-drift modifiers
      ▼
[Roll]
      │
      ├── Overwhelming (3+ net) ──► Gap closed; MS +2; Coherence 0; Mended-area +1 Ob to future Gaps for 1 season
      │
      ├── Success (2 net) ─────────► Gap closed; MS +1; Coherence 0
      │
      ├── Partial (1 net) ─────────► Gap reduced one severity; MS unchanged; Coherence 0; second Mending required
      │
      └── Failure (0 net) ─────────► Gap unchanged; MS −2; Coherence 0
                                          │
                                          │ At MS = 1 (Critical), failure can trigger Rupture cascade
                                          ▼
                                  [Rupture risk seasonal monitoring]
```

The full lifecycle pipes from per-operation MS deltas (F4-L05) into the Mending Stability track (F4-L08), which then feeds the cumulative threshold effects (F4-L09) at Accounting subject to the ±10 seasonal cap (F4-L10).

---

## 3. NERS at full grain — Mending lifecycle (24 cells)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | F4-L01..L13 specify pool, TN, Ob table, outcomes (4-degree), Coherence asymmetry, seasonal fatigue, MS feedback. Complete operation → track → endgame pipeline. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Per-Mending state: pool dice, Ob, Mending Stability delta. Trivially trackable. |
| Vertical | ✓ | ✓ | ✓ | ✓ | TTRPG Mending operation (F4-L01..L07) and board-game Mend order (F4-L12, F4-L13) bridge the same MS track via §5.5 Hybrid mode (Cascade Phase aggregation). |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Cross-system: Mending feedback into Threadwork (Coherence asymmetry F4-L06), into Faction-politics (MS Critical = institutional rendering failures, Mandate erosion), into Conviction (sustained MS-low triggers Faith-Conviction Companions Scar via secondary mechanics not tested here). |
| Lateral | ✓ | ✓ | ✓ | ✓ | Lateral coverage: Mending degrades on Failure (F4-L05) and via Lock drift (§5.2), recovers via Success/Overwhelming (F4-L05) and via Southernmost expedition Mending +2 permanent (§5.2). Two-direction balance preserved. |
| Horizontal | ⚠ | ⚠ | ✓ | ✓ | ⚠ N: Critical-band endgame structure (F4-L11) is intentionally near-unwinnable — by design "the table must coordinate across faction lines... or accept that the campaign ends in the Rupture." This is a design feature but produces ⚠ on N for tables that don't internalize the design intent. ⚠ E: discoverability of MS state in board game (hidden by default per §5.4) requires Investigate Thread (Intelligence vs Ob 3) — players may operate blindly. |

**Verdict:** 22/24 ✓, 2 ⚠ Horizontal (Critical-band design intent + board-game discoverability). Lifecycle is mature.

---

## 4. PP-716 propagation re-validation

R1 v2 Chain 2 (commit `13e288a8`) validated PP-716 −1D-Pool wound penalty against Mending. This module re-confirms:

### Per-operation impact

| Practitioner state | Mending Pool dice | Effect on outcome distribution |
|---|---|---|
| 0 Wounds | (Spirit × 2) + History + TPS | Baseline |
| 1 Wound | (Spirit × 2) + History + TPS − 1, floor 5 | −1D Pool; small TN-7 hit-rate drop |
| 2 Wounds | same formula − 2, floor 5 | If pool ≥ 7 base, drops to floor + 5; else stays at 5D floor |
| 3+ Wounds | floor 5D (cannot fall below) | Floor protection prevents extinction |

**Critical finding:** the floor-5D guarantees a wounded practitioner can always *attempt* a Mending operation. They cannot be pushed below 5D Pool — preventing the v1 +1-Ob unfloored extinction cascade where wound penalty + seasonal fatigue + Critical-band Ob inflation could drive Pool below 1D.

### Self-treatment loop

A practitioner Mending themselves:
1. Wounded practitioner casts Mending on a Gap → succeeds → MS +1 → ... not their own Wounds.
2. Mending is **substrate-repair**, not Wound-healing. PP-716 wound-floor protects the operation; it doesn't cure the Wounds via Mending.
3. Wound-healing uses Healing operations (W-08 and variants per the R-56 correction): "each healing operation in the same contact window adds +2 Ob (not +1). Sequence: 1st heal Ob 1, 2nd Ob 3, 3rd Ob 5, 4th Ob 7."
4. So a wounded practitioner attempting self-Healing has accelerated Ob inflation but still benefits from PP-716 floor on the attempt itself.

**No extinction cascade.** R1 v2 Chain 2's verdict is reaffirmed: PP-716 −1D-Pool with floor 5D produces a friction loop (each operation costs more dice up to the floor), not extinction.

### Mass-Mending Fatigue interaction

Per F4-L07 seasonal fatigue: cumulative +1 Ob per consecutive Mending in same season. A wounded practitioner Mending 3 times in a season:
- 1st: Pool = (S×2)+H+TPS −1 (floor 5), Ob base
- 2nd: Pool same, Ob +1
- 3rd: Pool same, Ob +2

Over a season, wound-penalty + fatigue compound on Ob side, not Pool side. This is the canonical loading: wounds reduce attempt strength uniformly; fatigue raises the bar per attempt. **Combination is well-defined and non-pathological.**

### Mass-battle Mend order interaction

Per F4-L12: faction-level Mend uses Intelligence (or faction-specific stat) vs lower Ob (F4-L13). PP-716 −1D Pool penalty for individual-actor Wounds doesn't apply at faction-scale rolls — wounds are personal-scale state. **No propagation issue at mass-battle layer.**

---

## 5. Mode B — Mending interaction chains

### Chain 1: FR Lock → drift → Mending recovery loop

Per §5.2: FR Lock causes immediate −1 to −3 MS plus chronic drift. Mending recovers +1 to +2 per success. Lock removal is required to stop drift; Mending closes Gaps that may exist.

**Equilibrium:** with N active Locks each producing −1 chronic drift per season and M successful Mendings per season at +1 each: MS net change ≈ M − N per season (ignoring other sources). For stable MS, M ≥ N. For recovery, M > N + (other losses).

This produces a mid-campaign mechanical pressure: as Locks accumulate, Mending throughput must scale or MS degrades.

### Chain 2: Critical-band endgame structural lock-in

Per F4-L11: at MS 19–1 Critical, "almost every Thread operation carries Rupture risk on Failure, but not operating also reaches Rupture within 1–3 seasons from Lock drift and winter."

**Operational tradeoff:** operating risks immediate Rupture on Failure; not operating reaches Rupture via passive drift. The escape requires:
1. Remove all active Locks (eliminates drift)
2. Mend all active Gaps (eliminates per-season Mending Stability loss)
3. Operate exclusively at Object/Personal scale until MS recovers

This is the **Einhir Catastrophe Mechanism** made playable. The game intentionally provides no clean rescue.

### Chain 3: Mending Coherence-zero exception unbroken under PP-716

Per F4-L06: Mending never costs Coherence. PP-716 wound-penalty applies to Pool dice, not Coherence. The two systems remain independent.

A wounded practitioner with Coherence at 5 (post-Pulling exposure) Mending a Gap: pool reduced by −1D (floor 5), Coherence unchanged because Mending is aligned work. The practitioner emerges from the Mending with same Coherence. **PP-716 does not break the canonical Mending-Coherence asymmetry.**

### Chain 4: Southernmost expedition Mending (+2 permanent)

Per §5.2: "Southernmost expedition Mending: +2 permanent per successful season". This is the canonical post-Einhir-Catastrophe restoration arc. PP-716 wound-penalty applies to the per-operation roll but not to the "+2 permanent per successful season" mechanic — the season-aggregate reward is independent of individual wound state. **Architecture preserves campaign-arc structure.**

### Chain 5: Hybrid mode aggregation

Per §5.5: TTRPG-sourced and board-game-sourced MS changes both apply at Accounting. Seasonal cap ±10 per season net.

Combined with PP-716: a wounded PC's TTRPG Mending operations produce −1D Pool; their faction's mass-battle Mend orders use Intelligence (faction stat) without per-PC wound application. **Cross-mode aggregation is clean.**

---

## 6. Mode D — Edge cases (compressed)

### Boundary
**EC-F4.B-01 [P3]:** Mending at exactly MS = 1 with Failure → MS −2 → MS = −1 floored at 0 = Rupture. Boundary canonically consistent. Rupture is irreversible (campaign ends).

**EC-F4.B-02 [P2]:** Practitioner with 0 Wounds, exactly at TS 50 (minimum F4-L03), Mending Shifting Object Ob 2: requirement met; pool baseline. Boundary clean.

### Cascade
**EC-F4.C-01 [P2]:** Multi-Mending season + Lock removal + Gap closure: the practitioner+team coordinate Lock removal first (stops drift), then sequential Mending of remaining Gaps. Cumulative seasonal fatigue compounds on Ob; PP-716 wound penalty on Pool. Both compositional; canonical.

### Regression
**EC-F4.R-01 [P3]:** A practitioner Mending in territory with active Lock contributes +1 strain to nearby Knots (per F-L06 source 4). If the practitioner has Knots in the territory, their own Mending operations strain those Knots. **Lateral cost.**

### Crunch cascade
**EC-F4.CR-01 [P3]:** Per-Gap state, per-territory Lock state, per-practitioner pool/Coherence/Wound state, per-season fatigue counter, faction-level Mend orders, MS track all tracked at Accounting. Bookkeeping is non-trivial but bounded.

### Ambiguity
**EC-F4.A-01 [P3]:** "Multiple successful Mendings in a season stack independently at Accounting" (§5.2 row 10) — clear. No ambiguity.

### Incoherence
**EC-F4.I-01 [P3]:** Threadcut beings Mending. F-L11 (Knot lifecycle) noted threadcut beings use Coherence as parallel resource. But F4-L06 says Mending costs 0 Coherence. Threadcut beings Mending should cost 0 Coherence on the threadcut as well — consistent if Mending is aligned work. The aligned-work distinction holds across actor type. **Coherent.**

### Optimal play
**EC-F4.O-01 [P3]:** Players optimal: maintain MS ≥ 60 (Strained band) buffer; close Gaps faster than they form; remove Locks proactively; coordinate cross-faction Mending in Critical-band recovery. Standard endgame strategy.

---

## 7. Decision-shape findings

**Recommendation: F4.1 (preserve canonical Mending lifecycle; PP-716 propagation through Mending re-validated; no mechanical changes).**

**Rationale:**

1. **All canonical channels present and consistent.** Pool formula (F4-L01), TN (F4-L02), requirements (F4-L03), Ob table (F4-L04), outcomes (F4-L05), Coherence asymmetry (F4-L06), seasonal fatigue (F4-L07), MS track (F4-L08), cumulation (F4-L09), seasonal cap (F4-L10), Critical endgame (F4-L11), board-game order (F4-L12, F4-L13). Comprehensive lifecycle.

2. **22/24 NERS pass.** Two ⚠ Horizontal: Critical-band endgame design (intentional Einhir Catastrophe Mechanism), board-game discoverability (intentional Investigate Thread gating).

3. **PP-716 propagation re-validated.** R1 v2 Chain 2's verdict holds: floor 5D Pool prevents extinction cascade; Mending operations remain attemptable for wounded practitioners; Mending Coherence-zero asymmetry unbroken; cross-mode aggregation clean.

4. **No new spec gaps surfaced** beyond what was already deferred (Mending Coherence asymmetry interaction with hypothetical future operation types is documented in canon/02 Amendment 3).

**Implementation:** No changes. F-bundle (F1 R5, F2 Knot Lifecycle, F3 Heresy Investigation, F4 Mending) verified COMPLETE.

---

## 8. Module status

| Item | Status |
|---|---|
| Canonical sources (threadwork §3 Mending; §5.1–5.5 MS track; §7.1 Mend order) fetched at full depth | ✓ |
| Verification ledger (13 entries) | ✓ |
| Mending lifecycle state machine reconstructed | ✓ |
| NERS full-grain analysis (24 cells) | ✓ |
| PP-716 propagation re-validation (4 sub-chains) | ✓ |
| Mode B chains (5) | ✓ |
| Mode D edge cases (8 across 7 categories) | ✓ |
| Decision-shape finding (F4.1 preserve canonical) | ✓ |

**F4 Mending lifecycle audit: verified.**

**fieldwork_lifecycle_stress_01 F-bundle: COMPLETE** (F1 covered in R5, F2 Knot Lifecycle ✓, F3 Heresy Investigation ✓, F4 Mending ✓).
