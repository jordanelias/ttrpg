"""Core engine module — canonical resolution primitives. Single source for ob/degree/roll/damage.
Resolves the sigma kernel through engine.dice_engine.sigma_leverage (the numpy-free single source,
Stage 1a / D0-2) so every subsystem resolves identically. No A/B knowledge here.

[ED-1085 container de-leak] The sigma math comes from sigma_leverage (parity-tested against the numpy originals
at 1e-9 — engine/tests/test_sigma_leverage_parity.py); the engine's own combat-state constants live here / in
combatant.py. The RNG contract: `rng` is a stdlib random.Random (rng.gauss). The continuous engine's distribution
is Normal(mu*N, sigma*sqrt(N)), same per-die TN table."""
import functools
from math import tanh, exp
from engine.dice_engine import sigma_leverage as SL
from engine.dice_engine import dice_engine as DE   # THE degree ladder's owner (degree() below routes through it)
from . import vocabulary as V   # the token ALPHABET (ED-PC-0042) — a zero-import leaf, so weapon_physics and
                         # capabilities (neither of which may import core) own-source the same tokens.
                         # This module owns the TABLES keyed by it; the asserts below pin the two together.

# ---------- logistic (single source, ED-PC-0025) ----------
# The single owner of the 1/(1+e^-x) squash (combat_systems.bind_dominance_p / the two read-contest sites,
# contact.grab_outcome) — a §8 "every rule lives once" rule AND an overflow hazard: a grossly out-of-contract
# net-sigma (e.g. an attribute/skill orders of magnitude past the legal ceiling of 5) drives `exp(-x)` past the float
# range and CRASHES fight resolution with OverflowError. Legal-build |argument| never exceeds ~2.4 (all
# weapon/armour/tradition mixes), so the clamp below sits ~200x outside any reachable value, guarding pathology
# only ("every build available" without crashing the engine on out-of-contract inputs). Pure.
_LOGISTIC_CLAMP = 500.0   # exp(500) is finite (< 1e218); exp(710)+ overflows. Legal max |arg| ~2.4.
def logistic(x):
    """Numerically-safe logistic squash 1/(1+e^-x) -> (0,1). Clamps the argument to [-500, 500] so an
    out-of-contract net-sigma cannot overflow exp() and crash resolution; unchanged for all in-contract x."""
    if x < -_LOGISTIC_CLAMP: x = -_LOGISTIC_CLAMP
    elif x > _LOGISTIC_CLAMP: x = _LOGISTIC_CLAMP
    return 1.0 / (1.0 + exp(-x))
from . import weapon_physics as WP   # percussion authority lives ONCE in WP (the credited derived value);
                              # core.strike reads WP.percussion_authority (the sigma path systems.adef_cap already does).
                              # WP imports only math + the zero-import `vocabulary` leaf at module scope (cycle-free),
                              # so this import is safe.

TN = SL.TN_STANDARD
POOL_FLOOR = 5     # [canonical: params/core.md §Derived Scores (Combat Pool min 5)]
BASE_POOL = 6      # [class-C: armature — faculty-driven pool base; pool = max(5, faculty+6), ED-901 (History until CR-85, ED-IN-0330); relocated verbatim from r1, ED-1085]

def resolution_pool(faculty):
    """Agility-INDEPENDENT resolution pool (ED-901; re-ratified ED-900/904): max(5, faculty + 6). `faculty` is the
    party's dice score for the verb that opened the fight (CR-85, ED-IN-0330: it replaces `history`, formula unchanged;
    `attributes.py` says where the season's value comes from)."""
    return max(POOL_FLOOR, int(round(faculty)) + BASE_POOL)
def roll_net(pool, rng): return SL.roll_net_continuous(pool, TN, rng=rng)
# Combat's lower-case band spelling of the owner's enum. A RELABEL, not a ladder: every key is decided by
# `DE.degree_from_net`, and this map cannot move a boundary.
_COMBAT_LABEL = {DE.Degree.FAILURE: 'fail', DE.Degree.PARTIAL: 'partial',
                 DE.Degree.SUCCESS: 'success', DE.Degree.OVERWHELMING: 'overwhelming'}
def degree(net, ob):
    """The degree of a continuous `net` against `ob`, read off THE owner ladder
    (`engine.dice_engine.dice_engine.degree_from_net`, Jordan's 2026-08-14 ruling: the margin `net - ob`
    decides the band, 3 or more is always Overwhelming) and spelled in combat's lower-case vocabulary.

    No local re-banding: a continuity shift on top of the owner would be a second ladder, which the single-owner
    guard (`tests/valoria/test_degree_ladder_single_owner.py`, where this site is enrolled in LADDERS) fails on."""
    return _COMBAT_LABEL[DE.degree_from_net(net, ob)]

_DEGREE_OF = {label: deg for deg, label in _COMBAT_LABEL.items()}
@functools.lru_cache(maxsize=None)
def band_floor(band, ob):
    """The smallest `net` the owner ladder reads as `band` OR BETTER at `ob` — a band EDGE, read off
    `DE.degree_from_net` by bisection (ranked by the owner's `DEGREE_ORDINAL`), never re-declared here.
    The workbench's displayed distribution and `strike()`'s overwhelming tail both need an edge, so the edge is
    DERIVED here rather than copied. Exact to the float: `degree(band_floor(b, ob), ob)` is `b` and the next float down is not.
    The +/-64 bracket around `ob` is asserted, not assumed (the owner's edges sit within 3 of `ob`). Pure; cached
    per (band, ob) — Ob is faculty/2, so a fight touches a handful of values. `band` is 'partial', 'success' or
    'overwhelming': 'fail' is the lowest band and has no edge (it fails the bracket assert)."""
    k = DE.DEGREE_ORDINAL[_DEGREE_OF[band]]
    rank = lambda x: DE.DEGREE_ORDINAL[DE.degree_from_net(x, ob)]
    lo, hi = ob - 64.0, ob + 64.0
    assert rank(lo) < k <= rank(hi), (band, ob)
    while True:
        mid = (lo + hi) / 2
        if mid <= lo or mid >= hi:
            return hi
        if rank(mid) >= k:
            hi = mid
        else:
            lo = mid

def ob_from_defender(defender):
    """RULED Ob-derivation (Jordan, 2026-08-15, verbatim: "DECISIVE_OB for combat is stupid as hell and is dead
    because Ob should be determined by your opponent more than anything" — tests/valoria/test_degree_ladder_
    single_owner.py's RULINGS dict, entry "2026-08-15 — combat, and the sequence"). Score/2 plus that instance's
    modifiers, the SAME reading modules/social_contest/roll.py::obstacle applies (under its H-213 ceiling) for a person subject
    on the season side. This resolver's own score is `faculty` — the SAME score resolution_pool() derives dice
    from (ED-901): `faculty` is the value `engine/season/seam/wrappers/sigma.py::faculty` reads for the party, passed
    in through `PersonalCombatInput.faculties` (CR-85, ED-IN-0330); one value per party feeds his pool and the Ob he
    is attacked against.
    [ASSUMPTION; medium; Jordan to correct; revert: the faculty value feeds the pool only and the Ob reads the class
    default 3] -- the CR-85 design is UNRATIFIED (ED-IN-0351).
    ⚠ THE OB READS MORE THAN THE SOCIAL CONTEST'S DOES (Phase 3, B10-11): `faculty` carries `pool_default` as the
    pool's fallback and the practice addend, which `seam/wrappers/sigma.py::_opposition_of` ("NEVER THE FALLBACK AND
    NEVER PRACTICE") leaves out. A person holding no key is attacked at Ob 1.0 here and at `opposed_ob(pool_default)` (plus the act's difficulty) in a
    social contest: two ladders for one quantity.
    NO INSTANCE MODIFIER IS ADDED HERE. Wound impairment already has its OWNER
    (combat_systems.wound_impairment, ED-1041) and is folded into net_sigma at every call site (bind_sigma,
    the defence assembly, reach_sigma, pursuit_sigma) — adding a second wound term onto Ob would double-count
    it, exactly the class of defect `wrapper.engagement`'s `neutralize` note already guards against for defence_sigma ("NOT re-scaled
    by dsig, which already shaped the roll via net_sigma (audit C-2: avoid double-counting defender skill)").
    A genuine per-instance Ob modifier would be a NEW term with its own owner, not folded into this function
    silently. Pure."""
    return defender.faculty / 2.0


