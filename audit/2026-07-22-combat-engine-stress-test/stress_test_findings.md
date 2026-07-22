# Combat-engine stress test — findings (2026-07-22)

**Lane:** PC (personal combat) · **Target:** `systems/combat/combat_engine_v1/` (CANONICAL head per `CURRENT.md`)
**Instruments (committed beside this report, reproducible):**
`stress_battery.py` (mechanical correctness) · `grounding_battery.py` (HEMA/physics/treatise grounding).
**Method framing (per Jordan, this session):** *weapons are not equal and armour is not equal.* Flat balance is
**not** the target (methodology §5, ratified **C1: no option globally best**). The target is that primitives,
formulae, mechanics and **emergent play** feel real and justified against treatises / manuals / HEMA / physics.
So this report separates **mechanical correctness** (must hold regardless of balance) from **grounding**
(does emergent play match the historical/physical source), and it reports grounding as MATCH / DIVERGE, not
pass/fail.

Baseline health at session start: `pytest tests/valoria` = **447 passed / 9 failed**, where the 9 are the
already-tracked "accepted-red" grounding-frontier tests (SPEAR flat-dominance, `test_gap_game_poleaxe_spikes_
plate` [PHASE-C], heft-ordering, 4 numpy element-parity). Nothing here was introduced by this audit — it is
read-only.

---

## TL;DR

- **Mechanical correctness is excellent.** 24-check battery: **all green except one** latent numerical-robustness
  gap (an unguarded logistic that `OverflowError`s only under attribute values ~100× outside the 1–8 gameplay
  range). Determinism, mirror-symmetry, damage/degree/resolve finiteness, win-rate monotonicity in every "good"
  attribute, the 95% upset cap, and bounded runtime all hold across the full 51-weapon × 4-armour × 8-tradition
  space.
- **Grounding is genuinely strong at the physics layer.** 20 falsifiable HEMA/physics assertions: **19 MATCH**,
  1 DIVERGE (the *known* PHASE-C poleaxe-spike item). The armour-arc physics is textbook: the thrust-daggers
  invert (useless unarmoured → decisive vs plate), pure cutters collapse vs plate, percussion & gap-thrust
  transmit, half-swording engages vs harness. **Tradition balance is exemplary** — 2.9pp unconditional spread
  and **5 distinct context-leaders across 5 weapon contexts** (perfect C1).
- **The interesting grounding divergences are emergent, and two look under-appreciated:**
  1. an **arbitrary vs-plate cliff among near-identical cutting polearms** (guandao 96% vs bardiche 9.6%),
     driven by *which weapons got an anti-armour affordance authored*, not by physics;
  2. a **non-monotone "mail valley"** where the half-sword weapons do *worse* against medium (mail) than
     against heavier plate — backwards from "mail is easier to defeat than plate."
  Plus the two already-tracked items (reach-class flat-dominance; poleaxe PHASE-C) which this run corroborates
  with fresh scope.

---

## Adversarial revision (2026-07-22, same day — supersedes the affected items below)

A second, adversarial pass (`adversarial_pass.py`; corpus cross-check via the combat audits/handoffs/ledger)
turned the skepticism on this report's own claims. Three material corrections:

