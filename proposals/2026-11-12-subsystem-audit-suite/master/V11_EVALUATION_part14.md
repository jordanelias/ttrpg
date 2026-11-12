# Evaluation of workplan v11, part 14: lane E4, carry-forward blocks (verbatim)

## Status: EVALUATION RECORD, assembled (stage 5 of `STAGES.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when workplan v12 is adopted)

**What this part is.** The carry-forward blocks of lane E4, copied by script from `master/eval/E4.md` lines 3453 to 4384, byte for byte; nothing below the rule was retyped or edited. Line numbers cited in the settlement ledger (`V11_EVALUATION_part2.md`) are those of the lane file, so a row of this part is found there as `E4:<line>`. Where the ledger re-dispositions a row, the ledger governs and the copy below keeps the lane's original call as the record.

---

### FA-01  ·  STILL-NEEDED  ·  FA · U3 B21 after `06_FA_shortest_loop_B`, once CR-29 (the FI carry) · gate: the trade-demand clause's falsifier · tier: sonnet

`..._part12.md:225` (handle index row)

| FA-01 | B10-17 | carried v9 position (`-04`) |

`..._part3.md:209` (batch card row)

| FA-01 | #445 P-3; FORCE-FOREIGN's cast: seat faction heads, let a head act, give the foreign faction a demand | The trade-demand clause only, released from M11 (ED-IN-0300) and built after CR-29 (B10-14) · LANDED-NARROWED (mechanism and content landed; what remains is the trade-demand clause, which waits on CR-29; `ED-IN-0298` stays open as a build, its §C.6 authorization answered by ED-IN-0300) | M | CR-29 | — | carried in full: `-04` |

`..._part5.md:113` (-04 content-owner entry)

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

### FA-03  ·  STILL-NEEDED  ·  FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:226` (handle index row)

| FA-03 | B10-Z | carried v9 position (`-04`) |

`..._part3.md:427` (batch card row)

| FA-03 | #453 §10.2: faction actions mapped to person acts | HELD · LEAVE (reference) | E | — | — | carried in full: `-04` |

`..._part5.md:166` (-04 content-owner entry)

### FA-03 — #453 §10.2: faction actions mapped to person acts (FA) · BATCH B10-Z · STATE LEAVE (reference) · R —
- WHAT: the table maps each entry of `references/action_vocabulary.yaml` (25 per #453 §10.2; `status: provisional`) and the acts it lacks to seat-holders' acts or to members' acts counted by a Query; "its own closing line is that no row needs a faction to act. It is reference for IN-12's builds, not a position, and it is why `ED-FA-0002` was cut."
- LANDED ALREADY: —. Nothing to build.
- REMAINING UNBUILT: nothing; it stays reference.
- GATE: none (DEPS none; EDITS none). Slots only if the falsifier below is read.
- EXIT and FALSIFIER: EXIT "`git grep -n action_vocabulary -- engine` returns nothing (read 2026-10-06); the one reader outside documents is `skills/valoria-vector-audit/scripts/vector_audit.py:286`, an audit script that resolves nothing at runtime." FALSIFIER "a path under `engine/` that reads `references/action_vocabulary.yaml` makes the vocabulary a mechanism and the 'reference' label wrong."
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: ED-FA-0002 (cut); no hole rows.
- ASKS ATTACHED: none.
- RE-BASE: none found.
- SOURCE: `v9_p7:127-132` (SOURCE there: `proposals/2026-10-03-verb-coverage-and-gap-fill.md:2359-2411`; `references/action_vocabulary.yaml:32-60`); state-index row `v9.md:294`.

### FA-07  ·  STILL-NEEDED  ·  FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:227` (handle index row)

| FA-07 | B10-Z | carried v9 position (`-04`) |

`..._part3.md:428` (batch card row)

| FA-07 | the original design's faction-vs-faction mechanisms; the second decision round restates five of its row texts onto lawful forms (Piety Track, Church Attention, Deniability Debt, Guild Favour and Schism, Parliament seats and the Sacred Veto) and records five named residues and two refusals on it (`-04` FA-07) `[revert: restore the five texts]` | HELD · LEAVE (named, unscheduled; a row becomes a position when a design reads its surface) | E | — | — | carried in full: `-04` |

`..._part5.md:178` (-04 content-owner entry)

### FA-07 — the original design's faction-vs-faction mechanisms (FA) · BATCH B10-Z · STATE LEAVE (named, unscheduled; a row becomes a position when a design reads its surface) · R —
- SECOND DECISION ROUND (item 5, translate the board-game aggregates, `-05` §1b; still LEAVE in B10-Z): five row texts of the v9 table below are corrected by the translation rule: Piety Track → the share of a territory's residents whose live `commit` is to the Church's Proposition (form F3); Church Attention → each Church seat-holder's own attention over his own ledger (F1; no pooled Query); Deniability Debt → no Query: the debt is the claims themselves, each read by its holder (F1); Guild Favour and Schism → each member's own regard (F1) and the members' `release` edges (F3); Parliament seats and the Sacred Veto → CR-34's live-commit tally at `parliamentary_debate` once CR-38 seats a bench; the seats are unbuilt (H-90) and the Veto is a residue. Named residues recorded here: the Parliamentary Stay (trigger: H-90's Parliament seated); the postmortem tribunal (no reader: a dead accused holds no edge); seizure modifiers by others' instruments (trigger: a `seize` matter on a docket); Church levies (trigger: CP-T09-07's obligee army); GD-2's mandatory muster (trigger: H-224's input reaching governors). Refused (`-05` §1b's refusals): the Gransol exception (RF-8, a rule keyed on a named entity) and the Policy Instrument (RF-4 and RF-1: a faction as actor, and a stored aggregate). Not engaged: Jordan's "ratcheting of Church as faction until it attempts to seize lands" (`rosters.yaml:2606`), whose lawful form would be F3 over Church `commit` and `hold` edges; no position takes it. `[ASSUMPTION; medium; Jordan to correct; revert: restore the five texts]`
- WHAT: Keep named, unscheduled, the faction-vs-faction mechanisms of the original design that no position owns (Church Influence, Piety Track, Church Attention, Altonian pressure, Autonomy, Deniability Debt, and others). Every stored clock is refused; each becomes a Query over existing carriers, banded only under T-b.
- LANDED ALREADY: as the per-row gates above show (B-Q, B-V, B-X rows landed their gates); no row is itself built as a position.
- REMAINING UNBUILT: [v9 WHAT, full text: one row per mechanism of the original design's faction work not already owned by a position (A-37 lists the owned ones). "Every stored clock is refused (T-a, T-c, A-29); each becomes a Query over existing carriers, banded only under T-b." Rows (mechanism: Layer-1 form · surface needed · gate): Church Influence: Query over Church holds, seats, members and territory piety · `faction_q.resolve` (landed) and the piety Query · SE-06. Piety Track: `piety_of(w, territory)` over residents' affiliation intensities · SE-06's temperaments, IN-64's convictions · SE-06. Church Attention: Query over the `deed_doers engaging` claims Church seat-holders hold · IN-67 · B-X. Altonian pressure (IP): Altonian head's own windowed estimate of realm weakness · IN-36, FA-01's clause (`ED-IN-0298`), IN-23 (landed `c4eb6f84`) · B-Z. Löwenritter Autonomy: Ehrenwall's regard of the King, banded under T-b; the Split is her `release` · FA-04, `regard` (with IN-58's grievance, `3bf936ee`) · B-X. Deniability Debt: Query over claims others hold about covert acts · `conceal` (IN-12 step 10, `67686661`) · B-Q. Warden's Accord: regard between heads · none (Wardens stay unplaced by Jordan's 2026-09-14 ruling, `harness/populated.py:760-773`). Parliament seats and the Sacred Veto: arrangement plus a Mandate Query · SC-01 (landed), IN-23 (landed) · landed. Mission shift: head's `utter` of an OUGHT plus members' `commit`/`release` · IN-66..IN-68, IN-11 · B-X. Leadership Deviation cost: cost on an act against one's org's goal · IN-69's `alignment` · B-X. Guild Favour and Schism: members' regard and holdings · B-V's Guilds head (`test_fa01_head_seats.py`'s `LEADERLESS` until then) · B-V.] every row, as a position.
- GATE: LEAVE; DEPS per row; EDITS none. A row becomes a position when a design reads its surface, slotted by `_part3` §B.0 (v10: its R8 step).
- EXIT and FALSIFIER: "a row that becomes a position takes its own; `git grep -n "piety\|church_influence\|attention_pool" -- engine/season ':!*cases*'` returning a stored field is the defect (T-a)".
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: none; A-29, A-33 (named residue FA-07: deviation COST and Mission shift as acts), A-37, T-a, T-b, T-c.
- ASKS ATTACHED: none.
- RE-BASE: the per-row gates cite B-Q (`conceal`), B-V (Guilds head), B-X (IN-66..IN-69, FA-04..FA-06; the batch is RS-30), all closed; the rows' "B-X" and "B-V" gate words are now landed. Whether each landed gate makes its row buildable is not examined in v9 [INFERRED]. None else found.
- SOURCE: `v9_p7:136-140`; note on FA-04..FA-07 at `v9_p7:134`; state-index row `v9.md:295`.

### GO-01  ·  STILL-NEEDED  ·  GO · U3 B03-hygiene last items (IS-B3-GO-01..: the four early landings GO-01, GO-11, GO-05, GO-09, each hash EQUAL with a `--check`) · gate: the exporter's `--check` named in the entry · hash: EQUAL…

`..._part12.md:228` (handle index row)

| GO-01 | B10-20 | carried v9 position (`-04`); released whole: the version owner only (`references/engine_series.yaml`, read by `tools/export_game_constants.py`), once `ED-GO-0002` is on `main` |

`..._part3.md:374` (batch card row)

| GO-01 | `26` GO-VERSION: the ruled engine version where code reads it (released whole; the tenth attribute's name returned to Jordan, J-T2, now answered by `ED-IN-0328`; GO-01 never waited on it) | BUILD: `references/engine_series.yaml` holds `engine_series: "4.7"` (a comment citing ED-GO-0002), read by `tools/export_game_constants.py` (the exporter owns no value) and emitted in `game_constants.json` under a bumped `schema_version` (1 → 2); a GO-06 item records the key change | E | —; ED-GO-0002 on `main` (B10-01's entry action) | — | carried in full: `-04` |

`..._part5.md:191` (-04 content-owner entry)

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

### GO-05  ·  STILL-NEEDED  ·  GO · U3 B03-hygiene last items (IS-B3-GO-01..: the four early landings GO-01, GO-11, GO-05, GO-09, each hash EQUAL with a `--check`) · gate: the exporter's `--check` named in the entry · hash: EQUAL…

`..._part12.md:229` (handle index row)

| GO-05 | B10-20 | carried v9 position (`-04`); M13 hold released |

`..._part3.md:375` (batch card row)

| GO-05 | SM-13: the manifest resource lists module paths (M13 released): the manifest of module entry files derived from `composition.json` (ED-IN-0017 F1) and a test that every listed path exists; the `.gd` RESIST re-export half lapses with PC-05 | BUILD | E | GO-01, GO-12 | — | carried in full: `-04` |

`..._part5.md:204` (-04 content-owner entry)

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

### GO-06  ·  STILL-NEEDED  ·  GO · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: the `valoria-game` checkout

`..._part12.md:230` (handle index row)

| GO-06 | B10-20 | carried v9 position (`-04`); listed in B10-20, HELD · BLK (another repository) |

`..._part3.md:378` (batch card row)

| GO-06 | cross-repo: `valoria-game`'s parity reader against the shrunk `MAPPING`; the stale `game_constants.json` sentence; gains GO-01's `engine_series`/`schema_version` item | HELD · BLK:`valoria-game` checkout (another repository: the parity run is done, the hand refresh of the port's copy is not) | E | — | — | carried in full: `-04` |

`..._part5.md:216` (-04 content-owner entry)

### GO-06 — cross-repo: `valoria-game`'s parity reader against the shrunk `MAPPING`; the stale `game_constants.json` sentence (GO) · BATCH B10-20 (listed, HELD · BLK; moved from B10-Z) · STATE BLK:`valoria-game` checkout (another repository: the parity run is done, the hand refresh of the port's copy is not) · R —
- WHAT: the coherence reshape retired the `COHERENCE_*` pairs from `tools/export_game_constants.py`'s `MAPPING`. Confirm `valoria-game`'s `tools/check_constants_parity.py` (or equivalent) tolerates a smaller `MAPPING` rather than a fixed constant count, and that its generated `game_constants.json` stops carrying the sentence that named a deleted module. GO-01 adds one item: the reader learns the new `engine_series` key and the bumped `schema_version` (1 → 2). "Nothing here edits the other repository."
- LANDED ALREADY: the reshape on this side (WR); the parity reader's tolerance of a smaller `MAPPING`, run at PC-12 against a scratch copy of `valoria-game@6b0df3d`.
- REMAINING UNBUILT: the hand refresh of the port's `resources/generated/game_constants.json` (another repository); GO-01's `engine_series` key when it lands.
- GATE: a `valoria-game` checkout. DEPS WR (the reshape); EDITS none here.
- EXIT and FALSIFIER: EXIT "here, `python tools/export_game_constants.py --check` exit 0; there, its parity check run against this repository's re-derived constants." FALSIFIER "its parity check, run against a `MAPPING` smaller by the retired pairs, fails if it assumes a fixed count; a pass with the pairs present proves nothing about the smaller set."
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: none. (SOURCE row "Port-bridge constants-parity risk from the coherence reshape" in `registers/handoffs/HANDOFF_WR.md`.)
- ASKS ATTACHED: none.
- RE-BASE: none found. The version is ED-GO-0002's (GO-01 writes it to its owner); this entry asserts nothing beyond GO-01's key. B10-20's exit line 9 (Jordan's side) reads this item.
- SOURCE: `v9_p7:108-113`; state-index row `v9.md:291`.

### GO-08  ·  STILL-NEEDED  ·  GO · U3 B41-go-port-gate; B41's content-owner entry carries `11_GO_port_gate_order_and_coverage.md` §1, §2, §5 as its own text (GO-12's scope = every `os.environ` read under `modules/`, built in B17,…

`..._part12.md:232` (handle index row)

| GO-08 | B10-20 | port gate (`-04`): the oracle pins export (`--check`), with the primitives and integer-contract vectors |

`..._part3.md:376` (batch card row)

| GO-08 | The oracle pins export (port gate): `tools/export_oracle_pins.py` (`--build`/`--check`) writes `engine/engine_params/oracle_pins.json` (per seed 0-2 the build hash, the initial world in GO-07's encoding, the slice 1 and slice 2 traces, the draw log's digest, the executed-function list, the `primitives` block and the integer contract vectors; no Mersenne Twister vectors); `port_oracle.py` prints one line per pin; blocking in CI | BUILD | E | GO-07, GO-09, GO-10, GO-12, GO-16 | — | written out in full: `-04` |

`..._part5.md:10` (-04 content-owner entry)

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

### GO-09  ·  STILL-NEEDED  ·  GO · U3 B03-hygiene last items (IS-B3-GO-01..: the four early landings GO-01, GO-11, GO-05, GO-09, each hash EQUAL with a `--check`) · gate: the exporter's `--check` named in the entry · hash: EQUAL…

`..._part12.md:233` (handle index row)

| GO-09 | B10-20 | port gate (`-04`): the season registries export (`--check`) |

`..._part3.md:369` (batch card row)

