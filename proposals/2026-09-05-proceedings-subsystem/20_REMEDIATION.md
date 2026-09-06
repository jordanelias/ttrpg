# 20 · THE REMEDIATION SUITE — eleven proposals, ordered by what makes the thing run

## Status: **PROPOSED (2026-09-06). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Planner: `fable`, read-only. Written up and independently verified here. Continues in `20_REMEDIATION_part2.md`.
## Scope: every issue this directory has identified about itself, plus seven it had not.

---

> # THE ONE PARAGRAPH
>
> **This directory is a specification with an execution-artifact count of zero, and the shortest
> path off zero is one pull request touching four files.** Two roster values, one registry row, one
> dispatch table, one provider module and one test. **No verb-table edit and no ruling.** Everything
> after that first PR is what turns a running thing into a game: a verb with a body, a bench that
> exists, a telling that lands in somebody's ledger, and a room that remembers you.
>
> ⛔ **THE PRIMITIVE COUNT IS NOT ZERO, AND A DRAFT OF THIS PARAGRAPH SAID IT WAS.** It banked *"ten
> of eleven spend ZERO primitives; the eleventh spends one verb-table column."* **The adversarial
> pass found four more:** three **undeclared carrier cells** on `Date` — `holder`, `matter`,
> `arrangement` — written from inside effect bodies, which **evades** the loader's write-class gate
> (`shape.py:1616-1621`) rather than satisfying it, and one **hardcoded grammar kind** in a branch
> the tracer deliberately keeps data-derived. **The true count is one column, three cells and one
> literal**, and the three cells must be declared as Part D rows before they are written.
>
> ✅ **THE PASS REJECTED FIVE OF THE ELEVEN — `P1`, `P2`, `P3`, `P6`, `P7` — AND ALL FIVE ARE NOW
> FIXED.** Their *mechanisms* had survived; their artifacts, breakage lists and several supporting
> claims had not. **Three of the fixes made the suite better rather than merely correct:** `P1`'s
> capability rule became *zero-and-floor*, which is the engine's own rule instead of a refusal;
> `P2` revives **`carry`**, a `grade: ruled` row missing only an effect, which makes the docket road
> a chain of person-acts end to end; and `P3` takes back the **third parameter** it had dropped,
> withdrawing an argument that would have re-admitted a defect this design had already deleted.
> Every defect and its fix are inline at the site, marked ⛔ then ⭐.
>
> ⭐ **The plan still gets SHORTER, not longer, at two places, and the pass did not dislodge it.**
> `Tenure.term` — the one new field in the whole design — **is not built at all**: the carrier
> exists, matures citing the act that wound it, and is already tested (`P7`). ⚠ **Its evidence chain
> named the wrong producer and is corrected** — `create_record`, not the inert `open_case` — but the
> conclusion stands. And `P-04`, `P-03` and half of `P-05` close from the tree rather than from
> work.

---

# PART A · THE CORRECTED STARTING POINT

**The state-of-affairs readout this suite was built from is `19_PLAN.md`'s successor and it was
wrong in three places.** They are corrected first, because a suite built on a false baseline
remediates the wrong things — and two of the three made the tree sound *further* from running than
it is.

## A.1 · What was verified, and what it cost to verify

Every claim in `PART B` was checked against the working tree at `da834ae` by **three** readers — the
planner; this document's author, re-reading nine load-bearing citations line-by-line before writing
them down; and **a read-only adversarial pass that received this document's OUTPUT and not its
reasoning.** ⚠ **The third reader broke five of the eleven proposals**, which is the argument for
structural independence over a careful self-review: *the author's nine re-reads all held, and every
one of them was a claim the author had chosen to check.* **The nine that were re-read, and held:** the dispatch
literal and its two refusal sites (`shape.py:6740`, `:6757-6765`, `:6766`); `degree_of`'s
never-fed margin branch (`:6668-6679`); the deposit-mode default (`:1847`); `judging_set`'s
unconditional raise (`:3161-3163`); `resolvable_verbs`' third gate and its stated ground
(`:3352-3375`); `_parties` (`:6135-6136`); `contest()`'s `extension` parameter (`:6692`);
`combat_seam.resolve`'s signature (`combat_seam.py:125`); and MATTER's term maturation
(`:5424-5444`).

⚠ **Two absences were confirmed by search rather than by reading, which is the weaker method and is
said so:** there is no writer of a Date's `holder` anywhere in the tracer, and **there is no
`arrangements.yaml` anywhere in the repository.**

## A.2 · ⛔ THE THREE CORRECTIONS, and two of them make the position better

### **1 · *"Every call site in the tree still passes a hand-set Ob"* — RETRACTED IN THE TREE ON 2026-09-05, AND THIS DIRECTORY REPEATED IT ANYWAY.**

`engine/autoload/dice_engine.py:244-252` carries the correction verbatim, under `ED-IN-0202`:

> *"⚠ CORRECTED 2026-09-05 (ED-IN-0202) — this read 'THAT DERIVATION IS IMPLEMENTED NOWHERE — every
> call site in the tree still passes a hand-set Ob', and the second clause is FALSE. Measured:
> `crown_initiative.py::coronation_renewal_ob` implements `floor(Church.L / 2) + 1` exactly, Royal
> Progress derives its Ob from the standing gap, and the tribunal derives under formal grounds."*

**`06_RESOLUTION.md:796-799` still carries the retracted sentence**, and the state-of-affairs
readout lifted it from there. **The true claim is narrower and is the one to work from:** there is
**no single-owner derivation**; most sites still hand-set; the three opposed sites disagree; and
`parliamentary_transfer`'s `L+2` contradicts the ruling while being stated as canon. **Reconciling
them is a systems ruling, SUSPENDED by Jordan (2026-08-21)** — so `P1` derives its obstacle *inside
the seam*, edits no opposed site, and does not touch the suspension.

### **2 · *"P-05's mechanism is `observation_deposit_modes` / `H-122`, open"* — H-122 IS BUILT, DEFAULTED AND EXECUTING.**

`shape.py:1847` sets `observation_deposit_mode="actor"` as the shipped default, swept
`none / actor / total`, with `none` declared as the control. The deposit runs at `:6287-6423`.

**So `P-05` is not one gap, it is two, and only one of them is open:**

| | state |
|---|---|
| an act's **READS** reaching the actor's ledger | ✅ **built and running since 2026-09-04.** This is the half `FI`'s six acts need, and it is probably already served for them once their rows are typed |
| a telling's **PRODUCT** reaching the *hearers'* ledgers | ⛔ **genuinely open**, and `P4` is the only proposal in this suite that spends a primitive on it |

⚠ **And the reason it is open is a good one, not an oversight.** `tell`'s only declared read is
`claim.held` (`verb_table.yaml:479-481`), and `LEDGER_DERIVED_STEMS` (`shape.py:1284`) excludes
derived-namespace reads from deposit at `:6407` — **because a deposit that reports what the ledger
holds would falsify itself.** The exclusion is correct. `P4` therefore does not widen the deposit
mode; it rides a different carrier at the same barrier.

### **3 · *"Three Event kinds are body literals, so the loop as built cannot run under the loader as specified"* — STALE, OVERSTATED, AND A DIFFERENT THREE.**

