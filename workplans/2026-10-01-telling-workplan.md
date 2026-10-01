# THE TELLING WORKPLAN — A tells B about C, as positions T0–T6 and a gated tail

## Status: **RATIFIED workplan, 2026-10-01, BY JORDAN's instruction** (*"Ratify 2026-10-01-telling-workplan.md. Use /methodology-execute on this workplan"*). Ratification accepts §10's three recommendations; the gated tail `G1`–`G8` is ratified as a plan, not scheduled (§5); ledger row `ED-IN-0282`. Content owner for `T0`–`T6` and the gated tail (§5); changes no existing position number. Plan positions `10` and `14` point here (§9).
## Owner: infrastructure / cross-cutting (IN lane)
## Produced by: a Fable → Opus relay (`CLAUDE.md` §10): a read-only Fable 5.1 planner re-opened every cited site on HEAD `85afbf5` and issued the [CORRECTION]s obeyed here; Opus wrote the dossier and this condensation. Two NERS gates ran, the second under Jordan's 2026-10-01 ruling (not restricted to existing code; design for the ideal). His rule was to restructure around the PDF's seven stages only if a top-down and a bottom-up pass both judged it better; **both critics returned PARTIAL, so that restructure is not adopted.** The dossier is not in the repo; every position stands without it.
## Grade under CLAUDE.md §0.2: `paper` — a plan, not an execution artifact. Nothing here is built or run.

**The organising principle: by primitive and loop phase.** Each piece goes in the phase that already
owns its kind of work. The PDF's flowchart (*A Tells B About C*: seven stages, two gates, four loops)
re-describes what those phases already sequence, and two descriptions of one telling is an S defect
(§0.06). So the flowchart is an **audit list**, walked in every commit body (§7). The PDF is cited in
commit bodies only, never in code, and never as the reason a behaviour is correct (§0.05).

---

## 1. What is being built

```
 CHOOSE   opening_set: one tell Candidate per (C, B), B ∈ known persons present   (T4)
          said_of → Said, carried as operands["said"] → Act.payload["said"]       (T1)
          clause 4: belief_contradicts reads LedgerReader(weigh = teller_weight)   (T3a)
          score term 2: regard by role polarity                                     (gated: G2)
 RESOLVE  fold: own_ledger ∧ with(to), else news.untold keyed holds|hearer          (T4)
          contest `a standing`: sides [A, B], obstacle = B's capability            (T4)
 WITNESS  hearers = co_located + witness_key, as today; no new channel             (T4)
          told deposit: Claim(chain = said.chain + (A,)); dedup by origin          (T3b, T5)
 READ     support over distinct origins; teller relation and record              (T3a, T6)
          regard = stored stance + judged deeds + told valence, never written      (gated: G1)
```

**The spine.** *A telling writes one thing: a claim in each hearer's ledger, carrying its chain.
Belief, regard, hostility and C's reply are computed from ledgers when read; none is written.* That
dissolves the H-79 failure that reverted plan position `10`, and honours AX-3.

## 2. Pre-flight

- **Shallow clone.** `cat .git/shallow`; on a shallow checkout `tests/valoria/test_forked_status.py`
  is red on arrival. That is the clone, not `main`.
- **Baselines before the first edit**, to the scratchpad: `python -m engine.season.harness.corpus_run 0`,
  `python -m engine.season.harness.register --requirements`, `python tools/m1_acceptance.py --summary`,
  `python -m engine.season.harness.aperture 1 0`, `pytest engine/season/tests/test_told_by_channel.py -q`,
  and the realm hash:
  `python -c "from engine.season.harness import populated as P; w=P.build_realm(0); P.run(1,0,w=w); print(w.content_hash())"`.
  Check each ran: output non-empty, the `tell` row present (§0.1 pt 3, row 4).
- **Scratch rule.** `m0_telling.py` and `t3_dump.py` live in the scratchpad, never committed; their
  output is cited in a commit body with its md5.

## 3. Shapes (the load-bearing specifics; paths under `engine/season/`)

