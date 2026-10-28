# R14 — Register producer's hand-back (the missing-in-code register, v1)

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). This is the agent's hand-back message, reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Under CLAUDE.md §0 an adversarial pass is a stage, not a deliverable; this file records a terminal verdict about artifacts that already exist, as the §0 exception permits, and asks nothing of a future session.

**Role:** producer (agonist) of the missing-in-code relay. **Wrote:** the v1 register (29 entries; not committed; the register committed is v2). The producer found two errors in the orchestrator's brief (`REFUSAL_KINDS` is at `data/verbs.py:1403`, not `:1073`; "51 of 803" does not reproduce as defined). **Model:** not recorded in this file.

---

I wrote the register: 29 entries, one table per takeaway. I changed nothing in the repo; `git status --short` was empty after every run, and no harness command folded a tracked file.

**Document:** `missing_in_code_v1.md (not committed; superseded by proposals/2026-10-25-thrust-layer/01_MISSING_IN_CODE.md)` (204 lines, but most are wide table rows).
**Sections:** 0 status and scope · 1 method and grades · 2 the probes (P1–P9) · 3 the register (T1–T8 tables plus a tally) · 4 what is not missing · 5 dependency order and decisions · 6 what would make it wrong.

**Entries by grade:**

| Grade | Count | Entries |
|---|---|---|
| PRESENT-BROKEN | 9 | G-01–06, G-14, G-15, G-27 |
| ABSENT-RUN | 5 | G-07, G-09, G-17, G-18, G-21 |
| ABSENT-READ | 7 | G-13, G-20, G-23, G-24, G-26, G-28, G-29 |
| PRESENT-INERT | 4 | G-16, G-19, G-22, G-25 |
| PRESENT-USED, narrowed | 4 | G-08, G-10, G-11, G-12 |

Ten rows are owned elsewhere (G-06, G-07, G-14, G-15, G-17, G-18, G-21) or already designed in the thrust-layer doc (G-13, G-19, G-28). They are listed so nobody designs them twice.

**Probes** (all in `.../scratchpad/probes/`, run with `PYTHONHASHSEED=0`, each output saved beside its script):

| Probe | Result |
|---|---|
| P1 refusal census | 76.2% of acts refused over 2 seasons and 76.8% over 4 (seeds 0–4), using the driver's own refusal rule. Closers executed/attempted at 4 seasons: determine 3/43, confer 10/111, covenant 0/70, commit 8/564, revoke 0/32 |
| P2 goals and `need` | 12 of 38 goal rows mint a Proposition. Both seat rows are on foreign seats, so no seat-attached goal binds anyone in the shipped realm. `need` is 24–27% of scenes, but only 7–8% are about a goal |
| P3 / P3b refusal causes | 33.1% of admissions are refused only because the subject is the wrong kind of thing. None are eligibility refusals |
| P4 deaths | 20 deaths in 20 seed-seasons, 11 of them by an `accept` with no challenge behind it. No claim names a dead holder's seat, and nothing points anyone's questions back at the killer |
| P5 dark switches | `body_step`, `illness_rate`, `season_factor_draw` and `lattice_coupling` all change the world when set. `age_at_build` does nothing on a built world, because `Person.born` is fixed when the person is constructed (`state/carriers.py:687`) |
| P6 case termini | 28 of 46 cases have no authored terminus by a text rule. I wrote the rule after reading the 46 strings, so its agreement with your count is not independent |
| P7 story chains | 55 of 66 deepest-chain acts were refused acts; that is the story instruments, not a number from them |
| P8 threadwork | No threadwork module loads during a season run |
| P9 committed aperture | Its own control holds (equal hash with `populated.run`) |

Every run checks that it happened: content hashes differ by seed and match across P1–P4 and P7.

