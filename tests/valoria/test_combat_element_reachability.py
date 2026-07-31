"""AUTHORED ELEMENTS MUST BE REACHABLE — E2b guards (M9/F6, ED-PC-0048).

DEFECT (verified red on the pre-fix tree): `weapon_physics.percussion_element_authority` derived its
lever as `abs(elem_x) / Lt` — the element's offset from the working hand as a fraction of the
weapon's length. That returns EXACTLY 0 for any element mounted AT the hand, so the authority is 0,
so the affordance gate never emits the token, so the element can never be selected:

    hook_sword  authored mode_elements = {curved_cut, blunt}   afforded_heads = {curved_cut, point}
                the authored crescent (element_ref 1, mass 0.140 kg, x = +0.000 m) -> authority 0.0000

This is the SECOND FACE of the M1/F1 defect E2a repaired at the weapon scale: a lever form that can
be exactly zero. The repair routes this consumer through the single owner E2a shipped,
`weapon_physics.strike_point_lever`, so the two scales cannot carry two different lever forms
(review R-11.4).

THE GUARD IS PER-TOKEN, NOT PER-ELEMENT (review R-11.1), and the distinction is the whole point.
`afforded_heads` returns a token -> best-element map, so when a weapon carries two elements sharing a
token, only one wins the union — CORRECTLY. Four weapons do this (`poleaxe` blunt+point+point,
`bec_de_corbin` blunt+point+point, `lucerne_hammer` blunt+blunt+point, `kama_yari`
point+curved_cut+curved_cut). A per-element guard flags all four as broken; the per-token guard
flags only `hook_sword`, which is the actual defect. `test_the_guard_is_per_token_not_per_element`
pins that distinction directly, so a future rewrite to the per-element form fails here rather than
silently indicting four correct weapons.

FALSIFIERS (CLAUDE.md §0.1 point 3) — mutations run against these guards, each naming its target:
  · revert the lever to `abs(elem_x) / Lt`                  -> guard 1 red, naming hook_sword/blunt.
  · route through `strike_point_lever(w, elem_mass, ...)`   -> guard 3 red (see its own docstring:
    that is the call signature E2a's docstring PRESCRIBED, and it double-counts mass).
  · rewrite guard 1 per-element instead of per-token        -> guard 2 red, naming all four
    multi-element weapons.
"""
import math
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S      # noqa: E402
import combatant as C          # noqa: E402
import vocabulary as V         # noqa: E402
import weapon_physics as WP    # noqa: E402


def _authored_tokens(w):
    """The head token of every authored `mode_element` — what the weapon record CLAIMS it can do."""
    return {el['head'] for el in (w.get('mode_elements') or [])}


def test_every_authored_element_token_is_reachable():
    """GUARD 1 (the defect pin). Every token a weapon's `mode_elements` authors must appear in
    `afforded_heads` for at least one legal configuration — otherwise the authoring is dead data.

    RED ON THE PRE-FIX TREE at exactly one weapon: hook_sword's authored `blunt` crescent, absent
    from `afforded_heads` = {curved_cut, point} because its x = 0.000 m zeroed the lever."""
    unreachable = {}
    for name, w in C.WEAPONS.items():
        authored = _authored_tokens(w)
        if not authored:
            continue
        # "at least one legal configuration": the affordance gate is grip/room-threaded, so a token
        # counts as reachable if ANY legal grip/room combination affords it.
        reachable = set()
        for grip in (0.0, 0.5, 1.0):
            for room in (0.35, 1.0):
                reachable |= set(S.afforded_heads(w, grip=grip, room=room).keys())
        missing = authored - reachable
        if missing:
            unreachable[name] = sorted(missing)
    assert not unreachable, (
        "authored mode_element tokens that no legal configuration can afford — the element is dead "
        f"data: {unreachable}. Mutation that produces this: reverting "
        "percussion_element_authority's lever to `abs(elem_x)/Lt`, which returns 0 for any element "
        "mounted at the working hand (hook_sword's crescent)."
    )


