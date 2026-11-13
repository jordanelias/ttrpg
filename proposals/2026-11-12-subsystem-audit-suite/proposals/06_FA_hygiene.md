# FA-P5 — hygiene: stale register rows, the refusing clause, unreached queries, two names, retired contract rows

Reconciled: 2026-11-12, wave 3 (W3-3) — item 4 WITHDRAWN: the kind rename `dispensation` → `writ` by D-U1-11h (the roster key stays `dispensation`, the cited key of `read_to_addressee`, D-U1-05; prose says "writ", and "decree" for one proclaimed, A-21; a rename would move every hash for a word), and the verb rename `oblige` → `swear` by R3 §1's Option B (the verb and its Tenure kind keep one name, `04` §B.7 "`oblige : Person -> Seat`"; the glossary's *sworn* row reads off a live `oblige`). Item 3 gains the sentence R3 §1 asks for (Option A: `Faction.holdings` is the surviving named access, `04` §B.6.1). With item 4 gone the proposal declares no hash mover. Batch, dependencies and tier added (U3 B03; R3 7b-0).

Reconciled: 2026-11-12, U6 repair lane R-A (`unified/U6_VERDICT_AND_REPAIRS.md` finding 3; `U3_CONFLICT_LEDGER.md` C3-V3): item 3 now **keeps** the standalone `faction_q.holdings` and deletes `faction_q.superiors` only. Ladder step 3: `04` §B.6.1 names it as a function, "`holdings(faction)` is a **named Query**" (`04:318`; again `04:1245`), and the function was built for that row (`engine/season/queries/faction_q.py:159-163`, its docstring); step 4: `17_CENSUS_C1A_01_deletion_batches.md` keeps uncalled queries Layer 1 names (`:113-115`). `superiors` is named by no Layer 1 row (only by the governance plan's list, `faction_q.py:19-23`), so its deletion stands. The earlier "Option A" sentence (the `Faction` field is the surviving access) is withdrawn.

Reconciled: 2026-11-12, A-97: the `holdings(faction)` note cited above moved from `04:1244` to `04:1245` (PART D row 52 was inserted at `04:1082`, so every `04` line after `:1081` moved by +1; opened at `04:1245`). No clause of this file waited on a Layer 1 amendment.

## Status: PROPOSED

Lands in batch: B03 (hygiene, hash EQUAL), after `16_PESSIMIST_CORE_no_stored_plan` and before `09_WR_B_pointer_text_for_the_orchestrator`'s neighbours in U3 §1 item 4.
Depends on: nothing proposed (every symbol named is on `main`).

Source: `audits/06_FA_audit.md` F-FA-09 to F-FA-12, §6.2 R-09 to R-15, R-18.

## What it changes in `engine/season/` at runtime

Items 1, 2, 5 and 6 change nothing at runtime. Item 3 deletes one function nothing calls (`superiors`). Item 4 is
withdrawn (see the head), so nothing renames and no `World.content_hash()` moves.

## The problems (evidence), and the resolution for each

**1. Two register rows describe a tree that no longer exists (R-13).**
`engine/season/hole_register.yaml` H-230 (`:4863`) opens "IN-61 … STOPPED AT ITS DESIGN-FIRST STEP, UNBUILT"
and its `default:` says "`succeed` stays declined … no `successions` registry". At `601e715`:
`loop/effects_governance.py::_eff_succeed` (`:145-182`), `data/rosters.py::SUCCESSIONS`,
`state/gate.py::may_claim` (`:770-786`) and `death_subjects` (`:1819-1832`, which names each seat `hold` a
death closes so witnesses hold a claim about the seat) are all in the tree, and the batch card records
IN-61, CP-T02-01 and CP-T02-02 as landed at `f9e4cef`. H-206 (`:4551`) says the office and `hold` half of a
death is unbuilt; `death_subjects` is that half.
*Edit:* prepend each row's `hole:` and `cite:` with one sentence stating what landed and where, and set
H-230's `default:` to the built state; keep the measured history below it (the register's own R0 rule:
append, never rewrite the measurement). Ladder step 1.

**2. Three refusals name no clause (R-14, H-252).** `_req_confer` and `_req_establish` return a bare
`False` at each of their clauses (`loop/predicates.py:140-179`, `:366-425`), so `aperture`'s DECIDING READ
prints `no-read` (`establish` 7 of 7 and `release` 15 of 15 at seed 0, two seasons). `_req_release` and
`_req_revoke` already route each refusal through `_refuse(clause, ids)` (`:62-75`), which writes a trace
row and nothing else.
*Edit:* each `return False` in the two predicates becomes `return _refuse("<the clause, in the words of its
own comment>", f"{a.actor} …")`. No Event, no claim, no hash. `harness/aperture.py`'s `no-read` class then
reads the trace row for a predicate row. Ladder step 4.

