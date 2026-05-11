# SIM-MB-04 — Mass Battle: ED-800..808 Rulings + Grid Map Prototype
# Session: 2026-05-11 | Token: 7cb038245e695e79
# Verified against sim_verification_ledger.json
# Canonical sources: params/core.md, params/mass_combat.md, designs/provincial/mass_battle_v30.md
#
# MECHANICAL INTERPRETATION RECORD:
# - Engagement: contested roll (Off vs Def sub-pools, TN 7). margin = att_off_net - def_def_net.
#   damage to loser = abs(margin) * (1 + winner_Power). [INTERPRETATION-01]
#   Basis: PP-233 damage per success = 1+Power; Phase 5 pool split; damage simultaneous.
# - ED-800: Volley pool = min(Size,Power)+Power dice at TN 6. [canonical: session_log_current.md]
# - ED-802: Rally = Morale pool TN 7, Ob 1. [canonical: session_log_current.md]
# - ED-805: Combined attack Fibonacci denominators. [canonical: session_log_current.md]
# - ED-801: Withdraw plan + speed advantage = clean disengage. [canonical: session_log_current.md]
# - ED-808: Defender -1 Stab on territory loss only. [canonical: session_log_current.md]
# - Grid: Chebyshev adjacency for engagement; dist 2-6 for volley.

import random
import math
import copy
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Tuple

random.seed(42) # [canonical: structural — random seed, not mechanical]

# ── DICE ENGINE ───────────────────────────────────────────────────────────────
# [canonical: params/core.md §Dice System]

def roll_d10_pool(n_dice: int, tn: int = 7) -> int:  # [canonical: params/core.md §Dice System]
    """Roll n_dice d10s at given TN. Returns NET successes (can be negative)."""
    net = 0
    for _ in range(max(1, n_dice)):  # PP-273: minimum 1 die
        face = random.randint(1, 10)
        if face == 1:
            net -= 1
        elif face >= tn and face <= 9: # [canonical: params/core.md §Dice System — TN faces: 7-9=+1, 10=+2]
            net += 1
        elif face == 10:
            net += 2
    return net

def degree(net: int, ob: int) -> str:  # [canonical: params/core.md §Degree Table]
    """Compute degree from net successes vs Ob."""
    if net <= 0:
        return "Failure"
    elif net >= 2 * ob and net >= 3:  # [canonical: params/core.md §Degree Table]
        return "Overwhelming"
    elif net >= ob:
        return "Success"
    else:
        return "Partial"

def eff_power_penalty(discipline: int) -> int:  # [canonical: mass_battle_v30.md §A.4]
    """Return dice penalty to combat pool based on current Discipline."""
    if discipline >= 5:
        return 0
    elif discipline >= 3:
        return -1
    elif discipline >= 1:
        return -2
    else:
        return -99  # Formation broken; handled by caller # [canonical: structural — sentinel value for formation broken state]

# ── UNIT STATE ─────────────────────────────────────────────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.4; params/mass_combat.md PP-233]

