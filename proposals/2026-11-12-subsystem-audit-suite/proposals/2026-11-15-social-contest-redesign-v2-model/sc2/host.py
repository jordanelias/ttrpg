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
from .engine import (SIGN, Input, Item, Present, Rite, mood, p_carried)

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
    start_step=2.0, presume_step=2.0, sympathy_step=1.5, power_scale=2.0, strain_fade=0.5, recuse_at=0.25,
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
    "theocracy": dict(unlawful=("debate",), gravity=0.5, standard=1.0, reason_lean=-0.1, admits_add=("confession", "oath"),
                      admits_drop=("precedent",), power={"church": 2.0}, silence="admits"),
    "commune":   dict(unlawful=("inquisition",), gravity=0.0, standard=-1.0, reason_lean=0.0, admits_add=("rumour",), admits_drop=(),
                      power={"guild": 1.0}, floor="open", silence="free"),
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
               "partial": ("tenure:oblige", "docket:adjourned"), "failure": ("record:acquittal", "legitimacy-"),
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
    x = L.get("relationships", {}).get(q, 0.0)
    x += 0.5 * (q in L.get("kin", ())) + 0.5 * (q == L.get("patron")) + 0.5 * (q in L.get("clients", ()))
    x += L.get("debts", {}).get(q, 0.0)                      # +: he owes q; -: q wronged him
    if people is not None and p.get("faction") and people.get(q, {}).get("faction") == p["faction"]:
        x += 0.3                                             # one of his own (C: faction acts on play)
    return _clip(x)


def bearing(p: dict, ref: dict, people: dict) -> tuple:
    """How a referent (a matter, an item, a person) BEARS on p: (want, hold, bond), each signed -1..1.
    `ref` carries `bears: {tag: signed weight}` and/or `parties: {for:, against:}` and/or `factions: {faction: sign}`.
    want: pursuits, goals, ambitions, needs.  hold: convictions and his office's duty.  bond: persons and faction."""
    L = p.get("layers", {})
    b = ref.get("bears", {})
    want = sum((L.get("pursuits", {}).get(t, 0.0) + L.get("needs", {}).get(t, 0.0)
                + 0.5 * (t in L.get("goals", ())) + 0.5 * (t in L.get("ambitions", ()))) * w for t, w in b.items())
    hold = sum(L.get("convictions", {}).get(t, 0) / 5.0 * w for t, w in b.items())
    hold += sum((p.get("office") or {}).get("duty", {}).get(t, 0.0) * w for t, w in b.items())
    par = ref.get("parties", {})
    bond = tie(p, par.get("for"), people) - tie(p, par.get("against"), people)
    bond += ref.get("factions", {}).get(p.get("faction"), 0.0)
    return (_clip(want), _clip(hold), _clip(bond))


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


def power(p: dict, regime: str = "crown") -> float:
    o = p.get("office") or {}
    auth = AUTHORITY_BY_FACTION.get(o.get("faction"))
    return o.get("rung", 0) + (2.0 * level(o["modifier"]) if o.get("modifier") else 0.0) \
        + (REGIMES[regime]["power"].get(auth, 0.0) if o else 0.0)


def strain_carried(p: dict, D) -> float:
    """each rattle fades on its OWN clock, and the k-th freshest counts half the one before: bounded, no ratchet."""
    f = sorted((max(0.0, 1.0 - D["strain_fade"] * s) for s in p.get("rattled_ago", ())), reverse=True)
    return 0.5 * sum(x / 2 ** k for k, x in enumerate(f))


def conflict(stake) -> tuple:
    """B6: a stake is a CONFLICT however it nets: (how much the matter bears on him at all, which way it leans).
    Opposite interests do not cancel to impartiality."""
    return sum(abs(x) for x in stake) / 3.0, sum(stake) / 3.0


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
    """D4 'how hard': the turns he prepares, from how much the matter bears on him: 0 a passing word .. 3."""
    return int(min(3, round(3 * abs(sum(bearing(p, matter, people)) / 3.0) + 1))) if any(bearing(p, matter, people)) else 0


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


def lawful(regime: str):
    return tuple(r for r in RITES if r not in REGIMES[regime]["unlawful"])


