# Personal Combat — Player Agency, Tradition Curricula, and the Ability-Lever Registry

## Status: PROPOSED — DESIGN-ONLY, HELD FOR JORDAN. Nothing here is built, ratified, or scheduled. No constant is changed by this document. It proposes an architecture and a registry; §9 states the preconditions that must land *before* any of it is implementable, and §11 lists the calls that are Jordan's, not mine.

**Date:** 2026-07-26 · **Lane:** PC · **IDs:** none allocated (design-only)
**Subject:** `systems/combat/combat_engine_v1/` at `248f344`
**Motivating measurement:** `audit/2026-07-26-combat-balance-customization-state/` (index + infill) — findings D1–D8
**Closes (if adopted):** ED-PC-0001 (the player-input surface, open since 2026-07-05) · `phase4_5_plan_v1.md` Phase 4b (abilities-as-access, NOT STARTED) · F23 (hollow `eff_cw` channels)

---

## §1 What the measurement forces

The balance-state report measured nine build levers and found the customization surface **broad and hollow**:

| finding | measured | consequence for this proposal |
|---|---|---|
| **D1** | four distinct archetypes land at 93.0 / 94.5 / 95.2 / 95.0 vs a neutral baseline — a 2.2pp spread, inside noise | weapon choice erases identity; *any* modulation layer built on top of this will measure as inert |
| **D2** | heavy vs none = 95.7%, and `c.armor` is read only as the target's protection | the second-biggest lever is unpriced |
| **D3** | disposition monotone 39.1 → 59.8 | the one existing "temperament" axis is a straight stat, not a trade |
| **D5** | tradition spread 3.8pp with `none` **highest** | tradition is flat because it is nearly absent, not because it is balanced |
| **D6** | 8 abilities across 5 of 8 traditions; 5 of 8 `eff_cw` channels identity ×1.0; every aggregate row inside ±4pp | the ability layer is a correct mechanism with almost no content |
| **D7** | `wrapper.engagement()` has no player-decision parameter | every customization choice is exercised *before* the fight |

**D6 is the precedent that governs this whole document.** The ability layer is not broken — the access gate works, graded investment works, cross-training works, and all of it is invariant-safe. It measures at zero because it is a small modulation on a surface where one lever (weapon) spans ninety percentage points. **Building a second modulation layer on the same surface will reproduce that result exactly.** §9 is therefore not optional sequencing advice; it is the condition under which this proposal is worth building at all.

**D3 is the cautionary shape.** `config.py` describes disposition as an axis where "BOTH poles cost." The engine implements only the benefit side of the aggressive pole. Any new player-facing axis that is not explicitly bound to *both* of its ends will become another monotone stat. §4's binding rule exists because of this.

---

## §2 The governing decision — where a player acts

Valoria has **no GM; the engine resolves everything** (CLAUDE.md). The engine resolves at *beat* granularity: `engagement()` runs a `while beats < soft*3` loop in which cadence, reads, commit-depth, mode, degree and outcome all resolve per beat. A human cannot meaningfully decide at that granularity, and a per-beat action menu would be the discrete-verb ACTIONS table that ED-PC-0007 already judged over-articulated and that `combat_engine_v1` deliberately superseded.

The engine has already answered the granularity question itself. `wrapper.fight()`:

> *each iteration = ONE engagement (~10s turn); victor emerges over MULTIPLE turns with persistent wounds/fatigue. `fight()` is the multi-turn SIM harness (runs to a decision for win-rates); **the GAME calls one engagement per turn**.*

So the player's decision cadence is **one decision per engagement**, and it is not my invention — it is the contract `fight()` already documents. Three tiers follow:

| tier | cadence | what the player supplies | status |
|---|---|---|---|
| **T0 — Build** | character generation / between sessions | weapon, armour, 9 attributes, 6 skills, tradition(s), techniques + invested level, disposition | **exists** (measured in the report §2) |
| **T1 — Plan** | once per engagement (~10s turn) | a small vector of **intents** that bias the engine's existing probabilistic gates | **this proposal** |
| **T2 — Beat** | per beat | *nothing* — the engine resolves; the trace narrates | **exists, and must stay closed** |

### 2.1 The three rules that make T1 legitimate

These are not stylistic preferences. Each closes a specific failure the repo has already ruled on.

1. **A plan is a prior, not a command.** `engagement_psychology_recovered.md` §B1: *"regimes are biased weights over the existing `engagement()` machinery, NOT a regime-selection planner."* An intent re-weights a gate the engine already rolls. It never selects an outcome, never adds a branch, never bypasses a contest.
2. **Intent is contested, never imposed.** ED-PC-0023 retired `impose_node` as top-down scripting: it forced a tradition's preferred node via a label-keyed coin-flip overriding the emergent resolution. A declared intent that *happens* is the same defect wearing a player's name. Every intent resolves against the opponent's own plan, the physics, and the read.
3. **Every intent is a trade with both ends wired.** An intent that buys threat-given without paying threat-received is D3 repeated. The two poles are already named in `combat_throughlines_v1.md` (*hit your opponent vs be hit by your opponent*) and in `phase4_5_plan_v1.md`'s Attack–Defence Convergence Principle. **The engine must charge the cost in the same commit that grants the benefit** — never in a follow-up.

### 2.2 What T1 is *not*

Not a stance system with named guards. Not an action queue. Not a cooldown economy. Not a "special move" list. Those are all T2 in disguise, and T2 is the engine's.

---

## §3 The Plan layer — six intents

The state graph already carries `INJECTION_POINTS` **as tested data** (`state_graph.py`, 9 points, `test_injection_points_reference_defined_states` verifies each against `STATES`). Composing on that registry rather than inventing a parallel one is the §0 "build bottom-up from primitives" discipline. Six of the nine points are player-facing; three are not, and the exclusions are principled:

| injection point | player-facing? | why |
|---|---|---|
| `exchange.read` | **no** | reading is a contest, not a choice. A player cannot decide to out-read someone. |
| `exchange.bind_entry` | **no** | entering the bind is a *consequence* of a mode and a degree, not a declaration. |
| `burst.continuation` | **no** | burst length is tempo-determined (`ACT_THRESHOLD`, `BURST_MAX`); declaring "keep pressing" would override cadence. |

The six that remain:

### I1 — MEASURE · `approach.measure` @ `Approach`

**Declares:** how you contest the closing of distance. Role-asymmetric, because the engine's approach is asymmetric: `close_rate` is a function of the `shorter` fighter alone; `stophit_p` is the `longer` fighter's threat.

| role | intent | benefit | cost (same commit) |
|---|---|---|---|
| shorter | **press** | `close_rate ×(1+k)` — fewer beats spent under the point | `stophit_p ×(1+k′)` — a headlong entry is easier to time (Silver's hand-before-foot; the stop-thrust against a step-in) |
| shorter | **measured** | baseline | baseline |
| shorter | **wait** | `stophit_p ×(1−k′)` — a cautious entry offers less | `close_rate ×(1−k)` — more beats at the longer weapon's measure |
| longer | **hold the point** | `stophit_p ×(1+k′)` — actively threatening | a *failed* stop-hit grants the closer a one-beat `close_rate` bonus (HEMA *Nachreisen* — travelling after the thrust that missed) |
| longer | **accept the close** | reaches the bind sooner, on their terms | forgoes the approach edge entirely |

**Why the cost is real and currently missing:** today a failed stop-hit costs the longer fighter *nothing*, and pressing costs the shorter fighter *nothing* (a faster close means strictly fewer stop-hit rolls). Both ends of this trade have to be built; neither exists.

### I2 — COMMITMENT · `exchange.commit` @ `Exchange`

**Declares:** where in the commitment–recovery spectrum you fight this engagement.

**Value:** `commit_depth`'s Beta skew `g = COMMIT_BETA_K·(DISP_COMMIT_K·lean − wary)`. An intent supplies a **second, bounded, per-engagement lean term** alongside disposition's standing lean and wariness — the identical mechanism, three inputs.

**Trade:** already fully built. Deep commit buys `COMMIT_SIGMA·(commit−3)` of attack σ and pays `overcommit_exposure` → riposte chance + Vor loss + poise break; shallow commit is the feint pole (full recovery, no tempo debt). **This is the one intent whose cost side needs no new work** — `commitment = recovery` is the engine's best-grounded axis.

**Bound:** the composed skew must respect `commit_depth`'s existing 0.25 spread-floor. Disposition + wariness + intent must never collapse the distribution to a spike; that floor is why wariness shipped at all (ENG-1's mandatory guard).

### I3 — GUARD · `exchange.mode` @ `Exchange`

**Declares:** the defence you default to when you are surprised.

**Value — and this is the most precise insertion point in the engine.** `read_contest` currently ends:

```python
mode = max(msig, key=msig.get) if read_win else modes[rng.randrange(3)]
```

A defender who **loses the read guesses uniformly across parry / dodge / wind.** That is the engine saying a trained swordsman surprised by an attack is as likely to attempt a wind as a dodge. He is not: he falls back on the guard his training made habitual.

