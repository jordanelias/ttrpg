# Refutation — v2 §4 (Light Function) + §9.4 (any-seed theorem)

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
_Role: try to BREAK `narrative_engine_design_v2_churn.md` §4 + §9.4. Read in full: v2, v1,
`00_grounding/00_engine_charter.md`, v1 fork 8, `spec_sections/s3_q4_render.md §Q4.8`, `critic.md`.
Method: working tree only._

---

## The money counterexample (one trajectory that hits every attack)

A **factionless PC in a peaceful settlement** engages 5 low-stakes local threads (marriage,
a debt, a rivalry, a shrine dispute, a harvest oath). A **high-imminence foreclosure looms two
settlements away** — nonzero but low tie-proximity to the PC. Trajectory:

1. The 5 engaged threads are **demotion-exempt** (§4-ii, v1 rule) and, being finite-budgeted,
   **fill the entire attention budget** (§6 "prose cost is O(attention budget)").
2. The looming foreclosure's selection score carries high **imminence + forecast mass** (§4) —
   the exact terms v2 *added* to fix v1's §0.5 critique — but it is **starved**: exemption + full
   budget leave zero room, so it never lights.
3. It resolves in the shade via faction autonomy ("autonomy is earned in the shade", §4 shade
   semantics) **before** any cast/impel deadline (§8 L4) schedules its intervention point.
