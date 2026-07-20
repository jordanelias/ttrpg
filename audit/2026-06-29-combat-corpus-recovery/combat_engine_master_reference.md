# Valoria Personal Combat Engine — Master Reference

**Source:** `designs/scene/combat_engine_v1/` — every file (`combatant.py, systems.py, core.py, config.py, wrapper.py, geometry.py, tradition.py`) byte-verified identical to HEAD this session, plus the canonical primitives it delegates to (`r1_sigma_resolution.py`, `r5_strength_stamina.py`, `r8_parity_harness.py` in `/home/claude/v32`). Every formula and constant below is read from the literal source, not memory. All constants are **Class-C** (tuned to hold the validated invariants; Jordan-vetoable).

---

## 0 · Orientation (how the engine is shaped)

**Architecture.** `wrapper.py` is the orchestrator: it owns the A/B identity, the engagement state graph, and **all** state mutation; it assigns aggressor/defender each beat and passes `Combatant` *objects* (never raw "A"/"B") to the subsystems. `systems.py` holds the mechanics as **pure functions** of role-objects. `core.py` delegates resolution to the canonical engine (`r1`/`r5`/`r8`). `tradition.py` is a modulator layer (channel-weights + equippable abilities). `geometry.py` bakes weapon coefficients once at import.

**Flow.** `fight(A,B)` → up to `max_bouts=12` bouts. Each bout = one `engagement()`:
- **GAUGE** (engagement entry, once): reach, longer/shorter (coin-flip on exact tie — fairness fix), initial `measure_gap`, `initiative_seize` (pre-contact Vor).
- **Beat loop** (`while beats < 24`), each beat does per-beat **UPKEEP** (fatigue, initiative decay + disposition-drift, poise recovery, tempo accrual) then runs one of:
  - **APPROACH** (gap > 0.3): the shorter closes (`close_rate`), the longer threatens with **stop-hits**.
  - **CLOSED** (gap ≤ 0.3): the tempo-gated **exchange** — read contest → mode pick → `net_sigma` → **the roll** → outcome → optional **BIND** sub-loop, riposte, displace, reopen.
- A felled fighter ends the engagement; a separation ends the bout (recover between bouts). Undecided after 12 bouts → **result 0** (no auto-tiebreak). Decided fights flip with prob `UPSET_FLOOR=0.05` (the 95 % cap).

**Where the dice pool actually rolls (answer to "in what stages?"):** the `resolution_pool` is rolled in **exactly two places** — (1) the **APPROACH stop-hit** (`wrapper.py:76-79`, only when reach differs and a stop-hit fires, probability ∝ gap), and (2) the **CLOSED exchange** (`wrapper.py:160-162`, every committed attack — the primary roll). It is **not** rolled in the bind loop (that is a `bind_sigma` logistic), **not** for damage (damage is deterministic given the degree), and **not** for initiative/seizure (those are `tanh`/logistic contests). Both rolls use `pool = resolution_pool(aggressor‑or‑longer.history)` — History only.

---

## 1 · MASTER TABLE — BY MECHANIC

Stage codes: **G**=gauge · **A**=approach · **C**=closed exchange · **B**=bind sub-loop · **U**=per-beat upkeep · **X**=inter-bout · **I**=build-time import. CHAR = character stat/skill; everything else (weapon/armour/tradition/state/constant) is non-character.

