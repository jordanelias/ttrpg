# Mode E — Core Principles Compliance: Personal Combat

**Cross-reference note (process finding, not a mechanic finding):** the task brief and
`skills/valoria-mechanic-audit/SKILL.md` both describe this mode as checking "the 13 core principles
from `canon/02_canon_constraints.md`." Having read that file in full, it contains **P-01 through
P-15** (Inseparability, Monstrosity, Rendering, three emergence modes, Threadcut beings, Calamity,
Epistemological barrier, Memory pulling, Coherence, Temporal Disjunction, Drift propagation,
Forgetting, Board/VG modes, three-layer being-persistence) plus **GD-1/2/3** (Peninsular Sovereignty,
mandatory-action precedence, Revolt→Insurgency pipeline) — a philosophy/game-design-directive ledger,
**not** the 13-item list ("Roll only when meaningful," "Let It Ride," "Histories not Skills," etc.)
that Mode E's own table in `SKILL.md` actually enumerates. The two lists do not overlap. This audit
uses `SKILL.md`'s self-contained 13-item table as the operative checklist below (since it is fully
specified there and is clearly the intended check), and separately confirms personal_combat's
relationship to the *actual* `canon/02_canon_constraints.md` P-01–P-15 set at the end of this file.
**No action** on this mismatch — it's a routing note for whoever next edits `SKILL.md`'s Input
Validation section, filed here rather than silently worked around. P3, no ED.

## The 13-principle table (per `SKILL.md`)

| # | Principle | Verdict | Evidence |
|---|---|---|---|
| 1 | Roll only when meaningful | **PRESENT** | `state_graph.py`'s `AwaitTempo`/`ACT_THRESHOLD` gate (`config.py:54`) means an Exchange only resolves once tempo clears a threshold — not a roll-every-beat model. |
| 2 | Let It Ride | **PRESENT** | `core.resolve()` is called once per exchange to produce one `(deg, net)`; no re-roll path found anywhere in `wrapper.py`/`systems.py` (grepped for "reroll"/"re-roll" — zero hits). |
| 3 | Fail Forward | **PRESENT** | A `'fail'` degree still produces a live consequence: `RIPOSTE_ON_FAIL=0.32` (`config.py:74`) gives the defender a riposte chance rather than the exchange being a dead no-op. |
| 4 | Histories, not Skills | **PRESENT** | `combatant.py:151` — `skill(axis)` returns "0 = untrained; positive = trained bonus," and Combat Pool is History-derived (`core.resolution_pool`), not a discrete Skills list. |
| 5 | Pool = Attribute + History bonus | **ALTERED (ratified)** | Combat Pool is **History-only**, explicitly "Agility-INDEPENDENT" (`core.py:31`, ED-901, re-ratified ED-900/904) — a deliberate, documented departure from the general Attribute+History pattern still used elsewhere (Fieldwork Pool = Primary Attribute×2 + History, `params/core.md:253`). This is a ratified subsystem-specific simplification, not a silent violation — cited by ED number in the code itself. **No action.** |
| 6 | Wound system with escalating Ob | **ALTERED (ratified)** | Not the literal tabletop "+1 Ob per wound" — instead a bilateral, continuous fractional-Ob channel (`WOUND_ATK_OB=0.15`/`WOUND_DEF_OB=0.25` per wound, `config.py:65`), reasoned through in the docstring as the correct reinterpretation for a continuous engine (ED-1041, superseding the −1D form via ED-PC-0005, 2026-07-08 Jordan ruling). Escalation and the wound-count cap (`MaxWounds+1`) are both present. **No action.** |
| 7 | Inspiration/Spirit economy | **PARTIAL** | A Spirit-linked resource exists (`Concentration = 3×Focus + 2×Spirit`, drains via `CONC_DRAIN_*`, recovers via `CONC_RECOVER_FRAC`) but no token named "Inspiration" appears anywhere in `combat_engine_v1` (grepped `config.py`/`systems.py`/`wrapper.py`/`combatant.py` for "inspir" — zero hits). Likely Inspiration is a session/narrative-layer resource that intentionally doesn't surface inside the physical resolver. **No action** — flag as a scope question for whoever owns the Inspiration economy doc, not a personal_combat defect. |
| 8 | Virtues & Vices | **ABSENT** | No mechanical presence in `combat_engine_v1` (grepped, zero hits for "virtue"/"vice"). Plausibly intentional — moral-character mechanics likely belong to the social/narrative layer, not melee resolution. **No action.** |
| 9 | Social combat via Rhetoric | **ABSENT (out of scope)** | Correctly absent — this is the `personal_combat` subsystem, not `social_contest` (a separate SC-lane doc). **No action.** |
| 10 | Reach/Speed priority | **PRESENT — central to the design** | `reach_base`, `weapon_tempo`, per-armour `REACH_W` weighting, and the entire reach↔armour rotation (`REACH_DECAY_K`, FIX-1) are core throughlines per `combat_throughlines_v1.md`; this principle is arguably the engine's organizing axis. |
| 11 | Phase-based combat | **PRESENT** | `state_graph.py`'s explicit `STATES` machine (Approach → AwaitTempo → Exchange → {Bind, Riposte, HitLanded, Contact} → Separation) is a tested, declarative phase graph (`test_combat_state_graph.py` + a dynamic coverage harness diff the map against the live trace). |
| 12 | Beginner's Luck | **PRESENT (functional equivalent)** | No named "Beginner's Luck" mechanic (only one repo-wide hit, in an unrelated D10 integration guide, not wired into combat_engine_v1) — but `POOL_FLOOR=5` (`core.py:27`) guarantees any character, including History=0 (untrained), always rolls a minimum-5 pool rather than a near-zero one. Functionally serves the same "untrained characters can still meaningfully attempt this" accessibility goal the tabletop principle names, via a different mechanism. **No action.** |
| 13 | Circles and Resources | **ABSENT (out of scope)** | Social/economic resolution correctly lives outside a melee-physics resolver. **No action.** |

## Relationship to the actual `canon/02_canon_constraints.md` (P-01–P-15, GD-1–3)

Checked for completeness since the task named this file explicitly. `combat_engine_v1` has **no
Thread-operation interface** (no Leap/Weaving/Pulling/Mending references in any of `core.py`,
`systems.py`, `wrapper.py`, `combatant.py`, `weapon_physics.py`, `contact.py`) — confirmed by
`propagation_map.md`'s PP-716 entry, which routes the wound↔Thread interface through
`designs/threadwork/threadwork_v30.md` instead. P-01 (Inseparability), P-11 (Temporal Disjunction),
and the rest of the P-XX set govern Thread operations specifically; a melee strike in
`combat_engine_v1` is not a Thread operation, so these constraints are correctly **not engaged** by
this subsystem rather than violated. GD-1/2/3 (victory conditions, mandatory actions, insurgency
pipeline) govern the provincial/strategic layer and are likewise not applicable to personal-scale
weapon resolution. **No action** — scope boundary is clean.

## Summary

0 violations. 2 ALTERED items, both explicitly ratified by cited ED numbers in the code itself
(exactly the CLAUDE.md §2 "loud, not silent" pattern working as intended). 1 PARTIAL (Inspiration —
flagged as a scope question, not a defect). No P1/P2 findings from this mode.
