"""
sim/autoload/registry.py — mechanics_index.yaml loader and mechanic-by-id dispatch

Canon source: canon/mechanics_index.yaml
Status: [CANONICAL — Phase 1 implementation 2026-05-17]

Dependencies:
  - none — root primitive (reads YAML file)

Entry points:
  - load_index(path) -> MechanicsIndex
  - get_mechanic(name) -> MechanicEntry
  - mechanics_by_scale(scale) -> list[MechanicEntry]
  - mechanics_by_faction(faction) -> list[MechanicEntry]
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # Fallback: minimal parser below


@dataclass
class MechanicEntry:
    name: str
    scale: str = ""
    faction: str = "universal"
    canon_sources: list[str] = field(default_factory=list)
    sim_module: str = ""
    test_status: str = "not_implemented"
    dependencies: dict = field(default_factory=dict)
    gd_constraints: list[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class MechanicsIndex:
    mechanics: dict[str, MechanicEntry] = field(default_factory=dict)
    schema_version: int = 1
    meta: dict = field(default_factory=dict)

    def by_scale(self, scale: str) -> list[MechanicEntry]:
        return [m for m in self.mechanics.values() if m.scale == scale]

    def by_faction(self, faction: str) -> list[MechanicEntry]:
        return [m for m in self.mechanics.values()
                if m.faction == faction or m.faction == "universal"]

    def by_sim_module(self, module_path: str) -> list[MechanicEntry]:
        return [m for m in self.mechanics.values() if m.sim_module == module_path]


_loaded_index: MechanicsIndex | None = None


def load_index(path: str = "canon/mechanics_index.yaml") -> MechanicsIndex:
    """Load and parse the mechanics index. Caches after first load."""
    global _loaded_index
    if _loaded_index is not None:
        return _loaded_index

    text = Path(path).read_text(encoding="utf-8")
    if yaml is not None:
        raw = yaml.safe_load(text)
    else:
        raise ImportError("PyYAML required to load mechanics_index.yaml")

    idx = MechanicsIndex(
        schema_version=raw.get("schema_version", 1),
        meta=raw.get("meta", {}),
    )

    mechanics_data = raw.get("mechanics", {})
    for name, entry_data in mechanics_data.items():
        if not isinstance(entry_data, dict):
            continue
        m = MechanicEntry(
            name=name,
            scale=entry_data.get("scale", ""),
            faction=entry_data.get("faction", "universal"),
            canon_sources=entry_data.get("canon_sources", []),
            sim_module=entry_data.get("sim_module", ""),
            test_status=entry_data.get("test_status", "not_implemented"),
            dependencies=entry_data.get("dependencies", {}),
            gd_constraints=entry_data.get("gd_constraints", []),
            notes=entry_data.get("notes", ""),
        )
        idx.mechanics[name] = m

    _loaded_index = idx
    return idx


def get_mechanic(name: str) -> MechanicEntry | None:
    """Look up a single mechanic by name. Returns None if not loaded or not found."""
    if _loaded_index is None:
        return None
    return _loaded_index.mechanics.get(name)


def mechanics_by_scale(scale: str) -> list[MechanicEntry]:
    if _loaded_index is None:
        return []
    return _loaded_index.by_scale(scale)


def mechanics_by_faction(faction: str) -> list[MechanicEntry]:
    if _loaded_index is None:
        return []
    return _loaded_index.by_faction(faction)


def reset():
    """Clear cached index (for testing)."""
    global _loaded_index
    _loaded_index = None
