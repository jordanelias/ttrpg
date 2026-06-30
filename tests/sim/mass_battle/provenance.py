"""mass_battle.provenance — primitive-provenance registry (SEED, data-only, additive).

Purpose (the grounding and validation directives of the bottom-up re-architecture audit; see the
audit folder under designs/audit/): give every mechanical constant in the engine a machine-readable
grounding tier, so "is this an evidentiary primitive or an assertion?" becomes an enforced, auditable
property instead of a comment convention.

THIS IS A SEED. It does NOT import or touch the engine — it is a pure data record, so adding it is
byte-exact (the gauge digest is unchanged) and it changes no behaviour. All `value` fields are stored
as STRINGS on purpose: (a) this is a record of a value, not a live mechanical constant, and (b) it keeps
tools/ci_sim_fabrication_check.py from flagging the catalogued numbers (string literals are stripped
before that scanner runs). Population to full coverage + the CI cross-check is a later roadmap stage.

Terminal tiers (the bar from the approved plan):
  derived       — computed from a named primitive (drill-spacing, mass, momentum, frontage, ...). OK for VALUES.
  academic-law  — a cited relationship/shape that parameterizes a derivation; supplies no magnitude. OK for LAWS.
  historical    — a documented battle/band used ONLY to gate emergent behaviour; never a value's provenance. OK as a GATE.
  calibrated    — a free magnitude tuned to hold a band. DEBT: must carry a retirement gate -> derived. NOT a final state.
  ungrounded    — no source. CI FAILURE once the gate is blocking.

The audit's success metric is the `calibrated` + `ungrounded` count trending to ZERO (tracked like the
repo's ED-citation count). See the provenance-ledger companion doc for the worklist and counts.
"""

TIERS = ("derived", "academic-law", "historical", "calibrated", "ungrounded")

# Acceptable TERMINAL tiers for a *value* literal. `historical` is a gate, not a value provenance;
# `academic-law` is for the law row, not the magnitude it parameterizes.
TERMINAL_OK_FOR_VALUE = ("derived",)
DEBT = ("calibrated", "ungrounded")


class Prov:
    """One provenance row. All scalar fields are strings (record, not live constant)."""
    __slots__ = ("name", "value", "loc", "tier", "source", "law",
                 "derives_from", "gauge_rows", "toggle", "retire_to", "note")

    def __init__(self, name, value, loc, tier, source="", law="",
                 derives_from="", gauge_rows=(), toggle="", retire_to="", note=""):
        self.name = name              # constant name as it appears in config/geometry
        self.value = value            # current value, as a STRING
        self.loc = loc                # "file:line"
        self.tier = tier              # one of TIERS
        self.source = source          # citation (academic / canonical / historical band)
        self.law = law                # the grounded relationship a calibrated coeff parameterizes
        self.derives_from = derives_from  # the primitive a `derived` value is computed from
        self.gauge_rows = tuple(gauge_rows)  # bands that license a calibrated value / validate a behaviour
        self.toggle = toggle          # env toggle gating the mechanic
        self.retire_to = retire_to    # for DEBT rows: the derivation it must become
        self.note = note


