"""Round-state probe (B14.13, F-PC-16): does a later engagement open with a fighter still in the half-sword form?

For N fights over four matchups (a half-swording weapon against an arming sword or a mace, in the armour that
calls the form), read each fight's `engagement_start` events through the trace seam and count the FIGHTER-STARTS
-- two per engagement, one per fighter -- of every engagement after the fight's first whose `weapon_A` / `weapon_B`
names a `HALFSWORD_BASE` key (a `_halfsword` record). The first engagement of a fight is read as a control: no form
has been taken yet, so it must never show one.

A "fighter-start" is one fighter at one engagement's opening. `engagement` resets the grip and the lunge at the
open measure and, since B14.13, the weapon form too (`combat_systems.base_form`), so after it the count is 0.

Reads the trace only: no draw beyond the fight's own `random.Random(seed)`, no state kept.

CLI:
    python workbench/round_state_probe.py [N]      # N fights in all, split evenly over the four matchups; default 800
"""
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))  # the repository root: `modules.combat` is a package
from modules.combat.combatant import Combatant
from modules.combat.weapons import HALFSWORD_BASE
import fight_trace as FT

# (half-swording weapon, opponent, armour tier of both): longsword v arming and estoc v arming in plate ('heavy'),
# greatsword v arming in mail ('medium'), longsword v mace in plate.
MATCHUPS = (('longsword', 'arming', 'heavy'),
            ('estoc', 'arming', 'heavy'),
            ('greatsword', 'arming', 'medium'),
            ('longsword', 'mace', 'heavy'))


def read(n_fights=800):
    """Returns {'fights', 'first_starts', 'first_in_form', 'later_starts', 'later_in_form'} over `n_fights` fights.
    Fight i of a matchup is seeded `i`; each matchup runs `n_fights // len(MATCHUPS)` fights."""
    per = n_fights // len(MATCHUPS)
    out = dict(fights=0, first_starts=0, first_in_form=0, later_starts=0, later_in_form=0)
    for a, b, tier in MATCHUPS:
        for seed in range(per):
            _r, events = FT.run_traced_fight(Combatant('A', weapon=a, armor=tier), Combatant('B', weapon=b, armor=tier), seed=seed)
            out['fights'] += 1
            starts = [e for e in events if e['kind'] == 'engagement_start']
            for i, e in enumerate(starts):
                key = 'first' if i == 0 else 'later'
                for w in (e['weapon_A'], e['weapon_B']):
                    out[key + '_starts'] += 1
                    out[key + '_in_form'] += w in HALFSWORD_BASE
    return out


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    r = read(n)
    print(f"{r['later_in_form']:,} of {r['later_starts']:,} fighter-starts in later engagements open in a half-sword form "
          f"({r['fights']} fights over {len(MATCHUPS)} matchups)")
    print(f"control: {r['first_in_form']} of {r['first_starts']:,} fighter-starts in the first engagement of a fight")
    sys.exit(1 if r['later_in_form'] else 0)       # the verdict rides the exit status: any later engagement opening in a form is red
