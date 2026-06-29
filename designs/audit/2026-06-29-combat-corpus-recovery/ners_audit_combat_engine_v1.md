<!-- [SUPERSEDED 2026-06-04] Reconciled against its critique + a grounded investigation. The working master is
     ners_audit_combat_engine_v1_RECONCILED.md. Key changes there: Necessary upgraded PASS (the "dead apparatus"
     is deliberately STAGED scaffolding, not redundant); wound-model gap CLOSED (clean bounded clock); a missed
     wound→pool loop added (bounded by felling); the #1 defect re-sharpened to un-propagated ratification
     (canon-of-record still contradicts the ratified engine). Retained for provenance. -->

# NERS Audit — `combat_engine_v1` (personal-combat resolution engine)

`[SELF-AUTHORED — bias risk]` I built this engine and ratified it earlier today (ED-900). Per the
valoria-resolution-diagnostic guardrail I am treating it as external work and actively surfacing the
case an independent reviewer would file against it, **not** defending the ratification. A ratified
system can still have NERS gaps; ratification is a canonical-authority decision, NERS is a quality
assessment, and the two are not in tension.

**Date:** 2026-06-04 · **Skill:** valoria-resolution-diagnostic (Stage 1–4) · **Scope:** the modular
resolver at `designs/scene/combat_engine_v1/` (wrapper / systems / core / config / combatant / geometry
/ tradition).

---

## VERDICT (first)

**NOT fully NERS-compliant.** The engine is *structurally robust* but carries verified dead apparatus
and deviates from its own canon on two derived quantities.

| Criterion | Verdict | One-line basis |
|---|---|---|
| **Necessary** | **PARTIAL FAIL** | 4 of 5 baked geometry coefficients unconsumed; tradition channel levers inert; focus/spirit barely-necessary. |
| **Robust** | **STRONG** (minor findings) | Every feedback loop damped **and** bounded; pools 6–12D avoid the worst small-pool variance; no one-shot; 95% cap. Minor: an out-of-breath step-cliff; disposition behaves against its documented intent. |
| **Smooth** | **WEAK** | Resolution-pool basis and Concentration formula both deviate from canon; methodology friction with dice-pool siblings. |
| **Elegant** | **WEAK** | Dead apparatus + very high Class-C constant count + the `disp`/Disposition naming collision. |

**Severity-ranked findings (worst first):**

1. **[S · high]** Resolution pool = `max(5, History+6)`, **Agility-independent** — deviates from the canonical Combat Pool (PP-615: `Agi×2 + Hist + 3`). *Intent gate: DELIBERATE* (Jordan struck reverting; r1 docstring documents the redesign) → reclassify as a **documented deviation**, not a defect. It still creates the largest single Smoothness friction with canon/siblings.
2. **[N/E · medium]** **Dead apparatus (verified).** `geometry.bake()` returns `{gap, thrust, cut, perc_conc, halfsword}`; only `gap` is read anywhere in systems/wrapper/core. `thrust`, `cut`, `perc_conc`, `halfsword`, `can_halfsword_thrust` are computed and discarded. Tradition channel levers are likewise registered-but-INERT. Over-engineering is a defect.
3. **[S · medium]** Concentration = `3·focus + spirit` deviates from ratified `derived_stats §5.2` (`Focus×3`). *Intent gate: NOT intended* — an un-propagated canon conflict. A true finding.
4. **[R · low]** Disposition is a monotonic aggression **reward** (disp1→7 vs neutral = 47/49/53/54), but `config` documents "both poles cost / neutral optimal." Behaviour ≠ stated intent. *Intent UNDETERMINED* (Jordan may now want aggression rewarded).
5. **[R · low]** Stamina `oob` penalty is a **step** at `stamina ≤ 0`, sitting on top of the already-smooth fatigue ramp (`fat = 1 − stamina/max`) — a small accidental cliff (Lesson 6).
6. **[E · low]** `disp`/Disposition **naming collision** — the engine-invented combat temperament shares a name with the canonical relational Disposition value. Invention deliberate (Jordan struck renaming); the clash is accidental and confusing.
7. **[N · low]** focus/spirit are weak per-point (+1 = 54/56) and the "compound over long fights" claim is **unsubstantiated** (see Phase 2). Barely necessary — they clear 50, so not redundant, but they carry little weight.

