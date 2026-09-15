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


# ⭐ RULED by Jordan, 2026-09-13: *"Loyalty can be invented. Just do it on a scale of 0-100."* The
# SCALE is his; the SHAPE is read off canon rather than drawn, because a varying quantity makes a
# better game than a constant and canon supplies the material for one.
#
# ⚠ **THERE IS A SECOND LOYALTY IN THE TREE AND IT IS NOT THIS ONE — SAID HERE SO NOBODY HAS TO
# REDISCOVER IT COLD.** `systems/world/sim/npe.py:70` declares `LOYALTY_MIN = 0` / `LOYALTY_MAX = 3`
# for a generated NPC's `affiliation_loyalty`. `tools/link_values_pointers.py` links both to the
# same `ppt.loyalty` pointer, which is how this was found — by the link map, not by reading.
#
# They are not two ladders for one quantity (`CLAUDE.md` §0.06's S test), and the reason is
# structural rather than a judgment call. MEASURED by AST 2026-09-14: `npe` has exactly ONE
# importer in the whole tree, `systems/overview/sim/accounting.py`, and nothing under `engine/`
# names `affiliation_loyalty` at all — so the two never meet at runtime, which
# `test_importing_every_engine_module_pulls_in_no_subsystem` enforces from the other side. `npe`
# is in the superseded tree; Jordan's 0-100 ruling is newer and names this scale explicitly.
#
# **So: do not reconcile them, and do not read `npe`'s 0-3 as a prior bound on this one.** If the
# season engine ever needs an affiliation strength, it comes from here. The note exists because a
# later session meeting `LOYALTY_MAX = 3` with no memory of this repo would otherwise read a
# contradiction where there is a supersession — the exact failure `CLAUDE.md` §4 records under
# `evacuate`, where a cold reading of one word escalated a non-existent blocker across five
# surfaces.
LOYALTY_SCALE = 100   # [JUSTIFIED: Jordan's ruled 0-100 scale, ED-IN-0228 — the unit's definition, not a tunable]
# Orthogonal ethics: neither aligned with the creed nor against it. DERIVED from the scale and
# not written as a second number — the cosine's `[-1,+1]` maps onto `[0, LOYALTY_SCALE]`, so
# indifference is its midpoint by construction and cannot drift out of step with the scale.
LOYALTY_INDIFFERENT = LOYALTY_SCALE // 2


def faction_leader(faction: Optional[str]) -> Optional[str]:
    """The case id of the faction's authored leader, or `None` where canon names none."""
    from .rosters import roster_map
    return (roster_map("faction_leaders", "by_faction") or {}).get(str(faction or ""))


