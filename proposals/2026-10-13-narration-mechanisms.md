# Narrative prose mechanisms for the season loop — proposal v2

## Status: PROPOSED — reference under CLAUDE.md §0.05; one seed, two seasons throughout; supersedes an earlier draft ("v1") that was never committed

Date: 2026-10-13

> **SCOPE, STATED LOUDLY.** This document is **reference and a proposal** (CLAUDE.md §0.05): it resolves nothing at runtime, and if it were deleted the game would behave identically. It creates **no plan position**, allocates **no ID** and writes **no ledger row**. **Merging the PR that carries it does NOT ratify anything in it**, notwithstanding the merge-ratifies default (ED-1094): the four decisions in section 7 are **held back** for Jordan, and every work package (W0–W9) is held back until it is built in code, at its owner, with a test that executes it. Grade: paper.

This document specifies the work that would let `engine/season/` be told as prose, and the decisions that work needs. It is reference: it builds nothing, decides nothing, and every figure in it is a reading of one seeded run of two seasons, not a balance claim.

Conventions. "S" is the scratchpad of the session that wrote this, `/tmp/claude-0/-home-user-ttrpg/8db7fd8c-53d4-5022-b81f-62a5d0959706/scratchpad/`. **S is not in the repository and does not persist.** Nothing this document places in S was committed: the measurement scripts and outputs (`storybar*`, `chains*`, `inventory`, `d12`, `measure_ma*`, `spread_out.txt`), the five reviews, the reconciliation notes and v1. A figure tagged [MEASURED] below was reproduced by an S artifact on the tree and seed named in section 10; from this tree alone it can be re-derived only by writing and running the measurement again, and W0(d) is the work package that repeats them on a second seed. A citation into S is a record of where the reading came from, not a path a reader can open. Evidence tags are [MEASURED] (an artifact in S reproduces it), [READ] (a file was opened at the line given), [PRECEDENT] (the tree decided this shape elsewhere) and [INFERRED] (reasoning, not observed). [WRITER: …] marks a connection the writer of v2 made; [EXTENSION] marks work no review or source proposed in that form. [CHECKED: …] records a citation the writer of v2 opened. Finding ids (L-n, A-n, E-n, P-n, NERS) refer to the five reviews in S; section 9 disposes of every one. The v1 document is `S/narration_mechanisms_recommendations.md`; its ids (C1–C15, M-A..M-C, D1–D5) are retired here and mapped in section 4.

**What changed from v1**
- The first obstacle is candidate formation, not record content.
- The render starts now, on today's substrate, as an instrument.
- Two products replace one: an omniscient instrument chronicle and a person-bounded journal.
- An act's subject is read with `subject_of`, not `anchor_of`.
- Candidate typing is a named, measured dispute rather than an omission.
- Content arrives as a new record kind on the `own_ledger` route; utterance binding is deferred.
- `Receipt.before/after` is conformance to §B.9, and appraisal is already live, so two decision rows close.
- The per-season deck emitter is refused; five planned objects are deleted.

## 0. Summary

**Verdict.** Narration of the season loop can begin now, as an instrument read over today's log. The first obstacle is not record content but candidate formation: it spends 439 of 1,318 acts (33.3%) on a subject that exists as another kind [MEASURED `measure_ma2_out.txt:2`; one seed, two seasons]. Content reaches no second person until a handover verb works, and that verb is held back by the same typing defect.

**The work, in dependency order.** W0 corrected instruments and the outstanding measurements. W1 a render v0: the instrument chronicle on today's substrate. W2 the candidate-typing disposition, as a measured arm in the owning verb batches. W3 IN-50, already scheduled in B-I. W4 a content-bearing record kind with a working handover. W5 the focalized journal. W6 the fragment bake. W7 scale lines. W8 the occasion ladder (existing carriers first, boot-time rows second). W9 conformance items, chiefly `Receipt.before/after`.

**Refused.** Anything that makes the world produce a beat because a story needs one: need-triggered injection, scripted beats, and the per-season authored-occasion emitter that would carry them. The grounds are argued on the five properties (section 3.4), not deferred to a ruling.

**Jordan's decisions.** (1) The candidate-typing disposition: refusals as learning, or declined at formation. (2) Authored occasions, already open as forcing-churn §7 decision 3. (3) The focalized journal as a new §A.2 module row (a declared amendment). (4) The narrowed wording of ED-IN-0225. Five v1 decision rows close or merge without him (section 7).

## 1. Evidence

**Verdict.** The measurements support four claims: half the refusals are verbs aimed at a subject of the wrong kind; the content to be told is thin but not absent (tellings carry it); the sim already owns occasion, attention and appraisal; and the shipped storybar understated cross-person causation. Every figure is seed 0, two seasons, tree `e6b706d`, `PYTHONHASHSEED=0`. None is sized for a decision without that caveat.

### 1.1 Measurements (corrected)

| Figure | Artifact | Tag |
|---|---|---|
| 1,318 acts; 389 executed; 929 refused, blocked or null (70.5%) under the orchestrator's suffix definition. The tree's owner of "refusal" is `REFUSAL_KINDS` (`data/verbs.py:1073`); the suffix list also counts `contest.undecided` (3) and `news.untold` (25), which the critics read as degree bands (`verb_table.yaml:548,959`) [CHECKED: holds, with a qualification — `contest.undecided` is `fight`'s Untouched degree; `news.untold` is `tell`'s Failure degree and also the refusal kind keyed `hearer` for an absent hearer (`verb_table.yaml:948`), so it is both]. The count under `REFUSAL_KINDS` is not yet measured (W0) | `storybar2_out.txt:4-6`; `measure_ma_out.txt:1`; `inventory_out.txt:26,47` | [MEASURED]; definition [READ] |
| Shipped storybar: cross 125 (9.5%), own 181, world 71, none 941 (71.4%); arms `off off` equal | `storybar_out.txt:6,12` | [MEASURED] |
| Occasion-restored reading: cross 314 (23.8%), own 568, world 292, none 144 (10.9%); 804 occasion edges restored; depth `{1:1004, 2:148, 3:96, 4:42, 5:17, 6:8, 7:3}`, 166 acts (12.6%) at depth ≥3, max 7. Executed acts read the same both ways | `storybar2_out.txt:1,10-13` | [MEASURED] |
| 460 of 929 refusals (49.5%) carry an `exists:<T> = 0` observation. Control: 0 of 250 observations on executed Events (a weak control: an executed act passed its existence check by construction, L-12) | `measure_ma_out.txt:2,20` | [MEASURED] |
| Of those 460, 439 (95.4%) chose a subject that exists as another kind (Rung, Site, Person/Rung, a `text` Record, …); 21 (4.6%) chose a subject in no store at the end of the run. So 439 of 1,318 acts (33.3%) are kind-mismatched attempts. Several "nowhere" ids look like persons who died (`p_npc_020`, `p_npc_052`, `p_npc_082`); not verified | `measure_ma2_out.txt:2,5-20,22-39` | [MEASURED]; the dead-person reading [INFERRED] |
| Refusal reasons: `observed-all-true` 191, `no-observation` 105 (together 296, 31.9%, with no failed conjunct); in-world reasons `path` 111, `not-present` 13, `claim-not-held` 13, `outside-purview` 9; `stores` 22, `with` 5 | `measure_ma_out.txt:5-18` | [MEASURED] |
| Verbs whose every attempt was refused: `migrate` 79 (all `path`), `commit` 74, `work` 67, `build` 33, `found` 29, `give` 24, `determine` 7, `confer` 4, `revoke` 4, `levy` 3 | `measure_ma_out.txt:23-55` | [MEASURED] |
| Acts with an effect beyond an existence flag: about 48 (`move` 23, `restore` 12, `accept` 5, `release` 3, `transfer` 2, `fight` 2, `convene` 1) | `measure_ma_out.txt:23-55` | [MEASURED] |
| 52 of 52 act-minted Propositions have predicate `''`, value `None`, mood OUGHT | `measure_ma_out.txt:57` | [MEASURED] (v1 flagged this as unsupported; now supported) |
| 120 Records: 112 `text`, every one with `subject_matter` None; 8 content-bearing (`petition` 3, `faction_sheet` 4, `dispensation` 1) | `measure_ma_out.txt:60` | [MEASURED] |
| Nonzero pursuits per person (n = 80): 0 → 37, 1 → 14, 2 → 29. The 37 are seated cohorts, pursuit-less by design (`harness/populated.py:391-398`) | `measure_ma_out.txt:62` | [MEASURED]; design reading [READ] |
| 19,970 Events, 17,746 bookkeeping; `condition.worn` 644 (all MATTER, no act); every StateChange `set` with `delta` None | `inventory_out.txt:1-4,60-71` | [MEASURED] |
| Tellings already carry content: `news.told` 11; `tell` payloads carry a `Said` (`predicate='record.created'`, told at Partial; `predicate='migrate.refused'`, `news.untold` at Failure) | `inventory_out.txt:33`; `chains4_out.txt:218-221,236-239` [CHECKED: holds] | [MEASURED] |
| 11,929 claims; 1,270 `told_by`, of which 4 arrived by a telling (a non-empty `chain`) and 1,266 by public-record channels | `d12_out.txt:2,14-16` | [MEASURED] |
| 803 deliberations; 19.45 questions available on average; aggregation `first` takes one; 686 took a `claim_landed`, 51 a `need`, 66 none | `d12_out.txt:4` | [MEASURED] |
| "801 of 1,068 deliberations share the leading source" is from 89 corpus baselines, not seed 0, and is not comparable with the 803 above | `queries/world_q.py:1489-1490` (code comment) | [READ] |
| Appraisal is live in the sim: `judged_gain` and `told_valence_gain` ship at 0.5 and `stance_gain` at 1.0 (Jordan 2026-10-09, "Gains are improvements and therefore ship"); `said_slant` (`newest`) and stance polarity (`legacy`) ship at control. Under `uniform` alignment every deed cell is 1.0, so valence is constant across deeds, not zero | `data/fixtures.py:694-733`; `data/verbs.py:1271-1281` | [READ] |
| Conviction spread: 3.81 effective axes of 7; four directions carry 94.5% | `spread_out.txt` (a table, not a run) | no tag in the sources |

D12's instrument checks held (9,729 of 9,729 raised and 426 of 426 acted question subjects resolve to recorded claims, `d12_out.txt:9-10`). Its caveat stands: it reads only the question's `about`, so a claim in the 12-claim View may sway scoring without being counted.

### 1.2 Retractions and corrections (v1 and earlier)

Each is stated once and propagated through this document; section 8.7 records how.

