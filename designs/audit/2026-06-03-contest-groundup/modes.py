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
                 win=ProofBar(bar=2.0), faults=DefeatCatalogue(), **o)
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
                 win=GraceThreshold(5.5), faults=DefeatCatalogue(barred=False, evasion_strikes=0), **o)

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


# ─────────────────────────────────────────────────────────────────────────────
# CROSS-CULTURAL VENUES — six new presets from comparative historical research
# (Roman contio, medieval inquisition, canonical excommunication, Byzantine/imperial
# petition, Venetian secret council, Chinese/Japanese remonstrance). Sources and
# mechanical grounding documented in the venue reference document; DOIs in the commit.
#
# Valorian names and world consequences: [Jordan] — as with the institutional modes,
# the Valorian identity of each venue is authored-layer; names here are structural.

def public_oration_venue(**o):
    """Competitive epideictic display before a large crowd (Roman contio, Byzantine Hippodrome,
    Athenian ekklesia display oration). pathos-dominant — the crowd is moved by emotion —
    with strong ethos secondary; present-tense register; TallyAtClose (who wins the room).
    No rebuttal: each orator delivers set speeches, not adversarial exchange.
    No device bar: all rhetorical instruments are permitted before a popular audience.
    The room mechanic is central: pathos accumulation moves the crowd, which feeds readiness.
    Sources: Mouritsen in Steel & van der Blom (2013) doi:10.1093/acprof:oso/9780199641895.003.0005;
    Beck in Gray et al. (2018) doi:10.1093/oso/9780198788201.003.0017 (laudatio funebris as
    'emotional economies, not content'); Meier (2016) doi:10.1111/emed.12152 (Hippodrome ceremony).
    [SEED] all numeric values."""
    return Venue(proof_ethos=.30, proof_pathos=.50, proof_logos=.20, start_ground=Stasis.QUALITY,
                 proof_past=.15, proof_present=.65, proof_future=.20,
                 win=TallyAtClose(), faults=DefeatCatalogue(barred=False), **o)

def inquisition_hearing_venue(**o):
    """Asymmetric proceeding: the inquisitor (A) must accumulate evidence to ProofBar(3.0);
    the accused (B) defends against the threshold being crossed. Lower bar than civil court (4.0)
    because fama already attaches — public suspicion is treated as partial proof. One evasion
    strike (not two): a single attempt to deflect the question is treated as a point of defeat.
    Logos-dominant (evidence required — two witnesses OR confession per Gratian's Decretum);
    ethos secondary (character and community reputation weight heavily); past-weighted (the
    charge is about what was done). Full fault catalogue: the accused cannot use procedural
    tricks; the inquisitor, by structural position, almost never evades.
    The accusatorial vs inquisitorial asymmetry (the inquisitor initiates AND judges) was a
    noted tension in canonical jurisprudence and produced the 'paradox of due process'
    (Eichbauer 2014 doi:10.1111/hic3.12130; Taliadoros 2018 doi:10.1111/1467-9809.12520).
    [SEED] all numeric values."""
    return Venue(proof_ethos=.30, proof_pathos=.15, proof_logos=.55, start_ground=Stasis.FACT,
                 proof_past=.65, proof_present=.25, proof_future=.10,
                 win=ProofBar(bar=2.5),
                 faults=DefeatCatalogue(barred=True, contradiction=True,
                                        evasion_strikes=1, yield_strikes=2), **o)

def excommunication_court_venue(**o):
    """Ecclesiastical censure proceeding: a Panel of clerics determines whether the accused
    has forfeited community membership. ethos-dominant (the highest ethos weight in any venue —
    the entire question is who you ARE before God and the community); past-weighted (the
    charges are about past conduct and continuing disposition).
    High ProofBar (3.0): canonical procedure required substantial proof and three prior citations
    with opportunities to recant before spiritual exclusion could be declared (Clarke 2007, cited
    in Nederman 2011 doi:10.1111/j.1467-9809.2010.01002.x). The community's participation —
    isolation, 'pollution' language, collective enforcement — is the mechanism of the sanction's
    force (Rice 2023 doi:10.1111/1750-0206.12678). No device bar is removed — the Church does
    enforce procedural purity (barred=True); however, emotion (pathos 0.25) plays a real role
    as the community's reaction to the accused's demeanour shifts the panel.
    [SEED] all numeric values."""
    return Venue(proof_ethos=.50, proof_pathos=.25, proof_logos=.25, start_ground=Stasis.FACT,
                 proof_past=.55, proof_present=.30, proof_future=.15,
                 win=ProofBar(bar=3.0),
                 faults=DefeatCatalogue(barred=True, contradiction=True,
                                        evasion_strikes=2, yield_strikes=2), **o)

