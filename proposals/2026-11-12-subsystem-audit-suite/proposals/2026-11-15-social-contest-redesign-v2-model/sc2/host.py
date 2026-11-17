"""sc2.host -- the HOST side of redesign-v2 as a toy: the data (rites, matters, context, disposal), the ONE bearing
reading, arrangement by power, the builder, the card, the fold, and a template renderer (a test fixture).
The module (engine.py) reads none of the tables here: the host hands it cells and numbers.
Second fix pass (2026-11-16): C3 (the rig's price), B1..B6, B9, B18, B19, C (context acting on play), D4, D6.
"""
from __future__ import annotations

import copy
import math
from dataclasses import dataclass
from typing import Optional
from types import MappingProxyType

from scmodel.dice import MU_PER_DIE, degree, level
from .engine import (SIGN, Input, Item, Present, Rite, _sole, close_odds, mood, p_carried)

ATTRS = ("focus", "reason", "attunement", "presence", "grace", "will")
GROUNDS = (("evidence", 0.8), ("consequence", 0.7), ("authority", 0.4), ("solidarity", 0.2))   # (id, weight of Reason)
MEANS = {"evidence": "logos", "consequence": "pathos", "authority": "pathos", "solidarity": "ethos"}

# ------------------------------------------------------------------ dials [every value ASSUMPTION; Jordan to correct]
SHIPPED = dict(
    pool_add=6, pool_floor=5, pool_default=2, opposition_rate=MU_PER_DIE, mid=4.0, floor=1.0, ceiling=7.0,
    fit_level="strong", answer_level="moderate", repeat_step=0.35, sense_step=0.15, involve=0.3,
    esteem_step=0.2, show=1.0, off_step=1.0, admit_step=0.5, contempt_step=1.0, ploy_step=1.5, grain_strain=0.5,
    heard_step=0.05, heard_floor=0.5, gap_step=0.25, weary_step=0.5, stay_base=1.0, stay_per_will=0.5,
    press_pull=1.0, rattle_pull=0.5, heckle=1.0, press_ob=1.25, wear=0.5, rattle_gain=1.5, rebound=1.0, reactance=0.75,
    room_level=0.5, concede_step=1.0, consent_at=2.5,
    crowd_at=12.0, crowd_lean=0.2, mood_scale=5.0, read_scale=1.0, read_blur=2.0, read_noise=0.3, bias_step=2.0, relevance=1, awe_step=0.5, comfort_step=0.5, rel_gain=0.5, flop=0.5, invite=0.5, track_step=0.2,
    temper_step=0.5, temper_break=0.75, temper_cool=0.5, grain=2.0, grudge=2.0, pride=2.0,
    start_step=2.0, presume_step=2.0, power_scale=2.0, strain_fade=0.5, recuse_at=0.25,
)
CONTROL_ZERO = dict(fit_level=None, answer_level=None, repeat_step=0.0, esteem_step=0.0, off_step=0.0, ploy_step=0.0,
                    grain_strain=0.0, start_step=0.0, awe_step=0.0, crowd_lean=0.0, heckle=0.0, room_level=0.0, heard_step=0.0,
                    gap_step=0.0, weary_step=0.0)

# the fold's writes [each ASSUMPTION; Jordan to correct]: one table, read by `fold`, `after` and the season driver
FOLD = dict(carried=0.1, accord=0.15, unmoved=0.05, accuser=0.1, acquitted=0.2, heard=0.03, contumacy=0.1,
            pressed=0.1, witness=0.1, lost=0.05, grudge_rig=0.3, reception=0.1, brute=0.2, wrong=0.1,
            legit_ruling=0.1, legit_brute=0.4, legit_wrong=0.2, legit_fall=0.5, rig_price=0.25, partial_price=0.5,
            standing=0.5, strife_ease=0.25, merits_at=1.0, fade=0.25)


def dials(**over):
    d = dict(SHIPPED); d.update(over)
    return MappingProxyType(d)


def controls(**over):
    d = dict(SHIPPED); d.update(CONTROL_ZERO); d.update(over)
    return MappingProxyType(d)


# ------------------------------------------------------------------ DATA: the closed roster of worldly matters
MATTERS = {   # kind: (carrier, who may bring, what bringing it costs)   [hook] = the carrier is proposed only
    "record":         ("Record (state/carriers.py:907)", "its holder", "disclosure: every one present now holds a claim of it"),
    "testimony":      ("Claim in the witness's own ledger (:325)", "the witness, or a side that calls him", "the witness is exposed to a press"),
    "deed":           ("deed Claim (person_q.attributed_deeds)", "anyone holding the claim", "names its source"),
    "oath":           ("oblige Tenure (:78)", "either party to it", "binds the bringer to it again"),
    "debt":           ("oblige Tenure, debt terms", "creditor or debtor", "calls the debt in: the tie is spent"),
    "title":          ("hold Tenure / Office (:1056)", "the holder", "puts the title in question"),
    "precedent":      ("case-file Record.stages of an earlier matter", "anyone who witnessed it or holds the record", "none"),
    "law":            ("Record of kind decree", "anyone", "none"),
    "treaty":         ("Record of kind covenant", "a party to it", "disclosure"),
    "rumour":         ("hearsay Claim (claim_sources)", "anyone holding it", "low weight; a known false one is a ploy"),
    "state_of_realm": ("world_q strife reading / open_era", "anyone present in the realm", "none"),
    "confession":     ("the `record:confession` an earlier questioning wrote on the case file", "the bench or the questioner", "none"),
}

