# Mode A — Formula Validation: Personal Combat

**Subsystem:** personal_combat · **Target:** `designs/scene/combat_engine_v1/` (CANONICAL per
`references/canonical_sources.yaml` lines 105-111: ratified ED-900/904, re-ratified ED-904; docket
ED-1029). No `params/combat.md` exists (deprecated 2026-06-04 → `deprecated/params/combat.md`); the
canonical parameter source for this subsystem is `designs/scene/combat_engine_v1/config.py`
(`CFG` dict) plus the shared `params/core.md` for cross-subsystem derived stats (Health, Stamina,
Combat Pool, Concentration).

Scope note: `combat_engine_v1` is a large, actively-audited Python package (core.py, systems.py 76KB,
weapon_physics.py, weapons.py 61KB, wrapper.py, contact.py, config.py ~150 tunables). Every constant
in `config.py` already carries an inline provenance tag (`[SIM-CALIBRATE]`, `[FIAT]`, `[ASSERTED]`,
or an ED-PC-NNNN citation) — this is unusually well self-documented for Class-C material. This audit
spot-checked the core resolution chain (pool → roll → degree → damage) and the Health/Wound formula
end-to-end; it does not re-derive every one of the ~150 config constants by hand.

## A1 — Core resolution chain

| ID | Formula | Source | Min Output | Max Output | Issues | Status |
|---|---|---|---|---|---|---|
| A1.1 | `resolution_pool(history) = max(5, round(history)+6)` | `core.py:30-32`; matches `params/core.md:161` (Combat Pool row, ED-901/900/904) | History=1 (attribute floor per `params/core.md:137`) → pool=7 ≥ floor 5 | History=7 (attribute max) → pool=13 | None. Floor prevents any negative/zero-pool state; attribute range 1-7 never drives pool below the floor. | **PASS** |
| A1.2 | `degree(net, ob)` — bands continuous `net` into fail/partial/success/overwhelming at 0.5-offset thresholds | `core.py:35-45`, citing the ER-2 continuity-correction (`params/core.md` §Continuous Engine) | net<0.5 → fail | net≥2·ob−0.5 & ≥2.5 → overwhelming | Self-consistent boundary math (the −0.5 correction is explained and matches the docstring's own worked rationale for a fixed `DECISIVE_OB=3`). No gap or overlap between bands verified algebraically (fail <0.5 ≤ partial <2.5 ≤ success <5.5 ≤ overwhelming, for ob=3). | **PASS** |
| A1.3 | `resolve(pool, net_sigma, rng)` — mu-shift resolution; boost = `soft_cap(net_sigma)*sigma_n(pool)` added to the raw roll | `core.py:47-53` | n/a (stochastic) | n/a | `soft_cap` bounds `net_sigma`'s contribution (prevents an unbounded sigma stack from producing a runaway net); doc explicitly notes an earlier Ob-shift approach was rejected because it "distorted the degree bands." No div-by-zero: `sigma_n(pool)` is called on `pool≥5` (floored above), never 0. | **PASS** |

## A2 — Damage chain

| ID | Formula | Source | Min Output | Max Output | Issues | Status |
|---|---|---|---|---|---|---|
| A2.1 | `damage(deg,...)` = `round(max(0, (strength+heft) × coupling × quality × DMG_SCALE))` | `core.py:200-216` | deg not in {graze,success,overwhelming} → 0 (explicit early return; `partial`/`fail` deal no damage) | Unbounded above in principle, but `quality` is itself capped (`OW_MAX=2.5` via `tanh(z/OW_Z)` at `core.py:232-234`) and `coupling` factors are all constants ≤~2.4 (DELIVERY×transmit) | `max(0, ...)` guards against a hypothetical negative impact; verified `strength` (1-7 attribute range) and `heft` (weapon-physics derived, ≥0 by construction — `weapon_physics.heft()`) cannot go negative given the attribute floor. | **PASS** |
| A2.2 | `_transmit(mode, mat, coverage, perc, gap_prec)` — puncture path: `max(t, GAP_EXPOSURE[mat]*gap_prec)`; percussion path: `t *= max(PERC_TRANSMIT_FLOOR, min(1.0, perc/ref))` | `core.py:143-157` | `PERC_TRANSMIT_FLOOR=0.35` floors the percussion multiplier — cannot reach 0 even if `perc=0` | multiplier capped at 1.0 | Division `perc/ref` uses `ref ∈ {PERC_AUTH_REF=8.0, PERC_AUTH_REF_SOFT=6.5}`, both nonzero constants — no div-by-zero. `RESIST` table covers all 4 armour materials × 3 modes with no missing cells (verified `none/cloth/mail/plate` × `percussion/shear/puncture` all populated, `core.py:86-89`). | **PASS** |
| A2.3 | `coupling(head, armor, ...)` — `cut_thrust` takes `max(cut-path, point-path)` (half-sword versatility) | `core.py:180-199` | n/a | n/a | `DELIVERY.get(head,1.5)` provides a fallback default for any unlisted head token, so an unrecognized head string degrades gracefully rather than raising `KeyError`. `eff/CUT_AUTH_REF` division uses a fixed nonzero constant (0.70). | **PASS** |

## A3 — Health / Wound formula: a genuine prose/code drift (finding)

| ID | Formula | Source | Issue | Status |
|---|---|---|---|---|
| A3.1 | Wound Interval: `WI = round(End + 4 + 0.4×Spirit)` · Health: `round(WI×(MaxWounds+1) + 0.25×Strength×End)` | `designs/scene/combat_engine_v1/combatant.py:35-42` (`wound_interval`, `health_full`) — **matches** `designs/scene/derived_stats_v30.md §4.1` exactly (lines 55-72, "AUTHORITATIVE (PP-716)", D-A update ED-1021 2026-06-18) | `params/core.md:158`'s own Health row still states the **pre-D-A** formula `(End+6) × (MW+1)`, range "14–48" — it omits both the Spirit-weighted Wound-Interval term (`+0.4×Spirit`, base lowered 6→4) and the Strength→Health survivability buffer (`+0.25×Strength×End`) that `derived_stats_v30.md §4.1` and the live `combatant.py` both implement. The row does cite `derived_stats_v30.md §4.1` as authoritative in bold, so a careful reader is pointed to the correct formula — but the row's *own* formula/range column is stale and would mislead anyone who reads only `params/core.md` (which CLAUDE.md §5 names as exactly the doc a number-into-Godot pass is supposed to resolve against). Concretely: at End=4/Spirit=3/Str=4 the stale formula gives `(4+6)×3=30`; the correct formula gives `round((4+4+1.2)×3 + 0.25×4×4)=round(27.6+4)=32` — a ~7% discrepancy that would propagate into a Godot Health stat if hand-transcribed from the wrong row. | **P2 — see gap register** |

## A4 — Stamina formula: a second doc-internal (not cross-doc) inconsistency (verification pass)

| ID | Formula | Source | Issue | Status |
|---|---|---|---|---|
| A4.1 | `stamina_max(end,spirit) = 3×end + 2×spirit` | `combatant.py:45-47` (`stamina_max`), thin-accessed by `systems.py:92-93` | Live code matches `derived_stats_v30.md` §4.2's own **Formula** row exactly (hand-verified `stamina_max(7,7)==35`). But that same §4.2 table's **Range** row states "5–47 (Spirit/End 1–7)" — internally inconsistent with its own Formula row one line above (max is 35, not 47; even the prior formula it says it replaces, `Endurance×5`, tops out at 35). This is a single-table, doc-only transcription error — not a cross-doc drift like A3.1, and not a code defect. | **P3 — see gap register GAP-PC-7** |

## Summary

No division-by-zero, negative-pool, or out-of-band boundary defects found in the core resolve/damage
chain — the module is unusually mature and self-audited (every tunable in `config.py` already carries
a provenance tag, and prior audit passes ED-1050/ED-PC-0002/ED-PC-0009/ED-PC-0010/ED-PC-0011 have
already swept most of the obvious formula-grounding issues). Two live formula/doc defects found, both
**documentation drift**, not engine bugs: `params/core.md`'s Health row (A3.1, P2) and
`derived_stats_v30.md`'s own internally-inconsistent Stamina range cell (A4.1, P3) — neither is
reflected incorrectly in the actual `combat_engine_v1` code, which was independently hand-verified
against both authoritative formulas.
