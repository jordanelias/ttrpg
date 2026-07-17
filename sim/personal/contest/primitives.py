"""
primitives.py — the general, emergent substrate. Same across venues; the venue (top-down) shapes
how they resolve. Numbers are [SEED]s. N-collapse applied: standing/room feed ONLY readiness (and
standing feeds leak); the inert standing/room → reception-leverage coupling is removed (the audit
toggle showed readiness carries the build payoff). DefeatCatalogue is venue-configured.
"""
from dataclasses import dataclass
from .contract import A, B
from engine.autoload.sigma_leverage import level   # Stage 1b: single-sourced σ-kernel (was local engine.py)

class Stasis:
    FACT, DEFINITION, QUALITY, JURISDICTION = "fact", "definition", "quality", "jurisdiction"
    CONSEQUENCE, FEASIBILITY = "consequence", "feasibility"   # deliberative/future grounds (Aristotle Rhet I.4-8)
    LADDER = [FACT, DEFINITION, QUALITY, JURISDICTION, CONSEQUENCE, FEASIBILITY]
    # intrinsic temporal orientation: the genre's question carries the tense (forensic past, deliberative future)
    TENSE = {FACT: "past", DEFINITION: "past", QUALITY: "present", JURISDICTION: "present",
             CONSEQUENCE: "future", FEASIBILITY: "future"}
    @staticmethod
    def is_ground(g):                       return g in Stasis.LADDER
    @staticmethod
    def relevant(move_ground, live_ground): return move_ground == live_ground
    @staticmethod
    def stronger_than(a, b):                return Stasis.LADDER.index(a) > Stasis.LADDER.index(b)
    @staticmethod
    def tense(g):                           return Stasis.TENSE.get(g, "present")

class Appeal:
    ETHOS, PATHOS, LOGOS = "ethos", "pathos", "logos"
    ALL = (ETHOS, PATHOS, LOGOS)

class Standing:
    LO, HI, START = 0.0, 10.0, 5.0
    BUILD, STRIP = 0.8, 0.8  # [SEED]
    def __init__(self, start=START): self.v = start
    def build(self, deg): self.v = min(self.HI, self.v + self.BUILD * deg)
    def strip(self, deg): self.v = max(self.LO, self.v - self.STRIP * deg)
    def strip_points(self, points):
        """Strip a FIXED number of Standing/Face POINTS directly (0–10 scale), NOT a degree scaled by
           STRIP. `strip(deg)` scales a degree-of-success by STRIP (0.8) — a per-move argue channel;
           `strip_points(p)` subtracts p Face points as-applied, so the REALIZED delta equals p exactly
           (judge finding 3: the CR5 backfire's cited −2 magnitude must equal the applied Face delta —
           passing 2.0 to strip(deg) applied only 0.8×2=1.6). Floor-clamped at LO. Returns the realized
           (clamped) delta so the caller/tests can assert cited == applied."""
        before = self.v
        self.v = max(self.LO, self.v - points)
        return before - self.v
    def frac(self):       return min(1.0, max(0.0, (self.v - self.START) / (self.HI - self.START)))

class Reserve:
    MAX = 12  # [SEED]
    COST = {"advance": 3, "hard": 5, "shift": 4, "support": 2, "pass": 0, "evidence": 3, "rebut": 3}
    REGAIN = 4
    def __init__(self, mx=MAX): self.max = mx; self.cur = mx
    def can(self, kind):   return self.cur >= self.COST[kind]
    def spend(self, kind): self.cur = max(0, self.cur - self.COST[kind])
    def regroup(self):     self.cur = min(self.max, self.cur + self.REGAIN)