| thing | shape | owner |
|---|---|---|
| `Said` | `NamedTuple(subject: str, predicate: str, value: Any, confidence: int, chain: tuple[str, ...], circle: tuple[str, ...] \| None)` | `state/carriers.py` |
| `said_of` | `(claims, subject, fx) -> Said \| None`; today's pick (newest non-`seen`, else newest) | `queries/person_q.py` |
| `Claim.chain` | `chain: tuple = ()`, origin first, replacing the `teller` field; `teller` becomes a property, `chain[-1]` or `None`; hops = `len(chain)` | `state/carriers.py` |
| told deposit | `chain = said.chain + (act.actor,)`; `visibility` stays `"own"`; confidence raw | `loop/witness.py` |
| `LedgerReader` | `(claims, weigh=None)`; `_best` groups matches by `value`; `support(v) = 1 − ∏ over distinct origins (1 − weigh(c))`, origin `chain[0]` (the holder, if firsthand); key `(support, when, confidence)`. At `weigh ≡ 1` it collapses to today's | `queries/person_q.py` |
| `teller_weight(p, fx)` | the `weigh` closure: firsthand 1.0, else `clamp01(told_weight ** hops · relation · record)`; `relation = 1 + rank_gain·rank + regard_gain·clamp(regard/STANCE_MAX, −1, 1)`, `STANCE_MAX = STANCE_VALENCE_SCALE ** 2`; `rank ∈ {−1, 0, +1}` from the hearer's own `office` claims; `record ≡ 1` until T6 | `decision/options.py` (`person_q` never imports `decision/`) |
| `regard(p, x, fx)` | `stance_toward + regard_gain·judged + lambda_teller·told_valence`; only the stored half exists until G1; `judged` has no relation factor, so regard never calls weigh | `queries/person_q.py` |
| `with` stem | two persons share `place_of`; UNKNOWN if either has none, and always UNKNOWN person-side | `data/requires.py`, `queries/world_q.py` |
| `tell` row | `requires_typed: {all: [{form: own_ledger, of: subject, conjunct: holds}, {form: relation, of: to, relation: with, conjunct: hearer}]}`, `counterparty: to`, `emits_on_refusal` keyed `holds`/`hearer` → `news.untold` (precedent: `issue`) | `verb_table.yaml` |
| `known_persons` | ids from truthy `exists:Person` claims, `Seen.who`, told `chain[-1]`; minus self and referent | `queries/person_q.py` |

---

## 4. THE POSITIONS — Batch 1 (`T0`–`T3b`) is the first committable slice

Every row is IN lane, OPEN. Size counts repo files touched; no time estimates.

