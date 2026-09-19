# THE WORK ORDER — unit content for the seven items (2026-09-13)

## Status: **CONTENT OWNER.** Not an order — `workplans/2026-09-18-governance-settlement-behaviour-plan.md` owns the
## order (`RATIFIED`, `ED-IN-0215`). This file owns what each of these seven units IS: the
## `file:line`, the measurement with its control, the falsifier, and the corrections earlier drafts
## needed. Moved out of root `HANDOFF.md` on 2026-09-17 (`ED-IN-0242`).
## Owner: infrastructure / cross-cutting (IN lane)

**WHY THIS FILE EXISTS, and it is the reconciled program's own rule.** That program's header states:
*"Unit CONTENT stays with its owners: `2026-09-09-r-execution-plan.md` (U5–U10),
`2026-09-09-layer1-conformance-plan.md` (G1–G4), `proposals/2026-09-05-proceedings-subsystem/` (the
proceedings build order)."* The content of these seven units lived in root `HANDOFF.md` instead — a
continuity index — and so had no named owner in that list. It does now.

⚠ **THIS WAS NOT DUPLICATED CONTENT, and a trim nearly deleted it on that belief.** The program's
rows for the same work are one-liners (*"W28-cast | author the `cast:` blocks and their reader"*);
what follows is the diagnosis behind them. A session that reads root's *"THIS IS AN INDEX, NOT AN
ORDER"* disclaimer and concludes the detail is redundant is about to lose it.

## Where each item sits in the ratified order

| this file's item | position in the reconciled program |
|---|---|
| 1 · the counterparty | **DONE 2026-09-13**; closed R-06 · R-07 · half of `W27` |
| 2 · the cast | **13** `W28-cast` |
| 3 · `H-71` | **13b** — added post-ratification 2026-09-17 (`ED-IN-0242`), on Jordan's instruction to fix the gap. It was in NO position; it is a tier-0 `grade: absent` hole with its own falsifier |
| 4 · the 20 silent verbs | **14** `U7-own` · **19** `U7-remit` · **19b** `U7-disp` — R-05's body is split across three positions |
| 5 · the antonym residue | **14** `U7-own` (the antonym pairs) · **15** `Record-kind fold` (the Petition/Dispensation precondition `ED-IN-0211` names) |
| 6 · `Tenure.term` / `T-n` | **3–7**, the gate contract — `_part2` carries the `T-n` clause quoting `04:529-534` |
| 7 · the strategic layer | **20** `U9 / R-04` |

⚠ **THE MAPPING IS THE POINT OF THE TABLE.** A 2026-09-17 pass grepped the program for the literal
strings `W27`, `H-71`, `R-05` and `Tenure.term`, found zero hits, and reported four items as having
no owner in the ratified order. **Three of those four are in it under different names** — the rows
above. Testing a token where the claim is about a concept is the error `CLAUDE.md` §0.1 pt 3 row 1
names: an absence is the cheapest claim to make and the hardest to see wrong.

---

## §2 · THE ORDER — do these in this sequence

| # | do this | closes | falsifier | size |
|---|---|---|---|
| ~~1~~ | ✅ **DONE 2026-09-13** — the counterparty. Each person now holds their OWN Proposition naming another PERSON, with the case's own want | R-06 · R-07 · half of `W27` | **acts** naming another person **0 → 256**; distinct behaviours **25 → 43** | **S** |
| **2** | **The cast.** Port `harness/populated.py`'s per-case cast into `build_at` — one named person per case, seated by institution | `W27` · R-06 · R-07 · `A3` | `build_at` seats > 3 named people; `RANKING DISCRIMINATION` moves | **M** |
| **3** | **`H-71`.** 5 verbs are foldable and never attempted. ⚠ *Downstream of Arc 2* | R-05 · `H-71` (tier 0) | ✅ **DONE 2026-09-18.** `test_no_person_can_choose_a_governance_verb_and_h71_is_why` went red as predicted and is now `test_a_holder_can_now_choose_the_governance_verbs_their_office_grants` | **M** |
| **4** | **The 20 silent verbs.** 20 of 38 carry no predicate and no effect | R-05 · `H-62` (tier 0) | `WHERE THE 38 GO`: the 20 shrinks | **L** |
| **5** | **The six antonyms.** `ED-IN-0210` Ruling 2; none of the 9 verbs exists | R-05 · relations that end | the 9 appear in `verb_table.yaml` and execute | **M** |
| **6** | **`Tenure.term`.** `T-n`'s unbuilt half — `Tenure` has `until`, not `term` | R-05 · relations that lapse | a `Tenure` matures a declared term at a later tick | **M** |
| **7** | **The strategic layer.** 54 of 143 cases unrepresentable; the loop runs at person/settlement/realm only | R-04 · `W10` · `W13` | `unrepresentable scales:` shrinks below 54 | **XL** |

