"""sc2.host -- the HOST side of redesign-v2 as a toy: the data (rites, matters, context, disposal), the ONE bearing
reading, arrangement by power, the builder, the card, the fold, and a template renderer (a test fixture).
The module (engine.py) reads none of the tables here: the host hands it cells and numbers.
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
    room_level=0.5, concede_step=2.0, consent_at=2.5, yield_track=12.0,
    crowd_at=12.0, crowd_lean=0.2, mood_scale=5.0, read_scale=1.0, read_blur=2.0, read_noise=0.3, bias_step=2.0, relevance=1, awe_step=0.5, comfort_step=0.5, rel_gain=0.5, flop=0.5, invite=0.5, track_step=0.2,
    temper_step=0.5, temper_break=0.75, grain=2.0, grudge=2.0, pride=2.0,
    start_step=2.0, presume_step=2.0, sympathy_step=1.5, power_scale=2.0, strain_fade=0.5,
)
CONTROL_ZERO = dict(fit_level=None, answer_level=None, repeat_step=0.0, esteem_step=0.0, off_step=0.0, ploy_step=0.0,
                    grain_strain=0.0, start_step=0.0, awe_step=0.0, crowd_lean=0.0, heckle=0.0, room_level=0.0, heard_step=0.0,
                    gap_step=0.0, weary_step=0.0)


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
    "confession":     ("the conceding beat of an earlier sitting on the case file", "the bench or the questioner", "none"),
}

# ------------------------------------------------------------------ DATA: the rites (the structures; rows are these, arranged)
PLAIN, FORMAL, SOLEMN = 4.0, 5.0, 6.0
_BOTH = ("argue", "press", "rest", "concede")
RITES = {
    "conversation": dict(silence="free", genre="dyadic", live="claim", bears="for", reply={"for": "may", "against": "may"},
                         issues=("the claim",), concede="accepts", moves={"for": _BOTH, "against": _BOTH},
                         close="hearers", turns=(1, 3), standard=PLAIN, reason_lean=0.0, floor="closed", authority="parties",
                         admits=("record", "testimony", "deed", "oath", "debt", "rumour", "state_of_realm"), disposes="none"),
    "negotiation": dict(silence="free", genre="dyadic", live="offer", bears="for", reply={"for": "must", "against": "must"},
                        issues=("the terms",), concede="accepts", moves={"for": _BOTH, "against": _BOTH},
                        close="consent", turns=(1, 3), standard=PLAIN, reason_lean=0.0, floor="closed", authority="parties",
                        admits=("record", "debt", "oath", "title", "treaty", "state_of_realm"), disposes="oblige"),
    "questioning": dict(silence="refusal", genre="judicial", live="question", bears="for", reply={"for": "may", "against": "must"},
                        issues=("the question",), concede="accepts",
                        moves={"for": ("argue", "press", "rest"), "against": ("argue", "rest", "concede")},
                        close="hearers", turns=(1, 4), standard=PLAIN, reason_lean=0.0, floor="closed", authority="parties",
                        admits=("testimony", "record", "deed", "rumour", "confession"), disposes="none"),
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
# the tree's other rows are the SAME structure arranged by another authority (no code, no second rite):
ALIASES = {
    "legal_trial": ("trial", {}), "tribunal": ("trial", dict(floor="admitted", disposes="ban")),
    "arbitration": ("trial", dict(authority="parties", standard=PLAIN, floor="closed", disposes="oblige")),
    "parliamentary_debate": ("debate", {}), "council_of_state": ("debate", dict(floor="closed")),
    "excommunication_deliberation": ("debate", dict(authority="church", floor="closed", standard=SOLEMN, disposes="ban")),
    "inquisition_hearing": ("inquisition", {}),
    "interrogation": ("inquisition", dict(authority="polity", standard=PLAIN, disposes="detain")),
}

# ------------------------------------------------------------------ DATA: context (era, regime, strife) as cell deltas
ERAS = {"plain": {}, "age_of_faith": {"authority": 1.4, "consequence": 0.8}, "mercantile": {"consequence": 1.4, "authority": 0.8}}
REGIMES = {
    "crown":     dict(unlawful=(), standard=0.0, reason_lean=0.0, admits_add=(), admits_drop=(), power={"polity": 1.0}, silence=None),
    "theocracy": dict(unlawful=("debate",), standard=1.0, reason_lean=-0.1, admits_add=("confession", "oath"),
                      admits_drop=("precedent",), power={"church": 2.0}, silence="admits"),
    "commune":   dict(unlawful=("inquisition",), standard=-1.0, reason_lean=0.0, admits_add=("rumour",), admits_drop=(),
                      power={"guild": 1.0}, floor="open", silence="free"),
}
STRIFE = {
    "peace":  dict(turns=0, unrest=0.0, stakes=0.0, care_want=0.0),
    "war":    dict(turns=-1, unrest=0.5, stakes=0.5, care_want=0.0),
    "famine": dict(turns=0, unrest=0.75, stakes=0.25, care_want=0.3),
    "schism": dict(turns=0, unrest=0.25, stakes=0.5, care_want=0.0),
}
AUTHORITY_BY_FACTION = {"Crown": "polity", "Parliament": "polity", "Church": "church", "Guild": "guild"}
DIFFICULTY = {"plain": 0.0, "routine": 0.5, "demanding": 1.0, "hard": 1.5}

# ------------------------------------------------------------------ DATA: disposal (what each outcome writes)
# (disposes, band) -> typed writes the fold performs. Band None = impasse / no verdict.
DISPOSAL = {
    "none":   {"overwhelming": ("pursuits+", "regard+", "claim:converted"), "success": ("pursuits+", "regard+"),
               "partial": ("regard+",), "failure": ("regard-", "grievance"), None: ("regard-",)},
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


def tie(p: dict, q) -> float:
    """how another PERSON bears on him: relationships, kin, patronage, debts, faction. Own interior only."""
    if q is None or q == p["id"]:
        return 0.0
    L = p.get("layers", {})
    x = L.get("relationships", {}).get(q, 0.0)
    x += 0.5 * (q in L.get("kin", ())) + 0.5 * (q == L.get("patron")) + 0.5 * (q in L.get("clients", ()))
    x += L.get("debts", {}).get(q, 0.0)                      # +: he owes q; -: q wronged him
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
    bond = tie(p, par.get("for")) - tie(p, par.get("against"))
    bond += ref.get("factions", {}).get(p.get("faction"), 0.0)
    fac = lambda q: people.get(q, {}).get("faction") if q else None
    if p.get("faction"):
        bond += 0.3 * (fac(par.get("for")) == p["faction"]) - 0.3 * (fac(par.get("against")) == p["faction"])
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


# ------------------------------------------------------------------ arrangement by power
def tilt(arranger: dict, weak: dict, rig: float, regime: str, D) -> float:
    return rig * max(0.0, math.tanh((power(arranger, regime) - power(weak, regime)) / D["power_scale"]))


@dataclass(frozen=True)
class Card:
    """A-133: what the proceeding IS, derived from data; every field is checked against the sitting."""
    kind: str
    genre: str
    arranged_by: str
    tilt: float
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
    standard: float            # the Grace the occasion expects
    reason_weight: tuple       # ((ground, share of Reason in the dice here), ...)
    odds: Optional[float]      # P(carried) before an ordinary unmoved bench; None where nothing is drawn (consent) or the
                               # verdict is the speech itself (the abridged form: the option's own chance)


def lawful(regime: str):
    return tuple(r for r in RITES if r not in REGIMES[regime]["unlawful"])


def build(people: dict, rite_id: str, matter: dict, *, bench=(), floor=(), form="full", era="plain", regime="crown",
          strife="peace", arranger=None, rig=0.0, effort=1, difficulty="routine", D=None, state=None,
          flat=(), decides_also=()):
    """-> (Input, Card). `flat`: layers to flatten for a control arm: any of 'bearing', 'context', 'power'."""
    D = D or dials()
    if "context" in flat:
        era, regime, strife = "plain", "crown", "peace"
    rid, over = ALIASES.get(rite_id, (rite_id, {}))
    if rid not in lawful(regime):
        raise ValueError(f"{rid} is not lawful under {regime}")
    r = copy.deepcopy(RITES[rid]); r.update(over)
    R, S = REGIMES[regime], STRIFE[strife]
    fid, aid = matter["parties"]["for"], matter["parties"].get("against")
    if aid is not None and aid == fid:
        raise ValueError("the two parties to a matter are one character: refused (A-139)")
    A, B = people[fid], (people[aid] if aid else None)
    arr = people[arranger] if arranger else A
    arr_side = "for" if arr["id"] == fid or (B is not None and tie(arr, fid) >= tie(arr, aid)) else "against"
    weak = (B if arr_side == "for" else A) or A
    t = 0.0 if ("power" in flat or weak is arr) else tilt(arr, weak, rig, regime, D)
    weak_side = "against" if arr_side == "for" else "for"
    # ---- who sits: the seats' own faction against the rite's authority; the arranger packs a share t of it
    seats = [people[b] for b in bench]
    if r["authority"] not in ("parties", "none"):
        seats = [p for p in seats if AUTHORITY_BY_FACTION.get((p.get("office") or {}).get("faction")) == r["authority"]]
    if t > 0 and len(seats) > 1:
        seats.sort(key=lambda p: -tie(p, arr["id"]))
        keep = max(1, len(seats) - int(t * (len(seats) - 1) + 0.5))
        seats = seats[:keep]
    if r["close"] in ("bench", "declared") and not seats:
        raise ValueError(f"{rid}: no seat of authority {r['authority']} (party-gap refusal)")
    fl = r["floor"] if "floor" not in R else R["floor"]
    fl_ids = [] if (fl == "closed" or t >= 0.75) else [f for f in floor if fl == "open" or people[f].get("office")]
    absent = set(matter.get("absent_in", {}).get(strife, ()))
    fl_ids = [f for f in fl_ids if f not in absent]
    lo, hi = r["turns"]
    turns = max(lo, min(hi, effort + 1) + S["turns"] - int(t * (hi - lo) + 0.5))
    admits = tuple(k for k in r["admits"] + R["admits_add"] if k not in R["admits_drop"])
    eraw = ERAS[era]
    grounds = tuple((g, c, eraw.get(g, 1.0)) for g, c in GROUNDS)
    moves = {s: tuple(m) for s, m in r["moves"].items()}
    close = r["close"]
    if form == "abridged":
        moves, turns, close = {"for": ("argue",), "against": ()}, 1, "exchange"
    rite = Rite(id=rid, live=r["live"], reply=tuple(r["reply"].items()), issues=tuple(r["issues"]), concede=r["concede"],
                moves=tuple(moves.items()), close=close, turns=turns, standard=r["standard"] + R["standard"],
                reason_lean=r["reason_lean"] + R["reason_lean"], admits=admits, difficulty=DIFFICULTY[difficulty],
                stakes=S["stakes"], quorum=r.get("quorum"), unrest=S["unrest"], bears=r["bears"],
                silence=r["silence"] if (R["silence"] is None or r["silence"] == "free" and "must" not in r["reply"].values()) else R["silence"])
    speak_against = bool(moves.get("against")) and B is not None
    room, in_room = [], set()

    def present(p, side, decides):
        st = (0.0, 0.0, 0.0) if "bearing" in flat else bearing(p, matter, people)
        ln = D["start_step"] * sum(st) / 3.0
        if decides:
            ln += t * D["presume_step"] * SIGN[arr_side]
        elif side is None:
            ln -= t * D["sympathy_step"] * SIGN[arr_side] * (1.0 - max(0.0, tie(p, arr["id"])))
        a = p.get("attributes", {})
        return Present(id=p["id"], weight=int(p.get("weight", 1)), side=side, decides=decides,
                       **{k: float(a.get(k, 4)) for k in ATTRS}, rank=float(p.get("rank", 0)),
                       care=(0.5, 0.5, 0.5) if "bearing" in flat else care(p, strife), stake=st,
                       bonds=() if "bearing" in flat else tuple((q, tie(p, q)) for q in people if q != p["id"] and tie(p, q)),
                       holds=() if "bearing" in flat else holds(p, matter), start=ln, believes=float(p.get("believes", {}).get(matter["id"], 0.0)), bias=float(p.get("bias", 0.0)),
                       power=0.0 if "power" in flat else power(p, regime),
                       precedence=int((p.get("office") or {}).get("rung", 0)),
                       items=tuple(p.get("items", ())), strain=strain_carried(p, D))

    def add(p, side, decides):
        if p["id"] not in in_room:
            in_room.add(p["id"]); room.append(present(p, side, decides))
        elif decides:                       # one person, two cells: a party who also adjudicates (a noble, an inquisitor)
            k = [q.id for q in room].index(p["id"]); room[k] = present(p, room[k].side, True)

    add(A, "for", False)
    if B is not None:
        add(B, "against" if speak_against else None, close in ("exchange", "hearers"))
    if close in ("bench", "declared") or (close == "exchange" and B is None):
        seats.sort(key=lambda p: -(p.get("office") or {}).get("rung", 0))
        for s in (seats if close == "declared" else seats[:1]):
            add(s, None, True)
    for f in fl_ids:
        add(people[f], None, close == "hearers")
    frames = tuple(sorted({(c, t) for p in room for c, t, _, _ in p.holds}))
    inp = Input(rite=rite, matter=matter["id"], room=tuple(room), grounds=grounds, dials=D, state=state, frames=frames)
    disp = matter.get("disposes", r["disposes"])
    barred = tuple((s, m) for s in ("for", "against") for m in _BOTH if m not in moves.get(s, ()) and moves.get(s))
    from .engine import _crowd
    rw = tuple((g, round(min(1.0, max(0.0, c + rite.reason_lean - D["crowd_lean"] * _crowd(inp))), 1)) for g, c, _ in grounds)
    card = Card(kind=rite_id, genre=r["genre"], arranged_by=arr["id"], tilt=round(t, 2), stake=disp,
                outcomes=tuple(DISPOSAL[disp].items()),
                room=tuple((p.id, (("speaks " + p.side) if p.side else ("judges" if p.decides else "attends")),
                            round(p.power, 1)) for p in room),
                live=r["live"], bears=r["bears"], reply=rite.reply, moves=rite.moves, barred=barred,
                admits=admits, close=close, decided_by=tuple(p.id for p in room if p.decides), turns=turns,
                issues=rite.issues, silence=rite.silence, standard=rite.standard, reason_weight=rw,
                odds=round(p_carried(inp, 0.0), 3) if close in ("bench", "declared", "hearers") else None)
    return inp, card


# ------------------------------------------------------------------ the host's read of the verdicts, and the fold
_RANK = {"failure": 0, "partial": 1, "success": 2, "overwhelming": 3}


def act_band(inp, out):
    """(band, margin, veto). Drawn closes: the presiding verdict (declared: demoted under quorum; hearers: the
    weight-mean). Consent: whether a party ACCEPTED (his act): the party addressed accepting is Success, the bearer
    withdrawing is Failure, neither is an impasse (band None). Never the actor's last exchange."""
    if inp.rite.close == "consent":
        if out.ended == "yielded":
            y = next(p for p in inp.room if p.id == out.ended_by)
            return ("success" if y.side != inp.rite.bears else "failure"), None, False
        return None, None, False
    w = {p.id: p.weight for p in inp.room}
    if inp.rite.close == "hearers":
        W = sum(w[i] for i, _ in out.verdicts)
        m = sum(w[i] * (v.net - v.ob) for i, v in out.verdicts) / W
    else:
        m = out.verdicts[0][1].net - out.verdicts[0][1].ob
    band = "failure" if m < 0 else "partial" if m < 1 else "success" if m < 3 else "overwhelming"
    veto = False
    if inp.rite.close == "declared":
        n_ok = sum(1 for _, v in out.verdicts if _RANK[degree(v)] >= 2)
        veto = n_ok < (inp.rite.quorum or 1)
        if veto and _RANK[band] >= 2:
            band = "partial"
    return band, m, veto