# ------------------------------------------------------------------ DATA: the rites (the structures; rows are these, arranged)
PLAIN, FORMAL, SOLEMN = 4.0, 5.0, 6.0
_BOTH = ("argue", "press", "rest", "concede")
RITES = {
    "conversation": dict(silence="free", genre="dyadic", live="claim", bears="for", reply={"for": "may", "against": "may"},
                         issues=("the claim",), concede="accepts", moves={"for": _BOTH, "against": _BOTH},
                         close="hearers", turns=(1, 3), standard=PLAIN, reason_lean=0.0, floor="closed", authority="parties",
                         admits=("record", "testimony", "deed", "oath", "debt", "rumour", "state_of_realm"), disposes="none"),
    "negotiation": dict(silence="free", genre="dyadic", live="offer", bears="for", reply={"for": "may", "against": "may"},
                        issues=("the terms",), concede="accepts", moves={"for": _BOTH, "against": _BOTH},
                        close="consent", turns=(1, 3), standard=PLAIN, reason_lean=0.0, floor="closed", authority="parties",
                        admits=("record", "debt", "oath", "title", "treaty", "state_of_realm"), disposes="oblige"),
    "questioning": dict(silence="refusal", genre="judicial", live="question", bears="for", reply={"for": "may", "against": "must"},
                        issues=("the question",), concede="accepts",
                        moves={"for": ("argue", "press", "rest"), "against": ("argue", "rest", "concede")},
                        close="hearers", turns=(1, 4), standard=PLAIN, reason_lean=0.0, floor="closed", authority="parties",
                        admits=("testimony", "record", "deed", "rumour", "confession"), disposes="yield"),
    "inquisition": dict(silence="admits", genre="judicial", live="charge", bears="for", reply={"for": "may", "against": "must"},
                        issues=("fact", "justification"), concede="descends",
                        moves={"for": ("argue", "press", "rest"), "against": ("argue", "rest", "concede")},
                        close="bench", turns=(2, 5), standard=SOLEMN, reason_lean=0.2, floor="closed", authority="church",
                        admits=("testimony", "confession", "record", "deed"), disposes="ban"),
    "trial": dict(silence="refusal", genre="judicial", live="charge", bears="for", reply={"for": "must", "against": "must"},
                  issues=("fact", "definition", "justification"), concede="descends", moves={"for": _BOTH, "against": _BOTH},
                  close="bench", turns=(2, 5), standard=FORMAL, reason_lean=0.2, floor="open", authority="polity",
                  admits=("record", "testimony", "oath", "deed", "precedent", "law"), disposes="detain"),
    "debate": dict(silence="free", genre="deliberative", live="motion", bears="for", reply={"for": "may", "against": "may"},
                   issues=("the question",), concede="accepts", moves={"for": _BOTH, "against": _BOTH},
                   close="declared", quorum=2, turns=(2, 4), standard=FORMAL, reason_lean=-0.1, floor="open", authority="polity",
                   admits=("precedent", "law", "treaty", "record", "state_of_realm", "rumour"), disposes="decree"),
    "rally": dict(silence="free", genre="deliberative", live="theme", bears="for", reply={"for": "raise"}, issues=("the theme",),
                  concede="accepts", moves={"for": ("argue", "rest"), "against": ()}, close="hearers", turns=(1, 3),
                  standard=PLAIN, reason_lean=-0.3, floor="open", authority="none",
                  admits=("deed", "rumour", "state_of_realm", "oath"), disposes="none"),
    "audience": dict(silence="free", genre="deliberative", live="plea", bears="for", reply={"for": "may", "against": "may"}, issues=("the plea",),
                     concede="accepts", moves={"for": ("argue", "rest"), "against": ("argue", "press", "rest")}, close="bench", turns=(1, 2),
                     standard=FORMAL, reason_lean=0.0, floor="admitted", authority="polity",
                     admits=("record", "debt", "title", "oath", "precedent", "law"), disposes="oblige"),
}
# the tree's other rows are the SAME structure arranged by another authority (no code, no second rite). One word,
# one thing (B19): `interrogation` is Jordan's "interrogation for information", a questioning; the polity's
# inquisition is an `examination`; a `tribunal` is a panel and decides by its seats.
ALIASES = {
    "legal_trial": ("trial", {}),
    "tribunal": ("trial", dict(floor="admitted", disposes="ban", close="declared", quorum=2)),
    "arbitration": ("trial", dict(authority="parties", standard=PLAIN, floor="closed", disposes="oblige")),
    "parliamentary_debate": ("debate", {}), "council_of_state": ("debate", dict(floor="closed")),
    "excommunication_deliberation": ("debate", dict(authority="church", floor="closed", standard=SOLEMN, disposes="ban")),
    "inquisition_hearing": ("inquisition", {}),
    "examination": ("inquisition", dict(authority="polity", standard=PLAIN, disposes="detain")),
    "interrogation": ("questioning", {}),
}

# ------------------------------------------------------------------ DATA: context (era, regime, strife) as cell deltas
ERAS = {"plain": {}, "age_of_faith": {"authority": 1.4, "consequence": 0.8}, "mercantile": {"consequence": 1.4, "authority": 0.8}}
REGIMES = {
    "crown":     dict(unlawful=(), gravity=0.0, standard=0.0, reason_lean=0.0, admits_add=(), admits_drop=(), power={"polity": 1.0}, silence=None),
    "theocracy": dict(unlawful=("debate", "parliamentary_debate", "council_of_state"), gravity=0.5, standard=1.0, reason_lean=-0.1, admits_add=("confession", "oath"),
                      admits_drop=("precedent",), power={"church": 2.0}, silence="admits"),
    "commune":   dict(unlawful=("inquisition", "inquisition_hearing", "examination"), gravity=0.0, standard=-1.0, reason_lean=0.0, admits_add=("rumour",), admits_drop=(),
                      power={"guild": 1.0}, floor="open", silence=None),
}
STRIFE = {
    "peace":  dict(turns=0, unrest=0.0, gravity=0.0, care_want=0.0),
    "war":    dict(turns=-1, unrest=0.5, gravity=0.5, care_want=0.0),
    "famine": dict(turns=0, unrest=0.75, gravity=0.25, care_want=0.3),
    "schism": dict(turns=0, unrest=0.25, gravity=0.5, care_want=0.0),
}
# stasis (A-134; B24.03's `issue_rungs`): what each rung is argued from; a rung not named weighs every ground alike
ISSUE_GROUNDS = {"fact": {"evidence": 1.25, "consequence": 0.75, "solidarity": 0.75},
                 "definition": {"authority": 1.25, "consequence": 0.75},
                 "justification": {"consequence": 1.25, "solidarity": 1.25, "evidence": 0.75}}
AUTHORITY_BY_FACTION = {"Crown": "polity", "Parliament": "polity", "Church": "church", "Guild": "guild"}
DIFFICULTY = {"plain": 0.0, "routine": 0.5, "demanding": 1.0, "hard": 1.5}

# ------------------------------------------------------------------ DATA: disposal (what each outcome writes)
# (disposes, band) -> typed writes the fold performs. Band None = impasse / no verdict.
DISPOSAL = {
    "none":   {"overwhelming": ("pursuits+", "regard+", "claim:converted"), "success": ("pursuits+", "regard+"),
               "partial": ("regard+",), "failure": ("regard-", "grievance"), None: ("regard-",)},
    "yield":  {"overwhelming": ("claim:yielded", "record:confession", "regard-questioned"),
               "success": ("claim:yielded", "regard-questioned"), "partial": ("claim:hinted",),
               "failure": ("regard-",), None: ("regard-",)},
    "oblige": {"overwhelming": ("tenure:oblige", "regard+", "precedent"), "success": ("tenure:oblige", "regard+"),
               "partial": ("docket:adjourned",), "failure": ("grievance", "docket:other_forum"), None: ("docket:other_forum",)},
    "detain": {"overwhelming": ("tenure:detain", "office:stripped", "precedent", "legitimacy+"),
               "success": ("tenure:detain", "precedent", "legitimacy+"), "partial": ("tenure:oblige", "docket:adjourned"),
               "failure": ("record:acquittal", "precedent", "regard-accuser"), None: ("docket:adjourned",)},
    "ban":    {"overwhelming": ("tenure:ban", "office:stripped", "precedent"), "success": ("tenure:ban", "legitimacy+"),
               "partial": ("tenure:oblige", "docket:adjourned"), "failure": ("record:acquittal", "legitimacy-accuser"),
               None: ("docket:adjourned",)},
    "decree": {"overwhelming": ("record:decree", "faction+", "precedent", "legitimacy+"), "success": ("record:decree", "faction+"),
               "partial": ("docket:adjourned",), "failure": ("record:defeated", "faction-"), None: ("docket:adjourned",)},
}


