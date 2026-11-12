# U5a · CHAR — self-knowledge is a belief, built narrowly: a gift a man does not know he has, a motive he does not recognise

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
| his body, seats, oaths, commits, residence, trained skills | yes | — |
| the one gated gift (`prac.thread_sensitivity`) | where the row is not marked | where the cast row marks it `unaware` |
| a pursuit he acts on | acts on it always (the score reads the true vector) | whether his **sheet and reason trail name it** |
| his creed | yes | — (a crisis of faith is `16_PESSIMIST_CHAR_A…`'s draw, which deposits its own claim to him) |

## Exact edits, by owner

1. **`engine/season/rosters.yaml`**: a closed roster `self_believed`, shipped
   `[prac.thread_sensitivity]` plus the pursuit roster by pointer (`from_descriptor: pursuit_roster`). A key
   outside it may not be marked unaware (refused at load).
2. **`references/npc_registry.yaml`**, **`engine/season/data/cast.py`**: an optional cast-row key
   `unaware: [<key>, …]`, each a `self_believed` member the row actually holds; `unaware_of(r)` validates
   it and refuses otherwise. Content for the three cases is authored by the CHAR content pass: NPC-004
   `unaware: [prac.thread_sensitivity]`; NPC-012 the pursuit his case names.
3. **`engine/season/harness/populated.py::build_realm`** (the one seeder): for every cast person and every
   `self_believed` key he holds that is **not** marked, one firsthand claim in his own ledger,
   `(self, "self:<key>", True)`. A marked key seeds none.
4. **`engine/season/queries/person_q.py::OwnStateReader`**: for a stem whose key is in `self_believed`,
   the person-side answer is his own claim `self:<key>` (held: the field's value; not held: `UNKNOWN`).
   For `thread_read`'s cell (built only of own-state stems, which forms on `True`), `UNKNOWN` does not
   form: he does not deliberately read the Thread. The fold's own read of the field is unchanged, so a
   hand-built act still folds. Every other own-state stem is answered from the field as today.
5. **`engine/season/decision/sheet.py`** and the reason trail's readers
   (`decision/voices.py` when `02_CHAR_voices_and_the_room.md` lands; `harness/chronicle.py`): a pursuit
   he holds no `self:` claim for is not listed on his sheet and its voice is attributed as *unrecognised*
   (kind `pursuit`, owner withheld). The score is untouched: the motive still biases every decision, which
   is NPC-012's first need.
6. **How he comes to know** (both existing mechanisms, no new verb): (a) he is told: a `tell` whose claim
   is `(him, "self:<key>", True)` deposits as any told claim and is graded by his regard for the teller,
   so he may disbelieve it; (b) it shows: when a use row keyed on the capability contributes to one of his
   own graded acts at Overwhelming (the `fed_by` record of U1 architecture §8 names it), WITNESS deposits
   `self:<key>` to him alone (the `witness_key` channel's rule). The band is the act's own draw; no second
   draw is taken.

## Gate (execution artifacts)

1. No row marked: `build_realm(0)` and one season, hash EQUAL (the seeded `self:` claims are new ledger
   rows: the build hash moves once when edit 3 lands and is re-recorded; with edits 1, 2, 4, 5 alone and no
   seeding the hash is today's. The control is stated per edit in the landing commit).
2. NPC-004 marked: over a seeded realm season he forms no `thread_read`; his inquiry rolls still show the
   capability in `fed_by` where a use row names it; his twin with the mark removed forms `thread_read`.
3. Told and disbelieving: a planted `tell` of `self:prac.thread_sensitivity` from a person he holds low
   regard for leaves his reader at `UNKNOWN` below the confidence the reader requires; from one he trusts,
   the candidate forms next round.
4. NPC-012 marked on one pursuit: `decision_spread --decisions` reads the same deciders with and without
   the mark (the score did not move); his sheet omits the pursuit.

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

Small build, then content (two or three cast rows). Lands after `02_CHAR_capability_uses_table.md` (the
gate's row) and with or after the reason trail.
