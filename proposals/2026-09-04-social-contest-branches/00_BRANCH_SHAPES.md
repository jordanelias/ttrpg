# 00 · BRANCH SHAPES — negotiation · inquiry · consensus

## Status: **PROPOSED — shape spec only, nothing ratifies.** 2026-09-04. Read-only planner output (Fable, CLAUDE.md §10 row: audit/planner, not author). Paper grade throughout (§7.6).
## Compliance target: `proposals/2026-09-03-meta-architecture/04_CODE_ARCHITECTURE.md` (PR #362, PROPOSED, HELD BACK IN FULL) — a **shape constraint, not canon**. Where its shape and the live kernel conflict, the conflict is named, never resolved by declaring prose authoritative (CLAUDE.md §0.05).
## What this is: the SEQUENCE and SHAPE of the three `GAMES` rows that are STUB at `systems/social_contest/sim/contest/wrapper.py:236 GAMES`, decomposed for downstream builders. Every anchor below is `path:line symbol`, verified against the working tree at HEAD `1e163ee` on 2026-09-04. Snapshot material is cited `v30-snapshot-2026-06-28:<path>` and is **not in `main`**.

---

## §0 · Reading log, method, and the pointer note

**Read in full (working tree):** `wrapper.py`, `resolver.py`, `primitives.py`, `contract.py`, `modes.py`, `dictionaries.py`, `armature.py`, `rhetoric.py`, `appraise.py`, `degree_extension.py`, `faction.py`, `narrative.py`, `agon_harness.py`, `_kernel_tests.py` (wrapper block :632-712), `contest_legacy_stub.py`, `parliamentary_vote.py`, `parliamentary_stay.py`; `engine/cross_scale/{scene_dispatch,parliamentary_bridge,combat_bridge,echo_transport}.py`; `engine/substrate/{keys,descriptors,composition,stubwire}.py`; `engine/autoload/{dice_engine,sigma_leverage,game_state,season_manager,scene_slate}.py`; `systems/settlements/sim/{ledger,registry}.py`; `systems/factions/sim/{treaty,tribunal,excommunication,parliamentary_action}.py`; `systems/fieldwork/sim/{investigation,fieldwork,knots}.py`; `systems/social_contest/social_contest_v30.md` (+infill), `social_contest_flow_skeleton_v1.md`; `references/{module_contracts.yaml,descriptor_registry.yaml,KEY_INDEX.md,id_reservations.yaml,restructure_ledger.md}`; `registers/handoffs/HANDOFF_SC.md`, `registers/editorial_ledger_sc.jsonl`; `canon/02_canon_constraints.md`; PR #362 `01_AXIOMS.md`, `03_VERBS_AND_LOOPS.md`, `04_CODE_ARCHITECTURE.md`, `09_WORKED_EXAMPLES.md`, `HANDOFF_NEXT.md`; PR #357 `verb_table.yaml`, `write_matrix.yaml`, `rosters.yaml`, `hole_register.yaml`, tracer `shape.py`/`combat_seam.py`; `proposals/2026-08-31-unified-code-shape/14_NERS.md`, `proposals/2026-08-31-ideal/04_ners_audit.md`; `audit/2026-08-06-social-contest-three-lens-audit/` (00, 02, 03, 04 — the sections cited); `engine/tests/test_contest_kernel.py:93 _KERNEL_EXPECTED`. **Research:** everything in §0.1.

**Method.** Verify each claimed defect by reading the anchor, not the claim (§1). Decide the shared spine first and hunt it for false N-lines (§2, per `14_NERS.md` §3). Then each branch a–k (§3–§5). Every "no dominant option" statement in this document is an **upper bound** — no AI-vs-AI sweep was run (§7.5). Nothing was executed: no pytest, no mutation of `systems/`, `engine/`, `canon/`, `registers/`, `CURRENT.md`. This is the only file created.

**Pointer note (a real finding, one §1 row).** `references/restructure_ledger.md:1356-1357` carries two rows sending `designs/audit/2026-06-28-social-contest-deliberation-critique/` and its `audit/` alias to `FORK:c451bcb`. In this clone `git cat-file -t c451bcb` → *not a valid object name* and a full `refs/*` fetch did not bring it; the coordinator confirms the same. The content is alive at tag **`v30-snapshot-2026-06-28`** (40 files, extracted to the session scratchpad). A provenance pointer nobody can follow reads as resolved and is not; the fix is a ledger-row edit (IN lane), not anything in this proposal.

**Idiom.** Sequences use the flow-skeleton tags from `systems/_architecture/subsystem_flow_skeletons_v1.md:94`: `[branch] [emit] [gate] [write] [loop]`, with reads/writes/owner per step. Shapes use PR #362 vocabulary: modules (§A.2 :127), the write gate (§C.2 :520), Degree-keyed `writes:` (§C.4 :573), the contest seam (§C.5 :677), the roster contract (§C.5.1 :699), PART D grades (:811) — **STRUCTURAL** (cannot be spelled), **MECHANICAL** (one path refuses at runtime), **CONVENTION** (a reader notices).

---

## §0.1 · Research base — what was read, what was taken, and the tiers carried

Tier codes are the corpus's own: the rhetoric research uses `[PR]` primary-source-backed / `[REF]` reference-grade / `[PRIM]` primary text / `[TER]` tertiary; the snapshot syntheses use **T0** primary · **T1** authoritative synthesis · **T2** reputable secondary · **T3** navigation. Never an encyclopedia as evidence (the corpora themselves say so).