`contest.resolved` was removed on 2026-09-04 (`shape.py:6175-6181`). What the fold emits as
literals today is `act.ineligible` (`:5866`), `act.refused` (`:5913`, `:5975`) and — **never counted
by the finding that named three** — `attempt.refused` (`:6101`). *The count is three again by
coincidence; the membership is different.*

⛔ **And the consequence clause is false. Loader invariant 7 does not exist in the tracer**, so
"cannot run under the loader as specified" describes a loader nobody has built. **The loop runs**:
184 tests, `test_tracer_is_honest.py`. `P9` closes the row honestly and is ranked near the bottom
for exactly that reason.

## A.3 · ⭐ SEVEN DEFECTS NOBODY HAD REGISTERED, four of them on the critical path

These are the planner's own finds. **None was in `10_LOOPS_AND_GAPS.md`, in `19_PLAN.md`'s weak
joints, or in the state-of-affairs readout** — which is the argument for having run an independent
pass at all.

| | the defect | why it matters |
|---|---|---|
| ⭐ **1** | **`speak`'s own precondition cannot be evaluated.** `04_VERBS.md:70-73` types it `{form: existence, of: subject, kind: DocketItem}`; `WorldReader.read`'s `exists` branch (`shape.py:1155-1164`) resolves a kind against `_STATE_COLLECTIONS` (`:2988-2989`), which has no docket — `w.docket` is a `_STATE_SEQUENCES` list of dicts (`:2993`). **Verdict UNKNOWN → refusal, every time.** The design's headline verb refuses unconditionally as drafted | **on the critical path.** `P2` fixes it with one branch |
| ⭐ **2** | **No convened date ever forms a docket item, because nothing writes a Date's `holder`.** `_eff_convene` (`:5029-5046`) does not set it; CALENDAR's firing path reads it (`:3888`, `:5371`); every convened date is therefore vacant, fires and lapses | **on the critical path.** The road from `convene` to a hearing is closed and no register row says so |
| ⭐ **3** | **`resolvable_verbs()`'s third gate excludes every contested verb** (`:3352-3375`), so an NPC is never offered a `speak` that contests. **The "zero authored acts" bar is unreachable by construction**, for any verb this subsystem cares about | **on the critical path.** It is the gate between a specification and `R`'s no-player half |
| ⭐ **4** | **`resolve()` hands the seam a non-person claimant.** `_parties = [a.actor] + [payload["subject"]]` (`:6135-6136`) — for a `speak` the subject is a **Proposition id**, and the seam's own law text says claimants are persons (`:6703`) | **on the critical path**, and a one-line fix |
| **5** | **`contest()`'s `extension` parameter is dead** (`:6692`; the only other occurrence in the file is unrelated, `:4096`) and `degree_of` passes no extension (`:6679`) — **so the "one BandExtension" veto has no path to the ladder** | `P6`. It also means `09_IMPOSSIBILITIES.md` row 5's *"veto : bool, and the ladder takes the minimum"* has no executable spelling |
| **6** | **`_fold` emits EVERY kind in `emits_on_refusal`** (`:5857-5861`, `:5913`), so `04_VERBS.md:305`'s two-kind refusal would publish both on every refusal | `P2`. A design decision made by a loop nobody read |
| ⭐⭐ **7** | **EIGHT of the "reused unchanged" verbs cannot execute.** The `@effect_for` roster is exactly ten — `confer · revoke · convene · move · work · create_record · destroy_record · kill/wound · utter · transfer` — and every one of the eight has a non-empty `writes`, so each raises `Unspecified` at `:5942-5949` on its first fold: **`commit`, `repudiate`, `oblige`, `open_case`, `petition`, `carry`, `issue`, `forge`** | ⚠ **Not on the critical path, and worse than the ones that are.** `04_VERBS.md:34-40` banks *"everything else is reused unchanged"* as the design's economy argument. **More than half of what it reuses is inert** |

> ### ⚠ **FIND 7 IS THE ONE TO SIT WITH, AND IT IS NOT FIXED BY THIS SUITE.**
> The zero-new-verbs claim is true and remains true. **What it does not say, and what a reader takes
> from it, are different things:** *reused* has been doing the work of *works*. **The honest form of
> the economy claim is: this design adds no verb, and inherits EIGHT that do not yet run.**
> `04_VERBS.md` should say that.
>
> ⛔ **THE MEMBERSHIP ABOVE IS THE ADVERSARIAL PASS'S, AND IT CORRECTED THIS FINDING IN BOTH
> DIRECTIONS.** A draft said *seven*, and got the list wrong twice: it counted **`determine`**,
> which is **not** a reused verb — `04_VERBS.md:29` lists it among the four this design *touches*,
> so counting it inflated the indictment with a verb the economy claim never made — and it **missed
> `issue` and `forge`**, which are on the reuse list (`04_VERBS.md:38-40`) and are inert
> (`verb_table.yaml:233`, `:244`). ⭐ **The finding is worse than first stated, and was stated
> against the wrong list** — which is the shape of error that survives an author's own re-read and
> does not survive an independent one.
>
> ⚠ **AND ONE ALTERNATIVE READING WAS TESTED AND FAILS.** `resolvable_verbs`' own predicate is
> `effected = not row.writes or v in EFFECTS` (`shape.py:3362`) — so a verb with an EMPTY `writes`
> legitimately needs no effect. **All eight have non-empty `writes`.** None is saved by that clause.

---

# PART B · THE SUITE

**Eleven proposals.** Each carries a mechanism with verified line numbers, an **execution
artifact** — §0.2's bar, without which a proposal is prose — a primitive count, a NERS score run
with `E` last as a ratio, and its honest failure surface.

---

## P1 · ⭐⭐ FIRST PRODUCER — the provider, dispatch by row, and the prize repoint

> **This is the whole of the shortest path. Everything else in the suite depends on it or is
> independent of it; nothing precedes it.**

**Statement.** Land the provider module beside `combat_seam.py`, replace the `personal_combat`
literal with a string-keyed table, and route the two social prizes to it — so a `speak` carrying
`contests=["a proposition"]` produces a `net`/`ob` pair, **the one ladder's margin branch runs for
the first time**, and the Event carries a degree.

**Closes.** `H-31`'s reader-with-no-producer (`shape.py:6553-6561`); **`ED-SC-0033` (1) and (2)** —
ruled 2026-09-06 and unexecuted; `12_BUILD_ORDER.md` steps 0 and 8; `19_PLAN.md` steps 8, 9, 12(b)
and 12(e). Partially `P-06`: the keys and magnitudes become injected fixtures with declared sweeps,
which is `ID-6`'s *inject, declare, sweep* rather than a ruling request.

### The mechanism

**1 · The prize rows, and NOT a new prize name.** `rosters.yaml:441-445` already carries
`"a standing": "social_contest"` and `"a proposition": "social_contest"`. Repoint both to
`proceedings`.

> ⭐ **A draft of this design coined `"a matter"` as a third prize. It is retired here, on three
> grounds that agree:** the matter **is** a Proposition (`00_DERIVATION.md:40`); `ED-SC-0033` (2)
> says *the two prize rows repoint*, which presumes the two that exist; and `CLAUDE.md` §4 says
> coin nothing a plain word already covers. **A new prize row would also have been a new primitive
> in a design whose entire defence is that it adds none.**

