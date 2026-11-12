# WR · Threadwork: the session on the input, three registered entries, a cost rule by direction, a practitioner who cannot read himself, and the Warden's season

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-15) — where this file names `PersonProjection` as a present reader (the practitioner who cannot read himself), read `account` (`11_GO_player_surface_contract_B.md` §4): the projection is deleted by `17_CENSUS_C1A_01_deletion_batches.md` D2. The property claimed (no Coherence value reachable by the person) is unchanged and is stated of `account`.

Reconciled: 2026-11-12, U5d closure — folded **A-43**, **A-40**, **A-11** and **A-5**. Edit 3 (R-25: `coherence` is world-only for its owner, not an `OWN_STATE_STEMS` member) stands and is joined by its other half, what **others** read of him: `U5d_WR_zero_coherence_unknowable.md` (legibility as the one dial; at zero he keeps seats and goals and cannot be understood). The sentence offering Jordan a visible band for the player's own person is not answered by A-43 (which speaks of what others can know of him) and stays as written. The breach and the strain draws are on the one sampler (A-5); Thread Sensitivity stays the one gate (A-11); a working's subject is a Site (A-40).

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §1 Option A / 7b-10: `WorkingInput.draw: object` becomes `draws: tuple` of pre-drawn integers, so the module's input is a plain record (`holonic` §45 typed records; the `modules/settlements` precedent); R3 §2 (A-5, A-6, A-7): the strain draw's single-input pool and obstacle are marked `[ASSUMPTION: single input pending U5a]` and pointed at the capability architecture's `thread` site row; the body follows the U5a head (edit 3 point 3 and the falsifier read `account`, not `PersonProjection`); tier and batch added (R3 7b-0; U3 B35). U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "typed record" → "dataclass" (glossary *record*); "Ob" → "obstacle" in prose (glossary *obstacle*).

## Status: PROPOSED

Lands in batch: B35 (WR thread), first in U3 §1 item 35.
Depends on: `09_WR_threadwork_module.md` edit 3 (B03, the typed parameter file and `thread_operations`); `17_CENSUS_C1B_01_deletions` (B03); `17_CENSUS_C1A_01` D2 (B03, `account` replaces the projection); B10-15's rows and CP-T07-02's host (plan positions; MISSING until STAGES.md step 5 carries them) for edit 4's play.

Carries findings F-WR-17 and F-WR-18 of `audits/09_WR_audit_addendum_B.md` (§4.2, §4.3), its resolutions
R-21, R-22, R-25 and R-34, its §2.2 correction 9 and its §4.5. **Supersedes edits 1, 2 and 4 of the first
lane's `09_WR_threadwork_module.md`; its edit 3 (the operation tables as typed data under
`engine/engine_params/`, behind `tools/export_engine_params.py --check`; the `thread_operations` roster)
stands and is assumed below.** Its problem statement (Layer 1, the registered-module contract, one code
path, the settlements and fieldwork precedent) stands too and is not repeated.

## What it changes in `engine/season/` at runtime

**Nothing by itself**, as the first lane's: the loop first calls a thread entry when B10-15's CP-T07-02
builds its host (`seam/wrappers/threadwork.py`). Edit 3's refusals bind that host when it lands. Edit 4
adds one overlay case to `harness/exercises.py`, which the loop does not import. Hash EQUAL.

## The problem

1. **The designed game inside a working has no code and no plan position (F-WR-17).** The design set
   (`.designs/systems/threadwork/reference/threadwork_v30.md` and its infill, intent only) gives the
   practitioner a contact window bounded by Thread Fatigue and by Focus, each further operation in one
   window harder (overweaving), concealment before the Leap, and the choice to stop. The oracle resolves one
   operation per call and none takes a count of prior operations or a fatigue
   (`systems/threadwork/sim/operations.py:351-512`; EB-05: the grep finds no session term). The first lane's
   `WorkingInput` (`operation, actor, depth, breadth, distance, target_kind, in_equilibrium, draw`) carries
   the operation, not the session. B10-15 schedules five verb rows and a host, no session. Without the
   session on the input, a played working (the manual mode) needs a second resolver, which the standing
   requirement forbids.
