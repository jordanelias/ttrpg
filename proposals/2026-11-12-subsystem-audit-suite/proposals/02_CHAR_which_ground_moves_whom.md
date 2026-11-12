# CHAR — which ground moves whom: a hearer's susceptibility, read from the cast row that already authors it

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-08) — the polarity this file left to the builder is decided: `against: true` means *against the roller* (U1 architecture §3 item 3). The four `moved_by_*` rows favour the arguer, so they are written `side: subject, against: false`. The four traits are rows of `descriptor_registry.yaml: capabilities`.

## Status: PROPOSED

Written by the CHAR audit lane, addendum B (`audits/02_CHAR_audit_addendum_B.md`, F-CHAR-16, B3.2
property P5, B6.2 rows 3 and 7). Ratifies nothing. Reference under `CLAUDE.md` §0.05. It composes on
`10_DICE_capability_axiom_map.md` (the `edge` role, the `capability_uses` table, the generic
`capability` advantage source), on `05_SC_capability_surface.md` (a trait as an advantage row) and on
`05_SC_evidence_and_rebuttal.md` (cited proofs); it adds no capability system and no field on
`Person`.

## What this changes in `engine/season/` at runtime

With no row authored, nothing: the hash is EQUAL. With the eighteen cast rows that already carry a
`resonant_style:` seated as traits, an `argue` whose support matches its hearer's susceptibility
resolves with one named level of advantage for the arguer; every other roll is as it was. A declared
mover, confined to `argue` on those eighteen hearers.

## The problem, with evidence

**Everybody is moved alike.** `argue` moves a hearer's pursuits by a roll of the arguer's pool
against half the hearer's score (`seam/wrappers/sigma.py`); nothing about the hearer decides *what
kind* of case reaches him, and his conviction does not resist (H-268). NPC-001's core need is a
person *"unmoved by rhetoric, moved by evidence"* (cited in `05_SC_capability_surface.md`).

**The fact is already authored and nothing reads it.** `references/npc_registry.yaml` carries
`resonant_style:` on 18 of 46 rows (Evidence 7, Consequence 5, Solidarity 4, Authority 2; parse). A
search of every non-test `.py` under `engine/`, `modules/`, `tools/` and `systems/` finds no reader.
The NPC research lane proposed deleting the key (K-NPC-11).

**What the design meant** (ARCHIVED-NOT-CANON; intent only). The third corner of the Stance Triangle:
*"the argument form that bypasses the NPC's defenses … Determines how the NPC can be moved"*
(`npc_behavior_v30_infill` §1.1). Evidence: named, verifiable facts. Consequence: outcomes his frame
fails to prevent. Authority: a source his frame recognises as binding. Solidarity: a relation that
asks what his position forbids, and *"requires active Knot"* (§1.3). It is discovered, not shown
(§6.1).

**The apparent conflict, named.** #353 §9.3: what is right is moved by argument and consequence,
never by evidence. The design's Evidence style, read whole, is a property of the hearer about the
support an argument needs; the mover stays `argue`, and a cited document moves no value by itself.
On that reading the ruling and the design agree. If Jordan reads the ruling as barring evidence from
weighing in an argument at all, the `moved_by_evidence` row is dropped and the other three stand.

## The resolution, decided

