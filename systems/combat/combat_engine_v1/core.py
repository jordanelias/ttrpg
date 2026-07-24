"""Core engine module — canonical resolution primitives. Single source for ob/degree/roll/damage.
Resolves the sigma kernel through engine.autoload.sigma_leverage (the numpy-free single source,
Stage 1a / D0-2) so every subsystem resolves identically. No A/B knowledge here.

[ED-1085 container de-leak, 2026-07-01] This module previously reached into the FROZEN
tests/sim/v32-combat-balance/ validation station via a sys.path hack (r1/r8/m1 imports),
dragging numpy into the engine runtime. The sigma math now comes from sigma_leverage
(parity-tested against the numpy originals at 1e-9 — sim/tests/test_sigma_leverage_parity.py);
the engine's own combat-state constants live here / in combatant.py. NOTE the RNG contract
changed with the substrate: `rng` is a stdlib random.Random (rng.gauss), no longer a numpy
Generator (rng.normal). The continuous engine's distribution is unchanged
(Normal(mu*N, sigma*sqrt(N)), same per-die TN table)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)          # resolve the sim.* shared-service layer (autoload)
from math import tanh, exp
from engine.autoload import sigma_leverage as SL

# ---------- logistic (single source, ED-PC-0025) ----------
# The 1/(1+e^-x) squash was open-coded FIVE ways across the resolver (combat_systems.bind_dominance_p /
# disrupt_resist_p / the two read-contest sites, contact.grab_outcome) — a §8 "every rule lives once"
# violation AND an overflow hazard: a grossly out-of-contract net-sigma (e.g. an attribute/skill orders of
# magnitude past the legal ceiling of 5) drives `exp(-x)` past the float range and CRASHES fight resolution
# with OverflowError (combinatorial-audit finding: strength/skills=50000 -> 99/300 fights crash). Measured
# legal-build |argument| never exceeds ~2.4 (n=2500 fights, all weapon/armour/tradition mixes), so the clamp
# below sits ~200x outside any reachable value — BYTE-IDENTICAL for every legal build, guarding pathology
# only ("every build available" without crashing the engine on out-of-contract inputs). Pure.
_LOGISTIC_CLAMP = 500.0   # exp(500) is finite (< 1e218); exp(710)+ overflows. Legal max |arg| ~2.4.
def logistic(x):
    """Numerically-safe logistic squash 1/(1+e^-x) -> (0,1). Clamps the argument to [-500, 500] so an
    out-of-contract net-sigma cannot overflow exp() and crash resolution; unchanged for all in-contract x."""
    if x < -_LOGISTIC_CLAMP: x = -_LOGISTIC_CLAMP
    elif x > _LOGISTIC_CLAMP: x = _LOGISTIC_CLAMP
    return 1.0 / (1.0 + exp(-x))
import weapon_physics as WP   # Phase-3 consolidation: percussion authority lives ONCE in WP (the credited derived value);
                              # core.strike reads WP.percussion_authority (the sigma path systems.adef_cap already does),
                              # retiring the duplicate core.p_auth that read the hand-set pob_frac. WP imports only math
                              # at module scope (cycle-free), so this import is safe.

DECISIVE_OB = 3    # [canonical: combat_v30 §5 degree band centre (decisive sub-action Ob); relocated verbatim from the frozen r8 harness, ED-1085]
TN = SL.TN_STANDARD
POOL_FLOOR = 5     # [canonical: params/core.md §Derived Scores (Combat Pool min 5)]
BASE_POOL = 6      # [class-C: armature — History-driven pool base; pool = max(5, History+6), ED-901; relocated verbatim from r1, ED-1085]

def resolution_pool(history):
    """Agility-INDEPENDENT resolution pool (ED-901; re-ratified ED-900/904): max(5, History + 6)."""
    return max(POOL_FLOOR, int(round(history)) + BASE_POOL)
def effective_ob(pool, net_sigma): return SL.eff_ob(DECISIVE_OB, pool, net_sigma)
def roll_net(pool, rng): return SL.roll_net_continuous(pool, TN, rng=rng)
def degree(net, ob):
    """Band a CONTINUOUS net into a degree, with the ER-2 continuity correction applied (params/core.md
    §Continuous Engine, commit a3d3888 — landed in canon TEXT, never propagated to engine CODE until now).
    The continuous net approximates a sum of integer per-die effects, so each integer degree threshold k is
    read at the k-0.5 boundary; without it the continuous read ran 5-9pp LOW across the whole 5-13D combat
    band (NERS R+S fail, 2026-06-23 critique). Self-contained here (NOT routed through the harness degree_of_success)
    so the DISCRETE/TTRPG path r1 serves stays exactly net>=k. [AUDIT-FIX — re-sweep Class-C calibration.]"""
    if net < 0.5: return 'fail'                                   # discrete net <= 0
    if net >= 2*ob - 0.5 and net >= 2.5: return 'overwhelming'    # discrete net >= 2*ob AND net >= 3
    if net >= ob - 0.5: return 'success'                          # discrete net >= ob
    return 'partial'                                              # discrete 1 <= net < ob

def resolve(pool, net_sigma, rng):
    """Canonical mu-shift resolution (sigma_leverage_handoff §1): base Ob fixed at DECISIVE_OB; the sigma-leverage
    boosts the ROLL (boost = eff_sigma*sigma_N = soft_cap(net_sigma)*sigma_n(pool)), it does NOT shift the Ob.
    SL.eff_ob is display-only per its own docstring; resolving via the floored Ob-shift distorted the degree
    bands (overwhelming trivialised by the Ob-floor). Returns (deg, net)."""
    net = roll_net(pool, rng) + SL.soft_cap(net_sigma) * SL.sigma_n(pool)
    return degree(net, DECISIVE_OB), net

# ---- damage (Impact x Coupling x Quality) — CONTINUOUS transmission, NO tanh saturation ----
# Adopts the ground-up linear damage model [damage_model.py / damage_model_design, Jordan 2026-05-30,
# ratified 2026-06-17]: damage = Impact x Coupling x Quality, NO cap/tanh, so head/strength/armour drive
# damage as a live gradient (the old tanh cap saturated everything to ~the cap and flattened the gradient).
#   Impact   = strength + heft; BLUNT heft is CONTINUOUS from percussion authority P_auth (perc carries it);
#              cut/thrust heft is weight-class (continuous-mass cut-impact deferred, plan #9).
#   Coupling = DELIVERY(head) x transmit(material-resistance-per-mode) x gap(coverage) — material/mode physics.
#   Quality  = degree factor.   Constants from damage_model (emergent-calibrated so an even Success ~= 1 WI).
HEFT_HEAVY=3.0                                                      # heavy-class cut/thrust heft scale (unchanged — the multiplier below anchors on the SAME 2H cut-thrust reference WP.heft() normalises to 1.0)
def heft_resp(w, cfg, grip=0.0, sel_head=None, sel_pc=None):
    """Continuous weapon heft response (heft-units) — morphology-rearch Phase B6: DERIVED from weapon_physics.heft()
    (striking mass × forward-balance, normalised so the longsword anchor reads 1.0), replacing the binary
    wt{light,heavy} class outright. No more HEFT_MODE toggle — there is no fiat category left to reproduce in
    'binary' mode. `cfg` is kept for call-site compatibility (unused; the derivation is pure).
    CIRCUMSTANCE-DEGRADED (I2, D2): threads grip/sel_head/sel_pc into WP.heft's mode-split Phi_grip — byte-
    identical at grip=0 (the default) for every weapon."""
    return WP.heft(w, grip=grip, sel_head=sel_head, sel_pc=sel_pc)
QUAL={'graze':0.25,'partial':0.5,'success':1.0,'overwhelming':1.5}  # [damage_model QUALITY base; overwhelming = sigma-leverage tail floor]
OW_MAX=2.5; OW_Z=1.5          # [M-QUAL D-A: overwhelming quality saturates 1.5->OW_MAX by sigma-leverage severity]
DMG_SCALE=1.55                                                      # [damage_model — even Success ~= 1 WI; emergent-tunable]
# PENETRATION THRESHOLD (ED-PC-0032, rapier plate fall-off): armour resists up to a floor — a blow whose coupling-
# reduced impact does not clear the tier's resistance inflicts little LASTING WOUND (it is stopped/deflected), so a
# weapon that CANNOT defeat the harness cannot win by VOLUME of sub-penetration pokes (the rapier's inverted field
# curve: field-win was RISING with armour because many fast light hits accumulated on plate). Applied as a SOFT knee
# on the post-coupling damage: eff = d · d²/(d²+PEN_THR²) — a blow at the threshold keeps half, well above keeps ~all,
# well below collapses toward 0. Unarmoured PEN_THR=0 (knee inert → open combat byte-identical). Emergent, not a
# rapier special-case: a gap-dagger/spike/blunt that DEFEATS plate produces a large d (kept); a rapier/arming/spear
# point that pings off it produces a small d (collapsed). [SIM-CALIBRATE] per-tier floors.
PEN_THR={'none':0.0,'light':0.0,'medium':2.5,'heavy':6.5}   # light (soft gambeson) needs no penetration floor; the rapier inversion is a HEAVY-tier effect (heavy 74->16), medium a smaller gate
HEAD_MODE={'blunt':'percussion','point':'puncture','cut_thrust':'shear','straight_cut':'shear','curved_cut':'shear','cut':'shear'}
DELIVERY={'blunt':1.6,'point':1.45,'cut_thrust':1.35,'straight_cut':1.5,'curved_cut':1.5,'cut':1.5}  # [damage_model head delivery]
# Material resistance per mode in [0,1] (resist; transmit = 1-resist). GROUNDED 2026-06-30 (Alan Williams, The Knight
# and the Blast Furnace, 2003) — designs/audit/2026-06-30-combat-grounding/. CHANGED 4 cells: cloth.shear .35->.45
# (a 16-30 layer jack sheds a ~60-130 J cut); cloth.puncture .15->.12 (a point stops at only ~50 J vs ~80 J cut — the
# documented cut>>point asymmetry); cloth.percussion .10->.12 (modest standalone blunt absorption); mail.shear .80->.85
# (cutting riveted mail is "functionally impossible," >130 J ceiling). Plate row + mail perc/punc KEEP (well-pinned).
# [CI — DESIGNER-SET/UNSOURCED: the cloth fractions are a designer normalisation of Williams' joules onto the 0-1 scale,
#  NOT a Williams figure.]  [PACKAGE: plate.percussion .30 is honest ONLY with the FIX-1b authority gate below — never
#  tune one without the other (ungated, an honest plate-vs-blunt resist is ~.55-.65).]  Assumes RIVETED mail + HARDENED
# ~2mm plate (butted mail / wrought iron are far weaker — not modelled).
RESIST={'none': {'percussion':0,   'shear':0,   'puncture':0},
        'cloth':{'percussion':.12, 'shear':.45, 'puncture':.12},
        'mail': {'percussion':.20, 'shear':.85, 'puncture':.45},
        'plate':{'percussion':.30, 'shear':.95, 'puncture':.70}}
TIER2MAT={'none':'none','light':'cloth','medium':'mail','heavy':'plate'}  # [armour_axes presets — tier->material]
COVERAGE_GAP={'full':0.15,'partial':0.5}                            # [damage_model — gap/bare-zone exposure]
# ── SITUATIONAL GAP GAME (2026-06-30) — a thrust/puncture is GAP-SEEKING ─────────────────────────────────────────
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
GAP_PREC_REF=0.65                                                   # neutral gap_precision default for the puncture path (a mid-roster point) — the LIVE combat path always THREADS the weapon's real w['gap'] (systems.select_mode / core.strike), so this default only guards a hypothetical unthreaded caller.
# FIX-1b [FIAT — no melee-speed behind-plate data exists; ballistic BABT is the wrong regime, per Phase-3 grounding]:
# percussion transmitted through RIGID armour (mail/plate) scales with the blow's percussion AUTHORITY — a steel
# hammer (p_auth 8) overwhelms the armour's impact-spread; a wooden staff (p_auth ~4) is largely absorbed. The TRANSMIT
# term is LINEAR in (perc/PERC_AUTH_REF) (E=1.0, momentum-like). It COMPOUNDS with the pre-existing blunt heft
# (3·perc/8 in damage()), so the net blunt-vs-rigid damage scales ~perc² in authority — force and through-armour
# transmission are distinct physics, both authority-dependent (intended). Soft cloth absorbs by deformation
# (~authority-independent) so it is unscaled. perc=PERC_AUTH_REF = full transmission. Magnitude is FIAT. NOTE: FIX-1b
# is a damage-LETHALITY reduction only — it does NOT touch the sigma/reach/control path that drives the staff's
# vs-plate WIN-RATE (that is FIX-1's job); the staff-vs-arming heavy win-rate is ~flat under this change alone.
# EXTENDED TO EVERY MATERIAL (U2/ED-PC-0011, 2026-07-08): the `mat in ('mail','plate')` restriction hid the
# authority scaling entirely against cloth/none. This was invisible pre-U2 because percussion_authority hard-
# zeroed for every non-blunt head, so 'blunt' candidates were ALWAYS dedicated blunt weapons — the gate never
# had a weak candidate to discriminate. Once weapon_physics.reversed_grip_percussion (ED-PC-0009) introduced a
# genuinely WEAK percussion candidate (~1.4-1.8/8 for a two-handed sword's Mordhau option) as a competitor in
# select_mode's greedy comparator, the gap surfaced directly: DELIVERY['blunt']=1.6 (the highest fixed constant
# of any token) let a weak pommel-strike win selection against UNARMOURED targets purely on the delivery
# constant, with `perc`'s actual magnitude never read at all for cloth/none — backwards from the HEMA sourcing
# (Mordhau is a response to armour defeating the edge, not a general preference). Removing the material
# restriction on WHETHER the scaling applies (it now applies vs none/cloth too) is correct; but a first attempt
# also collapsed the two material classes onto ONE reference constant, which an adversarial review caught as
# wrong: PERC_AUTH_REF=8.0 (mace's own exact value) is the reference the ORIGINAL mail/plate-only FIX-1b was
# already calibrated and tested against (poleaxe's spike-vs-plate gap game relies on poleaxe's blunt being
# SOMEWHAT weaker than mace's there, ratio 7.61/8.0=0.952 — pre-existing, untouched, must not change); but that
# SAME 8.0 reference applied to none/cloth (which had NO scaling at all before U2) needlessly discounts every
# dedicated hammer-class weapon that isn't mace itself, and for bec_de_corbin/lucerne_hammer even FLIPS their
# selected mode away from their own hammer face at the unarmoured tier (backwards — their hammer face should
# win vs bare flesh; the spike is specifically for defeating armour, not a general preference). The two
# material classes need DIFFERENT references: mail/plate keeps PERC_AUTH_REF=8.0 UNCHANGED (preserves the
# pre-existing, already-tested calibration exactly); none/cloth uses the lower PERC_AUTH_REF_SOFT=6.5, anchored
# on the WEAKEST attested genuinely-dedicated hammer-class weapon (bec_de_corbin, 6.51 via the live per-element
# percussion path) rather than the strongest (mace) — every dedicated weapon (mace 8.0, goedendag 8.0, poleaxe
# 7.61, lucerne_hammer 7.05, bec_de_corbin 6.51) then clamps to ratio=1.0 at none/cloth (byte-identical to the
# pre-U2 unscaled behaviour there, verified directly across all four), while the Mordhau candidates (1.4-1.8,
# a 4.7-point gap below bec_de_corbin with zero overlap) still score 0.22-0.28 — correctly discounted, losing
# to a weapon's own cut/thrust at low armour and only competitive vs rigid armour it cannot otherwise defeat.
PERC_AUTH_REF=8.0; PERC_AUTH_REF_SOFT=6.5; PERC_TRANSMIT_FLOOR=0.35
def _transmit(mode, mat, coverage, perc=PERC_AUTH_REF, gap_prec=GAP_PREC_REF, thrust_auth=1.0):
    t=1.0-RESIST[mat][mode]
    if mode=='puncture':                                           # SITUATIONAL GAP GAME: a thrust takes through-
        # material OR the reach-ladder gap it seeks. The gap term is GAP-SEEKING: the material's thrust-accessible gap
        # fraction (GAP_EXPOSURE) scaled by the WEAPON's derived gap_precision (a stiff concentrated point finds+holds
        # the gap; a whippy point deflects). Replaces the old fixed COVERAGE_GAP floor — plate is no longer a flat 0.15
        # for every point; the poleaxe spike / rondel now beat the through-material 0.30, the rapier's whippy point does
        # not. Emergent in gap_prec (= w['gap']); no weapon name.
        # PC-5 (ED-PC-0015): thrust_auth (point-to-hand lever authority) scales the GAP-PRESS term ONLY — pressing a
        # point INTO a harness gap is exactly the pommel-backed short-lever act (Fiore/Talhoffer half-sword, the rondel
        # to the visor); a long reach-thrust at extension cannot press the same way. The THROUGH-MATERIAL term `t` is
        # NOT scaled: a thrust that lands on flesh/cloth (none/cloth: t=1.0/0.88) is lethal regardless of lever — reach
        # weapons stay deadly vs soft targets, they only lose the GAP-penetration edge vs mail/plate. Inert at
        # thrust_auth=1.0 (short-lever/half-sword/dagger) — byte-identical to before this parameter existed.
        return max(t, GAP_EXPOSURE[mat]*gap_prec*thrust_auth)
    if mode=='percussion':                                          # FIX-1b, extended U2/ED-PC-0011: authority-scaled
        ref = PERC_AUTH_REF if mat in ('mail', 'plate') else PERC_AUTH_REF_SOFT   # rigid armour keeps the original, pre-existing reference; none/cloth uses the softer one (see comment above)
        t*=max(PERC_TRANSMIT_FLOOR, min(1.0, perc/ref))
    if mat!='none':
        g=COVERAGE_GAP[coverage]; return t*(1-g)+1.0*g             # some blows reach a bare zone
    return t
# CUT_AUTH_REF [U2/ED-PC-0011, 2026-07-08]: the bare 'cut' token key is NEVER a weapon's own native head —
# verified against the full roster (top-level `head` and every mode_element's `head`): no weapon is authored
# as native 'cut' (dedicated cutters use 'straight_cut'/'curved_cut', which this constant does NOT touch).
# The 'cut' key is populated ONLY by systems.element_afforded's graded secondary-affordance check (a weapon
# whose NATIVE head is something else — point/blunt/etc — but whose geometry also clears a real-edge floor).
# Without scaling, an incidental edge (rapier geo['cut']=0.30, dangpa=0.30, main_gauche=0.30) is credited with
# the SAME DELIVERY['cut']=1.5 as a dedicated cutting sword — high enough to beat a native point's DELIVERY
# (1.45) purely on the constant, regardless of how weak the incidental edge actually is (verified: rapier's own
# native 'point' loses to its incidental 'cut' at 'none' armour with no scaling). Anchored — per the same
# principle as PERC_AUTH_REF above — on the WEAKEST attested genuinely-dedicated cutter in the roster
# (hook_sword, curved_cut, geo['cut']=0.710), not a roster-wide average/median (a self-referential statistic
# with no independent grounding): every native straight_cut/curved_cut token sits at or above this floor by
# construction, so anchoring here is a lower-bound safety margin, not a curve-fit. 0.70 sits just below
# hook_sword's exact value; every incidental secondary-cut candidate found in the roster (0.20-0.50) sits
# clearly below it with no overlap. Scoped to the 'cut' token ONLY — 'point' does not need an analogous
# scaling: DELIVERY['point']=1.45 is already the lowest shear-family-adjacent constant, so a secondary point
# token can never win a native cutter's own selection purely on the DELIVERY constant (verified: no roster
# weapon's secondary point beats its own native cut-family token at 'none' armour via DELIVERY alone; where a
# secondary point DOES win at a higher tier, e.g. greatsword vs cloth, it is the RESIST table's own Williams-
# sourced puncture>>shear-vs-cloth asymmetry doing that — a real, already-grounded, pre-existing mechanism, not
# a DELIVERY-ordering bug).
CUT_AUTH_REF=0.70
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
# THRUST_AUTH_REF [PC-4 / ED-PC-0012, 2026-07-22]: the point-TOKEN-MAGNITUDE analog of CUT_AUTH_REF — the second,
# structurally identical gap the ED-PC-0011 adversarial Workflow found on 'point'. core._transmit's puncture gap-seeking
# term is floor-locked to the raw material transmission for any physically-plausible gap_prec, so DELIVERY['point']=1.45
# is credited IN FULL to a weak incidental point on a dedicated slasher regardless of how poor that point actually is
# (verified: scimitar point_eff 0.16, sabre 0.26, falchion 0.23 all scored the SAME point coupling as a real thruster) —
# so every cutter with any secondary point token eventually switched to 'point' vs armour purely on the fixed constant,
# a floor-locked artifact, not earned thrust geometry (the sabre/scimitar/falchion spurious plate-switch ED-PC-0012
# flagged). Fix = scale DELIVERY['point'] by the SELECTED point's own derived thrust magnitude (eff) vs a reference,
# exactly as 'cut' scales by eff/CUT_AUTH_REF. Anchored — per the same weakest-of-the-genuine-population principle as
# CUT_AUTH_REF (hook_sword, the weakest dedicated cutter) and PERC_AUTH_REF_SOFT — on the WEAKEST attested NATIVE
# pointer in the roster (bear_spear, point_eff 0.530; ED-PC-0012's cited 0.37/bec_de_corbin was stale — bec's native
# head is 'blunt', its beak a SECONDARY point, and its live magnitude has since drifted to 0.80). 0.52 sits just below
# bear_spear's 0.530, so every native point-headed weapon (bear_spear 0.53, rapier 0.61, spear 0.72, estoc 0.89, …)
# clamps to ratio 1.0 and is UNAFFECTED by construction — only SECONDARY/incidental points on cutters (all < 0.53) are
# scaled by their true geometric quality. Scoped to the 'point' HEAD only (the cut_thrust half-sword thrust keeps its
# own eff = the EDGE magnitude, a different quantity); distinct axis from PC-5's THRUST_LEVER_REF (head_len lever) —
# both refine the point path, one by geometry-magnitude, one by pommel-press lever.
THRUST_AUTH_REF=0.52
# THRUST_LEVER_FLOOR lowered 0.30 -> 0.24 (BROKEN-LOGIC FIX, ED-PC-0023): at 0.30 the floor BOUND for the 7 longest
# polearms (guandao/dangpa/bear_spear/ranseur/yari/fauchard/voulge, head_len 1.85-2.03m), flat-topping their real
# THRUST_LEVER_REF/head_len spread (~0.271-0.297) to one identical 0.300 — erasing the head_len-driven ordering the
# primitive is meant to express. 0.24 sits just below the roster's natural minimum (~0.271), so it only guards genuinely
# pathological/future weapon data (its stated intent — "a pike's point is never zero") and the polearm class regains its
# emergent spread. The longest reach-thrusts now read slightly LOWER gap-press authority (grounded: a longer lever
# presses a harness gap less well) instead of tying at the floor.
THRUST_LEVER_REF=0.55; THRUST_LEVER_FLOOR=0.24
def thrust_authority(head_len):
    """Point-to-hand lever -> thrust authority factor in [THRUST_LEVER_FLOOR, 1.0]. Short lever (dagger/half-sword) =
    1.0 (pommel-pressed, body-weight-backed); long reach-thrust decays toward the floor. head_len in METRES."""
    if head_len is None or head_len<=0: return 1.0
    return max(THRUST_LEVER_FLOOR, min(1.0, THRUST_LEVER_REF/head_len))
def coupling(head, armor, coverage='full', perc=PERC_AUTH_REF, gap_prec=GAP_PREC_REF, eff=None, thrust_auth=1.0):
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
    constants' comments. None (the default, every pre-existing caller) means "no scaling" (ratio 1.0, byte-identical to
    before this parameter existed); ignored for every head but 'cut'/'point'.
    `thrust_auth` [PC-5/ED-PC-0015] scales the GAP-PRESS term of the puncture path (the 'point' head + the cut_thrust
    half-sword thrust) by the point-to-hand lever authority (thrust_authority(head_len)). It scopes to the gap game vs
    a harness ONLY — a thrust that lands on soft targets (through-material) is untouched, so reach weapons stay lethal
    vs the unarmoured. 1.0 (the default) is byte-identical to before this parameter existed; inert for shear/percussion."""
    mat=TIER2MAT[armor]
    if head=='cut_thrust':
        # VERSATILE: better of the edge (shear — a cut is not pommel-pressed, no lever term) or the half-sword/gap
        # thrust (puncture, whose GAP-PRESS term carries thrust_auth — the short-lever pommel-press that defeats a harness).
        return max(DELIVERY['cut_thrust']*_transmit('shear',mat,coverage),
                   DELIVERY['point']*_transmit('puncture',mat,coverage,gap_prec=gap_prec,thrust_auth=thrust_auth))
    d=DELIVERY.get(head,1.5)
    if head=='cut' and eff is not None:
        d*=min(1.0, eff/CUT_AUTH_REF)
    elif head=='point' and eff is not None:
        d*=min(1.0, eff/THRUST_AUTH_REF)          # PC-4/ED-PC-0012: scale a POINT token by its own derived thrust magnitude — a weak incidental point on a slasher is not a dedicated thruster; native pointers (eff>=bear_spear 0.53) clamp to 1.0, unaffected
    return d*_transmit(HEAD_MODE.get(head,'shear'),mat,coverage,perc,gap_prec,thrust_auth=thrust_auth)
