# Handoff — WR (World)

Lane-scoped continuity for the `WR` (world) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

## Pending

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
