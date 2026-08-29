# 03 — Findings: T7 debate and negotiation · T8 the world churns · T9 field investigations

## Status: FILED (2026-08-29) — analysis. Reads: [`00_INDEX.md`](00_INDEX.md)
## Severities: BLOCKER (throughline unreachable as designed) · DEFECT · GAP · NIT.

---

# T7 — Events, political occurrences, clocks and gates are the basis for what gets debated, negotiated and argued about

**Verdict: PARTIAL.** The event→content half is genuinely built; the *argument* half is absent, the
*negotiation* half is designed nowhere, and the return edge is blocked on a filed fork.

## T7 steelman

A closed provenance chain from occurrence to politics. A world event fires and its effects terminate in
tags with required provenance — `we.route_severed` deposits a graded `Precedent: route_cut:<place>`
(`11:553-555`); a treaty breach deposits a Grudge on the treaty **edge** (`12:405-408`). `12 §5.2` then
makes a motion's required `subject` legally citable against exactly that tag: *"censure the crown over
the Baralta treaty's breach"* names a real tag on a real edge, *"not a free-text pretext"*
(`12:509-513`). Because every tag carries non-empty provenance, **no motion can exist without an
antecedent occurrence** — an argument that always exists regardless of what happened is unconstructible.
The Slate closes the perception leg: every candidate requires a causing Key, and the five world-state
triggers carry clock band transitions, treaties and control changes to the player. The epistemic layer
supplies the attack surface — *"an argument is a set of `prop_id`s, each with a provenance the
opposition can attack"* — and `09 §3.4` binds an advance term to the ruled `Condition` grammar, so one
predicate vocabulary underlies hooks, claims and potentially motions. Blocs give arguments **parties**
without authorship.

## T7 findings

1. **[BLOCKER] There is no debate mechanic — only a vote.** `social_contest` appears **exactly once** in
   the whole v2 directory, and that occurrence is the ED-SC-0002 docket row itself (`00:311`).
   `ad.motion` is `price(magnitude)` in standing, a monotone `vote_bar`, and summed `vote_weight` — no
   exchange in which a claim is made, contested, and its provenance attacked. **Canon owns that
   mechanic**: a CANONICAL contest system whose adjudicator table lists *"Parliamentary session"* as a
   crowd proceeding (`social_contest_v30.md:35`), with a +2D bonus for *"citing a specific, named,
   verifiable claim"* (`:169`) and a Domain Echo keyed to the cited precedent (`:290-291`). The epistemic
   layer's parliamentary argument is composed on in `02` and `09` but **nowhere in `12 §5`** — a motion
   has no `prop_id` and nothing the opposition attacks. — **structural**
2. **[DEFECT] The deliberative body is causally silent.** `ad.motion` declares `consumes: [] emits: []`
   (`12:572`). A passed or defeated motion produces **no Key** — it cannot satisfy the candidate
   contract's C-1, cannot appear on the Slate, and cannot enter `causes[]`, so `09 §7`'s arc-walking is
   broken for every parliamentary event. Worse, its own `Precedent` residue requires non-empty
   provenance — provenance the module never emits. — **structural**
3. **[DEFECT] `ad.motion` is `d_sigma` with no `ob_sites` declaration at all** (`12:566-580`). Under
   `00 §7` an undeclared site makes the commensurability gate *"a rule nothing can check"*, and a site
   without its fields is *"UNEVALUABLE, not passing"*. And since subject, magnitude and every
   `vote_weight` are disclosed **exact**, the vote sum is on the board — by `00 §7`'s own resolver table
   this is either the wrong engine or an undeclared noise term. *Authors would dispute*: `12 §8`
   self-audits P-v as a pass, reading the roll as persuasion-in-the-chamber uncertainty. **But that
   uncertainty is precisely a debate, and the suite ships no model of it** — the roll is a debate-shaped
   hole with no pool, no obstacle, no site. — **structural**
