<!-- SKELETON — mechanical spec only -->
<!-- Infill: references/throughlines_meta_infill.md -->
<!-- [EDITORIAL: PP-672 — throughlines hierarchical framework, canonical vetting guide, 2026-04-19] -->
<!-- [EDITORIAL: ED-717 — T-15a/b/c Hafenmark/Löwenritter/RM substrate-postures added, М-4 count 4→7, ED-717 CLOSED] -->
<!-- [EDITORIAL: Session B — T-10 struck (Niflhel dissolved), М-4 count 5→4] -->
<!-- [EDITORIAL: PP-674 — added tier N (Necessity Test), framework enforcement via vetting_gate, 2026-04-19] -->

# Valoria Throughlines Framework — Canonical Vetting Guide

**Purpose.** Evaluate every proposal for vision-alignment (belonging) and execution quality. Hierarchical: higher tiers more constitutive; a higher-tier failure cannot be rescued by lower-tier success.

**Adoption.** PP-672 (framework). PP-674 (tier N + enforcement). Applies to work after adoption. Existing canon grandfathered.

**Authority.** Jordan owns N, Ω, Μ. Co-owned М, Τ. Claude applies Q and the full protocol. Claude flags N/Ω concerns to Jordan; never unilaterally rejects for N or Ω failure.

**Enforcement (PP-674).** `valoria_hooks.vetting_gate` blocks commits to `canon/patch_register_active.yaml` that add Class A/B PP entries from PP-674 onward without a `vetting:` block. CI runs the same check externally.

**Load order.** For routine vetting, load this skeleton. Load infill (`throughlines_meta_infill.md`) only when a decision requires deeper justification — examples, rationale, worked cases, per-T tag table, full Μ̄ translation rationale.

---

## §0 N — NECESSITY (1)

**N:** *A proposal earns its existence in Valoria if it models a real, load-bearing dynamic of Renaissance-era political leadership — the ways leaders of political factions could succeed, fail, or die. Complexity is permitted only when grounded in the subject matter; complexity for its own sake is rejected, even when otherwise well-designed.*

**N-level questions** (all Class A/B must answer):
1. What Renaissance-era political dynamic does this model? (Name it.)
2. Is that dynamic already covered by existing mechanics?
3. Does the proposal produce meaningfully different player situations than existing mechanics?
4. Was the dynamic load-bearing in the historical subject, or edge-case?
5. What is lost by modeling this abstractly through existing mechanics?

**N failure modes** (see §7 Failure Lexicon):
- Fantasy imposition — from game-design convention, not subject grounding.
- Duplicate coverage — existing mechanic already models this dynamic.
- Edge case mechanic — dynamic was rare historically; doesn't earn dedicated mechanic.
- Abstractable — existing abstract mechanics cover it adequately.

**N failure = flag to Jordan. Do not autonomously reject.**

N is tier-0: checked before Ω. A proposal that fails N does not proceed to belonging vetting — complexity without subject grounding is rejected regardless of experiential fit.

---

## §1 Ω — INTENT (1)

**Ω:** *A proposal belongs in Valoria if it contributes to the central experience: a player making decisions inside a world whose ontology is the Thread substrate, where (a) strategic-layer actions produce cross-scale consequences the player can trace but cannot fully anticipate, (b) personal-layer moments of confrontation permanently transform the player's character through engagement with the substrate, (c) autonomous agents (NPCs, factions, clocks) continue generating consequential events regardless of player action, (d) no strategy or choice produces dominance — every action pays what it buys.*

**Ω-level questions:**
1. What cross-scale consequence? (Ω-a)
2. What personal-scale transformation? (Ω-b)
3. What autonomous events? (Ω-c)
4. What is the irreducible tradeoff? (Ω-d)

**Ω failure = flag to Jordan. Do not autonomously reject.**

---

## §2 Μ — MODES (4)

Four causal mechanisms by which Ω is produced. A proposal primarily serves 1–2; must not undermine others.

