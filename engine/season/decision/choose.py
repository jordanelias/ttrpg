"""`decision/` -- the `choose` member of `04_CODE_ARCHITECTURE.md` §A.2 (the `decision/` row).

`make_chooser` and everything it resolves by BARE NAME: `pack_scenes` (with
`_payload_of`). `align` (from `data/verbs.py`), `stance_toward` (from `queries/person_q.py`) and
`project` (from `options.py`) are imported here, so `from .choose import align, project` still
resolves.

⚠ **THE BARE-NAME CLUSTER IS WHY THESE ARE ONE FILE, AND IT IS NOT A STYLE CHOICE.** Two names
are read bare inside a body and rebound from OUTSIDE as module
attributes -- `pack_scenes` (by `make_chooser`) and `belief_contradicts` (by `opening_set`). A
bare name resolves in ITS OWN module's globals, so a rebind reaches it only if it targets the
module the reader lives in: `PS.pack_scenes = spy` in the degree-sweep arms reaches
`make_chooser` only because both live here, and a rebind aimed at the wrong namespace reports
every branch identical -- a fabricated null, which `CLAUDE.md` §0.1 pt 4 calls the worse of the
two directions. The rebind sites name `decision.choose` and `decision.options` directly for this
reason; see `__init__.py`.

⚠ **`ALIGNMENT` IS NOT BOUND HERE OR IN `options.py`: ITS ONE BINDING IS `data.verbs.ALIGNMENT`**,
where `align` is defined (telling workplan T2). The `H-66` sweep rebinds it there and `choose`'s
score and `options.refuses` both reach it through `align`. A stale `decision.choose.ALIGNMENT` or
`decision.options.ALIGNMENT` read fails loudly rather than rebinding a copy nothing reads.

⚠ **`belief_contradicts` IS NOT RE-EXPORTED FROM `__init__.py`**: a rebound value re-exported is
a stale snapshot, and a reader who rebinds the package attribute would silently miss the reader.

AX-2 binds every file under `decision/`: no `World`, as an import, a name, an attribute or a
string. Enforced BY PATH over this directory (`04 §E.1`).
"""

from __future__ import annotations

from typing import Any, Callable, Optional

from engine.dice_engine import fmath
from engine.dice_engine.fmath import ltr_sum
from ..data import goals as goals_data
from ..data.cast import STANCE_MAX
from ..data.pursuits import _AXES, to_axes   # the sorted axis order: a sum over the frozenset would add in PYTHONHASHSEED's order
from ..data.rosters import SCENE_PACKING_RULES, require_member, require_use_site, roster, seat_capability
from ..data.verbs import BODILY_PRIZES, CHOICE_SOURCED, VERB_TABLE, act_key, align, align_choice
from ..gaps import Unspecified
# `stance_toward` is the asker-first reader `queries/person_q.py` owns (`04 §C.3`: `decision/`
# imports `person_q` and `data/`); `_stance_arm` calls it, and `confliction` (IN-08 6f,
# the derived Query's caller, ID-13).
from ..queries.person_q import (
    believed_capability, confliction, intent_named, intent_said, refused_before, regard, stance_toward,
)
from ..state.carriers import EFFORT, Act, Candidate, Person, Question, Scene, Sensation, View, fade_of
from ..trace_log import TRACE
# `project` is DEFINED in `options.py` (see this module's docstring) and imported here because
# `make_chooser`'s score calls it; `options` never imports this module.
# `seat_of` is `options.py`'s own G3 helper (`via=seat_of(...)`, below).
from .options import VIOLENT_OPPONENT_VERBS, opening_set, project, refusal_tolerance, scruple, seat_of
# `options.py`'s one reader of a `judgement` row (`competence` is its other caller), under public names here: a call, not a copy (B10.28; CR-93 premise correction 2).
from .options import _judgement_factor as judgement_factor, _judgement_rows as judgement_rows
from .budget import body_band_penalty

STANCE_POLARITIES = roster("stance_polarities")
ODDS_WEIGHTINGS = roster("odds_weightings")
NPC_EFFORTS = roster("npc_efforts")
# B10.28: the use row that carries a person's own factor on the choice temperature (`rosters.yaml: tables.capability_uses`); a site
# renamed there refuses here at import, so `temper` cannot read no row and pass silently as 1.0.
CHOICE_TEMPER = require_use_site("choice_temper")
# B10.31: the use row that carries a person's own factor on the `risk` term (`nerve`); no row ships, and a site renamed there refuses here at import.
CHOICE_EXPOSURE = require_use_site("choice_exposure")


def stance_term(p: Person, c: Candidate, fx: "Fixtures", memo: Optional[dict] = None) -> float:
    """§F2's SECOND TERM, by `Fixtures.stance_polarity` (v9 IN-18 `G2`, `H-194`).

      * `legacy` (CONTROL; shipped until CR-16, which ships `declared`): `stance_toward(p, c.subject)` -- the pre-G2 term, verbatim.
      * `regard`: `regard(p, c.subject, fx)` with `+` on every row -- G1's regard and no polarity,
        the midpoint that separates what regard adds from what the sign adds.
      * `declared`: `regard(p, c.subject, fx)` times the row's `regard_sign` (B10.11; `+1`, `-1` or `0`), whose default
        is `-1` where the subject is the act's opponent (`options.subject_is_opponent`) and `+1` elsewhere: a grudge makes
        `fight` on its object score higher, where `legacy` scored it lower. With no cell authored the arms differ on
        contested rows only. `regard` is G1's, so its judged and told halves enter at their own gains
        (0.5 each, shipped).

    A Rung subject reads 0 at G1's control; at live gains it reads the deed claims held about it
    (`transfer.made` on a changed rung, under `claim_subject_rule: both`) -- nobody holds stance
    about a rung -- where the ROLE reading would regard its HOLDER; that operand needs a `held_by`
    claim (`H-195`).

    `memo` caches `regard` per subject for one deliberation: it depends on the subject and `p`'s
    ledger alone, which do not change inside one `choose` call.

    THE GAIN (v9 IN-25, BOUND-STAKES, `H-202`): whatever the arm returns is read at `1 + g`, `g` the
    swept `Fixtures.stance_gain`. §F2 gives the term weight 1 and no gain, so `g` is the weight the
    term carries ABOVE §F2's, and `0` -- the CONTROL (`1` ships, H-202) -- returns the arm's value
    untouched. It scales the SIGNED term, so under `declared` a grudge pulls `fight` on its object
    up and `tell` about it down, both harder. A negative or NaN `g` raises: below 0 the term is damped
    towards nothing and below -1 its sign flips, which is G2's polarity and not this gain."""
    # ABSENT: H-195 holder  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
    g = fx.get("stance_gain")
    if not g >= 0:                   # `not >=`, so a NaN is refused too
        raise ValueError(f"stance_gain {g} is not >= 0: it would damp or invert §F2's stance "
                         f"term, and inverting it is G2's polarity, not this gain (H-202)")
    # B10.04 (`U5a_CHAR_owed_amendments` §2, H-464): regard read as a share of `STANCE_MAX` times `Fixtures stance_scale`, applied to
    # the arm's value BEFORE either gain. At the control (`stance_scale == STANCE_MAX`) the quotient is `25 / 25 == 1.0` and
    # `t * 1.0 == t` for every float, so the term is today's exactly. The clamp to the bound is B10.10's (`stance_clamp`), inside `_stance_arm`, so this factor reads the clamped value.
    t = _stance_arm(p, c, fx, memo) * (fx.get("stance_scale") / STANCE_MAX)
    # v11 CR-87 (THE GRUDGE'S BOUND): on a VIOLENT row (`data/verbs.py::VIOLENT_VERBS`, off `rosters.yaml:
    # violent_prizes`) whose subject is its opponent, the term is read at `Fixtures hostile_stance_gain` in place of
    # `1 + g`, so a grudge's pull on violence is bounded apart from its pull on every other act; `declared`'s sign
    # (CR-16) is the arm's and is kept. `None` is the REVERT: `1 + g`, the same expression, exactly.
    h = fx.get("hostile_stance_gain")
    if h is not None and c.verb in VIOLENT_OPPONENT_VERBS:
        if not h >= 0:
            raise ValueError(f"hostile_stance_gain {h} is not >= 0: a negative weight would invert the "
                             "grudge's sign on a violent row, which is G2's polarity, not this bound (CR-87)")
        return h * t
    return (1.0 + g) * t             # at g == 0 this is 1.0 * t: exact for every float


def _bounded(v: float, clamp: bool) -> float:
    """`v` held to `+-STANCE_MAX` at `Fixtures.stance_clamp`, else `v` itself (the control)."""
    return max(-STANCE_MAX, min(STANCE_MAX, v)) if clamp else v


def _stance_arm(p: Person, c: Candidate, fx: "Fixtures", memo: Optional[dict]) -> float:
    """`stance_term`'s value at §F2's weight (gain 0): the arm `Fixtures.stance_polarity` names (H-194)."""
    subject = c.subject or ""
    arm = fx.get("stance_polarity")
    # B10.10 (`U5a_CHAR_owed_amendments` §2, H-471): at `stance_clamp` the value read is bound to the row type's own bound before the polarity sign, so a sum past
    # it (`stance_toward` has no ceiling) is read at `STANCE_MAX`. `False` is the control: the value is returned untouched.
    clamp = fx.get("stance_clamp")
    if arm == "legacy":
        return _bounded(stance_toward(p, subject), clamp)
    require_member(arm, STANCE_POLARITIES, f"stance polarity {arm!r} is not in the roster", "H-194",
                   law="§G -- declare it, default it, sweep it; an unknown arm silently reading "
                       "`legacy` would make the sweep report the control twice")
    if memo is None:
        memo = {}
    if subject not in memo:
        memo[subject] = regard(p, subject, fx)
    r = _bounded(memo[subject], clamp)
    if arm == "regard":
        return r
    row = VERB_TABLE.get(c.verb)
    # CP-T05-02 (B10-13): self-regard is read here as `regard(p, p.id)` (stored stance plus his own deeds), while `_bond`
    # treats a judge as his own full ally; the two are not routed together. `subject_is_opponent` encodes 'a person is not his own adversary'; a self-plea
    # (`subject_may_be_self`) is an act FOR himself, so the sign applies only where the subject is somebody else.
    # B10.11: the sign is the row's own column (`VerbRow.regard_sign`: +1, -1 or 0), whose default is `-1` where the act is contested
    # against its subject (`subject_is_opponent`), else `+1` -- so a row with no cell reads exactly as it did.
    return row.regard_sign * r if row is not None and subject != p.id else r