def resolve(pool, net_sigma, rng, ob):
    """Canonical mu-shift resolution (sigma_leverage_handoff §1): the sigma-leverage boosts the ROLL
    (boost = eff_sigma*sigma_N = soft_cap(net_sigma)*sigma_n(pool)), it does NOT shift the Ob.
    SL.eff_ob is display-only per its own docstring; resolving via the floored Ob-shift distorted the degree
    bands (overwhelming trivialised by the Ob-floor).
    `ob`: the RULED Ob-from-defender value (Jordan 2026-08-15) — callers pass `ob_from_defender(defender)`.
    REQUIRED rather than defaulted, so no caller can skip the derivation (ED-PC-0058).
    Returns (deg, net)."""
    net = roll_net(pool, rng) + SL.soft_cap(net_sigma) * SL.sigma_n(pool)
    return degree(net, ob), net

# ---- damage (Impact x Coupling x Quality) — CONTINUOUS transmission, NO tanh saturation ----
# Adopts the ground-up linear damage model [damage_model.py / damage_model_design, Jordan 2026-05-30,
# ratified 2026-06-17]: damage = Impact x Coupling x Quality, NO cap/tanh, so head/strength/armour drive
# damage as a live gradient (the old tanh cap saturated everything to ~the cap and flattened the gradient).
#   Impact   = K_STR_HEAD[head]*strength + heft (PC-20 (1): the Strength coefficient is the head's; blunt 1.0); BLUNT heft is CONTINUOUS from percussion authority P_auth (perc carries it);
#              cut/thrust heft is weight-class (continuous-mass cut-impact deferred, plan #9).
#   Coupling = DELIVERY(head) x transmit(material-resistance-per-mode) x gap(COVERAGE_GAP) — material/mode physics.
#   Quality  = degree factor.   Constants from damage_model (emergent-calibrated so an even Success ~= 1 WI).
HEFT_HEAVY=3.0                                                      # heavy-class cut/thrust heft scale (unchanged — the multiplier below anchors on the SAME 2H cut-thrust reference WP.heft() normalises to 1.0)
def heft_resp(w, cfg, grip=0.0, sel_head=None, sel_pc=None, sel_arm=None):
    """Continuous weapon heft response (heft-units) — DERIVED from weapon_physics.heft() (striking mass ×
    forward-balance, normalised so the longsword anchor reads 1.0). `cfg` is accepted for call-site compatibility
    (unused; the derivation is pure).
    CIRCUMSTANCE-DEGRADED (I2, D2): threads grip/sel_head/sel_pc into WP.heft's mode-split Phi_grip (1.0 at grip=0,
    the default).
    [ED-PC-0050, E3b] `sel_arm` ('shear' | 'puncture' | None) threads the RESOLVED arm of a cut_thrust weapon, so a
    composite that resolves a thrust is paid the axial thrust lever rather than the swing moment. None keeps the
    token-keyed behaviour."""
    return WP.heft(w, grip=grip, sel_head=sel_head, sel_pc=sel_pc, sel_arm=sel_arm)
QUAL={'graze':0.25,'partial':0.5,'success':1.0,'overwhelming':1.5}  # [damage_model QUALITY base; overwhelming = sigma-leverage tail floor]
# ED-PC-0036: 'partial' IS a real degree from degree() (0 <= net - ob < 1); the wrapper maps it to an explicit
# graze/bind rather than a damage call, and damage() gates on the LITERAL tuple ('graze','success','overwhelming'),
# not on QUAL membership. A quality table that omits a member of its own domain is a worse artifact than an unused row.
OW_MAX=2.5; OW_Z=1.5          # [M-QUAL D-A: overwhelming quality saturates 1.5->OW_MAX by sigma-leverage severity]
DMG_SCALE=1.55                                                      # [damage_model — even Success ~= 1 WI; emergent-tunable]
# PENETRATION THRESHOLD (ED-PC-0032): armour resists up to a floor — a blow whose coupling-
# reduced impact does not clear the tier's resistance inflicts little LASTING WOUND (it is stopped/deflected), so a
# weapon that CANNOT defeat the harness cannot win by VOLUME of sub-penetration pokes. Applied as a SOFT knee
# on the post-coupling damage: eff = d · d²/(d²+PEN_THR²) — a blow at the threshold keeps half, well above keeps ~all,
# well below collapses toward 0. Unarmoured PEN_THR=0 (knee inert). Emergent, not a
# rapier special-case: a gap-dagger/spike/blunt that DEFEATS plate produces a large d (kept); a rapier/arming/spear
# point that pings off it produces a small d (collapsed). [SIM-CALIBRATE] per-tier floors.
PEN_DEFICIT_K=6.0   # [SIM-CALIBRATE] how sharply the penetration knee rises with the weapon's armour-defeat DEFICIT (ED-PC-0038). 0 restores the raw-magnitude-only knee.
PEN_THR={'none':0.0,'light':0.0,'medium':2.5,'heavy':6.5}   # light (soft gambeson) needs no penetration floor; the rapier inversion is a HEAVY-tier effect (heavy 74->16), medium a smaller gate
HEAD_MODE={'blunt':'percussion','point':'puncture','cut_thrust':'shear','straight_cut':'shear','curved_cut':'shear','cut':'shear'}
DELIVERY={'blunt':1.6,'point':1.45,'straight_cut':1.5,'curved_cut':1.5,'cut':1.5}  # [damage_model head delivery]
K_STR_HEAD = {V.HEAD_BLUNT: 1.0, V.HEAD_STRAIGHT_CUT: 0.925, V.HEAD_CURVED_CUT: 0.925, V.HEAD_CUT: 0.925,
              V.HEAD_CUT_THRUST: 0.925, V.HEAD_POINT: 0.85}
# PC-20 (1), AR-10, adj §2.2 (v) [SIM-CALIBRATE; ASSUMPTION; medium; Jordan to correct; revert: every head 1.0, the
# control, which reproduces the pre-PC-20 tree byte for byte]. Strength's weight in `strike_impact`, PER SELECTED HEAD:
# a big blunt head turns the arm's force into damage most fully, a skinny point "slides in with little effort" and
# turns it least, an edge lies between. ADDITIVE (k·strength + heft): ED-1040's reverted multiplicative form
# ((STR_REF+heft)·(strength/STR_REF)^STR_EXP) is NOT reintroduced. Every head token is a key (a missing head is a
# KeyError, never a silent 1.0); `cut_thrust` takes the edge weight — its family claims an edge
# (V.CUT_FAMILY_HEADS), and it is one head token whichever arm `cut_thrust_arm` resolves.
# THE SWEEP RULE. AR-10 says Strength's damage is "mitigated by the type of weapon", the blunt head "most positively
# affected": blunt stays 1.0 (unmitigated), edge = 1-d, point = 1-2d (equal steps; nothing measured separates
# the two gaps), d > 0 so the order is strict and d < 0.5 so a point keeps some Strength. Shipped d = .075, the middle
# of the d-range (.05-.1) over which ED-1040's observable (the str-2 greatsword mirror's draw rate) AND every
# matchup family's pooled draw rate stay inside their d=0 Wilson 95% intervals (less damage per blow is a longer
# fight).
# Material resistance per mode in [0,1] (resist; transmit = 1-resist). GROUNDED (Alan Williams, The Knight
# and the Blast Furnace, 2003) — designs/audit/2026-06-30-combat-grounding/: a 16-30 layer cloth jack sheds a ~60-130 J
# cut; a point stops at only ~50 J vs ~80 J cut (the documented cut>>point asymmetry); cloth shows modest standalone
# blunt absorption; cutting riveted mail is "functionally impossible," >130 J ceiling. Plate row + mail perc/punc are
# well-pinned.
# [CI — DESIGNER-SET/UNSOURCED: the cloth fractions are a designer normalisation of Williams' joules onto the 0-1 scale,
#  NOT a Williams figure.]  [PACKAGE: plate.percussion .30 is honest ONLY with the FIX-1b authority gate below — never
#  tune one without the other (ungated, an honest plate-vs-blunt resist is ~.55-.65).]  Assumes RIVETED mail + HARDENED
# ~2mm plate (butted mail / wrought iron are far weaker — not modelled).
RESIST={'none': {'percussion':0,   'shear':0,   'puncture':0},
        'cloth':{'percussion':.12, 'shear':.45, 'puncture':.12},
        'mail': {'percussion':.20, 'shear':.85, 'puncture':.45},
        'plate':{'percussion':.30, 'shear':.95, 'puncture':.70}}
