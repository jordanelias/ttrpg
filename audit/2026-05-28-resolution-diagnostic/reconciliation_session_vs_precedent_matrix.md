# Reconciliation — Session Faction Work × Historical-Precedent Matrix

**Date:** 2026-05-29
**Task:** consolidation (`<document_consolidation>`). Two efforts produced verdicts on the same faction systems and were left **parallel and unreconciled**: (a) this session's internal-mechanical + remediation work (resolver, Trigger-5 fix, collapse sims), and (b) `designs/audit/2026-05-28-sql-index-and-ners/ners_historical_precedent_matrix.md` — an **external/precedent** validation pass. They are **complementary axes, not competing**, but until now nothing linked them, so the project carried two unconnected sources of truth on faction-collapse status. This doc unifies them.
**Source discipline:** all historical-precedent linkages below are **attributed to the matrix** (it cites the scholarship; I did not independently read Tainter / RAND / du Picq / Weber). My contribution is the internal mechanics and the cross-referencing.
**Bias:** `[SELF-AUTHORED — bias risk]`. This reconciliation corrects my own session: I ran Stages 1–4 (internal) and never applied the matrix's Stage 5 (precedent) axis until prompted.

---

## §0 — Headline

The two efforts **agree** wherever they overlap, and the overlap is load-bearing: every faction remediation this session produced is either **confirmed** or **strengthened** by the matrix's historical-precedent verdicts. Two corrections to my own framing fall out (ED-868 was already retracted by the matrix; my collapse sim is confirmatory, not novel), and one **cross-finding** emerges that neither effort had alone (the collapse bound's adequacy is contingent on the resolver decision). One genuine residual the matrix surfaced — the GD-3 insurgency down-path — is the right next target.

---

## §1 — Per-finding reconciliation

| Session finding | My internal basis | Matrix precedent (attributed) | Reconciled status |
|---|---|---|---|
| **ED-876 Trigger-5 cliff fix** (APPLIED, `2327adc4`) | NERS-S + recovery-independent firing curve; removed a non-monotonic `pool ≥ 6` auto-fire (single Command point → 25× collapse) | Entry 7 — du Picq / Clausewitz: routs **propagate but are locally arrested** (reserves, rallying, terrain); bounded contagion is the realistic pattern | **CONSISTENT / backed.** A single Command point causing a 25× collapse swing is *not* a realistic morale-cascade feature — it was a threshold artifact. The fix makes the loop's exposure monotonic, consistent with "propagates but arrestable." Precedent supports the fix; I had argued it only on internal grounds. |
| **ED-865/874 deterministic+stochastic resolver** (CANDIDATE, `07d9f536`) | NERS leverage uniformity (1/√N irreducible for dice; constant slope only via d+s) + Stage-4 | Entry 2 — COIN / defection / contest literature: real seizures/votes/coups are **decided by structural factors with a stochastic tail, not a low-variance coin-flip** | **STRENGTHENED.** Deterministic-odds + stochastic-resolution = *structure decisive, noise a tail* — exactly the empirical pattern. The matrix independently rates the bare-stat roll **R-FAIL** and prescribes routing through structure (its "Lesson 3"). Precedent endorses the direction Jordan chose; the spec gains an external justification it lacked. |
| **CC-4 recovery mechanic** (§1.3 Institutional Consolidation) | My read: deterministic +1/clean season is the damper | Entry 3 cites §1.3 as part of the bounded-loop basis | **CONSISTENT.** Both identify the same canonical damper. |
| **CC-5 / compound Trigger-5 → collapse cliff** | My compound sim (Cmd-3 → 22.6% collapse) | Matrix did not model the multi-system compound | **NOVEL, retained.** Additive to the matrix; not contradicted. The fix is ED-876 (applied). |
| **ED-868 collapse loop** | My collapse-recovery sim (reachability) | Entry 3 — Tainter: collapse = simplification + reconstitution, **NOT annihilation**; matrix already **RETRACTED** the diagnostic's Lesson-5 | **RECONCILED (corrects me).** The matrix settled the *existence* question top-down before my sim. My sim is **confirmatory + adds reachability** (territory is the binding gate; reconstitution is resolver-dependent). Lesson 5 stays **retracted**; no new safeguard. |
| **ED-880 Varfell reconciliation** (APPLIED, `7e1699f2`) | Repo investigation (Cultural Reclamation live; "purely military" stale) | Entry not in matrix (identity/canon, not a resolution mechanic) | **No precedent axis required** — documentation reconciliation, orthogonal. |