# IN-62: the keys under which `make_chooser` hoists a deliberation's candidate-independent factors
# into the `memo` `score_terms` reads. TUPLES, because `_stance_arm` keys the same dict by subject id
# (a string), so no subject can collide with one of these.
_AXIS_W, _DAMP, _AIM = ("axis_w",), ("damp",), ("aim",)


def deliberation_memo(p: Person, fx: "Fixtures") -> dict:
    """The `memo` `score_terms` reads, built the way `make_chooser` builds it for one deliberation:
    the projected axis weights (with the swept `scar_weight_shift`) and the `confliction` damp (the
    swept `confliction_weight`, H-188), hoisted once because neither depends on the candidate.
    Exists so a reading that scores a person outside `choose` (`harness/decision_spread.py`) takes
    the SAME two factors from the same arms rather than copying them. A third key, `_AIM`, holds the goal's projected lean for the
    question being answered (B10.30): empty here, filled by `aim_term` the first time a candidate is scored on a question, so a
    deliberation projects each goal's pursuits once however many candidates it scores."""
    k = float(fx.get("confliction_weight"))
    if not k >= 0:                   # `not >=`, so a NaN is refused too
        raise ValueError(f"confliction_weight {k} is not >= 0: it would invert, divide by zero "
                         f"or poison the score (H-188)")
    return {_AXIS_W: project(p, fx.get("scar_weight_shift")),
            _DAMP: 1.0 if k == 0 else 1.0 / (1.0 + k * confliction(p)),
            _AIM: {}}


def _odds_arm(fx: "Fixtures") -> str:
    """`Fixtures.odds_weighting`, refused if it is not in the roster (an unknown arm silently reading `none` would make
    the sweep report the control twice). Its own function so `score_terms` can validate the arm on a term it does not weigh."""
    arm = fx.get("odds_weighting")
    require_member(arm, ODDS_WEIGHTINGS, f"odds weighting {arm!r} is not in the roster", "H-248",
                   law="CR-17 -- declare it, default it, sweep it; an unknown arm silently reading "
                       "`none` would make the sweep report the control twice")
    return arm


def _writing_bands(c: Candidate) -> Optional[tuple]:
    """THE BANDS A CONTESTED CANDIDATE'S VERB WRITES IN (`row.writes_by_degree`'s non-empty lists), or `None` for a
    verb that contests nothing or writes in no band. The ONE test of whether a believed chance can price a
    candidate: `odds_weight` weights by it and `settle_efforts` offers an `effort` variant only where it holds."""
    row = VERB_TABLE.get(c.verb)
    if row is None or not row.contests:
        return None
    bands = tuple(b for b, written in row.writes_by_degree.items() if written)
    return bands or None


def odds_weight(p: Person, c: Candidate, fx: "Fixtures", odds: Optional[Callable]) -> float:
    """THE FACTOR `Fixtures.odds_weighting` PUTS ON A CONTESTED CANDIDATE'S PURSUIT TERM (CR-17, `H-248`;
    M1, AQ-X1 (b)): the person's believed chance of the bands that write what the term prices.

      * `none` (CONTROL) -- 1.0 for every candidate: the term as it stood before CR-17;
      * `believed` -- for a candidate whose verb CONTESTS something (`row.contests`) and writes in at least
        one band (`row.writes_by_degree`, a map from band to its write list), `odds(act, bands)` over
        the bands whose list is non-empty: the sum of the person's believed chances of those bands, which is
        what his pursuit-priced cells are worth if the roll lands there and nothing if it does not. An
        uncontested verb, a contested one that writes in no band, and an answer of `None` (a factor he
        cannot know, no dice dealt, S27.4's refusal, another module's prize) are 1.0: the term as it was.

    THE BANDS ARE READ OFF THE ROW'S OWN `writes:` MAP, never a verb name: `argue` writes in two bands, so its
    cells are weighted by P(those two); `determine` in three; a verb that writes in every band is weighted by
    1 (its cells are certain whichever way the dice fall). `odds` is the QUERY on the View (`View.odds`,
    `seam/wrappers/sigma.py::believed_chance`): `decision/` holds a callable and the act's shape, never the
    store behind it. A candidate is probed as the act it would become (`pack_scenes`' payload and seat), so
    the figure is the one for the roll the fold would deal that act."""
    return weigh_by_chance(fx, None if odds is None else (lambda: _believed_chance(p, c, odds)))


def weigh_by_chance(fx: "Fixtures", ask: Optional[Callable[[], Optional[float]]]) -> float:
    """THE ONE RULE OF `odds_weighting` (B10.57: `odds_weight` and `decider.make_decider`'s choice score both call it, so a choice inside a contest is
    priced by the factor a candidate is): `ask`, a no-argument call for the believed chance, is read only at the arm `believed`; the arm `none`, no `ask`
    and an answer of `None` are 1.0, and the arm is checked first whatever the rest holds."""
    if _odds_arm(fx) == "none" or ask is None:
        return 1.0
    chance = ask()
    return 1.0 if chance is None else float(chance)


def _believed_chance(p: Person, c: Candidate, odds: Callable) -> Optional[float]:
    """THE ONE ASK OF THE ODDS QUERY (B10.31: `odds_weight` and `risk_term` both read it here, so no second site builds the probe): `odds(act, bands)`
    for the candidate probed as the act it would become, over the bands its row writes in (`_writing_bands`); `None` for a candidate with no such
    bands (nothing a chance can price) and for the query's own `None` (a factor he cannot know)."""
    bands = _writing_bands(c)
    if bands is None:
        return None
    return odds(Act(f"odds:{c.verb}", p.id, c.verb, payload=_payload_of(c), via=seat_of(p, c)), bands)


def admission_weight(p: Person, c: Candidate, fx: "Fixtures") -> float:
    """THE FACTOR A REMEMBERED REFUSAL PUTS ON A CANDIDATE'S PURSUIT TERM (B09.03; `H-456`):
    `1 - refusal_memory * refused_before(...) / confidence_default`, so a person refused this opportunity retries it at lower odds,
    never at none below `refusal_memory` 1.0.

      * `refusal_memory` `0.0` (CONTROL) -- exactly 1.0 for every candidate, and no ledger is read;
      * a verb whose row declares no refusal kind (`VERB_TABLE[verb].emits_on_refusal`, empty), an opportunity with no subject, and
        one where nothing is remembered (`person_q.refused_before` is 0: no such claim, or news of the subject newer than it) -- 1.0.

    The remembered confidence is read at the person's own tick and the fixture's decay (`carriers.fade_of`, what `decision/`'s other
    readers take), so a refusal fades as any claim does; the own-ledger reader takes the person and no World (AX-2).
    A `refusal_memory` outside `[0, 1]` (or NaN) raises: above 1 the factor goes negative and would invert the pursuit term."""
    memory = fx.get("refusal_memory")
    if not 0.0 <= memory <= 1.0:     # `not <= ... <=`, so a NaN is refused too
        raise ValueError(f"refusal_memory {memory} is not in [0, 1]: above 1 the factor goes negative and would invert the "
                         "pursuit term it weighs (H-456)")
    if memory == 0.0:
        return 1.0
    row = VERB_TABLE.get(c.verb)
    if row is None or not row.emits_on_refusal or not c.subject:
        return 1.0
    tick, decay = fade_of(p)
    remembered = refused_before(p, row.emits_on_refusal, c.subject, tick, decay)
    return 1.0 if not remembered else 1.0 - memory * remembered / fx.get("confidence_default")


def fit_term(p: Person, c: Candidate, fx: "Fixtures") -> float:
    """THE CONFERRER'S VIEW OF A CANDIDATE, at `Fixtures.confer_fit_weight` (B04.22; `H-414`): `weight * (regard(p, to) +
    the skill his own ledger holds of `to`)`, over a row that SEATS a person -- the row's shape, never a verb name: a
    `referent_class` of `Office` with a `counterparty` of `to`, the candidate's `subject` being the seat. The skill is the
    one the SEAT'S ROW names (`offices.yaml`, `capability:`, read through `data.rosters.seat_capability`) as `believed_capability` has
    it; `None` -- no seat row, no key, or no claim held, which is every case in a built realm -- adds nothing, so the
    term is regard alone [ASSUMPTION; low; Jordan to correct: regard and skill are summed as they stand, in their own
    units]. Exactly `0.0` at the weight's `0.0` -- the CONTROL, today's positional order -- and reads no ledger there."""
    weight = float(fx.get("confer_fit_weight"))
    if not weight >= 0:                  # `not >=`, so a NaN is refused too
        raise ValueError(f"confer_fit_weight {weight} is not >= 0: a negative weight would seat the conferrer's least "
                         "regarded candidate (H-414)")
    if weight == 0.0:
        return 0.0
    row = VERB_TABLE.get(c.verb)
    to = (c.operands or {}).get("to")
    if row is None or row.referent_class != "Office" or row.counterparty != "to" or not to:
        return 0.0
    fit = regard(p, to, fx)
    capability = seat_capability(c.subject)
    skill = believed_capability(p, to, capability, *fade_of(p)) if capability else None
    return weight * (fit + (0 if skill is None else float(skill)))


