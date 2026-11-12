# Census (REST) 2 — wiring: four cut wires this census closes itself, and the ledger of those other proposals carry

## Status: PROPOSED

Author: Fable census lane, PART=REST. Source: `audits/17_CENSUS_REST.md` §1a, §2, §5–§9. Read at
`4995824` (working tree). Ordered by risk, lowest first. Layer 1 grading follows
`skills/layer-conformance` Lens B against `architecture/meta/04_CODE_ARCHITECTURE.md`; each edit names
the row it sits under.

## What it changes in `engine/season/` at runtime

- **W1** (module-internal): nothing in the season loop today, because no host builds an `ally_at`
  order. It changes what `04_MB_manager_battle_one_resolver.md` §2 can author: an `ally_at:D` standing
  order fires instead of silently damming its queue.
- **W2** (loader): nothing while the two files agree; an `arrangements.yaml` whose `speech_kinds` ids
  drift from the roster stops at import instead of passing until a test is run.
- **W3** (WITNESS, told channel): after `14_VERBS_PHYSICAL_D_thread_read.md` stage 1, a claim of a
  thread-substrate term is not deposited in a hearer below the sensitivity gate. A declared mover of
  every pin in which a sensitive person tells such a claim; none exists at this tree (no such claim is
  ever minted).
- **W5** (CALENDAR): nothing until `15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md` lands;
  then the Date's condition is read before `date.fired`.

## W1 — `ally_at:D` has an ally (mass battle; new edit)

**Problem (verified).** `Order.waypoint_ref` (`modules/mass_battle/hierarchy/units.py:333`) is written by
nothing. `ally_at:` is an accepted trigger kind (`:309`, `:336`) with a range-checked payload (`:349`).
`core/contact.py:106-110` evaluates it only `if order.waypoint_ref is not None`, and `check_orders` stops
at the first unfired order (`contact.py:89-90`). So an `ally_at:` order is accepted at construction, never
fires, and blocks every order queued behind it for the whole battle: the failure `Order.__post_init__`'s
own comment says construction-time validation exists to prevent (`units.py:305-308`: "a typo should not
get that far"). No test constructs one.

**Needed by.** `04_MB_manager_battle_one_resolver.md` §2 lists `ally_at:D` in the standing-order grammar it
exports and validates. That grammar gives the trigger no operand for *which* ally; this edit supplies it
and that proposal's row syntax gains it.

**Resolution, decided.** The ally is named, by the subformation's name, on the order; the army builder
resolves the name to the sibling subunit; an order that needs an ally and has none is refused where it
is built.

```
# modules/mass_battle/hierarchy/units.py
@dataclass
class Order:
    trigger: str
    behavior: dict = field(default_factory=dict)
    ally: Optional[str] = None                 # NEW: a sibling subformation's name; required by,
                                               # and only lawful with, an 'ally_at:D' trigger
    waypoint_ref: Optional[object] = field(default=None, repr=False)   # resolved by build_army, never authored

    def __post_init__(self):
        ...existing checks...
        if self.trigger.startswith('ally_at:') != (self.ally is not None):
            raise ValueError("Order: 'ally_at:D' needs ally=<subformation name>, and no other trigger takes one")
```

- `modules/mass_battle/armies.py::build_army`: a subunit spec may carry `'name'` (popped before
  `Subunit.of_type`; `orderofbattle._spec_for` adds `spec['name'] = sf.name`, which `OrderOfBattle`
  already holds unique: "duplicate" is refused, `tests/valoria/test_mass_battle_order_of_battle.py:86`).
  After the loop that builds `subs`, one pass: for each subunit's orders with `ally`, set
  `order.waypoint_ref = subs[index_of[order.ally]]`; refuse (`ValueError`, naming the unit and the name)
  an `ally` that is no sibling's name or is the subunit's own.
- `modules/mass_battle/core/contact.py:108`: the `if order.waypoint_ref is not None:` guard becomes an
  unconditional read. A `None` there is now a build defect and raises `AttributeError` at the first
  check rather than waiting forever.
- `04_MB_manager_battle_one_resolver.md` §2's row form: `(trigger, behaviour)` becomes
  `(trigger, behaviour[, ally])`, and `armyrecord.py::order`'s validation (that proposal's edit) refuses
  the third element on any other trigger.

