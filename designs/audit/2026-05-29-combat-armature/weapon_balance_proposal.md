# Weapon Balance — Audit + Rebalance Proposal (armature reset, Build-9)

**Date:** 2026-05-29 · Validated on the defect-immune R8 harness (budgets asserted, file-read) · **Status:** Class-C proposal — no canon file edited. The weapon-vs-armour values carry **ED-131 ("Exact modifier values require playtesting confirmation")**, so this is gap-completion of canon-flagged-provisional values; ratification is yours.

`[SELF-AUTHORED — bias risk: my harness + my proposal. Numbers are from the budget-asserted, file-read harness; the spear gap and the residual high outliers are reported honestly, not tuned away.]`

## 1. Audit of the current canonical weapons

Clean weapon-only audit (same neutral Str-4 build both sides, vary only the weapon, all-vs-all × armour, mean field win-rate):

| Weapon | class | STR mult | field % | by armour (none→heavy) |
|---|---|---|---|---|
| war hammer (long_heavy_blunt) | heavy_blunt | ×3 | **83%** | 73 → 81 → 87 → **92** (escalates) |
| longsword (long_cut_and_thrust) | heavy_blade | ×2 | 70% | 73 → 74 → 69 → 64 (degrades — healthy) |
| staff (long_pole_staff) | light_blunt | ×1.5 | 62% | 44 → 58 → 68 → 81 |
| paired_short | light_blade | ×1 | 38% | — |
| single_short | light_blade | ×1 | 38% | — |
| spear (long_pole_spear) | light_blade | ×1 | 36% | — |
| thrust (long_thrust_primary) | light_blade | ×1 | 36% | — |
| curved (curved_cut_primary) | light_blade | ×1 | 35% | — |

