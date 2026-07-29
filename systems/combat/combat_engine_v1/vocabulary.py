"""vocabulary.py — the combat engine's TOKEN ALPHABET, owned in exactly one place (ED-PC-0042).

WHY A SEPARATE LEAF MODULE, not `core.py`. The domain vocabulary is more primitive than any module that
resolves with it, and two consumers cannot reach `core`:

  · `weapon_physics` CANNOT import `core` — `core` imports `weapon_physics` (the Phase-3
    percussion consolidation). Routing WP's head/mode tokens through core would make that a hard cycle.
  · `capabilities` declares "pure data; no systems/core at module scope (cycle-free)" in its own module
    docstring, and its CAPABILITIES registry is built at module scope from head tokens.

This module imports NOTHING, so every engine module (including those two) can own-source its tokens from
here without creating an edge in the dependency graph. `core.py` keeps the TABLES keyed by this alphabet
(HEAD_MODE / DELIVERY / TIER2MAT / RESIST / PEN_THR / GAP_EXPOSURE) and asserts, at import, that their key
sets agree with the sets below — so a token added here and forgotten there fails loudly at import rather
than silently at a lookup.

ENFORCEMENT: `tests/valoria/test_combat_invariants.py::test_no_bare_vocabulary_literal_in_consumers`
forbids a bare literal from GUARDED_TOKENS in any consumer module (combat_systems / weapon_physics /
capabilities / wrapper / contact). The owner modules (this file and `core.py`, where the tables are
DEFINED) are exempt — that is what "owner" means. `workbench/structure_scan.py` reads GUARDED_TOKENS from
here too, so the measurement instrument and the guard cannot drift apart (CLAUDE.md §8, every rule lives
once).

HOMONYMS ARE DELIBERATELY NAMED SEPARATELY. `'none'` is an armour TIER, a harness MATERIAL and a HILT
type; each gets its own name (TIER_NONE / MAT_NONE / HILT_NONE) so renaming one namespace cannot silently
rename the others. Same for `'puncture'`/`'cut'`, which are both damage-mode tokens and armour-defeat
DIAGNOSTIC labels (`armour_defeat_mode`, pinned per weapon in r3_identity_golden.json).
"""

# ── HEAD tokens — the shape of the striking surface a mode is delivered with ────────────────────────
HEAD_BLUNT = 'blunt'
HEAD_POINT = 'point'
HEAD_CUT_THRUST = 'cut_thrust'
HEAD_STRAIGHT_CUT = 'straight_cut'
HEAD_CURVED_CUT = 'curved_cut'
HEAD_CUT = 'cut'                     # the GENERIC secondary-affordance edge token (never a weapon's native
                                     # head — see core.CUT_AUTH_REF; populated only by systems.element_afforded)
HEADS = frozenset({HEAD_BLUNT, HEAD_POINT, HEAD_CUT_THRUST,
                   HEAD_STRAIGHT_CUT, HEAD_CURVED_CUT, HEAD_CUT})
PURE_CUT_HEADS = frozenset({HEAD_STRAIGHT_CUT, HEAD_CURVED_CUT, HEAD_CUT})       # a pure cutter: no thrust arm
CUT_FAMILY_HEADS = frozenset(PURE_CUT_HEADS | {HEAD_CUT_THRUST})                 # heads whose OWN family already claims an edge
THRUST_FAMILY_HEADS = frozenset({HEAD_POINT, HEAD_CUT_THRUST})                   # heads whose OWN family already claims a tip

# ── DAMAGE-MODE tokens — the physics a blow transmits through (core.RESIST rows) ────────────────────
MODE_PERCUSSION = 'percussion'
MODE_PUNCTURE = 'puncture'
MODE_SHEAR = 'shear'
DAMAGE_MODES = frozenset({MODE_PERCUSSION, MODE_PUNCTURE, MODE_SHEAR})

