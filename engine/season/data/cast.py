"""`season.data.cast` — THE CAST, READ FROM CANON INSTEAD OF DERIVED FROM A HASH.

`references/npc_registry.yaml` declares itself *"Canonical source of truth for ALL named
characters"* and carries 46 rows. MEASURED 2026-09-13: its ids are an EXACT 1:1 MATCH with
`run_cases.load_cases("NPC")` — 46 for 46, zero symmetric difference — and every row carries an
authored `faction` and `role`, 31 a `territory`, 30 `goals`, 29 `stats`, 32 `ts`, and 7 a `title`.
All 81 weighted conviction entries across the 46 name one of the canonical thirteen; not one is
invalid.

⚠ NOTHING THAT EXECUTES HAD EVER OPENED IT. The only two Python files naming it are a test that
checks it PARSES (`tests/valoria/test_references_yaml_parse.py`, a regression guard from when it
was unparseable) and a proposal whose own comment says it is out of scope. Meanwhile
`run_cases.seed_convictions` draws each person's convictions from
`blake2b(seed, case_id, pid)` — so a corpus of 46 people with authored, weighted, canon-cited
conviction vectors was being given invented ones, and `R-06`'s *"characters must be robustly built
with goals, ambitions, convictions"* was measured against the invention.

WHAT THIS MODULE IS AND IS NOT. It READS and VALIDATES; it does not translate and it does not
guess. A faction string that resolves to no canonical faction comes back `None` and is counted,
never coerced to a plausible neighbour — §42.2's polarity rule, and the same line
`data/convictions.py` holds one layer down: *"A name that is not canonical is a typo or a rename,
and both should stop the run rather than seed a person with a conviction `CONVICTION_PROJECTION`
has no row for."*

⚠ LAZY, AND `data/__init__.py` RECORDS WHY AT LENGTH. Nothing here runs at import. That module's
own docstring measured what eager loading cost the last time: seven modules that wanted only a
path became able to `SystemExit` at import, and the loaders lost their last external patch point
FAIL-OPEN. To exercise this loader's path resolution, patch `cast.NPC_REGISTRY_YAML` and re-call.
"""

from __future__ import annotations

import re
from typing import Optional

from . import files
from .rosters import FACTIONS, load_yaml
from ..gaps import Unspecified

NPC_REGISTRY_YAML = files.NPC_REGISTRY_YAML

# ---------------------------------------------------------------------------
# ALIASES ARE READ FROM THE REGISTRY THAT OWNS THEM, NOT RETYPED HERE.
#
# ⭐ RULED by Jordan, 2026-09-13: *"the church is Church of Solmund."* Before that ruling
# `references/names_index.yaml` — which feeds the naming gate — carried `world.church` with
# `canonical: "Church"` while `rosters.yaml: factions` carried `"Church of Solmund"`: two
# registries single-owning one faction name and disagreeing, which is a §8 violation and surfaced
# the first time executing code read `references/npc_registry.yaml` (which uses the short form).
# The ruling landed in `names_index.yaml`, where `Church` is now an ALIAS of the canonical name.
#
# ⚠ SO THIS MODULE DERIVES ITS MAP AND DOES NOT AUTHOR ONE. A literal `{"Church": "Church of
# Solmund"}` here would have made this the THIRD owner of the same fact — the exact shape the
# ruling exists to end — and it would go stale silently the next time a faction gains an alias.
# `alias -> canonical` is built from the `token_class: faction` rows, so a new alias is a data
# edit in one file (the standing rule at the head of `rosters.yaml`).
#
# ⚠ `names_index.yaml` HAS NO `Schoenland` ROW, though `rosters.yaml: factions` carries it. That
# is a real gap in the naming index rather than anything this loader can fix, and it costs nothing
# here: a faction with no aliases needs no row to resolve by its own name.
def _alias_map() -> dict:
    """`{alias: canonical}` over every `token_class: faction` row in `names_index.yaml`."""
    global _ALIASES
    if _ALIASES is None:
        try:
            entries = (load_yaml(files.NAMES_INDEX_YAML.read_text(encoding="utf-8"))
                       or {}).get("entries") or {}
        except FileNotFoundError:
            entries = {}
        out: dict = {}
        for row_ in entries.values():
            if not isinstance(row_, dict) or row_.get("token_class") != "faction":
                continue
            canon = row_.get("canonical")
            for alias in (row_.get("aliases") or []):
                if canon:
                    out[str(alias)] = str(canon)
        _ALIASES = out
    return _ALIASES