# ------------------------------------------------------------------ the ONE bearing reading (role-free)
def _clip(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, x))


def tie(p: dict, q, people: Optional[dict] = None) -> float:
    """how another PERSON bears on him: relationships, kin, patronage, debts, and a shared faction. Own interior
    only (the faction is his own and the other's public allegiance)."""
    if q is None or q == p["id"]:
        return 0.0
    L = p.get("layers", {})
    Q = ((people or {}).get(q) or {}).get("layers", {})      # A5: patronage is one record read both ways
    x = L.get("relationships", {}).get(q, 0.0)
    x += 0.5 * (q in L.get("kin", ())) + 0.5 * (q == L.get("patron") or p["id"] in Q.get("clients", ())) \
        + 0.5 * (q in L.get("clients", ()) or Q.get("patron") == p["id"])
    x += L.get("debts", {}).get(q, 0.0)                      # +: he owes q; -: q wronged him
    if people is not None and p.get("faction") and people.get(q, {}).get("faction") == p["faction"]:
        x += 0.3                                             # one of his own (C: faction acts on play)
    return _clip(x)


PARTY_STAKE = 0.2   # [ASSUMPTION; Jordan to correct] a party's least stake in his own case: the season driver's
                    # literal (`acts._stake`, "a party always has something at stake"), moved here, its one owner


def bearing(p: dict, ref: dict, people: dict, party: bool = True) -> tuple:
    """How a referent (a matter, an item, a person) BEARS on p: (want, hold, bond), each signed -1..1.
    `ref` carries `bears: {tag: signed weight}` and/or `parties: {for:, against:}` and/or `factions: {faction: sign}`.
    want: pursuits, goals, ambitions, needs.  hold: convictions and his office's duty.  bond: persons and faction.
    A PARTY to the matter has a stake in his own case (A-139, B6: a judge who is the accused is partial): his bond
    is raised, as far as it goes, until his stake is at least PARTY_STAKE toward his own side. `party=False` reads
    what the matter touches of his own beyond being a party (how hard he prepares, `effort_of`)."""
    L = p.get("layers", {})
    b = ref.get("bears", {})
    want = sum((L.get("pursuits", {}).get(t, 0.0) + L.get("needs", {}).get(t, 0.0)
                + 0.5 * (t in L.get("goals", ())) + 0.5 * (t in L.get("ambitions", ()))) * w for t, w in b.items())
    hold = sum(L.get("convictions", {}).get(t, 0) / 5.0 * w for t, w in b.items())
    hold += sum((p.get("office") or {}).get("duty", {}).get(t, 0.0) * w for t, w in b.items())
    par = ref.get("parties", {})
    bond = tie(p, par.get("for"), people) - tie(p, par.get("against"), people)
    bond += ref.get("factions", {}).get(p.get("faction"), 0.0)
    want, hold, bond = _clip(want), _clip(hold), _clip(bond)
    sg = 1.0 if p["id"] == par.get("for") else -1.0 if p["id"] == par.get("against") else 0.0
    if party and sg and sg * (want + hold + bond) < 3.0 * PARTY_STAKE:
        bond = _clip(sg * 3.0 * PARTY_STAKE - want - hold)
    return (want, hold, bond)


def holds(p: dict, ref: dict) -> tuple:
    """what he wants and holds, tag by tag, and how the referent bears on each: ((channel, tag, weight, bear), ...)."""
    L, b, out = p.get("layers", {}), ref.get("bears", {}), []
    want = dict(L.get("pursuits", {}))
    for t, v in L.get("needs", {}).items(): want[t] = max(want.get(t, 0.0), v)
    for t in tuple(L.get("goals", ())) + tuple(L.get("ambitions", ())): want[t] = max(want.get(t, 0.0), 0.5)
    for t, w in want.items(): out.append((0, t, _clip(w, 0, 1), _clip(b.get(t, 0.0))))
    hold = {t: v / 5.0 for t, v in L.get("convictions", {}).items()}
    for t, v in (p.get("office") or {}).get("duty", {}).items(): hold[t] = max(hold.get(t, 0.0), abs(v))
    for t, w in hold.items(): out.append((1, t, _clip(w, 0, 1), _clip(b.get(t, 0.0))))
    return tuple(out)


def care(p: dict, strife: str = "peace") -> tuple:
    L = p.get("layers", {})
    w = max(list(L.get("pursuits", {}).values()) + list(L.get("needs", {}).values()) + [0.0])
    w = _clip(w + STRIFE[strife]["care_want"], 0, 1) if (L.get("pursuits") or L.get("needs")) else 0.5
    h = max(L.get("convictions", {}).values(), default=2.5) / 5.0
    rel = list(L.get("relationships", {}).values())
    f = _clip(max((abs(x) for x in rel), default=0.5), 0, 1)
    return (w, h, f)


def forum_faction(p: dict):
    """the faction a man answers for in the world's ledgers (legitimacy, standing, a rig's price): the faction of the
    seat he holds, else his own. A Church man in a Crown seat rules as the Crown; an office-holder with no faction of
    his own still has his seat's (the one owner; every legitimacy and standing write reads it)."""
    return (p.get("office") or {}).get("faction") or p.get("faction")


def power(p: dict, regime: str = "crown") -> float:
    o = p.get("office") or {}
    auth = AUTHORITY_BY_FACTION.get(o.get("faction"))
    return o.get("rung", 0) + (2.0 * level(o["modifier"]) if o.get("modifier") else 0.0) \
        + (REGIMES[regime]["power"].get(auth, 0.0) if o else 0.0)


def strain_carried(p: dict, D) -> float:
    """each rattle fades on its OWN clock, and the k-th freshest counts half the one before: bounded, no ratchet."""
    f = sorted((max(0.0, 1.0 - D["strain_fade"] * s) for s in p.get("rattled_ago", ())), reverse=True)
    return 0.5 * sum(x / 2 ** k for k, x in enumerate(f))


def conflict(stake, ties=()) -> tuple:
    """B6: a stake is a CONFLICT however it nets: (how much the matter bears on him at all, which way it leans).
    Opposite interests do not cancel to impartiality, and neither do opposite ties (A5): his bond counts as the sum of
    his ties to each party (`ties`: his tie to the one and to the other), where that is more than the bond nets to."""
    want, hold, bond = stake
    return (abs(want) + abs(hold) + max(abs(bond), min(1.0, sum(abs(x) for x in ties)))) / 3.0, sum(stake) / 3.0


