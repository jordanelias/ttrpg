"""modules/settlements/ -- the `settlements` module (A-25; v9 IN-07). Its entries are the composition rows
whose targets are `larder.py`'s `larder_draw` and `drawn_under` (both `entry: query`, E1),
`subsist.py`'s `subsist` and `produce.py`'s `produce` (both `entry: step_call`, E2 and E3, called by
MATTER in that order), and `housing.py`'s `housing`, `fabric.py`'s `fabric` and `fortification.py`'s
`fortification` (each `entry: query`, E4..E6, called by `queries/world_q.py`'s public wrappers), and
`provision.py`'s `provision` (`entry: query`, v9 IN-52, called by the field adapter
`seam/wrappers/mass_battle.py`)."""
