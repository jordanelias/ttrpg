"""capabilities.py — the weapon-morphology affordance gates, as one source (scene-combat WS-2 / req 5).

"Clearly indicate moments in the state graph for applicable vs non-applicable weapon morphologies" — you
cannot half-sword without a sword, gap-thrust without a point, or deliver a percussive blow without a blunt
head. (Armour-defeat EFFECTIVENESS is continuous, not gated — see the registry note.) The engine
already ENFORCES these through its physics (systems.halfsword_target, core.coupling, systems.armor_defeat_sigma);
this module makes them EXPLICIT and single-source, verifies each predicate against the live engine behavior,
and generates the capability x weapon table for the state-graph annotation.

Discipline (per the 06-13 consolidated-master): only TRUE affordance gates are hard here — everything else
(blade_guard -> bind quality, mass -> heft) is continuous scaling, not a gate. Each capability names the
state-graph node it gates, so the table reads as "which technique each weapon can even attempt, and where."
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from combatant import WEAPONS, HALFSWORD_FORM, HALFSWORD_BASE   # pure data; no systems/core at module scope (cycle-free)
from config import CFG   # pure data (GRAB_SHORT_REACH_LU); no cycle risk

def _affords_point(w):
    """Local import (systems.py sits above this module in the dependency order — importing it at module
    scope would create a cycle, per the module docstring's "pure data; no systems/core at module scope").
    True iff the weapon's DERIVED afforded-heads set (systems.afforded_heads — primitive-emergent, not the
    static `head` field) includes a real 'point' token. Catches the poleaxe: its static head is 'blunt', but
    its spike mode_element (an explicit point-tokened striking element, morphology-rearch Phase B2) affords a
    genuine point, and systems.select_mode already lets it SELECT that spike vs plate armour at runtime (the
    situational gap game) — so the static-head-only check under-reports this capability for it."""
    import systems as S
    return 'point' in S.afforded_heads(w)


# Each capability: the state-graph node it gates, a pure predicate over (name, weapon-dict), and the human
# "needs" string. Predicates are seeded to match current engine behavior exactly (verified in __main__).
CAPABILITIES = {
    'halfsword': {
        'node': 'closed.form_switch (systems.halfsword_target)',
        'pred': lambda name, w: name in HALFSWORD_FORM or name in HALFSWORD_BASE,
        'needs': "a long rigid blade you can grip mid-stave — high cross_section, sufficient blade length, a hilt that doesn't block the mid-blade grip",
    },
    'gap_thrust': {
        'node': 'closed.coupling / armour-defeat (core.coupling puncture path)',
        'pred': lambda name, w: w['head'] in ('point', 'cut_thrust') or _affords_point(w),
        'needs': "a thrusting point (point head, or a cut-and-thrust blade that can half-sword to one), or a blunt weapon whose beak/spike affords a real point (e.g. the poleaxe)",
    },
    'percussive_blow': {
        'node': 'closed.coupling / armour-defeat (blunt percussion mode)',
        'pred': lambda name, w: w['head'] == 'blunt',
        'needs': "a blunt striking head — an edge or point delivers no percussion mode",
    },
    'open_contact': {
        'node': 'Contact (contact.grab_available)',
        'pred': lambda name, w: w['head_len'] <= CFG['GRAB_SHORT_REACH_LU'],
        'needs': "a short enough head_len (dagger/unarmed-class) to already be functionally at grapple range — every other weapon needs a real prior opening this beat (bind / beaten-aside / deep-commit) before a grab is available",
    },
}
# NOTE the discipline: armour-defeat EFFECTIVENESS (a point's gap-precision, a blunt's percussion vs the
# armour threshold) is CONTINUOUS scaling in systems.armor_defeat_sigma, NOT a gate — a low-gap rapier or a
# low-percussion staff bounce off plate by degree, not by prohibition. Only mode/form AVAILABILITY is gated.
# `open_contact` is the ONE static morphology fact the contact axis (I7b, D8/D9) gates: whether a weapon needs
# an opening at all before a grab. disarm/throw/pin/control/foot_pin/escape are NOT separate gates — they are
# branches of the universal contact.grab_outcome menu, reachable for every weapon once contact.grab_available
# is True (no morphology excludes any weapon from EVER ending up in contact — only from open-contact grabbing
# without an opening first).


def allowed(key, name):
    """May the weapon `name` attempt the capability `key`? Pure morphology gate."""
    return bool(CAPABILITIES[key]['pred'](name, WEAPONS[name]))


def capability_table():
    """{weapon: {capability: bool}} for every weapon in the roster (auto-form half-sword excluded as a base)."""
    names = [n for n, rec in WEAPONS.items() if 'base' not in rec]   # exclude auto-switched FORMS (records carrying a `base`), never a named weapon
    return {n: {k: allowed(k, n) for k in CAPABILITIES} for n in names}


def markdown_table():
    tbl = capability_table()
    caps = list(CAPABILITIES)
    out = ["### Weapon-morphology affordance gates (applicable = yes; the engine enforces these via physics)",
           "| weapon | head | " + " | ".join(caps) + " |",
           "|---|---|" + "|".join(["---"] * len(caps)) + "|"]
    for n, row in tbl.items():
        cells = " | ".join("yes" if row[c] else "—" for c in caps)
        out.append(f"| {n} | {WEAPONS[n]['head']} | {cells} |")
    out.append("")
    for k, v in CAPABILITIES.items():
        out.append(f"- **{k}** @ `{v['node']}` — needs {v['needs']}")
    return "\n".join(out)


# ============================== self-test: predicates must match LIVE engine behavior ==============================
if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    from combatant import Combatant
    import systems as S   # imported here (not at module scope) so the registry stays cycle-free and pure
    import core
    import contact as CT
    checks, rule = [], '=' * 64
    print("capabilities.py — affordance gates verified against the live engine"); print(rule)

    names = [n for n, rec in WEAPONS.items() if 'base' not in rec]   # exclude auto-switched FORMS (records carrying a `base`), never a named weapon

    # (a) halfsword predicate matches systems.halfsword_target (does the form actually switch?)
    a_ok = True
    for n in names:
        c = Combatant('x', weapon=n)
        switches = S.halfsword_target(c, True, 'heavy') != n
        if switches != allowed('halfsword', n):
            a_ok = False; print(f"    MISMATCH halfsword {n}: engine={switches} pred={allowed('halfsword', n)}")
    checks.append(a_ok); print(f"(a) halfsword pred == halfsword_target switch: {'OK' if a_ok else 'FAIL'}")

    # (b) gap_thrust predicate matches core.coupling's puncture availability (point or cut_thrust), OR the
    # DERIVED afforded_heads set (catches the poleaxe's emergent beak/spike point — see _affords_point)
    b_ok = True
    for n in names:
        head = WEAPONS[n]['head']
        puncture_capable = (core.HEAD_MODE.get(head) == 'puncture') or head == 'cut_thrust' or 'point' in S.afforded_heads(WEAPONS[n])  # cut_thrust = max(shear,puncture)
        if puncture_capable != allowed('gap_thrust', n):
            b_ok = False; print(f"    MISMATCH gap_thrust {n}: engine={puncture_capable} pred={allowed('gap_thrust', n)}")
    checks.append(b_ok); print(f"(b) gap_thrust pred == coupling puncture path: {'OK' if b_ok else 'FAIL'}")

    # (c) percussive_blow predicate matches the engine's percussion mode: a blunt head, and only a blunt head,
    # delivers core.HEAD_MODE 'percussion'. (Armour-defeat EFFECTIVENESS is continuous, not gated — see the note
    # in the registry; a low-percussion staff bounces off plate by degree, not prohibition.)
    c_ok = True
    for n in names:
        head = WEAPONS[n]['head']
        percussion_mode = (core.HEAD_MODE.get(head) == 'percussion')
        if percussion_mode != allowed('percussive_blow', n):
            c_ok = False; print(f"    MISMATCH percussive_blow {n}: engine={percussion_mode} pred={allowed('percussive_blow', n)}")
    checks.append(c_ok); print(f"(c) percussive_blow pred == coupling percussion mode: {'OK' if c_ok else 'FAIL'}")

    # (d) open_contact predicate matches contact.grab_available with NO opening (opening_created=False) — the
    # exemption is the only case where the predicate is discriminating (WITH an opening every weapon is available).
    d_ok = True
    for n in names:
        c = Combatant('x', weapon=n); opp = Combatant('y', weapon='arming')
        exempt = CT.grab_available(c, opp, False, CFG)
        if exempt != allowed('open_contact', n):
            d_ok = False; print(f"    MISMATCH open_contact {n}: engine={exempt} pred={allowed('open_contact', n)}")
    checks.append(d_ok); print(f"(d) open_contact pred == grab_available(opening_created=False): {'OK' if d_ok else 'FAIL'}")

    # (e) the branching grab_outcome menu is reachable across seeds (D8 acceptance 2) — draw many times at a
    # fixed dominance edge and confirm every declared outcome token fires at least once.
    import random
    seen_outcomes = set()
    rng = random.Random(0)
    for _ in range(4000):
        seen_outcomes.add(CT.grab_outcome(rng.uniform(-1.5, 1.5), rng, CFG))
    e_ok = seen_outcomes == set(CT.GRAB_OUTCOMES)
    checks.append(e_ok)
    print(f"(e) grab_outcome menu reachable across seeds ({sorted(seen_outcomes)}): {'OK' if e_ok else 'FAIL — missing ' + str(set(CT.GRAB_OUTCOMES)-seen_outcomes)}")

    # (f) no hollow pull_capable/hook data boolean was introduced anywhere in weapons.py (the explicit guard
    # against the D9/JD-7 workaround the plan forbids — invisible to test_no_weapon_name_literal_in_resolution).
    weapons_src = open(os.path.join(os.path.dirname(__file__), 'weapons.py'), encoding='utf-8').read()
    f_ok = ('pull_capable' not in weapons_src) and ('hook_affordance' not in weapons_src) and ('clinch=' not in weapons_src)
    checks.append(f_ok)
    print(f"(f) no pull_capable/hook_affordance/clinch data field in weapons.py: {'OK' if f_ok else 'FAIL'}")

    print("\n" + markdown_table())
    print("\n" + rule)
    bad = [i for i, ok in enumerate(checks) if not ok]
    if bad:
        print(f"RESULT: FAIL — checks failing: {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS — all {len(checks)} affordance gates match live engine behavior.")
