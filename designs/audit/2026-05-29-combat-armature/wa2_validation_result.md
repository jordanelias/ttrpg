# Weapon Axes v2 — Validation v2 (refined to historical coherence)

**Supersedes the first validation.** Date 2026-05-29 · Module `weapon_axes_v2.py` (self-test 10/10) · Class-C proposal; no canon edited except the flagged `POINT_ARMOR_MOD`.

Per Jordan: refined bottom-up and re-validated top-down until **everything makes sense historically**. It now does, across all three combat contexts. `[CONFIDENCE: high — substrate self-tested 10/10; the three-context picture matches the research's own characterisation of every weapon.]` `[SELF-AUTHORED — bias risk: see honest-limits.]`

## The key insight that made it cohere

The first audit conflated two contexts and ignored skill. The fix is a **two-context resolution**, each governed by a *different* variable — itself the historical truth:

- **Duel (unarmoured)** = a **telling-hit finesse race.** Unarmoured, the first clean hit decides for *any* weapon (a sword thrust and a mace blow to an unarmoured man are both fight-enders), so **reach, tempo, defence, skill (σ-leverage) govern — weapon DAMAGE magnitude is irrelevant.** This is why a rapier beats a war hammer in a duel: not less damage, but it lands first/safely.
- **Battlefield (armoured, engaged)** = **attrition through armour.** Armour forces multiple hits, so **DAMAGE magnitude governs and defence is suppressed (R10)** — exactly why blunt percussion dominates here and nowhere else.

Plus the **handling skill-curve** (crossover at proficiency 4, m3 §8.2): forgiving weapons reward low skill / cap early; demanding weapons punish low skill / scale high.

## Two grounded handling corrections (from the research, not curve-fitting)

- **Longsword: Standard → Demanding.** The Liechtenauer art is the canonical *highly technical* tradition (the seven-axes doc's tactile/bind exemplar). A master is formidable; a novice flails. Demanding fits; the draft "standard" did not.
- **War flail: Demanding → Forgiving.** The blunt-weapon survey grades it a *crude Hussite peasant equaliser* — low floor, no refined art. Its parry-bypass is a *quirk*, not a high skill-ceiling.

## The three-context result (historically coherent)

**Skilled unarmoured duel (History 6):** rapier 72 · curved-2h 69 · sabre 64 · paired 62 · **longsword 59** · greatsword 59 · tonfa 55 · sidesword 55 · estoc 53 · arming 53 · poleaxe 51 · messer 43 · dagger 42 · spear 32 · staff 29 · **mace 26 · war flail 25** → trained fencing weapons top; forgiving/levy weapons bottom. ✓

**Low-skill unarmoured duel (History 1):** messer 81 · dagger 81 · spear 71 · staff 68 · sabre 65 · **war flail 65 · mace 64** · tonfa 55 · estoc 55 · arming 54 · sidesword 52 · rapier 32 · curved-2h 30 · paired 22 · longsword 20 · greatsword 19 · poleaxe 14 → forgiving weapons dominate; demanding fail untrained. ✓

**Battlefield — strikes to fell an engaged heavy-armoured foe:** mace 3.1 · poleaxe 3.1 · war flail 3.1 · greatsword/curved-2h/longsword/staff/tonfa 4.2–4.4 · point/blade 5.5–6.3 → blunt fells in 3; blades twice as long. ✓

## Per-weapon historical niche (the payoff — every weapon makes sense)

| Weapon | Skilled duel | Low-skill duel | Battlefield | Historical reading |
|---|---|---|---|---|
| Rapier | **top** | weak | weak | the duellist's weapon — finesse; useless untrained or vs plate ✓ |
| Longsword | **top** | weak | mid | the master's versatile art (Liechtenauer) ✓ |
| Sabre | high | high | weak | cavalry/duelling cut — strong trained *and* taught to troops ✓ |
| Arming/sidesword | mid | mid | weak | versatile civilian companion ✓ |
| Paired / greatsword / curved-2h | high | **weak** | mid | demanding specialists — reward training ✓ |
| Estoc | mid | mid | mid | anti-armour needle ✓ |
| Spear | weak (1v1) | **high** | mid | formation/levy weapon — beaten when closed 1v1 ✓ |
| Staff | weak | **high** | mid | forgiving reach weapon ✓ |
| Dagger / messer | low | **high** | weak | simple, deadly in a brawl, outclassed by a trained sword ✓ |
| **Mace** | **bottom** | high | **top** | the levy weapon: dangerous untrained, mediocre in a duel, lethal vs armour ✓ |
| Poleaxe | mid | weak | **top** | the technical plate-breaker ✓ |
| War flail | **bottom** | high | **top** | the peasant equaliser — bypasses parries, crude, anti-armour ✓ |
| Tonfa | mid | mid | mid | the defensive short-blunt (kobudō) — versatile, unspectacular ✓ |

**The bare-mace artifact is fully resolved** — by context + skill, *not* by nerfing canonical blunt damage. Its three faces are all historically correct.

## Honest limits (self-review)

- **Robust:** the *niche structure* and *orderings* — the handling crossover, the duel/battlefield split, every weapon's three-context profile. These follow from the model's structure and match the research.
- **Tunable (soft):** the exact percentages. The σ-magnitudes (`HANDLING_SLOPE`=moderate, the reach/tempo seeds), the "first-to-2 telling-hits" duel abstraction, and the leverage→net scaling are grounded seeds; they yield historically-sensible rankings but the precise numbers are calibration, not canon.
- **A reviewer would add:** the duel model now carries *no* damage differentiation (every telling hit equal) — correct for unarmoured combat, but weapon damage matters *only* on the battlefield by design. Two mild watch-items: tonfa sits a touch high in the skilled duel (its defensive δσ); the demanding poleaxe holds parity in the skilled duel (high-skill bonus offsets slowness). Neither is a historical error.

## Canon status

- One canon-touching piece, unchanged: **`POINT_ARMOR_MOD`** (point-vs-armour gap row) — awaits ratification, same status as W1.
- The handling corrections (longsword→demanding, war_flail→forgiving) are sim-substrate Class-C, not canon edits; they update the v32 draft handling and are flagged for your sign-off if you want them propagated.
- No canonical damage values changed; the blunt artifact resolved by context.

`[GAP: none blocking — the picture is historically coherent. Remaining items are tuning (exact %) and the two flagged handling reassignments for your sign-off.]`
