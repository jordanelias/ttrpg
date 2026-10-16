# Research and precedent by lane — critical evaluation, missing areas and recommendations

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · a pointer index; resolves nothing at runtime
## Date: 2026-10-16 · Lane: IN (cross-cutting)

**What this is.** `research/00_INDEX.md` maps where game precedent and historical research live. These files
judge it, and then set the whole game as it exists in code and in workplan v9 against what its lanes need.
For each lane: the historical research, the game precedent and the repository work are sorted separately and
evaluated (§§0–6); the lane's throughlines (§7); its missing areas, each shown absent by a search that was run
(§8); a NERS pass (§9); and distilled recommendations grouped as primitives, verbs, mechanics, texture and
surface (§10). `00_COMPARATIVE_ANALYSIS.md` weaves the ten lanes together: shared root causes, dependencies,
collisions between recommendations, how conflicts were reconciled, a consolidated missing-areas register, a
register of decisions that are Jordan's, and a dependency-ordered recommendation set.

This is an audit-design pass over six months of repository work (Jordan, 2026-10-16: it "gets permission to be
whatever it is"). Its recommendations are this pass's output; none is entered in the plan or a ledger until
Jordan so rules. If this directory were deleted the game would behave identically.

| File | Covers |
|---|---|
| `00_COMPARATIVE_ANALYSIS.md` | the ten lanes compared, interactions and collisions reconciled, consolidated registers |
| `MB_mass_battle.md` | formations, field engine, troop stock and composition, gauge bands, personal-to-field seam, mustering |
| `PC_personal_combat.md` | melee and ranged combat, wounds, duels, the person-to-fight seam |
| `FI_fieldwork_investigation.md` | investigation, inquiry verbs, findings, the information cluster |
| `SC_social_contest.md` | contests, proceedings, rhetoric, petitions, testimony |
| `FA_faction_actions.md` | factions, seats, war, treaty, succession, ending, army assembly |
| `WR_world.md` | canon, threadwork, the Calamity, events, forcing, the chronicle |
| `IN_infrastructure.md` | resolution kernel, season loop, the 45 verb rows, roster, plan |
| `GO_godot_port.md` | the Godot port: parity, pause, the rule export |
| `SE_settlements_territory_economy.md` | settlements, territory, economy, population, troop stock |
| `NPC_npc_cast.md` | people and cast (no ED lane of its own) |

## How to read them

1. **Each file opens with §0, a verdict and ranked problems, worst first.** Everything after §0 is the
   evidence for it. The appended sections run: 7 throughlines · 8 missing areas · 9 NERS pass · 10 key
   recommendations · 11 method note for the appended sections.
2. **Mark conventions.** `[CHECKED]` means the drafting agent opened the repository source at the cited
   locator. `[READER]` means it took the claim from a reader extraction. `[AUDIT]` means it took the claim
   from the NERS audit of 2026-10-14 and did not re-open it. The extractions (cited by stem and section, for
   example `R6 §K4`, `UP03 §N`) were working files of this pass and are not stored in the repository, so a
   `[READER]` locator cannot be followed; a `[CHECKED]` locator can be re-opened.
3. **Method.** Reader agents extracted each source in full to fixed templates; one synthesis per lane; an
   independent read-only critic attacked each draft against the working tree; every critic finding was
   re-verified at source before a draft changed; the lanes were then appended with sections 7–11, attacked a
   second time, corrected, and compared. Each file's METHOD NOTE lists its corrections. The critics checked a
   sample of each lane, not all of it.
4. **Missing area** means a function, primitive, verb, mechanic, texture or surface the game needs, shown by a
   named demand source (THE NINE, canon constraints, rulings and Layer 1 axioms that require a carrier,
   hole-register rows, the NERS audit, or research with at least two independent verified cases), that is
   absent or inadequate in code and in workplan v9. Each lane file separates MISSING (no position at all) from
   HOLLOW or BLOCKED, PLANNED-UNBUILT and BUILT-DARK. Lanes did not all hold the same boundary for MISSING;
   `00_COMPARATIVE_ANALYSIS.md` C6 states the rule it used.
5. **Dated readings.** The HEAD each lane was read at is stated in its notes; code in `engine/` and `modules/`
   did not change between `5445e34` and the final lane corrections. A count or locator is a reading of that
   commit.

## Design statements recorded in this pass (Jordan, 2026-10-16)

The lanes treat these as demand sources and test them against code and plan; they do not assume them built.

1. "mass battle is supposed to be based on army units that are troops levied from settlements as their own resource, and these troops are supposed to differ in quantity and quality based upon equipment and experience and their commanders etc"
2. "this 4/4 one line formation for one unit for mass battles as coded is a stub"
3. "factions are supposed to be able to assemble armies with different subunits with subformations"
4. "levy typically doesn't refer to goods/stores. that verb is wrong as currently used"
5. "our goal here, really, is to identify all the missing areas of the game as it exists in code/workplanv9"
6. "each lane to have NERS applied to it, and each lane section concludes with a series of distilled key recommendations based upon primitives/verbs/mechanics/texture/surface"

## Sources newly in hand

Seventeen uploaded documents were read and hash-checked. Five of the seven documents that
`proposals/2026-09-12-emergent-narrative-primitives-v2/04_PROVENANCE.md` §5 pins by SHA-256 are among them (the
emergent-narrative compendium and mechanical specification, the thirteen-game and nine-title surveys, and the
twenty-game consolidation); the other two pins are earlier drafts and are not in hand. The Third Strand
differs from its pin. The tracked NERS audit is `references/ners_audit_2026-10-14.md`. The uploaded documents
themselves are not committed here.

## Limits

- Not read: proposals the plan has retired, subjects outside the ten bins, and the bodies of the
  `v30-snapshot-2026-06-28` and `archive-2026-08-05` refs beyond the paths `00_INDEX.md` §2.E lists.
- Still absent from the repository and from the uploads: the two surveys behind VCD's P1–P58 and F01–F84
  (*Mechanics of Inquiry, Speech and Rule*; *Narrative Churn*), *A Tells B About C*, the earlier drafts of the
  teardown and thirteen-game documents, and Valoria Unreality Suite documents 09 and 10. Claims resting on them
  are unverifiable here.
- Most critics held read, grep and glob only; absence tests were re-run by search, and several behavioural
  claims rest on probes written by the drafting agents, which are not committed. Each lane file says which.
- `CONFIDENCE` and `GAP` tags inside each file mark where a lane could not settle a point.
