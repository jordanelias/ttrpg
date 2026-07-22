# Weapon Edge-Geometry Table (edges = {sides, false_edge_frac})

Source: `/home/user/ttrpg/systems/combat/combat_engine_v1/weapons.py` (WEAPONS dict). 51 non-`base`
weapons covered (2 half-sword forms — `longsword_halfsword`, `estoc_halfsword` — skipped per spec,
since they carry a `base` key and are derived forms, not independent morphology).

## ⚠️ Would-violate-invariant-1 conflicts (top-level `geometry.edge_keenness` vs. per-element reality)

For every multi-mode composite, the record's **top-level** `geometry.edge_keenness` is a *blended,
whole-weapon* value baked once at import — it is **not** the right number to gate a `sides=0` call for
an individual element. The correct per-element value is the `mode_elements[i].geometry.edge_keenness`
where one exists. Using the top-level value naively would have produced a **false invariant-1
violation** (assigning `sides=0` to something whose *governing* ek is actually >0.1) or a **missed
opportunity** (refusing `sides=0` to something whose top-level ek looks high but whose own mode ek is
≤0.1) for the following weapons. All calls below use the correct (mode-specific, where present) ek —
flagging here so these aren't mistaken for errors on review:

| Weapon | Element | Top-level ek | Element's own ek | Resolution |
|---|---|---|---|---|
| `poleaxe` | beak/fluke, top spike | 0.5 | 0.00 (each) | used 0.00 → `sides=0` both — top-level would have wrongly blocked this |
| `bec_de_corbin` | curved beak, top spike | 0.25 | 0.00 (each) | used 0.00 → `sides=0` both |
| `lucerne_hammer` | rear fluke, top spike | 0.2 | 0.00 (each) | used 0.00 → `sides=0` both |
| `hook_sword` | crescent_hand_guard_striking_element | 0.6 | 0.05 | used 0.05 → `sides=0` — top-level would have wrongly blocked this |
| `guandao` | rear spike/hook notch | 0.85 | 0.10 | used 0.10 (at threshold, ≤0.1 OK) → `sides=0` |
| `fauchard` | back_hook_spike | 0.85 | 0.05 | used 0.05 → `sides=0` |
| `voulge` | thrusting_heel_spike | 0.8 (top) | 0.15 (mode) | **0.15 > 0.1** — genuinely blocks `sides=0` despite the "spike" name; assigned `sides=2` instead, see row below |

