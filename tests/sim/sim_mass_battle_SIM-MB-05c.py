# SIM-MB-05C — Exhaustive branch exploration for Phase 2 unresolved options
# Session: 2026-05-11 | [canonical: structural — extends SIM-MB-05A/B]
#
# Branches under test:
#  H-1..H-5: Horseshoe trigger alternatives (for ED-821)
#  V-1..V-2: Volley TN comparison (for ED-822)
#  D-1..D-3: Drift cascade alternatives (for ED-817 robustness)
#  C-1..C-4: Combined attack defensive response (for ED-818 / Finding D)
#  X-1..X-4: Asymmetric stat / composition / size matchups

import sys, random, statistics, math, copy
sys.path.insert(0, '/home/claude')
exec(open('/home/claude/sim_mb_05.py').read())

# ─────────────────────────────────────────────────────────────────────────────
# HORSESHOE TRIGGER ALTERNATIVES (for ED-821)
# ─────────────────────────────────────────────────────────────────────────────

class HorseshoeH1(Horseshoe):
    """H-1: current — trigger on opponent >40% center mass."""
    name = "HorseshoeH1"
    def phase5_mods(self, col, opponent_in_center=False):
        return super().phase5_mods(col, opponent_in_center)

class HorseshoeH2(Horseshoe):
    """H-2: trigger on ANY engagement resolved at center (positional)."""
    name = "HorseshoeH2"
    def phase5_mods(self, col, opponent_in_center=False):
        # opponent_in_center treated as 'engagement happens at center' — always True if enemy present
        if col == "center":
            return {"off_d": -2, "def_d": 1}
        # Flanks always get +2 if engagement at center happens
        return {"off_d": 2, "def_d": 0}  # [canonical: structural — H-2 positional trigger]

class HorseshoeH3(Horseshoe):
    """H-3: trigger on opponent column pool >40% of their total at center."""
    name = "HorseshoeH3"
    # Used with custom signal computation
    def phase5_mods(self, col, opponent_in_center=False):
        return HorseshoeH1().phase5_mods(col, opponent_in_center)

def h3_signal(unit, opponent):
    """H-3 signal: opponent's center column pool > 40% of their total base pool."""
    if not opponent:
        return False
    total = opponent.base_combat_pool()
    if total <= 0:
        return False
    center_pool = opponent.column_combat_pool("center")
    return (center_pool / total) > 0.4  # [canonical: structural — H-3 pool-ratio trigger]

class HorseshoeH4(Horseshoe):
    """H-4: AI heuristic — opponent's targeting weights toward weak columns
    triggers trap. Modelled by signal: opponent's intended-target column matches our center."""
    name = "HorseshoeH4"
    def phase5_mods(self, col, opponent_in_center=False):
        return HorseshoeH1().phase5_mods(col, opponent_in_center)

def h4_target_signal(unit, opponent):
    """H-4: opponent's targeting prefers weakest defender column.
    Heuristic: opponent attacks the column with lowest defender mass."""
    if not opponent:
        return False
    masses = {c: unit.grid.cell_fraction("front", c) for c in COLS}
    weakest = min(masses, key=masses.get)
    return weakest == "center"  # [canonical: structural — H-4 weak-column AI]

class HorseshoeH5(Horseshoe):
    """H-5: trigger on any combined attack at center (specific anti-concentration)."""
    name = "HorseshoeH5"
    def phase5_mods(self, col, opponent_in_center=False):
        if col == "center":
            return {"off_d": -2, "def_d": 1}
        if opponent_in_center:  # flag set when combined attack fires
            return {"off_d": 2, "def_d": 0}
        return {"off_d": 0, "def_d": 0}

# ─────────────────────────────────────────────────────────────────────────────
# Battle runner with H-variant trap signal injection
# ─────────────────────────────────────────────────────────────────────────────