**Findings not in the brief or the thrust-layer doc:**
- **G-02: the committed per-verb census misses refused contested acts.** A contested act refused before its contest never reaches `SeasonDriver.resolved` (`loop/resolve.py:1039-1045` against `:377-379`), and `corpus_run.attribute` counts from that list. Aperture therefore reads `accept` as 4 attempted, 4 executed, when it was 48 attempted with 44 refused (seed 0, 2 seasons).
- **G-03: two definitions of "refused".** The driver counts a lost `tell` as refused; `attribute` counts it as both executed and refused.
- **G-27: `storybar` and `chronicle` count refused acts as chain links.** The cross-person share falls from 30.4% to 17.9% when only executed acts count.
- **G-16: a non-lethal duel already exists but is unwired.** RS-25 rules a non-lethal option in, and PC-10a built it in `modules/combat/wrapper.py`, but the season never passes it any terms. That partly answers the thrust-layer doc's D1, and makes its proposed `Slain` band a second mechanism for the same thing.
- **G-15:** PC-10b's planned refusal of an `accept` with no challenge would remove most measured deaths.
- **Naming:** the key `ladders` already means two other things in this package, so the register proposes `goal_stages`.

**Could not verify:**
- Why `arrest` is never formed.
- Whether `survey` mints a `works` record the actor holds, which `build` and `found` need.
- Whether any shipped case falls back to inferring its institution from `ends_when` prose.
- That wrapping `_admits` and `resolve` on the driver instance sees every call. Admissions (7,737) exceeding attempts (7,402) suggests it saw at least every attempt.
- P4 matches claims against end-of-run ledgers, so a claim evicted before the end would be missed.

**Brief corrections:** `REFUSAL_KINDS` is at `data/verbs.py:1403`, not `:1073`. "51 of 803" does not reproduce as defined; the nearest reading is 43–53 goal-anchored `need` scenes out of about 620 per seed.

**Decisions for you:**
1. Whether G-02 and G-03 come first. They change figures other sessions have quoted from aperture, soak and the corpus. Fixing G-03 also changes whether a lost `tell` is retried, which moves the hash.
2. G-01 (refuse wrong-kind acts before they are formed) raises a Layer 1 question: stamping every question referent with its kind adds a field to `Question`. That goes to `layer-conformance` Lens B, not to Jordan.
3. Escalate only two things: the default `fight_terms` for a fight nobody negotiated (a value that makes materially different games), and PC-10b's route under H-240, which the plan already gates on Jordan.
4. The narration proposal's open S12 question (decline wrong-kind acts at formation, or let them refuse) I answered from precedent: IN-53 already declines wrong-kind `confer` formations. Override if you read it differently.

I spawned no agents.

---

## Brief given to the agent (verbatim)

The instruction the agent received, so a reader can judge what it was and was not told.

~~~text
You are the AGONIST (producer) in an agonist→antagonist relay for the Valoria repo at /home/user/ttrpg (branch ccr-6964ef63-wdjqoh, which already carries proposals/2026-10-25-thrust-layer/). Read /home/user/ttrpg/CLAUDE.md FIRST; its rules bind you, above all §0.05 (code is the mechanism, prose is reference), §0.1 pt 3 (the table of what to OBSERVE before claiming: "X is absent / dead / never fires" → RUN the thing that would show presence; "X works today" → open the CALL SITE, not the declaration; "as F says at :L" → open F at :L; "I ran it" → check the RUN HAPPENED, e.g. a generator that no-ops or a test that skips returns 0), §0.1 pt 5 (a guard must earn its existence), §8 (one owner per rule) and §10. A separate read-only critic will then try to find each absence you claim PRESENT, so an absence you did not try to refute by running something is not yet a claim.

TASK: produce a CODE-GAP REGISTER AND DESIGN: what is MISSING IN CODE (in engine/season/ and the files it reads at runtime — YAML registries, loaders, queries, effects, harness instruments, tests) to deliver the eight takeaways below, with the minimal code design to add each. This is NOT a restatement of the thrust-layer design (read proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md for what is already proposed; cite its sections instead of repeating them). Your job is the layer beneath it: establish, by execution and call-site reading, what the tree does and does not do TODAY, and design only what is missing.

