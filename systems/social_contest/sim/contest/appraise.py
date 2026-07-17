"""
appraise.py — Stage 3 / Gate C: the APPRAISE-REVEAL BOUNDARY for the adjudicator armature_position.

Resolves the player-interaction walkthrough §5 open question (per locked decision 5): "how much of
the `armature_position` dot-product should Appraise be able to reveal, and how much should stay
genuinely hidden?" — deciding, and documenting, the reveal boundary so Stage 6 promotes it rather
than reverse-engineering it (player_interaction_walkthrough_v1 §5).

THE DECISION: PARTIAL REVEAL, fitted onto the EXISTING 4-band Appraise ladder (NOT a new ladder).
An Appraise action reveals PROGRESSIVELY MORE of the judge's armature_position as it rolls better,
but NEVER the full exact Conviction vector — even Overwhelming reveals the DOMINANT axis + a coarse
band, not the precise per-axis weights. The residual (the exact vector) stays genuinely hidden.

WHY PARTIAL, not full or none (the Greif grounding — read the source-research, not the distillation;
designs/audit/2026-06-28-social-contest-deliberation-critique/source-research/renaissance-machination-
games-lens-and-review.md §V.2 self-enforcing vs self-undermining equilibria; -testing-the-model §IX
the liberum-veto):
  • FULL reveal is SELF-UNDERMINING. If Appraise handed the orator the exact armature_position, the
    style choice collapses to a solved lookup — always pick the maximally-aligned style — and the
    armature degrades into a no-decision optimization. That is the self-undermining pole: concentrating
    full information/leverage in one actor's hands collapses the game to the cheapest capture (the
    liberum-veto lesson: maximal individual leverage + no uncertainty ⇒ hold-up/capture). A verdict
    you can always game is not robust; it is captured.
  • NO reveal fails the legibility lens (the user's core pain is opacity) — the player would bet blind
    forever, and the armature would never become a legible in-play surface.
  • PARTIAL reveal is SELF-ENFORCING and robust (Padgett–Ansell robust action / multivocality): the
    orator learns ENOUGH to make the style choice a real, informed BET (consequence-legible), but not
    so much that it is a lookup — the residual uncertainty is what keeps the verdict emergent from
    argument-meets-judge rather than pre-solved. This is the Greif self-enforcing pole: the judge's
    convictions are a stable, partly-legible property you argue TO, not a knob you flip.

THE HIDDEN RESIDUAL IS LEGITIMATE TENSION, NOT AN OPACITY BUG (walkthrough §5, explicit): "an
adjudicator with unknown convictions is a legitimate source of tension, not an opacity bug — this is
the one place 'hidden' is correct, and the antagonist should distinguish it from an opacity finding."
The opacity mandate is satisfied by surfacing the CONSEQUENCE CLASS at every band (even a failed
Appraise yields a — deliberately misleading — read, never a null), while the exact vector stays hidden
by design. Consequence surfaced ≠ number revealed (walkthrough §0 design principle).

FITS THE EXISTING LADDER (walkthrough §2 Step 1 / params/contest.md §Pools degree-of-success ladder,
PP-614/ED-893) — this is the SAME 4-band information-gathering shape already used to read the OPPONENT,
now pointed at the JUDGE's armature_position; it does NOT introduce a new information mechanic:
  Failure (0)      → a MISLEADING read (a wrong dominant axis) — the real cost of a bad Appraise, not null.
  Partial (1)      → the judge's REGISTER: whether it leans Revealing/open or Obscuring/implied (an
                     orientation-level hint — the coarsest true signal; mirrors the opponent-Appraise
                     "they lean toward directness" partial band).
  Success (2)      → the judge's DOMINANT armature AXIS (which of Evidence/Consequence/Authority/
                     Insinuation it is most moved by) — enough to pick a plausibly-aligned style.
  Overwhelming (3+)→ the dominant axis + a COARSE BAND on its strength (low/medium/high) — the
                     opponent-Appraise "numeric resistance / a concrete tell" analogue, but STILL a
                     band, never the exact weights. The exact per-axis vector is NEVER revealed.

This is the judge-facing analogue of the Overwhelming-Appraise reveal (npc_behavior_v30.md:387
"Contest Appraise step (Overwhelming: one Belief revealed per §4 social_contest_v30.md)"), extended
to surface the judge's primary Resonant Style per critique adjudicator FG-3 ("Extend the Overwhelming-
Appraise reveal to surface the judge's primary Resonant Style") — the SAME reveal shape, now surfacing
the ADJUDICATOR's dominant axis, capped so the residual stays hidden. (Citation points at the live :387
Appraise-step prose + the FG-3 critique; the empty section is §6.1 "Appraise Revelation" — judge findings 5/8.)
"""
from __future__ import annotations