def damage(deg, heft_units, weapon_head, strength, armor, close, gap=GAP_PREC_REF, perc=8, q=None, eff=None, thrust_auth=1.0):
    """Linear: (strength+heft) x Coupling x Quality x DMG_SCALE — no tanh/cap. perc carries P_auth; blunt heft
    continuous from it. DMG_SCALE (above) is the single damage-scaling knob; the old tanh-cap scale/cap_end
    parameters were dead under the linear model and have been removed (with the config DAMAGE_SCALE/CAP_END
    entries they read). `gap` (the weapon's derived gap_precision, w['gap']) is now LIVE — it threads into coupling's
    puncture path (the situational gap game): the SELECTED thrust's plate-defeat scales with how well the point finds+
    holds a gap (a stiff spike/rondel defeats plate at the gaps; a whippy point is deflected). Non-thrusting heads
    ignore it (percussion/shear do not gap-seek), so it is inert for a blunt/cut blow — de-vestigialised, not just
    plumbed. `eff` [U2/ED-PC-0011] is the SELECTED element's own derived cut/thrust magnitude — threaded into
    coupling's DELIVERY scaling (the 'cut' token only, see CUT_AUTH_REF); it does NOT touch `heft` above, which
    stays the separate, already-deferred weight-class quantity (plan #9, WP.heft() — cut/thrust magnitude-driven
    heft is future work, not this fix's scope)."""
    if deg not in ('graze','success','overwhelming'): return 0
    heft = 3.0*(perc/8.0) if weapon_head=='blunt' else HEFT_HEAVY*heft_units   # blunt heft is percussion-authority-continuous; cut/thrust/point heft_units is WP.heft() (Phase B6), normalised to 1.0 at the longsword anchor -> HEFT_HEAVY*1.0 reproduces the old heavy-class magnitude there
    qf = q if q is not None else QUAL[deg]
    impact = strength + heft                                      # additive force (damage_model design: Str+Heft). M-STR commit 2a2c9f78 reverted per sim v33-mstr-impact (mstr_lin stalled low-Str+heavy).
    raw = impact * coupling(weapon_head, armor, perc=perc, gap_prec=gap, eff=eff, thrust_auth=thrust_auth) * qf * DMG_SCALE   # FIX-1b: perc scales blunt transmit vs rigid armour; gap: the situational gap game (thrust seeks the reach-ladder gaps); eff: the 'cut' token's own edge-quality scaling; thrust_auth (PC-5): the point-to-hand lever authority
    t = PEN_THR.get(armor, 0.0)                                   # PENETRATION THRESHOLD (ED-PC-0032): armour resists up to a floor
    if t > 0.0 and raw > 0.0:
        raw *= (raw*raw) / (raw*raw + t*t)                       # soft knee: a sub-defeat blow inflicts little LASTING wound (deflected); a defeating blow (large raw) keeps ~all
    return max(0, int(round(raw)))