2. **The first lane's composition row cannot refuse its own deletion, and names one entry of three (R-21).**
   `references/module_contracts.yaml:43-50`: a `step_call` row is checked either through a role roster's
   `module_entry:` (`inquiry_modules`, `manifest/registry.py::check_inquiry_modules`, `:410`) or through a
   host tuple passed to `manifest/registrar.py::require_entries` (`:132`; `loop/matter.py:47`,
   `STEP_CALLS`; `loop/driver.py:294`). The proposal declared neither. The plan's own homes name two more
   entries: `threadwork.read` (CP-T07-10, through an `inquiry_modules` row) and IN-06's
   `threadwork.coherence_band` `query` row (which "lands only with a consumer", CP-T07-07).
3. **Cost is keyed on the verb, with Mending as a special case (R-22).** `operations.py:451`,
   `MENDING_COHERENCE_COST = 0`. The applications document's first rule (intent) is that *direction*
   (restorative, manipulative, destructive) decides whether there is a cost.
4. **The first lane's scenario shows the practitioner his own Coherence band (F-WR-18).** The design forbids
   it in terms (`threadwork_applications_part2.md` §10: "A Coherence meter its owner can read — the mechanic
   and its display contradict"; §1.4: "They cannot judge it themselves"); AX-7 points the same way (a person
   has a reading of the world, never the world). And the precedent a builder will reach for when
   `Person.coherence` lands is `data/requires.py:809`, `OWN_STATE_STEMS`, through which a person reads his
   own `thread_sensitivity` (`queries/world_q.py:4686-4695`): following it builds the forbidden meter.
   R7's table is a null on this point: every shipped game it lists shows its power-cost meter; the nearest
   shape is Darkest Dungeon II's companions voicing stress bands (addendum §2.4).

## The resolution, decided

- **The session is two integers on the input and one on the outcome.** The season's one fold is a session
  of length one (`prior_ops = 0`, `fatigue = 0`); a played working is the same entry folded again with
  the count and the fatigue it returned. Fatigue lives for one contact and is the host's to pass; no state
  is added to `Person`.
- **Three entries, each declared where its kind is checked (R-21).** `threadwork.work` by a host tuple
  (MATTER's precedent; no role roster, because the thread verbs carry no per-verb module variation);
  `threadwork.read` by an `inquiry_modules` row for kind `thread.read` (fieldwork's precedent: several
  inquiry kinds, one entry); `threadwork.coherence_band` as a `query` row, written only in the commit that
  lands its consumer.
- **One cost rule over a `direction` column (R-22).** ED-871's value (Mending costs nothing) becomes a row,
  the special case goes. The applications document's "restorative work moves the practitioner toward
  equilibrium" is not adopted as a number: it is `coherence.recover()`'s `mending=` term, already built,
  and its value is Jordan's.
- **A Partial's scope is the next-lower breadth (R-34)**, one row of the parameter file, replacing the
  design's "the engine sets scope" (a GM leaning).
- **Coherence is world-only for its owner (R-25).** He learns it from what it takes from him (a season with
  fewer scenes, CP-T07-07), from what a sensitive companion `tell`s him (CP-T07-10's second finding,
  deposited in his own ledger), and from how others treat him (`deeds_judged`, regard). Characterful by
  construction: the practitioner with a trusted, sensitive companion knows where he stands, the one who
  works alone does not. If Jordan wants the player's own person to see a band, `_part2` §10 is the line to
  overrule; named, not escalated (ladder step 3).

## The edits

### Edit 1 · the session on the dataclasses (`engine/season/queries/inputs.py`; replaces the first lane's edit 1)

The first lane's `Practitioner` stands unchanged. `WorkingInput` and `WorkingOutcome` become:

```python
class WorkingInput(NamedTuple):
    operation: str                    # a `rosters.yaml: thread_operations` member
    actor: Practitioner
    depth: str; breadth: str; distance: str
    target_kind: str                  # "site" | "person"   ("self" only for `mend`, CP-T07-04)
    in_equilibrium: bool              # CP-T07-05's read, projected by the host
    prior_ops: int                    # operations already made in this contact; 0 for the season's fold
    fatigue: int                      # Thread Fatigue accrued in this contact; 0 for the season's fold
    draws: tuple                      # integers the host pre-drew with `ids.draw_factory`, keyed
                                      # (seed, tick, actor, "thread", prior_ops); the module indexes them, never mints

class WorkingOutcome(NamedTuple):
    degree: str                       # the shared ladder's band, or "refused"
    refusal: str                      # "" | "window_closed"   (typed, never a raise; eligibility only)
    contact_lost: bool                # the strain draw (below) broke contact; graded, not a threshold
    coherence_delta: int
    resting_point_delta: int
    strain: int                       # what the target's fabric loses; 0 until H-236's source is ruled
    fatigue: int                      # fatigue after this operation; the host passes it back in
    observed: tuple                   # what a witness would read (CP-T07-09)
```

The parameter file of the first lane's edit 3 gains four rows: `overweave_step` (obstacle added per prior
operation), `fatigue_scale_per_will` (the fatigue at which strain starts to bite, as a multiple of
`actor.spirit`), `ops_per_contact` as `focus - k` with `k` a row, and `partial_breadth: next_lower` (R-34);
the operation table gains a `fatigue_cost` column. Values: the design set's (×5, Focus − 1, +1 obstacle),
`[ASSUMPTION; medium; Jordan to correct]`, carried as data and read nowhere else.

