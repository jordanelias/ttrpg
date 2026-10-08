"""EVERY CASE, EXECUTED — not graded, and not merely attempted.

`run_cases.py` GRADES the corpus: it reads each case's prose `need` rows, looks up the authored
declaration naming which verb / hole / probe answers each one, and reports PLAYABLE / DEGRADED /
BLOCKED / NOT-ASSESSED. That is a judgement about whether the engine COULD support a character.

This RUNS them. Jordan asked for it, 2026-09-02: *"shouldn't we consider running all NPCs and all
arcs in our test runs? a larger surface introduces more complexity, but given our goals, what
solves one may solve another while providing more pushback as to whether something is the RIGHT
solve."* It is `CLAUDE.md` §0.1's *"targeted-green is not validation"* at corpus scale.

⚠ REV 2. THE FIRST VERSION MEASURED A QUANTITY ITS OWN FIXTURE HAD ALREADY FIXED, and its
adversarial pass overturned the headline. Three defects, all of them the same shape — an instrument
that could only return the answer it returned:

  1. **IT COUNTED ATTEMPTS AND CALLED THEM EXECUTIONS.** It read `driver.resolved`, and
     `self.resolved.append(a)` is the FIRST statement of `_fold` — before `_eligible`, before the
     `requires` predicate, before the wrote-nothing refusal. `shape.py` says so in terms: *"record
     which acts REACHED RESOLVE"*. Every "verb that executed" was a verb that was tried. Execution
     is now read from the EVENT LOG through Part E's own `emits:` / `emits_on_refusal:` columns,
     which is the design's own statement of what success looks like.
  2. **EVERY WORLD WAS THE SAME WORLD PERSON-SIDE.** It hung persons, the Proposition, the
     convictions and the sites all on `chain[0]`, so `scale` varied only the count of rungs ABOVE
     the actors — and `View.__slots__` is `(holder, claim_ids, question)` with `__getattr__`
     raising, so L2 closes the only channel by which a rung could reach a verb choice. *"One verb
     set across three worlds"* was therefore entailed by a ruled refusal plus an identical fixture,
     before anything ran. That is not a finding about the ladder.
  3. **A PERSON IS ALSO A RUNG AND THIS FIXTURE FORGOT IT.** `tiny_world` gives every person a
     `person`-kind Rung under the same id; `build_at` did not, so `_req_move`'s `w.rungs.get(
     a.actor)` was `None` and `move` was refused in every world in the corpus — while being
     reported as one of the seven verbs that "executed".

⚠ AND `scale` IS NOT THE CORPUS'S ONLY STRUCTURED FIELD, WHICH IS WHAT MADE REV 1's CEILING
ARGUMENT WRONG IN THE REVERSE DIRECTION. `temporal` is a mapping with declared sub-keys and **57 of
143 cases carry an integer `temporal.span_seasons`** (1..16), which rev 1 ignored while hardcoding
2. And `cases/ENDINGS_CLASSIFIED.yaml` already classifies endings into DECIDER/ROLL/THRESHOLD/
NEVER/UNCLEAR with a boolean `forced_by_threshold`. Both are read here. So the number of distinct
worlds is a property of what the BUILDER reads, never a ceiling the corpus imposes.

⚠ AN UNREPRESENTABLE SCALE STILL REFUSES rather than being folded onto the nearest rung: §42.2's
polarity rule sends zero evidence to the verdict AGAINST the thing measured, and mapping `faction`
onto `settlement` would manufacture a pass for the largest single block of the corpus.
"""
from __future__ import annotations
import string
import sys
from collections import Counter

from .. import decision
from ..data.fixtures import DEFAULT_FIXTURES, SITE_YIELD
from ..data.matrix import Step
# `CONVICTIONS` dropped 2026-09-16: `seed_pursuits` moved to `run_cases.py`, which is its
# single owner, and nothing here reads the roster any more.
from ..data.rosters import (PURSUIT_AXES, RUNG_KINDS, VERB_CAPABILITY, load_yaml,
                            refuse_a_titled_post_off_its_rung)
from ..data.verbs import VERB_TABLE, align, celled_verbs
from ..decision import make_chooser
from ..gaps import Forbidden, InstrumentDefect, NoProducer, ShapeGap, Unowned, Unspecified
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries.world_q import RESIDE_KIND, questions_for
from ..state.carriers import Act, Event, Office, Person, Proposition, Rung, Site, Tenure
from ..state.ids import H, ROOT, draw_factory
from ..state.world import World
from ..data import files
from . import probes as P
from . import run_cases as R
from .run_cases import seed_pursuits, wants_of

# `CLAUDE.md` §0.1 pt 5 / `G1`: declared here with its reason, not a bare literal in a body.
# [JUSTIFIED: an INSTRUMENT BUDGET, not a rule of the game -- no design document names a season cap. `W6`'s flood is the measurement it is fitted to: the corpus's longest `span_seasons` is 16, and running those costs more than the grading they buy. Lowering it truncates long cases; raising it changes no verdict this instrument reports]
MAX_SEASONS = 6          # the corpus asks for up to 16; the flood (`W6`) makes that unaffordable
DEFAULT_SEASONS = 2      # for the 86 cases whose `span_seasons` is prose ("ongoing")

_ENDINGS = files.ENDINGS_CLASSIFIED_YAML


def endings() -> dict:
    """`cases/ENDINGS_CLASSIFIED.yaml`, keyed by case id. Its own header calls the 19 of 50 rows
    carrying `forced_by_threshold` *"load-bearing on the whole proposal"*, and rev 1 did not read
    it — so a deadline that the corpus says forces the ending reached no world."""
    if not _ENDINGS.exists():
        return {}
    d = load_yaml(_ENDINGS.read_text())
    rows = d.get("cases") if isinstance(d, dict) else d
    return {r["id"]: r for r in (rows or []) if isinstance(r, dict) and r.get("id")}


ENDINGS = endings()


def rescales() -> dict:
    """`W28`. The corpus's `scale:` re-authoring, as an OVERLAY keyed by case id.

    ⚠ AN OVERLAY, NOT AN EDIT TO THE CORPUS, AND THE REASON IS ARCHITECTURAL. 47 of the 57
    unrepresentable cases live in `engine/season/cases/chain/` — a PREDECESSOR proposal's
    committed corpus, which this chain reads and does not own. Editing another chain's extraction
    would destroy the record of what was extracted, and the corpus is evidence. `cases/exercises/`
    is already the established overlay: per-case files, bound by id, carrying this chain's answers
    about someone else's rows. One overlay mechanism, not two (§8).

    ⚠ EVERY RE-SCALE CARRIES ITS `why:`, WHICH IS WHAT MAKES IT AUTHORING RATHER THAN INVENTION.
    The defect being repaired is that `CASE_BRIEF.md`'s schema offered `faction` and `world`, which
    `rung_kinds` has never had — so the extractors wrote a vocabulary the architecture had already
    closed. A re-scale is a reading of the case's OWN text; where the text does not say, the case
    stays unrepresentable, which is the honest answer (§42.2's polarity rule).

    ⚠ AND THERE IS NO CLASSIFIER. 23 of the 47 match none of the institution words the other 24
    do, so a keyword rule would cover half the corpus and silently mis-scale the rest — the ROUTER
    `W10` deleted, returning as a corpus tool. Measured before deciding not to build one."""
    out: dict = {}
    files_of: dict = {}                   # case id -> the file that authored its re-scale
    for f, doc in _exercise_docs():
        sc = doc.get("scale")
        if doc.get("case") and isinstance(sc, dict):
            if not sc.get("why"):
                raise SystemExit(f"{f.name}: a `scale:` re-authoring with no `why:` — the "
                                 "derivation is what distinguishes this from an invention")
            _check_office(f.name, sc.get("office"))
            # REFUSED, NOT OVERWRITTEN: two files naming one `case:` let the LAST silently replace
            # the first -- the refusal `cast_overlay` makes for a `cast:`, in the same words.
            if doc["case"] in files_of:
                raise SystemExit(f"{f.name}: `case: {doc['case']}` is already the case of "
                                 f"{files_of[doc['case']]}'s `scale:` -- the later file would "
                                 "silently replace the earlier one")
            files_of[doc["case"]] = f.name
            out[doc["case"]] = sc
    return out


def _exercise_docs():
    """The one directory walk `rescales()` and `cast_overlay()` both read a different top-level
    key off — `cases/exercises/*.yaml`, "ONE OVERLAY MECHANISM, NOT TWO" (this module's own
    header). Factored out (methodology close, 2026-09-29, `/simplify` REUSE lens) after the two
    functions carried this loop byte-for-byte twice, differing only in which key and which type
    check each reads afterward — a third overlay key (already anticipated: position `17`'s
    roles/offices) would otherwise have copied it a third time. Yields `(path, doc)` so a caller
    can still cite the file by name in its own error messages; tolerant of a missing directory
    (no `sorted(d.glob(...))` on a `d` that doesn't exist)."""
    d = files.EXERCISES_DIR
    if not d.is_dir():
        return
    for f in sorted(d.glob("*.yaml")):
        yield f, (load_yaml(f.read_text()) or {})


