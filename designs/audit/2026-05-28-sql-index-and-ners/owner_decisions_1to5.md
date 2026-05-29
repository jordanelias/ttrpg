# Owner-Decision Resolution (items 1–5)

**Date:** 2026-05-28. **Task:** audit. Resolves/advances the five open decisions from `passC_synthesis.md §4`. Items 1–2 locked per Jordan; 3 reviewed in the long-term-play frame; 4–5 validated top-down against historical precedent (cited). `[SELF-AUTHORED — bias risk]` on the sim; `[CONFIDENCE: high on structure, low on absolute MS rates — illustrative, pending the repo mc engine]`.

---

## 1 + 2 — LOCKED (MS direction, start value, Warden Mending)

**Decision (Jordan):** game-time MS **net-decays by default** absent intensive effort; **start MS = 60** (resolves the 60-vs-72 contradiction → 60); **passive Warden Mending** exists but is **degradable by Warden interruption** (e.g. Edeyja pulled from the Southernmost).

**Resolves the DC-2 cluster:** the canon contradiction (ms_trajectory "always positive" vs clock_registry "↓ decay, start 72" vs sim −1/yr) is settled toward **net-decay, start 60.** `ms_trajectory §2`'s "Force 1 always positive" is **historical-only** and must be annotated as not describing game-time net direction. clock_registry start-MS **72 → 60.** The sim's `MS_BASELINE_DECAY_PER_YEAR=−1` is **correct in sign** (confirmed intended).

**Canon already supports the Warden-Mending mechanism** — no new design needed, just confirmation + an interruption pathway:
- `Mending Sanctuary (WC≥2 + Outpost near Southernmost) → +1 MS/season passive` — this *is* the passive Warden Mending. **Losing the Outpost near the Southernmost breaks the condition → passive Mending stops.**
- `WC3 → Edeyja active Mending +2 MS/season` — Edeyja's contribution. **Displacing Edeyja from the Southernmost removes it.**
- **New (small) design implication:** there must be game events that *can* interrupt Wardens — enemy capture of the Southernmost outpost, Edeyja diverted by a competing crisis, Altonian invasion reaching the south. This makes **Warden placement a defensible strategic asset** and couples cleanly to the arc (the Altonian invasion threatening the south is exactly the dramatic moment passive Mending should drop).

**Sim confirms the model is coherent (start 60, net decay, degradable Warden Mending):**
```
Default peacetime net ≈ −0.41/s → ~142 seasons (~36 yrs) runway to MS≤5  [gentle, long]
Warden availability (decision 2):
  all placed       net −0.41/s → ~36 yrs
  half interrupted net −0.91/s → ~16 yrs
  Edeyja pulled    net −1.41/s → ~10 yrs   (3.5× faster — interruption has real teeth)
```
Net decay is gentle in peace (long runway), accelerates under war/threadwork and Warden loss. ✓ matches "net decay without intensive effort."

---

## 3 — Maintain mitigation, in the long-term-play frame: **KEEP "de-escalate + heal." Do NOT strengthen WC to survive heavy tearing.**

**The question:** does the maintain victory require *de-escalation* (WC breaks even ~6.5/s raw tearing, fails against sustained heavy tearing), or should WC be strengthened so a player can maintain *while* tearing?

**Reviewed against long-term viability — recommend KEEP de-escalate+heal, on four grounds:**

1. **It preserves the core strategic tradeoff, which is what sustains a long game.** With the full corrected model (passive Warden + WC3 + active Mending), maintain net-recovers below ~8–11/s raw tearing and **declines above** (sim D: μ8 → +0.6/s; μ11 → −0.8/s; μ14 → −2.4/s). So a player can hold the world *or* tear it apart at climax intensity — **not both at once.** That tension ("you cannot rip reality apart and mend it simultaneously") is the engine of long-term replay: campaigns oscillate between expansion (MS declines) and consolidation (de-escalate, MS recovers). Strengthening WC to survive heavy tearing **collapses the tradeoff** — MS stops being a constraint, and the long game loses its central pressure.

2. **The long game is viable without strengthening.** From a post-climax MS 20, full maintain (de-escalate + WC3 + active Mending) **recovers to ~100 over 40 seasons and never drops below 5 (100% of runs).** The de-escalate+heal path is not a death sentence — it's a genuine recovery, and the ~36-year peacetime runway (item 1) means a player is never forced to terminal collapse by the clock alone. **Long-term play is sustainable; the player always has the de-escalation lever.**

