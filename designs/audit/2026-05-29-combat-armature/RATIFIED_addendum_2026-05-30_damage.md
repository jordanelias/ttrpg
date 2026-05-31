# RATIFIED — Addendum 2026-05-30 #3 (ground-up damage rebuild)

Appends to the armature RATIFIED records. Canon-of-record per Jordan "ratify commit." `[CONFIDENCE: high — self-test 8/8 + full-roster validation; anchored to the unchanged wound model.]`

## D1 — Damage = Impact × Coupling × Quality (replaces the inherited damage formula)
Damage is rebuilt from the ground up, derived only from the combat resolution (net/degree) and the wound model (WI=End+6):
- **Impact = Strength + Heft(weight)** — **additive force; NO Strength×weight multiplier.** *(The additive-vs-synergy fork is resolved toward additive, as built — the flat ×1/×1.5/×2/×3 lookup is removed; a strong fighter no longer gets disproportionately more from a heavy weapon.)*
- **Coupling = Delivery(head) × Transmission(material, mode) × GapAccess(coverage)** — derived from **material resistance-per-mode** (percussion/shear/puncture). The weapon-vs-armour matrix now **emerges** from this.
- **Quality = degree factor** (Partial 0.6 / Success 1.0 / Overwhelming 1.5) — replaces crit-doubles-weapon-mod.
- One calibration constant (`DMG_SCALE`) anchors an even Success hit ≈ 1 WI. The `DMG_SCALE` + resistance grid are tunable calibration.
- **Status:** ratified. The wound model (WI/MW/Health) is **unchanged**.

## Supersessions (flagged; prose-propagation pending)
- **Replaces** the canonical damage formula `net + STR×mult + weapon_armour_mod` and the **STR multiplier lookup** (×1/×1.5/×2/×3) — combat_v30 §5 / §3.3c prose to be updated.
- **Subsumes W1/W5**: the weapon-vs-armour **+mod table** (W1 blunt taper, W5 point-gap row — both ratified earlier this session) is superseded **in form** by the **Coupling** — which **reproduces the same relationships** (cut→0 vs plate, blunt high, point via gaps, thrust beats mail). The *relationships* are preserved; the *mechanism* unifies (one coupling, no separate +mod, no double-counting of armour). Not a reversal — a refinement Jordan directed.
- **Replaces** crit-doubles-weapon-mod → the Quality factor.

## Pending follow-through (canon-prose propagation — batched)
combat_v30 §5/§3.3c damage formula + the W1/W5 table → Coupling note; struck multipliers; the armour σ-tempo (A1) and material/coverage axes (A2). All ratified-but-unpropagated armature items remain a single pending prose-propagation batch (kept separate to avoid rushed large-file edits).