`[GAP: wound-tracker interval structure — not re-traced this turn]` Health is a continuous pool depleted
to a felled threshold (no one-shot: max single hit 18 < health 40, verified). Whether intermediate wound
thresholds impose step-penalties was **not** independently re-traced this session; Phase 3b is flagged
accordingly. If such thresholds exist they are intended clock-thresholds (exempt); if not, Health is a
smooth resource.

---

## METHOD & GROUNDING

`[READ: this session — designs/scene/combat_engine_v1/{wrapper,systems,config,combatant}.py full; geometry.py + tradition.py via targeted grep; byte-verified == HEAD]`
`[READ: canon/02_canon_constraints.md — P-01..P-15 (§A immutable) + GD-1..GD-3 (§B mutable) full]`
`[READ: empirical battery this session — per-point attribute tier, burst/turn distribution, weapon roster vs arming (unarmoured+heavy), 8-tradition matrix + familiarity, disposition axis, small-pool mirrors, no-one-shot, multi-hit under tempo asymmetry]`
`[CONFIDENCE: high on Necessary/Robust/Smooth findings (each grounded in a read or a measurement); medium on the wound-interval question (GAP above)]`

**Constraint compliance (P-01..P-15, GD-1..GD-3).** A first, easily-missed result: **none of the
canonical constraints bind personal combat directly.** P-01..P-15 govern Thread operations, monstrosity
ontology, rendering, Coherence, and being-persistence (metaphysics); GD-1..GD-3 govern faction victory,
faction threat-response, and the insurgency pipeline (faction scale). The combat engine resolves a duel
between embodied characters; it neither performs Thread operations nor produces faction-scale victory.
**Verdict: not in scope of any P-/GD- violation test → compliant by orthogonality.** Worth recording so a
future reviewer does not mistake silence for an unchecked pass.

---

## STAGE 1 — MECHANICAL DIAGNOSTIC

### Phase 0 — Decompose & classify every quantity

| Category | Quantities |
|---|---|
| **Continuous resources** (degrade across a fight) | Health/wounds; Stamina (`3·End + 2·Spirit`); Concentration (`3·focus + spirit`); Poise (`poise_factor`, band 0.5–1.0); Initiative/"Vor" (momentum scalar, bounded ±1.5). |
| **Discrete accumulators / clocks** | Degree bands `{fail, partial, success, overwhelming}` (intended thresholds); feint count (cap 3); burst exchange count (cap `BURST_MAX=4`); wound count *if* interval-structured (GAP). |
| **Base parameters** | 7 attributes (strength/agi/end/cog/att/focus/spirit) + History (skill track) + `disp` (temperament) + weapon geometry (`reach/spd/wt/hands/head/grip_len/head_len/guards`) + ~100 Class-C constants. |
| **The hub** | `net_sigma` — the σ-sum of nearly every mechanic → `effective_ob` → `degree`. One resolution funnel. |

### Phase 1 — Stress points (where the math does its worst work)

- **Small pools.** `resolution_pool = max(POOL_FLOOR 5, History + BASE_POOL 6)` → History 0–6 yields **6–12D**. A success-counting engine has its steepest S-curve sensitivity and highest variance at small N; combat's floor-of-5-plus-base-6 holds it in a **moderate** regime, materially better than the faction layer's bare 1–7D stat rolls. → **a Robustness positive, not a weakness.**
- **Thresholds.** Degree bands (intended); `oob` at stamina 0 (a cliff — see 3b); collapse at −4 (terminal/separation); poise floor 0.5.
- **Compounding.** Two positive-feedback sites — the initiative/Vor loop and the poise/kuzushi loop (analysed in Phase 4).

### Phase 2 — Characterize each finding (behaviour + evidence)

