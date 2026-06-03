"""
modes.py — the modes of discourse. Each is a distinct contest with its own framing authority,
decision rule, and win condition; they do not share a win condition. The contested-debate core
(deliberative + forensic) is implemented over the primitives. The genuinely separate sub-systems
are documented scaffolds — declared, not faked, since the corpus says they are different arts.
"""
from resolver import Contestant, Config, run
from primitives import Stasis

class ContestedMode:
    """The contested debate: two sides, an adjudicator, a live stasis ground, merits clock, and the
       defeat-condition checklist. Two flavors share this engine:
         - deliberative: a body decides FUTURE ACTION; opens on QUALITY (is the course advantageous/right).
         - forensic:     a judge weighs a PAST ACT; opens on FACT, defence climbs the ladder; verdict.
       Win = clinch (opponent incurs a defeat-condition) or merits threshold."""
    FLAVORS = {
        "deliberative": dict(start_ground=Stasis.QUALITY, base_ob=2.0),
        "forensic":     dict(start_ground=Stasis.FACT,    base_ob=2.0),
    }
    def __init__(self, flavor="forensic", **overrides):
        cfg = dict(self.FLAVORS[flavor]); cfg.update(overrides)
        self.flavor = flavor
        self.cfg = Config(**cfg)
    def play(self, faculty_a, faculty_b, polA, polB, standing_a=5.0, standing_b=5.0):
        A = Contestant(faculty_a, standing_a); B = Contestant(faculty_b, standing_b)
        return run(A, B, self.cfg, polA, polB)

# ── Distinct sub-systems (scaffolds; the corpus says these are different games) ──
class DyadicMode:
    """SCAFFOLD. Read and steer ONE listener; success is invisible (the course seems self-chosen).
       Loop: scan power+disposition → open/close → desire- or fear-register matched to character.
       Win condition: the listener adopts the course as his own (no audience, no public verdict).
       Composes: Leverage (reading), Standing, Reserve — NOT the public merits clock. To build."""
    def play(self, *a, **k): raise NotImplementedError("dyadic counsel is a separate sub-system — scaffold only")

class AppealMode:
    """SCAFFOLD. Asymmetric, up a power gradient. Two instruments:
       supplique (subject→sovereign, seeks grace; rank-indexed form, deference, intercessor modifies),
       remontrance (institution→Crown, contests a measure; escalation ladder).
       Win condition: grace granted / measure reconsidered. To build."""
    def play(self, *a, **k): raise NotImplementedError("royal appeal is a separate sub-system — scaffold only")

class NegotiationMode:
    """SCAFFOLD. Bounded, reputation-laden exchange: typed envoy latitude, escalating instruments
       (conciliation→concession→division→force), a small set of policy stances.
       Win condition: agreement inside the interest overlap. To build."""
    def play(self, *a, **k): raise NotImplementedError("negotiation is a separate sub-system — scaffold only")

class CeremonialMode:
    """SCAFFOLD. Nothing is at issue (the opposite of a contested case); builds/spends Standing only.
       Win condition: a standing shift / acclamation. To build."""
    def play(self, *a, **k): raise NotImplementedError("ceremonial is a separate sub-system — scaffold only")
