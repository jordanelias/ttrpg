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
from .contract import Adjudicator, Panel
from .resolver import (Contestant, Venue, run, ThresholdRace, TallyAtClose, ProofBar,
                       GraceThreshold, VoteAtClose, PersuasionTrack)
from .primitives import Stasis, Standing, DefeatCatalogue

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
    from .contract import Adjudicator as Adj
    inquisitor = Adj(hostile=True, learned=True, discipline=0.25,
                     char_ethos=0.20, char_pathos=0.15, char_logos=0.65)
    return ContestedMode(venue=inquisition_hearing_venue(**o), adjudicator=inquisitor)
def excommunication_mode(panel_size=7, **o):
    """Panel of ecclesiastical figures: high discipline, logos-leaning character."""
    from .contract import Adjudicator as Adj, Panel
    bench = Panel(tuple(Adj(hostile=False, learned=True, discipline=0.75,
                            char_ethos=0.40, char_pathos=0.20, char_logos=0.40)
                        for _ in range(panel_size)))
    return ContestedMode(venue=excommunication_court_venue(**o), adjudicator=bench)
def imperial_petition_mode(**o):
    """Single sovereign: discipline≈0 (character entirely dominant), warm by default [SEED]."""
    from .contract import Adjudicator as Adj
    sovereign = Adj(hostile=False, learned=False, discipline=0.05,
                    char_ethos=0.45, char_pathos=0.35, char_logos=0.20)
    return ContestedMode(venue=imperial_petition_venue(**o), adjudicator=sovereign)
def secret_council_mode(council_size=5, **o):
    """Small Panel of cold deliberators: max discipline, neutral character."""
    from .contract import Adjudicator as Adj, Panel
    council = Panel(tuple(Adj(hostile=False, learned=True, discipline=0.95,
                              char_ethos=0.34, char_pathos=0.33, char_logos=0.33)
                          for _ in range(council_size)))
    return ContestedMode(venue=secret_council_venue(**o), adjudicator=council)
def memorial_remonstrance_mode(**o):
    """Single lord: medium discipline, ethos-valuing character [SEED — Jordan sets per world]."""
    from .contract import Adjudicator as Adj
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


# ═════════════════════════════════════════════════════════════════════════════
# CANONICAL v30 RE-SKIN (Stage 1c) — the 8 canonical PROCEEDINGS + 4 canonical
# ADJUDICATOR types, read verbatim from params/contest.md (§Proceeding Types table)
# + social_contest_v30.md §2 (GM Setup) / §3 (Argue Pool). This is a SURFACE re-skin
# over the groundup mechanical substrate above. Every CANONICAL parameter — the 8
# proceedings' {exchanges, roles, resistance modifier, adjudicator type, track start}
# and the 4 adjudicator→primary-attribute mappings — traces to a cited canonical row.
# BUT canon fixes ONLY those; it does NOT specify any adjudicator discipline or
# proof/character profile (social_contest_v30 §2 Step 1 / §3 fix the primary ATTRIBUTE
# only). The discipline/char_* literals in the adjudicator constructors below are
# therefore NOT canonical — they are [SEED] calibration values (Jordan to set), tagged
# as such at each constructor, exactly as the groundup presets above are. The generic
# groundup presets (court / disputation / assembly / appeal / institutional /
# cross-cultural) stay UNTOUCHED as the mechanical library; these are the named
# canonical faces the game exposes.
#
# GM-REMOVAL: canon says "GM SETUP" (§2) but there is no GM in Valoria — the ENGINE
# resolves. The §2 "GM setup" choices (adjudicator type, exchange count, resistance
# modifier, track start) become VENUE-INTRINSIC parameters here, fixed by the named
# proceeding, so the wrapper (wrapper.py) sets them from the proceeding, never a GM.
#
# MAPPING (canonical name  <-  groundup mechanism it re-skins):
#   Adjudicator types (social_contest_v30 §2 Step 1 / §3 Argue Pool):
#     Expert Judge    -> single Adjudicator, primary attribute COGNITION
#     Crowd           -> Panel (collective), primary attribute CHARISMA
#     No Adjudicator  -> single Adjudicator (the parties themselves), primary ATTUNEMENT
#     Panel           -> Panel, primary attribute COGNITION (ED-137 provisional: use Expert Judge)
#   Proceedings (params/contest.md §Proceeding Types  +  social_contest_v30 §2 Step 5):
#     see PROCEEDINGS table below; each carries {exchanges, roles, resistance_mod, adjudicator, track_start}.
#
# Win-condition: ALL canonical proceedings that use the tracker resolve on the canonical
# Persuasion Track banding (params/contest.md §Persuasion Track: >=9 A_total, >=7 A_decisive,
# 4-6 committee, <=3 B_decisive, <=1 B_total). The remainder fall back to exchange-majority
# TallyAtClose (social_contest_v30 §2 Step 4: "If not used, winner determined by exchange majority").
#
# TRACKER TRI-STATE (social_contest_v30 §2 Step 4/5 distinguishes THREE cases; the params/contest.md
# §Proceeding Types table collapses the last two to a bare "N/A", so this reads §2 which carries the
# distinction — scope item 1 mandates reading BOTH sources):
#   "required" — Formal/Grand Contest, Royal Audience, Church Tribunal, Guild Arbitration: the
#                Persuasion Track is always used (adjudicated proceedings).
#   "none"     — Casual Dispute: social_contest_v30:87 "N/A (no tracker)" — the track is never used;
#                always exchange-majority TallyAtClose.
#   "optional" — Private Negotiation, Personal Appeal: social_contest_v30:88-89 "N/A (tracker optional)"
#                + :76 "With no adjudicator (private negotiation, personal appeal): Persuasion Track is
#                optional." The track is AVAILABLE but OFF BY DEFAULT — DEFAULTS to exchange-majority
#                TallyAtClose (so behavior is unchanged), and a caller may opt IN to the tracker via the
#                use_tracker= build param (proceeding_venue/proceeding_mode/build_contest).
# `tracker` (bool) is the DEFAULT-ACTIVE flag the venue builder reads (True => PersuasionTrack by
# default; False => TallyAtClose by default). `tracker_mode` names the canonical tri-state above; only
# "optional" proceedings honour the use_tracker opt-in.