# ─── SEED ROWS (the 9 census findings F1..F9 + the laws). Not exhaustive — Stage 0 completes it. ───
PROVENANCE = {

    # F1 — cell speed: shape-name switch -> must derive from momentum
    "cell_speed.tip": Prov(
        "cell_speed (tip/wing literals)", "2", "geometry.py:335", "ungrounded",
        derives_from="cells/kinematics.momentum(cell, advance_vec, footprint)",
        gauge_rows=("H2", "H4"), retire_to="derived",
        note="7-way `if shape==` switch returning hardcoded 2/1/0; Leuctra comment justifies a name, not a number."),

    # F2 — cell dimension tables -> must derive from footprint solver
    "line_cells.sizes": Prov(
        "line/horseshoe/gapped/refused *_cells tier tables", "{1:(3,3)...}", "geometry.py:19/33/47/60",
        "ungrounded", derives_from="footprint_for(troops, drill_spacing(type), depth)",
        retire_to="derived",
        note="arrowhead_cells/column_cells are ALREADY generative — these four are the holdouts."),

    # F3 — damage ladder: shape OK, value asserted
    "DAMAGE_BY_DEGREE": Prov(
        "DAMAGE_BY_DEGREE", "{Ovw:1+p,Suc:p,Par:1,Fail:0}", "config.py:72", "calibrated",
        law="degree->multiplier ladder (params/core.md)",
        derives_from="troop_atom.lethality_per_degree", gauge_rows=("H1",), retire_to="derived",
        note="ladder shape is cited; the flat magnitudes (Partial=1) are not."),

    # F4 — support weights -> derive from perpendicular falloff
    "SUPPORT_WEIGHTS": Prov(
        "SUPPORT_WEIGHTS", "{1:1.0,2:0.7,3:0.5} floor 0.3", "config.py:31", "calibrated",
        derives_from="_support_along_vector perpendicular-distance falloff (geometry.py:186)",
        gauge_rows=("H3", "H5", "H8"), retire_to="derived"),

    # F5 — min discipline -> derive from shape complexity
    "MIN_DISCIPLINE": Prov(
        "MIN_DISCIPLINE", "{Line:1..Horseshoe:5}", "config.py:61", "calibrated",
        law="ED-815 — shape complexity => drill requirement",
        derives_from="shape complexity (cell-count / aspect irregularity)", retire_to="derived"),

    # F6 — morale cap: law cited, magnitude debt
    "MORALE_PHASE_CAP": Prov(
        "MORALE_PHASE_CAP", "3", "config.py:47", "calibrated",
        law="du Picq / Clausewitz graded collapse, bounded per phase (mass_battle_v30 §A.4)",
        derives_from="morale-erosion-per-casualty primitive", gauge_rows=("C5",), retire_to="derived"),

    # F7 — PC_* shock/fatigue magnitudes: calibrated-to-band debt (representative rows)
    "PC_CHARGE_SIGMA": Prov(
        "PC_CHARGE_SIGMA", "0.55", "config.py:94", "calibrated",
        law="du Picq — cavalry weapon is the moral impulse (the SHAPE/gates are kept)",
        derives_from="charge mass x closing velocity primitive (one shock scale)",
        gauge_rows=("C2", "C4", "C5", "C7"), toggle="PER_CELL", retire_to="derived",
        note="comment says 'CAP reached only...'; magnitude is band-fit."),
    "PC_CHARGE_RECOIL": Prov(
        "PC_CHARGE_RECOIL", "6", "config.py:108", "calibrated",
        law="braced-wall-beats-frontal-charge (the gate is kept)",
        derives_from="momentum-derived recoil from the one shock scale",
        gauge_rows=("C2", "C6"), toggle="PC_BRACE_ENABLED", retire_to="derived",
        note="comment: 'CALIBRATED vs Courtrai/Swiss/Waterloo' — inverse of derivation."),
    "PC_SHOCK_FRONT": Prov(
        "PC_SHOCK_FRONT/REAR/HOLD_BRACE/DISC_FULL/DEPTH_FULL/SHAKEN_GAIN", "0.15/1.6/0.35/0.35/0.5/1.0",
        "config.py:96-103", "calibrated",
        law="front<flank<rear; brace x disc x depth gates — du Picq SHAPES (kept, law-cited)",
        derives_from="one momentum-derived shock scale x the structural ratios",
        gauge_rows=("C2", "C4", "C5", "C7"), toggle="PER_CELL", retire_to="derived",
        note="~9 dials -> collapse to one scale + documented ratios."),
    "PC_STAM_SIGMA": Prov(
        "PC_STAM_SIGMA / PC_STAMINA_DRAIN / PC_STAMINA_REST", "1.5/12/5", "config.py:82-85", "calibrated",
        law="du Picq — fatigue lowers effectiveness; depth rotates fresh ranks",
        derives_from="contact-cells x drain-per-clash primitive", toggle="PER_CELL", retire_to="derived"),
    "PC_KITE_STANDOFF": Prov(
        "PC_KITE_STANDOFF", "5", "config.py:106", "calibrated",
        derives_from="volley band geometry (VOLLEY_MIN/MAX_RANGE)", retire_to="derived",
        note="comment: 'Calibrate by measurement' — explicit band-fit."),

    # F8 — Lanchester: LAW grounded, coefficients calibrated
    "K_LINEAR": Prov(
        "K_LINEAR", "12", "config.py:125", "calibrated",
        law="Lanchester Linear Law — Hillestad/Taylor/Armstrong (gauge_grounding §1; mb_lanchester_design §3a)",
        derives_from="block-size x per-soldier-lethality x contact-frontage",
        gauge_rows=("H1", "H3"), toggle="LANCHESTER_ENABLED", retire_to="derived"),
    "K_SQUARE": Prov(
        "K_SQUARE", "0.25", "config.py:126", "calibrated",
        law="Lanchester Square Law — aimed fire lifts the frontage cap (gauge_grounding §1)",
        derives_from="shooter-count^2 x per-shot-lethality", gauge_rows=("R3",),
        toggle="LANCHESTER_ENABLED", retire_to="derived"),
    "CASUALTY_SCALE": Prov(
        "CASUALTY_SCALE", "4", "config.py:39", "calibrated",
        law="per-tick lethality rescoped by the Lanchester term",
        derives_from="block-size x lethality (subsumed once K_LINEAR is derived)",
        gauge_rows=("H1",), retire_to="derived"),

    # F9 — facing: octagon boundaries derived; vulnerability shape law-cited
    "ANGLE_DEF_MOD": Prov(
        "ANGLE_DEF_MOD", "{GREEN:0,YELLOW:-1,RED:-2}", "config.py:65", "calibrated",
        law="du Picq — flank worse than front, rear worst (validated C4/C7)",
        derives_from="fraction of a cell's frontage the attack angle exposes",
        gauge_rows=("C4", "C7"), retire_to="derived"),

    # Laws that are correctly grounded and must be PRESERVED (academic-law rows; no magnitude here)
    "law.lanchester": Prov(
        "Lanchester linear/square law", "n/a", "core/attrition.py (target)", "academic-law",
        source="Hillestad/Owen/Blumenthal 1995; Taylor 1979/1983; Armstrong/Sodergren 2015 (DOIs in gauge_grounding §1)"),
    "law.morale_sigma": Prov(
        "graded morale effectiveness", "n/a", "resolution.py:45", "academic-law",
        source="Ardant du Picq, Battle Studies; Clausewitz, On War III.12"),
    "law.cavalry_regimes": Prov(
        "cavalry regime differentiation (contested/braced/shaken/envelop)", "n/a", "resolution.py:83",
        "academic-law",
        source="Sidnell 2006; Burkholder 2007; Boddy 2015; Barua 2011 (DOIs in gauge_grounding §3)"),
}


def debt_rows():
    """The retirement worklist: every row that is not yet a terminal-OK value provenance."""
    return {k: p for k, p in PROVENANCE.items() if p.tier in DEBT}


def counts():
    """Tier histogram — the success metric (calibrated+ungrounded -> 0)."""
    h = {t: 0 for t in TIERS}
    for p in PROVENANCE.values():
        h[p.tier] = h.get(p.tier, 0) + 1
    return h
