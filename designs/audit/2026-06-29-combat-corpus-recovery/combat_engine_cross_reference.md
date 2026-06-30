# Valoria Personal-Combat Engine — Cross-Reference Tables

**Built from a full fresh read of every engine module at HEAD this session** (incl. the committed −1D/wound wiring `deb405b9` and the concurrent `config.py` edit from a parallel session). No values are from memory or prior context; every cell traces to a module:line read this turn.

**Scope.** The *live* engine is `wrapper.py` (state graph) + `systems.py` (mechanics) + `core.py` (resolver/damage) + `combatant.py` (attributes, equipment) + `config.py` (constants) + `geometry.py` (build-time weapon bake) + `tradition.py`. The leaf math lives in the `v32/` primitives: `r1` (effective-Ob, degree), `r8` (pool, roll, stamina, re-exports), `r2` (WoundTracker), `r5` (stamina), `m1` (the d10 roll, TN). **Note:** `r8`/`r1` also contain a *legacy* `resolve_phrase`/`run` parity harness — that is **not** the live path; the engine touches only the primitives those modules expose, via `core`.

Three quantity categories (used in the flag column): **base parameter** (1–7 stat), **derived resource** (depletes), **discrete accumulator** (wounds).

---

## §0 · State-Graph Map

```
fight(A,B,max_bouts=12)         ── multi-turn SIM harness; the GAME runs ONE engagement/turn
  └ per turn:
      • first-mover coin flip (rng<0.5)
      • engagement(A,B,first) ──────────► felled Combatant | None
      • felled → result ±1, stop
      • else BETWEEN-TURN RECOVERY: stamina regen · conc regen
  └ NO auto-tiebreak (unresolved = draw 0) · 95% UPSET_FLOOR clamp on decided results

engagement(A,B,first)
 PRE-CONTACT
   reach_base(A),(B) → longer/shorter (coin-flip on EXACT tie)
   initiative_seize → A.initiative,B.initiative
 BEAT LOOP (while beats<24)
   per-beat dampers:  init_hold_decay(×) + disp_lean drift → clamp_initiative ;  poise recovery → clamp_poise
   tempo:  weapon_tempo (approach) | close_tempo (closed) → ready[c]+=rate
   [closed & moment] REACH RE-OPENING → reopen_prob → maybe re-open
   ├ APPROACH (not closed)
   │   approach_displace · close_rate → measure_gap shrinks
   │   STOP-HIT (p∝gap):  ROLL#1  pool=max(1, resolution_pool(longer.History) − longer.wt.pool_penalty())
   │                       → effective_ob → roll_net → degree → strike → apply_wound
   │   stamina≤−4 → separate
   └ CLOSED (ready≥ACT_THRESHOLD)
       aggressor=max ready ; half-sword auto-switch ; commit{2..5}(disp) ; act_cost→stamina ; OOB
       build:  mental_fat · reach_sigma · init(tempo) · consistency(Focus) · FEINT
       VISUAL READ:  read_d vs read_a → read_win ;  MODE parry/dodge/wind (mode_sigma)
       net_sigma = atk_sig − dsig − reach_pen + adef + init_edge + ATTACKER_BIAS
       INDES STEAL (read_win & commit≥4) · COUNTER selection
       MAIN ROLL#2  pool=max(1, resolution_pool(aggressor.History) − aggressor.wt.pool_penalty())
                     → effective_ob → roll_net → degree
       overcommit_exposure → init/poise loss
       OUTCOME: fail→riposte? · partial→graze/bind · success→bind/neutralize/hit · overwhelming→hit
       COUNTER resolve · DISPLACE-step-inside · reopen flags
       HIT → apply_wound · conc↓ · init± · poise↓ · felled?
       BIND sub-loop (≤3): bind_sigma → kuzushi → bind hits
       RIPOSTE → disruption-resistance(Focus) · conc↓ · ROLE FLIP
       BURST exit:  stamina≤−4 | exchanges≥BURST_MAX(4) | clean-defence → separate
```

---

## §1 · MECHANICS — composition & place in state graph

