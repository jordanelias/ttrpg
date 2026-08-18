# Breaking the recursion — diagnosis, and the one change that ends it

## Status: PROPOSED — decision requested from Jordan. Terminal by design: executing it deletes it.

## Date: 2026-08-18 · Lane: IN (cross-cutting) · ED: none allocated — see note

**No ED was allocated.** `registers/editorial_ledger_in.jsonl` has ~108 tokens of headroom under a
blocking cap. This is the second consecutive document that could not file itself. That is not an
inconvenience to route around; it is the finding, arriving twice.

**Method note.** Fable 5 was requested for the orchestration and interrogation nodes and was
dispatched first. Both Fable agents terminated on an account usage limit, so the investigation ran
on Opus 5. **Fable later became available and adjudicated the result** — three read-only nodes:
the causal diagnosis, a re-run of the adversarial attack on the culling plan, and an independent
verification of the Recall derivation. **Fable refuted this document's original headline claim and
overturned its original culling disposition.** Both are corrected in place, with the superseded
versions and the cases that broke them recorded in §7.2 rather than deleted. Working log: §8.

---

## 0. The one-paragraph answer

**The premise needs one correction, and the correction changes the cure.** This is not a cycle of
building and demolishing. Measured: **zero** files under `tools/`, `tests/valoria/` or `.claude/`
have ever been deleted and re-created at the same path; **128 tools were added and 21 deleted.**
What is happening is **accretion with function migration** — each session leaves the prior layer
standing and adds a new one *above* it, and on the rare occasions a tool does die, its *function*
is usually re-hosted under a different name (8 of the 21 deletions). **Functions here die when
their subject dies, not when their file dies.** The felt experience of demolition has two real
referents: one platform turnover in June–July, and the mass evacuations, which are the only way
anything ever leaves and are always a governance event.

**You cannot fix that with a subtraction**, which is why the culling plan, though a correct and
honest inventory, is insufficient. But the reason is not the one this document originally gave.

**Corrected 2026-08-18 after adjudication (see §7.2).** This section first claimed the recursion
persists "because the repo has no external referent — every claim is checked against another claim
inside it," and that installing an arbiter is "the single change that terminates" it. **That is
refuted by this repository's own tree.** The Python engine already has hard external referents — the
interpreter, a deterministic campaign key-log hash, and byte-exact goldens — and **the deepest
recursion in the repo grew on top of them anyway**, ending in a test that a flag is pinned in the
gate that checks the goldens. An external referent terminates recursion only over the claims it can
adjudicate; the loop migrates to the meta-claims it cannot — *is the pin present, is the register
fresh, is the tier honest* — and only the doctrine stops that migration.

**The actual cause is the three-term mechanism in §2**: a subject-blind guard-minting doctrine that
generates the work (T3), a reward function satisfiable entirely by prose (T2), and an attention
surface that prices internal-consistency claims above game claims (T1). **Act 4 — the doctrine
amendments — is what terminates the recursion. Acts 1–2 — the compiler and the redefinition of
"done" — are the anchor that points the freed capacity at the game.** The compiler is still the
right first move, because "the game loads" is the highest-value claim available that a session
cannot satisfy by writing. It is not sufficient on its own, and this document originally said it was.

---

## 1. The measurement

### 1.1 What the repository spends itself on

| | value | command |
|---|---:|---|
| total commits | 3,728 | `git log --oneline \| wc -l` |
| commits touching executable game code | **123 (3.3%)** | `git log --oneline -- engine/ sim/ 'systems/*/sim/' combat_engine_v1/` |
| commits touching `audit/` | 570 (4.6× game) | |
| commits touching registers/references/canon/HANDOFF/CURRENT/workplans/proposals | **1,341 (10.9× game)** | |
| `[infrastructure]` commits | **921** | `git log --pretty=%s \| grep -c '^\[infrastructure\]'` |
| `[design]` commits | 53 | |
| `[godot]` commits | **11** | |

**921 infrastructure commits to 11 godot commits — 84 : 1.**

Current tree by line count: game 30.0% · apparatus 19.3% · prose-about-process 50.7%.
**Apparatus + prose = 69.9% of the repository.**

The last seven days, by added lines: game **1.9%** · apparatus 26.9% · prose 71.3%.
**Apparatus : game = 14.4 : 1. Apparatus + prose : game = 52.6 : 1.**
The only executable game code touched in the entire week was `combat_engine_v1/core.py`, **+30/−1**.

### 1.2 The trend is not flat — it is accelerating

(apparatus + prose) : game, by month —
2026-03 **1.89** · 04 **0.65** · 05 **0.24** · 06 **1.29** · 07 **1.79** · 08 (17 days) **6.42**

The worst ratio in the project's history is the current month, achieved on its *lowest* commit count.
The repo is slowing down and concentrating what is left on itself.

### 1.3 The reduction paradox — this is the finding that should end the debate

191 commits carry *consolidate / cull / prune / leanness / retire / evacuate / sweep / audit-of /
meta* in the subject line. Their combined effect:

> **net +82,020 lines. 149 of 191 (78%) are net INCREASES. Only 20 (10.5%) are net decreases.**

Of ~16 identifiable dated "reduce the apparatus" campaigns, **three** were net reductions. Specimens:

| date | commit | net Δ |
|---|---|---:|
| 2026-07-15 | "Consolidate the observability apparatus… + **prune**" | **+8,729** |
| 2026-07-31 | "Collapse 25 validator jobs into 2" | **+8,520** |
| 2026-08-12 | "Track G continued" | **+30,759** |
| 2026-07-19 | "**Retire `designs/`**" — the headline retirement | **−21** on 250,000 lines of churn |
| 2026-08-17 | "**Culling plan v1**" — a plan to cull | **+1,819** (adds 1,890, deletes 71) |

**A document proposing to delete 350,000 lines was, itself, a net addition of 1,819.**

### 1.4 Jordan has given this instruction four times

| date | quote |
|---|---|
| 2026-08-04 | "params .md are largely useless at this point and I want them gone. **code should have superseded them all by now**" |
| 2026-08-04 | "our fork is going to hold all the outdated largely-prose work that **contaminates our code-based work**" |
| 2026-08-11 | "make this project as lean as possible without sacrificing mechanisms… **my concern is with code**" |
| 2026-08-18 | "if it isn't a primary guardrail, then it's likely useless" · "We need as little as possible" |

Between instances 3 and 4 — the week whose stated theme was leanness — `tools/` grew 129→130 files
and **CLAUDE.md grew 61,367 → 70,349 bytes**. The execution commit for the leanness plan
(`ed7d0fd`) **net-added 3,448 lines**. Earlier precedent, 2026-06-12: a size guardrail was *widened*
9,000 → 12,000 to accommodate growth rather than the growth being cut.

