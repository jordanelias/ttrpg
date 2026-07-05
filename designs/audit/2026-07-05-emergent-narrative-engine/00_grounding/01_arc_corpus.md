# Grounding 1 — The simulated-arc corpus (seeds, register, mechanization state)

## Status: PROPOSED (design-effort grounding — Jordan-vetoable)
_Explorer output, 2026-07-05 planning phase (sonnet lane), verified against the working tree._

## (a) Inventory, ID scheme, generation provenance

`references/arcs/` is the **arc register** (v8, 2026-04-13, PP-575), one logical document split
across five files, ~110 arc IDs:

| File | Section | Count | Contents |
|---|---|---|---|
| `arc_register_clocks.md` §I | Clock vectors | 12 (ARC-P01–P07 + interactions) | Passive pressures from TC, RS, Coup Counter, Axis 9, NPC drift, IP, PI |
| `arc_register_threads.md` §II | Thread vectors | 8 (ARC-S04/05/15/32–34, T07/T18) | Coherence depletion, Lock/Gap drift, Calamity radiation |
| `arc_register_territory.md` §IV | Territory vectors | 6 root TE-IDs, tiered | Map-state pressures, active while trigger holds |
| `arc_register_factions.md` §III | Faction vectors | 87 (ARC-S/T/P + NPC-ARC-XXX) | Bulk of the corpus; incl. crime/underground reframes |
| `arc_register_events.md` §V–VI | BG events + Convergence | 5 BG-CV + 8 COLLISION A–J | One-time BG events; multi-vector intersections |

**ID scheme**: `ARC-` + tier (`S` standing/slow-burn, `T` triggered/threshold, `P`
passive/clock-driven) + number; `NPC-ARC-XXX`; `TE-##`; `BG-CV-##`; `COLLISION A–J`.

**Entry anatomy** (uniform): `**ID — Title** \`Faction | Territories | Mode\`` header → trigger
condition(s) → mechanical effects with exact stat deltas/thresholds → closing "Direction:"
sentence (the causal logic). Branching lives downstream (skeleton tests, sim_arc files), not in
the register.

**Two "randomized seed" methodologies** feed the register:
1. **Numeric RNG Monte-Carlo**: `tests/sim_framework/arc_test_batch{2,3,4}.py` +
   `arc_test_provisional.py` — settlement/faction dice engine (`random.Random(seed)`, TN7),
   fixed `SEEDS = [42, 77, 99, 137, 201]`, 16–24 seasons, one mechanic parameter varied per
   batch; `arc_test_batch*_results.md` are the prose write-ups per seed ("writing around
   randomized seeds"), with spec-change recommendations derived from observed divergence.
2. **Hand-authored "Mechanical Seed" stress docs**: `tests/sim/sim_arc_*.md` — each arc opens
   with a `### Mechanical Seed` threshold-crossing chain, then table-facing prose + a mermaid
   causal chart citing exact Ob/dice values; injects irrational-player archetypes (IP-A..F) as
   deliberate behavioral randomization.

## (b) Representative anatomy — ARC-S07 "Torben Loyalty Clock" (the capstone compilation target)

`arc_register_factions.md §III (Crown)`: `Crown | ALL | ALL`. Trigger: IP 30 → Tutoring Demand.
Vector: Loyalty (8→0) −1/season when Covert Contact (Intel vs Ob 3/season) fails; Loyalty ≤3 →
Coup Counter +1; ≤2 → Crown Mandate −2 cumulative; 3 consecutive successful contacts → floor 6;
Laskaris flip interaction. "Direction: Altonian pressure converts the heir into a lever against
the dynasty." Cross-referenced by ARC-S20, ARC-T02 (Almud Belief collision), ARC-T13,
COLLISION C, and `sim_arc_01_irrational_player_arcs.md` ARC 1 ("The Succession Weapon" — full
narrative walkthrough + decision tree).

## (c) The arc-generator skill (authoring pipeline, not runtime)

`skills/valoria-arc-generator/SKILL.md`: mandatory reading chain (canonical_sources → glossary →
params → NPC/territory docs → `designs/arcs/gm_ref/` for dedup) → fixed output (Narrative 3-4
paras, no jargon → mermaid causal chain, every node citing a mechanic/Ob/threshold → footer with
emergent-logic statement + arc shape). Hard rules: "no single player decision caused this";
seasonal ±2 cap; mandatory `[EDITORIAL:]` flags. ⚠️ `designs/arcs/gm_ref/README.md` claims the
directory is "currently empty" while it holds 8 files (~300KB) — stale README.

## (d) Mechanized vs prose-only

- **T-23 "NPC Arc Emergence" — implemented**: `npc_behavior_v30 §5` state machine (§5.1 generic
  transition triggers; §5.2 named-NPC branch maps A–F) + `sim/cross_scale/domain_echo.py`
  (the §5 scale_transitions mechanism) + `tests/sim/settlement_mgmt_stress_01/
  module_11_provincial_authority.py` (the Governor→Province→National Echo chain, "the literal
  canonical mechanism T-23 names").
- **T-24 "Convergence as Crisis" — prose-only** ("fully specified", a lower bar): sole home is
  `arc_register_events.md §VI`; no code module computes convergence detection (sim/ grep: only
  physics collisions/numerical convergence). = audit F-2 / ED-IN-0003.
- Open editorials against the register: ED-401–405 flagged (workplan_review_2026-04-26
  MISSING-10) as absent from the active ledger; ED-609 open (Torben Conviction emergence).

## (e) Hooks into live mechanics

Arc entries cite clocks/stats directly — TC, RS, IP, PI, Coup Counter, Mandate/Influence/
Wealth/Stability/Military deltas, Locks/Gaps — but **never Keys or Domain Echo by name**
(neither term appears in `references/arcs/`), and **no runtime module consumes ARC-IDs**
(module_contracts + sim/ contain zero `ARC-` references). The register is the narrativization
layer atop mechanized clock/Echo code — a data source the engine COULD ingest, not one it does.
