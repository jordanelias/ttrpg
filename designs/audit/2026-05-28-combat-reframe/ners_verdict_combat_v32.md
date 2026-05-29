# NERS Verdict — combat_v32_proposal (state-graph reframe)

`[SELF-AUTHORED — bias risk]` This diagnoses a proposal I built this session. Per the resolution-diagnostic skill's first guardrail, I treat it as external work and actively surface the criticism an independent reviewer would raise — the failure mode here is confirming the reframe "fixed everything." It did not.

> **POST-VERDICT UPDATE (same session):** Per Jordan's directive to address findings in priority order, **F7 was consolidated immediately after this verdict** — the two intra-attack Reading channels (Temporal + Biomechanical) merged into a single **Kinetic** channel (5 mundane → 4), the minimal Lesson-1 fix (combat_v32_proposal §4.5/§6.5/§11.1, §16.4). The verdict below is preserved as the **state at test time** (F7 open) — it is the honest test record, not edited retroactively. **Current proposal state:** F7 addressed; F3, N1, N3, N4, N5 remain per the remediation list.

**Method:** `valoria-resolution-diagnostic` skill, Stages 1–4, applied to designs/proposals/... (v32 working copy). NERS criteria per canon/definitions.yaml. Compared against the v31 diagnostic (designs/audit/2026-05-28-resolution-diagnostic + the v31 follow-up).

---

## Phase 0 — Components

combat_v32 is a composite: **dice** (state-transition resolutions in the bout subgraph; opposed rolls), **deterministic** (σ-space modifier composition, resource economy, handling curves, set bonuses), **clock-ish** (commit-depth chain caps; wound accrual toward MW). The reframe did not change the d10/TN/Ob substrate; it changed how modifiers compose (σ-space) and how the engagement is structured (state graph).

---

## The v31 findings → v32 status (the point of the re-test)

| v31 finding | Lesson | v32 mechanism | Status |
|---|---|---|---|
| **F1** non-uniform absolute modifier impact | 2 | §12.3 σ-space (δσ·σ_N) | **RESOLVED** — verified uniform ~25.8pp impact across 5–18D |
| **F2** compound foreclosure at small pool | 5 | §12.3 soft cap `1.5·tanh(net/1.5)` + state-gating | **RESOLVED** — worst adverse stack lands ~9%, not 0%; no dead-zone (tanh smooth) |
| **F4** "loop winner" undefined | 1 | §4.7/§12.6 explicit terminal states + clash tiebreaker (highest net; tie → both heavily wounded) | **DISSOLVED** — the ambiguous "loop" was replaced by concrete terminal states; the undefined concept no longer exists |
| **F6** over-complexity / E failure | 1-inv | §1 front-loading; §7 36-pair matrix retired; Reaction derived; state-gating | **PARTIALLY RESOLVED** — in-bout load genuinely lower; but total concept count *rose* (see N2–N5). Net E improved for play, mixed for the whole system |
| **F3** Concentration shared combat↔social pool | 5 | — (untouched) | **NOT ADDRESSED** — cross-system; still deferred to I-15 sim |
| **F7** Reading channel over-split | 1 | §4.5 added FoV-scaling but **kept all 7 channels** | **NOT ADDRESSED** — the over-split finding stands; FoV-scaling is orthogonal to channel-count reduction |

So the reframe **resolves the two correctness findings (F1, F2) that drove v31's non-compliance**, dissolves F4, and substantially improves in-bout E — but **F3 and F7 remain open**, and F6 is only partially closed.

---

## Stage 4 — new defects the reframe introduced (the part bias wants me to skip)

Running the diagnostic on the *fix* (not the original), per skill Stage 4. Five new concerns, verified quantitatively where possible:

- **N1 — state-transition modifier discontinuity (S; Lesson 6 in kind).** State-gating drops Stance Counter at the Closing→In-bind boundary. A fighter holding a Strong stance edge sees it vanish at the bind — an effective-Ob swing of **~1.2 (5D) to ~2.2 (16D)** at the transition (verified). It is an *intended, physically-grounded* boundary (the bind forming genuinely changes what matters), so Lesson-6-exempt in *kind* — but the *magnitude* is large and unsmoothed. **MODERATE; sim-check the transition feel.**
- **N2 — soft-cap nonlinearity vs player intuition (E).** Player-facing levels (Minor/Moderate/Strong) are **non-additive** under the cap: Moderate+Moderate = 0.875 eff (not 1.0); Strong+Strong = 1.14. Monotonic with diminishing returns — intuitable as "more stacking, less marginal" — but it does stress NERS-E's "player can intuit complex outcomes." **MILD.**
- **N3 — σ-space methodology divergence (S).** Combat now composes modifiers in σ-space; social/faction/mass resolve modifiers in raw Ob. Attribute-weight *equivalence* is maintained (attribute_weight_standard.md), but the modifier *methodology* is combat-only. NERS-S explicitly wants "calculations consistent in methodology with other mechanics." This is a real smoothness cost the reframe accepted. **MODERATE; either propagate σ-space to sibling systems or document the divergence as deliberate.**
- **N4 — all-or-nothing named-set bonus (E / Lesson 6, build axis).** A 7/8 set grants +0; 8/8 grants the full bonus — a genuine threshold cliff on the *build* axis. Deliberate (legibility: "a set is coherent or it is not"), but a cliff. **MODERATE — `[OPEN TRADE-OFF]`:** a graded partial bonus would smooth it but reintroduce the per-pair summing §7.3 just retired. Pick one.
- **N5 — weapon handling necessity (N).** §8.2 adds a skill-curve dimension (Forgiving/Standard/Demanding). Weapons already differentiate by phase-strength (§8.4) and damage. Is handling *necessary*, or apparatus the system could shed (NERS-N / over-engineering guardrail)? **MINOR–MODERATE — justify against play value in sim, or cut.**

---

## NERS verdict

```
SYSTEM: combat_v32_proposal   COMPONENTS: dice + deterministic + clock (Phase 0)
VERDICT: IMPROVED, NOT YET COMPLIANT — resolves the v31 correctness failures (F1, F2)
         and improves in-bout E, but F3/F7 remain and the reframe adds new S + E concerns.

N: conditional — apparatus largely necessary; N5 (handling) borderline (could be over-engineering)
R: PASS on the v31 fragility (small-pool foreclosure fixed via σ-space + soft cap);
   conditional overall — F3 (shared Concentration) and F7 (Reading over-split) still open;
   N1 transition swing unverified at sim
S: conditional/weakest — N3 (σ-space methodology diverges from sibling systems) and
   N1 (large unsmoothed transition discontinuity) are genuine smoothness costs
E: improved but conditional — in-bout load down (matrix retired, state-gating, named sets);
   N2 (soft-cap nonlinearity) mild, N4 (all-or-nothing set cliff) moderate

REMEDIATION (worst-first):
  MODERATE  N3 σ-space methodology divergence → decide: propagate σ-space to social/faction/
            mass for consistency, OR ratify combat-only σ-space as deliberate (document in canon)
  MODERATE  N1 transition discontinuity → Phase 11 sim; if jarring, soften via brief
            transition blending or cap the per-transition Δ
  MODERATE  N4 set-bonus cliff → Jordan decision: accept legible cliff vs graded partial bonus
  MODERATE  F7 Reading over-split → still requires the Lesson-1 consolidation (independent of FoV)
  MODERATE  F3 shared Concentration → I-15 cross-system sim
  MINOR     N5 handling necessity → justify in sim or cut; N2 soft-cap intuition → playtest read

RE-TEST: the reframe is sound on F1/F2/F4/F6-in-bout; it did NOT clear F3/F7 and it added
  N1–N5. v32 is a real improvement over v31's non-compliant verdict, but "compliant" requires
  closing F3/F7 and resolving N1/N3/N4 — several of which are Jordan decisions, not Claude fixes.
```

---

## Honest bottom line

v32 does what it was built to do: it **fixes the two correctness defects (F1, F2) that made v31 non-compliant**, dissolves F4, and makes the in-bout experience materially simpler (F6). That is genuine progress, verified numerically.

But an independent reviewer would not sign off on "compliant." **F7 (Reading over-split) and F3 (shared Concentration) were never touched by this reframe** — F7 in particular was on the v32 build plan and did not get done; the FoV work is orthogonal to it. And the reframe **bought its in-bout simplicity partly with new costs**: a modifier methodology that diverges from every sibling system (N3), a large unsmoothed state-transition swing (N1), and an all-or-nothing build cliff (N4). Several of these are deliberate trade-offs that only Jordan can adjudicate.

`[CONFIDENCE: high on F1/F2/F4 status and the N1/N2 quantitative checks (verified in-script); medium on the E/S severity calls (they depend on playtest + Jordan's intent for σ-space divergence and the set cliff)]`
`[SELF-AUTHORED — bias risk: I flagged F7 as not-done even though it was my own build-plan item I skipped, and rated S as the weakest NERS axis specifically because the σ-space divergence is a cost of a choice I implemented and would be tempted to defend]`
`[GAP: N1 transition feel, N4 cliff impact, N5 handling value, F3 — all sim/playtest-only or Jordan decisions; not closeable by analysis alone]`