def aim_term(p: Person, c: Candidate, fx: "Fixtures", memo: dict, odds: Optional[Callable], q: Optional[Question]) -> float:
    """THE GOAL'S OWN LEAN ON THE QUESTION IT RAISED (B10.30; `H-477`): `aim_gain * damp * Σ_axis to_axes(goal.pursuits)[axis] *
    align(c.verb, axis) * odds_weight`, the pursuit term's own dot over the GOAL's pursuits instead of the person's, in the same
    axis order (`_AXES`), with the same believed-odds factor. The goal is the one `q` is about: it applies where `q.source` is `need`,
    `q.about` is a row of `goals.yaml` and `p` holds a LIVE `commit` to it; otherwise 0.0. A person's own want (`prop_<cid>`) and a
    creed are not rows of `goals.yaml` and carry no `pursuits:`, so they read 0.0 -- a limit, until a want carries a lean.

    Exactly `0.0` at `aim_gain` 0, the CONTROL, and nothing is read there (the odds query is not asked). The gain is refused below 0:
    a negative gain would score a goal's own business against the goal. `odds_weight` is asked only for a candidate the lean scores
    (`score_terms`' pursuit term does the same: the query scans the log)."""
    gain = fx.get("aim_gain")
    if not gain >= 0:                # `not >=`, so a NaN is refused too
        raise ValueError(f"aim_gain {gain} is not >= 0: a negative gain would score a goal's business against the goal (H-477)")
    if gain == 0.0 or q is None or q.source != "need":
        return 0.0
    lean = memo[_AIM]
    if q.about not in lean:
        goal = goals_data.goal(q.about)
        live = goal is not None and any(t.kind == "commit" and t.live and t.object == q.about for t in p.tenures)
        lean[q.about] = to_axes(goal.pursuits) if live else None
    axes = lean[q.about]
    if axes is None:
        return 0.0
    aim = gain * memo[_DAMP] * ltr_sum(axes[ax] * align(c.verb, ax) for ax in _AXES)
    return aim * odds_weight(p, c, fx, odds) if aim != 0.0 else aim


def nerve(p: Person, fx: "Fixtures") -> float:
    """HOW FAR A PERSON'S SPIRIT LETS HIM BEAR A DANGER (B10.31; `H-480`): his own factor on `risk`, the `judgement` rows of site `choice_exposure` read by
    `options._judgement_factor` as `temper` and `competence` read theirs: `about_mid(held, floor, ceiling, nerve_gain)`, exactly 1 at the scale's mid-point and at
    gain 0, and 1.0 where no row is authored (none ships) or `p` holds no value at the row's key (a READ, never a default). `decision/` names no attribute (U1 §8):
    the key is the row's.

    ⚠ THE SIGN, as `temper`'s. `about_mid` RISES with the attribute, so a danger that weighs LESS on the high-Spirit person needs a NEGATIVE `nerve_gain`; a gain
    above 0 would make the bold fear more, and below -1 the factor goes negative at the top of the scale and `risk` becomes a pull toward danger. Both are refused
    where read."""
    rows = judgement_rows(CHOICE_EXPOSURE)
    for row in rows:
        gain = fx.get(row.gain)
        if not -1.0 <= gain <= 0.0:
            raise ValueError(f"{row.gain} {gain!r} is outside [-1, 0] (H-480): above 0 the bold fear more, and below -1 the factor is negative at the "
                             "scale's ceiling and `risk` would pull toward danger")
    factor = judgement_factor(p, rows, fx)
    return 1.0 if factor is None else factor


def risk_term(p: Person, c: Candidate, fx: "Fixtures", odds: Optional[Callable]) -> float:
    """WHAT AN ACT MIGHT COST THE PERSON WHO DOES IT, IN BODY OR IN THE FIELD (B10.31; `H-478`, `H-479`, `H-480`):

        risk = - risk_gain * exposed * (1 - chance) * (1 + body_band_penalty) * nerve

      * `exposed` -- 1 where the candidate's row contests a prize `rosters.yaml: bodily_prizes` lists (`BODILY_PRIZES`), else 0. Read off the row's own
        `contests:` column, never a verb name; a candidate that is not exposed reads exactly `0.0`;
      * `chance` -- his believed chance, asked of the ONE odds query (`View.odds`, `_believed_chance`: the bands the row writes in, as `odds_weight` asks), and
        `Fixtures.risk_unknown_chance` where the query answers `None` or there is none. The believed chance is read, never made here: a later error on his
        belief (B10.80, `misjudged`) wraps the query once and reaches this term through the argument, with no second owner of it. ⚠ WHAT THE QUERY SAYS OF A
        BODILY ROW: for a row whose prize provider registered a `believed_estimate` (`personal_combat`'s) it is the chance the SUBJECT ends in the bands the row
        writes (the combat module's own, `Felled`, `Wounded` ...), the figure `odds_weight` prices a gain by; it does not say which party fell, so it is the
        nearest figure the one query carries for his chance of coming through, not that chance [ASSUMPTION; low; Jordan to correct: H-478's cite]. A row whose
        provider has none (`march`, the field's) answers `None` and reads `risk_unknown_chance`;
      * `body_band_penalty` -- `decision/budget.py`'s count of the bands his body has fallen below the top: 0 at full health, so `1 + 0` is 1;
      * `nerve` -- `nerve(p, fx)`, his Spirit's factor; 1.0 where no row ships.

    Exactly `0.0` at `risk_gain` 0, the CONTROL, and nothing is read there: the odds query is not asked. The gain is refused below 0 (a negative gain would pull a
    person toward danger), and `risk_unknown_chance` outside [0, 1] where it is read."""
    gain = fx.get("risk_gain")
    if not gain >= 0:                # `not >=`, so a NaN is refused too
        raise ValueError(f"risk_gain {gain} is not >= 0: a negative gain would pull a person toward danger (H-478)")
    if gain == 0.0:
        return 0.0
    row = VERB_TABLE.get(c.verb)
    if row is None or row.contests not in BODILY_PRIZES:
        return 0.0
    chance = None if odds is None else _believed_chance(p, c, odds)
    if chance is None:
        chance = fx.get("risk_unknown_chance")
        if not 0.0 <= chance <= 1.0:
            raise ValueError(f"risk_unknown_chance {chance} is not in [0, 1]: it stands for a chance (H-479)")
    return 0.0 - gain * (1.0 - float(chance)) * (1 + body_band_penalty(p, fx)) * nerve(p, fx)     # `0.0 -`: a sure chance reads 0.0, not -0.0


def score_total(terms: tuple) -> float:
    """A candidate's score from its `score_terms`, the one sum (`make_chooser`, `harness/interactions.py` and
    `harness/decision_spread.py` read it here), left to right. A `fit`, an `aim` or a `risk` of `0.0` -- every candidate at the shipped
    weight and gains -- adds nothing, not even a sign of zero, so the score is the two-term sum exactly."""
    s = terms[0] + terms[1]
    if terms[2]:
        s = s + terms[2]
    if terms[3]:
        s = s + terms[3]
    return s + terms[4] if terms[4] else s


def score_terms(p: Person, c: Candidate, fx: "Fixtures", memo: dict, odds: Optional[Callable] = None,
                q: Optional[Question] = None) -> tuple:
    """§F2's score, term by term: `(pursuit, stance, fit, aim, risk)`, and `score(c)` is `score_total` of them (IN-62; the sum, `fit`
    being `0.0` at `confer_fit_weight`'s shipped `0.0`, `aim` at `aim_gain`'s and `risk` at `risk_gain`'s). `aim` is appended after `fit`, not set before it:
    `fit` was the tuple's third element before `aim` landed (B04.22), and every reader of it by index keeps it. `risk` follows `aim`, fifth, for the same reason
    (the entry's `(pursuit, stance, aim, risk)` cannot hold: slot 3 is `fit`); `TERM_NAMES` is this tuple's names in order.
    The ONE owner of the formula (`CLAUDE.md` §8): `make_chooser`'s `score` calls this and adds, and
    a reading that wants to know WHICH TERM decided a ranking calls this and never re-derives one.

      * `pursuit` -- `damp * Σ_axis axis_w[axis] * (align(c.verb, axis) + Σ_(key, value) align_choice(key, value, axis)) * odds_weight(...)` (the
        parenthesised sum over the candidate's `choice_sourced` operands, B10.56; empty where no cell is authored), `axis_w` the
        person's projected pursuits, `damp` the `confliction_weight` arm's factor (exactly 1.0 at 0) and
        `odds_weight` CR-17's believed-chance factor on a contested candidate (exactly 1.0 at
        `odds_weighting` `none`, for an uncontested candidate, and when `odds` is `None`), and
        `admission_weight` the factor a remembered refusal puts on it (exactly 1.0 at `refusal_memory` `0.0`, B09.03);
      * `stance` -- `stance_term(p, c, fx, memo)`, by `Fixtures.stance_polarity`, at gain `1 + g`;
      * `fit` -- `fit_term(p, c, fx)`: the conferrer's view of the candidate a seating row names in `to`;
      * `aim` -- `aim_term(p, c, fx, memo, odds, q)`: the lean of the goal `q` was raised by, on that goal's own question only (B10.30);
      * `risk` -- `risk_term(p, c, fx, odds)`: what a bodily candidate might cost its doer, by the same `odds` query (B10.31; not asked at `risk_gain` 0).

    `q` is the question being answered (`View.question`); `None` -- a reading that scores a person outside `choose` -- reads `aim` 0.0.
    `odds` is the believed-odds query a View carries (`View.odds`); a reading that scores a person outside
    `choose` passes the same query or leaves it `None` and reads the score without CR-17's factor.
    `memo` is a `deliberation_memo(...)` (it also caches `regard` per subject for the call). A memo
    without the hoisted factors is refused, not defaulted: a missing factor read as 0 or 1
    would score a different person than the one asked about."""
    try:
        axis_w, damp, _ = memo[_AXIS_W], memo[_DAMP], memo[_AIM]
    except KeyError:
        raise ValueError("score_terms needs a memo from `deliberation_memo(p, fx)` "
                         "(or `make_chooser`'s): the pursuit weights and damp are "
                         "hoisted per deliberation") from None
    pursuit = damp * ltr_sum(axis_w[ax] * align(c.verb, ax) for ax in _AXES)
    # B10.56: the candidate's CHOICE VALUES (`choice_sourced` keys its operands carry), scored by their own alignment cells through the same
    # weights and damp, so `odds_weight` below prices them with the verb's. Added only where a cell moves it: no cell authored (the shipped
    # roster) leaves `pursuit` the very float above, not that float plus a signed zero.
    chosen = tuple((k, c.operands[k]) for k in CHOICE_SOURCED.get(c.verb, ()) if k in (c.operands or {}))
    if chosen:
        by_choice = damp * ltr_sum(axis_w[ax] * ltr_sum(align_choice(k, v, ax) for k, v in chosen) for ax in _AXES)
        if by_choice != 0.0:
            pursuit += by_choice
    if pursuit != 0.0:
        pursuit *= odds_weight(p, c, fx, odds)
        pursuit *= admission_weight(p, c, fx)
    else:
        _odds_arm(fx)           # a zero term is zero whatever the factor: the query is not asked (it scans the log), the arm is still checked.
                                # Value-equal; the one difference is an error the query would raise on this candidate, which is no longer raised
    return (pursuit, stance_term(p, c, fx, memo), fit_term(p, c, fx), aim_term(p, c, fx, memo, odds, q), risk_term(p, c, fx, odds))


