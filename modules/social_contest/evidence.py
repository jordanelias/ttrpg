"""B24.19 -- `standing`, THE ONE EVIDENCE RULE (EVID_B "`standing`: the rules, in order"; "Exact edits" 3).

WHICH of the exhibits shown at a sitting still count, at what weight, which are struck and what the sitting owes for it: a pure function of the
`Item`s shown, World-free, rolling nothing. The answering act's own band (`Item.answered_band`, graded once on the ladder by whoever drew the answer)
is read, never regraded here.

THE RELATION IS DATA. This module names no `engine/season` module and restates no pairing rule: the host builder computes `contradicts` (the one owner,
`decision/options.py::contradicts`) and hands it over as `Item.pairs`, `((other exhibit id, "contradicts" | "agrees"), ...)` over the other filed
exhibits. `pair_of` is the one reader of that field.

THE RULES, in order, each over the items still standing after the one before:
  1. FORGERY -- an item a filed finding names forged (`findings`), answered: Failure it stands; Partial it is halved; Success it is struck; Overwhelming it and every item of its origin are struck and `forgery_found` is
     recorded against its side.
  2. CONTRADICTION -- an answered item the other side holds an item against: Failure it stands; Partial it and its answer (the heaviest such item) are
     halved; Success it is struck; Overwhelming it is struck and `self_contradiction` is recorded against its side if its holder knew it false
     (`not sincere`). An item with no answering act is never struck.
  3. AGREEMENT -- the same cell and value put by BOTH sides counts for neither (struck by nothing: it is simply not counted).
  4. CORROBORATION -- the same cell and value put by one side from DISTINCT origins is one item of weight `1 - prod(1 - w)`, no lighter than its
     heaviest member and gaining no more than `evidence_cap` over it; the same origin twice counts once.

An item with no `origin` is its own origin (nothing says it comes from anything another item does).

THE COST OF A FAILED IMPEACHMENT AND OF A DISCREDITED SOURCE IS NOT A FAULT HERE: `standing` emits neither `failed_impeachment` nor `discredited_source`. What an answering act costs
the one who made it, or the one it discredits, is the answering act's Event, which the room witnesses (B24.24, B24.25), never a fault this function owes.
"""
from __future__ import annotations

import functools
from collections import Counter
from dataclasses import replace
from typing import Optional

from engine.dice_engine import dice_engine

CONTRADICTS, AGREES = "contradicts", "agrees"
_ORD = {label: dice_engine.DEGREE_ORDINAL[deg] for deg, label in dice_engine.DEGREE_LABEL.items()}      # the ladder owner's own two maps, joined
FAILURE, PARTIAL, SUCCESS, OVERWHELMING = (_ORD[b] for b in ("Failure", "Partial", "Success", "Overwhelming"))


def band_of(label: Optional[str]) -> Optional[int]:
    """a band label (`DEGREE_LABEL`) as its ordinal, `None` where there is none."""
    return None if label is None else _ORD[label]


def pair_of(a, b) -> Optional[str]:
    """how the host filed `a` against `b`: `"contradicts"`, `"agrees"` or `None`. Read from either item's `pairs`: the one reader of the field."""
    for x, y in ((a, b), (b, a)):
        for iid, how in x.pairs:
            if iid == y.id:
                return how
    return None


def _rank(it) -> tuple:
    return (it.weight, it.id)


@functools.lru_cache(maxsize=4096)
def standing(presented: tuple, findings: tuple = (), cap: Optional[float] = None) -> tuple:
    """`(standing, struck, faults)` over `presented` (the `Item`s shown, at the weight they were entered at, in the order shown).

    `findings` -- the ids of the items a filed finding names forged; `cap` -- `evidence_cap` (`None`: uncapped).
    `standing` -- the items that count, in the order shown, each at the weight it now carries; `struck` -- the ids struck; `faults` -- `((a
    `proceeding_faults` member, who bears it), ...)`. Pure: the same board gives the same answer, so a caller
    recomputes it at every change rather than keeping what a past change left."""
    by_id = {it.id: it for it in presented}
    forged = frozenset(findings)
    struck, halved, faults = set(), set(), []
    for it in presented:                                                         # 1. forgery
        b = band_of(it.answered_band)
        if b is None or it.id not in forged:
            continue
        if b == PARTIAL:
            halved.add(it.id)
        elif b >= SUCCESS:                                                       # Failure: it stands, and the impeacher's cost is the answering act's Event, not a fault
            struck.add(it.id)
            if b == OVERWHELMING:
                struck.update(o.id for o in presented if it.origin is not None and o.origin == it.origin)
                faults.append(("forgery_found", it.side))
    for it in presented:                                                         # 2. contradiction
        b = band_of(it.answered_band)
        if b is None or it.id in forged or it.id in struck:
            continue
        mine = [o for o in presented if o.id not in struck and o.side != it.side and pair_of(it, o) == CONTRADICTS]
        if not mine:
            continue                                                             # nothing of the other side says otherwise: no answering act is to be read
        if b == PARTIAL:
            halved.update((it.id, max(mine, key=_rank).id))
        elif b >= SUCCESS:
            struck.add(it.id)
            if b == OVERWHELMING and not it.sincere:
                faults.append(("self_contradiction", it.side))
    live = [replace(it, weight=it.weight / 2.0) if it.id in halved else it for it in presented if it.id not in struck]
    agreed = {it.id for it in live for o in live if it.side is not None and o.side is not None and o.side != it.side and pair_of(it, o) == AGREES}   # 3.
    live = [it for it in live if it.id not in agreed]
    root = {it.id: it.id for it in live}                                         # 4. corroboration: components of the same side's `agrees` pairs
    def find(x):
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x
    for it in live:
        for o in live:
            if o.id > it.id and o.side == it.side and pair_of(it, o) == AGREES:
                root[find(o.id)] = find(it.id)
    groups = {}
    for it in live:
        groups.setdefault(find(it.id), []).append(it)
    kept = {}
    for g in groups.values():
        once = {}
        for it in g:                                                             # the same origin counts once: its heaviest
            k = it.origin if it.origin is not None else it.id
            if k not in once or it.weight > once[k].weight:
                once[k] = it
        top = max(once.values(), key=lambda i: i.weight)                     # the first shown of the heaviest stands for the group
        miss = 1.0
        for it in once.values():
            miss *= 1.0 - min(it.weight, 1.0)
        merged = max(top.weight, (1.0 - miss) if cap is None else min(cap, 1.0 - miss))
        kept[top.id] = replace(top, weight=merged) if len(once) > 1 else top
    out = tuple(kept[it.id] for it in live if it.id in kept)
    return out, tuple(sorted(struck, key=lambda i: [p.id for p in presented].index(i))), tuple(faults)


def newly_owed(before: tuple, after: tuple) -> tuple:
    """the faults `after` records that `before` did not: what one board change added (a fault is a count, so a repeat is a new one)."""
    gone = Counter(before)
    new = []
    for f in after:
        if gone[f] > 0:
            gone[f] -= 1
        else:
            new.append(f)
    return tuple(new)
