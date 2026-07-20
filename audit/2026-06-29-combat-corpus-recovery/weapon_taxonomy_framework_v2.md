# Weapon Taxonomy & Tradition Framework — v2 (consolidated, post-adversarial-review)
**Class-C proposal · OPEN · Jordan-vetoable · 2026-06-12 · supersedes v1**

`[SELF-AUTHORED — bias risk]` This is my own v1 framework after an adversarial pass against the engine code. **Two of v1's three new ideas did not survive as specified.** This version keeps what is grounded, cuts what duplicates the engine, and flags the remaining decisions for you. Leaner than v1 on purpose — the review found v1 over-built.

---

## §0 — Verdict: what changed from v1, and why (the review in one place)

| v1 claim | Survives? | Grounded reason |
|---|---|---|
| Taxonomy axes **head · length · grip** | ✅ **keep** | Already in `weapon_axes_v2` + `combatant.py`; solid, no change |
| **"Balance" axis** (consume `pob_frac`) | ⚠️ **demoted / at risk** | (1) name collides with the live `balance` *tradition channel* (FoV/geometry) **and** the `poise` state (kuzushi) — triple-overload; (2) its "impact" consequence is **already computed** by `geometry.py:49` from **mass + lever-arm**, not `pob_frac`; (3) `pob_frac` is likely **derivable** from `mass`+`head_len`+`grip_len`. Keep **only** if it earns a consequence nothing else computes (recovery-exposure); else cut |
| Two-layer **base × weapon-tradition** class model | ❌ **does not survive** | `tradition` is a **single flat slot** (`combatant.py: self.tradition`), no composition; and the **8 live traditions already encode weapon-affinity** in their channel-vectors — a separate weapon-tradition layer **duplicates** them |
| "F2 revives dead **mass + pob_frac**" | ◐ **half-wrong** | `mass` is **not** dead — `geometry.py` consumes it for percussion. **Only `pob_frac`** is dead |

The net correction: the taxonomy is fine; the *new mechanism* I proposed (a balance axis + a weapon-tradition layer) was mostly **already present in the engine or redundant with it.** The real F2 work is **wiring the inert channel levers**, not adding structure.

---

## §1 — The taxonomy (survived axes + one demoted)

| Axis | Values | Field | Drives | Status |
|---|---|---|---|---|
| **Head type** | point · cut-thrust · straight-cut · curved-cut · blunt | `head` | armour interaction, bind, cut↔thrust | ✅ live |
| **Length** | short <2 · med 2–3.5 · long 3.5–5 · polearm >5 (`head_len`+`grip_len`); binary `reach` is the coarse live form | `reach` (+ lengths) | measure, reach-TN, **grid squares threatened (F1)** | ✅ refine |
| **Grip** | 1H / 2H · off-hand slot · grip-state (normal/choke/lunge) · half-sword re-vector | `hands`, `grip` | bind leverage, off-hand loadout, armour-thrust | ✅ live |
| **Mass** *(supporting)* | light / heavy | `wt`/`mass` | STR-mult, speed, **percussion (LIVE via geometry)**, **F7 cap input** | ✅ live |
| speed · handling | scalar · Forgiving/Standard/Demanding | `spd`·`hand` | tempo · skill curve | ✅ live |
| **PoB / heft** *(renamed from "balance"; OPEN)* | hilt ≤.15 · neutral .15–.35 · head-heavy >.35 | `pob_frac` *(dead)* | **candidate: recovery-exposure after a committed attack** (head-heavy = slow recover = exposed next tick) — a consequence nothing currently owns | ⚠️ **keep-or-cut, your call** |

**The PoB decision (§6).** Its only non-redundant justification is *recovery-exposure*: `geometry.py` already derives impact from mass+lever, `speed` owns tempo-to-act, `poise` owns kuzushi — but "how exposed are you in the tick after you commit" is unowned, and it connects to F1 (flank vulnerability) and F5 (the commit/exposure model). If you want that mechanic, PoB earns its place (renamed, to clear the collision). If not, **cut it** — mass+lever cover impact and `pob_frac` is derivable.

