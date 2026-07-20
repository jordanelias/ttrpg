# Ability system — consolidated master (rigor pass + consolidation) (PROVISIONAL)

**2026-06-13 · status: PROPOSED, Jordan-vetoable · consolidates the seven session docs into one architected spec**

**Verdict (review first): the accumulated model is sound in principle but architecturally loose. It carries (1) two
partly-redundant structures — the emergent competence economy *and* an inherited FFT/Troubleshooter equip-library;
(2) three overlapping "combinations matter" layers; (3) an under-constrained innovation mechanic; and (4) a
mechanical core that is 100% deferred to "sim-tuning." None is fatal; all are resolved by *architecting* rather than
adding. The load-bearing fix: a technique stops being a modifier and becomes unlockable *access to a behavior* —
which honors your unlock-and-slot desire *and* the emergent no-dials principle at once, and makes the 55-dials
failure structurally impossible. Combinations collapse into a rarity hierarchy (emergent base → sparse authored
sets → rare synthesis). The budget is point-buy. Legibility is solved in presentation, not by cutting depth. The one
honest dependency — the effectiveness functions are the real content and they do not exist yet — is named, not
hidden.**

`[SELF-AUTHORED — bias risk: this reviews seven of my own docs; written to break the accumulation, not defend it]`
`[READ: the engine state graph (wrapper.py transitions), channels (tradition.py), weapon physics (combatant.py) — this session]`

---

## §1 — Alternatives, extended (curiosity)

Seven structural framings for "how a fighter is built," beyond the one the docs converged on:

| | Framing | Core idea | Verdict |
|---|---|---|---|
| A | **Pure emergence, no techniques** | a fighter = channel profile + weapon; "techniques" are just *names* for what a profile does in a situation | too radical — discards the unlock-and-slot agency you asked for |
| B | **Techniques as access** | a technique = unlockable *permission + competence* to attempt a graph transition; magnitude emerges from channels | **adopted** — synthesises A's purity with your collection/build desire |
| C | **Weapon-primary** | the weapon's physics is the spine; traditions/channels express it | folded in as a *co-equal* axis, not the spine (§4) |
| D | **Profile-threshold emergence** | techniques *unlock automatically* when the profile crosses thresholds | kept as a *progression* option (techniques can emerge from depth, not only be taught) |
| E | **Use-based growth** | channels develop through *use*, not allocation; builds reflect a fighter's history | kept as a *progression-flavour* note over the point-buy baseline |
| F | **Opposition-web primary** | the build is defined by what it beats/loses to; channels downstream | set aside — over-formalises; the cycle lives *emergently* in the channel economy already |
| G | **Stances + tuning** | a few legible stances, continuous tuning within | set aside as a *legibility fallback* if the profile model proves unreadable |

The curiosity that paid off: framing B. It is the hinge of the whole reconciliation (§3).

---

## §2 — Adversarial review (dispassionate)

1. **Two partly-redundant structures (sharpest).** The model runs *both* the emergent competence economy (channels →
   effectiveness) *and* a discrete equip-library + phase-slots (FFT/Troubleshooter inheritance). After the emergent
   reframe, what does "equip technique X into the Bind slot" add over "have high tactile/leverage"? The model never
   decided whether techniques are *emergent consequences* of the profile or *possessed objects* — it tries to be
   both. Architectural incoherence.
2. **Innovation is under-constrained and possibly over-engineered.** "Compose a child from two parents by blending
   channels + chaining effects" — the composition rule is unspecified, chaining arbitrary node-behaviors legally is
   a hard engine problem, generated content is the hardest to balance (you cannot sim a technique that does not
   exist), and it is heavy apparatus for a deliberately rare event. Highest-risk, least-grounded piece.
3. **Three overlapping combination layers.** Emergent shared-channel reinforcement, authored auto-activating sets,
   and synthesis *all* reward "deep/coherent combination." Redundant unless each is given distinct work.
4. **The budget shape is unsettled, and the candidates conflict.** Point-buy vs slots+points-per-category vs
   use-based growth are *different games*; leaving it open hides a fork that changes progression, balance, and UX.
5. **Legibility asserted, not engineered.** Seven channels × seven phases × library × sets × synthesis × weapon
   scaling is a large surface. Elegance-of-principle (all from primitives) ≠ legibility-of-experience.
6. **The mechanical core is 100% deferred.** Everything rests on effectiveness *functions* (how steeply technique X
   scales with channel Y) that do not exist. The design is all skeleton; the hard part — the functions and their
   joint balance — is entirely "later."