Ladder: step 3 (the design states the four and the registry authors them), step 4 (the DICE map's
`edge` rows; SC-P7's trait advantage). A susceptibility is a **trait** the hearer holds; it yields a
named level **against him** on an `argue` when a stated condition about the argument holds. The
conditions are things the engine can already observe.

## Exact edits, by file and owner

1. **The four traits** (rows of the capability definition table, in whichever file the holistic
   stage picks; shape per the DICE map §B, with `gloss` from `02_CHAR_capability_definitions.md`):

   ```yaml
   moved_by_evidence:    {kind: trait, scale: [0, 1], untrained: none, grows_by: [fixed], gloss: "Yields to a case that cites something he can check."}
   moved_by_consequence: {kind: trait, scale: [0, 1], untrained: none, grows_by: [fixed], gloss: "Yields when shown the harm his own position has already done."}
   moved_by_authority:   {kind: trait, scale: [0, 1], untrained: none, grows_by: [fixed], gloss: "Yields to one who stands over him or speaks for his creed."}
   moved_by_solidarity:  {kind: trait, scale: [0, 1], untrained: none, grows_by: [fixed], gloss: "Yields to one he holds dear."}
   ```

2. **Four `when` keys** (new members of the uses table's closed `when` roster; one host-side function
   each in `seam/wrappers/sigma.py`, beside `advantage_sigma`, which may read the World at RESOLVE):

   | key | holds when | reads |
   |---|---|---|
   | `cites: <proofs member>` | the act's payload cites at least one held item of that kind | SC-P8's typed `proofs` entries; `False` until SC-P8 lands (the row is then inert, not wrong) |
   | `consequence_held: true` | the hearer holds a deed claim about the argued Proposition's subject that his own `deeds_judged` scores negative | `queries/person_q.py::deeds_judged` on the hearer's ledger |
   | `speaker_over_subject: true` | the arguer holds a live seat whose purview contains the hearer, or uttered a creed the hearer is committed to | `state/gate.py::purview_reaches`; the hearer's live `commit` edges |
   | `regard_at_least: <n>` | the hearer's `regard` for the arguer is at least `n` stance steps | `queries/person_q.py::regard` |

3. **Four uses rows** (`capability_uses`):

   ```yaml
   - {use: social_roll, role: edge, key: moved_by_evidence,    side: subject, against: true, when: {verb: argue, cites: record},              level: moderate, per: held}
   - {use: social_roll, role: edge, key: moved_by_consequence, side: subject, against: true, when: {verb: argue, consequence_held: true},     level: moderate, per: held}
   - {use: social_roll, role: edge, key: moved_by_authority,   side: subject, against: true, when: {verb: argue, speaker_over_subject: true}, level: moderate, per: held}
   - {use: social_roll, role: edge, key: moved_by_solidarity,  side: subject, against: true, when: {verb: argue, regard_at_least: 3},         level: moderate, per: held}
   ```

   `moderate` and the regard floor 3 are `[ASSUMPTION; medium; Jordan to correct]`; the level is one
   of the map's four names, so no new magnitude enters. **Polarity, stated so it cannot invert
   silently:** each row's levels favour the ARGUER (the hearer who holds the trait is easier to move
   when the condition holds). The map's §C defines `against: true` as *"the levels count against the
   side named"*, and its §E example writes a trait that *hardens* a hearer with the same two fields;
   one of the two readings is the map's, and whoever builds the reader sets the flag on these four
   rows to whichever value means "for the actor". The gate's reading (b) observes the direction.

4. **The character's side** (`engine/season/data/cast.py`, owner of the cast loader). A function
   `susceptibility_of(r)` maps the row's `resonant_style:` value (checked against a closed roster
   `rosters.yaml: susceptibilities: [evidence, consequence, authority, solidarity]`, refused
   otherwise) to `{moved_by_<style>: 1}`; the builder merges it into `Person.capability` as it merges
   a lifepath's keys. The registry key keeps its name and its eighteen values. A second style per
   person (the design has one) is content: the key may become a list.

5. **Not built here: the arguer's own knowledge of it.** `View.odds` computes a believed chance from
   the believer's ledger. Whether an arguer counts a hearer's susceptibility in his believed odds
   should depend on his holding a claim of it, so that it must be found out (P5). The deposit of
   such a claim (by a resolved `argue` in which the row fired, or by an `interview`) is the FI and SC
   lanes' design; until then the edge is in the roll and not in anybody's forecast, which errs on
   the side of nobody knowing.

## The gate (an execution artifact)

(a) No rows, or no cast row seated: `build_realm(0)` one- and two-season hashes EQUAL. (b) A
hand-built pair of hearers identical but for `moved_by_solidarity`, the same arguer, the same
Proposition, the arguer's regard row toward each at 4: over 400 paired seeds the susceptible hearer
is moved at Success or better more often, by the difference a `moderate` level makes at those pools
(the dice lane's own table); with the regard row at 0 the two rates are equal. (c) In a seeded realm
season, at least one `argue` on one of the eighteen resolves with the edge reported by the
`capability` advantage source.

## The falsifier

(b)'s two rates are equal with the condition met (the row is not read), or differ with it unmet (the
trait is acting as a flat modifier). Or (c) reads zero at seeds 0 to 2 over four seasons: then the
conditions are unreachable in play and the proposal has added an unread row, which is F-CHAR-16
again.

## NERS reading (`CLAUDE.md` §0.06; E last)

- **N.** From the hearer's side it is the only thing that makes one person harder to reach than
  another except by pool size; from the arguer's side it gives a reason to gather a document, to
  seek office over a man, or to befriend him first; from the world's side, two NPCs arguing differ
  by who is being argued with. Removing it returns H-268's uniform hearer.
- **R.** Strategy (find out what reaches him, then get it), variety (four routes to one mind), and
  the no-player half: a bishop bends to his primate and not to a ledger, unobserved.
- **S.** One door (`advantage_sources`), named levels, no change to the obstacle; the same uses table
  every other trait will use; it pauses nothing.
- **E.** Four rows and four small predicates over state that already exists, for a property the cast
  already authors. A player can intuit it: *he will not hear this from you; he would from his
  confessor.*

## Cost class

Edit (rows, one loader function) after the DICE map's part one; small build for the four `when`
functions; `cites` waits on SC-P8.