**Genuine data-gap forced calls** (no per-element geometry exists at all — the element inherits the
single whole-weapon `geometry.edge_keenness`, which is >0.1, so `sides=0` is unavailable even though the
physical part (a thin catch-tine/wing/fluke) is plausibly closer to edgeless in reality). Flagging these
as low-confidence (S3) rather than silently picking a side:
- `dangpa` flank_tine_left/right (inherit top ek=0.3)
- `ranseur` — N/A, only one listed element (wings are guards-only, not in `elements[]`, no row needed)
- `spetum` left/right side prong-wing (inherit top ek=0.55)
- `partisan` left/right wing-lug (inherit top ek=0.7)
- `voulge` rear_fluke (no mode_element authored for it — 2 of voulge's 3 elements have mode_elements,
  this one doesn't — inherits top ek=0.8)

No weapon in the roster has a genuine, unresolvable invariant-1 conflict in the final table below —
every `sides=0` row cites an ek ≤0.1 at the granularity actually used.

---

## Table

| weapon | element | sides | false_edge_frac | S-grade | justification |
|---|---|---|---|---|---|
| rapier | blade (thrusting, narrow) | 2 | 0.0 | S1 | Rapiers were double-edged by construction (even late "true" thrusting rapiers kept both edges ground, just thin); ek=0.3 reflects thrust-dominant use, not edge count. |
| arming | blade | 2 | 0.0 | S1 | Standard knightly arming sword — double-edged is the archetypal Oakeshott form. |
| longsword | blade | 2 | 0.0 | S1 | Longsword canon double-edged (Fiore/Liechtenauer corpus). |
| greatsword | blade | 2 | 0.0 | S1 | Two-handed greatswords (Zweihänder-class) are double-edged along the cutting length. |
| sabre | blade | 1 | 0.2 | S1 | Military sabre: single edge with a clipped false edge (~1/5 of blade) near the point for the back-cut/draw-cut. |
| dagger | blade | 2 | 0.0 | S1 | "Dagger" is definitionally double-edged in period/typological usage (vs. single-edge "knife"). |
| paired_short | blade (×2, matched) | 2 | 0.0 | S2 | **FLAG (JD-2):** near-zero curvature (0.05) + `head=cut_thrust` reads as a straight double-edged short-sword pairing (European short-sword duo), not a curved single-edge dao-pair; a curved single-edge hudiedao/dao-pair reading is the live counter-interpretation and would flip this to sides=1. |
| spear | spearhead (leaf-shaped socketed) | 2 | 0.0 | S1 | European leaf-shaped spearheads are routinely edged on both sides for slashing as well as thrusting (attested archaeologically and in period fencing texts). |
| staff | working tip | — (omit) | — | S1 | Bare wood tip, mass_kg=0, ek=0.0 — no striking edge; blunt, omit `edges` key entirely. |
| mace | flanged head | — (omit) | — | S1 | Solid steel/iron flanged blunt head, ek=0.0 — no edge; omit `edges` key. |
| poleaxe | hammer face | — (omit) | — | S1 | Blunt striking face (mode ek=0.00); omit `edges` key. |
| poleaxe | beak/fluke | 0 | 0.0 | S1 | Curved rear hook/spike, mode ek=0.00 — edgeless hooking point, not a blade. |
| poleaxe | top spike | 0 | 0.0 | S1 | Langet-mounted thrusting point, mode ek=0.00 — edgeless spike. |
| yari | main_point (spearhead) | 2 | 0.0 | S2 | **FLAG (JD-2):** ek=0.32 (>0.1) rules out an edgeless read for *this* record; su-yari/sasaho-yari heads are commonly forged with two ground edges (functionally a straight short-sword blade on a shaft), supporting `sides=2`. Counter-case: a pure ryō-shinogi (diamond-section, near-symmetric, minimally-edged) thrust-only yari variant exists historically and would be closer to edgeless — not what this record's ek models. |
| kama_yari | main_point | 2 | 0.0 | S2 | Mode ek=0.32, same reasoning as `yari`'s main point. |
| kama_yari | cross_blade_left | 1 | 0.0 | S1 | Kama (sickle) blade — single edge ground on the inner (concave) curve, standard kusarigama/kama-yari morphology; mode ek=0.65. |
| kama_yari | cross_blade_right | 1 | 0.0 | S1 | Mirror of cross_blade_left. |
| dangpa | center_prong | 2 | 0.0 | S2 | Korean dangpa (trident) center tine — Muyedobotongji depicts a double-edged straight thrusting blade akin to a short spear point; top-level ek=0.3 (no mode_elements authored for this weapon). |
| dangpa | flank_tine_left | 2 | 0.0 | S3 | **Forced call (data gap):** no per-element geometry exists; inherits top ek=0.3 (>0.1), which rules out the plausibly-more-accurate edgeless-catch-tine reading. Physically these are documented primarily as catch/hook lugs (dual_role_element); assigned thin double edge only to stay ek-compliant. |
| dangpa | flank_tine_right | 2 | 0.0 | S3 | Mirror of flank_tine_left; same forced-call caveat. |
| bear_spear | main_point | 2 | 0.0 | S2 | European boar/bear-spear heads are broad, leaf-shaped, and typically edged on both sides (used to both stab and cut when toggled); top ek=0.5. |
| ranseur | main_point | 2 | 0.0 | S2 | Narrow ranseur point mounted on langets — typically a double-edged thin blade (short-sword-like), consistent with top ek=0.3. Side wing-lugs are guards-only in this record (no `dual_role_element`), not separate `elements[]` entries — no row needed. |
| spetum | central spear point | 2 | 0.0 | S2 | Broad triangular langet-socketed main blade — double-edged, top ek=0.55. |
| spetum | left side prong/wing | 1 | 0.0 | S2 | Forward-curving flange; Fiore/period spetum use documents both catching AND cutting with the wings in the bind, supporting a sharpened leading edge (single edge, unsharpened trailing side against the haft) rather than a pure blunt hook. Ek=0.55 (inherited from top, no mode_elements) rules out edgeless in any case. |
| spetum | right side prong/wing | 1 | 0.0 | S2 | Mirror of left wing. |
| partisan | central ox-tongue blade | 2 | 0.0 | S1 | Broad triangular/leaf ox-tongue blade — canonically double-edged (classic partisan form). |
| partisan | left wing-lug | 1 | 0.0 | S2 | Manciolino documents active trap-and-bind use of the wing-lugs; treated as a single sharpened cutting edge on the forward face, S2 given ek=0.7 (inherited, forces non-edgeless) but the specific single- vs.-blunt call is an inference. |
| partisan | right wing-lug | 1 | 0.0 | S2 | Mirror of left wing-lug. |
| naginata | nagasa (blade) | 1 | 0.15 | S2 | Naginata blade is forged like an oversized katana blade (same tradition), single edge with saki-zori curvature; kissaki-style false edge near the point is a reasonable extension of the katana/tachi/odachi convention (ek=0.85). |
| glaive | blade (leaf-shaped) | 1 | 0.0 | S1 | European glaive — single-edged cleaver-like blade, no false edge in the plain form (as opposed to glaive-guisarme hybrids). |
| guandao | main dao blade | 1 | 0.0 | S1 | Deep reclining-moon crescent dao blade — single edge is the defining dao/guandao feature (mode ek=0.85). |
| guandao | rear spike/hook notch | 0 | 0.0 | S2 | Mode ek=0.10 (at threshold) — documented hooking/catching spine feature at the socket end, not a cutting edge; treated as edgeless per its own authored geometry (guandao's I4/D5 mode_elements addition). |
| podao | dao_blade | 1 | 0.0 | S1 | Single-edged Chinese glaive-sword (podao/zhanmadao family); ek=0.85. |
| fauchard | fauchard_blade | 1 | 0.0 | S1 | Single-edged cleaver-style polearm blade ("composite glaive" typology); mode ek=0.85. |
| fauchard | back_hook_spike | 0 | 0.0 | S2 | Mode ek=0.05 — reverse hooking/thrusting spine spike, not a cutting edge; treated as edgeless per its own I4/D5-authored mode geometry, same pattern as guandao's notch. |
| bardiche | crescent_blade | 1 | 0.0 | S1 | Long crescent single-edge axe-blade — bardiche's defining feature; ek=0.85. |
| sparr_axe | broad_axe_bit | 1 | 0.0 | S1 | Scandinavian broad-axe bit — single edge (axe morphology); ek=0.85. |
| voulge | cleaver_blade | 1 | 0.0 | S1 | Cleaver-style single-edge chopping blade (mode ek=0.80), the voulge's namesake broad blade. |
| voulge | thrusting_heel_spike | 2 | 0.0 | S3 | Mode ek=0.15 — just above the 0.1 edgeless threshold, so `sides=0` is unavailable despite the "spike" name; modeled as a symmetric taper-ground point (two shallow facet edges) rather than a pure round spike. Weak grounding — this is an engine-abstraction feature (voulge+bill hybrid), not a single well-documented historical specimen. |
| voulge | rear_fluke | 1 | 0.0 | S3 | **Forced call (data gap):** no mode_element authored for this element (only cleaver_blade/thrusting_heel_spike have mode_elements); inherits top ek=0.8, ruling out the more plausible edgeless-catch-hook reading (it's documented only as an "incidental hook/catch point", not a blade). Assigned single edge only to stay ek-compliant. |
| guisarme | hooked cutting blade | 1 | 0.0 | S1 | Guisarme derives from a hooked agricultural bill/pruning blade — single edge on the hook's cutting face; mode ek=0.60. |
| guisarme | reverse thrusting spike | 0 | 0.0 | S1 | Mode ek=0.00 — plain thrusting spike, edgeless. |
| ji | straight spearhead | 2 | 0.0 | S2 | Straight ji spearhead — Chinese ji points are typically forged like a straight jian blade (double-edged); mode ek=0.40. |
| ji | perpendicular crescent (yueyadao) blade | 1 | 0.0 | S2 | Moon-tooth (yueyadao) crescent side-blade — single-edged curved cutting blade, the ji's hooking/dismounting feature; mode ek=0.75. |
| bec_de_corbin | hammer face | — (omit) | — | S1 | Blunt striking face, mode ek=0.00; omit `edges`. |
| bec_de_corbin | curved beak | 0 | 0.0 | S1 | Mode ek=0.00 — edgeless hooking beak (armor-piercing/dismounting hook), not a blade. |
| bec_de_corbin | top spike | 0 | 0.0 | S1 | Mode ek=0.00 — edgeless thrusting point. |
| lucerne_hammer | hammer face (4-tine fluke) | — (omit) | — | S1 | Blunt striking/fluked face, mode ek=0.00; omit `edges`. |
| lucerne_hammer | 3-4 tine fluke (rear beak) | 0 | 0.0 | S1 | Mode ek=0.00 — blunt/edgeless fluked rear beak, used to bind/hook not cut. |
| lucerne_hammer | top spike | 0 | 0.0 | S1 | Mode ek=0.00 — edgeless thrusting spike. |
| goedendag | tapering club body | — (omit) | — | S1 | Wooden club shaft, mass_kg=0 within elements, mode ek=0.00; omit `edges`. |
| goedendag | iron spike | 0 | 0.0 | S1 | Tanged iron thrusting point, mode ek=0.00 — edgeless spike. |
| katana | blade (nagasa) | 1 | 0.15 | S1 | Single-edged curved nihonto blade; kissaki false-edge (the sharpened yokote-to-tip zone) is a well-documented ~15% feature of the blade. |
| tachi | blade (nagasa) | 1 | 0.15 | S1 | Same nihonto kissaki false-edge convention as katana; slightly more curvature (0.35). |
| odachi | blade (nagasa) | 1 | 0.15 | S1 | Same nihonto kissaki false-edge convention, scaled up (o-dachi/nodachi class). |
| tsurugi | blade | 2 | 0.0 | S1 | **FLAG (JD-2), counter to "Japanese=single-edge":** chokuto-era tsurugi/ken are straight, pre-curvature, DOUBLE-edged blades (like a Chinese jian or European straight sword) — this predates the differentially-hardened, single-edge nihonto tradition entirely; the record's own material note ("chokuto-era ferrous forging, pre-dating classic differential-hardening nihonto technique") corroborates this. |
| changdao | blade | 1 | 0.1 | S2 | Ming-era Chinese long saber (changdao), single edge, modeled on captured Japanese nodachi/odachi forms encountered during anti-wokou campaigns; a modest false edge near the tip is a plausible carry-over from that lineage, though less firmly attested than the nihonto convention itself. |
| nandao | blade | 1 | 0.0 | S2 | Southern Chinese broad-backed saber (nandao) — single edge (dao family); this is largely a modern wushu competition weapon so false-edge grounding is weak — assigned 0.0 rather than claim an unattested feature. |
| jian | blade | 2 | 0.0 | S1 | Jian is THE archetypal Chinese double-edged straight sword — no dispute here. |
| scimitar | blade | 1 | 0.15 | S2 | Generic curved single-edge sabre (Mamluk/Ottoman-family); a false-edge/yelman flare near the tip (as on the kilij) is a recognized feature of this broad category, though "scimitar" as a catch-all term covers variants without one. |
| pulwar | blade | 1 | 0.0 | S2 | Afghan/Indian curved sabre — single edge; unlike the kilij, pulwar blades are not typically noted for a true yelman/false edge, so left at 0.0. |
| shamshir | blade | 1 | 0.0 | S1 | Persian shamshir — pure curved single edge for the draw-cut, no false edge (highest curvature in the roster, 0.7, consistent with a dedicated slasher). |
| szabla | blade | 1 | 0.2 | S1 | Polish szabla — single edge with the well-documented "pióro" (feather) false edge/back-edge near the point, a hallmark identification feature of the type. |
| cinquedea | blade | 2 | 0.0 | S1 | Italian cinquedea ("five-fingers") — broad, tapering, double-edged short sword/large dagger; double edge is definitional to the type. |
| flamberge | blade (forte-to-mid, flame-ground) | 2 | 0.0 | S1 | Two-handed flamberge/flammard — double-edged wavy blade (German/Swiss tradition); the flame-grinding is cosmetic/vibrational (see edge_undulation), not a change in edge count. |
| flamberge | blade tip (plain distal + Parierhaken zone) | 2 | 0.0 | S1 | Continuation of the same continuous double edge past the wave-ground section (per file docstring: "one continuous edge, no mode_elements"). |
| flamberge | ricasso | — (omit) | — | S1 | Deliberately blunted forward gripping section by design (half-sword grip zone) — not a striking edge; omit `edges` key. (Note: the record carries no per-element geometry distinguishing this from the rest of the blade, so an explicit `sides=0` here would sit awkwardly against the whole-weapon ek=0.8 — omission is the cleaner, spec-sanctioned choice for a non-striking part.) |
| estoc | blade | 0 | 0.0 | S1 | **FLAG (JD-2), confirmed:** the archetypal edgeless armoured thruster — ek=0.05, stiff square/hexagonal cross-section blade meant purely to find gaps in plate, no cutting edge at all. |
| falchion | blade | 1 | 0.2 | S1 | Classic broad cleaver-profile falchion — single edge with a clipped point forming a short false edge (the "cleaver" falchion sub-type), a well-attested feature. |
| rondel | blade | 0 | 0.0 | S1 | Rondel dagger — square/diamond cross-section stiletto-like thrusting spike, essentially no cutting edge (ek=0.05). |
| main_gauche | blade | 2 | 0.0 | S2 | ek=0.3 (>0.1) rules out edgeless; many parrying daggers (main gauche) carry sharpened double edges near the point with a thicker, unsharpened forte near the guard for parrying — modeled as double edge overall. Counter-case: some main gauche were single-edged with a reinforced spine throughout. |
| stiletto | blade | 0 | 0.0 | S1 | Pure thrusting stiletto — triangular/square section, no edge at all (ek=0.02, the lowest in the roster). |
| misericorde | blade | 0 | 0.0 | S1 | "Mercy dagger" — narrow edgeless piercing blade meant to slip through armor gaps/visor slits (ek=0.1, at the threshold). |
| hook_sword | blade_with_hooked_tip | 1 | 0.0 | S2 | Chinese hook sword (gou) — single edge on the outer curve of the main blade; mode ek=0.60. |
| hook_sword | crescent_hand_guard_striking_element | 0 | 0.0 | S2 | Mode ek=0.05 — the crescent moon-guard is used for percussive/hooking blows and trapping, not cutting; treated as edgeless per its own authored (I4/D5) mode geometry. |

---

## Summary of key/flagged calls

- **tsurugi = double-edged (sides=2)** — deliberately counter to the "Japanese swords are single-edged"
  intuition. This is correct: tsurugi/ken are chokuto-era pre-curvature straight blades, forged before
  the differentially-hardened single-edge nihonto tradition existed. The record's own material comment
  corroborates this ("chokuto-era ferrous forging, pre-dating classic differential-hardening").
- **yari = double-edged (sides=2)**, not edgeless — resolved by the record's own ek=0.32 (>0.1 rules
  out edgeless for this specific entry), reinforced by su-yari/sasaho-yari morphology (ground edges on
  a straight socketed head). Flagged that a pure diamond-section ryō-shinogi thrust-only yari variant
  would be the edgeless counter-case, not modeled here.
- **paired_short = double-edged (sides=2)**, called from near-zero curvature (0.05) + `head=cut_thrust`
  reading as a straight European short-sword pair rather than a curved single-edge dao-pair — flagged
  as the live dispute (jian-pair vs. dao-pair) per the brief; lowest-confidence single call in the set (S2).
- **estoc = edgeless (sides=0), confirmed** — ek=0.05, no ambiguity, the archetypal armoured thruster.
- **katana/tachi/odachi kissaki false edge = 0.15** as directed, applied uniformly across the three
  nihonto-family blades; `naginata` extended the same convention (S2, single step removed from a direct
  historical citation since naginata isn't one of the three named blades).
- **falchion clip = 0.2** (matching sabre's clip magnitude) — the "cleaver" falchion sub-type's
  documented clipped point.
- Two composite spike elements sit exactly at or just past the ek=0.1 threshold and needed a
  non-obvious call: `guandao`'s rear hook-notch (ek=0.10, kept edgeless) and `voulge`'s thrusting heel
  spike (ek=0.15, just over — forced to sides=2, weakest-grounded call in the whole table, S3).
- A cluster of catch-lug/wing/tine elements on `dangpa`, `spetum`, `partisan`, and `voulge`'s rear_fluke
  have **no per-element geometry authored at all** and inherit a whole-weapon ek that is comfortably
  >0.1 — meaning an edgeless reading (arguably the more physically honest one for several of these) was
  structurally unavailable under invariant 1. These are flagged as S3 data-gap calls, not confident
  historical assertions, and are good candidates for future per-element `mode_elements` authoring if the
  edge data needs to get more precise.
- Several multi-mode composites (`poleaxe`, `bec_de_corbin`, `lucerne_hammer`, `hook_sword`, `guandao`,
  `fauchard`) have a top-level `geometry.edge_keenness` that would have given the WRONG invariant-1
  answer if applied to an individual point/blunt element instead of that element's own
  `mode_elements[i].geometry.edge_keenness` — documented in the conflicts table at the top of the file
  so this isn't mistaken for an oversight on review.