def imperial_petition_venue(**o):
    """Appeal to absolute sovereign authority (Byzantine audientia, Chinese imperial memorial,
    Japanese daimyo petition). Near-equal proof weights: the sovereign has no institutional
    preference for argument type — resonance is ENTIRELY driven by their personal character
    leaking in (default adjudicator: discipline ≈ 0, so adj.character dominates almost fully).
    GraceThreshold(8.0): the sovereign's favour is extraordinarily difficult to command;
    the bar is higher than any other petition venue.
    Present-tense register (the oration is about NOW — the relationship, the moment of address).
    No device bar (supplicants may use any means before the throne); evasion fault disabled
    (desperate digression is tolerated — the sovereign is not an institution).
    Sources: Meier (2016) doi:10.1111/emed.12152 (adventus/audientia ceremony); Leonte (2025)
    doi:10.1111/rest.12980 (Byzantine court rhetoric as ideology vehicle). For the Chinese
    imperial memorial: Liao & Chen (2009) doi:10.1111/j.1944-9720.2009.01050.x (citations of
    classic texts as primary rhetorical proof); Wang (2010) doi:10.1111/j.1747-9991.2010.00312.x
    (self-sacrifice as proof of sincerity before imperial authority).
    [SEED] all numeric values. The adjudicator profile (discipline, character) is authored by Jordan."""
    return Venue(proof_ethos=.35, proof_pathos=.35, proof_logos=.30, start_ground=Stasis.QUALITY,
                 proof_past=.25, proof_present=.50, proof_future=.25,
                 win=GraceThreshold(bar=5.5),
                 faults=DefeatCatalogue(barred=False, contradiction=True,
                                        evasion_strikes=0, yield_strikes=3), **o)

def secret_council_venue(**o):
    """Venetian Council of Ten model: cold deliberation, no public oratory, documentary proof,
    rapid decision without consultation. logos=0.75, same weight as the scholastic disputation —
    arguments are evaluated as pure documents, stripped of rhetorical performance. A low threshold
    ThresholdRace(3.0): the Council acts swiftly in urgent matters 'without further consultation'
    (Machiavelli, cited in Geuna 2015 doi:10.1111/raju.12078). The procedural bar is enforced
    (barred=True): rhetorical manipulation is detected and penalised by a deliberating council.
    evasion_strikes=1: deflection is fatal here — the council demands answers. Neutral temporal
    (no tense weighting): cold deliberation does not favour any temporal register.
    Adjudicator: small Panel of 5, all high-discipline, neutral character (the Venetian ideal
    of civic virtue over personal preference — Comino et al. 2020 doi:10.1111/joie.12223).
    [SEED] all numeric values."""
    return Venue(proof_ethos=.15, proof_pathos=.10, proof_logos=.75, start_ground=Stasis.FACT,
                 win=VoteAtClose(jurors=5, sharpness=0.6, noise=0.8),
                 faults=DefeatCatalogue(barred=True, contradiction=True,
                                        evasion_strikes=1, yield_strikes=2), **o)

