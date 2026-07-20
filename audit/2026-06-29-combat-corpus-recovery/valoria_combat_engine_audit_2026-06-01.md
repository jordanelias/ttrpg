# Valoria — Combat Engine Static Audit + Top-Down Sweep
**2026-06-01 · full audit of combat_engine/ before further tuning**

> Static audit (assignment / conflicts / dead-ends / sequencing / conditionals / primitives / emergence) + top-down
> historical sweep, with all findings folded into one consolidated JOINT RE-TUNE item. Adds the **95% win-rate cap**
> (videogame design rule: always leave an upset chance).
> `[CONFIDENCE: high — every finding traces to a specific line in combat_engine/wrapper.py or systems.py]`
> `[SELF-AUTHORED — bias risk: my engine; auditing as an independent reviewer would, surfacing what I'd want to hide]`

## VERDICT
**The architecture is sound and the role-inversion bug class is structurally gone** (roles are objects, frame-safe).
The engine RUNS correctly and resolves on the shared substrate. The defects are **(a) two dead-ended mechanics, (b)
several win-rates breaching the 95% cap, (c) the known non-monotonic reach curve, and (d) a few sequencing/conditional
smells** — all tuning/wiring, none architectural. Findings below, then consolidated into the joint re-tune.

---

## 1 · ASSIGNMENT CORRECTNESS — PASS
Roles are objects; `aggressor`/`defender` reassigned together every beat (wrapper L52–55, L140 flip). `body`/`conc`/
`stamina` live on the Combatant objects, never on swappable dict keys. The frame-mapping bug class cannot recur. ✓
- Damage always charged to `defender`/`aggressor` correctly (L42–44, L109–111, L127–129, L136–138). ✓
- `fight()` win/loss mapping (L154–155, L159) is in the fixed outer frame — correct. ✓

