# Valoria — Full Bout & Fight Procedure
**Class-C proposal · 2026-06-01 (rev — corrected nesting) · clean-slate combat rebuild**

> Personal combat, ground-up, on the canonical state graph. **Corrected structure:** a **bout** is ONE approach →
> ONE engagement → ONE disengage (**6–10 s**); the "multiple blows" happen *inside the single engagement*. A
> **fight/duel** is a sequence of bouts (the multi-phase layer). Build configured beforehand; live input is
> **approach + technique** (attacker) and **stance** (defender). Defensive resolution is the companion
> `defensive_branch` doc; this is its spine.
> `[CONFIDENCE: high on structure — bottom-up from canonical state graph + ratified σ/degree engine + session multi-phase work]`
> Mechanical-tier proposal · Jordan-vetoable · nothing committed (lanes ignored).

## 0 · Structure (the corrected nesting)

```
FIGHT / DUEL  =  a sequence of BOUTS                  ← "multi-phase"; wounds + stamina PERSIST across bouts
      │
      ▼
   BOUT  =  6–10 s  =  ONE approach → ONE engagement → ONE disengage
                                          │
                                          ▼
              ENGAGEMENT  =  an exchange of multiple blows/attempts
                            (strike · bind · wind · strike — CONTINUOUS; no disengage mid-flurry)
```

You **approach once and disengage once** per bout. If you strike and end in a bind, you wind and strike again
*within the same engagement* — you do not break off and re-approach to do it. Re-approach is a **new bout**.

## 1 · Design principles
1. **Configure then play.** Identity is in the pre-bout build; live input is minimal.
2. **Everything is δσ** on the shared degree engine — no bespoke subsystems.
3. **No outcome is absolute.** Defense shifts initiative and modulates damage; never freezes the opponent or grants immunity (defensive_branch §4–5).
4. **The attacker initiates** — prevents stalemate: someone chose to approach and attack, so there is always an aggressor driving the bout.
5. **Length is emergent.** Number of bouts (and blows per engagement) varies with wounds, stamina, and how the exchange plays out — not a fixed count.

## 2 · Pre-bout configuration (the build)
Base stats (Str·Agi·End·Cog·Att·Spr·History) · derived (Pool, Health, Stamina, **Reading `(Cog+Att)/2`**,
**Reflexes `(3·Agi+Att)/4` — derived**) · martial tradition · weapon+grip (sets the defensive availability gate) ·
equipped named set(s) · stance repertoire & footwork pattern (from tradition).

## 3 · Roles per bout
- **Attacker** = the **initiator**. Chooses **approach** (how they close) + **technique** (angle + style + commit-depth). Drives the bout.
- **Defender** = the responder. Chooses **stance + intended defence** (parry / dodge / bind-block) — the live
  defensive lever. The weapon-grip + state **availability gate** still constrains what's possible, and reading/reflex
  still modulate whether the intended defence lands as the chosen mode or degrades.
- The role **passes** on a successful riposte (defender seizes initiative → becomes attacker, possibly within the same engagement) or at the next bout (either may initiate).
- **Engagement cannot be refused:** once the attacker initiates, the measure collapses and engagement happens. There is no closing-stall branch.

## 4 · The bout procedure (one approach → engagement → disengage)

### 4a · APPROACH (closing) — variable duration
- **Reading live** (both): anticipate the other's intent.
- **Attacker** picks **approach** (incl. how much to **commit distance** via lunge/footwork). **Both fighters set a
  stance** from their tradition repertoire (the m5 stance-counter resolves the pairing). Reach-control + footwork
  (r9 / M7) set the measure.
- **Defender** confirms **stance + intended defence.**
- **Negotiated measure (continuous reach):** the fighting distance each beat is set by **weapon reach (a continuous
  per-weapon value, derivation A)** ± each fighter's live range choices — **choke up** to fight closer (trading
  leverage/reach for control **and gaining a bind bonus**) or **commit lunge/footwork** to extend (trading exposure
  for distance). The longer weapon controls the far measure but pays exposure to commit; the shorter weapon wins by
  forcing the close measure where the long weapon must choke up and loses leverage.
