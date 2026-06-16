# Personal combat — stat/attribute map + weapon-attribute impact (reference)

**2026-06-13 · grounded in `designs/scene/combat_engine_v1/` at this session's HEAD**

`[READ: combat_engine_v1/{combatant,systems,core,wrapper}.py + v32/{r1,r2,r5,r8}]` — every site below is a real
call in that code; nothing inferred.

Three exact points first, because they correct common assumptions:
- **The resolution dice pool is History-driven and Agility-independent** — `resolution_pool = max(5, History+6)`.
  The old `(Agi×2)+History+3` was retired ("the cross-attribute dominance channel is closed by construction").
  Agility's combat role is tempo/initiative/reflex/footwork, **not** the pool.
- **Endurance does not cap incoming damage.** The damage cap is the constant `CAP_END=4`
  (`cap = 1.2·(CAP_END+6) = 12`). Endurance governs *survivability* through the wound pool, not hit size.
- **`head_len`/`grip_len` feed leverage, not reach.** Reach runs off the categorical `reach` flag + `HEAD_REACH`;
  the lengths drive the bind/displace lever-arm.

---

# PART 1 — Every stat/attribute and where it occurs

## 1.0 The resolution backbone (pool + wounds)

| Quantity | Formula | Where | Role |
|---|---|---|---|
| **Resolution pool** | `max(5, History+6)` − `wt.pool_penalty()` | `core.resolution_pool`; both strike sites in `wrapper` | the d10 success-count pool every roll draws from — the single largest competence term |
| **Wound increment WI** | `End+6` | `r2.WoundTracker` | gate size; a hit > WI crosses multiple gates (the decisive blow) |
| **Max wounds MW** | `min(End//2+1, 3)` | `r2.WoundTracker` | felled at MW+1 |
| **Health** | `WI·(MW+1)` (End 4 → 40) | `combatant.health_full` | total damage absorbed |
| **pool_penalty** | −1D per wound | `wt.pool_penalty()` → subtracted from the pool | **the death-spiral coupling**: wounds shrink the pool (no Ob penalty, ever) |

## 1.1 Base attributes (1–7, set at chargen)

| Stat (default) | Combat role | Feeds → site(s) |
|---|---|---|
| **Strength** (4) | wielding, power, the bind | `str_demand`→`handling_penalty` (lowers atk & def σ when under-strength) · `balance_eff` (½Str) · `mode_sigma` **wind** (Str−Str) · `bind_sigma` (Str diff) · `core.damage` impact `HEFT+clamp((Str−3)//2,−1,2)` |
| **Agility** (4) | cadence, reactions, footwork, initiative — *not* the pool | `weapon_tempo` (`AGI_TEMPO_K·(Agi−4)`) · `reflex` (`REFLEX_AGI`) · `balance_eff` (½Agi) · `wrapper` initiative (`INIT_K·(Agi−Agi)`) |
| **Endurance** (4) | toughness + stamina (not hit-size) | `health_full`/`WI`/`MW` (wound capacity) · `stamina_max` (`3·End`) |
| **Cognition** (3) | the read — primary | `reading = (2·Cog+Att)/3` → *every* reading site: `mode_sigma` read-diff, `feint_eval`, `reopen_prob`, `bind_sigma` tactile, `approach_displace`, `wrapper` read-contest + initiative reading term |
| **Attunement** `att` (3) | perception + reaction — secondary | `reading` (Att half) · `reflex` (`REFLEX_ATT`) |
| **Spirit** (3) | reserves | `stamina_max` (`2·Spirit`) · `conc_max` (`2·Spirit`) |
| **Focus** (3) | concentration, structure recovery, mental-fatigue resistance | `conc_max` (`3·Focus`) · `wrapper` poise recovery (`POISE_FOCUS_K·(Focus−3)`) · mental-fatigue protection (`FOCUS_MENTAL_K`) on reading/technique |
| **History** (3) | the resolution pool (primary) + experience | `resolution_pool` (`History+6`) · `reading` (`+(History−3)`) · `mode_sigma` technique (`History+skill`) · `bind_sigma` (`History+skill`) · `wrapper` initiative (`INIT_HISTORY_K·History-diff`) |
| **Disposition** `disp` (4) | behaviour, not skill — orthogonal to tradition | `disp_lean=(disp−4)/3` → commit-depth skew (aggressive deep 4–5 / cautious shallow 2–3) · initiative lean (`DISP_INIT_K`) · counter propensity (`DISP_COUNTER_K`) |

