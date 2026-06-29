# Valoria Personal Combat — Attribute ↔ Mechanic Map (granular)

Traced from `combat_engine_v1` source at HEAD (`systems.py`, `core.py`, `wrapper.py`,
`combatant.py`, `config.py`), verified byte-identical to the repo this session.
Every formula below is the **actual computation**, not a paraphrase. Constants are the
live `config.py` values (all Class-C — tuned to hold the invariants, Jordan-vetoable).

## 0 · How to read this

**Two input kinds, as requested:**
- **Character statistics** — the 9 base stats (`strength, agi, end, cog, att, spirit, focus, history, disp`, each 1–7), plus the **derived** quantities computed from them (§1), plus per-axis **skills** (trained bonuses, default 0).
- **Non-character statistics** — **weapon** fields (`gap, head, blade_guard, hand_guard, spd, head_len, grip_len, hands, percussion, …`), **armour** state, **tradition** channel-weights `ch(trad, channel)` (neutral = 1.0), **dynamic states** (`poise, initiative, stamina, conc, commit, fatigue`), and **tuning constants** (the `K`s).

**The spine (§2) is the thing to hold onto.** Almost every mechanic ends as a **σ contribution** that is summed into one number, `net_sigma`, which shifts a single dice roll. So "how a mechanic is calculated" almost always means "what it contributes to `net_sigma`, and through what terms." Damage, reads, and the state machine are the exceptions that resolve on their own tracks.

Notation: `[x]` = 1 if x else 0. `ch(t,c)` = tradition t's weight on channel c. `logistic(z) = 1/(1+e^−z)`. Aggressor = the fighter acting this beat; defender = the other (roles alternate, which is why a per-beat attacker edge leaves the mirror at 50).

---

## 1 · The derived layer (character stats → intermediate quantities)

Every mechanic is built from these, not from the raw stats directly.

| Derived quantity | Formula | Built from |
|---|---|---|
| **reading** | `(cog + att) / 2` | CHAR cog, att (equal) |
| **reflex** | `(2·agi + att) / 3` | CHAR agi (⅔), att (⅓) — `REFLEX_AGI 2.0, REFLEX_ATT 1.0` |
| **conc_max** | `4.0·(3·focus + spirit) / 4` | CHAR focus (¾), spirit (¼) — `CONC_BASE_K 4.0, CONC_FOCUS 3.0, CONC_SPIRIT 1.0` |
| **stamina_max** | `r8.stamina_max(end, spirit)` | CHAR end (primary), spirit |
| **balance_eff** | `(agi − 1 + skill_balance)·(1 − 0.30·fat)·poise_factor` | CHAR agi, skill; STATE fatigue, poise — `FATIGUE_FOOT_K 0.30`. The `−1` aligns agi-neutral 4 to balance-neutral 3 |
| **leverage** | `2.2·(grip_len/(grip_len+head_len) − 0.30) + 0.20·[2H]` | WEAPON grip_len, head_len, hands — `LEVER_K 2.2, LEVER_REF 0.30, LEVER_2H 0.20` |
| **reach_base** | `4.0 + 2.0·[long] + 0.8·[2H] + 1.0·HEAD_REACH[head] + reach_adj` | WEAPON reach, hands, head, reach_adj — `L0 4, LONG 2, HANDS2 0.8, HEADR 1` |
| **poise_factor** | `0.88 + 0.12·(clip(poise,0.5,1) − 0.5)/0.5` | STATE poise — `POISE_EFFECT_FLOOR 0.88, POISE_FLOOR 0.5`; **= 1.0 at full poise** |
| **disp_lean** | `(disp − 4) / 3` ∈ [−1,1] | CHAR disp; +ve aggressive, −ve cautious, 0 neutral |
| **fatigue (fat)** | `max(0, 1 − stamina/stamina_max)` | STATE stamina ÷ DERIVED stamina_max |
| **mental_fat** | `fat·(1 − 0.5·clip(conc/conc_max,0,1))` | DERIVED fat, conc — `FOCUS_MENTAL_K 0.5`; focus(via conc) buys fatigue-resistance |
| **consistency** | `0.10·(focus − 3)` | CHAR focus — `FOCUS_CONSISTENCY_K 0.10` |
| **anti_overcommit** | `0.06·(balance_eff − 3)` | DERIVED balance_eff — `FOOT_COMMIT_DISC_K 0.06` |
| **stance_stability** | `0.05·(balance_eff − 3)` | DERIVED balance_eff — `FOOT_STANCE_K 0.05` |
| **str_demand** | `1.0 + 0.35·reach_base + 1.0·[heavy] + 0.6·HANDLE_RANK[hand] + 0.4·[2H]` | WEAPON only — `D0 1, D_LEN .35, D_WT 1, D_HAND .6, D_2H .4` |
| **handling_penalty** | `0.10·max(0, str_demand − strength) + 0.20·fat` | CHAR strength vs WEAPON demand; STATE fat — `HANDLE_K .10, FATIGUE_HANDLE_K .20` |

