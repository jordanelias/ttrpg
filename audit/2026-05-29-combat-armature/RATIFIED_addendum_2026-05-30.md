# RATIFIED — Addendum 2026-05-30 (combat armature continuation)

Appends to `RATIFIED_2026-05-29.md`. All items canon-of-record as of 2026-05-30, per Jordan directive "ratify all." `[CONFIDENCE: high — each validated by the weapon_axes_v2 pipeline (self-test 10/10) and grounded in the canonical combat substrate + the project's own historical research.]`

## W5 — Point-vs-armour gap row (`POINT_ARMOR_MOD`)
A **point** (thrust) weapon on a light blade uses a distinct weapon-vs-armour row: **+3 / +3 / +2 / +1** (none/light/medium/heavy), where the cut row drops to +0 vs heavy. Models the thrust finding armour **gaps** (visor, armpit, groin) — the historical anti-plate strategy (half-swording, the estoc/tuck, the rondel dagger). Extends the `combat_v30 §5` weapon-vs-armour table; validated balance-safe (a light weapon's *modest* answer to armour — not plate-defeating; the heavy-blunt stays the true plate-breaker).
- **Status:** ratified. Prose propagation into `combat_v30 §5` table — PENDING (same batch as the other ratified-but-unpropagated armature items).

## H1 — Handling reassignments (two grounded corrections)
- **Longsword: Standard → Demanding.** The Liechtenauer art is the canonical *highly technical* tradition (the seven-axes tactile/bind exemplar); a master is formidable in a duel, a novice flails. High skill ceiling.
- **War flail: Demanding → Forgiving.** The blunt-weapon survey grades it a *crude Hussite peasant equaliser* — low floor, no refined corpus; its parry-bypass is a **quirk**, not a high skill-ceiling.
- **Status:** ratified. Updates the v32 draft handling assignments; flips the corresponding `weapon_axes_v2.py` annotations from "proposed/flagged" to ratified.

## Note — Stamina S⚠ flag resolved
The canonical armour atom (`3.4 Armour`) flagged **S⚠**: armour's per-action Stamina drain depended on the Stamina formula being settled. That dependency is now **resolved** — ratified **S1: Stamina = 3·End + 2·Spirit** (2026-05-29) supersedes the old `End×5` / `End+History+1−armour` the flag worried about. Armour drain is a **per-action drain modifier** (+0/+0/+1/+2), not a base-Stamina reduction. The armour atom's S criterion now passes.
