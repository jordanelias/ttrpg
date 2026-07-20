# Reconciliation — Session Multi-Phase Calibration ↔ Ratified Combat Armature
**2026-06-01 · staged, not committed (lanes ignored per Jordan directive)**

Reconciles this session's multi-phase + stamina-press + armour-context calibration against the ratified
armature in `designs/audit/2026-05-29-combat-armature/` (5 `RATIFIED_*` files + 4 validation results, all
read full this session). `[CONFIDENCE: high — every row traces to a ratified file or a session sim run.]`
`[SELF-AUTHORED — bias risk: this reconciles my own session work against ratified canon; deltas favour canon.]`

`[READ: RATIFIED_2026-05-29, RATIFIED_addendum_2026-05-30 (×4: base/damage/leverage_gating/tempo_axes),
strength_calibration_result, armour_validation_result, wa2_validation_result, grappling_validation_result
— all full]`

## Verdict

**Consistent.** This session's calibration independently reproduced the ratified armature's structure and its
two headline findings. The deltas are "adopt the ratified seed," not "disagree." Two amendments must be
recorded against the ratified record; one canon item (Health cliff) is reopened as a proposal at a higher bar.

## A — Convergence (session result = ratified result, reached independently)

| Concern | Ratified armature | This session | Status |
|---|---|---|---|
| Damage shape | **D1**: Impact(additive Str+Heft) × Coupling(material×mode) × Quality(degree) | unified model: force-cap → coupling(material×mode) → quality outside cap | same shape ✓ |
| Armour cost | **A1** σ-tempo penalty, seed `0.5·minor`/drain-pt | `armor_tempo` run at exactly this | same lever ✓ |
| Armour matrix | **A2** material/coverage regenerates weapon-vs-armour table | coupling grid (cloth/mail/plate × perc/shear/punc) | same structure ✓ |
| Duel vs battlefield | **C1** duel=σ-leverage / battlefield=damage-governed, defence suppressed | personal baseline balanced / armoured battlefield Str-led | same split ✓ |
| Leverage→damage | **L1** σ-leverage gates Quality, seed `LEVERAGE_TO_DEGREE=3.5` | degree feeds damage (partial) | same chain; adopt their seed |
| Equal value | strength_calibration: uniform Agi52/Str51/End58/Reading~75 | uniform thrust/light Str51/Agi50/End49 | same measurement ✓ |
| Fatigue role | armour_validation §3: "fatigue erodes duel" **struck** (symmetric fatigue cancels) | this turn: armour-fatigue barely moved plate-vs-light → dropped | same conclusion ✓ |

## B — Corrections to my prior-session assumptions (canon wins)

1. **Stamina `3·End+2·Spirit` is RATIFIED (S1)**, not stale. Last turn I worried `End×5` (combat_v30 prose)
   superseded it — backwards. S1 *replaces* `End×5`; the prose is unpropagated lag. My formula was right.
2. **Wound model `WI=End+6 / MW / Health=WI×(MW+1)` is RATIFIED UNCHANGED (R2 + D1 both reaffirm).** My
   "Vitality replaces Health" worry was the unpropagated ED-548/694 prose; the armature explicitly keeps it.
3. **STR×weight ×3 multiplier is REMOVED by D1** (additive Impact). W4 ("hammer ×3 identity stays") is
   preserved via **Heft + Coupling (percussion vs plate)**, not a lookup. Treat the multiplier as gone.

## C — Deltas to absorb into the session harness (so numbers track ratified canon)

- Adopt **D1 additive Impact** (already the shape) + **`LEVERAGE_TO_DEGREE = 3.5`** (L1).
- Verify coupling reproduces **W1 blunt taper +5/+5/+4/+3** and **W5 point-gap +3/+3/+2/+1**
  (validation asserts: blunt fells plate ~3, point ~5.5, cut ~6.2 — confirm session grid matches).
- Adopt **H1 handling**: longsword Standard→**Demanding**, war-flail Demanding→**Forgiving**.
- The plate-counter triad is **complete + validated**: blunt / point-to-gaps / **grapple** (`grappling.py`
  6/6; dagger-finish bypasses mitigation; loses to unarmoured spacer 0%, beats armoured man 98%). The
  grapple is not the gap I flagged last turn — it is a built module awaiting ratification.

## D — Amendments that MUST be recorded against the ratified record

1. **Multi-phase supersedes R2.** R2 ratified "fight = one decisive phrase (not attrition)." Jordan then
   directed **multi-phase exchanges** (approaches/disengagements; ~4 phases; Health+stamina persist, initiative/
   stance reset per phase). This is a direct supersession of a ratified item — canon-of-record currently
   contradicts the standing multi-phase decision. **Must be written in.**
2. **Health cliff is now a proposal against *reaffirmed* canon.** R2 + D1 reaffirm the wound model unchanged;
   the `MW: 2→3` integer step at End4 cliffs Health 27→40. Session-B's smooth σ-leverage derivation
   (`Health ≈ 24+5.6·(End−2)`, keeping wound *tiers* discrete) is reopening freshly-ratified canon — higher
   bar. **Jordan's call to reopen.**

## E — Open tuning items (pre-identified, not new)

- **Reading σ-magnitude ~75% / near-binary** (session-C) = strength_calibration item #5, explicitly
  "tunable down once weapons settle." Not a new defect — a known knob. Intended-steepness vs upset-room is
  Jordan's design call.
- σ-tempo / leverage / handling magnitudes are grounded **seeds**, not canon (Class-C).

## F — Martial traditions / skill-craft layer (the original question)

Authored as a **Class-C proposal** (`martial_traditions_mapping.md`), grounded bottom-up in the 8-weapon
roster + ratified σ-leverage model, top-down in the project's combat-manuals research. The seven axes
(reach·speed·stance·initiation·footwork·grip·technique) map to engine channels; a **tradition = a named
bundle of σ-leverage biases** (German→bind, Italian→tempo, Spanish→facing, Japanese→reading, Chinese→committed
thrust, Filipino→flow). Resolves session-C's "named sets/coherence" — they are real (Thrust Duelist, Bind
Fighter, Counter-time, Burst, Continuous-flow), but proposal-status, not propagated.

**Left to Jordan (contract):** (1) add a **short-blunt** weapon class (documented gap, thin if added);
(2) **in-world culture names** for the traditions (creative layer — not Claude's).

## G — Status / what is NOT done

- **Not committed.** Whole armature is "ratified but prose-propagation pending"; propagation routes through
  authorized commit paths + lanes, which Jordan said to ignore. Reconciliation is **staged**.
- **Not yet read:** `damage_model_design`, `weapon_axes_v2`, `armour_system_design`, `grappling_system_design`,
  and the three handoffs (`propagation_/sigma_leverage_/harness_defect_`). Read before any propagation.
- Editorial-ledger has an open **ID-collision backlog** — ED IDs for S1/S2/ST1/W1–W5/C1/A1/A2/L1/D1/H1
  unassigned, Jordan-adjudicated.
