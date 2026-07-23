"""ability_primitives.py — the ABILITY PRIMITIVES: the atomic, learnable units a tradition is built from.

The atoms half of the tradition split (the traditions DICTIONARY that aggregates them is traditions.py). "Abilities
are basically tradition primitives" (Jordan): just as a weapon is a bundle of physical primitives, a tradition is a
bundle of ability primitives — the named techniques/concepts it teaches (Indes, Winden, mezzo tempo, atajo,
sen-no-sen, true-times…), grounded in the historical-combat-manuals corpus.

CURRENT MODEL (levels-of-investment, ED-PC-0023 — Jordan directive "we'll probably have levels of investment for
techniques"): an ability is a tradition-learned MODULATOR a fighter INVESTS IN. `c.equipped` is either a LIST of
names (each at level 1.0 — full baseline mastery, back-compat) or a DICT {name: level} (graded investment, level>=0).
Each ability targets a named LEVER with op '+' (additive, scaled value*level) or '*' (multiplicative, value**level).
Level 0 -> inert (invariant-safe); efficacy EMERGES from the invested level, not tradition membership — the
tradition gates ACCESS to the kit, investment + skill drive efficacy (the design principle recorded in
audit/2026-07-23-combat-fiat-audit/fiat_audit_v1.md). This realises the old TARGET MODEL's "effectiveness emerges
rather than a hand-set value": the per-ability `value` is now the level-1 anchor of a continuum, not a fixed effect.

LEVER STATUS: the 7 channel levers + counter_success/counter_select/anti_overcommit are live (eff_cw consumed at
~9 sites). U10/ED-PC-0022 added FIVE morphology-lever channels — 'edge_read', 'spine_press', 'edge_grab',
'choke_control', 'facing_regime' — consumed at the six U3/U5/U7 lever sites (combat_systems.legibility ×2 /
bind_sigma / facing_target, contact.grab_sigma). Four are populated (shinogi/zwerchhau/ringen_am_schwert/guardia; ILLUSTRATIVE — per-event effect, ~0 aggregate, see the block below);
'choke_control' has the SURFACE (the ability_factor hook is live) but no ability yet — a deliberate honest gap: no
pole/staff tradition in the roster has treatise grounding I would assert, so the channel waits for grounded content
rather than inventing it. The 'seize' lever is DEAD (its pre-contact consumer was cut 2026-06-05): vorschlag/sen_no_sen
do nothing when equipped — slated for retire-or-reroute (Phase 4 / Jordan's call).
"""

