"""`manifest/registry.py` -- the role -> provider rows and the checks over them: `check_rows()`, and
(plan position `30`) the driver-construction refusals `check_contest_prizes()` and `check_effects()`,
and (plan position IN-41) `check_preconditions()`, refusal (a)'s precondition twin. Plan position
`31a` adds `check_contest_prizes()`'s third half: a prize row's `module_entry:` agrees with its
composition row. v9 FI-02 (`SM-3`) adds the second role, `inquiry`, and its refusal,
`check_inquiry_modules()`.

A REGISTRY, in this repo, is a register (see `harness/register.py`) that code reads at load to look
a key up; these rows are one.

`04 §C.5` spells the call the seam makes, and this module answers it:

    provider = manifest.resolve("contest", prizes[prize])

`04 §A.2:136` types the module -- *"role -> provider rows, resolved at boot"* -- and `04 PART E step 10`'s
build step 10 states its done-condition: *"a misspelled manifest row fails at boot naming the row."*
"""

from __future__ import annotations

import inspect
from typing import Any, Optional

from ..data import files
from ..data.rosters import load_yaml, roster_map
from ..gaps import NoProducer, Unspecified

# ⚠ THE ROLE NAMES ARE DATA, NOT A LITERAL HERE. A role maps to the roster that declares its
# providers, and the map exists so `resolve` does not branch on a role's name. Adding a role is a
# data edit, one row in this map, AND its own construction-refusal function (`check_contest_prizes`,
# `check_inquiry_modules`) with a call to it from `loop/driver.py`'s construction -- the refusals are
# per role, so `check_rows()` alone does not cover a new role's providers or entries.
_ROLE_ROSTERS = {"contest": ("contest_subsystems", "prizes"),
                 "inquiry": ("inquiry_modules", "findings")}
# ⚠ TWO ENTRIES SINCE v9 FI-02 (`SM-3`; Jordan, 2026-09-05: *"investigation is not a contest seam. it is
# its own thing."*). `inquiry` maps the KIND a graded finding emits to the fieldwork container
# (`rosters.yaml: inquiry_modules`), built in one landing with its caller, FI-03 (`ED-FI-0002`), because
# ID-13 forbids a role no caller requires. `check_rows()` and `World.boot` iterate this map and so cover
# the new rows unedited; the construction refusals are per role (`check_contest_prizes`,
# `check_inquiry_modules`), each reading its own row of this map.


# ---------------------------------------------------------------------------
# ⚠ THE CONTRACTS FILE IS READ AND PARSED **ONCE PER PROCESS**, AND THE CACHE IS A BUG FIX RATHER
# THAN AN OPTIMISATION. `check_rows()` runs on every `SeasonDriver` construction (that is where
# `04 PART E step 10`'s "at boot" actually reaches a run), and it resolves every row; each `resolve` was
# re-reading and re-parsing `references/module_contracts.yaml` from disk. The corpus builds many
# drivers, and the season suite went from ~170s to over 600s -- measured, on the commit that wired
# it. A per-process cache is safe because the file is repository content that cannot change under a
# running season; a test that needs it re-read clears `_CONTRACTS_CACHE`.
# ---------------------------------------------------------------------------
_CONTRACTS_CACHE: list = []


def _contracts() -> list:
    """`references/module_contracts.yaml`'s `modules:` list, parsed once."""
    if not _CONTRACTS_CACHE:
        text = files.MODULE_CONTRACTS_YAML.read_text()
        _CONTRACTS_CACHE.append((load_yaml(text) or {}).get("modules") or [])
    return _CONTRACTS_CACHE[0]


# ---------------------------------------------------------------------------
# `U1`: THE ROLE -> PROVIDER **CALLABLE** TABLE, AND IT IS THE OTHER HALF OF THE ROW.
#
# `resolve(role, key)` above answers *WHICH MODULE owns this key* by reading data. This answers
# *WHAT DO I CALL* -- the provider itself, registered by the module that defines it. `04 §C.5:682`
# spells the seam's call as `provider = manifest.resolve("contest", prizes[prize])`, and a name is
# only half a provider: something has to turn it into a function without the seam branching on it.
#
# ⚠ **THE DECORATOR IS `@effect_for`'s PATTERN AND THE REASON IS THE SAME ONE.** A table filled by
# decoration lives in the module that defines the decorated things, or it is empty at the moment the
# seam reads it. `loop/effects.py` states that rule at length for `EFFECTS`; this is it once more,
# one seam along.
#
# ⚠ **AND IT IS WHAT REPLACES `if _sub["module"] == "personal_combat":` IN `seam/contest.py`.**
# ED-SC-0033 clause (1) rules exactly that: *"the seam dispatches by manifest ROW rather than the
# hardcoded personal_combat literal"*. A literal in the seam is a second registry that disagrees
# with the first the day a row moves.
# ---------------------------------------------------------------------------
# ⚠⚠ **THE TABLE AND THE DECORATOR MOVED TO `manifest/providers.py`, A LEAF, TO BREAK A REAL
# IMPORT CYCLE.** They were defined here beside `_load_providers()`, which imports
# `seam/wrappers/*`, while the wrappers import the decorator back:
# `manifest.registry -> seam.wrappers.sigma -> manifest -> manifest.registry`.
# `_load_providers`'s docstring called that cycle *"genuine"* and made its import lazy, which hid
# it from the interpreter and not from the instrument: the cycle count went 3 -> 4 on the `U1`
# tree, and `tests/valoria/test_import_cycle_game_state_npe.py` says why in its own words --
# *"A deferred or bare-named import hides a cycle from an instrument; it does not remove it."*
# The table is a PRIMITIVE and this module is a POLICY over it; splitting them makes the package
# acyclic by construction. Re-exported here so every existing caller of
# `manifest.registry.provider` is untouched.
from .providers import PROVIDERS, provider      # noqa: F401


