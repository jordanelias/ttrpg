"""`loop/calendar.py` -- CALENDAR -- barrier 1. `04 §A.2`: owns `Date.fired`, `DocketItem`, `ConveningCondition`; emits `date.fired` / `docket.formed`; token CALENDAR.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.calendar = calendar`, so `SeasonDriver.calendar` IS this
function and `inspect.getsource(SeasonDriver.calendar)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS HANDED IN BY THE DRIVER (G2).** `SeasonDriver.season` mints a CALENDAR `Token`
through `loop/driver.py::mint_token` and passes it as `token`; every gate write below presents
it. This module constructs none and calls no minter -- `tests/test_g2_token.py` fails if it does.
"""

from __future__ import annotations

from ..data.matrix import Step
from ..queries import world_q
from ..queries.world_q import FIRED_KIND
from ..state.carriers import Event
from ..state.gate import Token
from ..state.ids import ROOT
from ..trace_log import TRACE



def _reslot(w, item: dict, slot: dict) -> None:
    """v11 CR-56: the waiting `item` TAKES the open `slot`'s place, dated with the slot's `date`, and leaves
    its own -- one docket item per matter, as `open_case`'s fill leaves it. The item moves whole, so no key is
    written into an item another step formed (CR-55's lapse removes an item whole under the same cell)."""
    w.docket[:] = [{**item, "date": slot["date"]} if d is slot else d for d in w.docket if d is not item]


# -- CALENDAR -- barrier 1 -- DECIDES NOTHING (S24) ----------------------
def calendar(self, token: Token) -> list[Event]:
    w = self.w
    w.step = Step.CALENDAR
    TRACE.step("CALENDAR", "enter"); TRACE.barrier(1, "CALENDAR")
    w.discard_caches()
    # ⚠ RETURNS ITS OWN EMISSIONS, SO `season()` CAN HAND THEM TO WITNESS BESIDE MATTER'S (IN-29).
    # `World.write` buffers an emission for fan-out ONLY at `Step.MATTER` (`state/world.py`, the
    # `_emitted_by_write` guard, which exists to keep WITNESS's own `claim.deposited` from looping),
    # so CALENDAR's `date.fired` reached `w.log` and nothing else. The log tail since this mark is
    # exactly what this barrier's writes emitted -- nothing else writes between here and the return.
    _mark = len(w.log)
    for did, d in list(w.dates.items()):
        if d.get("due_at") != w.tick:
            continue
        vacant = not d.get("holder")
        TRACE.decision(f"date {did} came due", "S24",
                       chose="fire-and-lapse" if vacant else "fire-as-sitting",
                       alternatives=["block until a holder exists", "defer to next season"])
        # ⚠ CHAINED ON THE VENUE, NOT `did` -- `last_emission_of`'s second argument must equal
        # the write's own `subject=`, because it matches `anchor_of(...) == subject` and
        # `anchor_of`'s tier 2 reads back exactly the `subject=` a write passed (`W4`,
        # `state/world.py:1042-1046`). Every MATTER clock this mirrors (`body.changed`/`pid`,
        # `stores.changed`/`yield.taken`/`rid` in `loop/matter.py`) uses the SAME value in both
        # places; chaining on `did` here would look for a prior Event whose subject is `did`,
        # which no `date.fired` Event ever carries (its subject is always the venue) -- so the
        # chain would silently never leave `[ROOT]`, on every date, forever.
        prior = w.last_emission_of(FIRED_KIND, d.get("venue"))
        w.write("Date", token, lambda d=d: d.__setitem__("fired", True),
                record_kind="Date", fieldname="fired", driver="Event",
                emits=FIRED_KIND, subject=d.get("venue"),
                causes=[prior] if prior else [ROOT])
        if not vacant:
            # `04 §A.2` and `write_matrix.yaml`'s (DocketItem, matter) row give CALENDAR `docket.formed`; the write
            # emitted nothing, the same defect `11b` closed for `date.fired`. Chained on the `date.fired` just emitted
            # at this venue, under the same subject, so the antecedent is the firing that put the matter on the docket.
            fired = w.last_emission_of(FIRED_KIND, d.get("venue"))
            w.write("DocketItem", token,
                    lambda did=did: w.docket.append({"date": did, "matter": None}),
                    record_kind="DocketItem", fieldname="matter", driver="Event",
                    emits="docket.formed", subject=d.get("venue"),
                    causes=[fired] if fired else [ROOT])
    # -- v11 CR-56: A WAITING MATTER IS RE-SLOTTED (reasons-to-convene §0 line 1, RL1's re-slot step;
    # [ASSUMPTION; medium; Jordan to correct; revert: drop this loop]). No act back-fills a matter already
    # waiting: `open_case` and `carry` both decline a docketed matter, and only `open_case` fills a slot, at
    # the case's opening. So each undated person-matter (`world_q.undated_matters`, oldest first) takes the
    # open slot `world_q.slot_for` finds for it -- the same nearest-sitting walk an opening case takes --
    # the waiting item taking the slot's place and its `date`, the dateless item gone.
    # Slots open here (the ones just formed) and wherever a determination emptied one (RESOLVE). One gate
    # write per matter, `docket.formed` at the venue, chained on that venue's firing as the slot's own is.
    for item in world_q.undated_matters(w):
        slot =world_q.slot_for(w, item["matter"])
        if slot is None:
            continue
        venue = world_q.slot_venue(w, slot)
        fired = w.last_emission_of(FIRED_KIND, venue)
        w.write("DocketItem", token,
                lambda item=item, slot=slot: _reslot(w, item, slot),
                record_kind="DocketItem", fieldname="matter", driver="Event",
                emits="docket.formed", subject=venue,
                causes=[fired] if fired else [ROOT])
    TRACE.step("CALENDAR", "leave")
    return w.log[_mark:]
