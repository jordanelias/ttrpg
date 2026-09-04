# 02 · NEGOTIATION — strike a bargain

## §0 · Status, grade, and what a veto costs

## Status: **PROPOSED — nothing ratifies.** 2026-09-04, SC lane. Agonist (producer) output for the negotiation branch of the social-contest rebuild. A read-only critic that never saw this reasoning is expected to attack it; §12 records the attacks I ran on it myself and which of them succeeded.
## Grade per `CLAUDE.md` §0.2: **PAPER.** `settle()` does not exist. Nothing in this document has executed. The pieces it composes on *do* execute in isolation (`Bout`, `TallyAtClose`, `DefeatCatalogue`, `degree_from_net`, `LedgerTag`) but no run has produced a `Settlement`, and until one has, this is a design and not a juncture. It becomes DONE when §9's F-N1..F-N8 pass and a seeded run through the seam produces either a Debt tag or a refusal Event and never both.
## Consumes: **`proposals/2026-09-04-social-contest-branches/01_SPINE.md`** (sibling, written) for `WinCondition.margin()`, the single `ContestOutcome` return shape, `burden` on `PROCEEDINGS`, `armature=` passthrough, `rng` injection and `contestant_from_person`. This document defines **only the terminal** and redefines no spine object. Three spine results bind it directly and are consumed rather than restated: **§1.9** (the binding-in-scene invariant, I-S6a/I-S6b), **§3.4 (iii)** (a mutual outcome is a `Record`, never per-claimant `commit` Tenures — with the order-fragility proof that makes the alternative broken on its own terms), and **§1.3 + A3** (`margin()` returns **whole-d10-success units** via a per-subclass `SUCCESS_UNIT`, shipped tagged **`[SEED]`** and uncalibrated).
## ⚠ **Inherited `[SEED]`:** `TallyAtClose.SUCCESS_UNIT` is uncalibrated (`01_SPINE.md:503`, `:526`). Every degree band this document quotes is therefore **`[SEED]`-dependent at its edges** — the *ratios* are canon and the *boundaries between them* are not yet measured. `tools/balance_oracle.py` is the named calibration instrument. Marked here once; §5.3 and §9 carry it.
## Compliance target: `proposals/2026-09-03-meta-architecture/04_CODE_ARCHITECTURE.md` (PR #362, **PROPOSED, HELD BACK IN FULL**) — a shape constraint, not canon (`CLAUDE.md` §0.05).
## Scope discipline: every anchor below is `path:line symbol`, read against the working tree at HEAD `1e163ee` on 2026-09-04. Snapshot material is cited `v30-snapshot-2026-06-28:<path>` and **is not in `main`**. No pytest was run. Nothing outside this file was created or edited.

**What a PR #362 veto costs this branch — measured against the parts, not asserted.**