| Mechanic | Composition (inputs → output) | Module · fn | Fires at (node) |
|---|---|---|---|
| **Resolution roll** | roll `pool` d10s, success = die ≥ TN(=7), success-count → continuous `net` | `core.roll_net` → `m1.roll_net_continuous` | Stop-hit; Main exchange |
| **Combat Pool** | `max(5, History+6) − wt.pool_penalty()`  (wound −1D/wound; floor 1) | `core.resolution_pool` (`r1`) + wrapper subtraction | both roll sites |
| **Effective Ob** | `max(1, eff_ob(DECISIVE_OB=3, pool, net_sigma))` — higher net_sigma lowers Ob | `core.effective_ob` → `r1.effective_ob` | both roll sites |
| **Degree band** | fail `net≤0` · partial `0<net<Ob` · success `net≥Ob` · overwhelming `net≥2·Ob ∧ net≥3` | `r1.degree_of_success` | both roll sites |
| **net_sigma (main)** | `atk_sig − dsig − reach_pen + adef + init_edge + ATTACKER_BIAS(0.12)` | `wrapper` inline | Closed exchange |
| **atk_sig** | `COMMIT_SIGMA·(commit−3) + init − OOB·0.5 − handling_penalty + consistency` | `wrapper` inline | Closed |
| **Damage / strike** | `QUAL[deg]·cap·tanh(imp·coupling·SCALE/cap)`; `imp=HEFT[wt]+clip((Str−3)//2,−1,2)`; `cap=1.2·(CAP_END+6)` | `core.strike→damage→coupling` | every hit |
| **Coupling (transmit)** | by head×armor: blunt`·perc/8` · point`(gap-find vs plate)` · cut_thrust`max(cut,point)` · cut | `core.coupling/_mode_transmit` | inside damage |
| **Wound gate** | `wi=End+6` · `wounds=⌊cum/wi⌋` (cap MW+1) · `MW=min(⌊End/2⌋+1, 3)` · `felled` at MW+1 · `health=(End+6)(MW+1)` · `pool_penalty=−1·min(wounds,MW+1)` | `r2.WoundTracker` | `apply_wound` everywhere |
| **reach_base** | `L0+LONG·long+HANDS2·2H+HEADR·HEAD_REACH[head]+reach_adj` | `systems.reach_base` | engagement init |
| **reach_sigma** (standing reach pen) | `REACH_W[def.armor]·((gap·REACH_FRAC+foot_meas)·measure_ratio)` | `systems.reach_sigma` | Closed (`reach_pen`) |
| **close_rate** (approach) | `CLOSE_RATE_K·balance_eff(shorter)/3·weapon_tempo/2·(1+displace)` | `wrapper` + `systems.approach_displace` | Approach |
| **approach_displace** | `min(MAX, K·(lev_shorter−lev_longer)·(1+0.1·read))` iff longer head=point | `systems.approach_displace` | Approach |
| **reopen_prob** | `REOPEN_K·gap·foot·read_edge·REACH_W[shorter.armor]/0.62 (+push)` | `systems.reopen_prob` | Reach re-opening |
| **stop-hit chance** | `STOPHIT_CHANCE·min(1, gap/FULL_GAP)·(1−displace)` | `wrapper` inline | Approach |
| **weapon_tempo** | `BASE+spd·SPEED_K+AGI_TEMPO_K·(Agi−4) − pen(wt,2H,grip)`, `×(1−FAT·fat)×poise_factor`, floor | `systems.weapon_tempo` | beat-loop tempo |
| **close_tempo** | `weapon_tempo − POLE_CLOSE_PENALTY (closes_poorly & ¬choke)`, compressed → CLOSE_TEMPO_MEAN | `systems.close_tempo` | beat-loop (closed) |
| **act_cost** | `(ACT_BASE+ACT_WEIGHT·heavy+ACT_COMMIT·commit)·COST_SCALE` | `systems.act_cost` | Closed (stamina drain) |
| **commit** | `{2..5}` uniform; disp-skewed by `DISP_COMMIT_K·lean` | `wrapper` inline | Closed |
| **stamina_max** | `3·End + 2·Spirit` | `systems.stamina_max` (`r5`) | init |
| **stamina recovery** | `+RECOVERY_FRAC·(max−cur)·(max/STAMINA_REF)` | `wrapper.fight` | between-turn |
| **handling_penalty** | `HANDLE_K·max(0, str_demand−Str) + FATIGUE_HANDLE_K·fat` | `systems.handling_penalty` | atk_sig & dsig |
| **str_demand** | `D0+D_LEN·reach+D_WT·heavy+D_HAND·HANDLE_RANK[hand]+D_2H·2H` | `systems.str_demand` | handling_penalty |
| **conc_max** | `3·Focus + 2·Spirit` | `systems.conc_max` | init |
| **conc drains** | `−CONC_DRAIN_HIT` (hit) · `−CONC_DRAIN_LOSS` (lost exchange) · `−CONC_DRAIN_BOUT` (per turn) | `wrapper` inline | hits / riposte / between-turn |
| **mental-fat protection** | `mental_fat_d = fat_d·(1 − FOCUS_MENTAL_K·conc_frac)` | `wrapper` inline | Closed (read & defence) |
| **consistency (Focus)** | `FOCUS_CONSISTENCY_K·(Focus−3)` → added to `atk_sig` and `read_a` | `wrapper` inline | Closed |
| **disruption-resistance** | `sigmoid(DISRUPT_K·(Focus−3))` → aggressor completes despite blow | `wrapper` inline | Riposte (simultaneous) |
| **reading** | `(2·Cog + Att)/3 + READ_HISTORY_K·(History−3)` | `systems.reading` | visual read, feint, mode_sigma, seizure, bind tactile, init term |
| **reflex** | `(2·Agi + Att)/3` | `systems.reflex` | mode_sigma (parry/dodge), counter success |
| **visual read** | `read_d` vs `read_a` → sigmoid → `read_win`; each `= reading × visual-channel × familiarity × legibility × (1−fat) × (1−feint)` | `wrapper` inline | Closed |
| **legibility** | head-mode (thrust hard 0.80 / swing-blunt easy 1.25) `+ LEGIB_COMMIT_K·(commit−3) + LEGIB_LUNGE` | `systems.legibility` | read_d |
| **mode_sigma** | `(base + mode)·GATE[weapon][mode]`; base`=READ_K·Δread·(read_win?1.3:0.7)`; parry`=reflex+tech+hand_guard`; dodge`=reflex+balance`; wind`=tech+ΔStr+blade_guard` | `systems.mode_sigma` | Closed (`dsig`) |
| **neutralize** | fixed per mode: PARRY .55 / DODGE .62 / WIND .50; overwhelming `−OVERWHELM_DROP` | `wrapper` (cfg) | Outcome map |
| **balance_eff** | `(½Agi + ½Str − 1 + skill('balance'))·(1−FATIGUE_FOOT_K·fat)·poise_factor` | `systems.balance_eff` | dodge, stance, anti-overcommit, reach foot, reopen |
| **stance_stability** | `FOOT_STANCE_K·(balance_eff−3)` | `systems.stance_stability` | dsig |
| **anti_overcommit** | `FOOT_COMMIT_DISC_K·(balance_eff−3)` | `systems.anti_overcommit` | overcommit_exposure |
| **seizure_score** | `SEIZE_READ·(reading×precommit) + SEIZE_REACH·reach + SEIZE_CONC·(conc/max) + ability(seize)` | `systems.seizure_score` | pre-contact |
| **initiative_seize** | `INIT_SEIZE_K·tanh((s_a−s_b)/SCALE)` → signed, symmetric | `systems.initiative_seize` | pre-contact |
| **initiative_sigma (edge)** | `INIT_SIGMA_K·tanh((agg.init − def.init)/INIT_SCALE)` (Vor edge, attack **and** defence) | `systems.initiative_sigma` | net_sigma (`init_edge`) |
| **init decay (damper)** | `× init_hold_decay = 1−(1−INIT_DECAY)/measure-channel` | `systems.init_hold_decay` | beat loop |
| **init cap (bound)** | clamp `±INIT_CAP(1.5)` | `systems.clamp_initiative` | every init change |
| **indes steal** | `INIT_STEAL_INDES·init_steal_factor·indes_scale(commit-depth × read-margin)` | `wrapper` + `systems.init_steal_factor` | Closed (read_win & commit≥4) |
| **init on hit** | `+INIT_GAIN_HIT` (aggressor) · `−INIT_LOSS_WOUNDED` (defender) | `wrapper` inline | hit |
| **init overcommit loss** | `INIT_LOSS_OVERCOMMIT·exposure / tempo-channel` | `systems.init_overcommit_loss` | overcommit |
| **disp init lever** | `DISP_INIT_K·disp_lean` (aggressive drifts Vor up, cautious down) | `wrapper` inline | beat loop |
| **bind_sigma** | `BIND_TECH_K·Δ(History+skill) + Δleverage·(leverage-ratio) + BIND_GUARD_K·Δblade_guard + BIND_TACTILE_K·Δ(reading×tactile×familiarity) + BIND_STR_K·ΔStr` | `systems.bind_sigma` | Bind entry + sub-loop |
| **bind sub-loop** | `range(3)`: `sigmoid(bind_sigma)` → `BIND_HIT_P` hit else riposte | `wrapper` inline | Bind |
| **kuzushi (bind break)** | bind winner breaks loser poise `POISE_BREAK_BIND × leverage-channel` | `wrapper` inline | Bind |
| **counter selection** | `COUNTER_SELECT_BASE × tempo-channel × max(0,1−DISP_COUNTER_K·lean) × ability(counter_select)` | `wrapper` inline | Closed |
| **counter success** | `COUNTER_SUCCESS_BASE + COUNTER_TRAIN_K·(History−3) + COUNTER_REFLEX_K·(reflex−3) + ability(counter_success)` | `wrapper` inline | Outcome |
| **riposte (2-time)** | on fail/neutralize: `RIPOSTE_ON_FAIL` / `RIPOSTE_ON_NEUTRALIZE` (+overcommit) | `wrapper` inline | Outcome |
| **role flip** | aggressor↔defender on riposte | `wrapper` inline | Riposte |
| **feint_eval** | `do` iff (FEINT_P, streak<3, stamina>0); `feint_q` vs `def_read` → debuff `FEINT_DEBUFF` or punish `−FEINT_PUNISH` | `systems.feint_eval` | Closed |
| **disp_lean** | `(disp−4)/3` ∈ [−1,1]; three hooks (commit skew, counter tilt, init lever) | `systems.disp_lean` | Closed / beat loop |
| **armor_defeat_sigma** | `ADEF_W[armor]·(cap − ADEF_THRESHOLD[armor])`; cap: blunt`·perc/8` · point`·gap` · cut_thrust`max(cut,point·gap)` · cut`(negative)` | `systems.armor_defeat_sigma` | net_sigma (`adef`) |
| **poise_factor** | maps poise[0.5,1] → [POISE_EFFECT_FLOOR,1] multiplier on tempo & defence | `systems.poise_factor` | weapon_tempo, balance_eff |
| **poise breaks** | overcommit `POISE_BREAK_OVERCOMMIT` · bind `POISE_BREAK_BIND` · hit `POISE_BREAK_HIT·min(1,hit/SOLID)` | `wrapper` inline | overcommit / bind / hit |
| **displace-step-inside** | vs head=point ∧ commit≥4 ∧ read_win ∧ leverage gap: `DISPLACE_P` → close + pullback graze | `wrapper` inline | Outcome |
| **half-sword switch** | longsword ↔ longsword_halfsword iff closed ∧ opp armor ∈ {medium,heavy} | `systems.halfsword_target` | Closed (weapon mutation) |
| **channel_weight** | per-tradition multiplier on a substrate channel | `tradition.channel_weight` | ~all read/init/bind sites |
| **familiarity** | cross-tradition read: 1.0 same/none · .93 adjacent · .85 default | `tradition.familiarity` | visual read, bind tactile |
| **ability bonus/factor** | equipped-ability `+`/`×` on a lever | `tradition.ability_bonus/factor` | seize, counter, anti-overcommit (live) |
| **ATTACKER_BIAS** | `+0.12` to net_sigma (first-mover edge; mirror holds because aggressor alternates) | `wrapper` (cfg) | net_sigma |
| **UPSET_FLOOR** | decided result flipped with p=0.05 (no matchup is certain) | `wrapper.fight` | result |