def _check_office(where: str, off) -> None:
    """`H-99`. An overlay's `office:` block, resolved against canon AT LOAD.

    ⚠ THE THREE AXES JORDAN ASKED FOR, AND THE CHECK IS HERE BECAUSE THE ERROR IS A RE-SCALING
    ERROR. 47 cases get an office authored by hand; the failure mode at that volume is a body
    seated in the wrong faction, which nothing downstream would notice — the world would build,
    the season would run, and a Cardinal would quietly belong to the Crown. `office_faction`
    refuses the mismatch, and refusing at LOAD means a bad overlay never reaches a world.

    ⚠ IT ALSO REFUSES A REMIT ACT THAT IS NOT IN THE ROSTER, for the same reason `Office` does:
    a remit is what the office MAY DO, and an unrecognised verb there is a silent no-op."""
    if off is None:
        return
    if not isinstance(off, dict) or not off.get("post"):
        raise SystemExit(f"{where}: an `office:` block with no `post:`")
    if not off.get("why"):
        raise SystemExit(f"{where}: an `office:` with no `why:` — same rule as `scale:`")
    if not off.get("body") and not off.get("faction"):
        # ⚠ REQUIRED AT THE OVERLAY, WHERE THE RULING APPLIES. `Office` leaves belonging optional
        # because a test fixture is not a canon office; a corpus overlay that names neither a
        # `body` nor a `faction` has simply not answered Jordan's question, and §42.2's polarity
        # rule makes no evidence a refusal rather than a default.
        raise SystemExit(f"{where}: an `office:` names neither a `body` nor a `faction`")
    # ⚠ THE VALIDATOR IS THE CONSTRUCTOR, NOT A SECOND COPY OF ITS RULES (§8). Rev 1 re-checked
    # the faction and the remit here by hand, and drifted immediately: `Office.__post_init__`
    # refuses a post that is both a TITLE and a body, and this loader did not, so
    # `{post: "King", body: "Cardinal of Justice"}` passed the overlay gate and was refused only
    # later at world-build. Building a throwaway Office means every rule the class enforces --
    # present and future -- applies at LOAD, before any world exists.
    try:
        Office("probe:" + where, str(off["post"]), None,
                 list(off.get("remit") or []),
                 body=off.get("body"), faction=off.get("faction"))
    except (Unspecified, Forbidden, Unowned) as e:
        raise SystemExit(f"{where}: {e}") from None


RESCALES = rescales()


def apply_rescale(case: dict) -> dict:
    """The case as the overlay re-authors it. Returns a copy; the corpus object is untouched."""
    sc = RESCALES.get(str(case.get("id")))
    if not sc:
        return case
    c = dict(case)
    c["scale"] = sc.get("is", case.get("scale"))
    if sc.get("office"):
        c["office"] = sc["office"]
    return c


# `17`: THE ONE `role` VALUE THE READER BRANCHES ON. `PLAN.md` §W28: *"~44 of 97 ARC cases name a
# player, a PC or the party in `who_acts`, and those become `WAITS-ON-PLAYER` rather than a
# failure"* -- an entry the engine does not supply and does not seat. Every other `role` is free
# text the author writes and nothing reads, so this is a TERM, not a closed set: a typo of it
# (`waits on player`) seats a person, which is why the comparison folds case and why an author
# reads `seating`'s output before trusting a cast.
WAITS_ON_PLAYER = "WAITS-ON-PLAYER"

# The three people every world has when a case's `cast:` names fewer. `build_at` seated exactly
# these before `17`, and a cast that names one protagonist has not said the world holds ONE person
# -- so the floor stays anonymous until an author names more (`seat_ids`).
ANONYMOUS_SEATS = ("p_a", "p_b", "p_c")


def _waits_on_player(entry: dict) -> bool:
    return str(entry.get("role") or "").strip().upper() == WAITS_ON_PLAYER


def _partition_cast(entries: list) -> tuple:
    """`(seated, waiting)` over one `cast:` list: the ONE place that says which entries become people.
    `seating` reads a case's overlay through it and `_check_cast` validates a file's list through it,
    so load and build cannot disagree about who is seated."""
    return ([e for e in entries if not _waits_on_player(e)],
            [e for e in entries if _waits_on_player(e)])


def cast_overlay() -> dict:
    """`W28-cast`. The corpus's per-case `cast:` authoring, `{case_id: [entry, ...]}` — an OVERLAY,
    read the SAME way `rescales()` reads `scale:`/`office:` and for the identical reason: 27 of the
    46 NPC-lane cases are CHAIN-sourced (`cases/chain/NPC1..3.yaml`), a predecessor proposal's
    committed evidence this repo reads and does not own, so a `cast:` block is never written into
    those files in place. `cases/exercises/*.yaml` is the established overlay directory (its own
    header: *"ONE OVERLAY MECHANISM, NOT TWO"*) — this reads a THIRD top-level key from the SAME
    per-case files `rescales()` already reads `scale:`/`office:` from, rather than inventing a
    second directory or a second per-case file convention.

    ⚠ EACH ENTRY IS `{who, role, capability?, office?, ought?}` (`CAST_KEYS`, the closed set).
    `who` names a cast member — the case's own PROTAGONIST is its `name:` field, never retyped
    independently (a second copy of a fact the case already owns is the hazard `CLAUDE.md` §0.05
    cl.3 names); another entry is a person the case's own `who_acts`/`one_line` names. `role`
    is free text with ONE term the code branches on, `WAITS_ON_PLAYER`: an entry carrying it names
    a player the engine does not supply and is NOT seated as an actor (`seating`). `capability` is
    present only where the case's OWN text grounds a number — absent is the honest reading
    (§42.2's polarity rule), never a placeholder zero standing in for one.

    ⚠ `office:` AND `ought:` ARE AUTHOR-WRITTEN STRUCTURED FIELDS (position `17-cast`), EACH ROUTED
    THROUGH AN OWNER THAT ALREADY EXISTS, NEITHER READ OFF PROSE (the W10 router's failure):
      * `office: {post, why, body | faction, remit?}` is the SAME block a `scale:` overlay's
        `office:` carries and is checked by the SAME `_check_office`; `build_at` seats it through
        `_seat_office`, the one constructor of an overlay's office. Its `why:` is the derivation,
        which is what makes it authoring rather than invention.
      * `ought: {about, predicate}` is ONE OUGHT Proposition for that entry. `about` is the exact
        `who` of ANOTHER SEATED entry (a person, so Q4's referent is a person), `predicate` the
        author's words. It replaces, for that entry only, the rotation default `build_at` writes
        for every seat — same Proposition id, same `commit` edge — so `world_q.ambitions(w, p)`
        finds it with no new reader.
    ⚠ `knows:` IS REFUSED BY NAME, NOT SEATED. An initial Claim is a `Claim(...)` construction and
    no world builder here has one: the only sites are `loop/witness.py`'s five event-driven deposits
    and `probes.py`'s hand-built fixtures. Adding a sixth in `build_at` is a Layer-1 question
    (`AX-7` limits the sites, and a seeded belief is a deposit nobody witnessed), which this
    position stopped on rather than answering. A field that parses and then reads nothing would be
    the silent no-op that makes an author believe a belief was seated.

    ⚠ A MALFORMED ENTRY REFUSES AT LOAD (a world is never built from it), by `_check_cast`: not a
    mapping, no `who`, a key outside `CAST_KEYS`, a bad `office:` (`_check_office`'s own errors), an
    `ought:` that is not exactly `{about, predicate}` or whose `about` names no OTHER seated entry
    (or names two), a `capability:` that is not a mapping, names a key `VERB_CAPABILITY` has no verb
    drawing on, or carries a magnitude that is not a whole number, a WAITS-ON-PLAYER entry carrying
    an `office:`/`ought:` or the KEY `capability:` at all, even empty (never seated, so the field
    would read nothing), or more seated entries than `string.ascii_lowercase` can name (`seat_ids`).
    A FILE refuses at load too: a `cast:` with no non-empty string `case:` (blank, missing or
    misspelled), and a `case:` that another file's `cast:` already claimed.

    ⚠ COUNT THIS WITH THIS FUNCTION, NEVER WITH A GREP OVER THE CASE FILES. The historical GAP this
    position's own plan entry names in terms: an antagonist once re-derived a corpus count by
    grepping raw YAML and got it wrong, because `_tolerant_yaml` is what actually parses the
    chain's non-standard files (markdown fences, a truncated head) and a grep sees none of that
    parsing. `len(cast_overlay())` (or `len(CAST)`) is the harness's own count; a
    `grep -c 'who:' cases/**/*.yaml` is not, and will over- or under-count the moment a comment or
    an unrelated `who:`-shaped string appears in a file this function does not read as one."""
    out: dict = {}
    files_of: dict = {}                   # case id -> the file that authored its cast
    for f, doc in _exercise_docs():
        if "cast" not in doc:
            continue
        # REFUSED, NOT SKIPPED (the two ways an overlay used to vanish): a file carrying `cast:`
        # whose `case:` is blank, missing or misspelled was dropped without a sound, so the case it
        # was written for seated the three anonymous people; and two files naming one `case:` let
        # the LAST silently replace the first. `rescales()` keeps its own `case:` filter -- its
        # files are `scale:` files, and a file with no `cast:` has no cast to lose.
        case = doc.get("case")
        if not isinstance(case, str) or not case.strip():
            raise SystemExit(f"{f.name}: carries a `cast:` but no non-empty string `case:` "
                             f"(found {case!r}) -- the cast would be dropped without a sound")
        if case in files_of:
            raise SystemExit(f"{f.name}: `case: {case}` is already the case of "
                             f"{files_of[case]}'s `cast:` -- the later file would silently "
                             "replace the earlier one")
        files_of[case] = f.name
        entries = doc["cast"]
        # REFUSED, NOT SKIPPED: a `cast:` that is a mapping (or a block missing its `- `, or empty)
        # used to fall through the `isinstance(list)` filter and be dropped without a sound, so the
        # case seated the three anonymous people its author had written a cast to replace.
        if not isinstance(entries, list):
            raise SystemExit(f"{f.name}: `cast:` is a {type(entries).__name__}, not a list of "
                             "entries -- a mapping, or a block missing its `- `, would be dropped "
                             "without a sound")
        _check_cast(f.name, entries)
        out[case] = entries
    return out