def loyalty(r: dict, faction: Optional[str]) -> Optional[int]:
    """How far this person's own ethics run with their faction's, `0..100`. `None` if unmeasurable.

    **50 IS INDIFFERENT, NOT AVERAGE.** The measure is the cosine between two positions in the
    four-axis ethical space — the person's, and their faction's role template's — mapped from
    `[-1, +1]` onto `[0, 100]`. So `100` is a person whose values point exactly where the faction
    expects, `50` is orthogonal (the creed is simply not about anything they care about), and `0`
    is someone whose ethics point the opposite way. A member at `0` is not a bad member; they are
    an opposed one, which is a thing a political game should be able to represent.

    ⚠⚠ **IT IS COMPUTED IN AXIS SPACE, AND THE FIRST WRITING COMPUTED IT OVER THE THIRTEEN.** That
    version returned **0 for 14 of 35 placed people — including Inge Baralta, who LEADS Hafenmark,
    and Magnus Vaynard, who leads Varfell.** The cause is sparsity, not disloyalty: a person holds
    1–3 of the thirteen and a template names 5, so two can share no vocabulary at all and score a
    bare zero. Projecting first asks *do these two point the same way ethically* instead of *do
    they happen to use the same words* — which is what `key_substrate_v30.md` §2.4 says the axis
    space is FOR: *"used by armature dot-products to produce per-observer interpretation."* After
    the fix the spread is 2–100 with no zeros, and the low end is legible: Kolbrun Thale, the
    Crown's Spymaster, reads 2.

    ⚠ **A LEADER MAY SCORE LOW AND THAT IS CANON, NOT A BUG.** `faction_canon_v30.md` §4 on the two
    factions sharing `military-order`: *"their differentiation comes from Mission, leader
    Convictions, and stat profile, not role template."* Vaynard reads 3 against the order he leads
    because his authored `Utility` pulls hard on the instrumental axis where `military-order`
    expects `Honor`. A pragmatist at the head of a traditionalist order is a situation.

    ⚠ **`None` FOR A FACTION WITH NO TEMPLATE, NEVER A DEFAULT.** `Guilds` and `Schoenland` have no
    `role_template`, no expected convictions and no authored leader — so there is nothing to be
    loyal TO, and inventing a midpoint would put a number where canon has a silence (§42.2's
    polarity rule)."""
    import math
    from .convictions import to_axes
    from .rosters import ROLE_TEMPLATE_OF, table
    template = ROLE_TEMPLATE_OF.get(str(faction or ""))
    if template is None:
        return None
    mine = to_axes(convictions_of(r))
    theirs = to_axes((table("role_template_convictions") or {}).get(template) or {})
    dot = sum(mine.get(a, 0.0) * theirs.get(a, 0.0) for a in set(mine) | set(theirs))
    na = math.sqrt(sum(v * v for v in mine.values()))
    nb = math.sqrt(sum(v * v for v in theirs.values()))
    if not na or not nb:
        return None                       # a person with no convictions has no ethics to compare
    cosine = max(-1.0, min(1.0, dot / (na * nb)))
    return round(LOYALTY_INDIFFERENT * (cosine + 1))


# #353 `:333` types a stance row `(referent, valence -5..+5, weight 0..5)`, and `decision/choose.py
# ::stance_toward` sums `valence * weight` over the rows naming a candidate's subject. Five is that
# type's own bound, read off the row rather than chosen here.
STANCE_VALENCE_SCALE = 5   # [JUSTIFIED: #353 `:333` types the row `(referent, valence -5..+5, weight 0..5)` — the type's own bound, not a tuning; ED-IN-0228]


def stance_from_loyalty(value: Optional[int]) -> Optional[tuple]:
    """A stance row's `(valence, weight)` from a `0..100` loyalty. `None` where loyalty is `None`.

    **THE TRANSLATION IS A REFLECTION ABOUT INDIFFERENCE, NOT A RESCALE.** Loyalty is a magnitude
    on one side of `LOYALTY_INDIFFERENT`; a stance row is a SIGN and a MAGNITUDE. So the sign comes
    from which side of 50 the person sits and the weight from how far, which is why a member at 50
    gets `(+1, 0)` — a row that sums to zero, indistinguishable in `stance_toward` from having no
    row at all. That is the honest encoding of *"the creed is not about anything they care about"*,
    and it means the indifferent member is not quietly given a small positive push.

    ⚠ **EVERY CONSTANT HERE IS DERIVED AND NONE IS CHOSEN.** The divisor is
    `LOYALTY_INDIFFERENT / STANCE_VALENCE_SCALE`, so the widest possible departure from
    indifference (50 points) maps to the widest weight the row type permits (5) by construction.
    Re-scale loyalty and the mapping follows; there is no second number to keep in step. The `min`
    is a belt against a loyalty outside `0..100` reaching here, not a clamp doing real work."""
    if value is None:
        return None
    offset = int(value) - LOYALTY_INDIFFERENT
    per_step = LOYALTY_INDIFFERENT / STANCE_VALENCE_SCALE
    weight = min(STANCE_VALENCE_SCALE, round(abs(offset) / per_step))
    return (1 if offset >= 0 else -1, weight)
