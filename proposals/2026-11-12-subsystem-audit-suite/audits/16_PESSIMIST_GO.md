# GO — pessimist audit: NERS, premise and emergent narrative, of the port, the port gate and the player-facing layer

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 826b747 (working tree)

Scope: `godot/`, the port-gate positions GO-07..GO-16, the typed exports (`engine/engine_params/` and
their exporters), the oracle recorder, the player-surface contract, the auto/manual doctrine, cognitive
load; and the five premise sentences of presentation: *a player sees what their character could see*;
*a player can read why a thing happened*; *a player can choose a lever and see its effect*; *a duel and a
battle can be watched, steered or skipped*; *the story the world tells is legible as a story*. The
emergent-narrative method is applied here to **legibility**: what a player could be shown today, from the
data the oracle exports, of the stories the engine produces. Prior work cited, not redone:
`11_GO_audit.md`, `11_GO_audit_addendum_B.md`, the `11_GO_*` proposals, `16_PESSIMIST_GAME.md`,
`18_DETERMINISM_SWEEP.md`, `20_NARRATIVE_CHURN.md`. Everything measured here is new work unless a lane is
named. All runs: `PYTHONHASHSEED=0`; scripts and outputs in
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_GO/`.

**IN PROGRESS: this head was written before the reading finished; sections are appended in the order they
are established and the verdict is rewritten last. If this line is still present, the lane was
interrupted and what follows is partial.**

## 0. Verdict

`[PENDING — rewritten after the probes]`

## 2. Premise audit — the five sentences of presentation

### 2.0 The first account: what each sentence means in ordinary words (written before the probes ran)

Written from the words alone, as a player of strategy and role-playing games would take them, and
committed to this file before any measurement below existed. Each link is a thing the game must do
for the sentence to be true.

**P1. "A player sees what their character could see."**
(a) The character has a place, senses, company and holdings. (b) The player is shown what lies within
them: where he stands, who is with him, what he holds, what he has been told and by whom. (c) The
player is not shown what lies outside them: a death in another town is unknown until word arrives.
(d) What is shown may be wrong, because a rumour is shown as a rumour. (e) The converse holds too:
nothing the character could plainly see (his purse, his wound, the people in the room) is hidden from
the player. *Genre:* a Crusader Kings player expects an omniscient ledger and would be surprised by
darkness; a Disco Elysium or Pentiment player expects exactly this sentence. Both would be surprised
if the menu of actions named a thing the character has never heard of.

**P2. "A player can read why a thing happened."**
(a) A thing happened that the player knows of. (b) It had causes: a person's act and that person's
reason, or a process of the world. (c) The game shows the cause as far as the character could know
it: who did it, in answer to what. (d) Where a roll decided it and the roll was his own, he is shown
what went into it and how it fell. (e) Where he cannot know, the game says "unknown", not nothing.

**P3. "A player can choose a lever and see its effect."**
(a) Several choices are offered that a player can tell apart. (b) Before choosing he can anticipate
what each would do: the chance, the cost. (c) Choosing one rather than another changes what happens.
(d) The change is shown to him and is traceable to the choice, at once (the result of the act) and
later (what others did about it).

**P4. "A duel and a battle can be watched, steered or skipped."**
(a) A duel or battle occurs with the player's person in it or near it. (b) *Watched:* an account of
its course, blow by blow or phase by phase, is presented with no input. (c) *Steered:* at decision
points his input changes the course. (d) *Skipped:* the outcome is produced at once, by the same
resolver, at the same odds. (e) The three are one fight, not three.

**P5. "The story the world tells is legible as a story."**
(a) The world produces sequences of events that answer one another. (b) A record of them exists.
(c) The record can be read in order with who, what and in answer to what. (d) Someone inside the
world, and so the player, can follow at least one thread from its opening to its end. (e) The things
in it have names a person would say aloud.