1. **"Content is the first obstacle"** — retracted as an ordering. The render can start on executed acts, tellings that carry `Said`, and refusals with in-world reasons; content reaches no second person without a handover the chooser cannot reach (L-4, P-1).
2. **"71% of acts have no antecedent; cross-person share 9.5%"** — retracted (already in v1). It was an IN-50 artifact; restored, "none" is 10.9% and cross-person 23.8%.
3. **"Persons hold 1-3 pursuits"** — false: 0, 1 or 2, with 37 of 80 at zero.
4. **"52 of 52 empty predicates has no artifact"** and **"M-A is not measured"** — both superseded by `measure_ma_out.txt`; v1's [INFERRED] tags on wrong-kind targeting flip to [MEASURED], narrowed by the elsewhere/nowhere split.
5. **"About what (`anchor_of`)"** — false for acts: `anchor_of` returns the actor for any act-caused Event (`state/attribution.py:112-114`) (L-1).
6. **"`uniform` zeroes appraisal" and "only non-control arms consume appraisal"** — false and stale (L-7, E-7).
7. **"C5 depends on C1" and "C7 depends on C3"** — false edges: `deed_valence` reads only the predicate kind; C7's depth term bypassed IN-50 (L-4).
8. **"A `text` record with no operands refuses to form"** — false; `said` is not a `requires_operands` member, and the real decline is the `own_ledger` conjunct (L-5).
9. **"`Receipt` has no pre-value field; adding one is Jordan's"** — wrong way round: 04 §B.9:425 specifies `before, after`; the code is the non-conformant party (A-4).
10. **"The deck is lawful as a MATTER/CALENDAR emitter"** — false: the write matrix admits Record and Proposition existence only at RES, class ACTS, and F.31 reads its roster once at boot (A-1, P-8).
11. **"`canonical_for` resolves names"** — wrong owner: it resolves terms (A-10).
12. **"The fragment file is what §0.05 clause 1 requires"** — misapplied: only a harness reader would read it (A-5).
13. **"`Scene.occasion.about` is enough for a legible why"** — narrowed: honest for the actor only; arbitrary under `first`; misattributed under `all` and `one_per_source` (L-11, E-2).
14. **"Nothing flows from the render back into the world"** — true only while no player reads it (E-1).
15. **"The focalizer is one of P-03's four chroniclers"** — no chronicler exists under `engine/` (L-3).
16. **"Ten record-existence writes carry keyed `subject_matter`"** — eight do (`measure_ma_out.txt:60`). [WRITER: v1 counted `case.opened` 2 among them; whether those two are among the 112 `text` records was not checked.]
17. **v1's four citation mismatches** stand as v1 footnoted them; none is relied on here except where noted.

## 2. What the work is for, and the two products

**Verdict.** The work produces two texts that must not be merged. An **instrument chronicle** is omniscient, lives in `harness/`, and is read by designers and spectators after the fact. A **focalized journal** is bounded by one person's beliefs and is the only text a player may read before choosing. All five reviews reach this split independently.

### 2.1 The two products

| | Instrument chronicle | Focalized journal |
|---|---|---|
| Reader | Designers, test readers, spectators; after the fact | The focalizer: the player's person, or any NPC's journal on demand |
| May read | `w.log`, `w.acts`, `driver.act_of`, `driver.scenes`, ledgers, per-season snapshots. Lawful for an instrument: precedents `soak.py:140,153`, `storybar.py:190`, `populated.py:1336` (A-3, A-D(a)) [READ by the critic] | The focalizer's own `PersonInterior`: their Claims, each claim's `seen` struct, and their own Scenes. No `World` parameter (04 §C.11:860) [READ] |
| May print `who` | Always | Only where the focalizer is the actor, or the channel that deposited the claim supplied `who` |
| May print `why` | The occasion claim, labelled as the instrument's reading | Only where the focalizer is the actor. "NO CHANNEL SUPPLIES `why`" (`rosters.yaml:948-963`) [READ]; `_term_why` returns `None` "as a scope decision" (`epistemic.py:765-776`, per NERS) |
| Labelled | As an instrument, on every output | As the focalizer's account |
| Home | `harness/chronicle.py` (IN-37) | A `person_q` function, the §C.11 `explain` shape; its shell is `port/`. No §A.2 row exists for it: a declared amendment (section 7, item 3) |
| Built in | W1 | W5 |

What each channel supplies (`supplied_by`, `rosters.yaml:948-963`, verified by the orchestrator):

| Channel | Supplies |
|---|---|
| `co_located` | stratum, marks, who |
| `witness_key` | stratum, who |
| `document_key` | nothing |
| `post_remit` | stratum |
| `chronicle` | stratum |

The journal's `who` and `why` rules are read from this table at runtime, not copied. A literal copy of `[stratum, marks, who, why]` duplicates `rosters.yaml:955` and fails the roster check (P-D) [READ by the critic].

### 2.2 Why they must not be merged

1. **Player coupling (E-1).** The single-player hook passes the callback a View, and "what a callback closes over is the client's own" (`harness/play_surface.py:14-19,47-51`) [CHECKED: holds]. A merged render read before choosing is salience-ranked memory reaching one seat's choices, the actor `architecture/meta/07_DYNAMICS.md:184-186` refuses. Concealment and falsity would do nothing against the player, that seat would differ from every other, and the IN-37 hash test would hold only while no player is attached. PC-06's ratified intent is that a client reads a per-person projection and the season renders "not as a feed of fact" (`proposals/2026-09-30-character-and-play-surface/03_play_surface.md:76-77,81`, per E-1).
2. **Hidden actors (04 §C.11:860-872).** `explain` has no `World` parameter and may not walk `causes[] → acts → Act.actor`, the attribution T-d forbids; "hidden actors are hidden in their EXISTENCE", which is what makes investigation worth a scene [READ by the orchestrator].
3. **Leaked knowledge (P-2).** 144 `date.scheduled` claims arrived through public-record channels and carry only the stratum (`d12_out.txt:20`). A merged render would print the convener's name and motive to every one of those holders.

The archived design admitted the coupling openly ("light allocation is outcome-RELEVANT", with a blind-control fixture), and v1 dropped that admission (E-1, citing `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:201-202,264-275`). This proposal restores it as a control (W5).

[WRITER: `skills/prose-writer/SKILL.md:158` says the player's vantage "is genuinely omniscient", which conflicts with PC-06's per-person projection. This proposal follows PC-06 for the journal and confines omniscience to the instrument chronicle; the skill line would need the same narrowing if W5 is adopted.]

### 2.3 Chroniclers, including a diegetic one [EXTENSION]

No chronicler exists in `engine/season/` (L-3, NERS; "chronicler" returns no hits under `engine/`). v2 therefore focalizes through sim persons' ledgers only. Three later options remain open (D-M):

| Option | What it is | Cost | Source |
|---|---|---|---|
| (a) Lexicon | A chronicler's voice applied to a person-focalized selection | No new object | NERS watchlist, MEDIUM |
| (b) Diegetic chronicler | A person whom the public-record `chronicle` channel admits (`rosters.yaml:399,404,918`; S-2 allows it), focalized by W5; their W4 record is a retellable artifact others can read through `research`. P-03's partiality comes from the channels they hold | No new object beyond W4 and W5 | E-E, P-F |
| (c) Engine change | Chroniclers become persons with ledgers | New persons; hashes move | L-3 |

No option is recommended yet. [WRITER: (b) composes on W4 and W5 and adds no object of its own, so it is the cheapest to test once both exist; it also gives a stale `faction_sheet` held by a chronicler a reader, which is faction-scale staleness without a new carrier (P-F, D-L).]

## 3. Architecture

**Verdict.** Four parts, with dependence running one way. The sim produces occurrences and beliefs. The instrument reads everything and writes nothing. The journal reads one person's interior. Authored fragments sit beside their reader and take their key space from `data/`. Nothing flows from either text back into the world except through a player who reads it, and W5 carries the control for that path.

### 3.1 The four parts

| Part | Home | Reads | Writes | What v2 would add there |
|---|---|---|---|---|
| Sim | `engine/season/` (Layer 2) | its own stores | Events, Claims, `Scene.occasion`, `Act.via`, Tenures, Records | At most: W2's typing clause (if adopted), W4's record kind, W9's `Receipt.before/after`. Never text, never salience |
| Instrument chronicle | `harness/chronicle.py` (IN-37) | `w.log`, `w.acts`, `driver.act_of`, `driver.scenes`, ledgers, W0's snapshots | nothing | W1, W7 |
| Focalized journal | a `person_q` function; shell in `port/` | the focalizer's `PersonInterior` only | nothing | W5 (and a new §A.2 row) |
| Authored fragments | a file beside `harness/chronicle.py` | — | — | W6 |

Harness modules are excluded from the model scans (`test_season_shape.py:642-643`, per A-3), and dependence from `harness/` runs one way (`harness/__init__.py:6-7`, per A-D(a)). The fragment file is reference with an instrument reader, not a fact the engine uses: deleting it changes no game behaviour, which is the proposal's own falsifier (A-5). It becomes load-bearing on the game only if W5 ships to the port, and only then would §0.05's clause 1 bind it.

### 3.2 The unit of text

For the instrument, the unit is one act with its Events and its occasion. For the journal, it is one claim the focalizer holds (P-2); see section 2.1.