**No threshold decides an outcome (the brief's standing rule, "we do not do deterministic").** The
Focus cap (`ops_per_contact`) is an eligibility check (whether a further operation may be *attempted*)
and is the only refusal. Fatigue never closes the window by itself: each operation made with `fatigue`
above zero is followed by a **strain draw** on the shared ladder (`dice_engine.degree_from_net`, the one
owner), whose obstacle is the operation's own plus `fatigue / (fatigue_scale_per_will × spirit)`, rounded,
and whose pool is the practitioner's will `[ASSUMPTION: single input pending U5a — A-7 rules two inputs and
A-6 a score plus base, floor five; the capability architecture's `thread` site row
(`U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §3) reads Focus as an `edge` and Will as the `resource` that
scales fatigue, so this pool and obstacle are re-expressed on that form when CAP lands, `[CALIBRATE]` in
the joint calibration, OWED §B]`. Overwhelming or Success: contact holds. Partial: contact holds and the
operation's Coherence cost rises one band. Failure: `contact_lost` is true, the operation's effect still
lands at its own degree, and the host ends the contact. State sets the odds; the draw sets whether he can
go on. The host pre-draws the integers the call needs (the operation's roll and the strain roll) under
keys that include `prior_ops`, and passes them in `draws`, so a seed replays it and the module holds no
draw handle (R3 §1, Option A: a plain record; the module never mints).

### Edit 2 · three entries, one cost rule (`modules/threadwork/`, `references/module_contracts.yaml`, `seam/wrappers/threadwork.py`, `rosters.yaml`; replaces the first lane's edit 2)

The first lane's move stands (`systems/threadwork/sim/` to `modules/threadwork/`; module stores deleted;
`rendering.py` deleted with a `FORK:` row). Its entry list becomes three:

```yaml
  threadwork.work:
    target: "modules.threadwork.working:work"
    entry: step_call
    needed_by: "engine/season/seam/wrappers/threadwork.py — the host (CP-T07-02) builds `WorkingInput` and calls this
      entry inside RESOLVE's fold; a played working folds it again with `prior_ops` and `fatigue`. No role roster names
      this row, so the host declares the need (`seam/wrappers/threadwork.py::STEP_CALLS`) and
      `manifest/registrar.py::require_entries` refuses at driver construction its absence, or an `entry:` other than
      `step_call`."
  threadwork.read:
    target: "modules.threadwork.reading:read"
    entry: step_call
    needed_by: "the `inquiry` role, kind `thread.read` (`rosters.yaml: inquiry_modules`, CP-T07-10);
      `manifest/registry.py::check_inquiry_modules` refuses a row whose `module_entry:` no composition row declares."
```

`threadwork.coherence_band` (`entry: query`) is **not** added here; it is added in the commit that lands
CP-T07-07's consumer (ID-13: "a role no caller requires is not declared"). `loop/driver.py:294`'s
`require_entries(world_q.QUERY_ENTRIES + MATTER_STEP_CALLS)` gains the wrapper's `STEP_CALLS` as a third
term. (The field adapter's need reaches the same call folded into `QUERY_ENTRIES` as `PROVISION`,
`registrar.py:137-140`; a separate term is chosen here because a thread working is a step, not a query.)

Cost: `working.py` computes a working's Coherence cost as `cost_table[scale] * DIRECTION_WEIGHT[direction]`,
**then modulated by the working's drawn degree** exactly as the oracle already does
(`operations.py:312-334`: the Partial and Failure penalty, Failure one step worse than Partial), with the
degree modulation moved to rows of the parameter file. `direction` is the operation row's new column
(`restorative | manipulative | destructive`) and the weights are three rows (`restorative: 0` carries
ED-871, at every degree, which is the oracle's present Mending exemption expressed as data).
`MENDING_COHERENCE_COST` and every `if operation == "mend"` branch on cost are deleted. A cost that did not
depend on the draw would make the price of power a fixed function of the choice; it must not. The parity
gate is the first lane's: the four oracle test files keep their expected numbers.

**The crossing (CP-T07-08, B10-15's) is listed for its owner, not built here.** As scheduled it is a
threshold: the breach fires when displacement passes the human band. Under the standing rule it becomes a
draw made whenever a working leaves the displacement past the band: odds from how far past (state), outcome
graded (Success: holds, Partial: the resting point moves one step, the oracle's plastic set; Failure: the
breach Event). The practitioner who works deep past his band will usually break, and sometimes will not.

### Edit 3 · the practitioner cannot read himself (`data/requires.py`, `verb_table.yaml`, the host)

1. `OWN_STATE_STEMS` (`data/requires.py:809`) does **not** gain `coherence` or any band of it. A comment on
   the roster says why, citing R-25, so the omission is not "fixed" by the next reader.
2. `thread_read` does not form on its own actor: its row's typed requirement gains a not-self conjunct on
   `subject`; if the cell grammar has no such form, a one-line `_req_thread_read` predicate in
   `loop/predicates.py`, on `_req_confer`'s shape. (CP-T07-04 lets him `mend` himself; reading himself is the
   faculty judging itself.)
3. The host passes `resting_point` and `displacement` to the module in `Practitioner` and to nothing else:
   not to `choose`, not to `play_surface`'s callback (which receives `(p, v, s, ask_budget, auto)`), and not
   into `account` (the person's own ledger, `11_GO_player_surface_contract_B.md`; `PersonProjection`,
   `world_q.py:4409-4431` on `main`, is deleted by `17_CENSUS_C1A_01` D2).

### Edit 4 · the Warden's season (`engine/season/harness/exercises.py`, one overlay case; replaces the first lane's edit 4)

A hand-built world of one settlement at breadth-first distance 1 from the wound (the first lane's
`09_WR_world_motion.md` edit 1): three Sites (one below its floor, one above, one dwelling); a practitioner
at sensitivity 60; an apprentice at 35 (can read, can barely work); a steward who governs the larder the
failing Site feeds; a witness whose affiliations are `incompatible` with the practitioner's. Run through
`SeasonDriver.season`, with `play_surface.dispatching_chooser` binding the practitioner.

| element | what the case states |
|---|---|
| choices, season scale | `thread_read`, `mend`, `weave`, `lock`, `ward` (B10-15), `restore`, `conceal`, rest at a place in equilibrium |
| choices, inside a working | continue (fold again with `prior_ops + 1` and the returned `fatigue`) or stop; refused with `window_closed` past the Focus cap; contact broken when the strain draw fails, which is likelier the more fatigue he carries |
| stakes | the Site's uses and the larder; the practitioner's headroom (never shown to him); exposure to the witness |
| legibility | each working's degree and what it wrote; the witness's deposited claim; what the apprentice can `tell` him |
| end | each reached by a drawn outcome, never by a number crossing: the Site restored (by drawn `restore`/`mend` workings) and holding two seasons; or the breach Event (the drawn crossing above, CP-T07-08); or the Site's last use closed (by the drawn wear of `09_WR_B_draws_not_thresholds.md`); or his detention (a drawn `arrest` on the witness's petition). Stated by the overlay; no ending carrier is added |
| instrument | `aperture` on the fixture; `chronicle --focus <the apprentice>` (`09_WR_B_chronicle_that_tells.md`) |

Until B10-15 lands the rows and CP-T07-02 the host, the case cannot be played; it is written so the
landing has a target, and it supplies no second chooser.

## The gate that shows it worked

```sh
python -m pytest tests/valoria/test_threadwork_resilience.py tests/valoria/test_threadwork_mending_parity.py \
       tests/valoria/test_coherence_elastic_plastic.py engine/tests/test_thread_mending_ed871.py -q
python -m pytest tests/valoria/test_engine_does_not_import_systems.py -q
python tools/export_engine_params.py --check
```

Passes when: the four oracle files are green on unchanged expected numbers with `prior_ops = 0, fatigue = 0`
(the session of length one is today's arithmetic); a planted pair of calls differing only in `prior_ops`
returns obstacles differing by `overweave_step`; a call with `fatigue` at the threshold returns
`contact_lost` on some seeds and not others (over 200 draws minted under distinct keys, otherwise equal input, fatigue above zero,
both values occur; at fatigue zero, no strain draw is made); a call past `ops_per_contact` returns
`refusal == "window_closed"` and writes nothing on the host side; a driver built with the composition row deleted
refuses at construction; `thread_read` with `subject == actor` is refused; and the round trip is clean.

## The falsifier

A `WorkingInput` field or parameter row that changes nothing when varied (`prior_ops` not read); a
consequential outcome (contact held or lost, the Coherence cost, the breach) that is the same for every
draw at a given state; a
Coherence value reachable from `choose`'s arguments, the callback's, or `account`; a `draws` tuple too
short for the call (the module minting a draw of its own); a `mend`
whose cost is non-zero with `restorative: 0`; a second resolver anywhere for the played working.

## NERS reading

- **N.** Without the session, threadwork can only ever be one roll, and the push-your-luck axiom the
  tradition expects of costly magic (Darkest Dungeon's stress, Sunless Sea's terror, R7) is absent.
  Without the declarations, deleting the row is silent. Holds vertically (season fold and played session on
  one entry), laterally (fieldwork's and MATTER's declarations) and from the player's direction (a choice
  inside the working).
- **R.** The hidden meter makes companions matter: a sensitive friend is information. Completeness: the
  Focus cap and the strain draw are the extremes, typed and tested; a deep working can succeed against the
  odds and a shallow one can break contact, which is the standing rule's "a good position still loses
  sometimes".
- **S.** One entry for both modes, pausing where a played fight does (ENCOUNTER's `host`); one cost rule;
  every value in the parameter file.
- **E, last.** Two input integers, one outcome integer, one column, two refusals and one overlay case,
  against a whole designed mode of play. High.

## Cost class

Edits 1, 2: small build (on the first lane's move). Edit 3: edit. Edit 4: design-first on B10-15's rows
before it can be played. Tier: edits 1–2 `opus` (the session shape and the entry declarations), edits 3–4
`sonnet` (R3 7b-0). The `[ASSUMPTION]` values (overweave, fatigue scale, Focus cap) stay INCOMPLETE as
content until CAP and the joint calibration land.
