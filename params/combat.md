<!-- version: v0.14-AUD5-R1 | sources: designs/combat/combat_v30.md | last_updated: 2026-04-03 -->
<!-- CANONICAL SOURCE: combat_v30.md supersedes stage8_combat.md -->
<!-- PATCHES APPLIED (canonical): PP-86, PP-91, PP-165, PP-171–172, PP-174, PP-188, PP-210, PP-215, PP-232, PP-238–239, PP-247–248, PP-258, PP-260–261, PP-263, PP-271, PP-273–277, PP-284–286, PP-290–292, PP-294–295, PP-337, PP-352, PP-382, PP-386, PP-406–407, PP-611–612, PP-615, PP-627 -->
<!-- ED-200/201/202/203 resolved 2026-04-04: wound cap, carry-over, recovery, pool floor -->
<!-- PP-232: Health formula revised; Stamina floor 2; armour wield constraint; wound penalty −1D only; -->
<!--         initiative order corrected (initiative holder declares last); tie result corrected; -->
<!--         weapon system rebuilt (Short/Long × Light/Heavy × Blade/Blunt matrix); STR in damage confirmed; -->
<!--         damage formula revised (armour-dependent modifier); Mass Mismatch exemptions corrected; -->
<!--         Close/Far zone terminology flagged ED-129 (open). Stage 1/2 struck ED-130. Reach zone flagged ED-129 (open). -->

# params_combat.md — Personal Combat

## Pool Formula
Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)
Stamina = Endurance × 5 (ED-694 canonical; PP-611 superseded). Variable action costs (standard 5, heavy 8, defensive 3). Armor adds to drain per action.
Health = (Endurance + 6) × (max Wounds + 1) — total pool, never resets. Wound threshold every (Endurance + 6) points of damage; Wound counter +1 at each threshold. Incapacitated at 0 HP. (PP-232, ED-438)

**Armour wield constraint (PP-232):** A character cannot wear armour whose Stamina modifier would reduce their Stamina to 1 or below.

Pool modifiers:
- Wounds: −1D per wound (cumulative). No Ob penalty from wounds. (PP-232)
- Fibonacci group bonus: +dice to Offence allocation only (see below)

## Weapon System (PP-232)

Weapons are defined by three binary axes. Base TN = 7. TN modifiers:

| Axis | Option A | Modifier | Option B | Modifier |
|------|----------|----------|----------|----------|
| Reach | Short | −1 | Long | +0 |
| Weight | Light | −1 | Heavy | +0 |
| Type | Blade | +0 | Blunt | +1 |

Final Hit TN = 7 + reach modifier + weight modifier + type modifier.

**STR minimums:** Each "Heavy" or "Long" axis adds +1 to minimum STR.
| Combination | Min STR |
|-------------|---------|
| Short Light (either type) | 1 |
| Short Heavy or Long Light | 2 |
| Long Heavy (either type) | 3 |
| Long Heavy Blunt | 4 |

Penalty if 1 below minimum: −1D Combat Pool. Cannot wield if 2+ below minimum.

**Blade vs Blunt note:** "Blade" encompasses cutting, piercing, and stabbing weapons. "Blunt" encompasses bludgeoning weapons.

Example weapons by combination:
| Combination | TN | Examples |
|-------------|-----|---------|
| Short Light Blade | 5 | Dagger, knife |
| Short Light Blunt | 6 | Sap, hand axe |
| Short Heavy Blade | 6 | Short sword, arming sword |
| Long Light Blade | 6 | Spear, light lance |
| Short Heavy Blunt | 7 | Club, mace (short) |
| Long Heavy Blade | 7 | Longsword, axe, glaive |
| Long Light Blunt | 7 | Staff, walking stick |
| Long Heavy Blunt | 8 | War hammer, pollaxe |
| Unarmed | 8 | Fists, grappling, improvised |

[EDITORIAL: ED-129 — Ranged weapon TN integration into Short/Long/Light/Heavy/Blade/Blunt matrix pending. Current ranged entries (LP, HP, sling) not yet mapped to new system.]

## Ranged Combat Rules (PP-172)

Ranged weapons require distance from the target to make an Offence roll. At melee range: cannot make a ranged attack. If forced to melee range by an attacker: may defend using full pool (no Offence split). [EDITORIAL: ED-129 — "Close zone" and "Far zone" terminology to be replaced with plain-language distance descriptors consistent with the new weapon reach matrix.]