3. **The maintain *victory* is gated on the Calamity-site grind, not on out-tanking war.** Foundational Mend at Askeheim (Ob 12 ~22%, Master Resonant ~28%, +2 MS/success) yields **~0.4–0.6 MS/season + closure progress** — a slow, deliberate grind. The player's long-game job is to **manufacture enough peace-windows** (de-escalate, protect Warden placement) to work that grind to completion. That's a satisfying long arc; strengthening WC would let players ignore it. `[GAP: the maintain-victory closure condition — how many successful Foundational Mends / what wound-reduction = "Calamity resolved" — is not specified in canon. Recommend Jordan set it knowing the grind rate above: e.g. N successful Foundational Mends, or reduce a site "wound" counter to 0 at +1/success → at ~28% that's ~3.5 seasons of focused attempts per point.]`

4. **It matches the intended narrative arc.** The decline → near-civil-war → invasion → unification → slow MS decline → Calamity-recurs arc *is* an oscillation between tearing and (attempted) mending. De-escalate+heal makes that arc mechanically real; survive-while-tearing would flatten it into "ignore MS."

**Bottom line for #3:** the WC mitigation is correctly calibrated as-is. **Maintain = de-escalate + protect Wardens + grind the Calamity Mend.** The one thing to *add* is not WC strength but the **closure condition** for the maintain victory (the `[GAP]` above — your call on the threshold).

---

## 4 — Insurgency dissolution (GD-3 Stage 3/4 down-path): top-down historical validation → **multi-path dissolution**

**Precedent (cited).** The counterinsurgency literature (RAND, *How Insurgencies End*, 89 cases) finds insurgencies end in **three ways: military victory (either side), negotiated settlement, or stalemate** — and these can manifest at any time during the course of an insurgency. Empirically the majority of insurgencies from 1815 to 2010 ended in defeat for the insurgents, and the **single strongest predictor of insurgent defeat is loss of sanctuary / external sponsorship** — withdrawal of state sponsorship can cripple an insurgency, typically leading to its defeat. Negotiated outcomes are now more common than battlefield ones post-1980, but remain a minority (one dataset: 12% ended through negotiations favoring the regime and only 7% favoring the rebels, with another 20% ending in a balanced way).

**Validation of the current pipeline.** GD-3 models the *up-path* (Revolt→Insurgency→Faction) well but has **no down-path** — historically incomplete, since most insurgencies end in *insurgent* defeat. The two candidates I'd surfaced map onto two of the three real exit modes; precedent says **use multiple paths, not one:**

| Real exit mode | Maps to | Proposed GD-3 dissolution trigger |
|---|---|---|
| **Military defeat** (most common) | Candidate A (territorial count → 0) | Insurgency dissolves when its controlled-territory count hits 0 (crushed) |
| **Loss of sanctuary/sponsorship** (strongest predictor) | *(new — precedent-driven)* | If the Insurgency's external backer (a sponsoring Faction / RM source) is itself suppressed or withdraws, Insurgency drops Stage 3→2 within N seasons (the "withdrawal of sponsorship" collapse) |
| **Negotiated reintegration** (minority, rising) | Candidate B (Legitimacy<1 + count<2) | Low-Legitimacy, low-territory Insurgency can be offered amnesty/reintegration → dissolves to a political actor (not destroyed) |
| **Stalemate** | *(emergent)* | If none fire, it persists — a chronic Insurgency (canon-faithful; ~10-yr average duration) |

**Recommended shape (for your decision):** dissolution is **not a single condition** — it's whichever of {territory→0, sponsor-withdrawn, amnesty-at-low-Legitimacy} fires first, else it persists. This matches precedent (multiple exits, insurgent defeat the modal outcome, sponsorship-loss decisive) and gives the player **levers** (cut the sponsor, grind territory, or negotiate) rather than one scripted off-ramp. The **sponsor-withdrawal path is the highest-value add** — it's the strongest historical predictor and creates strategic depth (attack the backer, not just the insurgent). Staged ED (`[DRIFT]`, B6):
```yaml
- id: ED-<next>  severity: P2  system: insurgency_pipeline / GD-3
  type: missing_mechanic  resolution: proposed (Jordan to confirm)
  summary: Stage 3/4 dissolution — multi-path per COIN precedent (RAND How Insurgencies End).
  paths: [territory_count→0 (military defeat); sponsor suppressed/withdrawn → Stage3→2 in N seasons
          (strongest predictor); amnesty at Legitimacy<1 & territory<2 (negotiated reintegration);
          else persists (stalemate, ~10-yr avg)]
  status: open
```

---

