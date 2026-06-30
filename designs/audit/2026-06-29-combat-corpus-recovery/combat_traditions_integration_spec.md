# Combat Traditions — Schema Integration Spec (force-relation + targeting axes)
**2026-06-25 · companion to `combat_traditions_morphology_critique.md` · target: `designs/scene/combat_engine_v1/` @ canonical HEAD · status: PROPOSED, mechanical-tier, Jordan-vetoable**

`[SELF-AUTHORED — bias risk: extends an engine prior Claude sessions built, and revises a claim my own §-critique made (see §0 correction). The integration is deliberately small-surface — most of the morphology's missing axes map onto seams that already exist; the genuinely-new code is isolated and flagged so it can be rejected without unwinding the rest.]`

**Grounding trail (all engine files read first-hand at HEAD, with line numbers):**
`[READ: wrapper.py — full, 297 lines]` (the `engagement()` state machine: beat loop, mode selection, outcome branch, hit/bind/riposte, the four ability call-sites) · `[READ: systems.py — full, 291 lines]` (the pure contribution funcs: `mode_sigma`, `bind_sigma`, `reach_sigma`, the initiative-differentiation layer) · `[READ: tradition.py — full, 136 lines]` (`ABILITIES`, `ability_bonus`/`ability_factor`/`eff_cw`, the lever model) · `[READ: core.py — full, 87 lines]` (`strike`/`damage`/`resolve`) · `[READ: config.py — full, 97 lines]` (`CFG`; 150 keys; new-constant collision-checked = none).

---

## §0 — One correction to the critique, found by reading `systems.py`

The morphology critique (its §2, §7) repeated the armature's note that `staerke_schwaeche`, `misura`, `atajo` are *"registered but inert, pending the `eff_cw` channel-wiring pass (~21 sites),"* and logged `[GAP: systems.py not read]` over exactly that claim. Reading `systems.py` resolves the gap and **corrects it**:

- `systems.py` commit **`40b58b04` (2026-06-13)** = `[fix] eff_cw channel-lever wiring (F2) + precommit`. The channel-wiring pass **landed**. `eff_cw` is now called live at the channel sites: `reach_sigma` (measure + balance, lines 171–173), `bind_sigma` (leverage + tactile, 234–237), the visual-read assembly (wrapper 131–132), `feint_eval` (202–203), `init_steal_factor`/`init_hold_decay`/`init_overcommit_loss` (systems 263–279).
- Therefore the **three "pending" channel abilities are LIVE**, not inert — `staerke_schwaeche` (`leverage`) bites in `bind_sigma`; `misura`/`atajo` (`measure`) bite in `reach_sigma` and the initiative hold. The engine carries **eight live abilities**, not five. `tradition.py`'s docstring (last touched 06-03) still says "INERT… the next pass" — that text is now stale; the ABILITIES `desc` strings still read "(channel; pending)". **`[MODIFY @ tradition.py:88–91 docstring + ABILITIES desc strings]` — strike the "pending/inert" language; the pass is done.** (Factual-specifics correction, canon-grounded per the authority rules — applies to my own prior output too.)

The operational consequence for this spec is positive: **`eff_cw` is the proven extension path.** The 06-13 wiring is the template the channel-style levers below reuse — the integration is not inventing a mechanism, it is repeating one the engine already validated.

---

## §1 — The schema being integrated into (so the markers are legible)

**The ability schema** (`tradition.py`): an ability is `dict(tradition, grade, lever, op, value, desc)`. A fighter equips ability *keys* (`c.equipped`, default empty → no-op). The engine reads equipped abilities three ways:
- `ability_bonus(c, lever)` → Σ of `op='+'` values (default **0.0**).
- `ability_factor(c, lever)` → Π of `op='*'` values (default **1.0**).
- `eff_cw(c, channel)` = `channel_weight(c.tradition, channel) × ability_factor(c, channel)` → the substrate-weight path (now wired).