def memorial_remonstrance_venue(**o):
    """Confucian court memorial / Japanese samurai remonstrance (Hagakure tradition).
    A single official addresses sovereign power at personal risk, invoking historical precedent
    and moral duty. ethos-dominant (the official's accumulated reputation and loyalty is the
    primary instrument); pathos secondary (emotional demonstration of sincerity — willingness
    to accept death if wrong — is the uniquely East Asian proof strategy); past-weighted (the
    argument is grounded in historical exemplars and past conduct, not future policy).
    GraceThreshold(6.0): the lord must be sufficiently moved to change course; the bar is
    lower than the imperial petition (6.0 vs 8.0) because the remonstrant has standing as
    a loyal retainer. Evasion fault disabled: the remonstrant cannot deflect; they must face
    the lord's response directly (Pascoe 2017 doi:10.1002/jls.21494 on Hagakure's injunction
    that remonstrance that stops short of 'being disliked' is incomplete loyalty). No device
    bar (all emotional means are permitted). Self-contradiction is still fatal — lying before
    a lord is unforgivable. Sources: Kim (2015) doi:10.1111/ajes.12084 (Mencian right to
    speech as ritual qualification of officeholders); Liao & Chen (2009)
    doi:10.1111/j.1944-9720.2009.01050.x (Chinese rhetoric: history + moral precept as proof).
    [SEED] all numeric values. Adjudicator is the lord/sovereign: Jordan sets discipline and character."""
    return Venue(proof_ethos=.45, proof_pathos=.35, proof_logos=.20, start_ground=Stasis.FACT,
                 proof_past=.60, proof_present=.25, proof_future=.15,
                 win=GraceThreshold(bar=5.5),
                 faults=DefeatCatalogue(barred=False, contradiction=True,
                                        evasion_strikes=0, yield_strikes=2), **o)

# Mode constructors for the cross-cultural venues
def public_oration_mode(crowd_size=15, **o):
    """Large crowd Panel (crowd_size ≈ 15 for a meaningful electoral assembly). TallyAtClose."""
    return ContestedMode(venue=public_oration_venue(**o), adjudicator=_default_panel(crowd_size))
def inquisition_mode(**o):
    """Single inquisitor: hostile=True, learned=True, discipline=0.25 (trained theologian, harsh)."""
    from contract import Adjudicator as Adj
    inquisitor = Adj(hostile=True, learned=True, discipline=0.25,
                     char_ethos=0.20, char_pathos=0.15, char_logos=0.65)
    return ContestedMode(venue=inquisition_hearing_venue(**o), adjudicator=inquisitor)
def excommunication_mode(panel_size=7, **o):
    """Panel of ecclesiastical figures: high discipline, logos-leaning character."""
    from contract import Adjudicator as Adj, Panel
    bench = Panel(tuple(Adj(hostile=False, learned=True, discipline=0.75,
                            char_ethos=0.40, char_pathos=0.20, char_logos=0.40)
                        for _ in range(panel_size)))
    return ContestedMode(venue=excommunication_court_venue(**o), adjudicator=bench)
def imperial_petition_mode(**o):
    """Single sovereign: discipline≈0 (character entirely dominant), warm by default [SEED]."""
    from contract import Adjudicator as Adj
    sovereign = Adj(hostile=False, learned=False, discipline=0.05,
                    char_ethos=0.45, char_pathos=0.35, char_logos=0.20)
    return ContestedMode(venue=imperial_petition_venue(**o), adjudicator=sovereign)
def secret_council_mode(council_size=5, **o):
    """Small Panel of cold deliberators: max discipline, neutral character."""
    from contract import Adjudicator as Adj, Panel
    council = Panel(tuple(Adj(hostile=False, learned=True, discipline=0.95,
                              char_ethos=0.34, char_pathos=0.33, char_logos=0.33)
                          for _ in range(council_size)))
    return ContestedMode(venue=secret_council_venue(**o), adjudicator=council)
def memorial_remonstrance_mode(**o):
    """Single lord: medium discipline, ethos-valuing character [SEED — Jordan sets per world]."""
    from contract import Adjudicator as Adj
    lord = Adj(hostile=False, learned=True, discipline=0.40,
               char_ethos=0.50, char_pathos=0.30, char_logos=0.20)
    return ContestedMode(venue=memorial_remonstrance_venue(**o), adjudicator=lord)

CROSS_CULTURAL_VENUES = {          # placeholder keys; Valorian names are Jordan's to assign
    "public_oration": public_oration_mode,
    "inquisition_hearing": inquisition_mode,
    "excommunication_court": excommunication_mode,
    "imperial_petition": imperial_petition_mode,
    "secret_council": secret_council_mode,
    "memorial_remonstrance": memorial_remonstrance_mode,
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
