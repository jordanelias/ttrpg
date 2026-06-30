# Grounded Weapon · Armour · Use-Mode Model (2026-06-30)

**Status:** DESIGN — grounded, adversarially fact-checked; pre-implementation. Class-C (Jordan-vetoable). Executes
scene-combat **WS-2** (continuous weapon morphology + affordance gates) and **WS-8** (balancing methodology) of the
origin WS-0..WS-8 plan, via the `REARCHITECTURE_v1` L0-L5 layer (the Phase-3 re-baseline).

## Context

The Gate-1 architecture audit found percussion authority derived twice with divergent inputs (`core.p_auth` hand-set
`pob_frac` vs `weapon_physics.percussion_authority` derived `PoB_frac`). Consolidating it naively dropped the poleaxe —
the historical anti-plate weapon — below the mace. Jordan's directives turned the fix into a full grounded model:
(1) *derive* the energy-credit magnitude from physics + biomechanics, don't pick it; (2) model the poleaxe **dual-mode**
(hammer + beak); (3) ground the **armour-as-protection** RESIST table; (4) model **how a weapon is used** — thrust vs
swing is a per-exchange technique choice, applying to poleaxe, spear, staff. Each was grounded by an adversarially
fact-checked Workflow (fabrication + selection-effect control per CLAUDE.md §7).

The four results **converge**: the poleaxe is *not* a better pure percussor than a head-heavy mace (biomech), and it
shouldn't be — it defeats plate by **thrusting the spike / striking the beak** (puncture), which it *selects* vs harness
(use-mode), against a plate that is vulnerable to concentrated puncture at gaps and to authority-scaled concussion
(armour). The mechanism is grounded end-to-end.

---

## 1. Concussion energy-credit magnitude — biomechanics (task `wpwi3b9qf`)

**A_HANDS = 0.25 (band 0.24–0.28); B_ARC = 0.04/length-unit (band 0.02–0.06).**

- `A_HANDS` from the measured **2H/1H force ratio ≈ 1.25** (Oh et al. 2022, within-subject crossover, **S1**;
  corroborated IASTM compact-tool 1.24–1.28, **S1**). The credit sits on the **momentum/effective-mass** side because
  the record shows 2H raises effective mass, not tip speed (tennis 2H trunk contribution 2.2× at comparable endpoint
  speed; boxing force +46% / velocity +13%). So `1+A_HANDS = R_F = 1.25`.
- `B_ARC` small and saturating: a longer haft raises effective mass but loses ω as ~I^−0.28 (Nathan 2003, **S1**;
  constant-power regime), capped at the Cross–Nathan swing-weight optimum.

**Honest finding (robust across the whole band):** at the grounded magnitude, **mace 7.45 > poleaxe 5.83 > staff 2.50** —
the poleaxe's concussion lands *below* the mace. This is correct: `√mass·PoB_frac` gives the mace a 3.1× base advantage
(compact head-heavy block vs long balanced haft); closing it would need a ~3× credit, but biomechanics support ~1.37×.
**The poleaxe's plate primacy is NOT a percussion effect** — it is the beak/spike (puncture), §3. *(Secondary option
considered and rejected: rebase percussion on handle-axis MOI `M_e=I_A/R²` instead of `PoB_frac` — it is r-fragile and
inflates the staff; let the beak own the plate ranking, the historically-correct mechanism.)*

## 2. Armour-as-protection RESIST — materials science (task `wht7pkx1c`)

Resisted-fraction per material × mode; `transmit = 1 − resist`. **Only 4 cells change**, all evidence-anchored to
Alan Williams, *The Knight and the Blast Furnace* (2003):

| change | from → to | grounding (tier) |
|---|---|---|
| `cloth.shear` | 0.35 → **0.45** | 16–30 layer jack resists ~80–200 J vs a ~60–130 J cut (S1) |
| `cloth.puncture` | 0.15 → **0.12** | same jack stops only ~50 J behind a point — the cut≫point asymmetry (S2) |
| `cloth.percussion` | 0.10 → **0.12** | modest standalone blunt absorption (S2) |
| `mail.shear` | 0.80 → **0.85** | cutting riveted mail "functionally impossible," >130 J ceiling (S1) |

