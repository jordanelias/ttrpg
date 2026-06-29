# Combat Traditions — Adversarial NERS Critique & Distillation
**2026-06-25 · subject: `combat_traditions_integration_spec.md` (this session's prior artifact) · lens: NERS, adversarial, goal = refine + distil · terms Englished throughout**

`[SELF-AUTHORED — bias risk: this attacks an integration spec I wrote an hour ago, and in doing so it also takes a chunk out of the morphology critique I wrote before that. The criticism an independent reviewer would press — that I over-built, and that my original "three missing axes" finding overstated the gap — is the criticism I am incentivised to dodge. Both are made below, in the verdict.]`

**Verdict (first line, no false balance): the over-granularity suspicion is correct, and it reaches further than suspected.** Of the integration spec's two lever-families (≈11 new levers + a dispatcher + 3 new states), **two levers survive a NERS pass — smother and choke — and they are really one capability: the clinch.** Everything else either duplicates machinery the engine already has (the counter/steal axis, the dodge mode, the poise-break and concentration-drain that fire on every hit) or is a dial on an existing quantity dressed up as a new axis. Two of my own artifacts take damage: **the integration spec over-builds (fails NERS-N and NERS-E on most levers), and the original critique's "three missing efficacy-bearing axes" overstated the gap** — the engine already expresses most of force-relation and targeting; what it genuinely lacks is narrow.

---

## §0 — The foreign terms, in English (the glossary, used from here on)

| Term (original) | Lang | English used in this doc |
|---|---|---|
| **Vor** | Ger | **the lead** (holding initiative) |
| **Nach** | Ger | **the follow** (responding / a beat behind) |
| **Indes** | Ger | **in-the-instant** — the counter struck in the *same* tempo |
| **Vorschlag** | Ger | **the opening strike** (the first blow that takes the lead) |
| **Stärke / Schwäche** | Ger | **strong / weak of the blade** (strong near the hilt, weak near the tip) |
| **Winden** | Ger | **winding** (pivoting the blade in the bind) |
| **Fühlen** | Ger | **feeling** (sensing pressure through the bind) |
| **Ringen am Schwert** | Ger | **grappling at the sword** |
| **Nachreisen** | Ger | **pursuit** (striking into the recovery) |
| **Mezzo tempo / contratempo** | It | **half-time counter** / **counter-in-tempo** |
| **Misura** | It | **measure** (distance management) |
| **Stringere** | It | **blade-constraint** (closing the line) |
| **Sen** (sen-sen-no-sen / sen-no-sen / go-no-sen) | Jp | **initiative-timing**: pre-emptive / simultaneous-seize / responding-counter |
| **Maai** | Jp | **fighting distance** (the interval) |
| **Seme** | Jp | **pressure** (applied to freeze the opponent) |
| **Kuzushi** | Jp | **balance-break** (off-balancing) |
| **Zanshin** | Jp | **continuing awareness** (follow-through) |
| **Atajo** | Sp | **blade-constraint** (off the circle) |
| **Compás** | Sp | **geometric footwork** |
| **Fa jin** | Zh | **explosive power-issue** |
| **Ting jin** | Zh | **pressure-sensing** (listening) |
| **Song / Lü** | Zh | **yielding-softness** / **rollback** |
| **True / false times** | Eng (Silver) | **sound / unsound timing** (hand-before-body-before-foot) |

Recommendation: the in-code ability *keys* (`indes`, `vorschlag`, `sen_no_sen`, `mezzo_tempo`, `staerke_schwaeche`, `misura`, `atajo`) and the `desc` strings can be Englished in a cleanup pass (`the_instant`, `opening_strike`, `simultaneous_seize`, `half_time_counter`, `strong_weak`, `measure_control`, `blade_constraint`) — optional, low-priority, and a pure rename. The *concepts* are translated above; this doc uses English.

---

## §1 — The failure surface (lever by lever, worst-first)

The NERS-N test for any lever: **does it catch a distinction nothing else catches, that the player can feel?** The NERS-E test: **can the player intuit the choice?** Against those, most of the families fall.

### The force-relation family ("power applied by means other than strength" — the user's prime suspect)

| Lever | Verdict | Why |
|---|---|---|
| **redirect** (turn a defence into a counter-steal) | **CUT** | Pure duplicate. The engine *already* steals the lead when a defender out-reads a committed attacker (the in-the-instant steal, `wrapper.py:147–158`) and *already* has the half-time-counter and simultaneous-seize abilities. "Turn defence into offence" is the counter/steal axis, built. And the morphology rates this force-relation the *least* efficacy-faithful (it fails when trained cooperatively). Adding a lever for the weakest, already-covered case is taxonomic elaboration of exactly the kind the morphology warns against. |
| **evade** (a tradition that voids) | **CUT** | The `dodge` mode already exists (`systems.py:100–101`) and is already selected when the read and the weapon favour it. `evade` is "dodge more" — mode-selection bias, which disposition/read already drive. A lever that says *dodge more often* is overhead, not a capability. |
| **absorb** (yield to bleed a blow) | **CUT (with a flagged cost)** | Folds into machinery present twice over: Endurance already absorbs damage inside `apply_wound`, and poise already recovers each beat. "Takes hits well by yielding" is, to the *player*, indistinguishable from "has high Endurance." **The cost of cutting, stated honestly:** the morphology rates yielding-absorption efficacy-faithful in *reality* — but reality-fidelity is not the NERS-E criterion, which is player-facing. We surrender a real-world distinction the player cannot feel, in exchange for elegance. Recorded, not hidden. |
| **smother** (deny the commit-window in the clinch) | **SURVIVES** | The one force-relation lever that catches something nothing else does. The engine has measure (distance) and tempo (cadence) but **no "actively jam the opponent's ability to generate force."** It is efficacy-core (the clinch holds up under full resistance — the morphology's convergent finding), and it is intuitable ("this fighter smothers you"). It is also the natural setup for the choke. |
| F1 opposition / F2 deflection | already present | leverage + strong-weak + parry/wind. No lever needed; the critique already credited this. |

**Four levers proposed; one survives.** The user's suspicion is confirmed and sharpened: the force-relation taxonomy is over-granular because the engine *already* expresses most of it (leverage, the counter/steal axis, the dodge mode), and the genuinely-missing piece is singular — the clinch.

### The targeting family (the user named it a legitimate axis — but the same disease is milder-present here)

| Lever(s) | Verdict | Why |
|---|---|---|
| **target_poise (T1 mass)** + **target_uproot (T5 base)** | **MERGE → fold** | These are the *same dial*: both amplify the poise-break that *already fires on every hit* (`wrapper.py:231`). Two levers for one effect. And it is a dial on an existing quantity, not a new effect. |
| **target_psych (T7)** | **fold** | Amplifies the concentration-drain that *already fires on every hit* (`wrapper.py:227`). A dial. |
| **target_vital (T3 kernel)** | **fold** | "More damage, capped." A dial on damage. |
| **target_hamper (T2 joints)** + **target_defang (T6 limb-first)** | **MERGE → defer** | These *are* one genuinely-new effect (a persistent handling/reach debuff = crippling). It is real and not currently expressible — but it is second-order, and like power-source it risks over-engineering. **Defer** unless a felt need appears (the FMA attribution is itself under-anchored). |
| **target_choke (T4)** | **SURVIVES** | The one new *effect*, not a dial: incapacitation without a wound, advancing only in the clinch. The convergent combat core. Pairs with smother. |

**Seven levers + a dispatcher proposed; one effect survives (choke), one merges-and-defers (cripple), the rest are dials on quantities the engine already moves.** The dispatcher (`hit_effects`) was built to route seven targets; routing two (choke + deferred cripple) needs no dispatcher — two guarded lines do it.

---

## §2 — NERS verdict on the integration spec as written

```
SYSTEM: integration spec (force-relation + targeting lever families)
COMPONENTS: dice (resolution) + clock (the proposed choke clock) + deterministic (the consequence dials)
VERDICT: NON-COMPLIANT as written — over-granular; fails N and E, gives false R.

N (necessary): FAIL. redirect, evade, absorb, target_poise, target_uproot, target_psych,
   target_vital are each removable without worsening play — existing machinery (counter/steal,
   dodge, Endurance+poise, poise-break, conc-drain, damage) already carries them. Necessary
   survivors: smother, choke (and a single deferred cripple).
R (robust): FALSE-PASS → FAIL. The eleven levers look like depth but most are choices the player
   cannot distinguish in outcome; indistinguishable choices are not strategic depth, they are
   surface. More levers also = more invariant-suite surface and more mis-tune risk. The distilled
   set is MORE robust (fewer, real, separable choices).
S (smooth): PARTIAL. The dispatcher integrates, but every added lever is another category boundary
   ("which dial does what"); distillation removes the friction.
E (elegant): FAIL. The player cannot intuit "absorb vs redirect vs evade" or seven targeting logics
   as distinct simple choices. "This tradition closes, smothers, and chokes" they can.

REMEDIATION: distil to the clinch (§3). Keep strength + leverage (existing). Add smother + choke as
   ONE capability. Fold absorb→Endurance, redirect→counter/steal, evade→dodge, the targeting dials→
   the existing per-hit quantities. Defer cripple like power-source.
```

---

## §3 — The distillation (the refined minimal set)

**The reframe (folded in 2026-06-25): the primary contest is the *regime*, not the exchange.** Before two fighters trade, they fight over *which kind of fight it will be* — each is trying to drag the bout onto its own ideal terms. Read this as a small **bias-space** with three axes: **measure** (far ↔ close), **contact** (seek-the-bind ↔ refuse-contact), **tempo** (press ↔ counter). Each fighter is a **bias-point** set by weapon × tradition — the rapier at *far / no-contact / counter*; the longsword-grappler at *close / bind / press* — and the bout is two vectors dragging the state toward two regions. "Fighting on your terms" is imposing your region on the opponent. This is the unifying object behind the modes the prior turn asked about: a defence-mode and a commit-depth are both just *means of pulling the state one way*; the bias is the thing, not a parallel menu of attack-modes (the attack mode is largely weapon-fixed already — the head type **is** the attack mode: a rapier thrusts, a poleaxe percusses).

**Two of the three axes the engine already has.** **Measure** is emergent and agentive on both sides — reach + the approach/reopen system *is* the distance contest (`wrapper.py:66–85, 217–226`): the long weapon actively re-makes distance, the short one actively closes (`close_rate` + `approach_displace`). **Tempo** is biased by the channel-weights + disposition. **Only the contact axis has a missing pole.** The engine can force the bind (and `clinch`, below, lets a fighter *drive* it) — but a fighter has **no way to refuse contact once caught**. That is exactly the rapierist's problem: dragged into the bind, the bind runs three iterations on leverage + feeling, the rapier has low leverage (long head, short grip) and winds at 0.4, so it loses — with no move to slip out. The armature already flagged this gap as the unbuilt `disengage`/reopen lever.

**Keep what exists, add the contact-axis pair (+ its finish).** Tradition differentiation, after distillation, runs on:
1. the **7 channel-weights** (visual / tactile / pre-commit / leverage / tempo / measure / balance) — live via `eff_cw`;
2. the **8 existing abilities** (opening-strike, the-instant counter, strong-weak, half-time counter, simultaneous-seize, sound-timing, measure ×2);
3. **familiarity** (reading an unfamiliar style worse);
4. **+ the contact-axis pair** — *force the fight in* vs *keep it out* — plus the clinch's finish:

| New lever | Op | Engine site | What it is | Grounding |
|---|---|---|---|---|
| **`clinch`** (was smother) | `*` | `[MODIFY @ wrapper.py:140]` atk_sig, as `SMOTHER_COMMIT_K*(factor−1.0)` so unequipped = exactly 0 | the **force-it-in** pole: deny the aggressor's commit-window in the close, dragging the bout into grappling range | bottom-up: closed tempo/commit; top-down: wrestling clinch / Muay Thai plum / grappling at the sword (German *Ringen* — S2-anchored) |
| **`disengage`** | `*` | `[INSERT @ wrapper.py:243–252]` bind loop — an escape check before the iterations, reusing the reopen reset (`closed=False`) | the **keep-it-out** pole: slip the bind and reset to measure (the *cavazione* / change-through), keyed to a measure/point profile + leverage *dis*advantage (the weak-in-the-bind fighter buys distance back) | bottom-up: the bind loop + the existing reopen reset; top-down: rapier *cavazione*, the change-through (*Durchwechseln*), MMA framing-out / standing up |
| **`choke`** | `+` | `[INSERT @ wrapper.py:243–252]` bind loop, clinch-only | the clinch's **finish**: an incapacitation clock; at threshold, felled without a wound | bottom-up: the bind loop + a new `choke_clock` state; top-down: the convergent-core choke |

**Why this is the right pair, not a parallel mode-menu.** `clinch` and `disengage` are the two poles of the *same* contact axis: the longsword's clinch forces the rapierist into the bind; the rapierist's disengage refuses it; whoever wins fights on their terms. Symmetric, each weapon × tradition-keyed, and it closes the "fight on your terms" loop on the one axis the engine lacked — without a second taxonomy of attack-modes.

**Footprint, before vs after:**

| | Integration spec (as written) | Distilled |
|---|---|---|
| new levers | ≈11 | **3** (clinch, disengage, choke) |
| new pure functions | 1 (`hit_effects` dispatcher) | **0** (guarded checks in the bind loop; disengage reuses the reopen reset) |
| new per-fighter states | 3 (`choke_clock`, `hampered`, `limb_dmg`) | **1** (`choke_clock`) |
| new CFG constants | 11 | **4** (`SMOTHER_COMMIT_K`, `CHOKE_CLOCK_RATE`, `CHOKE_CLOCK_THRESHOLD`, `DISENGAGE_K`) |
| MODIFY/INSERT sites | 14 | **3** (atk_sig; the bind-loop escape + choke checks) |

**Deferred-optional (one item, not a family):** `cripple` (the merged T2+T6 handling/reach debuff) — a single new state + one lever, built *only* if a felt limb-targeting distinction is demanded in play. Same disposition as power-source: flag the gap, do not build on spec.

**Folded, not built (and where each already lives):** redirect → the in-the-instant steal + counter abilities (`wrapper.py:147–189`); evade → the dodge mode (`systems.py:100`); absorb → Endurance-absorb in `apply_wound` + poise recovery; the poise/morale/damage targeting dials → the poise-break / concentration-drain / damage the engine *already* applies on every hit. If a tradition is wanted to lean on one of those existing quantities, that is at most a single scalar modifier on that quantity — never a targeting taxonomy.

---

## §4 — Re-test the distillation (does the cut re-create the problem it was meant to fix?)

The risk in distilling: re-opening the J-33 "traditions don't differentiate" gap the original critique was built to close. **Re-tested: it does not.** After distillation a tradition is still a point across 7 live channel-weights + up to 8 equipped abilities + a familiarity profile + (optionally) the contact-axis pair (clinch ↔ disengage) + choke — that is a large, separable space, now with an explicit regime axis. What the distillation removes is *redundant* levers (choices the player could not tell apart), not differentiation.

And it removes them *toward* the morphology's own priority, not away from it: the morphology's central efficacy claim is the **convergent core — range-control via the clinch, dominant position, the choke.** The distilled set keeps exactly that (clinch + choke) and adds the missing *defensive* pole of the same range contest (disengage), while dropping the granular periphery (the absorb/redirect/evade sub-taxonomy). So the refined version is **more** faithful to what the morphology says matters, with **less** apparatus — the NERS win. And the contact-axis pair *adds* a separable strategic axis (which regime the bout occupies) rather than another indistinguishable lever — the opposite of the over-granularity that got cut.

**The line to hold (tendency, not planner).** The whole reframe is "expressions of bias in vectorised space for tendencies" — so the mechanic must stay a *weighted tendency*, never a planner. A fighter that *plans* its way to a preferred regime is an AI subsystem: over-engineered, unintuitable, and an invariant-suite hazard. A fighter that merely carries *biased weights* (its `clinch`/`disengage` factors, its commit-skew, its measure channel) that tilt the existing machinery toward its region is cheap, no-op when unequipped, and exactly the intended object. Keep regime-imposition emergent from biased weights over the systems already in `engagement()`; do not add a regime-selection planner. Most of the reframe is therefore *naming* what the physics already does (the measure contest), not new code — the genuine addition stays the three contact-axis levers.

**One recorded loss (the honest trade):** the force-relation sub-distinctions below the clinch (the yielding/redirecting fighter as a *mechanically* distinct thing) are surrendered. They are efficacy-faithful in reality and not felt in a videogame; the cut buys elegance at the price of reality-fidelity on an axis the player cannot perceive. Recorded as a deliberate `[OPEN TRADE-OFF — design]`, not a silent deletion.

---

## §5 — Honesty block

- `[CONFIDENCE: high]` on the NERS-N/E failures and the fold-targets — each "this already exists" is anchored to a line read first-hand this session (`wrapper.py`, `systems.py`, `core.py`). `[CONFIDENCE: medium]` on the precise boundary of the cut: a reasonable designer could keep `absorb` as a genuinely-distinct active-mitigation mechanic (distinct from passive Endurance) if play shows the difference is felt — that is the one cut I am least certain of, flagged.
- `[CORRECTION: the morphology critique's §0/§4 "three missing efficacy-bearing axes (force-relation, targeting, power-source)" overstated the gap. Reading the engine for *this* critique shows the engine already expresses most of force-relation (leverage, counter/steal, dodge) and most of targeting (poise-break, conc-drain, damage on every hit). The genuinely-missing set is narrow: the clinch (smother + choke), and an optional cripple. The original framing inflated the failure surface.]` Self-authored revision.
- **No false balance, and no manufactured cut:** the clinch (smother + choke) is *not* cut — it survives because it catches a real, felt, efficacy-core distinction nothing else does. Cutting it to look decisive would be the inverse error. It stays.
- `[GAP: no sims run — the claim "the player cannot distinguish these levers" is a design judgment from the mechanics, not a play-tested result; a discrimination test (can a player tell absorb from high-Endurance blind?) would confirm it.]` · `[GAP: combatant.py still not read in full — the `choke_clock` field/reset surface inferred.]`
- **Not committed as canon.** This refines (and partially supersedes) `combat_traditions_integration_spec.md` §2–§4: treat the distilled §3 here (now the contact-axis pair + choke) as the live recommendation, the spec's full lever-families as the superseded maximal version. A **session checkpoint** was written to `canon/session_checkpoint.md` recording this arc; the deliverables themselves are *not* yet landed under `designs/audit/2026-06-25-combat-traditions-morphology/` — that remains a `safe_commit` + `Citations:` pass on your go. Not done unprompted.
