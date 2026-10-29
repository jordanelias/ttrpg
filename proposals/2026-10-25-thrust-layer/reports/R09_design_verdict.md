# R09 — Design of the thrust layer by agonist-antagonist methodology (verdict after the relay)

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> design using agonist-antagonist methodology how to make this "thrust" layer possible

**Correction recorded after delivery:** this report says the candidate-typing decision "is unruled and sits in no workplan". That is wrong: it is the open ruling H-156 (`engine/season/hole_register.yaml:3615`). See `../02_MAJOR_TAKEAWAYS.md` §9.

---

**The thrust layer is designable under the repo's rules, but not buildable yet.** Every closure route ends through verbs that the measured run refused almost every time. The design is at `proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md` (565 lines). It is a proposal only. Nothing in the repo was touched, committed or given a plan position.

**How I ran it.** An opus producer drafted v1. An opus critic that was read-only saw only the file and the tree, and attacked it. I re-opened six of its findings (F1, F2, F4, F6, F10, F13) before applying them. v2 is one reconciliation with no second wave. The critic opened about 125 citations: 114 held, 9 failed, 2 could not be verified.

**The design**
- **Thrust:** an existing ambition (a `commit` to an OUGHT) plus an authored ladder of typed stages in `goals.yaml`. A roster of ten axes lives in `rosters.yaml`. The current stage is read from the person's own ledger every time, so there is no arc store.
- **Starved `need` question:** the stage's referents enter that question. It is promoted to the top tier for one season in every deadline period, with a staggered per-person phase. Only aligned people are promoted (the A-33 rule that a misaligned head answers his own want first), and only when a candidate can form.
- **Closure, using only lawful forms:**
  - a threshold that raises a docket matter, writes nothing, and leaves the judge's choice;
  - a bound peace;
  - authored contest forms;
  - succession is left to the ruled IN-61.
- **Your constraints:** a beaten fighter ends "down", with a new `Slain` band kept for rare deaths. A deterministic standing gate builds on the existing access gate. Killing consequences ride existing carriers.
- **Arc test:** a self effect and a world effect, linked by `causes[]`, drawn from named field rosters and read at the driver.

**What the critic broke, all fixed in v2**
1. **The arc test was vacuous.** Every witnessed act deposits a claim, and the gate mints a receipt for it. So "moved and was seen" counted as an arc (`loop/witness.py:654-657`, `state/world.py:1144-1160`). The test now uses explicit field rosters, plus planted cases that must read FALSE and a bookkeeping null.
2. **My succession piece duplicated a ruled position.** It chose the carrier Jordan rejected (IN-61, `workplans/valoria_master_workplan_v9_part5.md:129-133`), so I deleted it.
3. **The standing gate protects three seats of 31.** The seats you mean by "authority" are unguarded, and the existing goal rows already target them (`goals.yaml:159-163`). v2 requires authoring guards for them and measuring harm to seat-holders.
4. **My starvation fix would have repeated the measured news regression.** All goal commits are minted at season 0, so every stage came due on the same tick. v2 replaces it with the staggered pulse.

**Blocked or open**
- **Closers.** `determine` was refused 7 of 7, `confer` 4 of 4 and `commit` 74 of 74 in the one measured run, and the candidate-typing decision that would reduce this is unruled and sits in no workplan. The cheapest remaining test that could sink the design is counting executed closers over several seeds.
- **Inherited gaps.** Axis 9 is out of scope until a thread-operation act exists. Axes 2 and 4 need authored content, and I read the Church as holding axis 2 from canon, which is an assumption for Jordan to correct.
- **For Jordan:** whether a beaten fighter is ever killed outright (and where the `Slain` edge sits), and where "a sequence of stages" ends and "an entire arc" begins under the 2026-08-18 ruling.

[CONFIDENCE: medium — the design is checked against the tree, not run, and its toy-world evidence is low-grade; the document lists the falsified predictions beside the confirmed ones.]

The files are in `proposals/2026-10-25-thrust-layer/toy/`: `thrust_layer_design_v2.md` is the revised design and `thrust_layer_design_v1_as_attacked.md` is the version the critic saw. The critic's full report existed only in this conversation. The design's last section carries its findings and my dispositions, and I can move the file to `proposals/` if you want it in the repo.