| Field | Owner | Rule |
|---|---|---|
| who | `actor_of` | Instrument always; journal per `supplied_by` |
| via which seat | `Act.via` | Both |
| did what | `Event.kind`, then `degree` | `degree` spans three ladders, so the kind family is read first (D-G) |
| about what | `subject_of(a)` (`state/carriers.py:749`, "THE ONE READ") [CHECKED: holds] | For act-caused Events. `anchor_of` stays the owner for actorless Events only (D-B, L-1) |
| having heard what | `Scene.occasion.about` | Cited only when the act's subject equals the `about` claim's subject. Under `first` the pick is lexicographic over claim-id hashes (`world_q.py:1485-1492`) [CHECKED: holds], so prose must not say "because". Under `all` and `one_per_source` the aggregate keeps `qs[0].about` while widening referents (`decision/questions.py:70-73`) [CHECKED: holds], so the occasion would name a claim about a different subject (D-F, L-11, E-2) |
| why it failed | the failed conjunct in `Event.observed` | In-world reasons (`path`, `purview`, `not-present`, `claim-not-held`) render as reasons. For the 296 refusals with no failed conjunct, the class can be named and the cause cannot (191 are no-op-write refusals carrying the admitted verdict's reads, `resolve.py:445-450`; 105 are ineligibilities, `resolve.py:369-371`; per NERS). Kind-mismatched attempts render as "found it was no T" or are suppressed, never as a social refusal |
| how the person judged it | `deeds_judged` / `regard` | Section 4, appraisal (D-H) |

Actorless MATTER Events never render singly; they aggregate by settlement per season (W7).

### 3.3 Epistemic rules

These rules apply to both products unless marked. Each is a reading rule over existing carriers; none adds a field.

1. **Who and why (journal).** `who` prints only where the focalizer is the actor or the depositing channel supplied it; `why` only where the focalizer is the actor. The table is read from `rosters.yaml` at runtime.
2. **Source.** A claim is told with the `source` and `chain` it carries. Documentary content deposits with `chain=()` (`carriers.py:305-308`, per P-9), so a document's content would read as firsthand; the journal names the record it was read in from the `content:<kind>` predicate, not from `chain`. [WRITER: the predicate is the only carrier that distinguishes "read it" from "saw it"; no review proposed this exact reading.]
3. **Staleness.** A claim is told "as of" the season it was deposited (`Claim.when`), never in the present tense when it is older than the current season. No threshold is introduced. [EXTENSION: P-9 asked for a rule and gave none.]
4. **Contradiction.** Two held claims on one subject with different values are both told, each with its source; the render never reconciles them. [EXTENSION]
5. **Occasion attribution.** As in section 3.2 (D-F).
6. **Evicted antecedents.** Ledgers cap at 200 (`data/fixtures.py:196`) [CHECKED: holds], and eviction emits no Event: "nobody can witness a forgetting" (`loop/witness.py:832-834`) [CHECKED: holds]. A "having heard that P" whose claim is no longer in the holder's ledger at render time is told from W0's per-season snapshot, or not at all (dynamics risk 5).
7. **Labelling (instrument).** Every instrument output says it is an instrument reading.

### 3.4 What is explicitly not done, and the ground

| Not done | Ground |
|---|---|
| A storyline object that steers the sim | The charter's C2 (no arc labels; Jordan's veto); the Light Function's "can never inject content" (ED-IN-0011, v2 §4); T-b; Layer 1 (the forcing proposal's STORY-READ row cites Layer 1 for no salience ranking inside the sim, `forcing-churn:169`). Not ED-IN-0225 alone (section 3.5) |
| Arc labels in fragments | C2. Carried by the fragment key schema, which has no arc slot (A-6), not by a literal-string lint |
| A forecast, countdown or meter | ED-IN-0011; v2 §6 `:397-402` [READ in v1]: anticipation renders pressure and direction, never a verdict or a quantized horizon |
| A stored salience or "interestingness" field | T-a; `forcing-churn:169`; "Bound it by importance and you have built salience-ranked memory … the actor the design exists to refuse" (`architecture/meta/07_DYNAMICS.md:184-186`) [CHECKED: holds] |
| A render-to-world write | The IN-37 falsifier (`_part5:234`) [CHECKED: holds], widened by D-K to `w.acts` and the driver's maps (W1) |
| Need-triggered injection; scripted beats | Argued on the five properties below |
| A per-season MATTER/CALENDAR occasion emitter | Record and Proposition `exists` are admitted only at RES, class ACTS (`write_matrix.yaml:254-265`, verified by the orchestrator); F.31 reads its roster "once at boot" (04 §F.31:1220); AX-6 (§B.6:285-286); `state/attribution.py:46-63`; T-c (A-1). The R2 argument it would need: §7 item 2 |
| Omniscient text read by a player before choosing | 04 §C.11:860-872; `07_DYNAMICS.md:184-186`; E-1 (section 2.2) |
| A runtime LLM | No ground in the sources beyond the bake-time design (frozen fragments, runtime lookup). [WRITER: stated so the absence is visible.] |
| Per-entity branches | Scripting drift (CLAUDE.md §0) |
| A literal copy of the `supplied_by` table | It duplicates `rosters.yaml:955` and fails the roster check (P-D) |

**The R2 argument for the two refusals.** R2 makes every refusal instrumental, to be justified against the five properties (dynamic, capable, flexible, emergent, persistent) or changed, and says the null result "must be argued rather than deferred to" (`references/design_rulings_2026-09-06.md:39-50`) [CHECKED: holds].

- *Need-triggered injection* (a beat for a "starved" prominent person). Capability: no gain, since a lawful carrier already makes a quiet person with an ambition act, the standing `need` question, which "recurs every season until the commitment ends" (`world_q.py:1473-1475`) [CHECKED: holds]; the defect is that it is starved by ordering (section 4, W8), which is a measurement, not a missing mechanism. Emergence: a loss, because the outcome would follow from an observer's threshold rather than from persons' choices; a threshold that acts is an actor (T-b, `01_AXIOMS.md:356-358`), and the shipped precedent emits and never writes ("a crossing MAY NEVER PRODUCE AN OUTCOME", `loop/matter.py:80`) [CHECKED: holds]. Dynamism and flexibility: the trigger couples the world to the observer, and the storybar would then measure its own injections. Persistence: an injected beat has no author, so it is uncontestable and unwitnessable (R4 route 4, `design_rulings:86-87`). It also special-cases an entity. Result: the refusal earns its place.
- *Scripted beats that will occur.* The same argument, plus T-c's dated pins. A multi-beat card survives only as one authored occasion placing an object, after which the later beats are the engine's own motions on it (`Record.stages` → `term.matured`) or persons' responses. A case for guaranteed beats would have to show an emergence gain from removing emergence; none of the inputs makes one.

Starvation is still worth seeing. It is detected outside the sim, as a group-by over `storybar.read` rows (NERS repair 4), never as a trigger.

### 3.5 Scope of ED-IN-0225, and the wording amendment

The row lives only in the archived ledger (`registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml:3209-3237`); no live ledger carries it. Jordan, 2026-09-13: *"Maybe we just ignore the arcs now."* It closes one design question, "what is an arc, as a thing the engine holds", for the 97 ARC cases, on the single ground that a carrier is on none of W23/W26/W30, the blockers of the ARC bar. It states no design argument against a carrier, leaves the 97 cases graded as before, and is not marked RULED in CLAUDE.md. It has since been cited as a positive prohibition: in forcing proposal §5, in the docstrings of `harness/storybar.py`, `harness/soak.py` and `harness/populated.py`, and in the IN-37 entry ("no arc or story carrier inside the simulation (#457 `:190`, ED-IN-0225)", `_part5:232`) [CHECKED: holds].

Three things are called a "carrier", and only the first is kept out:

| Carrier | Disposition | Ground |
|---|---|---|
| A storyline object that steers the sim | Kept out | C2, the Light Function, T-b, Layer 1 (section 3.4) |
| Obligations spanning seasons: staged `Record`s, `oblige` tenures, `date.scheduled`, `case.opened` | Already exist; lawful | They are the engine's own motions; a multi-beat card needs no arc carrier |
| A render-side index of threads | IN-37 itself | Not a carrier: it lives outside the sim and writes nothing |

The amendment proposed: do not lift the ruling; narrow its wording to the question it closed; rest the stronger bans on their own grounds; and replace "thread" with "storyline" or "narrative strand", because "thread" collides with Threadwork (`FORCE-HAZARD` in the same proposal "needs thread operations as a carrier"). The archived row is frozen (CLAUDE.md §3: never edit `registers/archive/`), so the edit would land where the ruling is cited: the docstrings of `harness/storybar.py`, `harness/soak.py` and `harness/populated.py`, the IN-37 entry (`_part5:232`) and forcing-churn `:190` (NERS 9b). [CHECKED: mismatch — NERS and the synthesis notes say "the four citing docstrings"; a search of `engine/` and `tools/` finds three `.py` files citing ED-IN-0225, plus the plan entry and the proposal line.] Section 7, item 4 sets out what is and is not Jordan's in this.

## 4. The proposed work

**Verdict.** Ten packages, ordered by dependency. Three are instruments that change no engine code (W0, W1, W7). Four would change the engine (W2 if adopted, W3, W4, W9), and W3 is already scheduled. W5 adds one Layer-2 read and needs a declared amendment. W6 is authored text. W8 is first a measurement and then, only if Jordan supplies content, boot-time rows. No package depends on the content work before the render can start. Every acceptance test below names the failure it can observe and its control (CLAUDE.md §0.1 pts 2-4); every figure that sizes one is seed 0, two seasons.

### W0 · Corrected instruments and the outstanding measurements

