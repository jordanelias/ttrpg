# Opus execution prompts — agonist→antagonist pairs

Copy verbatim. Each item is two dispatches: the producer, then the critic **with the producer's
OUTPUT only**. Critic dispatch: `subagent_type: "valoria-critic"` (tools `Read, Grep, Glob` — its
read-only property lives in the agent definition, not in the prompt).

---

## COMMON PRODUCER BLOCK — prepend verbatim to every agonist prompt

```
You are implementing one work item in the Valoria season-loop tracer. Read
/home/user/ttrpg/CLAUDE.md §0, §0.05, §0.1, §0.2, §2 and §10 before touching the tree.

Binding constraints, none negotiable:
- §27.2 NO SECOND RESOLVER. Read contest() at
  /home/user/ttrpg/engine/season/shape.py:4903-4984.
  You may not compute a band, a margin, an auto-resolve, or a fast path anywhere. A
  degree is read off a subsystem's return or minted by
  /home/user/ttrpg/engine/autoload/dice_engine.py::degree_from_net, nowhere else.
- §F1 / L2: `choose`, `opening_set`, `belief_contradicts`, and anything they call takes
  no World. test_w5_sense_is_still_the_only_world_taking_non_decision_function walks the
  AST for this; keep it green. Clause 4 is KNOWN-false from the person's OWN claims;
  absence of a belief is not a belief in the negative.
- §0.05: code is the mechanism. A value the engine uses lives in verb_table.yaml,
  rosters.yaml, write_matrix.yaml, or DEFAULT_FIXTURES with a hole_register.yaml row
  (grade, site, three sweep points for `assumption`). No literal in a body.
- §0.1 pt 5: add no guard/test unless it is load-bearing on the game or a Jordan
  decision. Every test you add must be able to observe the failure it excludes
  (§0.1 pt 2) and must carry its mutation check in the docstring.
- §0.2: done means it RUNS. Your output ends with the exact commands and their output.
- L1: no cap, dedup, truncation, or engine-side choice of a person's options.
- Emergence: no special case for an entity, verb or outcome. If you find yourself
  writing `if verb == "transfer"`, stop.
- One owner: never re-implement a rule that lives once. Delete the old copy when you
  move one.
- Prose: do NOT write a README, plan, summary or findings document. Edit code, data
  and register rows; commit message under 40 lines; PR body says PROPOSED, HELD BACK
  IN FULL, NOTHING RATIFIES ON MERGE (§2).
- Commit format `[design] ...`, on a branch, citing the H-rows touched. Run
  `python -m pytest engine/season/tests/test_season_shape.py -q`
  and `python -m pytest tests/valoria -q` before committing; report red honestly.
Return: (1) the unified diff, (2) the verbatim output of every command you ran,
(3) the register rows you changed, (4) one paragraph naming the falsifier and its
outcome. Nothing else.
```

## COMMON CRITIC BLOCK — prepend verbatim to every antagonist prompt

```
You are the antagonist (valoria-critic; Read/Grep/Glob only). You receive a producer's
OUTPUT below — a diff, command output, register rows — and never its reasoning. Re-verify
every claim against disk at
/home/user/ttrpg/engine/season/ and
/home/user/ttrpg/architecture/. Rule per claim:
uphold / overturn / soften / sharpen, each with file:line. Then hunt what the producer
did not cite: read at least one surface outside the diff. Check the repo's recurring
failure modes: a number without a reproducing command; a "missing" mechanic that exists
one field deeper (HANDOFF_NEXT.md PART 3); a guard that cannot observe its failure; a
special case for an entity or outcome; a rule now living twice; a World reaching a
person-side function; a band, margin or outcome computed outside dice_engine or the
seam's read. State exactly what you checked. Finding nothing is a verdict; say so and
list coverage. Output the schema the caller gives you and nothing else.
```

---

## W-0 · instrument prerequisites — agonist `sonnet`, antagonist `sonnet`