def has(role: str, module: str) -> bool:
    """Is a provider REGISTERED for this row? Read by `check_contest_prizes()` at driver construction
    (plan position `30`; it was `resolvable_verbs()`'s third gate, deleted there because the refusal
    made it unable to be false).

    ⚠ IT IS A QUESTION ABOUT THE CODE, NOT ABOUT THE DATA, WHICH IS WHY IT IS SEPARATE FROM
    `resolve`. A roster row may name a module the contracts file declares and nothing may have
    registered a callable for it — `mass_battle` was exactly that until `ED-IN-0279` (M3) gave it
    a provider; every prize row has one as of that plan, but this function stays the live check
    rather than a historical note, since a future row could land unregistered again. `resolve`
    answers *whose prize is this*; this answers *can anybody actually run it*, and a verb is
    resolvable only on the second.

    ⚠ **IT NO LONGER IMPORTS ANYTHING TO MAKE THE ANSWER TRUE.** `_load_providers()` stood
    here and imported `seam/wrappers/*`, which was an import cycle -- see
    `seam/wrappers/__init__.py` for the loop and the cut. The seam registers its own providers
    now, so this READS a table somebody else filled, which is what a registry should do. Every
    real caller arrives through `loop/driver.py` or `loop/resolve.py`, both of which import
    `..seam`."""
    return (str(role), str(module)) in PROVIDERS


def call(role: str, module: str):
    """The registered provider, or `None`. The seam's one lookup.

    ⚠ Reads the table; never fills it. See `has()` and `seam/wrappers/__init__.py`."""
    return PROVIDERS.get((str(role), str(module)))