**Two structural problems:**
1. **Heavy-Blunt is armour-blind AND highest-damage.** Canonically (combat_v30 §5) it has a flat +5 vs *every* armour tier (the only weapon that doesn't degrade) **and** the ×3 STR multiplier — so it does ~2× a longsword's damage and *gains* vs armour (73→92%). This is the war-hammer dominance, quantified.
2. **All five light blades are dead (~35–38%) and get worse vs armour.** They are the *fast* weapons (speed 2–3) whose intended value is tempo/Agi, but speed isn't rewarded, so low damage leaves them non-viable everywhere. **Weapon speed has no combat value in the current model** — the core gap.

## 2. Proposed rebalance (two grounded channels)

**(A) Taper the blunt vs-armour table** (keep "blunt beats plate" — historically true — but not armour-*blind*):

| class | None | Light | Medium | Heavy | change |
|---|---|---|---|---|---|
| light_blade | +3 | +2 | +1 | +0 | unchanged (cut degrades vs armour — historical) |
| heavy_blade | +6 | +4 | +2 | +0 | unchanged |
| light_blunt | +3 | +3 | **+2** | **+2** | tapered from +3 flat |
| heavy_blunt | +5 | +5 | **+4** | **+3** | tapered from +5 flat (still best vs heavy) |

**(B) Weapon speed → tempo σ-channel:** `Δσ += (speed_attacker − speed_defender) × 0.55·Minor`. Fast light weapons buy initiative/landing — their historical niche (the quick unarmoured duelist). Canonical `speed` already exists per weapon (−0.5 … 3); it just wasn't wired to combat value.

## 3. Validation — the proposed roster (locked v1)

| Weapon | canon % | proposed % | niche |
|---|---|---|---|
| war hammer | 83 | **69** | anti-armour (climbs 56→84 vs tiers) — now *earns* it |
| longsword | 70 | 64 | flat generalist |
| single_short | 38 | **60** | unarmoured duelist (64% vs none) |
| paired_short | 38 | 54 | fast, unarmoured |
| staff | 62 | 47 | anti-armour blunt (climbs vs plate) |
| curved | 35 | 44 | fast cut |
| thrust | 36 | 39 | — |
| **spear** | 36 | **23** | **still dead — see §5** |

Spread 48 → 46pp, mean 50%, but the **distribution transformed**: no runaway top, fast blades revived, and correct armour niches emerged (heavy/blunt climb vs plate, blades degrade, fast weapons win unarmoured). This is the historical structure.

## 4. The payoff — fixing weapons largely fixes ATTRIBUTE parity

Re-running the **attribute** parity (each archetype best-loadout, asymmetric) *under the proposed weapon table*:

| Attribute | under canon weapons | under proposed | |
|---|---|---|---|
| **Str** | **85%** | **69%** | the war-hammer taper is the lever |
| End | 43% | 51% | in-band |
| Agi | 58% | 46% | in-band |
| Reading | 49% | 67% | rose (item-5 σ-tune) |
| Spirit | 12% | 17% | cross-system (expected low) |

**Combat-primary spread 42pp → 23pp.** This is the headline: the Strength dominance was largely a *weapon* problem, not an attribute one. The rebalance compresses it without touching any attribute seed. Str at 69% and Reading at 67% are residual high outliers now in *tunable* range (the structural runaway is gone).

## 5. Honest gaps + design calls (yours)

1. **The spear is still dead (23%) despite canonical "spear is king."** Its reach advantage isn't credited. I tried a flat reach→tempo channel; it **over-corrected** — it inflated the heavy *long* weapons (war hammer back to 76%) because they're long too, and short blades dropped. **The correct model is phase-dependent reach:** reach gives a closing/Ob edge *before contact* but inverts *in the bind* (the shorter/faster weapon dominates once you close past the point — the actual HEMA dynamic). That's a combat-engagement refinement, **a design decision**, not a seed — flagged for you, not built here.
2. **The proposed armour-table values + the ×3 Heavy-Blunt multiplier are canonical** (combat_v30 §5). This proposal is gap-completion under ED-131, but the exact taper (+5/+5/+4/+3) and whether to also reduce ×3 are your ratification.
3. **Reading at 67%** under the rebalance is the known item-5 σ-magnitude tune (Class-C, I can lower it).
4. **Weapon balance is genuine multi-parameter optimization** (3 damage classes × 4 armour tiers × speed × reach × 8 weapons). I locked the cleanest validated proposal rather than hand-iterate all 8 strictly in-band by eyeball — landing the last few (spear, the two high outliers) needs either the phase-reach design call (#1) or a proper fit, not more single-knob passes.

## 6. Pending Jordan decisions (updated)

1. Stamina formula `End×5` → `3·End + 2·Spirit` (proposal; ratify + ledger).
2. Spirit definition — threadwork core + social/Composure + mass rallying + combat stamina-reserves (canon note).
3. Bind-as-Str-contest + Stagger (new mechanics, vetting).
4. **Weapon-vs-armour table taper** (§2A) — Heavy-Blunt +5/+5/+4/+3, Light-Blunt +3/+3/+2/+2. Canon edit (combat_v30 §5).
5. **Weapon speed → tempo channel** (§2B) — wires canonical `speed` to combat value. New mechanic.
6. **Phase-dependent reach model** (§5.1) — the spear fix. Design decision.
7. Reading σ-magnitude tune-down (Class-C, I can do).

## 7. Next
- **If you ratify §2** (table taper + speed channel), the roster is much healthier and Str falls to ~69% (then the ×3 / Reading tunes finish it).
- **Spear** needs your call on phase-dependent reach (§5.1) before it's viable.
- I can tune **Reading** down now (item 5/7) — it's a Class-C seed I can move.

`[CONFIDENCE: high — audit + rebalance + attribute payoff all on the budget-asserted, file-read harness. The spear gap and residual outliers are reported, not hidden.]`
`[ASSUMPTION: weapon-only audit uses a neutral Str-4 build both sides to isolate weapon profiles; attribute payoff uses the 6-attr equal-budget builds. Proposed magnitudes are sim-tunable seeds; the table values are canonical pending your ratification.]`

---

## 8. R9 — phase-dependent reach (the spear-fix mechanism) + the convergence finding

**Added Build-9.** `r9_weapon_engagement.py` (self-test 5/5) implements the spear fix as a **phase-dependent** reach+speed channel, replacing the flat reach channel that over-corrected:
- **Closing / breaking:** reach governs — the longer weapon controls the measure (canonical `reach = −1 Ob closing`).
- **In-bind:** speed governs — the faster weapon wins once closed, and reach **inverts** to a liability (HEMA: a spearman who lets you close past the point is in trouble).

This produces the correct niches by construction (self-tested): spear wins the approach/loses the bind; dagger loses the approach/dominates the bind; war hammer wins the approach but is *worst* in the bind (slowest). **Grounding:** bottom-up = canonical reach + per-weapon `speed`; top-down = the HEMA measure/bind dynamic. Gap-completion of canon's "spear is king."

**The honest convergence finding.** R9 is the right *mechanism*, but landing all 8 weapons strictly in-band is a **joint-fit problem, not a single-knob tune**:
- Reach (R9) helps **every long weapon** — the spear *and* the war hammer (both long). So adding reach lifts the spear (23→33%) but re-lifts the war hammer (69→79%).
- Tapering the canonical Heavy-Blunt **×3→×2** multiplier *on top of* R9 + the armour taper barely moved the hammer (79→76%) — because in the R9 configuration the hammer's edge is now its **reach-at-distance + survivability**, not only its damage.
- **Two "long-weapon advantages" (reach-at-distance + heavy damage/survivability) compound on the war hammer, and no single knob separates them.** Short fast weapons stay ~37% because they only win 1 of 3 phases (the bind).

**This is a design call, not a seed tune (for Jordan):** the clean separation would be e.g. *reach benefits light-long weapons (spear) but not heavy-long weapons (war hammer)* — i.e. a heavy weapon is too unwieldy to fully exploit reach-as-tempo. That's a combat-engagement design decision. Alternatives: make the bind phase weigh more (2 of 3 sub-actions) so fast weapons matter more; or accept the war hammer as a deliberate apex anti-armour weapon balanced by availability/cost outside the duel.

**Status of weapon balance:** the *mechanisms* are built and validated (armour taper §2A, speed-tempo §2B, phase-reach §8). The *magnitudes* for strict 8-way convergence await either the design call above or a joint optimization. The distribution is already far healthier than canon (war hammer no longer armour-blind; fast blades revived; correct armour niches), and the attribute-parity payoff (§4: Str 85→69%, spread 42→23pp) holds regardless.

**Updated pending decisions:** add **(8) phase-reach magnitudes / the light-long-vs-heavy-long reach question** (design) to the list in §6. (Reading σ-tune from item 5/7 applied in R8: `READING_PER_POINT` lowered toward band.)