### AGONIST
```
[COMMON PRODUCER BLOCK]
Work item W-0. Four mechanical changes, no design decision.
1. shape.py:2026-2033 World.content_hash reads only self.log (hole_register.yaml H-118).
   Make it fold persons, sites, rungs and tenures in id order, then the log, then each
   Event's observed[] if present. Falsifier: H-118's own repro — two identical worlds,
   delete a person from one with no Event, hashes must differ. Pin it as a test.
2. shape.py:708,712,728,733 raise SystemExit (H-115). Raise Unspecified(msg, "S39/H-98",
   needs=..., law=...) instead. Falsifier: arm2_onramp.run_2c's repro — the raise is
   caught by corpus_run.run_case's ShapeGap clause and reported DESIGN-GAP.
3. corpus_run.py:341 and :386-388 call season() with no contest_max_depth. Pass
   w.fixtures.get("contest_max_depth") (H-87's fixture). Falsifier: a hand-built
   Act("k","p_a","kill / wound",payload={"subject":"p_b"}) driven through run_case no
   longer raises Forbidden S39.3.
4. /home/user/ttrpg/proposals/2026-09-04-degree-sweep/arm9_forking.py imposes
   exclusivity by ranked[:1]. Replace with a NATIVE fork: baseline packs the person's
   real ranked list under the real budget; a fork at decision i, alternative t, swaps
   ranked[t] into the last in-budget slot and reports one of three outcomes per fork:
   INERT-BY-CONSTRUCTION (t was already inside the budget; the fold orders by
   (stratum, hash) at shape.py:4570, so order changes nothing), DIVERGED, RECONVERGED.
   Add fixtures= to run() and print per deliberation `budget_binds = candidates > slots`
   where slots = scene_budget × interactions_per_scene (read from fixtures, never a
   literal). Run it at DEFAULT_FIXTURES and at interactions_per_scene=1 and print both.
5. hole_register.yaml H-117 is already re-kinded from ABSENT_RULE to NUMBER. Verify the
   arm-9 line that shows budget_binds True at the 1 point now exists and is cited there.
   Do not add a row.
Do not touch belief_contradicts, opening_set, witness, the verb table, or any effect.
```

### ANTAGONIST
```
[COMMON CRITIC BLOCK]
The producer claims to have completed W-0 (instrument prerequisites). Try to break:
- content_hash: does it now hash state, and is the hash still deterministic under R4
  (same seed twice)? Does it iterate dict-ordered collections in id order? A hash over
  insertion order would pass the repro and break replay.
- SystemExit → Unspecified: grep shape.py for every remaining `raise SystemExit`; the
  14 load-time ones must remain (H-115 says so). Count them.
- contest_max_depth: is it passed to BOTH season() calls in run_case (the measured run
  and the R4 replay)? A cap on one and not the other silently breaks R4.
- The native fork: open arm9_forking.py. Is ranked[:1] gone everywhere? Does the swap
  change the SET only when t >= slots? Are the three outcomes reported separately, or
  is INERT-BY-CONSTRUCTION folded into RECONVERGED (which would inflate the finding)?
  Is `slots` read from fixtures or written as 15 or 5? Re-run nothing; read the
  printed output the producer supplied and check the arithmetic against
  DEFAULT_FIXTURES at shape.py:952 and :1020.
- H-117: did the producer preserve the measured evidence, or rewrite the finding?
Report per claim, then coverage.
```

---

## W-A · typed `requires`, one evaluator, two readers — agonist `opus`, antagonist `opus`

