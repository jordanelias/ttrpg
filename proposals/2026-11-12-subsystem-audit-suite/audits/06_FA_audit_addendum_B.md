# FA — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 6eff039 (working tree)

Addendum to `audits/06_FA_audit.md` (the first FA lane, read at `601e715`; its §0 to §15 and its six
proposals stand except where §B2 below corrects them). This addendum does the reading the first lane
reported as not done (its §12), and adds: a reading of the whole design set for governance, factions,
war and diplomacy against the code (§B3); the campaign layer that mass battle needs from FA (§B4);
the capability consequences (§B5); further proposals (§B6); and an evidence log (§B7). Findings
continue the first audit's numbering from `F-FA-13`; resolutions continue from `R-22`.

Nothing here is the reason a behaviour is correct (`CLAUDE.md` §0.05). `.designs/`, `.audit/` and
`research/` are cited as referents by path. `[UNVERIFIED]` marks what was not checked; `[TRUNCATED]`
marks a document whose long lines were cut when read.

## B1. What was read

(Appended as the reading proceeded; the table at the end of this section is the final account.)

**Faction design set, `.designs/systems/factions/reference/` — read in full, no line truncated**
(every file's longest line is under the reader's cut; checked with `awk` before reading):
`faction_canon_v30` (739 lines; it ends after the Church sheet, the other five sheets were never
written into this file), `faction_layer_v30` and its `_infill`, `faction_behavior_v30`,
`faction_state_authoring_v30`, `factions_personal_v30` and its `_infill`, `faction_politics_v30`
(all 1,189 lines, Parts 0 to 11), `franchise_v30`, `parliamentary_transfer_v30`,
`treaty_expiration_v30`, `fractional_province_ownership_v30`, `fail_forward_pp177`,
`ci_political_v30`, `baralta_crown_claim_v30` and its `_infill`, `varfell_path_b_v30` and its
`_infill`, `political_dynamics_keys_migration_v30`, `factions_flow_skeleton_v1`. The `_index`
files are generated heading tables (`doc_index_gen.py`; one opened, `faction_layer_v30_index`, to
confirm they carry no content of their own) and were not read further.

