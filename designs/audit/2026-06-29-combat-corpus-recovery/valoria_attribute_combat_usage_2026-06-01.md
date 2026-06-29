# Valoria — Attribute Usage in the Combat System
**2026-06-01 · how each attribute feeds combat**

> Every channel below traces to a **ratified** armature decision or a **verified** combat module read this
> session. Proposal-layer channels (Reading→stance/reaction prediction; named sets) are marked **[C-PROP]**.
> `[READ: RATIFIED_2026-05-29 + 4 addenda; r8/m5/r9/m1/m3 modules; derived_stats §4 — this session]`
> `[CONFIDENCE: high — ratified files + module constants; proposal channels flagged]`

## The architecture in one paragraph

The dice **Pool** is set by **History alone** (R1). Everything else an attribute does enters as a **σ-leverage
shift** — a δσ that bends the effective difficulty (`effective_ob`) of each strike. Per **L1**, that σ-leverage
raises **both** the chance to land **and** the degree/Quality of the hit (seed `LEVERAGE_TO_DEGREE=3.5`), so a
σ edge flows all the way into damage. **Damage** itself is `Impact(Str+Heft) × Coupling(material×mode) ×
Quality(degree)` (D1). **Endurance** governs the two pools that persist across phases (Health, Stamina). That
is the whole engine: History→pool, attributes→σ→(land × degree)→damage, End→durability/press.

---

## Strength (Str) — the leverage & force attribute

| Channel | Mechanism | Value / constant | Canon |
|---|---|---|---|
| **Wield** | heavy weapons need a STR-min; below it you cannot wield | STR-min gate (None = can't lift) | canonical |
| **Pressure** | flat σ pressure by Str difference | `(Str_atk − Str_dfn) × 0.0312` | r8 / ST1 |
| **Bind-win** | in the **In-bind** state, a Strength contest → δσ | bind δσ | **ST1** |
| **Stagger** | a heavy-weapon **Overwhelming** opens the foe's next-strike σ-window | `STR_STAGGER_WINDOW = 0.25` | **ST1** |
| **Armour-defeat** | Str expressed as a σ-leverage window vs armour (not only damage) | leverage component | **ST1** |
| **Stamina-efficiency** | Str above STR-min lowers per-action stamina cost | drain reduction | **ST1** |
| **Damage Impact** | additive force into damage — **no Str×weight multiplier** | `Impact = Str + Heft` | **D1** |

**Where it dominates:** the **armoured battlefield** — bind, stagger, armour-defeat, and Impact all compound
when defence is suppressed (C1). Str-led there is intended (59/46/45).

## Agility (Agi) — the tempo attribute

| Channel | Mechanism | Value / constant | Canon |
|---|---|---|---|
| **Initiative** | who strikes first each phase | `AGI_INITIATIVE_PER_POINT = 0.0625` | **R1** |
| **σ-tempo** | Agi contributes as a tempo δσ — **not** as pool dice | tempo δσ (agi_leverage) | **R1** |

**Note:** R1 deliberately **removed Agility from the pool** (superseded PP-247's `Agi×2+History+3`). Agility
buys *tempo*, not dice — landing first and not over-committing. **Dominates the unarmoured duel** (tempo is
the duel's currency); shrinks on the battlefield (everyone's slow, A1 taxes all).

## Endurance (End) — the durability & stamina attribute

| Channel | Mechanism | Formula | Canon |
|---|---|---|---|
| **Wound Interval** | damage absorbed per wound tier | `WI = End + 6` | R2 / derived_stats §4.1 |
| **Max Wounds** | number of discrete wound tiers | `MW = min(End÷2 + 1, 3)` | R2 / §4.1 |
| **Health** | total damage capacity | `Health = WI × (MW + 1)` | R2 / §4.1 |
| **Stamina** | press-duration pool (dominant term) | `Stamina = 3·End + 2·Spirit` | **S1** |
| **Press-duration** | in multi-phase, more stamina → press longer (foe gasses → out-of-breath penalty) | stamina drain across phases | session multi-phase |

**Watch-item (session-B, pending Jordan):** the integer `MW` step at End4 cliffs Health (End3:27→End4:40).

## Cognition (Cog) + Attunement (Att) — together they are **Reading**

| Channel | Mechanism | Canon |
|---|---|---|
| **Reading δσ** | jointly compute a Reading edge — out-think the opponent | `Reading = f(Cog, Att)` |
| **Stance prediction** **[C-PROP]** | read correctly → pick the **counter-stance** at closing | m5 stance-counter, `P(read) = σ((Cog+Att)/2)` |
| **Reaction selection** **[C-PROP]** | read commit-depth → pick the best reaction (counter-time) | m5 reaction |

**Note:** Cog and Att are **symmetric** into Reading — neither acts alone in combat; they average. **Reading is
the strongest single differentiator** under multi-phase (its magnitude is the open session-C tuning item —
near-binary today, "tunable down once weapons settle").

## Spirit (Spr) — stamina reserves (combat); a cross-system attribute

| Channel | Mechanism | Canon |
|---|---|---|
| **Stamina** | the `+2·Spirit` term — press-duration only | **S1** |

**Note (S2):** Spirit's **personal-combat role is *only* stamina reserves**, and its low combat showing is
**intended** — its real value is **cross-system**: threadwork core, social contests (with Composure),
mass-battle rallying. Don't read its small combat footprint as weakness.

## History (Hist) — the trained-skill attribute

| Channel | Mechanism | Formula | Canon |
|---|---|---|---|
| **Combat Pool** | the **only** input to the dice pool | `Pool = max(5, History + 6)` | **R1** |
| **Technique depth** **[C-PROP]** | gates the trained pool → equipped **named set** (tradition) | History-gated set access | martial_traditions |

**Where it dominates:** everywhere — deeper pool = more dice every strike, plus access to tradition technique
sets. With Reading, History is the **skill differentiator** the equal-value design rests on.

---

## Cross-cutting: how it all resolves (one strike)

```
Pool        = max(5, History+6)                                    ← History only (R1)
net σ-edge  = Str pressure/bind/stagger/armour-defeat (ST1)
            + Agi tempo + initiative (R1)
            + Reading (Cog,Att) → stance & reaction (m5) [C-PROP]
            + weapon speed/reach (W2/W3) − armour σ-tempo (A1)
effective Ob = base Ob shifted by net σ-edge                       ← σ-leverage
degree       = roll(Pool) vs effective Ob, lifted by σ-edge        ← L1 (LEVERAGE_TO_DEGREE=3.5)
damage       = Impact(Str+Heft) × Coupling(material×mode) × Quality(degree)   ← D1
apply to     = Health (WI=End+6); Stamina (3·End+2·Spirit) drains  ← End/Spirit persist across phases
```

## Summary — one line each

- **Strength** — force & leverage: wield, bind, stagger, armour-defeat, stamina-efficiency, damage Impact. *Battlefield king.*
- **Agility** — tempo: initiative + σ-tempo (not pool dice). *Duel king.*
- **Endurance** — durability (Health) + press (Stamina). *Persists across phases.*
- **Cognition + Attunement** — Reading: out-think → counter stance/reaction. *Strongest differentiator.*
- **Spirit** — combat = stamina reserves only; real value is cross-system. *Intentionally quiet in combat.*
- **History** — the dice pool + trained technique sets. *The skill the balance rests on.*