def _ties(p, fid, aid):
    """a Present's ties to the two parties, from his `bonds`."""
    b = dict(p.bonds)
    return (b.get(fid, 0.0), b.get(aid, 0.0) if aid else 0.0)


def false_items(p: dict, matter: dict, side: str) -> tuple:
    """B2, D6: where a false item comes from. (1) HIS OWN FALSE WORD: when what he knows of the matter (`believes`,
    his own ledger) runs against the side he speaks for, he can assert the contrary as testimony; it is his lie, and
    he knows it. (2) A forgery is a Record its maker knows false: `[HOOK]` a forging act; in the model it is fixture
    data (`Item(sincere=False)` among his items). Nothing else makes a false item."""
    b = float(p.get("believes", {}).get(matter["id"], 0.0))
    if SIGN[side] * b < 0:
        return (Item(f"word:{p['id']}:{matter['id']}", "testimony", 0.5, source=p["id"], about=None, sincere=False),)
    return ()


def takes_side(p: dict, matter: dict, people: dict) -> Optional[str]:
    """D4: which side a man takes from what he wants: the sign of how the matter bears on him, if it bears at all."""
    s = sum(bearing(p, matter, people)) / 3.0
    return None if s == 0 else ("for" if s > 0 else "against")


def effort_of(p: dict, matter: dict, people: dict) -> int:
    """D4 'how hard': the turns he prepares, from how much the matter touches his own (being a party is not
    preparation: `party=False`): 0 a passing word .. 3."""
    st = bearing(p, matter, people, party=False)
    return int(min(3, round(3 * abs(sum(st) / 3.0) + 1))) if any(st) else 0


# ------------------------------------------------------------------ arrangement by power
def tilt(arranger: dict, weak: dict, rig: float, regime: str, D) -> float:
    return rig * max(0.0, math.tanh((power(arranger, regime) - power(weak, regime)) / D["power_scale"]))


def rig_price(t: float) -> float:
    """C3: what a rig costs the arranger's faction in legitimacy: it is seen as plainly as it is pushed (a light hand
    passes for custom; a packed bench and a shut door are plain), and shutting the door hides nothing (a closed court
    is itself a sign), so the price is the tilt times how plainly it is seen, which is the tilt: rig_price x tilt^2.
    Monotone in the rig; no discount for secrecy."""
    return FOLD["rig_price"] * t * t


@dataclass(frozen=True)
class Card:
    """A-133: what the proceeding IS, derived from data; every field is checked against the sitting."""
    kind: str
    genre: str
    arranged_by: Optional[str]  # who tilted the forum; None where nobody did (C3: no arranger named without a tilt)
    tilt: float
    tilted_against: Optional[str]  # the side the tilt works against (C3: resentment and appeal follow it)
    stake: str
    outcomes: tuple
    room: tuple
    live: str
    bears: str
    reply: tuple
    moves: tuple
    barred: tuple
    admits: tuple
    close: str
    decided_by: tuple          # the adjudicators; () under consent: each party's own accept
    turns: int
    issues: tuple
    silence: str               # what not answering a standing point means here (A-145)
    unargued: str              # what happens to the matter if nobody speaks (C1: the burden)
    ends: str                  # when it closes: the forum's time is the measure of readiness (D5)
    standard: float            # the Grace the occasion expects
    unrest: float              # the pull of the times on every speaker (Focus holds against it, B14)
    gravity: float             # how grave the times make a change (an obstacle on the bearer at the close)
    reason_weight: tuple       # ((ground, share of Reason in the dice here), ...)
    recused: tuple             # seats that stepped down for a conflict (B6)
    odds: Optional[float]      # P(carried) if nobody speaks (an unpressed charge lapses), before an ordinary bench; None under consent or
                               # where the verdict is the speech itself (the abridged form: the option's own chance)


def _silence_says(inp, rite) -> str:
    """the card's `silence`: the cell, and what a point left unanswered costs with those who decide (A-145)."""
    if rite.silence == "free":
        return "free: nothing here must be answered, and silence costs nothing"
    from .engine import silence_cost, _lead
    ds = [p for p in inp.room if p.decides]
    owes = _lead(inp, "against" if dict(rite.reply).get("against") == "must" else rite.bears) or ds[0]
    c = sum(silence_cost(inp, d, None, owes) for d in ds) / len(ds) if ds else 0.0     # (a man is not contemptuous
                                                                                      # of himself: a deciding party)
    return f"{rite.silence}: a point owed an answer and left standing costs {c:.2f} with each who decides" \
        + (", and counts with him again as tacitly admitted" if rite.silence == "admits" else "")


def lawful(regime: str, row: str) -> bool:
    """B7: whether a row may sit under a regime: the regime's `unlawful` list names the ROWS it outlaws (a theocracy
    the polity's debates, not the Church's own deliberation on the debate rite)."""
    return row not in REGIMES[regime]["unlawful"]


