# ARCS — cross-cutting adjudication of the provided arcs and characters

## Status: REFERENCE (an adjudication; resolves nothing at runtime)

## Read at: 785bc62 (working tree; `engine/`, `modules/`, `references/` unchanged since 601e715)

Scope: all 143 cases under `engine/season/cases/` (97 in the arc lane, 46 characters), read one by one;
`ENDINGS_CLASSIFIED.yaml`; the five files of `proposals/2026-08-30-arc-reachability/`; the 77 overlay
files under `cases/exercises/`; the instruments (`harness/corpus_run.py`, `run_cases.py`, `exercises.py`,
`arc.py`, `storybar.py`, `gaps.py`). What ran is in §12. What was read in part or not at all is stated
there; a claim resting on a file not opened is marked `[UNVERIFIED]`. Case files are the specification of
what must be simulated, never evidence that it is (§0.05).

## 1. Verdict

**No: as coded the game cannot yet simulate any one of the 143 provided cases as that case, and the
shortest honest path to a first run whose beats arise from persons' acts with no script is Carin Vedel
(NPC-088) on the populated realm, then Vaynard's Wager (ARC-04) as the first arc proper.** Of the 427
core needs, my reading is: 21 represented and reached, 136 declared and not reached, 176 absent, 88 stated
against the ratified shape (an actorless social counter, a faction that decides, a stat lookup in place of
a choice), 6 unclear by the source's own admission (§3, generated table). The engine is nearer than those
numbers suggest in one respect and further in another. Nearer: `harness/populated.py::build_realm` already
seats all 46 provided characters by name with offices, creeds, commitments and authored Thread sensitivity
(probe, §12), so the cast exists; `corpus_run` does not use it and builds a three-seat template instead.
Further: no instrument reads a case's needs against a run (§2), and the chooser ranks a verb without
reading what the act would do (CHAR audit F-CHAR-01), so a character's defining choice has nothing to
arise from. NPC-088 needs three single-owner changes: the case built on the realm with beats and
controls (M-CASE), a second person coming to hold a Record (M-REC), and a held opinion formed from a find
(M-INFO). ARC-04 needs, in addition, the chooser's aim (M-AIM), regard that moves (M-REGARD) and a
hearing that binds (M-SIT). Forty-nine of the 143 cases turn on the Thread (perception or world substrate)
and wait on a decision that is Jordan's (§11).

## 2. The corpus as it is

### 2.1 Census (run: `arcs_work/census.py`, §12)

| lane | cases | by authored `scale:` | need rows | core | important | flavour | rows beginning `UNCLEAR:` |
|---|---|---|---|---|---|---|---|
| ARC | 97 | realm 43 · faction 29 · person 16 · world 9 | 626 | 301 | 283 | 42 | 15 |
| NPC | 46 | person 21 · faction 18 · realm 5 · settlement 1 · world 1 | 346 | 126 | 180 | 40 | 54 |

- Files: `chain/ARC1` 18, `chain/ARC2` 31, `chain/ARC3` 2, `ARC4` 10, `ARC5` 17, `ARC6` 19;
  `chain/NPC1` 8, `NPC2` 9, `NPC3` 10, `NPC4` 10, `NPC5` 9. Six chain files are committed inside a
  markdown fence; `ARC3.yaml` lost 37 lines above its first `- id:` (loader note, `run_cases.py:203-265`).
- The arc lane is five families: numbered arcs (ARC-01..55 with the root series as ARC-R16..R19),
  emergent arcs (EMG-*), narrative scenario chains (NSC-01..09), rules chains (SCN-01..15, SCN-LOOP-A..D)
  and two that are not in-fiction cases (ARC-META-COLLISION, EMG-11). The nineteen SCN cases describe
  rule procedures (combat rounds, Thread operations, clocks), not stories; fifteen of them have no
  chooser demand at all (§9).
- Marked struck by their own source: NSC-01 (`[STRUCK]`) and seven `[STRUCK-MECHANIC]` arcs (ARC-R18,
  -20, -23, -31, -34, -37, -45: the Coup Counter and Niflhel).
- 57 cases declare `faction` or `world`, which are not rung kinds; 57 overlay files re-author the scale to
  `realm` or `duchy` with a stated reason (`corpus_run.py:92-128`). The run uses duchy, person, realm,
  settlement.

### 2.2 What the binders bind (F-CORE-02, verified against the code)

**The builder.** `corpus_run.build_at` (`:467-662`) reads from a case: `scale` (through the overlay),
a case-level `office:`, the `cast:` overlay (`CAST_KEYS = who, role, capability, office, ought`,
`:313`), the integer `temporal.span_seasons` (`:460-464`), `ENDINGS_CLASSIFIED`'s `forced_by_threshold`
(one Date at tick 1 with `holder: None`, `:655-661`), and the text of the first core need, which
`run_cases.wants_of` (`:108-126`) returns as the predicate string of each person's OUGHT. It does not
read `season_requires` as needs, `who_acts`, `knowledge`, `ends_when`, `needs_memory_of` or
`needs_deadline`. Every world is a rung chain, one Site per yielding kind, three or more seats and a
ring of OUGHTs. Confirmed.

**The checks.** `run_case` (`:944-1059`) computes R1 (the seasons ran), R3 (some act's Event has a
cause emitted by another person's act), R4 (same seed, same hash), R5 (fixtures read are registered) and
A1 (span status). None reads a need. Run here, seed 0: `RUNS-UNDECLARED 103 · SPAN-UNAUTHORED 40`;
R1/R3/R4/R5 143 of 143; planted control False→True; `R2`, `A2`, `A3` printed `NOT-COMPUTABLE`.

**The overlay rows.** `exercises.resolve` (`:231-327`) grades a row by its tokens. A verb token passes
when the verb is in `resolvable_verbs()`, that is, when the table row has a predicate and an effect: a
static property of the table, not of the case. A hole token passes unless the register row's `grade:`
string is `absent` (and reads `ASSUMED` on `assumption`). An Event-kind token passes when the kind appears
in any `emits:` column. A probe token passes when a shared probe world passes. **So the 35 bound rows
(32 core, eight NPC cases) are bound to a table reading, a register string or a generic probe; not one
is bound to a run of its own case, and the 611 ARC rows are bound to nothing.** `run_cases`, run here:
NPC 2 BLOCKED · 6 DEGRADED · 38 NOT-ASSESSED; ARC 97 NOT-ASSESSED; probes 64 PASS of 121.

**The cast overlay.** 27 overlay files carry a `cast:`; one entry in the corpus carries a capability
(`NPC-088`, `copying: 3`); `knows:` is refused at load as a new Claim construction site
(`corpus_run.py:384-387`).

**The surface nothing points a case at.** `build_realm(0)` (probe, §12): 83 persons (46 cast, 37
cohorts), 34 offices, 414 rungs, 322 sites, 70 propositions, 148 commitments, 0 dates, 0 docket items, 2
records. Cast persons carry 15 pursuit weights each, stance rows, seeded ledgers, and Thread sensitivity
where the registry authors it (Edeyja 75, Maret Uln 50, Torsvald 35, Almud 28, Vossen 25, Haelgrund 15).
Capability is authored for two. The realm seats Altonia's officers too (`off_katepano`,
`off_kommerkiarios`; `goals.yaml` carries `goal_altonia_conquer_valoria`).

### 2.3 What the corpus run shows about play in these worlds (seed 0, §12)

23 of 67 verbs executed, 13 only refused, 30 never attempted (among them `convene`, `open_case`, `confer`,
`revoke`, `march`, `examine`, `seize`, `succeed`, `thread_read`, `work`). Graded outcomes: Failure 1,552 of
2,152. Claims: firsthand 93,696, `told_by` 64. Sixteen cases name a player the runner does not supply.
These are properties of the template, and they agree in kind with the realm readings the requirement file
records (R-04, R-05 `measured:` blocks: `confer` 70 attempted / 0 executed, `revoke` 15/0, `determine`
20/1, `convene` 12/2, `open_case` 28/7, `issue` 30/6, `found`/`build`/`work` 0; those are the file's
readings, not re-run here).

## 3. Per-case table

**How to read it.** One row per case, core needs only (important and flavour needs were read and inform
§4 and §6; they are not tabulated). Each need carries a status and the mechanism it turns on:

- **R** represented and reached (a code path and a run; evidence in §4's row for that mechanism or named
  below); **D** declared, not reached (a verb, field or roster row exists; no computed run of a case
  reaches it, or it executes only in another world); **A** absent (no carrier, verb or reader);
  **W** wrongly stated against the ratified shape (resolution in §6); **U** the source's own `UNCLEAR:`.
- Mechanism codes are §4's. Every case also needs **M-CASE** (the case built and its beats read).
  Evidence for a status is the mechanism's evidence in §4; where a need's evidence is its own it is
  listed after the table.
- `chooser` is §9's demand code; `evidence` is §10's (V reveal · I investigation · A accusation · T trial
  or hearing; e1–e6 the needs placed on typed evidence and argument).
- The table was generated from the adjudication mapping by `arcs_work/table.py` (scratchpad), which
  checks that every core need of every case is assigned exactly once.