## 5 — Defection cascade (L-DEFECT, npc_relational_graph B1.2): top-down historical validation → **the current model is precedent-correct; build it as specced + add a sponsorship/"losing-side" signal**

**Precedent (cited).** The game's defection model is explicitly the KOEI/*Romance of the Three Kingdoms* officer-network model; the political-science literature on real defection cascades validates that design closely:
- **Expectation-driven, not preference-driven.** Professional armed forces are susceptible to cascades driven by expectations rather than preferences; the institution's stance is highly sensitive to small events that shape officers' beliefs about colleagues' likely behavior — the mutiny of a handful of officers can tilt the institution as a whole, and flows of information are decisive. This is exactly a **tier-1 → tier-2 → tier-3 strain cascade triggered by a focal break.**
- **Bandwagoning toward the winning side.** A key factor is bandwagoning: when segments of the military recognize they are fighting on the "losing side" — that their government will inevitably succumb — the risk of defection surges. Validates **valence-isolation** (defect *away from* the weakening principal) and argues for a **"perceived-fragility" signal** as a cascade amplifier.
- **Sponsorship/ally signal.** An unwillingness of international allies to help a struggling government signals security forces that their principal will not prevail (e.g. Gorbachev staying idle in 1989 spurring East German defections) — the same sponsor-withdrawal lever as #4, on the relational layer.
- **Defection is decisive for collapse.** If defections are not addressed and continue to spread, or if the armed forces as a whole side with a rebellion, the effects can be devastating — often resulting in the regime's collapse. Confirms the cascade *should* be load-bearing (and that suppression/addressing it early is the damper).

**Validation of the current model.** `npc_relational_graph_v30 §7` already has the right topology — focal break → tiered strain → faction-Cascade decrement, with strain decay, half-rate valence-isolated spillover, and tier-3 gated on 3+ tier-2 breaks. **Precedent endorses every one of these.** The defect is purely that **it's unbuilt (B1.2 hooks-only)** — so the recommendation is *build it as specced*, with two precedent-driven refinements:
1. **Add a "perceived-fragility / losing-side" multiplier** to defection probability — when the principal Faction is visibly failing (low Stability, recent territory loss, sponsor withdrawn), cascade likelihood surges. This is the single most-supported finding in the literature and makes cascades fire at the dramatically right moment (a faction already losing tips fast — the bandwagon).
2. **Decisive early suppression halts it** (the damper, historically real): addressing the *first* defection (a show of strength / re-securing the focal node) resets tier-1 strain before it propagates — which the existing strain-decay mechanic already approximates; make it explicit that a successful response to the focal break stops the cascade.

**Recommended shape (for your decision):** keep the specced cascade; make defection probability a function of (focal-break severity) × (principal perceived-fragility) with valence-isolation; decisive suppression of the focal break is the brake. This is faithful to both the KOEI model and the empirical record. **The build itself (B1.2/B1.3) is the action item — a PP, your scheduling call.** Staged ED (`[DRIFT]`, B6):
```yaml
- id: ED-<next>  severity: P2  system: npc_relational_graph (B1.2/B1.3)
  type: incomplete_mechanic  resolution: validated against precedent; build as specced + 2 refinements
  refinements: [perceived-fragility/losing-side multiplier on defection prob (bandwagoning — strongest
                empirical finding); decisive suppression of the focal break halts the cascade (damper)]
  status: open
```

---

## Consolidated status after this pass
- **1, 2:** LOCKED → annotate ms_trajectory/clock_registry (direction + start-60), confirm Sanctuary/WC3 as passive-degradable Warden Mending, add Warden-interruption events.
- **3:** RESOLVED → keep de-escalate+heal (no WC buff); **only open piece = the maintain-victory closure threshold** (your call; grind rate provided).
- **4:** PROPOSED → multi-path dissolution (military / sponsor-withdrawal / amnesty / else-persist); sponsor-withdrawal is the high-value add. Your confirm.
- **5:** VALIDATED → current model is precedent-correct; build B1.2/B1.3 as specced + fragility-multiplier + suppression-brake. Your scheduling.
- **Still open from passC (unchanged):** the −10/s **cap** is still formally the params-vs-§5 contradiction — decisions 1–2 imply gentle *baseline* decay but don't settle the heavy-tearing cap; my recommendation (adopt −10/s as the explicit Force-3 guardrail) stands and is consistent with everything above. Remaining audit reads (clock_registry/DC-12, BG fuses/DC-3, faction_behavior §3.2/DC-6, faction remainder, PENDING-system NERS, per-loop gain computations, real mc run) are unaffected.
```
```