**2 · The contracts row.** `references/module_contracts.yaml` gains a `proceedings` entry with
`module`, `sim_module` and `resolver`. **This is not optional bookkeeping:** `contest_subsystem()`
raises when the prize roster names a module the contracts file lacks (`shape.py:6524-6528`), so the
row is what makes step 1 loadable.

**3 · Dispatch by table.** `shape.py:6740` reads:

```python
if _sub["module"] == "personal_combat":
    import combat_seam
    out = combat_seam.resolve(w, claimants, causes, prize)
```

Replace with a module-level `PROVIDERS = {"personal_combat": "combat_seam", "proceedings":
"proceedings_seam"}`, resolved by `importlib` at first use — **the same deferred-by-name discipline
`combat_seam.engine()` already uses** (`combat_seam.py:78-101`), not a new pattern. The refusal at
`:6757-6765` survives untouched for any module not in the table, so `mass_battle` still gets its
honest named refusal.

> **Why this is the architecture's own instruction and not a preference.** `02_THE_SOCKET.md`
> §2.1 registers the literal as the defect; `02_HIERARCHIES.md` §D.4 says *the engine names the
> ROLE, the registry names the MODULE, resolution happens by string*; and `G.2.6` says *resolution
> is a row — never an import, never an inference.* **A second `if` would have been the 114-line
> regex router's descendant.**

**4 · `proceedings_seam.py`**, mirroring `combat_seam.resolve(w, claimants, causes, prize) -> dict`
(`combat_seam.py:125`) exactly:

```
speaker  = claimants[0]                     -- and IGNORE every other claimant in v1 (breakage 2)
matter   = the act's subject as a Proposition id, off w.propositions
           absent -> status="MATTER-GAP"    -- ID-5 polarity; combat_seam.py:140 is the precedent

brought  = brought_per_claim × |{c ∈ speaker.ledger : c.subject == matter.subject}| × composure
conduct  = eloquence × latitude             -- latitude = 1.0 until P6; floored by fixture
pool     = max(1.0, brought + conduct)      -- the 1D floor, mean as well as variance

           the three keys are read off Person.capability (shape.py:2368).
           ⭐ A MISSING KEY CONTRIBUTES ZERO AND THE 1D FLOOR CATCHES IT.
           There is NO CapabilityGap and no refusal -- see THE FIX below.

resister = a person holding a live `commit` to a Proposition with the matter's
           (subject, predicate) and a DIFFERENT value          (Proposition, shape.py:2425-2434)
base_ob  = resister.composure / 2, or ABSENT where nobody resists
           swept {max · first · absent}                        (06_RESOLUTION.md §C.1.2)

ob       = max(1.0, base_ob + rung + proofs_told + aptness)
           the three room terms are 0.0 in v1 WITH FIXTURE SLOTS DECLARED, so the
           composition function is the single owner from day one   (06_RESOLUTION.md:669-697)

seed     = int(H(w.world_seed, w.tick, speaker, f"contest:{prize}:{causes[0]}"), 16)
net      = continuous_engine_sample(pool, rng=random.Random(seed))
           NEVER roll_pool — dice_engine.py:202 is `effective_pool = max(1, pool_size)`;
           there is NO rounding, and a float pool raises TypeError at range().
           (A draft said ":196 keeps int(round(pool))" -- wrong line, wrong reason,
            right conclusion. Corrected by the adversarial pass.)

return   dict(status="RESOLVED", module="proceedings", resolver="continuous",
              net=net, ob=ob, pool=pool, seed=seed, parties=...)
```

`degree_of` then takes its `"net" in result and "ob" in result` branch (`shape.py:6668`) — **the
branch that has existed since the ladder was imported and has never once been entered.**

> ⭐ **THE ZERO-VALUED ROOM TERMS ARE THE DESIGN DECISION HERE, AND THEY ARE NOT A STUB.** Writing
> `ob = max(1.0, base_ob + rung + proofs_told + aptness)` with three terms at `0.0` makes
> `obstacle()` **the single owner of the composition on the day it is born**. `P5` and `P6` then
> supply values into slots that already exist. The alternative — add terms as they are derived —
> produces two composition sites, which is the defect `06_RESOLUTION.md` §C.1 exists to prevent.

**5 · Fixtures.** `brought_per_claim`, `latitude_floor`, `resister_rule` join `DEFAULT_FIXTURES`
(`shape.py:1740-1860`), each with a three-point sweep and a hole-register row — `H-87`'s exact
shape, and `ID-6` discharged rather than escalated.

⛔ **6 · M-7 AND M-8 GATE THIS, AND A DRAFT OF THIS SUITE NEVER MENTIONED THEM.**
`registers/handoffs/HANDOFF_SC.md:82` is unambiguous: *"**M-7 and M-8 gate the composed obstacle**
and are blocking, not advisory"* — they are Jordan's 2026-09-06 ruling that a player is not deprived
of a chance at winning and that a brilliant speaker is still rewarded, turned into measurements.
**`P1` ships the composed obstacle.** ⚠ **And shipping it with `latitude` pinned at `1.0` until
`P6` makes M-7 and M-8 UNRUNNABLE — both arms identical by construction**, which is the fake-control
shape `CLAUDE.md` §7 flags through `ED-MB-0066`. **So `latitude` must be a swept fixture from `P1`,
not a constant**, even though nothing varies it until `P6`.

> ### ⭐ **THE FIX.** `latitude_floor` is swept `{0.4 · 0.7 · 1.0}` from `P1`'s first commit —
> `0.7` being the ~70% retention the evidence gave and Jordan ruled to
> (`registers/handoffs/HANDOFF_SC.md:70`). **M-7 and M-8 then have two genuinely different arms on
> day one**, and the blocking measurement is runnable before the composed obstacle acquires a
> second term. **A fixture pinned to a constant is a sweep with one arm, which is not a control.**

### ⭐ Execution artifact

`test_pr_the_margin_branch_has_its_first_producer`, in `test_tracer_is_honest.py`, modelled on the
`_we_bands` tests (`:7143-7169`):

- `tiny_world()` (`probes.py:57`); set `capability` on `p_low` and `p_mid`; plant an uttered
  Proposition and a countering `commit` for `p_mid`.
- `d.resolve([Act(id, "p_low", "speak", contests=["a proposition"], payload={"subject": prop})], 2)`
  across 24 act ids.
- **Assert every Event's `degree` is in `DEGREE_LABEL.values()`** (`dice_engine.py:36-41`), and
  `assert set(seen) == {Overwhelming, Success, Partial, Failure}` — ⭐ **assert that it asserted**
  (§0.1 point 2, the rule that surfaced the born-broken-subunit bug).
- Two runs at one seed give one `w.content_hash()` (`shape.py:2995-3036`, which folds `e.degree`).

**Falsifier** (§0.1 point 3 — name it or you have not attacked the result): monkeypatch
`degree_from_net` to a constant and every band collapses to one. The precedent is
`test_we_the_ladder_is_the_trees_own` (`:7295`).

**Control:** the same act with `contests=[]` still emits `speech.made` with `degree=None` — the
existing assertion at `:7262-7265`, unchanged.

