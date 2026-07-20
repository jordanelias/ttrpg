# CC-4 Resolution — Faction Stability Recovery Located; Compound Sim Re-Run

**Date:** 2026-05-28
**Resolves:** CC-4 (`sim_compound_collapse_results.md` §5) and the staged ED-877.
**Companion update:** `sim_compound_collapse.py` (re-run with canonical recovery).
**Bias:** `[SELF-AUTHORED — bias risk]`. This corrects my own prior "unspecified/unlocated" claim — the gap was **unread, not absent.**

---

## §0 — Headline

**CC-4 is closed: the faction Stability-recovery mechanic EXISTS and is canonical — I had not read §1.3.** My "unspecified" framing was wrong; the correct verdict is "unread." More important, the real mechanic is **structurally different** from what the sim assumed (deterministic, not a die-roll), and re-running with it both (a) makes collapse magnitudes trustworthy for the first time and (b) **confirms the CC-1 Trigger-5 cliff propagates all the way to faction collapse — a mid-tier faction collapses ~25× more often than a weak one.**

---

## §1 — The recovery mechanic (canonical, was unread)

`faction_layer_v30` **§1.3 Stability Recovery** + Accounting Step 9. The primary path is **deterministic, not a roll**:

> **Institutional Consolidation** — *"No Trigger 1–5 fired against this faction this season at Accounting → Stability +1"* (also Accord +1 in one territory, cap 2). The doc explicitly notes: *"This recovery path (+1 for a 'clean' season) **replaces the abstract simulator recovery rule** introduced during development. It is now formally canonical."*

Conditional paths (each +1, all gated): mutual peace treaty (both Stab ≥ 2), recapture own occupied territory (Military_advance Success), Parliamentary Rebuttal Overwhelming, Church Absolution (target Stab ≤ 2, costs Church Mandate −1), Löwenritter endorsement. **Seasonal cap ±2.**

And the check I had *conflated* with recovery — **§1.4 Accounting Stability Check** — is actually a **cascade-damage** check, not a recovery roll: it fires only if a faction lost ≥ 2 attribute points that season, rolling Stability vs Ob = magnitude of loss; Failure → −1, Overwhelming → +1 (the +1 is the rare exception, not the mechanism).

**Why this matters:** my earlier sim modeled recovery as a *die-roll gate* (~26–40% pass). The canonical mechanic is **automatic +1 on any clean season** — a far stronger, deterministic damper. The doc even says so directly ("replaces the abstract simulator recovery rule"). I had reinvented an abstract recovery rule the canon had already replaced.

`[CORRECTION: CC-4 "recovery mechanic unspecified/unlocated" → RETRACTED. Mechanic is faction_layer §1.3 Institutional Consolidation, deterministic +1 on a Trigger-free season, formally canonical. Was unread (I hit the doc header at "Accounting," not §1.3). ED-877 should be reclassified from "missing" to "resolved — was unread."]`

---

## §2 — Compound sim re-run with canonical recovery (now trustworthy)

Re-ran `sim_compound_collapse.py` replacing the placeholder recovery with Institutional Consolidation (deterministic +1 if no Trigger fired) + §1.4 cascade check + ±2 cap. **The SANITY case now passes** (strong faction, zero pressure → 0% collapse), so the magnitudes are reportable.

**Compound collapse (weak faction, Mil 2, Wealth 2, Cmd 2, Coh 8, all three pressures, 20 seasons, 6k trials):**

| Starting Stability | P(collapse / 20 seasons) |
|---|---|
| Stab 2 | 2.8% |
| Stab 3 | 0.4% |
| Stab 4–6 | 0.0% |

The compound does **not** spiral the weak faction — and now we know *why* precisely: **Trigger-5 fires only 1.9% of seasons at Cmd-2 (CC-1), so almost every season is "clean," and Institutional Consolidation auto-restores +1.** Deterministic recovery outpaces the rare losses. This supersedes my earlier "starved input" explanation (CC-2) with the full mechanism: starved input **plus** a deterministic recovery that the starved input can't overcome.

---

## §3 — The CC-1 cliff propagates to collapse (the real finding)

