# SC-02 — where `reception` and `proofs` read under option B: the actor's own ledger, and the bench's public commits (F8)
## Status: PROPOSED (design-first; builds nothing; ratified on merge by ED-1094's default unless held back)
## Lane: SC
## Grade under CLAUDE.md §0.2: paper
## IDs allocated: none

Base read: `c0baed2c` (CR-96 landed). Instruction: `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-13.md` §2 SC-02. The rule applied is the F8 row of `architecture/meta/04_CODE_ARCHITECTURE.md` §B.2: the fold may ask the actor's own ledger, through the `PersonInterior` snapshot the act carries, and no other. The answer applied is ED-SC-0040's superseding row (option B). This file is reference (CLAUDE.md §0.05). The behaviour is right only if the falsifier in §3 passes once a builder writes it.

**What "the actor's own ledger" means in code.** No `PersonInterior` class exists, and `Act` has no slot for a snapshot. The tree's precedent is `loop/resolve.py::_confidence_broken`: it reads `w.persons[a.actor].ledger` live at RESOLVE and hands that ledger to a `person_q` function. This design takes the same reading. The actor is `claimants[0]` (`loop/sides.py::sides_of`: `claimants = [a.actor, target]`).

**What a commit is in code.** A `commit` is a `Tenure` edge (`kind == "commit"`, subject = the committer, object = a `Proposition` id). `loop/effects_information.py::_eff_commit` writes it into `w.tenures`, and it carries the Proposition's `(mood, subject, predicate, value)` in `w.propositions`. It is a World store, like the seats `judging_set` already reads. It is in nobody's ledger. Reading it reads no person's ledger, so the commit route keeps F8 whoever the actor is.

## 1. Term-by-term read: today, and after the re-source

