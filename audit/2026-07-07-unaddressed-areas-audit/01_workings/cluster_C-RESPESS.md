# cluster_C-RESPESS

_Evidence cluster dossier, read-only; archived verbatim from the agent's final message by the Fable orchestrator (2026-07-07). Verdicts pending refuter pass + Fable adjudication - see `unaddressed_areas_audit_v1.md`._

# Cluster C-RESPESS dossier

Pessimist diagnostic-resolver review. Every numeric claim below was reproduced by direct computation against the actual code (probes archived in scratchpad). Baselines: `params/core.md`, `skills/valoria-resolution-diagnostic/SKILL.md`, the 2026-05-28 resolver spec. Read-only; no repo file touched.

---

## Engine 1 (combat d_σ) — phase findings + pessimist verdict

**Target:** `designs/scene/combat_engine_v1/core.py` (`resolve`/`degree`), `systems.py` (net-σ assembly), `config.py`, resolving through `sim/autoload/sigma_leverage.py`.

**Phase 0 (scope/engine).** Rolling engine present: `core.resolve(pool, net_sigma, rng)` — Instance A (σ-leverage continuous). Pool = `resolution_pool(history) = max(5, History+6)` (core.py:30-32). Base Ob **FIXED at `DECISIVE_OB=3`** for every sub-action (core.py:25,47-53). Advantage enters as a **μ-shift** (`net = roll + soft_cap(net_sigma)·σ_n(pool)`), never an Ob-shift. Recognize-and-exclude: damage (`core.damage`, deterministic given degree), tempo/stamina/poise clocks (roll-inputs).

**Phase 1 (stress point, pessimist).** Two extremes attacked: (a) the **low-pool floor** (History 0 → pool 6) and (b) the **high-pool head** (History 13 → pool 19), because base Ob is fixed at 3 while the pool mean `0.4·pool` sweeps 2.4→7.6 — i.e. the operating point drifts across the whole progression. Exposure: **routine and by-design** — pool tracks History, the core progression axis.

**Phase 2 (what it decides).** Graded 4-degree ladder → damage **Quality** (0.25/0.5/1.0/1.5–2.5× — core.py:72-73, `strike`). The degree, not just win/loss, is load-bearing (lethality). Reversibility: wounds are non-resetting (irreversible-load-bearing).

**Phase 3 (curves).**
- *3a leverage (z-space):* uniform **by construction** — `net_boost = soft_cap(net_σ)·σ·√N`, and `Δz = net_boost/(σ·√N) = soft_cap(net_σ)`, pool-independent (sigma_leverage.py:178-191). Confirmed. **No 1/√N re-import** — net_σ is σ-scaled, not a flat "+X to net."
- *3b/3c cliffs / continuity:* the **Ob-floor cliff (ED-884) is NOT re-introduced** — `eff_ob` is display-only, resolution is pure μ-shift (core.py:33 defined-but-unused; core.py:47-53; the P-232 Ob≥1 floor cannot be breached because base Ob is a fixed 3). Continuity correction **present** — `degree` reads each integer band at the `k−0.5` boundary (core.py:35-45), single-applied (the sample `continuous_engine_sample` is raw Normal, dice_engine.py:77-91 — no double-count).
- **THE PESSIMIST BREACH — degree-ladder saturation (Probe 1a).** The Overwhelming bar is a **fixed `2·Ob=6`** (core.py:43), NOT the pool-aware de-saturated bar the *sibling contest engine deliberately uses* (`sigma_leverage.degree`, MU·pool+OVERWHELM_SIGMA·σ·√N, lines 284-311). With base Ob pinned at 3 and pool sweeping 6→19, the Overwhelming **rate at parity (net_σ=0, mirror match)** runs:

  | History | pool | P(Overwhelming) | P(Success) | P(Partial) | P(Fail) |
  |--:|--:|--:|--:|--:|--:|
  | 0 | 6 | **0.057** | 0.425 | 0.351 | 0.167 |
  | 3 | 9 | 0.214 | 0.462 | 0.226 | 0.098 |
  | 7 | 13 | 0.464 | 0.361 | 0.123 | 0.052 |
  | 13 | 19 | **0.727** | 0.200 | 0.052 | 0.021 |

  A high-History mirror match resolves ~73% of landed blows as Overwhelming vs ~6% at low History — the graded output collapses toward a **near-binary (all-Overwhelming)** at the top of the progression, and the Overwhelming *rate* is pool-dependent. This is exactly the Lesson-2 de-saturation the contest engine applied and combat did **not**.

