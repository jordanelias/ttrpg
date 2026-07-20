# Valoria — Personal-Combat Character Sheet
**v2 · 2026-06-01 · combat slice, with martial-tradition skills**

> **Canon status (two layers).**
> • **RATIFIED canon** — base stats, derived values, Combat Pool (R1), wound model (R2/D1), Stamina (S1).
> • **CLASS-C PROPOSAL** *(grounded, Jordan-vetoable, not yet propagated)* — the martial-tradition layer, the
>   seven-axis skills, and the named technique sets, from `martial_traditions_mapping.md`.
> **In-world culture names are Jordan's** (creative layer). Traditions below carry their **historical grounding
> label** as a placeholder; the Valorian names are a slot only Jordan fills.
> `[READ: martial_traditions_mapping.md + the 5 RATIFIED_* armature files — full, this session]`

---

## 1 · Stat block  *(ratified)*

| Stat | Range | Feeds | σ-leverage channel |
|---|:-:|---|---|
| **Strength (Str)** | 1–7 | wield, bind-win, stagger, armour-defeat | pressure + bind/stagger/armour-defeat leverage |
| **Agility (Agi)** | 1–7 | who strikes first each phase | initiative / **tempo** |
| **Endurance (End)** | 1–7 | Health, Stamina | durability + press-duration |
| **Cognition (Cog)** | 1–7 | reading the opponent | Reading (with Att) |
| **Attunement (Att)** | 1–7 | reading the opponent | Reading (with Cog) |
| **Spirit (Spr)** | 1–7 | Stamina; (cross-system: threadwork, social, rally) | press-duration |
| **History (Hist)** | — | combat dice pool, trained technique depth | pool depth + named-set access |

## 2 · Derived combat values  *(ratified formulas)*

```
Combat Pool    = max(5, History + 6)            (R1 — Agility-independent)
Wound Interval = End + 6                          (damage per wound tier)
Max Wounds     = min(End ÷ 2 + 1, 3)              (discrete wound tiers, integer)
Health         = Wound Interval × (Max Wounds + 1)
Stamina        = 3·End + 2·Spirit                 (S1)
```
> Note (session-B, pending Jordan): the integer `Max Wounds` step at End4 cliffs Health (End3:27 → End4:40).
> A proposed σ-leverage fix derives Health linearly in End while keeping wound *tiers* discrete. Numbers below
> use **current ratified** formulas.

## 3 · The seven combat skills (axes)  *(proposal — the skill taxonomy)*

Each axis is a real capability resolved by an engine channel. A character's skill on an axis = the feeding
stat/History, **tilted by their martial tradition's emphasis**.

| Axis (your terms) | Governs | Engine channel | Feeds from |
|---|---|---|---|
| **Approach / Reach** | controlling the measure; closing & breaking | engagement-state graph + reach-TN (R9) | weapon reach · footwork |
| **Speed / Useability** | landing first; not over-committing | weapon speed + commit-depth × reaction-slope (m5) | Agi · weapon · handling |
| **Stance** | the guard you hold; what it beats | authored Stance-Counter, gated at closing (m5) | tradition stance-set |
| **Initiation** | before / on-contact / after the strike | bout-transition + reaction-vs-commit-depth + counter-time | Agi · Cog/Att (reading) |
| **Footwork** | facing, angles, where you stand | facing → field-of-view cone (M7) | tradition footwork pattern |
| **Grip** | how you hold it (half-sword, off-hand dagger) | weapon-constrained loadout slot | weapon · tradition grip |
| **Technique** | your trained repertoire | trained-pool → equipped **named set** (generative) | History · tradition |

## 4 · Martial traditions  *(proposal — pick one)*

