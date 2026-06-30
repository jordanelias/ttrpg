# NERS Audit — Recent Combat Mechanics (Initiative · Kuzushi · Contratempo) + Queue

**Scope:** the three tactical layers added this session — initiative (substrate + differentiation), kuzushi/structure,
contratempo — plus a NERS-preview of the unbuilt queue (body-void, G3 stringer/disengage, G5 armour energetics).
**Question (Jordan):** are we proliferating player-facing mechanics into noise/unnecessary complexity, or can any be
consolidated/refined harmoniously? **Critical observation is wanted; cut-recommendations are explicitly not** — the
target is process quality.

**Instrument:** `valoria-resolution-diagnostic` (Stage 0 decompose+categorise → NERS verdict) + the
`valoria-mechanic-audit` redundancy lens. **Criteria:** canonical N/R/S/E from PI `<definitions>` (`canon/
definitions.yaml` is unreachable at that path — `[GAP: definitions.yaml — using PI canonical block, which carries the
full N/R/S/E]`). The P-01–P-15 constraints are metaphysical and GD-1 governs victory; **none bear on combat-mechanic
complexity**, so this rests on N/R/S/E.
`[READ: combat_engine/{wrapper,systems,combatant,config}.py — committed HEAD, state-mutation trace]`
`[READ: skills/valoria-mechanic-audit/SKILL.md; canon/02_canon_constraints.md]`
`[SELF-AUTHORED — bias risk]` I built all of this. I have hunted the overlap I am motivated to overlook and graded
against the criticism an independent reviewer would raise, not my own intent.

---

## VERDICT (first, no false balance)
**R: PASS. S: PASS with one double-count flag. N: PASS-with-tension. E: the real pressure point.** The mechanics are
robust (loops bounded, invariants held) and integrate consistently. The proliferation concern Jordan senses is
**valid and localises precisely**: it is **not** at the player-INPUT level (the new mechanics add no new player
choices — they ride existing combat events), but at the **hidden-CONSEQUENCE level** — the same handful of events now
move several hidden states, and the two newest states (**initiative and structure overlap on three shared triggers**)
plus the **contratempo/riposte outcome-identity** are the two genuine consolidation candidates. The queue worsens this
on one item (body-void) and is clean on another (G5).

---

