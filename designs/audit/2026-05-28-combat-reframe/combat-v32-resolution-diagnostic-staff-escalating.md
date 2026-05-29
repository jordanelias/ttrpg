# Combat v32 — Resolution Diagnostic: staff handling (F-W1) + Escalating commitment (F-A2)

Full `valoria-resolution-diagnostic` run (Stages 1–4) on the two flagged sub-components the grounding pass surfaced as priority. This is the deeper "test" the grounding pass pointed at: where grounding asked *does it match history?*, this asks *does it hold up under stress, and is it NERS-compliant?*

`[SELF-AUTHORED — bias risk]` combat_v32 is prior-Claude work; per the skill's first guardrail it is treated as external and the criticism an independent reviewer would raise is surfaced, not softened. **Remediations below are lesson-mapped *options for Jordan*, not decisions** (project-owner contract: Claude does not invent design decisions). `[RuntimeError: none fired this session.]`

**Prerequisites met:** `assert_bootstrap()` via `quick_bootstrap` (token 354e18e7f2f4f489); `task_gate('audit')` PASS; canonical mechanics fetched this session (`combat_v32_proposal §6.8/§8.2`, `§7.2`); `canon/02_canon_constraints.md` fetched (gate). All quantities below are computed from the **verified** §8.2 handling table and §7.2 reaction formula — not from memory.

---

## VERDICT (both items, read first)

- **F-W1 (staff handling): true finding — fails NERS-R (build viability at high skill).** The Forgiving/Standard/Demanding *system* is sound; the *staff's assignment to Forgiving* is the defect. A master staff-fighter is locked **2 handling points below** a master rapier-fighter (computed), so a high-Proficiency staff build is dominated on the handling axis — it does not "hold at its extremes." This is a balance + grounding finding, **not** a resolution-engine defect, and **not** any of Lessons 1–6 (the Forgiving curve is a deliberate, legible absolute effect, which Lesson 2 exempts). **P2.**
- **F-A2 (Escalating commitment): the diagnostic CLEARS the scary reading and surfaces a quieter one.** Escalating is a *bounded* forced ramp (caps at depth 5) → it is **not** an undamped-and-unbounded loop → it **passes Lesson 5** (it is not the death-spiral it superficially resembles). But it is a **trap option**: the defender's advantage grows monotonically to **+0.80δσ at forced depth 5** (Yielding), so Escalating gets *worse the longer it operates*, with no pull-back. A strategy that is strictly self-defeating is apparatus players will avoid → **fails NERS-N (necessity)**. Plus it is the one historically-ungrounded spec. **P2–P3.**

Neither is a P1 engine break. Both are design-quality findings on a **proposal** (not ratified canon).

---

## DIAGNOSTIC 1 — STAFF HANDLING (F-W1)

**Target:** the `Long pole (staff)` weapon class's handling assignment (`§8.2`: **Forgiving**), within the Forgiving/Standard/Demanding handling subsystem. Mechanic category: a **base-parameter→pool conversion** (Proficiency `P` → handling `H` → dice Pool contribution).

### Stage 1 — diagnostic (Phase 0–6)

- **Phase 0 (decompose):** deterministic Proficiency→Pool conversion feeding dice-resolved sub-actions. The conversion curve is the component under test.
- **Phase 1 (stress point):** *not* the small-pool floor (that is the dice engine) — the stress point is the **high-Proficiency end (P=6–7)**, where the Forgiving cap (H=3) is maximally below the blade ceilings. Two sources: by-design (cap fixed at 3) and by-comparison (vs Demanding's 5).
  - **1b exposure:** any *dedicated* staff player pushes Proficiency high through progression → the stress point is reached **routinely by every staff specialist**, not an edge case.
- **Phase 2 (what it decides):** a **graded-magnitude, permanent Pool penalty**. Computed gap (best-blade H − staff H), verified from §8.2:

  | P | Forgiving (staff) | Standard (longsword) | Demanding (rapier) | best-blade − staff |
  |---|---|---|---|---|
  | 1–2 | 2–3 | 1–2 | 0–1 | **−1 (staff ahead)** |
  | 3 | 3 | 3 | 2 | 0 (crossover) |
  | 4–5 | 3 | 4 | 3–4 | **+1** |
  | 6–7 | 3 | 4 | 5 | **+2** |

  - **2a outcome type:** graded magnitude (a 2D weapon-contribution deficit at mastery), **permanent** for the staff specialist.
  - **2b stakes & reversibility:** build viability; **irreversible** within the weapon choice (the only "fix" the player has is to abandon the staff).
  - **2c risk profile:** Impact **H** (2D permanent deficit is large), Exposure **H** (routine for staff specialists), Irreversibility **H** (structural; cannot be trained around). **(H, H, H) — three-high candidate finding.**
- **Phase 3 (curves):** 3a — the Forgiving cap is non-uniform across P (helps low, hurts high), but this is the *intended* floor/ceiling design (the proposal notes the echo of MaxWounds/Power stepping) — a **deliberate, legible absolute effect, which Lesson 2 EXEMPTS**. So the *mechanic* is not the defect. 3b — no cliff (smooth cap). 3c — no role conflation.
- **Phase 4 (loops):** none (handling is static per weapon).
- **Phase 5 (intent gate):** the assignment **is deliberate** — the proposal states a rationale ("accessible percussive control"). But the rationale **contradicts the weapon's historical standing** (Silver ranks the short staff a *superior* weapon; the Chinese *gùn* is a master's weapon — `combat-manuals-seven-axes-throughlines.md`), and there is **no paired safeguard** offsetting the high-P deficit. Per the skill: *deliberate without adequate safeguard → true finding (intent good, execution unsafe).* The intent (an accessible weapon) is fine; making **the staff specifically** the floor weapon, with no high-P offset, is the unsafe execution.
- **Phase 6 (triage):** (H, H, H); severity **P2** — a build-viability + grounding finding, not an engine break (the dice engine and the handling system are both sound).