- **Geometry dead apparatus.** `geometry.bake()` docstring: returns `{gap, thrust, cut, perc_conc, halfsword}`. Grep of `w['…']` / `c.w['…']` reads across systems/wrapper/core returns **only `w['gap']`** (systems L126/129, core L60) among the baked keys; the consumed remainder are *raw* geometry params (`reach, spd, wt, hands, head, grip_len, head_len, blade_guard, hand_guard`). `thrust`, `cut`, `perc_conc`, `halfsword`, `can_halfsword_thrust` show **no read**. The validated armour-defeat rotation (sabre 86→0, greatsword 68→4, dagger 25→93, mace 7→73, poleaxe 39→83, spear 91→78) is therefore produced by the lethality-state logic over raw params, **not** by the baked cut/thrust/percussion coefficients. → four-fifths of the module's stated derivation is dead.
- **Inert tradition levers.** `tradition.py`: channel levers (`measure/tempo/leverage/visual/tactile/precommit/balance`) are *registered but INERT until `eff_cw` is wired*; only the channel **weights** (familiarity-scaled) are live. Those weights produce the observed tradition-vs-none spread (german 52 ↔ spanish/chinese/filipino 60) while the ability/lever layer does nothing yet.
- **Concentration drift.** Engine `3·focus + spirit`; ratified `§5.2` is `Focus×3` (Focus alone). Divergent and un-propagated. (Stamina `3·End+2·Spirit` **matches** ratified `§4.2` — that one is clean, though `params/core.md:155` still shows the old `End×5`, a separate stale-doc issue.)
- **Disposition vs intent.** Measured disp1/2/4/6/7 vs neutral = 47/49/49/53/54 — monotone "more aggression wins more." The `config` comment frames disposition as a tradeoff where neutral is optimal. The overcommit cost does not offset the Vor-drift + deeper-commit gains.
- **Pool basis.** `max(5, History+6)`, Agility-independent, vs canon Combat Pool PP-615 = `Agi×2 + Hist + 3`. Deliberate per the r1 redesign docstring.
- **focus/spirit weakness + retraction.** +1 = 54/56, +3 = 68/69. I tested the prior "compounds over long fights" claim by raising History to lengthen fights — but high History makes fights **shorter and more decisive** (mean 5.4 turns vs 6.0), and the focus/spirit edge **fell** (67/66). The claim is unsupported; treat it as **retracted**. They are simply low-weight resilience stats with no demonstrated strong regime.

### Phase 3 — Curves

- **3a Impact uniformity.** Modifiers are σ-additive on the probit-like axis: uniform in z-space, non-uniform in probability (inherent to success-counting). At 6–12D the S-curve is gentler than at 1–3D, so impact is **more uniform than the faction layer**. The continuous resources degrade ~uniformly (stamina linear in depletion; concentration linear drains/proportional recovery; poise a linear 0.5–1.0 band). → broadly Lesson-2-consistent; residual non-uniformity is inherent and mitigated by moderate pools.
- **3b Threshold cliffs.** Degree bands and the feint/burst caps are **intended clocks** (exempt). The **stamina `oob` step at 0** is a genuine accidental cliff: it lands a discrete penalty on top of the already-smooth fatigue ramp, so a fighter crossing 0 gets both the smooth degradation *and* a step. Collapse at −4 is a terminal threshold (separation), defensible. Health/wound intervals — `[GAP]` above.
- **3c Role conflation (Lesson 1).**
  - `att` → `reading (½)` **and** `reflex (⅓)`: one base stat into two derived stats; att +3 = 90 (strong) is partly the double contribution. A mild role-breadth question (is perception independent enough from reaction to justify one stat feeding both? — defensible: awareness aids both, but it concentrates power).
  - `History` → pool size + bind + counter + parry/wind + stamina-recovery: many touchpoints, but all facets of **one** role (mastery) → **not** conflation.
  - `disp` → commit-skew + counter-selection + Vor-drift: one role (temperament) through three hooks → **not** conflation.
  - `poise` (dynamic structural state) vs `balance_eff` (agility competence): **correctly separated** — a Lesson-1 positive, since collapsing them would conflate a transient state with a standing trait.

### Phase 4 — Feedback loops (highest severity)

| Loop | Mechanism | Damper | Bound | Lesson 5 |
|---|---|---|---|---|
| Initiative / Vor | hit → +Vor → higher `net_sigma` → more hits | per-beat decay ×0.75 (gain < 1) | hard cap ±1.5 | **PASS** (two safeguards) |
| Poise / kuzushi | hit → poise break → slower tempo + worse defence → more hits | recovery +0.20/beat toward 1.0 | floor 0.5 | **PASS** |
| Fatigue | act → stamina down → slower/worse → … | inter-turn recovery | burst cap 4 (intra-turn) + collapse −4 (terminal) | **PASS** |
| Cross-system | personal-combat output (wounds, felled) → character state | — (no return edge) | downstream only | **PASS** (open, not a loop) |

