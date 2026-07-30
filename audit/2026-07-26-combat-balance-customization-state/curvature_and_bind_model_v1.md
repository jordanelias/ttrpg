# Curvature, the thrust, and the bind — design specification v1

## Status: PROPOSED (Jordan-grounded 2026-07-29; channel 1 EXECUTED as ED-PC-0051, channels 2–5 NOT BUILT)

Captures Jordan's live design direction of 2026-07-29 on cutting weapons, together with the
measurements taken against it the same session. Written because the direction arrived in conversation
and this repo's recurring failure is a ruling that never reaches disk (CLAUDE.md §1/§2).

**Everything numeric below was measured, not asserted.** Instruments: `workbench/balance.py`,
`workbench/armour_participation.py`, and the carry-context field harness described in §1.

---

## §0 Jordan's direction, verbatim

1. *"unwieldy weapons like pikes or heavy weapons like warhammers etc fare poorly in duels as they are
   intended for other uses"*
2. *"all weapons and armour allowed on battlefield"* · *"medium and heavy armour not allowed inside
   settlements UNLESS a soldier/troop"* · *"polearms, blunt weapons or two-handed swords [not] allowed
   inside settlements UNLESS a soldier/troop, i.e. public spaces inside settlements, religious spaces,
   parliamentary spaces, etc allow none or light armour and allow arming swords/rapiers/daggers etc
   that are one-handed"*
3. *"cutters need to be excellent in contexts where they can CUT ie unarmoured and light armour. the
   curve does two things: (1) it extends the amount of cutting edge with which to do damage, and (2) it
   allows for faster recovery because the weapon isn't getting 'stuck' the same way a straightened
   weapon would"*
4. *"they can still thrust and pierce with the point of their weapons, but the benefit for the curve is
   that their thrust ALSO can cut because of how the weapon is shaped… the piercing area of a curved
   weapon isn't based upon the point of the blade but also how much of a curve gets invited in"* ·
   *"it's because a curved weapon's thrust isn't on an axis perpendicular to the swing; the thrust
   itself also includes cutting the way a swing does"*
5. *"the shamshir can still thrust and penetrate though. it just takes more precision and manipulation
   to do it. if there's a genuine POINT, which all these swords have, then it can thrust and puncture"*
   · *"i don't think you evaluated the tip of these curved swords correctly. they don't just…keep
   curving or curl."*
6. *"when it comes to parrying and blocking and binds and winds etc where weapons connect with one
   another… the lighter the weapon is, the easier it is to move away due to momentum. so while the
   rapier can react very quickly, wouldn't this make it a lot easier for an opponent with a heavier
   weapon — say a scimitar — or some other cutting weapon indicate that they would have an advantage in
   those weapon-to-weapon collision/reorienting scenarios due to weight/momentum/heft/leverage?"*

Also ruled, for the deferred half of (1): duels are gated by **legality for now**, but the eventual
target is **team-based grid tactical battles (Final Fantasy Tactics-shaped)** with per-attack
mini-resolutions, where sword-vs-spear must read correctly on a grid.

---

## §1 The carry ruling — measured, and it does NOT do what the proposal claimed

Legality derives entirely from **already-stored primitives** (`head_len + grip_len`, `hands`, `head`).
No new per-weapon data, and the threshold is not hand-placed: the roster self-separates with a
**0.30 m empty gap** (civilian tops at goedendag 1.20 m; the next weapon up is sparr_axe at 1.50 m).

**Divergence from `proposals/…-personal-combat-player-agency-and-tradition-curriculum.md` §12**, which
drafted the rule as length + hands only: Jordan bars **blunt** explicitly, which excludes the mace
(0.75 m, 1H) that §12's formula would have admitted. **Jordan's ruling governs.**

Settlement-legal set (18): dagger, rondel, stiletto, main_gauche, misericorde, paired_short, cinquedea,
hook_sword, tsurugi, jian, arming, pulwar, sabre, shamshir, falchion, szabla, scimitar, rapier.

### 1.1 ⚠ §12.1's central claim is FALSIFIED

§12.1 asserts carry context *"removes the entire D1 dominance problem from every civilian context
without touching a single constant."* Measured — each weapon vs the field of what else is legal there,
position-swapped, n=400/weapon:

| context | legal weapons | spread | range |
|---|---|---|---|
| battlefield | 51 | 21.4% – 73.5% | 52.1 pp |
| settlement civilian | 18 | 18.2% – 85.0% | **66.8 pp — LARGER** |
| civilian sidearms only (off-hand artifacts excluded) | 10 | 35.5% – 80.6% | 45.1 pp |

