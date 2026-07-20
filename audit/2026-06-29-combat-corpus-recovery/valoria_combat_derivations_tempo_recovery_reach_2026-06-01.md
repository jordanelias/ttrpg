# Valoria — Combat Derivations: Tempo · Recovery · Reach-Cost
**Class-C proposal · 2026-06-01 · clean-slate combat rebuild**

> Derives the three quantities Jordan flagged as *computed, not free seeds* — per-weapon **tempo / blow-cap**,
> **inter-bout stamina recovery**, and **commit / choke / exposure** — bottom-up from the canonical weapon
> axis-vectors (`weapon_axes_v2 §5`: reach·weight·hands·head·speed·handling) and the ratified Stamina/σ engine,
> validated top-down against historical fencing reality.
> `[READ: weapon_axes_v2.md §2/§5 — full; ratified S1 stamina, ST1, A1/D1 — this session]`
> `[CONFIDENCE: high on form (built on canonical vectors); coefficients are tunable seeds pending the rebuilt harness]`
> Mechanical-tier · Jordan-vetoable · not committed.

## Canonical primitives used (from `weapon_axes_v2 §5`)
Each weapon is a vector: **reach** (short/long → continuous, §A), **weight** (light/heavy), **hands** (1H/2H),
**head** (point / cut-and-thrust / straight-cut / curved-cut / blunt), **speed** (−0.5 … 3.0 scalar),
**handling** (Forgiving/Standard/Demanding). Plus character **grip** and **footwork**, and **Stamina = 3·End+2·Spr** (S1).

Representative speed anchors (canonical): dagger 3.0 · paired-short 2.5 · sabre 2.0 · messer 1.8 · rapier/arming/
sidesword 1.5 · estoc/curved-2H/mace 1.0 · longsword 0.5 · greatsword/spear/staff 0.0 · poleaxe/war-hammer −0.5.

---

## A · Continuous reach (the substrate for §6b)
Replace the short/long band with a scalar `reach_base`, **derived** from the vector so it reproduces the band ordering:

```
reach_base = L0
           + LONG_BONUS·[reach=long]          # long vs short is the dominant term
           + HANDS_BONUS·[hands=2H]            # 2H extends effective reach
           + HEAD_REACH[head]                  # point > cut-and-thrust > blunt (thrust reaches furthest)
```
`HEAD_REACH`: point > straight/curved-cut ≈ cut-and-thrust > blunt. So spear (long·2H·point) and estoc sit longest;
dagger/paired-short (short·1H) shortest; longsword mid-long. *(L0, LONG_BONUS, HANDS_BONUS, HEAD_REACH = seeds; the
ordering they must reproduce is fixed by the roster.)*

**Effective reach each beat** = `reach_base − choke_amount + commit_extension` (§D).
**Top-down:** matches real measure — a spear outreaches a dagger by a lot, a thrust outreaches a cut from the same
blade, two hands and a lunge extend you, choking up shortens you.

---

## B · Tempo / blow-cap (soft cap + per-weapon)
Two coupled quantities: how *fast* a weapon can throw/recover a blow, and the *soft cap* on blows in one 6–10 s engagement.

```
weapon_tempo   = BASE_TEMPO + speed·SPEED_K            # canonical speed scalar is the spine
               − WEIGHT_PEN·[weight=heavy]             # heavy = slower throw + weight-shift recovery
               − HANDS_COMMIT·[hands=2H]·[weight=heavy] # 2H heavy = most committed (poleaxe)
recovery_beats = ceil(BLOW_COST / weapon_tempo)        # beats to recover before the next blow
```
- **Light, fast weapons chain** (dagger 3.0, paired-short 2.5, sabre 2.0): `recovery_beats ≈ 1` — attack, recover,
  attack again within the engagement.
- **Heavy, committed weapons** (poleaxe −0.5, greatsword 0.0): `recovery_beats ≥ 2–3` — each blow demands weight-shift;
  a miss or parry leaves a long recovery window (the historical "committed swing" vulnerability).

```
soft_blow_cap(engagement) = min( TEMPO_CAP ,           # the soft ceiling on tempo beats per 6–10 s
                                 stamina_remaining / action_cost ,   # gas out first if low
                                 until felled / disengage )
```
**Soft, not hard:** exceeding `TEMPO_CAP` is possible but each extra blow past it takes an escalating stamina /
control penalty (frenzy has a cost). **Top-down:** a 6–10 s exchange historically lands a handful of real attempts,
not dozens; light weapons get more attempts, heavy weapons fewer but heavier.