ABILITIES = {
    # German (Liechtenauer; S1/S2)
    'indes':          dict(tradition='german',   grade='S1/S2', lever='counter_success', op='+', value=0.15,
                           desc="Indes / Fühlen — feeling the bind, the simultaneous counter in the same tempo"),
    'staerke_schwaeche': dict(tradition='german', grade='S1/S2', lever='leverage',       op='*', value=1.20,
                           desc="Stärke-Schwäche — strong/weak leverage in the bind (channel lever)"),
    # Italian (Fiore -> rapier; S2)
    'mezzo_tempo':    dict(tradition='italian',  grade='S2',    lever='counter_select',  op='*', value=1.40,
                           desc="Mezzo tempo — the half-time counterattack; reaches for the in-tempo counter more readily"),
    'misura':         dict(tradition='italian',  grade='S2',    lever='measure',         op='*', value=1.15,
                           desc="Misura — distance / measure control (channel lever)"),
    # English (Silver; S2)
    'true_times':     dict(tradition='english',  grade='S2',    lever='anti_overcommit', op='+', value=0.25,
                           desc="True Times — Silver's true-vs-false times: commitment discipline, fewer over-commits"),
    # Iberian Destreza (S2/S3 — partly reliable; flagged)
    'atajo':          dict(tradition='spanish',  grade='S2/S3', lever='measure',         op='*', value=1.18,
                           desc="Atajo — Destreza blade-constraint / measure off the círculo (channel lever; S2/S3)"),
    # ── U10/ED-PC-0022 MORPHOLOGY-LEVER modulators — the tradition surface the six U3/U5/U7 levers lacked.
    # HONESTY (ED-PC-0023 adversarial review): these are ILLUSTRATIVE seed content for the surface, NOT a proven
    # balance feature. The adversarial balance pass showed the abilities' AGGREGATE win-rate edge is ~0 once
    # isolated from tradition membership (the earlier "+2.8pp" was a tradition-membership CONFOUND); their effect is
    # PER-EVENT (a bind won, a grab de-hazarded), which aggregate winrate cannot see — exactly the situational nature
    # U9 identified. The `value` multipliers are all `[SIM-CALIBRATE]` (no treatise assigns a numeric coefficient) —
    # tagged here to match the honesty of config.py's baseline K's. Each is mapped to a lever the tradition's real
    # specialisation FITS (grounding-corrected from the first cut, which wired German `winden` — a double-edged
    # LONGSWORD technique — onto the single-edge-only spine lever, where it was inert for its own weapon). The surface
    # is tradition-AGNOSTIC; more traditions gain grounded abilities as authored (not privileged by construction).
    'shinogi':        dict(tradition='japanese', grade='S2',    lever='spine_press',     op='*', value=1.6,   # [SIM-CALIBRATE]
                           desc="Shinogi — pressing/binding along the single-edged blade's ridge-and-spine (shinogi/mune) to dominate the bind's bearing surface. Grounded to the tradition whose weapon (katana) actually HAS a spine — the physical prerequisite spine() encodes; [provisional grounding — kenjutsu shinogi-receiving, SIM-CALIBRATE value]. Amplifies BIND_SPINE."),
    'zwerchhau':      dict(tradition='german',   grade='S1/S2', lever='edge_read',       op='*', value=1.6,   # [SIM-CALIBRATE]
                           desc="Zwerchhau — the Thwart-cut driven with the SHORT/false edge: weaponizes the double/false-edge return-line ambiguity to attack unread (Liechtenauer; amplifies LEGIB_EDGELINE)"),
    'ringen_am_schwert': dict(tradition='german', grade='S1/S2', lever='edge_grab',      op='*', value=0.4,   # [SIM-CALIBRATE]
                           desc="Ringen am Schwert — wrestling at the sword: a trained grappler seizes the strong/bind of a live blade with far less self-injury (a MITIGATOR, factor<1 on GRAB_EDGE self-hazard)"),
    'guardia':        dict(tradition='italian',  grade='S2',    lever='facing_regime',   op='*', value=1.5,   # [SIM-CALIBRATE]
                           desc="Guardia stretta — the Italian single-time strong-side PROFILE (Capoferro/Fabris fight markedly side-on, vs the German square-on), committing the facing regime harder; amplifies FACING_REGIME. [weak grounding — a stance emphasis, not a discrete named technique]"),
}


# THE BUNDLE, made explicit: validate every ability's tradition tag (catch typos at import) and build the forward
# index "what does tradition T grant?". This is the data-level realisation of "a tradition is a bundle of ability
# primitives" — TRADITION_KIT['german'] -> ['indes', 'staerke_schwaeche', ...]. One-way import (traditions has no
# dependency on this module), so no cycle.
from traditions import TRADITIONS as _TRADITIONS
for _name, _a in ABILITIES.items():
    assert _a['tradition'] in _TRADITIONS, f"ability {_name!r} tags unknown tradition {_a['tradition']!r}"
TRADITION_KIT = {t: [a for a, d in ABILITIES.items() if d['tradition'] == t] for t in _TRADITIONS}


def kit(trad):
    """The list of ability primitives a tradition teaches (its bundle). Empty for 'none'/untrained."""
    return TRADITION_KIT.get(trad, [])