# ── ARMOUR TIERS (the fighter-facing axis) and MATERIALS (the physics axis) ─────────────────────────
# Distinct namespaces bridged by core.TIER2MAT; 'none' is a member of both and is named twice on purpose.
TIER_NONE = 'none'
TIER_LIGHT = 'light'
TIER_MEDIUM = 'medium'
TIER_HEAVY = 'heavy'
ARMOUR_TIERS = frozenset({TIER_NONE, TIER_LIGHT, TIER_MEDIUM, TIER_HEAVY})
RIGID_TIERS = frozenset({TIER_MEDIUM, TIER_HEAVY})    # mail/plate: the tiers a harness-defeat rule keys on

MAT_NONE = 'none'
MAT_CLOTH = 'cloth'
MAT_MAIL = 'mail'
MAT_PLATE = 'plate'
MATERIALS = frozenset({MAT_NONE, MAT_CLOTH, MAT_MAIL, MAT_PLATE})
RIGID_MATERIALS = frozenset({MAT_MAIL, MAT_PLATE})    # armour that spreads an impact rather than deforming

# ── DEFENCE modes — ORDERED, and the order is load-bearing ─────────────────────────────────────────
# systems.read_contest picks a missed-read mode with `modes[rng.randrange(3)]`, so this sequence IS part of
# the RNG contract: reordering it re-maps every missed-read draw. A tuple, never a set.
DEF_PARRY = 'parry'
DEF_DODGE = 'dodge'
DEF_WIND = 'wind'
DEFENCE_MODES = (DEF_PARRY, DEF_DODGE, DEF_WIND)

# ── HILT types (weapon_physics.GUARD / HILT_CATCH_MULT keys) ────────────────────────────────────────
HILT_COMPOUND = 'compound'
HILT_SIMPLE = 'simple'
HILT_NONE = 'none'                   # HOMONYM of TIER_NONE/MAT_NONE — a bare haft, not an armour level
HILT_TYPES = frozenset({HILT_COMPOUND, HILT_SIMPLE, HILT_NONE})

# ── ARMOUR-DEFEAT DIAGNOSTIC labels (weapon_physics.armour_defeat_mode) ─────────────────────────────
# A REPORT vocabulary, not a resolution one: these strings are pinned per weapon in the frozen
# tests/valoria/r3_identity_golden.json. 'puncture'/'cut' are homonyms of the damage-mode/head tokens and
# are named apart so a rename on either axis cannot silently re-key the golden.
ADEF_MODE_PUNCTURE = 'puncture'
ADEF_MODE_CONCUSSION = 'concussion'
ADEF_MODE_GAP_THRUST = 'gap-thrust'
ADEF_MODE_CUT = 'cut'

# ── THE GUARDED SET ────────────────────────────────────────────────────────────────────────────────
# The 18 tokens the ownership guard enforces. This is the set `workbench/structure_scan.py` [D] has always
# measured (279 occurrences / 18 tokens on the pre-sweep tree); it is declared HERE so the instrument and
# the test read the same list.
#
# DELIBERATE EXCLUSION: HEAD_CUT ('cut') is NOT guarded. The same string is the name of a GEOMETRY primitive
# field (`geo['cut']`, the derived edge magnitude, alongside `geo['thrust']`/`geo['gap']`), which is a
# different namespace with dozens of live sites. Guarding it would demand routing the geometry field names
# through this module too — a strictly larger job (the whole `geo`/`w` field vocabulary) that is FILED, not
# done here (CLAUDE.md §0.1 point 5: sweep only what the task is load-bearing on). The head-token USES of
# 'cut' inside the consumers are routed through HEAD_CUT regardless; they are simply not guard-enforced.
GUARDED_TOKENS = frozenset(
    (HEADS - {HEAD_CUT})            # 5 head tokens
    | DAMAGE_MODES                  # 3 damage modes
    | ARMOUR_TIERS                  # 4 armour tiers ('none' shared with materials)
    | MATERIALS                     # + cloth / mail / plate
    | set(DEFENCE_MODES)            # 3 defence modes
)
assert len(GUARDED_TOKENS) == 18, f"guarded vocabulary changed size: {sorted(GUARDED_TOKENS)}"
