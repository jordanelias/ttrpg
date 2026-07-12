"""trace_logger.py — per-event probabilistic trace, triage-flag collection, and a
LIVE (not backfilled) references/audit_registry.jsonl append.

Relationship to sim/substrate/keys.py's KeyLog, stated precisely rather than as a
vague "mirrors" claim: TraceLogger reuses the same append/serialize/content_hash
SHAPE, and (as of this revision) the same deterministic-JSON convention KeyLog uses
(sort_keys=True, fixed separators) so a trace's content_hash is reproducible the
same way a KeyLog's is. It does NOT share KeyLog's TypeRegistry, its 8 validation
invariants, or its schema — a TraceEvent is not a Key, traces are not
KeyLog-interoperable, and nothing here validates against key_type_registry_v30.md.
Anyone tempted to feed a trace file into KeyLog-consuming tooling should not.

Fixes the concrete gap the methodology proposal's inventory found: every one of the
8 audit/simulation skills claims to log to audit_registry.jsonl "on completion," but
the file had 5 entries, all backfilled after the fact by a one-time script, none
live-appended by an actual run. This module calls tools/audit_registry.append_record
(...) directly, in-process, so the registry stops depending on anyone remembering to
update it by hand.
"""
from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parents[1]
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))
import audit_registry  # noqa: E402  (tools/audit_registry.py — the one reader/writer)

from .triage import TriageLog


@dataclass
class TraceEvent:
    event_id: str
    tier: int
    n: int
    branch_counts: dict
    citations: list
    justification: str = ""
    param_provenance: dict = field(default_factory=dict)
    contract_note: str | None = None
    kind: str = "event"

    def to_obj(self) -> dict:
        return {
            "kind": self.kind,
            "event_id": self.event_id,
            "tier": self.tier,
            "n": self.n,
            "branch_counts": self.branch_counts,
            "citations": self.citations,
            "justification": self.justification,
            "param_provenance": self.param_provenance,
            "contract_note": self.contract_note,
        }


@dataclass
class TraceNote:
    """A non-event record — e.g. a deliberate opt-out that has nothing to tally but
    still needs to be visible in the trace, distinguishing 'this ran and chose to
    skip' from 'this silently never ran'."""
    event_id: str
    message: str
    kind: str = "note"

    def to_obj(self) -> dict:
        return {"kind": self.kind, "event_id": self.event_id, "message": self.message}


class TraceLogger:
    def __init__(self, adapter_name: str, contract_module: str | None):
        self.adapter_name = adapter_name
        self.contract_module = contract_module
        self.events: list = []  # TraceEvent | TraceNote, in emission order
        self.triage = TriageLog()

    def record(self, event: TraceEvent) -> None:
        self.events.append(event)

    def note(self, event_id: str, message: str) -> None:
        """Record a non-event trace line — see TraceNote. Use this instead of a
        bare pass/no-op whenever a code path deliberately does nothing further, so
        the trace can distinguish 'ran, chose to skip' from 'never ran'."""
        self.events.append(TraceNote(event_id, message))

    def serialize(self) -> str:
        # sort_keys + fixed separators mirror sim/substrate/keys.py's KeyLog.serialize()
        # so identical runs produce byte-identical output, the same determinism
        # guarantee KeyLog documents for its own content_hash.
        return "\n".join(
            json.dumps(e.to_obj(), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            for e in self.events
        )

    def content_hash(self) -> str:
        return hashlib.sha256(self.serialize().encode("utf-8")).hexdigest()

    def write_trace(self, out_dir: Path) -> Path:
        text = self.serialize()
        out_dir.mkdir(parents=True, exist_ok=True)
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        out_path = out_dir / f"{self.adapter_name}_{digest[:12]}.jsonl"
        out_path.write_text(text + "\n", encoding="utf-8")
        return out_path

    def append_registry_record(self, *, subsystem: str, scope: str, folder: str) -> dict:
        verdict = self.triage.verdict()
        n_events = sum(1 for e in self.events if getattr(e, "kind", "event") == "event")
        detail_bits = [f"{n_events} event(s) traced"]
        if self.triage.flags:
            cats = sorted({f.category.value for f in self.triage.flags})
            detail_bits.append(f"{len(self.triage.flags)} triage flag(s): {', '.join(cats)}")
        record = {
            "audit_type": "simulation_balance",
            "subsystem": subsystem,
            "skill": "sim-harness",
            "date": date.today().isoformat(),
            "folder": folder,
            "scope": scope,
            "verdict": verdict,
            "verdict_detail": "; ".join(detail_bits),
            "confidence": "measured",
        }
        return audit_registry.append_record(record)
