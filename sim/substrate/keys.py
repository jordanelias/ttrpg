"""Executable Key substrate v1 — Key, KeyLog, TypeRegistry, TickScheduler.

Status: [RATIFIED — Key & Echo armature v1, ED-IN-0018, 2026-07-07; §5 fork docket ruled by
Jordan's consolidated "ratify all" pass, ED-IN-0026, same date]

Canon sources (implemented 1:1 where ratified, flag-gated where PROPOSED):
  - designs/architecture/key_substrate_v30.md
      §2.1 universal Key schema · §2.2 field semantics · §2.3 validation
      invariants 1-8 · §2.5 canonical 4-axis set · §4.1 single update rule
      (steps 1-2, 5-6 subset; steps 3-4 observer/armature NOT implemented,
      blocked on ORD-3 — see module docstring of sim.substrate).
  - designs/architecture/key_type_registry_v30.md
      §1 type format (required/optional payload fields, defaults) · §2-§8 the
      44-type roster, parsed at load time — the registry markdown remains the
      single source of truth; nothing is duplicated here.
  - designs/architecture/propagation_spec_v1.md
      §1 O.4/SSI-1..4 (sub_step_index = append-order tiebreak ONLY; the
      re-entrancy meter `cascade_depth` lives on the tick-scoped scheduler and
      is NEVER a field on the logged Key) · §4.2 Level-B termination guard
      (cascade-depth cap + emissions-per-tick cap; Theorem B) · B1
      no-synchronous-re-entry (RATIFIED 2026-07-07, OF-B1 — flag-gated,
      default ON, still caller-toggleable) · §2 AU-3.2 deferred-apply at
      ACCOUNTING_BOUNDARY (RATIFIED 2026-07-07, OF-7 — flag-gated, default
      ON, still caller-toggleable) · ORD-1/ORD-2 (insertion-ordered
      containers throughout; no set() on any ordering path).

Open-fork discipline (armature §5 docket; ED-1050 rule — the sim never
silently corrects canon): OF-CAP is unresolved, so the two termination caps
are REQUIRED constructor arguments with no default value — the caller chooses,
and no fabricated constant enters the repo. OF-7 / OF-B1 were PROPOSED amendments
to key_substrate_v30.md §4.1 steps 4/5; both are now RATIFIED (Jordan's
consolidated ruling pass, 2026-07-07, ED-IN-0026 — see propagation_spec_v1.md's
amended "Relationship to other canonical surfaces" section) and default ON here,
while remaining ordinary caller-toggleable flags rather than hardcoded behavior.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

# §2.5 canonical Conviction axis set (key_substrate_v30.md).
AXES = ("hierarchical", "sacred", "instrumental", "traditional")

# §2.2 target roles (key_substrate_v30.md).
ROLES = ("subject", "object", "witness", "beneficiary", "bystander")

# §2.1 scale_signature members (key_substrate_v30.md).
SCALES = ("personal", "settlement", "territory", "peninsula")

PERMANENCE_VALUES = ("transient", "persistent", "indelible")
TIME_HORIZON_VALUES = ("immediate", "near", "far")

_PHASE_ACTION = "ACTION"
_PHASE_ACCOUNTING = "ACCOUNTING_BOUNDARY"


class KeyValidationError(ValueError):
    """A Key failed a §2.3 universal invariant or its type's payload contract."""


class TerminationBreach(RuntimeError):
    """A Level-B termination invariant was violated (propagation_spec §4.2).

    Raising is the correct behavior: the guard exists to catch genuine
    re-entrant runaway, and a silent clamp would hide the defect the
    propagation spec's Theorem B is meant to make loud.
    """


@dataclass
class Target:
    """One targets[] entry (§2.1). Wide fan-out is one Key, N targets — the

    targets[] width NEVER increments cascade_depth (propagation_spec §2
    AU-3 / §3 D.1: "one Key, not N Keys")."""

    actor_id: str
    role: str
    impact_vector: dict = field(default_factory=dict)   # axis -> signed magnitude
    stat_deltas: dict = field(default_factory=dict)     # stat_name -> delta

    def to_obj(self) -> dict:
        return {
            "actor_id": self.actor_id,
            "role": self.role,
            "impact_vector": dict(self.impact_vector),
            "stat_deltas": dict(self.stat_deltas),
        }


