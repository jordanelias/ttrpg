# FI — adversarial steelman audit, addendum B (the full design set, the detective precedent, the evidence interface)

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: ad07a9a (working tree)

Addendum to `audits/08_FI_audit.md` (§0–§17, findings F-FI-01 to F-FI-10, resolutions R-01 to R-33). It does
not repeat that file; it completes the reading that file reports as not done, corrects it where the full
reading shows it wrong, and adds what the full design set, the precedent corpus and the surviving audits
warrant. Finding numbers continue at F-FI-11; resolution numbers continue at R-34. `PYTHONHASHSEED=0` on every
run; scratch output is under the session scratchpad, `runs/FI_B/`. Proposals named below are under
`proposals/2026-11-12-subsystem-audit-suite/proposals/`.

**Verdict of the addendum, in one paragraph.** The first audit's verdict stands and is sharper than it
knew. Read against its whole design set, fieldwork was designed as three games (exploration, investigation,
socializing) joined by an exposure meter and a case board, and the code holds the substrate of the second
only: a ledger that is a case board with no view, three graded looks at the world, and no way to ask, to
conclude or to accuse on what is held. The largest single obstacle to the detective game is new (F-FI-11):
**the hand that did a killing or a wounding cannot be passed on.** A witness can name the doer; nobody he
tells can, and the witness himself has nothing to say when asked about the killer. So testimony,
denunciation and an accusation built on report (the acts every precedent game and the pre-modern record
run on) cannot carry the one fact a murder case is about. It is a limit stated in two docstrings and
registered nowhere. With it repaired, the evidence interface in §B4 is buildable from parts that exist.

## B1. What was read

