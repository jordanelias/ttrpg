"""`season.loop.effects` — the resolver's BODY. One effect per verb that writes.

EXTRACTED, step 5 of the decomposition (a PURE MOVE). `EFFECTS`, its decorator, the ONE operand
reader (`_operand`) and the eleven `_eff_*` (ten until `release`, 2026-09-11) move together and
must: §8's *"THE OWNER OF THE RULE, AND
THREE EFFECTS HAD THEIR OWN COPY"* is about `_operand` specifically, and the decorator-filled
table has to be defined where the decorated functions are or it is empty when the fold reads it.

WHAT THIS MODULE IS AGAINST, which is the reason it exists at all (§27.2). The fold once took an
`effect` parameter — a CALLER-SUPPLIED LAMBDA that inspected `a.verb` and returned Events, and
every probe wrote its own. That is a resolver per caller, each free to disagree about what a verb
does. A verb-keyed effect registered here is one implementation for every caller, and a verb with
a `writes:` column and no effect REFUSES rather than silently writing nothing. Register row H-63.

⚠ NOTHING HERE TAKES A WRITE TOKEN, AND NO EFFECT CALLS `w.write`. The first version of this
docstring said every effect writes THROUGH `w.write(...)`, which is the exact inversion the old
`_eff_confer` docstring refuted -- *"AN EFFECT MUTATES AND RETURNS THE IDS IT TOUCHED; IT DOES NOT
CALL `w.write` … My first version did both, and the fold correctly refused."* Caught by a
read-only critic, and it is §47's failure exactly: a false claim of enforcement stops the next
reader checking.

⚠⚠ G4 (plan position 7): THE CONTRACT EVERY EFFECT HERE IS WRITTEN TO, AND IT CHANGED. An effect
no longer MUTATES and REPORTS; it DESCRIBES. It reads the world as its predecessors left it and
returns a `state/gate.py::Change` -- the SUBJECTS it will write, named BEFORE anything moves, and
the write (`apply`), which still goes through the store's own methods (`add_tenure`,
`remove_person`, `_grant_remit`), because those are the one owners of their rules. The fold hands
the `Change` to `World.write`, which reads every subject, applies, reads again, and mints a receipt
for each subject that MOVED and for no other; if none moved it raises `NoOpReceipt` and the fold
emits the row's refusal (`04 §C.2`, F9). So an effect says what it will write and THE GATE says
whether it did -- the bookkeeping several effects carried to avoid claiming a write that did not
happen (`establish`'s `moved`, `_grant_remit`'s return value read as an `earned` filter) is the
gate's now, once.

WHAT EACH EFFECT NAMES IS A DECISION, and each docstring below states its own. Two rules hold for
all twelve, and both exist to keep every hash that is not `work`'s where it was:

  1. AN EFFECT NAMES THE IDS IT USED TO REPORT, IN THE ORDER IT REPORTED THEM -- and where it
     used to decide by hand WHETHER to report one (`establish`'s office), it names it always and
     the gate decides. So the receipts a success Event carries are exactly the ones it carried,
     and `content_hash` folds each receipt. Naming MORE
     (`move`'s legs, `create_record`'s `hold`, `kill`'s cascade) would add receipts to Events that
     have always carried fewer and move hashes no no-op refusal explains. The unnamed Tenures are
     still SEEN -- F3 judges every Tenure written, and a no-op refusal puts them back.
  2. DECLINING IS `NO_CHANGE`. An effect that decides not to write (`transfer` to a non-rung, a
     `move` up no ladder, an `utter` over an existing Proposition) returns it, and the gate's
     `NoOpReceipt` is the refusal -- the same channel as an effect that ran and moved nothing.

THE SPLIT (PHASE 4 of the decomposition, per the repo owner's settled requirement that each
subsystem be its own module -- per-subsystem files, human-readable, self-contained, the shape
`queries/` already had): this file's body divided into six sibling modules in `loop/`, flat --
no package, no `__init__.py` barrel:

  * `effects_shared.py`      -- `effect_for`, `_operand`, and the handful of helpers three or
                                 more domain files' effects share.
  * `effects_governance.py`  -- office/seat lifecycle: confer, establish, release, revoke,
                                 convene, oblige, levy.
  * `effects_economy.py`     -- labour, repair, material transfer: work, restore, transfer.
  * `effects_migration.py`   -- travel and settlement: move, migrate.
  * `effects_founding.py`    -- minting works: found, build.
  * `effects_information.py` -- records, propositions, matters: create_record, issue, open_case,
                                 determine, petition, survey, give, destroy_record, utter, commit.
  * `effects_combat.py`      -- casualties and morale: fight (renamed from "kill / wound"), march.

⚠ THIS FILE IS THE REASONED EXCEPTION TO `queries/__init__.py`'s "THIS FILE IMPORTS NONE OF ITS
SUBMODULES" CONVENTION, NOT A SILENT COPY OF A PATTERN THAT DOES NOT FIT HERE. `queries/`'s reason
holds where every submodule is reached by its OWN name (`world_q.ceiling`, `faction_q.resolve`):
nothing there needs the package eagerly loaded, so it is not. `EFFECTS` is different in kind: it is
ONE FLAT DICT every domain module's `@effect_for(...)` decorators populate BY SIDE EFFECT at import
time, and it is incomplete -- missing whichever verbs belong to whichever domain modules have not
yet run -- until every one of the six has been imported at least once. Several call sites reach it,
and a handful of the private names above, BY IDENTITY off this module's own dotted path rather than
off their owning domain file: `EFFECTS` from `loop/resolve.py`, `loop/driver.py` and
`harness/probes.py`, plus `test_information_cluster.py`, `test_record_kind_fold.py` and
`test_march.py`; the `effects` module itself (for `.EFFECTS`, `._eff_kill`, `._renewals` or
`._oblige_term`) from `test_term_upkeep.py`, `test_obligees.py`, `test_governance_build.py` and
`test_g4_no_op_receipt.py`. A caller reaching `engine.season.loop.effects.EFFECTS` before every
domain module has run would see a table with holes in it -- so this file imports every submodule
below for the decorator side effect alone, and re-exports the names those callers reach by dotted
path rather than by `from .effects_domain import name`.
"""

from __future__ import annotations

from .effects_shared import EFFECTS, _oblige_term, _operand, effect_for

# EAGER, DELIBERATELY -- see the docstring above: `EFFECTS` is incomplete until every domain
# module below has run its `@effect_for(...)` decorators at least once. Six imports, one per
# domain file (the order matches the list above), each for the decorator side effect only.
from . import effects_governance
from . import effects_economy
from . import effects_migration
from . import effects_founding
from . import effects_information
from . import effects_combat

# Re-exported because reached BY IDENTITY, off THIS module's own dotted path, from outside this
# file (see the docstring above for the call sites) -- not a re-implementation: each name below
# is the same object its owning domain file defines.
from .effects_combat import _eff_kill, _scar
from .effects_economy import _renewals