| ID | position | what runs | `GATE` | falsifier | pins that can move | size | tier |
|---|---|---|---|---|---|---|---|
| **T0** | **M0 — measure** | scratch `m0_telling.py`, spying on `opening_set` over the corpus and the realm | clean tree | each counter asserts it counted (`tell` Candidates > 0, or the spy never attached); output md5 recorded | none | S · 0 | sonnet |
| **T1** | **`said` rides the Act** | `Said`; `said_of`; `opening_set` sets `ops["said"]`; WITNESS reads the payload | T0 | `test_told_by_channel.py::test_t1_what_hearers_receive_is_decided_at_choose_not_at_witness`: a claim appended to the teller's ledger after CHOOSE must not reach the hearer | none; hash **equal** (payload is not hashed); `redeposits == 0` | M · 7 | sonnet |
| **T2** | **pure moves** | `align` (+ `align_kind`) → `data/verbs.py`; `stance_toward` → `person_q`; AX-2 scan widened | T1 | H-66 sweep still flips P31 under `uniform`; `test_season_shape.py::test_t2_one_rebind_moves_score_and_gate` | none; hash **byte-identical** | M · 8 | sonnet |
| **T3a** | **weighed reader, on today's `teller`** | `LedgerReader(…, weigh)`; `teller_weight`; `belief_contradicts(…, fx)`; three fixtures | T2 | `test_told_by_channel.py::test_t3_a_firsthand_claim_holds_against_a_newer_told_claim_of_equal_confidence` (both arms); `::test_t3_unplanted_members_with_opposite_loyalty_reach_different_verdicts` (`checked >= 1`) | shipped: `CLAIMS BY SOURCE`, executed sets, H-40 sweep. Control: hash **equal** | M · 6 | opus |
| **T3b** | **`Claim.chain` replaces `teller`** | the field, the deposit, `said_of`, `soak.py`; origin and hops read the chain | T3a; tuple dump **first** | `t3_pre.json == t3_post.json` at control; `test_told_by_channel.py::test_t3b_a_two_hop_claim_weighs_less_than_a_one_hop_claim` | hash moves on **every** world by construction; shipped: T3a's pins | M · 5 | sonnet |
| — | **STOP. Batch 1 closes here** (§7) | | | | | | |
| **T4** | **`to`, presence, opponent** | `tell` row; `with`; `known_persons`; `operand_bags`; contest target = `to`; Decision 3 | Batch 1 | `test_sides.py::test_t4_a_tell_contests_against_its_hearer_not_its_topic`; `test_told_by_channel.py::test_t4_a_telling_to_an_absent_hearer_is_refused_and_a_present_one_hears`; `test_season_shape.py::test_t4_one_candidate_per_known_hearer` | `tell` executed count; `test_n3` floors; each counterparty row's opponent; R-09 | L · 10 | opus |
| **T5** | **dedup by origin** | the told-deposit skip | T3b | `test_told_by_channel.py`: one origin via two tellers deposits once; two origins outrank one (0.75 > 0.5 at `told_weight` 0.5); `redeposits == 0` | `CLAIMS BY SOURCE`; H-40 sweep | S · 2 | sonnet |
| **T6** | **a teller's record (E5)** | `record(p, x)`; fixture `record_gain` | T3b | `test_told_by_channel.py`: an unknown teller reads exactly `told_weight`; contradicted twice < confirmed twice; control tuple-identical | none at control | S · 4 | sonnet |
| — | **Batch 2 closes here** | | | | | | |

The mid-session file is the one the falsifier names (§0.4 cl.2).

### T0 · M0 — the measurement (scratch, nothing committed)

Open first: `harness/corpus_run.py`, `populated.py`, `aperture.py`, and `tests/test_governance_build.py`
(the spy precedent). Run `build_at(case, 0)` ×3 seasons per NPC-rung case and `build_realm(0)` ×1
through `make_chooser`; compute `judged` inline. Output `m0_results.json`, cited in T3a and T4.

| id | counts | "about zero" |
|---|---|---|
| M0a | `tell` Candidates and executed `news.told`, split by `subject in w.persons` | executed person-subject = 0 in both, **and** candidate share < 2% |
| M0b | share of (holder, person) pairs with `judged ≠ 0`, at `declared` and `uniform` alignment | < 5% at `declared` |
| M0c | person-keyed stance rows; how many name a faction leader | descriptive |
| M0d | share of `tell` acts with a known person present at RESOLVE; `known_persons` size by source | < 20% |
| M0e | per obligee, `inferred` claims about a person | decides G5 |
| M0f | `told_by` deposits, redeposits, firsthand-duplicate drops | descriptive |
| M0g | share of persons holding a `held_by` claim | decides G2's `holder` |
| M0h | contest Events whose claims name a party other than the actor | `stake` trigger |
| M0i | aperture `tell` row, executed ÷ attempted | default-obstacle trigger |

### T1 · `said` rides the Act

Open first: `witness.py` (`_told_content`, `told_by_event`, the told branch); `opening_set`;
`_payload_of`; `binding_of`; `soak.py::_act_row`. **Edit:** move `_told_content`'s pick into
`said_of`; where `row.requires_typed` holds an `OwnLedger` clause (walk the form, never the verb name),
`opening_set` sets `ops["said"]`, skipping on `None`; `binding_of` excludes `said`; `_told_content`
reads the payload; delete `told_by_event`. Hand-built `tell` acts in tests gain `payload["said"]`;
`test_seen_claim.py` retargets to `said_of`. **Asymmetry:** grep every `tell` Act construction,
`probes.py` included; `opening_set` and the test helpers must be the only writers. **[UNVERIFIED]**
that every soak-row reader tolerates a non-scalar operand. Changes nothing about who hears.
Subject: `[fix] told triple rides the Act; WITNESS stops reading the teller`.