def _npc_effort_arm(fx: "Fixtures") -> str:
    """`Fixtures.npc_effort`, refused if it is not in the roster (`_odds_arm`'s reason: an unknown arm silently
    reading `off` would make the sweep report the control twice)."""
    arm = fx.get("npc_effort")
    require_member(arm, NPC_EFFORTS, f"npc effort arm {arm!r} is not in the roster", "H-249",
                   law="CP-T01-05 NPC half -- declare it, default it, sweep it; an unknown arm silently "
                       "reading `off` would make the sweep report the control twice")
    return arm


def settle_efforts(cands: list, scores: dict, score: Callable, fx: "Fixtures") -> tuple:
    """THE CHOOSER FORMS `effort` (CP-T01-05, NPC half; `H-249`): for each CONTESTED candidate whose believed
    chance can price it (`_writing_bands`), the variants at effort `1 .. interactions_per_scene - 1` are
    ordinary Candidates (`effort` an operand, `carriers.EFFORT`, which `_payload_of` carries to the act and
    to the odds query), scored by the SAME `score` as their base -- so a variant scores higher exactly where
    the believed chance of the bands the term prices rises with the effort (CR-17's factor; this function
    never asks a chance itself). One act per opportunity: of a base and its variants only the best survives,
    since they would share one act id.

    THE PRICE. Effort `e` fills `1 + e` slots (`Scene.slots`), so it costs the `e` acts the person does not take
    beside it: a variant scoring `r` is NET of the `e` best-scoring OTHER candidates ranked beneath `r` (the ones
    its extra slots push out of the scene; a negative score is no loss, so each counts at least 0). It survives only
    if that net strictly beats the base's own score; a tie keeps the base. With nothing ranked beneath it, effort
    displaces nothing and a believed gain is free in slots. No flat bonus: the only thing that lifts a variant is
    the believed chance in the pursuit term. The scene BUDGET (an effort scene costs `extended_scene_cost`) is
    `pack_scenes`'s `take()`, through `Scene.cost`.

    `off` returns its arguments untouched (the CONTROL); a verb that has no believed chance to ask, a
    chance of `None`, and `odds_weighting` `none` all leave a variant scoring as its base, so the base stays.
    Returns `(cands, scores)` for the kept set, `scores` keyed on `id(c)` as `score_order` wants."""
    if _npc_effort_arm(fx) == "off":
        return cands, scores
    per = fx.get("interactions_per_scene")
    if per is None or per < 2:
        return cands, scores                # no scene bound, or no room for a second slot: no effort can be formed
    kept, kept_scores = [], {}
    for c in cands:
        base = scores[id(c)]
        best, best_net, best_score = c, base, base
        if _writing_bands(c) is not None:
            others = None
            for e in range(1, per):
                v = Candidate(c.verb, c.subject, {**(c.operands or {}), EFFORT: e})
                raw = score(v)
                if raw <= base:
                    continue                # the price is never negative, so a variant that does not out-score its base cannot win
                if others is None:
                    others = sorted(scores[id(o)] for o in cands if o is not c)         # ascending
                beneath = [max(0.0, x) for x in others if x <= raw]
                priced = raw - ltr_sum(beneath[-e:])                                   # the `e` best beneath it
                if priced > best_net:
                    best, best_net, best_score = v, priced, raw
        kept.append(best)
        kept_scores[id(best)] = best_score
    return kept, kept_scores


def beneficiary_of(p: Person, c: Candidate) -> Optional[str]:
    """WHO THIS CANDIDATE IS TAKEN FOR THE GOOD OF -- the verb's declared `beneficiary:` column,
    resolved against the carriers THIS Candidate holds. `CAT-2`, phase-6 item `6d`.

    ⚠ THE RESOLUTION IS THE WHOLE OF THE MECHANISM AND IT TOUCHES `_derive_operand` NOWHERE.
    The column is static per verb; this reads it and looks up a carrier the Candidate already has.
    That is the property `CAT-2` bought by declaring rather than deriving -- *"a verb-table column
    never touches `_derive_operand`, so r2 item 7 and this are independent"* -- and it is why this
    function needs no World, no Query and no fifth `Candidate` field.

    ⚠⚠ `None` HAS TWO MEANINGS AND A CALLER THAT CONFLATES THEM IS WRONG. They are told apart by
    the ROW, not by this return:
      * `beneficiary: none` -- the verb DECLARES that no person the Candidate holds is the one it
        is done for the good of. A `create_record` benefits a Record. This is an answer.
      * a declared carrier that DID NOT BIND on this candidate -- `to` where the cell admits the
        operand but this particular form carries none. This is a HOLE, and
        `test_lb6d_the_column_resolves_on_candidates_the_engine_actually_forms` counts it
        separately, because a term that silently reads as
        *"benefits nobody"* whenever its operand is missing is `§0.1 pt 2` exactly: an assertion
        that cannot observe the failure it excludes.
    `VERB_TABLE[c.verb].beneficiary` discriminates the two, which is why this returns the id
    rather than a tri-state -- the discriminator is already in the data and a second encoding of
    it here would be §8's two owners."""
    row = VERB_TABLE.get(c.verb)
    if row is None:
        raise Unspecified(
            f"no verb_table row for {c.verb!r}, so its beneficiary cannot be read",
            "CAT-2",
            needs="a row in verb_table.yaml, or a candidate whose verb is in the table",
            law="the beneficiary is a PROPERTY OF THE VERB -- a candidate for a verb the table "
                "does not carry has no declaration to resolve, and defaulting would invent one")
    kind = row.beneficiary
    if kind == "none":
        return None
    if kind == "actor":
        return p.id
    if kind == "subject":
        return c.subject or None
    return c.operands.get(kind)


def temper(p: Person, fx: "Fixtures") -> float:
    """THE PERSON'S OWN FACTOR ON THE CHOICE TEMPERATURE (B10.28; CR-93 item 2, AR-23: a high-Focus person is less distracted, so
    his draw strays less from what he most values). The `judgement` rows of site `choice_temper`, read by `options._judgement_factor`
    as `competence` reads its own: `about_mid(held, floor, ceiling, gain)`, exactly 1 at the scale's mid-point and at gain 0, and
    1.0 where no row is authored or `p` holds no value at the row's key (a READ, never a default). `decision/` names no attribute
    (U1 §8): the key is the row's.

    ⚠ THE SIGN. `about_mid` RISES with the attribute, so a temperature that FALLS with Focus needs a NEGATIVE `temper_gain`; the
    shipped value is the control, 0 (H-476). A gain above 0 would make a focused person the more distracted, and a gain at or
    below -1 would take the factor to 0 at the top of the scale, where `_sample_order`'s `tau == 0` short-circuit would hand him
    the score order and its `(verb, subject)` tie-break, the alphabet H-96's sampler removes. Both are refused where read."""
    rows = judgement_rows(CHOICE_TEMPER)
    for row in rows:
        gain = fx.get(row.gain)
        if not -1.0 < gain <= 0.0:
            raise ValueError(f"{row.gain} {gain!r} is outside (-1, 0] (H-476): above 0 a focused person draws more widely, and at -1 "
                             "the factor reaches 0 at the scale's ceiling and the draw is lost")
    factor = judgement_factor(p, rows, fx)
    return 1.0 if factor is None else factor


