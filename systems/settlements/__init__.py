"""systems/settlements/ — the settlements data directory: `valoria_geography_v30.yaml` (read by
`modules/mass_battle/terrain.py` and `engine/season/harness/populated.py`) and `valoria_map_v30.svg`.

The `sim/` oracle that lived here (`systems.settlements.sim.*`, moved from sim/territory/ at ED-IN-0071 P4)
was deleted at plan position `29c`; each file has an exact `FORK:5c5d8ec6` row in
`references/restructure_ledger.md`. The ED-644 territorial piety_track rename (from
designs/scene/conviction_track_v30.md) is resolved, not deferred: the territorial track was absorbed
into the affiliation roster (`engine/season/rosters.yaml`), and `references/definitions/vocab_source.yaml`
records the CV abbreviation as retired.
"""
