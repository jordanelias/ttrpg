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
        'pred': lambda name, w: w['head'] in ('point', 'cut_thrust'),
        'needs': "a thrusting point (point head, or a cut-and-thrust blade that can half-sword to one)",
    },
    'percussive_blow': {
        'node': 'closed.coupling / armour-defeat (blunt percussion mode)',
        'pred': lambda name, w: w['head'] == 'blunt',
        'needs': "a blunt striking head — an edge or point delivers no percussion mode",
    },
}
# NOTE the discipline: armour-defeat EFFECTIVENESS (a point's gap-precision, a blunt's percussion vs the
# armour threshold) is CONTINUOUS scaling in systems.armor_defeat_sigma, NOT a gate — a low-gap rapier or a
# low-percussion staff bounce off plate by degree, not by prohibition. Only mode/form AVAILABILITY is gated.


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
    from config import CFG
    import systems as S   # imported here (not at module scope) so the registry stays cycle-free and pure
    import core
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

    # (b) gap_thrust predicate matches core.coupling's puncture availability (point or cut_thrust)
    b_ok = True
    for n in names:
        head = WEAPONS[n]['head']
        puncture_capable = (core.HEAD_MODE.get(head) == 'puncture') or head == 'cut_thrust'  # cut_thrust = max(shear,puncture)
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

    print("\n" + markdown_table())
    print("\n" + rule)
    bad = [i for i, ok in enumerate(checks) if not ok]
    if bad:
        print(f"RESULT: FAIL — checks failing: {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS — all {len(checks)} affordance gates match live engine behavior.")