# `17-cast`: THE KEYS A `cast:` ENTRY MAY CARRY. Closed on purpose: an entry key nothing reads is an
# author's belief that something was seated, so an unknown key refuses (`_check_cast`).
CAST_KEYS = ("who", "role", "capability", "office", "ought")
OUGHT_KEYS = ("about", "predicate")


def _referent(seated: list, entry: dict) -> int:
    """The index in `seated` of the OTHER entry `entry["ought"]["about"]` names -- by exact `who`,
    never by token. `seated`, not the whole cast: a WAITS-ON-PLAYER entry is nobody the engine
    seats, so an OUGHT about one would be about nobody. Raises `LookupError` unless exactly one
    OTHER seated entry carries that name (`e is not entry` is what makes an OUGHT about oneself
    refuse, as the rotation default has always guaranteed -- `build_at`'s own comment).

    [ASSUMPTION: an `ought:` names ANOTHER PERSON by the exact `who` the author typed, never a
    rung, a faction or oneself -- basis: Q4's referent is `(prop.subject,)`, and a PERSON subject is
    the half `build_at`'s 2026-09-13 measurement found load-bearing (443 -> 638 acts, 168 naming
    another person); a rung subject is the old control, and no id exists for an authored person
    until it is seated, so the name is the only key]"""
    who = str(entry["ought"]["about"]).strip()
    hits = [n for n, e in enumerate(seated) if e is not entry and str(e["who"]).strip() == who]
    if len(hits) != 1:
        raise LookupError(f"names {len(hits)} other seated entries ({who!r})")
    return hits[0]


def _check_capability(where: str, who: str, e: dict) -> None:
    """A SEATED entry's `capability:`, validated AT LOAD. `build_at` copies it onto the person, and
    its one reader, `seam/wrappers/sigma.py::_capability`, asks `Person.capability[VERB_CAPABILITY[
    verb]]` and nothing else -- `int()`-ed into a dice pool, halved into an opposed obstacle. So a
    key no verb maps to is NEVER READ, and a magnitude that is not a whole number is truncated
    (`2.5` -> 2) or raises at the first roll; both used to land silently, because `build_at` only
    tests `isinstance(cap, dict) and cap`. `VERB_CAPABILITY` is the owner of which keys exist -- the
    capability NAMES are its VALUES (`rosters.yaml: verb_capability`; its keys are verbs) -- so this
    asks it and keeps no list of its own. `{}` is the person's own default and is allowed: it seats
    nothing and does not claim to. (A WAITS-ON-PLAYER entry is refused for carrying the KEY at all,
    by `_check_cast`, before this runs.)"""
    if "capability" not in e:
        return
    cap = e["capability"]
    if not isinstance(cap, dict):
        raise SystemExit(f"{where}: cast entry {who!r}: `capability:` is a {type(cap).__name__}, "
                         f"not a mapping of capability key -> whole number -- {cap!r}")
    known = set(VERB_CAPABILITY.values())
    unread = sorted(str(k) for k in cap if k not in known)
    if unread:
        raise SystemExit(f"{where}: cast entry {who!r}: `capability:` keys no verb draws on: "
                         f"{unread} (`rosters.yaml: verb_capability` names {sorted(known)}) -- "
                         "nothing would ever read them")
    # `bool` is an `int` in Python and `True` would be read as a pool of 1: refused by name
    bad = {k: v for k, v in cap.items() if isinstance(v, bool) or not isinstance(v, int)}
    if bad:
        raise SystemExit(f"{where}: cast entry {who!r}: `capability:` magnitudes must be whole "
                         f"numbers (the pool is `int()`-ed, so a fraction would be truncated "
                         f"silently): {bad!r}")


def _check_cast(where: str, entries: list) -> None:
    """A case's `cast:` list, validated AT LOAD, so a malformed entry never reaches a world.
    `office:` goes through `_check_office` -- the validator IS the constructor's own rules (that
    function's comment), not a second copy -- and `ought:` through `_referent`, the resolver
    `build_at` seats from, so load and build cannot disagree about whom an OUGHT is about.
    `capability:` goes through `_check_capability`, which asks `VERB_CAPABILITY` what a key may be.
    An `ought.predicate` is a LABEL: nothing reads it (`H-185`), and it is validated only as
    non-empty text."""
    for e in entries:
        if not isinstance(e, dict) or not str(e.get("who") or "").strip():
            raise SystemExit(f"{where}: a `cast:` entry with no `who:` -- {e!r}")
    seated, _waiting = _partition_cast(entries)
    if len(seated) > len(string.ascii_lowercase):
        raise SystemExit(f"{where}: more seated `cast:` entries than the "
                         f"{len(string.ascii_lowercase)} seat ids `seat_ids` can name")
    for e in entries:
        who = str(e["who"]).strip()
        if "knows" in e:
            raise SystemExit(f"{where}: cast entry {who!r} carries `knows:`, which no builder seats "
                             "-- an initial Claim is a new `Claim` construction site (AX-7), a "
                             "Layer-1 question position `17-cast` stopped on")
        extra = sorted(set(e) - set(CAST_KEYS))
        if extra:
            raise SystemExit(f"{where}: cast entry {who!r} has keys nothing reads: {extra} "
                             f"(the closed set is {list(CAST_KEYS)})")
        # `capability` by KEY PRESENCE, not truthiness: an empty one (`{}`) on an entry nobody seats
        # is still an author believing something was seated, and `{}` passed the old test
        if _waits_on_player(e) and (e.get("office") or e.get("ought") or "capability" in e):
            raise SystemExit(f"{where}: cast entry {who!r} is WAITS-ON-PLAYER, so it is never "
                             "seated, and an `office:`/`ought:`/`capability:` on it would read "
                             "nothing")
        _check_capability(where, who, e)
        _check_office(f"{where}, cast entry {who!r}", e.get("office"))
        ought = e.get("ought")
        if ought is None:
            continue
        if (not isinstance(ought, dict) or set(ought) != set(OUGHT_KEYS)
                or not all(str(ought[k] or "").strip() for k in OUGHT_KEYS)):
            raise SystemExit(f"{where}: cast entry {who!r}: an `ought:` is exactly "
                             f"{{{', '.join(OUGHT_KEYS)}}}, both non-empty -- {ought!r}")
        try:
            _referent(seated, e)
        except LookupError as err:
            raise SystemExit(f"{where}: cast entry {who!r}: `ought.about` {err}; it must be the "
                             "exact `who` of exactly one OTHER seated entry") from None


CAST = cast_overlay()


def seating(case: dict) -> tuple:
    """`(seated, waiting)` -- THE ONE RESOLVER OF A CASE'S `cast:` (plan position `17`), `build_at`'s
    and `run_case`'s alike. `seated` is the entries that become people, in authored order; `waiting`
    is the entries carrying `WAITS_ON_PLAYER`, which are reported and never seated. A case with no
    overlay is `([], [])`, which `build_at` reads as *the anonymous floor and nothing else*."""
    return _partition_cast(CAST.get(str(case.get("id"))) or [])


