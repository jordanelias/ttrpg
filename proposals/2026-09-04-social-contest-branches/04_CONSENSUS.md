# 04 · CONSENSUS — enact a unity

## §0 · Status, grade, and what a veto costs

## Status: **PROPOSED — nothing ratifies.** 2026-09-04, SC lane. This is a branch proposal against `00_BRANCH_SHAPES.md` §5. Merging it ratifies nothing: no code is changed, no ledger row is closed, no `## Status:` line is flipped anywhere else. A later phase executes it.

**Paper/executes grade (`CLAUDE.md` §0.2): PAPER.** Nothing in this document runs. What runs *today*, verified by reading:

| piece | state |
|---|---|
| `VoteAtClose` weighted per-juror ballot | **executes**, and is on the campaign golden path — `scene_dispatch.py:118 EMERGENCY_COUNCIL_PROCEEDING = "guild_arbitration"` → `panel` adjudicator → `wrapper.py:181-190` rebuilds the venue with `panel_win_condition()` → `resolver.py:128` weighted branch |
| the frivolity antibody (`DefeatCatalogue` evasion clinch) | **executes** — `primitives.py:277`, checked per move inside `resolver.py:453` |
| the eristic antibody (`cr5_self_backfire`) | **executes**, but only behind an armature the seam cannot supply (`wrapper.py:110 build_contest` has no `armature=`) |
| `aggregation="unanimity_required"` | **does not exist** — a self-flagging `StubResult` (`dictionaries.py:721`) |
| per-member ballot retention | **does not exist** — ballots are counted and discarded (`resolver.py:139`, `:144`) |
| auto-vs-played parity measurement | **does not exist** — ED-SC-0011's harness has never been built |

Under §0.2 the grade is what matters and the grade is **paper**. It stops being paper when S2's execution artifact exists (§9).

**What a PR #362 veto costs this branch.** PR #362 (`proposals/2026-09-03-meta-architecture/`) is PROPOSED and HELD BACK IN FULL; it is a *shape constraint*, not canon. If it is vetoed:

