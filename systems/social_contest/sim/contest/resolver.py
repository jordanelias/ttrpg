"""
resolver.py — the WRAPPER + the top-down VENUE spec. No privileged "merits": primitives accumulate a
per-side advancement; the venue's win-condition decides what winning is, and the venue's defeat-
catalogue which faults are fatal. Adds (this pass):
  - a small persuasion JITTER (no two arguments land identically) — removes high-faculty exact-tie draws;
  - EVIDENCE: presenting a relevant item adds its HIDDEN value (deterministic, not a roll), with
    corroboration (diminishing returns); irrelevant evidence has nothing to present;
  - PRESSURE on the adjudicator: institutional pressure tilts advancement toward a side; public
    pressure raises the adjudicator's leak (more swayable) and tilts toward the publicly favoured side.
Resolution at the exchange boundary; clinch immediate.
"""
import random
from dataclasses import dataclass, field
from .contract import A, B, other, Move, ContestView, FaultState, Adjudicator, Pressure
from .primitives import (Stasis, Appeal, Standing, Reserve, Pool, SelfGating, Leverage, Room,
                        Resonance, Readiness, DefeatCatalogue, EvidenceItem, Dossier,
                        RhetoricalWeights, FaceScale)
# Stage 1b: rewired to the ONE canonical σ-kernel (engine.autoload.sigma_leverage), replacing the
# groundup local engine.py (the "third σ-kernel" hazard). effective_ob/degree/net_boost are
# byte-identical at TN7 (parity-tested). roll_net is wrapped below to preserve the kernel's
# GLOBAL-random stream (sigma_leverage.roll_net(rng=random) draws from the module-level RNG the
# 151 seeded tests rely on; passing rng=None would use a fresh Random and desync the seed).
from engine.autoload import sigma_leverage as _sigma
from engine.autoload.sigma_leverage import effective_ob, degree, net_boost

def roll_net(pool):
    """Behavior-preserving wrapper: canonical d10 roll drawn from the GLOBAL random stream
    (the 151-test suite seeds module-level random). Byte-identical to the groundup
    engine.roll_net loop; single-sourced through sigma_leverage/dice_engine."""
    return _sigma.roll_net(pool, rng=random)

VALID_KINDS = ("advance", "hard", "shift", "support", "pass", "evidence", "rebut")
RES_FLOOR = 0.15  # de-saturation floor (diagnostic Lesson 6): a hostile/off-axis reception can't zero
                  # an advance's resonance, so even an unfavoured appeal keeps minimal viability.
REBUT_CAP = 3.0   # Fork 3 (PROTOTYPE): max advantage a single rebuttal can erase — bounds the one
                  # attrition channel so a rebuttal war cannot death-spiral (diagnostic Lesson 5).
MERIT_SCALE = 2.6   # [SEED]
JITTER = 0.08       # [SEED] irreducible variability in how persuasion lands
PUBLIC_LEAK = 0.5   # [SEED] public pressure → adjudicator susceptibility
INST_BIAS = 0.6     # [SEED] institutional thumb on the scale
PUB_BIAS = 0.3      # [SEED] public favour tilt
EVIDENCE_CAP = 3.0  # [SEED] ceiling on one evidence item's magnitude (audit R1/R4: bound the readiness-free channel)

class ContestState:
    """Live tally the win-condition reads. Only `adv` is authoritative here; standing/room/live
       live on the Contestant / Bout (single source of truth) — no mirror to keep in sync."""
    def __init__(self):
        self.adv = {A: 0.0, B: 0.0}

class WinCondition:
    def resolve(self, s, closing, adj=None): raise NotImplementedError
class ThresholdRace(WinCondition):
    def __init__(self, T): self.T = T
    def resolve(self, s, closing, adj=None):
        a, b = s.adv[A], s.adv[B]
        if a >= self.T and a > b: return A
        if b >= self.T and b > a: return B
        if closing: return A if a > b else B if b > a else "draw"
        return None
