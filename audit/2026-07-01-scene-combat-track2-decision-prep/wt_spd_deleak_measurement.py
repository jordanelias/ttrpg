"""Track-2 decision-prep harness — measures the roster-wide delta IF the `wt`/`spd` legacy weapon fields were
replaced by their already-derived weapon_physics equivalents, WITHOUT touching any live engine code.

Context: HANDOFF.md flags two open, Jordan-gated single-source residuals from the Gate-1 audit:
  1. `wt`/`spd` cost-path de-leak (core.py:heft_resp reads w.get('wt'); systems.py:weapon_tempo reads w['spd'])
  2. WP.reach()/authority() vs systems.reach_base/wield_heft (see the companion comparison doc in this folder)
This script is prep for #1 only — a measured before/after so Jordan can rule on it with data in hand, per the
"needs a measured before/after presented for sign-off" note in HANDOFF.md. It does not flip anything live.

Two independent sub-questions (they use DIFFERENT existing derived quantities, so are reported separately):

  A. DAMAGE path (core.heft_resp / core.damage): heft_resp currently anchors on the binary `wt` class (`heavy`/
     `light`) with an optional continuous within-class mass refinement (HEFT_MASS_K, currently active per
     config.py HEFT_MODE='continuous'). The candidate reuses `systems.wield_heft`'s EXACT existing formula
     ((at_grip(w, 0)['I_g'] / REC_I_REF) ** WIELD_HEFT_EXP) — the same g-aware MoI heft already live on the
     tempo/cost path since Stage 2b (commit d3661936) — applied to the damage path instead of inventing a new
     coefficient. NOTE: core.damage() only reads heft_units for non-blunt heads (blunt heads get their damage
     heft from percussion authority instead — see core.py:144) — so this residual is INERT for blunt weapons
     (mace/staff/poleaxe) on the damage path; it only moves point/cut_thrust/cut weapons.

  B. TEMPO path (systems.weapon_tempo): currently reads `w['spd']` (a bare hand-authored constant, -0.5..3.0
     across the roster) times config SPEED_K. REVISED CANDIDATE (v2 — see wt_spd_deleak_report.md for why the
     first draft, a bare weapon_physics.agility() substitution, was rejected as under-grounded): the candidate
     instead reuses `systems.recoverability_factor` at baseline (grip_position=0, lunge_depth=0) — the
     engine's own existing, already-grounded commitment=recovery model, which blends:
       - WEIGHT + BALANCE  — WP.at_grip(w,0)'s I_g (swing inertia) and S_g (static moment/PoB), the same
         primitives wield_heft already uses;
       - HANDS             — a MoI-aware 1H/2H force-couple control credit (tau/tau_ref);
       - THRUST vs SWING   — geometry's point_concentration blending a swing-arrest cost (C_swing, MoI-based)
         against a thrust-retract cost (C_thrust, static-moment-based) — the primitive the v1 agility()
         candidate entirely lacked;
       - COMMITMENT/RECOVERY — this function IS the commitment=recovery axis (its own docstring), so using it
         for baseline tempo directly reuses the engine's already-established grounding, not a new invention.
     Empirically, current spd correlates far more strongly with 1/recoverability_factor (r=0.878) than with
     point_concentration alone (r=0.359) — see corr_table() — suggesting the hand-tuned spd constants were
     already informally approximating this exact physics before recoverability_factor existed to formalize it.
     CAVEAT (flagged, not resolved): weapon_tempo's `pen` term ALREADY separately penalises weight+hands via
     wield_heft (WEIGHT_PEN, HANDS_COMMIT) — so a naive full swap of spd for 1/recoverability_factor would
     DOUBLE-COUNT weight and hands (once via pen, once via recoverability_factor's I_g/S_g/tau terms). This
     script reports the naive full-swap numbers for visibility, WITH this caveat, and does not attempt to
     de-duplicate the overlap — that decomposition is exactly the kind of design judgment call this packet is
     prep for, not a recommendation to make unilaterally.

Run: python wt_spd_deleak_measurement.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../scene/combat_engine_v1'))
import config
import core
import systems
import weapon_physics as WP
from weapons import WEAPONS

CFG = config.CFG
ARMORS = ['none', 'light', 'medium', 'heavy']
ROSTER = ["rapier", "arming", "longsword", "greatsword", "sabre", "dagger",
          "paired_short", "spear", "staff", "mace", "poleaxe"]
STRENGTH = 4          # neutral mid-roster attacker; holds constant across weapons so only the weapon term varies
ANCHOR_WEAPON = 'arming'   # matches workbench/balance.py's own baseline='arming' convention


class _Mock:
    """Minimal Combatant stand-in exposing only what systems.weapon_tempo/wield_heft/recoverability_factor
    read (w, agi, poise, grip_position, lunge_depth). Not a Combatant subclass — this harness never calls
    anything that needs wound state, stamina, etc."""
    def __init__(self, w):
        self.w = w
        self.agi = 4          # neutral (AGI_TEMPO_K is centred here — config.py's own convention)
        self.poise = 1.0      # full structure — poise_factor returns 1.0, no distortion
        self.grip_position = 0.0   # baseline (as-issued) — no gather/choke
        self.lunge_depth = 0.0     # baseline — no lunge


# ---------------------------------------------------------------------------
# A. Damage-path heft: wt-anchor (live) vs wield_heft-reuse (candidate)
# ---------------------------------------------------------------------------
def current_heft(w):
    return core.heft_resp(w, CFG)


def candidate_heft(w):
    """Reuses systems.wield_heft's exact formula (no new coefficient) at grip_position=0 (as-issued)."""
    I_g = WP.at_grip(w, 0.0)['I_g']
    return (max(1e-6, I_g) / CFG['REC_I_REF']) ** CFG['WIELD_HEFT_EXP']