**Layer 1.** `holonic_ARCHITECTURE.md` §45 (a registered module takes typed input, returns typed
outcome, keeps no game state): the name is data on the module's own input record
(`OrderOfBattle`), resolved inside one `resolve_field` call; no state survives it. CONVENTION-grade
conformance; nothing STRUCTURAL is touched.

**Gate (execution artifact).** A new case in `tests/valoria/test_mass_battle_signals.py` (the file that
owns order triggers): two subunits `a`, `b` built 10 cells apart, `a` holding
`Order('ally_at:3', {'stance': 'aggressive'}, ally='b')`; `check_orders` leaves `a._order_idx == 0`
while the centroids are farther than 3, and advances it to 1 on the first check after `b` is moved
within 3. Three refusals: `Order('ally_at:3')` (no ally); `Order('tick:2', ally='b')`; `build_army`
with `ally='nobody'`. Run: that file.

**Falsifier.** Delete the resolution pass in `build_army`: the order never fires and the test's
`_order_idx == 1` fails (with the `contact.py` guard removed it fails louder, at the read). Control: the
same pair with `enemy_range:3` in place of `ally_at:3` does not fire on `b`'s approach.

**NERS.** N: a commander can tell a reserve to move when the line it supports comes near, which no
other trigger expresses (`tick:` is blind, `signal:` needs a caller). R: a plan that reacts to one's own
side. S: same grammar, same queue, one operand. E, last: one field, one resolution pass, one guard
removed.

**Cost class.** Edit.

## W2 — the arrangements loader holds `speech_kinds` to its roster (new edit)

**Problem (verified).** `arrangements.yaml:62` says its six `speech_kinds` ids reuse
`rosters.yaml: ladder_rungs`. `data/arrangements.py` refuses an unknown genre, reachable band, interposed
kind and proof (`:140`, `:146`, `:189`, `:194`) and a duplicate id (`:241`); it does not hold the ids to
the roster. The equality is asserted in a test (`tests/test_arrangements.py:89`,
`set(A.SPEECH_KINDS) == set(LADDER_RUNGS)`), and `LADDER_RUNGS` (`data/rosters.py:868`) has no reader in
game code. A closed set whose only enforcement is a test is the shape CLAUDE.md §0.05 names: the
licensed place is "the loader's refusal per data family".

**Resolution, decided.** In `data/arrangements.py::_load`, after the `speech_kinds` rows are read:

```
if set(speech_kinds) != set(LADDER_RUNGS):
    raise SystemExit("arrangements.yaml: speech_kinds ids and rosters.yaml: ladder_rungs disagree — "
                     f"only in speech_kinds: {sorted(set(speech_kinds) - set(LADDER_RUNGS))}; "
                     f"only in the roster: {sorted(set(LADDER_RUNGS) - set(speech_kinds))}")
```

`LADDER_RUNGS` joins the import at `data/arrangements.py:47`. `tests/test_arrangements.py:87-89` then
asserts the refusal (a mutated copy of the document raises) instead of restating the equality, and
`tests/test_stress_proceedings_rehost.py:141`'s `len(LADDER_RUNGS) == 6` stays.

**Interaction.** `05_SC_playable_hearing_B.md` corrects the roster's note (its edit list, `:152`)
(`audits/05_SC_audit_addendum_B.md` G-46: the six are the concession ladder; the issue ladder gets its
own roster). The refusal is written against the roster as that edit leaves it; if the six ids move to a
renamed roster, this line follows the name.

**Layer 1.** `04` §A.2 `data/loaders` row: "the in-memory forms; the cross-validation invariants
(§B.13)". A cross-file invariant belongs there. Conformant.

**Gate.** `engine/season/tests/test_arrangements.py`. **Falsifier.** Add a seventh id to a copy of
`arrangements.yaml: speech_kinds` and load it: `SystemExit` naming the id; before the edit the load
succeeds.

**Cost class.** Edit.

## W3 — `knowledge_kinds` gets its reader at the one place knowledge changes hands (new edit, after `14_VERBS_PHYSICAL_D` stage 1)

