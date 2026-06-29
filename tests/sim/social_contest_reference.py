#!/usr/bin/env python3
"""
social_contest_reference.py — clean-room REFERENCE implementation of the CANONICAL social contest
(designs/scene/social_contest_v30.md + params/contest*, as patched 2026-06-23).

Purpose: make the Layer-B-full factors of the test matrix RUNNABLE — the derived-resource economy
(Composure / Concentration / Rattled / Spent / strain), the canonical bonus-dice stack
(genre / orientation / Recall / Findings / Resonant / Momentum), the interaction types
(CLASH / REINFORCE / CROSS / TIE), resistance erosion (ED-864), the Doubt Marker, rolled
first-to-speak — and to emit the downstream RIPPLE flags (Obligation / Domain Echo / MS
co-movement / Conviction Scar / Contest Fatigue).

This is a REFERENCE model for sensitivity analysis, NOT the shipping engine and NOT the groundup
σ-engine. It implements the canonical rules as written (success-count d10, TN 7); where canon is
silent it takes the minimal documented choice, flagged inline with [REF].
"""
from __future__ import annotations
import random
from dataclasses import dataclass, field
from typing import Optional

TN = 7  # §3 standard

# ---- derived scores (as patched) ----------------------------------------
def composure(cha: int) -> int:              # §6 / derived_stats §5.1
    return cha * 3
def concentration_max(focus: int, spirit: int) -> int:   # §4 / ED-902
    return 3 * focus + 2 * spirit
