# Evaluation of workplan v11, part 5: lane E1, carry-forward blocks (verbatim)

## Status: EVALUATION RECORD, assembled (stage 5 of `STAGES.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when workplan v12 is adopted)

**What this part is.** The carry-forward blocks of lane E1, copied by script from `master/eval/E1.md` lines 2032 to 3505, byte for byte; nothing below the rule was retyped or edited. Line numbers cited in the settlement ledger (`V11_EVALUATION_part2.md`) are those of the lane file, so a row of this part is found there as `E1:<line>`. Where the ledger re-dispositions a row, the ledger governs and the copy below keeps the lane's original call as the record.

---

### FA-01

card row (`valoria_master_workplan_v11_part3.md`):

```
| FA-01 | #445 P-3; FORCE-FOREIGN's cast: seat faction heads, let a head act, give the foreign faction a demand | The trade-demand clause only, released from M11 (ED-IN-0300) and built after CR-29 (B10-14) · LANDED-NARROWED (mechanism and content landed; what remains is the trade-demand clause, which waits on CR-29; `ED-IN-0298` stays open as a build, its §C.6 authorization answered by ED-IN-0300) | M | CR-29 | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:113-124`):

````
### FA-01 — #445 P-3; FORCE-FOREIGN's cast: seat faction heads, let a head act, give the foreign faction a demand (FA) · BATCH B10-17 · STATE LANDED-NARROWED (mechanism and content landed; what remains is the trade-demand clause, released from M11 and HELD on CR-29) · R R-04
- WHAT: Remaining: the Schoenland trade-demand clause. A foreign seat offers a `covenant` to a realm seat-holder `via` its seat through the real chooser, gated on a read of the realm's perceived weakness from an existing Query, never a stored field. The head-seating mechanism and the foreign cast have landed.
- LANDED ALREADY: mechanism `42c5588c` (B-J, `engine/season/tests/test_fa01_head_seats.py`; no data edit; a faction's act is a person's act `via` a seat, `Faction` has no verbs, A-4); content via IN-36 `7c59d74c` (B-V, closed `b1eabf5d`, PR #498; RS-21 item 4: one foreign faction, two seats, authored in `references/npc_registry.yaml`, the empire's head holds a seat in `build_realm(foreign=True)` only). B-V's measurement of the clause: carrier `covenant` offered by `off_kommerkiarios` on a goal-object kind `terms`, gated on `person_q.stability` below 0, MEASURED UNREACHABLE — every unrest sign in either arm is firsthand, none has a settlement for subject, the prefect held none at three placements, `legitimacy` read no negative value (H-234). Deps satisfied: IN-53 `5652e846`, IN-13 `2e19aee8`, B-M `be02666e`, B-I `9d93cfab`.
- REMAINING UNBUILT: [v9 WHAT, full text: what remains is the Schoenland trade-demand clause: a foreign seat offers a `covenant` to a realm seat-holder `via` its seat through the real chooser, no hand-built act; "perceived weakness" is read at the head's decision from an existing Query over regard, stance or holdings, never a stored field (which Query is the builder's) [ASSUMPTION]. This is the one copy of the clause (IN-36 and A-37's `Altonian pressure (IP)` row point here). Carrier `covenant` (IN-12 step 7, `664986ee`) [ASSUMPTION; medium; Jordan to correct]; revert: `exchange` (IN-33, restorable) is the carrier; clause edits `verb_table.yaml` or `loop/effects_information.py` only where the carrier's cell needs it.] the trade-demand clause; and the news path it needs: "a reach or border channel (a Layer-1 C.6 row), coercive deeds made matter of record, or the clause struck (`ED-IN-0298`, H-234)".
- GATE: released from M11 (answered (a): the superseding row of ED-IN-0300, 2026-10-26, ratified); the clause builds after CR-29. ED-IN-0298 (how news of coercion travels) stays open as a build: its superseding row of 2026-10-26 records the §C.6 authorization as answered by ED-IN-0300, with `needs_jordan` false, and the id closes at FA-01's commit; Layer-1 amendments marked (RULED) are Jordan's to authorize (G2). NEEDS gain CR-29 (the reach channel, B10-14), so this clause cannot build before CR-29 does. Collision matrix: `offices.yaml`, `harness/populated.py`, `references/npc_registry.yaml` (content). If the carrier reverts to `exchange`, REM-2B / IN-33 must be restored first [INFERRED from the revert wording].
- EXIT and FALSIFIER: EXIT (quoted; R-04's reading runs on Jordan's call, head P10 and V4) "`python -m engine.season.harness.aperture 4 0` (R-04's measure, `requirements.yaml:684`; about 25 minutes) shows an act whose actor is a faction head executing with `via` set. Content and clause: same command, cast on, lists the offering seat's `covenant` as offered >= 1 with the realm's answer (`commit` or refusal) in the per-verb line, and with cast off the realm hash byte-identical to today (IN-36's control)". FALSIFIER "remove the head's seat and the same act refuses; at control `offices.yaml` names a faction on its offices for five factions only (`grep -E '^    faction:' engine/season/offices.yaml | sort | uniq -c`, read 2026-10-06: Crown 8, Church of Solmund 1, Hafenmark 1, Restoration Movement 1, Varfell 1, null 17). The clause: two seeded realms whose weakness input differs give different offered counts (a demand offered at the same count whatever the realm's state is the clock the N-line cuts, and the clause is wrong)." Read under head §0.5 (relaxed exit: hand-built-world falsifier suffices; the realm count is recorded, not required).
- HASH MOVERS: declared — the cast and the clause (cast on); pre-change `build_realm(0)` hash read on the base commit first.
- HOLES AND LEDGER IDS: ED-IN-0298 (partial since 2026-10-26: the §C.6 authorization answered by ED-IN-0300, the build open; `needs_jordan` false), H-234, H-58, #457 D4, RS-21 item 4, A-4, A-37; IN-36, IN-12 step 7, IN-33, IN-53, IN-13.
- ASKS ATTACHED: ED-IN-0298 — how news of coercion reaches a foreign prefect: reach/border channel, coercion as matter of record, or strike the clause; the plan's route is CR-29's reach channel, which is released from M11 (`-05`; ED-IN-0300). Also #457 D4 ANSWERED [medium; Jordan to correct]; J-8 partly answered [medium] (`dispatch` stays in the generic remit; per-post naming deferred by Jordan).
- RE-BASE: B-V (#498) landed the content and measured the clause; the "remainder" PR #499 ("Katepano presses the capital; FA-01 clause held (ED-IN-0298)") followed. v9's entry records both. None found since B-V. FA-04..FA-06 are B-X's (no part-7 entry).
- SOURCE: `v9_p7:119-125` (alias FA-02 = IN-30 at `:117`); state-index row `v9.md:292`.

````

### CR-91

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-91 | The casus-belli carrier: a claim to a territory is a Proposition `claim:<faction>:<rung>` on CP-T09-02's war/creed shape, uttered only on a ground from the closed roster `casus_grounds:` (a seizure from the claimant's faction, a seat that once held it, a refused succession, the Church's ground under a held theocratic war); `declare` takes a held claim as occasion; `march`'s gate admits a live claim or a civil war; `faction_q.civil_war` a reading over the vassals' `oblige` edges; at believed breakdown a vassal head's `declare` against the sovereign's faction needs no ground (`ED-IN-0317`; resolves CP-T09-02's and IN-36's carrier gap; the arc fold of 2026-11-05) | BUILD | M (`march` admits fewer) | CP-T09-02, CP-T09-04, CR-86 (landed `83715fd6`) | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:201-213`):

````
### CR-91 — The casus belli carrier, `march`'s claim gate and civil war (FA/IN) · BATCH B10-17b (first: CR-91 → CR-89 (1) → …) · STATE BUILD (hash MOVER: `march` admits fewer) · R R-04 (contributor), R-05 (`declare`, `march`)
- WHAT: `ED-IN-0317` (Jordan, 2026-11-04): a march needs a casus belli, a claim to the target territory held by the marcher, his faction or his office, civil war excepted. No carrier exists (`-04` part 2 IN-36's `[GAP: carrier]`, whose residue MERGES here; CP-T09-02's home lists "a casus-belli gate on `march`" as not built, direction 8, which the ruling supersedes, as it supersedes M10 (b), `-05`). The plan reference is `proposals/2026-11-05-unified-design-and-build-plan.md` Part 3 (d) (reference).
- LANDED ALREADY: by B10-17's close one, CP-T09-02's `declare` and its war Proposition and target set, and CP-T09-04's `occupying_faction` path; IN-36's interim march cap (B10-17, first); `faction_q.at_war`; CR-86's vassal `oblige` edges (B10-10, landed `83715fd6`).
- REMAINING UNBUILT: (1) the **carrier**: a claim to a territory is a Proposition on the war/creed shape CP-T09-02 decides, `claim:<faction>:<rung>`, uttered by a person whose faction, office or holding has a GROUND from the closed roster `rosters.yaml: casus_grounds:`, read at RESOLVE: (i) the rung was seized from the claimant's faction (`rung.seized` in the log); (ii) his seat once held it (an ended `hold`); (iii) a succession to it was refused (`succession.refused`); (iv) the Church's ground, a Church seat in its subtree, only under a held theocratic declaration; without a ground the `utter` is refused (a refusal kind per conjunct, `04` invariant 4). (2) `declare` takes a held claim as occasion; its war Proposition's target set is the claimed rungs. (3) **`march`'s gate** (`verb_table.yaml`, `requires_typed`; `data/requires.py`): the marcher, his faction or his office holds a live claim on the target, OR his faction is at civil war with the target's; IN-36's interim cap is superseded by it, as IN-36's entry states (its (a), "superseded by (b) once (b) is built"). (4) **civil war** a reading, `faction_q.civil_war(w, a, b)` = `at_war(w, a, b)` with both heads under the sovereign's purview (CR-86's oblige edges); at believed breakdown (CR-89) a vassal head's `declare` against the sovereign's faction needs no ground (wired by CR-89 commit (3), shipped off). (5) the theocratic attempt is the Church head's `declare` of `war:church:realm` (opened by CR-89's CI ≥ 60 trigger), under which the Church's officers' `seize` runs on the existing `occupying_faction` path; nothing names a territory or a date.
- GATE: B10-17b, first. NEEDS: CP-T09-02, CP-T09-04 (B10-17), CR-86 (landed `83715fd6`); `ED-IN-0317`.
- EXIT and FALSIFIER: a planted seizure gives the loser ground (i) and his claim executes; with no ground it is refused; a `march` with no claim and no civil war is refused, with one admitted; at planted breakdown a groundless vassal `declare` executes, below it is refused. CONTROL: `casus_grounds` empty reproduces the pre-item refusals.
- HASH MOVERS: declared MOVER (`march` admits fewer); its pre-change reading B10-17's close reading @sha (P14).
- HOLES AND LEDGER IDS: `ED-IN-0317`; H-175; IN-36's casus-belli residue (merged here); M10 (superseded); ED-IN-0346 (its correction (5)).
- ASKS ATTACHED: none open.
- RE-BASE: CP-T09-02's landed war Proposition and target set, `march`'s `requires_typed` and IN-36's landed cap by symbol; `succession.refused` and the ended-`hold` accessor.
- BUILDER: opus. VERB CLUSTER: yes (P13).
- SOURCE: `ED-IN-0317`; `proposals/2026-11-05-unified-design-and-build-plan.md` Part 2 C7, Part 3 (d) (reference).

````

### CR-89

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-89 | The clocks as folds of the log: Church Influence and Turmoil as `rosters.yaml: clocks:` rows (feeders by Event kind, bands as fixtures), one `clock_fold` read world-side and person-side over held claims, no matrix row; the breaking point `sittings_failed`; "the nation functions" as a goal row; each band trigger shipped off and flipped only on CR-90's reading (`ED-IN-0339`, `ED-IN-0341`, `ED-IN-0343` to `ED-IN-0345`; the arc fold of 2026-11-05) | BUILD in four commits: (1) roster, loader, fold and readers; (2) `sittings_failed`; (3) each trigger, shipped off; (4) each flip, one commit each | E (commits 1-3); M (each flip) | CR-91, CR-86 (landed `83715fd6`), CR-29, CR-34 (landed `67f118dd`), CP-T09-02, CP-T09-04 | the arc's target share (default in force, head §6 risk 4 (a)) | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:175-187`):

````
### CR-89 — The clocks (Church Influence, Turmoil) as folds of the log, the breaking point, "the nation functions", and the band triggers, each shipped off (IN/FA/SC) · BATCH B10-17b (after CR-91: CR-91 → CR-89 (1) → CR-89 (2) → CR-90 → CR-88's build → CR-89 (3) → CR-89 (4)) · STATE BUILD in four commits · R R-04 (contributor), R-02 (contributor)
- WHAT: `ED-IN-0339` (the stakes ratchet among the four powers), `ED-IN-0341` (not scripted; conditioned to near-inevitability), `ED-IN-0343` (stored clocks and counters belong to the game; Church Influence drives a theocratic seizure), `ED-IN-0344` (clocks are not contrary to emergence), `ED-IN-0345` (a clock is an accumulation of world events that triggers behaviour). Two clocks, the minimum the arc needs: **Church Influence (CI)**, 0-100, start 28, and **Turmoil**, 0-10, start 0 (the archived values, `[ASSUMPTION; medium; Jordan to correct]` as fixtures). The form: the STORE is `w.log`; a clock is a roster row plus one fold, so nothing is written twice (`CLAUDE.md` §0.05 cl. 3) and no `write_matrix.yaml` row is added. Which ratified cuts survive is the plan reference's C4: lifted for a clock and a threshold; surviving for a firing condition, an authored outcome, an actorless event and any clock that moves with no event (Layer 1's three licensed clocks, `architecture/holonic_ARCHITECTURE.md` §25.1; `04` loader invariant 5). The plan reference is `proposals/2026-11-05-unified-design-and-build-plan.md` Part 3 (b), (c), (e) (reference).
- LANDED ALREADY: `w.log` (Events persist); `data/verbs.py::EMITTED_KINDS`; the goal-row shape (`data/goals.py`); `own_stance_declines`; the σ-leverage μ-shift route at RESOLVE (`modules/social_contest/roll.py`, obstacle terms). The rosters note "NOT CARRIED, BY THE CUTS … no clock" (`rosters.yaml`, located by those words) stays as history.
- REMAINING UNBUILT: **Commit (1)** (EQUAL): `rosters.yaml: clocks:` (per clock `range`, `start`, `season_cap`, `feeders` of `{kind, sign, weight, actor_faction, against}`, `bands`), its loader in `data/`, fixtures in `data/fixtures.py`; one pure `clock_fold(events, row)` in `queries/`; world-side `world_q.clock(w, name, tick=None)` over `w.log`, attribution reading the causing act's actor and his faction at that tick `[UNVERIFIED: the act store's reach from world_q]`; person-side `person_q.believed_clock(p, name)`, the same fold over the Events of feeder kinds of which `p` holds a claim, distinct origins once (`ED-IN-0322`) `[UNVERIFIED: that a deposited claim keeps its Event kind and causing act; if not, a closed kind-to-predicate map in the same roster, decided at the re-base]`; one line beside the rosters' cuts note pointing at `clocks:` and `ED-IN-0343`. Feeders (weights shipped at 1 per Event `[ASSUMPTION; medium; Jordan to correct; revert: per-kind weights from the archived tables]`; CI's season cap ±5) as the plan reference's feeder table states; no row names a person or seat. **Commit (2)** (EQUAL): `world_q.sittings_failed(w, arrangement, window)` and its person twin; breakdown a conjunction read where used (believed Turmoil ≥ Crisis and believed `sittings_failed ≥ fx.breakdown_sittings`, 2 of the last 3) `[ASSUMPTION; medium; Jordan to correct; revert: Turmoil alone]`; nothing stores "broken". **Commit (3)** (EQUAL, each shipped off): each band's trigger through an existing term (the plan reference's band table: CI ≥ 40 a pursuit gain on `seize`, `establish`, `open_case` for Church members; CI ≥ 55 a μ-shift, never an Ob reduction; CI ≥ 60 the Church head's `declare` of the theocratic war (CR-91); CI ≥ 65 and ≥ 80 a decline weight on hostile verbs against a Church party; Turmoil ≥ 3 relieves CR-87's violence cost `[ASSUMPTION; medium; Jordan to correct; revert: 0]`; Turmoil ≥ 7 with breakdown, CR-91's groundless vassal `declare`); every head seat's goal row `nation_functions` (`[ASSUMPTION; medium; Jordan to correct; revert: no row]`). **Commit (4)**: each trigger's flip, one commit each, made only on CR-90's reading. Not built: Mending Stability, Institutional Pressure, faction stats, Accord, Popular Will, the Church Attention Pool, any passive per-season increment, a stored phase or one-shot flag, and the archived P = ((CI−60)/40)^3.3 as code (it is CR-90's reference only).
- GATE: B10-17b, after CR-91. NEEDS: CR-91, CR-86 (landed `83715fd6`), CR-29 (B10-14: REACH carries distant events), CR-34 (landed `67f118dd`: the declared disposal), CP-T09-02, CP-T09-04.
- EXIT and FALSIFIER: a hand-built log folds to its known value and clamps at cap and range; one planted Church `rung.seized` raises CI and Turmoil by one weight each, once; a person holding claims of half the Events believes half; an Event with no causing act is not counted; three planted sittings that dispose nothing read 3, one determination makes it 2; two heads at a planted war both form `convene` at the realm venue at believed Turmoil ≥ 3, and with the row off they do not. CONTROL: every weight 0 reproduces the start values; commits (1) to (3) hash EQUAL; each flip kept only if CR-90's arm moves the reading in the ruled direction and the strife guard closes no terminal route.
- HASH MOVERS: commits (1) to (3) EQUAL; each flip in (4) a declared MOVER, one commit each (P14). If the fold's measured cost breaks CR-82's run-time ceiling, the fallback is a barrier view; only if that fails, a stored carrier with a round-trip test `fold(w.log) == stored` `[ASSUMPTION; medium; Jordan to correct; revert: the stored carrier first]`.
- HOLES AND LEDGER IDS: `ED-IN-0339`, `ED-IN-0341`, `ED-IN-0343` to `ED-IN-0345`; ED-IN-0346 (its correction (1): which cuts survive).
- ASKS ATTACHED: none open. The arc's target share is a default in force (head §6 risk 4 (a)); no flip is kept for hitting a number.
- RE-BASE: `EMITTED_KINDS`, the claim's kind and causing-act fields, `occupying_faction`'s attribution and `bench_quorum`'s `convene.refused` by symbol; CR-91's landed war and claim Propositions; CR-82's run-time ceiling as recorded.
- BUILDER: opus.
- SOURCE: `ED-IN-0339`, `ED-IN-0341`, `ED-IN-0343` to `ED-IN-0345`; `proposals/2026-11-05-unified-design-and-build-plan.md` Part 2 C4, C10, C11, Part 3 (b), (c), (e) (reference).

````

### CR-90

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-90 | The arc instrument: a new harness reader (`python -m engine.season.harness.<name>`, the name chosen at build: `harness/arc.py` is taken by CL-THRUST B0.1's ARC reader) reads per seed the first season of each clock band, breakdown, the first claim, `declare`, civil war, theocratic `declare` and Church `rung.seized`, and whether parliament still determines after the first war; pooled shares with the seed spread; writes nothing (`ED-IN-0341`; `CLAUDE.md` §7's gap; the arc fold of 2026-11-05) | MEASURE (harness) | E | CR-89 | any pass bar is Jordan's | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:188-200`):

````
### CR-90 — The arc instrument: the first season of each band, breakdown, claim, declaration, civil war and Church seizure, per seed (IN) · BATCH B10-17b (directly after CR-89 (1) and (2), before CR-88's build and any flip) · STATE MEASURE (harness; hash EQUAL) · R — (an instrument; moves no row of THE NINE)
- WHAT: `ED-IN-0341` asks for an arc conditioned to near-inevitability; that is a campaign-level claim, and `CLAUDE.md` §7 names the campaign-level instrument as an open gap (`tools/balance_oracle.py` retired; `harness/arms.py` a one-mechanic season delta). A harness reader that reads the log and writes nothing, like `harness/strife.py`. The plan reference is `proposals/2026-11-05-unified-design-and-build-plan.md` Part 3 (h) (reference).
- LANDED ALREADY: the strife instrument's shape (`harness/strife.py`, seasons and seeds required); `harness/interactions.py` (the audit's reader). ⚠ `harness/arc.py` already exists (CL-THRUST B0.1's ARC reader and CR-68's `consequence_acts`), so the plan reference's `python -m engine.season.harness.arc` collides: this reader takes another module name, chosen at build (a plain word; `CLAUDE.md` §4).
- REMAINING UNBUILT: `python -m engine.season.harness.<name> <seasons> <seed>...` reads per seed the FIRST season of: each clock band crossed (the true fold, and the head seats' believed folds); breakdown; the first claim, `declare`, civil war, theocratic `declare`, Church `rung.seized`; and whether parliament still determines a matter after the first war. Pooled: the share of seeds reaching each mark by season N, with the seed spread.
- GATE: B10-17b, directly after CR-89 (1) and (2); its base reading taken with every trigger off. NEEDS: CR-89 (commits (1), (2)).
- EXIT and FALSIFIER: a planted log reads its known seasons; feeder weights 0 read "never" on every clock mark. CONTROL: triggers off against on, same seeds; equal arms mean the triggers do nothing. Runs at the batch's close at 8 seasons, at 24 on Jordan's call (head P10).
- HASH MOVERS: none (a reader; `content_hash` unchanged by a run).
- HOLES AND LEDGER IDS: `ED-IN-0341`; `CLAUDE.md` §7's gap; ED-IN-0346.
- ASKS ATTACHED: any pass bar is Jordan's. The reference reading (breakdown or a casus belli in at least 80% of seeds 0-9 by season 24, the off arm markedly fewer) is a default in force, recorded and never a bar (head §6 risk 4 (a)).
- RE-BASE: the names CR-89 and CR-91 landed (clock rows, claim and war Propositions); the module name free under `harness/`.
- BUILDER: sonnet.
- SOURCE: `ED-IN-0341`; `proposals/2026-11-05-unified-design-and-build-plan.md` Part 2 C13, Part 3 (h) (reference).

````

### CR-88

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-88 | Duty of office and the cost of betrayal: a person-side duty decline on opponent-rule verbs against his faction's head or officers, lifted only by `person_q.grievance_against` above a band (held deed claims from distinct origins); duty's positive half adds the faction's goals at `fx.duty_weight` (`ED-IN-0335`, `ED-IN-0338`; the arc fold of 2026-11-05) | DESIGN-FIRST (drafted beside B10-13 with CR-83; approved by ED-1094's merge default), then BUILD here | M (the build) | CR-86 (landed `83715fd6`), CR-83 (the design), CR-82 (landed `1ef8d273`), CR-90 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:161-174`):

````
### CR-88 — Duty of office and the cost of betrayal (IN/FA/SC) · BATCH B10-17b (DESIGN-FIRST, drafted beside B10-13 with CR-83; its BUILD in B10-17b after CR-90's base reading: CR-91 → CR-89 (1) → CR-89 (2) → CR-90 → CR-88's build → CR-89 (3) → CR-89 (4)) · STATE DESIGN-FIRST, then BUILD · R R-06 (contributor)
- WHAT: `ED-IN-0335` (Jordan, 2026-11-05): holding an office binds the holder to a duty to the office's and faction's tenets and goals; a major betrayal (attacking a faction member, let alone the head) needs a significant series of events, opinions and circumstances. `ED-IN-0338`: a faction's creed, goals and duties condition its officers as a strife flow conditions everyone. Diagnosis (the interaction audit, H5): nothing under `decision/` reads the officer's faction, office or goals; the refusal gate ships unarmed (`refusal_axis` None, `decision/options.py` `[UNVERIFIED: lines]`); the person-side declines do not touch hostile verbs; `faction_q.head` is None until CR-86 (landed `83715fd6`). The plan reference is `proposals/2026-11-05-unified-design-and-build-plan.md` Part 3 (f) (reference, `CLAUDE.md` §0.05).
- LANDED ALREADY: the person-side decline shapes `own_stance_declines` and `held_edge_declines` (a new loader is needed: the existing one refuses a member that writes no `Person.stance`); `person_q.deeds_judged` (IN-58's landed reader); `goals.expected`; by B10-10, CR-86's head seats and offices' factions (landed `83715fd6`); by B10-09, CR-82's retention.
- REMAINING UNBUILT: (design) ONE design file under `proposals/`, no code, drafted beside B10-13 with CR-83 (whose know-OF grade and opinion-persistence measurement it reads), naming: (1) the **duty decline**, a person-side block on the `own_stance_declines` shape: a person holding an office (his own `hold` on an Office whose faction is F) declines every opponent-rule verb (`subject_is_opponent`: per the audit accept, arrest, determine, fight, interrogate, march, speak) whose subject is F's head or an F office-holder, unless his betrayal reading exceeds `fx.betrayal_band`; (2) the **betrayal reading**, `person_q.grievance_against(p, q)`, computed when read: the deeds by `q` (or by F's officers acting through `q`'s seat) that `p`'s `deeds_judged` scores against his pursuits, kin and holdings, distinct origins only (`ED-IN-0322`), plus his stance row, plus a commitment to a rival creed; a build-time stance alone cannot clear the band (CR-87's loyalty fix); (3) **duty's positive half**: while he holds the office his score adds `goals.expected("faction", F)` at `fx.duty_weight` (seat-attached goal rows, G-09, stay Jordan's content, CL-THRUST B6.n; until authored the faction's goals stand in); (4) the re-point of CR-87's duel dispute conjunct from `deeds_judged` to `grievance_against`; (5) its falsifier and control. No stored opinion and no grudge carrier (CR-83 decides opinion persistence by measurement first). (build) in B10-17b, as the approved design states it.
- ADDED (ED-IN-0347, AR-52): the design also prices `accept` for an office holder by duty: a ruler's acceptance is costly unless the dispute bears on the realm and a duel could settle it (*"a king would see no reason to duel unless the country was at the brink of war and the duel could solve it somehow"*); the station read is an office's rank (`rung_kinds`), not `standing_of`.
- GATE: (design) drafted beside B10-13, approved by ED-1094's merge default; unapproved when B10-17b opens → this row moves to B10-Z as HELD and slots by R8 (`-03` §0; the CR-85 precedent). (build) B10-17b, after CR-90's base reading, before CR-89's triggers. NEEDS: CR-86 (head seats; landed `83715fd6`), CR-83's design, CR-82 (landed `1ef8d273`), CR-90 (its base reading); `ED-IN-0335`, `ED-IN-0338`.
- EXIT and FALSIFIER: (design) the file exists and states (1) to (5); no code. (build) the seed-0 Spymaster (after CR-87's loyalty fix) forms no hostile verb toward the King over the read horizon (the plan reference says four seasons; head P10 reads `aperture 3 0` at the close and four only on Jordan's call); three planted deeds by the King against her pursuits from three origins lift the decline; one origin three times does not. CONTROL: `fx.duty_weight` 0 and the band at +∞ reproduce the pre-item hash.
- HASH MOVERS: the design none; the build a declared MOVER (P14).
- HOLES AND LEDGER IDS: `ED-IN-0335`, `ED-IN-0338`, `ED-IN-0322`; G-09; ED-IN-0346.
- ASKS ATTACHED: none open; the band and weight are fixtures shipped as the design's reading rule states, each `[ASSUMPTION; medium; Jordan to correct; revert: fx.duty_weight 0, the band at +∞]`.
- RE-BASE: the decline loaders and `subject_is_opponent` by symbol; CR-83's approved design; CR-87's landed dispute conjunct; CR-86's `head_seat` rows (landed `83715fd6`).
- BUILDER: opus for the reading and the design (`valoria-author`), sonnet for the roster.
- SOURCE: `ED-IN-0335`, `ED-IN-0338`; `proposals/2026-11-05-unified-design-and-build-plan.md` Part 2 C3, C12, C14, Part 3 (f) (reference).

````

### CP-T10-06

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T10-06 | Kin: the releasable `kin` kind and authored edges (the news channel is CR-29's; it gains the kin-news half CR-29 enables, and its home decides whether to build it: no edge) | BUILD | M | H-209; not a dependency: ED-WR-0011 (a ruling already made) | — | `cp-world-travel-survival-npc-life`:265-291 |
```

entry (`2026-10-23-subsystem-completion-10-world-travel-survival-npc-life.md:265-292`):

````
### CP-T10-06 · Kin

- **Adds.**
  1. **A `kin` Tenure kind** (L18 M9): Person → Person, directed, its content from a `rosters.yaml: kin_roles` row
     `[spouse, parent, child, sibling]`, added to `tenure_kinds` (`rosters.yaml:130`). **Not** in `release`'s domain, on the `reside` and
     `detain` precedent (`rosters.yaml:105-129`): nobody resigns being someone's son. (L18 says the loader forces `release`'s domain to
     take it; the `reside` note shows a kind can stay outside it. [UNVERIFIED] at the loader.)
  2. **Authored only from canon.** An optional `kin:` field on rows of `references/npc_registry.yaml` (`{to: NPC-nnn, as: <kin_role>}`),
     loaded by `data/cast.py` (which already raises on a malformed row) and minted by `harness/populated.py` beside the person. A row
     whose text states no relation gets none: inventing a relation is the fabrication ED-WR-0011 and `npcs.yaml`'s header refuse for
     persons. The registry's `role:` lines name a royal family (King, Queen "Widow Regent if Almud eliminated", Prince "Heir Apparent",
     Princess "married to Doux Alexios Laskaris"; `references/npc_registry.yaml:577, 666, 705, 744`); only the Princess–Doux marriage is
     stated outright, so the rest are [UNVERIFIED] until a canon source is cited row by row.
  3. **A `kin` witness channel**: a sixth `rosters.yaml: witness_channels` member, its predicate in `epistemic.py` beside
     `_ch_witness_key` (`:543`): a person holding a live kin edge to an Event's subject or anchor receives it, source `told_by`, for the
     kinds in a closed `rosters.yaml: kin_news_kinds` row `[person.died, body.changed, condition.band_crossed, marriage.made]`.
     Precedence: after the told channels, before `post_remit` **[ASSUMPTION]**.
- **Readers** (so the carrier is not ID-13): the channel; CP-T10-07 (the heir); CP-T10-08; CP-T10-09; FA's IN-70 opinion (its kin term,
  FA's to take). **Not** seat succession: RS-27/RS-29 ruled the heir a title.
- **Primitives.** P11 (pairwise record), P27 (news that travels by relation), P30's input.
- **Hazard named.** H-209: a dead man's claim never becomes a question (he has no place). Nothing here depends on a question about the
  dead; CP-T10-07 forms from its own estate stamper and CP-T10-09 reads claims in `regard`.
- **Falsifier** (`test_kin.py`): the authored Princess–Doux pair gives two kin edges at build; the Doux dies far away and the Princess
  holds a `person.died` claim naming him, source `told_by`, while a non-kin beside her holds none. Mutation: drop the channel → red. A
  `kin:` row naming an absent id raises at load.
- **Control.** No `kin:` rows → no edges → the channel admits nobody → base hash. **Hash:** mover once rows are authored. **Revert:** the
  rows. **Size:** M.

````

### CP-T10-07

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T10-07 | An estate passes by its heir's claim (a hashed `estates` collection; the heir hears by `tell`; done live only when an estate `succeed` executes) | BUILD | M | CP-T10-06, IN-61 (landed `f9e4cef`), REM-21; H-206, H-230; not a dependency: CP-T02-01 (T10 :503: "its estate record does not wait on T02's CP-T02-01") | — | `cp-world-travel-survival-npc-life`:293-331 |
```

entry (`2026-10-23-subsystem-completion-10-world-travel-survival-npc-life.md:293-332`):

````
### CP-T10-07 · An estate passes by its heir's claim

- **Adds.**
  1. **A separate, non-broadcast estate record.** Seats are not this item's: T02's CP-T02-01 owns H-230's arm 2 (one `tenure.closed`
     Event per **Office** hold a death empties, broadcast by the chronicle), and this item neither widens it nor shares its change. A
     dead man's Record and Rung holds must not be listed among a broadcast Event's changes (that is H-206's option (b), unbuilt because
     those edges leave with him, `hole_register.yaml:4502`; broadcasting them would put every dead man's case files in every living
     ledger). Instead, inside the one death cascade (`World.remove_person`), before the dead man's own edges leave, the objects of his
     live `hold`s whose kind is in `estate_object_kinds` are recorded on a World-side record `w._estates[dead] = (objects, tick)`, on the
     precedent of `_departed` (where he stood, H-206, `state/world.py:757`). Nothing is deposited by it.
  2. **`heir_of(w, dead, obj)`** in `queries/world_q.py`: the first living person, by a `rosters.yaml: estate_heir_order` row
     `[spouse, child, sibling, parent]`, among those who **own** a kin edge naming `dead` that closed at his death; ties by id. It reads
     heir-owned edges only: the cascade sets `until` on every edge naming the dead (`state/world.py:755-759`), and an edge the survivor
     owns stays on the survivor's list, whereas the dead man's own edges leave with him (H-230, `hole_register.yaml:4814`).
  3. **How the heir comes to claim** (AX-2): he holds the death claim (CP-T10-06's kin channel). A stamper `estates_named(w, p)` on
     REM-21's `STAMPERS` registry offers, on that question, the objects of `w._estates[dead]` to `p` only when `p == heir_of(w, dead, obj)`
     — a person's own family's holdings as his own purview, on `larders_in_purview`'s shape (`world_q.py:2269`) **[ASSUMPTION; medium]**.
  4. **GV's `succeed`** (re-specified by IN-61 as the heir's own claim, GV's row by R-11) **accepts an estate object**, a Record or a Rung
     (a `rosters.yaml: estate_object_kinds` row `[Record, Rung]`), under the `inheritance` basis admitting exactly `heir_of` for an object
     in `w._estates[dead]`. The act opens the claimant's `hold` in one write (`give`'s shape). Offices stay on IN-61's `successions` route; Propositions are excluded (an
     utterance is its maker's).
- **Why a claim, not a transfer at MATTER.** RS-27 ("designated heir is not a verb but a status or title. the heir still has to claim
  their throne", quoted at `workplans/valoria_master_workplan_v9_part5.md:211`) is the precedent; one methodology for seats and estates
  (S); and `(Tenure, since)` is licensed at `[RES, ENC]` only (`write_matrix.yaml`), so an automatic opening at MATTER would need a new
  licence. The heir learns of the death through his own ledger (CP-T10-06's channel), and only he is offered the estate: nobody else's
  ledger fills with the dead man's papers.
- **Primitives.** P30 (heir transfer), P05 (each claimed hold is +1 budget point, so an inheritance buys acts).
- **Joins.** GV (IN-61, the `succeed` row, the `inheritance` basis); T02 (CP-T02-01's Office-only death Event is adopted as is for
  seats); FI (inherited case files and forged papers go to the heir,
  so evidence outlives its holder); FA (land held across a faction line by a widow).
- **Decision.** Claim the dead man's papers and land, or leave them; marry with an estate in view. **Unwatched:** holdings follow kin
  when nobody is looking; a dead minister's case file reaches his sister, who now holds the evidence.
- **Falsifier** (`test_estate.py`): a holder of a Record and a landholding dies far from his spouse; `w._estates` records both; she
  (and nobody else) is offered both; her `succeed` on the Record opens her `hold` and raises her `budget()` by 1; a person standing at
  the death holds the `person.died` claim but no claim naming the Record; a non-kin's claim is `succession.refused`; with a spouse and a
  child alive, the child's claim is refused. Mutations: `heir_of` ignores the order → the child is admitted → red; the estate objects
  ride the `person.died` Event's changes → the bystander holds a claim naming the Record → red.
- **Control.** `estate_object_kinds: []` → `_estates` is never written, no estate claim forms → base hash. **Hash:** mover on the on
  arm. **Revert:** the roster empty. **Size:** M.

````

### CP-T10-09

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T10-09 | Deeds done to me and mine (narrowed: a live `kin` edge in the judge's own `tenures` counts as an ally in `_bond`; no new kinds) | BUILD | M | CP-T10-06, IN-18 (its told channel, landed at B10-02; the held tail in B10-Z is not a dependency); not a dependency: IN-58 (narrowed at B10-09 close two, it hands on no state; the kin clause reads `tenures` directly) [INFERRED], ED-IN-0296 (the kin clause does not wait on M1) | — | `cp-world-travel-survival-npc-life`:353-369 |
```

entry (`2026-10-23-subsystem-completion-10-world-travel-survival-npc-life.md:353-370`):

````
### CP-T10-09 · Deeds done to me and mine

- **Adds.** In `person_q.regard`'s judged half (`person_q.py:393`, the one owner): a deed claim whose patient is the judge, or a person
  the judge holds a live kin edge to, adds `patient_gain × patient_valence[kind]` toward the deed's doer. A `rosters.yaml:
  patient_valence` row **[ASSUMPTION: `body.tended` +1, `record.given` +1, `person.died` −2, a fight's `body.changed` −1]**; fixture
  `patient_gain` **[ASSUMPTION: 0.5, the size of `judged_gain`]**. For the paired kinds (death, wound) the doer comes from IN-58's pairing
  in `deeds_judged`, the one route; [UNVERIFIED] that every listed kind's claim exposes its patient as `subject`.
- **Why it is not a second thumb** (NERS disqualifier 4): `deed_valence` (`person_q.py:371-379`) is the judge's pursuit lean on the
  kind and is blind to who received the deed; this is L18's M13 (a gift's effect on the receiver) and M10's kin slice.
- **Readers.** `regard` → `teller_weight` (`options.py:1515-1522`) and the score's regard term (IN-18 G1/G2). Vengeance as a *choice*
  still needs M6 (ED-IN-0296's declared arm, already Jordan's); not repeated.
- **Decision.** Tend, give and protect to earn trust; harm a man's kin and his whole house reads you lower. **Unwatched:** a healer's
  patients believe her; a dead man's brother distrusts the killer and everyone the killer tells him.
- **Falsifier** (`test_deeds_to_me.py`): A tends B → B's regard of A rises by `patient_gain` beyond the lean, while C (same pursuits,
  present) moves by the lean alone; A kills B's sibling → B's regard of A falls by `2 × patient_gain`. Mutation: key the term on the
  witness instead of the patient → C moves → red.
- **Control.** `patient_gain` 0 → base hash. **Hash:** mover on the on arm. **Revert:** the fixture. **Size:** S.

````

### CP-T10-01

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T10-01 | The journey is priced by its route (terrain by one extracted rule; pricing ships off: no position gives a chooser a person-side reading of a leg's price, **[GAP: unowned]**) | BUILD | M | CP-T09-08, REM-26, REM-29; H-140, H-168; not a dependency: IN-45 (cited as the precedent that answers H-140, not a prerequisite) | — | `cp-world-travel-survival-npc-life`:111-154 |
```

entry (`2026-10-23-subsystem-completion-10-world-travel-survival-npc-life.md:111-155`):

````
### CP-T10-01 · The journey is priced by its route

- **Adds.** A Query `route(w, a, b) -> (path, cost)` in `queries/world_q.py`: shortest path over `GEO: settlement_adjacency` (55 edges,
  one component of 37, diameter 8 edges; probe), each edge costing `terrain_cost_matrix[t]` of the settlement entered, where `t` is the
  terrain polygon containing its `coords` (`plains` where none does: 8 of 37, probe). A rung's route node is the settlement at or above it
  (a settlement rung is `set_` + its geography id, `harness/populated.py:850`); a rung above settlement kind, or a journey inside one
  settlement, costs the floor. **Leg points** = `max(1, ceil(cost / leg_unit))`, `leg_unit` a fixture **[ASSUMPTION: 2.0]**. Ties break on
  sorted ids, so the path is deterministic.
  - `_relocate` (`loop/effects_migration.py:119`, the one RESOLVE writer; `_eff_march` reaches it too) appends
    `(dest, points, path)` to `Person.travel_leg` on the on arm, where `path` is the tuple of settlement ids `route` returned (the
    origin is otherwise only on the closed `contain` edge, and a person may make several journeys a season, so MATTER could not recover
    it: the leg carries it, for CP-T10-02). On the off arm it appends the bare `dest`, as today. `budget.py:60` subtracts the sum of
    points × `budget_leg_penalty`, a bare id counting 1 point.
  - **Every leg writer goes through `_relocate`.** For a leg charged without a move (T04's siege leg: the army sits and pays), `_relocate`
    takes a `relocate=False` flag: the priced leg is appended and no `contain` edge closes or opens; the path is `route(origin, dest)` all
    the same. T09's `dispatch` (a dispatched man's journey) is acknowledged on the same terms: it calls `_relocate`, and the leg is
    priced on the person who travels.
  - **A journey that changes no presence is not formed, and one injected is declined** (`travel.blocked`, keyed `same_place`). H-140 is
    a RULING-kind row; it is answered at step 4 by precedent: IN-45 stopped `migrate` forming on a place "he already lives under" and
    `_eff_migrate` declines "a migration that changes no residence" (H-168; L17 S1 disposition 2).
  - `contain_path` stays a conjunct, so the border (§1) holds. The `move` → `travel` rename (L17, R-10) is not needed for this and is not
    bundled.
- **Owner artifacts.** `queries/world_q.py::route` (one owner of path and cost); `data/geography.py` (the season's existing reader of
  `GEO`, extended to `settlement_adjacency`, `terrain`, `terrain_cost_matrix`). `GEO` has **two** readers today: world-gen parses it
  independently in `harness/populated.py:773` (`_load(GEOGRAPHY)`), and `data/geography.py` reads it for the battle field. This item adds
  no third: `route` reads through `data/geography.py`, and routing world-gen's read through it too is a consolidation this item does not
  bundle. The file's own ownership move out of `systems/` is not this item's; fixtures `leg_unit`, `route_pricing` (the arm switch) in `data/fixtures.py`.
- **Primitives.** P05 (the budget is the price), P06 (a verb's price set by its object), TM10's leg.
- **Asymmetry (§0.1 pt 1).** `budget()` changes what it computes. Assignments of `Person.travel_leg` at HEAD: `effects_migration.py:119`
  (append), `loop/matter.py:651` (clear), `harness/probes.py:2942` (a probe sets bare strings: rewritten, or a bare id reads as 1 point).
  Readers: `budget.py:60`, `loop/deliberate.py:520` (the fingerprint; tuples stay hashable), `harness/soak.py:214`.
- **Decision handed to the chooser.** Go yourself or act where you stand; near business before far; a far journey early eats the season
  (a 4-point leg in round 0 leaves a budget-5 person nothing from round 1). **Unwatched:** officers who travel far act less that season;
  distance becomes who meets whom.
- **Falsifier** (`engine/season/tests/test_route_leg.py`, new): S-001 → S-002 prices 1 point; S-001 → S-013 (Aschenbach) prices
  `ceil(7.0 / 2.0) = 4` (probe: 5 edges, cost 7.0); after a round-0 journey to S-013 a hold-less person's `budget()` is 1; a same-place
  `move` forms no Candidate; a journey into T16 is still `travel.blocked`. Mutation: `route` returns cost 1 → the S-013 assertion reds.
- **Control.** `route_pricing` off → `_relocate` writes bare ids, so the leg's repr and the write deltas (both folded into
  `content_hash`, `state/world.py:1392-1393`) are unchanged → flat 1 point per leg → base hash at seeds 0–2, **except** for the same-place
  rule, which forms fewer `move`s and is a declared mover on both arms (it is not behind the switch). Paired arm (on vs off, same seeds): acts per acting
  person (act-store basis) and executed `move`s to a place other than the mover's own, which must rise from 16/16, 16/17, 10/12 "to own
  place" (T10 §9) — the observable the same-place rule exists for.
- **Hash.** Mover on the on arm (the leg's tuple repr is hashed, and budgets move); the same-place rule moves both arms. **Revert:** the
  fixture off; then the code. **Size:** M.

````

### CP-T10-03

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T10-03 | The year turns | BUILD: authors the home's `season_terms` row (year 4; winter yield 0.25, want 1.5, illness 2.0; other seasons 1.0, all [ASSUMPTION; medium; Jordan to correct]) and the `year_length` fixture, shipped 0 (calendar off); all three fields stay in the row (CP-T10-05 reads `illness`); flipping `year_length` to 4 is released (M6 taken) and lands as its own declared-mover commit directly after this one | E (the flip M) | CP-T10-02, REM-50; not a dependency: JQ-6 (closed by M6; the flip lands in this batch) | — | `cp-world-travel-survival-npc-life`:177-198 |
```

entry (`2026-10-23-subsystem-completion-10-world-travel-survival-npc-life.md:177-199`):

````
### CP-T10-03 · The year turns

- **Adds.** A fixture `year_length` read by `season_of_year` (`world_q.py:958`), decoupled from `season_factor_draw` (M-WT-2): `0`
  means "the draw table's length, if any", so every existing fixture world keeps its calendar; a declared draw table must then hold
  `year_length` entries or raise `Unspecified`. A `rosters.yaml: season_terms` row, one entry per season of the year, each with three
  multipliers: `yield` (on `season_factor_of`'s result, `world_q.py:967`, its one owner), `want` (on the per-head want inside
  `subsistence_draw`, `world_q.py:1024`, its one owner, so REM-50's `hunger` and MATTER's draw cannot disagree) and `illness` (read by
  CP-T10-05). **[ASSUMPTION: year 4; winter yield 0.25, want 1.5, illness 2.0; other seasons 1.0.]**
- **Cut from L17's M-WT-2:** the storm season refusing `sail`. The one `sea` edge (S-001 ↔ S-037) crosses the border, so the refusal has
  no reachable reader (§3).
- **Primitives.** P41 (the calendar presses), P20 (the draw scales), TM11's clock.
- **Asymmetry.** `season_of_year`'s result is unchanged wherever `year_length` is 0. Its readers: `season_factor_of` (today), and after
  this `subsistence_draw` and `body_hazard`.
- **Joins.** RB-5 (want → `demanded` → `hunger`; JQ-6's M-H2 sweep gains a season arm, the same instrument, no new one); EC (yield in
  the year); MB (a campaign season reads `season_of_year`).
- **Decision.** Stock before winter; travel in summer; a governor's relief `transfer` before the lean season. **Unwatched:** winter draws
  rise, REM-51's hunger crossings reach governors in winter, and sickness (CP-T10-05) rises with it.
- **Falsifier** (`test_calendar.py`): at `year_length` 4, tick 3 is season 3; a weight-2 cohort wants grain 6 at a winter tick and 4 at
  tick 0; `hunger(w, S)`'s cover falls in winter on unchanged stores. Mutation: apply `want` in MATTER instead of `subsistence_draw` →
  the Query and the draw disagree → red.
- **Control.** `year_length` 0 and `season_factor_draw` `()` → base hash; `test_season_weather.py`'s three-hash equality unchanged.
  **Hash:** mover on the on arm. **Revert:** `year_length` 0. **Size:** M.

````

### CL-EVENTS

card row (`valoria_master_workplan_v11_part3.md`):

```
| CL-EVENTS | The exogenous event channel, re-scoped to FORCE-WEATHER per territory, and the Tensions receiver as a world-generation draw (M16 taken (b): two of AX-5's three motions, matter and bodies, plus persons' own acts; the fourth motion is not taken (confirmed at the default, ED-IN-0301), blocks nothing and is not needed by commits (3) and (4)): four commits. Commit (1), landed in B10-05, keys `season_factor_of` on (world_seed, tick, territory rung id) with `ProduceInput.factor` per rung (an interface change, EQUAL at `()`); commit (2) here, the live arm `((0.5, 1.0, 2.0),)*4` `[ASSUMPTION; medium; Jordan to correct; revert: ()]`; the deck is not adopted as written, its climatic family the candidate source for the per-territory values Jordan sets. Commit (3), after CR-22: the Tensions receiver (`tensions.yaml` with `tensions: []`, one loader parsing card goals through `data/goals.py::parse`, `rosters.yaml: tension_effects: [goal, yield_scale]`, `territory_yield_scale = ()`, `build_realm(tensions=False)` drawing one card from the seed), read once at build by no step of the season loop `[ASSUMPTION; medium; Jordan to correct; revert: delete the registry, loader, roster, fixture member and switch]`. Commit (4), directly after (3): the archived six-card Tensions Deck as `[ASSUMPTION]` rows, each with its own revert (two of six keep their core; cards 3, 4 and 5 attention only; card 6 a motive toward one clerk seat), the switch staying off in v10 | BUILD | M (commit 2; commits 1, 3 and 4 EQUAL) | REM-50, REM-52, CP-T10-03; not a dependency: CR-22 (commits (3) and (4) follow it for the reading only; CR-22 needs this row) | — | `-05` M16; code report §14; `-04` CL-EVENTS |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:308-316`):

````
### CL-ATTR, CL-TROOP, CL-EVENTS, CL-THRUST — Design clusters (WR/IN/MB) · BATCH B10-19 (CL-EVENTS: B10-18) · STATE as listed (CL-ATTR narrowed to M24, the training composition, since J-T2 and M23 are answered by `ED-IN-0328`; CL-TROOP on M3; CL-THRUST's released pieces land in B10-02, B10-05 and B10-09, its other pieces held)
- **CL-CHAR** — the character template (`characters.yaml`, `template_of`, a seating step, the personal-input block): DELETED at B10-10's close (`0533c4da`). Absorbed by CR-20 (`c7764a5a`: its personal-input block and carrier), REM-30 (`fca48e4f`: the template's writer) and CR-33 (`6b068d8a`: the lifepaths as creation templates); the piece check found no reader of `template_of` or `characters.yaml` in `engine/` and no such file, so nothing remained as this row's remainder. CR-20's exit, quoted as the row required: two persons with attributes 2 and 6 on the vocation's attribute and no held key roll pools 2 and 6 and are opposed at Ob 1 and 3; a value written under a key that is not one of the ten is refused; a cast row's legacy spelling resolves to its key; CONTROL: an all-absent realm's act log equals the pre-change tree's (only the `repr` hash moves). The suite's dossier authoring layer (`proposals/2026-10-28-content-architecture-suite/02_P1_templates.md` §1) was recorded here as an OPTION for this row's remainder, never adopted; it dies with the row.
- **CL-ATTR** — the attribute roster. Home: `proposals/2026-10-16-attribute-derivation*.md` and `proposals/2026-10-16-attributes-from-scratch*.md`. Two exercises recommending eleven and fourteen primaries (with eight and thirteen/twenty as alternatives) against the registry's nine plus an unnamed tenth. Evidence, not a design: reference under `CLAUDE.md` §0.05. **The carrier is absorbed by CR-20** (nine keys; the pending tenth slot refuses a value). **What remains:** the tenth attribute's name (J-T2, narrowed, `-05`; confirmed at the default, ED-IN-0301): TS (it has readers and conforms to ID-13, at the cost of a second scale) or Recall with its reader built first. HELD on J-T2 in B10-19; until then IN FLUX and the bar on binding Godot attribute fields stay. FOLD OF 2026-10-30 (amendment ratified by Jordan, ED-IN-0305): the content-architecture suite's P2 options (`proposals/2026-10-28-content-architecture-suite/03_P2_attributes_skills_histories.md`: the plan's nine plus TS as tenth; a ten-score variant; a demand-derived eight; six as floors and ceilings) are inputs to the design, not answers; the list is `-10` M23 (= J-T2, widened to the whole list) and the training rule (CR-20's `max` against a sum of attribute and capped training) is `-10` M24. Defaults in force: nine keys, the pending slot refusing a value; CR-20 as written (`-05` §1c). An answer that changes the list or the rule had to land before B10-10 opened (CR-20 built the carrier there, `c7764a5a`; B10-10 has closed, `0533c4da`), so now it is a schema re-pin after B10-10; B10-10's entry gate is not changed by this row. THE KNOWLEDGE-MODEL FOLD OF 2026-11-04 (the text above is history): **M23, J-T2 and `-10` E-1 are ANSWERED by Jordan's ten** (`ED-IN-0328`: Strength, Coordination, Endurance, Reason, Focus, Spirit, Attunement, Presence, Perception, Grace; Bonds dropped), which none of the three listed options matches (the nearest is the suite's split); CR-84 (B10-10, before CR-20) rewrites the roster, and CR-20 builds ten keys with no pending slot. **CL-ATTR narrows to M24 (the training composition, CR-20's `max` in force); it is NOT closed**: its row stays in B10-19, held on M24's design. The naming brief is void. IN FLUX and the bar on binding Godot attribute fields stay until Jordan confirms the ten (his ruling is hedged), CR-84's decision (5).
- **CL-EVENTS** — FORCE-WEATHER per territory, and the Tensions receiver as a world-generation draw (re-scoped from "the exogenous event channel and its deck"; the second clause added by the second decision round, item 2). Home: `-05` M16 and code report §14; `proposals/2026-10-04-forcing-churn-and-the-story-bar.md` (FORCE-WEATHER); the decks `proposals/2026-08-29-greenfield-systems-suite-v2/11_world_events.md` and `proposals/grounded_event_card_deck_v1.md` stay PROPOSED and held back. **Decided:** M16 NARROWED (`-05`), (b): the exogenous channel is two of AX-5's three motions (matter and bodies) plus persons' own acts; events only as kinds of matter or bodies change at kinds of place; the 58-card deck is not adopted as written (its gate requires retired Key types), and its climatic family is the candidate source for the per-territory values Jordan sets; a fourth motion is confirmed at the default, no (ED-IN-0301), and blocks nothing, and is not needed by CL-EVENTS (3) and (4). **Four commits:** (1) and (2) below; (3) and (4), the Tensions receiver and its six cards, are the second decision round's (sub-entries after this paragraph). (1) `queries/world_q.py::season_factor_of` keyed on (world_seed, tick, territory rung id), with `queries/inputs.py::ProduceInput.factor` per rung and MATTER's call in `loop/matter.py` changed: an interface change, hash EQUAL at `()`; the port reads the per-rung factor from the same owner. It LANDED early, in B10-05 directly after REM-52 (`df4ffc88`; a landing, not a member). (2) the live arm `((0.5, 1.0, 2.0),)*4` (H-26's declared sweep arm until Jordan names the values), in B10-18 directly after CP-T10-03's flip and before CR-08; it sets aside FORCE-WEATHER's own gate (`forcing-churn` `:109`) as a delegated choice `[ASSUMPTION; medium; Jordan to correct; revert: ()]`. **Batch:** the row leaves B10-19 for B10-18. NEEDS: REM-50 (B10-04), REM-52 (B10-05, LANDED `4edd1778`), CP-T10-03 (B10-18, earlier). FALSIFIER: at the live arm two territories at one tick draw different factors at some seed, and a territory at 0.5 holds stores below the control's after its yield step; planted failure: the territory dropped from the key gives equal factors. CONTROL: `()` reproduces the base hash. HASH: commit (1) EQUAL; commit (2) declared MOVER; commits (3) and (4) EQUAL (switch off). BUILDER: `CLAUDE.md` §10's second tier for (1) to (3); its third tier for (4). Revert for M16: the key back to (seed, tick); the draw back to `()`. SECOND DECISION ROUND, item 2 (something that happens without the player; `-05` §1b), taken: the refusals at step 3, the reception at step 4, the draw at step 5. The Tensions Deck is the first receiver, as a world-generation draw read once at build and shipped off `[ASSUMPTION; medium; Jordan to correct; revert: delete the registry, loader, roster, fixture member and switch (EQUAL)]`. Recorded: the Goldenfurt deck (28 cards) is not receivable as written (its engine, pressure Π, Directives and place-held ledger tags, is refused by T-a, T-h, T-i, AX-2 and the Rung NEVER line, and it rests on a document Jordan marked IDEAS, `rosters.yaml:79-80`); the 11 named cards are not receivable as written (each EFFECT is a change written into a stored aggregate, or a fiat outcome; nine of the eleven triggers read an aggregate; Olafsson Exposure's trigger, an Overwhelming act at a place, is a lawful T-b hook and its effect is not); either may later yield rows through commit (3)'s schema, card by card, by a position that names it. FOLD OF 2026-10-30 (amendment ratified by Jordan, ED-IN-0305): story openings drawn from pools at world build are CL-OPEN (B10-19, DESIGN-FIRST, ratified as a row; build HELD on `-10` M26); if its design widens commit (3)'s card schema (role-bound goal rows plus a lawful seed, a Record held from build or none), that widening is a later commit of this row, after (4), and commits (3) and (4) are built as written meanwhile. Jordan's figure 45 = 6 + 28 + 11 holds on his three sources; "19 distinct named cards across two documents" is [UNVERIFIED] (sampled, not counted). ARC-39 is the one NEVER-class arc marked forced (CL-THRUST's arc rule, below).
  - **CL-EVENTS commit (3) — the Tensions receiver: registry, loader, roster, yield-scale member, build switch (WR/IN)** · B10-18: … → CR-08 → CR-22 → CL-EVENTS (3) → CL-EVENTS (4) → CP-T10-08, both before the freeze · BUILD · R —. NEEDS: commit (1) (landed in B10-05: the per-rung factor); IN-66, IN-68 (landed: the goals loader and seeder). Not a dependency: CR-22 (the commits follow it for the reading only; CR-22 needs this row, so this is order, not an edge). CHANGES: `engine/season/tensions.yaml` (a header with the schema and the struck-key list; `tensions: []`); `engine/season/data/tensions.py`, the one loader (card keys checked; `goal` effects parsed together with `goals.yaml`'s rows through `data/goals.py::parse`, so ids, seats and `derives` resolve in one pass and there is one validator; `yield_scale` territory ids resolved by `data/geography.py`; effect kinds from the roster); `rosters.yaml: tension_effects: [goal, yield_scale]`, a closed two-member roster, with a note defining "tension" (`CLAUDE.md` §4); `data/files.py: TENSIONS_YAML`; `data/fixtures.py: territory_yield_scale = ()`; `queries/world_q.py::season_factor_of` multiplies by its rung's territory scale on every return path (an absent territory reads 1.0); `harness/populated.py::build_realm(tensions: bool = False)`: `tensions=True` draws one card, equally likely, with `ids.draw_factory(world_seed, lambda: 0)("world", "tension")`, and each `choose_one` list with the same factory keyed on the card id and the list's index; the goal rows go to the existing `seed_goals`, the scales into a new `Fixtures` value by `.sweep` (a new value, never a mutation of the shared default, `populated.py:1750-1757`). A card is a world-generation draw: read once at build, by no step of the season loop; no new World field (the drawn card is recoverable from its goal Propositions, ids prefixed `tension_<card>_`, and from the world's `Fixtures`). May not be data (M20's line applied to a card): a date, a deadline, a firing condition, an outcome, a write to standing, a seat, a tenure or a stance, and a `closing`, `successor` or `deal` key; the loader refuses every key outside the schema and names these. LADDER: step 4 for the reception (the precedent is `goals.yaml`, world-generation content read once at build by one loader); T-c (`01_AXIOMS.md:376`) is satisfied because nothing a card authors falls due after build; AX-5's world-generation sentence (`:191-192`) speaks of individuation and is cited by analogy only; step 3 for the refusals; step 5 for drawing one card from the seed. FALSIFIER: planted rows the loader must refuse, each by its own message: (i) a card with a `fires_at` key; (ii) an effect kind outside the roster; (iii) a `goal` row `data/goals.py::parse` rejects, refused with goals' own law string (one validator); (iv) a goal id colliding with `goals.yaml`. With a planted one-card test registry and the switch on, seeds 0-5: the same seed twice draws the same card and alternative; the card's Propositions are minted and at least one person commits to each (the count checked asserted ≥ 1 per goal row); a scaled territory's factor equals base × scale, an unscaled territory's equals base. CONTROL: switch off reproduces the base hash (`build_realm(0).content_hash()`; `aperture 1 s`, s = 0-2); switch on with a card whose lists are empty reproduces it (the draw writes nothing by itself). RUN: `python -m pytest engine/season/tests/test_tensions.py -q` (new) and `engine/season/tests/test_season_weather.py`. HASH: EQUAL (switch off, empty registry, empty scale). PORT: `engine/season/tensions.yaml` is named in `data/files.py`, so GO-09's registries export carries it with `--check`; the `build_realm(tensions=)` switch and its draw are part of the build signature the port reproduces, and GO-16's recorder logs the draw on the on-arm (the shipped arm draws nothing). [UNVERIFIED: `season_factor_of`'s per-rung signature after commit (1), and whether `seed_goals` accepts rows from a second source without a change to its `goals_complete` refusal; both read from docstrings only.] BUILDER: `CLAUDE.md` §10's second tier.
  - **CL-EVENTS commit (4) — the six Tensions cards as `[ASSUMPTION]` data, and the on-arm reading (WR)** · B10-18, directly after commit (3) · BUILD (data) · R —. NEEDS: commit (3). Reading only, not gates: CR-22 (the famine bites), IN-61 (card 1's succession). CHANGES: the six cards of the archived 6-card fuse deck (`conflict_architecture_proposal.md:127-146`, archived, headed "CANON — approved by Jordan", intent; draw one at game start, `:131`) as rows of `tensions.yaml`, each `source:` quoting the archived line and carrying `[ASSUMPTION; medium; Jordan to correct; revert: <row>]`; no code. Per card: (1) **Royal Crisis**: a goal row, object `seat_holders` of one royal seat by a keyed `choose_one` among `off_king`, `off_widow_regent`, `off_heir` (the card's sub-roll for target), stance −1, on a plotting organisation by a second `choose_one` among Varfell, Restoration Movement and Hafenmark; core intact; struck: the S8+ date (T-c) and "succeeds when it fires" (T-b); its −1 stance makes `fight` form on the King (`goals.yaml:161-162`), which the on-arm reading measures. (2) **Feldmark Famine**: `yield_scale` 0.75 on the Feldmark territory rung for the world's life `[revert: 1.0]`; core intact (matter; it bites once CR-22's hunger binds). (3) **Cardinal Independence**: a seat goal on one Cardinal seat with object `{kind: rung, rung: set_s_001}`; attention only: no Cardinal seat can `confer` or `establish` (only `off_confessor` holds `confer`, `offices.yaml:369`, `:382`, `:395`, `:408`, `:421`), so the archived "appoints" has no executor and is struck, and its "what executes it" cell names no verb `[revert: the row goes]`. (4) **Guild Fracture**: a goal row on the Guild seat (`off_guild_comptroller`) with object `rung` `set_s_018` (Gransol; the archived S017 is the pre-PP-726 id, and S-017 is Holzbruck, `valoria_geography_v30.yaml:376-383`, `:391`); no stance (a rung goal writes none, `goals.yaml:445-447`, `populated.py:665-669`, `:711`); attention and commitments only. (5) **Einhir Incident**: a seat goal on `off_restoration_leader` with object `rung` T4 and T13; no stance; T4 and T13 are territories, so no `march` forms on them; attention only. (6) **Ministry Crisis**: a goal row on a Church seat with object `seat_holders` of the `Ministries` seats (one: `off_parliamentary_clerk`), stance −1: a motive toward one clerk seat; the fiat "bureaucracy collapses" is cut. Two of the six (cards 1 and 2) keep their core; card 6 keeps a motive; cards 3, 4 and 5 are attention only. The receiver passes N on cards 1 and 2 (per-seed variety of the opening); its value is narrower than the decision's table claimed. FALSIFIER: switch on, seeds 0-5 × four seasons: every drawn card loads and seeds; for each seed at least one person committed to the drawn card's goal forms a candidate whose referent is that goal's object (the count checked asserted ≥ 1 per seed, so a vacuous loop fails). Planted failure: a card whose `seat_holders` object names a seat absent from `offices.yaml` is refused at seeding, naming the row; a built but vacant seat seeds a goal with no stance row (asserted: the stance-row count for that row is 0). READING, recorded in the commit and not a pass condition: STORY-BAR on against off, seeds 0-2 × four seasons (milestone M2's first world-generation content arm); TL B0.1's ARC rate for card-committed persons on against off, if B0.1 has landed; the on-arm's CI and Turmoil readings by CR-90's arc instrument (B10-17b) beside the off arm's (the arc fold of 2026-11-05: a reading of a card's effect names no target). CONTROL: switch off reproduces commit (3)'s hash. HASH: EQUAL (switch off). CONTENT THAT IS JORDAN'S (`-05` §1a's content list): the Royal Crisis plotters and targets; the Feldmark yield value (0.75 assumed); which Cardinal; whether to keep card 6; the pursuit weights (copied from each organisation's own `goals.yaml` weights); how many cards are drawn (one); the three Solmund cards (`solmund_master_document.md:511`, named only, not authored); and turning the switch on (it stays off in v10; the on-arm flip, `build_realm(tensions=)`'s default, is a declared post-freeze mover on GO-15's freeze list). REVERT: delete the rows (EQUAL). BUILDER: `CLAUDE.md` §10's third tier (archived prose mapped to registry ids, each mapping flagged).
- **CL-TROOP** — the troop stock. Home: `proposals/2026-10-16-troop-stock-design.md` (+ `_part2`). A recruit pool per settlement, a `levy` verb that raises troops, and a per-side order of battle; its build order TS-1 … TS-12 is in the home. **Built so far:** the rename `levy` → `requisition` (#482) and, contrary to the design, IN-52's levy-to-field feed (shipped OFF, `b7a1e1b`). **Waits on:** M3 (`-05`), confirmed at the default (ED-IN-0301): ratified `04_CODE_ARCHITECTURE.md:793` and `:802` are not amended to admit a counted troop stock in `Rung.stores` (option A); a yes re-opens on Jordan's word. J-C-2 is decided uncoupled (step 3, R-POOL: raising draws no cohort weight); M-1 is deferred until a yes. CP-T04-10, REM-32's value (JQ-4) and IN-52's retirement wait on the same answer; until it, the field stays persons at weight, sized by REM-32's fixture. FOLD OF 2026-10-30 (amendment ratified by Jordan, ED-IN-0305): `-10` M22 (troop counts by type under a named commander, the suite's ruling 1) is M3's yes arm, not a new question. The anchors above moved when the applied hunks landed; re-derived by quoted words, the Layer 1 text a yes would amend is `04_CODE_ARCHITECTURE.md:801` ("units = PersonId[] at weight -- one type. There is NO unit class, at any scale") and `:810` (the grid squad combat row, "every combatant a `Person`"); a troop row with a stored grade, discipline or morale would also break `holonic_ARCHITECTURE.md`'s Rung NEVER line and T-i, so the suite's own troop stock stores only commander, type, count, kit kind and home rung. Default in force: no (M3, ED-IN-0301).
- **CL-THRUST** — the thrust layer: an ambition plus an authored ladder of typed stages across ten thrust axes, made possible with no arc carrier. Home: `proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md` (TL; PROPOSED, held back in full) and its gap register `01_MISSING_IN_CODE.md` (both reference under `CLAUDE.md` §0.05: they bind no code and allocate no id). What folds in here is TL §1-§4, §6 and §8's B0.1 and B2 to B6, with the register's G-09, G-10, G-13, G-14, G-19, G-23, G-24, G-26 and G-28; the register's substrate and instrument rows fold in elsewhere (CR-14, CR-15, `-08` HR-8 and HR-9, `-06` part 4). **Built so far:** B0.1, the ARC instrument (`engine/season/harness/arc.py`, B10-02 lane 2, `c96b5290`); B2.1 and B2.2, the `thrust_axes` roster, the `axis:` key and `goal_stages` (B10-05, `edb1e9d2`; `engine/season/tests/test_cl_thrust_b2_schema.py`); B3.1, `current_stage` (B10-05, `a397fa16`; `engine/season/tests/test_cl_thrust_b31_current_stage.py`). B3.2, stage referents through the classed stamper (B10-09 close two, `67f5b086` and `cf943457`). Nothing of B4.x, B5.2 or B6.n. (This line said "nothing" until the fold of 2026-10-30, after the three pieces had landed.) **Decided:** M20 taken (`-05`), (b) "yes in part": a sequence is an ordered list of stage conditions read from the person's own ledger that only adds referents to his own `need` question; `closing`, `successor` and `deal` are an arc and are struck; TL's R3′ pulse and the stage `deadline` are excluded unless Jordan amends ratified T-c (`architecture/meta/01_AXIOMS.md:376-388`; his question, confirmed at the default, excluded, ED-IN-0301; it blocks nothing) `[ASSUMPTION; medium; Jordan to correct; revert: delete the `goal_stages` and `axis:` keys and the roster]`. M21 taken (a): `Felled` is death and there is no `Slain` band, so **B5.1 is cut** `[ASSUMPTION; medium; Jordan to correct; revert: a later position adds an overkill quantity and a band]`. **The row stays in B10-19 (one row); its released pieces land as commits in other batches, each hash EQUAL at empty data:** B0.1 in B10-02 lane 2, after CR-15 (B10-02's exit adds TL §8's falsifier and instrument for it); B2.1 and B2.2 LANDED in B10-05 (`edb1e9d2`; CR-07 did not land first and waits in B10-Z), once `layer-conformance` Lens B has answered TL :462-467's two Layer 1 questions (any Layer 1 hunk it yields lands in that batch's PR, listed under "Layer 0/1 hunks": M11 answered (a), ED-IN-0300); B3.1 LANDED in B10-05 (`a397fa16`) after B2.x; B3.2 (R2 only: stage referents through the classed stamper) LANDED in B10-09's close two (`67f5b086`, `cf943457`). **Still held:** B4.1 and B4.2 (their gates: `determine` and `covenant` executing; no owner), B5.2 (HELD on M1's residue through IN-36's `guards` flip; it rests on RS-26 and no longer cites M20), B6.n (Jordan's content: G-09, G-10, G-26). **Needs (the row):** CR-10 (landed `1ef8d273`), CR-14, CR-15, CR-28 (landed `1ef8d273`), CP-T02-01, IN-12, IN-61 (PC-10 is dropped: B5.1 was its only reason). Piece needs: B0.1 on CR-15; B3.2 landed; B4.x on `determine` and `covenant` executing; B5.2 on M1's residue; only B4.x and B5.2 fall after B10-17. **The pieces in TL §8's order, mapped to v10:** B0.1 the ARC instrument: `arc_effect_fields` moves from `rosters.yaml` to its module (TL :452 builds it in B2.1, but B0.1 reads it, so it lands here) and the driver-side ARC reader over it, with the register's refusal null and bookkeeping null (G-28; needs CR-15) → B2.1 and B2.2 the `thrust_axes` roster, the `axis:` key and the stage schema, keyed `goal_stages` and not `ladders:` (G-13: `ladders` already means `LarderInput.ladders` and the degree ladder in this package, `CLAUDE.md` §4), with the Layer 1 questions TL §8 lists routed to `layer-conformance` Lens B before building → B3.1 `current_stage`, read person-side → B3.2 stage referents through the classed stamper, R2 only (the R3′ pulse is excluded, above): LANDED in B10-09 close two (`67f5b086`, `cf943457`) after CR-10 and on CR-28's stamp of the Propositions a person's own ledger names (register G-13, addition 2; `7cae2fa1`, built and falsified in B10-05, re-taken in B10-09; the `-07` §2 LEAVE for G-04(a) is superseded) → B4.1 the threshold-raised docket crossing (needs `determine` executing: H-163, IN-12, the CP-T09 items; composed on `world_q.endings_reached`'s shape, G-14) and B4.2 the bound-peace reader: B4.2 needs `covenant` executing in computed play, which no v10 position delivers (CP-T09-03 is done on a hand-built chain; H-156's row leaves `covenant` at MEASURE), and B4.1 and B4.2 wait on that reading, taken by CR-14's pooled census, not on B10-17's close → B5.1 the `Slain` band: CUT (M21 (a), above; rarity of death comes from persons' choices: the closed `accept` route, `capture`, RS-26's access gate) → B5.2 the standing gate G1-G3 (it contravenes the `fight` cell note G4; needs CR-14's arms; rests on RS-26): B5.2 follows the `guards` default flip, which no batch performs: IN-36 is HELD on M1's residue (H-233 and the `foreign`/`guards` defaults, confirmed at the default, ED-IN-0301) and LEAVE (`-06` part 2:239), and B10-17 must not flip `guards` (`-09-build-B10-17`:236); the flip does not muster the guards before CP-T09-07 (b)'s union lands; B5.2 can be measured earlier on CR-14's `guards` arm, passed to `run_arm` from Python → B6.n the ladders per axis in TL §6's order, one axis per position (content: it needs the referent-bearing rows G-09, G-10 and G-26, which are Jordan's authored content; axis I takes G-23's caste reader, one `person_q` or `world_q` read over convictions, TL D3, which CR-31 (landed `f1319502`) upholds for the order and completes for the person as a regard term; axis H takes G-24, content plus a Record schema question; axis J stays out until H-236 has a source). **B6.n's arc rule** (SECOND DECISION ROUND, item 2, `-05` §1b) `[ASSUMPTION; medium; Jordan to correct; revert: drop the rule]`: a ladder position names its source arc and that arc's `engine/season/ENDINGS_CLASSIFIED.yaml` class, and draws only from the first two classes. Of the 48 classified arcs: DECIDER or ROLL with `forced_by_threshold: false` (18): a sequence of stage conditions beneath a protagonist's ambition, if the case's `who_acts` names one person whose ambition the stages serve; DECIDER or ROLL, forced (11): a sequence plus a T-b hook at the forcing crossing (it raises a question and writes nothing), only once B4.1 is built; THRESHOLD (8): not as written: its counter is first restated as a person's own estimate whose crossing raises a question; NEVER (9): not an arc but an open situation whose opening conditions are Tensions-shaped (one, ARC-39, is marked forced: its opening may use a T-b occasion, never an outcome); UNCLEAR (2: ARC-02, ARC-11): none until classified. ARC-46 to ARC-55 (10, unclassified) are classified by the file's own method by whichever B6.n position first draws on one; no position is created. The arcs are never runtime data (ED-IN-0225 stands). [UNVERIFIED: the per-arc `who_acts` protagonist test was not run over the 18.] **Builder:** `CLAUDE.md` §10's second tier (bounded reasoning) for B0.1, B2.x and B3.1; its third tier (judgment) for B3.2, B4.1 and B5.2 (each edits a shared primitive or contravenes a ruling); B6.n is Jordan's content and has no builder. Succession is IN-61's and CR-35's; the cluster adds none. Mapping of TL §8's other items: B0.2 is CR-14; B1.1 (candidate typing) is B10-05: M19 taken (a), decline at formation row by row with the per-row revert (`-05`); B1.2 is IN-12 step 5. TL's D2 and D3 are taken (canon; precedent) with a revert (`-06` part 4 §4).

````

### CR-73

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-73 | Natural shock (SH): a low draw that bites, a territory-season at the live arm's lowest member in which the larder pass logs a `shortfall` there; the past draw recomputed through a new optional `tick` on `season_factor_of`; no Event kind added (the strife fold, v11) | BUILD (harness) | E | CL-EVENTS; not a dependency: CP-T10-02 | — | written out in full: `-11` |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:21-37`):

````
### CR-73 — Natural shock (SH): a low draw that bites (IN/WR) · BATCH B10-18 (directly after CL-EVENTS commit (2)) · STATE BUILD (harness, one optional argument on a query; hash EQUAL) · R —
- WHAT: SH has no producer (`strife_moves.yaml` SH `gap:`). The study's SH is an exogenous shock to matter or bodies (plague, eruption, flood, drought) that opens a subsistence strand; in the loop the only exogenous draw is CL-EVENTS commit (2)'s weather factor per territory, `((0.5, 1.0, 2.0),)*4`, and its lowest member comes up about a third of the time, so a low draw alone is a bad season, not a shock. **SH here is a low draw that bites:** a territory and season whose drawn factor is the arm's lowest member AND in which the larder pass (`loop/matter.py`) logs a `shortfall:<kind>` at a settlement of that territory (the reading CR-22's exit already names) `[ASSUMPTION; medium; Jordan to correct; revert: SH stays GAP]`. Read after the run from the log and the draw: `queries/world_q.py::season_factor_of` reads only `w.tick`, so it gains an optional `tick` argument defaulting to `w.tick` (the draw's key is already (world seed, tick, territory), CL-EVENTS (1)), and the harness recomputes the past draw with it; nothing is recorded during the run and no Event kind is added. Whether a low draw binds hunger at all is CR-22's reading, not this one's.
- LANDED ALREADY: CL-EVENTS commit (1) (`df4ffc88`, the key); S1's instrument.
- REMAINING UNBUILT: the `tick` argument; the SH reading in `strife.py`; the SH row's `gap:` replaced by the reading's description; its test.
- GATE: CL-EVENTS commit (2) landed (this batch). NEEDS: CL-EVENTS. Not a dependency: CP-T10-02 (a calamity band is a second producer only if it lands as an Event; read at the close if it does).
- EXIT and FALSIFIER: three hand-built one-territory worlds: a lowest-member draw with a settlement's larder at its floor logs a shortfall and reads one SH; the same draw with a full larder reads none; a shortfall caused at a 1.0 or 2.0 draw reads none (a shortfall without a shock is not SH). MUTATION: drop the draw condition and the third world reads SH (red). The live-arm count at the batch close is a reading, not a pass condition (it would be above 0 by construction). CONTROL: `season_factor_of(w)` with no `tick` returns today's value (hash EQUAL); `content_hash` and log length unchanged by the reading.
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: none.
- RE-BASE: `season_factor_of`'s signature and key as commit (2) leaves them; where the larder pass logs `shortfall:<kind>`; the SH row.
- FILES: `engine/season/queries/world_q.py` (`season_factor_of`'s optional `tick`), `engine/season/harness/strife.py`, `strife_moves.yaml` (the SH row), `strife_data.py` (only if the row needs a new key), `engine/season/tests/test_strife_instrument.py`.
- VERB CLUSTER: no.
- LAYER 1: none (an argument on an ownerless `world_q` function; a harness reader).
- N-LINE: the SH reading — cut it and the gameplay experience is worse, because the subsistence category (the study's A: drought, flood, plague) cannot be seen to open in play, so the reachability report cannot say whether a famine strand can begin even once the weather is live.
- BUILDER: second tier.
- SOURCE: `strife-00` §7 (natural shock row), §8 S2.

````

### CR-22

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-22 | Hunger binds: the per-head need chosen by a reading rule (M6 taken (a)): M-H2's per-head arms (×1, ×5, ×20) on `build_realm` seeds 0-2 for eight seasons, the gentlest arm at which REM-50 reads a settlement below `fed` after season 1 at every seed ships in `rosters.yaml: subsistence_weight.weights`; the season-0 floor rule; `body_step` re-derived by H-125's own test | MEASURE then BUILD (exit also reads the `shortfall:<kind>` observations and the executed `transfer` / `requisition` / `petition` / `migrate` counts at the shortfall rung, a reading not a pass condition; a `shortfall` claim already reaches every seat whose purview contains the rung and `_from_shortfall_claim` forms a `transfer`, so an "unrest becomes a Question" position was CUT: the story-telling fold of 2026-11-02) | M | REM-50, REM-52, CP-T10-03, CR-08, CL-EVENTS | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:88-100`):

````
### CR-22 — Hunger binds: the per-head need chosen by a reading rule (SE/IN) · BATCH B10-18 (… → CP-T10-03 → CP-T10-03's flip → CL-EVENTS (2) → CR-08 → CR-22 → CL-EVENTS (3) → CL-EVENTS (4) → CP-T10-08) · STATE MEASURE then BUILD · R R-04 (the settlement row)
- WHAT: M6, taken (a): a person's food need scales per head, and the magnitude is chosen at this position by a stated reading rule, not asserted. The owner is `engine/season/rosters.yaml: subsistence_weight.weights`; H-11's row gains the chosen arm and the rule.
- LANDED ALREADY: REM-50's census line `hunger_by_settlement` (B10-04, closing commit `566de4d7`). Before it lands: REM-52's `body_step` 10 (B10-05, LANDED `4edd1778`); CP-T10-03's calendar flip, CL-EVENTS (2)'s live weather draw and CR-08 (earlier in B10-18).
- REMAINING UNBUILT: THE RULE: run the per-head arms (×1, ×5, ×20 on both eaten kinds) on `build_realm` seeds 0-2 for eight seasons, calendar on, the live weather draw on, `body_step` 10; ship the gentlest arm at which REM-50 reads at least one settlement below `fed` in a season after season 1, at every seed; if ×5 does not bind and ×20 drains every settlement, bisect once (×10). SEASON-0 FLOOR RULE: no cohort's body crosses a floor at season 0 under any arm; an arm that does is refused, or a prior position stocks the larders as world-gen content. `body_step` is re-derived here by H-125's own "season or campaign" test (10 is a delegated pick). The exit records the arms read, the count of eaters fed from a larder above their own settlement (A2-26's exposure, a reading), and the strict-top share at CR-17's τ (a reading only).
- GATE: B10-18, after CR-08. NEEDS: REM-50, REM-52, CP-T10-03, CR-08, CL-EVENTS.
- EXIT and FALSIFIER: at the shipped arm `hunger_by_settlement` reads a band below `fed` after season 1; planted failure: `want = Person.weight` (per-head term dropped) and every band reads `fed`. Season-0 check: at `body_step` 10 the ×20 arm costs every cohort 1,200 body at season 0 (`data/fixtures.py:571-576`), so the floor check must refuse ×20 (the check reds if it admits it). CONTROL: ×1 reproduces the base hash. R-04's settlement-row `measure:` gains REM-50's census line (eight seasons, seeds 0-2, at least one band below `fed` after season 1; `-02`). REM-51's reopen trigger is read here: a settlement under two seasons of cover in this exit's census (REM-51 stays CUT, `-07` §2). **(The story-telling fold of 2026-11-02, ED-IN-0311.)** The exit gains one READING at the same seeds as its per-head arms and at the batch-close horizon (head P10: no further than `aperture 3 0`; a longer horizon runs on Jordan's call): per season, the `shortfall:<kind>` observations at settlement rungs (the larder pass, `loop/matter.py`) and the executed counts of `transfer`, `requisition`, `petition` and `migrate` by persons at or governing the shortfall rung; a reading, not a pass condition (V2). If shortfall occurs and none of the four executes, THAT, and only that, opens a position (S-UP: a demand no named person carries). Reason recorded: a `shortfall` claim already reaches every seat whose purview contains the rung (`witness.py` SEAT_CHANNEL, `world_q.governors_of`) and `decision/options.py::_from_shortfall_claim` forms a `transfer`, so a new "unrest becomes a Question" position was CUT (the paragraph "After the story-telling fold", §1).
- HASH MOVERS: declared MOVER (every realm-seeded pin, the `BASE_EVENTS` files, `results.json`).
- HOLES AND LEDGER IDS: H-11, H-125 (`hole_register.yaml:911-921`); ED-IN-0255 (`registers/editorial_ledger_in_archive.jsonl:171`); A2-26.
- ASKS ATTACHED: M6 TAKEN (`-05`), step 5 `[ASSUMPTION; medium; Jordan to correct; revert: another arm is one value; (b) edits `site_yield`'s food cells; (d) is `body_step` 0 and `year_length` 0 with CR-08 deleted]`. Option (a) rests mainly on one coefficient for towns and fields; truncation bites hard only at the deepest cut (a cell of 2; at a one-fifth cut the cells are 8 and 6); the ~20× surplus is inferred, not measured; the shock branch is filled by CL-EVENTS (2), and (d)'s removal stands on the draw's magnitude.
- RE-BASE: none of the arms was run when the decision was taken; whether ×5 or ×20 binds is open until this exit.
- BUILDER: second tier; an independent third-tier (judgment) critic judges the selected arm.
- SOURCE: `-05` M6; `proposals/2026-10-21-v9-remediation/2026-10-21-v9-remediation-01-verdict-and-coverage.md:18-19`; `…-remediation-04-asks-edits-measurement-and-risks.md:272`.

````

### CP-T10-04

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T10-04 | Recovery costs time and care | BUILD (released from M11, ED-IN-0300; its M6 hold lifted, CP-T03-07 builds in B10-11, REM-44 landed in B10-07, `4ffddcdeb`) | M | CP-T03-07, CP-T10-03, REM-29, REM-44 (landed `4ffddcdeb`); H-211 | — | `cp-world-travel-survival-npc-life`:200-232 |
```

entry (`2026-10-23-subsystem-completion-10-world-travel-survival-npc-life.md:200-233`):

````
### CP-T10-04 · Recovery costs time and care

- **Adds.**
  0. **The cap is one quantity, owned by PC.** Every rise here — this arm and `tend` — heals toward the person's `body_ceiling`
     (T03 CP-T03-07: a per-person `Person.body_ceiling`, built at `condition_scale`, lowered by T03's permanent marks), or toward
     `condition_scale` where no ceiling is set. T10 owns the time-driven rising arm; T03 owns the ceiling and the marks. So this arm never
     heals a mark away.
  1. **A rising arm** in MATTER's body pass (H-211 cause 1; r2 §A.4's signed step): a living person below his `body_ceiling` who is not
     short this season gains `recovery_step` **[ASSUMPTION: 50 a season]**, capped at the ceiling. A cohort rises only when fed (no entry
     in the draw's shortfall record); a named person always (he does not eat). Hunger therefore blocks healing.
  2. **Upward crossings** (H-211 cause 2): `_crossings` (`matter.py:39-86`) gains `before < floor <= after`, same kind
     `condition.band_crossed`, its antecedent the rising write. H-211's own control: the per-season count of downward site crossings is
     unchanged.
  3. **`tend` heals a share of the headroom**, the revert the code names (`effects_combat.py:378-379`: "a swept fixture fraction of the
     headroom — #453's 'fast partial and slow full form', C-48"): fixture `tend_share` **[ASSUMPTION: 0.5]** of the headroom to
     `body_ceiling`.
  4. **`tend.refused` keyed by clause** (dead or absent / not with / whole), on `migrate`'s keyed-refusal precedent (DA:#55).
- **Owner.** `loop/matter.py` (body pass, `_crossings`); `loop/effects_combat.py::_eff_tend`; fixtures. Reads T03's
  `Person.body_ceiling` (`state/carriers.py`, T03's field). **Primitives.** P40 (recovery priced in acts and presence), P01, P02.
- **Asymmetry.** Assignments of `Person.body`: `matter.py:525` (hunger), `effects_combat.py:389-392` (`tend`), the combat writes in
  `_eff_kill` and `_eff_march` (T10 §2.6), and this arm. Readers: `budget.py:59` (bands), `deliberate.py`'s fingerprint, the PC seam's
  wound state (T10 §0a: wound → body → `end` → next fight), so a recovering fighter's `end` rises over seasons (PC join).
- **Decision.** Tend now (one act, and you must be "with" the patient) or let time do it; whom to tend first once CP-T10-05 makes the
  sick. **Unwatched:** the wounded mend over seasons, and the mend is news (a crossing witnesses can hold).
- **Falsifier** (`test_recovery.py`): a fed cohort at 450 rises 50 a season and crosses `limited` (500) upward once, emitting one
  `condition.band_crossed` (MW-11 green); a short cohort does not rise; `tend` at 250 with `body_ceiling` 1000 gives 625, and at
  250 with `body_ceiling` 799 (a T03 mark) gives `250 + 0.5 × 549 = 524`, never 1000; a marked person at 799 gains nothing from the
  rising arm. Mutations: the rising write lands on a copy → `budget()` unchanged → red (LB-3b's pairing of crossing and budget); the
  arm or `tend` reads `condition_scale` instead of `body_ceiling` → the marked person rises past 799 → red.
- **Control.** `recovery_step` 0 and `tend_share` 1.0 → the behaviour of today (the upward predicate fires on nothing at control, since no
  MATTER write rises). **Hash:** not hash-equal off: `body_ceiling` is a new `Person` field, so the hash moves by **schema** alone (H-208's
  precedent: a new `Person` field changes its repr) — declared a SCHEMA mover, landed with T03's CP-T03-07, which owns it; the on arm is
  also an outcome mover. **Revert:** the two fixtures. **Size:** M.

````

### CR-46

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-46 | The R-05 reading (`ex - both`, pooled, per seed) and its definition: the denominator counts the six army rows, and the menu-door clause | BUILD (harness and text) | E | — | the menu-door clause: ratified by Jordan 2026-10-31 (ED-IN-0307), revert alone | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:378-390`):

````
### CR-46 — The R-05 reading and its definition (IN) · BATCH B10-18b (first) · STATE BUILD (harness and text; hash EQUAL) · R R-05
- WHAT: the batch's base reading and the three definition clauses its other positions need. (1) The base reading, quoted in the commit body: `python -m engine.season.harness.aperture 3 s`, s = 0-2, per verb, with the `ex - both` column (`ex` counts an act that emitted a declared kind, and an admission refusal whose kind is also an emitted kind, `finding.none` on `examine` and `research`, reads executed and `both`), pooled and per seed, over `len(VERB_TABLE)` rows. (2) R-05's `measure:` text in `engine/season/requirements.yaml` and `-02` §6 gain: "executed" is `ex - both`; the denominator is `len(VERB_TABLE)` at measurement time and counts the six rows ED-IN-0306 added (REM-02's rule, unchanged); and the **menu-door clause** `[ASSUMPTION; medium; Jordan to correct; revert: delete the clause, and the six army verbs are named residue]`: a verb held out of formation by `Fixtures withheld_verbs` because its command is the act's payload (`rosters.yaml: army_verbs`) is built out when CR-52's shipped scripted policy drives it through `dispatching_chooser` in a seeded run and each declared kind is emitted with a minted receipt whose before differs from after. This amends REM-02's "a hand-built execution never counts" for `rosters.yaml: army_verbs` only: an act built by `military_menu.act_for` counts when a shipped policy returns it through `dispatching_chooser`; a direct fold (`army_presets.install`) never does. (3) The `len(VERB_TABLE)` asserts and the never-attempted set at `test_season_shape.py` (`:9366-9369` at `eda39a6`) re-recorded by symbol, with `-02` §6's "56" and "unchanged" read as superseded.
- LANDED ALREADY: `aperture`'s per-verb funnel, `both` and `graded` columns (REM-10, REM-11); REM-02's denominator rule.
- REMAINING UNBUILT: an `ex - both` column in `aperture.py`'s `VERB_COLUMNS`, if the printed `ex` and `both` do not suffice (the pooled block exists: `aperture 3 --seeds 0 1 2`); the three text clauses.
- GATE: B10-18 merged. NEEDS: none inside the batch.
- EXIT and FALSIFIER: the reading prints the 62 rows (or `len(VERB_TABLE)` at the base commit) per seed with `ex - both`; a planted row whose only emission is its refusal kind reads not executed. CONTROL: `content_hash` EQUAL before and after (text and harness only).
- HASH MOVERS: none (E).
- HOLES AND LEDGER IDS: `engine/season/requirements.yaml` R-05 `measure:`; H-156.
- ASKS ATTACHED: the menu-door clause, above: it narrows what "built out" asks of the army verbs, which is a change to a requirement Jordan wrote; he ratified it with the fold on 2026-10-31 (ED-IN-0307), and it reverts alone.
- RE-BASE: re-take the reading on the batch's base commit; the figures in this file (36 of 60 resolvable rows executed, pooled over seeds 0-2; 27 of 60 not executed at seed 0; `succeed` and `tie / knot` outside `resolvable_verbs()`; HEAD `eda39a6`) come from probe runs whose output is not in the repository.
- BUILDER: second tier.
- SOURCE: the R-05 re-take of 2026-10-31 (this fold); `-02` §6; `engine/season/harness/aperture.py` header.

````

### CR-52

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-52 | The menu door: the preset order of battle (`recruit`, `form_unit`, `assign_troops`) through `dispatching_chooser`, with a test and an off control | BUILD (harness and test) | E | CR-46 | reconciliations (i) to (iii) in `-04` | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:456-468`):

````
### CR-52 — The menu door: the preset order of battle through `dispatching_chooser` (IN/MB) · BATCH B10-18b (second, after CR-46) · STATE BUILD (harness and test; hash EQUAL) · R R-05 (`recruit`, `form_unit`, `assign_troops`)
- WHAT: ED-IN-0306 (RULED, 2026-10-28) landed six verbs that a person cannot form for themselves: the command (cohort, troop type, count, subformation, tactics) is the act's payload, the operand vocabulary is closed at eight, and `Fixtures withheld_verbs` (`data/fixtures.py`, `("destroy_record", *ARMY_VERBS)`) keeps `opening_set` from forming them. The ruling's doors are a menu API (`harness/military_menu.py`: `menu`, `act_for`, `callback` for `dispatching_chooser`) and, for non-player factions, a deterministic preset order of battle (`harness/army_presets.py::install`, off by construction: nothing in the loop calls it, `test_army_menu_presets.py::test_the_presets_are_off_by_construction`; it folds directly, and `modules/mass_battle/troop_types/presets.py` plans only `recruit`, `form_unit` and `assign_troops`; "who marches where is MB-08's"). Build the one missing piece: a harness run that issues `army_presets.plan_for`'s commands through `military_menu.callback` and `dispatching_chooser` and `SeasonDriver.season` instead of `install`'s direct fold, with a test and an off control. It authors no command the ruling does not give: `order_unit`, `disband_unit` and `discharge_troops` are named R-05 residue owned by MB-08 (B10-Z, HELD; ED-IN-0306: "the AI general planner staying MB-08's"). Enlarging the closed operand roster (H-94) and flipping the presets on both move the hash and reopen MB-08, so neither is taken.
- LANDED ALREADY: ED-IN-0306 phases 1 to 5c (`HANDOFF_MB.md`'s army entry); the menu; the presets; `tests/valoria/test_army_verbs.py`. A probe at `eda39a6` drove a realm commander through all six verbs by the menu with no engine change.
- REMAINING UNBUILT: the harness run (a new harness file) and its test, beside `test_army_menu_presets.py`. A season-level run of these verbs is in no test at `eda39a6`.
- GATE: B10-18 merged. NEEDS: CR-46; its menu-door clause is ruled (Jordan, 2026-10-31, ED-IN-0307), so CR-52 does not wait on a ruling.
- EXIT and FALSIFIER: the test runs the harness through `SeasonDriver.season` on a hand-built world (`P.tiny_world` with one minted `army` Record; P9) and asserts `army.recruited`, `army.formed` and `army.assigned` with a receipt before ≠ after each; harness off, none. The realm run is a reading quoted in the commit, not a test (V2). CONTROL: `build_realm(s)` content hash EQUAL at seeds 0-2; the go07 digest and the season-weather pins do not move.
- HASH MOVERS: none (E).
- HOLES AND LEDGER IDS: H-94, H-166 (unheld land: unruled, untouched), MB-08 (HELD, B10-Z).
- ASKS ATTACHED: CR-46's menu-door clause. **Reconciliations this position owes and does not build:** (i) CP-T09-07 (a)'s planned `recruit` row (a contested offer of service writing a duty edge) collides with the landed army `recruit` row; `VERB_TABLE` is keyed by verb, so the planned row is `retain` (named now, not at B10-17's re-base, so no builder adds a second `recruit` key), `[ASSUMPTION; medium; Jordan to correct; revert: rename the army row and give CP-T09-07 (a) `recruit`]` (`-08` part 2's CP-T09-07 entry carries the reasoning); this position's `recruit` is the army row throughout; (ii) M22, CP-T04-10 and CL-TROOP are read against ED-IN-0306 at their own entries (its ruling amends `04` §C.5.1 for armies and neither the plan nor `-10` cites it); (iii) CP-T04-10's `levy` and `disband` rows are different verbs from `recruit` and `disband_unit` and stay held on M3.
- RE-BASE: re-run the season probe. The figures in this entry come from probe runs whose output is not in the repository (the R-05 re-take of 2026-10-31); none is quoted until re-taken at the re-base.
- BUILDER: second tier.
- SOURCE: ED-IN-0306 (`registers/editorial_ledger_in.jsonl`); `proposals/2026-10-29-army-phase5-design.md`.

````

### CR-47

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-47 | Works and Sites reach the chooser's ranking (`build`, `found`, `work`, `restore`, `examine`; `sabotage`'s rank link) | BUILD | M | CR-50, IN-45, REM-22, CP-T06-01, CR-21 | route (a) over (b) taken | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:391-403`):

````
### CR-47 — Works and Sites reach the chooser's ranking (IN) · BATCH B10-18b (after CR-50) · STATE BUILD (hash MOVER) · R R-05 (`build`, `found`, `work`, `restore`, `examine`; `sabotage`'s rank link)
- WHAT: the two planned works (`venues.yaml: planned_works`, minted by `harness/populated.py::mint_planned_works`) and the realm's Sites exist, and their masters FORM `build`, `found`, `work`, `restore` and `examine` on them, yet no act is ever attempted: a candidate whose subject is a works or a Site scores near zero (`research` .17, `work` .06, `restore` 0, `examine` 0, `build` -.03, `found` -.02) against about 8 for a candidate on a Person subject, because `decision/choose.py::score_terms` is the pursuit term plus the stance term and a Record or Site carries no stance. Measured pooled over seeds 0-2, four seasons: `build` 55 attempts and 0 executed (non-masters, on a non-works Record: `exists:works=0`), `found` 0, `work`, `restore` and `examine` 0 attempted. Two routes; the builder takes the first unless the re-base shows it does not move the ranking: (a) the works or Site occasion takes the head question (`qs[0]`) only where the person's question carries no Person referent, and changes no term of `score_terms` (`questions_for` appends `works_sites` to the head question's referents; a separate question would change the ranking only by becoming `qs[0]`, which is H-207's measured IN-53 failure, so the stop rule is that `issue`, `levy` and `transfer` formations at the realm line read against their pre-item counts and a fall reverts route (a) for (b)); `question_aggregation_rule: first` stays (H-54, ruled); (b) alignment cells for `restore`, `examine`, `sabotage` and the works verbs (`data/verbs.py` `ALIGNMENT`), which is authored content and is taken only by CR-21's stated rule (P11). `sabotage` takes `referent_class: Site` from CP-T06-01 (B10-14) and its Site occasion from this position.
- LANDED ALREADY: IN-45 (works as world data, B10-06, CLOSED), REM-22 (`Site` class, B10-05, CLOSED), `works_sites` (`world_q.py`), 322 Sites at `build_realm(0)` wearing each season (`loop/matter.py`).
- REMAINING UNBUILT: the chooser's route to a works or Site act (a or b above); for `work`, a plan with band floors (the court dwelling's `floor` reads UNKNOWN, so `work.unavailable` refuses it even if chosen: a `venues.yaml` `planned_works` row for a harbour or seam plus its `rosters.yaml: works_cost` row, which is content and so held to P11's rule).
- GATE: after CR-50 in B10-18b. NEEDS: IN-45, REM-22, CP-T06-01, CR-21.
- EXIT and FALSIFIER: `aperture 3 s`, s = 0-2: `build`, `found`, `restore`, `examine` each attempted by a works master or a person at a Site, and `site.built` or `rung.founded` caused by a computed act (IN-45's own G-05 exit, met on one of its two halves at `eda39a6`: `found` executed 0, 0 and 1 across the seeds, `build` 0). `work` and `sabotage` read executed, or are recorded 0 and left named residue with the refusal that decided (the `floor` reading; `site.damaged`'s producer). CONTROL: the route switched off reproduces the pre-item hash; the stance-term share of the top candidate is printed beside the pre-item figure.
- HASH MOVERS: declared MOVER (it changes which candidate every deliberating person ranks first); one golden re-record, stated plainly, old to new in the commit body.
- HOLES AND LEDGER IDS: H-54, H-165, H-166 (limit 4); `-08` G-05, G-09, G-10 (authored rows are Jordan's).
- ASKS ATTACHED: route (a) over (b) `[ASSUMPTION; medium; Jordan to correct; revert: route (b), through CR-21's cells]`.
- RE-BASE: the scores above were taken before B10-07b closed (CR-16's `stance_polarity: declared` is now shipped and CR-21's cells landed, both of which change the stance term), so re-run probes that print each master's candidates and scores at tick 0 first: the cause may have moved or narrowed, and `align` for `examine` and `sabotage` reads 0 at the post-B10-07b tree (`restore` -0.2 on one axis); the exact slice boundary of `scene_budget` 5 by `interactions_per_scene` 3 (`data/fixtures.py`, `decision/choose.py::pack_scenes`) is not verified here. The figures in this entry come from probe runs whose output is not in the repository (the R-05 re-take of 2026-10-31); none is quoted until re-taken at the re-base. CR-71 (reading @5d6aac5, `aperture 2 0` and `strife 2 0`, seed 0, `PYTHONHASHSEED=0`, REALM): RG stays at 0 on the read this entry reaches: `found` attempted 4, all refused on `exists:works=0` (a wrong Record sub-kind).
- BUILDER: third tier (judgment).
- SOURCE: the R-05 re-take of 2026-10-31; `-02` §6.

````

### CR-49

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-49 | `exchange` names another rung (`referent_class: Rung`; a self-trade declines) | BUILD | M | CR-48, REM-2B, REM-21 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:417-429`):

````
### CR-49 — `exchange` names another rung (IN/SE) · BATCH B10-18b (after CR-48) · STATE BUILD (hash MOVER) · R R-05 (`exchange`), R-04 (conjunct (1) re-read)
- WHAT: `exchange` is attempted 424 times over seeds 0-2 and never executes. `_eff_exchange` (`loop/effects_economy.py`) declines a side that is no rung or a kind traded for itself (a rung trading with itself is refused by the gate's no-op receipt); at seed 0, 82 of 133 acts have `from == to` on one rung, 25 have a Person as `to`, 16 a Record, 3 a Proposition, 1 a distinct rung, and the aperture reads `stores:salt=>0` for 78 post-admission refusals. Stores are not the limit (S-001's grain 40 to 144 over four seasons). The row has no `referent_class`, so `to` is whatever the question's referent is. Give it `referent_class: Rung` (the `places_named` and `larders_in_purview` precedent) and a decline in `opening_set` of `to == from`, read from a row column as `counterparty:` is, never from the verb's name.
- LANDED ALREADY: REM-2B's typed cell (B10-06, CLOSED); `_eff_exchange` (both sides' stores move, matter conserved).
- REMAINING UNBUILT: the class and the self-trade decline.
- GATE: after CR-48 (P13). NEEDS: REM-2B, REM-21.
- EXIT and FALSIFIER: `aperture 3 s`: `exchange.made` at least once from a computed act; `confer` and `oblige` re-read at the realm line against their pre-item counts, because the reverted build of the earlier `exchange` crowded them out (REM-2B's override in `-08`: `confer` 3/3/5/1 to 3/3/0/0, `oblige` 60/60/17/17 to 0); a fall to 0 reverts this position alone.
- HASH MOVERS: declared MOVER.
- HOLES AND LEDGER IDS: H-58, H-229 (a different row).
- ASKS ATTACHED: none.
- RE-BASE: re-run the operand census for `exchange` (`from`, `to` kinds) at the base commit. The figures in this entry come from probe runs whose output is not in the repository (the R-05 re-take of 2026-10-31); none is quoted until re-taken at the re-base.
- BUILDER: second tier.
- SOURCE: the R-05 re-take of 2026-10-31; `loop/effects_economy.py`; `data/fixtures.py` (`exchange` kind and return kind).

````

### CR-51

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-51 | A restraint exists: `arrest` on a held warrant, `pardon` closing it | MEASURE then BUILD only the gap | M if built | CR-49, CR-47, IN-12 (landed `f9e4cef`), CR-50 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:443-455`):

````
### CR-51 — A restraint exists: `arrest` on a held warrant, `pardon` closing it (IN/FA) · BATCH B10-18b (after CR-49) · STATE MEASURE then BUILD only the gap · R R-05 (`arrest`, `pardon`)
- WHAT: `pardon` refuses after admission: `_eff_pardon` (`loop/effects_governance.py`) returns an empty Change unless the subject holds a live `detain` or `ban` whose object is `Act.via`; at the end of four seasons at seed 0 the realm holds none. The three producers are `arrest` (formed 5, attempted 0), `determine`'s disposal (13 refused) and `revoke`'s ban (CR-54). `arrest` forms only where a held warrant names a Person (`decision/options.py`, the `WARRANT_SOURCED` block), and whether a computed `issue` ever mints a warrant whose terms name a Person is not verified here. MEASURE first: print, at the base commit, `issue`'s minted terms by kind, the warrants held, the formed-and-attempted line of `arrest`, and `determine`'s refusals by read; BUILD only the link the reading names missing (a warrant naming a Person, or the `arrest` rank). No new motive and no special case for either verb (§0). `pardon` follows with no change of its own once an edge exists.
- LANDED ALREADY: `_eff_arrest`, `_eff_pardon`, `_RESTRAINT_ENDED`; IN-12's warrant channel (B10-09 carries IN-12).
- REMAINING UNBUILT: the measured gap, if any. The church-custody warrant branch (a custody disposal becomes a warrant to a `dispatch` holder, who serves or declines, and a warrant that matures unserved is a witnessed decline) is this position's gap if the measure shows it, and is then built with CR-63's warrant duty (the build-all fold of 2026-11-02).
- GATE: after CR-49 and CR-47. NEEDS: IN-12, CR-50.
- EXIT and FALSIFIER: `aperture 3 s`: `arrest.made` and `detention.ended` or `ban.ended` caused by computed acts; or the exit records the missing link by name and both verbs stay named residue (no position is invented to fix it). A planted `detain` on the seat: `pardon` closes it and emits (the check the effect already passes by hand).
- HASH MOVERS: MOVER if built; EQUAL for the reading.
- HOLES AND LEDGER IDS: H-232, H-207 (the `revoke` ban producer, CR-54); `-06` part 4 G-07 (IN-12 step 5 owns `arrest`'s warrant, with CR-16's `subject_is_opponent` repair covering it, B10-07b): re-read after both.
- ASKS ATTACHED: none.
- RE-BASE: re-run the warrant census; CP-T05-05 (cut by the NERS fold) is not re-opened by this position. The figures in this entry come from probe runs whose output is not in the repository (the R-05 re-take of 2026-10-31); none is quoted until re-taken at the re-base. CR-71 (reading @5d6aac5, `aperture 2 0` and `strife 2 0`, seed 0, `PYTHONHASHSEED=0`, REALM): CA, AM and PU's `arrest` leg stay at 0 upstream of any refusal: `arrest` formed 1, offered 1, attempted 0, `pardon` formed 8, offered 8, attempted 0 and `interrogate` formed 0. The SPINE refuses `pardon` AT admission on `exists:Person=0` (4 of 4), which this entry's "refuses after admission" does not cover.
- BUILDER: third tier.
- SOURCE: the R-05 re-take of 2026-10-31; `-08` CP-T05-05's cut.

````

### CR-57

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-57 | A petition is addressable and deliverable (`to` fans over the known; a held petition has CR-48's `give` occasion) | BUILD | M | CR-48, IN-10, REM-25 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:504-516`):

````
### CR-57 — A petition is addressable and deliverable (SC/IN) · BATCH B10-18c (first) · STATE BUILD (hash MOVER) · R R-04 (contributor), R-05
- WHAT: a computed `petition` has `terms` and `to` bound to the same person (H-94: the row keeps the single-referent limit that `issue` left at IN-10), so no non-player petitions someone about another; and a petition is minted into the petitioner's hold (`_eff_petition`) and reaches its addressee only by `give`, which was refused 7 of 7 at seed 0 (`record.given` 0). Make `to` fan over the persons the petitioner knows, as `issue`'s does, with `terms` the referent; and give a held petition the same `give` occasion CR-48 gives a held writ. No mint into the addressee's hand (ED-IN-0292 (1), RULED NO, is untouched).
- LANDED ALREADY: IN-10 (`issue`'s fan), IN-45 (`carry`), REM-25 (the `Record` class widened), CR-48 (planned, the writ's `give` occasion).
- REMAINING UNBUILT: the `petition` row's addressee fan; the `give` occasion for a held petition; the co-location read.
- GATE: after CR-48 (the same row and the same occasion; serialise on `verb_table.yaml`'s `give` row). NEEDS: IN-10, REM-25, CR-48.
- EXIT and FALSIFIER: seeds 0-2: a petition whose `to` differs from its `terms` is filed; a `give` of a held petition executes (`record.given` above 0 for a petition); a petition reaches a seat that can `carry` it. CONTROL: the fan switched off reproduces the pre-item hash.
- HASH MOVERS: declared MOVER; one re-record.
- HOLES AND LEDGER IDS: H-94, H-229 (the Record half), ED-IN-0292 (1) (RULED NO).
- ASKS ATTACHED: none. Stop if the route needs an eleventh operand name (the operand vocabulary is closed, H-94).
- RE-BASE: re-run the petition census (`petition.filed` 27, `petition.carried` 5 and 2, `carry.refused` 19 and 16 at the 2026-11-01 probe) on the base commit.
- BUILDER: third tier (judgment).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-58

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-58 | Consent: acts admitted only on a council's count; `<verb>.unlicensed`; the discriminator at a data owner | BUILD | M | CR-57, CR-36, CR-37, CR-56 (landed `6e9550c4`) | which acts need consent is content (Jordan's) | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:517-529`):

````
### CR-58 — Consent: some acts are admitted only on a council's count, and a refusal says why (SC/IN) · BATCH B10-18c (after CR-57) · STATE BUILD (hash MOVER) · R R-04 (contributor)
- WHAT: no verb row carries a consent conjunct, so no act needs a sitting's count and nothing gives a ruler a reason to convene (reasons-to-convene §4 C; RL3). Add the licence conjunct to the owner's act (*the actor holds a live `resolution` naming this act's object*, CR-36's and CR-37's form) with its discriminator held at a data owner (a rung-kind or hold-kind row saying which cessions need consent), never in the effect (that would be scripting drift); and give a refusal on that conjunct its own kind (`<verb>.unlicensed`) so the refused owner holds a claim that says why, and that claim stamps the council's tier as his convene referent (CR-56's route).
- LANDED ALREADY: CR-36 (the `resolution` Record kind and `nominated`) and CR-37 (`joint_concurrence`), if landed by B10-17; `<verb>.refused` already deposits a claim.
- REMAINING UNBUILT: the conjunct for `give` of a hold and for `requisition`; the data owner; the new refusal kinds and their `verb_table.yaml` emits.
- GATE: after CR-57 and B10-17. NEEDS: CR-36, CR-37, CR-56 (landed `6e9550c4`). `warrant_sourced` maps one kind per verb and a listed verb then forms only on a subject a held Record names (`rosters.yaml:1931-1961`); the discriminator must live at a data owner, or `give: resolution` would gate every `give`.
- EXIT and FALSIFIER: seeds 0-2: an owner's act is refused for want of a held resolution, its refusal kind is `<verb>.unlicensed`, and a convening follows from it above 0 times. CONTROL: an owner whose act needs no count never convenes for it; the discriminator empty reproduces the pre-item hash.
- HASH MOVERS: declared MOVER.
- HOLES AND LEDGER IDS: H-90 (`hole_register.yaml:1126`), H-229.
- ASKS ATTACHED: which acts need consent is content (Jordan's, P11): the position builds the mechanism and one data row per act that the plan already rules (a cession of land, a requisition); no other row is authored.
- RE-BASE: the parliament design T3a (`2026-10-29-parliament-and-debate.md` §6) names the limit; read `warrant_sourced` first.
- BUILDER: third tier (judgment).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-59

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-59 | An appeal goes to another authority: the appellate closure basis (`appeal_to`) | BUILD (hand-built route) | E | CR-58, SC-04 (landed `bc5d987a`), CR-35, CR-51 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:530-542`):

````
### CR-59 — An appeal goes to another authority: the appellate closure basis (SC/IN) · BATCH B10-18c (after CR-58) · STATE BUILD (hash EQUAL: no computed route) · R R-04 (contributor)
- WHAT: R-35 wants an appeal to an authority, never back to the same bench. `pardon` closes a restraint only through the seat that is the edge's object (`state/gate.py`'s `determination` basis), so a crown seat cannot void a church custody or a ban (P4 stress claim 21). Add an appellate closure basis beside `pardon`'s: a seat named by the row's `appeal_to` may void, or commute one grade, a restraint opened under that row, on the record. Polity rows below the sovereign default `appeal_to: crown` (P4 critic finding 9).
- LANDED ALREADY: `pardon` (`loop/effects_governance.py`), `may_determine`, `detain` and `ban` as `RESTRAINT_KINDS`, SC-03a's rows.
- REMAINING UNBUILT: the basis in `gate.py`; the `appeal_to` key in `arrangements.yaml` and `data/arrangements.py`; a hand-built test.
- GATE: after CR-58 and SC-04, CR-35. NEEDS: SC-04 (landed `bc5d987a`), CR-35, CR-51 (a restraint exists).
- EXIT and FALSIFIER: a hand-built world: a crown seat voids a church `detain`; the same seat is refused on a restraint under a row with no `appeal_to`. No computed route is claimed. CONTROL: with no row carrying `appeal_to` the hash is EQUAL.
- HASH MOVERS: none (E).
- HOLES AND LEDGER IDS: H-90; R-35 (primitives §1).
- ASKS ATTACHED: none.
- RE-BASE: re-read `gate.py`'s `determination` and `warrant` bases by symbol on SC-04's landed tree.
- BUILDER: third tier (judgment).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-60

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-60 | Authority, scope and a two-valued rite default (`authority.by_faction`, `scope:`, case-opening reads `scope_rung`) | BUILD | M | CR-59, SC-04 (landed `bc5d987a`), CR-35 | P4 Q1 taken, revert stated | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:543-555`):

````
### CR-60 — Authority, scope and a two-valued rite default (SC/IN) · BATCH B10-18c (after CR-59) · STATE BUILD (hash MOVER: case-opening purview) · R R-04 (contributor)
- WHAT: R-34 gives a venue its force from the parties, the polity or the church; no row carries an authority, and the church cannot open or judge a case outside T9 because `offices.yaml` has one anchor that sets both `rung` and `scope_rung`. Add `authority.by_faction` to `rosters.yaml` (a mapping, the precedent of `role_templates.by_faction`); a `scope:` key on offices that `build_realm` passes as `scope_rung` (P4 repair m); case-opening that reads `scope_rung` as `sits_over` does, while `arrest`, `seize` and `issue` keep `rung` (repair g); and a rites block of two values, accusatorial and inquisitorial, that a row picks (P4 §3.4 cut back as its critic directed). One `may_determine`, with the authority conjunct inside the predicate (repair l).
- LANDED ALREADY: SC-03a and SC-04's rows and `disposes`; `bench_basis`; `judging_set`; the `titles` ladder; `faction_q`.
- REMAINING UNBUILT: the mapping, the `scope:` key and its loader, the case-opening read, the rite block and the authority conjunct.
- GATE: after CR-59. NEEDS: SC-04 (landed `bc5d987a`), CR-35, CR-38's interim two-seat bench (the interim bench stands until CR-38 lands). P4 Q1, whether the church may judge realm-wide while acting only where its `rung` reaches, is taken (§ASKS).
- EXIT and FALSIFIER: seeds 0-2: a church seat opens a case on a resident of a territory other than T9; the same accused under two rows gets two benches; the King is neither on a church bench nor admitted by the gate to judge a church-row matter. CONTROL: no `scope:` key reproduces the pre-item hash.
- HASH MOVERS: declared MOVER (which seat may open a case); one re-record.
- HOLES AND LEDGER IDS: H-80, H-90; the two `scope_rung`/`rung` anchors.
- ASKS ATTACHED: P4 Q1 taken: the church may judge realm-wide while acting only where its `rung` reaches `[ASSUMPTION; medium; Jordan to correct; revert: no `scope:` key, and R-36's own heresy example cannot occur]`; the reasoning is that without it the example in R-36 is impossible.
- RE-BASE: read `state/gate.py`'s `may_determine` and `sits_over` on the landed tree; the line numbers in P4 §6 were taken at `5c0e25ec`.
- BUILDER: third tier (judgment).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-61

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-61 | The case file: a Record of kind `case`, held, forgeable, burnable; the citation as a writ | BUILD | M | CR-60, CR-55 (landed `eb76f57f`), CR-57, CR-48 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:556-568`):

````
### CR-61 — The case file: a Record of kind `case`, held, forgeable, burnable (SC/IN) · BATCH B10-18c (after CR-60) · STATE BUILD (hash MOVER) · R R-04 (contributor)
- WHAT: a computed `open_case` writes a case file of kind `text` with no content and the H-80 default stage labels, and a second case on a docketed matter is refused (`effects_information.py:368`). Mint kind `case` whose stages are the rite's stage list (CR-60), with its readers landing in the same change: `determine`'s precondition asks for the held case file (a fifth conjunct), only its holder writes `stages`, `_mint_document` declines an existing id, `forge` accepts kind `case`, and the citation is a `dispensation` addressed to the party and served by CR-57's and CR-48's `give` (the writ-to-addressee mint stays refused). Defiance is a witnessed deed and a contempt ban needs no arm; an unserved warrant lapses visibly (CR-55's lapse).
- LANDED ALREADY: `_mint_document`, `_eff_open_case`, `_eff_forge`, `destroy_record`, `comply` and `evade / defy` (emission-only), CR-55's lapse.
- REMAINING UNBUILT: the `case` kind in `record_kinds`; the fifth `determine` conjunct (`verb_table.yaml:360`); the mint decline; `forge` on `case`; the citation; the stage list from the rite.
- GATE: after CR-60. NEEDS: CR-55 (landed `eb76f57f`: `<=`, the lapse), CR-57, CR-48. A kind lands with its readers (`rosters.yaml: record_kinds`' own note).
- EXIT and FALSIFIER: seeds 0-2: `docket_named_arrangement` above 0; burning the case file stalls `determine` and a restart is a new case; an overdue stage matures once when its holder returns; a citation unanswered emits a witnessed lapse. CONTROL: the `text` kind reproduces the pre-item hash; the H-80 labels move `BASE_HASHES[1, 2]` (`test_season_weather.py`) and the go07 `BASE` seeds, re-pinned and said plainly.
- HASH MOVERS: declared MOVER.
- HOLES AND LEDGER IDS: H-80, H-210, H-229.
- ASKS ATTACHED: none. P4's earlier batch A1 (deleting `VERB_CAPABILITY`, the discrete call and the H-80 labels first) is NOT taken: P4's critic showed A1 cannot be green as ordered (finding 11); each deletion lands with its replacement.
- RE-BASE: the H-80 default labels are deleted here, with the rite's stage list that replaces them.
- BUILDER: third tier (judgment).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-62

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-62 | A plea with a concession reward, tested through the obstacle before any grade cap | BUILD | M | CR-61, B10-08 (landed), CR-20 (landed `c7764a5a`) | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:569-581`):

````
### CR-62 — A plea with a concession reward, tested through the obstacle before any grade cap (SC/IN) · BATCH B10-18c (after CR-61) · STATE BUILD (hash MOVER) · R R-04 (contributor)
- WHAT: P4's plea fixes which question is tried (deny, concede the fact, concede the definition). Its critic found two methods for one quantity: grade caps rewrite the band outside `degree_from_net` (R-6, R-8), and the D-1 obstacle composition (the ceiling bounds the opponent's score, not the proofs and the aptness price added after it) removes the clip that justified the caps. First verify B10-08's closed form (see RE-BASE); then route the concession reward through the obstacle under D-1 and run the plea's dominance test against the control (deny alone best), and adopt grade caps only if the obstacle route fails it. An absentee resists at his own score ÷ 2 (R-5), not at the default 2.
- LANDED ALREADY: B10-08 (CLOSED): one faculty, one odds function, one ceiling; `roll.py::obstacle`; `degree_from_net`.
- REMAINING UNBUILT: the plea act's stage transitions (data); the D-1 composition in `obstacle()`; the absentee rule; the test.
- GATE: after CR-61. NEEDS: B10-08 (landed), CR-61, CR-20 (landed `c7764a5a`; attributes, so that pools differ).
- EXIT and FALSIFIER: a hand-built hearing and a seeded sweep: with the concession reward through the obstacle, deny is not best alone in more than 6 of 9 cells and a bare concession is not weakly dominated in 9 of 9 (the P2 control reading, `stress_p4_choices.py` log:6090). CONTROL: reward off reproduces P2's finding.
- HASH MOVERS: declared MOVER (every computed roll that composes an obstacle).
- HOLES AND LEDGER IDS: H-127, H-213.
- ASKS ATTACHED: none new; the cap route is held until the obstacle route has been tested.
- RE-BASE: FIRST: confirm B10-08's `p_success` equals P4's closed form at 2D and 12D (P4 §3.3: the live discrete roll read .581 against .430 at 2D) and that the ceiling bounds the score only. If not, this position waits for that edit and says so.
- BUILDER: third tier (judgment).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-64

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-64 | The forum is a stage of the same case (R-34 precedence) | BUILD (hand-built route) | E | CR-60, CR-61 | P4 Q5 taken, revert stated | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:595-607`):

````
### CR-64 — The forum is a stage of the same case (SC/IN) · BATCH B10-18c (after CR-62) · STATE BUILD (hash EQUAL until computed play opens it) · R R-04 (contributor)
- WHAT: a forum plea (Clarendon c. 3; Bruno) moves the docket item's row in place, decided by the other authority's seat by its own choice, with R-34's precedence (a royal party gives the matter to the polity if the polity claims it; otherwise the sitting bench keeps it by prevention). A second case on a docketed matter stays refused. P3's mutual forum contest is not adopted (its only equilibrium is impasse).
- LANDED ALREADY: the docket item's `arrangement` key (CR-61), `judging_set`, R-34.
- REMAINING UNBUILT: the forum transition and its precedence rule; the test.
- GATE: after CR-62. NEEDS: CR-60, CR-61. P4 Q5 ("a royal person is involved") is taken as a party `[ASSUMPTION; medium; Jordan to correct; revert: a bench member or the territory's ruler]`.
- EXIT and FALSIFIER: a hand-built hearing: a forum plea changes the item's row with no second case; the sitting bench keeps the matter when no royal party is involved. CONTROL: no forum plea reproduces the hash.
- HASH MOVERS: none until computed play forms it (E).
- HOLES AND LEDGER IDS: H-80.
- ASKS ATTACHED: P4 Q5 taken as above.
- RE-BASE: read CR-61's landed docket shape by symbol.
- BUILDER: third tier (judgment).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-63

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-63 | The five robust decisions as verb rows (proofs, self or advocate, naming enemies, the warrant duty, appear / evade / defy) | BUILD | M | CR-48, CR-51, CR-57, CR-61, CR-64, CR-20 (landed `c7764a5a`) | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:582-594`):

````
### CR-63 — The five robust decisions as verb rows (SC/IN) · BATCH B10-18c (after CR-64) · STATE BUILD (hash MOVER) · R R-04 (contributor), R-05
- WHAT: P4's critic kept five of its ten decisions as robust: which proofs to offer, self or advocate, naming mortal enemies, the warrant-holder's duty, and appear / evade / defy. Most of the ten are not acts the loop can form: there is no verb row for plea, offer-proof, speech kind, challenge a judge, name enemies, forum plea or come forward (P4 critic finding 12, accepted as BREAKS). Write the rows for the five, each with its writer, its `write_matrix.yaml` cell and its band writes, and price the defiance: a witnessed `compliance.withheld` deposits a deed claim and a warrant left unserved lapses visibly. The narrow options (judge challenge, forgery, impugn, cite-licence, the term of grace) stay held until the explanation contract can show a player why they matter.
- LANDED ALREADY: `comply`, `evade / defy`, `arrest`, `pardon`, `oblige`, `utter`; CR-48, CR-51, CR-57, CR-61.
- REMAINING UNBUILT: the verb rows and cells; the chooser's formation for each; the defiance deed.
- GATE: after CR-64. NEEDS: CR-48, CR-51, CR-57, CR-61, CR-64, CR-20 (landed `c7764a5a`).
- EXIT and FALSIFIER: seeds 0-2, an `aperture`-style run: each of the five is taken above 0; `compliance.given` and `compliance.withheld` are above 0; `arrest.made` above 0. CONTROL: each row switched off forms nothing and reproduces the pre-item hash.
- HASH MOVERS: declared MOVER.
- HOLES AND LEDGER IDS: H-94 (the operand vocabulary is closed: a row that needs an eleventh name is a stop), H-229.
- ASKS ATTACHED: none.
- RE-BASE: re-read P4 §4 for each choice's options and cost; the 2026-11-01 stress log is reference.
- BUILDER: third tier (judgment).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-74

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-74 | Religious sanction (CH): a strife signature on a restraint opened through a church seat, read from a property the institution already carries, or the missing carrier named (the strife fold, v11) | BUILD (harness) | E | CR-51, CR-63, IN-30 | — | written out in full: `-11` |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:38-55`):

````
### CR-74 — Religious sanction (CH): a signature on a restraint opened through a church seat (IN/FA) · BATCH B10-18c (directly after CR-63) · STATE BUILD (harness; hash EQUAL), or the missing carrier named · R —
- WHAT: CH has no kind (`strife_moves.yaml` CH `gap:`); `strife-00` §7: "a church seat issuing ban or detain tenures: data, and the seat". A CH signature reads an Event that opens a `detain` or `ban` (`arrest.made`, or the church-custody branch: CR-51's gap, which CR-51 builds "with CR-63's warrant duty", so the branch exists only after CR-63) whose causing act's `via` seat belongs to a church, read from a property the seat's institution already carries in code. The re-base looks for that property in this order: IN-30's `faction_props` (B10-17), an `offices.yaml` field naming the institution's kind, a faction's creed. A signature keyed on a named faction is refused (scripting drift, `CLAUDE.md` §0; the foreign-faction list is Jordan's ruling R16 and is no precedent for a church list). If no such property exists, the commit names the missing carrier and CH stays GAP; no roster is authored (P11).
- SIDE EFFECT, STATED: the residue counts an Event whose kind some signature names and that matches none (`strife.py::count_event`). Once CH has a signature on `arrest.made`, every arrest not through a church seat lands in the residue, because CA and PU are kind-only rows with no signature. That is intended and is labelled: the report prints those residue lines as "arrest, not through a church seat (CA, PU kind-only)", so they are not read as an unexplained mover, and S1r's "act plus residue equals one per Event" stays true. No CA or PU signature is added here (each needs side and office, which this position does not read).
- LANDED ALREADY: S1's instrument; the church seats in `offices.yaml` (the Cardinal seats, the Senior Inquisitor, faction "Church of Solmund").
- REMAINING UNBUILT: the signature or the named finding; the residue label; its test.
- GATE: CR-63 landed (this batch; CR-51 in B10-18b). NEEDS: CR-51, CR-63, IN-30.
- EXIT and FALSIFIER: at the batch close CH above 0 at some seed (`strife 3 0 1 2`; the batch declares movers, P10) or GAP with the carrier named; planted: a restraint opened through a church seat reads CH, the same restraint through a secular seat does not and appears in the labelled residue line. CONTROL: `content_hash` unchanged by the reading.
- HASH MOVERS: none (harness).
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: none (a church seat's authority to sanction is content, P11).
- RE-BASE: CR-51's and CR-63's outcomes (which restraint producer was built); the property search above.
- FILES: `engine/season/harness/strife.py`, `strife_moves.yaml` (the CH row and a signature), `engine/season/tests/test_strife_instrument.py`.
- VERB CLUSTER: no.
- LAYER 1: none.
- N-LINE: the CH signature — cut it and the gameplay experience is worse, because strife begun by the Church's own hand (the study's F and I categories, 15 cases) cannot be told from a secular arrest, so the report cannot say whether a religious strand can open in the realm at all.
- BUILDER: second tier.
- SOURCE: `strife-00` §7 (church sanction row), §8 S2; `-04` CR-51 (the church-custody branch, built with CR-63's warrant duty).

````

### CR-65

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-65 | The legitimacy index (design-first; held on P4 Q2) | DESIGN-FIRST, then BUILD only on approval | E (design) | CR-60 | P4 Q2 (Layer-1 F8) | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:608-620`):

````
### CR-65 — The legitimacy index (design-first, held on P4 Q2) (SC/IN) · BATCH B10-18c (last) · STATE DESIGN-FIRST, then BUILD only on approval · R R-04 (contributor)
- WHAT: R-36 scales an authority's weight in a territory by its legitimacy there. P4 reads it as a barrier index in `queries/cache`, built from residents' ledgers and read by the draw: its own critic calls that ED-SC-0040's read routed through a cache and *a stored magnitude between barriers* (S-7; P4 critic finding 16). Draft the design, argued against ED-SC-0040's precedent, with the L ≡ 1 control arm and the defined cases (an empty territory and a zero denominator read 0.5; NaN is refused, not clamped; `opinion_full <= 0` refused at load). Alternatively the effects of hostility (summons obedience, warrant service, a ban's bite) emerge from persons' own choices and the draw takes no L term at all, which the research (02 §3.5) supports.
- LANDED ALREADY: `world_q.opinion_of`, `person_q.legitimacy`, SC-02 `22b` step 23 (`standing_crossed`).
- REMAINING UNBUILT: the design file; the build only on approval.
- GATE: design drafted beside B10-18c; build after CR-60 if approved. NEEDS: the answer to P4 Q2 (may the draw read an index built from residents' ledgers, Layer-1 F8), which survives the answer-first ladder only if this position is built.
- EXIT and FALSIFIER: design approved by ED-1094's merge default unless held back; a built index shows an L ≡ 1 arm with no draw difference at control.
- HASH MOVERS: none at the design step (E).
- HOLES AND LEDGER IDS: H-222; ED-SC-0040.
- ASKS ATTACHED: P4 Q2 is the ask; the position does not build without it.
- RE-BASE: none.
- BUILDER: second tier (design).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-106

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-106 | Church-owned building kinds (`worship`, `templar_quarters`, `school`), the `site_owner` table (a kind-row cell naming an owning `factions` member), `faction_q.owner_of`, and the `site:` key that mints a Site from a venue row (the flow-conditioning fold, `ED-IN-0352`) | BUILD; content HELD BACK (first reading) | M | `ED-IN-0352` (landed in the fold) | — (the content is Jordan's to correct, P11) | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:131-153`):

````
### CR-106 — Church-owned building kinds, the owner table and the minting (IN/SE) · BATCH B11-F1 (settlement fabric) · STATE BUILD (roster rows, a loader table, a builder step; a declared hash mover; content authored here) · R —
- STATUS: PROPOSED; the merge ratifies the position (its rule, gate, falsifier and place in B11-F1). RATIFIED (Jordan, 2026-11-08): its CONTENT (`proposals/2026-11-08-flow-conditioning/content_church_sites.yaml`) as the accepted first reading; every cell keeps `[ASSUMPTION; medium; Jordan to correct]` and its revert.
- WHAT: Jordan's rule: buildings belong to the settlement and so to the governing faction, EXCEPT the Church of Solmund's (places of worship of differing scale, Templar quarters of varying size, schools and monasteries), which the Church always owns, never the faction owning the territory. The survey found that `engine/season/venues.yaml` (a runtime mechanism, its header `:15-19`) already puts a Church-tagged building (`serves: [Church]`) in every settlement type (`:68,73,79,85-88,97,103,108,116`) and `build_realm` mints a `hearth` rung for each (`harness/populated.py:1201-1210`), but the `serves:` tag never enters the World (its only reader seats persons, `populated.py:1284-1303`; ED-SE-0052, `registers/editorial_ledger_se.jsonl:1`, its first row; its last row `:6` supersedes it in part and carries the fabric-and-address ontology and "`hold` not reaching a `Site`" to ED-SE-0053 (`:7`), without restating the `serves:` sentence) and no Site kind names an owner. Four parts, each reusing an existing owner:
  - (a) KINDS. Three rows appended to `site_kinds` (`rosters.yaml:1741`, appended after `:1778`): `worship`, `templar_quarters`, `school` (names Jordan's; "schools/monasteries" is one function) `[ASSUMPTION; medium; Jordan to correct; revert: rename the rows]`. SCALE is `Site.condition` with `band_floors` rows (chapel, church, cathedral as bands of `worship`; sizes of `templar_quarters` likewise): ED-IN-0279 chose a Site's condition over a per-size alternative for fortification (`rosters.yaml:1759-1771`), H-38 rules `Site.condition` the model, and `restore`/`work` raising a building past a band floor already emits `condition.band_crossed` (`write_matrix.yaml:407-413`), so an upgrade needs no new verb; three separate kinds per function would duplicate that ladder. Each kind carries the required cells (`wear_per_season`, `band_floors`, `capacity_floor`; both-direction loader checks, `data/fixtures.py:106-111`; `rosters.yaml:1890-1896`); `wear_per_season` 0 ships as the control arm, as `dwelling` did (`rosters.yaml:1831`); `works_cost` optional (unpriced means `build` refuses, `loop/effects_founding.py:218-221`); no `site_yield` row.
  - (b) THE OWNER TABLE. A new table `site_owner` in `rosters.yaml`, `keys: [site_kinds]`, `default_cell: null`; a non-null cell names an owning institution, validated at load as a `factions` member (precedent: `HEAD_SEAT`, `data/rosters.py:1268-1274`, `require_member`). The three new kinds' cells name the Church of Solmund; null means owned through the rung, as today. The exception is DATA on the kind row; there is no branch on "Church" anywhere in code, and any institution with exclusive buildings uses the same cell.
  - (c) ONE OWNER OF OWNERSHIP. `queries/faction_q.py::owner_of(w, site) = SITE_OWNER[site.kind] or holder_faction_of(w, site.rung)`. No `hold` Tenure on a Site (refused by the roster `rosters.yaml:148-160`, by `World._refuse_bad_hold` `state/world.py:911-917` and by Layer 1 §15 `architecture/holonic_ARCHITECTURE.md:538`; ED-SE-0053 (its last row `editorial_ledger_se.jsonl:7`, RATIFIED AS INTENT ONLY) ratifies document 04, whose commons argument is the `:2` row's); no `Site.owner` field (a hash mover and a second home for what the kind row decides, §0.05 clause 3).
  - (d) MINTING. `venues.yaml` building rows gain an optional `site:` mapping `{kind, condition}` (a `site_kinds` member and its starting `condition`; ONE key, because the starting condition differs by row; the content draft spells it as two flat keys, `site:` and `site_condition:`, which the builder nests) `[ASSUMPTION; medium; Jordan to correct; revert: the flat pair]`; the builder mints `Site(f"s_{sid}_{slug}_{kind}", bid, kind, condition)` for any row carrying it, in the dwelling loop (`populated.py:1236-1240`); it reads no `serves` tag and no name. Uniform: any row may carry `site:`.
- CONTENT (authored here from Jordan's rulings, a first reading he corrects; he said "I already gave you P11 information to build from"): `proposals/2026-11-08-flow-conditioning/content_church_sites.yaml`, provenance per cell in `proposals/2026-11-08-flow-conditioning/content_provenance.md` (table A), checked by `proposals/2026-11-08-flow-conditioning/content_validate.py` (output `content_validate.out`). It gives: the three kinds with every per-kind cell (`wear_per_season` 0, `capacity_floor` 0, `works_cost` `{timber: 10}` like every fabric kind, H-166's one magnitude) and the `site_owner` cells naming the Church of Solmund; one three-floor `band_floors` ladder (100/500/800) borrowed from the body ladder (`rosters.yaml:3497-3500`, the only three-floor precedent) for chapel/church/cathedral and the Templar and school scales; each building starting at the midpoint of its band; 41 Church Sites in `build_realm(0)` (37 places of worship, 3 schools, 1 Templar quarters), Himmelenger's cathedral highest (1000) and the scale order village chapel < town church < cathedral holding; the `chapter_house` row carries the Templar quarters (Jordan says they exist; the plan's earlier "none at start" is withdrawn), the `almonry` row carries no `site:` (a charity house is not on his list). Coverage: every territory under `r_valoria` that holds a settlement holds at least one Church Site (the count is the validator's). `terr_T15` (no settlement in the geography) and `terr_ALT` (a foreign root whose one settlement has no venue rows) hold none; Jordan's "all territories" is read as every realm territory with a settlement (ladder step 5: buildings stand in settlements, and venue rows are per settlement) `[ASSUMPTION; medium; Jordan to correct; revert: carry a Church Site at those two by a row that is not a venue]`. Settlements of one type get identical buildings (Sigurdshelm's cathedral equals Valorsmark's seat cathedral, 900), since venue rows are per settlement type `[ASSUMPTION; medium; Jordan to correct; revert: per-settlement overrides]`. Pricing: `{timber: 10}`; unpriced kinds can never be newly built, so priced `[ASSUMPTION; medium; Jordan to correct; revert: unpriced]`.
- LANDED ALREADY: `site_kinds` and its per-kind tables; `Site.condition` and `band_floors`; `build` and `restore`/`work`; `venues.yaml`'s Church-tagged building rows and the hearth rungs they mint; `holder_faction_of` (`queries/world_q.py:2447,2472`); the default ownership of a Site by its rung's holder (`hold_force`, `governing_hold`, `loop/effects_founding.py:115-121, 209-213`).
- REMAINING UNBUILT: the three rows and their cells; the `site_owner` table and its loader; `owner_of`; the `site:` key and the minting step; the hole row; the tests.
- GATE: `ED-IN-0352` landed. NEEDS: `ED-IN-0352`.
- EXIT and FALSIFIER (hand-built worlds, P9): (1) a planted `worship` Site on a rung held by another faction: `owner_of` reads the Church's proposition; set that table cell null and it reads the rung's holder; (2) the rename falsifier (every id and faction name renamed consistently, `site_owner` cells included) changes no reading; (3) in `build_realm(0)` the number of `worship` Sites equals the number of settlements whose venue rows carry `worship`, asserted by counting `venues.yaml` rows in the test and not by a literal, and every territory under `r_valoria` that holds a settlement holds at least one Church-owned Site (the validator's check; `terr_T15` holds no settlement, and `terr_ALT` is a foreign root whose one settlement, `set_alt_1`, `populated.py:1173-1178`, has no venue rows); (4) with no row carrying `site:`, the World and its hash are unchanged. MUTATION: key `owner_of` on the kind's name and (1)'s null-cell variant reads red. CONTROLS: `wear_per_season` 0 (the control arm); `content_hash` EQUAL when no row carries `site:`; the control-arm identity `test_24d_i_...moves_no_question_in_one_season` is re-read with the Church Sites present and its result stated (the dwelling control relied on an EMPTY band cell so the `floor` stem raised, `rosters.yaml:3470-3481`, and the Church kinds' `{100,500,800}` rows remove that guard; MATTER also writes every Site every season at rate 0 and emits `condition.worn`, `rosters.yaml:1846-1848`, and `work` forms on a Site-classed referent, `world_q.py:3228`, so the Church Sites enter `work`/`restore`'s referent space: a reading, stated, not hidden).
- HASH MOVERS: `build_realm(0).content_hash()` MOVES where rows carry `site:` (new Sites fold into the encoding, `state/world.py:1664,1704-1707`); pre-change reading per P14; re-pinned once in the batch's pin commit (P15).
- HOLES AND LEDGER IDS: one `hole_register.yaml` row (kind `RULING`, grade `assumption`: the three names, the null-cell rule and the first-reading rows, with the revert above); `ED-IN-0352` records the ownership rule (item 7).
- ASKS ATTACHED: none (the content is Jordan's under P11 and is named above, not asked).
- RE-BASE: `venues.yaml` and `populated.py`'s dwelling loop as the settlement-lane batches that edit them leave them (not checked here).
- FILES: `engine/season/rosters.yaml`, `engine/season/data/rosters.py`, `engine/season/data/fixtures.py`, `engine/season/venues.yaml`, `engine/season/harness/populated.py`, `engine/season/queries/faction_q.py`, `engine/season/hole_register.yaml`, `engine/season/tests/test_cr106_church_sites.py` (new).
- VERB CLUSTER: no.
- LAYER 1: none (no `hold` on a Site, no Site field, no Tenure kind; ED-SE-0053 and Layer 1 §15 untouched).
- N-LINE: the Church-owned building kinds — cut them and the gameplay experience is worse, because the Church's reach into every territory, which canon makes the source of its political weight, would exist only in prose, and a territory's lord could seize or tax what is the Church's by right.
- BUILDER: second tier for the rows and loader; a third-tier (judgment) critic on the null-cell rule.
- SOURCE: Jordan's description of 2026-11-08 (settlement infrastructure and the Church exception); the Fable survey of that date.

````

### CR-107

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-107 | Several cohorts per settlement: `label:`, `heritage:`, `conviction:` on the cohort row, the id `cohort_<rung>_<label>`, the summed-weight ceiling; `faction:` HELD as CR-107b (the flow-conditioning fold, `ED-IN-0352`) | BUILD (loader EQUAL; content commit a mover); content HELD BACK | E (loader); M (content) | `ED-IN-0352` (landed in the fold); not a dependency: SE-06 (re-bases on it) | — (the content is Jordan's to correct, P11) | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:154-181`):

````
### CR-107 — Several cohorts per settlement, identified by caste, creed and allegiance (IN/SE) · BATCH B11-F1 (settlement fabric) · STATE BUILD (a loader change and a ceiling fix; hash EQUAL until rows are added) · R —
- STATUS: PROPOSED; the merge ratifies the position (the loader keys, the summed ceiling, its place in B11-F1). RATIFIED (Jordan, 2026-11-08): its CONTENT (`proposals/2026-11-08-flow-conditioning/content_cohorts.yaml`) as the accepted first reading, every row keeping `[ASSUMPTION; medium; Jordan to correct]`; CR-107b (`faction:`) as a held position behind the reader audit below (not built, not a member, no row); the Schoenland `engages:` cell, made at this position's build.
- WHAT: Jordan: settlements require several cohorts to represent the caste system, the contest between Einhir Revivalism and the Church of Solmund and/or the Altonian political system, and faction allegiances; cohorts may conflict in feelings and demands, and converge or diverge on everyday needs. Today a cohort's identity is its rung alone (`cohorts.yaml` rows `{rung, weight}`; the loader refuses a second row on a rung, `harness/populated.py:384-390`, and the id is `COHORT_PREFIX + rung`, `:499-504`). Three additions to the row and one held, all optional so that an old row reproduces today's id and hash:
  - `label:` (one word): the id becomes `cohort_<rung>_<label>`, and the duplicate test runs over `(rung, label)`. The `guards:` block (`populated.py:523-541`) is the precedent for a second cohort family with its own fields.
  - `heritage:` a `Person.heritage` member (`state/carriers.py:819-826`; five members, `descriptor_registry.yaml:240-244`): the caste carrier. The thrust layer rules there is no caste store (`proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md:501`) and CR-31 (B10-13) reads caste as an estimate off a `seen` heritage claim, so the cohort's heritage is the data the estimate reads. The thrust layer's D3 makes caste a Query over persons' convictions, and the cohort's `conviction` map feeds that Query, so both tree readings are carried `[ASSUMPTION; medium; Jordan to correct; revert: heritage only]`.
  - `conviction:` a map validated by `data/affiliations.py::conviction_map` (`:39`) over the affiliations (`solmund_orthodoxy`, `einhir_restoration`, `altonian_civics`, the others). This is SE-06's held conviction half (`workplans/valoria_master_workplan_v11_part5.md:101-111`): its GATE asks for a source or a ruling, and Jordan's statement above is the ruling that settlements hold opposed creeds in separate cohorts; the territory-derivation alternative (SE-06's residues (iii) and (iv): two Piety tables disagree, and no rule splits one bipolar track into unipolar intensities) would make every cohort of a territory identical, which defeats the contest he describes. CR-107 builds the loader path; SE-06 stays the owner of the conviction content and re-bases on this entry (§8: one owner).
  - `faction:` HELD (CR-107b, not built here): a faction member whose `commit` Tenure the builder would mint (cohorts hold none today, `populated.py:448`). A `commit` makes the faction OCCUPY the settlement at build (`occupies` → `mustered`, `queries/world_q.py:2131-2172`; the cohort's `contain` sits at the settlement, `populated.py:517`), licensing `seize`/`raze` (`loop/effects_information.py:1017-1031`, `loop/effects_founding.py:253-290`) and levies (`raisable_by`, `world_q.py:2185-2194`) from tick 0, adding acquaintance pairs (`acquaintance_pairs` runs after `seat_cohorts`, `populated.py:1976` vs `:1988-1989`, and its docstring at `:603`, "A cohort commits to no faction", would be false) and opinion referents (`world_q.py:3049-3051`), and turning `engine/season/tests/test_in36_foreign.py:120` (`members(foreign, FID) == CAST`) red. It is built only after a reader audit enumerates `occupies`, `mustered`, `standing_at`, `raisable_by`, `acquaintance_pairs`, `opinion_referents`, `footprint` and `density` and re-pins that test. Until then allegiance is carried by `heritage` and `conviction`; the shipped content carries no `faction:`.
  - THE CEILING FIX: `seat_cohorts` checks each row's weight against `capacity(w, rung)` (`populated.py:492-498`) while `population` sums residents' weights (`queries/world_q.py:1785-1798`) and `has_room` throttles `migrate` on that sum (`:1883-1899`); two cohorts of weight 2 at a capacity-4 settlement would each pass and fill it. The check becomes the SUM of the rung's cohort weights against `capacity`.
- CONTENT (authored here, a first reading he corrects; revised once after the independent attack): `proposals/2026-11-08-flow-conditioning/content_cohorts.yaml` (51 rows over the 37 settlements, replacing the `cohorts:` block; `temperaments:` and `guards:` stay), provenance, rejected alternatives and the ladder's choices in `proposals/2026-11-08-flow-conditioning/content_provenance.md` (table B), validated by `proposals/2026-11-08-flow-conditioning/content_validate.py` (69 PASS, 0 FAIL, exit 0, which also re-derives every row from the stated rules and diffs it). 14 settlements hold more than one cohort; 8 hold BOTH a northern and a southern Einhir cohort (S-026, S-028, S-029, S-030, S-031, S-032, S-033, S-034), which is Jordan's own example; no row carries `faction:`. Rules: (H) heritage from the canon timeline's territory gradient as the geography's calamity radiation bands (`valoria_geography_v30.yaml`) carry it, and the faction holdings, and `faction_politics_v30.md:655-657`, translated to the ENGINE's territory for each place (Jordan's ruling that engine locations govern): `:657`'s explicit territory ids win over `:655`'s "Varfell highlands", which lands on T11, so T11's majority is northern and a southern cohort sits beside it where capacity admits; (V) one conviction rule keyed on whether a heritage holds a majority cohort in a territory under `r_valoria`: for the Einhir heritages (data: central, northern, southern) the engaged affiliation reads `6 − band` for southern heritage (band 1 → 5, 2 → 4, 3 → 3) and `solmund_orthodoxy` reads `1 + band` capped at 5 for northern and central cohorts (minority rows included, or they would read all 1s and carry no creed contest), the Church's seat territory reads 5, every other member 1, with the radiation bands from `systems/settlements/valoria_geography_v30.yaml:842-872`; for the other heritages (altonian, schoenlander) the engaged affiliation reads the cast median of the faction whose rows carry that heritage, which gives the S-007 Altonian cohort `altonian_civics: 4` `[ASSUMPTION; medium; Jordan to correct; revert: 1 everywhere]`. The two quarantined Piety tables are rejected (they disagree on T1, T2, T3, T6, T13, T14; each is one two-ended track with no split rule), and the cast median over a whole populace is the rejected alternative for Einhir cohorts (it gave every populace its leaders' ceiling and flattened the canon gradient). Majority cohorts carry no `label:`; their ids stay as today.
- A GAP, NOT FILLED: the `schoenlander` heritage has no `engages:` cell in the registry (`descriptor_registry.yaml`, ED-IN-0301's confirmed cells), so the Schoenland cohort (S-037) holds 1 throughout and that populace has a heritage but no intensity. Adding `schoenlander: altonia` to `engages:` would fix it, but it edits a confirmed registry row, which is canon-adjacent data; it is recorded here and left for the owner of that registry, not made.
- FACTION ALIASES: none added. `FACTION_ALIAS` is derived from `engine/substrate/names.py::ALIASES`, the export of `references/names_index.yaml` (`data/rosters.py:1455`), and `Altonian` and `Einhir` are canonical names of peoples there (`names_index.yaml:352-353`; `canonical_for` checks ALIASES before CANONICAL, `names.py:89-96`), so an alias would silently re-point a canonical. The shipped content carries no `faction:` and reads allegiance from `heritage` and `conviction`; venue `seats:` rows are the NPC seating table and not an allegiance source.
- CONSEQUENCES THE CONTENT CREATES (stated, not hidden): every two-cohort village and fortress is at `capacity`, so `migrate` into it is refused from the first tick (the existing throttle, `has_room`, `queries/world_q.py:1883-1899`); orthodox and Revivalist cohorts in one settlement are `incompatible` under `commensurate`, so their tellings discount each other at once; no `commit` Tenure is minted, so no faction reader moves (CR-107b holds that); and NOT CARRIED: "convergence and divergence for everyday needs" — both cohorts of a settlement take the territory's one pursuit vector (`populated.py:481-482, 514`; `cohorts.yaml:105-106`) and the row has no pursuit field, so divergence on needs cannot occur yet; a `pursuits:` field on the row is the carrier and is not designed here.
- BEHAVIOUR WITH SEVERAL COHORTS (read, not changed): `subsistence_draw` draws per eater by weight (`world_q.py:1272-1297`), so demand doubles with no edit; `commensurate` over `Person.conviction` and `_credit` at WITNESS (`world_q.py:5250-5269`, `loop/witness.py:240-261`) discount two opposed-creed cohorts' tellings as soon as they hold convictions, with no edit; CR-100's within-stamp keys on home ancestry, so both cohorts of a settlement receive identical stamps and divergence enters only through convictions and faction. SE-04 (c)'s closure (one cohort splitting) is not reopened by authored cohorts.
- LANDED ALREADY: the cohort loader, `seat_cohorts`, `capacity`, `commensurate`, `_credit`; `Person.heritage` (cast-only today, never written in play).
- REMAINING UNBUILT: the four keys and their validation, the id change, the summed ceiling, the hole row, the tests.
- GATE: `ED-IN-0352` landed. NEEDS: `ED-IN-0352`.
- EXIT and FALSIFIER (hand-built worlds): (1) two planted cohorts of opposed creeds (an `incompatible` pair) in one settlement: `commensurate` reads -1 and a telling between them lands at a discounted confidence (`_credit`), the same teller to a cohort of the same creed does not; (2) a summed weight over `capacity` is refused at seating; (3) two rows on one `(rung, label)` are refused, and a row with no new key reproduces today's id and hash (EQUAL); (4) a `faction:` row mints exactly one `commit` Tenure; (5) the rename falsifier. MUTATION: check each row's weight alone and (2) reads red. CONTROLS: the shipped `cohorts.yaml` unchanged gives `content_hash` EQUAL; the authored rows are a separate content commit and a declared hash mover (P14, P15).
- HASH MOVERS: none from the loader change alone; the authored rows move every hash from `build_realm(0)` on (a golden re-record, stated plainly).
- HOLES AND LEDGER IDS: one `hole_register.yaml` row (kind `RULING`, grade `assumption`) for the summed-ceiling reading; SE-06's rows H-170 and H-171 are cited, not edited.
- ASKS ATTACHED: none (the content is Jordan's).
- RE-BASE: SE-06's entry and the `temperament_rows`/`seat_cohorts` code as the held batch leaves them; the readers CR-107b's audit lists (`faction_q.members`/`resolve`, `world_q.py:2026-2037`, and their callers).
- FILES: `engine/season/harness/populated.py`, `engine/season/cohorts.yaml` (the authored `cohorts:` block; comment lines `:21-23`, stale, corrected), `engine/season/data/affiliations.py` (read only), `engine/season/hole_register.yaml`, `engine/season/tests/test_cr107_cohort_identity.py` (new).
- VERB CLUSTER: no.
- LAYER 1: none.
- N-LINE: several cohorts per settlement — cut them and the gameplay experience is worse, because a town could hold only one mood, so the caste, creed and allegiance contests Jordan describes could not occur inside a settlement, and strife flows would have no populace to divide.
- BUILDER: second tier for the loader; the content pass is a separate judgment lane.
- SOURCE: Jordan's description of 2026-11-08 (cohorts and the three axes); SE-06 (`part5.md:101-111`); the Fable survey.

````

### CR-104

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-104 | Institutional reach: `faction_q.influence_rung(w, office_id)`, the lowest rung covering a head seat's institution (its seats, holdings and owned Sites, `owned_site_rungs`); `world_q.lowest_covering` extracted as the one owner (the flow-conditioning fold, `ED-IN-0352`) | BUILD | E | `ED-IN-0352`, CR-106 | — | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:182-201`):

````
### CR-104 — Institutional reach: the influence rung of an office (IN/FA) · BATCH B11-F2 (first item) · STATE BUILD (a query and its test; hash EQUAL: no loop consumer until CR-102) · R —
- STATUS: PROPOSED; the merge ratifies the position. HELD BACK: nothing beyond its `[ASSUMPTION]` (the head-only reading), which carries its revert.
- WHAT: one function, `queries/faction_q.py::influence_rung(w, office_id) -> rung id`: the lowest rung covering (a) the office's own `Office.rung` and, ONLY IF the office is the head seat of a faction (`HEAD_SEAT`, `engine/season/data/rosters.py:1268`, the roster `rosters.yaml: factions.head_seat` at `engine/season/rosters.yaml:2019-2023`, CR-86/ED-IN-0342), (b) every rung in that faction's `holdings`, (c) the `Office.rung` of every seat in its `seats` (`faction_q.resolve`) and (d) the rungs of the Sites the faction OWNS: a sibling query `faction_q.owned_site_rungs(w, prop)`, the sorted rungs of the Sites whose `owner_of` (CR-106) resolves to the faction. `faction_q.Faction` is a five-field view key-locked to `record_kinds.faction_sheet` (`queries/faction_q.py:60-70`), so `holdings` is NOT widened; (d) is a sibling. The covering rule is the one that gives `Strand.rung` (`queries/world_q.py:4922-4932`, `_StrifeReading.lowest_covering`, used at `:5057`), extracted to a module-level `world_q.lowest_covering(ancestry_of, places)` that the method then calls: one owner of "lowest covering rung". The influence ORDINAL, where a number is needed (CR-102), is `RUNG_KINDS.index(kind) + 1` (`data/rosters.py:740`; realm highest) through a one-line helper that `flow_capacity` (`queries/world_q.py:4829-4833`, which counts from the top as `len − index`) then calls (D6). An office heading nothing reads its own seat's rung; a non-head office of a wide institution reads its own seat's rung (the head exercises the institution's reach) `[ASSUMPTION; medium; Jordan to correct; revert: every office of a faction reads the faction's covering rung]`.
- WHY THIS ROUTE (the ladder, `CLAUDE.md` §0). Jordan's reason for the Church (churches and infrastructure of varying size in all territories) is now carried: CR-106 stands Church-owned `worship` (and school, Templar) Sites in the settlements whose venue rows carry them, owned by the Church whatever faction holds the rung, so the Church's covering rung is the realm because its OWNED BUILDINGS span the territories, not because of its seats. Canon names the apparatus (`canon/03_canonical_timeline.md:50,58,62,64`: Cardinals, diocesan structure, Knights Templar, educational monopoly, a cathedral city with tax-exempt lands) and the quarantined design the mechanism (`franchise_v30.md:80`, quarantined: "Church settlements ... count as infrastructure in ANY territory where they exist, regardless of controller"), reference not authority. Measured on `build_realm(0)` (2026-11-08) before CR-106, `[UNREPRODUCED; re-read at CR-104's build]`: the lowest covering rung of each faction's holdings ∪ seat rungs is Church of Solmund `r_valoria` (holdings `terr_T9` only; seats at `terr_T9` ×6 and `terr_T1` ×1; `terr_T9` hangs off `r_valoria` directly, `harness/populated.py:1154-1156`, so the second seat lifts it to the realm); Valorsmark `r_valoria`; Hafenmark `duchy_hafenmark`; Varfell `duchy_varfell`; Guilds `duchy_hafenmark`; Löwenritter `terr_T1`; Restoration Movement `terr_T15`; Altonia `terr_ALT`. Head seats: Valorsmark → `off_king` (realm) held by `p_npc_020`; Hafenmark → `off_duchess_hafenmark` (duchy) `p_npc_050`; Varfell → `off_duke_varfell` (duchy) `p_npc_052`; Church → `off_confessor` (territory T9) `p_npc_021`. Routes rejected: affiliation presence (a believer is not an institution's infrastructure and the same reading gives `altonian_civics` a realm reach); Church seats in every territory (needs holders the registry lacks); a `hold` on a Site and a `Site.owner` field (CR-106 (c)).
- STATED LIMITS: (1) before CR-106 lands, the Church reads the realm only because `terr_T9` is in no duchy and a second seat (T1) lies outside it; with CR-106 it reads the realm from its owned Sites even with `off_archbishops_rep` deleted. (2) `seats` and `holdings` are what the faction's committed members hold (`faction_q.resolve`), so a member holding an unrelated seat elsewhere widens the reading. (3) A Site's owner is read from its kind's row; a Church building the Church does not own (a seized one) is not representable, since ownership follows the kind.
- LANDED ALREADY: `faction_q.resolve` (`holdings`, `seats`, `head`), `faction_q.head` with the CR-86 head-seat branch (`queries/faction_q.py:116-155`), `rosters.yaml: factions.head_seat` (four rows), `_StrifeReading.lowest_covering`, `flow_capacity`, `RUNG_KINDS`.
- REMAINING UNBUILT: `influence_rung`; `owned_site_rungs`; the two one-line extractions (`lowest_covering`, the rung-position helper) with their original callers routed through them; the test.
- GATE: `ED-IN-0352` and CR-106 landed. NEEDS: `ED-IN-0352`, CR-106.
- EXIT and FALSIFIER (hand-built worlds, v11 P9; and one `build_realm(0)` reading): (1) a planted realm whose head seat sits in a territory contained by the realm root and whose institution owns `worship`-analogue Sites in two territories of one duchy reads the head seat at that duchy; add a Site in a third territory under another duchy and it reads the realm; (2) the Church-analogue with ONE seat at T9 and owned Sites in several territories reads the realm (red before CR-106, green after: the carrier's falsifier for Jordan's reason, run as a test once CR-106 exists); remove every Church seat but the Confessor and it still reads the realm; (3) a single-seat office with no owned Sites reads its seat's rung; (4) the rename falsifier changes no reading; (5) `build_realm(0)` reads `off_king` and `off_confessor` at a realm-kind rung and `off_duchess_hafenmark`, `off_duke_varfell` at duchy-kind rungs, asserted by rung KIND over all offices (the test enumerates offices and checks kinds; it names no office or person); (6) null every `site_owner` cell and the reading falls back to holdings ∪ seats (the control). MUTATION: drop the owned-site term and (2) reads the territory (red). CONTROL: `flow_capacity` and `Strand.rung` return what they returned before the extractions on `engine/season/tests/test_strife_flows.py`; `content_hash` unchanged by this position. EXPECTED: all pass; mutation red.
- HASH MOVERS: none (no loop consumer; hash EQUAL by construction).
- HOLES AND LEDGER IDS: one `hole_register.yaml` row (kind `RULING`, grade `assumption`, H-274's shape at `engine/season/hole_register.yaml:5449-5460`: the head-only reading, the owned-site term and the three limits, with the revert above).
- ASKS ATTACHED: none.
- RE-BASE: `faction_q.head`'s branches and `HEAD_SEAT` as B10-17 (IN-30's `faction_props`) and B10-17b (CR-88's head seats) leave them; CR-106's table and `owner_of`.
- FILES: `engine/season/queries/faction_q.py`, `engine/season/queries/world_q.py` (the two extractions), `engine/season/hole_register.yaml`, `engine/season/tests/test_cr104_influence_rung.py` (new).
- VERB CLUSTER: no.
- LAYER 1: `04_CODE_ARCHITECTURE.md:168` (`queries/world_q`: reads any store via World, no token) and the `faction_q` row of §A.2; a new query, no hunk.
- N-LINE: the influence rung — cut it and the gameplay experience is worse, because without one structural reading of how far an office's institution reaches, the Church's head weighs as a territory notable two rungs below the dukes although canon gives the Church the greatest standing influence, and the realm's greatest actors could only be made great by naming them.
- BUILDER: second tier; a third-tier (judgment) critic on the head-only `[ASSUMPTION]`.
- SOURCE: Jordan's D7 ruling and his settlement description (this session); CR-86 (ED-IN-0342) for the head seats; the Fable survey.

````

### CR-97

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-97 | Measure plot points and office influence: columns (a) to (h) on `strife.py::strands_block` (turns, closure class, chains in strands, office influence per move, referent breadth, dissemination, presence, the field the stamp would reach, the emergence row), three controls, per-seed spread | MEASURE (harness) | E | `ED-IN-0352`, CR-104 | — | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:202-239`):

````
### CR-97 — Measure plot points and office influence (IN) · BATCH B11-F2 · STATE MEASURE (a harness reading and its test; hash EQUAL) · R —
- STATUS: PROPOSED; the merge ratifies the position. HELD BACK: nothing (a harness reading).
- WHAT: extend the strands block (`engine/season/harness/strife.py:389-430`, `strands_block`; a reading, grades nothing, V2) with the columns below, every one computed from the finished log and the act store, reusing `harness/arc.py` (`consequence_acts` `:327`, `shuffled_causes` `:213`), `harness/chronicle.py` (`chain_ends` `:170`), `harness/storybar.py` (`chains` `:373`) and `world_q.flows_in` with the harness's code-level `terminal_for` (`harness/strife.py:221-233`). Nothing is built beside them.
  - (a) PLOT POINTS, per strand. TURN (computed from the log, never from live state: `open_referents` reads the world as it stands, `queries/world_q.py:5068-5088`, so it cannot say what was open at a past tick): a strand move whose own Event writes a change, on a strand referent or party, to a store `open_referents` reads (the strand-move kinds, `MOVE_KINDS` (`world_q.py:4745-4746`), whose `write_matrix.yaml` row writes a store `open_referents` reads (restraint Tenures, war Propositions, DocketItems), derived in code from the matrix at import and never listed here; a war Proposition has no strand-move writer until `declare`, B10-17, so the war clause reads 0 until then) or opens or closes a `hold` Tenure on a strand referent (`tenure.opened`/`tenure.closed`: its holder changes). A PLOT POINT is an opening move, a TURN reachable from it by `causes*`, and a consequence act (`arc.consequence_acts`) in that chain. Reported: the share of strands with at least one plot point; the share of moves that are consequence acts; the share of turns reachable by `causes*` from an opening move.
  - (a') CLOSURE CLASS, per strand, derived in code from the strand's latest terminal move: `decider` if its causing act (`state/attribution.py:91-102`) exists and its verb row declares no `contests:` prize and is not named by the `graded_inquiries` route (a roster route in `rosters.yaml`, named in `verb_table.yaml:1686`'s `emits_note`; not a verb-row field) (a person's choice ended it); `roll` if the causing act's verb declares `contests:` or is so named (a contest resolved it); `threshold` if the Event has no causing act (a MATTER or CALENDAR Event); `open` if the strand is not concluded at the horizon (`world_q.concluded`). The labels borrow the vocabulary of `engine/season/ENDINGS_CLASSIFIED.yaml` (DECIDER/ROLL/THRESHOLD/NEVER); that file is an agent classification of arc prose (its own header) and is read by nothing here (§0.05 clause 2).
  - (b) CHAINS IN STRANDS: for every consequence chain of depth ≥ D (D = 3, the deepest depth the folding session measured (its collation is not kept in the tree) `[ASSUMPTION; medium; Jordan to correct; revert: D = 2]`), whether its Events are strand moves.
  - (c) OFFICE INFLUENCE, per move: (i) the rung kind of the seat exercised (`causing_act(w, e).via` → `w.offices[via].rung` → kind), with the `via=None` and `act=None` shares; (ii) the highest rung kind among the doer's live `hold` tenures (the walk `own_purview` makes, `queries/world_q.py:1079-1098`); (iii) the rung kind of `faction_q.influence_rung(w, via)` (CR-104).
  - (d) REFERENT BREADTH: whether a seat-exercised move's subject lifts the strand's `rung` (the strand's lowest covering rung before and after the move).
  - (e) DISSEMINATION: per act-caused Event, the number of `claim.deposited` Events whose `causes` names it (`loop/witness.py:689`, `:801`), grouped by (c)(iii)'s rung kind. (The obligee channel `epistemic._ch_post_remit`, `epistemic.py:563-583`, is the seat route; the IN-22 purview limb, `loop/witness.py:545-555`, admits ACTORLESS Events only, so it carries no seat act.)
  - (f) PRESENCE: per person, whether he appears as doer in a `causes*` chain of depth ≥ D.
  - (g) THE FIELD THE STAMP WOULD REACH (CR-100's dose, read before it is built): per round-end world, for every person, the number of open strands he is within (`s.rung` in his home's ancestry; `within`'s person limb, `queries/world_q.py:5236-5247`) and the number of referents those strands would stamp (after `FLOW_STAKE_CLASSES`); and the number of strands the kind-level terminal (`default_terminal`, `:5061-5065`) reads open while `terminal_for` reads concluded (the disagreement CR-100 inherits). Reported as readings, no bar (V2): the fraction of persons with a non-empty within-stamp; the fraction of that stamp that comes from realm-rung strands alone (a stamp every person receives equally conditions no one in particular, so CR-103 reads the lift against the SHUFFLED arm); and the dose asserted ≤ Σ `flow_capacity(kind)` over the kinds in the person's ancestry, a bound by construction (the test plants K > capacity open strands at one duchy).
  - (h) EMERGENCE ROW: the set of persons holding a head seat whose `influence_rung` is of realm or duchy kind, printed as ids and names in the report (a result row; no test keys on a name). On `build_realm(0)` it is expected to read `p_npc_020`, `p_npc_050`, `p_npc_052`, `p_npc_021` (CR-104's measurement).
  - SPREAD: every number above is printed per seed and, where several seeds are read, as min, max and spread (max − min). At this position's own commit the OFF reading is taken at seeds 0, 1, 2 (P10/P14: B11-F2 declares CR-100 a mover), with N strands per seed printed beside P and Q, so CR-102's gate and CR-103's WIDE-SPREAD and QUANTISATION clauses are readable before CR-100 is built.
  - CONTROLS: `arc.shuffled_causes` (causal links shuffled); shuffled strand membership (moves re-dealt to strands of the same sizes, seeded); a matched-holder control for (c) to (f), matched on act count AND verb mix (otherwise `own`-verb petitioners are compared with `remit` issuers).
  - HORIZON: three seasons, seeds 0, 1, 2 (strife reading, P10's exception, with P10/P14's three seeds because the batch declares a mover; the arc columns ride P16 (1)'s arc exception). Four only if the three-season reading has fewer than two strands with any move (risk 8's logic applied to this instrument).
- LANDED ALREADY:
  - Strands link by `_links` (`queries/world_q.py:5001-5016`): a shared referent, a parent/child one rung step apart, or the same doer; never by `causes`.
  - A strand stays open while any referent is docketed (`open_referents`, `:5068-5088`); the blocker to conclusion is docket closure (H-254, `engine/season/hole_register.yaml:5189`). Terminal codes are reached at all (H-274's and H-275's readings, `:5459`, `:5471`).
  - `causing_act(w, e)` returns the Act (`state/attribution.py:91-102`), so the seat is recoverable per Event in a harness.
  - Most strand moves carry no seat: `petition` (`verb_table.yaml:1219`), `commit` (`:211`), `fight` (`:735`) and `accept` (`:953`) are `own`; `march` (`:1051`, `remit:dispatch`), `issue` (`:686`), `determine` (`:364`), and the other `remit:` rows carry `via`; MATTER Events have no causing act.
  - `Act.via` (`state/carriers.py:714-730`) is set at mint (`decision/choose.py:744`).
  - Seats and rungs (`engine/season/offices.yaml`): `off_king` realm (`:187-189`), `off_duke_valorsmark` duchy (`:200-202`), `off_duchess_hafenmark` duchy (`:213-215`), `off_duke_varfell` duchy (`:226-228`), `off_confessor` territory T9 (`:369-371`; `faction: null` in the file at `:373`, filled to "Church of Solmund" in `build_realm(0)`, measured; its note `:380`: "`governs: "ecclesiastical institution"` is not a rung kind"). Rung ladder `engine/season/rosters.yaml:281`. The authored realm is `harness/populated.py::build_realm` (`:1014`).
  - The 16 links in `strife_moves.yaml` are `[UNVERIFIED]` (`engine/season/harness/strife_moves.yaml:117`), 4 unreachable, and not a weight source.
  - One-season reading (seed 0, `build_realm(0)` + one season, 2026-11-08; reproduce the strands: `python -m engine.season.harness.strife 1 0 --strands`, re-read at HEAD `e4d0bb5` on 2026-11-08 it prints 3 strands, `r_valoria` 14 moves (open), `duchy_hafenmark` 6 (concluded) and `b_s_014_barracks` 3 (concluded), "concluded 2 of 3", "docketed 2"; at the plan's base `d87946a` the same command printed 4 strands (15/6/3/2, "concluded 2 of 4" under the harness's code-level terminal (`terminal_for`), against the "3 open" below, read under the plan's own count (the two-test disagreement CR-97 (g) measures), "docketed 3", the cathedral strand `b_s_036_cathedral` open), so B10-13 (#594) moved the reading: the cathedral strand is gone and the realm strand reads 14 moves; the earlier log size (13,454 Events), the `flows_in` timing (0.011 s) and the 79 of 83 persons within an open strand were taken at the base and are `[UNREPRODUCED; re-read at CR-97's build]`; the figures below are the BASE reading and are kept as the record of what was measured: 13,454 Events; `flows_in` 0.011 s; 4 strands (rungs `r_valoria` 15 moves/22 referents, `duchy_hafenmark` 6/4, a barracks 3/2, the cathedral 2/5); 3 open; 79 of 83 persons within at least one open strand.
- REMAINING UNBUILT: columns (a) to (h), the spread print, the three controls, the test.
- GATE: `ED-IN-0352` and CR-104 landed. NEEDS: `ED-IN-0352`, CR-104.
- EXIT and FALSIFIER (planted logs and hand-built worlds, P9): (1) a planted log whose every strand has opening → turn → consequence act reads plot-point share 1.0, and the `shuffled_causes` arm on it reads lower; (2) a strand of petitions only reads 0 turns; (3) a planted strand ended by an actorless Event reads `threshold`, by an uncontested act `decider`, by a contested act `roll`; (4) in a planted world, swapping two seats' rungs swaps their (c)(i) rows; (5) the rename falsifier changes no row; (6) the emergence row on a planted realm reads exactly the holders of the head seats whose `influence_rung` is realm or duchy. MUTATION: read TURN from `open_referents` at the end instead of from the log and (2)'s variant with a restraint opened then closed reads 0 turns (red). CONTROL: `content_hash` and log length unchanged by the reading. EXPECTED: all pass; mutation red.
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: none new (D's `[ASSUMPTION]` lives in the code at the constant, with its revert).
- ASKS ATTACHED: none.
- RE-BASE: `strands_block` and `terminal_for` as B10-18 (CR-73) and B10-18c (CR-74) leave `harness/strife.py`; `arc.py` as B10-17b (CR-88 to CR-91's arc instrument) leaves it.
- FILES: `engine/season/harness/strife.py`, `engine/season/tests/test_strife_instrument.py` (the existing instrument test, extended).
- VERB CLUSTER: no.
- LAYER 1: none (a harness reader).
- N-LINE: the measurement — cut it and the gameplay experience is worse, because the strife guard sees narrowing and concentration of terminal codes and cannot see coherence (H-275 passed "for want of movement", `engine/season/hole_register.yaml:5471`), so neither plot-point legibility nor influence by office could be observed, and no later term could be shown to help.
- BUILDER: second tier; a third-tier (judgment) critic on the TURN and closure-class definitions.
- SOURCE: the folding session's collation (not kept in the tree: the handshake and its two coverage conditions); Jordan's T2 (ED-IN-0352).

````

### CR-98

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-98 | Declare the loops L1 to L5 as `kind: "LOOP"` rows with `sign:` and a bound (L6, L7 with CR-102, CR-105) | EDIT (register rows) | E | CR-97 | — | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:240-265`):

````
### CR-98 — Declare the loops as rows (IN) · BATCH B11-F2 · STATE EDIT (register rows; hash EQUAL) · R —
- STATUS: PROPOSED; the merge ratifies the position. HELD BACK: nothing (register rows; L6 and L7 land only with CR-102 and CR-105).
- WHAT: `kind: "LOOP"` rows in `engine/season/hole_register.yaml`, each with `sign:` and a bound in `default:` so G13's three clauses hold (the header at `:1425-1440`: a LOOP row carries `sign:` `+`/`-`; a non-loop row none; an amplifying loop names its bound). Transcribed from `proposals/2026-11-04-strife-flows/00_MASTER.md:177-182` (§6), reference only (§0.05: the rows describe code; the prose is their vocabulary):
  - L1 — path "stamp, attention, acts, moves, strand, stamp"; sign `+` ("persons who know of a strand act on it", `:179`); bound: `scene_budget` 5 (`engine/season/data/fixtures.py:228`), `ledger_cap` 3200 (`:247`; the stamp reads `flows_known`, the ledger), `question_aggregation_rule: first` (`:547`; H-102's note that it flattens rather than bounds, `hole_register.yaml:1447-1459`). CR-101's `flow_salience_gain` is recorded on this row as a gain, no new row.
  - L2 — path "grouping under the flow above, fewer distinct strands held, fewer stamps"; sign `-` (`:180`).
  - L3 — path "conclusion frees a slot, a new strand is held, a new stamp"; sign `-` (`:181`).
  - L4 — path "in-regime tellers credited more, their claims acted on, more moves, more told"; sign `+`, "the strongest" (`:182`); its condition "present only once S5 exists" is met (B11-S5 CLOSED, `workplans/valoria_master_workplan_v11_part3.md:66`); bound: `_credit`'s clamp to `[0, max(confidence_default, the uncredited value)]` (`loop/witness.py:240`, H-275), `ledger_cap`, `scene_budget`.
  - L5 (lands with CR-100, not before; replaces the draft's Ob loop) — the WITHIN-STAMP loop, CR-100: "within-stamp, choices on stake referents, moves, strand, within-stamp"; sign `+`; bound: `flow_capacity` through `presented` (a grouped strand stamps nothing), `scene_budget` 5 (a person acts at most five scenes a season, `fixtures.py:228`), `question_aggregation_rule: first` with `_stamped`'s one-stamp-per-question (`queries/world_q.py:3769`; the stamp rides `out[0]` only), `FLOW_STAKE_CLASSES` (only rows declaring Rung, Person or Office form on a stamped id), and conclusion (`_concluded`, `:5090-5097`: a concluded strand stamps nothing). ⚠ STATED: `ledger_cap` and claim decay do NOT bound L5, which reads the log, not a ledger; a strand's referent set only grows until it concludes; the number of strands stamped is bounded by `flow_capacity` through `presented`, the size of each strand's referent set by conclusion, and conclusion waits on docket closure (H-254). CR-97 (g) measures the size.
  - L6 — only if CR-102 is built: "office act, wider within-reach or salience, choices on stakes, moves, strand"; sign `+`; bound: L5's.
  - L7 — only if CR-105 is built: "within-stake, choice score, acts on stakes, moves, strand, within-stake"; sign `+`; bound: `scene_budget`, `_sample_order`'s draw over the ranked candidates (`decision/choose.py:322`, called at `:574`; the score orders, it does not force a pick), conclusion.
  - Reason: ID-16 (`architecture/meta/01_AXIOMS.md:616-619`) asks every feedback path declared with a direction before a further amplifier lands; L1 to L4 are table rows in prose today, and the register's five LOOP rows are H-102, H-103, H-104, H-112, H-235 (`hole_register.yaml:1508`).
- LANDED ALREADY: the five LOOP rows; G13 (`harness/register.py:100-140`); the derived reading `python -m engine.season.harness.loops` (`hole_register.yaml:1508`: "amplifiers derived equal declared").
- REMAINING UNBUILT: rows L1 to L5 (L6, L7 with their positions).
- GATE: CR-97 landed (each row's `cite:` quotes CR-97's first reading as the unmeasured-sign baseline). NEEDS: CR-97.
- EXIT and FALSIFIER: `python -m engine.season.harness.register --check` passes G13 on the new rows; the falsifier: a planted copy of one row with `sign:` removed (or an amplifying row with `default: "none"`) fails G13 (red, the gate can see it); and `python -m engine.season.harness.loops` still exits 0 and prints its declared-against-derived comparison with the new rows: EXPECTED either "amplifiers derived equal declared" or a named disagreement, which the commit records (L1 to L5 pass through steps whose read tables the derivation hand-writes, so a disagreement is a finding about the derivation, not a reason to drop a row).
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: the LOOP rows themselves (next free H ids).
- ASKS ATTACHED: none.
- RE-BASE: the register as the batch finds it (other batches add rows).
- FILES: `engine/season/hole_register.yaml`, `engine/season/harness/loops.py` (`DECLARED_CYCLES`, `:172-181`, gains one key per row, or the row is recorded unmapped with the reason: a row absent there reads `unmapped` and `equal` is false, `engine/season/tests/test_loops_instrument.py:48-51`).
- VERB CLUSTER: no.
- LAYER 1: `01_AXIOMS.md:616-619` (ID-16) is satisfied, not edited; no hunk.
- N-LINE: the loop rows — cut them and the gameplay experience is worse, because ID-16 requires every feedback path declared with a sign before a further amplifier, and L1 to L4 exist only as a prose table, so CR-100 and CR-101 would add amplifiers to undeclared loops.
- BUILDER: second tier.
- SOURCE: `00_MASTER.md` §6 (`:175-184`).

````

### CR-99

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-99 | Give the strife guard a positive control: a function over arms returning PASS, FAIL or BLIND, with a planted concentrator | BUILD (harness) | E | CR-98 | — | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:266-283`):

````
### CR-99 — Give the strife guard a positive control (IN) · BATCH B11-F2 · STATE BUILD (harness and test; hash EQUAL) · R —
- STATUS: PROPOSED; the merge ratifies the position. HELD BACK: nothing (a harness function and its planted tests).
- WHAT: make the strife guard (`00_MASTER.md:184`; head §7's definition, `workplans/valoria_master_workplan_v11.md:162`) a function over arms: given per-seed terminal-code histograms for an off arm and an on arm, it returns pass/fail with the two clauses (every code reached off is reached on; no code's share rises by more than the off arm's seed-to-seed spread) and the off-arm count of distinct codes (so a blind guard, fewer than two codes, reports BLIND rather than pass: head §6 risk 8, `:143`). A test plants a forced concentrator (an on arm whose histogram puts every terminal move on one code) and asserts FAIL; a second plants an off arm with one code and asserts BLIND.
- LANDED ALREADY: the guard as a reading quoted in commits (V2), run by hand in CR-78 and CR-79; it has no positive control (H-275 passed "for want of movement", `hole_register.yaml:5471`).
- REMAINING UNBUILT: the function; its two planted tests.
- GATE: CR-98 landed. NEEDS: CR-98.
- EXIT and FALSIFIER: the planted concentrator reads FAIL; the one-code off arm reads BLIND; two identical arms read PASS. MUTATION: drop the share clause and the concentrator reads PASS (red). EXPECTED: as stated. The guard is still a reading at batch closes (head §7: "never a test that asserts a count" on the realm); only the planted arms are asserted.
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: none.
- RE-BASE: `harness/strife.py` as CR-97 leaves it.
- FILES: `engine/season/harness/strife.py`, `engine/season/tests/test_strife_instrument.py`.
- VERB CLUSTER: no.
- LAYER 1: none (a harness reader).
- N-LINE: the guard control — cut it and the gameplay experience is worse, because a guard that has never been seen to fail passed CR-79 for want of movement, so a concentrator added by CR-100 could pass unseen and harden L1 or L5 into a determinant.
- BUILDER: second tier.
- SOURCE: `00_MASTER.md:184`; head §6 risk 8.

````

### CR-100

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-100 | The unaware's field: `world_q.flow_stakes_within` spliced into `questions_for` through the driver's barrier-2 projection, behind `Fixtures stamp_flow_within`, shipped off | BUILD | E (off); M (on) | CR-97, CR-98, CR-99 | — | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:284-312`):

````
### CR-100 — The unaware's field: the within-stamp in `questions_for` (IN) · BATCH B11-F2 · STATE BUILD (a query term, one driver line, a fixture shipped off; hash EQUAL off, a declared mover on) · R —
- STATUS: PROPOSED; the merge ratifies the position, shipped OFF. Whether it ships ON is CR-103's decision rule, not the merge's.
- WHAT: a world-side splice in `questions_for` (`queries/world_q.py:3964`; World-first, resolver-side, so lawful with no AX-2 hunk) that appends, for a person WITHIN an open strand, the strand's referents at stake, whether or not his ledger holds any move of it (R9, `00_MASTER.md:55`: "Awareness is not required to be within a flow"). Precisely:
  - `world_q.flow_stakes_within(w, p, flows, classes=FLOW_STAKE_CLASSES) -> tuple`: for each strand PRESENTED (`presented(w, flows)`, the slots A1/A2 bound to `flow_capacity`, `:5200-5233`) at a rung in the ancestry of `p`'s home (the person limb of `within`, `:5236-5247`, extracted to a one-line predicate that `within` then calls), plus the open era's realm-rung strands, and not `concluded(w, s)` (`:5100-5102`); a strand grouped under the flow above stamps nothing (L2's damping reaches L5 by construction); the stamped strands' referents and parties sorted by id, never `p` himself, through `_of_stamped_class(w, ..., classes)` (`:3672`). Its loop body is SHARED with `flow_stakes` (`:5457-5489`) through one private helper both call (strands, a concluded test, `p`, classes); no second copy.
  - The splice: `questions_for` gains an optional parameter `flows: Optional[Flows] = None`; the `added =` expression (`:4194-4200`) gains, after `flow_stakes`, `+ (flow_stakes_within(w, p, flows) if flows is not None else ())`. `_stamped`'s dedup keeps an id carried by both stamps once.
  - HOW THE WORLD READING IS READ AT A BARRIER: `loop/driver.py::_questions_at_barrier` (`:377-385`), the barrier-2 projection the driver builds once per round for every person (04 PART D row 41), computes `flows = world_q.flows_in(w) if w.fixtures.get("stamp_flow_within") else None` once and passes it to every `questions_for` call. The driver owns barrier lifetimes (`04_CODE_ARCHITECTURE.md:172`), the World is frozen at that point (`loop/driver.py:494-495`), and the reading is a local dropped with the call (T-a). `queries/cache.py` is NOT used: it holds presence, tenure and home indexes only (`queries/cache.py:72-130`), the projection has one caller, and `world_q` cannot import `cache` (which imports `world_q`, `:68`) without a cycle.
  - TERMINAL TEST: `flows_in(w)` with its default, the kind-level `default_terminal` (`:5061-5065`), exactly as CR-78's stamp reads the kind-level `concludes` set (`:5462`). The code-level test (`harness/strife.py::terminal_for`, `:221-233`) reads `strife_moves.yaml` signatures through the harness and may not be imported by the loop; moving it to a roster-side home is CR-78's named precondition (`workplans/valoria_master_workplan_v11_part3.md:62`) and is not required here (ladder step 4, CR-78's precedent). Status: PARTIAL, accepted; CR-97 (g) measures the strands the two tests disagree on.
  - COST: `flows_in` read 0.011 s on a one-season `build_realm(0)` log of 13,454 Events (CR-97's BASE reading at `d87946a`, `[UNREPRODUCED]`; HEAD prints 3 strands; CR-97's LANDED ALREADY); once per round, five rounds a season (`scene_budget` 5, `scenes_per_round` 1).
  - Fixture `stamp_flow_within`, shipped `False` (pattern: `stamp_flow_stakes`, `engine/season/data/fixtures.py:1003-1010`). Sign: none to decide (the stamp widens a field; it weights nothing).
  - It applies identically to every person (ID-17, `architecture/meta/01_AXIOMS.md:703-717`): the only inputs are containment, the log and the closed class set.
- LANDED ALREADY:
  - The stamp `flow_stakes` iterates `flows_known` (`:5485`), the person's own ledger, so a person who holds no `opens` claim gets `()` (`:5476-5477`): no channel reaches the unaware today.
  - `flows_in` has no loop caller (callers outside tests: `harness/strife.py:392` only; grep 2026-11-08).
  - Dose of the existing stamp: 6 to 13 persons ever stamped (H-274, `hole_register.yaml:5449-5460`). CR-97's BASE reading (`d87946a`, `[UNREPRODUCED]`): 79 of 83 persons are within an open strand after one season (a realm-rung strand covers everyone).
  - Precedent for a fixture-gated splice term with a revert helper: CR-78 (`revert_cr78`, `engine/season/tests/test_strife_flows.py:106`).
- REMAINING UNBUILT: `flow_stakes_within`, the shared helper, the `within` extraction, the `questions_for` parameter and term, the driver line, the fixture, the hole row, the test and its `revert_cr100` helper.
- GATE: CR-97, CR-98 (L5's row), CR-99 landed. NEEDS: CR-97, CR-98, CR-99.
- EXIT and FALSIFIER (hand-built worlds, P9): (1) two persons at one settlement under an open strand's rung, one with an empty ledger and one who witnessed every move, receive the same within-stamped referents; (2) a person outside the strand's rung receives none; (3) a concluded strand stamps nothing; (4) `questions_for(w, p)` with `flows=None` is byte-identical to today's output; (5) the rename falsifier. MUTATION: read `flows_known` instead of `flows.strands` and (1)'s empty-ledger person receives none (red). CONTROLS: fixture off reproduces the pre-change one-season hashes at seeds 0, 1, 2 (EQUAL); a shuffled-flow arm (the same number of referents drawn at random from the strands' rung subtree, seeded) for CR-103. EXPECTED: all pass; mutation red. Execution artifact: the test file, and the commit body's one-season after-readings.
- HASH MOVERS: on, a mover of every season in which a strand is open: one-season `build_realm(0)` seeds 0, 1, 2 (P14; pre-change readings the previous item's recorded after-readings). It SHIPS OFF in this position; whether it ships on, and at what reach, is CR-103's decision. `build_realm(0).content_hash()` EQUAL (Fixtures is not hashed).
- HOLES AND LEDGER IDS: one `hole_register.yaml` row, kind `RULING`, grade `assumption`, `sweep: ["False (control, the revert)", "True"]` (H-274's shape); `revert_cr100` in `engine/season/tests/test_strife_flows.py` (idiom: `revert_cr78` `:106`, `revert_cr79` in `test_strife_credit.py:88`).
- ASKS ATTACHED: none.
- RE-BASE: `questions_for`'s `added =` expression as B10-18b and B10-18c leave it (head §4's re-base note, `workplans/valoria_master_workplan_v11.md:112`); `_questions_at_barrier` as it stands at build.
- FILES: `engine/season/queries/world_q.py`, `engine/season/loop/driver.py`, `engine/season/data/fixtures.py`, `engine/season/hole_register.yaml`, `engine/season/tests/test_strife_flows.py`.
- VERB CLUSTER: no (no `verb_table.yaml`, count or set pin, or `loop/effects_*.py`).
- LAYER 1: `04_CODE_ARCHITECTURE.md:168` (`queries/world_q` reads any store via World), `:171` (`decision/` receives `Question[]` and nothing new), `:172` (`loop/driver` owns the caches' lifetimes and builds the barrier-2 projection); no hunk.
- N-LINE: the within-stamp — cut it and the gameplay experience is worse, because a character who has not heard of the rising in his own duchy chooses exactly as if it did not exist, so era, regime and strife condition only the handful who already know (6 to 13 persons, H-274) and the world's drama never reaches the people living inside it.
- BUILDER: second tier; a third-tier (judgment) critic on the dose against L5's bound.
- SOURCE: `00_MASTER.md` §5 (R9, `within`); Jordan's K2 and the correction of 2026-11-08.

````

### CR-101

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-101 | The field's order: a flow-salience bump inside `attention_key`'s tiers, `Fixtures flow_salience_gain`, shipped 0 | BUILD | E (at 0); M (above 0) | CR-98, CR-99, CR-100 | — | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:313-331`):

````
### CR-101 — The field's order: flow salience in `attention_key` (IN) · BATCH B11-F2 · STATE BUILD (a sort-key term and a fixture shipped 0; hash EQUAL at 0) · R —
- STATUS: PROPOSED; the merge ratifies the position, shipped at gain 0. The value it ships at is CR-103's decision rule, not the merge's.
- WHAT: in `attention_key` (`queries/world_q.py:3790`), a salience bump for a question whose referent is at stake for `p`, in either stamp: `flow_stakes(w, p)` (his own ledger) or `flow_stakes_within(w, p, flows)` (CR-100). `questions_for` computes both once and passes the union to `attention_key` (it already passes `ambs` and `refs_of`, `:4133`), so nothing is computed twice. Fixture `flow_salience_gain`, shipped 0. The bump enters the key's salience slot of tiers 0, 2 and 3, inside the tier (the existing "never across tiers" rule, `:3817-3826`, stays), so a stake orders questions inside a tier and cannot lift a stranger's matter over a person's own ambition; this widens IN-69's rule that tiers 1 and 4 carry 0 (`:3825`) to tier 2 only, named at the site, and a stake on a tier-4 own-act echo stays tier 4 `[ASSUMPTION; medium; Jordan to correct; revert: tiers 0 and 3 only, which leaves the term inert for a stake that is neither an ambition referent nor the need question]`. Recorded as a gain on L1 (own-ledger stakes) and on L5 (within stakes).
- ⚠ STATED: `attention_key`'s docstring says it reads "ONLY THE QUESTION AND `p`'S OWN STATE … Never the log" (`:3834-3838`). The within half reads the log through the driver's `flows`. That is lawful (`world_q` reads any store, `04:168`; `decision/` still receives only the sorted `Question[]`) but it falsifies the docstring, which this position corrects at the site in the same commit.
- LANDED ALREADY: `attention_key`'s five tiers and salience slot (IN-57, IN-69); the own-act screen (tier 4, `:3813-3815`) damps echo only.
- REMAINING UNBUILT: the term, the fixture, the docstring correction, the hole row, the test, `revert_cr101`.
- GATE: CR-100 landed. NEEDS: CR-98, CR-99, CR-100.
- EXIT and FALSIFIER: (1) in a hand-built world, a tier-2 claim question whose referent is a within-stake sorts earlier at gain > 0 than at 0, and only inside its tier, while a second planted world whose only stake question is a tier-4 echo is byte-identical at any gain; (2) a person with no stake in either stamp is byte-identical at any gain; (3) a tier-1 question is never displaced by a tier-0 stake bump. MUTATION: apply the bump across tiers and (3) reads red. CONTROLS: gain 0 EQUAL at seeds 0, 1, 2; the shuffled-flow arm (CR-100's) for CR-103. EXPECTED: all pass; mutation red.
- HASH MOVERS: at a nonzero gain, a mover wherever a stamped referent is a question's referent: one-season seeds 0, 1, 2 (P14). Ships 0 here; CR-103 selects the value.
- HOLES AND LEDGER IDS: one `hole_register.yaml` row (kind `NUMBER`, grade `assumption`, `sweep` 0 / the CR-103 grid); `revert_cr101` in `engine/season/tests/test_in57_attention_tiers.py`.
- ASKS ATTACHED: none.
- RE-BASE: `attention_key`'s tiers as B10-13 (CR-34) and B10-14 (CR-29) leave `world_q.py`.
- FILES: `engine/season/queries/world_q.py`, `engine/season/data/fixtures.py`, `engine/season/hole_register.yaml`, `engine/season/tests/test_in57_attention_tiers.py`.
- VERB CLUSTER: no.
- LAYER 1: `04_CODE_ARCHITECTURE.md:168`, `:171`; no hunk (AX-2 untouched: the order of a person's questions is produced resolver-side; T-f, `01_AXIOMS.md:417`, holds).
- N-LINE: the salience bump — cut it and the gameplay experience is worse, because a stake handed to a person sorts behind every unrelated question in its tier, so with `question_aggregation_rule: first` he is told what is at stake and answers something else.
- BUILDER: second tier.
- SOURCE: `00_MASTER.md` §6 L1 ("stamp, attention, acts"); Jordan's K1.

````

### CR-102

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-102 | Office influence on the within-stake: a salience term `flow_office_gain × r`, `r` from `influence_rung`'s kind; shipped 0 | CONDITIONAL: BUILD only if its gate holds on CR-97's reading, else NOT BUILT | E (at 0); M (above 0) | CR-97, CR-100, CR-101, CR-104 | D6 (answered by precedent, revert stated) | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:332-350`):

````
### CR-102 — Office influence on the within-stake (IN) · CONDITIONAL · BATCH B11-F2 (last item) · STATE BUILD if its gate holds, else recorded NOT BUILT (hash EQUAL at 0, a declared mover above 0) · R —
- STATUS: PROPOSED, CONDITIONAL; the merge ratifies the position and its gate. It is built only if its gate holds on CR-97's reading, else recorded NOT BUILT.
- WHAT: a salience term added to CR-101's: a within- or own-stake referent belonging to a strand that holds a move exercised through an office (`causing_act(w, e).via`, read per move by `flow_stakes_within`'s caller from `flows`, since `Move` carries no seat, `queries/world_q.py:4836-4847`) gains `flow_office_gain × r`, where `r = RUNG_KINDS.index(kind) + 1` for `faction_q.influence_rung(w, via)`'s kind (realm highest; `flow_capacity` is `len − index` and is NOT reused for `r`; CR-104's one-line helper, D6), the highest such over the strand's moves. Fixture `flow_office_gain`, shipped 0, `[ASSUMPTION; medium; Jordan to correct; revert: gain 0]`. Not a weight in `flows_in`, `slot_rank` (`:5193-5197`, a presentation ranking read by `presented`, `:5216`, `:5224`) or the era (`_eras`, `:5166-5185`, a scope). Not a change to who is deposited what (the witness channels are unmodified): the draft's dissemination route is dropped by Jordan's correction (choices, not channels), and CR-97 (e) measures dissemination as it stands.
- FORBIDDEN: as §3.1's rule, and specifically: no literal or lookup on an office, faction, post, body or person id; the faction enters only through `influence_rung`'s structural derivation (§3.1's rename falsifier).
- LANDED ALREADY: `rank` returns 0 and is dormant (`decision/options.py:1685-1696`, H-181 `hole_register.yaml:4154`, `rank_gain` 0.5 `fixtures.py:903`, H-178 `:4076`): a hearer-relative quantity inside AX-2's island, not office influence; untouched.
- REMAINING UNBUILT: the term, the fixture, the hole row, the test, `revert_cr102`.
- GATE (computable from CR-97's three-seed OFF reading, taken in this batch): let `T_k` be the share of strand moves exercised through an office of influence kind k that are TURNS, `C_k` the share that start a consequence chain of depth ≥ D, and `T_m`, `C_m` the same for the matched-holder control; BUILT only if, for k ∈ {realm, duchy}, both `T_k − T_m` and `C_k − C_m` are at most the larger of their two arms' seed spreads (no influence gradient exists without it). Otherwise recorded as NOT BUILT, with the four numbers. NEEDS: CR-97, CR-100, CR-101, CR-104.
- EXIT and FALSIFIER: (1) in a planted world, swap two offices' rungs and the term follows the offices; (1b) a realm-kind office's term exceeds a territory-kind office's; (2) the rename falsifier; (3) a strand whose moves carry no `via` gains nothing; (4) gain 0 EQUAL. MUTATION: read the doer's own home rung instead of `influence_rung` and (1) reads red. EXPECTED: all pass.
- HASH MOVERS: at a nonzero gain, one-season seeds 0, 1, 2 (P14).
- HOLES AND LEDGER IDS: one `hole_register.yaml` row (kind `NUMBER`, grade `assumption`); L6 in CR-98's block; `revert_cr102` in `engine/season/tests/test_in57_attention_tiers.py`.
- ASKS ATTACHED: D6 (answered by precedent; carries `[ASSUMPTION; medium; Jordan to correct; revert: gain 0]`).
- RE-BASE: CR-101's term and CR-104's function as built.
- FILES: `engine/season/queries/world_q.py`, `engine/season/data/fixtures.py`, `engine/season/hole_register.yaml`, `engine/season/tests/test_in57_attention_tiers.py`.
- VERB CLUSTER: no.
- LAYER 1: `04_CODE_ARCHITECTURE.md:168`, `:171`; no hunk.
- N-LINE: the office term — cut it and the gameplay experience is worse, because a strand moved by the Confessor or the King would press on people's choices no harder than a quarrel between two smallholders, so the big four's deeds would not shape what the realm attends to; built only if CR-97 shows their deeds do not already shape strands more than matched commoners'.
- BUILDER: second tier; a third-tier (judgment) critic on the gate's verdict.
- SOURCE: Jordan's D7 ruling; D6.

````

### CR-103

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-103 | Evaluate the field route: arms OFF, FIELD, FIELD+S on a salience grid, SHUFFLED and (if CR-102 is built) FIELD+S+O, three seasons, seeds 0, 1, 2, under a decision rule with QUANTISATION and WIDE-SPREAD clauses fixed in advance | MEASURE (readings; the selected values shipped in its pin commit) | M (the shipped arm, if any) | CR-97, CR-99, CR-100, CR-101, CR-102 (if built), B10-17, B10-18, B10-18c | — | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:351-369`):

````
### CR-103 — Evaluate the field route (IN) · BATCH B11-F3 (after B10-18c; first item) · STATE MEASURE (readings; the selected values shipped in its pin commit) · R —
- STATUS: PROPOSED; the merge ratifies the position and its decision rule, fixed before the run. HELD BACK: nothing; which arm ships is the rule's output, not the merge's.
- WHAT: run CR-97's reading and CR-99's guard over arms, three seasons (strife: P10's exception; four only where the off arm is BLIND, risk 8), seeds 0, 1, 2 (P10: the arms declare movers), one process per seed and arm, `PYTHONHASHSEED=0`. Arms: OFF (all of `stamp_flow_within` False, `flow_salience_gain` 0, `flow_office_gain` 0); FIELD (`stamp_flow_within` True, salience 0); FIELD+S at each salience on the grid {0.25, 0.5, 1.0} `[ASSUMPTION; medium; Jordan to correct; revert: grid {0.5}]`; SHUFFLED (CR-100's shuffled-flow arm, salience at the best FIELD+S value); and, if CR-102 is built, FIELD+S+O at `flow_office_gain` on the same grid. It tests T1 (without a bias, events will not cohere at both depth and breadth) on the decisions-only route.
- DECISION RULE (fixed before the run). For arm A and number X, `X̄_A` is its mean over seeds 0, 1, 2 and `s_A(X)` its spread (max − min). The two coverage numbers are `P` = CR-97 (a)'s plot-point share (depth: strand → chain) and `Q` = CR-97 (b)'s share of depth-≥D chains inside strands (breadth: chain → strand). An arm A LIFTS when `P̄_A − P̄_OFF > s_OFF(P)` AND `Q̄_A − Q̄_OFF > s_OFF(Q)` AND `P̄_A − P̄_SHUFFLED > s_SHUFFLED(P)` (the lift is the flow's, not any extra stamp's). An arm A is SAFE when CR-99's guard PASSES A against OFF over the three seeds. Selection: among arms that LIFT and are SAFE, ship the one with the smallest largest-code share of terminal codes; ties to the smaller gains. If none lifts: ship everything OFF and 0, and CR-105's gate opens. QUANTISATION CLAUSE: P and Q move in steps of 1/N for N strands; if `s_OFF(P) ≥ 1 − P̄_OFF` or `s_OFF(Q) ≥ 1 − Q̄_OFF` the LIFT clause cannot be met and the reading is INCONCLUSIVE for that number, stated as such; CR-100 to CR-102 are then not shipped on, and CR-105's gate stays CLOSED, until a longer or wider reading that Jordan calls. WIDE-SPREAD CLAUSE: if `s_OFF(P)` or `s_OFF(Q)` exceeds half of `P̄_OFF` or `Q̄_OFF` respectively, or the guard is BLIND at four seasons, the reading is INCONCLUSIVE at the permitted seed set: ship OFF and 0, CR-105's gate stays CLOSED (an inconclusive field reading is not evidence the field failed), and the commit names the spread; more seeds are a P10 reading only Jordan calls, so the route is stated, not parked.
- LANDED ALREADY: none of the arms; the instruments (CR-97, CR-99) are this plan's.
- REMAINING UNBUILT: the readings; the pin commit if an arm ships.
- GATE: the supply gates that make strands able to conclude and every category able to open, so a coherence reading is not vacuous: B10-17 closed (`at_war` false in every buildable world until it, head §4 `workplans/valoria_master_workplan_v11.md:112`, the casus-belli carrier ED-IN-0317 (a)); B10-18 closed (CR-73's SH reading after CL-EVENTS (2)); B10-18c closed (docket closure, H-254; CR-74's CH signature). CR-100 to CR-102 may be built before these; they cannot be evaluated until they land. NEEDS: CR-97, CR-99, CR-100, CR-101, CR-102 (if built), B10-17, B10-18, B10-18c.
- EXIT and FALSIFIER: the falsifier of T1 on this route: OFF already meets both lift thresholds against SHUFFLED, or FIELD+S meets none against OFF. The commit body carries every arm's per-seed numbers, means and spreads, the guard's verdicts, and which clause selected the shipped arm. Execution artifact: the readings in the commit body (V2) and the pin commit. EXPECTED: not predicted (that is the point of fixing the rule first).
- HASH MOVERS: the shipped arm, if any: one-season seeds 0, 1, 2 and the three-season strife reading (P14; pre-change = CR-102's or CR-101's recorded after-reading); shared pins re-recorded in the batch's pin commit (P15), stated plainly as a golden re-record.
- HOLES AND LEDGER IDS: the `cite:` of CR-100's, CR-101's (and CR-102's) hole rows gains the readings; their `default:` the shipped value.
- ASKS ATTACHED: none (every branch of the rule is decided in advance).
- RE-BASE: the arms re-read on the tree after B10-18c (V1); CR-97's columns re-checked against any Event kind those batches add.
- FILES: `engine/season/hole_register.yaml`, `engine/season/data/fixtures.py` (only if an arm ships), and the pin files the shipped arm moves.
- VERB CLUSTER: no.
- LAYER 1: none.
- N-LINE: the evaluation — cut it and the gameplay experience is worse, because without a rule fixed in advance the field terms would ship on judgment, and Jordan's thesis that coherence needs a bias would be neither confirmed nor refuted.
- BUILDER: second tier; an independent third-tier (judgment) critic judges the selected arm (the builder line for a selected arm at `workplans/valoria_master_workplan_v11_part4.md:98`).
- SOURCE: Jordan's T1; `00_MASTER.md:184` (the guard).

````

### CR-105

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-105 | A choice-score bias toward what is at stake: one term in `decision/choose.py::score_terms` on `Question.stakes`, `flow_choice_gain` shipped 0 | CONDITIONAL and HELD (on CR-103 shipping OFF under "none lifts", and Jordan's AX-2 hunk, HELD BACK) · BUILD when released | E (at 0); M (above 0) | CR-103, the AX-2 hunk | the hunk's text (Jordan's file; a sentence proposed in the entry) | written out in full: `-11` §3 |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:370-388`):

````
### CR-105 — A choice-score bias toward what is at stake (IN) · CONDITIONAL · BATCH B11-F3 (after CR-103) · STATE HELD until CR-103's verdict and Jordan's hunk, then BUILD (a score term and a fixture shipped 0) · R —
- STATUS: RATIFIED, CONDITIONAL: built only if CR-103 ships OFF under "none lifts" and the AX-2 hunk (item 1 above, ratified as wording, applied at the gate) is in Jordan's file. Ratification adds no build.
- WHAT: in `decision/choose.py::score_terms` (`:193`, the one owner of the score's terms; `score` sums them, `:556-559`), one term: a candidate whose subject is a referent at stake in a flow the person is within (CR-100's within-stamp, or his own `flow_stakes`) gains `flow_choice_gain`, shipped 0. `choose` still receives no World (T-f, `01_AXIOMS.md:417`): the stake set reaches it on the `Question` it already receives, as a new field (`Question.stakes`, a frozenset filled by `_stamped` from the two stamp terms; `state/carriers.py:513`), not as a class (a referent class would make rows form on it). Uniform: the predicate is "subject ∈ stakes", never a verb, move code, side, faction, seat id or person. Direction: toward engaging what is at stake, so there is no sign decision.
- WHY A HUNK: AX-2 (`architecture/meta/01_AXIOMS.md:106`): "A person decides from what they hold … There is no view of world truth" inside a decision. A within-stake is world truth (the log's strands, read for a person who may know none of them), so a score term on it breaches AX-2 as worded. Jordan waived AX-2 under the split (W1); the hunk is Jordan-directed, one sentence at AX-2 naming the waiver and its bound (a structural stake predicate, one fixture, a gain), in the style of H-L0-11 (2026-11-07, the governors line of `01_AXIOMS.md`, B11-S5's record `workplans/valoria_master_workplan_v11_part3.md:66`).
- LANDED ALREADY: `score_terms` (IN-62); `Question.classes` (the stamp's carrier).
- REMAINING UNBUILT: the hunk (Jordan's), `Question.stakes`, the term, the fixture, the hole row, the test, `revert_cr105`, L7's row.
- GATE: CR-103 shipped OFF under "none lifts" (NOT under the wide-spread clause), and Jordan has applied the hunk. Otherwise recorded NOT BUILT. NEEDS: CR-103, the hunk.
- EXIT and FALSIFIER: (1) two hand-built persons with equal pursuits, one whose question carries a stake on a candidate's subject, rank that candidate higher at gain > 0 and alike at 0; (2) a candidate keyed by verb with the same subject not at stake gains nothing; (3) `choose` takes no World (the existing AX-2 path scan over `decision/` stays green); (4) gain 0 EQUAL. MUTATION: key the term on the verb and (2) reads red. Then the CR-103 rule re-run with this arm added (same seeds, horizon and clauses). EXPECTED: (1) to (4) pass; the re-run not predicted.
- HASH MOVERS: at a nonzero gain, one-season seeds 0, 1, 2 (P14).
- HOLES AND LEDGER IDS: one `hole_register.yaml` row (kind `NUMBER`, grade `assumption`); L7.
- ASKS ATTACHED: the hunk's text, Jordan's (a hunk to a Layer 1 file is his; the plan supplies a sentence for him to apply or correct, `[ASSUMPTION; medium; Jordan to correct]`: *"A world-side mechanism may add to the field and the score of a decision a bias derived from flows the person is within but does not hold; the bias is a weight on candidates whose subject is at stake and never a belief, a claim or an outcome, and the person still chooses from what he holds."*).
- RE-BASE: `score_terms` and `Question` as B10-13 and B10-18c leave them.
- FILES: `decision/choose.py`, `state/carriers.py` (`Question.stakes`), `queries/world_q.py` (`_stamped` fills it), `data/fixtures.py`, `hole_register.yaml` (all under `engine/season/`), `engine/season/tests/test_cr17_odds_weighting.py` (the existing score-term test's idiom) or a new `engine/season/tests/test_cr105_choice_stakes.py`; and `architecture/meta/01_AXIOMS.md` (Jordan's hunk).
- VERB CLUSTER: no.
- LAYER 1: `01_AXIOMS.md:106` (AX-2), HUNK REQUIRED, Jordan-directed.
- N-LINE: the choice bias — cut it and, if the field route has been measured not to lift coherence, the gameplay experience is worse, because people handed what is at stake still choose as if it were not, and Jordan's split (the world conditions the choices, the person chooses from what he knows) has no second lever.
- BUILDER: third tier (judgment) for the term and its gate reading.
- SOURCE: Jordan's W1 waiver and the correction of 2026-11-08 (*"bias decisions and choices"*).

````

### GO-09

card row (`valoria_master_workplan_v11_part3.md`):

```
| GO-09 | The season registries export (port gate): `tools/export_season_registries.py` (`--build`/`--check`) writes every file `data/files.py` names that the loader reads, plus `DEFAULT_FIXTURES`, to `engine/engine_params/season_registries.json`; blocking in CI | BUILD | E | — | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:23-34`):

````
### GO-09 — The season registries export (GO/IN) · BATCH B10-20 (first) · STATE BUILD · R —
- WHAT: the port must read the same registries the season loop loads, as data, behind a round-trip check.
- LANDED ALREADY: `engine/season/data/files.py` and the loader.
- REMAINING UNBUILT: `tools/export_season_registries.py` (`--build`/`--check`): every file `engine/season/data/files.py` names that the loader reads, parsed and written losslessly to `engine/engine_params/season_registries.json`, plus `DEFAULT_FIXTURES`; blocking in CI's validators job.
- GATE: B10-20's entry. NEEDS: none.
- EXIT and FALSIFIER: deleting one key in the JSON reds `--check`; adding a row to `verb_table.yaml` without a re-export reds it. CONTROL: the loader run over the JSON (a test-only path) yields tables equal to the loader run over the YAML.
- HASH MOVERS: EQUAL.
- HOLES AND LEDGER IDS: none. ASKS ATTACHED: none.
- RE-BASE: re-read `data/files.py`'s file list by symbol.
- BUILDER: second tier.
- SOURCE: the port gate.

````

### GO-10

card row (`valoria_master_workplan_v11_part3.md`):

```
| GO-10 | Refusal values as typed Results (port gate): the control-flow `except` sites that turn an exception into a game outcome return a typed `{code, needs, law}` record, `code` a closed roster; the §C.12 Result-shape hunk (Layer 1) lands with GO-10, in that PR, listed under 'Layer 0/1 hunks' (D-1 confirmed, ED-IN-0300; a (RULED) mark at the anchor stops that row) | BUILD | E | — | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:35-46`):

````
### GO-10 — Refusal values as typed Results (GO/IN) · BATCH B10-20 (second) · STATE BUILD · R —
- WHAT: the fold turns some exceptions into game outcomes; those outcomes cross to the port as values, so each such site returns a typed record instead. Defect raises stay halts.
- LANDED ALREADY: the refusal Events.
- REMAINING UNBUILT: the control-flow `except` sites that turn an exception into a game outcome (`loop/resolve.py:276`, `:502`, `:1137`; `loop/predicates.py:267`; re-derive by symbol) return a typed record `{code, needs, law}` whose `code` is a closed roster. The §C.12 Result-shape hunk (Layer 1, `04_CODE_ARCHITECTURE.md:993`) lands with GO-10 (B10-20), in that PR, listed under "Layer 0/1 hunks" (independently revertible; M11 answered (a), ED-IN-0300); a (RULED) mark at its anchor stops the hunk, and the code proceeds without it.
- GATE: B10-20, after GO-09. NEEDS: none.
- EXIT and FALSIFIER: a planted no-op write still yields its refusal Event; `grep` finds no `except NoOpReceipt` left on the fold. CONTROL: seeds 0-2, four seasons, realm hash equal before and after.
- HASH MOVERS: EQUAL.
- HOLES AND LEDGER IDS: none. ASKS ATTACHED: M11 ANSWERED (a), for the §C.12 hunk only (`-05`; ED-IN-0300).
- RE-BASE: re-derive the `except` sites by symbol.
- BUILDER: third tier (judgment).
- SOURCE: the port gate; `04_CODE_ARCHITECTURE.md` §C.12.

````

### GO-11

card row (`valoria_master_workplan_v11_part3.md`):

```
| GO-11 | `module_contracts.yaml` re-derived from code (port gate): `wiring:` (`key-log` replaced), `engine_clock`'s `[ASSUMPTION]` state row, `sim_module:` for `social_contest` and `mass_battle`, `golden_path:`; `accounting_sequence:` deleted if no reader | EDIT | E | —; not a dependency: GO-14 (the `golden_path:` edit is GO-11's and does not need the deletion) | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:47-59`):

````
### GO-11 — `module_contracts.yaml` re-derived from code (GO/IN) · BATCH B10-20 (third) · STATE EDIT · R —
- WHAT: `references/module_contracts.yaml` still carries retired wiring (`key-log`) and `[ASSUMPTION]` rows; re-derive every row from the code the composition reads.
- LANDED ALREADY: `tools/export_composition.py --check`.
- REMAINING UNBUILT: every row re-derived: `wiring:` (`build`, `godot`, `port_rank`, `parity`; `key-log` replaced by `state-hash` or `seam-io`), `engine_clock`'s `[ASSUMPTION]` state row, `sim_module:` for `social_contest` and `mass_battle` (ED-IN-0017 F9, F10), the `golden_path:` edit; `accounting_sequence:` deleted if `grep` finds no reader.
- GATE: B10-20, after GO-10. NEEDS: none. It does not need GO-14 (order only, not a dependency): this position's `golden_path:` edit does not need the skeleton deletion.
- AFTER B10-03 (GO-14 landed): the `combat` row's `godot_home` is gone and its `wiring.godot` reads `typed-exported`, but the row still carries claims about the deleted GDScript slice, which this position re-derives: `wiring.parity: key-log + typed-export round-trip` and `foundation_gaps.godot_spine.note` ("referenced by the skeleton"). (PC-16 corrected the `modules:` statuses and the `gap_notes`, `a02797ed`.) Check with `grep -n "key-log\|the skeleton" references/module_contracts.yaml`; `export_composition --check` cannot see a stale path or status (it checks vocabulary membership only).
- EXIT and FALSIFIER: `grep -c "key-log" references/module_contracts.yaml` prints 0 (a planted `key-log` row reddens the exit); `python tools/export_composition.py --check` OK. CONTROL: `composition.json` byte-equal.
- HASH MOVERS: EQUAL.
- HOLES AND LEDGER IDS: ED-IN-0017 F9, F10. ASKS ATTACHED: none.
- RE-BASE: re-read each row against the module it names.
- BUILDER: second tier.
- SOURCE: the port gate; `CLAUDE.md` §6.

````

### GO-12

card row (`valoria_master_workplan_v11_part3.md`):

```
| GO-12 | The seam port items (port gate): an explicit provider list; `rngsource.py`'s fallback to the process-global `random` refuses; provider `status` a closed roster; `registry.resolve` refuses a missing contract; `os.environ`-read module flags frozen into exported values | BUILD | E | GO-11 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:60-71`):

````
### GO-12 — The seam port items (GO/IN) · BATCH B10-20 (fourth) · STATE BUILD · R —
- WHAT: the seam still resolves some things the port cannot copy: an implicit provider set, a fallback to the process-global `random`, and module flags read from the environment.
- LANDED ALREADY: `engine/substrate/composition.py`; `registry.resolve`.
- REMAINING UNBUILT: an explicit provider list (ED-IN-0017 F2); `modules/mass_battle/rngsource.py`'s fallback to the process-global `random` refuses (F5), so every draw goes through a keyed generator; provider `status` a closed roster (F7); `registry.resolve` refuses a missing contract and the fields it reads are exported to `composition.json` (F8); `os.environ`-read module flags (`modules/mass_battle/config.py:113`, `hierarchy/units.py:33`) frozen into exported values.
- GATE: B10-20, after GO-11. NEEDS: GO-11.
- EXIT and FALSIFIER: a provider module not on the list reds driver construction; a `None` rng in `mass_battle` raises instead of drawing. CONTROL: the realm hash at seeds 0-2, four seasons, equal.
- HASH MOVERS: EQUAL.
- HOLES AND LEDGER IDS: ED-IN-0017 F2, F5, F7, F8. ASKS ATTACHED: none.
- RE-BASE: re-read `rngsource.py` and the flag reads by symbol.
- BUILDER: second tier producer; a third-tier (judgment) critic.
- SOURCE: the port gate.

````

### GO-01

card row (`valoria_master_workplan_v11_part3.md`):

```
| GO-01 | `26` GO-VERSION: the ruled engine version where code reads it (released whole; the tenth attribute's name returned to Jordan, J-T2, now answered by `ED-IN-0328`; GO-01 never waited on it) | BUILD: `references/engine_series.yaml` holds `engine_series: "4.7"` (a comment citing ED-GO-0002), read by `tools/export_game_constants.py` (the exporter owns no value) and emitted in `game_constants.json` under a bumped `schema_version` (1 → 2); a GO-06 item records the key change | E | —; ED-GO-0002 on `main` (B10-01's entry action) | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:191-203`):

````
### GO-01 — `26` GO-VERSION: the ruled engine version where code reads it (GO) · BATCH B10-20 (sixth: GO-09 → GO-10 → GO-11 → GO-12 → GO-16 → GO-01 → GO-05 → GO-08 → GO-15; moved from B10-Z) · STATE BUILD (released whole: the version owner only) · R — (M3)
- WHAT: record the ruled engine version where code reads it. Jordan's 2026-10-09 ruling, ED-GO-0002 (the 4.7 series), is recorded in PR #467 (unmerged); its landing on `main` is B10-01's entry action, not a question (`-05` M13: ACTION). The tenth attribute's name no longer rides this position: it is J-T2, confirmed at the default (ED-IN-0301), with CL-ATTR (`-04` §2), and GO-01 does not wait on it. ED-1050's module re-export lapses with PC-05 (closed by GO-14).
- LANDED ALREADY: GO-03 (the `godot_conversion_strategy_v1.md:138` heading string removed at B-C; v9_p8 K (c-held) still says the heading "carries" it — v9 conflicts with itself, re-read the file).
- REMAINING UNBUILT: one machine-read owner, `references/engine_series.yaml`, holding one key, `engine_series: "4.7"`, with a comment citing ED-GO-0002; `tools/export_game_constants.py` reads it (the exporter owns no value) and emits `engine_series` in `engine/engine_params/game_constants.json` under a `schema_version` bumped 1 → 2; a GO-06 item records the key change for `valoria-game`'s parity reader.
- GATE: B10-20's entry (B10-18 merged). NEEDS: none by handle; ED-GO-0002 on `main` (PR #467 merged, rebased with its v9 hunks dropped, or B10-01's fallback: the row landed verbatim from commit `24f62f1`, held back). The earlier "Godot 4.6" mentions (v9's J-9 evidence: organising instructions, none a pin) are superseded by ED-GO-0002 and are replaced in `README.md` and `references/glossary.md` by GO-13.
- EXIT and FALSIFIER: `python tools/export_game_constants.py --check` exit 0 after re-export; the version string appears in exactly one machine-read file (`git grep` returns one owner and only pointers); B10-20's exit line 1 prints `4.7`. FALSIFIER: editing the YAML's value without a re-export reds `export_game_constants.py --check`. CONTROL: the six existing constants are unchanged.
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: ED-GO-0002, ED-1050, ED-IN-0193; J-9 (answered by ED-GO-0002); M3 (the milestone).
- ASKS ATTACHED: none open (M13 is Jordan's action: his merge of PR #467). The tenth attribute's name is J-T2 (CL-ATTR).
- RE-BASE: none found (no B-Q..B-Y subject names GO-01). Re-read `export_game_constants.py`'s `MAPPING` and `schema_version` by symbol. The chain GO-01 -> GO-05 -> PC-05 of v9 is replaced: GO-05 needs GO-01 and GO-12; PC-05 closes by GO-14.
- BUILDER: `CLAUDE.md` §10's first tier (extraction).
- SOURCE: `v9_p7:86-99` (carried v8 block `:93-99`; v8 source `workplans/valoria_master_workplan_v8_part5.md:115-119,405`); state-index row `v9.md:289`; queue row `v9_p5:321`.

````

### GO-05

card row (`valoria_master_workplan_v11_part3.md`):

```
| GO-05 | SM-13: the manifest resource lists module paths (M13 released): the manifest of module entry files derived from `composition.json` (ED-IN-0017 F1) and a test that every listed path exists; the `.gd` RESIST re-export half lapses with PC-05 | BUILD | E | GO-01, GO-12 | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:204-215`):

````
### GO-05 — SM-13: the manifest resource lists module paths (GO) · BATCH B10-20 (seventh, after GO-01; moved from B10-Z) · STATE BUILD (M13 hold released) · R — (M3)
- WHAT: at the port, each module's path is listed in the generated manifest resource so export packing sees the targets `load()` resolves by string (SM-13, GO lane). The manifest of module entry files is derived from `engine/engine_params/composition.json` (ED-IN-0017 F1). The `.gd` RESIST re-export half (ED-PC-0013 item 1) lapses with PC-05, closed by GO-14.
- LANDED ALREADY: IN-05 (modules under `modules/**`; B-L closed `fc4f3ba9`).
- REMAINING UNBUILT: the generated manifest, derived from `composition.json`, and its test.
- GATE: B10-20, after GO-01. NEEDS: GO-01, GO-12 (same batch, earlier). DEPS: IN-05 (D, satisfied).
- EXIT and FALSIFIER: EXIT "a test that every path the manifest lists exists under `modules/`, beside `test_importing_every_engine_module_pulls_in_no_subsystem`; `python tools/export_game_constants.py --check` exit 0." FALSIFIER "deleting one listed module path reddens the test; packing resolving every `load()` is observed by the Godot repo's export (not runnable here), which is why the Python-side test is the one that must be able to fail."
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: SM-13, ED-PC-0013 (item 1 superseded by GO-14's row), ED-IN-0017 F1, IN-05.
- ASKS ATTACHED: none open (M13 is Jordan's action, B10-01's entry).
- RE-BASE: none found.
- SOURCE: `v9_p7:101-106` (v8 source `v8_part5.md:379`; `registers/editorial_ledger_pc_archive.jsonl:33`); state-index row `v9.md:290`.

````

### GO-08

card row (`valoria_master_workplan_v11_part3.md`):

```
| GO-08 | The oracle pins export (port gate): `tools/export_oracle_pins.py` (`--build`/`--check`) writes `engine/engine_params/oracle_pins.json` (per seed 0-2 the build hash, the initial world in GO-07's encoding, the slice 1 and slice 2 traces, the draw log's digest, the executed-function list, the `primitives` block and the integer contract vectors; no Mersenne Twister vectors); `port_oracle.py` prints one line per pin; blocking in CI | BUILD | E | GO-07, GO-09, GO-10, GO-12, GO-16 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:10-22`):

````
### GO-08 — The oracle pins export (GO/IN) · BATCH B10-20 (eighth: … → GO-05 → GO-08 → GO-15) · STATE BUILD · R —
- WHAT: one exported, checked artifact holds every value the port's parity reader compares against, including the primitives' vectors and the integer contract.
- LANDED ALREADY: the seven existing exporters with `--check`; `engine/season/harness/` runners.
- REMAINING UNBUILT: `tools/export_oracle_pins.py` (`--build`/`--check`) writing `engine/engine_params/oracle_pins.json`: the oracle commit; per seed 0-2 the build hash, the initial world in GO-07's encoding, the no-act two-season hash, event count and step trace (slice 1), the per-round act trace and hash of a computed two-season run (slice 2); the digest of GO-16's draw log; the executed-function list of the no-act season (`sys.settrace` or `coverage`; this list fixes slice 1); a `primitives` block with `blake2b` vectors for `H` (`state/ids.py`, digest_size 8) and for the 128-bit content digest, GO-07 encoder vectors, the float yield vectors (`modules/settlements/produce.py:17-19`: fixed operand order, then `int` truncation), and the INTEGER CONTRACT vectors: `H` values are 64-bit unsigned and used in `%` and `//` with floor semantics (`loop/witness.py:198`, `:211`, `:221-222`), including values at or above 2^63, against GDScript's signed, truncating integers; Python `round()` is half-to-even (`data/cast.py:413`, `:444`); mappings iterate in insertion order and sets in hash order, so the port sorts wherever the oracle iterates a set. The ID hash and the log fold's integer fields (decimal `i<dec>;` since GO-07) are integer-contract items. NO Mersenne Twister or `random`-method vectors (the port replays recorded draws). `engine/season/harness/port_oracle.py` prints one line per pin. Wired into CI's validators job, blocking.
- GATE: B10-20, after GO-05. NEEDS: GO-07, GO-09, GO-10, GO-12, GO-16.
- EXIT and FALSIFIER: `--check` reds when one pinned value is edited by hand, and when one registry row changes without a re-build. CONTROL: two `--check` runs under `PYTHONHASHSEED` 0 and 1 both pass; `--check` on an unchanged tree reports current.
- HASH MOVERS: EQUAL.
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: none `[ASSUMPTION; medium; Jordan to correct; revert: delete the exporter and its JSON]`.
- RE-BASE: re-derive the draw census (`random`, `randrange`, `randint`, `gauss`, `choice`, `betavariate`) by grep before writing the integer-contract list.
- BUILDER: second tier producer; a third-tier (judgment) critic.
- SOURCE: the port gate; `CLAUDE.md` §5.

````

### GO-15

card row (`valoria_master_workplan_v11_part3.md`):

```
| GO-15 | FREEZE (port gate): re-take every pin on the merged tree; write the `ED-GO-` freeze row (oracle SHA, the pins digest, the draw log's digest, the freeze list); run this card's exit | MEASURE | E | GO-09, GO-10, GO-11, GO-12, GO-16, GO-01, GO-05, GO-08 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:72-84`):

````
### GO-15 — FREEZE (GO/IN) · BATCH B10-20 (last) · STATE MEASURE · R —
- WHAT: re-take every pin on the merged tree and record the freeze in an `ED-GO-` row: the oracle SHA, the pins artifact's digest, the draw log's digest, and the freeze list.
- LANDED ALREADY: —.
- REMAINING UNBUILT: the re-take, the row and the exit run. THE FREEZE LIST (positions and questions still open whose release or answer would move a pinned slice): CP-T04-10 (M3: `Rung.stores` and the larder draw), CP-T04-04 (M4 Ask C (b)), IN-36's `guards` default if its flip (B10-17, ED-IN-0317) has not landed (`build_realm`), the deed lie (H-198 rule (ii)), CL-THRUST B4.x, B5.2 and B6.n, M16's fourth motion (not needed by CL-EVENTS (3) and (4)); from the second decision round: the tensions on-arm flip (`build_realm(tensions=)`'s default, beside IN-36's `foreign`/`guards` defaults), `FILLED_BY`'s elected narrowing if it waits on an election executing (CR-35), and CR-38 and CR-39 if CR-38 is unapproved when B10-18 closes (the interim two-seat bench, the King and the Widow Regent, named and frozen); and, by the row's own rule (every position still held when B10-20 opens whose release would move a pinned slice), read at B10-20's open: REM-44, CP-T10-04, CP-T10-05, FA-01's clause, SE-04 (b) and CR-29 (all released from M11, ED-IN-0300: each is read only if it has not landed; CR-29 is a WITNESS change slice 1 pins; SE-04 (b) sits in B10-Z, unscheduled), any DESIGN-FIRST row then HELD (SC-02's tail, CP-T03-06, IN-48, CR-12), the doctrine row (M14's residue), the tenth attribute if answered Recall with a reader (void since the knowledge-model fold of 2026-11-04: Jordan's ten, `ED-IN-0328`, land before the freeze through CR-84, B10-10), SC-05 if unslotted, and any re-opening of `-05` §1a questions (a) (if a heritage member changes), (b) (an authored electors list) and (c) (a seat serving an emerged creed), each confirmed at the default (ED-IN-0301). Not on it: REM-52, CP-T10-03, REM-45, CL-EVENTS (its four commits land before the freeze; (3) and (4) are EQUAL, shipped off) and CP-T02-06 (each lands before the freeze or is EQUAL). OPEN lines, listed in the row: an exit line whose Layer 0/1 hunk or deletion did not land in its own position's PR (a (RULED) mark stopped it) stays OPEN; it does not block the freeze or the port.
- GATE: B10-20, last. NEEDS: GO-09, GO-10, GO-11, GO-12, GO-16, GO-01, GO-05, GO-08.
- EXIT and FALSIFIER: GO-08's `--check` on the freeze commit; each of B10-20's exit lines (`-03` B10-20: line 1's `engine_series` read and its grep over `README.md`, `references/glossary.md` and `CURRENT.md`; lines 2 to 5; line 6's `module_contracts.yaml` grep; lines 7 to 9) prints, and a line that does not keeps B10-20 open. CONTROL: GO-08's `--check` under two hash seeds.
- HASH MOVERS: EQUAL.
- HOLES AND LEDGER IDS: the new `ED-GO-` freeze row (id from `references/id_reservations.yaml`).
- ASKS ATTACHED: none of its own; the freeze list names the open questions.
- RE-BASE: read the held rows at B10-20's open to complete the rule-derived part of the list.
- BUILDER: third tier (judgment).
- SOURCE: the port gate. After the freeze, a commit that changes a pinned output re-builds the pins and the draw log in the same commit and writes an `ED-GO-` row naming old and new values and the slice it moves; a disagreement the port finds is settled on the Python side first (ED-1050), re-pinned and re-exported.

````