| Mechanic | Stage | Exact formula | CHAR inputs | Non-character inputs | Output / effect | Canon status |
|---|---|---|---|---|---|---|
| **Resolution roll** | A,C | `ob = effective_ob(DECISIVE_OB, pool, net_sigma)`; `net = roll_net(pool, TN)`; `deg = degree(net,ob)` | — | net_sigma, pool, TN (r8) | degree ∈ {fail, partial, success, overwhelming} | engine = canonical r1/r8 resolution |
| **Resolution pool** | A,C | `max(POOL_FLOOR, round(history)+BASE_POOL)`; stored `pool = max(5, history+6)` | History (skill) | POOL_FLOOR, BASE_POOL | the d10 success-pool size | **deliberate redesign** — `r1` docstring: "Agility-independent… NOT (Agi×2)+History+3." **Deviates from canon Combat Pool (PP-615)** = (Agi×2)+History+3 |
| **net_sigma (hub)** | C | `atk_sig − dsig − reach_pen + adef + init_edge + ATTACKER_BIAS(0.12)` | (composite) | ATTACKER_BIAS | the roll's threshold shift; sum of nearly every σ below | engine-specific composite |
| · atk_sig | C | `COMMIT_SIGMA(0.18)·(commit−3) + init − 0.5·oob − handling_penalty(agg) + consistency_a` | Focus (consistency) | commit, oob, constants | aggressor's offensive σ | engine |
| · init (tempo term) | C | `INIT_K(0.045)·(agi_a − agi_d)·ch(agg,tempo)` | **Agility** | tradition tempo | per-beat tempo edge → atk_sig | engine routes Agi here (matches `agility_delta_sigma`); canon initiative is **Attunement-primary** |
| **Reach / measure** | C | `REACH_W[armor]·((gap·REACH_FRAC(0.82) + foot_meas)·meas_w)`; `foot_meas = FOOT_MEASURE_K(0.15)·(balance_eff_def·ch(def,balance) − balance_eff_agg·ch(agg,balance))`; `meas_w = ch(def,measure)/ch(agg,measure)` | Agility (balance_eff) | reach_base, armour REACH_W, tradition measure/balance | reach_pen (subtracted from net) | engine |
| **Defense — parry** | C | `(base + PARRY_K(0.9)·(0.45(reflex−3)+0.45(tech−3))/3 + skill_parry + PARRY_GUARD_K(0.45)·(hand_guard−0.45))·GATE`; commit≥4 → −0.25 | reflex(Agi,Att), History (tech), skill | hand_guard, GATE, base read | dsig | engine |
| **Defense — dodge** | C | `(base + DODGE_K(0.9)·(0.30(reflex−3)+0.70(balance_eff−3))/3 + skill_dodge)·GATE`; commit≥4 → +0.10, ≤2 → −0.10 | reflex(Agi,Att), Agility (balance) | GATE | dsig | engine |
| **Defense — wind** | C | `(base + WIND_K(0.9)·(0.45(tech−3)+0.45(str−str_agg))/3 + CHOKE_BIND_K(0.30)·choke + skill_bind + WIND_GUARD_K(0.40)·(blade_guard−0.45))·GATE` | History (tech), **Strength** | blade_guard, choke, GATE | dsig | engine |
| · mode base (all 3) | C | `READ_K(0.5)·(reading_def − reading_agg)·(1.3 if read_win else 0.7)` | reading(Cog,Att) | — | shared term in each mode | engine |
| **Armour-defeat** | C | `ADEF_W[armor]·(cap − ADEF_THRESHOLD[armor])`; cap = blunt `1.3·perc/8` / point `1.0·gap` / cut_thrust `max(−0.9, gap)` / cut `−0.9` | — (no stat) | weapon head/percussion/gap, armour | adef (added to net) | engine |
| **Read contest** | C | `read_d = reading(def)·ch(def,visual)·fam·legib·(1−0.4·mental_fat_d)·(1−feint_debuff)`; `read_a = reading(agg)·ch(agg,visual) + consistency_a`; `read_win = logistic(read_d−read_a)` | reading(Cog,Att), Focus | tradition visual, familiarity, legibility | read_win (gates mode pick, Indes, counter) | engine; consistent with canon roles of Att/Cog |
| **Legibility** | C | `{point/cut_thrust-vs-plate 0.80; swing/blunt/cut 1.25} + 0.10·max(0,commit−3) + 0.25·[lunge]` | — | weapon head, commit, grip | multiplies defender's read | engine |
| **Feint** | C | `feint_q = (reading(agg)+skill_tech)·ch(agg,tempo)`; `def_read = reading(def)·ch(def,visual)·(1−0.4·mental_fat_d)`; fooled → +0.30 debuff, read → −0.12 punish | reading, skill | tradition tempo/visual, FEINT_* | debuff on defender (or punish) | engine |
| **Initiative — standing edge** | C | `init_edge = INIT_SIGMA_K(0.16)·tanh((init_agg−init_def)/INIT_SCALE(1.2))` | — (state) | initiative state | the Vor σ (attack & defence) | engine substrate; NERS-bounded |
| **Initiative — pre-contact seizure** | G | `seizure = INIT_SEIZE_READ(1.0)·reading·ch(precommit) + INIT_SEIZE_REACH(0.3)·reach + INIT_SEIZE_CONC(0.5)·(conc/conc_max) + ability(seize)`; `edge = INIT_SEIZE_K(0.45)·tanh((sa−sb)/4.0)` | reading(Cog,Att), conc(Focus,Spi) | reach, tradition precommit, ability | initial A/B initiative | engine; canon initiative=Attunement aligns w/ reading term |
| **Initiative — per-beat dynamics** | U,C | decay `×init_hold_decay` (= `1−(1−INIT_DECAY 0.75)/ch(measure)`); drift `+DISP_INIT_K(0.10)·disp_lean`; on hit `+INIT_GAIN_HIT(0.18)` / wounded `−INIT_LOSS_WOUNDED(0.28)`; `clamp ±INIT_CAP(1.5)` | disp (drift) | tradition measure, constants | evolves the Vor; damper+cap (NERS) | engine |
| **Indes / sen-no-sen steal** | C | gated `read_win & commit≥4`: `scale = clip((1+INDES_COMMIT_K(0.4)(commit−4))(1+INDES_READ_K(0.15)(read_d−read_a)), 0.5, 2.0)`; `steal = INIT_STEAL_INDES(0.36)·init_steal_factor·scale` | reading (margin) | commit, tradition tactile/leverage or tempo | moves initiative def↔agg | engine |
| **Binding** | C,B | `bind_sigma = lev + catch + tac + strq`; `lev = ΔHistory·BIND_TECH_K(0.06) + Δleverage·(ch_agg_lev/ch_def_lev)`; `catch = BIND_GUARD_K(0.55)·Δblade_guard`; `tac = Δ(reading·ch_tactile·fam)·BIND_TACTILE_K(0.04)`; `strq = Δstr·BIND_STR_K(0.0156)`. Bind loop ×3: `logistic(bind_sigma)` → strike or riposte | History, **Strength**, reading(Cog,Att), skill | weapon leverage/blade_guard, tradition leverage/tactile, familiarity | bind win → Vor steal + kuzushi; hits/riposte | engine |
| **Counter — single-time** | C | select `rng < COUNTER_SELECT_BASE(0.45)·ch(def,tempo)·max(0,1−DISP_COUNTER_K(0.5)·disp_lean(def))·ability_factor(counter_select)`; succeed `clip(COUNTER_SUCCESS_BASE(0.5)+COUNTER_TRAIN_K(0.10)(history−3)+COUNTER_REFLEX_K(0.05)(reflex−3)+ability, 0.05, 0.92)` | History (train), reflex(Agi,Att), disp | tradition tempo, abilities | success → void+riposte+keep Vor; miss → cede Vor + eat attack | engine |
| **Counter — two-time riposte** | C | on fail/neutralize: `rng < min(0.95, RIPOSTE_ON_FAIL(0.32 fail / 0.20 neut) + overcommit_exposure)` | (via overcommit) | NEUTRALIZE_*, constants | riposte (role flip) | engine |
| **Commit & overcommit** | C | `commit` ~ {2,3,4,5} skewed by `DISP_COMMIT_K(0.8)·disp_lean` (neutral=uniform); `overcommit_exposure = max(0, COMMIT_EXPOSE_K(0.06)(commit−3)) − anti_overcommit(agg) − ability`; >0 → `init −= INIT_LOSS_OVERCOMMIT(0.14)·exp/ch(tempo)`, `poise −= POISE_BREAK_OVERCOMMIT(0.09)·exp` | disp, Agility (anti_overcommit via balance) | tradition tempo, ability | commit depth; exposure → riposte/Vor/poise | engine |
| **Tempo / cadence** | U | `weapon_tempo = max(0.7, (BASE_TEMPO(2.0)+spd·SPEED_K(0.6)−pen)·(1−TEMPO_FATIGUE_K(0.25)·fat)·poise_factor)`; `pen = min(0.8, WEIGHT_PEN(0.8)[heavy]+HANDS_COMMIT(0.5)[heavy&2H]) (+choke 0.4/lunge 0.6)`; `close_tempo`: compress toward 1.5 by 0.38, −POLE_CLOSE_PENALTY(1.2) if closes_poorly & not choked | (End,Spi via fat) | weapon spd/weight/hands/grip, poise | `ready` accrual → who acts | engine |
| **Stamina & fatigue** | U,X | `stamina_max = STAMINA_PER_END(3)·End + STAMINA_PER_SPIRIT(2)·Spirit`; `act_cost = (ACT_BASE 2 + ACT_WEIGHT 1[heavy] + ACT_COMMIT 0.4·commit)·COST_SCALE 0.5`; `fat = max(0,1−stamina/max)`; `oob=2` at 0; inter-bout recover `+RECOVERY_FRAC(0.5)·…` | **Endurance, Spirit** | commit, weight, constants | fatigue → tempo/handling/balance/reads; oob → atk_sig | **= ratified canon** `derived_stats §4.2` (3×End)+(2×Spirit) |
| **Concentration** | C,X | `conc_max = CONC_BASE_K(4)·(CONC_FOCUS(3)·focus + CONC_SPIRIT(1)·spirit)/4 = 3·focus + spirit`; drains BOUT/LOSS/HIT = 3/2/2; recover `+CONC_RECOVER_FRAC(0.4)·…`; `mental_fat = fat·(1−FOCUS_MENTAL_K(0.5)·conc/conc_max)`; `consistency = FOCUS_CONSISTENCY_K(0.10)(focus−3)`; disrupt-resist `logistic(DISRUPT_K(0.7)(focus−3))` | **Focus** (¾), **Spirit** (¼) | constants | mental_fatigue resist, read consistency, disruption resist | **DIVERGES from canon** `§5.2` = Focus×3 (Focus alone; Spirit not a term) |
| **Weapon handling** | C | `handling_penalty = HANDLE_K(0.10)·max(0, str_demand−strength) + FATIGUE_HANDLE_K(0.20)·fat`; `str_demand = D0 1 + D_LEN 0.35·reach_base + D_WT 1[heavy] + D_HAND 0.6·rank + D_2H 0.4[2H]` | **Strength** | weapon length/weight/hands/grip, fat | subtracted from atk_sig **and** dsig | engine |
| **Damage** | A,C,B | `imp = HEFT[wt](4/6) + clip((str−3)//2, −1, 2)`; `cap = 1.2·(CAP_END 4 + 6) = 12`; `dmg = round(QUAL[deg](.35/1/1.5)·cap·tanh(imp·coupling·DAMAGE_SCALE 4/cap))`; coupling = transmit by head×armour×close×gap×perc | **Strength** | weapon weight/head/gap/perc, armour, degree | wound (→ WoundTracker) | engine = canonical r2 damage shape |
| **Approach — closing** | A | `close_rate = CLOSE_RATE_K(0.40)·(balance_eff(shorter)/3)·(weapon_tempo(shorter)/2)·(1+displ)`; `measure_gap −= close_rate` | Agility (balance, shorter) | weapon tempo, displ | gap shrinks toward CLOSED | engine |
| **Approach — stop-hit** | A | `stophit_p = STOPHIT_CHANCE(0.75)·min(1, gap/STOPHIT_FULL_GAP 3.0)·(1−displ)`; if fires → roll `nsig = REACH_DISADV_K(0.22)·gap + STOPHIT_NSIG_BASE(0.4)` | History (longer's pool) | gap, displ, constants | longer hits shorter on the close | engine |
| **Approach — displace** | A,C | `approach_displace = min(0.6, APPROACH_DISPLACE_K(0.7)·lever_edge·(1+0.1·read_diff))` (longer head=point, lever_edge>0); displace-and-step-inside vs committed thrust: `DISPLACE_P(0.55)` if leverage edge > `DISPLACE_LEV_GAP(0.15)` & read_win & commit≥4 | leverage(weapon), reading | weapon head, constants | suppresses stop-hit / forces close + graze + riposte | engine |
| **Reopen / separation** | C | `reopen_prob = min(0.6, REOPEN_K(0.34)·gap·(balance_eff(longer)/3)·read_edge·REACH_W[armor]/0.62 (+PUSH_REOPEN_BONUS 0.18))`; moments: shorter overcommits / longer wins defence / 2H shove (`PUSH_AVAIL_P 0.22`); separation `SEPARATION_P 0.03` or `MAX_EXCHANGES_PER_BOUT 3` | Agility (balance), reading | armour, constants | CLOSED→APPROACH, or ends bout | engine |
| **Kuzushi / poise** | U,C,B | `poise_factor = POISE_EFFECT_FLOOR(0.88) + 0.12·(clip(poise,0.5,1)−0.5)/0.5` (1.0 at full); breaks OVERCOMMIT/BIND/HIT = 0.09/0.05/0.07·…; recover `+POISE_RECOVER(0.20)·(1−poise)` | — (state; **no Focus**) | constants, tradition leverage (bind break) | scales tempo & defence (dodge, stance) | engine |
| **Half-sword auto-switch** | C | `halfsword_target`: closed & opp armour ∈ {medium,heavy} → `longsword_halfsword`, else base | — | weapon, range, armour | weapon-form swap (wrapper mutates) | engine (models "mit dem kurzen Schwert") |
| **Engagement state machine** | all | bout loop (≤12) → beat loop (≤24) → GAUGE / APPROACH / CLOSED / BIND; terminals felled / separated / undecided(0); 95 % flip | — | soft=8, max_bouts=12, UPSET_FLOOR | the whole control flow | engine |
| **Tradition channels** | C,A,G | 8 traditions × 7 channels {visual,tactile,precommit,leverage,tempo,measure,balance}; neutral=1.0; multiply substrate terms | tradition | the 7 channel weights | biases ~21 σ sites | engine; grounded S1–S3 (corpus) |
| **Tradition abilities** | C,G | equipped modulators: `seize +4.0` (Vorschlag/sen_no_sen), `counter_success +0.15` (Indes), `counter_select ×1.40` (mezzo_tempo), `anti_overcommit +0.25` (true_times); **channel levers (misura/atajo/staerke_schwaeche) INERT until eff_cw wired** | c.equipped (default ∅) | ABILITIES registry | modulate vocabulary (not unlock) | engine; provisional Class-C |
| **Familiarity** | C | same/none = 1.0; adjacent = 0.93; else 0.85 — degrades reading/bind vs unfamiliar tradition | tradition pair | ADJACENT set | multiplies read_d & bind tac | engine |
| **Weapon geometry (bake)** | I | `gap = round(min(1, (0.25+0.75·point_conc)·(0.30+0.70·cross_section^1.15)), 2)` (+thrust/cut/perc_conc/halfsword baked) | — | geometric params | overrides hand-set `gap` (only `gap` is wired live; rest baked-but-unconsumed) | engine; calibrated to reproduce §4 |

---

## 2 · MASTER TABLE — BY ATTRIBUTE

### 2a · Canonical attributes (`params/core.md:138-141` — 10 attributes, 4 groups)

| Attribute (canon) | Engine var | Canon role (`params/core`) | Engine usage & weight | Status |
|---|---|---|---|---|
| **Strength** (Str) | `strength` | physical force | damage `imp` (sole); wind defence; bind `strq` (minor); weapon handling | ✓ in engine. **PENDING:** add to balance at ½ weight (your directive) |
| **Agility** (Agi) | `agi` | **Combat Pool ×2** (PP-615); Disengage | reflex (⅔); balance_eff (`agi−1`, sole); init/tempo term (sole); reach/measure & reopen (via balance) | ✓ but **routed to σ, not the pool** — deliberate redesign deviating from PP-615 |
| **Endurance** (End) | `end` | Stamina; Health; Wound Interval | stamina_max (×3, primary); str_demand (via reach_base); recovery | ✓ matches ratified canon |
| **Cognition** (Cog) | `cog` | examine/terrain/concealment | reading (½ → ⅔ pending); — | ✓. **PENDING:** reading→(2cog+att)/3; concentration→3·cog (your 11/12) |
| **Recall / "Memory"** (Rec) | — | retention; **caps History**; Research | **not in engine** | "Memory"↔"Recall" is inference (canon writes *Recall*). Caps History upstream of combat |
| **Focus** (Foc) | `focus` | **Concentration = Focus×3** (alone) | conc (¾); consistency; mental_fat; disruption-resist | ✓. **PENDING:** poise×Focus interaction; **your 11 removes Focus from concentration** (conflicts §5.2) |
| **Attunement** (Att) | `att` | **Initiative-primary** (PP-232); social Read; thread-sensing | reading (½); reflex (⅓) | ✓ but engine under-uses Att for **initiative** (uses Agi). Item 15 ↔ canon |
| **Bonds** (Bon) | — | Disposition ceiling (PP-684); Connect; Knot pool | **not in engine** | relational; caps Disposition |
| **Charisma** (Cha) | — | Composure=Cha×3; Command; Impress | **not in engine (combat)** | social |
| **Spirit** (Spi) | `spirit` | Stamina (×2); Thread Fatigue (×5); Resolve | stamina_max (×2); concentration (×1 — **engine drift**) | ✓ as Stamina term (canon); **its concentration term diverges** from §5.2 |

### 2b · Non-attribute quantities the engine treats as primitive

| Quantity | What it is | Engine usage | Status |
|---|---|---|---|
| **History** | weapon **skill** track (canon: in Combat Pool, gated by Recall) — *not* an attribute | resolution pool (sole driver); bind `lev`; counter training; parry/wind `tech`; stamina recovery | I wrongly called it an attribute earlier — it's a skill. Pool driver is canonical (Combat Pool keys off History) |
| **disp** (disposition) | engine-invented combat **temperament/aggression** (1–7, 4=neutral) | commit skew; counter-selection lean; per-beat Vor drift | **Collides with canonical Disposition** (a derived *relational* value, ceiling=Bonds, −4..+Bonds, per-NPC). Needs rename + a decision on what combat-temperament keys off |

### 2c · Derived quantities (computed from the above)

| Derived | Formula | From |
|---|---|---|
| reading | `(cog+att)/2` **→ PENDING (2cog+att)/3** | Cog, Att |
| reflex | `(2·agi+att)/3` | Agi (⅔), Att (⅓) |
| conc_max | `3·focus + spirit` **→ PENDING 3·cog+2·spirit** | Focus, Spirit (→ Cog, Spirit) |
| stamina_max | `3·End + 2·Spirit` | End, Spirit |
| balance_eff | `(agi−1+skill)·(1−0.30·fat)·poise_factor` **→ PENDING ½agi+½str** | Agi (→ +Str) |
| leverage | `2.2·(grip_len/(grip_len+head_len)−0.30)+0.20[2H]` | weapon geometry |
| poise_factor | `0.88 + 0.12·(clip(poise,0.5,1)−0.5)/0.5` **→ PENDING add Focus** | poise state (→ Focus) |
| reach_base | `4 + 2[long] + 0.8[2H] + 1·HEAD_REACH + reach_adj` | weapon |
| anti_overcommit / stance | `0.06·(balance_eff−3)` / `0.05·(balance_eff−3)` | balance_eff |
| mental_fat / consistency | `fat·(1−0.5·conc/conc_max)` / `0.10·(focus−3)` | Focus, fat |

---

## 3 · Constants index (live `config.py` + canonical primitives)

- **Resolution/spine:** ATTACKER_BIAS 0.12 · COMMIT_SIGMA 0.18 · INIT_K 0.045 · OOB 2 · DECISIVE_OB/TN (r8) · POOL_FLOOR/BASE_POOL (r1; stored max(5,history+6))
- **Reading/reflex/focus:** READ_K 0.5 · REFLEX_AGI 2.0 · REFLEX_ATT 1.0 · FOCUS_CONSISTENCY_K 0.10 · FOCUS_MENTAL_K 0.5 · MENTAL_FAT_READ_K 0.4 · MENTAL_FAT_DEF_K 0.3 · DISRUPT_K 0.7
- **Concentration:** CONC_BASE_K 4.0 · CONC_FOCUS 3.0 · CONC_SPIRIT 1.0 · drains 3/2/2 · CONC_RECOVER_FRAC 0.4
- **Defence modes:** PARRY_K/DODGE_K/WIND_K 0.9 · CHOKE_BIND_K 0.30 · PARRY_GUARD_K 0.45 · WIND_GUARD_K 0.40 · BIND_GUARD_K 0.55 · GUARD_NEUTRAL 0.45 · GATE[weapon][mode]
- **Reach/measure/balance:** REACH_FRAC 0.82 · FOOT_MEASURE_K 0.15 · REACH_W {.62/.50/.34/.20} · L0 4/LONG 2/HANDS2 0.8/HEADR 1 · FATIGUE_FOOT_K 0.30 · FOOT_COMMIT_DISC_K 0.06 · FOOT_STANCE_K 0.05
- **Leverage/bind:** LEVER_K 2.2 · LEVER_REF 0.30 · LEVER_2H 0.20 · BIND_TECH_K 0.06 · BIND_TACTILE_K 0.04 · BIND_STR_K 0.0156
- **Armour-defeat:** ADEF_W {0/.4/1/1.7} · ADEF_BLUNT 1.3 · ADEF_POINT 1.0 · ADEF_CUT −0.9 · ADEF_THRESHOLD {0/.70/.45/.72}
- **Initiative:** INIT_SIGMA_K 0.16 · INIT_SCALE 1.2 · INIT_SEIZE_K 0.45 · _SCALE 4.0 · _READ 1.0 · _REACH 0.3 · _CONC 0.5 · INIT_DECAY 0.75 · INIT_CAP 1.5 · INIT_GAIN_HIT 0.18 · INIT_LOSS_WOUNDED 0.28 · INIT_STEAL_INDES 0.36 · INIT_LOSS_OVERCOMMIT 0.14
- **Indes:** INDES_COMMIT_K 0.4 · INDES_READ_K 0.15 · floor 0.5 / ceil 2.0
- **Counter:** COUNTER_SELECT_BASE 0.45 · COUNTER_SUCCESS_BASE 0.50 · COUNTER_TRAIN_K 0.10 · COUNTER_REFLEX_K 0.05
- **Disposition (engine):** DISP_COMMIT_K 0.8 · DISP_COUNTER_K 0.5 · DISP_INIT_K 0.10
- **Commit/overcommit & outcome:** COMMIT_EXPOSE_K 0.06 · RIPOSTE_ON_FAIL 0.32 · RIPOSTE_ON_NEUTRALIZE 0.20 · NEUTRALIZE_PARRY .55/DODGE .62/WIND .50 · _OVERWHELM_DROP 0.45 · PARTIAL_DODGE_GRAZE 0.4 · PARTIAL_PARRY_GRAZE 0.30 · WIND_BIND_P 0.55 · BIND_HIT_P 0.4
- **Tempo/stamina:** BASE_TEMPO 2.0 · SPEED_K 0.6 · WEIGHT_PEN 0.8 · HANDS_COMMIT 0.5 · MAX_TEMPO_PEN 0.8 · TEMPO_FLOOR 0.7 · TEMPO_FATIGUE_K 0.25 · CHOKE/LUNGE_TEMPO_PEN 0.4/0.6 · POLE_CLOSE_PENALTY 1.2 · CLOSE_TEMPO_MEAN 1.5 · _COMPRESS 0.38 · ACT_BASE 2 · ACT_WEIGHT 1 · ACT_COMMIT 0.4 · COST_SCALE 0.5 · STAMINA_PER_END 3 · STAMINA_PER_SPIRIT 2 · RECOVERY_FRAC 0.5 · STAMINA_REF 18
- **Handling/damage:** D0 1 · D_LEN 0.35 · D_WT 1 · D_HAND 0.6 · D_2H 0.4 · HANDLE_K 0.10 · FATIGUE_HANDLE_K 0.20 · HANDLE_RANK {0/1/2} · DAMAGE_SCALE 4.0 · CAP_END 4 · HEFT {4/6} · QUAL {.35/1/1.5}
- **Approach/feint/displace:** CLOSE_RATE_K 0.40 · STOPHIT_CHANCE 0.75 · STOPHIT_FULL_GAP 3.0 · STOPHIT_NSIG_BASE 0.4 · REACH_DISADV_K 0.22 · REACH_ADV_K 0.12 · APPROACH_DISPLACE_K 0.7/MAX 0.6 · DISPLACE_LEV_GAP 0.15 · DISPLACE_P 0.55 · DISPLACE_PULLBACK_GRAZE 0.30 · REOPEN_K 0.34/MAX 0.6 · PUSH_AVAIL_P 0.22 · PUSH_REOPEN_BONUS 0.18 · FEINT_P 0.30 · FEINT_DEBUFF 0.30 · FEINT_PUNISH 0.12 · FEINT_MAX_STREAK 3
- **Poise/control:** POISE_FLOOR 0.5 · POISE_EFFECT_FLOOR 0.88 · POISE_RECOVER 0.20 · POISE_BREAK_OVERCOMMIT/BIND/HIT 0.09/0.05/0.07 · POISE_SOLID_HIT 8.0 · MAX_EXCHANGES_PER_BOUT 3 · SEPARATION_P 0.03 · soft 8 · max_bouts 12 · UPSET_FLOOR 0.05
- **Tradition:** 8 profiles × 7 channels (neutral 1.0); FAMILIARITY_DEFAULT 0.85 / ADJACENT 0.93; ABILITIES (8 registered; 4 live levers, 3 channel levers inert)

---

## 4 · Status, pending directives, and open decisions

**Canon reconciliations (engine vs canon):**
1. **Stamina** — engine `3·End+2·Spirit` = ratified `derived_stats §4.2` (2026-05-29). **But `params/core.md:155` still shows the old `End×5`** — an un-propagated internal canon conflict.
2. **Concentration** — engine `3·focus + spirit` **diverges** from canon `§5.2` `Focus×3` ("Focus alone"). The spirit term is the source of the stamina↔concentration correlation.
3. **Pool & initiative** — engine deliberately makes the pool **Agility-independent** (`r1` docstring) and routes initiative off **Agility**; canon has Combat Pool = (Agi×2)+History+3 (PP-615) and initiative **Attunement-primary** (PP-232/239). Deliberate redesign, but it deviates from ratified canon.

**Pending directives (you gave these; NOT yet applied):**
- **#11** Concentration → `(3·Cognition + 2·Spirit)` — note this **removes Focus** and **conflicts with ratified §5.2** (Focus×3, Focus alone); needs a canon revision + ledger entry, not just a code edit.
- **#12** reading → `(2·Cognition + Attunement)/3` (Attunement at half; symmetric with the existing reflex `(2·Agi+Att)/3`).
- (#13 reflex already `(2·Agi+Att)/3` — no change needed for symmetry.)
- **balance** → ½ Agility + ½ Strength (re-centred to keep neutral at 3).
- **poise** → introduce a Focus interaction (mechanism TBD: recovery speed? break resistance? floor?).

**Open questions:**
- **#15 — initiative including History and reading:** canon supports the *reading* part (initiative is **Attunement-primary**, and reading = Cog+Att) — so adding a reading term is *canon-aligned*; **History** is not a canonical initiative driver (it's the pool/skill axis), so including it would be a new design call. My read: route initiative partly through `reading` (Attunement), leave History out — but your call.
- **#16 — where the pool rolls:** answered in §0/§1 — **two stages only** (approach stop-hit; closed exchange). If you instead meant "should it roll in more/other places," that's open.
- **disp/Disposition** collision and the **missing Charisma/Bonds/Recall** attributes — structural, your decision.

**Not yet done / not committed:** all of the above are *current-state* documentation; nothing is changed. None of this is committed to the repo (the engine has unresolved canon conflicts + pending directives, so it isn't a settled state to canonize).