**Read first, so as not to repeat:** `AUDIT_BRIEF.md` (in full); `audits/08_FI_audit.md` (§0–§17, in full);
`proposals/08_FI_01` to `08_FI_05` (in full); `dossiers/08_FI.md` (in full); `audits/12_ARCS_adjudication.md`
(in full: at this reading it is a 15-line stub whose verdict line reads *"written at the end of the pass …
this line is replaced"*; it adjudicates nothing yet, so no arc dependency is taken from it).
For coordination: `audits/05_SC_audit.md` §16 and §17 (in full) and its headings; `proposals/05_SC_evidence_and_rebuttal.md`
(SC-P8) and `05_SC_playable_hearing.md` (SC-P3) in full; `05_SC_capability_surface.md` (SC-P7) and
`02_CHAR_capability_uses_table.md` to their resolution sections; `10_DICE_advantage_sources_for_the_arcs.md`
(head only); `05_SC_acquittal.md` (its gate and falsifier only).

**The fieldwork design set, `.designs/systems/fieldwork/reference/` (19 files, 284 KB; ARCHIVED-NOT-CANON):**

| file | how read | what it is |
|---|---|---|
| `fieldwork_v30.md` (916 lines) and `fieldwork_v30_infill.md` | in full | one document in two parts (skeleton and prose): §1 Depth Axis, §2 pool and transitions, §3 exploration, §4 investigation, §5 socializing and knots, §6 exposure, §7–§12 |
| `investigation_systems_v30.md` (474 lines) | in full | the four "investigation systems": NPC Population Engine, Investigation Interface (scene graph, Case Board), Dialogue Lattice, Response Resolution Matrix |
| `knots_v30.md` (377 lines) | in full | the unified Knot synthesis (formation, five use-sites, strain, break, rupture) |
| `fieldwork_investigation.md`, `fieldwork_socializing.md`, `fieldwork_exploration.md`, `fieldwork_exposure.md`, `fieldwork_godot.md`, `fieldwork_bg_v30.md` (+infill), `fieldwork_hybrid_v30.md` (+infill) | in full, by line difference against the parent and its infill (every line not byte-identical to a parent line was read; the rest is the parent, read above) | atomized copies of the parent's §3–§6, §8–§10, made 2026-04-13 and since drifted (F-FI-13) |
| `fieldwork_rationale.md`, `fieldwork_editorial.md`, `fieldwork_summary.md` | in full | §13 rationale; §12 open items and the PP-632 redesign note; the §11 table |
| `fieldwork_flow_skeleton_v1.md` | in full (the display cut the last long row of §7 at 1,300 characters; its subject, `apply_knot_loss` applying two of four consequence fields, was read) | a traced call structure of `systems/fieldwork/sim/` at `6545067`: three source files, two of which (`fieldwork.py`, `investigation.py`) no longer exist |
| `fieldwork_v30_index.md`, `investigation_systems_v30_index.md` | in full | generated heading maps; no content |

**Cross-cutting design documents the dossier lists (`.designs/systems/_architecture/reference/`):**
`auto_manual_resolution_duality_v1.md` in full; `player_agency_v30.md` §1 (the precedent analysis) in full;
`scale_transitions_v30.md` §3.9 and every fieldwork-bearing line. **By fieldwork-bearing line only, not in
full** (each was searched for fieldwork, investigation, evidence, knot, rumour, exposure, interview, case
board and lattice, and every matching line read): `videogame_mode_spec.md` (§1.3 whole), `complete_systems_reference.md`
(Part 5 and the Pressure Point lines), `integration_proposal_v30.md` (65 lines, including Mechanism 3, Gap 4
and Part 6's heads), `throughlines_complete.md` (T-02, T-30 and 45 lines), `engine_atlas_v1.md` (16 lines),
`campaign_architecture_v30.md`, `campaign_modes_v30.md` (+infill), `conflict_architecture_proposal.md`,
`early_game_ignition_analysis.md`, `companion_app_design_note.md`. `cogload_moderate_target.md` has no
matching line and was not opened. `[PARTIAL READ]` for all of these; nothing below rests on an unread part.

**Research:** `tutorials/T06_investigation.md` in full (309 lines); `dispositions/D_T06.md` in full (the file
holds Parts 1 and 4); `tables/R5_investigation_information.md` in full. The precedent companion: Part 1
§2.10 (adjudication and social contest) and §2.13; Part 2 §3.4 (the nulls), K5, §6 (steal / refuse), §7;
Part 4 R4, U-1 (the Disclosure Contract), I-8 and the refusal rows; Part 5 §12.9 and §12.10; Part 6 §13.7;
Part 7 §14.2. Parts 3 and 8 by heading only: they treat faction strategy, personnel and battle, not
inquiry. The companion has no investigation section of its own (its §7 says so). `research/historical/`
(three files, 122 KB): searched by keyword, six matching lines read (all on Inquisitor suppression and cell
resilience); it holds no research on inquiry, testimony or evidence, which confirms the first audit's null.

**`.audit/` (lesser weight; hidden; loaded by nothing).** Ranked by a keyword count across all 38 entries;
the four that bear on fieldwork, information, knots, the narrative engine or world churn were opened:
`2026-07-04-ners-qualitative-audit` (the audit file's head and every fieldwork line; `ed_options.md` E-12;
the four JSON working files filtered by keyword: 16 matching items read);
`2026-07-05-emergent-narrative-engine` (`narrative_engine_design_v1.md` in full; `…v2_churn.md` head, the
shade/trail passage, §5 the claim-grammar interface and §9.3 in full; `integration_with_ners_audit.md` by
line); `2026-08-08-world-churn-audit` (`00_findings.md` head, D5, D6 and the stub line; `06_master_synthesis.md`
by line, including the rumour prohibition); `2026-08-11-world-schema-gap-audit` (`02_verdict…` head and
lines; `05_second_adversarial_pass.md` and the gap registers by line). **Not read:** the two
`_workings_joined.md` files (252 KB and 777 KB) beyond keyword extraction; `05_key_catalogue.md`,
`04_throughline_permutations.md`, `01_plan.md` of the churn audit; the social-contest and combat entries
(the SC lane's). `[SKIPPED: size; the claims taken from this corpus are each re-verified below]`.

**Code:** `engine/season/queries/person_q.py` in full (1,442 lines); `engine/season/queries/inputs.py` in
full (604 lines); `loop/witness.py` `:264-336` and `:900-1019` (the found deposit and the told deposit),
`epistemic.py` `:329-404` and `:874-900`, `state/carriers.py` (the `Claim` class), `decision/options.py:1207-1219`,
`systems/fieldwork/sim/knots.py:315-380`, each to verify a claim made here.

**Hole register:** the full `cite:` of all 59 rows the dossier lists as primary, extracted by id from
`engine/season/hole_register.yaml` (129,934 characters; H-122 alone is 42,845). All read to the end.

## B2. Corrections to the first audit, and new findings

### B2a. Corrections (each is to a sentence of `08_FI_audit.md`)

| # | first audit | correction | evidence |
|---|---|---|---|
| C-1 | F-FI-07, R-14, §6a H-182: the knot's season form *"waits on `_eff_tie` (plan position `14`), which is CHAR's"* | It was built and reverted. Position `14` stopped on it; position `29f` was cancelled (Jordan, 2026-10-02: `systems/fieldwork/` stays the home); v9 IN-32 built `_eff_tie` and a `tied` term in `teller_weight` and was **reverted as falsified** (attempt `53ed995d`, revert `7c6df560`): the realm formed 11 to 13 live ties and the one reader never ran, because `teller_weight` is built only where a told claim carries a chain. The knot therefore waits on rumour traffic (`08_FI_02`), not on an effect. Layer 1 also decides two things the audit left open: `tie`/`knot` are two directed edges, one owned by each party, and strain is a Query stored nowhere (`04` §A.3 row 9), so the archived −5..+5 gauge cannot be a field | H-182 `cite:`, full text; R-34, R-48 |
| C-2 | R-22 and `08_FI_04` §4: `decision/budget.py` should count only `hold`s on an Office; gate *"`p_carin`'s budget unchanged by her first record"* | That one-line repair was measured at v9 IN-14 (2026-10-07) and **not landed**: on the 27 NPC-rung cases `attempt_cases` falls from 20 to 12 or 13 against a floor of 15 (`test_n3`), and R-03's `test_u2_the_one_round_arm…` reddens, because the NPC telling transport runs on the scene budget a Record's `hold` mints. The proposed gate cannot observe that cost. R-22 is re-sequenced, not withdrawn (R-39) | H-92 `cite:` |
| C-3 | §2 item 4 and §13 class D: a forgery's quality *"contests an examination"* | Inert at the shipped fixtures. At the shipped obstacle ceiling (2, equal to `obstacle_default`) the quality cannot raise a defaulted inquiry's obstacle, so quality 0, 1 and 3 are identical in play; with the ceiling off and quality 3, the composed obstacle exceeds twice a default pool and the examination is **refused**, so a good forgery becomes unexaminable, not harder to find | H-210 `cite:` (B-P Phase 1 reconciliation); R-40 |
| C-4 | `08_FI_03` §2: a new `observes:` column whose reads deposit *"when the act's band is `Partial` or better"* | The register already judged a degree-keyed product column *"beside those three tables would be a second owner of what a finding deposits"*. K-37 (ratified as intent, ED-IN-0288) forbids a wrong value on Failure; it does not forbid a true read. The column is kept and its band gate dropped (R-35) | H-218 `cite:` |
| C-5 | R-05 (the `unshared` slant) decided at ladder step 5 | Its narrow half is recorded in the tree as a follow-up, not built: *"`said_of` excluding the hearing's own `news.told` claim when a told copy of the topic is held — `R8.1`'s exclusion of `seen` is the precedent"*. Step 4, and it should ship as its own arm so its effect is separable from the preference tiers (R-36) | H-197 `cite:` |
| C-6 | F-FI-01 presented as found by the audit's probe | The register recorded the substance on 2026-09-04: *"three of `questions_for`'s four sources are pure WORLD reads"*, and that which question a person answers was then decided by the order of content-hashed claim ids. F-FI-01 stands and is older than the requirement text that contradicts it | H-122 `cite:` |
| C-7 | §16: the brief's list of games *"checked against `tables/REPO_MENTIONS.md` and the lane file"* | **Heavy Rain is named nowhere in the tree** outside the brief and the first audit (search of `research/`, `proposals/`, `.designs/`, `.audit/`, `engine/season/`). Danganronpa is named in the companion (Part 1 §2.10, Part 5 §12.9) and one `.audit` source file; *Immortality* only in the 2026-08-18 fieldwork proposal and `T08`. Nothing may be cited to Heavy Rain (R-49) | §B7 run 4 |
| C-8 | §7: companion Parts 2–8 not read | They hold two dispositions on exactly F-FI-09 that neither lane cites: **refuse** *"contradiction-matching as a primary political resolution … keep only inventory-as-argument"* (Part 2 §6 row 15; Part 4 §11.4), and **steal** *"investigation output caps a contest's ceiling via the existing `BandExtension`"* (Part 2 K5 and §6 row 6; Part 4 I-8). Both are applied in §B4 | companion, at those sections |
| C-9 | old findings carried without re-verification | Three are now false: D_T06 row 40 (*"`interrogate` is not a row at HEAD"*): `KIND_VERB["confession.made"] == "interrogate"`; H-169's *"a true sheet's `head` is `None` in every world the tree builds"*: true sheets name a head in 5 of 5, 17 of 17 and 20 of 21 cases (§B7 runs 2–3), so a forged sheet has no tell in its content; the churn audit's D6 (`apply_knot_loss` passes a conviction the callee does not know): the name is fixed and an unknown name raises, **but the `try/except (ImportError, AttributeError): pass` wrapper it also named is still there at both call sites** (`knots.py:347-364`, `:373-378`) | §B7 runs 1–3; `knots.py` |
| C-10 | §12 run 9: three-season runs not completed | Completed at seeds 0 and 1 (§B7 run 3). F-FI-02 and F-FI-03 hold at three seasons: chained claims 20 and 7, **all one hop**; found deposits held 0 and 0 against 52 and 54 forgings; `confidence.broken` 0; `speech.made` 0 against 23 and 34 `speech.unheard`; `matter.determined` 0 and 1; `examine` folded 0 times |  |

### B2b. New findings

#### F-FI-11 · blocks standalone play; degrades narrative (R-01, R-05, R-07) · The hand that did a killing or a wounding cannot be passed on

**Claim.** For the deed kinds several verb rows emit (`person_q.PAIRED_KINDS`: `person.died`, `body.changed`,
`tenure.closed`, `finding.made`, `news.told` and five more), a holder learns the doer only by pairing his own
untold `seen` claim with the deed claim (`person_q.deed_doer`). A telling passes one claim (`said_of`
returns one `Said`), so the hearer's told copy has no sighting beside it and **names nobody**; a told `seen`
is never indexed (`_seen_index` keeps untold claims only). The witness, asked about the killer, has nothing
to say: the deed claim's subject is the victim.

**Evidence (opened at the line).** `person_q.py:158-175` (`attributed_deeds`: *"A told copy carries no `seen`,
so a paired claim heard second-hand names nobody"*); `:236-247`; `:250-285`; `:546-549` (`legitimacy`:
*"second-hand news of a killing or a wound never moves legitimacy"*); `:1165-1201`.

**Falsifier run** (`hearsay_doer_probe.py`, hand-built ledgers, no World; §B7 run 1).

| arm | `deed_doers` | `attributed_deeds(K)` |
|---|---|---|
| witness W holds `(V, person.died)` and an untold sighting on V naming K | `('K',)` | the claim |
| what W would say of V | `Said(V, person.died, True, …)`: no hand | — |
| what W would say of K | `None` | — |
| hearer J, told by W | `()` | `[]` |
| J also told W's sighting in a second telling | `()` | — |
| **control:** J told an unpaired kind, `(K, record.forged, True)` | `('K',)` | the claim |

The control matters: for every deed kind one row emits, hearsay names its doer today. The tree has already
decided that a report may carry a hand; the paired kinds lose it by construction, not by ruling.

**In computed play** (`attribution.py`; §B7 runs 2–3). Seed 1, three seasons: one death by a person's act
(`capture`), seven persons hold a firsthand claim of it, **none can name a doer**; `deed_doers` with
`kinds: [person.died]` names anyone for 0 of 82 persons (0 of 83 at seed 0, where no death occurred). All 37
and 58 `body.changed` claims are unattributed; 37 of the 39 wounds at seed 1 have no hand (MATTER), so that
population is thin and the cause of the seven unattributed death claims was not isolated `[UNVERIFIED: which
of the pairing's stated limits applied]`. One event is an existence reading, not a rate.

**Status.** Stated as a limit in two docstrings; no hole-register row names it (search for *names nobody*,
*heard second-hand*, *second-hand news*: no row). Requirements touched: R-01 (propagation of who did what),
R-05 (`interview`'s answer, once CP-T06-05 lands, cannot name a hand), R-07.

**Narrative consequence.** No denunciation, no informer, no *"they say the steward killed him"*. A `goal`
whose object is `deed_doers: {kinds: [person.died]}` (the avenger, the inquisitor, the magistrate) has a
referent only for an eyewitness. A hearing's `proofs` about a killing can come only from a speaker who saw
it. The Foscarini shape the first audit wants (false testimony, a ruling on it, exposure later) cannot
begin, because testimony about a death accuses no one.

**Minimal fix at the owner.** `proposals/08_FI_06_testimony-names-a-hand.md`: the pairing travels with the
deed. `Said` carries the teller's own pairing; the told deposit mints the deed claim and its sighting on one
chain; `deed_doer` pairs a told deed only with a sighting told on the same chain. Decided at ladder step 4
(the unpaired kinds are the precedent), with *"only eyewitnesses and finders name a hand"* kept as the
control arm.

#### F-FI-12 · degrades narrative (R-05) · `examine` cannot form on a place, and the first lane's product for it does not reach it

**Claim.** `decision/options.py:1213-1214` derives `examine`'s `site` operand as the question's subject. A
question's subject is a person, a rung, a Record or a Proposition; D_T06's probe found it was never a Site
in 160 formed acts over three seeds, and `examine` folded 0 times in every run here and in the first audit.
`08_FI_03` §2 gives `examine` a product (`observes:` the site's condition and stores) and leaves the operand
as it is, so the product is attached to a row that never passes admission.
**Evidence.** The two lines; `research/game_precedent_suite/dispositions/D_T06.md` probe note and row 2;
§B7 run 3 (`examine` absent from the folded verbs at seed 1, three seasons).
**Consequence.** The one inquiry that reads a place (the Obra Dinn act: a later visitor reconstructs what
happened here) does not exist in play, so every finding is about a paper.
**Minimal fix.** R-37, in `proposals/08_FI_07_shortest-playable-case.md` §2: `site` ranges over the Sites the
actor's own ledger names (an operand bag, `marshal`'s precedent), and the fold's presence conjunct refuses
the rest.

#### F-FI-13 · hygiene · The design set is forked against itself, and the oracle implements one branch

The atomized copies drifted from their parent after 2026-04-13. Read side by side: Thread-Read's attribute is
Spirit in the parent and Attunement in `fieldwork_investigation.md`; a full Evidence Track resolves by itself
in the copy and only by a Reconstruct in the parent; `fieldwork_socializing.md` carries the stepped
Disposition table and, forty lines later, the rule it replaced (`max(1, base − Disposition)`); a failed Knot
formation costs Disposition −1 and four seasons (parent §5.6a), drops Disposition to +4 (`knots_v30` §3.2), or
costs nothing (the socializing copy); a Distant Knot becomes Close by three scenes with no roll (parent), by
a second roll at Overwhelming that resets strain to 0 (`knots_v30` §3.3), or shifts strain by −2 (parent
§5.6b); cited evidence gives +2D (parent §2.3, first clause) or +1D per Finding to a maximum of +2D (parent
§2.3, last clause; `scale_transitions_v30` §3.9). `throughlines_complete.md` records T-02 and T-30 as *"fully
implemented in investigation_systems"*, meaning written; the 2026-07-04 NERS audit (ratified as filed)
recorded the same document as audited by no lane (GAP-1), and the 2026-08-11 schema audit recorded that
fieldwork *"produced nothing"*. The lane has been the unaudited one three times.
**Resolution.** R-47: irrelevant to the game (nothing reads the archive; ladder step 2). Where a case file or
a proposal cites an archived term, the parent `fieldwork_v30.md` is the reading, and `knots.py` is not
evidence of any branch (it predates ED-912's gauge by its own header).

## B3. The full design set, read as a detective and noir game

### B3a. What the design is

Three activities on one Depth Axis (how far below the surface), each with its own track: **exploration**
(points of interest, found by a Discovery roll), **investigation** (an Evidence Track per question, filled
by six acts, closed by a Reconstruct), **socializing** (a Disposition per person, moved by seven social
acts). One meter joins them, **Exposure** against a derived **Cover**; one view shows them, the **Case
Board** and Journal. `investigation_systems_v30` adds the scene as a graph of five to nine nodes walked on a
time budget, a **Dialogue Lattice** of utterances gated by what the character is and holds (one gate is an
**Evidence Gate**: *"Your name is in the Inquisitor's report"* is sayable only by someone who holds it),
and a five-filter **Response Matrix** for how a particular person answers. Knots are the far end of
socializing: a bond that can be used as a channel and ruptures when private counsel is cited in public.
The design needs a GM in the places the lane research file lists (the hidden threshold, the false lead, the
Sincerity call, the complication), and that is why none of it was built as written.

### B3b. Element by element: does the code have it?

"Has" means executed in a seeded run; "partly" means the carrier exists and the game on it does not;
"lacks" means no carrier. Precedent in the fourth column is the game the design or the research ties the
element to.

| design element (archive reference) | code | evidence | precedent |
|---|---|---|---|
| **Case Board**: discovered facts as nodes, connections drawn at Reconstruct, persistent (`investigation_systems` System 2) | **partly**: the ledger is the board's data (typed triples with source, chain, confidence, age; grouped support over distinct origins is `LedgerReader._support`); no view, no connection object | `person_q.py:994-1112`; nothing renders a ledger (`08_FI_audit` §9) | Shadows of Doubt's board; Obra Dinn's book; Golden Idol |
| **Evidence Track**: a hidden threshold per question (3 / 5 / 8), no decay (§4.1) | **lacks, by ruling**: no stored magnitude, no GM to set a threshold; decay is ruled | R-33; ED-IN-0319 | none shipped that hides its threshold; Obra Dinn shows a blurred face instead |
| **Six investigation acts** (§4.2) | **partly**: six rows; three roll (`research`, `examine`, `surveil`), of which `examine` never forms (F-FI-12); three write nothing | first audit F-FI-03 | L.A. Noire (search), Shadows of Doubt (scan, look up, tail) |
| **Reconstruct**: the deduction, *"the investigation's climactic moment"*, with a wrong conclusion on Failure that the GM hides | **lacks**: the row emits and writes nothing; K-37 forbids an invented wrong value | H-218 `cite:` | Golden Idol; Sherlock Holmes: Crimes & Punishments; Lacuna's sheets |
| **Reliability tags** (seven, by act) | **partly, in another form**: provenance (`source`, `chain`) and carrier (belief or document) derive five; no "Thread-verified", no admissibility read | R-32; `rosters.yaml: proofs` unread | L.A. Noire's notebook has no grades; The Guild 2's evidence strength |
| **Interview through the Dialogue Lattice** (gated utterances; Evidence Gate; escalation to a contest) | **lacks the lattice; has the gate's rule**: saying requires holding (`tell`'s `own_ledger` cell); `interview` is a prompt that yields nothing; no turn, no state (H-336) | K-36; CP-T06-05 scheduled | Disco Elysium; L.A. Noire's Accuse-needs-evidence; Ace Attorney's present |
| **Response Matrix** (five filters on the answerer) | **partly**: the answerer's own chooser decides whether to `tell` or `lie` and (after `08_FI_02` §4) what; regard and pursuits stand where Disposition and Conviction filters did; no Information filter (Truth, TS) | first audit §15; ED-FI-0004's own demand for a one-line "why" is unmet (`Seen.why` is always `None`) | Disco Elysium; Pentiment's remembered choices |
| **NPC Population Engine** (territory ecology, genome, deviation roll) | **partly**: `build_realm` seeds 83 persons with pursuits, convictions and heritage; no ecology weights, no deviation | `harness/populated.py` (not re-read here) | Shadows of Doubt's generated citizens |
| **Scene as a graph of nodes on a time budget; Drift nodes on a clock** | **partly**: the scene budget and rounds are real (R-03); no node graph, no time of day | `decision/budget.py` | Pentiment's canonical hours; Lacuna (the design's own citation of it is unsupported: D_T06 row 41) |
| **Disposition track** −5..+5, stepped obstacle, decay, starting value by lifepath (§5.1) | **partly, as a read**: `regard` is computed when asked from stance rows and judged and told deeds; no stored track (ruling R7: no magnitude carrier) | `person_q.py:424-453`; R-45 | Pentiment's community opinion |
| **Social acts**: Read, Converse, Connect, Impress, Rumour, Negotiate, Gift (§5.2); Sincerity Gate (§5.3) | **lacks all seven as acts**; `argue`, `speak`, `tell`, `lie`, `give`, `forgive` stand nearby; nothing reads another person's interior (F8) and nothing *asks around* | `verb_table.yaml` rows | Disco Elysium's passive reads; Shadows of Doubt's bribe |
| **Knots**: formed at Bonded, used as a channel, strained, ruptured (§5.6; `knots_v30`) | **partly**: a `knot` Tenure admits a witness by `witness_key`; no producer, no strain, no rupture; the oracle is unplugged | C-1; H-331, H-332 | none of the detective set; CK3 hooks are the nearest |
| **Exploration**: points of interest by Depth, Discovery roll, hidden features (§3) | **lacks** | H-325, H-327 | Outer Wilds (knowledge gates traversal); Obra Dinn's unlocking decks |
| **Exposure and Cover**: a meter per territory with Noticed / Watched / Compromised (§6) | **lacks the meter; has its cause**: inquiring is witnessed by the room (`finding.made`, `seen{who}`), `conceal` re-anchors a deed for distant channels; `rosters.yaml` forbids a bare `exposure` name | first audit F-FI-06; R-46 | Shadows of Doubt's trespass and blown cover; Pentiment's *"they now know you are asking"* |
| **Contested investigation**: a Concealment roll sets an obstacle (§4.6) | **partly**: `Record.forgery_quality` enters an inquiry's obstacle and is inert at the shipped ceiling (C-3); a cover has no quality | H-210 | Shadows of Doubt's cover-up job |
| **Desperate Trail**: three failures raise the stakes; *"failures never produce nothing"* (§4.4) | **lacks**; the opposite holds: a Failure deposits nothing, a Partial closes the trail | H-314; CP-T06-03, -04 scheduled | Obra Dinn (every entry stays revisable) |
| **Fieldwork to Contest**: a Finding cited for dice; a public citation teaches the investigated person (§2.3, §2.5) | **lacks**: no act cites an item | F-FI-09; §B4 | L.A. Noire; Ace Attorney; Triangle Strategy |
| **Thread-Read** (§4.5) | **partly**: gated by sensitivity, writes nothing | H-331; B10-15 | none |

Count: of 17 elements the code has none whole, 11 partly, 6 not at all. Every "partly" has the same shape: the
**state** the element needs exists and is single-owned, and the **act or view** that makes it a game does not.

### B3c. Against each precedent game the brief names

| game | the loop it is known for (source) | what Valoria holds of it | faithful or not |
|---|---|---|---|
| Return of the Obra Dinn | replay a past scene at its remains; assert name, fate, killer; locks in threes (T06 §OD 2–3) | a later visitor learns nothing at a place (`examine` never forms); the assertion (name, fate, killer) is exactly a paired deed plus its doer, which only an eyewitness holds (F-FI-11); no verifier, by ruling | named, not built; the refusal of the lock is reasoned (it leaks: T06 §OD 7) |
| Shadows of Doubt | evidence objects, a board, lead chains, one graded field (the name), signatures by killer type | lead-following is the question agenda (D_T06 row 9: has); evidence decays (has); one covert kind, so no signature; inquiring is witnessed (has) | half understood: the simulation side is there, the case side is not |
| L.A. Noire | search a scene; judge each answer; **Accuse needs a held item**; a wrong answer loses information | "saying requires holding" is the engine's rule for `tell`, `survey`, `forge`, `reconstruct`; nothing is *presented against* a statement | the rule is understood and built; its use in a hearing is §B4 |
| Pentiment | finite hours; whom you eat with decides what you hear; accuse before a biased authority; no right answer; the community remembers | budget (has); presence as the strongest information act (has); a bench that judges without the truth (has in shape: `determine` reads no log); the accusation landing a consequence (0 and 1 determinations in three seasons) | the closest fit of the set, and the one the companion's Part 7 records as *"No. Fieldwork and social contest do not touch"* |
| Disco Elysium | passive checks surface what the character can notice; skills as voices; failure is content | every inquiry is an active roll; nothing surfaces unasked; `Failure` is silence | named only (CHAR's for the voices) |
| Ace Attorney / Danganronpa | press a statement; present a held item against it; one correct pair | the primitive (two held items on one cell disagreeing) exists person-side (`options._pair`, `record`); no statement is on a record to press | the companion refuses the *puzzle* and keeps *inventory-as-argument*; §B4 follows that |
| The Case of the Golden Idol | fill a typed sentence from collected nouns; the machine grades it | a conclusion as a typed Proposition is `08_FI_03` §3; nothing grades it, by ruling | understood; unbuilt |
| Outer Wilds, Her Story | knowledge is the only persistent state and gates where one can go | true of an inquirer by construction (findings are claims; candidates form on what is held) | built |
| Paradise Killer | the trial can be called at any time on whatever is held; the verdict follows the case made, not the truth `[M: from memory; the tree's own lines on this game were not opened here]` | a petition can be filed on any held claim; the bench's roll reads none of it | the shape Valoria is one operand short of |
| Blade Runner (1997) | the culprit set is randomised per run; clues are objects `[M; the first audit's reading]` | a seeded realm is that; the culprit leaves one kind of trail | named only |
| Frogwares' Sherlock Holmes | deduction board; a chosen conclusion and a moral choice, never corrected `[M; the first audit's reading]` | as Golden Idol | unbuilt |
| Heavy Rain | — | not named in the tree (C-7) | no claim |
| Lacuna; The Guild 2 (named by the tree, not the brief) | submit a hypothesis that may be wrong and live with it; evidence with strength and expiry weighed before rhetoric | claims decay and carry provenance (has); no submission | the two the code is nearest to |

**Nulls, restated with the companion's.** No surveyed game models the content of an argument (companion
Part 2 §3.4 item 1). None has an NPC build a case another NPC answers; none carries testimony between
simulated people as its information economy (first audit §16). Valoria is alone on all three, so its own
runs are the only evidence, and they read near zero.

### B3d. The shortest faithful playable loop

"Faithful" is taken from what the precedents share: something happened that the investigator did not see;
there is more than one way to learn of it (a place, a paper, a person); what is held is visible with its
source; a conclusion is stated at the investigator's own risk; an authority acts on the accusation whatever
is true; the world shows the consequence later; time is short.

| step | the player (or the chooser in his seat) does | carrier | exists? | needed change |
|---|---|---|---|---|
| 0 | enters a seeded place where a deed has been done and a paper handed on | `inquiry_world(seed)` | no | `08_FI_03` §1 (harness only) |
| 1 | holds the question: *who did this, and bring him before this seat* | a goal whose object is `deed_doers` (`person_q.deed_doers`, IN-67); its referents are the suspects his own ledger names, and it raises a standing `need` question each season | yes (11 such ambitions in `build_realm(0)`: first audit §12 run 2) | none: this is the case object (R-44) |
| 2 | looks: reads the paper (`research`), watches the place (`surveil`), examines the site (`examine`) | three graded rows; the observation deposit | two of three | R-37 (`examine` forms); R-35 (an admitted look teaches its reads at any band); B10-14 |
| 3 | asks: questions someone, who answers by his own `tell` or `lie` | CP-T06-05 | scheduled | F-FI-11's fix, or the answer cannot name a hand (`08_FI_06`) |
| 4 | reads his board: per subject, what he holds, from whom, how sure, how many independent origins | `sheet.chronicle` + `LedgerReader._support` | data yes, view no | `08_FI_07` §3 (a rendering; no state) |
| 5 | concludes: names a doer | `reconstruct` uttering a HOLDS Proposition | no | `08_FI_03` §3 (design-first) |
| 6 | accuses: petitions, the case is opened, he speaks **citing what he holds**; the accused answers | `petition`, `carry`, `open_case`, `speak` | rows yes; citing no | §B4; SC-P3, SC-P8 |
| 7 | the bench rules; he sees who is disposed of, who was believed, whose word fell | `determine`; `record`; SC-P6 for the second verdict | one verdict only | SC's |
| 8 | the scene ends: disposed, fled, budget spent, or four seasons | predicates over existing state | no | `08_FI_03` §5 |

**The cut that plays soonest** needs no engine change: steps 0, 1, 2 (`research` and `surveil` only), 4, 6
without citation, 8. It is a real loop on the season's own code path and it is thin: one route, nothing
asked, no conclusion, an accusation whose strength is the default roll. **The first loop that deserves the
word detective** adds steps 3 and 5 and the cited `speak`: that is B10-14, `08_FI_06`, `08_FI_03` §3 and the
interface of §B4, in that order. `proposals/08_FI_07_shortest-playable-case.md` states the cut, its edits and
its gate. One code path holds throughout: every step is a row the season loop resolves, with the investigator
on `play_surface.dispatching_chooser`; the duality doctrine's three fidelities (played, witnessed, auto) are
the same rows with a callback, with presence alone, or with the shipped chooser.

## B4. Evidence and argument: the interface for social contests, decision-ready

The full text is `proposals/08_FI_05_evidence-interface_B.md`, which supersedes `08_FI_05_evidence-interface.md`.
It reconciles three statements of the same interface: the first FI lane's (`cites`, a citation is a
telling), the SC lane's SC-P8 (typed entries on the case file, a struck stage), and the one the tree ratified
on 2026-07-05 on the since-retired Key substrate (`.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md`
§5: *a claim = rhetorical move × evidence binding*; an unbound claim is *bluster*; *investigation is the
evidence supply chain*; ED-IN-0011). The decisions, each with its reason:

| # | decision | why | differs from |
|---|---|---|---|
| E-1 | **One operand, refs only.** A citing act carries `payload["cites"]`: ids of claims in the citer's own ledger and of Records on his live `hold`. The proof kind is derived by one reader, never declared | a declared `kind` beside a derivable one is a second copy of a fact (§0.05 cl. 3) | SC-P8's `{kind, ref}` entries |
| E-2 | **What is entered on the case file is what was said, not a pointer into a ledger.** A cited claim is entered as its `Said` (the telling's own carrier: subject, predicate, value, confidence, chain) with the citer; a cited Record by its id | a later answer must be compared with the entered item, and the fold may not open the first speaker's ledger to do it (F8) | SC-P8 edit 2 (`ref`) |
| E-3 | **A citation is a telling.** Each cited claim is deposited to those present through the told channel | the room must be able to carry evidence out (NPC-086); disclosure is the price of citing (E-7) | first lane; kept |
| E-4 | **Both carriers, one fact each.** The case file holds the entry (it persists, and can be forged, seized or burned); the ledgers hold the told copies | they serve different readers and neither restates the other | first lane had no persistent record; SC-P8 had no deposit |
| E-5 | **Three ways to answer an item, all over held items, none over the log:** *contradiction* (the same cell, a different value); *impeachment of a document* (a held claim that the cited Record was forged: the found deposit already mints exactly `(record, record.forged, True)`, at `Partial` too); *impeachment of a witness* (the bench's own regard, through `reception`, which already reads what the bench holds of the speaker's deeds) | the second answers SC-P8's request for *"a finding on a Record that says whether it is forged"* with a claim that exists; the third needs no operand | SC-P8 (one relation); first lane (`rebuttals: float`) |
| E-6 | **An answer is a rolled act, and no item decides a case.** A contradiction strikes only by a `speak` that itself succeeds; the verdict stays a roll the standing items move by `proof_step` | the companion's refusal: contradiction-matching is *"a puzzle with one solution, not a debate"*; *"in a political trial the winner is often the side whose evidence is worse"* | — |
| E-7 | **Bluster is the control, and citing costs disclosure.** An act that cites nothing rolls as today. A cited item tells the room what the citer holds and from whom, puts a forged paper where it can be examined, and can be struck | the 2026-07-04 NERS audit (ratified) found the archived *"Recall +2D near-costless citation"* trunkless; no penalty number is invented | — |
| E-8 | **A killing can be cited only once its hand travels.** `08_FI_06` is this interface's precondition for any matter about a death, a wound or a seat's closing | F-FI-11 | both lanes |
| E-9 | **Not taken now: the `BandExtension` ceiling** (an unsupported case may not reach Overwhelming) | `determine`'s three non-Failure bands open the same edge (H-301; H-162 item 2), so the veto would change nothing; it becomes live the day `Tenure.degree` has a reader | companion I-8 |
| E-10 | **Left to SC, named:** precedent as a proof kind (a held claim of an earlier `matter.determined`); the opponent's own live `commit` cited against his plea (the ratified design's *commitment store*); a judge whom evidence moves more or less (the archived Pressure Points; SC-P7's `trait_advantages` is the door) | each is the consumer's design | — |

The brief's five questions, answered for the engine as it would stand after this interface and its
precondition: a contest takes evidence as a typed input (the cited items); an argument is refuted by a held
contradiction or a held finding; a case's strength comes from what is held, witnessed and cited (and its
absence is the plain roll); an NPC builds a case (the chooser forms `cites` variants as Candidates, SC-P3
edit 2) and another answers it by the same row; a falsehood wins until someone holds the thing that answers
it, and then its citer's word falls with every judge who learns of it (`record`, `reception`).
**Conflicts with ruled items, named and not resolved:** proofs on the obstacle against the archived dice
(ED-SC-0034, SC's G-33); the single `speak` act against item-by-item presentation (the nested run is
unbuilt); hearing by presence (H-323: a citation reaches the whole room, and a private showing of evidence
to one judge is not buildable); no verifier (kept: every comparison is of two held items).

## B5. Capability authoring: perception, deduction, interview and forgery as data

Not redone here: the existing owner and the merged target are in `02_CHAR_capability_uses_table.md`
(`capability_uses` rows for where a capability enters a person's own choice) and `05_SC_capability_surface.md`
(SC-P7: `lie → copying`, `interrogate → inquiry`, and `trait_advantages`); the first FI audit's §14 lists
this subsystem's reads. What the full design set and this addendum's proposals add is the list of rows a
designer would author for the four detective skills, and which of them have a reader today.

| skill, in the tradition's words | where it would enter | owner row | reader today? |
|---|---|---|---|
| **Perception / Notice** (seeing what is there) | the pool of `examine` and `surveil` | `verb_capability: {examine, surveil} → <vocation>`; `vocation_attribute` | yes (`faculty`); one vocation, `inquiry`, serves all three looks (R-31: splitting is two data rows) |
| **Notice against Stealth** (seeing who, when he hides) | the obstacle of a look against a covered deed | `vocation_attribute.opposed_by`; the cover's quality on `Record.forgery_quality` (`08_FI_03` §6) | no: `opposed_by` is an empty map; a cover carries no quality; C-3's ceiling applies |
| **Research / Lore** | the pool of `research` | as Perception | yes |
| **Deduction** | the pool of `reconstruct` (its band decides whether the conclusion names the hand) | a `verb_capability` row for `reconstruct`; it becomes a graded inquiry | no: the row is ungraded (`graded_inquiries` has three members) |
| **Interview / Interrogation** (getting an answer) | the asker's side of the questioned person's `tell` (CP-T06-05: *the answer is a contest*) | `verb_capability: interview`; SC-P7's `interrogate → inquiry` | no row for `interview`; SC-P7 covers `interrogate` |
| **Insight / Sense Motive** (weighing an answer) | how far a hearer credits what he is told | `capability_uses: told_claim_credit` (CHAR's table; today a literal at `options.py:1627`) | reader exists; ships at gain 0 |
| **Deception** | the pool of `lie` | SC-P7 edit 1 | no row today |
| **Forgery** | the quality `forge` writes | CR-94 (the forger's Coordination, ED-IN-0347) | fixture today; scheduled |
| **Document examination** (Forgery against Perception) | `research` or `examine` against `forgery_quality` | the existing obstacle term | yes, and inert at the shipped ceiling (C-3) |
| **Contacts / Streetwise** (hearing things) | none: who you know is ledger content | — | deliberately not a capability; a trait could bias `said_choices` later (CHAR's) |
| **Rhetoric with evidence** | `speak`'s pool; the proofs it cites | `verb_capability: speak → copying`; `cites` | pool yes; proofs after §B4 |

Two requirements follow for the holistic stage's merged table. First, a capability row needs a role
`opposes` with a reader (`_opposition_of`), or Notice-against-Stealth and Forgery-against-Examination cannot
be authored; today every opposed inquiry reads a fixture. Second, the obstacle ceiling decides whether any
opposed skill matters at all (C-3; R-40): authoring a master forger changes nothing while the ceiling equals
the default obstacle. Neither is an FI edit; both are stated so the merge does not ship a table whose rows
cannot bite.
**Axioms the full design names that the code lacks and the first audit did not list:** *help* (the archived
leader with two assistants, §3.2); *let it ride* (a failed attempt on one target may not be retried in the
scene; the loop has the opposite, a free retry bounded only by budget); *spend a meta-currency to lower the
difficulty* (Inspiration; `effort` is the one advantage source and is the nearest); *wound penalties on
physical inquiry* (DICE's advantage-channel proposal supplies the door).

## B6. Additional proposals, and the resolutions added by this addendum

**Proposals written by this lane** (all `## Status: PROPOSED`; none edits a first-lane file):
`08_FI_05_evidence-interface_B.md` (supersedes `08_FI_05_evidence-interface.md`);
`08_FI_06_testimony-names-a-hand.md` (F-FI-11); `08_FI_07_shortest-playable-case.md` (§B3d, F-FI-12);
`08_FI_08_knots-season-form.md` (C-1). Order across both lanes' FI proposals: CR-29 and `08_FI_02` (traffic),
`08_FI_01`, `08_FI_07` Cut A, B10-14, `08_FI_06`, `08_FI_07` §2, `08_FI_03` §3, `08_FI_05_B` with SC-P3 and
SC-P8, `08_FI_08` §3, then `08_FI_04` with R-39's amendment.

Ladder step: 1 superseded · 2 irrelevant · 3 a design document or plan answers · 4 precedent · 5 what the
architecture needs.

| # | what | kind | resolution (decided) | step | carried by |
|---|---|---|---|---|---|
| R-34 | the archived Knot strain gauge (−5..+5, stored) against Layer 1 (*strain is a Query stored nowhere*) and `Tenure.degree: Optional[str]` | design against Layer 1 | strain is a count over the pair's own Events since the knot opened (uses and neglect), read when asked; no field; rupture is a `release` the reader's threshold occasions as a question, not a MATTER write | 3 (`04` §A.3 row 9) | `08_FI_08` |
| R-35 | `08_FI_03` §2's `observes:` is band-gated; H-218 warns of a second degree-keyed owner | two owners | `observes:` reads deposit whenever the act is admitted, at every band; `finding_terms` stays the only band-keyed table; a refusal still teaches only its gating reads (CP-T06-04) | 3, 4 | `08_FI_07` §2 |
| R-36 | R-05's arm bundles two changes | measurement | ship the register's own follow-up (`said_of` skips the transport's event kinds) as arm `unshared`, and the preference tiers as a second arm `unshared_first`, each against `newest` | 4 (R8.1) | `08_FI_06` §5 (same owner, `said_of`) |
| R-37 | `examine`'s `site` operand is the question's subject, never a Site | wiring | `site` ranges over the Sites `ledger_names(p.ledger)` names; the fold's presence conjunct refuses the rest | 4 (`operand_bags`, `marshal`) | `08_FI_07` §2 |
| R-38 | a told paired deed names nobody | gap | the pairing travels with the deed on one chain; control arm off | 4 (the unpaired kinds) | `08_FI_06` |
| R-39 | R-22 (budget counts Office holds only) was measured and declined at IN-14 | superseded as sequenced | lands only after `08_FI_02`'s traffic arm ships, with `test_n3`'s `attempt_cases` read before and after in the same commit; until then it stays as H-92 records it | 1 | none (amends `08_FI_04` §4's order) |
| R-40 | a forgery's quality cannot affect a roll at the shipped ceiling, and makes the roll refuse with the ceiling off | number | the quality enters the examination's obstacle under the `ceiling_per_pool` arm (`SocialContestInput.ceiling_per_pool`, CP-T01-06), where the cap is solved per pool `[UNVERIFIED: read off the record's docstring; the arm was not run here]`; at the fixed arm it is declared inert in H-210's row. SC and DICE own the arm | 3 (H-213, CP-T01-06) | none (named for SC, DICE) |
| R-41 | two names and shapes for the citing operand (`cites` refs; `proofs: [{kind, ref}]`) | two readings | `cites`, refs only; kind derived (E-1) | 5 | `08_FI_05_B` |
| R-42 | a case-file entry that is a claim id cannot be compared without opening another's ledger | Layer 1 (F8) | the entry is the `Said` (E-2) | 5 | `08_FI_05_B` |
| R-43 | SC-P8 asks FI for a finding term saying a Record is forged | interface | none is added: the found deposit's `(record, record.forged, True)` is the item, at `Partial` and better (E-5) | 4 | `08_FI_05_B` |
| R-44 | what an investigation's "case" is, with no case object | unclear | the investigator's own goal with a `deed_doers` object (kinds, or `against` a patient): its referents are his suspects and its standing question is the case; nothing new is stored | 4 (IN-67's goal object) | `08_FI_07` §1 |
| R-45 | the archived Disposition track against `regard` | design against code | the code governs: Disposition is `regard`, computed at read; the seven social acts are not rows and are not proposed | 3 (ruling R7) | none |
| R-46 | the archived Exposure meter | design against code | no meter: for the scenario's instrument only, exposure is the number of distinct persons holding a `seen` claim naming the investigator at an inquiry, read resolver-side; no chooser reads it | 5 | `08_FI_07` §4 |
| R-47 | forks inside the archived design set | inconsistency | irrelevant to the game; the parent `fieldwork_v30.md` is the reading where a case file cites a term | 2 | none |
| R-48 | `_ch_witness_key` reads a `knot` undirected; `04:388` says directed | spec against code | the code is the defect: a person witnesses through a knot **he owns**; a mutual bond is two edges and reads as before | 3 | `08_FI_08` |
| R-49 | Heavy Rain in the precedent list | false referent | dropped; not named by the tree | 2 | none |
| R-50 | `knots.py` swallows `ImportError` and `AttributeError` at both lateral calls | hygiene | delete both `try/except` wrappers; an oracle that cannot import its callee should fail | 5 | `08_FI_08` |

**17 resolutions decided (R-34 to R-50).** None is a survivor.

**Survivors for Jordan added by this addendum: none.** Two candidates were run down the ladder and closed.
*Should hearsay name a killer at all?* Step 4: for every deed kind one row emits it already does (the
probe's control arm), so the paired kinds are an implementation limit, and the eyewitness-only reading is
kept as the control arm for Jordan to prefer if he wishes. *Is an investigation a case object?* Step 4: a
`deed_doers` goal and its standing question already are one (R-44). The first audit's two survivors stand.

**Arcs (§13 of the first audit), amended.** Classes G (testimony, confession, denunciation: 14 cases, 6
core) and E (an investigation that reaches a conclusion: 59 cases, 26 core) gain a dependency edge: any
case in them whose deed is a death, a wound or a seat's closing depends on `08_FI_06` before CP-T06-05 or
`08_FI_05_B` can represent it. The arc lane's file is a stub and supplied nothing to check this against.

## B7. Evidence log

All `PYTHONHASHSEED=0`. Scripts and outputs: session scratchpad, `runs/FI_B/`. No `pytest`; no `aperture`.

| # | command or probe | seed · seasons | outcome |
|---|---|---|---|
| 1 | `hearsay_doer_probe.py` (hand-built ledgers; no World) | — | F-FI-11's table; `PAIRED_KINDS` = `body.changed`, `capability.raised`, `confidence.broken`, `contest.undecided`, `finding.made`, `news.told`, `news.untold`, `person.died`, `pursuit.moved`, `tenure.closed`; control (unpaired `record.forged`, told) names its doer |
| 2 | `attribution.py 0 1` (plain `SeasonDriver.season`, post-hoc ledger reading; no wrapper) | 0 · 1 | hash `5ab73af282d0779646c38839fbab85d8`, 13,379 Events, 749 acts: **identical to the first audit's runs 4 and 5**, so this is the same world; `person.died` 0; `body.changed` 37 claims, none attributed; faction sheets: forged 16 with a head, true 5 with a head |
| 3 | `attribution.py 0 3`, `attribution.py 1 3` | 0, 1 · 3 | hashes `52ff67bc…`, `26d2091b…`; Events 74,510 / 68,159; acts 2,367 / 2,390; claims `firsthand` 20,734 / 20,325, `told_by` 14,272 / 11,159, `inferred` 345 / 387; largest ledger 831 / 865; chained claims 20 / 7, all one hop; found deposits held 0 / 0; `record.forged` 52 / 54; `record.given` 1 / 4; `cover.assumed` 34 / 39; `tell.refused` 81 / 110, `news.untold` 11 / 29, `news.told` 10 / 9; `confidence.broken` 0 / 0; `speech.made` 0 / 0, `speech.unheard` 23 / 34; `case.opened` 7 / 11; `matter.determined` 0 / 1; `person.died` Events 0 / 1; persons able to name a doer of a death 0 of 83 / 0 of 82; sheets: forged 52 / 54 with a head, true 17 / 20 with a head and 0 / 1 without |
| 3a | the same script at seed 1 with a hand census (`state/attribution.py::actor_of`) | 1 · 3 | `person.died`: 1, by a person's act (`capture`); `body.changed`: 2 by `capture`, 37 with no hand; folded verbs include `research` 171, `reconstruct` 151, `forge` 117, `surveil` 39, `conceal` 39, `give` 33, `interview` 29, `tell` 28, `argue` 19, `speak` 14, `lie` 10, `thread_read` 4, `determine` 1; **`examine` absent** |
| 4 | text search for each game the brief names over `research/`, `proposals/`, `.designs/`, `.audit/`, `engine/season/` | — | Heavy Rain: 2 files, both in this suite (the brief, the first audit); Unavowed: 0; Danganronpa: 11 files; the others as §B3c |
| 5 | roster and kind probe (`python -c`, `data/rosters`, `data/verbs`) | — | `covert_kinds` `('record.forged',)`; `proofs` `('record', 'testimony', 'oath', 'confession')`; `graded_inquiries` `('research', 'examine', 'surveil')`; `said_slants` `('newest', 'valence')`; `KIND_VERB['confession.made'] == 'interrogate'` |
| 6 | extraction of the 59 primary rows' `cite:` by id (`yaml.safe_load`, read-only) | — | 129,934 characters; H-22's `cite:` is empty |
| 7 | `git status --short` and `git diff --stat` at the end | — | no path outside `proposals/2026-11-12-subsystem-audit-suite/` is modified; the first lane's audit and its five proposals do not differ from HEAD; this lane wrote this file and four proposal files and ran no git write (some of them already show as tracked: something else commits the suite directory while lanes write) |

A first run of script 3a failed on an import path in the scratch script (`actor_of` lives in
`state/attribution.py`); the scratch file was corrected and re-run. No tracked file was written by any run.
Readings in rows 2–3 are single runs per seed: existence and count readings, not balance claims.