**Phase 4 (loops).** Initiative substrate is a positive-feedback state but is explicitly damped (per-beat DECAY, config INIT_DECAY=0.75) and capped (INIT_CAP=1.5, `clamp_initiative`) — Lesson-5 satisfied. Not a finding.

**Phase 5 (intent).** Fixed Ob-3 preserves the mirror **win-rate** (50/50 at any pool) — deliberate. But the **degree-distribution** side effect is un-audited; no design doc addresses the pool-dependent Overwhelming rate. `[INTENT UNDETERMINED]` on the degree ladder specifically.

**Pessimist NERS verdict (Engine 1):** **PARTIAL — compliant on P(success), non-compliant on the degree ladder.**
- N: pass. R: **fail (P2)** — the graded output is not robust across the input range; Overwhelming rate 0.06→0.73 across History (Probe 1a). S: **fail (P2)** — resolves the Overwhelming bar *inconsistently with its sibling* (fixed 2·Ob vs the contest kernel's pool-aware bar in the same `sigma_leverage.py`). E: pass. This is harsher than N-10's "combat likely compliant" optimist read, and the reason is exact: the optimist checks P(success) leverage (which is uniform in z) and stops; the pessimist checks the *degree distribution*, which the fixed 2·Ob bar de-stabilizes — a defect the corpus already recognizes (it fixed it in contest) but left live in combat. → Lesson 6 (bounded/de-saturated response): port the contest engine's pool-aware Overwhelming bar into `core.degree`.

---

## Engine 2 (contest, both formulas) — phase findings + divergence map + pessimist verdict

**Target:** `sim/personal/contest/resolver.py`+`primitives.py` (σ-kernel Bout) and `sim/personal/contest_legacy_stub.py` (the raw-dice stub), per N-2.

**Phase 0 (scope/engine) — the decisive pessimist finding.** Two contest resolvers coexist, and **the one the live campaign dispatches is the deprecated raw-dice stub, not the σ-kernel.** Traced: `sim/mc_v18.py` → `sim/cross_scale/scene_dispatch.py:106` → `contest.run_contest(...)` which re-exports `contest_legacy_stub.run_contest` (contest/__init__.py:35-50). That resolver is a **bare opposed d10 pool** — `build_argue_pool = max(1, (Primary×2)+History−Wounds)` (stub:111-127), roll A-net vs B-net, `margin−resistance` drives a 3-exchange track banded at 7/3. **No σ-leverage, no deterministic odds, no reception/degree structure**, floor 1D. `module_contracts.yaml:429` confirms `resolver: dice_pool`. The σ-leverage kernel (Bout / `build_contest`/`resolve_contest`) that satisfies P-i…P-v has **no live caller** — grep finds it only in `sim/tests/test_contest_kernel.py`. **The engine built to make contest NERS-compliant is dark; the engine actually resolving campaigns is the raw-pool-vs-pool pattern the diagnostic skill exists to flag as a wrong-engine defect (Lesson 3 / P-v).**

**Phase 1–3 divergence map (Probes 2a/2b/2c).** Where the same fiction resolves differently between the two formulas:

| Char (P,H,W) | Legacy pool `max(1,2P+H−W)` | Kernel pool `max(5,2P+3)` | P(succ Ob3) legacy | P(succ Ob3) kernel | Δ |
|---|--:|--:|--:|--:|--:|
| P2 H0 (novice) | 4 | 7 | 0.278 | 0.547 | **−0.269** |
| P2 H3 | 7 | 7 | 0.547 | 0.547 | 0.000 |
| P2 H6 (veteran) | 10 | 7 | 0.721 | 0.547 | **+0.173** |
| P4 H0 | 8 | 11 | 0.613 | 0.762 | −0.149 |
| P4 H6 | 14 | 11 | 0.849 | 0.762 | +0.087 |
| P1 H0 W4 (wounded) | 1 | 5 | — | — | floor gap 4D |

Three structural divergences, all reproduced:
1. **History-axis erasure.** `Pool.size` (primitives.py:211) has **no History term** — a flat `+3` base. The kernel is History-invariant: it collapses *every* orator to legacy-at-History-3. A veteran and a novice of equal Charisma resolve identically in the kernel; they diverge 15–27pp in the live legacy engine. The two engines agree *only* at H=3.
2. **Wound-blindness + floor-5 erasure of the low-pool regime.** The kernel has no wound term and floors at 5, so the sub-5D regime the 05-28 diagnostic measured (the floor-degeneracy regime) is **unreachable** in the kernel — a 4-wound P1 orator is pool 1 live but pool 5 in the kernel (Probe 2c). The kernel cannot represent a degraded contestant at all.
3. **Face monotonicity ratchet (KU-3 at resolver level, Probes 2d/4).** In the default (no-armature) venue, `Standing.strip()` is **never called** (confirmed by grep — the only strip site is the opt-in CR5 backfire, resolver.py:418). Face only *builds* (build_ethos, resolver.py:317-320), feeding a one-way readiness multiplier (0.40→0.64, saturating). The trailing contestant has **no Face-attrition / comeback channel** in default play; the two attrition channels (`rebut`, `allow_rebuttal=False` by default; CR5, armature-gated) are both opt-in.

**Phase 4/5.** Legacy stub at pool 1: opposed 1D-vs-1D produces frequent ties, and a tie moves the track `+1 toward the first speaker` (stub:172-177) — at the low-pool floor the outcome is decided by **turn order, not skill**, the degeneracy the diagnostic named. Intent: the σ-kernel is *documented* as the promotion (Stage 1b), so the legacy stub still being the live dispatch is a **wiring gap, not a design intent** — `[INTENT: NOT-INTENDED]`.

**Pessimist NERS verdict (Engine 2):** **NON-COMPLIANT as live-dispatched.**
- N: fail — a redundant second engine exists; the wrong one is live. R: fail — the live engine is the fragile bare-pool binary (floor 1, turn-order tie-break). S: **fail (P2)** — two resolvers give the same fiction 15-27pp apart, and the live resolver ≠ the "promoted" one ≠ the contract's declared engine three-ways. E: fail — the raw opposed-pool gives no legible odds. This is legitimately harsher than any optimist "social contest likely compliant" (Worked Example 2): the optimist audits the σ-kernel and pronounces it clean; the pessimist checks *which engine actually runs* and finds the deprecated raw-dice stub, i.e. the exact P-v defect. → Lesson 3: wire live dispatch to the σ-kernel (or, if the legacy stub is deliberately live, that is a wrong-engine ruling that needs Jordan). Then reconcile the pool formula (History erasure / wound-blindness / floor).

---

## Engine 3 (deterministic + stochastic) — phase findings + pessimist verdict

**Target:** `designs/audit/2026-05-28-resolution-diagnostic/sim_domain_resolver.py` + `domain_action_resolver_spec.md` (ED-874), vs `module_contracts.yaml` (`domain_actions`, `resolver: d_sigma` [ASSUMPTION], `doc: null`).

**Phase 0–2.** Instance B — `P_success=clamp(BASE+SLOPE·M, FLOOR, CAP)`, draw `r~U[0,1)`, 4-degree ladder feeding Domain Echo. Pivotal, load-bearing (Suppress→Stab−1). **No live implementation** — the only code is the audit-dir sim; the contract module is `doc:null`, resolver `[ASSUMPTION]`, params `PROPOSED`.

**Phase 3 (curves, pessimist).**
- *Monotonicity/cliffs:* `P_success` and `P_overwhelming` both **strictly monotonic** across M∈[−8,+8] (Probe 3a); the Partial band smoothly shrinks 0.20→0.07 as `ps` saturates at CAP=0.90 and `pap` at FAIL_FLOOR=0.97 — a clamp consequence, **not a cliff**. The resolver form passes its own Stage-4 (matches spec §6). Optimist verdict holds *inside the tested zone*.
- **PESSIMIST BREACH 1 — Ob round-trip divergence (Probe 3b).** The spec offers *two* difficulty derivations: direct stat contest `M=acting−target`, and fixed-Ob `D=max(1,(Ob−1)·2)` where `Ob=floor(stat/2)+1` (sim:82-83, spec §4). For every **odd** target stat (T=3,5,7 — 4 of the 7 legal values) the round-trip `stat→Ob→D` undershoots by 1, so the two legal resolutions of the *same matchup* diverge by exactly `SLOPE=0.10` (10pp):

  | target T | Ob | D | actor-4 direct P | actor-4 Ob-mapped P | gap |
  |--:|--:|--:|--:|--:|--:|
  | 3 | 2 | 2 | 0.600 | 0.700 | **+0.100** |
  | 5 | 3 | 4 | 0.400 | 0.500 | **+0.100** |
  | 7 | 4 | 6 | 0.200 | 0.300 | **+0.100** |

- **PESSIMIST BREACH 2 — high-Ob leverage death (Probe 3c).** The resolver's whole selling point (uniform legible SLOPE) **dies in the FLOOR clamp** at the difficulty extreme. At Ob≥8 (Structural; D≥14) *every* bare stat 1-7 clamps at FLOOR=0.05 — a flat 5% for everyone, stat-inert:

  | | stat1 | stat2 | stat3 | stat4 | stat5 | stat6 | stat7 |
  |---|--:|--:|--:|--:|--:|--:|--:|
  | Ob5 (D8) | 0.05 | 0.05 | 0.05 | 0.10 | 0.20 | 0.30 | 0.40 |
  | Ob8 (D14) | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 |

  The spec proved it *fixes* stat2-vs-Ob3 floor degeneracy but never tested stat-vs-Ob8. Because bare stats max at 7 < D=14, the flat-for-everyone degeneracy it was built to remove **reappears** at high Ob (Structural/Foundational exist on the canonical Ob scale, core.md:32-40).

**Phase 5 (intent).** Form ratified (ED-874); params PROPOSED. Neither divergence is addressed in the spec — both are at input extremes the Stage-4 self-test skipped (it swept M∈[−6,+6] at moderate difficulty only).

**Pessimist NERS verdict (Engine 3):** **PARTIAL — compliant in the live zone, non-compliant at the extremes, and unimplemented.**
- N: pass. R: **fail (P2)** — leverage collapses to a flat 5% at Ob≥8 (untested by the optimist Stage-4). S: **fail (P2)** — two legal difficulty derivations disagree 10pp for the majority (odd-stat) of matchups; a Godot importer must pick one, un-specified. E: pass in-zone. Plus: `doc:null`, `[ASSUMPTION]` resolver, PROPOSED params — no ratified implementation to audit against. Harsher than the optimist "compliant post-ED-874" because the optimist stopped at the moderate-Ob live zone; the pessimist swept to Ob≥8 and to the odd-stat round-trip, where the resolver's guarantees break.

---

## [ASSUMPTION] resolver census + worst-case table

Eleven `[ASSUMPTION]`-grade **resolvers** in `references/module_contracts.yaml` (matches CLAUDE.md §6's "11/27"). Each: the assumption, and the worst plausible M1 (first-milestone / first-live-turn) consequence if wrong.

| # | Module (line) | doc | Resolver [ASSUMPTION] | The assumption | Worst-case at M1 (named juncture) |
|---|---|---|---|---|---|
| 1 | `domain_actions` (474) | **null** | `d_sigma` (ED-874) | Faction Domain Actions resolve via the Engine-3 det+stoch resolver | **First faction turn.** The resolver is doc:null + PROPOSED params + the Ob-round-trip (C-RESPESS-6) and high-Ob-death (C-RESPESS-7) divergences. Pick the wrong difficulty map → every odd-stat matchup off 10pp; every Ob≥8 action a flat 5% coin-flip. The single most load-bearing unbacked resolver. |
| 2 | `faction_state` (57) | faction_behavior_v30 | `deterministic_accounting` (+ d_σ contested) | Accounting-cadence procedures are deterministic; only contested resolution draws | **First cascade Accounting.** If a contested/pivotal faction resolution is coded deterministic, its outcome is exploitable (the NERS-S "dice-on-a-ledger" inverse — a *deterministic* result where a draw was needed). |
| 3 | `npc_behavior` (109) | npc_behavior_v30 | `deterministic_accounting` | NPC decision derivation is a deterministic sequence (doc-12 §8/§9) | **First NPC action tick.** If any NPC choice actually needs a draw, NPCs are fully predictable/exploitable; conviction-armature reads (§8.2) feeding a deterministic path lock behavior. |
| 4 | `npc_memory` (181) | **null** | `state_reader` | Memory is written from Keys, queried by Procedures (doc-12 §2.3 bridge) | **First NPC that must recall an event.** Bridge unauthored → memory reads stale/absent → NPCs act on wrong world-state; silent, hard to detect. |
| 5 | `piety_track` (202) | conviction_track_v1 | `deterministic_accounting` | Scar-accumulation thresholds are deterministic (§2) | **First Conviction Scar.** Wrong threshold semantics → scars fire early/late; feeds faction `state.scar_acquired` (crisis-bypass un-damping at scars≥3). |
| 6 | `territorial_piety` (241) | conviction_track_v30 | `deterministic_accounting` | CV movement + seasonal TC are deterministic (§1.2/§3) | **First Year-End TC.** Mis-modeled CV movement mis-scores territorial piety at the seasonal accounting. |
| 7 | `peninsular_strain` (498) | peninsular_strain_v30 | `deterministic_accounting` | Strain accounting has no draw | **First disaster/strain-shock emit.** If strain shocks should be stochastic, a deterministic ledger makes catastrophe timing predictable/gameable. |
| 8 | `settlement_economy` (613) | **null** | `deterministic_accounting` | Economic intervention resolves as a pure ledger | **First economic-intervention Domain Action.** doc:null — no design backs the assumption; consumes `da.economic_intervention` but its resolution is unspecified. |
| 9 | `faction_politics` (711) | **null** | `deterministic_accounting` | Rank-ladder/coup/succession are deterministic accounting | **First succession/coup.** doc:null; emits `state.coup_attempted`/`succession`/`standing_change` into faction_state — if a coup needs a draw, a deterministic result is either always-on or never, both degenerate. |
| 10 | `miraculous_event` (731) | miraculous_event_v30 | `state_reader` | Gated emitter: "fires on high-Ob Mending near T15" | **First high-Ob Mending near the era-15 window.** The gate condition is a guess — miraculous events fire at the wrong time or never; a state_reader that should be a gated *emitter* emits nothing. |
| 11 | `scenario_authoring` (748) | **null** | `manifest` | Authoring-time event injection, no runtime resolution | Lowest risk (authoring, not a runtime draw), but doc:null — the injection contract is unspecified, so injected events may carry ill-formed Keys. |

Plus two `[ASSUMPTION bucket]` **state** annotations (not resolvers, noted for completeness): `threadwork` Coherence bucket (279) and `engine_clock` season-counter bucket (696) — `engine_clock` is also doc:null, the temporal spine with no home doc.

---

## Findings (reproduced breaches/divergences only)

| ID | Sev | Engine | Finding | Property | Evidence (file:line + probe) |
|---|---|---|---|---|---|
| **C-RESPESS-1** | P2 | 1 combat | Degree ladder not de-saturated: fixed `2·Ob=6` bar + fixed base Ob 3 vs History-scaled pool 6-19 → Overwhelming rate at parity 0.057→0.727; graded output collapses to near-all-Overwhelming at high History. Sibling contest engine de-saturates this; combat doesn't. | P-ii/P-iii/P-iv, NERS-S | core.py:35-53 (fixed `2*ob−0.5`, base=DECISIVE_OB=3); sigma_leverage.py:284-311 (contest's pool-aware bar combat lacks); **Probe 1a** |
| **C-RESPESS-2** | P2 | 2 contest | Live dispatch (`mc_v18`→`scene_dispatch.py:106`→`run_contest`) resolves via the **deprecated raw-dice opposed-pool stub** — the wrong-engine defect; the σ-kernel (Bout) has no live caller (test-only). | P-v, Lesson 3 | scene_dispatch.py:106; contest_legacy_stub.py:111-127; contest/__init__.py:35-50; module_contracts.yaml:429 (`dice_pool`); grep (no live `Bout(`) |
| **C-RESPESS-3** | P2 | 2 contest | Dual pool formula divergence: legacy `max(1,2P+H−W)` vs kernel `max(5,2P+3)`. Kernel is **History-invariant** (collapses all to H=3-equiv) + wound-blind → same fiction resolves 15-27pp apart. | NERS-S | primitives.py:211; contest_legacy_stub.py:126; **Probe 2a/2b** |
| **C-RESPESS-4** | P3 | 2 contest | Kernel floor 5 + no wound term makes the sub-5D regime (05-28 diagnostic's floor-degeneracy regime) unreachable; a 4-wound P1 orator = pool 1 legacy / pool 5 kernel. Kernel can't represent a degraded contestant. | P-iv, S | primitives.py:211; contest_legacy_stub.py:126; **Probe 2c** |
| **C-RESPESS-5** | P3 | 2 contest | Face is a monotonic ratchet in default play: `Standing.strip()` never called (only opt-in CR5); Face builds only → one-way readiness multiplier; no comeback/attrition channel for the trailing side. | P-iv | primitives.py:83,288; resolver.py:317-320,418; grep; **Probe 2d/4** |
| **C-RESPESS-6** | P2 | 3 domain | Ob round-trip loses odd-stat info: `stat→Ob=floor/2+1→D=(Ob−1)·2`. Direct contest vs Ob-mapped resolution of the *same* matchup diverge 10pp for every odd target stat (T=3,5,7). | NERS-S | sim_domain_resolver.py:82-83; spec §4; **Probe 3b** |
| **C-RESPESS-7** | P2 | 3 domain | High-Ob leverage death: at Ob≥8 (D≥14) every bare stat 1-7 clamps at FLOOR=0.05 — flat 5% for everyone, stat-inert. The floor-degeneracy the resolver removes at moderate Ob reappears at the difficulty extreme (untested by Stage-4). | P-ii/R | sim_domain_resolver.py:68-72; core.md:32-40 (Ob 8/20); **Probe 3c** |

---

## Honest gaps (UNSUBSTANTIATED pessimist cases — listed, not carried)

- **Combat Ob-floor cliff (ED-884) re-introduction — UNSUBSTANTIATED.** Resolution is pure μ-shift; `eff_ob`/`effective_ob` is display-only and *not called* in `core.resolve`/`resolver._reception` (core.py:33,47-53; resolver.py:24 imports but the μ-shift path is used). The P-232 floor cannot be breached because base Ob is a fixed 3. The fix holds in the live paths.
- **Combat leverage non-uniformity / flat-shift 1/√N — UNSUBSTANTIATED as a leverage defect.** `net_boost` is σ-scaled, so `Δz=soft_cap(net_σ)` is pool-independent by construction. The P-space `dP` drift in Probe 1b is an artifact of the fixed-Ob operating-point drift (already carried as C-RESPESS-1), not a flat-bonus defect.
- **Combat stacked-modifier saturation cliff — UNSUBSTANTIATED.** `soft_cap`(tanh, M_MAX=1.5) is smooth and bounded (P ceiling 0.984 at pool 12, Probe 1c) — the intended bound, not a cliff.
- **Domain-resolver internal cliff / non-monotonicity — UNSUBSTANTIATED.** `P_success`, `P_overwhelming` both strictly monotonic; the Partial-band shrink is a smooth clamp consequence (Probe 3a). The resolver *form* passes; the breaches are at the difficulty/derivation extremes (C-RESPESS-6/7), not the form.
- **Face death-spiral / Lesson-5 undamped-and-unbounded loop — UNSUBSTANTIATED.** The readiness ratchet is undamped but **bounded** (Standing cap 10 → readiness saturates ~exchange 3-4, Probe 4). It fails the Lesson-5 threshold (needs *both* undamped and unbounded); carried only as the weaker P3 asymmetry (C-RESPESS-5), not a runaway.
- **Exposure frequencies not quantified:** C-RESPESS-2's live-path frequency (how often `mc_v18` dispatches a social scene) and C-RESPESS-7's frequency (how often faction actions hit Ob≥8) were not measured — the breaches are reproduced structurally, but their campaign-weighted exposure is an open probe.