### AGONIST
```
[COMMON PRODUCER BLOCK]
Work item W-A. Type the `requires` column so ONE declaration has THREE readers.
Read first: /home/user/ttrpg/architecture/meta/04_CODE_ARCHITECTURE.md
§F.24a (lines 978-1010) — seven forms derived from the 32 live cells; and :226-230, the
carve-out licensing the fold to read the ACTOR'S OWN ledger and no other. Read
shape.py:2537-2560 (belief_contradicts), :3270-3660 (REQUIRES_PREDICATES and every
_req_*), :4414-4427 (the fold's requires check), :2296-2340 (resolvable_verbs).

Build:
1. rosters.yaml: a closed `requires_forms` roster (seven names derived from §F.24a; a
   form outside it refuses at load). Each form declares `needs:` — the operand names it
   binds (actor, subject, from, to, site, kind, amount, floor). Operand SUPPLY is W-C's
   job, not yours; today the binding comes from Act.payload and is allowed to be
   incomplete (→ UNKNOWN at the fold, which the fold reports as today's refusal).
2. verb_table.yaml: for every row whose eligibility includes `own` and whose `requires`
   is not in NO_PRECONDITION, add a typed cell beside the prose (keep the prose; it is
   provenance). Derive each cell from the prose and cite the §E3 line. Where the prose
   is a well-formedness constraint (issue, open_case) or "per act" (the six
   investigation acts) or `absent` (determine), write `requires_typed: none` with a
   `requires_typed_note:` and leave the verb on REQUIRES_PREDICATES or unresolvable —
   do not invent a predicate.
3. shape.py: a Requirement type per form; `evaluate(req, reader, binding) ->
   Verdict(value in {True, False, UNKNOWN}, observed: list[Observation])` where
   Observation = (subject, predicate, value) and predicate is DERIVED from the form
   (e.g. f"stores:{kind}", "condition", f"contain.path:{to}", f"edge.live:{kind}:{obj}")
   — never a roster entry; a `WorldReader(w)` that records every read as an
   Observation; a `LedgerReader(claims)` that answers from the most recent (then most
   confident) claim with matching subject and predicate, else UNKNOWN, and takes no
   World. Form 6 (own_claim) reads the actor's ledger on BOTH sides.
4. The fold uses evaluate() for a typed cell and REQUIRES_PREDICATES only for an
   untyped one. Delete each _req_* whose verb is now typed (one owner). Keep the
   Observation list on the Verdict but do NOT attach it to Events yet — that is W-B.
5. belief_contradicts becomes: evaluate(row.requires_typed, LedgerReader(p.ledger),
   binding_from(candidate)).value is False. It no longer reads PERSON_PREDICATES.
   Untyped verbs return False (not contradicted), as today.
Tests (each with its mutation named in the docstring):
- one-owner: no verb has both a typed cell and a REQUIRES_PREDICATES entry; every
  own-eligible verb with a prose requires has a typed cell or an explicit `none`
  (assert checked >= 11).
- asymmetry: for every form, evaluate over an empty LedgerReader is UNKNOWN and
  opening_set still forms the Candidate.
- contradiction: planted (Hh, "stores:grain", 0) removes transfer×Hh from
  opening_set in probes.tiny_world; planted value 9 keeps it.
- fidelity: every existing test that exercised a retired _req_* still passes; flip
  transfer's comparator to "<=" and name the test that goes red.
- L2: test_w5_sense_is_still_the_only_world_taking_non_decision_function green.
Do not change PERSON_PREDICATES, standing_of, agreement, witness, or Event.
Register: update H-72 (grade → measured, site → shape.evaluate / LedgerReader, cite the
test) and H-65 (the fold's prose defect narrowed to the untyped remainder, listed by
name). Print "typed N of 32; uncovered own-eligible: [...]" from a test, not by hand.
```

### ANTAGONIST
```
[COMMON CRITIC BLOCK]
The producer claims W-A: `requires` typed for own-eligible verbs, one evaluate() with a
WorldReader and a LedgerReader, belief_contradicts rewired. Specifically try to break:
- TRANSCRIPTION, cell by cell. For each typed cell, open verb_table.yaml's prose and
  ARCHITECTURE_V2.md §E3 (lines 404-435). Does the typed form OVER-refuse (a conjunct the
  prose does not have) or UNDER-refuse (a dropped disjunct — _req_confer's history at
  shape.py:3410 is the precedent for this exact error)? G4 weighs both equally.
- SECOND RESOLVER: does any form let the cell talk about the act's own payload
  beyond binding operand NAMES? §F.24a says a grammar that can inspect the act becomes
  a second resolver. Does any form compute a number the design does not state?
- ONE OWNER: grep for every remaining `_req_` definition and every REQUIRES_PREDICATES
  registration; list any verb present in both. Grep for any place that still reads
  PERSON_PREDICATES besides agreement()/standing_of().
- ASYMMETRY: read LedgerReader. Can it ever return False from an ABSENT claim? Can a
  claim with value True be misread as False? What about a stale claim newer than a
  refusal — which wins, and is that ordering declared?
- PREDICATE DERIVATION: is any observation predicate listed in a roster AND derived in
  code (ID-12 twice-declared)? Is `stores:<kind>` disjoint from PERSON_PREDICATES so
  standing_of cannot pair it?
- L2: does LedgerReader, evaluate, binding_from, or any Requirement method accept a
  World anywhere? Is the AST test still present and unmodified?
- Did the producer touch witness(), Event, or attach observations early (W-B's scope)?
- Re-check the printed "typed N of 32" against your own count of the YAML.
Report per claim; then a coverage list of every verb row you opened.
```

