# Insurgency Dissolution Down-Path — Design Proposal (Tested Candidate)

**Date:** 2026-05-29
**Resolves:** ED-881 (GD-3 has no down-path → NERS R-FAIL) and the insurgency-pipeline forward-flags **INSURGENCY-DISSOLUTION-001** (§6.2) and **INSURGENCY-PROMOTED-DISSOLUTION-001** (§6.3).
**Status:** **PROPOSAL — ratify-or-tune. NOT written to canon.** GD-3 is mutable canon (§B) requiring explicit Jordan ratification logged in the editorial ledger; the insurgency pipeline doc marks these flags "Jordan author." This document is the tested candidate; adopting it (and the parameter values) is Jordan's call.
**Sim:** `sim_insurgency_dissolution.py` (this folder), 8k-trial MC.
**Method:** Stage 1 (the gap), Stage 4 (re-test for new defects), **Stage 5 (historical-precedent validation)** — the axis now canonical in the diagnostic skill.
**Precedent (attributed to `ners_historical_precedent_matrix.md` entry 4, citing RAND *How Insurgencies End*, 89 cases):** three exits — military / negotiated / stalemate; **insurgent defeat is the modal outcome; loss of sanctuary/sponsorship is the strongest predictor of defeat.**
**Bias:** `[SELF-AUTHORED — bias risk]`. §4 reports the two defects this candidate had on first pass (found and fixed by Stage-4 testing) and the residual tuning sensitivity.

---

## §0 — Headline

The insurgency pipeline specifies the up-path fully but leaves dissolution as open forward-flags, and the two pre-staged options (territories→0; Legitimacy<floor ∧ base<2) are both **threshold mechanics that miss the dominant real-world driver — sponsor/sanctuary withdrawal.** This candidate adds a **four-path dissolution** (military defeat / sponsor withdrawal / amnesty-negotiated / persist) that subsumes the pre-staged options as the "military" exit and adds the RAND-dominant sponsor path. Tested, it reproduces the RAND outcome mix: **defeat modal, sponsor-loss the dominant defeat driver, negotiated settlement a real minority, stalemate reachable.**

---

## §1 — The gap (Stage 1)

GD-3 and `insurgency_pipeline_v30` fully specify Revolt → Insurgency → Faction (the up-path), but:
- **§6.2 (Stage 3 dissolution)** offers two pre-staged options — *Option A:* dissolve at 0 territories; *Option B:* Legitimacy < 1.0 ∧ territories < 2 — and forward-flags the choice to Jordan.
- **§6.3 (Stage 4, promoted-faction dissolution)** is fully open.

Per the precedent matrix (RAND), an insurgency that can only escalate and never dissolve **cannot represent the modal real outcome (insurgent defeat)** — NERS **R-FAIL**. The pre-staged options also miss RAND's strongest finding: **sanctuary/sponsor loss is the dominant defeat predictor**, and neither Option A nor B models sponsorship at all.

---

## §2 — The candidate (PROPOSED)

A promoted/insurgent entity dissolves via the **first** path to trigger at Accounting, evaluated in order:

| # | Path | Trigger | Subsumes / adds |
|---|---|---|---|
| 1 | **Military defeat** | territorial base eliminated (territories → 0), **or** Legitimacy < floor with a shrunk base (territories < 2) | **Subsumes** pipeline Options A + B as the "military" exit |
| 2 | **Sponsor withdrawal** | a *real external sponsor* is lost (sponsor faction collapses / signs a treaty renouncing support / is itself defeated); without sanctuary, Legitimacy decays each season and the entity dissolves on crossing the floor | **NEW — the RAND-dominant path, absent from the pre-staged options** |
| 3 | **Amnesty / negotiated** | the controlling/parent faction offers terms; accepted via a contested social resolution; the insurgency dissolves into the political settlement | **NEW — the negotiated exit; deliberately a minority outcome** |
| 4 | **Persist (stalemate)** | none of the above this season | **NEW — matches RAND's stalemate exit** |

**Mechanical hooks (all reuse existing systems):**
- Sponsor withdrawal keys off events that already exist: faction **collapse** (ED-675), **treaty** signature (the treaty system), or **military defeat** of the sponsor. No new entity needed — any faction can be a sponsor via an informal-alliance flag (insurgencies already "negotiate informal treaties/alliances," pipeline §4.3).
- The no-sanctuary **Legitimacy decay** uses the same Legitimacy stat the pipeline already tracks.
- Amnesty acceptance uses the **deterministic+stochastic resolver** candidate (a contested social resolution: parent Mandate vs insurgency Resolve) — another reason the resolver decision (ED-865/874) is load-bearing.
- The "military defeat via Legitimacy floor + shrunk base" branch **is** pipeline Option B, preserved.

