"""
rhetoric.py — Stage 3 / Gate C: making the classical/Renaissance grounding MECHANICAL, not nominal.

Two ratified redesign items land here as behaviour, not labels (Lens 6: "the primitive's behavior
must differ the way the source predicts; quoting Aristotle in a comment does not satisfy the lens"):

  CR4  Ciceronian STASIS × GENRE (RATIFIED_2026-06-01.md CR4): stasis (conjectural/definitional/
       qualitative/translative) = TERRAIN; genre (Memory/Projection, authored) = STANCE; stasis sets
       the primary genre; definitional = a HIGHER-ORDER REFRAME (via the authored Present-rendering —
       NOT a genre); translative = pre-merits jurisdiction (the Stay). Grounded in
       rhetoric_oratory_contest_research §1.4 (Hermagoras→Cicero, the four classical stases, translative
       = jurisdiction — session-verified) and confirmed well-founded there.

       GENRE MAP KEYED ON THE STASIS GROUND, NOT ON TENSE (reconciliation_map_raw.md §1.2 res(1)-(4)):
       the stasis→primary-genre map below is built on CR4's four classical stases (the GROUND), NOT on
       the kernel's internal Stasis.TENSE tag. §1.2 explicitly forbids TENSE as the genre intermediary
       ("a groundup-internal rhetorical-weight tag with no canonical standing; CR4 supersedes it") and
       rules that definitional/DEFINITION → NOT Memory (it is a reframe operator, "never collapsed to a
       genre"). Only conjectural/FACT sets Memory; CONSEQUENCE/FEASIBILITY → Projection (contract-
       endorsed, deliberative-future); QUALITY (qualitative) and JURISDICTION (translative) carry no
       primary genre. TENSE still drives RhetoricalWeights / venue temporal weighting (its legitimate
       role), but it is NOT the genre intermediary here.

  CR5  ORIENTATION re-grounded (RATIFIED_2026-06-01.md CR5): Direct → moves Persuasion (merits, as now);
       Indirect → attacks opponent FACE (ethos) WITH a self-Face BACKFIRE on failure. Grounded in the
       Nyāya nigrahasthāna (defeat-conditions) self-gating machinery: a rule-violating / over-reaching
       obstruction move is penalised WITHIN the game (a "point of defeat"), bounded by your OWN standing
       — Quintilian's vir bonus / Nyāya jalpa-vitaṇḍā (rhetoric_oratory_contest_research §5.1, §5.3, §9.1
       "Licit tactics are bounded by your own standing"; critique fallacies FG-2). This is the fallacy-
       as-foul the pragma-dialectics lens demands: eristic has a COST (critique §2.6).

       CR5 SCOPE — RATIFIED (Jordan, Gate C, 2026-07-02; ED-1062): keep the Gate-B Doubt Marker
       (landed Obscuring, ED-1060) and this module's self-Face backfire (failed Obscuring, deg==0)
       TOGETHER — both pieces together ARE the full CR5 realization, not two conflicting mechanics. The
       opponent-Face-attack question (whether a landed Obscuring move should also strip the OPPONENT's
       Face stat directly, retiring the Doubt Marker) is RESOLVED: no — the Doubt Marker already fills
       that role, so a separate Face-stat attack would double up rather than complete CR5.

The EPIDEICTIC question (Aristotle's THIRD genre — praise/blame, present-tense, audience-as-spectator)
is addressed in EPIDEICTIC_COMPRESSION below (scope item 1): is the 2-genre (Memory/Projection)
compression silently dropping it? Answer, grounded: NO — the epideictic REGISTER survives in the
RhetoricalWeights *_present column (ethos_present, the ethos-dominant praise/blame home, live in
_advance's joint_weight), the ceremonial basilikos-logos register (research §2.2). Only the genre
LABEL compresses 3→2 (PP-234). RATIFIED (Jordan, Gate C, 2026-07-02): the register-not-genre home is
ACCEPTED — the 2-genre grid stays and epideictic survives only via the ethos_present/praise-blame
register, not as a first-class genre (ED-1062; see EPIDEICTIC_COMPRESSION["decision_for_jordan"] below).
  NB (judge finding 3): this claim does NOT rest on equating the qualitative STASIS with the epideictic
  GENRE. The research doc distinguishes them: qualitative (quale sit — "was it justified?") is a FORENSIC
  EVALUATION stasis (§1.4), whereas epideictic is a present-tense PRAISE/BLAME GENRE (§1.2); §0.4
  explicitly downgrades the "honourable=deliberative/forensic" conflation ("the honourable/shameful is
  the epideictic axis, not the deliberative one … do not treat the six-item list as confirmed canon").
  The epideictic-survives argument therefore anchors ONLY on the defensible surfaces — RhetoricalWeights
  ethos_present + the §2.2 basilikos logos ceremonial register — NOT on a qualitative=epideictic identity.

SCOPE GUARDRAILS (Stage 3 / Gate C):
  • CR5 does NOT change CLASH/REINFORCE/CROSS/TIE for Direct-vs-Direct exchanges — it ONLY adds the
    self-Face backfire consequence for an Obscuring move that FAILS AS A MOVE (reception degree 0 — a
    genuine nigrahasthāna/foul), against the mover's own Face (scope item 2). A LANDED Obscuring move
    (deg >= 1, including a deg==1 partial that advanced the mover's own track) is NOT a foul and does
    NOT backfire (judge finding 7).
  • The backfire ANCHORS its −2 magnitude to the Doubt Marker precedent (params/contest.md §Interaction
    Types: "Doubt Marker … −2 …") rather than inventing a fresh number — but applies it to a DIFFERENT
    quantity (the 0–10 Face/Standing credibility stat, not the Doubt Marker's track-margin), so the −2
    is a magnitude PRECEDENT, not a claim the two −2s measure the same thing (judge finding 7).
  • The backfire is BOUNDED BY THE MOVER'S OWN STANDING — min(−2, own Face) (judge finding 4): the
    RATIFIED CR5 carry-across (reconciliation_map §1.3) requires it "gated by SelfGating.licit (your own
    Face caps your obstruction — F7)", realizing the cited "obstruction is bounded by your own standing"
    (research §5.3/§9.1). The prior flat −2 (no standing dependence) did NOT realize that invariant.
  • The exact Face-cost anchor (equal to the track −2 vs re-scaled to the credibility stat), and a deeper
    standing-SCALING variant (cost grows with standing, not just caps at it), are Class-B design-authority
    forks flagged for Jordan in the DESIGN doc.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

from .primitives import Stasis
from .dictionaries import Genre, Orientation, STYLES_TABLE

# A move's genre is keyed on its stasis GROUND (reconciliation_map_raw.md §1.2 res(1)-(4)), NOT on the
# kernel's Stasis.TENSE tag (which §1.2 forbids as the genre intermediary). This is the SAME ground→genre
# table CR4's stasis→primary-genre map uses (STASIS_PRIMARY_GENRE below), so a move's own genre and the
# live stasis's primary genre are read on ONE vocabulary, both derived from the ground:
#   conjectural/FACT → Memory (settled-record contest, forensic-past by the question asked)
#   definitional/DEFINITION → None — a HIGHER-ORDER REFRAME operator, NOT a genre (§1.2 res(3): "NOT
#     Memory … never collapsed to a genre"). A move ON definition-terrain re-classifies the act (see
#     is_higher_order_reframe); it does not itself argue in Memory or Projection.
#   qualitative/QUALITY, translative/JURISDICTION → None (present-terrain / the Stay)
#   deliberative CONSEQUENCE/FEASIBILITY → Projection (future-oriented; contract-endorsed)
_GROUND_TO_GENRE = {
    Stasis.FACT:         Genre.MEMORY,
    Stasis.DEFINITION:   None,             # §1.2 res(3): definitional is a reframe operator, NOT Memory/a genre
    Stasis.QUALITY:      None,             # present-terrain (epideictic register; see EPIDEICTIC_COMPRESSION)
    Stasis.JURISDICTION: None,             # translative: the Stay (pre-merits)
    Stasis.CONSEQUENCE:  Genre.PROJECTION,
    Stasis.FEASIBILITY:  Genre.PROJECTION,
}


def genre_of_ground(stasis_ground: str) -> Optional[str]:
    """The GENRE a move on this stasis ground argues in (Memory for conjectural/FACT, Projection for
       deliberative CONSEQUENCE/FEASIBILITY, None for present-terrain / the Stay, and None for
       definitional/DEFINITION — a reframe operator, not a genre; reconciliation_map_raw.md §1.2
       res(3)). Keyed on the stasis GROUND, NOT on Stasis.TENSE (§1.2 forbids TENSE as the genre
       intermediary) — so a move's genre and the live stasis's primary genre are read on the same
       ground-keyed axis for the CR4 +1D primary-genre match."""
    return _GROUND_TO_GENRE.get(stasis_ground)


# ══════════════════════════════════════════════════════════════════════════════════════════
# CR4 — CICERONIAN STASIS × GENRE  (RATIFIED_2026-06-01.md CR4)
# ══════════════════════════════════════════════════════════════════════════════════════════
# The four classical stases (rhetoric_oratory_contest_research §1.4, session-verified). Each is a
# TERRAIN — "what the fight is actually about". CR4 makes stasis BEHAVIORAL: which genre is primary
# (and thus which style earns the +1D primary-genre bonus, params/contest.md §Genre and Orientation
# Bonus Dice) is a FUNCTION of the live stasis GROUND, not a GM-fiat assignment (CR4 "closes the
# GM-fiat 'primary genre' assignment").
#
# ⚠ KEYED ON THE STASIS GROUND, NOT ON TENSE (reconciliation_map_raw.md §1.2 res(1)-(4)). §1.2 rules
# the map "must be built on the stasis GROUND keyed to CR4's four stases, NOT on the TENSE tag" (a
# groundup-internal rhetorical-weight tag with no canonical standing; CR4 supersedes it). Concretely
# §1.2 defect(a)+res(3): a DEFINITION→past→Memory chain "directly contradicts CR4", which routes
# definitional through the authored Present-rendering REFRAME operator, "never collapsed to a genre".
# So DEFINITION → None here (its reframe role is captured by STASIS_ROLE='higher_order' /
# is_higher_order_reframe, NOT by a genre). RATIFIED CR4 (L14): "definitional = higher-order reframe
# via the authored Present-rendering" — Present, NOT Memory/past.
#
# The four classical stases → their kernel Stasis ground → primary genre (by ground, per §1.2):
#   Conjectural  (an sit — "did it happen?" / FACT)          → Memory     (settled-record contest, §1.2 res(2))
#   Definitional (quid sit — "what is it?" / DEFINITION)     → None       (higher-order REFRAME operator, §1.2 res(3); NOT Memory)
#   Qualitative  (quale sit — "was it justified?" / QUALITY) → None       (present terrain; see EPIDEICTIC_COMPRESSION)
#   Translative  (translatio — "right venue?" / JURISDICTION) → None      (PRE-MERITS — the Stay, §1.2 res②)
#
# CONSEQUENCE/FEASIBILITY → Projection is contract-endorsed (§1.2 res(4): both deliberative-future
# grounds map to the Projection stance). Only conjectural/FACT sets Memory (§1.2 res(2)).

# Stasis GROUND → primary genre (CR4: stasis sets primary genre, keyed on the GROUND per §1.2). None =
# no primary genre (present terrain / pre-merits / the definitional reframe). Keyed by the kernel Stasis
# grounds (primitives.Stasis) — the SAME table genre_of_ground uses (_GROUND_TO_GENRE), single-sourced
# so a move's genre and the live-stasis primary genre are read on one ground-keyed axis.
STASIS_PRIMARY_GENRE = dict(_GROUND_TO_GENRE)  # FACT→Memory; DEFINITION/QUALITY/JURISDICTION→None; CONSEQUENCE/FEASIBILITY→Projection (§1.2)

# CR4 higher-order / pre-merits classification (behavioral, not just a label):
#   DEFINITIONAL is a HIGHER-ORDER REFRAME — it can re-open a fact-contest by re-classifying the act
#     (the kernel already models this: Stasis.stronger_than(DEFINITION, FACT) is True, so a "shift" to
#     definition is a legitimate reframe up the ladder; CR4 confirms definitional's reframe status).
#   TRANSLATIVE is PRE-MERITS JURISDICTION — the Stay: it is contested BEFORE the merits, and while it
#     is live no genre is primary (STASIS_PRIMARY_GENRE = None). This closes F6 (the jurisdiction silo).
STASIS_ROLE = {
    Stasis.FACT:         "merits",            # conjectural: on the merits
    Stasis.DEFINITION:   "higher_order",      # definitional: a higher-order reframe (re-classifies the act)
    Stasis.QUALITY:      "merits",            # qualitative: on the merits (present/epideictic register)
    Stasis.JURISDICTION: "pre_merits",        # translative: pre-merits jurisdiction — the Stay
    Stasis.CONSEQUENCE:  "merits",
    Stasis.FEASIBILITY:  "merits",
}


def primary_genre_for(stasis_ground: str) -> Optional[str]:
    """CR4: the PRIMARY GENRE the live stasis sets (Memory / Projection), or None when the stasis is a
       present-tense terrain (Qualitative) or pre-merits (Translative — the Stay). BEHAVIORAL: the
       style whose genre == this is the one that earns the +1D primary-genre bonus (params/contest.md
       §Genre and Orientation Bonus Dice), so CHANGING the live stasis CHANGES which dimension the
       contest rewards — stasis actually changes how the contest resolves, not just a label (Gate C
       requirement). Returns None when no genre is primary yet (present terrain / the Stay)."""
    if stasis_ground not in STASIS_PRIMARY_GENRE:
        raise ValueError(f"unknown stasis ground {stasis_ground!r}; valid: {sorted(STASIS_PRIMARY_GENRE)}")
    return STASIS_PRIMARY_GENRE[stasis_ground]


def is_pre_merits(stasis_ground: str) -> bool:
    """CR4: True iff the live stasis is TRANSLATIVE (jurisdiction — the Stay), which is contested
       BEFORE the merits and has no primary genre until settled. Closes F6 (jurisdiction silo)."""
    return STASIS_ROLE.get(stasis_ground) == "pre_merits"


def is_higher_order_reframe(stasis_ground: str) -> bool:
    """CR4: True iff the live stasis is DEFINITIONAL — a higher-order reframe that re-classifies the
       act (can re-open a settled fact-contest). Closes F5 (the definitional gap)."""
    return STASIS_ROLE.get(stasis_ground) == "higher_order"


# ── CR4 BEHAVIORAL CONSUMER: the +1D primary-genre bonus (the mechanic the resolver actually reads) ──
# params/contest.md §Genre and Orientation Bonus Dice: "Primary genre | +1D | Orator's CHOSEN GENRE
# matches [the GM-set] primary genre". CANONICALLY the primary genre was GM-set; CR4 makes the primary
# genre a FUNCTION of the live stasis (primary_genre_for). The CANONICAL condition preserved by CR4 is
# the orator's CHOSEN GENRE — i.e. the genre of the Style-card the orator PICKS (Precedent/Suppression =
# Memory; Vision/Insinuation = Projection), a FREE STRATEGIC CHOICE — matching the live-stasis primary
# genre. It is NOT the move's ground: on the merits the move MUST argue on the live issue
# (resolver Stasis.relevant forces move.ground == live), so keying the bonus on genre_of_ground(move.ground)
# would compare the live ground's genre against its own primary genre — a TAUTOLOGY that drops the
# orator's Style choice entirely (judge finding 1). CR4's strategic half is exactly that choice: the
# orator DECIDES which genre-stance (Memory vs Projection) to argue in, and is rewarded +1D iff that
# CHOSEN stance matches what the terrain (the live stasis) makes primary.
#
# This is the behavioral realization CR4 promises AND keeps the Style choice load-bearing: on a
# Memory-primary FACT stasis a Precedent/Suppression orator (chosen genre Memory) earns +1D but a
# Vision/Insinuation orator (chosen genre Projection) earns 0; on a Projection-primary CONSEQUENCE
# stasis it flips. So BOTH the live stasis AND the orator's Style choice move the outcome — a genuine
# non-dominated choice (churn axiom), not a terrain-determined constant.
#
# The +1D is a POOL bonus — the SAME channel the canonical prose specifies ("+1D", a die added to the
# Argue pool). Magnitude 1.0 die is the cited params value (not a fresh [SEED]). (The ARMATURE bonus is a
# SEPARATE, continuous δσ-leverage channel — CR6 — not this integer pool die; see armature.py.)
CR4_PRIMARY_GENRE_POOL_BONUS = 1.0   # +1D — params/contest.md §Genre and Orientation Bonus Dice (cited)


def genre_of_style(style_key) -> Optional[str]:
    """The GENRE of an orator's CHOSEN Style-card (the orator's 'chosen genre', params/contest.md
       §Genre and Orientation Bonus Dice). Precedent/Suppression → Memory; Vision/Insinuation →
       Projection (dictionaries.STYLES_TABLE[style].genre). This is the FREE STRATEGIC CHOICE the CR4
       +1D keys on — distinct from the move's ground (which the resolver forces onto the live issue).
       Accepts a style key or a Style object; None → None (no chosen genre, no CR4 bonus)."""
    if style_key is None:
        return None
    style = STYLES_TABLE[style_key] if isinstance(style_key, str) else style_key
    return style.genre


def primary_genre_pool_bonus(chosen_genre: Optional[str], live_stasis: str) -> float:
    """CR4 behavioral +1D primary-genre bonus (params/contest.md §Genre and Orientation Bonus Dice:
       "Orator's CHOSEN GENRE matches primary genre"), re-grounded on stasis (CR4). Returns
       CR4_PRIMARY_GENRE_POOL_BONUS (+1 die) when the orator's CHOSEN GENRE (`chosen_genre` — the genre
       of the Style-card the orator picked, genre_of_style; Memory or Projection) matches the live
       stasis's primary genre (primary_genre_for(live_stasis)); else 0.0.

    KEYED ON THE ORATOR'S CHOSEN GENRE, NOT THE MOVE GROUND (judge finding 1). The move must argue on
    the live issue (resolver Stasis.relevant forces move.ground == live), so keying on the ground's genre
    would be a tautology that erases the Style choice. The bonus instead rewards the orator for CHOOSING
    a genre-stance (via the Style card) that matches what the terrain makes primary — a real strategic
    bet: pick Memory (Precedent/Suppression) on a fact-terrain, Projection (Vision/Insinuation) on a
    consequence-terrain. `chosen_genre` is None when no Style is chosen (no armature) → no CR4 bonus (no
    'chosen genre' to match). When the live stasis is present-tense/pre-merits (primary genre None —
    Qualitative/Translative) NO genre is primary, so no chosen genre earns the bonus (the Stay /
    epideictic terrain). RESOLVES NOTHING on its own — the caller adds it to the reception pool
    (resolver._reception)."""
    if chosen_genre is None:
        return 0.0                                   # no Style chosen → no 'chosen genre' → no CR4 bonus
    primary = primary_genre_for(live_stasis)
    if primary is None:
        return 0.0                                   # present-tense terrain / the Stay: no primary genre
    return CR4_PRIMARY_GENRE_POOL_BONUS if chosen_genre == primary else 0.0


# ── The epideictic question (scope item 1) — addressed, not silently ignored ────────────────────
# Aristotle's THREE genres (rhetoric_oratory_contest_research §1.1-§1.2): deliberative (future/
# advantageous), forensic (past/just), EPIDEICTIC (present/honourable — praise & blame, audience as
# spectator). The v30 surface compresses to TWO genres (PP-234: "Genre restructure (3→2)"): Memory
# (=forensic/past) and Projection (=deliberative/future). Does that silently DROP epideictic?
#
# ANSWER (grounded, flagged — not silently ignored): the epideictic REGISTER is NOT dropped from the
# SUBSTRATE; only the genre LABEL compresses 3→2. The register survives as the RhetoricalWeights
# *_PRESENT column — ethos_present=1.20 is the epideictic home (ethos-dominant, praise/blame), fully
# live in resolver._advance's joint_weight (primitives.py RhetoricalWeights; "Epideictic / PRESENT :
# ethos-dominant"), the ceremonial basilikos-logos register (research §2.2). So epideictic is present
# as an ethos-dominant resonance register, not as a third stance/genre.
#
# ⚠ IMPORTANT (judge finding 3): this does NOT rest on a qualitative=epideictic identity. The research
# doc keeps them DISTINCT: qualitative (quale sit — "was it justified?") is a FORENSIC EVALUATION stasis
# (§1.4), while epideictic is a present-tense PRAISE/BLAME GENRE (§1.2); §0.4 explicitly downgrades the
# conflation ("the honourable/shameful is the epideictic axis, not the deliberative one … do not treat
# the six-item list as confirmed canon"). We therefore anchor the epideictic-survives claim ONLY on the
# defensible surface (RhetoricalWeights ethos_present + the §2.2 basilikos logos ceremonial register),
# and DROP the earlier "a qualitative contest IS the epideictic axis" equivalence.
#
# Whether that register-not-genre home is the RIGHT compression (vs restoring a third Epideictic genre
# with its own primary-genre bonus) is a GENUINE DESIGN DECISION, flagged for Jordan (DESIGN doc),
# because it trades surface simplicity against the lost praise/blame stance.
EPIDEICTIC_COMPRESSION = {
    "question": "Does the 2-genre (Memory/Projection) compression (PP-234, 3→2) silently drop "
                "Aristotle's third genre EPIDEICTIC (present-tense praise/blame, audience-as-spectator)?",
    "answer": "NOT SILENTLY — the epideictic REGISTER survives in the SUBSTRATE as the RhetoricalWeights "
              "*_present column (ethos_present=1.20, the ethos-dominant praise/blame home, live in "
              "_advance's joint_weight — the basilikos-logos ceremonial register, research §2.2). Only "
              "the genre LABEL compresses 3→2; the register is not lost.",
    "not_this": "The claim is NOT that a qualitative STASIS = the epideictic GENRE. Research §1.4 keeps "
                "qualitative (forensic 'was it justified?' evaluation stasis) distinct from epideictic "
                "(present-tense praise/blame GENRE, §1.2), and §0.4 downgrades that exact conflation. "
                "So the epideictic-survives argument rests ONLY on ethos_present + §2.2 basilikos logos, "
                "NOT on qualitative-terrain-as-epideictic.",
    "loss": "What IS lost is a present-tense STANCE with its own +1D primary-genre bonus: a Memory or "
            "Projection style can be primary, but there is no 'Epideictic/praise' style-card. A pure "
            "praise/blame ceremonial contest (basilikos logos, coronation oration — research §2.2) has "
            "no first-class genre; it is modelled via the ethos_present resonance register instead.",
    "decision_for_jordan": "RATIFIED (Jordan, Gate C, 2026-07-02): ACCEPT the 2-genre compression as-is. "
                           "The 2-genre (Memory/Projection) grid stays; epideictic survives ONLY via the "
                           "ethos_present/praise-blame register (RhetoricalWeights ethos_present, the "
                           "basilikos-logos ceremonial home), NOT as a first-class genre with its own "
                           "primary-genre bonus. No code/prose change was needed beyond this "
                           "ratification — the register is preserved where it is load-bearing and the "
                           "churn axiom is satisfied without a third stance; restoring a third EPIDEICTIC "
                           "genre (cost: a 5th/6th style-card, breaks the clean 2×2 Genre×Orientation "
                           "style grid) was considered and rejected. ED-1062.",
    "source": "rhetoric_oratory_contest_research §1.1-§1.2 (three genres; epideictic = present-tense "
              "praise/blame GENRE) + §1.4 (qualitative = forensic evaluation STASIS, distinct) + §0.4 "
              "(honourable = epideictic axis, six-item list downgraded) + §2.2 (basilikos logos "
              "ceremonial register); params/contest.md §Genres (PP-234 3→2); RhetoricalWeights *_present",
}


# ══════════════════════════════════════════════════════════════════════════════════════════
# CR5 — ORIENTATION RE-GROUNDED: Direct→Persuasion / Indirect→Face-attack + self-Face backfire
# ══════════════════════════════════════════════════════════════════════════════════════════
# CR5 (RATIFIED_2026-06-01.md): Direct (Revealing) orientation moves the Persuasion Track on the
# merits (as now — the existing CLASH/REINFORCE/CROSS/TIE path, UNCHANGED). Indirect (Obscuring)
# orientation attacks the opponent's FACE (ethos), WITH a self-Face BACKFIRE on failure. This is the
# Nyāya nigrahasthāna self-gating: obstruction (jalpa/vitaṇḍā-style eristic) is a legitimate move but
# BOUNDED BY YOUR OWN STANDING — a failed obstruction is a "point of defeat" (nigrahasthāna) that
# costs YOU (rhetoric_oratory_contest_research §5.1 nigrahasthāna defeat-conditions; §5.3 Vācaspati
# "obstruction is bounded by your own standing"; §9.1 self-gating invariant). This is the eristic-
# has-a-cost fix the critique demands (fallacies FG-2 / §2.6): an Obscuring win is no longer pure
# upside.
#
# WHAT CHANGES / WHAT DOES NOT (scope item 2 — this is REAL new mechanic scope, so it is bounded
# tightly):
#   • DOES NOT touch CLASH/REINFORCE/CROSS/TIE for Direct-vs-Direct exchanges (the existing merits
#     path is byte-unchanged — those are Revealing-orientation exchanges).
#   • ADDS ONLY: for an Obscuring move that FAILS AS A MOVE (reception degree 0 — a genuine
#     nigrahasthāna/foul, landing nowhere), a self-Face backfire consequence. An Obscuring move that
#     LANDS (deg >= 1) advances/plants as before (params/contest.md §Interaction Types: "Obscuring win …
#     place a Doubt Marker on the opponent"); only the move that lands NOWHERE (deg == 0) recoils onto
#     the mover's own Face — the eristic that failed as an argument (judge finding 7: a deg==1 partial
#     helped the mover and is no foul, so it must not be penalised).
#
# TRIGGER + MAGNITUDE, grounded in the Doubt Marker precedent (scope item 2 — "reuse its shape rather
# than inventing a parallel system"):
#   TRIGGER (revised — judge finding 7): an Obscuring (Indirect) argue move that FAILS AS AN
#     ARGUMENTATIVE ACT — i.e. its reception degree is 0 (it did NOT land at all). This is the Nyāya
#     nigrahasthāna proper: "victory is awarded against the side that incurs a nigrahasthāna" (research
#     §5.1/§206) — a nigrahasthāna is a move that FAILS as a move, a genuine FOUL, NOT a move that helped
#     you. The prior "did not win the exchange (deg < 2)" trigger was WRONG: a deg==1 partial LANDS and
#     advances the mover's own track (resolver._advance runs for deg >= 1), so it helped the mover — it
#     is no foul, and penalising it mis-attaches the cost to a partial SUCCESS. The corrected trigger
#     fires ONLY when the Obscuring move earned NOTHING (deg == 0): the eristic recoiled because it
#     landed nowhere. (A landed Obscuring move — deg >= 1 — advances/plants as before; only the
#     genuinely-failed foul recoils.)
#   MAGNITUDE: min(−2, the mover's OWN Face) — the −2 anchor (numerically the SAME −2 the Doubt Marker
#     applies, params/contest.md §Interaction Types "−2 … one active at a time; consumed on use") BOUNDED
#     BY THE MOVER'S OWN STANDING (judge finding 4). Reused, self-directed on a foul, standing-bounded —
#     NOT a fresh magnitude. QUANTITY MISMATCH, honestly flagged (judge finding 7): the Doubt Marker's −2
#     is a TRACK-MARGIN quantity ("−2 to opponent's next winning margin"), whereas this strips the 0–10
#     Face/Standing CREDIBILITY stat via Standing.strip_points, so the REALIZED Face delta equals the
#     standing-bounded magnitude exactly (judge finding 3). Same NUMBER anchor, different QUANTITY.
#     STANDING-BOUNDED (judge finding 4 — the fix): the RATIFIED CR5 carry-across (reconciliation_map
#     §1.3) requires the self-Face loss "gated by SelfGating.licit (your own Face caps your obstruction —
#     F7)". The prior flat −2 (no standing parameter) did NOT realize that — the central "bounded by your
#     own standing" invariant (research §5.3/§9.1) was behaviorally absent. cr5_self_backfire now takes
#     my_standing and returns min(CR5_BACKFIRE_MAGNITUDE, my_Face): a low-standing orator (Face < 2) risks
#     only what it holds, a higher-standing orator risks the full −2. Face is the CR3 contest-local
#     ethos/standing tracker (primitives.Face == Standing); the backfire strips it via strip_points (a
#     fixed-point penalty, NOT strip(deg) which scales by STRIP=0.8 and would apply only −1.6 — the
#     cited≠applied violation judge finding 3 flagged). This is the strip channel Stage 1d established but
#     left unwired (Gate-A note: "Standing.strip() is NEVER called in the contest kernel … Stage-3
#     scope"); CR5 fires it, at the standing-bounded magnitude.
#
# [SEED] / CANDIDATE: the −2 anchor ANCHORS to the Doubt Marker precedent (cited, not fabricated), but is
# applied to a different quantity (Face 0–10, not a track margin) and BOUNDED by the mover's standing
# (judge finding 4). The exact-quantity design-authority fork remains for Jordan: whether the Face CAP
# should equal the track −2 or be re-scaled to the credibility stat (DESIGN doc). The standing-dependence
# ITSELF is now REALIZED (not deferred) as the min(−2, Face) bound — the "bounded by your own standing"
# invariant. A DEEPER Nyāya variant (a high-standing orator risks MORE by stooping to jalpa — a strip
# that GROWS with standing, not just caps at it) remains a flagged candidate; the ratified-and-cited
# invariant realized here is the CAP (you cannot lose more than you hold), which is the directly-cited
# "bounded by your own standing" reading.
CR5_BACKFIRE_MAGNITUDE = 2.0    # −2 ANCHOR stripped from own Face on a FAILED-AS-A-FOUL Indirect move
                                #   (deg==0), BOUNDED by the mover's own Face (min(−2, Face); judge
                                #   finding 4). Anchored to the Doubt Marker −2 (params/contest.md
                                #   §Interaction Types) — a NUMBER precedent, applied to Face (0-10),
                                #   NOT the track-margin quantity the Doubt Marker measures (see fork).

# Orientation → resolution channel (CR5): the DESIGN-TABLE lookup for the ratified CR5 re-grounding.
#
# CR5 SCOPE — RATIFIED (Jordan, Gate C, 2026-07-02; ED-1062): CR5 has TWO halves, and the ratification
# keeps BOTH together as the full CR5 realization, rather than treating the opponent-Face-attack as a
# still-open replacement for the Doubt Marker:
#   • REVEALING → "persuasion_track": REALIZED — Direct moves the merits track (the existing
#     CLASH/REINFORCE/CROSS/TIE path, unchanged).
#   • OBSCURING → "face_attack": the ratified CR5 first half ("Indirect → attacks opponent Face
#     (ethos)") is realized by the EXISTING Gate-B Doubt Marker mechanic (params/contest.md §Interaction
#     Types; ED-1060) on a LANDED Obscuring move (deg>=1) — the Doubt Marker IS the opponent-facing
#     attack CR5's first half names (it degrades the marked opponent's own eventual winning margin),
#     realized as a track-margin penalty rather than a literal Face-stat strip. A landed Obscuring move
#     still advances the mover's own track exactly like a Revealing move (RATIFIED CR5-vs-ED-1060,
#     unchanged); the SECOND half — the self-Face backfire on a deg==0 Obscuring FOUL (cr5_self_backfire,
#     below) — is the piece newly wired this stage. RATIFIED: the Doubt Marker (landed) + the self-Face
#     backfire (failed) TOGETHER are the full CR5 realization, not two conflicting mechanics — no
#     separate opponent-Face-stat-attack mechanic is pursued (it would double up the Doubt Marker's
#     already-ratified role rather than complete CR5).
# So orientation_channel(OBSCURING) is a LABEL LOOKUP naming the ratified design intent; its resolution
# realization is the Doubt Marker (landed) + self-Face backfire (failed) pair described above, not a
# separate Face-stat strip on the opponent.
CR5_ORIENTATION_CHANNEL = {
    Orientation.REVEALING: "persuasion_track",  # Direct → moves the Persuasion Track on the merits (REALIZED, unchanged path)
    Orientation.OBSCURING: "face_attack",        # Indirect → attacks opponent Face (ethos) — RATIFIED: realized via the Gate-B Doubt Marker (landed) + this module's self-Face backfire (failed), together the full CR5
}


def orientation_channel(orientation: str) -> str:
    """CR5 DESIGN-TABLE lookup: the ratified resolution channel each orientation is DESIGNED to drive.
       Revealing (Direct) → the merits Persuasion Track (REALIZED — the existing CLASH/REINFORCE/CROSS/
       TIE path, unchanged). Obscuring (Indirect) → "face_attack" (the ratified CR5 intent: attack the
       opponent's Face). RATIFIED (Jordan, Gate C, 2026-07-02; ED-1062): this is realized by the Gate-B
       Doubt Marker (a landed Obscuring move, ED-1060) TOGETHER WITH the self-Face backfire on a deg==0
       foul (cr5_self_backfire) — both pieces together ARE the full CR5 realization, not two conflicting
       mechanics. RESOLVES NOTHING itself; do not read the "face_attack" string as a separate live
       channel beyond the Doubt Marker + self-backfire pair."""
    if orientation not in CR5_ORIENTATION_CHANNEL:
        raise ValueError(f"unknown orientation {orientation!r}; valid: {sorted(CR5_ORIENTATION_CHANNEL)}")
    return CR5_ORIENTATION_CHANNEL[orientation]


def cr5_self_backfire(style_key: str, landed: bool, my_standing: Optional[float] = None) -> float:
    """CR5 self-Face BACKFIRE (Nyāya nigrahasthāna): the Face self-strip a FAILED-AS-A-FOUL Indirect
       (Obscuring) move incurs, BOUNDED BY THE MOVER'S OWN STANDING. Returns the −Face magnitude (a
       positive number the caller strips from the mover's OWN Face), or 0.0 when no backfire applies.

    Fires ONLY when: (a) the style is OBSCURING (Indirect — Suppression or Insinuation), AND (b) the
    move DID NOT LAND at all (`landed` is False — reception degree 0). This is the nigrahasthāna proper
    (research §5.1/§206: "victory is awarded against the side that incurs a nigrahasthāna") — a genuine
    argumentative FOUL, a move that failed AS a move. A move that LANDED (`landed` True — deg >= 1,
    including a deg==1 partial that advanced the mover's own track) is NOT a foul and does NOT backfire
    (judge finding 7: the cost must not attach to a partial success that helped you). A Revealing
    (Direct) move NEVER backfires (it is the merits path).

    STANDING-BOUNDED (judge finding 4 — the fix). The RATIFIED CR5 carry-across (reconciliation_map_raw
    §1.3) requires the self-Face loss to be "gated by SelfGating.licit (your own Face caps your
    obstruction — F7)" — i.e. STANDING-DEPENDENT, realizing the cited Nyāya/Vācaspati invariant
    "obstruction is bounded by your OWN standing" (research §5.3/§9.1). The prior flat −2 (no standing
    parameter) did NOT realize that invariant — it stripped a fixed −2 regardless of the mover's Face,
    so the central self-gating principle the docstring named was behaviorally ABSENT. This now BOUNDS the
    strip by the mover's own Face: magnitude = min(CR5_BACKFIRE_MAGNITUDE, my_standing) when `my_standing`
    is supplied (a 0–10 Face value) — you cannot risk more standing than you have, so a low-standing
    orator's obstruction costs proportionally LESS in absolute Face (Face 1 → strips 1; Face ≥ 2 → strips
    the full −2). This is the "bounded by your own standing" self-gating made behavioral, not nominal.
    When `my_standing` is None (a pure-function/legacy call with no standing context), the unbounded −2
    precedent is returned (the caller's Face.strip_points floor-clamps at 0 either way, so a live-resolver
    strip is ALWAYS standing-bounded regardless — but passing my_standing makes the bound explicit in the
    returned magnitude, which is what the invariant requires).

    Magnitude anchor = CR5_BACKFIRE_MAGNITUDE (−2, the Doubt Marker precedent; applied to the 0–10 Face
    stat — see the quantity-mismatch note above). It does NOT touch the Direct-vs-Direct
    CLASH/REINFORCE/CROSS/TIE path (scope item 2). RESOLVES NOTHING on its own — the caller applies the
    strip to the mover's Face (primitives.Face.strip_points)."""
    style = STYLES_TABLE[style_key] if isinstance(style_key, str) else style_key
    if style.orientation != Orientation.OBSCURING:
        return 0.0        # Direct/Revealing move: the merits path, no backfire
    if landed:
        return 0.0        # a landed Obscuring move (deg >= 1) advanced/planted; no foul, no self-cost
    if my_standing is None:
        return CR5_BACKFIRE_MAGNITUDE   # legacy/pure call: unbounded precedent (floor-clamped by strip_points)
    # deg==0 foul: nigrahasthāna self-Face strip, BOUNDED by the mover's own standing (F7 self-gating):
    # you cannot risk more Face than you hold, so the cost is min(−2 precedent, your current Face).
    return min(CR5_BACKFIRE_MAGNITUDE, max(0.0, my_standing))


