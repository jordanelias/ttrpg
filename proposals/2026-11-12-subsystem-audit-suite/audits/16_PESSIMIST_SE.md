# SE — pessimist audit: NERS, premise and emergent narrative, of settlements, territory and economy

## Status: REFERENCE (an audit; resolves nothing at runtime)

Scope: `modules/settlements/`, the season loop's economy, migration, founding and hunger effects
(`engine/season/loop/effects_economy.py`, `effects_migration.py`, `effects_founding.py`), geography, the
campaign supply layer that feeds mass battle, and six premise sentences of a place. The first audit
(`audits/07_SE_audit.md`) and its addendum (`07_SE_audit_addendum_B.md`) and the ten `07_SE_*` proposals
are cited, not redone. Everything measured here is new work unless a finding id of theirs is named.

All runs: `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_SE/`.

(Sections below are appended as the work proceeds; §0, the verdict, is written last and placed first.)

## 2. Premise audit

Method: `skills/premise-check/SKILL.md`, SLICE scope (the six sentences the work order names). The
ordinary account O in §2.1 was written before this lane opened any settlement, economy, migration or
founding file, any SE audit or any SE note; it is from the words.

### 2.1 O — what each sentence should mean (written first)

**P1 "A town that cannot feed itself starves, shrinks and is blamed."**
1. A town has mouths (people) and food (what its ground yields, what it stored, what it bought or was
sent). 2. "Cannot feed itself" is a comparison the game makes each season or year: food available against
food needed; the shortfall has a size. 3. A store delays hunger: a town with a full granary survives one
bad year; hunger starts when the store is gone. 4. "Starves" is a state of the town with degrees (short
rations, hunger, famine), proportionate to the shortfall and its duration. 5. "Shrinks": people die or
leave; the loss is proportionate to the shortfall (a 10% shortfall is not a 50% loss), and it is by a
draw, not a fixed fraction (standing rule). 6. Shrinking lowers the need, so hunger is self-limiting: a
town shrinks toward what its ground can feed, it does not go to zero unless the ground gives nothing.
7. Zero: a town that can feed itself does not starve, shrink from hunger or get blamed for hunger.
8. "Is blamed": somebody is held responsible by somebody. The ordinary reading is that the hungry blame
whoever rules them (the lord, the steward, the council), and a neighbour or rival may be blamed if he
caused it (a siege, a seized harvest). The words "is blamed" with the town as subject could also mean the
town is blamed by its lord for failing its dues; the first reading is the commoner one. 9. Blame has a
consequence: lost standing, unrest, a deposition, a grievance somebody acts on. Blame with no consequence
is a log line. 10. Blame fits the cause: a ruler who emptied the granary for a war is blamed more than
one who met a drought with an open store. 11. Feedback: the player can see the town is hungry before it
starves, see why, and see who is blamed. 12. [GENRE] the player can do something: send food, buy grain,
cut the levy, move people. 13. Hunger also weakens what the town gives: fewer levies, less tax.