---

## §2 — Roster (infill unchanged; PoB column marked provisional)

Live (✓) + expressible-but-not-instantiated (○). `PoB` shown only as the `pob_frac` value — **meaningful only if §1 keeps the axis.**

| Weapon | head | PoB | length | grip | mass | Best-fit historical |
|---|---|---|---|---|---|---|
| ✓ Rapier | point | .10 | 3.8 long | 1H+offhand | 1.3 | Italian/Spanish rapier |
| ✓ Arming sword | cut-thrust | .12 | 3.2 med | 1H+offhand | 1.2 | period workhorse |
| ✓ Longsword | cut-thrust | .14 | 4.4 long | 2H | 1.4 | German/Italian longsword |
| ✓ Greatsword | straight-cut | .22 | 5.4 polearm | 2H | 2.7 | *Zweihänder* |
| ✓ Sabre | curved-cut | .18 | 3.3 med | 1H+offhand | 0.9 | szabla/talwar/dao/katana |
| ✓ Dagger | cut-thrust | .25 | 1.1 short | 1H+offhand | 0.3 | Fiore/German dagger |
| ✓ Paired short | cut-thrust | .22 | 1.9 short | 1H×2 | 0.7 | FMA *doble baston* |
| ✓ Spear | point | .42 | 6.7 polearm | 2H | 2.0 | *qiang*/*yari* (richest) |
| ✓ Staff | blunt | .05 | 5.6 polearm | 2H | 1.5 | *gùn*/*bō* |
| ✓ Mace | blunt | .60 | 2.5 med | 1H | 1.2 | levy mace |
| ✓ Poleaxe | blunt | .45 | 4.4 long | 2H | 2.5 | poleaxe corpus |
| ○ estoc · sidesword · messer · curved-2H | (expressible; content call) | | | | | |

Census shape (carried): universals = spear/sabre/staff/longsword; niche = rapier/paired/heavy-blunt. Documented gap = **short-blunt**. Folklore red-flags (bare-mace art, field flail, "Kali" mother-art, Bodhidharma, *gada* lineage) — do not encode.

---

## §3 — Weapon↔tradition: do NOT add a layer; wire what exists

**The reconciled answer to F2's "≥2 weapon-traditions that inform weapon-type use":** the engine already has it. The 8 live traditions are cognitive+weapon bundles whose channel-vectors favour a weapon-type's signature channels:

| Live tradition | Channel signature | Weapon-type it already favours |
|---|---|---|
| `german` | tactile 1.35 · leverage 1.30 | the bind → longsword / cut-thrust |
| `italian` | tempo 1.30 · measure 1.25 | tempo-thrust → rapier / point |
| `spanish` | measure 1.35 · balance 1.30 | geometry → rapier / point |
| `chinese` | leverage 1.15 · measure 1.20 | reach-thrust → spear |
| `filipino` | tactile 1.25 · balance 1.25 | flow → paired short |
| `japanese` | precommit 1.35 | intent-read → curved-cut |

Weapon-affinity is **emergent** from `channel-vector × weapon-axis-vector` — exactly the mapping's model. **No new structure needed.**

**The actual blocker (= the F2 dead-lever finding).** The channel levers (`measure`/`tempo`/`leverage`/`visual`/`tactile`/`precommit`/`balance`) are *"registered but INERT until the channel-weight sites are routed through `eff_cw()` (~21 sites)."* Until that wiring lands, the weapon-affinity above **does not fire**. Wiring `eff_cw` is the F2 work — and it is the **same plumbing as F4** (the σ-leverage of a tradition only becomes real once `eff_cw` routes the channel weights through the σ engine).

