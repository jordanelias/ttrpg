"""mass_battle.equipment._base — shared substrate for the standalone equipment registries.

A tiny, dependency-free building block the weapons and armour modules share: an OPEN record (any field
set is allowed, so the schema can evolve as the primitive grounding is worked out) plus a mutable
Registry (define / override / extend / remove entries at runtime). No engine import and no resolution
logic — equipment is a DATA surface the rest of the engine will read from once it is wired.

Design intent (Jordan 2026-06-30): weapons and armour are their OWN modules so they can be adjusted to
map onto the scene-combat (personal) model cleanly if that model changes. Keeping the record OPEN and the
registry MUTABLE is what makes the catalogue "dynamic and adaptable": a later grounding pass, a campaign,
or a cross-scale remap can reshape entries without a schema migration here."""
import copy


class EquipmentRecord:
    """One catalogue entry: a name + an OPEN bag of attributes (stored as real attributes).

    DYNAMIC: any attribute may be set now or added later — there is no fixed field list to migrate when
    the model grows (e.g. adding mass_kg / reach_m / coverage once the physics is settled).
    ADAPTABLE: `.variant(name, **overrides)` derives a modified copy without mutating the base (a heavier
    regional or higher-quality variant of a weapon/armour), and `.get(field, default)` tolerates fields
    that do not exist yet, so introducing a new axis never breaks an existing reader."""

    def __init__(self, name, **fields):
        self.name = name
        self.__dict__.update(fields)

    def get(self, key, default=None):
        return self.__dict__.get(key, default)

    def fields(self):
        """The attribute bag, excluding the name (so `variant`/serialisation round-trip cleanly)."""
        f = dict(self.__dict__)
        f.pop("name", None)
        return f

    def variant(self, name=None, **overrides):
        f = copy.deepcopy(self.fields())
        f.update(overrides)
        return EquipmentRecord(name if name is not None else self.name, **f)

    def __repr__(self):
        inner = ", ".join(f"{k}={v!r}" for k, v in self.fields().items())
        return f"EquipmentRecord({self.name!r}, {inner})"


class Registry:
    """A mutable, ordered, case-insensitive name -> EquipmentRecord catalogue.

    DYNAMIC: register / override / extend / remove at import OR at runtime, so a later grounding pass, a
    mod, or a campaign can reshape the catalogue without editing the seed file. Lookups are tolerant
    (`get` returns a default for an unknown name instead of raising), so the catalogue can grow
    incrementally while callers degrade gracefully."""

    def __init__(self, kind):
        self.kind = kind
        self._by_name = {}

    @staticmethod
    def _key(name):
        return str(name).strip().lower()

    def register(self, name, **fields):
        """Create + insert an entry (replacing any same-named one). Returns the record."""
        rec = EquipmentRecord(name, **fields)
        self._by_name[self._key(name)] = rec
        return rec

    def add(self, record):
        """Insert an already-built record (e.g. a `.variant(...)`)."""
        self._by_name[self._key(record.name)] = record
        return record

    def override(self, name, **fields):
        """Patch fields on an existing entry, or create it if absent. Returns the record."""
        rec = self.get(name)
        if rec is None:
            return self.register(name, **fields)
        rec.__dict__.update(fields)
        return rec

    def remove(self, name):
        self._by_name.pop(self._key(name), None)

    def get(self, name, default=None):
        if name is None:
            return default
        return self._by_name.get(self._key(name), default)

    def __getitem__(self, name):
        rec = self.get(name)
        if rec is None:
            raise KeyError(name)
        return rec

    def __contains__(self, name):
        return self._key(name) in self._by_name

    def __iter__(self):
        return iter(self._by_name.values())

    def __len__(self):
        return len(self._by_name)

    def names(self):
        return [r.name for r in self._by_name.values()]

    def where(self, **match):
        """Filter helper: records whose fields equal every key=value in `match` (missing field -> no
        match). Lets behaviour/movement code select e.g. every ranged weapon without a hard-coded list."""
        out = []
        for rec in self._by_name.values():
            if all(rec.get(k) == v for k, v in match.items()):
                out.append(rec)
        return out
