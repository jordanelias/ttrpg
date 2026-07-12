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
import os
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
    #: "verified" (the owning Adapter.canon_row resolved against a real CURRENT.md
    #: row) or "provisional" (canon_row is None — deliberately testing pre-canonical
    #: work). Distinct from an empty citations list, which alone is ambiguous: a
    #: verified row that happens to cite no docs and a provisional adapter with no
    #: row to cite would otherwise look identical in the trace. Added so a reader
    #: (or future tooling) can never mistake a provisional run's numbers for
    #: canon-verified ones just by scanning citations.
    canon_status: str = "verified"
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
            "canon_status": self.canon_status,
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
        #
        # Triage flags are included here, not just self.events: the first cut of
        # this method only serialized events/notes, so every triage flag (the
        # actual finding a run exists to produce) was visible in the printed CLI
        # summary and rolled up into the registry's verdict_detail category list,
        # but NEVER reached the one durable, per-event artifact this module's own
        # docstring calls "the actual audit artifact." A trace file re-opened
        # later (or read by anything other than this same process's stdout) had
        # no way to recover which event a flag belonged to, its tier, or its full
        # detail text. Found by adversarial review: writing a trace, then reading
        # it back, and observing the STUB_HIT flag printed to the console was
        # simply absent from the file.
        objs = [e.to_obj() for e in self.events]
        objs += [{"kind": "triage_flag", **f.to_obj()} for f in self.triage.flags]
        return "\n".join(
            json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            for o in objs
        )

    def content_hash(self) -> str:
        return hashlib.sha256(self.serialize().encode("utf-8")).hexdigest()

    def write_trace(self, out_dir: Path) -> Path:
        text = self.serialize()
        out_dir.mkdir(parents=True, exist_ok=True)
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        out_path = out_dir / f"{self.adapter_name}_{digest[:12]}.jsonl"
        # Write-to-temp-then-os.replace() rather than Path.write_text() directly:
        # write_text() opens in truncating mode with no atomicity guarantee. Two
        # concurrent harness processes running the identical scenario (same
        # adapter+seed+trial count -> identical content_hash -> identical target
        # filename, e.g. parallel CI/test workers) would otherwise both truncate
        # and rewrite the same path with no locking; a reader in the narrow
        # window between one process's truncate and its completed write could
        # observe a zero-length or partial file even though both writers
        # eventually produce identical, correct content. os.replace() is an
        # atomic rename on POSIX (and on Windows since it maps to
        # MoveFileEx+REPLACE_EXISTING via CPython's implementation), so any
        # concurrent reader sees either the fully-old or fully-new file, never a
        # partial one. Found by adversarial review reasoning through the
        # "deploy whenever we want, possibly multiple sessions" use case this
        # harness is explicitly meant to support — not currently triggered by
        # any single-shot shipped code path, but real latent exposure once it is
        # used from more than one process at a time.
        tmp_path = out_path.with_name(f".{out_path.name}.{os.getpid()}.tmp")
        tmp_path.write_text(text + "\n", encoding="utf-8")
        os.replace(tmp_path, out_path)
        return out_path

    def append_registry_record(self, *, subsystem: str, scope: str, folder: str) -> dict:
        # tools/audit_registry.py's append_record() opens references/audit_registry.jsonl
        # in append mode and writes one small (~150-400 byte) JSON line per call — safe
        # for concurrent appenders on a local POSIX filesystem, where O_APPEND makes the
        # kernel atomically seek-to-EOF immediately before each write() (a real guarantee,
        # distinct from and NOT the commonly-cited "PIPE_BUF" one, which is scoped to
        # pipes/FIFOs, not regular files). This does NOT hold on networked/shared storage
        # (explicitly not guaranteed on NFS) and has no size cap or fsync — acceptable for
        # this package's tiny fixed-shape records on a local checkout, but not fixed here:
        # audit_registry.py is a shared file this package doesn't own, used by other
        # skills, and hardening it is out of scope for a Gate-0 harness fix. Noted, not
        # silently left undiscovered, per adversarial review.
        verdict = self.triage.verdict()
        n_events = sum(1 for e in self.events if getattr(e, "kind", "event") == "event")
        detail_bits = [f"{n_events} event(s) traced"]
        if self.triage.flags:
            cats = sorted({f.category.value for f in self.triage.flags})
            detail_bits.append(f"{len(self.triage.flags)} triage flag(s): {', '.join(cats)}")
        today = date.today().isoformat()
        # tools/audit_registry.py defaults a record's id to f"{skill}-{date}" when not
        # given one explicitly — every harness run sharing a skill+date (i.e. any two
        # runs on the same day, which is the normal case during stress testing) would
        # silently collide on the identical id despite being genuinely different runs
        # (different seed/adapter/verdict). Pass an explicit, content-hash-disambiguated
        # id instead. Found by deliberately running the harness twice live in one day
        # and observing both entries share one id.
        record = {
            "id": f"sim-harness-{self.adapter_name}-{today}-{self.content_hash()[:8]}",
            "audit_type": "simulation_balance",
            "subsystem": subsystem,
            "skill": "sim-harness",
            "date": today,
            "folder": folder,
            "scope": scope,
            "verdict": verdict,
            "verdict_detail": "; ".join(detail_bits),
            "confidence": "measured",
        }
        return audit_registry.append_record(record)
