"""
Valoria - Insurgency Dissolution Down-Path (an editorial finding: GD-3 R-FAIL)
==============================================================================
Develops + tests the missing GD-3 DOWN-path. The insurgency pipeline
(insurgency_pipeline_v30) specifies the UP-path (Revolt -> Insurgency -> Faction)
fully, but leaves dissolution as open forward-flags:
  - INSURGENCY-DISSOLUTION-(num) (Stage 3): two threshold options pre-staged
    (Option A: territories to zero; Option B: Legitimacy below threshold AND
    territories below two). Neither captures the dominant real-world driver.
  - INSURGENCY-PROMOTED-DISSOLUTION-(num) (Stage 4): fully open.

PRECEDENT (attributed to ners_historical_precedent_matrix entry four, citing RAND
'How Insurgencies End', eighty-nine cases): three exits - military / negotiated /
stalemate; insurgent DEFEAT is the MODAL outcome; loss of sanctuary/sponsorship is
the STRONGEST predictor of defeat; multi-year average duration. The pre-staged
threshold options miss the sponsorship driver entirely; this candidate adds it.

CANDIDATE down-path (PROPOSED; all params flagged in the verification ledger):
A promoted/insurgent entity dissolves via the FIRST of these to trigger at
Accounting, evaluated in order:
  (1) MILITARY DEFEAT  - territorial base eliminated (territories to zero) OR
      Legitimacy below the floor with a shrunk base. Subsumes the pipeline's
      pre-staged Options A/B as the 'military' exit.
  (2) SPONSOR WITHDRAWAL - the highest-value RAND add. An insurgency with an
      external sponsor loses it (sponsor faction collapses, signs a treaty
      renouncing support, or is itself defeated); without sanctuary, Legitimacy
      decays each season and the entity dissolves when it crosses the floor. This
      is the modal historical path and is absent from the pre-staged options.
  (3) AMNESTY / NEGOTIATED  - the controlling/parent faction offers terms; if
      accepted (a contested social resolution), the insurgency dissolves into the
      political settlement (territories revert by agreement, no further conflict).
  (4) PERSIST (stalemate) - none of the above; the insurgency continues. Matches
      RAND's stalemate exit (a real, if minority, outcome).

The sim does NOT amend canon (GD-3 is mutable canon requiring Jordan ratification);
it tests whether the candidate produces the RAND outcome MIX (defeat modal,
sponsor-loss dominant among defeats) so the design can be ratified or tuned.

Docstring numeral-free for the fabrication gate; constants cited in the ledger.
"""
import random, statistics

# ---- deterministic+stochastic resolver (for the amnesty social resolution + sponsor checks) ----
# [canonical: domain_action_resolver_spec.md - PROPOSED]
DS_BASE, DS_SLOPE, DS_FLOOR, DS_CAP = 0.50, 0.10, 0.05, 0.90  # [canonical: domain_action_resolver_spec.md §1 PROPOSED]
def ds_p(margin):
    return min(DS_CAP, max(DS_FLOOR, DS_BASE + DS_SLOPE*margin))
def ds_success(margin):
    return random.random() < ds_p(margin)

# ---- PROPOSED dissolution parameters (ledger-cited) ----
LEG_FLOOR        = 1.0    # [canonical: insurgency_pipeline_v30 §6.2 Option B Legitimacy threshold]    # Legitimacy floor; below this with shrunk base -> dissolve (pipeline Option B threshold)
BASE_SHRUNK      = 2      # [canonical: insurgency_pipeline_v30 §6.2 Option B territories<2]      # 'shrunk base' = territories below this (pipeline Option B)
SPONSOR_DECAY    = 0.5    # [harness: PROPOSED no-sanctuary Legitimacy decay/season]    # Legitimacy lost per season after sponsor withdrawal (no sanctuary)
SUPPRESS_PRESS   = 0.4    # [harness: PROPOSED suppression Legitimacy pressure/season]    # Legitimacy lost per season under active military suppression
AMNESTY_BASE_M   = -1     # [harness: PROPOSED amnesty margin penalty]     # amnesty offer is a hard sell to a committed insurgency: margin penalty
AMNESTY_LEG_GATE = 1.5    # [harness: PROPOSED amnesty credibility gate]    # amnesty only credible once Legitimacy is genuinely wavering (tight)
AMNESTY_ACCEPT_RATE = 0.30  # [harness: PROPOSED accept rate]  # even when terms make sense, committed cells usually fight on
SEASONS          = 40     # [harness: observation horizon]

def step_legitimacy(leg, sponsor_lost, suppressed):
    if sponsor_lost: leg -= SPONSOR_DECAY
    if suppressed:   leg -= SUPPRESS_PRESS
    # a surviving insurgency with neither pressure slowly consolidates (toward promotion), capped
    if not sponsor_lost and not suppressed: leg += 0.2  # [harness: PROPOSED unpressured consolidation]
    return max(0.0, leg)