# ---------------------------------------------------------------------------
# CR3 — THE THREE TRACKERS (RATIFIED_2026-06-01.md CR3; DECISIONS.md reconciliation
# row "Standing/Reserve/Room/Readiness | Composure/Concentration | CR3 | three
# trackers: Concentration+Face+Persuasion; Composure retired").
#
# CR3 retires the single Composure buffer and splits its two conflated roles onto two
# distinct per-side trackers, alongside the preserved Persuasion merits clock:
#
#   canonical CR3 name    role (CR3)                 kernel primitive it BINDS TO
#   ------------------    ----------------------     ----------------------------
#   Face                  contest-local ethos /      Standing (per-side; built by
#                         standing (TRANSIENT)       ethos moves; feeds Readiness+leak)
#   Concentration         stamina (per-exchange      Reserve (per-side; spent per move;
#                         depletion; regroup refills) regroup() refills)
#   Persuasion Track      merits clock (PRESERVED)    ContestState.adv -> PersuasionTrack
#                         0-10 banded, two-pole       (resolver.py; canonical bands)
#
# CR3 is a NAMING + role binding over the ALREADY-BUILT groundup primitives — NOT a new
# mechanic and NOT a special case: `Face` IS `Standing` (the exact same Python class), exposed
# under its canonical CR3 name so the v30 surface and the tests can address the tracker by the
# ratified name. The mechanical substrate is unchanged (Stage 1d is behaviour-preserving); the
# change is that the contest now has a NAMED Face tracker where canon previously had "Composure".
#
# SCOPE HONESTY (Stage 1d, judge-upheld): what is established here is the NAME + registry + test
# surface, NOT a fully realized two-sided resource. The underlying Standing IS live in resolution
# (ethos-build raises it; it feeds Readiness + leak), but Standing.strip() is NEVER called in the
# contest kernel — Face has NO strip/strain channel wired, so it is monotonic-up. The v30-surface
# "strain -> Rattled -> -1D Argue pool" behaviour and the RATIFIED_2026-06-01 omega line-20
# stamina/standing/merits two-sided tradeoff (+ CR5 Face-attack/self-backfire) are NOT realized
# here; they are Stage-3 (rhetoric-armature) scope. Do not read `Face = Standing` as a claim that
# the v30 Charisma*3 (3-21) strain-buffer and this 0-10 ethos-built scale are the same magnitude —
# they are two representations of "Face" whose scale-binding is an OPEN DECISION for Jordan (see
# social_contest_v30 §4 Step 6 "two representations of Face" note).
#
# Composure-retirement blast radius: SCOPED TO THE SOCIAL-CONTEST TRACKER ONLY (per the
# Stage-1d scope guardrail; CR3 targets "Composure-as-buffer" in the contest). The kernel
# never modelled a "Composure" primitive, so nothing here touches Composure references in
# unrelated systems (knots / combat / conviction) — see the OPEN-DECISION note on the
# Knot-as-Composure-buffer coupling in social_contest_v30.md §4/§8.
#
# The D0-minor formula note: CR3's inline "Focus*3" for Concentration is the PRE-supersession
# form; the canonical Concentration magnitude is (3*Focus)+(2*Spirit) per the ED-901 (STRUCK
# Focus*3) + ED-902 (corrected coefficients + Cognition->Focus engine fix) + ED-933 (params
# propagation) chain. The kernel's Reserve is an ABSTRACT per-move stamina pool ([SEED] MAX=12,
# per-move COST) — it does not hard-code any attribute formula; the (3*Focus)+(2*Spirit)
# magnitude is the v30-surface value the wrapper/params carry, not a kernel literal.

# Face IS Standing: the canonical CR3 name for the contest-local ethos/standing tracker.
# (Alias, not a subclass — same identity, so isinstance/behaviour are bit-identical and no
# code path is special-cased for "Face" vs "Standing".)
Face = Standing

# ---------------------------------------------------------------------------
# FACE SCALE-BINDING (Gate-A RESOLVED, 2026-07-01; ED-1056 update): a combo formula, not a
# straight rescale either direction. Standing itself (its 0–10 representation, its ethos-build
# mechanics via .build()/.strip(), and its existing feed into Readiness/leak) is UNCHANGED by
# this resolution — FaceScale only ADDS a derived accessor on top of it:
#
#   Face_max     = Charisma × 3            (unchanged v30-surface formula, params/contest.md
#                                            §Derived Values / ED-127; the retired Composure
#                                            magnitude, range 3–21) — a build-time attribute,
#                                            in player control (Charisma is chosen at creation).
#   Face_current = round(Standing / 10 × Face_max)
#                                            Standing (the kernel 0–10 ethos-built value, earned
#                                            through play, NOT directly in player control
#                                            moment-to-moment) determines POSITION WITHIN that
#                                            ceiling.
#
# No new invented constants: this reuses the existing Cha×3 formula (already canonical) and the
# existing 0–10 Standing range (Standing.LO..Standing.HI, already canonical) — it only combines
# them. Charisma is NOT kernel state (the contest kernel has no Charisma attribute; `faculty` is
# an abstract pool-size parameter, not Charisma) — FaceScale is a pure function taking Charisma
# as an argument, so it adds a derived VIEW, not new mutable state, and Standing.v is never
# touched by it.
class FaceScale:
    """Derived Face_current accessor over an unchanged Standing (Gate-A Face scale-binding,
       ED-1056). Standing stays the single source of truth (0–10, ethos-built, feeds
       Readiness/leak, untouched); FaceScale only reads it and re-expresses it within the
       Charisma-set ceiling."""
    @staticmethod
    def face_max(charisma):
        """Face_max = Charisma × 3 (unchanged v30-surface ceiling formula; params/contest.md
           §Derived Values, ED-127). Build-time attribute — set by the player at creation,
           not by moment-to-moment play."""
        return charisma * 3
    @staticmethod
    def face_current(standing, charisma):
        """Face_current = round(Standing / 10 × Face_max). `standing` is the kernel 0–10 value
           (a Standing instance or a bare float/int .v); Standing.HI (10) is the fixed divisor
           per the existing kernel range — Standing itself is read-only here, never mutated."""
        v = standing.v if isinstance(standing, Standing) else standing
        return round(v / Standing.HI * FaceScale.face_max(charisma))