- **Μ-α PRESSURE AS ENGAGEMENT DRIVER.** Continuous pressure forces engagement over idling.
- **Μ-β AUTONOMOUS AGENT COMPOSITION.** Independent agents interact to produce events no agent predicts.
- **Μ-γ SUBSTRATE ONTOLOGY.** Every element is Thread-substrate configuration. Canon A1, A2.
- **Μ-δ CROSS-SCALE CONSEQUENCE.** Actions at any scale produce effects at other scales via shared substrate.

**Μ-level questions:**
1. Pressure contributed/alleviated? (Μ-α)
2. Autonomous events enabled/required? (Μ-β)
3. Substrate state measured/changed? (Μ-γ)
4. Cross-scale consequences? (Μ-δ)

---

## §3 М — META-THROUGHLINES (11)

Structural patterns across the 41 throughlines. Each subordinated to Μ modes. Expanded from 6 to 11 per S1–S7 rigorous audit synthesis v3.1 (ED-738).

| М | Pattern | Parent Μ |
|---|---|---|
| М-1 | Pressure is continuous | Μ-α |
| М-2 | Geography holds pressure | Μ-α, Μ-δ |
| М-3 | Substrate grounds all | Μ-γ |
| М-4 | Institutions stake substrate-postures | Μ-γ |
| М-5 | Scales connect through substrate | Μ-δ |
| М-6 | Choice is forced | Μ-α |
| М-7 | Borrowings are operational extensions (composite assembly) | Μ-γ, Μ-β |
| М-8 | Access is vertical-position gated (within the renderable) | Μ-β, Μ-γ |
| М-9 | Ontological inversion of clinical phenomenology | Μ-γ, Μ-α |
| М-10 | Environment as constitutive medium (bounded by the renderable) | Μ-δ, Μ-γ |
| М-11 | Voluntary and involuntary capacity duality | Μ-α, Μ-γ |

**Dependencies:** М-2→М-1 · М-4→М-3 · М-5→М-3 · М-6→М-1 · М-9→М-7 · М-10→М-3 · М-10→М-2 · М-11→М-6.

**Rating rubric:**
- **+** extends — new instantiation of the pattern
- **✓** satisfies — consistent with the pattern
- **−** violates — resolve or redesign
- **○** does not apply to proposal scope

**T→М tag table** (for Τ-level checks): see infill §3.1. Summary: all 25 T's covered; primary-assignment distribution — М-1: 4 · М-2: 2 · М-3: 4 · М-4: 8 · М-5: 7 · М-6: 5 · М-7: (framework design-level, cross-cutting) · М-8: 1 · М-9: 1 · М-10: 1 · М-11: 2. Full tag table in infill §3.1.

---

## §4 Τ — THROUGHLINES (25)

Source: `references/throughlines_complete.md`.

**Τ-level question:** Which T's does this touch? For each: extend, preserve, or break? If break, is there deliberate supersession? Log breaks to `canon/supersession_register.yaml`.

---

## §5 Q — QUALITY

Applied after belonging established. Q failure = iterate, not reject.

**Q-robust:** positive feedback loop.
- Three viable player approaches to any situation the mechanic governs.
- Visible, traceable world-state change from player action.
- Mechanic fires in scenarios without player action.
- **Dramatic legibility:** designer familiar with Valoria but unfamiliar with proposal can read game-state and answer in one sentence each — *whose position is at risk, what each named actor wants, what happens if no one acts next season*.

**Q-smooth:** composes without special-casing.
- Methodology matches governing subsystem.
- Scale-transition behavior specified.
- Temporal behavior specified: pause/queue/advance during scene vs season tick.

**Q-elegant:** depth from rule simplicity.
- Core rule restatable after one reading.
- Second-order consequence predictable without additional rule-reading.
- External dependencies enumerated; "except when X" flagged and justified.

**Q-level questions** (check when applying):
- Robust: 3 approaches + visible change + player-independent scenario + its stakes.
- Smooth: methodology + matching neighbor + scales + transitions + temporal behavior.
- Elegant: restated rule + predictable 2nd-order consequence + dependencies.

---

## §6 Μ̄ — MECHANICS (Godot)

**Μ̄-level question:** Implementable in Godot as described? What engine features required?

Implementation implications of higher-tier commitments: see infill §6 for full translation table (shader/clock/UI/state-machine mappings per Ω clause and Μ mode).