---

## 2 · The resolution spine (how one attack resolves)

A single closed-exchange beat. This is the backbone every σ-mechanic feeds.

```
pool       = resolution_pool(history)                      # mastery sets the d10 success-pool size
net_sigma  = atk_sig − dsig − reach_pen + adef + init_edge + 0.12   # ATTACKER_BIAS 0.12
ob         = effective_ob(DECISIVE_OB, pool, net_sigma)    # net_sigma shifts the success threshold
net        = roll_net(pool)                                # roll the pool, count successes (continuous approx)
deg        = degree(net, ob)  ∈ {fail, partial, success, overwhelming}
→ outcome mapping → hit / bind / riposte
→ if hit:  damage(...)
```

**The five σ-terms summed into `net_sigma`:**

- **`atk_sig`** `= 0.18·(commit − 3) + init − 0.5·oob − handling_penalty(agg) + consistency_a`
  - `commit` aggression (STATE, disp-skewed) — `COMMIT_SIGMA 0.18`
  - `init = 0.045·(agi_a − agi_d)·ch(agg,tempo)` — CHAR **agi** difference × TRADITION tempo — `INIT_K 0.045`
  - `oob = 2` if aggressor stamina ≤ 0 else 0 (out-of-breath) — `OOB 2`
  - `handling_penalty(agg)`, `consistency_a` (CHAR focus) — §1
- **`dsig`** (defender's mode contribution) `= mode_sigma·(1 − 0.3·mental_fat) − handling_penalty(def) + stance_stability(def)` — `MENTAL_FAT_DEF_K 0.3`. (mode_sigma in §3.2; subtracted because better defence lowers the attacker's net.)
- **`reach_pen`** = the defender's standing reach edge (§3.3) — subtracted.
- **`adef`** = the aggressor's armour-defeat capability (§3.4) — added.
- **`init_edge`** `= 0.16·tanh((init_agg − init_def)/1.2)` — STATE initiative (the Vor), bounded — `INIT_SIGMA_K 0.16, INIT_SCALE 1.2`.

**`net_sigma` is the hub:** it is the *sum of nearly every other mechanic's σ*, which is why so many attributes route into one die throw, and why a per-point attribute change moves the win rate so much.

**Degree → outcome** (per defensive mode, fixed shapes — `NEUTRALIZE_PARRY .55 / DODGE .62 / WIND .50`):
`fail` → riposte chance `min(0.95, 0.32 + overcommit_exposure)`; `partial` → graze (dodge .40 / parry .30) or bind; `success` → wind-bind (.55) / neutralize-riposte / hit; `overwhelming` → hit unless `neutralize − 0.45` voids it.

**Damage** (own track, fires only on graze/success/overwhelming):
```
imp = HEFT[wt] + clip((strength − 3)//2, −1, 2)        # HEFT light 4 / heavy 6
cap = 1.2·(CAP_END + 6) = 12                            # CAP_END 4 (global, not the fighter's end)
damage = round( QUAL[deg]·cap·tanh( imp · coupling(head,armour,close,gap,perc) · 4.0 / cap ) )
```
- CHAR **strength** (the only attribute in damage, via `imp`, capped two-step)
- WEAPON weight/head/gap/percussion + ARMOUR + degree — `QUAL graze .35 / success 1.0 / overwhelming 1.5`, `DAMAGE_SCALE 4.0`

