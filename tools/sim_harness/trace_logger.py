"""trace_logger.py — per-event probabilistic trace, triage-flag collection, and a
LIVE (not backfilled) references/audit_registry.jsonl append.

Deliberately mirrors sim/substrate/keys.py's KeyLog shape (append events, serialize,
content_hash) rather than forking a new logging convention — but this logs the
harness's own trial/exploration events, not canonical Key emissions. An adapter whose
resolver itself emits Keys should still use KeyLog for those; the two are
complementary, not competing.

Fixes the concrete gap the methodology proposal's inventory found: every one of the 8
audit/simulation skills claims to log to audit_registry.jsonl "on completion," but the
file has 5 entries, all backfilled after the fact by a one-time script, none live-
appended by an actual run. This module calls tools/audit_registry.append_record(...)
directly, in-process, so the registry stops depending on anyone remembering to update
it by hand.
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
    contract_note: str | None = None

    def to_obj(self) -> dict:
        return {
            "event_id": self.event_id,
            "tier": self.tier,
            "n": self.n,
            "branch_counts": self.branch_counts,
            "citations": self.citations,
            "contract_note": self.contract_note,
        }


class TraceLogger:
    def __init__(self, adapter_name: str, contract_module: str | None):
        self.adapter_name = adapter_name
        self.contract_module = contract_module
        self.events: list[TraceEvent] = []
        self.triage = TriageLog()

    def record(self, event: TraceEvent) -> None:
        self.events.append(event)

    def serialize(self) -> str:
        return "\n".join(json.dumps(e.to_obj(), ensure_ascii=False) for e in self.events)

    def content_hash(self) -> str:
        return hashlib.sha256(self.serialize().encode("utf-8")).hexdigest()

    def write_trace(self, out_dir: Path) -> Path:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{self.adapter_name}_{self.content_hash()[:12]}.jsonl"
        out_path.write_text(self.serialize() + "\n", encoding="utf-8")
        return out_path

    def append_registry_record(self, *, subsystem: str, scope: str, folder: str) -> dict:
        verdict = self.triage.verdict()
        detail_bits = [f"{len(self.events)} event(s) traced"]
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