_ALIASES: Optional[dict] = None

# ⚠ `[^)]*` AND A SEPARATE `tail`, BECAUSE A NON-GREEDY `.*?` SWALLOWS THE CLOSING PAREN.
# `Crown (Inner Circle) / Löwenritter Liaison` (NPC-035, Theodor Kreutz) parsed to a
# sub-organization of `Inner Circle) / Löwenritter Liaison` — the faction still resolved off the
# base, so nothing raised and the mangling showed up only in a census of sub-organizations. The
# `)?` stays optional for the two rows whose closing paren YAML ate as a comment.
_PAREN = re.compile(r"^(?P<base>[^(]+?)\s*\((?P<inner>[^)]*)\)?(?P<tail>.*)$")

_CACHE: Optional[dict] = None


def _rows() -> dict:
    """`{case_id: row}` from the registry, read once and kept.

    Raises `Unspecified` rather than returning `{}` if the file is absent: a world built from a
    silently empty cast is the invented-convictions behaviour this module exists to end, wearing
    a successful load's clothes."""
    global _CACHE
    if _CACHE is None:
        try:
            text = NPC_REGISTRY_YAML.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise Unspecified(
                f"the cast registry at {NPC_REGISTRY_YAML}", "references/npc_registry.yaml",
                needs="the canonical named-character registry",
                law="a cast read from nothing is a cast invented from a hash, which is the "
                    "behaviour this loader replaces") from exc
        data = load_yaml(text) or {}
        _CACHE = {str(r["id"]): r for r in (data.get("characters") or []) if r.get("id")}
    return _CACHE


def row(case_id: str) -> Optional[dict]:
    """The registry row for a case, or `None` where the registry does not carry one."""
    return _rows().get(str(case_id))


def name_of(r: dict) -> str:
    """`first_name last_name`, with a one-name person spelled as their one name.

    ⚠ `last_name: None` IS REAL DATA AND NOT A HOLE — Edeyja (NPC-001) and Orm (NPC-075) have one
    name each, and the corpus cases agree. Formatting it through `str()` would produce the literal
    string "Edeyja None", which is what a first cut of this function did."""
    first = str(r.get("first_name") or "").strip()
    last = str(r.get("last_name") or "").strip() if r.get("last_name") else ""
    return f"{first} {last}".strip() if last else first


def faction_of(r: dict) -> tuple[Optional[str], Optional[str], str]:
    """`(canonical faction | None, sub-organization | None, the raw cell)`.

    THE REGISTRY'S `faction` COLUMN IS 20 DISTINCT STRINGS FOR 8 ROSTER NAMES, because it packs a
    faction and a sub-organization into one cell: `Crown (Inner Circle)`, `Crown (Ministry)`,
    `Varfell (Jarl Council)`, `Independent (Southernmost Wardens)`. Two readings are tried and
    both are principled:

      * the BASE resolves — `Crown (Inner Circle)` is the Crown, seated in its Inner Circle;
      * the PARENTHETICAL resolves — `Independent (Schoenland)` is a Schoenland man who belongs to
        no Valorian faction, so the parenthetical is the affiliation and `Independent` is the
        statement that there is no other.

    Anything resolving on neither side returns `(None, sub, raw)` and is the caller's to count.

    ⚠ TWO ROWS ARE CORRUPTED IN THE SOURCE AND THIS FUNCTION SURVIVES THEM WITHOUT REPAIRING THEM.
    `faction: Hafenmark (Inner Council #4)` (NPC-081) and `Varfell (Jarl Council #5)` (NPC-082) are
    UNQUOTED, so YAML reads `#4)` and `#5)` as comments and the seat numbers are destroyed on load
    — the value arrives as `Hafenmark (Inner Council`, with an unbalanced paren. The regex tolerates
    the missing `)` so the faction still resolves, and the lost seat number is reported by
    `defects()` rather than reconstructed here. Quoting the two cells is a fix to the registry,
    which is canon and not this module's to edit."""
    raw = str(r.get("faction") or "").strip()
    base, inner = raw, None
    m = _PAREN.match(raw)
    if m:
        base = m.group("base").strip()
        inner = (m.group("inner") or "").strip()
        tail = (m.group("tail") or "").strip(" /")
        inner = " / ".join(p for p in (inner, tail) if p) or None
    for candidate in (base, inner):
        if not candidate:
            continue
        resolved = _alias_map().get(candidate, candidate)
        if resolved in FACTIONS:
            return resolved, (inner if candidate == base else None), raw
    return None, inner, raw


