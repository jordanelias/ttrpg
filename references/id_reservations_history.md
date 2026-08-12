# id_reservations — history

Companion to `references/id_reservations.yaml`. **That file is STATE; this one is HISTORY.**

## Why the split (ED-MB-0063 follow-on, 2026-08-01)

`id_reservations.yaml` is read on **every ED allocation, by every lane** — it is the most
contended file in the repo, and the concurrent-allocation collisions it exists to prevent are
the reason the `ED-<LANE>-NNNN` namespace exists at all. It had accreted ~9,000 tokens of
narrative provenance in trailing `#` comments and reached **14,263 of its 15,000-token BLOCKING
cap** — roughly two allocations from a `register-size-check` failure that would have stopped
every lane at once. Nothing reported that until the approaching-cap WARN was added.

The defect is structural, not a matter of anyone writing too much. The file conflated two things
with opposite lifecycles:

| | changes | read by | grows |
|---|---|---|---|
| **State** — `next_free`, block ranges, `verified_live_max` | every allocation | tooling, on every commit | no |
| **History** — why a block was reserved, released, frozen; incident write-ups | once, then never | humans, rarely | without bound |

Unbounded append-only history inside a hot, size-capped, machine-read state file guarantees the
cap is hit eventually. Splitting them is the same move this repo already makes three times over
(`editorial_ledger*` → `_archive`, `coverage_matrix` → `_archive`), so this is a fourth instance
of an established pattern rather than a new convention.

**Nothing was deleted.** Every narrative below is the verbatim comment text that used to sit in
the YAML, moved rather than rewritten — checked first, because the obvious cut would have
destroyed provenance: the `ED-IN-0064` LEDGER entry is about the governance research corpus, an
entirely different item, so the duplicate-key write-up existed **only** in that comment.

**What stayed behind, deliberately:** a one-line summary per lane carrying the facts a reader
needs to allocate correctly *today* (block spent/released, max allocated, deliberate gaps), plus
a pointer here. `0103-0111` stays in the YAML because
`tests/valoria/test_id_reservations_walkback.py` requires it there — an undocumented gap is
indistinguishable from an error, and that test enforces it.

**Adding here, not there.** New allocation narrative belongs in this file or in the lane's
`registers/editorial_ledger_<lane>.jsonl`. The YAML comment should stay one line per lane.

---


## MB — Mass battle

<a id="mb"></a>

*Moved verbatim from `id_reservations.yaml` line 111, 2026-08-01. 4100 chars.*

```text
0046-0060 RESERVED 2026-07-29 for the dedicated MB session (audit/2026-07-26-mass-battle-fable-audit/03_execution_plan.md v2 §12): draw MB ids from this block, do not read-and-bump mid-run (IN W0a pre-allocation — see the IN lane line). // ED-MB-0044 (2026-07-26, open/needs_jordan): R3 ranged-vs-ranged never engages — FILED as a real entry to end a dangling earmark that caused id churn twice; its proposed fix was under-scoped and is corrected by ED-MB-0045 (hold is a two-gate change and is load-bearing for freeze_wings/refused-flank/STANCE_COMMITMENT). ED-MB-0045 (2026-07-26): Fable-5 six-dimension read-only audit + all-surfaces remediation plan.   # allocate = take next_free, bump, co-commit. ED-MB-0042 (2026-07-25): CELL IS THE PRIMITIVE FOR MORALE (Jordan directive) — aggregate-up (troop-weighted mean of live cells) / modulate-down (a discipline-gated pull back toward the body); broken cells stop fighting but their men remain killable; lattice contagion. Phase 2 was unreachable until cells got their OWN du Picq break-point (an asymmetry, not a magnitude). ⚠ The default flip to ON was RETRACTED the same day — its measurement was confounded by scalar morale writes the cell aggregate shadows (between_turn_recovery / reset_morale_between_battles are silent no-ops under the flag), so the ON and OFF arms were not comparable. Default OFF, goldens back to pre-flip; net shipped change zero. Blocker for re-flipping is the scalar-write sweep. Kept: born-broken-subunit fix + exact uniform aggregate. FULL per-ED detail lives in registers/editorial_ledger_mb.jsonl (do NOT re-log it here — this comment is a terse index only, condensed 2026-07-23 to stay under the register-size cap). ED-MB-0041 (2026-07-24, needs_jordan): DEEP ADVERSARIAL AUDIT — 5 independent critics, every headline claim hand-verified; only 17 of ~92 magnitudes survive. Anti-fabrication gate defeated by a bare-integer self-whitelist; fabricated octagon citation; K_LINEAR fitted to superseded output; discipline misreads canon ~5x; convergence=1/N; Feigned Retreat dead; no pursuit; armour causes MORE arrow casualties. Tier-3 calls held for Jordan. Report: audit/2026-07-22-mass-battle-stress-test/adversarial_deep_audit_v1.md. ED-MB-0040 (2026-07-24): CELL-PRIMITIVE DAMAGE (Jordan: "the cell is the primitive") — per-cell octagon arcs were averaged into one subunit scalar, so flank/rear cells died no faster than front cells; _octagon_cell_mods now single-owns the arc, gated PC_CELL_DAMAGE. Envelop side-swing 41->15.5pp; re-bases the battery so ships gated. ED-MB-0039 (2026-07-24, needs_jordan): ENVELOPMENT STABILITY DIAGNOSIS — pure-infantry parity envelopment is deployment-chaotic (+/-54pp side swing); combined-arms cavalry-rear is the only stable regime; the moderate bands sit in an engine gap. Fork for Jordan. ED-MB-0038 (2026-07-24): MATCHED COMMAND-GRANULARITY — composed presets faced a monolith, pinning H3/H4/H6 to 0%; _command_army(n_cmd=3) builds a tripartite-line opponent; gauge multi 6->8/20. ED-MB-0034..0037 earlier. Allocated through ED-MB-0033 (2026-07-24): Fable logic audit Part A — 9 defects fixed in ED-MB-0027..0032; honest gauge 6/20 (was inflated 8/20). ED-MB-0032 (2026-07-23): FRACTIONAL POOL (Jordan: "pool must be fractional") — integer part rolls d10s, remainder contributes its EV; gated PC_FRACTIONAL_POOL. ED-MB-0031 (2026-07-23): STOCHASTIC ROUT break-point in the historical 15-30% band (du Picq), discipline/morale-skewed; loser casualty-at-rout ~90%->~30%. ED-MB-0030 (2026-07-23): conditional orders; 0029 intent-as-resolution (stance = offence/defence commitment, gated); 0028 cell closing-ranks T1 Phase-1a (gated); 0027 honest-gauge density-match; 0025/0026 explicit subunit deployment primitives (density/gradient/frontage×depth) + wing fix; 0022-0024 Feigned Retreat/Reserve/DG-2 yield (gated); 0018-0021 density cap + perimeter geometry + octagon damage-mult; 0011-0017 spatial-model v2 Stages B-F + envelopment pathing (0016 open: DG-6 CEV friction gated); 0008-0010 provenance-integrity (open).
```