**As built (`23bb90b`):** no decline on `said is None`. Measured: declining drops 3 of 31 corpus candidates
and moves the realm hash, because persons form `own_ledger` candidates on referents they hold nothing about
and the fold used to refuse them. It is deferred to T4 (below). `said_of`'s `fx` is unread until G3, and
`Said` carries no `circle` until G6 (a field lands with its reader).

### T2 · the pure moves

Open first: `options.py` (`align`, the recorded deferred move); `data/verbs.py` (imports,
`ALIGNMENT`); `person_q`'s charter; the two AX-2 scans in `test_season_shape.py`. **Edit:** `align` into `data/verbs.py`; derive
`KIND_VERB` (kinds emitted by exactly one row) and `EMITTED_KINDS` at load; `align_kind(kind, axis)` =
an authored `deed:<kind>` cell, else `align(KIND_VERB.get(kind), axis)`, else 0 (`deed:` keys admitted
only for `EMITTED_KINDS`; none authored); `stance_toward` into `person_q` unchanged; retarget
importers; `FORBIDDEN` becomes `("state.world", "queries.world_q", "queries.cache", "loop", "seam",
"combat_seam", "shape")`; rebinding tests target `data.verbs.ALIGNMENT`. **Asymmetry:** exactly one
`ALIGNMENT` attribute (grep assignments, `monkeypatch`, `setattr`).
Mid-session: `pytest engine/season/tests/test_season_shape.py -q -k "alignment or h146 or ax2 or person_q"`.
Subject: `[cleanup] align to data/, stance_toward to person_q, widen AX-2 scan`.