**Cover:**
| Cover type | vs Light Piercing | vs Heavy Piercing | vs Light Blunt | vs Heavy Blunt |
|------------|------------------|------------------|----------------|----------------|
| Soft (trees, wagon, bale) | +2 DR | +1 DR | +2 DR | +2 DR |
| Hard (stone wall, fortification) | Blocks shot | Blocks shot | Blocks shot | Blocks shot |

**Environmental approach (melee closing):**
| Terrain | Rounds to close | Penalty to closer |
|---------|----------------|-------------------|
| Open ground | 1 round | None |
| Difficult (marsh, rubble, slope) | 2 rounds | +1 Ob to movement actions |
| Shallow river / ford | 2 rounds | +1 Ob, −2D combat while crossing |
| Deep river | 3 rounds + Swim (Ob 2) | Fail = swept back |
| Wall or rampart | Climb (TN 8 Ob 1) | Action lost if climb fails |

**Reload (Heavy Piercing crossbow only):** Full round after each shot. Light Piercing, Light Blunt, Heavy Blunt fire every round.

**Ranged STR minimums:**
| Weapon | Min STR | Penalty if 1 below |
|--------|---------|-------------------|
| Light Piercing (bow) | 2 | −1D |
| Heavy Piercing (crossbow) | 1 | — |
| Light Blunt (stone sling) | 1 | — |
| Heavy Blunt (lead sling) | 2 | −1D |

## Damage Formula (PP-232)

Damage = net hits + STR + weapon modifier vs armour tier (see table below)

STR is confirmed as a damage addition (PP-232, resolves ED-092).

Critical Hit (net hits ≥ 3): weapon modifier doubled before applying armour reduction.

**Weapon modifier vs armour tier:**
| Weapon Class | vs None | vs Light | vs Medium | vs Heavy |
|--------------|---------|----------|-----------|----------|
| Light Blade | +3 | +2 | +1 | +0 |
| Heavy Blade | +6 | +4 | +2 | +0 |
| Light Blunt | +3 | +3 | +3 | +3 |
| Heavy Blunt | +5 | +5 | +5 | +5 |

[EDITORIAL: ED-131 — Exact modifier values require playtesting to confirm. Values above are the design intent from comments; simulation needed before treating as final.]

## Initiative and Pool Allocation (PP-232)

Initiative determines declaration order, not action speed. Higher initiative = more information.

**Declaration order each round:**
1. Lower initiative holder declares Offence/Defence split first.
2. Higher initiative holder sees that split, then declares their own.

Exchange 1 initiative: higher Attunement acts last (highest information). Subsequent rounds: transfers to the exchange winner. Tie result: no damage to either side; initiative stays with current holder.

**Note (PP-232):** Replaces prior "simultaneous reveal" procedure. Initiative holder now declares last, gaining positional knowledge.

## Fibonacci Group Bonus (Offence dice only)
| Attackers | Bonus Dice |
|-----------|-----------|
| 1 | 0 |
| 2 | +1 |
| 3 | +2 |
| 4–5 | +3 |
| 6–7 | +4 |
| 8+ | +5 |

## Wounds / Incapacitation (PP-232)

Health (full) = (Endurance + 6) × (Max Wounds + 1), where Max Wounds = floor(Endurance/2) + 1. Total damage capacity. Equipment adds flat Health (+4 leather, +6 chain, +8 plate). Max Health = (End+6)×(MW+1) + equipment bonus. See `designs/scene/derived_stats_v30.md` §4.1 for authoritative spec. (PP-716 reverts ED-694 Vitality formula.) Healing cannot exceed max.
Wound Interval = Endurance + 6. Wounds accrue at floor(cumulative_damage / Wound_Interval). Computed on the fly — no Max Wounds stat.
Example: Endurance 4 → Vitality 40, Wound Interval 10. Wounds at 10, 20, 30 cumulative damage; incapacitated at Vitality 0.
Allows critical hits to deal multiple wounds simultaneously. (ED-694: replaces Health formula, eliminates Max Wounds.)

Per Wound: **−1D Combat Pool only** (no Ob penalty). (PP-232)

**Wounds computed on the fly:** wounds_taken = floor(total_damage / Wound_Interval). No Max Wounds stat. (ED-694, replaces PP-263 Max Wounds formula.)

| Endurance | Vitality | Wound Interval | Wounds before incap |
|-----------|----------|----------------|---------------------|
| 1 | 10 | 7 | 1 |
| 2–3 | 20–30 | 8–9 | 2–3 |
| 4–5 | 40–50 | 10–11 | 4 |
| 6–7 | 60–70 | 12–13 | 5 |

[ED-130 resolved 2026-04-03] Stage 1 (down) and Stage 2 (dying) incapacitation states STRUCK. No staged incapacitation states in current design. Health track runs to 0 = incapacitated.