---

## C · Inter-bout recovery (computed from stamina)
Between bouts, fighters reset footing and recover **part** of spent stamina — a fraction of the deficit, capped, and
**better for high-Endurance/Spirit fighters** (S1 conditioning):

```
recover = RECOVERY_FRAC · (stamina_max − stamina_now)        # fraction of the deficit
        · conditioning,   conditioning = stamina_max / STAMINA_REF   # End/Spr-scaled (S1)
stamina_now ← min(stamina_max, stamina_now + recover)
```
Never full (a bout always costs net stamina over a fight); the **conditioned fighter recovers more between bouts**,
so across a multi-bout fight stamina trends down faster for the unconditioned → they gas, lose initiative, get pressed
(the across-bouts stamina-press from the session work, now with a recovery term). **Top-down:** fighters do catch
breath in the lull between exchanges, and the fitter man recovers more — but neither resets to fresh.

---

## D · Commit / choke / exposure (computed from primitives)
The live range modifiers and their costs, from grip · footwork · weapon vector:

```
choke_amount     = CHOKE_K · grip_skill · choke_capacity(weapon)
   choke_capacity ↑ with haft length: 2H pole/staff/longsword choke a lot; dagger/rapier almost none
choke_penalty    = leverage/reach lost when choked  (a choked weapon fights short — trades its reach game)

commit_extension = COMMIT_K · footwork_skill · lunge_capacity(weapon)
   lunge_capacity ↑ for point heads + light weight (rapier lunge); ↓ for heavy/blunt
exposure_cost    = EXPOSE_K · commit_extension · (1 + WEIGHT_EXPOSE·[weight=heavy])
                 / footwork_skill          # better footwork recovers the lunge → less exposure
   → exposure raises the fighter's own effective_ob (σ penalty) on the next beat: committing distance opens you up
```
**Contact-area / head term:** the **head** and **amount of possible contact by head** set how much a committed blow
exposes — a wide cut (straight/curved-cut) commits more arc and weight-shift (more exposure) than a point thrust that
retracts. Folded into `exposure_cost` via a `head_commit` factor (cut > thrust for exposure; blunt heaviest).

**Drivers, per Jordan:** grip (choke), footwork (commit + exposure recovery), then weapon type/reach/head/contact-area/
weight (capacities + costs). **Top-down:** choking up is a real close-quarters technique (half-staff, half-sword); the
lunge buys reach at the price of exposure and a recovery beat; recovering footwork is what makes a lunge safe; wide
swings expose more than thrusts. All consistent with the manuals.

---

## E · How these wire into the bout (§ refs to bout procedure)
- **A → §4a/§6b:** effective reach each beat sets the negotiated measure.
- **B → §4b.6 / §0:** `recovery_beats` paces blows within the engagement; `soft_blow_cap` bounds the 6–10 s window
  alongside stamina/wounds; per-weapon tempo decides chain-vs-commit.
- **C → §5:** inter-bout stamina update; feeds across-bouts press endurance.
- **D → §4a/§4b:** choke/commit set reach; `exposure_cost` is a σ penalty on the committing fighter's next beat (so
  a deep lunge that misses is punished — role can flip on the riposte).

## F · NERS / open items
- **Necessary/Elegant:** every quantity is derived from the **existing** weapon vector + S1 stamina — no new attributes,
  no new per-weapon hand-authored tables beyond the axis roster. Coefficients are a small shared set, not per-weapon seeds.
- **Coefficients are seeds** (L0/LONG_BONUS/HEAD_REACH, BASE_TEMPO/SPEED_K/WEIGHT_PEN/TEMPO_CAP/BLOW_COST,
  RECOVERY_FRAC/STAMINA_REF, CHOKE_K/COMMIT_K/EXPOSE_K/head_commit). Calibrate against the rebuilt state-graph harness;
  the **forms and orderings** above are the design, the numbers are tuning.
- **Open (yours):** exact `HEAD_REACH` and `head_commit` orderings if you want them to differ from point>cut>blunt /
  cut>thrust>blunt; whether choke also buys a *bind* bonus (shorter = more leverage in the bind), which is historically true.