def build(people: dict, rite_id: str, matter: dict, *, bench=(), floor=(), form="full", era="plain", regime="crown",
          strife="peace", arranger=None, rig=0.0, effort=None, difficulty="routine", D=None, state=None,
          flat=(), decides_also=(), grounds_for=None):
    """-> (Input, Card). `flat`: layers to flatten for a control arm: any of 'bearing', 'context', 'power'.
    `form`: 'full', 'abridged', or 'auto' (D6: the abridged form for a passing word nobody watches)."""
    D = D or dials()
    if "context" in flat:
        era, regime, strife = "plain", "crown", "peace"
    gone = [q for q in (matter["parties"].get("for"), matter["parties"].get("against"), arranger) if q and q not in people]
    if gone:
        raise ValueError(f"refused[absent]: {gone[0]} is not in the world (a party or arranger who is gone)")
    bench = tuple(q for q in bench if q in people)          # a seat whose holder is gone sits empty, as a vacated one
    floor = tuple(q for q in floor if q in people)
    rid, over = ALIASES.get(rite_id, (rite_id, {}))
    if not lawful(regime, rite_id):
        raise ValueError(f"refused[unlawful]: {rite_id} is not lawful under {regime}")
    r = copy.deepcopy(RITES[rid]); r.update(over)
    R, S = REGIMES[regime], STRIFE[strife]
    fid, aid = matter["parties"]["for"], matter["parties"].get("against")
    if aid is not None and aid == fid:
        raise ValueError("refused[one_party]: the two parties to a matter are one character (A-139)")
    floor = tuple(floor)
    if aid is None and r["moves"].get("against"):            # D4: who comes to oppose: the most opposed of the floor
        opp = [f for f in floor if takes_side(people[f], matter, people) == "against"]
        if opp:
            aid = min(opp, key=lambda f: sum(bearing(people[f], matter, people)))
            floor = tuple(f for f in floor if f != aid)
            matter = dict(matter, parties=dict(matter["parties"], against=aid))
    A, B = people[fid], (people[aid] if aid else None)
    if effort is None:
        effort = effort_of(A, matter, people)
    if form == "auto":
        form = "abridged" if (effort <= 0 and not floor) else "full"
    # ---- who arranges, and against whom (C3: his side is his own if he is a party; else the side his ties favour)
    arr = people[arranger] if arranger else (A if rig > 0 else None)      # the bearer convenes unless another does
    t, arr_side = 0.0, None
    if arr is not None:
        if arr["id"] == fid or (B is not None and arr["id"] == aid):
            arr_side = "for" if arr["id"] == fid else "against"
        else:                                        # B9: a third party leans to the side he is tied to; tied to
            lean = tie(arr, fid, people) - (tie(arr, aid, people) if B is not None else 0.0)    # neither more, no tilt
            arr_side = "for" if lean > 0 else "against" if lean < 0 else None
        weak = None if arr_side is None else (B if arr_side == "for" else A)
        if weak is not None and "power" not in flat:
            t = tilt(arr, weak, rig, regime, D)
    weak_side = None if t <= 0 else ("against" if arr_side == "for" else "for")
    close = r["close"]
    moves = {s: tuple(m) for s, m in r["moves"].items()}
    lo, hi = r["turns"]
    turns = max(lo, min(hi, effort + 1) + S["turns"])          # C3: the rig no longer cuts turns (it cut the arranger's own case)
    if form == "abridged":
        moves, turns, close = {"for": ("argue",), "against": ()}, 1, "exchange"
    # ---- who sits: the seats' own faction against the rite's authority; recusal (B6)
    seats = [people[b] for b in bench]
    if r["authority"] not in ("parties", "none"):
        seats = [p for p in seats if AUTHORITY_BY_FACTION.get((p.get("office") or {}).get("faction")) == r["authority"]]
    recused = []
    if close in ("bench", "declared"):
        seats.sort(key=lambda p: -(p.get("office") or {}).get("rung", 0))
        need = 1 if close == "bench" else (r.get("quorum") or 1)
        for p in list(seats):                                # a party who sits is partial by choice and seen (A-139)
            c, _ = conflict(bearing(p, matter, people), (tie(p, fid, people), tie(p, aid, people)))
            if p["id"] not in (fid, aid) and c >= D["recuse_at"] and len(seats) > need:
                seats.remove(p); recused.append(p["id"])          # he steps down; a conflicted seat who cannot sits and pays
        if close == "bench" and B is None and len(seats) > 1 and seats[0]["id"] == fid:
            seats = seats[1:] + seats[:1]            # A10: the sole speaker is not his own only listener: the next seat presides
        if not seats:
            raise ValueError(f"refused[no_seat]: {rid}: no seat of authority {r['authority']} (party-gap refusal)")
        if len(seats) < need:
            raise ValueError(f"refused[short_bench]: {rid}: {len(seats)} seat(s) for a quorum of {need}")
    fl = r["floor"] if "floor" not in R else R["floor"]
    fl_ids = [] if fl == "closed" else [f for f in floor if fl == "open" or people[f].get("office")]
    absent = set(matter.get("absent_in", {}).get(strife, ()))
    fl_ids = [f for f in fl_ids if f not in absent]
    seated = seats[:1] if close == "bench" else seats if close == "declared" else fl_ids if close == "hearers" else []
    if t > 0 and not [q for q in seated if (q if isinstance(q, str) else q["id"]) not in (fid, aid)]:
        t, weak_side = 0.0, None             # B5: an arrangement tilts those who decide; where none but a party decides
                                             # (a conversation, a questioning, a negotiation) there is nothing to tilt
    admits = tuple(dict.fromkeys(k for k in r["admits"] + R["admits_add"] if k not in R["admits_drop"]))   # once each
    eraw = ERAS[era]
    grounds = tuple((g, c, eraw.get(g, 1.0)) for g, c in GROUNDS)
    rite = Rite(id=rid, live=r["live"], reply=tuple(r["reply"].items()), issues=tuple(r["issues"]), concede=r["concede"],
                moves=tuple(moves.items()), close=close, turns=turns, standard=r["standard"] + R["standard"],
                reason_lean=r["reason_lean"] + R["reason_lean"], admits=admits, difficulty=DIFFICULTY[difficulty],
                gravity=S["gravity"] + R["gravity"], quorum=r.get("quorum"), unrest=S["unrest"], bears=r["bears"],
                weighs=tuple((i, tuple(ISSUE_GROUNDS[i].items())) for i in r["issues"] if i in ISSUE_GROUNDS),
                silence=r["silence"] if (R["silence"] is None or r["silence"] == "free" and "must" not in r["reply"].values()) else R["silence"])
    speak_against = bool(moves.get("against")) and B is not None
    room, in_room = [], set()

    def present(p, side, decides):
        st = (0.0, 0.0, 0.0) if "bearing" in flat else bearing(p, matter, people)
        ln = D["start_step"] * sum(st) / 3.0
        if decides and side is None:                              # a seat: the arrangement's presumption (the rig's
            if t > 0:                                             # one lever, A-132), and D1: an appeal's grounds
                ln += t * D["presume_step"] * SIGN[arr_side]
            if grounds_for:
                ln += grounds_for[1] * D["presume_step"] * SIGN[grounds_for[0]]
        a = p.get("attributes", {})
        its = tuple(p.get("items", ())) + (false_items(p, matter, side) if side else ())
        wt = p.get("weight", 1)
        if isinstance(wt, bool) or not isinstance(wt, (int, float)) or wt != int(wt):
            raise ValueError(f"refused[bad_weight]: {p['id']} weighs {wt!r}: a weight is a whole number of heads")
        return Present(id=p["id"], weight=int(wt), side=side, decides=decides,
                       **{k: float(a.get(k, 4)) for k in ATTRS}, rank=float(p.get("rank", 0)),
                       care=(0.5, 0.5, 0.5) if "bearing" in flat else care(p, strife), stake=st,
                       bonds=() if "bearing" in flat else tuple((q, tie(p, q, people)) for q in people if q != p["id"] and tie(p, q, people)),
                       holds=() if "bearing" in flat else holds(p, matter), start=ln, believes=float(p.get("believes", {}).get(matter["id"], 0.0)), bias=float(p.get("bias", 0.0)),
                       power=0.0 if "power" in flat else power(p, regime),
                       precedence=int((p.get("office") or {}).get("rung", 0)),
                       items=its, strain=strain_carried(p, D))

    def add(p, side, decides):
        if p["id"] not in in_room:
            in_room.add(p["id"]); room.append(present(p, side, decides))
        elif decides:                       # one person, two cells: a party who also adjudicates (a noble, an inquisitor)
            k = [q.id for q in room].index(p["id"]); room[k] = present(p, room[k].side, True)

    add(A, "for", False)
    if B is not None:
        add(B, "against" if speak_against else None, close in ("exchange", "hearers"))
    if close in ("bench", "declared") or (close == "exchange" and B is None):
        for s in (seats if close == "declared" else seats[:1]):
            add(s, None, True)
    for f in fl_ids:
        add(people[f], None, close == "hearers")
    frames = tuple(sorted({(c, t_) for p in room for c, t_, _, _ in p.holds}))
    inp = Input(rite=rite, matter=matter["id"], room=tuple(room), grounds=grounds, dials=D, state=state, frames=frames)
    disp = matter.get("disposes", r["disposes"])
    barred = tuple((s, m) for s in ("for", "against") for m in _BOTH if m not in moves.get(s, ()) and moves.get(s))
    from .engine import _crowd
    rw = tuple((g, round(min(1.0, max(0.0, c + rite.reason_lean - D["crowd_lean"] * _crowd(inp))), 1)) for g, c, _ in grounds)
    must_b = dict(rite.reply).get("against") == "must" and rite.silence != "free"
    from .engine import silence_cost, _lead
    bearer, ds_ = _lead(inp, rite.bears), [p for p in room if p.decides]
    unmoved = -sum(silence_cost(inp, d, None, bearer) for d in ds_) / len(ds_) if (must_b and bearer and ds_) else 0.0
    # A-133: the card's odds are the close's own where nobody speaks: each who decides at his own start (bearing, the
    # rig's presumption, an appeal's grounds; the packed bench as it sits), less the unput charge where the bearer must
    # put it (his rest is priced as silence), drawn as the close draws (the quorum over the seats' own draws)
    quiet = {d.id: d.start - (SIGN[rite.bears] * silence_cost(inp, d, None, bearer) if (must_b and bearer) else 0.0) for d in ds_}
    card = Card(kind=rite_id, genre=r["genre"], arranged_by=arr["id"] if (arr and t > 0) else None, tilt=round(t, 2),
                tilted_against=weak_side,
                stake=disp, outcomes=tuple(DISPOSAL[disp].items()),
                room=tuple((p.id, (("speaks " + p.side) if p.side else ("judges" if p.decides else "attends")),
                            round(p.power, 1)) for p in room),
                live=r["live"], bears=r["bears"], reply=rite.reply, moves=rite.moves, barred=barred,
                admits=admits, close=close, decided_by=tuple(p.id for p in room if p.decides), turns=turns,
                issues=rite.issues, silence=_silence_says(inp, rite),
                unargued=(f"it lapses: the bearer must put it, and his rest is priced as silence ({-unmoved:.2f} with those who decide)" if must_b
                          else "it stands where the room starts"),
                ends="when the turns are spent, a whole round rests, or a side yields",
                standard=rite.standard, unrest=rite.unrest, gravity=rite.gravity, reason_weight=rw,
                recused=tuple(recused),
                odds=round(close_odds(inp, quiet), 3) if close in ("bench", "declared", "hearers") else None)
    return inp, card


