# Evaluation of workplan v11, part 13: lane E4, carry-forward blocks (verbatim)

## Status: EVALUATION RECORD, assembled (stage 5 of `STAGES.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when workplan v12 is adopted)

**What this part is.** The carry-forward blocks of lane E4, copied by script from `master/eval/E4.md` lines 2166 to 3452, byte for byte; nothing below the rule was retyped or edited. Line numbers cited in the settlement ledger (`V11_EVALUATION_part2.md`) are those of the lane file, so a row of this part is found there as `E4:<line>`. Where the ledger re-dispositions a row, the ledger governs and the copy below keeps the lane's original call as the record.

---

### CR-38 — Court Parliament's bench (design-first) (IN/SC) · BATCH B10-19 (DESIGN-FIRST; drafted beside B10-13, approved before B10-18 closes) · STATE DESIGN-FIRST · R —
- WHAT: item 4 (make the endings reachable), the bench taken as design-first: Court Parliament has no bench of its own. At a realm venue `parliamentary_debate`'s bench is the King's and the Widow Regent's seats (`queries/world_q.py:475-481`), the interim two-seat bench. One design file names how a landed bench is derived, so that CR-34's tally can be flipped on at `parliamentary_debate`.
- LANDED ALREADY: the `parliamentary_debate` row; `judging_set`; CR-34's tally (landed `67f118dd`) and, by B10-17, CR-36's Record disposal site.
- REMAINING UNBUILT: one design file under `proposals/` naming the derivation, not authored seats. The default it tests: the holders of the governance-ladder title seats (`offices.yaml: titles.domains` posts) whose rung lies inside the venue ("Landed + distinguished service aristocrats", `worldbuilding_v30.md:180`), sitting by an assembly reading of the bench for a `parliamentary_debate` row. It states the cost of each route: (i) grant `determine` to the duchy-head seats (a remit edit that also lets them judge trials in their duchies, a mover on every duchy determination), or (ii) an arrangement-level bench reading (a fourteenth `arrangements.yaml` key, which the loader refuses today, `data/arrangements.py:73-75`); (iii) the interim realm bench is the third option. The same design flips `parliamentary_debate` to `disposal: declared` (CR-34's tally), and is the seating that H-90's "there is a Parliament" and the translation's named residue, the Parliamentary Stay (`-05` §1b), waits on.
- GATE: a B10-19 row. The design file is drafted beside B10-13 in a worktree (B10-19's card allows a worktree beside any code batch) and approved before B10-18 closes, by ED-1094's merge default unless its PR holds it back. Approved in time, its build (the bench reading it chooses and the `parliamentary_debate` flip) runs by R8 as its own sub-batch between B10-18 and B10-20; unapproved when B10-18 closes, it joins B10-20's freeze row as a declared post-freeze mover, with the interim two-seat bench (the King and the Widow Regent) named and frozen. NEEDS: CR-36 (its first reader). Not a dependency: CR-37 (the design states its falsifier against CR-37's specification).
- EXIT and FALSIFIER (for the design): it names a test in which a motion against the King is carried by a bench of at least two landed seats and refused by one, and a control in which the interim bench is kept.
- HASH MOVERS: EQUAL (a design file); its build a declared MOVER (either route moves every determination in the realm).
- HOLES AND LEDGER IDS: H-90.
- ASKS ATTACHED: item 4 (`-05` §1b) `[ASSUMPTION; medium; Jordan to correct; revert: delete the design; the interim bench stands]`. B10-19 members released later are post-freeze movers (`-03` B10-20).
- RE-BASE: re-read `judging_set` and the `parliamentary_debate` row by symbol on CR-36's landed tree.
- BUILDER: `CLAUDE.md` §10's third tier (judgment).
- SOURCE: `worldbuilding_v30.md:180` (intent); `data/arrangements.py:73-75`; `queries/world_q.py:475-481`.

### CR-39  ·  STILL-NEEDED  ·  FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:144` (handle index row)

| CR-39 | B10-Z | new from the second decision round (`-04`; item 4): promotion of an emerged creed; HELD on CR-38 |

`..._part3.md:435` (batch card row)

| CR-39 | Promotion: an emerged creed earns parliamentary standing (`queries/world_q.py::promoted`: its members hold live `hold`s on at least two territories, counted on demand, never stored) | HELD on CR-38 (trigger: CR-38 lands a Court Parliament bench) · BUILD when released | M (when built) | IN-30, CR-38 | — | written out in full: `-04` |

`..._part4.md:266` (-04 content-owner entry)

### CR-39 — Promotion: an emerged creed earns parliamentary standing (IN/FA) · BATCH B10-Z (HELD on CR-38) · STATE BUILD (HELD) · R —
- WHAT: item 4, promotion held at step 4: an emerged creed (IN-30) earns standing on Court Parliament's bench. GD-3's promotion conditions are restated in lawful forms and the position is held on its reader, CR-38's bench, because a Query with no consumer is a false N-line (r2 `05` §A.1.5 RULED (d), quoted in H-186's `cite:`). Trigger: CR-38 lands a Court Parliament bench.
- LANDED ALREADY: —.
- REMAINING UNBUILT (when built): `queries/world_q.py::promoted(w, creed)`: the creed's members hold live `hold`s on at least two territories (a count on demand, never stored, T-a's licensed form). GD-3 (c)'s `L ≥ 3` is refused as a gate (a stored aggregate, `-05` §1b's refusals); legitimacy enters as each bench member's reason when he votes the creed's seat in. `Accord ≥ 4 averaged` takes form F3 (the share of the held territories' residents whose live `commit` is to the creed, at or above a band) and is not carried until a band is ruled (no invented number). The two-season sustain is cut (a clock, #457 §5); GD-3 (d)/(e)'s `PT` split is an aggregate and is refused. The finding stands: the retired oracle's `L` was initialised at 1.0 and never written, so promotion was unreachable by construction (`git show 5c5d8ec6:systems/world/sim/insurgency_pipeline.py`, `:41`, `:44`, `:73`, `:218-221`; corroborated only in part by `governance_type_registry_v1.md:106`; the git object was not re-opened).
- GATE: HELD in B10-Z on CR-38. NEEDS: IN-30, CR-38.
- EXIT and FALSIFIER (when built): a creed whose members hold two territories sits on CR-38's bench; one holding one territory does not. CONTROL: CR-38's bench without the promotion term.
- HASH MOVERS: declared MOVER when built (it changes a bench).
- HOLES AND LEDGER IDS: H-186.
- ASKS ATTACHED: item 4 (`-05` §1b) `[ASSUMPTION; medium; Jordan to correct; revert: none needed while held]`. If CR-38 is unapproved when B10-18 closes, CR-39 is on B10-20's freeze row with it.
- RE-BASE: re-read IN-30's landed `faction_props` and CR-38's approved design when the trigger fires.
- BUILDER: `CLAUDE.md` §10's third tier (judgment).
- SOURCE: H-186's `cite:`; `canon/04_game_design_constraints.md` (GD-3).

### CR-40  ·  STILL-NEEDED  ·  SE · U3 B12-world-motion-and-ground, as the positions the SE proposals amend (R-SE-01..05, -19: `unified/U5_FINDINGS_CLOSURE_U5d.md:244`); CR-40 first, then CP-T08-01 onward in the card order · gate:…

`..._part12.md:145` (handle index row)

| CR-40 | B10-16 | new from the second decision round (`-04`; item 6): one grain for Prosperity, `starting_pros` deleted; first in B10-16, hash EQUAL |

`..._part3.md:165` (batch card row)

| CR-40 | One grain for Prosperity: delete the 17 `starting_pros` lines from `valoria_geography_v30.yaml` and write the header note that a Prosperity value lives at settlement grain only (a territory figure is a query over its settlements); the pin and the identifier census re-derived by the repo's tooling | EDIT (data; retire a field) | E | —; not a dependency: DEF-9 (the deletion is correct whether the frozen table survives or not) | — | written out in full: `-04` |

`..._part4.md:279` (-04 content-owner entry)

### CR-40 — One grain for Prosperity: delete `starting_pros` (SE) · BATCH B10-16 (first: CR-40 → CP-T08-01 → …) · STATE EDIT (data; retire a field) · R —
- WHAT: item 6 (reconcile the sources), Prosperity taken at step 5 with step 4: a Prosperity value lives only in a settlement's `stats` triplet. The provinces' `starting_pros` disagrees with the frozen territory table (`engine/engine_params/params_tables.yaml:6576`) in 11 of 17 territories (Jordan's "eleven Prosperity values"), nothing reads it, and a value over many settlements cannot be a field (T-a). It runs first in B10-16 (an EQUAL data edit on a file no B10-16 member edits), so the batch's movers read their controls on the post-deletion tree.
- LANDED ALREADY: each settlement's `stats` triplet [Prosperity, Defense, Order].
- REMAINING UNBUILT: `systems/settlements/valoria_geography_v30.yaml`: delete the 17 `starting_pros: <n>` lines (one per province) and insert, after line 6, the header note: "PROSPERITY IS A SETTLEMENT FACT ONLY. Each settlement's `stats` triplet [Prosperity, Defense, Order] is the one place a Prosperity value lives. Provinces carried a `starting_pros` until <commit>; it disagreed with the frozen territory table in `engine_params/params_tables.yaml` in 11 of 17 territories and with this file's own settlement sums in <n>, nothing read it, and a value over many settlements cannot be a field (T-a). A territory figure is a query over its settlements, written the day a reader needs one." (`<n>` is re-computed at the build and written as computed; the decision gave 13, not re-opened.) No clause about T1 exceeding a declared scale is written (the 0-5 scale is `set.prosperity`'s, a settlement stat, `descriptor_registry.yaml:89`). Re-derived by the repo's tooling: `references/canonical_sources.yaml:90` by `python3 tools/freshness_gate.py --update` (run `python3 tools/freshness_gate.py` first; the diff shows exactly that one line moved); `systems/settlements/_identifier_census.yaml` by `python tools/build_identifier_census.py` (`starting_pros` turns from defined to unresolved, the honest reading). Not edited: `params_tables.yaml:6576` (frozen; DEF-9 deletes it), `godot/data_serialization_spec.md` (stale).
- GATE: B10-16, first. NEEDS: none (DEF-9 is not a dependency: the deletion is correct whether the frozen table is still present or already deleted).
- EXIT and FALSIFIER: `python -c "import yaml; d=yaml.safe_load(open('systems/settlements/valoria_geography_v30.yaml')); assert not [t for t,v in d['provinces'].items() if 'starting_pros' in v]; assert len(d['settlements'])==37 and all(len(s['stats'])==3 for s in d['settlements'].values())"`. CONTROL: at the base commit the first assert fails (17 rows), so the defect is observable; the second holds on both sides. Then `python -m pytest engine/season/tests/test_mass_battle_module.py tests/valoria/test_mass_battle_terrain.py -q` (both open this file's `provinces:`).
- HASH MOVERS: EQUAL (`build_realm(0)` content hash equal against the base commit). Port: the geography YAML (opened by `data/files.py:148`, read by `data/geography.py`) crosses through GO-09; the port binds Prosperity at settlement grain only, and `godot/data_serialization_spec.md`'s `prosperity int # 0-5` (STALE) is implemented from nothing.
- HOLES AND LEDGER IDS: DEF-9 (the frozen table).
- ASKS ATTACHED: item 6 (`-05` §1b) `[ASSUMPTION; medium; Jordan to correct; revert: restore the 17 lines and re-pin the sha]`.
- RE-BASE: recount the eleven against `params_tables.yaml:6576` and the settlement sums at build.
- BUILDER: `CLAUDE.md` §10's second tier.
- SOURCE: `valoria_geography_v30.yaml:29`…`:237` against `params_tables.yaml:6576`; `01_AXIOMS.md:327-332` (T-a), `:512` (ID-1); Jordan's "reconcile all geography stuff with bias towards recency" (`valoria_geography_v30.yaml:241`).

### CR-46  ·  STILL-NEEDED  ·  IN · new batch `B11b-verbs-r05` (v11 B10-18b): CR-46 first (re-reads the R-05 base), CR-48 and CR-49 BEFORE U3 B12 (`14_VERBS_MATERIAL_B_stores` waits on CR-48), the remainder after U3 B26 · gate: `a…

`..._part12.md:151` (handle index row)

| CR-46 | B10-18b | new from the R-05 fold of 2026-10-31 (`-04`): the R-05 reading and its definition (`ex - both`; the denominator counts the six army rows; the menu-door clause) |

`..._part3.md:268` (batch card row)

| CR-46 | The R-05 reading (`ex - both`, pooled, per seed) and its definition: the denominator counts the six army rows, and the menu-door clause | BUILD (harness and text) | E | — | the menu-door clause: ratified by Jordan 2026-10-31 (ED-IN-0307), revert alone | written out in full: `-04` |

`..._part4.md:378` (-04 content-owner entry)

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

### CR-47  ·  STILL-NEEDED  ·  IN · new batch `B11b-verbs-r05` (v11 B10-18b): CR-46 first (re-reads the R-05 base), CR-48 and CR-49 BEFORE U3 B12 (`14_VERBS_MATERIAL_B_stores` waits on CR-48), the remainder after U3 B26 · gate: `a…

`..._part12.md:152` (handle index row)

| CR-47 | B10-18b | new from the R-05 fold (`-04`): works and Sites reach the chooser's ranking |

`..._part3.md:271` (batch card row)

| CR-47 | Works and Sites reach the chooser's ranking (`build`, `found`, `work`, `restore`, `examine`; `sabotage`'s rank link) | BUILD | M | CR-50, IN-45, REM-22, CP-T06-01, CR-21 | route (a) over (b) taken | written out in full: `-04` |

`..._part4.md:391` (-04 content-owner entry)

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

### CR-48  ·  STILL-NEEDED  ·  IN · new batch `B11b-verbs-r05` (v11 B10-18b): CR-46 first (re-reads the R-05 base), CR-48 and CR-49 BEFORE U3 B12 (`14_VERBS_MATERIAL_B_stores` waits on CR-48), the remainder after U3 B26 · gate: `a…

`..._part12.md:153` (handle index row)

| CR-48 | B10-18b | new from the R-05 fold (`-04`): a writ reaches its addressee through `give` |

`..._part3.md:272` (batch card row)

| CR-48 | A writ reaches its addressee through `give` (`comply`, `construe`, `evade / defy`); no mint (ED-IN-0292 (1)) | BUILD | M | CR-47, REM-2B, REM-25, IN-12 (landed `f9e4cef`) | — | written out in full: `-04` |

`..._part4.md:404` (-04 content-owner entry)

### CR-48 — A writ reaches its addressee (IN) · BATCH B10-18b (after CR-47) · STATE BUILD (hash MOVER) · R R-05 (`comply`, `construe`, `evade / defy`)
- WHAT: the three obedience verbs refuse every act on `exists:dispensation=0` (seed 0, four seasons: `comply` 37 refusals, `evade / defy` 17, `construe` 14) because their referent class is the shared `Record` class, so 38 persons form them on a non-writ Record, and the right formation (`world_q.writs_held`, `queries/world_q.py`) stamps only an addressee who HOLDS a writ: none does. Twelve dispensations were minted at seed 0 and every one is held by its issuer (`_eff_issue` mints into the issuer's hold). ED-IN-0292 (1) is RULED NO (a newborn Record is not a founding basis; `registers/editorial_ledger_in.jsonl`, 2026-10-14), so the route is not a mint into the addressee's hold; it is `give`, the act the ruling's own text names: a stamped occasion in `world_q.questions_for` that offers an issuer's held writs to `give` with `to` the addressee (`give` has no `referent_class`; with a held Record `decision/options.py::operand_bags` re-aims the subject to the writ's terms, not its id, so the re-aim for a writ needs its own read), and the `with` co-location that refuses 11 of 11 `give.refused` at seed 0 must hold for the pair. Once held, `comply` forms and admits, `evade / defy` emits `compliance.withheld`, `construe` `terms.distorted`.
- LANDED ALREADY: REM-2B (the typed cells and the class, B10-06, CLOSED, "no realm execution required", P9), REM-25 (widened the `Record` class, B10-05, CLOSED), IN-09's emission-only effects.
- REMAINING UNBUILT: the `give` occasion for a held writ and the re-aim of `operand_bags` for it; the co-location read. H-229's `give` Rung class is a different row and a neighbour on `verb_table.yaml`'s `give` row (P13: serialise).
- GATE: after CR-47. NEEDS: REM-2B, REM-25, IN-12 (B10-09).
- EXIT and FALSIFIER: `aperture 3 s`: `comply`, `evade / defy` and `construe` each executed at least once, with the compliance Event caused by an act of a non-issuer; a candidate on a dispensation id is non-empty in `opening_set`; or the exit records 0 with the refusal that decided and the verb stays a named residue. CONTROL: the occasion switched off reproduces the pre-item hash; the mint route is untouched (ED-IN-0292 (1)).
- HASH MOVERS: declared MOVER.
- HOLES AND LEDGER IDS: ED-IN-0292 (1) (RULED NO), H-44 (LEAVE: the nine dispensation terms), H-229 (open or closed not confirmed here: it is not in `-07` §1's index), H-203.
- ASKS ATTACHED: none new; K-24's evade-versus-defy split stays unbuilt, and `construe` stays emission-only (its row's witness-side revert is a standing `[ASSUMPTION]`). The build-all fold of 2026-11-02 adds CR-57 (a petition is addressable and deliverable), which reuses this position's `give` occasion; serialise on `verb_table.yaml`'s `give` row.
- RE-BASE: re-run the writ census (issuer, holder) and the `give` formation count at `give` with `with`. The figures in this entry come from probe runs whose output is not in the repository (the R-05 re-take of 2026-10-31); none is quoted until re-taken at the re-base. CR-71 (reading @5d6aac5, `aperture 2 0` and `strife 2 0`, seed 0, `PYTHONHASHSEED=0`, REALM): RF stays at 0 on the read this entry names: `evade / defy` formed 59, attempted 4, executed 0, all 4 refused `compliance.impossible` with last read `exists:dispensation=0`.
- BUILDER: third tier.
- SOURCE: the R-05 re-take of 2026-10-31; `verb_table.yaml` `comply`, `construe`, `evade / defy` and `give` rows.

### CR-49  ·  STILL-NEEDED  ·  IN · new batch `B11b-verbs-r05` (v11 B10-18b): CR-46 first (re-reads the R-05 base), CR-48 and CR-49 BEFORE U3 B12 (`14_VERBS_MATERIAL_B_stores` waits on CR-48), the remainder after U3 B26 · gate: `a…

`..._part12.md:154` (handle index row)

| CR-49 | B10-18b | new from the R-05 fold (`-04`): `exchange` names another rung |

`..._part3.md:273` (batch card row)

| CR-49 | `exchange` names another rung (`referent_class: Rung`; a self-trade declines) | BUILD | M | CR-48, REM-2B, REM-21 | — | written out in full: `-04` |

`..._part4.md:417` (-04 content-owner entry)

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

### CR-50  ·  STILL-NEEDED  ·  IN · new batch `B11b-verbs-r05` (v11 B10-18b): CR-46 first (re-reads the R-05 base), CR-48 and CR-49 BEFORE U3 B12 (`14_VERBS_MATERIAL_B_stores` waits on CR-48), the remainder after U3 B26 · gate: `a…

`..._part12.md:155` (handle index row)

| CR-50 | B10-18b | new from the R-05 fold (`-04`): referent classes for `raze` and `train` |

`..._part3.md:270` (batch card row)

| CR-50 | Referent classes for `raze` and `train` (H-232's stamps stay open) | EDIT (data) | M | CR-46, CR-52, REM-21, REM-27 | — | written out in full: `-04` |

`..._part4.md:430` (-04 content-owner entry)

### CR-50 — Referent classes for `raze` and `train` (IN) · BATCH B10-18b (first mover, after CR-46 and CR-52) · STATE EDIT (data: two classes) · R R-05 (contributor)
- WHAT: `raze`, `seize`, `pardon`, `train`, `arrest`, `covenant` and `establish` carry no `referent_class` in `verb_table.yaml`, so they form on every referent and the cell refuses what is not theirs (`train`: 37 of 86 refusals at seed 0 `exists:Person=0`; `raze`: 26 of 34 refusals on a `kind=person` rung that fails `MARCH_TARGET_KINDS` in `occupying_faction`, `loop/effects_shared.py`). `rosters.yaml: referent_classes` is closed at `[Office, Record, Rung, Site, Proposition, Person]`, and a person-kind rung classes as `Person`, so `referent_class: Rung` on `raze` drops its person-rung formations and `referent_class: Person` on `train` removes its subject-not-a-Person refusals. `seize`, `covenant` and `establish` take their classes from CP-T09-04, CP-T09-03 and CR-25; `pardon` refuses after admission (CR-51) and `arrest` is already warrant-narrowed (`decision/options.py`, `WARRANT_SOURCED`), so neither takes a class here. H-232's restrained-persons and occupied-settlements stamps are a new `questions_for` term, not built here; H-232 stays open. Cuts refusals; makes neither verb execute by itself.
- LANDED ALREADY: the class machinery (REM-21, REM-27, B10-05 and B10-06, CLOSED); `march`'s `referent_class: Rung`.
- REMAINING UNBUILT: the two cells.
- GATE: after CR-46, CR-52. NEEDS: REM-21, REM-27.
- EXIT and FALSIFIER: `aperture 3 s`: `train`'s `exists:Person=0` refusals and `raze`'s person-rung formations read 0; a verb whose class removes every formation reads formed 0 and is recorded, not repaired. CONTROL: classes removed reproduce the pre-item hash.
- HASH MOVERS: declared MOVER (formation changes).
- HOLES AND LEDGER IDS: H-232 (stays open); H-228 (limit 3).
- ASKS ATTACHED: none.
- RE-BASE: re-read the unclassed rows by symbol; `train`'s second refusal (`with=False`, pupil not present) is not this position's. The figures in this entry come from probe runs whose output is not in the repository (the R-05 re-take of 2026-10-31); none is quoted until re-taken at the re-base. CR-71 (reading @5d6aac5, `aperture 2 0` and `strife 2 0`, seed 0, `PYTHONHASHSEED=0`, REALM): VI and PU stay at 0 on `raze` attempted 12, executed 0: 10 refused after admission (last read `exists:Rung=1`, passed, so the decline is in the effect; the person-rung share this entry counts is not read here) and 2 at admission on `exists:Rung=0`. The decline is `_eff_raze`'s: `occupying_faction` (which CP-T09-04 edits) or `mustered` (`loop/effects_founding.py`); which one is not read. `requisition`, VI's third route verb, formed 18, offered 18, attempted 0 in these two seasons; it executes at four (CR-23's exit, IN-52's GATE), so VI's zero here is not this entry's alone. The SPINE refuses `pardon` AT admission on `exists:Person=0` (4 of 4, CR-51's sentence), which this entry's premise that `pardon` refuses after admission does not cover.
- BUILDER: first tier (data).
- SOURCE: the R-05 re-take of 2026-10-31.

### CR-51  ·  STILL-NEEDED  ·  IN · new batch `B11b-verbs-r05` (v11 B10-18b): CR-46 first (re-reads the R-05 base), CR-48 and CR-49 BEFORE U3 B12 (`14_VERBS_MATERIAL_B_stores` waits on CR-48), the remainder after U3 B26 · gate: `a…

`..._part12.md:156` (handle index row)

| CR-51 | B10-18b | new from the R-05 fold (`-04`): a restraint exists (`arrest`, `pardon`); MEASURE then BUILD the gap |

`..._part3.md:274` (batch card row)

| CR-51 | A restraint exists: `arrest` on a held warrant, `pardon` closing it | MEASURE then BUILD only the gap | M if built | CR-49, CR-47, IN-12 (landed `f9e4cef`), CR-50 | — | written out in full: `-04` |

`..._part4.md:443` (-04 content-owner entry)

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

### CR-52  ·  STILL-NEEDED  ·  IN · new batch `B11b-verbs-r05` (v11 B10-18b): CR-46 first (re-reads the R-05 base), CR-48 and CR-49 BEFORE U3 B12 (`14_VERBS_MATERIAL_B_stores` waits on CR-48), the remainder after U3 B26 · gate: `a…

`..._part12.md:157` (handle index row)

| CR-52 | B10-18b | new from the R-05 fold (`-04`): the menu door, the preset order of battle through `dispatching_chooser` |

`..._part3.md:269` (batch card row)

| CR-52 | The menu door: the preset order of battle (`recruit`, `form_unit`, `assign_troops`) through `dispatching_chooser`, with a test and an off control | BUILD (harness and test) | E | CR-46 | reconciliations (i) to (iii) in `-04` | written out in full: `-04` |

`..._part4.md:456` (-04 content-owner entry)

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

### CR-53  ·  STILL-NEEDED  ·  IN · new batch `B11b-verbs-r05` (v11 B10-18b): CR-46 first (re-reads the R-05 base), CR-48 and CR-49 BEFORE U3 B12 (`14_VERBS_MATERIAL_B_stores` waits on CR-48), the remainder after U3 B26 · gate: `a…

`..._part12.md:158` (handle index row)

| CR-53 | B10-18b | new from the R-05 fold (`-04`): `destroy_record`'s sink arm switched on |

`..._part3.md:275` (batch card row)

| CR-53 | `destroy_record`: the sink arm switched on (`withheld_verbs=ARMY_VERBS`) | BUILD (one value) | M | CR-51 | taken, revert stated; ratified by Jordan 2026-10-31 (ED-IN-0307) | written out in full: `-04` |

`..._part4.md:469` (-04 content-owner entry)

### CR-53 — `destroy_record`: the sink arm switched on (IN) · BATCH B10-18b (after CR-51) · STATE BUILD (one fixture value; hash MOVER) · R R-05 (`destroy_record`)
- WHAT: `destroy_record` is typed, `own`-eligible and effected, and withheld (`Fixtures withheld_verbs`, H-156 option (a), taken by v9 IN-26 `[ASSUMPTION; medium; Jordan to correct]` with "the flip ON is a separate, declared hash-moving commit"). Since then `rosters.yaml: own_hold_declines` narrows its formation to a referent the person himself holds, so the scene tax H-156 measured no longer applies to this row. A probe at `eda39a6`, seed 0, two seasons: the shipped arm 0 `record.destroyed`; with `withheld_verbs=ARMY_VERBS` 5 `record.destroyed`, 0 `destroy.refused`, content hash moved (H-156's IN-26 clause measured the sink arm at seed 0, realm at one and two seasons, and the corpus; seeds 1-2 at four seasons were not taken). Take the sink arm: `withheld_verbs=ARMY_VERBS`. CP-T06-08 (PARKED on JA-1) is read at its entry against the flip, not built here.
- LANDED ALREADY: the row, `_eff_destroy_record`, `test_in26_record_sink.py` (a hand-built world burns through a real season, with controls).
- REMAINING UNBUILT: the one value, the re-pins, H-156's row text.
- GATE: after CR-51. NEEDS: none.
- EXIT and FALSIFIER: `aperture 1 0` and `aperture 3 s`: `destroy_record` formed and executed with a Record receipt before ≠ after; the withheld control reproduces the pre-item hash; `test_season_weather.py` `BASE_HASHES` and `BASE_EVENTS`, `test_go07_canonical_digest.py` seeds 0-2, `test_season_shape.py`'s never-attempted set, `test_u7_own.py` and `test_in26_record_sink.py` re-recorded, each old to new in the commit body, stated plainly as a re-recorded golden.
- HASH MOVERS: declared MOVER.
- HOLES AND LEDGER IDS: H-156 (RULING, open); A2-07 (CARRIED); M19 (TAKEN, (a)).
- ASKS ATTACHED: `[ASSUMPTION; medium; Jordan to correct; revert: restore ("destroy_record", *ARMY_VERBS) in the fixture]`; a game change (a holder may burn a Record he holds), ratified by Jordan with the fold on 2026-10-31 (ED-IN-0307).
- RE-BASE: re-run both arms at seeds 0-2 on the base commit. The figures in this entry come from probe runs whose output is not in the repository (the R-05 re-take of 2026-10-31); none is quoted until re-taken at the re-base.
- BUILDER: first tier.
- SOURCE: `data/fixtures.py` (`withheld_verbs` and its comment); `hole_register.yaml` H-156.

### CR-54  ·  STILL-NEEDED  ·  IN · new batch `B11b-verbs-r05` (v11 B10-18b): CR-46 first (re-reads the R-05 base), CR-48 and CR-49 BEFORE U3 B12 (`14_VERBS_MATERIAL_B_stores` waits on CR-48), the remainder after U3 B26 · gate: `a…

`..._part12.md:159` (handle index row)

| CR-54 | B10-18b | new from the R-05 fold (`-04`): the `revoke` vacancy motive, design-first |

`..._part3.md:276` (batch card row)

| CR-54 | `revoke`: the vacancy motive, a design for a general motive (H-207 (A)'s remaining path) | DESIGN-FIRST, then BUILD | E (design) | B10-17 merged (CR-37, CP-T09-09) | design approved by ED-1094's merge default unless held back | written out in full: `-04` |

`..._part4.md:482` (-04 content-owner entry)

### CR-54 — `revoke`: the vacancy motive (design-first) (IN/FA) · BATCH B10-18b (design drafted beside the batch; build after CR-53 if approved) · STATE DESIGN-FIRST, then BUILD · R R-05 (`revoke`), R-04 (conjunct (1))
- WHAT: `revoke` is formed 17 times and attempted 8 times, pooled over seeds 0-2 at four seasons, and never executed; `loop/predicates.py::office_named_by` is not called for `revoke`, which keeps the base's read of `payload['office']`, so a computed act is refused at its precondition. H-207 (A) (`hole_register.yaml`; the recorder's reading of Jordan's 2026-10-12 ruling, "his words where quoted, the readings are mine" and an `[ASSUMPTION]`) says a computed `revoke` is not driven and none is to be special-cased in; what remains, in that row's words, is a design-first motive, a vacancy read as a need. CP-T02-04 was cut by the NERS fold and CR-37 builds a hand-built `joint_concurrence` route only, so no v10 position owns the motive until this one. Write a design under `proposals/` for a general, non-special-cased motive the chooser already scores (a vacancy read as a need; CP-T09-09's `legitimacy` occasion gaining the deposition's motive as a second named consumer is the candidate), the read of `subject` by `office_named_by`, its fit with CR-37's `REVOCATION_RULES` and `joint_concurrence`, and the falsifier its build carries. No code at this step.
- LANDED ALREADY: `_eff_revoke` and its ban (`loop/effects_governance.py`); IN-31's cost; REM-28 (`referent_class: Office`, B10-06, CLOSED); CR-37's hand-built route (B10-17).
- REMAINING UNBUILT: the design; its build is a successor row written when the design is approved.
- GATE: B10-17 merged (CR-37, CP-T09-09). Approval of the design by ED-1094's merge default unless the PR lists it held back; if it is unapproved when B10-18b closes, the row moves to B10-Z as HELD and `revoke` is a named R-05 residue.
- EXIT and FALSIFIER: the design file exists and names the motive's source, the `office_named_by` change and its guard against a special case (no entity or outcome named), and the realm reading its build must print (`aperture 3 s`: `revoke` executed with `Act.via` a seat whose `revocation` admits it). No code.
- HASH MOVERS: none at this step.
- HOLES AND LEDGER IDS: H-207 (A) and the hunk `-05` M8 corrected; `proposals/2026-10-14-in31-revocation-cost-provenance.md` (its reading: "not driven" means no motive scores it, not that it is never formed).
- ASKS ATTACHED: `[ASSUMPTION; medium; Jordan to correct; revert: revoke stays a named R-05 residue]`: H-207 (A) is read as barring a special case and not a general motive, on the ledger row's own wording that the readings are the recorder's. This supersedes `-08` part 2 AM-B-10's cut reading of CP-T02-04, whose "just say no for now" quote is ED-IN-0292 (1)'s (H-203), not H-207's, and whose reopen condition (a computed `revoke` executing) is replaced by H-207 (A)'s own "what remains is a design-first motive"; Jordan ratified this reading with the fold on 2026-10-31 (ED-IN-0307); the design itself is still approved by its own merge (ED-1094).
- RE-BASE: re-read H-207 (A) in full at `hole_register.yaml` and the ruling's quoted words before the design is written. The figures in this entry come from probe runs whose output is not in the repository (the R-05 re-take of 2026-10-31); none is quoted until re-taken at the re-base.
- BUILDER: third tier (judgment).
- SOURCE: the R-05 re-take of 2026-10-31; H-207.

### CR-57  ·  STILL-NEEDED  ·  SC · U3 B27-sc-proceedings (IS-B2-SC-10: 'after B24'); CR-57 only after CR-48 · gate: the entry's falsifier + `aperture 2 0` `open_case`/`determine` counts · hash: movers declared · tier: opus

`..._part12.md:162` (handle index row)

| CR-57 | B10-18c | new from the build-all fold of 2026-11-02 (`-04`): a petition is addressable and deliverable; reuses CR-48's `give` occasion; declared mover |

`..._part3.md:291` (batch card row)

| CR-57 | A petition is addressable and deliverable (`to` fans over the known; a held petition has CR-48's `give` occasion) | BUILD | M | CR-48, IN-10, REM-25 | — | written out in full: `-04` |

`..._part4.md:504` (-04 content-owner entry)

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

### CR-58  ·  STILL-NEEDED  ·  SC · U3 B27-sc-proceedings (IS-B2-SC-10: 'after B24'); CR-57 only after CR-48 · gate: the entry's falsifier + `aperture 2 0` `open_case`/`determine` counts · hash: movers declared · tier: opus

`..._part12.md:163` (handle index row)

| CR-58 | B10-18c | new from the build-all fold of 2026-11-02 (`-04`): consent: acts admitted only on a council's count; `<verb>.unlicensed`; needs CR-36, CR-37; declared mover |

`..._part3.md:292` (batch card row)

| CR-58 | Consent: acts admitted only on a council's count; `<verb>.unlicensed`; the discriminator at a data owner | BUILD | M | CR-57, CR-36, CR-37, CR-56 (landed `6e9550c4`) | which acts need consent is content (Jordan's) | written out in full: `-04` |

`..._part4.md:517` (-04 content-owner entry)

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

### CR-59  ·  STILL-NEEDED  ·  SC · U3 B27-sc-proceedings (IS-B2-SC-10: 'after B24'); CR-57 only after CR-48 · gate: the entry's falsifier + `aperture 2 0` `open_case`/`determine` counts · hash: movers declared · tier: opus

`..._part12.md:164` (handle index row)

| CR-59 | B10-18c | new from the build-all fold of 2026-11-02 (`-04`): an appeal goes to another authority: the appellate closure basis; hash EQUAL |

`..._part3.md:293` (batch card row)

| CR-59 | An appeal goes to another authority: the appellate closure basis (`appeal_to`) | BUILD (hand-built route) | E | CR-58, SC-04 (landed `bc5d987a`), CR-35, CR-51 | — | written out in full: `-04` |

`..._part4.md:530` (-04 content-owner entry)

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

### CR-60  ·  STILL-NEEDED  ·  SC · U3 B27-sc-proceedings (IS-B2-SC-10: 'after B24'); CR-57 only after CR-48 · gate: the entry's falsifier + `aperture 2 0` `open_case`/`determine` counts · hash: movers declared · tier: opus

`..._part12.md:165` (handle index row)

| CR-60 | B10-18c | new from the build-all fold of 2026-11-02 (`-04`): authority, scope and a two-valued rite default; P4 Q1 taken; declared mover |

`..._part3.md:294` (batch card row)

| CR-60 | Authority, scope and a two-valued rite default (`authority.by_faction`, `scope:`, case-opening reads `scope_rung`) | BUILD | M | CR-59, SC-04 (landed `bc5d987a`), CR-35 | P4 Q1 taken, revert stated | written out in full: `-04` |

`..._part4.md:543` (-04 content-owner entry)

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

### CR-61  ·  STILL-NEEDED  ·  SC · U3 B27-sc-proceedings (IS-B2-SC-10: 'after B24'); CR-57 only after CR-48 · gate: the entry's falsifier + `aperture 2 0` `open_case`/`determine` counts · hash: movers declared · tier: opus

`..._part12.md:166` (handle index row)

| CR-61 | B10-18c | new from the build-all fold of 2026-11-02 (`-04`): the case file, a Record of kind `case`; the citation as a writ; declared mover |

`..._part3.md:295` (batch card row)

| CR-61 | The case file: a Record of kind `case`, held, forgeable, burnable; the citation as a writ | BUILD | M | CR-60, CR-55 (landed `eb76f57f`), CR-57, CR-48 | — | written out in full: `-04` |

`..._part4.md:556` (-04 content-owner entry)

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

### CR-62  ·  STILL-NEEDED  ·  SC · U3 B27-sc-proceedings (IS-B2-SC-10: 'after B24'); CR-57 only after CR-48 · gate: the entry's falsifier + `aperture 2 0` `open_case`/`determine` counts · hash: movers declared · tier: opus

`..._part12.md:167` (handle index row)

| CR-62 | B10-18c | new from the build-all fold of 2026-11-02 (`-04`): a plea with a concession reward, tested through the obstacle before any grade cap; declared mover |

`..._part3.md:296` (batch card row)

| CR-62 | A plea with a concession reward, tested through the obstacle before any grade cap | BUILD | M | CR-61, B10-08 (landed), CR-20 (landed `c7764a5a`) | — | written out in full: `-04` |

`..._part4.md:569` (-04 content-owner entry)

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

### CR-63  ·  STILL-NEEDED  ·  SC · U3 B27-sc-proceedings (IS-B2-SC-10: 'after B24'); CR-57 only after CR-48 · gate: the entry's falsifier + `aperture 2 0` `open_case`/`determine` counts · hash: movers declared · tier: opus

`..._part12.md:168` (handle index row)

| CR-63 | B10-18c | new from the build-all fold of 2026-11-02 (`-04`): the five robust decisions as verb rows; declared mover |

`..._part3.md:298` (batch card row)

| CR-63 | The five robust decisions as verb rows (proofs, self or advocate, naming enemies, the warrant duty, appear / evade / defy) | BUILD | M | CR-48, CR-51, CR-57, CR-61, CR-64, CR-20 (landed `c7764a5a`) | — | written out in full: `-04` |

`..._part4.md:582` (-04 content-owner entry)

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

### CR-64  ·  STILL-NEEDED  ·  SC · U3 B27-sc-proceedings (IS-B2-SC-10: 'after B24'); CR-57 only after CR-48 · gate: the entry's falsifier + `aperture 2 0` `open_case`/`determine` counts · hash: movers declared · tier: opus

`..._part12.md:169` (handle index row)

| CR-64 | B10-18c | new from the build-all fold of 2026-11-02 (`-04`): the forum is a stage of the same case; hash EQUAL |

`..._part3.md:297` (batch card row)

| CR-64 | The forum is a stage of the same case (R-34 precedence) | BUILD (hand-built route) | E | CR-60, CR-61 | P4 Q5 taken, revert stated | written out in full: `-04` |

`..._part4.md:595` (-04 content-owner entry)

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

### CR-65  ·  STILL-NEEDED  ·  SC · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:170` (handle index row)

| CR-65 | B10-18c | new from the build-all fold of 2026-11-02 (`-04`): the legitimacy index, design-first, held on P4 Q2 |

`..._part3.md:300` (batch card row)

| CR-65 | The legitimacy index (design-first; held on P4 Q2) | DESIGN-FIRST, then BUILD only on approval | E (design) | CR-60 | P4 Q2 (Layer-1 F8) | written out in full: `-04` |

`..._part4.md:608` (-04 content-owner entry)

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

### CR-66  ·  STILL-NEEDED  ·  SC · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:171` (handle index row)

| CR-66 | B10-19 | new from the build-all fold of 2026-11-02 (`-04`): membership contests, design-first |

`..._part3.md:403` (batch card row)

| CR-66 | Membership contests: admission, expulsion, precedence (the `tribunal` row binds the order) | DESIGN-FIRST | E (design) | CR-60 | which bodies admit by contest is content (Jordan's) | written out in full: `-04` |

`..._part4.md:621` (-04 content-owner entry)

### CR-66 — Membership contests: admission, expulsion, precedence (design-first) (SC) · BATCH B10-19 · STATE DESIGN-FIRST, then BUILD only on approval · R R-04 (contributor)
- WHAT: the `tribunal` row *binds the order* (`disposes: ban`) and a guild, an order or a council admits and excludes, yet no matter family holds it. Today admission is a self-sworn `oblige` (255 acts at seed 0). Design what contests a membership: the party (the applicant or the member), the disposal (`ban` for exclusion; admission is a `confer` or an `oblige` accepted), the bench, and what is witnessed.
- LANDED ALREADY: `tribunal`, `oblige`, `confer`, `establishment_of`.
- REMAINING UNBUILT: the design file.
- GATE: drafted beside B10-19; build only on approval. NEEDS: CR-60.
- EXIT and FALSIFIER: design approved by ED-1094's merge default unless held back.
- HASH MOVERS: none at the design step (E).
- HOLES AND LEDGER IDS: H-90.
- ASKS ATTACHED: content (which bodies admit by contest) is Jordan's, P11.
- RE-BASE: none.
- BUILDER: second tier (design).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

### CR-67  ·  STILL-NEEDED  ·  SE · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:172` (handle index row)

| CR-67 | B10-19 | new from the build-all fold of 2026-11-02 (`-04`): trade and levy, design-first |

`..._part3.md:404` (batch card row)

| CR-67 | Trade and levy: a market, a toll, a price, a tax (no verb exists beyond `requisition`) | DESIGN-FIRST | E (design) | CR-58 | which taxes exist is content (Jordan's) | written out in full: `-04` |

`..._part4.md:634` (-04 content-owner entry)

### CR-67 — Trade and levy: a market, a toll, a price, a tax (design-first) (SC/SE) · BATCH B10-19 · STATE DESIGN-FIRST, then BUILD only on approval · R R-04 (contributor)
- WHAT: no tax or levy verb exists beyond `requisition` (parliament design §8), so a matter about a market, a toll or a tax has no disposal and no party. Design whether the matter is a motion about the holder of the market or the rung, what the owner's act is, and whether it needs CR-58's consent conjunct.
- LANDED ALREADY: `requisition`, `exchange` (CR-49), CR-58.
- REMAINING UNBUILT: the design file.
- GATE: drafted beside B10-19; build only on approval. NEEDS: CR-58.
- EXIT and FALSIFIER: design approved by ED-1094's merge default unless held back.
- HASH MOVERS: none at the design step (E).
- HOLES AND LEDGER IDS: H-163.
- ASKS ATTACHED: which taxes exist is content, Jordan's, P11.
- RE-BASE: none.
- BUILDER: second tier (design).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

### CR-73  ·  STILL-NEEDED  ·  WR · U3 B12 for the weather/route items (CP-T10-01, -02, -03 `season_terms`, CL-EVENTS (2) with `09_WR_B_weather_with_memory_and_the_year`, A-54); new batch `B37p-wr-npc-life` before U3 B39 for CP-T1…

`..._part12.md:177` (handle index row)

| CR-73 | B10-18 | new from the strife fold (v11; `-11`): natural shock (SH), a lowest-member draw that bites (a shortfall logged in that territory that season); harness and one optional `tick` on `season_factor_of`, hash EQUAL |

`..._part3.md:248` (batch card row)

| CR-73 | Natural shock (SH): a low draw that bites, a territory-season at the live arm's lowest member in which the larder pass logs a `shortfall` there; the past draw recomputed through a new optional `tick` on `season_factor_of`; no Event kind added (the strife fold, v11) | BUILD (harness) | E | CL-EVENTS; not a dependency: CP-T10-02 | — | written out in full: `-11` |

`..._part16.md:21` (-04 content-owner entry)

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

### CR-74  ·  STILL-NEEDED  ·  IN · harness reading after CR-63 (see the SCP target in the carry block header); carrier per PAPACY-A · hash: EQUAL · tier: sonnet

`..._part12.md:178` (handle index row)

| CR-74 | B10-18c | new from the strife fold (v11; `-11`): religious sanction (CH), a signature on a restraint opened through a church seat, or the missing carrier named; harness, hash EQUAL |

`..._part3.md:299` (batch card row)

| CR-74 | Religious sanction (CH): a strife signature on a restraint opened through a church seat, read from a property the institution already carries, or the missing carrier named (the strife fold, v11) | BUILD (harness) | E | CR-51, CR-63, IN-30 | — | written out in full: `-11` |

`..._part16.md:38` (-04 content-owner entry)

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

### CR-83  ·  STILL-NEEDED  ·  FI · design-first, before U3 B11/B26 consumers (IS-B2-FI-05) · gate: design approved, then measure-first · tier: opus

`..._part12.md:187` (handle index row)

| CR-83 | B10-13 | new from `ED-IN-0324` (`-04`): familiarity sets inference and adjudication, design-first, drafted beside B10-13; since the knowledge-model fold also CR-82's struck questions (opinion persistence measured first, subject fit, `said_of`'s weighing, CR-19's flip) and the `write_matrix.yaml` Layer-1 question |

`..._part3.md:102` (batch card row)

| CR-83 | Familiarity sets inference: how much a holder can infer of another's pursuits, convictions, ambitions, goals, obligations and demands (`ED-IN-0324`; design-first: one design file under `proposals/` naming what he may read of the other, its cost, and its falsifier; no carrier coined before it); since the knowledge-model fold of 2026-11-04 also the context (`ED-IN-0325`), Attunement and Reason (`ED-IN-0326`, `ED-IN-0327`; Reason read at `attr.mind.acuity`), opinion persistence as a measurement first, the subject-fit term, `said_of`'s weighing (G3), the event-identity gap (recorded, not fixed) and CR-19's flip; one open item, whether `write_matrix.yaml` is Layer-1-bound | DESIGN-FIRST (drafted beside B10-13, as CR-38 is; approved by ED-1094's merge default; its build waits on the design and is scheduled by it) | E (the design; its build M) | CR-31 (landed `f1319502`; its consumer `teller_weight`'s relation term), CR-17 (believed odds; landed `1ef8d273`) | — | written out in full: `-04` |

`..._part4.md:106` (-04 content-owner entry)

### CR-83 — Familiarity sets inference and adjudication: what a holder can infer of another person and of the context (SC, IN) · BATCH B10-13 (drafted beside it, as CR-38 is) · STATE DESIGN-FIRST (with the claim-model items CR-82 hands on) · R R-07
- WHAT: `ED-IN-0324` (Jordan, 2026-11-04): *"the more you know someone, the more you can intuit/understand their pursuits and convictions and ambitions and goals and obligations and demands"*. Today `person_q.py::known_persons` says whether a holder knows a person (a set), `regard` scores a referent's deeds by the holder's own pursuits and his stance rows, and no reader gives a graded estimate of another person's pursuits, convictions, ambitions, goals, obligations or demands; familiarity is not a degree. Write ONE design file under `proposals/` that says what a holder may read of another person and how the reading grows with what he holds of him (his `seen` and told claims, his own tenures with the other, shared faction membership, CR-81's acquaintance claims), by composing on what exists and coining no carrier; names its consumers (`teller_weight`'s relation term through CR-31, CR-27's `lie`, CR-17's believed odds, the tellings); its cost; and its falsifier (a seeded run in which a holder who knows another better infers more of the other's pursuits, and equal at no acquaintance). The five rulings on the claim model (`ED-IN-0319` to `ED-IN-0323`, CR-82) are its inputs: familiarity feeds on the same ledger CR-82 keeps. SECOND HALF (`ED-IN-0325`, Jordan, same day): *"and the more you know about strife flows and faction thrust and regimes and offices and other contextual elements, the more you can adjudicate"*: the same design file says what a holder may read of the CONTEXT (a strife flow, a thrust axis, a regime, an office) from what he already holds, how that grades his adjudication of a claim, a matter or a person's conduct (ED-IN-0323's fit factor, generalised), and which strife and thrust readers are its consumers (CR-75 to CR-79, CL-THRUST's readers); no carrier coined, and no change to those positions' own gates. THIRD HALF (`ED-IN-0326`, Jordan, same day): *"further your attunement will help you judge accurately the pursuits and convictions and everything, and your reasoning will help you judge accurately offices and regime and obligations etc"*: the design also says how the holder's Attunement (`attr.social.attunement`) sharpens the person inference and his judgment of whether a teller is telling the truth (`ED-IN-0327`: CR-19 and CR-27 are consumers) and how his Reasoning sharpens the context adjudication; Reason is now an attribute: CR-84 (B10-10, landed `1abaa612`) names the key `attr.mind.acuity` Reason and keeps the key (until that fold Reasoning was only an alias of Acuity), so the design takes Reason, read at `attr.mind.acuity` [ASSUMPTION; medium; Jordan to correct; revert: another attribute], and reads CR-20 (B10-10, landed `c7764a5a`) for the attribute carrier.
- ABSORBED FROM CR-82 (the knowledge-model fold of 2026-11-04; `proposals/2026-11-04-knowledge-model-build-plan.md` §2, §2.2 and §11 item 3, reference). The same design file also states, each with its falsifier: (1) **opinion persistence, as a measurement first** (`ED-IN-0320`): the deed claims evicted before N seasons at CR-82's shipped cap. If zero, the ruling is met and nothing is built. If non-zero, a design decision with a matrix change (`write_matrix.yaml` row steps), a single owner for the judgment (not `stance` and `regard` both), and a control that every reader of `stance_toward` (`legitimacy`, `_bond`, `teller_weight`, `choose`, forgive, `reception`) is unchanged. (2) **The subject-fit term** (`ED-IN-0323`: fit with what the holder holds of the claim's subject person) in `queries/person_q.py`, passed to `queries/` as a closure so `decision/` is never imported (`world_q.py:2672`), and `regard`'s recursion constraint (`deeds_judged` stays unweighted, `person_q.py:102-104`). (3) **`said_of`'s weighing** (G3; `ED-IN-0321`): today only `belief_contradicts` passes a `weigh` and the chained told arm is dormant (H-237). (4) **The event-identity gap, recorded and not fixed**: a "similar claim" is the exact `(subject, predicate, value)` triple, so news of a second killing by the same person from an origin already behind a copy is dropped; no field is coined. (5) **CR-19's flip** (`ED-IN-0327`): CR-19 ships its factor at gain 0; this design gives the separator between a lie and a truth that a live gain needs, and schedules the flip as a declared mover (CR-27's exit carries the falsifier the flip must pass). (6) **The old CR-82 commit 4's build half**: a reader of staleness only where the design already names one (`belief_contradicts`' floor, H-40), else the gap recorded. `ED-IN-0324` to `ED-IN-0327` are its inputs as above.
- OPEN ITEM, the one: **is `write_matrix.yaml` Layer-1-bound?** If (1)'s measurement is non-zero, an opinion mechanism needs a matrix row to gain a step; whether that edit is an agent's or Jordan's is unread in the tree. It blocks nothing until that measurement reads non-zero; the design states the question and does not answer it. FOURTH HALF (`ED-IN-0334`, Jordan, 2026-11-05): *"in addition to knowing people directly, you can know OF people due to their reputation and standing (eg everyone will know of king Almud even if they don't know him personally) as per combination of rung, allegiance and overlapping activities"*: the same design file says what a holder may know OF a person from the person's rung, allegiance and overlapping activities, as a graded reading computed when read (no claim per prominent person: that would repeat CR-81's eviction fade at ledger scale, and `known_persons` is a set with no degree); it reads the existing World halves (`world_q.opinion_of`, `reception`, rung and office relations) and coins no carrier. [ASSUMPTION; medium; Jordan to correct; revert: delete the design file] FIFTH HALF (the arc fold of 2026-11-05, ED-IN-0346): `person_q.believed_clock` and the person twin of `sittings_failed` (CR-89, B10-17b) are consumers of the retained claims and the know-OF grade, and CR-88's design (duty and the betrayal reading) is drafted beside this one and reads it; CR-81's acquaintance claims heading every question list (the interaction audit, H3) is a reading this design states, not a revert of CR-81. SIXTH HALF (ED-IN-0347, Jordan, 2026-11-05, AR-24 to AR-26a): *"perception will impact how much any given character will know about something … but it concerns FACTUAL matters"*: the design also says how the holder's Perception (`attr.mind.perception`) grades what he comes to know of worldly facts, at WITNESS (the World may read the true value; `observers_for`, `loop/witness.py`'s seat deposit of a larder's `shortfall:<kind>`), on the deposit's confidence and not as a gate `[ASSUMPTION; medium; Jordan to correct; revert: a gate]`; and it states which attribute grades CR-19's competence for which kind of told claim (persons: Attunement; offices, regimes, obligations: Reason; facts: Perception) before CR-19's flip.
- GATE: B10-13's entry; the design is drafted beside B10-13 (as CR-38 is) and reads CR-82 (landed `1ef8d273`), CR-17's believed odds (landed `1ef8d273`), CR-20's attribute carrier and CR-84's roster (B10-10, landed `c7764a5a` and `1abaa612`). NEEDS (v11's cell stands): CR-31 (landed `f1319502`), CR-17 (landed `1ef8d273`). It did not precede CR-27 (landed `db1dc1f2`), which built as written and needed nothing from this design. Approval by ED-1094's merge default unless the design PR lists it as held back.
- EXIT and FALSIFIER: the design file exists and states the three things above (what a holder may read, its cost, its falsifier), items (1) to (6) each with a falsifier, and the open item as a question; no code.
- HASH MOVERS: none at this step; each build it schedules (the opinion mechanism if (1) is non-zero, the fit term, CR-19's flip) is a declared mover, scheduled by the design.
- HOLES AND LEDGER IDS: `ED-IN-0320` to `ED-IN-0327`; H-40, H-237.
- ASKS ATTACHED: none open; Jordan's answers are `ED-IN-0324`, `ED-IN-0325`, `ED-IN-0326` and `ED-IN-0327`. The open item above is stated, not written as a `needs_jordan` row. [ASSUMPTION; medium; Jordan to correct; revert: delete the design file]
- BUILDER: opus; `valoria-author`.
- SOURCE: `ED-IN-0324`; `proposals/2026-11-04-knowledge-model-build-plan.md` §2.2 (reference).

### CR-88  ·  STILL-NEEDED  ·  FA · new batch `B21c-arc` after B21b: CR-91 -> CR-89 (1)(2) -> CR-90 -> CR-88 build -> CR-89 (3)(4) · gate: CR-90's arc instrument per seed + the entry's falsifier · hash: CR-91, CR-88 build and each…

`..._part12.md:192` (handle index row)

| CR-88 | B10-17b | new from the arc fold of 2026-11-05 (`-04`; `ED-IN-0335`, `ED-IN-0338`): duty of office and the cost of betrayal; DESIGN-FIRST, drafted beside B10-13 with CR-83; its build in B10-17b after CR-90 |

`..._part3.md:227` (batch card row)

| CR-88 | Duty of office and the cost of betrayal: a person-side duty decline on opponent-rule verbs against his faction's head or officers, lifted only by `person_q.grievance_against` above a band (held deed claims from distinct origins); duty's positive half adds the faction's goals at `fx.duty_weight` (`ED-IN-0335`, `ED-IN-0338`; the arc fold of 2026-11-05) | DESIGN-FIRST (drafted beside B10-13 with CR-83; approved by ED-1094's merge default), then BUILD here | M (the build) | CR-86 (landed `83715fd6`), CR-83 (the design), CR-82 (landed `1ef8d273`), CR-90 | — | written out in full: `-04` |

`..._part4.md:161` (-04 content-owner entry)

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

### CR-89  ·  STILL-NEEDED  ·  FA · new batch `B21c-arc` after B21b: CR-91 -> CR-89 (1)(2) -> CR-90 -> CR-88 build -> CR-89 (3)(4) · gate: CR-90's arc instrument per seed + the entry's falsifier · hash: CR-91, CR-88 build and each…

`..._part12.md:193` (handle index row)

| CR-89 | B10-17b | new from the arc fold of 2026-11-05 (`-04`; `ED-IN-0339`, `ED-IN-0341`, `ED-IN-0343` to `ED-IN-0345`): the clocks (Church Influence, Turmoil) as folds of the log, the breaking point, "the nation functions", the band triggers shipped off; each flip a declared mover |

`..._part3.md:225` (batch card row)

| CR-89 | The clocks as folds of the log: Church Influence and Turmoil as `rosters.yaml: clocks:` rows (feeders by Event kind, bands as fixtures), one `clock_fold` read world-side and person-side over held claims, no matrix row; the breaking point `sittings_failed`; "the nation functions" as a goal row; each band trigger shipped off and flipped only on CR-90's reading (`ED-IN-0339`, `ED-IN-0341`, `ED-IN-0343` to `ED-IN-0345`; the arc fold of 2026-11-05) | BUILD in four commits: (1) roster, loader, fold and readers; (2) `sittings_failed`; (3) each trigger, shipped off; (4) each flip, one commit each | E (commits 1-3); M (each flip) | CR-91, CR-86 (landed `83715fd6`), CR-29, CR-34 (landed `67f118dd`), CP-T09-02, CP-T09-04 | the arc's target share (default in force, head §6 risk 4 (a)) | written out in full: `-04` |

`..._part4.md:175` (-04 content-owner entry)

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

### CR-90  ·  STILL-NEEDED  ·  FA · new batch `B21c-arc` after B21b: CR-91 -> CR-89 (1)(2) -> CR-90 -> CR-88 build -> CR-89 (3)(4) · gate: CR-90's arc instrument per seed + the entry's falsifier · hash: CR-91, CR-88 build and each…

`..._part12.md:194` (handle index row)

| CR-90 | B10-17b | new from the arc fold of 2026-11-05 (`-04`; `ED-IN-0341`): the arc instrument, a harness reader of the first season of each band and mark per seed; hash EQUAL |

`..._part3.md:226` (batch card row)

| CR-90 | The arc instrument: a new harness reader (`python -m engine.season.harness.<name>`, the name chosen at build: `harness/arc.py` is taken by CL-THRUST B0.1's ARC reader) reads per seed the first season of each clock band, breakdown, the first claim, `declare`, civil war, theocratic `declare` and Church `rung.seized`, and whether parliament still determines after the first war; pooled shares with the seed spread; writes nothing (`ED-IN-0341`; `CLAUDE.md` §7's gap; the arc fold of 2026-11-05) | MEASURE (harness) | E | CR-89 | any pass bar is Jordan's | written out in full: `-04` |

`..._part4.md:188` (-04 content-owner entry)

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

### CR-91  ·  STILL-NEEDED  ·  FA · new batch `B21c-arc` after B21b: CR-91 -> CR-89 (1)(2) -> CR-90 -> CR-88 build -> CR-89 (3)(4) · gate: CR-90's arc instrument per seed + the entry's falsifier · hash: CR-91, CR-88 build and each…

`..._part12.md:195` (handle index row)

| CR-91 | B10-17b | new from the arc fold of 2026-11-05 (`-04`; `ED-IN-0317`): the casus-belli carrier, `march`'s claim gate and civil war; IN-36's casus-belli residue merged here; a declared mover |

`..._part3.md:224` (batch card row)

| CR-91 | The casus-belli carrier: a claim to a territory is a Proposition `claim:<faction>:<rung>` on CP-T09-02's war/creed shape, uttered only on a ground from the closed roster `casus_grounds:` (a seizure from the claimant's faction, a seat that once held it, a refused succession, the Church's ground under a held theocratic war); `declare` takes a held claim as occasion; `march`'s gate admits a live claim or a civil war; `faction_q.civil_war` a reading over the vassals' `oblige` edges; at believed breakdown a vassal head's `declare` against the sovereign's faction needs no ground (`ED-IN-0317`; resolves CP-T09-02's and IN-36's carrier gap; the arc fold of 2026-11-05) | BUILD | M (`march` admits fewer) | CP-T09-02, CP-T09-04, CR-86 (landed `83715fd6`) | — | written out in full: `-04` |

`..._part4.md:201` (-04 content-owner entry)

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

### CR-92  ·  STILL-NEEDED  ·  IN · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:196` (handle index row)

| CR-92 | B10-19 | new from the attribute-rulings fold of 2026-11-05 (`-12`; `ED-IN-0347`): the social attributes acting on others (Grace on regard, promotion and the venue standard; Presence on obedience; Attunement on bonds); DESIGN-FIRST |

`..._part3.md:409` (batch card row)

| CR-92 | The social attributes acting on others: Grace on regard, promotion and the venue's standard; Presence on obedience; Attunement on bonds (ED-IN-0347) | DESIGN-FIRST | E (design) | CR-20 (landed `c7764a5a`), CR-84 (landed `1abaa612`) (B10-10, read); SC-02 (design written, PROPOSED), CR-83 (design) | the venue shortfall acting on the result, a take | written out in full: `-12` |

`..._part17.md:13` (-04 content-owner entry)

### CR-92 — The social attributes acting on others: Grace on regard, promotion and the venue's standard; Presence on obedience; Attunement on bonds (SC/IN) · BATCH B10-19 (DESIGN-FIRST; drafted after SC-02's and CR-83's designs are approved; its builds slot by R8) · STATE DESIGN-FIRST · R R-07 (contributor), R-06 (contributor)
- WHAT: AR-29, AR-31, AR-32 to AR-36a, AR-49, AR-50 (ED-IN-0347). How a person's Grace, Presence and Attunement change what OTHERS do and think: Grace makes others think well of him whatever his office's rank (AR-34) and so raises his chance of an office (AR-35); a formal venue requires Grace and penalizes its want even in a persuasive speaker (AR-36, AR-36a); Presence moves others (AR-29), including whether an order is obeyed; Attunement sets the likelihood that a tie or knot forms (AR-31). Today `regard` (`queries/person_q.py:397`) and `reception` (`queries/world_q.py:678`) read no attribute, `roll.py::obstacle` has no venue standard, `comply`/`defy`/`evade` carry no term from the issuer, and the knot oracle gates on Bonds (`systems/fieldwork/sim/knots.py:53, 200`), which the ten drop (adj §1, §2.2 (iv), (ix)).
- LANDED ALREADY: `regard` and its gains; `stance_term`'s `declared` regard of a candidate's subject (`decision/choose.py:55`), which carries regard into `confer` with no change to `confer`; `reception`; `arrangements.yaml`'s keys `interposed`, `order`, `floor`, `venue_min_rank`; by B10-10's close, the ten keys (CR-84) and `Person.attributes` (CR-20).
- REMAINING UNBUILT: (design) ONE design file under `proposals/`, no code, stating with a falsifier each: (1) **how Grace reaches regard** without a person-side reader of another's true attribute: the candidate door is WITNESS (the World may read the true value; the holder reads only what was deposited), the precedent CR-79's credit term; `layer-conformance` Lens B on AX-2 answered first; (2) **promotion**: confirmed through `stance_term`, no `confer` edit, or the design names why not; (3) **the venue standard**: the requirement read from the existing keys (no fourteenth key; `data/arrangements.py` refuses one), and the shortfall demoting the contest result, surplus adding nothing in the venue (adj §3.1 (12)), with its band and the reading rule that chooses any coefficient; (4) **Presence on obedience**: a term on the receiver's `comply` against `defy`/`evade` from the issuer's Presence, as seen by the receiver; (5) **Attunement on bonds**: the formation term IN-32's `tie / knot` effect consumes, and the re-pointing of the knot oracle's Bonds gate (the oracle changes at its owner, re-exported, `CLAUDE.md` §6); (6) the two profiles as its falsifier pair: high Presence, low Grace wins the contest and loses regard; high Grace, low Presence wins regard and loses the contest (AR-49, AR-50).
- GATE: after B10-10's close, landed `0533c4da` (reads CR-20's carrier and CR-84's keys); after SC-02's design (it re-sources `reception`) and CR-83's design (the WITNESS deposit) are approved. Approved by ED-1094's merge default. NEEDS: CR-20 (landed `c7764a5a`), CR-84 (landed `1abaa612`) (B10-10, read, unchanged); SC-02, CR-83 (designs).
- EXIT and FALSIFIER: the file exists and states (1) to (6), each with a falsifier and a control (every term at 0 reproduces the base hash); no code.
- HASH MOVERS: the design none; each build it schedules a declared MOVER, P14.
- HOLES AND LEDGER IDS: ED-IN-0347; H-215 (`reception`'s valence source); ED-SC-0040.
- ASKS ATTACHED: none open. The venue shortfall acting on the result is a ladder take, worth a glance `[ASSUMPTION; medium; Jordan to correct; revert: the shortfall lowers `reception` only]`.
- RE-BASE: `regard`, `reception`, `stance_term`, `obstacle` by symbol; SC-02's and CR-83's approved designs; IN-32's landed effect if built.
- BUILDER: opus; `valoria-author`; its critic per `CLAUDE.md` §10 (Lens B is the judgment node).
- SOURCE: AR-29 to AR-36a, AR-49, AR-50; adj §2.2 (iv), (ix), §3.1 (12), (16), (17); map F11, F12, F16 to F19 (reference).

### CR-93  ·  STILL-NEEDED  ·  IN · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:197` (handle index row)

| CR-93 | B10-19 | new from the attribute-rulings fold of 2026-11-05 (`-12`; `ED-IN-0347`): attributes in a person's own choice (aptitude on uncontested candidates, Focus on the noise of choosing, Reason on the forecast); DESIGN-FIRST |

`..._part3.md:410` (batch card row)

| CR-93 | Attributes in a person's own choice: aptitude on uncontested candidates, Focus on the noise of choosing, Reason on the forecast (ED-IN-0347) | DESIGN-FIRST | E (design) | CR-20 (landed `c7764a5a`) (B10-10, read); CL-PERSON's design if approved | — | written out in full: `-12` |

`..._part17.md:26` (-04 content-owner entry)

### CR-93 — Attributes in a person's own choice: aptitude on uncontested candidates, Focus on the noise of choosing, Reason on the forecast (IN) · BATCH B10-19 (DESIGN-FIRST; drafted after B10-10's close; its builds slot by R8 into the next batch sharing `decision/`) · STATE DESIGN-FIRST · R R-08 (contributor), R-06 (contributor)
- WHAT: AR-04, AR-21, AR-23 (ED-IN-0347). Attributes and capabilities weight a character's choice beside his pursuits and convictions. Today an attribute can reach a choice only through `odds_weight` on a contested candidate (`decision/choose.py:171-195`; `seam/wrappers/sigma.py:146`), the believed odds are exact (`sigma.py:368-419`), and τ is one value for everyone (`choose.py:352`). ED-IN-0261's "identically disposed" sentence is narrowed, not reversed (adj §2.1).
- LANDED ALREADY: `score_terms`, `odds_weight` (CR-17), `_sample_order` (receives the person, `choose.py:243`); by B10-10's close, `Person.attributes` and the `vocation_attribute` rows (CR-20).
- REMAINING UNBUILT: (design) ONE design file under `proposals/`, no code: (1) an aptitude term on an uncontested candidate from the verb's vocation attribute (CR-20's rows), its scale against the pursuit term, and why it is not a second ladder for `odds_weight` on contested ones; (2) a per-person τ falling with Focus (AR-23); (3) an error on the believed chance that Reason shrinks and low Focus widens (AR-21), and how it composes with CL-PERSON's M40 risk term so the two are not two ladders for one quantity (NERS S); (4) obligations and demands named as CR-88's (no term here). Each coefficient is chosen by a stated reading rule over a measured sweep (`python -m engine.season.harness.decision_spread --persons` or the instrument the design names), never asserted.
- GATE: after B10-10's close (CR-20). NEEDS: CR-20 (read, unchanged), CR-17 (landed `1ef8d273`); reads CL-PERSON's design if approved.
- EXIT and FALSIFIER: the file exists and states (1) to (4) with falsifiers: two hand-built persons with equal pursuits and different attributes rank one uncontested candidate differently, and identically with the term at 0; "gates nothing": `opening_set` returns equal sets for the two; CONTROL: every term at neutral reproduces the base hash at seeds 0-2. No code.
- HASH MOVERS: the design none; each build a declared MOVER of every seeded choice.
- HOLES AND LEDGER IDS: ED-IN-0347; ED-IN-0261; ED-IN-0304 (M40).
- ASKS ATTACHED: none open.
- RE-BASE: `score_terms`, `odds_weight`, `_sample_order`, `odds_of` by symbol; CR-20's landed rows; CL-PERSON's state.
- BUILDER: opus; `valoria-author`.
- SOURCE: AR-04, AR-21, AR-23; adj §2.2 (i), §3.1 (14), (15); map F10, F14, F15 (reference).

### CR-94  ·  STILL-NEEDED  ·  FI · U3 B11-fi-readers, first items: CR-29 (row 2 of `U5c_FI_residue.md` §2), CR-94, then CP-T06-09, -01, -03, -04, -02, -07 (row 6), CP-T06-05 (row 9, with `14_VERBS_SOCIAL2_C` §3; U3 places those i…

`..._part12.md:198` (handle index row)

| CR-94 | B10-14 | new from the attribute-rulings fold of 2026-11-05 (`-12`; `ED-IN-0347`): forgery quality reads the forger's Coordination; a declared mover where a forger has authored Coordination |

`..._part3.md:116` (batch card row)

| CR-94 | Forgery quality reads the forger's Coordination (ED-IN-0347, AR-16) | BUILD | E in an all-absent realm; M where a forger has authored Coordination | CR-20 (landed `c7764a5a`), CR-84 (landed `1abaa612`) (read, unchanged) | — | written out in full: `-12` |

`..._part17.md:39` (-04 content-owner entry)

### CR-94 — Forgery quality reads the forger's Coordination (FI/IN) · BATCH B10-14 (first: … → CR-94 → the batch's order as written) · STATE BUILD · R R-05 (contributor: `forge`)
- WHAT: AR-16. `Record.forgery_quality` is written by `_eff_forge` (`loop/effects_information.py:777`) from the fixture `default_forgery_quality` (`data/fixtures.py:499`, H-210), the same for every forger. The forger is the examiner's opposition, so his Coordination enters as an opposition score does: `score/2` (Jordan, 2026-08-14; `modules/social_contest/roll.py:93-97`) `[ASSUMPTION; medium; Jordan to correct; revert: the fixture for everyone]`.
- LANDED ALREADY: `_eff_forge`; `forgery_quality` read as an instance modifier in `obstacle`; by B10-10's close, `Person.attributes` with `attr.body.agility` named Coordination (CR-84, CR-20).
- REMAINING UNBUILT: `_eff_forge` writes `attributes["attr.body.agility"] / 2` when the forger holds the key, else the fixture. Lock-picking has no verb and nothing is built for it (adj §3.1 (18)).
- GATE: after B10-10's close (landed `0533c4da`). NEEDS: CR-20 (landed `c7764a5a`), CR-84 (landed `1abaa612`) (read, unchanged).
- EXIT and FALSIFIER: two hand-built forgers with Coordination 2 and 6 mint sheets of quality 1 and 3, and an examiner's odds against them differ; planted failure: the attribute read dropped makes them equal and reddens. CONTROL: an all-absent realm reproduces the pre-item hash.
- HASH MOVERS: EQUAL in an all-absent realm; a declared MOVER wherever a forger has authored Coordination.
- HOLES AND LEDGER IDS: H-210; ED-IN-0347.
- ASKS ATTACHED: none.
- RE-BASE: `_eff_forge` and `_mint_sheet` by symbol; H-210's swept range (0, 1, 3) against the halved scale (0.5 to 3.5).
- BUILDER: sonnet.
- SOURCE: AR-16; adj §3.1 (18).

### CR-95  ·  STILL-NEEDED  ·  IN · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:199` (handle index row)

| CR-95 | B10-19 | new from the attribute-rulings fold of 2026-11-05 (`-12`; `ED-IN-0347`): Spirit against circumstance and influence; DESIGN-FIRST, run through the resolution diagnostic |

`..._part3.md:411` (batch card row)

| CR-95 | Spirit against circumstance and influence (ED-IN-0347) | DESIGN-FIRST | E (design) | CR-20 (landed `c7764a5a`) (B10-10, read); CR-96 (landed `c0baed2c`); B10-11b (closed) for its combat half | — | written out in full: `-12` |

`..._part17.md:52` (-04 content-owner entry)

### CR-95 — Spirit against circumstance and influence (IN/PC/SC) · BATCH B10-19 (DESIGN-FIRST; its combat half after B10-11b, its social half after SC-02's re-source; builds slot by R8) · STATE DESIGN-FIRST · R —
- WHAT: AR-44. Spirit resists influence and compulsion, tolerates harm and strain, and gets good results despite poor circumstances, "ignoring obstacle modifiers or adding modifiers to dice pool". Combat already reads Spirit as strain (`combatant.py:20, 34-37, 45-47, 147`); resistance and circumstance are absent (adj §1, AR-44 row).
- LANDED ALREADY: `register_pool_addend` (`sigma.py:133`); the instance modifiers (`roll.py:122-130`; combat's wound term `combat_systems.py:1044`, ED-1041); CR-96's `opposed_by` column (landed `c0baed2c`).
- REMAINING UNBUILT: (design) ONE design file under `proposals/`, no code: (1) which verbs are opposed by Spirit (influence and compulsion: the persons-targeted rows CR-20 lands), written as `opposed_by` values on CR-96's column (landed `c0baed2c`); (2) which ADVERSE instance modifiers Spirit discounts, never `base_Ob`, never TN, never below `base_Ob` or `OB_MIN` (adj §2.2 (ii)); (3) whether a pool addend is used anywhere instead; (4) the Grace and Spirit boundary (adj §2.2 (iv)). The design is run through `resolution-diagnostic` and carries its output as evidence (`CLAUDE.md` §9).
- GATE: after B10-10's close; the combat half after B10-11b closes (PC-19's and PC-20's terms change the same sigma); the social half after SC-02's re-source. NEEDS: CR-20 (landed `c7764a5a`) (read, unchanged); CR-96 (landed `c0baed2c`).
- EXIT and FALSIFIER: the file states (1) to (4) with falsifiers; the diagnostic's report shows no composed obstacle below `base_Ob` at any Spirit and modifier; CONTROL: Spirit's terms at 0 reproduce the base hash. No code.
- HASH MOVERS: the design none; (1)'s data edit a MOVER wherever a resisting person has authored Spirit; each build declared.
- HOLES AND LEDGER IDS: ED-IN-0347; ED-1041; ED-IN-0251.
- ASKS ATTACHED: none open `[ASSUMPTION; medium; Jordan to correct; revert: Spirit acts only through a pool addend]`.
- RE-BASE: `_opposition_of`, `obstacle`, the wound term by symbol.
- BUILDER: opus; `valoria-author`; the diagnostic run sonnet.
- SOURCE: AR-44; adj §2.2 (ii), (iv); map F5, F21 (reference).

### CR-97  ·  STILL-NEEDED  ·  WR · B11-F1 (CR-106, CR-107, lane SE/IN) at any point; B11-F2 (CR-104, CR-97..CR-101) before U3 B38; B11-F3 (CR-103) after the docket closes (U3 B27) · gate: the entry's hand-built falsifiers + the s…

`..._part12.md:201` (handle index row)

| CR-97 | B11-F2 | new from the flow-conditioning fold of 2026-11-08 (`-11` §3; `ED-IN-0352`): measure plot points and office influence, columns (a) to (h) on the strands block; hash EQUAL |

`..._part3.md:332` (batch card row)

| CR-97 | Measure plot points and office influence: columns (a) to (h) on `strife.py::strands_block` (turns, closure class, chains in strands, office influence per move, referent breadth, dissemination, presence, the field the stamp would reach, the emergence row), three controls, per-seed spread | MEASURE (harness) | E | `ED-IN-0352`, CR-104 | — | written out in full: `-11` §3 |

`..._part16.md:202` (-04 content-owner entry)

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

### CR-98  ·  STILL-NEEDED  ·  WR · B11-F1 (CR-106, CR-107, lane SE/IN) at any point; B11-F2 (CR-104, CR-97..CR-101) before U3 B38; B11-F3 (CR-103) after the docket closes (U3 B27) · gate: the entry's hand-built falsifiers + the s…

`..._part12.md:202` (handle index row)

| CR-98 | B11-F2 | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): the loops L1 to L5 declared as `LOOP` rows with sign and bound; hash EQUAL |

`..._part3.md:333` (batch card row)

| CR-98 | Declare the loops L1 to L5 as `kind: "LOOP"` rows with `sign:` and a bound (L6, L7 with CR-102, CR-105) | EDIT (register rows) | E | CR-97 | — | written out in full: `-11` §3 |

`..._part16.md:240` (-04 content-owner entry)

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

### CR-99  ·  STILL-NEEDED  ·  WR · B11-F1 (CR-106, CR-107, lane SE/IN) at any point; B11-F2 (CR-104, CR-97..CR-101) before U3 B38; B11-F3 (CR-103) after the docket closes (U3 B27) · gate: the entry's hand-built falsifiers + the s…

`..._part12.md:203` (handle index row)

| CR-99 | B11-F2 | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): a positive control for the strife guard (PASS, FAIL, BLIND over arms); hash EQUAL |

`..._part3.md:334` (batch card row)

| CR-99 | Give the strife guard a positive control: a function over arms returning PASS, FAIL or BLIND, with a planted concentrator | BUILD (harness) | E | CR-98 | — | written out in full: `-11` §3 |

`..._part16.md:266` (-04 content-owner entry)

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

### CR-100  ·  STILL-NEEDED  ·  WR · B11-F1 (CR-106, CR-107, lane SE/IN) at any point; B11-F2 (CR-104, CR-97..CR-101) before U3 B38; B11-F3 (CR-103) after the docket closes (U3 B27) · gate: the entry's hand-built falsifiers + the s…

`..._part12.md:204` (handle index row)

| CR-100 | B11-F2 | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): the unaware's field, `flow_stakes_within` in `questions_for`, shipped off; a declared mover on. The handle is kept and its content replaced (the obstacle term it once named was never filed, P4) |

`..._part3.md:335` (batch card row)

| CR-100 | The unaware's field: `world_q.flow_stakes_within` spliced into `questions_for` through the driver's barrier-2 projection, behind `Fixtures stamp_flow_within`, shipped off | BUILD | E (off); M (on) | CR-97, CR-98, CR-99 | — | written out in full: `-11` §3 |

`..._part16.md:284` (-04 content-owner entry)

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

### CR-101  ·  STILL-NEEDED  ·  WR · B11-F1 (CR-106, CR-107, lane SE/IN) at any point; B11-F2 (CR-104, CR-97..CR-101) before U3 B38; B11-F3 (CR-103) after the docket closes (U3 B27) · gate: the entry's hand-built falsifiers + the s…

`..._part12.md:205` (handle index row)

| CR-101 | B11-F2 | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): flow salience inside `attention_key`'s tiers, shipped at gain 0 |

`..._part3.md:336` (batch card row)

| CR-101 | The field's order: a flow-salience bump inside `attention_key`'s tiers, `Fixtures flow_salience_gain`, shipped 0 | BUILD | E (at 0); M (above 0) | CR-98, CR-99, CR-100 | — | written out in full: `-11` §3 |

`..._part16.md:313` (-04 content-owner entry)

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

### CR-102  ·  STILL-NEEDED  ·  WR · B11-F2 last item · gate: its own gate on CR-97's reading, else recorded NOT BUILT

`..._part12.md:206` (handle index row)

| CR-102 | B11-F2 (CONDITIONAL) | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): office influence on the within-stake, built only if its gate holds on CR-97's reading, else NOT BUILT; shipped at gain 0 |

`..._part3.md:337` (batch card row)

| CR-102 | Office influence on the within-stake: a salience term `flow_office_gain × r`, `r` from `influence_rung`'s kind; shipped 0 | CONDITIONAL: BUILD only if its gate holds on CR-97's reading, else NOT BUILT | E (at 0); M (above 0) | CR-97, CR-100, CR-101, CR-104 | D6 (answered by precedent, revert stated) | written out in full: `-11` §3 |

`..._part16.md:332` (-04 content-owner entry)

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

### CR-103  ·  STILL-NEEDED  ·  WR · B11-F1 (CR-106, CR-107, lane SE/IN) at any point; B11-F2 (CR-104, CR-97..CR-101) before U3 B38; B11-F3 (CR-103) after the docket closes (U3 B27) · gate: the entry's hand-built falsifiers + the s…

`..._part12.md:207` (handle index row)

| CR-103 | B11-F3 | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): evaluate the field route over arms under a decision rule fixed before the run; the shipped arm, if any, a declared mover |

`..._part3.md:352` (batch card row)

| CR-103 | Evaluate the field route: arms OFF, FIELD, FIELD+S on a salience grid, SHUFFLED and (if CR-102 is built) FIELD+S+O, three seasons, seeds 0, 1, 2, under a decision rule with QUANTISATION and WIDE-SPREAD clauses fixed in advance | MEASURE (readings; the selected values shipped in its pin commit) | M (the shipped arm, if any) | CR-97, CR-99, CR-100, CR-101, CR-102 (if built), B10-17, B10-18, B10-18c | — | written out in full: `-11` §3 |

`..._part16.md:351` (-04 content-owner entry)

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

### CR-104  ·  STILL-NEEDED  ·  WR · B11-F1 (CR-106, CR-107, lane SE/IN) at any point; B11-F2 (CR-104, CR-97..CR-101) before U3 B38; B11-F3 (CR-103) after the docket closes (U3 B27) · gate: the entry's hand-built falsifiers + the s…

`..._part12.md:208` (handle index row)

| CR-104 | B11-F2 | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): institutional reach, `faction_q.influence_rung` from the rung an office's institution covers; hash EQUAL |

`..._part3.md:331` (batch card row)

| CR-104 | Institutional reach: `faction_q.influence_rung(w, office_id)`, the lowest rung covering a head seat's institution (its seats, holdings and owned Sites, `owned_site_rungs`); `world_q.lowest_covering` extracted as the one owner (the flow-conditioning fold, `ED-IN-0352`) | BUILD | E | `ED-IN-0352`, CR-106 | — | written out in full: `-11` §3 |

`..._part16.md:182` (-04 content-owner entry)

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

### CR-105  ·  STILL-NEEDED  ·  WR · B11-F3 · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a until CR-103's verdict

`..._part12.md:209` (handle index row)

| CR-105 | B11-F3 (CONDITIONAL, HELD) | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): a choice-score bias toward what is at stake; HELD on CR-103's verdict and Jordan's AX-2 hunk (HELD BACK) |