### 1 · THE COUNTERPARTY — one authored value, then the authoring
`engine/season/harness/corpus_run.py:297` — `Proposition("prop_x", "OUGHT", ids[chain[0]], "a standing
ambition", True, 0)`. The third argument is a **rung** id and the fourth is **one string for all 143
people**. Make the subject a **person** and every committed person's Q4 question refers to a person.
**MEASURED 2026-09-13 THROUGH THE SEASON DRIVER, WITH A CONTROL** — 27 NPC cases run end to end in
both arms:

| arm | acts | naming another person |
|---|---|---|
| control — `prop_x.subject` = a **rung** | 443 | **0** |
| arm — `prop_x.subject` = a **person** | 638 | **168** |

⚠ **THE EFFECT IS LARGER THAN THE CLAIM THIS REPLACES.** The previous text said *"same 84 candidates —
the **referent** changed"*. At the ACT level the count is not the same: **acts rise 44%**, because
person-subject questions open verbs that were unreachable. The candidate-level figure could not be
reproduced — reconstructing `assemble`/`opening_set` by hand raises `Ungraded`, and a first attempt
that appeared to confirm it had silently passed `View=None`. **Use the driver, not a reconstruction.**

Nothing is added — `Proposition.subject` is an unconstrained `str`, and `decision/options.py` resolves
`subject`/`to`/`site` to that one referent. **Q4 is the only door**: Q2's guard
`c.subject == p.id or c.subject in mine` bars the others.

⚠ **19 OF 46 NPC CASES DO NOT BUILD AT ALL** — they are faction-scale and `build_at` refuses them.
That is R-04 (item 7) reaching into items 1 and 2: whatever the cast work achieves, it reaches 27 of
46 NPC cases until the re-scale lands. The order below does not currently account for that.
**Traces to** `ED-IN-0210` Ruling 1 — *"verbs invoke mechanisms or interactions between a character and
another entity/character. they are not fiats."*
⚠ **The one-line change is not the deliverable.** Deciding *which* Propositions name persons in which
cases is. `harness/populated.py` already does this for the 46 NPC cases (`wants_of` reads the case's
first `core` need; `concerns_of` resolves `who_acts`), which is why item 2 follows immediately.

### 2 · THE CAST — `W27`, narrowed to the NPC lane
`build_at` still does `for n, pid in enumerate(("p_a", "p_b", "p_c"))` — three anonymous people, same
rung, all 143 worlds. **Every number in R-01, R-02, R-06 and R-08 was measured on that.** `§0.1 pt 4`:
a number without a control is not a measurement.
The machinery exists and is proven: `harness/populated.build_realm` seats **46 named people across 26
buildings** from `who_acts` and the corpus's own names, and is wired into no gate. The work is porting
it per-case into `build_at`.
⚠ **`PLAN.md` makes `W27` depend on `W28` (143 authored `cast:` blocks). That does not bind the 27
NPC cases that build** — `populated.py` resolves a cast without authored blocks (11 named ties, 15 institutional).
`W28` remains required for the 97 ARC cases, which name situations, not people.
⚠ **`PLAN.md`'s stated proof bar is spent**: *"distinct executed sets > 2 (2 today)"* reads **25**.
Use `RANKING DISCRIMINATION` and the R-06/R-07 rows instead.

### 3 · `H-71` — 5 verbs built and unreachable
`hole_register.yaml` `H-71`, **tier 0, `grade: absent`**. §F1 clause 2 evaluates eligibility
person-side; `remit:<act>` cannot be, because the person holds the `hold` Tenure while the **office**
owns the remit. `person_side_eligible` declines every `remit:` alternative unconditionally, so a verb
whose ONLY eligibility is a remit is unreachable **even where the actor genuinely holds the office
whose remit names the act**. `H-71`'s own `unblocks:` says **9 of 32 verbs — 8 remit-ONLY, plus
`levy`**; the in-tree falsifier scopes to `stratum == "binding_decision"` with all-`remit:`
eligibility and asserts `>= 7`.

