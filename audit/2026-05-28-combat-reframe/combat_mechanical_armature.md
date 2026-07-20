# Combat-Derived Mechanical Armature

**An abstract, system-agnostic design standard extracted from `combat_v32_proposal`, for adjudicating other Valoria resolution systems.** Source: the v32 state-graph reframe (designs/proposals/combat_v32_proposal.md) and its verified mechanisms (designs/audit/2026-05-28-combat-reframe/).

---

## Purpose, and what this is *not*

The `valoria-resolution-diagnostic` skill's six lessons state **what** a sound system must achieve (uniform impact, bounded loops, no accidental cliffs, …). This armature states **how** — the concrete mechanical patterns combat_v32 used to satisfy those lessons, abstracted so they are not combat-specific. Combat is the *worked reference implementation*; the armature is the reusable yardstick.

It **subsumes and references** the two cross-system standards already extracted this session: `attribute_weight_standard.md` (σ-leverage parity) and `derived_stats_audit.md` (1/k resource parity).

**Out of scope (deliberately):** this document does **not** apply the armature to social, faction, mass, threadwork, or any other system — that adjudication is deferred to per-system work, not done here. It also does **not** settle N3 (whether σ-space should propagate beyond combat); the armature is the *tool* that would adjudicate N3, applied later. Creating the yardstick is in scope; swinging it across the project is not.

---

## The armature — seven principles

Each principle: the **abstract rule** · the **combat_v32 reference** (where it is realized) · the **test** to apply to any candidate system · the **NERS lesson/criterion** it serves.

### A1 — Modifiers carry uniform *impact*, expressed in σ-space
**Rule.** A fixed advantage must shift outcome probability by the same amount regardless of pool size. Express modifiers in standard-deviation units (δσ), convert to an Ob shift scaled to the pool (`δσ · σ_N`, σ_N = per-die SD · √pool).
**Combat ref.** §12.3 — Minor/Moderate/Strong/Major levels → δσ; uniform ~25.8pp impact across 5–18D.
**Test.** Does a fixed modifier in this system swing a small pool far more than a large one? If yes, it fails A1 (the v31 F1 defect).
**Serves.** Lesson 2 (uniform impact), NERS-R/S.

### A2 — Modifier stacks saturate; they never foreclose, and never cliff
**Rule.** Pass the net modifier sum through a smooth saturating cap before applying it, so no stack drives an outcome to ~0% (or 100%), and the cap introduces no discontinuity.
**Combat ref.** §12.3 — `eff = M·tanh(net/M)`, M = 1.5σ; worst adverse stack lands ~9%, not 0%; `tanh` is smooth (a hard clamp would be a Lesson-6 cliff).
**Test.** Can stacked modifiers in this system foreclose a result before the roll? Is the bound a hard clamp (cliff) rather than a saturation? Either fails A2.
**Serves.** Lessons 5/6 + NERS-R (the v31 F2 defect).

### A3 — Only state-relevant modifiers are live (state-gating)
**Rule.** Partition modifiers by the system state they physically apply to; only the relevant subset is active at any moment. This bounds the raw stack feeding A2 and shrinks the per-state decision.
**Combat ref.** §4.7/§12.3 — Stance Counter lives only at Closing; Tactile/Grip only In-bind; etc.
**Test.** Does this system apply its whole modifier set at every step, or gate by state? Ungated everything-at-once is the smell.
**Serves.** Lesson 5 (bounding) + NERS-E (per-state simplicity).

### A4 — Two-tier structure: deterministic choice weights a probabilistic resolution
**Rule.** Separate a **setup tier** (deterministic player choice under uncertainty — build, loadout, stance, approach) from a **resolution tier** (the probabilistic subgraph the setup *weights*). Front-load strategic depth into setup; keep per-moment resolution load low.
**Combat ref.** §1 P2, §4 — SETUP (1–5) weights the BOUT (6) probabilistic subgraph; CLP auto-resolves with intervention at decision nodes.
**Test.** Where does this system put its decisions — distributed as high-frequency micro-choices inside the random resolution (heavy, fatiguing, low-leverage), or front-loaded into deterministic setup (legible, high-leverage)? The former stresses NERS-E.
**Serves.** NERS-E (front-loaded complexity) + NERS-R (meaningful choice).