| GO-09 | The season registries export (port gate): `tools/export_season_registries.py` (`--build`/`--check`) writes every file `data/files.py` names that the loader reads, plus `DEFAULT_FIXTURES`, to `engine/engine_params/season_registries.json`; blocking in CI | BUILD | E | — | — | written out in full: `-04` |

`..._part5.md:23` (-04 content-owner entry)

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

### GO-10  ·  STILL-NEEDED  ·  GO · U3 B41-go-port-gate; B41's content-owner entry carries `11_GO_port_gate_order_and_coverage.md` §1, §2, §5 as its own text (GO-12's scope = every `os.environ` read under `modules/`, built in B17,…

`..._part12.md:234` (handle index row)

| GO-10 | B10-20 | port gate (`-04`): refusal values as typed Results |

`..._part3.md:370` (batch card row)

| GO-10 | Refusal values as typed Results (port gate): the control-flow `except` sites that turn an exception into a game outcome return a typed `{code, needs, law}` record, `code` a closed roster; the §C.12 Result-shape hunk (Layer 1) lands with GO-10, in that PR, listed under 'Layer 0/1 hunks' (D-1 confirmed, ED-IN-0300; a (RULED) mark at the anchor stops that row) | BUILD | E | — | — | written out in full: `-04` |

`..._part5.md:35` (-04 content-owner entry)

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

### GO-11  ·  STILL-NEEDED  ·  GO · U3 B03-hygiene last items (IS-B3-GO-01..: the four early landings GO-01, GO-11, GO-05, GO-09, each hash EQUAL with a `--check`) · gate: the exporter's `--check` named in the entry · hash: EQUAL…

`..._part12.md:235` (handle index row)

| GO-11 | B10-20 | port gate (`-04`): `module_contracts.yaml` re-derived from code |

`..._part3.md:371` (batch card row)

| GO-11 | `module_contracts.yaml` re-derived from code (port gate): `wiring:` (`key-log` replaced), `engine_clock`'s `[ASSUMPTION]` state row, `sim_module:` for `social_contest` and `mass_battle`, `golden_path:`; `accounting_sequence:` deleted if no reader | EDIT | E | —; not a dependency: GO-14 (the `golden_path:` edit is GO-11's and does not need the deletion) | — | written out in full: `-04` |

`..._part5.md:47` (-04 content-owner entry)

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

### GO-12  ·  STILL-NEEDED  ·  GO · U3 B41-go-port-gate; B41's content-owner entry carries `11_GO_port_gate_order_and_coverage.md` §1, §2, §5 as its own text (GO-12's scope = every `os.environ` read under `modules/`, built in B17,…

`..._part12.md:236` (handle index row)

| GO-12 | B10-20 | port gate (`-04`): the seam port items |

`..._part3.md:372` (batch card row)

| GO-12 | The seam port items (port gate): an explicit provider list; `rngsource.py`'s fallback to the process-global `random` refuses; provider `status` a closed roster; `registry.resolve` refuses a missing contract; `os.environ`-read module flags frozen into exported values | BUILD | E | GO-11 | — | written out in full: `-04` |

`..._part5.md:60` (-04 content-owner entry)

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

### GO-15  ·  STILL-NEEDED  ·  GO · U3 B41-go-port-gate; B41's content-owner entry carries `11_GO_port_gate_order_and_coverage.md` §1, §2, §5 as its own text (GO-12's scope = every `os.environ` read under `modules/`, built in B17,…

`..._part12.md:239` (handle index row)

| GO-15 | B10-20 | port gate (`-04`): FREEZE |

`..._part3.md:377` (batch card row)