## 1.2 Skills (equippable per-axis biases, default 0)

| Skill | Site |
|---|---|
| `balance` | `balance_eff` (footwork/measure, anti-overcommit, stance) |
| `technique` | `mode_sigma` (parry/dodge quality) · `feint_eval` |
| `parry` | `mode_sigma` parry |
| `dodge` | `mode_sigma` dodge |
| `bind` | `mode_sigma` wind · `bind_sigma` |

## 1.3 Dynamic state (managed by the wrapper, not chargen)

| State | Source / drain | Effect sites |
|---|---|---|
| **Stamina** | `stamina_max`; drained by `act_cost` (commit+weight) & feints; `fatigue = 1−stam/max` | degrades `weapon_tempo`, reading (mental-fat), `mode_sigma`, `balance_eff`; ≤ −4 ends the engagement |
| **Concentration** | `conc_max`; drained on being hit (`CONC_DRAIN_HIT`) | mental-fatigue resistance (protects reading/technique under fatigue) |
| **Initiative (Vor)** | signed; gained on hits, stolen (indes/sen-no-sen), decays (`init_hold_decay`), lost on overcommit (`init_overcommit_loss`); clamped `INIT_CAP` | `initiative_sigma` — a bounded edge on **both** attack and defence (hold-the-Vor-while-defending) |
| **Poise (kuzushi)** | 1.0 → `POISE_FLOOR`; broken by overcommit & lost binds; recovered (Focus-scaled) | `poise_factor` multiplies **tempo and defence** — a broken-structure fighter acts and defends worse |
| **Grip** | `normal` / `choke` / `lunge` | `weapon_tempo` (choke/lunge penalties), `leverage`, `legibility`, `close_tempo` pole penalty |
| **Weapon-form** | `halfsword_target` auto-switch by range+armour | swaps the whole weapon vector (longsword ↔ half-sword) |

---

# PART 2 — How weapon attributes impact those

Weapon attributes never change the base stats; they set the **derived quantities and σ-contributions the stats
combine with**. Each row: attribute → the site it feeds → the stat it meets there → effect.

## 2.1 The damage stack

| Attribute | Feeds → site | Meets stat | Effect |
|---|---|---|---|
| **wt** (light/heavy) | `core.HEFT` (4/6) | Strength (`imp`) | base impact |
| **head** (point/cut_thrust/straight_cut/curved_cut/blunt) | `coupling`/`_mode_transmit` → `RESIST`,`DELIVERY` | Strength | the *mode* of damage + how armour mitigates it — the qualitative weapon axis |
| **gap** (0–1, geometry-derived) | `coupling` point-transmit & gap-thrust | — | precision thrust into plate gaps |
| **percussion** (0–8, hand-set) | `_mode_transmit` blunt `×(perc/8)` | Strength | blunt transmission through armour *(session: derivable from mass·pob)* |

## 2.2 Reach / measure

| Attribute | Feeds → site | Effect |
|---|---|---|
| **reach** (short/long) + **reach_adj** | `reach_base` (`LONG`, additive) | standing measure (gap in `reach_sigma`) |
| **head** | `reach_base` `HEAD_REACH[head]` | a point adds reach, a blunt head none |
| **hands** (1/2) | `reach_base` `HANDS2` | two hands extend reach |