### A5 — Minimize authored apparatus: derive what reduces, let effects emerge
**Rule.** Two facets. (a) Before hand-authoring a matchup table, test whether it reduces to a low-dimensional model; if it does, replace the table with the formula and keep only the residual as authored. (b) Before adding a new modifier for a desired effect, check whether the effect can *emerge* from existing primitives; prefer emergence.
**Combat ref.** (a) §7.2 Reaction → 2-param formula (reduced); §7.1 Stance Counter kept authored (Hodge ~85% cyclic, *resisted* reduction — author only the irreducible). (b) §11.2 facing advantage emerges from field-of-view (lost-read + lost-reaction), not an authored Facing-Ob line.
**Test.** Does this system carry hand-authored tables that a rank/decomposition check would collapse? Does it add modifiers for effects its primitives already imply? Either is avoidable apparatus.
**Serves.** NERS-N (no redundant apparatus) + NERS-E. *Caution:* do not over-reduce — a genuinely multi-role or irreducible structure (Stance Counter) must stay authored (Lesson-1 inverse).

### A6 — Attribute-weight parity by σ-leverage (referenced standard)
**Rule.** A point of any attribute should buy comparable outcome-leverage in its domain, measured as σ-leverage = (E[net/die]·multiplier)/(SD/die·√baseline) ≈ 0.30σ/pt at the reference build, ±~20%.
**Reference.** `attribute_weight_standard.md` (combat = Thread exact; social +17%; Command via ⌈(Cha+Cog)/2⌉ analyzed in `derived_stats_audit.md`).
**Test.** Compute σ-leverage for each attribute feeding this system; flag any outside the ±20% band.
**Serves.** NERS-S (cross-system consistency), build balance.

### A7 — Resource parity by 1/k (referenced standard)
**Rule.** Linear ×N resources (capacity/buffer scores) all share proportional leverage 1/k per attribute point — independent of N — so they are mutually comparable. Multiplicative/stepped resources (e.g., Health) are the audited exception, not the template.
**Reference.** `derived_stats_audit.md` (Composure/Stamina/Concentration/Thread-Fatigue equivalent; Health the outlier).
**Test.** Are this system's resources linear ×N (comparable) or multiplicative/stepped (non-uniform — justify deliberately)?
**Serves.** NERS-S, build balance.

---

## How to adjudicate a system with this armature (procedure — not run here)

For a target system, walk A1–A7 as yes/no tests; each failure maps to a concrete remediation (the same mechanism combat used). Output is a per-system **armature-compliance line** plus the NERS verdict from the resolution-diagnostic skill (the armature feeds Stage 2 remediation with mechanisms, not just lessons). This procedure is the deferred cross-system work — **it is intentionally not executed in this conversation.**

The N3 question (σ-space scope) is answered *by* this procedure: a system passes A1 already (no fix needed), or fails A1 and the remediation *is* σ-space — which is how "propagate vs combat-only" gets decided per-system on evidence, rather than as a blanket call.

---

## Provenance & status

Extracted from combat_v32 mechanisms verified this session (σ-space impact, soft-cap foreclosure bound, Hodge reduction of matchup tables, FoV→emergent-facing, σ-leverage, 1/k). Status: **working standard, combat-derived.** Placement (this audit dir vs `references/` vs a dedicated standards location) and any promotion to canonical-standard status are Jordan's call, as with the proposal.

`[CONFIDENCE: high — every principle traces to a verified combat_v32 mechanism + an existing lesson/standard; the armature is distillation, not new claims]`
`[READ: combat_v32_proposal.md §1/§4/§7/§11.2/§12.3; attribute_weight_standard.md; derived_stats_audit.md; valoria-resolution-diagnostic-SKILL.md (six lessons, NERS)]`
`[SELF-AUTHORED — bias risk: armature derived from my own combat work; I flagged A5's over-reduction caution and kept the cross-system application explicitly out of scope rather than quietly grading other systems against my own yardstick in the same breath]`
