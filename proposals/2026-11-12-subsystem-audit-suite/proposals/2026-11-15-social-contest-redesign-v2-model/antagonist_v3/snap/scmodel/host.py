"""A toy host: builds a ProceedingInput from plain dicts of persons, following PLAN B24p.13 (`proceeding_input`),
B24p.06 (`moved_by`, `strain_carried`), B24p.03 (`abridged`), RD C.5 (`audience_kind`), C.6 (`row_for_case`).
The World reads (`judging_set`, `audience_of`, `world_q.proofs`, `reception`, `stance_toward`, `attributed_deeds`)
are replaced by fields on the person dicts.

Person dict (every key optional but `id`):
  id; attributes {focus, reason, attunement, presence, grace, will} (missing -> mid, B05.16);
  ranks {skill: rank} (held skills; `argue`, `insight`, `deception`); addends (practice dice);
  proofs (what he can show against the other side, raw); pursuits {id: weight in [0,1]}; convictions {id: 0..5};
  traits (set of `moved_by_<ground>`); weight (1; a cohort > 1); regard {other id: stance in [-1, 1]} (already over
  STANCE_MAX); seat {rung, faction, modifier} or None; knows (ids he holds a deed claim about -> accounts);
  marks_season, scenes_since (for strain_carried); operands [(name, raw, step, eased_by), ...] (e.g. rank_gap).
"""
from __future__ import annotations

import copy

from . import data
from .dice import level, pool_of
from .records import Decider, Move, ProceedingInput, ProceedingType, Room, Speaker

ATTRS = ("focus", "reason", "attunement", "presence", "grace", "will")


def _attr(p, k, D):
    return float(p.get("attributes", {}).get(k, D["attribute_mid"]))


# ---------------------------------------------------------------- B24p.06
def person_moved_by(p, D) -> tuple:
    """B24p.06 item 1: per GROUNDS row: attribute -> (attr - FLOOR) / (CEILING - FLOOR); pursuit: strongest ->
    max(pursuits, default 0) clamped [0,1]; conviction: strongest -> max(conviction, default 0) / scale_max (5);
    1.0 where p holds the row's trait."""
    fl, ce = D["attribute_floor"], D["attribute_ceiling"]
    out = []
    for g in data.GROUNDS:
        kind, key = g["read"]
        if g["trait"] in set(p.get("traits", ())):
            w = 1.0
        elif kind == "attribute":
            w = (_attr(p, key, D) - fl) / (ce - fl)
        elif kind == "pursuit":
            w = min(1.0, max(0.0, max(p.get("pursuits", {}).values(), default=0.0)))
        else:
            w = max(p.get("convictions", {}).values(), default=0) / 5.0     # affiliation_roster scale 0..5
        out.append((g["id"], w))
    return tuple(out)


def strain_carried(marks: int, scenes_since: int, D) -> float:
    """B24p.06 item 2: max(0, marks - strain_rest * scenes_since) * press_base; 0.0 when blow_gain is 0."""
    if D["blow_gain"] == 0:
        return 0.0
    return max(0.0, marks - D["strain_rest"] * scenes_since) * D["press_base"]


# ---------------------------------------------------------------- B24p.03 item 2, RD C.6 item 4
def abridged(row: dict, move: str = "argue") -> dict:
    m = data.MOVES_BY_ID.get(move)
    if m is None or not m["draw"]:
        raise ValueError(f"abridged: {move!r} is not a drawing move")
    r = copy.deepcopy(row)
    r["base_disposal"] = row["disposal"]
    r.update(order="free", exchanges=(1, 1), disposal="exchange", strikes=0, presumes="none", rite="plain",
             moves={"for": (move,), "against": (), "bench": ()})
    return r


# ---------------------------------------------------------------- RD C.5 / B24p.13 item 2
def audience_kind(bench: int, hearer_weight: float, crowd_at: float) -> str:
    if bench >= 1:
        return "bench"
    if hearer_weight >= crowd_at:
        return "crowd"
    if hearer_weight > 0:
        return "gallery"
    return "none"


# ---------------------------------------------------------------- RD C.6 item 3 / B24p.15
def row_for_case(seat: dict, matter: str, bench_size: int) -> str:
    authority = data.AUTHORITY_BY_FACTION.get(seat.get("faction"), "polity")
    rung = data.RUNG_KINDS.index(seat.get("rung", "hearth"))
    for when, rid in data.CASE_ROWS:
        row = data.ROWS[rid]
        if row["disposes"] not in data.DISPOSABLE_KINDS:
            continue
        if data.RUNG_KINDS.index(row["venue_min_rank"]) > rung:
            continue
        ok = True
        for k, v in when.items():
            if k == "authority" and v != authority:
                ok = False
            elif k == "matter" and v != matter:
                ok = False
            elif k == "bench" and v != ("several" if bench_size > 1 else "one"):
                ok = False
            elif k == "seat_at_least" and rung < data.RUNG_KINDS.index(v):
                ok = False
        if ok:
            return rid
    raise LookupError("no case row")   # G36: the last row `arbitration` can be skipped; see SPEC_GAPS