Personal combat's outputs feed character Health/state and, above it, narrative and higher-scale muster —
but nothing closes a tight positive loop **back into** the same combat resolution. (Contrast the faction
worked-example's combat → Stability → muster → combat closure; personal combat does not form that ring.)
**Phase 4 verdict: every loop is damped *and* bounded.** This is the engine's strongest axis and the one
that matters most, since `intent_of_game` is itself a positive-feedback structure.

### Phase 5 — Intent gate (deliberate-with-safeguard / deliberate-without / accidental)

- Pool Agi-independent → **deliberate**, documented (struck reverting). PASS as a documented deviation.
- Concentration ≠ §5.2 → **accidental** (un-propagated). True finding.
- `disp`/Disposition collision → invention deliberate; clash **accidental**. Finding stands.
- Disposition aggression-reward → **intent UNDETERMINED**; flag for Jordan.
- Geometry dead coefficients + inert levers → **accidental/incomplete** ("INERT until `eff_cw` wired", baked-but-unread). Over-engineering finding.
- `oob` step at 0 → likely intentional threshold, but a cliff atop a ramp (minor).

### Phase 6 — Severity (consolidated in the verdict table above)

---

## STAGE 2 — THE SIX LESSONS (mapped by content)

- **L1 — split only where two independent jobs exist (role conflation):** PASS overall; mild `att`-breadth note; `poise`/`balance_eff` correctly split.
- **L2 — uniform-impact steps for continuous resources & base parameters:** PASS-ish; resources degrade uniformly; σ non-uniformity inherent and mitigated by 6–12D pools.
- **L3 — discrete accumulators legitimately have spaced thresholds (don't smooth intended clocks):** SATISFIED; degree bands + feint/burst caps are real clocks and are correctly left un-smoothed.
- **L4 — route through multiple sub-resolutions, not one fragile binary (esp. small N):** PASS; a turn routes through an approach stop-hit + a burst of 1–4 graded exchanges + bind/counter sub-checks; the outcome is graded (degree), never a single coin-flip; the 95% cap blocks certainty.
- **L5 — no loop both undamped and unbounded (highest severity):** PASS; initiative/poise/fatigue all damped + bounded; no cross-scale positive loop.
- **L6 — continuous inputs must not cross unintended discrete cliffs:** MINOR FAIL; the stamina `oob` step at 0 is the one accidental cliff.

---

## STAGE 3 — NERS VERDICT (per criterion, with evidence)

**Necessary — PARTIAL FAIL.** The resolution spine, the σ-hub, the bounded loops, the reach/measure/tempo
primitives, and the armour-defeat rotation all earn their place (each maps to observed, differentiated
behaviour). But three pieces do not currently pull weight: (a) **four of five baked geometry coefficients
are unconsumed** — verified by read-trace; (b) **tradition channel levers are inert**; (c) **focus/spirit
are barely necessary** (>50, so not redundant, but low-weight with no strong regime, and the "compounding"
justification is retracted). An independent reviewer's first question — "does every subsystem of this
~650-line, ~100-constant engine earn its place?" — gets a *no* on the geometry derivation and the lever
layer.

**Robust — STRONG (with minor findings).** The decisive evidence is Phase 4: every feedback loop is both
damped and bounded. Reinforcing this: pools sit at 6–12D (out of the pathological small-N regime), the
resolution is graded rather than binary, the 95% cap prevents certainty, and no one-shot exists (max hit
18 < health 40). Minor erosions: the `oob` step-cliff (L6) and the disposition tilt diverging from stated
intent (an unstated behaviour). Robustness is the engine's real strength and survives the adversarial pass
honestly — this is a *survived*, not a *failed-to-break-so-padded*, result.

**Smooth — WEAK.** Two un-propagated canon deviations: the **pool basis** (Agi-independent vs PP-615) and
**Concentration** (`3·focus+spirit` vs §5.2 `Focus×3`). The pool deviation is deliberate (intent PASS) but
still the largest methodology friction with the dice-pool siblings; the concentration deviation is
accidental and should be reconciled in one direction. Internal scale transitions (exchange → burst → turn
→ bout) are smooth now that the burst is bounded, and the engine→character-state handoff is clean — so the
weakness is specifically *horizontal* (consistency with canon/siblings), not *vertical*.

**Elegant — WEAK.** Three drags: the **dead apparatus** (a fix that bolts on structure the system does not
use fails E by definition); the **very high Class-C constant count** (~100+ tunables — heavy cognitive
and tuning overhead, even granting most are invisible engine internals); and the **`disp`/Disposition
naming collision** (two distinct concepts, one name — a standing source of confusion that Jordan has
chosen to keep). The σ-hub itself is defensible as invisible engine logic, but the carried dead weight is
not.

---

## STAGE 4 — RECOMMENDATIONS (scoped; defect-fix vs design-call marked)

This was an audit, not a fix-and-retest cycle, so Stage 4 is the set of changes that would close each
finding, with what to re-validate. Several are **Jordan's design authority**, not unilateral fixes.

1. **[over-engineering cleanup · N/E]** Either **wire** the geometry `cut/thrust/perc_conc/halfsword`
   coefficients (and the tradition channel levers) into resolution, **or remove** them. Removal is the
   simpler NERS-restoring move if wiring is not on the roadmap. *Re-validate:* the armour-defeat rotation
   is unchanged (it does not currently depend on them) and import asserts still pass.
2. **[defect-fix · S, low-risk]** Reconcile **Concentration** with `§5.2` — propagate canon into the
   engine *or* update §5.2 + the ledger to match the engine. Jordan picks the direction. *Re-validate:*
   focus/spirit per-point tier + any concentration-gated behaviour.
3. **[low-risk smoothing · R/L6]** Ramp the `oob` penalty toward stamina 0 instead of a step. *Re-validate:*
   the depletion curve and turns-to-decision are unchanged in shape.
4. **[design-call · R]** Disposition: if "both poles cost" is still the intent, raise the overcommit cost
   until disp7 ≈ disp1 ≈ 50; if aggression-reward is now intended, update the `config` doc to say so.
   *Re-validate:* the disp1→7 curve.
5. **[design-call]** Traditions: trim the stronger profiles (spanish/chinese/filipino) toward parity if
   traditions are meant to be equal-value training; leave as differentiated otherwise. *Re-validate:* the
   tradition-vs-none matrix.
6. **[design-call]** focus/spirit: re-weight up if they should matter per-point; otherwise accept them as
   low-weight resilience stats and drop the "compounding" framing from the docs.
7. **[documented deviation · no action]** Pool basis ≠ PP-615 is Jordan-confirmed deliberate; leave it,
   but ensure the deviation is recorded in canon (largely is, via the r1 docstring / ED record) so the
   inconsistency reads as intentional rather than as drift.

---

## ALL-DIRECTIONS SUMMARY

- **Bottom-up (primitives →):** the σ-hub aggregates ~20 terms into one graded resolution; the spine is
  sound; the *base* carries dead geometry/lever apparatus.
- **Top-down (NERS →):** Necessary partial-fail, Robust strong, Smooth weak, Elegant weak.
- **Vertical (scale transitions):** exchange → burst → turn → bout is internally smooth and bounded;
  engine → character-state is a clean downstream handoff, no loop.
- **Lateral / horizontal (siblings & canon):** pool basis + Concentration deviate from canon/sibling
  methodology — the locus of the Smoothness weakness.
- **Diagonal (cross-cutting):** `att` double-feeds reading + reflex (power concentration); `History` feeds
  many mechanics but as one role; `disp`/Disposition name clash spans engine and canon.

## CLOSING

Honest bottom line: `combat_engine_v1` is **structurally robust** — bounded loops, graded resolution,
moderate pools, no one-shot — but **not fully NERS-compliant**. It carries verified dead apparatus
(Necessary/Elegant) and deviates from its own canon on pool basis and Concentration (Smooth). Ratification
stands as Jordan's canonical decision; this audit files the quality gaps a clean-room reviewer would
raise, none of which the ratification concealed. The single most defensible immediate action is the
over-engineering cleanup (wire-or-remove the dead geometry/lever apparatus); everything else is either a
small reconciliation or a design-intent call that is Jordan's to make.