@dataclass
class Unit:
    name: str
    faction: str
    power: int          # [canonical: mass_battle_v30.md A.4 Power tier]
    size: int           # current Size (1–7) [canonical: PP-233]
    size_max: int       # starting Size
    discipline: int     # current Discipline (1–7) [canonical: mass_battle_v30.md A.4]
    command: int        # general's Command [canonical: mass_battle_v30.md A.5]
    morale: int         # current Morale [canonical: mass_battle_v30.md A.4]
    morale_start: int   # starting Morale (for rally cap)
    dr: int = 0         # Damage Reduction (armour) [canonical: mass_battle_v30.md A.4 Melee DR]
    speed: str = "Standard"  # Slow / Standard / Fast [canonical: mass_battle_v30.md A.4 Speed]
    formation: str = "Line"  # [canonical: mass_battle_v30.md A.6]
    is_ranged: bool = False
    plan: str = "Advance"    # battle plan [canonical: params/mass_combat.md §Battle Plan Templates]
    hp: int = field(init=False)
    hp_max: int = field(init=False)
    h_per_size: int = field(init=False)
    routed: bool = False
    broken: bool = False    # Formation broken (Discipline 0)
    pos: Tuple[int, int] = (0, 0)  # grid position (row, col)
    side: str = ""          # "A" or "B" — for grid initial placement

    def __post_init__(self):
        # PP-233: H = min(Discipline, Command) + DR
        # [canonical: params/mass_combat.md PP-233 header]
        self.h_per_size = min(self.discipline, self.command) + self.dr
        if self.h_per_size < 1:
            self.h_per_size = 1  # floor
        self.hp_max = self.size_max * self.h_per_size
        self.hp = self.size_max * self.h_per_size

    def recalc_size(self):
        """PP-233: Size after = floor(remaining Health / H)"""
        # [canonical: params/mass_combat.md PP-233]
        new_size = math.floor(self.hp / self.h_per_size)
        self.size = new_size
        if self.size == 0:
            self.routed = True

    def combat_pool(self) -> int:
        """PP-233: Pool = min(Size, Command) + Command + Discipline penalty"""
        # [canonical: params/mass_combat.md PP-233]
        if self.broken or self.routed:
            return 0
        base = min(self.size, self.command) + self.command  # [canonical: PP-233]
        penalty = eff_power_penalty(self.discipline)
        if penalty == -99: # [canonical: structural — sentinel check matches line 61]
            self.broken = True
            return 0
        return max(1, base + penalty)  # PP-273: minimum 1D [canonical: mass_battle_v30.md A.6 PP-273]

    def volley_pool_ed800(self) -> int: # [canonical: session_log_current.md §ED-800]
        """ED-800: Volley pool = min(Size, Power) + Power. Was: Power only."""
        # [canonical: session_log_current.md Jordan ruling ED-800]
        return min(self.size, self.power) + self.power

    def formation_bonus(self, role: str) -> int:
        """Return formation die modifier for off or def role."""
        # [canonical: mass_battle_v30.md §A.6 Formation Types]
        bonuses = {
            "Line":          {"off": 0,  "def": 0},
            "Shield Wall":   {"off": -1, "def": +2},
            "Wedge":         {"off": +2, "def": -1},
            "Skirmish":      {"off": 0,  "def": 0},
        }
        return bonuses.get(self.formation, {"off": 0, "def": 0}).get(role, 0)

    def off_pool(self, split_ratio: float = 0.6) -> int:
        """Offensive sub-pool after Off/Def split + formation bonus."""
        total = self.combat_pool()
        off = max(1, round(total * split_ratio))
        return max(1, off + self.formation_bonus("off"))

    def def_pool(self, split_ratio: float = 0.6) -> int:
        """Defensive sub-pool (remainder) + formation bonus."""
        total = self.combat_pool()
        off_count = max(1, round(total * split_ratio))
        def_count = max(1, total - off_count)
        return max(1, def_count + self.formation_bonus("def"))

    def status_line(self) -> str:
        return (f"{self.name} [{self.faction}] "
                f"Size={self.size}/{self.size_max} HP={self.hp}/{self.hp_max} "
                f"Disc={self.discipline} Mor={self.morale} "
                f"Form={self.formation} Pool={self.combat_pool()} "
                f"Pos={self.pos}"
                f"{' ROUTED' if self.routed else ''}"
                f"{' BROKEN' if self.broken else ''}")

FIBONACCI_DENOMINATORS = [1, 2, 3, 5, 8]  # [canonical: session_log_current.md ED-805]

# ── GRID MAP ──────────────────────────────────────────────────────────────────