```
| Finding | Component | Stress point | Outcome@floor | Impact | Exposure | Irrev. | Intent | Phase | Severity |
| F-W1 staff=Forgiving | handling curve (param→pool) | P=6–7 (high skill) | −2D vs blade master, permanent | H | H | H | deliberate, no safeguard | 1,2,5 | P2 |
```

### Stage 2 — lesson mapping
Maps to **no** Lesson 1–6 *defect*: the Forgiving curve is a deliberate legible absolute effect (Lesson 2 exempt), no loop (5), no cliff (6), no role conflation (1). Per the skill's mapping rule, surfaced explicitly: **this is a NERS-R (build-viability) + grounding finding, not a resolution-engine defect.** The handling *system* passes the lessons; the *assignment* fails NERS-R.

### Stage 3 — NERS verdict
```
SYSTEM: Long pole (staff) handling assignment   COMPONENT: param→pool conversion (Phase 0)
VERDICT: non-compliant on R — the handling SYSTEM is sound; the STAFF's Forgiving assignment fails R.

N: pass — the handling axis is necessary; cross-cultural evidence supports ease-of-use as a real dimension.
R: FAIL — high-Proficiency staff builds are dominated on handling (−2D permanent); the weapon does not
   "hold at its extremes" for a specialist, and the dominance contradicts the staff's historical robustness.
S: conditional — the handling system is internally consistent; the staff's placement within it is the divergence.
E: pass — Forgiving/Standard/Demanding is legible.

REMEDIATION (options for Jordan — worst-first):
  P2  Re-rate the staff off Forgiving. The handling SYSTEM is not the problem; the assignment is.
```