4. Re-light renders the catch-up **retroactively as one chronicle sentence** ("while you were
   home, the border went", §4) — **telling, not showing** (§6: "showing carries the present;
   telling reserved for retrospect").

Result: a chronicle that is **connected** (all beats trace to the MS-clock root), **continuous**
(inertia kept the 5 local threads lit), and **rooted** (all local) — and **dramatically inert**:
no stakes surfaced, the one looming stake delivered as a summary line, its climax unplayable.
**Every invariant of §9.4 holds; no story results.** This single trajectory instantiates F1–F4.

Do the design's OTHER mechanisms close it?
- **meaningfulness gate** — no: the 5 local threads *pass* meaningfulness (identity/obligation
  touch is local and real); meaningfulness never required high stakes.
- **foreclosure_countdown (§3)** — partial: the countdown is *computed* and total-accounting
  forbids a *silent* drop, but an unlit countdown is never *foregrounded* → retroactive telling.
- **projected-beats (§6)** — no: "each **lit** thread carries a projected-next-beat." The starved
  thread is unlit, so no forward projection surfaces. Projection covers only what already won light.

Net: the other mechanisms guarantee **no-silent-drop + retroactive telling**. They do **not** close
the gap to "a story," to a **playable** climax of an **attended** stake, or to stakes-density.

---

## Findings

### F1 · MAJOR — §9.4 proves *legibility*, not *plot*; the theorem overclaims "a story"
- **Claim attacked:** §4 "The coherence guarantee — a story out of ANY branch"; §9.4 "A chronicle
  projected from a connected, continuous, rooted subtree is a narrative."
- **Evidence:** connectivity ⇒ a connected DAG; inertia ⇒ attention persistence; rooting ⇒
  proximity. None of the three, jointly or severally, yields **stakes, escalation, turn, or
  payoff** — the money counterexample satisfies all three and is inert. §9.4 itself deflates
  "narrative" to *"whose position, what they want, what happens next — all answerable"* — i.e. it
  actually proves the **legibility triad is answerable**, NOT that the answers are compelling.
  Legibility-answerable is satisfied by a plotless chronicle ("what is at stake?" → "little", still
  *answerable*). v1 §6 / doc-10 §8.5 already carry the honest NOT-list (no heroic-arc guarantee, no
  three-act guarantee) — but §9.4's theorem statement and §4's headline **do not carry that
  deflation**, so the doc reads as proving plot when it proves coherence.
- **Sub-bug (rigor):** §9.4 **misquotes its own criterion.** It cites the "dramatic-legibility
  criterion" as *"whose position, what they want, **what happens next**."* The actual triad
  (`spec_sections/s3_q4_render.md §Q4.8`, charter L129–131) is *"what is at stake / who is acting
  and why / **what changed**."* §9.4 silently swaps the retrospective third question for a
  **forward** one — the single question the invariants least support (forward answerability rides
  only on §6 projected-beats, which cover **lit** threads only). The theorem is stated against a
  triad the spec does not use, and forward-loaded.
- **REQUIRED_FIX:** (a) restate the theorem's conclusion as **"a connected, continuous, rooted, and
  *legible* chronicle — not a guaranteed satisfying plot"**; cross-reference the v1 §6 NOT-list in
  §9.4 and §4. (b) Correct the triad quote to the spec's `stake / actor / change`. (c) Extend the
  NOT-list with two new honest limits surfaced here (see F3, F4): *no guarantee an attended stake's
  climax is playable rather than retrospective*; *rooting yields proximity, not stakes-density —
  a quiet neighborhood yields a legible but plotless chronicle.*

### F2 · MEDIUM — invariant (i) connectivity is near-vacuous (root-connectivity ≠ narrative adjacency)
- **Claim attacked:** §4-i "every lit beat traces via causes[] to lit ancestors **or roots**; the
  lit subtree is connected by construction."
- **Evidence:** *"or roots"* makes connectivity trivial — **everything** eventually traces to a
  world-clock root (§4 "Roots (world clocks)"). A grain-price beat and a marriage beat both trace
  to the MS-clock root, so they are "connected" while sharing **no proximate stake or actor**.
  Graph-connectedness via a common *distant* ancestor is not narrative continuity between
  *successive* beats. The invariant guarantees the DAG is one component, which was never in doubt.
- **REQUIRED_FIX:** strengthen (i) to **proximate** connectivity — successive lit beats must share
  a *proximate* common ancestor **or** a shared actor/stake within N causal hops — or drop the
  connectivity claim to what it actually delivers (single-component DAG) and stop citing it as a
  continuity guarantee.

### F3 · MAJOR — invariant (ii) inertia guarantees attention, not payoff; the shade/autonomy race
- **Claim attacked:** §4-ii "Continuity is a property of the LIGHT, not the events"; shade
  semantics "autonomy is earned in the shade … re-light renders the catch-up retroactively."
- **Evidence:** inertia keeps a thread **lit**, but a lit, protagonist-**proximate** stake can be
  **terminally resolved by autonomy in the shade** (a low-tie resolving action need not itself
  light) **before** L4 cast/impel schedules its terminal intervention point. Charter Q4 (L120–121)
  guarantees "every major arc keeps ≥1 open intervention point until converging and routes through
  ≥1 playable scene" — but that guarantee **races** autonomy and is scoped to *major* arcs;
  nothing in §4 forbids autonomy from foreclosing a lit proximate climax. The design's only
  remedy is **retroactive telling**, which is continuity-without-drama.
- **REQUIRED_FIX:** add a **liveness invariant (iv)** to §9.4: *a lit, protagonist-proximate stake
  cannot reach a terminal (foreclosing) resolution in the shade without first surfacing its terminal
  intervention point — autonomy may **defer** a lit proximate climax but not silently foreclose it.*
  Or, if that is too strong to guarantee, admit the limit explicitly in the NOT-list (F1c).

### F4 · MAJOR — engaged-thread exemption × finite budget starves the imminence term (self-defeat)
- **Claim attacked:** §4-ii "engaged threads (player-participated) are demotion-exempt"; §4-selection
  the new **imminence** term; §6 "prose cost is O(attention budget)."
- **Evidence:** exemption + a finite budget interact so that a player engaging ≥ budget-many threads
  **occupies the whole budget**, starving every emergent candidate — **including a quiet arc about
  to foreclose**, which is *precisely* the case v2 added the imminence term to rescue (v2 §0.5 /
  §0-5 critique). The mechanism added to fix v1 is defeated by a v1 rule v2 kept. The **ordering is
  also unspecified** and both horns fail: if exempt threads **count against** budget → starvation
  (above); if exempt threads sit **on top of** budget → budget is unbounded → **breaks the
  O(attention budget) render-cost governor** the doc leans on in §6. "One-pass, order-independent"
  (§4 reflexivity bound) is only true for the *scored* partition; the exempt/scored accounting rule
  is never stated, so order-independence is **conditional on an undefined step**.
- **Is it a bug or the design?** As written it is an unacknowledged **bug**: the doc presents
  imminence and exemption as complementary and never reconciles them.
- **REQUIRED_FIX:** (a) **reserve** a budget slice for imminence/promotion that the exempt set
  cannot consume (e.g. exempt ≤ k of B; ≥1 promotion slot always live); (b) **specify** exempt-set
  budget accounting explicitly (against-budget, with a cap), restoring the O(budget) bound and
  genuine order-independence; (c) state the reserved-slot constant in the F-F surface (F6).

### F5 · MEDIUM — hard-bake: §7 DATA allowlist omits machinery named in §6
- **Claim attacked:** §7 "**Zero content literals**… no event, NPC, place, template string, or
  weight constant in kernel code — ever" (R-HB), enforced by the DATA allowlist ("everything
  swappable, versioned, schema-validated").
- **Evidence:** §7's DATA enumeration is the swap-path allowlist, and it is **incomplete** vs
  machinery §6 relies on:
  - **intent-class roster** (§6: "request, demand, warn, confide, accuse, deflect…" — the
    intent-grammar terminal set) — **not** a declared DATA class; if the grammar's class enum lives
    in the dialogue emitter it is a content literal in kernel.
  - **venue-class scene shapes** (§6/§8: "~12 venue-class scene shapes (setup → loop → resolution)"
    instantiated by the splice realizer, which is **KERNEL**) — **not** in the DATA list; the 12
    shapes have no declared schema/validator/swap path.
  - **chronicler / focalizer roster** (§6 "chronicler selection"; "focalizer 5"; §9.1's three named
    chroniclers) — **not** explicitly declared versioned data.
  - **aggregation templates** — §1 calls them "a first-class bank class" but §7 does **not** list
    them; only implicitly under "fragment banks." Borderline; confirm.
- **REQUIRED_FIX:** enumerate intent-grammar classes, venue-class scene shapes, and the
  chronicler/focalizer roster (and confirm aggregation templates) as first-class DATA classes in §7,
  each with schema + validator + CI round-trip; otherwise R-HB is under-enforced by an incomplete
  allowlist and these assets have no swap path.

### F6 · MEDIUM — authorial-surface honesty: F-F weight set omits real light tunables
- **Claim attacked:** §4 "The authorial surface — HELD BACK … the weight set (identity-touch ·
  forecast mass · imminence · tie-proximity · scale allocation · inertia constants) IS Jordan's
  narrative voice — exposed, versioned data."