# The CR3 tracker registry: canonical name -> (kernel primitive it binds to, role, whether
# it is per-side, provenance). Read by the surface/tests to assert the three-tracker model is
# wired and that Composure is absent (retired) as a kernel primitive.
TRACKERS = {
    "Face":            {"binds": Standing,      "role": "contest-local ethos/standing (transient)",
                        "per_side": True,  "source": "CR3 (RATIFIED_2026-06-01.md)"},
    "Concentration":   {"binds": Reserve,       "role": "stamina (per-exchange depletion; regroup refills)",
                        "per_side": True,  "source": "CR3 (RATIFIED_2026-06-01.md); Reserve is a [SEED] "
                                                       "abstract per-move pool (MAX=12, per-move COST), NOT a "
                                                       "hard-coded attribute formula — the v30-surface "
                                                       "(3×Focus)+(2×Spirit) magnitude (ED-901/ED-902/ED-933) is "
                                                       "carried by params/contest.md + wrapper.py, not this class"},
    "PersuasionTrack": {"binds": "ContestState.adv -> PersuasionTrack",
                        "role": "merits clock (0-10 banded, two-pole; PRESERVED)",
                        "per_side": False, "source": "CR3 (preserved) + params/contest.md §Persuasion Track"},
}
# Composure is RETIRED as a contest tracker (CR3). It is NOT a kernel primitive and must not
# reappear as one; the guard below is asserted by the kernel suite.
RETIRED_TRACKERS = ("Composure",)

# ---------------------------------------------------------------------------
# Rhetorical–Temporal matrix — the combinatorial cross of the three appeals
# with the three temporal registers (Aristotle Rhet. I.3; verified 2026-06-05).
# Each entry is a MODIFIER centred on 1.0 (row sums = 3.0, so neutral temporal
# weights → zero scale change). The matrix replaces the independent product
# venue_role[appeal] × tfit with a venue-specific joint weight.
#
# Defaults (Aristotelian):
#   Forensic / PAST   : logos-dominant (evidence, what happened)
#   Epideictic / PRESENT : ethos-dominant (character, praise/blame)
#   Deliberative / FUTURE : pathos-dominant (fear/hope, moving to action)
#
# All nine entries are [SEED] — Jordan to calibrate.
@dataclass
class RhetoricalWeights:
    """3×3 modifier matrix for (appeal, tense). Row sums = 3.0 → average modifier
    is 1.0 per appeal, preserving gain scale on neutral venues. Applied as:
      joint = venue_role[appeal] × R[appeal][tense] × tfit[tense]
    Aristotelian defaults grounded in Rhet. I.3 (forensic/past=logos;
    epideictic/present=ethos; deliberative/future=pathos). [SEED]"""
    # LOGOS — forensic home; weakest in deliberative
    logos_past:    float = 1.20   # [SEED] forensic evidence/fact
    logos_present: float = 1.00   # [SEED] epideictic demonstration
    logos_future:  float = 0.80   # [SEED] deliberative policy argument
    # ETHOS — epideictic home; credibility matters less in raw deliberation
    ethos_past:    float = 0.85   # [SEED] witness/character standing in past
    ethos_present: float = 1.20   # [SEED] reputation/honour display
    ethos_future:  float = 0.95   # [SEED] trustworthy advisor
    # PATHOS — deliberative home; emotional weight matters least in cold evidence
    pathos_past:   float = 0.85   # [SEED] victim impact / retrospective grief
    pathos_present: float = 0.90  # [SEED] epideictic affect / pride/shame
    pathos_future: float = 1.25   # [SEED] fear / hope / desire for future benefit

    def weight(self, appeal: str, tense: str) -> float:
        """Return the modifier for (appeal, tense). Row sums ≈ 3.0."""
        return getattr(self, f"{appeal}_{tense}", 1.0)

class Pool:
    BASE = 3  # [SEED]
    @staticmethod
    def size(faculty): return max(5, faculty * 2 + Pool.BASE)

class SelfGating:
    MARGIN = 1.0  # [SEED]
    @staticmethod
    def _hard_licensed(my, opp, learned, hostile):
        return (opp < my - SelfGating.MARGIN) and (not learned or hostile)
    @staticmethod
    def licit(kind, my, opp, learned, hostile):
        return SelfGating._hard_licensed(my, opp, learned, hostile) if kind == "hard" else True

