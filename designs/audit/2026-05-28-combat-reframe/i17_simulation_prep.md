# I-17 Simulation Prep — v32 Balance Validation

**This is the Mode-G decomposition deliverable: the module manifest, constant inventory, harness-reuse audit, and sequencing the formal simulator pipeline requires *before any sim code is written*. It is prep, not a sim run.** Running the modules is the multi-session work this plan sequences; per Mode G's hard rule, no module is coded until its canonical sources are full-read and every constant has a verification-ledger entry.

`[READ: skills/valoria-simulator/SKILL.md — full (Modes A–G, Mode-G protocol, ledger/manifest/fabrication-check conventions); tests/sim/scripts/phase11_c4_v0.py — full (prior engine harness); tests/sim/phase11_c4_v0_2026-05-17.md — full (prior balance findings); tests/sim/v17-integration/module_manifest.md + m7_sim_verification_ledger.json — manifest+ledger format; tests/sim_framework/sim_coverage_index.md — supersession map; combat_v32_proposal.md §15.7 + 34 draft-flag scan]`

`[SELF-AUTHORED — bias risk: this plans validation of a proposal I wrote. The structural-sanity sim (9b08fdd) already green-lit the engine's *shape*; this plan is explicitly about whether the *numbers* hold, which the sanity sim could not test. An independent reviewer would insist — and I agree — that I-17 must be empowered to return "v32 build axis is NOT balanced" and that such a result is a finding, not a failure of the plan. The plan is built to make that outcome reachable, not to confirm v32.]`

---

## 1. Why the prior phase11–13 harness is superseded as code (but not as questions)

The handoff names `tests/sim/scripts/phase11_c4_v0.py` (and phase12/13) as the prior balance work. Reading it: it models the **pre-v32 engine** — a 4-stance counter-table (`pressure/patience/decisive/cautious`), a *binary* reach gate (out-of-range → pool cut to 1D), undoubled-pool + 1/End-Ob wound, heuristic stance AI. **v32 replaces that entire resolution core** (SETUP→BOUT→RESET state graph, σ-space modifiers, soft-cap, 7 weapon classes, sub-action/CLP layer, facing/FoV, dual-resource economy). So:

- **Superseded as code.** The phase11 resolution loop cannot be reused — it computes the wrong engine. Reusing it would validate a system v32 abandoned.
- **Authoritative as the balance-question list.** What the phase11 run *found* is exactly what I-17 must re-test under v32. The prior findings (`phase11_c4_v0_2026-05-17.md`):

| Prior finding (old engine) | I-17 re-test target under v32 |
|---|---|
| Fast vs Strong **94/6** (light-light) | does σ-space + weapon-class + dual-resource pull this toward 40–60%? |
| Fast vs Tough-heavy **22/78 [INVERTED]**, Titan **12/88** | does v32 avoid the *inversion* (over-correcting into heavy-dominance)? |
| F3 gap: Fast vs Mighty-light **88%** (light+STR underclosed) | does STR contribute through the damage/Ob path in v32 without a bare-pool roll? |
| Balanced build **17.8%** vs Fast [non-viable] | does v32 make a balanced build viable, or is forced specialization still the cost? |
| M3 init-preempt recovers Att8 to **26.7%** | v32 folds initiative into Weapon Speed + state — re-test the Att-build floor |

