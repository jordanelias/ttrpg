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
from contract import Adjudicator, Panel
from resolver import Contestant, Venue, run, ThresholdRace, TallyAtClose, ProofBar, GraceThreshold, VoteAtClose
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


# ─────────────────────────────────────────────────────────────────────────────
# INSTITUTIONAL REGIMES (fork-enabled) — the three modes from the historical
# reconciliation (research 2026-06-04). MECHANICS ONLY: each fixes a win-condition,
# a proof/temporal register, and the rebuttal gate; the four presets above stay the
# fused baseline, untouched. The Valorian IDENTITY of each venue — its name, who sits
# in judgement, what is at stake in-world — is authored-layer, Jordan's to assign; the
# keys here are STRUCTURAL PLACEHOLDERS naming the mechanism, not the world.
#
# Axis the reconciliation turned on: does the running momentum (the room) also decide
# the verdict, or is the verdict a separate terminal act?
#   fused_arbiter           — momentum IS the verdict; one judge; no rebuttal (epideictic
#                             display). ~ a princely court: favour accrues and favour decides.
#   deliberative_body       — momentum and verdict SEPARATE: running adv is the room, a Panel
#                             casts a terminal vote with per-juror variance (VoteAtClose), rebuttal
#                             licit; the vote can cross the room. ~ a republican council (Diodotus
#                             v. Cleon, Thuc. 3.36-49).
#   scholastic_disputation  — fused tally-to-threshold + full nigrahāsthana faults + rebuttal licit
#                             (adversarial exchange / altercatio). ~ a canon-law / university disputation.
# [SEED] every numeric below (proof weights, thresholds, jury noise, panel size) — Jordan to calibrate.

def _default_panel(n=7):
    """A neutral bench of n judges. For VoteAtClose only the COUNT n bears on the vote (the variance is
       the per-juror noise, not per-juror character); the members' characters still drive the running
       adv via the bench's mean disposition. Specific benches are authored; this default is a [SEED]."""
    return Panel(tuple(Adjudicator() for _ in range(n)))

def fused_arbiter_venue(**o):
    # momentum = verdict; one judge; epideictic display (present-tense register, Rhet I.3); no rebuttal.
    return Venue(proof_ethos=.40, proof_pathos=.35, proof_logos=.25, start_ground=Stasis.QUALITY,
                 proof_past=.10, proof_present=.70, proof_future=.20,
                 win=TallyAtClose(), faults=DefeatCatalogue(), allow_rebuttal=False, **o)

def deliberative_body_venue(noise=1.0, jurors=7, **o):
    # momentum != verdict: running adv is the room; a Panel votes at close with per-juror variance;
    # rebuttal licit; deliberative future-tense register (Rhet I.3). Pair with a Panel (see the mode).
    # NOTE: cross-session REVERSIBILITY of the verdict (the Mytilene pattern) is a strategic-layer
    # mechanic, not a within-bout one — flagged here, not implemented at bout scope.
    return Venue(proof_ethos=.20, proof_pathos=.40, proof_logos=.40, start_ground=Stasis.CONSEQUENCE,
                 proof_past=.20, proof_present=.20, proof_future=.60,
                 win=VoteAtClose(jurors=jurors, noise=noise), faults=DefeatCatalogue(barred=False),
                 allow_rebuttal=True, **o)

def scholastic_disputation_venue(**o):
    # fused tally-to-threshold + full nigrahāsthana faults + rebuttal licit (altercatio); logos-dominant.
    return Venue(proof_ethos=.15, proof_pathos=.15, proof_logos=.70, start_ground=Stasis.DEFINITION,
                 win=ThresholdRace(5.0), faults=DefeatCatalogue(), allow_rebuttal=True, **o)

def single_arbiter_mode(**o):
    return ContestedMode(venue=fused_arbiter_venue(**o), adjudicator=Adjudicator())
def deliberative_body_mode(panel_size=7, noise=1.0, **o):
    return ContestedMode(venue=deliberative_body_venue(noise=noise, jurors=panel_size, **o),
                         adjudicator=_default_panel(panel_size))
def scholastic_disputation_mode(**o):
    return ContestedMode(venue=scholastic_disputation_venue(**o), adjudicator=Adjudicator())

INSTITUTIONAL_MODES = {            # placeholder keys (mechanism, not world); Jordan assigns Valorian names
    "fused_arbiter": single_arbiter_mode,
    "deliberative_body": deliberative_body_mode,
    "scholastic_disputation": scholastic_disputation_mode,
}


class DyadicMode:
    """SCAFFOLD. Steer one listener; success invisible; win = the listener adopts the course. To build."""
    def play(self, *a, **k): raise NotImplementedError("dyadic counsel is a separate sub-system — scaffold only")
class NegotiationMode:
    """SCAFFOLD. Typed envoy latitude, escalating instruments; win = agreement in the overlap. To build."""
    def play(self, *a, **k): raise NotImplementedError("negotiation is a separate sub-system — scaffold only")
class CeremonialMode:
    """SCAFFOLD. Nothing at issue (the corpus's point); builds/spends standing; win = acclamation. To build."""
    def play(self, *a, **k): raise NotImplementedError("ceremonial is a separate sub-system — scaffold only")