**The state graph** (`wrapper.py::engagement`): a per-beat loop. Phases, with the lines that own them:
| Phase | Lines | Key seams |
|---|---|---|
| per-beat recompute (decay/drift/poise/tempo) | 39–52 | `init_hold_decay`, `poise`, `weapon_tempo` |
| reach re-opening | 58–64 | `reopen_prob` |
| **APPROACH** (stop-hits while closing) | 66–85 | `approach_displace`, stop-hit `apply_wound` (81) |
| **CLOSED — aggressor select / commit** | 87–106 | tempo gate (87–93), commit depth (98–106) |
| **read → mode select** | 124–136 | `read_win` (133), `mode=max(msig)` (136) |
| sigma assembly → **net_sigma** | 139–143 | `atk_sig` (140), `net_sigma` (143) |
| **INDES steal / counter-select** | 144–158 | `steal` (151), `counter_select` ability site (158) |
| **resolution roll** | 159–160 | `core.resolve` |
| anti-overcommit | 162–167 | `anti_overcommit` ability site (163) |
| **OUTCOME branch** (hit/riposte/bind) | 168–185 | the `deg × mode` dispatch |
| counter-success | 186–198 | `counter_success` ability site (189) |
| **hit application** | 226–232 | `apply_wound` (227), init shift (229–230), poise-break (231) |
| **BIND loop** (3 iterations) | 233–252 | `bind_sigma`, bind-hit `apply_wound` (249) |
| riposte / role-flip | 253–261 | |

**The design rule every insertion obeys** (armature §1): *modulate, never unlock*; *no-op when unequipped* (invariant-safe); *bottom-up technique + top-down precedent or it isn't earned*; *bounded Class-C values*.

**Integration strategy.** Two new lever *families* (force-relation, targeting), each reusing `ability_bonus`/`ability_factor` — **no new op type, no new read-machinery**. The only genuinely-new code is one pure dispatcher (`hit_effects`) and one new state quantity (the choke clock). Everything else is a scalar lever read at an existing line. This keeps NERS-E: the engine does not grow a subsystem, it grows cells in the grid it already has.

---

## §2 — I1 · Force-relation (morphology D5, F1–F6) integration

D5 is the most efficacy-faithful axis the model omits (Vol III §2). Mapping each value to the engine:

| F-value | Status in engine | Lever (new unless noted) | op | Engine site → marker | Bottom-up seam | Top-down precedent |
|---|---|---|---|---|---|---|
| **F1 opposition** | **present** | `leverage` (+ `staerke_schwaeche`) | `*` | `bind_sigma` 234 — no change | the bind | Liechtenauer Stärke |
| **F2 deflection** | **present** | parry/wind mode + `leverage` | — | `mode_sigma` 95–104 — no change | parry/wind | geometric parry |
| **F3 yielding** | absent | `absorb` | `*` (<1) | **`[MODIFY @ wrapper.py:227,231]`** | hit + poise-break block | judo *ukemi* / Taiji *song* — **Vol III caveat: skill-gated, modest value** |
| **F4 blending** | partial (reuses steal) | `redirect` | `+` | **`[MODIFY @ wrapper.py:151]`** | the INDES steal | aiki redirection — **Vol III caveat: fails cooperatively-trained; gate on the read-margin the site already has** |
| **F5 evasion** | mode exists, not a *lean* | `evade` | `*` | **`[MODIFY @ systems.py:101]`** + **`[MODIFY @ wrapper.py:135–136]`** | the `dodge` mode | fencing slip / boxing head-movement |
| **F6 smothering** | absent | `smother` | `*` (<1) | **`[INSERT @ wrapper.py:140]`** (atk_sig) | closed tempo/commit | wrestling clinch / Muay Thai plum |

**Precise insertions:**

`[MODIFY @ wrapper.py:227]` hit application — wrap the damage the defender takes in the absorb factor:
```python
# was:  defender.apply_wound(hit); defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_HIT'])
hit_eff = max(0, int(round(hit * TR.ability_factor(defender,'absorb'))))   # F3 yielding: bleed the blow (1.0 if unequipped)
defender.apply_wound(hit_eff); defender.conc=max(0,defender.conc-cfg['CONC_DRAIN_HIT'])
```
`[MODIFY @ wrapper.py:231]` same block — soften the poise-break for a yielding defender (`* TR.ability_factor(defender,'absorb')` on `POISE_BREAK_HIT`). *Default `absorb`=1.0 ⇒ both lines unchanged for a no-ability fighter.*

