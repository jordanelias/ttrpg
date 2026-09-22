# Handoff — FA (Faction Actions)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. This file restates no count, status or date of state: open or run the pointer. The narrative this file used to carry is verbatim in `registers/handoffs/HANDOFF_FA_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| score/2 obstacle-Ob derivation: three sites disagree | `tests/valoria/test_faction_obstacle_conventions.py` | do not wire piecemeal — needs a Jordan ruling reconciling `parliamentary_transfer.py`, `tribunal.py` and `crown_initiative.py`; see standing order below |
| Author the `domain_actions` / strategic-turn home doc | ED-FA-0002 | author the home doc unifying card-hand + faction actions + resolver + `da.*` tagging |
| BG victory-params re-export | ED-FA-0003 | re-derive `params/bg/victory.md` from `victory_v30.md`, fix `params/board_game.md` index |
| Fiscal Stance Treasury coupling (design drafted, sim not wired) | ED-FA-0008 | wire the stance choice + yield formula into the territory registry |
| §1.0d Kaochengfa merge + E11 counter-mechanic authoring | ED-FA-0021, `.designs/systems/factions/reference/faction_politics_v30.md:137` | author the merge into `faction_politics_v30.md` in the same pass as E11 |
| Round-2 docket promote-ready items never filed as ED rows (HRE-2, HAB-4, IT-2) | `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md`, `.designs/systems/_architecture/reference/ners_vsg_reconciliation_v1.md` | file as `ED-FA-NNNN` and land per the NERS review's sequencing before landing |
| Round-2 docket `needs_jordan` queue never filed (BYZ-1, HAB-2, etc.) | `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md` | take to a decision memo, starting with BYZ-1 (composes with HAB-2) |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| Do not wire `score/2` by editing the three disagreeing sites into agreement — the disagreement is the finding, not a bug | `tests/valoria/test_faction_obstacle_conventions.py`; narrative at `HANDOFF_FA_history.md` § "SUSPENDED — the `score/2` obstacle derivation" |
| Do not author faction-roster content assuming the old territory-nesting model — local/provincial/national tiers are independent, people-based | ED-IN-0047 (B12) |
| Faction stat writes go through `engine.autoload.game_state.Faction.adjust` only — no second write path | ED-FA-0038, `tests/valoria/test_faction_write_sweep.py` |
