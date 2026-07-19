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
from math import tanh
from engine.autoload import sigma_leverage as SL
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
GAP_EXPOSURE={'none':1.0,'cloth':0.85,'mail':0.90,'plate':0.90}     # [SIM-CALIBRATE] thrust-accessible gap fraction / material (reach-ladder)
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
def _transmit(mode, mat, coverage, perc=PERC_AUTH_REF, gap_prec=GAP_PREC_REF):
    t=1.0-RESIST[mat][mode]
    if mode=='puncture':                                           # SITUATIONAL GAP GAME: a thrust takes through-
        # material OR the reach-ladder gap it seeks. The gap term is GAP-SEEKING: the material's thrust-accessible gap
        # fraction (GAP_EXPOSURE) scaled by the WEAPON's derived gap_precision (a stiff concentrated point finds+holds
        # the gap; a whippy point deflects). Replaces the old fixed COVERAGE_GAP floor — plate is no longer a flat 0.15
        # for every point; the poleaxe spike / rondel now beat the through-material 0.30, the rapier's whippy point does
        # not. Emergent in gap_prec (= w['gap']); no weapon name.
        return max(t, GAP_EXPOSURE[mat]*gap_prec)
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
def coupling(head, armor, coverage='full', perc=PERC_AUTH_REF, gap_prec=GAP_PREC_REF, eff=None):
    """DELIVERY x transmit. cut_thrust is VERSATILE — takes the better of its edge (shear) or the half-sword thrust
    (puncture/gaps) at each armour level: a longsword half-swords vs plate instead of bouncing (restores the prior
    engine's max(cut,point) mode-shift; HEMA: you half-sword vs harness). [damage_model.coupling + cut_thrust versatility]
    `perc` (percussion authority) scales the blunt transmit vs rigid armour (FIX-1b); ignored for non-blunt heads.
    `gap_prec` (the weapon's derived gap_precision, w['gap']) makes the PUNCTURE/thrust path GAP-SEEKING (the situational
    gap game): a stiff concentrated point defeats plate at the gaps, a whippy one is deflected. Threaded for every
    thrusting head (point + the cut_thrust half-sword thrust); percussion/shear ignore it (a broad blow/cut does not
    gap-seek). Defaults to a neutral point (GAP_PREC_REF); the live path threads the real w['gap'].
    `eff` [U2/ED-PC-0011] scales the 'cut' token's DELIVERY by its own derived edge-quality vs CUT_AUTH_REF — see
    that constant's comment for the full reasoning. None (the default, every pre-existing caller) means "no
    scaling" (ratio 1.0, byte-identical to before this parameter existed); ignored for every head but 'cut'."""
    mat=TIER2MAT[armor]
    if head=='cut_thrust':
        return max(DELIVERY['cut_thrust']*_transmit('shear',mat,coverage),
                   DELIVERY['point']*_transmit('puncture',mat,coverage,gap_prec=gap_prec))
    d=DELIVERY.get(head,1.5)
    if head=='cut' and eff is not None:
        d*=min(1.0, eff/CUT_AUTH_REF)
    return d*_transmit(HEAD_MODE.get(head,'shear'),mat,coverage,perc,gap_prec)
def damage(deg, heft_units, weapon_head, strength, armor, close, gap=GAP_PREC_REF, perc=8, q=None, eff=None):
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
    return max(0, int(round(impact * coupling(weapon_head, armor, perc=perc, gap_prec=gap, eff=eff) * qf * DMG_SCALE)))   # FIX-1b: perc scales blunt transmit vs rigid armour; gap: the situational gap game (thrust seeks the reach-ladder gaps); eff: the 'cut' token's own edge-quality scaling

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
    return damage(deg, heft_resp(attacker.w, cfg, grip=grip, sel_head=head, sel_pc=sel_pc), head, attacker.strength,
                  defender.armor, close, gap, perc, q=q, eff=eff)