# ── Canonical adjudicator types (social_contest_v30 §2 Step 1 + §3 Argue Pool) ──
# ADJUDICATOR_PRIMARY: the primary attribute the Argue pool doubles, per adjudicator type
# (social_contest_v30 §3 Argue Pool table). This mapping IS canonical. The wrapper reads it
# to build (PrimaryAttr×2)+H.
#
# ⚠ CANON BOUNDARY: canon fixes the primary ATTRIBUTE per adjudicator type and NOTHING ELSE
# about the adjudicator — social_contest_v30 §2 Step 1 (adjudicator table) + §3 (Argue Pool
# table) define no discipline value and no proof/character (ethos/pathos/logos) weighting.
# The `discipline=` and `char_*=` literals in the four constructors below are LIVE in the
# agon resolution path (resolver reads adj.discipline + adj.character()), so they are NOT
# cosmetic — but they are [SEED] calibration values, NOT canon. Each is tagged [SEED] at its
# constructor; Jordan calibrates. (These mirror the discipline/character shape of the groundup
# presets above, which are likewise [SEED].)
ADJUDICATOR_PRIMARY = {
    "expert_judge":   "Cognition",   # §3: "Judge evaluates logical structure"
    "crowd":          "Charisma",    # §3: "Crowd responds to delivery and authority"
    "no_adjudicator": "Attunement",  # §3: "You must read the other party and calibrate"
    "panel":          "Cognition",   # §3 [PROVISIONAL — ED-137: use Expert Judge until designed]
}

def expert_judge(**o):
    """Canonical 'Expert judge' (§2 Step 1): a single authority evaluating on merits; Cognition-primary
       (the ONLY canonical fact — see ADJUDICATOR_PRIMARY). Re-skins a single learned Adjudicator.
       [SEED] discipline=0.75, char_logos/ethos/pathos=0.55/0.25/0.20 (logos-leaning: evaluates logical
       structure) are calibration values, NOT canon — Jordan to set. LIVE in resolution."""
    return Adjudicator(learned=True, discipline=0.75, char_logos=0.55, char_ethos=0.25, char_pathos=0.20, **o)

def crowd(size=15, **o):
    """Canonical 'Crowd' (§2 Step 1): a collective audience reacting to delivery/force; Charisma-primary
       (the ONLY canonical fact). Re-skins a Panel (collective) of pathos/ethos-leaning members.
       [SEED] size=15, discipline=0.30, char_pathos/ethos/logos=0.55/0.30/0.15 are calibration values,
       NOT canon — Jordan to set. LIVE in resolution (shapes the resolved band distribution)."""
    return Panel(tuple(Adjudicator(learned=False, discipline=0.30,
                                   char_pathos=0.55, char_ethos=0.30, char_logos=0.15, **o)
                       for _ in range(size)))

def no_adjudicator(**o):
    """Canonical 'No adjudicator' (§2 Step 1): the parties themselves decide; Attunement-primary
       (the ONLY canonical fact). Re-skins a single low-discipline neutral Adjudicator (character
       leaks — the counterpart is read). [SEED] discipline=0.30, char_ethos/pathos/logos=neutral
       0.34/0.33/0.33 are calibration values, NOT canon — Jordan to set. LIVE in resolution."""
    return Adjudicator(learned=True, discipline=0.30, char_ethos=0.34, char_pathos=0.33, char_logos=0.33, **o)

