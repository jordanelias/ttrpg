"""`harness.strife_data` -- THE ONE LOADER for `strife_moves.yaml`.

The file reads the 40 move codes of the strife study against what the season loop can produce.
This module refuses a row naming a verb that is not in `verb_table.yaml`, an Event kind the loop
does not declare, a key the row does not define, a code listed twice, or per-code ending counts that
do not total the study's 102 cases. `load_links` does the same for the study's 16 drawn links (a code with no
row, a side suffix the code cannot carry, a repeated link, a tier outside robust/stable, a count other than
`drawn_links`) and carries the study's leave-and-rejoin figures. It resolves nothing and no step of the loop reads
it; `harness/strife.py` is its reader.

WHY IT LIVES UNDER `harness/` AND NOT `data/`. The port gate (plan position GO-09) exports every
file `data/files.py` names that a loader reads. A registry only the harness reads must not reach the
port, so its path is anchored here from `HARNESS_DIR` and `files.py` does not name it.
"""

from __future__ import annotations

from ..data.files import HARNESS_DIR
from ..data.rosters import load_yaml
from ..data.verbs import EVENT_KINDS, VERB_TABLE
from ..queries import world_q

STRIFE_MOVES_YAML = HARNESS_DIR / "strife_moves.yaml"


def declared_kinds() -> frozenset:
    """Every Event kind the loop declares: `data/verbs.py::EVENT_KINDS`, the one owner (loader invariant 7).

    A STRICT SUPERSET OF THE ROSTER THIS FUNCTION USED TO BUILD. That one (`EMITTED_KINDS` and the write matrix's
    `emits:`) already held the per-degree and per-clause emission columns, since `VerbRow.emits` and
    `emits_on_refusal` are flat unions over them. What `EVENT_KINDS` adds is `fold_kinds` and `logged_kinds`
    (`act.ineligible`, `act.refused`, `attempt.refused`, `standing.band_crossed`), so the loader now accepts
    those four; no kind it accepted is refused, and none of the four is named in the registry."""
    return EVENT_KINDS


def load_moves(path=STRIFE_MOVES_YAML) -> tuple:
    """`(rows, signatures)` of `strife_moves.yaml`, validated, in file order. The foreign nations are not here:
    CR-75 moved them to `rosters.yaml: foreign_factions` (`data/rosters.py::FOREIGN_FACTION_IDS`), so
    `queries/world_q.py`, which may not import the harness, reads them."""
    doc = load_yaml(path.read_text(encoding="utf-8"))
    rows, row_keys, needs_vocabulary = doc["moves"], set(doc["row_keys"]), set(doc["needs_vocabulary"])
    kinds, seen = declared_kinds(), set()
    for r in rows:
        code = r.get("code")
        unknown = set(r) - row_keys
        if unknown:
            raise ValueError(f"strife_moves.yaml: {code!r} carries unknown key(s) {sorted(unknown)}")
        if code in seen:
            raise ValueError(f"strife_moves.yaml: code {code!r} listed twice")
        seen.add(code)
        bad_verbs = [v for v in r["verbs"] if v not in VERB_TABLE]
        if bad_verbs:
            raise ValueError(f"strife_moves.yaml: {code} names verb(s) {bad_verbs} not in verb_table.yaml")
        bad_kinds = [k for k in r["kinds"] if k not in kinds]
        if bad_kinds:
            raise ValueError(f"strife_moves.yaml: {code} names Event kind(s) {bad_kinds} the loop does not declare")
        bad_needs = set(r.get("needs", ())) - needs_vocabulary
        if bad_needs:
            raise ValueError(f"strife_moves.yaml: {code} has needs {sorted(bad_needs)} outside side/office/context")
        if not r["kinds"] and not r.get("gap"):
            raise ValueError(f"strife_moves.yaml: {code} has no kinds and states no gap")
        if not isinstance(r.get("ends", 0), int) or r.get("ends", 0) < 0:
            raise ValueError(f"strife_moves.yaml: {code} has `ends` that is not a count")
    total = sum(r.get("ends", 0) for r in rows)
    if total != doc["study_cases"]:
        raise ValueError(f"strife_moves.yaml: per-code `ends` total {total}, not the study's {doc['study_cases']} cases")
    sig_keys, sides = set(doc["signature_keys"]), set(world_q.SIDES)
    sigs = doc.get("signatures", [])
    for g in sigs:
        unknown = set(g) - sig_keys
        if unknown:
            raise ValueError(f"strife_moves.yaml: signature {g} carries unknown key(s) {sorted(unknown)}")
        if g["code"] not in seen:
            raise ValueError(f"strife_moves.yaml: signature {g} names code {g['code']!r} that has no row")
        if g["kind"] not in kinds:
            raise ValueError(f"strife_moves.yaml: signature {g} names Event kind {g['kind']!r} the loop does not declare")
        cv = g.get("cause_verb")
        if cv is not None and cv != "none" and cv not in VERB_TABLE:
            raise ValueError(f"strife_moves.yaml: signature {g} names verb {cv!r} not in verb_table.yaml")
        if "victim_held" in g and not isinstance(g["victim_held"], bool):
            raise ValueError(f"strife_moves.yaml: signature {g} has `victim_held` that is not a boolean")
        if "attacker" in g and g["attacker"] not in sides:
            raise ValueError(f"strife_moves.yaml: signature {g} has attacker outside {sorted(sides)}")
    return tuple(rows), tuple(sigs)