- **Statement.** (a) Re-key every harness refusal count on `REFUSAL_KINDS` (`data/verbs.py:1073`) and split refused, blocked and null-outcome Events. (b) Verify the 21 "nowhere" subjects against `person.died` and closed tenures. (c) Keep the occasion-restored reading as a `storybar` option until W3 lands, then delete it. (d) Repeat the chain read and every section 6 measurement on a second seed and four seasons (v1's M-C). (e) Capture per-season snapshots of typed attributes read from the stores (not `state_of` digests), including `reach` inputs and every ledger, on `storybar.drive`'s `on_season` hook (`storybar.py:165-184`, per A-D). (f) Read questions available against questions taken on the same hook, and run the H-54 sweep (`hole_register.yaml:625-626`) [CHECKED: holds] as an `arms.py` arm, reusing `aperture.py`'s STR-4 arm.
- **Why.** The suffix definition miscounts (section 1.1); `reach`, `place_of` and `home_of` read end state, so a season-0 event would be judged against season-1 seats, and eviction emits no Event (L-2, P-6); every selection rule so far was judged on one seed.
- **Where.** Options on existing instruments and scratch scripts, as `measure_ma.py` was. The snapshot capture is W1's input and lives in `harness/chronicle.py`. No new measurement module (NERS repairs 3-4, A-12).
- **Engine change.** None. A new `storybar` option and new harness code need required arguments with no defaults (`storybar.py:11-12`) [CHECKED: holds], because `harness/` is in the blocking sim-fabrication scope.
- **Falsifier and control.** Per measurement, section 6. For (c): with the option off, `storybar` still reproduces 125/181/71/941 (the shipped reading). For (e): the same seed twice gives identical snapshots, and the hash is equal before and after capture.
- **Dependency.** None. **Cost.** S. **Tag.** Done items [MEASURED]; the rest unmeasured.
- **Replaces.** v1 M-A (done; extended), M-B, M-C, C4(i), C12 and C13 as modules, F1–F6.

### W1 · Render v0: the instrument chronicle on today's substrate

- **Statement.** `harness/chronicle.py`: pure functions over `w.log`, `w.acts`, `driver.act_of`, `driver.scenes`, ledgers and W0's snapshots, producing labelled instrument text per person page per season.
  - **Selection (D-A).** Candidates are `storybar.read` chains on the occasion-restored graph (W0(c) until W3). They are ranked lexicographically, not by a product: (1) executed acts with an effect, and tellings (`news.told` carrying `Said`); (2) executed acts without an effect [WRITER: D-A does not place these acts (389 executed, less about 48 with an effect and the tellings in tier 1); this placement is the writer's reading]; (3) refusals with an in-world reason (`path`, `purview`, `not-present`, `claim-not-held`); (4) kind-mismatched attempts, rendered only as "found it was no T", or suppressed. Within a tier, by cross-person depth. A hard cap per page per season, and a repetition window.
  - **Anti-repetition, with novelty folded in (v1 C9).** A `(template, binding-class)` repeated on one page within the window is suppressed or aggregated ("for the third time"). Precedent is an earlier Event with the same `(kind, subject-class, degree)`, matched discretely; no cosine over features. Restored "own" refusals are 388, and all 79 `migrate` refusals are `path`, so most are probably retries: this rule is first-order, not a refinement (L-D) [INFERRED].
  - **Appraisal (D-H).** Call the sim's own `deeds_judged` / `regard`, which weight by `to_axes(crisis_weights(…))` (`person_q.py:71-96`, per NERS), never `to_axes(p.pursuits)`, which is a second ladder (L-7). Render only where nonzero, labelled "as she judged it". Nothing for the 37 pursuit-less cohort persons, and nothing for refusals, which are not deeds (`person_q.py:106-110`) [CHECKED: holds].
  - **Names.** `Person.name`, else `[NAME?]`. Rungs have no name field (`carriers.py:990`) [CHECKED: holds], and adding one would amend §B.3. Settlement names come from the geography source `build_realm` reads (`populated.py:1271-1272`) [CHECKED: holds; a local dict, exposed once by W9(d)]; anything else is a stated limit. Not `canonical_for`, which resolves terms (`engine/substrate/names.py:1`) [CHECKED: holds].
  - **Realization.** A minimal fragment set (one per kind family and outcome tier) until W6.
- **Why.** The render can start on what exists (L-4); an honest render is itself a diagnostic of candidate typing (L-D); a product score zeroes about 96% of acts, since only about 48 of 1,318 have an effect, and so contradicts "a refusal renders as a one-line reason" (L-8, E-4).
- **Where.** `harness/chronicle.py`, the fragment file beside it (IN-37, B-U).
- **Engine change.** None. New harness modules are discovered by `test_season_shape.py:2402` [CHECKED: holds]; one test file.
- **Falsifier and control.**
  1. *No write.* `content_hash` equal before and after, and a digest of `w.acts`, `driver.act_of` and `driver.scenes` equal before and after (D-K, A-7: those three are outside `_STATE_COLLECTIONS`, `world.py:1277-1278`) [CHECKED: holds]. Control: a planted mutation of one Act payload fails the digest and passes `content_hash`, showing why both are needed. `reach` writes `TRACE.query` (`world_q.py:462`) [CHECKED: holds]; the render reads `reach` from W0's snapshots and never calls it.
  2. *Ranking.* A planted consequential cross-person chain outranks a planted kind-mismatched refusal. Control: the same pair with the tier order reversed inverts the result, so the test can observe a bad ranking (L-8).
  3. *Honesty.* Zero rendered lines use a social-refusal template for an Event whose `observed` carries `exists:<T> = 0`. Control: the input holds 460 such refusals, so a zero is a result, not an absence.
  4. *Determinism.* The same seed twice gives the same text; a different seed gives different text.
- **Dependency.** None (W0(c) for depth; on the shipped graph depth is understated). **Cost.** M. **Tag.** Owners [READ]; the tier order [INFERRED], since no measurement fixes it.
- **Replaces.** C7 (deleted), C9 (kept, novelty folded), C5 (as D-H), C15 (owner changed), the instrument half of C6.

### W2 · Candidate-typing disposition (a real dispute)

- **Statement.** A named item, owned by the decision and verb lane, decided by a measured arm and not by fiat. Narration does not wait for it: W1 labels the mismatches.
- **The case for fixing.** 439 of 1,318 acts (33.3%) choose a subject that exists as another kind. `opening_set` loops every verb (`options.py:109`) over every referent (`:124`) [CHECKED: holds], and the referent is the single `c.subject` (`world_q.py:1471`) [CHECKED: holds], with no kind filter. The engine already declines a refusal-feeding case at formation (a counterparty who is the actor), because "a refusal teaches nothing -- MEASURED, it fed itself", a "constant scene tax with nothing behind it" (`options.py:160-161,172`) [CHECKED: holds]. Typed existence cells exist (`of: subject, kind:`); typed ids are the §B.1 target (`Id := (kind_tag, n)`, ED-IN-0206, unbuilt), so the carrier-type half is conformance, not amendment (A-2); and `carriers.py:474-477` names the hazard, a refusal becoming "a FALSE BELIEF held by everyone who witnessed it" (per A-2).
- **The case against deciding by fiat.** Failed attempts are how the sim teaches types today: §F1 clause 4's `belief_contradicts` turns a failed look into a declined later attempt, 25 → 1,104 decision-affecting drops, across five predicates including `exists:Person`, `exists:Record`, `exists:Rung` and `exists:Site` (`test_season_shape.py:11210-11213`) [CHECKED: holds; the same block says three instruments give three figures for this quantity and only the 25/1,491 pair is like-for-like]. Clause 4 is deliberately epistemic: "a person who wrongly believes the granary full SHOULD form the Candidate and learn otherwise" (`options.py:138-142`) [CHECKED: holds]. AX-2 forbids the decision layer reading world truth (`place_of` "MAY NOT BE CALLED FROM `decision/`", `world_q.py:416`, per P-4), so a kind must arrive on the Question or from the person's own `exists:` claims. And R3's cross-person edges run through refused acts ("all five were refused", `_part4:48`) [CHECKED: holds], so removing refusals can remove edges (P-4).
- [WRITER: the tree's own test for decline-versus-learn is at `options.py:138-142`: decline where the fact "is not a belief anyone can be wrong about", form and learn where it is. Whether a subject's kind is such a belief is the question the arm should settle.]
- **Options.** (1) *Carrier-type half:* `questions_for` (World side) tags each referent with its kind, and `opening_set` binds a subject only where the row's own existence cell matches, reading the table's declarations, never a verb name, and no `World` (A-2). (2) *Keep refusals as learning:* no engine change; W1 labels them. (3) *One clause in `belief_contradicts`* reading kind-disjointness from the person's own `exists:` claims (NERS's minimal form; an inference producer R8.2 defers). The record-kind half (`build`/`found` on `exists:works = 0`, 62 refusals, no works ever minted) is separate: it is a missing producer, not a mistyped object, and is carried by W4 and W8 (E-3, NERS 9a).
- **Recommended.** (1) and (3) as a measured arm against a byte-identical control, five or more seeds, four seasons, composing on the H-94 operand channel inside the owning batches (P-4): B-I for `commit`, `confer`, `revoke`; B-K for `work`, `migrate`, `found`, `build`, `levy` (`_part3:297,299`) [CHECKED: holds for those eight; `give` is in neither row — B-R's row carries "give+Rung", `_part3:306`]. Measure executed acts, distinct executed sets, storybar depth, the refusal share, the clause-4 drops, R3 edges, and dynamics risk 1.
- **A disagreement between reviews, kept.** A-2 places option (1)'s binding in `opening_set`; P-4 asks for no new filter in `opening_set` and composition on H-94's operand channel instead. The arm should be built on H-94's channel; if option (1) cannot be expressed there, that is a finding for the lane, not a licence to add the filter.
- **Engine change.** Yes, if adopted. Co-edits: the executed-set pin `ever` (`test_season_shape.py:7628-7632`, "`H-96` must be re-measured") [CHECKED: holds]; `DECLINED` (`test_u7_own.py:42`) [CHECKED: mismatch — that tuple lists verbs declined from resolvability (`carry`, `exchange`, `forge`, `repudiate`, `succeed`, `thread_read`, `tie / knot`); a subject-typing arm touches none of them, so it is not an evident co-edit]; goldens; `runs/`.
- **Falsifier and control.** The `exists:<carrier> = 0` share falls to zero under the arm (A-2). Control: the arm off, byte-identical hash. Counter-falsifier: the clause-4 drops, measured under both arms, show what learning is lost.
- **Dependency.** W0 (re-keyed refusals, second seed). **Cost.** M–L. **Tag.** Evidence [MEASURED]; outcome unmeasured. **Replaces.** Nothing in v1 (it was missing).

### W3 · IN-50 (already scheduled)

- **Statement.** Every refusal return in `loop/resolve.py` carries the act's occasion ids (B-I; `_part2:61`, `_part4:46-51`) [CHECKED: holds].
- **Why.** Until then, the shipped reading cannot see the occasion of 929 acts.
- **Engine change.** Yes. Pins to re-record (the plan names two; P-D lists the rest): `d_pub` 5→10; depths (9,10)→(12,13) in `test_season_shape.py`; `runs/TRACE.txt` via `harness.report`; `_FOLD_PURPOSES` in `test_g1b_attribution.py` goes dead; R-01's `measured:` row; hash `d0015936`→`ff2f6742` (`_part4:48`) [CHECKED: holds]; the "FLOOR" paragraph in `storybar.py:21-25` [CHECKED: holds] goes stale. Each re-record is stated as a re-record (CLAUDE.md §7).
- **Falsifier and control.** After W3, the shipped reading equals the restored one exactly: 314/568/292/144 (L-13). Control: W0(c)'s option, which is then redundant and is deleted. [CHECKED: `storybar.py:22` places the success stamp at `resolve.py:487`; L-13 cites `:170,489`; the line drift was not reconciled.]
- **Caution.** Chain depth is partly self-feeding: a witnessed wrong-kind refusal deposits a claim that raises the next question (L-D). Restoring those edges before W2 makes depth rank instrument artifacts as the deepest chains (A-2). This is why W1 ranks by outcome tier before depth.
- **Dependency.** None. **Cost.** S. **Tag.** [READ]. **Replaces.** C3; M-B after it lands.

### W4 · A content-bearing record kind, and its handover

- **Statement.** Register a new record kind with one key, `says` (a `Said`), minted by `create_record` through a named `own_ledger` conjunct in its typed cell, so that `opening_set` copies `said` from the actor's ledger and declines when there is nothing to say (`options.py:119-121,182-204`) [CHECKED: holds], on `tell`'s precedent (`verb_table.yaml:937-941`) [CHECKED: holds]. A new registration on `_mint_document` (`effects_information.py:110-114`, per A-8). No `about` key: "an extra key is a second vocabulary".
- **Why a new kind and not `text`.** "`text: []` is why every Record minted before this roster stays lawful" (`rosters.yaml:177-178`) [CHECKED: holds]; amending it would raise `Forbidden` at 10 `text` constructions (4 in `harness/probes.py`, 6 in tests) [CHECKED: the count reproduces by search; the cited `carriers.py:720-723` states the mechanism, not the count]. Every content kind so far landed as its own kind with its producer (`works`, `faction_sheet`). This closes at CLAUDE.md §0 test 4; v1's D5 is withdrawn.
- **The handover.** Content reaches a second person only when they come to hold the Record (`witness.py:335-348`); `give` is chooser-unreachable (`witness.py:365-368`) and executed 0 of 24; `research` executed 14 of 84, 69 refusals on `exists:Record` (P-1). So the acceptance test depends on W2.
- **Open point.** Computed acts carry no payload and "always mint `text`" (`effects_information.py:65-66`) [CHECKED: holds]. How many of the 110 executed `create_record` acts would decline under the named conjunct is unmeasured; it should be few, since a `claim_landed` question is about a subject the actor holds a claim on [INFERRED].
- **Engine change.** Yes. Co-edits (P-D): `rosters.yaml:210-211` [CHECKED: holds] and the note at `:177-178`; `decision/options.py::operands_for` (`:842`); the content deposit (`witness.py:344-348`), which moves ledgers and evictions; `test_record_kind_fold.py`, `test_content_operands.py`, `test_information_cluster.py`; `test_season_shape.py:7628` if `create_record` leaves the executed set; goldens; `engine/season/runs/*`.
- **Falsifier and control.** (a) A non-author holds `content:<kind>` after a handover; control: the same seed with W4 off has none. (b) An actor with no claim about the subject forms no `create_record` Candidate of the new kind; control: an actor holding one forms one (L-5). (c) M-A before and after W4: the refusal share must not rise (dynamics risk 4).
- **Utterances (v1 C2), deferred.** Nothing reads `Proposition.predicate`: `ambitions` reads mood and edges (`world_q.py:1347-1352`) and Q4 reads `.subject` (`:1478-1479`) [CHECKED: both hold]. The operand vocabulary is closed at eight names (`options.py:705`), and `utter` declares `emits_on_refusal: []` (`verb_table.yaml:1219`) [CHECKED: both hold]. Binding would remove up to 52 executed acts for a reader that exists only in the render; render `utter` as "spoke of X". A later form would bind any operand Proposition, preserving falsity (`utter` has no precondition, which is how false content enters today), and state the mood (E-3, L-6).
- **Falsity.** [WRITER: `says` from the actor's own ledger admits honest error but not deliberate lies; deliberate falsity stays with `utter`, so W4 does not close it (E-F).]
- **Dependency.** The kind: none. The acceptance test: W2. **Cost.** M. **Tag.** [READ]; [PRECEDENT] for the new-kind shape. **Replaces.** C1 (option 2), C2 (deferred), D5.

### W5 · The focalized journal

- **Statement.** A `person_q` function in the §C.11 `explain` shape: no `World` parameter, no walk from `causes[]` to `Act.actor`. It selects from the focalizer's own claims and Scenes; takes text fields from each claim's `seen` struct; prints `who` and `why` per section 3.3 rule 1; tells appraisal through `deeds_judged`, labelled as the person's own; and reads the realizer and fragments W1 and W6 use. Its shell is `port/`.
- **Relevance.** The ledger is the relevance (A-9). [WRITER: D-F says relevance runs "through `questions_for`'s three clauses", but those call `reach(w, p)`, which needs `World`. The journal can take the clauses' output, the Questions already raised for that person, and never recompute them.]
- **Why.** Section 2.2: player coupling, hidden-actor existence, leaked knowledge.
- **Where.** `queries/person_q.py`; a new §A.2 module row (declared amendment, section 7 item 3).
- **Engine change.** A new pure read; no hash move. Co-edit: the §A.2 row in 04 (ratified Layer 1).
- **Falsifier and control.**
  1. *Leak count.* Fields the journal emits that the focalizer's `seen` struct lacks: 0. Control: the instrument over the same focalizer emits more than 0 (the 144 `date.scheduled` holders, P-2).
  2. *Player coupling (E-1, D-K).* The same seed with a scripted callback choosing from the View alone, then from the View plus the journal; compare distinct executed sets and `content_hash`. [EXTENSION: a third arm, View plus the instrument chronicle, is the positive control. It should differ, which shows the comparison can see coupling.]
  3. *Variety.* Two persons sharing a reach get different journals when their ledgers differ (NERS R-VARIETY).
- **Dependency.** W1; W0(e) for claims evicted before render. W4 enriches. **Cost.** M. **Tag.** [READ]. **Replaces.** C6's focalized half; answers A-3, P-2, E-1.

### W6 · Fragment bake and template selection

- **Template selection (D-G).** Key = (kind family, degree band, refusal stem or an explicit no-stem cell, `via?`, `weight > 1`). Kind family precedes degree, because degree spans three ladders. The most specific fragment wins; ties break by a seeded pick. [WRITER: the archived source seeds on `key.id` + `season_index` and marks the choice open (`_workings_joined.md:2852-2854`, per v1's check); seeding on `e.id` is a choice this proposal makes, not a precedent.] `source` and `hops-band` are dropped until IN-18 produces tellings: 4 of 11,929 claims carry a chain. The refusal stem reads `REFUSAL_KINDS`, not a suffix list.
- **Cells.** Static enumeration = each row's `emits_at(degree)` (`resolve.py:480`) × `REQUIRES_STEMS` × the closed sets, minus suppressed stems. It over-counts unreachable cells: `commit` never executes (`effects_information.py:503-504`) [CHECKED: holds].
- **Where the file lives.** Beside its reader. The reader builds its key space from `data/` (the derived Event kinds, §B.13:496; `CELL_STEMS`) and refuses an unknown key at load (A-5). Names bind at render, never in fragments (PART D 27a, `:1043`, per A-5).
- **Bake protocol (prose-writer).** Write N variants per enumerated cell, observed cells first; audit against `anti-patterns-skeleton.md` I.14; treat Certainty as a lexicon swap (the archived fork-6 fallback); a chronicler's voice, if wanted, is a lexicon over the same cells (section 2.3 (a)). No lint gate: the key schema has no arc slot, and the censured vocabulary already has a gate (A-6; a literal "arc" would also match `march`, a live verb, NERS). A coverage report (static against observed cells) runs once at bake and is never a gate (§0.1 pt 5).
- **Engine change.** None.
- **Falsifier and control.** A planted more-specific fragment wins; removing it falls back one level; an unknown key is refused at load (control: a known key loads); the same seed gives the same text.
- **Dependency.** W1; and W2's outcome, which changes the cell population (baking before it authors wrong-kind cells). **Cost.** L. **Tag.** [READ]. **Replaces.** C8 (two dimensions dropped), C10 (lint and gate deleted).

### W7 · Scale lines [EXTENSION, from the propagation review]

- **Statement.** (a) *Settlement:* actorless MATTER Events grouped per season by `place_of(anchor_of(e))` plus `containment.ancestry` (`state/containment.py:40,89`, per P-5); this turns the 644 wear writes into settlement lines. (b) *Faction:* through `faction_q.resolve` (`faction_q.py:98`, per P-5); `faction_sheet` Records are frozen when written and go stale, which gives staleness and contradiction with no new carrier. (c) *Cohort:* through the `weight > 1` key (S9's `is_cohort`, `carriers.py:645-653`, per P-E); `weight.changed` at CENSUS has no line (`write_matrix.yaml:240-246`) [CHECKED: holds; MATTER, step CEN]. (d) *Gaps, named:* a season summary and a realm line.
- **Vertical rule.** [WRITER: a person's act renders on the person's page and is never folded into a settlement aggregate; the settlement line carries actorless Events only. NERS found no rule for when a person beat yields to an aggregate; this is the proposed one.]
- **March.** A `march` act has two degrees (Declared, then the field band), and the seam emits `field.won/lost/unopposed` (`verb_table.yaml:667-671`, per P-C). The run has `march.declared` 8 and no `field.*` (`inventory_out.txt:34`) [MEASURED], so the path is untested. [WRITER: render the declaration at the act and the field band as a second line keyed by the field Event.]
- **Engine change.** None. **Falsifier and control.** The per-settlement aggregates sum to the count of actorless Events (nothing lost or counted twice); control: a planted MATTER Event at a known place appears in that settlement's line only.
- **Dependency.** W1. **Cost.** S–M. **Tag.** [READ] for owners; the grouping [INFERRED].

### W8 · The occasion ladder (replaces the deck)

- **Rung 1: existing carriers, measured first.** The standing `need` question from an ambition (`world_q.py:1473-1479`) [CHECKED: holds]; a faction creed is an ambition for 35 of 83 persons (`world_q.py:1365`) [CHECKED: holds]. `claim_landed` sorts before `need` (`rosters.yaml:574`) [CHECKED: holds], and under `first` a need question was taken in 51 of 803 deliberations. Measure need starvation under `one_per_source` first (E-6), remembering that occasion attribution breaks under that rule (D-J). Then petitions addressed with `to` (a summons through `named()`, `world_q.py:507-513`, per E-3), staged Records maturing at MATTER (`term.matured`, 61 in the run) and `condition.band_crossed` (`matter.py:35-82`). Works Records leading to `found` and `build` would grow the world, a stronger churn source than a deck (E-E); B-K carries "found/build priced and executing" (`_part3:299`) [CHECKED: holds].
- **Rung 2: authored occasions as boot-time rows**, read once by `build_realm` (04 §F.31; precedent `populated.py:1262`, "authored rows read once here (`ED-WR-0011` option A -- no clock and no formula mints one)") [CHECKED: holds]. Content is Jordan's, already open as forcing-churn §7 decision 3. Rows must not key on seat age: every hold tenure is minted with `since` 0 (`populated.py:909,1060,1115`) [CHECKED: holds], so seat-age cards would fire in one synchronized pulse (E-6).
- **Rung 3: a per-season emitter.** Refused (section 3.4) unless the R2 argument in section 7 is made.
- **Starvation.** Detected outside the sim as a group-by over `storybar.read` rows.
- **Engine change.** Rung 1: none (a sweep). Rung 2: yes (a roster, its loader in `data/rosters.py`, `build_realm`); goldens move only when a row is authored.
- **Falsifier and control.** Rung 1: need-taken share under `one_per_source` against `first` (control: `first` reproduces today's hash). Rung 2: with zero rows the hash is byte-identical (control); with one row, a claim lands and changes someone's decision. "Raises a question" is not enough: "pressure that changes nobody's decision is scenery" (`design_rulings:91`) [CHECKED: holds].
- **Dependency.** W0; FORCE-* measured first (forcing-churn §6). **Cost.** M. **Tag.** [READ]. **Replaces.** C11, C12, D2.

### W9 · Conformance items

- **(a) `Receipt.before/after`.** 04 §B.9:425 specifies `( id …, kind, field, subject id, before, after )` (verified by the orchestrator); the code carries subject, mode, driver, field, delta, spec and serial (`carriers.py:168-214`, per A-4). Use the spec's spelling, not `prior`, with typed values read from the store, since `was` is a `state_of` repr tuple (L-2). MATTER writes bypass the `Change` path and mint receipts with `None` (`world.py:1049-1050,1149`, per A-4), so MATTER receipts stay partial until they go through `Change`. `StateChange.delta` already exists, is hashed (`world.py:1322`) and is always `None`: fill it or add `before/after`, never both (P-7), declaring any hash move. Not a narration dependency. Falsifier: `content_hash` unchanged on every golden for unhashed fields, plus `runs/` byte identity, since "a carrier gaining a field moves every digest that reprs it" (`carriers.py:197-199`, per L-2); control: a planted hashed field moves the goldens. Co-edits: `carriers.py:214`, `world.py:1054,1097`, every site that reprs a Receipt. Closes at §0 test 3; v1's D1 is withdrawn.
- **(b)** Harness refusal counts read `REFUSAL_KINDS` (W0(a)).
- **(c)** If an instrument page filters by relevance, extract `questions_for`'s three-clause predicate once in `world_q` (`:1468-1470`) and call it from both sites: one rule, one spelling (A-9). Behaviour-neutral; falsifier: hash unchanged.
- **(d)** Expose settlement names once from the geography source `build_realm` reads (A-10).
- **Cost.** M for (a), S for the rest. **Tag.** [READ]. **Replaces.** C4(ii), D1.

### 4.1 Where each v1 item went

| v1 | v2 | | v1 | v2 |
|---|---|---|---|---|
| C1 | W4 (option 2) | | C10 | W6; lint and gate deleted |
| C2 | Deferred (W4) | | C11 | W8; emitter refused |
| C3 | W3 | | C12 | Deleted (a group-by) |
| C4(i) | W0(e) | | C13 | Deleted as a module; W0(f) |
| C4(ii) | W9(a) | | C14 | Out of lane: the telling lane, IN-18 |
| C5 | W1 / W5 appraisal | | C15 | W1 names; owner changed |
| C6 | W5; W9(c) | | M-A | Done; W0(a-b) |
| C7 | Deleted | | M-B | W0(c), deleted after W3 |
| C8 | W6 | | M-C | W0(d) |
| C9 | W1, novelty folded | | D1–D5 | Section 7 |

## 5. Sequencing against the master plan

**Verdict.** The instrument render needs nothing unscheduled: it can open in B-U beside B-P and B-Q. It stays that way only if IN-37 is not given the content work as a dependency. v1 named C1 and C2 as dependencies of IN-37 and also said nothing reordered B-U; those two statements contradict each other (P-3). This proposal recommends leaving IN-37 without them.

**The plan as it stands.** IN-37: STATE `BLK:SC-01 step 16`; batch B-U, head IN-37 → IN-27 → IN-30, entering on B-N merged; EDITS "none in `engine/season/` beyond a reader under `harness/`"; EXIT "a render of one seed's chain that a reader can follow" (`_part5:231-234`) [CHECKED: holds]. The batch order places "B-U beside B-P and B-Q (opens after B-N, merges before B-R)" (`_part3:190`) [CHECKED: mismatch — the synthesis notes and P-3 cite `_part3:303` for "B-U may open beside B-P"; line 303 is B-O's row; the ordering text is at `:190`, and B-U's own row is `:307`]. B-U's row closes with "next B-R once B-P and B-Q merge" (`_part3:307`) [CHECKED: holds]. So B-U opens before B-Q merges.

**The B-U/B-Q point.** The content kind (W4) sits with the verb batches (B-I, B-Q). If it became a dependency of IN-37, B-U would wait on B-Q: a reorder the plan owner would have to declare. W1 is specified to need none of it, so the reorder is unnecessary. The SC-01 step 16 block on IN-37 is M2 bookkeeping rather than a technical dependency, since `storybar` already reads the same log (the Fable file's reading); whether to treat it so is the plan owner's call.

| Package | Placement | Note |
|---|---|---|
| W0 | Any lane with slack, now | Instruments, as `storybar.py` landed at B-C |
| W1 | IN-37, B-U | Needs nothing unscheduled |
| W2 | Arms inside B-I (`commit`, `confer`, `revoke`) and B-K (`work`, `migrate`, `found`, `build`, `levy`) | Decision and verb lane; `give` sits at B-R |
| W3 | B-I, scheduled | Pin list in W3 |
| W4 | With the verb batches, after W2 is measured | Dynamics risk 4 forbids landing it before typing is decided |
| W5 | After W1, and after the §A.2 ruling | No batch is named. [WRITER: B-L carries PC-06 (M-1, S-2) (`_part3:300`), the play-surface work this journal serves; it is the nearest fit] |
| W6 | After W1 and W2's decision | Authored data |
| W7 | B-U, after W1 | |
| W8 | Rung 1 with W0; rung 2 after FORCE-* and Jordan's content | |
| W9(a) | IN lane, any batch | Not narration-gating |

## 6. Dynamics risks and measurements

**Verdict.** The fixes that would make the season more narratable would also change its dynamics in five ways nobody has measured, and the journal adds a sixth through the player. Each has a defined measurement; none has run. Nothing sized on seed 0 over two seasons should be fixed before W0(d) repeats it.

### 6.1 The risks

1. **Hostility after a typing fix.** `fight` is refused 14 of 16, `challenge` 29 of 34, `accept` 31 of 40, all wrong-kind. Fixing typing lets duels execute and write stance. Judged regard is live at 0.5, `stance_gain` ships at 1.0, polarity at `legacy`, and no `forgive` verb exists. [CHECKED: `data/fixtures.py:726-729` says that under `legacy` the stance term "moves no realm outcome there until a stance row meets one candidate's subject and not another's"; executed duels would supply exactly such rows. WRITER: so the shipped gain is inert today and may stop being inert after W2.] Measure: `populated.run(4, s)`, seeds 0-4, with the typing arm, crossing polarity `legacy` and `declared`; stance rows per person per season, `fight` acts per season, and the slope.
2. **Paper.** W4 plus working `give` and `research` makes Records the carrier between people, with no sink: `destroy_record` was never attempted, and records grew 79 → 240 over three seasons (`forcing-churn:167`, per E-C). Claims about Records raise questions about Records, which feeds wrong-kind targeting. Measure: records per season, and `claim_landed` questions whose subject is a Record, W4 on and off, four seasons.
3. **Ambitions only grow.** A working `commit` opens edges to OUGHTs, while `release` is refused 64 of 67. Measure: the length of `ambitions(w, p)` per season, and deliberation time per season.
4. **Ordering.** Content landing before typing raises the refusal share. Measure: M-A before and after W4.
5. **Evicted antecedents.** More content claims push ledgers against the cap, so a narrated "having heard P" may already be gone. Measure: the share of occasion claim ids no longer in the holder's ledger at render time.
6. **Coupling through the player.** Section 2.2; measured by W5's falsifier 2.

### 6.2 Measurements done and to run

All "done" rows are seed 0, two seasons, scratch scripts outside the tree.

| Measurement | Definition | Instrument | Control | State |
|---|---|---|---|---|
| Storybar (shipped, restored); chains; inventory; D12; M-A and its split; conviction spread | As reported in §1.1 | `S/storybar2.py`, `chains*.py`, `inventory.py`, `d12.py`, `measure_ma*.py` | Shipped reading; firsthand claims; executed Events (weak, L-12) | Done (spread is a table, not a run) |
| Second seed, four seasons | Every row above | the same scripts | Seed 0 reproduces the two trunks | To run (W0(d)) |
| Refusals re-keyed | Counts under `REFUSAL_KINDS`; refused/blocked/null split | W0(a) | The per-row emits | To run |
| The 21 "nowhere" | Are they dead persons? | `person.died`, closed tenures | A planted Act on a known-dead id | To run |
| Typing arm | Section 4, W2 | `arms.py` | Arm off, byte-identical | To run |
| Need starvation | Need-taken share under `one_per_source` | W0(f) | `first` = today's hash | To run |
| `anchor_of` vs `subject_of` | Agreement on act Events | `w.log` | Expected near zero where subject ≠ actor | To run |
| Receipt mix | Share of Receipts on fielded vs entity-digest subjects | `w.log` | — | To run |
| Appraisal coverage | Share of (person, deed claim) pairs with nonzero valence under `crisis_weights` | `deeds_judged` | `uniform` reads constant per holder | To run |
| Cell coverage | Static against observed W6 cells, five seeds | W6's enumeration | Observed ⊆ static | To run |
| Repeat rate | `(subject, kind)` per season per page | `w.log` | Shuffled seeds | To run |
| Leak count | `who`/`why` fields emitted beyond the `seen` struct | W5 | The instrument over the same person | To run |
| End state vs snapshots | Season-0 claims each side misses | W0(e) | — | To run |
| Handover | Non-authors holding `content:<kind>` after `give` | W4 | W4 off | To run |
| Risks 1-6 | Section 6.1 | as stated | as stated | To run |
| D12 on tellings | Restricted to `chain != ()`, after IN-18 | the telling lane | Firsthand claims | Out of lane |

## 7. Decisions that are Jordan's, and amendments declared

**Verdict.** Four questions survive CLAUDE.md §0's five-step ladder (superseded, irrelevant, answered by a design document, by precedent, by architecture). Two of them would amend ratified text, and the argument R2 requires is given for each. Five v1 rows close without him.

**1. Candidate-typing disposition (W2).** *Why it survives:* design documents and precedent point both ways (§B.1's typed ids and the formation-decline precedent for fixing; §F1 clause 4's learning and AX-2 against), and the two answers give materially different games. *Question:* are kind-mismatched attempts learning, or a scene tax to decline at formation? *Options:* W2's (1), (2), (3). *Recommended:* run W2's arm first; adopt (1) with (3) unless the arm shows that removing the attempts removes the cross-person edges and the learning by which the season propagates. *What each changes:* (1)/(3) redirect up to a third of all acts, let duels execute (risk 1), and move pins and goldens; (2) changes nothing and leaves 33.3% of acts to be told as "found it was no T".

**2. Authored occasions (W8).** *Why it survives:* it is already an open escalation, forcing-churn §7 decision 3: "May the scenario pin dates (an authored occasion, a clock)? Recommendation: no default" (`forcing-churn:213`, per NERS); v1's D2 merges here. *Options:* (a) none: rung 1 only; (b) boot-time rows whose content Jordan authors or approves; (c) a per-season emitter. *Recommended:* (a) until rung 1 is measured; (b) if the measurement shows starvation that existing carriers cannot reach. *Amendment if (c):* it touches 04 §F.31:1220 ("read once at boot"), T-c (`01_AXIOMS.md:376`), the Record and Proposition `exists` rows (RES, ACTS), and AX-6 via §B.6:285-286. *R2 argument owed for (c):* an emergence gain over the boot form that outweighs losing T-c's handles (a boot-time card is a Record someone can burn). On the five properties: dynamic and emergent, no gain the boot form lacks has been shown; persistent and capable, (c) loses contestability, since an unauthored per-season change is uncontestable and unwitnessable (R4 route 4). The reviews read the argument as unlikely to hold; none of the inputs makes it.

**3. The focalized journal as a §A.2 module row (W5).** *Why it survives:* adding a row to ratified Layer 1 (ED-IN-0204) is an amendment. *Declared amendment:* 04 §A.2 (`04:129-156`) gains a row for the journal function; §C.11 is not amended, because the journal takes no `World` and walks no `causes[] → Act.actor`. *R2 argument:* capable, the player gets a text of the season beyond the 12-claim View; persistent, the function is a read and keeps nothing; emergent, it preserves hidden actors' existence, which is what makes investigation worth a scene (§C.11:868-872); flexible, one §C.11 owner can serve the player's preview and NPC journals (A-E). *Options:* (a) add the row; (b) keep narration instrument-only, with no player text; (c) a player-facing omniscient render. (c) would amend §C.11 and owes an argument for giving up hidden-actor existence; none is offered. *Recommended:* (a). *What each changes:* (a) one Layer-1 row and one `person_q` function; (b) nothing, and the player reads only the View; (c) concealment and falsity stop working against the player (section 2.2).

**4. ED-IN-0225's wording (section 3.5).** *What closes on the ladder:* where the edit lands. The archived row is frozen, so the edit goes to the sites that cite it (step 3; v1's D4 location question). *What survives:* the reading of Jordan's own words, *"Maybe we just ignore the arcs now"*, is the scope of his ruling, and narrowing it is his. *Options:* narrow the citing text; leave it; lift the ruling. *Recommended:* narrow; do not lift. *What each changes:* narrowing distinguishes the three carriers and stops the ruling being cited against staged Records and a render-side index; leaving it keeps that over-broad citation; lifting reopens the 97 ARC cases, which nobody has asked for.

**Closed by the ladder, not Jordan's.**

| v1 row | Closes at | Ground |
|---|---|---|
| D1 · `Receipt` pre-value | Step 3 (design document) | 04 §B.9:425 already specifies `before, after`; the code is non-conformant (A-4). W9(a) |
| D3 · Should the sim consume appraisal? | Step 1 (superseded) | The gains shipped live on 2026-10-09 (`fixtures.py:699-708`) [CHECKED: holds] |
| D5 · Amend `text` or add a kind? | Step 4 (precedent) | Every content kind landed as its own kind with its producer. W4 |
| D4 · Where the wording edit lands | Step 3 | The archive is frozen (CLAUDE.md §3) |
| D2 · Deck content | Step 1 | Merged into item 2 above |

**Refused without escalation:** need-triggered injection, guaranteed beats, a stored salience, and a storyline carrier that steers the sim (section 3.4, argued on the five properties).

[WRITER: if W5 is adopted, `skills/prose-writer/SKILL.md:158` ("The player's vantage is genuinely omniscient") would need narrowing to match. That is a process surface, not a ruling, and needs no decision.]

## 8. NERS self-audit of this proposal

[SELF-AUTHORED — bias risk] The writer of v2 is in the producer's lineage and audits work it specified. The method is `skills/ners/SKILL.md` §2-§9; the object is the proposed work, not this text.

**Verdict.** v2 adds fewer objects than v1 and deletes more, and its disciplines hold except in one family, authored content entering the world, which it licenses narrowly. It remains paper: nothing in W1–W9 has run.

### 8.1 Object count (E-OVERHEAD)

| | v1 | v2 |
|---|---|---|
| Added | About 15, including six modules, the lint, the coverage gate, the `occasions` roster and its emitter, `Receipt.prior`, and about six parameters (NERS) | Unconditional: `harness/chronicle.py`; the fragment file beside it; one content-bearing record kind; one `person_q` journal function; one §A.2 row; up to three required arguments (cap, length bands, repetition window). Conditional on a ruling: the W2 clause; the W8 boot roster and its loader. Conformance, not addition: `Receipt.before/after` (§B.9) |
| Changed | 5: `record_kinds`, `create_record`, `utter`, `resolve.py`, a `storybar` option | `create_record`'s typed cell; `record_kinds`; `resolve.py` (IN-50, scheduled); a `storybar` option (removed after W3); conditionally `world_q`'s predicate extraction and the exposed settlement names (W9(c-d)) |
| Folded | 0 | Novelty into anti-repetition; C12 into a `storybar.read` group-by; C13 into `aperture.py`/`arms.py`/`on_season`; C4(i) into `chronicle.py`'s snapshot; M-B into W3 |
| Deleted | 0 | The C7 product; the C10 lint and gate; the C11 emitter; C15's owner; `source` and `hops-band`; the `about` key; C2's binding (deferred); `coverage.py`, `attention.py`, the D12, M-A and M-C modules; decision rows D1, D3, D4, D5 (D2 merged) |
| Vocabulary | About +10 | +4 ("instrument chronicle", "focalized journal", "kind-mismatched attempt", "occasion ladder"); retires "deck", "starvation report", "selection score" and its five factor names, "hops-band" |

Denominator (§5.1): the fragments are an authored inventory of (statically enumerated cells minus suppressed stems) × N variants, and no cell count is stated until W6's enumeration runs. W8 rung 2, if chosen, is authored content too.

### 8.2 N-line ledger and false-N-line check, for every object v2 adds

| Object | N-line (cut it and the game can no longer …) | Verdict | Disqualifiers (1 carrier exists · 2 no producer · 3 re-added cut · 4 second thumb · 5 flat bonus) |
|---|---|---|---|
| `harness/chronicle.py` | … be read by its designers as a sequence of attempts with reasons (IN-37's exit) | Holds, narrowed: an instrument, so the loss falls on the design process, not on play, unless W5 ships | 1: `storybar.read` gives classes and depth, not text — partial; 2-5 do not fire |
| Fragment file | … print anything | Holds | 2: its producer is the bake, an authored inventory (denominator above) |
| Content-bearing record kind | … let a document carry a claim to a second person | Holds, narrowed: until W2 makes a handover reachable, the content reaches its author only | 2 fires until W2; 1: `text` exists but carries `None`; 3: not a re-add |
| Journal function and §A.2 row | … give a player a text of the season that respects what their person could know | Holds | 1: the View carries 12 claim ids, not a text — partial |
| Required arguments | … bound the instrument's output | Not game objects; required by the fabrication gate | — |
| W2 clause (conditional) | … stop spending a third of all acts on wrong-kind subjects | Contested (W2) | 1: clause 4 already carries learning; this is the dispute |
| W8 boot roster (conditional) | … let the world churn by authored occasion | Narrowed: rung 1 may carry it | 1 may fire (hence rung 1 first); 3: v1 re-added the cut at `forcing-churn:185` without naming it; v2 names it and the open escalation |
| `Receipt.before/after` | … tell "from X to Y" for one act | Narrowed: about 25 act-driven non-existence writes in two seasons (`inventory_out.txt:61-71`, per NERS) | 1: `delta` already exists; hence "fill one, never both" |

### 8.3 E watchlist and E-LEGIBILITY

| Watched | The N it protects | Verdict |
|---|---|---|
| `before/after` beside `delta` | One carrier for the pre-value | Kept as conformance, MEDIUM: two carriers if both survive |
| `source`, `hops-band` dropped | The hearsay voice | Cut until IN-18, MEDIUM |
| Novelty folded into anti-repetition | First-occurrence emphasis | Fold, HIGH |
| C12 folded into a group-by | A per-person starvation view | Fold, MEDIUM |
| `about` key dropped | A document's topic separate from its claim | Cut, MEDIUM: `Said` carries its own subject [INFERRED] |
| C2 deferred | Utterances that say something, including lies | Deferred, MEDIUM: E-3's falsity point stands until a later form binds any Proposition |
| Chroniclers as a lexicon only | P-03's chronicle voice | Limit, MEDIUM |
| Per-season emitter refused | R3's external pressure | Cut, LOW–MEDIUM: FORCE-* owns that N |

E-LEGIBILITY: tiered selection is predictable from state (outcome class, then depth); PASS on shape. The tier order itself is unmeasured.

### 8.4 R

- **R-COMPLETE: FINDINGS.** No carrier for the cause of 296 refusals; rungs have no names; no chronicler exists; MATTER receipts stay partial; the `march` field path is untested.
- **R-VARIETY: FINDINGS, narrowed.** W5 gives each ledger its own journal, repairing v1's shared-reach collapse; but every deep-chain claim is firsthand at 95/100, and 37 persons have no appraisal.
- **R-WORLD: PROVISIONAL.** W4 and W8 rung 1 could add hooks without the player; no run shows a content deposit changing anyone's decision.
- **R-CHOICE: NOT SCORABLE.** The render occupies no seat. Precondition: W5 read by a player at a seat; the instrument is W5's coupling control. W2 would change verbs at every ordinary-person seat with no two-arm artifact yet.

### 8.5 S

| Direction | Carrier or gap |
|---|---|
| Up | W7: settlement aggregation keyed on `place_of(anchor_of(e))` plus ancestry; faction via `faction_q.resolve`. Gap: realm line |
| Down | `chronicle`/`post_remit` deposits (1,266); the journal tells only what the channel supplied |
| Vertical | W7's rule: person acts stay on person pages. Gap: `weight.changed` at CENSUS has no line; season summary |
| Diagonal | `field.won/lost/unopposed`: carrier exists, untested in the run |
| Lateral / horizontal | Occasion edges (804 restored); tellings, n = 4 |
| Pause | ENCOUNTER runs in the same round, so "one act" holds; `march`'s two degrees are rendered as two lines; `TRACE.query` avoided by reading `reach` from snapshots |
| Methodology | One refusal definition (`REFUSAL_KINDS`); one appraisal computation (`deeds_judged`); the three depth readings converge after W3; one pre-value carrier |

S-UP N-A for a render; S-DOWN passes on shape, near zero in the tree (4 tellings).

### 8.6 The design's own falsifier

| Discipline | Hits |
|---|---|
| No render-to-world write | 0 clean; 2 borderline, both handled: `TRACE.query` (snapshots), player coupling (W5 control) |
| The sim produces occurrences, never text | 0 |
| Discrete structure selects the template | 0 (the continuous product is deleted) |
| No storyline carrier in the sim | 0 |
| One owner per rule | 2 borderline, both repaired: journal relevance (reads raised Questions, not `reach`); `supplied_by` read, not copied |
| No per-entity keying | 1 borderline: W8 rung-2 rows name entities |
| No authored content entering the world with no act | 1 borderline: W8 rung 2 |

The hits cluster in one family, *authored content entering the world*, the family NERS found missing from v1's exception list. v2 licenses only its settled member, F.31 boot rows read once by `build_realm` (precedent `populated.py:1262`), and refuses the per-season member.

### 8.7 Backward propagation sweep

Checked in this document, by search after drafting: "1-3 pursuits" survives only in the retraction list; 52 of 52 and M-A carry [MEASURED]; `anchor_of` appears only for actorless Events and as retracted; `uniform` appears only as "constant"; no package has an edge from appraisal to content or from selection to W3; "801 of 1,068" appears once, with its population; the 70.5% carries its definition; D1, D3, D4 and D5 are closed in sections 0 and 7; "four citing docstrings" was found wrong and corrected (section 3.5). Not swept: the v1 file, which was not committed and was left unchanged in S as the superseded record.

### 8.8 Grade

**GRADE: paper.** Execution artifacts that exist: the S outputs (seed 0, two seasons, scratch scripts outside the tree) and the IN-50 counterfactual recorded at `_part4:48`. Nothing in W1–W9 has code, a test or a run. An independent reviewer would add a run of W0(d) on a second seed, a reader outside this session on decisions 1 and 3, and someone to open 04 §A.2, §B.13 and PART E, which neither the reviews nor this writer opened.

## 9. Disposition of review findings

**Verdict.** Every finding is placed. Most are accepted; twelve rows are narrowed; three rows of Fable verdicts are rejected as an ordering, a form or a superseded premise, each with the measurement or citation that rejects it, and one NERS repair is rejected in part; one is out of lane; nothing is deferred without a home. NERS limits are numbered NL-1..NL-8 in the order the audit lists them.

| id | Finding | Disposition | Where | Rejected by |
|---|---|---|---|---|
| L-1 | `anchor_of` returns the actor | ACCEPTED | §3.2; §1.2 item 5 | |
| L-2 | `state_of`/`was` are digests; a new field moves reprs | ACCEPTED | W0(e); W9(a) | |
| L-3 | No chronicler exists | ACCEPTED | §2.3 | |
| L-4 | Order not forced; typing step missing | ACCEPTED | §0; W1; W2 | |
| L-5 | C1's control is false | ACCEPTED | W4 falsifier (b) | |
| L-6 | C2 narrowed | ACCEPTED | W4 (C2 deferred) | |
| L-7 | Appraisal live; `uniform` constant | ACCEPTED | §1.1; W1; §7 | |
| L-8 | C7's product zeroes refusals | ACCEPTED | W1 selection, falsifier 2 | |
| L-9 | Key dimensions near-constant; no enumeration | ACCEPTED | W6 | |
| L-10 | A level predicate re-fires | NARROWED | W8 (per-season form refused; `_crossings` edges in rung 1) | |
| L-11 | Occasion arbitrary or misattributed | ACCEPTED | §3.2; §3.3 rule 5 | |
| L-12 | M-A matches a term; tautological control | ACCEPTED | §1.1 (split measured; control labelled weak); W0(a) | |
| L-13 | Equality as IN-50's falsifier | ACCEPTED | W3 | |
| A-1 | C11 breaks on four ratified points | ACCEPTED | §3.4; W8 | |
| A-2 | Candidate typing missing | NARROWED | W2, carried as a dispute, not as decided conformance | |
| A-3 | Focalization meets §C.11 | ACCEPTED | §2; W5 | |
| A-4 | §B.9 already specifies `before, after` | ACCEPTED | W9(a); §7 | |
| A-5 | Fragment file misplaced; §0.05 misapplied | ACCEPTED | §3.1; W6 | |
| A-6 | Lint fails as a guard | ACCEPTED | W6 | |
| A-7 | Hash falsifier blind to `acts`/`scenes` | ACCEPTED | W1 falsifier 1 | |
| A-8 | Operand binding; D5 closes at test 4 | ACCEPTED | W4; §7 | |
| A-9 | C6 is a second spelling | ACCEPTED | W5; W9(c) | |
| A-10 | C15 wrong owner | ACCEPTED | W1 names; W9(d) | |
| A-11 | Numbers have no home | ACCEPTED | W0; W1 (required arguments) | |
| A-12 | C13 duplicates H-54/`arms.py` | ACCEPTED | W0(f) | |
| E-1 | Render couples through the player | ACCEPTED | §2.2; W5 falsifier 2 | |
| E-2 | Wider aggregation misattributes "why" | ACCEPTED | §3.2; W8 | |
| E-3 | Content on the wrong kind; route to declared kinds; falsity | NARROWED | W2 record-kind half; W4; W8; C2's deferred form | |
| E-4 | C7 arithmetic | ACCEPTED | W1 | |
| E-5 | Key collapses; wrong-kind vs absent unmeasured | ACCEPTED | W6; §1.1 (measured since) | |
| E-6 | Deck pulse; need question starved | ACCEPTED | W8 | |
| E-7 | Appraisal narrowed | ACCEPTED | W1 appraisal | |
| Risk 1 | Hostility after typing | ACCEPTED | §6.1 | |
| Risk 2 | Paper with no sink | ACCEPTED | §6.1 | |
| Risk 3 | Ambitions only grow | ACCEPTED | §6.1 | |
| Risk 4 | Content before typing | ACCEPTED | §6.1; §5 (W4 after W2) | |
| Risk 5 | Evicted antecedents | ACCEPTED | §6.1; §3.3 rule 6 | |
| P-1 | Content reaches nobody | ACCEPTED | W4 handover; §0 | |
| P-2 | Render leaks hidden knowledge | ACCEPTED | §2.1; W5 falsifier 1 | |
| P-3 | Plan contradiction on B-U | ACCEPTED | §5 | |
| P-4 | Typing co-changes; R3 hazard; depth over hidden links | NARROWED | W2 (H-94 constraint kept as a disagreement with A-2); W1 tiers | |
| P-5 | No scale carriers | ACCEPTED | W7 [EXTENSION] | |
| P-6 | End-state reads | ACCEPTED | W0(e); §3.3 rule 6 | |
| P-7 | `delta` vs `prior` | ACCEPTED | W9(a) | |
| P-8 | C11's own writes refused | ACCEPTED | W8 | |
| P-9 | Hops constant; documentary hearsay; staleness | ACCEPTED | §3.3 rules 2-4; W6 | |
| P-10 | Two refusal definitions | ACCEPTED | §1.1; W0(a) | |
| P-11 | Constants in fabrication scope | ACCEPTED | W0; W1 | |
| NERS 1 | Select from the ledger | ACCEPTED | W5 | |
| NERS 2 | Delete C11 | NARROWED | W8 (emitter deleted; boot rows kept behind decision 2) | |
| NERS 3 | Delete C13 | ACCEPTED as a module | W0(f) (measurement kept) | |
| NERS 4 | Delete C12 | ACCEPTED | W8 (group-by) | |
| NERS 5 | Delete C7; the deepest chain is the selection | NARROWED | W1 (outcome tiers before depth, because depth ranks artifacts, A-2) | |
| NERS 6 | Use `deeds_judged` | ACCEPTED | W1 | |
| NERS 7 | Read `REFUSAL_KINDS` | ACCEPTED | W0(a); W6 | |
| NERS 8 | `Person.name` plus `[NAME?]` | ACCEPTED | W1 | |
| NERS 9 | Delete lint and gate | ACCEPTED | W6 | |
| NERS 10 | Drop `source`, `hops-band` | ACCEPTED | W6 | |
| NERS 11 | Delete C4(ii) and D1 | NARROWED | D1 deleted (§7); the field kept as conformance (W9(a)) | "Delete C4(ii)" rejected on 04 §B.9:425 |
| NERS 12 | Route C1 via `said`; drop `about` | ACCEPTED | W4 | |
| NERS 13 | Move C14 | OUT-OF-LANE | §6.2 (telling lane, IN-18) | |
| NERS 14 | Close D1, D3, D4, D5; merge D2 | NARROWED | §7 (D4's location closes; the reading of the ruling stays Jordan's) | |
| NERS 15 | Re-tag stale premises | ACCEPTED | §1 | |
| NL-1 | C6 reads the log | ACCEPTED | W5 | |
| NL-2 | "Why" honest for the actor only | ACCEPTED | §2.1; §3.3 | |
| NL-3 | 296 refusals have no cause | ACCEPTED | §3.2; §8.4 | |
| NL-4 | No chronicler | ACCEPTED | §2.3 | |
| NL-5 | Rung names have no producer | ACCEPTED | W1 (limit) | |
| NL-6 | Appraisal silent for 37 persons | ACCEPTED | W1 | |
| NL-7 | C11's shape is an open escalation | ACCEPTED | §7 item 2 | |
| NL-8 | Fragments not a §0.05 clause-1 artifact | ACCEPTED | §3.1 | |
| NERS typing row | Candidate typing contested | ACCEPTED as a dispute | W2; §7 item 1 | |
| Fable A.1, A.10 | Content first; order substrate → render → deck | REJECTED as an ordering | §0; §5 | `measure_ma2_out.txt:2` (439 of 1,318 kind-mismatched); P-1 (no handover reachable) |
| Fable A.2, A.3 | Refuse injection and scripted beats | ACCEPTED | §3.4 | |
| Fable A.4 | Deck at MATTER/CALENDAR | REJECTED in that form | W8 | `write_matrix.yaml:254-265`; 04 §F.31:1220 |
| Fable A.5 | Baseline delta, narrowed | NARROWED | W0(e); W9(a) | |
| Fable A.6 | Appraisal, non-control arms only | NARROWED | W1 | premise rejected: `fixtures.py:706,708,731` |
| Fable A.7 | Relational salience via `reach` | NARROWED | W5 (`reach` filters claims, not the log) | |
| Fable A.8, A.9 | Discrete templates; attention as roster data | ACCEPTED | W1; W6; W0(f) | |
| Fable E.1, E.5, E.6, E.8 | Retractions and corrections | ACCEPTED | §1.2 | |
| Fable E.2 | D12 measures channels | ACCEPTED | §1.1; §6.2 | |
| Fable E.3, E.4 | Appraisal reading needs a live arm; state-keyed cards | REJECTED (superseded) | §1.2 items 6, 10 | `fixtures.py:706,708` (gains live); `write_matrix.yaml:254-265` (no emitter) |
| Fable E.7, E.9 | Occasion undersold; upheld readings | NARROWED | §3.2 (L-11) | |
| v1 retractions 1-12 | v1 §8 | ACCEPTED, extended | §1.2 | |

## 10. Limits, gaps and provenance

**Verdict.** Every figure is one seed over two seasons; several claims rest on reviews whose sources this writer did not reopen; one upload's hash is unresolved; and nothing proposed here is built.

- **One seed, two seasons.** Seed 0, tree `e6b706d`, `PYTHONHASHSEED=0`, scratch scripts outside the tree. No figure here is a balance claim, and none should fix a parameter before W0(d) repeats it.
- **Nothing built.** No code, test or run exists for W1–W9.
- **Inherited unverified.** 04 §A.2, §B.13 and PART E; `epistemic.py:765-776` (cited through NERS); the ED-IN-0206 row (cited through the archive at `:2381`); `_part4:48`'s hash pair beyond the line itself; `forcing-churn:167,169,185,213` (cited through the reviews); the archived design at `.audit/…/narrative_engine_design_v2_churn.md`; PC-06 at `03_play_surface.md:76-81`; PP provenance generally.
- **What the reviewers did not open** (their own lists): the layer review did not open 04 PART E or §C.6, `epistemic.py:765-776`, the ED-IN-0206 row, `test_g1b_attribution.py`, `S/measure_ma.py`, prose-writer's `SKILL.md` or `_part4:48`; NERS did not reopen v1's four flagged mismatches; no reviewer ran code.
- **The 21 "nowhere" subjects** are not verified as dead persons; the ids only look like it.
- **The nearest-prototype precedent.** The statement that nearest-prototype matching on continuous features is "the oatmeal trap" (Fable A.8, carried into v1) is the orchestrator's inference, not sourced: the cited lines (`research/valoria_game_precedent_companion_v1.md:404-406`) do not mention nearest-prototype matching. The discrete-key choice in W6 rests on legibility and the A-5/A-6 placement, not on that citation.
- **The Third Strand hash.** The uploaded `c63b5daf-third_strand_integrated_proposals.md` is 78,634 bytes, matching the size pinned at `04_PROVENANCE.md:149`; its SHA-256 begins `285a62853b505a68`, while the pin begins `02458c7e`. Either the bytes differ or the pin is wrong. Unresolved [MEASURED by the orchestrator with `sha256sum`].
- **Writer's spot-checks.** About forty citations opened (each marked [CHECKED] where it is used). Mismatches or qualifications: `_part3:303` (the ordering text is at `:190`); `test_u7_own.py:42` (a declined-verb set, not a typing co-edit); `carriers.py:720-723` (mechanism, not the count of 10, which reproduces by search); `verb_table.yaml:959` (`news.untold` is also a refusal kind); "four citing docstrings" (three); `resolve.py:487` against `:489`; and `give` sits in B-R, not B-I.