from typing import Dict, Optional, Tuple

from .armature import ArmatureAxis, ArmaturePosition


# The 4-band Appraise ladder (params/contest.md §Pools degree-of-success; walkthrough §2 Step 1).
# 0 failure / 1 partial / 2 success / 3+ overwhelming.
APPRAISE_FAILURE = 0
APPRAISE_PARTIAL = 1
APPRAISE_SUCCESS = 2
APPRAISE_OVERWHELMING = 3

# The reveal boundary decision, as a documented policy record (flagged for Jordan in the DESIGN doc).
APPRAISE_REVEAL_BOUNDARY = {
    "decision": "PARTIAL REVEAL, fitted onto the existing 4-band Appraise ladder — Appraise reveals "
                "progressively more of the judge's armature_position (register → dominant axis → "
                "dominant axis + coarse strength band) but NEVER the exact per-axis Conviction vector; "
                "the exact weights stay genuinely hidden by design.",
    "why": "FULL reveal is self-undermining (the style choice collapses to a solved lookup ⇒ the judge "
           "is trivially capturable — the liberum-veto/Greif self-undermining pole); NO reveal fails "
           "the opacity/legibility lens; PARTIAL reveal is self-enforcing/robust (Padgett–Ansell robust "
           "action: the orator bets informed, the residual uncertainty keeps the verdict emergent).",
    "hidden_is_legitimate": "The residual (exact vector) is LEGITIMATE TENSION, not an opacity bug "
                            "(walkthrough §5): the consequence CLASS is surfaced at every band (even a "
                            "failed Appraise returns a — misleading — read, never null), but the exact "
                            "weights are hidden by design. Consequence surfaced ≠ number revealed.",
    "ladder": {
        "failure": "a MISLEADING dominant-axis read (real cost of a bad Appraise, not null)",
        "partial": "the judge's REGISTER (Revealing-leaning vs Obscuring-leaning) — coarsest true signal",
        "success": "the judge's DOMINANT armature axis (Evidence/Consequence/Authority/Insinuation)",
        "overwhelming": "dominant axis + a COARSE strength band (low/medium/high); NEVER the exact vector",
    },
    "open_fork_for_jordan": "The boundary (partial vs full vs none) is a genuine design-authority call. "
                            "Best-grounded: PARTIAL (above). Alternatives flagged: FULL reveal (rejected "
                            "— self-undermining) and NO reveal (rejected — opacity). Also open: whether "
                            "Overwhelming should reveal the SECOND axis too (a richer read) — implemented "
                            "as dominant-axis-only to keep the residual meaningfully hidden.",
    "source": "player_interaction_walkthrough_v1 §5 (open question) + §2 Step 1 (4-band ladder); "
              "npc_behavior_v30.md:387 (Overwhelming-Appraise reveal shape, reused judge-facing) + critique adjudicator FG-3; "
              "renaissance-machination-games-lens §V.2 (Greif self-enforcing/undermining) + "
              "renaissance-testing-the-model §IX (liberum-veto); critique adjudicator FG-3",
}

# Coarse strength bands for the Overwhelming reveal — a BAND, never the exact weight (that is the
# hidden residual). [SEED] thresholds on a 0..1 armature axis weight.
_STRENGTH_LOW = 0.34    # [SEED] < → "low" band
_STRENGTH_HIGH = 0.67   # [SEED] ≥ → "high" band; between → "medium"