| source | what was taken into §3–§5 |
|---|---|
| `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md` (full, 524 ln) | §1.4 stasis ladder (conjectural = the kernel's `FACT`) → inquiry terrain. §4 Guiguzi *bai-he* / Han Feizi *Shuinan* and §5.4 Kauṭilya *dūta* types + four *upāya* (conciliate · gift · divide · force) `[PRIM]` → negotiation's instrument ladder and the dyadic/public axis. §5.1–5.3 Nyāya *vāda/jalpa/vitaṇḍā*, *nigrahasthāna*, Caraka *pariṣad* triage `[PRIM]` → the fault catalogue and self-gating already in the kernel; "silence convicts" for inquiry. §7.1 Norse Lawspeaker/Lögrétta **consensus → lot → majority** `[PRIM]` → consensus's terminal ladder. §7.2 *ordo iudiciarius* (libellus, litis contestatio, two-witness, confession) + Bernard Gui `[PRIM]` → inquiry's stages. §8.1–8.3 supplique/remontrance, du Rosier/Callières `[REF]` → asymmetric petition is NOT negotiation (kept out). **§9.7 what the corpus does not license: structure, never numbers** — honoured: no constant below comes from history. |
| `research/governance/`, `research/historical/`, `research/provenance/`, `references/historical/precedents_analysis.md`, `research/valoria_systems_integration_master_v1*`, `research/valoria_game_precedent_companion_v1*` (grep-surveyed) | Vote primitives and the permanent one-season-penalty gap (`_part1:263-267`) → §5(k) ED-SC-0015. Game precedent: Burning Wheel Duel of Wits (collapse-by-damage-output — the constraint agon already has), Diplomacy (no binding treaties → why a Record is needed), Machiavelli (bribery as a legal action → the liberum-veto bribe is an act, not a cheat), Ace Attorney (contradiction-matching = zero political modelling — avoided), I-2 recorded defeat (*senatus auctoritas* → consensus Success band), I-8 investigation caps ceiling via `BandExtension` → inquiry degree extension can only demote. |
| `audit/2026-07-08-contest-settlement-faction-interface/interface_report_v1.md` §2.5 | The critique's Type-3 finding restated at the SE seam: "no threshold, no holdout/veto, no sortition"; the Record primitive lives in SE. |
| `audit/2026-07-01-contest-gate-c-packet/GATE_C_packet.md` :121-124, :350-358 | Padgett–Ansell robust action, Greif self-undermining equilibria, the liberum veto as pathology → §5(b). |
| `audit/2026-07-04-ners-qualitative-audit/` | L-F "four games collapse" (:1431) — the earlier statement of the same defect the critique found. |
| **`audit/2026-08-06-social-contest-three-lens-audit/`** (2026-08-06, **later than the snapshot**) | `00_synthesis.md:328` "the missing S4 is the missing terminal of the adjudication cluster"; `:342-354` **negotiation = `gate(burden = NONE)`**, Fork A recommend ADOPT; `:459-463` S4 `settle()` is "the largest single piece of *new* design". `04_reductive…md:224-228` the type table: `inquiry` ∈ T2 (burden-bearing before a judge), `negotiation` ∈ T4 "until `settle()` exists", **`consensus` is the BG vote — a fidelity view, not a fifth type**; `:334` **"ABANDON THE FRAMING. Keep `settle()` as the one genuinely new build; Inquiry and Consensus are venue rows, not games."** `03_persuasion…md:153-171` N10 Deliberation = `VoteAtClose` + `Panel`, "today's `VoteAtClose` is formally a degenerate zero-round N10"; `:318` NULL: no deliberation loop in the kernel. `01_lens…md:87` sortition ABSENT. |
| `v30-snapshot-2026-06-28:designs/audit/2026-06-28-social-contest-deliberation-critique/critique.md` (full) + `findings.json` (all 27 gaps, all 11 strengths, with the verifier's corrected leverage) | The four-things-a-procedure-can-do frame (crown a winner · strike a bargain · discern a truth · enact a unity) mapped to the four `GAMES` rows. Findings carried: `mixed-motive FG-1/FG-2` (sound, high) → negotiation; `contest-locus FG-3` (sound, high) → consensus antibody; `four-games FG-3` (**already-handled**: Belief Revision is the discern-a-truth outcome) → inquiry does NOT add a conversion mode; `adjudicator FG-5` (already-handled: Panel) → verified landed; `caillois FG-4` (sound, medium) sortition → §5 `on_hung`; `commitment-store FG-1/2` (sound, medium) → **cut as a false N-line, §2.3**; `fallacies FG-2` (CR5 stranded) → now `rhetoric.py:413 cr5_self_backfire`, reachable only with an armature (§1 defect 1). |
| `…/source-research/deliberation-as-game-synthesis.md` (full) | Part 0 four senses of "game"; Part II.B–C commitment stores (Hamblin T0, Walton–Krabbe T0) — the case FOR a store, weighed and cut; Part III.E Priest–Klein selection (T0) → inquiry's lopsidedness is a selection fact, not a mechanic; Part IV Nash/Schelling/Raiffa/Walton–McKersie (T0), Putnam two-level "a metaphor" (T0, tier-flagged) → negotiation's ZOPA and the ratification fork; Part VI.2 eristic as the degenerate mode. |
| `…/politics-as-deliberative-game.md` (full) | Part B models 4 (acclamation), 7 (consensus: Great Law's sequence and anti-frivolous-objection rule; Benedictine Rule ch. 3; *ijmāʿ*; Gadaa — T0/T1), 8 (parliament = supply-for-redress bargain), 9 (Lateran IV three modes; *maior et sanior pars* as a weapon inside the dispute). **Part D.1 the three Types; D.3 consensus resists Caillois — do not force a family; D.4 compose, never pick.** |
| `…/renaissance-deliberation-and-the-classical-inheritance.md` (full) | Part I.4 *quod omnes tangit*, *maior/sanior pars*, *plena potestas* (T0 via T1) → who may bind whom (M2 scope); Part III.1 the mode repertoire; III.6 conciliar commitment problem. |
| `…/renaissance-machination-games-lens-and-review.md` (full) | Part V.2 Dowlen 2009 / Buchstein 2019 / Frey–Osterloh–Rost 2022 (T1): the lot as anti-capture, degrading with a small pool → §5 `on_hung: lot` weighted by margin; robust action / multivocality (not built — Equivocal stance stays out). Part VII.7 the analytic-narratives hazard → §7.5. |
| `…/renaissance-testing-the-model-and-closing-findings.md` (full) | **Part IX the liberum veto** (Konopczyński T1, Klick & Parisi 2003 T1): unanimity + no randomization + external bribers ⇒ hold-up; conditional success under fractionalization → §5's falsifier F-C2 reproduces the prediction. Part VIII.1 Venice *broglio*: the mechanism channels, never eliminates, maneuver. |
| `v30-snapshot-2026-06-28:designs/audit/2026-06-01-contest-redesign/RATIFIED_2026-06-01.md` | The ratifying text of CR1–CR7 (provisional). CR3 three trackers, CR4 stasis × genre (translative = the Stay), CR5 self-gating, CR6 δσ tanh cap. **Not in the working tree** — cite the tag. |
| `v30-snapshot-2026-06-28:designs/audit/2026-06-03-contest-groundup/` (all 20 `.md`; `.py` read only for diffs) | The live kernel's provenance. `framework.md` B "the modes do not share a win condition"; `AUDIT.md` P1 turn-order bias 87/13 → boundary resolution (regression falsifier for every branch); `AUDIT_RECONCILED.md` R1 `resist` scale-fragile, R4 evidence readiness-free+uncapped, open item C9b "ProofBar lets the defender win only by timeout — stall incentive"; `STRESS*.md` F1 build-then-close, F-A 100% draws under mismatched appeal, F-C faculty draw-collapse; `VENUE_VALIDATION.md` ProofBar = presumption of innocence (equal skill → acquittal 1.00; passive defence → conviction 0.97; bar = standard-of-proof dial), TallyAtClose tied votes 12–18%; `EVIDENCE_PRESSURE_VALIDATION.md` hidden evidence weight; `FACTION_NOTES.md` coalition pooling, committee band; `BALANCING_PASS_2026-06-05.md` inquisition drama 0.14 < target, courtier monoculture held for Jordan; `TERMINOLOGY.md` the vocabulary the identifiers assume. |
| `v30-snapshot-2026-06-28:designs/audit/2026-05-28-resolution-diagnostic/` (both) | The prior NERS verdict (COMPLIANT, four axes scored independently — the shape `14_NERS.md` Rule 1 was written against). SC1 exit-not-floor; SC3/SC4/SC5 unverified P2s — **dispositioned in §7.7.** |
| `v30-snapshot-2026-06-28:archives/audit/2026-06-09-social-contest-comprehensive/ANALYSIS.md` + `SYSTEM_MAP.md` | Three layers (L1 canonical / L2 CR / L3 groundup); P1-1..P1-3 record contradictions; the HI lifecycle state graph (`SYSTEM_MAP.md` §2.3) → inquiry's closure set; the flattened registry G-23 Tribunal prerequisites, G-24 Stay, G-30 one active investigation per target per jurisdiction. |
| `proposals/2026-08-31-unified-code-shape/14_NERS.md` + `proposals/2026-08-31-ideal/04_ners_audit.md` | The method: E as a ratio, the N-line, the false N-line pattern (*a mechanism was named, a store was proposed, the store's job was already done*), name the failed attack, "no dominant option" is an upper bound, state the paper grade. `04_ners_audit.md` cites "P-1..P-5" — **undefined anywhere in the tree; not used here.** |

**Where the 2026-06-28 critique and the 2026-08-06 three-lens audit disagree, and which wins (the audit is later):**

1. *Four modes vs venue rows.* Critique: consensus and negotiation are new resolution modes; three-lens `:334`: abandon the four-GAMES framing, inquiry and consensus are venue rows, `settle()` is the one new build. **Later wins on shape** (§2). The critique's *content* — the holdout pathology needs an antibody — survives inside the venue row (§5).
2. *Adjudicator armature.* Critique rec. #1 "not configured"; it **landed** (Stage 3 / Gate C, ED-1062: `armature.py:262 ArmaturePosition`, `:436 dsigma`) but is unreachable from the one production seam (§1 defect 1). Later state wins; the critique's recommendation is done-but-dark.
3. *Commitment store.* Critique rec. #5 (sound, medium). Three-lens `:318` records a NULL ("no deliberation loop … no legibility field on Move") and proposes no store. Neither built. Cut here as a false N-line (§2.3).
4. *Panel.* Critique "already-handled" → confirmed landed: `modes.py:502-509` `guild_arbitration` adjudicator `"panel"` (ED-1059), `dictionaries.py:685 PANEL_AGGREGATION` ratified ED-1057.
5. *Sortition.* Both: absent. Neither built. §5(e) makes it venue data, not code.
6. *CR5.* Critique: stranded. Now `rhetoric.py:413 cr5_self_backfire`, fired only under `self.armature.cr5` (`resolver.py:341-356 _apply`, per the flow skeleton :82) — i.e. stranded one level deeper.

---

## §1 · Verified ground — the seven claimed defects, and what else surfaced

| # | claim | verdict | anchors |
|---|---|---|---|
| 1 | `build_contest` has no `armature=`; Stage 3 / Gate C unreachable from the seam | **CONFIRMED** | `wrapper.py:110 build_contest` (params: `side_a, side_b, *, venue, adjudicator, stakes, world, use_tracker, degree_extension` — no armature); `:215 _resolve_agon` builds `Bout(...)` without `armature=`; `agon_harness.py:71 WORKAROUND 3`; the subsystem's own self-test bypasses the seam: `wrapper.py:377 _stage3_resolution_invocation_check` constructs `Bout(..., armature=ac)` directly, so a green self-check proves nothing about the seam |
| 2 | `resolve_contest(game=)` is dead weight in production | **CONFIRMED** | `wrapper.py:248 resolve_contest` default `game="agon"`; only caller `engine/cross_scale/scene_dispatch.py:301` passes nothing; `_kernel_tests.py:696-703` pins the stubs |
| 3 | Two return shapes | **CONFIRMED** | `wrapper.py:254-259` docstring "TWO RETURN SHAPES"; `:220 _stub` returns bare `stubwire.StubResult` (`engine/substrate/stubwire.py:43`); `scene_dispatch.py:301` unpacks a 2-tuple unconditionally |
| 4 | No record spine | **CONFIRMED, AMENDED** | Every wired output is a stat write: `scene_dispatch.py:336-345` echo → `echo_transport.py:441 _apply` → `game_state.py:153 Faction.adjust`. The Record primitive exists once, single-owner: `systems/settlements/sim/ledger.py:36 LedgerTag(kind ∈ Precedent/Grudge/Debt/Reputation/Leverage, key, value, created_season, ttl)`, `:47 ledger_add` (dedupe by (kind,key)), `:69 ledger_sweep`; consumed only by `registry.py:34-35, :88`. **Amendment:** a sibling exists — `systems/factions/sim/treaty.py:62 TreatyRecord(parties, terms, bound_arc, bound_season, active)` — and **neither has a custody dimension**: tags live on `Settlement.ledger` (`ledger.py:15-17`), never on a Person. PR #362 `Record` is "the fact that can leave the head that holds it" (`01_AXIOMS.md:857 §D.4`); PR #357 `H-84` (`hole_register.yaml:962`): no verb moves a Record. The custody gap is SE-owned (§2.4) |
| 5 | BG one-season Mandate −1 is permanent | **CONFIRMED** | `parliamentary_vote.py:214 adjust("L", …)`, `:218` "[one-season penalty; temporary-modifier restoration deferred to season_manager]"; `season_manager.py:33 advance_season` has no temporary-modifier facility; `game_state.py:198 reset_seasonal` resets flags only |
| 6 | Three resolution models under one name | **CONFIRMED, AMENDED to four executing + one prose** | `resolver.py:238 Bout`; `parliamentary_vote.py:125 run_parliamentary_vote`; `contest_legacy_stub.py:191 run_contest` (dead function, live constants `:67-71`); `faction.py:128 coalition_vote` (hand-built `ContestState`, direct `roll_net`, `PersuasionTrack.resolve` outside the loop — flow skeleton `:183`); the canonical §4 loop (`social_contest_v30.md:144`) has no engine |
| 7 | `agon_harness.py` has zero callers | **CONFIRMED** | grep; only `_kernel_tests.py` imports the wrapper. Note ED-SC-0021's falsifier (AI-vs-AI best-response sweep) has NOT been run — only a combat r8 parity harness exists in the tree |

**Also found (each anchored; none padded):**

- **The tracer seam refuses social prizes.** `proposals/2026-09-01-season-loop-tests/tracer/shape.py:4903 contest` dispatches `personal_combat` via `combat_seam.py:125 resolve` and raises `Unspecified` for `"a standing"`/`"a proposition"` (`rosters.yaml:359-360`). H-88 (`hole_register.yaml:1016`, Jordan verbatim at `:1026`, 2026-09-02): the seam naming the subsystem and refusing IS the intended behaviour for now. So the branches below plug a socket that exists and is deliberately empty.
- **Margin already exists one field deeper.** `resolver.py:88 PersuasionTrack.resolve` reads `self.track(s)` (:87) = `start + scale·(adv[A] − adv[B])` and *then* bands it; `:67 ProofBar` computes `net`. The kernel has a margin at every win-condition; it throws it away at the return. `KEY_INDEX.md:811 scene.contest_resolved` payload `persuasion_track_final` is the same number under another name.
- **`contest_side.a/b` are `kind: value` roles** (`module_contracts.yaml:176,180`) while the wrapper returns band *strings* (`"A_decisive"`, `"committee"`, …) — a latent mismatch; `scene_dispatch.py:305` comments the shape is "a win-condition band or side label".
- **Factions are claimants today.** `scene_dispatch.py:121 _emergency_council_parties` returns faculty ints derived from `f.L` / `f.Sta` (`:139`); `coalition_vote` pools faction Mandate. PR #362 §C.5 grades "a faction as combatant" **STRUCTURAL** (`claimants : PersonId[]`), §B.6.1 `Faction` is a Query return. Conflict named; not resolved here (§2.5 adapter).
- **`unanimity_required` is a named-but-unimplemented aggregation** (`dictionaries.py:686`, `:707`); `VoteAtClose` implements `weighted_by_standing` and `simple_majority` only (`resolver.py:128`). This is the exact slot consensus needs (§5).
- **The tribunal dropped its record guard.** `tribunal.py:73 formal_grounds_check` checks CI ≥ 40 ∧ L ≥ 4 only; the docstring (:76-80) says the Evidence ≥ 3 ∨ Obligation-violation ∨ 2-convictions alternative "is not yet ported". `social_contest_v30.md:626` has all three. Inquiry restores it via `ledger_has` (§4).
- **`parliamentary_stay.py:101 resolve_stay_lift` has zero callers**; `:54 invoke_stay` gates on `:37 STAY_CI_AVAILABILITY_MAX = 55`.
- **`scene.investigation_resolved`** exists (`KEY_INDEX.md:948`; finding ∈ exonerated|guilty|inconclusive; producers `faction_politics`, `scene_slate`) — `social_contest` is not a declared producer; a registry row, not a new key.
- **The silence clinch is dodgeable.** `resolver.py:345-351 _apply`: `pass` accrues `fault.yields` and regroups; `support` spends 2, regroups +4 (`primitives.py:51 COST`, `:56 regroup`, `REGAIN = 4`) and builds ethos **with no fault**. A defender who never answers but always "supports" never silences. Relevant to inquiry's *silence convicts* (§4(j), §7.3).
- **Dead pointer:** `references/restructure_ledger.md:1356-1357` → `FORK:c451bcb` (see §0).

---

## §2 · The one shared spine — the dedup decision

**Decision.** There are not three new games. There is **one seam entry keyed by prize, one return shape carrying a Margin, one ladder, and `game` becomes proceeding data.** Inquiry and consensus are `PROCEEDINGS` rows with one new field each; negotiation is those plus `settle()`, the one genuinely new function. This is the three-lens verdict (`04_reductive…md:334`) restated as code shape, and it is what PR #362 §C.5 demands: *"a subsystem returning a winner has not met the contract."*

### §2.1 What the spine is (owner: SC, `wrapper.py` / `resolver.py` / `modes.py`)

```
seam.contest(proj, place, prize, claimants: PersonId[], depth, max_depth)      -- PR#362 §C.5, unchanged
  prize "a proposition" | "a standing" | NEW "a finding" | NEW "a matter"      -- rosters.yaml:359-360 (+2 rows, owner: PR#357 rosters)
  provider = social_contest                                                     -- manifest by prize; still refuses today (H-88)
  proceeding = PROCEEDINGS[name]         # name from the prize + place; modes.py:485
  sides     = contestant_from_person(claimants) resolved ONCE                   -- §C.5.1 roster contract; NEW adapter §2.5
  outcome   = resolve_contest(build_contest(..., armature=, rng=))             -- ONE return shape
  ContestOutcome(margin: float, reason: str, veto: bool, beats: list)          -- margin NEVER a winner
  degree    = dice_engine.degree_from_net(margin, ob=0, extension=proceeding.extension)   -- engine/autoload/dice_engine.py:227; ONE ladder
             veto=True (a clinch against the burden-holder) demotes to Failure; never promotes   -- §C.5 "the veto can only demote"
```

- **`WinCondition.margin(state) -> float`** (NEW method, `resolver.py:52`, one per subclass): `ThresholdRace`/`TallyAtClose` → `adv[A] − adv[B]`; `ProofBar` → `net − bar` (:67-72, sign = burden met); `GraceThreshold` → `adv[pet] − bar`; `PersuasionTrack` → `track − start` (:87; **this makes `persuasion_track_final` literally the margin**, closing the −5..+5 vs 0–10 scale collision); `VoteAtClose` → weighted share − 0.5 (:128). `resolve()` stays as the band view for `narrative.py:83 classify` and the tests. ED-SC-0020 Fork A ("burden-parameterized gate", HANDOFF_SC.md:32, needs_jordan) is **answered by architecture** (five-test rung 5): `T-k` one resolver one ladder (`01_AXIOMS.md:404`) + §C.5 Margin + the three-lens ADOPT recommendation (`00_synthesis.md:342-359`) all point the same way, and the burden family already exists in disguise (`ProofBar` = ACCUSER, `GraceThreshold` = petitioner, `TallyAtClose`/`PersuasionTrack` = NONE). What Fork A adds is *stall semantics* — whoever holds the burden loses the stasis on a stall — which `ProofBar:71-72` already has (closing → defender). So: `PROCEEDINGS[name]["burden"] ∈ {ACCUSER, RESPONDENT, LOWER_STANDING, NONE}` selects the `WinCondition`; the two biased starts (`church_tribunal` `CHURCH_TRIBUNAL_TRACK_START`, `modes.py:496`) and the `tracker_mode` tri-state (`:521 _use_tracker`) become derivable and are deletion candidates. **This closes ED-SC-0020 without a ruling; the row should be closed with this citation, not preserved.**
- **`GAMES` collapses into `PROCEEDINGS`.** Delete `game=` from `resolve_contest` (`wrapper.py:248`); delete the three `_stub` rows and their `ck`s (`_kernel_tests.py:696-703`); `_KERNEL_EXPECTED` (`test_contest_kernel.py:93`) moves. Defects 2 and 3 close by deletion (the `14_NERS.md` §1 meta-rule benchmark: *edits, two of them deletions, and the vocabulary got shorter*).
- **Armature passthrough (defect 1):** `build_contest(..., armature: ArmatureConfig | None = None)` → `Bout(..., armature=)`; `opponent_is_adjudicator` derived from `PROCEEDINGS[name]["roles"] in {"inquisitor_proposes", "crown_objects"}` (`modes.py:495, :491`) via `armature.py:374 position_of`. Gate-off, not a flag: an asymmetric proceeding never double-counts Resonant Style (critique adjudicator FG-2's own caveat).
- **rng injection (NEW param, MECHANICAL):** `Bout(..., rng: random.Random | None)`; `resolver.py:28 roll_net` takes `rng`; `sigma_leverage.py:269 roll_net(pool, tn, rng)` already does. Retires the global reseed dance at `scene_dispatch.py:299`. The 389 seeded kernel checks stay green because `rng=None` keeps the module stream.
- **Degree-keyed consequences live on the calling verb, never in the seam.** `verb_table.yaml:234 kill / wound` is the precedent (the only `contests:` row). The three branches each name the verb whose `writes:` column carries their Degree ladder (§3–§5 e). The seam has no token (`§C.5` "a state write from inside — no token, STRUCTURAL").
- **Key emission:** `echo_transport.py:108 KEY_TYPE_BY_SCENE` gains `"inquiry": "scene.investigation_resolved"`; negotiation and consensus emit `scene.contest_resolved` with `outcome` from the existing enum (`_OUTCOME_BY_DEGREE:114` — `compromise` is already there). **Zero new key types.**

### §2.2 The N-line for every spine object

| object | cut it, and the emergent possibility lost is… |
|---|---|
| `margin()` on every `WinCondition` | a contest that can feed the ONE ladder; without it each branch invents its own degree (four resolvers becomes seven) |
| `burden` on `PROCEEDINGS` | *silence convicts* — the inquiry outcome no handicap can express (`00_synthesis.md:349-351`) |
| `armature=` passthrough | every Stage-3 mechanic (CR4 terrain, CR5 backfire, the adjudicator's convictions) from the seam — the consensus antibody has no carrier without it |
| `rng` injection | same-seed reproducibility through the seam without touching global state; the parity harness (§5 i) is unrunnable without it |
| `contestant_from_person` | a Person as a claimant at all. Today only faction-derived ints reach the kernel from production |
| `ContestOutcome` (one shape) | a caller that cannot tell a stub from a result (`scene_dispatch.py:301` breaks on a stub today) |

### §2.3 False N-lines hunted — the highest-value pass (`14_NERS.md` §3 pattern)

| candidate store | its claim | why the possibility survives the cut |
|---|---|---|
| **In-contest Commitment Store** (critique rec. #5, commitment-store FG-1/2) | contradiction-traps and forced retractions need a ledger of conceded propositions | **Cut.** In-bout: `resolver.py:353-357` already sets `fault.contradicted` on an incoherent `shift` and `DefeatCatalogue.check` (`primitives.py:273`) clinches on it; `Bout(record=True).log` (flow skeleton :89) already records every beat. Cross-scene: what is owed is a `Proposition` the person `commit`ted to (`01_AXIOMS.md:1292 §E.1.7`), read from `Tenure` — a store on the contest would be a second owner of the same fact (AX-4) |
| **`Record.stages` on a Case object** (my own first draft of §4) | a multi-season investigation needs staged state | **Cut, against this document.** A stage is an act that happened; the record of acts is `engine/substrate/keys.py:336 KeyLog`. Stage = count of `scene.investigation_*` keys with `subject_id` (a Query; `T-a` an aggregate cannot be stored). The only persistent scalar — the evidence count — is a `LedgerTag` |
| **Reservation value as a new `Contestant` field** (negotiation) | a hidden walk-away point needs a carrier | **Cut.** `primitives.py:283 EvidenceItem` / `:291 Dossier` already model a hidden weight the view exposes as a count (`EVIDENCE_PRESSURE_VALIDATION.md`); the three-lens M3 says concealed value is "one object in three costumes" (`02_system…md:229-232`). Reservation = the person's own `commit` degree on their OUGHT (`write_matrix.yaml:329-330 Tenure.degree`) |
| **`offer` / `concede` Move kinds** (negotiation) | bargaining needs bargaining moves | **Cut.** An offer is an utterance of a new OUGHT at a different degree — `verb_table.yaml:475 utter` at the act layer, not a `Move` inside the bout (`VALID_KINDS`, `resolver.py:34`, unchanged). `HANDOFF_NEXT.md:57` 2e says exactly this: *"no bargain — test composability first; adding a verb is the last resort"* |
| **A Holdout Obligation clock** (critique contest-locus FG-3 b) | a blocked consensus needs a clock | **Cut.** The matter's own `SceneSlot` (`engine/autoload/scene_slate.py:25`, `:34 queue_scene`) re-queues next season (v30 §6.3 chain, `:368`); the holdout's mark is a durable `Grudge` tag (`ledger.py:30`) |
| **A fourth resolver for consensus** | unanimity is a different game | **Cut.** `VoteAtClose` with `aggregation="unanimity_required"` (`dictionaries.py:686`) is the slot; the loop is `Bout.resolve` (`resolver.py:440`); the per-member ballot is the existing sampling pass retained (three-lens N10 "degenerate zero-round") |

Six candidates, six cut. **One survived the hunt and is genuinely new: `settle()`** (§3 e) — its job is done by nothing ruled in; the three-lens reached the same conclusion independently.

### §2.4 Where the spine is genuinely short, and who owns it

- **Custody of a Record (SE lane).** `LedgerTag` has no holder. Negotiation's Debt, inquiry's finding, consensus's Precedent all want *a Person who holds the fact* (`§D.4`). Minimal owner-side change: one optional field `holder: PersonId | None` on `LedgerTag` (`ledger.py:36`), default `None` = the settlement holds it (today's semantics preserved byte-for-byte). NOT proposed here; named for SE. Until it exists, all three branches write to `Settlement.ledger` at `place`.
- **`Faction` as claimant (IN/FA seams).** `_emergency_council_parties` (`scene_dispatch.py:121`) must become a Query returning `PersonId[]` at weight (§C.5.1). Out of SC scope; the adapter in §2.5 refuses non-Person input so the leak is MECHANICAL, not silent.

### §2.5 The one new adapter (SC-owned)

`contestant_from_person(person, proceeding) -> Contestant` (`resolver.py:180 Contestant(faculty, standing_start, reserve_max, dossier, evidence, charisma)`): `faculty` from `ADJUDICATOR_PRIMARY` (`modes.py:426`) over `descriptors.py:59 ATTRIBUTES`; `standing_start` from the Standing track (`descriptor_registry.yaml:285`); `dossier` from held `Leverage` tags keyed to the stasis. Refuses (typed `Refusal(not_a_person)`) anything without a `PersonId` — this is where the STRUCTURAL faction-leak becomes MECHANICAL until the callers are fixed.

### §2.6 Watched despite being distillable (E-ratio, both directions)

| kept | the N it protects | confidence |
|---|---|---|
| `PersuasionTrack` as a band view beside `margin()` | the committee/compromise band as composed-echo magnitude key (ED-SC-0002 ruled; `00_synthesis.md:355-357` "keep the Persuasion Track") | high |
| `Panel` closure rebind in `build_contest` (`wrapper.py:181-190`) | the bench composition N19 (`03_persuasion…md:157`) | medium — could fold into the adapter |
| `on_hung` venue field (§5 e) | an anti-capture terminal for a hung unity | **medium** — one branch, watched; the smallest thing in this document that could still be a false N-line |

---

## §3 · NEGOTIATION — strike a bargain

**(a) Conflict class, and why agon cannot.** Mixed-motive, positive-sum: both parties can gain; the contest decides the *division* of a surplus the parties jointly create (synthesis Part IV, T0; politics model 8 supply-for-redress). Agon cannot because `PersuasionTrack.track` (`resolver.py:87`) is one bidirectional scalar — every unit A gains B loses — and the 4–6 band is "nobody won" (v30 `:279`, `:702` "ZOPA-style … not designed"). The three-lens is right that the *leverage* half is `gate(burden = NONE)` and already resolves as `TallyAtClose` under `private_negotiation` (`modes.py:513`, tracker optional); the *agreement* half — the terminal — does not exist (`00_synthesis.md:328`).

**(b) Grounding (tiers carried).** `[PRIM]` Kauṭilya's four *upāya* as the instrument ladder — conciliate → gift → divide → force — and typed envoys with typed latitude (`framework.md` B; rhetoric research §5.4). `[PRIM]` Han Feizi *Shuinan*: the same true offer lands or kills depending on the listener's concealed heart → the counterparty's reservation is hidden. **T0** Nash 1950 disagreement point; Schelling commitment as self-binding; Raiffa reservation price / ZOPA; Walton–McKersie integrative vs distributive. **T0 (tier-flagged "a metaphor")** Putnam two-level games: a deal binds only inside the win-set of whoever must ratify at home — the source of fork (k)1. **T1** conciliar commitment problem (`renaissance…inheritance.md` III.6; `machination` VI.5): a body cannot bind a head who regains the power to renege → why a treaty is a Record with a term. Game precedent: Diplomacy (no binding treaty → churn from repudiation is a feature, not a bug — the `repudiate` verb, `verb_table.yaml:378`, is the mechanism); Machiavelli (bribery as a legal action — a gift is `upāya` 2, an Act, not a cheat). Not licensed: any number.

**(c) Canon anchor.** v30 §2 proceedings table `:99-108` (Private Negotiation 1–3, symmetric, no adjudicator); §6.1 Obligations `:306`, Wager `:314-319`; §12 `:702`. P-14 (`canon/02_canon_constraints.md:23`): a bargain at faction scale must co-move like any other mode. PR #362 `§E.1.7` (`01_AXIOMS.md:1292`): an oath is an utterance; what is owed is the OUGHT Proposition; `§E.2.2` authority is a property of the seat (`:1356`); `Act.via: SeatId?` (§B.9 `:392`). `HANDOFF_NEXT.md:57` 2e: no `bargain` verb until composability is tested.

**(d) SEQUENCE** (owner SC unless marked; reads/writes named per step).

```
S1  [write] open — A: utter(P_A: OUGHT, degree d_A)  · B: utter(P_B: OUGHT, degree d_B)       verb utter, verb_table.yaml:475; each their own act (AX-1)
    reads: nothing of B's; writes: Proposition (immutable, write_matrix.yaml:231-243) via the gate; Receipt
S2  [loop ≤ exchanges(1,3)] leverage bout — Bout(private_negotiation, burden NONE, adjudicator none)
    S2.1 [branch] each exchange: Move ∈ VALID_KINDS (resolver.py:34); reception → _advance (resolver.py:283, :314)
    S2.2 [gate]   clinch → DefeatCatalogue.check (primitives.py:273) ⇒ veto=True for the faulting side
    S2.3 [emit]   beats (Bout(record=True).log)
    reads: Contestant (adapter §2.5), Dossier (hidden weights); writes: NOTHING (no token)
S3  [branch] margin = TallyAtClose.margin (adv[A]−adv[B]); degree = degree_from_net(margin, 0, extension)   ONE ladder
S4  [gate] settle(margin, d_A, d_B, stakes) -> Settlement | Refusal(no_zopa)          NEW pure map (§e); reads only its arguments
    share = split(margin)     -- the §7.2.1 track-distance table, single owner moved to dictionaries.py (today faction.py:86 succession)
    ZOPA holds iff share ∈ [d_B's floor, d_A's ceiling]  (reservations are the two commit degrees)
S5  [branch] on Settlement:
    S5.1 [write] A: commit(P_settled) via seat? -> Tenure.since (verb commit :92; Act.via if envoy)     own act
    S5.2 [write] B: commit(P_settled)                                                                    own act — THE FORK (k)1
    S5.3 [write] faction-scale: register_treaty(parties, terms, bound_arc, bound_season)  treaty.py:145 (FA-owned; existing)
                 person-scale: LedgerTag(kind="Debt", key=P_settled.id, ttl=term)        ledger.py:36 (SE-owned; existing)
    S5.4 [emit]  scene.contest_resolved{outcome: compromise|initiator_win|target_win, persuasion_track_final: margin}  echo_transport.py:371
    on Refusal(no_zopa):
    S5.5 [write] LedgerTag(kind="Grudge", key=(A,B,P), ttl=None) ; Let It Ride (v30 :680) blocks re-open until circumstances change
    S5.6 [emit]  scene.contest_resolved{outcome: stalemate}
```

**(e) SHAPE.** Modules: `modes.py` (`PROCEEDINGS["private_negotiation"]` gains `burden: "NONE"`, `settle: True`); `resolver.py` (`margin()`); **NEW** `settle.py` in `systems/social_contest/sim/contest/` — one function, pure, no world access (the DELIBERATE-is-a-pure-map idiom, `04_CODE_ARCHITECTURE.md:564 §C.3`). Owned state: none new. Params: `settle(margin: float, floor_b: float, ceil_a: float, stakes: Stakes) -> Settlement(share: float, terms: dict) | Refusal(no_zopa)`. Query vs write: `settle` is a Query; every write is a `commit` or `register_treaty` by the actor, through the gate (`§C.2 :520`), returning a `Receipt`; the seam returns `NoOpReceipt` on refusal (ID-9). Gate: `Refusal(no_zopa)`, `Refusal(scope)` — an envoy whose `via` seat lacks `commit` in its remit (`§E.2.2`; `rosters.yaml:94 remit_acts` has no `commit` today → binding via seat is **not expressible until the roster adds it**; conflict named), `Refusal(depth_cap)`. `Act.actor: PersonId` on every write. **Degree-keyed consequence column** (on `commit`'s `contests:` row, the `kill / wound` precedent `verb_table.yaml:234-238`): *Overwhelming* → settlement at A's terms + Wager-extraction right (v30 `:416` pattern, one free verifiable-condition Obligation); *Success* → settlement at `split(margin)`; *Partial* → 50/50 or deferred to a chain (`queue_scene`, cap 3, v30 `:383`); *Failure* → no deal, Grudge, Let It Ride. Veto (clinch) demotes only.

**(f) Keys.** Reads: `state.opinion_revised` (already consumed, `module_contracts.yaml:748`). Writes: `scene.contest_resolved` (`KEY_INDEX.md:811`; outcome enum already has `compromise`/`stalemate`), optionally `scene.dialogue` (`:828`). **NEW keys: none.** Descriptor registry: no new descriptor; the Debt tag is a `LedgerTag` kind that exists (`ledger.py:30`).

**(g) Reuse ledger.** `Bout`, `TallyAtClose` (burden NONE), `PersuasionTrack` optional tracker, `DefeatCatalogue`, `Dossier` hidden weight, the §7.2.1 split table (`faction.py:86-118 succession` bands — move the table, delete the duplicate band logic `AUDIT_RECONCILED.md` LOW "band logic duplicated"), `utter`/`commit`/`repudiate` verbs, `Act.via`, `register_treaty`/`process_treaty_expirations` (`treaty.py:121` — the term lapses by MATTER, `T-n`), `LedgerTag` Debt/Grudge, `echo_transport`. **Deleted:** nothing beyond §2.1's.

**(h) Invariants.**

| id | invariant | grade |
|---|---|---|
| I-N1 | the bout returns a margin, never a winner | STRUCTURAL under a type checker · MECHANICAL at runtime (`ContestOutcome` has no winner field) |
| I-N2 | the seam writes nothing; both commits are each actor's own act | STRUCTURAL (no token in the seam) · MECHANICAL (gate refuses `actor ≠ owner`) |
| I-N3 | no settlement outside the ZOPA | MECHANICAL (`settle` refuses) |
| I-N4 | a reservation is never readable by the counterparty | CONVENTION (the view is built, not filtered — `ContestView` exposes `evidence_available` as a count, `contract.py:54`) |
| I-N5 | a settlement has a term or it is not a settlement | STRUCTURAL by signature (`TreatyRecord.bound_season`; `LedgerTag.ttl`) — `T-n` |

**(i) Falsifiers** (`§0.1` pt 3; each observes the failure it excludes).

- F-N1 seeded: disjoint reservations (`ceil_a < floor_b`) → `Refusal(no_zopa)`, `len(receipts) == 0`, a Grudge tag present. Asserts `assert checked >= 1`.
- F-N2 same seed twice through the seam with `rng` injected → identical `Settlement.share`; no global `random` state change (compare `random.getstate()` before/after).
- F-N3 envoy `via` a seat without `commit` remit → `Refusal(scope)`, no `TreatyRecord` registered.
- F-N4 symmetry regression (groundup `AUDIT.md` P1 87/13): swap A/B over N seeds → mirrored `share` within tolerance; the tolerance is the `[SEED]` to declare, not to hide.
- F-N5 `_KERNEL_EXPECTED` (`test_contest_kernel.py:93`) moves by exactly the new `ck` count minus the three deleted stub pins.

**(j) Fairness / playability.** Consult load: ≤ 3 exchanges × 1 move + 1 accept/refuse = **≤ 4 decisions per negotiation** (agon measured 9 aggressive / 3 passive at `agon_harness.py:490-494` against a 3–4 ceiling). Playable seat: the envoy/principal — yes. Dominance candidates: *stonewall* (refuse every settlement) — cost is Let It Ride + a durable Grudge; *ethos-spam* (`support` is reserve-positive, §1) — buys nothing here because the terminal is `settle`, not standing. **Upper bound only: no sweep run.** Groundup STRESS_MATRIX F-A (100% draws when both sides use low-resonance appeals) becomes a *Partial* here, which is a real outcome (50/50), not a hung one — an improvement the shape gets for free.

**(k) Forks through the five-test ladder.**

1. **Agreement concluded in-scene vs cross-season ratification.** Tests: (1) superseded — no; (2) irrelevant — no; (3) design doc — v30 §6.1 makes the Obligation bind at contest close (in-scene) but predates AX-1; PR #362 §C.5 (no token) + `03_VERBS…md:136 §C.3` one act per person per season imply the counterparty's `commit` is a *separate act next RESOLVE* — cross-season, provisional until then; both documents are PROPOSED/unratified against each other; (4) precedent — the three-lens M2 Scope "PROVISIONAL-binding/repudiation spine" (`02_system…md:226-228`) is the same shape, also PROPOSED; (5) architecture — gives a **default** (cross-season, conformant) but the consequence is a game-feel fact: *every negotiated deal takes two seasons to bind and can be repudiated in between* (Putnam's Level II made literal). Two defensible options lead to materially different games. **Survives all five → `needs_jordan`, the only escalation in this document.** Recommended default: cross-season (PR #362-conformant; F-N3 assumes it).
2. ED-SC-0020 burden gate → answered by architecture (§2.1). Close the row with this citation.
3. Reservation visibility → answered by precedent (`Dossier` hidden weight; three-lens M3). Not escalated.
4. "Add a `bargain` verb?" → answered by `HANDOFF_NEXT.md:57` 2e and by §2.3 (utter + commit compose). Not escalated.

---

## §4 · INQUIRY — discern a truth

**(a) Conflict class, and why agon cannot.** Asymmetric, burden-bearing, judged by a third; the outcome is a *finding about a past act* — a truth claim, not a right claim (AX-3, `01_AXIOMS.md:111`). Agon cannot because the symmetric track has no burden and no stall semantics: `church_tribunal` fakes the burden with a biased start (`modes.py:495-497`, `CHURCH_TRIBUNAL_TRACK_START`), which changes expected value and cannot express *silence convicts* (`00_synthesis.md:349-351`). `ProofBar` (`resolver.py:67`) can: the challenger must clear the bar or lose at close.

**(b) Grounding.** `[PRIM]` *ordo iudiciarius*: libellus → litis contestatio → proof (two witnesses or confession) → sentence; Bernard Gui's manual (rhetoric research §7.2) → the stages S1–S4 below. `[PRIM]` Nyāya *nigrahasthāna* and Caraka triage → the fault catalogue with `evasion_strikes=1` (`modes.py:181-199 inquisition_hearing_venue`, whose docstring already cites Eichbauer 2014 doi:10.1111/hic3.12130 and Taliadoros 2018). `[PRIM]` stasis: the inquisitor's question is conjectural/FACT (`modes.py:64 CHURCH_TRIBUNAL_START_GROUND = FACT`, ED-1062). **T0** Walton–Krabbe *inquiry* dialogue type (resolution on the merits; eristic degenerate). **T0** Priest–Klein: the cases that reach trial are the closest ones — a *selection* fact, so no lopsidedness gate is built (critique mixed-motive FG-3 corrected to low). **Measured (snapshot, groundup):** ProofBar reproduces presumption of innocence — equal skill → acquittal 1.00, passive defence → conviction 0.97, the bar is the standard-of-proof dial (`VENUE_VALIDATION.md`); inquisition drama 0.14 < 0.20 target, intrinsic to bar venues (`BALANCING_PASS…md` finding 1, held for Jordan). Critique four-games FG-3 **already-handled**: the discern-a-truth conversion outcome is Belief Revision (npc_behavior §3.2) with `state.belief_revised` (`KEY_INDEX.md:1016`, producers `fieldwork_knots`, `npc_behavior`) — inquiry emits a *finding*, not a conversion; the Sincerity Gate (`systems/fieldwork/fieldwork_v30.md:419 §5.3`, Spirit TN 7 Ob 1) is FI-owned and not duplicated. Game precedent I-8 (investigation caps ceiling via `BandExtension`) → the extension may only demote. Ace Attorney avoided.

**(c) Canon anchor.** v30 §7 `:387`; §7.1 `:624-629` prerequisites (CI ≥ 40 ∧ Mandate ≥ 4 ∧ (Evidence ≥ 3 ∨ Obligation violation ∨ 2 prior convictions)), track starts 7, no accused corroboration; §7.3 `:441-468` Heresy lifecycle (Initiation → Investigation 2–4 seasons, one Zoom-In per season → Verdict; eight closures); §10.1 Stay `:647`. P-08/P-13 (`02_canon_constraints.md:17, :22`): evidence is available, the capacity to render it is not — a finding is what a *court* can hold, a Thread truth is not. PR #362 `§B.5` (`:249`) Record stages are act-declared, never MATTER-advanced; `T-o` seat revocation (`01_AXIOMS.md:1160`) is what a sentence *is*; `09_WORKED_EXAMPLES.md:131 §3.1` the chain, `:147 §3.2` "excommunication is not a flag". PR #357: `open_case` (`verb_table.yaml:345`, eligibility `assumption`, H-52 `hole_register.yaml:594`), `determine` (`:156`, `eligibility: ["remit:determine"]` :160, writes `Tenure.degree` :162; H-32 `:346`).

**(d) SEQUENCE.**

```
S1  [gate][write] open_case — actor: the inquisitor via a seat whose remit holds determine   H-52 (see k1)
    S1.1 [gate] formal_grounds_check RESTORED: CI ≥ 40 ∧ L ≥ 4 ∧ (ledger_get("Leverage", f"evidence:{accused}").value ≥ 3
              ∨ ledger_has("Debt", violated) ∨ count(ledger_get("Precedent", f"conviction:{accused}")) ≥ 2)     tribunal.py:73; ledger.py:61-65
    S1.2 [gate] uniqueness: one active case per accused per jurisdiction = ledger_add dedupe by (kind,key)     ledger.py:47; v30 G-30
    S1.3 [write] LedgerTag(kind="Leverage", key=f"case:{accused}", value=evidence_count, ttl=declared term 2..4)   T-n; the ONLY stored scalar
    S1.4 [emit]  queue_scene("inquiry", ctx={accused, inquisitor, jurisdiction})                              scene_slate.py:34; recurs per season
S2  [loop over seasons ≤ term] interrogation — Bout(inquisition_hearing_venue, burden ACCUSER, adjudicator expert_judge, armature: opponent_is_adjudicator=True)
    S2.1 [branch] moves; side B (accused) has NO `support` and NO corroboration (v30 §7.1; §1 dodge finding)   venue flag → SelfGating
    S2.2 [gate]   faults: accused evasion_strikes=1 (silence convicts); inquisitor barred-device → veto (acquits)
    S2.3 [write]  Evidence Track: advance_evidence(case, Δ) (fieldwork.py:54, FI-owned, stub) refreshes the Leverage tag value
    S2.4 [emit]   beats; scene.dialogue optional
    reads: Dossier (Findings as EvidenceItems), CI clock (world.clocks['CI']); writes: the tag via the inquisitor's act only
S3  [gate] Stay — invoke_stay (parliamentary_stay.py:54) iff CI < STAY_CI_AVAILABILITY_MAX (:37)          ID-17: a band on a Query, not a flag
    S3.1 [branch] a passed Stay = shift to JURISDICTION stasis (primitives.py:14 LADDER; rhetoric.py:172 is_pre_merits) for one season: the case sleeps, the tag's ttl does not tick
    S3.2 resolve_stay_lift (:101, zero callers today) becomes the lift at next season
S4  [branch][write] determine — actor: the judge seat; margin = ProofBar.margin (net − bar); veto from S2.2
    Overwhelming → finding guilty + sentence: revoke (T-o) / attempt_excommunication (excommunication.py:78)   writes Tenure close + Precedent(conviction)
    Success      → finding guilty; Precedent(f"conviction:{accused}", ttl=None)
    Partial      → inconclusive; tag survives; may resume if evidence reaches 3 within 4 seasons (SYSTEM_MAP §2.3 SuspendedInsufficient)
    Failure      → exonerated; Precedent(f"acquitted:{accused}"); re-file needs fresh evidence (Let It Ride); Renown +1 non-Church (v30 :457-468)
    S4.1 [emit] scene.investigation_resolved{subject_id, finding, public, sentence}                          KEY_INDEX.md:948
S5  [branch] closures at any phase: inquisitor death/demotion/reassignment, accused death/defection/protection/conversion (v30 :457-468) — each is an Event that ends the tag (ledger_sweep or the closing act); none is MATTER
```

**(e) SHAPE.** Modules: `modes.py` (`PROCEEDINGS["church_tribunal"]` gains `burden: "ACCUSER"`, `win` = `ProofBar(bar)`; the biased start deleted), `resolver.py` (`margin()`), `tribunal.py` (FA-owned: restore the guard), `parliamentary_stay.py` (wire `resolve_stay_lift`). Owned state: **none new** (the Case is a `LedgerTag` + a recurring `SceneSlot`; the stage is a `KeyLog` Query — §2.3). Params: `open_case(actor, via, accused, jurisdiction) -> Receipt | Refusal`; `determine(actor, via, case) -> Receipt`. Gate: `Refusal(eligibility)` (no `determine` remit), `Refusal(grounds)` (S1.1 false), `Refusal(duplicate)` (S1.2), `Refusal(depth_cap)`. Receipt on every write. `Act.actor: PersonId` — the inquisitor and the judge are Persons in seats, never "the Church" (§B.6.1). Degree-keyed column: on `determine`'s `contests:` row (H-98's degree source): as S4. Veto = a clinch against the burden-holder demotes to Failure; a clinch against the accused is not a veto — it is the burden met (Fork A's stall semantics, `ProofBar:71-72`). Refusal kinds: four above.

**(f) Keys.** Writes `scene.investigation_resolved` (exists; add `social_contest` to producers — registry row, IN). Reads `CI` (clock), `state.opinion_revised`. **NEW keys: none.** Descriptors: no new descriptor.

**(g) Reuse ledger.** `inquisition_hearing_venue` (`modes.py:181`), `excommunication_court_venue` (`:200`), `ProofBar`, `DefeatCatalogue(evasion_strikes=1)`, `Stasis` FACT/JURISDICTION, `is_pre_merits`, `armature` + `appraise_armature` (`appraise.py:140`; the accused may appraise the judge — critique adjudicator FG-3's residue, needing no new mechanic), `invoke_stay`/`resolve_stay_lift`, `formal_grounds_check`/`run_excommunication_tribunal` (`tribunal.py:87`), `attempt_excommunication`, `Dossier`/`EvidenceItem`, `queue_scene`, `LedgerTag`, `degree_from_net` + `CONTEST_DEGREE_EXTENSION` (`degree_extension.py:87`, may only demote — I-8).

**(h) Invariants.**

| id | invariant | grade |
|---|---|---|
| I-I1 | the burden-holder loses the stasis on a stall | MECHANICAL (`ProofBar:71-72` closing → defender) |
| I-I2 | a finding is written by `determine` through the gate, never by the seam | STRUCTURAL (no token) · MECHANICAL (gate) |
| I-I3 | a stage exists only as an act's key in the log | MECHANICAL under `T-a` (nothing stores a stage) · CONVENTION today |
| I-I4 | the Stay is a band on a Query (`CI < 55`), never a stored flag | MECHANICAL (`STAY_CI_AVAILABILITY_MAX` gate) |
| I-I5 | one active case per accused per jurisdiction | MECHANICAL (`ledger_add` dedupe) |
| I-I6 | the accused never corroborates or `support`s | MECHANICAL once the venue flag routes through `SelfGating.licit` (`primitives.py:213`) · **CONVENTION today, and dodgeable — §1** |

**(i) Falsifiers.**

- F-I1 seeded, N ≥ 200: equal-faculty inquisitor vs accused at `ProofBar(2.5)` → acquittal ≥ 0.9; passive (`pass`) defence → conviction ≥ 0.9 (reproduces `VENUE_VALIDATION.md`; the numbers are the falsifier's *control*, not canon).
- **F-I2 (the attack that partly succeeds today):** accused plays `support` every exchange → today: zero faults, no silence clinch (`resolver.py:350-351`). After I-I6: `Refusal`/fault on the first `support`. Assert conviction(support-spam) ≥ conviction(pass) − ε. *Whether the dodge changes the conviction rate is unmeasured* — the inquisitor may still reach the bar; the clinch is dodged, the verdict may not be. Stated as an upper bound.
- F-I3 `formal_grounds_check(Evidence=2, no violation, convictions=1)` → False; `(Evidence=3)` → True; `(convictions=2)` → True.
- F-I4 `invoke_stay` at CI = 55 → `Refusal`, no key, tag ttl unchanged; at CI = 54 → one season added to the tag's clock, `resolve_stay_lift` fires next season.
- F-I5 `open_case` twice on one accused in one jurisdiction → second returns `Refusal(duplicate)` and the ledger has one tag.
- F-I6 same seed through `scene_dispatch._resolve_slot` with a `church_tribunal` slot → identical finding and identical `KeyLog.content_hash()` (the `m1_acceptance` row-2 instrument, reused).

**(j) Fairness / playability.** Per-decision consult load at the accused seat: ≤ 5 moves per interrogation + 1 Stay decision per season = **≤ 6/season**; the inquisitor is NPC-driven in every named case (a dominant inquisitor act is a *portrait* — `14_NERS.md` Rule 3 — unless the seat is playable, which is open and must be answered per seat before R is scorable). The accused's real play is *outside* the bout: the Stay (`CI < 55`) and — **the composition this subsystem is missing** — a negotiated abjuration (`00_synthesis.md:328`: "our Church Tribunal cannot end in a negotiated abjuration — historically the ordinary outcome"). So inquiry's Partial band should be able to call `settle()` (§3) with `burden` still ACCUSER on the record: compose, don't pick (politics D.4). Drama floor 0.14 at bar venues is intrinsic (`BALANCING_PASS…md` finding 1, held for Jordan D-5b) — not re-opened here.

**(k) Forks through the ladder.**

1. **H-52 `open_case` eligibility (absent).** Test 3: `09_WORKED_EXAMPLES.md:131 §3.1` the chain names the inquisitor's seat; test 4: `rosters.yaml:94 remit_acts` (issue, determine, confer, revoke, dispatch, convene) — a seat that can `determine` can open what it will determine. **Answered by precedent, provisional on PR #362's status.** Not escalated.
2. **H-32 judging set (assumption).** For inquiry the judging set is the seat holding `determine` = `adjudicator="expert_judge"` (`modes.py:497`). Answered by code. Not escalated.
3. *Silence convicts* → answered by precedent: `evasion_strikes=1` (`modes.py:199`), Nyāya. Not escalated.
4. Restore the tribunal record guard → answered by design doc (v30 `:626`) and by code (`tribunal.py:76-80` says so itself). Not escalated.
5. Multi-season vs single-scene → answered by design doc (v30 §7.3 `:447-451`). Not escalated.
6. A `Case` object with stages → **dissolved** as a false N-line (§2.3). Nothing escalates from inquiry.

---

## §5 · CONSENSUS — enact a unity

**(a) Conflict class, and why agon cannot.** Type 3 (politics D.1 `:192`): the procedure *removes* competition by design, and the suppressed competition returns as pathology — the holdout's veto-war. Do not force a Caillois family on it (D.3 `:202`). Agon cannot because it has a winner by construction; the tallies (`run_parliamentary_vote:125`, `coalition_vote:128`, `VoteAtClose` weighted) are majorities and cannot express *no decision until all assent*, a holdout, or an antibody. **Reconciling the two audits:** the three-lens (later) is right that the *majority tally* is the BG vote at another fidelity (`04_reductive…md:228`); the critique is right that the *unanimity procedure with a holdout* is expressible by no tally. The named-but-unimplemented `aggregation="unanimity_required"` (`dictionaries.py:686, :707`) is exactly where the two meet: a venue row with one new aggregation value.

**(b) Grounding.** **T0/T1** Great Law of Peace: Elder Brothers → Younger Brothers → Fire Keepers confirm; *"impeding a decision with insignificant objections or frivolous considerations"* forbidden — the antibody (politics model 7 `:90-94`). **T0** Benedictine Rule ch. 3; *ijmāʿ*; **T1** Gadaa. **T0 via T2** Lateran IV c.24 three modes (scrutiny · *compromissum* · quasi-inspiration), *maior et sanior pars* — and the sounder-part claim as a weapon *inside* the dispute (model 9 `:110`). **T1** the liberum veto (`…closing-findings.md` Part IX `:413-417`): unanimity + no randomization + external bribers ⇒ hold-up; success under fractionalization; a self-undermining equilibrium — the framework predicts both halves from the design alone. **T1** Venice: the mechanism *channels* maneuver (*broglio*, Part VIII.1); the lot-and-ballot as anti-capture, degrading with a small pool (Dowlen 2009; Frey–Osterloh–Rost 2022). `[PRIM]` Norse Lögrétta consensus → lot → majority (rhetoric §7.1, §12.8) → the terminal ladder in (d). **Measured (snapshot):** TallyAtClose tied votes 12–18% (`VENUE_VALIDATION.md`), `resist` inert at large pools (`AUDIT_RECONCILED.md` R1) — abstention must not be modelled as a subtraction from both pools. Game precedent I-2 recorded defeat (*senatus auctoritas*): a majority with a recorded dissent is a distinct outcome, not a weaker win.

**(c) Canon anchor.** v30 §10 `:589-611`; §7.2 `:407` adjudicator per faction incl. "RM: Mandate ≥ 3 organizers by consensus" and "Varfell: Jarl Assembly by quorum"; §6.3 chain cap 3 `:383`; Sacred Veto's self-interest cost (faction_layer §5.3, the tree's one existing antibody, per critique contest-locus FG-5). PR #362 `§E.2.5` (`01_AXIOMS.md:1438-1451`): an election is `determine`, not `confer`; `§G.2.9` procedure is required wherever order changes outcome (`04_CODE_ARCHITECTURE.md:12`); `AX-1`/`§B.6.1` — a faction never votes, its members do; `T-b` a threshold never produces an outcome (`01_AXIOMS.md:284`) — see I-C3.

**(d) SEQUENCE.**

```
S1  [write] convene — actor via a seat with convene remit (rosters.yaml:94); the matter = a Proposition P uttered by its mover; term declared (T-n)
    S1.1 [emit] queue_scene("consensus", ctx={P, rung, members: Query})             scene_slate.py:34
    judging_set = members present at rung (Query, never stored)                    → Panel.members (contract.py:38); three-lens N19: prior play writes the bench
S2  [loop ≤ exchanges] debate — Bout(assembly row, roles symmetric, adjudicator panel, armature: each member an ArmaturePosition, resistance standard)
    S2.1 [branch] moves; speaking order standing-indexed (framework.md B) — an ordering rule, §G.2.9
    S2.2 [gate]   faults per venue (no barred-device clinch in an assembly — README.md "an assembly disables the rhetorical-device bar")
    S2.3 [emit]   beats
S3  [gate] first ballot — VoteAtClose sampling pass retained PER MEMBER (N10 first ballot; zero new state)   resolver.py:124-145
S4  [branch] aggregation
    unanimity_required (NEW branch at dictionaries.py:707):
      all assent → Overwhelming (unity enacted)
      else [loop ≤ K holdout rounds]: each dissenting member must utter a counter-OUGHT and commit to it — a SIGNED act (AX-1, AX-6)
        [gate] antibody: cr5_self_backfire(style, landed, standing) keyed to the holdout's armature alignment with P (rhetoric.py:413; armature.py:436 dsigma)
               aligned objection → no cost (a principled veto is a portrait) ; misaligned/frivolous → Face cost (CR5 self-gating) and a Grudge tag against the holdout
        [branch] holdout withdraws (repudiate, verb_table.yaml:378) → re-ballot ; persists → next round
    weighted_by_standing (existing) → maior et sanior pars: margin = share − 0.5
S5  [branch][write] terminal — determine by the presiding seat; margin = VoteAtClose.margin; degree = degree_from_net
    Overwhelming → unanimous: Precedent(P, "by consensus", ttl=None)
    Success      → majority with recorded dissent: Precedent(P); Grudge per holdout (I-2 recorded defeat, senatus auctoritas)
    Partial      → compromissum: referred to a committee — queue_scene next season; chain cap 3 (v30 :383)
    Failure      → blocked: the matter lapses (calendar; Let It Ride) — OR, if PROCEEDINGS[name].on_hung == "lot": weighted draw seeded from rng, weight = final share (Venice/Lögrétta)
    S5.1 [emit] scene.contest_resolved{outcome, persuasion_track_final: margin}
FIDELITY: at auto fidelity the whole of S2–S4 is run_parliamentary_vote (parliamentary_vote.py:125) — the SAME matter, rendered at depth 0 (ED-SC-0013 duality, resolved); parity is measured, not asserted (i F-C3)
```

**(e) SHAPE.** Modules: `resolver.py` (`VoteAtClose.resolve` returns per-member ballots alongside the aggregate; `aggregation="unanimity_required"` implemented — `:128` grows one branch), `dictionaries.py` (`panel_win_condition` accepts the third value it already names), `modes.py` (an `assembly` proceeding row: `burden: "NONE"`, `adjudicator: "panel"`, `aggregation`, `on_hung ∈ {defer, lot}`, `holdout_rounds: K`), `rhetoric.py` (`cr5_self_backfire` reused unchanged). Owned state: **none new** (ballots are the sampling pass; holdouts are `commit` edges; the decision is a `Precedent` tag; the matter is a `SceneSlot`). Params: `determine(actor, via, matter) -> Receipt`; the holdout is `utter` + `commit` by the member. Query vs write: judging set, ballots, alignment = Queries; Precedent/Grudge/Tenure = writes through the gate with `Receipt`. Gate: `Refusal(no_quorum)` (v30 §7.2 "by quorum"; a `[SEED]` fraction on the venue), `Refusal(depth_cap)`, `Refusal(not_a_member)` (a Person outside the judging set attempting a ballot). **No refusal for a frivolous objection** — it is *costed* (the antibody), not refused: AX-1 lets a person act badly and the mechanism is the price. `Act.actor: PersonId` on every ballot and holdout. Degree column on `determine`'s `contests:` row: as S5. Veto: a clinch against the mover demotes.

**(f) Keys.** Writes `scene.contest_resolved` (exists). Reads `state.opinion_revised` (already consumed) as the members' prior. **NEW keys: none.**

**(g) Reuse ledger.** `VoteAtClose`, `Panel`, `panel_win_condition`, `PANEL_AGGREGATION` (ratified ED-1057), `ArmaturePosition`/`position_of`/`dsigma`, `cr5_self_backfire`, `Bout.resolve` loop, `queue_scene`, `LedgerTag` Precedent/Grudge, `run_parliamentary_vote` (the auto arm), `utter`/`commit`/`repudiate`/`convene`/`determine`, `degree_from_net`. **Deletions offered (the meta-rule):** `faction.py:128 coalition_vote` (zero production callers, fourth resolver — §1 defect 6) and `contest_legacy_stub.py:191 run_contest` (dead; keep `:67-71` constants until `margin()` lands, then they too go — `parliamentary_vote.py` reads them).

**(h) Invariants.**

| id | invariant | grade |
|---|---|---|
| I-C1 | no faction ballots; members are `PersonId` | STRUCTURAL under a checker (`claimants: PersonId[]`) · MECHANICAL (adapter refuses) |
| I-C2 | a holdout is a signed act with an author | MECHANICAL (gate refuses a ballot write without `actor`) — AX-6 |
| I-C3 | the tally is a Margin; the decision is a `determine` write — a threshold never produces the outcome | MECHANICAL (`T-b`; the count grades, the act writes) |
| I-C4 | the antibody's cost is proportional to armature misalignment, never flat | MECHANICAL by signature (`cr5_self_backfire(style, landed, my_standing)`) · the proportionality curve is a `[SEED]` |
| I-C5 | the auto arm and the played arm agree in band | MECHANICAL under the parity test (F-C3) · CONVENTION until it runs |
| I-C6 | a hung matter with `on_hung: lot` is drawn from the injected `rng`, never `random` | MECHANICAL (§2.1) |

**(i) Falsifiers.**

- F-C1 unanimity, one Conviction-aligned holdout → outcome Failure/blocked, holdout Face delta = 0; one misaligned holdout → same block, Face delta < 0 and a Grudge tag. The antibody is observable as the *difference* between the two runs.
- **F-C2 the liberum-veto reproduction:** N members, one with `fixed_lean="no"` (`faction.py:20`, the bribed deputy); under `unanimity_required`, P(block) → 1.0 as N grows; under `weighted_by_standing`, P(block) unchanged. If the framework's out-of-sample prediction does not reproduce, the branch is wrong, not the history.
- F-C3 parity, 200 seeds: `VoteAtClose` per-member (played) vs `run_parliamentary_vote` (auto) on the same matter and members → band agreement rate reported as a number; the acceptable rate is a `[SEED]` to declare (ED-SC-0011's harness, finally built; combat's r8 parity harness is the template).
- F-C4 symmetry: mover/opponent swapped over N seeds → mirrored margin.
- F-C5 `_KERNEL_EXPECTED` moves; `coalition_vote`'s `ck`s deleted, not skipped.

**(j) Fairness / playability.** Consult load per member per matter: 1 ballot + ≤ K holdout commits (K = 2 → **≤ 3**). Playable seats: any member (S-DOWN: a postless Person at the rung is a member in RM's "organizers"; S-UP: a demand travels up as a Petition carried to the convener — `14_NERS.md` §6). Dominance candidates: *always hold out* — bounded by Face when misaligned and by durable Grudges; *bribe one member* — a real act with a real cost, and the liberum-veto result says it *should* work under unanimity (that is the portrait the venue paints; a polity that chooses unanimity has chosen this). **Upper bounds; no sweep.** R is not scorable until "which seats does a campaign offer at start" is answered per seat (`14_NERS.md` §5).

**(k) Forks through the ladder.**

1. **ED-SC-0015 Mandate stacking (needs_jordan, HANDOFF_SC.md:204-230).** Test 4 (precedent): `ledger.py:36 LedgerTag(ttl=1)` + `:69 ledger_sweep` is a one-season modifier that restores itself; `:47 ledger_add` dedupes by `(kind, key)`, so a second vote in the same season *refreshes* the same tag rather than stacking. The "stack or cap" menu presupposes a stat write; with a transient tag there is nothing to stack. **Dissolved by precedent.** Defect 5 (§1) closes the same way — the `adjust("L", …)` at `parliamentary_vote.py:214` becomes a tag the echo reads. Close the row with this citation.
2. ED-SC-0011 parity harness → a measurement to run (F-C3), not a ruling. ED-SC-0013 → already resolved.
3. `unanimity_required` → answered by precedent: the ratified-alternative slot exists (`dictionaries.py:686`); implementing a named alternative is not a design change.
4. Sortition → answered by architecture as venue data (`on_hung`), one branch, watched (§2.6). Not escalated.
5. Acclamation (`CeremonialMode`, `modes.py:351`, critique caillois FG-3) → **out of scope**: nothing is at issue, so it is not a contest (framework.md B; HISTORICAL_VALIDATION.md "ceremonial is correctly held as a separate scaffold"). A unanimous first ballot with no debate (S3 before S2) *is* acclamation-shaped and needs no mode. Nothing escalates from consensus.

---

## §6 · Build sequence — with the execution artifact that makes each juncture DONE (§0.2)

Order: bottom-up (CLAUDE.md §0), most-reused first; the three-lens ranks `settle()` as the largest new design, so it goes last.

| step | what | done when (execution artifact) | control |
|---|---|---|---|
| **S0 spine** | `WinCondition.margin()` · `ContestOutcome` · `burden` on `PROCEEDINGS` and `GAMES` deleted · `armature=` passthrough + roles gate-off · `rng` injection · `contestant_from_person` · `KEY_TYPE_BY_SCENE` row | `python -m pytest engine/tests/test_contest_kernel.py` green with `_KERNEL_EXPECTED` at its new value; a seeded `scene_dispatch._resolve_slot` run on a `church_tribunal` slot returns a `ContestOutcome` and one key in the `KeyLog` | **the two campaign goldens must NOT move** (`engine/tests/test_mc_v18_regression.py` n=2/seed-0, `test_f7_smoke_oracle.py` n=8/seed-42): the spine is value-identical for agon; if they move, the spine changed agon |
| **S1 inquiry** | `church_tribunal` row → ProofBar/ACCUSER; guard restored (FA); `invoke_stay`/`resolve_stay_lift` wired; I-I6 venue flag; producer row | F-I1..F-I6 pass; a 4-season seeded run shows a case opened, stayed once, determined, with `scene.investigation_resolved` in the log and `KeyLog.content_hash()` stable across two runs | F-I1's acquittal/conviction rates within the snapshot's measured band (the falsifier's control) |
| **S2 consensus** | `unanimity_required` branch; per-member ballots retained; antibody via `cr5_self_backfire`; `assembly` row; `on_hung`; `coalition_vote` and `run_contest` deleted | F-C1..F-C5 pass; F-C2 prints P(block) vs N; F-C3 prints the parity rate | the auto arm (`run_parliamentary_vote`) unchanged in output on the goldens |
| **S3 negotiation** | `settle.py`; `private_negotiation` row `burden: NONE`, `settle: True`; split table single-owned; commits through the gate; treaty/Debt writes | F-N1..F-N5 pass; a seeded two-person negotiation through the seam produces either a `TreatyRecord` or a Grudge tag, never both, and no global-random state change | **gated on §3(k)1** (the one `needs_jordan`); until ruled, build with the cross-season default and mark the binding PROVISIONAL |
| **S4 composition** | inquiry Partial → `settle()` (abjuration); consensus Partial → committee `queue_scene` | one seeded run in which a tribunal ends in a negotiated abjuration | — |

`tools/m1_acceptance.py` row 1 (`mc_v18` probe) is the instrument that would notice a spine regression; row 4 is doc-derived and must not be cited (CLAUDE.md §0.2).

**Registry edits that ride along (not code):** `rosters.yaml` prizes `+"a finding"`, `+"a matter"` (PR #357, held); `module_contracts.yaml:176,180 contest_side.a/b` → `kind: value` becomes `margin`; `KEY_INDEX.md:948` producers `+social_contest`; `references/restructure_ledger.md:1356-1357` → point at the tag; `registers/editorial_ledger_sc.jsonl` ED-SC-0020 and ED-SC-0015 closed with §2.1 / §5(k)1 citations; `id_reservations.yaml` — the SC lane's `next_free` could not be located by grep in this session (the lane blocks are commented at `:92-100`); allocate from the file, never max+1.

---

## §7 · The strongest case against this decomposition, the attacks I ran, and the grade

**7.1 The framing overclaims.** The three-lens audit says *abandon the four-GAMES framing*; this document agrees (§2) — so its title names three "branches" that are, on its own showing, **two venue rows and one function**. A reader who builds three modules from this document has misread it. The honest name is "one spine, one `settle()`, two rows".

**7.2 It bets on a PROPOSED shape.** `Act`, `Seat`, `remit`, `Tenure.degree`, `determine`, the roster contract — all PR #362/#357, HELD BACK IN FULL. If they are vetoed, `margin()`, `burden`, the `rng`/armature passthrough and `settle()` survive unchanged (they are kernel-local); the write-gate and seat-remit language dies with them and the branches revert to writing `LedgerTag`s directly. The decomposition was cut so that the veto costs the seam vocabulary, not the mechanics — but that is a claim about a future veto, not a measured one.

**7.3 Attacks run, and their results (an attack that fails is a result).**

| attack | result |
|---|---|
| "`VoteAtClose` returns a *side*, so consensus violates *margin never a winner*" | **FAILS.** Weighted share − 0.5 is a margin; the side is derivable from its sign; the band view stays for `narrative.py`. I-N1/I-C3 hold |
| "`LedgerTag` cannot carry a Debt *between two Persons*" | **SUCCEEDS.** Tags live on `Settlement.ledger`; there is no holder. Recorded as the SE-owned custody gap (§2.4), not hidden |
| "The negotiation binding question is answerable by test 5" | **FAILS to close it.** Architecture gives a default; the consequence (two-season binding) is a game choice. It escalates — the only one |
| "*Silence convicts* is already MECHANICAL via `evasion_strikes=1`" | **PARTLY SUCCEEDS against the kernel:** `support` dodges the clinch with no fault (`resolver.py:350-351`). Fixed by I-I6; the *rate* effect is unmeasured (F-I2) |
| "A Case needs stages, so a Record with stages is necessary" | **FAILS, against this document's own first draft** — a false N-line (§2.3). The `KeyLog` does the job |
| "The `on_hung: lot` field is a false N-line (chain contests already defer)" | **INCONCLUSIVE.** Deferral ≠ an anti-capture terminal; but nothing in the tree *needs* the terminal yet. Kept at medium confidence and watched (§2.6). If a later pass cuts it, cut it |
| "Faction-as-claimant is STRUCTURAL in PR #362, so nothing here can run through the seam today" | **SUCCEEDS.** Until `_emergency_council_parties` returns Persons, every branch is unreachable from production except through the adapter's refusal. Named in §1 and §2.4; not fixable in SC |

**7.4 Asymmetric skepticism check.** I accepted the critique's favourable "sound/high" verdicts on mixed-motive FG-1/2 and contest-locus FG-3 on the strength of its own 46-agent verifier — which was self-authored (its header says so). Under the same rule I applied to its "already-handled" verdicts (re-verified against the tree), those favourable ones are **PROVISIONAL**: their locations verified, their leverage not re-measured here.

**7.5 "No dominant option" is an upper bound everywhere.** No AI-vs-AI best-response sweep was run for any branch (ED-SC-0021's falsifier remains unrun; only combat's r8 parity harness exists). Every (j) subsection is a bound, not an estimate. The analytic-narratives hazard (`machination…md` VII.7) applies to §5(b): the liberum-veto reproduction F-C2 is the one place the history was given a chance to break the design, which is why it is a falsifier and not a citation.

**7.6 Paper vs executes, per branch (CLAUDE.md §0.2).** Spine: **paper.** Inquiry: **paper** (its venue, win-condition, tribunal, stay and evidence primitives execute today in isolation; the sequence does not). Consensus: **paper** (`VoteAtClose` weighted executes; the unanimity branch, the antibody path and the parity harness do not). Negotiation: **paper** (`settle()` does not exist). Nothing in this document runs, and it stays paper until S0's artifact exists.

**7.7 The prior NERS P2s, dispositioned (the coordinator asked).** SC3 (genre 0.5 near-inert at R=1), SC4 (Regroup-on-Spent dominant), SC5 (Focus-1 Regroup trap) were graded against the L1 canonical model (Argue pool / Composure / Regroup forfeit). In the live kernel: there is no genre-weight multiplier on margin — CR4 maps stasis→genre affinity as δσ in `armature.py`, unreachable from the seam (defect 1), so **SC3 is irrelevant to the substrate that runs and unmeasured on the one that should**; `Regroup` is not a `Move` (`VALID_KINDS`, `resolver.py:34`) — its nearest kin, `pass`, *accrues a fault toward the silence clinch* (`resolver.py:345-348`), the inverse incentive, so the SC4 loop cannot form, and `Reserve.REGAIN = 4` is flat, not Focus-derived (`primitives.py:52`), so SC5's trap has no mechanism — **SC4/SC5 irrelevant by retirement (test 2)**, with the caveat that `support`'s net-positive regroup (+2 reserve per move, no fault) is the *new* shape of the same question and is named in §1 rather than left unmeasured under an old label. Rule 1 re-grade: E is not scored here as an axis; the spine's deletions (GAMES, `game=`, `coalition_vote`, `run_contest`, biased starts, `tracker_mode`) against six cut false N-lines are the ratio, and it moves the right way — provisionally, on paper.

**7.8 What an independent reviewer would add.** (i) The whole document assumes `contestant_from_person` bridges faculty to Persons; the mapping from `ATTRIBUTES` to `faculty` is exactly the "one line that does not ship" the three-lens named (`04_reductive…md:210-212`) — if that line is wrong, every branch is wrong the same way. (ii) The `[SEED]`s this document refuses to name (K holdout rounds, quorum fraction, the parity tolerance, F-N4's symmetry tolerance) are where a builder will invent numbers; each is marked as a declared `[SEED]`, and the research licenses none of them (§9.7).

---

*End. One file. Nothing else was created or edited.*