## STAGE 0 — Decompose & categorise (the load-bearing step)
| Mechanic | Component | Quantity category | Unique role | Effect channel |
|---|---|---|---|---|
| **Initiative** (Vor/Nach) | feeds dice | **continuous resource** (signed, bounded ±1.5, decays) | tempo/timing *control*; **signed & transferable** (zero-sum steal); carries the **pre-contact seizure** + the **whole tradition-differentiation layer** | additive σ-edge on attack AND defence |
| **Structure** (kuzushi) | feeds dice | **continuous resource** (bounded [0.5,1], recovers) | physical *balance*; **absolute & per-fighter** (breaking yours doesn't help me); the **dynamic tempo fix** | multiplies tempo (cadence) AND defence |
| **Contratempo** | dice-outcome branch | **not a state — an event** | a counter on the read-win-vs-commit moment | sets `riposte=True`, voids the attack |

Both initiative and structure are continuous resources (Lessons 2 & 6 govern; both degrade smoothly, bounded — ✓).
Contratempo is an event that **reuses an existing outcome** (the riposte).

## The evidence — trigger → consequence matrix (from the code, not memory)
| Event (trigger) | Consequences now fired | Count |
|---|---|---|
| **Overcommit** (`overcommit_exposure>0`) | riposte-exposure *(pre-existing)* + initiative-loss + **structure-break** | 3 |
| **Hit lands** (`hit>0`) | wound + conc-drain *(pre-existing)* + aggressor initiative-gain + defender initiative-loss + **defender structure-break** | 5 |
| **Bind** (`bind`) | bind_sigma resolution *(pre-existing)* + initiative-steal + **structure-break** | 3 |
| **Read-win-on-commit** (`read_win and commit>=4`) | initiative-steal + contratempo-counter | 2+ |

**Initiative and structure both move on overcommit, hit, AND bind** — three shared triggers. That co-movement is the
spine of the N/E tension below.

---

## N — NECESSARY (nothing redundant; removal would worsen play)
- **Initiative — PASS.** It fills the literature's most-emphasised gap, and it is load-bearing for the stated game
  goal: the entire tradition-differentiation layer rides on its channels (seize/steal/hold). Its signed-transferable
  nature and pre-contact seizure are not duplicated anywhere. Removing it would lose the most.
- **Structure — PASS-with-tension.** It carries one genuinely unique, necessary role — the **dynamic tempo fix** (a
  flagged defect; nothing else makes cadence depend on current balance). But its *initiative-overlapping transitions*
  (the structure-break on overcommit/hit/bind) are where redundancy concentrates: on those three events it moves in
  lockstep with initiative, and **both ultimately just make the affected fighter less effective**. The honest read:
  structure's *tempo role* is necessary; structure's *break-on-the-shared-events* partly duplicates initiative's
  Nach-forcing. They are **not fully redundant** — they decouple at seizure (initiative-only), in effect channel (σ
  vs tempo), and in rate — but the mid-combat trigger overlap is real.
- **Contratempo — WEAKEST on N.** It adds **no new outcome** — it sets `riposte=True` and voids the attack, so its
  mechanical realisation is *identical to the existing riposte* (defender strikes, roles flip). What it adds is a new
  *trigger* (counter on the read-win-vs-commit moment, which the riposte didn't reach). So it is necessary as a
  *trigger-gap-filler*, not as a distinct behaviour. It also **shares its exact trigger** (`read_win and commit>=4`)
  with the initiative Indes-steal — so that single moment now fires two mechanics.

## R — ROBUST (holds at extremes; loops bounded)
- **PASS on loop safety.** Every new state is bounded with a paired damper: initiative (decay + hard cap), structure
  (recovery + floor), contratempo (gated + probabilistic). Validated: mirror 49–50 @ n6000, monotonic, mastery ~80,
  no-one-shot 18, 95% cap = 95.0. The positive-feedback risks the NERS process flags for such states are dampered.
- **Two watch-items (not failures):** (1) **cumulative armour compression** — across the three tactical layers the
  armour advantage drifted (medium ~71→67, heavy ~91→88); still strongly monotonic, but a primary physical axis is
  being slowly eroded by tactical layers that don't benefit armoured fighters. (2) **deep-commit pile-on** — a deep
  commit that gets read now triggers riposte-exposure + initiative-loss + structure-break + (contratempo) counter
  simultaneously; at the commit extreme this is a quadruple penalty on one choice. Both are robustness/balance
  watch-points worth an eye, not defects.

## S — SMOOTH (clean integration; consistent with siblings)
- **PASS, largely.** Continuous resources are handled consistently (clamp helpers, decay/recover, neutral-at-baseline
  so default fighters are unaffected). Contratempo **reusing the riposte path is the good kind of smoothness** — no
  new resolution path was added (this is consolidation already done correctly).
- **One double-count flag.** A hit reduces the struck fighter's effectiveness via **both** initiative (worse σ) **and**
  structure (worse tempo + defence); an overcommit penalises via riposte-exposure **and** initiative **and** structure.
  The same event reduces effectiveness through multiple states. It is defensible (a solid blow really does both
  stagger and cede momentum) and the magnitudes are individually small — but it is the same class of issue the
  engine's own `C-2` comment guards against elsewhere ("avoid double-counting defender skill"). Worth naming.

## E — ELEGANT (logically simple; player can intuit outcomes) — the pressure point
- The engine now tracks **five per-fighter hidden dynamic scalars** (stamina, concentration, readiness, initiative,
  structure) plus the engagement state-machine and the per-beat contest. The two newest (initiative, structure) **move
  together on the three shared triggers**, so a player perceives a single "momentum / how-well-am-I-doing" but the
  engine bookkeeps two. **Unless both are surfaced as distinct UI** (an initiative tug-of-war bar *and* a balance/
  stagger meter), they are effectively one *perceived* quantity carried by two *hidden* variables — which is precisely
  the "noise" sensation: not more to *do*, but more hidden machinery behind "why did I lose that exchange?"
- **Contratempo** introduces a named concept ("single-time counter") whose behaviour the player cannot distinguish
  from the two-tempo riposte (identical outcome). Two names, one observable behaviour — conceptual overhead unless the
  distinction is made perceptible (e.g., contratempo lands faster / can't be interrupted).
- **The redeeming structural fact:** the proliferation is consequence-side, not input-side. The mechanics ride
  *existing* events (overcommit, hit, bind, the read contest) — they added **zero new player inputs**. That is the
  opposite of the usual elegance failure (bolting on new player-facing systems). The cost is interpretability of
  outcomes, not decision overload.

---

## QUEUE PREVIEW (NERS-preview of the unbuilt items)
- **Body-void (passata-sotto / inquartata) — HIGH overlap.** It is "void + counter in one tempo," which the engine
  already approximates three ways: the **dodge** mode (void), **contratempo** (counter in one tempo), and the existing
  **displace-and-step-inside** (evade a committed thrust + counter). Building it as a fourth evade-counter is the
  clearest Lesson-1/E proliferation risk in the queue. *Observation:* it is expressible as a dodge-flavoured variant
  of contratempo (a void that also counters) rather than a new mechanic — a consolidation **opportunity**, your call.
- **G3 stringer + disengage — PARTIAL overlap.** *Stringer* (constraining the opponent's blade) substantially
  overlaps the existing **bind** (blade contact, `bind_sigma`). *Disengage* (cavazione / durchwechseln — going around
  the constraint) is **genuinely new** — the engine has binds but no action to *escape* one. *Observation:* the new
  value is the disengage; it could attach to the bind sub-state rather than arriving as a new stringer mechanic.
- **G5 armour energetics — CLEAN (lowest NERS cost in the queue).** It is a *calibration of the existing stamina
  system* (armour weight → faster drain + reduced recovery), empirically anchored (Jaquet et al., PLOS One). It adds
  **no new player-facing state** — it tunes a channel already present. *Note the interaction:* it further reduces
  armour's net advantage, compounding the R-watch armour-compression above; worth modelling together.

---

## CONSOLIDATION OPPORTUNITIES (observations, not cut-recommendations — per the brief)
These are design decisions for Jordan; each is a *possibility*, stated with its trade-off, none asserted as a cut.
1. **Initiative ⊕ structure.** Either (a) keep both and **surface both distinctly** (the distinction — signed/
   transferable tempo-control vs absolute balance — is real and becomes legible, justifying the two states), or
   (b) unify the *mid-combat Nach-forcing* into one path while keeping initiative's unique seizure/differentiation
   and structure's unique tempo-fix. The decision hinges on whether the player will *see* two states or one.
2. **Contratempo ⊕ riposte.** They are one observable behaviour (defender strikes + flip) reachable from three
   triggers (failed attack / neutralised attack / read-win-on-commit). Could be framed to the player as a single
   "counter" with three openings, or made mechanically distinct (single-time = faster/uninterruptible) to earn the
   separate name.
3. **The shared `read_win and commit>=4` moment** fires both the initiative-steal and the contratempo roll — already a
   natural single concept ("you read the committed attack"); consolidating their *presentation* would reduce perceived
   mechanism count without changing behaviour.

## WHAT IS GENUINELY SOUND (earned, not sham-cleared)
- **Input-level design is clean** — no new player choices were added; the mechanics ride existing events. This is the
  right discipline and the reason the proliferation is interpretability-cost, not decision-overload.
- **Loop safety is real and validated** (every new state bounded + dampered; invariants held throughout).
- **Contratempo reusing the riposte path** is correct consolidation already practised.
- **The initiative substrate/differentiation split** directly serves the stated game goal (distinct traditions) and is
  not duplicated elsewhere — its necessity is the strongest of the three.

`[CONFIDENCE: high — the overlaps are evidenced by the trigger→consequence matrix read from the committed code, not
inferred; the role-distinctions (why initiative≠structure) are equally from the code, so neither the findings nor the
"sound" calls are manufactured. The E grade is a judgement about player-perception that depends on UI choices not yet
made — flagged as such.]`