## PC — Personal combat

<a id="pc"></a>

*Moved verbatim from `id_reservations.yaml` line 124, 2026-08-01. 2978 chars.*

```text
BLOCK FULLY CONSUMED — 0 ids released 2026-07-30 (ED-IN-0098, W5 capstone walk-back). MEASURED max allocated = ED-PC-0055, i.e. EXACTLY the top of the block; next_free stays 56. ⚠ FINDING: this lane hit its reserved ceiling with zero headroom, so the reservation was undersized and the freeze was actively constraining it — size the next pre-allocation from observed burn rate, not a guess. Freeze lifted: read next_free, allocate, bump, co-commit as normal. Was 0041-0055 RESERVED 2026-07-29 for the dedicated PC session (audit/2026-07-26-combat-balance-customization-state/combat_execution_plan.md §15): draw PC ids from this block, do not read-and-bump mid-run (IN W0a pre-allocation — see the IN lane line). // SKELETON ONLY (Jordan 2026-07-24, CLAUDE.md §4): ONE SHORT LINE per ED. Prose lives in registers/editorial_ledger_pc.jsonl + audit/2026-07-24-combat-four-dimension-audit/ (index+infill). Do not grow prose here — it fights the 15k register cap. # ED-PC-0034..0039 = the four-dimension read-only audit (fiat/orphans/conflicts/tuning) and its batch-wise remediation, each batch adversarially reviewed: 0034 correctness (represent-gate path-dependence, riposte exposure floor, grab sign-flip); 0035 dead code + stale prose (8 keys un-leaked from the Godot contract, imposition machinery retired); 0036 fiat retirement (percussion sel_perc, pursuit_sigma, cut_thrust versatility, ATTACKER_BIAS/UPSET_FLOOR tagged); 0037 structural thresholds (first-actor race -> cadence x anticipation from an arbitrary phase; soft closed-latch; ATTACKER_BIAS retired) + 0037.1 review corrections; 0038 capability-gated penetration (damage now agrees with adef_cap, which moved to core as single owner); 0039 knee corrections (clamp capability at >=0 — ADEF_CUT is a sigma penalty, not a magnitude; grip/room threaded; one-weapon participation guard; K swept); 0040 the 0039 review — roster-wide primitive-derived participation guard (mutation-verified), 4 false claims retracted (incl. 0038's "estoc -> 0": it is the #1 plate weapon), medium round trip + ranseur covert-killer + F24 selection-vs-damage disagreement disclosed. # ED-PC-0029..0033 2026-07-24 = the reach/approach arc: arrest_impulse + tanh true_time (retire thrust_extension); closed-phase bind disengage; percussion -> stamina + poise stagger; penetration threshold (rapier plate fall-off); stale-grip fix + measure continuity. # ED-PC-0022..0028: U10 lever activation; fiat/broken-logic audit + imposition-fiat retirement; levels-of-investment; combinatorial audit + core.logistic(); HEMA grounding corrections; T_vuln + mode-aware heft; tradition gate on equipped. # ED-PC-0002..0021: U0 units-honesty; edges primitive; polearm choke counterbalance; weapon-class facing; half-sword roster + affordance; thrust authority + point-token scaling; attribute/value coherence; U9 recalibration; NERS-audit items. # ALL detail: registers/editorial_ledger_pc.jsonl.
```


## SC — Social contest

<a id="sc"></a>

*Moved verbatim from `id_reservations.yaml` line 195, 2026-08-01. 2539 chars.*

```text
BLOCK RELEASED 2026-07-30 (ED-IN-0098, W5 capstone walk-back). Was 0017-0020 RESERVED 2026-07-29 for cross-lane EDs the IN code-shape waves file in SC. MEASURED max allocated = ED-SC-0016; unused 0017-0020 (4) returned to the pool, next_free 21 -> 17. Freeze lifted: read next_free, allocate, bump, co-commit as normal. // ED-SC-0016 allocated 2026-07-13: 2026-07-13 multi-agent audit P1 -- Succession Contest Compromise split-ratio table (social_contest_v30 SS7.2.1) internally incoherent under its 'track-distance weighted' framing; sole citation ED-762 is an orphaned migration remnant. Open/needs_jordan; file jointly with formula F-A13. next_free bumped 16->17. // ED-SC-0015 allocated 2026-07-08 (THIS branch, RENUMBERED +1 from this branch's own prior ED-SC-0014 -- which collided with origin/main's concurrent ED-SC-0014, the coherence-audit Standing-range item below; itself already once RENUMBERED from an original ED-SC-0013 that collided with origin/main's Auto/Manual doctrine; status open, needs_jordan): Parliamentary total-victory Mandate stacking — §10 BG-Vote TV rider (-1) vs a per-motion-type target effect (e.g. §5.4 Censure -1) compose to -2 on the same faction within one motion; surfaced building the Censure fallback (ED-FA-0012/parliamentary_action.py), currently implemented as stacking (both fire) as the literal default, NOT ratified canon — Jordan picks stack-to-2 or cap-at-1. ED-SC-0014 allocated 2026-07-08 (origin/main): attribute/value coherence audit (ED-IN-0029) — Standing range collision ratified (BG faction track 0-10; scope-tag the cross-scale homonym with the contest kernel, OPT-AV-12; FA co-sign); execution pending. ED-SC-0013 allocated 2026-07-08 (origin/main): Auto/Manual Resolution Duality doctrine (PROPOSED, since RULED) — reframes ED-SC-0011 as the zoom-in expansion; forks A/B/D resolved, fork C needs_jordan. ED-SC-0012 allocated 2026-07-08: pessimist-audit SC work items — Recall/Prep cap, Appraise, Wager — execution pending (decision ED-IN-0027). ED-SC-0001 allocated 2026-07-05: NERS-audit E-10 accepted work item (dominance sweeps); ED-SC-0002..0010 allocated 2026-07-05: Fable 5 social-contest audit acceptance sweep (PR #80, Jordan post-merge instruction) — P0 decision docket 0002-0005 (echo keying / tracker naming / pool formula / bonus-stack cap; forks awaiting Jordan's picks, needs_jordan), consequence-spine work 0006-0007, contract refresh 0008, Stage-4 entry criteria 0009, Chronicle focalization+consumer 0010
```


