# R08 — The ten goal axes and the arc criterion

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> People are generally trying to accomplish goals across the following axes:
> (1) suppress Einhir Revival;
> (2) hide threadwork truth;
> (3) overthrow Church of Solmund;
> (4) overthrow Einhir caste system;
> (5) purge Altonian influence from peninsula;
> (6) maintain or expand political authority;
> (7) increase standing within a faction;
> (8) benelovent community actions;
> (9) heal the Calamity;
> (10) revive Einhir heritage
> 
> 
> not exhaustive, but these are major. an arc for a character needs to be something narrative that affects themselves and their world in some manner

---

**The ten axes work as the "thrust" layer.** The repo's goal rows cover four of them. Two more have partial rows. Three have none, and caste and healing lack a place in the engine for the world effect to land. I ran nothing new for this; the table comes from reading `goals.yaml` (38 rows), the `writes:` lists in `verb_table.yaml`, and `canon/03`.

**Your criterion as a test.** An arc is one actor's goal-driven chain with a self effect and a world effect, linked by `causes[]`.
- **Self effect:** a write lands on the actor's own standing, holdings, stance, capability or knowledge.
- **World effect:** a write lands on a store the actor doesn't own. That means a Record, Site, Rung, DocketItem or someone else's Tenure or stance.
- **Static check:** `verb_table.yaml` already lists each verb's writes, so a ladder can be checked before it runs.
- **Findings-only verbs:** at least nine verbs write nothing (`examine`, `interview`, `research`, `surveil`, `thread_read`, `reconstruct`, `tell`, `construe`, `comply`). They can open a ladder but cannot supply the world effect alone.

| # | Axis | Goal rows today | Ladder in existing verbs | Gap |
|---|---|---|---|---|
| 1 | Suppress Einhir revival | Church: suppress Restoration, root out heresy; Inquisitors | surveil, interview → open_case → arrest → determine; destroy_record or seize texts | none. `pardon` and `forgive` give soft endings. |
| 2 | Hide threadwork truth | none; Varfell's row is the opposite pole | conceal, destroy_record, forge → construe, argue → oblige | no row; exposure is the counter-arc |
| 3 | Overthrow the Church | Hafenmark: suppress Church influence | covenant, oblige → petition, carry → convene → determine | only the rung above in the same faction can strip a seat (ED-IN-0256 ruling 3). An outsider's route is force (`seize`). |
| 4 | Overthrow the caste order | Restoration: end the caste (no referent) | argue, tell → covenant, found → establish | caste has no store in engine code; canon calls it informal geographic stigma. No row defends it. |
| 5 | Purge Altonian influence | Crown: resist Altonia (resist, not purge) | surveil → open_case, arrest → revoke, requisition | the Kommerkiarios row keeps the trade treaties in force, a built-in opposing pole |
| 6 | Maintain or expand authority | Crown, Hafenmark, councils | confer, oblige → issue, establish → determine, succeed | well covered |
| 7 | Standing within a faction | none; only 2 of 38 rows attach to a seat | work, comply → give, exchange, tie → petition → determine | no personal-level row |
| 8 | Benevolent community action | Knights of the Peace, Cardinal of Prudence | work, restore, tend → give → build, found | no personal row; the world effect is clear (Site condition) |
| 9 | Heal the Calamity | none | thread_read → restore | no thread-operation act in the loop (`WR_world.md` T-WR-7, T-WR-11); `restore` can't be told from mending a wall |
| 10 | Revive Einhir heritage | Restoration: revive the Einhir way | research, reconstruct → create_record, train → found, carry, tell | covered |

**What this implies**
1. **Tension is already authored for four axes.**
   - 1 against 10 is a direct opposition, with both rows in `goals.yaml`.
   - 5 against the Kommerkiarios treaty row.
   - 2 against Varfell's "Thread truth accessible".
   - 3 against Church orthodoxy.
   - Missing poles are what block arcs on 4 and 9. Nobody defends the caste, and nobody opposes healing.
2. **Non-lethal closure is natural for every axis.** Closing acts are a determination (1), exposure or containment (2), schism or seizure (3), establishment (4, 10), revocation (5), conferral (6, 7), a completed work (8) and restoration (9). Nothing requires death or a fight against authority.
3. **My toy's ladders were placeholders.** Its "accuse" step stands in for what the axes need: a case opened, a record destroyed, a determination won. The stage predicates need to be typed per referent: person, record, seat, rung, site, or institution-wide orientation.
4. **Real ladders will stall at the substrate.** In one measured seed, 929 of 1,318 acts were refused, so a ladder step can exist and still not execute.

I haven't mapped the 46 character cases onto the axes. That, and rebuilding the toy's ambitions by axis, are the obvious next steps.

[ASSUMPTION: my axis-to-row mapping is a judgement from the row text, and the ladders are my proposals, not canon.]
[GAP: whether each listed verb executes in the current loop is unverified.]
[CONFIDENCE: medium — it rests on reading the data files, with no new run.]