---

## 3 · Per-mechanic granular calculations

### 3.1 Read contest (pre-contact anticipation)
```
read_d = reading(def)·ch(def,visual)·familiarity·legibility·(1 − 0.4·mental_fat_d)·(1 − feint_debuff)
read_a = reading(agg)·ch(agg,visual) + consistency_a
read_win = logistic(read_d − read_a)        # defender reads the attack?
```
- DERIVED reading (cog+att) both sides; CHAR focus via `consistency_a` and `mental_fat_d` — `MENTAL_FAT_READ_K 0.4`
- TRADITION `visual` channel; familiarity (degraded vs an unfamiliar opponent); STATE feint
- **legibility** `= {point or cut-thrust-vs-plate 0.80 ; swing/blunt/cut 1.25} + 0.10·max(0,commit−3) + 0.25·[lunge]` — WEAPON head + STATE commit/grip (`LEGIB_THRUST .80, LEGIB_SWING 1.25, LEGIB_COMMIT_K .10, LEGIB_LUNGE .25`)
- `read_win` then gates the defensive-mode pick (best mode if read, else random) **and** opens the Indes-steal / single-time counter.

### 3.2 Defensive modes — `mode_sigma` (parry / dodge / wind)
```
base = 0.5·(reading_def − reading_agg)·(1.3 if read_win else 0.7)     # READ_K 0.5
parry: 0.9·(0.45(reflex−3) + 0.45(tech−3))/3 + skill_parry + 0.45·(hand_guard − 0.45);  commit≥4 → −0.25
dodge: 0.9·(0.30(reflex−3) + 0.70(balance_eff−3))/3 + skill_dodge;    commit≥4 → +0.10 ; commit≤2 → −0.10
wind:  0.9·(0.45(tech−3) + 0.45(strength − strength_agg))/3 + 0.30·choke + skill_bind + 0.40·(blade_guard − 0.45)
mode_sigma = (base + mode_term)·GATE[weapon][mode]
```
- universal `base`: DERIVED reading (cog+att) both sides
- **parry** ← DERIVED reflex (agi,att) + `tech` (CHAR **history** + skill_technique) + WEAPON hand_guard — `PARRY_K .9, PARRY_GUARD_K .45, GUARD_NEUTRAL .45`
- **dodge** ← DERIVED reflex (0.30) + **balance_eff** (0.70, agi-governed) — `DODGE_K .9`
- **wind** ← `tech` (history) + CHAR **strength** vs aggressor's + WEAPON blade_guard + STATE choke — `WIND_K .9, CHOKE_BIND_K .30, WIND_GUARD_K .40`
- `GATE[weapon][mode]` caps each mode per weapon (e.g. rapier wind 0.4, longsword wind 1.0, dagger dodge 0.9).

### 3.3 Reach / measure — `reach_sigma`
```
gap       = reach_base(def) − reach_base(agg)
foot_meas = 0.15·(balance_eff_def·ch(def,balance) − balance_eff_agg·ch(agg,balance))
meas_w    = ch(def,measure) / ch(agg,measure)
reach_pen = REACH_W[def.armor]·((gap·0.82 + foot_meas)·meas_w)
```
- DERIVED reach_base (WEAPON geometry) + **balance_eff** (CHAR agi) + TRADITION balance & measure channels + ARMOUR scaling — `REACH_FRAC .82, FOOT_MEASURE_K .15, REACH_W none .62 / light .50 / medium .34 / heavy .20`
- the armour term is why reach dominates unarmoured and decays toward the clinch in plate.