def _pack(cands, arr_id, t, people):
    """C3: one rule for bench and floor: the arranger drops the share `t` of them least tied to him."""
    if t <= 0 or len(cands) <= 1:
        return list(cands)
    cands = sorted(cands, key=lambda p: -tie(p, arr_id, people))
    return cands[:max(1, len(cands) - int(t * (len(cands) - 1) + 0.5))]


def build(people: dict, rite_id: str, matter: dict, *, bench=(), floor=(), form="full", era="plain", regime="crown",
          strife="peace", arranger=None, rig=0.0, effort=None, difficulty="routine", D=None, state=None,
          flat=(), decides_also=(), grounds_for=None):
    """-> (Input, Card). `flat`: layers to flatten for a control arm: any of 'bearing', 'context', 'power'.
    `form`: 'full', 'abridged', or 'auto' (D6: the abridged form for a passing word nobody watches)."""
    D = D or dials()
    if "context" in flat:
        era, regime, strife = "plain", "crown", "peace"
    rid, over = ALIASES.get(rite_id, (rite_id, {}))
    if rid not in lawful(regime):
        raise ValueError(f"refused[unlawful]: {rid} is not lawful under {regime}")
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
        arr_side = "for" if arr["id"] == fid else "against" if (B is not None and arr["id"] == aid) else \
            ("for" if B is None or tie(arr, fid, people) >= tie(arr, aid, people) else "against")
        weak = B if arr_side == "for" else A
        if weak is not None and "power" not in flat:
            t = tilt(arr, weak, rig, regime, D)
    weak_side = None if t <= 0 else ("against" if arr_side == "for" else "for")
    close = r["close"]
    moves = {s: tuple(m) for s, m in r["moves"].items()}
    lo, hi = r["turns"]
    turns = max(lo, min(hi, effort + 1) + S["turns"])          # C3: the rig no longer cuts turns (it cut the arranger's own case)
    if form == "abridged":
        moves, turns, close = {"for": ("argue",), "against": ()}, 1, "exchange"
    # ---- who sits: the seats' own faction against the rite's authority; recusal (B6); the arranger packs a share t
    seats = [people[b] for b in bench]
    if r["authority"] not in ("parties", "none"):
        seats = [p for p in seats if AUTHORITY_BY_FACTION.get((p.get("office") or {}).get("faction")) == r["authority"]]
    recused = []
    if close in ("bench", "declared"):
        seats.sort(key=lambda p: -(p.get("office") or {}).get("rung", 0))
        need = 1 if close == "bench" else (r.get("quorum") or 1)
        for p in list(seats):                                # a party who sits is partial by choice and seen (A-139)
            c, _ = conflict(bearing(p, matter, people))
            if p["id"] not in (fid, aid) and c >= D["recuse_at"] and len(seats) > need:
                seats.remove(p); recused.append(p["id"])          # he steps down; a conflicted seat who cannot sits and pays
        seats = _pack(seats, arr["id"], t, people) if arr else seats
        if not seats:
            raise ValueError(f"refused[no_seat]: {rid}: no seat of authority {r['authority']} (party-gap refusal)")
    fl = r["floor"] if "floor" not in R else R["floor"]
    fl_ids = [] if fl == "closed" else [f for f in floor if fl == "open" or people[f].get("office")]
    absent = set(matter.get("absent_in", {}).get(strife, ()))
    fl_ids = [f for f in fl_ids if f not in absent]
    if arr is not None and t > 0:
        fl_ids = [p["id"] for p in _pack([people[f] for f in fl_ids], arr["id"], t, people)] if len(fl_ids) > 1 else \
            ([] if t >= 0.5 else fl_ids)
    admits = tuple(k for k in r["admits"] + R["admits_add"] if k not in R["admits_drop"])
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
        if t > 0 and decides and side is None:
            ln += t * D["presume_step"] * SIGN[arr_side]
        if grounds_for and decides and side is None:              # D1: an appeal's grounds, seen by the higher bench
            ln += grounds_for[1] * D["presume_step"] * SIGN[grounds_for[0]]
        elif t > 0 and side is None:
            ln -= t * D["sympathy_step"] * SIGN[arr_side] * (1.0 - max(0.0, tie(p, arr["id"], people)))
        a = p.get("attributes", {})
        its = tuple(p.get("items", ())) + (false_items(p, matter, side) if side else ())
        return Present(id=p["id"], weight=int(p.get("weight", 1)), side=side, decides=decides,
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
    card = Card(kind=rite_id, genre=r["genre"], arranged_by=arr["id"] if (arr and t > 0) else None, tilt=round(t, 2),
                tilted_against=weak_side,
                stake=disp, outcomes=tuple(DISPOSAL[disp].items()),
                room=tuple((p.id, (("speaks " + p.side) if p.side else ("judges" if p.decides else "attends")),
                            round(p.power, 1)) for p in room),
                live=r["live"], bears=r["bears"], reply=rite.reply, moves=rite.moves, barred=barred,
                admits=admits, close=close, decided_by=tuple(p.id for p in room if p.decides), turns=turns,
                issues=rite.issues, silence=rite.silence,
                unargued=("it lapses: the bearer must put it, and his rest is priced as silence" if must_b
                          else "it stands where the room starts"),
                ends="when the turns are spent, a whole round rests, or a side yields",
                standard=rite.standard, unrest=rite.unrest, gravity=rite.gravity, reason_weight=rw,
                recused=tuple(recused),
                odds=round(p_carried(inp, unmoved), 3) if close in ("bench", "declared", "hearers") else None)
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
        if inp.rite.close == "consent" or y.side == inp.rite.bears or y.decides:   # way (his own accept); otherwise
            return ("success" if y.side != inp.rite.bears else "failure"), None, False   # the bench draws (A-14)
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
                strife={}, precedents=[], docket=[], rattled={}, events=[], compliance={}, appeal_weight={}, reception=[])


