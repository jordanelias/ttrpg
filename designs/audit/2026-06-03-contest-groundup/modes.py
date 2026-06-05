"""
modes.py — institutions as top-down VENUE specs. Each venue supplies its proof-weighting, its
win-condition (what winning IS), and its defeat-catalogue (which faults are fatal). The primitives
are identical across them; only the imposed conditions differ.

  court        — tribunal: logos-weighted, ProofBar (burden of proof on the challenger), full
                 nigrahāsthana faults.
  disputation  — debate: logos-weighted, ThresholdRace, full faults.
  assembly     — deliberative: pathos-weighted, TallyAtClose (the body votes), no device-bar fault.
  appeal       — petition: ethos-weighted, GraceThreshold, deference faults (no device-bar, no
                 evasion clinch; silence and self-contradiction still fatal).

Genuinely different sub-systems (dyadic counsel, negotiation, ceremonial) remain scaffolds.
"""
from contract import Adjudicator
from resolver import Contestant, Venue, run, ThresholdRace, TallyAtClose, ProofBar, GraceThreshold
from primitives import Stasis, Standing, DefeatCatalogue

def court_venue(**o):
    return Venue(proof_ethos=.25, proof_pathos=.20, proof_logos=.55, start_ground=Stasis.FACT,
                 proof_past=.60, proof_present=.30, proof_future=.10,   # forensic register: past-weighted (Rhet I.3)
                 win=ProofBar(bar=4.0), faults=DefeatCatalogue(), **o)
def disputation_venue(**o):
    return Venue(proof_ethos=.15, proof_pathos=.10, proof_logos=.75, start_ground=Stasis.FACT,
                 win=ThresholdRace(5.0), faults=DefeatCatalogue(), **o)
def assembly_venue(**o):
    return Venue(proof_ethos=.25, proof_pathos=.50, proof_logos=.25, start_ground=Stasis.CONSEQUENCE,
                 proof_past=.20, proof_present=.20, proof_future=.60,   # deliberative register: future-weighted (Rhet I.3)
                 win=TallyAtClose(), faults=DefeatCatalogue(barred=False), **o)
def appeal_venue(**o):
    # petition: a personal plea, judged by the sovereign's character (no institutional proof-weighting,
    # so resonance comes from the sovereign via leak); grace is not automatic (high bar) and is
    # discretionary — a stern sovereign denies, a merciful one grants.
    return Venue(proof_ethos=.34, proof_pathos=.33, proof_logos=.33, start_ground=Stasis.QUALITY,
                 win=GraceThreshold(7.0), faults=DefeatCatalogue(barred=False, evasion_strikes=0), **o)

VENUES = {"court": court_venue, "disputation": disputation_venue,
          "assembly": assembly_venue, "appeal": appeal_venue}

class ContestedMode:
    def __init__(self, venue="disputation", adjudicator=None, **overrides):
        self.venue = VENUES[venue](**overrides) if isinstance(venue, str) else venue
        self.adj = adjudicator or Adjudicator()
    def play(self, fa, fb, polA, polB, sa=Standing.START, sb=Standing.START, da=None, db=None):
        return run(Contestant(fa, sa, dossier=da), Contestant(fb, sb, dossier=db), self.venue, self.adj, polA, polB)

class DyadicMode:
    """SCAFFOLD. Steer one listener; success invisible; win = the listener adopts the course. To build."""
    def play(self, *a, **k): raise NotImplementedError("dyadic counsel is a separate sub-system — scaffold only")
class NegotiationMode:
    """SCAFFOLD. Typed envoy latitude, escalating instruments; win = agreement in the overlap. To build."""
    def play(self, *a, **k): raise NotImplementedError("negotiation is a separate sub-system — scaffold only")
class CeremonialMode:
    """SCAFFOLD. Nothing at issue (the corpus's point); builds/spends standing; win = acclamation. To build."""
    def play(self, *a, **k): raise NotImplementedError("ceremonial is a separate sub-system — scaffold only")
