"""`season.data.tensions` -- THE TENSIONS DECK'S ONE LOADER (B12b.45, CL-EVENTS commit (3)).

`engine/season/tensions.yaml` authors the cards; `boot/realm.py::build_realm(tensions=True)` draws ONE at the world's making and applies it.
A TENSION is a strain drawn at the world's making that sets some people's aims (`rosters.yaml: tension_effects`' note); it is read once, at
build, by no step of the season loop. This module READS and VALIDATES and, given a picker, fills a card's `choose_one` lists; it draws nothing
(the draw is the realm's, keyed on the world seed) and guesses nothing. Every name a card carries is resolved against the one owner of that fact,
and a card that does not resolve is REFUSED by name, never skipped or coerced (`data/goals.py`'s line, one layer down):

  * a key outside the schema (`id`, `text`, `source`, `effects`) -- a date, deadline or firing condition, an outcome, a write to standing, a seat,
    a tenure or a stance, `closing`, `successor`, `deal` -- is refused, naming it (M20's line applied to a card);
  * an effect `kind:` is a member of `rosters.yaml: tension_effects`; its own keys are the kind's and no others;
  * a `goal` effect's row is parsed TOGETHER WITH `goals.yaml`'s rows by `data/goals.py::parse` -- ONE VALIDATOR, so a seat, an org, a `derives`
    parent and an id (which may not repeat a `goals.yaml` id) resolve in one pass and refuse in goals' own words, law string and all;
  * a `yield_scale` effect's territory is a territory of `data/geography.py`, its scale a finite number above zero, and a territory is scaled
    once per card;
  * `{choose_one: [a, b, ...]}` stands for one of its values wherever a value stands in a goal row; it may not be empty, and EVERY combination of
    picks is parsed, so no draw can reach a card the loader did not accept.
"""
from __future__ import annotations

import contextlib
import itertools
import math
from dataclasses import dataclass
from typing import Optional

from . import files
from . import goals as goals_data
from .geography import geography
from .rosters import load_yaml, require_member, roster, territory_rung_id
from ..gaps import Forbidden, Unspecified

TENSIONS_YAML = files.TENSIONS_YAML

_LAW = ("B12b.45 (CL-EVENTS commit (3)) -- a Tensions card is authored in tensions.yaml and names what is strained at the world's making, "
        "never what happens")
_NOT_DATA = ("a date, a deadline or a firing condition, an outcome, a write to standing, a seat, a tenure or a stance of a person, and a "
             "`closing`, `successor` or `deal` key are not data of a card")

# The one key a `choose_one` mapping carries; a mapping holding it with any other key is no pick, and is refused.
_PICK = "choose_one"


@dataclass(frozen=True)
class Card:
    """One validated `tensions.yaml` row. `goals` are the `goal` effects' rows as authored (a `{choose_one: [...]}` mapping still standing where one
    was written), `scales` the `yield_scale` effects as `((territory rung id, scale), ...)` sorted by rung, and `lists` the `choose_one` lists in
    the order the draw keys them (`(card id, ordinal)`)."""
    id: str
    text: str
    source: str
    goals: tuple
    scales: tuple
    lists: tuple


@dataclass(frozen=True)
class Drawn:
    """A card applied: its id, its goals as `data/goals.py::Goal`s (every pick made) and its scales."""
    card: str
    goals: tuple
    yield_scale: tuple


def _refuse(cls, cid, what: str, needs: str):
    raise cls(f"tension {cid!r}: {what}", f"tensions.yaml -- {cid}", needs=needs, law=_LAW)


def _text(cid, row: dict, key: str) -> str:
    v = row.pop(key, None)
    if not isinstance(v, str) or not v.strip():
        _refuse(Unspecified, cid, f"carries no `{key}:` string", f"a non-empty `{key}:`")
    return v