@dataclass
class Visibility:
    """§2.1 visibility block. Exactly one of the three §2.3-#8 shapes."""

    public: bool = True
    semi_public_observers: list = field(default_factory=list)
    private_observers: list = field(default_factory=list)

    def to_obj(self) -> dict:
        return {
            "public": self.public,
            "semi_public_observers": list(self.semi_public_observers),
            "private_observers": list(self.private_observers),
        }


@dataclass
class EmittedAt:
    """§2.1 ordered position. sub_step_index is assigned by KeyLog.append

    (append order, SSI-1); callers pass season_index only."""

    season_index: int
    sub_step_index: int = -1  # -1 = not yet appended

    def to_obj(self) -> dict:
        return {"season_index": self.season_index, "sub_step_index": self.sub_step_index}


@dataclass
class Key:
    """The §2.1 universal Key. NOTE (SSI-4): cascade_depth is deliberately

    NOT a field here — it is scheduler-internal state, never logged."""

    id: str
    type: str
    emitted_at: EmittedAt
    source_actor: str | None = None
    causes: list = field(default_factory=list)
    targets: list = field(default_factory=list)          # list[Target]
    scale_signature: list = field(default_factory=list)  # list[str]
    symbolic_dimensions: dict = field(default_factory=dict)
    visibility: Visibility = field(default_factory=Visibility)
    time_horizon: str = "immediate"
    permanence: str = "transient"
    payload: dict = field(default_factory=dict)

    def to_obj(self) -> dict:
        """Canonical serialization object (deterministic; feeds the R-F2-style

        key-log hash). Field order is irrelevant — serialization sorts keys —
        but list order is semantic and preserved."""
        return {
            "id": self.id,
            "type": self.type,
            "source_actor": self.source_actor,
            "emitted_at": self.emitted_at.to_obj(),
            "causes": list(self.causes),
            "targets": [t.to_obj() for t in self.targets],
            "scale_signature": list(self.scale_signature),
            "symbolic_dimensions": dict(self.symbolic_dimensions),
            "visibility": self.visibility.to_obj(),
            "time_horizon": self.time_horizon,
            "permanence": self.permanence,
            "payload": self.payload,
        }


_TYPE_HEADING = re.compile(r"^### (?P<tid>[a-z_]+\.[a-z_]+)\s*$", re.MULTILINE)
_YAML_BLOCK = re.compile(r"```yaml\s*\n(?P<body>.*?)\n```", re.DOTALL)