def bounded(x, d):
    """B9: a bounded quantity (regard, legitimacy, standing) moves by `d` toward its bound and never past it: a step
    is worth less the nearer the bound it pushes, and nothing runs away."""
    return x + d * (1.0 - x) if d > 0 else x + d * (1.0 + x)


def merits(inp, out):
    """B5: the merits AS THE RECORD SHOWS THEM: how far the sitting itself moved those who heard it (each listener's
    track less where his own stake and the arrangement started it), weight-mean, toward `for`."""
    T = dict(out.state.tracks)
    ls = [p for p in inp.room if p.side is None] or [p for p in inp.room if p.decides]
    W = sum(p.weight for p in ls) or 1
    return sum(p.weight * (T[p.id] - p.start) for p in ls) / W


def reception(inp, j):
    """A-144(6), B5: `brute`, how far his station outstrips his respectability, both on 0..1: station as
    tanh(power / power_scale), respectability as his Grace's share of the scale. A Grace-7 judge is never a brute."""
    D = inp.dials
    brute = max(0.0, math.tanh(j.power / D["power_scale"]) - (j.grace - D["floor"]) / (D["ceiling"] - D["floor"]))
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
    jf = (people[j.id].get("faction") or (people[j.id].get("office") or {}).get("faction")) if j else None
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
            standing(people[fid].get("faction"), F["standing"] * (1 if op[-1] == "+" else -1)); w(op, people[fid].get("faction"))
        elif op in ("legitimacy+", "legitimacy-"):
            if jf:                                         # the forum's authority, which ruled
                legit(jf, F["legit_ruling"] * (1.0 - card.tilt) if op[-1] == "+" else -F["legit_fall"]); w(op, jf)
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
        cj, lean = conflict(j.stake)
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
        aw = brute + (0.5 if wrong else 0.0) + (card.tilt if (loser and _side_of(inp, loser) == card.tilted_against) else 0.0)
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
            c, ln = conflict(p.stake)
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
            legit(people[card.arranged_by].get("faction"), -rig_price(card.tilt)); w("legitimacy-", card.arranged_by)
            if _side_of(inp, loser) == card.tilted_against:
                reg(loser, card.arranged_by, -F["grudge_rig"] * card.tilt, "rigged against him")   # C3: the grievance
    if matter.get("strife") and band is not None and won and card.stake in ("decree", "oblige", "detain", "ban"):
        k = matter["strife"]                               # B3: only what the sitting RESOLVED moves a strife
        if k in world["strife"]:
            world["strife"][k] = max(0.0, world["strife"][k] - F["strife_ease"]); w("strife", k)
    return band, tuple(writes)


def _side_of(inp, pid):
    if pid is None:
        return None
    p = next((q for q in inp.room if q.id == pid), None)
    return p.side if p else None


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
