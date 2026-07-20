# Cross-Reference Synthesis — 2026-07-13 Multi-Agent Audit

**Instruments:** mechanic_audit (all 8 subsystem heads — threadwork completed after the earlier crawler
passes were logged; see §4.2), module_adjudicator (full 27-module graph), vector_audit (status/blocked),
compliance_check (CI size gate).
**Synthesis inputs:** all four instruments' on-disk output + all four `crawler_log/*_delta.md` notes.
**Note on currency:** the three earlier crawler deltas (mechanic_audit, module_adjudicator, vector_audit)
were logged when only 6–7 mechanic_audit subsystems had landed and describe threadwork as absent; the
threadwork folder (5 files) has since completed on disk and is folded into this final synthesis. Where a
delta note says "7 subsystems" / "threadwork never ran," this report supersedes it.
**Governance discipline:** this document is analysis-only. No writes to `canon/editorial_ledger*.jsonl`,
`references/id_reservations.yaml`, or `references/audit_registry.jsonl` — those are owned by the run's
dedicated sequential registry step. No `ED-<LANE>-NNNN` IDs are allocated here.

---

## 1. Executive summary — corpus-health signal

Read together, the four instruments describe a corpus that is **structurally sound at the wiring
level but carrying a real, concentrated backlog of prose-level content defects** — not a systemic
break, but not clean either.

- **The Key-substrate wiring graph is close to closed.** module_adjudicator's machine pass returns
  22 violations / 61 warnings (exit 1, verdict OPEN), but the OPEN margin is fully characterized and
  contains **no missing-mechanism hole**: consume-closure 100%, cycles all annotated, gates /
  derivations / accounting-sequence all clean, emit-closure ~97.9%. 20 of the 22 violations are a
  single cross-scale down-seam cluster that canon (`scale_transitions §12.2`, ED-1038) explicitly
  exempts from the "missing channel" reading — a contract-annotation + assessor co-defect, not a
  design gap. Only **2 of the 22 are genuine substantive defects** (one mass_battle emit typo, one
  registry-hygiene gap).
- **The size/atomization gate is green.** compliance_check passed with zero violations. Nothing in
  the corpus is over its token cap today. (Caveat: the instrument's own crawler flagged a latent
  severity-misclassification bug — see §2.5 — but no file currently trips it.)
