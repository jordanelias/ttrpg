"""`seam/wrappers/` -- `04_CODE_ARCHITECTURE.md` §A.2: *"one wrapper per deferred subsystem"*, and
the §A.2 table's row for them is the shortest in the document: they own **"nothing, ever"**, they
read the projection, and they emit a `Margin`.

One wrapper today: `combat.py`, the IN-side of the personal-combat call `seam/contest.py` dispatches
to. `mass_battle` and `social_contest` are resolved by the roster and not called (Jordan,
2026-09-02), so they have no wrapper here yet -- and `ED-SC-0037` rules that the interim social
provider is `engine/autoload/sigma_leverage.py`, whose wrapper is U1's to write.

⚠ **A WRAPPER'S IMPORTS STAY RELATIVE.** `tests/valoria/test_engine_does_not_import_systems.py`'s
`_relative_module_files` follows relative imports only, so an absolute import here makes the
declared `sys.path` seam invisible to the scan that bounds it.
"""
