"""adapter.py — the Adapter protocol every subsystem "test module" implements, plus
the registry that makes adding one a single-file, single-import operation instead of
an edit to harness.py's core dispatch.

The harness core (harness.py) has zero subsystem-specific knowledge; everything
domain-specific — how to resolve this subsystem's canon parameters, what its events
are, how to sample one trial — lives in an adapter. This is the pluggable "test
module per subsystem" shape the methodology proposal calls for, bound to
references/module_contracts.yaml instead of inventing a second interface shape.

See adapters/dice_pool_demo.py for the worked example.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from .depth import DecisionPoint

#: name -> Adapter subclass. Populated by @register_adapter; harness.py reads this,
#: it never hardcodes adapter names itself. See register_adapter()'s docstring for
#: what actually has to happen for a new adapter to become runnable via the CLI.
ADAPTER_REGISTRY: dict[str, type["Adapter"]] = {}


def register_adapter(name: str):
    """Class decorator: `@register_adapter("my_adapter")` on an Adapter subclass
    makes it resolvable by that name via ADAPTER_REGISTRY / harness.py's CLI.
    Registration only happens once the module defining the class is imported —
    adapters/__init__.py imports every shipped adapter module for exactly this
    reason. Adding a new adapter therefore requires editing exactly one file
    outside the adapter's own (adapters/__init__.py, one import line) — never
    harness.py itself."""
    def _decorate(cls: type["Adapter"]) -> type["Adapter"]:
        if name in ADAPTER_REGISTRY and ADAPTER_REGISTRY[name] is not cls:
            raise ValueError(
                f"adapter name {name!r} already registered to "
                f"{ADAPTER_REGISTRY[name].__name__}, cannot also register {cls.__name__}"
            )
        ADAPTER_REGISTRY[name] = cls
        return cls
    return _decorate


@dataclass
class Outcome:
    event_id: str
    value: Any
    #: detail["branch"] (str, must be one of the owning DecisionPoint.branches) and
    #: detail["stub_hit"] (bool) are the two keys the harness reads; an adapter may
    #: add more for its own trace record. The harness ALSO auto-detects a stub hit
    #: if run_once() itself raises NotImplementedError — either path (setting
    #: detail["stub_hit"]=True on a returned Outcome, or letting the exception
    #: propagate) is equally valid and handled identically: the harness records
    #: one STUB_HIT flag and aborts the remaining trials for that decision point.
    #: Earlier revisions of this docstring claimed the detail-flag path preserves
    #: the ability to keep sampling further trials — that was never actually true
    #: of the shipped harness.py, which breaks immediately on either path (found
    #: by adversarial review as a docstring/behavior mismatch); corrected here.
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
    def resolve_params(self, resolver) -> tuple[dict, dict]:
        """Return (params, provenance) — both dicts, same keys as params.
        provenance[k] must state either a verified citation (typically the string
        returned by resolver.verify_citation(...)) or, for a value that is
        legitimately not a fixed canon constant (e.g. a dice pool size, which
        varies by character build rather than being a single documented number),
        an explicit note saying so — e.g. "test-scenario value, not canon-derived:
        <reason>". Every key in params must have a provenance entry; a harness-side
        check enforces this (see Harness.run()) so a value can never reach a trial
        silently unlabeled as fabricated-or-not. Must not fabricate: let
        CanonGapError propagate from the resolver rather than substituting a
        default when a citation can't be verified."""

    @abstractmethod
    def decision_points(self) -> list[DecisionPoint]:
        """Declare this adapter's events and their default tiers."""

    @abstractmethod
    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        """Sample one trial for the given decision point and classify it into one of
        decision_point.branches via Outcome.detail['branch']. May raise
        NotImplementedError to signal a genuine stub/unimplemented branch — the
        harness catches this automatically and records a STUB_HIT triage flag
        rather than crashing the run (see Harness.run())."""

    #: the audit_registry.jsonl `subsystem` value this adapter's runs are filed
    #: under — must be one of tools/audit_registry.py's SUBSYSTEMS vocabulary.
    registry_subsystem: str = "cross_cutting"