def _dominant_axis(position: ArmaturePosition) -> Optional[str]:
    """The armature axis the judge is MOST moved by (its heaviest weight). None for the zero vector.
       Ties break by the ArmatureAxis.ALL order (deterministic, no randomness)."""
    vec = position.vector()
    if all(v == 0.0 for v in vec.values()):
        return None
    return max(ArmatureAxis.ALL, key=lambda ax: (vec[ax], -ArmatureAxis.ALL.index(ax)))


def _strength_band(weight: float) -> str:
    """A COARSE band (low/medium/high) on an axis weight — never the exact value (hidden residual)."""
    if weight < _STRENGTH_LOW:
        return "low"
    if weight >= _STRENGTH_HIGH:
        return "high"
    return "medium"


# The register of each armature axis (for the Partial-band register read). Evidence/Consequence are
# the Revealing-leaning axes (Precedent/Vision, the open styles target them); Authority/Insinuation
# are the Obscuring-leaning axes (Suppression/Insinuation target them). This mirrors the Style→axis
# map in armature.STYLE_AXIS (npc_behavior_v30.md §1.3 head table, lines 32-42), read back to the orientation register.
_AXIS_REGISTER = {
    ArmatureAxis.EVIDENCE:    "Revealing",   # Precedent (Memory+Revealing) targets it → open register
    ArmatureAxis.CONSEQUENCE: "Revealing",   # Vision (Projection+Revealing) targets it → open register
    ArmatureAxis.AUTHORITY:   "Obscuring",   # Suppression (Memory+Obscuring) targets it → implied register
    ArmatureAxis.INSINUATION: "Obscuring",   # Insinuation (Projection+Obscuring) targets it → implied register
}


def appraise_armature(position: ArmaturePosition, degree: int) -> Dict:
    """Reveal (part of) the adjudicator's armature_position at a given Appraise degree (0..3+), per the
       PARTIAL-REVEAL boundary decision. Returns a dict describing WHAT THE PLAYER SEES at that band —
       progressively more of the position, but NEVER the exact per-axis vector (the residual stays
       hidden by design; walkthrough §5). Mirrors the existing opponent-Appraise 4-band ladder shape
       (params/contest.md §Pools), pointed at the judge.

    Bands (degree):
      0  Failure     → {'band':'failure', 'misleading': True, 'read': <a WRONG dominant axis>}
      1  Partial     → {'band':'partial', 'register': 'Revealing'|'Obscuring'}   (the coarsest true signal)
      2  Success     → {'band':'success', 'dominant_axis': <axis>}
      3+ Overwhelming→ {'band':'overwhelming', 'dominant_axis': <axis>, 'strength': 'low'|'medium'|'high'}
    The exact per-axis weights are in NO band — that is the hidden residual (legitimate tension)."""
    dominant = _dominant_axis(position)
    if degree <= APPRAISE_FAILURE:
        # A misleading read — a WRONG dominant axis (the next axis in order), never null. If the
        # position is the zero vector (no armature), even the failure read is a plausible-but-wrong axis.
        if dominant is None:
            wrong = ArmatureAxis.ALL[0]
        else:
            i = ArmatureAxis.ALL.index(dominant)
            wrong = ArmatureAxis.ALL[(i + 1) % len(ArmatureAxis.ALL)]
        return {"band": "failure", "misleading": True, "read": wrong,
                "note": "a deliberately misleading read — the real cost of a bad Appraise (never null)"}
    if degree == APPRAISE_PARTIAL:
        register = _AXIS_REGISTER[dominant] if dominant is not None else None
        return {"band": "partial", "register": register,
                "note": "the judge's register (open/Revealing vs implied/Obscuring) — coarsest true signal"}
    if degree == APPRAISE_SUCCESS:
        return {"band": "success", "dominant_axis": dominant,
                "note": "the judge's dominant armature axis — enough to pick a plausibly-aligned style"}
    # Overwhelming (3+): dominant axis + a COARSE strength band; NEVER the exact vector.
    if dominant is None:
        return {"band": "overwhelming", "dominant_axis": None, "strength": None,
                "note": "no armature to read (flat/degenerate adjudicator)"}
    strength = _strength_band(position.vector()[dominant])
    return {"band": "overwhelming", "dominant_axis": dominant, "strength": strength,
            "note": "dominant axis + a COARSE strength band; the exact per-axis vector stays hidden (residual)"}