**Restating the instruction a fifth time will not work. It has never been a comprehension failure.**

---

## 2. The generative mechanism — why every session does this

Three terms. They are **not symmetric**, and the original version of this section said they were.
**T3 is the generator** (audit → finding → row → banner); **T1 is the amplifier** (what floods
attention); **T2 is the reward** (what a session is graded on). Fixing only T3 disarms the generator
— no new self-sourced mandate — but leaves 389 stock items occupying attention, so the recursion
*terminates* while the game still does not get built. Fixing only T1 or T2 leaves the generator
armed. **T3 terminates; T1 and T2 redirect the freed capacity at the game.** Jordan asked for both,
which is why the five acts are right even though "hit all three or nothing" was imprecise.

### T1 — what a session SEES

The SessionStart banner presents roughly **389 named units of pending work**: 242 open EDs (115
needing Jordan), 24 lane items, 6 stale audits, a stale board, an uncomputed repo-state grade.
**None of them concern the game.** The one game line, `M1 0/7 junctures done`, carries no imperative
verb and sits above six `⚠` warnings. The only imperative in the entire banner is
`run python tools/review_core.py --json`.

The banner's own docstring states the design intent (`tools/session_open_work.py:5-18`): it exists
so that "the surfaces where live work actually accrues" — enumerated as lane handoffs, the editorial
ledger, and schema-flux flags — are not missed. **The banner was built, deliberately and
successfully, to make process debt unmissable.**

CLAUDE.md is 70,349 characters re-sent to every session — **86.9% process, 13.1% game-adjacent** —
and §3 alone (repository archaeology: retired trees, alias maps, evacuation history) is 15,876 of
them. Vocabulary: 600 process hits to 150 game hits. Of the 150, 37 are the word *Godot*, appearing
mostly inside the sections explaining why the port has not happened.

And the 13.1% is not *about* the game. It is a **prohibition notice**:
> §5: "Do not bind Godot resource fields to these keys yet."
> §6: "The skeleton is illustrative, not buildable. Do not represent the skeleton as a runnable head-start."
> §7: "handle with care… treat that gap as open."

§9's routing table offers 20 destinations. **Two produce game.**

### T2 — what a session must PRODUCE to be compliant

The Stop hook runs `session_handoff_reminder.py` and `review_core.py --check`. The four things it
rewards: clean tree · HANDOFF updated · progress board fresh · no repo-state regression.
**All four are satisfiable without touching the game. Three are satisfiable only by writing process
prose. No Stop check asks whether an M1 juncture moved.**

A session that spends eight hours authoring `domain_actions` and leaves the handoff untouched gets
nagged. A session that writes a 3,000-line audit and files an ED exits clean.

### T3 — what GENERATES the work

Of 1,233 editorial-ledger rows, **59 (4.8%) cite a Jordan ruling or directive**, while **152 name an
audit, proposal or session document as their source**. The single largest source is
`2026-07-13-multi-agent-audit` — *an audit of the audit apparatus* — which alone generated 14 work
items.

> **Audit-sourced work items outnumber ruling-sourced ones several-fold, and the largest single
> source is an audit of the audit apparatus.** §0 mandates adversarial passes; adversarial
> passes emit findings; findings become ED rows; ED rows appear in the banner; the banner defines
> the next session's work. Closed loop, gain > 1, no human in it.

### 2.1 The doctrine is subject-blind, and that is the whole defect

§0.1 point 5 — *"one owner for the operation, every site routed through it, and a guard that fails
on recurrence — if you cannot write the guard you have not understood the pattern"* — is a good
rule that earned its place. `tests/valoria/test_morale_write_sweep.py` is layer 1, guards real game
state against a real read/write-asymmetry class, and caught what a competent human reviewer missed.

**But the rule quantifies over pattern *defects*, not over *subjects*.** A pattern defect in the
morale model and a pattern defect in the test-register freshness checker are both pattern defects.
The rule fires identically on both. Apparatus outnumbers game 3.9:1 by line, so a session under
"max effort by default" reads more apparatus, finds more apparatus defects, and **mints more
apparatus guards**. The loop gain is (apparatus share) × (defects per artifact) × (guards per
defect ≥ 1), and the first term is 0.8 and rising.

The result, every rung a flawless application of the rule:

> `ci_wf_harness_check.py` (583 lines) guards `wf_harness.js` (369) · `test_wf_harness.py` (472)
> guards the harness · `test_wf_harness_check.py` (294) guards the guard — **1,718 lines guarding
> the prelude of the scripts that run the audits** → every test must appear in `test_register.json`
> (12,514 lines) → its `--check` is blocking → `ci_gate_coverage.py` (210) verifies the check line
> is present in the workflow → `test_gate_coverage.py` (385) tests that → and
> `test_blocking_tier_is_honest.py` (363) is **a test that the blocking tier's membership is honest.**

Depth five. `test_wf_harness.py` is mutation-verified, 13/13 mutants killed. The culling plan is
right that excellence at layer 4 is the most expensive kind of waste, because it is the hardest to
argue with.

Two further specimens, for the record. `ci_claim_provenance_check.py` and
`ci_vacuous_assertion_check.py` are **literal encodings of §0.1 points 3 and 2** — the doctrine has
begun compiling itself into blocking CI gates whose subject is the doctrine. And ED-IN-0190 records:
*"THE INSTRUMENT COUNTED ITSELF, again… recurring verbatim in a new instrument written by someone
who had read that finding."* The prescribed fix was to exclude itself and add
`test_the_gate_does_not_count_itself`. Another layer.

### 2.2 The ratchet has already eaten its own record-keeping

`ci_register_size_check.py:104` caps `editorial_ledger_in.jsonl` at 50,000 tokens, **blocking**.
The ledger entry for last week's work reads:

> "⚠ THIS ENTRY IS DELIBERATELY TERSE: filing it hit the 50,000-token BLOCKING cap on this file at
> 50,048."

And the tool's own comment proposes the remedy: *"a per-lane default would retire it."*
**The reflex to a ratchet symptom is to automate the ratchet.**

### 2.3 A permission gate on `tools/` would not have worked

Over the last 60 commits, by tree: `references` **+116,398** · `audit` **+80,103** · `tests`
**+22,392** · `tools` **+15,619 (5.5%)** · `godot` **+4**.

And the apparatus has already colonised the game's own folders. `systems/` gained 32,954 lines in
that window: design `.md` 4,413 · game `sim/*.py` **922** · generated `_identifier_census.yaml`
**24,598** — one per subsystem, with a blocking freshness gate, living inside every game directory.

