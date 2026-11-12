# MB — pessimist audit: NERS, premise and emergent narrative, of mass battle

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 2eba83c (working tree)

Scope: `modules/mass_battle/`, `systems/mass_battle/sim/`, `engine/season/loop/effects_army.py`, the host
seam (`engine/season/seam/wrappers/mass_battle.py`, `loop/sides.py`, `loop/effects_combat.py::_eff_march`),
Jordan's stated intent for mass battle (`AUDIT_BRIEF.md`: the cell-based army → unit → subformation →
troops hierarchy; mixed weapons at a fatigue and movement cost, archers carrying arming swords; Football
Manager, Total War, Ogre Battle, Unicorn Overlord, Bannerlord; the commanded and the auto-resolved battle
as one resolver), and five premise sentences of a battle. The first audit (`audits/04_MB_audit.md`,
F-MB-01..19) and its addendum (`04_MB_audit_addendum_B.md`, F-MB-20..26) and the ten `04_MB_*` proposals
are cited, not redone. Everything measured here is new work unless a finding id of theirs is named.

All runs: `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_MB/`.

(Sections below are appended as the work proceeds; §0 is written last and placed first.)

## 2. Premise audit

Method: `skills/premise-check/SKILL.md`, SLICE scope (the five sentences the work order names). The
ordinary account O in §2.1 was written before any module file was opened by this lane; what this lane
already knew of the code came from the first audit's §0 and §1 and the addendum's §B0, and O was written
from the words, not from those.

### 2.1 O — what each sentence should mean (written first)

**P1 "A flanked line breaks."**
1. A line is a body with a front; its front faces one way. 2. Flanked means an enemy body is in contact
with its side or rear while (or instead of) its front. 3. The flanked body fights worse on the flanked
side than it would on its front (fewer men can bring weapons to bear, no shields that way). 4. It also
loses heart faster than from the same losses taken frontally. 5. "Breaks" is a morale event (rout), not
annihilation: it should come sooner, at a lower loss, than in the frontal control. 6. Proportion: rear
worse than side, side worse than front; two flanks worse than one. 7. Not certainty: a steady, deep or
elite body sometimes holds a flank attack; "breaks" is the usual outcome, not a fixed one (standing
rule). 8. Zero: a line with nobody on its flank gets none of this. 9. Feedback: the record says it was
taken in flank. 10. [GENRE] the flanker needs to get there: flanking costs time or a manoeuvre, and a
commander can order it or guard against it (refuse a flank, reserve).

**P2 "A larger army usually wins but not always."**
1. Size is headcount. 2. Equal quality, equal ground, even numbers: about even, and swapping sides swaps
the result (mirror). 3. Win rate rises monotonically with the size ratio, with no cliff: 1.2:1 a modest
edge, 2:1 a strong one, 3:1 near-certain but still under 100% over many fields. 4. "Not always": at
ordinary ratios (1.5:1) the smaller side wins a visible share, and quality, ground or luck can be the
reason. 5. It holds at every scale the game fights at: 30 against 20 and 3,000 against 2,000 give
similar odds (or differ for a reason the words give). 6. The winner pays: the larger army's losses are
smaller in proportion but not zero. 7. Bounds: 1 man against 100 loses; 0 does not fight. 8. Feedback:
the result says who won and by how much.

**P3 "A pike block holds against cavalry."**
1. A pike block is infantry whose weapon is the pike, in close order, facing the charge. 2. Cavalry
charging its front does markedly worse than the same cavalry charging the same number of other infantry
(swords, levy, archers): control by troop type. 3. "Holds" means it does not rout and keeps its ground
for the engagement, usually; cavalry sometimes breaks in (draw). 4. The protection is frontal and
depends on order: cavalry into the flank or rear of pikes does well; disordered, tired or thinned pikes
hold less. 5. Pikes are not thereby good at everything: against swordsmen who close, or archers, they
should be ordinary or worse (otherwise "pike" is a dominant choice). 6. The word is the weapon: remove
the pike (same men, other weapon) and the effect goes.

**P4 "A tired unit fights worse."**
1. Tiredness is a state that rises with marching, fighting, charging and (per Jordan) carried kit, and
falls with rest. 2. More tired, worse fighting: monotone, starting before exhaustion. 3. "Worse" shows
in the outcome: the tired side of an otherwise even field loses more often and takes more losses.
4. Tiredness that arrived before the battle (a forced march) counts: a campaign-scale state enters the
field. 5. It persists and recovers on a readable clock. 6. A fresh reserve committed late beats a tired
front line (the reason reserves exist). 7. Heavier troops tire faster. 8. Bounds: at maximum tiredness a
unit still fights, badly; it does not vanish or become immune.

**P5 "A routed army can be rallied or destroyed in pursuit."**
1. Rout is a state distinct from destroyed: the men are alive and running. 2. Two exits: rallied (they
re-form and can fight again, now or later, at a cost) or run down. 3. Pursuit is an act by the winner
(or a standing order), most effective with fast troops, and kills or captures the routed. 4. Rallying
is an act by a commander, depends on him (presence, leadership) and on not being pressed, and may fail
(draw). 5. So the same rout has different ends depending on what both commanders do and on a draw.
6. Most of a pre-firearms battle's dead fall in the pursuit, so pursued-against-not-pursued should
differ largely in the loser's losses. 7. After the field: a routed army that was not destroyed exists
somewhere on the map, weaker, and can be met again. 8. Feedback: the record tells rout, rally and
pursuit apart.