def _sample_order(ranked: list, score, p: Person, fx: "Fixtures", draw) -> list:
    """`U4` / `H-96`: the triage stops being decided by the SPELLING of a verb.

    THE DEFECT. `H-96` records that only a handful of
    candidates carry a nonzero conviction score and that the triage is *"decided, for most
    candidates, BY ALPHABETICAL ORDER OF THE VERB'S NAME"* (`hole_register.yaml`, H-96's `hole:`).
    A design in which adding a correct verb makes the world
    do LESS, because of where its name falls in the alphabet, has its triage in the wrong place.

    THE FIX IS PLACKETT-LUCE VIA GUMBEL, and it is one line of arithmetic for a reason. Adding
    `-log(-log(u))` to `score/tau` and sorting descending samples an ORDER without replacement
    whose probabilities are `softmax(score/tau)` — so this generalises the score ranking rather than
    replacing it: as `tau -> 0` the score term dominates and the order converges on the score
    order, with the residual ties broken by the DRAW instead of by the alphabet. An ORDER is what
    is needed, not a pick: `pack_scenes` takes the ranked list and slices it by budget, so a
    chooser that sampled a single winner would leave the rest of the triage alphabetical.

    ⚠ `tau == 0` SHORT-CIRCUITS TO THE SCORE-ORDER PATH, AND THE ARM VALIDATES THE PLUMBING RATHER THAN
    THE SAMPLER. The zero-temperature limit of a softmax over TIED scores is uniform over the tied
    set, not the alphabetical order — so byte-identity at `tau = 0` needs this discontinuous case,
    and that case then exercises the score-order code. The `tau = 0` arm controls that the draw is
    threaded, the signature is unchanged and nothing else moved. The sampler's own falsifier is
    renaming a verb to a name that sorts elsewhere: the executed set must not move.

    ⚠ NO SILENT FALLBACK. A missing `draw` at `tau > 0` RAISES rather than quietly returning the
    alphabetical order: that would be S42.2.1's *"a silent default does not fail; it answers,
    plausibly and wrongly, forever"* — and it would answer with the exact defect this exists to
    remove, while every instrument reported the sampler as live.

    ⚠⚠ **A SECOND CLAUSE IS NOT MET: THE DRAW IS NOT CONSTRUCTED BY THE DRIVER.** `U4` lists
    `loop/driver.py` as the file that *"constructs and passes `draw`"*, and `04:861-862` says of an
    RNG *"its generator must be constructed by the driver from the run seed and passed down exactly
    as `World` is"*. It is instead built at every CALL SITE (`harness/headless.py`,
    `harness/corpus_run.py` x2, `harness/probes.py` x2, the degree-sweep arms, and the tests).
    **The structural reason: the driver never constructs the chooser.** `SeasonDriver.season(choose,
    ...)` RECEIVES an already-built one, so the only way the driver could own the draw is to hand it
    to `choose` — and `choose`'s four-parameter signature, which `U4` itself insists must not change, keeps the world
    out of it (`test_decision_package_never_names_world_anywhere_under_it` reads that nothing under `decision/` names
    `World`; no test reads the arity itself). The two clauses of
    the spec are in tension and this took the one that a test enforces.
    ⚠ SCOPE, STATED SO IT IS NOT OVERREAD: `04:858-860` scopes that sentence to **R-09's** producer
    (*"chains of events within a scene are probabilistic"*), which is unbuilt; this is R-08's
    chooser. But `04:862-863` gives its reason as *"so the roll is not built the idiomatic way first
    and retrofitted after"*, which is exactly the hazard here, and `U4`'s file list asked for the
    driver independently of `04`. **Whether a driver-owned generator is required before R-09's roll
    lands is the one question in this unit a ruling could change.**

    ⚠ **ONE CLAUSE OF THE UNIT'S SPEC IS NOT MET, AND IT IS DECLARED RATHER THAN QUIETLY DROPPED.**
    `U4` says *"the draw `purpose` includes the lap (U2)"*. The purpose is instead
    `choice:<verb>:<subject>`, seeded per `(world_seed, tick, person)` by the factory.
    `season()` runs DELIBERATE `scene_budget` times, `SeasonDriver.lap` is the index, and
    `_qualify_by_lap` re-derives act and scene ids through it. The clause is unmet for two
    reasons, and NEITHER is "there is no lap".

    **(1) STRUCTURAL — THE LAP CANNOT REACH THIS FUNCTION, AND IT IS THE SAME TENSION AS CLAUSE
    2 ABOVE.** The lap is state on the DRIVER; the chooser is built by the CALLER (clause 2's
    finding), so the driver cannot key a draw it never constructs. The only other route is to hand
    `choose` the lap, and `choose`'s four-parameter signature, which `U4` insists must not change, keeps the world out
    of it (`test_decision_package_never_names_world_anywhere_under_it`; no test reads the arity itself). A caller holding both CAN
    close over `d.lap` when it builds the draw, but that is a harness reaching past the engine, not the engine meeting the clause.

    **(2) DESIGN — IT CONTRADICTS THE KEYED-NOISE PROPERTY THIS FUNCTION IS BUILT ON**
    (the `⚠⚠` block below). The lap makes a
    candidate's noise a property of WHEN IT WAS REACHED; the whole argument for keying on
    `(verb, subject)` is that it must be a property OF THAT CANDIDATE, so that two arms of an
    experiment differ by what differed and not by a reshuffle. Under a scene tick a candidate that
    lost lap 0 keeps its margin in laps 1..4, which is a person whose TASTE is stable across a
    season while their OPTIONS move — and the options do move: what they have already realised is
    removed by `_drop_what_was_already_done`, so the later laps are them continuing down the list,
    never repeating it. A second lap is not a replay of the first; it is continuation, which is
    what R-03 asked for.

    ⚠ **AND THE CLAUSE IS NOT INERT, WHICH IS WHY THIS IS A DECISION AND NOT A SHRUG.** Wrapping
    the caller's draw as `orig(pid, f"{purpose}:r{d.lap}")` moves the run's events and content
    hash, so a reader may not conclude from "unmet" that it would change nothing.
    TAKEN UNDER `CLAUDE.md` §0's fifth step — 1..4 are silent, one option is clearly right for the
    code — rather than escalated: reasons (1) and (2) point the same way and no ruling overwrites a
    design call whose two defensible options are "unreachable" and "self-contradicting".
    ⚠ AND THE ADJACENT PRIMITIVE IS NAMED RATHER THAN IGNORED: the tree already owns a per-tick
    draw ordinal, `state/world.py::World.new_draw` (*"`S33`'s draw ordinal. Reset at the start of
    every tick by `season()`"*), and `harness/probes.py`'s own header argues the general case — *"A
    CONTENT-DERIVED draw was the second attempt and it collides whenever two draws in one tick are
    alike."* It is NOT used here for two reasons, both structural: it is a method on `World`, which
    `AX-2` bars from `decision/` by path (`04 §E.1`), and an ORDINAL would destroy the
    candidate-keyed replay this function depends on — the noise must be a property of the candidate,
    not of the order it was reached in. Recorded here because a declaration that a mechanism is
    missing, made without naming the adjacent one, is the defect this lane keeps finding."""
    tau = float(fx.get("choice_temperature")) * temper(p, fx)     # B10.28: x 1.0 is exact at the shipped gain 0
    if tau == 0 or len(ranked) < 2:
        return ranked
    if draw is None:
        raise Unspecified(
            "the choice draw", "H-96",
            needs=f"`make_chooser(fx, mint, verbs, draw)` with a draw at choice_temperature={tau}",
            law="U4/H-96 -- at a nonzero temperature the order is SAMPLED, and a chooser built "
                "without a draw would silently fall back to the alphabetical tie-break this "
                "replaces, reporting a sampler that is not running")
    keyed = []
    for c in ranked:
        # ⚠⚠ THE NOISE IS KEYED BY THE CANDIDATE, NOT DRAWN IN LIST ORDER, AND THE DIFFERENCE IS
        # WHAT MAKES A FORK ATTRIBUTABLE. ONE stream per person consumed down `ranked` would shift
        # the noise-to-candidate assignment WHOLESALE when a single candidate is added, removed or
        # reordered, and every downstream difference between two arms of an experiment would be
        # the reshuffle rather than the thing under test. `W-D` measures exactly that: whether a
        # forked decision changes a LATER one. Keying on `(verb, subject)` makes a
        # candidate's noise a property OF THAT CANDIDATE: identical candidates get identical draws
        # in both arms, so what differs between them is what actually differed.
        # ⚠ It is also the only form in which the `tau = 0` control means anything, because it is
        # the only form where a candidate's treatment does not depend on its neighbours.
        # ⚠ ONE STREAM PER CANDIDATE, AND THE RETRY ADVANCES IT. Re-calling `draw(...)` inside the
        # loop with a CONSTANT purpose would re-seed an identical `Random` and return the identical
        # value — an infinite loop wearing a retry's clothes, on the one input (`u == 0.0`) the
        # loop exists to handle. `random()` returns exactly 0.0 about once in 2^53 draws: a guard
        # that cannot do its job is not a weak guard but an absent one (`CLAUDE.md` §0.1 pt 2),
        # and a hang is the worst shape for one.
        rng = draw(p.id, f"choice:{c.verb}:{c.subject or '-'}")
        u = rng.random()
        while u <= 0.0:                   # `random()` is [0,1); log(0) is the one unusable draw
            u = rng.random()              # SAME stream, so it advances and can terminate
        g = -fmath.log(-fmath.log(u))
        # the trailing two terms are a STABLE TOTAL ORDER for exact float ties, which continuous
        # noise makes measure-zero; they are not the tie-break -- `g` is.
        keyed.append((-(score(c) / tau + g), c.verb, c.subject or "", c))
    keyed.sort(key=lambda t: t[:3])
    return [t[3] for t in keyed]


def sample_order(ranked: list, score, p: Person, fx: "Fixtures", draw) -> list:
    """`_sample_order` under a public name for `harness/decision_spread.attribute_top` (a call, not an
    alias: tests rebind `_sample_order` to observe the chooser, and the rebind must reach both)."""
    return _sample_order(ranked, score, p, fx, draw)


def score_order(cands: list, scores: dict) -> list:
    """`cands` ranked by score descending, ties by `(verb, subject)` -- THE ONE OWNER of the chooser's
    deterministic ordering (`make_chooser` and `harness/decision_spread.attribute_top` both call it).
    `scores` maps `id(c)` -> score; keyed on `id(c)` because a Candidate is not guaranteed hashable and
    `(verb, subject)` is not guaranteed unique, safe because `cands` holds every Candidate alive."""
    return sorted(cands, key=lambda c: (-scores[id(c)], c.verb, c.subject or ""))