---

## 3. The evidence that closes the case

Two facts, either of which alone settles it.

**First — the most valuable game work was never blocked, and nobody took it.**

```
workplans/workplan_v6_progress.yaml
  juncture 1 "Strategic decision" | state: not_started | blocked_on: None | owner: FA
  juncture 2 "Domain action"      | state: not_started | blocked_on: None | owner: IN
  next: "author the domain_actions home (ED-FA-0002) — the single largest M1 gap"
```

`ED-FA-0002` was filed **2026-07-05**. Since then: **242 commits, 0 of 7 M1 junctures closed.** Both
junctures read `blocked_on: None` and the board itself calls it the single largest gap. *(Corrected:
"nothing was missing" overstates it — `workplan_v6_progress.yaml:43` records real unformalized
prerequisites, the score/2 obstacle derivation being "wired NOWHERE" and fractional dice
unimplemented. What survives, and is the point, is that **nobody took it**.)* Every session for six weeks could have taken it. None did —
because nothing they read on startup, nothing they were graded on at exit, and nothing in the
governing document pointed at it.

**Second — the split already happened, and it failed in exactly the predicted direction.**

CLAUDE.md names `jordanelias/valoria-game` as the implementation repo, "frozen since 2026-05-04."
`godot/` in *this* repo has 14 commits ever and **+4 lines in the last 60 commits**. The last `.gd`
file change here was `248f344a`, titled *"[infrastructure] Meta-review lessons converted to
enforcement."*

> **The last time anyone touched the game's code, it was to add enforcement.**

Since the game froze, this repo has taken **1,596 commits and +1,040,549 / −766,721 lines.**

**Splitting the repositories did not move the work to the game. It moved the work to whichever
repository had the apparatus.** A second split, done the same way, produces a second frozen game
repo. This is the decisive counter-evidence against "just start a clean repo," and it is why the
recommendation in §5 is not that.

---

## 4. What is actually over there — the part nobody measured

No instrument in this repository reads the game repository. So this was measured directly.

### 4.1 The game exists, and it is not a skeleton

`jordanelias/valoria-game`: a real `project.godot`, **128 `.gd` files / 19,490 lines**, 8 `.tscn`
scenes, 37 `.tres` resources, and **six wired autoloads with a documented dependency chain** —
`Meta` (877) · `EventBus` (107) · **`KeyStore` (265)** · `SceneTimer` (353) · `GameStateMachine`
(149) · `GameDirector` (584). Six scene containers exist: board, combat, conflict, narrative,
debate, battle. It has its own CI. `docs/conversion_ledger.md` records Phase 0 and Phase 1 COMPLETE.

Meanwhile `godot/skeleton/` **in this repo** is 8 files, 155 lines for the combat slice, and
`extends BaseEngine` / `EngineModule` — classes that exist in **neither** repository. It is a
non-compiling re-draft, against an invented architecture, of code that already works next door.

### 4.2 The Key substrate inversion

`engine/substrate/keys.py` (601 lines) is good code that **almost nothing uses**: exactly 3 files in
the entire Python game code ever instantiate a `Key`, and `grep -rn "KeyBus\|class KeyStore"` across
the Python returns **zero**. The 24 modules importing `engine.substrate` are importing `stubwire` —
a marker for "not built" — not `keys`. The Python reference is a call-graph, not an event-bus graph.

`valoria-game/autoload/KeyStore.gd` **is** the PP-687 substrate: `emit / subscribe / walk_back /
walk_forward / log_hash / reset_for_replay`, per-emission RNG seeding, stable sort ordering, cycle
blocking, plus `Key.gd`, `KeyTypeRegistry.gd`, `KeyValidator.gd` and a test file.

**The design repo has spent months specifying a substrate that the Godot repo implemented in April
and the Python reference never adopted.** Gate-0's premise — "build KeyStore v2" — is false.

### 4.3 The key-type gap is exactly twenty rows, and they are nameable today

Canonical roster (`engine/engine_params/key_types.json`): **55**. Godot roster
(`systems/keys/KeyTypeRegistry.gd`): **35**. **In Godot but not canonical: zero — a strict subset,
no drift.** Missing, in full:

`mechanical.{era_transition, project_advanced, second_calamity, settlement_captured,
theocracy_unification_declared}` · `scene.{accord_echo, combat_felled, combat_hit, combat_resolved,
combat_strike, displacement, draft_da, gossip, interaction, thread_operation}` ·
`state.{concern_resolved, opinion_revised, project_completed, project_failed, settlement_revolt}`

Gate-0 item G0.4 says "register missing Key types (`scene.combat_resolved`, `scene.thread_operation`)."
It named **2 of 20**. The real fix is a twenty-line diff to one GDScript dictionary, and it has been
"blocked" for 106 days.

### 4.4 The "single largest M1 gap" is already implemented

`valoria-game/systems/engine/DomainActionSystem.gd` — 276 lines, `class_name DomainActionSystem`.
Its docstring is a better spec than the missing document would be:

> Phase 1 — `roll(action, meta, rng) → Enums.Degree` — board dice only, no consequences
> Phase 2a — `scene_for(action, degree, meta) → SceneOpportunity | null` — with `ob_modifier`
>   **derived from the board degree**; null if it resolves abstractly
> Phase 2b — `resolve_abstractly(action, degree, meta) → Array[Consequence]` — when the player declines
> **"This split enables the core zoom mechanic: board roll → degree → scene difficulty."**

That is the strategic↔personal bridge — the thing Valoria *is* — working, in GDScript, consumed by
`FactionTurnSystem`, `ValoriaFactionAI`, `GameDirector`, `DebateContainer`, `BattleContainer`.

### 4.5 The unnamed tenth attribute is `Recall`

`references/descriptor_registry.yaml:39-43` blocks all Godot field binding — a flag echoed in
CLAUDE.md §5 and printed to every session at startup:

> "THE COUNT IS RULED; THE ROSTER IS NOT COMPLETE. Jordan, 2026-08-14: 'it will be 10 attributes'.
> NINE are defined below. **The TENTH IS UNNAMED — naming it is the open workshop**… Until the tenth
> is named, 'IN FLUX' stays and **Godot fields stay unbound**."

`CharacterCreationManager.gd:146-151` allocates 31 points across ten named attributes: *agility,
endurance, strength, cognition, recall, focus, attunement, bonds, charisma, spirit.* Applying the
registry's own alias rules (Cognition→Acuity, Spirit→Will), **nine map exactly. The unmatched tenth
is `recall`** — and it is excluded by neither of the two candidates the registry's warning rules out.