4. **[SOFTEN — PR #338's finding is half-fixed, and the fixed half should be credited.** The v2 motion
   does **not** fire unconditionally every season for free: it costs a `post.budget` point and
   `k·magnitude` of the proposer's standing, and for NPCs it must win the appeal softmax against every
   other action. It also cannot exist without some event having left a tag. **Not fixed:** there is no
   event *gate* — the trigger is actor appetite, and no freshness term binds the subject. `09 §3.1`'s
   `tag age` term kind exists one document over and `12` does not use it, so **a thirty-season-old
   grievance is exactly as motionable as yesterday's breach.** — **omission**
5. **[BLOCKER — pre-existing, correctly abstained, but T7's cost must be named] The ED-SC-0002
   abstention blocks T7's *return* edge.** Even if a debate were composed in, its outcome could not reach
   the strategic layer: ED-SC-0007 is blocked at spec level by the echo-keying fork, and one ruling
   *"unblocks ED-SC-0007 … closes the AU-5 seam"*. **T7's "argued about" leg fails in both directions:**
   no argument mechanic going in, no owned echo keying coming out. — **structural (blocked, not the
   suite's error)**
6. **[GAP] Treaties are rolled for, not negotiated, and the negotiation is designed nowhere.**
   `act.treat` is one row: SO against the counterparty's `acceptance`, creating an edge with `Debt` terms.
   `12 §4.2` hands *"proposal, counter-terms, acceptance"* back to *"a `05`/`06` faction-action module's
   job … out of this document's scope"* — and `05` ships no counter-terms and no clause-selection. **The
   counterparty exists only as an obstacle number**; where the clauses come from is unanswered on both
   pages. Canon already owns a negotiated-commitment object with parties, commitment, duration and
   violation trigger — the Obligation clock (`clock_registry_v30.md:89`) — which the suite neither reads
   nor reconciles. — **structural omission**
7. **[GAP] The "clocks" half of T7 is mostly re-derived, not read.** Of the ratified clock roster the
   suite consumes **two** rows as mechanism — Truth and TS; it re-homes Institutional Pressure as a
   proposed new place gauge rather than reading the clock, flags Turmoil as vacuous, and never touches MS,
   CI, the Persuasion Track or Obligation. Clock/gauge band crossings **do** reach the player as
   informational candidates — but they **cannot become motion subjects**, because a subject must be a
   *tag* and a band crossing is a Key. — **omission**
8. **[UPHELD] The event→motion content chain is real and traceable on disk** — `we.route_severed` →
   graded `Precedent` → tag on a real owner → legal subject including edge-owned tags, with provenance
   required at every link. **This survives attack.**
9. **[NIT] `Precedent` does two jobs and one leaks into the chamber:** `11` uses `Precedent` tags as
   cooldown plumbing (`key: "we_cooldown:<event>:<target>"`). Any tag is a legal motion subject, so **an
   engine timer is a debatable matter of state.** — **structural, small** *(the same over-loading T5
   finding 5 reaches from the other side)*

---

# T8 — The world always churns; the player is not necessary

**Verdict: PARTIAL.** Executable today only as the pre-existing strategic loop; every mechanism the
suite adds is DOC-class; the scoring instrument has a verified dead leg.

## T8 steelman

Most of this is structural rather than aspirational. Fork A is already ruled, so headless resolution is
the same engine at a different fidelity, not a cheap path. **The Slate subtracts and cannot inject** —
not by rule but by construction: `state: []` in all four `sl.*` modules, no resolver, no dispatch, and
its one write channel was found breaching that and **cut**. P-A/P-B/P-C are carried by three named
mechanisms, and the per-candidate RNG substream closes a leak — shared-stream re-rolling — **that no
playtest would ever find**. `09` gives the world intentions that cost nothing to obstruct: advance is a
read of world state, so any actor moving a term obstructs a project it never heard of. `11` gives the
world an outside. J-N is honestly inventoried and designed *around*. The funnel commits to the strongest
form: ~195 candidates a season, ~3% surfaced, **100% resolved at full fidelity**. And `13` refuses to
count any of it as done: *"Nothing in this suite has moved a single byte of executable behaviour."*

## T8 findings

1. **[BLOCKER → downgraded on verification] The suite's emission arithmetic breaks the substrate's cap,
   and the document assigned to reconcile it is silent.** `11 §3.3` bounds only its own slice and passes
   the tick-wide sum to `13`; **`13` contains no occurrence of "64" or "emission".** The arithmetic:
   directives at 1/place/season × 37 places ≈ 37–74 emissions, plus ~25 project emissions, ~20 faction,
   ~5 vacancies, ≤5 events, ~3 transitions, ≤9 slate. Any two large rows exceed
   `DEFAULT_EMISSIONS_PER_TICK_MAX = 64`, and the cap **raises `TerminationBreach`** (`keys.py:561-565`)
   — Phase 6 as ordered can produce a world that crashes instead of churns. **Severity corrected by the
   synthesising session — see [05](05_independent_verification.md):** the cap is live by default but the
   tree emits 164–229 Keys per *campaign* today (~13× headroom), and the constant is explicitly
   caller-supplied and tunable. **Carried as an unowned Phase-0 reconciliation item, not an architecture
   blocker.** — **structural/omission**
2. **[DEFECT] P0-7 verified, and sharpened three ways.** (a) `engine/` never writes *any* clock; CI and
   MS move only via `ci_track.py:177` and `ms_track.py:69,90`, while IP is self-declared unread and
   PI/Strain also have zero writers. (b) One of the registry's two `build: live` modules **is `victory`
   itself** — so "live: 2 of 27" counts a module with a vacuous leg as fully live. (c) An A/B campaign
   control is only as good as its shared instrument when the treatment doesn't move the dead leg — **and
   a churn programme is precisely the treatment that would move political stability.** Every "unmeasured"
   loop naming `balance_oracle.py` will be scored on a two-legged gate until P0-7 closes. — **structural**
3. **[UPHELD, with a wording NIT] `13 §1`'s "live: 2 of 27" reproduces** — exactly two module rows carry
   `build: live` of 27. But `13:27` cites `wiring_map_check --summary`, **a tool retired in plan S5c**;
   the instrument is now `tools/build_contract_index.py:653`. `13 §2` demands *"re-verify every engine
   claim before citing"* — and then cites a retired instrument for its own headline measurement. — **wording**
4. **[UPHELD] J-N's engine facts are all true on disk:** `drain_tick` has zero production callers,
   `next_tick` raises on a non-empty queue, `DEFAULT_CASCADE_DEPTH_MAX = 0`. **The substrate genuinely
   has no cross-season transport.**
5. **[DEFECT — the finding the authors would dispute] The Key log is a cross-season transport in all but
   name, and J-N's guarantee is discipline, not structure.** `10 part2 §7` derives inertia from the
   accounting index of *last season's* `slate.item_surfaced` Keys — an emission carried forward and
   reacted to a season later, which is the shape the J-N table forbids. The authors would answer that
   reading the log is a boundary read of state, the ruled telemetry posture, and `sl.*` emits nothing
   pressure-bearing. **But nothing bounds *which* modules may derive from the log or *how far back*** — so
   the moment a second module copies the pattern for a reactive purpose, J-N is bypassed wholesale with no
   cap and no test. A registry-declared log-derivation allowlist, shrink-only like `PATH_SEAM_ALLOWED`, is
   the missing guard, and it passes §0.1 pt 5's predicate. — **structural**
6. **[GAP] No document enumerates what J-N forecloses.** Anything whose trace decays before reaction can
   never cause a late reaction — and the suite's own P0-9 (a legitimacy gauge seeded once that *"relaxes
   to rest and dies"*) is an instance arising **inside the suite**. Delayed reprisal, slow-travelling news,
   sleeper consequences: all impossible unless laundered through a durable Tag. `09` and `11` verified
   they need no latency — but **per-module verification does not aggregate to "the game loses no
   stories,"** and no page carries that argument. — **omission**
7. **[GAP, upheld honesty] Obstruction is unfalsifiable in both directions:** *"cannot be run yet — there
   are no rows"*, its own weakest claim, and the acyclicity check *"does not exist"*. The mechanism is
   genuinely verb-free but **content-contingent**: a registry whose kinds read state nobody else moves
   passes every structural falsifier and ships timers. In the executable tree churn *is* coupled through
   conquest/territory but **not through wealth** — verified: `faction_action.py:544-549`, `pool = Mil +
   floor(W/2)`, so a `W=0` faction musters on `Mil` alone. `13 §2`'s *"Wealth gates nothing"* is exactly
   right, including its correction of the audit's stale 0.5-floor claim. — **structural**
8. **[DEFECT] Claimed vs executing: the suite's contribution is 0%.** All thirteen documents are
   DOC-class and the falsifier holds — zero executable lines on the branch. What executes headless today
   is the pre-suite loop only: `mc_v18.py:124-217` (faction actions, contest dispatch, parliamentary vote)
   plus `accounting.py:96-120` (CI, MS, insurgency emergence and promotion — **which creates factions** —
   NPE stance drift). No NPC generation, no knots, no combat scenes ever queued. **T8 is true today at one
   scale only, and the funnel's "100% resolves" describes a world of which roughly six subsystems do not
   yet exist.** — **structural**
9. **[NIT] `10 §1.3`'s headline figures are six stacked shape assumptions, and the document says so with
   unusual candour** — *"a genuinely less trustworthy number than the one it replaces"*. The risk is
   downstream copying: the exact path the retracted 87% figure took through five documents. — **wording**

---

# T9 — Field investigations (cross-cutting, explicitly required)

**Verdict: PARTIAL.** Genuinely load-bearing in exactly one document, whose reverse direction is
specified against a deleted gauge, a Key type it wrongly declares missing, and an FI substrate of typed
no-ops.

## T9 steelman

Better than v1 had any right to be. `08 §6` is a genuine two-direction coupling: infrastructure opens an
investigation surface (`08:291-311` — rows that open only when a facility exists **and** a matching
unresolved tag is on the ledger, the same conditioned discipline as world events), and a resolved Finding
writes back **through the four declared write leaves only** (`08:335-364`), with an explicit falsifier
refusing any second write path. `07 §4.2` makes every built facility a named, typed, citable
investigation target with its own provenance and disclosure. `01 §3.1` adopts the ruled FI epistemic
layer as the `Holding` — the one object whose subject may be false — giving a Finding somewhere to land
as **belief** rather than as a stat delta. `10 §3.1`'s `witness_key`/`document_key` channels make
misperception, not world-state, what reaches the player. The Knot canon is cited line by line and never
restated, with its open items named rather than filled. The reliability discount reuses FI's own tags
instead of a second scoring system. **Where v1 had settlements and investigations mutually unaware, v2
names the seam, keeps both owners, and ships only wiring.**

## T9 findings

1. **[BLOCKER] The witness write-back deposits into a deleted gauge** (**X-1**), reached independently a
   third time. Additionally: per-witness `credence.<proposition>` is **exactly the shape `01 §3.2`
   rejects on its own arithmetic** — *"one gauge per proposition per person — the count grows with
   everything anyone was ever told"*. The correct target, `Holding.confidence` via a
   `state.proposition_revised` deposit, is owned by `npc_memory`, which is PROPOSED and unbuilt — **so
   the fix has no built depositor either.** — **structural**
2. **[DEFECT] `08 §6.3`'s "no such key type exists" is wrong in the direction the suite itself warns
   about.** `scene.investigation_resolved` — *"Investigation, inquiry, or trial concluded"*, payload
   `finding`, optional `witnesses` — is **registered** (`key_type_registry_v30.md:881-897`) and carried in
   live contracts (`module_contracts.yaml:229,304,628`). Meanwhile `sm.business` consumes an invented
   second id, `investigation.resolved` (`08:416`). **`00 §9.2`'s own correction box mandates checking the
   ratified registry before declaring a type missing, having caught the identical error on project keys.**
   The registered type lacks a settlement anchor and reliability field, so extension-vs-mint is a real
   question — but the honest status is *"check `:881`"*, not *"no such key exists"*. — **structural**
3. **[DEFECT] Two objects named Exposure** (**X-4**). `08` uses **both senses in one document** — its own
   gauge at `08:174-175,454`, canon's by name at `08:324-325` — and `01:763` admits the suite's `exposure`
   has no declared scale, so three declaration-time guards are inert on it too. — **structural/wording**
4. **[DEFECT] The forward direction delegates to a mechanism that does not exist.** *"All of the actual
   investigation … is canon's"* — but the FI resolver is **six typed no-ops** design-gated on ED-916
   (`fieldwork.py:38-59`, `investigation.py:30-51`); `fieldwork`/`investigation` have no
   `module_contracts.yaml` entry; and even `knots.py`, the "only live module", has **zero production
   callers** — `mc_v18.py:204-205` records a `stub_resolve` under the literal name
   `'form_knot(world-gen|season-tick)'`, which **sharpens** PR #337's claim. Canon's investigation text is
   **GM-mediated in a no-GM game**: *"The GM sets the threshold"*, *"GM may offer a misleading clue"*,
   *"The GM introduces a complication"*. **Authorize opens a case nothing can conduct**: no module, no post
   kind, no headless runner is named for the investigation itself. — **structural**
5. **[GAP] Coverage, counted.** Across 18 files, `systems/fieldwork/` engagement reduces to: the `08 §6`
   coupling plus its `07` far end; Knot canon (a *relationship* mechanic, not investigation); one ruling
   quote in `09`; one absence note in `13`. **`05` builds a parallel intelligence channel** —
   `act.inquire`'s `information` gauge — with no evidence type, no reliability, no proposition: **faction
   intel that structurally cannot be false**, in a suite whose `10 §3.2` centrepiece is misperception, and
   despite canon already routing Surveil's Observational evidence to *"Intelligence (faction action)"*.
   And **`13`'s build order contains zero rows for the `08 §6` coupling** — its only FI row is the
   descriptor fix. The coupling composes on fieldwork in one document and is orphaned from the plan that
   builds things. — **omission**
6. **[DEFECT] `07 §4.2` records a covert presence's discovery as a `Memory`/`Precedent` tag** — `Memory`
   was cut by O-6, and a discovered-but-possibly-wrong claim is precisely a `Holding`. Same document,
   `07:392`: the citation into fieldwork's Depth axis is a literal unresolved placeholder,
   *"`fieldwork_v30 §…`"*. — **wording/staleness**
7. **[DEFECT] `02 part 2`'s falsifier contradicts its own page:** it asserts zero `bucket: gauge` rows
   owned by any `cg.*` module (`02 part2:214-218`), while `cg.attach` declares `thread_sensitivity` and
   `truth` with `bucket: gauge, owner: cg.attach` twenty lines up (`:156-157`) — also violating the
   write-leaf ownership convention (`owner: substrate.gauge`) that `08:354-356` demands. **The falsifier as
   written fails against the document that ships it.** — **wording**
8. **[NIT] Upheld on verification:** `prac.thread_sensitivity` is `floor 0, ceiling: null` with a
   non-binding `open_ceiling_reference: 100`, exactly as `01:762` records. Also `08:361-364`'s example
   slightly misreads canon: Unverified/Rumour is *not admissible* and directional only, and a Finding's
   reliability is its **strongest** constituent tag — the discount exists, but that Finding can't. — **wording**
9. **[The finding the authors would dispute] Authorize/Suppress giving the deepest system in canon zero
   dedicated verbs is an amputation as currently written, not a distillation.** The authors would answer
   with `00 §2.3` point 5 (investigation removed from the player's hands still changes the game, ergo
   substrate) and the implicit precedent that combat's scene-internal verbs aren't counted either. **That
   defence works for combat because combat has a running engine and a ratified module path; it fails here
   because the substrate being distilled onto does not execute** (finding 4), so the distillation reduces
   to a reference. And canon's own design makes investigation choice-rich in a way substrate erases — the
   sensitive/non-sensitive team asymmetry **is** Jordan's "robust choosing" clause. **The suite never
   states whether the personal-scale scene game exists below the strategic layer or is exempt from the
   budget; that unmarked boundary, not the two verbs, is the defect.** — **structural/omission**
