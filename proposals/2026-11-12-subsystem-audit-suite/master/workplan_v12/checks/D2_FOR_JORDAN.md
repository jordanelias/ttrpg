# D2 — the one setting of B98.23 to B98.58 the ladder could not decide

## Status: REFERENCE (a decision register for lane D2's rows; resolves nothing at runtime, CLAUDE.md §0.05; not canon; deleted with the suite when v12 is adopted)

The form is `unified/DECISIONS_FOR_JORDAN.md`'s. Every other design-blocked row of `workplan_v12_part44_cont.md` was answered by the five steps (`D2_APPLIED.md`). One survives them.

---

### D2-1 · Does a fighter's lean also trade his own defence for attack? · PC

**What the game does today.** In a fight, a fighter can lean `defensive`, `normal` or `aggressive` in each phase. A lean moves draws the engine already makes: how deep he commits, how often he counters, and whether he tries to break a bind. A fifth term is built and switched off: `APPROACH_SIGMA_K`, set to 0. When it is above 0, every point of lean adds that much to the fighter's own attacks and the same amount to attacks made on him. It is conserved: nothing is created, it only moves between attack and defence. At 0 the fight is identical to one without the term.

**The question.** Should that transfer be switched on, at a value the workbench picks, or stay at 0?

**Option A — stays at 0 (as built).**
- *Feels like:* an aggressive lean is a matter of commitment and counters only. A reckless fighter is not automatically easier to hit; whether he is depends on what his commit and counters expose.
- *Costs:* nothing. The transfer stays as dead code behind a zero dial. A fight's length and bloodiness answer to the leans' three gates and to A-31's damage scale only.

**Option B — switched on at a calibrated value.**
- *Feels like:* leaning becomes a visible choice of intensity. Two aggressive fighters make a short, bloody exchange; two defensive ones make a long one that may end undecided. A player can choose how dangerous a fight is for both sides.
- *Costs:* it is the one lean term that no primitive produces: a flat amount added to the σ sum, conserved but invented. Your formations principle says instructions "modulate primitives — never add a flat number", and the design states this objection itself ("The case against the transfer, stated so the choice is visible"). The calibration would sweep the grid of `LAPSE_K`, the sibling coefficient (0.02 to 0.3), and keep the smallest value at which the nine-cell arming mirror stays level within its band and mean rounds fall as the summed lean rises. Every season fight with a non-normal lean then moves.

**Recommendation.** A. The three leans already give a fighter a choice of intensity through draws the engine makes. D-40 was closed by the ladder on your formations principle, with "B behind a dial at zero, set after D-39". A-31 has now landed, but nothing in the tree makes the flat term necessary. If you want intensity as a choice in its own right, answer B. B98 then runs it as a flip in the same form as B98.38.

**If you do not answer.** A: `APPROACH_SIGMA_K` stays 0. B98.26 is a reading, and B99 quotes the value as left.

**Blocks.** Nothing else in v12. B98.26 only.

**Sources.** `master/workplan_v12/workplan_v12_part44_cont.md` B98.26; `workplan_v12_part23.md` B16.08; `proposals/03_PC_duel_round_and_approach_B.md` §3 ("The case against the transfer"), §7 row 3c, §11; `unified/DECISIONS_ANSWERED.md` D-40 (ladder table), A-31; `modules/combat/config.py` (`LAPSE_K`'s grid).