The signatures gain the actor: `reception(w, target, venue, actor)` and `proofs(w, actor, opponent, venue)` (the second's speaker slot already holds the actor). `contest_input` passes `claimants[0]` as `actor`. For a `speak` the actor is the speaker. For a `determine` heard by a room (once CP-T05-01 moves its prize) the actor is the determiner, who sits on the bench.

### 1a. `queries/world_q.py::reception(w, speaker, venue)`

| # | term at the base | whose store it reads at the base | after the re-source |
|---|---|---|---|
| R1 | the bench: `judging_set(w, venue)` | `w.tenures`, `w.offices` (World; no ledger) | unchanged |
| R2 | each seated `h` once, skipping `h == speaker` | — | unchanged, with `target` in the speaker's slot |
| R3 | `attributed_deeds(h.ledger, speaker)`, the deed claims `h` holds of the speaker | **each judge's own ledger. For `speak` none of them is the actor, so this is F8's breach.** | **the own term:** read only for `h == actor` (and `actor != target`), on `w.persons[actor].ledger`. **the commit term:** for every other seated `h`, the Propositions in `h`'s live commits (§2), never `h.ledger`. |
| R4 | step 20's erosion: `suffered_deeds(h.ledger, speaker)` | each judge's ledger (breach, as R3) | kept inside the own term only (it is the actor's own ledger). The commit term carries no erosion: a commit is not a sighting, so there is no bluff to call on it. **Cost, stated:** step 20 no longer reaches a `speak`'s bench. |
| R5 | `v_h(c) = deed_term(h, projected_axes(h, shift), c)` | `h`'s pursuits and scar (the interior; not his ledger) | own term: unchanged. Commit term: `deed_valence(projected_axes(h, shift), P)` on the committed Proposition `P` (§2). This is the same valuation owner. It reads `h`'s interior, which F8 does not cover (the same kind of read as `_opposition_of` taking the subject's capability), and reads no ledger. |
| R6 | `remove_weight(c.source) · c.confidence / full` | fields on a claim in `h`'s ledger | own term: unchanged. Commit term: a live commit counts as a firsthand claim at full confidence, so weight `remove_weight("firsthand") · 1 = 1`. This adds no new number, but it is a rule choice: `[ASSUMPTION; medium; Jordan to correct; revert: the commit term counts 0 (reception reads the own term alone)]`. |
| R7 | `confidence_default`, `scar_weight_shift` fixtures | `w.fixtures` | unchanged |

So for a **`speak`** the bench reads only the commit term: what each seated member has bound himself to in public about the speaker. The speaker is not on the bench (R2), so the own term is empty. **No judge's ledger is read for `speak`.** For a **`determine`**, `reception(w, actor, …)` is the other judges' commit term about the determiner. The own term is empty there too (R2 skips the actor in his own slot). The own term appears only when the target is somebody else, which is CP-T05-01's `opposed` (§4).

### 1b. `queries/world_q.py::proofs(w, speaker, opponent, venue)`

| # | term at the base | whose store it reads at the base | after the re-source |
|---|---|---|---|
| P1 | `held = attributed_deeds(who.ledger, opponent)`, `who = w.persons[speaker]` | the speaker's ledger. `speaker` is `claimants[0]`, the actor, so this is already own-ledger. | unchanged. The parameter is renamed `actor` so that a call passing any other person reads as a defect at the site. |
| P2 | bench non-empty: `judging_set(w, venue)` minus the speaker | World | unchanged |
| P3 | the mirror: `{(c.subject, c.predicate) for c in opp.ledger}` | **the opponent's ledger: F8's sharpest breach (H-216 (7))** | **the opponent's commits:** `{(P.subject, P.predicate)}` over every live `commit` Tenure whose subject is the opponent (`P = w.propositions[t.object]`). The key is the same `(subject, predicate)` the base uses, and any value counts, as at the base (H-216 limit (2)). The opponent mirrors a proof by answering it on the record: a commit to a Proposition on that subject and predicate, for example a denial (`value` False). A non-person opponent has no edges and mirrors nothing, as at the base. |
| P4 | `remove_weight(c.source)` per unmirrored proof | the actor's own claims | unchanged |

**Consequence, stated: the mirror is no longer total.** At the base it zeroes every proof, because WITNESS deposits a doer's own act to him (H-216 (4); 49 of 49 at the B-P measurement). After the re-source it zeroes a proof only where the opponent has committed on that pair. §3's realm reading shows that no Proposition at seed 0 has a deed-kind predicate. So in computed play `proofs` becomes non-zero for the first time, wherever a `speak`'s actor holds an attributed deed of the subject before a seated bench. This is expected to be the build's largest realm mover (unmeasured; `proofs` last read at H-216), and the build declares it.

## 2. The route a bench member's commit gives

The source text (the obstacle reading live commits to a charge) assumes a charge carrier, and there is none (H-227). A bench member's commit gives this instead: **a public, live, owner-written binding to a Proposition whose subject is the target.** It is read off World edges at RESOLVE and needs no ledger.

**The read, which is all a builder needs:**

1. `bench = [h for h in dict.fromkeys(judging_set(w, venue)) if h in w.persons and h != target]` (R1, R2).
2. For each `h` in `bench` with `h != actor`, take the live commits `t` (`t.kind == "commit"`, `t.live`, `t.subject == h`) whose object `P = w.propositions.get(t.object)` exists, has `P.subject == target` and has `P.mood == "HOLDS"`. That last condition is H-227's testimony shape: *`target` did `predicate`*.
3. Each such `P` contributes `deed_valence(projected_axes(h, shift), P)`. `deed_valence` reads only `.predicate` and `.value`, which a `Proposition` has, so the one valuation owner is reused and no claim-shaped view is built. Its own rules then apply unchanged:
   - a predicate outside `DEED_KINDS` counts 0;
   - `value` other than `True` counts 0, so a bench member's public denial does not move the room `[ASSUMPTION; medium; Jordan to correct; revert: a HOLDS deed commit with value False counts the negated valence]`;
   - a `PAIRED_KINDS` predicate counts 0. A Proposition carries no sighting, so it names no doer of violence, the rule `attributed_deeds` keeps for a told copy.
4. If `actor` is seated and `actor != target`, add the own term: the base body of `reception` for `h = actor` alone, on `w.persons[actor].ledger` (attributed deeds, erosion, remove, confidence, `deed_term`).
5. `reception = Σ (2–3) + (4)`. It is signed, stores nothing, and returns `0.0` for a `None` venue, an unknown target or an empty bench, as at the base.

**What it excludes, and why:**

- **`OUGHT` commits count 0 in the room.** They are what a member wants done, and CR-34 counts them as votes, in `determine`'s `vote` conjunct at a `declared` sitting. Counting them here as well would put one commit in two operands of one verdict. It would also need a valence for a wish whose sign depends on whether the predicate harms its subject, a second ladder with no owner. This also closes the loyal-creed hazard: the realm's creed commits (`carries the creed of`, subject the leader, `OUGHT`) do not read as regard. `[ASSUMPTION; medium; Jordan to correct; revert: an OUGHT commit whose predicate names a verb contested against its subject (`VerbRow.opponent_operand() == "subject"`) counts −1 per commit, on a NUMBER row]`.
- **No reconstruction from the log.** Rebuilding what a judge saw from `w.log` and `epistemic.observers_for` would be a second store of the judge's knowledge, and F8 by another door. The route does not do it.

**For `speak`, then:** the bench reads its members' HOLDS commits about the speaker and nothing else. That is the answer to the instruction's `speak` question.

**How it composes with CR-96.** `_opposition_of` reads the subject's capability and his opposing attribute (`pool._opposing_attribute`, the row's `opposed_by` column, else the row's own). That is the subject's interior and no ledger, so F8 does not touch it, and the re-source leaves it alone. It stays the obstacle's base (`score/2`), and the room terms are subtracted after it in `roll.py::obstacle`, so the two compose by the existing formula. AM-D-02's guard (`opposition` `None` when `subject == claimants[0]`) sits beside it. Two names must not be confused: CR-96's `opposed_by` is an attribute column, and CP-T05-01's `opposed` is a room operand.

## 3. Falsifier, control, and the base reading

### 3a. The falsifier (a test the builder writes; nothing runs at this step)

File: `engine/season/tests/test_sc02_reception.py` (new tests beside the `22a` ones). Hand-built world: a venue `V` with a two-seat bench `{J1, J2}` (live `hold` tenures granting `determine`, offices scoped over `V`). Speaker `S` (the actor of a `speak` at `V`) and opponent `O`, both off the bench.

- **World A (opponent's ledger only).** `J1` holds one firsthand deed claim of `S`'s, an unpaired kind his pursuits disvalue (`deed_valence < 0`). `O` holds a claim with the same `(subject, predicate)` as `S`'s only proof against `O`. Nobody has a commit.
  - **After the re-source:** `reception(w, S, V, actor=S) == 0.0` (exact equality, not `approx`), and `proofs(w, S, O, V) == remove_weight(source)`, unmirrored. Neither `J1`'s ledger nor `O`'s moves anything.
- **World B (the own-commit route).** World A plus two edges: `J1` holds a live `commit` to `Proposition(mood="HOLDS", subject=S, predicate=<the same kind>, value=True)`, and `O` holds a live `commit` to a Proposition on the proof's `(subject, predicate)`.
  - **After:** `reception == deed_valence(projected_axes(J1, shift), P) < 0` exactly, and `proofs == 0.0`.
  - **Wrong if** World A's reception is non-zero, or World B's equals World A's. Planted failure: put `h.ledger` back in R3 and World A goes red.
- **World C (the own-ledger arm).** World A with the act a `determine` whose actor is `J1` (built by hand; CP-T05-01 has not moved the prize yet, so the test calls `reception(w, S, V, actor=J1)` directly).
  - J1's own claim counts through the own term, at `deed_term`'s value.
  - `J2` gets the same claim in his ledger, and the total does not change.
- **Ended commit.** World B with `J1`'s commit closed (`until` set) reads as World A.
- **One judge, two Propositions.** One judge's commits to two Propositions of the same (subject, predicate, value) count once: the route dedupes per judge by that key.

### 3b. Control

Run World A on the base commit `c0baed2c`, where `reception(w, S, V)` and `proofs(w, S, O, V)` take no `actor`. The base `reception` is non-zero and negative through `J1`'s ledger alone, and the base `proofs` is `0.0` through `O`'s mirror. The builder records both base values in the commit body. That is the control showing the opponent's ledger, and a judge's, moved the room before the re-source.

### 3c. Base reading, re-taken

**Instrument:** `build_realm(seed)`, one season through `harness/populated.run`, then `reception` for every (rung with a non-empty `judging_set`, person) pair. This is H-215's instrument, re-run at `c0baed2c`.

| seed | pairs | benched rungs | non-zero | + / − | H-215 figure (`cf10ec05`) |
|---|---|---|---|---|---|
| 0 | 33,034 | 398 | **4,958** | 1,678 / 3,280 | 925 of 30,888 |
| 2 | 33,034 | 398 | **3,317** | 842 / 2,475 | 2,099 of 31,363 |

The rise is consistent with H-215 (2): FI-02 and FI-03's found claims arrived after that reading. It was not decomposed here.

Commit edges at the same reading:

| seed | live commits | commits on a Proposition about another person | of those, by a seated bench member | (rung, target) pairs they touch |
|---|---|---|---|---|
| 0 | 185 | 86 | 18 | 1,607 |
| 2 | 171 | 86 | 15 | 1,563 |

At seed 0, the full split was taken: 177 of the live commits are `OUGHT` and 8 are `HOLDS`. None of the `HOLDS` commits is about a person, and none of the 143 Propositions has a predicate in `DEED_KINDS`. At seed 2 only the six most frequent `(mood, predicate)` keys were read, and all are `OUGHT`. **Expected realm reading after the build: `reception`'s commit term is 0 on every pair at seed 0 (and expected so at seed 2), because no HOLDS commit about a person forms in computed play (H-227: testimony is hand-built only).** For `speak`, `reception` then reads 0 in the realm until a computed testimony route exists. That is option B's honest price, and it is to be stated, not hidden. The builder re-takes the same table after the build, and the exit needs both counts.

## 4. Hand-over notes

**To the build of SC-02.** The commit is `[fix] SC-02: reception and proofs re-sourced from commits (F8, option B)`. The work is the signature change in §1, the read in §2, §3's tests, and re-recording the `22a` tests that read `reception` or `proofs`:
- `test_sc02_17_*`: their benches move a ledger, so they become own-term or commit-term worlds.
- `test_sc02_18_*`: their mirror becomes the opponent's commit.
- `test_sc02_20_*`: erosion survives in the own term only.

`seam/wrappers/sigma.py`'s docstring and H-215 (7) / H-216 (7) are amended to say F8 holds. Stop if any term needs `h.ledger` for `h != actor`.

**To CP-T05-01 (`opposed`).** `opposed = reception(w, opponent, venue, actor)`, with the opponent in the target slot.
- For a `determine`, the determiner is seated and `!= opponent`, so `opposed` = his own ledger's attributed deeds of the party (the own term, F8-admitted) plus the other judges' HOLDS commits about the party.
- For a `speak`, `opposed` is the commit term alone. So `speak` gains the term on this route without reopening F8.
- AM-D-03 limit (1), "character as evidence", now reads as follows. For a `determine`, it holds for the determiner's own record of the party. For the rest of the bench, it holds for what they have bound themselves to in public. Its realm reach is near 0 until testimony forms (H-227).
- The CP-T05-01 falsifier's "one judge holds one firsthand deed claim" world is valid only with that judge as the `determine`'s actor. For a second judge, use a HOLDS commit.
- Do not exclude kinds from `opposed`.

**To CP-T05-02 (i) (`hearing`).** AM-D-01's `hearing` counts band claims in every seated judge's ledger, which is the read F8 forbids for any judge but the actor. On this route:
- `hearing` reads the **determiner's own ledger only** (the act is a `determine`, after CP-T05-01): the `a matter` band claims he holds on the matter, weighed by AM-D-01's `remove_weight · confidence/full · max(DEGREE_STEP[band], 0)`, signed as AM-D-01 says.
- For a `speak`, `hearing` is `0.0`. The other judges' memory of a hearing reaches the verdict only through what they commit to (the commit term), never through their ledgers or a log reconstruction.
- The home's two-judge falsifier is re-pinned to one judge, the determiner. With full confidence and the AM-D-01 re-pin, a determiner who witnessed two carried speeches by others reads `hearing` = 2. The builder confirms this after settling the `[UNVERIFIED]` deposit-subject question.
- A second judge's ledger moves nothing: that is the falsifier's new wrong-if.

## 5. Hash

- **Now:** none. This commit is a design file.
- **When built: MOVER, declared.**
  - `reception`'s inputs change wherever a `heard_by: bench` contest reads it. At the base that is `speak`, and `determine` after CP-T05-01.
  - `proofs` is un-mirrored in computed play (§1b), which moves the composed obstacle wherever the actor holds an attributed deed of the subject before a seated bench, within the `H-213` ceiling and the per-pool arm.
  - The re-pinned pins are named old to new in the build commit's body: `engine/season/tests/test_season_weather.py::BASE_HASHES` (the 1- and 2-season realm hashes H-215 cites) and every seeded golden under `engine/tests/` that a moved `speak` band reaches, found by running them on the build.
  - Revert: `reception_gain = 0` and `proof_step = 0` give the no-room control. They are not a revert of the source.