def panel(size=5, **o):
    """Canonical 'Panel' (§2 Step 1): multiple individual judges deliberating; Cognition-primary
       (the ONLY canonical fact). ED-137 provisional: mechanically use the Expert-Judge profile per
       juror (a bench of expert judges) — so the [SEED] profile is expert_judge's, inherited. [SEED]
       size=5 is a calibration value, NOT canon — Jordan to set. LIVE in resolution."""
    return Panel(tuple(expert_judge(**o) for _ in range(size)))

CANONICAL_ADJUDICATORS = {
    "expert_judge":   expert_judge,
    "crowd":          crowd,
    "no_adjudicator": no_adjudicator,
    "panel":          panel,
}

# ── Canonical Persuasion-Track resistance (params/contest.md §Persuasion Track) ──
# "Audience resistance: average Stability of factions (round up) − 1, minimum 0." The proceeding's
# resistance MODIFIER (Standard / Halved / N/A) scales the base; here it is carried as a proceeding
# attribute (PROCEEDINGS[...]['resistance']) for the wrapper — the numeric resistance is derived from
# world Stability at build_contest time, not fabricated here.
CANONICAL_TRACK_START = 5.0   # params/contest.md §Persuasion Track: "Starting position ... (typical: 5)."
CHURCH_TRIBUNAL_TRACK_START = 6.0  # social_contest_v30 §7: "Persuasion Track starts biased at 6" (accused disadvantaged).

# PROCEEDINGS: the 8 canonical proceeding specs. Every field cites params/contest.md §Proceeding Types
# (Exchanges / Roles / Resistance Mod / Adjudicator) + social_contest_v30 §2 Step 4-5 (track start).
# `exchanges` is a (min, max) pair; the venue budget uses max (the Bout runs up to budget exchanges,
# resolving early on a clinch/threshold). `tracker` (bool) is the DEFAULT-ACTIVE flag (True =>
# PersuasionTrack by default; False => TallyAtClose by default). `tracker_mode` names the canonical
# tri-state ("required"/"none"/"optional" — see header): "optional" proceedings are tracker-OFF by
# default (tracker=False) but honour the use_tracker= opt-in.
PROCEEDINGS = {
    "formal_contest": dict(       # params/contest.md: "Formal Contest | 3 | Alternating | Standard | Crowd"
        exchanges=(3, 3), roles="alternating", resistance="standard",
        adjudicator="crowd", track_start=CANONICAL_TRACK_START, tracker=True, tracker_mode="required"),
    "grand_contest": dict(        # "Grand Contest | 5 | Alternating | Standard | Crowd"
        exchanges=(5, 5), roles="alternating", resistance="standard",
        adjudicator="crowd", track_start=CANONICAL_TRACK_START, tracker=True, tracker_mode="required"),
    "royal_audience": dict(       # "Royal Audience | 3 | Crown objects | Halved for petitioner | Expert Judge"
        exchanges=(3, 3), roles="crown_objects", resistance="halved_petitioner",
        adjudicator="expert_judge", track_start=CANONICAL_TRACK_START, tracker=True, tracker_mode="required"),
    "church_tribunal": dict(      # "Church Tribunal | 1–5 | Inquisitor proposes | Halved for accused | Expert Judge"
        exchanges=(1, 5), roles="inquisitor_proposes", resistance="halved_accused",
        adjudicator="expert_judge", track_start=CHURCH_TRIBUNAL_TRACK_START, tracker=True,
        tracker_mode="required"),  # §7: track starts biased at 6
    "guild_arbitration": dict(    # "Guild Arbitration | 3 | Symmetric | Standard | Panel"
        # ED-1059 REBIND (Jordan, Gate B): adjudicator expert_judge -> PANEL. Closes the original ED-137
        # note ("Panel not yet designed; use Expert Judge as provisional") exactly as it always pointed —
        # Guild Arbitration's canon flavor already says "Masters arbitrate" (plural = a seated bench). No
        # appeal mechanic (Jordan: "let the decision ride"); 8-proceeding roster unchanged. Panel routes to
        # the VoteAtClose weighted-by-standing ballot via build_contest's panel branch (wrapper.py).
        exchanges=(3, 3), roles="symmetric", resistance="standard",
        adjudicator="panel", track_start=CANONICAL_TRACK_START, tracker=True, tracker_mode="required"),
    "casual_dispute": dict(       # "Casual Dispute | 1 | Initiator proposes | N/A | No Adjudicator"
        exchanges=(1, 1), roles="initiator_proposes", resistance="none",  # social_contest_v30:87 "N/A (no tracker)"
        adjudicator="no_adjudicator", track_start=CANONICAL_TRACK_START, tracker=False, tracker_mode="none"),
    "private_negotiation": dict(  # "Private Negotiation | 1–3 | Symmetric | N/A | No Adjudicator"
        exchanges=(1, 3), roles="symmetric", resistance="none",  # social_contest_v30:88 "N/A (tracker optional)"
        adjudicator="no_adjudicator", track_start=CANONICAL_TRACK_START, tracker=False, tracker_mode="optional"),
    "personal_appeal": dict(      # "Personal Appeal | 1 | Appealer proposes | N/A | No Adjudicator"
        exchanges=(1, 1), roles="appealer_proposes", resistance="none",  # social_contest_v30:89 "N/A (tracker optional)"
        adjudicator="no_adjudicator", track_start=CANONICAL_TRACK_START, tracker=False, tracker_mode="optional"),
}

