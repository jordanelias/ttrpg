# Combined Research Brief — Closing-Distance / Facing / Grip / Grappling (Valoria scene-combat redesign)

**Scope & discipline.** This brief synthesizes four fact-gathering passes (`measure_gap`, `facing_stance`,
`commitment_depth`, `grappling`) into one cited reference for the closing-distance/facing/grip subsystem
redesign. It is **facts + citations only** — no formulas, gains, or 0–1 scalars are proposed here (that is the
next phase's job). Every claim is either something a treatise explicitly describes or a biomechanically
measurable fact; source is cited per claim, and disagreements/uncertainties are flagged rather than resolved
silently.

**Motivating symptom (not itself researched).** Spear/polearm-class weapons reportedly win 84–96% of matchups
against an arming sword in the current engine. Jordan has confirmed this needs a genuine mechanics redesign,
not number-tuning. The research below grounds what physically happens when a shorter-reach fighter closes on a
longer weapon, so the next phase can pick mechanics rather than multipliers.

---

## 0. Engine baseline — VERIFIED against the working tree (do not re-propose these)

All four research files were cross-checked against the live source at
`C:/Github/ttrpg-morph-rearch/designs/scene/combat_engine_v1/` (`systems.py`, `wrapper.py`, `weapons.py`).
The following primitives **already exist** and were confirmed by direct code read this pass:

| Primitive | File / loc | What it already models |
|---|---|---|
| `reach_base` / `reach_sigma` | systems.py:409–417 (+ ~11–20) | Standing reach derived from body offset + weapon geometry (head_len + 2H rear-hand setback). A **scalar**, not orientation-dependent. |
| `close_rate` / `approach_displace` | systems.py:444–450 | Linear closing rate; a higher-**leverage** shorter weapon sets aside a **thrusting** longer point (fires only if `longer.head=='point'` and lever edge > 0), suppressing the stop-hit. Purely **1D/linear** — no lateral/angular component. |
| `leverage` | systems.py:360–372 | `grip_len − LEVER_HEAD_K·head_len` (explicit hand-to-contact lever arm, +2H bonus). Comment documents the fix of a verified HEMA inversion (dagger 0.140 > spear −0.066 under the old ratio). |
| `commit_depth` / `lunge_depth` / `lunge_quality` | systems.py (commit_depth); wrapper `engagement` | Beta-distributed commitment [2,5] per closed beat; a deep thrust (≥`LUNGE_COMMIT` 4.0) stochastically becomes a lunge, gated by `lunge_quality` (point_concentration × lightness × hand-balance × one-handedness). Feeds power, recovery-tempo penalty, overcommit exposure, legibility. **Driven ONLY by aggressor disposition/wariness — never by current `measure_gap`.** |
| `recoverability_factor` / `_recovery_mode_commitment` / `at_grip` | systems.py:96–137 | Grip-position-aware MoI (I_g) + static-moment (S_g); blends swing-arrest vs thrust-retract by point_concentration; adds 1H/2H force-couple credit + lunge body-extension penalty (the "commitment=recovery" axis). Structure `[ASSERTED]`, gains `[FIAT/SIM-CALIBRATE]`. |
| `close_unwieldiness` / `can_choke` / `grip_target` / `grip_choke_max` | systems.py:138–156 | Once closed, a fighter **gathers in** (grip_position 0→1) proportional to `close_unwieldiness` (reach beyond `CLOSE_REACH_REF`), bounded by `grip_choke_max` (a pole chokes up; a rapier's short hilt cannot). **This is the engine's existing half-staff / choke-up equivalent.** |
| `halfsword_target` / `HALFSWORD_FORM` | systems.py:393–401 | Pure predicate: a half-sword-capable weapon switches to the shortened form when **closed AND vs medium/heavy armour**. Gated on armour, wired only for sword-family forms (e.g. `estoc`→`estoc_halfsword`). |
| `beat_aside` / `slip_inside` | wrapper.py:220–240 | Two **distinct** routes to exploit a committed thrust (M3 decoupling): (a) `beat_aside` = strong-leverage weapon sets point offline; (b) `slip_inside` = shorter reach + equal/better reflex ducks inside ("the dagger inside the rapier lunge"). |
| `reach_threat` | systems.py:347–358 | A longer weapon's reach edge decays if it cannot defeat the closer's armour (armour "walks through the reach-ladder"). A0-safe (unarmoured factor 1.0). |
| `reopen_prob` + freed-hand shove | wrapper.py:241–252, systems.py:452–462 | The longer weapon regains distance only when a "moment" exists (opponent overcommitted, defender's defensive win, or a 2H freed-hand shove at `PUSH_AVAIL_P`). **No lateral/circling component — re-opening is "walk straight back."** |
| `clinch` (weapon field) | weapons.py (all records) | Integer 1–10 "grappling affinity" on every weapon. **DEAD DATA — verified zero consuming functions this pass** (grep hits are weapon definitions + design-doc references only). Phase 5 (clinch/disengage/choke) is explicitly **NOT STARTED** (`phase4_5_plan_v1.md:216`). |

**Two engine facts every finding below should be read against:**
1. `commit_depth`/`lunge_depth` are **decoupled from range** — there is no coupling of "how much room the
   weapon has to develop its strike" to attack power or commit depth. (Confirmed gap, all files agree.)
2. Closing is **purely linear** — no facing/orientation, no lateral/circular footwork, and `dodge` is one
   uniform void mode (no distinction between pivoting-in-place, lateral/circular stepping, and linear retreat).

---

## 1. Footwork for closing distance against a longer/thrusting weapon

**[STRONGLY GROUNDED] The void and the close are the SAME motion, not sequential.** Fiore's first spear
defence: slide the front foot off the centreline and beat the opposing point aside **while passing the back
foot forward** — a single motion. Fiore generalizes it as doctrine: *"all guards which step off line with
short spear and short sword are enough when facing any long hand held weapon."*
— Fiore, *Fior di Battaglia*, Posta Mezza Porta di Ferro (spear), **fol. 39r** (fightlikefiore.wordpress.com
translation; corroborated selohaar.org "The Spear of Fiore dei Liberi"). *High confidence (verbatim play text
+ folio), but note the generalization is Fiore's own doctrine, not an independently verified biomechanical fact.*

**[STRONGLY GROUNDED] Hand-motion must lead foot-motion ("true times").** George Silver: true times are
*"whatsoever is done with the hand before the foot or feet"*; foot-before-hand is "false fight." A long weapon,
needing the feet to travel farther to "win the place," is inherently **slower-timed** than a short weapon's
hand-led response.
— Silver, *Paradoxes of Defence* (1599), true-times paradox (pbm.com/~lindahl/paradoxes.html). *Medium-high;
cross-checked against a second independent summary, but exact paradox numbering not verified against a facsimile.*
> **Cross-source convergence:** this is the SAME axis the engine already cites in `recoverability_factor`
> (Silver true-times / Giganti for the lunge/body-extension term). The treatise supports the existing axis; it
> does not demand a new one.

**[MODERATELY GROUNDED] The fight is divided into named temporal phases across three traditions:**
- Meyer (1570): **Zufechten** (onset/approach) → **Handtarbeit** (handwork/close) → **Abzug** (withdrawal),
  with **gathering steps** (feet don't cross) vs **passing steps** (feet cross, more ground/step) vs
  triangular/offline steps. Meyer's polearm (Stange) chapter reuses longsword footwork rather than a separate
  system. *Medium — division structure and step vocabulary well-attested across secondary Meyer scholarship;
  a direct primary quote for the polearm-footwork crossover was not retrieved (PDF exceeded fetch limits).*
- Liechtenauer tradition: **Vor / Nach / Indes** (before / after / the instant in-between), plus **Fühlen**
  (tactile sensing in the bind) and **Winden** (winding). Fühlen and Indes are treated as **one skill**.
  *Medium — well-established general doctrine; no primary quote specifically about closing against a spear was
  located (flagged gap).*
> **Cross-source convergence:** all three traditions carve the fight into an **approach phase** and a
> **close/handwork phase** — matching the engine's existing approach/closed-exchange state split. The
> treatises frame this as a **regime boundary** (different techniques become available), not a continuous gap.

---

## 2. Deflection of a thrusting point (leverage / forte-foible)

**[STRONGLY GROUNDED — rigid-body physics] Leverage is hand-to-contact distance.** Standard parry doctrine:
engage the opponent's **weak** (foible, midpoint→tip) with your own **strong** (forte, cross→midpoint),
because contact closer to your hand/pivot yields more torque/control per unit hand-force. Stated as basic
lever mechanics (torque = force × moment arm from the hand), near-identically across sources.
— historicaleuropeanmartialarts.com; Path of the Sword "Longsword Leverage…"; Wikipedia "Forte (fencing)".
*High — uncontroversial lever mechanics; treat the underlying physics as load-bearing fact.*
> **Consistency with the engine:** the current `leverage()` structure (grip_len minus a load term, **not** a
> ratio) matches this — leverage scales with absolute hand-to-contact distance, not proportional geometry. The
> code comment's documented inversion fix (dagger 0.140 > spear −0.066 under the old ratio) is the same fact.

**[FLAGGED GAP — analytical, not a single-source claim] Forte/foible is a WITHIN-EXCHANGE, contact-point fact;
`leverage()` is a fixed per-weapon scalar.** The treatise/physics concept is *where along YOUR OWN blade the
bind lands* (near your hilt = strong; near your tip = weak) — a quantity that varies **per crossing**. The
engine's `leverage()` is a whole-weapon scalar comparing two combatants' grip/head geometry. Both facts are
independently attested; the current single scalar may only capture the per-weapon half. (Noted for the next
phase; resolving it would mean proposing a formula, which is out of scope.)

**[MODERATELY GROUNDED] Deflection = perpendicular redirection, not a head-on block.** A small lateral force
redirects a moving point off-line (adds a sideways velocity component) with far less force than stopping its
forward momentum — the physical distinction between "redirection" parries and "opposition" parries.
— hema101.com "An Introduction to Parrying." *Medium-high — the vector mechanics are solid; the specific
source is a pedagogy blog, so treat any numeric claims as illustrative, not measured.*

**[MODERATELY GROUNDED] The weapon itself can be the deflector (spear beats spear).** Fiore's spear from Posta
di Fenestra: *"one can beat aside and obstruct every thrust… and beat to the ground"* — a percussive lateral
**beat** of the opposing shaft, not a static block, executed with the spear (not a sword's cross).
— Fiore, *Fior di Battaglia*, spear/Posta di Fenestra (fightencyclopedia.com; fightlikefiore.wordpress.com).
*Medium — corroborated across two secondary sources; exact folio not re-verified.*

**[MODERATELY GROUNDED] Seizing the shaft is a DISTINCT mechanism from a deflection.** Once inside, the free
hand can grab the opposing shaft directly — *"with a spear you can more easily grab the shaft and control the
weapon"* — because a haft is a graspable cylinder where a sword's edge is not. This is manual seizure, not
forte-leverage. — Paulus Hector Mair (polearm/wrestling material), via fightencyclopedia.com. *Medium — the
physical fact (haft grippable, edge not) is self-evident; specific Mair folio not retrieved.* (See §5 for the
grappling detail on this mechanism and its inconsistency with the current `clinch` data.)

---

## 3. Facing / stance (square vs bladed/oblique) — and its LOOSE relationship to footwork

> **Overarching finding [STRONGLY GROUNDED as a *disagreement*]: facing is per-guard/per-moment, NOT
> per-weapon-class.** A single fighter holds multiple guards across one exchange (Fiore: Donna [bladed] →
> Longa [centreline] → half-sword bind). "This weapon class uses this facing" is very likely the wrong level
> of abstraction. This is stated as an explicit cross-source disagreement, not a resolved rule.

**Bladed/oblique stances (attested):**
- **[STRONGLY GROUNDED]** Fiore **Posta di Donna** (2H longsword): explicitly bladed/turned — left shoulder to
  the opponent, sword chambered over the right shoulder, point trailing behind the left knee. — Fiore,
  *Fior di Battaglia* longsword guards (Wiktenauer; fightlikefiore). *Well-attested across sources + MS illustrations.*
- **[STRONGLY GROUNDED]** Fabris rapier (1H): forward lean at the hips, sword arm maximally extended forming
  *"a direct line between the shoulder and the point,"* torso profiled to reduce frontal target. — Fabris,
  *Lo Schermo* (1606), via Lanham analysis (klanham2018). *Well-attested; directly quotes Fabris.*
- **[MODERATE]** Capoferro rapier (1H): backward lean, refusing chest/head; measurable height loss + wrist-bend
  at full extension. — eastkingdomgazette.org comparative paper. *Moderate-high; secondary comparative sources.*

**Square stances (attested):**
- **[MODERATE]** German **Vom Tag** (2H longsword): hips/torso faced forward, one foot leads but torso not
  strongly bladed. — historicaleuropeanmartialarts.com. *Moderate; secondary/practitioner characterization.*
- **[LOW-MODERATE]** **Chudan-no-kamae** (kendo/naginata/kenjutsu, 2H/pole): squared, "hips straight forward,"
  feet parallel; a bladed variant **hanmi-dachi** exists and is named separately, tied to avoiding simultaneous
  strikes (ai-uchi). — Wikipedia (tertiary — flagged). *Low-moderate; cross-cultural corroboration only.*
- **[LOW-MODERATE]** Silver's English "true guard" characterized as "square-footed." — secondary/tertiary
  paraphrase of Wiktenauer/Grokipedia. *Lowest-confidence claim in the set; NOT read against Silver's primary
  wording — flagged for verification.*

**[STRONGLY GROUNDED as a disagreement] Bladed does NOT imply linear-only footwork:**
- **[MODERATE, strongest counterexample]** Spanish **La Verdadera Destreza** (rapier, 1H): **bladed/profiled
  stance + systematic CIRCULAR footwork** (the "Spanish Circle"); circular stepping demonstrably **does** close
  measure. — puckandmary.com destreza-footwork analysis. *Moderate — single detailed secondary source.*
- **[MODERATE]** Bolognese **Manciolino** (1H): lateral **traverse step** (passo alla traversa). — renfence.com.au.
- **[MODERATE-HIGH]** Italian rapier (Fabris/Capoferro): the ATTACK footwork **is** a single discrete linear
  lunge (lead foot advances, rear leg is the planted power source); passing step used sparingly. This is the
  source that most cleanly supports "bladed → linear advance." — hema101.com; klanham2018. *Tradition-specific,
  not universal.*

**[MODERATE] Square does NOT imply lateral-only footwork either:** German Liechtenauer doctrine explicitly
prescribes **not** stepping straight into a strike but stepping offline/circling to the flank — a squared
stance (F3) WITH prescribed lateral/circular stepping. — secondary Liechtenauer-gloss summary (specific folio
not traced). *Moderate.*

**Cross-domain corroboration only (NOT HEMA evidence — label clearly if used):** modern boxing coaching frames
**bladed** = smaller profile / more lead-hand reach / favors straight-line attacks / harder lateral in-out
movement; **squared** = larger profile / even reach split / favors circular movement + pivots. — myboxingcoach.com;
martialtheory.substack.com. *Low as HEMA evidence; directional/illustrative only.*

**[MAJOR OPEN CONTRADICTION — see flags] Polearm/greatsword facing is the LEAST-grounded question.** F3/F8
give converging circumstantial support that **long 2H weapons tend square**; but an un-verified web summary
(Quora, HTTP-403, only the search snippet obtained) asserts the **opposite** — that both European and Japanese
polearm traditions use a **side-on/angled** stance for hip rotation and reduced profile. Neither was
independently corroborated. This needs a primary polearm-treatise read before design relies on it.

---

## 4. Commitment depth, range-utilization, and the consequences for the longer weapon once closed

### 4a. Measure is a graded system of distance-gated actions (thrust side)

**[STRONGLY GROUNDED] Distance bands each map to a specific available action.** Capoferro's *Gran Simulacro*
(1610) defines named measures: **misura larga** (strike head/torso with a step-lunge, or the arm with a
leaning-lunge) and **misura stretta in pie fermo** (hit by inclining body/legs, no step). Capoferro:
*"the end of the tempo of wide measure is the beginning of the tempo of narrow measure"* — the closing motion
and the striking motion are two distinct, sequential, distance-gated actions.
— Capoferro, *Gran Simulacro* (1610), Ch. IV/XI (Wiktenauer; thetavernknight; grauenwolf). *High — multiple
independent translations agree.* **Caveat:** the four-tier scheme (larghissima/strettissima) is a **modern**
pedagogical gloss; only the two-tier larga/stretta distinction is primary-source-attested.

**[MEDIUM-HIGH] The lunge/passata is a distinct, deeper, less-recoverable action.** Executed as a single
tempo — weight thrown from back foot to front, driven by weight-transfer/body-drop, not just an arm reach —
mechanically distinct from the fixed-foot misura-stretta strike (body/leg inclination alone).
— Capoferro, *Gran Simulacro* (lunge mechanics). *Medium-high; secondary instructional paraphrase.*
> **Consistency with the engine:** matches the existing `lunge_depth`/`lunge_quality` model exactly (a lunge
> is a deeper, less-recoverable committed action). The treatise adds that **which action is available is
> distance-gated** — the piece the engine does NOT yet have (see confirmed gap).

**[MEDIUM] Graduated/partial commitment is a recognized category.** Fabris's **passata sotto** = a fully
committed passing lunge + body-drop evasion (depth does double duty: max reach/power AND removes the body from
the line). Capoferro's **scannatura** (Plate 13) = a committed passing thrust taken opportunistically against
an opponent's disengage. — Fabris (1606); Capoferro Plate 13 (swordschool.com). *Medium; plate numbers not
re-verified against a facsimile.*

**[MEDIUM] Lunge recovery is a distinct reversed motion with the arm recovered LAST** (point stays committed
while the body withdraws — prolonged exposure). This is the structural basis for the riposte/counter-time
family. — modern fencing pedagogy tracing to the historical tempo systems. *Medium — general consensus, not a
single treatise citation; same Nach-after-overextended-Vor principle the engine already invokes.*

**[MEDIUM] Commitment is a tactically-chosen spectrum, not binary.** Meyer categorizes fighters by commitment
discipline (a disciplined fighter "doesn't strike unless sure they can both land AND recover safely") and
instructs **avoiding full steps when feinting** (half-steps / un-planted foot to retain the abort option).
— Meyer (1570), longsword (hroarr.com; okanagancombatguild.com). *Medium.*
> **Consistency with the engine:** directly supports modeling commit-depth as a continuous chosen spectrum
> (the existing `commit_depth` Beta model), with recovery-safety as the cost side.

### 4b. Consequences for the LONGER weapon once distance is closed

**[STRONGLY GROUNDED] Half-swording (mit dem kurzen Schwert):** the off-hand grips partway down the blade,
converting the longsword into a short rigid spear-like thruster for armour-gap thrusts (visor/armpit/groin).
Period treatises show armoured combat as **primarily** conducted at the half-sword; cuts are "virtually
useless against plate." — Talhoffer (1467) & others; Wikipedia "Half-sword"; Grokipedia. *High — one of the
best-attested HEMA techniques.*
> **Consistency with the engine:** directly modeled by `halfsword_target()` (closed AND armoured → half-sword),
> and the trigger (measure + armour) matches the historical armoured use-case. **Not a gap.**

**[MEDIUM] Polearm close-range analogue = choke up to a centre/"staff"/"Robin Hood" grip** (hands at ~⅓
points, thumbs inward), striking with **either end** at close range — the polearm equivalent of half-swording,
using both the head end AND the butt-spike. — grauenwolf.wordpress.com grip terminology; general polearm
surveys. *Medium — the grip-terminology source is a community blog, but corroborated by the Fiore pollax
"half-staffing" material and matches the engine's `grip_target`/`can_choke`.*

**[MEDIUM] Fiore's pollax "half-staffing"** (centre grip) is a named technique class enabling both-end striking
AND grappling/hooking/tripping in close armoured combat. — secondary Fiore-pollax summaries (thearma.org).
*Medium — "half-staffing" is a modern label, not Fiore's period term; folio not retrieved.*

**[LOW-MEDIUM] The butt-spike is a documented fallback strike** when the primary head can't be brought to
bear ("a finishing move… or a secondary weapon if the spear head has broken and you can't withdraw [it] in
time"). — general polearm surveys (lostkingdom.net; Wikipedia "Poleaxe"). *Low-medium; not tied to a specific
named treatise play.*

**[MEDIUM-HIGH] The long weapon's excess length becomes an ACTIVE liability at close range.** Silver: the part
of the staff "that will lie behind him, will hinder him to strike, thrust, ward, or go back in due time" — the
behind-the-hands length is not inert; it impedes all four of strike/thrust/ward/retreat because it must be
repositioned as dead weight (moment of inertia) in confined space. Separately: a long rapier, once crossed by
a short sword at close range, "cannot be undone… without going back with their feet" — **recovery requires
footwork**, which true-times classifies as slower-timed than the short weapon's hand-led continuation.
— Silver, *Paradoxes of Defence* (1599), short-staff & rapier-crossing paradoxes. *Medium-high; internally
consistent with the MoI physics, but exact paradox numbers not cross-verified against a second transcription.*

### 4c. Minimum-distance / range-to-power (the "does a weapon need room to develop its strike" question)

**[STRONGLY GROUNDED — peer-reviewed] Thrust mechanics measurably reconfigure with available distance.**
Fencing-lunge biomechanics: as target distance increases, fencers increase rear-leg knee flexion early, then
enhance hip extension and plantar-flexion velocity. A modern lunge covers up to ~1.5× fencer height (one study
mean final lunge distance **260.0 ± 9.8 cm**); peak COM velocity rises with target distance.
— PMC10203838; ScienceDirect novel-sabre-lunge; MDPI 2024 target-distance kinematics. *High as biomechanics —
strongest-tier evidence in the corpus. **Caveat:** modern sport fencing (thin blade, no armour, different
mass/MoI); transfer the QUALITATIVE fact (thrust mechanics adapt continuously to distance), NOT the 1.5×/260 cm
numbers, to HEMA weapons.*

**[STRONGLY GROUNDED — peer-reviewed] Strike force scales with kinetic-chain / joint-extension completion.**
- Rinaldi et al. (2018) instrumented karate lunge-punch: mean force **181.2 N**, with significant positive
  correlations between force and knee ROM (1.13, 0.82 rad) and leg ground-reaction force (550.2, 425.1 N);
  elbow angle at impact **1.19 rad (~68° from lockout)** — even a maximal strike retains flexion at contact.
  Force correlated **negatively** with peak trunk angular acceleration → force depends on a full, unrushed
  sequential chain, not a fast truncated one.
- Dinu et al. (2020): elite boxers out-force juniors; juniors show higher **shoulder-only** contribution (a
  truncated, arm-driven, lower-force chain). Cross-punch front/rear GRF imbalance 60.6%/39.4% (weight shifts
  forward as part of delivering force).
- Beattie & Ruddock (2022): **lower-body** strength (not upper-body) differentiates high-impact-force boxers.
- Dunn et al. (2021): lower-body/trunk fatigue reduces punch force in all punch types, more so in rotation-
  heavy punches than the arm-only jab → removing the leg/trunk contribution collapses toward arm-only force.
— Rinaldi 2018 (EJSS); Dinu 2020 (Front. Sports); Beattie & Ruddock 2022 (JSCR); Dunn 2021 (EJSS).
*High — converging instrumented studies. **Caveat:** unarmed strikes, not a bladed/hafted swing or thrust arc;
transfer is an inference.*

**[MEDIUM] Force-vs-distance is NOT simply monotonic — there is an OPTIMAL distance.** Bolander, Neto & Bir
(2009) measured Kung Fu punch/palm strikes from varied distances: force generally increased with distance,
**but** the middle-distance chest-level palm strike out-accelerated the long-distance one — evidence of an
effective/optimal distance, not "farther is strictly better." — Bolander 2009 (J. Sports Sci. Med.; PMID
24474886). *Medium — the single most load-bearing and least-triple-verified numeric claim; full results table
not read this pass. Unarmed strikes, not weapons.*

**[LOW-MEDIUM] A "full" vs implicitly "checked/lesser" blow is a recognized period category** — Silver: "a
full blow upon the head or face with a short sharp sword, is most commonly death" (the word "full" implies a
non-full alternative). But the quote does NOT specify a required distance/space. — Silver (1599). *Low-medium;
establishes only that the category existed, not a quantified minimum distance.*

**[MEDIUM — treatise FRAMING contrast, important for design] Treatises frame close-range as SWITCHING to a
shorter action, not the SAME action arriving weakened.** European treatises (Capoferro/Fabris/Fiore/Silver)
speak in terms of *"what action is available/appropriate at this measure"* (misura stretta → strike by
inclining only, no lunge) rather than *"the same lunge thrown from too close arrives with less force."* This is
closer to the engine's existing **commit_depth/lunge_depth continuous-selection** model (choose how deep to
commit) than to a "same action, degraded" model. — negative/framing finding, no positive citation. *Low-medium
(absence finding).*

---

## 5. Grappling integrated into armed combat (weapon grabs, arm/wrist grabs, pins)

> **The `clinch` weapon field (1–10 on every weapon) is DEAD DATA — no consuming function exists** (verified
> this pass). Phase 5 (clinch/disengage/choke) is explicitly NOT STARTED. Everything below is grounding for
> whenever that field is wired; **no grapple/clinch/pin state exists in the state machine today.**

**[STRONGLY GROUNDED] Sword-on-sword grappling is BIND-GATED, in BOTH traditions.** It flows from an already-
established crossing/bind that has compressed to close range — never reached from open measure:
- Fiore: **Zogho Largo** (tips meet, left foot forward) — no grappling available; vs **Zogho Stretto** (blades
  cross near the hilt, right foot forward, within arm's reach) — teaches "every kind of parry, strike, bind,
  dislocation, grapple, disarm and throw." The Getty close-play sequence's 25 plays all proceed **from an
  existing crossing**, "largely without an additional step." — hemapenzance.com; chicagoswordplayguild.com.
- German **Ringen am Schwert**: entry is triggered *"When you bind against his sword"* (Ringeck, via
  thearma.org). — thearma.org "Ringeck." *High — independently corroborated in both traditions.*
> **Consistency with the engine:** the engine already has a bind subsystem (`bind_sigma`, 3-iteration Fühlen
> contest, wrapper.py). A grapple that gates off an existing bind fits the existing state machine's bind node.

**[STRONGLY GROUNDED — the clearest branching-outcome evidence] A single dominant grip yields a MENU of
outcomes.** Fiore's Dagger **2nd Remedy Master** (against a committed overhead/hammerfist thrust): *"I can
break your arm and I can throw you to the ground, and I can take your dagger. I can also tie you in the high
bind. And from these four things, you will not be free."* → four named branches: **(1) arm-break, (2) throw,
(3) disarm, (4) restrain/tie** — a decision point once control is achieved, not a fixed single outcome.
— fightlikefiore.wordpress.com; armizare.org. *High.*

**[STRONGLY GROUNDED] Dagger/unarmed grabs are OPEN-CONTACT (not bind-gated); the first contact IS the grab.**
Fiore Dagger **1st Master**: contact the attacker's forearm/wrist **at the apex of the strike**, "roll your
hand over and grab on"; disarm via **rotational torque** (palm-down, elbow drawn to the hip) — a lever-arm
action, **not raw grip strength**. — fightlikefiore.wordpress.com. *High.* So the range gate **differs by
weapon class**: sword-vs-sword grappling is bind-gated; dagger/unarmed grappling begins at first contact.

**[STRONGLY GROUNDED] Documented grab targets and named weapon-seizures:**
- Wrist/forearm (Fiore dagger); **upper arm / biceps** as throw-entry (Ringeck leg-breaks).
- **Hilt grab:** Ringeck "Fifth Sword Wrestle" — left hand over the opponent's right arm, seizes the opponent's
  own **sword handle** two-handed.
- **Mid-blade grab:** Ringeck "Taking a Sword" — seize **both crossed blades at their centre** with the (gloved)
  left hand, drive through with the right. Confirms blade-grabbing (not just hilt) is documented, reliant on
  gloved/armoured hands or a low-leverage grab point.
- **Finger lever:** Ringeck — seize two adjacent fingers and tear apart.
- **Shoulder-fulcrum arm-break** (Ringeck "Second Leg-break") and **torso-braced arm-pin** (Fiore posta lunga
  over the captured arm) — the practitioner's **own body** is the lever fulcrum.
- **Foot-pin of the weapon** (Fiore *rompere di punta*, Getty **Carta 28V**): after beating the point to the
  ground, "forcefully place [a] foot over his sword… Either I break it or I hold it [so] that he cannot control
  it any more," chained into a false-edge neck strike + cut to arms/hands.
— thearma.org "Ringeck"; learnfiore.org StrettoPlays.pdf (Getty Ms. Ludwig XV.13, Carta 28V). *High.*

**[STRONGLY GROUNDED — physical preconditions for a grab to succeed]:**
1. **Timing/geometry of the incoming strike** — Fiore's dagger grab is timed to the **apex/maximum commitment**
   of the incoming blow; the 2nd Master grip works "especially well against a committed overhead" (a clean
   linear line to the wrist). No such claim is made for a probing/disengaging attack.
2. **Leverage/torque over raw grip force** — the disarm mechanism is a moment-arm action, not muscle.
3. **A free hand is a stated precondition** — German seizures are two-part (one hand grabs the weapon/arm while
   the other retains one's own weapon or delivers a mordhau/pommel strike).
4. **Target exposure created by a PRIOR action** — every documented grab/pin is gated on a preceding event
   (a bind, a beaten-aside weapon, a committed strike). **No source documents a successful grab against an
   un-compromised weapon or limb.** Grabs are consistently opportunistic on a created opening, never a baseline
   always-available action.
— fightlikefiore; thearma.org/Ringeck. *High — consistent across all sources.*

**[STRONGLY GROUNDED, cross-verified against project data] Polearm hooking hardware is real, purpose-built, and
already in the roster.** `weapons.py` (morphology-rearch Phase B2/B4) records dedicated hook/catch elements
with inline citations: guisarme's "hooked cutting blade" ("the hook itself is the weapon's namesake catching
feature"), ji's "perpendicular crescent" (unhorse cavalry / catch shields), bec_de_corbin & lucerne_hammer
rear beak/fluke, ranseur's wing-prong (cites Monte), partisan's wing-lug (cites Manciolino), voulge's rear
hook-notch, fauchard's back-hook-spike, dangpa's cross-blade/flank-tine (cites Muyedobotongji). Historical
function of the bill/guisarme hook: drag/dismount mounted opponents, "finding a chink in the plate armour."
Talhoffer's poleaxe chapter includes close-range grappling, paralleling Ringen am Schwert. — weapons.py (read
directly); medievalchronicles.com; Wikipedia "Bill (weapon)"; truefork.org/Talhoffer. *High.*

**[STRONGLY GROUNDED] The hook-created-opening → pull-down → finish PATTERN (Fiore spear, Getty-cited):** after
beating the point offline, strike the neck with the **flat/shaft** (using the weapon's length as a lever), then
use the **shaft as a hook across the back of the neck to pull to the ground**, then thrust. Explicitly
bind/parry-gated ("any time the Scholar's parry takes his spearhead offline"). Both ends of a polearm
(head AND heel/butt) are documented for hooking/grappling follow-ups (butt face-thrusts, collar throw, "grapples
and hooks with the heel to the arms and neck"). — learnfiore.org StrettoPlays.pdf (Getty-cited). *High for the
MECHANICAL PATTERN.* **Scope note:** the primary-source detail covers Fiore's **plain spear** using an
**improvised shaft-hook**; no single primary source describing a named play with a **forged** guisarme hook (vs
the improvised shaft-hook or the bill's cavalry-dismount use) was located this pass.

**[MEDIUM] Counters/escapes for the grabbed fighter are documented to EXIST but were not extracted in named
detail:** Ringeck "frequently includes defensive counters"; grabbed fighters "counter-grip, escape through
footwork manipulation, or transition to alternative wrestling positions." Fiore's abrazare counters (secondary,
no MS citation) include lifting the arm and pushing to the face, stepping outside to bar the knee, resisting
chin pressure, or an eye strike. — thearma.org; academieduello.com wiki. *Medium — secondary-only, not verified
against a primary folio.*

**[MEDIUM — Ott Jud] Forceful arm-grabs + hip throws to disrupt balance early** (offensively-oriented
German/Austrian opening wrestling). — Wikipedia "Ringen"; secondary summary. *Medium — Wiktenauer blocked
(403); no named/numbered plays with page citation retrieved.*

---

## 6. Cross-cutting convergences (multi-source, treat as robust)

1. **Closing measure is a REGIME BOUNDARY, not just a shrinking scalar.** Fiore (Largo/Stretto), Silver
   (true-times), Liechtenauer (Vor/Nach/Indes), and Capoferro (larga/stretta) independently converge: crossing
   into close range makes an entirely different technique repertoire available/unavailable (grapples become
   reachable; half-swording becomes the norm; the long weapon's behind-the-hands length turns from inert into a
   liability). This is genuine cross-source convergence.
2. **The short weapon's success is always attributed to a SPECIFIC PHYSICAL MECHANISM, never abstract "speed."**
   Across every source: footwork voiding the line + closing simultaneously; hand-seizure of a graspable haft; a
   mechanically-favourable near-hilt deflection; the long weapon's own moment of inertia in confined space. This
   argues for grounding any fix in a specific mechanism, not a general multiplier.
3. **The strongest quantitative evidence (fencing-lunge + choking-up/MoI physics) supports things the engine
   ALREADY models** (`at_grip` I_g, `recoverability_factor`'s swing-arrest/thrust-retract blend). No physical
   mechanism was found that is COMPLETELY ABSENT from the existing primitives. The two clearest candidate gaps
   are structural, not missing-mechanism: (a) `commit_depth`/`lunge_depth` are **decoupled from range**; and
   (b) closing is **purely linear with no facing/lateral/circular dimension**, and `dodge` is one uniform mode.
4. **Grabs/pins are consistently OPPORTUNISTIC on a created opening** (bind, beaten-aside weapon, committed
   strike) and produce **BRANCHING outcomes** (Fiore's 4-branch grip). The historically-attested gate for a
   grapple attempt is **state-conditional**, not a standing per-weapon probability.