**As built (`1acf629`, corrected at the Batch 1 close `02151c7`):** the AX-2 scan became an ALLOW-LIST (`queries`
forbidden, `queries.person_q` admitted), not the deny-list tuple prescribed above, because the prescribed one admitted
`queries.faction_q` (which imports `World`); `test_person_q_cannot_reach_the_world_side` became an allow-list too, with
a floor on the in-package imports it resolves. `runs/results.json` was re-derived (probe P28's function count).

### T3a and T3b · the reader, then the chain — split, and why

The dossier fused these under H-157, but **that rule forbids a carrier before its reader, not a reader
before a carrier.** `Claim.teller` exists today, unread, so the reader can land first on it (a told
claim is one hop, its origin its teller). Each commit then has one mechanism and one clean control: T3a
changes no `Claim` field, so the hash at control is valid; T3b changes no reading at control, so the
tuple dump is. Fused, neither holds.

**T3a.** Open first: `Claim`; `LedgerReader._best`; `belief_contradicts` and its call in
`opening_set`; every `.confidence` reader. **Edit:** `LedgerReader` and `teller_weight` per §3, origin
= `c.teller` or the holder, `relation` reading `stance_toward`, `record ≡ 1`; `belief_contradicts(…,
fx=None)`, fed by `opening_set`. Fixtures: `told_weight` (control 1.0, shipped 0.5, sweep
[1.0, 0.5, 0.25]); `rank_gain`, `regard_gain` (control 0, sweep [0, 0.5, 1.0], shipped from the sweep;
[ASSUMPTION] 0.5). Three `assumption` H-rows, and an `absent` row for `stake` with its marker in the
`relation` product. **Asymmetry:** `confidence` stays raw; the body says so per reader. Second
falsifier: in `build_realm(0)`, two members of one faction with opposite-sign stance rows toward its
leader, one planted told claim from the leader against a firsthand claim both hold; verdicts differ at
`regard_gain` 0.5, agree at control. If the H-40 sweep reddens, re-argue H-40's row, never the
assertion. Subject: `[design] hearsay weighed at read on Claim.teller (H-157)`.

**As built (`4244d94`):** `belief_contradicts(…, weigh=None)` takes the closure, not `fx` (an import cycle:
`decision.options` imports `epistemic`); `regard(p, x)` takes no `fx` until G1. `rank` reads 0 (absent row H-180:
an ordering exists in `offices.yaml` but nothing deposits an `office` claim), so `rank_gain` (H-177) is dormant.
The second falsifier holds `told_weight` at 1.0, because at the shipped 0.5, while `rank` reads 0, a one-hop
claim reaches at most 0.5 × 1.5 = 0.75 < 1.0, so no regard can make hearsay beat a firsthand claim; regard
decides only between told claims, which `test_t3_regard_decides_between_two_told_claims_at_the_shipped_weights`
observes. `told_weight` 1.0 is a control only with both gains 0.

**T3b.** **Before any edit**, scratch `t3_dump.py` on the pre-edit tree (corpus ×3 seasons per NPC-rung
case, realm ×1): per person, the sorted `(subject, predicate, value, when, source, confidence, teller)`
tuples and, per held `(subject, predicate)`, what `LedgerReader.read` returns → `t3_pre.json`, md5
recorded. **Edit:** per §3 (`chain` field, `teller` property, the deposit's `chain=` keyword);
`said_of` copies `c.chain`; `soak.py` adds `"chain"`, keeps `"teller"`; origin and hops read the chain.
Re-dump at control, `chain[-1]` in the `teller` slot → `t3_post.json`; **the files must be equal.**
**Asymmetry:** grep `teller=` and any positional 11th argument to `Claim(`, tests and `probes.py`
included. The body says the hash moves on every world by construction; rollback is the control
fixtures, *measured* by a re-dump.
Subject: `[design] Claim.chain replaces teller; hops read from the chain`.

### T4 · `to`, presence, opponent

Open first: `verb_table.yaml` rows `tell`, `give`, `petition`; `VerbRow` and keyed refusals;
`writ_sourced_operands`; `operands_for`, `_derive_operand`, `opening_set`; `REQUIRES_STEMS`;
`WorldReader.read`'s `present_at` branch (and the trap note on it in `epistemic.py`); `resolve.py`'s
`_target` line; `sides_of`. **Edit:** row, stem and `known_persons` per §3; roster
`known_person_operands: {values: [to], claim: {...}}`; `operand_bags(...) -> list[dict]`, one bag per
known person, `operands_for` returning the first for existing callers; `opening_set` iterates bags,
still declining `to in (None, p.id)`; `_target = payload.get(row.counterparty or "subject")`; the
self-subject skip only when `not row.counterparty` (Decision 3). **Asymmetry:** the body lists every
`counterparty:` + `contests:` row and its new opponent (read `petition` closely). **Pins:** re-pin
`test_n3`'s floors at half the measured count, stating the mechanism (fewer formed, each addressed),
unless M0d < 20% (refused, §6); if M0d ≥ 20% and `attempt_cases` falls below its floor, stop: defect.
Re-measure M0a after. **Out of scope:** sigma's `REFUSED` raising uncaught for `tell` may surface. Subject: `[design] tell names its hearer: to, presence, opponent (ED-IN-0282)`.

**From Batch 1:** decide T1's deferred decline on `said is None` here (it changes who forms a `tell`). T0
measured (scratch `t0/`, md5 of `m0_results.json` 4e8fd3fa…): M0d is 12% on the realm, 100% on the corpus (one rung
by construction) and 78.2% pooled, so name the deciding instrument before re-pinning `test_n3` (the realm is the
shipped game; the corpus is a construction artifact); M0b is 49.3% pooled at `declared`, which meets G1's
trigger; M0h is 14 contest Events naming a person other than the actor, which meets `stake`'s trigger (H-179).
No told triple is deposited in either instrument (M0f), so the effects of T1-T3b appear only after T4.
`survey` and `reconstruct` also carry `said`, unread (their typed cell is `own_ledger` too), and
`opening_set` pays a `said_of` copy for each of their formed Candidates: when the `tell` cell gains
conjunct names here, gate `said` on that data-declared marker instead of on the clause alone.
A chain longer than one hop cannot form through the shipped path (terminal critique at the Batch 1 close):
a hearer of `news.told` holds the event-kind claim `(subject, news.told, True)` and the told claim at the same
tick, the event-kind one at `confidence_default` and first on a tie, so `said_of` picks it (empty chain) and the
next hearer's chain is `(teller,)`; the T3b retelling test sweeps `confidence_default` to 50 to reach two hops.
T5's falsifier needs a content retelling, so T5 decides whether `said_of` excludes event-kind predicates, as it
excludes `seen`. Read H-176's cite.

**As built (uncommitted at writing; the T4 commit):** the row, the `with` stem, `known_persons`, the roster and
`operand_bags` as §3 says, plus four things §3 did not name. (1) `act_key` (`data/verbs.py`) puts a known-person operand
in the act id (`subject>to`), because two `tell`s on one topic minted one id and `state/acts.py` refused the second on
the first realm season; every other row's ids are byte-identical. (2) `WORLD_ONLY_STEMS`: `LedgerReader` answers `with`
UNKNOWN by rule, since the fold's `with` read is deposited to the teller under `H-122`'s `actor` arm. (3) The loader's
"a contested row may not key its refusals" became "only to one kind" (`tell` keys `news.untold` twice). (4) The decline:
a NAMED `own_ledger` conjunct carries `said` and declines on `None`; `survey`/`reconstruct` stop carrying `said` and
form exactly as before. Decided instrument for M0d: the realm. Measured, realm `build_realm(0)` ×1: tellers 83 → 28 (only
a person who knows somebody tells), `tell` Candidates 266 → 378, attempted 25 → 4, `news.told` 9 → 3, told claims with a
chain 0 → 3; corpus `test_n3` loop: `attempt_cases` 20 → 20, `told_cases` 9 → 16 (no re-pin; §6). Re-run M0 (scratch
`t4/m0_telling_t4.py`, `m0_results.json` md5 `803755dd…`): M0a realm person-subject executed 2 of 3; M0d 100% of tellings
reaching RESOLVE have their `to` present in both instruments. Control: on one world, the 249,555 non-`tell` Candidates
are identical to `4bd5cee`'s.

### T5 · dedup by origin, and T6 · a teller's record

**T5.** The told dedup skips a deposit only if the hearer holds the triple with `chain == ()` or the
same `chain[0]`. Ledgers inflate (the eviction hazard), so re-run the H-40 sweep in this commit.
Subject: `[design] told deposits dedup by origin; support is noisy-OR over origins`.

**As built (the T5 commit):** the guard (`loop/witness.py`) skips only a held copy with `chain == ()` or the same
`chain[0]`; three falsifiers in `test_told_by_channel.py`. `said_of` is UNCHANGED, by ruling: the event-kind claim
`(subject, news.told, True)` is real tellable content, not noise. Measured at the shipped `confidence_default`: in the
realm and the corpus no told claim exceeds one hop (realm, 1 season: 3 chained claims, all length 1; 3 seasons: none;
corpus: 0 told claims), and `said_of` picks an empty-chain claim at all 378 / 1,480 / 16,810 calls (realm 1 season /
realm 3 seasons / corpus); where a teller holds both the event-kind claim and a told content claim at one
`(when, confidence)` (3 / 43 teller-calls) a newer claim wins. In `tiny_world` the tie goes to the event-kind claim
(chain `()`). So a content retelling cannot reach two hops at the shipped default; a fix is a design call, such as one
Candidate per held claim about the subject. Controls unmoved: realm hash `72af02fb…`, `corpus_run 0` md5 `125fd053…`,
PROBE FLIPS 0, `told_redeposits` 0, H-40 sweeps green.

**T6.** `record(p, x) = 1 + record_gain·(agree − dis)/(agree + dis)`, pairing p's claims told by x with
p's firsthand claims on the same `(subject, predicate)`, on `agreement`'s loop shape; zero pairs give
1.0 (deliberately unlike `standing_of`). Wire into `teller_weight`; fixture `record_gain`, control 0.
Subject: `[design] a teller's record weighs their hearsay (E5)`.

---

## 5. GATED — not scheduled

**The rule.** A field lands only in the same commit as its reader and its falsifier; an unfleshed
element is recorded by an `absent` row in `hole_register.yaml` plus a field-less `# ABSENT: H-NNN`
marker where it will go, never a dead carrier or a raising stub. §0.1 pt 5 forbids a guard over them,
so each trigger is a figure an existing instrument prints.

| ID | element | prerequisite | trigger | falsifier | marker site |
|---|---|---|---|---|---|
| G1 | judged regard | T2, T3b | M0b ≥ 5% at `declared` | no planted rows; two hearers, opposite `pursuits` on a deed's axis, same deed claim about X: `regard` signs differ; both 0 at control | `person_q.regard` |
| G2 | polarity in §F2 term 2 | T2, T3b (G1 if built) | none: after Batch 2, on the stored half | grudge on faction F: members choose `march` on F-held rungs more under `declared` than `legacy` (`checked >= 1`); `fight` against the disliked rises | `holder` operand (0 for Rung targets while M0g < 5%) |
| G3 | slant | G1 | M0a > 0 after T4 | the strongly valenced older claim is told under `valence`, the newer neutral one at control | `said_of` |
| G4 | C's move, **droppable** | G2 | M0a > 0 | two-arm count of C's acts naming A; **zero drops the row** | `questions_for`; `occasioned_by` branch [GAP] |
| — | ties | plan `14` (`_eff_tie`) | `aperture 1 0`: `tie / knot` executed > 0 | position `14`'s | none here |
| G5 | duty to report | T4 | M0e > 0 | an obligee forms a `tell` to the seat holder; without `oblige`, none | `_from_inferred_claim` |
| G6 | confidences | T4, G1 | M0a > 0 | a private telling deposits `visibility == (A, B)`; retelling outside it emits `confidence.broken` | told branch, circle line |
| G7 | deception | T6, G2, G3 | M0a > 0 | after two caught lies, the liar's `record` is below an honest teller's | `said_of` |
| G8 | letters | T4 | none; ahead of T5 if M0d < 20% | `create_record(letter)` + `give` deposits the said triple as `told_by`, chain ending in the maker | beside the `content:` deposit |

Other `absent` rows and triggers: `stake` (M0h > 0); a default-obstacle sweep (M0i after T4 no higher
than at T0); `Seen.who` as a source (only if M0d counts zero from it); sanctioned silence (`date.fired`
reaching WITNESS, plan position `22`).

## 6. M0 branches

- **Lands regardless:** T1, T2, T3a, T3b, T5, T6, G2 (stored half: loyalty and grudge rows are real), G8.
- **M0a ≈ 0:** G3–G7 wait; re-measure after T4 (it produces person subjects). Still zero: record on H-62; invent nothing.
- **M0b ≈ 0:** at `declared` only, G1 ships at control, or `deed:` cells are authored under H-66 in its commit (wait if plan `12c` is imminent); at both arms, G1 does not land.
- **M0d ≈ 0:** T4 lands, its `test_n3` re-pin is refused, and G8 moves ahead of T5 as the main channel.

## 7. Execution protocol

1. **Build** under `methodology-execute`, one `valoria-author` per position; no parallel write lanes
   (every position after T2 touches `options.py` or `person_q.py`).
2. **Close once per batch** under `methodology-close`: `pytest engine/season/tests -q -n auto` and
   `pytest tests/valoria -q -n auto` once (§0.4); `/code-review`, `/simplify`, `layer-conformance`
   (Lens A on T3a, B on T2); one terminal Opus `valoria-critic`. A red close re-runs only the failing file.
3. **No self-scheduling** (§11); **no guard over process** (§0.1 pt 5).
4. **Commits:** branch off `main`; `[scope] description`, subject ≤ 72 characters (each subject here is
   measured within it); stage only the position's files. Body: falsifier and outcome in both arms;
   every pin moved, with direction and mechanism; the stage-walk; a re-check of each `absent` row whose
   trigger this position's measurement touches; `ED-IN-0282`.
5. **IDs:** read `references/id_reservations.yaml` IN `next_free` (282 at `85afbf5`, checked
   2026-10-01), bump and co-commit in the **first** commit that cites it. H-176 onward comes from the
   tail of `engine/season/hole_register.yaml` at each landing, never pre-assigned. New numbers are
   fixtures tagged `[JUSTIFIED: H-NNN]`, control first, each with an `assumption` row (`site`, `sweep`,
   `default`, `unblocks`, a `cite` holding the ladder result).
6. **After each batch**, re-run §2's baselines; diff `CLAIMS BY SOURCE`, `DISTINCT EXECUTED SETS`, the
   `tell` funnel row and the hash (equal through T3a at control; different from T3b).

**The stage-walk key** (the flowchart as audit list):

| element | disposition |
|---|---|
| 1 · sourced claim; owner; C absent; ties | chain; partly G6; emergent; refused as a gate |
| 2 · licence; gate a · motive, cost, silence | composed (G5, G6, H-146); G2; emergent, no leak probability |
| 3–4 · tuning to B; stance detail; footing; quoting | refused; G3; refused; G7 |
| gate b · uptake; B closes; loops 3–4 | T4; emergent (`news.untold`); refused |
| 6 · competence, plausibility, sources, colouring | T3a, T6; clause 4; T5; G1 |
| 7 · belief; view of A; ties; norms; C's standing; onward | T3a–b; G1; plan `14`; emergent (N19 refused, AX-3); G1, no aggregate; the cascade, via the chain |
| loop 1 retell; loop 2 C learns | covered; emergent (G4 + G1) |

## 8. Expected effect on `python -m engine.season.harness.register --requirements`

Probably none. Its statuses are hand-written, validated for shape only; R-01/R-02 stay `not_met` on
their own instrument's break; R-07/R-08 move only with a new `measured:` line from a new instrument;
R-09 is re-measured at T4, not promised. Neither a change nor its absence is evidence (§0.1 pt 4); the
falsifiers and funnel diffs are.

## 9. Edits this workplan asks for but does not make

| edit | lands in |
|---|---|
| plan position `10` (`2026-09-28-the-plan-one-order-mc-v18-retired.md:193`): re-scope to "T0 → G8, this workplan; H-157, H-62, ED-IN-0282", plus a pointer to the `absent` H-rows | first commit; extended as rows land |
| plan position `14` (`:692`): keeps the tie effect; points at the ties `absent` row and at `known_persons`/G2 | T4, which writes that row |
| `engine/season/requirements.yaml:592`: "nothing writes it" is stale (`march`, `populated` write `stance`) | T3a |
| `verb_table.yaml` `tell` `contests_note`: position-10 paragraph superseded; "never a Person" → the M0a figure | T4 |
| `HANDOFF_IN.md` row 14 (stale `told_cases` floor; close it), row 17 (point here) | T4; first commit |
| `hole_register.yaml` H-157 (reader built), H-79 (`said`/`chain` touch no attribution rule), H-62 (the `tell` paragraph) | T3a; T3b; T4 |

## 10. Decisions

| # | decision | recommendation |
|---|---|---|
| 1 | **Private whispers** (heard only by the person told). Jordan's alone: it voids T-e (recipiency computed at WITNESS from presence) and T4 is redone | Do not build; absent that wish, nothing escalates |
| 2 | **Is the steering edit its own first commit?** | Yes: an `[editorial]` commit before T1 does §9's first-commit rows and allocates `ED-IN-0282`, so the bump lands before anything cites it (§4) |
| 3 | **Self-disclosure** (A tells B about A) | Allow: skip self-subjects only on rows without a counterparty; with `to` as opponent it is not self-contest, and `to == p.id` is still declined |