---

## W-C · operands on the Candidate — agonist `opus`, antagonist `opus`

### AGONIST
```
[COMMON PRODUCER BLOCK]
Work item W-C. Close H-94's structural half by precedent, and delete every silent
operand default. Read hole_register.yaml H-94 and H-80; shape.py:1383-1387 (Candidate),
:2220-2261 (opening_set), :2698-2779 (pack_scenes, payload at :2739), and the defaults
at :3533-3534 (_req_transfer), :3581 (_req_move), :3611 (_req_work's vacuous True),
:3798 (_eff_work's next(sorted(w.sites))), :3892 (_eff_transfer). Read the
requires_forms roster and each form's `needs:` from W-A.

⚠ THIS ITEM IS ON THE CRITICAL PATH AND THE SWEEP FIRST PUT IT BEHIND W-B. The corpus's
transfer.refused / travel.blocked are OPERAND-GAP refusals, not world refusals. If W-B
deposits observations before operands are supplied, every witness learns a FALSE fact
about the world from a malformed act. Operands first.

The answer to "where do operands live", under CLAUDE.md §0's five tests, at step 4:
operands live on the Candidate, derived PERSON-SIDE. §54 item 7's own formula is
stores(hearth(giver), kind) >= amount: hearth(giver) is the object of the actor's own
live `contain` Tenure (person state after W5), not a choice. `to` is the question's
referent. `kind` and `amount` are values the design does not supply — H-80's exact
shape, so they are `assumption` fixtures: declare, default, sweep. Write that argument
into H-94's cite and regrade the derivation `assumption` with a site and three sweep
points; the structural question closes at step 4 and does not go to Jordan.

Build:
1. Candidate gains `operands: dict`. `operands_for(row, p, q, fx) -> dict | None`,
   person-side, no World: actor=p.id; subject=referent; from = object of p's own live
   contain Tenure; to = subject when the form needs a rung; site = a Site id the person
   can name from their own state (if you cannot derive it without a World, DECLINE and
   record why in a TRACE.note); kind = from q.about's claim predicate if it is
   `stores:<kind>` else fixture default_store_kind; amount = fixture
   default_transfer_amount, swept [0, 1, 3] with 0 as the control (nothing is spent;
   scarcity never binds); floor = the params floor.
2. RULE, load-bearing: a form whose `needs` cannot be bound forms NO Candidate. Never
   mint an act with a hole. TRACE.note the missing operand so the count is measurable.
3. pack_scenes puts payload={"subject": ..., **operands}. binding_from(a) reads it.
4. Delete every `.get(<operand>, <literal>)` default in _req_*/_eff_* and the vacuous
   `return True` in _req_work. A missing operand at RESOLVE is an InstrumentDefect (a
   caller minted a malformed act), not a refusal — it must never emit
   emits_on_refusal. Leave _eff_kill's `harm` default with a comment naming W-E.
Tests: zero corpus refusals from a missing operand (count the TRACE reason across
`python corpus_run.py`); transfer executes at least once in the corpus (executed verbs
6 → 7 — cite H-94's cite for the 5 → 6 precedent and the measuring command); at
default_transfer_amount=0 no Rung.stores write occurs; a grep-test asserting no
`.get("kind"`, `.get("amount"`, `.get("from"`, `.get("to"` with a default remains in
shape.py; Candidate declines (not mints) when `from` cannot be derived.
```

### ANTAGONIST
```
[COMMON CRITIC BLOCK]
The producer claims W-C: operands derived person-side onto the Candidate, silent
defaults deleted, H-94 regraded by precedent. Try to break:
- THE PRECEDENT ARGUMENT in H-94's new cite: run CLAUDE.md §0's five tests yourself.
  Is `hearth(giver)` really derivable from the person's own state (check Person.tenures
  after W5, shape.py:1464-1500, and _TenureView)? Is H-80 genuinely the same shape, or
  does H-80 stand in for a Record's stages while this invents WHAT a person transfers,
  which is a materially different game (§62's test)? If you overturn, say what a
  ruling would have to decide.
- L2: does operands_for take a World, a Query over the world, or anything reaching
  w.sites / w.rungs? Grep its body. Does `site` derivation quietly read the world?
- THE DECLINE RULE: find any path where a Candidate with an unbound operand still
  reaches pack_scenes. Find any path where RESOLVE turns a missing operand into an
  emits_on_refusal Event (that would poison W-B).
- SILENT DEFAULTS: grep shape.py for `.get(` with a literal second argument inside any
  _req_ or _eff_ function; list survivors. Check _req_work no longer returns True on an
  empty a.changes.
- THE FIXTURES: are default_store_kind and default_transfer_amount in DEFAULT_FIXTURES
  with register rows carrying site and three sweep points? Is the 0 point actually run
  by a test (§0.1 pt 4: a control that is not run is not a control)?
- THE 6 → 7 CLAIM: read the producer's corpus_run output. Is `transfer` attributed by
  emission id (exact) or by kind (H-94's own cite records the forge/create_record false
  positive)? Does the executed set include anything the fold cannot execute?
- SCRIPTING DRIFT: any `if verb == "transfer"` or per-verb operand code outside the
  form's declared `needs`?
Report per claim; coverage list.
```

---

## W-B · observations ride the Event — agonist `sonnet`, antagonist `opus`

### AGONIST
```
[COMMON PRODUCER BLOCK]
Work item W-B. Give the world→belief edge a true payload. Read shape.py:1244-1262
(Event; §19.3's three deliberately-absent fields, and `degree` added by #358 — a typed
field is precedented), :4380-4497 (_fold), :4720-4800 (witness; the deposit at :4782
mints predicate=e.kind value=True), :2797-2870 (claim_subjects and its warning that
extra deposits once silenced the H-40 decay sweep), :1330 (View), rosters.yaml
view_builder_rules (H-53).

Build:
1. Event gains `observed: list[Observation] = field(default_factory=list)`.
2. _fold attaches verdict.observed to the emission on BOTH the success and the refusal
   path. An Observation is minted only from a read the WorldReader actually performed —
   the reader's trace is the only source; there is no other constructor call site.
3. witness() mints, per observation, one Claim(id, pid, obs.subject, obs.predicate,
   obs.value, w.tick, src, conf, "own") beside today's event-kind claim. Id derivation
   follows the existing H(seed, tick, pid, f"claim:{e.id}:{n}") scheme with a distinct
   purpose string. Go through w.write as today. H-111 stays open; append one sentence
   to its hole: a refusal now also teaches the fact it was refused on.
4. Fixture `observation_deposit` ∈ {on, off}, default on, register row `assumption`,
   `off` is the control. content_hash folds observed[].
5. LedgerReader in opening_set is built over the View's claim_ids (S18: at most K,
   built not filtered), so view_builder_rule `question_relevant` (H-53) finally has a
   reader; whole-ledger is a swept alternative on H-53's row. Do not change view_k.
Tests: the worked example — in probes.tiny_world, p_low's transfer from Hh (8 grain)
of amount > 8 is refused, the actor's ledger holds (Hh, "stores:grain", 8) at t, and at
t+1 opening_set omits transfer×Hh (control: observation_deposit=off keeps it);
fabrication guard — construct an Observation not in any reader trace and assert the
fold refuses to attach it; H-40's decay sweep still reports three distinct minimum
confidences; ledger sizes before/after over `python corpus_run.py`, and R3 unchanged
(30/30 NPC, 54/59 ARC, with the five 1-season misses named).
Do not change PERSON_PREDICATES, standing_of, or the event-kind claim.
```

### ANTAGONIST
```
[COMMON CRITIC BLOCK]
The producer claims W-B: Event.observed, deposit of observation claims at WITNESS, the
LedgerReader over the View. The hazard is ID-9's class inside the epistemic layer: a
claim that teaches every witness something false. Try to break:
- FALSE OBSERVATION: can an Observation be minted from anything other than a read the
  WorldReader performed? Can a refusal caused by a missing operand (an
  InstrumentDefect after W-C) still emit an Event that carries observations? Can a
  success emit an observation of the POST-write value (it must be the pre-write read)?
- STALENESS: the fold runs acts in order; a later act in the same season changes the
  granary. Which value is deposited — the one read at the fold or the one at WITNESS?
  Read _fold and witness and say which.
- SUBJECT: what subject does the observation claim carry, and does Q2 (shape.py:2600)
  fire on it next season? Trace one transfer refusal by hand through claim_subjects →
  witness → questions_for and state whether a question forms.
- THE VIEW: is LedgerReader really restricted to v.claim_ids, or does it fall back to
  p.ledger? Under view_builder_rule=recent with K=12 and total fan-out, can the
  observation the person needs be evicted before DELIBERATE? Is that measured?
- LEDGER PRESSURE: read the before/after ledger sizes and the three H-40 arm minima. If
  all three arms print the same minimum, the decay sweep is inert again and the item is
  not done.
- ONE OWNER: is the observation claim minted at exactly one site? Does content_hash
  fold observed[] and is R4 still a same-seed match?
- Did the producer touch standing_of/agreement/PERSON_PREDICATES?
Report per claim; coverage list.
```

---

## W-D · the acceptance run — agonist `sonnet`, antagonist `sonnet`

### AGONIST
```
[COMMON PRODUCER BLOCK]
Work item W-D. Re-run the forking exercise as the §0.2 execution artifact for W-0..W-C.
Read /home/user/ttrpg/proposals/2026-09-04-degree-sweep/arm9_forking.py (as changed by
W-0), sweep_core.py, and README.md's arm-9 section for what was measured before.

⚠ THE WINDOW MUST BE SEASON-AWARE. DELIBERATE is a parallel map over a FROZEN world
(shape.py:4204-4221), so decisions bind in order only ACROSS seasons. A lookahead that
counts same-tick decisions counts slots that cannot differ, and a fork in the final
season has no live slot at all. Take only decisions at a STRICTLY LATER tick, and
report a fork that cannot fill the window as NO-LIVE-WINDOW, excluded from the rate.

Run arm 9 over the full runnable corpus at seed 0 at BOTH DEFAULT_FIXTURES and
interactions_per_scene=1, each with observation_deposit on and off — four arms.
Report per arm: forks probed; INERT-BY-CONSTRUCTION / NO-LIVE-WINDOW / DIVERGED /
RECONVERGED; reconvergence over DIVERGED+RECONVERGED only; budget_binds rate; world
fingerprint divergence (not content_hash alone). Positive control: in probes.tiny_world,
a planted (Hh, "stores:grain", 0) claim at t flips p_low's decision at t+1 — print the
two ranked lists. Negative control: observation_deposit=off at interactions_per_scene=1
must return reconvergence to the pre-W-A figure; if it does not, something other than
the belief edge moved and you must find it before reporting.
Write results only to runs/SWEEP_LOG.txt and runs/results.json via sweep.py; do not
edit README.md. Every number in your commit message is copied from results.json.
```

### ANTAGONIST
```
[COMMON CRITIC BLOCK]
The producer reports the forking exercise re-run after the belief edge was opened. Try
to break the MEASUREMENT (§0.1: attack the setup, not only the statistics):
- Is the window season-aware? Open the code. Does it take only strictly-later-tick
  decisions? Are NO-LIVE-WINDOW forks excluded from the rate rather than counted as
  reconverged? (The first version of this arm did exactly that and inflated the result.)
- Are the arms the same experiment? Same seed, seasons, case list (89 runnable after
  apply_rescale), same fork enumeration? Diff the fork counts; an arm with a different
  denominator is not a control.
- Is INERT-BY-CONSTRUCTION excluded from the denominator, and is its count consistent
  with slots (5 at the 1 point, 15 at default)?
- Does the negative control actually return to the prior figure? If it returns to
  something else, name what else moved.
- Does the positive control print two ranked lists differing by the transfer candidate
  and nothing else?
- Is divergence measured on a world fingerprint reading persons/sites/rungs/tenures
  (H-118), or on the log?
- Read results.json yourself; check the commit message's numbers against it.
Report per claim; coverage list.
```

---

## W-E · a degree reaches the fold — agonist `opus`, antagonist `opus`

### AGONIST
```
[COMMON PRODUCER BLOCK]
Work item W-E. Let kill / wound resolve at a degree, end to end, without inventing one.
Read shape.py:2296-2340 (resolvable_verbs; the third gate at :2336), :4602-4677
(resolve's contest branch), :4441-4448 (_degree_for_writes = None), :3848-3867
(_eff_kill; `harm` defaults to the whole body), :701-738 (writes_at/emits_at; emits_at
has no caller — H-113), combat_seam.py (returns wound_state for both parties; `winner`
is NOT the degree source — H-119), verb_table.yaml's kill / wound row, hole_register
H-113, H-114, H-119, H-120, H-97, H-98.

Constraints beyond COMMON: the degree is READ, never mapped (Jordan 2026-09-03). The
band names are the verb's declared branches; you may not add a fourth (H-98). No band
literal in contest() (test_d4 pins it). Combat rules stay in systems/combat/.

Build:
1. resolvable_verbs third gate: `contested and not callable(row.contests)`, where
   callable(prize) is true iff contest_subsystem(prize)["module"] has a seam caller —
   derive it from contest()'s dispatch, do not list it.
2. verb_table.yaml kill / wound gains `degree_from:` — one predicate per declared
   branch over the subsystem's return, using W-A's grammar over a
   ResultReader(wound_state[target]): Felled ⇐ felled is true; Wounded ⇐ felled false
   and wounds > 0; Untouched ⇐ felled false and wounds == 0. Loader asserts the
   degree_from keys equal the writes and emits keys (extend invariant 12) and that
   exactly one branch is true for any wound_state — test it over the 300-fight sample
   arm2 already draws.
3. resolve(): on RESOLVED, mint the degree via degree_from and fall through to
   _fold(w, a, degree); on ContestError emit kill.refused with causes=[a.id]; on a
   non-RESOLVED status keep the Unspecified raise.
4. _fold(w, a, degree=None): _pairs = row.writes_at(degree); kinds from
   row.emits_at(degree); Event.degree set. Untouched writes nothing and still emits.
5. _eff_kill(w, a, degree, wound_state): Felled as today. Wounded lowers the target's
   body by ONE BAND PER WOUND on band_floors["body"] — the mirror of
   combat_seam.derive_party's one band = one `end` point (H-97); no new number. Apply to
   BOTH parties from wound_state and return {kind: [ids]} so one Event carries a
   StateChange per subject. Register the proportional alternative
   (health_remaining/health_full) as a sweep point on H-114, not as code. Delete the
   `harm` default. `winner` is never read (H-119 default).
Tests: arm3_tree.fold_one's repro — Untouched emits no person.died; Wounded leaves the
person alive and exactly one band lower per wound; a depth-cap contest emits
kill.refused as an Event with causes=[a.id]; test_d4 and
test_the_seam_calls_personal_combat_rather_than_naming_it green; over the corpus S39
firings > 0 and DESIGN-GAP still 0; arm 3's distinct-leaf count on ladder D exceeds 1 on
at least one case. Print how many corpus persons die across the 89 runs before and
after; do not tune anything to change it — report it against H-96.
```

### ANTAGONIST
```
[COMMON CRITIC BLOCK]
The producer claims W-E: kill / wound resolves at a degree read off scene combat. The
silent failure is §27.2 — a second resolver wearing data's clothes. Try to break:
- IS degree_from A MAPPING OR A READ? Open the new column and the ResultReader. Does any
  branch predicate compare quantities the engine did not compute (a margin, a ratio, a
  threshold nobody ruled)? "wounds > 0" is a read; "wounds > max_wounds/2" is an
  invention. Say which each branch is.
- FOURTH BAND: any path yielding a degree outside the three declared branches, or a
  fallback to the union (the defect writes_at exists to make unwritable)?
- EXCLUSIVE AND EXHAUSTIVE: does the 300-fight test assert exactly one branch per fight,
  and `checked >= N`?
- WINNER: grep the diff for any read of r["winner"] or r["result"] deciding a write.
  H-119 says the two surfaces disagree ~5-6%; reading winner is a wrong outcome in one
  fight in twenty.
- THE HARM MODEL: is "one band per wound" really the mirror of derive_party (open
  combat_seam.py and body_band_penalty), or a new number? Is the alternative registered
  on H-114 as a sweep point rather than coded?
- TWO PARTIES: does the actor's own wound go through the gate as a Person.body write
  with a StateChange naming the actor, or is it applied directly (a write bypassing the
  matrix)?
- THE THIRD GATE: is callable(prize) derived from contest()'s dispatch or a list? Would
  social_contest be admitted (it must not be)?
- THE BLOODBATH NUMBER: is the death increase explained by alphabetical tie-break (H-96)
  or by something in the seam? Observe; do not rule on H-96.
- Did contest() itself change at all? It should not have.
Report per claim; coverage list.
```

---

## W-F · interior consequence (GATED on W-D) — agonist `opus`, antagonist `opus`

### AGONIST
```
[COMMON PRODUCER BLOCK]
Work item W-F. Only proceed if W-D showed the candidate SET moves and the RANKING does
not. Read hole_register H-62 (absent: no verb writes any Person interior field),
write_matrix.yaml Person.stance / Person.convictions (convictions move "by argument and
consequence, never by evidence" — AX-3), 04_CODE_ARCHITECTURE.md §C.4 (an interior write
is a consequence of an outcome and rides the degree-keyed column), shape.py:2384-2472
(align, stance_toward, choose).

The shape is ruled; the VALUE is not. So: `assumption`, declare/default/sweep, one
register row. Build the smallest thing: a verb row's degree-keyed (or refusal-keyed)
writes may name Person.stance; the effect appends (subject, valence, weight) on the
ACTOR'S OWN stance rows only, magnitudes from two fixtures swept with 0 as the control;
never convictions; never from a claim (evidence). Which verbs and which outcomes carry
it is DATA on the row, graded assumption, and you must argue each from the design's
prose (§9, §18.2), not from what would make the corpus diverge. If you cannot argue a
row from the design, do not add it.
Tests: with the fixtures at 0, choose's ranking is byte-identical to before (control);
at the default, a refused transfer at t moves the actor's stance toward the refuser's
subject and the next season's ranked order differs (print both); AX-3: grep-test that no
effect writes Person.convictions; the write goes through the gate as class ACTS.
```

### ANTAGONIST
```
[COMMON CRITIC BLOCK]
The producer claims W-F: outcomes write the actor's stance through the degree-keyed
column. This is where scripting drift and AX-3 violations are most likely. Try to break:
- AX-3: does anything write convictions? Does any stance write take a Claim or the
  ledger as input (evidence moving the moral layer)? Read the effect's signature.
- SCRIPTING DRIFT: is the set of (verb, outcome) rows carrying a stance write argued
  from §9/§18.2 text the producer cites, or chosen because it makes the corpus diverge?
  Open the cited lines. A row that exists to produce a result is a script.
- SELF-ONLY: can a stance write land on anyone but the actor? (§20: nobody writes
  another's interior.)
- THE CONTROL: at magnitude 0, is the ranking byte-identical — and is that asserted on
  the ranked list, not on the act count?
- ONE OWNER: is there now a second scoring path, or is stance_toward untouched?
- Is the register row `assumption` with site and three sweep points, and does its cite
  survive CLAUDE.md §0's five tests without reaching Jordan?
Report per claim; coverage list.
```

---

## W-G · guard, critic only — `sonnet`

```
[COMMON CRITIC BLOCK]
Audit the combined diff of W-A..W-F against three refusals. (1) §27.4: no uncontested
verb acquired a degree, a roll, or a `contests:` column — check speak, tell, the six
investigation acts, refract, comply, evade / defy, utter, petition, carry, oblige,
repudiate, determine. (2) §27.2: grep shape.py, combat_seam.py and every arm for any
band computed outside engine/autoload/dice_engine.py::degree_from_net and the verb-row
read of wound_state; contest()'s Unspecified for social_contest and mass_battle must be
byte-identical to HEAD~N. (3) Jordan 2026-09-02/04: nothing calls
systems/social_contest; `inquiry` is a STUB and stays unreached. Report the exact grep
commands and their output; finding nothing is the expected verdict and must be stated
with coverage.
```
