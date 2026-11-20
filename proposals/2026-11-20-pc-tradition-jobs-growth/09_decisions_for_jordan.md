# Part 9 — Decisions for Jordan, ranked

## Status: PROPOSED. Each decision passed CLAUDE.md §0's filter (superseded? irrelevant? answered by a design document? by precedent? by what makes sense for the architecture?) and survived it: two defensible options lead to materially different games, or the answer would overwrite a ratified rule. §9.2 lists the questions the filter answered, so none of them waits on Jordan.

## 9.1 The decisions

### D-1. The job model: shared curriculum with a personal path (J-D)

- **Recommended: J-D** (Part 1). A tradition is a shared curriculum in short lines; each person walks it by a path (authored for notables, generated from the lifepath for everyone else); a primary tradition fixed by history; a second one after a threshold; at most one personal set for a notable.
- **Cost of the others.** J-A (shared ladder): cheaper, and every member of a school at a rung is the same fighter. J-B (job-swap): a per-fight decision and an NPC rule with no historical ground; invites a per-tradition bonus to make the swap matter. J-C (bespoke line alone): breaks "every build available" for notables and gives generated persons no growth.
- **Why it is yours.** It decides whether Valoria's fighters are members of schools, owners of careers, or both.

### D-2. The board's budget (brief D-A)

- **Recommended: slots per column plus attention, attention read from Concentration** (Part 2 §2.3.3): how much a fighter can hold in mind, not how strong. Fight experience and sparring raise it through PC-22's Concentration; a drilled technique costs less.
- **Cost of the others.** Slots only (everything learned is on): cheapest and right while a person knows little; loses preparation once cross-training makes the pool larger than the board, and is the recommended first increment. Troubleshooter's three budgets: needs a character level Valoria does not have, and the per-column cap duplicates the slots. **A power budget (equal points per stage) dies under the fiat audit** ("expressive availability, not parity").
- **Why it is yours.** It ties personal combat's breadth to the Concentration function PC-22 has not yet defined; if Jordan wants Concentration to stay a bout resource only, the budget needs another source.

### D-3. Sets (brief D-C)

- **Recommended: n-ary recipes of 3–4 techniques; the effect is one opened gate or one board rule, never a magnitude; recipes visible; at most three per tradition; a member counts at level 3+** (Part 3 §3.3).
- **Cost of the others.** Troubleshooter's sets (flat bonuses, forced outcomes): a tradition weight by another name (ED-PC-0023, ratified) and fiat. No sets (pairwise `requires`/`widens`/`branch` only): cheaper, and loses the one structure players of every precedent call satisfying, a named goal assembled from parts.
- **Why it is yours.** Whether a school's identity is allowed to show as *what its fighters can attempt* (a gate) is a design choice the fiat audit permits but does not make.

### D-4. The one module change: a `gate` slot family (brief D-D)

- **Recommended: add a `gate` slot family with four members, each an existing `if` and closed by default** (`counter_shallow`, `steal_shallow` at `wrapper.py:325`; `grab_close` at `contact.py:27-36`; `withdraw_band` at `combat_systems.py:857`). Player-facing access waits for B16's per-round choice set, on B18.09's `switch` precedent.
- **Grid and special abilities, answered.** Optional gate predicates on a technique (range, facing, terrain, adjacency): add only those naming a state the engine computes (measure, facing, armour tier, the weapon in hand). Terrain and adjacency are not added: no engine state carries them, and a field with no reader is refused (ID-13). **If a grid is never built, nothing breaks**, because nothing names one. A special active ability as an injected transition: it is a `gate` member (engine-side) or a choice-set member (player-side), paid from attention; the `techniques` field carries it as a number per slot after B18.02.
- **Cost of the others.** Access through the choice set only: every granted behaviour becomes a player decision, which an NPC must also make, and most of the four are beats, which the player never decides (agency proposal §2, T2). No access kind at all: sets can only be board rules, and a technique can only ever be a number.
- **Why it is yours.** It is the only edit to `modules/combat/` this proposal needs, and it widens Class B (agency proposal §5) by two rows (`counter_shallow`, `steal_shallow`) that no ruling has admitted yet.

### D-5. What a board is judged by (the earlier draft's decision 8, now measured)