`..._part3.md:353` (batch card row)

| CR-105 | A choice-score bias toward what is at stake: one term in `decision/choose.py::score_terms` on `Question.stakes`, `flow_choice_gain` shipped 0 | CONDITIONAL and HELD (on CR-103 shipping OFF under "none lifts", and Jordan's AX-2 hunk, HELD BACK) · BUILD when released | E (at 0); M (above 0) | CR-103, the AX-2 hunk | the hunk's text (Jordan's file; a sentence proposed in the entry) | written out in full: `-11` §3 |

`..._part16.md:370` (-04 content-owner entry)

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

### CR-106  ·  STILL-NEEDED  ·  WR · B11-F1 (CR-106, CR-107, lane SE/IN) at any point; B11-F2 (CR-104, CR-97..CR-101) before U3 B38; B11-F3 (CR-103) after the docket closes (U3 B27) · gate: the entry's hand-built falsifiers + the s…

`..._part12.md:210` (handle index row)

| CR-106 | B11-F1 | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): Church-owned building kinds, the `site_owner` table, `owner_of`, the `site:` minting; a declared mover; content HELD BACK (`proposals/2026-11-08-flow-conditioning/`) |

`..._part3.md:315` (batch card row)

| CR-106 | Church-owned building kinds (`worship`, `templar_quarters`, `school`), the `site_owner` table (a kind-row cell naming an owning `factions` member), `faction_q.owner_of`, and the `site:` key that mints a Site from a venue row (the flow-conditioning fold, `ED-IN-0352`) | BUILD; content HELD BACK (first reading) | M | `ED-IN-0352` (landed in the fold) | — (the content is Jordan's to correct, P11) | written out in full: `-11` §3 |

`..._part16.md:131` (-04 content-owner entry)

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

### CR-107  ·  STILL-NEEDED  ·  WR · B11-F1 (CR-106, CR-107, lane SE/IN) at any point; B11-F2 (CR-104, CR-97..CR-101) before U3 B38; B11-F3 (CR-103) after the docket closes (U3 B27) · gate: the entry's hand-built falsifiers + the s…

`..._part12.md:211` (handle index row)

| CR-107 | B11-F1 | new from the flow-conditioning fold (`-11` §3; `ED-IN-0352`): several cohorts per settlement (label, heritage, conviction; the summed ceiling); `faction:` HELD as CR-107b (no row); content HELD BACK |

`..._part3.md:316` (batch card row)

| CR-107 | Several cohorts per settlement: `label:`, `heritage:`, `conviction:` on the cohort row, the id `cohort_<rung>_<label>`, the summed-weight ceiling; `faction:` HELD as CR-107b (the flow-conditioning fold, `ED-IN-0352`) | BUILD (loader EQUAL; content commit a mover); content HELD BACK | E (loader); M (content) | `ED-IN-0352` (landed in the fold); not a dependency: SE-06 (re-bases on it) | — (the content is Jordan's to correct, P11) | written out in full: `-11` §3 |

`..._part16.md:154` (-04 content-owner entry)

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

### PC-21  ·  STILL-NEEDED  ·  PC · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:222` (handle index row)

| PC-21 | B10-19 | new from the attribute-rulings fold of 2026-11-05 (`-12`; `ED-IN-0347`): the opponent model: familiarity grown in the season, Attunement's anticipation, the combatant's state; DESIGN-FIRST |

`..._part3.md:412` (batch card row)

| PC-21 | The opponent model: familiarity grown in the season, Attunement's anticipation, the combatant's state (ED-IN-0347) | DESIGN-FIRST | E (design) | PC-06 (K-1, landed `2c7f2658`), PC-14 (landed `6732111a`); B10-11 | — | written out in full: `-12` |

`..._part17.md:65` (-04 content-owner entry)

### PC-21 — The opponent model: familiarity grown in the season, Attunement's anticipation, the combatant's state (PC/IN) · BATCH B10-19 (DESIGN-FIRST; drafted beside B10-11b; its builds slot by R8 into the next batch editing `modules/combat` and `seam/wrappers/combat.py`) · STATE DESIGN-FIRST · R —
- WHAT: AR-38, AR-39, AR-41, AR-42, AR-43, AR-45 to AR-48. Familiarity is two module constants keyed by tradition labels (`modules/combat/traditions.py:30-56`), read at `combat_systems.py:1128, 1057, 1059`; a missed read guesses uniformly (`:1136`); no quantity reads the opponent's state or nearness to yielding.
- LANDED ALREADY: `TR.familiarity`, `read_contest`, `disp_lean`; PC-10a's `yield` terms (`wrapper.py:508`); `world_q.practice` (`:4095`), the derived-from-the-log precedent; PC-06's K-1 (B10-11b).
- REMAINING UNBUILT: (design) ONE design file under `proposals/`, no code: (1) familiarity as a per-bout input set by the seam (AR-47, AR-48), derived from the holder's own past fights against that weapon class (`wclass`) and his tradition's skills, storing nothing (adj §2.2 (viii)); the label function stays the module default for un-seamed callers; where a person's tradition lives (no `Person` carrier exists; CR-33's keys are the candidate); (2) the anticipation on a missed read, combining familiarity, the defender's Attunement and the opponent's visible state, and its effect on the draw order (the `modes[rng.randrange(3)]` contract, `:1133-1136`); (3) the opponent's state composed from what the module already tracks (fatigue, wounds, poise, initiative, `disp`) before any new quantity is coined (AR-38); (4) nearness to yielding read against PC-10a's threshold, and its consumer, or the statement that it has none yet (AR-42).
- GATE: after B10-10's close and B10-11's (kit, CR-85's build, PC-10); drafted beside B10-11b. NEEDS: PC-06's K-1 (landed `2c7f2658`), PC-14 (landed `6732111a`).
- EXIT and FALSIFIER: the file states (1) to (4) with falsifiers: at least, a fighter with a record of fights against a weapon class reads it better than one without, and equally at no record; an attuned defender's missed-read guess beats a uniform one against a fixed-disposition opponent and not against a neutral one; CONTROL: every term at its control reproduces the base hash and the combat pins. No code.
- HASH MOVERS: the design none; each build declared.
- HOLES AND LEDGER IDS: ED-IN-0347.
- ASKS ATTACHED: none open; `wclass` and the derived store are takes (adj §2.2 (viii)).
- RE-BASE: the read sites and `traditions.py` by symbol; K-1's seam.
- BUILDER: opus; `valoria-author`.
- SOURCE: AR-38 to AR-48; adj §2.2 (viii), §3.1 (21), (22); map F8, F23 (reference).

### PC-22  ·  STILL-NEEDED  ·  PC · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:223` (handle index row)

| PC-22 | B10-19 | new from Jordan, 2026-11-07 (`-12`): sparring, a non-lethal venue that pays Concentration and pairwise familiarity, once a season; DESIGN-FIRST |

`..._part3.md:413` (batch card row)

| PC-22 | Sparring: a non-lethal venue that pays Concentration and pairwise familiarity, once a season (Jordan, 2026-11-07) | DESIGN-FIRST | E (design) | PC-21; PC-20 (landed `4b334f2a`) | — | written out in full: `-12` |

`..._part17.md:78` (-04 content-owner entry)

### PC-22 — Sparring: a non-lethal venue that pays Concentration and pairwise familiarity, once a season (PC/IN) · BATCH B10-19 (DESIGN-FIRST; drafted after PC-21's design is approved and B10-11b has closed; its build slots by R8 into the next batch editing the verb cluster, P13) · STATE DESIGN-FIRST · R —
- WHAT: Jordan, 2026-11-07, this session: *a verb that allows a non-lethal fight, without wounds carried into the season loop, between two individuals*; *a venue in which characters and the player fight without lethal consequences and get practice and experience*; the payoff is *pairwise familiarity and a marginal capability raise*; *you can do it once per season*. A new contested verb `spar`, distinct from `train` (uncontested, one vocation raised by one, no scene: `loop/effects_combat.py::_eff_train`).
- LANDED ALREADY: `rosters.yaml: duel_terms` and `DUEL_TERMS` (`yield`, `blood`, `death`; `capture: yield`, `accept: blood`); `loop/effects_combat.py::_grown` and `raised_capability` (build by doing, CP-T03-04 (iv): +1 whole point on a key the person already holds, never minted, only where blood was drawn); REM-31 and IN-46's `decide` (`modules/combat/fight.py`); `world_q.practice` (the derived-from-the-log precedent).
- REMAINING UNBUILT: ONE design file under `proposals/`, no code: (0) ONE THING, ONE NAME (Jordan, 2026-11-07: *concentration, focus, nerve, composure, whatever we are using in whatever places* all tie into it). The name is CONCENTRATION: the reserve the module already keeps (`conc`, `conc_max = 3F + 2S`), whose inputs are the attributes Focus (`attr.mind.focus`) and Spirit (`attr.mind.will`). *Nerve*, *calmness* and *composure* are plain words for it and are not coined as terms here; `consistency`, `mental_fatigue` and `LAPSE_K` are three code names for its effects, which (3a) asks to be one. The design file's glossary maps every place the tree says one of these words to this one quantity, or shows that place is a different thing (`poise`, the balance state, is not asserted to be the same without reading it). (1) a `spar` row (`contests:` the body prize, V-2; `writes:` its own, below) and a `duel_terms` line (`spar: yield` `[ASSUMPTION; medium; Jordan to correct; revert: blood]`); (2) `_eff_spar` writes no `Person.body` (the `fight` and `accept` effect writes it from the scene's `wound_state`), so no wound is carried; (3a) THE PRINCIPLE (Jordan, 2026-11-07: *everything in a fight, from reading your opponent to defending with the weapon to attacking, is impacted by the character's mental state; being nervous, anxious or inexperienced is very bad because execution is not to the calibre it should be, which is why experience matters: you do not feel as much of the PRESSURE of the moment or of your opponent*). Read against the module as it stands: mental state reaches execution through THREE separate formulas, all keyed on the depleting concentration reserve and none on experience or on the pressure of the moment: `consistency` (`combat_systems.py::consistency`) enters the aggressor's read and `attack_sigma`; `mental_fatigue` scales the defender's read (`MENTAL_FAT_READ_K`) and `defence_sigma` (`MENTAL_FAT_DEF_K`); PC-19's `LAPSE_K*consistency` enters `mode_sigma` (B10-11b, landed). So a fresh novice and a veteran at the same authored Focus and Spirit execute alike while the reserve is full; PC-19's term is 0 only at the default reserve of 15 (`3F + 2S`), and K-1 now feeds authored scores on the registry's 1 to 7 scale (midpoint 4) against combat defaults of 3, so an average authored fighter is fresh at a small positive term and the lapse acts as a static Focus bonus before any hit lands, not as a lapse; the principle is not yet carried. The design states ONE quantity, the pressure a fighter feels, its inputs (the stakes of the scene, `terms` lethal against `yield`; wounds taken; the opponent's menace, read from what the module already tracks, PC-21 (3)) and the experience that attenuates it, and ONE execution penalty from it applied at every execution step (the read, the response, the attack) through one owner, and the ruling on the three code names is made: `consistency`, `mental_fatigue` and `LAPSE_K` ARE ONE (Jordan, 2026-11-07: *concentration, consistency, mental_fatigue and lapse_k should all become one, a composite of your focus, your spirit/willpower AND your amount of experience*). ONE function of three inputs, Focus, Spirit and experience (the log-derived term of (3)), is the Concentration the reserve, the read, the response and the attack all read; the build retires `consistency`, `mental_fatigue`, `LAPSE_K`, `FOCUS_CONSISTENCY_K` and `FOCUS_MENTAL_K` as separate readers and keys (each site keeps one swept weight on the one function, which is its own, not a second ladder). Whether the reserve keeps depleting by pain per hit (`CONC_DRAIN_HIT`) with experience raising its ceiling and slowing the drain, or experience enters only the ceiling, is the design file's take `[ASSUMPTION; medium; Jordan to correct; revert: depletion unchanged, experience in the ceiling only]`; the re-point is a declared mover of every fight, and PC-19's `LAPSE_K` (B10-11b, landed at 0.05) is a transitional key it replaces, so the combat pins re-record again at that build.  A spar is low-pressure by its terms, so it attenuates less per exposure than a fight, which is the *marginal* in Jordan's word and why a better partner (more menace) pays more `[ASSUMPTION; medium; Jordan to correct; revert: a flat step per spar]`. (3b) THE PRESSURE FUNCTION (Jordan, 2026-11-07: *a function called pressure, from the difference in martial capability and experience between combatants, which speaks towards why someone with a lot of training can still be intimidated by someone who is a martial Master*). It is the opponent's term of (3a)'s pressure: a function of the two fighters' STANDINGS, each a combination of martial capability (the party's `faculty` for the verb, already on `PersonalCombatInput.faculties`, CR-85) and experience (the log-derived term of (3), nothing stored), whose value is the gap by which the opponent exceeds him. It is computed at the seam, where both parties are known, and handed to the module as a typed per-bout input beside PC-21 (1)'s familiarity (the module keeps no game state and sees one party's standing only through its Combatant). It is felt by the lesser fighter and is not mirrored: the Master feels none from the veteran `[ASSUMPTION; medium; Jordan to correct; revert: a signed term]`. It is NOT removed by training: a veteran facing a Master still feels the gap, and his own experience attenuates the felt value without zeroing it (3a), which is the case Jordan names. How capability and experience combine into one standing, and the bound on the value, are takes of the design file, swept `[SIM-CALIBRATE]`. The function takes two standings and returns a number; its use at any scale other than a fight (a social contest, a levy) is not asserted here. (3) WHAT THE EXPERIENCE WRITES (Jordan, 2026-11-07: *experience from fighting should write moreso to whatever in the system governs calmness, nerves, composure, concentration while fighting, as that is the real thing it gives you, not increased technique and martial prowess itself*). In the module that is Focus (`attributes.SPEC` `focus`, `attr.mind.focus`: the concentration reserve `conc_max = 3F + 2S`, `consistency` and PC-19's lapse, poise recovery `combat_systems.py` `POISE_FOCUS_K`) and Spirit (`spirit`, `attr.mind.will`, the reserve's other term); no season carrier holds either as a quantity that play can change, because `Person.attributes` is authored once and NEVER WRITTEN IN PLAY (CR-20; no `write_matrix.yaml` row). Two carriers, one taken: (b) TAKEN, `[ASSUMPTION; medium; Jordan to correct; revert: (a)]`: Concentration's experience term is DERIVED from the log, nothing stored (the rule PC-21 (1) and (4) use, `world_q.practice`'s precedent): the THIRD INPUT of (3a)'s one function beside Focus and Spirit (not a step added onto them), a bounded swept term from the person's spars and fights survived, passed at the seam beside K-1's map, with the margin rule above applied to it (a spar counts toward it only against a partner whose Concentration is at least his own); (a) HELD FOR JORDAN: a write row on `attr.mind.focus` and `attr.mind.will`, which lifts CR-20's authored-only rule and overwrites a ratified shape, so it is not taken here. The `arms` raise (`_grown`, CP-T03-04 (iv), built and shipping) shrinks from the main effect to a smaller step or none (*moreso*, read as primary and not exclusive `[ASSUMPTION; medium; Jordan to correct; revert: arms as it is]`); re-pointing `_grown` is a declared mover of every fight that draws blood, scheduled with this build and not before. SPARRING BUILDS THE EXPERIENCE TERM BUT CAPS (Jordan, 2026-11-07: *sparring helps build this experience, but it does cap*): the term is the sum of two derived parts, the spars a person has had and the fights he has survived, and the SPARRING PART HAS ITS OWN CEILING, below the term's overall bound, so a person who only ever spars reaches the ceiling and goes no further, while a fight survived raises the term past it (a spar is low-pressure by its terms, (3a), which is why it cannot carry a person the whole way) `[ASSUMPTION; medium; Jordan to correct; revert: no separate ceiling, the margin rule and once per season alone]`. The ceiling is a swept value `[SIM-CALIBRATE]`. It makes the margin rule above and once per season two further limiters on the same farming; the design file says whether the margin rule is still needed beside the ceiling (the cut test, `ners`). `spar` carries ITS OWN WRITE ROW (Jordan, 2026-11-07: *spar needs own write row*): the spar event Concentration's experience term and familiarity are derived from is declared on `spar`'s row, not borrowed from `fight`'s band writes, so the fold runs the effect at every band, an untouched spar included (`_grown` runs only where blood was drawn because a fight's `Untouched` band writes nothing and the gate refuses a no-op write); (4) pairwise familiarity: derived from the log of spars between the pair, storing nothing (PC-21 (1)'s rule), read by the seam as the per-bout familiarity input; (5) once per season, per person `[ASSUMPTION; medium; Jordan to correct; revert: per pair]`: no existing per-season act limit was found, so the design names its owner (a candidate: derived from the log, a person with a spar this season is declined at formation, `world_q.practice`'s precedent, no counter stored); (6) the player: the per-turn `decide` surface for the player's person in a spar (unverified end to end); (7) chooser formation, and the realm run that shows it executing (`CLAUDE.md` §0.2).
- GATE: B10-11b closed; PC-21's design approved. NEEDS: PC-21; PC-20 (landed `4b334f2a`).
- EXIT and FALSIFIER: the file states (1) to (7) with falsifiers, at least: a spar leaves both parties' `body` as it was; a person sparring a partner with less Concentration than himself gains no step and one sparring a partner with more gains it; a spar that ends untouched still pays and still emits its event; a second spar by one person in one season is declined; a pair's familiarity after a spar reads above no record, and a replay from the log reproduces it; at the same authored Focus and Spirit and a full reserve, a novice's read, response and attack under one pressure each fall below a veteran's, and equally at zero pressure and at no record. A person who spars every season reaches the sparring ceiling and no further across further seasons, and one fight survived then raises the term past it; planted failure: the ceiling removed, the spar-only person keeps rising. At equal standings (3b)'s value is 0; a veteran facing a Master executes below his own execution against an equal at the same stakes, and the Master facing the veteran does not; planted failure: the standing gap dropped, the veteran executes alike against both. CONTROL: the row absent reproduces the base hash. No code.
- HASH MOVERS: the design none; the build is a declared mover (a new verb in the cluster).
- HOLES AND LEDGER IDS: none allocated (P4).
- ASKS ATTACHED: none open; the three bracketed takes above.
- RE-BASE: `_grown`, `duel_terms`, `_eff_fight`'s body write by symbol; PC-21's landed design.
- BUILDER: opus; `valoria-author`.
- SOURCE: Jordan, 2026-11-07; CP-T03-04 (iv); CR-87 (RS-25); PC-21.