⛔ **CORRECTED BY THE ADVERSARIAL PASS — THIS NAMED THE WRONG REFUSAL, FIVE TIMES.** A draft said
*"Red today at `shape.py:6766` — `Unspecified: the degree ladder's margin model`."* **`:6766` is
unreachable for these prizes.** It sits outside the `if _sub is not None:` block opened at `:6734`,
so it fires only for a prize on **no** roster row — and `"a proposition"` has one (`rosters.yaml:445`).

**The real red is `shape.py:6757-6765`:** *"a contest for 'a proposition' belongs to the
`social_contest` subsystem (resolver: dice_pool), and nothing connects the seam to it."*

⭐ **And the correction changes the finding's meaning, not just its address.** The current failure is
a **dispatch gap the tree already names by subsystem** — not the unspecified-margin gap this
proposal was framed around. *The seam knows exactly who should answer and has no way to call
them.* **Green after, with a degree on the Event and a stable hash** — that transition is the
execution-artifact count going from zero to one.

### Primitive count

**0 verbs · 0 carriers · 0 edge kinds · 0 fields.** One roster value changed twice, one registry
row, one provider module, one dispatch table, three fixtures. `Act.contests` is an existing field
(`shape.py:2340`), so **no verb-table row is touched** — which is why this proposal needs no ruling
and no lane negotiation.

### NERS

**N — tested from three directions, and it narrows in one.** *Bottom-up:* without it `determine` is
dead, `speak` is a log line, and the seam names two prizes it cannot call (`:6765`). *Top-down:* the
strategic layer runs without it — ⚠ **narrowed, and `11_NERS.md:27` already says so.** *Lateral:* it
removes the one `if` the architecture registers as a defect, so **combat gets cleaner too**, which
is an N-line pointing away from this subsystem.

**R — the half with no player in it FAILS here, and that is stated rather than hidden.** NPC-driven
`speak` cannot reach the seam at all, because `resolvable_verbs`' third gate excludes contested
verbs (find 3). **This proposal alone does not give the world drama; `P2` does.** *Completeness:*
the obstacle is fully computable from a decision in v1, so the flowchart solver
(`15_WHY_IT_IS_A_GAME.md:15-31`) is intact until `P5`. **Both halves of R are honestly short, and
`P1` is still ranked first, because nothing else can run until it does.**

**S** — one ladder, one seam, one log. *Pauses correctly* is untouched: the seam already nests with
a caller-supplied cap (`:6722-6726`). *Calculations consistent in methodology*: the provider mirrors
`combat_seam`'s discipline line for line — same signature, same seed construction, same
gap-returning refusal.

**E, scored LAST and as a ratio against what N and R found** — near-zero overhead against a real N
gain and a *partial* R gain. **Amputation fails the test explicitly:** cutting anything here cuts
the producer, which is the thing being bought.

### What it breaks — and the adversarial pass found three the first draft missed

⛔ **THREE CURRENTLY-GREEN ASSERTIONS GO RED, ALL IN ONE TEST**, and a draft of this section named
none of them. `test_we_only_a_verb_that_declares_contests_can_be_graded_today`
(`test_tracer_is_honest.py:7346-7394`):

| the assertion | what breaks it |
|---|---|
| `:7376-7380` — `pytest.raises(Unspecified)` per prize, then `assert set(refused) == {"a field", "a proposition", "a standing"}` | **`P1` step 1.** Two of those three now resolve instead of raising |
| ⭐⭐ `:7384-7394` — a scan over `HERE.glob("*.py")` for `\bnet\b\s*=\|roll_pool\|\bsuccesses\b`, asserting `not producers` | **`P1` step 4 lands `proceedings_seam.py` IN THAT DIRECTORY computing `net = continuous_engine_sample(...)`. Red by construction** |
| `:7362-7366` — `assert contested == {"kill / wound": "the body"}` | **`P2`**, when `speak` gains `contests:` |