def resolve(role: str, key: Any) -> Optional[dict]:
    """The provider a role's registry names for this key, or `None` if no row claims it.

    `None` IS A REAL ANSWER, not a failure: an unclaimed prize leaves the seam's generic refusal
    intact, which is the behaviour `seam/contest.py` had before this rule moved here and which its
    callers still depend on. What is NOT a real answer is a row naming a module no contract
    declares -- that raises, because the dispatch target would otherwise be invented.

    ⚠ NEITHER HALF IS INVENTED HERE. The KEY is what Part E's `contests:` column carries; the
    PROVIDER is a module `references/module_contracts.yaml` already declares with a resolver."""
    roster, column = _ROLE_ROSTERS.get(role, (None, None))
    if roster is None:
        raise Unspecified(
            f"no registry is declared for role {role!r}", "S43",
            needs=f"a `{role}` entry in manifest/registry.py's role map, and the roster it names",
            law="04 §D.4 -- the seam names a ROLE and a manifest row names the PROVIDER. A role "
                "with no registry has no provider to name, and guessing one is the path literal "
                "in a body that S43 refuses")
    # ⚠ `U1`: A PRIZE IS A ROW NOW, NOT A MODULE STRING, AND BOTH SHAPES ARE READ HERE SO THE
    # SCHEMA CHANGE IS ONE EDIT RATHER THAN A SWEEP. `module:` is whose prize it is — what the
    # contracts file is checked against and what the seam names when it refuses. `provider:` is
    # what actually runs it, which `manifest.call` asks for separately, and the two are different
    # questions the moment an interim resolver stands in for an unbuilt subsystem.
    row = roster_map(roster, column).get(str(key))
    if row is None:
        return None
    # ⚠⚠ **A NON-DICT ROW IS A MODULE WITH NO PROVIDER, AND SAYING SO IS THE FIX — NOT DELETING
    # THE BRANCH.** A `/simplify` pass read this as a dead compatibility shim, on the grounds that
    # all four shipped rows are dicts. They are; the branch is still live, because
    # `test_a_misspelled_manifest_row_fails_at_boot_naming_the_row` PLANTS a bare string
    # (`{"a fabricated prize": "no_such_subsystem"}`) as its misspelled-row arm, and deleting the
    # branch turned that boot refusal from a typed `Unspecified` naming the row into a raw
    # `AttributeError`. The suite caught it; the reasoning that it was unreachable did not.
    # ⚠ WHAT *WAS* WRONG IS THE SECOND READ, AND IT IS FIXED BELOW: it spelled
    # `row.get("provider") if isinstance(row, dict) else row`, so a string row returned the MODULE
    # as the PROVIDER — the one confusion `U1` added the `provider:` field to end. A string names
    # WHOSE prize it is and nothing about what runs it, so the provider is `None` and the row
    # refuses downstream like any other row with no provider.
    name = row.get("module") if isinstance(row, dict) else row
    if name is None:
        raise Unspecified(
            f"`{roster}` has a row for {key!r} with no `module:`", "S39",
            needs="a `module:` naming the subsystem that owns the prize",
            law="a prize row names WHOSE contest it is before it names what runs it; a row with a "
                "provider and no module says a thing can be rolled without saying what it is")
    provider_name = row.get("provider") if isinstance(row, dict) else None
    # M4 (`ED-IN-0279` clause (a)). `step:` names WHEN this prize is fought -- absent means
    # RESOLVE, the default every prize before M4 already had; `ENCOUNTER` defers to the seventh
    # phase. `declares:` is the band RESOLVE's own admission-and-fold writes while deferred.
    # Read here, once, because `04 §C.4`'s seam asks `manifest.resolve()` for both rather than
    # reaching into the roster row a second way -- one reader, not two.
    step = row.get("step") if isinstance(row, dict) else None
    declares = row.get("declares") if isinstance(row, dict) else None
    # Plan position `31a` (A-25). `module_entry:` names the composition role the provider calls
    # through `MODULE_ENTRIES` -- the prize row's half of *"two owners say which module is called"*.
    # Absent means the provider calls no module entry (yet). Read here for `step:`'s reason: one
    # reader of the row, not two; `check_contest_prizes()` holds it to its composition row.
    module_entry = row.get("module_entry") if isinstance(row, dict) else None
    contracts = files.MODULE_CONTRACTS_YAML
    if not contracts.exists():
        return dict(module=name, provider=provider_name, resolver="unknown",
                    doc="module_contracts.yaml not found", step=step, declares=declares,
                    module_entry=module_entry)
    for m in _contracts():
        if m.get("module") == name:
            # ⚠ THE PYTHON, NOT THE MARKDOWN. Jordan, 2026-09-02: *"we aren't using the .md or
            # anything for those systems. those are super outdated."* The contracts file carries
            # both a `doc:` (markdown) and a `sim_module:` (the live Python) for these three, and
            # the first version of this refusal printed the `doc:` -- so it pointed a reader at a
            # file its owner calls superseded.
            where = m.get("sim_module") or ""
            if not where:
                guess = files.subsystem_sim_dir(name)
                where = (f"systems/{name}/sim/" if guess.is_dir()
                         else f"(no `sim_module:` in module_contracts.yaml; "
                              f"`doc:` is {m.get('doc')!r} and is out of date)")
            return dict(module=name, provider=provider_name,
                        resolver=m.get("resolver") or "undeclared", doc=where,
                        step=step, declares=declares, module_entry=module_entry)
    raise Unspecified(
        f"`{roster}` maps {key!r} to {name!r}, which is in no module contract", "S39",
        needs="a module named in references/module_contracts.yaml",
        law="the roster may only name a subsystem the contracts file declares -- otherwise the "
            "dispatch target is invented")


def check_roles(manifest: dict, required_roles: tuple) -> None:
    """S43. Every required role has a provider, or a STARTUP FAILURE WITH A NAME IN IT.

    Moved here from `World.boot`, where the rule sat inline on a STORE. The `World` keeps the
    method -- its callers hold a world, not a manifest -- and delegates, so the rule lives once."""
    missing = [r for r in required_roles if r not in (manifest or {})]
    if missing:
        raise NoProducer(
            f"role(s) {missing} have no provider in the manifest", "S43",
            needs="a registry row naming a role and its provider",
            law="S43 -- the engine names the ROLE; the registry names the MODULE; RESOLUTION "
                "HAPPENS BY STRING AT BOOT. A missing provider is a startup failure with a name "
                "in it. THE MANIFEST IS THE SEAM; A PATH LITERAL IN A BODY IS NOT")


def check_rows() -> list:
    """`04 PART E step 10`'s done-condition: **a misspelled manifest row fails at boot naming the row.**

    Every row of every declared role's roster is resolved once. A row naming a module no contract
    declares raises from `resolve` with the row in the message, so the failure names what to fix
    rather than surfacing three seasons later as a null.

    ⚠ CALLED FROM `World.boot`, NOT AT IMPORT, and the reason is in this package's docstring: an
    import-time read of `module_contracts.yaml` would make every reader of one name pay for it.
    Returns the rows it checked, so a caller can assert the sweep was not empty -- a validator that
    resolved nothing has reported clean over an unexamined registry (`CLAUDE.md` §0.1 pt 2)."""
    checked = []
    for role, (roster, column) in _ROLE_ROSTERS.items():
        for key, row in roster_map(roster, column).items():
            resolve(role, key)
            _check_step_declares(role, key, row)
            checked.append((role, key))
    return checked


