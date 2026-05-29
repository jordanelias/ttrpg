# NERS × Historical-Precedent Validation — Comprehensive Pass

**Date:** 2026-05-28. **Task:** audit (bootstrapped). **Method:** bottom-up NERS (each verdict cites the canonical mechanic from this session's full reads) + top-down validation against **real historical/scientific precedent, not videogame precedent** (genre convention is derivative and frequently unrealistic, so it is the wrong yardstick for a game whose stated intent is *believable emergent narrative*). `[SELF-AUTHORED — bias risk]` throughout; treats all prior work, mine and the diagnostic skill's, as falsifiable.

## Methodology (proposed standard — upgrade to `valoria-resolution-diagnostic`)
The skill's Stage 4 is an *internal* re-test (does a fix break something else). It has **no external validation axis.** This pass adds one:

> **Stage 5 — Historical-precedent validation.** For each true finding / system verdict, identify the real-world phenomenon the mechanic models and ask: *does the mechanic's behavior match how the phenomenon actually behaves?* Match → strong evidence for **R** (the system will produce believable emergence). Divergence → a finding (either the mechanic is unrealistic, or the divergence is a deliberate, defensible game-feel choice — decide which). **Validate against real history/science, never genre convention.**

**Scope boundary (honest):** precedent validates cleanly for **political/military/social/religious** systems. The **metaphysical layer** (threadwork/MS/Calamity) has no direct historical analog — validated *analogically* against systemic-dynamics precedent (Tainter collapse; ecological regime-shift). I do not fabricate historical analogs for the magic itself.

---

## The matrix

Legend: verdict per criterion; **bottom-up** = cited canonical mechanic; **precedent** = real-world check (cited); **Δ** = divergence finding.

### 1. Threadwork / MS engine — metaphysical (analogical validation)
- **Bottom-up:** two-force model — Force 1 baseline-positive, *small*, larger at low MS (ms_trajectory_v1; ~+13/257yr); Force 2+ tearing (warfare flat cap −3/s; Gap-bleed per-scale 1/2/3/5; Foundational ×3); net-decay default, start 60; bands Fragile/Fractured/Critical; −10/s cap (contested); Mending recovery (passive Warden + active ops).
- **Precedent — ecological regime-shift / alternative stable states (Scheffer, Holling):** real complex systems under stress show **distinct collapse (F2) and recovery (F1) thresholds with hysteresis** — *the reverse path is not the same as the forward path; returning to the original conditions does not restore the original state; you must over-correct past a different bifurcation point.* They also show **"warning signals" before tipping** and **disproportionate (non-linear) response near thresholds.**
- **Validation:** **strong match.** MS bands = ball-in-cup basins; the Pass-C finding that *maintain requires de-escalation, not just stopping the tearing* **IS hysteresis** — exactly the empirical signature. The Fragile→Fractured→Critical non-linear acceleration matches "disproportionate response near thresholds."
- **Δ-finding (precedent-driven, NEW):** real regime-shifts have **leading warning signals** (critical slowing, rising variance). Valoria's MS bands are *state* labels, not *early-warning* signals. **Recommend a diegetic warning signal** (e.g. rising Shifting-Object frequency / variance as MS approaches a band edge) — already partially present (Fragile = "spontaneous Shifting Objects"), make it a *legible trend* the player reads, not a step. Improves S and E (player can intuit the approaching tip). Also: hysteresis argues the **recovery threshold (F1) should sit higher than the collapse threshold (F2)** — i.e. once MS drops into Fractured, climbing back out should require reaching a *higher* MS than the level at which you fell in. Currently bands are symmetric. *Owner decision: add explicit hysteresis to the band edges?*
- **NERS:** N pass · **R pass iff cap holds** (else instakill, fails R — the contested cap decision is load-bearing) · S pass (+improves with warning-signal) · E pass.

### 2. Faction action layer — political (clean validation)
- **Bottom-up:** bare faction-stat 1–7D pool rolled for pivotal binary outcomes (seizure, vote) at the small-pool floor; deterministic CI/Legitimacy accounting underneath.
- **Precedent — political contests:** real seizures/votes/coups are **decided by structural factors** (resources, legitimacy, coalitions, force ratios) with a stochastic tail — *not* by a single low-variance coin-flip. The COIN/defection literature is explicit that outcomes track **expectations and structural position**, not noise.
- **Validation:** **the bare-stat roll DIVERGES from precedent.** A 2D binary verdict on a pivotal, irreversible political outcome makes *noise* decisive where history says *structure* is. Confirms the diagnostic's standing finding.
- **NERS:** N pass · **R FAIL** (fragile small-pool binary on load-bearing outcomes) · S fail (dice inconsistent with the deterministic layer) · E fail (uninfluenceable roll). → **Lesson 3** (route the consequence through the accounting layer / aggregate the pool). *Precedent strengthens the case: make structure decisive, noise a tail.*

### 3. Faction-collapse loop — political (clean validation; corrects diagnostic)
- **Bottom-up:** Stability recovery +1/clean season (§1.3); Survival Exception 1×/campaign (§1.5); **reconstitution within 4 seasons, treaties hold (§1.5→settlement §6.2); Military stat sticky (§1.7).**
- **Precedent — Tainter, *Collapse of Complex Societies*:** collapse is **a return to a lower sustainable level of complexity, not annihilation** — "sociopolitical organization is reduced to the level that can be sustained by local resources"; collapsed societies become *smaller, simpler, less centralized*, and frequently **reconstitute** as successor polities. Also: **peer-polities collapse near-simultaneously** ("no polity can withdraw from the spiral or it is absorbed by a neighbor").
- **Validation:** **strong match.** Reconstitution-not-extinction is *exactly* Tainter's collapse-as-simplification. **Confirms the Pass-B correction** — the loop is bounded; the diagnostic's "undamped terminal, no cap → Lesson 5" is **retracted**. Tainter's peer-polity simultaneity also validates the cross-faction cascade coupling (collapse propagates among interdependent factions).
- **Δ-finding (minor):** Tainter's legitimization mechanism — *under stress, resources shift to legitimization/control with declining returns* — is not explicitly modeled. The CI/Legitimacy track is the hook; consider a "legitimization spending with diminishing returns" pressure as flavor (low priority).
- **NERS:** N/R/S/E **pass on the loop.** Do NOT add Lesson 5.

### 4. L-INSURG (GD-3 pipeline) — political/military (clean validation)
- **Bottom-up:** Revolt→Insurgency→Faction up-path well-defined; **no down-path** (Stage 3/4 dissolution unspecified).
- **Precedent — RAND *How Insurgencies End* (89 cases):** three exits (military / negotiated / stalemate); **insurgent defeat is the modal outcome** (majority 1815–2010); **loss of sanctuary/sponsorship is the strongest predictor of defeat**; ~10-yr average duration.
- **Validation:** up-path realistic; **missing down-path is a real divergence** (most insurgencies end in insurgent defeat, which GD-3 cannot represent). → **multi-path dissolution** (military / sponsor-withdrawal / amnesty / else-persist), sponsor-withdrawal the high-value add (see `decisions_1to5_resolution §4`).
- **NERS:** N pass · **R FAIL** (no recovery path — can escalate, can't dissolve) · S/E pass on the up-path. → build dissolution (owner-authored).

### 5. L-DEFECT (npc relational) — social/military (clean validation; near-exact match)
- **Bottom-up:** focal break → tiered strain cascade → faction-Cascade decrement; strain decay; half-rate valence-isolated spillover; tier-3 gated. Specced but **unbuilt (B1.2 hooks-only).**
- **Precedent — defection-cascade literature (McLauchlin; Dworschak; Barany):** cascades are **expectation-driven, not preference-driven**; "**the mutiny of a handful of officers can tilt the institution as a whole**"; **bandwagoning away from the perceived losing side**; sponsorship/ally withdrawal signals fragility; **decisive early suppression halts it**.
- **Validation:** **near-exact match** — tiered cascade, valence-isolation, focal-trigger sensitivity, suppression-as-damper all endorsed. Refinements: add a **perceived-fragility/losing-side multiplier** (the single most-supported empirical finding) and an explicit **decisive-suppression brake**.
- **NERS:** N pass · **R FAIL on incompleteness** (load-bearing consequence unbuilt) · S/E pass on the design. → build B1.2/B1.3 as specced + 2 refinements (see `decisions §5`).

### 6. L-SPLIT (faction succession) — political (clean validation)
- **Bottom-up:** vacancy → contest → narrow-margin → split into two; re-merge at Mandate 3+; RM emergence 4-season cooldown (untuned).
- **Precedent — succession wars (Diadochi after Alexander; Wars of the Roses; Sengoku; Ottoman fratricide):** contested succession **routinely fragments polities into competing successor states**; fragments **re-consolidate** over time (successor-state coalescence); unmanaged partible succession produces **recurrent fragmentation** (a known failure mode → e.g. why primogeniture/fratricide rules emerged to suppress it).
- **Validation:** **strong match.** Split + re-merge mirrors fragmentation/coalescence; the 4-season cooldown is the analog of succession-suppression rules. The doc's own flag (cooldown "too slow → suppression wins; too fast → RM cascade") is the real historical tension — precedent says **unbounded fragmentation is the danger**, so err toward the cooldown being *present and meaningful*.
- **NERS:** N/R pass · S/E pass · cooldown value PROVISIONAL (smoke-test) — precedent endorses keeping a real brake.

### 7. mass-battle morale sub-loop — military (clean validation)
- **Bottom-up:** rout → contagion −1 Morale to adjacent friendlies, **braked (no further cascade this turn)**; rally/reform recover at phase boundaries.
- **Precedent — battle-morale collapse (Ardant du Picq; Clausewitz; surrender-cascade studies):** real routs **do propagate** (panic is contagious — "the flight begins with the rear"), and **surrender/rout has a documented cascade effect driven by information about adjacent units**, but routs are also **locally arrested** by reserves, rallying, and terrain (they do not always collapse a whole army in one stroke).
- **Validation:** **strong match.** Contagion + per-turn brake + rally/reform recovery mirrors real rout dynamics (propagates, but arrestable). Confirms the bounded verdict.
- **NERS:** N/R/S/E **pass.** (Sim *implementation* has separate P0 stubs — engineering, not design.)

### 8. L-CONV (conviction) — social/psychological (clean validation)
- **Bottom-up (conviction_taxonomy_v30):** 13 Convictions; 1–3 primary at weight 0.6–0.8 + cultural background 0.2–0.4; Self-Other orientation [−1,+1]; drift κ=0.03 bounded; 1 Scar/season cap; crisis at thresholds; multi-Conviction cascade.
- **Precedent — identity/belief change (attitude-change & radicalization literature):** belief systems are **multi-dimensional and weighted**, change is **gradual with occasional crisis-driven reorganization** (conversion/disillusionment), and **identity threat can cascade across linked beliefs**. Bounded drift + threshold-crisis is realistic.
- **Validation:** **match** on the single-Conviction path. The multi-Conviction cascade tail is `[INTENT UNDETERMINED]` — precedent says cascades exist but are rare (most belief change is gradual), so the rarity-gating is realistic; validate the cascade *severity* doesn't over-fire.
- **NERS:** N/R/S/E pass single-path; cascade tail flagged for the axis-matrix read.

### 9. L-MIRACLE (Solmund RWCE / church) — religious (clean validation)
- **Bottom-up:** miracle → Accord +1 (one-time, radius) + SA; Church recognition → SA-gated actions → CI/PI; TD escalation counter-pressure (at TD 3, Church PI loss → Hafenmark PI +1).
- **Precedent — Weber, charismatic authority & its routinization; religious legitimacy:** charismatic/miraculous authority is **real and politically potent but must be routinized into institutions to persist**, and **competing claimants / failed prophecy erode it** (the TD counter-pressure). Religious legitimacy is a **contested, transferable political resource.**
- **Validation:** **match.** One-time Accord (charisma is event-bound until institutionalized) + Church-recognition (routinization) + TD transfer (legitimacy is contested/zero-sum) all track Weber.
- **Δ-finding (low priority):** Weber's *routinization* — charisma decaying unless converted to institutional authority — isn't explicit; the SA-gated-actions path is the hook. Consider SA decaying without Church institutionalization.
- **NERS:** N/R/S/E pass (as read).

---

## PENDING — not yet read; precedent lens identified (honest gaps)
These had only the diagnostic skill's *untested hypotheses*; I will NOT issue NERS verdicts without bottom-up reads. Precedent axis pre-assigned:
- **Personal combat** (dice pools, wounds, Composure) → real combat **lethality & variance** (pre-modern combat is high-variance, morale-driven, quickly decisive); validate the flat −1D wound at the 5D floor (Lesson-2 candidate) + whether variance is realistic without being a coin-flip.
- **Social contest** (5–18D pools, Persuasion Track) → real **negotiation/persuasion dynamics** (incremental, position-dependent, reputation-mediated); validate the clock depth averages out small rolls.
- **Investigation / fieldwork** (deterministic five-filter + Evidence clock) → real **investigative/intelligence process** (deterministic accumulation of evidence, false leads); likely compliant.
- **Victory / peninsula** (deterministic clocks, GD-1) → real **hegemony/unification thresholds** (balance-of-power tipping, bandwagoning to a frontrunner); validate the 11/15 + Accord/Stability gates.
- **Diplomacy** (unread) → **balance-of-power & alliance defection** (already partly grounded via the defection literature); validate alliance stability/abandonment.

---

## Consolidated findings from this pass
- **Retract:** diagnostic's faction-collapse "Lesson 5" (Tainter: collapse = simplification + reconstitution, validated).
- **Confirm:** faction-action bare-stat roll fails R (political outcomes are structure-driven, not coin-flips) → Lesson 3.
- **NEW (precedent-driven), P3 design:** MS engine should expose a **leading warning signal** before band tips (ecological "critical slowing" analog) and consider **explicit hysteresis** (recovery threshold > collapse threshold) — both improve R/S/E and match real regime-shift behavior. *Owner decision on hysteresis.*
- **Validated proposals** (4 insurgency dissolution, 5 defection refinements) — precedent-backed, in `decisions_1to5_resolution.md`.
- **Method:** fold **Stage 5 (historical-precedent validation)** into `valoria-resolution-diagnostic/SKILL.md` — I can stage the skill patch (B6 blocks the commit). It makes precedent a standing axis, not ad hoc.

## Remaining to complete the comprehensive pass
Bottom-up reads for the 5 PENDING systems, then NERS+precedent each; per-loop gain computations (DC-8) still owed for the loops lacking one; clock_registry/DC-12 bounds cross-check; BG fuses/DC-3; faction remainder; real `mc` run for MS pacing. The matrix above covers every system I have canonical grounding for; the rest are honestly marked, not guessed.