### 3.4 Armour-defeat — `armor_defeat_sigma`
```
a = ADEF_W[def.armor]            # none 0 / light .4 / medium 1.0 / heavy 1.7 ; 0 ⇒ no effect
cap = { blunt: 1.3·(percussion/8) ; point: 1.0·gap ; cut_thrust: max(−0.9, 1.0·gap) ; cut: −0.9 }
adef = a·(cap − ADEF_THRESHOLD[def.armor])     # threshold none 0 / light .70 / medium .45 / heavy .72
```
- WEAPON head/percussion/gap + ARMOUR only — **no character stat**. `ADEF_BLUNT 1.3, ADEF_POINT 1.0, ADEF_CUT −0.9`. Pure cut collapses vs plate; percussion & gap-thrust gain.

### 3.5 Initiative / the Vor (state, three sub-mechanics)
- **Standing edge** (into net_sigma): `init_edge = 0.16·tanh(Δinitiative/1.2)` — holds on attack *and* defence.
- **Pre-contact seizure** (who enters holding the Vor):
  ```
  seizure_score = 1.0·reading·ch(precommit) + 0.3·reach + 0.5·(conc/conc_max) + ability(seize)
  edge = 0.45·tanh((score_a − score_b)/4.0)        # symmetric: equal fighters → 0
  ```
  DERIVED reading (cog+att) + WEAPON reach + DERIVED conc (focus,spirit) + equipped ability — `INIT_SEIZE_READ 1.0, _REACH 0.3, _CONC 0.5, _K 0.45, _SCALE 4.0`.
- **Per-beat dynamics:** drift `init += 0.10·disp_lean` (CHAR disp); decay ×0.75/beat (damper); hard cap ±1.5 (bound); `+0.18` on landing a hit, `−0.28` when wounded — `INIT_DECAY .75, INIT_CAP 1.5, DISP_INIT_K .10, INIT_GAIN_HIT .18, INIT_LOSS_WOUNDED .28`.

### 3.6 Indes / sen-no-sen steal (read-driven Vor flip)
Gated on `read_win and commit ≥ 4`:
```
scale = clip( (1 + 0.4·(commit−4))·(1 + 0.15·(read_d − read_a)), 0.5, 2.0 )
steal = 0.36·init_steal_factor(def, in_bind)·scale            # moved between the two fighters' initiative
init_steal_factor = in_bind ? (ch(tactile)+ch(leverage))/2 : ch(tempo)
```
- STATE commit-depth × read-margin (DERIVED reading) + TRADITION tactile/leverage (in a bind) or tempo (open) — `INIT_STEAL_INDES .36, INDES_COMMIT_K .4, INDES_READ_K .15, floor .5 / ceil 2.0`. σ-bounded downstream by the `tanh` in init_edge.

### 3.7 Binding — `bind_sigma`
```
lev   = ((history_agg+skill) − (history_def+skill))·0.06 + (leverage_agg − leverage_def)·(ch(agg,leverage)/ch(def,leverage))
catch = 0.55·(blade_guard_agg − blade_guard_def)
tac   = (reading_agg·ch(agg,tactile)·fam − reading_def·ch(def,tactile)·fam)·0.04
strq  = (strength_agg − strength_def)·0.0156
bind_sigma = lev + catch + tac + strq
```
- CHAR **history** (primary, `BIND_TECH_K .06`) + DERIVED leverage (WEAPON) × TRADITION leverage + WEAPON blade_guard (`BIND_GUARD_K .55`) + DERIVED reading × TRADITION tactile (`BIND_TACTILE_K .04`) + CHAR **strength** (minor, `BIND_STR_K .0156`).

### 3.8 Countering (single-time counter + riposte)
```
selection : rng < 0.45·ch(def,tempo)·max(0, 1 − 0.5·disp_lean(def))·ability_factor(counter_select)   # gated on read_win & commit≥4
success   : clip( 0.50 + 0.10·(history−3) + 0.05·(reflex−3) + ability(counter_success), 0.05, 0.92 )
            success → void attack + riposte + KEEP the seized Vor
            miss    → cede the Vor back + eat the attack UNDEFENDED (the downside)
```
- selection ← TRADITION tempo + CHAR disp (cautious favours it) + ability — `COUNTER_SELECT_BASE .45, DISP_COUNTER_K .5`
- success ← CHAR **history** (training, `COUNTER_TRAIN_K .10`) + DERIVED reflex (agi,att, `COUNTER_REFLEX_K .05`) + ability — `COUNTER_SUCCESS_BASE .50`
- the **two-time riposte** (on a failed/neutralized attack) is the universal fallback: `min(0.95, 0.32 + overcommit_exposure)` / `min(0.95, 0.20 + overcommit_exposure)`.