HARD RULES
- Do NOT edit, stage or commit anything in the repo. Write ONLY to the scratchpad: the document at missing_in_code_v1.md (not committed; superseded by proposals/2026-10-25-thrust-layer/01_MISSING_IN_CODE.md) and probe scripts under proposals/2026-10-25-thrust-layer/probes/ (create it). Do NOT spawn agents.
- Harness commands can write tracked files (e.g. engine/season/runs/TRACE.txt is folded per call). After EVERY run that touches the harness, run `git -C /home/user/ttrpg status --short`; if a tracked file changed, name it in the document and restore it with `git -C /home/user/ttrpg checkout -- <path>`. Leave the tree exactly as you found it. Use `python3 -I` for scripts that read untrusted data; for harness imports run from /home/user/ttrpg.
- WRITE THE DOCUMENT'S HEAD AND §1 BEFORE YOU FINISH INVESTIGATING and append as you learn (a producer that has read far and written nothing is failing). Return only a SHORT RECEIPT: path, section list, count of register entries by grade, the probes you ran and where they are saved, anything you could not verify, and decisions the orchestrator must make.
- Every claim about the tree carries a path:line you opened, or a probe name and its result. Mark guesses [ASSUMPTION]. Do not assert a Godot engine version. Do not quote figures from proposals/2026-10-13-narration-mechanisms.md as if you measured them; either re-measure them with a saved probe or label them "reported there, not re-measured".
- Canadian spelling. No padding. Tables over prose.