# [JUSTIFIED: a float-tie tolerance for the attribution (two scores within it are a tie), an instrument constant and not a game number]
ATTRIBUTION_EPS = 1e-9
TERM_NAMES = ("pursuit", "stance", "fit", "aim", "risk")      # `score_terms`' tuple, in order: what `deciding_term` names


def deciding_term(cands: list, terms: list, actual: Optional[Candidate], tau: float) -> dict:
    """WHICH TERM DECIDED A TOP: THE ONE OWNER OF THE ATTRIBUTION RULE (B09.13; it was `harness/decision_spread.py::attribute_top`'s,
    moved here beside `score_order` so a reader of what the chooser saw -- the `watch` hook -- and the one that re-scores a
    candidate set (`attribute_top`) call one rule). Pure: it reads `terms` and `actual` and scores, orders and samples nothing.

    `cands` and `terms` are parallel (`score_terms`' tuples, in `cands`' order); `actual` is the top the SAMPLER chose among them
    (`sampled[0]`; `None` with no candidate); `tau` is `choice_temperature`. The tests, in order:
      1. `draw`      the sampler's top is NOT the score's top (the draw outvoted the score), or the top two scores are within
                     `ATTRIBUTION_EPS` and `tau` > 0 (the draw ordered them);
      2. `tiebreak`  the top two scores are within `ATTRIBUTION_EPS` at temperature 0 (`(verb, subject)` ordered them);
      3. otherwise the TERMS (`TERM_NAMES`) whose removal leaves the top no longer strictly ahead of the field, joined by `+`;
         `overdetermined` if no single term's removal does.
    Returns `{top, decider, margin, scores, terms, draw_kind, field_zero}`; `scores` and `terms` are parallel to `cands`. `cands`
    empty -> `top` None, `decider` `none`; one candidate -> `sole`. `draw_kind` splits the `draw` label: `tie` (the draw ordered
    a tie) against `outvoted` (it overrode a leader); `field_zero` is true when every score is within `ATTRIBUTION_EPS` of 0."""
    if not cands:
        return {"top": None, "decider": "none", "margin": None, "scores": [], "terms": [],
                "draw_kind": None, "field_zero": False}
    scores = [score_total(t) for t in terms]
    field_zero = all(abs(s) <= ATTRIBUTION_EPS for s in scores)
    if len(cands) == 1:
        return {"top": cands[0], "decider": "sole", "margin": None, "scores": scores, "terms": terms,
                "draw_kind": None, "field_zero": field_zero}
    by_id = {id(c): s for c, s in zip(cands, scores)}
    ranked = score_order(cands, by_id)                  # the chooser's own ordering, not a second copy
    index_of = {id(c): i for i, c in enumerate(cands)}
    order = [index_of[id(c)] for c in ranked]
    ai = next(i for i, c in enumerate(cands) if c is actual)
    best, second = scores[order[0]], scores[order[1]]
    margin = best - second
    if ai != order[0]:
        decider = "draw"
    elif margin <= ATTRIBUTION_EPS:
        decider = "draw" if tau > 0 else "tiebreak"
    else:
        deciding = []
        for k, name in enumerate(TERM_NAMES):
            rest = [scores[j] - terms[j][k] for j in range(len(cands))]
            if rest[ai] - max(r for j, r in enumerate(rest) if j != ai) <= ATTRIBUTION_EPS:
                deciding.append(name)
        decider = "+".join(deciding) if deciding else "overdetermined"
    draw_kind = None if decider != "draw" else (
        "tie" if margin <= ATTRIBUTION_EPS and tau > 0 and scores[ai] >= best - ATTRIBUTION_EPS else "outvoted")
    return {"top": actual, "decider": decider, "margin": margin, "scores": scores, "terms": terms,
            "draw_kind": draw_kind, "field_zero": field_zero}


class Ranked(list):
    """A deliberation's SAMPLED ORDER (`make_ranker`'s return), a plain list that also carries `decide(c)`: the deciding term
    (`deciding_term`'s label) of candidate `c` among the candidates still unspent when `c` was taken (`c` and those after
    it in the order), `""` for a candidate not in the order. `pack_scenes` reads it by `getattr` to stamp `Scene.decided`, so
    a list that is not a `Ranked` (a player's pick, a hand-built list) packs Scenes stamped `""`. It scores nothing: `decide`
    is a closure over the terms the ranker itself summed (the ones `watch` is handed).

    It carries `forgone_of(lead, chunk)` beside it (B10.24; `Scene.forgone`'s docstring): the `((verb, subject, margin), ...)` a Scene
    led by `lead` and carrying `chunk` keeps of what his scruple struck, `pack_scenes` reading it by `getattr` as it reads `decide`.
    The ranker's strike is the carrier's one writer; a list that is not a `Ranked` packs Scenes whose `forgone` is `()`."""
    decide: Optional[Callable[[Candidate], str]] = None
    forgone_of: Optional[Callable[[Candidate, list], tuple]] = None


def make_chooser(fx: "Fixtures", mint: Callable[[str, str, str], str],
                 verbs: Optional[frozenset] = None,
                 draw: Optional[Callable[[str, str], Any]] = None,
                 watch: Optional[Callable[..., None]] = None) -> Callable[..., list[Act]]:
    """§F2's decision policy as a FACTORY, so `choose(p, view, sensation, ask_budget)` keeps the
    FOUR-parameter signature §26 states while still reaching its params.

    `H-03` is the row: "grade: assumption. THE SHAPE IS RULED (§3 L1, §9, §26); only the weighting
    is open", so §G's discipline applies to the weights and not to this structure.

    Four properties, and each is checked by a test rather than asserted here:
      1. EVERY INPUT IS PERSON-SIDE -- `pursuits` (read through `person_q.crisis_weights`,
         which also reads `scar`), `stance`, `conviction` (read through `person_q.confliction`),
         the View, and the Sensation, which no term reads since REM-44. No World, no resolver-side Query. L2 by
         parameter list.
      2. It CONSUMES `pursuits` and `stance`, which #353 declares as fields and no formula in
         the chain reads -- a carrier nothing consumes is dead state (§22.1's own complaint).
      3. THE PERSON TRIAGES. `ask_budget()` is asked, not imposed; the engine never truncates.
      4. A lookup on one's own interior is indistinguishable from a deliberation at this
         boundary, and the design does not claim otherwise (§F2 property 4).

    ⚠ `mint` IS HERE BECAUSE §F2 TYPES `choose -> Act[]` AND GIVES THE PERSON NO WAY TO MINT ONE.
    An `Act` needs an id, and §33 derives every id from the world seed and the tick -- "unique per
    DRAW, not per operation" -- so a person-side function cannot produce one. That is a real gap
    between §F1's `-> Candidate[]` and §F2's `-> Act[]` and it is registered (`H-74`), not filled:
    the barrier passes a minter closed over the seed and tick, which are the CLOCK, not anybody's
    interior. Same shape as `fx`, and the AST proof still sees no `World`.

    v10 REM-30 (IN-47): the body is two halves with one owner each -- `make_ranker` (what the person
    would do, in order) and `release` (that order packed into scenes and intents) -- so the player's
    development space (`decision/sheet.py`) shares both and differs only in who picks the order.

    B09.13, THE OBSERVER HOOK: `watch(p, q, ranked, terms, sampled) -> None` is called once per deliberation that has a
    question, after the order is sampled and before it is packed. `ranked` is `score_order`'s list, `terms` the parallel
    `score_terms` tuples the chooser itself scored with, `sampled` `_sample_order`'s list -- COPIES of the lists, so a
    watcher that reorders or empties them changes nothing that is packed -- and the return value is ignored (the observer
    rule of ED-IN-0225). `None` (the default) is the chooser as it was. It exists so a reader of "what the chooser saw"
    (`harness/decision_spread.py`, `harness/interactions.py`) is handed it, not a second scoring of the same set."""
    rank = make_ranker(fx, verbs, draw, watch)

    def choose(p: Person, v: View, s: Sensation, ask_budget) -> list[Act]:
        q = getattr(v, "question", None)
        if q is None:
            return []
        return release(p, rank(p, v), ask_budget(), fx, mint, q, draw)
    return choose


def _scruple_strikes(p: Person, c: Candidate, margin: float, fx: "Fixtures", draw) -> bool:
    """B10.25 (`Fixtures scruple_temperature`, H-475): is a candidate whose `options.scruple` is `margin` > 0 struck from his order?
    At temperature 0 it is the THRESHOLD, every positive margin (today's gate, no draw read). At `T > 0` it is struck with probability
    `1 - exp(-margin / T)` on the person's own draw `scruple:<verb>:<subject>`, keyed by the candidate as `choice:` is so a fork stays
    attributable: a large margin stops him nearly always and never certainly, a small one usually gives way (and giving way is the
    fold's `scruple.overridden`). A missing `draw` at `T > 0` RAISES, as `_sample_order`'s does: it would answer with the threshold."""
    t = float(fx.get("scruple_temperature"))
    if t < 0:
        raise ValueError(f"scruple_temperature {t!r} is below 0 (H-475): a negative temperature would make a larger margin the less likely to stop him")
    if t == 0:
        return True
    if draw is None:
        raise Unspecified(
            "the scruple draw", "H-475",
            needs=f"`make_chooser(fx, mint, verbs, draw)` with a draw at scruple_temperature={t}",
            law="B10.25 -- at a nonzero temperature the strike is DRAWN, and a chooser built without a draw would silently fall back to the "
                "threshold while every instrument reported the draw as live")
    return draw(p.id, f"scruple:{c.verb}:{c.subject or '-'}").random() < 1.0 - fmath.exp(-margin / t)


