# Handoff — SE (Settlements)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. This file restates no count, status or date of state: open or run the pointer. The narrative this file used to carry is verbatim in `registers/handoffs/HANDOFF_SE_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| SE-CAPACITY: build `capacity(w, rung)` Query the ED-SE-0051 ruling requires | `ED-SE-0051` (ruled arm); `workplans/2026-09-18-governance-settlement-behaviour-plan.md` position 24d | implement per the ruling's Query-not-fixture shape |
| `found` verb (P4, the capacity throttle) | `workplans/2026-09-18-governance-settlement-behaviour-plan.md` position 24e | build after position 15 |
| Matter/works proposal (`nearest_store`, body gate, `works`/`found`) HELD BACK IN FULL | `ED-SE-0053` | Jordan ratification decision, then author into canon |
| Built-world ontology proposal (Site/Rung fabric-address, fortification bands) HELD BACK IN FULL | `ED-SE-0052` | Jordan ratification decision, then author into canon |
| H-62: no verb writes a `Person` interior field, so `choose` scores a constant | `proposals/2026-09-10-settlements-factions-populations/05_COLLISIONS_AND_RESIDUE.md` §R7 | name which verbs write which axis at which `Degree` |
| D6: which G606 recall-clock wiring ships (blocks D5 execution) | `designs/architecture/ners_vsg_reconciliation_v1.md` (bare filename; see `CURRENT.md` Settlement row) | Jordan decision |
| Governance-loop redesign staging, overarching tracking row | `ED-SE-0001` | stage `governance_play_redesign_v1.md` toward ratified canon per-stage |
| Promote-ready P2/P3 items unlanded: CHN-6, HRE-3, HRE-4, VEN-SE-2, IT-1, HAB-1 | `ED-SE-0018`, `ED-SE-0019`, `ED-SE-0020`, `ED-SE-0022`, `ED-SE-0024` (open); see `designs/architecture/ners_vsg_reconciliation_v1.md` Phase 2/3 for per-item disposition | author per the reconciliation doc's refined dispositions |
| Card-deck specs for 2026-07-09 batch triggers (Cell Revolt, clerk-corruption Intrigue, Ordenanza-sanction, Patron's-Rivals-Move) | `governance_play_redesign_v1.md` §2.2/§2.3 (bare filename; see `CURRENT.md` Settlement row) | author standalone card specs |
| Sim implementation of SE-1..SE-6/SE-10 sections (drafted in prose, no sim code beyond SE-5's dormant proxy) | `ED-SE-0007`..`ED-SE-0012`, `ED-SE-0016` | sequence per docket: SE-5/SE-6 → SE-2/SE-3 → SE-4 riding `ED-SE-0001` |
| Remaining `needs_jordan` forks from the 2026-07-09/07-08 dockets | `grep -h needs_jordan.*true registers/editorial_ledger_se.jsonl` | Jordan rules each |
| MW-11 / MW-5 falsifiers currently RED (crossing predicate downward-only; `withdrawal_only`/death same-season collision) | `ED-SE-0053` | resolve if/when the proposal is authored into canon |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| Do not re-propose `band_floors.person` as new — `band_floors["body"]` already exists and is live-read | `ED-SE-0052` |
| Do not re-propose hearth larders or any delivery move across a `contain` edge — matter moves only by `transfer` | `ED-SE-0053` |
| Do not re-propose cutting `fort_level` / `facility_tier` — both have live engine readers behind a blocking round-trip `--check` | `ED-SE-0052` |
| Do not cite line numbers into a dated handoff section as stable — cite by heading text; a rewrite moves the body | prior repair recorded in `HANDOFF_SE_history.md` |
| Do not point at `systems/**` paths for SE design docs — `systems/` holds no `.md`; use `CURRENT.md`'s Settlement row (bare filename) | `ED-IN-0231`, CLAUDE.md §1 |