def _check_step_declares(role: str, key: Any, row: Any) -> None:
    """M4 (`ED-IN-0279` clause (a)): a `step:`/`declares:` pair, or neither -- never one field
    alone, and never a step or band the loop does not have. `04 PART E step 10`'s own done-condition --
    *"a misspelled manifest row fails at boot naming the row"* -- extended to the two fields M4
    added to a prize row.

    ⚠ CALLED FROM `check_rows()`, NOT AT IMPORT, for `check_rows()`'s own reason: an import-time
    read would make every reader of one manifest row pay to validate every row's timing fields."""
    if not isinstance(row, dict):
        return
    step, declares = row.get("step"), row.get("declares")
    if step is None and declares is None:
        return
    if (step is None) != (declares is None):
        raise Unspecified(
            f"{role}:{key!r} carries `step:` xor `declares:` ({step!r}, {declares!r})", "04 PART E step 10",
            needs="both fields together, or neither",
            law="a prize deferred to a later step must name the band its RESOLVE-time fold "
                "writes; one field with no partner is a row nobody finished")
    from ..data.matrix import Step
    if step not in {s.value for s in Step}:
        raise Unspecified(
            f"{role}:{key!r} declares `step: {step!r}`, which is on no row of `Step`", "04 PART E step 10",
            needs=f"one of {sorted(s.value for s in Step)}",
            law="04 PART E step 10 -- a misspelled manifest row fails at boot naming the row")
    from ..data.rosters import FIELD_BANDS
    if declares not in FIELD_BANDS:
        raise Unspecified(
            f"{role}:{key!r} declares `declares: {declares!r}`, which is on no row of "
            f"`field_degree_bands`", "04 PART E step 10",
            needs=f"one of {sorted(FIELD_BANDS)}",
            law="04 PART E step 10 -- a misspelled manifest row fails at boot naming the row")


def unclaimed_contest_prizes(verb_table: dict) -> list:
    """§B.13 invariant 9 (`04 §B.13 #9`): **every verb's `contests:` prize is in the subsystem roster.**
    `[(verb, prize)]` for each prize no `contest_subsystems` row claims; `check_contest_prizes()`
    below is the refusal that reads it.

    ⚠ **THIS IS THE OTHER HALF OF A MANIFEST ROW AND `check_rows()` DOES NOT COVER IT.** `check_rows`
    validates every roster row's PROVIDER -- that the module it names is one the contracts file
    declares. It says nothing about the KEY side: a verb declaring `contests: the bodyy` loads
    clean, boots clean, and at first call `resolve` returns `None` (a real answer, for a prize no row
    claims), so the seam falls through to its generic refusal, **naming no row.** That is the
    first-call failure mode `04 PART E step 10` replaces, surviving in the half nobody checked. Found by the
    Fable gate on Arc 1.

    ⚠ (plan position `30`) IT IS RAISED NOW, AT DRIVER CONSTRUCTION, by `check_contest_prizes()`;
    it was returned for a test to assert on while §B.13's loader was unbuilt. The loader half landed
    too -- `data/verbs.py` refuses an unclaimed prize at load (invariant 9) -- so a violation reaches
    the driver only through a table changed after load, which is exactly what a planted-violation
    test does."""
    claimed = set(roster_map(*_ROLE_ROSTERS["contest"]))
    out = []
    for verb, row in verb_table.items():
        prizes = getattr(row, "contests", None)
        if not prizes:
            continue
        for p in _as_list(prizes):
            if str(p) not in claimed:
                out.append((verb, str(p)))
    return out


def _as_list(x: Any) -> list:
    """A verb's `contests:` is one prize name or a list of them; either way, a list."""
    return [x] if isinstance(x, str) else list(x)