class TallyAtClose(WinCondition):
    def resolve(self, s, closing, adj=None):
        if not closing: return None
        a, b = s.adv[A], s.adv[B]
        return A if a > b else B if b > a else "draw"
class ProofBar(WinCondition):
    def __init__(self, bar, challenger=A): self.bar = bar; self.ch = challenger
    def resolve(self, s, closing, adj=None):
        df = other(self.ch); net = s.adv[self.ch] - s.adv[df]
        if net >= self.bar: return self.ch
        if closing: return df
        return None
class GraceThreshold(WinCondition):
    def __init__(self, bar, petitioner=A): self.bar = bar; self.pet = petitioner
    def resolve(self, s, closing, adj=None):
        if s.adv[self.pet] >= self.bar: return self.pet
        if closing: return other(self.pet)
        return None

class PersuasionTrack(WinCondition):
    """Canon's two-pole Persuasion Track (social_contest §10 BG vote, §7.2 succession): a 0-10 axis,
       neutral start 5, pushed up by Side A and down by Side B, READ AT CLOSE into bands. Supplies the
       committee/compromise outcome the binary win-conditions lack:
         >=9 A_total · >=7 A_decisive · 4-6 committee · <=3 B_decisive · <=1 B_total."""
    def __init__(self, scale=1.5, start=5.0): self.scale = scale; self.start = start
    def track(self, s): return max(0.0, min(10.0, self.start + self.scale * (s.adv[A] - s.adv[B])))
    def resolve(self, s, closing, adj=None):
        if not closing: return None
        t = self.track(s)
        if t >= 9: return "A_total"
        if t >= 7: return "A_decisive"
        if t > 3:  return "committee"
        if t > 1:  return "B_decisive"
        return "B_total"


class VoteAtClose(WinCondition):
    """Fork 1 (PROTOTYPE, opt-in via venue.win): un-fuse momentum from verdict. The running `adv` is the
       room's MOMENTUM (drama); the VERDICT is a separate terminal secret ballot. Each juror votes A iff
       (sharpness*gap + per-juror noise) > 0 — the vote tracks momentum on average, but a juror can cross
       AGAINST it, so a close room is near a coin-flip while a lopsided room is near-certain. Majority
       decides. Models the secret-ballot court that deliberately severs the room from the outcome
       (Athenian dikasteria; thorubos vs the counted vote — research 2026-06-04). `noise` = how independent
       the jury is (low: tracks the room; high: can upset it). Default venues do NOT use this; the fused
       ThresholdRace/TallyAtClose remain the baseline.

       AGGREGATION (`aggregation`, ED-1057 — Panel ratification): how the individual ballots combine.
         'simple_majority'    — one-juror-one-vote; A wins iff votesA*2 > n (the historical default; the
                                cross-cultural / institutional VoteAtClose venues keep this unchanged).
         'weighted_by_standing' — each juror's ballot counts in proportion to that juror's BENCH-WEIGHT,
                                the juror's institutional rank/rigor on this bench. A juror's bench-weight
                                is its EXISTING Adjudicator.discipline (0–1) — the already-carried per-juror
                                rigor field — NOT the contestant-side Standing primitive (a different
                                concept: in-contest credibility). A wins iff the summed weight of the
                                A-ballots > half the total bench weight, else draw. Ratified for the Panel
                                adjudicator (Gate B, ED-1057 weighted-by-standing); a heterogeneous bench
                                need not mirror its highest-weight juror (a low-weight juror crossing the
                                room can still swing a near-even split, and the summed-weight threshold — not
                                a single dominant vote — decides)."""
    def __init__(self, jurors=7, sharpness=0.6, noise=0.8, aggregation="simple_majority"):
        self.jurors = jurors; self.k = sharpness; self.noise = noise
        self.aggregation = aggregation
    def resolve(self, s, closing, adj=None):
        if not closing: return None
        gap = s.adv[A] - s.adv[B]
        members = getattr(adj, "members", None)
        if self.aggregation == "weighted_by_standing":
            # Weighted majority (ED-1057): each juror's ballot counts by its bench-weight (= its
            # Adjudicator.discipline, the existing per-juror institutional rigor field). No new per-juror
            # state is invented. A wins iff summed A-weight > half total weight; equal split => draw.
            if members:
                weights = [max(0.0, float(getattr(m, "discipline", 0.0))) for m in members]
            else:
                weights = [1.0] * self.jurors            # unpaired fallback: uniform => reduces to simple majority
            total = sum(weights)
            if total <= 0.0:                             # degenerate all-zero bench => no verdict basis => draw
                return "draw"
            wA = sum(w for w in weights if self.k * gap + random.gauss(0, self.noise) > 0)
            if wA * 2 > total: return A
            if wA * 2 < total: return B
            return "draw"
        n = len(members) if members else self.jurors
        votesA = sum(1 for _ in range(n) if self.k * gap + random.gauss(0, self.noise) > 0)
        if votesA * 2 > n: return A
        if votesA * 2 < n: return B
        return "draw"