# ---------------------------------------------------------------- B24p.13 item 1
def _move_record(mid, D):
    m = data.MOVES_BY_ID[mid]
    rw = D["content_w_reason"][m["content"]] if "content" in m else None
    return Move(id=mid, draw=m["draw"], capability=m["capability"], resisted_by=m["resisted_by"], ground=m["ground"],
                fit=m["fit"], holds=m["holds"], effect=m["effect"], reason_weight=rw, ploy=m["ploy"],
                difficulty=m["difficulty"])


def _score(p, D):
    """`pool.score(w, p, verb)`: his held rank in the proceeding's skill (`argue`), else the untrained score (G37)."""
    r = p.get("ranks", {})
    return float(r["argue"]) if "argue" in r else float(D["pool_default"])


def _judging(p, D):
    """B24p.13 item 3: "the larger of his held rank in the capability `verb_capability` names for `determine` (today
    `argue`) and `untrained(fx)`, plus the `POOL_ADDENDS` sum" -- NOT through pool_of: no base, no floor (G13)."""
    return max(float(p.get("ranks", {}).get("argue", 0)), float(D["pool_default"])) + p.get("addends", 0)


def _base_pool(D):
    """RD C.7: "`Decider.pool` for a hearer or a party is `pool_of(untrained, 0, pool_add, pool_floor)`"."""
    return pool_of(D["pool_default"], 0, D["pool_add"], D["pool_floor"])


def _decider(p, D, pool, score, lean, modifier=None):
    return Decider(id=p["id"], weight=int(p.get("weight", 1)), pool=pool, score=score, grace=_attr(p, "grace", D),
                   attunement=_attr(p, "attunement", D), reason=_attr(p, "reason", D), focus=_attr(p, "focus", D),
                   will=_attr(p, "will", D), lean=lean, modifier=modifier, moved_by=person_moved_by(p, D))


def _lean(hearer, speaker_id, D):
    """RD C.7: stance_toward(hearer, speaker) clamped at STANCE_MAX times regard_step (the for speaker: G38)."""
    st = max(-1.0, min(1.0, hearer.get("regard", {}).get(speaker_id, 0.0)))
    return D["regard_step"] * st