TIER2MAT={'none':'none','light':'cloth','medium':'mail','heavy':'plate'}  # [armour_axes presets — tier->material]
COVERAGE_GAP=0.15                                                   # [damage_model — gap/bare-zone exposure, full coverage]
# [ED-PC-0055, J-20 (B)] A scalar. A `coverage` level ('full' | 'partial') is out of scope for personal combat (an
# off-hand / partial-coverage hit location); add the key and the `coverage` parameter of _transmit, cut_thrust_arm and
# coupling with the first weapon or armour that needs a second level.
# ── SITUATIONAL GAP GAME — a thrust/puncture is GAP-SEEKING ─────────────────────────────────────────────────────
# grounded_weapon_armour_usemode_model.md + Williams (The Knight and the Blast Furnace, 2003): a point does NOT punch
# through plate — it SEEKS the reach-ladder gaps (visor/armpit/groin/palm). Its plate-defeat effectiveness is the
# fraction of the target that is thrust-accessible gaps (GAP_EXPOSURE, per material) SCALED BY the weapon's derived
# gap_precision (w['gap'] = point_concentration x cross_section rigidity — a stiff concentrated point finds+holds the
# gap; a whippy point deflects). This de-vestigialises w['gap'], which damage() already carried but ignored. The
# armoured-combat treatises (Le Jeu de la Hache / Harnischfechten) make the thrust-to-gap the PRIMARY armoured kill —
# so a poleaxe spikes vs harness, a rondel excels at the gaps, a rapier's whippy point is mediocre, all EMERGENT from
# the derived gap_precision (never a weapon name).
# [SIM-CALIBRATE within the reach-ladder frame]: plate is well-covered but a skilled stiff-point thrust ALWAYS reaches
# the visor/armpit/groin/palm gaps; mail exposes more (open weave/edges); cloth/none are mostly accessible. The plate
# value is set at ~the poleaxe hammer->spike flip (systems.select_mode) so the reach-ladder truth holds; the
# orchestrator tunes the final magnitudes. GROUNDING (direction): Williams (puncture succeeds at gaps/weak-points).
GAP_EXPOSURE={'none':1.0,'cloth':0.97,'mail':0.95,'plate':0.90}     # [SIM-CALIBRATE] thrust-accessible gap fraction / material (reach-ladder). BROKEN-LOGIC FIX (ED-PC-0023): the old {cloth:0.85, mail:0.90, plate:0.90} CONTRADICTED this block's own grounding prose above — "mail exposes MORE (open weave/edges)" than plate (was mail==plate) and "cloth/none are mostly accessible" (cloth was the LOWEST, below both armours). Corrected to the monotone none>cloth>mail>plate the prose states: mail 0.95 now exposes more than plate 0.90 (LIVE — the gap term binds for mail); cloth 0.97 matches "mostly accessible" (mostly inert — the through-material floor t=0.88 dominates for soft cloth). The plate=0.90 anchor (the poleaxe hammer->spike flip) is UNCHANGED — the heavy-armour gap game is preserved exactly.
# ── VOCABULARY OWNERSHIP (ED-PC-0042) — the tables above are keyed by vocabulary.py's alphabet ──────────────
# Import-time, so a token added to the alphabet and forgotten in a table (or vice versa) fails LOUDLY here
# rather than silently at a `.get(head, default)` that quietly takes the fallback branch. These are DERIVATION
# checks, not re-definitions: the tables stay hand-written (each cell carries its own sourcing comment).
assert set(HEAD_MODE) == V.HEADS, f"HEAD_MODE keys != HEADS: {set(HEAD_MODE) ^ V.HEADS}"
assert set(HEAD_MODE.values()) <= V.DAMAGE_MODES, "HEAD_MODE maps a head to an undeclared damage mode"
assert set(TIER2MAT) == V.ARMOUR_TIERS, f"TIER2MAT keys != ARMOUR_TIERS: {set(TIER2MAT) ^ V.ARMOUR_TIERS}"
assert set(TIER2MAT.values()) <= V.MATERIALS, "TIER2MAT maps a tier to an undeclared material"
assert set(RESIST) == V.MATERIALS and all(set(r) == V.DAMAGE_MODES for r in RESIST.values()), \
    "the RESIST matrix no longer covers materials x damage-modes exactly"
assert set(PEN_THR) == V.ARMOUR_TIERS and set(GAP_EXPOSURE) == V.MATERIALS, \
    "PEN_THR must cover the armour tiers and GAP_EXPOSURE the materials, exactly"
# DELIVERY is a STRICT SUBSET and must NOT be keyset-derived from HEADS: ED-PC-0037 keeps 'cut_thrust' out of it (the
# pre-max blended 1.35 is dead once cut_thrust_arm resolves the two arms on their own tokens) and out of the
# Godot-facing contract. Deriving these keys would resurrect it.
assert set(DELIVERY) < V.HEADS and V.HEAD_CUT_THRUST not in DELIVERY, \
    "DELIVERY must stay a strict subset of HEADS with no 'cut_thrust' entry (ED-PC-0037)"