def damage_table():
    rows = []
    for name in ROSTER:
        w = WEAPONS[name]
        if w['head'] == 'blunt':
            rows.append((name, w['head'], 'N/A (blunt heft comes from percussion authority, not heft_resp)',
                         None, None, None))
            continue
        cur_h, cand_h = current_heft(w), candidate_heft(w)
        dmgs_cur, dmgs_cand = [], []
        for arm in ARMORS:
            d_cur = core.damage('success', cur_h, w['head'], STRENGTH, arm, close=False,
                                 gap=w['gap'], perc=WP.percussion_authority(w))
            d_cand = core.damage('success', cand_h, w['head'], STRENGTH, arm, close=False,
                                  gap=w['gap'], perc=WP.percussion_authority(w))
            dmgs_cur.append(d_cur)
            dmgs_cand.append(d_cand)
        rows.append((name, w['head'], f"{cur_h:.2f} -> {cand_h:.2f}", dmgs_cur, dmgs_cand,
                     [c - u for u, c in zip(dmgs_cur, dmgs_cand)]))
    return rows


# ---------------------------------------------------------------------------
# B. Tempo-path spd: correlation of the CURRENT constant against grounded primitives, then a
#    recoverability_factor-derived candidate (anchored on 'arming', same convention as section A)
# ---------------------------------------------------------------------------
def _corr(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    va = sum((x - ma) ** 2 for x in a) ** 0.5
    vb = sum((y - mb) ** 2 for y in b) ** 0.5
    return cov / (va * vb)


def primitives_table():
    rows = []
    for name in ROSTER:
        w = WEAPONS[name]
        c = _Mock(w)
        a = WP.at_grip(w, 0.0)
        rec = systems.recoverability_factor(c, CFG)
        pc = w['geometry']['point_concentration']
        rows.append(dict(name=name, spd=w['spd'], pc=pc, hands=w['hands'],
                          I_g=a['I_g'], S_g=a['S_g'], recov=rec, inv_recov=1.0 / rec))
    return rows


def _recov_k_prime(rows):
    anchor = next(r for r in rows if r['name'] == ANCHOR_WEAPON)
    anchor_spd_term = WEAPONS[ANCHOR_WEAPON]['spd'] * CFG['SPEED_K']
    return anchor_spd_term / anchor['inv_recov']


def tempo_table(rows):
    k_prime = _recov_k_prime(rows)
    out = []
    for r in rows:
        w = WEAPONS[r['name']]
        c = _Mock(w)
        cur_tempo = systems.weapon_tempo(c, CFG)
        cur_spd_term = w['spd'] * CFG['SPEED_K']
        cand_spd_term = r['inv_recov'] * k_prime
        cand_tempo = cur_tempo - cur_spd_term + cand_spd_term
        out.append((r['name'], w['spd'], r['inv_recov'], cur_spd_term, cand_spd_term,
                     cur_tempo, cand_tempo, cand_tempo - cur_tempo))
    return out, k_prime


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    print("=" * 100)
    print("A. DAMAGE PATH — heft_resp (wt-anchored, live) vs wield_heft-reuse (candidate), strength=%d" % STRENGTH)
    print("=" * 100)
    print(f"{'weapon':18} {'head':12} {'heft cur->cand':24} " + " ".join(f"{a:>8}" for a in ARMORS) + "   deltas")
    for name, head, heft_str, dmgs_cur, dmgs_cand, deltas in damage_table():
        if dmgs_cur is None:
            print(f"{name:18} {head:12} {heft_str}")
            continue
        cur_str = " ".join(f"{d:8d}" for d in dmgs_cur)
        cand_str = " ".join(f"{d:8d}" for d in dmgs_cand)
        delta_str = " ".join(f"{d:+d}" for d in deltas)
        print(f"{name:18} {head:12} {heft_str:24} {cur_str}   (candidate: {cand_str})   deltas: {delta_str}")

    print()
    print("=" * 100)
    print("B0. GROUNDING CHECK — does the current spd constant already track a grounded primitive?")
    print("=" * 100)
    rows = primitives_table()
    print(f"{'weapon':18} {'spd':>6} {'pc(thrust-ness)':>16} {'hands':>6} {'I_g':>8} {'S_g':>7} {'recov':>7} {'1/recov':>8}")
    for r in rows:
        print(f"{r['name']:18} {r['spd']:6.1f} {r['pc']:16.2f} {r['hands']:6d} {r['I_g']:8.4f} {r['S_g']:7.3f} "
              f"{r['recov']:7.3f} {r['inv_recov']:8.3f}")
    spds = [r['spd'] for r in rows]
    pcs = [r['pc'] for r in rows]
    invrec = [r['inv_recov'] for r in rows]
    print(f"\ncorr(spd, point_concentration)        = {_corr(spds, pcs):+.3f}")
    print(f"corr(spd, 1/recoverability_factor)    = {_corr(spds, invrec):+.3f}   <-- much stronger")

    print()
    print("=" * 100)
    print("B. TEMPO PATH — spd (bare constant, live) vs recoverability_factor-derived (candidate, anchored on '%s')" % ANCHOR_WEAPON)
    print("   CAVEAT: pen already penalises weight+hands via wield_heft separately -- this candidate risks")
    print("   double-counting weight/hands. Reported for visibility, not as a clean drop-in. See report.md.")
    print("=" * 100)
    trows, k_prime = tempo_table(rows)
    print(f"(K' = {k_prime:.4f}, solved so (1/recov)('{ANCHOR_WEAPON}')*K' == spd('{ANCHOR_WEAPON}')*SPEED_K)")
    print(f"{'weapon':18} {'spd':>6} {'1/recov':>8} {'cur term':>9} {'cand term':>9} {'cur tempo':>10} {'cand tempo':>11} {'delta':>7}")
    for name, spd, invrec_v, cur_term, cand_term, cur_tempo, cand_tempo, delta in trows:
        print(f"{name:18} {spd:6.1f} {invrec_v:8.3f} {cur_term:9.3f} {cand_term:9.3f} {cur_tempo:10.3f} {cand_tempo:11.3f} {delta:+7.3f}")


if __name__ == '__main__':
    main()