@dataclass
class Venue:
    proof_ethos: float = 0.30
    proof_pathos: float = 0.30
    proof_logos: float = 0.40
    start_ground: str = Stasis.QUALITY
    budget: int = 8
    base_ob: float = 2.0
    win: WinCondition = field(default_factory=lambda: ThresholdRace(5.0))
    faults: DefeatCatalogue = field(default_factory=DefeatCatalogue)
    pressure: Pressure = field(default_factory=Pressure)
    proof_past: float = 1.0       # temporal-register weights; tense_weight() normalizes to a tilt (equal -> neutral)
    proof_present: float = 1.0
    proof_future: float = 1.0
    split_standing: bool = False   # PROTOTYPE: split fused Standing into ascribed Rank + earned Credit (default off)
    allow_rebuttal: bool = False   # PROTOTYPE (Fork 3): permit the rebut move (attrition on opponent adv); default off
    rhetorical: RhetoricalWeights = field(default_factory=RhetoricalWeights)  # 3×3 combinatorial matrix
    def role(self): return {"ethos": self.proof_ethos, "pathos": self.proof_pathos, "logos": self.proof_logos}
    def tense_weight(self):
        w = {"past": self.proof_past, "present": self.proof_present, "future": self.proof_future}
        s = sum(w.values()) or 1.0
        return {k: 3.0 * v / s for k, v in w.items()}   # equal weights -> 1.0 each (zero regression)
    def joint_weight(self, appeal: str, tense: str) -> float:
        """Combinatorial venue weight for (appeal, tense): venue_role × R[appeal][tense] × tfit.
        Replaces the independent res × tfit product in _advance with a single value that
        captures the Aristotelian cross-term (e.g. logos is stronger in past/forensic;
        pathos stronger in future/deliberative). Row sums of R ≈ 3.0 → neutral temporal
        weights leave gain scale unchanged."""
        return self.role()[appeal] * self.rhetorical.weight(appeal, tense) * self.tense_weight()[tense]

class Contestant:
    """Immutable SPEC: faculty, starting standing, reserve cap, evidence items. The Bout builds a fresh
       per-bout runtime (`_Side`) from this and never mutates the spec, so a Contestant is safely reusable
       across bouts. Accepts `dossier=` (its items become the spec) or `evidence=[items]`."""
    def __init__(self, faculty, standing_start=Standing.START, reserve_max=Reserve.MAX, dossier=None,
                evidence=None, charisma=None):
        self.faculty = faculty
        self.standing_start = standing_start
        self.reserve_max = reserve_max
        items = evidence if evidence is not None else (dossier.items if dossier is not None else [])
        self.evidence = tuple(items)
        # Gate-A Face scale-binding (ED-1056): Charisma is a BUILD-TIME attribute (in player
        # control), used only to derive Face_current's ceiling (FaceScale.face_max). Optional —
        # None leaves face_max/face_current unavailable without changing any existing behaviour
        # (Standing/Reserve/readiness/leak are untouched either way).
        self.charisma = charisma

