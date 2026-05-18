# Mass-Battle Audit Flags — Comparator Review

**Date:** 2026-05-17
**Scope:** Two audit flags surfaced by Phase 12 mass-battle sim. Reviewed against acclaimed videogame + boardgame patterns.
**Authorized by:** ED-864 follow-on
**Companion to:** `tests/sim/phase12_mass_archetype_v0_2026-05-17.md`

---

## Flag 1 — HeavyBlunt Universal Anti-Armor (100/0 vs everything)

**Verdict: NOT a defect. Phase 12 sim artifact, not canonical imbalance.**

### Phase 12 finding

Knights Templar (HeavyBlunt + Heavy armor + Power 5) won 100/0 vs every other archetype. HB's weapon-effectiveness row in canon is `✓ vs none/light/medium/heavy` — universal penetration. Combined with Power 5 + +5 Dmg Mod, HB crushes anything in isolated pool comparison.

### Comparator survey

**Historical reality.** Maces, warhammers, war picks, halberds were the actual answer to plate armor (14th-15th c.). Swords concuss but rarely penetrate; blunt force transmits through plate. Anti-armor weapons existed specifically because they bypassed the armor problem.

**Videogame treatments:**

| Game | HB-equivalent | Balance mechanism |
|---|---|---|
| Mount & Blade Bannerlord | Blunt damage type effective vs armor | Slow weapon speed; vulnerable to swift unarmored fighters |
| Kingdom Come Deliverance | Armor-piercing maces | Slow swing; struggles vs evasive opponents |
| For Honor | Heavy weapons (Lawbringer halberd, Conqueror flail) | Predictable patterns; light fighters dodge/parry |
| Total War: Medieval II | Knights Templar / heavy infantry | Cost, fatigue, terrain, cavalry rear-flank, missile pre-contact |
| Battle Brothers | Two-handed maces (armor-piercing) | Fatigue cost; slow attack speed |
| Warhammer 40K | Power weapons / Power fists | Slow strike order; limited model count |

**Boardgame treatments:**

| Game | HB-equivalent | Balance mechanism |
|---|---|---|
| War of the Ring | Elite/special units | Leader-cost; activation limits; positional requirements |
| Memoir '44 | Heavy infantry / elites | Battle cards limit which sectors activate; terrain restricts movement |
| Combat Commander | Elite firepower | Cards drive resolution; Recovery + morale checks gate sustained advantage |
| Crusader Kings (BG) | Heavy infantry counters cavalry | Rock-paper-scissors triangle; cavalry counters archers, archers counter heavy infantry |

### Pattern extracted

Acclaimed games include HB-style anti-armor weapons as canonical. They balance via:
1. **Cost / rarity** — Power-5 elites are expensive; fielded in small numbers
2. **Speed / initiative** — heavy weapons strike last or have predictable timing
3. **Logistics / fatigue** — heavy units break first in sustained engagement
4. **Counters** — cavalry rear, missile pre-contact, terrain denial
5. **Composition limits** — battle scenarios restrict which units arrive

None of these are pool-comparison reductions. All are *contextual* — they operate outside the single-engagement pool roll.

### Diagnosis

Phase 12 sim isolated single engagements at equal Size and equal cost. That's not how acclaimed games — or actual battles — resolve. Knights Templar are Power 5 elite; in real campaigns they'd be 5–10% of forces, not 50% of matchups. The 100/0 result is sim-of-isolation artifact.

### Recommendation

**No mechanic change to weapon effectiveness or DR.** HB anti-armor is canonically correct.

Verify the existing surrounding systems handle the contextual balance:
- **Power-tier scarcity** — does `params/mass_combat.md` cap Power-5 units as % of force composition? If not, add cap (recommend 10–15% max).
- **Cost differential** — recruitment/upkeep cost ratio between Power-5 and Power-2 units should be 3–5x. Audit `params/economy.md` or equivalent.
- **Battle composition** — terrain, season, distance-to-deployment restrictions should reduce HB unit availability in non-set-piece battles.

If those three contextual systems exist and produce realistic force composition, Phase 12's 100/0 is acceptable — HB elites WIN when present, are RARE in practice.

If contextual systems are missing or under-tuned, that's the actual defect — not weapon effectiveness.

**Action:** audit Power-tier composition rules in faction recruitment / battle composition layer. Separate task from C4. File as follow-on ED.

---

## Flag 2 — Heavy-vs-Heavy Stalemate (100% draws in pool comparison)

**Verdict: NOT a defect. Canonical resolution shape; depends on tactical-lever layer (currently unmodeled in Phase 12).**

### Phase 12 finding

HC vs Heavy armor = ✗ in weapon effectiveness table. Two Heavy Infantry units in pool-comparison engagement deal zero damage to each other → 100% draw at max_rounds. Same for HeavyCav-vs-HeavyInf, VetHeavy-vs-HeavyInf, etc.

### Comparator survey

Heavy-vs-heavy stalemate-by-pool-alone is the **canonical engagement type** in acclaimed games. Resolution comes from tactical layers, not pool comparison.

**Videogame treatments:**