- **The mechanical prose has a steady stream of content defects** that only a section-by-section read
  catches. Across all 8 subsystems mechanic_audit covered, it surfaced **15 new, previously-unfiled P1
  findings** (plus module_adjudicator's 2, for **17 total**), heavily concentrated in
  settlement/territory (5) and mass_battle (2, plus adjudicator's 1), with threadwork adding one
  (a truncated override table) and faction/social/fieldwork/architecture the rest. The dominant defect classes are
  **internal self-contradiction** (a value or rule stated two incompatible ways in one doc),
  **stale/dead cross-references** (citations to renamed or nonexistent files), and
  **referenced-but-undefined mechanics** (a formula invoking a term with no definition).
- **One instrument saw nothing.** vector_audit is BLOCKED — its Stage 1–7 dispatcher is unimplemented
  and its last real baseline is 304 in-scope file-changes stale. The corpus-wide
  citation/terminology-drift detector this run needed most was the one that could not run, so the
  stale-citation defect class is being caught by hand, one subsystem at a time, with no backstop.

Bottom line: **no fire, but a filing queue.** The wiring is trustworthy; the prose needs a
reconciliation pass, and the settlement/territory and mass_battle subsystems need it first.

---

## 2. Convergent findings (2+ instruments independently)

Highest-confidence signals: each is independently supported by more than one instrument or more than
one check-angle. Citations give file+section on every side.

### 2.1 mass_battle is a multi-instrument provenance-integrity hotspot (3 distinct P1s)
Three separate P1-grade defects, same subsystem, three different files/layers, three different check
angles, none a duplicate of another:
- **mechanic_audit G1** (`mechanic_audit/mass_battle/gap_register_update.md`): two contradictory
  Ranged/Volley DR tables in `params/mass_combat.md` (PP-104 Heavy vs bolts=5/arrows=7 vs PP-188
  Heavy vs Piercing=3), neither marked superseded.
- **mechanic_audit G2** (same file): `mass_battle_v30.md` §A.14 "Woven units" fragment cites a
  compilation pass on `stage5_clocks.md`, which **does not exist** anywhere in the repo (self-flagged
  in-doc `[EDGE-06 — P1]`, never filed).
- **module_adjudicator P1-A** (`module_adjudicator/verdict_full_graph.md`): the mass_battle contract
  emits a fabricated `scene_outcome.battle_concluded`, mislabeled "§8.5 verbatim" — canon writes
  `scene.battle_concluded`; `scene_outcome` is only the family name.
- **Read:** all three are the same *class* — a false or broken provenance claim on mass_battle's
  canon surface. Treat as one consolidated MB-lane remediation batch (three EDs, or fewer if the
  ledger step merges), not three unrelated one-offs.

### 2.2 personal_combat Health formula — canonical authority independently corroborated
- **mechanic_audit GAP-PC-4** (`personal_combat/gap_register_update.md` + `formula_audit.md` A3.1):
  `params/core.md:158`'s Health row is ~7% drifted (pre-D-A formula) from `derived_stats_v30.md §4.1`
  and the live `combatant.py:35-42`.
- **module_adjudicator** (personal_combat CONFORMANT note + `module_map_flat.md` derivations): for an
  unrelated F1 write-legality check, independently anchors the *same* authority —
  `health_full = WI*(MaxWounds+1)+0.25*Str*End` (ED-1041 / `derived_stats_v30 §4.1`) — as canonical.
- **Read:** two instruments reading different corpora converge on `derived_stats_v30 §4.1` / ED-1041
  as *the* Health authority, confirming `params/core.md` is the drifted outlier. Strengthens GAP-PC-4
  if it is ever escalated past its current P2/no-ED disposition. **Not a new P1** (both instruments
  rate it below the P1 bar — the derived stat is `writable:false`, F1-clean, and nothing consumes the
  drifted copy in play), included here only as a convergence signal.

### 2.3 personal_combat "declared-but-dead" surface (pattern, 3 instances / 2 instruments)
- **GAP-PC-1**: `reopen`/`disengage` lever named across 3 docs, never built.
- **GAP-PC-2**: `seize` lever dead since 2026-06-05, yet `ability_armature.md §7` still lists
  `vorschlag`/`sen_no_sen` as live with "a positive, bounded edge" (internal contradiction).
- **module_adjudicator A4**: `scene.combat_felled` / `scene.combat_resolved` are registry-declared
  personal_combat emits with **zero wired consumers**.
- **Read:** personal_combat's "declared capability" surface has drifted from its "actually live"
  surface across three independent instances. No single instance is P1, but the pattern is worth a
  PC-lane housekeeping pass. **Not a P1** — included as a subsystem trend signal.

### 2.4 module_contracts.yaml — three-instrument convergence on one file
- **compliance_check**: measured at 14.4k/18k tokens (80% of cap) — passing, but the crawler flagged
  a latent severity-classification bug (see §2.5).
- **module_adjudicator**: names this file its regenerate-never-hand-edit source of truth and queues
  **4 edits** into it (P1-A remove spurious emit; P2-A propagate §12 transitions; P3-A wire
  env.crisis; P3-B reconcile loop annotation).
- **mechanic_audit G-13**: independently found the `social_contest` entry (L425–447) stale
  (`resolver: dice_pool`, predates the δσ rebuild) — already tracked `ED-SC-0008`.
- **Read:** a file explicitly designed to keep growing, at 80% of cap, with ≥5 pending edits queued
  from this run alone. Not a violation today; a named near-term collision risk.

### 2.5 compliance_check's own latent severity bug (self-flagged, corroborated by the queue above)
compliance_check's CI-mode inline logic only treats `on_exceed ∈ {flag_unknown_pattern,
flag_for_split, flag_for_next_session}` as warn-tier. `module_contracts.yaml`'s actual policy
(`atomization_rules.yaml:251-254`) is `on_exceed: "warn_only"`, **not in that set** — so if the file
ever crosses 18k, CI-mode falls through to error severity (blocking merge), contradicting the file's
own "expected to grow" intent. §2.4's queued edits make crossing plausible. **Candidate IN-lane fix**
(not a P1 today — no file trips it yet).

### 2.6 piety_track / conviction_track_v1.md — same file, two instruments, cross-lane risk
- **module_adjudicator P1-B**: `designs/personal/conviction_track_v1.md` (real piety_track home)
  absent from `canonical_sources.yaml`; only the territorial `conviction_track_v30.md` is registered.
- **mechanic_audit G-6** (`social_contest/gap_register_update.md`): "Piety Track" name collision
  between the 0–10 debate tracker (sourced to that same `conviction_track_v1.md`) and the per-territory
  BG stat — already tracked open as **ED-SC-0003** (SC lane, needs_jordan).
- **Read:** the adjudicator's registry gap is the contract-symptom of the naming-collision root cause
  mechanic_audit already has open in a *different lane*. P1-B must be filed **coordinated with
  ED-SC-0003** (cross-cite, or fold the registration into ED-SC-0003's remediation) so SC and IN don't
  independently resolve overlapping halves — possibly incompatibly (SC renames/retires the label while
  IN registers it under that same name).

### 2.7 settlement_layer Fort Level — complementary detection (syntactic clean masks a semantic P1)
- **module_adjudicator**: the `Fort Level → Garrison Strength` derivation
  (`Garrison Strength = Defense × 20 + Fort × 30`, `settlement_layer_v30 §1.3`) reports A10/A11
  gate/derivation integrity **100% clean, zero violations**.
- **mechanic_audit GAP-02** (P1): "Fort Level" in that exact formula is a **province-granularity**
  value (one per T1–T17) with **no rule mapping it onto a province's 1–3 settlements** post the
  PP-726 two-tier split — the formula's input is undefined at the granularity it operates at.
- **Read:** not a disagreement — the adjudicator's derivation check is necessarily syntactic (does the
  cited field exist?) and cannot see a granularity mismatch. Its "clean" verdict must **not** be read
  as "formula sound." GAP-02 is the substantive finding and stands as P1.

---

## 3. Contradictions

### 3.1 settlement Prosperity → Treasury multiplier: ×50 vs ×10 (RESOLVED in this pass)
This is the one genuine instrument-vs-instrument disagreement, flagged by the vector_audit crawler
for synthesis to resolve. I resolved it by reading the source directly.

- **mechanic_audit GAP-01** (P1): `settlement_layer_v30.md` states Prosperity's Treasury contribution
  as **both ×50 and ×10** "for what both passages describe as the same edge" — an internal conflict.
- **module_adjudicator**: treats them as **two distinct, non-conflicting derivations** — `d1`
  Prosperity → Local Economy (×50, settlement-internal) and `d6` Σ Prosperity × 10 → faction Treasury
  (cross-module) — and reports the derivation layer clean.

**Direct read of the source (verified this pass):**
- Line 47 (§1.3 derived-values table): `Prosperity | Local Economy | Prosperity × 50 | Gold income
  contribution to faction Treasury`.
- Line 169 (§1.8): `faction Treasury income = Σ settlement Prosperity × 10, derived_stats §8.1`.

**Verdict: mechanic_audit is more likely correct; GAP-01 stands as a real P1.** The `×50` value is
not a clean settlement-internal stat separate from Treasury — §1.3's own **description column labels
it "Gold income contribution to faction Treasury,"** the exact quantity §1.8 computes as `Σ Prosperity
× 10`. So the same edge is described with two different multipliers. module_adjudicator's "two clean
derivations" read is a **syntactic artifact**: its extractor node-typed `Local Economy` and `Treasury`
as different targets and therefore never compared their multipliers — precisely the semantic collision
a graph check cannot see. The fix (SE lane) must clarify whether Local Economy (×50) is a display
value distinct from the ×10 Treasury rollup and correct §1.3's description column either way.
(Note: line 737 carries a third, mine-specific "Province Treasury +50/season" flavor figure — separate,
not part of this conflict, but worth sweeping in the same pass.)

**No other true contradictions were found.** The Fort Level pair (§2.7) and the down-seam A6 cluster
(module_adjudicator's own "assessor co-defect" framing) are complementary-coverage or
method-sensitivity differences, not factual disagreements.

---

## 4. Coverage gaps — what none of the four could see this run

Be explicit: **this is one dated snapshot, not exhaustive corpus coverage.** Four structural blind
spots:

1. **vector_audit is BLOCKED — no corpus-wide citation/terminology-drift backstop.**
   `scripts/vector_audit.py`'s Stage 1–7 dispatcher is unimplemented (verified by direct read, not
   taken on the SKILL.md's word); the last real baseline
   (`archives/audit/2026-04-29-topographic-analysis/`) is **304 in-scope file-changes stale** as of
   today. This run caught **four** stale/dead-citation defects **piecemeal**, only because a
   subsystem-scoped read happened to hit them: mass_battle G6 (`derived_stats_v1` ×5),
   settlement GAP-05 (pre-PP-726 S-IDs), fieldwork GAP-4 (`stage11 §11.x` ×4), and adjudicator P1-B
   (`conviction_track_v1.md` missing from the registry). These are exactly the class a working
   TF-IDF/citation-graph pass sweeps corpus-wide. Until the dispatcher is built, this class has **no
   systematic detector** — and the same defect plausibly sits uncaught in every subsystem no
   instrument read this run.

2. **mechanic_audit covered all 8 intended subsystem heads, but the slate is still only the CURRENT.md
   heads — not the full corpus.** On disk (all complete): architecture, faction_political,
   fieldwork_investigation, mass_battle, personal_combat, settlement_territory, social_contest, and
   **threadwork** (which landed after the three earlier crawler deltas were logged — those notes' "7
   subsystems / threadwork never ran" statements are stale; see the currency note at the top). The
   completed threadwork pass adds one new P1 (D1, truncated P-25 override table) and a dense P2 tail
   (D3/D4/D8/D9/D10/D11/D12/D14, all lane=WR) that this report folds in. Even at 8/8, the mechanic slate
   by design covers only the CURRENT.md subsystem heads; it does **not** cover
   piety_track/conviction_track, npc_behavior, victory, npc_memory, territorial_piety, or the engine
   temporal spine — several of which module_adjudicator independently flags with A6/A8 issues. The
   stale-citation and referenced-but-undefined defect classes remain unmeasured in every subsystem
   outside those 8.

3. **module_adjudicator only sees modules registered in `module_contracts.yaml`, and only the wiring
   layer.** It cannot catch (a) empty/never-cited canonical sections — e.g. mechanic_audit's **GAP-D3**
   (`scale_transitions_v30.md §3.3` is an empty Handoff Rule; because *no* contract cites §3.3, the J2
   citation-fitness check never touches it — invisible by construction); (b) prose-level no-GM
   invariant violations (GAP-D4/D5); (c) semantic defects behind syntactically-valid derivations
   (§2.7 Fort Level, §3.1 Prosperity). 10/27 contract modules also still carry `doc: null`
   (unimplementable specs), a standing gap this run did not close.

4. **compliance_check produced no per-file output to cross-reference.** Its two-line PASS gives
   synthesis nothing to check mechanic_audit's flagged docs against. If per-file detail is ever
   emitted, `ability_armature.md`, `scale_transitions_v30.md`, and `mass_battle_v30.md` (each carrying
   multiple confirmed structural defects this run) are the first to check.

---

## 5. P1 filing queue (consolidated, deduplicated)

Every **new, not-already-filed** P1 across mechanic_audit + module_adjudicator, deduplicated, with
file/section, recommended ED lane, and source audit(s). **No `ED-<LANE>-NNNN` IDs allocated here** —
that is the run's separate sequential step. Lanes are recommendations; alternates noted where the
source audit flagged more than one plausible home.

**Excluded from this queue (already tracked / resolved — do NOT re-file):** social_contest G-7
(ED-SC-0004, open), G-9 (ED-SC-0015, open), G-11 (resolved ED-SC-0006), G-12 (resolved ED-SC-0007);
fieldwork GAP-8 (ED-FI-0005, open). These are P1-severity by the source audits but carry existing
ledger entries; re-filing would duplicate.

| # | Lane | File / section | Summary | Source audit(s) |
|---|---|---|---|---|
| 1 | MB | `params/mass_combat.md` (Projectile-weapons DR ~L191-200 vs Volley-Phase DR ~L303-312) | Two contradictory Ranged/Volley DR tables (PP-104 vs PP-188), ~2× apart at Heavy armor, neither marked superseded | mechanic_audit (G1) |
| 2 | MB | `mass_battle_v30.md` §A.14 (Woven units — brittleness) | Orphaned rule fragment ending mid-sentence, citing a compilation pass on `stage5_clocks.md` which does not exist in the repo; self-flagged in-doc `[EDGE-06 — P1]` but never filed | mechanic_audit (G2) |
| 3 | MB | `references/module_contracts.yaml` (mass_battle emits) | Fabricated emit `scene_outcome.battle_concluded` mislabeled "§8.5 verbatim"; canon writes `scene.battle_concluded` (`scene_outcome` is the family name). Remove the spurious edge — contract fix, not a registry extension | module_adjudicator (P1-A) |
| 4 | SE | `settlement_layer_v30.md` §1.3 (L47) vs §1.8 (L169) | Prosperity's faction-Treasury contribution stated as both ×50 ("Local Economy," described as the Treasury contribution) and ×10 (Σ Prosperity aggregation) for the same edge. Resolved in §3.1: real conflict; module_adjudicator's clean read is a syntactic artifact | mechanic_audit (GAP-01); module_adjudicator touched the same formula but reported clean |
| 5 | SE | `settlement_layer_v30.md` §1.3; `settlement_adjacency_v30.md` §2.2 | "Fort Level" consumed as a settlement-granular input (Garrison Strength; Fortress Defender-Ob) but defined only at province granularity (one per T1–T17); no rule maps it onto a province's 1–3 settlements post-PP-726. (§2.2 also mis-cites `mass_battle_v30 §A.4`, the Unit Stat Block, for a fortification rule) | mechanic_audit (GAP-02); complementary to module_adjudicator's syntactically-clean derivation read (§2.7) |
| 6 | SE | `settlement_layer_v30.md` §1.2, §1.8, §3.2, PART 2 registry | Settlement types "Village" (14 of 37), "Fortress-City" (S-014), "Cathedral-City" (S-036) used throughout PART 2 but absent from §1.2's Settlement Types table and §1.8's `base(Type)` weight table (leaving `W_s` uncomputable for the 2 compound types) and §3.2 Governor Eligibility | mechanic_audit (GAP-03) |
| 7 | SE | `settlement_layer_v30.md` §4.7 (Black Markets) | §4.7 modifies "Settlement Wealth" and "Settlement Accord" — neither is a valid settlement field under the §1.3 REVISED schema (Prosperity/Defense/Order; Accord is province-derived). §4.7–§4.9 read as un-migrated pre-settlement-layer legacy content | mechanic_audit (GAP-04) |
| 8 | SE | `settlement_adjacency_v30.md` §1.2, §3, §4 (whole prose doc) | Prose companion still documents the pre-PP-726 graph verbatim ("36 settlements"; old S-IDs — S-011/S-034 now refer to different settlements) while the data file `valoria_geography_v30.yaml` was correctly rebuilt at PP-726. Co-file drift: implementing from the prose routes battles/movement/grain-dependency through the wrong settlements | mechanic_audit (GAP-05) |
| 9 | IN | `scale_transitions_v30.md` §3.3 (Personal → Scene (Contest)) | One of the eight named Handoff Rules is an empty section — heading, zero body, no editorial stub marker (unlike siblings §3.4/§3.6, fixed via ED-748). Leaves the Personal→Contest transition unspecified at the architecture layer. Alt lane: SC if content belongs to Social Contest's entry-condition spec | mechanic_audit (GAP-D3) |
| 10 | IN | `scale_transitions_v30.md` §1 (mode table), §3.2 | Literal "GM adjudication" / "GM recognises" resolution-actor language uncorrected against the no-GM engine invariant, in the canonical mode-bridge doc. Same class as the ED-WR-0007 fix to `player_agency_v30.md §4.2`. Alt lane: WR (precedent). (Companion P2 GAP-D5, `player_agency_v30.md §7.1`, should be swept in the same ED) | mechanic_audit (GAP-D4) |
| 11 | IN | `references/canonical_sources.yaml` | piety_track's real home `designs/personal/conviction_track_v1.md` (exists on disk, real canon) is not registered; only the territorial `conviction_track_v30.md` is. Additive registration. **File coordinated with open ED-SC-0003** (same file, overlapping naming-collision fix — see §2.6) to avoid cross-lane collision | module_adjudicator (P1-B) |
| 12 | SC | `social_contest_v30.md` §7.2.1 (L418-425) | Succession Contest Compromise split-ratio table (60/40 → 55/45 → 50/50) is internally incoherent under its own "track-distance weighted" framing (perverse majority-claimant incentive at Track 6 vs Track 4; Track-5 midpoint gets a non-even split); its sole citation ED-762 resolves to an unrelated migrated entry whose orphaned `_migration_alt` shows the real rationale was lost and never re-filed. File jointly with formula finding F-A13 (same defect) | mechanic_audit (G-2 / F-A13) |
| 13 | FA | `faction_behavior_v30.md` §3.7 (Domain Action Ob Calculation) | `Ob_modifier` has two non-computable summands: `cascade_alignment_modifier` is invoked but never defined anywhere in the corpus (only a `# -1,0,+1` comment); `expectation_alignment_modifier`'s `× {1,2}` is a bare set literal with no selection rule (the magnitude the comment needs is discarded by `sign()`). Governs the Ob of every Domain Action for every faction — cannot be executed as written | mechanic_audit (FA-A-01 / FA-D-01) |
| 14 | FI | `fieldwork_v30.md` §2.2 vs §2.3 | Wound penalty to physical fieldwork stated two contradictory ways in one doc: §2.2 "+0.15 Ob per wound, NEVER a −1D pool cut" vs §2.3 "−1D to physical fieldwork per wound, per §2.2" (mis-citing §2.2's own opposite rule). ED-PC-0005/0006 already made the call; this executes propagation. May combine with #15 | mechanic_audit (GAP-1) |
| 15 | FI | `fieldwork_v30.md` §2.4 (Wounds and Thread operations) | Wound penalty to Thread-Read/Leap ops still states flat "+1 Ob"; the co-file `params/fieldwork.md` (patched under ED-PC-0006) says this exact figure is superseded by "+0.15 Ob per wound." Design-doc source never swept. May be filed as one combined wound-language ED with #14 (§2.2/§2.3/§2.4) | mechanic_audit (GAP-2) |
| 16 | FI | `fieldwork_v30.md` §5.6b; **also** `designs/personal/knots_v30.md` §9 (CANONICAL, cross-lane) | P-06 (philosophy) violation: Knot mechanic "drains the threadcut being's Coherence." Fix replaces it with a self-maintenance-strain cost (model already in `fieldwork_v30.md §2.8`). **Must fix both files in the same pass** — the identical defect is replicated in `knots_v30.md §9`, which sits outside the fieldwork canonical_sources entries | mechanic_audit (P-06, Mode E) |
| 17 | WR | `designs/threadwork/threadwork_v30.md` line 40 (P-25 "Scale-based Mending Stability" override table) | Content-loss: the Scale-based Mending Stability override table is truncated to its header row + "Object" with zero data rows. Confirmed via `git log --follow -p` to be an original authoring truncation, not a regression — no prior revision ever had complete data. Leaves the scale-override behavior for Mending Stability unspecified. Lane WR per the threadwork audit's own routing (threadwork has no dedicated lane in the §3 taxonomy) | mechanic_audit (threadwork D1 / formula_audit A7) |

**Queue totals:** 17 new P1s — SE ×5, MB ×3, IN ×3, FI ×3, SC ×1, FA ×1, WR ×1. Consolidation
opportunities the ledger step may take: #1–#3 as one MB provenance batch; #14+#15 as one FI
wound-language ED; #16 requires a cross-file (fieldwork + personal/knots) edit; #11 requires
coordination with ED-SC-0003; #17 (threadwork) can anchor a WR-lane batch alongside the threadwork P2
tail (D3/D4/D8/D9/D10/D11/D12/D14, also lane=WR) rather than landing alone. personal_combat contributed
**0** new P1s (all its findings are P2/P3 with in-repo self-awareness).

---

## 6. Recommended next actions (workplan / HANDOFF surface)

1. **Run the sequential ED-filing step against §5's 16-row queue**, honoring the three coordination
   constraints: file #11 cross-cited with ED-SC-0003; author #16 as a two-file edit (fieldwork +
   `knots_v30.md`); consider #1–#3 (MB) and #14–#15 (FI) as merged EDs. Record lane recommendations;
   let the ledger step allocate IDs from `id_reservations.yaml` (`next_free`, never max+1).
2. **Prioritize settlement/territory (SE) remediation** — 5 of 16 new P1s land here (GAP-01..05),
   and the crawler flags settlement_layer as a two-instrument hotspot by volume. GAP-05 (adjacency
   prose vs rebuilt YAML) is the highest concrete-harm item: it silently routes gameplay through the
   wrong settlements.
3. **Treat mass_battle as a single MB-lane provenance batch** (§2.1) — three P1s, one theme, most
   efficient as one coordinated cleanup than three separate landings.
4. **File the compliance_check severity-classification fix (IN lane, §2.5) before the module_contracts
   edits land.** The §5 queue itself (#3, #11) plus module_adjudicator's P2-A/P3-A/P3-B stage ≥5 edits
   into `module_contracts.yaml`, which sits at 80% of cap; the misclassification would turn a
   designed-to-be-tolerated warn into a CI-blocking error if the file crosses 18k. Sequence the fix
   ahead of the growth.
5. **Land the threadwork (WR-lane) remediation as a batch.** The threadwork Mode A–E pass did complete
   this run; it yields one new P1 (#17, truncated P-25 override table) plus a dense P2 tail
   (D3 empty Combat-Timing section, D4 broken §2.7 cross-ref, D8 History-bonus ambiguity, D9 asymmetric
   Pulling floor, D10 fractional-Ob rounding gap, D11 Knot-Strain terminology collision, D12 P-NN
   namespace collision, D14 stale propagation-map paths) — all lane=WR. Land them as one WR batch;
   D5 (CANONICAL-vs-proposal header) and D2 (Thread Debt homing gap) are already tracked — do not re-file.
6. **Escalate vector_audit dispatcher implementation to the workplan as real engineering work.** Until
   Stage 1–7 exists, the stale-citation / terminology-drift class (4 hand-caught instances this run)
   has no corpus-wide detector, and the modules no instrument read (threadwork, npc_behavior, victory,
   piety_track) are unmeasured for it. Also refresh the 304-file-stale baseline
   (`python3 tools/freshness_gate.py --update` for the pin residue; dispatcher build is separate).
7. **Log the two module_adjudicator sub-P1 residuals** (P2-A down-seam `transitions[]` population per
   `scale_transitions §12.3`/§12.4 + the A6 assessor §12.2-exemption fix; P1-B registry gap) to
   `handoffs/HANDOFF_IN.md`, and the settlement items to the SE handoff, so the in-flight surface
   reflects this snapshot.

**Scope honesty:** this synthesis reflects exactly what four instruments saw on 2026-07-13 — all 8
intended mechanic subsystem heads (threadwork included, landed late), the registered-module wiring
graph, a green size gate, and a blocked topographic pass. It is a reliable read of *that* surface — the
CURRENT.md heads plus the registered-contract graph — **not** a clean bill of health for the corpus:
the modules outside the CURRENT.md slate, the empty/never-cited canonical sections, and the entire
stale-citation/terminology-drift class (vector_audit blocked) remain unmeasured.
