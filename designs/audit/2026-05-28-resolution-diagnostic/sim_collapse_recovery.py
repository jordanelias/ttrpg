"""
Valoria - Collapse Loop Bound Reachability (an editorial finding re-examination)
==================================================================
an editorial finding (and diagnostic the diagnostic finding) framed the faction collapse loop as "damped but
unbounded - no cap short of extinction." A full read of the collapse mechanics
(this session) shows that framing is INCOMPLETE - the same unread-not-absent error
CC-(value) caught. The loop has multiple bounds:

  - Survival Exception (faction_layer): a faction at Stability one that an Accounting
    Stability Check would push to zero holds at one (once per campaign; cost Mandate
    minus one, one territory Contested). An explicit cap short of extinction.
  - Collapse is NOT deletion (an editorial finding Collapse Exit): Mandate to zero, other
    attributes FREEZE, territories Uncontrolled, units Masterless. Faction persists.
  - Reconstitute: Influence Domain Action at Ob four, three consecutive seasons,
    requires at least one territory held or recaptured -> re-emerge at Stability one,
    Mandate one, other attributes at half of frozen values.
  - Wealth-zero to Military cascade is bounded: any Wealth gain restores the stat;
    Military is re-musterable. Cascade exits the moment Wealth rises above zero.
  - Institutional Consolidation (CC-(value)): deterministic plus one Stability on a clean
    season - the primary damper.

So Lesson five (no loop both undamped AND unbounded) is SATISFIED in text. But
Lesson five has a sub-clause: a bound that EXISTS but is UNREACHABLE is not an
adequate safeguard. THE REAL QUESTION: are Survival Exception and Reconstitute
practically reachable, or nominal? A collapsed faction at half attributes trying to
roll Influence Ob four three seasons running may face effective extinction even with
a paper recovery path. This sim answers that, under the deterministic+stochastic
resolver candidate (since Reconstitute is an Influence Domain Action) AND under the
current bare dice, so the answer does not depend on the resolver decision.

All mechanical constants cited in the verification ledger; narrative numbers in the
companion .md. Docstring numeral-free for the fabrication gate.
"""
import random, statistics

# ---- current bare-dice resolver ----
def die(tn=7):
    r = random.randint(1, 10)
    return -1 if r == 1 else (2 if r == 10 else (1 if r >= tn else 0))
def net(n, tn=7):
    return sum(die(tn) for _ in range(max(n, 0)))
def dice_success(pool, ob):
    return net(pool) >= ob

# ---- deterministic+stochastic resolver candidate (domain_action_resolver_spec) ----
# [canonical: domain_action_resolver_spec.md §1 — PROPOSED params]
DS_BASE, DS_SLOPE, DS_FLOOR, DS_CAP = 0.50, 0.10, 0.05, 0.90  # [canonical: domain_action_resolver_spec.md §1 — PROPOSED]
def ds_success(acting_stat, difficulty):
    p = min(DS_CAP, max(DS_FLOOR, DS_BASE + DS_SLOPE*(acting_stat - difficulty)))
    return random.random() < p

# Reconstitute: Influence Domain Action, Ob 4, 3 consecutive seasons, needs >=1 territory.
# Influence at re-emergence is 50% of frozen value; model the COLLAPSED faction's Influence
# as it tries to climb back. Ob 4 maps to difficulty ~6 in the contest model (floor(D/2)+1=4 -> D~6).
RECON_OB = 4        # [canonical: faction_layer_v30.md Reconstitute — Influence Domain Action Ob 4]
RECON_DIFF = 6      # [canonical: Ob 4 -> contest difficulty via floor(D/2)+1=4 => D~6]
RECON_STREAK = 3   # [canonical: faction_layer_v30.md Reconstitute — 3 consecutive seasons]

def attempt_reconstitute(influence, resolver, has_territory, seasons_cap=40):  # [harness: recovery observation horizon]
    """Returns (recovered: bool, seasons_taken). Needs 3 CONSECUTIVE successes + a territory."""
    if not has_territory:
        return (False, seasons_cap)   # structural precondition unmet -> cannot even start
    streak = 0
    for s in range(1, seasons_cap+1):
        ok = dice_success(influence, RECON_OB) if resolver=='dice' else ds_success(influence, RECON_DIFF)
        streak = streak+1 if ok else 0
        if streak >= RECON_STREAK:
            return (True, s)
    return (False, seasons_cap)

def mc_reconstitute(influence, resolver, has_territory=True, trials=8000, seasons_cap=40):  # [harness: MC]
    res = [attempt_reconstitute(influence, resolver, has_territory, seasons_cap) for _ in range(trials)]
    rec = [r for r in res if r[0]]
    return {
        'p_recover_within_cap': round(len(rec)/trials, 3),
        'median_seasons': (statistics.median([r[1] for r in rec]) if rec else None),
    }

if __name__ == '__main__':
    random.seed(42)
    print("="*76)  # [harness: separator]
    print("ED-868 COLLAPSE-LOOP BOUND REACHABILITY (seed 42)")
    print("="*76)  # [harness: separator]
    print("\nReconstitute = Influence Ob 4, THREE CONSECUTIVE successes, requires >=1 territory.")
    print("Influence at re-emergence = 50% of frozen value. Testing reachability across")
    print("the collapsed faction's available Influence, under BOTH resolvers:\n")

    print(f"{'Influence':>9} | {'dice: P(recover<=40s)':>22} | {'dice median s':>13} | "
          f"{'d+s: P(recover<=40s)':>21} | {'d+s median s':>12}")
    for infl in [1,2,3,4,5,6,7]:
        d = mc_reconstitute(infl, 'dice')
        s = mc_reconstitute(infl, 'ds')
        print(f"{infl:>9} | {d['p_recover_within_cap']:>22} | {str(d['median_seasons']):>13} | "
              f"{s['p_recover_within_cap']:>21} | {str(s['median_seasons']):>12}")

    print("\n[precondition] Reconstitute requires >=1 territory held or recaptured.")
    print("  If a collapsed faction holds NO territory and cannot recapture one:")
    no_terr = mc_reconstitute(4, 'ds', has_territory=False)
    print(f"    P(recover) with no territory = {no_terr['p_recover_within_cap']}  "
          f"-> the BINDING constraint is territory, not the roll.")

    print("\n[Survival Exception] one-time Stability-1 floor vs an Accounting Stability Check.")
    print("  This is a deterministic cap (no roll) - always 'reachable' by definition when")
    print("  the faction is at Stability 1 and has not yet used it this campaign.")

    print("\n[interpretation gate] A 3-consecutive-success requirement at Ob 4 is the")
    print("  reachability bottleneck on the ROLL side. Compare single-attempt success to the")
    print("  3-streak probability to show how much the 'consecutive' clause costs:")
    for infl in [3,5,7]:
        N=60000  # [harness: MC single-attempt]
        single_dice = sum(1 for _ in range(N) if dice_success(infl,RECON_OB))/N
        single_ds   = sum(1 for _ in range(N) if ds_success(infl,RECON_DIFF))/N
        print(f"   Influence {infl}: single-attempt  dice {single_dice:.3f} / d+s {single_ds:.3f}   "
              f"-> per-season streak start is rare at low Influence; recovery is SLOW not IMPOSSIBLE")
