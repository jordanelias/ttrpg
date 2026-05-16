"""
WP-1 (F8.4 emit-events) — Foundation refactor scaffold.

Comparative-audit plan: designs/audit/2026-05-15-mb-comparative-audit/plan.md
Source audit:          designs/audit/2026-05-15-mb-comparative-audit/audit.md (SHA ec1a3beb)

Scope of THIS file:
  • Define BattleOutcome surface (the F8.4 emit dataclass).
  • Define StrategicLayer.on_battle_resolved(outcome).
  • Implement the F7.1 Military-ceiling ±2 handler (§A.14) as proof of unlock,
    per plan WP-1 acceptance criteria.
  • Stub remaining strategic-layer handlers with explicit pointers to their
    owning WPs.

Deliberately NOT in this file (per plan Phase α gating):
  • F2.1 axis split (Unit.spatial_pattern × Unit.combat_mode)
      → blocked by canon decision Q1 (damage formula direction)
  • F2.2 class taxonomy (UnitClass with class-dependent Dmg Mod)
      → blocked by canon decision Q2 (PP-233 vs PARAMS-GAP-05 drift)
  • Concrete strategic-state mutations beyond Military cap
      → WP-2 (calibration), WP-4 (terrain), WP-5 (Thread), WP-6 (persistence)

Bottom-up sanctity (M-C / §M-9):
  Every BattleOutcome field derives from a battle-resolution primitive.
  No top-down "this looks like a strategic event" recognition. The
  StrategicLayer is a sink; the emitter composes from per-unit state.

Canon refs:
  §A.14 (Military ±2, Discipline, Mandate), §A.14b (hostile Treasury),
  §A.14c (Levy offensive restriction), §E.1 (Conquest cascade),
  §A.10 EDGE-05 (Gap registration), peninsular §3.1 (Substrate Fracture),
  peninsular §3.2 (Vulnerability Signal IP), peninsular §4.1 (Turmoil Strain).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Literal, Optional


# ── Result enum ───────────────────────────────────────────────────────────────


class BattleResult(Enum):
    DECISIVE_WIN     = "decisive_win"      # attacker wins decisively
    MARGINAL_WIN     = "marginal_win"      # attacker wins marginally
    DRAW             = "draw"
    MARGINAL_LOSS    = "marginal_loss"     # defender wins marginally
    DECISIVE_LOSS    = "decisive_loss"     # defender wins decisively
    CONQUEST         = "conquest"          # attacker takes territory (§E.1 cascade)


# ── Snapshots ─────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class UnitSnapshot:
    """End-of-battle state per unit. Source for F7.4 Discipline persistence,
    F7.2 Experience progression, F7.3 Reinforcement seed.

    Bottom-up primitive: every field a direct readout of unit state at the
    battle-resolution boundary.
    """
    unit_id:           str
    faction_id:        str
    size_start:        int
    size_end:          int
    discipline_end:    int                                # 0..100
    experience_state:  Literal["fresh", "seasoned", "veteran"]
    destroyed:         bool


@dataclass(frozen=True)
class CasualtyTotals:
    attacker_size_lost:  int
    defender_size_lost:  int
    attacker_size_start: int
    defender_size_start: int

    @property
    def attacker_ratio(self) -> float:
        return self.attacker_size_lost / max(1, self.attacker_size_start)

    @property
    def defender_ratio(self) -> float:
        return self.defender_size_lost / max(1, self.defender_size_start)


# ── The F8.4 surface ──────────────────────────────────────────────────────────


@dataclass(frozen=True)
class BattleOutcome:
    """The F8.4 emit-events dataclass.

    Captures everything required for strategic-layer effects canonized in
    §A.14, §A.14b, §A.14c, §E.1, §A.10 EDGE-05, peninsular §3.1/§3.2/§4.1.

    Deltas are computed by `emit_outcome_events` from primitive end-of-battle
    state; this WP implements the F7.1 Military handler, and stubs the rest
    so downstream WPs have an explicit attach point.
    """
    # Identity
    battle_id:         str
    territory_id:      str
    attacker_faction:  str
    defender_faction:  str

    # Outcome
    result:            BattleResult
    winner_faction:    Optional[str]                       # None on draw
    loser_faction:     Optional[str]                       # None on draw

    # Aggregates
    casualties:        CasualtyTotals
    units:             tuple[UnitSnapshot, ...]

    # §A.14 — Military ceiling delta (capped ±2 / battle, F7.1 handler implemented)
    military_delta_winner: int = 0
    military_delta_loser:  int = 0

    # §A.14 — Mandate -1 on decisive loss / conquest (WP-2 handler)
    mandate_delta_loser:   int = 0

    # §E.1 — Conquest cascade flags (WP-6 handler)
    substrate_fracture_loser: bool = False                 # peninsular §3.1 MS-1
    conquerors_accord:        bool = False                 # §E.1 Accord = 1
    defenders_accord:         bool = False                 # §E.1 Order -1

    # peninsular §3.2 / §4.1 — territory-aware deltas (WP-6 handler)
    vulnerability_signal_ip: int = 0
    turmoil_strain_delta:    int = 0

    # §A.10 EDGE-05 — Thread gap registrations (WP-5 handler)
    gap_registrations: tuple[tuple[str, str], ...] = field(default_factory=tuple)

    # §A.14b — hostile-territory Treasury cost to winner (WP-6 handler)
    treasury_delta_winner: int = 0

    # Editorial
    canon_refs: tuple[str, ...] = (
        "§A.14", "§A.14b", "§A.14c", "§E.1", "§A.10 EDGE-05",
        "peninsular §3.1", "peninsular §3.2", "peninsular §4.1",
    )


# ── Strategic layer ───────────────────────────────────────────────────────────


@dataclass
class FactionState:
    """Minimum surface to validate F7.1 Military cap. Real FactionState lives
    in the strategic-layer skill; this is a stand-in for verification only.
    """
    faction_id:       str
    military:         int                                  # 0..10 per canon
    mandate:          int
    treasury:         int
    morale_substrate: int
    accord:           int = 0
    order:            int = 0


class StrategicLayer:
    """Sink for F8.4 events.

    WP-1 implements only the F7.1 Military-cap handler. Other deltas are
    explicitly stubbed; each stub logs its owning WP so downstream
    implementers have a clean attach point.
    """
    def __init__(self, factions: dict[str, FactionState]) -> None:
        self.factions: dict[str, FactionState] = factions
        self.log: list[str] = []

    # Public entry — F8.4 contract
    def on_battle_resolved(self, outcome: BattleOutcome) -> None:
        self._apply_military_delta(outcome)               # F7.1 — implemented
        self._stub_mandate(outcome)                       # WP-2 (§A.14)
        self._stub_conquest_cascade(outcome)              # WP-6 (§E.1)
        self._stub_vulnerability(outcome)                 # WP-6 (peninsular §3.2)
        self._stub_turmoil(outcome)                       # WP-6 (peninsular §4.1)
        self._stub_treasury(outcome)                      # WP-6 (§A.14b)
        self._stub_gap_registration(outcome)              # WP-5 (§A.10 EDGE-05)

    # ── F7.1: Military ceiling ±2 (§A.14) — IMPLEMENTED ──────────────────────

    def _apply_military_delta(self, o: BattleOutcome) -> None:
        if o.winner_faction is not None and o.military_delta_winner:
            d_in = o.military_delta_winner
            d = max(-2, min(2, d_in))                     # §A.14 ±2 cap
            f = self.factions[o.winner_faction]
            f.military = max(0, min(10, f.military + d))  # 0..10 rail
            self.log.append(
                f"[F7.1] {o.winner_faction} Military {'+' if d >= 0 else ''}{d} "
                f"(now {f.military}/10)"
            )
        if o.loser_faction is not None and o.military_delta_loser:
            d_in = o.military_delta_loser
            d = max(-2, min(2, d_in))
            f = self.factions[o.loser_faction]
            f.military = max(0, min(10, f.military + d))
            self.log.append(
                f"[F7.1] {o.loser_faction} Military {'+' if d >= 0 else ''}{d} "
                f"(now {f.military}/10)"
            )

    # ── Downstream WP attach points (stubs) ──────────────────────────────────

    def _stub_mandate(self, o: BattleOutcome) -> None:
        if o.mandate_delta_loser:
            self.log.append(
                f"[STUB WP-2 §A.14] mandate_delta_loser={o.mandate_delta_loser} "
                f"for {o.loser_faction} — implement in WP-2 calibration."
            )

    def _stub_conquest_cascade(self, o: BattleOutcome) -> None:
        if o.result is BattleResult.CONQUEST:
            self.log.append(
                f"[STUB WP-6 §E.1] conquest of {o.territory_id}: substrate_fracture, "
                f"conquerors_accord, defenders_accord — implement in WP-6 persistence."
            )

    def _stub_vulnerability(self, o: BattleOutcome) -> None:
        if o.vulnerability_signal_ip:
            self.log.append(
                f"[STUB WP-6 peninsular §3.2] vulnerability_signal_ip="
                f"{o.vulnerability_signal_ip} — implement in WP-6."
            )

    def _stub_turmoil(self, o: BattleOutcome) -> None:
        if o.turmoil_strain_delta:
            self.log.append(
                f"[STUB WP-6 peninsular §4.1] turmoil_strain_delta="
                f"{o.turmoil_strain_delta} — implement in WP-6."
            )

    def _stub_treasury(self, o: BattleOutcome) -> None:
        if o.treasury_delta_winner:
            self.log.append(
                f"[STUB WP-6 §A.14b] treasury_delta_winner={o.treasury_delta_winner} "
                f"for {o.winner_faction} — implement in WP-6 hostile-territory cost."
            )

    def _stub_gap_registration(self, o: BattleOutcome) -> None:
        if o.gap_registrations:
            self.log.append(
                f"[STUB WP-5 §A.10 EDGE-05] {len(o.gap_registrations)} gap(s) "
                f"to register: {list(o.gap_registrations)} — implement in WP-5."
            )


# ── Emitter ───────────────────────────────────────────────────────────────────


def emit_outcome_events(
    *,
    battle_id:           str,
    territory_id:        str,
    attacker_faction:    str,
    defender_faction:    str,
    result:              BattleResult,
    units:               tuple[UnitSnapshot, ...],
    in_hostile_territory: bool = False,
) -> BattleOutcome:
    """Compose a BattleOutcome from raw battle-end state.

    Bottom-up: every emitted delta derives from a primitive (result enum,
    per-unit snapshot, hostile-territory flag). No top-down recognition.
    """
    # Winner / loser from result
    if result in (BattleResult.DECISIVE_WIN, BattleResult.MARGINAL_WIN, BattleResult.CONQUEST):
        winner, loser = attacker_faction, defender_faction
    elif result in (BattleResult.DECISIVE_LOSS, BattleResult.MARGINAL_LOSS):
        winner, loser = defender_faction, attacker_faction
    else:
        winner = loser = None

    # Casualty aggregation
    att = [u for u in units if u.faction_id == attacker_faction]
    dfd = [u for u in units if u.faction_id == defender_faction]
    cas = CasualtyTotals(
        attacker_size_lost  = sum(u.size_start - u.size_end for u in att),
        defender_size_lost  = sum(u.size_start - u.size_end for u in dfd),
        attacker_size_start = sum(u.size_start for u in att),
        defender_size_start = sum(u.size_start for u in dfd),
    )

    # §A.14 Military delta — magnitude per result tier
    # decisive → 2, marginal → 1, draw → 0, conquest → 2
    magnitude = {
        BattleResult.DECISIVE_WIN:  2,
        BattleResult.MARGINAL_WIN:  1,
        BattleResult.DRAW:          0,
        BattleResult.MARGINAL_LOSS: 1,
        BattleResult.DECISIVE_LOSS: 2,
        BattleResult.CONQUEST:      2,
    }[result]
    mil_w = +magnitude if winner is not None else 0
    mil_l = -magnitude if loser  is not None else 0

    # §A.14 Mandate -1 on decisive / conquest loss
    decisive_set = {BattleResult.DECISIVE_WIN, BattleResult.DECISIVE_LOSS, BattleResult.CONQUEST}
    mandate_l = -1 if (result in decisive_set and loser is not None) else 0

    # §E.1 conquest cascade
    is_conq = result is BattleResult.CONQUEST

    # §A.14b hostile-territory Treasury cost to winner
    treas_w = -1 if (winner is not None and in_hostile_territory) else 0

    return BattleOutcome(
        battle_id                = battle_id,
        territory_id             = territory_id,
        attacker_faction         = attacker_faction,
        defender_faction         = defender_faction,
        result                   = result,
        winner_faction           = winner,
        loser_faction            = loser,
        casualties               = cas,
        units                    = units,
        military_delta_winner    = mil_w,
        military_delta_loser     = mil_l,
        mandate_delta_loser      = mandate_l,
        substrate_fracture_loser = is_conq,
        conquerors_accord        = is_conq,
        defenders_accord         = is_conq,
        treasury_delta_winner    = treas_w,
    )


# ── Verification ──────────────────────────────────────────────────────────────


def _verify() -> None:
    """Acceptance proof per plan WP-1 criteria:
       'one downstream finding (e.g. F7.1 faction Military ceiling) functional
       as proof of unlock.'
    """
    factions = {
        "solmund": FactionState("solmund", military=5, mandate=4, treasury=10, morale_substrate=5),
        "altonia": FactionState("altonia", military=6, mandate=5, treasury=12, morale_substrate=6),
    }
    layer = StrategicLayer(factions)

    units = (
        UnitSnapshot("S1", "solmund", 100, 85, 65, "seasoned", False),
        UnitSnapshot("A1", "altonia", 100, 30, 40, "fresh",    False),
        UnitSnapshot("A2", "altonia", 100,  0,  0, "fresh",    True),
    )
    outcome = emit_outcome_events(
        battle_id            = "B-001",
        territory_id         = "T-12",
        attacker_faction     = "solmund",
        defender_faction     = "altonia",
        result               = BattleResult.DECISIVE_WIN,
        units                = units,
        in_hostile_territory = True,
    )

    # Surface assertions
    assert outcome.winner_faction == "solmund"
    assert outcome.loser_faction  == "altonia"
    assert outcome.military_delta_winner == +2,        outcome.military_delta_winner
    assert outcome.military_delta_loser  == -2,        outcome.military_delta_loser
    assert outcome.mandate_delta_loser   == -1,        outcome.mandate_delta_loser
    assert outcome.treasury_delta_winner == -1,        outcome.treasury_delta_winner
    assert abs(outcome.casualties.attacker_ratio - 0.15) < 1e-9, outcome.casualties.attacker_ratio
    assert abs(outcome.casualties.defender_ratio - 0.85) < 1e-9, outcome.casualties.defender_ratio

    # F7.1 handler: Solmund 5→7, Altonia 6→4
    layer.on_battle_resolved(outcome)
    assert factions["solmund"].military == 7, factions["solmund"].military
    assert factions["altonia"].military == 4, factions["altonia"].military

    # §A.14 ±2 cap at the 10-rail
    factions["solmund"].military = 9
    layer.on_battle_resolved(outcome)
    assert factions["solmund"].military == 10, factions["solmund"].military

    # §A.14 ±2 cap at the 0-rail
    factions["altonia"].military = 1
    layer.on_battle_resolved(outcome)
    assert factions["altonia"].military == 0, factions["altonia"].military

    # Draw produces no Military delta
    factions["solmund"].military = 5
    factions["altonia"].military = 6
    draw = emit_outcome_events(
        battle_id="B-002", territory_id="T-12",
        attacker_faction="solmund", defender_faction="altonia",
        result=BattleResult.DRAW, units=units,
    )
    assert draw.winner_faction is None and draw.loser_faction is None
    assert draw.military_delta_winner == 0 and draw.military_delta_loser == 0
    layer.on_battle_resolved(draw)
    assert factions["solmund"].military == 5
    assert factions["altonia"].military == 6

    # Conquest sets cascade flags and triggers the WP-6 stub
    conq = emit_outcome_events(
        battle_id="B-003", territory_id="T-12",
        attacker_faction="solmund", defender_faction="altonia",
        result=BattleResult.CONQUEST, units=units,
    )
    assert conq.substrate_fracture_loser is True
    assert conq.conquerors_accord        is True
    assert conq.defenders_accord         is True
    layer.on_battle_resolved(conq)
    assert any("STUB WP-6 §E.1" in line for line in layer.log), \
        "conquest stub should log a WP-6 attach point"

    print("[F8.4 ✓] BattleOutcome emit surface verified")
    print("[F7.1 ✓] Military ±2 cap at decisive / 10-rail / 0-rail / draw")
    print(f"[F8.4 ✓] {len(layer.log)} event-log entries; stubs noted for WP-2, WP-5, WP-6")
    for line in layer.log:
        print(f"  {line}")


if __name__ == "__main__":
    _verify()