**P2 "A good harvest and a bad one differ."**
1. A harvest is the yearly (or seasonal, at the season it falls) yield of a place's ground. 2. It varies
by a draw: weather or luck, not a constant. 3. Its size depends on the ground (fertile land yields more),
the hands (too few workers lowers it), and disturbance (war on the fields, a siege). 4. "Differ": the
difference is visible in the stores and then in what follows: a good year fills the granary, lets the
town grow, sell or feed an army; a bad one draws the store down and, if repeated or severe, starts P1.
5. The difference is in proportion: one bad year after good ones is a tight winter, not a collapse; two
or three are a famine. 6. Neighbouring places share weather to a degree (a regional bad year) and differ
to a degree (one valley's flood). 7. The spread is wide enough to matter and narrow enough that the
ground still matters more than the luck over ten years. 8. Feedback: the record says "a poor harvest at
X", so a later hunger traces back to it. 9. Zero: a place with no farmland has no harvest and lives by
trade. 10. [GENRE] the season matters: harvest comes in autumn, hunger bites in late winter and spring.

**P3 "People leave a failing place."**
1. A place fails when it is hungry, unsafe (raided, besieged, lost a battle nearby), ruinously taxed or
badly ruled. 2. People are counted; leaving reduces the count there. 3. They go somewhere: a named
destination that gains them, near enough to walk to, and better off than where they left (conservation:
those who leave arrive, less those lost on the road). 4. The rate is proportionate to how badly the
place fails, and by a draw. 5. Not everyone can leave: the bound, the poor and the old stay; the first
to go are those with means or nothing to lose. 6. Zero: a thriving place does not lose people this way,
and it attracts them. 7. Leaving has consequences at both ends: the origin's labour, levy and tax fall
(a spiral or a relief, since fewer mouths); the destination gains hands and mouths, perhaps strain and
resentment. 8. A ruler notices and can respond (hold them, lure them, fix the cause). 9. A place can
empty and be abandoned; that is an ending the record states. 10. Named persons leave too, or pointedly
stay. 11. Feedback: the record says who left where and why.

**P4 "A founder builds something that lasts or fails."**
1. A founder is a person (named) who starts a new thing: a settlement, in this scope (it could be a
house, an order or a company). 2. Founding takes an act, a site, people and stock; it costs the founder
and the place the people came from. 3. The site matters: good ground, water, a road. 4. The outcome is
open at the founding: it "lasts or fails" over the following years by its ground, its luck (a draw),
its neighbours and what the founder does. 5. Failing means the place is abandoned or absorbed, its
people dead or returned, and the record says so. 6. Lasting means it grows into a place like the
others, with its own people and character, and outlives the founder. 7. The founder is bound to it: it
is his name on it, his standing rises or falls with it, his death early matters. 8. Both outcomes occur
in computed play in a visible share; a founding that always lasts or always fails is not this sentence.
9. Zero: nobody founds, nothing new appears. 10. [GENRE] the player can found, and choose where.

**P5 "Trade moves goods to where they are wanted."**
1. Goods are kinds (grain, timber, iron, cloth), held in amounts at places. 2. "Wanted" is a shortage or
a higher price at a place: demand over supply. 3. Trade is a movement along a route between places that
are connected (a road, a river, a neighbour), by somebody (a merchant, a caravan) or by an abstract flow.
4. Goods move from surplus to shortage: the source's stock falls, the destination's rises (conservation,
less a loss on the way). 5. The amount moved is proportionate to the difference and limited by the route
and the distance. 6. Trade relieves shortage: a hungry town with a rich neighbour and an open road is
less hungry than the same town cut off (the control). 7. Trade can be cut: war, a closed road, an
embargo, a siege, bandits; cutting it hurts the one that depended on it. 8. Somebody profits: the
carrier or the selling town gains coin. 9. Zero: no difference in want, nothing moves; no route, nothing
moves. 10. Feedback: the record names what moved and from where to where. 11. A draw: caravans are lost.

**P6 "A place has a character from its ground and its people."**
1. Ground: terrain, soil, water, resources, position (coast, pass, river). 2. People: how many, of what
callings, faiths, loyalties, origin. 3. Character: a set of traits of the place a player could name
("a poor hill town of shepherds, stubborn, loyal to the old house") that follow from those two.
4. Character has effect: what the place yields, what troops it raises, how it takes a tax, a new lord
or a faith, what it resists. 5. Two places on different ground differ; the same ground with different
people differs. 6. Character changes slowly when its causes change: migrants change the people; a mine
changes the ground's use; a sack leaves a mark. 7. It is not arbitrary: a trait with no cause in ground
or people is a label; a cause with no trait is unused data. 8. Feedback: the player can read it and
predict from it. 9. [GENRE] character gives a place a reason to be wanted or avoided.

