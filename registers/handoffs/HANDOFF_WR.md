# Handoff — WR (World)

Lane-scoped continuity for the `WR` (world) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

## Pending

- **ED-WR-0010 (PROPOSED 2026-09-10) — threadwork implementation design; the philosophy rulings
  replaced the Coherence mechanism and the code implements the replaced one.**
  New doc: `systems/threadwork/reference/threadwork_implementation_design.md`. Written against
  `canon/philosophy/` (the live suite) and salvaging the uploaded *Valoria Unreality Suite* of
  2026-09-06.

  **What needs Jordan:** adoption, and whether `threadwork_v30.md` Part 3 is edited in place or
  superseded by a new head. `CURRENT.md`'s Threadwork row is annotated and **not moved**.

  **The finding.** `RULINGS.md` rules Coherence a **distance** with two quantities that have
  different remedies — present displacement (returns with time, *conditioned on the environment
  being at equilibrium*) and a resting point (no rest moves it) — and states the consequence for
  code itself: *"a track that depletes does not model that, so whatever implements it will need a
  different shape."* `systems/threadwork/sim/coherence.py` is that shape. Six clauses absent:
  the two quantities; conditioned recovery (E-1); the permanent set (E-3/E-4); **direction**
  deciding whether there is a cost at all (§6.6) rather than scale alone; the practitioner-side
  **resilience** term (R-14); and a crossing that is a resting-point fact (§7.1/§7.4) rather than
  an integer floor that un-sets.

  **Three of the suite's four blocking questions close by ruling.** Q-1 — Diagnosis is *not* an
  operation (§6.1's criterion + R-16), so it costs nothing. Q-4 — dissolved; the regenerated P-11
  names neither CD nor History Resonance. Q-11 — **both** of its readings are struck rather than
  chosen between (Reading A quotes the formulation P-07's second clause now FAILS by name;
  Reading B is answered by §3.4's *"Not the rendering's, either"*), and §6.6's third type,
  **destructive**, is the answer: harm is not free. Q-7 superseded by R-14; Q-8 still open.

  **NO CODE WAS CHANGED.** Jordan directed the deliverable as design prose; the doc records
  precisely what `coherence.py` would become, at the granularity a later session can act on.

  **Cross-lane, and it is the one to pick up next:** `systems/threadwork/sim/rendering.py`'s
  `apply_rs_strain` / `check_calamity_threshold` are **wired stubs**, and they are the one place
  personal scale and strategic scale meet — threadwork → substrate tension → incursions → Accord →
  mandatory faction action. Turmoil and MS (`systems/overview/sim/ms_track.py`) are already live
  and ticking underneath them.

- **ED-WR-0007 (RESOLVED 2026-07-08) — pessimist-audit WR verdicts EXECUTED** (Scene Slate + threadwork;
  WR-lane follow-up to ED-IN-0027). `player_agency_v30 §4`: Step 6 → "Territorial Texture" (Thread-phenomenon
  clause CUT → Step 2b; NPC-arrival MERGED → Step 5); Step 7 Ambient DISTILLED → Step-6 backfill; Witness-Mode
  narrative-input DISTILLED → the Read/Appraise outcome (GM mechanic, never re-derived for the no-GM engine);
  Step 4 validator REFINED (capitalization-signal → explicit confirm prompt). `threadwork_v30 §2`: Past-Oriented
  Pulling DISTILLED (temporal-target variant → Pulling's Three-Axis Ob; capability kept), Mending REFINED
  (Q-robust mono-solution flag for a second Gap-repair branch — **zero-cost/Amendment-3/ED-871 untouched**).
  Scene-Slate Steps kept as numbered anchors (physical renumber = a Scene-Slate rebuild); POP physical fold =
  Stratum-B C-TW-3/4/10/11. `params/threadwork.md` carries a doc-side co-file note (no values changed). No sim edits.
  **Decision packet available** for the Mending second-branch question:
  `designs/audit/2026-07-08-pessimist-action-audit/decision_packets/DP-3_WR-TW_mending_second_branch.md`.

- **ED-WR-0003 (open) — ambient-fabric window + Appraise Revelation.** Filed 2026-07-05 from the
  ratified edge-playability audit (PR #81, "Ratify all"; finding EP-7): `scene.interaction`/
  `scene.gossip` are emitted with hard-coded `private_observers: [npc_a, npc_b]` (six sites in
  doc-12 incl. visibility defaults) so the player can never overhear gossip about themselves; and
  `npc_behavior_v30` §6.1/§6.1b "Appraise Revelation" are empty headers (npc_memory doc:null).
  Two actions: an "overheard" rule (conditional player observer when the player shares the
  scene) + write the §6.1/§6.1b revelation procedures. See the audit report §1 EP-7 / §7 item 10.

## Decisions

- 2026-06-28 — **ED-912**: Disposition & Knot unified on a ±5 swing (Bonds ≥5 now a Knot
  prerequisite; break = Disposition −3 / 4 Composure). Resolves ED-841/842/912/914; supersedes
  PP-632/PP-684. Source-of-truth + consumer tail regenerated; "Stance table" rename in combat.
  *(Filed here under `WR` since Disposition/Knots/Bonds are core personal-narrative/world-state
  mechanics, not combat- or contest-specific — but it does have a combat cross-reference
  ("Stance table" rename) and a Composure tie into the contest tracker; genuinely a borderline
  call between `WR`/`PC`/`SC` at migration time, noted honestly rather than picking silently.)*

## Next actions

(none currently tracked.)