# Investment scale is BOUNDED (ED-PC-0024 adversarial-review fix): an unbounded level made value**level overflow the
# downstream 1/(1+exp(-x)) sigmoids (bind_dominance_p / read_contest / grab_outcome) and CRASH fight resolution at a
# plausible deep-investment level (~15-22). MAX_INVESTMENT_LEVEL caps the per-technique investment (a character-gen /
# XP layer will bound it too — this is the engine's own safety floor); ABIL_FACTOR_{FLOOR,CEIL} additionally clamp the
# COMPOSED multiplicative factor so even several abilities stacked on one lever at max level cannot overflow (or a
# mitigator underflow to exactly 0.0). The clamps sit FAR above/below any sane use (level 8 shinogi=1.6**8≈43 << CEIL;
# ringen 0.4**8≈6.5e-4 > FLOOR), so they guard pathology only — graded behaviour at sane levels is unchanged.
MAX_INVESTMENT_LEVEL = 8.0
ABIL_FACTOR_FLOOR = 1e-4
ABIL_FACTOR_CEIL = 1e3


def _invested(c):
    """Yield (ability_name, level) over the fighter's LEARNED techniques — the levels-of-investment model
    (ED-PC-0024, Jordan directive "we'll probably have levels of investment for techniques"; efficacy emerges from
    what the fighter INVESTED, not tradition membership). `c.equipped` supports either:
      · a LIST of names        -> each at level 1.0 (full baseline mastery) — BACK-COMPAT, byte-identical to before;
      · a DICT {name: level}   -> graded investment (level in [0, MAX_INVESTMENT_LEVEL]; 0 = untrained/inert).
    Level is clamped to [0, MAX_INVESTMENT_LEVEL] (bounded scale; also the overflow safety guard). Pure."""
    eq = getattr(c, 'equipped', ()) or ()
    if isinstance(eq, dict):
        for name, lvl in eq.items():
            yield name, min(MAX_INVESTMENT_LEVEL, max(0.0, float(lvl)))
    else:
        for name in eq:
            yield name, 1.0


def ability_bonus(c, lever):
    """Sum of ADDITIVE ('+') modulations for `lever`, each SCALED BY the invested level (value*level). Default 0.0.
    Level 0 -> 0 (inert); level 1 -> value (baseline); deeper investment adds proportionally."""
    tot = 0.0
    for name, lvl in _invested(c):
        a = ABILITIES.get(name)
        if a and a['lever'] == lever and a['op'] == '+':
            tot += a['value'] * lvl
    return tot


def ability_factor(c, lever):
    """Product of MULTIPLICATIVE ('*') modulations for `lever`, each RAISED TO the invested level (value**level).
    Default 1.0. Level 0 -> 1.0 (inert); level 1 -> value (baseline); deeper investment COMPOUNDS — an amplifier
    (value>1) grows, a mitigator (value<1) approaches 0 — and value**level never crosses sign or goes negative, the
    correct graded form for BOTH (unlike a linear 1+level*(value-1), which would drive a mitigator negative). The
    tradition gates ACCESS to the technique; the invested level drives its EFFICACY."""
    f = 1.0
    for name, lvl in _invested(c):
        a = ABILITIES.get(name)
        if a and a['lever'] == lever and a['op'] == '*':
            f *= a['value'] ** lvl
    return min(ABIL_FACTOR_CEIL, max(ABIL_FACTOR_FLOOR, f))   # bound the composed factor (overflow/underflow guard; far from any sane level, guards pathology only)


def eff_cw(c, channel):
    """Effective lever modulator for `channel`. The scalar channel WEIGHTS are removed: only a learned ABILITY hooked
    to that lever (ability_factor) moves this off 1.0. With no such ability — the default — this is exactly 1.0, so
    the channel has no intrinsic effect and traditions differ only via the imposition gate + familiarity. (Name kept
    so call-sites read as the lever they modulate; an authored ability on e.g. 'measure' goes live here.)"""
    return ability_factor(c, channel)