- **G2 was mis-diagnosed — and the real finding is bigger. The half-sword auto-switch is a NET LIABILITY.**
  My "mail valley / medium-tier coupling discontinuity" was wrong: the coupling tables are perfectly monotone
  for every weapon (longsword none/light/med/heavy = 1.45/1.28/**1.02/1.02** — no dip). The win-rate dip is
  real but its cause is the **half-sword form-switch itself**. Ablating it (weapon never half-swords):
  longsword vs arming at mail/plate **27→62 (+35pp) / 41→73 (+32pp)**; estoc **70→94 / 79→96**. The ablated
  arcs are clean and monotone-rising. So `halfsword_target` — the mechanic that implements "mit dem kurzen
  Schwert" to help vs harness — makes the fighter *worse*. **Mechanism:** the full longsword's *versatile*
  `cut_thrust` head already gets ~90% of the gap-thrust for free (adef_cap 0.94 vs the half-sword's 1.02;
  coupling 1.02 vs 1.11) **without** losing reach, while the half-sword form has ~**3× the leverage**
  (leverage-proxy 0.29→0.90) that `adef_cap(point)=ADEF_POINT·gap` **never reads** — it credits point
  concentration only, not the weight-bearing leveraged thrust. So the switch pays a large reach cost (−0.44)
  for a tiny anti-armour gain. **This is backwards from the source** (Jordan, this session: half-swording with
  high-pressure weight-bearing thrusts *is* the answer to penetrating armour; edged weapons should struggle to
  cut mail — the engine gets the cut-vs-mail half right, the half-sword half wrong). A **prototype** crediting
  leverage into the gap-thrust adef (emergent, no weapon name) moves the arc the right way (longsword vs plate
  44→64 at K=0.8), but it lifts *every* thrust weapon and so needs a roster-wide joint re-tune — a validated
  *direction*, not a finished fix. **This B.1 "half-swording engages vs harness" strength claim below is
  RETRACTED; G2 below is superseded by this item.** Corpus: an earlier hand-audit flagged the half-sword
  under-credited vs plate (2026-06-29 recovery, F3) and a damage-path fix (`d3661936`) lifted its *damage*;
  the *switch decision* was never re-checked and is still a net loss — this is the novel part.
- **The C1 "5 distinct context-leaders" claim (B.1) was a low-N artifact — RETRACTED.** At N=120 the per-context
  leaders sat within ~2pp of each other (noise). Re-run at N=400: only **3** distinct leaders, margins
  0.2–0.6pp — i.e. the leader is effectively random per context. The **2.9pp unconditional field spread is the
  real, solid C1 result** (no globally dominant tradition); the "leader flips across every context" gloss is not
  supported. (Historically the handoff recorded only ~2 distinct leaders, so the unconditional flatness *is* a
  genuine improvement — just not via a robust per-context flip.)
- **Agility-dominance SURVIVED falsification (strengthened).** Re-measured from an all-4 baseline: agi
  **+34.4pp**, still the clear leader by ~17pp over cog — not a baseline artifact.

Unchanged by the adversarial pass: M1 (overflow), G1 (cutting-polearm cliff — confirmed **novel**, ED-PC-0011/12
adjacent), G3/G4 (confirmed **known**, deferred to Phase-C), and the physics-layer MATCH set (the point-superiority
check even survived a cherry-pick test: every real weapon's own `gap_prec` still out-couples a cut vs plate).

### Fix investigation (half-sword) — a rigorous negative result: NOT independently fixable

Following Jordan's ruling, I tried to make half-swording the armour-penetration answer it should be. Three
attempts, all validated against **switch-benefit** (live-with-switch vs the same-config no-switch ablation)
AND the **arming mirror = 50** fairness invariant. None succeeded, and the failures triangulate the root cause:

| attempt | idea | result |
|---|---|---|
| 1. leverage → adef | credit the half-sword's ~3× leverage into `adef_cap` (point/cut_thrust) | **fails** — helps the full form too; switch stays −26/−14pp even at large K |
| 2. full form bounces | standing `cut_thrust` gets no gap-thrust adef vs armour (only the half-sword `point` does) | switch flips **+25/+10pp** and the longsword arc becomes 44/44/84/94 — BUT the **arming mirror at plate collapses to 0%** (arming has no half-sword form → helpless vs plate → degenerate), and everything inflates against the crippled baseline (mace 20→97) |
| 3. partial factor | scale the standing gap-thrust adef by `f∈{0.6,0.4,0.2}` (middle ground) | at **no** `f` does the switch become beneficial at the **mail (medium)** tier (−36/−25/−25/−11); pushing `f` low enough to help at plate starts drifting the arming mirror off 50 (47→56) |

**Conclusion: the half-sword liability is a symptom of the reach-over-weighting (Phase-C / G4) debt, not an
independent bug.** The reach given up by half-swording is worth more than any armour-defeat bonus `adef_cap`
can return — because **reach keeps dominating even in the close** (`reach_sigma` applies in the closed exchange
and the longer weapon can re-open distance). At grappling range the half-sword's control/leverage *should*
dominate reach; it doesn't. So the real fix is the **joint** Phase-C recalibration — suppress reach's grip in
the close **and** credit the leveraged weight-bearing thrust, together — not any single `adef`/`coupling` knob.
This is the methodology's own "multi-parameter joint optimization, not single-knob" (§4). **No engine change
was committed** (all three attempts were in-process only); the working tree stays clean. Reproducible in
`adversarial_pass.py` (§6 fix-investigation).

---

## Phase-C investigation (2026-07-22) — the recalibration is a THREE-lever joint problem

Following "Phase C", I traced the reach-class dominance + half-sword liability to their actual drivers
(`phasec_probe.py`). Result: **not one knob — three coupled levers, each with a cross-constraint that a naive
fix trips.** I confirmed each empirically and committed **no** engine change (all deep-copied CFG / monkeypatch).

- **Lever 1 — reach-class dominance is the APPROACH stop-hit, and the "reach class" is HETEROGENEOUS.**
  Full ablation (`STOPHIT_CHANCE=0`) collapses **spear 93→38 / yari 91→45** at plate — the stop-hit is their
  whole game. **But `poleaxe` barely moves (91→88)** and guandao only 96→56 — poleaxe's dominance is *not*
  the stop-hit at all; it is its own mass/percussion/adef (plausibly grounded — a poleaxe *should* win the
  armoured press). So Phase C must **not lump the reach class**: the stop-hit lever targets spear/yari, not
  poleaxe. **Cross-constraint (confirmed):** the stop-hit also carries the *grounded* unarmoured reach
  (spear-vs-arming at *none* 80→19 at `STOPHIT=0`), so it can't be globally cut — it must be
  **armour-conditional** (compress the approach threat as the *closer's* armour rises; an armoured man walks
  through a spear).
- **Lever 2 — the half-sword liability is SEPARATE.** The stop-hit fix leaves the half-sword switch-benefit
  negative (−27 → −29). The half-sword fights *in the close*; its loss is reach-volume there (surrendering the
  reach that throttles the opponent's attack count — traced: half-swording gives the arming sword +36% more
  attacking beats), not the approach stop-hit. It needs its own close-range lever (reach must decay hard once
  genuinely closed, so the leveraged half-sword thrust can win at grappling range).
- **Lever 3 — heft-ordering is a FORWARD-BALANCE / normalization effect [CORRECTED — my first read was wrong].**
  I initially claimed the spear's ~1.6 kg shaft was *unmodelled*; the adversarial pass falsified that. The spear
  **is** fully mass-modelled — `_all_parts` = head 0.4 kg @ 1.51 m **+ haft 1.354 kg @ 0.645 m + butt 0.25 kg**,
  summing to the full 2.0 kg (my earlier probe printed only `elements` and missed the `haft` field; adding a
  shaft *element* would in fact double-count and corrupt `m_head`, which sums `elements`). The real cause:
  `heft = m_head × PoB_frac`, and the spear's **PoB_frac 0.34 is ~3× the swords' ~0.12** because
  `PoB_frac = PoB/(head_len+grip_len)` reads the long spear as strongly forward-balanced. So the fix is the
  **PoB_frac normalization / haft-position calibration (a formula question)**, not "add missing mass" — and it
  is **decoupled from reach-dominance** (mass doesn't move `reach_base`, which is geometry). Harder and more
  design-laden than a data patch.

**The blocker is a design call, not code:** Levers 1 & 2 need **target win-rate bands** — e.g. *should a spear
beat an arming sword when both are in full plate, and by how much?* (Historically a spear/pike vs a harnessed
swordsman is genuinely strong — pike squares — so the answer may be "yes, but not 93%.") I can't invent those
targets; they set where each lever lands. Once the bands are fixed I can implement all three, joint-tune, and
validate (matrices + `pytest` + re-export). Run `python phasec_probe.py` to reproduce.

## Primitives & emergence adversarial pass (2026-07-22) — `primitives_probe.py`

Hammering the L0 primitive-law (behaviour *emerges* from geometry primitives; no weapon-name tables):

- **Finding P1 [CORRECTED — NOT novel; this is RATIFIED-BUT-UNIMPLEMENTED design] — half-sword capability is a
  2-name fiat list + a dead primitive.** The current code decides who can half-sword by a hardcoded data table
  `HALFSWORD_FORM = {longsword, estoc}` (a name-table in the data layer, so the
  `test_no_weapon_name_literal_in_resolution` guard doesn't catch it), and `geometry.can_halfsword_thrust →
  geo['halfsword']` is a **dead** coefficient (`bake()` computes it; nothing reads it). **All of this was already
  diagnosed and a fix ratified** — the 2026-07-04 morphology-granularity **audit G3** ("a name-keyed behaviour
  whitelist — the exact shape the primitive-law forbids… `can_halfsword_thrust` exists but only gates, never
  grants") and **plan P3 / consolidation JD-3**: add `elements[].grippable = True` (the **ricasso** / attested
  safe forward grip), make `affords_halfsword(w) = (∃ grippable forward element) ∧ can_halfsword_thrust(cv, pc)`,
  **retire `HALFSWORD_FORM`/`HALFSWORD_BASE` as behaviour gates**, landing **byte-identical at {longsword, estoc}**
  on the un-extended roster, with any roster expansion (flamberge's/greatsword's attested ricassos) a **loud
  Jordan decision (JD-3)**. **Status: ratified plan-of-record, never wired into code.** So this is not an
  emergence *gap* — it is **implementation debt on a ratified design**, and my earlier "novel" framing was a
  search failure (I did not check the audit corpus before claiming novelty — see the prevention note). It is the
  first entry in the ratified-but-unimplemented register (`ratified_unimplemented_register.md`).
- **Finding P2 (reassuring) — the RAW primitives are all LIVE.** Zeroing/maxing each of the 5 raw geometry
  primitives roster-wide and re-baking moves a win-rate basket by 29–87pp — none is a dead/inert lever. The
  raw-primitive emergence is real (`curvature`/`edge_keenness` → cut; `point_concentration`/`cross_section` →
  gap+thrust; `strike_concentration` → percussion pierce). *(Caveat: the roster-wide ablation also perturbs the
  arming baseline, so per-cell magnitudes are confounded — the identical stiletto shift under two different
  primitives is arming's edge moving; the "all live" conclusion is unaffected.)*
- **Watch item — the derivation is calibrated to REPRODUCE hand-set values.** `geometry.py`'s own docstring:
  the derived coefficients are "calibrated to REPRODUCE the already-validated §4-grounded values." So the
  emergence is partly *curve-fit to a top-down tier list* (magic constants like `0.25+0.75·pc`,
  `cross_section**1.15`, `1.0−0.6·curvature`) rather than predicted from physical units — real emergence at the
  raw-primitive level, but the fitting constants are a latent place for hand-tuning to masquerade as physics.

## Trace + backward-causal analysis (2026-07-22) — `trace_backward.py`

A new lens: instrument the engine's `_TRACE` seam + spy `assemble_net_sigma` (the net-σ decomposition) and
`core.strike` (damage inputs), so **every input every decision node consumes** is captured; then walk each
battle **backward from its terminal state to its origin**. Three archetypal battles, each auto-selected by
outcome, reconstruct the causal chain — and independently confirm the findings above:

- **Half-sword loss (longsword vs arming, both plate).** Backward chain: felling blow `AR→LS cut_thrust
  dmg 7` — but *LS was already at 3 wounds*, and the run's tally is **AR 11 attacking beats vs LS 5**. The
  half-sworded longsword (origin reach **5.55**, down from 5.99) died by **accumulated volume**, even though
  its *own* blows were bigger (a traced `dmg 14` overwhelming at adef +0.51). This is the causal proof that the
  half-sword liability is volume-driven — and *why* the per-hit `adef` fixes I tried couldn't rescue it (they
  raise per-blow power; the loss is beat-count).
- **Reach win (spear vs arming, unarmoured).** The felling blow (`dmg 40`, overwhelming) is a **stop-hit during
  the approach** at gap 2.37 — the spear killed *before ever closing*. Lever-1 (reach-dominance = approach
  stop-hit) made visible end-to-end.
- **Anti-armour dagger (rondel vs arming, both plate).** Rondel wins on **armour-defeat σ = 0.53** (the
  gap-thrust through plate), from origin reach 4.51 (shorter — it first had to close). The grounded
  anti-harness dagger, causally traced.

Incidental: the **contact axis fires** (`CONTACT throw` / `escape` observed in the traces) — not an inert
lever. Run `python trace_backward.py` to reproduce (forward trace + backward chain per battle).

## Part A — Mechanical correctness (`stress_battery.py`)

| category | result | evidence |
|---|---|---|
| **robustness** — 51 wpn × 4 armour grid; 8×8 tradition grid | **PASS** | 204 matchups + 64 pairs, 0 crashes, 0 malformed results |
| **extremes** — all-zero / all-one / negative / huge / float / mixed-asym attrs | **PASS ×5, FAIL ×1** | only `mixed-asym` crashes → **Finding M1** below |
| **determinism** — same seed ⇒ identical result | **PASS** | 12 weapons × 3 replays × 15 fights, 0 nondeterministic |
| **symmetry** — mirror match ≈ 50% | **PASS** | worst dev 0.050 @ rapier/light (N=400 ≈ sampling noise; tradition-field mirrors sit within 2.9pp) |
| **numerical** — no NaN/inf; damage int ≥ 0; degree/resolve finite | **PASS** | 4080 damage calls, 400 degree bands, 405 resolve draws — all finite/valid |
| **monotonicity** — a better attribute never lowers win-rate | **PASS** | str/end/history/agi/cog/focus/spirit all non-decreasing over +0/+2/+4 |
| **upset-cap** — no matchup is 100/0 | **PASS** | maximal-vs-minimal fighter clamps to 94.7% (UPSET_FLOOR 0.05 active) |
| **termination** — bounded runtime | **PASS** | 6.8 ms/fight, no runaway loops |

### Finding M1 (LOW severity, latent) — unguarded logistic overflows on extreme input
`combat_systems.py` uses a bare `math.exp` logistic in **four** places:
`read_contest` (L782), `_read_edge`/id-read (L703), `bind_dominance_p` (L909), `disrupt_resist_p` (L914),
all of the shape `1/(1+exp(-x))`. `math.exp` overflows for `x < ~-709`, raising `OverflowError` and crashing
the fight. Reached only under a **large asymmetry** between the two fighters' reading-related attributes
(the fuzz case `cog=50, history=100, focus=0, spirit=0` vs a default fighter). It is **not reachable in real
play** (attributes are 1–8; uniform values up to 1000 do *not* trip it because the two sides' read terms scale
together and the margin stays bounded). Severity is low, but it is exactly the class a fuzzer finds and the fix
is a one-liner (clamp the exponent, or a numerically-stable logistic — `tanh` is already used safely elsewhere).
Recommend hardening all four sites at once. *(No fix applied here — PC lane is Jordan-deferred, ED-PC-0007.)*

---

## Part B — Grounding validation (`grounding_battery.py` + `workbench/balance.py`)

### B.1 What the engine gets RIGHT (the strengths — worth stating plainly)

**The armour arc is textbook Williams / Fiore.** Weapon × armour matrix (`weapon_armour_matrix`, N=300/cell,
each weapon vs a uniform arming baseline, both fighters at the same tier). The *arc* is the signature, not the
column:

- **The gap-thrust family INVERTS, exactly as the treatises demand.** none → heavy win-rate:
  rondel **26 → 88 (+62)**, stiletto **26 → 88 (+62)**, misericorde **34 → 90 (+56)**, dagger **21 → 76 (+55)**.
  Useless in an unarmoured duel (too short/slow), decisive against harness — the anti-armour dagger driven to
  the visor/armpit/groin gaps (Fiore *armizare*, Le Jeu de la Hache). This is the single most convincing piece
  of grounding in the engine.
- **Pure cutters COLLAPSE vs plate.** shamshir **85 → 8 (−77)**, pulwar **72 → 7 (−66)**, sabre **73 → 32 (−42)**,
  scimitar/falchion/tachi/nandao all −30ish. Deterministically confirmed at the coupling layer: a native cut
  retains ≤ 22% of its unarmoured damage vs plate (Williams: cutting riveted mail is "functionally impossible").
- **Percussion & gap-thrust rise vs plate:** mace **+12**, bec_de_corbin **+10**, goedendag **+10**,
  lucerne_hammer **+8**, spear **+10**, jian **+8**. Direction is right; magnitudes see B.2.
- ~~**Half-swording engages vs harness**~~ **[RETRACTED — see Adversarial revision]**: the switch *fires*
  (longsword/estoc adopt the half-sword form vs medium/heavy in the close), but it is a **net liability**, not a
  strength — the fighter wins ~30pp *more* vs armour when it never half-swords. The mechanic is backwards from
  the source.
- **Reach threat decays vs plate** (FIX-1): a cutting polearm's reach advantage drops (factor 1.00 → 0.86) once
  the target's armour makes its edge irrelevant — "the armoured man walks through a threat that can't hurt him."

**Tradition design is exemplary (C1 fully satisfied).** Unconditional spread over the field is **2.9pp**
(italian 50.8 … japanese 47.9), inside the ±2–3pp parity band — *no globally dominant tradition*. And the
context matrix flips the leader every time:

| context | leader | context | leader |
|---|---|---|---|
| arming | **german** | sabre | **chinese** |
| longsword | **english** | spear | **filipino** |
| rapier | **japanese** | | |

~~**5 distinct leaders across 5 contexts**~~ **[the per-context leader claim is RETRACTED — low-N artifact; see
Adversarial revision]**. What holds is the **2.9pp unconditional field spread** — no globally dominant tradition,
the core C1 requirement met. The per-context "leader flip" was noise (N=120; at N=400 only 3 leaders, ~0.4pp
margins). The unconditional flatness is real and is an improvement over the handoff's prior ~2-leader state.

### B.2 Where emergent play DIVERGES from the source (the findings)

#### Finding G1 (MEDIUM, appears under-tracked) — an arbitrary vs-plate cliff among cutting polearms
Two near-identical heavy cutting polearms land **86pp apart against plate** for a non-physical reason:

| weapon | affords | selects vs plate | win% vs plate |
|---|---|---|---|
| guandao | curved_cut + **point** | point (gap-thrust) | **96.0** |
| fauchard | curved_cut + **point** | point | 93.3 |
| voulge | cut_thrust + **point** | point | 91.7 |
| glaive | curved_cut + **point** | point | 56.9 |
| **bardiche** | straight_cut only | straight_cut (bounces) | **9.6** |
| **sparr_axe** | straight_cut only | straight_cut | **8.1** |

The discriminator is purely **whether an anti-armour `point`/gap mode_element was authored** on the weapon —
not any physical property. A real bardiche or sparth-axe fighter facing plate would half-sword, use the haft,
or target gaps just like anyone; modelling it as a pure cutter with *no* anti-armour mode drops it to 8%, while
its cousin the guandao (which happens to have a spike element in the data) sits at 96%. The U2/ED-PC-0011 work
added `point` elements to *some* cutting blades (and even flagged sabre/scimitar/falchion's switch as a
*probable* bug, ED-PC-0012); this is the **complementary gap** — weapons that *should* afford an anti-harness
mode but were left pure. The cliff is an authoring-coverage artifact, not grounded physics. **Recommend** a
roster audit of anti-armour affordance coverage (every pole/haft weapon can half-sword/gap-seek to *some*
degree; a pure-cutter-vs-plate floor of ~8% should require a positive physical reason, e.g. a true edge-only
Dane axe, rather than falling out of missing data).

#### Finding G2 [SUPERSEDED by the Adversarial revision — kept for the audit trail; the cause is the half-sword switch, not a coupling discontinuity] — the non-monotone "mail valley"
The half-sword switchers perform **worse against mail (medium) than against plate (heavy)** — backwards, since
mail should be *easier* to defeat than plate. N=600/cell, CIs non-overlapping (not noise):

| weapon | none | light | **medium** | heavy |
|---|---|---|---|---|
| longsword | 46.3 | 45.5 | **27.6** | 40.8 |
| estoc | 93.7 | 93.3 | **70.5** | 78.9 |

A ~13–18pp notch at the mail tier that recovers at plate. The half-sword form triggers at medium *and* heavy,
so the switch itself is not the cause; the driver is a coupling/`ADEF_THRESHOLD` discontinuity at the mail
tier (mail resists both shear .85 and puncture .45 while offering less of the exploitable gap-geometry the
plate path rewards) — a "valley of death" where the weapon neither cuts through nor gets full gap-thrust
credit. It surfaces only for the half-sword switchers. Whether a mail-is-good-all-rounder dip is *intended* is
a design call, but a monotone armour-difficulty curve is the physical default and this notch reads as a tuning
discontinuity. **Recommend** inspecting the medium-tier coupling for the point/half-sword path against the heavy
tier.

#### Finding G3 (KNOWN — corroborated) — poleaxe uses its hammer, not its spike, vs plate
Confirmed deterministically: `select_mode(poleaxe, 'heavy')` → **blunt**, never `point`. Le Jeu de la Hache
makes the *spike* the primary anti-harness answer. This is the accepted-red `test_gap_game_poleaxe_spikes_
plate` [PHASE-C]: the morphology-rearch Phase-B real mass distribution lifted the poleaxe's percussion
authority *above* the mace's, so it prefers the hammer face. Already deferred to a Phase-C engine-scale
recalibration; this run simply re-confirms it is still live.

#### Finding G4 (KNOWN — corroborated with fresh scope) — reach-class flat-dominance
The whole polearm class beats an arming baseline at **80–96% across *every* armour tier** (spear 81/79/83/91,
yari 91/89/88/92, guandao 95/95/97/96), above the plan's intended ~55–75% *contested* band. Root cause is the
tracked Phase-B mass-model debt (`test_heft_percussion_ordering_at_ideal` / SPEAR finding: spear's heft
numerator sits above arming/longsword's, so `spear < arming < longsword` fails). Reach is *supposed* to
dominate the unarmoured duel (correct, grounded), but it should compress toward contested as armour rises and
across the roster it does not. Same debt cluster as G3.

### B.3 Notes (lower confidence / design calls, not asserted as bugs)

- **Attribute drift — agility is now the dominant stat.** Marginal +1 win-rates: **agi +29.9**, cog +18.6,
  history +14.4, strength +13.9, end +10.6, spirit +10.3, att +5.9, focus +3.1, disp −3.2. A single agility
  point swinging a duel to ~80/20 is a steep single-stat dependency, and agi has pulled well clear of the
  documented 2026-06-28 baseline (agi +20 ≈ strength +20). Worth a re-budget check that agility hasn't absorbed
  too much of the outcome (it drives cadence + reflex + closing simultaneously). `disp −3.2` ("both poles cost")
  is intended.
- **mace vs plate magnitude.** The mace *rises* vs plate (grounded direction) but only to 21% vs a half-swording
  arming baseline. The "war-hammer owns the armoured press" principle (which the methodology itself cites) may
  want more; this is downstream of the same percussion-path calibration as G3.

---

## Reproduction

```
python audit/2026-07-22-combat-engine-stress-test/stress_battery.py       # mechanical, ~90s
python audit/2026-07-22-combat-engine-stress-test/grounding_battery.py    # grounding physics layer, instant
cd systems/combat/combat_engine_v1 && python workbench/balance.py armour 300   # the weapon×armour matrix
```

## Suggested triage (all Jordan-gated; PC lane is deferred — nothing actioned here)

| id | severity | type | owner-lane |
|---|---|---|---|
| **half-sword switch is a net liability** (fix direction: credit the leveraged weight-bearing thrust into gap-thrust adef, emergent; roster-wide joint re-tune) | **high (grounding)** | grounding / calibration | PC |
| G1 cutting-polearm anti-armour affordance cliff (novel) | medium | grounding / roster data | PC |
| agility single-stat dominance (novel; robust to baseline) | medium | balance budget | PC |
| M1 unguarded logistic overflow (4 sites) | low | robustness hardening | PC |
| G3 poleaxe hammer-not-spike vs plate | known | grounding / Phase-C | PC |
| G4 reach-class flat-dominance | known | grounding / Phase-C mass model | PC |
| ~~G2 mail valley~~ | superseded | → the half-sword finding above | — |
