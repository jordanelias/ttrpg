"""engine/ — Valoria's executable model. THE ENGINE is the season loop, engine/season/ (ED-IN-0284):
the host, and the only thing here that is "the engine". The rest of this package serves it:
  substrate/      leaf readers the loop uses (descriptors, composition, names)
  engine_params/  the typed exports (a fact the engine reads lives there or in one Python owner)
  autoload/       the dice engine: the d10 chain, degree_from_net, sigma leverage (not the engine;
                  renamed engine/dice_engine/ at plan position `34`)
A MODULE is reachable running code, reached by a composition row (home modules/<name>/ once built).
engine/ names no system by import: a system is resolved by string at driver construction. ONE path
seam is declared, PATH_SEAM_ALLOWED in tests/valoria/test_engine_does_not_import_systems.py, and it
holds a single entry. (Package created under ED-IN-0071 P3.)
"""