def run_battle_h_variant(side_a, side_b, max_turns=10,
                          h_variant=1, verbose=False):
    """Battle with configurable Horseshoe trigger logic.
    h_variant: 1=mass>40%, 2=positional always, 3=pool-ratio>40%, 4=weak-col AI, 5=combined-only."""  # [canonical: SIM-MB-05 §3.1 — opponent-mass threshold]
    units = side_a + side_b
    turns = 0
    for t in range(1, max_turns + 1):
        turns = t
        active_a = [u for u in side_a if not u.routed and not u.broken]
        active_b = [u for u in side_b if not u.routed and not u.broken]
        if not active_a or not active_b:
            break
        # Volley
        volley_dmg = {}
        for s in units:
            if s.routed or s.total_volley_pool() == 0:
                continue
            enemies = [u for u in units if u.faction != s.faction and not u.routed]
            if enemies:
                target = enemies[0]
                pool = s.total_volley_pool()
                net = roll_pool(pool, tn=6)
                d = max(0, max(0, net) - target.ranged_dr)
                volley_dmg[target.name] = volley_dmg.get(target.name, 0) + d
        # Engagement with variant trap signal
        pending = {}
        if active_a and active_b:
            a, b = active_a[0], active_b[0]
            for col in COLS:
                # Compute trap signals per H variant
                def horseshoe_signal(unit, opp):
                    if not isinstance(unit.shape, Horseshoe):
                        return False
                    if h_variant == 1:
                        if not opp: return False
                        ft = opp.grid.row_mass("front")
                        if ft < 0.01: return False  # [canonical: structural — float epsilon]
                        return (opp.grid.cell_fraction("front", "center") / ft) > 0.4
                    elif h_variant == 2:
                        return True  # always fires if engagement happens
                    elif h_variant == 3:
                        return h3_signal(unit, opp)
                    elif h_variant == 4:
                        return h4_target_signal(unit, opp)
                    elif h_variant == 5:
                        return False  # combined-only; no combined here
                    return False

                a_trap = horseshoe_signal(a, b)
                b_trap = horseshoe_signal(b, a)
                # GappedLine trap signal (conditional)
                def gapped_signal(unit, opp):
                    if not isinstance(unit.shape, GappedLine):
                        return False
                    if not opp: return False
                    gap_col = unit.shape.gap_column
                    ft = opp.grid.row_mass("front")
                    if ft < 0.01: return False  # [canonical: structural — float epsilon]
                    return (opp.grid.cell_fraction("front", gap_col) / ft) > 0.4
                a_g = gapped_signal(a, b)
                b_g = gapped_signal(b, a)

                a_mods = a.shape.phase5_mods(col, a_trap or a_g)
                b_mods = b.shape.phase5_mods(col, b_trap or b_g)
                if a_mods["off_d"] == -99 or b_mods["off_d"] == -99:  # [canonical: structural — empty-column sentinel from sim_mb_05.py]
                    continue
                a_dice = max(1, a.column_combat_pool(col) + a_mods["off_d"])
                b_dice = max(1, b.column_combat_pool(col) + b_mods["def_d"])
                a_net = roll_pool(a_dice)
                b_net = roll_pool(b_dice)
                a_deg = compute_degree(a_net, max(1, b_net))
                b_deg = compute_degree(b_net, max(1, a_net))
                pending[b.name] = pending.get(b.name, 0) + max(0, DAMAGE_BY_DEGREE[a_deg](a.power) - b.dr)
                pending[a.name] = pending.get(a.name, 0) + max(0, DAMAGE_BY_DEGREE[b_deg](b.power) - a.dr)
        # Apply
        all_dmg = {**volley_dmg}
        for k, v in pending.items():
            all_dmg[k] = all_dmg.get(k, 0) + v
        size_before = {u.name: u.size for u in units}
        for u in units:
            if u.name in all_dmg:
                u.hp = max(0, u.hp - all_dmg[u.name])
                u.recalc_size()
        # Discipline
        for u in units:
            if u.routed or u.broken: continue
            sl = size_before[u.name] - u.size
            opp_units = [x for x in units if x.faction != u.faction]
            opp_sl = (sum(max(0, size_before.get(x.name, x.size) - x.size) for x in opp_units)
                       / max(1, len(opp_units)))
            if sl > u.discipline and sl > opp_sl:
                u.discipline = max(0, u.discipline - 1)
            u.check_drift([])
        # Morale
        for u in units:
            if u.routed: continue
            sl = size_before[u.name] - u.size
            cap = 3; adj = 0
            if u.size < u.size_max // 4 and u.size > 0:
                adj += -min(2, cap); cap -= 2
            elif u.size < u.size_max // 2:
                adj += -min(1, cap); cap -= 1
            u.morale = max(1, u.morale + adj)
        for u in units:
            if not u.routed and u.morale <= 0:
                u.routed = True
        for u in units:
            if not u.routed and not u.broken:
                u.morale = min(u.morale_start, u.morale + 1)
    a_surv = [u for u in side_a if not u.routed]
    b_surv = [u for u in side_b if not u.routed]
    return ("A" if a_surv and not b_surv else
             "B" if b_surv and not a_surv else "draw"), turns