GAP_PREC_REF=0.65                                                   # neutral gap_precision default for the puncture path (a mid-roster point) — the LIVE combat path always THREADS the weapon's real w['gap'] (systems.select_mode / core.strike), so this default only guards a hypothetical unthreaded caller.
# FIX-1b [FIAT — no melee-speed behind-plate data exists; ballistic BABT is the wrong regime, per Phase-3 grounding]:
# percussion transmitted through RIGID armour (mail/plate) scales with the blow's percussion AUTHORITY — a steel
# hammer (p_auth 8) overwhelms the armour's impact-spread; a wooden staff (p_auth 5.63, ED-PC-0047/E2a) is
# absorbed proportionately more. A "~4" staff intent is NOT reachable while the mace is pinned at PERC_CAP: at
# PERC_EXP=0.30 an authority ratio of 0.5 demands an INPUT ratio of 0.5^(1/0.30)=0.099, which no honest mass/lever
# form yields between a 1.478 kg 2H staff and a 1.2 kg mace. Closing that gap is the PERC_SCALE/PERC_EXP re-fit, not a
# lever question. The TRANSMIT
# term is LINEAR in (perc/PERC_AUTH_REF) (E=1.0, momentum-like). It COMPOUNDS with the blunt heft
# (3·perc/8 in damage()), so the net blunt-vs-rigid damage scales ~perc² in authority — force and through-armour
# transmission are distinct physics, both authority-dependent (intended). Soft cloth absorbs by deformation
# (~authority-independent) so it is unscaled. perc=PERC_AUTH_REF = full transmission. Magnitude is FIAT. NOTE: FIX-1b
# is a damage-LETHALITY reduction only — it does NOT touch the sigma/reach/control path that drives the staff's
# vs-plate WIN-RATE (that is FIX-1's job).
# EXTENDED TO EVERY MATERIAL (U2/ED-PC-0011): the authority scaling applies vs cloth/none too, because
# weapon_physics.reversed_grip_percussion (ED-PC-0009) puts a genuinely WEAK percussion candidate (~1.4-1.8/8 for a
# two-handed sword's Mordhau option) into select_mode's greedy comparator: without the scaling DELIVERY['blunt']=1.6
# (the highest fixed constant of any token) would let a weak pommel-strike win selection against UNARMOURED targets
# purely on the delivery constant, with `perc`'s magnitude never read — backwards from the HEMA sourcing (Mordhau is a
# response to armour defeating the edge, not a general preference). The two material classes need DIFFERENT
# references: mail/plate keeps PERC_AUTH_REF=8.0 (mace's own exact value; the poleaxe's spike-vs-plate gap game
# relies on poleaxe's blunt being SOMEWHAT weaker than mace's there, ratio 7.61/8.0=0.952); none/cloth uses the lower
# PERC_AUTH_REF_SOFT=6.5, anchored on the WEAKEST attested genuinely-dedicated hammer-class weapon (bec_de_corbin,
# 6.51 via the live per-element percussion path) rather than the strongest (mace) — a mace-anchored 8.0 would
# needlessly discount every dedicated hammer-class weapon that isn't mace itself and flip bec_de_corbin/
# lucerne_hammer away from their own hammer face at the unarmoured tier. Every dedicated weapon (mace 8.0, goedendag
# 8.0, poleaxe 7.61, lucerne_hammer 7.05, bec_de_corbin 6.51) then clamps to ratio=1.0 at none/cloth, while the
# Mordhau candidates (1.4-1.8, a 4.7-point gap below bec_de_corbin with zero overlap) score 0.22-0.28 — discounted,
# losing to a weapon's own cut/thrust at low armour and only competitive vs rigid armour it cannot otherwise defeat.
# SINGLE-OWNER BINDING (ED-PC-0042 rider I1b): PERC_AUTH_REF is the TOP OF THE PERCUSSION-AUTHORITY SCALE, which is
# owned by the module that clamps to it — WP.PERC_CAP (weapon_physics.py), bound over core's
# `from . import weapon_physics as WP` (no new dependency edge) so a PERC_SCALE/PERC_EXP re-fit cannot desync them.
# PERC_AUTH_REF_SOFT is NOT bound: it is a DIFFERENT anchor (bec_de_corbin's 6.51 live authority, the weakest
# dedicated hammer — see the U2 block above), not the scale top.
PERC_AUTH_REF=WP.PERC_CAP; PERC_AUTH_REF_SOFT=6.5; PERC_TRANSMIT_FLOOR=0.35
def _transmit(mode, mat, perc=PERC_AUTH_REF, gap_prec=GAP_PREC_REF, thrust_auth=1.0):
    t=1.0-RESIST[mat][mode]
    if mode=='puncture':                                           # SITUATIONAL GAP GAME: a thrust takes through-
        # material OR the reach-ladder gap it seeks. The gap term is GAP-SEEKING: the material's thrust-accessible gap
        # fraction (GAP_EXPOSURE) scaled by the WEAPON's derived gap_precision (a stiff concentrated point finds+holds
        # the gap; a whippy point deflects). Plate is not a flat 0.15 for every point: the poleaxe spike / rondel
        # beat the through-material 0.30, the rapier's whippy point does not. Emergent in gap_prec (= w['gap']); no
        # weapon name.
        # PC-5 (ED-PC-0015): thrust_auth (point-to-hand lever authority) scales the GAP-PRESS term ONLY — pressing a
        # point INTO a harness gap is exactly the pommel-backed short-lever act (Fiore/Talhoffer half-sword, the rondel
        # to the visor); a long reach-thrust at extension cannot press the same way. The THROUGH-MATERIAL term `t` is
        # NOT scaled: a thrust that lands on flesh/cloth (none/cloth: t=1.0/0.88) is lethal regardless of lever — reach
        # weapons stay deadly vs soft targets, they only lose the GAP-penetration edge vs mail/plate. Inert at
        # thrust_auth=1.0 (short-lever/half-sword/dagger).
        return max(t, GAP_EXPOSURE[mat]*gap_prec*thrust_auth)
    if mode=='percussion':                                          # FIX-1b, extended U2/ED-PC-0011: authority-scaled
        ref = PERC_AUTH_REF if mat in ('mail', 'plate') else PERC_AUTH_REF_SOFT   # rigid armour keeps the original, pre-existing reference; none/cloth uses the softer one (see comment above)
        t*=max(PERC_TRANSMIT_FLOOR, min(1.0, perc/ref))
    if mat!='none':
        g=COVERAGE_GAP; return t*(1-g)+1.0*g                       # some blows reach a bare zone
    return t
# CUT_AUTH_REF [U2/ED-PC-0011]: the bare 'cut' token key is NEVER a weapon's own native head: no weapon is authored
# as native 'cut' (dedicated cutters use 'straight_cut'/'curved_cut', which this constant does NOT touch).
# The 'cut' key is populated ONLY by systems.element_afforded's graded secondary-affordance check (a weapon
# whose NATIVE head is something else — point/blunt/etc — but whose geometry also clears a real-edge floor).
# Without scaling, an incidental edge (rapier geo['cut']=0.30, dangpa=0.30, main_gauche=0.30) would be credited with
# the SAME DELIVERY['cut']=1.5 as a dedicated cutting sword — high enough to beat a native point's DELIVERY
# (1.45) purely on the constant, regardless of how weak the incidental edge actually is. Anchored — per the same
# principle as PERC_AUTH_REF above — on the WEAKEST attested genuinely-dedicated cutter in the roster
# (hook_sword, curved_cut, geo['cut']=0.710), not a roster-wide average/median (a self-referential statistic
# with no independent grounding): every native straight_cut/curved_cut token sits at or above this floor by
# construction, so anchoring here is a lower-bound safety margin, not a curve-fit. 0.70 sits just below
# hook_sword's exact value; every incidental secondary-cut candidate found in the roster (0.20-0.50) sits
# clearly below it with no overlap. Scoped to the 'cut' token ONLY — 'point' does not need an analogous
# scaling: DELIVERY['point']=1.45 is already the lowest shear-family-adjacent constant, so a secondary point
# token can never win a native cutter's own selection purely on the DELIVERY constant; where a secondary point
# DOES win at a higher tier, e.g. greatsword vs cloth, it is the RESIST table's own Williams-sourced
# puncture>>shear-vs-cloth asymmetry doing that.
CUT_AUTH_REF=0.70
# CUT_REF_NATIVE [A7a channel 1 / M6, ED-PC-0051]: the reference NATIVE cutting edge, anchored on the
# KATANA, whose derived cut_factor is exactly 1.00 — a canonical attested single-edged cutter. Follows this module's
# own precedent of anchoring a reference on a named weapon (CUT_AUTH_REF <- hook_sword, the weakest dedicated cutter;
# THRUST_AUTH_REF <- bear_spear; PERC_AUTH_REF_SOFT <- the weakest attested hammer).
# WHY A SECOND REFERENCE RATHER THAN RE-ANCHORING CUT_AUTH_REF: the two populations do not overlap and must not share
# a scale. The bare 'cut' TOKEN is an INCIDENTAL edge on a weapon whose native head is a point or a blunt (core.py's
# own comment above: it "is NEVER a weapon's own native head"), and its eff runs 0.02-0.50 — genuinely below 0.70, so
# min(1.0, eff/CUT_AUTH_REF) grades it correctly. The NATIVE cut heads run 0.710 (hook_sword) to 1.330 (shamshir),
# entirely ABOVE 0.70, so that same expression would be identically 1.000 for all of them (31% of the roster coupled
# identically regardless of its edge): a min(1.0, ...) cap can only ever penalise a population that is already losing.
CUT_REF_NATIVE=1.00
# CUT_EDGE_GATE_MODE [Jordan ruling, 2026-07-29]: "cutters need to be excellent in contexts where they can CUT ie
# unarmoured and light armour". A SUPERIOR edge therefore pays off in proportion to how much the target yields to an
# edge — which is already owned by _transmit('shear', mat), normalised to its unarmoured value (none 1.000 /
# cloth 0.618 / mail 0.277 / plate 0.193). No new constant: the gate IS the existing resist table.
# The asymmetry is deliberate and guarded (test_a_poor_edge_is_poor_everywhere): a keen edge's BENEFIT is gated on the
# target yielding, but a poor edge's PENALTY is not. A badly-edged weapon does not become a good cutter against an
# unarmoured man. Note this means the benefit carries a SECOND material dependence on top of the _transmit factor the
# return already applies — that is intended (the benefit concentrates where an edge can work), not an oversight.
def _shear_yield(mat):
    """How much this material yields to an EDGE, normalised so unarmoured == 1.0. Reads the owned resist table; adds
    no constant of its own. Pure."""
    base = _transmit('shear', 'none')
    return (_transmit('shear', mat) / base) if base > 0 else 0.0
