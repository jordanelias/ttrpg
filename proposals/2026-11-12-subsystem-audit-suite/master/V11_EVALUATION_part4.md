# Evaluation of workplan v11, part 4: lane E1, carry-forward blocks (verbatim)

## Status: EVALUATION RECORD, assembled (stage 5 of `STAGES.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when workplan v12 is adopted)

**What this part is.** The carry-forward blocks of lane E1, copied by script from `master/eval/E1.md` lines 295 to 2031, byte for byte; nothing below the rule was retyped or edited. Line numbers cited in the settlement ledger (`V11_EVALUATION_part2.md`) are those of the lane file, so a row of this part is found there as `E1:<line>`. Where the ledger re-dispositions a row, the ledger governs and the copy below keeps the lane's original call as the record.

---

## Carry-forward blocks

Verbatim extracts (made by script from the v11 files, not retyped): the part3 card row, then the content-owner entry (`-04`/`-04` part 2/`-11`/`-12` by heading; a `CP-*` entry from its home file by heading). Rows with a split suffix (`a`/`b`) share their position's block. A group heading (NM-W0..W9; CL-ATTR..CL-EVENTS) is copied once. Where a block says NO ENTRY FOUND the position's text is the card row alone.

### P1

head text (`valoria_master_workplan_v11.md`):

```
| P1 | The plan has one status column, the state index in `-03` §1; every row cites its evidence. If a row and its instrument disagree, the instrument wins and the plan is wrong. | §0.1 |
```

### P2

head text (`valoria_master_workplan_v11.md`):

```
| P2 | A `GATE` of `—` is buildable today. | §0.2 |
```

### P3b

head text (`valoria_master_workplan_v11.md`):

```
| P3 | Finished positions leave the plan; the commit is their record. A closed batch's rows are deleted in one net-deleting commit and the run stops for a cleared window before the next batch opens. **The stop is between batches, not inside one:** a card splits into several closes only for a risk it names (a run with no verification checkpoint, or a diff too large for `methodology-close`'s Phase 1 or Phase 3 to hold), and a position that is hash-EQUAL by construction (a deletion, a comment, config routing) joins a neighbouring close. This clarifies the row (B10-10b's six closes applied the stop inside one batch, 12.5 h for seven positions); it adds no rule. | §0.2; `CLAUDE.md` §2 |
```

### P4

head text (`valoria_master_workplan_v11.md`):

```
| P4 | No existing position number changes meaning; retired handles are never reused; a handle allocates no ledger id (an id is allocated when the position is built). | §0.3 |
```

### P5

head text (`valoria_master_workplan_v11.md`):

```
| P5 | One step is one position (or sub-position) is one commit. Phases per step: BUILD, then (per batch) `/code-review` and `/simplify`, FORWARD SWEEP, CLOSE. | §0.4 |
```

### P6

head text (`valoria_master_workplan_v11.md`):

```
| P6 | The forward sweep checks instruments, the hole register, call sites, figures made stale, and goldens; it produces edits plus at most one paragraph in the commit message, never a document or a directory. | §0.4 |
```

### P7

head text (`valoria_master_workplan_v11.md`):

```
| P7 | Mid-step run only the file covering the edit; the full suite runs once per batch close, never to re-confirm a green already held. CI runs twice per batch (at its end, and once to confirm the commit carrying every fix). **Every validator, suite, golden-modes check and four-season exit reading runs once, at the batch close, and no earlier item runs them** (Jordan, 2026-11-02: *"Ensure all validators etc only run at the very end of a batch"*; it restates `methodology-execute`'s RULED CI cadence of 2026-10-13); mid-batch an item is judged by its covering test file or a one- or two-season probe, and every commit before the batch's last carries `[skip ci]`. | §0.5 |
```

### P8

head text (`valoria_master_workplan_v11.md`):

```
| P8 | **Stopping rule.** A falsifier that fails means `git revert` of that position's commits; never `--no-verify`, never skip, xfail or quarantine a test; never widen the position to make the falsifier pass; one hole row only if the gap was measured; one ledger row only if a human decision is needed. | §0.5 |
```

### P9

head text (`valoria_master_workplan_v11.md`):

```
| P9 | **Restoration rule** (RULED 2026-10-13, the session's user: *"Relax exit rules."*; v9 head §0.5, read at `FORK:c1374059`; no ledger row). A verb position is BUILT when it is wired and proven by a falsifier on a hand-built world (the cause controlled, a mutation red). Its executed count in the realm is not required. This relaxes a *position's* exit, not a requirement's `met`: R-04's and R-05's `met` still read computed play (this sentence alone is v9's [ASSUMPTION; medium; Jordan to correct; revert: those `met`s read the hand-built test too, an edit to `requirements.yaml` and `-02` R-04/R-05]). **Three levels, one standard each:** a position's exit is this rule; a batch's close reads its card's Exit, and where that Exit names a computed-probe observable (B10-18c), a built row that leaves it at 0 is a named residue with the refusal that decided it, not a revert (P8) and not an unbuilt row, and the run stops at that close and reports it; a requirement's `met` reads its own `measured:` block (V4) [ASSUMPTION; medium; Jordan to correct; revert: a row whose computed observable stays 0 is reverted under P8 and its batch holds open until it reads above 0]. | §0.5 |
```

### P11

head text (`valoria_master_workplan_v11.md`):

```
| P11 | **Must not**, in any batch: edit `.designs/` or `.audit/`; cite a `.md` as the reason a behaviour is correct; build a guard whose subject is process (`CLAUDE.md` §0.1 pt 5); create a directory or standing document; author a cell, a Godot version, or a Jordan item's answer that no position's home, taken decision (`-05`) or recorded ruling gives (CR-21's and CR-27's cells follow their stated rule; GO-01 records ED-GO-0002's series, it does not choose one); build in `engine/mc_v18.py`; `git add` a file another lane is editing (use `isolation: worktree`); re-fetch from the GitHub API; write a count into `CURRENT.md` or `HANDOFF.md`. | §0.5 |
```

### P12

head text (`valoria_master_workplan_v11.md`):

```
| P12 | The telling workplan's rulings stand: `tell` writes no stance and told valence enters regard at read (G1; AX-3). | §0.6 |
```

### P14

head text (`valoria_master_workplan_v11.md`):

```
| P14 | Every batch's exit names its hash movers with the pre-change `build_realm(0)` reading on its base commit; a mover's pre-change reading is the previous item's recorded after-reading (V1), not a fresh run, and a known-red list is quoted from the previous close, not re-derived. A re-pin states plainly that a golden was re-recorded, and is made in the batch's pin commit (P15). | `_part3` §B |
```

### P15

head text (`valoria_master_workplan_v11.md`):

```
| P15 | **Pins are re-recorded once per batch, after the last item is built** (Jordan, 2026-11-07: when an item's season run ends, the next item's before-reading is already in hand, so a per-item re-pin is overwritten by the next item and nothing reads it). **An item** reports its after-readings (`build_realm(0)` and the 1-season seeds it is judged by) in its commit body (P14), and runs only its own test file and the files that read what it touched. It does NOT re-record a shared seeded golden or digest, a count or set pin (`len(VERB_TABLE)`, the always-refused and executed sets, a corpus or candidate count), or a derived artifact a byte-check compares (`engine/season/runs/results.json`); and it adds no revert switch to an OLDER control merely to keep one pin standing; a WHOLE-BATCH control (one that reverts every mover of the batch to read the batch-open world) lists each mover's switch, and an item's own isolation control (reverting later items to read the item alone) may list theirs, as controls and not as kept pins [ASSUMPTION; medium; Jordan to correct; revert: those controls are re-pinned to the batch-final value in the pin commit and the switches removed]. A pin whose value only that item can move, its own falsifier's numbers and its own new test file, is made in the item. **One commit, the batch's pin commit,** the last before the close, re-records every shared pin the batch moved from the batch-open reading to the batch-final one, with each old to new and a "was" comment in its body, and says plainly that goldens were re-recorded; the close then reads a tree whose pins match. **Every card, build entry or home below that says its item's commit "re-records", "re-pins" or "re-takes" a golden is read as this rule,** as P10 reads every `aperture 4 0` below it; a record of a pin already re-recorded stays history. A verb-cluster item (P13) is still judged mid-batch by its covering file and a one- or two-season probe (P7). | new, 2026-11-07 `[ASSUMPTION; medium; Jordan to correct; revert: delete P15, and each item re-records its own pins as before]` |
```

### P16

head text (`valoria_master_workplan_v11.md`):

```
| P16 | **Build economy** (Jordan, 2026-11-08: *"I am concerned about the excessive build times that comes with running too many pins, tests and seasons."*). **Scope: every batch not yet built except B10-13** (B10-14 to B10-18c with B10-17b, B10-20, B10-19, B10-Z); B10-13 keeps P7, P10, P14 and P15 as written, and no strife batch is reopened. Where P16 and a card, entry, exit or build file below differ, P16 governs, as P10 and P15 govern theirs. **(1) Horizon.** No mid-batch probe, exit or close reads beyond `aperture 2 0`: every `aperture 3 0`, `3 s`, `4 0` or `4 s` a card, entry, exit or build file names as a reading *to take* is read as `aperture 2 0` (a one-season probe stays one season; seeds 1 and 2 only where P14's declared mover calls for them). **Two exceptions only:** a reading that concerns strife explicitly (P10's exception, unchanged), and a reading that tests an arc or a chronicle (CR-88 to CR-91's arc instrument and the readings that test it; the `chronicle` and `storybar` readers' story readings), which takes the horizon its own entry names, as strife's does `[ASSUMPTION; medium; Jordan to correct; revert: arc and chronicle readings are `aperture 2 0` too]`. **(2) Pins carry forward.** A batch takes one fresh base reading, at entry (V1). An item's recorded after-reading is the next item's before-reading wherever the two are related (a shared file, roster, instrument or `needs` edge), a mover or not (P14 said so for movers alone); a fresh reading is taken for an item only where `git diff <sha>..HEAD` reaches what its instrument reads (V1), never to re-confirm. An item records ONE after-reading: `build_realm(0).content_hash()` and the one probe its exit names; an item that is hash-EQUAL by construction records the hash alone. Shared pins are re-recorded in the batch's pin commit (P15), unchanged. **(3) One continuous run.** An invocation that names a batch by its handle is approved by that card (the plan is ratified on merge, ED-1094; it is the `approved:` of `methodology-execute` 0.1 for the card's own order), so 0.1 does not stop to present it. From the first item's BUILD to the completion of BATCH-CLOSE's Phase 3 (the accretion pass between Phases 2 and 3 included) the run does not pause, report and wait, or ask for a cleared window. It halts only on a `STOPPED` condition of that skill (an unmet gate, a held or Jordan row, a BATCH-CLOSE finding that can be neither applied nor rejected by measurement) or an item's own Stop-if and P8 revert `[ASSUMPTION; medium; Jordan to correct; revert: 0.1 presents a named batch for approval as before]`. The stop for a cleared window is P3's, after the expunge and the merge, unchanged. **(4) The full suites run once, as the last act of building**: after the pin commit (P15), before Phase 1 opens, over what `python tools/tests_for_diff.py --base <batch-start-sha>` and the batch's close sequence name. Phases 1 to 3 and the accretion pass run no full suite: the run `methodology-close` places in Phase 2 is this one, not a second. Each fix those phases apply runs only the file covering it, and a red re-runs the failing file only (`CLAUDE.md` §0.4). CI is unchanged (P7). | new, 2026-11-08 |
```

### V1

head text (`valoria_master_workplan_v11.md`):

```
| **V1** | **Re-base at entry.** The first step of every batch re-derives each site by symbol (line numbers drift; line anchors into Layer 0/1 and canon files moved when the applied hunks landed and are re-derived by quoted words), takes the batch's base reading from the last recorded `reading @<sha>` (the previous close's, or the previous item's after-reading, in its commit body) and re-takes it only where `git diff <sha>..HEAD` reaches what the instrument reads, at that reading's own season count (`methodology-execute` "Baselines", RULED 2026-10-13; Jordan, 2026-11-02: validator results are *"referred to by subsequent validation runs ... so we don't duplicate work setting a baseline"*), and compares it with the figure the position's home cites. A premise that moved narrows the position or retires it with a one-line note in the commit; it is not built from stale text. The same step restates the position's N-line in the form `<object> — cut it and the gameplay experience is worse, because <what the game can no longer do>` and names the shipped object each step of that loss would otherwise use; a position whose loss survives the cut (the carrier already ships, or nothing produces it) is cut with a one-line note, not built (`.claude/skills/ners/SKILL.md` §2 and §3; the NERS fold cut eight such positions from the inherited set, `-08`). | new |
```

### V2

head text (`valoria_master_workplan_v11.md`):

```
| **V2** | **A reading is a harness reader, never a guard.** The failure classes in the code report are tracked by readers in `harness/` (REM-10, REM-11, REM-14) whose output is quoted in the batch's commit. No test asserts a refusal count or that a verb executed in the realm (P9 stands). | new |
```

### V3

head text (`valoria_master_workplan_v11.md`):

```
| **V3** | **Asks are answered by the ladder first.** Every `needs_jordan` row in `-05` has been through the five steps. What survives is a short list of questions; the rest are answered, closed, or *taken* with a stated revert. A taken answer is [ASSUMPTION; medium; Jordan to correct] and reverts alone. | `CLAUDE.md` §0 |
```

### V4

head text (`valoria_master_workplan_v11.md`):

```
| **V4** | **The plan states what it cannot do.** No row of THE NINE reads `met` because a position landed; it reads `met` on its own `measured:` block (§3). | new |
```

### -00 §6 risk 2

head text (`valoria_master_workplan_v11.md`):

```
2. **Premises older than HEAD.** The re-base rule (V1) is the mitigation; its cost is a base reading per batch.
```

### -00 §6 risk 4

head text (`valoria_master_workplan_v11.md`):

```
4. **Nothing is a question to Jordan** (`CLAUDE.md` §0: `needs_jordan` is not a parking space; corrected 2026-11-04, ED-IN-0317, from an earlier list that read as owed). What stands instead: (a) **Confirmed defaults in force, re-opening only on his word:** J-T2 (nine attribute keys; the pending slot refuses a value; since ANSWERED by his ten, `ED-IN-0328`, with `-10` M23 and E-1, and built by CR-84 before CR-20, the knowledge-model fold of 2026-11-04; CL-ATTR narrows to M24) and M3 (the field stays persons at weight; a yes after the freeze is a declared re-pin), both CONFIRMED AT THE DEFAULT by his "Confirm all" (ED-IN-0301, `-05` §1a); M22 to M40, each with its default in force (`-05` §1c), resolved by `-10`'s design lanes, not by him. The arc fold of 2026-11-05 (ED-IN-0346) adds three defaults in force, none asked: the arc's target share (`proposals/2026-11-05-unified-design-and-build-plan.md` Part 6 Q1) is Jordan's; until set, CR-90's reading is recorded, never a bar, and no CR-89 flip is kept for hitting a number; the reference reading is breakdown or a casus belli in at least 80% of seeds 0-9 by season 24, the off arm markedly fewer `[ASSUMPTION; medium; Jordan to correct; revert: any share he names; CR-89's flips are re-read against it]`; fighting forms in the ruled contexts, war, crime and duel, with defence (`ED-IN-0337`, `ED-IN-0340`; CR-87) `[ASSUMPTION; medium; Jordan to correct; revert: `violence_contexts` reduced to the duel, ED-IN-0336's "duels only"]`; Valorsmark is the Crown's faction renamed, "Crown" an alias (`ED-IN-0342`; CR-86) `[ASSUMPTION; medium; Jordan to correct; revert: a separate `world.valorsmark` beside `world.crown`, a fifth faction]`. (b) **Taken by the ladder:** `guards` ships ON once CP-T09-07 (b)'s union lands, as its own declared mover in B10-17 (step 4: ED-IN-0310's `foreign` ON and the standing "Gains are improvements and therefore ship"; step 5: until the union lands the flip musters nobody), `[ASSUMPTION; medium; Jordan to correct; revert: guards stays off]` (`-04` part 2 IN-36). (c) **Design files approved by ED-1094's merge default:** CR-38 (Court Parliament's bench), drafted beside B10-13 and approved by merge before B10-18 closes, else on the freeze row with the interim bench. (d) **Content only he authors:** CL-THRUST's B6.n ladders (G-09, G-10, G-24, G-26: the domestic seats' goal rows and the referent-bearing rows of axes B, H, I and J); until they exist that range is unmeasured, not zero. (e) **Deferred by him (ED-IN-0317):** `age_step` and `illness_rate` stay at the control (H-208), so natural death (DR, DN) stays unobserved by design; if he later wants them derived rather than set, period life tables are the source, but he held them off. Answered on 2026-11-04 (ED-IN-0317): the march frequency (a casus-belli rule, held as a design piece, and for testing a cap of one march per season into each territory, built under IN-36 in B10-17); the four-season strife-guard reading (allowed for strife testing, P10's exception). Not his: A3's cross-check of the 102 final moves against the study before the loop reads a terminal set derived from them (CR-75, CR-78); that is work, not a question: the study is the claude.ai artifact `XDjCCRvbxiPS6sumpRtnte` ("Mechanics of Strife to c. 1600", read through the Artifact tool's read action), no copy is in the repository, and the session that runs CR-78's flip owns the cross-check.
```

### -00 §6 risk 6

head text (`valoria_master_workplan_v11.md`):

```
6. **Content is not the plan's to author** (P11). Equipment, tradition, troop types, the cast's attribute values, per-territory weather values, CL-THRUST's ladders, the Tensions cards' content and the strife deck's per-category rows beyond `[ASSUMPTION]` rows are Jordan's; until they exist the emergent range of those systems is unmeasurable, not zero. A strife flow that cannot open or conclude for want of content is reported by the instrument, never patched by widening a kind list (`strife-01` §3 item 3).
```