---

## §2 · ATTRIBUTES — role in mechanics & state graph

| Attribute | Cat. | Mechanics it feeds (touchpoint) | Where in graph | Notes |
|---|---|---|---|---|
| **History** | base | **Combat Pool** `max(5,History+6)` (sets roll size at BOTH rolls); `reading` (+`READ_HISTORY_K·(H−3)`); mode_sigma `tech` (parry/wind); `bind_sigma` tech; `init` term (`INIT_HISTORY_K`); `counter success` (`COUNTER_TRAIN_K`) | every roll, read, bind, init, counter | **most touchpoints**; the only attribute that sizes the dice pool. Weapon-skill axis (canon: capped by Recall) |
| **Cog** | base | `reading = (2·Cog+Att)/3` (primary term) | wherever reading is read (read, feint, mode base, seizure, bind tactile, init) | single channel (reading), but reading is pervasive → highest measured per-point value |
| **Att** | base | `reading` (half: `(2Cog+Att)/3`) **and** `reflex = (2Agi+Att)/3` | read sites + reflex sites | **double-dips** reading + reflex |
| **Agi** | base | `reflex` (primary); `balance_eff` (½Agi); `weapon_tempo` (`AGI_TEMPO_K·(Agi−4)`, small); `init` (`INIT_K·ΔAgi`) | tempo, reflex, balance, init | tempo + reflex + balance |
| **Strength** | base | **damage** `imp` (`+clip((Str−3)//2,−1,2)`); `balance_eff` (½Str); mode_sigma `wind` (`ΔStr`); `bind_sigma` (`BIND_STR_K`); `handling_penalty` (vs str_demand) | damage, balance, bind, handling | **non-uniform / saturating** delivery curve (the one clear Lesson-2 flag) |
| **End** | base | `stamina_max` (`3·End`); WoundTracker `wi=End+6`, `MW=min(⌊End/2⌋+1,3)`, `health=(End+6)(MW+1)` | stamina reserve + wound capacity / health | durability axis; gates how many −1D wounds you can take before felling |
| **Spirit** | base | `stamina_max` (`2·Spirit`); `conc_max` (`2·Spirit`) | stamina + concentration (secondary in both) | conditionally valuable in long/heavy fights |
| **Focus** | base | `conc_max` (`3·Focus`, primary); `consistency` (`FOCUS_CONSISTENCY_K·(Focus−3)` → atk_sig & read_a); `mental-fat protection` (`FOCUS_MENTAL_K`); `disruption-resistance` (`DISRUPT_K`); `poise recovery` (`POISE_FOCUS_K`) | concentration, consistency, mental-fatigue, disruption, poise | **many small-coefficient touchpoints** → under-*weighted*, not under-*wired* |
| **Disposition** | base | `disp_lean=(disp−4)/3` → commit skew (`DISP_COMMIT_K`), counter-select tilt (`DISP_COUNTER_K`), init lever (`DISP_INIT_K`) | commit, counter select, beat-loop init | shapes style/propensity; ≈inert as a win-determinant; lean 0 = all hooks no-op |
| **initiative** | derived | from `seizure` → `decay/cap/steal/gain-loss`; feeds `net_sigma` (init_edge) | pre-contact → every beat | signed Vor/Nach state, clamped ±1.5; damper (decay) + bound (cap) |
| **conc** | derived | `=3Focus+2Spirit`; drained by hits/loss/bout; feeds seizure & mental-fat protection | init → exchanges → between-turn | depleting resource |
| **stamina** | derived | `=3End+2Spirit`; drained by act_cost; feeds fatigue (tempo, handling, balance), OOB, collapse | init → exchanges → between-turn | depleting resource; ≤−4 ends engagement |
| **poise (kuzushi)** | derived | `=1.0` default; broken by overcommit/bind/hit; feeds `poise_factor` (tempo, balance, defence) | beat loop | clamped [0.5,1]; recovers each beat (Focus-sped) |
| **Combatant.pool** | derived | `max(5,History+6)` set at init — **never read** (resolver recomputes from History at the roll) | — | **DEAD** (computed-unread); see §5 |
| **wt** | accumulator | per-End wound gate; `pool_penalty()` = the committed −1D/wound | every apply_wound + both rolls | discrete accumulator; the only thing the −1D wiring reads |
| **Recall / Bonds / Charisma** | base | **0 combat touchpoints** (Recall caps History in canon; Composure=Cha×3 — all non-combat) | — | not referenced anywhere in the engine |

