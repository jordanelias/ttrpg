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
     (engine/autoload/dice_engine.py) scales to the difficulty. This tree's
     faction_action._degree used fixed cutoffs and ignored it.
  2. Does scraping exactly zero count as a partial success or a failure? Canon
     says failure; faction_action said partial. Same number, opposite outcome.

A third difference was NOT part of that call: faction_action rolled d6 counting
4+, while the canonical engine is d10 (the separate strategic-layer question).

⚠⚠ ALL THREE OF THOSE BLOCKERS ARE NOW FALSE, AND HAVE BEEN FOR WEEKS. Read this
before treating the paragraph above as a reason not to migrate. Verified against
the code 2026-08-24 by a read-only contamination audit:

  1. `faction_action._degree` does NOT use fixed cutoffs. It is an adapter:
     `return dice_engine.degree_label(net, 0)` — the owner's ladder, in this
     module's string vocabulary. Its own docstring says "NOT a second ladder".
  2. Therefore zero does NOT read as a partial here either; the owner decides,
     and the owner says failure. Blockers 1 and 2 were the same blocker and both
     died when `_degree` became an adapter.
  3. `faction_action` does NOT roll d6. It calls
     `sigma_leverage.roll_net_continuous(pool, rng=rng)` — d10, fractional,
     sigma-leveraged, carrying the Jordan ruling of 2026-08-14 inline.

So J2's migration is UNBLOCKED by its own stated criteria, and the live campaign
has gone on resolving every battle through this retired tree while the reasons
not to migrate were already untrue. NOT migrated here: that is MB-lane work with
a measured balance delta, and a docstring is not the place to do it. What this
note fixes is the contamination — a retired module telling every future reader
that a migration is blocked, using three facts that the code had already
overturned.
"""