## Mass Mismatch Penalty
Light weapon defender vs Heavy weapon attacker: defensive successes −1 (min 0).
Exempt: Full Guard only. (PP-232 — Long weapon at Close zone exemption removed.)

## Armour (Stamina modifier and wield constraint)
| Armour | STR Min | Stamina Mod |
|--------|---------|-------------|
| None | — | +0 |
| Light | 2 | +0 |
| Medium | 3 | −1 |
| Heavy | 4 | −2 |

Cannot wear armour if it would reduce Stamina to 1 or below (PP-232).
Damage Reduction (DR) is now subsumed into the weapon modifier vs armour tier table above.

## Ranged Damage Reduction (DR) by Armour Tier
| Armour | vs Light Piercing | vs Heavy Piercing | vs Light Blunt | vs Heavy Blunt |
|--------|------------------|------------------|----------------|----------------|
| None | 0 | 0 | 0 | 0 |
| Light | 2 | 1 | 1 | 0 |
| Medium | 3 | 2 | 2 | 1 |
| Heavy | 5 | 3 | 3 | 2 |

Cover DR stacks additively with armour DR.

## Actions Summary
Strike / Establish Distance / Feint / Take a Breath / Full Guard / Disarm / Retrieve Weapon / Reload (Heavy Piercing only) / Dodge (ranged attacks only — forfeit all offensive action; full pool as passive Defence vs one incoming ranged attack; armour DR applies) (PP-215) / Out of Breath (forced at Stamina 0)

## Stamina (ED-694)
Stamina = Endurance × 5. Range 5–35. Cannot wear armour that would reduce effective Stamina below action cost minimum.

<!-- patch_history: references/params_combat_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->

## Cover Declaration — Phase 1 Requirement (ED-098 resolved 2026-04-03)
Cover must be declared in Phase 1 to apply that round. GM determines physical availability from zone description. No declaration = no DR benefit that round.

## PP-238 — Feint full-pool
Feint commits full Combat Pool to Offence; Defence = 0 this round. Feinting character exposed — incoming attacks resolve against Defence 0. On success: opponent −2D Defence next round only.

## PP-239 — Initiative tiebreaker
Equal Attunement in Exchange 1: higher Agility acts last. If Agility also equal: GM or coin flip.

## PP-247 — Action priority order
| Priority | Action |
|----------|--------|
| 1 | Strike |
| 2 | Feint |
| 3 | Disarm, Tie Up, Retrieve |
| 4 | Establish Distance, Escape |
| 5 | Leap (Thread — full-round) |
| — | Full Guard, Take a Breath, Dodge, Rescue (reactive) |

## PP-273 (mass battle) — Minimum pool 1 die
Minimum 1 die after all penalties. Formation Break at Discipline 0 removes attacking. Command=0: 1 die minimum.

## PP-274 — Multi-engagement pool split
Target declares one Offence/Defence split; both attackers roll against same Defence allocation.

## PP-275 — Stamina maximum
Stamina capped at base value (End + H + 1 − armour mod). Take a Breath restores Endurance score, capped at base.

## PP-276 — Initiative mixed outcome
Both succeed at different priorities → initiative stays with current holder.

## PP-277 — Feint -2D ceiling
-2D is ceiling on Defence dice allocation (max Defence = pool − 2), not total pool reduction.

## PP-284 — Stage 1/2 clarifications
- Wound recovery: stabilised characters return after 1-scene rest; wounds clear at session end
- Stage 2 trigger: any attack with ≥1 net hit on downed Stage 1 character; downed = Defence 0

## Rescue — PP-290, PP-292
| Property | Value |
|----------|-------|
| Eligibility | Rescued actor outnumbered at Phase 1 declaration (Fibonacci condition); assessed at declaration only |
| Commit | Rescuer allocates N Offence dice (minimum 1) to contest; remainder defend own engagement |
| Contest | N dice TN 7 vs attacker's Offence roll (contested) |
| Win condition | Rescuer net ≥ attacker net |
| On win | Attack redirects to rescuer; resolves vs armour DR only (contest dice expended) |
| On loss | Attack hits original target; rescuer N dice wasted; own engagement Defence unaffected |
| Weapon speed | TN 5–6 attackers harder to intercept (higher expected net); TN 7–8 easier |
| Rescuer payoff (PP-406) | +2 Momentum on successful intercept if struck (≥1 wound) this Rescue round, any source; capped 2/round |
| Martyr Rule (PP-407) | Failed intercept + rescuer wounded from own engagement same round → +1 Momentum; no wound = no Momentum |
| Rescued actor payoff | Fibonacci exempt + untargetable this round (successful intercept only) |
| Exemption duration | Current round only |
| Zone | Adjacent zone |
| Fails silently | Ineligible / no declared attack — action lost |
| Chain block | Rescuers cannot be rescued the same round |
| Incapacitation at P1 | Rescue fails; attack reverts; no Momentum |

