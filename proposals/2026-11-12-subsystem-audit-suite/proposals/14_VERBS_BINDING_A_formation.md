# VB-A — a tie is released only where it is held, and an office is founded only over land that can carry one

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-10, C-25) — edit 14's audience is the `heard_by: seat_body` cell on the `a seat` prize row, read by one function (`U5c_VERBS_residue_and_governance_owner.md` §2). The term `standing` is the roster member `rank_gap`. §1's `own_edge_declines` also declines an edge a disposal imposed: a party does not release his own sentence (Jordan, A-37; `U5c_VERBS_residue_and_governance_owner.md` §4).
Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — applied `unified/U3_CONFLICT_LEDGER.md` C3-C9 (the A-37 clause: the fold refuses resolver-side in `_req_release`, formation reads only the actor's own ledger; new edit 4a), C3-C11 (A-81: each band of `establish` names its durable write), the body's stale `standing` replaced by `rank_gap` (`unified/work/R4_READ.md` §1.1, U1 R-21, D-U1-01), U3 batch B21 and its dependencies, R4 7b.0 implementation block. R4's `[UNVERIFIED]` on `PersonInterior.tenures` is settled at the tree: `opening_set` takes a `Person` (`decision/options.py:63`) and already reads `p.tenures` with `t.live` (`_held_objects`, `:973-976`); no `PersonInterior` class exists.

## Status: PROPOSED

Lands in batch: B21 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), after `22_HAPPENINGS_B` edits 1–2 and `06_FA_seat_terms_by_body_B`, before `U5d_FA_owed_edits` §2 (C3-D5's order inside B21). `17_CENSUS_C1A_02_wires_and_corrections.md` W2's closing gate for these rows rides in this batch (U3 §4.1 row 36).
Depends on: `05_SC_obstacle_difficulty_and_modifiers_B.md` edits 1–6 and `U5c_SC_one_obstacle_form.md` §4 steps 0–2 (B05: the `difficulty:` column, `reception`, `rank_gap`); `U5c_VERBS_residue_and_governance_owner.md` §2 (B07: the `a seat` prize row and `audience_of`) and §4 (B07: the A-37 clause).
Lane: FA. Tier (R4 7b.0 (1)): A1 and A2 `sonnet` producer, effort `high`; A3 (the contested row and its obstacle terms) `opus` producer; one `opus` read of each gate's output. Test file: `engine/season/tests/test_vb_a_formation.py` (one function per gate A1–A3; `aperture 2 s` is called inside it).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, U1 D-U1-08) on the actor's skill score (A-6); the governing attribute enters as levels (A-7); a wound is a level against the roll (A-8). The `establish` draw takes `H(w.world_seed, w.tick, <actor id>, "establish.seat")` (A-30; `04` PART D 35). A-81: see edit 12's band list.

Source: `audits/14_VERBS_BINDING.md` §0.1, §0.2, §5 (`establish`), §10 (`release`); batch A of its landing
order. Evidence: `aperture 2 0` `[FA]` and `aperture 2 1` (realm, seeds 0 and 1, two seasons,
`PYTHONHASHSEED=0`); the per-act probe `scratchpad/runs/VERBS_BINDING/binding_probe_2_1.txt`.

## What it changes in `engine/season/` at runtime

1. `release` forms only on a referent that is the object of one of the actor's own live Tenures of a kind
   in the row's own `domain:`. Today it forms on any plain referent and the fold refuses.
2. `establish` forms only on a holding its actor may found over and whose derived office does not yet
   exist, carried as a new named class `Holding`. Today it shares the `Rung` class with four verbs and
   re-forms a founding already made.
3. `establish` becomes a contested row (the standing rule, audit §0.2): the founding is drawn, graded and
   recoverable.

(1) and (2) narrow formation and change no effect. (3) changes the effect. Each is a declared hash mover
for the realm and ships behind its own revert.

## The problem (evidence)

- `release`: seed 0 attempted 15, executed 0, refused 15; seed 1 attempted 18, executed 3, refused 15
  (`release.refused`, read `no-read`). The probe: every refusal names a referent the actor owns no
  releasable edge toward (persons releasing the King; cohorts releasing the settlement they live in,
  `cohort_set_s_036 → set_s_036` seven times). `_req_release` (`loop/predicates.py:429`) is right to
  refuse; the actor could have known.
- `establish`: seed 0 attempted 8, executed 1, refused 7; seed 1 attempted 5, refused 5 (`no-read`), all
  one act: the Confessor founding over `b_s_014_barracks`, not among `holdings_to_found` for him. Two
  causes, both stated in the code: the `Rung` class is shared (`queries/world_q.py:3535`, *"the fold
  disposes"*), and *"A HOLDING ALREADY FOUNDED IS STILL OFFERED: the derived office's id is the
  derivation's (`loop/`), not this module's"* (`:3536-3539`).
- Both are untyped rows, so the refusal does not decay (`rosters.yaml: own_title_declines` note: *"an
  untyped row's refusal does not decay"*): the act re-forms every scene.
- `establish` founds with certainty once admitted, which the standing rule forbids.

## The resolution, decided

**Formation reads what the actor owns** (ladder step 4: `own_hold_declines` and `own_title_declines`
are the precedent, *"no scene is spent on a refusal of the row's conjunct he could have known"*).
`release`'s decline reads the row's own `domain:` column, so the set of releasable kinds keeps one owner
(the loader already asserts that column against `tenure_kinds`). `establish` gets a named class on
`Detainee`'s precedent (a world fact the chooser cannot see, stamped by the one standing occasion that
computes it), and the founded-office id moves to the module both its readers can import, so the
already-founded filter is no second copy of the rule.

**The founding is drawn** (audit §0.2): prize `a seat`, no person opponent, obstacle `difficulty`
`demanding` + `reception` of the holding's seated persons + `rank_gap` (OBS §2 member 6; U1 D-U1-01: a seat
above the actor's stands against the act only as this term; the actor's own exercised seat helps him only
as the `office` leverage source). This file is the first in B21's order to read `rank_gap`, so commit A3
lands the member in `rosters.yaml: obstacle_terms` (OBS §2's order) with its fixture `rank_step` (control
0; NUMBER row in `hole_register.yaml`), as OBS §4 step 6+ orders (a member lands with its first reader);
BINDING_C and D read it and do not add it again. Partial founds with half the
derived remit; Failure founds nothing and is re-attemptable.

## Exact edits, by owner

**Commit A1 — `release` (formation only).**

1. `engine/season/rosters.yaml`, after `own_title_declines`:
   ```yaml
   own_edge_declines:
     source: >-
       VB-A (`proposals/2026-11-12-subsystem-audit-suite/proposals/14_VERBS_BINDING_A_formation.md`);
       `own_hold_declines`' shape, one carrier over: any live Tenure of a kind the row closes.
     note: >-
       WHICH VERBS A PERSON FORMS ONLY ON A REFERENT HE IS TIED TO BY A LIVE EDGE OF A KIND THE ROW'S OWN
       `domain:` NAMES. Read in `decision/options.py::opening_set`, person-side and World-free (AX-2): the
       objects of his own live Tenures whose kind is in the row's `domain:`. It NARROWS the referents a
       question carries and widens nothing. ONE LOADER, `data/verbs.py::OWN_EDGE_DECLINES`, refused at
       import when a member names a verb the table lacks, one that is not `own`-eligible, or one with no
       `domain:`. [ASSUMPTION; medium; Jordan to correct; revert: drop the member, and `release` forms on
       every plain referent.]
     values: [release]
   ```
2. `engine/season/data/verbs.py`, beside `_load_own_hold_declines`:
   `_load_own_edge_declines(values) -> dict[str, frozenset]` returning `{verb: frozenset(row.domain)}`,
   raising `Forbidden` (the sibling's message shape) per refused member;
   `OWN_EDGE_DECLINES = _load_own_edge_declines(roster("own_edge_declines"))`.
3. `engine/season/decision/options.py::opening_set`, after the `OWN_HOLD_DECLINES` block:
   ```python
   kinds = OWN_EDGE_DECLINES.get(verb)
   if kinds is not None and refs:
       tied = {t.object for t in p.tenures if t.kind in kinds and t.live}
       refs = tuple(r for r in refs if r in tied)
   ```
   Import `OWN_EDGE_DECLINES` with its siblings.
3a. *(W3-4a, C3-C9; A-37.)* The disposal clause, in two halves and never by reading the log from
   `decision/` (`04` §B.9: `state/acts` is resolver-side). **Fold:** `loop/predicates.py::_req_release`
   (T, `:429`) gains one clause: refuse (`release.refused`, clause `own`) an edge whose opening Event was
   caused by an Act of verb `determine`, read through `state/attribution.py::causing_act` (T, `:91`).
   **Formation:** in `opening_set`, after the block of edit 3, drop a `release` referent when the actor's
   own ledger holds a claim of a `matter.determined` Event (T, `verb_table.yaml:406-408`) naming him as
   the party and the referent's edge as its object `[UNVERIFIED: the claim's value shape; read
   `loop/witness.py`'s deposit for `matter.determined` before landing]`. Order: the fold clause first,
   then the formation decline. Text owner: `U5c_VERBS_residue_and_governance_owner.md` §4 edit 1.
4. `engine/season/verb_table.yaml`, `release` row: append to `requires_note` one sentence: *"VB-A: formed
   only on a referent the actor is tied to by a live edge of a kind in `domain:` (`rosters.yaml:
   own_edge_declines`); the predicate is unchanged and stays the fold's check."* No new key (the loader
   refuses unknown keys).

**Commit A2 — `establish` (formation).**

5. `engine/season/queries/world_q.py`: move `founded_office_id(rung, post)` here from
   `loop/predicates.py:260`, and add `founded_post(w, rung) -> Optional[str]` (the first post in
   `TITLE_DOMAINS` authored order whose kind is the rung's kind, the reverse lookup `office_founded_by`
   performs inline today). `loop/predicates.py::office_founded_by` imports and calls both; nothing else
   changes there (`loop` already imports `queries`; `queries` never imports `loop`).
6. `queries/world_q.py::holdings_to_found`: keep a holding only if `founded_post(w, r)` is not `None` and
   `founded_office_id(r, founded_post(w, r)) not in w.offices`. Delete the docstring's
   *"Not filtered here: that would be a second copy of the id rule"* and say the rule has one owner here.
7. `engine/season/data/verbs.py`: `HOLDING_CLASS = "Holding"`, checked against `REFERENT_CLASSES` at
   import exactly as `DETAINEE_CLASS` is (`:1937-1938`).
8. `engine/season/rosters.yaml: referent_classes`: add `Holding` to `values`, with one note sentence:
   *"`Holding` (VB-A): a rung the person holds and may found an office over, not yet founded
   (`world_q.holdings_to_found`); not a collection, stamped explicitly; `establish` declares it."*
9. `queries/world_q.py::questions_for`: append `tuple((r, HOLDING_CLASS) for r in holdings_to_found(w,
   p))` to the classed tuple `held` beside the detainees. **Keep** `holdings_to_found` in `added` (the
   `Rung` stamp), so `migrate`, `requisition`, `march` and `convene` are unmoved; a pair `(id, class)`
   may repeat an id under a second class (`state/carriers.py:556` refuses only a repeated pair).
10. `verb_table.yaml`, `establish`: `referent_class: Holding`; `referent_class_note` rewritten to name
    VB-A and its revert (`referent_class: Rung`). Declared derived narrowing: `RUNG_REMIT_ACTS`
    (`data/verbs.py:1930`) loses `confer` if no other `Rung`-classed row is `remit:confer`; measure
    `larders_in_purview`'s offers before and after (REM-28 measured them at 0 of 83).

**Commit A3 — `establish` drawn.**

11. `rosters.yaml: contest_subsystems.prizes`: add `"a seat"`, `module: social_contest`, `provider:
    social_contest`, `module_entry: social_contest.roll` (the `a proposition` row's fields; one prize row,
    shared by `confer`, `revoke`, `succeed` in VB-C). The composition row in
    `references/module_contracts.yaml` binds the entry to a verb naming the prize
    (`manifest/registry.py::check_contest_prizes`).
12. `verb_table.yaml`, `establish`:
    ```yaml
    contests:    "a seat"
    difficulty:  demanding        # SC-B's column (05_SC_obstacle_difficulty_and_modifiers_B.md edit 2)
    writes:
      Overwhelming: ["Office.exists", "Office.remit_acts", "Tenure.payload"]
      Success:      ["Office.exists", "Office.remit_acts", "Tenure.payload"]
      Partial:      ["Office.exists", "Office.remit_acts", "Tenure.payload"]
      Failure:      []
    emits:
      Overwhelming: ["office.established", "remit.changed", "tenure.payload_set"]
      Success:      ["office.established", "remit.changed", "tenure.payload_set"]
      Partial:      ["office.established", "remit.changed", "tenure.payload_set"]
      Failure:      ["office.unrecognised"]
    ```
    The flat `emits_on_refusal: ["establish.refused"]` stays (a contested row keys one refusal kind,
    `data/verbs.py` invariant 4's contested half). No counterparty: the opposition term is absent (SC-B:
    *"absent for a non-person subject"*). The obstacle's `difficulty: demanding` names a member of
    `rosters.yaml: difficulty_levels` (U1 D-U1-04). **Durable write of every band (A-81; C3-C11):** O/S/P
    write the office; the Failure Event `office.unrecognised` is witnessed by the holding's seated persons
    (the `reception` audience) and the persons present, and deposits a claim of that Event to each of them,
    so the refused founding is a remembered deed; where nobody else is present the actor deposits his own
    firsthand claim `(self, establish.failed, True)`.
13. `loop/effects_governance.py::_eff_establish`: read `res.degree`; at `Partial` build the office with
    `remit_acts = derived[: (len(derived) + 1) // 2]` (the derived list in its authored order). The
    office object is still built once by `office_founded_by`; the effect narrows the copy it writes.
    Typed in: `(World, Act, Resolution)`; out: `Change`. No held state; no branch on an entity.
14. `seam/wrappers/sigma.py::contest_input`: for a row with no counterparty, the `reception` audience is
    the holding's seated persons (`world_q.establishment_of` over the seats on the rung) — the
    audience operand the audit §0.2 asks of SC-B's `reception` reader.

Order: A1 (with 3a), A2, A3; A3 waits on SC-B's obstacle terms (edits 1–6 of that proposal) and on the
`a seat` prize row (VRES §2, B07).

## Gate (execution artifact)

- A1: `aperture 2 0` and `2 1`: `release.refused` 15/15 → 0; executed not below 0/3. 3a: at one seed with a
  determined case, the party's candidates hold no `release` of the disposal edge; a planted one is refused
  naming the clause `own`; a `pardon` at Success closes it. Falsifier: a disposal edge closed by an Event
  whose actor is its subject. Control: the formation decline removed, the candidate returns and the fold
  still refuses.
- A2: same instrument: `establish.refused` 7/5 → ≤1 each; the probe shows no act on a non-holding and no
  repeat of a founded holding. If `holdings_to_found` is empty for every person the reading says so and
  is reported as content (nobody holds land he may found over), not as a pass.
- A3: on a hand-built world with one foundable holding, seeded across 40 seeds: all four bands occur,
  Partial founds an office whose `remit_acts` is the first half, Failure writes nothing and the act
  re-forms next scene.

## Falsifier

- A1: read `RELEASABLE_KINDS | {"reside"}` in the decline instead of the row's `domain:`: the cohorts'
  refusals on their home return.
- A2: drop edit 6's filter: the Confessor's repeated refusals return (or a repeat on a founded holding).
- A3: pin the roll to Success: the band count collapses to one and the gate's band check fails.

## What it does not do

It does not decide why a person would release or found (the chooser's alignment cells and CR-88's duty
term). It adds no closer and no opener. It does not touch `own_hold_declines`.

## NERS reading

N: without A1/A2 both verbs spend scenes on refusals the actor could read; without A3 a founding cannot
fail. R: a founding may half-take and be re-remitted; a tie is reconsidered when news of it arrives. S:
one decline shape (three siblings), one office-id owner, one roll owner; the `Partial` founding is the
same "less than whole" shape the family uses. E (last, as a ratio): three small narrowings and one band
map buy every refusal in both rows.

## Cost class

Small: one roster, one loader, one filter, one class, a function moved, one band-keyed row, one effect
branch on degree.