Headline rules:
- Strategic clock is real-time; single save per campaign; NPCs and factions autonomous.
- Substrate state parameterizes rendering (shaders, environmental UI).
- Every stat has a thread-state visualization.
- Tooltips show costs alongside gains.

---

## §7 FAILURE LEXICON

| Term | Fails |
|---|---|
| Fantasy imposition | N |
| Duplicate coverage | N |
| Edge case mechanic | N |
| Abstractable | N |
| Rest state | Ω-c, Μ-α |
| Dominant strategy | Ω-d, М-6 |
| Flavor-only | Ω, Μ-γ, М-3 |
| Scale break | Μ-δ, М-5 |
| Reskinned attractor | М-4 |
| Event without stakes | Q-robust |
| Special-cased | Q-smooth, Q-elegant |
| Cost-hidden | М-6 |
| Strategic-only | Ω-b |
| Personal-only | Ω-a |
| Authored emergence | Μ-β |

Full definitions with concrete examples: infill §7.

---

## §8 VETTING PROTOCOL

### §8.1 Scope classification

| Class | Definition | Vetting |
|---|---|---|
| A. New system | New subsystem/resource/action category/state machine | Full: **N** → Ω → Μ → М → Τ → Q |
| B. System extension | New mechanic within existing system | **N** → Μ → М → Τ → Q (Ω inherited) |
| C. Parameter change | Threshold/rate/cap on existing mechanic | Τ only |
| D. Content addition | New NPC/territory/arc/narrative beat | Τ only |
| E. Cleanup | Bug/typo/rename/reorg/register | Triage: touches mechanics? → escalate to D. No mechanics? → execute. |

### §8.2 Failure behavior

- **N fail → flag Jordan; do not proceed.** Complexity without subject grounding is rejected.
- Ω fail → flag Jordan; do not proceed.
- Μ fail → redesign required.
- М fail (single) → redesign OR documented tradeoff.
- М fail (multiple) → redesign required.
- Τ break → supersession log if intended; otherwise fix.
- Q fail → iterate.

### §8.2-A Subtractive disposition (ED-IN-0027, ratified 2026-07-08)

§8.2 routes every *failed* check to a constructive disposition (build / wire / redesign / flag /
iterate). It has no verdict for an *existing* action that should not exist, or should exist only as
part of a more general one. §8.2-A supplies that half: the canonical mapping from N/Ω/Q + the §7
Failure Lexicon to a **subtractive verdict**, so scope can be *reduced* upstream of realization, not
only added to downstream of it.

**Cardinal rule — judge as-if-built, never by build state.** Evaluate how an action *would*
contribute if built as its design intends. Stub / unwired / unbuilt / Godot-unported status is
orthogonal to the verdict (routing metadata only). A never-built action whose realized contribution
is load-bearing is **KEEP**; a fully-built action that would be dominant or redundant even when
realized is **CUT**. **Any subtractive verdict citing build-state as a reason is invalid by
construction.**

| Canonical signal (judged as-if-built) | Verdict |
|---|---|
| N-fail — not a load-bearing dynamic even realized (Fantasy imposition) | **CUT** |
| Duplicate coverage — the same job even if both are built | **PRUNE** (re-home) / **MERGE** (in-lane) |
| Abstractable / Edge-case — folds into a general rule, no lost decision | **DISTILL** |
| Q-elegant fail — not restatable after one read even well-built | **REFINE** |
| Dominant strategy (Ω-d, М-6) — a free win is not a choice | **CUT / PRUNE** |
| Flavor-only (Ω, Μ-γ, М-3) — no decision the player weighs | **CUT / DISTILL** |
| Passes N + Ω + Q as-if-built under adversarial attack | **KEEP** |

**Verdict ladder** (least→most removed): `KEEP → REFINE → DISTILL → MERGE → PRUNE → CUT`. Prefer the
weakest verdict that resolves the failure — REFINE/KEEP preserve the action; DISTILL/MERGE preserve
the *decision* while dissolving the *packaging*; PRUNE/CUT remove both.