def seat_ids(n: int) -> tuple:
    """The person ids for `n` seated cast entries: `p_a`, `p_b`, `p_c` first (the ids every probe,
    docket and `main()`'s own `p_a` read already key on), then `p_d`... in alphabet order. Never
    fewer than the anonymous floor. `cast_overlay` refuses a cast that would need more than the
    alphabet has."""
    return ANONYMOUS_SEATS + tuple(f"p_{c}" for c in
                                   string.ascii_lowercase[len(ANONYMOUS_SEATS):n])


def _seat_office(w: World, oid: str, pid: str, scope: str, off: dict) -> None:
    """ONE CONSTRUCTOR OF AN OVERLAY'S OFFICE: `off` is the `{post, remit, body | faction, why}`
    block `_check_office` validated, `pid` the person who holds it at `scope` (the deepest
    non-person rung). Both callers -- the case-level `office:` held by `p_a`, and a cast entry's
    own (`17-cast`) -- build it here, so the two cannot drift.

    ⚠ NO SILENT FILTER. Rev 1 wrote `[a for a in ... if a in S.REMIT_ACTS]`, dropping an
    unrecognised remit act on the floor -- a quiet default sitting underneath
    `Office.__post_init__`'s loud one, which could then never fire. Pass them through and let the
    constructor refuse.

    [ASSUMPTION: a cast entry's office sits at `scope`, the deepest non-person rung -- the same
    scope the case-level office has, because the overlay carries no per-entry rung key -- basis:
    `build_at`'s case-level `office:` seating, which this function now serves]

    ⚠ A TITLED POST MUST STAND AT THE RUNG KIND ITS TITLE GOVERNS, and only here is that kind known:
    `_check_office` validates the block at LOAD, before any world, and the rung is the case's own
    scale. The rule is `rosters.refuse_a_titled_post_off_its_rung`, the one `populated.seat_anchor`
    applies to an `offices.yaml` row; without it `{post: Duke, faction: Crown}` seated a Duke at a
    hearth. A post that is not a title (an organ, a Dicastery) stands at any rung, as before."""
    refuse_a_titled_post_off_its_rung(oid, off["post"], w.rungs[scope].kind, scope)
    w.offices[oid] = Office(oid, str(off["post"]), scope, list(off.get("remit") or []),
                            body=off.get("body"), faction=off.get("faction"))
    w.add_tenure(Tenure(f"t_{oid}", pid, oid, "hold", 0))


def seasons_for(case: dict) -> int:
    """The case's own `temporal.span_seasons` where it is an integer, clamped to `MAX_SEASONS`."""
    t = case.get("temporal")
    n = t.get("span_seasons") if isinstance(t, dict) else None
    return min(int(n), MAX_SEASONS) if isinstance(n, int) and n > 0 else DEFAULT_SEASONS