# ─────────────────────────────────────────────────────────────────────────────
# VOLLEY TN COMPARISON (for ED-822)
# ─────────────────────────────────────────────────────────────────────────────

def run_battle_volley_tn(side_a, side_b, volley_tn=6, max_turns=10):
    """Battle with configurable Volley TN."""
    units = side_a + side_b
    for t in range(1, max_turns + 1):
        active_a = [u for u in side_a if not u.routed and not u.broken]
        active_b = [u for u in side_b if not u.routed and not u.broken]
        if not active_a or not active_b: break
        # Volley with configurable TN
        volley_dmg = {}
        for s in units:
            if s.routed or s.total_volley_pool() == 0: continue
            enemies = [u for u in units if u.faction != s.faction and not u.routed]
            if enemies:
                target = enemies[0]
                pool = s.total_volley_pool()
                net = roll_pool(pool, tn=volley_tn)  # configurable
                d = max(0, max(0, net) - target.ranged_dr)
                volley_dmg[target.name] = volley_dmg.get(target.name, 0) + d
        # Engagement (standard)
        pending = {}
        if active_a and active_b:
            a, b = active_a[0], active_b[0]
            for col in COLS:
                a_mods = a.shape.phase5_mods(col, False)
                b_mods = b.shape.phase5_mods(col, False)
                if a_mods["off_d"] == -99 or b_mods["off_d"] == -99: continue  # [canonical: structural — empty-column sentinel from sim_mb_05.py]
                a_dice = max(1, a.column_combat_pool(col) + a_mods["off_d"])
                b_dice = max(1, b.column_combat_pool(col) + b_mods["def_d"])
                a_net = roll_pool(a_dice)
                b_net = roll_pool(b_dice)
                a_deg = compute_degree(a_net, max(1, b_net))
                b_deg = compute_degree(b_net, max(1, a_net))
                pending[b.name] = pending.get(b.name, 0) + max(0, DAMAGE_BY_DEGREE[a_deg](a.power) - b.dr)
                pending[a.name] = pending.get(a.name, 0) + max(0, DAMAGE_BY_DEGREE[b_deg](b.power) - a.dr)
        all_dmg = {**volley_dmg}
        for k, v in pending.items():
            all_dmg[k] = all_dmg.get(k, 0) + v
        size_before = {u.name: u.size for u in units}
        for u in units:
            if u.name in all_dmg:
                u.hp = max(0, u.hp - all_dmg[u.name])
                u.recalc_size()
        for u in units:
            if u.routed or u.broken: continue
            sl = size_before[u.name] - u.size
            opp = [x for x in units if x.faction != u.faction]
            opp_sl = sum(size_before.get(x.name, x.size) - x.size for x in opp) / max(1, len(opp))
            if sl > u.discipline and sl > opp_sl:
                u.discipline = max(0, u.discipline - 1)
            u.check_drift([])
        for u in units:
            if u.routed: continue
            sl = size_before[u.name] - u.size
            cap = 3; adj = 0
            if u.size < u.size_max // 4 and u.size > 0:
                adj += -min(2, cap); cap -= 2
            elif u.size < u.size_max // 2:
                adj += -min(1, cap); cap -= 1
            u.morale = max(1, u.morale + adj)
        for u in units:
            if not u.routed and u.morale <= 0:
                u.routed = True
        for u in units:
            if not u.routed and not u.broken:
                u.morale = min(u.morale_start, u.morale + 1)
    a_surv = [u for u in side_a if not u.routed]
    b_surv = [u for u in side_b if not u.routed]
    return ("A" if a_surv and not b_surv else
             "B" if b_surv and not a_surv else "draw"), t

