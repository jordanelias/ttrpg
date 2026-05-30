# Strength Calibration — Result (armature reset, Build-8 follow-up)

**Date:** 2026-05-29 · Calibration on the defect-immune R8 harness (budgets asserted, file-read) · **Status:** finding — the lever is **canonical** (weapon profile), not a Class-C seed. Jordan's call.

`[SELF-AUTHORED — bias risk: my modules; the calibration isolates the cause in canon (the weapon table), not in my tunable channels.]`

## Directive (a): dial Str's magnitudes down → it doesn't work, and here's why

I swept Str's Class-C leverage scale from 100% → 0% (all of bind / armour-defeat / stagger / pressure off), loadouts fixed:

| Str-leverage scale | Agi | Str | End | Reading | Spirit |
|---|---|---|---|---|---|
| 1.0 (current) | 58 | **83** | 47 | 42 | 18 |
| 0.5 | 60 | 80 | 47 | 44 | 18 |
| 0.0 (channels OFF) | 61 | **76** | 46 | 46 | 19 |

**Turning my Str channels entirely off only moved Str 83 → 76.** The dominance is not in the tunable channels. Tuning the Class-C seeds cannot fix it.

## Exact diagnosis: it's the canonical war hammer, not Strength

Isolation (Str leverage OFF throughout):

- **Everyone on the same weapon (longsword/heavy): Str = 51%.** Perfectly balanced. Strength's *attribute* value (damage multiplier, bind, stamina) is fine.
- **Str-5 picks up the war hammer (others longsword): Str = 79%.** The entire over-strength appears the moment Str accesses the heavy weapon.

Damage per strike (net 2 / net 3) vs **medium** armour:

| | net2 | net3 |
|---|---|---|
| Str-5 war hammer (Heavy-Blunt) | **22** | **28** |
| Str-5 longsword (Heavy-Blade) | 14 | 17 |
| Str-3 longsword | 10 | 13 |

The war hammer does **~2× a longsword's damage** because canonically (combat_v30 §5) **Heavy-Blunt = STR ×3 multiplier + a flat +5 vs EVERY armour tier**. It's the only weapon class whose armour modifier does **not** degrade vs armour (+5 vs none = +5 vs heavy). Heavy-Blade, by contrast, goes +6/+4/+2/+0 (useless vs plate). So the war hammer is both the hardest-hitting AND the only armour-ignoring weapon.

## The finding (for Jordan — canonical lever)

**Strength is balanced; the war hammer (Heavy-Blunt profile) is overpowered.** Two canonical knobs, both in combat_v30 §5 (yours to set; I will not edit canon):

1. **Heavy-Blunt's flat +5 vs all armour tiers.** Every other weapon degrades vs armour; Heavy-Blunt doesn't. Historically blunt *does* beat plate — but "ignores armour entirely AND hits hardest" is the over-tune. Option: taper it (e.g. +5/+5/+4/+3) so it's still the best anti-armour option without being armour-blind.
2. **Heavy-Blunt's ×3 STR multiplier** (vs Heavy-Blade ×2). Combined with #1 it's double damage. Option: leave ×3 (it's the slow heavy weapon's identity) but pair with the #1 taper.

These are `[INTENT UNDETERMINED]` until you rule — the ×3 + flat-+5 may be deliberate (the pollaxe/warhammer-defeats-plate design), in which case the war hammer is *meant* to dominate armoured fights and the "balance" lever is elsewhere (e.g. weapon availability / cost, or a speed/Stamina penalty making it situational). That's a design call.

## Secondary finding: weapon choice dominates attribute choice

With everyone on the longsword, **Reading jumps to 75%** — once weapons are equalised, the σ-leverage (Reading/Agi) axis is strongest. So the current build "balance" is driven more by **weapon selection than by attribute selection.** This suggests the next balancing pass should be **weapon balance** (the weapon-vs-armour table + multipliers), not attribute seeds — the attributes are closer to equal than the weapons are.

## Spirit — reframed (per Jordan 2026-05-29), NOT a combat fix

Jordan: Spirit also covers social contests (with Composure), mass-battle rallying, and is the core threadwork stat — in addition to its combat stamina-reserve role. **So Spirit's 12% in personal combat is correct, not a defect.** Spirit's equal value is *cross-system*; a Spirit-dump build is meant to be weak in a duel and strong in social/mass/thread. I am **not** force-buffing Spirit in combat (that would over-engineer combat and break the "every attribute contributes game-wide, not per-system" principle). The combat sim cannot assess Spirit's true value — that needs a social/mass/thread audit.

## Status of "equal value" (combat-primary attributes)

On **uniform weapons**, the combat-primary attributes are close to equal: Agi 52 / Str 51 / End 58 / Reading ~75 (Reading high — its own tuning item). The **attribute** balance is largely there; what's NOT balanced is **weapons** (war hammer) — and that's canonical.

## Pending Jordan decisions (updated)

1. **Stamina formula** `End×5` → `3·End + 2·Spirit` (proposal; ratify + ledger).
2. **Spirit definition** — now explicitly: threadwork core + social/Composure + mass rallying + combat stamina-reserves. Canon note (editorial ledger) — widened again this session.
3. **Bind-as-Str-contest + Stagger** — new mechanics (vetting).
4. **NEW — war-hammer / Heavy-Blunt profile** (the real Str-dominance lever): taper the flat +5-vs-all-armour and/or the ×3 multiplier, OR confirm it's intended (armour-defeating heavy weapon) and balance via availability/speed instead. Canon edit (combat_v30 §5).
5. **NEW — Reading σ-leverage magnitude** (75% on uniform weapons) — Class-C, tunable down (I can do this once weapons are settled).

## Next
- **If you taper the war hammer** (decision 4), I re-run R8 — Str should fall to ~50s and the combat-primary four converge.
- **Reading** (item 5) I can tune down now or after weapons settle.
- Spirit needs no combat action; its value is cross-system.

`[CONFIDENCE: high — uniform-weapon Str 51% vs hammer-access 79%, damage table, all on the asserted-budget harness. The over-tune is canonical (weapon profile), confirmed by isolation.]`
