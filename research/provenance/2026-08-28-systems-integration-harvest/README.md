# Harvest provenance — systems integration master, 2026-08-28

## Status: PROVENANCE — append-only evidence, not canon and not reference to reason from
## Lane: IN

**What this is.** The 1,079 structured records eleven parallel harvest lanes emitted while reading the
corpus for `research/valoria_systems_integration_master_v1*.md`, plus the four briefs that governed
them. It is the evidence base for the flatten in that document's Parts 1–2.

**Why it is committed.** The master's §1.2 states that code citations from six of the eleven lanes are
advisory rather than verified. A reader who wants to check that had nothing to check against; this is
what they check against. Every code claim *reproduced into* the master was re-verified against disk
before inclusion and unverifiable ones were dropped — so **these records are upstream of that filter,
not downstream of it.**

**How to read a record.** The schema, the closed sets for `slice` / `system` / `status` / `shape`, and
the anti-fabrication rules are in `HARVEST_CONTRACT.md`. `GATE_A_BRIEF.md` is what the adversarial gate
was told to do; `CORRECTIONS.md` is the verdicts it returned, which were applied silently as edits.
`SYNTHESIS_BRIEF.md` governed the three synthesis groups.

⚠ **Do not reason from these records directly.** They are a snapshot of what eleven lanes believed on
2026-08-28, including the errors the gate later overturned — six of them traceable to a single date
window, where the lanes' design-doc sources predate thirteen commits that landed 2026-08-22 to 08-27.
**The corrected statements live in the master document.** These files exist so a claim can be traced,
not so it can be re-used.

**Do not edit.** Append-only, like the frozen ED-ledger fragments in `registers/archive/`. A record
edited after the fact stops being evidence of anything.

| file | lane beat |
|---|---|
| `H1` | `research/` — cross-scale action catalogue, personnel/muster integration master |
| `H2` | `proposals/` — social contest consolidation, throughlines and precedent, conflict architecture |
| `H3` | `systems/_architecture/` — propagation spec, derived stats, player agency, key substrate |
| `H4` | `audit/2026-07-12-governance-compendium/` — all ten files |
| `H5` | `systems/factions/` — 18 design docs + `sim/` (17 modules, 2,747 lines) read in full |
| `H6` | `systems/settlements/` + `systems/world/` |
| `H7A` / `H7B` | `scale_transitions_v30.md`, `engine/cross_scale/`, `engine/substrate/` |
| `H8A` / `H8B` | `research/` roster and historical-precedent corpus; `research/governance/` |
| `H9` | `engine/` core — `game_state`, `dice_engine`, `sigma_leverage`, `victory`, `mc_v18` |