| Game | Heavy-vs-Heavy resolution |
|---|---|
| Total War: Medieval II / Three Kingdoms | Pool grinds for minutes; resolves via flanking, fatigue, morale break, leadership |
| Battle Brothers | Fatigue accumulates; even heavies break after sustained combat |
| For Honor | Stamina exhaustion (whoever drops guard first), not damage trade |
| Mount & Blade Bannerlord | Tactical AI flanks during sieges; sustained pushes break via morale |
| Old World / Civilization VI | Leadership bonus traits + tile bonuses + general levels decide engagements |
| Crusader Kings 3 | Commander skills + martial trait + terrain + supply decide; raw stack-size insufficient |

**Boardgame treatments:**

| Game | Heavy-vs-Heavy resolution |
|---|---|
| War of the Ring | Leader pool spent for re-rolls + special abilities; commander attrition matters |
| Combat Commander | Recovery cards (resupply, morale rally) + Initiative cards drive resolution; pure unit-vs-unit doesn't |
| Memoir '44 | Battle cards limit which sectors can act; "stalemate" breaks via card hand differential |
| Twilight Struggle | Operations cards drive coup attempts; raw strength isn't enough |
| Twilight Imperium | Tech advancement + leader actions + agenda phase manipulation |
| Pax Pamir / John Company | Political setup, family specialization, bidding — combat is rare and resolved by political math |
| Inis | Card-driven retreat/casualty negotiation, not pool comparison |

### Pattern extracted

Every acclaimed system resolves heavy-vs-heavy via one or more of:

1. **Flanking** — positional/tactical maneuver (Total War, Memoir, COIN, Inis)
2. **Fatigue / morale** — endurance attrition (Battle Brothers, For Honor, Total War)
3. **Reserves / reinforcement** — strategic depth (Twilight Struggle, Risk, War of the Ring)
4. **Tactic cards / event cards** — special abilities (War of the Ring, Combat Commander, Memoir)
5. **Leadership / Command** — commander differential, decapitation (Total War, Bannerlord, CK3)

None resolve via pool-arithmetic alone. **Pool comparison without tactical layer = stalemate is the expected output.**

### Diagnosis

Valoria's `params/mass_combat.md` already specifies these layers — Command, Discipline, tactic cards, multi-phase engagement structure. Phase 12 sim deliberately modeled ONLY the Phase 5 pool resolution to isolate the archetype-matchup question. The 100% draw is canonical because Phase 12 is intentionally a pool-only test.

The follow-on work is already in Jordan's pipeline:
- `tests/sim/v17-integration/m3_mass_battle.py` — validated engine that DOES model tactic cards (per handoff `2026-05-18-phase-7-mass-battle`)
- Phase 7 Mass Battle integration port — converts single-roll Conquest in faction_action.py to multi-unit mass-battle resolution
- `sim/provincial/tactic_cards.py` exists (currently BLOCKED on contamination audit per integration_plan_v18.md §1.4)

### Recommendation

**No mechanic change.** Stalemate is canonical resolution shape; tactical layer is the resolution mechanism.

Three verification tasks (sequential, not blocking):

1. **Command-differential sim** — pure pool comparison with Command 5 vs Command 7 heavy-vs-heavy. Does the Command 7 side break the stalemate via Discipline rolls / Pool advantage? Target: ~60/40 in Command-favored direction.

2. **Tactic-card-effect sim** — once tactic_cards.py contamination audit resolves (per handoff), run heavy-vs-heavy with active tactic-card play. Target: variance + interesting outcomes, not deterministic.

3. **Phase 13 — full Battle Turn integration sim** — Phase 1 (Recon/Initiative) through Phase 7 (Aftermath). Heavy-vs-heavy should resolve via accumulated Discipline attrition + tactic-card pressure + morale break, not pool damage.

If verification tasks 1–3 produce *interesting* play (variance, meaningful choices, asymmetric outcomes), heavy-vs-heavy is solved. If they produce *theatrical* stalemate even with tactical layer active, then weapon-effectiveness table needs HC-vs-Heavy = ✓ marginal damage instead of ✗ binary zero — but that's a fallback, not the first recommendation.

**Action:** verification sims 1–2 fold into the existing Phase 7 Mass Battle handoff (Jordan's active pipeline). No separate ED needed; sequence as Phase 7 + Phase 8 follow-on per the handoff plan.

---

## Cross-Flag Synthesis

Both flags share a diagnosis pattern: **Phase 12 isolated pool comparison from canonical contextual systems.** The pool layer in isolation produces extreme outcomes (100/0, 100% draw); those outcomes are sim-of-isolation, not canon defects.

Acclaimed games — including Valoria's own design canon (mass_battle_v30, params/mass_combat.md) — handle mass-battle balance via contextual systems: cost, scarcity, terrain, tactic cards, Command, morale, flanking. The pool roll is one variable among many.

**Implication for Reframing 2:** the Phase 12 100/0 categorical Heavy dominance over Light at mass scale is the CORRECT signal — light archetypes cannot threaten heavy via pool comparison. But the full mass-battle outcome depends on whether the player's faction can RECRUIT and DEPLOY heavy units, which depends on economy, population, faction-specialty, terrain, and campaign context. Reframing 2 holds: Heavy dominates mass scale *when present*; light dominates scene scale *across all engagements*.

---

## Related

- `tests/sim/phase12_mass_archetype_v0_2026-05-17.md` — source sim with the two flagged matchups
- `params/mass_combat.md` — Core Formula, DR Table, Weapon Effectiveness
- Active handoff `2026-05-18-phase-7-mass-battle` — Jordan's pipeline for tactical-layer integration
- ED-864 — original audit decision record
- ED-839 — Phase 10 reform baseline