# ------------------------------------------------------------------ the host's read of the verdicts, and the fold
_RANK = {"failure": 0, "partial": 1, "success": 2, "overwhelming": 3}


def act_band(inp, out):
    """(band, margin, veto). Drawn closes: `bench` the presiding verdict; `declared` the QUORUM-th best seat's
    margin, so a majority carries and the presiding seat is one vote (C5); `hearers` the weight-mean. Consent:
    whether a party ACCEPTED (his act): the party addressed accepting is Success, the bearer withdrawing is Failure,
    neither is an impasse (band None). Never the actor's last exchange."""
    if out.ended == "yielded":                   # a yield that IS a decision: the bearer drops the matter (nothing is
        y = next(p for p in inp.room if p.id == out.ended_by)          # left to decide), or a party who decides gives
        if inp.rite.close == "consent" or y.side == inp.rite.bears or _sole(inp, y):   # way and his verdict alone is
            return ("success" if y.side != inp.rite.bears else "failure"), None, False   # the close (his own accept);
                                                                         # otherwise the bench draws (A-14): one seat, one vote
    if inp.rite.close == "consent":
        return None, None, False
    w = {p.id: p.weight for p in inp.room}
    if inp.rite.close == "hearers":
        W = sum(w[i] for i, _ in out.verdicts)
        m = sum(w[i] * (v.net - v.ob) for i, v in out.verdicts) / W
    elif inp.rite.close == "declared":
        ms = sorted((v.net - v.ob for _, v in out.verdicts), reverse=True)
        m = ms[min(len(ms), inp.rite.quorum or 1) - 1]
    else:
        m = out.verdicts[0][1].net - out.verdicts[0][1].ob
    band = "failure" if m < 0 else "partial" if m < 1 else "success" if m < 3 else "overwhelming"
    return band, m, False


def new_world():
    return dict(tenures=[], offices={}, case_files={}, ledgers={}, regard={}, pursuits={}, standing={}, legitimacy={},
                strife={}, precedents=[], docket=[], rattled={}, events=[], compliance={}, appeal_weight={}, reception=[],
                refused=[])


def bounded(x, d):
    """B9: a bounded quantity (regard, legitimacy, standing) moves by `d` toward its bound and never past it: a step
    is worth less the nearer the bound it pushes, and nothing runs away. The step is at most the whole way (|d| <= 1)
    and the result stays in [-1, 1] whatever is handed in (A2, C8: a step over 1 overshot the bound)."""
    x, d = _clip(x), _clip(d)
    return _clip(x + d * (1.0 - x) if d > 0 else x + d * (1.0 + x))


def merits(inp, out):
    """B5: the merits AS THE RECORD SHOWS THEM: how far the sitting itself moved those who heard it (each listener's
    track less where his own stake and the arrangement started it), weight-mean, toward `for`."""
    T = dict(out.state.tracks)
    ls = [p for p in inp.room if p.side is None] or [p for p in inp.room if p.decides]
    W = sum(p.weight for p in ls) or 1
    return sum(p.weight * (T[p.id] - p.start) for p in ls) / W


def reception(inp, j):
    """A-144(6), B5: `brute`, how far his station outstrips his respectability, both read on ONE scale, the
    attribute scale: his station is his power (a rung a point, as `power` counts it) held to floor..ceiling, his
    respectability his Grace; the brute is the shortfall as a share of the scale, 0..1. Monotone in rung, modifier
    and regime weight, and in Grace; a mid judge of a mid seat (Grace 4, rung 3 under a crown: power 4) is no brute,
    a Grace-1 judge of the highest seat wholly one, and a Grace-7 judge never (A7: the old tanh station saturated at
    any office, so every judge below Grace 5.6 was a brute)."""
    D = inp.dials
    station = min(D["ceiling"], max(D["floor"], j.power))
    brute = max(0.0, station - j.grace) / (D["ceiling"] - D["floor"])
    return brute, 1.0 - brute