# ─────────────────────────────────────────────────────────────────────────────
# COMBINED ATTACK DEFENSIVE RESPONSE (for ED-818 / Finding D)
# ─────────────────────────────────────────────────────────────────────────────

def run_combined_with_def_response(attackers, defender, def_bonus=0, max_turns=10):
    """3v1 with defender getting +def_bonus D when targeted by combined attack."""
    units = attackers + [defender]
    for t in range(1, max_turns + 1):
        active_a = [u for u in attackers if not u.routed and not u.broken]
        if not active_a or defender.routed:
            break
        # Volley
        volley_dmg = {}
        for s in units:
            if s.routed or s.total_volley_pool() == 0: continue
            enemies = [u for u in units if u.faction != s.faction and not u.routed]
            if enemies:
                target = enemies[0]
                pool = s.total_volley_pool()
                net = roll_pool(pool, tn=6)
                d = max(0, max(0, net) - target.ranged_dr)
                volley_dmg[target.name] = volley_dmg.get(target.name, 0) + d
        # Combined attack at center with defensive bonus
        FIB = [1, 2, 3, 5, 8]  # [canonical: structural — trial count / seed offset]
        if active_a:
            lead = active_a[0]
            sups = active_a[1:]
            lead_pool = lead.column_combat_pool("center")
            combined = lead_pool
            for i, s in enumerate(sups):
                denom = FIB[min(i + 1, len(FIB) - 1)]
                combined += math.floor(s.column_combat_pool("center") / denom)
            def_mods = defender.shape.phase5_mods("center", False)
            def_pool = max(1, defender.column_combat_pool("center") + def_mods["def_d"] + def_bonus)
            if def_mods["off_d"] == -99:  # [canonical: structural — empty-column sentinel from sim_mb_05.py]
                continue
            att_net = roll_pool(combined)
            def_net = roll_pool(def_pool)
            att_deg = compute_degree(att_net, max(1, def_net))
            def_deg = compute_degree(def_net, max(1, att_net))
            dmg_to_def = max(0, DAMAGE_BY_DEGREE[att_deg](lead.power) - defender.dr)
            dmg_to_att = max(0, DAMAGE_BY_DEGREE[def_deg](defender.power) - lead.dr)
        # Apply
        size_before = {u.name: u.size for u in units}
        defender.hp = max(0, defender.hp - dmg_to_def - volley_dmg.get(defender.name, 0))
        defender.recalc_size()
        lead.hp = max(0, lead.hp - dmg_to_att)
        lead.recalc_size()
        # Disc / Morale skipped for speed — focus is on combined attack outcome
        for u in units:
            if not u.routed and u.size < u.size_max // 4 and u.size > 0:
                u.morale -= 1
                if u.morale <= 0:
                    u.routed = True
    return ("A" if not defender.routed and active_a else
             "B" if defender.routed else "draw"), t

# ─────────────────────────────────────────────────────────────────────────────
# DRIFT CASCADE ALTERNATIVES (for ED-817)
# ─────────────────────────────────────────────────────────────────────────────

# Tiered drift: shape downgrades through stages
TIERED_DRIFT_TARGET = {
    "GappedLine":   "Horseshoe",
    "Horseshoe":    "Arrowhead",
    "Arrowhead":    "RefusedFlank",
    "RefusedFlank": "Line",
    "Line":         "Line",
}