It is not a stub. 19 references: `@export var recall` on `CharacterData.gd:18`; an
`effective_recall(coherence_state)` with −1D/−2D degradation; **the investigation dice pool**
(`InvestigationSystem.gd:88,97`); a `recall / 2` learning bonus in `SkillSparkingSystem.gd:125`;
History `dice_bonus ≤ recall` validation; and seeded values across six named characters
(`prudence_cardinal = 5`, `peder_almstedt = 5`, `doux_laskaris = 4`).

**A blocking flag on the whole Godot pipeline has been waiting since 2026-08-14 to name something
that shipped in April, in the repository the design exists to serve.**

*Corollary, and it is a real risk: the registry folds Spirit→Will and Cognition→Acuity. The game
treats both as distinct live `@export` fields. Ratifying those folds is a breaking rename against
shipped code and shipped `.tres` data.*

### 4.6 The game was compiled for the first time in its history

Godot 4.3-stable was downloaded and run headless against the game. **No session in this project has
ever done this.** Bisected result:

| state | error lines | scripts failing to load |
|---|---:|---:|
| as committed on `main` | 58 | 7 (all 5 autoloads + CombatLogic + GameDirector) |
| after fixing 5 root causes | **121** ⬆ | 27 |
| + one `project.godot` warning setting | **16** ⬇ | **3** |

The middle row is the instructive one, and I nearly mis-reported it. Godot reports only the *first*
parse error per file, so fixing the top layer uncovers the layer beneath — "it got worse" is the
wrong reading, and so was "only 5 defects." Neither number means anything until bisected.

The bisection: the dominant failure class was **one Godot version change, not 27 defects.** Godot
4.3 promoted `INFERENCE_ON_VARIANT` to an error by default; the code was written against earlier
semantics where `var x := some_dict[k]` was legal. Two lines in `project.godot` took it from 121
errors and 27 broken scripts to **16 and 3**. Every scene container, every `systems/` module, and
five of six autoloads then load.

**That failure class is CLAUDE.md §0.1's own definition of a pattern defect** — *"the broken code
was correct when written and stopped working because something else changed."* The repo has a
doctrine written for precisely this, and a five-layer guard stack enforcing it. It has never been
pointed at the game.

Five root causes were found in the production code, and one of them indicts the cross-repo ledger:

| # | defect | note |
|---|---|---|
| 1 | `Meta.gd` uses `_victory_candidates` at **7 sites** and never declares it | |
| 2 | `CharacterData.gd:104` — `composure_max = charisma + Constants.COMPOSURE_BASE` | **ED-694 changed Composure to Cha×3; `COMPOSURE_MULTIPLIER` was added, the call site never migrated, and `docs/design_sync.md` claims "✓ Updated (Composure Cha×3)". That tick is false and has been for months.** |
| 3 | `PackedByteArray.sha256_buffer()` is not a Godot 4 API — 3 sites incl. `KeyStore.gd:212` | |
| 4 | `Enums.SceneType` omits `BOARD`, used at `SceneSystemMap.gd:31,45` | **`BoardContainer.tscn` and `ConflictContainer.tscn` are built. The strategic layer's own scene container is unreachable through the enum.** |
| 5 | remaining: `Meta.gd`, `GameDirector.gd`, `CombatLogic.gd`, `ValoriaFactionAI.gd` | ~5 typed-declaration fixes |

**Honest bound, stated plainly.** "Scripts load" is not "the game runs" and is certainly not "the
game is correct." This measures parse and load only, and the behaviour it would load is April's
rules — predating the 2026-08-14 degree-ladder unification, the d10 strategic dice, and the
`CONQUEST_MIN_MIL` deletion. What it establishes is narrower and still decisive: **the premise that
the Godot port is a large unstarted project, which is what defers it behind Gate-0 and behind
M1+M2, is false.** It is roughly a day of typed-declaration work from loading.

Two further honest facts about that repo: `addons/` does not exist, so the 14 test files (which use
**gdUnit4**, not GUT as the README claims) **have never run**; and its CI is three grep checks with
no Godot binary, no compile step and no test step.

---

## 5. The change that ends it

### 5.1 The principle — corrected

**The original version of this section was wrong and is replaced. It read: "the recursion is
possible because this repository has no external referent."** The refutation is in §7.2 and it is
decisive: the engine already has external referents, and the deepest guard stack in the tree grew on
top of the strictest one.

Here is the corrected principle, which is narrower and survives the attack.

An external referent adjudicates only the claims inside its reach. A compiler rules on *does this
load*; a byte-exact golden rules on *is this output identical*. Neither can rule on *is the pin
present*, *is the register fresh*, *is the blocking tier honest*. Those meta-claims are unbounded,
and a subject-blind doctrine that mints a guard per observed defect will keep producing them
**however good the referent underneath is** — demonstrably so, since that is exactly what happened
above the goldens.

So the referent's real job is not to terminate the loop. Its job is to make **one specific claim
un-prose-satisfiable**: the definition of *done*. Today an M1 juncture closes when a document exists
with a `## Status:` line — a claim checked against other claims. With a compiler wired to the board,
it closes when the behaviour executes. That is what Acts 1–2 buy, and it is worth buying.

**What terminates the loop is Act 4**, because the loop's generator is doctrinal: the rule that
converts every observation into a permanent new artifact. Order of causal weight:

> **Act 4 terminates. Acts 1–2 anchor. Act 3 tests whether the diagnosis was right.**

**Two caveats that decide whether Act 1 works at all.**

**A referent nobody reads is the 2026-05-04 split again.** Act 1 puts the compile job in
`valoria-game`'s CI — a repo whose state no session here has looked at in 106 days. If the
compiler's verdict never reaches *this* repo's attention and reward surfaces, Act 1 reproduces the
arrangement it diagnoses, with a better gate. The fix is one line: **Act 3's single banner line must
carry the referent's verdict** — `game compiles: YES/NO · M1 juncture N: <next increment>` — and
Act 2's "done = it runs" must read that same signal.

**And the referent is writable.** §0.1's own origin story is a confounded change that **re-recorded
two byte-exact goldens** to agree with it, and shipped. This very session moved the compile from 121
errors to 16 with two `project.godot` warning-severity lines — legitimately, but it demonstrates the
point. A compiler is much stiffer than prose. It is not incorruptible. The difference is degree, not
kind, and Act 4 is what keeps the stack from regrowing around it.

This is still why the 2026-05-04 split failed, and the diagnosis there is unchanged: it moved the
*files* without installing a referent on either side, and left every attention surface here. But
note precisely what that does and does not prove — it is decisive against "just start a clean repo,"
and it is *not* evidence about referents, because no referent experiment had ever been run until
this session ran one.

