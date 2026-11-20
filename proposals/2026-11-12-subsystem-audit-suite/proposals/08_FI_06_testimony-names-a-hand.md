# 08 · FI · 06 — Testimony names a hand: the pairing travels with the deed

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.5 row FI-06 (CONFORMS), §6 row *`Said` in Layer 1*, §7 (INCOMPLETE: the `g6` method names no file; planted failures unnamed), §7b-17, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger S-07; `unified/U3_DEPENDENCY_ORDER.md` node B11, §6.2). Settled: the Layer 1 `[UNVERIFIED]` (`grep -c Said architecture/meta/04_CODE_ARCHITECTURE.md` reads 0: `04` lists no `Said` members, so no row is amended); the `g6` tests' method is `engine/season/tests/test_told_by_channel.py` (the `test_g6…` group); §5's slants are `U5c_FI_residue.md` §6's one roster text. Added: named tests (7b-17) for the gate and the planted failures; the two scratch probes restated by them; lands-it and tier.

Reconciled: 2026-11-12, unification lane U4c (test 9; from `unified/U3_DEPENDENCY_ORDER.md` §3.1, node B11, and the line below) — dependency line added, which the file lacked: **Depends on:** `08_FI_02_rumour-that-travels.md` (B11, before this file) and `U5c_FI_residue.md` §6 (the one slant roster); no other proposal.

**Lands in batch:** B11 (`U5c_FI_residue.md` §2 row 7: after `08_FI_02` and before `16_PESSIMIST_FI_A` edit 4).

## Status: PROPOSED

Carries `audits/08_FI_audit_addendum_B.md` F-FI-11 and resolutions R-36, R-38. It is the precondition of
`08_FI_05_evidence-interface_B.md` (E-8) for any matter about a death, a wound or a seat's closing, and of
CP-T06-05 (*the person questioned answers by his own act*) being able to name anyone.

## What this changes in `engine/season/` at runtime

A telling of a deed of a paired kind (`person.died`, `body.changed`, `tenure.closed`, …) carries the doer
the teller's own ledger names, and the hearer can read it. A person asked about someone can say what he saw
that person do. At the control arm (`told_pairing: off`) nothing moves. At `on` it is a declared hash mover
in any world where such a deed is told; in `build_realm` that is rare today (0 and 1 deaths by a hand in
three seasons at seeds 0 and 1) and grows with `08_FI_02`.

## The problem, with evidence

`queries/person_q.py::deed_doer` (`:250-285`) names the doer of a paired deed by pairing the deed claim with
the holder's own untold `seen` claim on the same subject, season and round. A telling passes one claim
(`said_of`, `:1165-1201`), and `_seen_index` (`:236-247`) keeps untold sightings only. So:

| holder | `deed_doers(kinds: [person.died])` |
|---|---|
| the witness | `('K',)` |
| anyone he tells | `()` |
| anyone told his sighting as a second telling | `()` |
| control: anyone told an **unpaired** deed, `(K, record.forged, True)` | `('K',)` |

