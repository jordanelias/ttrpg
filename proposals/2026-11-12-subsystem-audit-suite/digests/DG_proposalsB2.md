# Digest proposalsB2

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane proposalsB2: 21 files from `proposals/2026-10-16-*` (attributes-from-scratch parts 4-5, character-template parts 1-3, troop-stock-design parts 1-2, verbs 01-14), assigned from `assign/B_proposals2.txt`. Earlier digests `DG_proposals_recent*.md` read several of these only partly; this one is a full read. Every file below is PROPOSED unless stated; none of this is a mechanism (CLAUDE.md §0.05).

### proposals/2026-10-16-attributes-from-scratch_part4.md
- **What it is:** Part 4 of a blind, verb-driven derivation of the attribute set: selection principles P1-P10, the recommended fourteen, what is left to other layers, smaller (8) and larger (20) alternatives with generated coverage tables (2026-10-16, IN-lane style).
- **Status:** "PROPOSED" (:3). Reading: live proposal, undecided; competes with the eleven in `attribute-derivation_*`.
- **Bears on:** CHAR (primary), all subsystems (PC MB SC FI WR FA SE).
- **Content that matters:**
  - Ten principles: P1 breadth (>=10 verbs and >=4 subsystems as performer), P2 independence between persons, P3 readable, P4 stable (spent-and-refilled = a track), P5 absorbs specifics as skills, P6 personal not positional (heir-passing = holding), P7 capacity not preference (preference = value), P8 opposition symmetry (every contested act has an attribute on both sides), P9 a clean draw (one kind of quantity: odds/cost/access/effect), P10 root-sense (:14-25).
  - The fourteen: Bodily force, Quickness, Fine hand, Toughness, Watchfulness, Reading people, Reasoning, Forethought, Nerve, Constancy, Composure, Presence, Warmth, Thread perception (:34-35). Thread perception is [INFERRED], "weakest foundation in the set", false-N check "unverified" (:164-171).
  - Each attribute is tied to ONE kind of draw: force moves effect, quickness only odds (20 of 20), toughness cost (23) and the "only thing moving cost", forethought the largest effect-mover (22), nerve moves ACCESS (16 of 20) and "may belong in the chooser" (a threshold on which acts a person considers) not in a resolution roll, left open (:123-127), constancy cost (19) (:228-243).
  - Layers deliberately off the attribute row: skills, values (mercy/ruthlessness/conviction: move access 14 of 21, belong in the chooser), holdings (rank, remit, claim, means, kit, following; fail P6: "the office is a borrowed body"), computed (credibility, command of many, load, who acts first), tracks (harm, fatigue, stores, self-integrity, reputation), situation (:175-182).
  - Coverage: the fourteen carry 308 of 536 demand instances (57%); 24 verbs have no attribute demand at all (issue, revoke, pardon, open_case, petition, succeed, detain, abolish, waive, depose, vote, pray, bless ...), called "the right outcome, not a gap" because they are decided by who holds what (:245-299). Standing has 40 verbs but moves access (37 of 40) and fails P6/P9 (:184-186).
  - Not covered by any set: age, illness, appearance, learning rate, ("a verb-driven derivation cannot see properties nobody performs") (:311-312).
- **Conflicts / stale:** four plain names collide with registry words (see part5). Counts include 86 of 179 verbs the author added (part5 :203); `verb ids` V001-V179 resolve only through part 1 of `attributes-from-scratch`, not read here.
- **Open items:** whether nerve is a roll attribute or a chooser threshold (:126-127); whether standing/means could ever be a primary (answered no under P6).

### proposals/2026-10-16-attributes-from-scratch_part5.md
- **What it is:** Phase B of the blind attribute derivation: mapping the fourteen against the registry's nine and the "recommended eleven", eight disagreements D-1..D-8, tier-3 precedent cross-check (CK3, RoTK, Bannerlord, Burning Wheel, Disco Elysium, Pendragon, Darklands), ten stated limits.
- **Status:** "PROPOSED" (:3). Reading: live proposal; explicitly "not resolved here".
- **Bears on:** CHAR (primary), all subsystems.
- **Content that matters:**
  - Four of the author's plain names collide with registry words (reasoning = alias of Acuity, presence = alias of Charisma, composure and stamina = `not_descriptors` derived values), kept as written (:25-36).
  - Mapping: of the registry/eleven STR AGI END FOC ACU WIL ATT CHA BON REC TS, five map whole (STR END ATT BON TS), six split (AGI FOC ACU WIL CHA REC); FOC has no whole counterpart; forethought, nerve, composure have no counterpart in the eleven (:84-88).
  - The two derivations "count different things": the eleven count what formulas and code read, the blind set counts what acts ask for; "a formula nobody performs and a verb nobody resolves are both unverified demand"; each disagreement is decided only by "a resolver that reads the candidate and a divergence test against its nearest neighbour" (:123-130).
  - D-1..D-8: forethought primary vs practice `planning`/`numeracy`; nerve primary vs temperament `boldness` (precedent: never a primary in 7 games); composure primary vs practice; fine hand splits from AGI (divergence test D06 NOT TESTABLE, no reader); FOC (concentration) only read by the combat tracker; noticing vs reasoning (D09 not testable); REC's `learning`/`breadth`/`practice-ceiling` have no verb home; ATT found a rescaled ACU (X05) and CHA inert at T2 (:112-121).
  - Precedent (from memory, tier 3): body triad near universal; planning split from reasoning in 1 of 7 (RoTK); nerve and composure never primary; values a separate block wherever modelled (:187-197).
  - Limits: 86 of 179 verbs are author additions; on the 45 code rows alone force ranks 18th, quickness 24th; 536 demand statements by one author, no critic; etymologies unchecked; possible priming by the brief naming the eleven; nothing executed (:203-234).
- **Conflicts / stale:** relies on `references/descriptor_registry.yaml:36-48,64` (nine attributes + Thread Sensitivity) [UNVERIFIED line numbers today]. Disagrees with the recommended eleven by design (not a defect).
- **Open items:** the eight D-rows; renaming of colliding words "a choice for whoever adopts any of this" (:35-36).