LINK_TIERS = ("robust", "stable")
LINK_SIDED = frozenset({"KL", "CA", "DN", "XE"})        # the codes the study splits by side
LINK_SIDES = frozenset({"A", "R", "O"})                 # the study's sides of the person: authority, rebels, outside power
_LINK_KEYS = frozenset({"a", "b", "tier", "cases", "of"})
_FLOW_KEYS = frozenset({"leave_and_rejoin", "mean_share_pct", "end_off"})


def base_code(code: str) -> str:
    """A link code without its side suffix: `CA-R` is `CA`."""
    return code.split("-", 1)[0]


def load_links(doc=None) -> tuple:
    """`(links, leave_rejoin)` of `strife_moves.yaml`, validated, links in file order. `doc` is the parsed document
    (default: the file), so a planted bad one needs no file on disk. Refuses a code with no row, a side suffix on a
    code other than KL/CA/DN/XE or outside A/R/O, a link listed twice, a tier outside robust/stable, a key the row does
    not define, a `cases`/`of` that is not a count of at most `of`, a count of links other than `drawn_links`, and
    leave-and-rejoin figures that are not counts within the study's cases."""
    if doc is None:
        doc = load_yaml(STRIFE_MOVES_YAML.read_text(encoding="utf-8"))
    codes, seen, links = {r["code"] for r in doc["moves"]}, set(), []
    for r in doc["links"]:
        unknown = set(r) - _LINK_KEYS
        if unknown:
            raise ValueError(f"strife_moves.yaml: link {r} carries unknown key(s) {sorted(unknown)}")
        for end in (r.get("a"), r.get("b")):
            base, _, side = str(end).partition("-")
            if base not in codes:
                raise ValueError(f"strife_moves.yaml: link {r} names code {end!r} that has no row")
            if side and (base not in LINK_SIDED or side not in LINK_SIDES):
                raise ValueError(f"strife_moves.yaml: link {r} gives {end!r} a side suffix it cannot carry")
        if (r["a"], r["b"]) in seen:
            raise ValueError(f"strife_moves.yaml: link {r['a']}>{r['b']} listed twice")
        seen.add((r["a"], r["b"]))
        if r.get("tier") not in LINK_TIERS:
            raise ValueError(f"strife_moves.yaml: link {r['a']}>{r['b']} has tier {r.get('tier')!r}, not one of {LINK_TIERS}")
        if ("cases" in r) != ("of" in r):
            raise ValueError(f"strife_moves.yaml: link {r['a']}>{r['b']} states only one of `cases` and `of`")
        if "cases" in r and not (isinstance(r["cases"], int) and isinstance(r["of"], int) and 0 <= r["cases"] <= r["of"]):
            raise ValueError(f"strife_moves.yaml: link {r['a']}>{r['b']} has `cases`/`of` that are not counts, cases at most of")
        links.append(dict(r))
    if len(links) != doc["drawn_links"]:
        raise ValueError(f"strife_moves.yaml: {len(links)} links listed, not the study's {doc['drawn_links']}")
    flow = dict(doc["leave_rejoin"])
    if (set(flow) != _FLOW_KEYS or any(not isinstance(v, int) or v < 0 for v in flow.values())
            or flow["leave_and_rejoin"] > doc["study_cases"] or flow["end_off"] > doc["study_cases"]
            or flow["mean_share_pct"] > 100):
        raise ValueError(f"strife_moves.yaml: `leave_rejoin` must hold counts {sorted(_FLOW_KEYS)} within the study's cases")
    flow["cases"] = doc["study_cases"]
    return tuple(links), flow


MOVES, SIGNATURES = load_moves()
LINKS, STUDY_FLOW = load_links()