**Problem (verified).** `rosters.yaml: knowledge_kinds` (`:1763-1777`; values `mundane`,
`thread_substrate`) is named by no code and says so itself. H-85's `default:` is "a two-valued
knowledge-kind roster … with Thread Sensitivity gating only the second". The verb half is built (K-3:
`thread_read`'s typed cell over `Person.thread_sensitivity`). The knowledge half is not: nothing is
classed, so the roster's two values distinguish nothing. `12_ARCS_adjudication.md` row 19 answers three
case needs (NPC-086 N3, NPC-087 N2, NPC-088 N6) with "ordinary; `rosters.yaml: knowledge_kinds` is the
owner and the gate applies to the kinds it names", marked unverified; verified here, the roster names
kinds and applies to nothing.

**Why not delete it.** The three cases turn on the difference: their material must be retainable by
ordinary minds *as opposed to* knowledge that is not. A world in which a sensitive reader can tell
anyone what he read in the Thread has no such difference, and after `14_VERBS_PHYSICAL_D` stage 1 that
is what the loop does: a successful `thread_read` deposits an observation claim (the subject's
sensitivity; at stage 2 his `knot`/`tie` edges and Coherence band), and `tell` copies any held claim to
any hearer (`loop/witness.py`, the told channel, `Claim(… _held.subject, _held.predicate, …,
"told_by", …)`). Ladder: step 3 (H-85's own default); nothing for Jordan.

**Resolution, decided.** The kind is a property of *what a claim is about*, carried by the claim's
`predicate`, so no carrier field is added (`state/carriers.py::Claim`'s docstring: `round` is the only
field U2 may add).

1. **Owner.** `rosters.yaml: knowledge_kinds` gains a mapping beside `values:`

   ```
   knowledge_kinds:
     values: [mundane, thread_substrate]
     predicates:                       # a predicate absent from every list is `mundane`
       thread_substrate: [<the observation terms `thread_read`'s `observes:` cell deposits>]
   ```

   The list is exactly the terms `14_VERBS_PHYSICAL_D_thread_read.md` writes in `thread_read`'s
   `observes:` column (stage 1: the sensitivity term; stage 2 adds the edge and Coherence terms). One
   owner; that proposal's column and this list are cross-checked at import (below).
2. **Loader** (`data/rosters.py`): `KNOWLEDGE_KIND_OF = _load_knowledge_kinds(roster_map("knowledge_kinds",
   "predicates"), roster("knowledge_kinds"), OBSERVATION_TERMS)`: a `{predicate: kind}` map; refuses a
   kind outside `values`, a predicate under two kinds, and a predicate that is not an
   `observation_terms` member. `data/verbs.py` refuses, at import, a `thread_read` `observes:` term
   that the roster does not class `thread_substrate` (the two files cannot drift).
3. **Reader** (`queries/person_q.py`, pure, no token: `04` §A.2 `queries/person_q` row):

   ```
   def retainable(hearer_sensitivity: Optional[int], gate: int, predicate: str) -> bool:
       """May a mind of this sensitivity hold a claim of this predicate? `mundane`: always.
       `thread_substrate`: only at or above the gate (H-85, H-239)."""
       return KNOWLEDGE_KIND_OF.get(predicate, "mundane") == "mundane" or (
           hearer_sensitivity is not None and hearer_sensitivity >= gate)
   ```

4. **The gate, at one site.** `loop/witness.py`, told channel, immediately before the `tc = Claim(…)`
   construction: `if not person_q.retainable(p.thread_sensitivity,
   w.fixtures.get("thread_sensitivity_gate"), _held.predicate): continue`. The hearer still receives the
   event-kind claim `(subject, "news.told", True)`: he knows he was told something; he does not hold
   it. No new Event kind, no new write class (the deposit that does not happen is WITNESS's own).
5. **What is not gated.** First-hand deposits: the reader's own finding passes the verb's gate already.
   Documents: a `Record` whose content is a thread-substrate claim is `14_VERBS_MATERIAL_E_knowledge.md`'s
   subject `[UNVERIFIED: not opened for this rule]`; if a non-sensitive reader can take the claim from
   paper, the same `retainable` call belongs at that deposit, and that proposal names it.

**Layer 1.** `04` §A.2: `loop/witness` owns `(Person, claim_ledger)`; `queries/person_q` writes nothing
and takes no token; `data/loaders` owns cross-validation. All three edits sit in their rows.
`holonic_ARCHITECTURE.md` is not touched. Conformant.

**Gate (execution artifact).** A test beside `engine/season/tests/test_k3_thread_sensitivity.py`, on a
hand-built world through the real fold: a sensitive teller holding one thread-substrate claim and one
mundane claim tells both to (a) a hearer below the gate and (b) a hearer at it. Asserted: (a) gains a
`told_by` claim for the mundane predicate and none for the thread-substrate one, and gains `news.told`
for both tellings; (b) gains both. `assert checked == 4` (four hearer-claim pairs).

**Falsifier.** Empty `predicates.thread_substrate` in a copy of the roster: (a) gains both and the test
fails. Control: the mundane claim in the same run, same hearer.

**NERS.** N: the setting's one class-shaped gate reaches knowledge as well as action; without it a
single sensitive informant dissolves the barrier for a realm in one season of `tell`. R, the half with
no player: what a faction can know about the Thread depends on whom it has, which is a recruiting
motive nobody scripts. S: one comparison, the same `thread_sensitivity_gate` fixture the verb reads; one
ladder for one quantity. E, last: one mapping, one pure reader, one line at one deposit.

**Cost class.** Small build. Lands after `14_VERBS_PHYSICAL_D` stage 1 (before it there is no
thread-substrate claim and the gate is unobservable).

## W5 — the convening condition is read, or its key goes (carried, with the fallback stated)

**Problem (verified).** `_eff_convene` writes `date["convening_attached"] = True`
(`loop/effects_governance.py:457`) through the `(ConveningCondition, attached)` cell, 17 times in the
three-season realm run. Nothing reads the key, tests included; `loop/calendar.py` fires a due Date
unconditionally. `04` §A.2's `loop/calendar` row names `ConveningCondition` among what CALENDAR owns, so
the cell is Layer 1's and stays.

**Resolution.** The condition a sitting must meet is `15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md`'s
`quorum_share:` (or today's integer `quorum:`), read from the arrangement row the convening names. When
that proposal lands: `_eff_convene` writes the row's condition under the key in place of `True`, and
CALENDAR tests it against the bench present before `date.fired`; a Date whose condition fails emits
nothing and stays due. If Papacy B is not adopted, the fallback is deletion of the *key* (the write of a
constant), leaving the matrix row declared and unwritten like `(Rung, envelope)`. No edit is made here.

## Carried by other proposals (no edit here; listed so the wire is not counted twice)

| cut wire (audit row) | carrier |
|---|---|
| `Unit.officers` read at resolution (§1a) | `04_MB_manager_battle_one_resolver.md` §7 |
| threadwork outcome fields: `just_transitioned`, `net_successes`, `CollectiveResult` ×4, `OpposingResult` ×4 (§1d) | `09_WR_threadwork_module.md`; rule added: a field the host adapter does not read at landing is cut in that commit |
| `scar.taken`, `conviction.moved` at their writers (§5a) | `11_GO_player_surface_contract.md` §4 with `02_CHAR_scar_is_a_wound.md`; wording corrected in `17_CENSUS_REST_3_corrections.md` C-5 |
| `weight.changed` (§5a) | `07_SE_population_census.md` |
| `(Person, coherence)` and `coherence.changed` (§5a) | `09_WR_threadwork_module.md`; `14_VERBS_PHYSICAL_D_thread_read.md` stage 2 |
| 39 consumers waiting on kinds that did not occur (§5 class B) | the verb build-outs, `14_VERBS_*` |
| 34 verbs that execute in neither instrument (§6) | `14_VERBS_*` by stratum; `08_FI_08_knots-season-form.md` for `tie / knot` |
| `MassBattleInput.loyalties` × `loyalty_gain`, 0 by construction twice (§7 X-R4) | `04_MB_typed_outcome_and_one_path.md`; CR-88 |
| the character sheet's five spaces, called only by tests (§9 X-T1) | `11_GO_player_surface_contract_B.md`; `01_CORE_one_scene_contract.md` |
| `signal:` orders and `fired_signals` (§9 X-T6) | `04_MB_manager_battle_one_resolver.md` §2 (`fire_signal`) |

## Order

W1 and W2 are independent of everything and can land first. W3 after `14_VERBS_PHYSICAL_D` stage 1. W5
with Papacy B. No cycle: none of the four depends on another.