| GO-15 | FREEZE (port gate): re-take every pin on the merged tree; write the `ED-GO-` freeze row (oracle SHA, the pins digest, the draw log's digest, the freeze list); run this card's exit | MEASURE | E | GO-09, GO-10, GO-11, GO-12, GO-16, GO-01, GO-05, GO-08 | — | written out in full: `-04` |

`..._part5.md:72` (-04 content-owner entry)

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

### IN-18  ·  STILL-NEEDED  ·  IN · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:243` (handle index row)

| IN-18 | B10-Z (HELD; its MEASURE closed at B10-02) | carried v9 position (`-04`), narrowed |

`..._part3.md:437` (batch card row)

| IN-18 | G5, G8, the gated tail (telling workplan residue), narrowed at B10-02's close | HELD · the MEASURE landed (`harness/obligee_report.py`, `165d355c`; survivors-only floor, stated in the module): headline M0e 0 / 0 / 0 at seeds 0 / 1 / 2 over four realm seasons (G5 HELD), the workplan's own M0e (`inferred_about_person`) 4 / 18 / 4 (above 0: its Stop-if, the site `_from_inferred_claim` not derived); G5 unbuilt, G8 gated by judgment | M (conditional: a declared realm-hash mover per commit only if G5 builds; H-204 moves the told channel) | — | — | carried in full: `-04` |

`..._part4.md:649` (-04 content-owner entry)

### IN-18 — G5, G8, the gated tail (telling workplan residue) (IN) · BATCH B10-Z (HELD; its MEASURE closed at B10-02) · STATE BLK:G5 trigger M0e (re-measured at B10-02: headline 0, the workplan's own definition above 0); G8 gated by judgment · R —
- WHAT: Build the two gated tail rows of the telling table: G5 (an obligee reports to the seat holder) when its trigger M0e > 0 is met, and G8 (letters deposited as `told_by`) when judgment lifts its gate. A field lands only with its reader and falsifier; unfleshed elements stay `absent` hole rows with field-less markers.
- LANDED AT B10-02 (`165d355c`, with the close commit's corrections): the M0e reader `harness/obligee_report.py` (`python -m engine.season.harness.obligee_report SEASONS SEED ...`; it reads survivors only, so every count is a lower bound where an obligee or holder died). Four realm seasons, seeds 0 / 1 / 2: headline `m0e` (an executed `news.told` by an obligee to his seat's holder) 0 / 0 / 0; `attempted` 0 / 1 / 3 (all `news.untold`, degree None); `told_by` 0 / 0 / 0; `inferred_about_person` (the telling workplan's own M0e) 4 / 18 / 4; obligee edges 36 / 44 / 39. G5 is HELD on the headline definition, and on the workplan's definition M0e is above 0 with the site not derived (this position's Stop-if); G5 stays unbuilt either way.
- LANDED ALREADY: step 2a, G1 (live, `judged_gain` and `told_valence_gain` at 0.5), G2, G3 at B-E `ac9724fc`; G4 dropped; G7 recorded (H-198); G6 at B-I `66bf51f9` (dormant in play, H-204); `oblige` (IN-10 sub-step (a)) `905b7a21`; telling T0-T6 (#449).
- REMAINING UNBUILT: [v9 WHAT, full text: the open rows of the telling §5 table, the §6 branches they read and the §10 judgments. G5 (duty to report: an obligee forms a `tell` to the seat holder) builds when M0e > 0; G8 (letters: `create_record(letter)` + `give` deposits the said triple as `told_by`) is gated by judgment. The ties row is IN-32's. Rule that governs both: a field lands only in the same commit as its reader and its falsifier; an unfleshed element is an `absent` hole row plus a field-less `# ABSENT: H-NNN` marker, never a dead carrier.] G5 (site `_from_inferred_claim` — "names no symbol in the tree read at B-E's boundary — re-derive it by grep before editing"); G8 (letters); the ties row (IN-32's). Other `absent` rows and triggers carried: `stake` (M0h > 0); a default-obstacle sweep (M0i after T4 no higher than at T0); `Seen.who` as a source (only if M0d counts zero from it); sanctioned silence (`date.fired` reaching WITNESS, plan position `22`). Standing §10 judgments (recorded, not ruled by Jordan, reversible): G8 letters gated; self-disclosure allowed; private whispers not built.
- GATE: G5: prerequisite T4 (landed), trigger "M0e > 0" (§5 row G5) — read 0 over four realm seasons at B-I's close (2026-10-13) after `oblige` landed; "re-measure when obligees exist before the final season". G8: prerequisite T4; trigger "none; ahead of T5 if M0d < 20%" — realm M0d 12% licensed G8 ahead of T5, T5 landed first, G8 stays gated. Ties: prerequisite IN-32 (`_eff_tie`), trigger `aperture 1 0`: `tie / knot` executed > 0. Each trigger is a figure an existing instrument prints (§0.1 pt 5 forbids a guard).
- EXIT and FALSIFIER: EXIT "per gate, §5's falsifier column, observed at the batch that builds it" (G1's EXIT, `engine/season/tests/test_told_by_channel.py::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone`, ran at B-E's exit). FALSIFIER, G5: "an obligee forms a `tell` to the seat holder, and without `oblige` none (§5 row G5)"; G8: "`create_record(letter)` + `give` deposits the said triple as `told_by`, chain ending in the maker"; ties: IN-32's.
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: H-62, H-66, H-175, H-149, H-192, H-193, H-198, H-204 (cited by v9); per G1 classification also H-194 (G2, `stance_polarity`, asked in ED-IN-0296; answered by CR-16, `declared`), H-195 (G2 `holder` operand, trigger M0g >= 5 %), H-196 (G3, `said_slant`), H-197 (G6, `telling_privacy`); ED-IN-0282 (telling workplan); ED-IN-0296.
- ASKS ATTACHED: §10 #1 private whispers, "Jordan's alone" (voids T-e; T4 redone); recommendation recorded "Do not build". §10 #3 self-disclosure; recommendation "Allow". (v9_p4:91-94)
- RE-BASE: v9 re-read the position at B-I (G6, `oblige`) and B-M (CARRY-INTERIOR reads G1 at IN-13's fought field; realm fights 0 fields). Since: B-X (#480) landed the decision-surface cast/goals/salience work and wrote ED-IN-0296, which carries H-194's `declared`-arm question that G2 depends on; B-Q..B-Y subjects do not name IN-18. No M0e re-measure is recorded after B-I [INFERRED from the extracts]. Otherwise none found.
- SOURCE: `v9_p4:58-94` (entry; table rows `:70-74`; §6 branches `:82-87`; §10 `:89-94`); state-index row `v9.md:257`.

### IN-30  ·  STILL-NEEDED  ·  FA · new batch `B21b-fa-plan` (v11 B10-17) after U3 B21 (so `06_FA_war_lives_in_seats_B` edits 1-3 land first) and before B23, B32; card order IN-36 march cap, CP-T09-01..06, CR-32, CR-35, CR-36, CR-…

`..._part12.md:244` (handle index row)

| IN-30 | B10-17 | carried v9 position (`-04`) |

`..._part3.md:192` (batch card row)

| IN-30 | H-186 GD-3's insurgency beyond its first condition; an emerged faction (= SE-05, FA-02): faction identity gets one owner that admits emergence, `queries/world_q.py::faction_props` (the rostered faction Propositions plus every Proposition in the creed shape, the shape a roster key `factions.creed`), founded by a person's own `utter` of a creed; it ships with the GD-3 FAIL named on H-186 (an emerged creed cannot `seize`) `[ASSUMPTION; medium; Jordan to correct; revert: faction_props returns FACTION_BY_PROP's keys; the creed term dropped]` | BUILD (with CP-T09-04 (d) as its acting caller) · STOPPED (at B-U, closed `156f3e5d`, unbuilt: finding in H-186) | M (declared wherever a creed is uttered; EQUAL at build) | — | `-05` §1a (c) | carried in full: `-04` |

`..._part5.md:125` (-04 content-owner entry)

### IN-30 — H-186 GD-3's insurgency beyond its first condition; an emerged faction (= SE-05, FA-02) (IN; FA, SE) · BATCH B10-17 · STATE STOPPED (at B-U, closed `156f3e5d`, unbuilt: finding in H-186) · R —
- SECOND DECISION ROUND (item 4, make the endings reachable, `-05` §1b; B10-17, first, slot and NEEDS unchanged; faction identity taken at step 4, its occasion at step 5): faction identity gets ONE owner that admits emergence, `queries/world_q.py::faction_props(w)`: the rostered faction Propositions (`data/rosters.py:996`, `FACTION_BY_PROP`) plus every Proposition in the world in the creed shape (`mood: OUGHT`, `predicate: "carries the creed of"`, `harness/populated.py:1090`), the shape hoisted to a roster key `rosters.yaml: factions.creed` read by the builder and the Query ([UNVERIFIED] whether the roster loader accepts the subkey); `faction_holding` (`world_q.py:1876-1882`) and every other "is this a faction" test read it (every reader of `FACTION_BY_PROP` is enumerated at the build). No threshold, counter or stored entity. The founding act is a person's own `utter` of a creed (mood and predicate from the roster key, `value` the new Proposition's id, `subject` the founder); membership is the existing `commit`. Its occasion is CP-T09-01's leaver: CP-T09-01's body, built only if its measurement finds a leaver, offers the creed `utter` to a person whose opinion of each rostered faction he is committed to has fallen below indifference and who `release`s that `commit`, formed only if he holds a seat or a land `hold`; if no leaver is measured, the creed lands as a hand-built mechanism (this falsifier) and its realm reading is a named residue. GD-3 (a)'s trigger is not carried (contiguity has no carrier since `29c`, H-186; the streak is a clock, #457 §5; a world event that forms an insurgency with nobody choosing is a threshold producing an outcome, T-b). **GD-3 FAIL:** an emerged faction keeps the land its founder held and receives land by cession (CP-T09-05's `give` + Rung), but cannot take more by `seize` (`seize` requires the actor committed to his seat's faction, and a seat's faction is the authored `Office.faction`); that fails GD-3's violation test (`canon/04_game_design_constraints.md:29`) and is recorded on H-186 as a GD-3 FAIL, not a stated limit; IN-30 ships with the FAIL named, and the fix (a seat serving an emerged creed, every same-faction rule then re-reading `seat_faction`) or an amended GD-3 is `-05` §1a question (c), confirmed at the default (ED-IN-0301): IN-30 ships with the FAIL named on H-186, and the question blocks nothing built now. EXIT is met by CP-T09-04 (d) for `uncontrolled` and by `faction_props` for emergence. FALSIFIER (hand-built, real fold): a land-holding seat-holder `release`s his faction `commit`, `utter`s a creed and `commit`s to it → `faction_holding` names the creed, his territory is not `uncontrolled`, and a planted world with every realm territory under the creed's members reports `peninsular_sovereignty`; CONTROL: the same with a non-creed OUGHT → not a faction (today's reading); mutation: drop the predicate test → every uttered OUGHT becomes a faction and the build's `uncontrolled` reading moves → red. HASH: declared MOVER wherever a creed is uttered; EQUAL at build (the six creed Propositions of `build_realm(0)` are all in `FACTION_BY_PROP`; a probe, not re-run). READINGS: `faction_props(w)` size per season, seeds 0-2, eight seasons (base 10), and land held under non-rostered creeds (base 0). PORT: the faction set becomes a function of the world; a GDScript port must not cache `FACTIONS` as an enum for identity (display names stay the roster's; an emerged creed's display name is its founder's). BUILDER: `CLAUDE.md` §10's third tier (judgment). `[ASSUMPTION; medium; Jordan to correct; revert: faction_props returns FACTION_BY_PROP's keys; the creed term dropped]`
  - **CP-T09-04, built with this position (one build, two handles; its home and B10-17 build card carry the rest), gains the unpeopled clause:** an unheld place in whose subtree no faction is `mustered` is licensed to a seat whose purview reaches it (`purview_reaches`), in the one owner `loop/effects_shared.py::occupying_faction` (`:149-165`), shared by `seize` and `raze`; `raze` keeps CP-T09-04's explicit unheld decline, so the clause licenses a taking, never a razing; term (d) offers such places as well. LADDER: step 4 on the gate's own seizure reading (`may_seize` asks the seat's purview over the rung, `gate.py:1208-1221`), not on ED-IN-0256 (4) (that ruling defines governing authority, and H-90's message 1 separates it from holdings). Still not covered, named: GD-1's Accord, Stability, sustain and treaty clauses (the translation's lawful F3 forms are the route; each needs a band nobody has given, a residue whose trigger is a ruled band); an emerged faction's seizures (the GD-3 FAIL above); a seizure by a seat-holder not committed to his seat's faction. FALSIFIER (5): a planted world where every realm territory but `terr_T15` is held by Crown persons and nobody stands under `terr_T15`: the realm seat's computed `seize` of `terr_T15` executes and that season's `endings` contains `peninsular_sovereignty`, credited to the seize's opened `hold` (T-b); CONTROL: the clause off → `seize.refused` and `endings == []`; mutation: drop the purview conjunct → a Hafenmark seat (no purview over Askeheim) seizes it → red. H-176's "structural zero" clause and the `endings` note (`rosters.yaml:2595-2596`) are rewritten in its commit. READINGS: `rung.seized` on territories and `uncontrolled_in_realm` per season, seeds 0-2, eight seasons (base 11 after one season, H-186), and `SeasonDriver.season`'s `endings`; [UNVERIFIED: whether any seat's question in seeded play names `terr_T15` once (d) offers it; not run]. PORT: a Godot consumer reading `victory: true` as the game's end breaks GD-1's two-season test, so it carries the ending row's caveat. `[ASSUMPTION; medium; Jordan to correct; revert: drop the clause]`
  - The GATE, EXIT, FALSIFIER and HASH lines below are v9's and are superseded by this block where they differ; CR-39 (B10-Z, HELD on CR-38) is the emerged creed's promotion.
- WHAT: `24h` P5's remainder. `queries/world_q.py:1192` `uncontrolled` is the built first condition and its only non-test caller is a report (`harness/populated.py:1304`). Build a caller that acts on it, and faction emergence: contiguity, streak, promotion and emerged-faction identity have no carrier, and no verb acts on unheld land (H-186).
- LANDED ALREADY: the first condition `uncontrolled` (report-only caller); `raze` `68eaaa41` (H-166 limit 3's closer; executes 0 in computed play, H-228 limit 3); IN-27 `6ae70998` (ending vocabulary) and D4/D6 answers (RS-21 items 3 and 4).
- REMAINING UNBUILT: an acting caller of `uncontrolled` in `queries/` or `loop/` that a person's choice reaches, in a seeded season; faction emergence; design choices for adjacency, streak counter, promotion thresholds, emerged-faction identity. Per H-186, one of three choices first: (a) H-166 seize on an unheld settlement, (b) `march` `referent_class: Rung`, (c) a question source.
- GATE: BLK: H-149's march-target positions (`raze`, H-166 limit 3's closer, landed and executes 0 in computed play: H-228 limit 3) — "no ruling owed: ladder answered it in H-186"; #457 D4 and D6 answered (RS-21 3 and 4) [medium; Jordan to correct]. FA-01's content (B-V) is NOT a data edge [ASSUMPTION; if faction emergence needs FA-01's content, IN-30 moves behind B-V — now landed]. Rides the first batch that edits `queries/world_q.py::questions_for` or the Rung-stamp cell (R1/R8). EDITS `questions_for` stamp source in `queries/world_q.py`, called from `loop/driver.py::_questions_at_barrier`; `queries/world_q.py::faction_holding`.
- EXIT and FALSIFIER: EXIT "`grep -rn "uncontrolled(" engine/season/queries engine/season/loop --include=*.py` shows a caller in `queries/` or `loop/` that a person's choice reaches, and it executes in a seeded season." FALSIFIER "report still the only non-test caller -> not built." Revert: either answer reverted (RS-21 3 or 4) -> this position reverts with it.
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: H-186 (its row in `engine/season/hole_register.yaml` records the GD-3 FAIL in this position's build commit), H-149, H-166, H-176, H-228; RS-21 (3, 4); FA-01. Aliases SE-05 and FA-02 take this position's batch (both state-index rows read "= IN-30").
- ASKS ATTACHED: none open ("no ruling owed") for v9's remainder; the GD-3 FAIL's fix is `-05` §1a question (c) (above), confirmed at the default (ED-IN-0301).
- RE-BASE: B-U (#494, "IN-30 stopped") is the stop; B-R (#496) landed `raze`/`give`+Rung whose realm execution stays 0; B-V (#498) landed FA-01's content. v9 carries all three. None found since.
- SOURCE: `v9_p5:66-71`; state-index row `v9.md:258`; aliases `v9_p6:97` (SE-05), `v9.md:279` and `:293`.

### IN-36  ·  STILL-NEEDED  ·  FA · new batch `B21b-fa-plan` (v11 B10-17) after U3 B21 (so `06_FA_war_lives_in_seats_B` edits 1-3 land first) and before B23, B32; card order IN-36 march cap, CP-T09-01..06, CR-32, CR-35, CR-36, CR-…

`..._part12.md:246` (handle index row)

| IN-36 | B10-17 | carried v9 position (`-04`) (casus-belli residue → CR-91) |

`..._part3.md:208` (batch card row)

| IN-36 | FORCE-FOREIGN: an external empire and Schoenland as persons; the march frequency answered in kind (ED-IN-0317) | `foreign` ON by default since ED-IN-0310 (Jordan, 2026-11-04); BUILD: the interim march cap, one march per season into each territory (ED-IN-0317), a declared mover, first in this batch; HELD (the casus-belli rule moved to CR-91, B10-17b): Schoenland as persons, perception channels at the border, the three `field.unopposed` arrivals; BUILD: the `guards` flip ON after CP-T09-07 (b), a declared mover (ED-IN-0317: ships ON once CP-T09-07 (b)'s union lands, its own declared mover in B10-17; `[ASSUMPTION; medium; Jordan to correct; revert: guards stays off]`) · LANDED-NARROWED (landed at B-V `7c59d74c`; the rest in its `-04` part 2 entry) | M (the cap) | — | — | carried in full: `-04` part 2 |

`..._part5.md:140` (-04 content-owner entry)

### IN-36 — FORCE-FOREIGN: an external empire and Schoenland as persons (IN; FA, MB) · BATCH B10-17 · STATE LANDED-NARROWED (landed at B-V `7c59d74c`); BUILD the interim march cap (ED-IN-0317, a declared mover, first in B10-17); HELD for its other residues (Schoenland as persons, perception channels, the three `field.unopposed` arrivals; the casus-belli carrier moved to CR-91, B10-17b) · R —
- WHAT: what remains after the landing: Schoenland as persons (factor placed, no head, no template); perception channels at the border (not built; CR-29's reach channel, released from M11, is the plan's route); `stance: -1` toward the Crown head's seat (inert, H-233); the march FREQUENCY (H-233), ANSWERED IN KIND by Jordan, 2026-11-04 (ED-IN-0317; below); and a Katepano march on the capital that arrives `field.unopposed`.
- LANDED ALREADY: `7c59d74c` (B-V, closed `b1eabf5d`, PR #498; remainder PR #499). Altonia a faction (`names_index.yaml`); `rosters.yaml: foreign_cast`; two seats (`offices.yaml: foreign_seats`); three goal rows; IN-60's guard cohorts (`cohorts.yaml: guards`). Landed behind `build_realm(foreign=, guards=)`, both default OFF [ASSUMPTION; medium; Jordan to correct]; no harness flag turns either on. Hashes: `build_realm(0)` `d3edd90a` unchanged, `foreign=True` `36e59a16` (re-recorded when Katepano's goal retargeted to Valorsplatz, `goal_katepano_press_the_capital`, `set_s_001`), `guards=True` `73ecca60`. Natural-play half MET AT WITNESS SEEDS 39 and 53 only (the real unrestricted chooser picks the march on the first goal-question scene; the fold reaches `mass_battle.field_input`, ends `field.lost`; `test_in36_foreign.py`); first released scene tick 0 in 7 of 80 seeds.
- REMAINING UNBUILT: perception channels at the border (the trade-demand clause waits on them: FA-01, ED-IN-0298, H-234); Schoenland as persons; the march FREQUENCY half, in two parts, by Jordan's ruling of 2026-11-04 (ED-IN-0317; verbatim: *"march can only happen if there is a casus belli ie claim to a territory...unless civil war breaks out. anyway, for testing purposes, once a season per territory cap."*): **(a) the interim test cap, BUILD in B10-17 (first):** at most one march per season (one `w.tick`) INTO each territory, counting a march on a settlement against the territory that contains it, uniform for every marcher, civil-war marches included, behind a plain integer fixture (name chosen at build; shipped 1; 0 or unset = no cap) `[ASSUMPTION; medium; Jordan to correct; revert: no cap]`, superseded by (b) once (b) is built. Seam: a typed `requires` conjunct on `march`'s row (a new stem in `data/requires.py` reading the season's admitted marches into the target's territory), refused on the row's existing refusal channel (`emits_on_refusal: ["march.refused"]`) and read by the one admission path (`loop/resolve.py::_admits`, eligibility then `requires`) like every other conjunct; not a `march` branch inside `_admits` (special-casing a verb, `CLAUDE.md` §0). It edits `verb_table.yaml`, so it joins the verb cluster and serialises (P13). Its fixture needs a `hole_register.yaml` row with a `site:` (`test_season_shape.py::test_w9_check3_every_fixture_read_resolves_to_a_register_site`). **(b) the standing casus-belli rule, MOVED to CR-91 (B10-17b; the arc fold of 2026-11-05, ED-IN-0346: the carrier is a claim Proposition on a ground, `-04` CR-91; the text below stays as the ruling's record):** a march needs a claim to the target territory held by the marcher, his faction or his office; the exception is civil war (a rising: side R in the strife instrument's terms, a marcher whose faction governs nothing up the target's chain); the foreign nations' marches (side O) need a claim to the territory they march on like anyone else; a marcher's own held territory is claimed by its `hold`. No carrier for "a claim to a territory" exists in the plan or the code: the `Tenure` kinds (`rosters.yaml: tenure_kinds`: hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban) name none; `succession.claimed` (CL) is a claim to a SEAT; `faction_q.at_war` reads live `commit`s to a two-faction WAR Proposition and names no territory; `hole_register.yaml` H-175 ("a hostile-presence claim, a standing casus belli, a border dispute) is a live design choice ... this row does not invent one") invents none; CP-T09-02's home builds a war's Proposition and a target set (term (c): the other side's settlements in the seat's purview) and states "a march needs no war", listing "a casus-belli gate on `march`" as not built (direction 8), which this ruling supersedes. `[GAP: carrier — the claim to a territory; candidate: a Proposition on the WAR / creed shape (subject the territory, value the claimant faction, held by `commit` edges, so a claim ends when its committers release it and nothing is stored, ED-IN-0225), produced by CP-T09-02's `declare` or an `utter`; owner CP-T09-02, decided at B10-17's re-base (V1)]`; the gate on `march` is built only once the carrier exists; a Katepano march forming at seeds 16, 38, 44 arrives `field.unopposed` in a full season (the King's `t_hold_terr_T1` gone by round-0 ENCOUNTER; traced at seed 16, cause unverified); flipping `foreign` or `guards` ON is its own declared hash mover (realm hashes and 1-/2-season pins re-recorded).
- WHAT REMAINS HELD (the story-telling fold of 2026-11-02, ED-IN-0311; amended by ED-IN-0317): Schoenland as persons; perception channels at the border (CR-29's reach channel is the route); the cause of the three `field.unopposed` arrivals. The casus-belli carrier (above) is no longer held here: it moved to CR-91 (B10-17b). The frequency is no longer held: ED-IN-0317 answers it in kind.
- GATE: DEPS IN-36 -> FA-01's content and trade demand (D, content landed); guard content -> IN-60 `d32d7931`, IN-59 (b) `590f753a`. EDITS none further. Coupling: IN-38's NPC-089 overlay names `faction: Altonia`, so reverting IN-36 reverts that file first (`corpus_run.CAST` is read at import).
- EXIT and FALSIFIER: natural-play half as above (witness seeds). The cap (ED-IN-0317): a planted second march into one territory in one season is refused on `march.refused` while the first is admitted, hand-built; MUTATION: the cap at 0 lets both through; CONTROL: the cap off reproduces the base hash. The casus-belli rule: its exit is CR-91's (`-04`). v9 states no separate FALSIFIER line for the remainder beyond `test_in36_foreign.py` and the hash controls (`foreign` off reproduces the realm hash).
- TRIGGER (hole-row pass): nothing flips `guards` ON before CP-T09-07 (b)'s union lands; then IN-36's own flip does (ED-IN-0317, below); the trigger was M1's answer on H-233 (the natural-play march frequency), now answered in kind by ED-IN-0317 (the cap builds; the casus-belli rule waits on its carrier). After the decision round M1 is NARROWED and this is its residue, confirmed at the default (ED-IN-0301; `-05`: where the frequency of a foreign march in natural play comes from, and whether `build_realm` ships `foreign` and `guards` on): IN-36 stays HELD, FORCE-FOREIGN's driver stays off, and CL-THRUST's B5.2 waits with it. IN-36's `foreign`/`guards` default is on GO-15's freeze list. **ED-IN-0310 (Jordan, 2026-11-04) flipped `foreign` to ON by default; `guards` stayed off.** **`guards` is then TAKEN by the ladder (ED-IN-0317):** step 4, ED-IN-0310's `foreign` ON and the standing "Gains are improvements and therefore ship"; step 5, before CP-T09-07 (b)'s union lands the flip musters nobody (the guard cohorts hold an `oblige` and no `commit`), so it lands directly after that union in B10-17, as its own declared mover (P14, its pre-change reading CP-T09-07's recorded after-reading; goldens re-recorded and said so) `[ASSUMPTION; medium; Jordan to correct; revert: guards stays off]`. What it does (verified): `build_realm(guards=True)` seats `cohorts.yaml: guards` (the King's at 4, two dukes' at 2) sworn to their seats (`harness/populated.py::seat_guards`), so `guard_weight` (IN-60) reads above 0 where a principal is present and IN-59 (b)'s `audience` limb closes `move` and `migrate` into a guarded rung to those without audience; `march` carries no `audience` conjunct, so foreign and civil-war marches are not gated by it. EXIT: `guard_weight` above 0 at the King's rung at seed 0; the strife guard, guards on against off at `strife 4 0 1 2` (P10's strife exception), closes no terminal route (KL, DR, XE) and concentrates no ending, else the flip is not made (P8); CONTROL: `guards=False` reproduces the pre-flip hash. CL-THRUST's B5.2, held on this flip, is released when it lands. The freeze list's `foreign` entry is answered, and the pinned slices moved with it (`test_season_weather.BASE_HASHES`, `test_go07_canonical_digest.BASE`).
- HASH MOVERS: flipping `foreign` or `guards` ON is a declared mover; at the shipped OFF, `build_realm(0)` is unchanged (`d3edd90a`). The cap (ED-IN-0317) is a declared mover in B10-17: its pre-change `build_realm(0)` reading is B10-16's close reading @sha (P14), every seeded golden it moves re-recorded, old to new, and said so.
- HOLES AND LEDGER IDS: H-233, H-234, ED-IN-0298; FA-01, IN-60, IN-59, IN-38, IN-13. SOURCE #457 `:145-155`.
- ASKS ATTACHED: none for the frequency (answered in kind, ED-IN-0317; whether a march is chosen at all stays the chooser's, from convictions and IN-08 `alignment` cells, which are content); ED-IN-0298 via FA-01.
- RE-BASE: B-V (#498/#499) is the landing; v9's entry is written after it. B-Y (#502) added `guard_weight` Query (IN-60/IN-59, A-28). None found since. CR-71 (reading @5d6aac5, `aperture 2 0` and `strife 2 0`, seed 0, `PYTHONHASHSEED=0`, REALM): OW reads 0: no side-O `march.declared` occurs in two seasons (the FR, WN and OW signatures: A 2, R 11, O 0; S1r read side-O marches at four seasons, `-11` §1). WA and WR read 0: `field.won` and `field.lost` are never emitted. The declared marches, their refusals and the `field.unopposed` ones are counted at H-149's cite; whose marches the `field.unopposed` ones are is this entry's open question, not read.
- SOURCE: `v9_p5:87-91`; state-index row `v9.md:261`.

### IN-44  ·  STILL-NEEDED  ·  IN · U3 B03-hygiene · gate: `python tools/currency_consistency_check.py` + `python tools/valoria_local.py --staged` · hash: n/a (text) · tier: sonnet; (RULED)-checked at each anchor

`..._part12.md:247` (handle index row)

| IN-44 | B10-Z | carried v9 position (`-04`) |

`..._part3.md:432` (batch card row)

| IN-44 | Layer 0 and Layer 1 edits owed: LISTED, NOT MADE (SM-10, SM-12, A-24's wording); row 1 (the `CLAUDE.md` §0.2 `mc_v18` bullet) released by M15 (a), retired as a listed Layer 0 hunk (H-L0-6, applied in PR #507) | HELD · LEAVE (rows 2-16, released from M11 by ED-IN-0300: unscheduled, slotted by R8; each row is re-derived by symbol and (RULED)-checked at its anchor before it is listed or landed) | E | — | — | carried in full: `-04` |

`..._part4.md:662` (-04 content-owner entry)

### IN-44 — Layer 0 and Layer 1 edits owed: LISTED, NOT MADE (SM-10, SM-12, A-24's wording) (IN) · BATCH B10-Z · STATE rows 2-16 released from M11 (ED-IN-0300), unscheduled in B10-Z; row 1 released by M15 and applied as H-L0-6 · R —
- DECISION ROUND: row 1 (the `CLAUDE.md` §0.2 `mc_v18` paragraph) is released by M15 taken (a) (`-05`; step 1, superseded: it executes Jordan's 2026-09-16 and 2026-09-27 words quoted in row 1): it is applied in PR #507 as H-L0-6 `[ASSUMPTION; medium; Jordan to correct; revert: restore the four lines]`. Rows 2-16 are released from M11 (answered (a): the superseding row of ED-IN-0300, 2026-10-26, ratified): they stay in B10-Z, unscheduled, slotted by R8, and each row is re-derived by symbol and (RULED)-checked at its anchor before it is listed under "Layer 0/1 hunks" or landed.
- WHAT: Hold the sixteen stale Layer 0 and Layer 1 passages (file:line, what is stale, reading owed) that no batch edits; they are Jordan's files. It owns the SM-10, SM-12 and A-24 wording and receives other positions' Layer-1 wording rows.
- LANDED ALREADY: —. (Adoption edited only the two `CURRENT.md` rows named at v9_p8:369-371, item 1.)
- REMAINING UNBUILT: [v9 WHAT, full text: the table of stale Layer 0 and Layer 1 text that no batch edits; "Jordan does". It names the file:line, what is stale and the reading owed. It owns the SM-10 and SM-12 wording and A-24's wording rows, and is the destination for IN-61's Layer-1 wording (`04` §B.8, §A.3 row 8, §F.24a row 5), SE-04 (b)'s `Rung.envelope` row and IN-56's AX-4 log-index reading. v9 treats it as a table, not an entry.] all sixteen rows of the v9 table (rows 1-16, `v9_p8:416-431`): (1) `CLAUDE.md:278-281` §0.2 `mc_v18` paragraph (Jordan's words supporting retirement are quoted there: 2026-09-16 "Remember that mc_v18 is being fully retired."; 2026-09-27 "we need to move beyond any mention or use of this mc_v18. that is critical."); (2) `CLAUDE.md:407-414` §3 `engine/` bullet; (3) `CLAUDE.md:395-447` §3 no `modules/` row; (4) `CLAUDE.md:527-531` §6 "starting with `engine_clock`"; (5) `CLAUDE.md:540-547` §7 retired `balance_oracle` paragraph; (6) `CLAUDE.md:155` §0.05 `fac.intel` "reachable by nothing"; (7) `CLAUDE.md:514` (SM-10 cite); (8) `CURRENT.md:15, :22, :41` stamp, retire-set wording, `engine/autoload`; (9) `architecture/meta/04_CODE_ARCHITECTURE.md:1000`, `architecture/PLAN.md:1271`, `architecture/VOCABULARY.md:125` (SM-10); (10) `architecture/holonic_ARCHITECTURE.md:75` `[engine]` tag (SM-12); (11) `04_CODE_ARCHITECTURE.md:164, :370, :374-376, :596-611 (C.2), :391, :494` (determination opens any `disposes:` kind; tenth basis `warrant`; `RELEASABLE_KINDS`); (12) SM-12 / A-24's holonic item (the 2026-09-17 "holonic shape" preference predates A-25; "later governs; Jordan to note the earlier preference when he edits"); (13) `CLAUDE.md:727-730` §11 deny-list vs `RemoteTrigger` [UNVERIFIED in v9: what `RemoteTrigger` does in the current tool surface]; (14) `04:195, :326, :359, :1188, :609-610` (heir as holder-owned `succeed` edge; RS-27 makes the heir a title; `succeed` Tenure kind opened by nothing); (15) `04:115` AX-4 vs IN-56's `World._last_by_anchor`/`_last_by_subject` log index; (16) `04:255` `Rung :=` `envelope`, `:179`, `:1166` (H-171). Closing line (v9_p8:433): "`CURRENT.md:41`'s pointer repair is the same class as #448's and may ride adoption at Jordan's word." [Line numbers in rows are v9's, read 2026-10-06 and earlier; re-derive each anchor by symbol before use.]
- GATE: released from M11 (ED-IN-0300): an agent may land unmarked `CLAUDE.md` and `architecture/` text in the PR, stated openly under "Layer 0/1 hunks"; text marked (RULED) stays Jordan's and stops its row. v9: "IN-44 sits in B-Z: no batch edits these files; Jordan does." Rows 14-16 carry "Nothing waits on it" / "[medium]" tags where stated (rows 14, 15). `CLAUDE.md` marks some rules (RULED): v10's batch card for B10-03 requires each anchor to be checked for a (RULED) mark before a hunk is listed.
- ALSO OWED (`-08`, REM-41 cut): `architecture/meta/04_CODE_ARCHITECTURE.md:496` says 'the log accepts no other kind'; `matter.py`'s three direct appends (`:105`, `:234`, `:297`) are game emitters that bypass the fold's check, so the sentence is unmet until Jordan edits it or the appends are checked. No position builds either.
- EXIT and FALSIFIER: v9 states none for IN-44 as a table. The instrument v9 names for the adoption-time subset is `python tools/currency_consistency_check.py` and `python tools/valoria_local.py --staged` (v9_p8:389); v9 states no falsifier for the rest.
- HASH MOVERS: none stated (text only).
- HOLES AND LEDGER IDS: H-171 (row 16); ED-IN-0206 (row 8: becomes `superseded` -> `23`, SC-02); ED-IN-0292 (1) (row 14, `founding` wording); SM-10, SM-12, A-24, A-25, RS-11, RS-27, RS-29, IN-56.
- ASKS ATTACHED: whether the PR #450 deletions return, A-24 (i) — v9 working answer NO [medium], "yours to overrule" (v9_p5:246, :350-352). Not answered here.
- RE-BASE: rows 14-16 cite IN-61's stop at B-R, IN-56 (landed B-W) and H-171 (appended at B-T), so they were added after B-R/B-W/B-T [INFERRED from what the rows cite]; rows 8 and 13 are older. Since v9 was written: HEAD is `b7a1e1b`; `CURRENT.md`/`CLAUDE.md` wording may have moved again — re-derive each anchor. No batch among B-Q..B-Y edited Layer 0/1 per the merge subjects.
- SOURCE: `v9_p8:410-433` (table `:416-431`; H.3 adoption edits `:369-385`); state-index row `v9.md:263`.

### IN-48  ·  STILL-NEEDED  ·  FA · new batch `B21b-fa-plan` (v11 B10-17) after U3 B21 (so `06_FA_war_lives_in_seats_B` edits 1-3 land first) and before B23, B32; card order IN-36 march cap, CP-T09-01..06, CR-32, CR-35, CR-36, CR-…

`..._part12.md:249` (handle index row)

| IN-48 | B10-17 | carried v9 position (`-04`) |

`..._part3.md:207` (batch card row)

| IN-48 | H-108's delegation half: a seat exercised by someone who does not hold it | DESIGN-FIRST again (Layer 1's route; v9 batch B-JR), then BUILD | E | —; not a dependency: CR-35, CR-36, CR-37 (order only: `state/gate.py`) | — | carried in full: `-04` |

`..._part5.md:154` (-04 content-owner entry)

### IN-48 — H-108's delegation half: a seat exercised by someone who does not hold it (IN; FA, SE) · BATCH B10-17 · STATE BUILD (DESIGN FIRST AGAIN on Layer 1's route; v9 batch B-JR, unscheduled) · R R-04
- WHAT: Delegation without a hold (regent beside a living principal, puppet, governor, council): a non-holder exercises a seat `via` it. The `delegate` kind was built and reverted for contradicting ratified Layer 1; redesign on Layer 1's route (`establish` a second seat, `confer` it, `Tenure.term`) and measure early revocation.
- LANDED ALREADY: IN-40 `3f320093`; IN-10 sub-steps (a), (b) `905b7a21`; IN-11 `2a2ed152`; the `Act.via` half. A `delegate` tenure kind was BUILT at `40926a95` and REVERTED at the B-J close (#476): it contradicts ratified Layer 1 (`01_AXIOMS.md` §E.2.4 `:1465-1467`, `:1569`; `04_CODE_ARCHITECTURE.md:351`: delegation is conferring a seat, `tenure_kinds` does not move). The held `delegate` design and what the build found: `proposals/2026-10-14-in48-delegation-carrier.md` §9.
- REMAINING UNBUILT: [v9 WHAT, full text: Jordan 2026-09-03 "Regency and puppet rulers must be possible." / "Same with delegation". Regency by TERM is IN-10 (b); `_eff_confer` closes every live hold on the seat (`effects_governance.py:63-69`), so a termed regent displaces the principal. Left: delegation WITHOUT a hold (regent beside a living principal, puppet, governor, council; `gate.py:239-242`). H-108 re-scoped at B-C (IN-43, landed) to "delegation without a hold"; its `Act.via` half is built (`choose.py:434`; `resolve.py:116-117`); this position owns H-108 and closes it when it lands.] the design, on Layer 1's route (`establish` a second seat over the domain, `confer` it, IN-10's `Tenure.term`) — MEASURE whether a principal can revoke a same-rung seat early. READ, not yet run: creating a regent works on today's code (`may_fill`, `gate.py` ~575-579; `_eff_confer` closes holds only on the seat conferred) but ending one early does not — both `REVOCATION_RULES` need the revoking seat on the PARENT rung (`gate.py` ~422-428, ~512-513), the top rung's seat is strippable by nobody, so a realm regency ends by `Tenure.term` or the regent's own `release`; an early dismissal would be a new `revocation` basis (data in Layer 1's shape); a revoked `appointed` regent would carry IN-31's ban (`d16bd895`). That design may rewrite this entry's EXIT (whose premise, a person holding no `hold`, is non-Layer-1). A new `tenure_kinds` member is NOT licensed (Jordan's).
- GATE: DEPS IN-10 (satisfied), IN-11 (satisfied), IN-40 `3f320093` <-> IN-48 (F, satisfied). EDITS (assumed, [UNVERIFIED] until the design) `state/gate.py` (`seat_hold` `:230`), `decision/choose.py` (`:434`), `loop/resolve.py` (`:116-117`), tests. Serialises with any batch that edits `state/gate.py` (R7), including IN-12/IN-61. SECOND DECISION ROUND: not a dependency: CR-35, CR-36, CR-37 (order only: they precede it in B10-17 on `state/gate.py`). B-JR placement is an [ASSUMPTION; medium; Jordan to correct; revert: IN-48 returns to B-J's row].
- EXIT and FALSIFIER: EXIT "design reviewed, then built in B-J: in a seeded season a person holding no `hold` on a seat exercises it `via` that seat through the delegation carrier while the principal keeps the hold, and when the carrier ends the same act refuses; H-108 closed." FALSIFIER "delegate's act admitted after delegation ended, or a seat exercised by a person with neither hold nor carrier -> fail; principal's hold closed by a delegation -> regency by term (IN-10), not this." (The EXIT's "built in B-J" no longer applies: B-J closed without the build.)
- HASH MOVERS: possible — "a new dataclass field would move hash by schema and is declared if the design needs one".
- HOLES AND LEDGER IDS: H-108 (`hole_register.yaml` `:1571`); IN-43, IN-31, IN-40, IN-10, IN-11.
- ASKS ATTACHED: none attached [INFERRED]; design-first.
- RE-BASE: the revert happened at the B-J close (#476/#477), before the later batches; B-W..B-T subjects do not name IN-48. v9 batch card B-JR "gates nothing" and is unscheduled. None found since.
- SOURCE: `v9_p5:110-115`; B-JR card `v9_p3:173, :227, :257`; state-index row `v9.md:267`.

### IN-52  ·  STILL-NEEDED  ·  SE · U3 B12-world-motion-and-ground, as the positions the SE proposals amend (R-SE-01..05, -19: `unified/U5_FINDINGS_CLOSURE_U5d.md:244`); CR-40 first, then CP-T08-01 onward in the card order · gate:…

`..._part12.md:250` (handle index row)

| IN-52 | B10-16 | carried v9 position (`-04`) |

`..._part3.md:176` (batch card row)

| IN-52 | the levy-to-field feed (now `requisition`): levied stores provision a season field | the flip: BUILD (released from M17, on CR-23; it provisions fields from treasuries filled by requisition and moves no pin while the realm fights no field) · the retirement: HELD on M3 | M (the flip, its own declared commit; no pin moves while the realm fights no field) | CR-23 | M3 (the retirement) | carried in full: `-04` |

`..._part4.md:748` (-04 content-owner entry)

### IN-52 — the levy-to-field feed (now `requisition`): levied stores provision a season field (IN; SE, MB) · BATCH B10-16 (the flip, last) · STATE BUILD (the flip, released from M17 through CR-23); its retirement HELD on M3 · R —
- DECISION ROUND: the flip is released: CR-23 (B10-06, M17 taken) is the owner of H-163 limit 3(a), so `requisition` executing in computed play is CR-23's exit (met at B10-06's close, `7362fa46f`), not an unowned gap. The flip provisions fields from treasuries filled by requisition and moves no pin while the realm fights no field; it lands as B10-16's last commit, a declared mover. The row's retirement stays HELD on M3 (`-05`). NEEDS gain CR-23 (B10-06). If CR-23 reverts (`stock_report = off`), the flip re-holds.
- WHAT: flip `field_provisioning` ON, in its own commit; moves no pinned hash while the realm fights no field (H-241); the decisions owed at the flip are H-241's `default:`. (Verb rename 2026-10-16: the Rung.stores verb `levy` is `requisition` in code; `levy` is reserved for the verb that raises troops — `proposals/2026-10-16-troop-stock-design.md`, PROPOSED.)
- LANDED ALREADY: the OFF build `128bc9db` (B-T, #503). LF-1..LF-3 DELEGATED-RULED 2026-10-12 [ASSUMPTION; medium; Jordan to correct]: LF-1..3 adopted; build ships OFF (hash-neutral); flip ON is its own commit.
- REMAINING UNBUILT: the flip ON (`engine/season/data/fixtures.py`, the default). H-241's owed decisions: ration min over kinds, casualties on all losers, defender debit.
- GATE: `requisition` executing in computed play (H-163 limit 3(a)), read at CR-23's exit (B10-06, MET at its close: `aperture 4 s`, realm, `requisition` executed 4 / 6 / 8 at seeds 0 / 1 / 2, `requirements.yaml` R-04); without it a flip "would floor fields on whatever treasuries the build seeds; its falsifiers run on hand-built worlds" (H-241).
- EXIT and FALSIFIER: EXIT "with it on, in a seeded season a side's fielded troops are bounded by its levied treasury." FALSIFIER "on, a side with an empty treasury fields as many troops as a full one -> the bound is not built."
- HASH MOVERS: "moves no pinned hash while the realm fights no field (H-241)"; `content_hash` folds no fixture.
- HOLES AND LEDGER IDS: H-163, H-241; J-18 (cited as SOURCE); `proposals/2026-10-07-settlements-computation-modules.md`.
- ASKS ATTACHED: none open (LF-1..3 delegated-ruled).
- RE-BASE: B-T (#503) built the OFF feed and, per the commit subject, "IN-52 shipped off"; v9 records it. Verb rename `levy` -> `requisition` (#482) post-dates the original entry. None found since B-T.
- SOURCE: `v9_p4:100-105`; state-index row `v9.md:268`; `v9_p5:339` (LF ask-then row).

### IN-58  ·  STILL-NEEDED  ·  IN · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:251` (handle index row)

| IN-58 | B10-Z (HELD; narrowed at B10-09's close two, `1ef8d273`) | carried v9 position (`-04`) |

`..._part3.md:440` (batch card row)

| IN-58 | RS-23, RS-24 grievance at read: its sworn-to half | HELD (moved from B10-09 at its close two; not decided against): NARROWED, not built: the `oblige` edge IS person-side (`Person.tenures`), but no claim a judge holds pairs the victim with the seat (`Claim` has one `subject`; `person.died` and `tenure.closed` share only `when` and `round`). Reopening needs a carrier naming the dead holder in a death's claim: a CP-T02-01 follow-up and a Layer 2 shape change (stance-only half LANDED) · BUILD when that carrier exists | E | IN-12 (landed `f9e4cef`), CR-16 (landed `142e91e22`); not a dependency: IN-61 (IN-58's gate is IN-12 step 5's exit, `-04` IN-58) | — | carried in full: `-04` |

`..._part4.md:680` (-04 content-owner entry)

### IN-58 — RS-23, RS-24 grievance at read: its sworn-to half (IN, FA) · BATCH B10-Z (moved from B10-09 at its close two) · STATE HELD, NARROWED at B10-09 close two: the `oblige` edge is person-side, but no claim pairs a victim with the seat, so the sworn-to half is not built (stance-only half LANDED); the M1 hold is lifted (CR-16) · R R-07 (contributor)
- DECISION ROUND: the sworn-to half loses its M1 hold: CR-16 (B10-07b) ships `stance_polarity: declared`, the arm under which the grievance factor reaches candidate formation. Its own BLK (IN-40's `oblige` edge read person-side) stays; build or narrow at re-base. NEEDS gain CR-16 (B10-07b, closing commit `868fd6034`; landed `142e91e22`) and IN-12 (close one).
- WHAT: Build the sworn-to half of grievance-at-read: a judge sworn to the victim's seat reads a different regard for the killer than an unsworn judge with equal stance and pursuits. It ships OFF until IN-40's `oblige` edge is readable person-side. The stance-only half has landed.
- LANDED ALREADY: stance-only half `3bf936ee` (B-W, PR #477); faction-level grievance with IN-70 `f3e1b7b9` (H-225). Measurements recorded at B-W: M-who (every non-actor witness of a death/wound holds `seen.who`: realm 18/18 and 10/10, corpus 62/62 and 156/156); M-polarity (injected -25 stance, top candidate on the killer turns hostile under `legacy`/`regard`/`declared` in 0/0/7 of 12 realm and 1/1/29 of 58 corpus pairs).
- REMAINING UNBUILT: [v9 WHAT, full text: `person_q.deeds_judged` judges a `PAIRED_KINDS` deed once for its doer via `person_q.deed_doer`; value `_lean * _bond` (cell pairs `deed:person.died`, `deed:body.changed` in `rosters.yaml`; `_bond` from stored `stance_toward` only). What remains: the sworn-to half — a judge sworn to the victim's seat reads a different regard for the killer than an unsworn one — ships OFF because `person_q` reads a `PersonInterior` only and IN-40's `oblige` edge is a `World` Tenure read by a `world_q` reader.] the sworn-to half, as its own commit once the `oblige` edge is readable person-side. Not built either: the factor's reach to candidate formation at the shipped `stance_polarity` `legacy` (reaches only under `declared`, ED-IN-0296; CR-16 shipped `declared` in B10-07b, `142e91e22`).
- NARROWED (B10-09 close two): re-base read in code. A judge's own live, un-`imposed` `oblige` to a seat is in `Person.tenures` and outlives the victim, so the edge is person-side; the v9 blocker is gone. What is missing is the pairing: a death's seat reaches a ledger as `(seat, tenure.closed, True)` (`state/gate.py::Subject.seat`) beside `(victim, person.died, True)`, held firsthand by witnesses only, and `Claim` carries one `subject` and no pairing field, so the two share only `when` and `round`. Reading that as a pairing mis-pairs two deaths in one round (`deed_doer` declines to guess for the same reason). Observed by a planted death of a seat-holder through the real fold and WITNESS, every ledger dumped. Reopens when a claim names the dead holder with the seat (a CP-T02-01 follow-up, a Layer 2 shape change); no hole row is claimed.
- GATE: DEPS IN-40 -> sworn-to half (D: IN-40 landed `3f320093`; the edge must be read person-side first); IN-58 -> IN-12 step 5's EXIT (I). BLK until the `oblige` edge is readable person-side (D). LIMITS: allegiance only scales a pursuit lean; where the actor died attacking no killer is named. Revert: factor off and cells unauthored.
- EXIT and FALSIFIER: the sworn-to falsifier: "two judges with equal stance and pursuits, one sworn to the victim's seat, read different regard for the killer -> else that half is not built." v9 notes the entry's original EXIT "hash MOVED" is NOT MET: hash EQUAL at shipped `legacy` (`2eedf7b0…` before and after).
- HASH MOVERS: equal at shipped `legacy` (stated); the sworn-to half would be a declared mover wherever it executes [INFERRED].
- HOLES AND LEDGER IDS: H-194, H-209, H-225; ED-IN-0296; RS-23, RS-24, RS-29 (cells RATIFIED as authored), A-29 (REFUSED carriers [medium]).
- ASKS ATTACHED: ED-IN-0296's polarity question (H-194; v9_p5:124, :346) is answered: `declared`, by CR-16 (M1, `-05`; its revert is CR-16's).
- RE-BASE: landed at B-W (#477, #479); IN-70 landed B-X/B-R (`f3e1b7b9`, #496). B-Y (#502) added IN-59/IN-60 `guard_weight` (not this position). None found for the sworn-to half.
- SOURCE: `v9_p5:123-127`; state-index row `v9.md:269`.

### MB-08  ·  STILL-NEEDED  ·  MB · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a (map generator, AI generals)

`..._part12.md:254` (handle index row)

| MB-08 | B10-Z | carried v9 position (`-04`) |

`..._part3.md:429` (batch card row)

| MB-08 | generated map, AI generals (#445 U-1, U-2, U-6); records the trigger of R-04's commander-chosen orders residue (a typed `Orders` record shared by the PLAYABLE scene and the AUTOMATED planner) | HELD · LEAVE (named, unscheduled) | E | — | — | carried in full: `-04` |

`..._part5.md:228` (-04 content-owner entry)

### MB-08 — generated map, AI generals (#445 U-1, U-2, U-6) (MB) · BATCH B10-Z · STATE LEAVE (named, unscheduled) · R —
- WHAT: each its own subsystem: a seeded terrain-shaped generator; an AI planner authoring Orders; #445 U-1 (musters with inputs beyond headcount), U-2 (one equipment model for both scales), U-6 (armour and endurance bridges through U-2). "Their gates are met, but none is scheduled and no R-row moves on them."
- LANDED ALREADY: —.
- REMAINING UNBUILT: all.
- GATE: STATE LEAVE. DEPS: IN (the season-side reader of any of them); EDITS none.
- EXIT and FALSIFIER: EXIT "`python -m engine.season.harness.register --requirements` — no R-row's `measure:` or missing-mechanism text names any of the three." FALSIFIER "an R-row, or a `hole_register.yaml` row, citing one of them as its cause shows 'no R-row moves on it' wrong, and the item is scheduled the day that is read."
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: #445 U-1, U-2, U-6; no hole rows.
- ASKS ATTACHED: none.
- NAMED RESIDUE (decision round, R-04 conjunct (3), `-02`): commander-chosen orders (the AUTOMATED mode may run the default orders, `massbattle.py:170-178`); trigger: a position that designs a typed `Orders` record shared by the PLAYABLE scene and the AUTOMATED planner (this entry's AI-generals half). It is not a position and does not gate R-04.
- RE-BASE: none found.
- SOURCE: `v9_p7:26-31` (SOURCE there: `registers/handoffs/HANDOFF_MB.md`; `proposals/2026-09-25-squad-engagement-synthesis.md:137`; `proposals/2026-09-30-character-and-play-surface/08_mass_battle_units.md:125,126,130`); state-index row `v9.md:282`.

### NM-W1  ·  STILL-NEEDED  ·  WR · @DESIGN|WR

`..._part12.md:256` (handle index row)

| NM-W1 | B10-19 | narration package (`proposals/2026-10-13-narration-mechanisms.md` §4); its ranking-tier piece moved to CR-68 (B10-10, the story-telling fold of 2026-11-02), the remainder stays HELD · PARTLY LANDED |

`..._part3.md:392` (batch card row)

| NM-W1 | render v0: an omniscient instrument chronicle (ranking tiers, appraisal, name fallback, per-person pages, anti-repetition, snapshots); the ranking-tier piece moved to CR-68 (B10-10, landed `eddcca8b`, the story-telling fold of 2026-11-02, ED-IN-0311); the remainder's first step is still the diff against IN-37 and it has no consumer until a player seat exists | HELD · PARTLY LANDED | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |

`..._part4.md:292` (-04 content-owner entry)

### NM-W0 … NM-W9 — Narration packages (IN/WR) · BATCH B10-19 (NM-W0: B10-02, CLOSED, an EDIT whose row left at B10-02's close; NM-W2: B10-05, CLOSED, an EDIT whose row was deleted at B10-05's close; NM-W3: B10-01, an EDIT whose row is deleted in the adoption commit) · STATE as listed · R M2 (the any-seed story bar)
Home: `proposals/2026-10-13-narration-mechanisms.md` §4 (W0-W9). The proposal is PROPOSED, grade `paper`; nothing in W1-W9 had code, a test or a run when it was written. It names four decisions for Jordan (§7 there); they are in `-05`. Premises are one seed, two seasons.

| handle | package | state at HEAD | note |
|---|---|---|---|
| NM-W1 | render v0: an omniscient instrument chronicle (ranking tiers, appraisal, name fallback, per-person pages, anti-repetition, snapshots) | PARTLY LANDED | IN-37 (`bd5d5b45`) landed a narrower `harness/chronicle.py` (numbered lines of actor, verb, emitted kinds); W1's fuller specification was not diffed against it; [UNVERIFIED] whether v9's D1-b #1 is IN-37's render. **The story-telling fold of 2026-11-02 (ED-IN-0311):** the ranking-tier piece moves to CR-68 (B10-10, landed `eddcca8b`); NM-W1 stays HELD · PARTLY LANDED for its remainder (appraisal, name fallback, per-person pages, anti-repetition, snapshots), whose first step is still the diff against IN-37 and which has no consumer until a player seat (CL-SLICE / NM-W5) exists; NM-W4 to NM-W9 unchanged |
| NM-W2 | candidate-typing disposition: refusals as learning versus declined at formation | CLOSED INTO B10-05 | M19 taken (a), decline at formation row by row (`-05`); REM-21 to REM-25 decline at formation; REM-29 is the learning channel for capacity; DEC-12 keeps `finding.none` off the ledger. Its measured arm is `-08` HR-9's control (4); the row was deleted at B10-05's close with that reading quoted in the close commit `1d6cd152`'s body (default cross-person share read literally fails on seeds 0-4, 27.0% against 29.4%, taken on the executed-only share, 19.3% against 17.8%) |
| NM-W4 | a content-bearing record kind | UNBUILT | needs W2 and a working handover (`give` was attempted 14 times and executed 3 in the three seeds). PR #506's G-04(b) is a note here, not a new position: act-minted Propositions have predicate `''` in 52 of 52 (the narration proposal's figure, which the register reports and did not re-measure), so a `covenant` on one binds nothing; HELD with this package |
| NM-W5 | focalized journal on `person_q` | UNBUILT; released from M12 | M12 taken (a) in substance, without the §A.2 row; held on NM-W1 only; the amended entry is below the table |
| NM-W6 | fragment bake | UNBUILT | |
| NM-W7 | scale lines | UNBUILT | |
| NM-W8 | occasion ladder (replacing a per-season deck) | UNBUILT | decision 2 in `-05`: none, authored boot-time rows, or a per-season emitter |
| NM-W9 | conformance items (`Receipt.before/after` against 04 §B.9, and others) | UNBUILT | "not a narration dependency"; hash and golden moves declared |

**NM-W5, amended by the decision round** (B10-19; released from M12). Home: `proposals/2026-10-13-narration-mechanisms.md` W5, with the §A.2 row struck from its "Where" and "Co-edit" lines. NEEDS: NM-W1 (NM-W2 is discharged at B10-05). It slots by R8 into the next unopened code batch after NM-W1 lands its instrument control; it cannot slot earlier. HASH: EQUAL, asserted: `content_hash()` of `build_realm(0)` over two seasons is equal with and without a journal call per person per season. FALSIFIER: W5's three, the control for (1) being the instrument's field count over the same focalizer (above 0) against the journal's 0; plus a covered actor's act reaching the focalizer with `seen.who = None` prints unattributed (planted failure: `actor_of` passed in reddens). The no-row reading holds only if the journal reads what `person_q` may read (`04_CODE_ARCHITECTURE.md:169`); W5 also selects from Scenes (narration proposal `:283`): if Scenes are not person-side, the §A.2 row is owed and lands with NM-W5 as a Layer 1 hunk listed under "Layer 0/1 hunks" (M11 answered (a), ED-IN-0300; an unmarked anchor only `[ASSUMPTION; medium; Jordan to correct; revert: ED-IN-0300 reopened]`). `skills/prose-writer/SKILL.md:158` is narrowed in NM-W5's commit. BUILDER: `CLAUDE.md` §10's second tier. ASKS: M12 taken at step 5 ((a) over (b) on player experience; the Layer 1 half at step 4; (c) excluded by §C.11) `[ASSUMPTION; medium; Jordan to correct; revert: delete the function and test; restore the skill line]`.

### NM-W4  ·  STILL-NEEDED  ·  WR · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:259` (handle index row)

| NM-W4 | B10-19 | narration package (`proposals/2026-10-13-narration-mechanisms.md` §4) |

`..._part3.md:393` (batch card row)

| NM-W4 | a content-bearing record kind | HELD · UNBUILT | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |

`..._part4.md:292` (-04 content-owner entry): same section already copied under NM-W1

### NM-W5  ·  STILL-NEEDED  ·  WR · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:260` (handle index row)

| NM-W5 | B10-19 | narration package (`proposals/2026-10-13-narration-mechanisms.md` §4); released from M12, held behind NM-W1 only, slots by R8 after NM-W1 lands its instrument control |

`..._part3.md:394` (batch card row)

| NM-W5 | focalized journal on `person_q` (released from M12, taken (a) without the §A.2 row; the "Where" and "Co-edit" lines' §A.2 row struck) | HELD on NM-W1 (slots by R8 after NM-W1 lands its instrument control) · UNBUILT | E | NM-W1 | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |

`..._part4.md:292` (-04 content-owner entry): same section already copied under NM-W1

### NM-W6  ·  STILL-NEEDED  ·  WR · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:261` (handle index row)

| NM-W6 | B10-19 | narration package (`proposals/2026-10-13-narration-mechanisms.md` §4) |

`..._part3.md:395` (batch card row)

| NM-W6 | fragment bake | HELD · UNBUILT | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |

`..._part4.md:292` (-04 content-owner entry): same section already copied under NM-W1

### NM-W7  ·  STILL-NEEDED  ·  WR · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:262` (handle index row)

| NM-W7 | B10-19 | narration package (`proposals/2026-10-13-narration-mechanisms.md` §4) |

`..._part3.md:396` (batch card row)

| NM-W7 | scale lines | HELD · UNBUILT | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |

`..._part4.md:292` (-04 content-owner entry): same section already copied under NM-W1

### NM-W8  ·  STILL-NEEDED  ·  WR · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:263` (handle index row)

| NM-W8 | B10-19 | narration package (`proposals/2026-10-13-narration-mechanisms.md` §4) |

`..._part3.md:397` (batch card row)

| NM-W8 | occasion ladder (replacing a per-season deck) | HELD · UNBUILT | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |

`..._part4.md:292` (-04 content-owner entry): same section already copied under NM-W1

### NM-W9  ·  STILL-NEEDED  ·  WR · design-first, held: carry the ask, no batch · gate: design approved by Jordan or by merge · tier: opus

`..._part12.md:264` (handle index row)

| NM-W9 | B10-19 | narration package (`proposals/2026-10-13-narration-mechanisms.md` §4) |

`..._part3.md:398` (batch card row)

| NM-W9 | conformance items (`Receipt.before/after` against 04 §B.9, and others) | HELD · UNBUILT | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |

`..._part4.md:292` (-04 content-owner entry): same section already copied under NM-W1

### PC-06  ·  STILL-NEEDED  ·  PC · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a (K-5)

`..._part12.md:266` (handle index row)

| PC-06 | B10-Z | carried v9 position (`-04`) |

`..._part3.md:430` (batch card row)

| PC-06 | #445 recommendations ratified as intent: K-5 held (K-1 landed at B10-11b, `2c7f2658`) | HELD · LEAVE (K-5, unscheduled); K-1 LANDED; K-3 LANDED | E | — | — | carried in full: `-04` part 2 |

`..._part5.md:241` (-04 content-owner entry)

### PC-06 — #445 recommendations ratified as intent: K-5 held (PC) · BATCH B10-Z · STATE LEAVE (K-5, unscheduled); K-3 LANDED; K-1 LANDED at B10-11b (`2c7f2658`) · R —
- WHAT: Nothing in the #445 digest recommendations is still scheduled. K-1/K-5 (a `Combatant` built from the person; loadout as `hold` tenures) wait on `Person.attributes` (K-2), which builds only with its first reader. M-2..M-6 stay with PC-08. K-3 and the earlier items have landed.
- LANDED ALREADY: S-1 at B-E (`engine/season/harness/play_surface.py`, falsifier `engine/season/tests/test_play_surface_dispatch.py`; `ac9724fc`); M-1/S-4 and S-2/L-1 at B-L (`9ad86e87`); K-3 at B-S (`1023197b`, B-S closed `6e833a57`, #500) — its EXIT is read under head §0.5 (`engine/season/hole_register.yaml` H-238; H-239 the gate's row), and its FALSIFIER's Coherence clause is unobservable at B-S (HANDOFF_IN, the B-S row).
- REMAINING UNBUILT: [v9 WHAT, full text: no digest recommendation is still scheduled. K-1/K-5 (the `Combatant` built from the person; loadout as `hold` tenures) are NOT scheduled: they need `Person.attributes` (K-2), which builds only with its first reader (K-1/K-6), and "K-2 is not ratified". M-2..M-6 (engagement cadence, wound state between engagements, the Plan layer, duel mode, the grid as mass battle) stay with PC-08; J-15 (#445 `05` §4.1, §4.2) is ask-then and attaches to M-2.] K-1, K-5, K-2 (and with it M-2..M-6 -> PC-08).
- GATE: DEPS K-2 -> K-1/K-5. K-2 is CR-20 (B10-10, `Person.attributes`); K-1 LANDED at B10-11b (`2c7f2658`, closed; ED-IN-0347, AR-48: the seam sets each `Combatant` field from `Person.attributes` by PC-14's `registry_key` map, absent keys at the class default, by `party_end`'s precedent). K-5 stays held (kit is CP-T03-03's). K-1's EXIT: a person with authored Strength 6 fights as Strength 6; CONTROL: an all-absent realm reproduces the pre-item hash; HASH: a declared MOVER wherever an authored person fights.
- EXIT and FALSIFIER: EXIT "`python -m engine.season.harness.register --requirements` — no R-row's `measure:` or missing-mechanism text names K-1 or K-5." FALSIFIER "an R-row, or a `hole_register.yaml` row, citing K-1 or K-5 as its cause shows 'unscheduled' wrong, and the item is scheduled the day that is read."
- HASH MOVERS: none stated for the LEAVE items (K-3's three sweep arms are declared corpus movers, H-239).
- HOLES AND LEDGER IDS: H-238 (SUPERSEDED as a blocker by head §0.5, 2026-10-13), H-239 (gate 30 shipping; 0 the control; arm 50 declared not run), H-85 (G1: the verb gate half is built at K-3; the knowledge-KIND half is not — `thread_substrate` is read by no code in `engine/season`); K-1..K-6; J-15.
- ASKS ATTACHED: J-15 (#445 `05` §4.1, §4.2: do unwatched fights resolve in one act or span scenes?; does duel mode open any closed moment, recommended no) — asked when M-2 is scheduled (PC-08).
- RE-BASE: B-S (#500) landed K-3 and the v9 entry records it. None found since.
- SOURCE: `v9_p7:42-47` (SOURCE there: `proposals/2026-09-30-character-and-play-surface/README.md:44-52`; `.../09_the_character_sheet.md:128-132`); state-index row `v9.md:284`.

### PC-08  ·  STILL-NEEDED  ·  PC · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:267` (handle index row)

| PC-08 | B10-Z | carried v9 position (`-04`) |

`..._part3.md:431` (batch card row)

| PC-08 | Phase 4a / 4b / 5, WS-7, channel-leverage: design-gated backlog | HELD · LEAVE (named, unscheduled; J where Jordan names one) | E | — | — | carried in full: `-04` |

`..._part5.md:253` (-04 content-owner entry)

### PC-08 — Phase 4a / 4b / 5, WS-7, channel-leverage: design-gated backlog (PC) · BATCH B10-Z · STATE LEAVE (named, unscheduled; J where Jordan names one) · R —
- WHAT: Keep named and unscheduled the design-gated backlog: Phase 4a, 4b and 5, WS-7, the channel-leverage residual (4c), and the #445 items K-4, V-3, V-2, U-4, U-5, K-6, so none is dropped. The R2 capstone finding is history to read first if Phase-C recalibration starts.
- LANDED ALREADY: K-4's role by IN-12 step 9 `train` (`996c16dc`, B-Q).
- REMAINING UNBUILT: [v9 WHAT, full text: abilities-as-access depth (4b), the game-theoretic layer (4a), the contact axis (5), WS-7 multi-combatant (also gated on ED-911) and the channel-leverage residual (4c, where Jordan sets per-paradigm strength) are design-gated, "no immediate action". #445's M-2..M-6 cover live parts; J-15 attaches to M-2. Items named so none is dropped (README ranks at `README.md:62-64, :71, :76, :81`): K-4 (`09_the_character_sheet.md:131`, the `practice` verb as `capability`'s writer) SUPERSEDED by IN-12 step 9's `train` (`996c16dc`; J-13 (iii), RS-21 item 10 [medium; Jordan to correct]); V-3 (`10_verbs_and_attributes.md:199`, `faculty(domain)` as sole owner of the aptitude slot) stays LEAVE, presupposes `Person.attributes` (K-2, unscheduled, PC-06); U-4 and K-6 (`08_mass_battle_units.md:128`, `09_the_character_sheet.md:133`: an `Officer`'s charisma and cognition from the commander's attributes) stay LEAVE ("after K-2"); U-5 (`08_mass_battle_units.md:129`: a stat preset for `mounted_archers` or a written reason it has none; "trivial, any time") stays LEAVE — no season field carries a troop type other than infantry (`_MVP_SUBUNIT_SHAPE`, `massbattle.py:159-161`) — and attaches to the same first position as J-19 (MB-07r, landed `aa6871b8`); V-2 (`10_verbs_and_attributes.md:198`, standing rule: an attribute reaches a verb only through a faculty and only if the verb's row has `contests:`) is not a position — it binds the author of every `verb_table.yaml` row IN-08 and IN-12 add (three rows declare `contests:` today: `fight` `verb_table.yaml:466`, `march` `:601`, `tell` `:889`, read 2026-10-06). The R2 capstone finding (reach-class weapons above the contested-balance target against arming) is history: read first if Phase-C recalibration starts (`HANDOFF_PC_history.md`, heading "R2 (closing-distance/facing/grip/contact redesign)").] everything else named.
- GATE: STATE LEAVE; DEPS none scheduled; EDITS none.
- EXIT and FALSIFIER: EXIT "`python -m engine.season.harness.register --requirements` — no R-row's measure names any of them; for the channel-leverage residual, `python systems/combat/combat_engine_v1/workbench/balance.py context` is the re-measure once Jordan scopes it." FALSIFIER "an R-row, or a `hole_register.yaml` row, citing one as its cause shows 'no R-row moves on it' wrong and the item is scheduled the day that is read."
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: ED-911, K-4, V-2, V-3, U-4, U-5, K-6, M-2..M-6, J-13 (iii), RS-21 item 10, IN-12 step 9; no hole rows.
- ASKS ATTACHED: channel-leverage per-paradigm strength (4c, Jordan sets); J-15 (ask-then at M-2).
- RE-BASE: B-Q (#490) landed `train`, which superseded K-4. None else found.
- SOURCE: `v9_p7:49-54` (SOURCE there: `registers/handoffs/HANDOFF_PC.md` rows; README `:44-52`); state-index row `v9.md:285`.

### SC-02  ·  STILL-NEEDED  ·  SC · U3 B27-sc-proceedings (IS-B2-SC-10: 'after B24'); CR-57 only after CR-48 · gate: the entry's falsifier + `aperture 2 0` `open_case`/`determine` counts · hash: movers declared · tier: opus

`..._part12.md:306` (handle index row)

| SC-02 | B10-Z (HELD: the design is written, the re-source build awaits its approval; left B10-13 at its close) | carried v9 position (`-04`) |

`..._part3.md:442` (batch card row)

| SC-02 | `22a` -> `23` -> `22b`, RESIDUE after B-P: design written (`proposals/2026-11-08-sc02-reception-proofs-own-commit-design.md`), PROPOSED; the re-source build awaits its approval | HELD on the design's approval (ratified on merge by ED-1094's default) · BUILD (the re-source of `reception` and `proofs`) when released, slotted by R8 | M | — | — | carried in full: `-04` |

`..._part4.md:698` (-04 content-owner entry)

### SC-02 — `22a` -> `23` -> `22b`, RESIDUE after B-P (SC) · BATCH B10-Z (HELD; left B10-13 at its close) · STATE DESIGN WRITTEN for A1-08's option B (`proposals/2026-11-08-sc02-reception-proofs-own-commit-design.md`, PROPOSED, ratified on merge by ED-1094's default); the re-source BUILD is HELD on that approval · BLK for the rest: H-218, H-219, H-221, H-222, ED-SC-0040 (held; each left item sits at its hole row) · R —
- WHAT: residue only. Each left item sits at its hole row and is not buildable without the input named.
- LANDED ALREADY: at B-P (commits `07510eae..eba20137`): `22a` steps 17, 18, 20 (`reception`, `proofs`, route erosion; `Claim.visibility` KEPT, its reader runs from the fold); `23` (`SeatId`, `load_all()`, loader invariants 4's flat half and 7's fold half); `22b` step 23 (on a hand-built world), step 24 (except its Failure arm), step 25's writer and reader, step 26 (a test); step 27 found nothing to delete.
- REMAINING UNBUILT: step 19 (investigation products) STOPPED, superseded by #453 K-36 and K-37 (H-218; G2: SUPERSEDED, the asked-subject residue "3 of 8 asked subjects not co-located never learn they were asked" stays open); step 21 (failure's severity by observer set) STOPPED, no row has a Failure consequence to gate (H-219); step 24's Failure arm (H-221); step 25's rest (examiner witnessed examining; a forged record counted as a proof until examined), unscheduled; step 23's contradictory-commitments and overdue-obligation sources (no measure exists, H-222) and its realm life (never fires in computed play until a writer of person-predicates exists, step 19); the F8 question: `reception` and `proofs` read other persons' ledgers at RESOLVE against `04` §B.2:250 (ED-SC-0040; answered, option B, A1-08): the design is written and the re-source build (`reception` and `proofs` read the actor's own ledger and the bench's public commits) is HELD on its approval.
- GATE: v9 states no GATE line. STATE line: "B-Z, held. BUILT at B-P (the commits `07510eae..eba20137` are their record)". DEPS "ED-SC-0040 (J) for the F8 question; step 19's writer for steps 21's and 23's realm life."
- EXIT and FALSIFIER: v9 states none.
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: H-218, H-219, H-221, H-222; limits of what was built: H-210, H-215, H-216 ("inert at the shipped ceiling; the mirror is total in play; the valence sweep is open; recusal; the bench's place; the uncapped arm's cliff"); per G2 also H-220 (`EventLog.append` takes any kind; refusal built at the fold; SC-02 `23` loader invariant 7) and H-223 (standing-gap bands, `22b` step 23); #453 K-36, K-37; ED-SC-0040, ED-SC-0039.
- ASKS ATTACHED: none open. ED-SC-0040 is answered (A1-08, ANSWERED-DOC, option B: re-source from commits). The design is written; its merge ratifies it by default (ED-1094), and its build, CP-T05-01 and CP-T05-02's part (i) (`hearing`, `hearing_step`) wait on that approval in B10-Z and slot by R8 into the next unopened verb-cluster batch when it is released. The only source text concerns the obstacle reading live commits to a charge, and no charge carrier exists (H-227).
- RE-BASE: B-P closed `eba20137` (#490) — v9 was written after it; the entry is "RESIDUE after B-P". B-O (#488/#489) FI-01/FI-02/FI-03 are the executors that superseded step 19. None found since B-P.
- SOURCE: `v9_p6:22-25`; state-index row `v9.md:271`.

### SC-07  ·  STILL-NEEDED  ·  SC · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: CR-36/CR-37 (the FA carry)

`..._part12.md:310` (handle index row)

| SC-07 | B10-Z | carried v9 position (`-04`) |

`..._part3.md:434` (batch card row)

| SC-07 | #445 P-4, V-4, V-5: attach to the proceedings design | HELD · BLK:a carrier per item | E | — | — | carried in full: `-04` |

`..._part5.md:277` (-04 content-owner entry)

### SC-07 — #445 P-4, V-4, V-5: attach to the proceedings design (SC) · BATCH B10-Z · STATE BLK:a carrier per item · R —
- WHAT: Carry three #445 digest recommendations that wait on a proceedings carrier: P-4 procedure before the vote (agenda, motion order, recorded defeat), V-4 one non-combat acquisition layer, V-5 gloss `survey`/`surveil` by their roots. They stay reference until each has a carrier.
- LANDED ALREADY: —. (SC-01 landed, B-N closed `cf69ceed`; it built nothing for this entry.)
- REMAINING UNBUILT: [v9 WHAT, full text: three digest recommendations waiting on the proceedings build. P-4: procedure before the vote (agenda control, chair's order of motions, recorded defeat). V-4: one non-combat acquisition layer, in the proceedings design. V-5: gloss `survey`/`surveil` by their roots, and name any rostered speech kind other than `construe`. They are NOT in the set ED-IN-0290 ratifies as intent (S-1, M-1/S-4, S-2/L-1, K-3, U-3, P-1..P-3); they stay reference until each has a carrier.] all three items, each awaiting a carrier; then `arrangements.yaml: speech_kinds`, `verb_table.yaml` notes. V-5's gloss half is "trivial, any time" (`README.md:71`) but v9 gates the whole row on SC-01.
- GATE: "BLK: a carrier per item"; v9 BATCH "B-Z (held: each item builds when a carrier exists) [ASSUMPTION; medium; Jordan to correct — basis: #445's own 'SC, when un-held'; revert: Jordan slots an item into the next SC batch]".
- EXIT and FALSIFIER: EXIT P-4: "a carried-and-vetoed motion persists as a citable record (`02_against_precedent.md:83`)"; V-4: "two persons differing only in an acquired technique choose differently in one situation (`10_verbs_and_attributes.md:200`)". FALSIFIER "a motion vetoed in a seeded proceeding that leaves no Record fails P-4; two persons identical but for the technique that choose identically fail V-4; both must be seen failing on the tree before the build."
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: #445 P-4, V-4, V-5; ED-IN-0290, ED-IN-0286.
- ASKS ATTACHED: none beyond the assumption's revert ("Jordan slots an item into the next SC batch").
- RE-BASE: SC-01 (B-N) and B-P landed without building a carrier for these. None found since.
- SOURCE: `v9_p6:70-76` (SOURCE there: `proposals/2026-09-30-character-and-play-surface/02_against_precedent.md:83`, `10_verbs_and_attributes.md:200-201`, `README.md:71, :79`); state-index row `v9.md:276`.

---

### SE-04  ·  STILL-NEEDED  ·  SE · U3 B12-world-motion-and-ground, as the positions the SE proposals amend (R-SE-01..05, -19: `unified/U5_FINDINGS_CLOSURE_U5d.md:244`); CR-40 first, then CP-T08-01 onward in the card order · gate:…

`..._part12.md:311` (handle index row)

| SE-04 | B10-16 | carried v9 position (`-04`) |

`..._part3.md:177` (batch card row)

| SE-04 | H-170/H-171: cohort weight, the territorial carry, a cohort's internal spread (CAST-POPULACE) | Part (b) only: released from M11 (ED-IN-0300), still BLK:(b) IN-44 (Layer-1 `Rung.envelope`; unscheduled in B10-Z, slotted by R8, the row re-derived by symbol and (RULED)-checked at its anchor before it is listed or landed); (c) closed at ladder step 2 (no spread at shipped weights, H-39's ruled shape; M1 answered); (a) LANDED | E | — | — | carried in full: `-04` |

`..._part4.md:761` (-04 content-owner entry)

### SE-04 — H-170/H-171: cohort weight, the territorial carry, a cohort's internal spread (CAST-POPULACE) (SE) · BATCH B10-16 · STATE (b) released from M11 (ED-IN-0300; IN-44 row 16, Layer-1 `Rung.envelope`), in B10-Z with IN-44's rows, unscheduled and slotted by R8; (c) CLOSED by M1 (no spread at shipped weights); (a) LANDED · R —
- DECISION ROUND: (c)'s M1 hold is answered: no cohort spread at shipped weights, closed at ladder step 2 (H-39's ruled shape; `-05` M1). The vector half is SE-06's (B10-07b built its pursuit half; the conviction half is in B10-Z). Part (b) is released from M11 (`Rung.envelope`'s writer or its Layer-1 deletion; the row is re-derived by symbol and (RULED)-checked at its anchor before it is listed or landed); the GATE's (c) clause and the (c) falsifier below are v9's and no longer schedule work.
- WHAT: Carry what `24f` left at the territorial scale: (b) H-171, a producer for `Rung.envelope` (or its Layer-1 deletion), eaters in corpus worlds; (c) CAST-POPULACE, a cohort's internal spread so riots, flight and conversion stop being single decisions. (a) cohort weight is done.
- LANDED ALREADY: (a) `dd0a1c5a` (H-170's `cite:`); IN-08 cells commit `0f998f64` (the pursuits half of (c)); (b) was STOPPED at its design step at B-T (H-171) — nothing built, `Rung.envelope` stays.
- REMAINING UNBUILT: [v9 WHAT, full text: (b) H-171: what `24f` did not carry to the territorial scale — corpus worlds seat no eater (`corpus_run.build_at`), `Rung.envelope` has no producer, a cohort's own deliberation. (c) CAST-POPULACE (#457; ENP v2 proposal 13, ratified AS INTENT only if the construal answers so): a cohort's internal spread and pursuits for its 37 cohorts, so riots, flight and conversion stop being single decisions.] (b) either a writer for `Rung.envelope` or the field's deletion — deleting a field `04 §B.3` declares is a Layer-1 edit, Jordan's (IN-44 row 16); (c) the cohort spread.
- GATE: (b) BLK:IN-44 — "stopped at its design step at B-T (H-171; the IN-44 table row in `_part8`; the field stays: `Rung.envelope` has no writer, and deleting a field `04 §B.3` declares is a Layer-1 edit, Jordan's)". (c) J: Jordan's construal of a cohort's internal spread (`proposals/2026-10-04-forcing-churn-and-the-story-bar.md:171`, "Jordan (construal)"), on v9's STILL HELD list; J-1 and J-5 are answered and "do NOT cover it". DEPS IN-08 -> (c) (D, landed). EDITS `engine/season/cohorts.yaml`, `loop/census.py`, `harness/populated.py::seat_cohorts`, `state/carriers.py` (`Rung.envelope`).
- EXIT and FALSIFIER: EXIT (b) `python -m pytest engine/season/tests/test_territorial_subsistence.py -q`; (c) the falsifier test. FALSIFIER "a cohort splits on one claim — two members of one cohort at one rung hold a differing claim and diverge in one season; control is the shipped cohort (one decision for all), which must still hold when the spread is off. Part (b)'s `envelope`: either a writer exists or the field is deleted; a field with neither fails."
- HASH MOVERS: declared, by schema alone: "`Rung` is digested as `repr(sorted(vars(obj).items()))` (`state/world.py:181-182`) and `envelope` is one of its declared fields (`state/carriers.py:965, :975`), so deleting it moves every hash and a writer moves every world where it writes."
- HOLES AND LEDGER IDS: H-170, H-171; IN-08, IN-44, J-1, J-5; #457; ENP v2 proposal 13. (`hole_register.yaml:3700-3725`.)
- ASKS ATTACHED: the construal of a cohort's internal spread (on the v9 still-held list) is answered by M1 at step 2 (above); the Layer-1 deletion of `Rung.envelope` is released from M11 (ED-IN-0300): an unmarked anchor may be edited in the PR and listed under "Layer 0/1 hunks"; a (RULED) mark stops the row.
- RE-BASE: B-T (#503, subject "SE-04 (a)") stopped (b) at its design step and appended H-171 limit 2; v9 carries both. B-V's guard cohorts (IN-60) are the seat-cohort vector SE-06 re-reads. None other found.
- SOURCE: `v9_p6:82-88`; state-index row `v9.md:278`.

### SE-06  ·  STILL-NEEDED  ·  SE · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: CR-107 (B11-F1)

`..._part12.md:312` (handle index row)

| SE-06 | B10-Z (HELD) | carried v9 position (`-04` part 2); released by M1: MEASURE then BUILD in B10-07b, where its pursuit half landed (`bcaf1d519`); its row moved to B10-Z at the close, HELD for its conviction half (four named residues) |

`..._part3.md:439` (batch card row)

| SE-06 | ED-IN-0293 row 1 reading (b); SE-04 (c)'s VECTOR half: every cohort's CONVICTIONS, from its territory (the pursuit half LANDED at B10-07b, `bcaf1d519`) | HELD (moved from B10-07b at its close; not decided against): no source for an `altonia` concern member; no Piety Track start value for T16 (Schoenland, cohort S-037); the two quarantined Piety Track start tables disagree on T1, T2, T3, T6, T13 and T14 and which to use is unruled; no rule splits one bipolar track into unipolar `affiliation_roster` intensities, `inner_tradition`'s share included; `valoria_geography_v30.yaml: spiritual_weight` examined, not a basis · BUILD (data) when a source or a ruling releases it; ruling: ED-IN-0352 item 7; carrier: CR-107 | M (when built) | — | — | carried in full: `-04` part 2 |

`..._part5.md:101` (-04 content-owner entry)

### SE-06 — ED-IN-0293 row 1 reading (b); SE-04 (c)'s VECTOR half: every cohort's CONVICTIONS, from its territory (SE, IN) · BATCH B10-Z (HELD; moved from B10-07b at its close, where the pursuit half landed) · STATE HELD (the conviction half; not decided against) · R R-06 (contributor)
- WHAT: the conviction half of SE-06: give each of the 37 cohorts the convictions (`Person.conviction`, over `affiliation_roster`) of its territory, the way the pursuit half gave it pursuits. Cohorts get no goals. There is no spread (SE-04 (c) is closed by M1: no spread at shipped weights).
- DECISION ROUND: M1 NARROWED (`-05`) took the vector half, "cohorts get territory vectors if the source exists" `[ASSUMPTION; medium; Jordan to correct; revert: delete the `temperaments:` block]`. The MEASURE read the source: `territory_temperaments_v30.md` carries a scalar pair per territory (alpha on outcomes, beta on conduct) and no conviction content, so the pursuit half is a stated translation and the conviction half has no source.
- LANDED: the pursuit half, B10-07b's SE-06 `bcaf1d519` (pin fix `bcff7ecf4`): `engine/season/cohorts.yaml: temperaments:` read by `harness/populated.py::temperament_rows` and applied by `seat_cohorts`, the one rule `data/pursuits.py::temperament_pursuits`, `[ASSUMPTION; medium; Jordan to correct; revert: delete the block]`. R-06's fifth conjunct (every acting person carries a pursuit vector) reads 83 of 83 by `python -m engine.season.harness.decision_spread --persons`. Landed dependencies: IN-63, IN-64 (D, landed `2f0c0227`); IN-62's `decision_spread` (I, landed `2f0c0227`).
- REMAINING UNBUILT (four items, the residue of the conviction half): (i) no source for an `altonia` concern member (`descriptor_registry.yaml: affiliation_roster.concerns`); (ii) no Piety Track start value for T16 (Schoenland), which holds cohort S-037; (iii) the two quarantined Piety Track start tables (`conviction_track_v30.md`, `peninsular_strain_v30.md`) disagree on T1, T2, T3, T6, T13 and T14, so which to use is unruled; (iv) no rule splits one bipolar track into unipolar `affiliation_roster` intensities, including `inner_tradition`'s share. `valoria_geography_v30.yaml: spiritual_weight` was examined and is NOT a basis (a territory's institutional capacity, not belief). Built, it would add a `conviction` map to each `temperaments:` row, read by `seat_cohorts` and validated through `data/affiliations.conviction_map`.
- GATE: a source or a ruling for the four items above (Jordan's content); the position slots by R8 when released. DEPS SE-06 -> IN-36's guard cohorts (I: the rule is re-read for them, B-V); the v9 edge SE-06 -> SE-04 (c) lapses with (c)'s closure. RULING RECEIVED (ED-IN-0352 item 7, 2026-11-08): convictions are authored per cohort row, several per settlement; the loader path is CR-107 (`-11` §3, B11-F1); SE-06 owns the conviction content and re-bases on it.
- EXIT and FALSIFIER: 37 of 37 cohorts hold a conviction map over `affiliation_roster`; two cohorts in one territory identical (declared); a cohort whose territory has no conviction row -> `Unspecified` naming it; **hash MOVED, declared.**
- HASH MOVERS: declared MOVER when built.
- HOLES AND LEDGER IDS: ED-IN-0293 (row 1 reading (b), row 2), ED-IN-0296, ED-SE-0056 (reserved), H-54, H-194, IN-62, IN-63, IN-64, IN-36, R-06.
- ASKS ATTACHED: none open. H-233 and IN-36's defaults are M1's residue, confirmed at the default (ED-IN-0301), and do not hold this position.
- SOURCE: `engine/season/cohorts.yaml` (the comment above `temperaments:`); `v9_p6:90-95`; state-index row `v9.md:280`.

### WR-01  ·  STILL-NEEDED  ·  WR · U3 B35-wr-thread after `09_WR_B_threadwork_session_and_practitioner` edits 1-2, in the card order CR-13, CP-T07-02, -03, -05, -09, -04, -06, -07, -10, -08, -11 (IS-B3-WR-01, changes 1-5) · gate:…

`..._part12.md:313` (handle index row)

| WR-01 | B10-15 | carried v9 position (`-04`) |

`..._part3.md:151` (batch card row)

| WR-01 | `27` remainder: the R-14 practitioner-resilience term, the `engine/season/` reach | BLK (narrowed): a working with a cost running in the season (its M2 slot answered: the attribute at `attr.mind.will`, which CR-84 names Spirit, Will being Spirit's alias) | E | IN-32 | — | carried in full: `-04` |

`..._part4.md:723` (-04 content-owner entry)

### WR-01 — `27` remainder: the R-14 practitioner-resilience term, the `engine/season/` reach (WR) · BATCH B10-15 (last, after IN-32) · STATE BLK (narrowed): a working with a cost running in the season (its own condition; the M2 slot question is answered) · R —
- DECISION ROUND: M2 answers what fills the slot (`-05`): Will (Spirit is Will's alias), read as CP-T07-02's `spirit` reads it, through a registered `faculty` addend active only where the carrier (CR-20) holds a value. WR-01 stays BLK on its own condition. NEEDS: IN-32 (same batch, earlier; order).
- WHAT: Give the R-14 practitioner-resilience term its season reach: the in-module half (`RESILIENCE_GAIN`, `resist_coherence_cost`) is built, but nothing in `engine/season/` supplies `actor.resilience` or a gain. It waits on a working with a cost running in the season.
- LANDED ALREADY: in-module half `0a690b30` (B-D3); WR-01..03 landed in-module; `27` BUILT 2026-10-01 (PR #451); IN-06 re-review `759eefb8` and IN-35 `23b33e9e` (B-S).
- REMAINING UNBUILT: [v9 WHAT, full text: B-D3 built the in-module half: `operations.RESILIENCE_GAIN` (shipped at control 0; `RESILIENCE_GAIN_SWEEP = (0, 1, 3)`) and `operations.resist_coherence_cost`, applied to every practitioner's working cost via `operations.charge_working` in `operations.py`, `collective.py`, `opposing.py`. Remaining: the reach — nothing in `engine/season/` supplies `actor.resilience` or a gain. The two unruled things (the slot's name and what fills it; where the gain lives) were answered by IN-06's re-review (§6 item 11) [ASSUMPTION; medium; Jordan to correct]; "what fills the slot waits on J-9 / K-2".] the season reach, once a working with a cost runs in the season. B-S built nothing for it ("a `Fixtures` gain would have no reader, ID-13").
- GATE: DEPS IN-06 (satisfied `759eefb8`); a working with a cost running in the season (D) (`proposals/2026-10-07-unplugged-systems-replug.md` §6 item 11). EDITS `engine/season/` once that working runs.
- EXIT and FALSIFIER: EXIT "observed when a working with a cost runs in the season (unobservable at B-S, nothing plugs): a plugged row's deletion refuses in a fresh subprocess and one seed twice in one process gives one hash; plus `python -m pytest tests/valoria/test_threadwork_resilience.py -q`, 0 failed." FALSIFIER "at gain 0 the plugged practitioner's costs equal the unplugged ones; at gain > 0 a practitioner with resilience takes strictly less than one without, on one planted pair, in a season run."
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: H-94 (cited), ID-13, R-14, WR-SCOPE, `27`; WR-05 = IN-06 + IN-35 (both landed B-S).
- ASKS ATTACHED: J-9 / K-2 — what fills the resilience slot (J-9 is the Godot-version item, now ED-GO-0002; K-2 is `Person.attributes`, built by CR-20): answered by M2, Will (above; M2 NARROWED, its reverts are `-05`'s).
- RE-BASE: B-S (#500) re-reviewed IN-06 and landed IN-35; the v9 entry records "B-S built nothing for it". None found since.
- SOURCE: `v9_p7:77-82` (carried v8 block `:69-75`); state-index row `v9.md:288`.

### §2:CP-T03-06  ·  STILL-NEEDED  ·  see CP-T03-06

`..._part12.md:40`

| CP-T03-06 | B10-11 | completion item (home: `proposals/2026-10-23-subsystem-completion/`); its park trigger met by CR-16: DESIGN-FIRST then BUILD, last in B10-11; since the story-telling fold of 2026-11-02 (ED-IN-0311) MEASURE first (the survivor's `regard` toward his opponent), then DESIGN-FIRST, then BUILD, or CUT |

### §2:CP-T03-10  ·  STILL-NEEDED  ·  see CP-T03-10

`..._part12.md:44`

| CP-T03-10 | B10-11 | completion item (home: `proposals/2026-10-23-subsystem-completion/`) |

### §2:CP-T06-08  ·  STILL-NEEDED  ·  see CP-T06-08

`..._part12.md:66`

| CP-T06-08 | B10-14 | completion item (home: `proposals/2026-10-23-subsystem-completion/`) |

### §2:ED-1043 the mass-battle god-file split  ·  STILL-NEEDED  ·  see ED-1043

`..._part12.md:347`

| ED-1043 the mass-battle god-file split | LEAVE (named, unscheduled) | a behaviour-neutral refactor with no request and no M1 juncture; trigger: a position edits `modules/mass_battle/orchestration.py` (B10-12's CP-T04-01 and CP-T04-03, or CR-12); then that position's first commit extracts only the functions it touches, hash EQUAL (`-06` part 3 §4) |

### §2:ED-WR-0005 C-TW-4, C-TW-6, C-TW-8 and the anchoring cadence cap  ·  STILL-NEEDED  ·  see CR-13

`..._part12.md:348`

| ED-WR-0005 C-TW-4, C-TW-6, C-TW-8 and the anchoring cadence cap | PARKED / LEAVE | C-TW-4 is parked with past-pulling (`subsystem-completion-07` §3, M9); C-TW-8 is unplugged per IN-06; C-TW-6 has no carrier until CP-T07-02 lands; the cadence cap was never ruled, so a design call waits for Jordan |

### §2:ED-MB-0045 the CellTable owner and item 4  ·  STILL-NEEDED  ·  see ED-MB-0045

`..._part12.md:349`

| ED-MB-0045 the CellTable owner and item 4 | LEAVE | trigger: a position adds a per-cell map in `modules/mass_battle` (the owner comes before new maps); item 4 stays under Jordan's cell-is-the-primitive directive (ED-MB-0040) |

### §2:ED-SC-0001 the combat armour-tier and ability sweeps  ·  STILL-NEEDED  ·  see ED-SC-0001

`..._part12.md:350`

| ED-SC-0001 the combat armour-tier and ability sweeps | LEAVE | trigger: CP-T03-03 or CP-T03-04 builds (M2 released both into B10-11, JQ-2 (1) yes); then run the sweeps |

### §2:`covenant` formation (PR #506 G-04 (c); 0 of 70)  ·  STILL-NEEDED  ·  see CP-T09-03

`..._part12.md:351`

| `covenant` formation (PR #506 G-04 (c); 0 of 70) | MEASURE, then LEAVE (no new position) | stays at MEASURE at B10-06's close (H-156's row, REM-28's why-refused line); CP-T09-03's exit names `referent_class` on `covenant` as the next link (`-09-build-B10-17`). Trigger for a position: CR-14's pooled census at B10-06's close reads `covenant` attempted and never executed after B10-05 (`-06` part 4, G-04 and G-13 rows). READ AT B10-06's CLOSE (`7362fa46f`): the trigger's condition holds in the realm (`aperture 4 s`, seeds 0 / 1 / 2: `covenant` attempted 14 / 27 / 21, executed 0) and in the corpus (`covenant` in `corpus_run`'s 'only refused'; `requirements.yaml` R-05); no position is written here, and the next link stays CP-T09-03's `referent_class` on `covenant` |

### §2:H-90 sovereign power and Parliament as a constraint  ·  STILL-NEEDED  ·  see CR-35..CR-37, IN-48 (the FA carry)

`..._part12.md:353`

| H-90 sovereign power and Parliament as a constraint | LEAVE (named, unscheduled) | the row is `ruled` canon with no builder; trigger: an SC `vote` position, or an R-04 grand-strategy reading names it. The Parliament half now has two positions of its own: CR-34 (B10-13) counts a vote at a sitting and CR-38 (B10-19, design-first) is the seating; sovereign power stays LEAVE on this trigger (`-06` part 2, H-90) |

### §2:social-contest wording rows left unscheduled by the build-all fold of 2026-11-02  ·  STILL-NEEDED  ·  SC · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:354`

| social-contest wording rows left unscheduled by the build-all fold of 2026-11-02 | LEAVE (named, unscheduled) | terms as a periodic reason for a sitting (reasons-to-convene RL7; it reverses the resolution design's default of no term and a term needs a renewer): trigger, CR-58 landed and a seat shown to need renewal; faction expectations and poles for Schoenland and "faction x", and a Church goal engaging `solmund_orthodoxy`: authored content, Jordan's (P11), trigger, his authoring them (until then those two factions read 0.0 for every person, a measured empty standpoint) |

### §2:`depose` (M8; the verb suite's PARK row, verbs-14:187)  ·  STILL-NEEDED  ·  see CR-37

`..._part12.md:355`

| `depose` (M8; the verb suite's PARK row, verbs-14:187) | CLOSED (M8 corrected) | answered by `revoke` under `joint_concurrence` (CR-37, B10-17; H-L0-9 applied in PR #507): the throne is revoked through the Holy See's concurrence with a carried Parliamentary motion, two persons' acts; the deposed King keeps `off_duke_valorsmark` until his death or release. Jordan's 2026-10-26 request selected the form M8's own revert named (`-05` M8); the Royal Deposition conjunction (`proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:628`) is restated as each concurrer's motive, never a gate, and is not a precondition. `depose` is not a verb, so no row is added [ASSUMPTION; medium; Jordan to correct; revert: `off_king` null, `depose` PARKED with M8's trigger (H-90's sovereign power built, or a ruling on that conjunction)] |

### §2:H-207's vacancy motive (`revoke`'s owner for R-05)  ·  STILL-NEEDED  ·  see CR-54

`..._part12.md:356`

| H-207's vacancy motive (`revoke`'s owner for R-05) | DESIGN-FIRST residue, no v10 position | a vacancy read as a need (`confer` onto a seat vacated of its own accord) is H-207's remaining path; it owns `revoke` for R-05 and is a named residue, not a permanent one. No v10 position builds it since CP-T02-04's cut, so R-05 cannot read `met` in v10. Trigger: a design for that motive is written and approved (`-06` H-207). CR-37 (B10-17) adds a hand-built `revoke` route on the throne only, with no computed route, so this residue is unchanged |

### §2:the deed lie (H-198 rule (ii))  ·  STILL-NEEDED  ·  WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:358`

| the deed lie (H-198 rule (ii)) | LEAVE (unbuilt; on GO-15's freeze list) | CR-27 builds the cell lie only. Trigger: a deposit that can hold a deed `False` and a reader that pairs it |

### §2:the Goldenfurt deck (28 cards)  ·  STILL-NEEDED  ·  WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: a named card passes the world-card schema

`..._part12.md:361`

| the Goldenfurt deck (28 cards) | NOT RECEIVABLE AS WRITTEN (the second decision round, item 2) | its engine (a pressure Π, Directives, place-held ledger tags) is refused by T-a, T-h, T-i, AX-2 and the Rung NEVER line, and it rests on a document Jordan marked IDEAS (`engine/season/rosters.yaml:79-80`). Reopens card by card: a position that names a card and passes it through CL-EVENTS commit (3)'s schema |

### §2:the eleven named cards  ·  STILL-NEEDED  ·  WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:362`

| the eleven named cards | NOT RECEIVABLE AS WRITTEN (the second decision round, item 2) | each card's effect is a write into a stored aggregate or a fiat outcome, and nine of the eleven triggers read an aggregate; Olafsson Exposure's trigger (an Overwhelming act at a place) is a lawful T-b hook and its effect is not. Reopens as the Goldenfurt deck does. Jordan's figure 45 = 6 + 28 + 11 holds on his three sources; "19 distinct named cards across two documents" is [UNVERIFIED] (sampled, not counted) |

### §2:the arcs (55 numbers, 58 arc cases)  ·  STILL-NEEDED  ·  WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a (standing rule)

`..._part12.md:363`

| the arcs (55 numbers, 58 arc cases) | NEVER RUNTIME DATA (ED-IN-0225 stands) | no arc is a carrier, a card field or a loaded row; CL-THRUST's B6.n draws on an arc only as a ladder position's named source, from the first two `ENDINGS_CLASSIFIED.yaml` classes (`-04`); ARC-46 to ARC-55 are classified by the file's own method by whichever B6.n position first draws on one, and no position is created for them. Case ids, the arc cases' included, are series-prefixed and a collision is recorded (CR-44). This line stands as written; CL-OPEN (B10-19, HELD on `-10` M26) would amend it to "no arc is a carrier or a loaded row; a row may quote one in `source:`", and the amendment lands only with CL-OPEN's approved design |

### §2:an emerged creed's `seize` (H-186)  ·  STILL-NEEDED  ·  FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:364`

| an emerged creed's `seize` (H-186) | GD-3 FAIL, recorded (not a stated limit, not a position) | an emerged faction keeps the land its founder held and receives land by cession, but cannot take more by `seize`, because a seat's faction is the authored `Office.faction`; this fails GD-3's violation test (`canon/04_game_design_constraints.md:29`). IN-30 ships with the FAIL named (`-06` H-186). The fix (a seat serving an emerged creed) or an amended GD-3 is `-05` §1a question (c); it blocks nothing built now |

### §2:the `heritage` member of `person_predicates`  ·  STILL-NEEDED  ·  SE · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: a writer of person-predicate claims (H-222)

`..._part12.md:365`

| the `heritage` member of `person_predicates` | named residue (no producer) | CR-30 gives `marks` its carrier, but no deposit mints a claim on the `heritage` member of `person_predicates` (`engine/season/rosters.yaml:641-650`). Trigger: a position that writes person-predicate claims through the channels (H-222's writer) |

### §2:the Cardinal electorate  ·  STILL-NEEDED  ·  FA · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:366`

| the Cardinal electorate | REF: content, not a position | by CR-35's rule (the live seats of the vacant seat's faction whose grant carries `determine`) only the Cardinal of Justice and the Senior Inquisitor elect the Confessor, so three of the four Cardinals do not vote; an authored electors list is AX-6's alternative and is Jordan's content (`-05` §1a question (b)). Default in force: the rule |

### DEF-2  ·  STILL-NEEDED  ·  IN · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:375`

| DEF-2 | the eight handoff rules (`requirements.yaml:55-58`) | 3: R-04's `met` (P2:211-217) reads no handoff; they are NERS S tests | deferred out of M1. SM-6 (IN-46) is the one on a row's path (REM-31). H-56 stays J.2 rank 6 | — |

### DEF-3  ·  STILL-NEEDED  ·  WR · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a · trigger: milestone M2

`..._part12.md:376`

| DEF-3 | THE BAR's ordering (4 of 72 determinations dated) | 3: P1 §1 M2 names THE BAR a candidate M2 gate, not an M1 conjunct | deferred to M2. REM-16 re-runs the figure so it stops being [RELAYED] | — |

### DEF-5  ·  STILL-NEEDED  ·  IN · with CR-07

`..._part12.md:378`

| DEF-5 | mapping between the three scale vocabularies | 1: H-89 (J.2 rank 5) holds `scale:` column's fate; stored verb×scale column refused (`verb | held at J.2 rank 5 | — |

### DEF-7  ·  STILL-NEEDED  ·  SE · with IN-52

`..._part12.md:380`

| DEF-7 | LF-1 (troops bounded by treasury) vs Jordan's 2026-10-16 wording | 1: LF-1 DELEGATED-RULED (P5 J.2 ask-then, IN-52), tagged revertible | carried; IN-52 ships OFF. Not an M1 conjunct | — |

### DEF-8  ·  STILL-NEEDED  ·  IN · U3 B02 (decide there)

`..._part12.md:381`

| DEF-8 | NERS X2 (move R-01/R-02 narrative out of `requirements.yaml`) | 5: would rewrite `measured:` blocks RB-1/RB-2b must append to | deferred until after RB-2's R-01/R-02 re-take | reopen: after RB-2 re-take |

### DEF-12  ·  STILL-NEEDED  ·  IN · see gap register

`..._part12.md:383`

| DEF-12 | H-185 (authored OUGHT's `predicate` does nothing) and H-191 (intent reconciliation read by nothing) | 3: neither read by any R-row's `met`; both `hole_register.yaml` rows with named owners (`q | deferred to owners; not M1 | — |

### DEF-10  ·  STILL-NEEDED  ·  IN · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:384`

| DEF-10 | NERS X5 (move `build_realm` out of `harness/`) | 5: no module owns world-gen yet (04 PART E step 9), "no new directory" binds | deferred; not M1 | — |

### DEF-11  ·  STILL-NEEDED  ·  IN · held residue, no work (v12 'held and leave' list), trigger unchanged · gate: none until the trigger fires · hash: n/a · tier: n/a

`..._part12.md:385`

| DEF-11 | loader invariant 5 (`writer:` column) | 3: 04 §B.13 decides it, agent work; but on no R-row's path and CLAUDE.md §0 scopes to M1 j | deferred. L1-3 states honest grade meanwhile | — |