7. **The reframe may be partly cosmetic.** If "winding scales with `blade_guard`" is steep enough that a rapier
   (0.45) winds uselessly, that is a *de-facto* gate wearing continuous clothing — the reframe renamed gates as
   steep scalings without removing their effect. Untested.
8. **Discovery is a separable meta-system.** Study-to-learn is appealing and fits the corpus axiom, but it is a
   whole intel/progression economy orthogonal to combat resolution — scope-creep risk.

---

## §3 — Reconciliation (cautious)

- **①, the hinge → techniques are access, not modifiers.** Adopt framing B. Your **channel profile** (continuous)
  sets *how well* you do things; your **learned techniques** (discrete, collectible, slottable) set *which behaviors
  you can attempt* — a reopen-rewind, a measure-intercept, a winding. A technique is never `+X`; it is "you may now
  attempt this transition," its strength emerging from channels. This keeps *both* structures with *non-overlapping
  jobs* (no redundancy), satisfies your unlock-and-slot collection, and makes the dial-failure **structurally
  impossible** — you cannot author a "+measure technique" because measure is a channel you invest in, not a behavior
  you access. Access gated by *learning* is bottom-up ("you cannot do what you never trained"), not a label gate.
- **②, innovation → keep as goal, defer as layer, bound the space.** Synthesis stays a design goal but is a *later*
  layer: the core (channels + access + emergent effectiveness) must work and tune *first*. And constrain it — under
  framing B, synthesis = gaining *access to a composed transition* drawn from a **bounded, enumerated** set of legal
  compositions of two accesses you already hold, not open-ended generation. Tractable and sim-testable; still feels
  like innovation.
- **③, three layers → a rarity hierarchy.** (1) emergent shared-channel reinforcement = the *always-on base*
  (coherent profiles self-reward); (2) authored auto-activating sets = *sparse*, signature doctrines only; (3)
  synthesis = *rare*, dual-mastery. Distinct work at distinct rarity — the redundancy dissolves by ordering, not by
  cutting.
- **④, budget → point-buy baseline, options noted.** Allocate a fixed competence budget across channels (most
  controllable, clearest to read). Use-based growth (E) and profile-threshold unlocks (D) are *progression layers*
  over it; Troubleshooter's slots+points is an *enrichment* — all deferred, not adopted now. The fork is *closed* to
  a baseline, not left open.
- **⑤, legibility → solve in presentation.** Do not cut depth. The player reads their **profile as one shape** (a
  silhouette/radar), their techniques as **named accesses**, and the exchange shows *which channel or access decided
  each beat* — which the tick-by-tick visual already demonstrates. The emergent model *helps*: one profile shape to
  reason about, not fifty dials.
- **⑥, deferred core → name the dependency.** Accept it, but state plainly: the next real step is building and
  jointly tuning a *small* number of effectiveness functions, and the model's viability *depends* on their being
  tuneable. No pretence the framework is finished.
- **⑦, cosmetic-reframe → make continuity real and test it.** Commit that effectiveness functions are continuous
  with **no floor-to-zero except true affordance gates** — a rapier winds at low-but-nonzero effect (rings *do* aid
  winding, per the source), distinct from a mace which *cannot* half-sword (no blade). Sim-verify that low-channel
  attempts are weak-but-occasionally-live, so the reframe is substantive.
- **⑧, discovery → scope out as adjacent.** Note study-to-learn as a *desirable connected system* serving the
  knowledge-of-others axiom, but **out of the core combat-resolution scope** — a separate effort. Scope discipline.

---

## §4 — The consolidated architecture (judicious)