def check_contest_prizes(verb_table: dict) -> list:
    """Refusal (c), plan position `30`: **the contest roster, both halves, at driver construction.**

    1. A verb whose `contests:` prize no prize row claims -- refused naming the VERB
       (`unclaimed_contest_prizes`, above).
    2. A prize row whose `provider:` nobody registered -- refused naming the PRIZE. `has()` asks the
       CODE (`PROVIDERS`, filled when `seam/` is imported), not the data; a row with no `provider:`
       at all is the same defect, since nothing can be registered under no name.
    3. (plan position `31a`) A prize row whose `module_entry:` disagrees with its composition row, or
       names one no row declares -- refused naming the role (`_check_module_entry`, below).

    ⚠ HALF 2 IS WHY `loop/driver.py::resolvable_verbs()` LOST ITS `manifest.has` CLAUSE. That clause
    dropped a contested verb from the game SILENTLY when its prize's provider was not registered;
    once construction refuses that state, the clause can no longer be false on any run, and a gate
    that cannot be false is not a gate. Returns the `(role, prize)` rows checked, so a caller can see
    the sweep was not empty (`CLAUDE.md` §0.1 pt 2)."""
    unclaimed = unclaimed_contest_prizes(verb_table)
    if unclaimed:
        verb, prize = unclaimed[0]
        raise Unspecified(
            f"verb {verb!r} declares `contests: {prize!r}`, which no `contest_subsystems` row claims "
            f"(all: {unclaimed})", "04 §B.13 #9",
            needs="a `contest_subsystems.prizes` row for the prize, or the verb's `contests:` fixed",
            law="04 §B.13 #9 -- contest prizes are a SUBSET of the subsystem roster; an unclaimed "
                "prize reaches the seam's generic refusal at first call, naming no row")
    checked = []
    # ⚠ THE CONTEST ROLE ALONE (v9 FI-02, `SM-3`'s fact 4). This looped over EVERY role in
    # `_ROLE_ROSTERS`, which was the contest role while it was the only one; with `inquiry` beside it,
    # half 3 asked whether an inquiry entry's composition row `contests:` a prize -- it contests none,
    # by ruling -- and no driver constructed. `unclaimed_contest_prizes` and `check_graded_inquiries`
    # already read this one row of the map; the inquiry role's rows are `check_inquiry_modules`'.
    role = "contest"
    roster, column = _ROLE_ROSTERS[role]
    for key in roster_map(roster, column):
        row = resolve(role, key) or {}
        name = row.get("provider")
        if not name or not has(role, name):
            raise Unspecified(
                f"`{roster}` prize {key!r} names provider {name!r}, which nobody registered", "S43",
                needs=f"`@provider({role!r}, {name!r})` on the callable that runs it, imported "
                      "by `seam/`, or the prize row's `provider:` fixed",
                law="S43 -- a missing provider is a STARTUP FAILURE WITH A NAME IN IT; before "
                    "plan position `30` it silently removed every verb contesting the prize "
                    "from the game")
        _check_module_entry(role, key, row, verb_table, _VERB_CALL, _bound_verb_contests_it)
        checked.append((role, key))
    return checked


def check_inquiry_modules(verb_table: dict) -> list:
    """v9 FI-02 + FI-03 (`SM-3`, `ED-FI-0002`): **the `inquiry` role's rows, at driver construction** --
    refusal (c)'s shape, one role over, each refused naming the row:
      1. the row's `provider:` is registered under `@provider("inquiry", …)` (`has`, the code);
      2. it names a `module_entry:` (a prize row may name none; an inquiry row may not, since its
         provider always calls one), and that entry agrees with its composition row
         (`_check_module_entry`): a row declares it as a `step_call` entry -- RESOLVE's per-act bookkeeping calls it, keyed by the Event's kind, so no
         verb's adapter does -- whose target lies in the row's `module:`; and, half 3's analogue, a verb
         the loop GRADES (a `graded_inquiries` route) emits the row's key at some band, so the key can
         reach the entry carrying a degree (`_graded_verb_emits_it`);
      3. the provider takes the `module_entry` keyword `seam/contest.py::find_trail` always passes
         (`check_graded_inquiries`' refusal 3, for its reason: a `TypeError` at the first find).
    THIS IS THE DECLARATION THAT THE COMPOSITION ROW MUST EXIST: in a fresh process the registrar holds
    nothing to miss, so a deleted `fieldwork.find` row is refused here, naming it. Returns the
    `(role, key)` rows checked, so a caller can see the sweep was not empty (`CLAUDE.md` §0.1 pt 2)."""
    role = "inquiry"
    roster, column = _ROLE_ROSTERS[role]
    checked = []
    for key in roster_map(roster, column):
        row = resolve(role, key) or {}
        name = row.get("provider")
        if not name or not has(role, name):
            raise Unspecified(
                f"`{roster}` row {key!r} names provider {name!r}, which nobody registered", "S43",
                needs=f"`@provider({role!r}, {name!r})` on the callable that runs it, imported by "
                      "`seam/`, or the row's `provider:` fixed",
                law="S43 -- a missing provider is a STARTUP FAILURE WITH A NAME IN IT")
        # A row with no `module_entry:` would pass `_check_module_entry` unchecked (a prize row may
        # call no module entry) and fail at the first find instead: the provider always calls one.
        if not row.get("module_entry"):
            raise Unspecified(
                f"`{roster}` row {key!r} has no `module_entry:`", "04 PART E step 10",
                needs="the row's `module_entry:` naming the composition row its provider calls",
                law="A-25 -- the inquiry role's provider calls its module through the entry the row "
                    "names; a row naming none reaches `ENGINE-UNAVAILABLE` at the first find rather "
                    "than refusing construction")
        _check_module_entry(role, key, row, verb_table, _STEP_CALL, _graded_verb_emits_it)
        if "module_entry" not in inspect.signature(call(role, name)).parameters:
            raise Unspecified(
                f"`{roster}` row {key!r} names provider {name!r}, which takes no `module_entry` keyword",
                "S43", needs="a provider accepting the row's module entry, or the row's `provider:` fixed",
                law="`seam/contest.py::find_trail` always passes `module_entry=`; a provider without it "
                    "fails at the first find rather than at construction")
        checked.append((role, key))
    return checked