def new_world():
    return dict(tenures=[], offices={}, case_files={}, ledgers={}, regard={}, pursuits={}, standing={}, legitimacy={},
                strife={}, precedents=[], docket=[], rattled={}, events=[])


def fold(world, people, inp, card, out, matter):
    """The toy fold: performs EVERY write of the DISPOSAL row for (card.stake, band), then the hooks every sitting
    leaves. Regard moves both ways. The module wrote nothing. Returns (band, writes)."""
    band, m, veto = act_band(inp, out)
    fid, aid = matter["parties"]["for"], matter["parties"].get("against")
    writes, R = [], world["regard"]

    def w(kind, *a):
        writes.append((kind,) + a)

    def reg(x, y, d, why):
        if x and y and x != y:
            R[(x, y)] = R.get((x, y), 0.0) + d; w("regard" + ("+" if d > 0 else "-"), x, y, why)

    won = band in ("success", "overwhelming")
    world["events"].append((matter["id"], card.kind, out.ended, band))
    world["case_files"].setdefault(matter["id"], []).append((card.kind, out.ended, band, len(out.beats)))
    w("case_file:stage", matter["id"])
    arr_fac = people[card.arranged_by].get("faction")
    hearers = [p for p in inp.room if p.side is None]
    for op in DISPOSAL[card.stake][band]:
        if op.startswith("tenure:") and aid:
            world["tenures"].append((op[7:], aid, matter["id"])); w(op, aid)
        elif op == "office:stripped":
            if aid and people[aid].get("office"):
                world["offices"][aid] = "contested"; w(op, aid)
        elif op.startswith("record:"):
            world["case_files"][matter["id"]].append(("record", op[7:])); w(op, matter["id"])
        elif op == "precedent":
            world["precedents"].append(Item(f"prec:{matter['id']}", "precedent", min(1.0, 0.5 + abs(m or 0) / 6.0),
                                            source=card.decided_by[0] if card.decided_by else None, about=aid)); w(op, matter["id"])
        elif op.startswith("docket:"):
            world["docket"].append((matter["id"], op[7:])); w(op, matter["id"])
        elif op == "grievance":
            world["docket"].append((f"grievance:{fid}:{matter['id']}", "grievance")); w(op, fid)
        elif op in ("faction+", "faction-"):
            f = people[fid].get("faction")
            world["standing"][f] = world["standing"].get(f, 0.0) + (0.5 if op[-1] == "+" else -0.5); w(op, f)
        elif op in ("legitimacy+", "legitimacy-"):
            d = 0.1 * (1.0 - card.tilt) if op[-1] == "+" else -0.5
            world["legitimacy"][arr_fac] = world["legitimacy"].get(arr_fac, 0.0) + d; w(op, arr_fac)
        elif op == "regard+":
            for p in hearers:
                reg(p.id, fid, 0.1, "carried")
            reg(aid, fid, 0.15, "accord"); reg(fid, aid, 0.15, "accord")
        elif op == "regard-":
            for p in hearers:
                reg(p.id, fid, -0.05, "unmoved")
            reg(aid, fid, -0.05, "importuned")
        elif op == "regard-accuser":
            for p in hearers:
                reg(p.id, fid, -0.1, "a charge that failed")
            reg(aid, fid, -0.2, "accused and acquitted")
        elif op == "pursuits+":
            for p in hearers:
                world["pursuits"][p.id] = world["pursuits"].get(p.id, 0.0) + 0.1; w(op, p.id)
        elif op == "claim:converted":
            for p in hearers:
                world["ledgers"].setdefault(p.id, []).append(("converted", fid, matter["id"])); w(op, p.id)
        else:
            raise KeyError(op)
    # ---- ADJUDICATOR'S GRACE (A-144): how the verdict is RECEIVED, apart from whether it was right
    ds = sorted((p for p in inp.room if p.decides), key=lambda p: (-p.precedence, p.id))
    if ds and band is not None and inp.rite.close != "consent":
        j = ds[0]
        brute = max(0.0, j.power - (j.grace - inp.dials["floor"])) / 6.0         # station outstripping respectability
        rec = 1.0 - min(1.0, brute)
        wrong = (m is not None) and ((m >= 1) != (dict(out.state.tracks)[j.id] > 0)) and abs(dict(out.state.tracks)[j.id]) > 1.0
        jf = people[j.id].get("faction") or (people[j.id].get("office") or {}).get("faction")
        world["legitimacy"][jf] = world["legitimacy"].get(jf, 0.0) + 0.1 * rec - 0.4 * brute * (2.0 if wrong else 1.0)
        world.setdefault("compliance", []).append(round(rec * (1.0 if not wrong else 0.9), 2))
        world.setdefault("reception", []).append((j.id, round(rec, 2), wrong))
        for p in inp.room:
            if p.id != j.id:
                reg(p.id, j.id, 0.1 * rec - 0.2 * brute * (2.0 if wrong else 1.0), "how he ruled")
        if brute > 0:
            world["standing"][jf] = world["standing"].get(jf, 0.0) - 0.2 * brute
            world["appeal_weight"] = world.get("appeal_weight", 0.0) + brute * (2.0 if wrong else 1.0); w("appeal_weight", j.id)
        w("reception", j.id, round(rec, 2))
    T = dict(out.state.tracks)
    for p in inp.room:
        led = world["ledgers"].setdefault(p.id, [])
        for b in out.beats:
            if b.rattled:
                led.append(("rattled", b.rattled, b.mover))
            if b.insincere > 0 and p.attunement >= inp.dials["mid"] and p.id != b.voice:
                led.append(("hypocrite", b.voice, round(b.insincere, 2)))
            if b.item:
                led.append(("shown", b.item, b.voice))
            if b.move == "concede":
                led.append(("conceded", b.mover, b.closed))
            if b.evaded:
                led.append(("contumacy", b.mover, b.issue))
            if b.broke:
                led.append(("lost his temper", b.mover, b.n))
        if card.tilt > 0 and p.id != card.arranged_by:
            led.append(("rigged", card.arranged_by, card.tilt))
        if p.decides and abs(sum(p.stake)) > 0:
            for q in inp.room:
                if q.id != p.id:
                    world["ledgers"].setdefault(q.id, []).append(("partial", p.id, round(sum(p.stake) / 3.0, 2)))
        if p.side is None:
            reg(p.id, fid, 0.03 * (T[p.id] - p.start), "what he heard")
    for d_id, dep in out.ruled:
        if dep > 0:
            for q in inp.room:
                world["ledgers"].setdefault(q.id, []).append(("ruled against the room", d_id, dep))
    for b in out.beats:
        if b.evaded:
            for p in inp.room:
                if p.decides and p.id != b.mover:
                    reg(p.id, b.mover, -0.1, "he would not answer")
        if b.move == "press" and b.target:
            reg(b.target, b.mover, -(0.1 if b.rattled else 0.03), "pressed")
        if b.rattled:
            world["rattled"].setdefault(b.rattled, []).append(0); w("strain_carried", b.rattled)
        if b.voice != b.mover:
            reg(aid if b.side == "for" else fid, b.voice, -0.1, "testified against him")
            reg(b.mover, b.voice, 0.1, "stood by him")
    if aid and band is not None:
        for pid, sgn in ((fid, 1.0), (aid, -1.0)):
            st = sum(bearing(people[pid], matter, people)) / 3.0
            world["pursuits"][pid] = world["pursuits"].get(pid, 0.0) + (1.0 if won else -1.0) * sgn * abs(st)
        loser, winner = (aid, fid) if won else (fid, aid)
        if inp.rite.close != "consent":
            reg(loser, winner, -0.05 - 0.3 * card.tilt, "lost to him")
        if card.tilt > 0:
            seen = sum(p.weight for p in inp.room if p.id != card.arranged_by)
            world["legitimacy"][arr_fac] = world["legitimacy"].get(arr_fac, 0.0) - card.tilt * min(1.0, seen / 12.0)
            w("legitimacy-", arr_fac)
            if loser != card.arranged_by:
                world["docket"].append((f"appeal:{matter['id']}", "appeal")); w("docket:appeal", loser)
    if matter.get("strife") and band is not None:
        k = matter["strife"]
        world["strife"][k] = world["strife"].get(k, 1.0) + (-0.25 if won else 0.25); w("strife", k)
    return band, tuple(writes)


