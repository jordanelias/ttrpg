# atomization_rules — history

Companion to `references/atomization_rules.yaml`. **That file is POLICY; this one is HISTORY.**

## Why the split (B-X, Jordan 2026-10-06: *"you can extract all edit histories/discussion from .yaml files in references and just make those a supplement"*)

`atomization_rules.yaml` is the size-cap policy: `tools/compliance_check.py` loads it with
`yaml.safe_load` and grades each file against the first matching `policies:` row, and
`tools/ci_register_size_check.py`'s `yaml_max_tokens()` reads the `max_tokens:` of three rows from
its raw text (a line scan on `- match:` and `max_tokens:`, so comments are invisible to it). Over
time the file accreted, around its rows, dated incident write-ups, "raised from X to Y" histories,
retired-rule obituaries and Jordan's rulings. None of that is read by any program. It sat in the file
every reader of the policy had to carry.

**Nothing was deleted.** Every block below is the YAML text as it stood, moved verbatim (comment
lines as they were; for a `note:` key, the whole original line). Line numbers are those of the file
at the split.

**What stayed behind:** the schema (`defaults:`, every `match:`/`max_tokens:`/`on_exceed:` and the
other keys the loaders read), the editor instructions (first-match order, "MUST stay above the `*.md`
glob", "single owner: this row", "change the cap HERE only"), and a one- or two-line summary where a
reader needs the fact to use the row correctly today. Notes whose original was long were shortened
in the YAML to their operative sentences; the original is here. No program reads a `note` key
(grep of `tools/`, `tests/`, `engine/`, `skills/` and `.claude/` finds none; `compliance_check.py`
has no `note` access), and the one raw-text reader of this file, `tests/valoria/test_compliance_on_exceed_vocabulary.py`,
scans for `on_exceed: "<token>"` and still finds every token the rows declare.

**One defect found at the batch's close and repaired.** The `tests/sim/**/session_activity_log.md` row ended with TWO
`note:` keys (the first at the row itself, the second after the retired-row comment below). PyYAML keeps the last,
so the note the row parsed to described a `designs/audit/` file the row no longer refers to. The second, misattached
note was removed from the YAML, so the row now parses to its own first note (an unread key); the removed text is
reproduced here verbatim:

```yaml
    note: "Frozen evidence artifact of a completed one-off audit merge stage (self-declared 'QUARANTINE-NOTE: not a registry and not a source of canonical truth' in the file header). Was hitting the generic **/*.yaml 10000 catch-all at ~18.5k tokens with no action possible or intended — same class as the tests/sim/ and research/ skip-policies above, scoped to this specific file rather than a blanket designs/audit/**/*.yaml exemption."
```

**Adding here, not there.** New dated rationale, raise-histories and rulings about a row belong in
this file. The YAML comment should say what the row does today.

## History by section of the YAML

### defaults: auto_fix_on_violation (audit 2026-05-25, Phase 0 item 0.4)  _(was lines 12-19 of the file at the split)_

```yaml
  # NOTE (audit 2026-05-25 — Phase 0 item 0.4):
  # auto_fix_on_violation is HONORED at commit time (pre_commit_gate_mutating
  # calls compliance_check.apply_auto_fixes_to_additions) but OVERRIDDEN to
  # print-only at bootstrap time (valoria_hooks.assert_bootstrap). The bootstrap
  # override landed 2026-05-10 after auto-fix-during-bootstrap produced two
  # destructive commits (a8f7b2f8, 1df4259b) that wiped editorial_ledger_summary
  # by running atomizer on empty content. See architecture <compliance_subsystem>
  # (V2.5+) for full context.
```

### defaults: the 2026-07-26 ruling, reasoning (line 21 stays in the YAML as the operative statement)  _(was lines 22-26 of the file at the split)_

```yaml
  # A long document just breaks into sequential parts at ~15k tokens. Rationale: the split was
  # enforced by NOTHING -- grep confirms these two keys have zero readers in tools/, .githooks/ or
  # skills/, ci_co_file_checker.py has no pair rule (its only mention of 'infill' is an EXCLUSION),
  # and compliance_check.py merely skips such files. It propagated purely by imitation, and cost a
  # reader two files to follow one argument. Existing pairs are grandfathered, not a migration target.
```

### REGISTERS - editorial ledger: migration and lane split  _(was lines 96-115 of the file at the split)_

```yaml
  # Editorial ledger fully migrated to registers/editorial_ledger.jsonl (JSONL
  # migration 5c07bff0; reader cutover 6a42b1f1). The YAML ledger and all 10
  # editorial_ledger_archive*.yaml files were deprecated 2026-05-28 to
  # deprecated/canon/ — no active editorial YAML register remains to atomize.
  # The JSONL store is integrity-checked at commit by validate_ledger_jsonl.
  #
  # LANE SPLIT (2026-07-08 atomization pass): entries whose id already declares a lane
  # (ED-<LANE>-NNNN) were moved out of the flat registers/editorial_ledger.jsonl into their own
  # registers/editorial_ledger_<lane>.jsonl (lowercase lane code), mirroring the
  # registers/handoffs/HANDOFF_<LANE>.md split and the same ED-<LANE>-NNNN taxonomy. Pre-cutover
  # flat-ID entries are NOT retrofitted with a lane (same no-retrofit precedent as the
  # ED-<LANE>-NNNN cutover itself) and stay in registers/editorial_ledger.jsonl, which dropped
  # from ~150k tokens (at its own cap) to ~90k as a result. Both the main file and every
  # per-lane file are "active" — consumers (tools/validate_ed_citations.py,
  # tools/broken_dependency_checker.py) read all of them, not just the main one, or the
  # lane-tagged third of live entries would silently stop being validated. A lane file is
  # created only on that lane's first ED allocation (no `_go.jsonl` yet — zero GO entries).
  # Size caps for all ledger files live in tools/ci_register_size_check.py's THRESHOLDS,
  # not here (that script is the actual enforcement gate for this register; see its own
  # comments for per-file caps).
```

### REGISTERS - audit/simulation-run verdict registry  _(was lines 120-132 of the file at the split)_

```yaml
  # Added 2026-07-11 with the GitHub Pages dashboard (tools/dashboard_data.py):
  # references/audit_registry.jsonl is one JSONL line per completed audit/simulation
  # run (audit_type: canon_guard | mechanic_audit | resolution_diagnostic |
  # module_adjudicator | vector_audit | editorial_register | simulation_balance),
  # appended by tools/audit_registry.py's `append` mode. Same append-only shape and
  # merge-collision rationale as registers/editorial_ledger.jsonl (CLAUDE.md §1/§3) — a
  # shared YAML list that concurrent-session skill runs edit would collide the same
  # way HANDOFF.md/editorial_ledger.yaml did before their splits; JSONL append avoids
  # the structural-edit collision without needing a lane split (audit runs are far
  # less frequent than editorial decisions). Freshness (registry vs. actual
  # designs/audit/ folders) is checked by tools/ci_audit_registry_check.py, report-only.
  # Size cap lives in tools/ci_register_size_check.py's THRESHOLDS, not here (same
  # single-sourcing convention as the editorial ledger above).
```

### HANDOFF / CONTINUITY - why HANDOFF.md is capped (2026-07-08)  _(was lines 137-142 of the file at the split)_

```yaml
  # Added 2026-07-08 (token-efficiency pass): HANDOFF.md had drifted from its stated
  # "index + cross-cutting items" role to a ~21.5k-token append-only session log, and
  # nothing was governing it — the generic "**/*.md" catch-all below never applied because
  # fnmatch (not path-aware globbing) requires a literal "/" in the candidate, so a
  # leading "**/" pattern can never match a root-level file (see the compliance_check.py
  # fix in the same pass). Pruned narrative moved to registers/handoffs/HANDOFF_archive.md.
```

### The frozen ED archive (registers/archive/*), 2026-08-23 S6/6b  _(was lines 143-149 of the file at the split)_

```yaml
  # THE FROZEN ED ARCHIVE (relocated out of deprecated/ 2026-08-23, S6/6b). Under deprecated/ these
  # 26 fragments matched a `skip` rule; the move dropped them through every rule here to the generic
  # `**/*.yaml` catch-all at 10,000 tokens, and three of them exceed it — so the relocation silently
  # added three advisory warnings to a blocking gate's output. They are FROZEN, append-only history
  # that `tools/validate_ed_citations.py` parses to tell a real ED id from an invented one; nobody
  # may edit them, so a size cap on them is a warning nobody can act on, and warnings nobody can act
  # on are how a warning tier stops being read. Same `skip` posture their previous home had.
```

### The ratified architecture (architecture/*.md), ED-IN-0204  _(was lines 150-154 of the file at the split)_

```yaml
  # THE RATIFIED ARCHITECTURE (adopted 2026-09-05, ED-IN-0204). Moving Layer 1 out of `proposals/`
  # dropped five governing documents through every rule here to the generic `**/*.md` catch-all at
  # 15,000 tokens, adding five advisory warnings to a blocking gate's output — the SAME defect the
  # `registers/archive/*` note above records for the S6/6b relocation, so the precedent is followed
  # rather than the warning tier being quietly grown again.
```

### engine/season/*.yaml - why it is skipped  _(was lines 169-171 of the file at the split)_

```yaml
  # The season loop's runtime registries. `hole_register.yaml` is 113 rows of dense provenance prose
  # that `register.py --check` parses; it is MECHANISM under §0.05, not a document, and splitting it
  # would give the loader two files to reconcile for no reader's benefit.
```

### HANDOFF caps - the superseded paragraph (ED-IN-0221) and the ED-IN-0220 standing request  _(was lines 184-215 of the file at the split)_

```yaml
  # ⚠⚠ THE PARAGRAPH BELOW IS SUPERSEDED BY `ED-IN-0221`, THE SAME DAY, AND IS KEPT BECAUSE ITS
  # REASONING WAS WRONG IN AN INSTRUCTIVE WAY. It concluded the handoff bulk could not be moved
  # mechanically and needed adjudication. Jordan's answer — *"why don't you just hive off all closed
  # IN work into its own document"* … *"tbh it's applicable to all handoffs"* — dissolved it, because
  # `6c`'s refusal killed PRUNING BY MARKER (delete what a heading calls done), and a lossless MOVE
  # judged on a unit's BODY is a different operation with none of that failure mode. Nothing is
  # deleted, so a live item inside finished work is one file-open away instead of lost. DONE: four
  # lanes split, 99,491 tokens of closed narrative moved, zero lines lost (proved by line-multiset
  # partition against `git HEAD`). Live sizes now: IN 70,592 · MB 6,982 · PC 14,388 · SC 6,191 —
  # MB, PC and SC under this cap, IN still over and honestly so, its residue being genuinely
  # unresolved material. The lesson worth keeping: CUT AT THE FINEST GRANULARITY THE DOCUMENT
  # ALREADY LABELS. `Pending`/`Decisions`/`Next actions` label every ENTRY, which is why 6c's
  # section-level finding did not bind them.
  #
  # ⚠ THIS CAP AND THE ONE BELOW NOW FIRE AS *REAL* SIGNAL, AND WHAT THEY ASK FOR IS ADJUDICATION
  # WORK — NOT A SWEEP (ED-IN-0220, 2026-09-13). Two facts, both measured:
  #
  #   1. Deleting the uninformative `.md`/`.yaml` catch-alls below took the gate's advisory output
  #      from 116 warnings to 8. These two rules are among the 8, so they are no longer buried and a
  #      session that sees them should act on them. HANDOFF.md ~16.6k/4k; HANDOFF_IN.md ~130k/20k.
  #   2. THE OBVIOUS FIX IS THE ONE THAT WAS ALREADY TRIED AND REFUSED, and the reason binds whoever
  #      tries it next. `HANDOFF.md`'s own "Next actions" records step 6c ("slim the handoffs") as
  #      NOT RUN: its premise that ">=75% of HANDOFF_IN.md is narrative about completed work"
  #      measured at 21% corpus-wide, "and that 21% cannot be swept either: 12 of 17 sections marked
  #      [DONE]/[RULED]/EXECUTED carry open, held or needs_jordan items inside them", as does
  #      HANDOFF_archive.md itself. "The disposition markers in this corpus do not mean what they
  #      say. Pruning it is adjudication work, not a culling wave."
  #
  # SO: the threshold is NOT raised and the rule is NOT set to skip. Either move would convert a
  # standing request for adjudication into a silence, and the adjudication is real work with a real
  # hazard — burying a `needs_jordan` item inside a section marked done. Whoever takes it reads each
  # section for live items BEFORE moving it, and moves rather than deletes.
```

### HANDOFF.md row note, original  _(was lines 220-220 of the file at the split)_

```yaml
    note: "Root continuity index — read every session (CLAUDE.md §2), so keep it thin. Move closed/dated narrative to the archive; lane-owned '## Next actions' content belongs in that lane's registers/handoffs/HANDOFF_<LANE>.md, never here (2026-07-08 second pass: ~9k tokens of lane-specific bullets were fully redundant with content already in the lane files and were dropped, not just moved). on_exceed is flag_for_split (warn-tier in compliance_check.py's CI-mode severity map), not block_commit — HANDOFF.md is written by whichever session is pausing mid-task, and a hard block here would repeat the auto-fix-during-bootstrap destructive-commit failure mode noted above."
```

### HANDOFF_*_closed.md row note, original  _(was lines 226-226 of the file at the split)_

```yaml
    note: "Closed work for one lane, moved VERBATIM out of HANDOFF_<LANE>.md and never read for orientation — the live file carries an index of what moved. Uncapped for the same reason HANDOFF_archive.md is: an archive's size is not a defect, it is the point, and it only ever grows by accretion. A cap here would ask a session to split finished history, which is work with no reader. The thing that must stay small is the LIVE file, and that is the rule below."
```

### HANDOFF_*_history.md row note, original (ED-IN-0240)  _(was lines 232-232 of the file at the split)_

```yaml
    note: "Dated lane narrative, moved VERBATIM out of HANDOFF_<LANE>.md and never read for orientation — the live file carries an index of every OPEN MARKER the moved units hold, verbatim, which is the safety claim of the move. Distinct from the _closed sibling: _closed is what the marker predicate proved FINISHED, _history is dated narrative regardless of markers (CLAUDE.md §4 forbids a file named *closed* holding open items). Uncapped for the same reason as _closed and HANDOFF_archive.md: an archive's size is not a defect. The thing that must stay small is the LIVE file, and that is the rule below."
```

### tests/coverage_matrix.md row note, original (raise history 8000 -> 10000 -> 15000)  _(was lines 245-245 of the file at the split)_

```yaml
    note: "SINGLE SOURCE for the coverage_matrix cap (2026-06-28 consolidation): tools/ci_register_size_check.py reads this max_tokens at runtime via _coverage_matrix_threshold() rather than carrying its own literal (the two had drifted 8000 vs 10000). Change the cap HERE only. Raised 8000 -> 10000 (2026-06-24) when the 8000 cap had been failing CI (file ~8.3k). Raised 10000 -> 15000 (2026-07-22, ED-MB-0012, Jordan-directed 'coverage matrix may need to grow to 15k'): the register is a legitimately-growing per-session mass-battle test-coverage log and archiving faster than it grows was churning the register on every sim touch; give it real headroom instead. Markdown narrative file; auto-archive-by-status doesn't apply (no per-entry status field). When THIS threshold is reached, manually move closed-finding paragraphs to tests/coverage_matrix_archive_<date>.md and reset."
```

### references/propagation_map.md row note, original (raise history)  _(was lines 253-253 of the file at the split)_

```yaml
    note: "Append-only per-PP propagation log; grows over time and archives old batches to deprecated/archives/propagation/ (see the file's header). Raised from the default 5000 to 10000 (2026-07-21) — it had crossed 5000 (5019) and blocked CI; archiving by batch, not a hard split, is the maintenance path. When it approaches 10000, move the oldest active batches to a new deprecated/archives/propagation/propagation_map_archive_<date>.md."
```

### DESIGN DOCS - skeleton rule retired 2026-08-12 (plan step G2, ED-IN-0159 §1.6)  _(was lines 324-335 of the file at the split)_

```yaml
  # RETIRED 2026-08-12 (plan step G2, ED-IN-0159 §1.6). The only skeleton/index
  # policy rule matched "designs/**/*.md", and `designs/` was RETIRED 2026-07-19
  # (ED-IN-0071 P4/P5, PR #191) — CLAUDE.md §3: "Do not recreate designs/". The
  # rule therefore matched nothing for three weeks. Its `require_skeleton_above`
  # key was read by compliance_check's `_check_index`, itself dead and excised by
  # plan step G1 in this same programme, so nothing now reads it either.
  #
  # THIS DOES NOT UNDO THE 2026-07-26 RULING. That ruling grandfathered the
  # existing skeleton/index pairs and retired the pattern as a DEFAULT; the 37
  # `systems/**/*_index.md` files stay exactly where they are and their
  # disposition remains HELD for Jordan. This deletes a policy row that could not
  # have applied to any of them — they are not under `designs/`.
```

### references/canonical_sources.yaml row note, original (raise history 5000 -> 14000)  _(was lines 350-350 of the file at the split)_

```yaml
    note: "Raised 5000 -> 8000 -> 9000 (2026-05-18) -> 12000 (2026-06-12, aligned with TOKEN_THRESHOLDS + arch interim cap 633f5e57). 115 canonical_sha fields added by freshness_gate --update pushed file to 8086 tokens; threshold predated SHA metadata. RAISED 12000 -> 14000 (2026-09-09, ED-IN-0179): the `reference/` relocation lengthened every `canonical_sha__systems__<sub>__...` key by the inserted `__reference__` segment and freshness_gate --update re-pinned them, taking the file to 12,711. Same cause as every prior raise -- machine-written SHA metadata, not authored content. There is no _archive file, so the checker's suggested action does not exist. ~ 1,300 tokens of headroom."
```

### references/module_contracts.yaml row notes: note_2026_08_23, note_2026_07_29, note (all three originals)  _(was lines 355-357 of the file at the split)_

```yaml
    note_2026_08_23: "Raised 24000 -> 32000 (plan S5c, the wiring_manifest.yaml fold). MEASURED, AND THE MEASUREMENT IS THE WHOLE ARGUMENT: content did not grow, it SHRANK. Pre-fold the two files were 23,302 + 4,223 = 27,525 tokens, each under its own cap; post-fold the single file is 27,088, a delta of -437 -- the WIRING banner and the fold's disclosure content, net of the tier/scale/resolver fields dropped as duplicates of the contract row. A per-file cap that fires when two under-cap files merge is measuring FILE COUNT, not size, and the merge is what plan S5c was directed to do ('one registry, two blocks'). So the cap moves, as this row moved at 10000 -> 18000 -> 24000, and for a stronger reason than either: neither of those could say the content was already in the tree, and neither was a net reduction. FIRST SHIPPED AS 33000 ON A +116 DELTA, AND CORRECTED THE SAME DAY BY AN ADVERSARIAL PASS: the first fold repeated an 82-character `wiring:` comment on all 27 rows -- 553 tokens of exact duplication of the top-level WIRING banner -- which is most of what the cap raise was paying for. Deduplicated; the critic's further hypothesis that this would avoid the raise entirely is REFUTED by measurement (27,088 still exceeds 24,000), so the raise stands at a smaller number. REPRODUCE: ci_common.tokens() over the file, i.e. len(text)//4 -- python3 tools/ci_register_size_check.py prints it directly. Named because the first version of this note asserted four numbers and cited no instrument (CLAUDE.md 0.1 pt 3). Headroom sized to the 2026-07-29 raise's own ratio (24000/20402 = 1.18; 32000/27088 = 1.18), which also puts the file just outside the 85% report-only WARN band. The `on_exceed: warn_only` NO-OP recorded in the note below is still a no-op and is still not fixed here."
    note_2026_07_29: "Raised 18000 -> 24000 (ED-IN-0097, W4 OI-54 contract<->code join). MEASURED: the join added `sim_module:` to all 27 modules, taking the file 70,069 -> 82,280 chars (17,372 -> 20,402 tokens), which tripped the BLOCKING compliance gate. The added bulk is NOT prunable bloat: it is the join's disclosure content — per-row `none` reasons, three recorded DISCREPANCIES against the W4 preflight, and two-file-split residuals logged rather than papered (CLAUDE.md §0.1 #4/#5). Condensing it to fit a cap would delete exactly the honesty the join exists to provide, so the cap moves instead — the same disposition this row's own note below took at 10000 -> 18000, and canonical_sources.yaml took three times. Headroom sized for the 9 remaining `sim_module: none` rows to gain real paths as their doc:null gaps close. ⚠ RATIFIABLE ON MERGE (ED-1094) — called out in the W4 PR body, not slipped in. SEPARATE DEFECT FILED, NOT FIXED HERE: `on_exceed: \"warn_only\"` on the line below is a NO-OP — tools/compliance_check.py:179 reads `severity = 'warn' if on_exceed.startswith('flag') else 'error'`, so `warn_only` (and any unrecognised token) silently grades as a blocking error. 12 files in this file declare `warn_only` and every one of them is mis-graded. Had it worked, no raise would have been needed. Routed to audit/2026-07-29-centralization-single-owner/ (declared scope: size-cap single-sourcing); see 04_execution_ledger.md's W4 rows."
    note: "Was hitting the generic **/*.yaml 10000 catch-all (actual: ~14.4k tokens as of 2026-07-09), flagged as an unexplained violation nobody had acted on. Not narrative bloat to prune — it's a genuinely comprehensive per-module IN/resolver/OUT contract registry (27 modules), machine-checked by skills/valoria-module-adjudicator/scripts/contract_adjudicator.py, and CLAUDE.md §6 notes 10/27 modules still have doc:null — expected to grow, not shrink, as those gaps get filled. Same category as canonical_sources.yaml/mechanical_terms_index.md above: raise the explicit cap with headroom rather than leave it flagged against a generic threshold that never accounted for this file's real shape."
```

### Retired size rules for tools/observability/DECISIONS.md and PROPOSALS.md (ED-IN-0194)  _(was lines 402-418 of the file at the split)_

```yaml
  # Auto-generated observability decision register: a human-skimmable summary, not the
  # complete data (that's decisions.json, deliberately uncapped — console.html and any
  # programmatic consumer read the JSON, never this .md). Regenerated by
  # tools/observability/build_decisions.py; do not hand-edit. 2026-07-09: PER_CAT_CAP
  # dropped 60 -> 12 in the generator after this file drifted to ~59k tokens (4x this
  # cap) with the higher setting adding no real coverage.
  # RETIRED culling wave 1 (ED-IN-0194, 2026-08-21): the size rule for tools/observability/DECISIONS.md
  # went with tools/observability/ and its generator. A size cap on a file that
  # cannot be produced is a rule no run can satisfy.

  # Auto-generated unified proposals / open-work register (sibling of DECISIONS.md).
  # Human-skimmable summary; complete data is proposals.json (uncapped). Regenerated by
  # tools/observability/build_proposals.py; do not hand-edit. Tune PER_GROUP_CAP in the
  # generator, not this file, if it drifts. (ED-IN-0068 apparatus consolidation.)
  # RETIRED culling wave 1 (ED-IN-0194, 2026-08-21): the size rule for tools/observability/PROPOSALS.md
  # went with tools/observability/ and its generator. A size cap on a file that
  # cannot be produced is a rule no run can satisfy.
```

### Retired row: the designs/audit/ skip exemption (plan step G2, ED-IN-0165); the `note:` that followed stays in the YAML  _(was lines 475-488 of the file at the split)_

```yaml
  # RETIRED 2026-08-12 (plan step G2, ED-IN-0165) — DELETED, not repointed.
  #
  # This was a `skip` exemption for one file under `designs/audit/`. The first
  # attempt at this sweep REPOINTED it to `audit/2026-07-08-.../quantity_census.yaml`
  # and recorded that as "the live audit/ path". It is not live:
  # `references/restructure_ledger.md:1257-1258` records BOTH spellings — the
  # `designs/audit/` one and the `audit/` one — as `FORK:c451bcb`, FORKED. The unit
  # was evacuated 2026-08-05 with the non-design-lane July corpus.
  #
  # So the dead-scope sweep manufactured a fresh dead row and called it a fix,
  # against its own governing rule ("an absent path is dead only if its subject was
  # RETIRED" — this subject WAS retired, so the row was dead both before and
  # after). Two independent adversarial passes caught it, and the register that
  # would have told the first attempt so is in this same repository.
```

### AUDIT CORPUS - the 30k ruling (Jordan, 2026-08-11)  _(was lines 493-502 of the file at the split)_

```yaml
  # ────────────────────────────────────────────────────────────
  # An audit unit is a findings report plus, increasingly, a remediation plan; both are read
  # end-to-end by whoever executes them, and cutting evidence to fit a cap is the wrong trade.
  # Ruled: chunk the plan into a companion document rather than cut content, and give these files
  # 30,000. Placed ABOVE the catch-all because `_match_rule` is first-match.
  #
  # SINGLE OWNER: this row. Do not add a second cap for audit files in ci_register_size_check's
  # THRESHOLDS — that dict already carries three rows single-sourced from this file precisely
  # because they kept drifting (ED-IN-0097), and the two gates already disagree on the register cap
  # (15,000 in the gate vs 10,000 here; ED-IN-0159 §1.8, plan step G6).
```

### CATCH-ALL - measured into silence 2026-09-13 (ED-IN-0220)  _(was lines 510-536 of the file at the split)_

```yaml
  #
  # ⚠ THE `max_tokens` ON BOTH CATCH-ALLS IS DELETED, DELIBERATELY, AND THE RULES STAY SO THE
  # MATCH IS STILL DOCUMENTED. Their job was to "flag any unrecognized file above safe size" —
  # an OUTLIER alarm. MEASURED on the working tree the day they were removed:
  #
  #     116 violators · min 10,125 · median 20,941 · max 196,463 tokens
  #     17 above 40k · 4 above 100k · and all 116 of the gate's warnings were this one rule
  #
  # A median only 40% over the threshold means these were not identifying outliers, they were
  # describing the tree's ordinary document size. An alarm whose normal state is 116 firings
  # carries no information, and it was the ENTIRE advisory output of the compliance gate, so any
  # other warning arrived buried in it.
  #
  # CLAUDE.md §0.1 pt 5's predicate is the authority: a defect in an artifact load-bearing only on
  # this repository's PROCESS — not on the game, the exported params, the port, or a Jordan
  # decision — is "evidence the artifact can be wrong without cost. Delete it, or accept the defect
  # and write nothing." These caps gated nothing (advisory, exit 0), so the predicate says delete.
  #
  # WHAT SURVIVES, AND IT IS THE PART THAT WAS ALWAYS THE REAL RULE: CLAUDE.md §4's convention that
  # a long document splits into `_part2`, `_part3`, … IN READING ORDER. That is a judgment a session
  # makes when a document becomes unwieldy to work with, which is what it always was — §4 used to
  # claim the cap "is enforced", and it never was.
  #
  # NOT TOUCHED: every EXPLICIT per-file cap above, including the blocking ones
  # (`on_exceed: error` on the patch-register archives, `block_commit` on the session logs). Those
  # name a specific file for a specific reason and several of them are load-bearing. This deletion
  # is scoped to the two rules that fired on everything because they matched everything.
```
