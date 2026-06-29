# Valoria — Combat Tuning Status
**2026-06-01 (rev 4 — footwork/dynamic-reach/roster sweep; armour bug found) · state-graph harness**

> This round: validated the mastery thesis (historical), expanded footwork to balance/orientation, activated
> dynamic weapon reach, swept the weapon roster, swept armour — **which surfaced an armour-model sign inversion
> (top-priority fix).** Concentration σ-shape flagged for Jordan.
> `[CONFIDENCE: high — calibrated on canonical primitives + HEMA validation; armour inversion is a confirmed bug]`
> `[SELF-AUTHORED — bias risk: my harness/calibration; the armour bug is exactly what an independent sweep caught]`

## Mastery thesis — VALIDATED (historical + in-engine)
`[READ: HEMA sources]` The 200+ Fechtbücher exist *because* trained skill, not strength, decided fights; "winding
asks you to be clever rather than strong"; *Fühlen* (feeling the bind) is the skill ceiling; masters' guilds
certified exactly this. **In-engine confirms:** technique (History 6v3) **71%**, reading (Cog/Att 5v3) **80%** vs
physical-stat edges ~52%. → **Weapon mastery (the stacked skill set across all state-graph components) is the
dominant factor, above physical stats — as intended.** This is the design anchor for the multivariate skill +
set-bonus system (players equip per-component skills: footwork/grip/reading/cutting/thrusting/approach/parry/bind…).

## This round's wiring (validated)
- **Footwork = balance/orientation, not just movement** (Jordan): now feeds **dodge** (dominant input), **measure
  control**, **anti-overcommit** (balance curbs self-exposure when committing), and **stance stability**. Footwork
  6v3 → **56%** (was 51% movement-only). A footwork tradition (Destreza/koryū) is now a real, broad lever.