class TypeRegistry:
    """Loader/validator over designs/architecture/key_type_registry_v30.md.

    The registry markdown is the single source of truth (CLAUDE.md §8 "every
    rule lives once"); this class parses it at load time rather than
    duplicating the 44-type roster in code. Parsing accepts the §1 template
    fields plus the Class-B extras (default_visibility, class, declared_by,
    articulation_significance) without requiring them.
    """

    def __init__(self, types: dict):
        # dict preserves registry order (ORD-1 discipline).
        self.types = types

    @classmethod
    def load(cls, registry_path: str | Path) -> "TypeRegistry":
        text = Path(registry_path).read_text(encoding="utf-8")
        types: dict = {}
        headings = list(_TYPE_HEADING.finditer(text))
        for i, m in enumerate(headings):
            start = m.end()
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            block = _YAML_BLOCK.search(text, start, end)
            if not block:
                continue  # heading without a yaml block is registry prose, not a type
            types[m.group("tid")] = cls._parse_entry(block.group("body"))
        if not types:
            raise KeyValidationError(f"no key types parsed from {registry_path}")
        return cls(types)

    @staticmethod
    def _parse_entry(body: str) -> dict:
        """Line-based tolerant parse of a registry entry block.

        The registry's ```yaml blocks are prose-flavored: several entries carry
        unquoted colons/parentheticals inside scalar values (e.g. scene.gossip's
        default_visibility line), so strict yaml.safe_load fails on real,
        canonical entries. Parsed here: top-level `field:` scalars (kept as raw
        strings), block lists (`- item`, inline `# comments` preserved — the
        payload-field convention), and flow lists (`field: [a, b]`). Nested
        structures the substrate does not consume are kept as raw lines.
        """
        entry: dict = {}
        current_list = None
        for raw in body.splitlines():
            if not raw.strip():
                continue
            stripped = raw.strip()
            if stripped.startswith("- ") and current_list is not None:
                current_list.append(stripped[2:].strip())
                continue
            m = re.match(r"^(\w+):\s*(.*)$", raw)  # top-level fields only (no indent)
            if m:
                field, value = m.group(1), m.group(2).strip()
                if not value:
                    entry[field] = []
                    current_list = entry[field]
                elif value.startswith("[") and value.endswith("]"):
                    entry[field] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
                    current_list = None
                else:
                    entry[field] = value
                    current_list = None
            # indented continuation lines of nested structures: ignored (not consumed)
        return entry

    def require(self, type_id: str) -> dict:
        if type_id not in self.types:
            raise KeyValidationError(f"key type {type_id!r} not registered (§2.3 invariant 2)")
        return self.types[type_id]

    def validate_payload(self, key: Key) -> None:
        entry = self.require(key.type)
        required = entry.get("required_payload_fields") or []
        # Registry lists fields as "name  # comment" strings after yaml parse.
        missing = []
        for raw in required:
            field_name = str(raw).split("#", 1)[0].strip()
            if field_name and field_name not in key.payload:
                missing.append(field_name)
        if missing:
            raise KeyValidationError(
                f"key {key.id!r} type {key.type!r} missing required payload fields: {missing}"
            )

    def apply_defaults(self, key: Key) -> None:
        """Fill §1-template defaults for fields the emitter left empty."""
        entry = self.require(key.type)
        if not key.scale_signature and entry.get("default_scale_signature"):
            key.scale_signature = list(entry["default_scale_signature"])
        if entry.get("default_permanence") and key.permanence == "transient":
            # only override the dataclass default, never an explicit choice:
            # emitters wanting explicit transient on a persistent-default type
            # set permanence after apply_defaults (documented limitation v1).
            key.permanence = entry["default_permanence"]
        if entry.get("default_time_horizon") and key.time_horizon == "immediate":
            key.time_horizon = entry["default_time_horizon"]