These five are the **acceptance questions** for the v32 build axis. I-17 passes the build-balance criterion when symmetric-optimization matchups across the archetype set land **40–60%** (the skill's stated balance band, §8.8) with **no inversion** and **no non-viable** baseline build.

- **Reusable scaffold.** `tests/sim_framework/engine*.py` + `state.py` + `combat.py` provide the Monte-Carlo harness, RNG seeding, and reporting shell. Reuse the *scaffold* (seeding, batch runner, report format); rebuild the *resolution core* against v32. The `sim_verification_ledger.json` + `module_manifest.md` formats (from v17-integration) are the templates to copy.

---

## 2. Module manifest (Mode-G — build order, one module per session)

Sim name: **`v32-combat-balance`** → commits to `tests/sim/v32-combat-balance/` as a directory (Mode-G rule: manifest, modules, ledger snapshot, batch outputs all live there). *(This prep doc lives in the combat-reframe audit dir with its sibling analyses; the `tests/sim/v32-combat-balance/` directory is created by Module 1 when the first ledgered sim code lands, with its `tests/coverage_matrix.md` entry at that point.)*

| # | Module | Depends on | Canonical sources (full-read before coding) | What it builds | Budget |
|---|---|---|---|---|---|
| **1** | **Dice + σ-space core** | — | `params/core.md`; combat_v32 §12.3 | Canonical d10 net engine; σ-space modifier (`δσ·σ_N`), soft-cap `M·tanh(net/M)`; level→δσ map. The verified primitive from the sanity sim, promoted to a ledgered module. | 1 |
| **2** | **Attribute → pool builder** | 1 | `params/core.md §Attributes`; `designs/scene/derived_stats_v30.md`; combat_v32 §2.1, §11 | Build Combat Pool `(Agi×2)+History+3`, derived Stamina/Composure/Concentration, MaxWounds/Health. Archetype stat blocks (Fast/Strong/Tough/Balanced/Mighty) defined here as ledgered inputs. | 1 |
| **3** | **Weapon-class layer** | 1,2 | combat_v32 §8 (all); `combat_v30 §5` (canonical TN/STR/armor) | 7 classes: base TN, STR mult, armor-modifier table, handling H(P), phase-keyed Pool/TN, Weapon Speed, sub-action availability. | 1 |
| **4** | **Bout state graph + sub-actions** | 1,3 | combat_v32 §4.7, §12.1–12.4 | SETUP→BOUT→RESET transitions; per-state sub-action option set; degree-of-success effects; termination (wounds≥MW+1 / disengage / cap). Extends the sanity-sim bout with the real sub-action policy. | 2 |
| **5** | **Stance + Reaction + coherence** | 4 | combat_v32 §7.1–7.3 | Authored Stance Counter (state-gated, Closing); Reaction 2-param formula; named-set bonuses (§6.11) + 2 antagonism exceptions. | 1 |
| **6** | **Dual-resource economy** | 4 | combat_v32 §11.5–11.6, §4.9 | Stamina depletion/threshold + Concentration; recovery; the physical/mental two-economy build differentiation. | 1 |
| **7** | **Facing / FoV** *(optional for build-balance; required for full fidelity)* | 4 | combat_v32 §11.2 | Field-of-view zones; emergent flank/rear Ob; reaction-gating by facing. Can be stubbed (frontal-only) for the first balance sweep, then added. | 1 |
| **8** | **Integration + archetype sweep** | all | — (wires modules; no new mechanics) | Symmetric-optimization batch over the archetype set; the §1 acceptance-question matrix; N≥1000 Wilson 95% CI per the v17 precedent. | 1 |

**Decision-gated modules (do not block the manifest, but flag for Jordan):**
- **Module 5 magnitudes** (named-set bonuses, Reaction coefficients, Stance Counter Ob values) are I-11/I-13/I-14 *draft* values — the sweep will tune them, but their *starting* values need either a Jordan call or an explicit "sim-seed, will tune" ledger note.
- **Module 7** is optional for the *build-balance* question (frontal symmetric duels don't exercise facing); it is required before any positional-balance claim. Recommend stub-first, add in a later pass.
- **Cross-system** (Concentration↔social shared pool, F3 / I-15) is **out of I-17's scope** — it's a cross-system sim, and the standing scope is combat-only this conversation. Module 6 builds Concentration *within combat*; the shared-pool interaction is deferred.

---

## 3. Constant inventory (Mode-G — every value needs a ledger entry before its module is coded)

The proposal carries **34 draft/sim-tunable flags across 25 sections**. Mode-G's `sim_fabrication_check()` blocks any constant lacking a ledger entry or inline `# [canonical: …]`. Two classes:

**Class A — canonical (cite the canon path).** Sourced, not tunable; ledger entry cites the real path:
- d10 face values, TN 6/7/8, per-die σ=0.80 → `params/core.md`
- Combat Pool `(Agi×2)+History+3`, MaxWounds `min(floor(End/2)+1,3)`, Health `(End+6)×(MW+1)`, Stamina `End×5`, Composure `Cha×3`, Concentration `Focus×3` → `designs/scene/derived_stats_v30.md` / `params/core.md`
- Weapon TN matrix, STR mult (Light×1/Heavy×2/Blade×1/Blunt×1.5), armor-modifier table, Long Heavy Blunt +5/all & TN 8 → `combat_v30 §5`

**Class B — draft (cite the proposal as the draft source + flag `tune`).** These are v32's *own* new numbers; the honest ledger entry cites `combat_v32_proposal.md §X` with `assumption: "draft sim-seed, tuned in I-17 module N"` — they are NOT canonical and the ledger must say so:
- **σ-space:** M_max=1.5; level→δσ (Minor 0.25 / Moderate 0.5 / Strong 0.75 / Major 1.0); base-Ob values (§12.3) — *the most load-bearing draft set; the whole impact-uniformity result rides on these*
- **Weapon Speed** values per class (§3.2); **handling** profile→class assignments (§8.2)
- **Phase-keyed** ±0.5 Pool/TN modifiers (§8.4); fractional Commit-Pool TN per signal tier (§4.3)
- **Named-set bonus** magnitudes + 2-step graded steps (§6.11); **Reaction** 2-param coefficients (§7.2); **Stance Counter** legacy-Ob→σ map (§7.1)
- **Sub-action** Pool compositions (Displace = Str+Agi composite, etc., §12.2); degree-of-success magnitudes (§12.4)
- **CLP** max 32 rules (§6.10.7); **Stamina/Concentration** thresholds + recovery (§11.5, §4.9); **Intent** Tier-4 pre-empt 0.2–0.4× (§13)

**The Class-B/Class-A split is itself a prep finding:** ~20 of the 34 flags are Class B (v32's own draft numbers). That means I-17 is genuinely a *tuning* exercise on a large draft surface, not a confirmation — and the verification ledger will be honest that these entries cite the proposal, not canon. A reviewer who saw all 34 cite canon paths should distrust the sim; the correct ledger has ~20 entries saying "draft, tuned here."

---

## 4. Per-module session protocol (the Mode-G loop, applied)

Each module session: (1) bootstrap; (2) `h.task_gate('simulation')`; (3) read manifest from GitHub; (4) pick next `pending` module; (5) **full-read** its canonical sources, verify each reads `full` via `g.read_depth_report`; (6) build/extend `sim_verification_ledger.json` — every constant gets an entry, `quoted_text` verified to appear in fetched content (Class A) or marked `draft sim-seed` citing the proposal (Class B); (7) `h.sim_gate('custom', systems=[…])`; (8) write module code with inline `# [canonical: …]` per constant; (9) run in isolation vs known inputs; (10) `h.safe_commit()` + mark module `status: verified`; (11) update session log. Checkpoint via `h.write_checkpoint()` if a module can't finish in one session — **never compress reads to finish**.

**Hard rules carried from Mode G:** no multi-module code in one session; no constant without a ledger entry; no assuming a prior module is correct (re-verify the values you import); no cross-module patching in integration (flag for rebuild); **no batch run until every module is `status: verified`** (the sim_v2 failure: 50-seed batches on an unvalidated sim made fabrication look rigorous).

---

## 5. What I-17 will and won't answer

**Will:** whether the v32 build axis is balanced (archetype matchups 40–60%, no inversion, no non-viable baseline) under tuned constants; whether dual-resource economy differentiates builds; whether the §1 prior-finding regressions are closed. This is the real balance validation the structural-sanity sim explicitly could not provide.

**Won't (deferred):** N1 transition *feel* (needs playtest, not Monte Carlo); cross-system Concentration shared-pool (F3 / I-15, cross-system); positional/facing balance unless Module 7 is built; anything requiring human judgment of "fun." These stay flagged, not silently folded in.

**First session to run:** Module 1 (dice + σ-space core) — smallest, all-canonical-or-verified-draft, and everything depends on it. The sanity-sim code (committed in `9b08fdd`) is the starting point; promoting it to a ledgered module is the lift.

---

`[CONFIDENCE: high on the plan structure — it's the Mode-G protocol applied to v32's actual section map and the real prior harness; MEDIUM on session budgets — estimates, the bout/sub-action module (4) is the risk and may split. The Class-B constant count (~20) is the honest signal that I-17 is a large tuning effort, not a quick confirmation.]`
