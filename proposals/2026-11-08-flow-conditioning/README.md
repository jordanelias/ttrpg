# Flow conditioning: the settlement content CR-106 and CR-107 build from
## Status: RATIFIED as the accepted first reading (Jordan, 2026-11-08, "ratify all and merge"; ED-1094): a first reading Jordan corrects; every row `[ASSUMPTION; medium; Jordan to correct]`.

**What it changes in `engine/season/`: nothing at runtime.** No loader, test or gate reads these files.
They are the builder's input for two positions of workplan v11 (`workplans/valoria_master_workplan_v11_part16.md`):
CR-106 (Church-owned building kinds, transcribed into `engine/season/rosters.yaml` and `venues.yaml`) and
CR-107 (several cohorts per settlement, the `cohorts:` block of `engine/season/cohorts.yaml`). The rulings
they follow are ED-IN-0352. Once both are built the engine files are the one owner, and this directory is
deleted with a `FORK:` row (`CLAUDE.md` §0.05 clause 3, §1).

- `content_church_sites.yaml` (CR-106), `content_cohorts.yaml` (CR-107): the drafts.
- `content_provenance.md`: each cell's source, rule and rejected alternative; the canon location disagreements the canon alignment reads.
- `content_validate.py`: read-only; from the repository root, `python proposals/2026-11-08-flow-conditioning/content_validate.py`.
- `content_validate.out`: its output, verbatim.