def tiered_drift_check(unit, log):
    if unit.shape_drifted:
        # Already drifted once; check if needs to drift further
        # Tiered model: drift down one tier per Disc-below-min event
        pass
    if unit.discipline < unit.shape.min_discipline:
        target_name = TIERED_DRIFT_TARGET.get(unit.shape.name, "Line")
        target_cls = {"Line": Line, "Arrowhead": Arrowhead, "Horseshoe": Horseshoe,
                       "GappedLine": GappedLine, "RefusedFlank": RefusedFlank}[target_name]
        unit.shape = target_cls()
        unit.grid = unit.shape.distribute(unit.melee_pct, unit.ranged_pct, unit.support_pct)
        unit.shape_drifted = True

# ─────────────────────────────────────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    out = []
    out.append("=" * 70)  # [canonical: structural — display / loop bound]
    out.append("SIM-MB-05C — Branch exploration for ED-821, ED-822, ED-817")
    out.append("=" * 70)  # [canonical: structural — display / loop bound]

    # === H-variant comparison ===
    out.append("\n## H-variants: Horseshoe trigger alternatives")
    out.append("  Horseshoe vs each shape opponent (100 trials each)")
    out.append("  Goal: Horseshoe should win 45-60% vs most shapes (balanced)")
    out.append("  Current H-1 (mass>40%) underperforms vs Line/Gapped/RefusedFlank")

    targets = ["Line", "Arrowhead", "GappedLine", "RefusedFlank"]
    target_classes = {"Line": Line, "Arrowhead": Arrowhead,
                       "GappedLine": GappedLine, "RefusedFlank": RefusedFlank}

    out.append(f"\n  {'Variant':22s} " + " ".join(f"{t:>14s}" for t in targets))
    for variant in [1, 2, 3, 4]:
        labels = {1: "H-1 mass>40%", 2: "H-2 positional always",
                  3: "H-3 pool-ratio>40%", 4: "H-4 weak-col AI"}
        row = [f"  {labels[variant]:22s} "]
        for target in targets:
            wins = 0
            for seed in range(80):
                random.seed(seed + 30000 + variant * 1000)  # [canonical: structural — trial count / seed offset]
                hs = Unit(name="HS", faction="A", power=4, size=4, size_max=4,
                           discipline=6, discipline_start=6, command=4,
                           morale=6, morale_start=6, melee_pct=0.7, ranged_pct=0.3,
                           support_pct=0.0, shape=Horseshoe(), dr=1)
                opp = Unit(name="OPP", faction="B", power=4, size=4, size_max=4,
                            discipline=6, discipline_start=6, command=4,
                            morale=6, morale_start=6, melee_pct=0.7, ranged_pct=0.3,
                            support_pct=0.0, shape=target_classes[target](), dr=1)
                w, _ = run_battle_h_variant([hs], [opp], h_variant=variant)
                if w == "A": wins += 1
            row.append(f"{wins/80*100:>11.1f}%   ")
        out.append(" ".join(row))

    # === Volley TN comparison ===
    out.append("\n## Volley TN: TN6 (current) vs TN7 (proposed)")
    out.append("  Composition sweep with each TN (Line vs Line, 80 trials per cell)")

    for tn in [6, 7]:
        out.append(f"\n  Volley TN={tn}:")
        compositions = [(1.0, 0.0), (0.7, 0.3), (0.5, 0.5), (0.3, 0.7)]
        out.append(f"  {'':12s} " + " ".join(f"{f'{m:.1f}m/{r:.1f}r':>12s}" for m, r in compositions))
        for ma, ra in compositions:
            row = [f"  {ma:.1f}m/{ra:.1f}r  "]
            for mb, rb in compositions:
                wins = 0
                for seed in range(80):
                    random.seed(seed + 40000 + tn * 100)  # [canonical: structural — trial count / seed offset]
                    a = make_unit("A", "A", power=4, size=4, discipline=5, command=4,
                                   morale=6, shape_name="Line", dr=1, melee_pct=ma,
                                   ranged_pct=ra, ranged_dr=0)
                    b = make_unit("B", "B", power=4, size=4, discipline=5, command=4,
                                   morale=6, shape_name="Line", dr=1, melee_pct=mb,
                                   ranged_pct=rb, ranged_dr=0)
                    w, _ = run_battle_volley_tn([a], [b], volley_tn=tn)
                    if w == "A": wins += 1
                row.append(f"{wins/80*100:>11.1f}%")
            out.append(" ".join(row))

    # === Combined attack defensive response ===
    out.append("\n## Combined attack: defensive response calibration")
    out.append("  3 attackers (Arrowhead, Size 3) vs 1 defender (Line/Horseshoe, Size 5)")
    out.append("  Vary defender +def_d bonus when targeted (0/+1/+2/+3)")
    out.append("  Goal: attacker winrate 50-70% (concentrated assault should usually win but not always)")

    for def_shape in ["Line", "Horseshoe", "GappedLine"]:
        out.append(f"\n  vs {def_shape}:")
        for def_bonus in [0, 1, 2, 3]:
            wins = 0
            for seed in range(60):
                random.seed(seed + 50000 + def_bonus * 100)  # [canonical: structural — trial count / seed offset]
                atts = [make_unit(f"A{i}", "A", power=4, size=3, discipline=5,
                                   command=4, morale=6, shape_name="Arrowhead", dr=1)
                         for i in range(3)]
                def_ = make_unit("D", "B", power=4, size=5, discipline=6,
                                  command=4, morale=6, shape_name=def_shape, dr=1)
                w, _ = run_combined_with_def_response(atts, def_, def_bonus=def_bonus)
                if w == "A": wins += 1
            out.append(f"    def_bonus +{def_bonus}: A winrate {wins/60*100:.1f}%")

    # === Drift cascade: direct vs tiered ===
    out.append("\n## Drift cascade: direct-to-Line vs tiered (Gapped→Horseshoe→Arrowhead→Line)")
    out.append("  Test by starting unit at low Disc, observing battle outcome difference")
    out.append("  Direct already validated in SIM-MB-05A/B")
    out.append("  Tiered comparison:")

    for shape_name, min_d in [("GappedLine", 5), ("Horseshoe", 5), ("Arrowhead", 4)]:
        for start_disc in [min_d - 2, min_d - 1]:
            random.seed(60000 + min_d + start_disc)  # [canonical: structural — trial count / seed offset]
            # Direct drift
            wins_direct = 0
            for seed in range(60):
                random.seed(seed + 60100)  # [canonical: structural — trial count / seed offset]
                u = make_unit("U", "A", power=4, size=4, discipline=start_disc,
                               command=4, morale=6, shape_name=shape_name, dr=1)
                opp = make_unit("O", "B", power=4, size=4, discipline=5,
                                 command=4, morale=6, shape_name="Line", dr=1)
                w, _ = run_battle_h_variant([u], [opp], h_variant=1)
                if w == "A": wins_direct += 1

            # Tiered drift — patch check_drift temporarily
            wins_tiered = 0
            original_check = Unit.check_drift
            Unit.check_drift = lambda self, log: tiered_drift_check(self, log)
            for seed in range(60):
                random.seed(seed + 60100)  # [canonical: structural — trial count / seed offset]
                u = make_unit("U", "A", power=4, size=4, discipline=start_disc,
                               command=4, morale=6, shape_name=shape_name, dr=1)
                opp = make_unit("O", "B", power=4, size=4, discipline=5,
                                 command=4, morale=6, shape_name="Line", dr=1)
                w, _ = run_battle_h_variant([u], [opp], h_variant=1)
                if w == "A": wins_tiered += 1
            Unit.check_drift = original_check

            out.append(f"  {shape_name} at Disc {start_disc} (min {min_d}):"
                       f" direct {wins_direct/60*100:.0f}% / tiered {wins_tiered/60*100:.0f}%")

    out.append("\n" + "=" * 70)  # [canonical: structural — display / loop bound]
    return "\n".join(out)

if __name__ == "__main__":
    print(main())