### 3.9 Commit & overcommit
```
commit ~ distribution over {2,3,4,5}, skewed by 0.8·disp_lean(agg)   # neutral → uniform ; DISP_COMMIT_K 0.8
overcommit_exposure = max(0, 0.06·(commit−3)) − anti_overcommit(agg) − ability(anti_overcommit)   # COMMIT_EXPOSE_K .06
if exposure > 0:  initiative −= 0.14·exposure/ch(agg,tempo);  poise −= 0.09·exposure
```
- CHAR **disp** sets depth; DERIVED **anti_overcommit** (CHAR agi via balance_eff) curbs the exposure; TRADITION tempo (true-times) softens the Vor loss — `INIT_LOSS_OVERCOMMIT .14, POISE_BREAK_OVERCOMMIT .09`. Exposure also raises the defender's riposte chance (§3.8) and feeds the read-legibility (§3.1).

### 3.10 Tempo / cadence
```
weapon_tempo = max(0.7, (2.0 + spd·0.6 − pen)·(1 − 0.25·fat)·poise_factor)
pen = min(0.8, 0.8·[heavy] + 0.5·[heavy & 2H])  (+0.4 choke / +0.6 lunge grip)
close_tempo  = 1.5 + (weapon_tempo − pole_pen − 1.5)·0.38      # compressed toward the mean; pole_pen 1.2 if closes_poorly & not choked
```
- WEAPON spd/weight/hands/grip + STATE fatigue (CHAR end+spirit via stamina) + STATE poise — `BASE_TEMPO 2.0, SPEED_K .6, WEIGHT_PEN .8, TEMPO_FATIGUE_K .25, TEMPO_FLOOR .7, POLE_CLOSE_PENALTY 1.2, CLOSE_TEMPO_MEAN 1.5, CLOSE_TEMPO_COMPRESS .38`. Action-frequency is a secondary edge by design; reach governs.

### 3.11 Stamina & fatigue
```
stamina_max = r8.stamina_max(end, spirit)
act_cost    = (2.0 + 1.0·[heavy] + 0.4·commit)·0.5            # ACT_BASE 2, ACT_WEIGHT 1, ACT_COMMIT .4, COST_SCALE .5
fat         = max(0, 1 − stamina/stamina_max)   →   oob = 2 if stamina ≤ 0
```
- CHAR **end** (primary) + **spirit**; STATE commit drives the cost. Fatigue then degrades tempo (§3.10), reads (mental_fat), balance_eff, and handling.

### 3.12 Concentration & mental game
```
conc_max = 4.0·(3·focus + spirit)/4
drains: −3 per bout, −2 per loss, −2 per hit ; recover +0.4·(conc_max − conc)/beat
disruption-resistance (complete despite a blow): logistic(0.7·(focus − 3))
```
- CHAR **focus** (¾) + **spirit** (¼) — `CONC_DRAIN_BOUT 3, _LOSS 2, _HIT 2, CONC_RECOVER_FRAC .4, DISRUPT_K .7`. Concentration's output is fatigue-resistance (`mental_fat`), read consistency, and disruption-resistance.

### 3.13 Weapon handling
`handling_penalty = 0.10·max(0, str_demand − strength) + 0.20·fat` — CHAR **strength** vs WEAPON demand + STATE fat. Subtracted from **both** `atk_sig` and `dsig` (an under-strength fighter is worse attacking *and* defending).