## 2.3 Tempo / cadence

| Attribute | Feeds → site | Meets stat | Effect |
|---|---|---|---|
| **spd** | `weapon_tempo` `SPEED_K` | Agility | the cadence base |
| **wt** | `weapon_tempo` `WEIGHT_PEN` (+`HANDS_COMMIT` if heavy 2H) | Agility | heavy = slower (bounded) |
| **closes_poorly** (flag) | `close_tempo` `POLE_CLOSE_PENALTY` | (grip) | long poles slow once a faster weapon is inside — unless they choke up |

## 2.4 Handling

| Attribute | Feeds → site | Meets stat | Effect |
|---|---|---|---|
| **wt**, **hands**, **reach** | `str_demand` (`D_WT`,`D_2H`,`D_LEN`) | Strength | sets the strength the weapon demands |
| **hand** (Forgiving/Standard/Demanding) | `str_demand` `D_HAND·HANDLE_RANK` | Strength | how punishing it is to wield under-strength → `handling_penalty` lowers **both** atk & def σ |

## 2.5 Leverage / the bind

| Attribute | Feeds → site | Meets stat | Effect |
|---|---|---|---|
| **grip_len**, **head_len** | `leverage = LEVER_K·(grip/(grip+head) − ref)` | — | lever-arm (long grip + compact head = high) |
| → `leverage` flows into | `bind_sigma`, `approach_displace`, `reopen_prob` | History+`skill(bind)`, Strength, tradition | who wins the bind / sets aside a point on approach / regains distance |
| **hands** | `leverage` `LEVER_2H` | — | two hands add lever control |
| **blade_guard** (0–1) | `bind_sigma` `BIND_GUARD_K` + `mode_sigma` **wind** `WIND_GUARD_K` | History+`skill(bind)` | active blade-catching (cross/quillons/rings) in the bind & wind |

## 2.6 Defence caps

| Attribute | Feeds → site | Meets stat | Effect |
|---|---|---|---|
| **hand_guard** (0–1) | `mode_sigma` **parry** `PARRY_GUARD_K` | reflex+technique | safe parrying / forward hand commitment ("don't parry with your hands") |
| **head** (per-weapon **GATE**) | `mode_sigma` final `×cap` | reflex/balance/technique | per-weapon parry/dodge/wind ceilings (a poleaxe winds well, dodges poorly) |

## 2.7 Armour-defeat (the armoured-exchange controller)

| Attribute | Feeds → site | Effect |
|---|---|---|
| **head** | `armor_defeat_sigma` mode select | which defeat-mode applies |
| **percussion** | `armor_defeat_sigma` blunt `×(perc/8)` | blunt defeats plate (mace/poleaxe yes; staff no) |
| **gap** | `armor_defeat_sigma` point/cut_thrust `×gap` | gap-thrust + half-sword vs plate |

## 2.8 Sourced but not consumed (the session's findings)

| Attribute | Status |
|---|---|
| **mass**, **pob_frac** | **dangling** — the engine collapsed them to binary `HEFT` + hand-set `percussion`. The 2026-06-13 work derives `P_auth` (percussion) and `puncture_pressure` from `mass·pob`. |
| **geometry** {curvature, point_concentration, cross_section, edge_keenness, strike_concentration} | `geometry.bake` wires **only `gap`** (from point_concentration × cross_section); `perc_conc`/`cut`/`thrust` are baked but **dangling**. The puncture work uses `strike_concentration`. |
| **clinch** | a grappling-range datum present on every weapon; **not read** by `systems`/`core`/`wrapper` (for a grappling submodule, or dangling). |

---

*Tradition channel weights (`eff_cw`) additionally multiply ~19 of these σ-sites — measure, tempo, leverage,
visual, tactile, precommit, balance — but that layer is under separate review (see the tradition-representation
exploration); it is orthogonal to the stat→site map above.*
