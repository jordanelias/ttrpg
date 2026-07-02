"""faction.py — ADAPTER (not canon). Models the canonical Parliamentary action (faction_layer §5)
on the contest engine, to exercise the engine in the faction-action context. The faction layer keeps
its own ratified resolution (§5.5 Rebuttal roll, §5.3 Mandate-weighted vote, §5.4 thresholds); this
maps that SHAPE onto the engine: proposer vs target argue before each faction-voter; each casts its
Mandate-weighted vote for whoever persuades it; the motion passes at the venue threshold."""
from dataclasses import dataclass
from .contract import A, B, Adjudicator, Pressure
from .primitives import Stasis, Appeal, Standing, Dossier, EvidenceItem
from .policy import logos_spammer
from .resolver import Bout, Contestant, Venue, TallyAtClose, PersuasionTrack

@dataclass
class Faction:
    name: str
    mandate: int                 # vote weight (§5.3)
    faculty: int = 4             # argue skill when proposer/target
    disposition: tuple = (.34, .33, .33)   # (ethos,pathos,logos) — how this voter is moved
    discipline: float = 0.25     # low → votes its disposition (high leak); high → weighs the forum case
    ci: int = 0                  # Church CI adds floor(ci/20) to weight (§5.3)
    fixed_lean: str = None       # 'yes'|'no' — AI rule (e.g. Guilds always 'no' on Blockade, §5.8)

# §5.4 thresholds + §5.5 rebuttal Ob
MOTIONS = {'censure': dict(threshold=0.50, reb_ob=2), 'outlawry': dict(threshold=0.60, reb_ob=3),
           'embargo': dict(threshold=0.50, reb_ob=None), 'blockade': dict(threshold=0.50, reb_ob=None),
           'subsidy': dict(threshold=0.50, reb_ob=None)}
# political forum baseline (the role); voters' own disposition is their character
FORUM = dict(proof_ethos=.30, proof_pathos=.25, proof_logos=.45, start_ground=Stasis.QUALITY)
RESIST_DAMP = 0.15   # [SEED] each high-Stability abstainer compresses the track toward committee (audit R1: scale-stable)

def case(strength='solid'):
    """Calibrated documented evidence for the faction context. Weights chosen (sweep 2026-06-03) so a
       'solid' case is a strong but BOUNDED lever — lifts a persuadable body's vote ~+0.2, but cannot
       carry a hostile body (~0 either way). Evidence value stays hidden from the player."""
    w = {'weak': (0.8, 0.6), 'solid': (1.2, 0.9), 'strong': (1.6, 1.2)}[strength]
    return lambda: Dossier([EvidenceItem(Stasis.QUALITY, w[0]), EvidenceItem(Stasis.QUALITY, w[1])])

def _adj(f):
    e,p,l = f.disposition
    return Adjudicator(discipline=f.discipline, char_ethos=e, char_pathos=p, char_logos=l)

def _one_vote(proposer, target, voter, prop_style, targ_style, pressure, prop_eviz):
    if voter.fixed_lean: return voter.fixed_lean
    v = Venue(**FORUM, win=TallyAtClose(), pressure=pressure)
    ca = Contestant(proposer.faculty, Standing.START, dossier=prop_eviz() if prop_eviz else None)
    cb = Contestant(target.faculty, Standing.START)
    return 'yes' if Bout(ca, cb, v, _adj(voter)).resolve(prop_style, targ_style)[0] == A else 'no'

