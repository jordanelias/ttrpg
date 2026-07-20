# Mode B — Number System Coherence: Settlement / Territory

**Audit date:** 2026-07-13. Scope as in formula_audit.md.

| System | Range | Scale Basis | Analogous Systems | Inconsistency |
|--------|-------|-------------|--------------------|----------------|
| Settlement Prosperity / Defense / Order | 0–5 | Flat 0–5 tracked stat (settlement_layer §1.3) | Province-level equivalents largely retired in favor of settlement grain (Accord now derived, not tracked) | None internally — the three are deliberately co-scaled. |
| Settlement Legitimacy (L) / Popular Support (PS) | 0–7 | Matches the faction 1–7 stat convention (settlement_layer §1.8) | Faction stats (Mandate, Wealth, Military, Influence, Stability, Intel) are also 0–7 | Consistent by design — §1.8 explicitly ports the faction 0–7 scale down to settlement grain. |
| Settlement Weight (`W_s`) | 1–11 (uncapped ceiling that grows with development; see formula_audit F-06) | Composite: base(Type 1–3) + Prosperity(0–5) + FacilityTier(0–3) | No other settlement value uses an additive composite on this range; Faction Mandate (0–7) and settlement L/PS (0–7) are the nearest neighbors but are NOT capped at 11 or normalized before entering the Mandate formula — they pass through the `T/(T+K)` saturation instead | Weight is the one settlement-level number that does *not* sit on a 0–5 or 0–7 rail; it is deliberately open-ended per-settlement mass feeding a saturating aggregate. The doc's own audit trail (`references/canonical_sources.yaml` note on the 2026-05-30 LPS-mandate-ners-audit) already flags this exact "Weight redundancy" as a standing Jordan-reservation item — **no new finding needed, already tracked upstream.** |
| Facility Tier (Wing/Suite/Chamber/Billet capacity) | 0–3 counted tiers, slot counts 0–8 (+ "unlimited" for Billet) | Ladder mirrored from `faction_politics_v30 §1` Hall Tier | Standing track (0–5), Renown (0–10) | The "unlimited (shared/cloister)" Billet row is the only unbounded numeric field in the settlement stat surface besides Weight; consistent with its narrative role (lowest tier, no scarcity pressure), not flagged as an inconsistency. |
| Renown | 0–10 | Cross-faction reputation track (player_agency_v30, referenced by settlement_layer §6.1) | Standing (0–5, per-faction) | Two different player-progression tracks with different ranges (0–10 vs 0–5) map onto the same 5-stage Stature Ladder (§6.1) via *paired* bands (Renown 0–2 ↔ Standing 0–2, Renown 9–10 ↔ Standing 5, etc.) — asymmetric but the doc supplies an explicit crosswalk table, so this is resolved coherence, not an unreconciled redundant lever. |
| Generational Shift | 0–10 | New clock, +1/5 years (settlement_layer §7.1) | MS decay, CI, IP (all roughly 0–100-ish clock scales) | Generational Shift uses a much coarser 0–10 scale than its sibling clocks (MS/CI/IP, all effectively 0–100). This is likely intentional (it only needs 3 named thresholds: 2/4/6), but it is a fourth distinct clock-scale convention in the same subsystem with no explanatory note tying its granularity choice to the others. **P3 — polish note only, no mechanical harm; the three named thresholds (2/4/6) are unambiguous regardless of the underlying range.** |
| Political Stability (GD-1 victory gate) | 0–∞ cumulative, gated at ≤6 | Cumulative +1 per violence event (geography/victory docs, referenced not defined here) | N/A | Out of scope — defined in `designs/provincial/victory_v30.md`, not one of this audit's target docs. Noted for completeness only. |
| Province Accord | Canonical 0–3 (`peninsular_strain_v30.md` line 144) vs derived formula's actual range 0–5 (`settlement_layer §1.3`, unclamped floor-mean of 0–5 settlement Order) | Two different range statements for the same value, in two different canonical docs | Settlement Order (0–5, the input) | **Direct range mismatch — see gap_register_update.md GAP-14 (P1).** This is the clearest instance in this subsystem of "different scales for analogous concepts" causing an actual defect rather than a benign convention difference: Order's 0–5 scale was never rescaled or clamped before being assigned as the value of a field whose own canonical doc caps it at 0–3. |
| Territory count vs Settlement count | 17 provinces (T1–T17, unchanged since 2026-04-05) vs 36 (stated in settlement_layer §1.1) vs 37 (stated in settlement_layer PART 2, current per PP-726) | Two-tier map | N/A | See gap_register_update.md GAP-05 — the settlement total is stated inconsistently within the *same* canonical document. |
| Governance action Ob | 1–4 (see formula_audit F-08) | Derived from the settlement stat it targets | Standard TN/Ob conventions inherited from core dice system (out of scope) | No redundant lever detected — each of the four governance verbs targets a distinct stat with a distinct Ob formula; no two verbs compete for the same Ob channel. |
| Edge Traversal Cost (settlement_adjacency §1.1) | 0 (Thread-Witnessed) / 1 (Road/River/Coastal) / 2 (Mountain Pass) | Small integer cost | March-budget system in march_layer_v30 (out of scope, referenced only) | See Mode C for the unresolved question of whether this edge-cost system or march_layer's march-budget system is the operative movement resolver — a Mode C/D finding, not a Mode B range inconsistency per se. |
| Temperament α/β | 0.1–0.9 (five fixed pairs, always summing to 1.0) | Continuous weight pair | N/A within scope | Internally coherent; see formula_audit F-13. |

## Redundant-lever check

No genuine redundant difficulty levers (à la "TN × Ob interaction") were found duplicated across the
settlement/territory docs themselves. The one candidate — settlement-adjacency edge cost vs
march_layer march-budget, both purporting to gate settlement-to-settlement movement — is filed as a
Mode C/D interaction gap, not a redundant-lever Mode B finding, because the two systems are not
obviously computing the *same* quantity (one is a discrete per-edge cost, the other a seasonal budget
pool); which one governs is the open question, not whether they duplicate.

## Analogous-but-different-scales check

The Weight (1–11, open) vs L/PS (0–7, closed) pairing is the one place two "how much does this
settlement matter" numbers use genuinely different scale philosophies feeding the *same* Mandate
formula. This is pre-flagged in the corpus's own audit trail (see table above) — **no new action
taken here; already tracked as a standing Jordan-reservation, not re-filed.**