def make_ranker(fx: "Fixtures", verbs: Optional[frozenset] = None,
                draw: Optional[Callable[[str, str], Any]] = None,
                watch: Optional[Callable[..., None]] = None) -> Callable[..., list]:
    """`rank(p, v) -> list[Candidate]`: THE SHIPPED POLICY'S ORDER over the person's own candidate set
    -- `opening_set`, narrowed to `verbs`, scored, struck by his scruple (the armed gate, B10.24), effort-settled and sampled -- and
    nothing packed.

    v10 REM-30 (IN-47): split out of `make_chooser` unchanged, so the automated chooser and the player's
    development space (`decision/sheet.py::development_space`) read ONE candidate set in ONE order: the
    player's sheet offers exactly this list, and a player who takes it whole is the automated chooser
    (the space's control). `[]` when the View carries no question. Person-side only, as `make_chooser`.
    `watch` is `make_chooser`'s observer hook (B09.13); the sheet builds its ranker without one."""
    def rank(p: Person, v: View) -> list:
        q = getattr(v, "question", None)
        if q is None:
            return []
        cands = opening_set(p, v, q, fx)
        if verbs is not None:
            cands = [c for c in cands if c.verb in verbs]
        # `U3`: the person's pursuits are weights over the FIFTEEN (`ED-IN-0261`), so they are projected into
        # the seven-axis basis once per deliberation; IN-08 H9's `scar_weight_shift` and IN-08 6f's
        # `confliction` damp (`confliction_weight`, H-188; damping the pursuit pull, never
        # inverting it [ASSUMPTION: no source states how strain enters the score]) are hoisted the
        # same way. None depends on `c`; `deliberation_memo` is their owner.
        # v9 IN-18 `G2`: term 2 by the role the subject plays (`stance_term`; `legacy` is the
        # pre-G2 `stance_toward(p, c.subject)`). `memo` holds one regard per subject per call, and
        # the two hoisted per-deliberation factors under tuple keys (`score_terms`).
        memo: dict = deliberation_memo(p, fx)
        # CR-17: the person's believed-odds query rides his View (`View.odds`); a View built without one
        # (a test's, a callback's) answers None and the pursuit term stays as it was.
        odds = getattr(v, "odds", None)
        _terms: dict = {}                # id(c) -> the `score_terms` tuple `score(c)` summed: what `watch` is handed
        def score(c: Candidate) -> float:
            # IN-62: the terms have ONE owner, `score_terms`; the score is `score_total` of them.
            _terms[id(c)] = t = score_terms(p, c, fx, memo, odds, q)
            return score_total(t)
        # ⚠ SCORED ONCE, NOT TWICE. `score` is pure in `c` given the closure, so each candidate is
        # scored once here and `_sample_order` reads it back from `_scores`.
        _scores = {id(c): score(c) for c in cands}
        # B10.24 (ED-IN-0261's deontological gate, moved here from `opening_set`: AFTER scoring, BEFORE the sample, so a struck
        # candidate's score is known): a candidate whose verb his scruple forbids (`options.scruple` > 0 at his `refusal_tolerance`)
        # is struck from the order. The strike is `_scruple_strikes`: the threshold at `scruple_temperature` 0, a draw on the margin above
        # it (B10.25). What is struck, with its margin and score, is kept (`Ranked.forgone_of`); a candidate with a positive margin
        # the strike leaves standing is kept too, for the fold's `scruple.overridden` (`loop/resolve.py::_scruple_overridden`).
        axis = fx.get("refusal_axis")
        tolerance = refusal_tolerance(p, axis)
        marked: list = []           # (Candidate, margin, score, struck): every candidate with a positive margin
        if tolerance is not None:
            kept = []
            for c in cands:
                margin = scruple(c.verb, axis, tolerance)
                if margin <= 0.0:
                    kept.append(c)
                    continue
                struck = _scruple_strikes(p, c, margin, fx, draw)
                marked.append((c, margin, _scores[id(c)], struck))
                if struck:
                    TRACE.note(f"{p.id} refuses {c.verb!r}: its `{axis}` alignment lies {margin:.3f} past his tolerance "
                               f"{tolerance:+.3f} toward the refused pole (ED-IN-0261)", "H-146")
                else:
                    kept.append(c)
            cands = kept
        # CP-T01-05 NPC half: the person may put effort behind a contested act (`npc_effort`); `off` is a no-op.
        cands, _scores = settle_efforts(cands, _scores, score, fx)
        ranked = score_order(cands, _scores)
        # ⚠ KEYED ON `id(c)` AND THAT IS SAFE HERE, NARROWLY: `cands` holds every Candidate alive
        # for the whole of this call, so no id can be recycled underneath the dict. A Candidate is
        # not guaranteed hashable and `(verb, subject)` is not guaranteed unique, so neither is a
        # key this can use.
        sampled = _sample_order(ranked, lambda c: _scores[id(c)], p, fx, draw)
        if watch is not None:
            # B09.13: an OBSERVER. Copies, so a watcher that mutates what it is handed changes nothing packed; the return is ignored.
            # `_terms[id(c)]` is the entry `score(c)` last wrote for a LIVE `c` (a kept effort variant stays alive, so its id is not reused).
            watch(p, q, list(ranked), [_terms[id(c)] for c in ranked], list(sampled))
        # `Scene.decided`: the rule is `deciding_term`'s, over the unspent tail the candidate heads, on the terms summed above (lazy:
        # `pack_scenes` asks once per Scene it builds, so a deliberation's candidates are not all attributed). The first
        # Scene's first act heads the whole order, which is the reading `harness/decision_spread.py` takes of it.
        order = tuple(sampled)
        at = {id(c): i for i, c in enumerate(order)}
        tau = float(fx.get("choice_temperature"))

        def decide(c: Candidate) -> str:
            i = at.get(id(c))
            if i is None:
                return ""
            tail = order[i:]
            return deciding_term(list(tail), [_terms[id(x)] for x in tail], c, tau)["decider"]

        def forgone_of(lead: Candidate, chunk: list) -> tuple:
            # B10.24: a STRUCK candidate that out-scored the Scene's lead (what he gave up for what he did), and a standing one with a
            # positive margin that this Scene carries (the act the fold looks for). `(verb, subject, margin)`, in the order struck.
            if not marked or id(lead) not in _scores:
                return ()
            lead_score = _scores[id(lead)]           # the kept candidates' (effort-settled) scores: what the Scene's lead scored
            carried = {(c.verb, c.subject) for c in chunk} | {(lead.verb, lead.subject)}
            return tuple((c.verb, c.subject or "", margin) for c, margin, score, struck in marked
                         if (score > lead_score if struck else (c.verb, c.subject) in carried))
        out = Ranked(sampled)
        out.decide = decide
        out.forgone_of = forgone_of
        return out
    return rank


def release(p: Person, ranked: list, n_scenes: int, fx: "Fixtures", mint, q: "Question",
            draw=None) -> list:
    """A person's ORDERED candidates, as the scenes they spend a budget of `n_scenes` on, with any intent
    a telling declares (`declare_intents`). The one owner of that step for both choosers: the automated
    (`make_chooser`, over `make_ranker`'s order) and the player's (`decision/sheet.py`, over the player's).
    `pack_scenes` is read BY BARE NAME here, so a rebind of `decision.choose.pack_scenes` reaches both."""
    # §26.3: the PERSON triages. The slice is the person's own choice of what to leave
    # undone, taken against a budget they ASKED for -- not an engine truncating a tail.
    # `W17`: the budgeted unit is the SCENE, so the slice is over scenes and each carries up
    # to `interactions_per_scene` of the ranked candidates. The default policy fills scenes
    # greedily in score order -- a person spends a scene on their best option and whatever
    # else it can carry, which is what "1-3 mechanical interactions" describes.
    # `U2`: `n_scenes` (the caller's `ask_budget()`) is the person's SEASON REMAINDER, not one lap's
    # allowance. The person chooses the whole of what they will do with the season they have left; the
    # driver releases `scenes_per_lap` of it per lap (`H-124`). Nothing is discarded, so S26.3's
    # *the engine never truncates* is untouched -- what the lap bounds is WHEN a chosen scene
    # runs, not WHETHER.
    # Telling `T7` (G9): what the person has chosen is known HERE, whole, before any of it runs,
    # so this is where a telling may declare a later chosen act. `intent_disclosure` 0 returns
    # the scenes untouched.
    return declare_intents(p, pack_scenes(p, ranked, n_scenes, fx, mint, occasion=q), fx, draw)