Carry context **relocates** the dominance problem one scale down (rapier over shorter swords) rather
than removing it. The battlefield field is almost perfectly rank-ordered by length: every 2H weapon
≥1.50 m is above 50%, nearly every 1H sidearm below 46%.

### 1.2 Legality delivers (1) by EXCLUSION only, not by performance

With war weapons present under civilian armour (lawless town, ambush, unregulated duel) reach
dominance is **worse** than on the battlefield — spread **10.0% – 88.0%, 78 pp**, guandao (2.40 m) at
88.0%, and the top 14 all ≥1.57 m two-handers. Armour no longer offsets reach.

**So the ruling is a content/legality mechanism, not a balance fix.** Per Jordan it is accepted as
such for now; the performance half routes to the grid layer (§5).

### 1.3 It CONFIRMS §12.5's own prediction

§12.5 predicted carry context makes A7a *more* urgent. Confirmed: the curved cutters are the bottom of
the only field they exist for — sabre 38.2%, pulwar 35.5%, shamshir 41.5% — against rapier 80.6%.
That is what promoted A7a to the next batch.

---

## §2 Channel 1 — extended cutting edge → damage. **EXECUTED (ED-PC-0051)**

Jordan (3)(1). **Already derived and then discarded:**
`geometry.cut_factor = edge_keenness × (1 + 0.45·tanh(2·curvature))` — the curve already adds up to
+45% — and `core.coupling` threw it away, because it scaled only the bare `'cut'` token, which
core.py's own comment says "is NEVER a weapon's own native head." 16 weapons (31% of roster) coupled
identically regardless of edge, and `min(1.0, eff/CUT_AUTH_REF=0.70)` was identically **1.000** across
the native population (0.710–1.330), so the defect register's own proposed fix was a **no-op**.

Shipped: a second reference `CUT_REF_NATIVE = 1.00` (katana-anchored, following the module's
named-weapon precedent), non-saturating so a superior edge is a *benefit*; the benefit gated on
`_transmit('shear', mat)` normalised (none 1.000 / cloth 0.618 / mail 0.277 / plate 0.193) per Jordan's
"excellent where they can CUT"; the penalty ungated, because a poor edge is poor everywhere.

**Measured effect on the civilian sidearm field** — correct direction, insufficient magnitude:
scimitar +6.1, pulwar +4.7, shamshir +2.8, sabre +2.3; falchion −5.2, arming −1.9. Spread 45.1 →
**40.6 pp**. **The rapier is untouched at 80.8% and remains a 26 pp outlier — it is a POINT weapon, so
cut grading cannot reach it.** A7a was a real defect and is fixed; it is *not* the cause of the rapier
problem. That lives in §3 and §4.

**Disclosed, not tuned:** the penalty side flips two selections at `none` — greatsword (eff 0.80) and
hook_sword (eff 0.71), the two lowest native cut effs, now prefer their point unarmoured. A greatsword
preferring the point unarmoured is questionable feel and is **Jordan's call**; it is a consequence of
the katana anchor de-rating everything beneath it.

---

## §3 Channel 2 — the curve does not stick → faster recovery. **NOT BUILT**

Jordan (3)(2). **There is no consumer of "sticking" anywhere in the engine** — grep for
stuck/stick/bind_on_cut/extraction over `combat_systems.py`, `weapon_physics.py`, `core.py` returns
nothing. `curvature` has exactly **one** runtime consumer, `arrest_impulse`, where it *reduces*
braceability (a cost).

Home: the recovery path (`recoverability_factor` / `weapon_tempo`), keyed on `geo['curvature']`, behind
its own `[SIM-CALIBRATE]` constant. **New mechanic — needs its own batch and its own guard.**

---

## §4 Channels 3–4 — the curved thrust. **NOT BUILT, and the defect is DATA, not formula**

Jordan (4) and (5). Two claims: a curved thrust also *cuts* (the thrust axis is not perpendicular to
the swing axis), and a genuine point *can* still puncture — it just needs more precision and
manipulation.

### 4.1 The finding: curvature penalises the thrust TWICE

`thrust_factor = point_concentration × (0.55 + 0.45·cross_section) × (1 − 0.6·curvature)`.