---

## §3 — Test results (Stage 4 + Stage 5)

8k MC, sponsored insurgency, moderate suppression, baseline params:

| Path | Baseline share |
|---|---|
| Military defeat | 0.38 |
| Sponsor withdrawal | 0.59 |
| Amnesty negotiated | 0.03 |
| Persist | 0.00 |

**Total defeat (military + sponsor) = 0.97 — modal, as RAND requires.** Sponsor-loss is the dominant defeat sub-driver (0.61 of defeats).

**Sponsor-dependence (the RAND signature):** varying P(sponsor-loss/season) 0 → 0.20 shifts the modal fate from military defeat (0.88 at no sponsor-loss) to sponsor withdrawal (0.78 at high sponsor-loss). **This reproduces "sanctuary loss is the strongest predictor of defeat."**

**Stage-4 new-defect checks (all PASS):**
- Not immortal: under heavy pressure, persist → 0.00.
- Stalemate reachable: under no pressure + no amnesty, persist = 0.73 (RAND's stalemate exit exists).
- No-sponsor insurgency correctly shows sponsor_withdrawal = 0.00 (a never-sponsored entity cannot take the sponsor path).
- Outcomes partition (sum = 1.00).

**Stage-5 (precedent) verdict:** **MATCH.** Defeat modal, sponsor-loss dominant among defeats, negotiated settlement a real minority, stalemate reachable — the full RAND outcome structure.

---

## §4 — Stage-4 self-critique (defects found + fixed, and the residual)

**Two defects this candidate had on first pass — found by testing, fixed before proposing:**
1. **Sponsor-path misattribution.** The first version attributed the Legitimacy-collapse branch to "sponsor withdrawal" whenever the entity currently had no sponsor — which wrongly tagged *never-sponsored* insurgencies' military defeats as sponsor losses (no-sponsor runs showed an impossible 0.30 sponsor share). Fixed by tracking "a real sponsor was lost" separately from "currently has no sponsor."
2. **Amnesty over-fired and was wrongly modal** (51% on first pass), contradicting RAND's "defeat is modal." Fixed by tightening the amnesty gate (only once Legitimacy is genuinely wavering), making committed cells resistant (a sponsored insurgency has no reason to settle; an acceptance rate even when terms make sense), so amnesty became the intended minority exit (3%).

**Residual tuning sensitivity (flagged, Jordan's call):** at baseline the sponsor sub-path (0.59) slightly exceeds military defeat (0.38). Defeat is modal *in aggregate*, and sponsor-loss being the single largest sub-path is faithful to RAND — but the split is **sensitive to the assumed P(sponsor-loss/season)**, which is a PROPOSED value, not a measured one. **This is the key tuning knob:** a designer who wants military suppression to feel like the primary defeat route would lower P(sponsor-loss); one who wants the historical "cut off their sponsor" dynamic to dominate would keep it. The *structure* is the proposal; the *split* is tunable.

**Limits:** the sim abstracts the sponsor as a Bernoulli withdrawal rather than modeling the sponsor faction's own decision-making (a sponsor withdraws for its own strategic reasons — unmodeled). Multi-insurgency and the interaction with GD-2 mandatory threat-response are not simulated. Amnesty terms (what the parent concedes) are not specified — only that the path exists.

---

## §5 — Ledger impact

- **ED-881:** **resolved-candidate** — tested four-path dissolution proposal, RAND-validated, ready for Jordan ratification. Completes pipeline forward-flags INSURGENCY-DISSOLUTION-001 (§6.2) and INSURGENCY-PROMOTED-DISSOLUTION-001 (§6.3).
- **Not written to canon:** GD-3 (§B) and the pipeline doc require Jordan ratification; on adoption, the changes land in `canon/02 §B GD-3` (add the down-path clause), `insurgency_pipeline_v30 §6.2–6.3` (replace the forward-flags with the ratified mechanic), and `canonical_sources.yaml` (co-file).
- **Cross-dependency noted:** the amnesty path uses the deterministic+stochastic resolver (ED-865/874) — another reason that decision is load-bearing.
- Recorded in `ledger_candidates_consolidated.json`; not appended to the live ledger (JSONL migration owns it).

`[CONFIDENCE: high]` — the gap, the four-path structure, the RAND match, and the Stage-4 defect-fixes. `[CONFIDENCE: medium]` — the specific parameter values and the sponsor-vs-military split (the flagged tuning knob, Jordan's call).