## FA — Faction actions

<a id="fa"></a>

*Moved verbatim from `id_reservations.yaml` line 197, 2026-08-01. 2519 chars.*

```text
BLOCK RELEASED 2026-07-30 (ED-IN-0098, W5 capstone walk-back). Was 0036-0039 RESERVED 2026-07-29 for cross-lane EDs the IN code-shape waves file in FA. MEASURED max allocated = ED-FA-0036; unused 0037-0039 (3) returned to the pool, next_free 40 -> 37. Freeze lifted: read next_free, allocate, bump, co-commit as normal. // ED-FA-0035 allocated 2026-07-13: 2026-07-13 multi-agent audit P1 -- faction_behavior_v30 SS3.7 Domain Action Ob_modifier has two non-computable summands (cascade_alignment_modifier undefined corpus-wide; expectation_alignment_modifier's x{1,2} bare set literal). Open/needs_jordan. next_free bumped 35->36. // ED-FA-0018..0034 allocated 2026-07-09: comparative-governance-research docket round 2 (designs/audit/2026-07-09-comparative-governance-research/) — Byzantine/China/Japan/HRE/Venice/Renaissance-Italy/Spain rank-advancement proposals, judged 44-kept/14-cut by an Opus 4.8 pass; 5 authored into faction_politics_v30.md as PROPOSED (ED-FA-0019/0020/0021/0022/0023 — Recognition Fork, Court Attendance, Kaochengfa audit, Guild mastership/entry forks), rest open/needs_jordan (see registers/editorial_ledger.jsonl and registers/handoffs/HANDOFF_FA.md). next_free bumped 18->35. ED-FA-0008..0017 allocated 2026-07-08 (THIS branch, RENUMBERED +1 from this branch's original ED-FA-0007..0016 -- collided with origin/main's concurrent ED-FA-0007, the coherence-audit execution bundle below): FA/SE historical-precedent research docket (designs/audit/2026-07-08-fa-se-historical-precedent-research/) — fiscal stance, muster re-grounding, conquest terms, regency, tributary variant, guild embargo, citation-patch batch; several needs_jordan forks (0010,0013,0014,0015,0016). ED-FA-0007 allocated 2026-07-08 (origin/main): attribute/value coherence audit (ED-IN-0029) execution bundle — Mandate dual-form marking (OPT-AV-10), CI starting-value provenance/TTRPG-vs-BG split (OPT-AV-11), factions_personal Intel backfill hygiene item; decisions ratified, execution pending. next_free bumped 7->8. ED-FA-0006 allocated 2026-07-08: pessimist-audit FA work items — Parliamentary distill, da.* crosswalk, etc. — execution pending (decision ED-IN-0027). ED-FA-0001 allocated 2026-07-05: faction-count reconciliation work item (narrative-census fork 10); ED-FA-0002 + ED-FA-0003 allocated 2026-07-05: edge-playability §7 items 5 (strategic-turn surface / domain_actions home doc) + 8 (BG victory-params re-export), edge-playability §7 batch (PR #81)
```


## IN — Infrastructure / cross-cutting

<a id="in"></a>

**ED-IN-0170/0171 allocated 2026-08-12** (next_free 170 -> 172), moved here from the lane row so
that row stays a pointer rather than a narrative (`test_narrative_does_not_creep_back_into_the_state_file`
caps it at 600 chars, and it caught this append at 659).

- **ED-IN-0170 — degree-vocabulary equivalence census.** Prices the held ruling #0. The divergence
  audit's "16 producers" is a count of code sites; measured behaviourally it is **7 equivalence
  classes over 11 sites**, and **8 of those 11 need no ruling at all**. Instrument:
  `audit/2026-08-12-degree-vocabulary-census/degree_census.py`.
- **ED-IN-0171 — Jordan ruling, 2026-08-12: "Dead files get moved to deprecated."** Resolves
  ED-IN-0163 and unblocks G2's generator-retirement half. ⚠ One conflict flagged, not routed
  around: `tests/valoria/test_evacuation_plan.py:98/:166` pins the opposite disposition and must be
  amended deliberately when the retirement is executed. Not executed in the same commit as the
  census — it is its own scoped change.

