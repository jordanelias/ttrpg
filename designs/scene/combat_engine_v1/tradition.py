"""Tradition module — each martial tradition is a COGNITIVE MODE (a way of reading the same physics), expressed as
selection-weights over the shared substrate primitives, NOT a separate rule-set. The engine always resolves in the
substrate (measure + commitment-window + contact-channel + collision physics); a tradition only biases HOW its
fighter reads/selects, and how well it reads an UNFAMILIAR opponent.

Grounded in designs/audit/2026-05-28-combat-reframe/historical-precedents/ (seven-axes throughlines T2/T3/T6/T7 +
the manual-vs-combat-v32-bridge set<->tradition mapping). Class-C: seeds are tunable, Jordan-vetoable.

Substrate channels a tradition weights (all resolve in the engine's physical substrate):
  visual    — pre-contact anticipation (Cog/Att); the temporal-spatial read
  tactile   — in-bind feeling (Fuhlen / sentimento / ting jin); the contact-as-information channel
  precommit — pre-commitment intent-read (sen-sen-no-sen); finest initiative tier
  leverage  — bind leverage emphasis (Stark/Schwach / winding-over-strength)
  tempo     — commitment-window exploitation (tempo / Indes / sen timing)
  measure   — distance-control emphasis (misura / maai / circulo)
  balance  — geometric position emphasis (compases / FoV)
A weight of 1.0 = neutral; >1 emphasises that channel, <1 de-emphasises. Weights are RELATIVE biases applied to the
substrate channels the engine already computes; they re-weight, they do not add new physics.
"""

# Each tradition: channel emphasis (multiplicative bias, neutral=1.0) + the named-set it expresses (bridge mapping).
# Seeded from the bridge's explicit set<->tradition mapping and the throughlines master cross-reference.
TRADITIONS = {
    # German Liechtenauer — Bind Fighter: tactile/Fuhlen + leverage in the bind; Indes timing. (bridge: Bind Fighter)
    'german':   dict(visual=0.95, tactile=1.35, precommit=1.00, leverage=1.30, tempo=1.10, measure=1.05, balance=1.00,
                     set='Bind Fighter', mode='tactile'),
    # Italian (Fiore->Bolognese->rapier) — Thrust Duelist: temporal-spatial; tempo + measure + visual. (bridge: Thrust Duelist)
    'italian':  dict(visual=1.20, tactile=1.00, precommit=1.00, leverage=0.95, tempo=1.30, measure=1.25, balance=1.05,
                     set='Thrust Duelist', mode='temporal-spatial'),
    # Spanish Destreza — geometric: measure off the circulo + balance; visual. (throughlines: geometric mode)
    'spanish':  dict(visual=1.15, tactile=0.95, precommit=1.00, leverage=0.95, tempo=1.05, measure=1.35, balance=1.30,
                     set='Thrust Duelist', mode='geometric'),
    # Japanese koryu — consciousness/intent: the finest pre-commitment tier (sen-sen-no-sen) + tactile. (bridge: sen)
    'japanese': dict(visual=1.05, tactile=1.15, precommit=1.35, leverage=1.05, tempo=1.20, measure=1.10, balance=1.10,
                     set='Counter-time', mode='intentional'),
    # Chinese — energetic + reach/thrust (qiang the deepest spear corpus); fa jin burst. (bridge: Burst ~ fa jin)
    'chinese':  dict(visual=1.05, tactile=1.20, precommit=1.05, leverage=1.15, tempo=1.05, measure=1.20, balance=1.15,
                     set='Burst', mode='kinetic-rhythmic'),
    # Filipino FMA — flow: kinetic-rhythmic continuous-flow; tactile (hubud) + balance. (bridge: Continuous-flow)
    'filipino': dict(visual=1.00, tactile=1.25, precommit=1.05, leverage=1.00, tempo=1.15, measure=1.05, balance=1.25,
                     set='Continuous-flow', mode='kinetic-rhythmic'),
    # English (Silver) — true-times biomechanical: fast-part-first, anti-overcommit; measure. (throughlines: biomech)
    'english':  dict(visual=1.10, tactile=1.05, precommit=1.00, leverage=1.05, tempo=1.15, measure=1.15, balance=1.10,
                     set='Counter-time', mode='biomechanical'),
    # Neutral / untrained baseline — no tradition emphasis (all channels 1.0). Used for stat-only fighters.
    'none':     dict(visual=1.00, tactile=1.00, precommit=1.00, leverage=1.00, tempo=1.00, measure=1.00, balance=1.00,
                     set=None, mode=None),
}

