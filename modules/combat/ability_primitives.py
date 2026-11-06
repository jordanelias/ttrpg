"""ability_primitives.py — the ABILITY PRIMITIVES: the atomic, learnable units a tradition is built from.

The atoms half of the tradition split (the traditions DICTIONARY that aggregates them is traditions.py). "Abilities
are basically tradition primitives" (Jordan): just as a weapon is a bundle of physical primitives, a tradition is a
bundle of ability primitives — the named techniques/concepts it teaches (Indes, mezzo tempo, atajo,
true-times…), grounded in the historical-combat-manuals corpus.

CURRENT MODEL (levels-of-investment, ED-PC-0024 — ED-PC-0035 citation fix: 0023 is the fiat audit that RECORDED the principle; 0024 is the entry that filed the model. Jordan directive "we'll probably have levels of investment for
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
bind_sigma / facing_target, contact.grab_sigma). TWO are populated with abilities whose grounding HELD under the
2026-07-23 adversarial HEMA pass (shinogi->spine_press, ringen_am_schwert->edge_grab; ILLUSTRATIVE — per-event
effect, ~0 aggregate, see the block below). 'edge_read' and 'choke_control' have no GROUNDED ability; since PC-17
(ED-PC-0059) they and five channel levers carry the 21 GENERIC calibration abilities built below the ABILITIES dict.
'facing_regime' stays BARE (the ability_factor hook is live, factor 1.0 default, byte-identical): a deliberate
honest gap, NOT invented privilege. ('zwerchhau' was re-homed off edge_read to counter_select
and 'guardia' removed off facing_regime — both were winden-class category errors, ED-PC-0026.) There is no 'seize' lever, and no 'vorschlag' or 'sen_no_sen' ability.
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
    'atajo':          dict(tradition='spanish',  grade='S2/S3', lever='leverage',        op='*', value=1.18,
                           desc="Atajo — Destreza OCCUPATION/interruption of the opponent's line: a blade-constraint/control action via angulation on the círculo, conceptually a bind/LEVERAGE action (analogous to German Stärke-Schwäche), NOT a distance concept — Destreza's distance runs through compás/footwork. [GROUNDING-CORRECTED 2026-07-23, ED-PC-0026: was mis-wired to 'measure'; adversarial HEMA critic — atajo is line-occupation, a leverage action. S2/S3]"),
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
    'zwerchhau':      dict(tradition='german',   grade='S1/S2', lever='counter_select',  op='*', value=1.4,   # [SIM-CALIBRATE]
                           desc="Zwerchhau — the Thwart-cut, a Liechtenauer Meisterhau: crossing the hands to form a structural 'roof' that INTERCEPTS an incoming Oberhau and strikes in the SAME TEMPO. Its documented function is tempo-interception (Ringeck / pseudo-Peter-von-Danzig glosses) — reaching for the single-time counter — NOT false-edge unreadability. [GROUNDING-CORRECTED 2026-07-23, ED-PC-0026: was mis-wired to 'edge_read' on a return-line-ambiguity claim the glosses don't give; adversarial HEMA critic. Now amplifies COUNTER_SELECT alongside Italian mezzo_tempo — the in-tempo counter reach.]"),
    'ringen_am_schwert': dict(tradition='german', grade='S1/S2', lever='edge_grab',      op='*', value=0.4,   # [SIM-CALIBRATE]
                           desc="Ringen am Schwert — wrestling at the sword: a trained grappler seizes the strong/bind of a live blade with far less self-injury (a MITIGATOR, factor<1 on GRAB_EDGE self-hazard)"),
    # 'guardia' REMOVED 2026-07-23 (ED-PC-0026, adversarial HEMA critic): it wired "guardia stretta" onto the
    # facing_regime (body side-on-vs-square) lever, but "stretta" names a NARROW blade-position / close-MEASURE
    # guard (paired with misura stretta), a different referent than body facing — the same winden-class category
    # error (real period term, wrong lever). The Italian profiled-stance TENDENCY facing_regime models is real,
    # but it has no discrete named technique to anchor an ability honestly, so facing_regime stays a BARE
    # morphology lever (fires from WP.facing_pref weapon geometry; honest-gap for a tradition amplifier, exactly
    # like choke_control was) rather than ship a misnamed one. edge_read likewise has no GROUNDED ability (zwerchhau
    # re-homed to counter_select above); it and choke_control now carry only the GENERIC calibration abilities below.
}


# THE BUNDLE, made explicit: validate every ability's tradition tag (catch typos at import) and build the forward
# index "what does tradition T grant?". This is the data-level realisation of "a tradition is a bundle of ability
# primitives" — TRADITION_KIT['german'] -> ['indes', 'staerke_schwaeche', ...]. One-way import (traditions has no
# dependency on this module), so no cycle.
from traditions import TRADITIONS as _TRADITIONS

# ── GENERIC CALIBRATION ABILITIES (PC-17, ED-PC-0059; PROVISIONAL) ────────────────────────────────────────────────
# Jordan, 2026-11-01: "a spread of generics for now so that we have more calibration data". Instruments, not
# grounded technique: plain descriptive names, no period terms (ED-PC-0026), grade 'GENERIC', every value
# [SIM-CALIBRATE]. All op '*': `ability_bonus` ('+') is read at two sites only (counter_success, anti_overcommit), so
# an additive generic on these levers would never act. Six beneficial levers at x1.10 / x1.25 / x1.50 (edge_read's
# refined tier REVISED to x1.40, see GENERIC_LEVERS); choke_control
# as a MITIGATOR at x0.90 / x0.75 / x0.55, because its site (combat_systems.legibility) ADDS the owner's gathered-pole
# telegraph to the read the OPPONENT takes, so a factor below 1 helps its owner. facing_regime stays bare (geometry,
# not this position; Jordan 2026-11-01).
# PLACEMENT is a Latin square over the seven traditions in TRADITIONS order ('none' excluded): tradition t receives
# (lever (t + k) mod 7, tier k) for k = 0, 1, 2, so each (lever, tier) pair exists in exactly one tradition and each
# tradition gains three generics on three different levers. Kit totals stay unequal; no equality is claimed.
# REVERT: delete this block (every ability with grade 'GENERIC') and their probes in
# tests/valoria/test_combat_lever_sign_safety.py. CFG['INIT_TEMPO_LEVER_K'] may STAY (with no 'tempo' ability the term
# is exactly 0); deleting the key alone raises KeyError in combat_systems.init_emphasis_sigma, so delete the key and
# that term together or not at all.
GENERIC_TIERS = ('basic', 'practiced', 'refined')   # tier k = 0, 1, 2
# (lever, name stem, what the trained fighter does, the three tier factors) — the square's lever order. [SIM-CALIBRATE]
# Beneficial levers x1.10 / x1.25 / x1.50; choke_control is a MITIGATOR (x0.90 / x0.75 / x0.55). edge_read's refined
# tier is x1.40, REVISED from the plan's x1.50 under its falsifier ("a cliff: the tier is revised, not shipped"): the
# site SUBTRACTS LEGIB_EDGELINE_K * edge_lines * factor from legibility, which at x1.50 and level 8 reads -0.316 on the
# jian (the roster's worst case) and then scales the defender's read the wrong way; x1.40 keeps one generic off
# combat_systems.legibility's floor (0.119 there). Stacking several is closed at that floor, not here.
GENERIC_LEVERS = (
    ('visual',        'keen_eye',       "watches the opponent's whole body, so the coming action is seen earlier", (1.10, 1.25, 1.50)),
    ('precommit',     'reading_intent', "reads the attack in its preparation, before it is committed", (1.10, 1.25, 1.50)),
    ('tactile',       'blade_feel',     "feels the opponent's pressure and intent through blade contact in the bind", (1.10, 1.25, 1.50)),
    ('tempo',         'timing',         "acts in the opponent's slow moments and keeps the initiative once taken", (1.10, 1.25, 1.50)),
    ('balance',       'footing',        "keeps a stable, mobile base under footwork and pressure", (1.10, 1.25, 1.50)),
    ('edge_read',     'hidden_return',  "uses a double or false edge to hide the line of the return cut", (1.10, 1.25, 1.40)),
    ('choke_control', 'quiet_gather',   "gathers up a long pole without telegraphing the shortened grip", (0.90, 0.75, 0.55)),
)


def _generics():
    """The 21 generics: tradition t receives (lever (t + k) mod 7, tier k) for k = 0, 1, 2. Raises, not asserts, so the
    checks survive `python -O`: an eighth tradition or a name collision with an authored ability fails the import."""
    traditions = [t for t in _TRADITIONS if t != 'none']
    if len(traditions) != len(GENERIC_LEVERS):
        raise ValueError("the Latin square needs as many traditions as levers")
    out = {}
    for t, trad in enumerate(traditions):
        for k, suffix in enumerate(GENERIC_TIERS):
            lever, stem, what, factors = GENERIC_LEVERS[(t + k) % len(GENERIC_LEVERS)]
            name = f'{stem}_{suffix}'
            if name in ABILITIES or name in out:
                raise ValueError(f"generic {name!r} collides with an existing ability")
            out[name] = dict(
                tradition=trad, grade='GENERIC', lever=lever, op='*', value=factors[k],
                desc=f"GENERIC ({suffix}) {lever} lever: {what}. A calibration instrument, not a grounded technique "
                     f"(PC-17, ED-PC-0059, provisional) [SIM-CALIBRATE]")
    return out


ABILITIES.update(_generics())

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
    Level is clamped to [0, MAX_INVESTMENT_LEVEL] (bounded scale; also the overflow safety guard).

    TRADITION GATE (ED-PC-0028): the tradition gates ACCESS to the kit — a fighter can only invest in a technique a
    tradition they KNOW teaches (the design principle in audit/2026-07-23-combat-fiat-audit/fiat_audit_v1.md;
    closes the build-legality gap the interaction-degeneracy critic flagged: a fighter could equip every tradition's
    kit at once). An equipped technique NOT in the fighter's tradition's kit is INERT (you cannot use a technique you
    were never taught) — silently skipped, not an error, so an illegal-but-harmless equip degrades to no-op rather
    than crashing ('every build available'). The gate reads `c.known_traditions` (a set/list, for cross-training) if
    present, else the single `c.tradition`. If the fighter has NO tradition attribute at all (a raw-mechanism unit
    stub), the gate is OFF (ungated) — the gate is a fighter-layer legality rule, not part of the raw factor/bonus
    math the stub tests. Pure."""
    eq = getattr(c, 'equipped', ()) or ()
    known = getattr(c, 'known_traditions', None)
    if known is None and hasattr(c, 'tradition'):
        known = (getattr(c, 'tradition'),)
    allowed = None if known is None else {a for t in known for a in kit(t)}   # None -> ungated (stub); else the union of known kits
    items = eq.items() if isinstance(eq, dict) else ((name, 1.0) for name in eq)
    for name, lvl in items:
        if allowed is not None and name not in allowed:
            continue                                                          # untaught technique -> inert (tradition gates ACCESS)
        yield name, min(MAX_INVESTMENT_LEVEL, max(0.0, float(lvl)))


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