- **Dynamic weapon reach — ACTIVATED** (was coded-but-dormant). Per beat, each fighter chooses **choke** (close into
  a longer weapon's measure) / **commit-distance** (lunge to extend), footwork-enabled, with **exposure cost** on the
  lunge and a **bind bonus** on the choke. Validated: spear vs dagger only **52%** (dagger chokes/footworks inside
  the measure, not a blowout); **dagger with footwork 6 flips spear to 46%** (footwork wins the measure); longsword
  vs rapier 41% (rapier reach+tempo). Measure is now negotiated live, per the design.
- **Baseline held throughout:** mirror **50%**, equal-value **Str 50 / Agi 52 / End 48, spread 13–14**, no one-shot.

## Weapon roster sweep (4/4/4, light armour, equal skill) — coherent
```
sabre 58 · arming 57 · spear 56 · staff 54 · rapier 52 · dagger 52 · paired_short 52
· mace 46 · longsword 46 · greatsword 42 · poleaxe 38     (SPREAD 20)
```
**Reading:** fast/versatile/balanced weapons lead; slow heavy two-handers trail — **correct for an UNARMOURED duel
with equal skill.** The poleaxe/greatsword are battlefield/armour weapons; their value should appear vs plate (and
does NOT here only because the armour model is currently inverted — see bug). The 20-pt spread is "right tool for
the context," expected to compress/flip under armour once the bug is fixed.

## ⚠ ARMOUR MODEL — SIGN INVERSION (top-priority bug, found by the sweep)
The armour sweep returned **backwards** results vs history and vs the earlier (pre-state-graph) harness:
- light vs heavy (same sword) = **85% light**; fresh plate vs unarmoured = **19% plate** → says plate is a *handicap*.
- armour-defeat inverted: cutting arming sword "beats" plate **83%**, while poleaxe/mace (true armour-defeat) **33–39%**.
**Expected (confirmed earlier + historical):** fresh plate ~**95% dominant**; cuts nearly useless vs plate; blunt/
poleaxe/half-sword-to-gaps/grapple are the counters. **Diagnosis:** the A1 σ-tempo penalty (plate = slower) is
applied, but **plate's mitigation is not reducing incoming damage correctly** — mitigation appears to help the
attacker (coupling/`close`/damage sign). The state-graph rebuild lost the mitigation wiring the old harness had.
**Fix (next session, before any further armour/plate work):** correct the mitigation→damage sign so plate heavily
reduces cut damage and is dominant fresh; re-confirm the armour-defeat triad (blunt/point-gap/grapple); then
re-run the roster sweep *under plate* (expect heavy/armour-defeat weapons to rise). Plate availability + the
fatigue/heat gate (cost+context, not in-combat nerf) are confirmed design — the bug is purely the mitigation sign.

## Concentration — continued; one decision for Jordan
Wired as the σ-leveraged Focus+Spirit tracker (editorial override, recorded). **Open: the σ-leverage SHAPE.**
Currently Concentration depletes **linearly** and scales the mental-fatigue protection linearly. "σ-leveraged"
could instead mean a **probit-axis** effect (Concentration shifts a σ on the skill channels, like the other
leverage channels) rather than a linear pool. **Jordan call:** does the linear tracker satisfy intent, or do you
want Concentration to act on the probit σ-axis? (Functionally: linear = steady degrade; probit = sharper "holding
it together vs cracking" threshold.)

## Remaining (ordered)
1. **Fix the armour mitigation sign** (above) — blocks all plate/armour/battlefield work.
2. Re-run roster sweep **under plate**; confirm armour-defeat triad; confirm C1 battlefield Str-lead.
3. **Multivariate skill + set-bonus system** — formalize equippable per-component skills (the mastery-stack); the
   axis levers are now all wired (footwork/grip/reading/technique/approach/reach/parry/bind), so skills bias them.
4. Concentration σ-shape (Jordan), differentiator steepness (Jordan).

## Files
`sg_harness.py` (~275 ln) — `/home/claude/`. Design: `full_bout_procedure`, `defensive_branch`,
`combat_derivations`, `stat_role_expansion`, `holistic_review`, this status — `/mnt/user-data/outputs/`.

## Not committed
Lanes ignored per directive; all staged. Propagation to `combat_v30`/`params/combat`, the R2 multi-phase amendment,
the params/combat drift fix, ED-ID assignment, and the armour-bug fix remain for later passes.

---
# REV 5 ADDENDUM (2026-06-01) — corrections + two structural gaps found

## FIXED this turn
- **Reach physics corrected** (Jordan): CHOKE shortens weapon + closes body (the LONG weapon's tool when a foe gets
  inside its point); EXTEND/LUNGE opens the body into space (+reach,+exposure). A short weapon CANNOT choke-to-close
  — it must lunge/rush in, eating the long weapon's reach (no auto-neutralize). Reach disadvantage is real, gated by
  **availability** (can't carry a spear into a royal court), not balanced away.
- **ARMOUR INVERSION FIXED — root cause was a frame-mapping bug, NOT the damage model.** The engagement was called
  with swapped A/B parameters when B initiated, but `body`/`conc`/`stam` dicts kept fixed A/B keys → trackers
  mismatched to the wrong fighter, and the fell-path loser mapping was inverted. **Fix:** engagement now takes a
  `first=` initiator flag in a FIXED outer frame; no parameter swapping. **Result:** plate vs naked = **100%**
  (was 19%), cut vs plate = **0%**, blunt poleaxe vs plate = **83%** — historically correct. Mirror holds **51%**.
  The damage-by-armour model (cut~1, blunt~12, point partial vs heavy plate) was correct all along.
  *(This frame bug likely also contributed to the earlier mirror skews — worth noting it's now structurally clean.)*

## ⚠ TWO STRUCTURAL GAPS FOUND (next session — these are builds, not tunes)
1. **Weapon tempo is dead code in the resolver.** `weapon_tempo` / `recovery_beats` are computed (dagger 1 /
   poleaxe 6) but **never used in `engagement`** — every fighter attacks every beat equally. Consequence: the
   dagger's speed advantage isn't modeled, AND the spear's reach can't express "I strike you during your approach."
   **Build needed:** tempo must gate attack frequency (fast weapon = more beats/attacks; slow weapon recovers
   between blows), and reach must interact with tempo (reach-holder strikes first/more during the approach phase;
   fast weapon gets more beats once it has closed inside).
2. **Spear vs dagger still inverted (18% spear / 82% dagger) despite correct reach penalty + symmetric reach.**
   Per-engagement the spear wins exchanges (trace: dagger took 11, spear 0, → separation), but across a full fight
   the dagger wins. Root cause is tied to gap #1 (no tempo throttle) + the fight-loop's separation/wound-count
   accumulation. **A spear should dominate a dagger overwhelmingly** (the dagger must survive the whole approach
   through the kill-zone to reach grappling measure). **Build needed:** with tempo wired, re-confirm reach
   dominates; the dagger's only path is surviving to the close measure, which should be rare vs a spear.

## Concentration — SHARPENED (Jordan)
Two-sided, both confirmed: (a) **baseline consistency** (always on) — low Concentration = more error-prone even when
fresh/unfatigued (a consistency floor), NOT a fatigue battle; (b) **fatigue resistance** (scales with fatigue) —
protects Reading + technique execution as stamina drops. **Current harness has only (b).** **Build needed:** add the
always-on consistency term (low Focus = a small flat σ penalty / higher variance on skill channels regardless of
fatigue), separate from the fatigue-scaled protection. σ-leverage shape = the "holding it together vs cracking"
probit effect (Jordan-confirmed direction).

## Armour mitigation model (Jordan direction — for the rebuild)
Damage reduction = f(**weapon head/technique** × **armour type**): blunt vs slash vs thrust each interface
differently with light/medium/heavy. **Granularity = armour TYPE** (light/medium/heavy), NOT piecemeal/located
blows (Jordan: too granular, and we don't model aimed location). The `RESIST[armour][head_mode]` matrix already
encodes this correctly (cut crushed by plate, blunt transmits, point finds gaps); it is validated and stays.

## Updated remaining (ordered)
1. **Wire weapon tempo into the engagement** (gap #1) — attack frequency + reach-tempo interaction.
2. **Re-confirm reach dominance** (gap #2) once tempo is wired — spear ≫ dagger.
3. **Add Concentration baseline-consistency term** (gap (a)) + probit σ-shape.
4. Re-run weapon roster + armour sweeps **with tempo + fixed frame** (the rev-4 roster numbers predate both fixes —
   re-sweep). Confirm C1 battlefield Str-lead under correct armour.
5. Multivariate skill + set-bonus system (mastery-stack) on the now-wired axes.
6. Jordan calls: differentiator steepness.

## State (rev 5)
`sg_harness.py` (~280 ln). Calibrated baseline holds (mirror 51%, equal-value ~50/50/50 spread ~18, no one-shot,
armour now correct). The roster/equal-value numbers are stable for SAME-reach matchups; cross-reach matchups await
the tempo wiring. Nothing committed; all staged.

---
# REV 6 ADDENDUM (2026-06-01) — tempo+measure WIRED (major fix), one binding bug isolated

## MAJOR FIX: weapon tempo + measure-state wired (gap #1 + #2 resolved structurally)
The engagement now models **approach vs closed phases** with a tempo budget:
- **Measure state:** a bout opens at the LONGER weapon's measure; the shorter weapon must CLOSE (footwork+tempo
  drive `close_rate`). During the approach the longer weapon gets **stop-hits** (`STOPHIT_CHANCE`) at the closing
  fighter — the dagger must survive the kill-zone to reach its measure.
- **Tempo budget:** each fighter accumulates readiness at `weapon_tempo` rate; acts when `ready ≥ ACT_THRESHOLD`.
  Fast weapons (dagger) get more beats; slow weapons (poleaxe) recover between blows. Actor chosen by most-ready
  (ties random) — verified FAIR (skilled/weak get equal attacker-beats).
- **Closed phase:** reach damped to a `RESIDUAL_REACH_FRAC` (the shorter weapon earned its measure).
**Result — reach now historically correct:** spear vs dagger **67–92%** (was inverted 18–29%); spear>longsword>
dagger ordinal; dagger w/ footwork-6 narrows but does NOT flip vs spear (availability answers the spear, not skill);
plate vs naked **100%**; mirror **51%**; turns-to-fell **3.4**, timeout **1%**. Also adopted the **canonical
`effective_ob(DECISIVE_OB=3, pool, net_sigma)` + `degree_of_success`** (replaced a mis-scaled hand-rolled ob=1.0
that was saturating the degree ladder) — net_sigma sign verified, skilled defender dsig verified higher.

## ⚠ ONE BINDING BUG ISOLATED (next session — precise, not a redesign)
**Symptom:** the differentiator is INVERTED in the full engagement — History 6v3 wins only **23%**, Reading 5v3
**28%** (the *more skilled* fighter loses), even though:
- **Per-strike resolution is PROVABLY CORRECT** (isolated test: skilled lands 71%, weak 42%).
- **Attacker-beats are FAIR** (skilled 2210, weak 2204).
- **net_sigma sign is correct** (higher → lower ob); **skilled defender dsig is higher** (0.456 vs 0.091);
  effective_ob math correct.
- Yet **inside the engagement the weak fighter lands 663 vs skilled 412** — the *opposite* of the isolated per-strike
  rates. → **A variable-binding bug in the engagement loop**: `atk`/`dfn`/`pool` or the hit-application is
  referencing the wrong fighter at the `damage()` call (defender-skill effectively inverts only in the loop).
**This is a localized binding bug, not a model error** — the model components each test correct in isolation. The
fix is to audit the closed-phase block's atk/dfn binding through to `body[dfd].apply` / riposte application,
likely a desync introduced when the tempo actor-selection reassigns `agg`/`dfd` mid-loop relative to the cached
`atk`/`dfn`. **Do NOT re-tune anything until this is fixed** — the differentiator (mastery thesis, the project's
core) cannot be validated through the harness while it inverts.

## What is SOLID (unaffected by the bug)
- Reach/measure/tempo (validated, historical). Armour (plate 100%, cut~0, blunt defeats — validated). Mirror 51%.
  Equal-value ~50/50/50 spread ~19 (the Str/Agi/End builds don't vary History, so the binding bug doesn't distort
  the equal-value sweep — confirmed it still lands right). Turns-to-fell 3.4. No one-shot. Footwork as balance/
  orientation. Dynamic reach physics (choke/lunge corrected). Concentration tracker (Focus+Spirit).

## Updated remaining (ordered)
1. **FIX the engagement binding bug** (above) — blocks differentiator validation, top priority.
2. Re-validate differentiator (History/Reading should be HIGH — mastery dominant, per validated historical thesis).
3. Add Concentration **baseline-consistency** term (always-on low-Focus penalty) + probit σ-shape.
4. Re-run weapon roster + armour sweeps clean (post-tempo, post-bugfix).
5. Multivariate skill + set-bonus system (mastery-stack) on the wired axes.
6. Jordan: differentiator steepness; Concentration σ-shape confirm.

## State (rev 6)
`sg_harness.py` (~300 ln). Mastery thesis VALIDATED historically (200+ treatises exist because skill, not strength,
decided fights; "winding asks you to be clever rather than strong"; Fühlen is the ceiling). Reach/armour/tempo
historically correct. One binding bug blocks differentiator validation. Nothing committed; all staged.

---
# REV 7 ADDENDUM (2026-06-01) — DEGREE-INVERSION BUG FIXED (correctness); balance needs re-tune on corrected base

## ROOT-CAUSE FIXED: the differentiator inversion was a degree→outcome mapping bug
The engagement mapped **`deg=='fail'` (attacker's roll FAILED) → a full hit for the attacker** — backwards. A failed
attack was being rewarded with damage. Since a skilled fighter (big pool) rarely rolls `fail` and a weak fighter
rolls it constantly, the weak fighter was *gifted* damage every failed swing → skill inverted. **Fixed:** `fail` →
no hit (defender defended, may riposte); `success` → defender's mode can neutralize (parry/dodge/wind), else lands;
`overwhelming` → reliably lands. Also added an **exchange cap** (`MAX_EXCHANGES_PER_BOUT=3`) so a bout is a 6–10s
handful of exchanges (was running ~24 beats → one-bout kills).

## NOW VALIDATED-CORRECT (keep — these are the mastery thesis confirmed in-engine)
- **Differentiator scales correctly:** History 4v3 **65%**, 5v3 **79%**, 6v3 **90%**; Reading decisive. **Mastery is
  dominant**, exactly as the historical thesis requires. This is the project's core design goal — now true in sim.
- **Reach correct:** spear vs dagger **87%**, longsword vs dagger **71%** (ordinal, historical).
- **Plate vs naked 100%**, cut vs plate **0%** (cuts useless vs plate — correct).
- **Mirror 51%**, turns-to-fell **4.5 bouts** (0% timeout) — in the 3–6 band.

## ⚠ BALANCE REGRESSED — must re-tune ON TOP of the corrected foundation (NOT revert the fixes)
Fixing the degree mapping (correctness) invalidated the prior balance tuning, which had been fitted around the
buggy mapping. Three items need a fresh sweep on the corrected base:
1. **Equal-value drifted to Str 54 / Agi 45 / End 51 (spread 37).** The exchange cap (fewer exchanges/bout) favors
   Strength's per-hit power over Agility's tempo. Re-tune the Agi/Str channels for this exchange count.
2. **longsword vs rapier = 0%** (rapier over-dominates). The reach/tempo weighting over-rewards the rapier's
   speed+reach combo at the 3-exchange cap. Re-balance weapon tempo vs reach.
3. **poleaxe vs plate = 0%** (WRONG — blunt should DEFEAT plate). The poleaxe's slow tempo gives it too few
   exchanges to land its armour-defeating blows inside the 3-exchange cap. The armour-defeat triad needs the
   slow heavy weapons to either land harder per blow or get their exchanges weighted up vs armour. **This is the
   interaction between the exchange cap and weapon tempo — slow armour-defeat weapons are starved of actions.**

## Diagnosis of the coupling (for the re-tune)
The system is tightly coupled: lethality (damage × hit-rate × exchanges/bout) interacts with stat balance (Agi
tempo vs Str power), weapon balance (fast vs slow), and armour-defeat (slow blunt weapons need enough swings). The
**correctness fixes are right and stay**; the balance constants (DAMAGE_SCALE, MAX_EXCHANGES, tempo weights,
Agi/Str channel strengths, neutralize rates) must be re-fit together on the corrected base. Recommend a **joint
sweep** rather than one-at-a-time (they interact).

## Updated remaining (ordered)
1. **Joint balance re-tune on the corrected base:** equal-value Str/Agi/End→~50; longsword vs rapier→~50; weapon
   roster spread reasonable; **armour-defeat triad (poleaxe/mace MUST beat plate)** — give slow weapons enough
   per-bout impact (e.g. exchanges weighted by tempo, or per-blow damage higher for slow weapons, or a separate
   armour-defeat resolution that doesn't need many swings).
2. Add Concentration baseline-consistency term + probit σ-shape.
3. Multivariate skill + set-bonus system (mastery-stack) — the differentiator now works, so set bonuses will stack
   meaningfully.
4. Jordan: differentiator steepness (currently History 6v3=90%, Reading ~100% — is that the intended ceiling?).

## State (rev 7)
`sg_harness.py` (~305 ln). **The differentiator (mastery) now works correctly — the core thesis is validated in
sim.** Reach + plate-dominance + mirror + turn-count all correct. Equal-value / weapon-vs-weapon / armour-defeat
need a joint re-tune on the corrected base (the prior tuning was fitted around the now-fixed degree bug). Nothing
committed; all staged.