`[MODIFY @ wrapper.py:151]` INDES steal — F4 redirect adds to the steal a defender earns by reading a committed aggressor:
```python
steal = cfg['INIT_STEAL_INDES']*S.init_steal_factor(defender, mode=='wind', TR)*indes_scale \
        * (1 + cfg['REDIRECT_STEAL_K']*TR.ability_bonus(defender,'redirect'))   # F4 blend, gated by indes_scale (read-margin)
```
Because `indes_scale` already encodes the read-margin (`read_d-read_a`, line 150), F4's "fails when uncontested" caveat is structural: a redirect only pays out proportional to how cleanly the defender out-read the attack.

`[MODIFY @ systems.py:101]` `mode_sigma` dodge branch — F5 promotes evasion from a fallback mode to a competence:
```python
sig=cfg['DODGE_K']*(0.30*(rfx-3)+0.70*(ftw-3))/3 + defender.skill('dodge')
sig*=TR.ability_factor(defender,'evade')     # F5 evasion lean (1.0 if unequipped)
```
Optionally bias *selection* too at `[MODIFY @ wrapper.py:135–136]` (raise dodge's weight in the `max(msig)`/random pick). *Default 1.0 ⇒ unchanged.*

`[INSERT @ wrapper.py:140]` atk_sig — F6 smother denies the aggressor's commit-window when a smotherer defends in the clinch:
```python
smother = (cfg['SMOTHER_COMMIT_K']*TR.ability_factor(defender,'smother')) if (closed) else 0.0   # 0 if unequipped (factor 1.0 → K*(1-1)=0… see note)
atk_sig = cfg['COMMIT_SIGMA']*(commit-3) + init - oob*0.5 - S.handling_penalty(aggressor,fat_a,cfg) + consistency_a - smother
```
*Implementation note:* express smother as `SMOTHER_COMMIT_K*(TR.ability_factor(defender,'smother')-1.0)` so an unequipped defender (factor 1.0) contributes exactly 0 — preserving the invariant — and an equipped smotherer (factor >1) subtracts from the aggressor's commit edge. Pairs with I2's choke (T4): smother creates the clinch, choke finishes it.

**No change for F1/F2** — the engine already expresses opposition/deflection through `leverage`+`staerke_schwaeche`+parry/wind. The critique credited this; the integration keeps it.

---

## §3 · I2 · Targeting logic (morphology D7, T1–T7) integration

Today a landed hit is generic: `core.strike` → damage → `apply_wound`, with poise/conc/init shifts (wrapper 226–232; bind-hit 247–249; stop-hit 79–81). Targeting biases the hit's **consequence type**, not its probability. Cleanest integration = one new **pure** dispatcher in `systems.py` (honouring the "wrapper owns mutation, systems are pure" contract), called at the three `apply_wound` sites.

`[ADD @ systems.py — new pure function]`:
```python
def hit_effects(attacker, defender, hit, cfg, TR):
    """Targeting dispatch (morphology D7). Returns the consequence bundle for a landed hit, biased by the
    ATTACKER's equipped targeting ability. All-default (no targeting ability) reproduces the current generic
    hit exactly (invariant-safe). Pure — wrapper applies the mutations."""
    f = lambda lev: TR.ability_factor(attacker, lev)      # 1.0 default
    b = lambda lev: TR.ability_bonus(attacker, lev)       # 0.0 default
    dmg        = max(0, int(round(hit * min(cfg['TARGET_VITAL_QUAL_CAP'], f('target_vital')))))  # T3 [M]-kernel only, capped
    poise_mult = f('target_poise') * (1 + cfg['TARGET_UPROOT_K']*b('target_uproot'))             # T1 mass / T5 base
    conc_extra = cfg['TARGET_PSYCH_CONC_K']*b('target_psych')                                    # T7 psychological
    hamper     = cfg['HAMPER_HANDLE_K']*b('target_hamper')                                       # T2 joints
    defang     = cfg['DEFANG_REACH_K']*b('target_defang')                                        # T6 weapon/limb-first
    choke      = b('target_choke') > 0                                                           # T4 (clinch-only; see below)
    return dict(dmg=dmg, poise_mult=poise_mult, conc_extra=conc_extra,
                hamper=hamper, defang=defang, choke=choke)
```

`[MODIFY @ wrapper.py:226–231]` route the hit through the dispatcher:
```python
if hit>0:
    fx = S.hit_effects(aggressor, defender, hit, cfg, TR)
    defender.apply_wound(int(round(fx['dmg']*TR.ability_factor(defender,'absorb'))))   # I1-F3 absorb still composes
    defender.conc=max(0, defender.conc - cfg['CONC_DRAIN_HIT'] - fx['conc_extra'])      # T7
    defender.hampered = max(getattr(defender,'hampered',0.0), fx['hamper'])             # T2 (decays each beat)
    defender.limb_dmg = max(getattr(defender,'limb_dmg',0.0), fx['defang'])             # T6 (reach/handling debuff)
    aggressor.initiative=S.clamp_initiative(aggressor.initiative+cfg['INIT_GAIN_HIT'], cfg)
    defender.initiative=S.clamp_initiative(defender.initiative-cfg['INIT_LOSS_WOUNDED'], cfg)
    defender.poise=S.clamp_poise(defender.poise - cfg['POISE_BREAK_HIT']*fx['poise_mult']*min(1.0,hit/cfg['POISE_SOLID_HIT']), cfg)  # T1/T5
    if defender.felled: return defender
```

| T-value | Consequence routed to | Lever | op | Marker | Top-down |
|---|---|---|---|---|---|
| **T1 gross-mass** | poise-break ×  | `target_poise` | `*` | hit_effects → wrapper 231 | hammer-blow staggering |
| **T2 joints** | handling/balance debuff (new `hampered`, decays) | `target_hamper` | `+` | `[MODIFY @ systems.py:60 handling_penalty]` to add `c.hampered` | joint manipulation |
| **T3 vital (kernel)** | damage × (capped) | `target_vital` | `*` | hit_effects | chin/liver/throat — **NO death-touch, NO hour-timing (Vol III F6)** |
| **T4 choke** | **clinch incapacitation clock (NEW state)** | `target_choke` | `+` | **`[INSERT @ wrapper.py:243–252 bind loop]`** | the convergent-core choke |
| **T5 balance-base** | poise-break + init swing | `target_uproot` | `+` | hit_effects → wrapper 230–231 | wrestling/judo uproot |
| **T6 defang** | reach/handling debuff *before* body (new `limb_dmg`) | `target_defang` | `+` | `[MODIFY @ systems.py:reach_base/handling]` to read `c.limb_dmg` | FMA defang (**attribution flagged — I4**) |
| **T7 psychological** | concentration drain × | `target_psych` | `+` | hit_effects → wrapper 227 | *seme* / freezing feint |

**The one genuinely-new state mechanic — T4 choke** `[INSERT @ wrapper.py:243–252]` inside the bind loop:
```python
for _ in range(3):
    beats+=1
    bsig = S.bind_sigma(aggressor, defender, cfg, TR)
    if rng.random() < 1/(1+exp(-bsig)):
        if TR.ability_bonus(aggressor,'target_choke')>0 and closed:        # clinch-only incapacitation path
            defender.choke_clock = getattr(defender,'choke_clock',0.0) + cfg['CHOKE_CLOCK_RATE']
            if defender.choke_clock >= cfg['CHOKE_CLOCK_THRESHOLD']:
                return defender                                            # felled by incapacitation, NOT a wound
        if rng.random()<cfg['BIND_HIT_P']:
            ... (existing strike path unchanged)
    else: riposte=True; break
```
This is the morphology's convergent unarmed core (Vol III §1/§6.3) and the natural payoff for I1-F6 smother: the choke ends a fight without producing a "wound," which is exactly right — it is an incapacitation exit, distinct from the wound-felling path. **It is the single piece of this spec that adds genuinely new state**, so it is the single most rejectable piece: cut it and the rest stands.

---

## §4 · Consolidated schema additions

**`[ADD @ ability_armature.md §2c lever map]`** — new rows (op + wiring status):

| Lever | Family | Op | Site | Status |
|---|---|---|---|---|
| `absorb` | force-relation (F3) | `*` | wrapper 227,231 | new — scalar (no wiring pass needed) |
| `redirect` | force-relation (F4) | `+` | wrapper 151 | new — composes with INDES steal |
| `evade` | force-relation (F5) | `*` | systems 101 | new — over existing dodge mode |
| `smother` | force-relation (F6) | `*` | wrapper 140 | new — needs the clinch (closed) |
| `target_poise`/`target_uproot` | targeting (T1/T5) | `*`/`+` | hit_effects | new — over existing poise-break |
| `target_psych` | targeting (T7) | `+` | hit_effects | new — over existing conc drain |
| `target_hamper`/`target_defang` | targeting (T2/T6) | `+` | handling/reach | new — two new decaying debuff states |
| `target_vital` | targeting (T3 kernel) | `*` | hit_effects | new — **capped; [M]-kernel only** |
| `target_choke` | targeting (T4) | `+` | bind loop | new — **the one new state mechanic** |

**`[ADD @ config.py CFG]`** (Class-C seeds; collision-checked vs the 150 live keys = none): `ABSORB_FLOOR`, `REDIRECT_STEAL_K`, `SMOTHER_COMMIT_K`, `CHOKE_CLOCK_RATE`, `CHOKE_CLOCK_THRESHOLD`, `HAMPER_HANDLE_K`, `HAMPER_DECAY`, `DEFANG_REACH_K`, `TARGET_VITAL_QUAL_CAP`, `TARGET_PSYCH_CONC_K`, `TARGET_UPROOT_K`. Slot near the matching existing block (the targeting keys beside `POISE_BREAK_*`/`CONC_DRAIN_*`; the force-relation keys beside `INIT_STEAL_INDES`/`NEUTRALIZE_*`). All values provisional — calibrate per §5.

**`[ADD @ wrapper.py:_init_live (9–14) + fight reset (278–279)]` and `[ADD @ combatant.py Combatant fields]`** — three new per-fighter states init to neutral: `choke_clock=0.0`, `hampered=0.0`, `limb_dmg=0.0`; and a per-beat decay `[INSERT @ wrapper.py:47–49 recompute block]` (`hampered *= cfg['HAMPER_DECAY']`, `limb_dmg *= cfg['HAMPER_DECAY']`). `[GAP: combatant.py not read in full — the exact field-declaration + `.skill()`/`.equipped` surface is inferred from its use throughout wrapper/systems; confirm the field sites before patch.]`

**`[ADD @ tradition.py ABILITIES]` — example grounded abilities, well-anchored core only.** Per the selection-effect discipline, levers are populated only where the corpus anchors them; the rest stay registered-but-empty (exactly how the engine treats priority-gap traditions today):
- `ringen_smother` — **german, S2**, `lever='smother'`, op `*`, value ~1.25. Bottom-up: *Ringen am Schwert* (grappling at the sword; Ott's wrestling in the Liechtenauer corpus). Top-down: the clinch.
- `target_uproot` example — **german/italian, S2**, off the documented *Mortschlag*/throw-from-the-bind. Bottom-up: the bind-to-throw plays. Top-down: wrestling uproot.
- F4 `redirect`, T6 `target_defang`: **levers added, abilities deferred.** Aiki-style redirection is post-period and koryū-adjacent (anchoring-thin); FMA/defang is the under-anchored tradition the armature already flags. The mechanism is sound; the *attribution* waits for an S1/S2 anchor — surfacing the gap, not inventing the ability. (This is the armature's own rule, applied.)

**Doc-level modifications (not state-graph):**
- `[MODIFY @ tradition.py:88–91 + ABILITIES desc]` — strike the stale "(channel; pending)/INERT" language (§0).
- **I4** `[MODIFY @ tradition.py TRADITIONS]` — the four-axis vetting the critique surfaced: the `chinese` mode↔profile mismatch and the `filipino`/`chinese` two-file anchoring tension. **Direction of fix is Jordan's** (`mode` is flavour); the finding is recorded.
- **I5** `[ADD @ ability_armature.md]` — one paragraph naming the aliveness/D14 position as a sourcing constraint.
- **I3 (power-source, DEFERRED)** — if ever wanted, the insertion point is `core.strike`/`core.damage` (a strike-*profile* bias on the `heft`/cadence split), **not** a new attribute. The critique recommends deferring (Vol III F9 over-engineering risk); shown here only to complete the map.

---

## §5 · Invariant-safety (the gate — armature §1.3, mandatory)

Every lever above defaults to a no-op: `ability_factor`=1.0, `ability_bonus`=0.0, the three new states init 0.0 and only move when the matching ability is equipped *and* (for smother/choke) the clinch holds. The smother term uses `(factor-1.0)` so an unequipped defender contributes exactly 0. **Therefore a no-ability fighter — and the mirror match — produces byte-identical resolution to current HEAD**, and the existing invariant suite must pass unchanged. The per-item workflow before any commit (armature §6): ground → define → wire → **invariant-check (no-ability suite byte-identical)** → calibrate `value` vs the matchup harness (respect the tanh/cap safeguards) → log → commit. `[GAP: no sims run — values are seeds; each lever needs the invariant pass + calibration before it lands.]`

---

## §6 · Layer boundary (unchanged from the critique)

Mechanical-tier here = the lever vocabulary, the wiring, the grounding discipline. **Jordan's creative/metaphysical layer, untouched:** the roster; which tradition *gets* which force-relation/targeting ability (a roster + flavour + anchoring call, not Claude's — I supply the machinery and the bottom-up/top-down gate, never the assignment); each tradition's `mode`/analogue *choice* (I4 surfaces `chinese`'s inconsistency; the resolution direction is Jordan's); and the entire `[B]/[L]` metaphysical layer. **The one carried-over flagged decision still stands** (critique §6): when a Valoria tradition invokes "internal power," does it resolve to (a) inert flavour, (b) the engine's `[M]` channels, or (c) the actual Thread/Coherence metaphysics? Canon-structure ruling — Jordan's. Flagged, not decided.

---

## §7 · Honesty block

- `[CONFIDENCE: high]` on the insertion *points* and the existing-item *modifications* — every marker is anchored to a line read first-hand at HEAD across all five engine files, and the new-constant names are collision-checked against the live `CFG`. `[CONFIDENCE: medium]` on the seed *values* (Class-C, uncalibrated) and on the cleanest *form* of two choices: (i) scalar levers vs a single categorical `target` lever — I chose scalars to avoid adding a third `op` type, but categorical is more elegant if a tradition picks exactly one targeting logic; **`[OPEN TRADE-OFF — Jordan/design]`**; (ii) whether F4/F5 are distinct levers or biases over the existing steal/dodge — I made them thin levers that compose with the existing machinery.
- `[CORRECTION: §0 — the "channel abilities pending/inert" claim in the critique (§2,§7) is superseded; `eff_cw` wiring landed 2026-06-13 (`40b58b04`); eight abilities live, not five.]` Self-authored revision, canon-grounded.
- `[GAP: combatant.py not read in full — the new-state field declarations and the `.skill()`/`.equipped`/`.felled` surface are inferred from pervasive use in wrapper/systems; confirm before patch.]` · `[GAP: no sims run — proposal, not a validated change.]`
- **Project linkage:** this is the build-side of the J-33 / W4 #17 "traditions F2" item the critique decomposed; I1 (force-relation) is the piece that most directly retires it. The 06-13 commit message already tagged the eff_cw work "(F2)" — the project is mid-stream on exactly this gap.
- **Not committed.** Mechanical-tier, Jordan-vetoable. If wanted in-repo, home = `designs/audit/2026-06-25-combat-traditions-morphology/` (alongside the critique), landed via `safe_commit` with a `Citations:` block (`wrapper.py`, `systems.py`, `tradition.py`, `core.py`, `config.py`, the five morphology uploads). Say the word and I'll bootstrap a commit pass; not done unprompted.
