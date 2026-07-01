"""Track-2 decision-prep — tabulates WP.reach()/WP.authority() (the diagnostic-only weapon_physics
derivations, `[BUILD-ONLY/DIAGNOSTIC]`, zero live callers) alongside their live counterparts
(systems.reach_base, and — for the concept authority() targets — core.damage's actual impact-force inputs),
so Jordan can see what each side currently computes and where they diverge, without deciding or touching
anything. See the companion wp_reach_authority_comparison.md for the write-up.

Run: python wp_reach_authority_measurement.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../scene/combat_engine_v1'))
import config, core, systems
import weapon_physics as WP
from weapons import WEAPONS

CFG = config.CFG
ROSTER = ["rapier", "arming", "longsword", "greatsword", "sabre", "dagger", "paired_short",
          "spear", "staff", "mace", "poleaxe", "longsword_halfsword"]


class _Mock:
    def __init__(self, w):
        self.w = w


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    print(f"{'weapon':20} {'WP.reach()':>11} {'reach_base()':>13} {'ratio':>7}   "
          f"{'WP.authority()':>15} {'perc_authority':>15}   {'live edged heft*':>17}")
    for n in ROSTER:
        w = WEAPONS[n]
        r_wp = WP.reach(w)
        r_live = systems.reach_base(_Mock(w), CFG)
        a_wp = WP.authority(w)
        a_perc = WP.percussion_authority(w)
        # *the live path's actual "impact force" analogue for an EDGED weapon is core.heft_resp (feeds
        # damage's Impact=strength+heft), not percussion_authority (which is 0 for non-blunt heads by
        # construction) -- shown so authority()'s comparison column isn't misread as apples-to-apples.
        live_edged_heft = core.heft_resp(w, CFG) if w['head'] != 'blunt' else float('nan')
        print(f"{n:20} {r_wp:11.2f} {r_live:13.2f} {r_wp / r_live:7.2f}   "
              f"{a_wp:15.2f} {a_perc:15.2f}   {live_edged_heft:17.2f}")


if __name__ == '__main__':
    main()