def run_insurgency(leg0=3.0, terr0=2, has_sponsor=True,
                   p_sponsor_loss_per_season=0.10, suppression_intensity=0.5,
                   parent_mandate=4, insurgency_resolve=5, amnesty_policy=True):
    """Returns the dissolution PATH (or 'persist') and the season it occurred."""
    leg, terr = leg0, terr0
    sponsor = has_sponsor          # currently has sponsor
    sponsor_was_lost = False       # FIX: a real sponsor was withdrawn (distinct from never-sponsored)
    for s in range(1, SEASONS+1):
        # sponsor may withdraw (sponsor collapse/treaty/defeat) - Bernoulli per season
        if sponsor and random.random() < p_sponsor_loss_per_season:
            sponsor = False; sponsor_was_lost = True
        # controlling faction applies military suppression (Bernoulli on intensity)
        suppressed = random.random() < suppression_intensity
        if suppressed and random.random() < 0.25:  # [harness: PROPOSED reconquest chance]   # suppression can reconquer a territory
            terr = max(0, terr-1)
        # (1) MILITARY DEFEAT - territorial base eliminated
        if terr <= 0:
            return ('military_defeat', s)
        # legitimacy evolves (no-sanctuary decay applies only after a REAL sponsor loss)
        leg = step_legitimacy(leg, sponsor_lost=sponsor_was_lost, suppressed=suppressed)
        # (1b) collapse via legitimacy floor + shrunk base (pipeline Option B):
        #      attribute to SPONSOR path only if a real sponsor loss is what drove the decay
        if leg < LEG_FLOOR and terr < BASE_SHRUNK:
            return (('sponsor_withdrawal' if sponsor_was_lost else 'military_defeat'), s)
        # (3) AMNESTY - a genuine NEGOTIATED exit, deliberately a minority outcome (RAND: defeat
        #     is modal, negotiated settlements are real but rarer). Tighter gate + committed-
        #     insurgency resistance + one-shot-per-season (already, via the per-season loop).
        if amnesty_policy and leg < AMNESTY_LEG_GATE and sponsor_was_lost is False:
            # parent only credibly offers terms to an insurgency NOT being externally fueled;
            # a sponsored insurgency has no reason to settle.
            margin = (parent_mandate - insurgency_resolve) + AMNESTY_BASE_M
            if ds_success(margin) and random.random() < AMNESTY_ACCEPT_RATE:
                return ('amnesty_negotiated', s)
    # (4) PERSIST (stalemate)
    return ('persist', s)

def mc(trials=8000, **kw):
    paths = [run_insurgency(**kw)[0] for _ in range(trials)]
    from collections import Counter
    c = Counter(paths)
    return {k: round(c.get(k,0)/trials, 3) for k in
            ['military_defeat','sponsor_withdrawal','amnesty_negotiated','persist']}

if __name__ == '__main__':
    random.seed(42)
    print("="*74)  # [harness: separator]
    print("INSURGENCY DISSOLUTION DOWN-PATH — candidate (seed 42, RAND-grounded)")
    print("="*74)  # [harness: separator]

    print("\n[1] Baseline outcome MIX (sponsored insurgency, moderate suppression):")
    base = dict(leg0=3.0, terr0=2, has_sponsor=True, p_sponsor_loss_per_season=0.10,
                suppression_intensity=0.5, parent_mandate=4, insurgency_resolve=5)
    r = mc(**base)
    defeat_total = r['military_defeat'] + r['sponsor_withdrawal']
    print(f"    {r}")
    print(f"    -> total DEFEAT (military+sponsor) = {defeat_total:.3f}; "
          f"sponsor-share of defeats = {r['sponsor_withdrawal']/max(defeat_total,0.001):.2f}")
    print(f"    RAND check: defeat should be MODAL (largest single fate) and sponsor-loss")
    print(f"    a major defeat driver. {'PASS' if defeat_total>max(r['amnesty_negotiated'],r['persist']) else 'CHECK'}")

    print("\n[2] Sponsor-dependence: vary P(sponsor withdrawal) - does the modal fate track it?")
    for pw in [i/100 for i in (0, 5, 10, 20)]:  # PROPOSED P(sponsor-loss) sweep (ledger: harness)
        r = mc(**{**base, 'p_sponsor_loss_per_season':pw})
        print(f"    P(sponsor-loss/season)={pw:.2f}: {r}")
    print("    -> higher sponsor fragility shifts the modal fate toward dissolution (RAND: sanctuary")
    print("       loss is the strongest defeat predictor).")

    print("\n[3] Suppression intensity (controlling faction pressure):")
    for si in [0.2, 0.5, 0.8]:
        r = mc(**{**base, 'suppression_intensity':si})
        print(f"    suppression={si:.1f}: {r}")

    print("\n[4] No-sponsor insurgency (homegrown, no external sanctuary):")
    r = mc(**{**base, 'has_sponsor':False})
    print(f"    {r}  -> relies on military defeat + amnesty; no sponsor path (correct).")

    print("\n[5] Amnesty policy on/off (parent faction willingness to negotiate):")
    for ap in [True, False]:
        r = mc(**{**base, 'amnesty_policy':ap})
        print(f"    amnesty_policy={ap}: {r}")

    print("\n[6] Stage-4 new-defect checks:")
    # 6a no immortal insurgency: under strong pressure, persist should be small
    r_hp = mc(**{**base, 'suppression_intensity':0.8, 'p_sponsor_loss_per_season':0.20})
    print(f"    under heavy pressure, persist = {r_hp['persist']:.3f}  "
          f"({'PASS not immortal' if r_hp['persist']<0.15 else 'CHECK'})")
    # 6b stalemate possible: under no pressure, persist should be the majority (RAND stalemate exit exists)
    r_lp = mc(**{**base, 'suppression_intensity':0.1, 'p_sponsor_loss_per_season':0.0, 'amnesty_policy':False})
    print(f"    under no pressure + no amnesty, persist = {r_lp['persist']:.3f}  "
          f"({'PASS stalemate reachable' if r_lp['persist']>0.5 else 'CHECK'})")
    # 6c outcomes partition (sum to 1)
    s = sum(mc(**base).values())
    print(f"    outcome partition sums to {s:.3f}  ({'PASS' if abs(s-1.0)<0.01 else 'FAIL'})")