Measured across 42 bladed weapons: **corr(curvature, point_concentration) = −0.729.** The stored tip
data was authored largely *as a function of* blade curvature — and then the formula applies a curvature
penalty **again**. That is a double-count, exactly the class the R3 consolidation ruling forbids ("one
channel per edge-effect… drop the double-counts").

The shamshir is the extreme: **`point_concentration = 0.08`**, below **sparr_axe's 0.10 — an axe**.
Its collapse to `thrust 0.03` is overwhelmingly the *data* (base 0.059), not the curve term (0.58). A
shamshir has a genuine, needle-like point. Jordan's *"they don't just keep curving or curl"* is exactly
this: the tip was encoded as though the blade curls through it.

**The roster contains its own counter-example:** `szabla`, curvature 0.30 / pc **0.60** — a curved
sword with a proper point, correctly encoded. It is the template for the correction.

### 4.2 What the fix is

1. **Data correction**: `point_concentration` is a *tip* property and must be independent of *blade*
   curvature. Re-author the curved family's tips against the szabla pattern. Roster-wide golden
   re-record; the *values* are a Jordan design call.
2. **De-double-count**: with tips corrected, `thrust_factor`'s `(1 − 0.6·curvature)` term is either
   removed or re-grounded as the *alignment/precision* cost Jordan describes — which makes it
   **skill-conditioned**, not flat geometry, consistent with the governing principle that efficacy
   comes from investment rather than category.
3. **Thrust-carries-cut**: the puncture arm of a curved blade gains a curvature-weighted shear
   component. Derivable from `curvature` alone — no new stored data.

⚠ **Interaction with ED-PC-0050 (E3b), which shipped hours earlier.** E3b split `heft` on the resolved
arm, shear **or** puncture, via `cut_thrust_arm`'s binary `max()`. Jordan's (4) says those arms are not
cleanly separable for a curved blade. Note the two quantities decouple: the *motion* is axial (so the
axial `THRUST_POB` lever is right) while the *wound mode* is partly shear. **Do not extend the binary
split further until this is resolved** — see ED-PC-0050's own disclosed selection-vs-damage residue,
which is the same seam.

---

## §5 Channel 5 — mass/momentum in the bind. **NOT BUILT. Strongest lead on the rapier outlier**

Jordan (6). **The bind has no mass, momentum or inertia term at all:**
`bind_sigma = lev + catch + tac + strq + spine + wound`, where the only physical lever is
`leverage() = grip_len − K·head_len` — **pure geometry**.

Measured, and it refines Jordan's example rather than simply confirming it:

| | rapier | scimitar | shamshir |
|---|---|---|---|
| mass (kg) | **1.37** | 0.95 | 0.77 |
| MoI | 0.1578 | 0.1517 | 0.1026 |
| **static_moment** | **0.1231** | **0.2199** | 0.1631 |
| `leverage()` | −0.0792 | −0.0041 | +0.0180 |
| `blade_guard` → `catch` vs rapier | 0.54 | 0.18 (**+0.197** to rapier) | 0.16 (**+0.208**) |

**The rapier is the HEAVIER weapon** — so the mechanism cannot key on weight. It must key on the
**moment about the hand**: the scimitar's `static_moment` is **1.8× the rapier's**, because the
rapier's mass sits in hilt and pommel (which is also why its `PoB_frac` is tiny and its agility high).
A rapier is heavy but hand-balanced — quick to move, and *cheap for an opponent to displace at the
blade*, which is precisely Jordan's mechanism stated in the right variable.

And the rapier's bind advantage is currently **the hilt**: `leverage()` already puts it slightly
behind, but `catch` (+0.197 from the swept hilt, historically legitimate) more than cancels it, with no
mass-moment counterweight anywhere.

**Home:** a new additive `bind_sigma` term on `static_moment` (or `at_grip`'s `S_g`) differential,
`[SIM-CALIBRATE]`, its own ablatable primitive — **not** multiplied into `leverage()`, per §2.3's
one-primitive-per-effect rule. Expected direction: scimitar/shamshir gain in the bind against the
rapier, which is the missing counterweight to its hilt.

---

## §6 Sequencing

| # | channel | status | blocked on |
|---|---|---|---|
| 1 | native edge grading (§2) | **DONE**, ED-PC-0051 | — (greatsword flip awaits Jordan) |
| 5 | bind mass-moment (§5) | next | nothing — clean additive primitive, strongest lead on the rapier |
| 3–4 | curved thrust (§4) | after 5 | tip-data *values* are Jordan's; interacts with ED-PC-0050 |
| 2 | curve recovery (§3) | last | new mechanic, needs grounding + constant |
| — | carry-context primitive | cross-lane | home is IN/Jordan (§12.4); PC can stub it |
| — | grid tactical layer | future | subsumes most of (1)'s performance half — see §5 note below |

**On the deferred performance half of (1):** on a grid, reach becomes **positional** (attack range in
tiles), which is its natural expression. The σ-layer would then only need to handle "sword closed
inside the spear's point" as an adjacency *state*, not a hidden continuous measure. **This suggests the
closed-phase LEVERAGE/DAMAGE rework the handoff scoped as "a large high-risk change with no bounded
fix" may be the wrong tool, and should NOT be commissioned before the grid layer exists.**