def cha_mod(cha: int) -> int:                # §4 CLASH, ×3-scaled (C2/ED-891)
    return max(0, (cha - 3) // 2) * 3
def foc_def(focus: int) -> int:              # §4 CLASH, ×3-scaled (C2/ED-891)
    return (focus // 2) * 3

CONC_DRAIN = 5       # §4 / ED-890: −5 per exchange
CONC_DRAIN_LOSS = 5  # −5 additional on loss


@dataclass
class Orator:
    side: str                 # 'A' / 'B'
    primary: int = 4          # primary attribute (by adjudicator type)
    history: int = 3          # raw history points (pool adds history + 3)
    cha: int = 4
    focus: int = 4
    spirit: int = 3
    attunement: int = 4
    genre: str = "Memory"     # Memory | Projection
    orientation: str = "Revealing"   # Revealing | Obscuring
    uses_recall: bool = False  # +2D citation
    findings: int = 0          # 0..2, Exchange 1 only
    resonant: bool = False     # Resonant-Style targeting (+1D; on win → Scar)
    momentum: int = 0          # auto-successes spent per exchange [REF: flat spend]


@dataclass
class Venue:
    proceeding: str = "Formal"     # Formal | Grand | RoyalAudience | Tribunal | ...
    exchanges: int = 3
    resistance0: int = 1           # audience resistance (avg Stability rounded −1)
    start_track: int = 5
    primary_genre: str = "Memory"
    boost_axis: Optional[str] = None     # 'genre' | 'orientation' | None
    boost_value: Optional[str] = None    # e.g. 'Memory' or 'Obscuring'
    erosion: bool = True                 # ED-864 per-exchange resistance erosion


@dataclass
class Result:
    winner: Optional[str]          # 'A' | 'B' | None (compromise)
    final_track: int
    decisive: bool
    total_victory: bool
    exchanges_run: int
    incapacitated: Optional[str]   # side rattled out, or None
    spent_events: int
    max_rattled: int
    strain_dealt: dict             # side -> total strain taken
    # ripple flags
    obligation: bool = False
    ms_comove: bool = False
    domain_echo: Optional[str] = None   # 'mandate' | 'domain_action' | None
    scar: bool = False
    contest_fatigue: Optional[str] = None
    interaction_seen: dict = field(default_factory=dict)


def _bonus_dice(o: Orator, v: Venue, exchange_idx: int) -> int:
    b = 0
    if o.genre == v.primary_genre:        # §2 primary genre +1D
        b += 1
    if v.boost_axis == "genre" and o.genre == v.boost_value:        # audience boost +1D
        b += 1
    elif v.boost_axis == "orientation" and o.orientation == v.boost_value:
        b += 1
    b = min(b, 2)                         # genre + audience cap +2
    if o.uses_recall:
        b += 2                            # §3 Recall +2D
    if o.resonant:
        b += 1                            # Resonant +1D (extensions)
    if exchange_idx == 1:
        b += min(o.findings, 2)           # §9.1 Findings, Exchange 1 only
    return b


def _interaction(a: Orator, b: Orator) -> str:
    if a.genre != b.genre:
        return "CROSS"
    return "REINFORCE" if a.orientation == b.orientation else "CLASH"


def _roll(pool: int, rng: random.Random) -> int:
    pool = max(1, pool)                   # core engine pool floor 1D
    return sum(1 for _ in range(pool) if rng.randint(1, 10) >= TN)


def run_reference_contest(a: Orator, b: Orator, v: Venue, rng: Optional[random.Random] = None) -> Result:
    rng = rng or random.Random()
    track = v.start_track
    comp = {"A": composure(a.cha), "B": composure(b.cha)}
    strain = {"A": 0, "B": 0}
    rattled = {"A": 0, "B": 0}
    conc = {"A": concentration_max(a.focus, a.spirit),
            "B": concentration_max(b.focus, b.spirit)}
    spent_next = {"A": False, "B": False}   # Spent penalty applies next exchange
    spent_events = 0
    doubt_on = {"A": False, "B": False}     # a Doubt Marker sitting on this side (reduces their next win margin)
    inter_seen: dict = {}

    # §5 first-to-speak: rolled Attunement vs Attunement, higher acts last (holds the marker)
    fa, fb = _roll(a.attunement, rng), _roll(b.attunement, rng)
    fts = "A" if fa >= fb else "B"

    incapacitated = None
    n = 0
    for n in range(1, v.exchanges + 1):
        res = max(0, v.resistance0 - ((n - 1) // 2)) if v.erosion else v.resistance0  # ED-864
        inter = _interaction(a, b)
        inter_seen[inter] = inter_seen.get(inter, 0) + 1

        def pool_for(o: Orator, side: str) -> int:
            p = 2 * o.primary + o.history + 3 + _bonus_dice(o, v, n)
            p -= rattled[side]                       # −1D per Rattled level (M1)
            if spent_next[side]:                     # Spent: −2D self this exchange
                p -= 2
            other = "B" if side == "A" else "A"
            if spent_next[other]:                    # opponent Spent → +1D to me
                p += 1
            return p

        a_net = _roll(pool_for(a, "A"), rng) + a.momentum
        b_net = _roll(pool_for(b, "B"), rng) + b.momentum
        # clear the spent penalty after it applied this exchange
        for s in ("A", "B"):
            if spent_next[s]:
                spent_next[s] = False

        loser = None
        if inter == "CROSS":
            ea, eb = a_net // 2, b_net // 2
            ma, mb = max(0, ea - res), max(0, eb - res)
            if ma == mb:
                track += 1 if fts == "A" else -1     # TIE-like: toward first-to-speak
            elif ma > mb:
                if a.orientation == "Obscuring":     # Obscuring CROSS → Doubt Marker, no movement
                    doubt_on["B"] = True
                else:
                    track += (ma - mb)
                fts = "A"
            else:
                if b.orientation == "Obscuring":
                    doubt_on["A"] = True
                else:
                    track -= (mb - ma)
                fts = "B"
            # CROSS: no strain
        else:
            margin = abs(a_net - b_net)
            if a_net == b_net:                        # TIE
                strain["A"] += 1; strain["B"] += 1
                track += 1 if fts == "A" else -1
            else:
                winner = "A" if a_net > b_net else "B"
                loser = "B" if winner == "A" else "A"
                wo = a if winner == "A" else b
                lo = b if winner == "A" else a
                eff_margin = margin
                if doubt_on[winner]:                  # Doubt Marker: −2 to winner's margin before resistance
                    eff_margin = max(0, eff_margin - 2); doubt_on[winner] = False
                move = max(0, eff_margin - res)
                track += move if winner == "A" else -move
                base = (eff_margin - 1) if inter == "REINFORCE" else eff_margin   # REINFORCE base margin−1
                # §4: strain = base margin + winner Cha-mod − loser Focus-defence, min 0 (×3-scaled)
                st = max(0, max(0, base) + cha_mod(wo.cha) - foc_def(lo.focus))
                strain[loser] += st
                fts = winner

        # Rattled check (strain ≥ Composure → mark, carry excess)
        for s in ("A", "B"):
            while strain[s] >= comp[s] and rattled[s] < 2:
                strain[s] -= comp[s]; rattled[s] += 1
            if rattled[s] >= 2:
                incapacitated = s
        # Concentration depletion / Spent
        for s in ("A", "B"):
            drain = CONC_DRAIN + (CONC_DRAIN_LOSS if s == loser else 0)
            conc[s] -= drain
            if conc[s] <= 0:
                spent_events += 1
                spent_next[s] = True
                conc[s] = concentration_max(a.focus if s == "A" else b.focus,
                                            a.spirit if s == "A" else b.spirit)

        track = max(0, min(10, track))
        if incapacitated:
            track = 0 if incapacitated == "A" else 10   # rattled-out side loses
            break

    # §6 resolution
    if track >= 7:
        winner = "A"
    elif track <= 3:
        winner = "B"
    else:
        winner = None
    decisive = winner is not None
    total = track >= 9 or track <= 1

    r = Result(winner=winner, final_track=track, decisive=decisive, total_victory=total,
               exchanges_run=n, incapacitated=incapacitated, spent_events=spent_events,
               max_rattled=max(rattled.values()), strain_dealt=dict(strain),
               interaction_seen=inter_seen)

    # ---- ripple (§6, §6.1) ----
    if decisive and v.proceeding in ("Formal", "Grand"):
        r.obligation = True                                   # §6.1 binding Obligation
    if decisive:
        won = a if winner == "A" else b
        if won.genre == "Memory":
            r.ms_comove = True                                # §6 Memory → MS +1 (retention)
            r.domain_echo = "mandate"                         # §6 Decisive+Memory → Mandate +1
        else:
            r.domain_echo = "domain_action"                   # §6 Decisive+Projection → +1D DA
            r.ms_comove = True                                # [REF] Projection MS +1 if Thread-sensitive (assume on)
        if won.resonant:
            r.scar = True                                     # §6.2 Resonant-style decisive → Conviction Scar
    if total:
        r.contest_fatigue = "B" if winner == "A" else "A"     # §6 Total Victory → loser Contest Fatigue
    return r


if __name__ == "__main__":
    # tiny self-check
    rng = random.Random(1)
    a = Orator("A", primary=5, genre="Memory", orientation="Revealing", uses_recall=True)
    b = Orator("B", primary=4, genre="Memory", orientation="Obscuring")
    v = Venue(primary_genre="Memory", boost_axis="orientation", boost_value="Revealing")
    res = run_reference_contest(a, b, v, rng)
    print("self-check:", res.winner, "track", res.final_track, "interaction", res.interaction_seen,
          "obligation", res.obligation, "spent", res.spent_events)
