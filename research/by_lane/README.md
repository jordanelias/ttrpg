# Research and precedent by lane — critical evaluation

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · a pointer index; resolves nothing at runtime
## Date: 2026-10-16 · Lane: IN (cross-cutting)

**What this is.** `research/00_INDEX.md` maps where game precedent and historical research live. These ten
files judge it: for each lane, the historical research, the game precedent and the repository work are
sorted separately, each is evaluated for method and sourcing, and §4 of each file joins every function,
verb and primitive of the lane to its evidence (GROUNDED, PARTLY, UNGROUNDED, CONTRADICTED, UNREACHED).
If this directory were deleted the game would behave identically.

| Lane | File | Covers |
|---|---|---|
| MB | `MB_mass_battle.md` | formations, field engine, gauge bands, personal-to-field seam, mustering |
| PC | `PC_personal_combat.md` | melee and ranged combat, wounds, duels, HEMA sources |
| FI | `FI_fieldwork_investigation.md` | investigation, inquiry verbs, detective-game survey |
| SC | `SC_social_contest.md` | contests, proceedings, rhetoric, negotiation |
| FA | `FA_faction_actions.md` | factions, seats, governance, treaties and war, victory |
| WR | `WR_world.md` | canon, threadwork, the Calamity, events, emergence, arcs |
| IN | `IN_infrastructure.md` | resolution kernel, season loop, the 45 verb rows, roster, plan |
| GO | `GO_godot_port.md` | the Godot port documents and their agreement with Layer 1 |
| SE | `SE_settlements_territory_economy.md` | settlements, territory, economy, populations |
| NPC | `NPC_npc_cast.md` | people and cast (no ED lane of its own) |

## How to read them

1. **Each file opens with §0, a verdict and ranked problems, worst first.** Everything after §0 is the
   evidence for it.
2. **`[CHECKED]` means the drafting agent opened the repository source at the cited locator. `[READER]`
   means it took the claim from a reader extraction.** The extractions (cited by stem and section, for
   example `R6 §K4`, `C7_2 F`) were working files of this pass and are not stored in the repository, so a
   `[READER]` locator cannot be followed; the claim stands on the extraction's word. A `[CHECKED]` locator
   can be followed and re-opened.
3. **Method.** Reader agents extracted each source in full to fixed templates; one synthesis per lane;
   then an independent read-only critic attacked the draft against the working tree; then every critic
   finding was re-verified at source before the draft was changed. Each file ends with a METHOD NOTE
   listing the corrections. The critic checked a sample of each lane (14 to 41 claims), not all of it.
4. **Findings the critics overturned are corrected in the files**, so a claim in the index's earlier
   commits (`00_INDEX.md` history) may differ from the file.
5. **Dated readings.** The HEAD each lane was read at is stated in its opening note; lanes were read at
   `d885abf` or `021fd96`. A count or locator is a reading of that commit.

## Limits

- Not read: proposals the plan has retired, subjects outside the ten bins, and the bodies of the
  `v30-snapshot-2026-06-28` and `archive-2026-08-05` refs beyond the paths `00_INDEX.md` §2.E lists.
- The two surveys behind the 58 and 84 primitives, and the nine-game systems teardown behind
  `proposals/2026-09-10-settlements-factions-populations/`, are not in the repository
  (`00_INDEX.md` §7); claims resting on them are unverifiable here.
- `CONFIDENCE` and `GAP` tags inside each file mark where a lane could not settle a point.