**Intent gate** (on the design, never the code): DELIBERATE / NOT-INTENDED / UNDETERMINED. *"Not
wired/built/ported yet"* is never a gate value — it routes to the additive resolution program.

**Two binding guards.** (1) A subtractive verdict is a *scope reduction* only if it names the
downstream work (resolution-plan Stratum/OPT or lane task) it retires or shrinks — otherwise it
drops to an ordinary §8.2 finding. (2) No CUT/PRUNE/MERGE/DISTILL is final until an independent
adversarial pass has **steelmanned the action** (argued, as-if-built, for KEEP) and *failed* against
direct source. Full method + the 2026-07-08 corpus application (97 actions; 0 top-level CUTs, the
disposition landed against real over-articulation): `designs/audit/2026-07-08-pessimist-action-audit/`.

### §8.3 Conflict resolution

Higher tiers override lower. N precedes Ω — a proposal that passes Ω but fails N is rejected before Ω even applies.

### §8.4 Test battery

Protocol must correctly classify:
- Pass: PP-666 settlement adjacency (passes N — succession fracture is Renaissance-load-bearing; Medici, Habsburg, Visconti), hypothetical Hafenmark food vulnerability (passes N — Italian city-states repeatedly collapsed on grain supply), companion Thread-witness dialogue (passes N — confidant/witness politics is real dynamic).
- Fail: 10-season peace treaty (fails Ω-d), merchant caravan minigame (fails N — fantasy imposition), Standing-7 permanent boost (fails Μ-α/М-6), reskinned Hafenmark (fails М-4), hypothetical "legendary weapon" system (fails N — fantasy imposition from game-design convention).

Full walkthroughs: infill §5.

### §8.5 Enforcement (PP-674)

Class A/B patch register entries must include a `vetting:` block:

```yaml
vetting:
  class: A | B | C | D | E
  necessity: pass | fail | flagged   # N result
  omega: pass | fail | flagged       # Ω result
  mu: [primary-Μ-served, ...]        # list of Μ modes served
  m_ratings:                         # М pattern ratings per §3 rubric
    M-1: "+" | "✓" | "−" | "○"
    M-2: ...
    M-3: ...
    M-4: ...
    M-5: ...
    M-6: ...
  q: pass | iterate | skip           # Q-tier result
```

Class C/D/E entries may use minimal `vetting: { class: C }` (or D/E).
Pre-PP-674 entries may use `pre-framework: true` for grandfathering.

`valoria_hooks.vetting_gate` blocks commits missing the block. CI runs same check.

---

## §9 REGISTER INTEGRATION

No new registers. Uses existing:
- `canon/patch_register_active.yaml`: Class A/B entries include `vetting` field with Ω/Μ/М/Q results.
- `canon/editorial_ledger.yaml`: flagged concerns use Failure Lexicon terms.
- `canon/supersession_register.yaml`: Τ-breaks with supersession.
- `references/canonical_sources.yaml`: notes framework as vetting authority.
- `references/throughlines_complete.md`: М-tag annotations per infill §3.1.

---

## §10 AUTHORITY

| Tier | Owner | Claude |
|---|---|---|
| N | Jordan | Flag failures; no reject |
| Ω | Jordan | Flag failures; no reject |
| Μ | Jordan | Apply ratings; propose refinements |
| М | Jordan approves; Claude refines | Apply ratings; propose reclassifications |
| Τ | Co-owned | Propose new T's w/ Jordan approval |
| Q | Claude | Apply autonomously |
| Μ̄ | Dev team | Document implementation |

---

## §11 SCOPE

Effective PP-672. New work vetted. Existing canon grandfathered. When existing touched: touched aspects vetted; untouched remain. Retroactive audit separate future project.

---

## §12 LIMITS

- Not a simulation validator (rates need engine_v4 smoke-test).
- Not a fiction/flavor guide (worldbuilding, names remain Jordan's).
- Not a replacement for editorial ledger (ED tracks questions; framework vets answers).
- Not a hard filter. Jordan is final authority on disagreements.

---

*Infill: per-tier rationale, М-derivation walkthrough, per-T tag table, worked examples (5), failure-lexicon definitions with examples, Godot translation rationale, PP-671 historical note. Load only when routine skeleton insufficient.*