CR5_SELF_GATING = {
    "cr": "CR5",
    "ed": "ED-1062",
    "status": "RATIFIED (Jordan, Gate C, 2026-07-02; ED-1062)",
    "rule": "Direct (Revealing) → moves the Persuasion Track on the merits (unchanged CLASH/REINFORCE/"
            "CROSS/TIE path). Indirect (Obscuring): a LANDED Obscuring move (deg >= 1) advances/plants as "
            "before (the Gate-B Doubt Marker retained on the win path, RATIFIED CR5-vs-ED-1060); a move "
            "that LANDS NOWHERE (deg == 0 — a genuine argumentative foul) backfires min(−2, own Face) onto "
            "the mover's OWN Face — BOUNDED BY THE MOVER'S OWN STANDING (Nyāya nigrahasthāna self-gating; "
            "judge finding 4). RATIFIED (Jordan, Gate C, 2026-07-02; ED-1062): the Doubt Marker (landed "
            "Obscuring, opponent-facing) and the self-Face backfire (failed Obscuring, second half) are "
            "kept TOGETHER as the full CR5 realization — both pieces are wired this stage; the separate "
            "'opponent-Face-attack' idea that would retire the Doubt Marker is NOT pursued.",
    "trigger": "Obscuring (Indirect: Suppression/Insinuation) argue move whose reception degree is 0 — "
               "it FAILED AS A MOVE (a nigrahasthāna / foul), landing nowhere. Revealing moves never "
               "trigger; a LANDED Obscuring move (deg >= 1, including a deg==1 partial that advanced the "
               "mover's own track) never triggers (judge finding 7: the cost must not attach to a "
               "partial success that helped the mover).",
    "magnitude": "min(−2, the mover's own Face) — STANDING-BOUNDED (judge finding 4). The −2 ANCHOR is "
                 "the Doubt Marker −2 (params/contest.md §Interaction Types) as a magnitude precedent, "
                 "applied to a DIFFERENT QUANTITY (the 0–10 Face CREDIBILITY stat, not the marker's "
                 "track-MARGIN) via Standing.strip_points so the realized Face delta equals the bounded "
                 "magnitude exactly (judge finding 3; NOT strip(deg) which would scale by STRIP=0.8 and "
                 "apply only −1.6). BOUNDED BY OWN STANDING (judge finding 4): cr5_self_backfire takes "
                 "my_standing and returns min(CR5_BACKFIRE_MAGNITUDE, own Face), realizing the RATIFIED "
                 "'gated by SelfGating.licit — your own Face caps your obstruction' (reconciliation_map "
                 "§1.3) / 'obstruction is bounded by your own standing' (research §5.3/§9.1). The prior "
                 "flat −2 (no standing parameter) did NOT realize that invariant. Strips Face — the strip "
                 "channel Stage 1d established but left unwired; CR5 fires it, standing-bounded.",
    "grounding": "Nyāya nigrahasthāna defeat-conditions + Vācaspati/Quintilian self-gating: obstruction "
                 "is a legitimate move BOUNDED BY YOUR OWN STANDING (realized as the min(−2, own Face) cap "
                 "— judge finding 4); a move that INCURS a nigrahasthāna (fails as a move / a foul) is a "
                 "point of defeat that costs you — 'victory is awarded against the side that incurs a "
                 "nigrahasthāna' (research §5.1/§206; §5.3 Vācaspati 'obstruction is bounded by your own "
                 "standing'; §9.1; critique fallacies FG-2 / §2.6 eristic-has-a-cost). The standing-bound "
                 "is the RATIFIED CR5 carry-across 'gated by SelfGating.licit' (reconciliation_map §1.3).",
    "scope": "REAL new mechanic scope: adds the foul-side self-Face backfire consequence to the "
             "already-ratified Gate-B Doubt Marker. Does NOT change CLASH/REINFORCE/CROSS/TIE for "
             "Direct-vs-Direct exchanges; does NOT change the Obscuring-WIN Doubt Marker (params/"
             "contest.md, ratified Gate B ED-1060). WIRED this pass: the self-Face strip fires in "
             "resolver._apply on a deg==0 Obscuring argue move (opt-in Bout(armature=…, cr5=True)); off "
             "by default. RATIFIED (Jordan, Gate C, 2026-07-02) — CR5 SCOPE: keep the Doubt Marker + "
             "self-backfire TOGETHER, as the full CR5 realization. A landed Obscuring move produces the "
             "Gate-B Doubt Marker (ED-1060); a FAILED Obscuring move (deg==0) ALSO costs the mover's own "
             "Face (cr5_self_backfire) — both pieces together ARE the full CR5 realization, not two "
             "conflicting mechanics. The separate 'opponent-Face-attack' idea (a landed Obscuring move "
             "stripping the OPPONENT's Face, which would retire the Doubt Marker) is NOT pursued — the "
             "Doubt Marker already fills that landed-Obscuring-move role, so wiring a second attack "
             "would double up rather than complete CR5. ED-1062.",
    "open_forks_for_jordan": "(a) RESOLVED (Jordan, Gate C, 2026-07-02, ED-1062): CR5's shape is the "
                             "Doubt Marker (landed Obscuring, ED-1060) + the self-Face backfire (failed "
                             "Obscuring, this module) TOGETHER — both pieces together ARE the full CR5 "
                             "realization; the opponent-Face-attack idea that would retire the Doubt "
                             "Marker is not pursued. No further wiring is needed for CR5 scope. "
                             "(b) exact QUANTITY of the "
                             "self-Face cost ANCHOR — the −2 is anchored to the Doubt Marker's track-margin "
                             "−2 but applied to the 0–10 Face stat (a different quantity); whether the CAP "
                             "should equal that −2 or be re-scaled to the credibility stat is Jordan's "
                             "call; (c) standing-dependence is now REALIZED (judge finding 4) as the "
                             "min(−2, own Face) CAP — the directly-cited 'obstruction is bounded by your "
                             "own standing' (research §5.3) / 'gated by SelfGating.licit' "
                             "(reconciliation_map §1.3); a DEEPER Nyāya variant where the cost GROWS with "
                             "standing (a high-standing orator risks MORE by stooping to jalpa, not just "
                             "caps at −2) remains a flagged candidate for Jordan, distinct from the "
                             "realized cap.",
    "source": "RATIFIED_2026-06-01.md CR5; params/contest.md §Interaction Types (Doubt Marker −2 "
              "precedent); rhetoric_oratory_contest_research §5.1/§5.3/§9.1; social_contest_v30 §4 Step 2/4",
}