def _use_tracker(spec, use_tracker):
    """Resolve the tri-state tracker choice for a proceeding (social_contest_v30 §2 Step 4/5).
       DEFAULT (use_tracker=None) preserves behavior: `tracker` bool decides (True=>track, False=>tally).
       For a "optional" proceeding (Private Negotiation / Personal Appeal — §2:88-89 "N/A (tracker
       optional)"), a caller may pass use_tracker=True to opt IN to the Persuasion Track, or =False to
       force the exchange-majority fallback. "none" (Casual Dispute — §2:87 "N/A (no tracker)") and
       "required" proceedings reject the opt-in: the tracker is fixed by canon, not the caller."""
    mode = spec.get("tracker_mode", "required" if spec["tracker"] else "none")
    if use_tracker is None:
        return spec["tracker"]                        # behavior-preserving default
    if mode != "optional":
        raise ValueError(f"use_tracker is only honoured by 'optional' proceedings "
                         f"(social_contest_v30 §2:88-89); this proceeding is tracker_mode={mode!r}")
    return bool(use_tracker)

def proceeding_venue(name, *, use_tracker=None, **o):
    """Build the Venue for a canonical proceeding. Exchange count -> venue budget (max of the range).
       Tracker choice is the canonical tri-state (social_contest_v30 §2 Step 4/5): "required" => always
       PersuasionTrack; "none" => always exchange-majority TallyAtClose; "optional" (Private Negotiation
       / Personal Appeal) => TallyAtClose BY DEFAULT, or PersuasionTrack when the caller opts in via
       use_tracker=True. Proof/temporal registers are NOT re-invented — a proceeding inherits the
       groundup default register unless a caller overrides. RESOLVES NOTHING.

       ED-137/ED-1057/ED-1059 PANEL CLOSURE: a proceeding whose adjudicator is 'panel' (Guild Arbitration,
       rebound Gate B) resolves on the terminal per-member VoteAtClose ballot (weighted-by-standing), NOT
       the Persuasion-Track band — so ANY entry point (proceeding_mode here, build_contest in the wrapper)
       yields a coherent Panel venue. The bench-size default is dictionaries.PANEL_DEFAULT_JURORS; at
       resolve time VoteAtClose reads the paired Panel's actual members for count + per-juror weights. Lazy
       import breaks the dictionaries<->modes cycle (dictionaries imports modes)."""
    spec = PROCEEDINGS[name]
    budget = spec["exchanges"][1]
    tracker_on = _use_tracker(spec, use_tracker)   # also validates: required/none proceedings reject opt-in
    if spec["adjudicator"] == "panel":
        from .dictionaries import panel_win_condition
        win = panel_win_condition()   # weighted-by-standing VoteAtClose (ED-1057); reads members at resolve
    elif tracker_on:
        win = PersuasionTrack(start=spec["track_start"])
    else:
        win = TallyAtClose()
    return Venue(budget=budget, win=win, **o)

def proceeding_mode(name, *, use_tracker=None, **o):
    """ContestedMode for a canonical proceeding, pairing its Venue with its canonical adjudicator type.
       `use_tracker` opts an "optional" proceeding in to the Persuasion Track (see proceeding_venue)."""
    adj_key = PROCEEDINGS[name]["adjudicator"]
    adj = CANONICAL_ADJUDICATORS[adj_key]()
    return ContestedMode(venue=proceeding_venue(name, use_tracker=use_tracker, **o), adjudicator=adj)

# The registry the wrapper routes canonical proceeding names through.
CANONICAL_PROCEEDINGS = {name: (lambda n=name, **o: proceeding_mode(n, **o)) for name in PROCEEDINGS}