### 3.14 Feint
```
feint_q  = (reading(agg) + skill_technique)·ch(agg,tempo)
def_read = reading(def)·ch(def,visual)·(1 − 0.4·mental_fat_d)
fooled → defender's read/defence debuffed +0.30 ; read → aggressor punished −0.12
```
- DERIVED reading both sides + TRADITION tempo/visual — `FEINT_P .30, FEINT_DEBUFF .30, FEINT_PUNISH .12, MAX_STREAK 3`.

### 3.15 Approach (closing, stop-hit, displace, reopen)
- **stop-hit** (longer weapon hits as the shorter closes): `STOPHIT_CHANCE .75`, magnitude scaled by the reach gap (`STOPHIT_NSIG_BASE .4, STOPHIT_FULL_GAP 3.0`).
- **approach_displace** (a higher-leverage closer sets aside a thrusting point): `min(0.6, 0.7·lever_edge·(1 + 0.1·read_diff))` — DERIVED leverage + reading; WEAPON head must be `point`.
- **reopen_prob** (longer weapon regains distance): `0.34·base_gap·(balance_eff/3)·read_edge·REACH_W[armor]/0.62 (+0.18·foot if a shove is available)` — DERIVED balance_eff (agi) + reading + ARMOUR — `REOPEN_K .34, REOPEN_MAX .6, PUSH_REOPEN_BONUS .18`.

---

## 4 · Chart A — attribute → every mechanic it enters

| Attribute | Enters via | Mechanics reached |
|---|---|---|
| **history** | resolution pool; `tech`; bind `lev`; counter success | the **dice pool** (sole) · parry · wind · binding (primary) · countering (training) |
| **agi** | reflex (⅔); balance_eff (`agi−1`); `init`; seizure | dodge · parry (reflex) · counter (reflex) · measure & closing · anti-overcommit · stance · initiative tempo-term · reopen |
| **cog** | reading (½) | read contest · mode base · seizure · feint · bind tactile |
| **att** | reading (½) + reflex (⅓) | everything reading touches **and** everything reflex touches (double-counted → tested joint-highest) |
| **strength** | damage `imp`; wind; bind `strq`+leverage feel; handling | striking (sole) · wind defence · binding (minor) · weapon-handling |
| **focus** | conc (¾); consistency; mental_fat; disruption | concentration · read consistency · fatigue-resistance · disruption-resistance |
| **spirit** | stamina; conc (¼) | stamina pool (with end) · concentration |
| **end** | stamina (primary) | stamina → fatigue → tempo, handling, balance, reads |
| **disp** | disp_lean | commit depth · counter-selection lean · per-beat Vor drift |