**3. Unreached query surface (R-10).** `grep -rn "\.superiors(\|faction_q\.holdings(" engine/season
--include=*.py` outside tests returns nothing; `purview` and `subordinates` are read only by
`harness/interactions.py:123-127`.
*Edit:* delete `faction_q.superiors` with its tests (`engine/season/tests/test_faction_q.py:141`'s case, and the
`superiors` assertion of `:123`'s case, whose `subordinates` half stays; `:94`'s `holdings` case stays). *(U6 R-A, C3-V3:)*
**keep the standalone `faction_q.holdings`**: `04` §B.6.1 names "`holdings(faction)`" as a named Query (`04:318`), it
already reads `resolve(w, prop).holdings` rather than re-deriving the walk (`faction_q.py:159-163`), and an uncalled
Query Layer 1 names is kept (`17_CENSUS_C1A_01_deletion_batches.md:113-115`'s rule). Keep `purview` and
`subordinates`. Keep `head`'s `Tenure.degree` branch, which `04` §B.6.1 and §F.34 name, and add one line at
the site: unreachable until something writes a degree on a `commit`. Ladder step 5 (`ID-13`: a role no
caller requires is not declared).

**4. Two names that say the opposite of what the thing does (R-11, R-12; H-262, H-298). WITHDRAWN
(D-U1-11h; R3 §1 Option B).** The finding stands as vocabulary: a `dispensation` is an order where the
ordinary word means an exemption, and the verb `oblige` binds only the actor. The repair is in prose, not in
the roster: new suite text says "writ" for any `dispensation` Record and "decree" for one proclaimed by
`issue` (A-21; `U1_GLOSSARY.md` *writ*), and "swear" / "sworn" for the act of taking an `oblige` (the
glossary's *sworn* row). No roster value, Event kind, verb row or cell changes, so no hash moves. The two
renames formerly proposed here (kind `dispensation` → `writ`, Event `dispensation.issued` → `writ.issued`;
verb row `oblige` → `swear` with the Tenure kind kept) are not to be built: the first would move every hash
for a word and break the cited key of `read_to_addressee` (D-U1-05); the second would give one act-and-edge
two names (test 1). H-262 and H-298 are closed by this paragraph's prose rule, `[ASSUMPTION: the hole rows
accept a vocabulary closure — basis: D-U1-11h's decision is the vocabulary owner's]`.

**5. Contract rows for a retired faction (R-09).** `references/module_contracts.yaml` `modules:` carries
`faction_state` (`:127`) and `faction_politics` (`:797`) with stored state ("faction stats 1-7",
"Standing", "Coup posture"), Key-registry vocabulary and `doc:` pointers into `.designs/`. The stat-vector
faction was deleted at plan position `29b`, the Key substrate retired by ED-IN-0232, and no code under
`engine/season/` or `modules/` implements either row. Known readers of the names:
`tools/build_engine_atlas.py:179`; `engine/season/manifest/registry.py:55-58` parses the `modules:` list.
*Edit:* in one commit, reduce each of the two rows to its `module:` name and a one-line note (a faction is
`engine/season/queries/faction_q.py`'s view; it has no contract, no state and no composition role), and
re-point or drop `build_engine_atlas.py`'s `VALORIA_CONTRACTS` entry. Before the edit, list every reader of
the two rows' fields (`grep -rn "faction_state\|faction_politics" tools engine tests`) and name them in the
commit; this proposal found the two above and did not trace the workbench census. Ladder step 2.

**6. Two process rows.** `registers/handoffs/HANDOFF_FA.md` row 3 orders authoring a merge into a
quarantined `.designs/` file "in the same pass as E11", in the cell that says v9 schedules none (R-15).
*Edit:* delete the row; ED-FA-0021 stays ratified as intent, and what it intends is built as a fold by
FA-P1. The B10-17 card's CP-T09-06 row says `off_duke_valorsmark`'s conferral is `inheritance`
"replacing `appointed`"; `offices.yaml:206` reads `conferral: null` (R-18). *Edit:* the card's words become
"replacing `null`".

## Gate (execution artifact)

`python -m engine.season.harness.register --check` after item 1; `aperture 2 0` printing a clause in place
of `no-read` for `establish` after item 2; the `engine/season/tests` files that import the deleted
functions pass after item 3; item 4 has no check (withdrawn); the two-season `build_realm(0)` hash is
equal before and after the whole proposal; `tools/valoria_local.py --staged` after items 5 and 6.

## Falsifier

For item 3, a grep that finds a caller is the falsifier, run before the deletion. For the proposal as a
whole, any change of the two-season `build_realm(0)` hash means an edit moved behaviour, and that commit is
wrong.

## NERS reading

Not a design object. E alone would be the wrong reason to do any of it; the reason is that a register row
that says a built thing is unbuilt, and a contract that describes a deleted module, mislead the next reader
of a repository that has no memory between sessions.

## Cost class

Edit. Five commits (item 4 withdrawn); none is a hash mover. Tier: `sonnet` (text and data edits; R3 7b-0).