## Feint — PP-294
| Property | Value |
|----------|-------|
| Commit | Player chooses N dice (minimum 3) to Offence for feint; remainder to Defence |
| Roll | N dice TN 7 vs opponent's Defence pool TN 7 (sequential per initiative) |
| Payoff | B loses [margin] dice from total pool next round; scales with margin |
| Pool reduction floor | Minimum 1D (B cannot be reduced below 1D by Feint) |
| Non-stacking | Successive Feints reset reduction to current margin; do not accumulate |
| Expires | Pool reduction cancelled if Feinting actor incapacitated before reduction round |
| Initiative note | Higher initiative B sees A's commit and can over-allocate Defence; costs B offensive output |


## Resolved Rulings (2026-04-04)

### No wound cap per hit (ED-200 resolved)
No maximum wounds per single hit. Damage converts to wounds via the Health track
formula: every (Endurance + 6) Health depleted = 1 wound. A sufficiently powerful
hit can inflict multiple wounds in a single strike. This is the intended lethality model.

### No excess damage carry-over (ED-201 resolved)
Wound thresholds are milestones on a non-resetting pool. Health depletes continuously;
each time an (Endurance + 6) interval is crossed the Wound counter increments.
No excess damage is lost and no reset occurs. Wounds are discrete milestones, not resets.

### Recovery model (ED-202 resolved)
No Quick Rest / Full Rest distinction. Single recovery model:
- Take a Breath (combat action): restores Stamina up to base value
- Scene rest (post-combat): stabilised incapacitated characters return to consciousness
- Session end: all wounds clear

### Pool minimum — clean floor (ED-203 resolved)
Combat Pool minimum 5 is a clean floor. No −1D penalty at the floor. If penalties
would reduce the pool below 5, it stays at 5 with no additional modifier.

## PP-406: Rescue Momentum — ED-290
- Rescue Momentum on declaration: upgraded from +1 to **+2**
- Rationale: rescuer accepts double wound exposure (~96% probability both attacks land); +1 undervalued the sacrifice.

## PP-407: Martyr Rule — ED-292
- New rule: if a Rescue attempt **fails** AND the rescuer takes a wound from their own engagement in the same round → **+1 Momentum**
- Distinct from successful intercept payoff (which yields +2 per PP-406)
- Failed intercept with no rescuer wound: no Momentum return (correct tension maintained)

## Surrender and Disengage (PP-634)

**Yield:** Declared at Phase 1. Opponent chooses: Accept (combat ends; prisoner/withdrawal) or Refuse (unresisting — no contest roll). Cannot Yield while faction's objective is actively contested in zone.

**Disengage:** Phase 1 declaration, viable exit required. Roll Agility pool TN 7 Ob 1, contested if opponent spends action to pursue.
| Result | Outcome |
|---|---|
| Disengager wins or unopposed success | Leaves zone cleanly |
| Partial (unopposed, net 0) | Exits but opponent gets one free undefended strike |
| Disengager loses/ties (contested) | Cannot disengage this round |

Out of Breath (Stamina 0): −2D on Agility disengage roll. Wounds do not penalise disengage.

## Thread Integration Cross-References (F-07)

Combat mechanics operate on thread-configurations at the rendered level (Foundations A1). The following cross-references apply:

- **Wound → Thread Pool:** −1D per Wound to all Thread operation Pools — Leap, Weaving, Pulling, Mending, FR (per `designs/scene/derived_stats_v30.md` §4.1 universal rule; PP-716 supersedes prior +1 Ob framing). The body's damage impedes substrate-level suspension.
- **Incapacitation → Thread contact:** Contact terminates immediately on incapacitation (threadwork_v30 §2.3). Operation in progress resolves as Failure.
- **Death → Thread cascade:** Killing named NPC fires Knot rupture, Conviction Scar, Scene Slate entries, faction Stability trigger, Exposure (combat_v30 §13.3).
- **Dissolution in combat:** RS cost per threadwork_v30 §5.2. Scar on all witnesses per npc_behavior_v30 §3.4. Companion Thread departure per companion_specification_v30 §6.1.
- **Thread perception:** TS-sensitive observers perceive combat as thread events. See combat_v30 §10.2 and threadwork_v30 §2.3 ED-677 rendered-level visibility table.

