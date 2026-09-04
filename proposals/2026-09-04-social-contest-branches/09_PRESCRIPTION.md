# 09 · PRESCRIPTION — what to do going forward

## Status: **PROPOSED (2026-09-04). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE. Nothing here runs.**
## Written by the orchestrator (Opus). **The Fable tier hit its usage limit mid-session**, so this is
## not the Fable-authored prescription the plan called for; the synthesis is Opus-tier and says so.
## Ranked by what is load-bearing on **the game**, per `CLAUDE.md` §0.1 pt 5 and §0.3.

---

## §0 · THE THREE THINGS THAT CHANGED LATE, AND WHAT THEY COST

Three corrections landed after most of this session's work was done. Each narrowed a finding, and a
reader who skips them will act on a superseded picture.

1. **The social contest terminal is RATIFIED, not an unratified engine.** `ED-1057` (ratified
   2026-07-01) designs the per-juror ballot verbatim: *"each juror votes A iff
   `sharpness*(adv_A − adv_B) + per-juror-noise > 0`, so a juror can cross against the room (a lopsided
   room is near-unanimous, a close room is near a coin-flip)."* That is exactly `resolver.py:139`.
   **The engine-classification lens (Instance A/B/C, "wrong-engine defect") does not apply and its
   findings are withdrawn.** What survives from the NERS material is the **method** (`CLAUDE.md` §0.06
   per PR #364, and `14_NERS.md`'s scoring rules), which never depended on the engine taxonomy.
2. **Therefore the 87.7 % crisis-side win rate is not a defect of the terminal.** ED-1057 *designs for*
   "a lopsided room is near-unanimous". A lopsided input producing a lopsided verdict is the ratified
   behaviour working. **The defect is upstream, in what makes the room lopsided.**
3. **The `9`-member import-cycle figure is docstring-only**; the test asserts two families, not a member
   count. No cycle test blocks any change here.

---

## §1 · TIER 0 — SHIPPED BEHAVIOUR IS WRONG. Cheapest work in the session, no design authority needed.

### 1.1 · The victory condition advertises three clauses and has two

`engine/autoload/victory.py:73` reads `world.clocks.get('Turmoil', 0.0)`. `game_state.py:338`
initialises `Turmoil` to `0.0` and **nothing in `engine/` or `systems/` ever writes it**. With
`PS_MAX = 6.0`, `ps_ok = (0.0 <= 6.0)` is **always True**. A faction can win with the realm in any
political state whatsoever.

**Prescription — decide, then make the code say what you decided.** Two honest options, and *leaving
it* is not one:
- **(a) Wire it.** Give `Turmoil` a writer. Its natural producers already exist — the same events that
  move `Stability` and `Legitimacy`. This is the option that makes the victory condition mean what it
  says.
- **(b) Delete the clause.** If political stability is not a victory gate, `ps_ok` and `PS_MAX` are
  dead vocabulary asserting a rule the game does not have.

**Falsifier, either way:** a test that constructs a world at `Turmoil > PS_MAX` with all other clauses
satisfied and asserts the faction does **not** qualify. Under (b) it asserts the clause is gone. **It
must fail on today's tree** — that is the control (`§0.1` pt 3).

### 1.2 · The only production-path gate cannot see the regression it exists to catch

`engine/tests/test_mc_v18_regression.py:151-158` sums `world.scenes_resolved` and asserts `> 0`.
`engine/mc_v18.py:156-160` **also increments that counter for parliamentary votes**. So the assertion
passes with **zero kernel contests** — and its own docstring says it exists to catch *"the promoted
kernel was reachable in code but dead-in-campaign"*, which is precisely the failure it cannot observe.
`CLAUDE.md` §0.1 pt 2, in the one gate guarding this subsystem.

**Prescription: count kernel contests separately.** One counter, one expression, no new guard — this is
the §0.1 pt 5 case where a guard is *earned*, because the artifact is load-bearing on the game.
**Falsifier: it must fail on a tree where the contest path is stubbed out but votes still run.**

---

## §2 · TIER 1 — THE SOCIAL CONTEST'S ACTUAL DEFECT

### 2.1 · The faculty derivation is a provisional bridge that makes every contest a foregone conclusion

`engine/cross_scale/scene_dispatch.py:139` derives both sides as
`(max(1, round(f.L)), max(1, round(7.0 - f.Sta)))`. **Measured over 4,979 councils: 81.9 % are fought
at side-A faculty 1, and 87.7 % are won by the crisis side.** Faculty 1 against faculty 6 is not a
contest under any resolver, and the ratified terminal is behaving correctly when it returns a
near-unanimous verdict for the strong side.

This is a `[SEED]` bridge — self-declared provisional, never ratified — and it is **the single highest-value
change available to the social contest.** Fix it and the ratified mechanism starts producing real
verdicts; leave it and every downstream branch inherits a decided contest.

**Prescription — this needs a design call, and here is the architecture-conformant default.** The two
sides are currently derived from **incommensurable quantities**: one faction's Legitimacy against the
*inverse* of the same faction's Stability. Under `CLAUDE.md` §4's *idempotent in meaning* test that is
already a defect — the two numbers do not measure comparable things. The default that follows from the
architecture is to derive **both sides from the same quantity on two different parties**, which is what
a contest is. If the Emergency Council genuinely has only one faction, then it is **not a contest** and
should not be routed to a contest resolver — that is the honest reading of `_emergency_council_parties`'
own `[SEED]` marker.

**Do not attempt to fix this by giving the weak side more dice.** The resolution-diagnostic material
records that the `1/√N` non-uniformity **cannot be fixed by any pool transformation** — a Stage-4
aggregation sweep proved it. Adding dice moves the operating point; it does not make the contest close.

**Escalation:** whether an Emergency Council is one faction in crisis (therefore not a contest) or two
parties (therefore a contest, and who is the second) is a live design choice with materially different
games behind it. **This survives all five tests and is Jordan's.**

### 2.2 · The seam discards the design — six parameters

`engine/cross_scale/scene_dispatch.py:300-301` passes none of: **venue preset · policies · armature ·
record · world · proceeding literal.** These six are the entire distance between the kernel that exists
and the kernel the tests exercise. Consequences measured: Stage-3/Gate-C (CR4 terrain, CR5 backfire,
the adjudicator armature) is unreachable in production; `proceeding_venue` passes no preset so all
eight proceedings run on `Venue` defaults and the ~260-line venue library is unreachable; **zero player
decisions occur on the production path** (all 846 traced moves were the defaulted `logos_spammer`).

**Prescription: open the seam before building anything on it.** In dependency order —
`armature=` passthrough (closes the Stage-3 reachability defect), `rng` injection at **all three** draw
sites (`resolver.py:32`, `:334`, `:139`/`:144` — not one), then policies and venue preset.
**Control: the two campaign goldens must not move**, because opening a parameter with its current
default is meant to be value-identical. If they move, the change was not what it claimed.

---

## §3 · TIER 2 — CROSS-SYSTEM INTEGRITY, straight from the meta-architecture

These are `PR #362` shape violations that exist **today**, independent of whether #362 is ever ratified.
Each is a case where the tree already agrees with the shape and the code does not.

### 3.1 · Territory ownership has three stored homes — `AX-4` / `D-10`

`Territory.owner` · `Faction.territories` · `Settlement.owner_faction`. `mass_seizure.py:290` writes
only the first (latent — zero callers), no transfer path ever writes the third, and `mc_v18.py:295`
scores a winner from two of them **in one expression**. `parliamentary_transfer.py:347-360` records a
prior divergence, so this has already gone wrong once.

**Prescription: one owner, and the other two become Queries.** This is `PR #362`'s *"every object-side
index is a barrier cache owned by Nobody"* applied literally. Pick `Territory.owner` as the store —
it is the one the seizure path already writes — and derive the other two. **Falsifier: a test that
transfers a territory by every available path and asserts all three reads agree.** It must fail today.

### 3.2 · Two grammars produce the same four words — an **S** defect under §0.06

`massbattle.py:130-139` maps rout state and survivor fractions to
`Overwhelming/Success/Partial/Failure` with three uncited thresholds; `faction_action.py:470-524`
consumes that to key Terms/Storm and Accord **with no marker of which grammar produced it**.

⚠ **The single-owner guard's exemption is documented and reasoned** — it exempts band-producers that
are not dice-margin ladders, and says so. **No guard failed.** But under `CLAUDE.md` §0.06's S
definition — *"calculations consistent in methodology with other mechanics"*, glossed as **"two ladders
for one quantity is an S defect even when each is individually correct"** — this is a straightforward
S defect at the consumer.

**Prescription, cheapest first:** make the grammar explicit at the boundary. The consumer should
receive a value that names which ladder produced it, or the two should be unified. **Do not start by
unifying** — the mass-battle bands may be right for mass battle; what is wrong is that a consumer
cannot tell them apart.

### 3.3 · Mass battle re-implements four engine primitives, and only one is guarded

`resolution.py:37` (die rule), `:209` (soft-cap), `:221` (μ-shift with its own `_SIG_PER_DIE`), `:104`
(ladder). No test compares the σ pair to `sigma_leverage`. **A drift in `M_MAX` or per-die σ in either
home moves every conquest, unseen.** This is `CLAUDE.md` §8's *"every rule lives once"* invariant, and
it is load-bearing on the game.

**Prescription: a parity test, not a refactor.** Assert the two homes agree across a swept range. That
is the cheap guard that earns its existence under §0.1 pt 5, and it makes any later unification safe
rather than speculative.

### 3.4 · Key ids cannot survive a restore

Ids are minted from three undeclared per-`World` counters that `serialize_world`/`restore_world` do not
carry, so **the replay premise asserted at `module_contracts.yaml:1545` cannot hold across a reload.**

**Prescription: carry the counters in the serialised state.** Falsifier: serialise mid-campaign,
restore, emit, and assert no id collides with one already in the log.

---

## §4 · TIER 3 — THE THREE BRANCHES. Do not execute the proposals as written.

`05_RECONCILIATION.md` establishes that none of the four documents is executable. In dependency order,
and **only after Tier 0–1**:

| # | work | blocker to clear first |
|---|---|---|
| 1 | **Spine** | rename `_resolve` (collides with `wrapper.py:303`, called at `:444`); **do not consume `margin()` in production during S0** — the document's own §9.1 states this mitigation and its change list contradicts it; add the 7 unlisted `_kernel_tests.py` break sites |
| 2 | **Inquiry** | the `formal_grounds_check` rewrite **silently regresses shipped faction code** — default the third clause `True` when the new parameters are absent, or gate under a new name; replace `KeyLog.of_type` (does not exist) with an iteration; re-run the dominance analysis against the **reachable** venue (`evasion_strikes=2`, not 1) |
| 3 | **Consensus** | **B1: the degree mapping is arithmetically inoperable** — `margin ∈ [−1,0]` against fixed bands at 0/1/3. Adopt the spine's `SUCCESS_UNIT` division. Then the antibody, which is inert on all three channels |
| 4 | **Negotiation** | reconcile `floor_a`'s two contradictory definitions; delete the false import-cycle argument and the falsifier built on it; re-argue `settle()`'s N-line (`destroy_record` exists); move the breach asymmetry into the exploit table as a **dominant strategy** |

**And one thing that is ready now:** `ED-SC-0020` is answered by architecture on rungs 4–5 — the burden
family already exists in disguise and `ProofBar:71-72` already carries Fork A's stall semantics. **Close
the row with that citation.** `ED-SC-0015` is *closable, not closed*: `ledger_sweep`'s only call site has
zero callers, so `ttl=1` is permanent today. Do not close it until that is fixed.

---

## §5 · META-ARCHITECTURE POSTURE

**PR #362 stays PROPOSED. Do not ratify it.** Three reasons, all from the document:
1. Its own §F names **two gaps that block the build outright** — `F.20`, *nothing founds a hearth or
   builds a site, so **the world only decays***; and `F.24`, every verb's `requires` is a prose string,
   so *"the resolver has no body"* returns as *"the resolver has thirty."* Ratifying a document that
   says it cannot build makes its `## Status:` line a claim the code cannot honour — the §0.05 failure.
2. **Ratifying would not buy dynamism.** Its in-season loop already resolves everything inside the
   season; its constraints are purity guarantees that buy the reproducible season hash.
3. **`F.20` is the real dynamism defect.** *"The world only decays"* is a far more direct threat to a
   living world than commit sequencing, and it is a gap to close, not a ratification to grant.

**Feed two things back to the chain:**
- **The in-scene binding ruling is already satisfiable** — no amendment needed. `§C.4:576` flattens acts
  across all scenes into one ordered fold; `D-49:871` forbids nesting, not same-pass resolution.
- **`§C.5.1` is a genuine finding.** A contest resolves its sides and stakes **once, from `proj`** — the
  barrier-2 pre-fold snapshot — so a later contest in the same fold cannot see an earlier contest's
  write. The document is internally asymmetric: `requires` reads `world_as_predecessors_left_it`
  (`:579`) while the roster reads `proj` (`:707`). **This is the same "time doesn't exist within a
  season" shape one level up**, and it is the most valuable thing this session can return.

**Merge PR #364.** It gives the NERS definitions a canonical home and closes **ED-929**, open since
2026-06-11, where two skills cited `canon/definitions.yaml` as their source and that file **has never
existed**. It is reference under §0.05, which is the correct status.

---

## §6 · PROCESS — four rules this session earned the hard way

1. **Reachability is a property of an EDIT, not a BRANCH.** Three of four proposals got their own
   control wrong, in three different directions. Ask it edit by edit; anything touching
   `systems/factions/`, `systems/settlements/sim/ledger.py` or `engine/cross_scale/` is reachable until
   shown otherwise.
2. **Check the assertion, not the prose above it.** Four instances, mine first: a docstring is not a
   gate, a `values:` line is not the `note:` above it, and a summary of a source is not the source.
3. **An ablation without a positive control is a story with numbers in it.** Arm P — a known-enormous
   intervention — was **invisible to the χ² test** that had just returned "not significant" for the
   real arm. Without it, *"the social contest is inert"* would have shipped: dramatic, wrong, and
   undetectable.
4. **A design document may not be cited as the reason a behaviour is correct** (§0.05), and the
   converse now has a worked case: **a mechanism may not be called unratified without checking the
   ledger.** ED-1057 ratified the thing this session nearly filed as an escaped engine.

---

## §7 · WHAT WOULD MAKE THIS PRESCRIPTION WRONG

- **It is Opus-authored, not Fable-authored**, and it synthesises audits it did not perform. The Fable
  tier was unavailable; a Fable pass over this document has not happened and is the obvious next check.
- **§2.1's default is a design opinion.** "Derive both sides from the same quantity" is architecturally
  conformant but it is not the only conformant answer, and the escalation is real.
- **The Tier 2 items rest on a reading with stated gaps** — `npcs` and `ui` unreached, `_architecture`
  surface-only, ~10,300 lines of combat and mass-battle interior unread. A `Turmoil` writer outside
  Python, or a mass-battle parity test under `tests/sim/`, would overturn §1.1 or §3.3 respectively.
- **Nothing here has run.** Under §0.2 this document is **paper**, and every item above is done only
  when its named falsifier executes and something ran it.