def fold(world, people, inp, card, out, matter):
    """The toy fold: performs EVERY write of the DISPOSAL row for (card.stake, band), then the hooks every sitting
    leaves. Bounded writes (B9). The module wrote nothing. Returns (band, writes)."""
    band, m, _ = act_band(inp, out)
    F = FOLD
    fid, aid = matter["parties"]["for"], matter["parties"].get("against")
    if aid is None:
        aid = next((p.id for p in inp.room if p.side == "against"), None)
    writes, R = [], world["regard"]

    def w(kind, *a):
        writes.append((kind,) + a)

    def reg(x, y, d, why):
        if x and y and x != y and d:
            R[(x, y)] = bounded(R.get((x, y), 0.0), d); w("regard" + ("+" if d > 0 else "-"), x, y, why)

    def legit(f, d):
        if f:
            world["legitimacy"][f] = bounded(world["legitimacy"].get(f, 0.0), d)

    def standing(f, d):
        if f:
            world["standing"][f] = bounded(world["standing"].get(f, 0.0), d)

    won = band in ("success", "overwhelming")
    ruling = inp.rite.close in ("bench", "declared") and band is not None
    ds = sorted((p for p in inp.room if p.decides), key=lambda p: (-p.precedence, p.id))
    j = ds[0] if ruling else None
    jf = forum_faction(people[j.id]) if j else None
    world["events"].append((matter["id"], card.kind, out.ended, band))
    world["case_files"].setdefault(matter["id"], []).append((card.kind, out.ended, band, len(out.beats)))
    w("case_file:stage", matter["id"])
    hearers = [p for p in inp.room if p.side is None]
    for op in DISPOSAL[card.stake][band]:
        if op.startswith("tenure:"):                     # on the other party; a granted plea binds the authority that granted it
            on = aid or (card.decided_by[0] if card.decided_by else None)
            if on:
                world["tenures"].append((op[7:], on, matter["id"])); w(op, on)
        elif op == "office:stripped":
            if aid and people[aid].get("office"):
                world["offices"][aid] = "contested"; w(op, aid)
        elif op.startswith("record:"):
            world["case_files"][matter["id"]].append(("record", op[7:])); w(op, matter["id"])
            if op == "record:confession" and aid:          # a worldly matter later sittings can show (MATTERS: confession)
                world["precedents"].append(Item(f"conf:{matter['id']}", "confession", 0.8, source=aid, about=aid))
        elif op == "precedent":
            world["precedents"].append(Item(f"prec:{matter['id']}", "precedent", min(1.0, 0.5 + abs(m or 0) / 6.0),
                                            source=card.decided_by[0] if card.decided_by else None, about=aid)); w(op, matter["id"])
        elif op.startswith("docket:"):
            world["docket"].append(dict(matter=matter["id"], kind=op[7:], party=fid, weight=0.0)); w(op, matter["id"])
        elif op == "grievance":                            # B3: a grievance needs someone who caused it: the other
            if aid and any(x.mover == aid for x in out.beats):   # party spoke against him (a tell's listener did not)
                world["docket"].append(dict(matter=matter["id"], kind="grievance", party=fid, against=aid, weight=0.0)); w(op, fid)
        elif op in ("faction+", "faction-"):
            standing(forum_faction(people[fid]), F["standing"] * (1 if op[-1] == "+" else -1)); w(op, forum_faction(people[fid]))
        elif op == "legitimacy+":
            if jf:                                         # the forum's authority, which ruled
                legit(jf, F["legit_ruling"] * (1.0 - card.tilt)); w(op, jf)
        elif op == "legitimacy-accuser":                   # a charge that failed discredits whoever BROUGHT it (the same
            legit(forum_faction(people[fid]), -F["legit_fall"]); w(op, forum_faction(people[fid]))   # shape as
                                                           # `regard-accuser`); a right acquittal never discredits the court
        elif op == "regard+":
            for p in hearers:
                reg(p.id, fid, F["carried"], "carried")
            reg(aid, fid, F["accord"], "accord"); reg(fid, aid, F["accord"], "accord")
        elif op == "regard-":
            for p in hearers:
                reg(p.id, fid, -F["unmoved"], "unmoved")
            reg(aid, fid, -F["unmoved"], "importuned")
        elif op == "regard-accuser":
            for p in hearers:
                reg(p.id, fid, -F["accuser"], "a charge that failed")
            reg(aid, fid, -F["acquitted"], "accused and acquitted")
        elif op == "regard-questioned":
            reg(aid, fid, -F["accuser"], "made to yield")
        elif op == "pursuits+":
            for p in hearers:
                world["pursuits"][p.id] = bounded(world["pursuits"].get(p.id, 0.0), F["carried"]); w(op, p.id)
        elif op == "claim:converted":
            for p in hearers:
                world["ledgers"].setdefault(p.id, []).append(("converted", fid, matter["id"])); w(op, p.id)
        elif op == "claim:yielded":
            world["ledgers"].setdefault(fid, []).append(("yielded", aid, matter["id"], 1.0)); w(op, fid)
        elif op == "claim:hinted":
            world["ledgers"].setdefault(fid, []).append(("yielded", aid, matter["id"], 0.4)); w(op, fid)
        else:
            raise KeyError(op)
    # ---- ADJUDICATOR'S GRACE (A-144): how a RULING is received, apart from whether it was right (B3, B5)
    loser = winner = None
    if aid and band is not None:
        loser, winner = (aid, fid) if won else (fid, aid)
    if j is not None:
        brute, rec = reception(inp, j)
        mer = merits(inp, out)
        wrong = band != "partial" and ((won and mer < -F["merits_at"]) or (not won and mer > F["merits_at"]))
        legit(jf, (F["legit_ruling"] * rec if not wrong else -F["legit_wrong"]) - F["legit_brute"] * brute * (2.0 if wrong else 1.0))
        comp = round((1.0 + rec) / 2.0 * (0.6 if wrong else 1.0), 2)
        world["compliance"][matter["id"]] = comp
        world["reception"].append((j.id, round(rec, 2), wrong))
        cj, lean = conflict(j.stake, _ties(j, fid, aid))
        favoured = (won and lean > 0) or (not won and band != "partial" and lean < 0)
        for p in inp.room:
            if p.id == j.id:
                continue
            if p.id == loser:
                d = -F["brute"] * brute - (F["wrong"] if (wrong or card.tilt > 0 or (cj > 0 and favoured)) else 0.0)
            elif p.id == winner:
                d = F["reception"] * rec
            else:
                d = (F["reception"] * rec - F["brute"] * brute) if not wrong else -(F["wrong"] + F["brute"] * brute)
            reg(p.id, j.id, d, "how he ruled")
        if cj > 0 and favoured:                            # B6: a conflicted judge who rules his own way pays
            legit(jf, -F["partial_price"] * cj); w("partial_paid", j.id)
        if brute > 0:
            standing(jf, -F["brute"] * brute)
        aw = brute + (0.5 if wrong else 0.0) + (card.tilt if (loser and _party_side(fid, aid, loser) == card.tilted_against) else 0.0)
        if loser:
            world["appeal_weight"][matter["id"]] = round(aw, 3)
        w("reception", j.id, round(rec, 2))
    T = dict(out.state.tracks)
    broke_logged = set()
    for p in inp.room:
        led = world["ledgers"].setdefault(p.id, [])
        for b in out.beats:
            if b.rattled:
                led.append(("rattled", b.rattled, b.mover))
            if p.id in b.caught:
                led.append(("hypocrite", b.voice, round(b.insincere, 2)))      # B2: from what HE saw
            if b.item:
                led.append(("shown", b.item, b.voice))
            if b.move == "concede":
                led.append(("conceded", b.mover, b.closed))
            if b.evaded:
                led.append(("contumacy", b.mover, b.issue))
            if b.broke and (p.id, b.mover) not in broke_logged:
                broke_logged.add((p.id, b.mover)); led.append(("lost his temper", b.mover, b.n))   # C4: once
        if card.tilt > 0 and p.id != card.arranged_by:
            led.append(("rigged", card.arranged_by, card.tilt))
        if p.decides:
            c, ln = conflict(p.stake, _ties(p, fid, aid))
            if c > 0:
                for q in inp.room:
                    if q.id != p.id:
                        world["ledgers"].setdefault(q.id, []).append(("partial", p.id, round(c, 2), round(ln, 2)))
        if p.side is None:                                 # B21: what a bystander heard, never a ruling
            mv = T[p.id] - p.start
            reg(p.id, fid, F["heard"] * mv, "what he heard")
            if aid and any(q.id == aid and q.side for q in inp.room):
                reg(p.id, aid, -F["heard"] * mv, "what he heard")
            if not p.decides:
                led.append(("heard", fid, matter["id"], round(mv, 2)))
    for d_id, dep in out.ruled:
        if dep > 0:
            for q in inp.room:
                world["ledgers"].setdefault(q.id, []).append(("ruled against the room", d_id, dep))
    for b in out.beats:
        if b.evaded:
            for p in inp.room:
                if p.decides and p.id != b.mover:
                    reg(p.id, b.mover, -F["contumacy"], "he would not answer")
        if b.move == "press" and b.target and b.rattled:
            reg(b.target, b.mover, -F["pressed"], "pressed")
        if b.rattled:
            world["rattled"].setdefault(b.rattled, []).append(0); w("strain_carried", b.rattled)
        if b.voice != b.mover:
            reg(aid if b.side == "for" else fid, b.voice, -F["witness"], "testified against him")
            reg(b.mover, b.voice, F["witness"], "stood by him")
    if aid and band is not None:
        for pid, sgn in ((fid, 1.0), (aid, -1.0)):
            st = sum(bearing(people[pid], matter, people)) / 3.0
            world["pursuits"][pid] = bounded(world["pursuits"].get(pid, 0.0), (1.0 if won else -1.0) * sgn * abs(st))
        if inp.rite.close != "consent":
            reg(loser, winner, -F["lost"], "lost to him")
        if card.tilt > 0:
            legit(forum_faction(people[card.arranged_by]), -rig_price(card.tilt)); w("legitimacy-", card.arranged_by)
            if _party_side(fid, aid, loser) == card.tilted_against:      # B8: the PARTY rigged against, moves or none
                reg(loser, card.arranged_by, -F["grudge_rig"] * card.tilt, "rigged against him")   # C3: the grievance
    if matter.get("strife") and band is not None and won and card.stake in ("decree", "oblige", "detain", "ban"):
        k = matter["strife"]                               # B3: only what the sitting RESOLVED moves a strife
        if k in world["strife"]:
            world["strife"][k] = max(0.0, world["strife"][k] - F["strife_ease"]); w("strife", k)
    return band, tuple(writes)


