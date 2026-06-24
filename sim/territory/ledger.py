"""
sim/territory/ledger.py — Durable per-settlement governance memory (Ledger tags)

Canon source: designs/territory/goldenfurt_slice/sim_build_spec.md §2;
              designs/territory/governance_play_redesign_v1.md §1.6

A LedgerTag records a consequence of governance that the world remembers:
  Precedent  — a ruling/policy that biases future events (±Ob, opens/closes cards)
  Grudge     — an actor/faction wronged; raises their hostile-action weight
  Debt       — an obligation (a sponsorship expectation, a called-in favour)
  Reputation — the settlement's read on the governor (Just/Harsh/Generous/Weak/…)
  Leverage   — a hook the player holds (e.g. konrad-corrupt, tomas-known)

Tags live on the Settlement (registry.Settlement.ledger), NOT on the governor,
so they survive succession — the player->world persistence guarantee. Durable
tags (ttl=None) never expire; transient tags drop on the season-boundary sweep.

Entry points:
  - LedgerTag(kind, key, value=1.0, created_season=0, ttl=None)
  - ledger_add(ledger, tag)        # dedupe by (kind, key); Reputation is single-valued
  - ledger_has(ledger, kind, key=None)
  - ledger_get(ledger, kind)
  - ledger_sweep(ledger, season)   # drop expired ttl tags; returns removed
"""
from __future__ import annotations

from dataclasses import dataclass

# §1.6 tag kinds
TAG_KINDS = {"Precedent", "Grudge", "Debt", "Reputation", "Leverage"}
# Reputation is a single read of the governor — latest wins (replaces prior).
SINGLE_VALUED = {"Reputation"}


@dataclass
class LedgerTag:
    kind: str
    key: str
    value: float = 1.0
    created_season: int = 0
    ttl: int | None = None  # None = durable (survives succession + sweeps)

    def is_expired(self, season: int) -> bool:
        return self.ttl is not None and season >= self.created_season + self.ttl


def ledger_add(ledger: list, tag: LedgerTag) -> None:
    """Add a tag, deduping by (kind, key). A single-valued kind (Reputation)
    replaces any prior tag of that kind."""
    if tag.kind in SINGLE_VALUED:
        ledger[:] = [t for t in ledger if t.kind != tag.kind]
        ledger.append(tag)
        return
    for i, t in enumerate(ledger):
        if t.kind == tag.kind and t.key == tag.key:
            ledger[i] = tag  # refresh in place
            return
    ledger.append(tag)


def ledger_has(ledger: list, kind: str, key: str | None = None) -> bool:
    return any(t.kind == kind and (key is None or t.key == key) for t in ledger)


def ledger_get(ledger: list, kind: str) -> list:
    return [t for t in ledger if t.kind == kind]


def ledger_sweep(ledger: list, season: int) -> list:
    """Remove expired (ttl) tags; durable tags (ttl=None) always survive.
    Returns the list of removed tags."""
    removed = [t for t in ledger if t.is_expired(season)]
    if removed:
        ledger[:] = [t for t in ledger if not t.is_expired(season)]
    return removed
