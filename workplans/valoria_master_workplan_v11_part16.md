# Valoria master workplan v11 — the strife positions (T11 · lane IN)
## Status: PROPOSED, ratified on merge (ED-1094, ED-IN-0315).
## Lane: IN (cross-cutting).
## Grade under `CLAUDE.md` §0.2: `paper`. IDs allocated: none (ED-IN-0315 is the head's). Short form: `-11`, read after `-10`.

## 1. How to read

Format as `-04` §1: `### <handle> — <title> (<lane>) · BATCH <…> · STATE <…> · R <rows>`, then WHAT, LANDED ALREADY, REMAINING UNBUILT, GATE (with NEEDS), EXIT and FALSIFIER, HASH MOVERS, HOLES AND LEDGER IDS, ASKS ATTACHED, RE-BASE, BUILDER and SOURCE. Each strife entry adds four lines: **FILES** (what the position edits), **VERB CLUSTER** (whether it joins P13's serialisation), **LAYER 1** (the `04`/`01` row it touches, opened at the row, and whether it needs a hunk) and **N-LINE** (rule V1's form, restated at the batch's re-base). HASH MOVERS names, for a mover, the pre-change `build_realm(0)` reading it takes (P14: the previous item's recorded after-reading, not a fresh run). Seeds follow P10: a reading from seeds 1 and 2 is taken only where the batch declares a hash mover, and a batch close reads no further than three seasons, except that the strife instrument and the strife guard may be read at four seasons (P10's strife exception, Jordan 2026-11-04, ED-IN-0317); elsewhere a reading and a control read seed 0. The one exception is CR-78, whose flip re-reads HR-9's controls on the seed sets those controls are defined on for CR-28 (0-4 and 5-9, `-08` HR-9).

**The home.** Every entry's design home is `strife-00` (the batch it names in §8) and, for CR-75 to CR-77, `strife-01`. Both files are RATIFIED by Jordan (2026-11-04, *"Ratify strife master and kind list"*, ED-IN-0316), with the corrections this plan found made in them first and marked "(v11)"; the entry here is the plan's spec, and where it is more exact than the home it says so. `strife-00`'s R1 to R18 are Jordan's rulings of 2026-11-04; its assumptions A1 to A12 and `strife-01` §6's five calls (first taken by the orchestrator on narrative grounds at Jordan's instruction) are ratified with the files, each keeping its `[ASSUMPTION; medium; Jordan to correct]` mark and the revert `strife-00` §10 or `strife-01` §6 states, carried by the entries that rely on them. Ratification removed a hold, not a gate: no entry's GATE named an assumption, so none changed. No other ruling is asserted.

**The study.** The source of the move codes, the per-code `ends` counts and the terminal set is the claude.ai artifact `XDjCCRvbxiPS6sumpRtnte`, "Mechanics of Strife to c. 1600" (read through the Artifact tool's read action; `strife-00` read its rev 769 for the mechanics tab and rev 69 for the dossiers). No copy is in the repository. A3's cross-check (the 102 final moves against the study's nine case-mapping tables, `strife-00` §10) is owned by whichever session runs CR-78's flip; it is work, not a question.

**Positions, by batch.** B10-11: CR-72. B10-18: CR-73. B10-18c: CR-74. B11-S3: CLOSED (CR-75 to CR-77; its record is `-03` §1's paragraph). B11-S4: CLOSED (CR-78; its record is `-03` §1's paragraph). B11-S5: CLOSED (CR-79; its record is `-03` §1's paragraph). B10-Z (HELD, by the plan's R8, head §7): CR-80. CR-71 is CLOSED (B11-S2; its record is `-03` §1's paragraph). CR-70 is a retired handle (the story-telling fold dropped it, ED-IN-0311) and is not reused (P4).

**What is not a position, so nobody re-files it.** S1 and S1r are built (`60d13a7`, `79419b7`). `strife-00` §8 S2's lane for the foreign nations' natural-play frequency (H-233) is answered by S1r's readings (side O marches 12, 3, 4 and 6 at seeds 0 to 3, four seasons; `strife-00` §7's table row "unmeasured here" predates them); the frequency is answered in kind by Jordan (ED-IN-0317: a casus-belli rule, and for testing a cap of one march per season into each territory, both under IN-36 in B10-17). The bodies lane (DR, DN) is a reading at B10-18's close after CP-T10-05 (`-03` B10-18's exit): `age_step` and `illness_rate` are deferred by Jordan and stay at the control (ED-IN-0317, H-208), so natural death stays unobserved by design until he sets them. `strife-00` §0's `queries/situation_q.py` is not built: CR-76 and CR-77 place both readings in `queries/world_q.py` (CR-76, LAYER 1).

## 2. The positions


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

### CR-80 — The deck: world-build seeds per strife category (IN/WR) · BATCH B10-Z (HELD on CL-OPEN's build; slots by the plan's R8, head §7) · STATE BUILD (rows; shipped off; hash EQUAL) when released · R —
- WHAT: `strife-00` §8 S6: world-build seeds per category (A to I) through the schema of CL-EVENTS commit (3) (goal rows or yield scales, drawn once at build), so that every category can open in a seeded world without anything firing in a season (R1, R2; T-c). Rows only: the schema, and any widening of it, are CL-EVENTS (3)'s and CL-OPEN's (the one owner of the widening, `-10` §3). Each row is read from the study's occasion column (`strife-00` §2) and carries `[ASSUMPTION; medium; Jordan to correct; revert: delete the row]`; the switch is the Tensions switch, shipped off.
- LANDED ALREADY: none (CL-EVENTS (3) and (4) are B10-18's).
- REMAINING UNBUILT: the rows; their test.
- GATE: CL-EVENTS commits (3) and (4) landed (B10-18); CL-OPEN's build landed (B10-19, HELD on M26). Released, it slots by the plan's R8 (head §7; not `strife-00`'s R8, "People exist within flows") into the next unopened batch that edits `tensions.yaml`, else runs as its own sub-batch; released after B10-20 opens, it is a declared post-freeze change. NEEDS: CL-EVENTS, CL-OPEN.
- EXIT and FALSIFIER: on the test arm (switch on), each category's opening kind appears in the strife reachability report at seed 0; the loader refuses a row outside CL-EVENTS (3)'s schema. CONTROL: switch off reproduces the base hash. "It has no on-arm today": the on-arm flip is the Tensions flip already on B10-20's freeze row.
- HASH MOVERS: none (switch off). Released after B10-20 opens, a registry change re-exported through GO-09 with an `ED-GO-` row.
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: the rows' content beyond `[ASSUMPTION]` rows is Jordan's (P11).
- RE-BASE: CL-EVENTS (3)'s schema and CL-OPEN's widening as built.
- FILES: `engine/season/tensions.yaml`, `engine/season/tests/test_tensions.py`.
- VERB CLUSTER: no.
- LAYER 1: none beyond CL-EVENTS (3)'s.
- N-LINE: the deck — cut it and the gameplay experience is worse, because categories whose occasion no default world holds (a subject people under a burden, a servile population, an unpaid army) can never open, so R1 holds only for the categories the cast happens to seed.
- BUILDER: second tier for rows.
- SOURCE: `strife-00` §8 S6.