def build_input(people, row, form="full", move="argue", *, actor, addressed=None, bench=(), present=(), effort=0,
                difficulty_level="routine", dials, topic="topic", order=None, state=None) -> ProceedingInput:
    """people: {id: person dict}; row: an arrangement id; form: full | abridged; actor: the `for` speaker;
    addressed: the one the act is made to (a person, or a cohort for a rally; None for an act on a matter: the
    presiding seat is seated, C.6 item 4); bench: the seats over the venue (judging_set, before the authority filter);
    present: everyone else at the venue (audience_of, before the floor filter); effort: the act's effort."""
    D = dials
    r = dict(data.ROWS[row])
    r["reason_bias"] = D["reason_bias"][row]
    r["standard"] = D["row_standard"][row]
    if form == "abridged":
        r = abridged(r, move)
    base_disp = r.get("base_disposal", r["disposal"])
    rite = data.RITES[r["rite"]]
    moves_by_side = r.get("moves") or {s: rite[s] for s in ("for", "against", "bench")}
    if order:
        r["order"] = order                                   # e.g. written_only for a filed petition (RD C.3)
    struck_ends = "irrelevance" in rite["faults"]
    # the bench: judging_set filtered by authority (RD C.7)
    seats = sorted((people[b] for b in bench), key=lambda p: p["id"])
    if r["authority"] not in ("parties", "none"):
        seats = [p for p in seats if p.get("seat") and
                 data.AUTHORITY_BY_FACTION.get(p["seat"].get("faction"), "polity") == r["authority"]]
    if base_disp in ("bench", "declared") and not seats:
        raise ValueError(f"{row}: empty bench after the {r['authority']} filter (party-gap refusal)")
    if form == "abridged" and addressed is None:
        addressed = seats[0]["id"] if seats else None       # speak: the presiding seat (C.6 item 4)
    A = people[actor]
    B = people[addressed] if addressed else None
    against_speaks = bool(moves_by_side["against"]) and B is not None
    speakers_p = [(A, "for")] + ([(B, "against")] if against_speaks else [])
    sp_ids = {p["id"] for p, _ in speakers_p}
    seat_ids = {p["id"] for p in seats}
    # hearers: present less speakers, the bench and the one addressed, by floor (RD C.5). G35: the addressed is NOT a
    # hearer (else C.5's "an abridged tell ... reads none" fails); so a rally to one cohort with nobody else present
    # reads `none`, not `crowd`.
    pres = [people[x] for x in present]
    pres = [p for p in pres if p["id"] not in sp_ids and p["id"] not in seat_ids
            and (B is None or p["id"] != B["id"])]
    if r["floor"] == "closed":
        hear_p = []
    elif r["floor"] == "admitted":
        hear_p = [p for p in pres if p.get("seat")]
    else:
        hear_p = pres
    hearers = tuple(_decider(p, D, _base_pool(D), _score(p, D), _lean(p, actor, D)) for p in hear_p)
    # room (RD C.5)
    hw = sum(int(p.get("weight", 1)) for p in hear_p)
    kind = audience_kind(len(seats) if base_disp in ("bench", "declared") else 0, hw, D["crowd_at"])
    rk = D["audience_room"][kind]

    def reception(sid):
        if not seats:
            return 0.0
        return sum(p.get("regard", {}).get(sid, 0.0) for p in seats) / len(seats)

    room = Room(audience=kind, attention=rk["attention"], distraction=rk["distraction"],
                proof_weight=rk["proof_weight"], reception=tuple((p["id"], reception(p["id"])) for p, _ in speakers_p))
    # speakers (B24p.13 item 1)
    speakers = []
    for p, side in speakers_p:
        other = B if side == "for" else A
        rec = reception(p["id"])
        ops = [("reception", max(0.0, -rec), D["reception_gain"], "will")]
        if other is not None and kind == "none" and not seats:     # B05.21: regard "one person counterparty,
            st = other.get("regard", {}).get(p["id"], 0.0)          # no audience; never with a bench"
            ops.append(("regard", max(0.0, min(1.0, -st)), D["regard_step"], "will"))
        ops += [tuple(o) for o in p.get("operands", ())]
        knows = other is not None and other["id"] in set(p.get("knows", ()))
        accounts = tuple(o[0] for o in ops if o[3] == "reason") if knows else ()
        levels = []
        fav = int(max(0.0, D["reception_gain"] * rec) + 0.5)           # B05.17: one favour_level per whole unit
        if fav:
            levels.append(("favour", level(D["favour_level"]) * fav, 0.0))
        seat = p.get("seat") or {}
        if seat.get("modifier"):
            levels.append(("office", level(seat["modifier"]), 0.0))    # A-12: office, one level
        speakers.append(Speaker(
            id=p["id"], side=side, **{k: _attr(p, k, D) for k in ATTRS},
            ranks=tuple(sorted(p.get("ranks", {}).items())), addends=int(p.get("addends", 0)), score=_score(p, D),
            proofs=float(p.get("proofs", 0.0)), accounts=accounts,
            precedence=(data.RUNG_KINDS.index(seat["rung"]) + 1) if seat.get("rung") else 0,
            effort=effort + 1, levels=tuple(levels), operands=tuple(ops), moved_by=person_moved_by(p, D),
            strain=strain_carried(p.get("marks_season", 0), p.get("scenes_since", 0), D)))
    # deciders (B24p.13 item 1)
    disp = r["disposal"]
    if disp in ("bench", "declared"):
        resp = _score(B, D) if against_speaks else None              # "a seat's is the respondent's" (G34)
        deciders = tuple(_decider(p, D, _judging(p, D), resp if resp is not None else _score(p, D), 0.0,
                                  (p.get("seat") or {}).get("modifier")) for p in seats)
    elif disp == "hearers":
        first = []
        if B is not None:
            first = [_decider(B, D, _base_pool(D), _score(B, D), _lean(B, actor, D))]
        deciders = tuple(first + list(hearers))
    elif disp == "exchange":
        if B is None:
            raise ValueError("abridged form with nobody addressed")
        deciders = (_decider(B, D, _base_pool(D), _score(B, D), _lean(B, actor, D),
                             (B.get("seat") or {}).get("modifier")),)
    else:
        deciders = ()
    typ = ProceedingType(
        id=row, disposal=disp, order=r["order"], exchanges=tuple(r["exchanges"]),
        moves=tuple((s, tuple(_move_record(m, D) for m in moves_by_side[s])) for s in ("for", "against", "bench")),
        standard=D["standard_demand"][r["standard"]], difficulty=D["difficulty_ob"][difficulty_level],
        stakes=D["stakes_ob"].get(r["disposes"], 0.0), presumes=r["presumes"], reason_bias=r["reason_bias"],
        quorum=r["quorum"], break_at=D["break_at"], strikes=r["strikes"], struck_ends=struck_ends,
        base_disposal=base_disp)
    ground_reason = tuple((g["id"], D["content_w_reason"][g["content"]]) for g in data.GROUNDS)
    return ProceedingInput(type=typ, topic=topic, issue=None, speakers=tuple(speakers), deciders=deciders,
                           hearers=hearers, room=room, grounds=data.GROUND_IDS, ground_reason=ground_reason,
                           dials=D, state=state)