**KEEP:** the entire plate row (0.30/0.95/0.70) and mail percussion 0.20 / puncture 0.45. Qualitative truths preserved:
mail strong-vs-cut/weak-vs-blunt; plate near-immune-to-cut (0.95)/vulnerable-to-concussion (0.30, lowest); textile the
anti-blunt under-layer (cut 0.45 ≫ puncture 0.12).

**Two mandatory honesty flags:** (a) the cloth fractions (0.12/0.45/0.12) are a **designer normalisation of Williams'
joules onto the 0–1 scale — NOT Williams figures**; CI-flag designer-set/unsourced. (b) `plate.percussion 0.30` is honest
*only because* FIX-1b scales it by blow authority (steel hammer overwhelms; wood staff absorbed) — **the 0.30 and the
authority gate are one package, never tuned apart** (ungated, an honest value is ~0.55–0.65). Caveats: **riveted ≠ butted**
(butted ~10–15× weaker; the model assumes riveted), **hardened ≠ wrought** (the 0.95/0.70 plate row assumes ~2 mm hardened).

## 3 & 4. Use-mode model: weapons afford a SET of strike modes; the wielder SELECTS per exchange (tasks `wht7pkx1c`, `w4bekmb5e`)

The engine fixes one `head` per weapon, so the mode is weapon-fixed. But a weapon affords several modes the fighter
chooses each exchange (the technique). **The engine already does this for `cut_thrust`** (a 2-element set auto-selected
by `max()` vs armour) + `halfsword_target` (form-switch vs harness) + `legibility` (thrust hard-to-read / swing easy).
Generalize that one seam — no new resolution physics.

**Afforded mode sets (each mode = an existing head string + a geometry override; all S1 unless noted):**
- **POLEAXE** {`thrust_dague`(point/gap — *dominant* per Le Jeu), `swing_hammer`(blunt/concussion — attested *once*),
  `hook_bec`(point/puncture + hook/leverage), `strike_queue`(butt-spike, uses `butt_kg`), `demy_hache`(centre-haft
  leverage/bind, head=None)}. **Thrust-and-haft dominant** — `head='blunt'` is backwards.
- **SPEAR** {`thrust_point`(primary, "held short to deceive"), `haft_as_staff`(blunt/swing on a failed thrust),
  `butt_sauroter`(uses `butt_kg`)}.
- **STAFF** {`strike_blow`(blunt), `end_thrust`(point, low concentration ~0.3)} — Silver "no fight perfect without both
  blow and thrust."
- **LONGSWORD** {`cut`,`thrust`(both already in `cut_thrust`), `half_sword`(already `HALFSWORD_FORM`), **`mordhau`**(blunt
  pommel — *the one missing mode*)}.
- **SINGLE-MODE 1H** (mace=swing, rapier=thrust, sabre=cut, arming=cut+thrust, dagger=thrust-to-gap): keep scalar `head`,
  **zero behaviour change** — mode-set cardinality is itself a weapon property.

**Selection cascade `select_mode(weapon, armor, closed, bind, tradition, history)`:**
- **RULE 1 ARMOUR** (hard-deletes options): vs harness, delete cut/shear modes → survivors {thrust-to-gap, half-sword,
  spike, beak, percussion}; vs unarmoured, cut is the wounding default. *This is exactly the existing `coupling`/`adef_cap`
  `max()`, generalized from 2 modes to N.* (S1/S2)
- **RULE 2 RANGE** (hard-gates reachability): open→point modes; close→short-grip modes (half-sword, queue, butt, bec,
  demy-haft). *Mirrors `halfsword_target`/`grip_target`.* (S1)
- **RULE 3 TRADITION** (soft): German bind-then-thrust vs Italian/English/Spanish point-and-refuse — *already at node level
  via `impose_node`.* (S1)
- **RULE 4 READ/DECEPTION** (soft): thrust reads hard (LEGIB_THRUST 0.80), swing easy (1.25) — *the one real wiring change:
  feed `legibility` the SELECTED mode's head, not the fixed weapon head.* (S1)
- **RULE 5 LEARNED ACCESS** (gate): half-sword, mordhau, armoured bec/queue plays, naginata flourishes are TRAINED —
  *gate behind the existing History/ability check; untrained collapses to the intuitive mode.* (S3)