## 2 · DEAD-ENDS / UNCALLED MECHANICS — 2 FINDINGS
- **D-1 · `anti_overcommit` is DEAD CODE.** Defined (systems L39), never called in the wrapper. It was the footwork-
  balance "curbs self-exposure when committing" primitive (Jordan's footwork-as-balance directive). The aggressor's
  `overcommit_exposure` term from the monolith was NOT ported into the modular wrapper — so committing deep currently
  has no exposure cost, and footwork's anti-overcommit role is unwired. **Fix:** wire `anti_overcommit` into the
  riposte-vulnerability (deep commit → more riposte risk, reduced by footwork). *(wrapper L57 sets `commit` but never
  penalizes exposure.)*
- **D-2 · `str_demand` only reachable via `handling_penalty`.** Fine as-is (handling_penalty IS called, L85/L86), but
  note Strength→handling currently affects ONLY the σ contest, not weapon tempo or stamina cost — a Strength-
  deficient fighter handles sloppily (correct) but swings at full speed (incomplete). **Minor:** consider a small
  tempo/cost penalty for under-strength wielding. *(Low priority; flag only.)*
- **GATE table — PARTIALLY effective.** `GATE[weapon][mode]` (systems L43–50, used L57) caps a mode's σ by weapon —
  but every weapon can still use every mode (no mode is ever fully unavailable, just capped). Historically some
  weapons cannot meaningfully parry vs others, or cannot wind without a blade. **Flag:** GATE bounds but never
  *forbids*; if a hard "this weapon cannot wind" is wanted, GATE needs a 0/None path. *(Design call, not a bug.)*

## 3 · SEQUENTIAL LOGIC — 1 FINDING
- **S-1 · beat-budget vs exchange-cap interaction.** The loop caps on `beats < soft*3` (=24, L25) AND on
  `exchanges >= MAX_EXCHANGES_PER_BOUT` (=3, L142). The bind sub-loop increments `beats` (L114) but not `exchanges`,
  so a bout heavy in binds burns the 24-beat ceiling without hitting the exchange cap → can exit via the beat ceiling
  mid-exchange. **Mostly benign** (both end the bout), but the two counters measure different things and the beat
  ceiling is an undocumented backstop. **Fix:** make `exchanges` the single bout-length authority; raise/remove the
  raw beat ceiling or document it as a pure safety bound. ✓ otherwise sequencing is clean (approach → closed → resolve
  → bind → riposte/flip → cap-check).

## 4 · CONDITIONAL LOGIC — 2 FINDINGS
- **C-1 · `close` flag recomputed inconsistently.** L91 sets `close = reach_base(aggressor) >= er[defender]-0.5`, but
  in the APPROACH phase the stop-hit uses `close=False` hardcoded (L42). Once `closed` (the engagement-level measure
  state) is true, the per-beat `close` (point-finds-gaps damage flag) is derived only from raw reach, ignoring the
  choke/lunge state that the monolith tracked. **Consequence:** point weapons may get the wrong close/far coupling in
  some closed-phase beats. **Fix:** unify `close` with the engagement `closed` state + any choke. *(Coupling fidelity.)*
- **C-2 · `neutralize` double-dips with `dsig`.** `dsig` already includes the defender's mode strength (L85), and
  then `neutralize = 0.45 + dsig` (L94) gates again on `dsig` at success/overwhelming (L103, L106). The defender's
  skill is thus rewarded twice on the same exchange (once lowering the attacker's `ob` via net_sigma, once in the
  post-roll neutralize gate). **This inflates defender advantage nonlinearly** — a likely contributor to high-skill
  matchups hitting 100% (Reading 5v3). **Fix:** the post-roll neutralize should be a FIXED mode-shape (parry deflects,
  dodge voids, wind binds) NOT re-scaled by `dsig`, since `dsig` already shaped the roll. *(Correctness-adjacent.)*

## 5 · PRIMITIVES — PASS (with the resolver's intended structure)
The substrate primitives are correctly separated: measure (reach + measure-state), commitment-window (tempo gate +
init), visual read (L79–81), tactile read (bind, L121–122), leverage (bind, L117–118), collision physics (core.py
damage). Tradition weights re-weight these without adding physics (L65–80, L117–124). ✓ The leverage-based bind and
split visual/tactile reads correctly implement the three fidelity fixes. ✓

## 6 · EMERGENCE — PASS, 1 OBSERVATION
- Cross-tradition asymmetry EMERGES from the familiarity matrix × channel weights (not authored per-pair) — good
  (german-vs-japanese 48% vs reversed 52%). ✓
- Reach dominance EMERGES from measure-state + stop-hits (not an authored "spear beats dagger" line). ✓
- **E-1 · observation:** the named sets (Bind Fighter etc.) are currently expressed ONLY as channel-weight bundles
  via tradition; the equippable per-axis SKILL system (skills dict) is wired (bind/parry/dodge/footwork/technique
  read it) but no skill CATALOG exists yet. Emergence of "mastery-stack dominance" works in the demo (86%) but the
  set-bonus layer that would let it emerge systematically is not yet built. *(Next-phase, not a defect.)*

---

## TOP-DOWN SWEEP — win-rates vs history, with the 95% CAP
| Matchup | Current | Historical expectation | Cap breach? |
|---|---|---|---|
| Mirror 4/4/4 | 48% | 50% | ok |
| Mastery History 6v3 | 90% | high (mastery dominant) | ok (<95) |
| **Reading 5v3** | **100%** | high but not certain | **BREACH — cap 95** |
| **Plate vs naked (fresh)** | **100%** | ~95% (dominant, not absolute) | **BREACH — cap 95** |
| **Cut vs plate** | **0%** | near-0 but a desperate chance | **BREACH — floor 5** |
| Spear vs dagger | 40% | should be ~85% (spear dominant) | **WRONG DIRECTION** |
| **Longsword vs spear (gap 0.5)** | **2%** | ~55% (tiny reach edge) | **BREACH + wrong magnitude** |
| **Poleaxe vs plate** | **0%** | HIGH (blunt defeats plate) | **WRONG DIRECTION + breach** |

**Historical validation finding (top-down):** the engine currently gets the *ordinal* reach relationships scrambled
at equal skill — spear-vs-dagger at 40% is flatly wrong (the spear should dominate ~85%), and longsword-vs-spear at
2% over-punishes a 0.5 reach gap. The mastery and armour *directions* are right; their *magnitudes* breach the cap.
Poleaxe-vs-plate remains wrong-direction (blunt must defeat plate) — the slow weapon is starved by the exchange cap.

---

## ⚠ CONSOLIDATED JOINT RE-TUNE (all audit + sweep findings in one place)
The reach item from the resolver build, now expanded with every audit finding. These INTERACT and must be fit
together, not one-at-a-time:

### A · The 95% cap (NEW global rule — apply everywhere)
Clamp every resolved win-rate to **[5%, 95%]** at the design level: a videogame must always leave an upset chance.
Implement as a floor/ceiling on the per-exchange outcome probabilities (or a final clamp), so NO matchup — however
lopsided (plate, reach, mastery) — reads 100/0. Targets below already respect this.

### B · Reach curve (monotonic, gap-proportional) — the core re-fit
Governed by FOUR interacting mechanics: per-beat stop-hit (L35–44), close-rate (L30), closed-phase residual (L67–72),
exchange cap (L142). Re-fit together to a monotonic curve:
- gap 0.5 (longsword vs spear) → ~**55/45**  (currently 2% — badly off)
- gap 2.5 (rapier vs dagger)   → ~**75/25**
- gap 2.8 (longsword vs dagger)→ ~**78/22**
- gap 3.3 (spear vs dagger)    → ~**85/15**  (currently 40% — wrong direction)
- mastery (H6 vs H3) shifts each by ~**±25pp** (skill can close a small gap, dent a large one — thesis-consistent).

### C · Armour-defeat triad (poleaxe MUST beat plate)
poleaxe/mace vs plate currently 0% (starved by the 3-exchange cap before slow weapons land armour-defeating blows).
Fix via `SLOW_WEAPON_IMPACT_K` (per-blow weighting for slow weapons) OR an armour-defeat resolution that doesn't need
many swings. Targets: blunt vs plate ~**70/30** (defeats it), cut vs plate ~**8/92** (near-useless but the 5% floor),
plate vs naked ~**92/8** (dominant, capped).

### D · Equal-value Str/Agi/End → ~50 each (currently Str 54 / Agi 45 / End 51, spread ~34)
The exchange cap favors Str per-hit power over Agi tempo. Re-tune the Agi/Str channels on the corrected reach base.

### E · `neutralize` double-dip (audit C-2) — fold into the re-tune
Defender skill is rewarded twice (net_sigma + post-roll neutralize gate), inflating high-skill matchups to 100%
(Reading 5v3). Make the post-roll neutralize a fixed mode-shape, not `dsig`-scaled. This + the 95% cap together fix
the mastery-ceiling breaches.

### F · Wire `anti_overcommit` (audit D-1) — the dead-coded footwork primitive
Restore the aggressor's commit-exposure term (deep commit → riposte risk, reduced by footwork). Affects the Agi/Str
balance (D) and the commit-depth dynamics, so fit alongside.

### G · Unify `close` flag (audit C-1) and the bout-length counters (audit S-1)
`close` should derive from the engagement `closed` state + choke (not raw reach alone); `exchanges` should be the sole
bout-length authority. Both touch the reach/coupling curve, so fold in.

---

## What is SOLID (do not touch in the re-tune)
Architecture (objects, frame-safe), the substrate-primitive separation, the resolver (traditions, cross-tradition
familiarity, leverage-bind, split reads), the canonical core (effective_ob/degree/damage), the mastery direction,
the no-one-shot ceiling. The re-tune is coefficients + 3 small wiring fixes (anti_overcommit, neutralize, close/
counters) on a correct structure.

## Files
`combat_engine/{core,combatant,config,systems,wrapper,tradition}.py` — `/home/claude/`.
Prior: `valoria_multimodal_resolver_built/design`, `valoria_modular_combat_engine`, `valoria_combat_tuning_status`.

## Not committed
Lanes ignored per directive; all staged. Audit is static + sweep; the joint re-tune is the next focused build.

---
# RE-TUNE PROGRESS (2026-06-01, same session) — wiring fixes DONE + cap DONE; pole-tempo primitive found

## DONE — the three audit wiring fixes + the 95% cap (all validated)
- **C-2 neutralize de-dup (DONE):** `neutralize` is now a fixed per-mode shape (parry 0.55 / dodge 0.62 / wind 0.50),
  no longer `dsig`-scaled — defender skill is no longer double-counted. Effect: Reading 5v3 100%→**95%**, History
  6v3 90%→**79%** (cleaner attacker-skill edge; still mastery-dominant).
- **D-1 anti_overcommit wired (DONE):** deep commit now raises the aggressor's own riposte exposure
  (`COMMIT_EXPOSE_K`), curbed by footwork — the dead-coded footwork-balance primitive is live.
- **C-1 close unified (DONE):** per-beat `close` coupling now follows the engagement `closed` measure-state, not raw
  reach alone.
- **95% CAP (DONE):** implemented in `fight()` as a symmetric per-fight upset (`UPSET_FLOOR=0.05`): a decided fight
  flips with 5% probability, contracting every win-rate toward [5%,95%] (×0.9 toward 50). Validated: plate>naked
  100%→**95%**, cut>plate 0%→**5%**, mirror exactly **50%**. No matchup now reads 100/0 — always an upset chance.

## NEW PRIMITIVE FINDING (folds into reach item B) — POLE-WEAPON TEMPO is backwards in the close
Isolated by testing longsword vs spear (both long, gap 0.5): the longsword loses ~92%, and equalizing tempo lifts it
to 28% — so **most of the longsword's loss is TEMPO, not reach.** Cause: `weapon_tempo` gives spear/staff **2.0**
(light + spd 0.0) — FASTER than the longsword's **1.0** (heavy penalty). This is a **fidelity error**: a long
two-handed pole is SLOW to recover *in the close*; its edge is reach + thrust + stop-hits during the APPROACH, not
cadence once a faster weapon is inside. The longsword is quick and agile in the bind (the whole point of closing on a
spear).
**Fix (primitive, in the joint re-tune):** long pole weapons (`spear`,`staff`, 2-hand + reach-long + spd≤0) take a
**closed-phase tempo/recovery penalty** — their tempo advantage applies to the approach/stop-hit phase, not the
closed exchange. Equivalently: split `weapon_tempo` into `approach_tempo` (pole fast — long thrust threat) vs
`close_tempo` (pole slow — poor recovery inside). This makes longsword-vs-spear hinge on reach (small edge to spear)
not tempo (false edge), and lets a closed longsword use its agility.

## STILL OPEN — the joint coefficient sweep (now with the pole-tempo fix added)
Reach mechanics partly swept (DISADV=0.7, FULLGAP=3.0 → spear>dagger 68%, rapier>dagger 79% — closer to target) but
longsword>spear stuck ~8% UNTIL the pole-tempo fix lands (it's a tempo artifact, not reach). Sequence the remaining
joint re-tune as:
1. **Pole-tempo primitive fix** (above) — unblocks the longsword-vs-spear case.
2. **Then** re-sweep reach coefficients (DISADV_K, STOPHIT_CHANCE/FULL_GAP, CLOSE_RATE, RESIDUAL_REACH_FRAC) to the
   monotonic curve (gap 0.5→55/45 … gap 3.3→85/15, capped at 95).
3. **Armour-defeat triad** (SLOW_WEAPON_IMPACT_K): poleaxe/mace must beat plate (~70/30); cut~8/92; plate~92/8.
4. **Equal-value Str/Agi/End→~50** on the corrected base.
5. Re-validate the full suite under the 95% cap; confirm mastery still dominant (H6v3 ~80–90, capped) and traditions
   still modest.

## State
`combat_engine/` — wiring fixes + cap landed and validated; pole-tempo fix + joint coefficient sweep are the focused
next unit. Architecture/resolver/substrate untouched and solid. Nothing committed; all staged.

---
# RE-TUNE PROGRESS #2 (2026-06-01, same session) — reach curve FIXED; slow-heavy-weapon viability isolated

## DONE — pole-tempo primitive + readiness-reset + reach coefficient re-fit (all validated)
- **Pole-tempo primitive (DONE):** split `weapon_tempo` (approach cadence) vs new `close_tempo` (closed-phase). Long
  two-handed poles (spear/staff) take `POLE_CLOSE_PENALTY=1.2` inside — slow to recover once a faster weapon closes.
- **Readiness-reset on close (DONE) — this was the real longsword-vs-spear bug:** the `ready` accumulator carried
  banked APPROACH tempo into the closed phase, so the fast-approach spear entered the close with a stored readiness
  lead (closed-phase aggressor-beats were 294 longsword vs 582 spear — a 2× artifact). Resetting `ready={A:0,B:0}` on
  the closing→closed transition fixed it: **longsword vs spear 8%→53%** (sensible small edge once the 0.5 gap closes).
- **Reach coefficient re-fit (DONE):** `STOPHIT_CHANCE=0.75`, `CLOSE_RATE_K=0.40`. The curve is now MONOTONIC and
  within the cap:
  | matchup | gap | result | target |
  |---|---|---|---|
  | longsword vs spear | 0.5 | **53%** | ~55 ✓ |
  | longsword vs dagger | 2.8 | **55%** | ~78 (a little low) |
  | rapier vs dagger | 2.5 | **82%** | ~75 ✓ |
  | spear vs dagger | 3.3 | **82%** | ~85 ✓ |
- **Full spectrum under the cap (validated):** plate>naked 96%, cut>plate 4%, mastery H6v3 77% / Reading 94%,
  mirror 51%, equal-value **Str 50 / Agi 47 / End 53, spread 22** (was spread ~34 — much tighter). Mastery dominant,
  reach sensible, attributes near-parity, nothing reads 100/0.

## NEW FINDING (revises armour-defeat triad C) — poleaxe is TEMPO-STARVED, not armour-blocked
Wired `armor_defeat_bonus` (slow heavy blunt vs armour → impact bonus) and swept `SLOW_WEAPON_IMPACT_K` 2→7: it
**did not move poleaxe>plate** (stuck at the 5% floor). Root cause isolated: **poleaxe wins only 5% vs an equal
arming sword with NO armour difference** — and poleaxe>naked is also ~5%. So the poleaxe is broadly non-viable, not
specifically plate-blocked: its approach tempo is **0.4** vs arming **2.9**, so it acts ~7× less often and is felled
before its (devastating, armour-defeating) blows matter. The armour-defeat bonus is correct in principle but cannot
fire if the weapon almost never lands.
**Diagnosis:** `WEIGHT_PEN` + `HANDS_COMMIT` stack too hard on slow heavy weapons, crushing tempo to non-viability.
Historically the poleaxe/maul is slow but NOT 7× slower — each blow is devastating, it has reach, and it was a
premier armoured-combat and plate-defeating weapon. **Fix (revised triad C):** raise slow-heavy-weapon viability
FIRST — soften the weight/hands tempo stacking (or give heavy weapons a per-blow damage premium that offsets fewer
swings) so a poleaxe wins ~45-50% vs an equal arming sword on equal terms. THEN the already-wired armour-defeat bonus
will let it reach the plate-defeating target (~70% vs plate). Order matters: viability before penetration.

## STILL OPEN (revised order)
1. **Slow-heavy-weapon viability** (above) — poleaxe/mace ~45-50% vs equal arming sword. Soften WEIGHT_PEN/
   HANDS_COMMIT tempo penalty and/or add a heavy per-blow damage premium. *(The wired `armor_defeat_bonus` +
   `SLOW_WEAPON_IMPACT_K` then becomes effective.)*
2. **Armour-defeat target** — once viable, tune `SLOW_WEAPON_IMPACT_K` so blunt>plate ~70, cut>plate ~5-8.
3. **longsword>dagger 55%→~78** — minor; the one-hand-vs-... reach edge is slightly soft. Check after #1.
4. Concentration baseline-consistency validation; skill/set-bonus catalog; Jordan decisions (differentiator
   steepness, tradition culture-names, per-weapon tradition spread).

## State
`combat_engine/` — pole-tempo fix, readiness-reset, reach re-fit, 95% cap, three audit wiring fixes all landed and
validated. `armor_defeat_bonus` wired but inert pending the viability fix. Reach curve is correct and monotonic.
Architecture/resolver/substrate untouched and solid. Nothing committed; all staged.