def strike(attacker, defender, deg, close, cfg, net=None, pool=None):
    """Role-object damage convenience: reads weight/head/strength/gap/percussion off the ATTACKER and armour off the
    DEFENDER, returning the int damage. Single call-site for every blow so the 9-arg positional surface (the
    transposition-bug class) exists in exactly one place. Takes role objects (never raw A/B), consistent with the
    subsystem contract. `cfg` is retained as the engine-config handle at this single damage chokepoint — no longer
    read here now that DMG_SCALE is the lone scaling constant, but it is the wiring point should a damage knob ever
    move into config.
    CIRCUMSTANCE-DEGRADED (I2, D2/D2b/D5 — BLOCKER-2 + M-02 fixes): `gap`/`perc` now read the SELECTED element's
    OWN sel_gap/sel_perc (systems.select_mode's widened 5-tuple, threaded onto the attacker by the wrapper),
    native whole-weapon fallback only when unset — the canonical single source of truth (fixes the sel-vs-native
    object-confusion: a composite routed to a blunt sub-element is now damaged on THAT element's percussion, not
    the whole-weapon value). `heft_resp` reads the attacker's current grip_position + the selected head/pc so the
    thrust-protected, mode-split Phi_grip degrades the SAME grip the wielder actually holds."""
    q=None
    if net is not None and deg=='overwhelming':                  # M-QUAL: sigma-leverage tail (canonical sigma_n + tanh)
        z=max(0.0,(net-2*DECISIVE_OB)/SL.sigma_n(pool))          # severity beyond the overwhelming bar (net>=6)
        q=1.5+(OW_MAX-1.5)*tanh(z/OW_Z)
    head=getattr(attacker, 'sel_head', None) or attacker.head    # the SELECTED use-mode head (systems.select_mode, set by the wrapper); falls back to the native head
    gap=getattr(attacker, 'sel_gap', None); gap = gap if gap is not None else attacker.w['gap']
    perc=getattr(attacker, 'sel_perc', None); perc = perc if perc is not None else WP.percussion_authority(attacker.w)
    eff=getattr(attacker, 'sel_eff', None)                        # SELECTED element's own derived cut/thrust magnitude (U2/ED-PC-0011); None for a native-fallback attacker, inert for every head but 'cut'
    grip=getattr(attacker, 'grip_position', 0.0); sel_pc=getattr(attacker, 'sel_pc', None)
    tauth=thrust_authority(attacker.w.get('head_len'))            # PC-5: point-to-hand lever authority from the SELECTED weapon record (the half-sword swap already gives the short-lever form its own head_len); inert for shear/percussion heads
    return damage(deg, heft_resp(attacker.w, cfg, grip=grip, sel_head=head, sel_pc=sel_pc), head, attacker.strength,
                  defender.armor, close, gap, perc, q=q, eff=eff, thrust_auth=tauth)