def resolve_faction(name: Optional[str]) -> Optional[str]:
    """A bare faction name resolved to its canonical roster spelling, or `None`.

    The one owner of *is this string a faction*. `faction_of` reads a registry ROW and has to
    unpack a packed `faction (sub-organization)` cell; this takes a plain string — the geography
    file's per-province `faction:` column, for one — and does nothing but alias-resolve and check.

    ⚠ `Uncontrolled` RESOLVES TO `None`, WHICH IS THE ANSWER AND NOT A FAILURE. It is the
    geography's own value for a province nobody holds, and the caller writes no `hold` edge for it
    — so the province shows up in `sovereign_fraction`'s `undetermined_count`, which is the
    mechanism reporting an unheld place rather than a lookup quietly failing."""
    if not name:
        return None
    resolved = _alias_map().get(str(name).strip(), str(name).strip())
    return resolved if resolved in FACTIONS else None


def convictions_of(r: dict) -> dict:
    """`{conviction: weight}` from the row, every name checked against the canonical thirteen.

    ⚠ IT VALIDATES THROUGH THE ONE OWNER AND DOES NOT RE-DO THE MEMBERSHIP TEST.
    `data.convictions.conviction` already is that check, delegating in turn to
    `engine.substrate.descriptors.resolve_conviction` — the single reader of the single export of
    the single roster. A second membership test here is the exact shape
    `tests/valoria/test_conviction_roster_single_owner.py` exists to prevent, and that guard is
    mutation-verified: three incompatible rosters once shipped at once and silently disabled the
    Conviction Scar.

    ⚠ THE ROW GROUPS ARE `primary` AND `secondary` AND BOTH ARE TAKEN FLAT. The registry's own
    schema separates them; §F2's score does not, because a weight is a weight. Keeping the groups
    would mean inventing what the distinction is worth, which nothing states."""
    from .convictions import conviction
    out: dict = {}
    block = r.get("convictions") or {}
    if not isinstance(block, dict):
        return out
    for group, rows in block.items():
        if not isinstance(rows, list):
            continue                    # `cultural_label` / `self_other_initial` sit here too
        for entry in rows:
            if isinstance(entry, dict) and entry.get("conviction") is not None:
                out[conviction(str(entry["conviction"]))] = float(entry.get("weight") or 0.0)
    return out


def title_of(r: dict) -> Optional[str]:
    """The row's `title`, present on seven of the 46. Not normalised against `titles.domains` —
    `Doux`, `Confessor`, `Father` and `Prince` are real titles that govern no rung, and forcing
    them onto the eight-rung ladder would invent a placement canon does not make."""
    t = r.get("title")
    return str(t).strip() if t else None


def defects() -> list[str]:
    """What is wrong with the registry AS DATA, reported rather than repaired.

    §0.1 pt 3: a result claim carries the thing that would show it wrong. This is the standing
    list for a caller that wants to know how far to trust a row, and it is computed from the file
    rather than remembered from the session that first read it."""
    out = []
    for cid, r in sorted(_rows().items()):
        raw = str(r.get("faction") or "")
        if raw.count("(") != raw.count(")"):
            out.append(f"{cid}: faction cell {raw!r} has an unbalanced paren — an unquoted "
                       f"`#` in the source was eaten as a YAML comment, destroying a seat number")
        fac, _sub, _raw = faction_of(r)
        if fac is None:
            out.append(f"{cid}: faction {raw!r} resolves to no name on `rosters.yaml: factions`")
    return out
