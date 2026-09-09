# Valoria — Game Design Constraints (GD-1 … GD-3)

**Status:** CANONICAL (mutable canon — updates require explicit ratification logged in the editorial ledger)
**Extracted:** 2026-09-07, verbatim, from `canon/02_canon_constraints.md` §B when that file was
retired and its §A (P-01…P-15) was superseded by `canon/philosophy/10_constraints.md`.

**Why this file exists.** §B was always a different kind of thing from §A — the source file said so
itself: *"Unlike §A (P-XX) which derives from immutable Philosophical Foundations, §B (GD-XX) is
mutable canon."* §A concerns what the world is; §B concerns victory conditions, AI action selection
and faction emergence. The philosophy suite does not carry them, and `engine/autoload/victory.py` and
`engine/mc_v18.py` cite them as their canon source, so they get their own home rather than being
retired with the file that happened to hold them.

**Nothing below is edited.** The text is as it stood, including its own dated version line, its
provisional hook table, and its cross-references to trees that have since moved. Path resolution for
those goes through `references/restructure_ledger.md`.

---

# §B — Game Design Constraints

## Version: 2026-05-17 (GD-1, GD-2, GD-3 canonized from Jordan-directed handoff 2026-05-15 hard rules HR-1, HR-9, HR-10)

These constraints govern Valoria's project-owner directives. Unlike §A (P-XX) which derives from immutable Philosophical Foundations, §B (GD-XX) is mutable canon — updates require explicit Jordan ratification logged in the editorial ledger. Same enforcement format. Mechanical violation = revision required.

| ID | Constraint | Source | Mechanical Implication | Violation Test |
|----|-----------|--------|----------------------|----------------|
| GD-1 | **Peninsular Sovereignty is the sole victory condition.** All factions share one win path: control all 15 territories (treaties counting), Accord ≥ 2, Political Stability ≤ 6, sustained 2 consecutive seasons. The 8 faction-specific alternates previously documented in `designs/scene/conviction_track_v30.md` §4.2 (Altonian Theocracy PP-414), §4.3 (Hollow Victory PP-415), §6.1 (Path B Southernmost Dominion PP-417), §6.2 (Path C Thread Supremacy PP-417), §7 (Co-Victory PP-418), and `designs/architecture/complete_systems_reference.md` Part 7 ("8 faction-specific alternates" + Partition co-victory) are STRUCK. No conditional override exists, including calamity-healing variants of Southernmost Dominion. Faction-specific competitive advantages (Crown Treaty network, Church Mass Seizure, Hafenmark Altonian Reinforcements + equipment, Varfell Threadwork first-mover + Einhir Revival, RM extra-parliamentary emergence) operate as tactical leverage toward the universal goal, not alternate paths to it. | Jordan-directed handoff 2026-05-15 HR-1, reaffirmed 2026-05-17 (project-owner directive: "only peninsula control is a victory, no conditional other ways to win"). | Victory-check code routes through a single `peninsular_sovereignty()` function. No `faction_specific_victory()` functions are permitted. Faction-unique actions (Mass Seizure, Einhir Revival, Altonian Reinforcements, etc.) produce territorial / stat / political effects that *advance toward* universal victory, never trigger victory directly. The `victory_paths` category in `registers/mechanics_index.yaml` contains exactly one entry: `peninsular_sovereignty`. | Does any code path or canon doc declare a victory condition other than Peninsular Sovereignty, including with prerequisites, qualifiers, or "alternate paths"? If yes → FAIL. Does any mechanic produce game-end faction victory without all 15 territories sustained 2 seasons? If yes → FAIL. Does any "co-victory" or "shared victory" mechanic exist? If yes → FAIL. |
| GD-2 | **Deterministic threat response precedes stochastic action selection.** Faction action-selection per season runs a mandatory-actions pass before stochastic candidate generation: (a) Accord ≤ 3 in any owned territory with no garrison → mandatory Muster action targeting that territory; (b) Accord ≤ 2 in any owned territory with garrison → mandatory Govern action targeting that territory. Up to 3 mandatory actions per faction per season may be triggered. Mandatory actions consume action slots. Stochastic candidate generation runs only after mandatories are scheduled. | Jordan-directed handoff 2026-05-15 HR-9. | AI action-selection cycle (`select_actions(faction, world)`) calls a `mandatory_actions(faction, world)` pass first. Triggered actions are scheduled to faction action queue ahead of stochastic candidates. Mandatory action pool defined in `params/factions.md` (or successor) — initial set: Muster, Govern. Faction-specific actions (Excommunication, Crown Initiative, etc.) are not mandatory-eligible. | Does AI action selection ever ignore a threat trigger at Accord ≤ 3 ungarrisoned or Accord ≤ 2 garrisoned within an owned territory? If yes → FAIL. Does any stochastic candidate evaluate before mandatories are scheduled? If yes → FAIL. |
| GD-3 | **Revolt → Insurgency → Faction pipeline.** New factions can emerge during gameplay through territorial neglect. Trigger sequence: (a) 2+ contiguous territories at Uncontrolled status, sustained 2 consecutive seasons → Insurgency formation event. (b) Insurgency starts at L=1.0, low stats (I, Sta < starting-faction baselines), non-parliamentary status — operates territorially (can hold and invade) but does NOT cast Parliamentary votes. (c) Insurgency promotes to formal Faction (parliamentary or extra-parliamentary status per below) when: L ≥ 3, 2+ territories held, Accord ≥ 4 averaged across holdings, sustained 2 consecutive seasons. (d) PT < 3 average across held territories → faction emerges as Restoration Movement variant (anti-Church identity, extra-parliamentary status — participates in CB / treaty / political surface, does NOT cast Parliamentary votes). (e) PT ≥ 3 average → generic new Parliamentary candidate, Convictions set by emergence conditions. Insurgencies can invade like any faction, including the parent faction whose territorial neglect generated them. RM-as-emergent-faction is more likely than generic emergence when world-state PT-decay (per `designs/provincial/restoration_movement_v30.md` — pending Pass 2d) has produced low-PT territories. | Jordan-directed handoff 2026-05-15 HR-10, refined 2026-05-17 ("RM is a parliamentary candidate as is any other emergent faction — it's just more likely... it would likely be extra-parliamentary"). | World maintains insurgency state machine in `sim/world/insurgency_pipeline.py` (pending Pass 2l). Accounting cascade checks insurgency triggers post-Accord-aggregation each season. Insurgency-as-invader uses the same `action_military_conquest` → mass-battle pipeline as established factions. Promoted-RM is recorded with `parliamentary_status: extra` flag that gates Parliamentary Vote eligibility while permitting all other political surface mechanics. | Does any code path prevent insurgencies from invading owned territory of any faction? If yes → FAIL. Does any mechanic require player consent for insurgency emergence? If yes → FAIL. Does promoted-RM cast Parliamentary votes? If yes → FAIL. Are non-RM emergent factions blocked from parliamentary status? If yes → FAIL. |