class _Side:
    """Per-bout MUTABLE runtime for one contestant, instantiated from a Contestant spec.
       Accessors (cred_frac / rank_v / build_ethos) are pure pass-throughs when split=False, so the
       fused path is bit-identical to the un-split engine. split=True (opt-in per venue) routes
       readiness+leak through earned Credit and the hard-tactic gate through ascribed Rank."""
    def __init__(self, spec, split=False):
        self.faculty  = spec.faculty
        self.split    = split
        if split:
            self.rank   = Standing(spec.standing_start)   # ascribed station: gates the hard-tactic gradient; not built by ethos
            self.credit = Standing(Standing.START)        # earned credibility: built by ethos/support; drives readiness + leak
        else:
            self.standing = Standing(spec.standing_start) # fused (current engine)
        self.reserve  = Reserve(spec.reserve_max)
        self.fault    = FaultState()
        self.dossier  = Dossier(list(spec.evidence))
        self.charisma = spec.charisma   # Gate-A Face scale-binding (ED-1056); optional, build-time
    def cred_frac(self):      return (self.credit if self.split else self.standing).frac()
    def rank_v(self):         return (self.rank   if self.split else self.standing).v
    def build_ethos(self, m): (self.credit if self.split else self.standing).build(m)
    # ── CR3 canonical tracker accessors (RATIFIED_2026-06-01.md CR3) ──────────────────────
    # Face = the contest-local ethos/standing tracker; canonically it is the fused Standing
    # (or, when split, the earned Credit — the ethos-built component, NOT ascribed Rank).
    # Concentration = the per-move stamina pool (Reserve). These are canonical NAMES over the
    # existing primitives — no new state, so the fused path is bit-identical.
    @property
    def face(self):           return self.credit if self.split else self.standing
    @property
    def concentration(self):  return self.reserve
    # ── Gate-A Face scale-binding (ED-1056, resolved 2026-07-01) ───────────────────────────
    # Derived accessors ON TOP OF the unchanged Face(=Standing) above — they do not read or
    # write Standing.v differently, they only re-express its existing 0–10 value within the
    # Charisma-set ceiling. Standing/Readiness/leak behaviour is bit-identical either way.
    def face_max(self):
        """Face_max = Charisma × 3 (build-time ceiling; unchanged v30-surface formula)."""
        return FaceScale.face_max(self.charisma)
    def face_current(self):
        """Face_current = round(Standing / 10 × Face_max) — Standing (unchanged) determines
           position within the Charisma-set ceiling."""
        return FaceScale.face_current(self.face, self.charisma)