Greedy `max(coupling)` baseline reproduces `cut_thrust` byte-identical for 1- and 2-mode weapons; generalizes to the
poleaxe's 4-strike set with one comparator. Modes **feed** `percussion_authority`/`puncture_pressure` (§1) and the RESIST
rows (§2) — they don't replace them.

---

## Honest residual (what is grounded vs designed)

- **Well-attested (S1, ship as grounded):** A_HANDS force-ratio; the 4 RESIST cells' direction; the poleaxe/spear/staff/
  longsword mode SETS + the armour→thrust/half-sword selection rule (the single best-attested rule, already in-engine).
- **`[SIM-CALIBRATE]` within an evidence band:** B_ARC magnitude (0.02–0.06); the cloth RESIST fractions; mail.shear/
  puncture magnitudes; `plate.percussion` (gate-coupled).
- **`[DESIGN]` (flag, not grounded):** the per-mode geometry-override numbers (e.g. `hook_bec` strike_concentration,
  `end_thrust` point_concentration 0.3); the greedy-vs-tradition selection weighting; `demy_hache` as bind-not-strike;
  which modes the learned-access gate covers + its threshold.
- **Selection-effect (central caveat):** the whole model is **European-treatise-anchored**. Asian polearm mode-SETS are
  S3; their selection *doctrine* is largely undocumented (oral transmission) — a gap, not a claim those arts lacked it.
  If they enter the roster, their selection is reasoned-by-analogy and flagged.

## Engine mapping (minimal — the `cut_thrust` generalization seam)

`weapons.py`: add an optional `modes` list to multi-mode weapons (single-mode omit → read scalar `head`). `core.coupling`/
`systems.adef_cap`: generalize the internal `max(shear, puncture)` to a loop over the mode set. `wrapper` attack node:
`select_mode()` writes `c.head` (the single downstream write site — `core.strike`/`adef_cap`/`reach_threat` already read
`head`). `systems.legibility`: read the selected mode's head. `weapons.py`: add the longsword `mordhau`. `weapon_physics`:
A_HANDS=0.25/B_ARC=0.04. `core.py`: the 4 RESIST cells + the designer-set CI flag.

## Implementation roadmap (sequenced, each validated)

1. **Byte-identical scaffold** — `modes` field + generalize `coupling`/`adef_cap` `max()` to a mode-set loop; single/
   2-mode weapons reproduce current behaviour (verify the seeded 576-cell SHA unchanged).
2. **Re-baseline A — concussion single-source** — consolidate `core.p_auth`→`WP.percussion_authority` with A_HANDS=0.25/
   B_ARC=0.04 (corrects the uncommitted WIP placeholder 0.5/0.5).
3. **Re-baseline B — armour RESIST** — the 4 cloth/mail cells + CI flag.
4. **Re-baseline C — weapon modes + selection** — the poleaxe/spear/staff sets, the longsword mordhau, `select_mode`,
   the legibility wiring; behind the RULE-5 trained-access gate.

**Validation gates (WS-8):** non-blunt-vs-non-blunt cells byte-identical (bounded change); the full weapon×armour matchup
matrix matches the grounded ranking (poleaxe>mace>staff vs plate via the selected mode; mail strong-vs-cut/weak-vs-blunt;
plate near-immune-cut/vulnerable-concussion); mirror-50 + determinism (`test_combat_balance_guard.py`); no-one-shot;
`pytest tests/valoria`. File ED-1055+ with the designer-set values flagged.

## Provenance
Adversarially fact-checked Workflows (this session): biomech `wpwi3b9qf`, armour `wht7pkx1c`, use-mode `w4bekmb5e`;
treatise/historical grounding `w4h8gl48w`. Primary sources: Williams *The Knight and the Blast Furnace* (2003); Le Jeu de
la Hache (Anglo, Archaeologia 109, 1991); Silver *Paradoxes* (1599); Fiore *Fior di Battaglia*; Liechtenauer
Harnischfechten (Ringeck/Danzig); Oh et al. 2022; Nathan 2003; Cross & Nathan 2009. Full claim-level tiers in the task
outputs.