def build_at(case: dict, seed: int = 0) -> World:
    """A world for THIS case: the containment chain down to its `scale`, people who are themselves
    `person` rungs, a site per producing kind, a motive, and — where the corpus says the ending is
    forced by a threshold — a Date coming due, which is `questions_for`'s Q1.

    ⚠ WHO THE PEOPLE ARE (plan position `17`). A case with no `cast:` overlay seats the three
    anonymous people it always did (`ANONYMOUS_SEATS`). A case WITH one seats its entries -- the
    ones not `WAITS_ON_PLAYER`, which `seating` splits off and nobody seats -- as `p_a`, `p_b`, ...
    in authored order, each named for its `who` and carrying its own `capability`, and pads with
    anonymous people only up to the floor of three. An 11-entry cast seats eleven.

    ⚠ THE CONVICTIONS ARE SEEDED FROM THE CASE ID, over the THIRTEEN CONVICTIONS -- not over
    `conviction_axes`, which this said until 2026-09-16 and which `U3` superseded when the set
    it indexes went from 4 to 13. The draw itself lives in `run_cases.seed_pursuits`, its
    single owner; this module only calls it. Rev 1 wrote
    three axis names and the weight `0.9` as literals, which is a fill off the register (`G1`) and,
    worse, was the ENTIRE ranking function — `stance` is empty in these worlds and §F2's `urgency`
    term has no `c` in it, so the conviction axis alone orders every candidate. Identical
    convictions therefore forced identical rankings in every world. Seeding from the id makes them
    differ per case, reproducibly, and takes the axis names from the roster rather than a body."""
    scale = str(case.get("scale"))
    w = World(seed, DEFAULT_FIXTURES)
    order = list(RUNG_KINDS)
    chain = order[order.index(scale):] if scale in order else []
    # ⚠ NO SYNTHETIC `person`-KIND RUNG. Rev 1 minted `r_person` for a `scale: person` case AND
    # made each of the three people a `person` rung contained in it — a person inside a person.
    # Nothing refused it, because `add_tenure` validated no direction; `W28`'s ladder check found
    # it on the first build. `H-95` counts 37 person-scale cases, so 37 worlds had that shape.
    # The people ARE the bottom rung (`tiny_world` models it that way), so the synthetic one is
    # not a missing parent, it is a duplicate of the persons themselves.
    chain = [k for k in chain if k != "person"]
    ids = {k: f"r_{k}" for k in chain}
    for k in chain:
        w.rungs[ids[k]] = Rung(ids[k], k)
    for lower, upper in zip(chain, chain[1:]):
        w.add_tenure(Tenure(f"t_{lower}_in_{upper}", ids[lower], ids[upper], "contain", 0))
    for kind in sorted(SITE_YIELD):
        if SITE_YIELD[kind]:
            w.sites[f"s_{kind}"] = Site(f"s_{kind}", ids[chain[0]], kind,
                                          condition=w.fixtures.get("condition_scale"))
    seated, _waiting = seating(case)
    pids = seat_ids(len(seated))
    by_pid = dict(zip(pids, seated))      # the entry each seated person stands for; the floor has none
    for pid in pids:
        entry = by_pid.get(pid)
        w.persons[pid] = Person(pid, str(entry["who"]) if entry else pid)
        # ⚠ A PERSON IS THE BOTTOM RUNG OF THE LADDER, and `tiny_world` models it that way. Without
        # this, `move` is refused everywhere. ⚠ THE STATED REASON IS NOW STALE AND THE FIXTURE
        # IS NOT: `_req_move` was retired by `W-A` and the typed cell short-circuits on an
        # unbound `to` BEFORE it reads `w.rungs` at all, so the mechanism named here no longer
        # runs. The seat is still required — `Query.presence` and the contain-path read both need
        # it — but a reader should not be told a retired predicate is why.
        w.rungs[pid] = Rung(pid, "person")
        # The parent is the deepest NON-person rung, which after the filter above is `chain[0]`.
        # A case scaled at `person` therefore seats its people in the `hearth` -- the next rung up
        # -- rather than in a person-shaped container, which is what the ladder actually says.
        if chain:
            w.add_tenure(Tenure(f"t_{pid}_in", pid, ids[chain[0]], "contain", 0))
            # Plan position `19c`: and they live there (`populated.build_realm`'s rule).
            w.add_tenure(Tenure(f"t_{pid}_home", pid, ids[chain[0]], RESIDE_KIND, 0))
        w.persons[pid].pursuits = seed_pursuits(seed, str(case.get("id")), pid)
    # ⚠ `W28-cast`: THE CAST'S AUTHORED `capability`, WRITTEN ONCE, AT WORLD-GEN, AND NOWHERE ELSE.
    # `04_CODE_ARCHITECTURE.md` F.6 (`:1087`): *"capability's season writer ... world-gen writes it
    # once; nothing else does."* Until this, the one writer in the tree ZEROED the dict --
    # `probes.py::p11`'s own comment: *"`capability` at zero ... for EVERY corpus person"* -- which
    # is why R-09's roll varies by SEED and FIXTURE and never by PERSON (`hole_register.yaml`
    # H-126/H-127). Each seated entry writes ITS OWN `capability` onto ITS OWN person (position `17`
    # widened this from "the primary entry's onto `p_a`", which is the same rule when the cast has
    # one entry). A case with no overlay, an anonymous seat, or an entry with no `capability`
    # leaves the person exactly as before: `Person`'s own empty-dict default, never a fabricated
    # non-zero fill.
    for pid, entry in by_pid.items():
        cap = entry.get("capability")
        if isinstance(cap, dict) and cap:
            w.persons[pid].capability = dict(cap)
    # ⚠ `W28`: THE CASE MAY SEAT ITS OWN ACTOR ON AN OFFICE. A re-scaled case carries
    # `office: {post, remit, why}` — `post` names the office the prose names, `remit` the acts it
    # carries, and `why` records the DERIVATION, because that is what makes this authoring rather
    # than invention. A case without an `office:` block is unchanged.
    #
    # ⚠ AND THERE IS NO CLASSIFIER HERE, DELIBERATELY. 23 of the 47 faction cases match none of the
    # institution words the other 24 do, so a keyword rule would cover half the corpus and quietly
    # mis-scale the rest — which is the ROUTER `W10` deleted, returning as a corpus tool. Every
    # re-scale is authored against the case's own text and carries its `why:`; where the text does
    # not say, the case stays unrepresentable and that is the honest answer (§42.2).
    off = case.get("office")
    case_level = isinstance(off, dict) and bool(off.get("post"))
    if case_level:
        _seat_office(w, f"off_{case.get('id', 'x')}", "p_a", ids[chain[0]], off)
    # `17-cast`: AND EACH CAST ENTRY MAY SEAT ITS OWN. The same block, the same constructor
    # (`_seat_office`), held by THAT entry's person rather than `p_a`; the id carries the person so
    # it cannot collide with the case-level office above. An entry with no `office:` seats nothing.
    #
    # ⚠ THE CASE-LEVEL OFFICE IS `p_a`'S, SO THE FIRST SEATED ENTRY (`p_a`) MAY NOT CARRY ONE TOO:
    # it would seat `p_a` twice and `decision/options.py::exercised_seat` takes the first seat, so
    # the second would be inert while looking authored. REFUSED, not skipped -- the author put the
    # entry's own office there to be held (`NPC-038.yaml` leaves it off its first entry for this
    # reason, in a comment nothing read).
    for pid, entry in by_pid.items():
        entry_office = entry.get("office")
        if not isinstance(entry_office, dict):
            continue
        if case_level and pid == "p_a":
            raise Forbidden(
                f"case {case.get('id')!r}: the cast entry {entry['who']!r} is seated as `p_a`, "
                "who already holds the case-level `scale: office:`, and carries an `office:` of "
                "its own", "harness/corpus_run.py -- overlay offices",
                needs="the entry's office on a different entry, or the case-level office dropped "
                      "(one seat per person here: the second is never the one exercised)",
                law="`exercised_seat` takes the first seat a person holds, so a second office on "
                    "the same person is inert")
        _seat_office(w, f"off_{case.get('id', 'x')}_{pid}", pid, ids[chain[0]], entry_office)
    # ⚠⚠ **THE OUGHT NAMES A PERSON, AND THE WANT IS THE CASE'S OWN.** Until 2026-09-13 this was
    # ONE Proposition for all three people -- `Proposition("prop_x", "OUGHT", ids[chain[0]],
    # "a standing ambition", ...)` -- whose subject was a **rung** and whose predicate was a single
    # authored string repeated across all 143 worlds. Both halves were load-bearing and both were
    # wrong:
    #
    #   * `world_q`'s Q4 emits `(prop.subject,)` as the referent, so a RUNG subject means every
    #     question a committed person raises is about a place. MEASURED through the season driver
    #     over the 27 NPC cases that build, with the old world as the control:
    #         control (rung subject)    443 acts,   0 naming another person
    #         arm     (person subject)  638 acts, 168 naming another person
    #     Acts rise 44% because person-subject questions open verbs that were unreachable at all.
    #     Traces to `ED-IN-0210` Ruling 1 (Jordan, 2026-09-10): *"verbs invoke mechanisms or
    #     interactions between a character and another entity/character. they are not fiats."*
    #   * one shared predicate gave all 143 cases the same ambition, which is `build_at`'s
    #     three-identical-people defect in the motive rather than in the cast. `wants_of` reads the
    #     case's own first `core` row of `season_requires`; the corpus declares 427 of them.
    #     ⚠⚠ **AND THIS HALF IS BEHAVIOURALLY INERT TODAY — SAID HERE BECAUSE THE FIRST DRAFT OF
    #     THIS COMMENT CLAIMED BOTH HALVES WERE LOAD-BEARING AND AN ADVERSARIAL PASS REFUTED IT.**
    #     Q4 reads `prop.mood` and `prop.subject` ONLY (`queries/world_q.py:246-248`), and sets
    #     `q.about` to the proposition ID, not its predicate. No live path reads
    #     `Proposition.predicate` at all, so the 443 -> 692 acts and the 0 -> 256 person-naming
    #     acts are attributable to the SUBJECT, not to `wants_of`. What the predicate reaches is
    #     `World.content_hash` (`propositions` is in `_STATE_COLLECTIONS`) and a human reading a
    #     world. It is kept because "a standing ambition" 143 times is a lie about the corpus and
    #     this is not; it is NOT claimed as a cause of any number above.
    #
    # ⚠⚠ **THE ROTATION IS A DEFAULT, NOT A REFUSAL, AND THAT IS A KNOWN DIVERGENCE FROM THE
    # SINGLE OWNER OF THIS DECISION.** With three ANONYMOUS people nothing in the case says which
    # of them a want is about -- `concerns_of` resolves `who_acts` to a CASE id, and no case id
    # maps to `p_a`/`p_b`/`p_c`. So each person's OUGHT names the next, which guarantees only that
    # nobody's ambition is about themselves.
    #
    # `harness/populated.py` ALREADY OWNS THIS and does it properly: a four-tier priority chain
    # (named in `who_acts` -> same institution -> same roof -> next building) with the rule
    # recorded per person, and it REFUSES BY NAME to do what this loop does --
    # *"Nobody is tied to a stranger by a draw. A draw here would read as a relationship and be one
    # only by accident"* (`populated.py`), and *"a person with no tie at all is the one case that
    # writes nothing: an OUGHT about nobody is not a motive"*. Under §42.2's polarity rule the
    # conformant answer here is that same `continue`.
    #
    # ⚠ **IT IS NOT TAKEN, AND THE REASON IS THE ONE JORDAN GAVE: *"Always improve game."*** A
    # `continue` in a three-anonymous-person world writes no Proposition, so nobody holds a `commit`,
    # so Q4 raises nothing and the corpus grader measures a world where NOBODY ACTS. The rotation is
    # the lesser of two wrongs and is labelled as a wrong rather than dressed as a rule.
    #
    # ⚠ **AND "W27 WILL REPLACE IT" WOULD BE FALSE, SO IT IS NOT SAID.** `populated.py` IS `W27`,
    # landed 2026-09-13, and it declares itself *"a second instrument beside [`corpus_run`], not a
    # replacement"*. Nothing currently schedules this loop's removal. Removing it means porting
    # `populated`'s per-case cast INTO `build_at` -- item 2 of `workplans/2026-09-13-work-order.md` -- and
    # until somebody does that, this default is load-bearing on every number the grader reports.
    #
    # ⚠ `17`: THE ROTATION NOW RUNS OVER EVERY SEATED PERSON (`pids`), a cast's eleven as readily as
    # the floor's three, AND IT IS THE DEFAULT, NOT AN AUTHORED OUGHT: the case's own `wants_of` and
    # the next person in the rotation stand in for every entry that wrote none.
    # ⚠ `17-cast`: AN ENTRY'S `ought: {about, predicate}` REPLACES THE DEFAULT FOR THAT ENTRY ONLY -- the
    # same Proposition id (`prop_<pid>`), the same `commit` edge below, so `ambitions` and Q4 find
    # it with no new reader. `about` resolves through `_referent`, the resolver `_check_cast`
    # validated with. Reading `one_line` for either half would be the token-match this file refuses.
    want = wants_of(case)
    for i, pid in enumerate(pids):
        entry = by_pid.get(pid)
        if entry is not None and entry.get("ought"):
            about, predicate = pids[_referent(seated, entry)], str(entry["ought"]["predicate"])
        else:
            about, predicate = pids[(i + 1) % len(pids)], want
        prop = Proposition(f"prop_{pid}", "OUGHT", about, predicate, True, 0)
        w.propositions[prop.id] = prop
        w.add_tenure(Tenure(f"t_{pid}_commits", pid, prop.id, "commit", 0))
    # The docket names ONE matter, so it names the first person's. `prop_x` is gone -- and an
    # adversarial pass confirmed NOTHING outside this function ever read that id, so the rename
    # breaks no surface.
    # Derived, not re-typed: `"prop_p_a"` was a hand-written copy of the `f"prop_{pid}"` rule
    # three lines above, so the id format had to stay in sync by eye and a change to `pids`'
    # order or contents would have silently pointed this at the wrong person.
    prop = w.propositions[f"prop_{pids[0]}"]
    if (ENDINGS.get(str(case.get("id"))) or {}).get("forced_by_threshold"):
        # Q1: a Date coming due, with a DocketItem naming a matter. The corpus says this case's
        # ending is forced by a threshold; a world with no deadline cannot represent that at all.
        w.dates["d_forced"] = {"id": "d_forced", "venue": ids[chain[0]], "due_at": 1,
                               "holder": None, "fired": False}
        w.docket.append({"date": "d_forced", "matter": prop.id})
    return w