- **Traversing the measure (F6):** initiating against a **longer effective reach** means crossing the opponent's
  measure — the longer weapon gets a **first-contact advantage** (a free defensive beat / stop-thrust as you close).
- The attacker's initiation **collapses the measure → engagement** (engagement cannot be refused, §3).

### 4b · ENGAGEMENT — the exchange of multiple blows/attempts (variable duration, the heart)
A **continuous** exchange; loops over blows/attempts until it resolves to separation. **Cadence:** per beat the
current **aggressor** commits a technique, the current **defender** an intended defence; **both fighters hold a
stance** (set at approach, transitioning during the exchange via tradition-gated guard flow). Each beat:
1. **Intent.** Aggressor commits a **technique** (commit-depth 1–5); defender commits an **intended defence**
   (parry / dodge / bind-block). Both also carry a current **stance**; the m5 **stance-counter** resolves
   aggressor-stance vs defender-stance.
2. **Clash resolution** — invoke the **defensive branch procedure** (defensive_branch §6: one anticipation check
   `Reading` vs deception → availability gate (weapon-grip + effective measure) → the intended defence resolves on
   its **mode-specific degree ladder**, possibly upgraded/degraded). Anticipation runs **once, here.** Tempo
   (initiative Agi + weapon speed + control of the **current effective measure**, §6b) orders who acts; a tied
   tempo opens the **simultaneous** window. Outcome ∈ {single hit · graze · no hit · control+riposte}.
3. **Simultaneity (emergent, two sources):** (a) a **non-absolute defence + simultaneous riposte** — a dodge that
   still grazes or a parry that leaks, while the defender's counter also lands → **both hit**; (b) **post-role-flip
   mutual attack** at tied tempo (the *Doppelhau*). No separate "trade" input — simultaneity falls out of the
   non-absolute degree ladders + role-flip.
4. **Bind sub-loop (CONDITIONAL — only if the clash leaves blades in contact** with neither winning outright; a
   dodge or a clean/gap hit creates **no** bind): a Strength+Technique wind contest (ST1), with a **choke bonus**
   (`bind_sigma += CHOKE_BIND_K·choke_amount` — half-swording). The loser keeps a degraded option (disengage-out,
   off-end strike, grapple, counter-wind) — winning is **initiative, not lockout**. A protracted bind **extends the
   engagement** (toward the 6–10 s ceiling).
5. **Role flip:** a successful **riposte** flips aggressor/defender **for the rest of the engagement** (in place, no
   re-approach); roles may flip **multiple times** (conversation of the blade), bounded by soft tempo cap + stamina
   + the 6–10 s window.
6. **Continue or resolve:** strike → (bind → wind →) strike flows on **within this engagement**; it ends when a
   fighter is felled, a fighter breaks to **disengage**, or the bout's 6–10 s window closes.
7. **Apply each beat:** hits on the **D1 damage model**, reduced by defensive degree (graze); **stamina drains per
   action, scaled by weight × commit-depth** (heavy/deep = costlier per beat; light recovers cheaply — so a fast
   flurry of many cheap beats and a few heavy committed blows cost comparably per bout); wounds accrue. Lower-stamina
   fighter gasses → out-of-breath penalty → pressed.

### 4c · DISENGAGE (separation) — once
Fighters break apart. → **next bout** (re-approach, roles may flip) **or fight end**.

## 5 · Fight termination
A fight ends when a fighter is **felled**, **yields/incapacitated**, or **both disengage and neither re-approaches**.
No fixed bout cap — emergent (§1.5). Wounds + stamina carry across all bouts; stamina governs how long a fighter
can keep initiating/ pressing across successive bouts (better stamina → more/longer bouts before gassing).

## 6 · Player interface (tactical grid)
- **Configured up front:** entire build (§2).
- **Live, attacker's turn:** **approach + technique** (incl. shallow vs deep commit, and how much **distance to
  commit** via lunge/footwork).
- **Live, defender's turn:** **stance + intended defence** (parry / dodge / bind-block).
- **Auto-resolved from configuration + situation:** footwork, defensive-mode execution (gate + stance + reading/reflex
  may upgrade/degrade the intended defence), bind contest, tempo, negotiated measure, degree outcomes. The player
  expresses *intent + stance + defence*; the engine resolves *execution* from the build. Two players both choosing
  "attack" get different fights because their configurations resolve differently.