def check_graded_inquiries(verb_table: dict) -> list:
    """v9 FI-01 (`ED-FI-0009`, J-22 option (A)): **an inquiry's route names a roll a prize row already
    binds, and is not itself a prize** -- at driver construction, naming the verb.

    `rosters.yaml: graded_inquiries` maps an inquiry verb to `{provider, module_entry}`, which
    `seam/contest.py::grade` calls with no prize. Three refusals, each a way the route could become a
    second resolver (a route that is also a contest is the loader's refusal, `data/verbs.py`):
      1. the provider is not registered (`has`, the code, as `check_contest_prizes` half 2 asks);
      2. no prize row binds the SAME `(provider, module_entry)` pair -- so the route reaches only a
         module entry the contest roster already holds to its composition row (`_check_module_entry`),
         and adds no roll of its own (S27.2);
      3. the provider takes no `module_entry` keyword (`grade()` always passes one, and only the
         `social_contest` adapter accepts it), which would be a `TypeError` at the first act.
    Returns the verbs checked, so a caller can see the sweep was not empty (`CLAUDE.md` §0.1 pt 2)."""
    from ..data.rosters import GRADED_INQUIRIES
    roster, column = _ROLE_ROSTERS["contest"]
    prizes = roster_map(roster, column)
    bound = {(r["provider"], r["module_entry"]) for k in prizes if (r := resolve("contest", k))}
    law = ("rosters.yaml -- investigation must not be made a contest to become gradeable; S27.2 -- one "
           "roll owner. A route is a pointer at a roll the tree already makes, never a prize and never "
           "a roll of its own")
    checked = []
    for verb, route in sorted(GRADED_INQUIRIES.items()):
        provider_name = route.get("provider")
        if not provider_name or not has("contest", provider_name):
            raise Unspecified(
                f"the graded inquiry {verb!r} routes to provider {provider_name!r}, which nobody "
                f"registered", "S43",
                needs=f"`@provider('contest', {provider_name!r})`, or the route's `provider:` fixed",
                law=law)
        if (provider_name, route.get("module_entry")) not in bound:
            raise Unspecified(
                f"the graded inquiry {verb!r} routes to ({provider_name!r}, "
                f"{route.get('module_entry')!r}), which no `{roster}` prize row binds "
                f"(bound: {sorted(bound, key=str)})", "S27.2",
                needs="the route naming a provider and module entry a prize row already binds",
                law=law)
        if "module_entry" not in inspect.signature(call("contest", provider_name)).parameters:
            raise Unspecified(
                f"the graded inquiry {verb!r} routes to provider {provider_name!r}, which takes no "
                f"`module_entry` keyword", "S27.2",
                needs="a provider whose adapter accepts a route's module entry (`social_contest`), "
                      "or the route's `provider:` fixed",
                law=law)
        checked.append(verb)
    return checked


# The two entry kinds a role's rows are held to. The closed set's owner is
# `tools/export_composition.py::_ENTRIES` (validated at export); these are two of its members, named once
# here so the two callers below pass a kind rather than this function branching on a role's name.
_VERB_CALL, _STEP_CALL = "verb_call", "step_call"


def _bound_verb_contests_it(role: str, key: Any, entry_role: str, comp: dict, verb_table: dict,
                            law: str) -> None:
    """Half 3 for the CONTEST role (plan position `31a`): the composition row's `verb:` contests a prize
    whose row names the same entry, so the verb the entry is bound to reaches it through the seam."""
    verb = comp.get("verb")
    contests = getattr(verb_table.get(verb), "contests", None) or []
    prizes = _as_list(contests)
    if not any((resolve(role, p) or {}).get("module_entry") == entry_role for p in prizes):
        raise Unspecified(
            f"composition row {entry_role!r} binds `verb: {verb!r}`, which contests {prizes!r}; no "
            f"prize row among them names `module_entry: {entry_role!r}` (prize {key!r} does)",
            "04 PART E step 10",
            needs="the composition row's `verb:` naming a verb whose prize calls this entry",
            law=law)


def _graded_verb_emits_it(role: str, key: Any, entry_role: str, comp: dict, verb_table: dict,
                          law: str) -> None:
    """Half 3's analogue for the INQUIRY role (v9 FI-02): a `step_call` entry names no verb, so what must
    hold is that the row's KEY can reach it carrying a degree -- some verb the loop grades (a
    `graded_inquiries` route) emits the key at some band (`VerbRow.emits_by_degree`). Otherwise the
    entry is reached by ungraded findings alone, and `finding_terms` keys nothing for them."""
    from ..data.rosters import GRADED_INQUIRIES
    emitters = sorted(v for v in GRADED_INQUIRIES if v in verb_table and any(
        str(key) in kinds for kinds in (verb_table[v].emits_by_degree or {}).values()))
    if not emitters:
        raise Unspecified(
            f"`{role}` row {key!r} (`module_entry: {entry_role!r}`) is a kind no graded inquiry emits at "
            f"any band (graded: {sorted(GRADED_INQUIRIES)})", "04 PART E step 10",
            needs="the row keyed by a kind a `graded_inquiries` verb's degree-keyed `emits:` declares",
            law=law)