def vote(proposer, target, body, motion, prop_style, targ_style, pressure=None, prop_eviz=None):
    m = MOTIONS[motion]; pressure = pressure or Pressure(); yes = tot = 0.0
    for f in body:
        if f.name == target.name: continue            # target doesn't vote on its own motion (§5.3)
        wt = f.mandate + (f.ci // 20)
        tot += wt
        if f.name == proposer.name: yes += wt; continue   # proposer votes for its motion
        if _one_vote(proposer, target, f, prop_style, targ_style, pressure, prop_eviz) == 'yes': yes += wt
    share = yes / tot if tot else 0.0
    return (share >= m['threshold']), share

def rate(proposer, target, body, motion, prop_style, targ_style, N=500, **kw):
    p = s = 0.0
    for _ in range(N):
        passed, share = vote(proposer, target, body, motion, prop_style, targ_style, **kw)
        p += passed; s += share
    return round(p/N, 3), round(s/N, 3)


# ── WIRING: §10 BG-vote banded outcome (committee, the strict-threshold vote() lacks it) ──
def band_of(share, threshold=0.50, margin=0.06):
    """A motion within ±margin of its pass threshold is too close to decisively resolve → committee
       (canon §10/§5.6 referral); clear of the margin → pass/fail. Respects the §5.4 Majority/
       Supermajority threshold while supplying the committee outcome the strict vote() lacks."""
    if share >= threshold + margin: return 'pass'
    if share <= threshold - margin: return 'fail'
    return 'committee'

def rate_banded(proposer, target, body, motion, prop_style, targ_style, N=500, margin=0.06, **kw):
    from collections import Counter
    thr = MOTIONS[motion]['threshold']; w = Counter(); ssum = 0.0
    for _ in range(N):
        _, share = vote(proposer, target, body, motion, prop_style, targ_style, **kw)
        w[band_of(share, thr, margin)] += 1; ssum += share
    return {k: round(v / N, 3) for k, v in w.items()}, round(ssum / N, 3)


# ── BUILD: §7.2 Succession Contest on the Persuasion Track ──
def succession(a_fac, b_fac, body_adj, a_style=None, b_style=None,
               a_stand=None, b_stand=None, exchanges=5, scale=1.5):
    """Two leading claimants contest leadership on the Persuasion Track (two-pole; a multi-claimant
       field reduces to its two leaders). Returns (outcome, winner, split_ratio, track):
         unified  (track>=9 or <=1) — unified transition, no split
         decisive (track>=7 or <=3) — single winner takes leadership
         split    (track 4-6)       — FACTION SPLIT; majority winner's share per §7.2.1
                                       (track 4 -> 0.60, 5 -> 0.55, 6 -> 0.50).
       Downstream domain logic (stat division by the ratio, Stability floor 3, territory/treaty split,
       schismatic identity by Conviction) is NOT modelled here — this returns the engine verdict."""
    pt = PersuasionTrack(scale=scale)
    v = Venue(proof_ethos=.40, proof_pathos=.25, proof_logos=.35,
              start_ground=Stasis.QUALITY, budget=exchanges, win=pt)
    a_style = a_style or logos_spammer; b_style = b_style or logos_spammer
    ca = Contestant(a_fac, a_stand if a_stand is not None else Standing.START)
    cb = Contestant(b_fac, b_stand if b_stand is not None else Standing.START)
    bout = Bout(ca, cb, v, body_adj); bout.resolve(a_style, b_style)
    t = pt.track(bout.state)
    band = pt.resolve(bout.state, closing=True)   # audit: dedup — single source for the band thresholds
    if band in ('A_total', 'B_total'):       return ('unified',  'a' if band == 'A_total' else 'b', None, round(t, 2))
    if band in ('A_decisive', 'B_decisive'): return ('decisive', 'a' if band == 'A_decisive' else 'b', None, round(t, 2))
    leader = 'a' if t >= 5 else 'b'
    ratio = {4: 0.60, 5: 0.55, 6: 0.50}[min(6, max(4, round(t)))]
    return ('split', leader, ratio, round(t, 2))

def succession_rate(a_fac, b_fac, body_adj, N=500, **kw):
    from collections import Counter
    w = Counter()
    for _ in range(N): w[succession(a_fac, b_fac, body_adj, **kw)[0]] += 1
    return {k: round(v / N, 3) for k, v in w.items()}


# ── BUILD: §10 BG Parliamentary Vote — coalitions pooled onto the two-pole engine ──
def coalition_vote(sides, lobby=0.0, scale=1.0):
    """Canon §10: factions declare pro (Side A) / anti (Side B) / abstain; each side's pool = sum of its
       Mandate; the pools clash and move the Persuasion Track (start 5 ± lobby, ED-621 clamped to the
       compromise zone), read in bands. Demonstrates that COALITIONS pool onto the two-party engine — the
       multi-faction case needs no N-party spine. `sides`: list of (Faction, 'pro'|'anti'|'abstain').
       Returns pass | committee | fail."""
    from .resolver import ContestState, roll_net   # Stage 1b: roll_net wraps sigma_leverage on the GLOBAL rng
    pool_A = sum(f.mandate for f, st in sides if st == 'pro')
    pool_B = sum(f.mandate for f, st in sides if st == 'anti')
    # canon §10: high-Stability abstention makes the vote harder to resolve decisively → compress toward
    # committee. Audit R1: damp the SCALE (acts on the track's deviation from centre, scale-stable), NOT
    # subtract from both pools (cancelled in the difference; went inert at large pools).
    abst = sum(1 for f, st in sides if st == 'abstain' and f.mandate >= 5)
    damp = max(0.0, 1.0 - RESIST_DAMP * min(2, abst))
    start = max(4.0, min(6.0, 5.0 + lobby))                       # ED-621 lobby clamp
    s = ContestState()
    s.adv[A] = max(0, roll_net(max(1, pool_A)))
    s.adv[B] = max(0, roll_net(max(1, pool_B)))
    band = PersuasionTrack(scale=scale * damp, start=start).resolve(s, closing=True)
    return {'A_total': 'pass', 'A_decisive': 'pass', 'committee': 'committee',
            'B_decisive': 'fail', 'B_total': 'fail'}[band]

def coalition_rate(sides, N=600, **kw):
    from collections import Counter
    w = Counter()
    for _ in range(N): w[coalition_vote(sides, **kw)] += 1
    return {k: round(v / N, 3) for k, v in w.items()}