- **Survives unchanged** (all kernel-local): the `unanimity_required` aggregation branch, ballot retention, the assembly venue row, the two antibody channels, the holdout-round loop, `on_hung`, and every falsifier in §9. None of them names a PR #362 type.
- **Dies with it**: the seam vocabulary — `determine`/`Receipt`, `Act.actor`, seat `remit` for the convener, `claimants : PersonId[]`, the write gate. The branch then writes `LedgerTag`s directly to `Settlement.ledger`, which is what the tree does today anyway (`registry.py:102`).
- **Degrades**: invariant I-C1 ("no faction ballots") loses its structural leg and becomes MECHANICAL-only (the adapter's refusal). I-C3 ("a threshold never produces the outcome", `T-b`, `01_AXIOMS.md:284`) loses its citation but not its implementation — the winner/margin split in §5 stands on its own.

The decomposition was cut so a veto costs vocabulary, not mechanics. That is a claim about a future veto, not a measured one.

---

## §1 · Verification of `00_BRANCH_SHAPES.md` §5, element by element

Every row below was read at HEAD `1e163ee` on branch `claude/social-contest-system-review-dn2y5d`. No pytest was run. Line numbers are mine, taken from the working tree, not inherited from the shape spec.

| # | §5 element | verdict | verified anchor |
|---|---|---|---|
| 1 | `consensus` is a STUB row in `GAMES` sourced to v30 §10 / §7.2 | **CONFIRMED** | `wrapper.py:236 GAMES`, row `"consensus"` → `_stub("consensus")` (`wrapper.py:220`), `status: "STUB"`, `source: "social_contest_v30 §10 BG-Vote / §7.2 (largely in faction.py — Stage 4)"` |
| 2 | `unanimity_required` is a **named-but-unimplemented slot** | **CONFIRMED, and it is named in four places** | `dictionaries.py:686` (the `PANEL_AGGREGATION` comment, "Alternatives recorded (not chosen): a) simple_majority \| c) unanimity_required"); `:707` (the `panel_win_condition` docstring: "'unanimity_required' returns a self-flagging StubResult"); `:721` (the stub reason: "'unanimity_required' was sketched but not selected"); `:741` (`PANEL_CLOSURE["aggregation_ratified"]`). The implemented set is exactly `("weighted_by_standing", "simple_majority")` — `dictionaries.py:715`, and `resolver.py:128` branches on the first with `:144` as the fallback. A live pytest already probes it: `engine/tests/test_pipeline_reach.py:881` asserts `panel_win_condition(aggregation="unanimity_required")` returns `stub_wired`. |
| 3 | it is **a venue row**, not a fourth game | **CONFIRMED** | `build_contest` already accepts a prebuilt `Venue` (`wrapper.py:137-145`), and `Venue.win` is any `WinCondition` (`resolver.py:158`). A consensus proceeding needs no router entry: it needs `resolver.py:128` to grow one branch. |
| 4 | ballots are **retained per member** | **CONFIRMED as absent, AMENDED as to cost** | `resolver.py:139` `wA = sum(w for w in weights if …)` and `:144` `votesA = sum(1 for _ in range(n) if …)` — both are generator expressions that consume the per-juror draw and keep only the sum. Nothing survives the call. **Amendment:** retention is *not* free of the goldens unless the draw order and the number of `random.gauss` calls are preserved exactly — see §5.3 and the control in §9. |
| 5 | holdouts as **signed `commit` acts** | **AMENDED — and this is the largest change to §5** | A `commit` in PR #362's sense is an outer-loop Act, and `PART D` row 49 (`04_CODE_ARCHITECTURE.md:871`) says *"`commit` moves only through an Act, and no Act resolves inside another's resolution."* Jordan's 2026-09-04 ruling requires the block to bind **when cast, inside the proceeding**. Both are satisfied by making the block a **Move inside the bout** (`resolver.py:34 VALID_KINDS`) authored by the holdout's policy, with the durable record written by the calling verb's degree-keyed `writes:` column after the seam returns. §4.4 works this through. |
| 6 | the antibody is `cr5_self_backfire` **keyed to armature alignment** | **REFUTED as stated; AMENDED to a two-channel antibody** | `rhetoric.py:413 cr5_self_backfire(style_key, landed, my_standing)` takes **no armature and no alignment argument**. It fires on exactly two conditions (`:449-455`): the Style's `orientation` is `OBSCURING`, and `landed` is False (reception degree 0). Armature alignment enters only *indirectly and probabilistically*, through `dsigma` shifting the reception roll (`resolver.py:405-406`) — and `style_axis_dsigma` is **never negative** (`armature.py:365`, "a misaligned style buys 0, not a penalty"). So a misaligned block is not *charged*; it is merely *more likely to fail*, and only then charged. Worse, a holdout who blocks in a **Revealing** style (`precedent`/`vision`) can never backfire at all. The critique's own text asked for something else again — *"a frivolous block — armature dot-product below threshold — costs Mandate"* (`v30-snapshot-2026-06-28:designs/audit/2026-06-28-social-contest-deliberation-critique/critique.md` §2.4, `contest-locus FG-3`) — i.e. a **deterministic, alignment-keyed cost**, which no live function computes. §5.4 supplies the composable answer: the **primary** antibody is the orientation-independent evasion clinch that already ships. |
| 7 | `run_parliamentary_vote` is the **auto-fidelity arm** | **REFUTED for the unanimity venue; CONFIRMED for the majority venue** | `parliamentary_vote.py:125 run_parliamentary_vote` implements v30 §10: Mandate pools, TN 7, `track ≥ 7 = passed / ≤ 3 = failed / 4–6 = committee` (`:200-206`). It has **no unanimity path and no per-member ballot** — factions declare a side and the pools roll. Comparing it against a played `unanimity_required` assembly is not a fidelity comparison; it is two different procedures on the same matter. §5.6 splits F-C3 accordingly. |
| 8 | parity must be **measured, not asserted**; ED-SC-0013's constraint is `E[auto] ≈ E[played]` for exploit prevention | **CONFIRMED** | `registers/editorial_ledger_sc.jsonl`, `ED-SC-0013` (status `resolved`): *"the two must be distributionally consistent on matched inputs (E[auto]≈E[played]) — an EXPLOIT-PREVENTION requirement (no mode-shopping) whose acceptance oracle is a NEW parity harness."* `ED-SC-0011` (status `open`, `needs_jordan: false`) carries FORK-C: *"the auto/played calibration TOLERANCE … is set here when the parity harness lands. Lean: unbiased mean is the hard anti-exploit constraint; variance looser for auto."* The tolerance is therefore **declarable, not escalatable** — §11 rung 5. |
| 9 | the Holdout Obligation clock and the fourth resolver are **false N-lines** | **CONFIRMED, both** | The clock: `scene_slate.py:25 SceneSlot` / `:34 queue_scene` already re-queues, and a durable mark is `LedgerTag(kind="Grudge", ttl=None)` (`ledger.py:36`). The fourth resolver: `VoteAtClose` is a `WinCondition` on the one kernel (`resolver.py:98`), and the loop is `Bout.resolve` (`resolver.py:440`). Neither is resurrected here. |
| 10 | `on_hung` is *"the smallest thing in this document that could still be a false N-line"* | **REFUTED — it IS one, and it is cut.** | Full adjudication in §7.3. Short form: the second value `lot` pulls in a weighted-draw mechanism that exists **nowhere** in the tree (grep: no `WeightedDraw`, no sortition), which is the `14_NERS.md` meta-rule violation (*a fix that adds a system has failed*); and the research argues against a lot *at this scale* — Dowlen's finding is that the lot's protective power **degrades as the pool shrinks**, and a hung assembly is a small pool. |

**Also found, each anchored, none padded:**

- **The one production contest is a Panel contest.** `scene_dispatch.py:118` pins `guild_arbitration`, whose `PROCEEDINGS` row (`modes.py:502-509`) carries `adjudicator="panel"`, which `wrapper.py:180-190` rebinds to `panel_win_condition()` → `VoteAtClose(aggregation="weighted_by_standing")`. **Every contest in the campaign goldens already runs through the function this branch modifies.** That makes the control in §9 exact and non-optional.
- **`ledger_sweep` is unreachable in production.** `registry.py:207` is its only call site, inside `succeed_governor` (`registry.py:199`), and `succeed_governor` has **zero callers anywhere in the tree** (grep). `engine/autoload/season_manager.py:33 advance_season` contains no ledger call. Additionally `ledger_has`/`ledger_get` (`ledger.py:61`, `:65`) do **not** filter by `is_expired`, so an expired tag reads as live until a sweep physically removes it. This **refutes** the shape spec's ED-SC-0015 closure argument — see §11.
- **There is no `assembly` row in `PROCEEDINGS`.** `modes.py:485 PROCEEDINGS` holds exactly the 8 canonical rows, each field cited to `params/contest.md §Proceeding Types` (`modes.py:478-479`), and `wrapper.py:187` records that the roster is deliberately unchanged. `assembly` exists one level down as a **venue** (`modes.py:73 assembly_venue`, registered at `:84 VENUES`), and a deliberating bench exists as `modes.py:127 deliberative_body_venue` / `:144 deliberative_body_mode` in `INSTITUTIONAL_MODES` (`:150`), which is explicitly *"placeholder keys (mechanism, not world)"*. §5.1 puts the consensus row there, not in the canonical 8.
- **`assembly_venue` and `deliberative_body_venue` both already set `DefeatCatalogue(barred=False)`** (`modes.py:76`, `:133`), which is the shape spec's S2.2 exactly — and `DefeatCatalogue`'s own docstring states the rule: *"a vote disables the rhetorical-device bar"* (`primitives.py:265`). Both keep `evasion_strikes=2` and `yield_strikes=2` at default (`primitives.py:267`).
- **The fault check runs inside the exchange loop, not at close.** `resolver.py:453` calls `self.v.faults.check(...)` after **every move**, and a hit returns immediately with `clinch:<reason>`. This is what makes the antibody bind in-scene without any new machinery.
- **`Bout` already takes `armature=`** (`resolver.py:238-239`). The unreachability is entirely in `build_contest`'s signature (`wrapper.py:110`), which is a spine fix (`00_BRANCH_SHAPES.md` §2.1), not a consensus fix.
- **`run_parliamentary_vote` already takes `rng=None`** and threads it to `dice_engine.roll_pool(rng=rng)` (`parliamentary_vote.py:125`, `:187`). The played arm does not: `resolver.py:32 roll_net` is hard-wired to the global `random` module, and `scene_dispatch.py:298-300` reseeds and restores the global stream around the call. The parity harness needs the spine's `rng` injection to be seed-comparable at all.
- **`stalemate` is a declared, unemitted outcome token.** `engine/engine_params/key_types.json:958` gives `scene.contest_resolved`'s enum as `initiator_win | target_win | compromise | stalemate`, while `echo_transport.py:114 _OUTCOME_BY_DEGREE["contest"]` emits only the first three. I do **not** reach for `stalemate` (§6); recorded because a reader will and should know why not.
- **A per-member deliberation pattern already exists twice and neither retains.** `faction.py:39 _one_vote` builds a whole `Bout` per voter with that voter as adjudicator, and returns `'yes'`/`'no'`; `resolver.py:124 VoteAtClose.resolve` samples per juror. Both discard the per-member record. That is the gap this branch closes, and the shape it closes it in is already established twice.

---

## §2 · The conflict class, and why `agon` cannot resolve it

**The class.** A body that must act as one, where the decision rule is *no decision until all assent*, and where any single member can withhold. Concretely in this world: `social_contest_v30.md:407` names two — *"RM: Mandate ≥ 3 organizers by consensus"* and *"Varfell: Jarl Assembly by quorum"* — as the adjudicating bodies of a Succession Contest. The canon names the procedure and the engine has never had it.

**Why `agon` cannot.** Not "cannot easily" — cannot, and the reason is structural rather than a matter of tuning.

`politics-as-deliberative-game.md:192` (Part D.1) sorts every deliberative procedure by *where the competition sits relative to the decision*, and consensus is **Type 3: a procedure that removes the competition by design.** The relevant sentence is the one about what happens next: *"the competition they abolish **re-emerges as pathology** — … the holdout's veto-war under consensus."*

An agôn has a winner by construction. `Bout.resolve` (`resolver.py:440`) returns `(winner, reason)` where winner ∈ `{A, B, "draw"}` or a band string. Every win-condition in the tree — `ThresholdRace` (`:54`), `TallyAtClose` (`:62`), `ProofBar` (`:67`), `GraceThreshold` (`:74`), `PersuasionTrack` (`:81`), `VoteAtClose` (`:98`) — answers *who prevailed*. A majority tally can be tuned to make winning hard; it cannot express **"no decision until all assent"**, because at every threshold there is still a side that prevails at that threshold. And it cannot express a **holdout**: a person whose refusal is not a losing vote but a stop.

The three-lens audit (2026-08-06, later than the critique) is right that the *majority tally* is the BG vote at another fidelity (`04_reductive…md:228` — "`consensus` is the BG vote — a fidelity view, not a fifth type"). The 2026-06-28 critique is right that the *unanimity procedure with a holdout* is expressible by no tally. **Both are true and they are about different objects**, and the named-but-unimplemented `aggregation="unanimity_required"` is precisely where they meet: one aggregation value on an existing win-condition, not a fifth game.

**The design consequence, stated so it cannot be tuned away.** A Type-3 procedure must *express* the removal of competition, and must then supply an **antibody** against the pathology it thereby creates. `politics-as-deliberative-game.md:192`: *"The anti-frivolous-objection rule of the Great Law and the oaths against bribery in Venice are constitutional antibodies against exactly that re-emergence."* A consensus branch without an antibody is not an incomplete design; it is a **known-defective** one, and history says so in advance. The antibody is therefore not a polish item in §5 — it is the load-bearing element, and §8 grades it honestly rather than favourably.

**Do not force a Caillois family on it.** `politics-as-deliberative-game.md:202` (Part D.3): *"Consensus genuinely resists the scheme … the families all presuppose a form of play, and consensus is constructed to suppress the play-element."* Nothing in this document assigns consensus a family, and the `CeremonialMode` acclamation scaffold (`modes.py:351`) is deliberately left alone (§11 rung 2).

---

## §3 · Historical grounding, with tiers and stated limits

Tier codes are the corpora's own — **T0** primary · **T1** authoritative synthesis · **T2** reputable secondary · **T3** navigation; `[PRIM]`/`[REF]`/`[CONFIDENCE: …]` are the rhetoric corpus's. **`rhetoric_oratory_contest_research.md:367` (§9.7) binds every row: history validates the *structure*, never the *numbers*.** No constant in §5 comes from any source below, and each is marked `[SEED]`.

### 3.1 Framing authority — who poses the question and in what order members speak

- **Roman Senate — *relatio* / *sententiae* / *discessio*.** `rhetoric…:279` **[PRIM/REF]**: the presiding magistrate frames the question (*relatio*); opinions are delivered *"in strict order of rank — princeps senatus first; the lower ranks often never reached"*; decision by physical division. The corpus's own summary: *"Persuasion was bounded by a rigid speaking-order that was itself a function of standing."*
- **Norse Lawspeaker / Lögrétta.** `rhetoric…:281` **[PRIM]** and, in far more detail, `rhetoric…:516` (§12.8, Icelandic + Old Norse *Grágás*, `[CONFIDENCE: high]`): the *lögsögumaður* is the commonwealth's only paid official, elected by the Lögrétta for three-year terms, whose office is to hold the law in memory, recite the *þingsköp* (standing orders) every year, and rule on procedure — *"procedural and session-bound, not executive … at the Alþingi 'the most powerful man in the land', but between assemblies 'formally powerless'."* The Lögrétta seats 48 *goðar*, **each flanked by two advisors he may consult during the session**, and decides by a **consensus → lot (by quarter) → majority (*afl ráða*)** cascade.
- **§7.3 synthesis** (`rhetoric…:294`): every institution supplies *(a)* a framing authority, *(b)* a standing-indexed speaking order, *(c)* a decision rule, *(d)* often a clock — and *"the institution is the deterministic wrapper, the speeches the stochastic core."* That sentence is the design of §4 and §5.
- **What the corpus flags as weak, honestly carried.** `rhetoric…:347` (§9.2) is the section that names the *relatio* and the Lawspeaker as *"two concrete framing-authority designs for who poses the question and in what order members may speak — a standing-gated turn order that is historically the heart of assembly procedure."* **The same paragraph carries `[CONFIDENCE: low]` on the six-head τελικὰ-κεφάλαια list** and states the securely-verified minimum instead: *"Aristotle's paired deliberative topics, the good and the advantageous."* **Nothing in this document builds on the six-head list.** The only deliberative argument-typing §5 uses is the existing `Stasis`/`Genre` vocabulary already in the kernel (`primitives.py`, `rhetoric.py`), which is grounded on §1.4, not §9.2.
- ***Ars arengandi*** (`rhetoric…:255`, `[CONFIDENCE: medium — less web-verified this session]`): occasion-typed model speeches for the Italian communal assemblies — Matteo dei Libri, Jacques de Dinant. Carried at its stated confidence and used for **nothing load-bearing**: it corroborates that assembly speech is occasion-templated, which the kernel's `PROCEEDINGS`/Style tables already assume. No mechanic rests on it.

### 3.2 The procedure and its two antibodies

- **The Great Law of Peace** — `politics-as-deliberative-game.md:90` **T0/T1** (Great Law recensions: Newhouse/Parker, Hale 1883, Hewitt 1928; Fenton; `politics…:277` flags *recension variance is real and the article count varies*, and the founding date is *genuinely disputed*, c. 1142 vs c. 1450–1600). The structure taken: a **fixed sequence** — Elder Brothers (Mohawk, Seneca) deliberate to agreement → Younger Brothers (Oneida, Cayuga) → **Fire Keepers (Onondaga) confirm**; clan mothers select and can remove sachems.
- **Antibody 1, the anti-frivolous-objection rule** — `politics…:94`: *"the Iroquois Great Law explicitly forbids impeding a decision 'with insignificant objections or frivolous considerations', and **caps the Onondaga's power to refuse**"* — and the corpus draws the general conclusion itself: *"a consensus constitution must build in anti-gaming rules precisely because it knows consensus can be gamed."* **Two antibodies, not one**: the frivolity rule *and* a cap on the confirming body's refusal. §5.4 implements the first; §5.5 implements the second as `on_hung`.
- **The exploit the corpus names** — `politics…:94`: *"When it is gamed, 'winning' means extracting concessions as the price of one's assent, or framing the finally-agreed position as one's own."* §10 answers this specific sentence, not a general worry.
- **Antibody 2, Venice** — `renaissance-machination-games-lens-and-review.md:53` **T1** (Frey, Osterloh & Rost 2022; Saran & Tumennasan 2018): rotation, short terms, a prohibition on accumulating offices, the Ten policing defection, and the ten-round lot-and-ballot dogeship *"deliberately injecting indeterminacy so that no faction could predict or purchase the outcome and bribery lost its point."* **The qualification that binds a game designer is in the sibling document** — `renaissance-testing-the-model-and-closing-findings.md:15-21`, Part VIII.1 (Finlay's reconstruction from Sanudo and Priuli): the design *"did **not** eliminate strategic behavior — it *channeled* it"* (*broglio*).
- **Benedictine Rule ch. 3, *ijmāʿ*, Gadaa** — `politics…:90` **T0/T1**, corroborating breadth. Used for breadth only; no mechanic rests on them.

### 3.3 The worked pathology: the *liberum veto*

`renaissance-testing-the-model-and-closing-findings.md:37-45`, **Part IX**, **T1** (Konopczyński 1930; Klick & Parisi 2003; *Constitutional Political Economy* 2008; Britannica/Wikipedia **T2/T3 for dates only**). The corpus itself flags the case as **borderline in period** — *"it emerged only at the close of the sixteenth century and was formalised after 1600"* (`politics…:90`, and `politics…:277` "flagged as borderline").

- **The device** (`…closing-findings.md:41`): any single deputy could halt all business and annul the session's passed acts — *Nie pozwalam!* First dissolving use 1652 (Siciński); abolished by the Constitution of 3 May 1791.
- **The prediction, derivable from the design alone** (`:43`): *"maximal individual veto power plus no randomization plus external bribers entails hold-up … the cost of controlling the outcome collapsed to the price of the single cheapest deputy."*
- **And the other half, which matters more for a game** (`:45`): the framework *"also predicts the rule's long period of success … under benign conditions the unanimity rule worked, securing religious peace in a deeply fractionalized polity … and it was 'used sparingly' in the seventeenth century."* Greif's **self-undermining equilibrium**: well-suited to fractionalization and minority protection, fatal under external predation.
- **The measured record** (`:43`): of roughly 150 *sejms* 1573–1763, about a third passed no legislation, mostly from the veto; under Augustus II, ten of eighteen were wrecked.

**How this is used, and how it is not.** F-C2 (§9) reproduces the **qualitative** prediction — both halves — and reports the numbers it produces. It does **not** tune to one-third, and §9.7 is the reason. Reproducing only the failure half would be cherry-picking a framework that explicitly predicts both.

### 3.4 The lot, and why it is not in §5

`renaissance-machination…md:33` **T1**: Dowlen 2009 — the lot's *arationality* is its primary anti-manipulation property, **but** *"when the pool of names is small and its members coordinate into groups, the lottery becomes in effect a weighted lottery … 'the arational blind break does less and less work'"*, which Dowlen says was *"very much the case with the Florentine and Venetian schemes, aggravated by their small pools."* Buchstein 2019 — the lot's historical functions were **anti-faction and anti-bribery**, not democratic equality. `:81` states the correction bluntly: *"the corrected account makes the lot an anti-manipulation device whose protective power degrades as the pool shrinks."*

The Lögrétta cascade (§3.1) *does* place a lot between consensus and majority, and I am dropping that rung. §7.3 states the cost of dropping it rather than pretending the history licenses the simplification.

---

## §4 · THE SEQUENCE

Idiom per `systems/_architecture/subsystem_flow_skeletons_v1.md` as used by `social_contest_flow_skeleton_v1.md`: `[branch] [emit] [gate] [write] [loop]`. Each step names what it **reads**, what it **writes**, and **who owns the write**.

### 4.1 The binding rule this sequence is built to (Jordan, 2026-09-04)

> *"negotiated agreement bind in scene. in fact, everything that occurs within a scene should bind or else it's as if time doesn't exist within a season."*

For consensus this means: **assent, dissent and the block take effect at the point they are cast, inside the proceeding.** It is more load-bearing here than in the sibling branches, because a block that does not bind when it is cast is not a veto — it is a suggestion, and the entire Type-3 pathology depends on the block biting immediately.

**The tree already satisfies this and I did not have to add anything for it.** `Bout.resolve` (`resolver.py:453`) evaluates `self.v.faults.check(...)` after **every move**, and a hit returns from the loop immediately. `_apply` (`resolver.py:423-437`) applies the CR5 Face strip **at the move**, inside `_apply`, before the loop advances. Both antibodies therefore fire in the same scene as the block they punish, at the exchange in which it is made. Nothing is deferred to a season boundary and nothing is deferred to the close.

### 4.2 The sequence

```
S1  [write] CONVENE — the presiding seat poses the question (relatio; Lawspeaker as fundarstjóri)
      reads   : the seat's convene remit; the matter's place; the roster Query at the rung
      writes  : the Proposition P (utterer = the mover), the SceneSlot
      owner   : the convener (a Person). AX-1 — a body never convenes; its presiding member does
    S1.1 [gate] quorum — |members present| / |members seated| >= QUORUM_FRACTION [SEED]
                else Refusal(no_quorum). v30 §7.2 "Varfell: Jarl Assembly by quorum" names it, no number
    S1.2 [gate] depth — depth < max_depth else Refusal(depth_cap)                      §C.5, no default
    S1.3 [emit] queue_scene("consensus", ctx={P, rung, members})            scene_slate.py:34 queue_scene
      judging_set = the members present, resolved ONCE at the boundary        -> contract.py:37 Panel
      speaking_order = judging_set sorted by Standing (relatio + sententiae; rhetoric...:279)
                       ORDER OF SPEECH ONLY — never the ballot draw order (see S3 and §5.3)

S2  [loop <= venue.budget exchanges] DEBATE — the mover argues the question before the assembly
      Bout(mover, opponent, consensus_venue, adjudicator=Panel(members), armature=ArmatureConfig(...))
      reads   : ContestState.adv, Standing, Reserve, Room, the live Stasis    resolver.py:238 Bout
      writes  : bout-local state only — nothing crosses the seam           NO WRITE TOKEN, §C.5
      owner   : the resolver
    S2.1 [branch] moves per side, in speaking_order                            resolver.py:341 _apply
    S2.2 [gate]   faults per venue: barred=False (an assembly disables the rhetorical-device bar
                  -- primitives.py:265, and modes.py:76/:133 already set it); evasion and yield
                  strikes LIVE                                                primitives.py:262
    S2.3 [gate]   ANTIBODY CHANNEL 1 fires HERE, per move, not at close       resolver.py:453
    S2.4 [gate]   ANTIBODY CHANNEL 2 fires HERE, per move, not at close       resolver.py:423
    S2.5 [emit]   beats (Bout(record=True).log)                               resolver.py:453

S3  [gate] FIRST BALLOT — VoteAtClose per member, RETAINED
      reads   : gap = adv[A] - adv[B]; each member's bench-weight (Adjudicator.discipline)
      writes  : Ballot[] on the WinCondition's own result object -- no world state
      owner   : the resolver                                              resolver.py:124 resolve
      SIMULTANEOUS: every member draws against the SAME gap. No member reads another's ballot.
                    Adding a bandwagon term is DECLINED -- see §4.4 and §12 attack 3

S4  [branch] AGGREGATION
    aggregation == "weighted_by_standing" (EXISTS):  maior et sanior pars; margin = share - 0.5
    aggregation == "unanimity_required"   (NEW branch at resolver.py:128):
      all ballots assent -> A. unity enacted. margin = 0.0
      else [loop <= K holdout rounds]  K = HOLDOUT_ROUNDS [SEED]; K=0 IS the liberum veto
        the dissenting members are named by the retained ballots (S3)
        S4.1 [branch] the mover addresses the block: a fresh Bout, mover=A vs holdout=B,
                      adjudicator = Panel(judging_set MINUS the holdout)     -- RECUSAL, §5.4
        S4.2 [gate]   antibody channels 1 and 2 both live in that bout, per move (S2.3/S2.4)
        S4.3 [branch] the holdout's position at the end of S4.1 is the bout's own outcome:
                      clinch against the holdout -> the block is SET ASIDE (Great Law frivolity rule)
                      otherwise                  -> the block STANDS
        S4.4 [gate]   re-ballot: S3 again, against the NEW gap. Members respond to the ARGUMENT,
                      never to each other's ballots. A prior ballot is superseded, never read
      after K rounds with a standing block -> not unanimous. winner = B (the blocker prevailed)

S5  [branch][write] TERMINAL — the presiding seat DETERMINES; the count grades, the act writes  T-b
      margin  : see §5.2. degree = degree_from_net(margin * UNANIMITY_MARGIN_SCALE [SEED], ob=0)
      Overwhelming -> unity: LedgerTag(Precedent, key=P, ttl=None) on the place
      Success      -> carried with a recorded dissent: Precedent + Grudge per dissenter
                      (I-2 recorded defeat; senatus auctoritas)
      Partial      -> referred back / compromissum: queue_scene next season; chain cap 3 (v30 :383)
      Failure      -> blocked: the matter lapses this season
      writes  : LedgerTag(s) via the calling verb's degree-keyed writes: column   §C.4, after the seam
      owner   : the presiding seat's determine act -- never the resolver, never the threshold
    S5.1 [emit] scene.contest_resolved{outcome, persuasion_track_final: margin}   echo_transport.py:427

FIDELITY: the auto arm is NOT run_parliamentary_vote for a unanimity venue -- see §5.6.
```

### 4.3 Who poses the question and in what order members speak — the two research designs, both used

- **Framing authority** = S1. The convener is a **seat with a convene remit**, whose power is *procedural and session-bound*: it poses the question and it `determine`s the terminal. It does not decide the matter. That is the *lögsögumaður* precisely (`rhetoric…:516`), and it is also the *relatio* (`rhetoric…:279`). Mechanically it costs one thing: the terminal is an act by a person, which is what `T-b` (`01_AXIOMS.md:284`) requires anyway.
- **Speaking order** = S2.1, `speaking_order` sorted by Standing. This is `sententiae` in rank order. It is **the order of moves in the bout**, and it is deliberately **not** the ballot draw order — see §5.3 for why that separation is load-bearing on the goldens rather than merely tidy.
- **Declined, with reason:** the Lögrétta's *goði + two advisors* (bounded per-voter consultation, `rhetoric…:516`). It is a real primitive and it would be a second per-member state store. `Adjudicator.discipline` (`contract.py:31`) already carries "how much this member weighs the forum case versus its own disposition", which is the same dial at one field instead of three. Recorded as a distillation kept out, not as an oversight.

### 4.4 Does this design need intra-scene *reaction*? — worked, not waved at

The constraint: PR #362's `deliberate(frozen)` is a pure map (`04_CODE_ARCHITECTURE.md:509`), and `41a` (`:863`) makes the falsifier explicit — shuffle the deliberation order and the `Scene` **set** and the season hash must be identical. So a member may not condition their choice on another member's same-tick choice.

**The answer is (a): the ballots are simultaneous, and the "rounds" are the resolver's own sub-ticks. This branch needs no intra-scene reaction between members, and I have designed it so that it cannot acquire one.** Four separate checks:

1. **The first ballot is already a simultaneous-move game in shipped code.** `resolver.py:139`/`:144`: each juror's decision rule is `k*gap + gauss(0, noise) > 0`. The only shared input is `gap`, the room's momentum. **No juror reads another juror's ballot, and there is no parameter through which one could.** Retaining the ballots (§5.3) adds a list; it adds no input to the decision rule.
2. **The holdout round's reaction is between *contestants*, not between members.** S4.1 is a `Bout`: the mover and the holdout alternate and each reads a `ContestView`. That is the agôn that ships today and runs in the campaign goldens. `§E.1` (`03_VERBS_AND_LOOPS.md:217`) grants a contest *"the same steps over a smaller person set on a shorter clock"*, which is exactly a sub-deliberate/sub-resolve. Two contestants reacting inside a bout is not two persons reacting inside one DELIBERATE.
3. **The re-ballot conditions on the argument, not on the ballots.** S4.4 re-runs S3 against the **new `gap`** — a public, resolver-owned aggregate (`ContestState.adv`, `resolver.py:46`) produced by the contestants' moves. This is reading the world as the sub-tick's predecessors left it, which is what `§C.4`'s fold does by construction (`04_CODE_ARCHITECTURE.md:583`). It is not reading another person's undecided choice. **A prior ballot is superseded and is never an input.**
4. **The antibody needs no member to respond.** Channel 1 is `DefeatCatalogue.check` — pure resolver, reading only the blocker's own `FaultState` (`contract.py:17`). Channel 2 is `cr5_self_backfire` on `(style_orientation, deg)`, where `deg` comes from `_reception` rolling against the **Panel's precomputed mean armature position** (`armature.py:374 position_of` → `ArmaturePosition.mean`, `:285`). That is a read of frozen member state — the resolver evaluating the block's merit — not a member responding to the block.

**Therefore: no conflict with PR #362 was found, and I decline to manufacture one.** The one boundary worth naming in a sentence, which the spine agent owns: **the holdout's block is a `Move` inside the bout, not a `commit` Act.** If a future design needed the holdout's `commit`/`Tenure` edge itself to change mid-proceeding, that is `PART D` row 49 (`04_CODE_ARCHITECTURE.md:871`) and it would be a real conflict. This design does not need it: the block's *effects* bind in-scene (Face, faults, clinch, the round's outcome) and the *durable edge* is written by the fold after the seam returns.

**The cost of binding in-scene, stated rather than hidden.** There is **no free probe.** A member cannot cast a block, watch the room, and retract before paying: the Face strip and the fault accrual land at the move (`resolver.py:423`, `:453`). Withdrawal in a later round reverses the **position**, never the **cost**. That removes a real churn source — the exploratory block, the "let me see who flinches" move — and it is precisely what makes the antibody bite. It also means "binds" must be read correctly: a ballot binds **for its round** (its consequences land and the round's outcome is final), not forever; the Great Law's own procedure refers the question back and the body votes again, so re-balloting is the historically exact shape and not a loophole.

---

## §5 · THE SHAPE

Every invented number is `[SEED]`. **The research licenses none of them** (`rhetoric…:367` §9.7). There are five, and they are named together in §5.7 so a builder cannot miss one.

### 5.1 The venue row — `INSTITUTIONAL_MODES`, not the canonical 8

```python
# modes.py — beside deliberative_body_venue (:127), same tier
def consensus_body_venue(noise=1.0, members=7, aggregation="unanimity_required",
                         on_hung="defer", holdout_rounds=HOLDOUT_ROUNDS, **o):
    """A body that must act as one. Deliberative register (future-weighted, Rhet I.3), inherited
       from deliberative_body_venue unchanged. barred=False: an assembly disables the rhetorical-
       device bar (primitives.py:265 DefeatCatalogue docstring; modes.py:76/:133 precedent).
       evasion_strikes LIVE and load-bearing: they ARE the Great Law's anti-frivolous rule."""
    return Venue(proof_ethos=.20, proof_pathos=.40, proof_logos=.40,
                 start_ground=Stasis.CONSEQUENCE,
                 proof_past=.20, proof_present=.20, proof_future=.60,
                 win=VoteAtClose(jurors=members, noise=noise, aggregation=aggregation),
                 faults=DefeatCatalogue(barred=False, evasion_strikes=FRIVOLITY_STRIKES),
                 allow_rebuttal=True, **o)

def consensus_body_mode(members=7, **o):
    return ContestedMode(venue=consensus_body_venue(members=members, **o),
                         adjudicator=_default_panel(members))       # modes.py:115 _default_panel

INSTITUTIONAL_MODES["consensus_body"] = consensus_body_mode         # modes.py:150 — placeholder key
```

**Why not a ninth `PROCEEDINGS` row.** `modes.py:478-479` states that every field of every `PROCEEDINGS` row cites `params/contest.md §Proceeding Types`, and `wrapper.py:187` records the roster as deliberately unchanged across the ED-1059 rebind. A ninth row would have to invent a canon cell in a table that is a transcription. `INSTITUTIONAL_MODES` is the tier whose own comment says *"placeholder keys (mechanism, not world); Jordan assigns Valorian names"* (`modes.py:150`) — mechanism without a canon claim, which is exactly what this is. **Answered by architecture (§11 rung 5), no ruling needed.** Reachability from the seam is via `build_contest`'s prebuilt-`Venue` path (`wrapper.py:137`), which already works.

`on_hung` and `holdout_rounds` ride on the venue rather than on `PROCEEDINGS` for the same reason.

### 5.2 The `unanimity_required` branch — winner and margin are different objects

```python
# resolver.py — VoteAtClose.resolve, one new branch beside :128 and :143
@dataclass(frozen=True)
class Ballot:
    member_index: int          # position in the bench tuple; the identity the Panel already has
    weight: float              # Adjudicator.discipline, unchanged (ED-1057)
    assent: bool

@dataclass(frozen=True)
class BallotBook:
    ballots: tuple             # Ballot[], in DRAW ORDER (see §5.3)
    assent_share: float        # weighted, in [0.0, 1.0]
    unanimous: bool
    dissenters: tuple          # member_index[], the holdouts, named

    def margin(self) -> float:                    # WinCondition.margin(), the spine's one contract
        return self.assent_share - 1.0            # 0.0 at unity; negative by distance from unity

# resolve(closing=True) under aggregation == "unanimity_required":
#   winner = A iff book.unanimous else B          -- STRICT. one dissenter defeats the motion
#   margin = book.margin()                        -- graded, NOT the decision
```

**The winner/margin split is the whole of the design and must not be collapsed.** Under strict unanimity a single dissenter among fifty defeats the motion — that is what unanimity *is*, and `winner` says so with no softening. But `margin` grades **how far from unity the body stood**, and it is the margin that keys the consequence column:

| assent share | margin | degree | consequence (S5) |
|---|---|---|---|
| 1.00 | 0.00 | Overwhelming | unity enacted — `Precedent(P, ttl=None)` |
| 0.98 (one objector in a body of ~50) | −0.02 | Partial | **referred back** — the Great Law's own remedy for a lone objection |
| 0.60 | −0.40 | Failure | blocked; the matter lapses |

The motion does not carry in rows 2 and 3 alike; **what happens next** differs, and that difference is the Great Law's structure rendered mechanically. `Overwhelming` is reachable **only** at share exactly 1.0, which is the correct and only reading of "unity".

`margin` is in `[−1, 0]` and `degree_from_net` (`engine/autoload/dice_engine.py:227`) is a σ-space ladder, so the branch multiplies by `UNANIMITY_MARGIN_SCALE` `[SEED]` to place the band edges. That scale is the one number that decides whether a lone objector refers back or blocks outright, so it is the `[SEED]` a builder must not guess quietly.

**`T-b` compliance** (`01_AXIOMS.md:284`, *a threshold may never produce an outcome*): the count grades; the presiding seat's `determine` writes. The unanimity test is not a threshold producing an outcome, because there is a person whose act produced it — the holdout — and a person who writes it — the convener.

### 5.3 Ballot retention — and the exact constraint that keeps the goldens still

```python
# resolver.py:128-146, weighted branch — the ONLY safe shape
weights = [...]                                   # unchanged, same order as adj.members
ballots, wA = [], 0.0
for i, w in enumerate(weights):                   # SAME ORDER, SAME COUNT of gauss draws
    assent = (self.k * gap + random.gauss(0, self.noise) > 0)
    ballots.append(Ballot(member_index=i, weight=w, assent=assent))
    if assent: wA += w
```

**This is not a stylistic note; it is the control.** `random.gauss` consumes the global stream, and `scene_dispatch.py:118` puts `guild_arbitration` — hence `VoteAtClose`'s weighted branch — on the campaign golden path. Three things must hold or the goldens move and the branch has silently changed `agon`:

1. **the same number of `gauss` draws** — the generator expression draws once per weight and the loop must too;
2. **the same order** — reordering `weights` by Standing maps different draws to different weights, and since the weights differ the sum differs. **This is why the standing-indexed speaking order of §4.3 governs S2 and not S3.** The `sententiae` order is real and is used where it belongs; importing it into the ballot draw would be a golden-moving change wearing a historical costume;
3. **the same short-circuit behaviour** — `sum(...)` over a generator does not short-circuit, and neither does the loop.

The `simple_majority` branch (`resolver.py:143-147`) takes the identical treatment.

**What retention buys, in one line (the N-line):** cut it and the holdouts have no names, so there is no signed block, no antibody target, no `Grudge` recipient, and no *liberum veto* to reproduce. The whole branch is downstream of naming the dissenters.

### 5.4 The antibody — two channels, and the honest binding

The shape spec routed the antibody to `cr5_self_backfire` "keyed to armature alignment". §1 row 6 refutes that binding. Here is what composes instead, both channels already in the tree.

**Channel 1 — the frivolity clinch (PRIMARY).**

```python
DefeatCatalogue(barred=False, evasion_strikes=FRIVOLITY_STRIKES)     # primitives.py:262
```

`resolver.py:381`: a move whose ground is not relevant to the live stasis accrues `c.fault.evasion` with reason `"argued off the live issue (arthantara)"`. `primitives.py:277`: at `evasion_strikes` the catalogue clinches **against that side**. `resolver.py:453`: the check runs after **every move**, and a hit returns immediately with `clinch:evasion`.

**That is the Great Law's anti-frivolous-objection rule, already executing.** *"Impeding a decision with insignificant objections or frivolous considerations"* (`politics…:94`) is, mechanically, blocking on a ground the question is not about. And the remedy matches the history: the objection is **set aside** (S4.3), not merely fined.

Three properties make this the primary channel rather than the secondary one:

- **It is orientation-independent.** It fires on Revealing and Obscuring blocks alike. This matters because `ED-SC-0021` (open, `needs_jordan: true`) records that *"the orientation bit is DOMINATED contest-wide … Revealing dominates at every resistance value"* and that *"CR5's COST half is wired while the Doubt Marker (its entire upside) is not, so Obscuring currently ships as pure downside."* **A rational holdout therefore never picks an Obscuring style, and an antibody that only fires on Obscuring never fires.** Channel 1 is immune to this.
- **It terminates the block rather than pricing it.** A Face strip is a tax a determined blocker pays. A clinch removes the block from the proceeding.
- **It executes today**, in the loop, in-scene, at the move.

**Channel 2 — the eristic self-cost (SECONDARY, and contingent).**

```python
cr5_self_backfire(style_key, landed=(deg >= 1), my_standing=c.face.v)   # rhetoric.py:413
```

Unchanged, called exactly where it is called today (`resolver.py:430`), under `armature is not None and armature.cr5`. It strips `min(2.0, own Face)` (`rhetoric.py:366 CR5_BACKFIRE_MAGNITUDE`) from a blocker whose **Obscuring** move **landed nowhere**.

**How armature alignment actually enters, stated exactly.** It does not gate the antibody. It shifts the reception roll: `armature.dsigma(side, adj)` (`armature.py:436`) → `style_axis_dsigma` (`:357`) → the δσ term in `_reception` (`resolver.py:405-406`). The dot-product is `Σ_axis STYLE_AXIS[style][axis] · position[axis]` (`armature.py:346`) against the **Panel's mean member position** (`:374`, `:285`). Perfect alignment buys `ARMATURE_MAX_DSIGMA` = 0.50σ (`armature.py:336`); **misalignment buys 0, never a penalty** (`:365`). So a block pitched in a register the assembly is not moved by is *more likely to land nowhere*, and only a block that lands nowhere is charged. **The antibody is therefore probabilistic, not deterministic**, and every falsifier in §9 that touches it must measure a **rate over N seeds**, never a single run.

**Recusal, and why it is required rather than tidy.** For channel 2's alignment gradient to exist at all, the holdout must not sit on the bench it argues to. `position_of(adjudicator, opponent_is_adjudicator=True)` returns the **zero vector** (`armature.py:388`) — the asymmetric-proceeding gate — which zeroes `dsigma` and flattens the gradient to nothing. S4.1 therefore builds the holdout round with `Panel(judging_set MINUS the holdout)`. This costs **no new state**: the judging set is a Query and `Panel` is a frozen tuple built at call time (`contract.py:37`). It is also historically exact — the Great Law's objecting brother speaks *to* the confederacy, and the Fire Keepers confirming are a distinct body (`politics…:90`).

**Channel 3 — the durable mark.** `LedgerTag(kind="Grudge", key=<holdout>, ttl=None)` at S5 (`ledger.py:36`, added via `ledger_add`, `:47`). Durable, so the missing season-boundary sweep (§1, §11) does not touch it. This is what makes *repeated* holding-out costly at strategic scale where a single Face strip is not.

### 5.5 `on_hung` — reduced to one value plus a fallback, and the lot is cut

```python
on_hung ∈ {"defer", "majority"}          # was {"defer", "lot"}; the lot is CUT — §7.3
```

- `"defer"` — S5 `Partial`: `queue_scene` next season, chain cap 3 (`social_contest_v30.md:383`). **Inherits a known defect** and I will not pretend otherwise: after three consecutive compromises v30 §6.3 puts the matter into "cold equilibrium" — Disposition frozen, no contest on the topic for 4 seasons — which the critique names as *"the single most anti-churn line in the spec"* (`critique.md` §2.4, `contest-locus FG-4`).
- `"majority"` — after K holdout rounds, the **same** `VoteAtClose` re-runs at `aggregation="weighted_by_standing"`. Zero new mechanism: the branch already exists (`resolver.py:128`). This is the Lögrétta cascade's **third** rung (`rhetoric…:516`, *consensus → lot → majority (afl ráða)*) and it is the Great Law's second antibody — the **cap on the confirming body's power to refuse** (`politics…:94`) — rendered as a rule rather than a number.

`"majority"` is what makes F-C2 a two-arm experiment rather than a demonstration: *liberum veto* (`on_hung="defer"`, K=0) against *sanior pars* (`on_hung="majority"`), which is exactly the Sejm/Venice contrast Part IX is built on.

### 5.6 The auto arm — and why `run_parliamentary_vote` is only half of it

`run_parliamentary_vote` (`parliamentary_vote.py:125`) resolves v30 §10 by Mandate pools at TN 7 into `passed | failed | committee` (`:200-206`). It has no unanimity path and no per-member ballot. **A unanimity venue and a Mandate-pool tally are not the same procedure**, so pairing them and calling the disagreement a parity failure would be measuring nothing.

The split:

| venue aggregation | auto arm | what parity means |
|---|---|---|
| `weighted_by_standing` | `run_parliamentary_vote` — genuinely the same decision rule at faction fidelity | ED-SC-0013's `E[auto] ≈ E[played]` as written |
| `unanimity_required` | the **same** venue at `budget = 0` — a zero-exchange `VoteAtClose` closing immediately on the venue's start state | same aggregation, no debate: parity asks *what does playing the debate buy* |

The zero-exchange arm is not a new construct: the three-lens audit already observed that *"today's `VoteAtClose` is formally a degenerate zero-round N10"* (`audit/2026-08-06-social-contest-three-lens-audit/03_persuasion_documents_adjudication.md:173` (the N10 row is `:153`)). It costs one integer.

**And this is what makes `E[auto] ≈ E[played]` well-posed.** The anti-exploit constraint is that a player must not be able to shop for a fidelity. If E[played] > E[auto] systematically at equal inputs and equal policy, playing is farming. Parity is measured **at equal inputs and with both arms driven by the same default policy**, so that any residual gap is the procedure and not the player.

**Does binding in-scene make parity easier or change what is being compared?** Worked, not assumed: **it makes it easier, and it does not change the comparand.** `run_parliamentary_vote` already binds within the season — it calls `world.factions[dominant].adjust("L", …)` **inside its own body** (`parliamentary_vote.py:214`) and returns a `VoteResult` describing writes that have already happened. Before the ruling, the played arm would have had its writes deferred to the fold while the auto arm's landed immediately; the two arms would have differed in *when state lands* as well as *what distribution it comes from*, and a parity number over outcomes would have concealed a timing mismatch that an exploit could live in (act, observe, act again in the same season on one arm but not the other). After the ruling both arms bind in-season, so the comparand is what ED-SC-0013 always said it was: the **outcome distribution on matched inputs.** The ruling removes a confound; it does not move the target.

### 5.7 Every `[SEED]` in this branch, in one place

| `[SEED]` | where | what it decides | why it is not in the research |
|---|---|---|---|
| `QUORUM_FRACTION` | venue, S1.1 | when a body may sit at all | v30 §7.2 names "by quorum" and gives no number |
| `HOLDOUT_ROUNDS` (K) | venue, S4 | **K=0 is the *liberum veto*; K≥1 is the Great Law.** The single most consequential number here | the Great Law's sequence has three referrals; that is a structure claim, and §9.7 forbids importing it as a count |
| `FRIVOLITY_STRIKES` | venue, S2.2 | how many off-ground blocks before the clinch (kernel default is 2, `primitives.py:267`) | the rule is sourced; the count is not |
| `UNANIMITY_MARGIN_SCALE` | `VoteAtClose`, §5.2 | whether a lone objector refers back or blocks outright | no historical source states a band edge |
| the parity tolerance | F-C3, §9 | what counts as `E[auto] ≈ E[played]` | ED-SC-0011 FORK-C says it is set when the harness lands; §11 rung 5 |

`ARMATURE_MAX_DSIGMA` (0.50σ), `STYLE_AXIS_PRIMARY`/`OFFAXIS` (1.0/0.15) and `CR5_BACKFIRE_MAGNITUDE` (−2) are **inherited** `[SEED]`s (`armature.py:228-229`, `:336`; `rhetoric.py:366`), not new ones. This branch changes none of them and adds no sixth number.

---

## §6 · Keys, state, ownership, and the write path

**Keys: zero new types.**

| Key | direction | anchor |
|---|---|---|
| `scene.contest_resolved` | emitted | `echo_transport.py:427` constructs it; type from `KEY_TYPE_BY_SCENE["contest"]` (`:108`). Payload per `references/KEY_INDEX.md:819-822`: required `scene_id`, `outcome`, `participants`; optional `persuasion_track_final` (which the spine makes literally the margin). Producer `social_contest` already declared |
| `state.opinion_revised` | read as the members' prior | already declared consumed by `social_contest` (`references/module_contracts.yaml:750`; `KEY_INDEX.md:109`). ⚠ It has **no consumer in the package today** (SC_INVENTORY §C) — this branch would be its first, which is a *closure*, not a new declaration |

**Outcome-token mapping, and the one I deliberately do not use.** `_OUTCOME_BY_DEGREE["contest"]` (`echo_transport.py:114`) maps `Overwhelming/Success → initiator_win`, `Partial → compromise`, `Failure → target_win`. A blocked matter is `Failure → target_win`, which is semantically right: **the blocker is the target of the motion and the blocker won — that is what a veto is.** `key_types.json:958` also declares `stalemate`, which nothing emits. It is tempting and it is wrong here: under unanimity a non-unanimous result always has a dissenter, so there is no stalemate, only a defeat. **No change to `echo_transport.py` is needed for this branch.**

**State changes and ownership.**

| what | owner of the write | when | anchor |
|---|---|---|---|
| bout-local state (`adv`, `Face`, `Reserve`, `Room`, `FaultState`) | the resolver, inside `Bout._apply` | **in-scene, at the move** | `resolver.py:341`; the seam has **no write token** (`04_CODE_ARCHITECTURE.md:695`) |
| `Ballot` / `BallotBook` | the `WinCondition`, on its own result object | at each ballot round | §5.2; **not world state** |
| `LedgerTag(Precedent, key=P, ttl=None)` | the presiding seat's `determine` act | at the terminal, through the fold | `ledger.py:36`, `ledger_add` `:47`; `§C.4` `04_CODE_ARCHITECTURE.md:583` |
| `LedgerTag(Grudge, key=<holdout>, ttl=None)` | same | same | same |
| the `SceneSlot` re-queue on `Partial` | the convener's act via `queue_scene` | at the terminal | `scene_slate.py:34` |

**Where the tags land, and the gap that is not mine.** `LedgerTag` has **no holder field** — tags live on `Settlement.ledger` (`ledger.py:14-17`, `registry.py:102`), never on a Person. So a Grudge against a holdout is a fact the *place* holds, not a fact the holdout carries. `00_BRANCH_SHAPES.md` §2.4 names this as the SE-lane custody gap and proposes one optional `holder: PersonId | None` field. **Not proposed here, not needed here** — the Grudge's game function (raising a hostile-action weight at that place) works without custody. Named so a reader does not think it was missed.

**The degree-keyed consequence column on the calling verb.** Per `§C.4`'s `writes_at(degree)` (`04_CODE_ARCHITECTURE.md:583-594`) and the `kill / wound` precedent (`proposals/2026-09-02-executable-architecture/verb_table.yaml:234 kill / wound`, whose `contests: "the body"` is at `:238`, the only live `contests:` row):

```yaml
determine:
  actor:    a seat with a determine remit at the rung
  requires: quorum ∧ the matter is live ∧ depth < max_depth
  contests: a matter                                # -> seam.contest, prize "a matter"
  writes:
    Overwhelming: [LedgerTag.Precedent(P, ttl=None)]
    Success:      [LedgerTag.Precedent(P, ttl=None), LedgerTag.Grudge(*dissenters, ttl=None)]
    Partial:      [SceneSlot.queue(P, next season)]          # chain cap 3, v30 :383
    Failure:      []                                          # the matter lapses; nothing is written
  emits:    scene.contest_resolved
  refuses:  no_quorum | depth_cap | not_a_member | not_seated
```

`Failure` writing nothing is deliberate and is the branch's cheapest honest statement: **a blocked matter leaves no record but the Grudges the blocking already produced in-scene.** That is what a veto costs the world — nothing happens — and it is why the pathology is a pathology.

---

## §7 · Reuse ledger, false-N-line hunt, and the `on_hung` adjudication

### 7.1 What this composes on (nothing here is new)

| composed on | path:line | what it supplies |
|---|---|---|
| `VoteAtClose` | `resolver.py:98`, `:124 resolve` | the per-member ballot; one new aggregation branch |
| `Panel` | `contract.py:37` | the bench, its member-averaging, and `discipline` as bench weight |
| `panel_win_condition` / `PANEL_AGGREGATION` | `dictionaries.py:699`, `:685` (ratified ED-1057) | the aggregation selector that already names the third value |
| `Bout.resolve` + `_apply` | `resolver.py:440`, `:341` | the loop, and the per-move fault check that makes the antibody bind in-scene |
| `DefeatCatalogue` | `primitives.py:262`, `:277` | **antibody channel 1** — venue-configured fault→clinch, `evasion_strikes` |
| `cr5_self_backfire` | `rhetoric.py:413` | **antibody channel 2**, unchanged, called where it is called today (`resolver.py:430`) |
| `ArmatureConfig` / `position_of` / `dsigma` / `ArmaturePosition.mean` | `armature.py:415`, `:374`, `:436`, `:285` | the alignment gradient, and the recusal gate |
| `deliberative_body_venue` / `assembly_venue` / `_default_panel` | `modes.py:127`, `:73`, `:115` | the venue's proof and temporal registers, and `barred=False` |
| `faction.py` — `Faction.fixed_lean`, `_one_vote`, `vote`, `succession` | `:20`, `:39`, `:45`, `:120` | the bribed deputy for F-C2; the committee band; and the precedent that a per-member deliberation is already modelled here as a bout per voter |
| `run_parliamentary_vote` | `parliamentary_vote.py:125` | the auto arm for the **majority** venue only (§5.6) |
| `scene_slate.queue_scene` / `SceneSlot` | `scene_slate.py:34`, `:25` | the deferral, replacing the cut Holdout Obligation clock |
| `settlements` `LedgerTag` / `ledger_add` | `ledger.py:36`, `:47` | Precedent and Grudge; the one Record primitive, single-owner |
| `degree_from_net` | `engine/autoload/dice_engine.py:227` | the one ladder |
| the spine (`00_BRANCH_SHAPES.md` §2) | — | `margin()`, `ContestOutcome`, `armature=` passthrough, `rng` injection, `contestant_from_person` |

### 7.2 What is genuinely new, each justified

| new | N-line: *cut it, and the emergent possibility lost is…* | size |
|---|---|---|
| the `unanimity_required` branch in `VoteAtClose.resolve` | **a body that cannot act until all assent** — no tally expresses it (§2), so the entire Type-3 conflict class is unreachable | one `if`, ~10 lines |
| `Ballot` / `BallotBook` retention | **a named holdout** — without it there is no signed block, no antibody target, no Grudge recipient, and no *liberum veto* to reproduce | two frozen dataclasses; the loop rewrite of §5.3 |
| `consensus_body_venue` + `holdout_rounds` (K) | **the dial between the Great Law and the Sejm.** K=0 dissolves on a block; K≥1 refers back. Cut it and only one of the two histories is representable | one factory, one field |
| `on_hung ∈ {defer, majority}` | **a terminal for a hung unity that is not simply a win for the blocker** — the Lögrétta's third rung and the Great Law's cap on refusal | one field, both values already implemented |
| the recusal in S4.1 | **the alignment gradient itself.** With the holdout on its own bench, `position_of` gates to the zero vector (`armature.py:388`) and channel 2 flattens to nothing | one `Panel(...)` construction, no state |

**Deletions offered (the `14_NERS.md` meta-rule benchmark: *edits, two of them deletions, and the vocabulary got shorter*).**

- `faction.py:128 coalition_vote` + `:150 coalition_rate` — a **fourth resolver** (§1 defect 6): it builds its own `ContestState`, calls `roll_net` directly and runs `PersuasionTrack.resolve` outside any loop. **Zero production callers** (grep: only `_kernel_tests.py:186-192`). Deleting it removes a parallel resolution path and shortens the vocabulary. **Cost, stated:** ~5 kernel checks go, so `_KERNEL_EXPECTED` (`engine/tests/test_contest_kernel.py:93`, currently 389) moves. That must be a deliberate same-commit edit, never a surprise (F-C5).
- `contest_legacy_stub.py:191 run_contest` — dead; the `contest/__init__.py:24` docstring names a caller path that no longer exists. **Keep `:67-71`'s `PERSUASION_*` constants** until the spine's `margin()` lands, because `parliamentary_vote.py:44-50` imports exactly those five.

Both are **offered**, not required by this branch. Neither is bundled into the S2 juncture's own falsifiers except as F-C5.

### 7.3 False-N-line hunt over my *own* additions — and the `on_hung` adjudication

The pattern to hunt (`14_NERS.md` §3): *a mechanism was named, a **store** was proposed for it, and the store's job was already being done by an object the design had ruled in.*

| my candidate | its claim | verdict |
|---|---|---|
| a `Holdout` state object carrying who is blocking and for how long | a veto-war needs a persistent blocker record | **CUT.** `BallotBook.dissenters` is recomputed each round from the ballots, and the durable half is a `Grudge` tag (`ledger.py:36`). A store would be a second owner of the same fact. (This is the shape spec's own cut, re-derived independently and confirmed.) |
| a **frivolity score** on the block (the critique's "armature dot-product below threshold") | the antibody must be proportional to misalignment | **CUT.** The dot-product already exists (`armature.py:346`) and already produces a proportional effect — through the reception roll, not through a stored score. Storing it would duplicate `dsigma`. **Cost accepted and named in §8: the resulting antibody is probabilistic, and "proportional to misalignment" is therefore a CONVENTION-grade property, not a MECHANICAL one.** |
| a `consent` edge per member per matter | assent must be durable | **CUT.** Under §4.1's ruling the ballot binds for its round and the terminal is a `Precedent` tag. A per-member consent edge would be a third representation of the same decision (ballot, tag, edge). |
| **`on_hung: lot`** | a hung unity needs an anti-capture terminal | **CUT — it is a false N-line, and this reverses the shape spec's "keep at medium confidence".** |
| a ninth `PROCEEDINGS` row | consensus needs a canonical proceeding | **CUT** — §5.1. `INSTITUTIONAL_MODES` is the tier for mechanism-without-canon-claim, and the canonical 8 are a transcription. |

**`on_hung: lot`, adjudicated in full, because the brief asks for it explicitly.**

Four arguments, and they converge:

1. **It fails the meta-rule.** `WeightedDraw` and sortition exist **nowhere** in the tree (SC_INVENTORY §5; `audit/2026-08-06-social-contest-three-lens-audit/01_lens…md:87` records sortition ABSENT). `on_hung: lot` reads as one venue field but pulls in a mechanism that is not a `WinCondition` on the sigma kernel — it is a draw that **bypasses** the kernel. That is the parallel resolver the critique's own architectural verdict forbids (*"Reject any 'fix' that adds a parallel resolver"*), and *a fix that adds a system has failed* (`14_NERS.md` §1).
2. **The claimed lost possibility survives the cut.** The claim is "an anti-capture terminal". The anti-capture work in a Type-3 procedure is done by the **antibody**, and history supplies the antibodies for *consensus* specifically: the frivolity rule and the cap on refusal (`politics…:94`). The lot is history's antibody for a **different** Type-3 procedure — sortition — whose pathology is *control of the pool*, not the holdout's veto-war (`politics…:192` names the two pathologies separately). Substituting one procedure's antibody for the other's is a category error dressed as reuse.
3. **The research argues against a lot at this scale.** Dowlen 2009, via `renaissance-machination…md:33` and `:81`: the lot's protective power *"degrades as the pool shrinks"*, and the Florentine and Venetian small-pool lotteries were *"in effect weighted lotteries"* open to capture. **A hung assembly is a small pool by construction.** The research does not merely fail to license the lot here; at this pool size it predicts the lot would not do the job claimed for it.
4. **A cheaper value does the job with zero new mechanism.** `on_hung: "majority"` re-runs the same `VoteAtClose` at `weighted_by_standing`, a branch that already exists (`resolver.py:128`). It is the Lögrétta cascade's third rung and the Great Law's cap on refusal, and it makes F-C2 a controlled two-arm experiment (§5.5).

**The cost of cutting it, stated rather than buried.** The Lögrétta cascade genuinely has a lot as its *second* rung (`rhetoric…:516`), and I am dropping a rung the history has. What is lost is the churn class the critique named — *"the dice chose wrongly"*, the leader nobody fully backs (`critique.md` §2.4, `caillois FG-4`). **This branch does not deliver that class**, and no other branch in this wave does either. If sortition is built later it belongs where its own pathology lives — a **selection** venue (Type 2: who shall decide), not a hung-matter terminal (Type 3) — and it should arrive as its own `WinCondition` with its own N-line, not as the second value of somebody else's field.

**Net.** Five of my six candidates cut; one kept and *reduced* (`on_hung`, two values, both already implemented). Together with the two deletions offered in §7.2, the ratio moves the right way — provisionally, on paper.

---

## §8 · Invariants, graded honestly

Grades per PR #362 `PART D` (`04_CODE_ARCHITECTURE.md:811`): **STRUCTURAL** (cannot be spelled) · **MECHANICAL** (one path refuses at runtime) · **CONVENTION** (a reader notices). *"A row graded MECHANICAL or CONVENTION is here because the reader will assume it is structural, and the assumption is the failure mode."*

| id | invariant | grade | what carries it |
|---|---|---|---|
| **I-C1** | members are Persons; a faction never ballots | **MECHANICAL**, not structural | `contestant_from_person` (spine §2.5) refuses non-Person input. STRUCTURAL only under PR #362's `claimants : PersonId[]` — and **today `scene_dispatch.py:121 _emergency_council_parties` returns faction-derived ints**, so nothing structural exists yet |
| **I-C2** | a block is a signed act with a named author | **MECHANICAL** | `Ballot.member_index` is required at construction; a `BallotBook` cannot be built without one per bench member. Not structural: nothing prevents a caller inventing an index |
| **I-C3** | the count grades; the presiding seat's act writes — a threshold never produces the outcome (`T-b`, `01_AXIOMS.md:284`) | **MECHANICAL** | `VoteAtClose` returns `(winner, margin)`; every `LedgerTag` is written by `determine`'s `writes_at(degree)` column through the gate (§6). Under a PR #362 veto this survives as a convention |
| **I-C4** | the antibody's **existence** is not optional in an assembly venue | **MECHANICAL** | `consensus_body_venue` constructs `DefeatCatalogue(evasion_strikes=FRIVOLITY_STRIKES)` with no path to `0`/`None`. `primitives.py:270` documents `0/None` as the disable, so a caller passing an override could switch it off — hence MECHANICAL, not STRUCTURAL |
| **I-C4b** | **the antibody's cost is proportional to armature misalignment** | ⚠ **CONVENTION** | **This is the grade that matters, and it is the weak one.** No function computes a misalignment-proportional cost. `cr5_self_backfire` keys on `(orientation, landed)` only (`rhetoric.py:449-455`); alignment enters as a *probability shift* via a δσ that is **never negative** (`armature.py:365`). So "proportional" is a statement about an emergent rate, observable only over N seeds, and asserted by no signature. **A CONVENTION antibody does not stop a veto-war** — and this one is doubly contingent, because `ED-SC-0021` records that Obscuring is dominated contest-wide and CR5's upside is unwired, so a rational holdout picks a Revealing style and channel 2 never fires at all. **Channel 1 is what actually stops a veto-war, and it is MECHANICAL. Do not credit channel 2 with channel 1's grade** |
| **I-C5** | a block's cost lands in the same scene as the block | **MECHANICAL, and it already executes** | `resolver.py:453` checks faults after every move; `resolver.py:423-437` strips Face inside `_apply`. Neither is deferred to close or to the fold |
| **I-C6** | no member's ballot is an input to another member's ballot | **STRUCTURAL by signature** | the per-juror decision rule's inputs are `(gap, k, noise)` and there is no ballot-history parameter (`resolver.py:139`, `:144`). Adding one is the only way to break it, and §4.4/§12 decline it explicitly |
| **I-C7** | the auto arm and the played arm agree in band on matched inputs | **CONVENTION until F-C3 runs**; MECHANICAL only under the test | nothing today measures it. ED-SC-0013's constraint is stated; ED-SC-0011's harness does not exist |
| **I-C8** | ballot retention does not move the seeded goldens | **MECHANICAL under the control in §9**, CONVENTION until it runs | §5.3's three constraints (same draw count, same order, no short-circuit). `scene_dispatch.py:118` puts this exact function on the golden path |

**The honest summary a critic should hold me to:** of the eight, one is STRUCTURAL, five are MECHANICAL, two are CONVENTION — and **the one the whole Type-3 argument rests on (I-C4b) is a CONVENTION.** The design survives that because the *primary* antibody (I-C4, channel 1) is MECHANICAL and terminates the block rather than pricing it. If channel 1 were removed, this branch would ship a known-defective consensus procedure with a decorative antibody.

---

## §9 · Falsifiers

Per `CLAUDE.md` §0.1 pt 3 — a result claim carries, in the same commit, the test that would have shown it wrong and that test's outcome. Per pt 2 — **each assertion must be able to observe the failure it excludes**, which for a *probabilistic* antibody (§8 I-C4b) means a **rate over N seeds**, never a single run, and a loop that asserts conditionally must assert that it asserted.

**F-C0 · THE CONTROL, and it is not optional.** `scene_dispatch.py:118` routes every production contest through `guild_arbitration` → `panel` → `VoteAtClose`'s weighted branch. So:

```
python -m pytest engine/tests/test_mc_v18_regression.py engine/tests/test_f7_smoke_oracle.py -q
```
**Both campaign goldens must be byte-unchanged** (n=2/seed-0 and n=8/seed-42). If they move, ballot retention changed the RNG stream and the branch has silently changed `agon` — §5.3 failed. Additionally the auto arm must be untouched: `git diff --stat systems/social_contest/sim/parliamentary_vote.py` is empty for this juncture.

**F-C1 · The antibody is observable as a difference between two arms — as a RATE.**
```
python -m tools.consensus_probe --arm aligned --arm misaligned --seeds 400 \
       --members 7 --print face_delta_mean block_upheld_rate clinch_rate
```
One Conviction-aligned holdout versus one misaligned holdout, same seed set, everything else identical. Expected: `clinch_rate` and `|face_delta_mean|` strictly higher on the misaligned arm; `block_upheld_rate` strictly lower. **Names the failure it excludes:** if the two arms are statistically indistinguishable, the antibody is decorative and I-C4b is not merely CONVENTION but false. A single-run version of this test cannot see that failure and must not be written.

**F-C2 · The *liberum veto* reproduction — the one place history is given a chance to break the design.**
```
python -m tools.consensus_probe --sweep N=3,5,7,11,15,21 --sweep K=0,1,2 \
       --arm unanimity_required --arm weighted_by_standing \
       --bribed-deputy 1 --seeds 400 --print p_block
```
Uses `faction.py:20 fixed_lean` as the bribed deputy — a real act with a real cost, not a cheat (Machiavelli's precedent: bribery as a legal action).
- **Prediction A (failure half, `…closing-findings.md:43`):** under `unanimity_required` with a bribed deputy, `P(block) → 1.0` as N grows and is **highest at K=0**; under `weighted_by_standing`, `P(block)` is flat in N.
- **Prediction B (success half, `:45`, and it is not optional):** with **no** bribed deputy and a fractionalized body, `unanimity_required` does **not** paralyse — `P(block)` stays low. The framework predicts both halves; reproducing only the first would be cherry-picking.
- **Prediction C (`on_hung`, §5.5):** `on_hung="majority"` collapses `P(block)` relative to `"defer"` at the same N and K. This is the Sejm/Venice contrast as a controlled arm.
- **The number is the deliverable; the historical one-third is NOT the target.** §9.7 forbids fitting to it. **If prediction A does not reproduce, the branch is wrong and the history is not.**

**F-C3 · Auto-vs-played parity, per venue (ED-SC-0011's harness, finally built).**
```
python -m tools.consensus_parity --seeds 200 --venue weighted_by_standing \
       --auto run_parliamentary_vote --played bout --print band_agreement_rate mean_delta
python -m tools.consensus_parity --seeds 200 --venue unanimity_required \
       --auto zero_exchange --played bout --print band_agreement_rate mean_delta
```
Two runs, because the auto arm differs per venue (§5.6). Both arms driven by the same default policy on matched inputs; `rng` injected through the spine so the seeds are comparable at all. **The number is the deliverable.** The acceptance tolerance is a `[SEED]` to declare against ED-SC-0011 FORK-C's stated lean (*"unbiased mean is the hard anti-exploit constraint; variance looser for auto"*), so `mean_delta` is the gate and `band_agreement_rate` is the report. Combat's r8 parity harness is the template.

**F-C4 · Symmetry.** Mover and holdout swapped over 400 seeds → mirrored margin distribution within tolerance. Guards the turn-order bias the groundup audit measured at 87/13 (`v30-snapshot-2026-06-28:designs/audit/2026-06-03-contest-groundup/AUDIT.md` P1) — a regression falsifier every branch in this wave inherits.

**F-C5 · The kernel count moves deliberately.** `engine/tests/test_contest_kernel.py:93 _KERNEL_EXPECTED` changes in the **same commit** as the `coalition_vote` deletion, and the removed `ck`s are **deleted, not skipped**. `python -m pytest engine/tests/test_contest_kernel.py -q` green at the new value. Names the failure it excludes: a silently-loosened count.

**F-C6 · Retention is order-faithful (the direct falsifier for §5.3 and I-C8).**
```
python -m pytest tests/valoria/test_vote_at_close_ballots.py -q
```
Seed the module RNG, run the pre-change weighted branch and the retained-ballot branch on the same bench, and assert **the same number of `random.gauss` calls, in the same order, producing the same `wA` to exact equality — not `pytest.approx`.** §0.1 pt 2: `approx` on an exactness claim is not a weak test, it is an absent one. Counting the draws (a `Random` subclass wrapper) is what makes it observe the failure rather than assume it.

**F-C7 · The unanimity branch is strict.** A body of 7 with 6 assents returns `winner == B` and `margin < 0` — never `A`, never `"draw"` — across the full ballot space, and `Overwhelming` is reachable **only** at share exactly 1.0. Exhaustive over 2⁷ ballot patterns with the count asserted (`assert checked == 128`), so a vacuous pass is impossible.

**What the S2 juncture's execution artifact is (§0.2).** F-C1..F-C7 pass; **F-C2 prints `P(block)` against N and K for both aggregations**; **F-C3 prints the parity rate for both venues**; and the two campaign goldens are byte-unchanged (F-C0). Until those outputs exist, this branch is **paper**, and no `## Status:` line changes that.

---

## §10 · Fairness and playability

**Every "no dominant option" claim below is an UPPER BOUND, not an estimate.** No AI-vs-AI best-response sweep has been run — `ED-SC-0021`'s falsifier remains unrun, and only combat's r8 parity harness exists in the tree. Asymmetric skepticism is itself a finding (`04_ners_audit.md`), so this section applies the same bound to the favourable readings as to the unfavourable ones.

### 10.1 The exploit surface — a unanimity rule is the richest griefing surface in the system

**How a player abuses it, concretely.** The corpus names the exploit before I do (`politics…:94`): *"'winning' means extracting concessions as the price of one's assent, or framing the finally-agreed position as one's own."* In this design that is three distinct plays:

| the play | what stops it | grade |
|---|---|---|
| **Serial blocking** — block every matter to paralyse a rival body | channel 1: an off-ground block accrues `fault.evasion` and clinches at `FRIVOLITY_STRIKES`, **setting the block aside**; channel 3: a durable `Grudge` per block accumulates against the blocker at that place | MECHANICAL |
| **Hostage-taking** — assent only in exchange for a concession | **Nothing stops it, and nothing should.** This is the *sanior pars* claim used as a weapon inside the dispute (`politics…:110`, model 9) and it is the genuine substance of consensus politics. It is bounded by the Grudge accumulation and by `on_hung="majority"`, which caps the price a holdout can charge before the body simply proceeds | MECHANICAL via `on_hung` |
| **The bribed deputy** — a rival pays one member to block | **Nothing stops it, and the history says it should work.** Part IX's whole point is that unanimity plus external bribers entails hold-up. This is the portrait the venue paints: **a polity that chooses unanimity has chosen this.** What bounds it is the venue *choice* — `on_hung` and K are the constitution, and `on_hung="majority"` is the anti-capture answer the Lögrétta and the Great Law both reached for | MECHANICAL via the venue |
| **Style-shopping the antibody** — block in a Revealing style so channel 2 never fires | ⚠ **Channel 1 still fires** (orientation-independent), and this is exactly why channel 1 is the primary. **Channel 2 alone would be fully evadable**, and `ED-SC-0021` says a rational player is already picking Revealing for unrelated reasons | channel 1 MECHANICAL; **channel 2 evadable — named, not hidden** |
| **Quorum-shopping** — convene when opponents are absent | `Refusal(no_quorum)` at S1.1, and the judging set resolves ONCE at the boundary (`§C.5.1`), so it cannot be gamed mid-proceeding. But `QUORUM_FRACTION` is a `[SEED]` and this exploit's severity is entirely a function of that number | MECHANICAL, magnitude unset |

**The Venice qualification binds here** (`renaissance-testing-the-model-and-closing-findings.md:19`, Part VIII.1): the mechanism **channels** manoeuvre, it never eliminates it. Two of the five rows above are deliberately not stopped. That is the design, not a hole — but it is a design that must be *chosen*, and `on_hung` plus K are where the choosing happens.

### 10.2 Dominant-strategy risk

- **"Always hold out."** Bounded by channel 1 (the block is set aside and you lose the exchange), by Face cost when the block is Obscuring and fails, and by durable Grudges. ⚠ **Upper bound only** — and I have a specific reason to distrust it: the same reasoning applied to Obscuring styles produced `ED-SC-0021`'s finding that the orientation bit is dominated contest-wide, which nobody predicted from the design either. The honest statement is *no dominance has been demonstrated*, not *none exists*.
- **"Support forever."** Inherited and real: `resolver.py:350-351` — `support` spends 2, regroups +4 (`primitives.py:51`, `:52 REGAIN = 4`) and builds ethos **with no fault accrued**. A holdout who never answers but always "supports" is net-positive on Reserve and never triggers the silence clinch. `00_BRANCH_SHAPES.md` §1 names this as a live kernel defect; **it is not fixed here and it partially defeats channel 1's yield-strike leg** (the evasion leg still bites, because `support` does not block either). Named, unmeasured, and it belongs to the spine.
- **"Never convene."** If blocking is cheap, the dominant meta-move is to stop putting matters to a consensus body at all. `on_hung="majority"` is what makes convening worth doing. Untested.

### 10.3 What the player decides, and the consult load

| step | the decision | who |
|---|---|---|
| S1 | put this matter, at this rung, now — or not | the convener |
| S2 | the Style pick (one per contest, `social_contest_v30 §4 Step 2`) and per-exchange moves | mover and opponent |
| S3 | none — the ballot is the member's disposition resolved by the resolver | — |
| S4 | **block or assent** — and, if blocking, on what ground | each member, once per round |
| S4.1 | the moves of the holdout round | mover and holdout |
| S5 | none — the terminal is determined | — |

**Consult load per member per matter: 1 ballot + ≤ K block decisions.** At K=2 that is **≤ 3**, which sits inside the 3–5 scene-action budget `player_agency_v30` §4 already assumes (via ED-SC-0013's scene-slate reframing).

**S-UP / S-DOWN** (`14_NERS.md` Rule 2, both halves graded separately):
- **S-UP — can a demand travel up and be filtered by a named person at a rung?** **Yes.** The convener is a named seat with a convene remit and can refuse to put the matter (S1). That is the *lögsögumaður* as filter, and the filtering person is named.
- **S-DOWN — can an opportunity travel down and reach a person who holds no post?** **Partially, and I will not overclaim.** In an RM assembly ("Mandate ≥ 3 organizers by consensus", `social_contest_v30.md:407`) a postless organizer is a member and holds a full veto — the strongest S-DOWN in the subsystem. In a Jarl Assembly, membership is seated, so a postless person reaches it only as a petitioner. **S-DOWN is venue-dependent, and that is a real limit, not a pass.**

**R is not scorable** (`14_NERS.md` Rule 3): R binds at seats a player can occupy, and *"which seats does a campaign offer at start"* is unanswered for this subsystem. Saying so is a legitimate verdict; the source document says it about itself.

---

## §11 · Open forks, through the five tests

Order per `CLAUDE.md` §0: superseded → irrelevant → answered by a design document → answered by precedent → answered by architecture. **Escalate only what survives all five.**

1. **`unanimity_required` — is implementing it a design change Jordan must approve?** ⚠ **This deserves more care than `00_BRANCH_SHAPES.md` §5(k)3 gave it**, because the tree does not merely record the alternative — it records a *rejection*. `dictionaries.py:681` states the reason: *"unanimity-required (would make Panel strictly harder to win than Expert Judge — a dominance asymmetry)"*, and *"Jordan rejected simple-majority as the default and selected weighted-by-standing"* (ratified, ED-1057).
   **Test 3 (design document) answers it, and the distinction is exact:** what was ratified is the **default aggregation for the Panel adjudicator** — `PANEL_AGGREGATION`, the value `panel_win_condition` uses when no caller says otherwise. `PANEL_CLOSURE["aggregation_ratified"]` (`dictionaries.py:736`) is scoped to the Panel closure of ED-137. This branch **does not change that default**: `guild_arbitration` keeps `weighted_by_standing`, `PANEL_AGGREGATION` is untouched, and the new value is selected only by a venue that explicitly asks for it. The dominance-asymmetry objection was about **choosing between adjudicators inside one contest** — an assembly deciding its own matter is not that comparison.
   **Closed by design document, no ruling.** ⚠ The falsifier for my own reasoning: **if a commit changes `PANEL_AGGREGATION` itself, or makes `guild_arbitration` unanimity, it has overstepped this closure** and needs the ruling I am declining to ask for. F-C0's golden control catches exactly that.
2. **Sortition / acclamation.** Sortition: **cut with reasons** (§7.3) — not escalated, and it is not a deferral either; a later sortition build belongs to Type-2 selection with its own N-line. Acclamation (`modes.py:351 CeremonialMode`, critique `caillois FG-3`): **irrelevant to this branch (test 2)** — nothing is at issue in a ceremony, so it is not a contest, and a unanimous first ballot with no debate is already acclamation-shaped and needs no mode. Not escalated.
3. **ED-SC-0020 (burden-parameterized gate, `needs_jordan: true`).** Answered by architecture in the spine (`00_BRANCH_SHAPES.md` §2.1); consensus is `burden: NONE` either way and the row's disposition does not gate this branch. Not escalated **from here**.
4. **ED-SC-0011 FORK-C (the parity tolerance).** The ledger row's own text says the tolerance *"is set here when the parity harness lands"* and states the lean (*unbiased mean is the hard anti-exploit constraint; variance looser for auto*). **A measurement to run and a number to declare (test 5), not a ruling.** `needs_jordan` is already `false`. Not escalated.
5. **ED-SC-0013.** `status: resolved`. **Superseded/closed (test 1).** Not escalated.
6. **ED-SC-0015 (Parliamentary total-victory Mandate stacking, `needs_jordan: true`).** ⚠ **The shape spec claims this dissolves by precedent via `LedgerTag(ttl=1)` + `ledger_add` dedupe. I verified the claim and it is REFUTED as stated.**
   - The dedupe half **holds**: `ledger_add` (`ledger.py:47-59`) refreshes in place on `(kind, key)`, so two votes in one season on the same faction refresh one tag rather than stacking two.
   - The expiry half **does not hold**: `ledger_sweep` (`ledger.py:69`) has exactly one call site, `registry.py:207`, inside `succeed_governor` (`registry.py:199`) — and **`succeed_governor` has zero callers anywhere in the tree.** `season_manager.py:33 advance_season` contains no ledger call. Worse, `ledger_has` (`:61`) and `ledger_get` (`:65`) do **not** filter by `is_expired`, so an expired tag reads as live until something physically removes it. **A `ttl=1` tag today is permanent in practice** — which is the identical defect ED-SC-0015 was filed about (`parliamentary_vote.py:218`: *"one-season penalty; temporary-modifier restoration deferred to season_manager"*).
   - **Re-running the five tests on the corrected facts.** Test 4 (precedent) still gives the *shape*: `ledger.py`'s own docstring already declares the intent — *"Durable tags (ttl=None) never expire; transient tags drop on the season-boundary sweep"* (`ledger.py:16`) — so the design decision was made and only the wiring is missing. Test 5 (architecture) then closes it: **one call to `ledger_sweep` at the season boundary, plus expiry filtering in `ledger_has`/`ledger_get`, and a `ttl=1` tag becomes the temporary modifier `parliamentary_vote.py:218` says it wants.** With a transient tag there is nothing to stack, so the "stack or cap" menu the row poses **dissolves** — but it dissolves **on a one-line SE/IN fix, not on today's tree.**
   - **Verdict: closable, not closed.** The row should be closed with *this* citation — naming the missing sweep — and **not** with the shape spec's, which asserts an expiry mechanism that does not run. **`needs_jordan` should become `false`**, since no live design choice survives: two defensible options do not lead to materially different games once the tag is transient. **The one-line wiring is SE/IN-lane work and is not proposed here.** I have not edited the ledger row; a later phase should.

**Escalated from this branch: nothing.** No fork here is a live design choice where two defensible options lead to materially different games, and none would overwrite ratified canon. `needs_jordan` is not a parking space.

---

## §12 · The strongest case against this proposal, and the attacks I ran

**12.1 The strongest case against it, stated as an opponent would.** *This branch's central promise is an antibody, and its antibody is the wrong one wearing the right one's name.* The critique asked for a cost proportional to armature misalignment; the tree has no such function; §5 substitutes a fault-clinch that was designed for a different purpose (arguing off the live issue) and calls it the Great Law's rule. The mapping is an **interpretation**, not an implementation — a frivolous objection and an off-ground argument are not the same thing, and a holdout who blocks *on* the live ground for bad reasons accrues no evasion at all. **That gap is real and I cannot close it without adding a mechanism.** What defends the design is narrower than the promise: an on-ground block that fails still costs the blocker the exchange, and a durable Grudge lands regardless — but a *well-argued cynical block* is, in this design, indistinguishable from a principled one. Which, arguably, is also true of the history. Recorded as the honest limit rather than argued away.

**12.2 The second strongest.** Every falsifier in §9 assumes the spine lands first — `margin()`, `armature=` passthrough, `rng` injection, `contestant_from_person`. **Without the spine, F-C1 and F-C3 are unrunnable** (no armature through the seam; no comparable seeds), so more than half this branch's evidence base is downstream of a document that is also paper. That is not a hidden dependency, but it is a real one and it means S2 cannot precede S0.

**12.3 Attacks run, with results. An attack that fails and is reported as failed is a result.**

| attack | result |
|---|---|
| *"`cr5_self_backfire` is keyed to armature alignment, as the shape spec says"* | **SUCCEEDS against the shape spec.** The function's signature is `(style_key, landed, my_standing)` (`rhetoric.py:413`); alignment appears nowhere in it. §1 row 6, and it is the largest amendment in this document |
| *"the antibody therefore does not work"* | **FAILS.** Channel 1 (`DefeatCatalogue` evasion clinch, `primitives.py:277`) is orientation-independent, MECHANICAL, terminates the block, and executes today. The antibody works; the shape spec named the wrong channel as primary |
| *"per-member ballots need a bandwagon term or the 'deliberation' is fake"* | **FAILS, and adding one would be the defect.** PR #362 `41a` (`04_CODE_ARCHITECTURE.md:863`) makes order-independence falsifiable, and `deliberate(frozen)` is a pure map (`:509`). More importantly the *liberum veto* reproduces without it: one blocker suffices regardless of order. Declined with a reason, and I-C6 makes the decline structural |
| *"binding in-scene conflicts with PR #362"* | **FAILS on the primary text, and I decline to manufacture it.** `§E.1` (`03_VERBS_AND_LOOPS.md:217`) grants a contest its own shorter clock; row 49 (`:871`) forbids **nesting an Act**, and the block is a `Move`, not an Act; `§C.5`'s no-write-token holds because the durable tags are written by the fold after the seam returns. §4.4 has the full working. The one boundary is named in one sentence there; the spine agent owns the verdict |
| *"ballot retention is free"* | **SUCCEEDS as an attack on a careless implementation.** `scene_dispatch.py:118` puts `VoteAtClose`'s weighted branch on the campaign golden path, so a generator→loop rewrite that changes the draw count or order moves `test_mc_v18_regression`. §5.3's three constraints and F-C6 exist because of this attack |
| *"`on_hung: lot` is a false N-line"* | **SUCCEEDS.** The shape spec left it INCONCLUSIVE at medium confidence; §7.3 closes it as CUT on four converging arguments, one of which (Dowlen's small-pool degradation) argues against the lot at exactly this scale. The cost of the cut is stated |
| *"ED-SC-0015 dissolves via `LedgerTag(ttl=1)` + dedupe"* | **SUCCEEDS as an attack on the shape spec.** `ledger_sweep`'s only caller has zero callers, and `ledger_has`/`ledger_get` do not filter expiry. §11 rung 6 re-derives the closure on corrected facts — closable, not closed |
| *"a ninth `PROCEEDINGS` row is the natural home"* | **SUCCEEDS as an attack on my own first draft.** The 8 rows are a cited transcription of a canon table (`modes.py:478`); a ninth invents a canon cell. Moved to `INSTITUTIONAL_MODES`, which is the tier for mechanism-without-canon-claim |
| *"the unanimity margin makes `Overwhelming` unreachable in a large body"* | **FAILS, and that is the design.** `Overwhelming` requires share exactly 1.0, which is what "unity" means. What a large body makes rare is unity, correctly |
| *"`run_parliamentary_vote` is the auto arm, as the shape spec says"* | **SUCCEEDS.** It implements a Mandate-pool majority with no unanimity path (`parliamentary_vote.py:200-206`). §5.6 splits the arm per venue |
| *"channel 2 is evadable by picking a Revealing style"* | **SUCCEEDS, and `ED-SC-0021` says a rational player already does.** Not fixable inside this branch — it is that row's open question. Reported in §8 I-C4b and §10.1 rather than mitigated with a guard |
| *"F-C2 is decoration — the design was built from the history it 'tests'"* | **PARTLY SUCCEEDS.** The analytic-narratives hazard (`renaissance-machination-games-lens-and-review.md:87`, Part VII finding 7; restated as MITIGATED-NOT-ELIMINABLE at `renaissance-testing…md:89`) is *"a permanent epistemic condition of the method, not a fixable error."* What reduces it here: F-C2's prediction A is derivable from the design alone (unanimity + a bribed deputy + no randomizing step), and prediction B is an *unfavourable-to-simplicity* prediction the design does not want (unanimity should be **fine** absent bribery). Requiring both halves is the only thing that makes it a test rather than an illustration |

**12.4 Asymmetric-skepticism check on myself.** I applied a harder standard to the shape spec's antibody binding (which I refuted, in detail) than to its `unanimity_required` slot claim (which I confirmed after checking four sites). Both were checked; only the first was *attacked*. Re-attacking the second produced §11 rung 1's correction — the tree records a **rejection**, not merely an unimplemented alternative — which the first pass had missed. **I also accepted the critique's "sound/high" verdict on `contest-locus FG-3` on the strength of its own self-authored verifier**; its location I verified, its leverage I did not re-measure. That closure is **PROVISIONAL** under the same rule.

**12.5 Self-review bias, and what an independent reviewer would add.** This document is inside its own audit scope (SESSION_BRIEF §8.6). Three limits a reviewer with no stake would raise:

1. **The `speaking_order` in S2.1 is decorative as written.** It orders the moves, but `Bout.resolve` (`resolver.py:441-442`) already alternates `for side in (A, B)` — with two contestants there is no order to permute. The `sententiae` ordering only becomes mechanically real if the *members* speak, which this design does not have them do. **A reviewer would call it grounded-but-inert, and they would be right.** I keep it because S4.1's holdout rounds *do* order (mover, then holdout, per round) and because the `speaking_order` Query is what a later N-party version would need — but its N-line today is weak, and I mark it as the most likely thing in this document to be cut by the next pass.
2. **`FRIVOLITY_STRIKES` is doing the work of a whole constitutional rule with one integer**, and no measurement anywhere in this wave tells anyone what it should be. At 1 it makes any off-ground move fatal; at 3 it may never fire inside a short assembly budget. §5.7 marks it `[SEED]`; a reviewer would say the branch's headline claim is hostage to an unset number, and that is accurate.
3. **The whole branch inherits `contestant_from_person`**, whose `ATTRIBUTES → faculty` mapping is the *"one line that does not ship"* the three-lens audit named (`04_reductive…md:210-212`). If that line is wrong, every branch in this wave is wrong the same way.

---

*One file. Nothing else was created or edited. Status PROPOSED; grade paper (§0).*