> ### ⭐ **THE SECOND ONE IS A DESIGNED TRIPWIRE AND MUST BE TREATED AS ONE.**
> Its own failure message reads: *"something now produces a margin. `W-E` published `the ladder
> branch has no producer` and recorded it on `H-98`; **that sentence is now false and must be
> rewritten rather than left standing**."* **The test is not an obstacle to `P1` — it is `P1`'s
> receipt.**
>
> ### ⭐⭐ **THE FIX: `P1`'s COMMIT DISCHARGES ALL THREE, AND THE THIRD IS THE POINT.**
>
> | assertion | what the commit does |
> |---|---|
> | the `refused` set | **narrow it to `{"a field"}`.** `mass_battle` is still uncalled and still refuses by name; that is the assertion's remaining true content |
> | ⭐ the `producers` scan | **rewrite `W-E`'s published sentence and re-pin `H-98` in the same commit**, which is what the failure message instructs. Then **re-arm the scan against the new truth** — it excludes `proceedings_seam.py` by name and keeps guarding every other file, so a *second* undeclared margin producer still trips it |
> | the `contested` set | `P2`'s commit, not `P1`'s — `{"kill / wound": "the body", "speak": "a proposition"}` |
>
> ⚠ **Excluding a file by name from a scan is normally the move that hollows a guard out.** It is
> admissible here only because the scan's own message says the published claim must be rewritten
> rather than the test loosened — **the exclusion is the guard recording that its subject changed,
> and the rewrite is the price.** If `P1` lands without the `W-E` rewrite, the exclusion is
> unearned and the guard is hollow.

⛔⛔ **AND THE CAPABILITY RULE REFUSES FOR EVERY PERSON THE TRACER ACTUALLY CONTAINS.** The spec
above says *a missing key REFUSES; it never defaults*. **Nothing anywhere populates
`Person.capability`**: it is `field(default_factory=dict)` (`shape.py:2368`); `tiny_world` sets none
on any of its five persons (`probes.py:57-98`); `corpus_run.py` and `headless.py` contain the word
zero times; and the only writer in the tree is probe **P11**, which *zeroes* it to prove it gates
nothing (`probes.py:432`).

**So as drafted, `P1` returns `CAPABILITY-GAP` for every corpus person, and — mirroring the combat
branch at `:6750-6756` — `contest()` raises.** `P2`'s bar test cannot go green; `P5`'s two-world
comparison cannot run; and `P2`'s *"`results.json` moves"* understates it, because the corpus does
not produce a delta, it produces a raise.

⚠ **AND THE POLARITY IS ARGUABLE IN BOTH DIRECTIONS, WHICH IS WHY IT IS NOT SILENTLY FLIPPED HERE.**
Refusing on a missing key routes around `shape.py:1622-1629`, which refuses at load any verb *gated*
on capability — *"#353 §9.2: capability supplies dice and GATES NOTHING."* The seam is not the
`eligibility:` column, so that loader guard cannot see the provider — **but the behaviour a refusal
produces (no `eloquence` key ⇒ the act cannot happen) is precisely what the rule forbids.**
> ### ⭐⭐ **THE FIX, AND IT IS BETTER THAN WHAT IT REPLACES.**
> **A missing key contributes ZERO to the pool, and `max(1.0, brought + conduct)` catches it.**
> There is no `CAPABILITY-GAP` status, no refusal, and no seeding of `tiny_world` required — **the
> corpus runs unmodified and a person with no declared capability is simply bad at speaking.**
>
> **This is the design's own rule arriving rather than a workaround.** `§A.2`: *"a person who tries
> something they are bad at is the engine working."* The 1D floor was ruled on 2026-09-04 and
> applied to **the mean as well as the variance** precisely so that an incompetent speaker still
> rolls. **An unspecified speaker is the limiting case of an incompetent one**, and the floor was
> already the right answer for both.
>
> ⭐ **And it puts the proposal back on the right side of `shape.py:1622-1629`** — *"capability
> supplies dice and GATES NOTHING."* The draft's refusal made capability a gate in everything but
> name, in a place the loader's guard could not see. **Zero-and-floor makes it supply dice, which is
> what the rule says it does.** Refuse only on a key **present but unparseable**, which is an
> instrument fault rather than a world fact.

**Four further consequences, and the second is a real bug:**

1. **Every `speak` with `contests` set now needs a caller-supplied cap.** `probes._run` passes none
   by default (`probes.py:124-131`), so any probe hand-setting `contests` must pass
   `contest_max_depth` or raise `Forbidden` at `:6117-6119`.
2. ⚠ **`resolve()` hands the seam a Proposition id as a claimant** (find 4). The provider tolerates
   it in v1; **the honest fix is one line at `:6136`** — `if _target in w.persons` — which leaves
   combat byte-identical, because there `p_mid` is a person.
3. The dead `extension` parameter at `:6692` stays dead until `P6`.
4. **`08_SEAM.md:46-73` and `README.md:112-116` become false on merge** and must be corrected in the
   same commit — `ED-1094`'s rule that a PR ratifies what it lands.

---

## P2 · ⭐⭐ `speak` GETS A BODY THAT RUNS — the row, the effect, an evaluable precondition, and the gate

> **This is the proposal that produces the no-player half of `R`. `P1` makes the subsystem run;
> `P2` makes the world run it.**

**Statement.** Give `speak` its degree-keyed `writes`/`emits`, an `EFFECTS` entry so the fold can
write them, a precondition the grammar can actually evaluate, and narrow `resolvable_verbs()` so a
typed contested verb reaches an NPC — **so four bands leave the world in four different states with
zero authored acts.**

**Closes.** `12_BUILD_ORDER.md` step 6; `19_PLAN.md` step 13; the `(Person, stance)` producer gap
(`H-62`; `write_matrix.yaml:203-209`); `04_VERBS.md` §B.1 (vii) — the Partial that docketed. **And
finds 1, 2, 3 and 6 of `§A.3`.**

### The mechanism

**1 · The row, with two corrections it needs in order to load and run.**

- ⛔ **`requires_typed: {form: existence, of: subject, kind: DocketItem}` is unevaluable as built**
  (find 1). `WorldReader.read`'s `exists` branch (`shape.py:1155-1164`) resolves a kind against
  `_STATE_COLLECTIONS` (`:2988-2989`); there is no docket in it, because `w.docket` is a
  `_STATE_SEQUENCES` list of dicts (`:2993`, `:5378-5380`). **The verdict is UNKNOWN and the act
  refuses, every time.** Fix: one branch in `read()` —
  `if arg == "DocketItem": return sum(1 for it in w.docket if it.get("matter") == subject)`.
  ⚠ **This is one more object class for a stem the grammar already has, NOT a new form.** A new
  `form` would be a grammar extension and would need a different argument.
- ⛔ **`emits_on_refusal` stays ONE kind** (find 6). `_fold` builds one Event per kind in the tuple
  (`:5857-5861`) and passes the whole tuple (`:5913`), so a two-kind refusal publishes both on
  every refusal — a design statement made by a loop rather than by a designer.

**2 · The effect.** `@effect_for("speak")`, beside `_eff_utter` (`shape.py:5277`), reading
`res.degree`:

| band | write | emits |
|---|---|---|
| **Overwhelming · Success** | append `(matter, +1)` to `p.stance` | `matter.carried` / `matter.advanced` |
| **Partial** | append `{"date": <the live date at the venue>, "matter": <the speech's own operand>}` to `w.docket` | `docket.formed` **and** `matter.held` |
| **Failure** | append `(matter, −1)` — ⭐ **the adverse write** (`04_VERBS.md:131-136`) | `matter.turned` |

> ⭐ **AND THE RETURN VALUE IS WHY `P5` NEEDS NO ATTRIBUTION RULE.** The effect returns `[a.actor]`
> for the stance bands, so the `StateChange` names **the speaker** — which is what puts the speaker
> into `claim_subjects` (`:4148`, `:4150-4152`). **The hearers' claims about the speaker are then
> minted by the ordinary WITNESS path**, with no change to the deposit rules `19_PLAN.md` step 2
> was going to make. *That is the deposit-attribution problem solving itself for the one case this
> subsystem needs.*

**3 · The gate.** `resolvable_verbs()`'s third gate (`:3352-3375`) excludes every contested verb.
Its stated ground is *a contested act needs a `subject` operand, and `operands_for` returns `{}` for
an UNTYPED verb.* The draft narrowed it to `contested and row.requires_typed is None`, on the ground
that a typed contested verb binds its subject.

⛔ **THE ADVERSARIAL PASS BROKE THIS, AND THE BREAK IS ORDERING, NOT TYPING.** In
`SeasonDriver.resolve` the contest dispatch is at `shape.py:6114-6140` and `_fold` is called **after
it** at `:6182`. Eligibility (`_eligible`, `:5863`) and the typed precondition (`:5869-5894`) are
both **inside** `_fold`. ⭐ **So a contested act reaches the provider BEFORE anything checks whether
it should have been formed** — and the typed cell the narrowing relies on is evaluated *downstream
of the call it would have to gate.*

**And the subject is not guaranteed to be a Proposition.** `_derive_operand` binds `subject` to the
question's referent (`:3719-3720`), and the four question sources supply Dates (Q1), ledger subjects
(Q2), band-crossing sites (Q3) and Propositions (Q4) (`:3886-3933`). **Three of four hand the
provider a non-Proposition** → `MATTER-GAP` → `Unspecified` → whole-case DESIGN-GAP.

> **That is verbatim the failure the gate's own comment says it exists to prevent** (`:3378-3382`):
> *"A computed `kill / wound` would therefore reach the seam with ONE claimant, `combat_seam` would
> return `PARTY-GAP`, and every case that produced one would become a whole-case DESIGN-GAP."*
>
> ⭐ **The narrowing IS safe for `kill / wound`** — it is untyped, so `requires_typed is None` keeps
> it excluded, and the pass confirmed that.
>
> ### ⭐⭐ **THE FIX: THE FORMATION-TIME FILTER ALREADY EXISTS, AND TYPING `speak` IS WHAT SWITCHES IT ON.**
>
> The pass was right that the check must happen before the act is minted, and wrong that no such
> check exists. **`operands_for` is it**, and its own docstring says so in terms:
>
> > *"`None` means THIS PERSON CANNOT FORM THIS CANDIDATE. **⚠ THE RETURN OF `None` IS THE
> > LOAD-BEARING HALF, NOT THE DICT.** Never mint an act with a hole."*
>
> It runs inside the candidate loop at `shape.py:3284-3286`, **before `Candidate(...)` is built at
> `:3289`**, followed at `:3287` by `belief_contradicts(p, row, subject, ops)` — which the same file
> describes as asking *"whether the requirement is known-false ABOUT THIS BINDING."*
>
> ⭐ **And the reason it does not fire for `speak` today is stated in that same docstring:**
> *"AN UNTYPED VERB IS NOT DECLINED. `{}` is the right answer for `speak`, `utter` and
> `create_record`: the grammar states no precondition for them, so there is nothing to bind."*
>
> **So typing `speak` is not merely compatible with the narrowing — it is what arms the filter.**
> A `date_due` question binding a Date, a ledger subject or a band-crossing site now fails to bind
> a `DocketItem`-kind existence cell, `operands_for` returns `None`, and **the candidate is never
> formed.** Where the person *believes* no docket names the subject, `belief_contradicts` declines
> it one line later — `AX-2`-clean, because a person who believes wrongly forms the candidate and
> the fold refuses it.
>
> **The narrowing therefore stands as written — `contested and row.requires_typed is None` — and
> what makes it safe is the typed cell routing through a filter that already runs at the right
> time.** The draft asserted safety; this is the mechanism that supplies it.
>
> ⚠ **The falsifier this needs, and it is cheap:** fold a season with `speak` typed and assert that
> **no `Candidate(verb="speak")` is formed against a Date or a site subject** — `TRACE.note` makes
> the declines countable, and `assert declined >= 1` is the assert-that-it-asserted.

**4 · The docket road — ⛔ AND A DRAFT OF THIS STEP DID NOT CONNECT IT.**

`_eff_convene` (`shape.py:5029-5046`) must set `date["holder"] = a.actor` — **the convener holds the
sitting** — and that half is right: `vacant = not d.get("holder")` (`:5371`), so setting it is what
makes a `DocketItem` form at all.

⛔ **But the draft then said `_eff_convene` should set `date["matter"]`, and claimed that populates
`DocketItem.matter`. IT DOES NOT.** The DocketItem is written by **CALENDAR, not by `convene`**, and
its matter is a hardcoded `None`:

```python
w.write("DocketItem", WriteClass.CALENDAR,
        lambda did=did: w.docket.append({"date": did, "matter": None}),
        record_kind="DocketItem", fieldname="matter", driver="Event")
```
(`shape.py:5377-5380`.) **Nothing reads `date["matter"]` anywhere in the tracer.**

> ### ⛔⛔ **SO THE WHOLE CHAIN BUILT ON IT FAILS, AND THE SUITE HAD THE ANSWER IN ITS OWN HAND.**
> - `P2`'s grammar branch — `sum(1 for it in w.docket if it.get("matter") == subject)` — returns
>   **0 for every CALENDAR-formed item**, so `speak` refuses and the bar test's asserted `matter.*`
>   Event never appears. What appears is `act.refused` (`:5913`).
> - `P3`'s predicate (*"a docket item naming `payload["subject"]`"*) has the same problem.
> - `P3`'s two-vs-three-parameter argument rests on the same false premise.
>
> ⭐ **The declared producer of `DocketItem.matter` is `carry`** (`verb_table.yaml:92`) — **and
> `carry` is one of the seven inert verbs `§A.3` find 7 names and this suite explicitly declines to
> fix.** *The road from a convened date to a docketed matter runs through a dead verb, and two
> findings that were both in this document never met.*
>
> ### ⭐⭐ **THE FIX: REVIVE `carry`. IT IS NOT A COMPROMISE — IT IS THE ROAD THE DESIGN ALREADY
> ### DREW AND NOBODY WALKED.**
>
> `carry`'s row is **`grade: "ruled"`** — not assumption, not absent — and it is complete
> (`verb_table.yaml:88-96`):
>
> ```yaml
> requires_typed:  {form: existence, of: subject, kind: Petition}
> writes:          ["DocketItem.matter"]
> emits:           ["petition.carried"]
> emits_on_refusal:["carry.refused"]
> grade:           "ruled"
> ```
>
> **It is the declared producer of the exact field `speak` needs, it has a typed precondition, and
> it is missing precisely one thing: an `@effect_for`.** Reviving it is not a design decision — the
> row is ruled and its own note already reasons about scoping (*"`carry` writes `(DocketItem,
> matter)`, i.e. it carries a PARTICULAR one"*).
>
> ⭐ **AND THE SEMANTICS ARE RIGHT, WHICH IS THE ARGUMENT.** *A person carries a petition to the
> sitting, and that names the matter.* The road becomes a chain of person-acts end to end:
>
> ```
>   convene  →  the date has a HOLDER, so it is not vacant        (P2 step 4)
>            →  CALENDAR fires it and forms a DocketItem          (shape.py:5371-5380)
>   carry    →  a person carries a Petition; the item gains its MATTER
>   speak    →  requires a DocketItem naming this matter
> ```
>
> **`AX-1` holds at every link: only a person acts, and CALENDAR's step is the maturation of a term
> a person wound.** A docket that filled itself would have been the defect.
>
> **What it costs:** one `@effect_for("carry")`. **Zero primitives** — the row exists, the write is
> declared, the write-matrix row for `DocketItem.matter` exists because CALENDAR already writes it.
> ⚠ **And `_eff_convene` sets `holder` ONLY.** The draft's `date["matter"]` is dropped: the matter
> belongs to the docket item, written by `carry`, and a second home for it would be `ID-2`.
>
> ⚠ **One consequence, stated:** `speak` now depends on a verb outside this design's five. That is
> the *eight inert reused verbs* finding arriving as work rather than as an observation — **and it
> is the right one to revive first**, because it is the only one of the eight on this subsystem's
> critical path.

### ⭐ Execution artifact — two, and the second is the bar

**`test_pr_four_bands_leave_the_world_in_four_states`.** Fold hand-authored `speak`s across act ids
until all four bands appear; assert stance `+1` / `+1` / unchanged-with-docket-grown / `−1`, and
`len({state signature per band}) == 4`.

**`test_pr_a_hearing_runs_with_zero_authored_acts`** — ⭐ **this is `R`'s no-player half becoming an
artifact.** `convene` by `p_high` (who holds it, `probes.py:82-84` + `:95`) in season *n*; in *n+1* the date
fires (`:5363-5381`), `questions_for` raises `date_due` for everyone with `holder in (p.id, None)`
(`:3888`), the chooser forms a `speak` Candidate, the seam runs, and `w.log` holds a `matter.*`
Event carrying a degree. **Twice at one seed, byte-identical hash, and `causes[]` walks from that
Event back to the `date.scheduled` emission.**

**Falsifier:** revert the `resolvable_verbs` narrowing and the bar test finds zero contested Events
— and it asserts that it asserted.

**Control:** `contest_max_depth=None` at the bar still raises `Forbidden` (`:6117-6119`) — **the cap
remains the caller's, so `L-4`'s bound is not quietly relocated into the provider.**

### Primitive count

**0 · 0 · 0 · 0.** One verb-row body in existing columns, one effect, one grammar branch, one gate
narrowed, one bug fix.

### NERS

**N** — the row is the design's entire action set; and without the effect the fold raises
`Unspecified` at `:5940-5949` (*"Part E does not say WHAT VALUE"*) on the first band that writes. So
`P2` is necessary bottom-up *and* laterally: it is what makes `P1`'s degree consequential.

**R** — ⭐ **the no-player half lands here**: dates fire, NPCs speak, bands write, nobody authored
it. *Completeness:* `Partial` genuinely leaves a different world state — a docket that grew — which
is what `04_VERBS.md:151-157` asked for and what a design usually fudges.

**S** — *pauses correctly*: the outer `speak` is one act, and `P6`'s nested run subdivides it.
`Failure: []`-style lawful empties follow `kill / wound`'s precedent (`verb_table.yaml:262-264`), so
the methodology matches an existing row rather than inventing one.

**E, as a ratio** — the largest N/R gain in the suite for one row and one effect. The grammar branch
is the only overhead and it is eight lines.

### What it breaks — and the first one is a re-baseline, which must be printed

1. ⚠ **The corpus re-baselines.** `speak` is one of six verbs that execute today and currently has
   no precondition; with a typed `DocketItem` precondition it refuses wherever no docket names its
   subject. **`runs/results.json` moves, and the deltas must be printed** — `19_PLAN.md:139-140`'s
   discipline, and the §0.1 point 4 rule that a number without a control is not a measurement.
2. ⛔ **ABOUT A DOZEN SITES NEED A CAP, NOT ONE.** A draft named probe A38 alone. **Every
   hand-authored `speak` folded through `probes._run` / `_run_d` raises `Forbidden` once `speak`
   carries `contests:`**, because `_run` passes no `contest_max_depth` (`probes.py:124-131`;
   `shape.py:6117-6119`). The sites: `probes.py:146, 246, 266, 675, 1999, 2119, 2339-2341` (probe
   **A37**, three `speak`s, the same shape as A38 and unnamed in the draft), `:2364-2365`;
   `test_tracer_is_honest.py:922, 2419, 2459, 2741`; and ⭐ **`corpus_run.py:445-448`, which uses two
   bare `speak`s AS A CONTROL** and reads `VERB_TABLE["speak"].emits[0]`. Three further assertions
   pin `speak` in the executed-verb set (`test_tracer_is_honest.py:4651`, `:4721-4722`, `:5575`).
   ⚠ **Ordering rule 2 does not help these** — the failure is a missing cap, not the gate.
3. **`test_we_event_degree_is_assigned…`** (`:7262-7265`) folds a bare `speak` expecting
   `degree is None`; it now reaches the seam. Rewrite to `utter`.
4. ⛔ **Landing `P2` before `P1` turns every corpus case that speaks into a DESIGN-GAP**, because
   the seam raises at `:6766`. **The order is not a preference.**

---

## P3 · THE BENCH EXISTS — `judging_set`, and `determine`'s predicate and effect

**Statement.** Replace the unconditional raise with `H-32`'s own registered default, and give
`determine` a predicate and an effect — so a seat-holder can dispose of a docketed matter and an
unseated person is refused, witnessed.

**Closes.** `H-32` (grade `assumption`, default stated, sweep declared); `12_BUILD_ORDER.md` steps
1 and 7; `19_PLAN.md` step 10; `determine`'s `grade: absent` (`verb_table.yaml:177`); and **`P-35`**
— *bench: persons or seats?* — **settled by the code**: the Query returns holders, and `holder_of`
is the tenure walk.

### The mechanism

**1 · `Query.judging_set(w, rung_id)`** (`shape.py:3161-3163`) currently raises
`Unspecified("judging_set_rule", "S61")` unconditionally. Replace with `H-32`'s default verbatim:
holders of a live `hold` on an `Office` whose `remit_acts` includes `determine` and whose
`scope_rung or rung` contains `rung_id` by `w.contain_ascends` (`:2664`). **Empty returns `[]`,
never a raise** — the date fires and lapses, which is `H-32`'s own stated default. Sweep arms
`remit+scope / remit only / scope only`, as data.

> ⛔ **A DRAFT SHIPPED TWO PARAMETERS AND ARGUED THE THIRD HAD NO PRODUCER. IT NOW HAS ONE, AND
> ### THE ARGUMENT IS WITHDRAWN — `judging_set(w, venue, matter)`, THREE PARAMETERS.**
>
> The draft's reasoning was that `DocketItem.matter` is never populated, so a third argument would
> always be `None` and would be `ID-13` on a parameter. **`P2`'s revival of `carry` populates it**,
> so the premise is gone.
>
> ⭐ **And the draft ignored the design's own objection, which the adversarial pass caught.**
> `04_VERBS.md:333-337` does not argue for the third parameter on completeness grounds — it argues
> that **a venue-only judging set makes two different questions before one bench return the same
> answer**, which it names as *"the `Rung.judging_set_rule` defect — decision-shaped state on a
> place — arriving one level up."* **And `Rung.judging_set_rule` was deleted for exactly that
> shape** (`04_VERBS.md:341-343`). A two-parameter form would have re-admitted a defect this design
> had already removed, **one level up, where nothing would have caught it.**
>
> ⚠ **The draft also claimed to settle `P-35` "by the code" while shipping the reading the design
> document argues against.** That is a design objection answered by silence — which is the one
> disposition `§G.4.5`'s five tests do not offer. **Withdrawn.**

**2 · The predicate.** `@requires_predicate("determine")`, beside `_req_convene` (`:4848`): a date
at `payload["venue"]` that has `fired`, a docket item **whose `matter` is** `payload["subject"]`,
**and** `a.actor in Query.judging_set(w, venue, matter)`. ⚠ **This depends on `P2`'s revival of
`carry`** — without it the docket item's matter is `None` for every date and the predicate never
holds. **`P3` does not land before `P2`.**

> ⭐ **AND THIS NARROWS `P-03` SUBSTANTIALLY.** Eligibility (`remit:determine`) is already evaluated
> by `_eligible` (`:5757-5762`) over the actor's own live holds — **so a seat-holder can already act
> as their seat.** What `Act.via` would add is a *delegate acting through a seat they do not hold*.
> That is regency and governors, not the twelve games.

**3 · The effect.** `@effect_for("determine")` opens a `commit` Tenure `actor → matter` carrying
`degree = payload["disposition"]`. **The finding is the determiner's own commitment**
(`00_DERIVATION.md:117`; `19_PLAN.md:462-468`) — owner-clean under `T-m`, because the person who
made it is the person who may close it.

> ⚠ **THIS NEEDS ONE MORE `writes` PAIR THAN THE LIVE ROW, AND `04_VERBS.md:303` SAYS "UNCHANGED".**
> The file is wrong, for a checkable reason: **`commit` has no `@effect_for`** (find 7), so a
> `determine` that only *graded* a prior commit could never execute — there would be no commit to
> grade. `writes: ["Tenure.since", "Tenure.degree"]`. **One act, one owner.**

### ⭐ Execution artifact

`test_pr_a_bench_member_determines_and_an_unseated_one_is_refused`: `p_high` holds `off_duke`
(remit includes `determine`, rung `D`); `judging_set(w, "S")` → `["p_high"]`; `judging_set(w, "R")`
→ `[]`; strip `determine` from the remit → `[]`; **all three sweep arms run.** Then `determine` by
`p_high` opens a Tenure with a degree and emits `matter.determined`; by `p_low` it emits
`determine.refused`.

⚠ **Two probes must be rewritten in the same commit — and a draft of this paragraph described the
transition wrongly.** Probes **F8 and F21** (`probes.py:1097`, `:2315`) call
`Query.judging_set(w, "D")`, which raises. **They are not passing today:** `run_probe` catches
`ShapeGap` and records `verdict="GAP"` (`run_cases.py:89-91`). After `P3` the call returns a list,
the probe returns its literal `"UNREACHABLE"`, and `run_probe:78-85` records
**`verdict="NOT-REFUSED"`** — *"the shape PERMITTED what this probe expected it to refuse."* **Both
feed `DEGRADED` (`run_cases.py:321`) before and after.** The rewrite is required; the *"green-to-red
flip somebody reads as a regression"* framing was false, and would have sent a reader looking for a
pass that was never there.

### Primitive count

**0 · 0 · 0 · 0.** One Query body, one predicate, one effect, one extra `writes` pair on an existing
row.

### NERS

**N** — `determine` is the only disposing verb in the design and has been dead since it was written
(`11_NERS.md:28`). Every game with `disposal: bench` needs it; that is seven of the twelve.

**R** — the no-player half needs `P2`'s docket road, so this is a dependency and not a gap.
*Completeness:* **the empty-bench case is a lapse, not a crash** — a sitting nobody is seated for
simply does not decide, which is the correct world behaviour and is the reason `H-32`'s default
returns `[]`.

**S** — ⚠ **`binding_decision` resolves before `social` in the stratum order** (`rosters.yaml:130`),
so a hearing and its judgment fall in different seasons. **That is the existing order, not this
proposal's** — `P-14`, and it is worth Jordan's eye but is not a defect introduced here.

**E, as a ratio** — four lines and a tenure walk, against the largest open governance row in
`02_THE_SOCKET.md:174`.

### What it breaks

F8 and F21's verdicts. And `H-32` moves from `assumption` to `measured`, which the register's own
`--check` may require a `cite:` for. `[UNVERIFIED]` — I did not read `register.py`, and the planner
did not either.

---

## P4 · `tell` DEPOSITS WHAT IT TOLD — the `product` column, at WITNESS

> **The only proposal in the suite that spends a primitive, and the one with the strongest
> no-player result.**

**Statement.** A verb-table column `product: own_ledger`, read at the WITNESS barrier, deposits the
actor's own claims about the act's subject into every observer's ledger at source `told_by` and the
teller's own confidence — **so a proof told at a hearing changes the hearers' ledgers.**

**Closes.** `P-05` for `tell`; `19_PLAN.md` step 19; `12_BUILD_ORDER.md` step 11; `H-116`'s write
half (`14_THE_WORLD_IN_THE_ROOM.md:205-215`). ⭐ **And it mints `told_by`**, which has been rostered
(`rosters.yaml:119`) and never minted since the roster was written.

### Why it cannot ride the existing carrier — stated first, because it is the interesting part

`tell`'s one declared read is `claim.held` (`verb_table.yaml:479-481` → `WorldReader.read`,
`shape.py:1227-1229`), and `LEDGER_DERIVED_STEMS` (`:1284`) excludes it from deposit at `:6407`.
⭐ **That exclusion is correct and must not be relaxed: a deposit reporting what a ledger holds
would falsify itself.** So the product cannot ride on `e.observed`, and the fix is not a fourth
`observation_deposit_mode` value — `H-121`'s lesson (`:6355-6360`) is that two decisions must not
share one fixture.

### The mechanism

It rides what already exists at WITNESS: `self.act_of[e.id]` (`:6212`) gives the act, `act_refs(a)`
(`:4118-4130`) gives the subject, and `w.persons[e.subject].ledger` is the teller's. **A third loop
after `:6423`:**

```python
row = VERB_TABLE.get(act.verb)
if row.product == "own_ledger":
    for n, c in enumerate(teller.ledger):
        if c.subject == subj and c.when <= w.tick:
            Claim(H(..., f"told:{e.id}:{n}"), pid, c.subject, c.predicate, c.value,
                  w.tick, source="told_by", confidence=c.confidence, visibility="own")
            → w.write("claim_ledger", INTERIOR, ..., emits="claim.deposited", causes=[e.id])
```

Recipient is every `pid` in the fan (`observers_for`, `:4430-4449`) **except the teller**. `VerbRow`
gains `product: str = ""` (`:1413-1471`), loaded at `:1573-1580`.

### ⭐ Execution artifact — and the second one is what it is for

**`test_pr_a_telling_lands_in_the_hearers_ledger`**: plant
`Claim(p_low, "Hh", "stores:grain", 5, source=firsthand, confidence=60)`; fold `tell(subject="Hh")`;
after WITNESS `p_mid.ledger` holds `("Hh", "stores:grain", 5, source="told_by", confidence=60)` and
`p_low` holds no second copy. **Control:** with the column absent, `p_mid` holds only
`("Hh", "news.told", True)` — the event-kind claim, which is all a telling deposits today.

**The seeded hash moves, and the move is asserted** — `content_hash` digests `Person` via `repr`
(`:2593-2604`), following `test_wb_the_carrier_moves_the_seeded_hash` (`:6578`).

⭐⭐ **The second artifact is the one that matters.** `belief_contradicts` (`:3822`) now sees, in its
own namespace, a claim that arrived from somebody else's telling — **one NPC declines a `transfer`
on a *told* belief that a granary is empty.** That is the first firing of the belief→decision edge
on hearsay, and it is the difference between a world that logs and a world that gossips.

### Primitive count

**0 verbs · 0 carriers · 0 edge kinds · 0 fields — and ⚠ ONE VERB-TABLE COLUMN.**
`17_PLAYABILITY.md:801-803` is right that a column is a schema addition. **It is counted, it is the
only one in the suite, and it is spent on the edge the whole epistemic layer was waiting for.**

### NERS

**N** — `15_WHY_IT_IS_A_GAME.md:91-93`: without it, nobody has a reason to tell anybody anything.
And from the other lane's side it is the deposit both lanes were told to build **once**
(`ED-SC-0036`; `04_VERBS.md:432-438`), so building it here discharges a cross-lane obligation rather
than duplicating one.

**R** — ⭐ **the strongest no-player result in the suite: rumours exist, and they can be wrong.**
*Completeness:* the told claim carries the teller's own confidence, which closes `19_PLAN.md` PART
I.8's residue **for the single-claim case**. ⚠ **The max-confidence residue survives** where a
teller holds several claims on one subject — stated, not swept under.

**S** — it feeds `H-102` harder than anything else in the game (one occasion, many witnesses, many
deposits), and **the 200-claim cap (`:1772`, `:6429`) will evict.** `M-1` must run after it.

**E, as a ratio** — one column and one loop, against the edge the design's entire anti-solver
argument presupposes.

### What it breaks

**Ledger pressure — and this is the exact defect the tracer already recorded once**
(`:4183-4190`: extra claims made the decay sweep inert). **Ship with `M-1`.** And `H-111` (refusals
propagate as news) gets louder: a `news.untold` refusal still deposits an event-kind claim, so
**the product loop must key on the success emission only.**

---

*The suite continues at `20_REMEDIATION_part2.md` — `P5` through `P11`, the dependency order and
the shortest path, the conflict matrix, what is deliberately not proposed, the one item that needs
a ruling, and the adversarial pass.*