# THRUST_LEVER_REF / _FLOOR [PC-5 / ED-PC-0015, 2026-07-22]: thrust AUTHORITY — the capacity to drive a point home
# behind body-weight and a pommel-press — is a PRIMITIVE derived from the point-to-controlling-hand lever (head_len,
# METRES). A SHORT lever (a rondel dagger, head_len 0.21; a half-sworded longsword, head_len 0.42) can be pressed home
# with the off-hand on the pommel and full body-mass stacked behind a rigid short column — the historical armour answer
# (Fiore/Talhoffer half-sword, the rondel to the visor/armpit). A LONG lever (a spear/pike thrust at full extension,
# head_len 1.6-1.9) delivers the SAME point but cannot be backed the same way: the reach is bought by surrendering the
# short-column pommel-press, so per-contact penetrating authority falls. Emergent in head_len — NO weapon name. Anchored
# (THRUST_LEVER_REF=0.55 m) so the dagger/half-sword class (head_len<=0.42) saturates at full authority (ratio>=1.0,
# clamped) and the reach-thrust class is scaled down toward the floor; THRUST_LEVER_FLOOR=0.30 keeps even a pike's point
# a real (never-zero) threat. Scoped to the THRUST family only (the 'point' head + the cut_thrust half-sword/gap-thrust
# term); shear/percussion do not gap-press and are untouched. Distinct from ED-PC-0012's proposed THRUST_AUTH_REF (that
# is a point-TOKEN-magnitude anchor; this is a head_len LEVER factor) — different axis, deliberately different name.
# THRUST_AUTH_REF [PC-4 / ED-PC-0012, 2026-07-22]: the point-TOKEN-MAGNITUDE analog of CUT_AUTH_REF.
# core._transmit's puncture gap-seeking term is floor-locked to the raw material transmission for any
# physically-plausible gap_prec, so DELIVERY['point']=1.45 would be credited IN FULL to a weak incidental point on a
# dedicated slasher regardless of how poor that point actually is (scimitar point_eff 0.16, sabre 0.26, falchion 0.23),
# and every cutter with any secondary point token would switch to 'point' vs armour purely on the fixed constant — a
# floor-locked artifact, not earned thrust geometry. So DELIVERY['point'] scales by the SELECTED point's own derived
# thrust magnitude (eff) vs a reference, exactly as 'cut' scales by eff/CUT_AUTH_REF. Anchored — per the same
# weakest-of-the-genuine-population principle as CUT_AUTH_REF (hook_sword, the weakest dedicated cutter) and
# PERC_AUTH_REF_SOFT — on the WEAKEST attested NATIVE pointer in the roster (bear_spear, point_eff 0.530; bec_de_corbin's
# native head is 'blunt', its beak a SECONDARY point). 0.52 sits just below bear_spear's 0.530, so every native
# point-headed weapon (bear_spear 0.53, rapier 0.61, spear 0.72, estoc 0.89, …) clamps to ratio 1.0 and is UNAFFECTED
# by construction — only SECONDARY/incidental points on cutters (all < 0.53) are scaled by their true geometric
# quality. Scoped to the 'point' HEAD only (the cut_thrust half-sword thrust keeps its own eff = the EDGE magnitude, a
# different quantity); distinct axis from PC-5's THRUST_LEVER_REF (head_len lever) — both refine the point path, one
# by geometry-magnitude, one by pommel-press lever.
THRUST_AUTH_REF=0.52
# THRUST_LEVER_FLOOR (ED-PC-0023): sits just below the roster's natural minimum THRUST_LEVER_REF/head_len (~0.271, the
# longest polearms, head_len 1.85-2.03m), so it only guards genuinely pathological/future weapon data (its stated
# intent — "a pike's point is never zero") instead of flat-topping the polearm class to one identical value and
# erasing the head_len-driven ordering the primitive expresses. The longest reach-thrusts read slightly LOWER
# gap-press authority (grounded: a longer lever presses a harness gap less well).
THRUST_LEVER_REF=0.55; THRUST_LEVER_FLOOR=0.24
def thrust_authority(head_len):
    """Point-to-hand lever -> thrust authority factor in [THRUST_LEVER_FLOOR, 1.0]. Short lever (dagger/half-sword) =
    1.0 (pommel-pressed, body-weight-backed); long reach-thrust decays toward the floor. head_len in METRES."""
    if head_len is None or head_len<=0: return 1.0
    return max(THRUST_LEVER_FLOOR, min(1.0, THRUST_LEVER_REF/head_len))
def cut_thrust_arm(mat, gap_prec=GAP_PREC_REF, eff_cut=None, eff_thrust=None, thrust_auth=1.0, impact=None):
    """SINGLE OWNER of the cut-and-thrust versatility contest. Returns `(value, mode)` — the winning arm's coupling and
    which arm won ('shear' | 'puncture') — so the DAMAGE and the REPORTED MODE can never disagree (ED-PC-0036).

    The coupling and the label are read from this one contest: the cut arm is graded on its OWN token
    (DELIVERY['cut']) and BOTH arms carry the same `eff` quality scaling their standalone tokens use (the derived
    edge-quality and thrust-magnitude of all 19 cut_thrust weapons). The result is the doctrine: CUT the unarmoured
    man, half-sword THRUST anything armoured — and a poor-edged weapon (spetum, eff 0.63 < CUT_AUTH_REF) may prefer its
    point even unarmoured, which an armour-keyed label rule could not express.

    PRICED ON DAMAGE when `impact` is given [ED-PC-0050, E5/M7 — the ratified direction of ED-PC-0036]: `impact` is
    the (shear, puncture) pair from `cut_thrust_impacts`, the Str+Heft each arm is paid. Since E3b a cut_thrust
    weapon's heft differs by arm (the puncture arm takes the axial thrust lever, the shear arm the swing moment), so
    the better-COUPLING arm is not always the more-DAMAGING one; with `impact` the contest compares impact x coupling,
    the product `damage()` pays (its remaining factors are common to both arms, and its penetration knee is monotone),
    so the arm chosen is the arm that does more damage. This MOVES the doctrine above: a hand-balanced sword, whose
    thrust heft exceeds its swing heft, now thrusts the unarmoured man too, and a forward-balanced polearm with a heavy
    swing can cut where its point coupled better. `strike` and `select_mode`'s label call pass `impact`;
    `select_mode`'s cross-head comparator ranks every head on coupling alone and so reaches this contest without it,
    as does a weapon-only probe with no wielder (None keeps the coupling-only contest). The returned value is
    the winning arm's COUPLING either way (impact is paid separately, in `damage`). Pure."""
    cut_arm = DELIVERY['cut']*_transmit('shear',mat)
    thr_arm = DELIVERY['point']*_transmit('puncture',mat,gap_prec=gap_prec,thrust_auth=thrust_auth)
    # PER-ARM quality [ED-PC-0037]. Each arm is de-rated by ITS OWN derived magnitude — the edge by geo['cut'], the
    # point by geo['thrust'] — not by the element's blended sel_eff = max(cut, thrust), which would credit an incidental
    # edge with a dedicated point's quality (a ranseur's cut 0.30 sits squarely inside the 0.20-0.50 band CUT_AUTH_REF's
    # own comment says must never earn the full constant). Per-arm, the ranseur's cut scales to 1.5*0.30/0.70 = 0.643
    # and its point correctly wins (the ED-PC-0011 mis-crediting class, closed here).
    if eff_cut is not None:    cut_arm *= min(1.0, eff_cut/CUT_AUTH_REF)
    if eff_thrust is not None: thr_arm *= min(1.0, eff_thrust/THRUST_AUTH_REF)
    cut_price, thr_price = (cut_arm, thr_arm) if impact is None else (cut_arm*impact[0], thr_arm*impact[1])
    return (cut_arm, 'shear') if cut_price >= thr_price else (thr_arm, 'puncture')

