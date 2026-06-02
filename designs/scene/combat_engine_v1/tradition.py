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
  footwork  — geometric position emphasis (compases / FoV)
A weight of 1.0 = neutral; >1 emphasises that channel, <1 de-emphasises. Weights are RELATIVE biases applied to the
substrate channels the engine already computes; they re-weight, they do not add new physics.
"""

# Each tradition: channel emphasis (multiplicative bias, neutral=1.0) + the named-set it expresses (bridge mapping).
# Seeded from the bridge's explicit set<->tradition mapping and the throughlines master cross-reference.
TRADITIONS = {
    # German Liechtenauer — Bind Fighter: tactile/Fuhlen + leverage in the bind; Indes timing. (bridge: Bind Fighter)
    'german':   dict(visual=0.95, tactile=1.35, precommit=1.00, leverage=1.30, tempo=1.10, measure=1.05, footwork=1.00,
                     set='Bind Fighter', mode='tactile'),
    # Italian (Fiore->Bolognese->rapier) — Thrust Duelist: temporal-spatial; tempo + measure + visual. (bridge: Thrust Duelist)
    'italian':  dict(visual=1.20, tactile=1.00, precommit=1.00, leverage=0.95, tempo=1.30, measure=1.25, footwork=1.05,
                     set='Thrust Duelist', mode='temporal-spatial'),
    # Spanish Destreza — geometric: measure off the circulo + footwork; visual. (throughlines: geometric mode)
    'spanish':  dict(visual=1.15, tactile=0.95, precommit=1.00, leverage=0.95, tempo=1.05, measure=1.35, footwork=1.30,
                     set='Thrust Duelist', mode='geometric'),
    # Japanese koryu — consciousness/intent: the finest pre-commitment tier (sen-sen-no-sen) + tactile. (bridge: sen)
    'japanese': dict(visual=1.05, tactile=1.15, precommit=1.35, leverage=1.05, tempo=1.20, measure=1.10, footwork=1.10,
                     set='Counter-time', mode='intentional'),
    # Chinese — energetic + reach/thrust (qiang the deepest spear corpus); fa jin burst. (bridge: Burst ~ fa jin)
    'chinese':  dict(visual=1.05, tactile=1.20, precommit=1.05, leverage=1.15, tempo=1.05, measure=1.20, footwork=1.15,
                     set='Burst', mode='kinetic-rhythmic'),
    # Filipino FMA — flow: kinetic-rhythmic continuous-flow; tactile (hubud) + footwork. (bridge: Continuous-flow)
    'filipino': dict(visual=1.00, tactile=1.25, precommit=1.05, leverage=1.00, tempo=1.15, measure=1.05, footwork=1.25,
                     set='Continuous-flow', mode='kinetic-rhythmic'),
    # English (Silver) — true-times biomechanical: fast-part-first, anti-overcommit; measure. (throughlines: biomech)
    'english':  dict(visual=1.10, tactile=1.05, precommit=1.00, leverage=1.05, tempo=1.15, measure=1.15, footwork=1.10,
                     set='Counter-time', mode='biomechanical'),
    # Neutral / untrained baseline — no tradition emphasis (all channels 1.0). Used for stat-only fighters.
    'none':     dict(visual=1.00, tactile=1.00, precommit=1.00, leverage=1.00, tempo=1.00, measure=1.00, footwork=1.00,
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