⚠ **THE FIVE-NAME LIST THIS ENTRY FIRST CARRIED WAS WRONG IN TWO PLACES, which is precisely the
failure its own "do not re-derive" warning is about — so the correction stays.** The set
`{confer, convene, destroy_record, dispatch, revoke}` is right as *"foldable but never attempted"*
(`corpus_run`'s `WHERE THE 38 GO`), but the LABEL was false for two of them:
**`dispatch` has no effect body at all** (`effects.py:88-89`: *"`dispatch` needs none: Part E gives it
`writes: []`, so an order is an EMISSION and nothing else"*), and **`destroy_record` has no `remit:`
alternative**, so `H-71`'s mechanism cannot be why it is unreachable — its eligibility is
`["hold:<record>", "presence"]` and it declines on **both**, which is **`H-75`**, a different hole.
⚠ **Do not re-derive `H-71`.** Three sessions have now independently "found" it, this entry included.

### 4 · THE 20 SILENT VERBS — R-05's main body
`WHERE THE 38 GO`, measured 2026-09-13: **20 have no predicate and no effect**, 5 are item 3, 2 are
always refused (`work`, `examine` — no question these worlds raise refers to a Site), **11 execute**.
The SHAPE comes from `H-62` (tier 0): an interior write is a consequence of an outcome, declared in
`write_matrix.yaml`'s Degree-keyed `writes` column. The column exists; the rows do not.
⚠ **BUT `H-62` IS NOT R-05's BLOCKER and this entry first implied it was.** `H-62` is
`kind: PRODUCER ×5` over **Person interior fields** (`convictions`, `beliefs`, `scar`, `axis_count`,
`stance`) and `requirements.yaml` assigns it to **R-06 and R-08**. **R-05's own `blocks:` is
`[W10-core, H-65, H-94]`** — none of which appears anywhere in this order. Writing 20 predicates
closes `H-62` only for those verbs that write a Person interior field.

### 5 · THE ANTONYM RESIDUE — and it is THREE cases, not six, and NOT six new verbs
⚠⚠ **THIS ENTRY ORIGINALLY INSTRUCTED A LAYER-1 VIOLATION AND THE CORRECTION IS THE ENTRY.** It read
*"the six antonyms… none of the 9 verbs exists… falsifier: the 9 appear in `verb_table.yaml` and
execute"*, citing `ED-IN-0210` Ruling 2. The nine spellings ARE absent — that fact checks out. **The
disposition does not**, and the successor was not cited:

- **`ED-IN-0211`**, `status: closed`, filed the same day *to adjudicate ED-IN-0210*: *"**THE ANTONYM
  CLOSERS ARE NOT SIX NEW ROWS**… Jordan's six names remain useful as the IDIOM for what each closure
  means; **they are not six rows**. `establish <-> abolish` is the one genuinely uncovered case"*, and
  *"the antonym half is real and **already spelled by `release`**."*
- **`01_AXIOMS.md`**: *"**CLOSURE IS NOT A VERB. IT IS A CONSEQUENCE OF OWNERSHIP.** Asking *which
  verb ends an `oblige`* is the wrong question."*
- **`04_CODE_ARCHITECTURE.md` row 14**: *"four closing verbs missing | **one `release` verb**,
  eligibility `own`, generic over kind."*
- **`release` EXISTS, `grade: "ruled"`**, `domain: [hold, commit, oblige, succeed, tie, knot]`, and
  executes in 15 of the 89 live worlds (20 acts over the 27 NPC cases, measured 2026-09-13).

So **WAIVE, DEPOSED, FRAY and LOOSEN name closures `release` performs today** — "relations stay
one-way" is false for `oblige`, `succeed`, `tie` and `knot`. ED-IN-0210's premise (*"grep release finds
nothing"*) was true on 2026-09-10 and falsified by a merge on 2026-09-11.

**THE GENUINE RESIDUE IS THREE:** `issue`↔RESCIND · `petition`↔WITHDRAW/DENY · `establish`↔ABOLISH.
`ED-IN-0211` names the **precondition** for the first two: the Petition/Dispensation carrier conflict
(`04:180` row 11 against `write_matrix.yaml:224`/`:112`). `utter` stays unpaired by §14 — a Proposition
is immutable.

### 6 · `Tenure.term` — `T-n`'s unbuilt half
**Verified 2026-09-13: `Tenure` carries `(id, subject, object, kind, since, until, degree, payload)` —
there is no `term`.** `until` is a hard end, not a declared term. MATTER already matures act-declared
stages at a later tick and stops if the maker is gone; the same branch on a `Tenure` is the change.
`T-o` constrains it: the opening act declares *when*, the **Seat** declares who may end it early.

### 7 · THE STRATEGIC LAYER — R-04
**54 of 143 cases unrepresentable**: 44 at faction scale, 10 at world. The loop runs at person,
settlement and realm only, so the half of the premise that fuses personal with strategic has no
expression in the head. `W28`'s `world` half is already decided and not escalated (`PLAN.md`: a
`world` case is ≥2 realm Rungs under a shared container). **XL, and it should follow 1–6, not precede
them** — a strategic layer over three anonymous people measures nothing.

---

---

# WHY THIS ORDER, AND WHAT ITS INSTRUMENTS UNDERSTATE

Moved from root `HANDOFF.md` 2026-09-17 (`ED-IN-0242`) — it argues about the ORDER and about `requirements.yaml`, neither of which a continuity index owns.

## ⚠⚠ THIS IS AN INDEX, NOT AN ORDER. THE ORDER IS RATIFIED AND LIVES ELSEWHERE.

**`workplans/2026-09-18-governance-settlement-behaviour-plan.md` — *"every live item, in one order, across every lane"*,
`## Status: RATIFIED 2026-09-12 (ED-IN-0215)`, 27 positions — IS THE SINGLE OWNER OF THE ORDER.**
The first draft of this section was a *third* ordering surface that did not name it, and an
adversarial pass overturned it on exactly that.

⚠ **BUT THE OWNERSHIP CLAIM ABOVE OVERCLAIMS, MEASURED 2026-09-17 (`ED-IN-0241`).** Grep the reconciled program for §2's seven items: **`W27`, `H-71`, `R-05` and `Tenure.term` appear ZERO times in it.** So this section is NOT a redundant index — for four of its seven items it is the only place the work is stated, and compressing it into a pointer would delete them. Two readings, and the difference matters: either the ratified program owns the order of *the items it carries* and these four are outside it, or the program is incomplete and they belong in it. **The second would mean editing a RATIFIED document, so it is Jordan's.** Until then, do not treat this section as duplicated content, and do not let its own disclaimer talk you into deleting it — a trim that reads this heading and believes it would lose four work items. Re-derive with a grep before trusting either side. **If you are choosing what to do next, open the
reconciled program.** What lives here is an index into it: where this session's work landed, and the
measured state of the tree that a reader needs before position 1 makes sense.

⚠ **AND THE RATIFIED ORDER PUTS ARC 2 FIRST, WHICH THIS SECTION ORIGINALLY HAD BACKWARDS.** Positions
3–7 are `G1a · G1b · G2 · G3 · G4` — the gate contract — *before* `U5` (10), `U6` (11) and
`H-62-rest` (12). `ED-IN-0212`'s reason: effects mutate inside the gate's `apply()` closure while
`04 §C.2:536` has the gate compute before/after itself, so **the gate's signature IS the effect
contract and 11 effects are already on the wrong one.** Anything that writes an effect — governance
verbs, the 20 silent verbs, antonym closers, `Tenure.term` — is downstream of that. A session that
starts with a verb is paying for the rewrite twice.

⚠ **ITS OWN STATUS LINE RECORDS A LIVE COLLISION**, and it is not this file's to settle:
*"§0's claim to be the single owner of the ORDER across all lanes is **contested** —
`workplans/2026-09-11-arc-sequence-spine.md` positions 2–15 remain independently actionable, and
`valoria_master_workplan_v7.md` §6 records that the collision is open and needs a commit rather than
a paragraph."*

⚠ **THE `measured:` BLOCKS IN `requirements.yaml` ARE STALE IN THE DIRECTION OF UNDERSTATING PROGRESS.**
Re-measured 2026-09-13 by `python -m engine.season.harness.corpus_run`: R-01's row says R3 passes
*"22/30 NPC and 34/59 ARC"*; the run prints **30/30 and 56/59**. R-08's row says candidate ties break
*"ALPHABETICALLY BY VERB"* with *"only 2–7 of 22"* candidates scoring; the tie is **broken by the draw**
(U4/H-96). `PLAN.md`'s `W27` proof bar — *"distinct executed sets > 2 (2 today)"* — read **25** before
this session and **43** after it. **Re-run the instrument before you plan against a row.**

⚠ **THREE CORRECTIONS AN ADVERSARIAL PASS MADE TO THE PARAGRAPH ABOVE, kept because each is a trap
the next reader would fall into as well.** (1) **R-08 is not stale in the direction claimed** — the
same row retracts itself at `requirements.yaml:452-463` and R-06 at `:396` already carries
*"7..11 of 28 -> 16..22 of 28"* from `U3`. A figure already written in the file was presented here as
a fresh re-measurement. (2) **"16..22 of 28" has a per-case denominator** — `corpus_run.py:579` prints
`sep[0][1]`, the FIRST case's candidate count, not a corpus-wide one. (3) **R-01's replacement has a
denominator clash**: 30/30 + 56/59 is out of **89 live worlds**, while `:265` and `:524` count *"84 of
143"* — **cases**. `requirements.yaml` carries **four mutually inconsistent R3 figures** (`:142`,
`:265`, `:333`, `:524`) and nothing says which is the baseline. That is the real finding, and it is
bigger than any one stale row.

---