def declare_intents(p: Person, scenes: list, fx: "Fixtures", draw=None) -> list:
    """TELLING `T7` (G9, declared intent; v9 IN-16, `ED-IN-0282`): A TELLER MAY TELL A HEARER AN ACT
    THEY HAVE CHOSEN AND NOT YET DONE.

    `scenes` is the person's own triage, in the order the driver releases it (`pack_scenes`; the
    driver runs at most `scenes_per_lap` of it per lap and queues the rest). An act in a LATER
    scene than a telling is one the person has chosen and that has not run when the telling does.
    For each act carrying a `said` (a telling: the payload key `opening_set` sets on a NAMED
    own-ledger conjunct, never a verb name), the first act in a later scene that NAMES THE TELLING'S
    TOPIC -- the topic is the teller (a self-telling, Decision 3), or one of the ids the act binds
    under `rosters.yaml: intent_claim` -- is the intent it may declare. With chance
    `intent_disclosure` (`H-190`; one draw keyed by the telling's own id, so no other stream moves)
    the telling's `said` becomes `person_q.intent_said(...)`, and the told deposit lands
    `(teller, intent:<verb>, ((name, id), ...))` in each hearer's ledger. What the teller held about
    the topic is not told by THAT telling; nothing is deleted from anybody's ledger.

    ⚠ `0` RETURNS `scenes` UNTOUCHED AND TAKES NO DRAW: the control is the pre-`T7` chooser by
    construction, and the realm test observes it. ⚠ NOTHING CHECKS THAT THE ACT IS LATER DONE: the
    driver may re-deliberate and replace the queue, the fold may refuse the act, or the act may be
    one the driver drops as already realised this season (`loop/deliberate.py::
    _drop_what_was_already_done`, which this person-side function cannot see, AX-2). Reconciling a
    declared intent against what was done is `H-191`, absent. A missing `draw` at a non-zero rate
    RAISES rather than declaring every intent or none (`_sample_order`'s precedent).

    ⚠ *not yet done* holds at `scenes_per_lap` 1 (shipped, H-124); at 2 or 5 a later scene can
    release in the telling's own lap."""
    rate = float(fx.get("intent_disclosure"))
    if not 0 <= rate <= 1:           # `not ... <=`, so a NaN is refused too
        raise ValueError(f"intent_disclosure {rate} is not a chance in [0, 1] (H-190)")
    if rate == 0:
        return scenes
    conf = fx.get("confidence_default")
    for i, sc in enumerate(scenes):
        for a in sc.acts:
            pay = a.payload if isinstance(a.payload, dict) else None
            if pay is None or pay.get("said") is None:
                continue
            topic = pay.get("subject")
            intent = None
            for later in (b for s in scenes[i + 1:] for b in s.acts):
                said = intent_said(p.id, later.verb, later.payload, conf)
                if topic == p.id or topic in intent_named(said):
                    intent = said
                    break
            if intent is None:
                continue
            if draw is None:
                raise Unspecified(
                    "the intent-disclosure draw", "H-190",
                    needs=f"`make_chooser(fx, mint, verbs, draw)` with a draw at "
                          f"intent_disclosure={rate}",
                    law="T7/H-190 -- whether a telling declares an intent is a CHANCE; a chooser "
                        "with no draw would answer every telling alike")
            if draw(p.id, f"intent:{a.id}").random() < rate:
                a.payload = {**pay, "said": intent}
    return scenes


def _payload_of(c: "Candidate") -> Optional[dict]:
    """WHAT A COMPUTED ACT CARRIES: its subject, and the operands its verb's cell names.

    ⚠ `subject` STAYS EVEN WHEN NO CELL BINDS IT, because it is not only an operand. `act_refs`
    reads it to say what an act NAMES, `claim_subjects` reads it to say what a deposit is ABOUT,
    and `tell` -- whose `writes:` is empty by design -- has nothing else that knows what was told.
    Dropping it for a verb whose requirement happens not to mention `subject` would break the
    causal graph for the one verb the corpus most relies on.

    ⚠ `H-134`: A Candidate formed among several seats carries `VIA` in its operands, and it STAYS on
    the payload -- not as a binding (`binding_of` drops it; `Act.via` is what the fold reads) but
    because `loop/deliberate.py::_qualify_by_lap` re-mints the id with `act_key` from the payload,
    seeing no Candidate, and two acts of one person through two seats must not share an id.
    `opportunity_key` reads the same payload and deliberately ignores the seat (`data/verbs.py`)."""
    d = dict(c.operands or {})
    if c.subject:
        d.setdefault("subject", c.subject)
    return d or None


def pack_scenes(p: Person, ranked: list, n_scenes: int, fx: "Fixtures", mint,
                occasion: Optional["Question"] = None) -> list:
    """`H-78`: WHICH interactions share one scene. `H-76` says how many; this says which.

    `greedy` is the default policy, filling scenes in score order, declared and kept as the control.
    `one_per_scene` is the pre-ruling
    accounting. `by_subject` groups the interactions that share a subject, which is what
    `player_agency_v30.md` §6.3's "one scene opportunity pursued" describes -- an opportunity is
    an opportunity to do something ABOUT something.

    ⚠ `n_scenes` IS A COST BUDGET AND NOT A SCENE COUNT, WHICH IS WHY `U2`'s LAP BOUND IS NOT
    HERE. `take()` spends it, and an extended scene costs `extended_scene_cost` (2) against a
    plain one's 1. The scene tick bounds how many of a person's chosen scenes RUN in one lap,
    and that is a scheduling fact the driver owns (`SeasonDriver.deliberate`, `H-124`) -- not a
    second bound on the person's triage. Putting it here as a count of 1 would make every extended
    chunk cost 2 > 1 and be trimmed to a single interaction, so no extended scene could form,
    `Scene.cost` would return 1 unconditionally, and `H-77`'s three-point sweep would go INERT."""
    rule = fx.get("scene_packing_rule")
    require_member(
        rule,
        SCENE_PACKING_RULES,
        f"scene-packing rule {rule!r} is not in the roster",
        "H-78",
        law="H-78 -- nothing in the chain says WHICH interactions share a scene, so a rule "
            "outside the roster is a fourth answer nobody declared")
    per = fx.get("interactions_per_scene")
    width = 1 if rule == "one_per_scene" else (len(ranked) if per is None else per)

    decide = getattr(ranked, "decide", None)        # a `Ranked`'s: what decided a candidate (`Scene.decided`); `None` of any other list
    forgone_of = getattr(ranked, "forgone_of", None)    # a `Ranked`'s: what his scruple struck (`Scene.forgone`, B10.24); `None` of any other list

    def scene(n: int, chunk: list, lead: Optional["Candidate"] = None) -> "Scene":
        # `lead` is the candidate the Scene's first act was taken from, where `chunk` holds a rebuilt copy of it (the unaffordable effort below)
        # ⚠ `occasion=` IS NOT DECORATION. `choose` already holds the question — it refuses to
        # produce anything without one — and dropping it here is what left the act with no route
        # back to what raised it (`N3`).
        return Scene(mint(p.id, "scene", str(n)), p.id,
                     # ⚠ THE CANDIDATE'S SUBJECT REACHES THE ACT: `opening_set` computed a subject
                     # from the question's referents and `mint` folds it into the act's ID, so the
                     # act itself must carry it -- `_req_tell` reads `payload["subject"]` and
                     # `_eff_tell` needs its target.
                     #
                     # ⚠ THE OPERANDS RIDE WITH IT (`H-94`, `W-C`). The
                     # Candidate carries `operands`, derived person-side from the actor's own
                     # Tenures, the question's referent and two fixtures, so
                     # `stores(hearth(giver), kind) >= amount` has a `from`, a `kind` and an
                     # `amount` -- and the act CARRIES them, which is what makes the fold bind
                     # what the person bound. The subject is written first and the operands over
                     # it, so a cell that binds the referent under its own name (`to`, `site`)
                     # cannot disagree with `subject` about which thing that is.
                     #
                     # ⚠ G3: AND THE SEAT IT IS EXERCISED THROUGH. `via` is read person-side off
                     # the grant `person_side_eligible` admitted the verb on (`exercised_seat`,
                     # the same walk), so a remit act names the seat whose remit it is and an
                     # `own` act names none. The fold's eligibility, `_req_revoke`/`_req_confer`
                     # and the write gate ask THIS seat and no other (`04:332`).
                     # `H-134`: `seat_of` -- the seat `opening_set` formed the Candidate for where
                     # the person holds several that grant the act, else `exercised_seat`'s one.
                     # `T4`: the id is of `act_key` -- the subject, plus `tell`'s hearer (`data/verbs.py`);
                     # `H-134`: plus the seat, for a Candidate formed among several.
                     [Act(mint(p.id, c.verb, act_key(c.verb, c.subject, c.operands)), p.id, c.verb,
                          payload=_payload_of(c),
                          via=seat_of(p, c)) for c in chunk],
                     # `H-77`: `Scene.cost` prices the scene from the `slots` it fills.
                     occasion=occasion,
                     decided="" if decide is None else decide(chunk[0] if lead is None else lead),
                     forgone=() if forgone_of is None else forgone_of(chunk[0] if lead is None else lead, chunk))

    # ⚠ THE BOUND IS THE COST, NOT THE SCENE COUNT: once `extended` is set, five greedy scenes
    # cost ten against a budget of five, so a packer bounded by count would overspend by
    # construction and every season using `make_chooser` would refuse itself. The row and the
    # packer are the same mechanism seen from two sides.
    ext = fx.get("extended_scene_cost")

    def fill(cands) -> list:
        """Consecutive runs of `cands`, each filling at most `width` interaction slots (a Candidate at effort `e`
        fills `1 + e`, `Scene.slots`'s own count). With every effort 0 this is the slice by `width`."""
        runs, cur, used = [], [], 0
        for c in cands:
            need = 1 + (c.operands or {}).get(EFFORT, 0)
            if cur and used + need > width:
                runs.append(cur)
                cur, used = [], 0
            cur.append(c)
            used += need
        if cur:
            runs.append(cur)
        return runs

    def take(chunks) -> list:
        out, left = [], n_scenes
        for chunk in chunks:
            if left <= 0:
                break
            # THE PRICE IS `Scene.cost`'s, ASKED OF THE BUILT SCENE: the slots it fills, not the number of acts.
            # An extension the person cannot afford is taken as a PLAIN scene rather than
            # skipped: they still pursue the opportunity, with less in it. Skipping would be the
            # engine deciding what they leave undone, which is L1. The same for a single act at effort that
            # the budget cannot carry: it is done at effort 0.
            sc = scene(len(out), chunk)
            if sc.cost(ext) > left:
                chunk = chunk[:1]
                sc = scene(len(out), chunk)
                if sc.cost(ext) > left:
                    c0 = chunk[0]
                    sc = scene(len(out), [Candidate(c0.verb, c0.subject,
                                                    {k: v for k, v in (c0.operands or {}).items() if k != EFFORT})], lead=c0)
            out.append(sc)
            left -= sc.cost(ext)
        return out

    if rule == "by_subject":
        seen: dict = {}
        for c in ranked:
            seen.setdefault(c.subject or "", []).append(c)
        # first appearance in the ranked list, never the subject's ID: a name is not a rank (U4 removed the alphabet
        # as a tie-break for verbs; this is the same defect for subjects)
        chunks = [run for subj in seen for run in fill(seen[subj])]
    else:
        chunks = fill(ranked)
    return take(chunks)