THE EIGHT TAKEAWAYS (the thing to be made real in code), ranked:
1. The substrate mostly fails. Reported (one seed, two seasons, uncommitted scratch instruments): 929 of 1,318 acts (70.5%) refused/blocked/null; 439 (33.3%) aimed at a subject that exists as another kind; closure verbs refused (determine 7/7, confer 4/4, revoke 4/4, commit 74/74). My own chronicle runs of harness/chronicle.py (seeds 0,1,2,4,5, four seasons) read 53 of 66 deepest-chain acts as refusal-like by a suffix definition that over-counts degree bands. No narrative layer can work until closers execute. RE-MEASURE THIS with a saved probe: a per-verb census of attempted/executed/refused acts over several seeds (at least 5) of the shipped realm for 2 and 4 seasons, with the executed and refused counts for the closers determine, confer, covenant, open_case, commit, release, oblige, revoke, succeed, arrest, issue, petition, found, build, work, give, restore, tend. Use the repo's own definition of refusal (REFUSAL_KINDS at data/verbs.py:~1073) and show the check that the run happened (event counts, content hash changes across seeds).
2. A motive layer exists in part: ambitions are live `commit` tenures to OUGHT Propositions (queries/world_q.py ambitions, goal_referents, attention_key, Q4 `need`); reported: the `need` question won 51 of 803 deliberations; 24 of 38 goals.yaml rows are orientation-only and mint no Proposition (verify with a probe: count by object kind, and confirm what populated.seed_goals does with them); only 2 of 38 rows attach to a seat.
3. Arc shape needs a goal ladder under an ambition AND a closure form (toy-world result, low confidence; see proposals/2026-10-25-thrust-layer/toy/). Closure by settlement/bound peace works; plain exile and lethal-only closure do not.
4. Killing has no consequences today and the standing gate reaches 3 of 31 seats: `fight`'s Felled band deletes the person (verb_table.yaml row `fight`; loop/effects_combat.py via World.remove_person); a death never reaches anyone's questions (H-209) and a dead holder's seat is named by no claim (H-206) — check each by executing a planted killing in a built realm and reading what questions/claims result; the access gate admits_audience/guard_weight exists (world_q.py ~1250-1344) but binds only where guards are seated (cohorts.yaml guards: 3 rows; build_realm(guards=?) default).
5. Do not build: lookahead-steered choice, an arc carrier, forced outcomes. (No code needed; but check that nothing in the tree already does these by another name.)
6. The deepest premise is the least buildable: healing the Calamity has no act (thread operations unplugged from the season loop, research/by_lane/WR_world.md T-WR-7, T-WR-11 — VERIFY by call-site search, do not repeat their claim); hiding the threadwork truth has no goal row; caste has no readable store; exogenous motion ships dark (season_factor_draw, body_step, age_step, illness_rate, age_at_build in data/fixtures.py — verify the shipped values and what each switch would do if set, by probe where safe).
7. Authoring is the largest content job: of the 46 NPC case files (engine/season/cases/, via harness/run_cases.load_cases("NPC")), 28 have no authored terminus or only one the extractor presumed (my hand classification; ids in proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md is NOT the source — the toy README and this brief are; re-derive a defensible machine-checkable subset of this claim, e.g. which cases' ends_when contains an authored branch list, and say what you could not mechanise); the ten user axes (suppress Einhir Revival; hide threadwork truth; overthrow the Church; overthrow the Einhir caste system; purge Altonian influence; maintain/expand political authority; increase standing within a faction; benevolent community actions; heal the Calamity; revive Einhir heritage) need referent-bearing goal rows before a ladder can attach.
8. Metrics fail quietly: an arc/narrative predicate must be read beside a shuffled null and a bookkeeping null (claim deposits mint Receipts: loop/witness.py:654-657, state/world.py:1144-1160). What instrument code is missing: a driver-side ARC reader, a committed need-share/news.told instrument (harness/arms.py is wired to field_casualty_model only), a refusal census (item 1). Check what harness/soak.py, storybar.py, chronicle.py, aperture.py, arms.py actually measure TODAY (by running them or reading their call sites) and what each cannot.

REQUIRED CONTENT of the document (~350-500 lines):
 0. Status/scope (PROPOSED; reference under §0.05; creates no plan position). One paragraph: what this register is and is not.
 1. METHOD AND GRADES. The grade vocabulary you use for every entry, defined once: ABSENT-RUN (a probe that would show presence was executed and showed none), ABSENT-READ (call sites and owners searched, not executed), PRESENT-INERT (declared/loaded, no live caller or switched off — name the caller search), PRESENT-USED (a call site that executes, with evidence), PRESENT-BROKEN (executes but refuses/mis-writes — name the observation), UNVERIFIED. For each ABSENT entry state the probe or search that would have refuted it.
 2. THE PROBES: a table of every probe you ran (name, file under probes/, what it observed, the RESULT, the check that the run happened).
 3. THE REGISTER, grouped by takeaway (T1..T8). One row per missing or broken thing: ID (G-nn) | what is missing | grade | evidence (probe or path:line) | takeaway served | existing plan position / hole / ED that ALREADY covers it (search workplans/valoria_master_workplan_v9*.md, engine/season/hole_register.yaml, registers/ — a gap the plan already owns is NOT a new design item; cite it and say whether its scheduled form delivers what the takeaway needs) | minimal code design (owner file/module, data head per §0.05 cl.1, loader refusal, the falsifier AND the control per §0.1, the instrument) | Layer 1 question (yes/no, which row of architecture/meta/04_CODE_ARCHITECTURE.md) | depends on.
 4. WHAT IS NOT MISSING: things that look like gaps but exist and are used (with the call site) — including anything in the thrust-layer design that the tree already provides or already plans.
 5. DEPENDENCY ORDER: the minimal sequence, naming the cheapest observation that would show the register wrong, and which entries are blocked on an unruled Jordan decision (apply CLAUDE.md §0's five-step answering before escalating anything; TAKE the architecture-right option for the rest and record the reasoning).
 6. WHAT WOULD MAKE THIS REGISTER WRONG: one paragraph.
Order the register by leverage on the eight takeaways, not by file. Prefer fewer, sharper entries (aim for 20-40) over an exhaustive list; fold sub-gaps into one row with a sub-list.
~~~
