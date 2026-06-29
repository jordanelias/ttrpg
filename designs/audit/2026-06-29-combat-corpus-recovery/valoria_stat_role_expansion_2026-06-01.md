# Valoria — Stat-Role Expansion + Survivability Findings
**Class-C proposal · 2026-06-01 · clean-slate combat rebuild**

> Captures Jordan's 2026-06-01 stat-role directives precisely, built bottom-up on the canonical engine and validated
> top-down, plus the measured survivability / strike-rate findings. **One item is blocked on a Jordan roster call**
> (Concentration vs the canonical Certainty stat) and is NOT wired pending that.
> `[READ: params/combat.md, derived_stats_v30, char_gen_v30, canon foundations — this session]`
> `[CONFIDENCE: high on findings (measured); high on design forms; coefficients are seeds]`

## A · Survivability & strike-rate (answering the draw-rate question)
**Clarified:** the earlier "13% draw" was a **fight-level timeout** (ran all bouts, no fell, wounds tied) — NOT a
"nobody got hit" rate. Measured properly on the state-graph harness (4/4/4 mirror):
- **Turns(bouts)-to-fell:** mean ~10, median 11; **0% felled by turn 3, ~8% by turn 6, ~49% hit the MAX_BOUTS cap.**
  → Survivability is **high — arguably too high**; "multiple turns before a fell" is satisfied, but fights **drag to
  the cap** rather than resolving. Each hit is too small relative to Health across the bout count.
- **Per-bout strike rate:** **~62% of bouts land ≥1 hit / ~38% clean no-hit** — and this is **structural** (invariant
  to damage scale): the ~38% clean bouts come from the engagement's per-beat disengage (seed 0.12) ending the bout
  before a hit lands.

**Top-down (HEMA / tradition research):** clean no-touch outcomes in committed fencing are a **minority**; the
Liechtenauer corpus drills explicitly against the *Nachreisen*/afterblow precisely because clean unhit exchanges are
hard, and tournament datasets typically show a **majority of exchanges scoring a touch** with doubles often 15–30%.
**Verdict:** ~62% strike / 38% clean is **plausible but on the survivable side**; historically ~**70–80%** of committed
exchanges land something. **Correction (tuning, not structural):** fewer, more consequential turns — lower the
per-beat **disengage rate** and raise per-bout lethality so fights resolve in **~3–6 turns** with strike rate ~**70%+**.