### Stage 4 — re-test of fix options
Running Stage-1 logic on each candidate (does the fix introduce a new defect?):
- **Option A — staff → Standard.** Re-test: at P=6–7 staff H=4 (vs rapier 5) — still 1 below the top but viable; ahead of/equal to other Standard weapons; staff master competes. **New cost:** at P=1 Standard H=1 vs Forgiving 2 → the staff *beginner* is now slightly worse (loses the accessibility identity). Trade-off: fixes high-P viability, mild low-P cost. **Cleanest minimal fix.**
- **Option B — staff → Demanding.** Re-test: staff reaches H=5 at high P (matches the rapier ceiling — fits Silver's "master's weapon" exactly). **New cost:** at P=1 Demanding H=0 (punishing) → breaks the staff's real-world *accessibility* (it was also an everyman weapon). Fits the master-weapon standing, breaks the floor.
- **Option C — split the class** (simple stave = Forgiving; staff method = Demanding), mirroring the manual's two-tier reading. Re-test: resolves both ends, but **adds a weapon class → NERS-N cost** (and stacks with the short-blunt-gap F-W2 wish for more classes). Over-engineering risk.
- **Option D — keep Forgiving + a staff-specific high-P offset** (e.g., a scaling reach/control bonus). Re-test: **adds apparatus** (A5 over-reduction inverse) and reintroduces complexity the handling system was meant to avoid.

```
RE-TEST: [OPEN TRADE-OFF] — every fix trades something. Option A (Standard) is the minimal, lowest-risk fix
(restores high-skill viability at a small low-skill cost). Options B/C fit the historical standing better but
cost accessibility (B) or a class (C). This is a Jordan design decision, not closeable by analysis.
```

---

## DIAGNOSTIC 2 — ESCALATING COMMITMENT (F-A2)

**Target:** `§6.8` Commitment spec **Escalating** — "depth raises by 1 per round (forced); cannot lower depth back." Mechanic category: a **discrete-accumulator-like forced parameter ramp** feeding dice-resolved commits and the §7.2 reaction interaction.

### Stage 1 — diagnostic (Phase 0–6)
- **Phase 0 (decompose):** a forced monotonic increment on commit depth, resolved through dice commits; its danger and its value both live in the **reaction interaction** (§7.2).
- **Phase 1 (stress point):** the **late-fight high-depth state** (forced depth 5), reached by any Escalating fighter in a bout of 2+ rounds (3→4→5 over ~2 rounds).
  - **1b exposure:** **routine** for any Escalating-spec fighter in a multi-round bout (i.e., the spec's normal operation).
- **Phase 2 (what it decides):** at forced depth 5 the commit is maximally exploitable. Computed defender best-reaction advantage as forced depth climbs (§7.2 formula, verified):

  | forced depth | best defender reaction | defender δσ |
  |---|---|---|
  | 3 | Voiding | +0.40 |
  | 4 | Yielding | +0.45 |
  | 5 | **Yielding** | **+0.80** |

  The defender's advantage **rises monotonically**; at the forced ceiling (depth 5) a Yielding defender sits at **+0.80δσ** (strong defender advantage).
  - **2a/2b:** graded, **growing** magnitude; **irreversible by the Escalating fighter** (cannot lower depth — the spec's defining constraint); the only escape is to leave the bout (Phase 7 disengage).
  - **2c risk profile:** Impact **M–H** (growing defender advantage), Exposure **H** (the spec's normal operation), Irreversibility **H** (forced, no pull-back). **(M/H, H, H).**
- **Phase 3 (curves):** no cliff (smooth ramp); no role conflation.
- **Phase 4 (loops) — the decisive lens:** is Escalating **undamped AND unbounded**? It is **undamped** (forced; the fighter cannot lower depth) but **BOUNDED** (caps at depth 5). The Lesson-5 defect requires *both* → Escalating **does NOT meet it → PASSES Lesson 5.** **It is a bounded ramp, not a death-spiral.** (This is the useful negative result: Escalating is not the dangerous runaway it superficially resembles.) Caveat: the bound (depth 5) is not a protective *safeguard* — it is the **worst** state for the Escalating fighter.
- **Phase 5 (intent gate):** the mechanic is defined but the proposal gives **no stated design purpose** for forcing escalation, and it has **no historical anchor** (F-A2: every other Commitment spec maps to the record; Escalating is a pure game archetype). No paired safeguard against the growing exploitability. → `[INTENT UNDETERMINED]` on purpose; **true finding.**
- **Phase 6 (triage):** (M/H, H, H); severity **P2–P3** — a **trap/dead-apparatus** finding (a spec that worsens the more it operates, which rational players avoid), not an engine break.

```
| Finding | Component | Stress point | Outcome@floor | Impact | Exposure | Irrev. | Intent | Phase | Severity |
| F-A2 Escalating | forced depth ramp | forced depth 5 (late fight) | defender +0.80δσ (Yielding) | M/H | H | H | undetermined, ungrounded | 1,2,4,5 | P2–P3 |
```

### Stage 2 — lesson mapping
**Passes Lesson 5** (bounded → not undamped-and-unbounded). Maps to no other Lesson 1–6 *defect*. Per the mapping rule, surfaced explicitly: this is a **NERS-N (necessity / trap-option) + grounding (F-A2)** finding, not a resolution-engine defect. The diagnostic's value here is the **clearance** (it is not a death-spiral) plus the **trap** flag.

### Stage 3 — NERS verdict
```
SYSTEM: Escalating commitment spec   COMPONENT: forced depth ramp (Phase 0)
VERDICT: bounded and engine-safe (NOT a death-spiral), but likely a TRAP option — fails N.

N: FAIL — a spec that is strictly self-defeating against a Yielding-capable opponent (advantage grows to
   +0.80δσ, no pull-back) is apparatus rational players avoid; per the over-engineering guardrail, an option
   nothing uses is unnecessary.
R: conditional/weak — a strategy that is self-defeating is not a robust strategic option; it reduces, not adds,
   real build variety (the appearance of a choice that is never correct).
S: pass — integrates mechanically; no friction.
E: pass on legibility ("ramps, can't lower" is simple) — but a legible trap is still a trap.

REMEDIATION (options for Jordan — worst-first):
  P2–P3  Either cut Escalating (retirement discipline — it catches no real strategy nothing else catches),
         OR give it a balanced payoff so the forced depth buys something (turning a trap into a real trade-off).
```

### Stage 4 — re-test of fix options
- **Option A — cut Escalating** (the `<retirement>` move: does it catch a real failure nothing else catches? As a self-defeating trap, no). Re-test: removing it loses **no viable strategy**; NERS-N improves; nothing downstream depends on it. **Cleanest.** Residual: loses a *flavour* archetype (berserk/momentum) — but a flavour that is mechanically self-defeating is not serving the player.
- **Option B — add a scaling payoff** (forced-deep commits gain a damage/Pool bonus that offsets the Yielding exploitability), making Escalating a genuine **high-risk/high-reward** ramp. Re-test: this **introduces a new Lesson-5 risk** — if the payoff outpaces the +0.80δσ defender advantage, the ramp becomes a *positive* feedback the fighter wants to max → a runaway. The payoff must be tuned *against* the computed +0.80δσ ceiling. Viable but **needs sim calibration**, and adds apparatus (A5 caution).
- **Option C — make it non-forced** (allow lowering depth). Re-test: removes the spec's only distinction (the forced ramp) → collapses into Decisive/Sustained → **redundant** (fails N a different way).

```
RE-TEST: [OPEN TRADE-OFF] — Option A (cut) is the minimal, lowest-risk resolution and is favoured by the
retirement discipline. Option B (payoff) preserves the archetype but requires sim-tuning against the +0.80δσ
ceiling and risks a runaway if mis-tuned. Jordan's call: cut the trap, or invest in making it a real trade-off.
```

---

## DISPOSITION

| Finding | NERS | Lesson result | Severity | Cleanest option (Jordan decides) |
|---|---|---|---|---|
| F-W1 staff handling | fails **R** (build viability) | no Lesson 1–6 defect; handling system sound | **P2** | A: re-rate staff → Standard |
| F-A2 Escalating | fails **N** (trap option); **passes Lesson 5** | engine-safe, bounded; not a death-spiral | **P2–P3** | A: cut it |

**What this run adds over the grounding pass.** The grounding pass flagged both as historical divergences; this run gives them **resolution-fitness verdicts with numbers**: the staff is a *quantified build-viability gap* (−2D at mastery, fails R), not just a flavour mismatch; and Escalating is **cleared of the death-spiral worry** (bounded, passes Lesson 5) while being exposed as a **quantified trap** (+0.80δσ, fails N). The negative result on Escalating matters — it is *not* the dangerous thing it looks like.

**Relationship to `ners_verdict_combat_v32.md`.** Both findings are **new** — that verdict covered F1/F2/F4/F6 (σ-space, soft-cap, terminal states, in-bout E) and N1–N5; it did **not** examine the staff handling assignment or Escalating. These extend it at the sub-component level.

**Editorial-ledger disposition.** These are **proposal-review** findings on a non-ratified doc, not canon-consistency gaps — so neither *forces* a `canon/editorial_ledger.jsonl` entry. If Jordan wants them logged, both carry a concrete decision (re-rate the staff; cut/payoff Escalating). A ledger write needs a commit, and **branch protection (finding B6) blocks PAT commits to main** → would stage inline + flag `[DRIFT]`, not commit. **Not done here** (not requested + B6 + project-owner contract reserves the decisions to Jordan).

**Next, if useful:** carry either decision into the **I-17 balance sim** as a calibration input (the staff Standard-vs-Forgiving re-rate is a clean sim A/B; the Escalating payoff in Option B *requires* sim-tuning against the +0.80δσ ceiling before it could ship). Or run the same diagnostic on any other sub-component you want stress-tested.

---

`[CONFIDENCE: high — both findings computed from the verified §8.2 handling table and §7.2 reaction formula (re-derived this session); the Lesson-5 clearance of Escalating and the −2D staff gap are arithmetic, not judgment]`
`[CONFIDENCE: medium — on severity tiers (P2/P3) and the "trap" characterization of Escalating, which assume rational play and a Yielding-capable opponent; sim would confirm exploitation rates]`
`[SELF-AUTHORED — bias risk: v32 is prior-Claude work; I gave Escalating a fair hearing (the diagnostic CLEARS it of being a death-spiral rather than forcing a defect) and grounded the staff finding in arithmetic so the "fails R" verdict is not a soft call]`
`[READ: combat_v32_proposal §6.8, §8.2 (this session); §7.2 (in context, re-derived this session); canon/02_canon_constraints.md (fetched for gate; no P-constraint found directly governing handling curves or commit-depth ramps — full P-01–P-15 cross-check is part of the complete NERS pass, not this focused run); valoria-resolution-diagnostic-SKILL.md (Stages 1–4, six lessons, NERS) + PI <definitions>]`

*Method: `valoria-resolution-diagnostic` Stages 1–4. v32 source: `designs/proposals/combat_v32_proposal.md` (PROPOSAL; canon baseline `designs/scene/combat_v30.md`). Historical grounding (external, heuristic): `combat-manuals-seven-axes-throughlines.md`. Remediations are options for Jordan; historical fidelity is not the design goal. Companion to the two grounding-test documents (weapons×schools; aspects).*