def cut_thrust_impacts(w, strength, grip=0.0, sel_pc=None):
    """(shear, puncture): the Str+Heft impact each arm of a cut_thrust weapon is paid — `strike_impact` on that arm's
    own heft (heft_resp with sel_arm). The `impact` input of `cut_thrust_arm` [ED-PC-0050, E5/M7]. Pure."""
    return tuple(strike_impact(strength, h, V.HEAD_CUT_THRUST)
                 for h in WP.heft_by_arm(w, grip=grip, sel_head=V.HEAD_CUT_THRUST, sel_pc=sel_pc))

def coupling(head, armor, perc=PERC_AUTH_REF, gap_prec=GAP_PREC_REF, eff=None, thrust_auth=1.0, eff_cut=None, eff_thrust=None, ct_impact=None):
    """DELIVERY x transmit. cut_thrust is VERSATILE — takes the better of its edge (shear) or the half-sword thrust
    (puncture/gaps) at each armour level: a longsword half-swords vs plate instead of bouncing (restores the prior
    engine's max(cut,point) mode-shift; HEMA: you half-sword vs harness). [damage_model.coupling + cut_thrust versatility]
    `perc` (percussion authority) scales the blunt transmit vs rigid armour (FIX-1b); ignored for non-blunt heads.
    `gap_prec` (the weapon's derived gap_precision, w['gap']) makes the PUNCTURE/thrust path GAP-SEEKING (the situational
    gap game): a stiff concentrated point defeats plate at the gaps, a whippy one is deflected. Threaded for every
    thrusting head (point + the cut_thrust half-sword thrust); percussion/shear ignore it (a broad blow/cut does not
    gap-seek). Defaults to a neutral point (GAP_PREC_REF); the live path threads the real w['gap'].
    `eff` [U2/ED-PC-0011] scales the 'cut' token's DELIVERY by its own derived edge-quality vs CUT_AUTH_REF, and
    [PC-4/ED-PC-0012] the 'point' token's DELIVERY by its own derived thrust-magnitude vs THRUST_AUTH_REF — see those
    constants' comments. None (the default) means "no scaling" (ratio 1.0); ignored for every head but 'cut'/'point'.
    `thrust_auth` [PC-5/ED-PC-0015] scales the GAP-PRESS term of the puncture path (the 'point' head + the cut_thrust
    half-sword thrust) by the point-to-hand lever authority (thrust_authority(head_len)). It scopes to the gap game vs
    a harness ONLY — a thrust that lands on soft targets (through-material) is untouched, so reach weapons stay lethal
    vs the unarmoured. 1.0 (the default) is neutral; inert for shear/percussion.
    `ct_impact` [ED-PC-0050]: cut_thrust_arm's `impact` pair (price the arm contest on damage); inert for other heads."""
    mat=TIER2MAT[armor]
    if head=='cut_thrust':
        # VERSATILE: better of the edge (shear — a cut is not pommel-pressed, no lever term) or the half-sword/gap
        # thrust (puncture, whose GAP-PRESS term carries thrust_auth — the short-lever pommel-press that defeats a harness).
        # [ED-PC-0036] Both arms carry the SAME `eff` quality scaling their standalone tokens use, so the derived
        # edge-quality and thrust-magnitude of the cut_thrust weapons are not discarded (the "a composite is graded on
        # something other than its own element" class the sel_* contract exists to prevent). A weak edge de-rates the
        # cut arm and a weak point the thrust arm, so the max() is a contest between the weapon's REAL two
        # capabilities instead of between two hand-set DELIVERY constants.
        # The cut arm is graded as a CUT (DELIVERY['cut']), not by a blended 'cut_thrust' constant: a cut-and-thrust
        # sword's cut IS a cut and has no reason to be weaker than a dedicated cutter's. On its own token the shift is
        # REAL and matches the doctrine stated above: cut the unarmoured man (1.500 > 1.450), half-sword-thrust anything
        # armoured — because padding and plate resist an edge far more than they resist a point.
        return cut_thrust_arm(mat, gap_prec, eff_cut, eff_thrust, thrust_auth, impact=ct_impact)[0]
    d=DELIVERY.get(head,1.5)
    if head=='cut' and eff is not None:
        d*=min(1.0, eff/CUT_AUTH_REF)
    elif head in (V.HEAD_STRAIGHT_CUT, V.HEAD_CURVED_CUT) and eff is not None:
        # [A7a channel 1 / M6, ED-PC-0051] NATIVE edge quality, finally consumed. `eff` here is
        # geometry.cut_factor = edge_keenness * (1 + 0.45*tanh(2*curvature)) — so Jordan's "the curve extends the
        # amount of cutting edge with which to do damage" is ALREADY in this number; the geometry layer computed it
        # and this function discarded it. Nothing new is invented here, a derived value is stopped from being thrown
        # away. Non-saturating (see CUT_REF_NATIVE): a superior edge is a BENEFIT, not merely a smaller penalty —
        # which is why re-anchoring the old min(1.0, ...) form could not have fixed this, since a cap can only ever
        # penalise a population that is already losing.
        rel = eff/CUT_REF_NATIVE
        d *= (1.0 + (rel-1.0)*_shear_yield(mat)) if rel >= 1.0 else rel
    elif head=='point' and eff is not None:
        d*=min(1.0, eff/THRUST_AUTH_REF)          # PC-4/ED-PC-0012: scale a POINT token by its own derived thrust magnitude — a weak incidental point on a slasher is not a dedicated thruster; native pointers (eff>=bear_spear 0.53) clamp to 1.0, unaffected
    return d*_transmit(HEAD_MODE.get(head,'shear'),mat,perc,gap_prec,thrust_auth=thrust_auth)
def _puncture_adef(w, cfg, grip, room):
    """SINGLE OWNER of the percussion-driven puncture armour-defeat term: a concentrated beak/spike defeats a harness
    by the ENERGY behind it, scored against ADEF_PERC_REF. Used by adef_cap's native-blunt max() and (ED-PC-0049) the
    blunt-composite selected-spike branch (§8 'every rule lives once'). Pure."""
    return cfg['ADEF_POINT']*(WP.puncture_pressure(w, grip=grip, room=room)/cfg['ADEF_PERC_REF'])