## 6b · Reach model (continuous, negotiated)
Reach is **no longer discretely long/medium/short-banded.** Each weapon carries its **actual continuous reach value**;
the *effective* fighting range is dynamic, set live each beat by:
- **choke up** — grip closer to fight at shorter measure (trades reach/leverage for close control);
- **commit distance** — lunge / aggressive footwork to extend (trades exposure for reach).
So measure is a **negotiated band**, not a fixed property: the long weapon holds the far measure at the cost of
exposure when it commits; the short weapon's game is forcing the close measure where the long weapon must choke up.
This replaces r9's banded reach-control with a continuous reach scalar + the two live range modifiers.

## 7 · How this maps to the session multi-phase calibration
The session "phases" = **bouts**; the sub-actions within a phase = the **engagement's blows**; phase-persistence of
wounds/stamina = **across-bouts persistence**; stamina-press = the across-bouts initiative endurance (§5). Carries
forward intact. The corrections to model in the rebuilt harness: **6–10 s bout ceiling**, **one approach/disengage
per bout** (re-approach = new bout), **simultaneous + no-hit**, the **bind sub-loop**, **stance as defender input**,
and **per-mode degree ladders**.

## 8 · NERS / open items
- **Necessary / Elegant:** one state graph, one degree engine, one σ-channel set; live input is just
  approach+technique (attacker) / stance (defender). Variety comes from configuration vs situation, not added subsystems.
- **Resolved this rev:** defender live input = **stance + intended defence** (a); **engagement cannot be refused**
  (b — closing-stall branch struck); **partial stamina recovery between bouts** (c, confirmed); **reach is continuous /
  negotiated**, not banded (§6b). Prior rev resolved: attacker-initiates, 6–10 s bout, one-approach nesting.
  **This rev resolves the four calibration calls:**
  - **Role passing on riposte** — a successful riposte flips the role **for the rest of that engagement**: the
    defender becomes the aggressor and pursues advantage. Initiative is seized, not merely traded for one beat.
  - **Soft tempo cap + per-weapon tempo** — the engagement has a **soft cap on blows** (tempo beats), AND weapons
    differ: heavy/committed weapons (war-hammer, poleaxe) swing slower and force weight-shift recovery between blows;
    light/recovering weapons (rapier, paired short) **chain** attacks and recover fast. Tempo cap is per-weapon, not flat.
  - **Inter-bout recovery is computed from stamina** — not a free rate; derived from the fighter's stamina state
    (see `recovery` derivation below).
  - **Commit / choke / exposure are computed** from primitives (grip · footwork · weapon type/reach/head/contact-area/
    weight), not free seeds (see `reach_cost` derivation below).
- **Sim-fidelity rebuild required before calibration:** 6–10 s ceiling, one-approach nesting, simultaneity/no-hit,
  bind sub-loop, stance+defence input, per-mode degree ladders, **continuous reach + choke-up/commit range modifiers**
  (replaces banded reach-control), partial inter-bout stamina recovery. Until then δσ magnitudes / degree cutoffs /
  tempo + reach weights / gate strengths are **uncalibrated seeds**.
- **Open design calls (yours):** (a) does the **role pass mid-engagement** on every successful riposte, or only at the
  next bout? (b) within the 6–10 s engagement, is there a soft cap on blows (tempo beats) or does stamina/wounds alone
  bound it? (c) **how much** partial stamina recovers between bouts (the recovery rate is a seed)? (d) choke-up /
  commit-distance magnitudes — how far each modifier shifts effective reach, and the exposure cost of committing.
- **Grounding:** HEMA bout = *zufechten* (approach) → *krieg* (the exchange/winding war) → *abzug* (withdrawal);
  multiple bouts per fight; 6–10 s matches a real intense exchange before fighters reset.

## Discarded (recorded)
Full Guard · Dodge-action · Feint-action · Tie Up · Rescue · O/D dice-split · multi-cycle-within-a-bout ·
engagement-refusal / closing-stall · discrete long/medium/short reach bands · the
`in_bind`/`breaking` node names. Intents survive as emergent outputs within the state graph.