class KeyLog:
    """Append-only canonical key log (§4.1 step 2; AU-4's read surface).

    Assigns sub_step_index at append (SSI-1 append order; propagation_spec §1
    O.4). Serialization is deterministic: canonical JSON per Key in log order,
    newline-joined — two identical runs produce byte-identical logs (the
    R-F2-style determinism surface).
    """

    def __init__(self, registry: TypeRegistry):
        self.registry = registry
        self._entries: list = []          # list[Key], append order
        self._ids: dict = {}              # id -> index (dict, not set: ORD-2)
        self._season_counters: dict = {}  # season_index -> next sub_step_index

    def __len__(self) -> int:
        return len(self._entries)

    def __iter__(self):
        return iter(self._entries)

    def lookup(self, key_id: str) -> Key:
        return self._entries[self._ids[key_id]]

    def append(self, key: Key) -> Key:
        self._validate(key)
        season = key.emitted_at.season_index
        key.emitted_at.sub_step_index = self._season_counters.get(season, 0)
        self._season_counters[season] = key.emitted_at.sub_step_index + 1
        self._ids[key.id] = len(self._entries)
        self._entries.append(key)
        return key

    def _validate(self, key: Key) -> None:
        # §2.3 invariant 1 — id unique across the log.
        if key.id in self._ids:
            raise KeyValidationError(f"duplicate key id {key.id!r} (§2.3 invariant 1)")
        # invariant 2 + per-type payload contract (§2.3 preamble).
        self.registry.validate_payload(key)
        # invariant 3 — causes[] only references Keys already in the log.
        for cause_id in key.causes:
            if cause_id not in self._ids:
                raise KeyValidationError(
                    f"key {key.id!r} cites unknown cause {cause_id!r} (§2.3 invariant 3)"
                )
        # invariant 4 (cycle-freedom) holds by construction for an append-only
        # log whose causes[] may only cite already-logged Keys: no logged Key
        # can ever gain an edge back to a later one (§4.6 BFS check subsumed).
        # invariant 5 — ordering. season monotonicity is the scheduler's job;
        # the log enforces non-decreasing season_index.
        if self._entries and key.emitted_at.season_index < self._entries[-1].emitted_at.season_index:
            raise KeyValidationError(
                f"key {key.id!r} season_index regresses (§2.3 invariant 5)"
            )
        # invariant 6 — axis names match the canonical 4-axis set.
        for axes_dict in [key.symbolic_dimensions] + [t.impact_vector for t in key.targets]:
            for axis in axes_dict:
                if axis not in AXES:
                    raise KeyValidationError(
                        f"key {key.id!r} uses non-canonical axis {axis!r} (§2.3 invariant 6)"
                    )
        for t in key.targets:
            if t.role not in ROLES:
                raise KeyValidationError(
                    f"key {key.id!r} target {t.actor_id!r} has invalid role {t.role!r} (§2.2)"
                )
        # invariant 7 — scale_signature non-empty and canonical.
        if not key.scale_signature:
            raise KeyValidationError(f"key {key.id!r} has empty scale_signature (§2.3 invariant 7)")
        for scale in key.scale_signature:
            if scale not in SCALES:
                raise KeyValidationError(
                    f"key {key.id!r} has non-canonical scale {scale!r} (§2.1)"
                )
        # invariant 8 — exactly one visibility shape.
        v = key.visibility
        if v.public:
            if v.semi_public_observers or v.private_observers:
                raise KeyValidationError(
                    f"key {key.id!r}: public=true forbids observer lists (§2.3 invariant 8)"
                )
        elif not (bool(v.semi_public_observers) ^ bool(v.private_observers)):
            raise KeyValidationError(
                f"key {key.id!r}: public=false requires exactly one non-empty observer list "
                "(§2.3 invariant 8)"
            )
        if key.time_horizon not in TIME_HORIZON_VALUES:
            raise KeyValidationError(f"key {key.id!r} invalid time_horizon {key.time_horizon!r}")
        if key.permanence not in PERMANENCE_VALUES:
            raise KeyValidationError(f"key {key.id!r} invalid permanence {key.permanence!r}")

    def serialize(self) -> str:
        return "\n".join(
            json.dumps(k.to_obj(), sort_keys=True, ensure_ascii=False, separators=(",", ":"))
            for k in self._entries
        )

    def content_hash(self) -> str:
        return hashlib.sha256(self.serialize().encode("utf-8")).hexdigest()