def adef_cap(w, cfg, head=None, gap=None, grip=0.0, room=1.0):
    """The aggressor head's RAW armour-defeat CAPABILITY (head-based, armour-tier-independent): the best mode its head
    can deliver vs a harness. Consumed by armor_defeat_sigma (vs the per-tier threshold) AND reach_threat (the FIX-1
    deficit). Blunt = the BETTER of CONCUSSION (broad percussion authority — a mace dents the harness) or PUNCTURE (a
    concentrated beak/spike that pierces plate — the poleaxe queue); both DERIVED:
    concussion~percussion_authority, puncture~percussion_authority x strike_concentration (a broad
    mace face sc~0 -> no puncture; a spike sc high -> pierces). A wooden staff (low authority) does NEITHER. A
    cut-and-thrust sword takes the better of its cut or a half-sword gap-thrust; a point thrusts to gaps; a pure
    cutter collapses (ADEF_CUT).

    `head` (the SELECTED mode-head from select_mode) overrides w['head'] when the wielder has committed to a specific
    mode this exchange: a poleaxe whose select_mode chose 'point' (the spike) is scored on the spike's gap-thrust, not
    the better-of-blunt max. head=None keeps the native head (the per-head max over the weapon's intrinsic modes) — so
    every existing caller is unaffected. percussion_authority carries the §1 energy-credit (the poleaxe's plate edge
    is NOT concussion; see select_mode).
    CIRCUMSTANCE-DEGRADED (I2, D2b): `gap` overrides w['gap'] (None = native fallback — the sel_gap object-
    confusion fix, M-02); `grip`/`room` thread the SAME mode-split/room-floored Phi as the damage path into the
    blunt branch's percussion_authority/puncture_pressure, so armour-defeat capability and reach_threat resolve
    the SAME grip as core.strike (D2b). Unchanged at grip=0/room=1.0/gap=None."""
    head = head if head is not None else w['head']
    gap = gap if gap is not None else w['gap']
    tauth = thrust_authority(w['head_len'])   # PC-5: point-to-hand lever authority — scales the gap-THRUST armour-defeat terms (a short/half-sword thrust presses the harness; a reach-thrust at extension cannot), keeping adef consistent with coupling. NOT applied to the blunt-puncture beak (a poleaxe's spike authority is its percussion energy, already in puncture_pressure) nor to the pure-cut collapse.
    if head=='blunt':
        return max(cfg['ADEF_BLUNT']*(WP.percussion_authority(w, grip=grip, room=room)/cfg['ADEF_PERC_REF']),
                   _puncture_adef(w, cfg, grip, room))
    if head=='point':
        if w['head']=='blunt':
            # [ED-PC-0049, E3a] THE BLUNT-COMPOSITE SPIKE. `tauth` is a point-to-hand LEVER de-rating: a reach-thrust
            # delivered at full extension cannot press a harness the way a short/half-sword thrust can. That grounding
            # does not describe a two-handed percussive blow driving a concentrated spike — the exemption "NOT applied to
            # the blunt-puncture beak (a poleaxe's spike authority is its percussion energy, already in
            # puncture_pressure)" above also covers the branch where select_mode has committed the weapon to its
            # spike, which is exactly when the spike is the thing being scored. Two rules, one principle: the spike is
            # not lever-de-rated, and it keeps access to the percussion-driven puncture path the blunt branch computes
            # on the line above (a beak defeats plate by the energy behind it, not by gap precision alone), so
            # armor_defeat_sigma does not read plate as SHIELDED against a poleaxe on the mode select_mode itself picks
            # (ED-1080's "set so the poleaxe spike adef ~= its hammer" calibration).
            # SCOPED to native-blunt: a spear/rapier/yari reach-thrust is still de-rated, which is what PC-5 is for.
            # Reaches all four blunt-composites (poleaxe, bec_de_corbin, lucerne_hammer, goedendag) at every tier where
            # select_mode commits them to the spike (bec_de_corbin takes its hammer at heavy; lucerne_hammer and
            # goedendag take the hammer from medium up).
            return max(cfg['ADEF_POINT']*gap, _puncture_adef(w, cfg, grip, room))
        return cfg['ADEF_POINT']*gap*tauth
    if head=='cut_thrust': return max(cfg['ADEF_CUT'], cfg['ADEF_POINT']*gap*tauth)   # cut OR half-sword gap-thrust (the thrust term pressed home by the short lever)
    return cfg['ADEF_CUT']                                                            # straight/curved pure cut collapses

def adef_deficit(cap, cfg, armor):
    """How far an armour-defeat CAPABILITY falls short of `armor`'s ADEF_THRESHOLD, floored at 0 on BOTH sides [ED-PC-0039, ED-PC-0046]. `adef_cap`
    returns a NEGATIVE number for a pure cutter (ADEF_CUT = -0.9): a sigma-domain CONTROL PENALTY for armor_defeat_sigma's +/- scale (which keeps the
    raw signed cap), not a capability magnitude. Every DEFICIT clamps it at zero capability first, since 'cannot defeat the harness' is a floor, not
    an unbounded negative: raw, it would inflate the bardiche's medium deficit threefold, inflate damage()'s knee roughly tenfold and crowd it
    off measure in represent_measure_p. Pure."""
    return max(0.0, cfg['ADEF_THRESHOLD'][armor] - max(0.0, cap))

# ── primitive-emergent USE-MODE selection (the per-exchange technique choice) ───────────────────────────────────
# grounded_weapon_armour_usemode_model.md §3-4 (tasks wht7pkx1c / w4bekmb5e). There is NO per-weapon mode table:
# the AFFORDED modes + their effectiveness DERIVE from each weapon's existing geometry primitives, so poleaxe/mace/
# staff are just bundles of primitives, never a name-keyed list (the L0 primitive-law). The modes are the UNIVERSAL
# set {thrust, cut, percuss, puncture}; each maps to one of the engine's existing head TOKENS (so the downstream
# coupling/adef/legibility machinery is unchanged) and one DAMAGE mode. The wielder greedily SELECTS the afforded
# head whose resulting damage-coupling vs THIS armour is highest — generalizing the existing cut_thrust max() and the
# blunt max(concussion,puncture) from 2 modes to N. Pure.
def strike_impact(strength, heft_units, weapon_head, perc=PERC_AUTH_REF):
    """The Str+Heft IMPACT term of `damage` — its single owner, so `cut_thrust_impacts` prices the cut_thrust arm
    contest on exactly what `damage` pays (ED-PC-0050). Strength is weighted by the head (`K_STR_HEAD`, PC-20 (1)).
    Pure."""
    heft = 3.0*(perc/PERC_AUTH_REF) if weapon_head=='blunt' else HEFT_HEAVY*heft_units   # blunt heft is percussion-authority-continuous; cut/thrust/point heft_units is WP.heft() (Phase B6), normalised to 1.0 at the longsword anchor -> HEFT_HEAVY*1.0 reproduces the old heavy-class magnitude there
    # ED-PC-0042 rider I1b: the denominator routes through the owned anchor (PERC_AUTH_REF). The NUMERATOR 3.0 is the
    # blunt branch's damage-scale magnitude, numerically equal to HEFT_HEAVY (`core.HEFT_HEAVY`) but not established as
    # the same constant — whether "blunt heft at full authority" IS the heavy cut/thrust class, or merely coincides
    # with it, is an unresolved design question (value-collision reasoning, CLAUDE.md §7, would not settle it).
    return K_STR_HEAD[weapon_head]*strength + heft              # additive force (damage_model design: Str+Heft)