---

## §3 · STATE-GRAPH NODES — mechanics & attributes each calls

| Node | Phase | Mechanics invoked | Attributes / derived read | Resources changed | Exits |
|---|---|---|---|---|---|
| **fight() turn loop** | harness | first-mover flip · between-turn recovery · UPSET_FLOOR | (all via engagement); recovery: End/Spirit/Focus | stamina↑, conc↑ | felled→result; max_bouts→draw |
| **Engagement init** | pre-contact | reach_base · initiative_seize (seizure_score) | reach(weapon), reading(Cog/Att/History), conc(Focus/Spirit) | sets initiative, poise=1, ready=0 | →beat loop |
| **Beat-loop top (dampers)** | per-beat | init_hold_decay · disp drift · clamp_initiative · poise recovery · weapon/close_tempo | Disp, Focus(poise), Agi(tempo), stamina(fat), poise | initiative↓, poise↑, ready↑ | →reopen / approach / closed |
| **Reach re-opening** | transition | reopen_prob | reading, balance(Agi/Str), reach gap, armor | closed→False | →approach |
| **APPROACH** | approach | approach_displace · close_rate · stop-hit | leverage, balance(Agi/Str), reading, reach | measure_gap↓ | just_closed→closed; stamina≤−4→draw |
| **Stop-hit roll (ROLL#1)** | approach | resolution_pool−**pool_penalty** · effective_ob · roll_net · degree · strike | **History**, **wt(wounds)**, Str(dmg), weapon(head/gap/perc), armor | wound, conc↓ | felled→return |
| **Closed setup** | closed | ACT_THRESHOLD gate · aggressor select · halfsword_target · commit(disp) · act_cost · OOB | ready, Disp, weapon(wt), stamina | stamina↓; weapon may switch | →read/defence |
| **Read & defence build** | closed | mental_fat · reach_sigma · init(tempo) · consistency · feint_eval · visual read · mode_sigma · dsig · atk_sig · adef · init_edge · net_sigma | Cog/Att(reading), Agi(init/reflex), History(init/tech), Focus(consistency/conc), Str(wind/handling), balance, conc, poise, weapon(GATE/guards/head), armor, tradition channels, familiarity | feint costs beats/stamina | →indes/counter |
| **Indes steal & counter-select** | closed (pre-roll) | indes_scale · init_steal_factor · counter selection | reading(Cog/Att), commit, Disp, tradition tempo/tactile/leverage, ability | initiative shifts | →main roll |
| **Main roll (ROLL#2)** | closed | resolution_pool−**pool_penalty** · effective_ob · roll_net · degree | **History**, **wt(wounds)**, net_sigma | (degree) | →outcome |
| **Overcommit** | closed | anti_overcommit · init_overcommit_loss | balance(Agi/Str), commit, tradition tempo, ability | initiative↓, poise↓ | |
| **Outcome map** | closed | neutralize · riposte (fail/neutralize) · graze/bind by mode | mode, commit, weapon | sets hit/riposte/bind | →counter/hit/bind/riposte |
| **Counter resolve** | closed | counter success | History, reflex(Agi/Att), ability | hit/riposte/initiative | |
| **Displace-step-inside** | closed | leverage compare · DISPLACE_P | leverage(weapon), commit, read_win | close, graze, riposte | |
| **Reopen-moment flags** | closed | (state flags) | longer/shorter, commit, weapon hands | reopen_moment / push_avail | |
| **Hit application** | closed | strike · apply_wound · init gain/loss · poise break | Str(dmg), weapon, armor, **wt**, hit magnitude | wound, conc↓, init±, poise↓ | felled→return |
| **Bind sub-loop (≤3)** | closed | bind_sigma · kuzushi · bind hits (BIND_HIT_P) · strike | History(tech), leverage, blade_guard, reading(tactile), Str, tradition leverage/tactile | init steal, poise↓, wound | felled→return |
| **Riposte / role-flip** | closed | disruption-resistance · conc drain · role flip | Focus, conc | conc↓, aggressor↔defender | →continue burst |
| **Burst exit** | closed | stamina collapse / BURST_MAX / clean-defence | stamina, exchanges, hit/riposte/bind | | →separate (draw) |
| **Between-turn recovery** | harness | stamina recovery · conc recovery | End/Spirit (stamina max), Focus/Spirit (conc max) | stamina↑, conc↑ | →next turn |

---

## §4 · WEAPONS / EQUIPMENT — interface with everything above

**Roster (13):** rapier · arming · longsword · greatsword · sabre · dagger · paired_short · spear · staff · mace · poleaxe · longsword_halfsword (auto-form). Each carries an axis-vector (`combatant.WEAPONS`) + a geometry vector (`combatant.GEOMETRY`, baked at import).

| Equipment property | Range / values | Consumed by (mechanic) | Interacts with attributes | Node |
|---|---|---|---|---|
| **reach** | long / short | `reach_base` (+LONG) | — | init (who's longer) |
| **wt** | light / heavy | damage `HEFT` · weapon_tempo `WEIGHT_PEN` · act_cost `ACT_WEIGHT` · str_demand `D_WT` | Str (demand), damage | tempo, hit, cost |
| **hands** | 1 / 2 | reach_base `HANDS2` · weapon_tempo `HANDS_COMMIT` · leverage `LEVER_2H` · str_demand `D_2H` · freed-hand shove | Str | tempo, bind, reopen |
| **head** | point / cut_thrust / straight_cut / curved_cut / blunt | coupling/damage (mode) · armor_defeat_sigma (cap) · legibility (thrust hard / swing easy) · reach_base `HEAD_REACH` · displace (point only) · half-sword | Str (damage) | hit, read, adef, displace |
| **spd** | −0.5 … 3.0 | weapon_tempo `SPEED_K` | — | tempo |
| **hand** (handling) | Forgiving/Standard/Demanding → HANDLE_RANK 0/1/2 | str_demand `D_HAND` | Str | handling penalty |
| **gap** (geometry-baked) | 0–1 | damage coupling (point transmit) · armor_defeat_sigma (point cap) | — | hit, adef |
| **head_len, grip_len** | relative | `leverage = LEVER_K·(grip/(grip+head) − REF)` | — | bind, displace, reopen |
| **hand_guard** | 0–0.9 | mode_sigma **parry** (`PARRY_GUARD_K·(hg−neutral)`) | — | dsig (parry) |
| **blade_guard** | 0–0.85 | mode_sigma **wind** (`WIND_GUARD_K`) · bind_sigma **catch** (`BIND_GUARD_K`) | — | dsig (wind), bind |
| **reach_adj** | −0.9 … +1.4 | reach_base (additive) | — | init |
| **percussion** | 0–8 | damage coupling (blunt `·perc/8`) · armor_defeat_sigma (blunt cap `·perc/8`) | — | hit, adef |
| **closes_poorly** | flag (spear/staff) | close_tempo `POLE_CLOSE_PENALTY` (unless choke grip) | — | closed tempo |
| **base** | half-sword link | `halfsword_target` form mapping | — | weapon switch |
| **geo.{thrust,cut,perc_conc,halfsword}** | baked 0–1 | **gap is live**; thrust/cut/perc_conc/halfsword are baked but mostly **not yet consumed** beyond gap | — | (partial — see §5) |
| **clinch** | int per weapon | **not read by the live engine** (data field, unwired) | — | — (see §5) |
| **Armor** | none / light / medium / heavy | damage `RESIST` (mitigation by mode) · armor_defeat_sigma (`ADEF_W`, `ADEF_THRESHOLD`) · reach_sigma (`REACH_W` — reach value falls with armour) · legibility (cut_thrust thrusts vs plate) · half-sword trigger (medium/heavy) · reopen_prob (`REACH_W[shorter.armor]`) | — | hit, adef, reach, read, switch |
| **Tradition** (8) | german/italian/spanish/japanese/chinese/filipino/english/none | `channel_weight` on 7 channels — **live:** visual (read), tactile (bind), precommit (seizure), leverage (bind, steal), tempo (init, counter, feint, overcommit-loss, open steal), measure (reach_sigma, init_hold_decay), balance (reach_sigma foot) · `familiarity` (read degradation) | — (multiplies attribute-derived channels) | read, bind, seizure, init, reach |
| **Skills** (per-axis) | dict, default 0 | mode_sigma (parry/dodge/bind) · balance_eff (`balance`) · bind_sigma (`bind`) · feint (`technique`) | adds to the relevant attribute term | dsig, balance, bind, feint |
| **Equipped abilities** | list, default [] | **live levers:** seize(+), counter_success(+), counter_select(×), anti_overcommit(+) · **channel levers** (misura, atajo, Stärke-Schwäche, …) **registered but INERT** (pending `eff_cw` routing) | — | seize/counter/overcommit (live) |
| **Grip** | normal / choke / lunge | weapon_tempo (`CHOKE/LUNGE_TEMPO_PEN`) · legibility (lunge) · close_tempo (choke offsets closes_poorly) | — | tempo, read |

---

## §5 · Wiring status & flags (what is live, partial, dead)

- **−1D/wound — LIVE (committed `deb405b9`).** Both roll sites subtract `wt.pool_penalty()`. Penalty = `−1 × wounds`; operationally capped at −3D because a fighter is felled at the 4th wound (MW cap 3, PP-717). Canon: `derived_stats_v30 §4.1`, `§14.4`.
- **Defender-side wounds — OPEN (not implemented).** The penalty is literal canon ("−1D to the rolled Pool"), so it lands on whoever attacks. The engine's defence is a derived `dsig`, not a rolled pool, so a wounded *defender* is not directly penalised. Whether to mirror the penalty onto defence is a Jordan decision (extrapolation beyond the text).
- **`Combatant.pool` — DEAD.** `max(5,History+6)` is set at init and never read; the resolver recomputes from `History` at each roll. Remove or repurpose.
- **`clinch` weapon field — UNWIRED.** Present on every weapon, read by nothing in the live engine. Either wire (a clinch/grapple state) or prune (same class as the dead pool).
- **Baked geometry — PARTIAL.** `geometry.bake` produces `{gap, thrust, cut, perc_conc, halfsword}`; only **gap** is consumed downstream. `thrust/cut/perc_conc/halfsword` are computed but not yet read.
- **Tradition channel abilities — INERT.** `misura`, `atajo`, `Stärke-Schwäche` (and the other channel-lever abilities) are registered but have no effect until call sites route through `eff_cw` (`tradition.py` notes ~21 pending sites). The four *non-channel* ability levers (seize, counter_success, counter_select, anti_overcommit) **are** live.
- **Grip levers — DORMANT.** The tempo/legibility penalties for `choke`/`lunge` are wired, but the wrapper sets grip to `normal` and never mutates it (only the half-sword *weapon* form auto-switches). Grip effects fire only if a build pre-sets a non-normal grip.
- **Concurrent `config.py` edit.** A parallel session changed `config.py` this session (effect: lifts spirit/strength/end ≈ +3 per point in the per-point tier). The constants in §6 are the *current* synced values.

---

## §6 · Exact constants (appendix — load-bearing literals, read this session)

**Resolution:** `TN_STANDARD = 7` · `DECISIVE_OB = 3` · `POOL_FLOOR = 5` · `BASE_POOL = 6` · overwhelming `net ≥ 2·Ob ∧ ≥ 3`.
**Wounds:** `WOUND_INTERVAL_BASE = 6` (wi = End+6) · `MAXWOUNDS_CAP = 3` (PP-717) · `MW = min(⌊End/2⌋+1, 3)` · `health = (End+6)(MW+1)` · `WOUND_POOL_PENALTY = 1`.
**Stamina/conc:** `stamina_max = 3·End + 2·Spirit` · `STAMINA_REF = 18` · `RECOVERY_FRAC = 0.5` · `conc_max = 3·Focus + 2·Spirit` (`CONC_FOCUS=3, CONC_SPIRIT=2`).
**Damage:** `HEFT{light:4, heavy:6}` · `QUAL{partial .6, graze .35, success 1.0, overwhelming 1.5}` · `DAMAGE_SCALE = 4.0` · `CAP_END = 4` · `DELIVERY{blunt 1.6, point 1.45, cut 1.35}`.
**Reading/reflex/init:** `reading = (2Cog+Att)/3 + 0.2(History−3)` · `reflex = (2Agi+Att)/3` · `INIT_K = 0.045` · `INIT_READING_K = 0.03` · `INIT_HISTORY_K = 0.02` · `AGI_TEMPO_K = 0.03` · `READ_HISTORY_K = 0.2`.
**Tempo/economy:** `BASE_TEMPO = 2.0` · `ACT_THRESHOLD = 2.5` · `BURST_MAX = 4` · `OOB = 2`.
**Initiative:** `INIT_SIGMA_K = 0.16` · `INIT_SCALE = 1.2` · `INIT_SEIZE_K = 0.45` · `INIT_DECAY = 0.75` · `INIT_CAP = 1.5` · `INIT_GAIN_HIT = 0.18` · `INIT_LOSS_WOUNDED = 0.28` · `INIT_STEAL_INDES = 0.36`.
**Defence:** `PARRY/DODGE/WIND_K = 0.9` · `NEUTRALIZE` parry .55 / dodge .62 / wind .50 · `OVERWHELM_DROP = 0.45` · `READ_K = 0.5`.
**Focus levers:** `FOCUS_CONSISTENCY_K = 0.10` · `FOCUS_MENTAL_K = 0.5` · `DISRUPT_K = 0.7` · `POISE_FOCUS_K = 0.10`.
**Disposition:** `DISP_COMMIT_K = 0.8` · `DISP_COUNTER_K = 0.5` · `DISP_INIT_K = 0.10`.
**Bind:** `BIND_TECH_K = 0.06` · `BIND_TACTILE_K = 0.04` · `BIND_STR_K = 0.0156` · `BIND_GUARD_K = 0.55`.
**Global:** `ATTACKER_BIAS = 0.12` · `UPSET_FLOOR = 0.05` · `FAMILIARITY` 1.0 / .93 adjacent / .85 default.
