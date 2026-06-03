"""
modes.py — modes of discourse. The contested-debate core (deliberative + forensic) is implemented
over the primitives via the Bout wrapper; the genuinely distinct sub-systems are honest scaffolds.
Flavors differ by opening stasis ground (forensic opens on FACT, the defence climbing the ladder;
deliberative opens on QUALITY — is the course advantageous/right). Fuller win-condition/decision-rule
differentiation between deliberative and forensic is still to design.
"""
from contract import Adjudicator
from resolver import Contestant, Config, run
from primitives import Stasis, Standing

class ContestedMode:
    FLAVORS = {"deliberative": dict(start_ground=Stasis.QUALITY),
               "forensic":     dict(start_ground=Stasis.FACT)}
    def __init__(self, flavor="forensic", adjudicator=None, **overrides):
        self.flavor = flavor
        self.cfg = Config(**{**self.FLAVORS[flavor], **overrides})
        self.adj = adjudicator or Adjudicator()
    def play(self, faculty_a, faculty_b, polA, polB,
             standing_a=Standing.START, standing_b=Standing.START):
        ca = Contestant(faculty_a, standing_a)
        cb = Contestant(faculty_b, standing_b)
        return run(ca, cb, self.cfg, self.adj, polA, polB)

# ── Distinct sub-systems (scaffolds; the corpus says these are different games) ──
class DyadicMode:
    """SCAFFOLD. Read and steer ONE listener; success invisible (the course seems self-chosen).
       Loop: scan power+disposition → open/close → desire/fear register matched to character.
       Win: the listener adopts the course as his own. Composes Leverage/Standing/Reserve, not the
       public merits clock. To build."""
    def play(self, *a, **k): raise NotImplementedError("dyadic counsel is a separate sub-system — scaffold only")

class AppealMode:
    """SCAFFOLD. Asymmetric, up a power gradient. Two instruments: supplique (subject→sovereign,
       seeks grace; rank-indexed, deference, intercessor modifies) and remontrance (institution→Crown,
       contests a measure; escalation ladder). Win: grace granted / measure reconsidered. To build."""
    def play(self, *a, **k): raise NotImplementedError("royal appeal is a separate sub-system — scaffold only")

class NegotiationMode:
    """SCAFFOLD. Bounded, reputation-laden exchange: typed envoy latitude, escalating instruments
       (conciliation→concession→division→force), a small set of policy stances. Win: agreement inside
       the interest overlap. To build."""
    def play(self, *a, **k): raise NotImplementedError("negotiation is a separate sub-system — scaffold only")

class CeremonialMode:
    """SCAFFOLD. Nothing is at issue (the opposite of a contested case); builds/spends Standing only.
       Win: a standing shift / acclamation. To build."""
    def play(self, *a, **k): raise NotImplementedError("ceremonial is a separate sub-system — scaffold only")