> **Install an arbiter that is not made of prose, and the loop opens.**

This is why the 2026-05-04 split failed and why another one would fail: it separated the *files*
without moving the *referent*. The design repo remained the place where truth was decided, so the
work followed it. The fix is not to move the game away from the apparatus. It is to **make the
running game the thing the apparatus is accountable to** — to invert the polarity, so the design
repo documents a working artifact instead of specifying an imagined one.

### 5.2 The five acts, in order

**Act 1 — make the game load, and put a compiler in CI. (~1–2 days)**
Fix the five defects in §4.6, add the `project.godot` warning setting, and add **one** job to
`valoria-game`'s CI: open the project headless and fail on any script load error. That job is a
layer-1 guard with an external referent. It cannot be satisfied by writing prose, cannot be gamed,
cannot generate a finding about itself, and it replaces more assurance than the entire five-layer
stack in §2.1. Vendor gdUnit4 and run the 14 tests that have never run.

**Act 2 — redefine "done" as "it runs." (one edit to the board)**
An M1 juncture closes when the behaviour executes in Godot, not when a document exists with a
`## Status:` line. This is the single highest-leverage edit available, because it is what the Stop
hook and the banner both ultimately read.

**Act 3 — change what a session sees. (one file, one hook)**
Replace the SessionStart banner's ~389 apparatus items with **one line**: the current M1 juncture
and its next concrete increment. Cut CLAUDE.md to a governing document that names a deliverable
rather than a process. This is also the **cheapest falsifiable test of the whole diagnosis**: change
nothing else, print `M1 juncture 2 (Domain action): DomainActionSystem.gd exists — port or ratify
it. blocked_on: nothing.`, and watch one session. If it still writes apparatus, the ordering here is
wrong and this document should be attacked accordingly.

**Act 4 — amend the doctrine. This is the act that terminates the recursion. (three edits to CLAUDE.md)**
The culling plan deletes stock. These three change flow. **All three wordings below are the
post-adjudication versions; the first drafts are recorded in §7.2 with the cases that broke them.**

- **§0.1 pt 5 — predicate on what the artifact is LOAD-BEARING ON, not on what it is about.**

  > *A pattern defect earns a guard only if the defective artifact is load-bearing on the game or on
  > a Jordan decision — its output crosses into the engine, the exported params, the port, or the
  > `needs_jordan` queue. A pattern defect in an artifact that is load-bearing only on this
  > repository's process is not evidence the artifact needs a guard; it is evidence the artifact can
  > be wrong without cost. Delete it, or accept the defect and write nothing.*

  My first draft predicated on *subject* ("a tool, a test, a register…") and a real case breaks it:
  `tools/export_engine_params.py` and its round-trip `--check` are apparatus by subject, but the
  artifact they produce is the bridge the Godot port ingests. A silent key-drop after a schema
  change is the exact "correct when written, broke when something else changed" signature — and the
  subject predicate would have said *delete the exporter*. Same failure for the compile gate Act 1
  installs. The load-bearing predicate keeps `test_morale_write_sweep.py`, `ci_golden_modes_check`,
  `ci_sim_fabrication_check` and the compile gate; it forbids `test_wf_harness_check.py`,
  `test_gate_coverage.py`, `test_blocking_tier_is_honest.py`.

  ⚠ **This edit must land with the next one or it reroutes rather than closes.** A session forbidden
  to write a guard will write a *finding about the defect* instead. The loop's carrier is prose.

- **§0 adversarial pass — keep the requirement, bound the product, and name the one channel that survives.**

  > *The adversarial pass is a stage of the work, not a deliverable. Its output is edits to the thing
  > under review and at most one paragraph in the commit message. It does not create a directory or a
  > document. It may append at most one ledger row, and only if the row requires a human decision
  > (`needs_jordan: true`). A finding that needs no ruling is either fixed in this commit or dropped.*

  My first draft banned creating "a register" and left fatally ambiguous whether that meant a
  register *file* or a register *row*. Rows are the loop's carrier — but they are also the only
  persistence channel across a session boundary, and this repo has no context between sessions. Ban
  rows outright and a real cross-lane game defect evaporates at Stop; allow them freely and T3's gain
  stays above 1. Gating rows on `needs_jordan` **makes the human the low-pass filter on the only
  surviving channel** — gain below 1 by construction, because the loop can no longer feed itself work
  no human ordered. It is also exactly consistent with Act 5's reduction of the ledger to
  `needs_jordan`. All four of the pass's verified catches were pre-commit corrections; none required
  a corpus. This deletes `audit/` **as a category**, not as a cleanup.

- **§0 max effort — supply the missing *selection* term, with two carve-outs that are needed and bounded.**

  > *Max effort on the deliverable named by the current milestone, where a juncture is done only when
  > the behaviour executes (Act 2). Work is this session's work if Jordan asked for it this session
  > or it traces to an open M1 juncture; nothing else is. If something broken blocks the milestone,
  > fix it minimally, without adding a guard.*

  My first draft omitted both carve-outs and the literal reading told a session to **refuse Jordan** —
  "rule on the tenth attribute", lore authorship, and this very interrogation trace to no juncture.
  The second carve-out covers a red `main`, which blocks everything and traces to nothing; it is
  bounded by *minimally, without adding a guard*, because unbounded carve-outs are how the apparatus
  grew. The diagnosis behind the edit is unchanged and is the sharpest thing in this document:
  "exhaustive" is satisfiable on apparatus (107 tools are enumerable) and unsatisfiable on the game,
  so **a doctrine demanding exhaustiveness drifts to whichever surface is enumerable** — and *"the
  harder-but-correct fix over the local patch"* literally instructs the agent to prefer the option
  that grows the tree.

  ⚠ **Act 2 is a precondition of this edit, not its sibling.** Binding max effort to "the milestone
  deliverable" only helps once *done* means *it runs*. If done still means "a document exists with a
  `## Status:` line," this edit aims maximum effort at authoring `domain_actions` **prose** — the same
  output, better targeted.

**Act 5 — then cull, but only the half that is safe.** A structurally independent read-only critic
was pointed at the culling plan and recounted every figure against the tree. Its verdict, which I
adopt: **the measurements are unusually good — better than this repo's baseline — and the execution
plan is unsafe.** 20 of 24 recounted figures confirmed, several to the digit; all nine cited CI line
numbers and all eight `valoria_local.py` line numbers exact. But:

- **§6b's load-bearing premise is false.** `ci_claim_provenance_check.py:54-90` — **blocking in CI
  (`valoria-ci.yml:124`) and locally (`valoria_local.py:175`), and kept by the plan** — scans the
  **body text** of all four ledger files for `MEASURED-BY:` and fails when the named instrument is
  absent from the tree. §6b deletes two of its four inputs and strips the other two. Worse, archived
  rows name ~9 of the tools the cull deletes as their instruments. **Each of those deletions turns a
  kept blocking gate red.** This row is not in the plan's risk register.
- **Waves 1–3 each red the plan's own post-wave gate**, because tests deleted in wave 3 dynamically
  load wave-1 and wave-2 targets — and two tests in *no* wave, inside modules §7 keeps
  (`test_ci_common.py:89-91`, `test_ci_common_primitives.py:687-693`), do the same. Wave 1's verify
  command greps `.github .githooks tools/valoria_local.py` — **not `tests/`, not `skills/`.** The
  plan's own top risk is "load-bearing in a way grep missed"; the mitigation ships with the blind
  spot pre-installed.
- **`valoria_local.py` degrades to a silent pass.** `:256-258` skips a missing tool; `:289` still
  prints "all local gates passed." The only path that treats absence as failure is `run_ci_validators`
  — which wave 3 deletes.
- **Two of three cited callers in its central dependency table are prose** — `ci_hooks_verifier:93`
  is inside a comment documenting a *false positive*; `dead_primitive_census:9` is a docstring. The
  plan grepped for filenames and reported the hits as callers, which is this repo's own named
  costliest error class.

**⚠ CORRECTED 2026-08-18 — the disposition below replaces an earlier one that was wrong in the more
damaging direction.** This document first said: *"execute waves 4, 5, 6a and 6f, and refuse waves
1–3 and 6b as written."* A second independent critic overturned both halves, and it was right:

- **Waves 1–3 *are* the flow.** They contain `audit-refresh.yml` (the weekly
  regenerate-and-open-PRs loop), `dashboard.yml`, the `wf_*.js` orchestration that **produces** the
  machine lens-output — the two largest files in `audit/`, 57,772 and 24,999 lines, **46% of the
  corpus by the plan's own §2** — plus the `review_core` Stop hook and the banner machinery.
  "Execute 4/5/6a/6f, refuse 1–3" therefore deletes 273,000 lines of accumulated stock **while
  leaving every producer running.** That is stock removal with the tap open, and it is precisely the
  error this document accuses the culling plan of.
- **6a cannot execute while 6b is refused.** The plan's own sequencing (`6b ──► 6a`) is a hard gate,
  and the measured precedent is inside the tool: `tools/validate_ed_citations.py:353-361` records
  that when just `deprecated/archives/editorials/` left the archive walk, the citation universe fell
  **1167 → 1107 and 110 valid citations became NONEXISTENT** in a blocking gate.

**The corrected disposition:**

| item | ruling |
|---|---|
| **Waves 1–3** | **Repair, not refuse.** Every defect found is a *manifest* error — tests and callers assigned to the wrong wave or to no wave — not evidence the targets are load-bearing. Union each wave's deletions with the tests and callers that touch them, in the same commit. |
| **6b** | Rewrite first (add the `ci_claim_provenance_check.LEDGERS` edit, rehome `test_claim_provenance_archives.py`, handle open rows citing deleted instruments), then run it **before** 6a. |
| **6a** | Execute only after the rewritten 6b, or carve the ledger archives out of it. |
| **Wave 4** | Execute, with two additions to its resolution list — see the oracle finding below — and `honest_gauge_readout.md` added to the extract set. |
| **Wave 5** | Execute only after regenerating the flip list against whichever waves actually ran. As written it names two already-deleted tests and **omits `build_identifier_census --check`**, which is blocking at `valoria-ci.yml:122` and diffs a wave-5 untrack target. |
| **6f** | Execute; lowest risk. Residue: CLAUDE.md §6 still points at the four forked stale docs — one more doctrine-orphaning instance. |

**Three things no wave touches, and the first is the one that matters most.**

**The generator is in the prompts.** Seven kept `SKILL.md` files carry an identical instruction
ordering every run to append to `references/audit_registry.jsonl` *"so the GitHub Pages dashboard and
`tools/ci_audit_registry_check.py` can see it. **Do this every time**"* — `valoria-canon-guard:89`,
`valoria-editorial-register:407`, `valoria-mechanic-audit:135`, `valoria-module-adjudicator:173`,
`valoria-resolution-diagnostic:363`, `valoria-simulator:276`, `valoria-vector-audit:385`. Wave 1
deletes the dashboard; wave 2 deletes both consumers. **No wave edits a single skill.** Post-cull,
every kept skill still instructs sessions to grow a registry nothing reads. **This is the flow layer,
and neither the plan nor the first version of this document put it in any wave.**

**A §7-kept gate's oracle lives inside wave 4's fork target.** `tools/gen_sigma_parity_goldens.py:10,152`
executes `audit/2026-06-03-contest-groundup/engine.py` as one of its two oracles, and its own
docstring records that the file cannot move. Forking `audit/` wholesale makes
`engine/tests/goldens/sigma_leverage_parity.json` a **second** frozen non-regenerable source —
falsifying §5.1's "it is the only file in this state; every other generator was located."

**The §6 merge quietly demotes a blocking gate.** `ci_register_size_check` is *locally* blocking
(`valoria_local.py:160`); `compliance_check` is deliberately excluded from the local list. Merging
the cap into `compliance_check` moves it from both-tiers-blocking to CI-only — so the ledger-headroom
failure this document's own header narrates would in future surface only after push.

**Two amendments that stand unchanged:** do **not** create `registers/ed_tombstones.yaml` as
specified (a new 1,150-line hand-maintained register, sequenced first, is apparatus built to retire
apparatus — rewrite it per the table above); and reduce the ledger to the one thing in it that is
load-bearing — **`needs_jordan`**, the only genuine human-decision queue in the repo, 115 items.
Delete status, description, falsifier, measured_by, citations, lane splits, archives and caps.
1,233 rows → ~115 lines.

Two structural findings from the same review belong here rather than in a wave.

**The apparatus has colonised the game engine's source shape.** `engine/substrate/stubwire.py` sits
inside the plan's 29,570-line "Game engine" row and is therefore protected — but its own docstring
says its purpose is to be *"composed on by `structure_audit.py` (the `stub_wired` node attribute)
and `review_core.py` (the `stubs.count` ratchet signal),"* and `:46-50` justifies its counter design
because *"resetting on every call would make the counter useless for the ratchet signal in
`tools/review_core.py`."* It returns a typed no-op. Three further kept
engine files carry the same reasoning verbatim — `engine/cross_scale/articulation.py:26-28`,
`engine/autoload/npc_ai.py:25-27`, `engine/cross_scale/scene_dispatch.py:363-365`.