**Proposal:** replace the uniform `randrange(3)` on the *lost-read* branch with a weighted draw over a per-fighter guard prior, formed from `(declared GUARD intent) × (trained modes) × (weapon `defense_affinities`)`. The won-read branch is **untouched** — a fighter who reads the attack still picks the best mode.

**Why this shape is safe:** it can only ever act where the fighter has *already lost* the contest, so it cannot make a good reader better. It is a floor on failure, not a ceiling on success. And it is bounded by construction: the best it can do is convert a 1-in-3 guess into the fighter's trained guard, which `mode_sigma` then still has to win with.

**Trade:** a guard prior is a *commitment to a line*. Weighting toward one mode must weight *away* from the others, so a fighter with a strong habitual guard is more exploitable by an opponent who reads it — the natural hook for `phase4_5_plan` §4a's within-fight threat-memory (dynamic A), if that is ever built.

### I4 — COUNTER · `exchange.counter` @ `Riposte`

**Declares:** appetite for the single-time counter over the safe two-time riposte.

**Value:** `counter_select`'s gate — currently `COUNTER_SELECT_BASE(0.45) × eff_cw(tempo) × (1 − DISP_COUNTER_K·disp_lean) × ability_factor('counter_select')`. Intent supplies one more bounded factor in a product that already has four.

**Trade:** fully built and unusually well-shaped. `counter_success_prob` gates success on training + reflex, and a **missed** counter cedes the seized Vor *and* eats the attack undefended (`wrapper.py:334-340`). The untrained single-time counter is already "a desperate-idiot move that mostly fails and is punished." Intent raises the reach for it; the existing punishment is the cost.

### I5 — BIND-OR-BREAK · `reopen.measure` @ `AwaitTempo`

**Declares:** whether you fight the bind you are in or refuse it and re-present at your own measure.

**Value:** `disengage_attempt_p` — the proactive fighting-withdrawal *inclination* (ED-PC-0030), currently derived purely from the leverage deficit. Intent biases the inclination; `disengage_clean_p`'s read contest and the `pursuit_sigma` Nachreisen consequence stay exactly as they are.

**Trade:** already built and genuinely two-sided — a read withdrawal is *pursued*, and the pursuer seizes the tempo (`ready[shorter] = max(ready[shorter], ACT_THRESHOLD)`).

**This is the intent that expresses the Italian identity the tradition decomposition says the scalar model *structurally could not*:** *"the 'refuse bind' (cavazione/disengage) is **missing entirely** from the scalar model — the vector cannot express it."* It is now expressible, because ED-PC-0030 built the mechanism. Nothing currently reaches for it deliberately.

### I6 — CONTACT · `contact.axis` @ `Contact`

**Declares:** whether you seek grips when an opening appears.

**Value:** the `grab_available` → `grab_sigma` → `grab_outcome` chain. Today a grab fires **automatically** whenever `opening_created` is set and the actor is grab-available — nobody chooses it. Intent gates the *attempt*; `grab_sigma` still decides whether it works.

**Trade:** committing to grips forgoes the strike that opening also afforded. That cost is currently zero (the grab is free, resolved after hit/bind/riposte) and must be built.

### 3.1 Summary — the plan vector

Six declarations, each an ordinal in a small range, set once per engagement:

```
Plan = (MEASURE, COMMITMENT, GUARD, COUNTER, BIND_OR_BREAK, CONTACT)
```