def damage(deg, heft_units, weapon_head, strength, armor, gap=GAP_PREC_REF, perc=PERC_AUTH_REF, q=None, eff=None, thrust_auth=1.0, eff_cut=None, eff_thrust=None, weapon_geo=None, cfg_adef=None, grip=0.0, room=1.0, ct_impact=None):
    """Linear: (K_STR_HEAD[head]*strength+heft) x Coupling x Quality x DMG_SCALE — no tanh/cap. perc carries P_auth; blunt heft
    continuous from it. DMG_SCALE (above) is the single damage-scaling knob. `gap` (the weapon's derived
    gap_precision, w['gap']) threads into coupling's puncture path (the situational gap game): the SELECTED thrust's
    plate-defeat scales with how well the point finds+holds a gap (a stiff spike/rondel defeats plate at the gaps; a
    whippy point is deflected). Non-thrusting heads ignore it (percussion/shear do not gap-seek), so it is inert for a
    blunt/cut blow. `eff` [U2/ED-PC-0011] is the SELECTED element's own derived cut/thrust magnitude — threaded into
    coupling's DELIVERY scaling (the 'cut' token only, see CUT_AUTH_REF); it does NOT touch `heft` above, which
    stays the separate weight-class quantity (WP.heft()).
    `ct_impact` [ED-PC-0050] is the cut_thrust arm contest's (shear, puncture) impact pair, passed through `coupling`
    to `cut_thrust_arm` so the coupling paid here is the arm `strike` priced on damage; None for every other head."""
    if deg not in ('graze','success','overwhelming'): return 0
    qf = q if q is not None else QUAL[deg]
    impact = strike_impact(strength, heft_units, weapon_head, perc)
    raw = impact * coupling(weapon_head, armor, perc=perc, gap_prec=gap, eff=eff, thrust_auth=thrust_auth, eff_cut=eff_cut, eff_thrust=eff_thrust, ct_impact=ct_impact) * qf * DMG_SCALE   # FIX-1b: perc scales blunt transmit vs rigid armour; gap: the situational gap game (thrust seeks the reach-ladder gaps); eff: the 'cut' token's own edge-quality scaling; thrust_auth (PC-5): the point-to-hand lever authority
    # PENETRATION THRESHOLD (ED-PC-0032), CAPABILITY-RELATIVE (ED-PC-0038). The knee keys on the weapon's armour-defeat
    # capability, not RAW magnitude alone, which would let a heavy-headed weapon buy its way through a harness it
    # demonstrably cannot defeat (a guandao's adef_cap sits far below a spear's against plate): the damage path
    # would reward head mass exactly where the sigma path says the weapon cannot find a gap, which is both physically
    # inverted (a narrow point seeks a gap better than a broad blade) and a silent contradiction of the armour-defeat
    # model the rest of the engine resolves on. The threshold RISES with the weapon's own armour-defeat DEFICIT, so
    # what gets through a harness is governed by whether the weapon can defeat it — not by how heavy its head is.
    # Zero deficit (a weapon that clears the tier) leaves the ED-PC-0032 threshold, and every tier with PEN_THR 0
    # (none/light) stays completely inert.
    t = PEN_THR.get(armor, 0.0)
    if t > 0.0:
        _cap = (adef_cap(weapon_geo, cfg_adef, head=weapon_head, gap=gap, grip=grip, room=room)
                if (weapon_geo is not None and cfg_adef is not None) else None)
        if _cap is not None:
            t *= (1.0 + PEN_DEFICIT_K * adef_deficit(_cap, cfg_adef, armor))   # the clamp, and why, live in adef_deficit
    if t > 0.0 and raw > 0.0:
        raw *= (raw*raw) / (raw*raw + t*t)                       # soft knee: a sub-defeat blow inflicts little LASTING wound (deflected); a defeating blow (large raw) keeps ~all
    return max(0, int(round(raw)))

def strike(attacker, defender, deg, cfg, net=None, pool=None):
    """Role-object damage convenience: reads weight/head/strength/gap/percussion off the ATTACKER and armour off the
    DEFENDER, returning the int damage. Single call-site for every blow so the 9-arg positional surface (the
    transposition-bug class) exists in exactly one place. Takes role objects (never raw A/B), consistent with the
    subsystem contract. `cfg` rides to `damage` as `cfg_adef`, where the penetration knee reads `ADEF_THRESHOLD` and
    `adef_cap` the `ADEF_*` weights (ED-PC-0039); `strike` itself reads none.
    CIRCUMSTANCE-DEGRADED (I2, D2/D2b/D5 — BLOCKER-2 + M-02): `gap`/`perc` read the SELECTED element's
    OWN sel_gap/sel_perc (systems.select_mode's return, threaded onto the attacker by the wrapper),
    native whole-weapon fallback only when unset — the canonical single source of truth (a composite routed to a
    blunt sub-element is damaged on THAT element's percussion, not the whole-weapon value). `heft_resp` reads the
    attacker's current grip_position + the selected head/pc so the thrust-protected, mode-split Phi_grip degrades
    the SAME grip the wielder actually holds."""
    q=None
    if net is not None and deg=='overwhelming':                  # M-QUAL: sigma-leverage tail (canonical sigma_n + tanh)
        # severity beyond the overwhelming bar THIS roll was banded at: the owner's edge at the defender's Ob (PC-03).
        # Every caller banded its roll at ob_from_defender(defender) of this same `defender` (wrapper: the exchange,
        # the stop-hit, the pursuit).
        z=max(0.0,(net-band_floor('overwhelming', ob_from_defender(defender)))/SL.sigma_n(pool))
        q=1.5+(OW_MAX-1.5)*tanh(z/OW_Z)
    head=getattr(attacker, 'sel_head', None) or attacker.head    # the SELECTED use-mode head (systems.select_mode, set by the wrapper); falls back to the native head
    gap=getattr(attacker, 'sel_gap', None); gap = gap if gap is not None else attacker.w['gap']
    perc=getattr(attacker, 'sel_perc', None); perc = perc if perc is not None else WP.percussion_authority(attacker.w)
    eff=getattr(attacker, 'sel_eff', None)                        # SELECTED element's own derived cut/thrust magnitude (U2/ED-PC-0011); None for a native-fallback attacker, inert for every head but 'cut'
    grip=getattr(attacker, 'grip_position', 0.0); sel_pc=getattr(attacker, 'sel_pc', None)
    tauth=thrust_authority(attacker.w.get('head_len'))            # PC-5: point-to-hand lever authority from the SELECTED weapon record (the half-sword swap already gives the short-lever form its own head_len); inert for shear/percussion heads
    # [ED-PC-0037.1] ELEMENT-LOCAL per-arm magnitudes, written by the wrapper from systems.selected_arm_magnitudes.
    # The whole-weapon bake is only a fallback for callers that never went through select_mode (direct/test callers):
    # grading a composite's blow on the WEAPON's cut/thrust rather than the struck ELEMENT's is the M-02 object
    # confusion the sel_* contract exists to prevent.
    _geo = attacker.w.get('geo', {})
    _ec = getattr(attacker, 'sel_eff_cut', None);  _et = getattr(attacker, 'sel_eff_thrust', None)
    # [ED-PC-0050, E3b] Resolve the cut_thrust ARM before pricing heft, through cut_thrust_arm — the SINGLE OWNER of
    # the versatility contest (ED-PC-0036), never a second copy of the comparison. A composite that resolves the
    # puncture arm must be paid the axial thrust lever, not the swing moment. None for every other head.
    # [ED-PC-0050, E5/M7] The contest is priced on DAMAGE: `_imp` is the Str+Heft each arm is paid, and the same pair
    # rides into damage() -> coupling() -> cut_thrust_arm, so the coupling paid is the arm chosen here.
    if head == V.HEAD_CUT_THRUST:
        # both arms' heft in ONE grip evaluation (WP.heft_by_arm); the impact pair and the paid heft come from it
        _hefts = WP.heft_by_arm(attacker.w, grip=grip, sel_head=head, sel_pc=sel_pc)
        _imp = tuple(strike_impact(attacker.strength, h, head) for h in _hefts)
        _arm = cut_thrust_arm(TIER2MAT[defender.armor], gap,
                              eff_cut=(_ec if _ec is not None else _geo.get('cut')),
                              eff_thrust=(_et if _et is not None else _geo.get('thrust')),
                              thrust_auth=tauth, impact=_imp)[1]
        _heft = _hefts[0] if _arm == V.MODE_SHEAR else _hefts[1]
    else:
        _imp = None
        _heft = heft_resp(attacker.w, cfg, grip=grip, sel_head=head, sel_pc=sel_pc)
    return damage(deg, _heft, head, attacker.strength,
                  defender.armor, gap, perc, q=q, eff=eff, thrust_auth=tauth,
                  eff_cut=(_ec if _ec is not None else _geo.get('cut')),
                  eff_thrust=(_et if _et is not None else _geo.get('thrust')),
                  weapon_geo=attacker.w, cfg_adef=cfg, grip=grip, room=getattr(attacker,'range_avail',1.0),
                  ct_impact=_imp)   # [ED-PC-0039] same grip/room the sigma path threads, so the two cannot disagree about the same question
