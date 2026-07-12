"""adapter.py — the Adapter protocol every subsystem "test module" implements.

The harness core (harness.py) has zero subsystem-specific knowledge; everything
domain-specific — how to resolve this subsystem's canon parameters, what its events
are, how to sample one trial — lives in an adapter. This is the pluggable "test
module per subsystem" shape the methodology proposal calls for, bound to
references/module_contracts.yaml instead of inventing a second interface shape.

See adapters/dice_pool_demo.py for the Gate-0 worked example.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from .depth import DecisionPoint


@dataclass
class Outcome:
    event_id: str
    value: Any
    #: detail["branch"] (str, must be one of the owning DecisionPoint.branches) and
    #: detail["stub_hit"] (bool) are the two keys the harness reads; an adapter may
    #: add more for its own trace record.
    detail: dict = field(default_factory=dict)


class Adapter(ABC):
    #: key into references/module_contracts.yaml's `module` field. None is a
    #: deliberate, explicit opt-out for genuinely cross-cutting substrate that has no
    #: row of its own (confirmed by grep for the Gate-0 dice adapter — see its
    #: docstring) — NOT a silent skip; the harness logs the opt-out either way.
    contract_module: str | None = None
    #: substring matched against a CURRENT.md bold row label by CanonResolver
    canon_row: str

    @abstractmethod
    def resolve_params(self, resolver) -> dict:
        """Return {param_name: value}. Must not fabricate: let CanonGapError
        propagate from the resolver rather than substituting a default."""

    @abstractmethod
    def decision_points(self) -> list[DecisionPoint]:
        """Declare this adapter's events and their default tiers."""

    @abstractmethod
    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        """Sample one trial for the given decision point and classify it into one of
        decision_point.branches via Outcome.detail['branch']."""

    #: the audit_registry.jsonl `subsystem` value this adapter's runs are filed
    #: under — must be one of tools/audit_registry.py's SUBSYSTEMS vocabulary.
    registry_subsystem: str = "cross_cutting"