## §B — Enforcement Status (Level 4 hooks)

The following Level-4 hook checks are **aspirational** as of 2026-05-17. Code-level enforcement ships when the corresponding hook lands in `valoria_hooks.py`. Text constraint above is canonical immediately and supersedes any unannotated implementation.

| Hook | Constraint enforced | Status |
|------|--------------------|--------|
| `h.victory_singularity_check(victory_fn)` | GD-1: raises if any victory function other than `peninsular_sovereignty` is registered | [PROVISIONAL — pending] |
| `h.mandatory_action_precedence(action_queue)` | GD-2: raises if stochastic candidate appears in queue before all mandatories are scheduled | [PROVISIONAL — pending] |
| `h.insurgency_invariant_check(world)` | GD-3: raises if insurgency state machine produces invalid transitions or blocks valid invasion targets | [PROVISIONAL — pending] |

## §B — Cross-references

GD-1 strike propagation (Pass 2c, pending):
- `designs/scene/conviction_track_v30.md` §4.2, §4.3, §6.1, §6.2, §7 — strike with [SUPERSEDED-BY: GD-1] markers
- `designs/architecture/complete_systems_reference.md` Part 7 — strike "8 faction-specific alternates" and "Partition co-victory" with [SUPERSEDED-BY: GD-1] markers
- `designs/provincial/varfell_path_b_v30.md` — mark entire doc historical; archive
- `designs/provincial/victory_v30.md` §3 — restate sole condition, remove alternates
- `references/canonical_sources.yaml` — remove "Varfell military conquest only" stale entry

GD-2 implementation surface: `params/factions.md`, `sim/provincial/faction_action.py` (pending Pass 2l).

GD-3 implementation surface: `designs/world/insurgency_pipeline_v30.md` (pending Pass 2i), `sim/world/insurgency_pipeline.py` (pending Pass 2l).