# ===========================================================================
# `W18` -- THE RUN DEFINITION, AS AN INSTRUMENT (`PLAN.md` §6.1, §6.2)
#
# `run_cases.py` GRADES; this RUNS. The difference is the whole of `PLAN.md` Part 4B: the first
# item set optimised for a grading count that rose while zero cases ran.
#
# ⚠ A CHECK THIS CANNOT COMPUTE REPORTS `NOT-COMPUTABLE` AND NAMES THE ITEM THAT CLOSES IT. It
# does NOT score. `R2` needs authored `exercises:` rows and a real cast (`W27`); `A2`'s DECIDER and
# ROLL predicates need mechanisms `W26` and `W23` build; `A3` needs the case's own cast (`W27`).
# A number that cannot fail is not a measurement (§0.1 pt 2), and it flatters toward progress every
# time -- which this chain has now found in its own work six times.
# ===========================================================================

NOT_COMPUTABLE = {
    "R2": "W10-core (author the rows) + W27 (a real cast)",
    "A2": "W23 (contest results) + W26 (binding decisions) + W30 (the predicates)",
    "A3": "W27 (the cast comes from the case)",
}


def _register_sites() -> str:
    """Every `site:` on the register, as one string -- `R5`'s haystack.

    ⚠ THE SAME READING `W9` CHECK 3 USES, not a second one (§8). That check asserts the milestone
    run's fixture reads all resolve; this asks the same question per case."""
    from . import register as REG
    return " ".join(str(r.get("site") or "") for r in REG.load()["rows"])


def _r3_propagates(w, driver) -> bool:
    """`R3`: is there an **Act by another person** whose `causes[]` walks back to an act of a
    different person?

    ⚠ THE FIRST WORDING OF THIS CHECK SAID *AN EVENT* AND WAS SATISFIABLE 711 TIMES OVER ON DAY
    ONE. Every `claim.deposited` Event has a cause whose `subject` differs from its own -- that is
    what a witness deposit IS -- so an Event-level test scores every completing case immediately,
    and the instrument built to say zero would have opened by saying twenty-seven. Measured: 711 of
    711 deposits pass the loose reading; 0 Events have a cause that is an ACT by a different person.

    ⚠ AND IT MUST GO THROUGH `causes[] -> Act.actor`, BECAUSE THE EVENT HAS NO ACTOR BY RULING.
    #353 §19.3 puts `actor` among the three fields the Event does NOT carry; `driver.resolved` is
    the only surface that knows who acted, which is also what `H-82`'s `log u resolved` integrity
    check is for."""
    acts = list(getattr(driver, "resolved", []))
    if len(acts) < 2:
        return False
    # Event id -> the ACTOR of the act that emitted it, by the fold's own id derivation
    # (`H(seed, tick, actor, f"{kind}:{act.id}")`), which is the same route execution attribution
    # uses. One index, built once -- the first draft of this nested four loops and was O(n^4).
    emitter: dict = {}
    for a in acts:
        row = VERB_TABLE.get(a.verb)
        if row is None:
            continue
        for k in tuple(row.emits or ()) + tuple(row.emits_on_refusal or ()):
            for t in range(w.tick + 2):
                emitter[H(w.world_seed, t, a.actor, f"{k}:{a.id}")] = a.actor
    for e in w.log:
        mine = emitter.get(e.id)
        if mine is None:
            continue
        for c in (e.causes or []):
            theirs = emitter.get(c)
            if theirs is not None and theirs != mine:
                return True
    return False


def _span_status(case: dict) -> str:
    """`A1`: an integer `span_seasons` is run in full; a prose span REFUSES rather than defaulting.

    ⚠ REFUSES, NOT DEFAULTS. `MAX_SEASONS` clamps 3 arcs the corpus asks for at 8/10/16, and a
    silent default would report a 2-season run as an arc that ran its span. `W29` lifts the clamp;
    `W28` authors the prose spans."""
    t = case.get("temporal")
    n = t.get("span_seasons") if isinstance(t, dict) else None
    if not isinstance(n, int) or n <= 0:
        return "SPAN-UNAUTHORED"
    return "CLAMPED" if n > MAX_SEASONS else "OK"


def attribute(w: World, d, n: int) -> list:
    """`[(act, made, refused)]` for every act the fold resolved over `n` seasons — EXECUTION,
    ATTRIBUTED TO THE ACT, not to any verb that shares an emission kind. `made` is the tuple of the
    act's row's `emits:` kinds whose Event is in the log, `refused` the same over its
    `emits_on_refusal:` kinds — so each is truthy when an Event of that column's kinds is in the
    log, and `refused` says WHICH refusal when there are several. The two are not exclusive, for two
    DIFFERENT reasons (measured in the populated realm, 2026-09-30): a `march` can publish TWO
    Events, `march.declared` at RESOLVE and `march.refused` at ENCOUNTER; a LOST `tell` publishes
    ONE, `news.untold` at degree `Failure`, whose kind is in both the row's degree-keyed `emits:` and
    its `emits_on_refusal:` (deliberately — `verb_table.yaml`'s `tell` note), so both columns match
    the same Event. A graded loss is not a refusal (`04 §C.4`); `Event.degree` is what tells them
    apart, and this function does not read it — a caller that needs the difference reads it there.

    ⚠ THE KIND ALONE IS NOT AN ATTRIBUTION, AND READING IT AS ONE PUT A FALSE POSITIVE IN THE
    PUBLISHED SET. `forge` and `create_record` BOTH emit `record.created` (and `confer` and
    `revoke` both emit `tenure.closed`), so a scan over `{e.kind for e in w.log}` credited
    `forge` with every record `create_record` made — while `forge` has no predicate and no
    effect and cannot execute at all. Caught by cross-checking the executed set against the
    predicate/effect tables: a verb the fold cannot execute appeared among the verbs that did.

    The fold derives every emission's id as `H(seed, tick, actor, f"{kind}:{act.id}")`
    (`shape.py`, `_fold.ev`), so attribution is EXACT and reuses the design's own id scheme
    rather than adding a second rule for the same question (§8). The act id is unique, so a
    match at any tick is a genuine match for that act.

    ⚠ ONE OWNER, TWO CALLERS. This body sat inline in `run_case` and returned only verb SETS; the
    aperture re-measurement (`harness/aperture.py`, plan position `★`) needs the same answer PER
    ACT, so it can say which PERSON executed what. Extracted rather than re-derived there, so the
    corpus's "executed" and the populated realm's "executed" are one rule and cannot drift into
    two ladders for one quantity (`CLAUDE.md` §0.06 S)."""
    ids = {e.id for e in w.log}
    out = []
    for a in getattr(d, "resolved", []):
        row = VERB_TABLE.get(a.verb)
        if row is None:
            continue
        made, refused = (
            tuple(k for k in (kinds or ())
                  if any(H(w.world_seed, t, a.actor, f"{k}:{a.id}") in ids for t in range(n + 1)))
            for kinds in (row.emits, row.emits_on_refusal))
        out.append((a, made, refused))
    return out