(`hearsay_doer_probe.py`, scratchpad `runs/FI_B/`, not in the repository; hand-built ledgers; restated by the
named tests below.) The witness asked about K says
nothing: `said_of(claims, 'K')` is `None`, because the deed claim's subject is the victim. In the realm at
seed 1 over three seasons one person died by another's act; seven persons hold a firsthand claim of it and
none names a doer; `deed_doers` with that kind names anyone for 0 of 82 persons (`attribution.py`, same
scratchpad). The limit is written in two docstrings (`attributed_deeds`: *"a paired claim heard second-hand
names nobody"*; `legitimacy`: *"second-hand news of a killing or a wound never moves legitimacy"*) and in no
hole-register row.

## The resolution, decided

**A pairing travels with its deed, on one chain.** Ladder step 4: for every deed kind a single row emits,
the told copy already names its doer (the control arm above). The paired kinds lose the hand because the
hand lives in a second claim that the telling does not carry, not because anything ruled that a report may
not accuse. The eyewitness-only reading is kept as the control arm.

## Edits, by owner

1. **`engine/season/state/carriers.py::Said`** gains one optional member, `pairing`, default `None`: the
   `Seen` value the teller pairs with the deed he is passing on (as he holds it, with whatever terms his
   channel showed). Keyword-only, so every existing construction is untouched. `Said` rides the Act's
   payload; no ledger carrier gains a field.
2. **`queries/person_q.py::said_of`.**
   - The pool for `subject` becomes: the claims whose subject it is, **and** `attributed_deeds(claims,
     subject)` (the one owner of "which of a holder's claims are about what this person did"). A witness
     asked about K can now say `(V, person.died, True)`.
   - When the picked claim is of a `PAIRED_KINDS` kind and `deed_doer` over the teller's own ledger names a
     doer, the returned `Said` carries that sighting as `pairing`. A told deed the teller holds with a told
     pairing passes the same pairing on, so the hand survives a retelling.
3. **`loop/witness.py`, the told deposit.** After the told deed claim, where `_held.pairing` is not `None`,
   deposit one told `seen` claim on the same subject with the same `when`, `round`, source and **chain**,
   through the same guard, refraction and credit. At `Partial` the copy withholds `who` (the lossy copy's
   own rule, and `rosters.yaml: finding_terms`' precedent: *a partial finding withholds the hand*), so a
   garbled report says that it happened and not who.
4. **`queries/person_q.py::_seen_index`** returns a third index, told sightings keyed by `(subject, when,
   round, chain)`. **`deed_doer`** answers a told deed from that index and only from it: a told deed is
   paired with a sighting told on the same chain at the same deposit, never with the hearer's own
   sightings. The existing refusals stand unchanged (no `who`, two different `who`, a stratum the kind's
   rows do not carry). `attributed_deeds`, `suffered_deeds`, `deed_doers` and `paired_deed_term` drop their
   own `c.chain` exclusions for paired kinds and ask `deed_doer`; a told paired deed lands in
   `deeds_judged`'s `told` half, as every told deed does. `legitimacy`'s caveat is deleted with the limit.
5. **`said_of`'s slant arms (R-36; the same owner, so sequenced here).** `rosters.yaml: said_slants` carries
   the one text of `U5c_FI_residue.md` §6: `unshared` (the register's own recorded follow-up, H-197: the pick
   skips the transport's own event kinds, `R8.1`'s exclusion of `seen` being the precedent) and
   `unshared_first` (that, plus the tiers `[told, inferred, deed, quantity, other]`). Each is read against `newest`, so a traffic
   gain can be attributed to one change.
6. **`engine/season/data/fixtures.py`:** `told_pairing`, `off` (control, today) / `on`; ships `on` when the
   gate reads.
7. **`engine/season/hole_register.yaml`:** one row for the limit as measured (it has none), closed by this
   position.

**Not built here, named.** Saying a *false* hand (the deed lie, H-198 rule (ii)) becomes expressible once a
`Said` carries a pairing: `lie_said_of` could name another person the liar knows of. That is the false
accusation corpus cases NPC-004 and the Foscarini shape need, and it is design-first (whom a liar would
name is a choice, `08_FI_02` §4's operand), so it is left out.

**Layer 1.** `Said` gains a member. `architecture/meta/04_CODE_ARCHITECTURE.md` does not list `Said`'s
members (settled: `grep -c Said` on it reads 0), so no Layer 1 row is touched. The told `seen` claim is an
ordinary claim, not `04` §B.9's `Claim.doer?` stamp (which WITNESS stamps only on a holder's own act's
deposits). `loop/witness` reads nothing new (the Act's own `said`).

## Gate (execution artifact)

Through the real fold and the real WITNESS barrier on a hand-built world (the `g6` tests' method,
`engine/season/tests/test_told_by_channel.py`):
W witnesses K kill V; W tells J; J tells L.
- `on`: `deed_doers(J.ledger, {kinds: [person.died]}, J)` and the same for L read `('K',)`; L's claims carry
  the chain `(W, J)`; `attributed_deeds(J.ledger, 'K')` yields the deed; J's `regard` for K moves by the
  `told` half.
- `on`, the telling at `Partial`: J holds the death and names nobody.
- W, asked about K, says the death (the `said` on his Act is `(V, person.died, True)` with a pairing).
- `off`: every reading above is today's (`()`, `None`), and `build_realm(0..2)` one-season hashes are equal
  to the base.
Then the probe's readings (restated): the hearer rows read `('K',)`; the unpaired control is unchanged.
Named tests (new, `engine/season/tests/test_told_pairing.py`): `test_a_telling_carries_the_hand`,
`test_a_retelling_keeps_the_chain`, `test_a_partial_telling_withholds_it`,
`test_the_witness_asked_about_the_doer_says_the_death`, `test_off_arm_is_todays_reading_and_hash_equal`.

## Falsifier

A hearer who holds his **own** sighting of a different person acting on V in that round must name that
person from his firsthand claim and K from the told one, and never K from his own sighting
(`test_told_pairing.py::test_a_hearers_own_sighting_is_never_the_told_ones`). Planted failure: key the told
index without the chain; that test must go red. A second: a told deed with no pairing (the teller's own
pairing was ambiguous) must still name nobody (`::test_an_unpaired_telling_names_nobody`).

## Risks, stated

- A hand now travels at the teller's confidence less refraction; nothing checks it. That is hearsay as the
  knowledge model rules it (graded at read by teller, hops and record), and it is the point.
- The told sighting is one more claim per such telling; the same ledger cap and exact-triple guard bound it.

## NERS reading

N: accusation, denunciation, an informer's worth, vengeance on report and a magistrate's `deed_doers` goal
all need it; top-down (R-01: who did what must be able to propagate), bottom-up (one optional member, one
index), lateral (SC's proofs, CHAR's regard and legitimacy read the same owner). R: the no-player half
directly: a death becomes a story other people can carry, garble and act on. S: the pairing rule stays one
rule (same subject, season, round; now also same chain for a told one); the lossy copy drops the hand as a
partial finding does. E, last: one member, one deposit line, one index, against homicide being untellable.

## Cost class

Small build. Lanes: FI (owner), CHAR (`regard`, `legitimacy` read it), SC (consumes it through `proofs`).

**Lands it and tier.** The B11 batch, an FI `valoria-author` session on `sonnet` (`high`), closed by B11's
`methodology-close` once. **Hash movers.** At `told_pairing: on` (declared); none at the control.
