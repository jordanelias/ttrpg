"""sc2.acts -- the acts AROUND a sitting (host side; the module never sees them):

  before(...)  D1: the weak party's choice when the card shows a forum tilted against him: accept it, or take
               the matter elsewhere where another authority sits (`contest` was cut: best in no case). Each is an
               executable act with a visible price; after a loss his recourse is appeal.
  after(...)   D3: the loser's choice when a sitting has gone against him: accept, appeal (a re-hearing before
               another authority), another forum, or a grudge carried to a later sitting. It READS compliance and
               the appeal weight the fold wrote (A-144 reception), so those have a reader.
  season(...)  D2: a minimal labelled season driver: it convenes the recurring matters and the docket (appeals,
               grievances, adjourned matters, other forums), folds each sitting, lets the loser act, and fades
               regard, legitimacy, standing and strain between seasons. Every world quantity it moves is bounded.

Every number here is [ASSUMPTION; Jordan to correct] and lives in host.FOLD.
"""
from __future__ import annotations

import copy
from typing import Callable, Optional

from scmodel.rng import draw
from . import host
from .engine import SIGN, proceed

F = host.FOLD


def _stake(people, pid, matter):
    return abs(sum(host.bearing(people[pid], matter, people)) / 3.0)     # a party's least stake is the bearing's own


def _his_odds(inp, side, start):
    from .engine import p_carried
    p = p_carried(inp, start)
    return p if side == "for" else 1.0 - p


# ------------------------------------------------------------------ D1: before a tilted forum
def before(people, rite_id, matter, *, arranger, rig, alt_bench=(), choose: Optional[Callable] = None, **kw):
    """-> (act, rig actually sat at, the docket entry or None, the options shown). `choose(options)` is a player's
    choice; with none the weak party takes the option of greatest worth as the card lets him see it. Each option's
    worth is 2 x his stake x his side's odds in that forum, less its price: accept (none); elsewhere, only where
    another authority has seats (`alt_bench`): a fair forum, a season's delay. (`contest` was cut: best in no case;
    his recourse is elsewhere before, and appeal after.)"""
    inp, card = host.build(people, rite_id, matter, arranger=arranger, rig=rig, **kw)
    if card.tilt <= 0:
        return "accept", rig, None, ()
    weak = card.tilted_against
    wid = matter["parties"][weak]
    D = inp.dials
    st = _stake(people, wid, matter)
    lean = -SIGN[weak] * card.tilt * D["presume_step"]          # where the packed bench starts, as the card shows it
    fair = _his_odds(inp, weak, 0.0)
    opts = (("accept", 2.0 * st * _his_odds(inp, weak, lean), "none"),) \
        + ((("elsewhere", 2.0 * st * fair - 2.0 * F["lost"], "a season's delay before a fair forum"),) if alt_bench else ())
    act = choose(opts) if choose else max(opts, key=lambda o: o[1])[0]
    if act == "elsewhere":
        return act, 0.0, dict(matter=matter["id"], kind="other_forum", party=wid, weight=0.0, bench=tuple(alt_bench)), opts
    return act, rig, None, opts


# ------------------------------------------------------------------ D3: after a sitting that went against him
def after(world, people, inp, card, out, matter, band, choose: Optional[Callable] = None, appeal: bool = True):
    """-> (act, options). The loser's menu, each line with its believed worth and its price; the act's effect is
    written to the world (a docket entry the season driver convenes, and regard). `appeal`: whether an appeal lies
    (C9: an appeal's own verdict is final, and an appeal lies only to a forum that exists and may hear the matter;
    the caller, who knows the forum, says so)."""
    fid, aid = matter["parties"]["for"], matter["parties"].get("against")
    if aid is None or band in (None, "partial"):
        return None, ()
    won = band in ("success", "overwhelming")
    loser, winner = (aid, fid) if won else (fid, aid)
    side = "against" if won else "for"
    st = _stake(people, loser, matter)
    comp = world["compliance"].get(matter["id"], 1.0)
    aw = world["appeal_weight"].get(matter["id"], 0.0)
    D = inp.dials
    R = world["regard"]
    grudge = -R.get((loser, winner), 0.0)
    other = any(d["matter"] == matter["id"] and d["kind"] == "other_forum" for d in world["docket"])
    opts = [("accept", -(1.0 - comp) * st, "the disposal holds")]
    if appeal and inp.rite.close in ("bench", "declared"):
        opts.append(("appeal", 2.0 * st * _his_odds(inp, side, SIGN[side] * D["presume_step"] * aw) - F["contumacy"],
                     "the first judge's regard; standing if it fails"))
    if other:
        opts.append(("other_forum", 2.0 * st * 0.25, "a season's delay"))
    if not str(matter["id"]).startswith("grudge:"):          # a grudge once aired is settled by its hearing
        opts.append(("retaliate", 0.5 * grudge - F["contumacy"], "his regard for the winner, a grudge on the docket"))
    act = choose(opts) if choose else max(opts, key=lambda o: o[1])[0]
    if act == "appeal":
        world["docket"].append(dict(matter=matter["id"], kind="appeal", party=loser, weight=aw, rite=card.kind))
        for j in card.decided_by:
            R[(j, loser)] = host.bounded(R.get((j, loser), 0.0), -F["contumacy"])
    elif act == "retaliate":
        world["docket"].append(dict(matter=f"grudge:{loser}:{winner}", kind="grievance", party=loser, against=winner, weight=0.0))
        R[(loser, winner)] = host.bounded(R.get((loser, winner), 0.0), -F["lost"])
    elif act == "accept":
        R[(loser, winner)] = host.bounded(R.get((loser, winner), 0.0), F["lost"] * comp)   # a verdict he can live with
    if act != "other_forum":                       # taking another road drops the other forum the disposal offered
        world["docket"] = [d for d in world["docket"] if not (d["matter"] == matter["id"] and d["kind"] == "other_forum")]
    return act, tuple(opts)