### CP-T03-06

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T03-06 | The survivor's grudge (its park trigger, ED-IN-0296's polarity, answered by CR-16) | MEASURED at B10-11 (@`eb34324f`, seeds 0-2, `aperture 2 0`, `PYTHONHASHSEED=0`, the run's hash unmoved by the probe): the Wounded-survivor fights are 0, 2 and 2 (all four a `capture` by p_npc_013 at tick 0; `fight` forms 0 Candidates at every seed, as CR-87 reads), so seed 0 is vacuous and the sample is thin; 0 of 4 survivors' regard reached a Candidate after the fight. That is the rule's "zero or fading" side, so CP-T03-06 is NOT cut (no second ladder exists to duplicate) and stays DESIGN-FIRST. Causes seen: no doer attributed to the survivor's wound claim, in 3 of 4 (the wound's `(person, "body", v)` Observation is held by the act's actor only under the shipped `actor` deposit mode, CP-T03-02's stated limit, so repairing it widens a deposit rule, a knowledge-model choice this batch did not take); the one fight-caused regard, p_npc_034's toward p_npc_013, is -0.068 (about 2% of CR-87's -3 bar) and is held toward a man felled at tick 1; eviction was not seen. The design owes which cause it repairs `[GAP: the mechanism behind "no doer" was read, not diagnosed]` · MEASURE first, then DESIGN-FIRST, then BUILD — or CUT (the story-telling fold of 2026-11-02, ED-IN-0311: at seeds 0-2, at the mid-batch horizon (head P7, P10: `aperture 2 0`, two seasons), for each fight a person survived with a Wounded band, read the survivor's `regard` toward his opponent (`queries/person_q.py::regard`, whose `judged` term is IN-58's landed `deeds_judged`), whether it reaches a Candidate under `stance_polarity: declared`, and whether it is still held at its end (a longer persistence reading runs on Jordan's call); non-zero, reaching a Candidate and surviving, a stored `combat_grudge` row is a second ladder for one quantity (NERS S) and CP-T03-06 is CUT with the reading quoted in the commit; zero or fading, the design names which cause it repairs, no doer attributed or eviction, and builds only that) `[ASSUMPTION; medium; Jordan to correct; revert: delete the measure step]` | M (when built) | CR-16 (landed `142e91e22`) | — | `cp-personal-combat`:192-199 |
```

entry (`2026-10-23-subsystem-completion-03-personal-combat.md:192-200`):

````
### CP-T03-06 · The survivor's grudge — PARKED (trigger: ED-IN-0296)

The item: after a fight, each surviving party who took a Wounded band appends `(other party, -1.0, combat_grudge_weight)` to his
stance, `_eff_march`'s row shape (`EC:301-306`), symmetric by role. **Parked**, by one cut test applied as T04 applied it to CP-T04-09:
at the shipped `stance_polarity = "legacy"` (`FX:833`) a grudge **lowers** `fight` on its object (T03 §8 #5), so the item would make
revenge rarer; `declared` rides ED-IN-0296, which is open. Trigger: ED-IN-0296 answered for `declared` (or `regard`); then the item
lands with a control arm that writes no row. The refusal-cost cell L09 paired with it is **dropped**: PC-10b's challenge Record has
no term or expiry (`v9_part7.md:58`), so nothing lapses for a cell to judge, and this file names no lapse owner.

````

### CP-T03-10

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T03-10 | `rescue` — PARKED (trigger: a gate basis for closing another's restraint by force) | HELD · DESIGN (PARKED) | E | — | "Not raised: the N-line does not earn | `cp-personal-combat`:254-258 |
```

entry (`2026-10-23-subsystem-completion-03-personal-combat.md:254-259`):

````
### CP-T03-10 · `rescue` — PARKED (trigger: a gate basis for closing another's restraint by force)

L09 Suite C's `rescue` closes a live `detain` by defeating its keeper. A `detain` is owned by the prisoner and closable only under
`determination` (`ROS:126-129`; F3's clauses, `state/gate.py:109-117`); a third party closing it by force has no basis, and adding one
is a Layer 1 amendment (04 §C.2). The N-line is narrow (§3), so it is parked with that trigger, not raised as an ask.

````

### CR-83

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-83 | Familiarity sets inference: how much a holder can infer of another's pursuits, convictions, ambitions, goals, obligations and demands (`ED-IN-0324`; design-first: one design file under `proposals/` naming what he may read of the other, its cost, and its falsifier; no carrier coined before it); since the knowledge-model fold of 2026-11-04 also the context (`ED-IN-0325`), Attunement and Reason (`ED-IN-0326`, `ED-IN-0327`; Reason read at `attr.mind.acuity`), opinion persistence as a measurement first, the subject-fit term, `said_of`'s weighing (G3), the event-identity gap (recorded, not fixed) and CR-19's flip; one open item, whether `write_matrix.yaml` is Layer-1-bound | DESIGN-FIRST (drafted beside B10-13, as CR-38 is; approved by ED-1094's merge default; its build waits on the design and is scheduled by it) | E (the design; its build M) | CR-31 (landed `f1319502`; its consumer `teller_weight`'s relation term), CR-17 (believed odds; landed `1ef8d273`) | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:106-117`):

````
### CR-83 — Familiarity sets inference and adjudication: what a holder can infer of another person and of the context (SC, IN) · BATCH B10-13 (drafted beside it, as CR-38 is) · STATE DESIGN-FIRST (with the claim-model items CR-82 hands on) · R R-07
- WHAT: `ED-IN-0324` (Jordan, 2026-11-04): *"the more you know someone, the more you can intuit/understand their pursuits and convictions and ambitions and goals and obligations and demands"*. Today `person_q.py::known_persons` says whether a holder knows a person (a set), `regard` scores a referent's deeds by the holder's own pursuits and his stance rows, and no reader gives a graded estimate of another person's pursuits, convictions, ambitions, goals, obligations or demands; familiarity is not a degree. Write ONE design file under `proposals/` that says what a holder may read of another person and how the reading grows with what he holds of him (his `seen` and told claims, his own tenures with the other, shared faction membership, CR-81's acquaintance claims), by composing on what exists and coining no carrier; names its consumers (`teller_weight`'s relation term through CR-31, CR-27's `lie`, CR-17's believed odds, the tellings); its cost; and its falsifier (a seeded run in which a holder who knows another better infers more of the other's pursuits, and equal at no acquaintance). The five rulings on the claim model (`ED-IN-0319` to `ED-IN-0323`, CR-82) are its inputs: familiarity feeds on the same ledger CR-82 keeps. SECOND HALF (`ED-IN-0325`, Jordan, same day): *"and the more you know about strife flows and faction thrust and regimes and offices and other contextual elements, the more you can adjudicate"*: the same design file says what a holder may read of the CONTEXT (a strife flow, a thrust axis, a regime, an office) from what he already holds, how that grades his adjudication of a claim, a matter or a person's conduct (ED-IN-0323's fit factor, generalised), and which strife and thrust readers are its consumers (CR-75 to CR-79, CL-THRUST's readers); no carrier coined, and no change to those positions' own gates. THIRD HALF (`ED-IN-0326`, Jordan, same day): *"further your attunement will help you judge accurately the pursuits and convictions and everything, and your reasoning will help you judge accurately offices and regime and obligations etc"*: the design also says how the holder's Attunement (`attr.social.attunement`) sharpens the person inference and his judgment of whether a teller is telling the truth (`ED-IN-0327`: CR-19 and CR-27 are consumers) and how his Reasoning sharpens the context adjudication; Reason is now an attribute: CR-84 (B10-10, landed `1abaa612`) names the key `attr.mind.acuity` Reason and keeps the key (until that fold Reasoning was only an alias of Acuity), so the design takes Reason, read at `attr.mind.acuity` [ASSUMPTION; medium; Jordan to correct; revert: another attribute], and reads CR-20 (B10-10, landed `c7764a5a`) for the attribute carrier.
- ABSORBED FROM CR-82 (the knowledge-model fold of 2026-11-04; `proposals/2026-11-04-knowledge-model-build-plan.md` §2, §2.2 and §11 item 3, reference). The same design file also states, each with its falsifier: (1) **opinion persistence, as a measurement first** (`ED-IN-0320`): the deed claims evicted before N seasons at CR-82's shipped cap. If zero, the ruling is met and nothing is built. If non-zero, a design decision with a matrix change (`write_matrix.yaml` row steps), a single owner for the judgment (not `stance` and `regard` both), and a control that every reader of `stance_toward` (`legitimacy`, `_bond`, `teller_weight`, `choose`, forgive, `reception`) is unchanged. (2) **The subject-fit term** (`ED-IN-0323`: fit with what the holder holds of the claim's subject person) in `queries/person_q.py`, passed to `queries/` as a closure so `decision/` is never imported (`world_q.py:2672`), and `regard`'s recursion constraint (`deeds_judged` stays unweighted, `person_q.py:102-104`). (3) **`said_of`'s weighing** (G3; `ED-IN-0321`): today only `belief_contradicts` passes a `weigh` and the chained told arm is dormant (H-237). (4) **The event-identity gap, recorded and not fixed**: a "similar claim" is the exact `(subject, predicate, value)` triple, so news of a second killing by the same person from an origin already behind a copy is dropped; no field is coined. (5) **CR-19's flip** (`ED-IN-0327`): CR-19 ships its factor at gain 0; this design gives the separator between a lie and a truth that a live gain needs, and schedules the flip as a declared mover (CR-27's exit carries the falsifier the flip must pass). (6) **The old CR-82 commit 4's build half**: a reader of staleness only where the design already names one (`belief_contradicts`' floor, H-40), else the gap recorded. `ED-IN-0324` to `ED-IN-0327` are its inputs as above.
- OPEN ITEM, the one: **is `write_matrix.yaml` Layer-1-bound?** If (1)'s measurement is non-zero, an opinion mechanism needs a matrix row to gain a step; whether that edit is an agent's or Jordan's is unread in the tree. It blocks nothing until that measurement reads non-zero; the design states the question and does not answer it. FOURTH HALF (`ED-IN-0334`, Jordan, 2026-11-05): *"in addition to knowing people directly, you can know OF people due to their reputation and standing (eg everyone will know of king Almud even if they don't know him personally) as per combination of rung, allegiance and overlapping activities"*: the same design file says what a holder may know OF a person from the person's rung, allegiance and overlapping activities, as a graded reading computed when read (no claim per prominent person: that would repeat CR-81's eviction fade at ledger scale, and `known_persons` is a set with no degree); it reads the existing World halves (`world_q.opinion_of`, `reception`, rung and office relations) and coins no carrier. [ASSUMPTION; medium; Jordan to correct; revert: delete the design file] FIFTH HALF (the arc fold of 2026-11-05, ED-IN-0346): `person_q.believed_clock` and the person twin of `sittings_failed` (CR-89, B10-17b) are consumers of the retained claims and the know-OF grade, and CR-88's design (duty and the betrayal reading) is drafted beside this one and reads it; CR-81's acquaintance claims heading every question list (the interaction audit, H3) is a reading this design states, not a revert of CR-81. SIXTH HALF (ED-IN-0347, Jordan, 2026-11-05, AR-24 to AR-26a): *"perception will impact how much any given character will know about something … but it concerns FACTUAL matters"*: the design also says how the holder's Perception (`attr.mind.perception`) grades what he comes to know of worldly facts, at WITNESS (the World may read the true value; `observers_for`, `loop/witness.py`'s seat deposit of a larder's `shortfall:<kind>`), on the deposit's confidence and not as a gate `[ASSUMPTION; medium; Jordan to correct; revert: a gate]`; and it states which attribute grades CR-19's competence for which kind of told claim (persons: Attunement; offices, regimes, obligations: Reason; facts: Perception) before CR-19's flip.
- GATE: B10-13's entry; the design is drafted beside B10-13 (as CR-38 is) and reads CR-82 (landed `1ef8d273`), CR-17's believed odds (landed `1ef8d273`), CR-20's attribute carrier and CR-84's roster (B10-10, landed `c7764a5a` and `1abaa612`). NEEDS (v11's cell stands): CR-31 (landed `f1319502`), CR-17 (landed `1ef8d273`). It did not precede CR-27 (landed `db1dc1f2`), which built as written and needed nothing from this design. Approval by ED-1094's merge default unless the design PR lists it as held back.
- EXIT and FALSIFIER: the design file exists and states the three things above (what a holder may read, its cost, its falsifier), items (1) to (6) each with a falsifier, and the open item as a question; no code.
- HASH MOVERS: none at this step; each build it schedules (the opinion mechanism if (1) is non-zero, the fit term, CR-19's flip) is a declared mover, scheduled by the design.
- HOLES AND LEDGER IDS: `ED-IN-0320` to `ED-IN-0327`; H-40, H-237.
- ASKS ATTACHED: none open; Jordan's answers are `ED-IN-0324`, `ED-IN-0325`, `ED-IN-0326` and `ED-IN-0327`. The open item above is stated, not written as a `needs_jordan` row. [ASSUMPTION; medium; Jordan to correct; revert: delete the design file]
- BUILDER: opus; `valoria-author`.
- SOURCE: `ED-IN-0324`; `proposals/2026-11-04-knowledge-model-build-plan.md` §2.2 (reference).

````

### CP-T06-09

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T06-09 | The room files a covered deed under the hand | EDIT | M | — | no. | `cp-fieldwork-and-information`:155-161 |
```

entry (`2026-10-23-subsystem-completion-06-fieldwork-and-information.md:155-162`):

````
### CP-T06-09 · The room files a covered deed under the hand

- **What it adds.** At both WITNESS deposit sites (the fan, `loop/witness.py:630-633`; the found deposit, `:301-303`), an alias anchor (a cover's id, or CP-T06-07's borrowed name) is swapped for the actor in the event-kind claims' subjects **when the deposit shows `who`**: for a channel, when `rosters.yaml: observation_terms.supplied_by` lists `who` for it (`co_located`, `witness_key`); for a finding, when its band's `finding_terms` do. One helper in `epistemic.py` beside `non_anchor_subjects`, called from both sites; `claim_subjects` stays the single owner of what a deposit is about and is passed the anchor to use. `anchor_of`, its indexes and the knot channel's admission do not change.
- **Why.** Today a bystander of a covered act holds `seen.who = actor` and the deed claims about the alias (T06 §3, cover probe), so his proofs and deed judgements land on nobody, because `attributed_deeds` reads an unpaired deed by its subject (`queries/person_q.py:150-158`). Under CP-T06-07 they would land on the innocent. With this item a cover hides a man from those who hear of his deed and never from those who saw it, which is the plan's acceptance line for the cover (K-19, "`seen.who` still names the actor", quoted at `state/attribution.py:116-121`) carried into the deposit.
- **Owner.** The helper; the data it reads is the two rosters named. Asymmetry: no getter changes; two of the writers of `Person.ledger` change what they write. Every writer outside tests and harness is in `loop/witness.py` (`:655, :765, :788, :817, :968, :988`, by grep at HEAD); the event-kind sites the swap touches are `:655` (fan) and the found deposit's yield into it, and the observation, `seen`, told and content sites (`:765-988`) take no event-kind subject from the anchor and are left alone.
- **Falsifier.** T06 §3's cover probe re-run: the bystander holds `(p_other, record.forged, True)`, not `(rec:cv, record.forged, True)`; a `document_key` learner still holds the alias claim. Mutation: drop the swap, and the probe's old result returns.
- **Control.** The same world with no cover: deposits identical to HEAD (the swap is the identity when the anchor is the actor). **Hash.** Mover wherever a live cover has a witness in the room (19 / 34 / 28 covers assumed in two seasons at seeds 0-2). **Revert.** The helper. **Size** S.

````

### CR-29

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-29 | REACH: the event-kind reach channel, then `chronicle`'s paired deletion (a `reach` roster row keyed on event kind, its predicate in `epistemic.py`, `mints: told_by`, shipped with an empty map; then the kinds it carries and the deletion of `_ch_chronicle`, keeping realm reach for `tenure.closed` and `person.died`) | BUILD (released from M11; its §C.6 row is Layer 1 and lands with it, listed under 'Layer 0/1 hunks'; a new row in ratified 04 §C.6 at an anchor with no (RULED) mark `[ASSUMPTION; medium; Jordan to correct; revert: ED-IN-0300 reopened]`) | M (commit 1 EQUAL, an empty map; commit 2 a declared mover) | IN-18 (its told channel and step 2a, landed at B10-02; the held tail in B10-Z is not a dependency), REM-04 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:118-130`):

````
### CR-29 — REACH: the event-kind reach channel, then `chronicle`'s paired deletion (IN/FA) · BATCH B10-14 (after CP-T06-09, before CP-T06-01) · STATE BUILD (released from M11) · R R-07 (conjunct 1 re-read), R-04 (the grand-strategy row's input)
- WHAT: news of an event reaches persons by the event's kind, at a stated reach, instead of through `chronicle`'s special channel; then `chronicle` is deleted. FA-01's clause and the coercive kinds H-234 names need it. It adds a row to ratified Layer 1 §C.6, which M11 answered (a) allows for an unmarked anchor: the superseding row of ED-IN-0300 (2026-10-26, ratified) confirms D-1 and reads M11's second half as yes `[ASSUMPTION; medium; Jordan to correct; revert: ED-IN-0300 reopened]`. The row lands in this position's PR, listed under "Layer 0/1 hunks"; a (RULED) mark at the anchor still stops that row.
- LANDED ALREADY: the witness-channel roster and `CHANNEL_PREDICATES`; IN-18's told channel; `_ch_chronicle`.
- REMAINING UNBUILT: (1) a `reach` roster row keyed on event kind in `rosters.yaml`'s witness-channel roster (looked up through `CHANNEL_PREDICATES`), its predicate in `engine/season/epistemic.py`, `mints: told_by`, shipped with an empty kind→reach map; the §C.6 row (Layer 1) lands only in the same PR as the channel's code and first reader. (2) the kinds the channel carries (the `binding_decision` kinds `chronicle` admits today, `person.died`, the coercive kinds H-234 names) and the deletion of `_ch_chronicle` with its roster row. The kind-to-reach table keeps realm reach for `tenure.closed` and `person.died`, or names who loses that news.
- GATE: B10-14, after CP-T06-09 and before CP-T06-01; M11 answered (a): the superseding row of ED-IN-0300 (2026-10-26, ratified). The §C.6 anchor is checked for a (RULED) mark before the row is listed. NEEDS: IN-18, REM-04.
- EXIT and FALSIFIER: the same event at reach `room` and at reach `realm` deposits into different ledger counts; NPC-090's `person_q.stability` at a settlement rung reads non-zero in at least one of seeds 0-2 of `build_realm(S, foreign=True)` over four seasons (0 at HEAD, H-234). CONTROLS: commit (1) reproduces `build_realm(0)`'s base hash; with commit (2)'s map emptied `told_by` falls to 0 (H-214: 879 → 0 at one season); CR-26 and IN-61's exit stay green; a throne released by its holder still reaches the heir; R-07 conjunct (1) is re-read in commit (2).
- HASH MOVERS: commit (1) EQUAL (empty map; its control); commit (2) declared MOVER (every seeded pin re-recorded old to new). It is on GO-15's freeze list (a WITNESS change slice 1 pins).
- HOLES AND LEDGER IDS: H-214 (`hole_register.yaml:4604-4616`), H-234; ED-IN-0298 (`registers/editorial_ledger_in.jsonl:76`; stays open, `needs_jordan`, no superseding row).
- ASKS ATTACHED: M11 ANSWERED (a) (`-05`; ED-IN-0300): D-1 stands, and a new row in ratified 04 §C.6 is read as yes for an unmarked anchor. Revert: commit (2) reverts as a declared re-pin; commit (1) stays inert.
- RE-BASE: re-read `_ch_chronicle`, `CHANNEL_PREDICATES` and the witness roster by symbol at B10-14's open.
- BUILDER: second tier; a third-tier (judgment) critic on the reach-per-kind table.
- SOURCE: `-05` M11; `proposals/2026-09-05-proceedings-subsystem/19_PLAN.md:499-509`; FA-01's entry (part 2).

````

### CP-T06-01

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T06-01 | A deed that writes a place or an alias leaves a trail | BUILD · CR-71 (reading @5d6aac5, `aperture 2 0` and `strife 2 0`, seed 0, `PYTHONHASHSEED=0`, REALM): `sabotage` attempted 23, all refused on `exists:Site=0` (a subject that is no Site); this row gives `sabotage` its `referent_class: Site` (CR-47's WHAT) | M | CP-T06-09, REM-21, REM-22, REM-2C | — | `cp-fieldwork-and-information`:72-83 |
```

entry (`2026-10-23-subsystem-completion-06-fieldwork-and-information.md:72-84`):

````
### CP-T06-01 · A deed that writes a place or an alias leaves a trail

- **What it adds.** `rosters.yaml: covert_kinds` `["record.forged"]` → `["record.forged", "site.damaged", "cover.assumed"]`, with the membership rule written into the roster's note so the next member is decided by it, not by taste: a deed kind is covert when (i) no `binding_decision` row emits it, so `chronicle` never broadcasts it (`epistemic.py:652-654, 685-686`); (ii) its row has no `remit:` eligibility, so it is not done through a seat and `post_remit` never reports it; (iii) it writes a thing some graded inquiry takes as its subject (a Site for `examine`, a Record for `research`). `sabotage` (`site.damaged`; `own`; `uncontested_material`) and `conceal` (`cover.assumed`; `own`; `social`) pass, as `forge` does. `record.destroyed` fails (iii): a destroyed Record cannot be researched. The note's stale line "`conceal` … unbuilt" is corrected in the same edit.
- **Owner.** `rosters.yaml: covert_kinds`, loaded by `data/verbs.py` (`COVERT_KINDS`; `_check_covert_kinds` refuses a non-deed member). All three are in `DEED_KINDS` (checked at HEAD by import: `data/verbs.py:1406`). One reader: `epistemic.trail_of`.
- **Reads / writes.** Reads the log through `World.last_emission_of(kind, subject, written=True)`. Writes nothing new: found deposits go through `loop/witness.py::_found_claims` unchanged.
- **Depends on.** REM-22 (`examine` forms on a Site; 0/0 at seed 0 today); REM-2C (a `research` on the cover's id forms only if the question names it). ⚠ **REM-22 classes only `restore`, `work` and `examine`** (remediation part 02, REM-22), and no T08 item takes `sabotage` (T08 part 2's interface table names none), yet `sabotage` takes the same `site` operand filled the same wrong way (34/0 at seed 0, T06 §4). So this item carries one more step of REM-22's own shape: **`sabotage` gains `referent_class: Site`** and its `referent_class_note` in the house form, read by REM-21's `Site` stamper; nothing else. Without it the `site.damaged` half has no route into the realm. Its falsifier is REM-22's pair: a question about a person and a Site forms `sabotage` on the Site only, and a hand-built saboteur present at a Site executes through the real fold. [UNVERIFIED] whether `sabotage` has refusal causes beyond the fill.
- **Joins.** Settlements/economy (T08) owns `sabotage`'s effect; needed from it only that `sabotage` keeps emitting `site.damaged` with the Site as the written subject (§5).
- **Decision handed to the chooser.** The saboteur chooses to act where nobody stands (only then is the trail his whole risk) and whether to take a cover first. The investigator chooses to go to the Site and spend a scene on it. Under a cover, a distant learner holds the deed about the alias's id; `research` on that id finds `cover.assumed` written to it and, at Success, its maker. Unwatched: NPCs sabotage, conceal, examine and research by the same agenda.
- **Falsifier.** (1) `test_fi03_trail.py::trail_world` plus a Site at R: p_other sabotages it with nobody at R; p_high moves to R and `examine`s it. At an act id that rolls Success he holds `(p_other, site.damaged, True)` and `seen(site){who: p_other}`, `inferred`, at 50; at Partial, `(site, site.damaged, True)` and `who: None`. (2) p_other conceals; p_high is told of `rec:cv` and `research`es it; at Success he holds `seen(rec:cv){who: p_other}`. Mutation for both: the shipped roster, and both deposit nothing.
- **Control.** Paired seeds 0-2, two seasons, the ctl recipe, both arms after REM-22/REM-2C: found deposits per seed (claims caused by both a `finding.made` and a covert Event). Zero in both arms means the realm still never reaches a trail; that is the finding, not a pass.
- **Hash.** Mover wherever a trail is found. Declared re-record: `test_fi03_trail.py::test_the_realm_seed_twice_in_one_process_gives_one_hash_and_reaches_no_find` (`:768`), whose "reaches no find" is what this item exists to break.
- **Revert.** One roster line. **Size** S.

````

### CP-T06-03

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T06-03 | A Partial closes the deed, not the hand (the retry is next season) | BUILD (the home's `holds_trail` hand test, as filed, T06:96-103; it also accepts the actor's event-kind claim, for CP-T06-09) | E at the base realm; M wherever a retry forms (declared) | CP-T06-01 | no. | `cp-fieldwork-and-information`:96-103 |
```

entry (`2026-10-23-subsystem-completion-06-fieldwork-and-information.md:96-104`):

````
### CP-T06-03 · A Partial closes the deed, not the hand

- **What it adds.** `epistemic.holds_trail` answers True only when the person holds the **hand**: its present test (an event-kind claim on a subject specific to the Event, made no earlier than it) **and** either the anchor's event-kind claim made no earlier than the Event, or a `seen` claim on a specific subject whose `who` is set. `_found_claims`' re-check then deposits only the triples the finder lacks, by the exact-triple guard the told deposit already uses (`loop/witness.py:932-935`), not by a second guard. The `finding_terms` note's sentence "also closes it to a later, better finding" is rewritten.
- **Owner.** `epistemic.holds_trail`, one test for both readers (`trail_of`, `_found_claims`). A reader only: no field, no writer moves.
- **Decision handed to the chooser.** A finder who learned *that* a sheet was forged may spend another scene to learn *by whom*; each try is witnessed by those present, so the forger's warning grows with the investigator's persistence. This is the staged reasoning Obra Dinn teaches (D_T06 #5) and the reverse of L.A. Noire's lockout (#31).
- **Falsifier.** `test_fi03_trail.py::test_a_partial_find_closes_the_same_trail_to_a_later_better_one` (`:342`) is inverted: Partial, then Success, on one Record deposits `(p_other, record.forged, True)` and `seen{who: p_other}` and does not re-deposit `(rec, record.forged, True)`. `test_a_second_research_of_the_same_record_deposits_nothing` (`:301`, Success then Success) stays green. Mutation: the old body; the inverted test reds.
- **Edge, declared.** A claim on the anchor from the same actor's *later* Event of the same kind closes this one too; the `when` guard cannot separate them. `test_a_found_forger_s_other_forging_is_still_trail` (`:368`) is the instrument that sees it, and is re-run.
- **Control.** The fixed arm: the same hand-built sequence on the shipped body. **Hash.** The realm does not move until some trail is found (0 found deposits, seeds 0-2); the named tests re-record. **Revert.** The body. **Size** S.

````

### CP-T06-04

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T06-04 | A refused or failed inquiry teaches its actor his reads; only its event-kind claim is skipped | EDIT | M | CP-T06-03, REM-11, REM-29 | — | `cp-fieldwork-and-information`:105-114 |
```

entry (`2026-10-23-subsystem-completion-06-fieldwork-and-information.md:105-115`):

````
### CP-T06-04 · A refused or failed inquiry teaches its actor his reads; only its event-kind claim is skipped

- **What it adds.** The arm the owner's own note names: *"skip only the `finding.none` event-kind claim"* (`rosters.yaml:1163-1168`). Today `loop/witness.py:365` drops every Event of an undeposited kind before the fan (*"fans to nobody -- no event-kind claim, no read"*, `:360`). After: the event-kind claim of an undeposited kind is skipped, and the Event's other deposits go as for any Event: the actor's own observation reads at `observation_deposit_mode: actor` and the `seen` claims of those present. No verb row, no new kind: `finding.none` stays the refusal and the Failure kind of the six rows and stays in `undeposited_kinds`, whose meaning narrows from "fans to nobody" to "no event-kind claim".
- **What it buys.** A refused inquiry leaves its actor the read that refused it (not present at the Site; no such Record), which the known-false veto learns from (REM-29's channel), so he stops re-forming it. A rolled Failure leaves reads that all held, so he can tell "impossible" from "failed" by what he holds (O5). Those present learn he tried, in both cases, which is the counter-information the inquiry already pays on success.
- **Owner.** The skip at `loop/witness.py:360-365` and `rosters.yaml: undeposited_kinds`' note (L2). The roster and its loader are unchanged.
- **Touches, plainly.** H-111's default (RS-21 item 1, "[medium; Jordan to correct]": a refused inquiry deposits nothing) is revised to its own named alternative. **Remediation DEC-12 is reversed**: it declined so that "the right-kind re-forming stays by that ruling's design" (remediation part 01:329); this item ends that re-forming. Not raised as an ask: (1) not superseded; (2) relevant (O5, D_T06 #6); (3) the owner's note calls the strict skip "THE THING TO CORRECT" and names this arm, with the measured cost (refused `research` 3 → 12 headless, `rosters.yaml:1163-1167`); (4) every other row's refusal leaves its actor his reads; (5) one deposit rule for every refusal. **REM-40** (every row declares its refusal kinds; part 03, REM-40) does not collide: it changes which kind a refusal emits, and the six inquiry rows already declare `finding.none`; this item lands after REM-40 so the skip keys on declared kinds only.
- **Decision handed to the chooser.** He stops spending scenes on an inquiry his own ledger now says is impossible; a player can tell "nothing could be learned here" from "I failed to learn it".
- **Falsifier.** A hand-built `examine` by a person not present at the Site: his ledger holds the refusing `present_at` read and no `finding.none` claim, and his next deliberation forms no `examine` on that Site while he is absent; a bystander holds `seen{who: examiner}`. A rolled Failure deposits no event-kind claim (`test_fi01_graded_inquiries.py:97`'s "deposits no claim" is re-recorded to "no `finding.none` claim"; `news.untold` unchanged). Mutation: the whole-Event skip; the refusal leaves nothing and the act re-forms.
- **Control.** Paired seeds 0-2: inquiry formations and refusals per verb, by REM-11's per-kind line. Base at seed 0: 250 `finding.none`, 218 of them refusals (T06 §8).
- **Hash.** Mover, declared. **Revert.** The skip. **Size** S.

````

### CP-T06-02

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T06-02 | `surveil` finds the covert deeds done at the place it watches (the latest per kind and place only) | BUILD | M | CP-T06-01, CP-T06-04 | no. | `cp-fieldwork-and-information`:85-94 |
```

entry (`2026-10-23-subsystem-completion-06-fieldwork-and-information.md:85-95`):

````
### CP-T06-02 · `surveil` finds the covert deeds done at the place it watches

- **What it adds.** A third side to `trail_of`: for each covert kind, the most recent Event of that kind that **happened at** `subject` (a Rung), beside the sides that wrote it and that it did; the same filters (a person did it, not the watcher, not already held). `trail_of`'s own docstring keeps its walk "so such an inquiry needs no second projection" (`epistemic.py:386-388`); this is that walk widened, not a second sifter.
- **Where the place comes from.** `world_q.event_place` places an act-caused Event by its actor's *current* place (`queries/world_q.py:694-704`), so it cannot be asked later. The tree's precedent for a time-varying per-Event fact is to read it **once, at logging**: `World._on_logged` keeps the cover an actor held when his Event was logged (`_covers_logged`, "read ONCE, here", `state/world.py:1295-1313`). The place is kept the same way: in `_on_logged`, for an Event of a covert kind whose actor is a person (`attribution.actor_of`; `trail_of` keeps no other), `(kind, place) → event id` is written to an index of `_last_by_anchor`'s shape, the place read through `state/containment.home_of`, the owner of `event_place`'s person limb (`place_of`'s "person -> `home_of(w)[x]`", `queries/world_q.py`), since `state/` may not import `queries/`. Read through `World.last_emission_of(kind, subject, at=True)`; most recent wins, the existing bound. `event_place`'s other limbs (a death's place, a placeless anchor) are not needed, because a covert Event is always act-caused.
- **Owner.** `epistemic.trail_of`; the index on `World`, one writer (`World._on_logged`, inside the log callback like its two sibling indexes). Asymmetry: a new field with exactly one writer and one reader; no existing getter changes what it computes for the two existing sides.
- **Joins.** None beyond CP-T06-01's kinds; it earns its place only with them (a forging at a hall, a cover taken at an inn, a Site sabotaged in a holding).
- **Decision handed to the chooser.** A householder or seat-holder chooses to spend a scene watching his own place. At Success he learns the hand of a covert deed done there while he was away; at Partial, only that one was done. Anyone present, the doer included, sees him watching (`seen{who: watcher}`, T06 §3's counter-information). Unwatched: a master who re-asks about his hall each deliberation (§5, the purview question) is CK2's standing spymaster without a container clock.
- **Falsifier.** `trail_world`: p_other forges at R at tick 0 while p_high is at S; at tick 1 p_high moves to R and `surveil`s it. Success deposits `(p_other, record.forged, True)` and `seen{who: p_other}`; a forging at another Rung is not found from R. Mutation: drop the `at` side; nothing is found.
- **Control.** As CP-T06-01, plus `surveil`'s attempted/ok and found deposits per seed (base 30/5 at seed 0, 0 found).
- **Hash.** Mover wherever a watch finds anything. [UNVERIFIED] whether `World.content_hash()` covers the index; it covers whatever it covers of `_last_by_anchor`, which has the same shape and writer. **Revert.** The side and the index. **Size** M.

````

### CP-T06-07

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T06-07 | A cover can borrow another man's name (hand-built Acts only until a formation interface exists; the victim may learn at once) | BUILD | M | CP-T06-02, CP-T06-09 | no. | `cp-fieldwork-and-information`:135-144 |
```

entry (`2026-10-23-subsystem-completion-06-fieldwork-and-information.md:135-145`):

````
### CP-T06-07 · A cover can borrow another man's name

- **What it adds.** A mode of `conceal`, by the lexicon's own fold test (S8: one actor; one cover Record and one anchor reader; differs in a content key). The cover kind gains an optional content key naming the person whose name it borrows (`rosters.yaml: record_kinds`, beside `COVER_KEY`). `state/attribution.py::_cover_for` answers that person's id for an Event logged under such a cover, else the cover's id as now. Everything reading the anchor follows unedited: deposit subjects (`claim_subjects`), the knot channel, `_last_by_anchor`, `trail_of`'s deeds-by side. `actor_of`, `causing_act` and `seen.who` still name the real hand: the performance is untouched, only its reading moves (AX-7's sanctity, `01_AXIOMS.md:268-273`).
- **What it does in play.** A learner whose channel withholds `who` (`document_key`, `chronicle`, `post_remit`) holds `(framed, kind, True)`. That is the framed man's deed in `attributed_deeds`, so a proof against him in `speak` and `determine`, and a mark in every such learner's deed judgement of him. Those present are not fooled (CP-T06-09). The framed man is admitted by `witness_key` (the anchor himself, terms `stratum, who`), so he learns of the deed and, after CP-T06-09, files it under the true hand: he knows he is framed and by whom, and must persuade others by his own `tell`.
- **Formation.** A player sets the key through the Act interface: `_eff_conceal` already reads its payload (`loop/effects_information.py:270-271`). The chooser forms the borrowed-name cover only on persons the actor holds a negative stance row against (`queries/person_q.py::held_against`, the reader `own_stance_declines` already uses), so the fan is bounded by grudges, not by acquaintance: a decision-lane interface (§5).
- **Owner.** `state/attribution.py::_cover_for` (the alias's one reader) and the cover kind's keys. Asymmetry: `_cover_for` is a getter over `World._covers_logged`, whose one writer (`World._on_logged` via `cover_at_logging`) is unchanged; every reader of the anchor is listed above.
- **Joins.** SC: nothing to build (proofs read the deed). GV: a warrant naming the framed man needs `issue` to form on a held deed, then `arrest` (§5). That is the wrongful-arrest path, the only one that needs no liar.
- **Decision handed to the chooser.** The framer chooses whom to frame and when (the cover lapses in about three seasons, and the room always sees him). The framed man chooses whether to accuse the framer. A magistrate chooses whether to act on hearsay proofs (weight 0.5) or found ones (0.25). Unwatched: grudges become frames, frames become charges, and a watch at the place (CP-T06-02) clears a name.
- **Falsifier.** Hand-built: framer F takes a borrowed-name cover naming V, then does an act at R, where only C stands, whose kind reaches a distant learner (a `chronicle` kind, or a Record a `document_key` holder holds). The learner holds `(V, kind, True)` and nothing naming F; C holds `seen{who: F}` and, with CP-T06-09, `(F, kind, True)`; V holds `(F, kind, True)` through `witness_key`. Mutation: drop the content key, and the learner holds `(rec:cv, kind, True)`.
- **Control.** The same world with a plain cover. **Hash.** Mover wherever a borrowed-name cover forms. **Revert.** The key and one branch in `_cover_for`. **Size** M.

````

### CP-T06-05

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T06-05 | The person questioned answers by his own act (limits: no event for not answering; absent-hearer refusals unlearnable; the answer is a contest) | EDIT (verb retype) | M | CP-T06-07 | no. | `cp-fieldwork-and-information`:116-124 |
```

entry (`2026-10-23-subsystem-completion-06-fieldwork-and-information.md:116-125`):

````
### CP-T06-05 · The person questioned answers by his own act

- **What it adds.** `interview` retyped on `tell`'s cell shape (the `tell` row, `verb_table.yaml:1255`): `subject` is the **topic**, with `own_ledger` of `subject` (the asker holds a claim on it, the F8 carve-out for his own ledger); `to` is **the person questioned**, `existence` Person and `relation with` (conjunct `hearer`), `counterparty: to` (which also closes self-interview, lexicon FI-G20), fanned over the persons the asker knows as `tell`'s hearer is (`known_person_operands`). Still ungraded; still emits `finding.made`. Because the questioned person is with the asker, WITNESS gives him the question (`seen{who: asker}`, and the event-kind claims on the act's referents; [UNVERIFIED] that `act_refs`, which `holds_trail` and the fan both pass to `claim_subjects`, carries `subject` and `to` for this row). His answer is his own `tell(topic, to=asker)` at a later deliberation, the next round of the same season at the earliest, or no answer.
- **Why this shape.** It is the lexicon's J1 option (b) (`verbs-12:904-917`), taken at step 5, not asked: option (a) widens F8 (`04 §B.2`, the fold reads no ledger but the actor's) and AX-2; (b) keeps both, and makes refusal to answer the questioned man's own choice. A lie is SC's J-C-6.
- **Owner.** `verb_table.yaml: interview` (L2 data). No code, unless the loader requires the `to` operand declared beyond the cell.
- **Joins.** Decision lane: the question the landed `finding.made` raises in the person questioned must carry the topic as a referent (the hearer fan already exists). SC: `tell` is contested over "a standing", so an answer can itself fail (`news.untold`).
- **Decision handed to the chooser.** The asker chooses whom to ask about what, knowing the asking is news to the one asked (a suspect learns he is suspected). The one asked chooses whether to answer. Unwatched: NPCs question each other and answer or stonewall by their own agenda.
- **Falsifier.** Hand-built: A and B at R, B holding a claim on X; A interviews B about X in round 1, so B holds the question. Across 40 act-id draws of B's later deliberations that season, B forms `tell(X, to=A)` at a share above zero. Control arm: the shipped row (subject = B) in the same world. Equal shares mean the item does nothing, and it is reverted.
- **Control.** As the falsifier, plus realm `interview` and `tell` attempted/ok at seeds 0-2. **Hash.** Mover. **Revert.** The row's cell. **Size** M.

````

### CR-13

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-13 | The Leap is not charged for failing (C-TW-3), and `DEPTH_TS_MINIMUM` gets its reader (C-TW-10/11, if they ask for it) | BUILD | E | — | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:71-83`):

````
### CR-13 — The Leap is not charged for failing; the depth gate gets its reader (WR/PC) · BATCH B10-15 · STATE BUILD (hash EQUAL) · R —
- WHAT: ED-WR-0005's open clauses. (a) C-TW-3: `systems/threadwork/sim/operations.py::_resolve_operation` charges every Partial or Failure one extra Coherence unless the operation is Mending (`if degree in ("Partial", "Failure") and operation != "Mending"`, ED-871's exemption). `attempt_leap` passes `coherence_delta=0` and its own docstring says a failed Leap costs no Coherence (§3.2), so the blanket mis-hits it. Exempt `Leap` the way Mending is exempt; the exit covers Partial as well as Failure. `collective.py:116` also calls `attempt_leap`, so the collective path's per-participant Leap stress changes with it; no test pins a Leap Partial or Failure stress source, so nothing re-records. (b) C-TW-10 and C-TW-11: `DEPTH_TS_MINIMUM` (`operations.py:95`, 30, 30, 50, 50, 70, 90 by depth) has no reader; `attempt_leap` gates on TS 30, and `attempt_weaving`, `attempt_pulling` and `attempt_locking` apply no TS-by-depth gate. The audit that coined C-TW-10 and C-TW-11 is dissolved: the builder first reads ED-WR-0005's rows (`registers/editorial_ledger_wr_archive.jsonl`) and `.designs/`; if they ask for exactly this gate, give the table its reader on `attempt_leap`'s model (an ineligible attempt returns Failure, `coherence_delta=0` and a note); if they do not, stop and leave (b) **[UNVERIFIED: what C-TW-10 and C-TW-11 ask]**. Update the comments the change makes stale, in the same commit: `operations.py:261-262` and `:319-320`, `engine/tests/test_thread_mending_ed871.py:14-15`, `tests/valoria/test_threadwork_mending_parity.py:317-318`, `tests/valoria/test_threadwork_resilience.py:110`.
- NOT THIS ITEM'S: C-TW-4 (the past-pulling cap) is parked with past-pulling (`subsystem-completion-07` §3, M9); C-TW-8 (co-movement) is unplugged per IN-06; C-TW-6 (Thread Fatigue) has no carrier and waits for CP-T07-02; the anchoring cadence cap was never ruled and stays a design call (`-07` §2).
- LANDED ALREADY: ED-871's Mending exemption and its pinned test (`engine/tests/test_thread_mending_ed871.py`).
- REMAINING UNBUILT: (a) and (b).
- GATE: first in B10-15, before REM-45 (which needed it: same file; REM-45 is dropped by the knowledge-model fold of 2026-11-04, `-07` §2) and CP-T07-02, so the host reads a corrected oracle. The season loop does not reach this code (`engine/season/loop/matter.py:135`: "threadwork module stays unplugged"); nothing under `engine/` imports it but that one test.
- EXIT and FALSIFIER: a pinned test beside `test_thread_mending_ed871.py`: a Leap that rolls Partial and one that rolls Failure each net 0 Coherence. Control: a Weaving at the same degrees keeps the blanket penalty. Hash EQUAL: `build_realm(0)` hashes equal to the base commit. No test pins the Leap's current charge (grep of `tests/` and `engine/tests/`), so none re-records.
- HASH MOVERS: none (season-unreachable until CP-T07-02).
- HOLES AND LEDGER IDS: ED-WR-0005.
- ASKS ATTACHED: none. CP-T07-02's home text (`subsystem-completion-07` lines 120-121, 138-139 and 463: "the Leap's charge stands") is overridden by `-08` HR-6.
- RE-BASE: re-read `_resolve_operation` and `attempt_leap` by symbol.
- SOURCE: the editorial-id pass, lane 3 and critic ED3.

````

### CP-T07-02

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-02 | The Leap stage, the one working host, the actor adapter and the `Person.coherence` carrier; stored `spirit` reads `attr.mind.will` (named Spirit since CR-84) through a registered `faculty` addend, active only where the carrier holds a value (M2). RE-BASE (the knowledge-model fold of 2026-11-04; REM-45 dropped): the actor adapter reads `_actor_pool`'s `min(3, history + 3)` as the code has it (HR-7's override revived without its "waits on M18" clause, `-08` part 2 HR-7), and the term's fate is CR-85's | BUILD | M | CR-13, CR-20 (landed `c7764a5a`); B-S, IN-06; not a dependency: CR-85 (the history term's fate, a design) | no. | `cp-threadwork`:117-142 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:117-143`):

````
### CP-T07-02 · The Leap stage and the one working host · size M

- **Adds.** `engine/season/seam/wrappers/threadwork.py` [proposed]: the one host every thread row dispatches through. Order, fixed:
  (1) materialise elapsed recovery (CP-T07-06); (2) roll `attempt_leap`; on Failure the act ends, `working.failed`, and the Leap's
  charge stands (the oracle's own −1, C-TW-3, is carried, not fixed here); Partial proceeds, the reading `collective.py:116-118`
  already makes; (3) roll the operation (`attempt_weaving` / `_locking` / `_mending`, or the read of CP-T07-10); (4) sum the charges
  into one seam Event `coherence.changed` carrying both quantities before and after (the matrix's declared kind, `write_matrix.yaml:191`);
  (5) return the degree as the act's `Resolution`, so each row's effect (CP-T07-03, -04) reads `res.degree`. **Scale is read off the
  target, not chosen**: a roster `thread_scales` maps the target's class (Person → Personal; Tenure → Relational; Site by kind, a
  lattice Site → Structural) `[ASSUMPTION — basis: `DEPTH_OB` is "how deep in the substrate the target sits", T07 §1]`. The choice
  left to the person is which target.
- **Owner.** The host; one prize row in `rosters.yaml: contest_subsystems.prizes` (as I expect it: `"a configuration"` → module
  `threadwork`, `module_entry: threadwork.work`), on `determine`'s precedent of a single-actor roll through `contest`
  (`verb_table.yaml:383-384`). IN-06 left B-S to choose between this and a second `_ROLE_ROSTERS` row
  (`manifest/registry.py:38-39`); every item here is indifferent to which.
- **Primitives.** P23 (the draw), P39 (cost on the practitioner), P24 (the gate).
- **Reads/writes.** Writes `(Person, coherence)` (RES, Seam). Reads the actor adapter, `thread_scales`.
- **Joins.** IN-06: *need* each oracle entry to return its cost rather than write a store (the store-shed); *need* the composition rows.
  T01 resolution core: the degree is `dice_engine`'s single ladder (`test_degree_ladder_single_owner.py`); no second ladder.
- **Chooser / unwatched.** Every thread row is now one act of the scene economy (7 acts at budget 5, T07 §0): a working displaces a
  `tell` or a `move`.
- **Falsifier.** A planted practitioner's `weave` at seed s writes exactly one `coherence.changed` whose deltas equal the oracle's
  `OperationResult.coherence_delta` plus the Leap's for the same dice; a Leap Failure writes the Leap's charge and no target change.
  Mutation: skip step 2, and the Leap-Failure test reds. **Control.** `ts_seed: none`.
- **Hash movers.** Every executed thread row, by outcome. **Revert.** Delete the thread rows and the prize row in one commit (deleting
  the prize row alone refuses at boot, IN-06's deletion refusal, which is a breakage and not a revert).

````

### CP-T07-03

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-03 | `weave` and `lock` on Sites: two held shapes that write different things (no strain row; strain waits on H-236's source) | BUILD | M | CP-T07-02, REM-21, REM-22 | no. | `cp-threadwork`:144-189 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:144-190`):

````
### CP-T07-03 · `weave` and `lock` on Sites: two held shapes that write different things · size L

- **Adds.** Two verb rows (verbs-13 names; R-10 keeps `dissolve` apart), one Tenure kind `weave` in `rosters.yaml: tenure_kinds`,
  and one Site field `locked` with its write-matrix row `(Site, locked)`, RES, ACTS, `social: false` (as `(Site, condition)` is,
  `write_matrix.yaml:373-379`). The lock is **not** a Tenure, deliberately: a Tenure owned by the locker would close when he dies
  (the cascade on `(Person, exists)`) and could be closed by nobody else (the gate admits a Tenure write only by its owner, a term,
  a seat's revocation or a cascade, `engine/season/state/gate.py:109-117`), so it could neither outlive him nor be mended
  (cross-file ruling R8):

  | | `weave` (Things Cohere) | `lock` (Unable to Become) |
  |---|---|---|
  | on Success+ | opens Tenure `weave` (weaver → Site) | sets `Site.locked` |
  | wear (`loop/matter.py:659-673`) | skipped while live | skipped while live |
  | staged condition deltas (`loop/resolve.py:1113-1132`: `restore`, `work`, `sabotage`) | admitted | refused, every sign (`<verb>.refused`) |
  | yield (`loop/matter.py:591`) | as today | 0 `[ASSUMPTION — basis: a Locked Zone is "a place where becoming has been precluded", `canon/philosophy/09_terminology.md:117`]` |
  | the worker's headroom | its cost stays in his elastic while the Tenure is live (held load; `recover` cannot empty it) `[ASSUMPTION — basis: "It stands only while it is held, and the holding is the practitioner's", `06_operations.md:195-197` as quoted in verbs-13 §3.3 B]` | not held: the lock persists by itself ("Persists indefinitely", `09_terminology.md:117`) |
  | ends by | the weaver's `release`; his death (the Tenure-closing cascade on `(Person, exists)`). Nobody else ends it (gate F3) | `mend` by any practitioner present, which clears the field (CP-T07-04); neither the locker's choice nor his death |
  | strain for IN-35 | +1 per live Tenure in the Site's territory | +1 per locked Site |

  So `weave` is upkeep a weaver carries (a held load that occupies headroom, P20's shape paid in headroom rather than stock), and `lock`
  is a one-time price that outlives the locker and denies everyone the place, its owner included.
- **Owner.** `verb_table.yaml` rows; `rosters.yaml: tenure_kinds`; `state/carriers.py` (`Site.locked`) and its write-matrix row; the
  wear reader in `loop/matter.py`; the refusal in the staged accumulator `loop/resolve.py`; one Query `held_load(w, person)` and one
  `strain(w, territory)` in `queries/world_q.py`. `release`'s `domain:` (`verb_table.yaml:1034`) gains `weave`, as its loader
  invariant requires (verbs-13 §3.3 C).
- **Primitives.** P20 (a standing charge, here on headroom), P07-like lockout (a locked place cannot change), P38 via IN-35 (the world's
  threat sized by what practitioners hold).
- **Reads/writes.** Writes Tenure `weave` (open; the weaver's own edge) and `(Site, locked)` at RES; reads both in MATTER (wear,
  yield) and RESOLVE (accumulator).
  **Asymmetry check (§0.1 pt 1):** this changes what the condition getter's writers achieve. Writers of `Site.condition` at HEAD:
  the wear write `loop/matter.py:672-673`, the staged accumulator `loop/resolve.py:1132` (fed by `effects_economy.py:105`, `:176`,
  `:210`), and the harness `harness/probes.py:1717` (a probe, outside the season). The item routes the first two through the lock and
  weave readers; the probe is named in the test so a new bare writer reds.
- **Joins.** IN-35: *need* a strain input on its coupling rule (`strain(territory)`, weight at IN-35's control 0). REM-21 (RB-2a, Site
  referents): *need* questions to carry Site referents so `weave`/`lock` can form on a Site (T02 `:633-635`). T08 settlements: *give*
  locked and woven Sites; their yield and repair rules change where a shape is live.
- **Chooser / unwatched.** A weaver chooses what to preserve and how much headroom to tie up; a locker chooses to deny a place for
  good. Unwatched: an NPC practitioner's weave holds his town's mill against wear and raises his territory's strain; when he dies the
  weave falls and wear resumes.
- **Falsifier.** Paired seeds, one planted Site woven and its twin not: after one MATTER the woven Site's condition is unchanged and
  the twin's falls by `wear_per_season`. A locked Site refuses a planted `restore` and a planted `sabotage` and yields 0. A weaver
  with one live Relational weave rests a season in equilibrium and ends with elastic ≥ 1. Each fails if otherwise.
  **Control.** `ts_seed: none`; IN-35 weight 0 for strain.
- **Hash movers.** `Site.locked` is a SCHEMA mover (a new carrier field moves the hash by schema alone, H-208), declared; then wear
  and yield on shaped Sites, refusals on locked Sites, strain at IN-35 weight > 0. **Revert.** Delete the two rows, the kind, the field
  and its matrix row together; the readers have nothing to read.

````

### CP-T07-05

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-05 | Equilibrium decided by place (the locked-Site gate only) | BUILD | E | CP-T07-03 | no. | `cp-threadwork`:230-243 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:230-244`):

````
### CP-T07-05 · Equilibrium decided by place · size S

- **Adds.** One Query `in_equilibrium(w, person)`: True unless the Site the person is contained at is `locked`, or its
  territory's Calamity band, read through `calamity_band(w, territory)`, is below `equilibrium_band_floor` (a fixture).
  `calamity_band` is the name this file expects for IN-35's "effect per territory as a Query over band floors" (`_part5.md:91-92`);
  IN-35 owns it, and T10 depends on the same Query (T10's demand, not this file's). The host
  passes it as the oracle's `environment_in_equilibrium` for recovery (CP-T07-06) and Mending feedback (CP-T07-04).
- **Owner.** `queries/world_q.py`; the fixture in `Fixtures`. **Control:** `equilibrium: everywhere` (always True), a fixed arm.
- **Primitives.** P40 (recovery gated by place: Darkest Dungeon II's Inn, Pathologic 2's beds; D_T07 #23).
- **Reads.** `contain` Tenure, `Site.locked`, `calamity_band`. Writes nothing.
- **Joins.** IN-35: *need* its effect-per-territory Query (named in IN-35's *Builds*, `_part5.md:91-92`). T10 travel: *give* a reason to
  `move` (a stretched practitioner travels to a stable place to recover, paying a leg).
- **Falsifier.** A planted practitioner contained at a locked Site recovers 0 over a season; moved to an unlocked Site he recovers 6.
  At `equilibrium: everywhere` both recover 6. **Hash movers.** Recovery amounts where a place fails. **Revert.** The fixed arm.

````

### CP-T07-09

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-09 | Every thread row is a witnessable, celled deed (affiliation cells; pursuit cells wait on JQ-3, so NPCs tie among the four rows until then) | EDIT (data cells) | M | CP-T07-05; IN-08; not a dependency: JQ-3 (a stated limit: NPCs tie among the four rows until pursuit cells are authored) | no. | `cp-threadwork`:303-322 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:303-323`):

````
### CP-T07-09 · Every thread row is a witnessable, celled deed · size S

- **Adds.** On `weave`, `lock`, `mend`, `ward`: affiliation cells on the three columns `thread_read` already has
  (`solmund_orthodoxy` −1, `inner_tradition` +1, `thread_truth` +1; `rosters.yaml:2793-2797`); on `mend` also the cell the roster's
  revert clause holds for "a thread-operation verb", `einhir_restoration` + (`rosters.yaml:2765-2770`), landing with that clause's
  `solmund_orthodoxy` − `[UNVERIFIED: at HEAD `einhir_restoration` appears as a pole at `rosters.yaml:2712-2724`, not as a `cells:`
  column, so carrying it may add the column]`; and pursuit-axis cells or an
  `uncelled:` reason per IN-08's loader rule (`_check_alignment_density`, `_part5.md:43`). Conspicuousness is the observer set
  WITNESS already computes (ED-FI-0009's retraction; T07 §0): no Exposure meter. Because every row now moves state at RESOLVE
  (`coherence.changed`, a Tenure, or `Site.locked`), the scar can fire (`rosters.yaml:2776-2778`). A Personal-scale `thread_read`
  whose Leap takes costs 0 and writes nothing (`COHERENCE_COST_BY_SCALE`, `operations.py:128-136`), so a quiet reading is no deed to a
  witness; a Relational one is, and so is a fumbled Leap (−1).
- **Owner.** `rosters.yaml` cells (data). **Primitives.** P13 (a breach count, here scars on witnesses), P33 (a conviction folds at scar
  ≥ 3, `person_q.py:579-580` per D_T10 #25).
- **Joins.** T02 / IN-08: the cell values ride the CELL-VALUE AND COSINE PASS (remediation JQ-3's annex); this item adds rows to it,
  not values of its own beyond the three signs already authored.
- **Chooser / unwatched.** Working in front of the orthodox is a choice with a social price; the unwatched world scars orthodox
  witnesses of an NPC weaver and may fold a conviction.
- **Falsifier.** A planted orthodox witness co-located with an executed `weave` gains a scar on `solmund_orthodoxy`; with the witness
  absent, none. **Control.** `ts_seed: none`. **Hash movers.** Scars and pursuit scores for thread rows. **Revert.** Remove the cells.

````

### CP-T07-04

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-04 | `mend`: a locked Site, another person (in-season), oneself; and a price on self-repair (no lattice route: `restore` is IN-35's arm) | BUILD | M | CP-T07-03, CP-T07-05, CP-T07-09 | — | `cp-threadwork`:191-228 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:191-229`):

````
### CP-T07-04 · `mend`'s targets beyond IN-35's lattice, and a price on self-repair · size M

- **Adds.** The `mend` row (R-26: `mend` is Mending; `restore` stays fabric) routes by target, each route on an existing owner:

  | target | on Success+ (Partial for another's configuration, as the oracle pays, `operations.py:494-509`) | owner it composes on |
  |---|---|---|
  | a lattice Site | IN-35's raise | IN-35 (`_rise`, `effects_economy.py:109`) |
  | a locked Site | clears `Site.locked` (a Site field, not anyone's edge, so no gate basis is needed) | `(Site, locked)` at RES, as `restore` writes `condition` |
  | another person | the **target's** elastic falls by the restorative term, if the target stands in equilibrium | the oracle's `recover(..., mending=term)` (`coherence.py:341-377`; E-1 "mending accelerates") |
  | oneself | resting point −1 (refused past the crossing) | `mend_resting_point` (`coherence.py:380-408`) |

  The mender's own elastic feedback stays as the oracle computes it (1-2, in equilibrium). **Price on self-repair:** each cast is one
  act (it now competes with the person's other ~6 acts), and the self-aim Ob gains a swept step `self_mend_ob_step ∈ (0, 2, 4)`,
  shipped at 0, passed by the host as one keyword on `attempt_mending` — the place the oracle's own `[GAP]` note puts the difficulty
  (`operations.py:159-167`; C-1 "extremely difficult to do but possible"). Today's arm is 0.
  **Not a target:** another person's live Tenure (his `weave`, his `ward`). The gate admits a Tenure write only by its owner, a
  maturing term, a seat's revocation or a cascade (`engine/season/state/gate.py:109-117`, 04 §C.2), and no basis lets a third party
  close another's edge; verbs-13's "undo another's weave" fold is therefore not built (cross-file ruling R8, the reshape preferred over
  a Layer 1 amendment). A weave ends by its weaver's `release` or death only.
- **Owner.** The `mend` row and its effect; the fixture in `Fixtures`; one keyword on the oracle entry (the only oracle edit in this
  file, a parameter, not a rule).
- **Primitives.** P40 (recovery bought by an act, gated by place through CP-T07-05), TM01's recovery leg.
- **Reads/writes.** `(Person, coherence)` for mender and target (both through the seam, one Event each); `(Site, locked)`; lattice
  Site via IN-35.
- **Joins.** IN-35: *need* its Mending arm to be `mend`. This is an **edit to IN-35's text** (`workplans/valoria_master_workplan_v9_part5.md:91`
  reads "Mending as persons' acts (the `restore` arm)"), proposed on verbs-13 §3.3 D's fold test, held back with the rest of this file.
  The roster clause at `rosters.yaml:2765-2770` is a separate matter: it withholds two affiliation cells from `restore` until "a
  thread-operation verb … exists", and CP-T07-09 lands both on `mend`. T10 NPC life: `tend` stays bodies; thread healing of a body is
  not built here.
- **Chooser / unwatched.** A mender chooses between holding back the Calamity, freeing a locked place, easing another practitioner
  (a social bond the healer earns), or walking back his own set. Unwatched: menders work the lattice; a stretched NPC practitioner can
  be eased by a knotted friend.
- **Falsifier.** At `self_mend_ob_step` 4, a planted practitioner at resting 2 does not reach resting 0 within one season in more than a
  stated share of 100 seeds where at step 0 he does (the share is the measurement; it must differ between arms or the knob is dead).
  `mend` on a locked Site clears `Site.locked`; `mend` on another person lowers that person's elastic and leaves his resting point; a
  `mend` naming another's live `weave` cannot form. **Control.**
  Step 0 = today's oracle; `ts_seed: none`.
- **Hash movers.** Every executed `mend`. **Revert.** Step to 0; delete the non-lattice routes.

````

### CP-T07-06

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-06 | Recovery as a projection, written at the next seam write (K-WR-8 answered) | BUILD | M | CP-T07-03, CP-T07-04, CP-T07-05; IN-06 | no. | `cp-threadwork`:245-261 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:245-262`):

````
### CP-T07-06 · Recovery as a projection, written at the next seam write (K-WR-8 answered) · size S

- **Adds.** IN-06's `[ASSUMPTION]`, specified: no step writes coherence. The **read** (`threadwork.coherence_band` and the host) projects
  elastic return as the oracle's `recover(seasons=Δ, environment_in_equilibrium=…)` where Δ = seasons since the person's last
  `coherence.changed` (`w.last_emission_of`, the reader `matter.py:670` already uses), floored at CP-T07-03's `held_load`; the **write**
  materialises the projection inside the next seam Event, before that act's stress. Equilibrium is read at materialisation
  (one read for the interval; stated, not hidden).
- **Why this is not an ask.** verbs-13 §3.9 item 1 asked "a licensed clock or a rest a person chooses". Step 3 answers the game: E-1
  is ruled ("time is the mechanism, environmental equilibrium is the condition, mending accelerates", `coherence.py:39-40`). Step 5
  answers the mechanism: a read-time projection writes nothing on its own, so it is not a fourth clock (`write_matrix.yaml:190`), and
  no rest verb is needed (verbs-13's `anchor` cull stands).
- **Owner.** The host and the query. **Primitives.** P03 (a value that reaches the world with elapsed time), P40.
- **Asymmetry check.** This changes what the coherence getter computes. Assignments to `(Person, coherence)`: the gate admits only
  `driver="Seam"` (`state/world.py:1014-1021`), so the only writer is CP-T07-02's host; the test greps for a second assignment.
- **Falsifier.** A practitioner at elastic 4 who takes no thread act for one season reads band Stable at the next deliberation and
  writes elastic 0 at his next working, in equilibrium; out of equilibrium he reads Fragmented. **Control.** `ts_seed: none`.
- **Hash movers.** Every later working's charge arithmetic. **Revert.** Projection off (Δ = 0): today's oracle-only behaviour.

````

### CP-T07-07

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-07 | Permanent set narrows the season (a `coherence_band_floors` Fixtures tuple, shipped `()`, counted by `bands_below`) | BUILD | E | CP-T07-02, CP-T07-06 | no. | `cp-threadwork`:263-284 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:263-285`):

````
### CP-T07-07 · Permanent set narrows the season · size M

- **Adds.** The scene budget subtracts a coherence penalty beside the body's: `budget()` already does `b -= body_band_penalty(p, fx)`
  (`decision/budget.py:57-60`). The penalty reads the **resting point's band**, carried on `Person` and written by the seam in the
  same `coherence.changed` write that moves the resting point (the oracle's band owner, `coherence._displacement_band`,
  `:154-162`, computes it; nothing else writes it). Why the resting band and not the present one: `budget(p, k, fx)` is person-side
  and admits `fx` only because it is "identical for every person … not world state" (`decision/budget.py:49-55`); a present band
  projected from `w.last_emission_of` and a place-based equilibrium would be a World read handed in. The resting point changes only at a
  seam write (recovery never assigns it, `coherence.py:28-30`), so the carried band is never stale and no World is read. A per-band
  table `coherence_band_penalty` (Stable, Dissonant, Fragmented, crossed), swept `(0,0,0,0)` / `(0,0,1,2)` / `(0,1,1,2)`, shipped at
  all-zeros. No band edges are copied into a second table (the rule `body_band_penalty`'s docstring states, `budget.py:72-76`).
- **Owner.** `decision/budget.py` (one term); `Fixtures`; the band carried in IN-06's `(Person, coherence)` value (a third member
  of the structured field, beside the two quantities IN-06 keeps apart).
- **Primitives.** P01 (bands that apply modifiers), P05 (the per-season budget), P32 (a lasting mark that changes the person's numbers).
- **Joins.** IN-06: *need* the structured coherence field to carry the resting band written at the seam. T08: CP-T08-10 edits the
  same lines (`budget.py:57-58`); the two items are **serialised** on that file (whichever lands second rebases and re-runs the
  other's falsifier).
- **Chooser / unwatched.** Stretch is felt as headroom and in CP-T07-06's band reading; set is felt every season: a practitioner who
  takes permanent set has fewer acts until he mends it back. Unwatched NPCs who overwork shrink their own seasons for good.
- **Falsifier.** At `(0,1,1,2)` a planted practitioner at resting 2 (Dissonant) has a budget one less than his resting-0 twin at the
  same holdings, and his elastic stretch changes neither; at all-zeros they are equal. **Control.** All-zeros = today. **Hash movers.**
  Budgets of practitioners with set at a non-zero arm. **Revert.** All-zeros.

````

### CP-T07-10

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-10 | What `thread_read` finds | BUILD | M | CP-T07-02, CP-T07-03, CP-T07-07 | no. | `cp-threadwork`:324-344 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:324-345`):

````
### CP-T07-10 · What `thread_read` finds · size M

- **Adds.** Two finding contents a non-sensitive cannot mint: on a Site, which shapes it carries (live `weave` and `ward` Tenures,
  `Site.locked`, and `calamity_band` where IN-35 has one); on a person (verbs-13's `diagnose` fold), his band and whether his TS is
  ≥ 30. **Why today's route cannot carry it:** `inquiry_modules` is keyed by the emitted kind, `finding.made` already maps to
  `fieldwork.find`, and an ungraded `finding.made` (`thread_read` is one) "reaches the row and finds nothing" because `finding_terms`
  keys on the degree (`rosters.yaml:2486-2500`); `trail_of` returns covert deed Events, not live shapes or bands. **So:** the row's
  roll is its Leap stage in CP-T07-02's host (canon's stand-alone perceptive Leap, verbs-13 §3.3.0), which grades it; on Partial or
  better the row emits a **new kind `thread.read`** carrying that degree; on Failure it emits `finding.none`, which no row claims, so
  nothing is found (the existing rule, no band branch). A row `inquiry_modules.findings."thread.read"` →
  `{module: threadwork, provider: threadwork, module_entry: threadwork.read}` mints the Claim at WITNESS.
- **Owner.** The **single owner of what a shape is** is `threadwork.read` (the module entry), which reads `weave`/`ward` Tenures and
  `Site.locked` through Queries and the person's carried band; `thread_read`'s `emits:` changes from `finding.made` to `thread.read`.
- **Primitives.** P26 (the ledger), P24 (TS gate).
- **Joins.** T06 fieldwork (FI-G01): T06 replied "none required … finds through `trail_of`"; that answer covers `finding.made`, which
  this row stops emitting. *Need* T06 to accept, in its file, the `thread.read` row under the `inquiry` role (R-13: TW owns the gate
  and cost, FI the finding shape) and the graded-event shape its provider reads `[UNVERIFIED: the field a graded inquiry's Event
  carries its degree in]`.
- **Chooser / unwatched.** A sensitive hunts hidden practitioners (an orthodox inquisitor with TS has a reason to exist) or scouts a
  place before working it. **Falsifier.** A planted practitioner reads a woven Site and holds a Claim naming the weave; a reader at TS
  25 cannot form the act. **Control.** `ts_seed: none`. **Hash movers.** `thread_read`'s Claims. **Revert.** Drop the kind.

````

### CP-T07-08

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-08 | The crossing as a witnessed breach (the Event alone: no outcome slot, no knot arm) | BUILD | M | CP-T07-02, CP-T07-10 | no. | `cp-threadwork`:286-301 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:286-302`):

````
### CP-T07-08 · The crossing as a witnessed breach, with an outcome slot · size M

- **Adds.** When a seam write carries a resting point past `HUMAN_BAND_LIMIT` for the first time, the host emits one Event
  `coherence.crossed` (subject: the person), fanned at WITNESS like any Event, so those present hold a Claim about it. A roster
  `crossing_outcomes` keyed by TS band (P-15's "TS-gated branching", `coherence.py:67-70`) names the consequence, shipped as `none`
  for every band (today). A knot arm (P-12, drift propagates along knots): each live `knot` partner of the crossed person takes one
  stress event of `crossing_knot_stress` (control 0) through the seam. The crossed person keeps acting; no game over (D_T07 #7, ruled).
- **Owner.** The host (the Event), `rosters.yaml: crossing_outcomes`, the fixture. The outcome **content** is Jordan ask A1 (§6).
- **Primitives.** P02 (breach event with an outcome fork, odds from the holder's own state), P27 (others learn of it), P11 via knots.
- **Reads/writes.** Event; `(Person, coherence)` of knot partners (seam); IN-32's `knot` Tenure as reader.
- **Joins.** IN-32: *need* a directed, readable `knot` Tenure. T09 factions / T05 social: *give* a witnessed Claim the orthodox can act
  on (charge, `arrest`).
- **Falsifier.** A planted practitioner driven 0 → crossing by three Structural lock Failures (T07 §2.3) emits `coherence.crossed`
  exactly once, and a co-located witness holds the Claim after WITNESS; a fourth working emits none. At `crossing_knot_stress` 1 his
  knot partner's elastic rises by 1; at 0 it does not. **Control.** Outcomes `none`, knot stress 0.
- **Hash movers.** The Event and its Claims (new kinds), wherever a crossing occurs. **Revert.** Delete the emission.

````

### CP-T07-11

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T07-11 | `ward`: protection that routes a working into a contest | BUILD | M | CP-T07-03, CP-T07-08 | no. | `cp-threadwork`:346-356 |
```

entry (`2026-10-23-subsystem-completion-07-threadwork.md:346-357`):

````
### CP-T07-11 · `ward`: protection that routes a working into a contest · size M

- **Adds.** The `ward` row: Tenure `ward` (warder → Site or person) with a one-season `Term` (the field `oblige` uses). Any working on a
  warded target by someone other than the warder resolves through `opposing.resolve_opposing_operations(actor, warder, …)`
  (`opposing.py:102`) instead of the solo entry, and both sides pay through the seam. No "hostile" classifier: the ward routes every
  other person's working. `release`'s domain gains `ward`.
- **Owner.** The row, the kind, a branch in CP-T07-02's host. **Primitives.** P23 opposed, P14-like term (`Term`, lapses unless renewed).
- **Joins.** Builds with CP-T07-03 (its first reader: a `lock` on another's Site), verbs-13 §3.3 E's build condition.
- **Chooser / unwatched.** Pay now against a working that may never come; an unwatched ward that fires on a rival's lock is a story
  nobody scripted. **Falsifier.** A planted `lock` on a warded Site rolls the opposed resolver (both sides charged); on an unwarded
  twin it rolls solo. **Control.** No ward. **Hash movers.** Workings on warded targets. **Revert.** Delete the row and kind.

````

### WR-01

card row (`valoria_master_workplan_v11_part3.md`):

```
| WR-01 | `27` remainder: the R-14 practitioner-resilience term, the `engine/season/` reach | BLK (narrowed): a working with a cost running in the season (its M2 slot answered: the attribute at `attr.mind.will`, which CR-84 names Spirit, Will being Spirit's alias) | E | IN-32 | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:723-735`):

````
### WR-01 — `27` remainder: the R-14 practitioner-resilience term, the `engine/season/` reach (WR) · BATCH B10-15 (last, after IN-32) · STATE BLK (narrowed): a working with a cost running in the season (its own condition; the M2 slot question is answered) · R —
- DECISION ROUND: M2 answers what fills the slot (`-05`): Will (Spirit is Will's alias), read as CP-T07-02's `spirit` reads it, through a registered `faculty` addend active only where the carrier (CR-20) holds a value. WR-01 stays BLK on its own condition. NEEDS: IN-32 (same batch, earlier; order).
- WHAT: Give the R-14 practitioner-resilience term its season reach: the in-module half (`RESILIENCE_GAIN`, `resist_coherence_cost`) is built, but nothing in `engine/season/` supplies `actor.resilience` or a gain. It waits on a working with a cost running in the season.
- LANDED ALREADY: in-module half `0a690b30` (B-D3); WR-01..03 landed in-module; `27` BUILT 2026-10-01 (PR #451); IN-06 re-review `759eefb8` and IN-35 `23b33e9e` (B-S).
- REMAINING UNBUILT: [v9 WHAT, full text: B-D3 built the in-module half: `operations.RESILIENCE_GAIN` (shipped at control 0; `RESILIENCE_GAIN_SWEEP = (0, 1, 3)`) and `operations.resist_coherence_cost`, applied to every practitioner's working cost via `operations.charge_working` in `operations.py`, `collective.py`, `opposing.py`. Remaining: the reach — nothing in `engine/season/` supplies `actor.resilience` or a gain. The two unruled things (the slot's name and what fills it; where the gain lives) were answered by IN-06's re-review (§6 item 11) [ASSUMPTION; medium; Jordan to correct]; "what fills the slot waits on J-9 / K-2".] the season reach, once a working with a cost runs in the season. B-S built nothing for it ("a `Fixtures` gain would have no reader, ID-13").
- GATE: DEPS IN-06 (satisfied `759eefb8`); a working with a cost running in the season (D) (`proposals/2026-10-07-unplugged-systems-replug.md` §6 item 11). EDITS `engine/season/` once that working runs.
- EXIT and FALSIFIER: EXIT "observed when a working with a cost runs in the season (unobservable at B-S, nothing plugs): a plugged row's deletion refuses in a fresh subprocess and one seed twice in one process gives one hash; plus `python -m pytest tests/valoria/test_threadwork_resilience.py -q`, 0 failed." FALSIFIER "at gain 0 the plugged practitioner's costs equal the unplugged ones; at gain > 0 a practitioner with resilience takes strictly less than one without, on one planted pair, in a season run."
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: H-94 (cited), ID-13, R-14, WR-SCOPE, `27`; WR-05 = IN-06 + IN-35 (both landed B-S).
- ASKS ATTACHED: J-9 / K-2 — what fills the resilience slot (J-9 is the Godot-version item, now ED-GO-0002; K-2 is `Person.attributes`, built by CR-20): answered by M2, Will (above; M2 NARROWED, its reverts are `-05`'s).
- RE-BASE: B-S (#500) re-reviewed IN-06 and landed IN-35; the v9 entry records "B-S built nothing for it". None found since.
- SOURCE: `v9_p7:77-82` (carried v8 block `:69-75`); state-index row `v9.md:288`.

````

### CR-40

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-40 | One grain for Prosperity: delete the 17 `starting_pros` lines from `valoria_geography_v30.yaml` and write the header note that a Prosperity value lives at settlement grain only (a territory figure is a query over its settlements); the pin and the identifier census re-derived by the repo's tooling | EDIT (data; retire a field) | E | —; not a dependency: DEF-9 (the deletion is correct whether the frozen table survives or not) | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:279-291`):

````
### CR-40 — One grain for Prosperity: delete `starting_pros` (SE) · BATCH B10-16 (first: CR-40 → CP-T08-01 → …) · STATE EDIT (data; retire a field) · R —
- WHAT: item 6 (reconcile the sources), Prosperity taken at step 5 with step 4: a Prosperity value lives only in a settlement's `stats` triplet. The provinces' `starting_pros` disagrees with the frozen territory table (`engine/engine_params/params_tables.yaml:6576`) in 11 of 17 territories (Jordan's "eleven Prosperity values"), nothing reads it, and a value over many settlements cannot be a field (T-a). It runs first in B10-16 (an EQUAL data edit on a file no B10-16 member edits), so the batch's movers read their controls on the post-deletion tree.
- LANDED ALREADY: each settlement's `stats` triplet [Prosperity, Defense, Order].
- REMAINING UNBUILT: `systems/settlements/valoria_geography_v30.yaml`: delete the 17 `starting_pros: <n>` lines (one per province) and insert, after line 6, the header note: "PROSPERITY IS A SETTLEMENT FACT ONLY. Each settlement's `stats` triplet [Prosperity, Defense, Order] is the one place a Prosperity value lives. Provinces carried a `starting_pros` until <commit>; it disagreed with the frozen territory table in `engine_params/params_tables.yaml` in 11 of 17 territories and with this file's own settlement sums in <n>, nothing read it, and a value over many settlements cannot be a field (T-a). A territory figure is a query over its settlements, written the day a reader needs one." (`<n>` is re-computed at the build and written as computed; the decision gave 13, not re-opened.) No clause about T1 exceeding a declared scale is written (the 0-5 scale is `set.prosperity`'s, a settlement stat, `descriptor_registry.yaml:89`). Re-derived by the repo's tooling: `references/canonical_sources.yaml:90` by `python3 tools/freshness_gate.py --update` (run `python3 tools/freshness_gate.py` first; the diff shows exactly that one line moved); `systems/settlements/_identifier_census.yaml` by `python tools/build_identifier_census.py` (`starting_pros` turns from defined to unresolved, the honest reading). Not edited: `params_tables.yaml:6576` (frozen; DEF-9 deletes it), `godot/data_serialization_spec.md` (stale).
- GATE: B10-16, first. NEEDS: none (DEF-9 is not a dependency: the deletion is correct whether the frozen table is still present or already deleted).
- EXIT and FALSIFIER: `python -c "import yaml; d=yaml.safe_load(open('systems/settlements/valoria_geography_v30.yaml')); assert not [t for t,v in d['provinces'].items() if 'starting_pros' in v]; assert len(d['settlements'])==37 and all(len(s['stats'])==3 for s in d['settlements'].values())"`. CONTROL: at the base commit the first assert fails (17 rows), so the defect is observable; the second holds on both sides. Then `python -m pytest engine/season/tests/test_mass_battle_module.py tests/valoria/test_mass_battle_terrain.py -q` (both open this file's `provinces:`).
- HASH MOVERS: EQUAL (`build_realm(0)` content hash equal against the base commit). Port: the geography YAML (opened by `data/files.py:148`, read by `data/geography.py`) crosses through GO-09; the port binds Prosperity at settlement grain only, and `godot/data_serialization_spec.md`'s `prosperity int # 0-5` (STALE) is implemented from nothing.
- HOLES AND LEDGER IDS: DEF-9 (the frozen table).
- ASKS ATTACHED: item 6 (`-05` §1b) `[ASSUMPTION; medium; Jordan to correct; revert: restore the 17 lines and re-pin the sha]`.
- RE-BASE: recount the eleven against `params_tables.yaml:6576` and the settlement sums at build.
- BUILDER: `CLAUDE.md` §10's second tier.
- SOURCE: `valoria_geography_v30.yaml:29`…`:237` against `params_tables.yaml:6576`; `01_AXIOMS.md:327-332` (T-a), `:512` (ID-1); Jordan's "reconcile all geography stuff with bias towards recency" (`valoria_geography_v30.yaml:241`).

````

### CP-T08-01

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T08-01 | Hands make the yield: one factor per rung, not per Site (G1; Γ1) | BUILD | E | — | no. | `cp-settlements-governance-economy`:— |
```

entry (`2026-10-23-subsystem-completion-08-settlements-governance-economy.md:73-89`):

````
### CP-T08-01 · Hands make the yield (G1; Γ1)

- **What it adds.**
  1. A Query `labour(w, site) → hands`: the summed `weight × body / body_scale` over the persons `share` already counts at the Site's rung — the same `presence` reading (`queries/world_q.py:1188`, read by `share` at `:429-444`), weighted by head count and strength instead of counted. Every person present counts at every producing Site of the rung: **nobody is assigned and nobody is refused.** Stored nowhere.
  2. A roster `rosters.yaml: site_crew` (per producing kind, the hands at which yield reaches its condition-scaled base) with its `hole_register.yaml` row (kind NUMBER, JQ-6's family; no magnitude is set here).
  3. The yield line (`loop/matter.py:589-591`) gains one factor: `× min(1, labour / site_crew[kind])` when the fixture `labour_mode` is `on`; `≡ 1` when `off` (shipped). `work` is not changed.
- **The two ruled rows, argued.** `D_T08:#59` (DIFFERS) records that Valoria's labour primitive is ruled as `share`, "no cap or assignment" (r2 `04` §A.6.4, quoted at `queries/world_q.py:435-438`); `D_T08a:#53` (DIFFERS) records that a work area which caps and auto-allocates workers is an institution deciding, refused by AX-1. This item composes on that ruling rather than beside it: (i) it reads `share`'s own presence set, so there is one reading of who is at a place, not two; (ii) it assigns no one — the earlier draft's even split across Sites and its `labour` edge are withdrawn, since a split rule is the auto-allocation AX-1 refuses; (iii) `site_crew` caps no worker and refuses no one: it is a yield curve (output stops rising past it), and a fifth man present is still present. The quantities differ: `share` divides a repair among those present; `labour` sums the strength of those present.
- **Owner artifacts.** `queries/world_q.py::labour` (one owner of the rule, beside `share`); `rosters.yaml: site_crew`; `data/fixtures.py: labour_mode` + its H-row; `loop/matter.py` (one factor). Binds L2.
- **Primitives.** P16 in the only form AX-1 admits here (where a person stands is his own act, `move`; no allocation rule); P20 (the body as the draw-down, through RB-5).
- **Reads / writes.** Reads presence, `Person.weight`, `Person.body`, `SITE_YIELD`. Writes: MATTER's existing `Rung.yield` and `stores` writes, one factor changed. ⚠ **Asymmetry (§0.1 pt 1):** the yield getter starts reading presence and bodies. Its writers are unchanged (MATTER only), but every writer of presence (`move`, `migrate`, `march`'s `_relocate`, `raze`'s cascade) and of body (`fight`, `tend`, MATTER's body fall) now moves output. Grep assignments of `contain` edges and `.body` at the build and list them in the commit.
- **Joins.** Persons/NP: cohort bodies (RB-5). Mass battle: a cohort felled or moved by `march` removes its hands (no MB change; MB gains a production consequence). CP-T08-02: with unlike places, where one stands decides what one's hands make.
- **Decision handed to the chooser.** Where to stand (`move`), whether to bring one's men (an establishment present adds hands), whether to keep a populace fed and whole. What a place makes is decided by its ground (CP-T08-02), not by an allocation. **Unwatched:** every populace works its own place by being there; a cohort that starves (RB-5) works less, so the town makes less food, so it starves faster (Banished's spiral, `D_T08a:#20`); a felled cohort's town stops producing (`D_T08:#83`). Lost against the earlier draft: the choice of grain against ore inside one town (§3).
- **Falsifier.** `engine/season/tests/test_labour_yield.py` on `harness/scarce.build`: (a) arm on, with crew above the cohort's weight, halving the cohort's weight halves the harbour's yield to the truncation; (b) a cohort at body 500 yields as half its weight; (c) a named person moving onto the rung raises every producing Site's yield there at the next MATTER, and moving off lowers it; (d) arm off, yield is byte-identical to today. Mutation: count present persons (as `share` does) instead of weighting them; (a) reds.
- **Control.** Paired seeds: `build_realm(s)`, s = 0, 1, 2, two seasons, arm off against arm on with `site_crew` at a value under the realm's weight (so the arm is inert by construction) — hashes equal; then a crew above it, where yield must fall and the off arm must not. The inert-by-construction arm is the check that the factor, not the code path, moves the hash.
- **Hash movers.** Off: none. On: every seeded realm hash (yield, stores, draws), `results.json`, the BASE_EVENTS pins RB-5 lists. **Revert:** `labour_mode: off`; then the code.
- **Size.** M.

````

### CP-T08-03

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T08-03 | Stores spoil (G3, G5; Γ3) | BUILD | E | CP-T08-01 | no. | `cp-settlements-governance-economy`:— |
```

entry (`2026-10-23-subsystem-completion-08-settlements-governance-economy.md:106-119`):

````
### CP-T08-03 · Stores spoil (G3, G5; Γ3)

- **What it adds.** A per-kind spoilage rate, `rosters.yaml: store_spoil` (per-mille of a rung's stock lost per season, by matter kind; shipped all 0 [ASSUMPTION; JQ-6's family]). MATTER's wear step (`loop/matter.py:643-691`) lowers each rung's stores by `int(stock × rate / 1000)` per kind, through the existing `stores` write and its existing `stores.changed` kind. No new Event kind, no new carrier. Matter decaying by itself is one of AX-5's three motions, so no act need wind it.
- **Owner artifacts.** `rosters.yaml: store_spoil` and its H-row; `loop/matter.py`. Binds L2.
- **Primitives.** P20 (source-side draw-down).
- **Reads / writes.** Reads `Rung.stores`. Writes `Rung.stores` (MATTER, the existing pair).
- **Joins.** CP-T08-05: a spoiling good is cheap to hold and dear to lack, so the price reads it through stores alone. RB-5: `cover` falls with spoilage.
- **Decision handed to the chooser.** Spend or move a surplus before it rots: requisition and pay now (CP-T08-08), trade it (CP-T08-05), or let it go. **Unwatched:** a town's grain pile stops growing without bound (0 → 9,250 realm-wide in two seasons today, T08 §5d) and settles where yield meets draw plus spoilage.
- **Falsifier.** `test_store_spoil.py`: with grain at 100 per-mille, 200 grain becomes 180 at the next MATTER and salt at 0 per-mille is unchanged; the conservation check (`effects_economy.py:199-208`) is not asked of MATTER's sink (it is one-sided, as `build`'s cost is). Mutation: apply the rate to `yield` instead of `stores`; the 180 reds.
- **Control.** All-zero rates reproduce today's hashes at seeds 0-2; a nonzero grain rate lowers realm grain at season 2 against the zero arm, same seeds.
- **Hash movers.** Off: none. On: every seeded realm hash. **Revert:** the rates to 0.
- **Size.** S.
- **Cut, not proposed:** a storehouse Site kind that halves spoilage (Songs of Syx). It would make storage a decision, but adds a Site kind, a works row and a reader for one modifier; §3 records the cut.

````

### CP-T08-02

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T08-02 | Places are endowed by their ground (G4; Γ2): ships `uniform`; the `ground` flip waits on a relief path that executes | BUILD | E | CP-T08-03; not a dependency: JQ-6 (the `ground` flip's magnitudes only; ships `uniform`) | — | `cp-settlements-governance-economy`:— |
```

entry (`2026-10-23-subsystem-completion-08-settlements-governance-economy.md:90-105`):

````
### CP-T08-02 · Places are endowed by their ground (G4; Γ2)

- **What it adds.**
  1. A Site kind `field` (yields `grain`) in `rosters.yaml: site_kinds`, `site_yield`, `wear_per_season`, `band_floors` (its use floors), `works_cost` (so `build` can raise one). Magnitudes are JQ-6's family; none is set here.
  2. A roster `rosters.yaml: site_endowment` mapping a ground class to the producing Site kinds a settlement there receives (e.g. `coast_or_river → harbour`, `mountain → seam`, `lowland → field`) [ASSUMPTION; medium; Jordan to correct; revert: the `uniform` arm].
  3. `harness/populated.py` (`:903-908`, "a site per producing kind", which today loops every kind with a `site_yield` row) places Sites from `site_endowment` in both modes, under the fixture `endowment_mode: uniform | ground` (shipped `uniform`). The roster's `uniform` entry lists exactly today's kinds (`harbour`, `seam`), so adding `field` to `site_yield` gives no shipped settlement a field; without this, the uniform path would mint 37 fields. The ground class is read from the authored geography the builder already loads (`data/files.py::GEOGRAPHY_YAML`: the settlement's `coords` against `terrain` polygons and `water` rivers and lakes) by one function, `ground_class(geo, settlement)`, at world-build only. No class is stored; no settlement row is edited.
- **Owner artifacts.** `rosters.yaml: site_endowment`, the `field` rows; `harness/populated.py::ground_class`; the fixture and its H-row. Binds L2 (world-build data the loop then reads as Sites).
- **Primitives.** P22's precondition (unlike stocks, without which no price moves); P21's raw end.
- **Reads / writes.** Reads the geography file (authored, already loaded). Writes Sites at build only.
- **Joins.** CP-T08-05 (a price needs unlike stores to steer). Mass battle: `fortification_of` reads garrisons, untouched. WT: settlement adjacency (distance) is WT's to price; not demanded here.
- **Decision handed to the chooser.** What to move where: salt exists only where water is, ore only in the hills, so a lowland town must get salt by `transfer`, `requisition` or `exchange`. **Unwatched:** an inland town's cohort draws no salt from its own larder and goes short of that kind (RB-5's `starving` band reads per-kind unmet), and its governors receive shortfall claims (IN-22) they can answer only by moving stock between settlements.
- **Falsifier.** `test_endowment.py`: under `ground`, a settlement whose coords fall inside a mountain polygon gets a seam and no harbour; a riverside one a harbour; every settlement gets at least one producing Site (R-COMPLETE: no settlement may yield nothing; the loader refuses a ground class mapping to an empty list). Mutation: map every class to every kind; the first assertion reds.
- **Control.** `endowment_mode: uniform` reproduces `build_realm(s)`'s hash for s = 0-2. Under `ground`, the count of `shortfall:salt` Observations over two seasons is > 0 where it is 0 under `uniform` (with RB-5 on), at all three seeds.
- **Hash movers.** Off: none. On: `build_realm` itself (Sites), so every seeded pin. **Revert:** the fixture.
- **Size.** M.

````

### CP-T08-05

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T08-05 | A price read from the draw record REM-50 reads (`price_base[kind] × (need + 1) // (stock + 1)`), and trade between places (G4; Γ5): paper until an `offer` has a producer | BUILD | E | CP-T08-02, REM-2B, REM-50; H-165; not a dependency: ED-IN-0297 (a stated limit: hand-built worlds only until an `offer` has a producer, AM-E-16) | no. | `cp-settlements-governance-economy`:— |
```

entry (`2026-10-23-subsystem-completion-08-settlements-governance-economy.md:136-152`):

````
### CP-T08-05 · A price, read off the place, and trade between places (G4; Γ5)

- **What it adds.** On top of REM-2B's restored `exchange` (IN-33's two-sided swap and its second-side operands, which this item does not re-specify):
  1. A Query `price_of(w, rung, kind) → per-mille value`: `price_base[kind] × (need + 1) // (stock + 1)`, where `stock` is the rung's stores of the kind and `need` is `demanded(w, rung)[kind] × price_horizon` (REM-50's owner of demand) plus the inputs of the recipes whose workshops stand at the rung (CP-T08-04). Stored nowhere (EC M10's shape).
  2. A roster `rosters.yaml: price_base` (one value per matter kind) and the fixture `price_horizon`, each with its H-row.
  3. `exchange`'s effect computes the return from the counterparty's prices: for an offer of `a1` of `k1` for `k2`, the counterparty's rung gives `a2 = a1 × price_of(r2, k1) // price_of(r2, k2)`; if `a2 = 0` or `r2` cannot cover it, `exchange.refused`.
  4. **Consent is an act the counterparty already made.** EC S6 read consent off the counterparty's rung state; that lets goods leave another person's rung on one person's act, the institution-decides shape AX-1 refuses (`D_T08a:#12, #53`). Instead a Record kind `offer` (exact keys `{at, until}`, `rosters.yaml: record_kinds`) is minted by `create_record` by a person who holds `at` or sits in a seat whose purview reaches it — a standing offer to trade at `at`'s prices. `exchange` requires a live `offer` naming `r2`; the offer's holder is the counterparty. The market is wound by his act and ends with his death or the Record's destruction (T-c). A computed `create_record` mints only `text` today (H-165), so offers form only from a hand-built or played act until the decision layer gives `create_record` an `offer` source — ED-IN-0297's problem in another kind, stated as a demand (part 2, §5).
- **Owner artifacts.** `queries/world_q.py::price_of`; `rosters.yaml: price_base`; `data/fixtures.py: price_horizon`; REM-2B's `exchange` effect (the return arithmetic and the `offer` clause); `rosters.yaml: record_kinds` (`offer`). Binds L2.
- **Primitives.** P22 (stock-responsive price; a fixed table would create no arbitrage, THROUGHLINES §2 P22).
- **Reads / writes.** Reads stores, `demanded`, `recipes`. Writes nothing new (REM-2B's `exchange` writes `Rung.stores` ×4).
- **Joins.** Decision layer: an `exchange` Candidate needs operands naming a counterparty rung and kinds; the source is the trader's own `stores:<kind>` claims (EC-G07's channel) — the decision layer's to form. Information: a trader learns a price only from claims about stores (AX-2); a stale claim makes a bad trade, which is lawful. SC: `bargain` would move the price by a contest's degree later (EC §3.8); not demanded.
- **Decision handed to the chooser.** Where to buy and where to sell: grain bought at a full lowland larder fetches more salt at a hungry coast. The holder of a place chooses whether to open it to trade (an `offer`) and so to let its stock flow at its prices. **Unwatched:** with CP-T08-02 on and offers standing, persons whose cells favour `exchange` carry surplus to dear places; a town in dearth draws grain by its high price (Sen's entitlement case, EC S6: the poor town with nothing to offer still goes short).
- **Falsifier.** `test_price.py` on a hand-built two-town world: the town short of grain prices grain above the town in surplus; an `exchange` of salt for grain at the short town returns less grain than the same offer at the full town; after the swap, the short town's grain price falls. Mutation: read `stock` from the actor's rung instead of the counterparty's; the second assertion reds. With the counterparty's `offer` destroyed, the same `exchange` is refused. And EC's own: across seeds, a rung in dearth receives more grain by `exchange` than a rung in surplus.
- **Control.** `exchange` executes 0 in the shipped realm today and REM-2B's arm sets its base; this item's control is REM-2B's merged hash with `price_horizon` at 0 and every `price_base` equal (every price equal, so `a2 = a1`: barter at par), against the priced arm, seeds 0-2.
- **Hash movers.** Every world where `exchange` executes. **Revert:** equal bases and horizon 0 (par barter), then the Query.
- **Size.** M.

````

### CP-T08-06

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T08-06 | The settlement's mood: `unrest(w, S)` over `stability`'s existing signs (G9; Γ9): a report until `requisition` executes | BUILD, with a STOP RULE (the story-telling fold of 2026-11-02, ED-IN-0311): if CP-T08-07's gate (H-163 limit 3(a), owned by CR-23) is not met at B10-16's entry (re-based by symbol; CR-23 closed in B10-06, so the condition is known before the batch opens), CP-T08-06 moves to B10-Z as HELD with it, because alone it is a gauge whose only reader is a census line; it does not merge into CP-T08-07's commit (P5) `[ASSUMPTION; medium; Jordan to correct; revert: delete the stop rule]` | E | CP-T08-05, REM-50 | no. | `cp-settlements-governance-economy`:— |
```

entry (`2026-10-23-subsystem-completion-08-settlements-governance-economy_part2.md:9-25`):

````
### CP-T08-06 · The settlement's mood: `unrest(w, S)` (G9; Γ9)

- **What it adds.**
  1. A Query `unrest(w, S) → (band, signs)`: `signs` is the sum, over the cohorts whose live `reside` edge names S (`residence_of`, `queries/world_q.py:1211`), of `−stability(c, S, unrest_window)` — the signs of unrest the populace itself holds about its own place. `band` is the first entry of a new `rosters.yaml: band_floors["unrest"]` row the reading falls under (`calm`, `restless`, `defiant`, `rising`) [ASSUMPTION; medium; Jordan to correct; thresholds a NUMBER H-row, a balance number in H-160's sense]. Stored nowhere (T-a; RB-5's route A, the same reasons).
  2. `stability`'s signs (`queries/person_q.py:481-505`, IN-23's one owner) gain the predicates listed in a new `rosters.yaml: unrest_signs` row: REM-51's hunger claim at band `hungry` or `starving`. Dominance deeds (which already include `requisition.taken`, so CP-T08-07's collections count with no new kind) and shortfall claims stay as they are. The list is a separate row so `standing_routes.dominance` does not move: that roster is also read by `world_q.reception` (speech erosion, `queries/world_q.py:601-604`), and adding a non-deed kind there would change speech and fail `data/verbs.py::_check_dominance_kinds`.
  3. A harness census line `unrest_by_settlement` (a band histogram; a report, never read by the loop — `uncontrolled`'s precedent).
- **Against the two Layer 1 lines that name unrest.** `04_CODE_ARCHITECTURE.md:257` puts "any social aggregate — no norms, unrest, legitimacy, …" on the Rung's NEVER line, and `loop/matter.py:657` says "S25: NO SOCIAL QUANTITY MOVES HERE". Both hold: (i) nothing is stored on a Rung or anywhere — `unrest` is a function over persons, the populace's own ledger of acts done to its place (deeds of `requisition`, seizure, death, field won) and of hunger, exactly the derived-over-persons shape IN-23's `stability` already is, read on demand; (ii) no MATTER step reads it — its one game reader is `requisition`'s effect at RESOLVE (CP-T08-07), not the barrier; the earlier draft's MATTER levy, which did read it inside MATTER, is withdrawn. If `04` is read as forbidding even a derived reading named "unrest" at place grain, the revert is to read the populace's `stability` directly at the one call site, with no world-side Query.
- **Owner artifacts.** `queries/world_q.py::unrest`; `queries/person_q.py::stability` (one clause); `rosters.yaml: band_floors["unrest"]`, `unrest_signs`; `data/fixtures.py: unrest_window`; `harness/populated.py::census`. Binds L2 (the census line binds nothing).
- **Primitives.** P01 (summed condition meter, bands); P10 at the one grain Valoria has for a populace (the cohort is the bloc); C3 of the NERS skill passes by construction: the reading is evaluated from claims a named person holds.
- **Reads / writes.** Reads cohort ledgers, `reside` edges. Writes nothing. ⚠ **Asymmetry:** `stability` is a getter whose result changes; it has no writer, and its readers are `harness/storybar.py::estimates` (a declared report move) and now `unrest`. Grep `stability(` at the build.
- **Joins.** Information: the signs arrive through existing channels (REM-51's hunger deposit; co-located deposit of `requisition.taken` at the taken-from rung, `[UNVERIFIED]` that the cohort present there holds a claim whose subject is its own rung). Factions: `uncontrolled(w, rung)` (`queries/world_q.py:1714`) is the revolt reading FA owns; this file asks FA to let a settlement at `rising` read as open to taking (§5). Endings: a settlement predicate an ending row may read (§5).
- **Decision handed to the chooser.** None directly: unrest is a consequence, read by `requisition`'s take (CP-T08-07). The governor's choices about it are relief (`transfer`), a lower rate, or pressing on. **Unwatched:** a town taxed and hungry grows restless from its own claims and pays less; one fed and untaxed calms as its claims fall out of the window.
- **Falsifier.** `test_unrest.py`: a cohort holding three `starving` hunger claims about its town reads the band the floors give; the same claims about another rung count nothing; a weight-1 resident adds nothing (only cohorts are the populace). Mutation: count claims by where the event happened rather than by subject; the second assertion reds.
- **Control.** No game code reads `unrest` until CP-T08-07's arm is on, so every season hash is equal with this item alone, seeds 0-2; the story-bar's `stability` spread moves only for persons whose ledgers hold the new signs (none in the shipped realm before RB-5's reach is on).
- **Hash movers.** None alone. **Revert:** the Query, the roster rows, the clause.
- **Size.** S.

````

### CP-T08-07

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T08-07 | A standing levy: the `tax` edict (G5, G6; Γ6, Γ8, Γ12 narrowed) | BUILD (M17 released: H-163 limit 3(a), a governor's stock claim, is owned by CR-23; AM-E-21) | E | CP-T08-06, REM-2B, CR-23; H-52, IN-10, H-163 | — | `cp-settlements-governance-economy`:— |
```

entry (`2026-10-23-subsystem-completion-08-settlements-governance-economy_part2.md:26-44`):

````
### CP-T08-07 · A standing levy: the `tax` edict (G5, G6; Γ6, Γ8, Γ12 narrowed)

- **What it adds** (GV Suite 4's `tax` and M-TAX, and Suite 3's `edict` carrier, built for the one kind that has a reader; `proclaim` and `ration` are not built here).
  1. A verb row `tax` (its own row, as GV's PROPOSED note R-04 has it, `proposals/2026-10-16-verbs/2026-10-16-verbs-14-lexicon-settlements-and-governance.md:11`; a seat-set rate is [ASSUMPTION; medium; Jordan to correct], `D_T08a:#10`). Eligibility `remit:issue` [ASSUMPTION; medium; Jordan to correct; precedent: `requisition`'s declared substitution, EC-G06; H-52 holds the remit roster's question]. Subject: a rung within the exercised seat's purview (IN-40's vassal ground included). Operands: `amount` (per-mille of the rung's yield), optional `until`. Stratum `binding_decision`, so the shipped chronicle filter publishes `tax.levied` to everyone alive (`epistemic.py:652-654`); no new publication route.
  2. A Record kind `edict` in `rosters.yaml: record_kinds` with exact keys `{kind, at, amount, until}` (GV M-EDICT's), and a roster `rosters.yaml: edict_kinds` with one member, `tax: {phase_in}`: the seasons the rate takes to arrive in full.
  3. **One slot per place** (P08): a live `tax` edict at `at` held by someone else refuses the act (`tax.refused`). The same holder's new `tax` at the same `at` closes his old edict and mints the new one in one write, and the phase-in restarts; so a change of rate costs the ramp, which is the lock (P07) without a lockout table.
  4. **Collection is the holder's act each season, never MATTER's** (`04_CODE_ARCHITECTURE.md:1165`, F.18: "A MATTER payment would be a fourth clock, so the repair is a verb"; quoted at `loop/effects_economy.py:290-292`). A question source `levy_due`, read from the holder's own held edict (IN-10's held-Record channel, `record_sourced_operands`, extended with `edict: {subject: at}`), forms once per season per live edict a `requisition` through the seat the edict's creating act went through (`state/attribution.py::causing_act`, `arrest`'s precedent): `subject` the edict's `at`, `kind` each kind he holds a stock claim of there, `amount` = `edict.amount × ramp ÷ 1000` × the stock his newest claim gives, where `ramp = min(1, (seasons since minted + 1) / phase_in)` [UNVERIFIED: which claim carries a rung's stock to its governor; IN-49's fixture requisition amount is the fallback]. The collection is the shipped `requisition` (`loop/effects_governance.py:426-464`): purview, stores, `requisition.taken`. Nothing moves unless he acts and pays the act from his budget; if he dies, is stripped, or never acts, nothing is collected.
  5. **Compliance, one rule for every requisition.** `requisition`'s effect takes `amount × unrest_compliance[band] ÷ 1000`, where `band` is CP-T08-06's `unrest` of the subject rung, read at RESOLVE; `rosters.yaml: unrest_compliance` (per-mille per band) ships all 1000, so the shipped `requisition` is unchanged. A restless town hides its stock from any taker, edict or no.
  6. **What this withdraws from the earlier draft.** The MATTER reader, the kinds `tax.collected` and `tax.withheld`, and the `defy` branch. That branch was unreachable: IN-09's `defy` keys on the actor's ledger claim of a held writ's terms (`workplans/valoria_master_workplan_v9_part5.md:49`), and no resident holds an edict. Resistance to a levy is a demand on social contest (§5), not built here.
- **Owner artifacts.** `verb_table.yaml` (`tax`); `loop/effects_governance.py::_eff_tax` and `_eff_requisition` (the compliance factor); the `levy_due` question source (`decision/options.py`, beside IN-49's requisition source); `rosters.yaml: record_kinds`, `edict_kinds`, `record_sourced_operands`, `unrest_compliance`; `data/verbs.py::KIND_VERB` (new kinds `tax.levied`, `tax.refused`); the `alignment` cells or `uncelled:` entry. Binds L2.
- **Primitives.** P20 (a recurring charge, act-paid as Valoria's upkeep is); P03 (lagged arrival); P08 (one per place); P07 (a change restarts the ramp); P14 in its Valoria form (the edict is a held token, killable with its holder); P05 (each collection costs an act).
- **Reads / writes.** `tax` writes `Record.exists`. `requisition` writes `Rung.stores` ×2 as shipped. ⚠ **Asymmetry:** `requisition`'s take now reads `unrest`; its writers are unchanged, but every writer of the populace's signs (`requisition` itself, `seize`, `fight`, MATTER's hunger deposit) now lowers what the next taker gets. Grep the dominance kinds' emitters at the build.
- **Joins.** CP-T08-06 (compliance). CP-T08-08 (the treasury the levy fills pays the establishment). Decision layer: the `levy_due` source. Social contest: resistance to an edict (§5). Factions: a covenant's tribute is paid by `transfer`, unchanged (EC §3.8); `seize`, `issue`, `give` + Rung and `confer` are not changed by this file.
- **Decision handed to the chooser.** The rate, the place, when to lower it, and each season whether to spend an act collecting. High rates fill the treasury now and make the town restless (its own `requisition.taken` claims), which lowers what every later taker gets; a town no edict names is levied by nobody (KoH II's governed-against-ungoverned split, in revenue rather than output; `D_T08a:#32` narrowed). **Unwatched:** an NPC seat-holder whose cells favour `tax` and `requisition` levies the towns in his purview and collects when the question wins his budget; a dead lord's levy stops; a hungry, overtaxed town's payments fall to the compliance floor.
- **Falsifier.** `test_tax_edict.py` on `harness/scarce.governed`: with a 200 per-mille edict and `phase_in` 2, the holder's `levy_due` question forms a `requisition` for 10 % of the stock he knows in the first season and 20 % in the second; with no act, nothing moves at MATTER (the F.18 check); the holder's death leaves no question; a second seat's `tax` on the same town is refused; at band `defiant` a requisition takes the `unrest_compliance` share. Mutation: read `unrest` at the seat's rung rather than the taken-from one; the last assertion reds.
- **Control.** `tax` ships in `Fixtures withheld_verbs` and `unrest_compliance` at 1000: hashes equal today's at seeds 0-2. Formable, the paired comparison over two seasons shows `requisition.taken` > 0 through seats and treasury stores > 0 on territory rungs, which are 0 today (T08 §2.3; `requisition` 2/0, 5/0, 5/0).
- **Hash movers.** Withheld: none. Formable: every seeded realm hash (new candidates, new writes). Compliance below 1000: any world where a requisition executes. **Revert:** withhold the verb; compliance to 1000; then the row, the kind, the source.
- **Size.** L.

````

### CP-T08-08

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T08-08 | The upkeep payment gets a question (G5; Γ7): forms only against a stocked treasury, never to the seat's own rung | BUILD | M (a declared candidate mover: home part 2 :58; it forms 0 acts in computed play until a treasury holds stock, `-08` AM-E-19) | REM-2A; IN-49; not a dependency: CP-T08-07 (the home's order only; it holds nothing behind it, AM-E-18) | — | `cp-settlements-governance-economy`:— |
```

entry (`2026-10-23-subsystem-completion-08-settlements-governance-economy_part2.md:45-60`):

````
### CP-T08-08 · The upkeep payment gets a question (G5; Γ7)

- **What it adds.**
  1. A question source `upkeep_due` for a seat-holder, built from **his own held claims** (AX-2): each `duty.taken` claim naming a seat he holds whose claimed season plus `oblige_term` falls within `upkeep_lead` seasons of his newest claim, and for which he holds no later `term.renewed` claim, grouped by the obligee's last-known place. It forms one `transfer` Candidate per group: `via` the seat, `from` the seat's rung, `to` that place, `kind` grain, `amount` = obligees in the group × upkeep. The payment is still an act, so `04` F.18's ruling ("the repair is a verb", quoted at `loop/effects_economy.py:290-292`) stands; what was missing is the occasion.
  2. One WITNESS route: `duty.taken` is deposited to the holder of the seat the `oblige` names (the `post_remit` channel, `loop/witness.py:60`, widened from "obligees of the seat that acted" to "the holder of the seat an act names"). Today `oblige` is `social` and own-eligible, so only those standing there learn of it.
  3. The seat's per-seat upkeep reaches the holder through the hold's payload snapshot, as `granted_acts` does, or else the fixture `default_upkeep` is used person-side [UNVERIFIED: whether `Office.upkeep` is in any snapshot today].
- **Owner artifacts.** The decision layer's question-source registry (`decision/options.py`, beside `_from_shortfall_claim`); `loop/witness.py` (one channel clause); `data/fixtures.py: upkeep_lead` with its H-row. Binds L2.
- **Primitives.** P20 (the wage drain, here act-paid); P14 (the term as a contract that expires, JA2's shape, `D_T08a:#45`).
- **Reads / writes.** Reads the holder's ledger and fixtures. Writes nothing itself; the `transfer` it forms writes `Rung.stores` ×2 and `Tenure.term` through the shipped `_renewals` (`loop/effects_economy.py:287-356`).
- **Joins.** Information (the deposit). Decision layer (the source). CP-T08-07 (a treasury with stock in it). IN-49's `requisition` source already forms a requisition on a stocked larder in purview (`rosters.yaml:630-637`), so an empty treasury has a refill route.
- **Decision handed to the chooser.** Pay the men before their terms run out, or let some go (pay fewer than are due; the soonest-maturing are renewed first) and keep the stock. **Unwatched:** a seat-holder with a levied treasury keeps his establishment; one without lets it lapse, and every lapse is public (`tenure.closed` is broadcast). H-159 (lapse or arrears) is untouched: lapse stays the consequence.
- **Falsifier.** `test_upkeep_question.py` on `scarce.governed`: an obligee sworn three seasons ago puts a `transfer` Candidate through the seat into the holder's questions, to the obligee's last-known place, for `upkeep`; executing it emits `term.renewed`. Mutation: take `to` from the obligee's residence instead of his last-known place (H-174's other reading); the renewal reds when he stands elsewhere. Realm reading: seed 1, six seasons, `term.renewed` > 0 (0 today, T08 §5c).
- **Control.** `upkeep_lead: none` (the source off) reproduces today's hashes at seeds 0-2.
- **Hash movers.** On: seed 1 (the only seed with act-made obliges at two seasons) and any later seed that forms obliges; every seed through the widened deposit. **Revert:** the source off; then the channel clause.
- **Size.** M.

````

### CP-T08-04

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T08-04 | `craft`: goods made from goods (G2; Γ3, Γ4) | BUILD (M5 released: a workshop is raised by `build` on an authored works row, IN-45) | E | REM-2B, IN-45; IN-08 | — | `cp-settlements-governance-economy`:— |
```

entry (`2026-10-23-subsystem-completion-08-settlements-governance-economy.md:120-135`):

````
### CP-T08-04 · `craft`: goods made from goods (G2; Γ3, Γ4)

- **What it adds.**
  1. A verb row `craft` (EC Suite S2's NEW ROW, its name and shape): actor present at a workshop Site; operands `site`, `kind` (the product), `amount`. Typed precondition: present at `site`; the Site's kind admits the recipe; its condition is at or above the recipe's floor; the Site's rung holds `inputs × amount`. Writes `Rung.stores` at that one rung (inputs down, product up, one write). Emits `goods.made`; refusal `craft.refused` (the scarcity channel). Uncontested, no draw.
  2. A roster `rosters.yaml: recipes` (product → `{inputs: {kind: n}, site_kind, floor}`), refused at load if a product or input is not a registered matter kind or the Site kind has no row.
  3. Two workshop Site kinds, `smithy` and `mint`, with `works_cost`, `wear_per_season` and `band_floors` rows and no `site_yield` (a workshop yields nothing by itself), raised by the shipped `build`. One new matter kind, `arms`. Recipes at adoption: `coin ← ore` at a mint; `arms ← ore + timber` at a smithy [ASSUMPTION; medium; Jordan to correct; quantities are JQ-6's family].
- **Owner artifacts.** `verb_table.yaml` (`craft`); `loop/effects_economy.py::_eff_craft`; `rosters.yaml: recipes`, `site_kinds`, `matter_kinds`, `works_cost`, `wear_per_season`, `band_floors`; the `alignment` cells or `uncelled:` entry. Binds L2.
- **Primitives.** P21 (fixed-ratio recipe); P20 (inputs consumed).
- **Reads / writes.** Reads `Rung.stores`, `Site.condition`, presence. Writes `Rung.stores` (the `(Rung, stores)` matrix pair exists, `verb_table.yaml` `build`'s row). ⚠ Asymmetry: none (a new writer of an existing field; no getter changes).
- **Joins.** Mass battle: MB's troop-stock design names no arms producer (`proposals/2026-10-16-troop-stock-design.md:101-104`, cited by EC S2); `arms` stock is what MB's `equip` would read (MB's to wire). CP-T08-05: coin becomes a medium the price can name.
- **Decision handed to the chooser.** Coin or arms from one seam's ore; build a smithy or a dwelling with the timber. **Unwatched:** an NPC present at a workshop with stock forms `craft` by its cells; a town with a mint and no seam must import ore.
- **Falsifier.** `test_craft.py`: a person at a mint whose rung holds ore 10 crafts coin by the recipe and the rung's ore falls by exactly the input; with ore short, `craft.refused` and no partial product (R-COMPLETE). Mutation: drop the input debit; the store-mass check (inputs out equal recipe × amount) reds.
- **Control.** `craft` ships in `Fixtures withheld_verbs` (v9 IN-26's switch, read first by `decision/options.py::opening_set`, `:124`), so nobody forms it and every hash is today's at seeds 0-2. It is not equal "by construction": a formable typed row whose presence clause reads UNKNOWN person-side forms on every referent and crowds scenes (H-156's measured shape, `hole_register.yaml:3615-3619`), so the arm that drops it from `withheld_verbs` is a declared mover, read for scene crowding before it ships. The falsifier runs on a hand-built world through the real fold.
- **Hash movers.** Withheld: none. Formable: every seeded realm hash (new candidates), and every world where a workshop is built. **Revert:** withhold the verb; then delete the row, the rosters and the kinds.
- **Size.** M.

````

### IN-52

card row (`valoria_master_workplan_v11_part3.md`):

```
| IN-52 | the levy-to-field feed (now `requisition`): levied stores provision a season field | the flip: BUILD (released from M17, on CR-23; it provisions fields from treasuries filled by requisition and moves no pin while the realm fights no field) · the retirement: HELD on M3 | M (the flip, its own declared commit; no pin moves while the realm fights no field) | CR-23 | M3 (the retirement) | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:748-760`):

````
### IN-52 — the levy-to-field feed (now `requisition`): levied stores provision a season field (IN; SE, MB) · BATCH B10-16 (the flip, last) · STATE BUILD (the flip, released from M17 through CR-23); its retirement HELD on M3 · R —
- DECISION ROUND: the flip is released: CR-23 (B10-06, M17 taken) is the owner of H-163 limit 3(a), so `requisition` executing in computed play is CR-23's exit (met at B10-06's close, `7362fa46f`), not an unowned gap. The flip provisions fields from treasuries filled by requisition and moves no pin while the realm fights no field; it lands as B10-16's last commit, a declared mover. The row's retirement stays HELD on M3 (`-05`). NEEDS gain CR-23 (B10-06). If CR-23 reverts (`stock_report = off`), the flip re-holds.
- WHAT: flip `field_provisioning` ON, in its own commit; moves no pinned hash while the realm fights no field (H-241); the decisions owed at the flip are H-241's `default:`. (Verb rename 2026-10-16: the Rung.stores verb `levy` is `requisition` in code; `levy` is reserved for the verb that raises troops — `proposals/2026-10-16-troop-stock-design.md`, PROPOSED.)
- LANDED ALREADY: the OFF build `128bc9db` (B-T, #503). LF-1..LF-3 DELEGATED-RULED 2026-10-12 [ASSUMPTION; medium; Jordan to correct]: LF-1..3 adopted; build ships OFF (hash-neutral); flip ON is its own commit.
- REMAINING UNBUILT: the flip ON (`engine/season/data/fixtures.py`, the default). H-241's owed decisions: ration min over kinds, casualties on all losers, defender debit.
- GATE: `requisition` executing in computed play (H-163 limit 3(a)), read at CR-23's exit (B10-06, MET at its close: `aperture 4 s`, realm, `requisition` executed 4 / 6 / 8 at seeds 0 / 1 / 2, `requirements.yaml` R-04); without it a flip "would floor fields on whatever treasuries the build seeds; its falsifiers run on hand-built worlds" (H-241).
- EXIT and FALSIFIER: EXIT "with it on, in a seeded season a side's fielded troops are bounded by its levied treasury." FALSIFIER "on, a side with an empty treasury fields as many troops as a full one -> the bound is not built."
- HASH MOVERS: "moves no pinned hash while the realm fights no field (H-241)"; `content_hash` folds no fixture.
- HOLES AND LEDGER IDS: H-163, H-241; J-18 (cited as SOURCE); `proposals/2026-10-07-settlements-computation-modules.md`.
- ASKS ATTACHED: none open (LF-1..3 delegated-ruled).
- RE-BASE: B-T (#503) built the OFF feed and, per the commit subject, "IN-52 shipped off"; v9 records it. Verb rename `levy` -> `requisition` (#482) post-dates the original entry. None found since B-T.
- SOURCE: `v9_p4:100-105`; state-index row `v9.md:268`; `v9_p5:339` (LF ask-then row).

````

### IN-30

card row (`valoria_master_workplan_v11_part3.md`):

```
| IN-30 | H-186 GD-3's insurgency beyond its first condition; an emerged faction (= SE-05, FA-02): faction identity gets one owner that admits emergence, `queries/world_q.py::faction_props` (the rostered faction Propositions plus every Proposition in the creed shape, the shape a roster key `factions.creed`), founded by a person's own `utter` of a creed; it ships with the GD-3 FAIL named on H-186 (an emerged creed cannot `seize`) `[ASSUMPTION; medium; Jordan to correct; revert: faction_props returns FACTION_BY_PROP's keys; the creed term dropped]` | BUILD (with CP-T09-04 (d) as its acting caller) · STOPPED (at B-U, closed `156f3e5d`, unbuilt: finding in H-186) | M (declared wherever a creed is uttered; EQUAL at build) | — | `-05` §1a (c) | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:125-139`):

````
### IN-30 — H-186 GD-3's insurgency beyond its first condition; an emerged faction (= SE-05, FA-02) (IN; FA, SE) · BATCH B10-17 · STATE STOPPED (at B-U, closed `156f3e5d`, unbuilt: finding in H-186) · R —
- SECOND DECISION ROUND (item 4, make the endings reachable, `-05` §1b; B10-17, first, slot and NEEDS unchanged; faction identity taken at step 4, its occasion at step 5): faction identity gets ONE owner that admits emergence, `queries/world_q.py::faction_props(w)`: the rostered faction Propositions (`data/rosters.py:996`, `FACTION_BY_PROP`) plus every Proposition in the world in the creed shape (`mood: OUGHT`, `predicate: "carries the creed of"`, `harness/populated.py:1090`), the shape hoisted to a roster key `rosters.yaml: factions.creed` read by the builder and the Query ([UNVERIFIED] whether the roster loader accepts the subkey); `faction_holding` (`world_q.py:1876-1882`) and every other "is this a faction" test read it (every reader of `FACTION_BY_PROP` is enumerated at the build). No threshold, counter or stored entity. The founding act is a person's own `utter` of a creed (mood and predicate from the roster key, `value` the new Proposition's id, `subject` the founder); membership is the existing `commit`. Its occasion is CP-T09-01's leaver: CP-T09-01's body, built only if its measurement finds a leaver, offers the creed `utter` to a person whose opinion of each rostered faction he is committed to has fallen below indifference and who `release`s that `commit`, formed only if he holds a seat or a land `hold`; if no leaver is measured, the creed lands as a hand-built mechanism (this falsifier) and its realm reading is a named residue. GD-3 (a)'s trigger is not carried (contiguity has no carrier since `29c`, H-186; the streak is a clock, #457 §5; a world event that forms an insurgency with nobody choosing is a threshold producing an outcome, T-b). **GD-3 FAIL:** an emerged faction keeps the land its founder held and receives land by cession (CP-T09-05's `give` + Rung), but cannot take more by `seize` (`seize` requires the actor committed to his seat's faction, and a seat's faction is the authored `Office.faction`); that fails GD-3's violation test (`canon/04_game_design_constraints.md:29`) and is recorded on H-186 as a GD-3 FAIL, not a stated limit; IN-30 ships with the FAIL named, and the fix (a seat serving an emerged creed, every same-faction rule then re-reading `seat_faction`) or an amended GD-3 is `-05` §1a question (c), confirmed at the default (ED-IN-0301): IN-30 ships with the FAIL named on H-186, and the question blocks nothing built now. EXIT is met by CP-T09-04 (d) for `uncontrolled` and by `faction_props` for emergence. FALSIFIER (hand-built, real fold): a land-holding seat-holder `release`s his faction `commit`, `utter`s a creed and `commit`s to it → `faction_holding` names the creed, his territory is not `uncontrolled`, and a planted world with every realm territory under the creed's members reports `peninsular_sovereignty`; CONTROL: the same with a non-creed OUGHT → not a faction (today's reading); mutation: drop the predicate test → every uttered OUGHT becomes a faction and the build's `uncontrolled` reading moves → red. HASH: declared MOVER wherever a creed is uttered; EQUAL at build (the six creed Propositions of `build_realm(0)` are all in `FACTION_BY_PROP`; a probe, not re-run). READINGS: `faction_props(w)` size per season, seeds 0-2, eight seasons (base 10), and land held under non-rostered creeds (base 0). PORT: the faction set becomes a function of the world; a GDScript port must not cache `FACTIONS` as an enum for identity (display names stay the roster's; an emerged creed's display name is its founder's). BUILDER: `CLAUDE.md` §10's third tier (judgment). `[ASSUMPTION; medium; Jordan to correct; revert: faction_props returns FACTION_BY_PROP's keys; the creed term dropped]`
  - **CP-T09-04, built with this position (one build, two handles; its home and B10-17 build card carry the rest), gains the unpeopled clause:** an unheld place in whose subtree no faction is `mustered` is licensed to a seat whose purview reaches it (`purview_reaches`), in the one owner `loop/effects_shared.py::occupying_faction` (`:149-165`), shared by `seize` and `raze`; `raze` keeps CP-T09-04's explicit unheld decline, so the clause licenses a taking, never a razing; term (d) offers such places as well. LADDER: step 4 on the gate's own seizure reading (`may_seize` asks the seat's purview over the rung, `gate.py:1208-1221`), not on ED-IN-0256 (4) (that ruling defines governing authority, and H-90's message 1 separates it from holdings). Still not covered, named: GD-1's Accord, Stability, sustain and treaty clauses (the translation's lawful F3 forms are the route; each needs a band nobody has given, a residue whose trigger is a ruled band); an emerged faction's seizures (the GD-3 FAIL above); a seizure by a seat-holder not committed to his seat's faction. FALSIFIER (5): a planted world where every realm territory but `terr_T15` is held by Crown persons and nobody stands under `terr_T15`: the realm seat's computed `seize` of `terr_T15` executes and that season's `endings` contains `peninsular_sovereignty`, credited to the seize's opened `hold` (T-b); CONTROL: the clause off → `seize.refused` and `endings == []`; mutation: drop the purview conjunct → a Hafenmark seat (no purview over Askeheim) seizes it → red. H-176's "structural zero" clause and the `endings` note (`rosters.yaml:2595-2596`) are rewritten in its commit. READINGS: `rung.seized` on territories and `uncontrolled_in_realm` per season, seeds 0-2, eight seasons (base 11 after one season, H-186), and `SeasonDriver.season`'s `endings`; [UNVERIFIED: whether any seat's question in seeded play names `terr_T15` once (d) offers it; not run]. PORT: a Godot consumer reading `victory: true` as the game's end breaks GD-1's two-season test, so it carries the ending row's caveat. `[ASSUMPTION; medium; Jordan to correct; revert: drop the clause]`
  - The GATE, EXIT, FALSIFIER and HASH lines below are v9's and are superseded by this block where they differ; CR-39 (B10-Z, HELD on CR-38) is the emerged creed's promotion.
- WHAT: `24h` P5's remainder. `queries/world_q.py:1192` `uncontrolled` is the built first condition and its only non-test caller is a report (`harness/populated.py:1304`). Build a caller that acts on it, and faction emergence: contiguity, streak, promotion and emerged-faction identity have no carrier, and no verb acts on unheld land (H-186).
- LANDED ALREADY: the first condition `uncontrolled` (report-only caller); `raze` `68eaaa41` (H-166 limit 3's closer; executes 0 in computed play, H-228 limit 3); IN-27 `6ae70998` (ending vocabulary) and D4/D6 answers (RS-21 items 3 and 4).
- REMAINING UNBUILT: an acting caller of `uncontrolled` in `queries/` or `loop/` that a person's choice reaches, in a seeded season; faction emergence; design choices for adjacency, streak counter, promotion thresholds, emerged-faction identity. Per H-186, one of three choices first: (a) H-166 seize on an unheld settlement, (b) `march` `referent_class: Rung`, (c) a question source.
- GATE: BLK: H-149's march-target positions (`raze`, H-166 limit 3's closer, landed and executes 0 in computed play: H-228 limit 3) — "no ruling owed: ladder answered it in H-186"; #457 D4 and D6 answered (RS-21 3 and 4) [medium; Jordan to correct]. FA-01's content (B-V) is NOT a data edge [ASSUMPTION; if faction emergence needs FA-01's content, IN-30 moves behind B-V — now landed]. Rides the first batch that edits `queries/world_q.py::questions_for` or the Rung-stamp cell (R1/R8). EDITS `questions_for` stamp source in `queries/world_q.py`, called from `loop/driver.py::_questions_at_barrier`; `queries/world_q.py::faction_holding`.
- EXIT and FALSIFIER: EXIT "`grep -rn "uncontrolled(" engine/season/queries engine/season/loop --include=*.py` shows a caller in `queries/` or `loop/` that a person's choice reaches, and it executes in a seeded season." FALSIFIER "report still the only non-test caller -> not built." Revert: either answer reverted (RS-21 3 or 4) -> this position reverts with it.
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: H-186 (its row in `engine/season/hole_register.yaml` records the GD-3 FAIL in this position's build commit), H-149, H-166, H-176, H-228; RS-21 (3, 4); FA-01. Aliases SE-05 and FA-02 take this position's batch (both state-index rows read "= IN-30").
- ASKS ATTACHED: none open ("no ruling owed") for v9's remainder; the GD-3 FAIL's fix is `-05` §1a question (c) (above), confirmed at the default (ED-IN-0301).
- RE-BASE: B-U (#494, "IN-30 stopped") is the stop; B-R (#496) landed `raze`/`give`+Rung whose realm execution stays 0; B-V (#498) landed FA-01's content. v9 carries all three. None found since.
- SOURCE: `v9_p5:66-71`; state-index row `v9.md:258`; aliases `v9_p6:97` (SE-05), `v9.md:279` and `:293`.

````

### CP-T09-04

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T09-04 | Land with no holder, and territories, are taken by plurality occupation; the second decision round adds the unpeopled clause (an unheld place in whose subtree no faction is `mustered` is licensed to a seat whose purview reaches it, in the one owner `occupying_faction`; a taking, never a razing), so `peninsular_sovereignty` becomes reachable `[ASSUMPTION; medium; Jordan to correct; revert: drop the clause]` | BUILD · CR-71 (reading @5d6aac5, `aperture 2 0` and `strife 2 0`, seed 0, `PYTHONHASHSEED=0`, REALM): XN's `seize` reaches the fold and is refused there, attempted 8, executed 0, all 8 refused after admission on `clause:write`, which pools the Record half and the Rung half (`verb_table.yaml` `seize`) and a subject of neither kind; which is not read. `raze` (VI, PU) shares this row's owner: attempted 12, executed 0, 10 refused after admission in `_eff_raze` (`occupying_faction` or `mustered`) | M | IN-30; H-166, IN-40 | — | `cp-factions-war-diplomacy`:255-302 |
```

entry (`2026-10-23-subsystem-completion-09-factions-war-diplomacy.md:255-303`):

````
### CP-T09-04 · Land with no holder, and territories, are taken by plurality occupation

- **Adds.** Edits at one owner, `es/loop/effects_shared.py:149` `occupying_faction`, which `seize`'s Rung half and `raze` share, and an
  occasion. (a) **Unheld place** (H-166): for `seize`, a place whose `holder_faction_of` is `None` licenses when the seat's faction is the
  strict plurality of the factions `mustered` there. **`_eff_raze` has no decline of its own** — it relies wholly on `occupying_faction`
  (`es/loop/effects_founding.py:285-287`), and the `holder is None` test lives in the shared owner (`es/loop/effects_shared.py:163`) — so
  the same commit adds the "nobody holds the place" decline to `_eff_raze` explicitly; without it `raze` would destroy every unheld
  settlement (after the season-0 collapse, those under 11 of 16 territories). `raze`'s realm reading (base 22 reached the fold / 0 ok) is a
  declared mover. (b) **Plurality against a holder, for a town taken without a fight**: where no field was won there this round, a held
  place licenses only when the seat's faction has strictly more members mustered there than the holder's faction — Pax Pamir's rule
  (`D_T09 #44`), replacing "one resident suffices" (`T09 §5b`) and re-recording the arm at `es/tests/test_march.py:918-930`. **After a won
  field the licence is unchanged**: a won field removes no defender (`es/tests/test_march.py:913`), and the seizure that follows is
  admitted by #453 exit (vii) (`EI:958-959`, pinned at `test_march.py:893-915`); T04 relies on it ("Title after a win is already
  `seize`", T04's file `:76`; its §4 walk-through takes title by `seize` after an arrival). Plurality after a win too is the stated revert, and
  taking it re-records `:893-915` and collides with T04. "A field was won here this round" is read off the round's own `field.won`
  Event naming the place [UNVERIFIED: which Event field names the field's rung]. (c) **Territories**: `seize`'s target kinds become a roster key, `RY: seizure_target_kinds`
  = `march_target_kinds` ∪ {territory}, taking the stated revert of the open assumption at `EI:961-963` (*"revert: any Rung kind, the
  licence still occupation"*), restricted to territory; `raze` still reads `march_target_kinds`. A territory's occupation is `mustered` in
  its subtree (`WQ:1477` reads the subtree). (d) **The occasion — IN-30 re-scoped** (an edit to `_part5:66-71`): a `Rung`-class standing
  term offering a holder of a seat granting `issue` the rungs `uncontrolled` (`WQ:1714`) returns inside that seat's purview where the seat's
  faction is mustered; the seat's self-warrant (`issue`, C3, `VT:1141`) forms on them and `seize` follows through `warrant_sourced`. This
  is the production caller IN-30's EXIT asks for (`_part5:70`); IN-30's emergence half stays IN-30's.
- **Consequence.** After a death the land is contested by every seat that reaches it, in order of who has people standing there; the
  victory row `peninsular_sovereignty` becomes reachable (`terr_T15` can be taken), and its assumption note (`RY:2591-2592`, *"no verb opens
  a `hold` on any territory"*) is rewritten in the same commit — it is already stale for cession (`give` + Rung opens one).
- **Owner · Layer.** `es/loop/effects_shared.py`, `EI` `_seize_rung`, `RY` (one key), `WQ` (one term) · Layer 2.
- **Primitives.** P35 (the field, where one is fought), P42 (the existing ending row made reachable); Pax Pamir's rule by plurality
  (`D_T09 #44`) as the licence.
- **Reads / writes.** Reads `mustered`, `holder_faction_of`, `uncontrolled`, `purview_reaches`. Writes `seize`'s existing pairs.
- **Joins.** T08 (GV): `seize` (remit `issue`) and the self-warrant, and **`raze`'s occupation licence**, which is GV's act on a place
  (routed to T08, not T04): it moves with (a)'s explicit decline and (b). T04 (MB): none required; the won-field licence T04 relies on is
  kept.
- **Decision.** A seat-holder chooses whether to take the land his people stand on; any member's residence is a vote of presence.
  Unwatched: the season-0 collapse (11 of 16 territories uncontrolled at tick 2 in every seed) becomes a scramble instead of a steady state.
- **Asymmetry.** `occupying_faction` is a getter with two callers (`seize`, `raze`; grep both before the edit); the writers of `contain`
  and `hold` are untouched.
- **Falsifier.** (1) Seed 0, tick 1, King dead: the Widow Regent's seat (`off_npc_032`, realm purview, `issue`) seizes a former royal
  territory where Crown members are the plurality; a territory where another faction outnumbers the Crown refuses. (2) (b)'s arm at
  `set_s_036` (Church 6 of 9 persons, Crown 1), no field: `seize.refused`; move at least six more Crown members in (Crown 7 > Church 6) →
  `rung.seized`. Mutation: drop the comparison → the first arm executes. (3) After a won field at `set_s_036` the seizure is still admitted
  (`test_march.py:893-915` unchanged). (4) `raze` on an unheld settlement → `raze.refused` (the explicit decline). Realm reading:
  `uncontrolled` at tick 2, seeds 0-2, base 11; `raze`, base 22/0.
- **Stopping rule.** A seat's purview widens with every seat-holder sworn to it (IN-40's `oblige` clause, `es/state/gate.py:389-398`), so
  a won `recruit` (CP-T09-07) of a rival seat-holder brings his ground into term (d)'s seizable land across factions: the reading counts
  seizures through a sworn seat's ground separately, and if they exceed seizures in the seat's own ground, the `recruit` arm is reverted
  first.
- **Hash · revert.** Mover (re-records `test_march.py:918-930`; `raze` moves) · per sub-edit: H-166's decline back; one head; the roster
  key; the term. **Size** M.

````

### CP-T09-01

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T09-01 | Allegiance follows opinion: join, leave, switch (measure first: the body is built only if a leaver exists); its body carries the creed `utter` option for a leaver who holds a seat or a land `hold` (IN-30's founding act); with no leaver measured, the creed lands hand-built and its realm reading is a named residue | MEASURE first, then BUILD only if a leaver exists · CR-71 (reading @5d6aac5, `aperture 2 0` and `strife 2 0`, seed 0, `PYTHONHASHSEED=0`, REALM): `release` executed 2, both as `tenure.closed` with no `commit` edge; `commitment.ended` 0, this row's realm base | M | CP-T02-05 (landed `1ef8d273`, re-taken inside CR-28), CP-T09-04, REM-21, REM-23, REM-24; IN-57, IN-70; not a dependency: ED-IN-0296 (the measure-first reading does not wait on M1) | — | `cp-factions-war-diplomacy`:113-155 |
```

entry (`2026-10-23-subsystem-completion-09-factions-war-diplomacy.md:113-156`):

````
### CP-T09-01 · Allegiance follows opinion: join, leave, switch

- **Adds.** (rulings sheet R9) **Join is a filter, not a route.** T02's CP-T02-05 `oughts_named` is the one stamper by which a person
  takes up a cause he has heard of; creeds are OUGHT (`WQ:1961-1965`), so without a filter `commit` forms on every rival creed he has
  heard of, ungated. This item filters that stamper's output for **creed** Propositions (rostered factions' only; other OUGHTs pass
  untouched): a rival creed F passes iff `opinion_of(w, p, F) > max(0, opinion_of(w, p, own))` (own = 0 for a person in no faction).
  `commit` (REM-23's class) then forms only on creeds he favours over his own. **Leave** is a new stamper body: on a question whose
  referent is the head of p's own faction (the creed subject, `WQ:2099-2100`) or a member-doer his ledger names, stamp his own creed iff
  `opinion_of(w, p, own) < 0`; `release` forms on it (T02 offers an own cause for release only when it is met or spent). A switch is the
  two in turn, each his own act; **joining before leaving** gives two memberships, which by `faction_holding` (`WQ:1649-1660`) makes any
  land he holds uncontrolled (`WQ:1731-1733`) — declared, not prevented. The score is untouched (`es/decision/choose.py:130`). A
  discontented member's **petition** to his head needs no term: the head is tier 0 for every creed member (ambition referent, IN-57) and
  REM-24 classes `petition` on Person. Execution of a computed `commit` is also screened by IN-57's own-act screen (ED-IN-0296 (3),
  remediation part 02 `:383`), which this item does not decide.
- **Owner · Layer.** `WQ` (the filter, registered and checked as its own body on `oughts_named`'s output; the leave body; the
  indifference point 0 named once, beside `opinion_of`, and read by IN-70's gate at `WQ:2157` too) · Layer 2. Note `opinion` is documented
  as consumed only as `< 0` (`PQ:545-547`); the join reads it as `>`, so that docstring changes in the same commit.
- **Primitives.** P11 at faction scale (IN-70), P33 (scar-shifted pursuits enter `opinion_of` through `projected_axes`), P08 refused
  (dual membership stays possible and priced by land, as built).
- **Reads / writes.** Reads `opinion_of`, `faction_holding`, `members`, the creed Propositions. Writes nothing; the acts it lets form write
  `(Tenure, since)` and `(Tenure, until)`, existing matrix pairs.
- **Joins.** T02 (persons): **CP-T02-05** (`oughts_named`, the stamper this item filters), REM-21's registry and REM-23's class. T05 (SC):
  `petition` on Person (REM-24). T08 (GV): land follows `faction_holding` with no edit.
- **Decision.** Whether to act on the occasion (join, leave, petition, or any other act the question offers). Unwatched: one witnessed
  deed by a head (a killing, a seizure, a revocation) moves the regard term of every witness's `opinion_of` at once, so a faction loses
  members — and, through `faction_holding`, their land — in one season with nobody aiming at land: Imperator's secession (`D_T09 #28`)
  without its timer, and a shock on a ruler's death (`#71`), since a dead head leaves the regard term.
- **Falsifier.** Hand-built through the real fold, seed 0, tick 0: two Crown members with equal pursuits; one carries a stance row
  (−5, 5) toward the King. His question about the King carries `fac_crown` and `release` on it forms; the other's does not. Mutation:
  delete the leave body → neither forms. Join arm (on T02 landed): a person in no faction who holds a told claim naming `fac_varfell`
  (so `oughts_named` offers it) and a positive stance toward Varfell's creed subject → `commit` to `fac_varfell` forms and executes, and
  `members(fac_varfell)` lists him; the same person with a negative stance → the filter removes it and no `commit` forms. Mutation: drop
  the filter → the second arm forms it.
  Realm reading: faction `commitment.made` / `commitment.ended`, seeds 0-2, base 0 / 0.
- **Control.** Against **T02 landed** (CP-T02-05 built, this item off): the filter and the leave body off reproduce that arm's hash;
  seeds 0-2 paired. The control's own reading is the number of computed faction `commit`s on rival creeds T02 alone produces.
- **Measure first, both halves.** IN-58 found that stance reaches formation only under `stance_polarity: declared` (`_part5:138`), and
  B-V's prefect read no negative `legitimacy` at its three placements (`_part7:122`). The join gate is the opposite risk: `opinion_of`'s
  pursuit term is a cosine against a faction's expected pursuits and needs no deed (`PQ:513-517`, `:532`), so it can pass at tick 0 for
  anyone whose pursuits fit a rival's template. One hash-equal reading at ticks 0-2 comes first: how many members read their own faction
  below 0, and how many (person, rival creed) pairs pass the join gate. If none read below 0, the leave body is not built; if the join gate
  passes for most of the cast at tick 0, the filter is too loose to build as written; either residue is recorded (REM-26's shape).
- **Hash · revert.** Mover · remove the filter and the body. **Size** M.

````

### CP-T09-05

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T09-05 | Land rewards the sworn: an occasion for a fief (land moves; keeping a follower waits on an IN-08 cell) | BUILD | M | CP-T08-08, CP-T09-01, CP-T09-04; IN-08, IN-40 | — | `cp-factions-war-diplomacy`:304-332 |
```

entry (`2026-10-23-subsystem-completion-09-factions-war-diplomacy.md:304-333`):

````
### CP-T09-05 · Land rewards the sworn: an occasion for a fief

- **Adds.** On a question about a person X who holds a live `oblige` to one of p's seats (`establishment_of`, `WQ:1868`), add the rungs p
  holds as **plain** referents — the shape IN-70's `opinion_referents` already uses to add plain referents to a formed question — so `give`
  + Rung (PR #496, `VT:571-592`, unclassed) forms on them. **The occasion is bounded; the recipient is not:** `give` fans `to` over every
  person the giver knows — *"the receiver is somebody known, never the referent"* (`VT:585`) — so X is one of the candidate receivers,
  not the only one. Binding `to` to the question's referent would be a new formation rule for one term (shape divergence), so it is not
  proposed; the bound is the stopping rule below.
- **What it buys, stated narrowly.** **Land moves to a follower.** `give` is celled, and the cells are null on six axes and −0.2 on
  `deontological_instrumental` (`RY:3192`, `:3238`, `:3278`, `:3335`, `:3376`, `:3429`, `:3487`), so a witnessed cession does not raise the
  grantee's regard of the giver: the "a granted man stays" arm fails by construction today. It becomes true only with a demand on v9
  IN-08's cell pass — a `deed:rung.ceded` cell pair, the shape IN-11 names for `deed:commitment.ended` (`VT:1039`) — which this item asks
  for and does not author. The bond that exists without it is the oath: the land lies under the liege's purview through it (IN-40); if the
  vassal defects, CP-T09-04 lets the liege's seat retake it by plurality.
- **Owner · Layer.** `WQ` (one term) · Layer 2.
- **Primitives.** P15 (the office slot whose holder is rewarded), P14 (the oath as the token), P11.
- **Reads / writes.** Reads `establishment_of`, live `hold`s. Writes `give`'s existing pair.
- **Joins.** T08 (GV): `give` + Rung as built; IN-08 (the `deed:rung.ceded` cell, demanded); T08's CP-T08-08 (the oath lapses unpaid
  otherwise).
- **Decision.** Whom to reward, and with what; the grantee's loyalty stays his own. Unwatched: lords hand land to their men; whether a
  grant keeps a follower longer waits on the IN-08 cell.
- **Shared-class cost, named.** Other unclassed rows may form on the added Rung referents, and `give` may name any known receiver;
  both counted. Stopping rule: any computed cession to a person holding no `oblige` to the giver's seat, or the realm's held territories
  falling against the base over two seasons with no rise in obligees' holdings → revert.
- **Falsifier.** Hand-built: a territory holder with a seat and a co-located obligee forms `give {subject: terr, to: obligee}`; executed,
  `rung.ceded` and the obligee holds it. Control: the same holder with no obligee forms no `give` on the rung. The reward arm, run only
  with the IN-08 cell authored: the grantee's `regard` of the giver after the cession exceeds it before; at today's cells it does not,
  and the item says so. Realm reading: `rung.ceded`, and cessions to non-obligees, seeds 0-2, base 0.
- **Hash · revert.** Mover · the term. **Size** S.

````

### CP-T09-02

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T09-02 | `declare`: a war has a producer, an occasion and a target set (the declaration is done on execution; the teeth only on an arrival) | BUILD | M | CP-T02-05 (landed `1ef8d273`, re-taken inside CR-28), CP-T09-01, CP-T09-04, CP-T09-05; A1, H-209, IN-08, IN-40 (landed or rows; the home names more ids after IN-40, none a position); not a dependency: ED-IN-0296 (does not wait on M1) | — | `cp-factions-war-diplomacy`:157-219 |
```

entry (`2026-10-23-subsystem-completion-09-factions-war-diplomacy.md:157-220`):

````
### CP-T09-02 · `declare`: a war has a producer, an occasion and a target set

- **Adds.** (a) **The `declare` row** as `FA §3.3` S2 designs it: a seat-holder `via` a seat granting `dispatch` (`march`'s and `raze`'s
  eligibility, `VT:1109`; but see §6 A1); subject the target faction's creed Proposition; stratum `binding_decision`, so the chronicle's
  kind filter carries `war.declared` to every living ledger (`es/epistemic.py:649-686`, per `T09 §2.1`); writes `(Proposition, exists)` —
  mood `WAR` (`FQ.WAR_MOOD`), subject the seat's faction creed, value the target — and `(Tenure, since)`, the declarer's own `commit`, so a
  war is never "of one" (FA-G03); refuses (`declare.refused`) a target that is his own faction or no rostered faction's Proposition;
  celled on the seven axes in IN-08's pass (IN-08 → every verb-adding position, `_part5:44`). The row declares **`referent_class:
  Proposition`**, so it forms only on Proposition-classed referents (an unclassed row forms on every plain referent, `RY:604-608`;
  `commit`'s 66/0 before REM-23, remediation part 02 `:381`). Its feeders are T02's `oughts_named` as CP-T09-01 filters it, and term (b).
  **`at_war` is edited, as `FA §3.3` S2 asks** (verbs-15 `:130`, `:159`; M1 `:580`): it counts only WAR Propositions whose creating
  Event's causing act is a `declare` (read through `state/attribution.py::causing_act`, the reader `EI:992` uses). Without it an `own`
  `utter` of mood WAR plus a `commit` (`FQ:234-238`; `at_war` needs a live commit, `FQ:250`) still makes a war that term (c) reads, and
  §6 A1 would be moot. The hand-built WAR chains in `es/tests/test_faction_q.py:220-260` are re-recorded to mint through `declare`.
  (b) **The grievance occasion**: a new `Proposition`-class stamper body on a question for which IN-70's `opinion_referents`
  (`WQ:2108-2161`) is non-empty — a **wound** p judges, by a doer of faction F that p regards below indifference — stamping F's creed.
  **A killing raises nothing yet:** a dead victim's claim is held and never asked about (H-209, `es/hole_register.yaml:4539-4545`;
  `WQ:2124-2125`), so no killing starts a war until H-209 closes (T03, T05 and T10 name the same hole). IN-72's tier 2 acts on wound
  (`body.changed`) and `contest.undecided` claims only.
  (c) **The war's target set, `at_war`'s first production reader** (M1): a `Rung`-class standing term for a holder of a seat granting
  `dispatch` or `issue` whose side in a live war W is `seat_faction(via)` when that faction is one of W's two sides, else `side_in(w, p,
  W)` (an ally, CP-T09-03) — one rule, consistent with `sides_of` and `occupying_faction`, which also key on the seat: the settlements the other side holds
  (`holder_faction_of`) inside that seat's purview (`es/state/gate.py:353` `purview_reaches`). `march` (classed `Rung` by REM-27) and the
  seat's self-warrant `issue` form on them, and `seize` then forms through `warrant_sourced` (`RY:1912`). War widens a seat's targets from
  the towns its ledger names (REM-27's `fields_named`) to every enemy town it reaches; when every committer has released W, the term
  withdraws. Nothing is refused (direction 8; "a march needs no war" stays true).
  (d) **Rallying**: on a question about a `war.declared` claim, stamp W for a person whose faction is one of W's two sides; `commit` to W
  forms (defenders too — `at_war` is symmetric).
- **Not built.** A world-tension or aggressive-expansion meter (`D_T09 #19`, `#53`: T-a); a phased play with a countdown (`also #1`:
  T-c); a casus-belli gate on `march` (direction 8). A coalition against an expander is several declarations on one public grievance.
- **Owner · Layer.** `VT` (the row), `es/loop/effects_information.py` (`_eff_declare`, `_eff_utter`'s one mint and `_eff_commit`'s opener
  in one write), `WQ` (three terms) · Layer 2. The new verb is checked against `architecture/VOCABULARY.md` at the build, `give`'s
  precedent (`VT:594`) [UNVERIFIED].
- **Primitives.** P06 (the price is a public deed and exposure, not a currency), P12 (war as one state on a ladder of one), P35 (MB
  resolves what forms), P27 (the declaration spreads through the chronicle).
- **Reads / writes.** Reads `opinion_referents`, `opinion_of`, `holder_faction_of`, `purview_reaches`, `at_war`, `side_in`. Writes
  `(Proposition, exists)`, `(Tenure, since)` — existing pairs (`utter`, `commit`).
- **Joins.** T04 (MB): the Rung stamper already carries REM-27's `fields_named`; this term sits beside it, deduped by REM-21 (iv-b), and
  MB fights what forms. T06 (information): `war.declared` is realm-public through the chronicle kind filter, live at HEAD
  (`es/epistemic.py:685-686`) — but its docstring schedules the filter's deletion in the change that builds the `<rung kind>` reach channel
  (`:675-684`), which is one of `ED-IN-0298`'s options; the publicity of a declaration depends on that channel being kept or replaced.
  T02: CP-T02-05 and IN-08's cells for `declare`; the hostile ranking depends on `stance_polarity` (ED-IN-0296's ask-then), which this item
  does not decide. **H-209** (a dead victim's claim raises no question) is a dependency for wars over killings.
- **Decision.** A marshal decides whether a grievance becomes a war; members decide whether to rally; seat-holders at war decide which
  enemy town to march on. Unwatched: a wounding across factions becomes a war (a killing too, once H-209 closes), the war offers every
  enemy town a seat reaches, and the declarer's own towns enter the enemy's set — the cost of declaring is becoming a target.
- **Shared-class cost, named.** `declare` and `commit` share the Proposition class: term (b)'s creed stamp lets `commit` form on the hated
  faction's creed, and CP-T09-01's filtered (favoured) creeds let `declare` form on a faction the declarer favours. Stopping rule: if any
  computed faction `commit` names a faction the committer reads below 0, or any computed `declare` names one the declarer reads at or above
  0, revert (b) and record the residue against REM-21's per-row `referent_source:` question (K4). A seat whose purview a won `recruit` of
  a seat-holder widened (IN-40's `oblige` clause, `es/state/gate.py:389-398`; CP-T09-07) reaches across factions, so term (c)'s target set
  grows with every sworn seat-holder: counted in the same reading.
- **Falsifier.** (1) Hand-built: a Hafenmark seat-holder with a `dispatch` grant who holds the firsthand claim of a Crown member
  **wounding** a Hafenmark man (`body.changed`, the `seen.who` pairing naming the Crown member) and reads `opinion_of(fac_crown) < 0` forms
  `declare` on `fac_crown`; executed, `at_war(fac_hafenmark, fac_crown)` is True and a person not co-located holds a `war.declared` claim
  at the next WITNESS. Control: a hand-built `utter` of mood WAR **plus** a `commit` leaves `at_war` False (the S2 edit). (2) With W live,
  a Crown `dispatch` seat forms `march` on a Hafenmark-held settlement its ledger never named; with every committer released, the same
  seat forms none. Mutation: delete term (c) → none. Realm reading: WAR Propositions, `war.declared`, `field.won` + `field.lost`, seeds
  0-2; base 0, 0, 0.
- **Control.** The formation count: with term (b) off, `declare` forms only on the filtered `oughts_named` creeds — that count, with
  `declare.refused`, is the arm term (b) is measured against (the row alone moves the hash, by its load and its formations, a declared
  mover of the verb-table pins); seeds 0-2 paired.
- **Hash · revert.** Mover · the row, the three terms and the `at_war` edit (re-records `es/tests/test_faction_q.py:220-260`). **Size** L.

````

### CP-T09-03

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T09-03 | Alliance and peace are acts on the war Proposition (done on a hand-built chain; computed only if `covenant` executes) | BUILD | M | CP-T09-02, IN-12 (landed `f9e4cef`) | — | `cp-factions-war-diplomacy`:221-253 |
```

entry (`2026-10-23-subsystem-completion-09-factions-war-diplomacy.md:221-254`):

````
### CP-T09-03 · Alliance and peace are acts on the war Proposition

- **Adds.** No content roster, one roster cell and one Query. (a) **`side_in(w, p, W)`** in `FQ`, beside `at_war`: p's faction if it is W's
  subject or value; else the faction of the seat that issued a dispensation p holds, is addressed by and whose `terms` is W — the issuing
  seat read through `state/attribution.py::causing_act`, the read `EI:992` `_issuing_seat` already makes (moved to one shared reader, not
  copied); else `None`. CP-T09-02 (c) reads it, so an ally fights on the side that invited him. (b) **Alliance**: a `covenant` whose subject
  is W — in the maker's reach through his own `commit` (`WQ:785-817`, limb 2) — addressed to a person of a third faction; acceptance is his
  `commit` to W through the existing `terms_sourced` route (`RY:1951`); he is then at war on the maker's side. (c) **Peace**: the same
  covenant addressed to a person on the other side; acceptance is his `release` of his own `commit` to W, formed by `terms_sourced` gaining
  `release: [dispensation]` (one roster cell). The offerer's own release is his own act; the war ends when no committer is left
  (`FQ:229-233`).
- **What binds.** Reception, by ruling: a peace broken by a new `declare` is a public deed judged at its cells, *"public, witnessed,
  priced by reception, and accepted by ruling"* (C-1, `VT:1044`). Nothing refuses it. Truce, tribute, dated terms and the pact chain are
  declined (GP-5b, GP-13).
- **Owner · Layer.** `FQ` (`side_in`), `RY: terms_sourced` (one cell) · Layer 2.
- **Primitives.** P12 (alliance and peace as states on the war), P14 (the instrument is the obligation token), P27.
- **Reads / writes.** Reads held dispensations, `causing_act`, the WAR Propositions. Writes nothing new; `covenant`, `commit` and `release`
  write their existing pairs.
- **Joins.** T08/GV: `covenant` as built (IN-12 step 7). T04: an ally marches with his own seat's army; M3's ally-in-`mustered` half is not
  built (a joint army would widen `occupying_faction`'s occupation too). CP-T09-08 delivers an instrument at a distance.
- **Decision.** Whom to invite, whom to offer peace, whether to accept. Unwatched: wars widen on invitation and end on sealed peace,
  every step a person's act.
- **Asymmetry.** `terms_sourced` is read person-side by `decision/options.py` (formation only; `T09 §2.6`); no getter of world state
  changes.
- **Falsifier.** (1) Hand-built: a Varfell seat-holder holding the Crown's covenant on W(Crown, Hafenmark) forms `commit` to W; afterwards
  CP-T09-02 (c) offers him Hafenmark-held towns in his purview. Control: without the instrument, neither. (2) A Hafenmark committer
  holding a Crown peace covenant on W forms `release` on W; executed, his edge closes, and with every committer released `at_war` is
  False. Mutation: drop the `release` cell → no release forms from the instrument. (3) **One instrument, two offers:** `terms_sourced`
  forms each listed verb on whatever the held writ's terms name (`RY:1960-1968`), so a peace covenant held by an enemy committer also
  offers him `commit` to W — an escalation, or a redundant second edge if he already holds one. Stated, not prevented; the arm records
  which forms (`release`, `commit`, or both) and how often each is chosen, and a `commit` chosen from a peace offer is counted in
  CP-T09-02's stopping reading.
- **Hash · revert.** Mover · the cell and the Query. **Size** M.

````

### CP-T09-07

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T09-07 | Service that serves: `retain` (uncapped arm only; the contested offer of service, renamed from `recruit`, which ED-IN-0306's army row holds: `-08` part 2), and the seat's obligees in its army (the one count of a seat's people at a place) | BUILD | M | CP-T01-06 (landed `60f32d138`), CP-T04-01 (landed `5de92100`), CP-T08-08, CP-T09-03, REM-27; H-213, IN-40, IN-70, JQ-4; not a dependency: CP-T04-04 (the two homes disagree whether they share `loop/sides.py`, T09 :383 against T04 :187, :450-451; re-derive at re-base; no file overlap means no edge) | — | `cp-factions-war-diplomacy`:359-396 |
```

entry (`2026-10-23-subsystem-completion-09-factions-war-diplomacy.md:359-397`):

````
### CP-T09-07 · Service that serves: `recruit`, and the seat's obligees in its army

- **Adds.** (a) **The `recruit` row** as `FA §3.3` S3: a seat-holder `via` a seat granting `confer` [S3's ASSUMPTION], `to` a known person;
  contested on the counterparty through the season's social roll, the obstacle read world-side at the fold — his live `oblige` or
  `commit` to a rival seat or faction, his `opinion_of` the recruiter's faction (IN-70), his regard of the recruiter. These terms are an
  **explicit demand on the obstacle's single owner, `modules/social_contest/roll.py::obstacle`** (T05's file `:389-390`); T05 has no
  `recruit` item and "M10" is verbs-15's name for this demand, not a T05 item (rulings R10). Won opens his `oblige` to the exercised seat
  with `oblige_term` (the edge, its upkeep and its lapse are built); Lost emits `recruit.declined`, a witnessed refusal. Opening an edge
  the counterparty owns has its precedent: `determine`'s disposal opens an `oblige` owned by the party it binds (C-1, RULED A, `VT:1044`).
  (b) **Obligees march**: `es/loop/sides.py:115`'s claimants become `mustered(origin, faction)` ∪ the exercised seat's obligees present
  in the origin's subtree (`establishment_of(via)`), and `es/state/gate.py:865` `may_muster` admits a moved man holding a live `oblige`
  to `via` as well as one committed to its faction. Retainers fight (`D_T09 #15`); a vassal's oath yields men (`#2`).
- **B-V, declared.** Under `build_realm(guards=True)` the guard cohorts' `oblige` to the throne and duchy seats (`_part5:152`) puts
  cohorts in those seats' armies — a weight-carrying army that JQ-4's weight → troop value then prices. Read on that arm only (default
  OFF).
- **Owner · Layer.** `VT` (the row), its effect beside `_eff_oblige` in `es/loop/effects_governance.py:420` (the `oblige` opener, with the
  literal `Tenure(..., "oblige")` that `data/verbs.py`'s opener walk reads), `es/loop/sides.py`, `es/state/gate.py` · Layer 2.
- **Primitives.** P14, P20 (upkeep and lapse, built), P18 (a seat's retinue), P23 (the contest).
- **Reads / writes.** Reads ties, `opinion_of`, regard, `establishment_of`. Writes `(Tenure, since)` and `Tenure.term` on `oblige`
  (existing); (b) writes nothing.
- **Joins.** **T05 (SC):** the obstacle terms above, added at `roll.py::obstacle`, and a `contests:` prize on the season roll whose Won
  band opens the counterparty's edge. **T01:** at the shipped ceiling (default 2 = ceiling 2, `es/data/fixtures.py:416-419`;
  `modules/social_contest/roll.py:89-113`) an added obstacle term is clipped, so falsifier (1) runs on H-213's uncapped arm, whose owner is
  T01's CP-T01-06 (rulings R2). **T04 (MB):** none demanded — this item owns the `sides_of` claimant edit and `may_muster`'s clause; it
  merges with T04's CP-T04-01 (one subunit per person on a side: each obligee becomes his own subunit) and CP-T04-04 (the field fought a
  round later, which edits the same `es/loop/sides.py`), batch order to be set by the batch. **T08:** CP-T08-08 (a retinue lapses unpaid
  without it).
- **Decision.** Whom to bring into service, whom to pay, whom to take to the field. Unwatched: seats compete for men, poach from rivals,
  and lose retinues they do not pay.
- **Asymmetry.** `may_muster` and `sides_of` are getters; the openers of `oblige` (`oblige`, `determine`'s disposal, B-V's guard build)
  are untouched — grep the `oblige` opener list (`data/verbs.py` `_OPENERS_FROM_EFFECTS`) before the edit.
- **Falsifier.** (1) S3's, on H-213's uncapped arm: a seeded `recruit` of an unattached known person opens his `oblige` on Won; over seeds
  0-9, a person with a live `oblige` to a rival seat is declined more often (control: the tie removed). A won `recruit` of a seat-holder
  also widens the recruiter's purview over that seat's ground (IN-40, `es/state/gate.py:389-398`), feeding CP-T09-02 (c) and CP-T09-04
  (d) across factions — counted in their stopping readings. If the degree distribution does not move with the tie, the
  obstacle is not reading him. (2) A hand-built settlement march whose marcher's seat has one obligee, not a faction member, at home:
  the army is one larger than base. Mutation: drop the union → base.
- **Hash · revert.** Mover · the row; the union and the gate clause. **Size** L.

````

### CR-09

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-09 | `own_purview` and the oblige clause agree: route `queries/world_q.py::own_purview` through `state/gate.py::purview_reaches` (H-101); `faction_q.purview` has no game caller and is left | BUILD | M | CP-T09-07 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:47-58`):

````
### CR-09 — `own_purview` and the oblige clause agree (IN/FA) · BATCH B10-17 · STATE BUILD (hash mover) · R R-04
- WHAT: IN-40 closed the main hole, but `queries/world_q.py::own_purview` (limb 4 of `reach`) does not call `state/gate.py::purview_reaches`, so the set form misses the oblige clause where a seat-holder has sworn an `oblige` and the swearer's ground lies outside the sworn seat's own ground (H-101). Route `own_purview` through `purview_reaches` (or one shared clause walk). `faction_q.purview` has no game caller, so routing it changes nothing and it is left.
- LANDED ALREADY: IN-40's predicate in `state/gate.py`.
- REMAINING UNBUILT: the set-form agreement.
- GATE: B10-17's entry. It serialises with CP-T09-07, which also edits `queries/world_q.py`.
- EXIT and FALSIFIER: a hand-built world as `test_in40_oblige_purview.py` builds, where a swearer's ground lies outside the sworn seat's own ground: for the holder's seat, `rung in own_purview(w, holder)` agrees with `purview_reaches(w, seat, rung)`, and a claim about that ground enters `reach`. Control: the same world before the routing, where the claim is not admitted. (`purview(w, seat)` is `faction_q.purview`, which CR-09 leaves alone; `own_purview` takes a Person.)
- HASH MOVERS: declared. `own_purview` feeds `reach`, `attention_key` tier 1 and `larders_in_purview`, so it moves question formation, and it imports the clause's recorded unbounded over-reach (measure both).
- HOLES AND LEDGER IDS: H-101.
- ASKS ATTACHED: none.
- RE-BASE: re-read `own_purview` and `purview_reaches` by symbol.
- SOURCE: the hole-row pass, lane 3 and critic A.

````

### CP-T09-09

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T09-09 | `conspire`: a plot with backers (measure first; cut if no `legitimacy` reads below 0); its occasion gains a second named consumer, the deposition's motive (CR-37); if it is cut, that motive needs another Proposition producer | MEASURE first, then BUILD (cut if no `legitimacy` reads below 0) | M | CP-T01-06 (landed `60f32d138`), CP-T09-01, CP-T09-07, CP-T09-08, IN-12 (landed `f9e4cef`); H-213, IN-57 | — | `cp-factions-war-diplomacy`:431-454 |
```

entry (`2026-10-23-subsystem-completion-09-factions-war-diplomacy.md:431-455`):

````
### CP-T09-09 · `conspire`: a plot with backers

- **Adds.** `FA §3.3` S7: any person (`own`), `to` an invitee. The first `conspire` with no plot held mints an OUGHT plot Proposition
  (subject the target seat's holder, predicate naming the seat) and the plotter's `commit`; a later one on a held plot is contested on the
  invitee (obstacle terms — his live `oblige` or `commit` to the target seat or its faction, his regard of the target — demanded of
  `roll.py::obstacle`, as CP-T09-07's; falsifiers on H-213's uncapped arm, T01's CP-T01-06); Won opens his `commit`
  to the plot, Lost emits `plot.refused` and leaves him a claim against the plotter (he may `petition`, or `arrest` from a seat). **The
  reader (M7) is already built:** a `commit` to an OUGHT is an ambition (`WQ:1946`) and an ambition's referent is tier 0 (IN-57), so every
  conspirator attends to the target first, and the hostile acts already on the table (`fight`, `challenge`, `petition`, `arrest`) form on
  him. The first act's occasion: a question about a seat-holder H for whom p's own `legitimacy(p, H)` (`PQ:452`) is below 0.
- **Owner · Layer.** `VT` (the row), its effect, `WQ` (the first act's term) · Layer 2.
- **Primitives.** P13 without a breach counter (exposure is witnessing; `conceal`, IN-12 step 10, does not hide `who` from those present,
  overview §6 #6), P27, P23.
- **Reads / writes.** Reads ties, regard, `legitimacy`. Writes `(Proposition, exists)`, `(Tenure, since)`.
- **Joins.** T05 (SC): the obstacle terms at `roll.py::obstacle`, as CP-T09-07. T01: the uncapped ceiling arm. T06 (FI): discovery by `surveil` / `interview`. T03 (PC): a coup's execution is a `fight`. T08
  (GV): `arrest` (PR #496).
- **Decision.** Whom to plot against, whom to invite, whether to join or denounce. Unwatched: plots gather among the discontented, and a
  refusal turns into a denunciation.
- **Measure first.** As CP-T09-01: B-V's foreign prefect read no negative `legitimacy` at three placements (`_part7:122`); one reading
  over the realm's persons toward seat-holders at ticks 0-2 first.
- **Falsifier.** S7's: a `conspire` on a held plot opens the invitee's edge on Won only; over seeds an invitee with a live `oblige` to the
  target seat refuses more often. The reader: a conspirator's first question each round is about the target where a non-conspirator's
  is not.
- **Hash · revert.** Mover · the row and the term. **Size** L.

````

### CP-T09-06

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T09-06 | The Crown's own ducal seat can be refilled (data only): `off_duke_valorsmark` `conferral: inheritance`, replacing `appointed`, and `successions` gains `off_duke_valorsmark: off_heir`, so it passes with the line through IN-61's one-act claim; if that write does not execute, `appointed` stands; `off_duchess_hafenmark` stays null `[ASSUMPTION; medium; Jordan to correct; revert: appointed]` | EDIT (data) | M | IN-61 (landed `f9e4cef`); IN-53 | — | `cp-factions-war-diplomacy`:334-357 |
```

entry (`2026-10-23-subsystem-completion-09-factions-war-diplomacy.md:334-358`):

````
### CP-T09-06 · The Crown's own ducal seat can be refilled (data only)

- **Adds.** `es/offices.yaml`: `off_duke_valorsmark` (the King's second seat: post Duke, rung the Crown duchy, faction Crown, `revocation:
  null`, `offices.yaml:196-204`), `conferral: null` → `appointed` [ASSUMPTION; medium; Jordan to correct]. A vacant Valorsmark then enters
  the `vacancies` of a seat with `confer` and purview over the Crown duchy (IN-53, `WQ:2164`) — the realm seat — so the Widow Regent or a
  crowned heir appoints a Crown duke. It sits in the hereditary set the file's translation left null as "a JUDGMENT CALL flagged for
  attack" (`offices.yaml:43-44`), and IN-61 keeps it out of the `successions` registry — *"not inherited with the throne"*
  (`_part5:159`, LIMITS) — so without a basis it is empty for good; `appointed` is that limit's answer, and IN-61's throne is untouched.
- **Not done, and why.** `off_duchess_hafenmark` stays null: `appointed` would let the Crown's realm seat appoint a rival faction's head,
  and the row's own note says the seat is *"unreachable by the Crown specifically — a real consequence of the ruling, not smoothed over"*
  (`offices.yaml:219`; no duchy is in anyone's holdings as built, `:83-84`). Its route is `elected` by its own body, which waits on the
  unruled "which act fills an `elected` seat" (`RY:2289-2303`, ED-IN-0256 (2)); a residue, not an ask. The `off_npc_084` row is IN-61's
  content decision (rulings R4): it is rungless (`offices.yaml:125-126`), a rung of `None` is reached by no seat's purview, and a row
  here would be inert. The precedent claim the first draft made from Jordan's 2026-10-12 revocation is withdrawn: that note sits on the
  Hafenmark and Varfell rows (`offices.yaml:215`, `:228`), not on Valorsmark's.
- **Owner · Layer.** `es/offices.yaml` (content) · Layer 2. No code: `may_fill` admits every rostered basis today (`es/state/gate.py:675-697`).
- **Primitives.** P30 without lineage (the seat passes by an act, not by blood), P15.
- **Joins.** T08 (GV): `confer`, `vacancies`, `may_fill` unchanged. IN-61's gate edit (`may_fill` refusing `inheritance`) does not touch
  `appointed`.
- **Decision.** The realm seat chooses whom to appoint. Unwatched: the Crown's duchy, emptied by the King's death, is refilled instead of
  staying empty.
- **Falsifier.** Seed 0, tick 1, the King dead: the Widow Regent's `vacancies` lists `off_duke_valorsmark`, and her `confer` on a known
  person executes. Control: `null` → absent. Realm reading: seats still vacant at tick 2, seeds 0-2, base 8 / 6 / 10 (`T09:451`).
- **Hash · revert.** Mover · `null` again, or the `annex`-by-land reading cut in §3. **Size** S.

````

### CR-32

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-32 | Standing ladders as posts on seats (H-181's producer): `offices.yaml` gains `ladders:` (names and order only), `World._grant_remit` stamps the seat's `post`, `_term_marks` shows a post only where its ladder's Livery cell names a visible mark, and `rank` compares within one scale only | BUILD (data + reader) | M | CR-30 (landed `e03c7129`), CP-T09-06 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:136-148`):

````
### CR-32 — Standing ladders as posts on seats; `marks` shows a visible post; `rank` reads one scale (H-181's producer) (IN/FA) · BATCH B10-17 (close two, first: … → CP-T09-06 (close one) → CR-32 → CR-35 → CR-36 → CR-37 → IN-48) · STATE BUILD (data + reader) · R R-07 (contributor), R-04 (contributor)
- WHAT: item 1, Standing rank taken at step 5: a Standing rank is a post on a seat, read off the grant, never a Person field; livery shows in `marks` only where the archived ladder names a visible mark; `rank` compares within one scale only. Jordan's "about 60 ranks" reads 82 rank rows, 81 of them named, 59 on the eight-ladder subset.
- LANDED ALREADY: `offices.yaml: titles:`; `World._grant_remit` stamping `remit_acts` and `seat_rung` on the `hold` grant (H-71 arm 2); `rank_gain` (dormant, H-178); `rung_kinds`.
- REMAINING UNBUILT: (1) `engine/season/offices.yaml` gains `ladders:` beside `titles:`: per ladder its faction (a `factions` member), an ordered list of post names (rank 0 first; rank 0 is membership, a live `commit`, never a post) and whether the ladder's archived Livery cell names a visible mark; the nine ladders on live organisations (Crown, Hafenmark, Varfell, Church, Löwenritter, Riskbreaker, Inquisitor, Templar, Guild; 66 named posts), the Warden ladder only if its organisation is a `factions` member, Niflhel's not transcribed (dissolved); names and order only, transcribed from `faction_politics_v30.md` (archived), never its gates, Obs or Renown thresholds; authored seats mapped where a post matches; no seat minted for an unheld rank. (2) `World._grant_remit` stamps the seat's `post` on the `hold` grant beside `remit_acts` and `seat_rung`, so a person reads his own standing with no `World` (AX-2). (3) `epistemic.py::_term_marks` returns CR-30's heritage plus the sorted posts of the actor's live ladder-post and title holds, a ladder post only where that ladder's Livery cell names a visible mark: the Riskbreaker and Warden ladders show nothing (`faction_politics_v30.md:416`, `:422-428`, `:636`). (4) `decision/options.py::rank(p, teller)` compares within one scale only: the sign of the teller's ordinal minus p's own on a ladder both stand on (read from p's newest `seen` claim naming the teller and from p's own grants), else the title ordinal in `rung_kinds`, never across the two, else 0. `01_AXIOMS.md:1596` ("a title's rank is its domain's ordinal and that needs no second scale") stands untouched, because ladder posts are not titles. Not built: the Initiation Gates and Demotion columns (a conferrer's decision and a revocation basis).
- GATE: B10-17's second close (the batch is cut into two closes at its open, as B10-09 is: close one the T09 rows as ordered, close two CR-32, CR-35, CR-36 and CR-37, which need CP-T09-06). NEEDS: CR-30 (B10-10, landed `e03c7129`: `_term_marks`), CP-T09-06 (shares `offices.yaml`).
- EXIT and FALSIFIER: a co-located witness of an act by the holder of a Church-ladder post holds `marks` containing that post; a witness of `off_riskbreaker_covert`'s holder holds no Riskbreaker post in `marks`; a hearer at rank 2 on the Church ladder, told by a teller he has seen at rank 6, reads `rank == +1`; a teller seen only on the Varfell ladder, with no title, reads 0; a hearer who has never seen the teller reads 0; a ladder post and a title never compare. Planted failure: the ordinal difference reversed reddens the +1 assertion. CONTROL: an empty `ladders:` map reproduces the prior tree's hash, and `rank` reads 0 for every pair.
- HASH MOVERS: declared MOVER (every `seen` claim about a holder of a post whose ladder shows livery carries new marks; `rank_gain` wakes, H-178). Port: the `post` stamp is an untyped key in `Tenure.payload` (CONVENTION grade, `seat_rung`'s precedent), which the Godot payload types.
- HOLES AND LEDGER IDS: H-181 (`hole_register.yaml:4103-4124`) re-graded `absent` → `assumption` at this position, its producer; H-178 (its `rank_gain` wakes); H-71.
- ASKS ATTACHED: item 1 (`-05` §1b) `[ASSUMPTION; medium; Jordan to correct; revert: an empty ladders: map, one re-pin]`. The ladder transcription and the seat-to-post mapping are content (`-05` §1a's content list).
- RE-BASE: re-read `_grant_remit` and CR-30's landed `_term_marks` by symbol; recount the ladders and posts from the archived file at build.
- BUILDER: `CLAUDE.md` §10's second tier; the ladder transcription and the seat mapping to a third-tier (judgment) verify pass.
- SOURCE: `04_CODE_ARCHITECTURE.md:322-351`; `01_AXIOMS.md:1595-1621`; HR H-181, H-178.

````

### CR-35

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-35 | An elected seat is filled by its faction's bench, and the contested succession (H-217 closes here): the `election` gate arm, the `_disposal` `hold` literal, `judging_set`'s electorate, the `election` and `succession` rows at `disposal: declared`, CR-34's tally (landed `67f118dd`) with the seat as predicate, and `FILLED_BY`'s elected narrowing `[ASSUMPTION; medium; Jordan to correct; revert: no rows]` | BUILD (H-L0-8 applied in PR #507: the gate arm and the H-217 clause build in the ordinary way; the rows' shipped state is whatever this position's falsifier and control say) | M | IN-61 (landed `f9e4cef`), CP-T02-02 (landed `f9e4cef`), CR-34 (landed `67f118dd`), CP-T09-06 | `-05` §1a (b), confirmed at the default (ED-IN-0301) | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:214-226`):

````
### CR-35 — An elected seat is filled by its faction's bench; the contested succession; H-217 closes (IN/SC/FA) · BATCH B10-17 (close two: CP-T09-06 (close one) → CR-32 → CR-35 → CR-36 → CR-37 → IN-48) · STATE BUILD (its gate arm and H-217 clause: H-L0-8 applied in PR #507) · R R-04 (conjunct (1): `confer` at risk, `determine`)
- WHAT: item 3 (widen succession and revocation), taken: an elected seat is filled by its faction's bench through `determine`, never `confer` (`01_AXIOMS.md:1681`: "an election is `determine`, not `confer`"; `04_CODE_ARCHITECTURE.md:326`), and a contested succession by the throne's bench. H-217's `succession` row, the `_disposal` `hold` literal, the determination clause, the contested-succession falsifier arms and the tripwire move here from IN-61; H-217 closes at this position's commit. It sits in B10-17, not B10-13, because B10-17 already serialises `offices.yaml` and `state/gate.py`, and in B10-13 it would sit before SC-02's `reception` re-source and force a re-record.
- LANDED ALREADY: `may_determine` (`state/gate.py:752-806`) and `may_fill` (`:675-695`); `judging_set` with an unwired `matter` parameter (`queries/world_q.py:492-502`); the docket's petition key (`DOCKET_PETITION`, K-55); by this batch's open, IN-61's `FILLED_BY` with its first narrowing, `REVOCATION_DISPOSAL["inheritance"]` and the claim write (B10-09), and CR-34's tally (landed `67f118dd`).
- REMAINING UNBUILT: (1) **The gate arm**, `election`, in `state/gate.py::tenure_write_basis`'s determination clause: opening a `hold` whose object is a seat S other than `via` is admitted iff S has no live `hold` (one per object), `FILLED_BY[S.conferral]` contains the determination's election arm, `seat_faction(via) == S.faction`, and, for an `elected` S, the candidate holds a LIVE `commit` Tenure to `faction_prop_id(S.faction)` (`may_muster`'s shape: `state/gate.py` may not import `queries/world_q.faction_holding`, `gate.py:292-296`), a candidate holding a live commit to a second faction Proposition being refused; for an `inheritance` S (the contested succession) the party's faction clause is dropped, so a claimant of any faction may be judged (Baralta's claim, RS-23's contest). (2) `loop/effects_information.py::_disposal` gains the literal `Tenure(tid, party, S, "hold", since=w.tick, degree=degree)` (moved here from IN-61; a literal, so `data/verbs.py::_derive_openers_from_effects` reads it). (3) `queries/world_q.py::judging_set` wires its `matter` parameter for a row disposing `hold`: the electorate is the live seats whose faction is S's and whose grant carries `determine`, S excluded; no containment walk (containment at the seat's rung would seat the King and the Widow Regent on every election; a rungless member such as the guild leader would sit on none). (4) `engine/season/arrangements.yaml` gains `election` and `succession` (`disposal: declared`, `quorum: 1` swept {1, 2}, `bench_basis: determine`, `disposes: hold`, `venue_min_rank: hearth`, the other keys as `council_of_state`'s) `[ASSUMPTION; medium; Jordan to correct; revert: no rows]`, seeded at `declared` directly (no row is seeded at `bench` and flipped later). (5) The seat is the docketed petition's `terms` (`DOCKET_PETITION`); no ninth operand, no payload key. (6) Contest polarity: a hold-disposing row rolls against the provider's `obstacle_default` with `opposition` None (`modules/social_contest/roll.py:103`), keyed on the row's existing `disposes:` value, so no fourteenth key `[ASSUMPTION; medium; Jordan to correct; revert: party-as-opponent on every row]`; party-as-opponent stays for Record rows. (7) The vote is CR-34's tally with the hold-disposing predicate test: an elector's commit counts only if it is to an OUGHT whose subject is the candidate and whose predicate names the vacant seat in the docketed petition's terms `[ASSUMPTION; medium; Jordan to correct; revert: any Proposition about the party]`. (8) **`FILLED_BY`'s elected narrowing** (ladder step 3 on `01_AXIOMS.md:1681` and `04:326`): `elected` maps to the election arm only (a `confer` of an elected seat refuses) and `inheritance` gains the election arm. It is measured on the post-item tree (`python -m engine.season.harness.aperture 3 s`, s = 0-2, the `confer` row's `ex` against the pre-item tree): the narrowing removes the Widow Regent's main vacancy candidates (`off_npc_052`, `off_npc_082`, both elected), and the one seed-0 `confer` recorded on 2026-10-13 was onto `off_npc_082` (`hole_register.yaml:4515`, `:4523`). If seed-0 `confer ex` falls to 0, the elected narrowing waits until an election executes, and `elected` keeps CONFERRAL until then. (9) H-217 closes here: the `conferral_bases` note's open question (`rosters.yaml:2307-2310`) is rewritten, and the tripwire `test_arrangements.py::test_a_hold_disposing_row_is_reported_by_c1_until_determine_can_open_a_hold` goes red the day the site exists and is re-recorded in this commit. CONTENT CONSEQUENCES (stated, not filled): the Holy See's electorate by this rule is the Cardinal of Justice and the Senior Inquisitor (only their remits carry `determine`, `offices.yaml:381`, `:394`, `:407`, `:420`, `:434`), so three of the four Cardinals do not vote and canon's "the Cardinals elect" (`offices.yaml:375`) is met in part; the Commune Representative (`off_npc_081`) and the Restoration Leader have no electorate, so each stays vacant once vacated.
- GATE: B10-17's second close (see CR-32). NEEDS: IN-61 (B10-09: `FILLED_BY`, `REVOCATION_DISPOSAL["inheritance"]`, the claim), CP-T02-02 (B10-09: realm seat ids equal row ids), CR-34 (landed `67f118dd`: the tally), CP-T09-06 (shares `rosters.yaml`). The gate arm and its H-217 clause rest on hunk H-L0-8 (`architecture/meta/04_CODE_ARCHITECTURE.md` §C.2, the determination's election arm, worded to cover both arms: "for a party S's faction admits, or, for a seat whose conferral basis is inheritance, any claimant"; `held-back-layer0-hunks.md`), applied in PR #507, so CR-35 builds the arm and the `election` and `succession` rows in the ordinary way. The elected narrowing is on B10-20's freeze row as a declared post-freeze mover if it waits on an election executing.
- EXIT and FALSIFIER (hand-built, real fold): the Confessor's seat vacated; a Church candidate's petition naming it docketed under `election`; the Cardinal of Justice holding a live commit to an OUGHT whose subject is the candidate and whose predicate names `off_confessor` `determine`s Success → the candidate holds `off_confessor`; (i-b) no elector committed → `determine.refused` (the tally); (i-c) the elector committed only to a plot OUGHT against the candidate → refused; (ii) the King as judge → refused at the gate (faction clause); (iii) a non-Church candidate → refused; (iv) a held seat → refused (one per object); (v) a candidate holding a live commit to a second faction Proposition → refused; (vi) once the elected narrowing ships, the King's `confer` of the vacant Confessor seat → refused (`FILLED_BY`). Contested succession (the arms moved from IN-61): a rival's petition naming the vacant throne, docketed under `succession` and determined Success by the Widow Regent → the rival holds the throne; the same with a live throne-hold → refused; with the heir's claim executed first → the determination declines (one per object). Mutation: drop the faction clause and (ii) goes red. CONTROL: the `election` row absent reproduces the pre-item hash on `build_realm(0)` at one and two seasons; `aperture 3 s` `confer ex` equal to the pre-item tree while the elected narrowing is unshipped. REACH: a computed `open_case` writes `DOCKET_ARRANGEMENT` and `DOCKET_PETITION` as None (`queries/world_q.py:213-219`, citing H-80/§F1), so no computed docket item names `election` or `succession` and none carries the seat: CR-35 lands as a hand-built mechanism, and its realm reading (`aperture 3 s`, s = 0-2, the `determine` row plus the count of `matter.determined` receipts opening a seat-`hold`, base 0) is a named residue whose owner is H-80.
- HASH MOVERS: EQUAL in the realm while no computed docket item names `election` or `succession` (REACH above); a declared MOVER where an election executes and where the elected narrowing moves `confer` formation (`vacancies` stops offering `elected` seats to `confer`-holders).
- HOLES AND LEDGER IDS: H-217 (`hole_register.yaml:4645`, `:4653`; closes here); H-80 (realm reach); RS-23; K-55.
- ASKS ATTACHED: item 3 (`-05` §1b): `FILLED_BY` taken at step 3 (`01_AXIOMS.md:1681`, `04:326`), the elected arm at step 3 then 4 then 5 `[ASSUMPTION; medium; Jordan to correct; revert: delete the rows, the arm and the wiring; elected seats fall back to confer; re-pin where an election executed]`, plus the three assumptions above. `-05` §1a question (b), the Cardinal electorate (keep the rule, or author an electors list, AX-6's alternative and content), is confirmed at the default (ED-IN-0301) and blocks nothing: the rule ships. H-L0-8 (question (d)) is applied in PR #507.
- RE-BASE: re-read `tenure_write_basis`, `_disposal`, `judging_set` and IN-61's landed `FILLED_BY` by symbol. Read the electorates off `build_realm(0)` at build: two electors for the Confessor, two for Varfell and none for the Commune Representative or the Restoration Leader are [UNVERIFIED] (not run), and many seats read `faction: null` in `offices.yaml`.
- BUILDER: `CLAUDE.md` §10's third tier (judgment): a gate arm.
- SOURCE: HR H-217; `queries/world_q.py:492-502` (`judging_set`'s `matter`), `:201-204`; `state/gate.py:752-806` (`may_determine`), `:675-695` (`may_fill`); `offices.yaml:370-375`, `:227-232`; RS-23 (`v9_p8:336`).

````

### CR-36

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-36 | Nominate-then-confirm: a fourth way to fill a seat, the `nominated` basis; `_eff_determine` mints a `resolution` Record under a `disposes: Record` row, and a `confer` of a `nominated` seat needs the confirming actor to hold one naming the seat and the conferee; `off_parliamentary_clerk` `appointed` → `nominated` `[ASSUMPTION; medium; Jordan to correct; revert: appointed]` | BUILD | M (at build: the clerk's basis) | IN-61 (landed `f9e4cef`), CR-35 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:227-239`):

````
### CR-36 — Nominate-then-confirm: a fourth way to fill a seat, `nominated` (IN/SC) · BATCH B10-17 (close two, after CR-35, before CR-37) · STATE BUILD · R R-04 (conjunct (1): `confer`, `determine`)
- WHAT: item 3, nomination taken (it survived all five steps, delegated): a seat may be filled by a body's nomination and a second seat's confirmation. A bench nominates by `determine` under `parliamentary_debate`, which mints a `resolution` Record; the confirming seat `confer`s only on a held resolution naming the seat and the nominee. `off_parliamentary_clerk`, the one `Ministries` seat, is the first `nominated` seat (agreeing with CR-41, landed `acb954dde`).
- LANDED ALREADY: `_eff_determine` (it declines a Record disposal today); `_mint_document`, the one mint; `warrant_sourced`'s form (`rosters.yaml:1920-1926`); the creating-Act provenance `_eff_arrest` reads (`gate.py:828-831`).
- REMAINING UNBUILT: `rosters.yaml: conferral_bases` gains `nominated` (`open: false` admits it because this is the design change its note requires, `rosters.yaml:2300-2301`); `record_kinds` gains `resolution: [terms, to]`. `state/gate.py`: `FILLED_BY["nominated"]` = the conferral basis; `REVOCATION_DISPOSAL["nominated"] = ban`, as `appointed` (a confirmed nominee is an appointee) `[ASSUMPTION; medium; Jordan to correct; revert: None]`. `loop/effects_information.py::_eff_determine` gains the Record disposal site: under a `disposes: Record` row (`parliamentary_debate`) at Overwhelming or Success it mints, through `_mint_document`, a `resolution` whose `terms` is the docketed petition's `terms` (the seat) and whose `to` is `[party]` (the nominee), held by the determining actor (ED-IN-0292 (1), RULED NO, bars minting a newborn Record's hold to anyone else). `loop/predicates.py::_req_confer` (declined again in `_eff_confer`): the **confirming actor HOLDS** a live `resolution` naming the seat and the conferee, minted through a seat other than the conferring `via` (`warrant_sourced`'s form; the provenance read off the Record's creating Act). Delivery to the confirmer is a `give`; until a computed `give` carries it (H-229's residue) the route is hand-built. The alternative, stated and not taken: drop the warrant precedent and declare a world read of an unheld document, in tension with AX-7. `offices.yaml: off_parliamentary_clerk` `appointed` → `nominated` `[ASSUMPTION; medium; Jordan to correct; revert: appointed]`. The nominating bench is today's `judging_set` for `parliamentary_debate` (at a realm venue the King and the Widow Regent: the interim two-seat bench, CR-38). The nomination's contest sign (party-as-opponent on a Record row) is a named limit. No Layer 1 text changes: `01_AXIOMS.md:1681` makes the conferral vocabulary content, and the filling act is `confer`, already listed at `04_CODE_ARCHITECTURE.md:326`.
- GATE: B10-17's second close, after CR-35. NEEDS: IN-61 (`FILLED_BY` and `REVOCATION_DISPOSAL`, which it extends), CR-35 (shares `state/gate.py` and `rosters.yaml`).
- EXIT and FALSIFIER (hand-built, real fold): the clerk's seat vacant; the Widow Regent `determine`s Success on a nominee under `parliamentary_debate` → a `resolution` naming the seat and him, held by her; after a hand-built `give` the King, holding it, `confer`s the seat on him → executes; (ii) on another person → `confer.refused`; (iii) with no resolution held by the confirmer → refused; (iv) the King nominating and confirming, both through `off_king` → refused (two-seat clause); (v) a `determine` Failure mints nothing. Mutation: drop the two-seat clause and (iv) goes red. CONTROL: the clerk's basis left `appointed` reproduces the pre-item build hash and the `aperture 3 s` `confer` and `determine` rows.
- HASH MOVERS: declared MOVER at build (`off_parliamentary_clerk`'s value; the `Office` repr folds `conferral`).
- HOLES AND LEDGER IDS: H-90 (its `cite:`, `hole_register.yaml:1126`); H-229 (the `give` residue); ED-IN-0292 (1).
- ASKS ATTACHED: item 3 (`-05` §1b) `[ASSUMPTION; medium; Jordan to correct; revert: the clerk back to appointed; drop nominated, the kind and the site, one commit and a re-pin at build]`, plus the two assumptions above. [UNVERIFIED: whether a minted Record's creating Act is readable for every Record; read from `may_warrant`'s docstring only, not traced into `_mint_document`.]
- RE-BASE: re-read `_eff_determine`, `_req_confer`, `_mint_document` and CR-35's landed `FILLED_BY` edits by symbol.
- BUILDER: `CLAUDE.md` §10's third tier (judgment): a fold predicate and a new disposal site.
- SOURCE: `proposals/2026-09-03-governance-corpus-rebuild/annex-a-decomposition.md:1187` (F-10.03); `worldbuilding_v30.md:180`, `worldbuilding_v30_infill.md:55` (intent); `engine/season/arrangements.yaml:123-136`; H-90's `cite:`.

````

### CR-37

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-37 | The throne may be stripped by the Holy See's concurrence with a carried motion (`joint_concurrence`; the Confessor's `revoke` on a held `resolution`); the deposed King keeps `off_duke_valorsmark`; `depose` CLOSED `[ASSUMPTION; medium; Jordan to correct; revert: off_king null, depose PARKED]`; a seat whose `revocation:` names `joint_concurrence` takes the same route (no route special to `off_king`) | BUILD (H-L0-9 applied in PR #507) | M | CR-36, IN-61 (landed `f9e4cef`) | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:240-252`):

````
### CR-37 — The throne may be stripped by the Holy See's concurrence with a carried motion (`joint_concurrence`); `depose` closed (IN/FA) · BATCH B10-17 (close two, after CR-36, before IN-48) · STATE BUILD (H-L0-9 applied in PR #507) · R R-04 (conjunct (1): `revoke`, hand-built reading unchanged)
- WHAT: item 3, deposition: M8 is corrected by Jordan's 2026-10-26 request (step 1: his words select the form M8's own revert names, a third `revocation_bases` value for the throne), with the shape at step 3 (`04_CODE_ARCHITECTURE.md:327`). Deposition is two persons' acts: the Parliamentary vote (a `determine` under `parliamentary_debate` with the monarch as party; party-as-opponent stays, because the monarch really resists) and the Holy See's concurrence, which is an act (the Confessor's own `revoke` through his seat; refusing is not acting). `depose` is CLOSED, answered by this `revoke`; ARC-40's "be replaced" arm (`engine/season/ENDINGS_CLASSIFIED.yaml:180`) gains its non-violent route.
- LANDED ALREADY: `REVOCATION_RULES` and `check_revocation_disposal` (`gate.py:599`, `:602-614`); `may_warrant`'s split between the gate and the Record read (`gate.py:828-831`); by this batch, CR-36's `resolution` kind and IN-61's `REVOCATION_DISPOSAL["inheritance"]: None`.
- REMAINING UNBUILT: `rosters.yaml: revocation_bases` gains `joint_concurrence`, plus a closed roster `concurring_bodies: [Holy See]` (canon's concurring body, data); `state/gate.py::REVOCATION_RULES` gains its rule: the revoking seat (`via`) belongs to a body named in `concurring_bodies`; `loop/predicates.py::_req_revoke` and `_eff_revoke` gain the record conjunct (the gate reads no Record): the **revoking actor HOLDS** a live `resolution` whose `terms` is the seat and whose `to` names the seat's current holder, minted through a seat other than `via`; `offices.yaml: off_king.revocation` null → `joint_concurrence` `[ASSUMPTION; medium; Jordan to correct; revert: off_king null, depose PARKED]`. No ban opens (`REVOCATION_DISPOSAL["inheritance"]` is None); the throne is then vacant and goes by IN-61's claim or CR-35's contested route. The revocation strips the throne only: **the deposed King keeps `off_duke_valorsmark` until his death or his release.** The motive: the Royal Deposition conjunction supplies the motive only: its conjuncts (ii) (the Holy See's standing) and (v) (the monarch deemed unfit) are each concurrer's occasion (his own `legitimacy(p, King)` below a band, CP-T09-09's occasion, one owner), never a gate; (i), (iii) and (iv) are not carried (the Imperial Court is a rostered `office_bodies` member with zero seats, `rosters.yaml:1744`, `:1783`, so (iii) is unreachable until a seat is authored in it; a further `concurring_bodies` member or a heads-of-factions member set is the data extension and the revert). The board-game conjunction ("PI ≥ 5 + Church Mandate ≥ 5 + Crown Mandate ≤ 1 + 2 Standing tokens") is not a precondition. The sources disagree: PP-194's institutions block names the Holy See AND the Imperial Court (`params_tables.yaml:6619`); world canon names the Parliamentary vote and the Holy See (`worldbuilding_v30_infill.md:58`); the world text is taken. A seat whose `revocation:` names `joint_concurrence` takes the same route (no route special to `off_king`; the arc fold of 2026-11-05, ED-IN-0346: the throne's row is content, a data row on one seat, never a by-name outcome).
- GATE: B10-17's second close, after CR-36; rests on hunk H-L0-9 (`01_AXIOMS.md:1257`, T-o's "who" cell gaining a seat the revoked seat's declared basis names; `held-back-layer0-hunks.md`), applied in PR #507; `04:327` stands as written, because one seat revokes. NEEDS: CR-36 (the `resolution` kind), IN-61 (`REVOCATION_DISPOSAL["inheritance"]: None`; the heir's claim after).
- EXIT and FALSIFIER (hand-built, real fold): a carried motion (a `resolution` naming `off_king` and the King, held by the Confessor after a hand-built `give`) and the Confessor's `revoke` through his seat → the throne-hold closes, no ban opens, the King's `off_duke_valorsmark` hold stays live, and the heir's `succeed` claim then executes (IN-61); (ii) the same `revoke` with no resolution held → `revoke.refused`; (iii) a resolution present and a non-Holy-See seat revoking → refused at the gate; (iv) the resolution naming a former King → refused (holder clause); (v) a resolution minted through `off_confessor` itself → refused (two-seat clause). Mutation: drop the body clause and (iii) goes red. CONTROL: `off_king` back to null reproduces the pre-item hash. REACH: no computed route: `revoke` under `joint_concurrence` has none until an operand channel names the arrangement and the petition (H-80/§F1); R-04 conjunct (1)'s `revoke` stays on H-207 (A)'s hand-built reading. Whether the Confessor forms `revoke` on the throne in computed play is moot while H-80 holds.
- HASH MOVERS: declared MOVER at build (`off_king`'s value; hashed `w.offices`).
- HOLES AND LEDGER IDS: H-207 (disposition unchanged: this adds a hand-built route on the throne only, and the Church seats' null revocation, which a same-ladder basis could answer, is not decided); H-80; PP-194.
- ASKS ATTACHED: M8 corrected (`-05` §1 M8) `[ASSUMPTION; medium; Jordan to correct; revert: off_king back to null; drop the value, the roster and the rule; depose PARKED with M8's trigger]`. The motive rests on CP-T09-09's occasion: if CP-T09-09 is cut (no `legitimacy` reads below 0), the deposition's motive needs another Proposition producer. H-L0-9 (`-05` §1a question (d), confirmed at the default, ED-IN-0301) is applied in PR #507.
- RE-BASE: re-read `REVOCATION_RULES`, `_req_revoke`, `_eff_revoke` and CR-36's landed `resolution` kind by symbol; read the applied wording of H-L0-9 in `01_AXIOMS.md` at B10-17's open.
- BUILDER: `CLAUDE.md` §10's third tier (judgment).
- SOURCE: `worldbuilding_v30_infill.md:58`, `worldbuilding_v30.md:190-199` (intent); the Royal Deposition conjunction at `proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:628`, Jordan's ruling at `:616-619`; `04_CODE_ARCHITECTURE.md:327`, `:334-336`; `state/gate.py:599`, `:602-614`.

````

### IN-36

card row (`valoria_master_workplan_v11_part3.md`):

```
| IN-36 | FORCE-FOREIGN: an external empire and Schoenland as persons; the march frequency answered in kind (ED-IN-0317) | `foreign` ON by default since ED-IN-0310 (Jordan, 2026-11-04); BUILD: the interim march cap, one march per season into each territory (ED-IN-0317), a declared mover, first in this batch; HELD (the casus-belli rule moved to CR-91, B10-17b): Schoenland as persons, perception channels at the border, the three `field.unopposed` arrivals; BUILD: the `guards` flip ON after CP-T09-07 (b), a declared mover (ED-IN-0317: ships ON once CP-T09-07 (b)'s union lands, its own declared mover in B10-17; `[ASSUMPTION; medium; Jordan to correct; revert: guards stays off]`) · LANDED-NARROWED (landed at B-V `7c59d74c`; the rest in its `-04` part 2 entry) | M (the cap) | — | — | carried in full: `-04` part 2 |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:140-153`):

````
### IN-36 — FORCE-FOREIGN: an external empire and Schoenland as persons (IN; FA, MB) · BATCH B10-17 · STATE LANDED-NARROWED (landed at B-V `7c59d74c`); BUILD the interim march cap (ED-IN-0317, a declared mover, first in B10-17); HELD for its other residues (Schoenland as persons, perception channels, the three `field.unopposed` arrivals; the casus-belli carrier moved to CR-91, B10-17b) · R —
- WHAT: what remains after the landing: Schoenland as persons (factor placed, no head, no template); perception channels at the border (not built; CR-29's reach channel, released from M11, is the plan's route); `stance: -1` toward the Crown head's seat (inert, H-233); the march FREQUENCY (H-233), ANSWERED IN KIND by Jordan, 2026-11-04 (ED-IN-0317; below); and a Katepano march on the capital that arrives `field.unopposed`.
- LANDED ALREADY: `7c59d74c` (B-V, closed `b1eabf5d`, PR #498; remainder PR #499). Altonia a faction (`names_index.yaml`); `rosters.yaml: foreign_cast`; two seats (`offices.yaml: foreign_seats`); three goal rows; IN-60's guard cohorts (`cohorts.yaml: guards`). Landed behind `build_realm(foreign=, guards=)`, both default OFF [ASSUMPTION; medium; Jordan to correct]; no harness flag turns either on. Hashes: `build_realm(0)` `d3edd90a` unchanged, `foreign=True` `36e59a16` (re-recorded when Katepano's goal retargeted to Valorsplatz, `goal_katepano_press_the_capital`, `set_s_001`), `guards=True` `73ecca60`. Natural-play half MET AT WITNESS SEEDS 39 and 53 only (the real unrestricted chooser picks the march on the first goal-question scene; the fold reaches `mass_battle.field_input`, ends `field.lost`; `test_in36_foreign.py`); first released scene tick 0 in 7 of 80 seeds.
- REMAINING UNBUILT: perception channels at the border (the trade-demand clause waits on them: FA-01, ED-IN-0298, H-234); Schoenland as persons; the march FREQUENCY half, in two parts, by Jordan's ruling of 2026-11-04 (ED-IN-0317; verbatim: *"march can only happen if there is a casus belli ie claim to a territory...unless civil war breaks out. anyway, for testing purposes, once a season per territory cap."*): **(a) the interim test cap, BUILD in B10-17 (first):** at most one march per season (one `w.tick`) INTO each territory, counting a march on a settlement against the territory that contains it, uniform for every marcher, civil-war marches included, behind a plain integer fixture (name chosen at build; shipped 1; 0 or unset = no cap) `[ASSUMPTION; medium; Jordan to correct; revert: no cap]`, superseded by (b) once (b) is built. Seam: a typed `requires` conjunct on `march`'s row (a new stem in `data/requires.py` reading the season's admitted marches into the target's territory), refused on the row's existing refusal channel (`emits_on_refusal: ["march.refused"]`) and read by the one admission path (`loop/resolve.py::_admits`, eligibility then `requires`) like every other conjunct; not a `march` branch inside `_admits` (special-casing a verb, `CLAUDE.md` §0). It edits `verb_table.yaml`, so it joins the verb cluster and serialises (P13). Its fixture needs a `hole_register.yaml` row with a `site:` (`test_season_shape.py::test_w9_check3_every_fixture_read_resolves_to_a_register_site`). **(b) the standing casus-belli rule, MOVED to CR-91 (B10-17b; the arc fold of 2026-11-05, ED-IN-0346: the carrier is a claim Proposition on a ground, `-04` CR-91; the text below stays as the ruling's record):** a march needs a claim to the target territory held by the marcher, his faction or his office; the exception is civil war (a rising: side R in the strife instrument's terms, a marcher whose faction governs nothing up the target's chain); the foreign nations' marches (side O) need a claim to the territory they march on like anyone else; a marcher's own held territory is claimed by its `hold`. No carrier for "a claim to a territory" exists in the plan or the code: the `Tenure` kinds (`rosters.yaml: tenure_kinds`: hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban) name none; `succession.claimed` (CL) is a claim to a SEAT; `faction_q.at_war` reads live `commit`s to a two-faction WAR Proposition and names no territory; `hole_register.yaml` H-175 ("a hostile-presence claim, a standing casus belli, a border dispute) is a live design choice ... this row does not invent one") invents none; CP-T09-02's home builds a war's Proposition and a target set (term (c): the other side's settlements in the seat's purview) and states "a march needs no war", listing "a casus-belli gate on `march`" as not built (direction 8), which this ruling supersedes. `[GAP: carrier — the claim to a territory; candidate: a Proposition on the WAR / creed shape (subject the territory, value the claimant faction, held by `commit` edges, so a claim ends when its committers release it and nothing is stored, ED-IN-0225), produced by CP-T09-02's `declare` or an `utter`; owner CP-T09-02, decided at B10-17's re-base (V1)]`; the gate on `march` is built only once the carrier exists; a Katepano march forming at seeds 16, 38, 44 arrives `field.unopposed` in a full season (the King's `t_hold_terr_T1` gone by round-0 ENCOUNTER; traced at seed 16, cause unverified); flipping `foreign` or `guards` ON is its own declared hash mover (realm hashes and 1-/2-season pins re-recorded).
- WHAT REMAINS HELD (the story-telling fold of 2026-11-02, ED-IN-0311; amended by ED-IN-0317): Schoenland as persons; perception channels at the border (CR-29's reach channel is the route); the cause of the three `field.unopposed` arrivals. The casus-belli carrier (above) is no longer held here: it moved to CR-91 (B10-17b). The frequency is no longer held: ED-IN-0317 answers it in kind.
- GATE: DEPS IN-36 -> FA-01's content and trade demand (D, content landed); guard content -> IN-60 `d32d7931`, IN-59 (b) `590f753a`. EDITS none further. Coupling: IN-38's NPC-089 overlay names `faction: Altonia`, so reverting IN-36 reverts that file first (`corpus_run.CAST` is read at import).
- EXIT and FALSIFIER: natural-play half as above (witness seeds). The cap (ED-IN-0317): a planted second march into one territory in one season is refused on `march.refused` while the first is admitted, hand-built; MUTATION: the cap at 0 lets both through; CONTROL: the cap off reproduces the base hash. The casus-belli rule: its exit is CR-91's (`-04`). v9 states no separate FALSIFIER line for the remainder beyond `test_in36_foreign.py` and the hash controls (`foreign` off reproduces the realm hash).
- TRIGGER (hole-row pass): nothing flips `guards` ON before CP-T09-07 (b)'s union lands; then IN-36's own flip does (ED-IN-0317, below); the trigger was M1's answer on H-233 (the natural-play march frequency), now answered in kind by ED-IN-0317 (the cap builds; the casus-belli rule waits on its carrier). After the decision round M1 is NARROWED and this is its residue, confirmed at the default (ED-IN-0301; `-05`: where the frequency of a foreign march in natural play comes from, and whether `build_realm` ships `foreign` and `guards` on): IN-36 stays HELD, FORCE-FOREIGN's driver stays off, and CL-THRUST's B5.2 waits with it. IN-36's `foreign`/`guards` default is on GO-15's freeze list. **ED-IN-0310 (Jordan, 2026-11-04) flipped `foreign` to ON by default; `guards` stayed off.** **`guards` is then TAKEN by the ladder (ED-IN-0317):** step 4, ED-IN-0310's `foreign` ON and the standing "Gains are improvements and therefore ship"; step 5, before CP-T09-07 (b)'s union lands the flip musters nobody (the guard cohorts hold an `oblige` and no `commit`), so it lands directly after that union in B10-17, as its own declared mover (P14, its pre-change reading CP-T09-07's recorded after-reading; goldens re-recorded and said so) `[ASSUMPTION; medium; Jordan to correct; revert: guards stays off]`. What it does (verified): `build_realm(guards=True)` seats `cohorts.yaml: guards` (the King's at 4, two dukes' at 2) sworn to their seats (`harness/populated.py::seat_guards`), so `guard_weight` (IN-60) reads above 0 where a principal is present and IN-59 (b)'s `audience` limb closes `move` and `migrate` into a guarded rung to those without audience; `march` carries no `audience` conjunct, so foreign and civil-war marches are not gated by it. EXIT: `guard_weight` above 0 at the King's rung at seed 0; the strife guard, guards on against off at `strife 4 0 1 2` (P10's strife exception), closes no terminal route (KL, DR, XE) and concentrates no ending, else the flip is not made (P8); CONTROL: `guards=False` reproduces the pre-flip hash. CL-THRUST's B5.2, held on this flip, is released when it lands. The freeze list's `foreign` entry is answered, and the pinned slices moved with it (`test_season_weather.BASE_HASHES`, `test_go07_canonical_digest.BASE`).
- HASH MOVERS: flipping `foreign` or `guards` ON is a declared mover; at the shipped OFF, `build_realm(0)` is unchanged (`d3edd90a`). The cap (ED-IN-0317) is a declared mover in B10-17: its pre-change `build_realm(0)` reading is B10-16's close reading @sha (P14), every seeded golden it moves re-recorded, old to new, and said so.
- HOLES AND LEDGER IDS: H-233, H-234, ED-IN-0298; FA-01, IN-60, IN-59, IN-38, IN-13. SOURCE #457 `:145-155`.
- ASKS ATTACHED: none for the frequency (answered in kind, ED-IN-0317; whether a march is chosen at all stays the chooser's, from convictions and IN-08 `alignment` cells, which are content); ED-IN-0298 via FA-01.
- RE-BASE: B-V (#498/#499) is the landing; v9's entry is written after it. B-Y (#502) added `guard_weight` Query (IN-60/IN-59, A-28). None found since. CR-71 (reading @5d6aac5, `aperture 2 0` and `strife 2 0`, seed 0, `PYTHONHASHSEED=0`, REALM): OW reads 0: no side-O `march.declared` occurs in two seasons (the FR, WN and OW signatures: A 2, R 11, O 0; S1r read side-O marches at four seasons, `-11` §1). WA and WR read 0: `field.won` and `field.lost` are never emitted. The declared marches, their refusals and the `field.unopposed` ones are counted at H-149's cite; whose marches the `field.unopposed` ones are is this entry's open question, not read.
- SOURCE: `v9_p5:87-91`; state-index row `v9.md:261`.

````