**ED-IN-0158/0159 allocated 2026-08-11, RENUMBERED from 0156/0157** (next_free 156 -> 160): the
consolidation sweep and the code-leanness census. **A same-lane DOUBLE collision.** This branch
(`claude/repo-cleanup-consolidation-lig2jo`) and PR #302 both branched from `c26a22c` reading
`next_free: 156`, and both allocated 156 **and** 157. #302 merged first (2026-08-11 17:52Z,
`9aabd35`), so it keeps `ED-IN-0156` (CLAUDE.md's 13 unguarded countable figures) and `ED-IN-0157`
(the second adversarial pass over the ED-IN-0153 residuals); this branch renumbered both, per the
standing later-merging-side-renumbers rule.

**This is at least the sixth same-lane renumber-at-merge on the IN lane**, after 0074, 0075, 0083,
0086 and 0087 — the list `tests/valoria/test_id_reservations_walkback.py`'s own docstring keeps. The
`ED-<LANE>-NNNN` namespace eliminates *cross-lane* collision by construction and, as
`id_reservations.yaml`'s header says, explicitly does not address the same-lane case, calling it
"much narrower, already-expected". Six occurrences on one lane says otherwise: IN is the
cross-cutting lane every infrastructure session uses, so two concurrent IN sessions is the normal
case, not the narrow one.

**Nothing catches it.** Measured 2026-08-11 across all live lane ledgers: 1,195 entries, 13 ids
appearing more than once (`ED-129`, `ED-131`, `ED-200`, `ED-295`, `ED-297`, `ED-306`, `ED-IN-0012`,
`ED-IN-0013`, `ED-IN-0016`, `ED-IN-0029` x3, `ED-IN-0149` x3, `ED-MB-0042`, `ED-MB-0063`), and no
test asserts id uniqueness. Some are deliberate progress-appends; others may be unresolved
collisions; the register carries nothing that distinguishes them. `next_free` is a hand-edited
counter with no relation to the ledger it indexes — a check that fails when an allocated id already
exists in the merged ledger, and when `next_free` is not strictly above every allocated id in its
lane, would have caught this before either PR opened. Instrument + the shape of that guard:
`audit/2026-08-11-code-leanness/duplication_census.py` §6. Full adjudication:
`audit/2026-08-11-consolidation-sweep/00_consolidation_sweep.md` §8.

**ED-IN-0153 allocated 2026-08-11** (next_free 153 -> 154): world-schema gap audit — a three-axis
agonist->antagonist interrogation of the ratified entity ladder, 19 domain lenses, and the
individuation/authoring surface, against the Key type registry and the module contracts, to find
MISSING keys and contracts. Read-only; ratifies nothing. See
`audit/2026-08-11-world-schema-gap-audit/` and `registers/editorial_ledger_in.jsonl`.

**ED-IN-0152** (prior): subsystem flow skeletons + the anchor guard. RENUMBERED from ED-IN-0151,
which PR #298 claimed concurrently and merged first — a **same-lane** collision, which is the case
the `ED-<LANE>` tag does *not* prevent by construction (it prevents cross-lane collision only).

*Housekeeping, 2026-08-11: the yaml line carried a mangled pointer — a stray `.md#in.` fragment
left mid-sentence by an earlier edit, immediately before the real `Narrative:` pointer. Removed
while shortening the line back under the 600-char cap that
`tests/valoria/test_id_reservations_walkback.py` enforces.*

*Moved verbatim from `id_reservations.yaml` line 225, 2026-08-01. 3802 chars.*

**COLLISION 2026-08-09 — ED-IN-0148 double-allocated; the later-merging side renumbered** (the recurring pattern already recorded below for ED-IN-0031, ED-IN-0032, ED-IN-0044/0045 and
ED-IN-0048/0049/0050 — same failure class, same resolution).

Two sessions concurrently read `next_free: 148`, both allocated it, and both bumped to 149 from
different bases:

- **Keeps 0148** — the post-evacuation vector audit + "GM Decides" Resolution Register
  (`audit/2026-08-06-vector-audit/`, allocated 2026-08-06, landed on `main` via PR #291).
- **RENUMBERED 0148 → 0149** — the world-churn audit (`audit/2026-08-08-world-churn-audit/`,
  allocated 2026-08-08, still on branch `claude/fable-world-churn-audit-0gydi3` / PR #294 at the time
  of the merge). All citations in that directory, its three ledger rows and its two `HANDOFF_IN.md`
  sections were rewritten; the vector audit's references were left untouched.
  `next_free` 149 → 150.

**Standing observation.** CLAUDE.md §4 adopts the `ED-<LANE>-NNNN` taxonomy because *"a lane tag
makes cross-lane collision impossible by construction, not just by allocation discipline."* That
held — this was not a cross-lane collision. What it exposes is the residual: **same-lane concurrent
allocation is still possible, and IN is the lane most exposed**, since cross-cutting work
concentrates there and this is now the fifth recorded IN collision. The guard that would close it is
nameable and unwritten: a check that no ED id appears twice across the ledger files with different
`system` values.

```text
ED-IN-0139 allocated 2026-08-04: engine/params/ flips KEEP -> EVACUATE in tools/evacuation_plan.py (rule R-PARAMS-INFO -> R-PARAMS-DUMPED). Jordan: "params .md are largely useless at this point and I want them gone" / "just dump the constants to a yaml" / "provenance can cite to a fork" — the last of which dissolves the ~50-provenance-referent objection that had kept the tree. Gated on capture, not on trust: tools/export_params_constants.py writes engine/engine_params/params_tables.yaml holding all 43 files BYTE-IDENTICALLY plus a structured table view (258 tables, 1367 rows); lossless by construction because the parser is NOT total (six index-stub/history files yield no table). --check is wired blocking in all four places and is a MIGRATION-WINDOW gate that must be retired with its source. Also fixed the two false-positive scan classes that surfaced when engine/params became the first sub-root evacuation: slice_prefixes() (a slice is the shortest wholly-evacuating prefix, not the top-level dir) and a wholly-evacuating test in joined_path_readers() (tests/sim holds the KEPT canon MB engine; 30 kept readers were being reported as breakages). Split-path alarms 33 -> 4. next_free 139->140. // ED-IN-0125/0126 allocated 2026-08-04: 0125 = the fork-direction inversion (fork stores outdated material, MAIN is reserved for ongoing work) + J1 reinterpreted + the eight C-item rulings; 0126 = build_fork.py's empty-scan guard (--verify-only scanned clean over a nonexistent tree). Both resolved. // ED-IN-0114 allocated 2026-07-31: age-weight the scope ratchet's ledger signals — ed.open/ed.needs_jordan were raw censuses that punished FILING rather than rot (213->76 stale, 94->21 stale at STALE_DAYS=30); obs_core extended to carry `date` so age is available to every consumer instead of a second ledger reader. next_free 114->115. // ED-IN-0113 allocated 2026-07-31: ED-IN-0112 residuals — the DECISION-POLICY precedence fork (Jordan's alone; 134-ruling precedent mine attached, mechanical canon demonstrably subordinate to measured grounding, metaphysical-canon tier UNESTABLISHED and deliberately not invented) + five unfixed adversarial findings (HELD_INACTIVE is display-only; health is self-reportable; blind to partial movement; m1_acceptance/build_program untested; active_until has no reader). next_free 113->114. // ED-IN-0112 allocated 2026-07-31 (read next_free=112, allocated THERE, bumped — the documented protocol; NOT from the 0100-0102 sub-block remainder): M1 program scaffolding — scope ratchet (tools/scope_ratchet.py + registers/scope_baseline.yaml), season acceptance gate (tools/m1_acceptance.py), dashboard program panel. Decision policy HELD for Jordan (ED-1094 loud exception). next_free 112->113. // FREEZE LIFTED 2026-07-30 (ED-IN-0098, W5 capstone walk-back) — the three-session run is over; read next_free, allocate, bump, co-commit as normal. next_free STAYS 112 and that is DELIBERATE, not an oversight: the 0092-0111 block is SUB-PARTITIONED. MEASURED (2026-07-30): allocated = 0092,0093,0094,0095,0096,0097 (code-shape) + 0103 (the CSO program itself). The code-shape sub-block 0093-0102 had 5 free ids at that point; 0098 (this release) and 0099 (the audit-family critique, 2026-07-30) have since been consumed FROM the sub-block directly — which is legitimate, the sub-block belongs to this program; what is withheld is releasing them to the general pool via next_free. 0100-0102 remain. They are NOT released, because audit/2026-07-29-centralization-single-owner/ §0.1 row 6 partitions this block "ED-IN-0091 keeps 0093-0102; this program takes 0103-0111", its pointer declares block 0103-0111, and its W0 has NOT started. A single next_free pointer cannot express "0098-0102 free, 0103-0111 held", so walking it back to 98 would hand out a LIVE reservation five allocations later — the same failure class as the W4 tools/registry.py near-retirement (ED-IN-0097). Wasting 5 ids is the cheap side of that trade. RECLAIM 0100-0102 when the CSO program completes or releases its block; until then they are stranded by design. Guard: tests/valoria/test_id_reservations_walkback.py asserts next_free > max-allocated for every lane, so no future walk-back can re-issue a live id. // ED-IN-0091 allocated 2026-07-29: code-shape open-items register + connective-tissue/compliance orchestration plan (audit/2026-07-29-code-shape-open-items/) — collates the open I/O/Keys/centralization/scales/orphan items across the recent audit corpus and sequences 6 Sonnet/Opus waves (P1 stubwire self-flagging-stub primitive + dispatch closure + pipeline-reach oracle; P2 single-owner/contract-truth); ALL MB elements route to the dedicated MB session's 03_execution_plan.md v2 and ALL PC elements to the dedicated PC session's combat_execution_plan.md (PR #249) per Jordan's 2026-07-29 lane-partition directives; this program touches no MB- or PC-owned file. next_free 91->92. // ED-IN-0073..0090 (2026-07-17..2026-07-28): full per-ED detail lives in registers/editorial_ledger_in.jsonl — comment condensed 2026-07-29 to stay under the register-size cap, per the MB-lane precedent. Note the recurring same-lane merge collisions in that span (0074/0075/0083/0086/0087 each RENUMBERED at merge): read next_free, never max+1.
```


## IN — the 2026-07-14 duplicate-key repair (ED-IN-0064, finding OBS-IN-1)

<a id="dup-key"></a>

*Moved verbatim from `id_reservations.yaml` line 226, 2026-08-01. 10738 chars.*

```text
# [ED-IN-0064 DUP-KEY REPAIR, finding OBS-IN-1] STALE DUPLICATE IN: mapping neutralized — was next_free: 63; the authoritative IN: line above now carries next_free:65. YAML last-key-wins had been resolving IN.next_free to this stale 63 (the recurring 2026-07-07 duplicate-IN class). Provenance retained (full text in registers/editorial_ledger_in.jsonl): ED-IN-0062 allocated 2026-07-13: cross-scale governance-grounding synthesis docket (designs/audit/2026-07-13-cross-scale-governance-grounding/) -- one graph + per-scale grounding matrix + pressure-key registry + classified gap register (COMPLETE-THE-CHAIN vs GENUINE-GAP) + precedent-fix decision-queue, spanning the spatial (settlement->territory->province->duchy->country) and political (factions/governance-type/franchise/caste/standing/parliament) spines; cross-cutting IN lane (SE/FA/SC/WR/GO); FILED, PROPOSED fixes, needs_jordan. next_free bumped 51->52. // ED-IN-0048/0049/0050 allocated 2026-07-13 (0049/0050 RENUMBERED from this branch's original ED-IN-0046/0047 -- COLLISION: this branch read next_free=46 and allocated ED-IN-0046/0047/0048 for the 2026-07-13 multi-agent audit's cross-cutting P1 batch, but origin/main's governance_consolidation_v1 ratification (PR #130) concurrently claimed ED-IN-0046/0047 for its own D1-D5/D6-B1 rulings and merged first -- renumbered this branch's colliding entries during merge reconciliation, same pattern as the ED-IN-0031/0032 etc. collisions documented below; ED-IN-0048 needed no renumber, 48 was still free): ED-IN-0048 = piety_track home conviction_track_v1.md unregistered in canonical_sources.yaml (COORDINATE with ED-SC-0003); ED-IN-0049 (was ED-IN-0046) = empty SS3.3 Personal->Contest Handoff Rule (scale_transitions_v30); ED-IN-0050 (was ED-IN-0047) = literal 'GM adjudication'/'GM recognises' language vs no-GM invariant (scale_transitions SS1/SS3.2, same class as ED-WR-0007). All open/needs_jordan. next_free bumped 48->51. // ED-IN-0047 allocated 2026-07-13: D6 (G606 recall-clock wiring) and B1 (starting faction count) RULED directly by Jordan in conversation (not "ratify commit all"-inferred) -- D6: cumulative per-Defy-season accrual is canonical, conditioned on E11 (a symmetric suspicion-reduction counter-mechanic) landing in the same authoring pass as D5's merge; B1: starting count = 4 (Valorsmark/Hafenmark/Varfell/Church of Solmund), matching valoria_political_hierarchy_v30.md's existing 3-duchy+Church structure, with emergent factions (RM, Lowenritter-style splits, an Altonia-usurper archetype) explicitly allowed. Resolves ED-FA-0001. next_free bumped 47->48. ED-IN-0046 allocated 2026-07-13: governance_consolidation_v1.md D1-D5 RULED (Jordan "ratify commit all" on PR #129 + PR #129's merge, per the ED-1094 merge-ratifies convention) -- card-deck/AP-economy/Compact-as-Debt/Mandate-retirement/1.0d-merge all accepted per their own stated recommendations; D6 (G606 wiring), B1 (faction count), B2 (S-006 identity), B12 (Territory naming) explicitly left open (no stated recommendation existed for any of the four). next_free bumped 46->47. ED-IN-0044/0045 allocated 2026-07-12 (RENUMBERED from this branch's original ED-IN-0038/0039 -- COLLISION: this PR (#124, branch claude/repo-audit-testing-methodology-w2f1wo) read next_free=38 and allocated ED-IN-0038/0039 for the simulation-harness methodology proposal + Gate-0 prototype (tools/sim_harness/), but PR #126 ("Skills-ecosystem staleness remediation, Phase 7") concurrently claimed ED-IN-0038 through ED-IN-0043 and merged to main first -- renumbered this PR's entries during the merge reconciling onto main, same pattern as the ED-IN-0031/0032 and ED-IN-0033/0034 collisions documented below): ED-IN-0044 = the ratified simulation/test harness methodology (designs/audit/2026-07-12-simulation-test-harness-methodology/) + Gate-0 prototype (tools/sim_harness/, six rounds of adversarial review/stress-testing, 34 bugs found and fixed, provisional-adapter support added post-ratification); ED-IN-0045 = the four section-9 quick-win findings, filed separately per Jordan's ruling, open/execution pending. See registers/editorial_ledger_in.jsonl for full resolution text. next_free bumped 44->46. ED-IN-0043 allocated 2026-07-12: adversarial verification pass on ED-IN-0038..0042 (PR #126) -- 3 independent read-only critics found and this same PR fixed: a real Ob-20-exception bug in valoria_dice.py's continuous resolver, a repeated "40-weapon" vs actual-51-weapon inaccuracy across 4 docs, a minor combat_engine_v1/workbench/balance.py CLI coverage gap (documented, not fixed -- out of scope), two intra-PR misses (arc-generator's dead compilation_current ref, design_registry.yaml's dead editorial_ledger.yaml ref), and a miscounted inline comment. See registers/editorial_ledger_in.jsonl. next_free bumped 43->44. ED-IN-0038..0042 allocated 2026-07-12: skills-ecosystem staleness remediation "Phase 7" (continuing the 2026-07-11 audit-ecosystem batch, ED-IN-0032..0037) -- 0038 fixes across 8 skills + design_registry.yaml (stale ledger-file/HANDOFF/orchestrator refs, wrong archives-vs-designs output path); 0039 retires valoria-combat-simulator (superseded by combat_engine_v1/workbench/balance.py); 0040 adds valoria-dice-model's canonical continuous resolver mode; 0041 adds a PP-NNN allocation protocol to valoria-editorial-register; 0042 documents deferred ecosystem gaps (needs_jordan) -- see registers/editorial_ledger_in.jsonl and designs/audit/2026-07-12-skills-ecosystem-audit/. next_free bumped 38->43. ED-IN-0037 allocated 2026-07-11 (RENUMBERED from its original ED-IN-0032, read at next_free=32): dashboard extension — Balance & victory data card (personal-combat weapon matrix, faction win-share goldens extracted from sim/tests/, explicit no-data flags for mass_battle/social_contest/threadwork/settlement_territory) + Registers card (editorial ledger open/needs_jordan counts by lane, active patch-register counts); corrected the dashboard's stale "~87% degenerate win-share" callout to the debunked/corrected framing per sim/tests/test_f7_smoke_oracle.py. COLLISION 2026-07-11 (same failure class as the ED-IN-0031 collision documented below, resolved the same way): this PR (branch claude/github-project-dashboard-9e2n19) read next_free=32 and allocated ED-IN-0032 for the above work, but PR #122's audit-ecosystem consolidation batch concurrently claimed ED-IN-0032 through ED-IN-0036 for its own six phases and merged to main first — renumbered this PR's entry ED-IN-0032 -> ED-IN-0037 during rebase reconciliation (next_free 32 -> 38, skipping over PR #122's now-occupied 0032-0036 range). ED-IN-0036 allocated 2026-07-11: Phase-6 (partial) audit-ecosystem batch (forward-only findings-disposition discipline added to valoria-vector-audit + valoria-simulator SKILL.md output contracts; two more stale vector-audit references corrected in passing -- scripts/vector_audit.py's stub status, designs/audit/ -> deprecated/archives/audit/ path for the 2026-04-29 run); status resolved, see registers/editorial_ledger_in.jsonl. ED-IN-0035 allocated 2026-07-11: Phase-5b audit-ecosystem batch (.github/workflows/audit-refresh.yml -- scheduled decisions-digest refresh; vector-audit mechanical-refresh job deferred, vector_audit.py found to be a stub with no stage dispatcher); status resolved, see registers/editorial_ledger_in.jsonl. ED-IN-0034 allocated 2026-07-11 (renumbered from its original ED-IN-0033 during the collision reconciliation below): Phase-3 audit-ecosystem batch (skills/valoria-editorial-register/SKILL.md full rewrite against the real JSONL/lane-split ledger schema, replacing a 3-months-stale YAML-era doc); status resolved, see registers/editorial_ledger_in.jsonl. COLLISION 2026-07-11, resolved by renumbering the later-merging side (same failure class as the ED-1088/1090/1094 flat-sequence saga above): PR #121 (main, bd5c798) and this session's Phase 1 (branch commit 05141e6) both read next_free=31 concurrently and both allocated ED-IN-0031. PR #121 merged to main first, so it keeps ED-IN-0031 (mobile-friendly GitHub Pages status dashboard: dashboard/ + tools/audit_registry.py + tools/dashboard_data.py + tools/build_audit_registry_backfill.py + tools/ci_audit_registry_check.py + .github/workflows/dashboard.yml, retrofitting the 8 audit/simulation-run skills to log verdicts to references/audit_registry.jsonl). This session's colliding entries were RENUMBERED one step each during the rebase reconciling onto main: ED-IN-0031 -> ED-IN-0032 (Phase-1 audit-ecosystem batch -- mechanic-audit params path fix, quantity_registry/descriptor_registry dedup, npc_audit_report_gen path portability, canon_coverage_check GitHub-API->working-tree port, ci_checks_registry known_issues closure), ED-IN-0032 -> ED-IN-0033 (Phase-2 audit-ecosystem batch -- mechanics_index_gen.py --strict + ci_generation_consistency.py + canon_coverage_check.py --strict --json wired into CI report-only; social_contest_audit.workflow.js retired to deprecated/; ci_checks_registry.yaml regenerated 8->22 entries with a new broken_dependency_checker.py::check_ci_registry_coverage() verifier; tools/README.md regenerated from the registry), and ED-IN-0033 -> ED-IN-0034 (Phase-3, this entry). ED-IN-0030 allocated 2026-07-08: phantom 'debt scene' mechanic flag (scale_transitions_v30.md §4.3.2 row 8 cites a mechanic undefined in faction_politics_v30.md; needs_jordan, surfaced executing ED-IN-0016). ED-IN-0029 allocated 2026-07-08: attribute/value coherence audit (quantity-layer extension of the Key & Echo armature; read-only; 88-row census; docket UNRULED - Jordan picks). ED-IN-0027 allocated 2026-07-08: pessimist subtractive NERS audit of player-available actions (read-only scope-gate; PROPOSED §8.2 subtractive-disposition extension; docket UNRULED - Jordan picks). ED-IN-0001 cutover; ED-IN-0002 docket adjudication; ED-IN-0003..0008 allocated 2026-07-05: NERS-audit accepted work items E-2/E-3/E-4/E-6/E-7/E-11 (convergence detector, articulation triggers, walkthrough policy, steering reconcile, register back-propagation gate, naming unification); ED-IN-0009 workplan v6 + steering reconcile; ED-IN-0010 workplan navigator; ED-IN-0011 PR #78 sign-off record; ED-IN-0012..0013 DOUBLE-ALLOCATED 2026-07-05 by PR #83 (SC-audit batch: throughline-registry/UI refresh; rolling-engine re-run, sequenced after ED-SC-0004) AND by PR #81/#82 (edge-playability §7 items 1-2: registry×rendering sweep; GM-token sweep); ED-IN-0014..0016 allocated 2026-07-05: edge-playability §7 items 3/6/9 (key the silent emitters, seam-feedback convention, index the joints); ED-IN-0017 allocated 2026-07-07: unaddressed-areas comprehensive audit (this PR); ED-IN-0018 allocated 2026-07-07: Key & Echo armature program (this PR)
```


## SE — Settlements

<a id="se"></a>

*Moved verbatim from `id_reservations.yaml` line 236, 2026-08-01. 3104 chars.*

```text
BLOCK RELEASED 2026-07-30 (ED-IN-0098, W5 capstone walk-back). Was 0049-0052 RESERVED 2026-07-29 for cross-lane EDs the IN code-shape waves file in SE. MEASURED max allocated = ED-SE-0049; unused 0050-0052 (3) returned to the pool, next_free 53 -> 50. Freeze lifted: read next_free, allocate, bump, co-commit as normal. // ED-SE-0045..0048 allocated 2026-07-13: 2026-07-13 multi-agent audit P1 batch (designs/audit/2026-07-13-multi-agent-audit/) -- 0045 Prosperity->Treasury x50 vs x10 conflict (settlement_layer SS1.3 L47 vs SS1.8 L169); 0046 Fortress-City/Cathedral-City/Village missing from SS1.2 + base(Type) weight table (W_s uncomputable for the 2 compound types); 0047 SS4.7 Black Markets modifies invalid 'Settlement Wealth'/'Settlement Accord' fields; 0048 settlement_adjacency prose stale (36 settlements/PP-723) vs PP-726-rebuilt geography YAML (37/55). All open/needs_jordan. NOTE: mechanic_audit GAP-02 (Fort Level province->settlement granularity) NOT re-filed -- already ratified + tracked under ED-SE-0006 (open, execution pending); its SS2.2 mass_battle-SSA.4 mis-citation residual folds into ED-SE-0006 execution. next_free bumped 45->49. // ED-SE-0018..0044 allocated 2026-07-09: comparative-governance-research docket round 2 (designs/audit/2026-07-09-comparative-governance-research/) — same batch as the FA-lane note above; 7 authored into governance_play_redesign_v1.md/settlement_layer_v30.md as PROPOSED (ED-SE-0018/0019/0020/0021/0022/0023/0024 — Kokudaka Survey + Encabezamiento locked-extraction substrate, Goningumi cells, Za patron-lapse, Clerk Capacity, Ordenanza Ratification, Seggio Council), rest open/needs_jordan (see registers/editorial_ledger.jsonl and registers/handoffs/HANDOFF_SE.md). next_free bumped 18->45. ED-SE-0007..0017 allocated 2026-07-08 (THIS branch, RENUMBERED +1 from this branch's original ED-SE-0006..0016 -- collided with origin/main's concurrent ED-SE-0006, the coherence-audit Fort-Level bundle below): FA/SE historical-precedent research docket (designs/audit/2026-07-08-fa-se-historical-precedent-research/) — Weberian L/PS derivation table (SE-1, highest priority), dearth chain + grain routes, charter/prescription, entry terms, succession continuity, oversight toolkit, church-state seam, marcher autonomy, Weight-as-Exit, citation-patch CP-2; several needs_jordan forks (0013,0014,0015,0017). ED-SE-0006 allocated 2026-07-08 (origin/main): attribute/value coherence audit (ED-IN-0029) — Fort Level province→settlement inheritance (default: settlement = province value) + Garrison/Local-Economy/Public-Order §9 ratify-vs-[ASSUMPTION]-mark, both OPT-AV-18; decisions ratified, execution pending. ED-SE-0005 allocated 2026-07-08: pessimist-audit SE work items — Trade/Grant prune, Sponsor merge, etc. — execution pending (decision ED-IN-0027). ED-SE-0001 allocated 2026-07-05: NERS-audit E-1 accepted work item (governance_play_redesign path); ED-SE-0002 allocated 2026-07-05: edge-playability §7 item 4 (Accord/Order stacking ruling, needs_jordan), edge-playability §7 batch (PR #81)
```

## Round-2 block D (ED 1050-1099)

<a id="d-block"></a>

*Moved verbatim from `id_reservations.yaml` line 46, 2026-08-01. 1214 chars.*

```text
1050-1054 ecosystem Top-5; 1055-1079 reserved -> contest_rebuild; 1080 grounded combat re-baseline (percussion/armour/use-mode/gap-game); 1081-1087 -> 2026-07-01 month-overview consolidation (LB-21 session); 1088 -> 2026-07-02 mass-battle LC-8 execution (shared ancestry, consistent on both branches); 1089-1091 -> 2026-07-02 Jordan rulings (field default flip / subunit cap 11 / recoil frontal zone-gate), PR #62 (shared ancestry); 1092 -> 2026-07-02 Stage F investigation + D2 fidelity-fix verification, PR #65 (shared ancestry); 1093 -> 2026-07-02 origin/main month-overview-consolidation lane: J-38 propagation-spec authorship (RENUMBERED twice on that lane, see its own history); 1094 -> 2026-07-02 origin/main month-overview-consolidation lane: merge-ratifies-by-default governance convention (RENUMBERED twice on that lane); 1095 -> 2026-07-02 THIS branch: T1-T4 charge-recoil actor/timing/reach ruling (renumbered from this branch's own original ED-1093 -- third collision, see verified_live_max note above); 1096 -> 2026-07-02 THIS branch: movement/pathing audit ratification, Fable-led/Opus-verified (renumbered from this branch's own original ED-1094)
```


## contest_rebuild sub-block (ED 1055-1079)

<a id="contest-rebuild"></a>

*Moved verbatim from `id_reservations.yaml` line 50, 2026-08-01. 839 chars.*

```text
CR1-CR7 fold-in, armature, 4 games, seam-closure, probes, settlement; 1055 (CR1/CR2 + D0-3 HYBRID substrate confirmation) + 1056 (CR3 three-tracker / Face primitive) filed Stage 1d 2026-07-01; 1057 (ED-137 Panel closure / VoteAtClose) + 1058 (Stage-2 typed dictionaries + flavor) filed Stage 2 / Gate B 2026-07-01; 1059 (Panel proceeding-reachability, finding 3) + 1060 (Obscuring single-exchange dominance / Doubt Marker terminal value, finding 4) filed Stage 2 / Gate B round-2 revision 2026-07-01; 1061 (Guilds either-axis boost context-derived-from-venue, no-GM canon fix) filed Stage 2 / Gate B FINAL ratification 2026-07-01; 1062 (Stage 3 / Gate C FINAL ratification: armature 4th axis, epideictic compression, CR5 scope, CR4 reachability fix + canon propagation) filed 2026-07-02
```


## FI — Field investigation

<a id="fi"></a>

*Moved verbatim from `id_reservations.yaml` line 193, 2026-08-01. 1242 chars.*

```text
ED-FI-0006/0007/0008 allocated 2026-07-13: 2026-07-13 multi-agent audit P1 batch (designs/audit/2026-07-13-multi-agent-audit/) -- 0006 SS2.3 wound rule '-1D per wound' contradicts SS2.2's '+0.15 Ob, NEVER -1D' (un-propagated ED-PC-0005/0006); 0007 SS2.4 Thread-op wound '+1 Ob' superseded by engine/params/fieldwork.md's '+0.15 Ob/wound' (ED-PC-0006); 0008 P-06 violation -- Knot mechanic drains threadcut being's Coherence (fieldwork SS5.6b + cross-lane knots_v30 SS9, must fix both). 0006+0007 may combine; 0008 is cross-file. All open/needs_jordan. next_free bumped 6->9. // ED-FI-0005 allocated 2026-07-08: attribute/value coherence audit (ED-IN-0029) — Knot Pool formula ratified ((Spirit×2)+History(Rel)+3, Bonds eligibility-gate only, OPT-AV-9); execution + regression test pending. next_free bumped 5->6. ED-FI-0004 allocated 2026-07-08: pessimist-audit FI work items — Interview merge, Dialogue-Lattice refine — execution pending (decision ED-IN-0027). ED-FI-0001 allocated 2026-07-05: NERS-audit E-12/GAP-1 accepted work item (investigation-lane audit); ED-FI-0002 allocated 2026-07-05: edge-playability §7 item 7 (counter-espionage loop), edge-playability §7 batch (PR #81)
```


## WR — World

<a id="wr"></a>

*Moved verbatim from `id_reservations.yaml` line 199, 2026-08-01. 1135 chars.*

```text
BLOCK RELEASED 2026-07-30 (ED-IN-0098, W5 capstone walk-back). Was 0009-0012 RESERVED 2026-07-29 for cross-lane EDs the IN code-shape waves file in WR. MEASURED max allocated = ED-WR-0009; unused 0010-0012 (3) returned to the pool, next_free 13 -> 10. Freeze lifted: read next_free, allocate, bump, co-commit as normal. // ED-WR-0008 allocated 2026-07-13: 2026-07-13 multi-agent audit P1 -- P-25 'Scale-based Mending Stability' override table in threadwork_v30 (line 40) truncated to header + 'Object' with zero data rows (original authoring truncation, git-confirmed). Open/needs_jordan; can anchor a WR threadwork batch with the P2 tail. next_free bumped 8->9. // ED-WR-0007 allocated 2026-07-08: pessimist-audit WR Scene-Slate + threadwork work items, execution pending (decision ED-IN-0027). ED-WR-0001 + ED-WR-0002 allocated 2026-07-05: NERS-audit E-5 (peninsular_strain GD-1 sweep) + E-8 (MS/RS name sweep) accepted work items; ED-WR-0003 allocated 2026-07-05: edge-playability §7 item 10 (ambient-fabric window + Appraise Revelation), edge-playability §7 batch (PR #81)
```