```
 PRIMITIVES (universal)
   · 7 channels — Perception · Measure · Timing · Feel · Leverage · Composure · Structure
   · weapon physics — the real WEAPONS properties (blade_guard, percussion/mass/pob, clinch, reach, head, …)
   · base stats
        │  effectiveness EMERGES (continuous functions; no label gates)
        ▼
 ── CORE (build + tune FIRST) ─────────────────────────────────────────────
   · CHANNEL PROFILE  — allocated competence budget (point-buy). Sets HOW WELL. The bound:
       can't be good at everything → coherent profiles self-reward, scattered self-punish.
   · TECHNIQUES = ACCESS — unlockable/slottable permission to attempt a graph transition.
       Sets WHICH behaviors. Never a modifier. Learned from traditions (templates/curricula),
       practice, or study. Cross-training a tradition grants its weapons.
   · WEAPON — co-equal axis with the profile: its physics scales every access continuously,
       + a short list of true affordance gates (point→thrust, blade→half-sword, pommel→strike).
 ── LAYER 2 · SETS (sparse) ───────────────────────────────────────────────
   · coherence sets AUTO-ACTIVATE when their component accesses are all assembled (Troubleshooter
     middle path: authored combo→capability, but activation emergent from the loadout — assembled,
     not triggered). Signature doctrines only; everywhere else, coherence is the emergent base.
 ── LAYER 3 · SYNTHESIS (rare, later) ─────────────────────────────────────
   · dual mastery + circumstance → ACCESS to a COMPOSED transition, drawn from a bounded enumerated
     composition space. The poleaxe "anticipatory measure-control" lives here.
 ── PRESENTATION (the legibility solution) ────────────────────────────────
   · profile-as-shape + techniques-as-named-accesses + per-beat attribution ("the bind decided it").
 ── ADJACENT (separate scope) ─────────────────────────────────────────────
   · study-to-discover intel — serves knowledge-of-others; not core.
```

**The one-sentence model:** a fighter is a **channel profile + a weapon + a kit of learned behavior-accesses**;
*how well* emerges from the profile and the physics, *what's possible* is the kit, coherent profiles self-reward,
signature bundles auto-activate as sets, and deep dual mastery innovates new accesses — no label ever gates anything,
and no technique is ever a dial.

---

## §5 — Consolidation: what's folded, what's superseded

Collated, the seven docs and their fate:

| Doc | Contribution | Status in the master |
|---|---|---|
| comprehensive library | the hook inventory; the archetype roster | folded — the hooks become *accesses*; the 55-atom framing **superseded** |
| reconciliation | composite>atomic; method-primary; bounded | folded — composites = accesses; "method" = template |
| FFT parallel | unlock-and-slot; the bounded-loadout idea | folded — slots hold *accesses*; bound = the budget |
| granular phase-indexed | the 7 phases + 7 channels | folded — phases = where accesses live; channels = the profile |
| gating chain + sets | the three-relations disentangling (`set`/`mode`/adjacency as descriptors) | folded as *descriptive*; the **hard-gate chain is superseded** by emergence |
| emergent reframe | no label gates; traditions as learning-paths | **the spine** of the master |
| innovation + Troubleshooter | synthesis; auto-activating sets; study-to-discover; budget | folded — synthesis = Layer 3; sets = Layer 2; discovery = Adjacent |

**Superseded outright:** the 55-atom dial library; the hard label/mode gate chain. **Carried as descriptive
structure feeding emergent functions:** the `set`/`mode`/adjacency relations, the phase/channel taxonomy. This
master is the single document to work from; the seven are its derivation (git history preserves them).

---

## §6 — The deferred core, open decisions, honesty

- **The real next step (named, not hidden):** build and *jointly* tune a small set of effectiveness functions
  (channel × weapon → per-access strength). The architecture is only as good as these prove tuneable. Until then it
  is a sound skeleton, not a finished system. `[GAP: the mechanical core is unbuilt by design-stage; this is the work.]`
- **Open decisions:** (a) the access *catalogue* — which graph transitions are learnable accesses, and the few true
  affordance gates; (b) the budget — point-buy baseline confirmed? use-based/threshold layers wanted? (c) sets —
  authored signature only, or also emergent capstones? (d) the bounded *synthesis composition space* + its
  guardrails; (e) is study-to-discover in scope or parked? (f) the sim plan: coherent strong / scattered weak / no
  dominant profile, and the cosmetic-reframe test (low-channel attempts weak-but-live), ±2–3 pp at N≈3000.
- **Honesty:** `[CONFIDENCE: high]` that the access framing resolves the redundancy and the dial-failure, and that
  emergent-not-gated is right. `[CONFIDENCE: medium]` on the rarity hierarchy and the synthesis bounding (sound,
  unproven). `[CONFIDENCE: low / GAP]` on anything quantitative — the functions are unbuilt. Mechanical, not
  creative; historical names stay anchored and remain templates, never gates.

Provisional; engine unchanged. This is the consolidated master: **profile + weapon + learned behavior-accesses;
emergent effectiveness; coherence self-rewarding; sets that assemble; synthesis that innovates; presentation that
makes it legible — one architecture, the seven prior docs folded in.**