Every component defaults to *neutral*, and **the all-neutral plan must be byte-identical to today** (§8's load-bearing invariant, the same one Phase 4b names: *"empty kit == today, byte-identical"*).

---

## §4 Traditions as curricula

### 4.1 The problem to solve

D5: tradition spread is 3.8pp with `none` **highest**. With the imposition gate retired and the channel-weight vector removed, an ability-less tradition differs from another *only* through `familiarity()` feeding `WARINESS_K`. Both removals were correct — a hand-tuned channel vector and a forced preferred-node coin-flip were exactly the fiat the design principle forbids. But nothing replaced them, and "no top-down weight" currently means "nothing at all."

### 4.2 The resolution

**A tradition is a curriculum: which intents it teaches you to declare well, and which levers its techniques sharpen.** Efficacy never comes from the tradition; it comes from `weapon primitives × invested ability × state` — the `TRADITION-IS-NOT-A-WEIGHT` principle already recorded in `phase4_5_plan_v1.md` and re-ratified by Jordan's fiat-audit ruling.

Concretely, a tradition supplies exactly two things:

1. **Access** — which abilities you may invest in (`_invested`'s existing gate, already working and already measured inert-when-untaught at 47.7). Unchanged.
2. **Intent affinity** — which of the six declarations its curriculum makes *coherent*. This is not a bonus. It is that a tradition's abilities happen to hook the levers that resolve that intent, so declaring it while trained pays off and declaring it while untrained does not.

A tradition-less fighter can declare **all six intents at baseline.** Every build stays available (Jordan's governing design principle); training makes a declaration *sharper*, never *permitted*.

### 4.3 The curricula, from the existing decomposition

`tradition_decomposition_v1.md` already did this work bottom-up at graded source tiers. Mapping its emergent profiles onto the six intents:

| tradition | tier | signature intent(s) | grounded techniques → lever | authored today |
|---|---|---|---|---|
| **German** (Liechtenauer) | S1/S2 | **I5 hold the bind** · I4 counter | Winden → `spine_press`/`leverage` · Indes/Fühlen → `counter_success` · Zwerchhau → `counter_select` · Ringen am Schwert → `edge_grab` · Nachreisen → **`pursuit` (proposed)** | 4 of 5 |
| **Italian** (Fiore→rapier) | S2 | **I5 break the bind** · I1 measure | Mezzo tempo → `counter_select` · Misura → `measure` · Cavazione → **`disengage` (proposed)** · Stringere → `measure` | 2 of 4 |
| **Spanish** (Destreza) | S2/S3 | **I1 hold measure** | Atajo → `leverage` · Compás → **`balance` (bare today)** · círculo → `measure`/`init_hold_decay` | 1 of 3 |
| **English** (Silver) | S2 | **I2 commitment discipline** · I1 hold the point | True times → `anti_overcommit` · four governors → **`stophit` (proposed)** | 1 of 2 |
| **Japanese** (koryū) | S2 | **I3 guard** · I4 counter | Shinogi → `spine_press` · sen-no-sen → `precommit`/`counter_select` · maai → `measure` · kiriotoshi → fused parry-strike | 1 of 4 |
| **Chinese** (Ming) | S2 *caution* | — | sparse-tradition rule: **one** mechanic (burst-from-reach) or none | 0 |
| **Filipino** (FMA) | **unanchored** | — | `ability_armature` §5 is explicit: no S1/S2 anchor → **no ability** | 0 |
| **none** | — | all six at baseline | — | n/a |

**The source-tier discipline is not negotiable and is the reason two traditions stay empty.** `ability_armature.md` §5's selection-effect rule — counter-prestige is a European/Japanese observation, not a universal — is why `guardia` and `winden` were both *removed* when the HEMA critic caught them as category errors rather than kept as invented privilege (ED-PC-0026). Leaving Chinese and Filipino unrepresented is that discipline working, not an oversight. **A curriculum that cannot cite a documented technique and a real precedent is not authored.**

### 4.4 How C1 contextual balance emerges (rather than being imposed)

The C1 target is *no option globally best; each leads in some context; the unconditional field stays flat*. Under this model that is a **consequence**, not a tuning goal: an Italian build leads the rapier context because the rapier's primitives make I5-break cheap and the Italian curriculum sharpens exactly that lever; a German build leads the longsword context because the longsword's primitives make I5-hold profitable and Winden sharpens the bind. Neither gets a multiplier. **If the contexts do not separate under this model, the correct conclusion is that the curricula or the levers are wrong — not that a weight should be added back.**

---

## §5 The lever registry — which values an ability may modify

This is the registry the question asks for. Every engine value falls in exactly one class.

### Class A — FORBIDDEN. Never an ability target, at any magnitude.

| value | why |
|---|---|
| `core.strike` / `core.coupling` / `RESIST` / `DELIVERY` | the damage physics. An ability that edits how steel meets steel is scripting drift. |
| `adef_cap` / `armor_defeat_sigma` capability / `ADEF_THRESHOLD` / `PEN_THR` | armour-defeat capability. F19/F24 show this surface is *already* internally inconsistent across three models; adding a character-driven fourth input is the treadmill, not a feature. |
| weapon primitives (`mass`, `head_len`, `grip_len`, geometry) | these are the weapon. A technique does not change a blade's moment of inertia. |
| `WoundTracker` / `health_full` / `wound_interval` / `max_wounds` | trauma physiology. |
| `UPSET_FLOOR` | explicitly a designer rule (ED-PC-0036), not an emergent mechanic. |
| `resolution_pool` / the degree bands | the ratified resolver (ED-900/904), not re-litigated. |

**The rule behind the list:** an ability may change *how well a fighter negotiates* a contest. It may never change *what the world does* when steel arrives.

### Class B — GATED. Ability may change AVAILABILITY, never magnitude.

| value | ability may | may not |
|---|---|---|
| `capabilities.CAPABILITIES` predicates | — | **nothing.** Morphology gates are the weapon's, not the fighter's. Training does not put a point on a mace. |
| `grab_available`'s `opening_created` requirement | grant a trained grappler a grab on a class of opening they could not otherwise use | make grabs available from open measure |
| `disengage_attempt_p` eligibility | widen the leverage-deficit band in which a withdrawal is *attempted* | change `disengage_clean_p`'s read contest |
| `halfsword_target` form-switch | — | **nothing.** Already morphology-gated and correct. |

### Class C — LEGAL. The σ-domain and read-domain modulators.

**The 15 levers live today** (a fighter reaches them via `eff_cw` / `ability_factor` / `ability_bonus`):

| lever | op | consumer site(s) | authored ability |
|---|---|---|---|
| `measure` | × | `reach_sigma` meas_w · `init_hold_decay` | misura (IT) — **⚠ SIGN-BROKEN, see below** |
| `leverage` | × | `bind_sigma` · `init_steal_factor` · bind kuzushi | staerke_schwaeche (DE), atajo (ES) — **⚠ SIGN-BROKEN, see below** |
| `spine_press` | × | `bind_sigma` spine differential | shinogi (JP) |
| `counter_select` | × | `counter_select` gate | mezzo_tempo (IT), zwerchhau (DE) |
| `counter_success` | + | `counter_success_prob` | indes (DE) |
| `anti_overcommit` | + | `overcommit_exposure` | true_times (EN) |
| `edge_grab` | × | `contact.grab_sigma` hazard | ringen_am_schwert (DE) |
| `tempo` | × | `counter_select` · `init_steal_factor` · `init_overcommit_loss` · `tempo_pressure` · `init_emphasis_sigma` | **none — bare** |
| `visual` | × | `read_contest` · `reopen_prob` · `disengage_clean_p` | **none — bare** |
| `tactile` | × | `bind_sigma` reads · `init_steal_factor` | **none — bare** |
| `precommit` | × | `read_contest` read_d | **none — bare** |
| `balance` | × | `reach_sigma` foot_meas · `pursuit_sigma` | **none — bare** |
| `edge_read` | × | `legibility` edge-line term | **none — bare** |
| `choke_control` | × | `legibility` choke term | **none — bare** |
| `facing_regime` | × | `facing_target` | **none — bare** |

**Eight of fifteen levers are bare** (F23 counts five of the eight `eff_cw` channels; the three bare morphology levers make eight overall). The mechanism is wired and tested at every one of them; only the content is missing. **Authoring content into a bare lever is strictly cheaper and safer than adding a new lever, and should be exhausted first.**

**Proposed NEW levers** — each names a documented technique, an existing *pure function* with no current ability hook, and the intent it serves. No new mechanism is required at any of them; each is one `ability_factor()` call at a site that already computes the right quantity.

| proposed lever | op | consumer (exists today, unhooked) | technique · tier | serves |
|---|---|---|---|---|
| `disengage` | × | `disengage_clean_p` | Cavazione / durchwechseln · S2 | I5 |
| `pursuit` | × | `pursuit_sigma` | Nachreisen · S1/S2 | I5 |
| `stophit` | × | `stophit_sigma` | Silver's four governors / the true-time point · S2 | I1 |
| `guard_prior` | × | the lost-read branch of `read_contest` (§3 I3) | the habitual guard — *every* treatise · S1/S2 | I3 |
| `grapple_control` | × | `contact.grab_outcome` branch weights | Fiore *abrazare* 2nd Remedy / *Ringen* · S2 | I6 |

That is **20 levers total**, of which 7 have authored content today.

> **⚠ CORRECTION (independent `fable` audit, finding F5) — two of the levers this table calls LEGAL are
> currently SIGN-BROKEN, and the registry above sanctioned them.** `bind_sigma` computes
> `(leverage(agg) − leverage(def)) · eff_cw(agg,'leverage') / eff_cw(def,'leverage')`, so a factor > 1 amplifies
> a **negative** difference: **investing in the lever makes its owner worse whenever they are behind on the
> differential it multiplies.** Measured and independently re-verified: a dagger with `staerke_schwaeche` (×1.2)
> binding a poleaxe goes **−1.0562 → −1.1904** — training in bind-leverage *worsened* the bind. `reach_sigma`'s
> `measure` ratio has the identical shape: a `misura` (×1.15) defender suffers **15% more** from enemy reach.
>
> This is live for **any invested build** — the whole ED-PC-0024 surface — and default `equipped=[]` is why no
> test sees it. **Consequence for this proposal: §5.1 needs a fifth rule, and it is now rule 5 below.** Until
> the call sites are fixed, `measure` and `leverage` must be treated as **Class C-BROKEN**: authoring content
> onto them (§9 P2, increment I-7) would ship a lever that punishes investment.

### 5.1 The four rules a lever must satisfy

1. **One lever per physical fact.** A new lever must name its fact and show no existing lever already carries it. *This rule is currently violated:* ED-PC-0040 records that the armour-defeat deficit enters `armor_defeat_sigma`, `reach_threat`, `represent_measure_p` **and** the penetration knee "with no recorded budget — against a repo rule that forbids exactly that." Adding levers before that budget exists compounds it.
2. **σ-domain or probability-factor only.** A lever multiplies a factor inside a bounded contest or adds to a σ term. It never sets a probability directly, never short-circuits a contest, never post-processes an outcome.
3. **Bounded by construction.** `ability_factor` already clamps the composed product to [1e-4, 1e3] and caps investment at level 8 — after an unbounded level was measured to overflow the downstream sigmoids and *crash* fight resolution at ~15–22 (ED-PC-0024's adversarial-review fix). Any new lever inherits this, and any lever feeding a sigmoid must be re-checked against it.
4. **Ablatable in isolation.** Setting the lever's ability to level 0 must be *byte-identical* to it being absent. This already holds and must keep holding.
5. **Sign-safe on a signed contest.** A multiplicative lever may scale **its owner's own contribution**, or the
   resulting win-probability — it must **never ratio-multiply a signed difference**, because that inverts the
   lever's meaning for whichever side is behind (F5). Any new or re-authored multiplicative lever must ship a
   test that equips it on the *disadvantaged* side and asserts the term does not get worse. This rule exists
   because two shipped levers already violate it.

---

## §6 Appropriate values — magnitudes, pricing, and the budget

### 6.1 The magnitude problem, stated honestly

Our measurement gives the scale every proposed number must live on:

| lever class | measured marginal worth |
|---|---|
| weapon | up to **+47pp** (arming 49.7 → estoc 97.3) |
| armour (asymmetric) | up to **+46pp** (none → heavy) |
| attribute (cog/history) | **+20pp** per point |
| skill (dodge) | **+16pp** per point |
| disposition | **~+3pp** per point |
| **ability (any, at level 1–4)** | **~0pp — inside the ±4pp floor** |

A plan/curriculum layer priced to compete with the top of that table would be a balance catastrophe; priced where abilities sit now, it is invisible. **Neither is the target.**

### 6.2 The target: texture, not aggregate

ED-PC-0023's adversarial review already settled the correct instrument for a situational lever, after retracting a "+2.8pp specialist edge" as a tradition-membership confound: **per-fight texture with outcome preservation.** The live test `test_levers_add_texture_without_shifting_balance` measures it — 16–28% of fights play out differently, ~3–8% flip the winner.

**Proposed acceptance band for every intent and every new ability, at level 1 against an equal opponent:**

| quantity | band | instrument |
|---|---|---|
| aggregate win-rate shift | **|Δ| ≤ 2pp** at n ≥ 2000 | `build_levers.py` / `balance.py` |
| fights that play out differently | **≥ 15%** | `test_levers_add_texture_without_shifting_balance` |
| fights whose winner flips | **3–10%** | same |
| mirror fairness | **50 ± 2pp** at n ≥ 2000, all three loadouts | `build_levers.py mirror` |

A lever that fails the texture floor is inert and is **cut**, per the ablation gate and the `seize` precedent. A lever that breaches the aggregate ceiling is a stat, not a technique, and is **re-scoped**.

### 6.3 Pricing must be measured, not asserted

D4 (focus at −0.7pp/pt against cog's +20.4) is what a hand-set point-buy produces. **Proposal: character-generation costs are *derived from* the marginal-value instruments, not authored.** Concretely — `balance.py attr` and `build_levers.py skills` already produce the marginal table; a generator consumes it and emits costs proportional to measured marginal win-rate, and a CI gate fails when a shipped cost table drifts from a re-measure by more than a stated tolerance.

This is the ED-PC-0040 discipline applied one layer up: *a claim is a query, not a recollection.* It also means a balance change automatically surfaces as a pricing change instead of silently making one build free.

**Caveat, stated because it is load-bearing:** this only works if marginal values are *comparable*, and today they are not — D1 means weapon choice swamps everything, so a measured price for "one point of dodge" is conditioned on a weapon table that is itself the dominant term. **Pricing is downstream of §9.**

### 6.4 Intent magnitudes — the specific proposal

All `[SIM-CALIBRATE]`, all subject to §6.2's band, all default-neutral:

| intent | value modified | proposed form | neutral |
|---|---|---|---|
| I1 MEASURE | `close_rate`, `stophit_p` | `×(1 ± k·intent)`, **both**, `k ≈ 0.15` | `intent = 0` → ×1.0 |
| I2 COMMITMENT | `commit_depth`'s `g` | `g += COMMIT_BETA_K·PLAN_COMMIT_K·intent`, spread-floor preserved | 0 |
| I3 GUARD | lost-read mode draw | uniform → weighted over 3, weight `1 + PLAN_GUARD_K·intent` on the declared mode, renormalised | uniform |
| I4 COUNTER | `counter_select` product | `× (1 + PLAN_COUNTER_K·intent)` | ×1.0 |
| I5 BIND-OR-BREAK | `disengage_attempt_p` | `× (1 + PLAN_BREAK_K·intent)` | ×1.0 |
| I6 CONTACT | grab attempt gate | `× (1 + PLAN_CONTACT_K·intent)` | ×1.0 (today's automatic attempt = intent 0 *only if* the gate defaults open — see §11 Q4) |

Every `PLAN_*_K` lives in `config.py` (Class-C, workbench-tunable, never Class-A), consistent with that file's own header contract that *all* tunable coefficients live in one place — a contract ED-PC-0036 had to enforce after two inline magic numbers were found on the path producing ED-PC-0031's headline result.

---

## §7 What this does *not* propose

Stated explicitly, because scope creep here would be expensive:

- **No new state-graph node.** Six intents attach to six existing injection points at five existing states. `STATES` is unchanged; `INJECTION_POINTS` gains an `intent` field.
- **No discrete action menu.** ED-PC-0007's forward constraint holds: do not reintroduce Feint / Disarm / Tie-Up / Full-Guard as separate verbs when the continuous mechanics already subsume them.
- **No cross-bout persistence.** Consistent with `phase4_5_plan` §4a's "no cross-bout scars."
- **No multi-combatant scope.** ED-911 / `scene_combat_design_v1.md` stays deferred.
- **No re-litigation of the resolver.** ED-900/904 and the d10 substrate are the ground, not the subject.
- **No tradition weights, ever.** If differentiation does not emerge from curriculum × weapon × state, the curriculum is wrong.

---

## §8 Acceptance gates

Every increment carries all of these:

1. **Byte-identity.** All-neutral plan + empty kit ⇒ same seed, same outcome, bit for bit. This is the load-bearing safety check, and it is the one the U9 pass got wrong once already (a global-write leak in `test_both_channels_live_not_dead`, fixed in ED-PC-0022).
2. **RNG-stream discipline.** A neutral intent must draw **no** rng and must not reorder draws. The `represent_measure_p` short-circuit (`if _rep < 1.0 and rng.random() >= _rep` — inert off-plate, drawing nothing) is the pattern to copy.
3. **Mirror fairness** at n ≥ 2000 across arming/light, longsword/heavy, rapier/none.
4. **Texture + aggregate double gate** (§6.2). Both, not either.
5. **Write-sweep guard** for any newly cell-owned or plan-owned state, per CLAUDE.md §0.1's first check — grep the field's *assignments* and ship a guard that fails on a new bare assignment. `test_morale_write_sweep.py` is the template.
6. **A named falsifier per claim**, in the same commit, with its outcome (§0.1 check 3).
7. **`MEASURED-BY:`** on every quantitative ledger entry (`ci_claim_provenance_check`, blocking, ED-PC-0040 forward).
8. **Golden disclosure.** Any change that moves `r3_identity_golden.json` or `combat_armour_reference.json` regenerates deliberately, and **the diff is the required disclosure** — never regenerate to turn a build green.

---

## §9 Sequencing — the precondition, stated as a blocker

**Do not build the Plan layer or the curricula first.**

The ability layer is the controlled experiment that already ran: a correct, bounded, invariant-safe modulation layer, wired at fifteen sites, measured at **~0 aggregate**. The reason is not that the mechanism is bad — it is that the surface underneath it has one lever worth ninety points. A second modulation layer on the same surface will measure the same way, and the honest reading of that result would again be "the layer is inert," which would be wrong twice.

**Proposed order:**

| phase | work | why first |
|---|---|---|
| **P0** | **D1 — weapon-identity compression.** Batch 6's F21/F22/F24 plus the off-plate reach question. Until the 26-weapon 91–97 band separates, nothing above it can be measured. | measurement precondition |
| **P0** | **D2 — price armour.** Heavy vs none at 95.7% with no wearer-side cost makes I1/I5 largely moot: an armoured fighter has no reason to manage measure. | the intents need a reason to exist |
| **P1** | **D3 — resolve disposition's shape** (Jordan's call: genuine trade, or accept aggression as good). I2 composes with `disp_lean` in the same expression; building it against an axis whose intended shape is unsettled means calibrating twice. | I2 depends on it |
| **P2** | **Author the 8 bare levers.** Cheapest, safest, no new mechanism, directly closes F23 and D6. | content before architecture |
| **P3** | **Plan layer, one intent at a time**, each behind its own default-off gate, each through §8's full gate set. Order: I2 (cost side already built) → I3 (most precise, most bounded) → I5 (mechanism built by ED-PC-0030) → I4 → I1 (needs new cost machinery) → I6 (needs new cost machinery). | risk-ascending |
| **P4** | **Curricula + the 5 new levers**, per §4.3, source-tier gated. | needs P2's precedent and P3's surface |
| **P5** | **Measured pricing** (§6.3). | needs a stable surface to price against |

**If P0 is not done, this proposal should not be started.** That is the single most important sentence in this document.

---

## §10 Risks

| risk | severity | mitigation |
|---|---|---|
| Plan layer measures inert, exactly like abilities | **high** | §9 P0 gate; texture instrument rather than aggregate win-rate |
| An intent becomes a monotone stat (D3 repeated) | **high** | §2.1 rule 3 — both ends wired in the same commit; I1 and I6 do not ship until their cost machinery exists |
| Intent slides into imposition (ED-PC-0023 repeated, wearing a player's name) | **high** | §2.1 rule 2; every intent resolves through an existing contest; no intent may set an outcome |
| RNG-stream drift silently re-records every golden | medium | §8 gates 1–2 and 8 |
| Lever proliferation without a double-count budget | medium | §5.1 rule 1 — and the four-channel armour double-count must get its budget *first* |
| Curriculum authoring outruns its sources | medium | `ability_armature` §5 source tiers; Chinese/Filipino stay empty until anchored; `guardia`/`winden` are the precedent for removal-over-invention |
| Six intents is too many to present in a UI | low–medium | they are ordinals with neutral defaults; a UI may expose two and default four |
| Uncapped skills interact badly with intent multipliers | medium | skills are uncapped today (`skill()` is a bare `dict.get`); the ED-PC-0034 sign-flip is the precedent. Bound skills before multiplying them by anything. |

---

## §11 Open questions — Jordan's calls, not mine

1. **Q1 — Is one decision per engagement the right player cadence?** The engine's own `fight()` docstring says the game calls one engagement per turn. If the intended feel is finer-grained, T1 as specified is wrong and the whole shape changes.
2. **Q2 — D3: should disposition be a genuine trade, or is aggression simply good?** Both are legitimate designs. The code and its comment currently disagree, and I2 composes with it.
3. **Q3 — D2: should armour cost the wearer?** Mass/tempo/stamina/mobility are all plausible channels and all absent. This is a design decision with large blast radius, not a bug fix.
4. **Q4 — I6 default:** grabs currently fire automatically on any opening. Is neutral intent "attempt as today" (byte-identical, but then declining is the only real choice) or "do not attempt" (a behaviour change, and not byte-identical)?
5. **Q5 — Chinese and Filipino:** leave empty on the source-tier rule, commission the research to anchor them, or accept explicitly-flagged provisional content? The armature's rule says empty; that is a real cost in player-facing variety.
6. **Q6 — Does the guard prior (I3) need the threat-memory** (`phase4_5_plan` §4a dynamic A) to be interesting, or is a static trained guard enough for a first increment?
7. **Q7 — Scope of §6.3 measured pricing:** does character generation live in this engine's scope at all, or in a layer above it? ED-PC-0024 put the investment-bounding economy explicitly *out* of engine scope.
8. **Q8 — Carry context (Appendix B, Jordan's own direction).** Is the scene-context taxonomy right, and where does the primitive live? It is cross-lane (settlement law-and-order, fieldwork scene, strategic layer), so it is not a PC-lane call. **If adopted it revises §9's P0** — see B.5.
9. **Q9 — The off-hand slot** (defect register A2/A6). There is no shield, buckler or targe in the 51-weapon roster, and no slot to put one in; `main_gauche`, `paired_short` and `hook_sword` are all being measured in a configuration they were never used in. Is this in scope for personal combat, and at what priority?

---

## §12 Carry context — SPECIFICATION (promoted from Appendix B's sketch)

Appendix B recorded Jordan's direction and argued it supersedes §9's P0. This section turns it into something
buildable. **Everything here is measured against the live roster, not asserted.**

### 12.1 The decisive empirical result

Carriability's dominant term is **overall length = `head_len + grip_len`**, both already stored primitives. No
new data, no per-weapon table. Measured across the 51-weapon roster it separates into three clean bands:

| band | overall length | members |
|---|---|---|
| **concealable** | ≤ 0.60 m | dagger 0.33 · rondel 0.36 · stiletto 0.38 · main_gauche 0.43 · misericorde 0.43 · paired_short 0.57 · cinquedea 0.58 · hook_sword 0.60 |
| **civilian sidearm** | 0.75 – 1.20 m | mace 0.75 · tsurugi 0.88 · jian 0.94 · arming 0.96 · katana 0.97 · pulwar 0.98 · sabre 0.99 · shamshir 1.00 · falchion 1.03 · szabla 1.05 · tachi 1.06 · scimitar 1.06 · longsword 1.09 · nandao 1.09 · **rapier 1.14** · goedendag 1.20 |
| **weapon of war** | ≥ 1.50 m | sparr_axe 1.50 · odachi 1.56 · **estoc 1.57** · flamberge/greatsword 1.65 · staff 1.68 · poleaxe/bardiche/bec/lucerne 1.80 · … · guandao/ji 2.40 |

There is a **0.30 m empty gap** between the civilian band (top: goedendag 1.20) and the war band (bottom:
sparr_axe 1.50). The roster separates itself; the threshold is not hand-placed into a continuum.

**And the result that matters: all 26 weapons in the dominant 91–97% band are ≥ 1.50 m.** Every one. The
dominant band **is** the war band. Rapier 1.14 sits at the top of the civilian band, estoc 1.57 at the bottom of
the war band — exactly Jordan's example, falling out of stored primitives.

**Consequence: carry context removes the entire D1 dominance problem from every civilian context without
touching a single constant.** That is why it supersedes "compression."

### 12.2 Length alone is insufficient — the second term, and its honest limit

Longsword (1.09 m) and rapier (1.14 m) are near-identical in length and socially opposite. The separating
primitive already stored is **`hands`**: the rapier is 1H, the longsword 2H. So:

```
carriable(context) = f(overall_length, hands)      # both stored; no new per-weapon data
concealable        = g(overall_length)             # monotone decreasing
```

**Stated limit, because it is a real one:** "2H ⇒ weapon of war" is *culture-specific*, not universal. The
katana (2H, 0.97 m) was carried daily in Edo townscapes as the daishō. So the second term cannot be a global
rule — it has to be a property of the **setting's** legal regime, which is precisely why §12.4 puts the
threshold in the scene/settlement layer rather than in the weapon record.

### 12.3 The instrument — what makes this measurable rather than merely appealing

New table in `workbench/balance.py`:

```
context_weighted_field(context_weights) ->
    for each context: restrict the roster to what is CARRIABLE there,
                      measure each weapon vs the FIELD OF WHAT ELSE IS LEGAL THERE
    then weight the per-context fields by a scene-frequency distribution
```

**The balance requirement changes shape:** the *context-weighted* field must be level (±2–3pp); the raw matchup
table stays deliberately spiky, exactly as C1 already demands.

**The crux, stated because it is the frame's real cost:** this requires a **scene-frequency distribution** —
how often is an encounter a street fight versus a battlefield? That is a **content-design input, and it is
Jordan's**, not a measurement. The frame therefore trades "balance is a property of the engine" for "balance is
a joint property of the engine and the campaign's scene mix." That is a defensible trade for a game with a
strategic layer, but it is a trade, and it must not be smuggled in silently (§11 Q8).

### 12.4 Where the primitive lives — and why this is not a PC-lane call

`scene_context` belongs on the **encounter**, not the fighter, and it reads from the settlement/faction layer's
law-and-order state (the same street is different in a lawless town). That crosses PC, SE and FA lanes, so the
primitive's home is an **IN-lane or Jordan-level decision.** The PC lane can build §12.3's instrument against a
*stubbed* context and gain the measurement immediately, without waiting for the cross-lane primitive — that
decoupling is the recommended first increment (§15 I-1).

### 12.5 What carry context does NOT fix

- **Within-context dominance.** If the estoc still beats everything else legal on a battlefield, the frame did
  nothing there. *Partly falsified by the data, in the frame's favour:* against the battlefield-legal cohort the
  estoc's arc (96.5/96.0/92.0/95.0) is comparable to poleaxe (93.5/95.0/95.5/95.7) and lucerne_hammer
  (96.0/91.5/95.5/97.3). **The estoc looks globally dominant largely because the duel table pits it against
  daggers and sabres it would never meet where both are legal.** That is a real finding, and it is the strongest
  single argument for the frame.
- **A7a.** The cut path stays ungraded; curved swords stay all-cost-no-benefit *within* the civilian band, where
  they now actually have to compete. **Carry context makes A7a MORE urgent, not less** — it moves the sabre from
  "loses to spears" (excusable) to "loses to the arming sword in the only context it exists for" (not).
- **A2/A6.** The off-hand gap is untouched. Worse: carry context *raises its cost*, because the civilian band is
  exactly where rapier-and-dagger and sword-and-buckler belong.
- **D2's within-context half.** Access prices armour across contexts but not inside a battlefield.

---

## §13 The off-hand slot — SPECIFICATION (Q9)

### 13.1 The finding that makes this cheap

`core.coupling` already takes a `coverage` parameter, threaded all the way into `_transmit`, and
`core.COVERAGE_GAP = {'full': 0.15, 'partial': 0.5}` is defined. **No call site anywhere passes anything but
`'full'`** — ED-PC-0035's F8 recorded `'partial'` as unreachable dead code.

**So the shield's damage-model hook already exists and is simply not reachable.** A shield does not need new
physics; it needs the existing `coverage='partial'` path given a live caller. That converts the largest content
gap in the roster (A6) from "design a subsystem" into "wire a parameter that is already there, and author the
records."

### 13.2 Minimum viable increment (deliberately not the full system)

An `offhand` field on `Combatant`, defaulting to `None` (byte-identical when unset). Three effects, all on
**existing** terms — no new mechanism:

| off-hand | effect | existing site |
|---|---|---|
| **buckler / shield** | the attacker's `coverage` drops to `'partial'` | `core.coupling(coverage=...)` — already plumbed, currently dead |
| **parrying dagger** (main_gauche) | adds to the defender's parry affinity | `mode_sigma`'s `parry` branch / `WP.defense_affinities` |
| **paired weapon** (paired_short, hook_sword) | frees the contact axis without needing an opening | `contact.grab_available`'s `opening_created` gate (a Class-B availability change, §5) |

**Explicitly out of scope for the increment:** a second attack sequence. That doubles the exchange loop and is
where a paired-weapon system gets expensive; the three effects above are all σ/coverage modulations of one
sequence.

### 13.3 What it fixes

A2's three false negatives (`main_gauche`, `paired_short`, `hook_sword` are no longer measured in a
configuration they were never used in) and A6's absence (a buckler and a targe become authorable records). It
also gives the civilian band its historically-defining configurations — rapier-and-dagger, sword-and-buckler —
which §12 makes load-bearing.

### 13.4 Cost, stated

Coverage is a **damage-path** change. `'partial'` at 0.5 versus `'full'` at 0.15 is a large multiplier on the
gap term, so a shield is potentially very strong; it needs its own calibration pass against §8's bands, and it
moves both reference tables. **This is the one item in this extension that touches Class A territory** (§5:
the damage path is FORBIDDEN to *abilities*) — legitimately, because it is equipment physics rather than a
character modulator, but the distinction must be held deliberately, not blurred.

---

## §14 The A7a cut-grading increment — and the defect in my own fix sketch

### 14.1 My register's fix sketch was wrong; here is the correction

`combat_defect_register.md` A7d item 1 proposed: *"Extend `eff` scaling to `straight_cut`/`curved_cut` in
`core.coupling`, symmetric with the `cut`/`point` tokens."*

**That would be a no-op.** The existing form is saturating:

```
d *= min(1.0, eff / CUT_AUTH_REF)        CUT_AUTH_REF = 0.70
```

The native-cutter `cut_factor` range is **0.71 – 1.33** (minimum: hook_sword 0.71). **Every native cutter is
already at or above the reference, so every ratio would clamp to 1.0 and nothing would change.** The reference
sits *below the entire population it would be grading*.

Caught while planning the increment, before anyone built it. Recorded rather than quietly corrected, per this
lane's convention.

### 14.2 What the fix actually requires

Grading needs the reference to **straddle** the population, or a non-saturating form:

- **Option A — re-anchor.** Raise the native-cut reference so the 0.71–1.33 spread straddles it (a roster
  midpoint ≈ 1.05). **Coupled risk:** `CUT_AUTH_REF` also grades the *incidental* cut token, where 0.70 is
  anchored on hook_sword as "the weakest attested native cutter" (ED-PC-0011). Re-anchoring one path changes
  the other unless they are split into two constants — and splitting them needs its own justification, or it
  is two references for one physical fact (§5.1 rule 1).
- **Option B — non-saturating form** for the native path (linear in `eff` about a reference), so the whole
  spread expresses. Cleaner, but it is a *new functional form*, not the symmetry the register claimed.

**Both are re-baselines, not fixes.** Either changes damage for 16 weapons at every tier, moves
`r3_identity_golden.json` and `combat_armour_reference.json`, and needs the diff as disclosure (§8 gate 8).

### 14.3 Direction of the change, so nobody is surprised

Option A buffs the keen curved swords (shamshir 1.33, pulwar 1.24, scimitar 1.22, sabre 1.18 — the exact A3
collapse cohort) and nerfs the dull ones (hook_sword 0.71, greatsword 0.80, glaive 0.95). **That is the
intended direction** — it is what makes curvature a trade rather than a tax — but it is a *balance* change and
must be presented as one.

---

## §15 The increment ladder

Executable increments, risk-ascending, each with its own acceptance. **P0 from §9 (as revised by B.5) still
gates everything below I-2.**

| # | increment | depends on | acceptance |
|---|---|---|---|
| **I-1** | `balance.py context_weighted_field()` against a **stubbed** context map | nothing | the instrument runs and reproduces today's numbers when every weapon is carriable everywhere (identity check) |
| **I-2** | Derive `overall_length` / `carriable()` from stored primitives; publish the three bands | I-1 | bands reproduce §12.1 exactly; **no per-weapon table anywhere** (AST-checkable, like the existing no-name-table guard) |
| **I-3** | Off-hand slot, **buckler only**, via the dead `coverage='partial'` path | nothing | `offhand=None` byte-identical; buckler within §8's bands; both reference tables regenerated with the diff as disclosure |
| **I-4** | Off-hand: parrying dagger + paired-weapon contact availability | I-3 | A2's three weapons re-measured *in configuration*; their solo numbers explicitly retired as invalid |
| **I-5** | A7a cut grading (Option A or B — **Jordan picks**) | §14 decision | the 0.71–1.33 spread becomes visible in coupling; A3 cohort re-measured; roster-wide disclosure diff |
| **I-6** | Bound the T_vuln selection discount + re-examine `close_efficacy` as a *selection* input (A7b) | I-5 | the katana cuts at ≥1 tier; no weapon's mode flips on a <5% comparator margin |
| **I-7** | Author the 8 bare levers (§5) | nothing | each passes §6.2's texture floor or is cut |
| **I-8** | Plan layer, one intent at a time (§3 order) | P0, I-7 | per §8, all gates |

**I-1 through I-4 are independent of the P0 blocker** and can start immediately: I-1/I-2 *produce* the
measurement P0 needs, and I-3/I-4 fix a modelling gap rather than tune balance.

---

## §16 Adversarial pass — findings against this plan

Run against §12–§15 before publishing them. **This is a self-critique, not a structurally independent one**
(§10 is explicit that a critic who never saw the producer's reasoning is more independent), so it is weaker
than the four-dimension audit's method and should not be credited as equivalent. Findings that survived:

| # | finding | severity | disposition |
|---|---|---|---|
| **X1** | **The register's A7a fix sketch was a no-op** (`min(1, eff/0.70)` against a 0.71–1.33 population). | high | **Corrected in §14.1**, and the register's A7d amended. This is the pass's main catch. |
| **X2** | §12 makes balance depend on a **scene-frequency distribution that does not exist and is a content-design input**. The frame can therefore "prove" almost any weapon balanced by choosing the mix. | high | **Stated as the frame's cost in §12.3**, escalated to Q8. Not resolvable by me. |
| **X3** | "2H ⇒ weapon of war" is **culture-specific** (the katana falsifies it). | med | **Stated in §12.2**; pushes the threshold into the setting's legal regime, not the weapon record. |
| **X4** | §13's coverage change is a **damage-path** edit, and §5 forbids the damage path to abilities. | med | Legitimate (equipment physics ≠ character modulator) but **the distinction is now stated explicitly in §13.4** rather than blurred. |
| **X5** | Carry context is presented as superseding compression, but it **makes A7a more urgent, not less** — the sabre goes from losing to spears to losing in its own context. | med | **Stated in §12.5.** |
| **X6** | The 0.30 m gap between bands is real **for this roster**; adding one 1.3 m weapon would fill it, so the clean separation is a property of current content, not a law. | low | Stated here. The bands must be re-derived, never frozen as constants. |
| **X7** | I asserted "all 26 dominant weapons are ≥1.50 m" — **verified** against both tables, all 26 checked. | — | Survives. |

Findings I raised and **rejected on inspection**, recorded so they are not re-raised:

- *"Carry context is just a content gate, not balance."* Rejected: C1 already defines balance as
  context-conditional, and armour tier — an accepted axis — is exactly the same kind of gate.
- *"§13 should include the second attack sequence or it is not really paired weapons."* Rejected: that is where
  the cost is, and the three σ/coverage effects deliver A2/A6's value without it. Scope discipline.
- *"I-5 should just be done as part of batch 6's F21."* Rejected: F21 targets the capability/σ path
  (`adef_cap`), I-5 targets the damage path (`core.coupling`). Different owners; bundling them is the
  same-commit pattern that half-stood twice.

---

## §17 The Godot export contract — the gap round 1 missed entirely

Round 1 planned six increments that change `config.py` or `core.py` and **said nothing about what crosses into
the Godot port.** That is a real omission, because the crossing is a *blocking CI gate*.

### 17.1 Measured

`engine/engine_params/combat_engine_v1.json` exports **226 parameters — 201 `cfg` + 25 `core`** — generated
from `config.py` via `tools/export_engine_params.py` and round-trip-checked by the blocking
`engine-params-roundtrip` job. Every constant this plan proposes to touch is in it:

| constant | increment that moves it | exported? |
|---|---|---|
| `COVERAGE_GAP` | I-3 (buckler) | **yes** |
| `CUT_AUTH_REF` / a new native-cut reference | I-5 (A7a) | **yes** |
| `EXPOSE_SELECT_K` | I-6 (T_vuln bound) | **yes** |
| `ADEF_CUT`, `MAX_TEMPO_PEN`, `GRAB_SHORT_REACH_M` | adjacent items | **yes** |

**So every increment in §15 trips the round-trip gate.** That is not a problem in itself — regenerating the
export is one command — but it has a consequence the plan must carry.

### 17.2 The consequence: the export is wholesale, the port is not

The round-trip gate checks that the JSON **matches `config.py`**. It does **not** check that the Godot port
*implements* the constant. And the port covers **1 of 27 modules** (CLAUDE.md §6, `godot/skeleton/`), so most
exported constants have no consumer **by construction**.

**B13 (`PEN_DEFICIT_K` exported to a port with no penetration knee) is therefore not a one-off — it is the
pattern.** Each increment that adds or re-anchors an exported constant silently widens parity debt.

*Scope honesty:* I verified the export contents and the round-trip gate directly. I did **not** enumerate which
of the 226 the port consumes — that needs a read of `godot/skeleton/` against the JSON, which is a GO-lane job.
So "most have no consumer" follows from the 1/27 module coverage, not from a per-constant check.

### 17.3 What each increment must therefore state

Three lines, in the increment's own ledger entry:

1. which exported constants it moves or adds;
2. whether the port has a consumer for them (or "unknown — not enumerated");
3. whether it widens parity debt, and if so, that the debt is **recorded in the same commit** rather than
   discovered later.

**Rule proposed:** an increment must not add a *new* exported constant the port cannot consume without
recording that as parity debt in the same commit. This is the §8-gate-8 disclosure principle applied to the
port boundary instead of the goldens.

---

## §18 ID allocation — record, do not reserve

The PC lane's `references/id_reservations.yaml` state today is **`PC: next_free = 41`**, so implementation
would begin at `ED-PC-0041`.

**Corrected by the round-2 pass (Y3): this plan does NOT pre-allocate those IDs.** Reserving IDs for
increments that may never run is exactly the speculative allocation the reservations file exists to prevent,
and the file's protocol is *read `next_free`, allocate, bump, co-commit* **at the point of use**. The number
above is recorded as an observation so an implementer knows where to start, not as a claim on the range.

One ED per **increment**, not per finding. Any entry stating measured numbers needs `MEASURED-BY: <path>`
pointing at something that exists — blocking since ED-PC-0040.

---

## §19 X2 revisited — is the scene distribution derivable rather than invented?

§12.3 recorded X2: carry context makes balance depend on a **scene-frequency distribution that does not
exist**, so the frame could "prove" almost any weapon balanced by choosing the mix. Round 1 escalated that to
Jordan as unresolvable. Round 2 asked whether it is instead *derivable* from content the repo already has.

**Method:** the repo holds 55 generated arcs in `arcs/simulated/`. If arcs implied their scene types, the mix
could be counted rather than chosen.

**Result — negative, and worth recording so it is not retried naively.** A keyword sweep returns 24 total hits
across the whole corpus (17 court-ish, 6 battlefield, 1 tavern), which is already too thin to be a
distribution. **And the sweep is invalid on inspection:** every "court" hit is *legal or political* — "Crown
courts", "Church arbitration courts", "court-intrigue arc" — not a scene location. In a game whose strategic
layer is faction politics, that collision is systematic, not incidental.

**Conclusion, revising X2's disposition:**

- The *method* is right: derive the mix from content, do not invent it.
- The *content* cannot supply it today. Arcs do not carry scene-type tags, and no keyword proxy will
  substitute for one in this corpus.
- So X2 is **not a design decision Jordan must make in the abstract** — it is a **content deliverable**
  (tag scenes, or generate arcs with a scene field), after which the mix is *counted*.

That is a materially better disposition than round 1's "unresolvable, Jordan's call," and it converts an open
philosophical objection into a tractable work item. It does not remove the dependency — until the tagging
exists, §12.3's instrument must be run against an **explicit, declared** mix, and every result it produces
must be reported *as conditional on that mix*.

---

## §20 Round-2 adversarial pass

Attacking §17–§19. Same caveat as §16: **self-critique, weaker than a structurally independent audit.** (A
`fable`-tier independent audit of the physics, weapon data and logic was commissioned separately and is not
folded in here.)

| # | finding | disposition |
|---|---|---|
| **Y1** | §17 initially claimed the port "has no consumer" for these constants. **I had not checked.** | **Corrected in §17.2** to state what actually follows (1/27 module coverage) and to mark the per-constant enumeration as unverified GO-lane work. An unverified negative is the same defect class as an unverified positive. |
| **Y2** | §19's keyword evidence was **invalid** — "court" matches Crown/arbitration courts and court-intrigue, i.e. politics, not scene locations, and 24 hits is not a distribution regardless. | **Corrected in §19** before publication; the negative result is now the finding. Caught by asking what the string actually matched instead of trusting the count. |
| **Y3** | §18 originally pre-allocated `ED-PC-0041+` to increments that may never run — speculative allocation, exactly what the reservations protocol forbids. | **Corrected in §18**: record `next_free`, allocate at point of use. |
| **Y4** | My own first export probe read the wrong nesting level and reported "not exported" for all seven constants — a **false negative I nearly wrote into the plan**. | Caught and re-run before writing; §17.1's numbers are from the corrected probe (226 = 201 + 25). Recorded because the near-miss is the point: the first probe *looked* like a clean result. |
| **Y5** | §17's proposed rule ("do not add an unconsumable exported constant without recording debt") is unenforceable — nothing checks it. | **Accepted, not fixed.** It is a convention, and this repo's own meta-review says a convention is what failed three times. A real version is a GO-lane gate diffing the JSON against the port's consumed set; out of PC-lane scope, and named here rather than pretended away. |

**Rejected on inspection** (recorded so they are not re-raised): *"§17 means every increment is blocked on the
Godot port"* — no; the round-trip gate is satisfied by regenerating the export, and parity debt is disclosed,
not blocking. *"§19 kills carry context"* — no; it constrains how its results must be reported, which §12.3
already required.

---

## §21 Appendix A — The Final Fantasy Tactics lens

Jordan asked what an FFT-shaped game would look like on this engine. It is a useful lens because FFT is the
canonical **build-expressive tactical RPG**, and holding Valoria's measured state against it isolates exactly one
gap — and it is not the gap most people would guess.

### A.1 The inversion, stated first

| | Final Fantasy Tactics | Valoria today (measured) |
|---|---|---|
| what carries a build's identity | the **job + ability slots** | the **weapon**, at up to 47pp |
| what equipment contributes | meaningful but secondary | **dominant** — weapon 5.7→97.3%, armour up to +46pp |
| what the ability layer contributes | ~everything | **~0pp aggregate** (D6) |

**FFT and Valoria are currently mirror images.** In FFT a Knight and a Monk with the same equipment fight
completely differently; in Valoria a duellist, a binder, an armour-breaker and a reach specialist land within
2.2pp of each other and the weapon did all of it (D1). *Every* structural feature below is secondary to that one
inversion. An FFT-shaped Valoria is not a UI project — it is §9's P0/P2 with a front end.

### A.2 What already maps, one-to-one

More of FFT's architecture is already in this engine than one would expect:

| FFT | Valoria | status |
|---|---|---|
| **Job** (curriculum + what you may learn) | **Tradition** — gates *access* to a kit, contributes no efficacy itself | **built** (`_invested`'s access gate; measured inert-when-untaught at 47.7) |
| **JP spent to learn an ability** | **levels of investment** — `{name: level}`, `value**level`, level 0 inert | **built** (ED-PC-0024) |
| **Secondary ability set from another job** | **cross-training** — `known_traditions` unions the accessible kits | **built** (ED-PC-0028) |
| **CT / Speed turn order** | `ready[c] += rate × tempo_pressure`, act at `ACT_THRESHOLD` | **built** — and richer: cadence *proposes*, the Vor and the read *dispose* (ED-PC-0037) |
| **Reaction abilities** (Counter, Hamedo, Blade Grasp) | the counter node — `counter_select` → `counter_success_prob` → riposte, plus the Indes steal | **built.** Hamedo *is* the single-time counter; Blade Grasp *is* `ringen_am_schwert` on `edge_grab` |
| **Facing** (front/side/back) | `c.facing`, per-beat, stance × grip × weapon-class regime | **scaffolded, deliberately conservative** — `FACING_REGIME_K=0.12` pending the unresolved C1 polearm-direction call |
| **Equipment** | weapon + armour | **built** (and over-powered — D1/D2) |
| **Zodiac compatibility** | — | **deliberately absent.** An opaque hidden multiplier is precisely the fiat ED-PC-0023 retired. Do not add it. |

### A.3 What needs a translation, not a port

**Grid → measure.** FFT is tile-based; Valoria canon is explicitly *zone-based, no maps or grids*
(`combat_design_v1` three-mode framing). The tactical content of FFT's grid — positioning, reach, who can be
reached this turn — lives in Valoria on the **continuous `measure_gap` axis** and the approach/close/reopen loop.
That is a real translation, not a loss: I1 (MEASURE) and I5 (BIND-OR-BREAK) are the measure game made
player-facing. What genuinely does not survive is *terrain and elevation*, which FFT uses heavily and Valoria
has no representation for.

**"Hit 85% · Dmg 42" → a probability read-out.** The tactical genre's core loop is an *informed* choice, and
FFT shows you the odds before you commit. Valoria's resolution is continuous and emergent, with no per-weapon
table to display — but the distribution is computable in closed form, and `workbench/probabilities.py` already
does it (`net ~ Normal(µ·pool + soft_cap(net_sigma)·σ_n, σ_n)` banded by `core.degree`, validated against
Monte-Carlo to ±2pp). **The read-out layer exists; nothing consumes it.** This is the single cheapest
FFT-shaped feature available and it is nearly free.

**Per-turn command → the plan vector.** This is §3, and the fit is exact. FFT's loop is *one command per unit
per turn*; `wrapper.fight()`'s own contract is *"the GAME calls one engagement per turn."* The plan vector
(MEASURE · COMMITMENT · GUARD · COUNTER · BIND-OR-BREAK · CONTACT) **is** the FFT turn command, expressed as
intents over a continuous resolver rather than as a menu of discrete verbs.

### A.4 The one structural feature worth stealing outright

**FFT's slot architecture.** Its build system is not a bag of abilities — it is five *orthogonal* choices, each
drawn from a different pool: primary job, secondary ability set, reaction, support, movement. That is what makes
an FFT build feel *composed* rather than accumulated, and it is why two players with the same JP total build
different characters.

Valoria's `c.equipped` is a flat bag today. **But the native slot taxonomy already exists on paper:**
`phase4_5_plan_v1.md` §4b specifies **7 named phase-slots — Approach · Reading · Feint (dissolved into Commit) ·
Commit · Defence · Bind · Counter** — plus a point-buy affinity budget and the three co-equal access gates
(affordance ∧ mode-compatibility ∧ **learned**). It has been NOT STARTED since 2026-06-29.

The difference from FFT is instructive and in Valoria's favour: **FFT's slots are indexed by *when in the turn*
a thing fires; Valoria's are indexed by *where in the engagement* it acts** — and those phases are the
state-graph nodes the engine already resolves through. So the slot system is not an overlay; it is the
injection-point registry with a budget on it. Six of the seven phase-slots are exactly §3's six intents.

That correspondence is the strongest argument in this document that §3 and Phase 4b are the same design arriving
from two directions.

### A.5 What an FFT-shaped Valoria would additionally require

Named honestly, because none of it is small:

1. **Multi-combatant.** FFT is squad tactics; this engine is strictly 1v1. The envelope is designed
   (`scene_combat_design_v1.md`, wrap-never-fork) but **DESIGN-ONLY and gated on ED-911.** Without it there is
   no squad, and squad composition is half of what FFT builds are *for*.
2. **A progression structure.** FFT's job tree gates jobs behind JP spent in prerequisite jobs. Valoria has
   `MAX_INVESTMENT_LEVEL = 8` and an access gate, but **no economy at all** — ED-PC-0024 put the bounding layer
   explicitly out of engine scope, and skills are still literally uncapped (`skill()` is a bare `dict.get`).
   §6.3 proposes deriving that economy from measurement rather than authoring it.
3. **Enough authored content to fill the slots.** 8 abilities across 5 of 8 traditions will not populate a
   7-slot build system. FFT ships ~20 jobs × ~15 abilities. Valoria's source-tier discipline
   (`ability_armature` §5) makes that a *research* cost, not a writing cost — and correctly so: two traditions
   currently stay empty because no S1/S2 anchor exists, and `guardia`/`winden` were *removed* rather than kept
   as invented privilege (ED-PC-0026). **This is the honest tension between the FFT shape and this repo's
   grounding rules, and it is Q5 in §11.**
4. **Terrain / elevation**, if wanted — currently unrepresented at any layer.

### A.6 The warning FFT itself provides

FFT's best-known balance failures — a single job or unit that trivializes the game — are structurally identical
to **D1**. An FFT player looking at Valoria's weapon table would recognize the shape immediately: 26 of 53
options sitting in a 91–97% band against a baseline at 49.7 is not variety, it is one dominant option wearing
26 names, and eight options at ≤18% are traps.

So the FFT lens does not add a new work item. **It independently confirms §9's ordering**: fix the dominant
lever, then price the second, then author content into the slots, then hand the player the controls. Building
the front end first would produce a tactics game in which the tactics do not matter — which is precisely what
the ability layer already measured.

---

## §22 Appendix B — Carry context: the ORIGINAL sketch (now specified in §12)

**Jordan, 2026-07-26:** *"an aspect of resolution is that polearms/larger weapons were typically disallowed in
any public places during Renaissance. It was acceptable to have a smaller sword like a rapier, but not
acceptable to carry a spear."*

**This is a better answer to D1 than the one §9 P0 currently gives, and it changes that phase.** §9 P0 says
"weapon-identity compression" — flatten the 26-weapon 91–97% band. Under this frame, **the band mostly should
not be flattened.** The spear *should* beat the rapier in an open fight; that is correct physics and correct
history. The reason a rapier was worth owning is not that it beats a spear — it is that **you could carry a
rapier into a city, a court, a tavern, or a stairwell, and you could not carry a spear.** The spear wins the
fight you are never permitted to have.

### B.1 Why this is the C1 principle, not a new one

`combat_balancing_methodology.md` §5 already ratified the shape: *"You do not flatten asymmetric options to
sameness. Balance the unconditional mean flat and let context flip the conditional advantage — ratified C1: no
option globally best."* Its named precedent is **duel-vs-battlefield**: the war-hammer isn't duel-balanced, it
owns the armoured press, *and that is correct*.

Carry context is a **third axis of the same principle**, and a better-grounded one than either existing axis:

| axis | already in the engine? |
|---|---|
| armour tier (duel ↔ battlefield) | **yes** — the weapon × armour matrix |
| measure (approach ↔ bind) | **yes** — phase-dependent reach |
| **carry legality / social setting** | **no** — nothing represents it at any layer |

### B.2 The reframe, stated precisely

**The balance target changes from "every weapon wins ~50% against every other" to "every weapon is the best
*available* choice in some context, and the contexts occur often enough to make it worth owning."**

That is measurable and directly implementable: weight the existing matchup matrix by a **scene-context
distribution**, and require the *context-weighted* field to be level rather than the raw matchup table. That is
a new `balance.py` table, not new physics — and it is a far better balance target than a flat matrix, because a
flat matrix is the thing C1 explicitly forbids.

Illustrative contexts (the taxonomy is a design call, §11 Q8):

| context | what is carriable | who wins |
|---|---|---|
| **court / salon / indoors** | dress sword, dagger, concealed only | the rapier tier — and the concealed tier if weapons are *forbidden* |
| **city street** | civilian sidearm; polearms illegal, armour socially impossible | rapier, arming sword, sidesword, main gauche |
| **road / wilderness** | travel arms — spear and staff become respectable again | the reach tier |
| **battlefield / siege** | everything, plus harness | the armour-defeat tier; the whole reach band is legitimate here |
| **judicial duel / tournament** | negotiated, often symmetric by agreement | whoever trained for the agreed weapon |

### B.3 What this fixes that a nerf could not

- **It preserves the physics.** No per-weapon dial, no special case, no "the spear is too good so we reduce it."
  That is the §0/lens-6/lens-7 discipline the repo enforces everywhere else, and B8 in the defect register
  already proved the alternative fails: bringing off-plate reach to 0.75 is **not reachable by lever** without
  breaking `guisarme@heavy`. **Carry context resolves by frame what four levers could not resolve by tuning.**
- **It gives the bottom of the table its purpose back.** The ≤18% band (stiletto 17.3, misericorde 17.4, rondel
  12.0, dagger 11.7) is not a set of traps — those are the **concealed tier**, and in a scene where weapons are
  forbidden they are the *only* weapons. They already have a second context the engine does model: all four rise
  to 94–97% at plate. Two contexts, both correct, and neither visible in a duel table.
- **It supplies armour's missing cost (D2/C2) without inventing a fatigue model.** The reason plate is not free
  is not tempo — it is that **you cannot wear harness to a dinner, into a city, or up a stairwell**, it needs a
  servant to don, and wearing it is itself an accusation. That is a much better-grounded cost than a mobility
  penalty, and the engine needs no new physics for it. **Caveat, stated because it is load-bearing:** access
  gates the *distribution* of encounters but does not price the choice *within* a context where armour is
  allowed — on a battlefield "wear plate vs not" is still 95.7 / 4.3. So some wearer-side cost is probably still
  needed; carry context does most of the work, not all of it.
- **It makes `cinquedea` explicable.** Defect-register A1 calls it the worst weapon in the roster with no
  context anywhere — 4.5–6.5% at every tier it can act in. But historically the cinquedea *was* a civilian
  status/dress weapon, not an armour tool. Under carry context it is a weapon for the setting where its rivals
  are illegal, and its physics can stay exactly as they are. **A1 is the cheapest test of whether this frame is
  right.**

### B.4 What it would cost to build

1. **A scene-context primitive** — which the engine does not have, and which is *not* PC-lane-local: it touches
   the settlement/faction layers (law and order state), the fieldwork/scene layer, and the strategic layer.
   Cross-lane, so an IN-lane or Jordan-level decision, not a PC-lane one.
2. **A carriability property per weapon** — and this must be **derived, not hand-set per weapon**, or it is the
   name-keyed table the repo forbids. The honest derivation is over primitives already in the records: overall
   length, whether it is concealable, whether it is two-handed, whether it reads as a weapon of war. That is a
   real derivation problem, not a data-entry one.
3. **Historical grounding at the usual source tiers.** Renaissance and early-modern arms restrictions are well
   attested in principle — the arms-of-peace vs arms-of-war distinction, city statutes on weapon carry, and
   Silver's *Paradoxes of Defence* being in large part a polemic **against** the rapier's civilian adoption over
   the English short sword. But **I have not verified specific statutes**, and under `ability_armature` §5's
   rule the specific claims need S1/S2 anchoring before any of them is encoded. Do not let me author a carry
   table from general impressions.
4. **A context-weighted balance table** in `balance.py` — cheap, and the piece that makes the whole frame
   *measurable* rather than merely appealing.

### B.5 Revised §9 P0

| was | becomes |
|---|---|
| **P0** D1 — weapon-identity *compression* | **P0a** — build the carry-context frame and re-measure the field **context-weighted**. Compress only what is *still* dominant inside its own context. |
| **P0** D2 — price armour (mechanically) | **P0b** — price armour primarily by **access**, and measure whether a within-context cost is still needed. |

The rest of §9's ordering is unchanged, and the blocking claim is unchanged: **a modulation layer built before
the dominant lever is resolved will measure as inert.** Carry context is a different — and better — way of
resolving the dominant lever, not a way of skipping that step.

---

## §23 Provenance

Built on, and consistent with: `state_graph.py` (`INJECTION_POINTS`, 9 points, tested) · `tradition_decomposition_v1.md` (per-tradition technique → primitive → node → gate, S-tiered) · `ability_armature.md` (§1 principles, §5 source menu, the sparse-tradition rule) · `phase4_5_plan_v1.md` (Phase 4b abilities-as-access, the 7 review lenses, the Primitive / Tradition-is-not-a-weight / Attack–Defence Convergence principles) · `engagement_psychology_recovered.md` (§B1 "biased weights, not a planner") · `combat_throughlines_v1.md` (the two poles; commitment = recovery) · `combat_balancing_methodology.md` (§5 C1, §6 the ablation gate) · Jordan's fiat-audit ruling (`audit/2026-07-23-combat-fiat-audit/fiat_audit_v1.md`: efficacy from investment, not membership; every build available; no fiat) · ED-PC-0023/0024/0028/0030/0034/0040 · and the measured state in `audit/2026-07-26-combat-balance-customization-state/`.

**Nothing in this document has been implemented, measured, or ratified.** The magnitudes in §6.4 are proposals to be calibrated against §6.2's bands, not findings. The one measured input is the balance-state report, whose own instruments and noise floors are stated there.