| case | name | scale (as authored→as run) | core needs: status·mechanism (need, first words) | owner lanes | changes required (mechanisms; all also need M-CASE) | chooser | evidence |
|---|---|---|---|---|---|---|---|
| ARC-01 | The Unworked Clause | realm | N1 **W**·M-LATENT (a background/ambient quantity tied to a population's cultural situation…); N2 **D**·M-AIM (a person's genuinely unresolved private ethical question (not a…); N5 **A**·M-PLAYER (players must be able to remove one specific named…); N6 **W**·M-LATENT (when a background track bottoms out in a territory,…) | CHAR, CORE·FA, CORE·GO | M-AIM M-LATENT M-PLAYER | c1c2c8 | — |
| ARC-02 | The Unseeing Eye | person | N1 **D**·M-SEAT (an institution's routine, individually-defensible placement decisions must be able…); N2 **A**·M-PERC (a character must be able to change in a…); N3 **A**·M-PERC (a slow-accumulating exposure quantity tied to routine, unremarkable activity…); N4 **A**·M-PERC (a spontaneous state-change check on a person must be…); N6 **D**·M-INFO (a third party must be able to choose, as…) | CHAR·FI, FA, FI·SC | M-INFO M-PERC M-SEAT | c7c8 | V |
| ARC-03 | The Hammer's Reserve | faction→duchy | N1 **D**·M-AIM (a single named decisive resource (usable once per arc)…); N2 **W**·M-LATENT (two independent counters (one faction's rising standing, an unrelated…); N3 **W**·M-LATENT (a reserved resource's effectiveness must be able to have…); N7 **W**·M-LATENT (firing a reserved resource must be able to produce…) | CHAR, CORE·FA | M-AIM M-LATENT | c1c2 | — |
| ARC-04 | Vaynard's Wager | faction→duchy | N1 **D**·M-AIM (a Non-Player Character must be able to sustain deliberate,…); N2 **A**·M-REGARD (a subordinate's trust/loyalty in a patron must be able…); N3 **D**·M-SIT (a formal accusatory process against a person must be…); N6 **D**·M-AIM (a patron facing a subordinate's public accusation must be…) | CHAR, SC·FA | M-AIM M-REGARD M-SIT | c1c2c6 | AT e4e5 |
| ARC-05 | The Quiet Fracture | world→realm | N1 **A**·M-SUB (a slow, per-action cost on a shared world-substrate resource…); N2 **A**·M-SUB (a background world-scale stat must be able to decay…); N4 **A**·M-SUB (the same tracked world-substrate resource must be able to…); N5 **D**·M-SIT (players must be able to force a stalled, private…) | SC·FA, WR | M-SIT M-SUB | c7c8 | IV |
| ARC-06 | The Debate That Won the Wrong Thing | faction→realm | N1 **D**·M-SIT (a formal contest with a trackable winner must be…); N2 **D**·M-SIT (a losing party in a formal contest must be…); N4 **D**·M-SIT (an implementation action following a political win must be…); N6 **D**·M-AIM (the faction that won the original contest must be…); N7 **W**·M-LATENT (an institution whose formal position was weakened by losing…) | CHAR, CORE·FA, SC·FA | M-AIM M-LATENT M-SIT | c2c5 | T e5 |
| ARC-07 | The Army That Stayed | faction→realm | N1 **D**·M-FIELD (a rare-but-nonzero outcome from an ordinary combat sub-procedure (two…); N2 **A**·M-FIELD (a failed sub-check during combat must be able to…); N3 **A**·M-FIELD (a military commander must be able to be placed…); N5 **D**·M-AIM (resolving the persistent condition must require a distinct, nameable…) | CHAR, MB·PC | M-AIM M-FIELD | c1c7 | I e1 |
| ARC-08 | What the Guilds Know | faction→realm | N1 **D**·M-INFO (a faction must be able to possess an information/intelligence…); N3 **W**·M-LATENT (the faction holding valuable accumulated information must be able…) | CORE·FA, FI·SC | M-INFO M-LATENT | c2c7 | V e1 |
| ARC-09 | The Practitioner Who Stopped | person | N1 **A**·M-PERC (a person's capacity to act as an independent agent…); N2 **D**·M-INFO (a character must be able to conceal an approaching…); N7 **D**·M-SEAT (when a person's hidden state is surfaced to their…) | CHAR·FI, FA, FI·SC | M-INFO M-PERC M-SEAT | c1c7 | IV |
| ARC-10 | The Penitent Duke | realm | N1 **D**·M-SIT (a political actor must be able to construct a…); N4 **A**·M-REC (a character must be able to choose, mid-contest, to…); N6 **D**·M-SIT (a decisive action's degree of success must be able…) | FI·FA, SC·FA | M-REC M-SIT | c2c5 | AT e1e5 |
| ARC-11 | Three Crowns in a Season | realm | N1 **W**·M-LATENT (a ruler facing existential institutional collapse must be able…); N2 **W**·M-CAP (a subordinate administrator's personal flaw (taking on too much)…); N4 **D**·M-INFO (an intermediary reporting to an external power must be…) | CHAR·DICE, CORE·FA, FI·SC | M-CAP M-INFO M-LATENT | c3c4c7 | — |
| ARC-12 | The Chained Ships | realm | N1 **D**·M-STORES (three or more factions must be able to independently…); N2 **A**·M-SUB (a hidden hazard embedded within an economic arrangement must…); N3 **D**·M-INFO (one participant who personally vetted the tainted component must…) | FI·SC, SE·FA, WR | M-INFO M-STORES M-SUB | c2c7 | IV e1 |
| ARC-13 | Wait Until It Sings | realm | N1 **D**·M-SEAT (a faction's default, low-effort defensive behavior must be able…); N3 **W**·M-LATENT (a previously-neutral institution's inertia must be able to become…) | CORE·FA, FA | M-LATENT M-SEAT | c1c5 | — |
| ARC-14 | The Purple Shroud | realm | N1 **W**·M-LATENT (a public-order crisis must be able to require every…); N3 **W**·M-LATENT (a decision-maker's response to an identical offer must be…); N6 **D**·M-REGARD (a marginalized population's spontaneous show of solidarity during an…) | CHAR, CORE·FA | M-LATENT M-REGARD | c2c5c6 | I e1 |
| ARC-15 | The Banker's War | faction→realm | N1 **D**·M-STORES (a faction must be able to simultaneously fund or…); N2 **D**·M-INFO (detecting a hidden financial arrangement must be able to…); N4 **D**·M-INFO (a party that detects a hidden arrangement must be…); N6 **D**·M-INFO (the party that finally exposes a hidden arrangement must…) | FI·SC, SE·FA | M-INFO M-STORES | c1c2c7 | IV e1e6 |
| ARC-16 | The Empty Fort | faction→realm | N1 **D**·M-AIM (a faction leader must be able to deliberately choose…); N2 **D**·M-AIM (an opposing institution's decision to NOT act against a…); N3 **A**·M-REGARD (removing one unit of a spread-out presence must be…); N4 **A**·M-PERC (a specific piece of caste-legitimizing evidence must be able…) | CHAR, CHAR·FI | M-AIM M-PERC M-REGARD | c1c2c6 | — |
| ARC-17 | The Sinigaglia Dinner | faction→realm | N2 **W**·M-LATENT (a superior's response to detecting a subordinate's disloyalty must…); N3 **D**·M-REC (two parties in an adversarial relationship must be able…); N4 **W**·M-LATENT (a subordinate under coercive tolerance must be able to…) | CORE·FA, FI·FA | M-LATENT M-REC | c1c3c6 | IV e1 |
| ARC-18 | The Stolen Steward | realm | N1 **A**·M-CAP (a single administrator's documented psychological vulnerability must be able…); N2 **W**·M-LATENT (small, individually low-cost influence-purchases against the same target must…); N3 **D**·M-INFO (the target's own superior must be able to maintain…); N6 **D**·M-SEAT (a superior's culminating decision about a compromised-but-valuable subordinate must…) | CHAR·DICE, CORE·FA, FA, FI·SC | M-CAP M-INFO M-LATENT M-SEAT | c4c5c7 | I e1 |
| ARC-R16 | The World Without Direction | realm | N1 **R**·— (the world's other power-holders must be able to act…); N2 **D**·M-AIM (each faction's autonomous action must follow a distinct, fixed…); N3 **D**·M-PLAYER (the consequences of several seasons of unattended autonomous action…); N5 **R**·— (there must be a way to attribute an accumulated…) | CHAR, CORE·GO | M-AIM M-PLAYER | c2c4 | — |
| ARC-R17 | The Favour Gate | faction→realm | N1 **D**·M-STORES (a faction that is not a single decision-maker must…); N2 **D**·M-STORES (building a local quantity toward a use-threshold must be…); N3 **W**·M-LATENT (reaching a threshold quantity in one place must unlock…) | CORE·FA, SE·FA | M-LATENT M-STORES | c2c8 | — |
| ARC-R18 | The Tied Vote | realm | N1 **A**·M-SIT (a multi-round formal vote between two competing coalitions must…); N2 **W**·M-LATENT (a tied/failed formal vote must trigger two independent background…) | CORE·FA, SC·FA | M-LATENT M-SIT | c2c5 | T |
| ARC-R19 | The Accounting Sequence | realm | N1 **R**·— (periodic resolution of pending effects must happen in a…); N2 **W**·M-LATENT (when an at-risk quantity drops to a specific low…); N3 **W**·M-LATENT (gains or losses to a single quantity from any…); N4 **R**·— (helping one at-risk holder in a period must be…); N6 **R**·— (an action taken by a player at a small,…) | CORE·FA | M-LATENT | c2c8 | — |
| ARC-20 | The Tutoring Demand | realm | N1 **W**·M-LATENT (a slowly rising background pressure quantity must, on crossing…); N2 **A**·M-REGARD (a person sent away as the compliant response must…); N4 **W**·M-LATENT (the sent person's allegiance hitting its floor must trigger…); N6 **D**·M-FIELD (the eventual mass-combat event's outcome must depend on whether…) | CHAR, CORE·FA, MB·PC | M-FIELD M-LATENT M-REGARD M-SPAN(8) | c1c2c6 | — |
| ARC-21 | The Excommunication | realm | N1 **D**·M-SIT (a single formal contest must support more than two…); N2 **W**·M-LATENT (the institution's best possible outcome must remove a suppression…); N3 **A**·M-REGARD (a failed formal challenge against a power-holder must weaken…); N4 **W**·M-LATENT (crossing an accumulating threshold on the spiking background quantity…) | CHAR, CORE·FA, SC·FA | M-LATENT M-REGARD M-SIT | c2c5 | AT e5 |
| ARC-22 | The Ceiral Ritual | world→realm | N1 **A**·M-SUB (several independent long-running preparation tracks (a held object, a…); N3 **A**·M-SUB (the operation must resolve via one roll with at…); N4 **A**·M-SUB (the worst outcome degree must spawn a persistent hostile…) | WR | M-SUB | c2c8 | — |
| ARC-23 | The General Falls | realm | N1 **A**·M-FIELD (a battle must have discrete resolution phases within a…); N2 **W**·M-CAP (whether any character has invested in a specific, rarely-used…); N3 **A**·M-FIELD (a commander's incapacitation must impose an immediate structural penalty…); N4 **A**·M-FIELD (failing to stabilize must escalate to a second, worse…); N5 **D**·M-AIM (a standing threat/threshold that exists only because one specific…) | CHAR, CHAR·DICE, MB·PC | M-AIM M-CAP M-FIELD | c2 | — |
| ARC-24 | The Faction That Breaks | realm | N1 **W**·M-LATENT (an institution's overall health quantity reaching its floor must…); N2 **D**·M-SEAT (the specific shape of the fracture must depend on…); N4 **W**·M-LATENT (a collapsed institution's role in driving a background world-quantity…) | CORE·FA, FA | M-LATENT M-SEAT | c2c6 | — |
| ARC-25 | The Schoenland Pivot | realm | N1 **D**·M-ABROAD (a neutral third-party actor must independently evaluate several unrelated…); N2 **R**·M-INFO (that actor's read must depend only on externally visible…); N3 **W**·M-LATENT (the chosen alignment must change the ongoing rate of…) | CORE·FA, WR·FA | M-ABROAD M-LATENT | c2c3 | — |
| ARC-26 | The Duke Awakens | person | N1 **A**·M-PERC (an NPC's own repeated, self-directed institutional actions must silently…); N2 **A**·M-PERC (crossing a threshold on that hidden quantity must trigger…); N3 **D**·M-INFO (the failure branch must produce behavior that is objectively…) | CHAR·FI, FI·SC | M-INFO M-PERC | c3 | — |
| ARC-27 | The Dissolution | world→realm | N1 **A**·M-SUB (a single declared operation must resolve to at least…); N2 **A**·M-PERC (even the best possible outcome must produce a passive…); N3 **A**·M-SUB (the worst outcome must spawn a hostile entity in…); N4 **A**·M-SUB (the ambient world-health quantity's pre-existing band must change what…) | CHAR·FI, WR | M-PERC M-SUB | c2 | — |
| ARC-28 | Vaynard -- The Reckoner Who Saw the Sum | person | N1 **W**·M-PERC (a character's internal capability-cost quantity must be able to…); N2 **A**·M-INFO (after crossing that threshold, the character's communication to others…); N3 **A**·M-PERC (the transformed character must retain full continuity of prior…) | CHAR·FI, FI·SC | M-INFO M-PERC | c7 | — |
| ARC-29 | Almud -- The King at the Limit of Order | realm | N1 **D**·M-SEAT (a formal head-of-state role must be able to be…); N2 **D**·M-SEAT (a head of state who remains in his role…) | FA | M-SEAT | c2c5 | — |
| ARC-30 | Lenneth -- What She Finally Understood | person | N1 **A**·M-PERC (a long-concealed identity/capability must remain undetectable to non-specialist observers…); N3 **A**·M-PERC (discovery of the transformation by one specific, relationally-close character…) | CHAR·FI | M-PERC | c7 | V |
| ARC-31 | The Quaestio of Baralta | realm | N1 **A**·M-SIT (a formal, multi-exchange debate procedure must be interruptible by…); N2 **W**·M-LATENT (the tribunal's win/lose outcome for the challenger must apply…); N3 **W**·M-LATENT (a private, unshared threshold maintained by one specific NPC…) | CORE·FA, SC·FA | M-LATENT M-SIT | c1c2 | AT e4 |
| ARC-32 | Vaynard's Confession | faction→realm | N1 **A**·M-PERC (a faction leader's private capability track must reach a…); N2 **D**·M-INFO (an institutional surveillance track targeting a specific individual must…) | CHAR·FI, FI·SC | M-INFO M-PERC | c3c5 | IAT e4 |
| ARC-33 | The Forgetting Road | realm | N1 **A**·M-PERC (a location must be able to strip a person's…); N2 **A**·M-PERC (knowledge or procedure gained inside such a memory-stripping zone…); N3 **W**·M-LATENT (a successful, player-desired outcome achieved via this zone must…) | CHAR·FI, CORE·FA | M-LATENT M-PERC | c2 | — |
| ARC-34 | Ehrenwall's Count | realm | N1 **W**·M-LATENT (a private, monotonically-increasing counter held by a single actor…); N2 **D**·M-SIT (that counter reaching its ceiling must issue a formal…) | CORE·FA, SC·FA | M-LATENT M-SIT | c1c2c5 | — |
| ARC-35 | The Klapp Threshold | faction→realm | N1 **A**·M-PERC (a senior official's long, routine, in-role activity must be…); N2 **A**·M-PERC (that check's success must produce a genuinely destabilizing personal…); N3 **W**·M-LATENT (an internal leadership crisis inside an institution, invisible to…) | CHAR·FI, CORE·FA | M-LATENT M-PERC | c2c7 | T e4 |
| ARC-36 | The Tithe That Fed the Enemy | faction→realm | N1 **D**·M-STORES (an NPC pursuing a fixed optimization objective must be…); N2 **W**·M-LATENT (a slow-eroding, per-location cultural/loyalty value must silently accumulate downward…); N3 **D**·M-INFO (an institution's investigative branch, on detecting the derivative marker,…) | CORE·FA, FI·SC, SE·FA | M-INFO M-LATENT M-STORES | c4c5 | I |
| ARC-37 | The Heresy in the Warehouse | faction→realm | N1 **A**·M-SUB (a legitimate, ordinary supply chain must carry a good…); N4 **D**·M-INFO (a separate investigator working an unrelated case must be…) | FI·SC, WR | M-INFO M-SUB | c3c7 | IV e1e2 |
| ARC-38 | The Sandcastle Alliance | realm | N1 **W**·M-LATENT (two agents belonging to rival external powers, with no…); N2 **A**·M-ABROAD (each shielding agent's suppression must be revocable by a…) | CORE·FA, WR·FA | M-ABROAD M-LATENT | c2c4 | — |
| ARC-39 | The Practitioner They Didn't Know They Had | faction→realm | N1 **A**·M-PERC (a leader's repeated, intentional use of a specific asset…); N2 **A**·M-PERC (that hidden quantity crossing a threshold must trigger a…) | CHAR·FI | M-PERC | c3c7 | — |
| ARC-40 | The Weight That Broke the Balance | realm | N1 **W**·M-LATENT (a wealthy faction's own internal optimization must independently and…); N2 **D**·M-STORES (when several independent external-pressure collapses occur in temporal proximity,…); N5 **W**·M-LATENT (the near-simultaneous failure of several independent stabilizing mechanisms must…) | CORE·FA, SE·FA | M-LATENT M-STORES | c2c6 | — |
| ARC-41 | The Inquisitor's Unravelling | faction→realm | N1 **A**·M-PERC (a hidden personal capability in a loyal enforcer must…); N3 **D**·M-REC (an enforcer's positive, valued professional trait (rigorous documentation) must,…); N4 **D**·M-INFO (a third party who can independently verify the enforcer's…) | CHAR·FI, FI·FA, FI·SC | M-INFO M-PERC M-REC | c3c7 | IV e1 |
| ARC-42 | The Debate That Changed the World | realm | N4 **A**·M-SUB (the debate's outcome, regardless of which side wins, must…); N5 **D**·M-SIT (this debate must be unable to occur meaningfully until…) | SC·FA, WR | M-SIT M-SUB | c5 | T e1e2 |
| ARC-43 | The Battle That Ate the South | world→realm | N1 **D**·M-FIELD (a purely conventional mass-combat engagement must be triggerable because…); N2 **A**·M-SUB (any reality-altering ability used specifically within a large-scale, multi-unit…); N3 **A**·M-SUB (the pre-existing local condition of an ambient world-health quantity…) | MB·PC, WR | M-FIELD M-SUB | c2 | — |
| ARC-44 | The Invisible Majority | realm | N1 **W**·M-LATENT (a per-location cultural-allegiance quantity must be capable of eroding…); N2 **D**·M-SEAT (a designated institutional mechanism built specifically to block structural…) | CORE·FA, FA | M-LATENT M-SEAT M-SPAN(16) | c5 | — |
| ARC-45 | The Tutoring Demand That Started a War | realm | N1 **D**·M-INFO (a formal, threshold-triggered diplomatic demand must remain permanently suppressed…); N2 **W**·M-LATENT (both formal responses available to the demand must each…) | CORE·FA, FI·SC | M-INFO M-LATENT | c2c7 | — |
| ARC-META-COLLISION | Root/gm_ref arc-numbering collision (16-18) | world→realm | N1 **R**·— (the arc-indexing scheme must be able to disambiguate two…); N2 **R**·— (the same disambiguation must hold for Arc 17 (root:…) | — | none beyond M-CASE | c0 | — |
| EMG-10 | The Endgame Configuration (nine simultaneous conditions) | realm | N1 **W**·M-LATENT (nine named conditions, each belonging to a different subsystem…); N2 **D**·— (the game must be able to evaluate "at least…); N3 **W**·M-LATENT (at least one of the nine conditions (a private…) | CORE, CORE·FA | M-LATENT — | c0 | — |
| EMG-11 | 'Throughline resolution' — closing cross-system design-integration gaps | realm | N1 **R**·— (when multiple independent progress-clocks are scheduled to change state…); N2 **A**·M-SEAT (a finite, per-location capacity must be able to gate…) | FA | M-SEAT | c0 | — |
| ARC-46 | The Quiet Seizure | faction→realm | N1 **W**·M-LATENT (an institution's standing quantity must be able to increase…); N2 **W**·M-LATENT (an actor must be able to attempt, once per…); N3 **W**·M-LATENT (failing that counter-action must be able to cost the…); N5 **W**·M-LATENT (when the automatically-growing standing quantity crosses a set level,…) | CORE·FA | M-LATENT | c2c5 | — |
| ARC-47 | The Counter She Keeps | faction→realm | N1 **W**·M-LATENT (a hidden counter, invisible to players by default, must…); N2 **W**·M-LATENT (each of the counter's triggering conditions must be able…); N3 **D**·M-INFO (the counter's current value must be able to stay…) | CORE·FA, FI·SC | M-INFO M-LATENT | c1c7 | — |
| ARC-48 | The Practitioner Economy | world→realm | N1 **A**·M-SUB (an ambient world-quality quantity must be able to decrease…); N2 **A**·M-SUB (that ambient quantity must be organized into contiguous bands…); N3 **A**·M-SUB (an increase in a category of action's difficulty must…) | WR | M-SUB | c2 | — |
| ARC-49 | The Mediator's Debt | faction→realm | N1 **A**·M-CAP (an actor's institutional/ethical alignment must be able to grant…); N2 **W**·M-LATENT (a faction's separate systemic ability (unrelated to the contested…) | CHAR·DICE, CORE·FA | M-CAP M-LATENT | c5 | — |
| ARC-50 | The Counter That Runs Backward | faction→realm | N1 **W**·M-LATENT (a faction's personal advancement/independence track must be able to…); N4 **D**·M-INFO (the side-effect's existence must be discoverable only through a…) | CORE·FA, FI·SC | M-INFO M-LATENT | c7 | I |
| ARC-51 | The Weight of Sight | person | N1 **A**·M-PERC (a character must be able to repeatedly advance a…); N2 **A**·M-PERC (the perception-scale stat must be able to cross multiple…); N3 **A**·M-CAP (a character's capability-to-act stat, separate from the perception stat,…); N5 **W**·M-CAP (a scenario must be able to arise where a…) | CHAR·DICE, CHAR·FI | M-CAP M-PERC | c2 | — |
| ARC-52 | Parliament as Weather | realm | N1 **W**·M-LATENT (a quantity must be able to accumulate from the…); N2 **W**·M-LATENT (when that aggregate quantity reaches its ceiling, the system…); N3 **W**·M-LATENT (stopping the aggregate quantity's rise must be able to…) | CORE·FA | M-LATENT | c0 | — |
| ARC-53 | The Wound Economy | person | N1 **D**·M-FIELD (damage taken by an individual character in a personal-scale…); N2 **W**·M-LATENT (when a character holding a leadership role acts at…); N4 **W**·M-LATENT (a failed faction-scale action must be able to cost…); N6 **R**·M-FIELD (there must be a discrete recovery action, distinct from…) | CORE·FA, MB·PC | M-FIELD M-LATENT | c2 | — |
| ARC-54 | What The Unaffiliated Know | faction→realm | N1 **A**·M-PERC (a character's ongoing use of a personal ability must…); N2 **D**·M-INFO (an institution with a distributed network of observers must…); N3 **R**·M-INFO (an actor must be able to spend a specific…); N4 **A**·M-PERC (the profile an institution builds about a sensitive individual…) | CHAR·FI, FI·SC | M-INFO M-PERC | c3c7 | I e2 |
| ARC-55 | The Withdrawal | faction→realm | N1 **W**·M-LATENT (a non-player faction's ability to use one of its…); N2 **W**·M-LATENT (that gating standing value must be able to move…); N3 **W**·M-LATENT (crossing below the gating floor must be able to…); N4 U (UNCLEAR: no mechanism is specified anywhere in the source…) | CORE·FA | M-LATENT | c0 | — |
| EMG-C1 | The Coup That Wasn't Supposed to Happen | realm | N1 **W**·M-LATENT (an actor's readiness to act must be able to…); N2 **W**·M-LATENT (a change of state in an unrelated area (e.g.…); N3 **D**·M-SEAT (crossing the accumulation threshold must trigger a state change…) | CORE·FA, FA | M-LATENT M-SEAT | c1c5 | — |
| EMG-C2 | The Vaynard Revelation Cascade | realm | N1 **D**·M-AIM (repeated interaction between a player and a single non-player…); N2 **W**·M-LATENT (an actor's private understanding advancing must be able to…); N4 **D**·M-SIT (a hostile institution's investigation of a suspected violation must…) | CHAR, CORE·FA, SC·FA | M-AIM M-LATENT M-SIT | c2c8 | IAT |
| EMG-C3 | The Invisible Drain (Niflhel and the Rising Thread) | world→realm | N1 **A**·M-SUB (a hidden actor's routine operation must be able to…); N2 **A**·M-SUB (the degrading shared resource must be able to fall…); N3 **A**·M-SUB (players must be able to choose not to investigate…) | WR | M-SUB M-SPAN(9) | c8 | I |
| EMG-C4 | The Axis 9 Resolution (Thread Truth Goes Public) | realm | N3 **W**·M-LATENT (the accumulation of several independent conditions (personal degradation reaching…); N5 **D**·M-SIT (the highest political authority must be forced to take…); N6 **A**·M-SIT (the constitutional-crisis-level proceeding must be resolvable through a structured…) | CORE·FA, SC·FA | M-LATENT M-SIT M-SPAN(10) | c5c8 | T e5 |
| EMG-X5 | The Brittle Peace | faction→realm | N1 **A**·M-SUB (a deliberate action that succeeds at making an agreement…); N2 **W**·M-LATENT (an agreement's hidden fragility must remain dormant until a…); N3 **D**·M-REC (when a fragile agreement fails under stress, its status…) | CORE·FA, FI·FA, WR | M-LATENT M-REC M-SUB | c3 | — |
| EMG-X6 | The Tribunal and the Temporal Shimmer | faction→realm | N1 **D**·M-SIT (a formal proceeding must be able to strip one…); N4 **A**·M-PERC (an especially decisive evidentiary victory margin within the proceeding…) | CHAR·FI, SC·FA | M-PERC M-SIT | c5 | AT e1e4 |
| EMG-X7 | The Rendering Debt | person | N1 **A**·M-PERC (repeated use of a powerful capability across successive rounds…); N3 **A**·M-FIELD (a leadership or command role within the structured conflict…); N7 **A**·M-PERC (the cumulative personal cost must have an absolute floor…) | CHAR·FI, MB·PC | M-FIELD M-PERC | c2 | — |
| EMG-X8 | The Temporal Window | world→realm | N1 **A**·M-SUB (a specific powerful capability must be categorically impossible while…); N2 **R**·M-INFO (knowledge that the capability has become available must not…); N3 **A**·M-SUB (using the powerful capability must require satisfying several independent,…); N6 **A**·M-PERC (a successful use of the capability must be able…) | CHAR·FI, WR | M-PERC M-SUB M-SPAN(9) | c2c7 | — |
| NSC-01 | The Hunting Accident (~218 AG) | realm | N1 **D**·M-INFO (multiple independent factions must each be able to hold…); N2 **A**·M-INFO (a full, correct reconstruction of the past event must…); N3 **R**·M-INFO (acting on a partial or incomplete investigation must be…) | FI·SC | M-INFO | c3c7c8 | IAV e1e2e3 |
| NSC-02 | Almud's Sympathies — The Sovereign Constraint | realm | N1 **D**·M-AIM (a ruling actor's continued inaction on a matter must…) | CHAR | M-AIM | c1c2 | — |
| NSC-03 | Baralta and the Solmund Claim | realm | N1 **A**·M-SIT (a political actor's standard legal-authority claim must be augmentable…); N3 **D**·M-SIT (a claim that a ruling authority's foundational legitimacy narrative…) | SC·FA | M-SIT | c2c5 | AT e1 |
| NSC-04 | Niflhel Exposes the Church | faction→realm | N1 **A**·M-INFO (exposing an institutional actor's secret partnership with a criminal…) | FI·SC | M-INFO | c7c8 | IAT e1e2e5 |
| NSC-05 | Torben in Altonia — The Loyalty Clock | realm | N1 **A**·M-REGARD (a person held by a foreign power must have…); N4 **W**·M-LATENT (the held person's allegiance crossing one specific band must…); N5 **D**·M-FIELD (forcibly retrieving the held person against the holding power's…) | CHAR, CORE·FA, MB·PC | M-FIELD M-LATENT M-REGARD | c2c6 | — |
| NSC-06 | Elske — The Royal Fate | realm | N1 **A**·M-INFO (a person's decision to align with an approaching faction…) | FI·SC | M-INFO | c3c6 | e1 |
| NSC-07 | The Southernmost Spiral | world→realm | N2 **A**·M-SUB (sustained neglect of a repeatable stabilizing action across a…); N5 **A**·M-SUB (a culminating ritual attempt at the degraded structure must…); N6 **A**·M-SUB (the culminating ritual's outcome must resolve to one of…) | WR | M-SUB | c2 | — |
| NSC-08 | Ehrenwall's Coup — The Löwenritter Threshold | realm | N1 **W**·M-LATENT (a specific institutional actor must maintain a private, not-directly-visible…); N2 **W**·M-LATENT (the private readiness counter must be irreversible — once…); N4 **D**·M-SEAT (the ruling authority's two possible responses to the ultimatum…) | CORE·FA, FA | M-LATENT M-SEAT | c1c5c8 | — |
| NSC-09 | Vaynard — From Acquisition to Dangerous Knowledge | faction→realm | N2 **W**·M-LATENT (each stage of the actor's advancing understanding must automatically…); N5 **D**·M-AIM (the actor's advancing understanding must culminate in a stage…) | CHAR, CORE·FA | M-AIM M-LATENT | c2c3 | — |
| SCN-01 | A specialized practitioner enters combat | person | N1 **A**·M-SUB (A character must be able to hold two mutually…); N3 **A**·M-SUB (A single triggering roll for the special action must…); N4 **A**·M-SUB (Once a special contact/channel state is established, it must…) | WR | M-SUB | c0 | — |
| SCN-02 | A resource-costly action's full consequence chain | person | N1 **A**·M-SUB (The engine must support several distinct sub-actions within one…); N2 **A**·M-SUB (At least one sub-action's outcome table must impose a…); N3 **A**·M-SUB (The shared currency crossing two different low thresholds on…); N6 **A**·M-SUB (A single aggregate roll must fire once per multi-action…) | WR | M-SUB | c0 | — |
| SCN-03 | The combat wound chain | person | N1 **D**·M-FIELD (Damage must be trackable via discrete milestone crossings of…); N5 **A**·M-SUB (Reaching incapacitation must be able to immediately and forcibly…) | MB·PC, WR | M-FIELD M-SUB | c0 | — |
| SCN-04 | A social conflict escalates into a faction-level consequence | faction→realm | N2 **D**·M-REGARD (A single-roll persuasion attempt's difficulty must be dynamically derived…); N5 **A**·M-SIT (A specific sub-action available within the contested exchange must…); N6 **A**·M-SIT (The stress resource reaching zero must impose a recurring,…); N8 **W**·M-LATENT (Any personal-scale roll made in a social scene must…) | CHAR, CORE·FA, SC·FA | M-LATENT M-REGARD M-SIT | c2 | T |
| SCN-05 | A character's convictions convert into a spendable resource | person | N1 **A**·M-CAP (A character must be able to hold a small…); N4 **A**·M-CAP (The converted spendable resource must be usable to buy…); N5 **A**·M-SIT (A specific sub-action belonging to a DIFFERENT case (a…) | CHAR·DICE, SC·FA | M-CAP M-SIT | c0 | — |
| SCN-06 | A hazard-event forms and drains the world | realm | N1 **A**·M-SUB (At least four different failure conditions belonging to OTHER,…); N2 **A**·M-SUB (The severity tier of a newly-spawned hazard must be…); N4 **A**·M-SUB (An unresolved instance of the full hazard must impose…); N9 **A**·M-SUB (The system must be able to sum multiple independent…) | WR | M-SUB | c0 | — |
| SCN-07 | An individual practitioner's stability degrades in bands | person | N1 **A**·M-PERC (A per-character resource must start at a fixed ceiling…); N2 **A**·M-PERC (The resource must have NO passive or automatic recovery…); N3 **A**·M-PERC (The resource's current value must be divisible into at…); N5 **A**·M-PERC (The lowest defined value (0) must be a distinct…) | CHAR·FI | M-PERC | c0 | — |
| SCN-08 | Three world clocks cross-feed each other | realm | N1 **W**·M-LATENT (At least three independent numeric clocks must run in…); N3 **W**·M-LATENT (A clock crossing a threshold must introduce an ongoing…); N5 **W**·M-LATENT (When ALL of a fixed set of clocks are…); N6 **W**·M-LATENT (Each clock must independently support at least three ordered…) | CORE·FA | M-LATENT | c0 | — |
| SCN-09 | The terminal decline of the world-health currency | realm | N1 **A**·M-SUB (A shared currency's lowest band must activate SEVERAL simultaneous,…); N4 **A**·M-SUB (Exiting this band's terminal spiral must require satisfying MULTIPLE…); N5 **A**·M-SUB (One of those structural exit conditions must itself be…); N6 **A**·M-SUB (A restorative action's WORST outcome branch must apply a…) | WR | M-SUB | c0 | — |
| SCN-10 | An entity whose existence is itself a sustained action | person | N1 **A**·M-PERC (An NPC-type entity's perceptibility must vary continuously across at…); N4 **A**·M-PERC (Taking a wound must cost this entity type a…); N5 **A**·M-PERC (A single terminal-sequence trigger must fire from EITHER of…); N6 **A**·M-PERC (Once triggered, the terminal sequence must run as a…) | CHAR·FI | M-PERC | c0 | — |
| SCN-11 | An external pressure clock accrues from many sources toward invasion | realm | N1 **W**·M-LATENT (A single clock must accrue from at least five…); N5 **W**·M-LATENT (The clock's maximum value must trigger an unconditional, irreversible…); N6 **W**·M-LATENT (At least three structurally different decrease paths must exist…) | CORE·FA | M-LATENT | c0 | — |
| SCN-12 | A succession crisis branches into distinct resolution paths | faction→realm | N1 **D**·M-SEAT (A single succession decision must present multiple, mutually exclusive…); N2 **D**·M-REC (One resolution path must trade an immediate, present-tense benefit…); N7 **W**·M-LATENT (A coup-availability condition must be gated behind a DIFFERENT…) | CORE·FA, FA, FI·FA | M-LATENT M-REC M-SEAT | c2c5 | T |
| SCN-13 | Multiple practitioners act as one on a shared operation | person | N1 **A**·M-SUB (Multiple independent actors must be able to jointly target…); N2 **A**·M-SUB (All designated participants must roll the SAME gating step…); N4 **A**·M-SUB (Each helper's contribution to the anchor's pool must be…); N5 **A**·M-SUB (A participant's own pre-existing personal commitment must be able…) | WR | M-SUB | c0 | — |
| SCN-14 | A personal action interleaves with a mass-scale battle | faction→realm | N1 **A**·M-FIELD (A personal-scale action must be declarable and resolvable WITHIN…); N3 **A**·M-FIELD (An actor holding a mass-scale command role, upon choosing…); N4 **A**·M-SUB (The SAME action-category used at the personal scale elsewhere…); N5 **A**·M-SUB (That same action-category's resource-cost FORMULA must be swappable based…) | MB·PC, WR | M-FIELD M-SUB | c0 | — |
| SCN-15 | Two resolution modes collide over the same target | faction→realm | N1 **A**·M-FIELD (Two structurally different resolution modes (a roll-based personal mode…); N2 **A**·M-FIELD (The combined resolution of both modes' attempts must support…); N3 **A**·M-SUB (In ALL THREE outcome shapes, resource costs to the…); N5 **D**·M-FIELD (An individual character must be able to OPT IN…) | MB·PC, WR | M-FIELD M-SUB | c0 | — |
| SCN-LOOP-A | The self-worsening spiral toward world-currency collapse | realm | N1 **A**·M-SUB (The loop's root trigger (a practitioner's own choice to…); N2 **A**·M-SUB (Once the shared currency crosses a specific threshold, the…); N5 **W**·M-LATENT (A specific institution's own COUNTER-MECHANISM against the loop's root…) | CORE·FA, WR | M-LATENT M-SUB | c0 | — |
| SCN-LOOP-B | One institution's rise removes the counter-pressure against it | realm | N2 **W**·M-LATENT (A rising metric crossing one threshold must trigger an…); N4 **W**·M-LATENT (A rival institution's resource, once reduced by the above,…) | CORE·FA | M-LATENT | c0 | — |
| SCN-LOOP-C | A practitioner's degrading stability erodes the relationship that could save it | person | N2 **A**·M-PERC (The resource crossing a specific band must impose a…); N3 **A**·M-PERC (The resource's degradation must be able to propagate OUT…); N4 **A**·M-REGARD (That second character's relational resource, once sufficiently strained, must…); N6 **A**·M-PERC (Reaching the resource's absolute floor must trigger a distinct,…) | CHAR, CHAR·FI | M-PERC M-REGARD | c0 | — |
| SCN-LOOP-D | A destabilizing world-state opens a window that its own consequences can close | realm | N1 **A**·M-SUB (A shared world-condition metric's own RISE (framed elsewhere as…); N4 **A**·M-SUB (A specific group's OWN deliberate, dedicated action must be…); N5 **W**·M-LATENT (That SAME specific group's own separate institutional-standing resource must…); N6 **W**·M-LATENT (That group's institutional-standing resource crossing its OWN floor must…) | CORE·FA, WR | M-LATENT M-SUB | c0 | — |
| NPC-088 | Carin Vedel | person | N1 **R**·M-REC (A person holding no office, post, or command must…); N2 **D**·M-REC (The physical product of her labor (a copied text)…); N3 **A**·M-REC (Simply possessing the product of her labor must be…); N5 **R**·— (A person with no faction rank, no assigned Duty,…); N7 **A**·M-REC (A person with no political voice must be able…); N9 **R**·M-REC (The engine must represent something about a season of…) | FI·FA | M-REC | c2c3 | IV e1 |
| NPC-087 | Uwe Askeland | person | N1 **D**·M-CAP (A person with no office must be able to…); N2 U (The material he teaches must be classified as suppressed…); N4 **D**·M-AIM (His discovery must be able to branch three ways…); N6 **R**·— (He must be reachable by a scene opportunity despite…) | CHAR, CHAR·DICE | M-AIM M-CAP | c7 | V e1 |
| NPC-086 | Joren Bergvall | person | N1 **D**·M-REC (A technical specialist's field data must be able to…); N2 **D**·M-INFO (Presenting his evidence to a political audience must be…); N7 **D**·M-INFO (Corroborating or refuting his claim must be possible for…) | FI·FA, FI·SC | M-INFO M-REC | c2c7 | IV e1e2e6 |
| NPC-075 | Orm | person | N1 **D**·M-AIM (A person's decision to continue an exhausting, unrewarded maintenance…); N2 **A**·M-SUB (A practitioner's ongoing exposure to the substrate damage he…); N3 **A**·M-SUB (His death, if it occurs while performing a repair,…); N5 **A**·M-SUB (The cumulative consequence of every other faction's warfare and…) | CHAR, WR | M-AIM M-SUB | c1c2 | — |
| NPC-005 | Sigrid Torsvald | person | N1 **D**·M-INFO (An act she performs must be able to leave…); N2 **W**·M-LATENT (An act that goes partially wrong must be able…); N3 **D**·M-REGARD (Her private reputation among people who can never publicly…); N4 **D**·M-PERC (A perception or capability she secretly has (Thread Sensitivity)…); N6 **A**·M-PERC (Her perception of the consequences of a mission must…) | CHAR, CHAR·FI, CORE·FA, FI·SC | M-INFO M-LATENT M-PERC M-REGARD | c4c7 | V |
| NPC-010 | Dalla Virke | person | N1 **D**·M-INFO (A non-faction, non-institutional actor must be able to hold…); N2 **R**·M-INFO (Information she sells must be able to be true,…); N3 **D**·M-AIM (She must be discoverable, killable, buyable, or turnable by…); N4 **D**·M-REC (Her personal judgment about a specific past transaction (vetting…) | CHAR, FI·FA, FI·SC | M-AIM M-INFO M-REC | c2c7 | IV e3 |
| NPC-012 | Rikard Solberg | person | N1 **A**·M-CAP (A single office-holder's personal, unstated motive must be able…); N2 **A**·M-ABROAD (His employer's institutional evaluation of him must be able…); N3 **A**·M-INFO (A player who identifies his true motive must be…) | CHAR·DICE, FI·SC, WR·FA | M-ABROAD M-CAP M-INFO | c3c4c8 | — |
| NPC-002 | Maret Uln | person | N1 **A**·M-SUB (Performing a Thread operation as part of ordinary intelligence…); N2 **D**·M-CAP (As her personal condition degrades across a season, the…); N3 **A**·M-CAP (Her personal sympathy for a population she is ordered…) | CHAR·DICE, WR | M-CAP M-SUB | c4c6 | — |
| NPC-004 | Sæmund Haelgrund | person | N1 **D**·M-INFO (A completed investigation must be able to produce a…); N2 **A**·M-PERC (A person must be able to possess a perceptual…); N3 **A**·M-PERC (A second person with the right capability must be…) | CHAR·FI, FI·SC | M-INFO M-PERC | c3 | IA e3e6 |
| NPC-033 | Kolbrun Thale | faction→realm | N1 **D**·M-SEAT (An office must be able to be the sole…); N2 **D**·M-INFO (A spymaster must be able to surface a hidden…) | FA, FI·SC | M-INFO M-SEAT | c5c7 | I |
| NPC-083 | Hedda Kronvald | settlement | N1 **D**·M-STORES (A governor must be able to spend a limited,…); N2 **A**·M-STORES (Each administrative action must be resolvable by more than…); N3 **D**·M-SEAT (The governor's controlling authority must be able to issue…); N4 **D**·M-STORES (The settlement itself must be able to generate demands…); N8 U (UNCLEAR / structural: the mechanics this case depends on…) | FA, SE·FA | M-SEAT M-STORES | c2c5 | — |
| NPC-008 | Peder Almstedt | faction→realm | N1 **A**·M-SEAT (A bureaucratic office-holder must be able to make any…); N3 **A**·M-SEAT (A person seeking institutional change must be able to…); N4 **D**·M-REC (An office-holder must be able to hold institutional memory…) | FA, FI·FA | M-REC M-SEAT | c5 | T e1 |
| NPC-038 | Arnlod Olafsson | faction→realm | N1 **D**·M-SEAT (An institution's investigative-and-punitive branch must have a single named…); N3 **D**·M-INFO (The superior's own hidden compromising connection must be discoverable…) | FA, FI·SC | M-INFO M-SEAT | c5 | IA e1 |
| NPC-013 | Aldric Tormann | faction→realm | N1 **D**·M-STORES (An office-holder must be able to take a repeatable…); N2 **W**·M-LATENT (That same action must automatically and simultaneously degrade a…) | CORE·FA, SE·FA | M-LATENT M-STORES | c4c5 | — |
| NPC-007 | Annika Feldhaus | faction→realm | N1 **W**·M-LATENT (A faction representative must be able to repeatedly grow…); N2 **A**·M-SUB (An economic actor's supply chain must be able to…); N3 **D**·M-REC (Two separate economic actors who each independently built one…) | CORE·FA, FI·FA, WR | M-LATENT M-REC M-SUB | c4 | IV |
| NPC-071 | Torvi Heljason | person | N1 **A**·M-SEAT (A ruler's formal legal advisor must be able to…); N2 **A**·M-INFO (An advisor whose sole articulated commitment is precedent and…); N4 U (UNCLEAR: the source never specifies what her office of…); N5 U (UNCLEAR: no goal, ambition, leverage (wants/fears/secret), or relationship is…) | FA, FI·SC | M-INFO M-SEAT | c4 | e1 |
| NPC-034 | Gustav Linder | faction→realm | N1 **D**·M-SEAT (A person embedded in one institution's inner circle must…); N3 **R**·M-SEAT (A person must be able to sit in formal…); N4 **A**·M-INFO (This person's confidentiality obligation to the council he sits…); N7 U (UNCLEAR: no goal, ambition, or arc trajectory is authored…) | FA, FI·SC | M-INFO M-SEAT | c6c7 | V |
| NPC-020 | Almud Almqvist | realm | N1 **D**·M-AIM (A single leader must be able to face several…); N2 **D**·M-AIM (A leader's own long-held private doubt about a policy…); N3 **D**·M-SEAT (Actions taken in the leader's name by subordinates must…); N4 **A**·M-REGARD (A standing armed institution nominally loyal to the leader's…); N5 **A**·M-REGARD (The leader must be structurally unable to act on…) | CHAR, FA | M-AIM M-REGARD M-SEAT | c1c2c5c6 | — |
| NPC-021 | Arne Himlensendt | faction→realm | N2 **D**·M-REGARD (A leader whose personal faith is intact must be…); N4 **D**·M-SIT (The leader must be able to face a decision…) | CHAR, SC·FA | M-REGARD M-SIT | c3c5 | T e1 |
| NPC-050 | Inge Baralta | faction→duchy | N1 **D**·M-AIM (A leader must be able to build a multi-season…); N2 **D**·M-SIT (An overreaching attempt at the higher seat must be…); N3 **D**·M-SEAT (A leader's personal authority over her own institution must…) | CHAR, FA, SC·FA | M-AIM M-SEAT M-SIT | c1c2 | — |
| NPC-052 | Magnus Vaynard | faction→duchy | N1 **A**·M-PERC (A leader's personal, private research into a dangerous or…); N2 **A**·M-SEAT (A confederated leader's authority must be able to be…); N4 **D**·M-SEAT (If this leader is removed from play, the identity…) | CHAR·FI, FA | M-PERC M-SEAT | c2 | — |
| NPC-070 | Lisbeth Ehrenwall | faction→realm | N1 **A**·M-REGARD (A standing military institution nominally loyal to a ruler…); N2 **D**·M-AIM (The military leader assessing the ruler must be able…) | CHAR | M-AIM M-REGARD | c1c6 | — |
| NPC-003 | Yrsa Vossen | faction→realm | N1 **D**·M-REGARD (A person recognized as a movement's leader must be…); N2 **A**·M-INFO (The leader's public visibility, which is the source of…); N3 **A**·M-AIM (A leader must be able to choose, season after…) | CHAR, FI·SC | M-AIM M-INFO M-REGARD | c2 | — |
| NPC-032 | Lenneth Almqvist | realm | N1 **D**·M-AIM (A person with a genuine political programme and real…); N3 **A**·M-CAP (A person's capability in a specialized domain must be…); N4 **D**·M-SEAT (An external, unpredictable event unrelated to this person's own…) | CHAR, CHAR·DICE, FA | M-AIM M-CAP M-SEAT | c2 | — |
| NPC-031 | Torben Almqvist | realm | N1 **A**·M-REGARD (A minor political heir must be able to start…); N3 **W**·M-LATENT (Once the heir's alignment locks in, whether through successful…); N5 **D**·M-REGARD (The heir's relationship to whoever currently rules in his…) | CHAR, CORE·FA | M-LATENT M-REGARD | c6 | — |
| NPC-030 | Elske Almqvist | realm | N1 **A**·M-ABROAD (A person with no independent action economy, off the…); N2 **D**·M-ABROAD (A hostile foreign power must be able to hold…) | WR·FA | M-ABROAD | c6 | — |
| NPC-001 | Edeyja | world→realm | N1 **A**·M-PERC (The single most capable person in a specialized domain…); N2 **A**·M-INFO (This character must be completely unmoved by political, emotional,…); N3 **R**·M-SEAT (This character must be able to operate entirely outside…); N6 **W**·M-LATENT (A party who has repeatedly and visibly destabilized the…) | CHAR·FI, CORE·FA, FI·SC | M-INFO M-LATENT M-PERC | c1c3 | — |
| NPC-006 | Halvar Brandt | person | N1 **A**·M-SEAT (A person holding a seat on a faction's collective…); N2 **A**·M-CAP (A standing external-threat orientation attached to one specific rival…); N7 **D**·M-SEAT (Removing this person from his seat must be able…) | CHAR·DICE, FA | M-CAP M-SEAT | c4c5 | — |
| NPC-009 | Gerik Strand | person | N1 **A**·M-SEAT (A person holding a formal administrative post must be…); N2 **A**·M-CAP (A specific, named personal weakness must be able to…) | CHAR·DICE, FA | M-CAP M-SEAT | c4 | — |
| NPC-011 | Alexios Laskaris | person | N1 **D**·M-ABROAD (A foreign noble holding a governing title in another…); N2 **W**·M-LATENT (This person's entire behavioral mode must be able to…); N3 **A**·M-ABROAD (A foreign noble's personal goal must be able to…) | CORE·FA, WR·FA | M-ABROAD M-LATENT | c4c6 | — |
| NPC-035 | Theodor Kreutz | person | N1 **D**·M-REGARD (A person holding a formal military post must be…); N2 **W**·M-LATENT (A single named individual's removal from a specific post…) | CHAR, CORE·FA | M-LATENT M-REGARD | c6 | — |
| NPC-036 | Wilhelm Voss | person | N4 **D**·M-SEAT (A person holding a specific named Crown command post…) | FA | M-SEAT | c5 | — |
| NPC-037 | Annalie Reichard | person | N1 **R**·— (A named character's faction affiliation, once established in one…); N2 **D**·M-STORES (A person holding the Crown's treasury-oversight post must be…) | SE·FA | M-STORES | c5 | — |
| NPC-039 | Magnus Klapp | person | N1 **A**·M-SEAT (A Church figure must be able to be one…); N2 **A**·M-PERC (Extended engagement with archived or restricted material must be…); N3 **D**·M-INFO (A scholar developing this restricted perceptual capacity through his…) | CHAR·FI, FA, FI·SC | M-INFO M-PERC M-SEAT | c7 | V |
| NPC-040 | Osten Jarnstal | person | N1 **A**·M-SEAT (A Church figure must be able to be a…) | FA | M-SEAT | c5 | — |
| NPC-041 | Aldric Hann | person | N1 **A**·M-INFO (A faction operating partly underground must be able to…); N2 **A**·M-SEAT (Two named individuals must be able to jointly hold…) | FA, FI·SC | M-INFO M-SEAT | c5 | — |
| NPC-072 | Olaf Geirson | person | N3 **D**·M-SEAT (A named military commander sitting on a faction's inner…) | FA | M-SEAT | c5 | — |
| NPC-073 | Björn Holdar | faction→realm | N1 **A**·M-SEAT (A named seat on a faction's ruling council must…) | FA | M-SEAT | c5 | — |
| NPC-074 | Ingrid Stenskald | faction→realm | N1 **A**·M-SEAT (A council seat tied to a cultural or historical-keeper…) | FA | M-SEAT | c5 | — |
| NPC-080 | Vidar Haldorsen | person | N1 **D**·M-PERC (A person must be able to hold a hard…); N2 **A**·M-PERC (Two members of the same covert operational role must…) | CHAR·FI | M-PERC | c3c4 | — |
| NPC-081 | Uta Falkenrath | faction→realm | N1 **D**·M-SEAT (A polity's highest office must be able to become…); N2 **A**·M-SEAT (Among the paths available to win a succession contest,…) | FA | M-SEAT | c2 | — |
| NPC-082 | Njal Torberg | faction→realm | N1 **D**·M-REGARD (A subordinate's loyalty must be able to attach to…); N2 **A**·M-REGARD (A leader's own conduct -- specifically self-serving choices that…) | CHAR | M-REGARD | c6 | — |
| NPC-084 | Frieda Kessler | faction→realm | N1 **D**·M-AIM (An internal faction leader must be able to hold…); N2 **A**·M-SEAT (Two named leaders within the same faction must be…) | CHAR, FA | M-AIM M-SEAT | c2c5 | — |
| NPC-085 | Nessa Grindvold | faction→realm | N1 **D**·M-SIT (A guild's autonomy or privileges must be able to…); N2 **A**·M-REC (An advocate must be able to cite established precedent…) | FI·FA, SC·FA | M-REC M-SIT | c5 | T e1e5 |
| NPC-089 | Zoe Palaiologina | realm | N1 **D**·M-ABROAD (A foreign power's posture toward a neighboring territory must…); N2 **D**·M-ABROAD (A single named frontier governor must be able to…) | WR·FA | M-ABROAD | c2c4 | — |
| NPC-090 | Stephanos Doukas | faction→realm | N1 **D**·M-REC (A trade relationship between two polities must be able…); N2 **D**·M-ABROAD (Two named officials from different polities must be able…) | FI·FA, WR·FA | M-ABROAD M-REC | c4c5 | e1 |

**Needs whose evidence is their own.**

- NPC-088 N1, N9 (R): `create_record` executes and her Record's stages mature at MATTER by her own act
  (CORE audit §13, headless run: `record.created` 4, `term.matured` 5 in season 1; `loop/matter.py:338-395`).
  N5 (R): she forms candidates from a standing `need` question (`queries/world_q.py:4031`, headless acts
  16/17).
- ARC-R16 N1, N5; ARC-R19 N1, N4, N6; EMG-11 N1 (R): the world runs unattended (`m1_acceptance`, 24 seeds
  × 4 seasons, CORE audit §1.4), causes are attributable (R3 143/143 and the planted control), the season's
  steps and RESOLVE's strata are a fixed order (`loop/driver.py:388-563`, `loop/resolve.py:51-58`), one
  budget is spent across competing matters (`decision/budget.py`), and a faction is a view over persons'
  acts (`queries/faction_q.py`), so a personal act is already the faction's.
- ARC-25 N2, EMG-X8 N2, NSC-01 N3, NPC-010 N2, ARC-54 N3 (R): a decision reads only the decider's own
  ledger (`state/carriers.py:504-509`; CHAR audit §2 item 2); the fold does not check a belief's truth;
  `lie` (138 graded) and the graded inquiries (`research` 639, `surveil` 236) execute in the corpus run.
- ARC-53 N6 (R): `tend` executes in corpus worlds (this run's executed list). NPC-034 N3, NPC-001 N3,
  NPC-037 N1 (R): the realm seats Linder in a Church office inside the Crown's circle, Edeyja with no
  office, and Reichard as `off_lord_treasurer` (probe, §12).
- ARC-META-COLLISION (R): `run_cases.CASE_SERIES` (`:277-286`) gives the root series its own ids.

## 4. The mechanisms the needs repeat (the build order that matters)

Counts are cases with at least one unreached core need on the mechanism, and the core needs involved
(from the generated mapping). A case usually needs several.

| rank | mechanism | what the cases need | what exists today (evidence) | cases · core needs | single owner and change | carried by |
|---|---|---|---|---|---|---|
| 0 | **M-CASE** case built, beats read | the case's own people, seats, records and dates; each need checked by a run with a control | template builder; no need read (§2.2) | 143 · all | `harness/corpus_run.py`, `harness/arc.py`; cases on the realm | `01_CORE_case_setup_and_beats.md`, extended by `12_ARCS_case_on_the_realm.md` |
| 1 | **M-LATENT** a held resolve armed by what a person learns | 84 core needs are a counter, a clock or a scalar that fires with nobody deciding (Coup Counter, Church Influence, Invasion Pressure, Public Instability, loyalty clocks) | refused for social quantities by Layer 1 (`state/world.py:64-107`: no social quantity moves at MATTER; a crossing emits and produces no outcome, `loop/matter.py:132-135`); the reachability adjudication (2026-08-30, §4) gave the replacement and nothing built it: no hold candidate, no enabling-claim gate; `goals.yaml` `goal_stages:` loader exists and is empty | 54 · 84 | `goals.yaml` (`goal_stages`, a person-level goal), read by `decision/` | `12_ARCS_arcs_as_staged_goals.md`; chooser term: `02_CHAR_goal_lean_on_its_own_question.md` |
| 2 | **M-INFO** information that travels, is withheld, is found | disclosure as a choice; a third party learning later; investigation that can conclude wrongly; reports that differ from what is held | `tell`, `lie`, the six inquiry verbs exist; `told_by` 64 of 93,760 claims (this run); CHAR F-CHAR-09: 12 of 22,958 claims carry a chain | 33 · 37 | the telling and inquiry rows; `loop/witness.py` | `08_FI_02_rumour-that-travels.md`, `08_FI_01_claim-sourced-referents.md`, `08_FI_03_playable-inquiry.md` `[not opened]` |
| 3 | **M-SEAT** an office that does its business | passive effects of holding a seat, sole conduits, authorisation gates, council seats that vote, candidacy, vacancy and succession, removal that changes what the body does | seats and remits exist; realm readings (requirement file): `confer` 70/0, `revoke` 15/0, `establish` 19/0, `dispatch` 86/16, `issue` 30/6; `succeed` formed and executed 0 times in 9 heir-seasons (CHAR F-CHAR-01, H-289) | 32 · 37 | `verb_table.yaml` seat rows, `offices.yaml`, `loop/predicates.py`; duty in the chooser (CR-88) | `06_FA_decree_binds.md` `[not opened]` |
| 4 | **M-PERC** Thread, person side | sensitivity that grows unseen, perception in bands per observer, Coherence that degrades in bands, diagnosis of another | `Person.thread_sensitivity` set at build, written by nothing (`harness/loops.py:96`), read by one gate (`thread_read`, `data/fixtures.py:1146`); `(Person, coherence)` is a matrix row with a gate branch and no writer (`state/world.py:1305`; H-47) | 26 · 48 | `write_matrix.yaml`, `rosters.yaml: knowledge_kinds`, `loop/witness.py` | `12_ARCS_substrate_as_ground.md` (person half); §11 |
| 5 | **M-SUB** Thread, world side | a world quantity per place that acts degrade and that changes options; operations; hazards; restoration | nothing: no carrier, no verb beyond `thread_read`, no entity (grep, §12). The class is admissible (Site condition, stores and bodies already move at MATTER) | 25 · 58 | `rosters.yaml` site kinds and `band_floors`, three verb rows | `12_ARCS_substrate_as_ground.md`; §11 |
| 6 | **M-AIM** the chooser reads what an act would do | holding back as a choice, a three-way choice made for a reason, an act chosen because it serves the person's own want | F-CHAR-01: the pursuit term reads the verb only; 36 of 46 cast hold one top verb across six situations | 20 · 23 (57 cases by chooser demand, §9) | `decision/choose.py::score_terms` | `02_CHAR_goal_lean_on_its_own_question.md`, `02_CHAR_choice_alignment.md` |
| 7 | **M-SIT** a sitting that binds | a matter gets before a room on a date; several outcome tiers; ruling separate from enforcement; a venue's own rules of who may speak; a tie; a reopenable file | `convene`, `open_case`, `petition`, `carry`, `speak`, `argue`, `determine`, `interrogate`, `pardon`, `comply`, `evade / defy`, `construe` are rows; `venues.yaml`, `arrangements.yaml` exist; corpus: `determine` only refused, `convene`/`open_case` never attempted; realm builds 0 dates | 18 · 24 | docket reach (H-254), arrangement rows | `05_SC_playable_hearing.md`, `05_SC_arrangement_rows_that_bind.md`, `05_SC_contest_record_on_event.md`, `05_SC_acquittal.md` `[not opened]` |
| 8 | **M-REGARD** the interior moves | loyalty that erodes from neglect, regard earned or lost by a witnessed deed, a conviction that cracks | F-CHAR-03: stored stance moved for 0 of 83 persons over two seasons at two seeds | 16 · 19 | `queries/person_q.py::regard` | `02_CHAR_scar_cap_and_regard_unit.md` |
| 9 | **M-REC** a record as an object with consequence | evidence that is held, moved, hidden, forged, cited; possession that has consequences; a founding text in one man's custody | `create_record`, `give`, `conceal` execute in the corpus; `forge`, `seize` only refused or never attempted; `destroy_record` cannot fire (H-75); nothing makes holding a Record a fact others act on | 12 · 14 | `loop/effects_information.py`, `world_q.questions_for` | `12_ARCS_cited_evidence.md` |
| 10 | **M-CAP** persons differ in what they can do | skills, a named weakness, specialist experience, a ceiling | capability empty for all but two cast; attributes ship off; `train` attempted and never executed (requirement file); pool default for nearly everyone | 12 · 15 | `rosters.yaml: verb_capability`, `references/npc_registry.yaml` | `02_CHAR_capability_uses_table.md`, `10_DICE_advantage_sources_for_the_arcs.md` `[not opened]`; §8 |
| 11 | **M-FIELD** force at scale with consequences that last | a commander's fall, a unit's lasting condition, a personal act inside a battle, a wound that follows a leader into later acts | `fight` executes (13); `march` never attempted in the corpus; body bands cut the scene budget, not a pool (`decision/budget.py`) | 10 · 17 | `modules/mass_battle`, the seam's typed outcome | `04_MB_headcount_grade_and_scale.md`, `03_PC_exits_withdrawal_recovery.md` `[not opened]` |
| 12 | **M-STORES** material economy | a levy per territory, trade, a treasury, per-place favour | stores, subsistence and production run at MATTER; `exchange` attempted and never executed; `requisition` executes a few times; `levy` 0 (requirement file) | 8 · 11 | settlement rows | `07_SE_ground_and_granaries.md` `[not opened]` |
| 13 | **M-ABROAD** powers beyond the map, through persons | a foreign governor who chooses a posture, a hostage, a superior who recalls | Altonian seats and goals are authored; the home authority above them is not a person; no off-map place | 7 · 10 | `offices.yaml`, `npcs.yaml` | none written; §6 row 12 |
| 14 | **M-PLAYER** a player's seat | 16 cases name a player | `play_surface.dispatching_chooser` exists, no caller in the runner | 16 cases (2 core needs name it) | `harness/corpus_run.py` | `01_CORE_case_setup_and_beats.md` |
| 15 | **M-SPAN** long arcs | spans of 8 to 20 seasons | `MAX_SEASONS = 6` | 5 integer spans above 6, plus the ranges in `ARC4.yaml` | `loop/matter.py` | `01_CORE_claim_fade_as_read.md` |

**Order.** Rank by count is not the order to build in. M-AIM underlies M-LATENT (a latent act is an aim
with an unmet enabling claim); M-INFO feeds it (the claim must arrive); M-SEAT and M-SIT share one owner
family; M-PERC and M-SUB are one decision. The order that unlocks cases soonest is §5's.

## 5. Staged simulation sequence

"Simulable" below means: no core need of the case is left unreached on a mechanism, by §3's mapping. It
is a necessary condition, not a demonstration; the demonstration is the artifact named per stage.
Counts come from the generated mapping, for this order.

| stage | lands | cases that become simulable | cumulative | execution artifact (seeds 0, 1, 2; on-arm and control) |
|---|---|---|---|---|
| 0 | M-CASE | none alone; makes every later stage checkable | 0 | two cases at one scale differ in content hash at tick 0; a beat reader that returns `absent` on the shuffled-causes log (`arc.shuffled_causes`) |
| 1 | M-REC, M-INFO | NPC-088, NPC-086, NSC-01, NSC-04, NSC-06 | 5 | NPC-088: a second person comes to hold her Record and deposits a claim about her; off-arm (no Record made): the beat is absent |
| 2 | M-AIM, M-REGARD | NSC-02, NPC-010, NPC-070, NPC-003, NPC-082 | 10 | NPC-082: Torberg's commitment to the cause survives while his regard for the leader falls after witnessed deeds; control: leader's deeds withheld |
| 3 | M-SEAT, M-SIT | ARC-29, ARC-04, ARC-10, NSC-03, EMG-11 N2, NPC-008, -020, -021, -033, -034, -036, -038, -040, -041, -050, -071, -072, -073, -074, -081, -084, -085 | 32 | ARC-04: a case opened against Maret matures by stage, her petition to Vaynard is dropped or carried, the sitting forces his public act; control: no case opened |
| 4 | M-CAP, M-STORES | SCN-05, NPC-087, -032, -006, -009, ARC-15, NPC-083, -037 | 40 | NPC-009: the same approach to Strand and to a peer resolves at different obstacles, read from data; control: the trait row removed |
| 5 | M-LATENT (authoring per case) | 38 cases, among them ARC-03, -06, -11, -13, -14, -17, -18, -21, -24, -31, -34, -36, -40, -44 to -47, EMG-C1, -C2, -C4, NSC-08, -09, SCN-12 | 78 | ARC-47: Ehrenwall's demand enters her option set only after three claims reach her ledger; control: one claim withheld; second control: a planted false claim arms her |
| 6 | M-ABROAD, M-FIELD, M-PLAYER | ARC-25, -38, NPC-011, -012, -030, -089, -090; ARC-07, -20, -23, -53, NSC-05; ARC-01, ARC-R16 | 92 | ARC-23: a commander falls in a fought field and the army's next acts differ; control: same seed, commander absent from the field |
| 7 | M-PERC | 24 cases (ARC-02, -09, -16, -26, -28, -30, -32, -33, -35, -39, -41, -51, -54, EMG-X6, -X7, SCN-07, -10, SCN-LOOP-C, NPC-001, -004, -005, -039, -052, -080) | 116 | NPC-004: a qualified person's diagnosis deposits a claim about Haelgrund that he does not hold; control: observer below the gate |
| 8 | M-SUB | 25 cases (ARC-05, -12, -22, -27, -37, -42, -43, -48, EMG-C3, -X5, -X8, NSC-07, eight SCN chains, NPC-002, -007, -075) | 141 | ARC-48: ground condition falls with operations and a band crossing raises the floor of the same verb; control: operations withheld, baseline wear only |

ARC-META-COLLISION is satisfied today (142). The one case left is EMG-10, the nine-condition endgame
checklist: its conditions belong to the mechanisms above and its evaluation to `world_q.endings_reached`,
which computes endings nothing reads (CORE F-CORE-05). Stages 7 and 8 wait on §11.

**The scripting-drift test, applied.** A beat counts only if (i) the setup names no outcome and no act,
(ii) it is absent in the off-arm, (iii) it does not survive shuffling the cast's creeds between persons
when it is keyed to an actor, (iv) it is absent on the shuffled-causes log. Cases whose core need, *as
stated*, can be satisfied only by special-casing an entity or an outcome, with the form that passes the
test:

| case · need | as stated | why it is a script | the form that is not |
|---|---|---|---|
| ARC-14 N3, ARC-17 N2 | an NPC's response is a fixed lookup on his own stability | a named person's answer written in a table | his choice through the one chooser; his condition enters as budget and odds |
| ARC-11 N2 | an administrator breaks after a fixed span | a timer on a named man | his load is the acts routed through him; he fails when his budget cannot cover them |
| NPC-011 N2, ARC-38 | Laskaris flips when another's loyalty value crosses 2 | a threshold on a named pair | his regard for Elske and what he learns of her danger decide his next act |
| ARC-52, ARC-55, ARC-46, SCN-08, SCN-11, SCN-LOOP-B, EMG-10 | a quantity auto-resolves at a ceiling | an outcome with no actor | no faithful form for the auto-resolve; the pressure survives as M-LATENT in the persons who would act (reachability scored 52 NEVER-WORKED) |
| NPC-020 N8, NPC-032 N4, NPC-031 N6, NPC-030 N5 | an unpredictable family death reconfigures the realm | an authored event card on named persons | deaths arise at MATTER (body falls) and at ENCOUNTER; if a seeded mortality draw is wanted it is the existing actorless channel (`season(actorless=…)`), applied to every person alike |
| ARC-22 N4, ARC-27 N3 | the worst roll spawns a hostile entity in the room | an authored spawn table | absent until an entity is a person or a cohort the engine individuates; out of the minimal M-SUB |
| ARC-01 N5, ARC-03 (pretext), NSC-02 | a player removes one named cost from a ruler's calculus | a designer's list of costs | each cost is a claim or a commitment the ruler holds; removing it is an ordinary act on its referent |

## 6. Wrongly stated or contradictory needs, and their resolutions

Ladder step: 1 superseded · 2 irrelevant · 3 answered by a design document or the code's owner ·
4 precedent · 5 what the architecture makes clearly right.

| # | need or contradiction | decided resolution | step | carried by |
|---|---|---|---|---|
| 1 | 88 core needs state a social counter, clock or scalar that fires with nobody deciding (54 cases) | re-express each as a person's held resolve armed by claims, a standing date, or a material quantity; the cases keep their story and lose the gauge | 1 (Layer 1, ED-IN-0204; reachability adjudication §4) | `12_ARCS_arcs_as_staged_goals.md` |
| 2 | "the faction chooses / holds a stat" (ARC-08 N3, NPC-007 N1, ARC-53 N2, ARC-40 N1) | a faction is a view; the choice is each seated person's; the "Guilds' choice" becomes several brokers' | 1 (`queries/faction_q.py`; Jordan's ruling recorded in reachability lane 1, Arc 8) | case setup |
| 3 | "response fixed by a stat lookup when not player-controlled" (ARC-14 N3, ARC-17 N2) | one chooser for player and NPC; the lookup is dropped | 3 (R-08's statement; `decision/choose.py`) | §9 |
| 4 | "GM-judged", "a judgment call determines" (ARC-03 N3, EMG-X5 N2, SCN-05 N1) | there is no GM; the judgment is the acting person's estimate from his own ledger | 2 | — |
| 5 | a skill gates whether an attempt may be made (ARC-23 N2, ARC-51 N5) | capability supplies dice and gates nothing (the ruling CHAR §5 records as binding, #353 §9.2); the need becomes "the pools differ". Thread sensitivity stays the one class-shaped gate (H-85) | 1 | — |
| 6 | Coherence at 0: the engine's design reading is loss of agency; ARC-28/29/30 require expansion with continuity | not decided here; §11 | survives | — |
| 7 | struck mechanics (Coup Counter in six arcs, Niflhel in two, NSC-01) | the mechanic is dead; the story half re-enters as M-LATENT (Ehrenwall's resolve) and as an independent broker (Virke) | 2 | — |
| 8 | 86 spans stated as prose | CORE resolution 3 (integer plus `ongoing:`) | 5 | `01_CORE_case_setup_and_beats.md` |
| 9 | case text and the realm's roster differ (Lenneth "queen consort" against `off_widow_regent`; Almud holding three territories) `[UNVERIFIED what the realm's seat names imply]` | the registry and `offices.yaml` are the code-read owners; the case's setup delta states the difference it needs | 3 | `12_ARCS_case_on_the_realm.md` |
| 10 | NPC-002 N4: Thread sensitivity 50 or 35; Almud 28 or 0 | the registry row the builder reads: 50 and 28 (probe, §12) | 3 | — |
| 11 | NPC-035/036/037/040: migrated convictions disagree with their sources; "resonant style" has no field | the live carrier is the fifteen-pursuit vector every cast person holds (ED-IN-0261); the 7- and 13-conviction notes are superseded. Resonant style is a missing trait, §7 | 1 | §7 |
| 12 | off-map superiors (the imperial court, Schoenland's centre) decide things (ARC-38 N2, NPC-012 N2, NPC-089 N6) | "generate a person": the superior is one seated person with one seat outside the map's rungs, or the need stays unreached. Reachability lane 2 (Arc 38) found the fiction itself argues for persons | 4 (Altonia's two seats already follow it) | none written |
| 13 | ARC-META-COLLISION | closed by `CASE_SERIES` | 1 | — |
| 14 | EMG-11 | not a case; N2 (a finite per-place capacity gating a rank) is the establishment gap both earlier exercises found; FA lane | 2 / cross-listed | — |
| 15 | `ARC3.yaml`'s lost head | unrecoverable; dropped | 2 | — |
| 16 | CORE proposal 02 adds `knows:` to the cast; the loader refuses `knows:` as a Layer-1 question | seed what a person knows as prehistory: acts and witnessed Events through the gate before tick 0, not constructed Claims. `populated.py:647` constructs acquaintance claims directly; that precedent is narrow and is not widened | 5 | `12_ARCS_case_on_the_realm.md` |
| 17 | ARC-55 N4: the gating value can only be restored by the act it gates | under row 1 the value is regard held by named persons, which moves on acts toward them; the circle opens | 5 | — |
| 18 | SCN-LOOP-A N6, -C N5, -D N7: the source contradicts itself on exits | decided only if M-SUB is built: mending is its own verb row (so both conditions hold); the abstention path stays; only the counter-group loses access | 5, conditional | `12_ARCS_substrate_as_ground.md` |
| 19 | NPC-088 N6, NPC-087 N2, NPC-086 N3: is the material Thread-substrate knowledge or ordinary suppressed knowledge | ordinary; `rosters.yaml: knowledge_kinds` is the owner and the gate applies to the kinds it names `[UNVERIFIED: roster not opened at the row]` | 3 | — |
| 20 | NPC-071, -034 N7, -036, -040, -041, -072, -073, -074: no goal, arc or stake authored | not an engine gap: the character is an office-holder whose behaviour is the seat's business plus creed (the realm already gives each fifteen pursuit weights and commitments). They become simulable with M-SEAT; nothing is invented for them | 5 | — |

## 7. Traits the character model cannot yet carry

The referents are the quarantined roster's "AI flaw" per character and the case needs that restate them
(`.designs/…/npc_roster_v30.md`, read for vocabulary only).

| described trait | carried today | extension at the single owner |
|---|---|---|
| a standing disposition that persists against interest (CONFLICTED, PROCEDURALIST, CONSERVATIVE, OVERPERFORMER, PROTECTIVE, STABILITY-SEEKING, OPTIMISER, EXTERNAL THREAT FIXATED and four more) | nothing but the pursuit vector; one realm-wide temperature (F-CHAR-02) | a per-person temper read by the chooser (`02_CHAR_resolve_and_temper.md`); never a numeric modifier on a faction quantity |
| a personal goal or ambition | `goals.yaml` rows attach to a faction, body or seat only; the registry's `goals` are non-null for 17 of 46 (F-CHAR-13) | a person-level goal row and `goal_stages` (`12_ARCS_arcs_as_staged_goals.md`) |
| a private doubt that is itself a choice (Almud, Himlensendt) | `scar`, `conviction`, `confliction` exist; `confliction_weight` ships at 0 | arm the existing reader behind its fixture; the doubt is a stage, not a meter |
| loyalty to a person, to an institution, to a cause, kept apart (Kreutz, Ehrenwall, Torberg) | a `commit` to a Proposition and a stance toward a person are separate carriers already | M-REGARD; no new field |
| what kind of appeal moves this person (the design's "resonant style" / pressure point: evidence, consequence, authority, loyalty) | no carrier (grep: comments in `rosters.yaml` only) | a registry field per person and one row in `rosters.yaml: advantage_sources`, read by `seam/wrappers/sigma.py::contest_input` |
| a named weakness that eases one kind of approach (Strand) | none | the same advantage-source row, keyed on the target |
| typed relationships: kin, patron and client, sworn bond, rivalry, feud | tenure kinds `contain`, `reside`, `commit`, `hold`, `oblige`; `npcs.yaml` gives each person one `tie: institution` and one `concerns:`; `tie / knot` is the one verb row with no predicate or effect | build the `tie / knot` row with edge kinds as tenure kinds; author kin in `npcs.yaml` |
| Thread sensitivity that grows, and ignorance of one's own | set at build, never written | M-PERC |
| Coherence and its bands | a matrix row with no writer | M-PERC; §11 |
| overt and covert reputation kept apart (Torsvald) | regard is computed per asker, so two audiences already differ | none |
| two offices at once (Feldhaus, Kreutz, Strand) | represented: several `hold` tenures (the realm gives Strand two) | none |

## 8. Capability authoring: what the corpus implies

Listed so that each can be defined once as data and referenced by declaration (the §14 charge). The
single authoring surface is CHAR's (`02_CHAR_capability_uses_table.md`, not opened); this is content for
it, not a second scheme. "Code today" names the reader that exists.

| RPG axiom | capabilities the provided characters and arcs imply | code today |
|---|---|---|
| **Attribute** (innate, slow to change; sets a pool base or a threshold) | Spirit, Cognition, Charisma or Presence, Focus, Endurance, Agility, Attunement, Strength (named by the SCN chains and the roster) | ten ruled attributes exist as a carrier that ships off |
| **Skill** (trained; supplies dice to named verbs) | copying (Vedel), teaching (Askeland), surveying (Bergvall), inquiry and procedure (Haelgrund), tradecraft: watch, conceal, forge (Thale, Torsvald, Uln), brokerage and appraisal (Virke, Feldhaus, Doukas), administration (Strand, Reichard, Kronvald), finance and levy (Tormann), advocacy and precedent (Grindvold, Heljason, Almstedt), oratory, mediation (Falkenrath), lore-keeping (Stenskald), command (Ehrenwall, Brandt, Geirson, Torberg, Voss), medicine (ARC-23), diplomacy (Laskaris, Solberg, Palaiologina), mending (Orm, Edeyja) | `rosters.yaml: verb_capability` maps a verb to one key; keys seen in play: `copying`, `inquiry` |
| **Sense** (banded perception; gates what is witnessed) | Thread sensitivity, diagnosis of another's sensitivity, reading a motive | one gate on one verb |
| **Resource track** (spent and recovered; bands change what is possible) | wounds and body bands, stamina, composure or stress, Coherence, cover and exposure, the season's scene budget | body bands and the budget; the rest absent |
| **Trait or tag** (a keyed modifier or a refusal) | the twelve dispositions, a named weakness, the appeal that moves a person, a hard zero in a sense (Haldorsen), caste and heritage, a cultural template as default | `heritage` (4 authored); a deontological refusal built and unarmed (CHAR §5) |
| **Drive** (what a person is after) | creed, beliefs, private doubt, ambition | fifteen pursuits over seven axes; scar; commitments |
| **Standing** (position and regard) | office and rank, candidacy, regard, loyalty, bond, renown, covert standing | offices, tenures, stance, computed regard |
| **Advancement** (how a capability is gained or lost) | training by another, experience from engaged convictions (SCN-05), a ceiling (Lenneth), a rank gated by a place's capacity (EMG-11), exposure from routine work | `train` writes `Person.capability` and has not executed in computed play |
| **Opposition** (what stands against a roll) | the subject's own score, a venue's bench, held proofs, concealment kept up scene by scene (NPC-004 N6) | obstacle from the opponent's score; `reception` and `proofs` lower it (`world_q.py:852`) |
| **Aid and command** (many acting as one) | helper dice to an anchor (SCN-13), a commander's order reaching a unit, corroboration by a bonded ally (EMG-X6) | none in the season loop `[UNVERIFIED for `modules/mass_battle`]` |

What a definition must say for these cases to use it: name; axiom; scale (person, seat, unit); the verbs
that draw on it and in which role (pool, obstacle, gate, advantage); its range and bands; how it grows
and what opposes it. The cases supply two requirements a designer might not expect: a capability may be
**unknown to its holder** (Haelgrund, Vaynard, Klapp), so "held" and "known to hold" are separate facts;
and a capability may be a **hard zero** that no training moves (Haldorsen, Himlensendt).

## 9. The chooser: what each case asks of it, and where it cannot answer

The statement of NPC and chooser intent is the CHAR lane's; its audit holds the built facts this section
rests on (F-CHAR-01 to F-CHAR-09) and its intent statement was not yet on disk when this was written.
I do not restate it. Demand codes, with the number of cases that carry each (§3's `chooser` column):

| code | the chooser must | cases | as built |
|---|---|---|---|
| c2 | choose an act because of what it would do for the person's own want | 57 | cannot: the score reads the verb, not the act's effect (F-CHAR-01) |
| c5 | do a seat's business because the office calls for it | 39 | partly: seat verbs form; several never execute (§4 M-SEAT); duty is unbuilt (CR-88) |
| c7 | tell or withhold a held fact to a particular person for a reason | 29 | partly: `tell` and `lie` are offered; withholding is not a scored choice; little is told at all |
| c1 | hold: decline to act now, with a stated condition for acting | 21 | cannot: no hold candidate, no enabling-claim gate |
| c3 | act confidently on a belief that is partial or false | 19 | structurally yes (the decision reads the ledger); almost nothing second-hand is held, so nobody is mistaken (F-CHAR-09) |
| c6 | let a changing regard or loyalty change the choice | 18 | cannot: stored stance did not move in two seasons (F-CHAR-03) |
| c4 | carry a personal disposition into every choice | 17 | cannot beyond creed: the departure from the optimum is realm-wide (F-CHAR-02) |
| c8 | take a player's choice in a named seat | 13 | the dispatch exists; the runner passes the automated chooser only |
| c0 | nothing (a rules chain or a meta case) | 22 | — |

- **(a) Who decides, on what.** In every case a named person decides on his own ledger; no case needs
  a decision on world truth. The budgets the cases imply are the season's scene budget plus office bonus;
  seat-holders (Almud, Kronvald, Strand) are the ones the round count caps (CORE F-CORE-06).
- **(b) One interface.** The cases that name a player (16) ask nothing of the engine that an NPC in the
  same seat would not do; the proxy must go through `dispatching_chooser` so that the echo policy leaves
  the hash equal (CORE proposal 02).
- **(c) Where the cases themselves hard-code an NPC rule.** §5's scripting table: the stability-band
  lookups, the flaw timers, the flip thresholds, the "automatic" objection that "fires every time"
  (ARC-13 N2). Each is re-expressed through the chooser or dropped.
- **(d) Characterful and legible.** The cases distinguish people by one thing each: what they will not
  do (Edeyja, Heljason), what they keep doing (Tormann, Strand), whom they protect (Laskaris, Kreutz),
  what they cannot see (Haldorsen, Feldhaus). The pursuit vector separates creeds (CHAR §2 item 1) and
  carries none of these four. A reason trail the beat reader can use is the question a person answered
  and the term that decided (`02_CHAR_reason_trail_and_small_edits.md`, not opened); `beats:` should be
  able to match on it.
- **(e) Missing, as proposals.** `12_ARCS_arcs_as_staged_goals.md` (c1, c2 as data), and CHAR's own for
  c2, c4, c6.

## 10. Cases that turn on a reveal, an investigation, an accusation or a trial

Fifty-one cases are marked in §3: investigation 25, reveal 19, hearing or trial 19, accusation 12. The
needs they place on typed evidence and argument:

| code | need (count: cases) | engine today |
|---|---|---|
| e1 | an argument or accusation must cite a held item: a record, a finding, a testimony (25 cases: ARC-07, -08, -10, -12, -14, -15, -17, -18, -37, -41, -42, EMG-X6, NSC-01, -03, -04, -06, NPC-008, -021, -038, -071, -085, -086, -087, -088, -090) | a contested act reads `proofs`: the speaker's own deed-claims about the opponent, weighed by how far removed, and worth zero where the opponent holds the same claim (`world_q.py:852-866`). The proof is a count from a ledger, not a cited item; a Record is not an input to any contest; the arrangement's own `proofs` column is not read (H-216) |
| e5 | a verdict in several tiers, kept as a record that can be cited or reopened (7: ARC-04, -06, -10, -21, EMG-C4, NSC-04, NPC-085) | degree ladder with different writes per band on `argue` and `determine`; `determine` does not execute in corpus worlds; no reopening |
| e2 | corroboration needs independent roots; no single trail suffices (6: ARC-37, -42, -54, NSC-01, -04, NPC-086) | not found `[UNVERIFIED: claim source chains not opened; CHAR counts 12 chained claims of 22,958]` |
| e4 | the venue decides who may speak, defend or corroborate (5: ARC-04, -31, -32, -35, EMG-X6) | `venues.yaml` and arrangement rows exist `[UNVERIFIED which columns are read]` |
| e3 | a wrong conclusion binds as hard as a right one (3: NSC-01, NPC-004, NPC-010) | holds by construction: the fold never checks truth |
| e6 | planting, forging, suppressing or altering evidence changes a case (3: ARC-15, NPC-004, NPC-086) | `forge` and `conceal` rows exist; neither reaches a contest |

Bearing on the precedents the brief names (I rely on the brief's characterisation of them; the research
tables were not opened): the cited-item accusation (L.A. Noire) is e1 and is the gap; the conclusion that
locks only when its support is jointly right (Obra Dinn) is e2 and NSC-01's whole premise; cross-examination
by contradiction (Ace Attorney) is the mirror test turned round, a claim the opponent holds that
*contradicts* rather than *matches*; a community whose opinion moves with each conversation (Pentiment) is
`reception`, which exists. The honest null: no case in the corpus needs an internal chorus of faculties.
Ownership of proceedings is ruled (ED-SC-0033..0039) and is not touched; `12_ARCS_cited_evidence.md`
states the arcs' requirements at the owner and is to be reconciled with the SC lane's hearing proposals,
which I did not open.

### Proposals written by this lane

| file (under `proposals/2026-11-12-subsystem-audit-suite/proposals/`) | mechanism | decided | gate |
|---|---|---|---|
| `12_ARCS_case_on_the_realm.md` | M-CASE | a case is a delta on the realm; knowledge seeded as prehistory through the fold; three controls | NPC-088's beats on-arm, absent off-arm, absent on the shuffled-causes log, seeds 0–2 |
| `12_ARCS_arcs_as_staged_goals.md` | M-LATENT, M-AIM (data) | a counter becomes stages of the holder's goal, each armed by a claim in his own ledger; a stage names no act and no outcome | ARC-47: the demand is issued with three claims, not with two, and also with a planted third |
| `12_ARCS_substrate_as_ground.md` | M-SUB, M-PERC | **held back**: two options (§11) | ARC-48's loop measured against a pinned-ground control |
| `12_ARCS_cited_evidence.md` | M-REC, the e-needs | a held Record is a proof; the arrangement admits; a contradiction strikes; possession can be found | NPC-086's obstacle with the Record, without it, and against a contradicting finding |

Decided resolutions in §6: 20 rows, of which row 6 is escalated (S-2) and row 18 is conditional on S-1.

## 11. Survivors for Jordan

Two. Each is written as a proposal and listed here because it would add to or overwrite ratified design.

**S-1. Does the world itself decay?** Forty-nine cases turn on the Thread: 25 on a world quantity (M-SUB), 26
on the person side (M-PERC), two on both (ARC-27, EMG-X8). The quarantined throughlines make it the first of "the two
contests" (T-04, T-20); the 2026-08-30 synthesis found its absence an omission, three lanes independently;
the code has no carrier.
- *Option A (proposal `12_ARCS_substrate_as_ground.md`): ground.* A Site kind per territory whose
  condition wears at MATTER, is damaged by the failure bands of three verb rows and repaired by one, and
  whose bands set those rows' floors. No entity, no operation table beyond the three. The world can run
  down; survival and sovereignty compete for the same scenes.
- *Option B: not built.* The Thread stays a matter of perception and belief only. The 25 M-SUB cases are
  recorded as outside the game; the world is misunderstood, not dying.
- They are different games. A is taken as the working answer for sequencing only `[low; Jordan to decide]`.

**S-2. Coherence at zero.** The design reading the tree last adopted is loss (a person "returns to cohort
fidelity"); ARC-28, -29 and -30 open by retracting that reading in favour of expansion with full
continuity and a calibrated, lossy way of speaking. The code follows neither (no writer).
- *Option A: loss.* The practitioner's career ends in de-individuation; three arcs become other stories.
- *Option B: expansion.* A terminal state that keeps the seat and the goals and changes what can be
  told to whom; needs a per-listener telling the engine does not have.

## 12. Evidence log

Tree 785bc62, `PYTHONHASHSEED=0`. Outputs: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/ARCS/`;
working scripts: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/arcs_work/`.

| command or probe | seed · seasons | outcome |
|---|---|---|
| `python -m engine.season.harness.corpus_run` | 0 · 1–6 per case | exit 0 (`corpus_run.txt`); figures in §2 |
| `python -m engine.season.harness.run_cases` | — | exit 0 (`run_cases.txt`); NPC 2 BLOCKED · 6 DEGRADED · 38 NOT-ASSESSED; ARC 97 NOT-ASSESSED; 972 rows = 35 declared · 868 undeclared · 69 UNCLEAR; probes 64 PASS of 121 |
| `python -m engine.season.harness.exercises` | — | NPC 35/292 (32/122 core); ARC 0/611 (0/300 core) |
| `arcs_work/census.py` (loads through `run_cases.load_cases`) | — | §2.1; loader defects listed |
| `arcs_work/ex.py` (overlay listing) | — | 77 files; rows in 8; cast in 27; scale re-authored in 57 |
| inline: `VERB_TABLE`, `resolvable_verbs()`, `MATRIX` | — | 67 rows, 66 resolvable (`tie / knot` not); matrix keys include `(Person, coherence)` |
| inline: `build_realm(0)` | 0 · tick 0 | 2.0 s; hash `600d8b271474…`; counts in §2.2 |
| greps: `coherence`, `thread_sensitivity`, `proofs`, `resonan` under `engine/season` (non-test) | — | as cited in §4, §7, §10 |
| `arcs_work/table.py` | — | 143 rows; 427 core needs assigned once each (R 21 · D 136 · A 176 · W 88 · U 6); §4 and §5 counts |
| `git status --short` | — | see receipt |

No `pytest`; no `aperture` run. The realm figures for individual verbs are the requirement file's.

**Reading coverage.** Read in full: every case (143; `ARC-01..14` from the file, the rest from a
field-complete dump of the loader's objects); `CASE_BRIEF.md`; `ENDINGS_CLASSIFIED.yaml`; all five
arc-reachability files; the brief (as it stood at each amendment I was told of); `00_NINE.md`; the CORE
audit; the CHAR audit to its §5; CORE proposal 02; `goals.yaml` rows; the quarantined
`videogame_mode_spec.md`, `complete_systems_reference.md`, `throughlines_complete.md` and the skeleton of
`npc_roster_v30.md`. Read as executable lines with docstring heads (comments stripped, line numbers kept):
the six instruments. Read as headings and first lines only: `npc_behavior_v30` (index),
`npc_relational_graph_v30.md` (to §4.6), `character_canon_v30.md`, `npc_foils_v30.md` (skeleton),
`decision_policy_v1.md` (to §6), `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md`
(head; its transport, the Key substrate, is retired, and its "about thirteen structural shapes" census
was not re-verified).

`[SKIPPED: the rest of the CHAR design set in `dossiers/02_CHAR.md` (about 700 KB: `npc_behavior_v30` body and infill, `npc_roster_v30_infill`, `npc_character_analyses_v30` and infill, `npc_foils_v30_infill`, `character_histories`, `conviction_*`, `derived_stats`, `player_agency`, `companion_specification`, `edeyja_npc`, `baralta_v30`) — context budget; the directive to read them arrived after the case reading had been done]`
`[SKIPPED: `.audit/` beyond the one head named — same reason]`
`[SKIPPED: the brief's "Context and referents" section and `dossiers/99_cross_cutting.md` — acted on from the coordinator's summary of them, not opened]`
Notes: HEAD moved to f83534e during the pass (the suite's own files); the code trees were not re-read
after it. §3's table was inserted into this file by `arcs_work/table.py` through a script, not through
the editor; the naming gate was checked afterwards by grep (0 hits).
`[SKIPPED: the other lanes' proposals named in §4 — cited by filename as owners, not opened]`
`[SKIPPED: `research/` — not opened; §10's precedent mapping rests on the brief's wording]`
`[SKIPPED: `harness/populated.py` body, `loop/predicates.py`, `loop/witness.py`, `venues.yaml`, `arrangements.yaml`, `offices.yaml`, `npcs.yaml` beyond a sample — statements about them rest on the probe, greps and the audits cited]`