# Knowledge-of-others: how well a tradition READS an unfamiliar one. 1.0 = full read (own/familiar);
# <1 = degraded read vs an unfamiliar tradition (mis-times their commitment-window, mis-anticipates their openings).
# Default cross-tradition familiarity (the bridge: traditions have PARTIAL knowledge of others). Same-tradition = 1.0.
# Geographically/historically adjacent traditions read each other better than distant ones (seed; Class-C).
FAMILIARITY_DEFAULT = 0.85          # baseline read of any unfamiliar tradition
FAMILIARITY_ADJACENT = 0.93         # adjacent/cross-pollinated traditions
ADJACENT = {                        # pairs that historically exchanged (read each other better)
    frozenset({'german','italian'}), frozenset({'italian','spanish'}), frozenset({'german','english'}),
    frozenset({'italian','english'}), frozenset({'chinese','japanese'}), frozenset({'chinese','filipino'}),
    frozenset({'japanese','filipino'}),
}

# WS-4/WS-5 (section C, flag-gated): each tradition's PREFERRED node — the part of the state graph it fights to
# impose (tradition_decomposition_v1.md). 'bind' = German (the crossing); 'counter' = Italian/Japanese/English
# (the single-time counter, refusing the bind); 'measure' = Spanish (the circulo). none = no preference. Read ONLY
# when cfg['IMPOSITION_GATE'] is on (the imposition experiment) — decoupled from the channel magnitudes.
PREFERRED = {'german': 'bind', 'italian': 'counter', 'spanish': 'measure', 'japanese': 'counter',
             'english': 'counter', 'chinese': 'burst', 'filipino': 'flow', 'none': None}
def preferred(trad):
    return PREFERRED.get(trad)


def familiarity(reader_trad, opponent_trad):
    """How well `reader_trad` reads `opponent_trad`. 1.0 if same or either is 'none' (no tradition to misread)."""
    if reader_trad==opponent_trad: return 1.0
    if reader_trad=='none' or opponent_trad=='none': return 1.0   # no tradition-specific deception to misread
    if frozenset({reader_trad,opponent_trad}) in ADJACENT: return FAMILIARITY_ADJACENT
    return FAMILIARITY_DEFAULT

def profile(trad):
    return TRADITIONS.get(trad, TRADITIONS['none'])

def channel_weight(trad, channel):
    return TRADITIONS.get(trad, TRADITIONS['none']).get(channel, 1.0)