| survives a veto (kernel-local, no PR #362 vocabulary) | dies with it |
|---|---|
| `settle.py` — `settle()`, `split()`, `SHARE_BY_DEGREE`, `Settlement`, `Refusal` | `Act.actor` / `Act.via` / `Seat` / `remit` as the envoy channel |
| the symmetry repair to the §7.2.1 split (§1 row 6) | the write gate, `Receipt`, `NoOpReceipt` |
| `PROCEEDINGS["private_negotiation"]["burden"] = "NONE"` | `Tenure.degree` as the reservation's source (§4 S0) |
| the deletion of `NegotiationMode` (`modes.py:342`) and of the `negotiation` `GAMES` row | `writes_at(degree)` on a verb row |
| the ZOPA gate and the clamp rule | `claimants : PersonId[]` — the branch reverts to faction-derived ints |

Under a veto the branch still runs: the caller supplies the two reservation bounds explicitly, and the settlement is written as a `LedgerTag(kind="Debt")` through `systems/settlements/sim/registry.py:102 Settlement.tag` and/or `systems/factions/sim/treaty.py:145 register_treaty`. **The decomposition was cut so a veto costs the seam vocabulary, not the mechanic** — but that is a claim about a future veto, not a measured one.

---

## §1 · Verification of `00_BRANCH_SHAPES.md` §3, element by element

Each row is the shape spec's claim, my verdict, and the anchor I read. **Amendments are the point of this section**; four elements needed one and one is refuted outright.

| # | shape-spec element (`00_BRANCH_SHAPES.md` §3) | verdict | evidence |
|---|---|---|---|
| 1 | `negotiation` is a STUB row returning a bare `StubResult` | **CONFIRMED** | `systems/social_contest/sim/contest/wrapper.py:236 GAMES` row `"negotiation"` at `:242`, resolve = `wrapper.py:220 _stub`, which returns `stubwire.stub_resolve(...)` → `engine/substrate/stubwire.py:42 StubResult`. Pinned by `systems/social_contest/sim/contest/_kernel_tests.py:700-703`. |
| 2 | the leverage half already resolves — `private_negotiation` is `TallyAtClose` with the tracker optional | **CONFIRMED** | `modes.py:513 "private_negotiation"` — `exchanges=(1,3), roles="symmetric", resistance="none", adjudicator="no_adjudicator", tracker=False, tracker_mode="optional"`; `modes.py:521 _use_tracker` resolves the tri-state; `resolver.py:62 TallyAtClose` returns A/B/`"draw"` at close only. |
| 3 | the *agreement* half does not exist | **CONFIRMED** | `audit/2026-08-06-social-contest-three-lens-audit/00_synthesis.md:328` "**The missing S4 is the missing terminal of the adjudication cluster we do have**"; `:462` "the largest single piece of *new* design this subsystem needs". Canon agrees against itself: `systems/social_contest/social_contest_v30.md:702` "Negotiation compromise resolution (ZOPA-style) | Identified as structurally different from Persuasion Track, **not designed**". |
| 4 | `settle()` survived the false-N-line hunt; its job is done by nothing ruled in | **CONFIRMED** | Re-run independently in §7 against `systems/settlements/sim/ledger.py`, `systems/factions/sim/treaty.py`, `resolver.py`'s win-conditions and `armature.py`. Nothing computes a division of a surplus. `faction.py:117` computes one — for succession only, and incorrectly (row 6). |
| 5 | the split comes from the §7.2.1 track-distance table, single owner **moved to `dictionaries.py`** | **REFUTED on the destination; confirmed on the source.** | The table is real: `faction.py:117` `ratio = {4: 0.60, 5: 0.55, 6: 0.50}[min(6, max(4, round(t)))]`, canon at `social_contest_v30.md:421-423` (ED-762). **But `dictionaries.py` is the wrong home and the reason is mechanical, not stylistic.** `skills/valoria-vector-audit/scripts/structure_audit.py:312-325 build_g_code` resolves `from . import X` to an edge onto the **package node** as well as the submodule; `dictionaries.py:45` is one of only two files in the package that use that form (`wrapper.py` is the other — verified by counting `from . import` per file across all 15 modules: `dictionaries` 1, `wrapper` 3, every other non-test module 0). So `dictionaries` → `contest` → `wrapper` → `dictionaries` is the loop, and **any new module that imports `dictionaries` joins the 9-module SCC** that `tests/valoria/test_import_cycle_game_state_npe.py:23` hard-codes and `test_exactly_two_cycles_remain_and_they_are_the_expected_families` fails on. Putting the split table in `dictionaries.py` and reading it from `settle.py` would break a live blocking test as a side effect. **The table belongs in `settle.py`, beside its one reader**, which keeps `settle.py` a leaf (§7, F-N6). |
| 6 | the split table is the right rule to lift | **AMENDED — the table as written is side-asymmetric, and lifting it unchanged would carry the defect into every negotiated deal.** | Read `faction.py:107` `leader = 'a' if t >= 5 else 'b'` together with `:117`'s `{4: 0.60, 5: 0.55, 6: 0.50}`. On B's side the leader's share is **monotone** in advantage (t=4.6→0.55, t=4.0→0.60); on A's side it is **anti-monotone** (t=5.0→0.55, t=5.6→**0.50**) — more advantage buys A *less*. And an exact tie (t=5.0) awards **A 55%**. Canon carries the same defect in its own principle: `social_contest_v30.md:415` says "**track-distance weighting** applies", and tracks 4 and 6 are the same distance from the centre yet get 0.60 and 0.50. **The values are canon; the keying contradicts canon's own stated principle.** §5 re-keys on `abs(margin)` through the one ladder, which is symmetric and monotone by construction and preserves the three ratios exactly. |
| 6a | — the one test over that table | **AMENDED — it cannot observe the failure it excludes** (`CLAUDE.md` §0.1 pt 2). | `_kernel_tests.py:182`: `ck("succession split ratio canonical (§7.2.1)", _o[0]!='split' or _o[2] in (0.50,0.55,0.60))`. It asserts **membership in the value set** and nothing about the keying, and its leading `_o[0]!='split'` disjunct makes it vacuously true whenever the sampled contest was not a split. The `SC_INVENTORY.md` §G3 sweep found 0 vacuous-pass patterns because it swept `for`-loops; this one is a bare conditional at module level. |
| 7 | reservations are the two actors' `commit` degrees, not a new `Contestant` field | **CONFIRMED as the right source; AMENDED as unavailable today.** | `proposals/2026-09-02-executable-architecture/write_matrix.yaml:329-331` declares `Tenure.degree`, steps `[RES]`, class `ACTS`, `by: DR-2`, emits `tenure.graded` — so the carrier is declared. **It does not exist in the live tree**: `systems/social_contest/` has no Person, no Tenure and no commit degree (grep — the package's only inputs are `Contestant(faculty, standing_start, reserve_max, dossier, evidence, charisma)`, `resolver.py:180`). `settle()` therefore takes the two bounds as **required parameters** and the derivation is named as the one missing line (§4 S0, §11 fork 3). |
| 8 | `settle(margin, floor_b, ceil_a, stakes) -> Settlement \| Refusal(no_zopa)` | **AMENDED on three of four parameters and on the return payload.** | (a) **`floor_b` is transposed against the spec's own call.** §3(d) S4 writes `settle(margin, d_A, d_B, stakes)`; positionally `d_A` lands on `floor_b`. A floor *on A's share* can only come from A. Renamed `floor_a`, with the coordinate system stated once (§5). (b) **`stakes` is read by no line of the body** once `terms` is cut (§7's hunt) — and a declared parameter nothing reads is the exact defect `proposals/2026-09-02-executable-architecture/hole_register.yaml` H-89 registers against `verb_table.yaml`'s `scale:` column. Cut. (c) `Refusal` carries **one** kind here: `Refusal(scope)` and `Refusal(depth_cap)` in the spec belong to the gate and the seam (`04_CODE_ARCHITECTURE.md:520 §C.2`, `:677 §C.5`), not to a pure function. |
| 9 | both commitments are made as **each actor's own `commit` act** | **REFUTED. Two `commit` Tenures is the wrong model, and it fails for two independent reasons — one of which has nothing to do with any ruling.** | **(i) The gate refuses it.** `commit` is a Tenure kind (`04_CODE_ARCHITECTURE.md:475`), so `§C.2` F3 fires: `kind is Tenure => actor == subject(id)` … `otherwise raise NotYours` (`:529-534`). A's act cannot write B's commit edge. **(ii) And if B acts instead, it is an actor-hash coin flip.** `canonical_order` is `(stratum, actor-hash, intra-person position)` (`:576`) and `PART D` row 36 (`:857`) states *"rank never breaks a tie"* — so **nothing orders A's act before B's conditional commit**, and roughly half the time B's `requires` is evaluated against a world where the deal does not yet exist and the bargain silently fails to bind **for a reason nobody chose**. That is broken independently of Jordan's ruling. Both findings are the spine's, re-derived here from the same lines: `01_SPINE.md:760-776`. **The model that works is one `Record` naming both parties** — `write_matrix.yaml:243 Record.exists` carries no ownership clause, `treaty.py:63 TreatyRecord.parties: tuple` already has the shape, and `§B.4/§B.5` (`:249-261`) already folds `Petition`/`Dispensation` into Record kinds. §4 S5, §11. |
| 10 | `register_treaty` is "FA-owned; existing" | **AMENDED — existing, and self-declared scaffolding.** | `treaty.py:145-147` docstring, verbatim: *"Test/scaffolding helper: directly insert a treaty without going through `propose_treaty` (which is canon-gated). Used until Pass 2h lands and the proposal protocol becomes the supported insertion path."* The canon path is a stub: `treaty.py:99 propose_treaty` returns `stubwire.stub_resolve(...)` (`:113`). Writing settlements through `register_treaty` is writing through a declared placeholder — legitimate today, and it must be named rather than cited as the supported path. |
| 11 | `TreatyRecord.bound_season` and `LedgerTag.ttl` make I-N5 ("a settlement has a term") **STRUCTURAL by signature** | **REFUTED.** | `TreatyRecord.bound_arc/bound_season` (`treaty.py:65-66`) record **when the treaty was bound**, not when it ends; expiry is a 0.90 lapse roll at each arc boundary (`treaty.py:121 process_treaty_expirations`, `:42 TREATY_LAPSE_RATE_DEFAULT`), which is a stochastic sweep, not a declared term. `LedgerTag.ttl` (`ledger.py:41`) defaults to `None`, and `None` means **durable forever** (`ledger.py:16-17`, `:44 is_expired`). Both signatures happily express a termless settlement. I-N5 is **CONVENTION** unless the write path refuses `ttl=None` for `kind="Debt"` — an SE-owned change this branch does not propose. Regraded in §8. |
| 12 | the outcome enum "already has `compromise`/`stalemate`" | **CONFIRMED in the registry; AMENDED in the producer.** | `engine/engine_params/key_types.json:958` declares `outcome # initiator_win \| target_win \| compromise \| stalemate` for `scene.contest_resolved`. But the one producer, `engine/cross_scale/echo_transport.py:114 _OUTCOME_BY_DEGREE["contest"]`, maps only `{Overwhelming→initiator_win, Success→initiator_win, Partial→compromise, Failure→target_win}` — **`stalemate` has no producer anywhere in the tree**, and the Key fires at all only when `er.fires and … er.delta != 0` (`echo_transport.py:424`). A refused negotiation emits nothing today. |
| 13 | `persuasion_track_final: margin` in the emitted payload | **AMENDED — declared, not produced, and on a different scale.** | Declared optional at `references/KEY_INDEX.md:822` and `key_types.json:962` as `persuasion_track_final # int -5..+5`. The producer's payload (`echo_transport.py:434-438`) carries `scene_id`, `outcome`, `participants` **only**. And the kernel's own track is 0–10 (`resolver.py:87 PersuasionTrack.track`) while `margin` is an unbounded float — three scales for one field. §6 states the mapping rather than assuming it. |
| 14 | `HANDOFF_NEXT.md:57` 2e — no `bargain` verb; `utter` + `commit` compose | **CONFIRMED, verbatim** | `proposals/2026-09-03-meta-architecture/HANDOFF_NEXT.md:57`: *"⚠ **test composability first** — `utter` a counter-`OUGHT` + `commit` may already express it. Adding a verb is the last resort, not the first"*. This branch adds no verb. |
| 15 | the SC lane's `next_free` "could not be located by grep" (`00_BRANCH_SHAPES.md` §6) | **REFUTED — it is there.** | `references/id_reservations.yaml:195`: `SC: { name: "Social contest", next_free: 33 }`, with the note that block `0017-0020` was released 2026-07-30 (ED-IN-0098) and max allocated is `ED-SC-0016`. Allocate `ED-SC-0033` from that row and bump; never max+1. |

**Also found, each anchored, none padded.**

- **`support` is the live shape of the retired SC4 dominance question.** `resolver.py:350-351`: `support` spends 2 (`primitives.py:51 COST`) and regroups +4 (`:52 REGAIN`), builds ethos, and **accrues no fault** — a net +2 reserve per move with a standing gain. `pass`, by contrast, accrues `fault.yields` toward the silence clinch (`resolver.py:345-348`). In a 1–3 exchange budget this is the branch's one real dominance risk (§10).
- **The flow skeleton's `build_contest` anchor has drifted.** `social_contest_flow_skeleton_v1.md:17` cites `wrapper.py:106 build_contest`; the `def` is at `wrapper.py:110`. The skeleton records its trace commit as `6545067`. Harmless, reported so a reader does not conclude the anchor was fabricated.
- **`stubwire.StubResult` must not be reused for a refusal.** Its module-level invocation counter is read as a before/after delta by `tools/m1_acceptance.py` row 1 around a seeded probe season (`engine/substrate/stubwire.py:56-62`). A refusal returned as a `StubResult` would inflate the milestone instrument's stub count with a *built* behaviour saying no.
- **The seam already refuses this prize by name.** `proposals/2026-09-01-season-loop-tests/tracer/shape.py:4970-4977` raises `Unspecified` for `"a proposition"` — *"belongs to the `social_contest` subsystem (resolver: dice_pool), and nothing connects the seam to it"*. `hole_register.yaml:1016` H-88 records Jordan's ruling that naming-and-refusing **is** the intended behaviour for now. So this branch plugs a socket that exists and is deliberately empty.

---

## §2 · The conflict class, and why `agon` cannot resolve it

**The class.** A *mixed-motive, positive-sum division*: two parties jointly create a surplus that exists only if they agree, and then compete over how it is divided. The contest decides **the division**, not the winner — and both parties are better off at every point inside the bargaining range than at no deal.

**Why `agon` cannot, stated so it can be attacked.** The agôn path resolves on `PersuasionTrack` (`resolver.py:81`), whose entire state is one bidirectional scalar: `track(s) = clamp(start + scale·(adv[A] − adv[B]), 0, 10)` (`resolver.py:87`). Three consequences, each verifiable by reading that line:

1. **It is conservative by construction.** Every unit A gains, B loses. A positive-sum outcome — both sides ending better than they started — has no representation in a single difference.
2. **Its middle band is "nobody won", not "both gained".** `resolver.py:91` returns `"committee"` for `3 < t < 7`, and canon reads it as a partial narration (`social_contest_v30.md:279`) with the private case explicitly falling back to *"exchange majority determines winner. Tie = stall with consequences"*. A stall is not a bargain.
3. **The engine's own canon says so.** `social_contest_v30.md:702` files ZOPA resolution as *"structurally different from Persuasion Track, not designed"*, and `:679` gives Private Negotiation's tie the fail-forward stall.

**Is that enough to keep the row?** The legitimate opposite finding would be: *the leverage half already resolves, so delete the row and let `private_negotiation` be an ordinary `TallyAtClose` proceeding.* I take that seriously because it is the three-lens audit's own position — `04_reductive_audit_primitives_and_foundations.md:226` files `GAMES negotiation` inside **T4, "untracked private tally", *until `settle()` exists***, and `:334` says *"ABANDON THE FRAMING. Keep `settle()` as the one genuinely new build."*

**Verdict: delete the `GAMES` row, keep the branch.** These are not in tension, and conflating them is the misreading `00_BRANCH_SHAPES.md` §7.1 warns about. What is deleted is the *game*: `GAMES["negotiation"]` (`wrapper.py:242`) and `NegotiationMode` (`modes.py:342`). What is kept is a **terminal on a proceeding that already resolves** — `PROCEEDINGS["private_negotiation"]` with `burden: "NONE"` plus one pure function. That is the three-lens position implemented, not contradicted: *"negotiation is not a separate system — it is the gate with `burden = NONE`"* (`00_synthesis.md:344`), and `:354` *"'Private Negotiation = burden NONE' literally true, since it already resolves as `TallyAtClose`."*

So the honest one-line statement of this branch is: **one deletion, one row field, and one pure function.**

---

## §3 · Historical grounding, with tiers, and what canon licenses

Tiers are the corpora's own — `[PRIM]` primary text, `[REF]` reference-grade, **T0** primary scholarship, **T1** authoritative synthesis. `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:367` §9.7 binds every row: **history validates the *structure*, never the *numbers*.** No constant in §5 is taken from a source below.

| source | tier | what it licenses here | what it does **not** |
|---|---|---|---|
| **Kauṭilya, *Arthaśāstra*** — envoys (*dūta*) typed by latitude: *nisṛṣṭārtha* plenipotentiary · *parimitārtha* limited brief · *śāsanahara* message-bearer; the four *upāya* (*sāma* conciliate → *dāna* gift → *bheda* divide → *daṇḍa* force); the six *ṣāḍguṇya* under *maṇḍala* geometry (`research/…rhetoric_oratory_contest_research.md:225-228`, §5.4) | `[PRIM]` | That **who may bind whom is a typed property of the envoy's office, not of the person** — which is `Act.via : SeatId?` plus the seat's remit, an object PR #362 already owns (`04_CODE_ARCHITECTURE.md:392 §B.9`). §7 uses this to CUT a `latitude` parameter rather than to add one. | Any ladder of instruments as *Move kinds*. The four *upāya* are acts at the act layer (`utter`, a gift as a `transfer`, `bheda` as a separate contest), not new `VALID_KINDS` (`resolver.py:34`). |
| **Han Feizi, *Shuinan*** — the difficulty is reading the listener's **concealed heart**; the same true offer wins favour or gets you executed (`…research.md:181`, §4.2) | `[PRIM]` | That the counterparty's reservation is **hidden from the other party and known to the engine** — which is exactly the `Dossier` hidden-weight idiom already built (`primitives.py:283 EvidenceItem`, `:291 Dossier`; the view exposes a *count*, `contract.py:66 evidence_available`). This is why the ZOPA test is mechanical and the *bet* is the player's. | Any covert-influence subsystem. §9.4 of the same corpus flags the dyadic/public split as an open Jordan question (`…research.md:355`); this branch does not answer it. |
| **Callières, *De la manière de négocier avec les souverains* (1716)** — negotiation as patient relationship-building and **reputation**; "the secret of negotiation is to harmonise the interests of the parties" (`…research.md:321`, §8.3) | `[REF]` | That a settlement is a **durable record with a reputational afterlife**, not a one-scene stat delta — the `LedgerTag(kind="Debt")` composition (`ledger.py:12`, `:30`). §9.6 (`…research.md:363`) names Kauṭilya's grammar and Callières' model as *the two anchors* for any treaty design. | Any coefficient. §9.6 closes with *"[Anchor set for future treaty design; no claim about current canon.]"* |
| **du Rosier / Barbaro / Gentili / Wicquefort** — the ambassador literature; ceremonial vs negotiation missions, short vs long legations (`…research.md:315-320`) | `[REF]` | The **asymmetric appeal is not negotiation** (`…research.md:325`, §8.4: *"contests with a different topology"*). Petition/*supplique*/*remontrance* stay out of this branch; §9.5 files them as a proposed, unauthorised subsystem. | Folding `personal_appeal` (`modes.py:517`) into this terminal. |
| **Nash (1950) · Schelling (1960) · Raiffa (1982) · Walton–McKersie (1965)** — the disagreement point; commitment as self-binding; reservation price / ZOPA; integrative vs distributive (`v30-snapshot-2026-06-28:designs/audit/2026-06-28-social-contest-deliberation-critique/source-research/deliberation-as-game-synthesis.md:186-196`, ledger `:296-302`) | **T0** | The *shape* of `settle()`: a disagreement point, two reservations, a range, and a division. Schelling supplies the reason a reservation must be **fixed before the deal and unadjustable during it** — a commitment binds by removing your own options. | Any solution concept. `settle()` does **not** implement Nash bargaining; it maps an exchange margin onto a canon-sourced share and clamps. Said plainly so nobody cites Nash for the arithmetic. |
| **Putnam (1988), two-level games / the win-set** — a deal binds only inside the set that survives ratification at home (`…deliberation-as-game-synthesis.md:194`) | **T0, tier-flagged by the corpus itself: *"Putnam is scrupulous that this is 'a metaphor', not a finished formal theory"*** | The counterparty's floor **is** their win-set, collapsed to one number. Under Jordan's in-scene ruling (§11) Level II is not a later ratification stage; it is a **precondition read at the moment of settling**. The metaphor survives; the two-season staging does not. | A ratification *act*. §11. |
| **Parliament as supply-for-redress** (`…/politics-as-deliberative-game.md:173` model 8; `:217`: *"a parliament is fully a game in the game-theoretic sense … precisely where it is least a zero-sum contest, because supply-for-redress is a positive-sum bargain in which both sides can gain"*) | **T0/T1** | The positive-sum argument of §2, in the corpus's own words. | Anything about the vote itself — that is `04_CONSENSUS.md`'s lane. |
| **Diplomacy (1954)** — a negotiation phase, then simultaneous execution, with **no mechanism whatever for enforcing an agreement**; *"This must be the default, with binding instruments as the expensive exception. A world where treaties bind automatically has no diplomacy in it."* (`research/valoria_game_precedent_companion_v1.md:491-493`) | game precedent | The strongest counter-pressure on this branch, and it is handled rather than dodged: §11's ruling binds **the agreement reached**, it does not make it self-enforcing. `repudiate` (`proposals/2026-09-02-executable-architecture/verb_table.yaml:378`, `requires: "a live commit exists"`, `writes: ["Tenure.until"]`, `emits: ["commitment.ended"]`) is the defection path and it costs an act and an Event. | Automatic enforcement. If a later pass makes a settlement unbreakable, this precedent is the falsifier. |
| **Machiavelli (the *Diplomacy* variant)** — bribery as an **explicit legal action** (`…companion_v1.md:501`) | game precedent | A gift (*dāna*) is an Act, not a cheat — so a side payment enters through `transfer`, outside this terminal. | A `bribe` verb. |
| **`mixed-motive FG-1/FG-2`** (`v30-snapshot-2026-06-28:…/critique.md:83-84`) — "add a Negotiation mode as a **parameterization of the existing contest, not a new engine** … a deal in the overlap pays each side its split via the §7.2.1 track-distance weighting … *zero new engine*"; and "Putnam's two-level game is absent … give each member a **win-set**" | sound/high, verifier-corrected — and **PROVISIONAL** here (§12.4) | Directly: this branch *is* FG-1, minus the Recruitment-Offer import (which FG-3's own verifier note downgrades). FG-2's win-set becomes the reservation. | FG-1's "Offer table" import — `npc_behavior §9.5` was not read this session and the critique's own FG-3 note corrects a sibling claim about it. Not carried. |

**What canon licenses, and where it stops.**

- `social_contest_v30.md:101-107` — Private Negotiation is a real proceeding: 1–3 exchanges, symmetric, no adjudicator, no resistance, tracker optional. The venue exists in canon and in code.
- `social_contest_v30.md:310` — a binding **Obligation** is canon's own name for a settlement, and it is produced by *"A Decisive win … in a Formal or Grand Contest"*. **Private Negotiation is not in that list**, and `:312-318`'s duration table has no row for it. So canon gives this venue a resolution and denies it a terminal — precisely the gap.
- `social_contest_v30.md:323` — an Obligation **TRANSFERS to the relevant faction/institution** on death or collapse: *"the institution remembers the commitment"*. That is a `Record` in PR #362's sense (`01_AXIOMS.md:857 §D.4`, *"the fact that can leave the head that holds it"*), not a belief. It is why §4 writes one Record rather than two Tenures.
- `social_contest_v30.md:325` — Wager Obligations are **valid only in Grand Contests** with Projection genre + Consequence style. This closes a fork I was about to open (§11 fork 4): no Wager right at Overwhelming in a private negotiation.
- `canon/02_canon_constraints.md:23` **P-14** — every play mode must express three-dimensional co-movement. A settlement is a thread operation's consequence like any other: it emits `scene.contest_resolved` into the same Key path (§6), so the co-movement is the existing one and this branch adds no bypass.
- `canon/02_canon_constraints.md:10` **P-01** — no mechanic may resolve without its automatic co-movement effects. A refused negotiation must therefore still *emit*; §6 makes the refusal emit rather than vanish.

---

## §4 · THE SEQUENCE

Idiom: `systems/_architecture/subsystem_flow_skeletons_v1.md:94` — numbered steps, branches nesting one level, each tagged `[gate] [branch] [loop] [emit] [write]`, each naming what it reads, what it writes, and **who owns the write**. Owner is SC unless marked.

```
S0  [gate] OPEN — resolve the two reservations, ONCE, at the seam boundary
      reads:  floor_a  = the largest share of the stake A will concede to B, read as A's floor
              ceil_a   = the largest share of the stake B will concede to A, read as A's ceiling
              source (PR#362 shape): Tenure.degree, the degree at which each party already
                                     committed to the OUGHT at issue
                                     -- write_matrix.yaml:329 Tenure.degree, by DR-2
              source (live tree):    NEITHER EXISTS. The caller supplies both, and the one
                                     production caller does not -- scene_dispatch.py:300
                                     calls build_contest(parts[0], parts[1], venue=proceeding)
                                     and nothing else. THIS IS THE BRANCH'S REACHABILITY GAP.
      writes: nothing
      owner:  the caller (IN lane at the seam; PR#357 rosters for the derivation)
      why ONCE, and why here: §C.5.1's roster contract -- the sides and their stakes are
              resolved from the frozen projection before provider.run, so a reservation cannot
              move mid-contest.  04_CODE_ARCHITECTURE.md:699 §C.5.1

S1  [write] UTTER — A utters the proposition the deal is about
      verb:   utter -- verb_table.yaml:475, writes ["Proposition.exists"], grade "assumption"
      reads:  nothing of B's
      writes: Proposition (IMMUTABLE -- write_matrix.yaml:231-241, "§14 -- there is no write")
      owner:  A, through the gate; A is the actor (AX-1)
      note:   the deal's TERM lives in the Proposition A uttered. It is authored, not defaulted,
              which is why §5 invents no duration constant.

S2  [loop <= exchanges(1,3)] THE LEVERAGE BOUT -- unchanged, already built
      Bout(private_negotiation, burden=NONE, adjudicator=no_adjudicator)
                                                    modes.py:513; resolver.py:238 Bout
    S2.1 [branch] each exchange, each side: a Move in VALID_KINDS -> _apply -> _reception
                  -> _advance                        resolver.py:34, :341, :283, :314
    S2.2 [gate]   DefeatCatalogue.check after each move; a hit clinches and ends the bout,
                  setting veto=True against the faulting side
                                                    primitives.py:272 check; resolver.py:53
    S2.3 [emit]   beats, when Bout(record=True)      resolver.py:238
      reads:  Contestant (spine's contestant_from_person), Dossier hidden weights
      writes: NOTHING. The bout holds no token and touches no persistent state.
      owner:  -- (SC kernel, transient per-Bout state only; SC_INVENTORY §D2)

S3  [branch] MARGIN AND BAND -- the spine, consumed not redefined
      margin = TallyAtClose.margin(state) = (adv[A] - adv[B]) / SUCCESS_UNIT
                                            01_SPINE.md:526 (A-positive already); resolver.py:62
               ⚠ WHOLE-D10-SUCCESS UNITS, and SUCCESS_UNIT is an uncalibrated [SEED]
                 (01_SPINE.md:503, :521). The raw `adv` difference is NOT on the ladder's scale --
                 the spine measured a unanimous 7-0 ballot banding as Partial (§1.3). Every band
                 edge quoted below inherits that [SEED].
      degree = degree_from_net(margin, ob=0, extension=...)        dice_engine.py:227
               margin >= 3 Overwhelming | >= 1 Success | [0,1) Partial | < 0 Failure
      ONE ladder. This branch adds no second banding.

S4  [gate] SETTLE -- the one new thing (§5)
      outcome = settle(margin, floor_a, ceil_a) -> Settlement(share) | Refusal("no_zopa")
      reads:  its three arguments and nothing else. No world, no Bout, no module state.
      writes: nothing. It is a Query.
    S4.1 [branch] Refusal("no_zopa")  -- floor_a > ceil_a; there was never a deal to be had
    S4.2 [branch] Settlement(share)   -- share = clamp(split(margin), floor_a, ceil_a)

S5  [branch] ON A SETTLEMENT -- ONE act, ONE write that binds both, in the scene
             (Jordan, 2026-09-04; the modelling is 01_SPINE.md §3.4 (iii))
    S5.1 [write] THE SETTLEMENT IS THE RECORD -- this is the binding write, not a side effect
                 one Record naming BOTH parties and carrying `share`; A's act is its author
                 person scale:  LedgerTag(kind="Debt", key=f"settle:{P.id}",
                                          value=share, created_season, ttl=P.term)
                                ledger.py:36 LedgerTag, :47 ledger_add, :30 TAG_KINDS
                                applied via registry.py:102 Settlement.tag
                                owner: SE (systems/settlements) -- SC returns, SE writes
                 faction scale: register_treaty(parties=(A,B), terms, bound_arc, bound_season)
                                treaty.py:145 -- owner: FA. ⚠ self-declared scaffolding (§1 row 10)
                 ⚠ A RECORD IS NOT A TENURE, so the gate's AX-4 clause 2 never fires
                   (04_CODE_ARCHITECTURE.md:529-534); write_matrix.yaml:243 Record.exists
                   carries no ownership clause. B is bound by being a NAMED PARTY to the
                   document, not by an edge somebody else wrote. One act. One write.
                   No nesting, no DELIBERATE reacting to RESOLVE, no order fragility.
    S5.2 [write] A: commit(P) -- A's OWN edge, A's own act, in the same fold
                 verb commit -- verb_table.yaml:92, eligibility ["own"], writes ["Tenure.since"]
                 gate clause satisfied: actor == subject(id)   04_CODE_ARCHITECTURE.md:530
                 ⚠ THIS IS NOT A SECOND OWNER OF THE SETTLEMENT. Its one job is to give A a
                   breach path: `repudiate` requires "a live commit exists" and writes
                   Tenure.until (verb_table.yaml:378-383). Cut it and A's defection is mere
                   non-performance -- no act, no Event, no author -- which is precisely the
                   loss §11 cost 1 says the ruling must not incur.
                 ⚠ AND IT IS ASYMMETRIC. B has no Tenure and therefore no `repudiate`.
                   B's durable duty needs B's own `oblige` in this or a later season
                   (01_SPINE.md §3.4 (iii) 2); until then B is bound documentarily only.
                   This is the sharpest price of one-act binding. §11 cost 4.
    S5.3 [emit]  commitment.made                     verb_table.yaml:97
    S5.4 [emit]  scene.contest_resolved{outcome, persuasion_track_final}   §6
                 echo_transport.py:371 emit_scene_echo -> :427 Key(...)
                 ⚠ WHEN it takes effect is I-S6b, which the live tree does NOT satisfy:
                   the echo's apply is deferred to accounting_boundary (keys.py:569-573,
                   OF-7). Owner: IN lane. 01_SPINE.md §1.9 (b) and its §7.4 falsifier.

S6  [branch] ON A REFUSAL -- the act refuses; nothing binds
    S6.1 [emit]  commitment.refused                  verb_table.yaml:98 emits_on_refusal
                 -- ALREADY DECLARED. This branch adds no refusal kind.
    S6.2 [emit]  scene.contest_resolved{outcome: "stalemate"}
                 ⚠ `stalemate` is declared (key_types.json:958) and has NO PRODUCER today
                   (echo_transport.py:114 _OUTCOME_BY_DEGREE). §6 adds the row.
    S6.3 [write] LedgerTag(kind="Grudge", key=f"nozopa:{A}:{B}:{P.id}", ttl=P.term)
                 ⚠ WATCHED, NOT ASSERTED -- see §7's E-ratio table. Under PR#362 this is a false
                   N-line (the refusal Event carries it); in the live tree, which has no WITNESS
                   and whose echo does not fire on a stalemate, it is the ONLY durable trace.
                 owner: SE
    S6.4 [gate]  Let It Ride blocks re-opening until circumstances change
                 social_contest_v30.md:680 -- an existing contest-level rule, not a new clock
```

**What is new in this sequence:** exactly `S4`. `S0` is a caller derivation that does not exist yet. `S1`, `S2`, `S3`, `S5.1`, `S5.3` are existing verbs, an existing bout and an existing ladder. `S5.2`, `S6.3` are existing SE/FA write paths. `S5.4`, `S6.2` are an existing Key with one missing enum row.

---

## §5 · THE SHAPE

### 5.1 The module, and why its dependency list is load-bearing

```python
# systems/social_contest/sim/contest/settle.py
"""settle.py — the NEGOTIATION TERMINAL. One pure function: an exchange margin and two
   reservations in, a division of the stake or a typed no-deal out. No world access, no
   package state, no randomness.

   ⚠ THIS MODULE MUST NOT IMPORT ANY SIBLING THAT REACHES THE PACKAGE NODE.
   `contest/__init__.py`, `dictionaries.py` and `wrapper.py` are the three nodes of the
   package's reported import cycle (they are the only files using the `from . import X`
   form, which structure_audit.py:312-325 resolves onto the package itself). Importing
   `dictionaries` or `wrapper` from here would enlarge the 9-module SCC that
   tests/valoria/test_import_cycle_game_state_npe.py:23 hard-codes, breaking a live blocking
   test as a side effect of adding a leaf. `contract.py` and `primitives.py` are safe —
   they are imported by `__init__` and are NOT in the reported cycle. Falsifier: F-N6.
"""
from dataclasses import dataclass
from engine.autoload.dice_engine import Degree, degree_from_net
```

`dice_engine` is an upward dependency on `engine/`, the same edge `resolver.py:24` and `primitives.py:9` already carry. Nothing else is imported.

### 5.2 Types

```python
@dataclass(frozen=True)
class Settlement:
    """A struck bargain. `share` is A's fraction of the divisible stake, in [0.0, 1.0];
       B's is 1.0 - share. Carries nothing else: the degree is the caller's (it already
       has the margin and the one ladder), and whether the share was set by the margin or
       by a reservation is derivable as `share != split(margin)`."""
    share: float


@dataclass(frozen=True)
class Refusal:
    """No deal was available. ONE kind: the reservations do not overlap. `Refusal(scope)`
       and `Refusal(depth_cap)` in 00_BRANCH_SHAPES §3(e) belong to the write gate
       (04_CODE_ARCHITECTURE.md:520 §C.2) and the seam (:677 §C.5); a pure function cannot
       raise them and must not claim them."""
    kind: str = "no_zopa"
    reason: str = ""
```

### 5.3 The split rule — the exact arithmetic

**The coordinate system, stated once so it cannot drift.** Every bound and every share is **A's fraction of the divisible stake**, in `[0.0, 1.0]`. B's fraction is `1.0 - share`.

- **`floor_a`** — the smallest A-share **A** will accept. Below it A walks. It is A's reservation.
- **`ceil_a`** — the largest A-share **B** will accept. Above it B walks. It is B's reservation, written as a ceiling on A.
- The **ZOPA** is `[floor_a, ceil_a]`, and it is empty iff `floor_a > ceil_a`.

```python
# The three ratios are CANON, not invented: social_contest_v30.md:421-423 (ED-762), the
# §7.2.1 track-distance split. The KEYING is re-derived — see §1 row 6 for why the canon
# keying (track 4 -> 0.60, 5 -> 0.55, 6 -> 0.50) is anti-monotone on A's side and awards a
# dead tie 55% to A, and why canon's own stated principle ("track-distance weighting",
# :415) demands the symmetric reading. Marked [DERIVED], not [SEED]: no number is invented,
# one assignment is corrected.
#
# ⚠ BUT THE BAND EDGES ARE [SEED], AND THEY ARE NOT MINE. The keys are Degrees, and which
# Degree a given `adv` difference reaches depends on TallyAtClose.SUCCESS_UNIT, which the
# spine ships uncalibrated and tagged [SEED] (01_SPINE.md:503, :521, :526). So: the three
# SHARES are canon and exact; WHERE ONE SHARE GIVES WAY TO THE NEXT is unmeasured. Calibrate
# with tools/balance_oracle.py, per the spine — never by argument, and never here.
SHARE_BY_DEGREE = {                 # the winner's share, by how decisive the exchange was
    Degree.PARTIAL:      0.50,      # |margin| in [0, 1)   — even split
    Degree.SUCCESS:      0.55,      # |margin| in [1, 3)
    Degree.OVERWHELMING: 0.60,      # |margin| >= 3
}
# Degree.FAILURE is deliberately absent and is UNREACHABLE: degree_from_net(abs(m), 0.0)
# has margin >= 0 by construction, and dice_engine.py:281 returns FAILURE only below 0.
# This is 04_CODE_ARCHITECTURE.md:620's rule applied — "a verb may not declare a band its
# subsystem cannot report" — read here as: the table declares three rows because three is
# what abs() can produce, and does not invent a fourth.


def split(margin: float) -> float:
    """A's share before reservations. SYMMETRIC BY CONSTRUCTION: split(-m) == 1 - split(m)
       for every m, including m == 0 (which yields 0.50 from both arms). Monotone
       non-decreasing in margin. Both properties are exact identities, not tolerances —
       falsifier F-N2 asserts them with no [SEED]."""
    lead = SHARE_BY_DEGREE[degree_from_net(abs(margin), 0.0)]
    return lead if margin >= 0.0 else 1.0 - lead


def settle(margin: float, floor_a: float, ceil_a: float) -> "Settlement | Refusal":
    """The negotiation terminal.

    margin  — the bout's TallyAtClose margin, adv[A] - adv[B], in success units.
    floor_a — A's reservation, as A's share of the stake. A walks below it.
    ceil_a  — B's reservation, as A's share of the stake. B walks above it.

    A no-ZOPA is a DESIGN OUTCOME and returns a Refusal. An out-of-range bound is a CALLER
    BUG and raises, matching the kernel's own convention for a malformed input
    (resolver.py:343 raises on an unknown Move.kind; :320 on an unknown appeal).
    """
    for name, v in (("floor_a", floor_a), ("ceil_a", ceil_a)):
        if not (0.0 <= float(v) <= 1.0):
            raise ValueError(f"settle: {name}={v!r} is not a share in [0.0, 1.0]")

    if floor_a > ceil_a:
        return Refusal("no_zopa",
                       f"floor_a={floor_a:.3f} > ceil_a={ceil_a:.3f}: no share satisfies both")

    return Settlement(share=min(ceil_a, max(floor_a, split(margin))))
```

### 5.4 The two decisions inside those six lines, and why each is right

**(a) Clamp into the ZOPA; refuse only when the ZOPA is empty.** The alternative — refuse whenever the margin-derived share falls outside the range — throws away deals both parties want. Nash's disagreement point (T0) says that where a range exists, the parties settle inside it; the margin decides *where*, and a boundary is the most the strong party can get. **The emergent consequence is the branch's best property: a stronger bargaining position can cost you the deal.** At `|margin| ≥ 3` the winner's share is 0.60; if that breaches the other side's reservation the ZOPA does not close (the *range* is unchanged) — the share is clamped back to the boundary. The ZOPA only closes when the two reservations genuinely cannot both be met, which is a fact about the parties, not about the roll. A weak-but-stubborn party (high `floor_a`) extracts more than their exchange performance warrants, right up to the point where nothing is left to agree on. That is Schelling's commitment, made mechanical, with a real cost attached.

**(b) `Refusal` is not a `veto`, and the difference is load-bearing.** The spine's `veto` channel exists for a clinch (`primitives.py:272 DefeatCatalogue.check`) and per `04_CODE_ARCHITECTURE.md:696` "the ladder takes the minimum". A no-ZOPA is not a demotion — it is the absence of a contest outcome, and PR #362's fold already routes it: `if row.contests: degree, evs = seam.contest(...)  # Refusal => emit refusal kind` (`04_CODE_ARCHITECTURE.md:582`). So:

| in-bout event | channel | effect |
|---|---|---|
| A contradicts himself / falls silent | `veto = True` (existing) | A's degree demotes; a settlement still happens, at worse terms |
| the reservations do not overlap | `Refusal("no_zopa")` | the act refuses; `commitment.refused` emits; nothing binds |

Collapsing them would make "I argued badly" and "there was never a deal" indistinguishable to every downstream consumer.

### 5.5 Registry and venue changes (data, not code)

| where | change |
|---|---|
| `modes.py:513 PROCEEDINGS["private_negotiation"]` | `+ burden: "NONE"`, `+ settle: True` (spine owns the `burden` field; this branch owns the two values) |
| `modes.py:342-350` | **DELETE `NegotiationMode`** and its `stub_resolve` body |
| `wrapper.py:242` | **DELETE** the `GAMES["negotiation"]` row (spine deletes `GAMES` entire; if the spine is deferred, this row goes alone) |
| `_kernel_tests.py:700-703` | the stub loop loses one of its three names; `_KERNEL_EXPECTED` (`engine/tests/test_contest_kernel.py:93`) moves by the net check count |
| `echo_transport.py:114 _OUTCOME_BY_DEGREE["contest"]` | `+ "stalemate"` as the refusal's outcome (§6) |
| `faction.py:107,117` | `succession` imports `split()` from `.settle` and deletes its own `leader`/`ratio` lines — **the duplicate band logic named LOW in `v30-snapshot-2026-06-28:designs/audit/2026-06-03-contest-groundup/AUDIT_RECONCILED.md`** |

**Every number in §5 is canon-sourced. There are no `[SEED]`s in `settle()`.** The one place this branch would have needed one — the settlement's duration — is avoided by putting the term in the Proposition A uttered (§4 S1), where it is authored rather than defaulted. The two `[SEED]`s that remain are outside `settle()` and are named in §9: F-N8's bout-symmetry tolerance, and the Grudge's `ttl` if the Proposition carries no term.

---

## §6 · Keys, state, ownership, the write path, and the degree-keyed column

### 6.1 Keys — zero new types

| Key | direction | what this branch does | anchor |
|---|---|---|---|
| `scene.contest_resolved` | emit | carries `outcome` and (new) `persuasion_track_final` | declared `key_types.json:954`; `KEY_INDEX.md:811`; produced at `echo_transport.py:427` |
| `state.opinion_revised` | consume | already declared consumed; unchanged | `references/module_contracts.yaml:746` |
| `scene.dialogue` | emit (optional) | unchanged; still has no construction site anywhere | `module_contracts.yaml:751`; `SC_INVENTORY.md` §C |

**Payload.** `outcome` takes `initiator_win | compromise | target_win` from the existing `_OUTCOME_BY_DEGREE["contest"]` map (`echo_transport.py:114`) — no change — plus **one new row, `stalemate`, for the refusal**, which the registry has declared since `key_types.json:958` and no producer has ever emitted.

**`persuasion_track_final` is declared `int -5..+5`** (`key_types.json:962`) while `margin` is an unbounded float and `PersuasionTrack.track` is `0..10` (`resolver.py:87`). The mapping this branch proposes, stated rather than assumed: `round(max(-5.0, min(5.0, margin)))`. The bounds are the registry's; the rounding is a transcription choice and is flagged as such. If the spine settles the scale collision differently, this line follows the spine.

### 6.2 State changes and who owns each write

| what is written | owner | path | grade of the ownership claim |
|---|---|---|---|
| **the settlement — one `Record` naming both parties** | **SE** (person scale) / **FA** (faction scale) | `registry.py:102 Settlement.tag` → `ledger.py:47 ledger_add`; or `treaty.py:145 register_treaty` (⚠ self-declared scaffolding, §1 row 10) | live today. **A Record is not a Tenure**, so `AX-4` clause 2 (`04_CODE_ARCHITECTURE.md:529-534`) does not fire |
| `Proposition.exists` | A (the actor) | `verb_table.yaml:475 utter` → the gate | PR #362 shape only; no live equivalent |
| `Tenure.since` on **A's own edge only** | A | `verb_table.yaml:92 commit` → the gate; `actor == subject(id)` satisfied (`:530`) | PR #362 shape only. Its job is the breach path, not the settlement (§4 S5.2) |
| `LedgerTag(kind="Grudge")` on refusal | **SE** | as the settlement's person-scale path | live today; **watched, medium confidence** (§7.3) |
| a `Faction` stat delta | IN | `echo_transport.py:441 _apply` → `game_state.py:153 Faction.adjust` | live today, unchanged. **Timing is I-S6b's, not this branch's** |

**No `Tenure` edge belonging to the counterparty is written anywhere on this path.** That is the whole content of the compliance argument, and it is checkable by reading the writes column above: one Record, one self-edge, one stat delta.

**`systems/social_contest/` writes nothing persistent in this branch, and that is checkable.** The package's one persistent write today is `parliamentary_vote.py:214` (`SC_INVENTORY.md` §D1), on a different path. `settle()` is a Query; the wrapper returns a value; every write above is somebody else's. This is `04_CODE_ARCHITECTURE.md:164`'s `seam/wrappers/* — owns nothing, ever` satisfied by the current tree rather than by a promise.

**The dedupe hazard, named because it silently destroys settlements.** `ledger_add` dedupes by `(kind, key)` and **refreshes in place** (`ledger.py:53-56`). Two Debts between the same parties with the same key overwrite each other. The key must therefore carry the Proposition id: `f"settle:{P.id}"`, not `f"settle:{A}:{B}"`. Invariant I-N6, falsifier F-N7.

### 6.3 The degree-keyed consequence column — and the finding it produces

Per `04_CODE_ARCHITECTURE.md:573 §C.4` / F6, a verb declaring `contests:` keys its `writes` **and** its `emits` on the Degree, and the loader asserts the two key sets are equal (`:644`). The column lives **on the calling verb, never in the seam** (`:694`, "a state write from inside — no token, STRUCTURAL"). The verb here is `commit` (`verb_table.yaml:92`), which gains `contests: "a proposition"` — the prize `rosters.yaml:360` already maps to `social_contest`.

```yaml
  - verb:        "commit"
    contests:    "a proposition"           # NEW — routes to the seam at RESOLVE
    writes:
      Overwhelming: ["Record.exists", "Tenure.since"]
      Success:      ["Record.exists", "Tenure.since"]
      Partial:      ["Record.exists", "Tenure.since"]
      Failure:      ["Record.exists", "Tenure.since"]
    emits:
      Overwhelming: ["commitment.made"]
      Success:      ["commitment.made"]
      Partial:      ["commitment.made"]
      Failure:      ["commitment.made"]
    emits_on_refusal: ["commitment.refused"]   # unchanged — already declared at :98
```

**`Record.exists` is first in every row because it is the binding write; `Tenure.since` is A's own edge and exists to give `repudiate` something to close** (§4 S5.2). **Why `commit` and not `oblige`**, since `oblige` (`verb_table.yaml:336-343`) is the semantically apter verb for taking on a duty: `oblige` has an opener and **no closer** — the defect `HANDOFF_NEXT.md:54` 2a registers, which it names as blocking *"breaking a treaty"* explicitly — and it carries `emits_on_refusal: []`, so a refused negotiation would produce no Event at all, violating P-01 (`canon/02_canon_constraints.md:10`). `commit` has both. Chosen on the registered defect, not on preference; if `release` (`04_CODE_ARCHITECTURE.md §A.3` row 14) lands, revisit.

⚠ **THE FOUR BRANCHES ARE IDENTICAL, AND THAT IS THE RESULT, NOT AN OVERSIGHT.** `writes_at(degree)` was built to fix `kill / wound`, where losing the fight wrote the same fields as winning it (`04_CODE_ARCHITECTURE.md:606-608`; the landed row at `verb_table.yaml:282-285` now reads `Felled / Wounded / Untouched`). **Negotiation is the case that shows the repair is not universal: here the degree changes the *value* written, not the *set of fields*.** Every band that reaches the column is a struck bargain; what differs is the `share` in the Record's `value`, which rides in the gate receipt's change, not in the field list. There is no `Failure: []` because there is no losing *outcome* — a negotiation that produces nothing produces a **refusal**, which the fold handles on the `emits_on_refusal` path with no writes at all.

By PR #362's own rule — *"the verb declares fewer branches rather than the table inventing the difference"* (`:621`, Jordan-ruled 2026-09-03) — the honest column for this verb is therefore the **flat list**, and the four-band form above is written out only to show that it collapses. The generalisation this branch offers back to the meta-architecture, in one sentence: *a contested verb varies either its field set or its written value by degree, and the sixth column only expresses the first.* That verdict belongs to `01_SPINE.md`; it is flagged here and not adjudicated.

---

## §7 · Reuse ledger, and the false-N-line hunt over my own additions

### 7.1 What this composes on (nothing here is authored by this branch)

| composed object | anchor | role |
|---|---|---|
| `Bout` + the exchange loop | `resolver.py:238`, `:440 resolve` | the leverage half, unchanged |
| `TallyAtClose` | `resolver.py:62` | `burden = NONE` — the win-condition `private_negotiation` already uses |
| `PROCEEDINGS["private_negotiation"]` | `modes.py:513` | the venue: 1–3 exchanges, symmetric, no adjudicator |
| `DefeatCatalogue.check` | `primitives.py:272` | the clinch → `veto` |
| `Dossier` / `EvidenceItem` | `primitives.py:291`, `:283` | the hidden-weight idiom the reservation reuses |
| `degree_from_net` | `dice_engine.py:227` | the ONE ladder; `settle` calls the owner and never re-bands |
| `Degree` | `dice_engine.py` | the three reachable members are the split table's keys |
| `utter` / `commit` / `repudiate` | `verb_table.yaml:475`, `:92`, `:378` | open, bind, defect — no new verb (`HANDOFF_NEXT.md:57` 2e) |
| `LedgerTag` kinds `Debt`, `Grudge` | `ledger.py:30` | zero new tag kinds |
| `ledger_add` / `ledger_sweep` | `ledger.py:47`, `:69` | the SE write and expiry path |
| `TreatyRecord` / `register_treaty` / `process_treaty_expirations` | `treaty.py:62`, `:145`, `:121` | the FA-scale instrument |
| `emit_scene_echo` + `scene.contest_resolved` | `echo_transport.py:371`, `key_types.json:954` | zero new Key types |
| the §7.2.1 ratios | `social_contest_v30.md:421-423` | the three shares |
| `Let It Ride` | `social_contest_v30.md:680` | the re-open block after a refusal |

### 7.2 What is new — four objects, each with its N-line

| new | N-line: *cut it, and the emergent possibility lost is…* | can anything ruled in supply it? |
|---|---|---|
| **`settle()`** | …a positive-sum division. Without it the bout's margin becomes a winner, the 4–6 band stays "nobody won" (`resolver.py:91`; `social_contest_v30.md:279`), and the one thing negotiation is — *both parties end better than they started* — has no representation anywhere in the engine. | **No.** Checked against `resolver.py`'s six win-conditions (all return a side or a band), `armature.py` (a δσ leverage shift), `ledger.py` (a store, no arithmetic), `treaty.py` (a store plus a lapse roll), and `faction.py:117` (a division — for succession only, and side-asymmetric). The three-lens audit reached the same conclusion independently (`00_synthesis.md:462`). |
| **`SHARE_BY_DEGREE`** | …any reward for winning the exchange. Cut it and every settlement is 50/50, which makes the entire bout inert — the strongest possible argument buys exactly what silence buys. | **No.** The values exist in canon prose (`v30:421-423`) and in `faction.py:117`, but §1 row 5 shows `faction.py` is the wrong owner and §1 row 6 shows its keying is wrong. |
| **`Settlement` / `Refusal`** | …the caller's ability to tell a struck bargain from no bargain without a sentinel value. | **No** — and reusing `stubwire.StubResult` for the refusal would corrupt `tools/m1_acceptance.py` row 1's stub-hit delta (`stubwire.py:56-62`). |

### 7.3 THE FALSE-N-LINE HUNT — run against my own additions

`14_NERS.md` §3's pattern, quoted so the test is the source's and not mine: *a mechanism was named, a **store** was proposed for it, and the store's job was already being done by an object the design had ruled in.* Ten candidates, **seven cut**, one kept-conditionally, two survived.

| candidate | its claim | verdict |
|---|---|---|
| **a second `commit` Tenure, on the counterparty** *(the shape spec's S5.2, and my own draft before the spine's verdict)* | both parties must be bound, so both must hold a commit edge | **CUT, and it is the most consequential cut in this document.** The Record does the job — one write naming both parties (`write_matrix.yaml:243`, no ownership clause; `treaty.py:63 TreatyRecord.parties`), which is `§B.4/§B.5`'s own precedent for `Petition`/`Dispensation` (`:249-261`). And the store fails on its own terms twice: the gate refuses it (`:529-534`) and the fold cannot order it (`:576` + `D-36 :857`). §1 row 9 |
| **A's own `commit` Tenure** | A must be bound too | **SURVIVED, on a narrow N-line that is not "binding".** The Record already binds A. What the self-edge uniquely provides is a **breach path**: `repudiate` requires *"a live commit exists"* (`verb_table.yaml:381`). Cut it and A's defection has no act, no Event and no author — the loss §11 cost 1 says the ruling must not incur. Nothing else in the tree closes a commitment visibly |
| **`terms: dict` on `Settlement`** *(my own first draft)* | a settlement divides several axes, so the terminal must return a term map | **CUT.** The claimed possibility is the critique's `four-games FG-1` *proportional trade* — "genre-won attribution decides who keeps which axis" (`critique.md:85`). `settle(margin, floor_a, ceil_a)` has **no per-axis input**, so it cannot produce a trade; what it *could* produce is one `share` multiplied across every axis, which is one multiplication the caller already owns. A store for a fact the function cannot compute. |
| **`stakes: Stakes` parameter** | the terminal needs to know what is being divided | **CUT, as a consequence.** Once `terms` is gone, no line of the body reads it. That is exactly the defect `hole_register.yaml:1029` H-89 registers against `verb_table.yaml`'s `scale:` column — *"a declared axis that decides nothing"*. A reservation stated as a *share* is scale-free, so the pie's size is not needed. |
| **`latitude` (the Kauṭilyan `dūta` ladder) as a `settle()` parameter** | plenipotentiary vs limited-brief vs message-bearer must be typed somewhere | **CUT.** Its job is done by `Act.via : SeatId?` plus the seat's remit (`04_CODE_ARCHITECTURE.md:392 §B.9`; `01_AXIOMS.md:1356 §E.2.2` — *"authority is a property of the seat being exercised"*). Putting it on `settle()` would be a second owner of an authority fact. **And the honest consequence: `rosters.yaml:102 remit_acts` is `[issue, determine, confer, revoke, dispatch, convene]` — no `commit` — and `commit`'s eligibility is `["own"]` (`verb_table.yaml:94`). So no envoy can bind a principal today, and under §11's ruling a negotiation binds only between principals present in the scene.** Named, not routed around. |
| **a reservation FIELD on `Contestant`** | the walk-away point needs a carrier | **CUT** — the shape spec cut it first and I re-ran the cut rather than inheriting it. `Contestant` (`resolver.py:180`) is an immutable per-bout spec that is explicitly reusable across bouts; a reservation is a per-*matter* fact. `Tenure.degree` (`write_matrix.yaml:329`) is the declared carrier; the concealment idiom is `Dossier`'s (`primitives.py:291`, exposed as a count at `contract.py:66`). |
| **`offer` / `concede` Move kinds** | bargaining needs bargaining moves | **CUT** — re-verified. `VALID_KINDS` (`resolver.py:34`) is a closed tuple validated at `resolver.py:342`; an offer is an utterance of a different OUGHT (`verb_table.yaml:475`), which is an Act, not a Move inside the bout. `HANDOFF_NEXT.md:57` 2e forbids the verb until composability is tested; this branch tests it and it composes. |
| **`clamped: bool` on `Settlement`** *(my own second draft)* | you cannot tell a deal set by the margin from a deal set by a reservation | **CUT.** Derivable: `share != split(margin)`, from three values the caller already holds. A stored aggregate where a Query suffices. |
| **`LedgerTag(kind="Grudge")` on refusal** | a failed negotiation must leave a mark future scenes can read | **KEPT, CONDITIONALLY — and it is the weakest object in this document.** Under PR #362 it *is* a false N-line: the refusal Event (`commitment.refused`) enters the log, WITNESS mints claims from it (`04_CODE_ARCHITECTURE.md:724 §C.6`), and the Grudge is a second owner. **In the live tree it is the only durable trace**: there is no WITNESS, `_OUTCOME_BY_DEGREE` has no `stalemate` row, and the echo fires only on a non-zero delta (`echo_transport.py:424`). Confidence: **medium**. Cut condition, stated so a later pass does not have to re-derive it: *the moment a refusal Event reaches a durable log, cut the Grudge.* |
| **`settle()` itself** | the terminal | **SURVIVED.** §7.2. |

**Score against `14_NERS.md`'s meta-rule** — *"three edits, two of them deletions, and the vocabulary got shorter"*: this branch adds **one module and three names** (`settle`, `Settlement`, `Refusal`, plus the private `split`/`SHARE_BY_DEGREE`), deletes **`NegotiationMode`, the `negotiation` `GAMES` row, and `faction.py`'s duplicate band logic**, and cuts six candidate objects before they were written. The vocabulary is net shorter by the deletions and net longer by one function that nothing else can do.

### 7.4 E-ratio, watched in both directions (`14_NERS.md` §4.1)

| kept despite being distillable | the N it protects | confidence |
|---|---|---|
| `Settlement` as a type rather than a bare `float` | a caller that cannot treat "no deal" as a share; the discriminated union is the whole guard | high |
| the `Grudge` on refusal | a refused deal leaving any trace at all, in the tree as it is today | **medium** — see the cut condition above |
| `Refusal.reason` (a free string beside the kind) | the explanation contract (`04_CODE_ARCHITECTURE.md:751 §C.11` — *"there is no referee, so the engine inherits the referee's second job"*): a player refused a deal must be able to learn why | medium — the string is not machine-read and could be regenerated from the two bounds |

---

## §8 · Invariants, graded honestly

Grades per `04_CODE_ARCHITECTURE.md:66 §0`: **STRUCTURAL** = the defect has no spelling · **MECHANICAL** = one path exists and it refuses · **CONVENTION** = a reader notices. Per the same section's rule, a property holding only under an optional checker is written out as both halves, and **the runtime grade is the real one** because this repository runs no type checker in CI.

| id | invariant | grade |
|---|---|---|
| **I-N1** | `settle()` returns a share, never a winner | **STRUCTURAL under a checker · MECHANICAL at runtime** — `Settlement` has one field and it is a float; there is no side label to return |
| **I-N2** | `settle()` writes nothing and reads nothing but its arguments | **STRUCTURAL** — no `world` parameter exists, no module state is mutated, no import reaches a store. The defect cannot be spelled without changing the signature |
| **I-N3** | no settlement outside the ZOPA | **MECHANICAL** — one path, `min(ceil_a, max(floor_a, …))`, and the empty case returns before it. Falsifier F-N1 |
| **I-N4** | the split is symmetric under side swap: `split(-m) == 1 - split(m)` | **MECHANICAL** — one expression with one sign branch, and an exact identity test (F-N2) that **fails against the current `faction.py:117` table**, which is the control proving the test can see what it excludes |
| **I-N5** | ~~a settlement has a term or it is not a settlement~~ | **CONVENTION.** *Regraded down from the shape spec's "STRUCTURAL by signature".* `LedgerTag.ttl` defaults to `None` = durable (`ledger.py:41`, `:16-17`); `TreatyRecord.bound_season` is when it was **bound**, not when it ends (`treaty.py:65-66`), and expiry is a 0.90 lapse roll (`treaty.py:121`). Both signatures express a termless settlement happily. §1 row 11 |
| **I-N6** | two settlements between the same parties do not clobber each other | **MECHANICAL, and only if the key carries the Proposition id** — `ledger_add` dedupes by `(kind, key)` and refreshes in place (`ledger.py:53-56`). Falsifier F-N7 |
| **I-N7** | a reservation is never readable by the counterparty | **CONVENTION.** `ContestView` (`contract.py:54`) is *built*, not filtered — it exposes `evidence_available` as a count (`:66`), and a reservation is not on it at all today. When it becomes reachable, nothing structurally prevents a policy from being handed it |
| **I-N8** | the seam holds no token; both sides' consequences flow from one actor's act | **STRUCTURAL in the live tree** — `systems/social_contest/` contains zero writes to persistent state on this path (`SC_INVENTORY.md` §D1; the package's one such write is `parliamentary_vote.py:214`, a different seam). **STRUCTURAL under PR #362** — `04_CODE_ARCHITECTURE.md:164`, the wrapper is handed no token |
| **I-N9** | `settle.py` never joins the package import cycle | **MECHANICAL** — `tests/valoria/test_import_cycle_game_state_npe.py::test_exactly_two_cycles_remain_and_they_are_the_expected_families` fails on any change to the count. Falsifier F-N6 |
| **I-N10** | there is no second ladder | **MECHANICAL** — `settle()` calls `dice_engine.degree_from_net` (`:227`), the declared single owner, and passes no `extension`. Falsifier F-N5 uses the `test_balance_oracle_arms.py:65` idiom: patch the ladder, assert the output moves |
| **I-N11** | **no `Tenure` edge belonging to the counterparty is written on this path** — the settlement is a `Record`, and the only Tenure touched is the actor's own | **MECHANICAL under PR #362** — the gate refuses the alternative outright (`04_CODE_ARCHITECTURE.md:529-534`, `raise NotYours`), so the defect has exactly one path and it refuses. **CONVENTION in the live tree**, which has no gate and no Tenure at all. Falsifier F-N11 |
| **I-N12** | the settlement binds at return — nothing represents a not-yet-effective agreement | **STRUCTURAL, and inherited: it is the spine's I-S6a** (`01_SPINE.md:334-341`). `Settlement` has one field and `ContestOutcome` has no `pending`/`provisional`/`awaiting_ratification`. This branch adds no such field and could not add one without a visible edit to the spine's contract |
| **I-N13** | the settlement is in force for everything later in the same season | **NOT ENFORCED — and not CONVENTION, which would be the "guard that cannot observe what it guards" defect wearing a better label** (`04_CODE_ARCHITECTURE.md:78`). It is the spine's **I-S6b**, owned by IN (`engine/substrate/keys.py:569-573`, OF-7 defers the apply to `accounting_boundary`). The falsifier is the spine's §7.4 and **it fails on the current tree** |

---

## §9 · Falsifiers

`CLAUDE.md` §0.1 pt 3 — every result claim carries the test that would show it wrong, in the same commit. Pt 2 — each assertion must be able to **observe** the failure it excludes, so every loop below asserts that it asserted.

| id | claim it can break | how to run it | what makes it able to observe the failure |
|---|---|---|---|
| **F-N1** | *no settlement outside the ZOPA* | `settle(margin=5.0, floor_a=0.9, ceil_a=0.2)` → `Refusal("no_zopa")`; and over a grid of 400 `(margin, floor_a, ceil_a)` triples with `floor_a ≤ ceil_a`, `assert floor_a <= s.share <= ceil_a` with `assert checked >= 400` | the grid includes margins whose `split()` lies **outside** the range on both sides — without those the clamp is never exercised and the test passes vacuously |
| **F-N2** | *the split is symmetric* (I-N4) | for `m` in a grid spanning `[-6, 6]` including `0`, `±0.999`, `±1.0`, `±2.999`, `±3.0`: `assert split(-m) == 1.0 - split(m)` exactly (no `approx`), `assert checked >= 25` | **The control.** Run the identical assertion against `faction.py:117`'s current keying and it **fails** at `m` mapping to track 4 vs 6. A symmetry test that cannot fail on the known-asymmetric table is not testing symmetry. `pytest.approx` is forbidden here per `CLAUDE.md` §0.1 pt 2 — this is an exactness claim |
| **F-N3** | *the split is monotone, and `Failure` is unreachable* | over the same grid: `split` non-decreasing in `m`; and `assert degree_from_net(abs(m), 0.0) is not Degree.FAILURE` for every `m`, `assert checked >= 25` | the grid straddles every band edge (0, 1, 3) from both sides; a table keyed on the signed margin would return `FAILURE` for negative `m` and the second assertion fires |
| **F-N4** | *a clamp is a clamp, not a refusal* | `settle(margin=5.0, floor_a=0.0, ceil_a=0.52)` → `Settlement(share=0.52)`, not a `Refusal`; and `settle(margin=-5.0, floor_a=0.48, ceil_a=1.0)` → `Settlement(share=0.48)` | both cases have a non-empty ZOPA and an out-of-range `split()`; if the implementation refuses instead of clamping, both fail |
| **F-N5** | *there is no second ladder* (I-N10) | monkeypatch `dice_engine.degree_from_net`'s band edges (the `tools/balance_oracle.py:153` / `tests/valoria/test_balance_oracle_arms.py:65` arm idiom) and assert a fixed `margin` produces a **different** `share` | **the anti-fake-control clause**: if patching the owner's ladder does not move `settle()`'s output, `settle()` is banding somewhere else, which is the second resolver |
| **F-N6** | *`settle.py` stays out of the SCC* (I-N9) | `python -m pytest tests/valoria/test_import_cycle_game_state_npe.py -q` after the module lands | the test hard-codes the 9-module family (`:23`) and asserts the whole-repo cycle count is exactly 2 (`:53-92`). If `settle.py` imports `dictionaries` or `wrapper`, the count moves and the test fails — this is the only automatic detector of the §1 row 5 hazard |
| **F-N7** | *settlements do not clobber* (I-N6) | write two `Debt` tags for the same `(A,B)` with different Proposition ids into one `Settlement.ledger`; `assert len(ledger_get(led, "Debt")) == 2` | `ledger_add` refreshes in place on a `(kind, key)` match (`ledger.py:53-56`), so a key omitting the Proposition id silently yields 1 |
| **F-N8** | *the bout itself is not side-biased* | swap A/B over N seeds through `private_negotiation` with mirrored policies and compare the `share` distributions | reproduces the groundup `AUDIT.md` P1 87/13 turn-order finding (`v30-snapshot-2026-06-28:designs/audit/2026-06-03-contest-groundup/AUDIT.md`). **This one needs a tolerance, and the tolerance is a `[SEED]` to declare in the commit, not to hide.** Note the asymmetry with F-N2: `split()`'s half of the symmetry claim is an exact identity and needs no seed; only the bout's half is statistical |
| **F-N11** | *no counterparty Tenure is written* (I-N11) | scan the branch's write sites for any `Tenure` write whose subject is not the acting person; under PR #362, assert the gate raises `NotYours` on a synthetic attempt (`04_CODE_ARCHITECTURE.md:534`) | a scan that only counted writes would pass on a two-Tenure model; the assertion is on the **subject**, which is the field the defect lives in. In the live tree the scan is the only half available, because there is no gate to raise |
| **F-N12** | *the two-Tenure alternative is order-fragile* — the reason to reject it that is independent of any ruling | construct both act orders (A-then-B, B-then-A) over the fold and assert the bargain binds in **both**; the two-Tenure model fails one of them | **this is the falsifier for a design I did not choose**, and it is worth shipping precisely because it makes the rejection checkable rather than asserted. `canonical_order` (`:576`) + `D-36` (`:857`) are the mechanism |

### The control — what would show the change is **not** value-identical where it should be

**F-N9 (the control).** `python -m pytest engine/tests/test_mc_v18_regression.py engine/tests/test_f7_smoke_oracle.py -q` must be **byte-identical** before and after this branch lands. Negotiation is campaign-unreachable today — `scene_dispatch.py:301` is the only production caller of `resolve_contest` and it passes no `game=` (`SC_INVENTORY.md` §F: no file outside the package names any of the four game strings) — so adding `settle.py` and deleting a stub row must move nothing. **If the goldens move, the change reached agon and the branch is wrong.**

⚠ **This control is valid for THIS branch alone and must not be confused with the spine's.** `01_SPINE.md` §1.9 (b) / I-S6b will move the same goldens deliberately when the IN-lane `bind_now` change lands, and that is a **re-pin with a measured delta** (`CLAUDE.md` §0.1 pt 4), not a regression. Land them in separate commits, or F-N9 stops being able to tell the two apart — which is the whole reason it exists.

⚠ **And the instrument that must NOT be used as the control:** `tools/balance_oracle.py`. Because this branch is campaign-unreachable, both of its arms are identical **by construction**, and a green run would be a fake control — the exact worked case `CLAUDE.md` §7 records as ED-MB-0066. The goldens are the control; the oracle is not.

**F-N10 (the positive control for F-N9).** Deliberately patch `SHARE_BY_DEGREE` to `{0.5: …}`-different values and assert a seeded settlement moves. If it does not, the test suite is not reaching `settle()` and F-N1..F-N5 are measuring nothing.

---

## §10 · Fairness and playability

### 10.1 What the player decides, per step, and the consult load

| step | the decision | cost to think about |
|---|---|---|
| S0 | **the reservation** — how much am I willing to walk away from? | one number, declared before the bout, unchangeable during it |
| S2, ×1–3 | one `Move` per exchange from a 7-element closed set (`resolver.py:34`), of which `private_negotiation` realistically uses 4 (`advance`, `hard`, `support`, `pass`) | one choice from ~4 |
| S4–S6 | **nothing** — the terminal is mechanical | zero |

**Total: ≤ 4 decisions per negotiation.** The measured comparison is agon's harness at 9 aggressive / 3 passive moves (`agon_harness.py:490-494`) against the 3–4 ceiling the harness itself sets. This branch sits at the bottom of that band, which is right for a proceeding canon caps at 3 exchanges (`modes.py:514`).

**The consult load's real cost is the reservation, and it is one number**, not a table lookup. Nothing here asks the player to consult `SHARE_BY_DEGREE` — they will learn "arguing better gets me more" from playing, and the exact 0.50/0.55/0.60 is engine-side.

### 10.2 The exploit surface

| exploit | why it is bounded | measured? |
|---|---|---|
| **Stonewall** — set `floor_a = 1.0` every time | guarantees `Refusal` unless the counterparty concedes everything; the cost is no deal at all plus Let It Ride blocking a re-open (`v30:680`). Only dominant if no-deal is weakly better than every deal, which is false whenever the surplus is positive | **no** |
| **Reservation as a free lie** — always set the highest floor that still leaves a ZOPA | requires knowing `ceil_a`, which is hidden (Han Feizi's concealed heart; the `Dossier` idiom). **This is the branch's whole bet-under-uncertainty and it collapses the instant anything reveals a counterparty's reservation.** Nothing does today — and that is a property to defend, not an accident | **no** |
| **`support`-spam** — `support` costs 2, regroups +4, builds ethos, and accrues **no fault** (`resolver.py:350-351`, `primitives.py:51-52`) | in a 1–3 exchange budget, an exchange spent on `support` is an exchange not spent advancing. Whether the ethos→`readiness` feedback (`primitives.py Readiness.of`) repays that inside 3 exchanges is **unknown** | **no — and this is the live shape of the prior NERS pass's retired SC4 "Regroup-on-Spent dominant"** |
| **Silence** — never answer | `pass` accrues `fault.yields` toward the silence clinch (`resolver.py:345-348`), which sets `veto` and demotes. But `support` dodges the clinch with no fault, so the *stated* silence penalty is dodgeable — the defect `00_BRANCH_SHAPES.md` §1 already found, inherited unchanged | **no** |

### 10.3 ⚠ EVERY "NO DOMINANT OPTION" CLAIM IN §10.2 IS AN UPPER BOUND, NOT AN ESTIMATE

**No AI-vs-AI best-response sweep has been run**, for this branch or for any other. ED-SC-0021's falsifier — the sweep — remains unrun (`registers/handoffs/HANDOFF_SC.md:32-37`), and the only comparable harness in the tree is combat's. `04_ners_audit.md`'s discipline binds here: the bounds above say *"I could not construct a dominant line"*, which is a statement about my search, not about the strategy space. The `support` row is the one I would bet against first.

**One property is better than an upper bound and is worth stating separately**: the groundup stress work's F-A finding — 100% draws when both sides use low-resonance appeals (`v30-snapshot-2026-06-28:…/STRESS_MATRIX.md`) — becomes a **Partial here, i.e. a 50/50 settlement**, which is a real outcome rather than a hung one. That improvement is structural (`SHARE_BY_DEGREE[Degree.PARTIAL] = 0.50` is reached by a zero margin) and costs nothing.

---

## §11 · Open forks, run through the five tests

`CLAUDE.md` §0 (2026-08-24): **superseded → irrelevant → answered by a design document → answered by precedent → answered by the architecture.** Escalate only survivors. `needs_jordan` means *"Jordan is the only person who can answer this"*, not *"nobody got around to it"*.

### Fork 1 — in-scene vs cross-season binding · **RULED, NOT ESCALATED**

This is the one thing `00_BRANCH_SHAPES.md` §3(k)1 sent up. **It came back the same session.**

> **RULING — Jordan, 2026-09-04, verbatim:** *"negotiated agreement bind in scene. in fact, everything that occurs within a scene should bind or else it's as if time doesn't exist within a season."*

**The ruling is general and this branch merely instances it.** It is not a negotiation carve-out: it is a property of scene resolution — *a scene is where time passes inside a season*, and a scene whose outcome does not take effect until the next season has not, in the ruling's terms, happened. The finding and the vote inherit it identically (`03_INQUIRY.md`, `04_CONSENSUS.md`).

**What it settles here, concretely.** The two-season deal with a repudiation window between is REJECTED. `settle()` produces a binding agreement at the point of agreement: A's own `commit` and the instrument Record land in the same RESOLVE that ran the bout (§4 S5). There is no proposal awaiting ratification.

**What it costs — named, because a cost stated is worth more than a cost hidden. The ruling stands regardless.**

1. **The deniable defection dies.** Putnam's Level II gave you *"my principal refused to ratify"* — a betrayal with no author, expressible as a **non-event**. Under in-scene binding every defection is `repudiate` (`verb_table.yaml:378`): an act, with an actor, emitting `commitment.ended`, seen by whoever was present. **You lose authorless betrayal; you gain attributable and therefore costly betrayal.** For a game about political intrigue that is a genuine loss on one side and a genuine gain on the other, and I do not think it is obvious which is larger.
2. **The envoy cannot be disavowed — because the envoy cannot bind.** `commit`'s eligibility is `["own"]` (`verb_table.yaml:94`) and `rosters.yaml:102 remit_acts` has no `commit`, so no seat's remit reaches it. **Under today's roster the ruling means: a negotiation binds only between principals present in the scene.** The Kauṭilyan `dūta` ladder has no home until the roster gains `commit`. That is a registry gap owned by PR #357, named here rather than worked around.
3. **The ratification window as a pacing device is gone.** A two-season deal gave the world a season to react — counter-offers, bribery, pressure on the principal. Nothing in this branch compensates for that. If the game later wants it, the place to put it is a *declared term before the instrument matures*, not a staged consent.
4. **⚠ THE BREACH PATH IS ASYMMETRIC, AND THIS IS THE SHARPEST PRICE OF ONE-ACT BINDING.** One act means one actor, so only A ends the fold holding a `commit` Tenure — and `repudiate` requires exactly that (`verb_table.yaml:381`). **A can defect visibly; B cannot, because B has nothing to repudiate.** B is bound documentarily by the Record and, until B opens their own `oblige` in this or a later season (`01_SPINE.md` §3.4 (iii) 2), B's failure to perform is non-performance rather than an act. The two parties are therefore not symmetric in how their betrayal *reads*, and no ruled-in object closes that today. I did not paper over it with a synthetic B-side act, because a speculative `commit` chosen before the terms existed is the blank cheque the spine's order-fragility proof rules out. **Named as an open consequence, not solved.**
5. **The `Diplomacy` precedent is honoured, not violated — and this is an interpretation, not a proof.** `research/valoria_game_precedent_companion_v1.md:493`: *"A world where treaties bind automatically has no diplomacy in it."* Binding **in-scene** is not binding **automatically**: what binds is the agreement the parties reached, and `repudiate` remains available at the cost of an act, an Event and a visible broken commitment. The instrument is the thing that can be broken; that is precisely the *"binding instruments as the expensive exception"* the precedent asks for, priced on the breaking rather than on the making. If a later pass makes a settlement unbreakable, that precedent becomes the falsifier.

### Fork 1a — **the sharp question: where does an NPC counterparty's assent come from?**

The world freezes at barrier 2 and `deliberate(frozen)` is a pure map (`04_CODE_ARCHITECTURE.md:507`), so an NPC's act array was fixed before the contest resolved. If B's assent were a *choice*, B would have had to choose it before A's offer existed.

**It is not a choice. It is computed, and this branch is designed so that it can be.**

- **`settle()` is a pure function of three numbers.** The counterparty's floor (`ceil_a`) is an **input**, resolved at the seam boundary from the frozen projection along with the roster (`04_CODE_ARCHITECTURE.md:699 §C.5.1` — *"the sides are resolved once, at the seam boundary, and held for the contest's duration"*). No second Act is needed, the freeze is intact, and the agreement binds in-scene with nothing waiting on a later step.
- **Where the floor comes from, and what makes it fair rather than arbitrary.** It is `Tenure.degree` — the degree at which B **already committed** to the OUGHT at issue (`write_matrix.yaml:329-331`, `by: DR-2`, emits `tenure.graded`). Three properties follow, and together they are the whole fairness argument:
  1. **B authored it.** `commit` has eligibility `["own"]` (`verb_table.yaml:94`); nobody sets B's floor but B, in a prior act B chose.
  2. **It cannot be tuned at the moment of the deal.** That is not a limitation, it is Schelling's commitment (T0): a reservation binds by removing your own options, and one you could revise on the spot would bind nothing.
  3. **It is hidden from A.** The engine reads it; A bets against it. That is Han Feizi's concealed heart (`[PRIM]`), and it is the same concealment idiom the kernel already implements for evidence (`primitives.py:291 Dossier`, exposed as a count at `contract.py:66`).
- **The honest gap, stated as a gap.** `Tenure.degree` is **declared and does not exist in the live tree** — there is no Person, no Tenure and no commit degree anywhere in `systems/social_contest/`. Until it exists, `settle()`'s two bounds are supplied by the caller, and the one production caller supplies neither (`scene_dispatch.py:300`). **That is this branch's reachability gap, and it is the same "one line that does not ship" the three-lens audit named for `contestant_from_person`** (`04_reductive_audit_primitives_and_foundations.md:210-212`). It is why §0's grade is **paper**.
- **Is there a reason computed assent cannot work?** One, and it is worth stating precisely so a later pass can test it: **a reservation read from a prior `commit` is a reservation about the *proposition*, not about *this counterparty*.** A person may accept 40% from an ally and refuse 60% from an enemy. Modelling that needs a second input (a disposition toward A), which would make the floor a function of the pair rather than of the person — still computable at the seam, still no second Act, but no longer a single stored degree. I did not add it: it is a widening with no ruled-in carrier, and `settle()` composes with it unchanged if it ever arrives (the caller resolves the bound; `settle()` does not care how).

**On PR #362: there is no conflict, and the verdict is the spine's, not mine.** `01_SPINE.md` §3.4 (iii) establishes it from the primary text and this branch consumes the result: `§C.4:576` flattens acts **across all scenes** into one ordered fold; `PART D` row 49 (`:871`) forbids **nesting**, not same-pass resolution; `:579` evaluates a later act's `requires` against `world_as_predecessors_left_it`; and `:507` forbids DELIBERATE reacting to RESOLVE, which computed assent does not do. **A scene-internal outcome binds in the same RESOLVE with the freeze intact. Nothing in PR #362 needs amending, and this document proposes no amendment to it.**

**What made it look like a conflict is a modelling choice, and it is the one a builder is most likely to make.** Two `commit` Tenures puts you inside `tenure_kinds` (`:475`) and fires `AX-4` clause 2 (`:529-534`); one `Record` does not fire it at all (`§B.4/§B.5`, `:249-261`). **And the two-Tenure route fails for a second reason that has nothing to do with any ruling:** `canonical_order` is `(stratum, actor-hash, intra-person position)` (`:576`) with no rank tiebreak (`D-36`, `:857`), so nothing orders A's act before B's conditional commit and **the bargain silently fails to bind about half the time, for a reason nobody chose**. This branch takes the Record modelling, which has neither defect, and ships F-N12 so the rejection is checkable rather than asserted.

**The remaining gap is real, and it is IN-lane, not architectural.** PR #362's gate applies the write synchronously (`:536`, *"THE GATE APPLIES THE WRITE"*), so a PR #362 build satisfies the ruling natively. **The live engine does not** — OF-7 defers the echo's apply to `accounting_boundary` (`engine/substrate/keys.py:569-573`), so scene 2 of season N reads the world as scene 1 left it *before* scene 1 resolved. That is I-N13 / the spine's I-S6b; its owner is `engine/substrate/keys.py` and its falsifier is `01_SPINE.md` §7.4, which **fails on the current tree**. The ruling and PR #362 agree; the live tree disagrees with both.

### Fork 2 — ED-SC-0020, the burden-parameterized gate · **ANSWERED BY ARCHITECTURE (rung 5). CLOSE THE ROW.**

Superseded? No. Irrelevant? No. Design doc? Silent. Precedent? `ProofBar` = ACCUSER, `GraceThreshold` = petitioner, `TallyAtClose`/`PersuasionTrack` = NONE — the burden family already exists in disguise (`resolver.py:62-79`). Architecture? `T-k` one resolver one ladder (`01_AXIOMS.md:404`), §C.5's Margin contract, and the three-lens ADOPT recommendation (`00_synthesis.md:342-359`) all point the same way. **For this branch specifically the row is trivially answered: `private_negotiation` already resolves as `TallyAtClose`, so `burden: "NONE"` is a label on behaviour that exists.** Close `ED-SC-0020` with this citation; do not preserve it.

### Fork 3 — where the reservation comes from · **ANSWERED BY DESIGN DOCUMENT (rung 3), pending its existence**

`write_matrix.yaml:329 Tenure.degree` is the declared carrier and `00_BRANCH_SHAPES.md` §2.3 reached it independently. Not escalated; recorded as a **build dependency**, not a decision.

### Fork 4 — a Wager right at Overwhelming? · **ANSWERED BY DESIGN DOCUMENT (rung 3). CLOSED.**

I was about to give the Overwhelming band a Wager-Obligation right, on the `social_contest_v30.md:416` pattern. **Canon forbids it**: `social_contest_v30.md:325` — Wager Obligations are *"valid only in Grand Contests using Projection genre + Consequence Resonant Style."* Private Negotiation is neither. Closed at rung 3, and this is why §6.3's four bands share a field set: with the Wager gone, no band writes anything another does not.

### Fork 5 — reservation visibility · **ANSWERED BY PRECEDENT (rung 4)**

Hidden, on the `Dossier` precedent (`primitives.py:291`; the view exposes a count, `contract.py:66`). Not escalated. Graded CONVENTION in §8 (I-N7) because nothing structurally enforces it once the field becomes reachable.

### Fork 6 — the split table's asymmetry · **ANSWERED BY ARCHITECTURE (rung 5), against a design document**

Canon states the principle (*"track-distance weighting"*, `v30:415`) and lists values whose keying contradicts it (`v30:421-423`; `faction.py:107,117`). Under `CLAUDE.md` §0.05 the disagreement is *"a defect in one of them, resolved by deciding and then CHANGING THE CODE"*. The values are canon and are kept; the keying is corrected to the symmetric reading canon's own principle names. **`succession()`'s outputs move as a consequence** — the only assertion over them is `_kernel_tests.py:182`, which tests set membership and cannot observe the change (§1 row 6a). Not escalated; recorded so the behaviour change is not silent (`CLAUDE.md` §0.1 pt 4).

**Escalated to Jordan by this document: nothing.** The one fork that had survived all five tests was ruled on 2026-09-04 and is implemented above.

---

## §12 · The strongest case against this proposal, and the attacks I ran

### 12.1 The strongest case against it

**`settle()` is six lines, and six lines do not need a document this long.** The honest counter-reading of this branch is that it is a lookup table, a `min`, a `max` and a comparison — and that everything of substance here is either the spine's (the margin, the ladder, the return shape) or somebody else's lane (the Record, the treaty, the reservation's source). A reader who wants the shortest true summary should take §2's last line — *one deletion, one row field, and one pure function* — and treat the rest as the verification that entitled me to write those six lines.

**And the second-strongest: the reachability gap is not incidental, it is most of the work.** `settle()` cannot be reached from production without (a) a caller that supplies two reservations and (b) a Person reaching the kernel at all. Neither exists. Both are outside SC. So the deliverable that *executes* is not `settle()` — it is `settle()` plus two derivations this document does not own, and until they land the branch's grade cannot move off **paper** no matter how well the six lines are tested.

### 12.2 Attacks run, and their results — a failed attack reported as failed is a result

| attack | result |
|---|---|
| *"The split table can be lifted from `faction.py` as-is; §7.2.1 is canon."* | **SUCCEEDS — the strongest finding in this document.** The table is anti-monotone on A's side and awards a dead tie 55% to A (`faction.py:107,117`), and canon's own "track-distance weighting" principle (`v30:415`) contradicts the values it lists. §1 row 6 |
| *"The split table's single owner should be `dictionaries.py`, per the shape spec."* | **SUCCEEDS.** It would drag `settle.py` into the 9-module SCC that `test_import_cycle_game_state_npe.py:23` pins, breaking a live blocking test as a side effect. §1 row 5 |
| *"`_kernel_tests.py:182` already guards the split, so a change there is safe."* | **SUCCEEDS.** It tests set membership behind a vacuously-satisfiable disjunct. §1 row 6a |
| *"I-N5 is STRUCTURAL by signature, per the shape spec."* | **SUCCEEDS.** `bound_season` is a start, not a term; `ttl` defaults to durable. Regraded to CONVENTION. §1 row 11 |
| *"The counterparty's assent needs a second Act, so in-scene binding is unbuildable under PR #362."* | **FAILS.** `settle()` is pure; the floor is an input; the assent is computed. No second Act, no nesting, freeze intact. §11 fork 1a |
| *"Then PR #362 must be amended for binding-in-scene."* | **FAILS, and the refutation is the spine's** (`01_SPINE.md` §3.4 (iii)): `§C.4:576` folds acts across all scenes, `D-49:871` forbids only nesting, `:579` evaluates against `world_as_predecessors_left_it`. **No amendment is owed and this document proposes none.** The clause I had found (`§C.2` F3, `:529-534`) applies to the two-Tenure modelling, which this branch does not use |
| *"`kill / wound` writes `Tenure.until` on the victim, so PR #362's only contested verb already violates its own gate."* | **FAILS — and I ran it as a check on myself, because it would have been a convenient finding.** `verb_table.yaml:282-285`: `Tenure.until` appears **only** in the `Felled` band, which also writes `Person.exists` — so gate clause 4, *"cause is an existence change this same act caused — destroy's cascade"* (`04_CODE_ARCHITECTURE.md:533`), covers it exactly. The `Wounded` band writes `Person.body` alone. **The verb is compliant and my draft's parenthetical was wrong; it is deleted rather than softened** |
| *"Even under the Record modelling, the counterparty could bind itself with a conditional `commit` chosen in DELIBERATE."* | **FAILS, on an argument I did not have and the spine did.** `canonical_order` (`:576`) has no rank tiebreak (`D-36`, `:857`), so nothing orders A's act first and the bargain binds on an actor-hash coin flip. F-N12 makes the rejection checkable |
| *"`stakes` must stay — a terminal that does not know what is being divided cannot divide it."* | **FAILS.** A reservation stated as a share is scale-free, and once `terms` is cut nothing in the body reads `stakes`. A parameter nothing reads is `H-89`'s registered defect. §7.3 |
| *"`terms` is necessary for a multi-axis trade (critique `four-games FG-1`)."* | **FAILS, against my own first draft.** `settle()` has no per-axis input, so it cannot produce a trade; the uniform division it *could* produce is one multiplication the caller owns. A false N-line. §7.3 |
| *"A typed envoy latitude is the Kauṭilyan grounding's whole contribution, so it must be a parameter."* | **FAILS as a parameter, SUCCEEDS as a gap.** Latitude is the seat's remit (`§E.2.2`), not the terminal's business — and `rosters.yaml:102` has no `commit`, so no envoy can bind today. The research's contribution survives as a *cut*, and the gap is named. §7.3, §11 fork 1 cost 2 |
| *"`Refusal` duplicates `stubwire.StubResult`."* | **FAILS, with a mechanical reason.** A stub means *not built*; a refusal means *built, and it says no*. And `StubResult`'s module counter feeds `tools/m1_acceptance.py` row 1's stub-hit delta (`stubwire.py:56-62`), so reusing it would inflate the milestone instrument with working behaviour. §1 "also found" |
| *"`stalemate` already has a producer, so the refusal emits fine."* | **SUCCEEDS against the shape spec's §3(f).** Declared at `key_types.json:958`; `echo_transport.py:114` has no such row, and the Key does not fire on a zero delta at all. §1 row 12 |
| *"`writes_at(degree)` gives this branch its consequence column."* | **PARTLY SUCCEEDS, and produces a finding.** It gives the column a shape, and negotiation's four bands share a field set because the degree varies the *value*, not the fields — which shows the sixth column expresses only one of the two ways a degree can matter. §6.3 |
| *"Delete the row: negotiation is just `TallyAtClose`."* | **HALF-SUCCEEDS, and I acted on it.** The *game* is deleted (`GAMES` row, `NegotiationMode`); the *terminal* is not, because the three-lens audit that says "abandon the framing" says in the same breath *"keep `settle()` as the one genuinely new build"* (`04_reductive…md:334`). §2 |
| *"`support` is dominant in a 3-exchange budget."* | **INCONCLUSIVE — and named as the one I would bet against first.** `support` is reserve-positive with no fault (`resolver.py:350-351`); whether that repays a lost exchange inside a budget of 3 is unmeasured. This is the live shape of the retired SC4 finding. §10.2 |

### 12.3 Self-review bias, marked

This document audits a shape spec and then proposes the branch that shape spec asked for, and §8.6 of the session brief puts *this proposal* under the same NERS pass. Two limitations an independent reviewer would add and I cannot:

1. **I graded my own false-N-line hunt.** Six cuts, two of them against my own drafts, is a suspiciously convenient ratio. The `Grudge` row is the one I kept, and I kept it on a live-tree argument rather than an architectural one — which is exactly the shape of a rationalisation.
2. **I never ran anything.** Every property in §5 is an argument about code that does not exist, checked against code that does. F-N2's control (running the symmetry identity against the *current* `faction.py` table and watching it fail) is the single cheapest thing a reviewer could execute to test whether §1 row 6 — this document's headline finding — is real. It takes four lines and no fixtures.

### 12.4 Asymmetric-skepticism check

I accepted the 2026-06-28 critique's favourable *sound/high* verdicts on `mixed-motive FG-1/FG-2` on the strength of its own 46-agent verifier, which was self-authored (its header says so). Under the same standard I applied to its *already-handled* verdicts — which I re-checked against the tree — those favourable ones are **PROVISIONAL**: I verified their **locations**, not their **leverage**.

### 12.5 The prior NERS P2s, as they bear on this branch

`v30-snapshot-2026-06-28:designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_social_contest.md` left SC3/SC4/SC5 unverified. **SC4 ("Regroup-on-Spent dominant") is the only one that touches this branch**, and it is *irrelevant under its old name and live under a new one*: `Regroup` is not a `Move` (`resolver.py:34`), so the loop it described cannot form — but `support`'s net-positive reserve with no fault (`resolver.py:350-351`) is the same question wearing different clothes, and it is unmeasured (§10.2). SC3 (genre 0.5 near-inert) and SC5 (Focus-1 Regroup trap) have no mechanism in the live kernel and do not reach this branch. Re-graded under `14_NERS.md` Rule 1 rather than inherited: **E is not scored as an axis here** — the ratio is one new function and three new names against one deleted class, one deleted registry row, one deleted duplicate, and six candidates cut before they were written, with N and R unimpaired. It moves the right way, provisionally, on paper.

---

*End. `proposals/2026-09-04-social-contest-branches/02_NEGOTIATION.md` is the only file this agent created or edited.*
