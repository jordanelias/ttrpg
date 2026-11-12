# Decisions for Jordan from the A-100 design lane (mass battle as an abstraction of personal combat)

## Status: REFERENCE (a decision register in the form of `unified/DECISIONS_FOR_JORDAN.md`; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of 2026-11-12. Lane: `master/mb_abstraction/` (design: `MBA_DESIGN.md`, `_part2`, `_part3`).

**What this is.** The one question the design leaves to you after the five checks (superseded, irrelevant, settled by a design document, by precedent, by what the architecture needs). Everything else the lane decided is listed at the end with what settled it, so you can see it was not dropped.

---

**ANSWERED 2026-11-12 (A-113): stated rows, checked against history and banded logically to the derived results; personal combat is not taught the equipment now.**

### J-MBA-01 · Should personal combat gain shields, the pike, the mounted fighter and missile weapons, so that mass battle can derive those numbers from it too?

**What the game does today.** You asked for the weapon-on-weapon and weapon-on-armour numbers of a battle to come from simulating personal combat. The duel engine can supply them for swords, axes, maces, spears and polearms against the four armour tiers: the lane ran it (spear against sword, sword against plate, a skilled man against an average one) and the numbers come out cleanly. But the duel engine has **no shield, no pike, no lance, no horse and no bow, crossbow, sling or javelin**: its catalogue has 54 weapons, all hand weapons used on foot. So for exactly the matchups you named as different (pikes against cavalry, bows against cavalry), and for every shielded line, the duel cannot say anything.

**The question.** For those troops, should the battle's numbers wait on personal combat learning the equipment, or should mass battle carry them as stated rows checked against history?

**Options.**

- **A. Teach personal combat the equipment, in two steps.** First the foot kit: a **shield** (most period foot carried one; the sources note arrows "bounced off the shields" at Hastings) and the **pike** (in a duel, a pike is a poor weapon; in a line it is everything, so the duel would need a "pressed, cannot step back" round). Then the **mounted fighter with a lance** and **missile heads** (an arrowhead and a bolt run through the duel's own armour model). *How it plays:* one set of facts at both scales: a shield that saves a duellist saves a shield wall; a bolt that punches mail in a scene punches it in a field. The squad of named characters on a grid (already proposed) becomes the bridge that turns a duel into a charge. *Cost:* a substantial personal-combat build (the foot kit first, then horse and missiles), each with its own calibration; mass battle's matching rows switch from "stated" to "derived" as each lands.
- **B. Keep them as stated rows in mass battle.** Pikes against cavalry, bows against cavalry and the charge stay a small table of rows (about 35, ten needed first) on the existing brace-and-shock rules, checked against what the sources support (a braced pike block stops a frontal charge more often than not; horse ridden into stakes and arrows fail; a pike block without a screen is weak to archers). *How it plays:* the same battles, but those numbers are tuned to history, not derived; a change to personal combat does not reach them. *Cost:* small; already in the design as its first step.
- **C. A then B is not a third option**; the design already ships B and moves to A row by row if you choose A.

**Recommendation: A, foot kit first (shield and pike), with B shipping meanwhile.** The shield and pike are the largest gaps (without the shield every foot troop fights unshielded; without the pike the pike block borrows the spear's numbers), and they are foot equipment the duel engine is built to model. Horse and missiles can follow or stay as rows; the design works either way.

**If you do not answer.** B ships (the rows are flagged "stated, not derived" in the battle report); the shield is absent, and the pike borrows the spear's duel numbers, both printed in the report so nobody mistakes them for measured.

**What waits on it.** Nothing in the first mass-battle batches: the contact draw, the calibration instrument and the first ten rows ship on B. What waits is the switch of those rows to derived (design item MBA-09) and the missile per-hit numbers.

**Sources.** `MBA_DESIGN.md` §2.1, §2.5; `MBA_DESIGN_part2.md` §3.1, §3.2, §4.3, §6.3; `MBA_DESIGN_part3.md` MBA-09, §9.2 E-3; `research/historical/mass_battle_maneuver_sequences_grounding.md:105`, `:96-97`, `:129`; `research/historical/mass_battle_movement_and_behaviour_grounding.md:130-131` (H1, H2); `modules/combat/weapons.py` (`WEAPONS`).

---

## Not yours (answered by the five checks; reversible on your word)

| question | answer taken | what settled it |
|---|---|---|
| Does the contact draw use the one opposed rule of fights and arguments (A-79)? | No: a contact is a count of many independent duel rounds, drawn as a bell curve (A-5) around the measured felling chance; the will checks (stand, rally, obedience) keep their obstacle | A-100's "not a pool against an obstacle" (step 1); the felling chance is itself measured under A-79's rule inside the duel |
| What does a contact return: men, or a separate "endurance" loss? | Men put out of the fight (casualties); their kind (dead or injured) is drawn once at the field's end | A-60 and the lexicon's casualty/loss words (step 3); one quantity, one ledger (step 5) |
| The troop table's `power` column | Read as the men's martial skill and renamed `skill`, values unchanged | A-98 (3) (skill at arms is martial skill) and A-59 (2) (prowess is troops and kit) (steps 1, 5) |
| How many duel rounds a man fights in a field tick (exposure) | Well under one; set against the sources' loss ratios, its absolute level flagged as not established | Sabin's bound in the casualties note (A10) and the calibration targets proposal's rule: ratios and orderings, never a historical percentage (step 3) |
| The duel's reach edge (a spear beats a sword in 94.5% of duels and fells in the first round in 93%) carried into the field | Reported to the personal-combat lane as a finding; not tuned on the mass-battle side | the standing rule "no certain matchup" and its proposal (step 4); a port never corrects its oracle in place (CLAUDE.md §6) |
| Dead against injured | Stays the open item already listed (the share tables of what an army carries back); the duel's mortal-wound reading is recorded beside it as a candidate | IS-MB-B3, already for you or a source search; not a new question |
| The side-wide luck multiplier | Removed in the same change, as your A-77 already rules | A-77 (step 1) |
| Round length in seconds | No seconds figure enters a resolver; the round is bounded by its exchanges | A-101 as amended (step 1) |
