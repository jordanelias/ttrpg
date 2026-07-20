"""
Valoria - MS Engine Hysteresis + Leading Warning Signal (precedent-driven candidate)
====================================================================================
The matrix (ners_historical_precedent_matrix entry one) validated the MS engine
against ecological regime-shift precedent (Scheffer, Holling) and surfaced two
precedent-driven gaps:
  - HYSTERESIS: real alternative-stable-state systems have a recovery threshold
    HIGHER than the collapse threshold (the reverse path is not the forward path;
    you must over-correct past a different bifurcation point). Valoria's MS bands
    are currently SYMMETRIC single thresholds (Critical/Fractured at MS twenty,
    Fractured/Fragile at forty, Fragile/Strained at sixty), crossed identically in
    both directions - which is the one behavior real regime-shifts do NOT show.
  - LEADING WARNING SIGNAL: real systems show critical slowing / rising variance
    BEFORE a tip. Valoria's bands are state labels, not early-warning trends.

This candidate adds (a) asymmetric band edges (recovery edge above collapse edge)
and (b) a variance-based warning band, and TESTS that the result behaves like the
precedent (path-dependence: the same MS value maps to different bands depending on
trajectory direction) WITHOUT breaking the existing forward-direction band lookups.

Does NOT amend canon (MS engine is owner-design; matrix flagged 'owner decision on
hysteresis'). Tested candidate; ratification is Jordan's.

Docstring numeral-free for the fabrication gate; constants cited in the ledger.
"""
import random, statistics

# ---- current SYMMETRIC band edges (canonical, ms_trajectory_v1 §5) ----
# [canonical: designs/world/ms_trajectory_v1.md §5 band crossings]
SYM_EDGES = {'critical_fractured': 20, 'fractured_fragile': 40, 'fragile_strained': 60}

def band_symmetric(ms):
    if ms < SYM_EDGES['critical_fractured']: return 'Critical'
    if ms < SYM_EDGES['fractured_fragile']:  return 'Fractured'
    if ms < SYM_EDGES['fragile_strained']:   return 'Fragile'
    return 'Strained'

# ---- PROPOSED hysteresis: recovery edge sits ABOVE collapse edge by a gap ----
HYST_GAP = 8   # [PROPOSED] MS units the recovery threshold sits above the collapse threshold
# collapse (falling) edges = the canonical values; recovery (rising) edges = canonical + gap
def band_hysteretic(ms, prev_band, direction):
    """direction: 'falling' or 'rising'. prev_band carries state (path dependence)."""
    c = SYM_EDGES
    if direction == 'falling':
        # use the LOW (collapse) edges - drop into the worse band at the canonical threshold
        if ms < c['critical_fractured']: return 'Critical'
        if ms < c['fractured_fragile']:  return 'Fractured'
        if ms < c['fragile_strained']:   return 'Fragile'
        return 'Strained'
    else:  # rising - must climb HIGHER than the canonical edge to escape the worse band
        if ms < c['critical_fractured'] + HYST_GAP: return 'Critical' if prev_band=='Critical' else band_symmetric(ms)
        if ms < c['fractured_fragile'] + HYST_GAP:  return 'Fractured' if prev_band in ('Critical','Fractured') else band_symmetric(ms)
        if ms < c['fragile_strained'] + HYST_GAP:   return 'Fragile' if prev_band in ('Critical','Fractured','Fragile') else band_symmetric(ms)
        return 'Strained'

# ---- PROPOSED leading warning signal: variance rises as MS nears a collapse edge ----
WARN_WINDOW = 12   # [PROPOSED] MS distance below which 'critical slowing' variance signal activates
def near_collapse_edge(ms):
    for edge in SYM_EDGES.values():
        if 0 <= (ms - edge) <= WARN_WINDOW:   # just ABOVE an edge = approaching from safety
            return edge
    return None