class TickScheduler:
    """The engine_clock-shaped emission seam (propagation_spec §1 O.2, §4.2).

    Owns the tick-scoped queue, the cascade_depth meter (scheduler-internal,
    NEVER written onto Keys — SSI-4), the Level-B termination guard, the B1
    no-synchronous-re-entry rule (OF-B1, flag default ON), and OF-7
    deferred-apply at ACCOUNTING_BOUNDARY (flag default ON).

    Caps are REQUIRED: OF-CAP is an open fork, so no default constant is
    supplied here — tests and callers pass explicit values, [PROVISIONAL]
    until Jordan rules OF-CAP (armature §5 docket).
    """

    def __init__(
        self,
        log: KeyLog,
        *,
        cascade_depth_max: int,
        emissions_per_tick_max: int,
        no_sync_reentry: bool = True,   # OF-B1 RATIFIED 2026-07-07 (Jordan "ratify all" consolidated
                                        # ruling pass, ED-IN-0026; armature §5.4). Amends key_substrate
                                        # §4.1 step 5 ("O(1) or async") to forbid synchronous re-entry.
                                        # Still caller-toggleable (opt OUT with no_sync_reentry=False)
                                        # for callers that need the unamended semantics.
        defer_apply: bool = True,       # OF-7 RATIFIED 2026-07-07 (same ruling pass; armature §5.3).
                                        # Amends key_substrate §4.1 step 4 to allow a deferred-apply
                                        # target. Still caller-toggleable (opt OUT with defer_apply=False).
    ):
        self.log = log
        self.cascade_depth_max = cascade_depth_max
        self.emissions_per_tick_max = emissions_per_tick_max
        self.no_sync_reentry = no_sync_reentry
        self.defer_apply = defer_apply
        # type -> list[callable(key, scheduler)]; dict + list = ORD-1 ordering.
        self.subscriptions: dict = {}
        self._phase = _PHASE_ACTION
        self._queue: list = []            # list[(depth, Key)] FIFO within depth arrival order
        self._pending_apply: list = []    # list[(key_id, callable)] — OF-7 deferred effects
        self._emitted_this_tick = 0
        self._in_drain = False
        self._current_depth = 0

    # -- subscription ------------------------------------------------------
    def subscribe(self, type_id: str, callback) -> None:
        self.subscriptions.setdefault(type_id, []).append(callback)

    # -- emission paths ----------------------------------------------------
    def emit(self, key: Key, apply=None) -> Key:
        """Root emission (cascade_depth 0). §4.1 steps 1-2 + 5 (subset).

        `apply` is an optional settlement-locus effect callable; under OF-7 it
        is deferred to accounting_boundary() while the Key itself is logged
        LIVE (AU-3.2: the echo Key is visible at scene end, its settlement
        effect lands at the boundary).
        """
        if self._in_drain and self.no_sync_reentry:
            raise TerminationBreach(
                "synchronous re-entry: consumers must route new Keys through "
                "schedule_emission() (B1 / OF-B1, propagation_spec §4.2)"
            )
        return self._emit_at_depth(key, 0, apply)

    def schedule_emission(self, key: Key, apply=None) -> None:
        """B1 path: a consumer reacting to an observed Key enqueues its new Key

        at cascade_depth = parent + 1 (propagation_spec §4.2). Drained by
        drain_tick(); never applied synchronously."""
        depth = (self._current_depth + 1) if self._in_drain else 0
        if depth > self.cascade_depth_max:
            raise TerminationBreach(
                f"cascade_depth {depth} exceeds cap {self.cascade_depth_max} "
                "(Theorem B, propagation_spec §4.2) [caps PROVISIONAL — OF-CAP]"
            )
        self._queue.append((depth, key, apply))

    def drain_tick(self) -> int:
        """Drain the tick-scoped queue to empty (Theorem-B guarded). Returns

        the number of Keys emitted during the drain."""
        drained = 0
        self._in_drain = True
        try:
            while self._queue:
                depth, key, apply = self._queue.pop(0)  # FIFO — ORD-1 arrival order
                self._current_depth = depth
                self._emit_at_depth(key, depth, apply)
                drained += 1
        finally:
            self._in_drain = False
            self._current_depth = 0
        return drained

    def _emit_at_depth(self, key: Key, depth: int, apply) -> Key:
        if depth > self.cascade_depth_max:
            raise TerminationBreach(
                f"cascade_depth {depth} exceeds cap {self.cascade_depth_max} "
                "(Theorem B) [caps PROVISIONAL — OF-CAP]"
            )
        if self._emitted_this_tick + 1 > self.emissions_per_tick_max:
            raise TerminationBreach(
                f"emissions this tick exceed cap {self.emissions_per_tick_max} "
                "(Theorem B) [caps PROVISIONAL — OF-CAP]"
            )
        self.log.registry.apply_defaults(key)
        self.log.append(key)                      # §4.1 steps 1-2 (validate + log)
        self._emitted_this_tick += 1
        if apply is not None:
            if self.defer_apply and self._phase == _PHASE_ACTION:
                self._pending_apply.append((key.id, apply))   # OF-7 deferred-apply
            else:
                apply(key)
        # §4.1 step 5 (subset): synchronous notify; consumers wanting to emit
        # must schedule_emission() (B1) — direct emit() raises under the flag.
        for callback in self.subscriptions.get(key.type, []):
            callback(key, self)
        return key

    # -- clock -------------------------------------------------------------
    def accounting_boundary(self) -> int:
        """Enter ACCOUNTING_BOUNDARY: run OF-7 deferred applies in emission

        order, then reset. Returns the number of applies executed."""
        self._phase = _PHASE_ACCOUNTING
        ran = 0
        for key_id, apply in self._pending_apply:
            apply(self.log.lookup(key_id))
            ran += 1
        self._pending_apply = []
        return ran

    def next_tick(self) -> None:
        """Advance to the next season tick: reset the per-tick emission count

        and return to ACTION phase. Season indexing is the caller's (future
        engine_clock's) responsibility."""
        if self._queue:
            raise TerminationBreach("tick advanced with undrained emissions in queue")
        self._emitted_this_tick = 0
        self._phase = _PHASE_ACTION