(Weapon, armour, and tradition channels are non-character inputs; their per-mechanic entry points are in §3. The single largest structural fact: **`net_sigma` is the sum of §3's σ-terms**, so a change to almost any attribute reaches the resolution roll through it.)

---

## 5 · Constant index (by subsystem, live `config.py` values)

- **Resolution / spine:** `ATTACKER_BIAS 0.12, COMMIT_SIGMA 0.18, INIT_K 0.045, OOB 2, DECISIVE_OB/TN` (canonical r1/r8)
- **Reading / reflex / focus:** `READ_K 0.5, REFLEX_AGI 2.0, REFLEX_ATT 1.0, FOCUS_CONSISTENCY_K 0.10, FOCUS_MENTAL_K 0.5, MENTAL_FAT_READ_K 0.4, MENTAL_FAT_DEF_K 0.3, DISRUPT_K 0.7`
- **Concentration:** `CONC_BASE_K 4.0, CONC_FOCUS 3.0, CONC_SPIRIT 1.0, CONC_DRAIN_BOUT/LOSS/HIT 3/2/2, CONC_RECOVER_FRAC 0.4`
- **Defence modes:** `PARRY_K/DODGE_K/WIND_K 0.9, CHOKE_BIND_K 0.30, PARRY_GUARD_K 0.45, WIND_GUARD_K 0.40, BIND_GUARD_K 0.55, GUARD_NEUTRAL 0.45`, `GATE[weapon][mode]`
- **Reach / measure:** `REACH_FRAC 0.82, FOOT_MEASURE_K 0.15, REACH_W {.62/.50/.34/.20}`, `L0 4, LONG 2, HANDS2 0.8, HEADR 1`
- **Balance / footwork:** `FATIGUE_FOOT_K 0.30, FOOT_COMMIT_DISC_K 0.06, FOOT_STANCE_K 0.05`
- **Leverage / bind:** `LEVER_K 2.2, LEVER_REF 0.30, LEVER_2H 0.20, BIND_TECH_K 0.06, BIND_TACTILE_K 0.04, BIND_STR_K 0.0156`
- **Armour-defeat:** `ADEF_W {0/.4/1.0/1.7}, ADEF_BLUNT 1.3, ADEF_POINT 1.0, ADEF_CUT −0.9, ADEF_THRESHOLD {0/.70/.45/.72}`
- **Initiative:** `INIT_SIGMA_K 0.16, INIT_SCALE 1.2, INIT_SEIZE_K 0.45, _SCALE 4.0, _READ 1.0, _REACH 0.3, _CONC 0.5, INIT_DECAY 0.75, INIT_CAP 1.5, INIT_GAIN_HIT 0.18, INIT_LOSS_WOUNDED 0.28, INIT_STEAL_INDES 0.36, INIT_LOSS_OVERCOMMIT 0.14`
- **Indes flip:** `INDES_COMMIT_K 0.4, INDES_READ_K 0.15, SCALE_FLOOR 0.5, SCALE_CEIL 2.0`
- **Counter:** `COUNTER_SELECT_BASE 0.45, COUNTER_SUCCESS_BASE 0.50, COUNTER_TRAIN_K 0.10, COUNTER_REFLEX_K 0.05`
- **Disposition:** `DISP_COMMIT_K 0.8, DISP_COUNTER_K 0.5, DISP_INIT_K 0.10`
- **Commit / overcommit:** `COMMIT_EXPOSE_K 0.06`, riposte `RIPOSTE_ON_FAIL 0.32, RIPOSTE_ON_NEUTRALIZE 0.20`, neutralize `PARRY .55 / DODGE .62 / WIND .50, OVERWHELM_DROP 0.45`
- **Tempo / stamina:** `BASE_TEMPO 2.0, SPEED_K 0.6, WEIGHT_PEN 0.8, HANDS_COMMIT 0.5, MAX_TEMPO_PEN 0.8, TEMPO_FLOOR 0.7, TEMPO_FATIGUE_K 0.25, CHOKE/LUNGE_TEMPO_PEN 0.4/0.6, POLE_CLOSE_PENALTY 1.2, CLOSE_TEMPO_MEAN 1.5, _COMPRESS 0.38`, `ACT_BASE 2, ACT_WEIGHT 1, ACT_COMMIT 0.4, COST_SCALE 0.5`
- **Handling:** `D0 1, D_LEN 0.35, D_WT 1, D_HAND 0.6, D_2H 0.4, HANDLE_K 0.10, FATIGUE_HANDLE_K 0.20, HANDLE_RANK {Forgiving 0 / Standard 1 / Demanding 2}`
- **Damage:** `DAMAGE_SCALE 4.0, CAP_END 4, HEFT {light 4 / heavy 6}, QUAL {graze .35 / success 1.0 / overwhelming 1.5}`, RESIST/DELIVERY tables (head × armour)
- **Legibility / feint / displace:** `LEGIB_THRUST 0.80, LEGIB_SWING 1.25, LEGIB_COMMIT_K 0.10, LEGIB_LUNGE 0.25`, `FEINT_P 0.30, FEINT_DEBUFF 0.30, FEINT_PUNISH 0.12`, `APPROACH_DISPLACE_K 0.7/MAX 0.6, REOPEN_K 0.34/MAX 0.6`
- **Poise / cap:** `POISE_FLOOR 0.5, POISE_EFFECT_FLOOR 0.88, POISE_RECOVER 0.20, POISE_BREAK_OVERCOMMIT/BIND/HIT 0.09/0.05/0.07, UPSET_FLOOR 0.05`