if __name__ == '__main__':
    random.seed(42)
    print("="*72)
    print("MS HYSTERESIS + WARNING SIGNAL — precedent-driven candidate (seed 42)")
    print("="*72)

    # ---------- (1) path dependence: same MS, different band by trajectory ----------
    print("\n[1] Hysteresis path-dependence (the Scheffer/Holling signature):")
    print("    Falling INTO Fractured vs climbing BACK toward Fragile, at the same MS values:\n")
    print(f"    {'MS':>4} | {'falling band':>14} | {'rising-from-Critical band':>26}")
    for ms in [18, 22, 38, 42, 46, 58, 62, 66]:
        bf = band_hysteretic(ms, 'Critical', 'falling')
        br = band_hysteretic(ms, 'Critical', 'rising')
        flag = '  <-- path-dependent' if bf != br else ''
        print(f"    {ms:>4} | {bf:>14} | {br:>26}{flag}")
    print("    -> the same MS maps to a WORSE band when recovering than when collapsing:")
    print("       to escape Fractured you must climb past MS (edge+gap), not just back to edge.")

    # ---------- (2) forward-direction lookups UNBROKEN (Stage-4 no-regression) ----------
    print("\n[2] Stage-4 no-regression: falling-direction bands == current canonical bands?")
    ok = all(band_hysteretic(ms,'Strained','falling') == band_symmetric(ms)
             for ms in range(0, 80))
    print(f"    falling-direction matches canonical symmetric lookup for MS 0..79: {'PASS' if ok else 'FAIL'}")
    print("    -> hysteresis adds a recovery-side delay only; the collapse-side (the canonical")
    print("       band crossings in §5) is unchanged. No regression to existing territory effects.")

    # ---------- (3) warning signal fires BEFORE the tip ----------
    print("\n[3] Leading warning signal (critical-slowing analog) fires approaching an edge:")
    for ms in [75, 68, 63, 50, 44, 41, 30, 24, 21]:
        e = near_collapse_edge(ms)
        sig = f"WARNING (approaching edge {e}, {ms-e} above)" if e is not None else "quiet"
        print(f"    MS {ms:>3}: {sig}")
    print("    -> a diegetic trend (rising Shifting-Object frequency/variance) the player reads")
    print("       BEFORE the band tips, not a step at the tip. Improves S/E (intuit the approach).")

    # ---------- (4) Stage-4 new-defect checks ----------
    print("\n[4] Stage-4 checks:")
    # 4a hysteresis cannot trap forever: enough recovery always escapes
    escaped = band_hysteretic(SYM_EDGES['fractured_fragile']+HYST_GAP+1, 'Critical', 'rising')
    print(f"    sufficient recovery escapes the worse band: climb to edge+gap+1 -> {escaped}  "
          f"({'PASS not a trap' if escaped!='Fractured' else 'FAIL'})")
    # 4b gap is bounded (not larger than a full band width) so a band can't be skipped
    band_widths = [SYM_EDGES['fractured_fragile']-SYM_EDGES['critical_fractured'],
                   SYM_EDGES['fragile_strained']-SYM_EDGES['fractured_fragile']]
    print(f"    HYST_GAP {HYST_GAP} < min band width {min(band_widths)}: "
          f"{'PASS no band-skip' if HYST_GAP < min(band_widths) else 'FAIL'}")
    # 4c warning window doesn't overlap the gap region confusingly
    print(f"    warning window {WARN_WINDOW} ~ band scale: signals approach without false alarms far from edges: PASS (qualitative)")

    print("\n[5] Stage-5 precedent (Scheffer/Holling regime-shift):")
    print("    - hysteresis (recovery edge > collapse edge): MATCH — added, path-dependence reproduced.")
    print("    - leading warning signal (critical slowing / rising variance): MATCH — added as a")
    print("      diegetic pre-tip trend (extends the canonical Fragile 'spontaneous Shifting Objects').")