A tradition is **a named bundle of biases across the seven axes** — it tilts your σ-profile toward specific
phases of the fight. (The seven axes are the European-treatise lens; traditions organised around *intent*,
*geometry*, etc. show that lens dimming — that's data, not a gap.)

| Tradition (historical grounding) | Character of | Stance | Initiation | Footwork | Grip | Signature set | σ-signature | Best weapons |
|---|---|---|---|---|---|---|---|---|
| **German (Liechtenauer)** | the **bind** | Vier Leger | Vor/Indes/Nach (feel the bind) | linear pass | **Halbschwert** | **Bind Fighter** | in-bind → **Strength** | longsword · dagger · poleaxe |
| **Italian (Fiore→rapier)** | **tempo & measure** | four point-forward guards | tempo / contratempo | **the lunge** | off-hand dagger | **Thrust Duelist / Counter-time** | **Agility** (tempo) | rapier · longsword · dagger |
| **Spanish (Destreza)** | **geometry** | atajo (close the line) | calculated safe action | **the círculo** | off-hand dagger | (geometric control) | **facing/position** (M7) | rapier |
| **Japanese (koryū)** | **reading intent** | five kamae | **sen-sen-no-sen** (before) | **triangular** | two-hand | (kiriotoshi) | **Cognition/Attunement** (reading) | sabre · longsword · staff |
| **English (Silver)** | **biomechanics** | open guards | counter-stroke | true-place stepping | sword-and-dagger | (true-times discipline) | tempo discipline (punish over-commit) | short staff · backsword |
| **Chinese (qiang/internal)** | **reach + committed thrust** | rooted | committed opening | rooted advance | two-hand pole | **Burst** | reach-control (battlefield) | spear · staff · sabre |
| **Filipino (FMA)** | **continuous flow** | mobile | continuous (no counter-apex) | triangular flow | **paired** | **Continuous-flow** | sustained tempo across passes | paired short · dagger · staff |

**Match tradition to body:** a tradition's σ-signature names the stat it rewards — German wants Strength,
Italian wants Agility, Japanese wants Cog/Att. A character whose stats fit their tradition compounds; a
mismatch wastes the tradition.

## 5 · Named technique sets  *(proposal — the technique axis output)*

Equipped from the trained pool (History-gated). Each maps to a tradition: **Thrust Duelist** (Italian) ·
**Bind Fighter** (German) · **Counter-time** (Italian/Japanese counter) · **Burst** (Chinese) ·
**Continuous-flow** (Filipino).

## 6 · Gear  *(ratified costs)*

- **Weapon** — reach · weight · type, plus speed and handling (skill-curve crossover at proficiency 4:
  *forgiving* weapons reward low skill, *demanding* reward training). Longsword is **Demanding** (H1).
- **Armour** — mitigation by material (cut deflected by plate; point finds gaps; blunt transmits). Costs:
  STR-min (0/2/3/4 none→heavy), per-action stamina drain (+0/+0/+1/+2), and a modest σ-tempo penalty (A1 —
  a step slower). Plate's ~95% 1v1 dominance is **intended/historical**; counters are **blunt · point-to-gaps
  · grapple**, not fatigue. Gated by cost + availability, not an in-fight nerf.

---

## Build 1 — "The Duelist"  ·  tradition: **Italian (rapier)**

| Str | Agi | End | Cog | Att | Spr | Hist |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 4 | 4 | 4 | 3 | 3 | 3 | 3 |

- **Pool** 9 · **Health** 40 · **Stamina** 18 · **Gear** rapier (long thrust) / light
- **Tradition skills** — Approach: *misura* reach-control · Initiation: *tempo/contratempo* · Footwork: **the lunge** · Set: **Thrust Duelist** · σ leans **Agility/tempo** — matches the body.
- **Reads as** the ~50% balanced baseline; lands first via tempo, not force.

## Build 2 — "The Man-at-Arms"  ·  tradition: **German + poleaxe**

| Str | Agi | End | Cog | Att | Spr | Hist |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 5 | 2 | 5 | 3 | 3 | 3 | 4 |

- **Pool** 10 · **Health** 44 · **Stamina** 21 · **Gear** war-hammer/poleaxe / heavy plate
- **Tradition skills** — Stance: *Vier Leger* · Initiation: *Indes* (on-contact) · Grip: **Halbschwert** · Set: **Bind Fighter** · σ leans **Strength/in-bind** — matches the body.
- **Reads as** the armoured battlefield archetype: wins the bind, defeats plate with percussion + half-sword to the gaps. Slow and readable in a light duel — the intended trade.

## Build 3 — "The Master"  ·  tradition: **Japanese (koryū)**

| Str | Agi | End | Cog | Att | Spr | Hist |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 4 | 4 | 4 | 5 | 5 | 3 | 6 |

- **Pool** 12 · **Health** 40 · **Stamina** 18 · **Gear** long blade / light
- **Tradition skills** — Initiation: **sen-sen-no-sen** (reads intent before the strike) · Footwork: **triangular** · Technique: *kiriotoshi* (parry-and-strike as one) · σ leans **Cognition/Attunement/reading** — matches the maxed mental stats.
- **Reads as** the **same physical body as the Duelist**, separated only by tradition + reading. Beats the Duelist heavily under the multi-phase engine — the proof that the differentiator is **skill and tradition, not stats**. (How steep that edge should be is the open session-C tuning call.)

---

### Notes
- **Multi-phase:** each fighter resolves a bout over several **approach → engage → break** phases (initiative
  and stance reset each phase; wounds and stamina accumulate). Tradition decides *which* phase you dominate.
- **Open, Jordan's by contract:** (1) add a **short-blunt** weapon class (documented gap, thin if added);
  (2) **in-world culture names** for the traditions above.
- **Proposal status:** §§3–5 are Class-C, grounded and validated but not yet propagated to `combat_v30`.
