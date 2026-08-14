"""systems.mass_battle.sim — mass-battle oracle (was sim.provincial.{massbattle,units,tactic_cards,altonian_reinforcements}).

RETIRED per Jordan ruling J2 (2026-08-03, ED-MB-0064): canon mass battle is
`tests/sim/mass_battle/`. This 5-module tree is retired, not kept alongside the
canon engine — J2 settles which engine is canonical; it does not author `degree`.

Still imported by `systems/factions/sim/faction_action.py:431` pending migration
to the canon engine. The live campaign still runs on this tree — do not change or
delete code here until that migration lands.

WHAT THE MIGRATION IS WAITING ON, in plain words (rewritten 2026-08-14, ED-IN-0184:
this said "blocked on Jordan ruling the four `degree` band edges", which Jordan
correctly pointed out does not mean anything in English — coined jargon copied
forward instead of translated, the failure CLAUDE.md 4 legislates against):

  1. When a faction takes a strategic action, is "how well did it go" judged
     against how hard the action was, or against fixed numbers? Canon
     (engine/autoload/dice_engine.py:94-122) scales to the difficulty. This
     tree's faction_action._degree:97-104 uses fixed cutoffs and ignores it.
  2. Does scraping exactly zero count as a partial success or a failure? Canon
     says failure; faction_action says partial. Same number, opposite outcome.

A third difference is NOT part of that call: faction_action rolls d6 counting
4+, while the canonical engine is d10 (the separate strategic-layer question).
"""