**Net:** zero conflicts. Every overlap is agreement; the matrix strengthens the resolver case and corrects my ED-868 framing.

---

## §2 — The cross-finding (neither effort had it alone)

Combining the matrix's Tainter-bounded verdict with my reachability sim yields a result **neither produced independently**:

> **The collapse-loop bound (Reconstitution) is adequate only under the deterministic+stochastic resolver.** Under bare dice, a collapsed faction at low Influence (the likely post-freeze state) reconstitutes with near-zero probability (P ≈ 0.004 at Influence 3) — *effectively extinction despite a paper recovery path*. Under d+s, the same faction recovers meaningfully (Influence 4 → 0.54).

This **links ED-868 to ED-865/874**: adopting the resolver is not only a Domain-Action-degeneracy fix — it is also what makes the faction-collapse bound genuinely reachable rather than nominal. It is a **second, independent argument** for the resolver decision, and it means ED-868's "resolved-bounded" status is *contingent* on that decision. Recorded in `sim_collapse_recovery_results.md §2–3`.

---

## §3 — Method reconciliation: fold in Stage 5

My session ran the resolution-diagnostic skill's **Stages 1–4 only** (internal: locate defect → lessons → NERS → re-test). The matrix demonstrates and proposes **Stage 5 — Historical-precedent validation** ("does the mechanic behave like the real phenomenon it models? validate against real history/science, never genre convention"). The answer to *"are you validating against the historical research?"* is, at the method level: **the skill should require it.** Folding Stage 5 into `valoria-resolution-diagnostic/SKILL.md` makes precedent a standing axis rather than an ad-hoc pass — applied as a companion skill patch alongside this reconciliation.

---

## §4 — Genuine residuals the matrix surfaced (next targets, owner-authored)

These are **not** closed by my session and are better-grounded than further faction-collapse work:

1. **GD-3 insurgency down-path** (matrix entry 4, **RAND *How Insurgencies End*** — insurgent defeat is the *modal* outcome; sanctuary/sponsor loss the strongest predictor). GD-3 can escalate (Revolt → Insurgency → Faction) but **cannot dissolve** → **R-FAIL**. Recommend multi-path dissolution (military / sponsor-withdrawal / amnesty / persist), sponsor-withdrawal the high-value add. **The strongest next design target.**
2. **MS-engine hysteresis + leading warning signal** (matrix entry 1, **Scheffer/Holling** regime-shift): recovery threshold should sit *higher* than the collapse threshold (currently symmetric); add a diegetic early-warning trend. Metaphysical layer — out of faction scope, flagged.
3. **Minor Δ:** Tainter legitimization-with-diminishing-returns (flavor, low priority); Weber routinization decay for charismatic Accord (low priority).

---

## §5 — Consolidation outcome

- The consolidated master (`ledger_candidates_consolidated.json`) now **cross-references the matrix** as the precedent axis; the two efforts are unified (internal/remediation + external/precedent), no longer parallel.
- **ED-868** marked **resolved-bounded** (matrix/Tainter) with the resolver-contingent reachability note.
- **ED-865/874** annotated with the precedent backing (matrix entry 2) **and** the second justification (collapse-bound reachability, §2).
- **ED-876** annotated with the morale-cascade precedent backing (matrix entry 7).
- **New residual** logged: GD-3 down-path (RAND), as the next target.
- Method: Stage-5 skill patch staged as a companion change.

`[CONFIDENCE: high]` — the reconciliation mapping (both documents read in full this session). The precedent claims are the matrix's, attributed; the internal-mechanics claims are this session's, cited to canon.