# ------------------------------------------------------------------ D2: the season driver
def fade(world):
    """between seasons every bounded quantity fades toward 0 by FOLD['fade']: time heals and fame is forgotten."""
    k = 1.0 - F["fade"]
    for key in ("regard", "legitimacy", "standing", "pursuits"):
        world[key] = {a: v * k for a, v in world[key].items() if abs(v * k) > 1e-3}
    world["rattled"] = {p: [s + 1 for s in v if s + 1 < 4] for p, v in world["rattled"].items()}
    world["docket"] = [dict(d, age=d.get("age", 0) + 1) for d in world["docket"] if d.get("age", 0) < 2]


def _carry_strain(people, world):
    pp = copy.deepcopy(people)
    for pid, ago in world["rattled"].items():
        if pid in pp:
            pp[pid]["rattled_ago"] = tuple(ago)
    return pp


def _sits(people, rite, matter, kw) -> bool:
    """whether a forum exists and may hear the matter: the builder does not refuse it."""
    try:
        host.build(people, rite, matter, **kw)
        return True
    except ValueError as e:
        if str(e).startswith("refused["):
            return False
        raise


def convene(world, people, rite, matter, key, appeal_kw=None, **kw):
    """one sitting: build, proceed, fold, and the loser's after-sitting act. `appeal_kw`: the forum an appeal would
    sit before (None where the verdict is final: an appeal's own)."""
    pp = _carry_strain(people, world)
    inp, card = host.build(pp, rite, matter, **kw)
    out = proceed(inp, draw(key, "act", rite))
    band, writes = host.fold(world, pp, inp, card, out, matter)
    act, _ = after(world, pp, inp, card, out, matter, band, appeal=appeal_kw is not None and _sits(pp, rite, matter, appeal_kw))
    return dict(rite=rite, matter=matter["id"], band=band, act=act, card=card, out=out, inp=inp)


def _convene_or_skip(world, ran, s, kind, *a, **kw):
    """C2: a keyed refusal (a vacated seat, a man who is gone, a forum that cannot sit) skips THAT sitting and is
    recorded (`world['refused']`); the season goes on. Anything else is a fault and is raised."""
    try:
        ran.append(convene(world, *a, **kw))
        return ran[-1]
    except ValueError as e:
        if not str(e).startswith("refused["):
            raise
        world.setdefault("refused", []).append((s, kind, a[2]["id"], str(e).split("]")[0] + "]"))
        return None


def season(world, people, schedule, s, *, appeal_bench=(), grievance_rite="conversation", key="season"):
    """`schedule`: [(rite, matter, build kwargs)], convened every season; then the docket as it stood at the start
    of the season: appeals (re-heard before `appeal_bench`, no rig, the appellant's grounds weighed as a presumption
    toward him), grievances (a conversation between the two), adjourned matters (the same row), other forums
    (arbitration). Returns the season's sittings."""
    ran = []
    up = lambda kw: dict(kw, bench=appeal_bench or kw.get("bench", ()), rig=0.0, arranger=None)   # where an appeal sits
    for k, (rite, m, kw) in enumerate(schedule):
        if m.get("strife") and m["strife"] not in world["strife"] and s == 0:
            world["strife"][m["strife"]] = 1.0                       # the world's own strife, seeded once, not by a sitting
        _convene_or_skip(world, ran, s, "sched", people, rite, m, (key, s, "sched", k), appeal_kw=up(kw), **kw)
    docket, world["docket"] = list(world["docket"]), []
    by_id = {m["id"]: (rite, m, kw) for rite, m, kw in schedule}
    for k, d in enumerate(docket):
        base = by_id.get(d["matter"])
        if d["kind"] == "appeal" and base:
            rite, m, kw = base
            kw2 = dict(up(kw), grounds_for=("for" if d["party"] == m["parties"]["for"] else "against", d["weight"]))
            res = _convene_or_skip(world, ran, s, "appeal", people, rite, m, (key, s, "appeal", k), appeal_kw=None, **kw2)
            if res is None:                                          # the appeal could not sit: the verdict stands
                continue
            res["appeal"] = d
            if (res["band"] in ("success", "overwhelming")) == (d["party"] == m["parties"]["for"]):
                world["tenures"] = [t for t in world["tenures"] if not (t[2] == m["id"] and t[1] == d["party"])]
                res["reversed"] = True
            else:
                res["reversed"] = False
        elif d["kind"] == "grievance" and d.get("against"):
            m = dict(id=d["matter"], parties={"for": d["party"], "against": d["against"]}, bears={})
            _convene_or_skip(world, ran, s, "grievance", people, grievance_rite, m, (key, s, "griev", k), effort=2)
        elif d["kind"] in ("adjourned", "other_forum") and base:
            rite, m, kw = base
            if d["kind"] == "other_forum":
                rite, kw = "arbitration", dict(kw, rig=0.0, arranger=None, bench=kw.get("bench") or appeal_bench)
            _convene_or_skip(world, ran, s, d["kind"], people, rite, m, (key, s, d["kind"], k), appeal_kw=up(kw), **kw)
    fade(world)
    return ran