- **Evidence:** tunables that demonstrably shape the light but are **absent from the enumerated
  F-F set**:
  - **attention-budget sizes** — the scarcity lever §6 says "manufactures significance by
    selection" (anti-slop property 3). Inherited silently from `player_agency §4.3`'s 3–5 envelope;
    it is arguably the single strongest authorial dial (how much story is told) and it is **not** in
    the held-back, versioned surface. Budget is Jordan's voice as much as any weight.
  - **anti-strobe floor** (§4-ii) — governs how sticky attention is; unstated whether it is an
    "inertia constant." If it tunes the light it belongs in F-F, named.
  - **durability** — a meaningfulness factor in the selection score ("durability × tie-proximity ×
    identity-touch") yet **missing** from the §4 F-F enumeration (which names identity-touch and
    tie-proximity but not durability).
- **REQUIRED_FIX:** pull budget sizes, anti-strobe floor, and durability into the enumerated F-F
  surface (or state, per tunable, why it is excluded). The honesty claim ("exposed, versioned data,
  presented for sign-off") is false while these sit in prose / inherited config.

### F7 · N/Ω/Q gate (term undefined in working tree — principled Necessity / Ω-closure / Quantifiability read; flagged)
_No `N/Ω/Q` definition exists anywhere in the working tree (grep clean across the audit folders,
skills, canon, references); treating it as an orchestrator shorthand and applying a principled read._
- **Light Function** — **N** (necessary): PASS — "pruning IS authorship" is well-argued (§0.7, §4).
  **Ω** (closure/termination): **CONDITIONAL FAIL** — one-pass/no-fixed-point is clean, but
  termination-under-saturation is the **F4** hole (exempt/budget accounting undefined), and the
  reflexivity bound (§4) is *asserted*, not shown non-divergent. **Q** (quantified/testable):
  **PARTIAL** — the selection score names its terms but gives no ranges/units and does not state the
  combination is fully multiplicative-with-clamps; F6's hidden tunables widen the gap. Verdict:
  **passes N, conditionally fails Ω, partially passes Q** — fix F4 + F6 to close.
- **Claim-grammar organ (§5)** — **N**: PASS (arguments need substance — sound). **Ω**:
  **OPEN-BY-DECLARATION** (acceptable) — §5's lane boundary ships the **interface contract only**;
  resolution closure is explicitly the SC lane's next stage. Honestly flagged, not a defect. **Q**:
  **DEFERRED** (acceptable) — evidence weight is "gradable from the object" (witness/chain/recency/
  standing) but the combining formula is **fork F-G** (form canonical, numbers Jordan's). One
  residual gap: **bluster pricing** ("priced, attackable") — the *price* is neither specified nor
  declared a DATA class (relates to F5). Verdict: **passes N; Ω open-by-design (OK); Q deferred
  (OK) — minor: declare the bluster-price table as versioned DATA.**

---

## Verdict

§4/§9.4 are **structurally sound but the any-seed theorem is over-stated and two mechanism
interactions are unresolved.** The three invariants genuinely deliver a **connected, continuous,
rooted, legible chronicle** — a real and useful guarantee — but **not** "a story" in the plot sense
the headline claims. The theorem needs an **honest weakening** (F1) and a **NOT-list extension**;
the **exemption × imminence starvation** (F4) and the **shade/autonomy payoff race** (F3) are true
design holes the doc does not acknowledge; connectivity is near-vacuous as stated (F2); the DATA
allowlist (F5) and the F-F authorial surface (F6) are both incomplete against machinery/tunables
named elsewhere in the same doc.