def run_case(case: dict, seed: int = 0, lane: str = "NPC") -> dict:
    case = apply_rescale(case)
    scale, cid = str(case.get("scale")), case["id"]
    if scale not in set(RUNG_KINDS):
        return dict(id=cid, scale=scale, status="UNREPRESENTABLE", executed=[], refused=[],
                    seasons=0, why=f"`scale: {scale}` is not a rung kind", checks={})
    n = seasons_for(case)
    w = build_at(case, seed)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    try:
        for _ in range(n):
            # `H-87` -- S39.3 gives the contest depth cap NO DEFAULT, so an uncapped call raised
            # `Forbidden` before `contest()` was ever entered, for every case reaching a contested
            # act. `w.fixtures.get(...)`, not a literal -- `DEFAULT_FIXTURES.contest_max_depth`
            # is the one registered number (§0.05).
            d.season(ch, question=None, subsistence=P.SUBSIST,
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    except InstrumentDefect as e:
        # ⚠ THE TWO BUCKETS ARE SHAPE'S OWN, NOT A SECOND TAXONOMY (§8). `shape.py` states why the
        # split matters: a call-site bug landing in the design column *"corrupts the measurement in
        # the direction that flatters it"*. Rev 1 merged them and labelled the merged bucket
        # "an INSTRUMENT defect", which mis-attributes every design gap the fold can raise.
        return dict(id=cid, scale=scale, status="INSTRUMENT-DEFECT", executed=[], refused=[],
                    seasons=n, why=f"{type(e).__name__}: {e}", checks={"R1": False})
    except (ShapeGap, Unspecified, Forbidden, NoProducer) as e:
        return dict(id=cid, scale=scale, status="DESIGN-GAP", executed=[], refused=[],
                    seasons=n, why=f"{type(e).__name__}: {e}", checks={"R1": False})
    outcomes = attribute(w, d, n)
    ok = sorted({a.verb for a, made, _ in outcomes if made})
    no = sorted({a.verb for a, _, refused in outcomes if refused})
    # ---- `W18`: §6.1's R1/R3/R4/R5 and §6.2's A1, computed. R2/A2/A3 are NOT-COMPUTABLE.
    before = dict(DEFAULT_FIXTURES.reads)
    w2 = build_at(case, seed)
    d2 = SeasonDriver(w2)
    mint2 = lambda pid, verb, subj: H(w2.world_seed, w2.tick, pid, f"act:{verb}:{subj}")
    ch2 = make_chooser(w2.fixtures, mint2, verbs=resolvable_verbs(),
                       draw=draw_factory(w2.world_seed, lambda: w2.tick))
    try:
        for _ in range(n):
            # ⚠ THE SAME FIXTURE, ON BOTH CALL SITES. A cap on the measured run and not the R4
            # replay (or vice versa) would make the two runs different EXPERIMENTS -- one
            # reaching the contest seam and one refusing before it -- and R4 would then be
            # comparing a hash that never got a chance to diverge against one that did.
            d2.season(ch2, question=None, subsistence=P.SUBSIST,
                     contest_max_depth=w2.fixtures.get("contest_max_depth"))
        r4 = w2.content_hash() == w.content_hash()
    except Exception:
        r4 = False
    read = [k for k, c in w.fixtures.reads.items() if c > before.get(k, 0)]
    sites = _register_sites()
    checks = {
        "R1": True,
        "R3": _r3_propagates(w, d),
        "R4": r4,
        "R5": all(k in sites for k in read) if read else None,
        "A1": _span_status(case),
    }
    # §6.1's statuses. `RUNS` needs R2, which is NOT-COMPUTABLE — so a case that passes everything
    # computable is `RUNS-UNDECLARED`, which is the honest name for it and exists because the first
    # draft had no status a case could occupy today.
    core = checks["R1"] and checks["R4"] and (checks["R5"] is not False)
    if not core:
        status = "HALTS"
    elif lane == "ARC" and checks["A1"] == "SPAN-UNAUTHORED":
        status = "SPAN-UNAUTHORED"
    elif checks["R3"]:
        status = "RUNS-UNDECLARED"
    else:
        status = "RUNS-ALONE-UNDECLARED" if ok else "NO-EXECUTION"
    # `U1` / R-09: the bands the seam's provider resolved in this case. An Event carries a
    # `degree` only when the fold took the CONTEST branch and `degree_of` read one off the
    # subsystem's own result — so this is a count of rolls that happened, not of acts attempted.
    degrees = Counter(str(e.degree) for e in w.log if getattr(e, "degree", None))
    # `ED-IN-0222`: HOW EACH BELIEF IN THIS WORLD WAS COME BY. `rosters.yaml: claim_sources`
    # declares four and the loop wrote one until the told channel landed, which is a fact about
    # the GAME that no instrument reported -- so a claim about it could not be reproduced from
    # the tree, and `tools/ci_claim_provenance_check.py` is right to refuse one that cannot be.
    # ⚠ COUNTED PER WORLD AND SUMMED BY THE CALLER, like `degrees` above, rather than recomputed
    # from a second walk: the ledgers are this world's and the report is the corpus's.
    # ⚠ ONE WALK OVER THE LEDGERS, NOT THREE. `sources`, `told_holders` and `told_redeposits`
    # were three independent `for p_ in w.persons.values(): for c in p_.ledger` passes over the
    # same pairs, run once per corpus case (up to 143 a run). The redeposit count still needs
    # `own` complete before it can test membership, so it keeps its own second pass over THAT
    # person's ledger — which is per-person and bounded by `ledger_cap`, not a third world walk.
    sources, told_holders, told_redeposits = Counter(), 0, 0
    for p_ in w.persons.values():
        own, told_here, holds_told = set(), [], False
        for c in p_.ledger:
            sources[c.source] += 1
            if c.source == "told_by":
                holds_told = True
                told_here.append(c)
            else:
                own.add((c.subject, c.predicate, c.value))
        told_holders += 1 if holds_told else 0
        told_redeposits += sum(1 for c in told_here
                               if (c.subject, c.predicate, c.value) in own)
    # ⚠ THE REDEPOSIT COUNT IS THE ONE THAT CAUGHT A REAL DEFECT, so it is reported rather than
    # left to a probe. A `told_by` claim whose triple the hearer ALREADY HOLDS firsthand is one
    # belief stored twice — it tells them nothing and takes a `ledger_cap` slot from a claim that
    # would have. The first cut of the told channel deposited 180 and **175 were this**; the
    # corpus is where that is visible, because `build_world(0)` produces none.
    # `17`: the cast entries that name a player and so were NOT seated, by `who` -- the PLAN's
    # *"reported `WAITS-ON-PLAYER` naming the entry that caused it"*. Read through `seating`, the
    # same resolver `build_at` seats from, so the two cannot disagree about who was left out.
    return dict(id=cid, scale=scale, status=status, executed=ok, refused=no, seasons=n,
                why="", checks=checks, degrees=dict(degrees),
                claim_sources=dict(sources), persons=len(w.persons),
                told_holders=told_holders, told_redeposits=told_redeposits,
                waits_on_player=[str(e["who"]) for e in seating(case)[1]])


def planted_control(seed: int = 0) -> tuple:
    """`W18`'s CONTROL, and the only clause of its proof that demonstrates sensitivity.

    ⚠ PRINTING ZERO WHERE ZERO IS ENTAILED IS NOT A CONTROL (§0.1 pt 4). The first draft called it
    one. This plants a second person's Act caused by the first person's act and asserts `R3` flips
    false -> true; without it the instrument has shown only that it can print a number.

    Returns `(before, after)`."""
    case = next(c for c in R.load_cases("NPC") if str(c.get("scale")) in set(RUNG_KINDS))
    w = build_at(case, seed)
    d = SeasonDriver(w)
    before = _r3_propagates(w, d)
    # Two acts, two actors, the second caused by the first. Hand-built: the point is to prove the
    # DETECTOR works, not that the loop produces one -- the loop producing one is `W24`/`W25`.
    a1 = Act(id="ctl_a", actor="p_a", verb="speak")
    a2 = Act(id="ctl_b", actor="p_b", verb="speak")
    d.resolved.extend([a1, a2])
    k = VERB_TABLE["speak"].emits[0]
    # G1b: `Event.subject` is deleted, so each carries what it is about as a change (`P.about`).
    # `_r3_propagates` reads neither -- it attributes by the fold's id derivation -- so this keeps
    # the planted Events anchored for every OTHER reader of the log without moving the control.
    e1 = Event(H(w.world_seed, 0, "p_a", f"{k}:{a1.id}"), k, [P.about("p_a")], [ROOT], 0)
    e2 = Event(H(w.world_seed, 0, "p_b", f"{k}:{a2.id}"), k, [P.about("p_b")], [e1.id], 0)
    w.log.extend([e1, e2])
    return before, _r3_propagates(w, d)


def main(seed: int = 0) -> int:
    rows = []
    for lane in ("NPC", "ARC"):
        for c in R.load_cases(lane):
            r = run_case(c, seed, lane); r["lane"] = lane; rows.append(r)
    by = Counter(r["status"] for r in rows)
    print(f"CORPUS RUN — {len(rows)} cases, seed {seed}, seasons from `temporal.span_seasons`")
    for k, v in sorted(by.items()):
        print(f"  {k:18} {v}")
    un = Counter(r["scale"] for r in rows if r["status"] == "UNREPRESENTABLE")
    if un:
        print(f"  unrepresentable scales: {dict(un)}")
    # ⚠ THE DISCRIMINATION MEASUREMENT, which is what explains a single executed set across many
    # different worlds. §F2 ranks candidates by `Σ conviction[axis] · alignment(verb, axis)`, and
    # `alignment` is SPARSE with `default_cell: 0.0` — so a person's convictions separate only the
    # handful of (verb, axis) pairs the table actually carries. Every other candidate scores
    # identically and `sorted(..., key=(-score, c.verb, c.subject))` breaks the tie ALPHABETICALLY
    # BY VERB NAME. Reported rather than inferred, because "the worlds agree" is worthless without
    # saying WHY they agree (`H-97`).
    sep = []
    for c in R.load_cases("NPC") + R.load_cases("ARC"):
        if str(c.get("scale")) not in set(RUNG_KINDS):
            continue
        w2 = build_at(c, seed); w2.step = Step.DELIBERATE
        pr = w2.persons["p_a"]
        qs = questions_for(w2, pr)
        vw = decision.assemble(pr, qs[0] if qs else None, w2.fixtures.get("view_k"))
        cd = decision.opening_set(pr, vw, qs[0], w2.fixtures) if qs else []
        # ⚠ `U3`: THROUGH THE PROJECTION, AND VIA `decision.project` RATHER THAN A SECOND COPY
        # OF IT. This read `pr.convictions.get(a)` for each AXIS `a`, which was correct while the
        # conviction dict was keyed by axis; after the swap that lookup misses on every person and
        # this line would report a flat `0 of N` — a measurement silently reading zero, which is
        # the failure mode `H-97` exists to report on. `make_chooser` scores the same way (§8: the
        # rule lives once), so this instrument and the thing it measures cannot drift apart.
        axis_w = decision.project(pr)
        # ⚠ G-1 (2026-10-06, [medium; Jordan to correct]; IN-08's cells commit): THE DENOMINATOR
        # IS THE CANDIDATES WHOSE VERB HAS AT LEAST ONE CELLED AXIS (`data/verbs.py::celled_verbs`).
        # A candidate whose verb has none -- `tell`, declared `uncelled:` by design, or a verb every
        # cell of which is a considered `null` -- scores 0.0 for every person by construction, so
        # counting it would read as a tie the ranking failed to break when no score could break it.
        # R-06 and R-08 read this line that way; both figures are printed, never a ratio alone.
        celled = celled_verbs()
        cc = [x for x in cd if x.verb in celled]
        nz = sum(1 for x in cc if any(axis_w[a] * align(x.verb, a) for a in PURSUIT_AXES))
        sep.append((nz, len(cc), len(cd)))
    if sep:
        print(f"\n  RANKING DISCRIMINATION   {min(s[0] for s in sep)}..{max(s[0] for s in sep)} "
              f"(numerator) of {min(s[1] for s in sep)}..{max(s[1] for s in sep)} (denominator: "
              f"candidates whose verb has >= 1 celled axis; {min(s[2] for s in sep)}.."
              f"{max(s[2] for s in sep)} candidates in all) carry a nonzero pursuit score; the "
              f"rest TIE and the tie is broken BY THE DRAW (U4/H-96), not by the verb's name")
    # ⚠ A CASE THAT EXECUTED, WHATEVER ITS BAR STATUS. `W18` renamed the statuses (`RAN` became
    # `RUNS-UNDECLARED` / `RUNS-ALONE-UNDECLARED`), and this filter still named the old ones — so
    # the verb counts went to 0 of 32 the moment the bar landed, silently, because an empty set has
    # no obvious tell. Keyed on `checks["R1"]` now, which is the property meant all along: the run
    # completed. Caught by reading the output rather than by a test, which is the honest account.
    live = [r for r in rows if r.get("checks", {}).get("R1") is True]
    sigs = {tuple(r["executed"]) for r in live}
    print(f"\n  DISTINCT WORLDS RUN      {len(live)} (scales {sorted({r['scale'] for r in live})}, "
          f"season counts {sorted({r['seasons'] for r in live})})")
    print(f"  DISTINCT EXECUTED SETS   {len(sigs)}")
    # ⚠⚠ `U1` / R-09: THE BANDS THE SEAM ACTUALLY RESOLVED, AND THIS LINE IS THE MILESTONE'S OWN
    # OBSERVABLE. Before `U1` nothing in this instrument produced a margin, so `degree_of` was a
    # reader with no producer (`H-98`) and this histogram was necessarily empty. It is not a count
    # of contested ACTS — an act whose precondition fails never reaches the seam — but of rolls
    # that completed and were graded through `degree_from_net`, the tree's single ladder.
    # ⚠ AND IT MUST MOVE WITH THE RUN SEED. If the histogram at `corpus_run 7` matches this one,
    # the generator is not being constructed from the run seed and a same-seed determinism test
    # cannot see it — which is why the acceptance runs two seeds rather than one twice.
    _deg = Counter()
    for r in live:
        _deg.update(r.get("degrees") or {})
    print(f"  DEGREES RESOLVED         {dict(sorted(_deg.items())) or '{} — no contest completed'}")
    # `ED-IN-0222`. THE LINE THAT MAKES A CLAIM ABOUT BELIEF TRANSMISSION REPRODUCIBLE.
    # `rosters.yaml: claim_sources` declares four values; a run that reports three zeros is
    # reporting a hole, and one that reports none lets a session assert any number it likes.
    _src, _persons, _holders = Counter(), 0, 0
    for r in live:
        _src.update(r.get("claim_sources") or {})
        _persons += r.get("persons") or 0
        _holders += r.get("told_holders") or 0
    print(f"  CLAIMS BY SOURCE         {dict(sorted(_src.items()))} — of the four "
          f"`claim_sources`; {_holders} of {_persons} person-instances hold a `told_by`")
    # `17`: printed ONLY WHERE A CAST NAMES A PLAYER, so a corpus with none prints exactly what it
    # printed before this line existed.
    _waits = {r["id"]: r["waits_on_player"] for r in live if r.get("waits_on_player")}
    if _waits:
        print(f"  WAITS-ON-PLAYER          {len(_waits)} cases name a player the engine does not "
              f"supply: {_waits}")
    ever = sorted({v for r in live for v in r["executed"]})
    tried = sorted({v for r in live for v in r["refused"]})
    foldable = set(resolvable_verbs())
    print(f"\nVERBS THAT EXECUTED : {len(ever)} of {len(VERB_TABLE)} — {ever}")
    print(f"VERBS ONLY REFUSED  : {len(set(tried) - set(ever))} — {sorted(set(tried) - set(ever))}")
    print(f"\nWHERE THE {len(VERB_TABLE)} GO: {len(set(VERB_TABLE) - foldable)} have no "
          f"predicate/effect · {len(foldable - set(ever) - set(tried))} foldable but never even "
          f"attempted ({sorted(foldable - set(ever) - set(tried))}) · "
          f"{len(set(tried) - set(ever))} attempted and always refused · {len(ever)} executed")

    # ---- `W18`: THE BAR, per lane (`PLAN.md` §6.1 / §6.2) --------------------
    # [JUSTIFIED: a TERMINAL RULE WIDTH -- presentation, not a mechanical quantity. Nothing reads it and no value in the game depends on it; it is here because the fabrication gate counts every integer literal and a bare 72 is indistinguishable from a fitted threshold to a scanner]
    print("\n" + "=" * 72)
    print("THE BAR — `PLAN.md` Part 6.  Two counts, one per lane, NEVER averaged (`G10`):")
    print("  the NPC number counts PROPAGATION; the ARC number counts ENDINGS.")
    for lane in ("NPC", "ARC"):
        ls = [r for r in rows if r["lane"] == lane]
        st = Counter(r["status"] for r in ls)
        headline = "RUNS" if lane == "NPC" else "ENDS"
        # ⚠ `RUNS` / `ENDS` ARE NOT ASSIGNED STATUSES. `_case_status` emits only HALTS,
        # SPAN-UNAUTHORED, RUNS-UNDECLARED, RUNS-ALONE-UNDECLARED, NO-EXECUTION,
        # UNREPRESENTABLE, INSTRUMENT-DEFECT and DESIGN-GAP -- so `st.get(headline, 0)` returned
        # a CONSTANT 0 for every corpus, every seed, and was read off as a measurement of the
        # loop (it was quoted as one in PR #368's body and again at adoption). §0.1 pt 4: a
        # number without a control is not a measurement. The bar depends on `R2`, which is
        # NOT-COMPUTABLE, so the honest print is the reason -- not a zero that cannot move.
        blocked = NOT_COMPUTABLE.get("R2" if lane == "NPC" else "A2")
        print(f"\n  {lane}  ({len(ls)} cases)     ** {headline} = NOT-COMPUTABLE "
              f"-- closed by {blocked} **")
        for k, v in sorted(st.items(), key=lambda kv: -kv[1]):
            print(f"     {k:24} {v}")
        live = [r for r in ls if r["checks"]]
        for c in ("R1", "R3", "R4", "R5"):
            n = sum(1 for r in live if r["checks"].get(c) is True)
            print(f"     check {c}: {n} of {len(live)} pass")
            # IN-43: the count says THAT a case failed, not WHICH. Same `live` set as the count.
            failing = [r["id"] for r in live if r["checks"].get(c) is not True]
            print(f"     check {c} not True: {', '.join(failing) if failing else 'none'}")
    b, a = planted_control(seed)
    print(f"\n  CONTROL — planted cross-person edge: R3 {b} -> {a}  "
          f"{'(the detector works)' if (not b and a) else '⚠ THE CONTROL DID NOT FIRE'}")
    print("\n  NOT-COMPUTABLE — reported, never scored:")
    for k, why in NOT_COMPUTABLE.items():
        print(f"     {k}: closed by {why}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(*(int(a) for a in sys.argv[1:])))