def _check_module_entry(role: str, key: Any, row: dict, verb_table: dict,
                        entry_kind: str, reached) -> None:
    """Refusal (c), half 3 -- plan position `31a`, generalised at v9 FI-02 (`SM-3`): **a role's row's
    `module_entry:` and its composition row agree** (A-25: *"two owners say which module is called"* --
    the role's row and the composition row). A row with no `module_entry:` calls no module entry and is
    not checked here; a role whose rows must name one refuses its absence before calling this
    (`check_inquiry_modules`).

    The caller passes the ENTRY KIND its role's rows are called through and the half-3 test
    (`reached`) -- `_VERB_CALL` and `_bound_verb_contests_it` from `check_contest_prizes`, `_STEP_CALL`
    and `_graded_verb_emits_it` from `check_inquiry_modules` -- so nothing here branches on a role's
    name, and neither has a default.

    THIS IS THE DECLARATION THAT A ROW MUST EXIST. The registrar refuses only a role it already holds
    (`manifest/registrar.py`), so in a fresh process a deleted composition row left nothing to refuse
    on (plan position `30`'s falsifier 2, observed only within one process). The role's row names the
    entry, so the row's absence is refused here, at driver construction, naming it. The composition
    rows are read through `engine/substrate/composition.py` (data loaded at import), never through
    `MODULE_ENTRIES`, so this refusal does not depend on a driver having been constructed earlier in
    the process. Agreement is three facts, each refused naming the role:
      1. a composition row declares the entry and carries `entry:`;
      2. it is an `entry_kind` entry whose target lies in the row's `module:` -- the module's one
         identity is its directory name, the target's first package under its root (A-25);
      3. `reached` holds: the role's own test that the entry is reachable from the verb table."""
    entry_role = row.get("module_entry")
    if entry_role is None:
        return
    from engine.substrate import composition

    law = (f"A-25 -- two owners say which module is called, the `{_ROLE_ROSTERS[role][0]}` row and "
           "the composition row; they agree or the driver does not construct")
    comp = composition.ROLES.get(entry_role)
    if comp is None or not comp.get("entry"):
        raise Unspecified(
            f"{role}:{key!r} names `module_entry: {entry_role!r}`, which no composition row declares "
            f"as an entry", "04 PART E step 10",
            needs="the composition row back in references/module_contracts.yaml `composition_roles:` "
                  "(re-run tools/export_composition.py), or the role row's `module_entry:` fixed",
            law=law)
    parts = str(comp["target"]).split(":", 1)[0].split(".")
    if comp.get("entry") != entry_kind or len(parts) < 2 or parts[1] != row.get("module"):
        raise Unspecified(
            f"{role}:{key!r} names `module_entry: {entry_role!r}`, whose composition row "
            f"(`entry: {comp.get('entry')}`, target {comp['target']!r}) is not a `{entry_kind}` into "
            f"module {row.get('module')!r}", "04 PART E step 10",
            needs="the role row and the composition row naming the same module, by its directory",
            law=law)
    reached(role, key, entry_role, comp, verb_table, law)


# ---------------------------------------------------------------------------
# REFUSAL (a), plan position `30`: A WRITING VERB ROW WITH NO EFFECT AND NO `effect_decline_note:`
# -- AND, SINCE PLAN POSITION IN-41 (`SM-9`), ITS CONVERSE: A ROW WITH AN EFFECT THAT DECLARES IT HAS
# NONE. Its twin, `check_preconditions` (`SM-11`), follows it.
#
# `EFFECTS` (`loop/effects_shared.py`) is the verb -> effect table and `@effect_for` its decorator --
# this module's `PROVIDERS`/`@provider` pattern one table over (the comment above `providers` says
# so) -- so the check over it sits beside `check_contest_prizes()`. `resolvable_verbs()`'s second
# gate (`loop/driver.py`) drops a writing verb with no effect from the game, and it used to do that
# WITHOUT A WORD: a row whose effect was deleted, or never written, quietly left the game. After
# this refusal every row that gate drops has SAID why, in its `effect_decline_note:`, or the driver
# does not construct.
#
# ⚠ TWO-SIDED SINCE IN-41. At `30` it was one-sided by [ASSUMPTION] (`SM-9`): the converse
# (`SM-9`) -- a row carrying BOTH an effect and a declining note -- fired on the shipped
# tree, because `oblige` and `destroy_record` used the one `decline_note:` column to decline their
# FORMATION (`14`), not their effect. IN-41 split the column: `effect_decline_note:` (read here),
# `formation_decline_note:` (an annotation nothing gates on; those two rows) and
# `requires_decline_note:` (`check_preconditions`, below). With the split the converse fires on
# nothing shipped, so it is armed: a note declining an effect that exists is a stale declaration,
# and a declaration that can be false is the silent state this refusal ends.
#
# ⚠ A CONTESTED ROW IS NOT EXEMPT. It routes to the seam first, but `loop/resolve.py::_contest` then
# folds the seam's result through `EFFECTS` (`_fold` raises `Unspecified` for a writing row with no
# entry there), so a contested writing row with no effect is the same silent exclusion
# `resolvable_verbs()` makes. The plan's text (`_part5` `30` WHERE 4a) exempts them on the premise
# that they take the seam path and not the effect path, and that premise is false: `fight` and
# `march` write and have effects, and `tell` writes nothing at any degree, so `not row.writes` skips
# it already. Dropping the exemption departs from the plan's text and refuses nothing on the
# shipped tree.
#
# ⚠ THE NOTES ARE READ OFF `VerbRow`, NOT RE-PARSED FROM THE FILE. At `30` this module parsed
# `verb_table.yaml` itself for `decline_note:`, because the loader ignored the column (its `*_note`
# rule) and `data/verbs.py` was then held by the telling workplan. That carve-out is absorbed into
# plan v9, which gives `data/verbs.py` to IN-41, so the two gate-read notes are `VerbRow` fields on
# `requires_typed_note`'s precedent, and a planted row is one `dataclasses.replace` away -- the
# table the refusal reads is the table the driver runs.
# ---------------------------------------------------------------------------


