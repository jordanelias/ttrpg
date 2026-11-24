"""B10.63 -- A RIVAL'S REPORT IS DISCOUNTED AS INTERESTED (`H-180`; `02_CHAR_relations_have_a_ground` edit 5).

`teller_weight` multiplies a told claim's weight by `1 - rival_gain` when the HEARER holds the teller's own `bond:rivalry` claim on the claim's
subject, told to him. Planted on `probes.tiny_world`: the claim is planted, so the six relation rows the shipped registry authors since BA1.08 do not enter."""
from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..decision.options import teller_weight
from ..harness import probes as P
from ..queries.person_q import BOND_STEM
from ..state.carriers import Claim


def _told(cid, subject, teller, *, predicate="stores:grain", value=5):
    return Claim(cid, "p_low", subject, predicate, value, 2, "told_by", 100, "own", chain=(teller,))


def test_a_rivals_report_weighs_less_than_a_strangers():
    """`p_low` holds a `bond:rivalry` claim on `p_other` that `p_mid` told him (`p_mid`'s own bond, chain origin `p_mid`). A claim on `p_other` told by
    `p_mid` weighs `1 - rival_gain` of what it weighs at the control; the same teller on `p_king`, a different teller (`p_high`) on `p_other`, and a
    claim on `p_king` told by `p_mid` while `p_low` holds a rivalry bond of HIS OWN on `p_king` (no chain) each weigh as they do at gain 0.
    FALSIFIER: the factor reads nothing -- the rival's claim weighs what a stranger's does."""
    p = P.tiny_world().persons["p_low"]
    p.ledger[:] = [
        _told("b_rival", "p_other", "p_mid", predicate=BOND_STEM + "rivalry", value=True),
        Claim("b_own", "p_low", "p_king", BOND_STEM + "rivalry", True, 0, "firsthand", 100, "own"),
        _told("c_rival", "p_other", "p_mid"),
        _told("c_other_teller", "p_other", "p_high"),
        _told("c_other_subject", "p_king", "p_mid"),
    ]
    live = teller_weight(p, DEFAULT_FIXTURES.sweep("rival_gain", 0.5).sweep("record_gain", 0.0))
    control = teller_weight(p, DEFAULT_FIXTURES.sweep("rival_gain", 0.0).sweep("record_gain", 0.0))
    by_id = {c.id: c for c in p.ledger}
    base = control(by_id["c_rival"])
    assert 0.0 < base < 1.0, base
    assert live(by_id["c_rival"]) == base * 0.5, (live(by_id["c_rival"]), base)
    checked = 0
    for cid in ("c_other_teller", "c_other_subject", "c_rival"):
        want = control(by_id[cid]) * (0.5 if cid == "c_rival" else 1.0)
        assert live(by_id[cid]) == want, (cid, live(by_id[cid]), want)
        checked += 1
    assert checked == 3
    # and the discount is the gain's: at 1.0 the rival's report weighs nothing, a stranger's is untouched
    full = teller_weight(p, DEFAULT_FIXTURES.sweep("rival_gain", 1.0).sweep("record_gain", 0.0))
    assert full(by_id["c_rival"]) == 0.0 and full(by_id["c_other_subject"]) == control(by_id["c_other_subject"])