class Leverage:
    """δσ into the reception roll. N-collapsed: faculty (skill) + on-ground (terrain) only.
       Standing/room no longer feed the roll — they feed readiness (their one role)."""
    ONGROUND = level("moderate")
    READING_COEFF = 1/6    # exact 1/6 — 0.167 was a decimal approximation that gave lev=-0.001 at fac=1
    @staticmethod
    def net(faculty, on_ground):
        d = (faculty - 4) * Leverage.READING_COEFF
        return d + Leverage.ONGROUND if on_ground else d

class Room:
    CAP = 3.0  # [SEED] pathos's target; feeds readiness
    def __init__(self):         self.r = {A: 0.0, B: 0.0}
    def build(self, side, deg): self.r[side] = min(self.CAP, self.r[side] + 0.5 * deg)
    def frac(self, side):       return self.r[side] / self.CAP

class Resonance:
    """How much a proof moves THIS adjudicator HERE = blend(role, character) by leak.
       leak rises as discipline is low and as built ethos draws the judge toward character."""
    ETHOS_UNLOCK = 0.5  # [SEED]
    LEAK_CAP = 0.9      # [SEED]
    @staticmethod
    def leak(discipline, standing_frac):
        return min(Resonance.LEAK_CAP, max(0.0, (1.0 - discipline) + Resonance.ETHOS_UNLOCK * standing_frac))
    @staticmethod
    def effective(appeal, role_w, char_w, leak):
        return (1 - leak) * role_w.get(appeal, 0.0) + leak * char_w.get(appeal, 0.0)
    @staticmethod
    def tension(role_w, char_w):
        return sum(abs(role_w.get(a, 0.0) - char_w.get(a, 0.0)) for a in Appeal.ALL)

class Readiness:
    """Built support that makes appeals land; floor < 1 so unsupported still moves something."""
    FLOOR = 0.40       # [SEED] raised from 0.35: floor is competitive enough without ethos/pathos investment
    W_STANDING, W_ROOM = 0.40, 0.40  # [SEED] lowered from 0.50: reduces 1.66x amplification to ~1.35x
    @staticmethod
    def of(standing_frac, room_frac):
        r = Readiness.W_STANDING * standing_frac + Readiness.W_ROOM * room_frac
        return Readiness.FLOOR + (1 - Readiness.FLOOR) * min(1.0, max(0.0, r))

class DefeatCatalogue:
    """Venue-configured fault→clinch rules. WHICH faults are fatal, and at what count, is a
       top-down property of the institution: a disputation clinches on the nigrahasthāna (all four);
       a vote disables the rhetorical-device bar; a ceremony has no defeat-conditions at all.
       The general fault *detection* lives in the wrapper; this decides which are *fatal*."""
    def __init__(self, barred=True, contradiction=True, evasion_strikes=2, yield_strikes=2):
        self.barred = barred
        self.contradiction = contradiction
        self.evasion_strikes = evasion_strikes   # 0/None disables
        self.yield_strikes = yield_strikes
    def check(self, faults):
        for side in (A, B):
            f = faults[side]
            if self.barred and f.barred:                                       return (side, "barred-device")
            if self.contradiction and f.contradicted:                          return (side, "self-contradiction")
            if self.evasion_strikes and f.evasion >= self.evasion_strikes:      return (side, "evasion")
            if self.yield_strikes and f.yields >= self.yield_strikes:           return (side, "silence")
        return None


@dataclass
class EvidenceItem:
    """A piece of evidence/testimony. `weight` is the engine's HIDDEN true value (relevance×quality);
       the player never sees it. `appeal` is the proof it bolsters (documentary→logos, a credible
       witness→ethos, a victim's testimony→pathos)."""
    ground: str
    weight: float
    appeal: str = Appeal.LOGOS

class Dossier:
    """A side's evidence. Presenting a RELEVANT item (ground == live stasis) adds its hidden value;
       presenting more relevant evidence is good but with diminishing returns (corroboration
       saturates). Irrelevant evidence has nothing to present. Weights are hidden from the player."""
    CORROB = (1.0, 0.7, 0.5, 0.35)  # [SEED] diminishing returns; beyond → 0.25
    def __init__(self, items=None):
        self.items = list(items or [])
        self.presented = set()
        self.count_on = {}
    def available(self, ground):
        return [i for i, it in enumerate(self.items) if it.ground == ground and i not in self.presented]
    def best(self, ground):
        av = self.available(ground)
        return max(av, key=lambda i: self.items[i].weight) if av else None
    def present(self, idx):
        self.presented.add(idx)
        g = self.items[idx].ground
        k = self.count_on.get(g, 0); self.count_on[g] = k + 1
        factor = Dossier.CORROB[k] if k < len(Dossier.CORROB) else 0.25
        return self.items[idx], factor
