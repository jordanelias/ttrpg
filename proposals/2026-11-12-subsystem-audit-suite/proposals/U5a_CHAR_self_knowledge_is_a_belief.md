# U5a · CHAR — self-knowledge is a belief, built narrowly: a gift a man does not know he has, a motive he does not recognise

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.3 row (CONFORMS, one dependency gap), §2 row A-34 (NPC-021), §7, §7b-16, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-06, ledger S-26; `unified/U3_DEPENDENCY_ORDER.md` node B10). Changed: edit 6 (b)'s dependency is stated — `fed_by` lives on the provider's returned record, which WITNESS cannot read; per D-U1-06 (which governs where it differs from the read lane's §7b-16), the act's effect puts the shown capability on `Event.observed` as an `observation_terms` member and WITNESS deposits it to the actor alone, so (b) lands only after `fed_by` exists (U1-B, B05), and until then (a) alone carries coming to know; **NPC-021** is carried by `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` (the crisis of faith deposits its own claim to him), said at edit 2; the reason-trail reader is `decision/score_parts.py` (the renamed `voices.py`, glossary *voice*); named tests; lands-it and tier.

**Lands in batch:** B10 (edits 1–6 (a)); edit 6 (b) after U1-B (B05) and with the `observation_terms` member. **Depends on:** `02_CHAR_capability_uses_table.md` (B04), `U5c_SC_one_obstacle_form.md` (B05), `02_CHAR_voices_and_the_room.md` (B10, for edit 5's reader).

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Authored by the U5a unification-closure lane, 2026-11-12. Carries the one survivor of
`audits/02_CHAR_audit.md` §11 and `02_CHAR_audit_addendum_B.md` §B6.3 (*can a person be wrong about
himself?*), which no proposal carried because it was Jordan's. Jordan answered it on 2026-11-12
(`unified/DECISIONS_ANSWERED.md` A-34, D-47): **B, a belief, built narrowly: first for the gifts and motives
the cases name (NPC-004, NPC-012, NPC-021).** This is that narrow build and nothing wider. Every value is
`[ASSUMPTION; medium; Jordan to correct]` and reverts alone.

## What it changes in `engine/season/` at runtime

With no cast row marked (the shipped state), nothing: every person knows his own sheet as today; hashes
EQUAL. With a row marked `unaware:` for a key, that person does not form the acts the key would admit,
is not shown it, and can come to know it by being told or by its showing in his own act. What the key
*does* on a roll is unchanged: a gift works whether or not its holder knows of it.

## The problem, with evidence

- `decision/options.py::opening_set`'s own-state branch reasons that a person's sensitivity *"is not a belief
  about the world he can be wrong about"*, and `queries/person_q.py::OwnStateReader` answers it from the
  field (`02_CHAR_audit.md` §11). So self-deception and an unrecognised gift cannot be played.
- The provided cases ask for it. NPC-004 (Sæmund): *"does not know he is Thread Sensitive. He attributes
  his 'hunches' to investigative instinct"* (`npc_roster_v30` §4, archived, intent only). NPC-012 (Rikard):
  a motive its holder does not recognise biases every decision. NPC-021 (Arne): faith privately
  challenged. AR-49 (Jordan, 2026-11-05): a man *"unaware of their impact on others (attunement)"*.

## The resolution, decided (ladder step 5, inside A-34's bound)

A person's knowledge of himself is carried where all his knowledge is carried: a claim in his own ledger
whose subject is himself. **Only what a closed roster names is read that way**; everything else about
himself he still knows by construction. No second answer on every own-state read (the cost A-34's
"narrowly" avoids).

| what | known by construction (today, unchanged) | read from his own ledger (this proposal) |
|---|---|---|
| his body, seats, oaths, commits, residence, skills | yes | — |
| the one gated gift (`prac.thread_sensitivity`) | where the row is not marked | where the cast row marks it `unaware` |
| a pursuit he acts on | acts on it always (the score reads the true vector) | whether his **sheet and reason trail name it** |
| his creed | yes | — (a crisis of faith is `16_PESSIMIST_CHAR_A…`'s draw, which deposits its own claim to him) |

## Exact edits, by owner

1. **`engine/season/rosters.yaml`**: a closed roster `self_believed`, shipped
   `[prac.thread_sensitivity]` plus the pursuit roster by pointer (`from_descriptor: pursuit_roster`). A key
   outside it may not be marked unaware (refused at load).
2. **`references/npc_registry.yaml`**, **`engine/season/data/cast.py`**: an optional cast-row key
   `unaware: [<key>, …]`, each a `self_believed` member the row actually holds; `unaware_of(r)` validates
   it and refuses otherwise. Content for the cases is authored by the CHAR content pass: NPC-004
   `unaware: [prac.thread_sensitivity]`; NPC-012 the pursuit his case names. NPC-021 (faith privately
   challenged) needs no `unaware:` row: his doubt is carried by the crisis-of-faith draw of
   `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md`, which deposits its own claim to him (the
   table above, row *his creed*); A-34's three named cases are thereby all carried.
3. **`engine/season/harness/populated.py::build_realm`** (the one seeder): for every cast person and every
   `self_believed` key he holds that is **not** marked, one firsthand claim in his own ledger,
   `(self, "self:<key>", True)`. A marked key seeds none.
4. **`engine/season/queries/person_q.py::OwnStateReader`**: for a stem whose key is in `self_believed`,
   the person-side answer is his own claim `self:<key>` (held: the field's value; not held: `UNKNOWN`).
   For `thread_read`'s cell (built only of own-state stems, which forms on `True`), `UNKNOWN` does not
   form: he does not deliberately read the Thread. The fold's own read of the field is unchanged, so a
   hand-built act still folds. Every other own-state stem is answered from the field as today.
5. **`engine/season/decision/sheet.py`** and the reason trail's readers
   (`decision/score_parts.py` when `02_CHAR_voices_and_the_room.md` lands; `harness/chronicle.py`): a pursuit
   he holds no `self:` claim for is not listed on his sheet and its voice is attributed as *unrecognised*
   (kind `pursuit`, owner withheld). The score is untouched: the motive still biases every decision, which
   is NPC-012's first need.
6. **How he comes to know** (both existing mechanisms, no new verb): (a) he is told: a `tell` whose claim
   is `(him, "self:<key>", True)` deposits as any told claim and is graded by his regard for the teller,
   so he may disbelieve it; (b) it shows: when a use row keyed on the skill contributes to one of his
   own graded acts at Overwhelming (the `fed_by` record of U1 architecture §8 names it), the act's effect
   adds an Observation `capability_shown:<key>` to the Event's `observed` (D-U1-06: `observed` is the one
   channel for a per-Event fact WITNESS may deposit; the member joins the closed roster
   `rosters.yaml: observation_terms` `[ASSUMPTION: the member's name]`), and WITNESS deposits `self:<key>`
   to him alone (the `witness_key` channel's rule). The band is the act's own draw; no second draw is taken.
   **Dependency:** `fed_by` exists only after U1 §11 U1-B (B05); until then (b) is not built and (a) alone
   carries coming to know.

## Gate (execution artifacts)

1. No row marked: `build_realm(0)` and one season, hash EQUAL (the seeded `self:` claims are new ledger
   rows: the build hash moves once when edit 3 lands and is re-recorded; with edits 1, 2, 4, 5 alone and no
   seeding the hash is today's. The control is stated per edit in the landing commit).
2. NPC-004 marked: over a seeded realm season he forms no `thread_read`; his inquiry rolls still show the
   skill in `fed_by` where a use row names it; his twin with the mark removed forms `thread_read`.
3. Told and disbelieving: a planted `tell` of `self:prac.thread_sensitivity` from a person he holds low
   regard for leaves his reader at `UNKNOWN` below the confidence the reader requires; from one he trusts,
   the candidate forms next round.
4. NPC-012 marked on one pursuit: `decision_spread --decisions` reads the same deciders with and without
   the mark (the score did not move); his sheet omits the pursuit.

Named tests (new, `engine/season/tests/test_self_knowledge.py`): `test_no_row_marked_is_hash_equal_before_seeding`
(1); `test_an_unaware_holder_forms_no_thread_read_and_his_twin_does` (2);
`test_a_told_self_claim_is_weighed_by_regard_for_the_teller` (3); `test_an_unrecognised_pursuit_moves_no_score_and_leaves_the_sheet` (4);
`test_a_shown_capability_is_deposited_to_the_actor_alone` (6 (b), after B05).

## Falsifier

A marked person forms the gated act; an unmarked person stops forming it; a marked pursuit changes any
score; a person other than the holder receives a `self:` deposit from edit 6 (b).

## Layer 1 and the standing rule

AX-2 is kept and strengthened: the person-side answer is his ledger's, never the field's, for the keys
named. No `World` under `decision/`. Nothing here decides an outcome from state: coming to know is by a
told claim's weighing or by an act's own band.

## NERS reading (E last)

**N.** Three provided characters cannot be played as written without it (`core` needs); from below it
uses the ledger and the own-state reader that exist; laterally it gives `02_CHAR_voices_and_the_room.md`
the "voice that was wrong about oneself". **R.** A gift discovered, a motive named by someone else, a man
talked into a false view of himself: drama inside one person, with no player needed. Complete at the
bound: a key outside the roster cannot be marked. **S.** One carrier for all knowledge, the self included;
one reader. **E (last).** One roster, one cast key, one seeded claim per held key, one branch in one reader.

## Cost class

Small build, then content (two cast rows; NPC-021 is carried by `16_PESSIMIST_CHAR_A`). Lands after
`02_CHAR_capability_uses_table.md` (the gate's row) and with or after the reason trail.

**Lands it and tier.** The B10 batch, a CHAR/IN `valoria-author` session on `sonnet` (`high`), closed by B10's
`methodology-close` once; edit 6 (b) in the first batch after B05 that touches WITNESS. **Hash movers.** The
build hash once when edit 3 seeds the `self:` claims (declared); none with no row marked otherwise.