- **The measurement.** In a mirror against themselves with an empty board, the six generated sheets' boards move the win rate by +0.0 (no school), +3.7 (novice), +10.3 (practised), +10.8 (cross-trained), +17.0 (veteran) and +20.8 points (bespoke), n = 400 each (Part 8; Part 4 §4.4b).
- **Recommended:** keep the agency proposal's band (|Δ| ≤ 2 points, texture ≥ 15%, flips 3–10%) as the **calibration test for one technique at level 1**, which is what it was measured on, and judge a **board** by the fiat audit's instrument (texture, outcome not decided by label) plus one stated ceiling per growth stage that Jordan sets or declines to set.
- **Cost of the others.** The band applied to boards: no practised fighter may be better than an untrained one, which makes teaching worthless. No ceiling at all: the veteran's edge grows with every lever that is built, unbounded except by the clamps.
- **Why it is yours.** It is the fiat audit's "some builds are stronger and that is fine" given a number.

### D-6. How far Addendum 6's relaxation of the source-tier rule reaches (a conflict with a ratified rule)

- **The conflict, named.** This session's instruction (brief Addendum 6) lets a technique appear without a documented source and lets Chinese and Filipino be authored. The agency proposal calls the source-tier discipline "not negotiable" (§4.3; PROPOSED) and the archived armature says "no technique, no ability" (archived, not binding). **No ledger row rules the source-tier rule itself** (searched `registers/editorial_ledger_pc*.jsonl` for "source-tier", "source tier", "S1/S2 anchor", "no technique, no ability"; none). But **ED-PC-0026 is ratified**: it removed real period terms wired onto the wrong lever (`winden`, `guardia`). Part 3's NEW Chinese and Filipino entries carry period terms from my own recollection (`lan`, `na`, `zha`, `zhan`), which is exactly the error class ED-PC-0026 removed.
- **Recommended:** adopt Addendum 6 as the PC lane's standing rule, with the INSP / INV / RECALL label kept on every entry; and **until a NEW technique's period term has been checked, it ships under its plain name only** ("block and seize", "the thrust", "sticking", "the live hand"), so a mis-wired term cannot enter the engine.
- **Cost of the others.** Keep the old rule: Chinese and Filipino stay empty and every invention in Part 3 is withdrawn. Relax it without the label: Jordan can no longer see which parts are history and which are design.

### D-7. May a teacher's own level gate `train`? (a change of principle)

- **Recommended: yes, for techniques only**: `train` raises the next technique on the subject's path when the actor holds it at a higher level (Part 4 §4.2). Today "the ACTOR's own capability is NOT read: capability gates nothing" (`effects_combat.py:918-919`).
- **Cost of the others.** No teacher gate: anyone can teach anything to level 8, and the scarcity that makes a master worth seeking disappears. A currency instead: the grind every precedent reports (Part 4 §4.4).
- **Why it is yours.** It reverses, for one family of writes, a principle the `train` verb was built on (#353 §9.2, as cited in its docstring).

### D-8. The 21 generics become tradition-neutral (brief D-B, answered except for this)

- **Recommended: yes** (Part 3 §3.5): any person may learn them; the Latin square's import-time coupling to the roster dies, so an eighth tradition no longer needs them retired first.
- **Cost of the other.** Keep the square: a person with no school can learn nothing, and adding a tradition raises `ValueError` at import (`ability_primitives.py:113-114`).
- **Why it is yours.** The generics are PROVISIONAL under your own permission (ED-PC-0059, "a spread of generics for now"); changing who may learn them changes what they are for.

## 9.2 Questions the filter answered (not escalated)

| question | answered by | answer |
|---|---|---|
| what to call the layer | precedent: B18.06 glossary gives "loadout" to weapons and armour | "tradition board" |
| per-column cost caps | architecture and the user's own board (the pool binds first) | dropped |
| hidden set recipes | precedent (Part 6 complaints) and §0.06 E | visible |
| set magnitudes | ED-PC-0023 (ratified) | never |
| growth by use (Tactics Ogre, SaGa, FFT JP) | superseded by Jordan's 2026-11-07 ruling | rejected |
| where choice comes from (brief D-B) | architecture | own curriculum + generics + a second tradition; binding once a person knows more than the board holds; the source-tier part is D-6 |
| cross-training through today's door (one tradition name per fighter) | B18.02 (host-side gate) | disappears when B18.02 lands; nothing to build before it |
| stacking two techniques on one lever | architecture (the product compounds; Ysolde's ×14.8, Part 8) and B15.13 owns the sweep | one technique per lever on a board |
| the counter's reach saturating at level 3 | the repo's own `lever_log_edge` precedent (ED-PC-0045) | a lever-form fix for the PC lane's B15.13 sweep; reported in Part 4 §4.4b, not built here |
| where the person's state lives | the plan (PC-21) | input given (Part 5); not decided here |
| grid predicates | ID-13 (no field without a reader) | only predicates over states the engine computes |
