# Weapon Axes v2 — Curvature + One/Two-Handed (Revised Substrate)

**Status:** Class-C **proposal**, Jordan-vetoable. Per Jordan directive 2026-05-29 ("add curvature and one/two handed"). Built **bottom-up** from the current `m3` axis substrate + the ratified σ-leverage channels, and **top-down** from the project's historical research (`combat-manuals-seven-axes-throughlines.md`, `manual-vs-combat-v32-bridge.md`, `blunt-weapon-martial-traditions-completed.md`). No canon edited except the flagged armour-table extension (§4), which is a proposal like the W1 taper.

`[CONFIDENCE: high — both gaps are named in the bridge doc; every mechanical consequence wires to an already-ratified channel; encoding choice (one refined axis + one new axis) is mine, vetoable.]`

---

## §1 — The two additions, and how they're encoded elegantly

Jordan directed two new distinctions. The naive build adds two literal axes (curvature, cut/thrust) on top of `hands` — six categorical axes, an Elegance problem. The cleaner build:

- **`hands` (NEW axis): one-handed (1H) / two-handed (2H).** This also *fixes a hidden role-conflation* — the current `weight` axis was silently carrying handedness (the longsword is "heavy" partly because it's two-handed). Splitting `hands` out returns `weight` to meaning *mass*.
- **`head` (REFINED `type`): point / cut-and-thrust / straight-cut / curved-cut / blunt.** This single axis absorbs three things at once — the old `type` (blade vs blunt), **curvature** (curved-cut is its own explicit value, distinct from straight-cut — Jordan's call honoured), and **cut↔thrust attack-mode** (point → cut-and-thrust → cut). One axis, five intuitive values, instead of three separate axes.

Net: **one new axis (`hands`) and one refinement (`type`→`head`)** — not a six-axis explosion. Curvature is explicit; cut/thrust (the load-bearing armour mechanic) is captured; blunt stays cleanly separate (curvature/cut-thrust don't apply to it).

## §2 — The revised axis set

| Axis | Values | Drives |
|---|---|---|
| reach | short / long | measure; phase-dependent reach (R9) |
| weight | light / heavy | **mass** → STR-mult, speed, STR-min *(de-conflated)* |
| **hands** *(new)* | 1H / 2H | bind leverage (Strength) + off-hand slot + grip-reach |
| **head** *(refined)* | point / cut-and-thrust / straight-cut / curved-cut / blunt | armour interaction, tempo, bind behaviour |
| speed | scalar (−0.5 … 3) | tempo channel (unchanged) |
| handling | Forgiving / Standard / Demanding | skill curve (unchanged) |

## §3 — Mechanical consequence of each new value (wired to ratified channels)

**`hands`** — both consequences map to things already ratified (ST1 Strength bind; the Grip loadout slot):
- **2H** → **+ Strength bind-win δσ** (more leverage in the bind — the German *Stark/Schwach* + *Winden* mechanic), **+ reach** (longer grip/lever), **− no off-hand slot** (both hands committed).
- **1H** → **opens the off-hand slot** (dagger / buckler / shield — the Spanish *daga de mano izquierda*, the I.33 sword-and-buckler), **− less bind leverage**.

**`head`** — drives the armour interaction (the gap the current table misses — all light blades currently share one armour row) and the bind/tempo bias:
- **point** (rapier, estoc, spear-tip): **+ modest vs-armour** (finds gaps — *not* armour-defeating; the heavy-blunt stays the true plate-breaker), **+ reach on the approach/lunge**, **− weak in the bind** (a thrust is poor once bound).
- **cut-and-thrust** (arming sword, longsword, sidesword): **balanced** — the versatile generalist; no armour edge, no bind weakness.
- **straight-cut** (messer, falchion, greatsword): **+ percussive cut**, **+ strong in the close/bind**, **− poor thrust**, **− degrades vs armour**.
- **curved-cut** (sabre, katana, talwar): **+ draw-cut** (best cut vs unarmoured — the curve slices on the pass), **+ recovery/flow** (fast follow-cuts → tempo; the moulinet, the Filipino *Continuous-flow* identity), **− poor thrust**, **− degrades vs armour**.
- **blunt** (mace, hammer, staff): crush — the existing blunt armour mechanics (W1 taper) unchanged.

**The two axes *interact* exactly as history shows:** **half-swording** is a *grip* change (`hands`: a hand moves to the blade) that converts a longsword's **head** behaviour from cut-and-thrust to **point** to punch into armour gaps — the seven-axes doc's "weapon-mode shift that scrambles the categories." The substrate now expresses that move natively.

## §4 — Armour-table extension (canon-touching — flagged for ratification)

The current weapon-vs-armour table (combat_v30 §5) keys on `damage_class` and gives every light blade `+3/+2/+1/+0` (degrades to zero vs heavy). Under `head`, the **point** profile gets a distinct row with a **modest non-zero value vs heavy** (gap-finding), while **cut** profiles keep the degrading row:

| head (light blade) | none | light | medium | heavy |
|---|---|---|---|---|
| point | +3 | +3 | +2 | **+1** (gaps — was +0) |
| cut-and-thrust | +3 | +2 | +1 | +0 (unchanged) |
| straight-cut / curved-cut | +3 | +2 | +1 | +0 (unchanged) |

This is the only canon change here — same status as the W1 taper, awaiting your ratification. It's what makes the thrust a *light weapon's modest answer to armour* (gaps), complementing the heavy-blunt's crush — and it ties into the duel/battlefield split (R10): a point weapon has a thin armour option the pure cut lacks.

## §5 — Weapon reclassification (the canonical roster as axis-vectors)

The old eight named classes become *points in the axis space*; the new axes split the straddles the bridge doc flagged and unlock the homeless weapons.

| Weapon | reach | weight | hands | head | speed | handling | resolves |
|---|---|---|---|---|---|---|---|
| Rapier | long | light | 1H | point | 1.5 | Demanding | (= old `long_thrust_primary`) + off-hand dagger |
| Estoc / tuck | long | light | 1H/2H | point | 1.0 | Standard | NEW — anti-armour needle |
| **Arming sword** | long | light | 1H | cut-and-thrust | 1.5 | Standard | **NEW HOME** (was homeless) + off-hand/shield |
| Sidesword | long | light | 1H | cut-and-thrust | 1.5 | Standard | NEW — civilian companion to arming sword |
| Longsword | long | heavy | 2H | cut-and-thrust | 0.5 | Standard | (= old `long_cut_and_thrust`) — 2H bind leverage |
| Greatsword | long | heavy | 2H | straight-cut | 0.0 | Demanding | NEW — mass + reach, no off-hand |
| Messer / falchion | long | light | 1H | straight-cut | 1.8 | Forgiving | NEW — straight cut, off-hand-capable |
| **Sabre** | long | light | 1H | **curved-cut** | 2.0 | Standard | (= old `curved_cut_primary`) — curvature now explicit |
| Curved two-hander (ōdachi/wodao) | long | heavy | 2H | **curved-cut** | 1.0 | Demanding | **NEW HOME** (was straddling) |
| Dagger / short sword | short | light | 1H | cut-and-thrust | 3.0 | Forgiving | (= old `single_short`) |
| Paired short | short | light | 1H ×2 | cut-and-thrust | 2.5 | Demanding | (= old `paired_short`) — off-hand *is* the weapon |
| Spear | long | light | 2H | point | 0.0 | Forgiving | (= old `long_pole_spear`) — held 2H (1H+shield variant) |
| Staff | long | light | 2H | blunt | 0.0 | Forgiving | (= old `long_pole_staff`) |
| **Mace** | long/short | heavy | **1H** | blunt | 0.0 | Forgiving | splits the old `long_heavy_blunt` — the levy weapon |
| **Poleaxe / war hammer** | long | heavy | **2H** | blunt | −0.5 | Demanding | splits the old `long_heavy_blunt` — the technical plate-breaker |

**`hands` even resolves the `long_heavy_blunt` duality we flagged at ratification:** the **bare mace** (1H, Forgiving, levy weapon) and the **poleaxe/war-hammer** (2H, Demanding, technical, grappling-heavy) are now *distinct axis-vectors*, not one fused class — exactly the duel-vs-battlefield split, now structural.

## §6 — What it resolves (every straddle the research named)

- **Arming sword / sidesword** — was "neither curved nor heavy two-hander," homeless. Now: 1H cut-and-thrust. ✓
- **Curved two-handers** (ōdachi, wodao) — were straddling heavy-cut and light-curved. Now: 2H curved-cut. ✓
- **Rapier vs sabre** — were both "light blade," distinguished only by a speed number. Now mechanically distinct: point (armour-gaps, lunge, weak-bind) vs curved-cut (draw-cut, flow, no armour). ✓
- **Mace vs poleaxe** — were one fused `long_heavy_blunt`. Now 1H vs 2H. ✓
- **The off-hand game** (sword-and-dagger, sword-and-buckler) — was inexpressible. Now: any 1H weapon opens the off-hand slot. ✓

## §7 — Elegance guard (held)

- Added **one** axis (`hands`) and **refined one** (`type`→`head`). Not six axes.
- The axes are **modifiers**, not a mandate to enumerate all combos (5 heads × 2 hands × 2 reach × 2 weight = 40 cells, but only ~15 are real weapons; the rest are never instantiated). Elegance is in the *substrate*, expressiveness in the *instantiation*.
- Excluded-by-nature combos confirm the encoding is tight: no curved-point (curved blades thrust poorly); blunt ignores curvature/cut-thrust.

## §8 — What remains yours (contract)

1. **Ratify the armour-table extension** (§4 — the point-vs-armour row). Canon-touching.
2. **Which new weapons to instantiate** — estoc, sidesword, greatsword, messer, curved two-hander, and the mace/poleaxe split are now *expressible*; which become actual game weapons is a content call.
3. **In-world naming** — these are the historical/mechanical archetypes; the Valorian weapon names and cultural attributions are your creative layer.

`[ASSUMPTION: I included the cut↔thrust attack-mode (folded into `head`) alongside curvature, because curvature alone can't separate the rapier (thrust) from the arming sword (cut-and-thrust) — both straight — and cut/thrust is what carries the armour interaction. Flag if you want `head` reduced to a pure curvature flag instead.]`
`[GAP: short/one-handed blunt class still open — the mace (1H blunt) now partly fills it, but the dedicated short-blunt arts (shillelagh/canne/tonfa) remain a thin, separate gap; your call whether to add a short-blunt weapon beyond the mace.]`