def _lists(node, out: list) -> None:
    """Append every `choose_one` list under `node` to `out`, in document order; refuse an empty or malformed one."""
    if isinstance(node, dict):
        if _PICK in node:
            options = node[_PICK]
            if len(node) != 1 or not isinstance(options, list) or not options:
                raise Unspecified(f"`{_PICK}` is {node!r}, not the one key of a non-empty list", "tensions.yaml",
                                  needs=f"`{{{_PICK}: [a, b, ...]}}` with at least one value, and no other key beside it", law=_LAW)
            out.append(options)
            return
        for v in node.values():
            _lists(v, out)
    elif isinstance(node, list):
        for v in node:
            _lists(v, out)


def _filled(node, picks):
    """`node` with each `choose_one` mapping replaced by the next of `picks` (document order, as `_lists` found them)."""
    if isinstance(node, dict):
        if _PICK in node:
            return next(picks)
        return {k: _filled(v, picks) for k, v in node.items()}
    if isinstance(node, list):
        return [_filled(v, picks) for v in node]
    return node


def _goal_effect(cid, e: dict) -> dict:
    row = e.pop("goal", None)
    if not isinstance(row, dict):
        _refuse(Unspecified, cid, f"a `goal` effect's `goal:` is {row!r}, not a goals.yaml row", "`goal: {id: ..., org: ..., ...}`")
    return row


def _scale_effect(cid, e: dict, seen: set) -> tuple:
    territory, scale = e.pop("territory", None), e.pop("scale", None)
    if not isinstance(territory, str) or territory not in geography()["provinces"]:
        _refuse(Unspecified, cid, f"a `yield_scale` effect names the territory {territory!r}, which geography does not hold",
                "a territory code of `valoria_geography_v30.yaml: provinces`")
    if territory in seen:
        _refuse(Forbidden, cid, f"`yield_scale` scales {territory!r} twice", "one `yield_scale` per territory per card")
    if isinstance(scale, bool) or not isinstance(scale, (int, float)) or not math.isfinite(scale) or not scale > 0:
        _refuse(Unspecified, cid, f"a `yield_scale` effect's `scale:` is {scale!r}", "a finite number above 0")
    seen.add(territory)
    return territory_rung_id(territory), scale


def _goals_doc() -> dict:
    """`goals.yaml`, parsed raw: the document a card's goal rows are checked beside."""
    try:
        text = goals_data.GOALS_YAML.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise Unspecified(f"the goals file at {goals_data.GOALS_YAML}", "engine/season/goals.yaml",
                          needs="`goals: []` or a list of goal rows",
                          law="a card's goals are parsed beside goals.yaml's; none can be read from nothing") from exc
    return load_yaml(text) or {}


def _together(base: dict, rows: list) -> tuple:
    """`goals.yaml`'s document with `rows` appended to its goals, through `data/goals.py::parse`: the `Goal`s of `rows` alone, in order."""
    out = goals_data.parse({**base, "goals": [*(base.get("goals") or []), *rows]})
    return out[len(base.get("goals") or []):]


def _card(row, base: dict) -> Card:
    if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"].strip():
        raise Unspecified(f"a card is {row!r}, with no `id:` string", "tensions.yaml", needs="a unique `id:`", law=_LAW)
    left = dict(row)
    cid = left.pop("id")
    text, source = _text(cid, left, "text"), _text(cid, left, "source")
    effects = left.pop("effects", None)
    if left:
        _refuse(Forbidden, cid, f"carries {sorted(map(str, left))}, which a card does not read",
                f"a card is its id, text, source and effects and nothing else ({_NOT_DATA})")
    if not isinstance(effects, list):
        _refuse(Unspecified, cid, f"`effects:` is {effects!r}, not a list", "`effects: []` or a list of effects")
    kinds = roster("tension_effects")
    goals, scales, seen = [], [], set()
    for e in effects:
        if not isinstance(e, dict):
            _refuse(Unspecified, cid, f"an effect is {e!r}, not a mapping", "`{kind: <tension_effects member>, ...}`")
        left = dict(e)
        kind = left.pop("kind", None)
        require_member(kind, kinds, f"tension {cid!r}: effect kind {kind!r} is not rostered", f"tensions.yaml -- {cid}", law=_LAW)
        if kind == "goal":
            goals.append(_goal_effect(cid, left))
        else:
            scales.append(_scale_effect(cid, left, seen))
        if left:
            _refuse(Forbidden, cid, f"a `{kind}` effect carries {sorted(map(str, left))}, which it does not read",
                    f"an effect is its `kind:` and the kind's own keys and nothing else ({_NOT_DATA})")
    lists: list = []
    _lists(goals, lists)
    for combo in itertools.product(*(range(len(o)) for o in lists)):
        picks = iter(lists[i][j] for i, j in enumerate(combo))
        _together(base, _filled(goals, picks))
    return Card(cid, text, source, tuple(goals), tuple(sorted(scales)), tuple(tuple(o) for o in lists))