> **Game-engine code is now being written in a shape chosen to be legible to the audit apparatus.**
> That is the recursion reaching its final surface, and no cull that classifies by directory can see it.

**And the plan never measured the game.** `grep -in godot` over its 432 lines returns **exactly one
hit**. `godot/` is in neither of §2's two "the thing" rows, not in §7's Keep list, and not in §8's
target table. §8's end state is stated entirely in line counts — no runnable target, no build step,
no `project.godot`, no scene, no acceptance criterion a human could play. Meanwhile
`rg 'doc: null' references/module_contracts.yaml` returns 10 — the named porting blocker — and 6e
touches that exact file to reorganise it while authoring none of the ten.

### 5.3 Six things that are true today and cost hours, not milestones

Each is unblocked right now, and each moves the game rather than the repository.

1. Name **Recall** as the tenth attribute (§4.5). Closes ED-IN-0193, clears "IN FLUX", and lifts the
   standing "do not bind Godot fields" flag that is printed to every session.
2. Add the **20 missing Key types** (§4.3). A twenty-line diff; closes Gate-0 G0.4.
3. Mark Gate-0's "build KeyStore v2" **already satisfied** (§4.2) — `KeyStore.gd` is 265 lines and wired.
4. Close M1 junctures 1–2 by **pointing them at `DomainActionSystem.gd`** (§4.4). The document that
   "does not exist" is a docstring away from existing.
5. Fix the five compile defects and add the compiler to CI (§4.6).
6. Correct `docs/design_sync.md`'s false "✓ Updated (Composure Cha×3)" and delete
   `godot/skeleton/` — 155 non-compiling lines against an invented architecture that actively
   misdirect anyone who reads them as a head start.

---

## 6. What I am not claiming

- **Not that the apparatus catches nothing.** `test_morale_write_sweep.py`, `ci_golden_modes_check`
  and `ci_sim_fabrication_check` are genuinely load-bearing on game correctness. The adversarial
  pass killed three candidate findings in `926dbc2d`, refuted three of its own claims in `fdbef6bc`,
  found seven defects in `1e3e0e1e`, and refuted its own headline claim last week. **Any cut that
  treats all apparatus as equivalent will destroy real value.**
- **Not that sessions do no game work.** ~112 game test files / 19,285 lines exist, and
  `engine/mc_v18.py` runs a 50-season campaign in 2.4 seconds producing a winner and a deterministic
  key-log hash. The narrower true claim: substantial game work happens in **personal combat and mass
  battle**, and essentially none on the M1 critical path or the port.
- **Not that the Godot code is better than the Python.** It is not. The Python engine is 33,235
  lines to 19,490 and is mechanically far ahead. The Godot repo's value here is that it is an
  **external referent** and a **working scaffold**, not that it is the superior artifact.
- **Not that the culling plan is wrong.** It is an unusually honest inventory, and it caught its own
  session's errors. It is *insufficient*, and its §7 "Keep" list ends with `CLAUDE.md` — the
  document that generates what it is deleting.

## 7. The falsifier

Per §0.1 point 3, stated in the same document as the claim.

**This diagnosis is wrong if T1 is not the binding term.** The test is in Act 3 and costs one
session: replace the banner with a single game-work line, change nothing else, and observe. If the
session still produces apparatus, the ordering here is wrong — the binding term is T2 or T3 — and
Acts 1–2 should be re-sequenced ahead of Act 3.

**A second, cheaper falsifier:** if fixing the five compile defects does not produce a loading
project, then §4.6's central claim — that the port's blocking premise is false — collapses, and the
Gate-0 sequencing in `godot_conversion_strategy_v1.md` is vindicated.

### 7.1 What this document cost to commit — measured, not argued

Committing these two prose files ran the full gate set. Results, in order:

- `tools/valoria_local.py --staged`: **blocking gates passed**; one report-only failure,
  `scope_ratchet`, which was **already REGRESSED before my change** (`ed.stale` 198 vs ceiling 76,
  `ed.needs_jordan_stale` 83 vs 21 — byte-identical before and after, verified against a stash).
- My own contribution to the ratchet, stated rather than hidden: `proposals.open` **13 → 15**,
  `tracked.files` **1431 → 1433**. A document about accretion is itself +2. That is why it carries a
  death date in its status line.
- `pytest tests/valoria`: **1 failed, 1932 passed.** The failure was
  `test_build_glossary.py::test_committed_output_matches_a_fresh_build`. Verified by stash that it is
  caused **solely by adding two `.md` files to `proposals/`**: clean before, failing after.
- The remedy the gate demands is to regenerate `references/glossary/`. Cost, measured:

> **1,366 lines of hand-written prose forced 21 generated files to change, +451 / −319.**
> Suite green afterwards.

Then the regeneration tripped a *second* gate, and this one is sharper than the first.
`ci_names_check` (report-only locally, blocking in CI) reported **17 naming-drift hits** — every one
of them in `references/glossary/*.md`, every one the same deprecated term "Rendering Stability" in
the **Coherence** definition. Traced:

- occurrences in my prose: **zero** (`grep -c` across all three files)
- true origin: `systems/threadwork/*` and `systems/world/calamity_radiation_v30_infill.md` — real
  upstream design docs
- occurrences already on `main` in `MASTER_GLOSSARY.md`: **1**

**Nothing changed. The regeneration reflowed lines that already existed, so a drift gate scanning
"added lines" fired 17 times on content that has been in the tree all along** — and it names, as the
offender, generated output rather than the two design documents that actually contain the term.

That is the whole mechanism, executed live, in the commit that describes it: prose edit → stale
generated artifact → blocking gate → regenerate → 770 lines of generated churn → a second gate
firing 17 false positives at the regenerated copy of an unchanged upstream term. `glossary.json` is
the same 68,473-line artifact that was **44.5% of last week's entire diff**, rewritten in 8 of 15
commits. Untracking it is wave 5 — one of the four waves §5.2 recommends executing, and this is the
argument for it in one paragraph.

**And then it happened a third time, in CI, on the commit above.** `test_engine_atlas::test_atlas_is_current`
failed on PR #319 — the atlas was stale. The diff, in full:

```
-| `mass_battle` | 2518 |      +| `mass_battle` | 2520 |
-| `threadwork`  | 2273 |      +| `threadwork`  | 2277 |
-| `social_contest` | 2207 |   +| `social_contest` | 2210 |
-| `victory` | 2112 |          +| `victory` | 2114 |
```

Four counters moved by two-to-four each, because **this document names those subsystems in prose.**
Nothing about the engine changed. A blocking gate failed because a design document mentioned the
names of design subsystems.