def check_effects(verb_table: dict, effects: dict) -> list:
    """Refusal (a), both arms: every WRITING verb row has an effect or an `effect_decline_note:`
    -- a contested row too -- and no row that has an effect, or writes nothing, carries one.

    Raises at the first arm broken (the missing note before the converse), naming every verb that
    breaks it. Returns the writing rows it checked."""
    checked, silent, stale = [], [], []
    for verb, row in verb_table.items():
        carried = row.effect_carried(effects)
        if row.effect_decline_note and carried:
            stale.append(verb)
        if not row.writes:
            continue
        checked.append(verb)
        if not carried and not row.effect_decline_note:
            silent.append(verb)
    if silent:
        raise Unspecified(
            f"writing verb row(s) {silent} have no effect and no `effect_decline_note:`",
            "04 §A.1 ID-13",
            needs="an `@effect_for` body for each, or an `effect_decline_note:` on its "
                  "verb_table.yaml row saying why it has none",
            law="A-25 / plan position `30` -- a verb the fold cannot execute leaves the game only "
                "by declaring why; before this it left without a word (`resolvable_verbs()`)")
    if stale:
        raise Unspecified(
            f"verb row(s) {stale} carry an `effect_decline_note:` and HAVE an effect, or write "
            f"nothing and need none",
            "04 §A.1 ID-13",
            needs="the note deleted (the effect exists, or the row writes nothing and so has no "
                  "effect to decline), or -- if it declines something else -- "
                  "moved to the column for that: `formation_decline_note:` (no Candidate forms) "
                  "or `requires_decline_note:` (nothing evaluates the precondition)",
            law="IN-41 / `SM-9` -- a declared absence the code contradicts is a declaration nobody "
                "can trust; refusal (a)'s converse arm")
    return checked


def check_preconditions(verb_table: dict, predicates: dict) -> list:
    """`SM-11`, refusal (a)'s PRECONDITION TWIN (plan position IN-41), both arms: every row whose
    precondition NOTHING EVALUATES -- no typed cell, no `predicates` entry -- carries a
    `requires_decline_note:` saying why, and no row whose precondition IS evaluable carries one.

    `resolvable_verbs()`'s first gate (`loop/driver.py`) drops the first kind from the game, and
    until IN-41 it did so WITHOUT A WORD. The answer to *evaluable* is `VerbRow.precondition_evaluable`,
    the one both sites read. `predicates` is `loop/predicates.py::REQUIRES_PREDICATES`, passed by the
    driver as `check_effects` is passed `EFFECTS`. Raises at the first arm broken (the missing note
    before the converse), naming every verb that breaks it; returns the rows that carry a
    precondition, so a caller can see the sweep was not empty."""
    checked, silent, stale = [], [], []
    for verb, row in verb_table.items():
        evaluable = row.precondition_evaluable(predicates)
        if evaluable and row.requires_decline_note:
            stale.append(verb)
        if not row.has_precondition:
            continue
        checked.append(verb)
        if not evaluable and not row.requires_decline_note:
            silent.append(verb)
    if silent:
        raise Unspecified(
            f"verb row(s) {silent} have a precondition nothing evaluates and no "
            "`requires_decline_note:`", "04 §A.1 ID-13",
            needs="a typed `requires_typed:` cell or a `REQUIRES_PREDICATES` entry for each, or a "
                  "`requires_decline_note:` on its verb_table.yaml row saying why it has neither",
            law="IN-41 / `SM-11` -- a verb the fold cannot evaluate leaves the game only by "
                "declaring why; before this `resolvable_verbs()` dropped it without a word")
    if stale:
        raise Unspecified(
            f"verb row(s) {stale} carry a `requires_decline_note:` and their precondition IS "
            "evaluable (no precondition, a typed cell, or a `REQUIRES_PREDICATES` entry)",
            "04 §A.1 ID-13",
            needs="the note deleted, since the fold can evaluate the precondition",
            law="IN-41 / `SM-11` -- a declared absence the code contradicts is a declaration nobody "
                "can trust; the converse arm, as refusal (a)'s")
    return checked