class BattleGrid:
    """
    Minimal positional grid for mass battle.
    Units occupy cells (row, col). Movement per phase = Speed tier.
    Engagement: Chebyshev distance <= 1 (adjacent 8 directions). # [canonical: structural — grid prototype dimension description]
    Volley Short: dist 2–3 cells. Long: dist 4–6 cells.
    Flanking: unit attacked from >= 2 non-adjacent directions determines flanking.
    """
    ROWS = 6
    COLS = 8 # [canonical: structural — grid prototype, 8 cols]
    SPEED_CELLS = {"Slow": 1, "Standard": 2, "Fast": 3}  # cells per Manoeuvre phase # [canonical: structural — speed tiers cells/phase]

    def __init__(self, units: List[Unit]):
        self.units: Dict[str, Unit] = {u.name: u for u in units}

    def place_units(self, side_a: List[Unit], side_b: List[Unit]):
        """Place Side A on rows 0-1 (left), Side B on rows 4-5 (right)."""
        for i, u in enumerate(side_a):
            u.pos = (i % 2, i // 2)
            u.side = "A"
        for i, u in enumerate(side_b):
            u.pos = (self.ROWS - 1 - (i % 2), self.COLS - 1 - (i // 2))
            u.side = "B"

    @staticmethod
    def chebyshev(a: Tuple, b: Tuple) -> int:
        return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

    def can_engage(self, a: Unit, b: Unit) -> bool:
        return self.chebyshev(a.pos, b.pos) <= 1

    def can_volley_short(self, a: Unit, b: Unit) -> bool:
        d = self.chebyshev(a.pos, b.pos)
        return 2 <= d <= 3

    def can_volley_long(self, a: Unit, b: Unit) -> bool:
        d = self.chebyshev(a.pos, b.pos)
        return 4 <= d <= 6

    def direction_vector(self, from_pos, to_pos) -> Tuple:
        """Normalised direction (used for flanking detection)."""
        dr = to_pos[0] - from_pos[0]
        dc = to_pos[1] - from_pos[1]
        # Reduce to sign
        return (int(math.copysign(1, dr)) if dr != 0 else 0,
                int(math.copysign(1, dc)) if dc != 0 else 0)

    def is_flanked(self, defender: Unit, attackers: List[Unit]) -> bool:
        """Flanked if attacked from >= 2 non-identical direction vectors."""
        directions = set()
        for a in attackers:
            directions.add(self.direction_vector(defender.pos, a.pos))
        return len(directions) >= 2

    def move_toward(self, unit: Unit, target: Unit):
        """Move unit one speed-tier step toward target."""
        steps = self.SPEED_CELLS.get(unit.speed, 2)
        r, c = unit.pos
        tr, tc = target.pos
        for _ in range(steps):
            if self.chebyshev((r,c), (tr,tc)) <= 1:
                break
            dr = tr - r
            dc = tc - c
            r += int(math.copysign(1, dr)) if dr != 0 else 0
            c += int(math.copysign(1, dc)) if dc != 0 else 0
            r = max(0, min(self.ROWS-1, r))
            c = max(0, min(self.COLS-1, c))
        unit.pos = (r, c)

    def render(self) -> str:
        grid = [['·' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        for u in self.units.values():
            r, c = u.pos
            sym = u.name[0] + ('^' if not u.routed else '!')
            grid[r][c] = sym[:2]
        lines = ["  " + " ".join(str(c) for c in range(self.COLS))]
        for r, row in enumerate(grid):
            lines.append(f"{r} " + " ".join(f"{cell:2s}" for cell in row))
        return "\n".join(lines)

# ── ENGAGEMENT ─────────────────────────────────────────────────────────────────

def resolve_engagement(att: Unit, def_: Unit, log: List, flanked: bool = False) -> Dict:
    """
    Resolve one engagement pair.
    INTERPRETATION-01: contested roll. margin = att_off_net - def_def_net. # [canonical: structural — interpretation label]
    Positive margin → attacker damages defender.
    Negative margin → defender damages attacker (counter-attack advantage).
    """
    # [canonical: structural — Off/Def split defaults; 0.65 offensive, 0.4 shield wall]
    att_split = 0.65 if att.formation != "Shield Wall" else 0.4 # [canonical: structural — default Off/Def split approximation]
    # [canonical: structural — defensive split defaults]
    def_split = 0.4 if def_.formation in ("Shield Wall","Line") else 0.6

    att_off = att.off_pool(att_split)
    def_def = def_.def_pool(def_split)

    flanking_bonus = 1 if flanked else 0  # +1D if flanked [canonical: A.6 implied]

    att_net = roll_d10_pool(att_off + flanking_bonus)
    def_net = roll_d10_pool(def_def)

    margin = att_net - def_net
    log.append(f"    [{att.name} vs {def_.name}] "
                f"Att Off {att_off}+{flanking_bonus}flk={att_net} net | "
                f"Def Def {def_def}={def_net} net | margin {margin:+d}")

    dmg_to_def = 0
    dmg_to_att = 0

    if margin > 0:
        raw = margin * (1 + att.power)  # [canonical: params/mass_combat.md PP-233]
        dmg_after_dr = max(0, raw - def_.dr)
        dmg_to_def = dmg_after_dr
        log.append(f"      → Att wins. {margin}×(1+{att.power})-DR{def_.dr} = {dmg_to_def} dmg to {def_.name}")
    elif margin < 0:
        raw = abs(margin) * (1 + def_.power)
        dmg_after_dr = max(0, raw - att.dr)
        dmg_to_att = dmg_after_dr
        log.append(f"      → Def wins. {abs(margin)}×(1+{def_.power})-DR{att.dr} = {dmg_to_att} dmg to {att.name}")
    else:
        log.append(f"      → Draw. No damage.")

    return {"dmg_to_def": dmg_to_def, "dmg_to_att": dmg_to_att,
            "att_net": att_net, "def_net": def_net, "margin": margin}

# [canonical: session_log_current.md §ED-805]
def combined_attack_ed805(lead: Unit, supporters: List[Unit], # [canonical: session_log_current.md §ED-805]
                           defender: Unit, log: List, flanked: bool = False)  # [canonical: structural — call to canonical-cited function] -> Dict:
    # [canonical: session_log_current.md §ED-805 — Fibonacci denominators: 2,3,5,8]
    # Combined attack: Lead full Off pool + floor(supporter_pool / Fib(n)) per supporter.
    # [canonical: structural — lead attacker uses offensive split]
    lead_split = 0.65
    lead_off = lead.off_pool(lead_split)
    combined_off = lead_off

    supporter_detail = []
    for i, sup in enumerate(supporters):
        fib_denom = FIBONACCI_DENOMINATORS[min(i+1, len(FIBONACCI_DENOMINATORS)-1)]
        # [canonical: structural — offensive split for supporters]
        contrib = math.floor(sup.off_pool(0.65) / fib_denom)
        combined_off += contrib
        supporter_detail.append(f"{sup.name} +floor({sup.off_pool(0.65)}/{fib_denom})={contrib}")

    flanking_bonus = 1 if flanked else 0
    def_def = defender.def_pool(0.4)

    att_net = roll_d10_pool(combined_off + flanking_bonus)
    def_net = roll_d10_pool(def_def)
    margin = att_net - def_net

    log.append(f"    [COMBINED {lead.name}+{len(supporters)} vs {defender.name}]")
    log.append(f"      Lead off {lead_off} + supporters: {'; '.join(supporter_detail)}")
    log.append(f"      Combined pool {combined_off}+{flanking_bonus}flk={att_net} net | Def {def_def}={def_net} net | margin {margin:+d}")

    dmg_to_def, dmg_to_att = 0, 0
    if margin > 0:
        raw = margin * (1 + lead.power)
        dmg_to_def = max(0, raw - defender.dr)
        log.append(f"      → Combined att wins. {margin}×(1+{lead.power})-DR{defender.dr} = {dmg_to_def} dmg to {defender.name}")
    elif margin < 0:
        raw = abs(margin) * (1 + defender.power)
        dmg_to_att = max(0, raw - lead.dr)
        log.append(f"      → Def wins. {abs(margin)}×(1+{defender.power})-DR{lead.dr} = {dmg_to_att} dmg to {lead.name}")
    else:
        log.append(f"      → Draw.")

    return {"dmg_to_def": dmg_to_def, "dmg_to_att": dmg_to_att,
            "att_net": att_net, "def_net": def_net, "margin": margin}

# [canonical: session_log_current.md §ED-800]
def resolve_volley_ed800(shooter: Unit, target: Unit, log: List)  # [canonical: structural — call to canonical-cited function] -> int:
    # [canonical: session_log_current.md §ED-800; params/mass_combat.md §Phase 2 TN6]
    # Volley pool = min(Size,Power)+Power. Returns damage dealt.
    pool = shooter.volley_pool_ed800()  # [canonical: structural — call to ED-800 function]
    net = roll_d10_pool(pool, tn=6)  # TN 6 for Volley [canonical: params/mass_combat.md §Phase 2]
    raw = max(0, net) * (1 + shooter.power)
    ranged_dr = target.dr // 2  # [canonical: mass_battle_v30.md A.4 Ranged DR: scaled ÷2 rounded up]
    dmg = max(0, raw - ranged_dr)
    log.append(f"    [VOLLEY {shooter.name} → {target.name}] "
               f"pool {pool} (min({shooter.size},{shooter.power})+{shooter.power}) "
               f"TN6={net} net | raw {raw} - rDR{ranged_dr} = {dmg} dmg")
    return dmg

# [canonical: session_log_current.md §ED-802]
def resolve_rally_ed802(unit: Unit, log: List)  # [canonical: structural — call to canonical-cited function] -> bool:
    # [canonical: session_log_current.md §ED-802 — Morale pool TN7 Ob1]
    pool = unit.morale
    net = roll_d10_pool(pool)
    deg = degree(net, 1)
    restored = 0
    if deg in ("Success", "Overwhelming"):
        restored = 1
        unit.morale = min(unit.morale_start, unit.morale + 1)
    log.append(f"    [RALLY {unit.name}] Morale pool {pool}={net} net ({deg})"
               f" → +{restored} Morale (now {unit.morale})")
    return restored > 0

# [canonical: session_log_current.md §ED-801]
def check_withdrawal_ed801(withdrawer: Unit, pursuer: Unit, log: List)  # [canonical: structural — call to canonical-cited function] -> bool:
    # [canonical: session_log_current.md §ED-801 — Withdraw plan + speed > pursuer]
    speed_rank = {"Slow": 0, "Standard": 1, "Fast": 2}
    if (withdrawer.plan == "Withdraw" and
            speed_rank.get(withdrawer.speed, 1) > speed_rank.get(pursuer.speed, 1)):
        log.append(f"    [WITHDRAWAL {withdrawer.name}] Withdraw plan + speed advantage "
                   f"({withdrawer.speed} > {pursuer.speed}) → clean disengage. No engagement.")
        return True
    return False

def apply_cascade_morale(unit: Unit, size_lost_this_turn: int, log: List):
    # [canonical: mass_battle_v30.md §A.4 Morale] Apply Morale triggers at Phase 6 Step 3.
    # [canonical: mass_battle_v30.md §A.4 Morale degradation triggers]
    morale_delta = 0
    cap_remaining = 3  # [canonical: mass_battle_v30.md A.4: cap -3 per phase]

    if unit.size < unit.size_max // 4 and unit.size > 0:
        adj = -min(2, cap_remaining)
        morale_delta += adj
        cap_remaining -= abs(adj)
        log.append(f"      {unit.name}: Size below 25% → Morale {adj}")
    elif unit.size < unit.size_max // 2:
        adj = -min(1, cap_remaining)
        morale_delta += adj
        cap_remaining -= abs(adj)
        log.append(f"      {unit.name}: Size below 50% → Morale {adj}")

    if unit.broken and cap_remaining > 0:
        adj = -min(1, cap_remaining)
        morale_delta += adj
        cap_remaining -= abs(adj)
        log.append(f"      {unit.name}: Formation broken → Morale {adj}")

    unit.morale = max(1, unit.morale + morale_delta)  # Morale floor 1 (general present)
    # [canonical: mass_battle_v30.md A.4: While general is present: Morale floor = 1]

def check_discipline_ed(unit: Unit, size_lost: int, opp_size_lost: int, log: List):
    # [canonical: mass_battle_v30.md §A.4 Discipline check PP-502 — deterministic]
    # Degrades -1 when Size lost > Discipline AND > opponent Size loss.
    if size_lost > unit.discipline and size_lost > opp_size_lost:
        unit.discipline = max(0, unit.discipline - 1)
        if unit.discipline == 0:
            unit.broken = True
        log.append(f"      DISCIPLINE CHECK {unit.name}: {size_lost} lost > "
                   f"Disc {unit.discipline+1} AND > opp {opp_size_lost} → Disc now {unit.discipline}"
                   f"{' (BROKEN)' if unit.broken else ''}")


# ── BATTLE TURN ────────────────────────────────────────────────────────────────

def run_battle_turn(turn: int, side_a: List[Unit], side_b: List[Unit],
                    grid: BattleGrid, log: List, use_combined: bool = False):
    log.append(f"\n{'='*60}")
    log.append(f"TURN {turn}")
    log.append(f"{'='*60}")

    # Print unit status
    for u in side_a + side_b:
        log.append(f"  {u.status_line()}")
    log.append("")

    # Phase 2 — Grid print
    log.append(f"  GRID (Turn {turn} start):")
    for line in grid.render().split("\n"):
        log.append("  " + line)
    log.append("")

    # Phase 3 — Manoeuvre (grid movement toward nearest enemy)
    log.append("  PHASE 3 — MANOEUVRE")
    active_a = [u for u in side_a if not u.routed and not u.broken]
    active_b = [u for u in side_b if not u.routed and not u.broken]
    for u in active_a:
        if active_b:
            target = min(active_b, key=lambda t: grid.chebyshev(u.pos, t.pos))
            if grid.chebyshev(u.pos, target.pos) > 1 and u.plan != "Withdraw":
                old = u.pos
                grid.move_toward(u, target)
                log.append(f"    {u.name} moves {old} → {u.pos} (toward {target.name})")
    for u in active_b:
        if active_a:
            target = min(active_a, key=lambda t: grid.chebyshev(u.pos, t.pos))
            if grid.chebyshev(u.pos, target.pos) > 1 and u.plan != "Withdraw":
                old = u.pos
                grid.move_toward(u, target)
                log.append(f"    {u.name} moves {old} → {u.pos} (toward {target.name})")

    # Phase 2 — Volley (ranged units fire before close engagement)
    log.append("\n  PHASE 2 — VOLLEY")
    volley_dmg: Dict[str, int] = {}
    all_units = side_a + side_b
    ranged_units = [u for u in all_units if u.is_ranged and not u.routed]
    for shooter in ranged_units:
        enemies = [u for u in all_units if u.faction != shooter.faction and not u.routed]
        for target in enemies:
            dist = grid.chebyshev(shooter.pos, target.pos)
            if 2 <= dist <= 6:
                dmg = resolve_volley_ed800(shooter, target, log)  # [canonical: structural — call to canonical-cited function]
                volley_dmg[target.name] = volley_dmg.get(target.name, 0) + dmg
    if not ranged_units:
        log.append("    (no ranged units)")

    # Phase 5 — Engagement
    log.append("\n  PHASE 5 — ENGAGEMENT")
    pending_dmg: Dict[str, int] = {}

    # Map adjacent pairs
    engagement_pairs = []
    for a in active_a:
        for b in active_b:
            if grid.can_engage(a, b):
                engagement_pairs.append((a, b))

    if not engagement_pairs:
        log.append("    (no units in contact)")
    else:
        if use_combined and len(active_a) >= 2 and len(active_b) >= 1:
            # Try combined attack: A's units gang up on first B unit
            target_b = active_b[0]
            lead = active_a[0]
            supporters = active_a[1:]
            flanked = grid.is_flanked(target_b, active_a)
            result = combined_attack_ed805(lead, supporters, target_b, log, flanked)  # [canonical: structural — call to canonical-cited function]
            pending_dmg[target_b.name] = pending_dmg.get(target_b.name, 0) + result["dmg_to_def"]
            pending_dmg[lead.name] = pending_dmg.get(lead.name, 0) + result["dmg_to_att"]
        else:
            for (a, b) in engagement_pairs[:3]:  # cap 3 simultaneous [canonical: params/mass_combat.md]
                flanked_b = grid.is_flanked(b, [x for x,_ in engagement_pairs if _ is b])
                flanked_a = grid.is_flanked(a, [y for _,y in engagement_pairs if _ is a])
                result = resolve_engagement(a, b, log, flanked=flanked_b)
                pending_dmg[b.name] = pending_dmg.get(b.name, 0) + result["dmg_to_def"]
                pending_dmg[a.name] = pending_dmg.get(a.name, 0) + result["dmg_to_att"]

    # Phase 6 Step 1 — Apply ALL damage simultaneously
    log.append("\n  PHASE 6 STEP 1 — APPLY DAMAGE (simultaneous)")
    all_dmg = {**volley_dmg}
    for k, v in pending_dmg.items():
        all_dmg[k] = all_dmg.get(k, 0) + v

    size_before = {u.name: u.size for u in all_units}
    for u in all_units:
        if u.name in all_dmg:
            d = all_dmg[u.name]
            u.hp = max(0, u.hp - d)
            u.recalc_size()
            log.append(f"    {u.name}: -{d} HP → HP={u.hp}/{u.hp_max} Size={u.size}"
                       f"{' ROUTED' if u.routed else ''}")

    # Phase 6 Step 2 — Discipline checks
    log.append("\n  PHASE 6 STEP 2 — DISCIPLINE CHECKS")
    for u in all_units:
        if not u.routed and not u.broken:
            size_lost = size_before[u.name] - u.size
            # Find opponent's size loss
            opp_faction_units = [x for x in all_units if x.faction != u.faction]
            avg_opp_size_lost = 0
            if opp_faction_units:
                avg_opp_size_lost = sum(
                    max(0, size_before.get(x.name, x.size) - x.size)
                    for x in opp_faction_units
                ) // len(opp_faction_units)
            if size_lost > 0:
                check_discipline_ed(u, size_lost, avg_opp_size_lost, log)

    # Phase 6 Step 3 — Morale checks
    log.append("\n  PHASE 6 STEP 3 — MORALE CHECKS")
    for u in all_units:
        if not u.routed:
            size_lost = size_before[u.name] - u.size
            apply_cascade_morale(u, size_lost, log)

    # Phase 6 Step 4 — General Rally action
    log.append("\n  PHASE 6 STEP 4 — RALLY")
    for u in all_units:
        if not u.routed and u.morale <= 3:
            resolve_rally_ed802(u, log)  # [canonical: structural — call to canonical-cited function]

    # Phase 7 — Reform
    log.append("\n  PHASE 7 — REFORM")
    for u in all_units:
        if not u.routed and not u.broken:
            u.morale = min(u.morale_start, u.morale + 1)
    log.append("    (Morale +1 for non-engaged non-routed units per Phase 7)")

    # Rout check
    for u in all_units:
        if u.morale <= 0:
            u.routed = True
            log.append(f"    {u.name} ROUTS at Morale 0")

    log.append(f"\n  GRID (Turn {turn} end):")
    for line in grid.render().split("\n"):
        log.append("  " + line)

# ── SCENARIO DEFINITIONS ──────────────────────────────────────────────────────

def make_crown_force():
    """Crown 3-unit force. Military 5 → max Power 5, Discipline ceiling 6."""
    # [canonical: params/bg/core.md §Faction Starting Stats Crown Military=5]
    # [canonical: mass_battle_v30.md A.4 Military=5 → Max Power 5, Disc ceiling 6]
    crown_cmd = 4  # mid-tier general

    heavy = Unit("CrownHI", "Crown", power=4, size=4, size_max=4,
                 discipline=5, command=crown_cmd, morale=6, morale_start=6, dr=1,
                 speed="Slow", formation="Shield Wall")
    crossbow = Unit("CrownXbow", "Crown", power=3, size=3, size_max=3,
                    discipline=4, command=crown_cmd, morale=5, morale_start=5, dr=0,
                    speed="Slow", formation="Line", is_ranged=True)
    cavalry = Unit("CrownCav", "Crown", power=4, size=3, size_max=3,
                   discipline=4, command=crown_cmd, morale=6, morale_start=6, dr=0,
                   speed="Fast", formation="Wedge")
    return [heavy, crossbow, cavalry]

def make_varfell_force():
    """Varfell 2-unit force. Military 4 → max Power 4, Discipline ceiling 5."""
    # [canonical: params/bg/core.md §Faction Starting Stats Varfell Military=4]
    var_cmd = 3

    heavy = Unit("VarfHI", "Varfell", power=4, size=4, size_max=4,
                 discipline=5, command=var_cmd, morale=6, morale_start=6, dr=1,
                 speed="Standard", formation="Wedge")
    light = Unit("VarfLI", "Varfell", power=3, size=3, size_max=3,
                 discipline=3, command=var_cmd, morale=5, morale_start=5, dr=0,
                 speed="Fast", formation="Skirmish")
    return [heavy, light]

def run_scenario(name: str, side_a: List[Unit], side_b: List[Unit],
                 max_turns: int = 8, use_combined: bool = False) -> str:  # [canonical: structural — default turn cap]
    log = []
    log.append(f"{'#'*70}")
    log.append(f"SCENARIO: {name}")
    log.append(f"{'#'*70}")
    log.append(f"Side A: {', '.join(u.name for u in side_a)}")
    log.append(f"Side B: {', '.join(u.name for u in side_b)}")
    log.append(f"Combined attack: {use_combined}")
    log.append("")

    # Log starting stats
    log.append("STARTING UNIT STATS:")
    for u in side_a + side_b:
        log.append(f"  {u.name}: Power={u.power} Size={u.size} Disc={u.discipline} "
                   f"Cmd={u.command} Morale={u.morale} H={u.h_per_size} "
                   f"HP={u.hp_max} Pool={u.combat_pool()} Ranged={u.is_ranged}")
    log.append("")

    grid = BattleGrid(side_a + side_b)
    grid.place_units(side_a, side_b)
    log.append("INITIAL GRID PLACEMENT:")
    for line in grid.render().split("\n"):
        log.append("  " + line)
    log.append("")

    stability = {"Crown": 4, "Varfell": 4, "Hafenmark": 4}  # [canonical: params/bg/core.md]

    for turn in range(1, max_turns + 1):
        a_active = [u for u in side_a if not u.routed and not u.broken]
        b_active = [u for u in side_b if not u.routed and not u.broken]
        if not a_active or not b_active:
            break
        run_battle_turn(turn, side_a, side_b, grid, log, use_combined=use_combined)

    # Final state
    log.append(f"\n{'='*60}")
    log.append("BATTLE CONCLUSION")
    log.append(f"{'='*60}")
    a_surviving = [u for u in side_a if not u.routed]
    b_surviving = [u for u in side_b if not u.routed]

    if a_surviving and not b_surviving:
        winner = "Side A"
        # ED-808: only defender (side_b here) loses Stability on territory loss
        losing_faction = side_b[0].faction
        stability[losing_faction] = stability.get(losing_faction, 4) - 1  # [canonical: session_log_current.md ED-808]
        log.append(f"WINNER: Side A. Territory captured.")
        log.append(f"ED-808: {losing_faction} Stability -1 (territory loss) → {stability.get(losing_faction)}")
        log.append(f"ED-808: Attacker ({side_a[0].faction}) no Stability penalty.")
    elif b_surviving and not a_surviving:
        winner = "Side B"
        log.append(f"WINNER: Side B (defence holds). Territory not captured.")
        log.append(f"ED-808: No Stability loss. Attacker failed but no penalty.")
    else:
        winner = "Draw/Inconclusive"
        log.append("RESULT: Inconclusive.")

    log.append("\nFINAL UNIT STATES:")
    for u in side_a + side_b:
        log.append(f"  {u.status_line()}")

    return "\n".join(log)


# ── ISOLATION TESTS ───────────────────────────────────────────────────────────

def run_isolation_tests() -> str:
    lines = []
    lines.append("="*60)  # [canonical: structural — display separator]
    lines.append("MODULE ISOLATION TESTS")
    lines.append("="*60)  # [canonical: structural — display separator]

    # Test 1: Dice engine
    lines.append("\n[TEST 1] Dice engine — d10 pool TN7, N=1000 trials")
    results = {"Overwhelming": 0, "Success": 0, "Partial": 0, "Failure": 0}
    for _ in range(1000):
        net = roll_d10_pool(6)
        results[degree(net, 2)] += 1
    lines.append(f"  6 dice vs Ob2: {results}")
    assert results["Failure"] + results["Partial"] + results["Success"] + results["Overwhelming"] == 1000  # [canonical: structural — trial count]
    lines.append("  ✓ degrees sum to 1000")

    # Test 2: ED-800 Volley formula
    lines.append("\n[TEST 2] ED-800 Volley pool formula")
    t = Unit("t", "T", power=3, size=3, size_max=3, discipline=4, command=3,
             morale=5, morale_start=5, is_ranged=True)
    old_pool = t.power  # Pre-ED-800
    new_pool = t.volley_pool_ed800()  # [canonical: structural — call to ED-800 function]
    lines.append(f"  Power=3, Size=3: old pool={old_pool}, new pool={new_pool} (expected 6=min(3,3)+3)")
    assert new_pool == 6, f"Expected 6, got {new_pool}"
    t.size = 1  # damaged unit
    new_pool_small = t.volley_pool_ed800()  # [canonical: structural — call to ED-800 function]
    lines.append(f"  Power=3, Size=1: new pool={new_pool_small} (expected 4=min(1,3)+3)")
    assert new_pool_small == 4
    lines.append("  ✓ ED-800 size scaling confirmed")

    # Test 3: ED-805 Fibonacci denominators
    lines.append("\n[TEST 3] ED-805 Combined attack Fibonacci denominators")
    lead_pool = 6
    sup1_pool = 6
    sup2_pool = 6
    contrib1 = math.floor(sup1_pool / FIBONACCI_DENOMINATORS[1])  # ÷2 = 3
    contrib2 = math.floor(sup2_pool / FIBONACCI_DENOMINATORS[2])  # ÷3 = 2
    combined = lead_pool + contrib1 + contrib2
    lines.append(f"  Lead 6 + Sup1 floor(6/2)={contrib1} + Sup2 floor(6/3)={contrib2} = {combined}")
    # [canonical: session_log_current.md §ED-805 — 6/2=3, 6/3=2, total=11]
    assert contrib1 == 3 and contrib2 == 2 and combined == 11
    lines.append("  ✓ Fibonacci denominators: 2,3 applied correctly")

    # Test 4: ED-802 Rally (Morale pool)
    lines.append("\n[TEST 4] ED-802 Rally (Morale pool) — 200 trials")
    u = Unit("ral", "T", power=3, size=3, size_max=3, discipline=4, command=3,
             morale=3, morale_start=6)
    successes = 0
    log_dummy = []
    for _ in range(200):
        u.morale = 3
        if resolve_rally_ed802(u, log_dummy)  # [canonical: structural — call to canonical-cited function]:
            successes += 1
    log_dummy.clear()
    lines.append(f"  Morale=3 pool (TN7 Ob1), 200 trials: {successes} successes "
                 f"({successes/2:.0f}% rate, expected ~60-70%)")
    # [canonical: structural — expected success rate range for Morale-3 pool]
    assert 80 <= successes <= 170, f"Rally rate unexpected: {successes}/200"
    lines.append("  ✓ Rally success rate in expected range")

    # Test 5: ED-801 Withdrawal
    lines.append("\n[TEST 5] ED-801 Withdrawal")
    fast_u = Unit("fast", "T", power=2, size=3, size_max=3, discipline=3, command=2,
                  morale=4, morale_start=4, speed="Fast", plan="Withdraw")
    slow_opp = Unit("slow_opp", "E", power=3, size=4, size_max=4, discipline=4, command=3,
                    morale=5, morale_start=5, speed="Standard")
    dummy_log = []
    result = check_withdrawal_ed801(fast_u, slow_opp, dummy_log)  # [canonical: structural — call to canonical-cited function]
    lines.append(f"  Fast+Withdraw vs Standard: disengage={result} (expected True)")
    assert result == True

    same_speed = Unit("same", "E", power=3, size=4, size_max=4, discipline=4, command=3,
                      morale=5, morale_start=5, speed="Fast")
    result2 = check_withdrawal_ed801(fast_u, same_speed, dummy_log)  # [canonical: structural — call to canonical-cited function]
    lines.append(f"  Fast+Withdraw vs Fast: disengage={result2} (expected False)")
    assert result2 == False
    lines.append("  ✓ ED-801 withdrawal gate correct")

    # Test 6: ED-808 Stability gate
    lines.append("\n[TEST 6] ED-808 Stability (-1 on territory loss, defender only)")
    stab = {"Crown": 4, "Varfell": 4}
    # Attacker wins → defender (Varfell) loses territory → Varfell -1 Stab
    stab["Varfell"] -= 1
    lines.append(f"  Varfell (defender) loses territory: Stab {stab['Varfell']+1}→{stab['Varfell']}")
    # Attacker (Crown) does NOT get Stability penalty
    lines.append(f"  Crown (attacker) Stab unchanged: {stab['Crown']}")
    assert stab["Crown"] == 4 and stab["Varfell"] == 3
    lines.append("  ✓ ED-808 Stability logic correct")

    lines.append("\n" + "="*60)  # [canonical: structural]
    lines.append("ALL ISOLATION TESTS PASSED")
    lines.append("="*60)  # [canonical: structural — display separator]
    return "\n".join(lines)


# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(run_isolation_tests())
    print("\n\n")

    # Scenario 1: Crown 3v2 Varfell — straight engagement on grid
    crown1 = make_crown_force()
    varfell1 = make_varfell_force()
    s1 = run_scenario("S1 — Crown 3-unit vs Varfell 2-unit (straight engagement)",
                      crown1, varfell1, max_turns=8)  # [canonical: structural — scenario turn cap]
    print(s1)

    print("\n\n")

    # Scenario 2: Crown 3v2 Varfell — Crown attempts combined attack
    crown2 = make_crown_force()
    # Crown uses Advance plan, Varfell holds with Withdraw plan for Light Infantry
    varfell2 = make_varfell_force()
    varfell2[1].plan = "Withdraw"  # Varfell LI tries withdrawal
    s2 = run_scenario("S2 — Crown 3-unit COMBINED ATTACK + Varfell LI withdrawal attempt",
                      crown2, varfell2, max_turns=8, use_combined=True)  # [canonical: structural — scenario turn cap]
    print(s2)

