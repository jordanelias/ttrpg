"""
ED-912 regression: knots.py runs the bidirectional -5..+5 bond-strain gauge (C-TW-12).

WHY THIS EXISTS
---------------
ED-912 (ruled 2026-06-28) reframed the Knot tier model onto a bidirectional -5..+5 gauge and
struck the pre-ED-912 one-way 0->capacity accumulator (TIER_CAPACITY {Distant:4, Close:7}, PP-632).
The doc side propagated 2026-07-07 (knots_v30 §6 + fieldwork_v30 §5.6b); the audit (C-TW-12) found
systems/fieldwork/sim/knots.py still ran the struck model with ZERO test coverage. This pins the rebuild:

  - Distant strain range -2..+5 (start 0); Close range -5..+5 (start -2)
  - rupture/break at +5 (the wear-direction ceiling, both tiers)
  - -5 = Tempered (Close only): absorbs the next rupture trigger once, resetting strain to 0
  - break/betrayal-rupture Disposition -3 (revised from -4), floor -5
  - a Close Knot that broke from POSITIVE strain -> Conviction Scar +1

knots/ is an island (no campaign callers), so the F7 + seed-0 campaign goldens are unaffected.
"""
import os
import sys
import random

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

import systems.fieldwork.sim.knots as knots  # noqa: E402


class _FormActor:
    """Duck-typed actor for form_knot prerequisites (§3.1)."""

    def __init__(self, bonds=6, spirit=5, history_relationships=6, ts=40, disposition=6):
        self.bonds = bonds
        self.spirit = spirit
        self.history_relationships = history_relationships
        self.ts = ts
        self.disposition = disposition


def _make(tier, strain, disposition=6, knot_id="KTEST"):
    """Insert a Knot directly into the module store (bypasses form_knot's roll)."""
    knots.reset_knots()
    k = knots.Knot(knot_id=knot_id, actor_a="A", actor_b="B", tier=tier,
                   strain=strain, disposition=disposition)
    knots._knots[knot_id] = k
    return k


def test_ed912_formation_starts_at_tier_gauge_start():
    """A formed Knot starts at its tier's gauge start (Distant 0, Close -2), not 0-for-all."""
    formed = 0
    for seed in range(80):
        knots.reset_knots()
        k = knots.form_knot("A", "B", actor_a_obj=_FormActor(), actor_b_obj=_FormActor(),
                            rng=random.Random(seed))
        if k is not None:
            formed += 1
            assert k.strain == knots.TIER_START[k.tier], (
                f"{k.tier} knot started at strain {k.strain}, expected {knots.TIER_START[k.tier]}"
            )
    assert formed, "no knots formed across seeds — check _FormActor prerequisites"


def test_ed912_sustain_clamps_to_tier_range():
    """Decay floors at the tier minimum (-2 Distant / -5 Close), not 0."""
    _make("Distant", 0)
    st = knots.sustain_knot("KTEST", strain_delta=-10)
    assert st.strain_after == -2 and not st.broke, f"Distant floored wrong: {st.strain_after}"
    _make("Close", -2)
    st = knots.sustain_knot("KTEST", strain_delta=-10)
    assert st.strain_after == -5 and not st.broke, f"Close floored wrong: {st.strain_after}"


def test_ed912_sustain_breaks_at_plus5_both_tiers():
    for tier in ("Distant", "Close"):
        _make(tier, 0)
        st = knots.sustain_knot("KTEST", strain_delta=5)
        assert st.strain_after == 5 and st.broke and not st.knot.active, (
            f"{tier} did not break at +5: {st.strain_after}, broke={st.broke}"
        )


def test_ed912_tempered_close_absorbs_first_rupture_then_ruptures():
    """A Close knot at -5 (Tempered) absorbs the first rupture trigger (reset to 0), then ruptures."""
    _make("Close", -5)
    st1 = knots.check_knot_rupture("KTEST", "public_citation")
    assert not st1.ruptured and st1.knot.active and st1.strain_after == 0, (
        f"Tempered should absorb + reset to 0: ruptured={st1.ruptured}, strain={st1.strain_after}"
    )
    st2 = knots.check_knot_rupture("KTEST", "public_citation")
    assert st2.ruptured and not st2.knot.active, "second trigger should rupture (Tempered spent)"


def test_ed912_non_tempered_close_and_distant_rupture_immediately():
    _make("Close", 0)
    assert knots.check_knot_rupture("KTEST", "partner_death").ruptured
    # Distant floor is -2, so it can never be Tempered (-5) — a trigger always ruptures.
    _make("Distant", -2)
    assert knots.check_knot_rupture("KTEST", "fr_dissolution").ruptured


def test_ed912_break_disposition_minus3_and_positive_strain_close_scar():
    # Close broke from POSITIVE strain (reached +5) -> Scar; Disposition -3; 4 Composure.
    _make("Close", 5)
    c = knots.apply_knot_loss("A", "KTEST", mode="break")
    assert c["composure_damage"] == 4
    assert c["disposition_set_to"] == -3
    assert c["conviction_scar"] == 1
    # Close at non-positive strain -> no Scar (branch guard).
    _make("Close", -3, knot_id="KNEG")
    assert knots.apply_knot_loss("A", "KNEG", mode="break")["conviction_scar"] is None
    # Distant break -> never a Scar; still Disposition -3.
    _make("Distant", 5, knot_id="KDIST")
    c3 = knots.apply_knot_loss("A", "KDIST", mode="break")
    assert c3["conviction_scar"] is None and c3["disposition_set_to"] == -3


def test_ed912_rupture_disposition_minus3_and_coherence():
    _make("Close", 3)
    c = knots.apply_knot_loss("A", "KTEST", mode="rupture")
    assert c["disposition_set_to"] == -3, f"betrayal-rupture Disposition should be -3, got {c['disposition_set_to']}"
    assert c["coherence_delta"] == -1  # [UNVERIFIED post-ED-912] — matches the doc's retained value