# ─────────────────────────── EQUIPPABLE ABILITIES (scaffold) ───────────────────────────
# Traditions grant equippable abilities that MODULATE the vocabulary (improve a competence or phase-behaviour) — they
# do NOT unlock it. The channel-weights above are the substrate competences; abilities are tradition-learned modulators
# a fighter EQUIPS on top (c.equipped, default empty -> no change -> invariant-safe). Each ability targets a LEVER with
# an op: '+' (additive bonus) or '*' (multiplicative factor).
#
# GROUNDING (provisional; per corpus 10-rewrite): abilities are drawn from the documented martial record and are
# CONFIDENT only for the well-anchored core — German/Italian/Japanese (S1/S2) and Iberian Destreza (S2/S3, flagged).
# The selection-effect lesson is honoured: counterattack-prestige is European/Japanese (not universal), and the
# priority-gap traditions (Polish szabla, Hungarian sabre, Filipino, Chinese-technique, …) get NO ability until an
# S1/S2 anchor exists. 'grade' records the source tier.
#
# LEVER STATUS (corrected 2026-06-28 per the recovered combat-critique; supersedes the prior 'pending' note):
#   the 7 CHANNEL levers ('measure','tempo','leverage','visual','tactile','precommit','balance') ARE wired -
#   eff_cw() is consumed at ~9 live sites - so staerke_schwaeche/misura/atajo are LIVE (calibrate before relying).
#   'counter_success', 'counter_select', 'anti_overcommit' are live. The 'seize' lever is DEAD: its pre-contact
#   consumer was cut 2026-06-05, so 'vorschlag'/'sen_no_sen' do NOTHING when equipped. Do not implement against
#   'seize' (slated for retire-or-reroute in scene-combat WS-4).
ABILITIES = {
    # German (Liechtenauer; S1/S2 — critically edited)
    'indes':          dict(tradition='german',   grade='S1/S2', lever='counter_success', op='+', value=0.15,
                           desc="Indes / Fühlen — feeling the bind, the simultaneous counter in the same tempo"),
    'vorschlag':      dict(tradition='german',   grade='S1/S2', lever='seize',           op='+', value=4.0,
                           desc="Vorschlag — the first-strike that seizes the Vor before the opponent acts [DEAD: 'seize' lever has no consumer since 2026-06-05]"),
    'staerke_schwaeche': dict(tradition='german', grade='S1/S2', lever='leverage',       op='*', value=1.20,
                           desc="Stärke-Schwäche — strong/weak leverage in the bind (channel; pending)"),
    # Italian (Fiore -> rapier; S2)
    'mezzo_tempo':    dict(tradition='italian',  grade='S2',    lever='counter_select',  op='*', value=1.40,
                           desc="Mezzo tempo — the half-time counterattack; reaches for the in-tempo counter more readily"),
    'misura':         dict(tradition='italian',  grade='S2',    lever='measure',         op='*', value=1.15,
                           desc="Misura — distance / measure control (channel; pending)"),
    # Japanese (koryū; S2)
    'sen_no_sen':     dict(tradition='japanese', grade='S2',    lever='seize',           op='+', value=4.0,
                           desc="Sen-no-sen — pre-emptive seizing, taking the initiative as the opponent commits [DEAD: 'seize' lever has no consumer since 2026-06-05]"),
    # English (Silver; S2)
    'true_times':     dict(tradition='english',  grade='S2',    lever='anti_overcommit', op='+', value=0.25,
                           desc="True Times — Silver's true-vs-false times: commitment discipline, fewer over-commits"),
    # Iberian Destreza (S2/S3 — partly reliable; flagged)
    'atajo':          dict(tradition='spanish',  grade='S2/S3', lever='measure',         op='*', value=1.18,
                           desc="Atajo — Destreza blade-constraint / measure off the círculo (channel; pending; S2/S3)"),
}

def ability_bonus(c, lever):
    """Sum of ADDITIVE ('+') modulations for `lever` across the fighter's equipped abilities. Default 0.0 (no change)."""
    tot=0.0
    for name in getattr(c,'equipped',()) or ():
        a=ABILITIES.get(name)
        if a and a['lever']==lever and a['op']=='+': tot+=a['value']
    return tot

def ability_factor(c, lever):
    """Product of MULTIPLICATIVE ('*') modulations for `lever` across the fighter's equipped abilities. Default 1.0."""
    f=1.0
    for name in getattr(c,'equipped',()) or ():
        a=ABILITIES.get(name)
        if a and a['lever']==lever and a['op']=='*': f*=a['value']
    return f

def eff_cw(c, channel):
    """Effective channel weight = substrate (tradition) weight × equipped-ability channel modulators. The channel-lever
    wiring path: replace TR.channel_weight(c.tradition, ch) with TR.eff_cw(c, ch) at the call sites to make channel
    abilities (misura, atajo, Stärke-Schwäche, …) live. Default (no abilities) == channel_weight (invariant-safe)."""
    return channel_weight(c.tradition, channel) * ability_factor(c, channel)