The culling plan predicted this defect in the exact words — *"three times in one session an edit to
prose staled `engine_atlas.json` and failed a blocking gate — once because the word 'audit' appeared
one more time in a comment"* — and it is the standing argument for wave 5.

**Tally for one prose-only commit: three separate generated artifacts staled, two blocking-tier
failures, one report-only failure firing 17 times at unchanged upstream content, and ~800 lines of
generated churn attached to 1,400 lines of writing.** My own error is in there too and is worth
naming: after the last edits I ran targeted tests instead of the full suite, so the atlas failure
reached CI rather than being caught locally — which is CLAUDE.md §0.1's *"check the gate that gates
the thing"* committed by the document that quotes it.

**This section is the artifact §0.1 point 3 asks for: the specific checks that would have shown the
claim wrong, run, with their outcomes — including the three that fired at me.**

---

### 7.2 Adjudication record — what Fable 5 overturned, and the evidence that did it

Fable became available after this document was first merged (PR #319) and ran three read-only
nodes against the tree. **It refuted the headline and overturned the culling disposition.** Both are
corrected above. The superseded claims are recorded here rather than deleted, per this repo's
standing convention that a corrected claim stays visible with its correction.

**SUPERSEDED CLAIM 1 — the headline.** *"The recursion persists because the repo has no external
referent; every claim is checked against another claim inside it. The single change that terminates
it is to install an arbiter."*

**Refuted by the tree.** The Python engine has hard external referents: the interpreter executes it,
`mc_v18` emits a deterministic key-log hash, `engine/tests/` is a seeded regression suite, and
`tools/ci_golden_modes_check.py` compares battle output **byte-exactly** against recorded goldens in
three pinned modes. And the deepest guard stack in the repository grew on top of the strictest of
them. In the gate's own words (`ci_golden_modes_check.py:1-22`): the goldens sat red for five days
undetected → a gate was built → *"minimal pinning is how ED-1089 went wrong"* → a **pin doctrine** →
an inventory of **85 unique env names swept twice, independently, with an adversarial critic pass**
→ `tests/valoria/test_field_golden_pins.py` asserting completeness → and
`tests/valoria/test_cell_exclusion_no_deadlock.py:133`,
**`test_exclusion_flag_is_pinned_in_the_golden_gate`** — a test that a flag is pinned in the gate
that checks the goldens. Layers 2–4, minted on a byte-exact external referent.

The corrected causal statement is in §5.1, and it was already present in this document's own §2.
**The headline contradicted the mechanism section directly beneath it.**

**SUPERSEDED CLAIM 2 — the culling disposition.** *"Execute waves 4, 5, 6a and 6f; refuse waves 1–3
and 6b as written."* Wrong in both halves; corrected in §5.2. Waves 1–3 contain the producers, so
refusing them removes stock and leaves the tap open; and 6a is hard-gated on 6b by the plan's own
sequencing, with a measured precedent of **110 valid citations turning NONEXISTENT** in a blocking
gate (`tools/validate_ed_citations.py:353-361`).

**Corrections to individual numbers and phrasings**, all applied above:

| was | now | why |
|---|---|---|
| "154 tools added, 24 deleted" | **128 added, 21 deleted** | both figures were in the working log 30 lines apart; §0 quoted the unreconciled pair |
| "monotonic layer accretion" | **accretion with function migration** | 8 of 21 deletions had their function rebuilt under a different name; `extract_values.py` → `export_sim_params.py` (9-day gap) is the one true delete-then-rebuild |
| "~95% of its own mandate" | **audit-sourced items outnumber ruling-sourced several-fold** | 95% = 100% − 4.8% treated every non-citing row as self-generated, including rows that *execute* rulings |
| "no gate, no missing ruling, no dependency" | **"nobody took it" survives; "nothing was missing" does not** | `workplan_v6_progress.yaml:43` records real unformalized prerequisites |
| `stubwire` "does nothing in the game" | claim dropped | it feeds `mc_v18`'s `CampaignResult.stub_hits`, and `engine/tests/test_pipeline_reach.py` consumes the `stub_wired` contract. The colonisation of *rationale* is real; of *behaviour*, not shown |
| "every one of those deletions turns a kept blocking gate red" | **some may; not every one** | `ci_claim_provenance_check.py:104-110` validates only rows matching five claim patterns, so a row citing a deleted tool can pass green — demonstrated live on `main` for `measure_stamp_false_positives.py` |

**What survived the adjudication unchanged**, verified independently and often to the digit: the
depth-5 guard chain at every cited line count; the banner contents; the `stubwire` docstrings; the
ledger cap self-consumption; the reduction paradox; the ratio measurements; every game-repo fact in
§4 including the false `design_sync.md` tick; and the Recall derivation in §4.5 — which was
**upheld and strengthened**, since `engine/engine_params/params_tables.yaml:9104-9122` names the
roster outright, inside this repo, making the game-repo derivation unnecessary. The finding is worse
than stated: canon named the tenth attribute, the 2026-06-06 registry ratification dropped it along
with the whole Metaphysical group, and the loss was then formalised as "the open workshop."

**The falsifiable prediction this leaves on the record:** ship Act 1 without Act 4 and the compile
gate acquires its own stack within weeks — a `ci_gate_coverage` row asserting the job is present, a
test of that, a freshness pin on the Godot version. Every ingredient already exists, and
`ci_gate_coverage.py`'s stated job is literally to verify a check line is present in the workflow.

---

## 8. Working log and status of the Fable nodes

The full evidence log — every measurement with its command, every raw agent finding including the
ones that refuted my own claims — is at `proposals/2026-08-18-recursion-interrogation-log.md`,
committed alongside this file. **Both files are deleted in the same commit that rules on this
proposal.**

All three suspended Fable nodes are now **DELIVERED**, and their results are folded in above:

| node | subject | outcome |
|---|---|---|
| F1 | causal-mechanism adjudication | **Refuted the headline** (§7.2); sharpened all three Act-4 wordings; corrected four numbers |
| F2 | adversarial re-run against the culling plan | **Overturned the disposition** (§5.2); found the SKILL.md generator, the wave-4 oracle, and the wave-5 flip-list staleness |
| F3 | independent verification of the Recall derivation | **Upheld and strengthened** — canon names it directly at `params_tables.yaml:9118` |

Nothing in this document is now awaiting a model. What it awaits is Jordan's ruling on the three
held items in the PR body, and on the corrected culling disposition in §5.2.

**A live handoff for the next session — what to do first, in order, with the state it needs — is at
`proposals/2026-08-18-next-session-handoff.md`, pointed to from root `HANDOFF.md`'s "Next actions",
the only section the SessionStart banner reads.**