def test_the_guard_is_per_token_not_per_element():
    """GUARD 2 (the guard's own scope pin, review R-11.1). Four weapons legitimately carry two
    elements sharing one token; only one wins the token -> element union, which is correct. This
    test asserts those four exist and are NOT flagged, so a future rewrite of guard 1 into the
    per-element form fails HERE rather than quietly indicting four correct weapons."""
    shared_token_weapons = {}
    for name, w in C.WEAPONS.items():
        tokens = [el['head'] for el in (w.get('mode_elements') or [])]
        dupes = {t for t in tokens if tokens.count(t) > 1}
        if dupes:
            shared_token_weapons[name] = sorted(dupes)
    assert set(shared_token_weapons) == {'poleaxe', 'bec_de_corbin', 'lucerne_hammer', 'kama_yari'}, (
        "the population of multi-element-sharing-a-token weapons changed: "
        f"{shared_token_weapons}. Guard 1 must stay PER-TOKEN — a per-element form flags every one "
        "of these as broken when none of them is."
    )
    # and each is fully afforded, i.e. guard 1's per-token form passes them
    for name in shared_token_weapons:
        w = C.WEAPONS[name]
        assert not (_authored_tokens(w) - set(S.afforded_heads(w).keys())), (
            f"{name} is flagged by guard 1 despite sharing a token legitimately — guard 1 has been "
            "rewritten per-element."
        )


def test_element_lever_does_not_double_count_mass():
    """GUARD 3 (the form pin — the review-R-11.4 trap E2a's own docstring walked into).

    E2a prescribed `sqrt(elem_mass) * strike_point_lever(w, elem_mass, elem_x)` for this consumer.
    That call signature double-counts the striking mass: `strike_point_lever`'s first argument is a
    mass that it divides by the weapon's total, so mass would enter at power 1.5 AND be normalised
    by the whole weapon — dropping percussion 19-37% across all 53 weapons, a roster-wide balance
    change inside a batch labelled 'no balance intent'.

    The element's own mass belongs in `sqrt()`, where it always was; the LEVER is geometric. Calling
    the same single owner with the delivered mass yields exactly that geometric lever,
    `(STRIKE_HAND_LEVER + |x|) / (STRIKE_HAND_LEVER + Lt)` — one owner, no third form.

    This pin is a scale invariant an epsilon cannot satisfy: the lever must be INDEPENDENT of the
    striking element's mass."""
    w = C.WEAPONS['poleaxe']
    a_light = WP.percussion_element_authority(w, 0.20, 0.60)
    a_heavy = WP.percussion_element_authority(w, 0.80, 0.60)
    # authority itself must rise with mass (sqrt term), ...
    assert a_heavy > a_light, "element authority must still rise with the striking mass"
    # ... but the ratio must be the pure sqrt-and-exponent ratio, with NO extra mass factor from the
    # lever. Double-counting mass in the lever would make this ratio (4**1.5)**PERC_EXP, not
    # (4**0.5)**PERC_EXP.
    expected = (math.sqrt(0.80 / 0.20)) ** WP.PERC_EXP
    doubled = ((0.80 / 0.20) ** 1.5) ** WP.PERC_EXP
    got = a_heavy / a_light
    assert abs(got - expected) < 1e-9, (
        f"element-authority mass ratio {got:.6f} != {expected:.6f}; the lever is carrying a mass "
        f"term it must not ({doubled:.6f} is the double-counted value). Mutation that produces "
        "this: routing through strike_point_lever(w, elem_mass, elem_x) — the signature E2a's "
        "docstring prescribed — instead of strike_point_lever(w, delivered_strike(w)[2], elem_x)."
    )


def test_hook_sword_crescent_is_the_worked_example():
    """GUARD 4 (the named instance, asserted THROUGH the consumer). The defect was reported against
    hook_sword specifically; pin it by name so a general fix that happens to miss this weapon is
    still caught. Asserted through `afforded_heads` — the gate that actually decides selectability —
    not through the physics function alone."""
    w = C.WEAPONS['hook_sword']
    crescent = [el for el in w['mode_elements'] if el['head'] == V.HEAD_BLUNT]
    assert len(crescent) == 1, "hook_sword's authored crescent is gone — this guard's premise moved"
    em, ex = S._element_mass_x(w, crescent[0])
    assert abs(ex) < 1e-12, (
        f"hook_sword's crescent is no longer mounted at the hand (x={ex}); it was x=0.000 m, which "
        "is precisely why the `abs(x)/Lt` lever zeroed it. This guard no longer observes M9/F6."
    )
    assert WP.percussion_element_authority(w, em, ex) > 0.0, (
        "a strike delivered AT the working hand derives zero authority — the M9/F6 lever defect is "
        "back. A hand-mounted crescent swings on the hand/hilt's own lever, not on nothing."
    )
    assert V.HEAD_BLUNT in S.afforded_heads(w), (
        "hook_sword's authored crescent is still unreachable: afforded_heads = "
        f"{sorted(S.afforded_heads(w))}. The physics may be fixed while the affordance gate is not."
    )