def _party_side(fid, aid, pid):
    """the side a man is a PARTY to (not the side he speaks: in a rally the opposing party has no moves)."""
    return "for" if pid is not None and pid == fid else "against" if pid is not None and pid == aid else None


# ------------------------------------------------------------------ the renderer (a TEST FIXTURE: beats -> a scene)
_APPEAL = {"evidence": "on the proof", "consequence": "from what it will bring", "authority": "from what is owed",
           "solidarity": "as one of their own"}


def render(inp, card, out) -> str:
    L = [f"[{card.kind}: a {card.genre} proceeding on a {card.live}, "
         + (f"arranged by {card.arranged_by} (tilt {card.tilt})" if card.arranged_by else "arranged by custom")
         + f"; decided by {', '.join(card.decided_by) or 'each party`s own accept'}; silence: {card.silence};"
         f" {card.turns} turn(s) each]"]
    pts = {p.id: p for p in out.state.points}
    told = {}
    for b in out.beats:
        who = b.mover if b.voice == b.mover else f"{b.mover} calls {b.voice}, who"
        if b.move == "argue":
            if b.relation == "answers":
                p = pts[b.point]
                s = f"{who} answers {p.by}'s point {p.id} ({_APPEAL[p.ground]}) {_APPEAL[b.ground]}"
            else:
                s = f"{who} raises point {b.point} on {b.issue} {_APPEAL[b.ground]}" + (f" (framed on {b.frame})" if b.frame else "")
            if b.item:
                s += f", citing {b.item}"
            s += ": it " + ("lands" if b.margin >= 1 else "half lands" if b.margin >= 0 else "falls flat")
            if b.caught:
                s += f"; {', '.join(b.caught)} see{'s' if len(b.caught) == 1 else ''} it is not what he holds"
            elif b.insincere > 0.3:
                s += "; it is not what he himself holds"
        elif b.move == "press":
            s = f"{who} presses {b.target} {_APPEAL[b.ground]}" + (f" on his {b.frame}" if b.frame else "") \
                + (f", with {b.item}" if b.item else "")
            s += f": {b.target} is rattled" if b.rattled else f": {b.target} holds"
        elif b.move == "concede":
            s = f"{who} concedes {b.closed}" + (" and yields" if (out.ended == "yielded" and b is out.beats[-1]) else "")
        else:
            s = f"{who} rests"
        if b.drift > 0.5:
            s += "; he wanders from the point"
        must = dict(card.reply).get(b.side) == "must"
        if b.left is not None:
            s += f"; {pts[b.left].by}'s point {b.left} stands unanswered" + (" and the room marks it" if (b.evaded and must) else "")
        if b.evaded and not (b.left is not None and must):
            s += "; he has put nothing of his own and the room marks it"
        sgn = (b.esteem >= 1.0) - (b.esteem <= -1.0)
        if b.move in ("argue", "press") and sgn and told.get(b.voice) != sgn:
            told[b.voice] = sgn                  # said once, and again only when it turns
            s += "; his bearing tells for him" if sgn > 0 else "; his bearing tells against him"
        if b.broke:
            s = ("(his temper gone, he gives way) " if b.move == "concede" else "(he can hold his tongue no longer) ") + s
        L.append(f"  {b.n}. [{b.issue}] {s}. (room {b.mood:+.2f})")
    return "\n".join(L + [f"  -> ended {out.ended}" + (f" by {out.ended_by}" if out.ended_by else "")])
