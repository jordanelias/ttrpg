"""B10.70 -- `world_q.attention_key`, inside tier 1: an unmet need is attended first.

What each test proves, and the failure it can observe:

  `test_a_shortfall_claim_sorts_first_larger_first_in_tier_one` -- a holder with two shortfall claims
      (8 and 15) and a routine `stores.changed` claim, all about his own tenure's object (tier 1). The
      routine claim's id sorts first and the 8's before the 15's, so the pre-edit key `(1, 0.0)` answers
      them c_0, c_1, c_2 (asserted as the control); the rule answers the 15, the 8, then the routine one.
  `test_tier_two_order_is_unchanged` -- a shortfall claim the holder has no tenure over is no tier 1:
      it keeps tier 4's `0.0`, and two deed claims keep their `-|valence|` order, so the rule reaches
      tier 1 and nothing else.
"""
from __future__ import annotations

from ..data.requires import SHORTFALL_PREDICATE
from ..queries import world_q
from ..state.carriers import Tenure
from .test_in57_attention_tiers import PURSUITS, _ambitious, _claim, _deed_kinds, old_key

SHORT = f"{SHORTFALL_PREDICATE}:grain"


def test_a_shortfall_claim_sorts_first_larger_first_in_tier_one():
    p, w = _ambitious()
    p.tenures.append(Tenure("t_obj", p.id, "obj_t", "hold", 0))
    p.ledger += [_claim("c_0", p.id, "obj_t", "stores.changed", 3),
                 _claim("c_1", p.id, "obj_t", SHORT, 8),
                 _claim("c_2", p.id, "obj_t", SHORT, 15)]
    qs = world_q.questions_for(w, p)
    key = world_q.attention_key(w, p)
    assert [key(q)[0] for q in qs] == [1, 1, 1, 3], "all three claims are tier 1"
    assert [q.id for q in sorted(qs, key=old_key)][:3] == [
        "q:claim:c_0", "q:claim:c_1", "q:claim:c_2"], "control: the id order is the unranked one"
    assert [q.id for q in qs][:3] == ["q:claim:c_2", "q:claim:c_1", "q:claim:c_0"], [q.id for q in qs]


def test_tier_two_order_is_unchanged():
    p, w = _ambitious()
    p.pursuits = dict(PURSUITS)
    small, big = _deed_kinds(p.pursuits)
    p.ledger += [_claim("c_0", p.id, p.id, SHORT, 15),      # no tenure over its subject: not tier 1
                 _claim("c_1", p.id, p.id, small, True),
                 _claim("c_2", p.id, p.id, big, True)]
    qs = world_q.questions_for(w, p)
    key = world_q.attention_key(w, p)
    by_id = {q.id: key(q) for q in qs}
    assert [q.id for q in qs][:2] == ["q:claim:c_2", "q:claim:c_1"], [q.id for q in qs]
    assert by_id["q:claim:c_2"][:2] < by_id["q:claim:c_1"][:2] and by_id["q:claim:c_2"][0] == 2
    assert by_id["q:claim:c_0"][:2] == (4, 0.0), "a shortfall claim outside tier 1 carries no magnitude"