class Bout:
    def __init__(self, ca, cb, venue, adjudicator=None, record=False, armature=None):
        self.c = {A: _Side(ca, venue.split_standing), B: _Side(cb, venue.split_standing)}
        self.v = venue
        self.adj = adjudicator or Adjudicator()
        self.pr = venue.pressure
        self.live = venue.start_ground
        self.room = Room()
        self.state = ContestState()
        self.log = [] if record else None   # opt-in beat trace for narrative.summarize; None => no recording
        # ── Stage 3 / Gate C — the ADJUDICATOR ARMATURE (opt-in; None => armature adds nothing) ──
        # `armature` is an ArmatureConfig (armature.py) carrying, per side, the chosen Contest Style and
        # the judge's armature_position(s). When present, _apply adds (a) the Style×armature_position
        # CONTINUOUS δσ leverage to the net_boost μ-shift term (the σ-space channel, not the rounded pool —
        # judge finding 5), and (b) the CR4 +1D primary-genre POOL die when the chosen Style's genre matches
        # the live stasis's primary genre; and fires the CR5 self-Face backfire on a deg==0 Obscuring foul.
        # None (the default) leaves BOTH the armature AND CR4 contributing nothing — CR4 keys on the orator's
        # CHOSEN GENRE (the Style card), which lives on the armature, so with no armature there is no 'chosen
        # genre' to match (judge finding 1). This makes the armature=None golden-trace agôn path byte-
        # identical to the pre-Stage-3 engine (parity restored — see _kernel_tests).
        self.armature = armature

    def _view(self, side, i):
        c, opp = self.c[side], self.c[other(side)]
        return ContestView(
            live_ground=self.live, appeal_axis=Appeal.ALL,
            my_standing=c.rank_v(), opp_standing=opp.rank_v(),
            can_hard=c.reserve.can("hard"), reserve_frac=c.reserve.cur / (c.reserve.max or 1),
            i=i, n=self.v.budget,
            leading=self.state.adv[side] > self.state.adv[other(side)],
            audience_learned=self.adj.learned, audience_hostile=self.adj.hostile,
            evidence_available=len(c.dossier.available(self.live)))

    def _reception(self, side, pool_bonus=0.0, dsigma_bonus=0.0):
        c = self.c[side]
        # ── Stage 3 / Gate C: TWO distinct additive channels, per CR6 (POOL die vs δσ leverage) ──
        # `pool_bonus` — the CR4 primary-genre +1D (rhetoric.primary_genre_pool_bonus): an INTEGER POOL
        #   die (params/contest.md §Genre and Orientation Bonus Dice "+1D"), added to the Argue pool BEFORE
        #   the roll. CR4 is a whole die, so the pool (rounded to an integer die count) is its correct home.
        # `dsigma_bonus` — the ARMATURE alignment (armature.ArmatureConfig.dsigma): a CONTINUOUS δσ-LEVERAGE
        #   μ-shift, added to the net_boost leverage term (the σ-space channel), NOT the pool. CR6 SPECIFIES
        #   δσ for setup/audience-boost advantages ("audience boost … accumulate as δσ, tanh soft-capped,
        #   uniform probability impact"); the armature is such an advantage. Routing it through δσ (not the
        #   pool) is the judge-finding-5 fix: a fractional pool bonus rounds away in roll_net's
        #   max(1,int(round(pool))) floor (making the wired armature a 0.5-threshold CATEGORICAL step),
        #   whereas net_boost's μ-shift is NOT rounded, so off-axis 0.15 alignment produces a real, non-zero,
        #   continuous net boost (flat < misaligned < aligned holds behaviorally).
        # Both default 0.0 → byte-identical to Stages 0-2 (evidence and rebut receptions pass no bonus; a
        # bonus-less argue is unchanged). Neither is a resonance/resistance multiplier; the two prior
        # parallel armature channels are deleted (judge findings 3/4/6).
        pool = Pool.size(c.faculty) + max(0.0, pool_bonus)
        lev = Leverage.net(c.faculty, on_ground=True) + max(0.0, dsigma_bonus)   # armature δσ enters the CR6 leverage term (continuous μ-shift, not the rounded pool)
        net = roll_net(pool) + net_boost(lev, pool)             # σ-leverage as mu-shift (ED-884/934): base_ob untouched, Ob floor never breached
        return degree(net, self.v.base_ob, pool)                # pool-aware degree -> σ-gated Overwhelming; effective_ob now display-only

    def _bias(self, side):
        if self.pr.toward != side: return 1.0
        return 1.0 + self.pr.institutional * INST_BIAS + self.pr.public * PUB_BIAS

    def _advance(self, side, magnitude, appeal, ground, readiness=True, build=True):
        """Shared scorer. Argument (magnitude=deg): readiness-gated and builds its resource. Evidence
           (magnitude=weight·corroboration): HARD proof — readiness-independent, builds nothing; its
           value is the hidden weight weighted by how much this adjudicator credits that proof."""
        appeal = appeal or Appeal.LOGOS
        if appeal not in Appeal.ALL:
            raise ValueError(f"unknown appeal {appeal!r}; valid: {Appeal.ALL}")
        c = self.c[side]
        tense = Stasis.tense(ground)
        leak = min(Resonance.LEAK_CAP, Resonance.leak(self.adj.discipline, c.cred_frac())
                   + self.pr.public * PUBLIC_LEAK)
        venue_w = self.v.joint_weight(appeal, tense)          # rhetorical × temporal × venue-role — combined
        res = max(RES_FLOOR, (1 - leak) * venue_w + leak * self.adj.character().get(appeal, 0.0))
        # NB (Stage 3 / Gate C): the adjudicator armature and the CR4 primary-genre bonus do NOT touch
        # `res` here. CR4's +1D enters the POOL and the armature's δσ enters the net_boost leverage term,
        # both in _reception — two distinct additive channels per CR6 (an integer pool die vs a continuous
        # δσ leverage; judge finding 5), not a resonance multiplier on `res`. The prior multiplicative
        # res *= (1 + resonance_uplift) armature path was a SECOND, uncited channel and has been removed
        # (judge findings 3/4/6); the prior fractional-pool armature was rounded away (judge finding 5).
        rdy = Readiness.of(c.cred_frac(), self.room.frac(side)) if readiness else 1.0
        gain = MERIT_SCALE * magnitude * res * rdy * random.uniform(1 - JITTER, 1 + JITTER) * self._bias(side)
        self.state.adv[side] += gain
        if build and appeal == Appeal.ETHOS:
            c.build_ethos(magnitude)
        elif build and appeal == Appeal.PATHOS:
            self.room.build(side, magnitude)

    def _apply(self, side, mv):
        if mv.kind not in VALID_KINDS:
            raise ValueError(f"unknown Move.kind {mv.kind!r}; valid: {VALID_KINDS}")
        c = self.c[side]; opp = self.c[other(side)]
        if mv.kind == "pass" or not c.reserve.can(mv.kind):
            c.fault.yields += 1
            c.fault.reason = "declined to answer (ananubhasana)" if mv.kind == "pass" else "no reply left, reserve spent (apratibha)"
            c.reserve.regroup(); return
        c.reserve.spend(mv.kind)
        if mv.kind == "support":
            c.reserve.regroup(); c.build_ethos(1); return
        if mv.kind == "shift":
            g = mv.ground
            if g is None:               c.fault.contradicted = True; c.fault.reason = "abandoned the question (pratijna-hani)"; return
            if not Stasis.is_ground(g): raise ValueError(f"unknown stasis ground {g!r}")
            if Stasis.stronger_than(g, self.live): self.live = g
            else:                                  c.fault.contradicted = True; c.fault.reason = "incoherent reframe (apasiddhanta)"
            return
        if mv.kind == "evidence":
            idx = c.dossier.best(self.live)          # best unpresented RELEVANT item (hidden value)
            if idx is None:                          # nothing relevant to present — refund the spend, no gain
                c.reserve.cur = min(c.reserve.max, c.reserve.cur + Reserve.COST["evidence"]); return
            item, factor = c.dossier.present(idx)
            mag = min(item.weight * factor, EVIDENCE_CAP)   # audit R4: cap the one readiness-free channel
            self._advance(side, mag, item.appeal, item.ground, readiness=False, build=False)   # hard proof; value hidden
            return
        if mv.kind == "rebut":                               # Fork 3 (PROTOTYPE): contest the opponent's case
            if not self.v.allow_rebuttal:                    # off-limits here -> treated as arguing off the live issue
                c.fault.evasion += 1; c.fault.reason = "rebuttal not permitted in this venue (arthantara)"; return
            deg = self._reception(side)                      # reception-gated like an argument
            if deg >= 2:                                     # a landed rebuttal erases up to REBUT_CAP of opp adv, floored at 0
                tgt = other(side)
                self.state.adv[tgt] = max(0.0, self.state.adv[tgt] - min(REBUT_CAP, float(deg)))
            return
        # advance / hard (argument — stochastic reception)
        if not SelfGating.licit(mv.kind, c.rank_v(), opp.rank_v(), self.adj.learned, self.adj.hostile):
            c.fault.barred = True; c.fault.reason = "overreach not licensed by standing (chala/jati)"; return
        if mv.ground is None or not Stasis.is_ground(mv.ground):
            raise ValueError(f"advance/hard requires a valid ground, got {mv.ground!r}")
        if not Stasis.relevant(mv.ground, self.live):
            c.fault.evasion += 1; c.fault.reason = "argued off the live issue (arthantara)"; return
        # ── Stage 3 / Gate C: TWO distinct additive channels (CR6: an integer POOL die vs a δσ leverage) ──
        # Computed here and passed to _reception so they enter resolution BEFORE the roll.
        #   CR4 (pool_bonus — an INTEGER +1D pool die; params/contest.md §Genre and Orientation Bonus Dice):
        #        +1D when the orator's CHOSEN GENRE (the genre of the Style-card the orator picked —
        #        rhetoric.genre_of_style; NOT the move's ground, which the resolver forces onto the live
        #        issue) matches the LIVE stasis's primary genre (rhetoric.primary_genre_pool_bonus). Keying
        #        on the CHOSEN genre (not the ground) is the judge-finding-1 fix: because Stasis.relevant
        #        already forces mv.ground == self.live, keying the +1D on genre_of_ground(mv.ground) was a
        #        TAUTOLOGY (the ground's genre == its own primary genre) that erased the orator's Style
        #        choice. CR4's strategic half IS that choice — pick a Memory (Precedent/Suppression) or
        #        Projection (Vision/Insinuation) stance and be rewarded iff it matches what the terrain makes
        #        primary. So CR4 is now armature-gated (no chosen Style → no 'chosen genre' → no +1D), which
        #        also restores byte-identical parity on the armature=None golden-trace path.
        #   ARMATURE (dsigma_bonus — a CONTINUOUS δσ leverage μ-shift; opt-in, only with an armature):
        #        Style×armature_position alignment (armature.ArmatureConfig.dsigma), gated off in asymmetric
        #        proceedings. Routed through the net_boost δσ term (NOT the pool) so sub-die alignment is not
        #        rounded away (judge finding 5).
        from .rhetoric import primary_genre_pool_bonus, genre_of_style, cr5_self_backfire
        pool_bonus = 0.0
        dsigma_bonus = 0.0
        if self.armature is not None:
            chosen_genre = genre_of_style(self.armature.style_of(side))   # CR4 'chosen genre' = the chosen Style's genre
            pool_bonus = primary_genre_pool_bonus(chosen_genre, self.live)
            dsigma_bonus = self.armature.dsigma(side, self.adj)
        deg = self._reception(side, pool_bonus=pool_bonus, dsigma_bonus=dsigma_bonus)
        if deg >= 1:                                         # partial (1) gives a small gain; 0=failure still nothing
            self._advance(side, deg, mv.appeal, mv.ground)
        # ── Stage 3 / Gate C: CR5 self-Face BACKFIRE on a deg==0 Obscuring FOUL (nigrahasthāna) ──
        # (RATIFIED_2026-06-01.md CR5; Nyāya nigrahasthāna self-gating.) A LANDED Obscuring move (deg>=1,
        # including a deg==1 partial that ADVANCED the mover's own track above) advances/plants as before
        # (params/contest.md §Interaction Types Doubt Marker, ratified Gate B ED-1060) — no self-cost. An
        # Obscuring move that lands NOWHERE (deg==0 — a genuine argumentative foul, a nigrahasthāna)
        # strips the mover's OWN Face by min(−2, its own Face) (rhetoric.CR5_BACKFIRE_MAGNITUDE, anchored
        # to the Doubt Marker −2 but applied to the 0–10 Face stat AND BOUNDED BY THE MOVER'S STANDING —
        # judge finding 4). Judge finding 7: the cost attaches ONLY to the deg==0 foul, NOT to a partial
        # success that helped the mover. Eristic-has-a-cost self-gating: obstruction is BOUNDED BY YOUR OWN
        # STANDING (Nyāya §5.3; reconciliation_map §1.3 "gated by SelfGating.licit") — the strip cannot
        # exceed the Face you hold, so a low-standing orator's foul costs proportionally less. Touches ONLY
        # the failed-foul side — the Direct-vs-Direct CLASH/REINFORCE/CROSS/TIE merits path is untouched
        # (scope item 2). Opt-in: fires only when the Bout carries an armature with cr5 enabled and an
        # Obscuring style this side.
        if self.armature is not None and self.armature.cr5:
            style_key = self.armature.style_of(side)
            if style_key is not None:
                # STANDING-BOUNDED backfire (judge finding 4): pass the mover's OWN Face so the strip is
                # bounded by its standing (Nyāya "obstruction is bounded by your own standing", F7
                # self-gating; reconciliation_map §1.3 "gated by SelfGating.licit"). A high-standing orator
                # risks the full −2; a low-standing orator (Face < 2) risks only what it holds.
                backfire = cr5_self_backfire(style_key, landed=(deg >= 1), my_standing=c.face.v)
                if backfire > 0.0:
                    # strip_points (NOT strip): a FIXED-point penalty, so the REALIZED Face delta equals
                    # the standing-bounded magnitude exactly (judge finding 3: strip(2.0) scaled by
                    # STRIP=0.8 applied only −1.6, a cited≠applied anti-fabrication violation). The
                    # magnitude is already bounded by the mover's Face (judge finding 4), and strip_points
                    # floor-clamps at 0. Face == Standing; the CR3 strip channel, wired here (CR5).
                    c.face.strip_points(backfire)
                    c.fault.reason = "eristic recoiled — a failed obscuring move landed nowhere and cost your own face (nigrahasthana)"

    def resolve(self, polA, polB):
        pol = {A: polA, B: polB}
        for i in range(self.v.budget):
            for side in (A, B):
                mv = pol[side](self._view(side, i))
                if self.log is not None:
                    before = self.state.adv[side]
                    f0 = (self.c[side].fault.evasion, self.c[side].fault.yields,
                          self.c[side].fault.contradicted, self.c[side].fault.barred)
                self._apply(side, mv)
                if self.log is not None:
                    f1 = (self.c[side].fault.evasion, self.c[side].fault.yields,
                          self.c[side].fault.contradicted, self.c[side].fault.barred)
                    self.log.append(dict(i=i, side=side, kind=mv.kind, appeal=mv.appeal, ground=mv.ground,
                                         gain=self.state.adv[side] - before, live=self.live,
                                         advA=self.state.adv[A], advB=self.state.adv[B],
                                         fault=(self.c[side].fault.reason if f1 != f0 else None)))
                hit = self.v.faults.check({A: self.c[A].fault, B: self.c[B].fault})
                if hit:
                    loser, reason = hit
                    detail = self.c[loser].fault.reason
                    return (other(loser), f"clinch:{reason}" + (f" - {detail}" if detail else ""))
            w = self.v.win.resolve(self.state, closing=False, adj=self.adj)
            if w:
                return (w, "win")
        w = self.v.win.resolve(self.state, closing=True, adj=self.adj)
        return (w, "draw" if w == "draw" else "win")

def run(ca, cb, venue, adjudicator, polA, polB):
    return Bout(ca, cb, venue, adjudicator).resolve(polA, polB)