The decisive new result. Holding the compound fixed and varying only Command (which sets the defender's battle pool, hence the Trigger-5 firing rate):

| Faction Cmd | Pool | Trigger-5 firing (CC-1) | **P(compound collapse / 20s)** |
|---|---|---|---|
| Cmd 2 | 4D | 1.9% | **0.9%** |
| **Cmd 3** | **6D** | **16.6%** | **22.6%** |
| Cmd 4 | 8D | 11.3% | 18.6% |

**A single point of Command (2→3) raises compound collapse ~25×** (0.9% → 22.6%), then it *declines* at Cmd 4 — exactly tracking the non-monotonic Trigger-5 firing curve. The mechanism is now end-to-end:

1. At Cmd 3 the battle pool hits exactly 6D → Trigger-5 Condition C's `pool ≥ 6` clause auto-fires on **any** failure (16.6% of seasons, vs 1.9% at Cmd 2).
2. A fired Trigger means the season is **not clean** → Institutional Consolidation's deterministic +1 is **withheld**.
3. So at Cmd 3, recovery is suppressed ~17% of seasons while losses land — and over 20 seasons that compounds into **22.6% collapse**, versus near-immunity at Cmd 2.

**This is the same non-monotonicity as CC-1, now confirmed at the outcome (collapse) level with a canonically-grounded recovery model.** It is a genuine, counterintuitive balance finding: **the faction most likely to collapse under sustained pressure is the *mid-tier* one (Cmd 3), not the weakest** — because the weak faction is shielded by Trigger-5 Condition A/C *and* recovers automatically, while the mid-tier faction trips the pool ≥ 6 cliff that both costs Stability and denies it the clean-season recovery.

---

## §4 — Updated findings

| # | Finding | Confidence | Status change |
|---|---|---|---|
| CC-4 | Faction Stability-recovery mechanic EXISTS: §1.3 Institutional Consolidation, **deterministic +1 on a Trigger-free season** (canon explicitly "replaces the abstract simulator recovery rule"). | high | **CC-4 CLOSED.** My "unspecified" was wrong (unread). ED-877 → resolved-was-unread. |
| CC-5 (NEW) | The CC-1 Trigger-5 cliff **propagates to faction collapse**: compound collapse jumps ~25× from Cmd 2 (0.9%) to Cmd 3 (22.6%), then declines at Cmd 4 — because the pool ≥ 6 cliff fires Trigger-5, which **denies the deterministic clean-season recovery**. Mid-tier factions are the most collapse-prone, not the weakest. | high (canonical recovery model; SANITY passes) | NEW — strengthens ED-876 to a collapse-level finding |
| CC-2 (updated) | Weak-faction compound does not spiral — mechanism is now complete: starved Trigger-5 input **+** deterministic Institutional Consolidation recovery the input can't overcome. | high | refined |

**Net:** the compound-collapse magnitude question — which I declined to answer last pass because the recovery model was unspecified — is **now answered**, because the recovery model is canonical (and stronger/simpler than I'd modeled). The honest negative result (CC-4) converted into a positive one by reading the section I'd missed.

---

## §5 — Ledger impact

- **ED-877** (the consolidated master's "recovery mechanic unspecified" P1): **reclassify to resolved — was unread**, recovery mechanic is faction_layer §1.3 Institutional Consolidation. Note for the JSONL consolidation owner: do **not** file ED-877 as an open gap; file as a resolved note pointing at §1.3, OR drop it.
- **ED-876** (Trigger-5 non-monotonic cliff, P2): **strengthen** — the cliff is not just an exposure curve; it propagates to a ~25× swing in faction collapse (Cmd 2→3) via clean-season-recovery denial. The smoothing recommendation (severity scaled by margin rather than a hard pool ≥ 6 auto-fire) is now backed by an outcome-level magnitude, which raises its priority — **consider P2→P1** given a single attribute point swinging collapse 25× is a robustness defect.
- These update the consolidated master (`ledger_candidates_consolidated.json`); not appended to the live ledger (JSONL migration owns it).

`[CONFIDENCE: high]` — §1 (direct canon read), §2/§3 (canonical recovery model, SANITY passes, 6k-trial MC). The Cmd-3 collapse cliff is the load-bearing new result and is grounded in the verbatim §1.3 mechanic + the recovery-independent CC-1 firing curve.

**Limits:** the sim still uses the [A2]/[A3] qualitative couplings (territory→muster, RS→Stability) — swept earlier, and the §3 Command-contrast is robust across those sweeps because it is driven by the Trigger-5 firing rate, not by [A2]/[A3]. Officer-loss Trigger-5 paths and multi-faction dynamics remain unmodeled.