**"More classes / specialization"** → this is the **D-α decision**, now with a third option the review surfaced:
- **Option 1 — keep the live 8 historical traditions** (they already work as bundles; just wire `eff_cw` + tune the vectors so each has a clear weapon-type). *Lowest apparatus; strongest historical grounding.* **[surfaced by review]**
- **Option 2 — replace with the synthesis's 6 Valoria-native cognitive traditions** (the synthesis's D-α default).
- **Option 3 — coexist** (8+6=14 → fails NERS-E; the synthesis already warned).
- Plus the **familiarity graph** (`ADJACENT`) as within-tradition specialization depth.

Recommendation: **Option 1 or 2, never 3.** Option 1 if you value minimal apparatus + the historical bundles you already have; Option 2 if you want the native re-grounding. **Either way the unblocking work is wiring `eff_cw`, not adding a layer.**

**The orthogonal build-matrix** (cognitive mode × weapon-tradition as *independent* picks — my v1 idea) requires a **second `tradition` slot = an engine change.** Flagged as **optional**: adopt only if you want "how I think" and "what I wield" as separate build axes. Default stays single-slot.

---

## §4 — Naming collision (register it — J-2/J-30 class)

"balance" is overloaded **three** ways: the tradition **`balance` channel** (FoV/geometry), the **`poise` state** (kuzushi), and the proposed weapon axis. Disambiguation: weapon axis → **PoB / heft**; keep channel = `balance`, state = `poise`. This belongs in the naming-collision register, not silently resolved.

---

## §5 — Corrected connections to the other rulings

- **F5 (wounds):** `mass` is **already live** (geometry) — no revival. Only `pob_frac` is dead; if §1 keeps PoB-as-recovery, that revives it. Synergy: a wounded fighter recovering slower means **F5's wound model and PoB could share the recovery channel** (wounds + head-heavy weapon both raise recovery-exposure).
- **F7 (cap):** reads **live `mass`** (already on the geometry percussion path) — F7 only adds Strength-scaling to the existing mass→impact path; no new data.
- **F4 (σ-leverage):** wiring `eff_cw` is where tradition channel-weights enter the σ engine — **F4 correctness and the F2 lever-wiring are the same ~21-site pass.** Do them together.
- **F1 (grid):** facing already has a home — the **`balance` channel = FoV/geometry**; grid facing extends it. PoB-recovery (if kept) feeds flank vulnerability.

---

## §6 — What remains yours

1. **D-α** — keep-the-8 (Opt 1) / replace-with-6 (Opt 2) / coexist (Opt 3, not advised).
2. **PoB / heft** — keep it (with recovery-exposure) or cut it (mass+lever already cover impact).
3. **The orthogonal second tradition-slot** — engine extension, y/n.
4. **D-δ** in-world naming/cultures (creative — yours).
5. **D-γ** `grade='V'` for any genuinely new ability lever.
6. **Short-blunt** weapon class — add or leave to the mace.

---

## Citations
- `combat_engine_v1/tradition.py` — the 8 live traditions, the 7 channels (incl. `balance`=FoV), the **inert channel levers / `eff_cw` pending note**, `familiarity`/`ADJACENT`.
- `combat_engine_v1/geometry.py:49` — percussion from **mass + lever-arm**; `pob_frac` **unused**.
- `combat_engine_v1/combatant.py` — single `self.tradition` slot, `self.poise`, weapon vectors (`mass`/`pob_frac`/`head_len`/`grip_len`).
- `combat_engine_v1/ability_armature.md` — modulate-not-unlock (§1.1), source-tier gate (§1.5).
- `weapon_axes_v2.md` — the six-axis substrate + reclassification.
- `martial_traditions_mapping.md` / `_synthesis.md` — weapon census, per-weapon historical attestation, the 6 native cognitive traditions, `grade='V'`.

`[CONFIDENCE: high — every cut/demotion is grounded in the consuming code read this session (geometry.py percussion path; tradition.py single-slot + inert levers), not in preference.]`
`[CORRECTION: stage v1 — balance axis demoted to PoB/keep-or-cut; two-layer class model withdrawn (engine has one slot); "mass dead" struck (geometry consumes it).]`