def parse(doc, goals_doc: Optional[dict] = None) -> tuple:
    """`doc` (a parsed `tensions.yaml`) as `Card`s in file order; raise on the first card that breaks the schema. `tensions: []` is the shipped
    state and loads to `()`. `goals_doc` (default: `goals.yaml`, read raw) is the document a card's goal rows are parsed beside."""
    rows = doc.get("tensions") if isinstance(doc, dict) else None
    if not isinstance(rows, list):
        raise Unspecified("tensions.yaml has no `tensions:` list", "tensions.yaml", needs="`tensions: []` or a list of cards", law=_LAW)
    stray = sorted(str(k) for k in doc if k != "tensions")
    if stray:
        raise Forbidden(f"tensions.yaml carries the top-level key(s) {stray}", "tensions.yaml", needs="`tensions:` only", law=_LAW)
    ids = [r.get("id") for r in rows if isinstance(r, dict)]
    for cid in ids:
        if ids.count(cid) > 1:
            _refuse(Forbidden, cid, "more than one card carries this id", "one card per `id`")
    base = _goals_doc() if goals_doc is None else goals_doc
    return tuple(_card(r, base) for r in rows)


def resolve(card: Card, pick, goals_doc: Optional[dict] = None) -> Drawn:
    """`card` with every `choose_one` list answered by `pick(card id, ordinal, options)` (the draw is the caller's), its goal rows made `Goal`s by
    `data/goals.py::parse` beside `goals.yaml`'s, and its scales as `Fixtures territory_yield_scale` holds them."""
    chosen = iter([pick(card.id, i, options) for i, options in enumerate(card.lists)])
    rows = _filled(list(card.goals), chosen)
    base = _goals_doc() if goals_doc is None else goals_doc
    return Drawn(card.id, _together(base, rows), card.scales)


_CACHE: Optional[tuple] = None


def cards() -> tuple:
    """Every card, in file order, read once and kept. Raises `Unspecified` rather than returning `()` if the file is absent: a deck read from
    nothing cannot be told from a deck authored empty."""
    global _CACHE
    if _CACHE is None:
        try:
            text = TENSIONS_YAML.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise Unspecified(f"the tensions file at {TENSIONS_YAML}", "engine/season/tensions.yaml", needs="`tensions: []` or a list of cards",
                              law="a deck read from nothing cannot be told from a deck authored empty") from exc
        _CACHE = parse(load_yaml(text) or {})
    return _CACHE


def load() -> tuple:
    """`data.load_all`'s handle on this loader: read the file now, so a malformed card refuses at the one entry rather than at the first world
    that draws one. The same cache `cards()` fills."""
    return cards()


@contextlib.contextmanager
def cards_replaced(rows: tuple = ()):
    """The deck the reader sees, swapped for `rows` (`Card`s from `parse`) for the block and restored after: the one place that touches the cache."""
    global _CACHE
    saved, _CACHE = _CACHE, rows
    try:
        yield
    finally:
        _CACHE = saved