**Sweep targets (need a joint sweep; disengage rate must first be parameterized — it's a hardcoded literal):**
`disengage_rate × beats-per-engagement floor × DAMAGE_SCALE × MAX_BOUTS` → 3–6 turns, strike/bout ≥70%, draws <5%.

## B · Strength → weapon handling (NEW role, groundable now)
Strength gains a **graded handling** role (beyond the binary wield-min gate and damage Impact): the **longer / heavier
/ more unbalanced** the weapon, the more Strength it takes to handle **well**.
```
str_demand(weapon) = D0 + D_LEN·reach_base + D_WT·[weight=heavy] + D_HAND·handling_rank + D_2H·[hands=2]
handling_deficit   = max(0, str_demand − Strength)
handling_penalty   = HANDLE_K · handling_deficit        # σ penalty: sloppy control → worse pool/defense/tempo
```
`handling_rank`: Forgiving 0 / Standard 1 / Demanding 2 (weapon_axes_v2). A Strength surplus → clean (no penalty;
optional small bonus capped). **Top-down:** a greatsword or poleaxe in weak hands is genuinely unwieldy; a dagger is
not. This is the *Meyer/Fiore* point that big weapons demand strength to wield with control, not just to lift.

## C · Endurance → handling-via-fatigue, footwork, press (EXPANDED roles, groundable now)
Endurance already gives Health + Stamina + inter-bout recovery. Add, via the **physical-fatigue** channel (low stamina):
- **Fatigue degrades handling:** as stamina drops, effective handling worsens — `handling_penalty += FATIGUE_HANDLE_K
  · fatigue_frac`, where `fatigue_frac = 1 − stamina/stamina_max`. Endurance (capacity + recovery) sets how long you
  handle the weapon well before this bites.
- **Fatigue degrades footwork:** footwork (→ dodge, measure control) scales down with fatigue —
  `footwork_eff = footwork · (1 − FATIGUE_FOOT_K·fatigue_frac)`.
- **Press capacity:** low stamina caps how much you can attack (already the OOB penalty; make pervasive — fewer/
  weaker presses when gassed). Endurance → number of **effective turns** across the fight (capacity + recovery).

**Top-down:** fatigue wrecks both edge control and footwork first (every manual and every modern coach); a tired
fighter cannot press. Endurance as the fatigue-capacity stat is historically central.

## D · Concentration (focus) — BLOCKED on roster call, spec ready
Jordan: a **focus stat, Concentration, that combines with Spirit**, governing how well skill survives fatigue/pain.
**Canon check:** the canonical substrate names *TS/Coherence/Spirit/**Certainty***, **not** "Concentration." So this is
**either a new 8th attribute OR the intended role of the existing `Certainty` stat** — a canon-structure call only
Jordan makes. **Not wired pending that.** Spec (whichever it maps to):
```
focus = (Concentration + Spirit)/2      # composure under fatigue/pain
```
Two roles:
1. **Protects mental channels from physical fatigue:** Reading and technique/skill normally degrade as stamina drops;
   focus resists it — `mental_fatigue_frac = fatigue_frac · (1 − FOCUS_K·(focus−3)/N)`. So **Endurance governs how fast
   you fatigue physically; Concentration governs how well your *skill* survives the fatigue.** (Clean division: C
   protects Reading/technique; it does NOT protect Strength-handling or footwork — those are the physical-fatigue
   domain in B/C above.)
2. **Disruption resistance on a simultaneous blow:** when you take a hit while acting, focus governs whether you still
   **complete your action / maneuver** (pain not modelled directly, modulated indirectly) — `disrupt_resist =
   σ(DISRUPT_K·(focus−3))`; a simultaneous/afterblow that would interrupt your strike is resisted by focus.

**Top-down:** the ability to hold technique and finish the action under exhaustion and after being struck is exactly
what separates a trained fighter late in a fight; modelling it as focus-vs-physical-fatigue is faithful and keeps pain
out of the model while capturing its effect.

## E · Strength → Health (CONDITIONAL, deferred)
Jordan: **if** Strength ends up too weak after B–D, add a **musculature → Health** contribution. **Procedure:** tune
B–D first; if Str-lead group rate stays low (< ~46), add `Health += STR_HEALTH_K·(Strength−ref)` and re-tune. Not added
yet — it is a *fallback* contingent on the post-tuning measurement, not a baseline change.

## F · Drift flagged (not mine to fix here)
`params/combat.md` is the **unpropagated old engine**: still `Pool=Agi×2+Hist+3`, `Stamina=End×5`, Attunement-acts-last
initiative — all **superseded** by the ratified armature (R1/S1). I work from the ratified files; this doc needs the
armature propagation (separate commit pass, lanes).

## G · NERS / consistency
- **Necessary/Elegant:** B and C reuse the **existing** Strength/Endurance/stamina machinery and the weapon vector — no
  new attributes for handling/footwork/press. D *does* add an attribute (or repurposes Certainty) — justified by two
  distinct roles nothing else covers, but its necessity is Jordan's call alongside the roster question.
- **Precise division of fatigue (the load-bearing consistency point):** **physical fatigue** (Endurance domain) degrades
  Strength-handling + footwork + press; **focus** (Concentration+Spirit) protects the **mental** channels (Reading,
  technique) and resists disruption. No double-counting: a stat is in exactly one fatigue domain.
- **All coefficients** (`D*`, `HANDLE_K`, `FATIGUE_*_K`, `FOCUS_K`, `DISRUPT_K`, `STR_HEALTH_K`) are **seeds** for the
  joint sweep; the forms above are the design.

## Pending (ordered)
1. **Jordan: Concentration vs Certainty** — new 8th attribute, or the role of canonical Certainty? (blocks D, and the
   character sheet's stat block).
2. Parameterize the disengage rate; **joint survivability sweep** → 3–6 turns, strike ≥70%, draws <5% (A).
3. Wire B + C (Strength-handling, Endurance fatigue→handling/footwork/press); re-tune Str/Agi/End to ~50 each — this is
   also the most likely fix for the **Agi-lead ≈53 / Str ≈46** gap (Strength-handling gives Str pervasive value).
4. Wire D once (1) is answered.
5. If Str still weak → add E (Str→Health) and re-tune.
6. Then weapon-roster, differentiator-steepness (Jordan call), plate re-confirm, reach game.