# ------------------------------------------------------------------ the renderer (a TEST FIXTURE: beats -> a scene)
_REL = {"raises": "raises", "answers": "answers", "presses": "presses", "concedes": "concedes", "rests": "rests"}
_APPEAL = {"evidence": "on the proof", "consequence": "from what it will bring", "authority": "from what is owed",
           "solidarity": "as one of their own"}


def render(inp, card, out) -> str:
    L = [f"[{card.kind}: a {card.genre} proceeding on a {card.live}, arranged by {card.arranged_by}"
         + (f" (tilt {card.tilt})" if card.tilt else "") + f"; decided by {', '.join(card.decided_by) or 'each party`s own accept'};"
         f" {card.turns} turn(s) each]"]
    pts = {p.id: p for p in out.state.points}
    for b in out.beats:
        who = b.mover if b.voice == b.mover else f"{b.mover} calls {b.voice}, who"
        if b.move == "argue":
            what = f"the {card.live}" if b.point is None else f"point {b.point}"
            if b.relation == "answers":
                p = pts[b.point]
                s = f"{who} answers {p.by}'s point {p.id} ({p.ground}) {_APPEAL[b.ground]}"
            else:
                s = f"{who} raises point {b.point} on {b.issue} {_APPEAL[b.ground]}" + (f" (framed on {b.frame})" if b.frame else "")
            if b.item:
                s += f", citing {b.item}"
            s += ": it " + ("lands" if b.margin >= 1 else "half lands" if b.margin >= 0 else "falls flat")
            if b.evaded:
                s += "; he has turned away from what was put to him and the room marks it"
            elif b.drift > 0.5:
                s += "; he wanders from the point"
            if b.insincere > 0.3:
                s += "; it is not what he himself holds"
        elif b.move == "press":
            s = f"{who} presses {b.target} {_APPEAL[b.ground]}" + (f", with {b.item}" if b.item else "")
            s += f": {b.target} is rattled" if b.rattled else f": {b.target} holds"
            if b.evaded:
                s += "; he has gone after the man and left the point unanswered, and the room marks it"
        elif b.move == "concede":
            s = f"{who} concedes {b.closed}" + ("" if out.ended != "yielded" or b is not out.beats[-1] else " and yields")
        else:
            s = f"{who} rests" + ("; the point against him stands unanswered" if b.evaded else "")
        if b.broke:
            s = "(he can hold his tongue no longer) " + s
        if b.evaded and b.move != "argue":
            s += "; the point against him stands unanswered and the room marks it"
        L.append(f"  {b.n}. [{b.issue}] {s}. (room {b.mood:+.2f})")
    return "\n".join(L + [f"  -> ended {out.ended}" + (f" by {out.ended_by}" if out.ended_by else "")])
