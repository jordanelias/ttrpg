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

*Trimmed from `id_reservations.yaml` line 111 again, 2026-09-27 (the live row had re-grown past the 600-char lane-row cap, `test_narrative_does_not_creep_back_into_the_state_file`). ED-MB-0065..0075, full detail in `registers/editorial_ledger_mb.jsonl`:*

```text
ED-MB-0065 (2026-07-xx): J2 ruled-but-not-executable; PENDING Jordan's re-issue. ED-MB-0067 (2026-09-25, two rows): squad-engagement-engine-v5 synthesis against canon (proposals/2026-09-25-squad-engagement-synthesis.md); Part C is Jordan's direct, in-session ruling on six items (C1-C6). ED-MB-0068 (2026-09-26): d.1 executed — massbattle.py:_faction_to_unit derives morale start from Faction.Sta, superseding the untagged starting-formula sentence (NOT PP-711, the separate morale-reset rule). ED-MB-0069 (2026-09-26): Tier-1 build slate (A1 routes / A2 perception-gated orders / A4 go-code latency / A6 ammunition) executed, agonist-antagonist relay, three build/fix rounds, F1-F13 findings. ED-MB-0070 (2026-09-27): two disclosed Tier-1-review loose ends closed — byte-exact test wiring (a root-cause bat.py sys.path bug, plus a dead valoria-ci.yml lanchester_signature step); PP-711 confirmed not a gap at the strategic seam. ED-MB-0071 (2026-09-27): A8 executed — ROUT_CASCADE_FRAC default 1.0->0.6 by sweep (workbench/rout_cascade_sweep.py), corrected from an under-evidenced first draft (0.5) after review found a wrongly-excluded row pair; zero effect on the live campaign (single-subunit armies). ED-MB-0072 (2026-09-27): C4 executed — feigned retreat's fog/recognition machinery (PP-256) was already correct; only the 'feign_retreat' Order trigger was missing, added as a pseudo-field mirroring A4's fire_signal. ED-MB-0073 (2026-09-27): A3+C5 executed — Officer dataclass + build_army's officers= param (ED-1090's queued span-of-control mechanism), corrected after review found a mode-switch loophole letting an idle officer bypass both the SUBUNIT_CAP and Command ceilings; not yet campaign-reachable. ED-MB-0074 (2026-09-27): A7 executed — terrain.py derives one of A.9's six rows from the engagement province's geography, wired into resolve_mass_battle's previously-dead terrain param; REWRITTEN after adversarial review found and fixed four defects (fort_level read from the geography YAML's own authored copy rather than the engine's live, garrison-derived value -- a duplicated single-owned fact; a fabricated 'ED-780's own citation' for the fortification-dominance rule; the FOREST_BROKEN speed branch described as merely campaign-unreachable when run_battle never reads .speed at all, full stop; fjord_coast mismapped to OPEN_FLAT against the geography file's own 'broken inlet' cost-matrix entry). ED-MB-0075 (2026-09-27, needs_jordan): C2/C3 envelopment damage-to-morale coupling — a complete DESIGN (proposals/2026-09-25-squad-engagement-synthesis.md Part D), not executed; recommends a roll-gated Discipline check (reusing discipline_check_cascade unmodified) over a formula-only or roll-scaled alternative, escalated because the check-form is a live game-feel choice Part C's own ruling left open. ED-MB-0075's superseding row (2026-09-28) reads Part D's own declines as picking option (2). ED-MB-0076 (2026-09-29): plan position 11's MB hand pass + 25 MB-GOLDEN's remainder EXECUTED — three stale "Default OFF" config.py comments (MB_FRICTION_CEV/MB_CLOSE_RANKS/MB_CELL_DAMAGE, all default ON since ED-MB-0001) corrected; ED-MB-0057's resolve_internal_collisions DELETE disposition executed (FORK row, restructure_ledger.md); ED-MB-0044's R3 gauge scenario fixed (stance='balanced'+kite, was both sides 'hold'). ED-MB-0077 (2026-09-29): ED-MB-0075 option (2) BUILT — resolve_engagements's pre-combat delta-sigma envelopment-shock penalty replaced by a shocked_a/shocked_b flag consumed post-damage in run_battle as a discipline_check_cascade-gated erosion (freed_attacker's own formula); goldens cell_field_mor0/cell_legacy_mor1 re-recorded (PER_CELL=1 only; unit_*_mor0 provably unaffected).
```


## PC — Personal combat

<a id="pc"></a>

*Moved verbatim from `id_reservations.yaml` line 124, 2026-08-01. 2978 chars.*

```text
BLOCK FULLY CONSUMED — 0 ids released 2026-07-30 (ED-IN-0098, W5 capstone walk-back). MEASURED max allocated = ED-PC-0055, i.e. EXACTLY the top of the block; next_free stays 56. ⚠ FINDING: this lane hit its reserved ceiling with zero headroom, so the reservation was undersized and the freeze was actively constraining it — size the next pre-allocation from observed burn rate, not a guess. Freeze lifted: read next_free, allocate, bump, co-commit as normal. Was 0041-0055 RESERVED 2026-07-29 for the dedicated PC session (audit/2026-07-26-combat-balance-customization-state/combat_execution_plan.md §15): draw PC ids from this block, do not read-and-bump mid-run (IN W0a pre-allocation — see the IN lane line). // SKELETON ONLY (Jordan 2026-07-24, CLAUDE.md §4): ONE SHORT LINE per ED. Prose lives in registers/editorial_ledger_pc.jsonl + audit/2026-07-24-combat-four-dimension-audit/ (index+infill). Do not grow prose here — it fights the 15k register cap. # ED-PC-0034..0039 = the four-dimension read-only audit (fiat/orphans/conflicts/tuning) and its batch-wise remediation, each batch adversarially reviewed: 0034 correctness (represent-gate path-dependence, riposte exposure floor, grab sign-flip); 0035 dead code + stale prose (8 keys un-leaked from the Godot contract, imposition machinery retired); 0036 fiat retirement (percussion sel_perc, pursuit_sigma, cut_thrust versatility, ATTACKER_BIAS/UPSET_FLOOR tagged); 0037 structural thresholds (first-actor race -> cadence x anticipation from an arbitrary phase; soft closed-latch; ATTACKER_BIAS retired) + 0037.1 review corrections; 0038 capability-gated penetration (damage now agrees with adef_cap, which moved to core as single owner); 0039 knee corrections (clamp capability at >=0 — ADEF_CUT is a sigma penalty, not a magnitude; grip/room threaded; one-weapon participation guard; K swept); 0040 the 0039 review — roster-wide primitive-derived participation guard (mutation-verified), 4 false claims retracted (incl. 0038's "estoc -> 0": it is the #1 plate weapon), medium round trip + ranseur covert-killer + F24 selection-vs-damage disagreement disclosed. # ED-PC-0029..0033 2026-07-24 = the reach/approach arc: arrest_impulse + tanh true_time (retire thrust_extension); closed-phase bind disengage; percussion -> stamina + poise stagger; penetration threshold (rapier plate fall-off); stale-grip fix + measure continuity. # ED-PC-0022..0028: U10 lever activation; fiat/broken-logic audit + imposition-fiat retirement; levels-of-investment; combinatorial audit + core.logistic(); HEMA grounding corrections; T_vuln + mode-aware heft; tradition gate on equipped. # ED-PC-0002..0021: U0 units-honesty; edges primitive; polearm choke counterbalance; weapon-class facing; half-sword roster + affordance; thrust authority + point-token scaling; attribute/value coherence; U9 recalibration; NERS-audit items. # ALL detail: registers/editorial_ledger_pc.jsonl.
```

*Trimmed from `id_reservations.yaml` line 124 a second time, 2026-09-29 (ED-PC-0058), to keep the live
row under `test_narrative_does_not_creep_back_into_the_state_file`'s 600-char cap — the row had grown
to 922 chars after the ED-PC-0058 allocation note was appended without first moving anything out. Full
detail for ED-PC-0056/0057, moved verbatim rather than summarised again:*

```text
ED-PC-0056 allocated 2026-08-08 (combat design-doc consolidation 5->1). block FULLY CONSUMED, 0
released 2026-07-30 (ED-IN-0098): max allocated ED-PC-0055 = exactly the block top, so the reservation
was undersized. 2026-08-27: 57 was allocated (ED-PC-0057, the fiat-ceiling abolition) after that row
was first mis-filed as a DUPLICATE ED-PC-0041 and renumbered. The 58 that followed was briefly correct
by accident — it had been bumped from 57 by the mis-filed row — and was correct by derivation from then
on, until ED-PC-0058 (below) consumed it.
```

**ED-PC-0058, 2026-09-29** (workplan `2026-09-28-the-plan-one-order-mc-v18-retired.md` position `12`,
"PC lane"): the `partisan` deletion (Jordan, 2026-09-20, choosing between renaming and deleting the
polearm to resolve its naming collision with the `pursuit_axes` pole of the same name — HANDOFF_PC's
own record, since the ruling was given alongside ED-IN-0261 and not transcribed into that entry's own
text) and Ob-from-defender in `combat_engine_v1/core.py` (Jordan, 2026-08-15, verbatim: *"DECISIVE_OB
for combat is stupid as hell and is dead because Ob should be determined by your opponent more than
anything"* — `tests/valoria/test_degree_ladder_single_owner.py`'s `RULINGS` dict, entry "2026-08-15 —
combat, and the sequence"). Both ruled, both ungated, neither `needs_jordan`. Full description in
`registers/editorial_ledger_pc.jsonl`.


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

**2026-09-26 — ED-IN-0262..0274 allocated, and the state-file comment condensed a second time.**
`tests/valoria/test_id_reservations_walkback.py::test_narrative_does_not_creep_back_into_the_state_file`
caught the IN row at 723 chars (cap 600) -- it was condensed once already at `ED-IN-0218`
(2026-09-12, below) and simply re-grew the same way, one ID's worth of narrative appended per
allocation with nothing ever moved out. Per the guard's own instruction the narrative moves here;
the row keeps a short summary and the pointer. The per-ID detail for this stretch (13f/13e/13d-i/
24d-i's build-then-verify pairs, the plan write-up and its correction, and `24d-i`'s own
correction pass) lives in `registers/editorial_ledger_in.jsonl`, one row per ID
(`ED-IN-0262`..`ED-IN-0274`), and is not re-duplicated here. The same run also caught a second,
unrelated pin gone stale: `test_the_2026_07_30_walkback_actually_moved_something` still expected
`SE` at 55, one allocation (`ED-SE-0055`, the `24d-i` dwelling-Site ruling, 2026-09-25) behind the
tree -- updated in the same commit as this condensation, per that test's own instruction.

### 2026-09-17/18 — `ED-IN-0246..0249`, and a two-unmerged-branches allocation

- **`ED-IN-0246`** — the governance/settlements/decisions execution pass: item 16 landed, items 1
  and 4 measured and held.
- **`ED-IN-0247`** — item 3b, a body finally falls, shipped at its control arm.
- **`ED-IN-0248`** — phase-6 item **6d**, the `beneficiary:` column closing `CAT-2`. ⚠ This read
  *"the `0248` slot"* while PR #416 was unmerged, because a citation whose ledger row this tree did
  not carry is what `tools/validate_ed_citations.py` calls NONEXISTENT — and it was right to. #416
  merged first, so the row is here and the citation is spelled properly again.
- **`ED-IN-0249`** — phase-6 item **6e**, `(Person, scar[axis])`, the first write to any `Person`
  interior field.

⚠ **`0248` AND `0249` WERE ALLOCATED ON TWO SEPARATE BRANCHES, NEITHER MERGED, AND THAT IS §4's
DOCUMENTED HAZARD ARRIVING RATHER THAN A MISTAKE.** Both branches were cut from the same `main`,
so both read `next_free: 248`. The second branch saw `0248` already taken by the open PR #416,
took `0249`, and bumped `next_free` to **250** so a third branch cannot re-take either. The same
collision hit a *section heading* in the same pair of branches — PR #416 holds `§7.3e` of
`01_THE_BUILD_ORDER.md` and the 6e branch numbered itself `§7.3f` around it.

**The lesson is the one `CLAUDE.md` §4 already states and is worth re-stating with a second
instance: renumbering to `next_free` does not escape a collision, because every live branch
renumbers to the same `next_free`.** What worked here was reading the OTHER branch's claim before
allocating, which is discipline and not a mechanism; `wiring_status.auto_allocation` remains the
structural fix and remains PARKED.


**2026-09-12 — ED-IN-0216 / 0217 / 0218 allocated, and the state-file comment condensed to fit the lane-row
cap.** `tests/valoria/test_id_reservations_walkback.py::test_narrative_does_not_creep_back_into_the_state_file`
caps a lane row at 600 chars; the IN row stood at 593 and the third of these allocations pushed it to 655.
Per the guard's own instruction the narrative moves here and the row keeps a summary and this pointer —
the same repair the 2026-07-29 condensation records further down.

- **ED-IN-0216** — master workplan **v7**. Supersedes v6 in authority; v6's *retirement* was attempted,
  reversed and deferred with its reason (v7 §6), so v6 is still on disk and this is not a `FORK:` row.
- **ED-IN-0217** — the emergent-narrative proposal suite (`proposals/2026-09-12-emergent-narrative-primitives-v2/`):
  four research documents NERS-audited as Valoria candidates, 21 false N-lines, and the counterparty
  finding measured over 177,170 candidates. `proposed`, **held back from ratification-on-merge in full.**
- **ED-IN-0218** — **Amendment 1 to v7** (filed as its §7): `ED-IN-0210` re-sorted — two of its three
  rulings are ruled-and-unexecuted **work**, not rulings, so they leave §3.1 for §3.2 — plus the
  counterparty control (84 candidates / 0 with another person as subject, against 84 / 56, on one authored
  value at `engine/season/harness/corpus_run.py:280`), the `H-71` rediscovery recorded as one, and the
  `HANDOFF.md` requirements-figure repair.

**2026-09-10 — ED-IN-0207/0208 collided WITHIN the lane; the later-merging side renumbered to
0209/0210.** Same failure class as the ED-IN-0031/0032, ED-IN-0033/0034 and ED-IN-0044/0045
collisions recorded further down, and resolved the same way.

`main` allocated **ED-IN-0207** to the σ-leverage resolution-diagnostic skill split (PR #390) and
**ED-IN-0208** to the blocking-rulings measurement (PR #393). Concurrently, branch
`claude/workplan-orientation-u1-u10-e13l6x` allocated **ED-IN-0207** to Jordan's verb-table rulings
of 2026-09-10 and **ED-IN-0208** to the Fable adjudication of that row. Both sessions read
`next_free: 207`; neither saw the other's bump. `main` merged first and its ids are cited in merged
PR titles, so they keep 0207/0208 and the branch's two rows became **ED-IN-0209** (verb-table
rulings) and **ED-IN-0210** (the Fable adjudication). No content changed on either side; the
branch's citations in `workplans/2026-09-09-r-execution-plan_part2.md` and `ED-FI-0009` were
rewritten in the same merge.

⚠ **AND IT HAPPENED A SECOND TIME, HOURS LATER, WHICH IS THE PART WORTH KEEPING.** While that merge
was being verified, `main` advanced again: PR #392 (the layer-conformance skill) allocated
**ED-IN-0209** — the id the branch's first row had just been renumbered *to*. The same rule applied
again and the two rows moved once more, to **ED-IN-0210** (verb-table rulings) and **ED-IN-0211**
(the Fable adjudication). `next_free` → **212**.

**Two collisions in one day, in one lane, is the argument FOR the rule rather than against it.** The
later-merging side moves, every time. A published id therefore never shifts under a citation already
aimed at it, and the cost falls entirely on the branch that has not landed yet — which is the side
that can still cheaply rewrite its own references. The alternative, letting whoever wrote it first
keep the number, would require rewriting citations on `main`.

⚠ **The lane tag did its job and this is what it does NOT cover.** `ED-<LANE>-NNNN` makes
CROSS-lane collision impossible by construction. WITHIN a lane the allocation protocol — read
`next_free`, allocate, bump, co-commit — is still discipline alone, and two concurrent sessions in
one lane can still both read the same value. The file header says so; this is the worked instance.

⚠ **A separate pre-existing defect was observed during the same merge and NOT repaired:** `main`
carries **two rows both numbered ED-IN-0208** (a measurement row and a correction row, both dated
2026-09-10), alongside the long-standing `ED-IN-0149` × 3. Renumbering an already-merged, already-
cited row is not a merge-resolution call; the tree's own precedent for that shape is ED-IN-0195,
*"split out 2026-08-21 from a duplicate ED-IN-0194 row whose needs_jordan CONFLICTED with its
twin"*. Recorded here so the next allocator sees it rather than rediscovering it.


<a id="in"></a>

**ED-IN-0228 COLLIDED ACROSS TWO CONCURRENT IN-LANE SESSIONS, 2026-09-16 — the fifth in this lane.**
PR #405 (the decision layer) and PR #404 (the faction creed) both read `next_free: 228` and both
allocated it. #405 merged to `main` first, so **`ED-IN-0228` IS THE DECISION LAYER**; #404 renumbered
on merge — creed `0228 -> 0229`, axis-roster single-owner `0229 -> 0230`, `next_free` 231. 26
citations were rewritten across 11 files, and `engine/engine_params/sim_params.json` was REBUILT from
its renumbered sources rather than hand-edited (§0.05 clause 3).

⚠ THIS IS §4's DOCUMENTED FAILURE MODE, NOT A NEW ONE. That section already says renumbering does not
escape a collision *"because every live session renumbers to the same `next_free`"*, and names the
structural fix — `wiring_status.auto_allocation` — as specified and PARKED. Four prior within-lane IN
collisions (2026-09-10/11) motivated that text; this is the fifth, and the first where the two
sessions were a merged PR and an open one rather than two open branches. The discipline worked
exactly as far as it can: both sessions read, allocated, bumped and co-committed, and still collided.

**ED-IN-0229 and ED-IN-0230 allocated 2026-09-14**, next_free 228 -> 230, both `status: landed`,
both `needs_jordan: false`. Moved here from the `IN:` lane row the same day, because two summaries
took that row from 528 to 694 characters against a 600 cap —
`test_narrative_does_not_creep_back_into_the_state_file` caught it, which is the guard doing
exactly the job its docstring describes. The lane row keeps a one-line summary and this pointer.

* **ED-IN-0229** — a faction's creed is an `OUGHT` subjected on its authored LEADER (never on the
  faction name, which Q4 would put into every member's deliberation as a referent naming no
  entity), and membership is weighted by a 0-100 loyalty carried on `Person.stance`, where
  `decision/choose.py::stance_toward` reads it. Jordan ruling, three parts. The loyalty is
  deliberately NOT on `Tenure.degree`: measured, nothing in `engine/season/` reads that field.
* **ED-IN-0230** — the four ethical axes had two unreconciled owners. `engine/substrate/keys.py`
  held a tuple literal and `engine/season/rosters.yaml: conviction_axes` held a `values:` list,
  while the roster's own note claimed a loader refusal that did not exist. Both now resolve to
  `references/descriptor_registry.yaml: axis_roster`, on the `conviction_roster` precedent.

**ED-IN-0214 allocated 2026-09-11 ON MERGE** (next_free 214 -> 215), **BECAUSE THE RENUMBER
DIRECTLY ABOVE LANDED ON A FOURTH COLLISION — AND THE ENTRY THAT MADE IT PREDICTED THIS IN ITS OWN
TEXT.** PR #396 renumbered 0212 -> 0213 to avoid PR #395's spine row. Between that renumber and
#396's merge, #395 allocated **0213** for its own second row (the conviction-matrix escalation) and
bumped its branch `next_free` to 214. So #396 merged holding 0213 and #395 arrived holding 0213.
Resolved on the same standing precedent, applied one step further: **the later-MERGING side
renumbers**, #396 merged first, so #395's row became **ED-IN-0214** and `next_free` went to 215.
Nothing merged was rewritten, on either pass.

⚠ **THE MITIGATION REPRODUCED THE DEFECT IT WAS MITIGATING, AND THAT IS THE FINDING.** The entry
above says, of the three collisions before it: *"renumbering to `next_free` does not make an id
safe, because every concurrent session renumbers to the same `next_free`."* Its own renumber is the
fourth instance of exactly that — it moved to `next_free` while a concurrent branch was moving to
the same `next_free`, which is the stated failure with one extra hop. **This is no longer a rate
argument.** Four collisions in two days, and the fourth was produced by the repair for the third;
the sub-block device the entry above declines to propose is the only one of the options on the
table that closes this by construction rather than by two sessions happening not to allocate in the
same window. Still not filed as a proposal here — §0.1 pt 5 wants a subject before a mechanism, and
this file is evidence rather than the place to rule — but the evidence is now that the incumbent
mitigation has a demonstrated failure mode, not merely an argued one.

**ED-IN-0213 allocated 2026-09-11** (next_free 213 -> 214), **RENUMBERED 0212 -> 0213 BEFORE EITHER
BRANCH MERGED.** The verification-cadence ruling (`CLAUDE.md` §0.4 — the full suite is a close step,
not an inner loop) was filed as the IN-lane id **0212**, which **PR #395** (`claude/repo-workplans-state-xk44q2`)
had already taken for *"ONE SPINE FOR EVERYTHING THAT REMAINS"*. Both branches read `next_free: 212`
off `main`; neither had merged. Renumbered on the standing precedent — *the later-merging side
renumbers* — with #395 keeping 0212 on the ordinary grounds: opened ~8 hours earlier, CI green,
`mergeable_state: clean`. **Caught before either merged, so no merged ledger line was rewritten** —
which is the only materially better version of this event than the three below it.

⚠ **This is the third within-lane IN collision in two days** (0207→0208→0209 on 2026-09-10, then
0212→0213). The entry below already names why: *renumbering to `next_free` does not make an id safe,
because every concurrent session renumbers to the same `next_free`.* That remains true and this event
is one more instance of it, not a new diagnosis. **The lane tag makes CROSS-lane collision impossible
by construction and does nothing for SAME-lane**, and IN is the lane every cross-cutting session
lands in — so IN collides at a rate the other eight lanes do not. A per-session reserved sub-block
(the device MB/PC/SC/FA/WR/SE blocks once used) would close it by construction rather than by
discipline. **Not proposed, and deliberately so:** it is process apparatus, and §0.1 pt 5 wants a
subject before a mechanism — recorded here as evidence for whoever rules on it.

**ED-IN-0209 allocated 2026-09-10** (next_free 209 -> 210), **RENUMBERED TWICE ON MERGE: 0207 -> 0208
-> 0209.** Two same-lane collisions on one branch, back to back — the case the `ED-<LANE>` tag does
*not* prevent by construction, and the same failure class recorded below at ED-IN-0031, 0032,
0044/0045, 0048/0049/0050, 0148 and 0152. PR #390 took 0207 while this branch was open; PR #393 —
itself renumbered 0207 -> 0208 by a third concurrent session for the same reason — then took 0208
before this branch could merge. ⚠ **The second hit is the informative one: renumbering to
`next_free` does not make an id safe, because every concurrent session renumbers to the same
`next_free`.** Recorded as evidence; no guard is proposed here (§0.1 pt 5 — the subject is this
repository's process, not the game). The work: the
`layer-conformance` skill —
`skills/layer-conformance/SKILL.md`, one skill with two lenses (layer PLACEMENT, and Layer-1
CONFORMANCE of code against `architecture/meta/04_CODE_ARCHITECTURE.md`), owning the METHOD while
`CLAUDE.md`'s layer table and `architecture/` keep the definitions. Wired into `CLAUDE.md` §9's
routing table. Filed here and not on the lane row for the reason the 0203 entry below already
gives: that row is at its 600-char cap. See `registers/editorial_ledger_in.jsonl`.

**ED-IN-0203 allocated 2026-09-07** (next_free 203 -> 204), moved here rather than onto the lane
row because that row sits at 598 of its 600-char cap — any append breaks
`test_narrative_does_not_creep_back_into_the_state_file`, exactly as it did to the 0170/0171
append below at 659. The guard is right and the fix is the one it names.

- **ED-IN-0203 — the `shape.py` decomposition.** Breaking the 6,771-line idealized system into
  holonic modules addressed BY SYMBOL, so the eight play surfaces can be developed in parallel.
  Zero game yield; a completed split is NOT milestone progress under §0.2.
  ⚠ **A PROVENANCE CORRECTION, and it is why this ID exists.** Steps 0b/1/2 cited `ED-IN-0202`,
  which is the cross-lane reading of the game (2026-09-05) and names no `season/` file. No ID had
  been allocated for this work at all — §4's read-next_free-allocate-bump-co-commit was skipped.
  Found by an adversarial pass verifying provenance BY HAND against the ledger, which is precisely
  the leak §7 names: a miscited but REAL id resolves, so `validate_ed_citations` passes it. The
  gate can tell an invented ID from a real one; it cannot tell a right one from a wrong one.

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


### 2026-09-17 — ED-IN-0236 / ED-IN-0237 (governance and holdings) — ~~0231 / 0232~~, RENUMBERED ON MERGE

⚠ **THE SIXTH WITHIN-LANE IN COLLISION, AND THE SECOND IN TWO DAYS ON THIS SAME WINDOW.** This pair
was allocated **ED-IN-0231 / ED-IN-0232** against a `next_free` of 231, read on 2026-09-17. While the
branch was open, **#407 landed on `main` having taken exactly those two numbers on 2026-09-16** — the
design-prose quarantine and the Key-substrate retirement — which is the section two below this one,
where 0231 arrives as the *third* claimant on the 0228 window and nobody had yet seen it. `main` landed
first, so **`main` keeps 0231 / 0232 and this branch renumbered to 0236 / 0237** on the merge of
2026-09-17. `next_free` 231 -> **238**.

**Round two's ED-IN-0233 / 0234 / 0235 did NOT collide** and are unchanged: `main` never allocated past
0232, and its own `next_free` read 233 — so the two branches' windows abutted exactly rather than
overlapping there. That is luck, not discipline.

**And it is the worked example of the sentence in `CLAUDE.md` §4 that a session keeps reading as
advice:** *"renumbering does not escape a collision, because every live session renumbers to the same
`next_free`."* Both branches read 231 and both bumped — one to 233, one to 236 — and neither reading was
wrong at the moment it was taken. The structural fix, `wiring_status.auto_allocation`, is specified and
PARKED in `references/id_reservations.yaml`; until it lands, the only mitigation is the one §4 names:
**land the `next_free` bump on `main` before anything cites the number**, which narrows the window and
does not close it. **Any citation of `ED-IN-0231`/`ED-IN-0232` dated 2026-09-17 in this branch's
history means `ED-IN-0236`/`ED-IN-0237`; before the merge there was no other reading.**

Both belong to `proposals/2026-09-17-governance-and-holdings/`, PROPOSED and
HELD BACK IN FULL; nothing ratified on merge. **Round two supersedes both in part** — see the
ED-IN-0233 / 0234 / 0235 section below, and `proposals/2026-09-17-governance-and-holdings-r2/README.md`
for what survives.

- **ED-IN-0236 — seats and policy** (allocated as ~~ED-IN-0231~~). Governance at every rung, hearth -> realm. Its spine is a
  CONFORMANCE DIVISION, which is the finding: most of the seat model is already ratified Layer 1 and
  merely unbuilt (`architecture/meta/04_CODE_ARCHITECTURE.md` §B.7 ships `Seat`, rejects the
  `establishment` field, deletes `judging_set_rule`, and carries the MECHANICAL invariant that purview
  is asked of the seat exercised through `Act.via`). Extensions: policy as a dispensation Record held
  by its issuer with the seat read from `Act.via`; `in_force(w, rung, clause)` as a nearest-ancestor
  walk; seven clauses onto the closed seven `requires` forms; a `purview` question source; `H-71`
  closed person-side from the holder's own ledger. Three field placements were repaired against
  ratified Layer 1 — `Tenure.conferrer` is deleted, `Tenure.payload` is retired for `term?`, and
  `Proposition.scope` is already written and read. **`needs_jordan: true` for one fork only:** does a
  nearer rung's clause or a higher rank win a collision (recommendation: nearest, with a superior's
  `reach: all` override).
- **ED-IN-0237 — the player surface and the build order** (allocated as ~~ED-IN-0232~~). One id for two documents because the
  second is the execution plan for the first three. Records that the interface can only offer what the
  engine raises a question about (four sources today), carries a pre-flight loader-refusal checklist
  derived by planting each defect, and states the gate-contract rule: work is downstream of Arc 2 iff
  it is an `@effect_for` body or writes a Tenure whose subject is not the actor. Nine ruling requests
  were CLOSED with citations under `CLAUDE.md` §0's five-step gate rather than escalated.

Full text for both: `registers/editorial_ledger_in.jsonl`.

### 2026-09-17 (later) — ED-IN-0238 / ED-IN-0239 (HANDOFF_IN pass 2, and three resolutions)

- **ED-IN-0238 — the second `HANDOFF_IN` closed-work pass.** Moved 10 units / 3,809 tokens, proved
  lossless by `tools/verify_handoff_split.py --before HEAD` (0 lines lost). Widened `ED-IN-0221`'s
  marker predicate to match case-INSENSITIVELY after `**Awaiting Jordan**` slipped its lower-case
  `awaiting`; the widening kept four live-item sections in place that the old predicate would have
  moved. Filed `needs_jordan` on one question — what bounds the mandatory orientation surface — and
  **that flag is CLEARED by its own successor row**, per the append-only rule.
- **ED-IN-0239 — the three resolutions.** Jordan refused the multi-`Agent` deny (*"I want multiple
  agent dispatches"*, recorded in `CLAUDE.md` §10); `valoria-author` promoted as the second agent
  definition; and `ED-IN-0238`'s escalation answered as *clear the stale queue*, not *edit Layer 0* —
  §0.3 had already measured that shrinking the orienting surface did not change session behaviour.
  Four queue entries closed with citations, each verified at the call site; 17 further candidates
  REFUSED as path citations rather than dead subjects.

### 2026-09-17 (later still) — ED-IN-0243 (the seam between the governance suite and the behaviour layer)

**Why an id at all:** two suites written a day apart —
`proposals/2026-09-17-governance-and-holdings-r2/` (ED-IN-0233/0234/0235, ED-SE-0053) and
`proposals/2026-09-16-conviction-decision-layer/` — **do not cite each other**, and both were about to
be built. They touch eight shared engine objects. `ED-IN-0243` is the unified proposal over the SEAM;
it supersedes neither and takes no position inside either.

- **One true conflict, at `H-71`,** and it is a defect in the QUESTION rather than the answer. The
  behaviour register's `CAT-6` offers Jordan three arms; r2's `03:794` declares H-71 closed by a
  **fourth** (the commission claim) with a build item already attached. Repair: `CAT-6` gains arm 4.
  ⚠ And **arm 2's carrier, `(Tenure, payload)`, is r2's own deletion-ledger row 13**, so choosing it
  is now an `RR-B`-shaped amendment — a price on neither suite's sheet.
- **Seven live forced orderings, one demoted, one collision measured ABSENT.** The absent one is worth
  the line: `STR-1` does **not** bind r2's body write, because `(Person, body)` is `[MAT, RES]
  MATTER/ACTS`.
- **The ruling sheet.** All 21 open questions from both suites through `CLAUDE.md` §0's five-step gate:
  **12 closed with opened citations, 9 escalated.** `STR-1` — the largest claimed gate, held to block
  five categories at once — **closes at step 3**: the six `Person` rows are `steps: [RES]`,
  `class: "ACTS"`, each with its own `emits:` kind, so they are **a licence nobody has taken up**, not
  the prohibition the register states. That close was only available after correcting the proposal's
  own first-draft error, which had called those rows `INTERIOR`.
- **Method note, since it is the reusable part:** three passes over one shared extract (§10 — *share
  the reading, fork only the judgment*). **Both independent passes found real defects in the author's
  document**, including the class-name error above and two seam points it had missed. Corrections are
  struck-and-kept in place.

Allocation note: `next_free` 243 → 244. Held back in full; `ED-1094`'s ratify-on-merge is refused.

### 2026-09-17 (rulings) — ED-IN-0244 / ED-IN-0245 (AX-7, and the eight remaining escalations)

**Jordan ruled all nine of `ED-IN-0243`'s escalations in session.** Two ids, because one of them
amends a RATIFIED Layer 1 file and needs its own citation.

- **`ED-IN-0244` — `AX-7` added to the axiom set.** *No character touches the world directly.* The
  sanctity is the **brute physical fact** — ink meeting paper, air moving — and three layers are held
  apart: the ontical performance, the performer's own understanding, and everyone else's. (2) runs on
  its own mechanism (a person does not witness themselves) and **is revisable by (3)**. Divergence is
  governed by channel + competence + prior belief together. **Scope clause:** it reaches what
  HAPPENED, never what is PERMITTED — remits are certain. **It binds the character, never the
  player**, whose option set narrows while their understanding does not. The live falsifier is
  `witness.py:191`, which all six prior axioms permit. ⚠ The count has moved five → six → seven.
- **`ED-IN-0245` — the other eight.** RR-A fold; RR-C withdrawn; CAT-6 arm 2; RR-B limb by limb
  (B-4 withdrawn on a misread question mark that r2 made first and this suite inherited); STR-6
  `conviction` = religious affiliations and intensities, as a vector, with confliction DERIVED;
  STR-2's axes found mis-recorded and the thirteen superseded; RR-2 capacity plus **migration as a
  verb**, since `move` is travel and `residence` has no writer.

Allocation note: `next_free` 244 → 246.


Allocation note: `next_free` 238 → 240 across the two. The `ED-IN-0236/0237` renumber narrative that
used to be duplicated on the `IN:` lane row lives at the subsection above it — one owner, per §0.05
clause 3, which is why the row now carries state and a pointer only.

### 2026-09-27/28 — ED-IN-0279, 0280, 0281 allocated; a sixth within-lane collision, renumbered

**`ED-IN-0279`** allocated 2026-09-27 (`needs_jordan`): the `mc_v18` retirement plan's Stage M4, the
field-battle verb and what a loss writes.

**`ED-IN-0280`/`ED-IN-0281` COLLIDED, 2026-09-28** — the same class as the 2026-09-10/16 collisions
above: two concurrent sessions both read `next_free: 280` and both allocated `ED-IN-0280`.
`origin/main`'s PR #437 (the `methodology` skill) merged first and keeps `ED-IN-0280` (status
resolved, not `needs_jordan`: the skill added at `skills/methodology/SKILL.md`, per Jordan's
directive). This branch's PR #438 renumbered its own allocation to **`ED-IN-0281`** (status resolved,
no ruling needed): THE PLAN re-adopted as the single order, superseding the 2026-09-18 plan and
retiring `mc_v18` in full (`workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md`). Neither
commit's content changed, only the number. `next_free` 280 → 282.

Moved here from the `IN:` lane row 2026-09-29, because the row's narrative reached 804 characters
against the 600 cap — `test_narrative_does_not_creep_back_into_the_state_file` caught it. The lane
row keeps a one-line summary and this pointer, as every prior instance of this same pattern does.

### 2026-10-01 — ED-IN-0282 allocated

**`ED-IN-0282`** (ruled by Jordan): the telling workplan, adopted and ordered built
(`workplans/2026-10-01-telling-workplan.md`). Allocated in the steering `[editorial]` commit, which
lands before the first build position cites it. `next_free` 282 → 283.

## IN — the 2026-07-14 duplicate-key repair (ED-IN-0064, finding OBS-IN-1)

<a id="dup-key"></a>

*Moved verbatim from `id_reservations.yaml` line 226, 2026-08-01. 10738 chars.*

```text
# [ED-IN-0064 DUP-KEY REPAIR, finding OBS-IN-1] STALE DUPLICATE IN: mapping neutralized — was next_free: 63; the authoritative IN: line above now carries next_free:65. YAML last-key-wins had been resolving IN.next_free to this stale 63 (the recurring 2026-07-07 duplicate-IN class). Provenance retained (full text in registers/editorial_ledger_in.jsonl): ED-IN-0062 allocated 2026-07-13: cross-scale governance-grounding synthesis docket (designs/audit/2026-07-13-cross-scale-governance-grounding/) -- one graph + per-scale grounding matrix + pressure-key registry + classified gap register (COMPLETE-THE-CHAIN vs GENUINE-GAP) + precedent-fix decision-queue, spanning the spatial (settlement->territory->province->duchy->country) and political (factions/governance-type/franchise/caste/standing/parliament) spines; cross-cutting IN lane (SE/FA/SC/WR/GO); FILED, PROPOSED fixes, needs_jordan. next_free bumped 51->52. // ED-IN-0048/0049/0050 allocated 2026-07-13 (0049/0050 RENUMBERED from this branch's original ED-IN-0046/0047 -- COLLISION: this branch read next_free=46 and allocated ED-IN-0046/0047/0048 for the 2026-07-13 multi-agent audit's cross-cutting P1 batch, but origin/main's governance_consolidation_v1 ratification (PR #130) concurrently claimed ED-IN-0046/0047 for its own D1-D5/D6-B1 rulings and merged first -- renumbered this branch's colliding entries during merge reconciliation, same pattern as the ED-IN-0031/0032 etc. collisions documented below; ED-IN-0048 needed no renumber, 48 was still free): ED-IN-0048 = piety_track home conviction_track_v1.md unregistered in canonical_sources.yaml (COORDINATE with ED-SC-0003); ED-IN-0049 (was ED-IN-0046) = empty SS3.3 Personal->Contest Handoff Rule (scale_transitions_v30); ED-IN-0050 (was ED-IN-0047) = literal 'GM adjudication'/'GM recognises' language vs no-GM invariant (scale_transitions SS1/SS3.2, same class as ED-WR-0007). All open/needs_jordan. next_free bumped 48->51. // ED-IN-0047 allocated 2026-07-13: D6 (G606 recall-clock wiring) and B1 (starting faction count) RULED directly by Jordan in conversation (not "ratify commit all"-inferred) -- D6: cumulative per-Defy-season accrual is canonical, conditioned on E11 (a symmetric suspicion-reduction counter-mechanic) landing in the same authoring pass as D5's merge; B1: starting count = 4 (Valorsmark/Hafenmark/Varfell/Church of Solmund), matching valoria_political_hierarchy_v30.md's existing 3-duchy+Church structure, with emergent factions (RM, Lowenritter-style splits, an Altonia-usurper archetype) explicitly allowed. Resolves ED-FA-0001. next_free bumped 47->48. ED-IN-0046 allocated 2026-07-13: governance_consolidation_v1.md D1-D5 RULED (Jordan "ratify commit all" on PR #129 + PR #129's merge, per the ED-1094 merge-ratifies convention) -- card-deck/AP-economy/Compact-as-Debt/Mandate-retirement/1.0d-merge all accepted per their own stated recommendations; D6 (G606 wiring), B1 (faction count), B2 (S-006 identity), B12 (Territory naming) explicitly left open (no stated recommendation existed for any of the four). next_free bumped 46->47. ED-IN-0044/0045 allocated 2026-07-12 (RENUMBERED from this branch's original ED-IN-0038/0039 -- COLLISION: this PR (#124, branch claude/repo-audit-testing-methodology-w2f1wo) read next_free=38 and allocated ED-IN-0038/0039 for the simulation-harness methodology proposal + Gate-0 prototype (tools/sim_harness/), but PR #126 ("Skills-ecosystem staleness remediation, Phase 7") concurrently claimed ED-IN-0038 through ED-IN-0043 and merged to main first -- renumbered this PR's entries during the merge reconciling onto main, same pattern as the ED-IN-0031/0032 and ED-IN-0033/0034 collisions documented below): ED-IN-0044 = the ratified simulation/test harness methodology (designs/audit/2026-07-12-simulation-test-harness-methodology/) + Gate-0 prototype (tools/sim_harness/, six rounds of adversarial review/stress-testing, 34 bugs found and fixed, provisional-adapter support added post-ratification); ED-IN-0045 = the four section-9 quick-win findings, filed separately per Jordan's ruling, open/execution pending. See registers/editorial_ledger_in.jsonl for full resolution text. next_free bumped 44->46. ED-IN-0043 allocated 2026-07-12: adversarial verification pass on ED-IN-0038..0042 (PR #126) -- 3 independent read-only critics found and this same PR fixed: a real Ob-20-exception bug in valoria_dice.py's continuous resolver, a repeated "40-weapon" vs actual-51-weapon inaccuracy across 4 docs, a minor combat_engine_v1/workbench/balance.py CLI coverage gap (documented, not fixed -- out of scope), two intra-PR misses (arc-generator's dead compilation_current ref, design_registry.yaml's dead editorial_ledger.yaml ref), and a miscounted inline comment. See registers/editorial_ledger_in.jsonl. next_free bumped 43->44. ED-IN-0038..0042 allocated 2026-07-12: skills-ecosystem staleness remediation "Phase 7" (continuing the 2026-07-11 audit-ecosystem batch, ED-IN-0032..0037) -- 0038 fixes across 8 skills + design_registry.yaml (stale ledger-file/HANDOFF/orchestrator refs, wrong archives-vs-designs output path); 0039 retires valoria-combat-simulator (superseded by combat_engine_v1/workbench/balance.py); 0040 adds valoria-dice-model's canonical continuous resolver mode; 0041 adds a PP-NNN allocation protocol to valoria-editorial-register; 0042 documents deferred ecosystem gaps (needs_jordan) -- see registers/editorial_ledger_in.jsonl and designs/audit/2026-07-12-skills-ecosystem-audit/. next_free bumped 38->43. ED-IN-0037 allocated 2026-07-11 (RENUMBERED from its original ED-IN-0032, read at next_free=32): dashboard extension — Balance & victory data card (personal-combat weapon matrix, faction win-share goldens extracted from sim/tests/, explicit no-data flags for mass_battle/social_contest/threadwork/settlement_territory) + Registers card (editorial ledger open/needs_jordan counts by lane, active patch-register counts); corrected the dashboard's stale "~87% degenerate win-share" callout to the debunked/corrected framing per sim/tests/test_f7_smoke_oracle.py. COLLISION 2026-07-11 (same failure class as the ED-IN-0031 collision documented below, resolved the same way): this PR (branch claude/github-project-dashboard-9e2n19) read next_free=32 and allocated ED-IN-0032 for the above work, but PR #122's audit-ecosystem consolidation batch concurrently claimed ED-IN-0032 through ED-IN-0036 for its own six phases and merged to main first — renumbered this PR's entry ED-IN-0032 -> ED-IN-0037 during rebase reconciliation (next_free 32 -> 38, skipping over PR #122's now-occupied 0032-0036 range). ED-IN-0036 allocated 2026-07-11: Phase-6 (partial) audit-ecosystem batch (forward-only findings-disposition discipline added to valoria-vector-audit + valoria-simulator SKILL.md output contracts; two more stale vector-audit references corrected in passing -- scripts/vector_audit.py's stub status, designs/audit/ -> deprecated/archives/audit/ path for the 2026-04-29 run); status resolved, see registers/editorial_ledger_in.jsonl. ED-IN-0035 allocated 2026-07-11: Phase-5b audit-ecosystem batch (.github/workflows/audit-refresh.yml -- scheduled decisions-digest refresh; vector-audit mechanical-refresh job deferred, vector_audit.py found to be a stub with no stage dispatcher); status resolved, see registers/editorial_ledger_in.jsonl. ED-IN-0034 allocated 2026-07-11 (renumbered from its original ED-IN-0033 during the collision reconciliation below): Phase-3 audit-ecosystem batch (skills/valoria-editorial-register/SKILL.md full rewrite against the real JSONL/lane-split ledger schema, replacing a 3-months-stale YAML-era doc); status resolved, see registers/editorial_ledger_in.jsonl. COLLISION 2026-07-11, resolved by renumbering the later-merging side (same failure class as the ED-1088/1090/1094 flat-sequence saga above): PR #121 (main, bd5c798) and this session's Phase 1 (branch commit 05141e6) both read next_free=31 concurrently and both allocated ED-IN-0031. PR #121 merged to main first, so it keeps ED-IN-0031 (mobile-friendly GitHub Pages status dashboard: dashboard/ + tools/audit_registry.py + tools/dashboard_data.py + tools/build_audit_registry_backfill.py + tools/ci_audit_registry_check.py + .github/workflows/dashboard.yml, retrofitting the 8 audit/simulation-run skills to log verdicts to references/audit_registry.jsonl). This session's colliding entries were RENUMBERED one step each during the rebase reconciling onto main: ED-IN-0031 -> ED-IN-0032 (Phase-1 audit-ecosystem batch -- mechanic-audit params path fix, quantity_registry/descriptor_registry dedup, npc_audit_report_gen path portability, canon_coverage_check GitHub-API->working-tree port, ci_checks_registry known_issues closure), ED-IN-0032 -> ED-IN-0033 (Phase-2 audit-ecosystem batch -- mechanics_index_gen.py --strict + ci_generation_consistency.py + canon_coverage_check.py --strict --json wired into CI report-only; social_contest_audit.workflow.js retired to deprecated/; ci_checks_registry.yaml regenerated 8->22 entries with a new broken_dependency_checker.py::check_ci_registry_coverage() verifier; tools/README.md regenerated from the registry), and ED-IN-0033 -> ED-IN-0034 (Phase-3, this entry). ED-IN-0030 allocated 2026-07-08: phantom 'debt scene' mechanic flag (scale_transitions_v30.md §4.3.2 row 8 cites a mechanic undefined in faction_politics_v30.md; needs_jordan, surfaced executing ED-IN-0016). ED-IN-0029 allocated 2026-07-08: attribute/value coherence audit (quantity-layer extension of the Key & Echo armature; read-only; 88-row census; docket UNRULED - Jordan picks). ED-IN-0027 allocated 2026-07-08: pessimist subtractive NERS audit of player-available actions (read-only scope-gate; PROPOSED §8.2 subtractive-disposition extension; docket UNRULED - Jordan picks). ED-IN-0001 cutover; ED-IN-0002 docket adjudication; ED-IN-0003..0008 allocated 2026-07-05: NERS-audit accepted work items E-2/E-3/E-4/E-6/E-7/E-11 (convergence detector, articulation triggers, walkthrough policy, steering reconcile, register back-propagation gate, naming unification); ED-IN-0009 workplan v6 + steering reconcile; ED-IN-0010 workplan navigator; ED-IN-0011 PR #78 sign-off record; ED-IN-0012..0013 DOUBLE-ALLOCATED 2026-07-05 by PR #83 (SC-audit batch: throughline-registry/UI refresh; rolling-engine re-run, sequenced after ED-SC-0004) AND by PR #81/#82 (edge-playability §7 items 1-2: registry×rendering sweep; GM-token sweep); ED-IN-0014..0016 allocated 2026-07-05: edge-playability §7 items 3/6/9 (key the silent emitters, seam-feedback convention, index the joints); ED-IN-0017 allocated 2026-07-07: unaddressed-areas comprehensive audit (this PR); ED-IN-0018 allocated 2026-07-07: Key & Echo armature program (this PR)
```


## SE — Settlements

<a id="se"></a>

*Moved verbatim from `id_reservations.yaml` line 236, 2026-08-01. 3104 chars.*

**2026-09-19 — `ED-SE-0054` allocated; `next_free` 54 → 55.** Jordan, answering ruling-batch item
3(ii) of `workplans/2026-09-18-governance-settlement-behaviour-plan.md`: **"accept"** — P1 (dearth
reaches the body), P3 (individuation is a refusal) and P4 (founding and building) of
`proposals/2026-09-10-settlements-factions-populations/` are **accepted for build**.

- **P2 is NOT in the acceptance.** The question named three; P2 (the bodies clock) is the loop
  `ED-SE-0051` bounded with hearth capacity two rulings earlier the same day.
- ⚠ **P1's carrier is in question and the acceptance does not settle it.** P1 writes
  `(Person, body)` on every eater at a rung; `ED-IN-0255` (2026-09-18) ruled subsistence
  **territorial** — *"i don't think having lords and guild members etc worry about subsistence is
  worthwhile"* — which is P1's mechanism exactly. Not escalated, because plan position `24f`
  already carries it: *"Answer the scale before picking the number."* P1's write site inherits it.
- ⚠ **Neither P3 nor P4 is buildable as it stands**, per `04_EVALUATION.md`'s own grading: P3 has
  two writes the gate refuses; P4 **refuses at load** pending three table corrections. Build
  details rather than design questions. P4 is `24e` and stays blocked on position 15.

Full row: `registers/editorial_ledger_se.jsonl`, `ED-SE-0054`.

```text
BLOCK RELEASED 2026-07-30 (ED-IN-0098, W5 capstone walk-back). Was 0049-0052 RESERVED 2026-07-29 for cross-lane EDs the IN code-shape waves file in SE. MEASURED max allocated = ED-SE-0049; unused 0050-0052 (3) returned to the pool, next_free 53 -> 50. Freeze lifted: read next_free, allocate, bump, co-commit as normal. // ED-SE-0045..0048 allocated 2026-07-13: 2026-07-13 multi-agent audit P1 batch (designs/audit/2026-07-13-multi-agent-audit/) -- 0045 Prosperity->Treasury x50 vs x10 conflict (settlement_layer SS1.3 L47 vs SS1.8 L169); 0046 Fortress-City/Cathedral-City/Village missing from SS1.2 + base(Type) weight table (W_s uncomputable for the 2 compound types); 0047 SS4.7 Black Markets modifies invalid 'Settlement Wealth'/'Settlement Accord' fields; 0048 settlement_adjacency prose stale (36 settlements/PP-723) vs PP-726-rebuilt geography YAML (37/55). All open/needs_jordan. NOTE: mechanic_audit GAP-02 (Fort Level province->settlement granularity) NOT re-filed -- already ratified + tracked under ED-SE-0006 (open, execution pending); its SS2.2 mass_battle-SSA.4 mis-citation residual folds into ED-SE-0006 execution. next_free bumped 45->49. // ED-SE-0018..0044 allocated 2026-07-09: comparative-governance-research docket round 2 (designs/audit/2026-07-09-comparative-governance-research/) — same batch as the FA-lane note above; 7 authored into governance_play_redesign_v1.md/settlement_layer_v30.md as PROPOSED (ED-SE-0018/0019/0020/0021/0022/0023/0024 — Kokudaka Survey + Encabezamiento locked-extraction substrate, Goningumi cells, Za patron-lapse, Clerk Capacity, Ordenanza Ratification, Seggio Council), rest open/needs_jordan (see registers/editorial_ledger.jsonl and registers/handoffs/HANDOFF_SE.md). next_free bumped 18->45. ED-SE-0007..0017 allocated 2026-07-08 (THIS branch, RENUMBERED +1 from this branch's original ED-SE-0006..0016 -- collided with origin/main's concurrent ED-SE-0006, the coherence-audit Fort-Level bundle below): FA/SE historical-precedent research docket (designs/audit/2026-07-08-fa-se-historical-precedent-research/) — Weberian L/PS derivation table (SE-1, highest priority), dearth chain + grain routes, charter/prescription, entry terms, succession continuity, oversight toolkit, church-state seam, marcher autonomy, Weight-as-Exit, citation-patch CP-2; several needs_jordan forks (0013,0014,0015,0017). ED-SE-0006 allocated 2026-07-08 (origin/main): attribute/value coherence audit (ED-IN-0029) — Fort Level province→settlement inheritance (default: settlement = province value) + Garrison/Local-Economy/Public-Order §9 ratify-vs-[ASSUMPTION]-mark, both OPT-AV-18; decisions ratified, execution pending. ED-SE-0005 allocated 2026-07-08: pessimist-audit SE work items — Trade/Grant prune, Sponsor merge, etc. — execution pending (decision ED-IN-0027). ED-SE-0001 allocated 2026-07-05: NERS-audit E-1 accepted work item (governance_play_redesign path); ED-SE-0002 allocated 2026-07-05: edge-playability §7 item 4 (Accord/Order stacking ruling, needs_jordan), edge-playability §7 batch (PR #81)
```

### 2026-09-17 — ED-IN-0233 / 0234 / 0235 (governance and holdings, ROUND TWO)

`next_free` 233 -> 236, then -> **238** when round one renumbered into 236/237 on the merge with `main` (see the section above). **These three ids are unchanged by that collision.** `proposals/2026-09-17-governance-and-holdings-r2/`, PROPOSED and HELD BACK IN
FULL. Round two exists because round one's own pessimistic steelman NERS pass found four defects that
were not polish: the headline emergent path **did not construct**, the downward half of its central
mechanism was **forbidden by `holonic_ARCHITECTURE.md` §37.3**, its net-deletion claim **failed against
the tree**, and one option **strictly dominated** at every issuing seat. Jordan then licensed changing
the engine rather than routing around it.

- **ED-IN-0233 — attention and reach (01), and the ledger and build order (05).** Two question sources
  instead of four-plus-one: `claim_landed` over a new `reach(w, p)` Query, plus `need`. Dates and
  crossings become claims; `date_due`, `band_crossed` and `w.crossings` are deleted and `H-110`
  *dissolves*. Carries the suite's central claim: **net −20 engine objects**, 37 removed against 17
  added, counted by name — where round one was net +17.
- **ED-IN-0234 — the writ and the word (02).** The centrepiece, answering what `ARCH F.15` files as an
  open gap. Two people-borne channels; the writ arrives verbatim or not at all; the word is lossy only
  at `Partial`; MATTER reads no policy. **`needs_jordan: true` for RR-P**, the act-inviolate principle
  as candidate `AX-7`, which would bind every subsystem.
- **ED-IN-0235 — seats and content (03).** `conferral` and `revocation` as values; the `is_title` branch
  and all four title helpers deleted; content derived from `offices_draft.yaml` rather than copied,
  because that file cannot load as written.

Full text: `registers/editorial_ledger_in.jsonl`.

### 2026-09-17 — ED-SE-0052 (the built world)

`next_free` 52 -> 53. `proposals/2026-09-17-governance-and-holdings/02_THE_BUILT_WORLD.md`, PROPOSED
and HELD BACK IN FULL.

Settlements and their buildings, infrastructure, fortifications and works as the expression of faction
holdings. A built thing's FABRIC is a `Site` and its ADDRESS is a `Rung`, which NARROWS `ED-IN-0223`'s
*"A BUILDING is a `hearth`"* rather than overturning it — a building stands on a hearth, and the hearth
is the plot. Five site families discriminated by which existing table a condition band reaches;
fortification as an ENCLOSURE `Site` whose condition IS its strength, reading onto three mechanisms
that already exist, with no siege subsystem. `hold` must NOT reach a `Site` — confirmed, on the ground
that mandatory single-holdership deletes the commons, and noting that `World.add_tenure` performs no
object-class check, so the refusal is currently unenforceable and a guard ships rather than being
asked for. Two free cuts were WITHDRAWN as breakages: `fort_level` has live engine readers behind a
blocking descriptor export, and `facility_tier` is read by its own registry.

Measured, and it reorders the work: after one season on the populated world 37 settlements hold 4,810
units of matter and **211 hearths hold none** — every site hangs from a settlement, every person lives
in a hearth, and the shortfall is clamped away. Recommends `ED-SE-0051`'s **capacity** arm as a
`capacity(w, rung)` Query over DWELLING sites with a floor, never a fixture; `ED-SE-0051` stays the
open escalation.

Full text: `registers/editorial_ledger_se.jsonl`.

### 2026-09-17 — ED-SE-0053 (matter and works, ROUND TWO)

`next_free` 53 -> 54. `proposals/2026-09-17-governance-and-holdings-r2/04_MATTER_AND_WORKS.md`,
PROPOSED and HELD BACK IN FULL; the round-two successor to `ED-SE-0052`.

Matter **stays where it is produced** and moves only by `transfer`, preserving `AX-1` because a person
moves it; eaters **draw up the ladder** through a new `nearest_store(w, rung, kind)` Query. Shortfall
crosses into `Person.body`, bodies cross `band_floors.person`, and death at 0 reuses the existing kill
cascade. Building is a `works` Record whose last stage is `restore` or `found` — and it costs little,
because `_eff_create_record` already mints the Record and opens the maker's `hold`, and MATTER's
living-holder test already stops a maturation when the maker is gone.

Carried forward from `ED-SE-0052` because each survived a pessimistic pass: the fabric/address
ontology, the five site families, fortification as an `ENCLOSURE` condition band, and `hold` not
reaching a `Site`. Also carried: that ontology's original licensing argument was **unsound** and now
rests on cardinality, and the `fort_level` / `facility_tier` cuts stay **withdrawn as breakages**.

**`ED-SE-0051` still STAYS OPEN** — the capacity arm is recommended, not adopted.

Full text: `registers/editorial_ledger_se.jsonl`.

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

### 2026-09-16 — the 0228 window took a THIRD claimant (ED-IN-0231)

The design-prose quarantine (#407) first took **ED-IN-0229**, skipping 0228 on purpose: `next_free`
read 228, but 0228 was already claimed by the then-open PR #405, and taking it would have produced
the within-lane collision CLAUDE.md §4 warns about. **It collided one number higher anyway.** While
#407 was open, #405 landed keeping 0228, and #404 landed having renumbered 0228 -> 0229 and
0229 -> 0230 — so by the time #407 merged `main`, its 0229 belonged to #404 and it renumbered again,
to **0231**, with `next_free` at 232.

That is §4's sentence demonstrated rather than quoted: *renumbering to `next_free` does not escape a
same-lane collision*, because every live session renumbers to the same number. Skipping ahead does
not escape it either — it only changes which number you land on. Three claimants on one window in
one day, after the same lane collided twice on 2026-09-10 and once more after that renumber.

What would actually have prevented it is the structural fix the reservations file already specifies
and PARKS: `wiring_status.auto_allocation`. Until that exists, the only real mitigation is the one
§4 names — land the `next_free` bump on `main` **before** anything cites the number — which narrows
the window rather than closing it, and a branch open for hours cannot use it at all.

---

## Part 2 — the remaining YAML comment narrative (B-X extraction, 2026-10-06)

*(Jordan, 2026-10-06: "you can extract all edit histories/discussion from .yaml files in references and
just make those a supplement".)* The first split (above) moved the per-lane `Narrative:` rows. This part
moves what that pass left in `id_reservations.yaml`: the header's provenance lines, the very long trailing
comment on `verified_live_max.ED` (the ED-1095/1096 collision incident), the Round-1 and lane-namespace
motivation, the 2026-07-07 duplicate-lane-key repair, and the stand-alone per-ED comment blocks that sat
between the lane rows (MB, PC, FI, SC, FA, WR, IN, SE).

**What stayed in the YAML:** the ALLOCATION PROTOCOL, the schema and `FORMAT`/`MIGRATION` notes, every
`next_free`, block and gap, the lane rows with their one-line summaries and pointers, and a one-line
summary where an editor needs the fact (the duplicate-lane-key hazard, the frozen flat-ED ceiling).
`0103-0111` stays on the IN row because `tests/valoria/test_id_reservations_walkback.py` and
`tests/valoria/test_audit_plan_ids_are_allocated.py` read it there.

The text below is VERBATIM, grouped under the YAML section it came from. Nothing was deleted.

### <a id="p2-header"></a>Header: source and the session-time verification note

*(original lines 8-10 at 8b57336, verbatim)*

```yaml
# Source: Valoria Master Workplan v2 (2026-05-31) — RESERVED ID RANGES + item 5.10.
# Live maxima VERIFIED this session (don't trust the doc blind): ED 884, PP 726 — so every
# reserved block below is clear of existing IDs.
```

### <a id="frozen-ed"></a>`verified_live_max.ED` — the freeze point and the ED-1095/1096 collision incident (the full trailing comment)

*(original lines 25-25 at 8b57336, verbatim)*

```yaml
  ED: 1096                         # FROZEN 2026-07-02 (ED-IN-0001 cutover, origin/main) — 1094 was the FINAL flat ED-NNNN value AS OF THAT CUTOVER; no new flat allocations from here on. This branch's own ED-1095/ED-1096 (T1-T4 charge-recoil ruling; movement/pathing audit ratification) were filed on the mass-battle lane BEFORE this branch learned of the cutover, using the old flat scheme, and do not collide with anything origin/main claimed (origin/main jumped straight from 1094 to ED-IN-0001/0002) — so 1095/1096 stand as valid, permanent flat IDs, just filed after the nominal freeze point. Any FURTHER new ED from this point on uses the ED-<LANE>-NNNN namespace below, not a flat number. Full incident history (three same-session collisions on this one block): registers/editorial_ledger.jsonl (max ED referenced, 2026-07-02 — origin/main's concurrent month-overview-consolidation lane independently claimed ED-1093/1094 for its own content (J-38 propagation-spec + merge-ratifies-by-default convention, itself already twice-renumbered on that lane) while this branch held ED-1093 (T1-T4 charge-recoil ruling) + ED-1094 (movement/pathing audit ratification) — this branch's two colliding IDs renumbered to ED-1095/ED-1096 before merging origin/main in, which itself had independently landed ED-1088-1092 (mass-battle LC-8 + three Jordan rulings + Stage F investigation, PRs #59/#62/#64/#65) against this branch's own now-renumbered ED-1089/1090 — two same-session collisions on origin/main's side plus this branch's own third motivated the ED-<LANE>-NNNN namespace below)
```

### Round 1 overrun note (above `reservations:`)

*(original lines 29-31 at 8b57336, verbatim)*

```yaml
# Round-1 blocks A/B/C (ED 890-999) were exhausted and overrun to ED-1042 in the unreserved
# 1000-1042 overflow — exactly the collision class this file exists to prevent. Round 2 below
# opens a fresh disjoint block starting safely above the live max (1043-1049 left as buffer).
```

### <a id="lane-namespace"></a>ED-<LANE>-NNNN namespace — the motivating collisions

*(original lines 66-76 at 8b57336, verbatim)*

```yaml
# Motivated by TWO same-session concurrent-allocation collisions on the flat ED-NNNN
# sequence above (ED-1088 collided with mass-battle LC-8, renumbered to 1090; ED-1089/
# 1090 then collided AGAIN with three more mass-battle EDs, renumbered to 1093/1094 —
# see ED-1094's ledger entry for the full incident). The A-E reservation-block scheme
# above only prevents collision through allocation DISCIPLINE (read next_free before
# allocating); two sessions in the same numeric block that both skip that step, or read
# next_free before the other commits, can still collide. A lane tag makes CROSS-LANE
# collision impossible BY CONSTRUCTION — two sessions in different lanes can never
# collide, full stop. Same-lane collisions are still possible (two sessions both doing
# mass-battle work concurrently) but are a much narrower, already-expected case, and
# the existing CollisionError-retry append-safety still applies within a lane.
```

### <a id="lane-key-repair"></a>`lane_ids`: the 2026-07-07 duplicate-lane-key repair, and the ED-IN-0012/0013 renumber

*(original lines 92-106 at 8b57336, verbatim)*

```yaml
# ⚠ 2026-07-07 REPAIR (this file previously carried DUPLICATE lane keys for FI/SC/FA/WR/IN —
# a merge artifact of the two concurrent 2026-07-05 ratification PRs (#82 edge-playability batch,
# #83 SC-audit batch) each appending its own full lane list. YAML last-key-wins made the stale
# duplicates authoritative: SC's effective next_free regressed to 2, colliding with the already-
# allocated ED-SC-0002..0010. Repaired here to ONE block per lane, next_free = the true union
# maximum, comment histories merged. SEPARATE residue, since RULED (Jordan-reserved authority
# exercised directly by Jordan, ED-306 precedent — merged ledger lines are not rewritten
# unilaterally, but Jordan himself may rule the renumber): ED-IN-0012 and ED-IN-0013 were each
# allocated TWICE in the merged ledger — once by PR #83 (SC-audit acceptance sweep: throughline-
# registry/UI refresh; rolling-engine re-run) and once by PR #81/#82 (edge-playability §7 items
# 1-2: registry×rendering sweep; GM-token sweep). ⚠ 2026-07-07 RULED + EXECUTED (armature §5.10,
# Jordan's consolidated "ratify all" pass, ED-IN-0026): the edge-playability pair is renumbered to
# fresh ED-IN-0019 (registry×rendering sweep) / ED-IN-0020 (GM-token sweep). ED-IN-0012/0013
# themselves are NOT rewritten (existing ledger lines stand) — they now unambiguously mean the
# SC-audit batch content only. Cite ED-IN-0019/0020 for edge-playability work going forward.
```

### <a id="p2-mb"></a>MB: older per-ED notes (ED-MB-0001..0007 and the OPT-13 allocation)

*(original lines 112-123 at 8b57336, verbatim)*

```yaml
    # Older MB history (moved to its own comment lines 2026-07-13 so a fresh OPEN citation on the
    # primary line above no longer inherits a "ratified"/"resolved" basis-keyword hit from these —
    # tools/validate_ed_citations.py's OPEN_AS_BASIS check is line-scoped; mirrors the PC lane's
    # existing convention below):
    # ED-MB-0001: movement/pathing audit (ED-1096) fix-plan execution + adversarial review, 2026-07-02
    # ED-MB-0002: Cannae gauge-band root-cause audit, ratified + DG-3/DG-4 ruled 2026-07-04
    # ED-MB-0003: D1-D4 defects found+fixed, DG-1/DG-3 completion + DG-2-as-workplan ruled+executed, 2026-07-05
    # ED-MB-0004: partition-invariance fix + RC-5 preliminary finding, resolved 2026-07-08
    # ED-MB-0005: DG-2 commanded-entry slice built, 2026-07-08
    # ED-MB-0006: Command abandoned for combat pool -- troop type/quality/numbers model (POOL_QUALITY_MODEL), 2026-07-08
    # ED-MB-0007: 11-surface agonist-antagonist gauge architecture audit (why 7/20), resolved 2026-07-08, opens DG-6..DG-16
    # ED-MB-0004 allocated 2026-07-07 (status open): unaddressed-areas ed_options OPT-13 (gauge triage continuation) — 2026-07-07 consolidated ruling pass, see ED-IN-0026
```

### <a id="p2-pc"></a>PC: per-ED notes ED-PC-0003..0012

*(original lines 125-192 at 8b57336, verbatim)*

```yaml
    # ED-PC-0003 + ED-PC-0004 allocated 2026-07-07 (status open): ed_options OPT-10 (sigma band-discipline unification, executes armature §5.12) + OPT-15 (ED-1042 reconciliation) — 2026-07-07 consolidated ruling pass, see ED-IN-0026
    # ED-PC-0005 allocated 2026-07-07 (status open): ED-1042 residual wound-Ob prose drift, re-filed from ED-PC-0004/OPT-15 during the Stratum-A execution PR. NOTE: a plan-text label "ED-PC-0005" in designs/audit/2026-07-04-weapon-morphology-granularity/consolidation_v1.md:115 (U4 item) is NOT an allocation and must renumber when actually filed (the ED-PC-0001 plan-label collision class). RESOLVED 2026-07-08 (Jordan ruling "never -1D, always fractional Ob").
    # ED-PC-0006 allocated 2026-07-08 (status resolved): non-combat wound fractional-Ob calibration — follow-on to the ED-PC-0005 ruling. RESOLVED 2026-07-08: adopted +0.15 Ob per wound (cumulative), reusing ED-1041's combat "attacking" magnitude, propagated to Thread ops/fieldwork/mass-battle Command + params mirrors (see ledger entry). next_free bumped 6→7.
    # ED-PC-0007 allocated 2026-07-08 (status deferred): pessimist-audit PC action-consolidation work items.
    # DEFERRED 2026-07-08 (Jordan: "Defer PC") — the audited combat_v30 §4 ACTIONS menu predates the current
    # continuous resolver combat_engine_v1/, which has no discrete player-action surface yet; the subtractive
    # consolidations are already realized/moot under combat_engine_v1's design. No edits to the stale surface.
    # Forward constraints (see ledger entry for the full list) attach to the post-R3 player-input-surface item.
    # next_free bumped 7→8.
    # ED-PC-0008 allocated 2026-07-08 (status open, needs_jordan): U2 scoping findings — attempted U2 (graded
    # mode affordance + Phase-C percussion enactment) this session and found it materially underspecified
    # relative to consolidation_v1.md's one-line description; three NEW forks surfaced (percussion self-gate
    # removal produces a severe balance regression without new grounding; thrust_factor carries its own
    # undocumented floor bug; the graded-affordance change has a much wider blast radius on exact-set tests
    # than the plan's 5 named acceptance tests). U2 NOT implemented this pass — see ledger entry for full
    # evidence. next_free bumped 8->9.
    # ED-PC-0009 allocated 2026-07-08 (status resolved): JD-4 + JD-9 DETERMINED by testing bottom-up emergent
    # primitives (mass/position/geometry, no per-weapon table) and validating top-down against HEMA sourcing +
    # physics (Jordan directive 2026-07-08). geometry.py's cut_factor/thrust_factor floor-drop fixes; a new
    # weapon_physics.reversed_grip_percussion (the grounded Mordhau/Mordschlag pommel-strike model, hands==2
    # bladed weapons only, ~1.4-1.8/8 vs mace's 8.0/poleaxe's ~7.5) replaces percussion_authority's non-blunt
    # hard-zero self-gate. Live mode-selection wiring for JD-4/JD-9 IN PROGRESS under ED-PC-0011 (below), a
    # separate later allocation — not this entry. next_free bumped 9->10.
    # ED-PC-0010 allocated 2026-07-08 (status resolved), RENUMBERED at merge time from an original ED-PC-0007
    # allocation: R3 U1 — PoB recalibration (JD-1 RULED by Jordan: "accept plan bands" — consolidation_v1.md's
    # default arms-scholarship ranges). weapons.py data-only mass redistribution (rapier/arming/longsword/
    # greatsword blade->pommel; bec_de_corbin/lucerne_hammer haft->head) for the 6 flagged weapons (V7 evidence
    # table); HEFT_REF re-anchored to longsword's recalibrated PoB; two NEW deliberately-left-failing tests
    # document a corroborating spear-dominance finding (see ledger entry). RENUMBER NOTE: this entry was
    # originally filed as ED-PC-0007 (the U1/JD-1 execution, chronologically the FIRST PC-lane ED filed this
    # session) but collided at merge with main's own independently-allocated ED-PC-0007 (pessimist-audit PC
    # action-consolidation deferral, above) — same plan-label-vs-allocation collision class as ED-PC-0001/
    # ED-PC-0005's precedent notes (this same file). Main's ED-PC-0007 was already merged to main first, so it
    # keeps the number; this entry (not yet merged) moves to the next free PC-lane slot instead. All internal
    # citations updated to match (weapons.py, weapon_physics.py, tests/valoria/test_combat_invariants.py,
    # test_combat_heft.py, test_combat_pob_bands.py, CURRENT.md, consolidation_v1.md, HANDOFF_PC.md). Note this
    # entry numerically follows ED-PC-0008/0009 despite being chronologically first — file/allocation order
    # diverge here precisely because of the merge-time renumber, exactly as this file's own header docs warn
    # ("never max+1"; read next_free, allocate, bump). next_free bumped 10->11.
    # ED-PC-0011 allocated 2026-07-08 (status: resolved): live mode-selection wiring for JD-4 (Mordhau reversed-
    # grip percussion) + JD-9 (thrust_factor floor drop), the integration ED-PC-0009 explicitly deferred as a
    # real architectural gap. core.py: FIX-1b's percussion-authority transmit scaling extended from
    # `mat in ('mail','plate')` to every material, with a dual-reference split (PERC_AUTH_REF=8.0 unchanged for
    # mail/plate, PERC_AUTH_REF_SOFT=6.5 for none/cloth) found necessary by an adversarial review of a first
    # attempt that collapsed both onto one reference and silently regressed poleaxe/bec_de_corbin/
    # lucerne_hammer. systems.py: the three graded secondary-affordance checks (percussion/cut/point)
    # re-enabled in element_afforded via dict.setdefault. Also fixes the related gap: core.coupling's
    # DELIVERY['cut'] now scales by the candidate's own derived cut magnitude via CUT_AUTH_REF=0.70 (anchored
    # on the weakest attested native cutter, hook_sword) — an incidental secondary 'cut' token (e.g. rapier)
    # no longer outscores a weapon's own dedicated 'point' regardless of how weak the incidental edge is.
    # Validated via a 13-agent agonist/antagonist adversarial Workflow (6 Sonnet producer/critic weapon-group
    # pairs + 1 Opus synthesis) against HEMA/physics grounding across the full roster. NOTE: this ID was
    # drafted into in-progress code comments (core.py, systems.py) BEFORE the ED-PC-0007 merge collision above
    # was discovered and U1 was renumbered to claim ED-PC-0010 first — comments originally said "ED-PC-0010"
    # and were corrected to ED-PC-0011 to avoid a second collision on the same slot. next_free bumped 11->12.
    # ED-PC-0012 allocated 2026-07-08 (status: open): a SECOND, structurally identical gap to the one ED-PC-0011
    # fixed for 'cut', found by the same adversarial Workflow, this time on 'point' — DELIVERY['point']=1.45 is
    # NOT scaled by the candidate's own derived thrust magnitude, and the puncture transmit path is floor-
    # locked (verified: scimitar/sabre/falchion/hook_sword's secondary point ALL score the identical coupling
    # at 'light' armour regardless of their wildly different point geometry, 0.16-0.40). Judged by the
    # adversarial pass to matter concretely for the one-handed sabre-class roster (sabre/scimitar/falchion —
    # FLAG-AS-FORK, their historically-attested pure-slashing identity makes this switch a floor-locked
    # artifact, not earned capability) but NOT for the two-handed cutter roster (their switches are historically
    # defensible regardless). Deliberately NOT implemented this pass — a THRUST_AUTH_REF fix analogous to
    # CUT_AUTH_REF would also touch several two-handed cutters (tachi/nandao/glaive/podao, whose own point sits
    # below the proposed reference too) and needs its own roster-wide re-verification before landing, not a
    # third redesign-and-reverify cycle rushed through in the same session. See ledger entry for the full
    # recommendation. next_free bumped 12->13.
```

### <a id="p2-fi"></a>FI: ED-FI-0003

*(original lines 194-194 at 8b57336, verbatim)*

```yaml
    # ED-FI-0003 allocated 2026-07-07 (status open): ed_options OPT-6 (knots propagation completion) — 2026-07-07 consolidated ruling pass, see ED-IN-0026
```

### <a id="p2-sc"></a>SC: per-ED notes ED-SC-0011, 0017..0024, 0033..0038

*(original lines 196-222 at 8b57336, verbatim)*

```yaml
    # ED-SC-0038 allocated 2026-09-26 (status ruled, NOT needs_jordan): two of Jordan's 2026-09-04
    # rulings (multi-matter/conditional adjudication; binding-in-scene), relayed only inside the
    # scope-banned 09-04-social-contest-branches corpus, apply to all twelve proceeding rows in the
    # 09-05-proceedings-subsystem successor, not just negotiation. Reopens 19_PLAN.md PART I item 1
    # and P-14/D-8 for a build session. next_free 38 -> 39.
    # ED-SC-0037 allocated 2026-09-09 (status open, NEEDS_JORDAN): which provider resolves a
    # social contest until proceedings lands -- interim dice now vs. wait. The one call in the
    # R-execution plan that survived all five of CLAUDE.md section 0's tests. next_free 37 -> 38.
    # ED-SC-0036 allocated 2026-09-07 (status open, NOT needs_jordan): the stress suite run against
    # the proceedings subsystem -- 38 executable tests, 23 inventions, 8 mechanical decisions, 35
    # findings of which 15 new; two independent read-only critics killed two of them, overturned a
    # third as stale and voided one execution, all applied in place. next_free 36 -> 37.
    # ED-SC-0033..0035 allocated 2026-09-06 (all status ruled, none needs_jordan): the proceedings
    # subsystem rulings -- 0033 ownership of all social contests + retirement of the orphaned tree;
    # 0034 resolution (aggregates licensed, multilateral + debate score accepted, latitude pool-only
    # with a floor, M-7/M-8 blocking); 0035 the character model (fears pressed not spent, the break
    # lands on the feared thing, pressure is the gap, second-person lever refused). next_free 33->36.
    # ED-SC-0023..0024 allocated 2026-08-06 (both open, both needs_jordan): the precedent-grounded
    # consolidation/integration programme CIP-0..CIP-10 (proposals/social_contest_consolidation_integration_v1.md)
    # + the CIP-9b amendment to the RATIFIED Auto/Manual Duality parity constraint. next_free 23->25.
    # ED-SC-0017..0022 allocated 2026-08-06 (all status open; 0017/0019/0020/0021 needs_jordan):
    # three-lens pessimistic NERS audit + upload delta (audit/2026-08-06-social-contest-three-lens-audit/).
    # 0017 spec/kernel divergence + KU-1 sharpening + params-provenance break; 0018 CR4 reachability
    # (Projection half); 0019 no record spine / compose on settlements LedgerTag + M2 Scope; 0020 FORK A
    # burden-parameterized gate; 0021 FORK B anti-collapse device; 0022 live bug batch (8 defects).
    # next_free bumped 17->23.
    # ED-SC-0011 allocated 2026-07-07 (status open): ed_options OPT-11 (contest live-dispatch acceptance criterion) — 2026-07-07 consolidated ruling pass, see ED-IN-0026
```

### <a id="p2-fa"></a>FA: ED-FA-0004 / 0005

*(original lines 224-224 at 8b57336, verbatim)*

```yaml
    # ED-FA-0004 + ED-FA-0005 allocated 2026-07-07 (status open): ed_options OPT-1 (faction-oracle reconciliation, banner-now sequencing ruled) + OPT-2 (elimination-lockout, no-permanent-lockout ruled) — 2026-07-07 consolidated ruling pass, see ED-IN-0026
```

### <a id="p2-wr"></a>WR: ED-WR-0004 / 0005 / 0006

*(original lines 226-226 at 8b57336, verbatim)*

```yaml
    # ED-WR-0004/0005/0006 allocated 2026-07-07 (status open): ed_options OPT-4 (Turmoil victory-gate, wire-the-clock ruled) / OPT-5 (threadwork execution reconciliation) / OPT-12 (NPC orphan triage ED) — 2026-07-07 consolidated ruling pass, see ED-IN-0026
```

### <a id="p2-in-a"></a>IN: the duplicate-`IN:`-key collapse (ED-IN-0068) and the ED-IN-0068..0072 / 0280-0281 notes above the IN row

*(original lines 227-255 at 8b57336, verbatim)*

```yaml
    # IN lane (Infrastructure / cross-cutting). 4 duplicate IN: keys collapsed -> 1
    # (2026-07-15, ED-IN-0068): the recurring 2026-07-07 duplicate-IN class — YAML
    # last-key-wins hazard. All four agreed on next_free:68; per-ED allocation history is
    # preserved in registers/editorial_ledger_in.jsonl (prior: ED-IN-0062/0064/0066/0067) and
    # the comment block below. ED-IN-0068 allocated 2026-07-15 (apparatus consolidation:
    # shared observability core + build_proposals generator + apparatus registry).
    # ED-IN-0069/0070 allocated 2026-07-15 (proposal-reconciliation pass,
    # designs/audit/2026-07-15-proposal-reconciliation/): 0069 = reconciliation-pass umbrella
    # (census + Nature-A flips + A2 reclassify + Nature-D status-lines + Nature-C dispositions
    # + reconciliation map + broken-path fix; open, needs_jordan); 0070 =
    # governance_cluster_reconciliation_v1.md unified governance-play head (PROPOSED, open, needs_jordan).
    # RENUMBERED from ED-IN-0068/0069 at merge — collision with PR #146's ED-IN-0068 (merged first
    # keeps the number; same class as ED-IN-0031/0044/0064 precedents). next_free 69->71.
    # ED-IN-0071 allocated 2026-07-15 (repository reorganization proposal,
    # proposals/repo-reorganization-v1.md): content-class taxonomy critique + resolved
    # target buckets + phased P0-P5 migration plan; PROPOSED, needs_jordan, all forks HELD-BACK.
    # Captures Jordan's previously-untracked repo-reorg suggestion (found nowhere in the corpus).
    # next_free 71->72.
    # ED-IN-0072 allocated 2026-07-16 (RENUMBERED from this branch's original ED-IN-0071 --
    # COLLISION: origin/main PR #150 concurrently claimed ED-IN-0071 for the repo-reorg proposal
    # above and merged first; same class as the ED-IN-0044/0064 precedents, later-merging side
    # renumbers): register-honesty fix to tools/observability/build_proposals.py --
    # obs_core.text_needs_jordan() rescues design-doc + flat-ledger Jordan-gating (register
    # needs_jordan 79->97). status resolved, no ruling needed. next_free 72->73.
    # [ED-IN-0280/0281 COLLISION, 2026-09-28] Two concurrent sessions both read next_free 280 and
    # both allocated ED-IN-0280 -- same class as ED-IN-0072/ED-IN-0209-0211's precedent above and
    # below. origin/main's PR #437 (the `methodology` skill) merged first and keeps ED-IN-0280;
    # this branch's PR #438 renumbers its own allocation to ED-IN-0281 (THE PLAN re-adopted as the
    # single order). Neither commit's content changes, only the number.
```

### <a id="p2-in-b"></a>IN: the 2026-07-07 note and ED-IN-0028 below the IN row

*(original lines 258-265 at 8b57336, verbatim)*

```yaml
    # 2026-07-07 (status open unless noted): ED-IN-0012/0013's edge-playability pair RENUMBERED to
    # ED-IN-0019/0020 (armature §5.10 decided + executed, see repair note above); ED-IN-0021..0025
    # allocated: ed_options OPT-3/7/8/14/17 (F7 smoke oracle / registry hygiene / consumer-closure /
    # intent-hygiene addenda / C-VERIFY carry-forward); ED-IN-0026 (status: the consolidated
    # ruling-pass record itself) allocated. ED-IN-0017/0018 status flipped in the ledger this same
    # pass (see their own ledger entries) — not repeated here to avoid a stray basis-keyword tainting
    # this comment's open-ED citations.
    # ED-IN-0028 allocated 2026-07-08 (status resolved — plumbing complete, downstream deferred): Key & Echo Armature PR-2a — deterministic echo-transport plumbing (ECHO_TRANSPORT flag, default OFF/byte-exact) un-orphaning domain_echo.py + the campaign's first substrate KeyLog. next_free bumped 28->29. Downstream owned by FA-comeback (ED-FA-0005) + SC context-derivation bridge (ED-SC-0006/0007).
```

### <a id="p2-se"></a>SE: ED-SE-0003 / 0004

*(original lines 268-268 at 8b57336, verbatim)*

```yaml
    # ED-SE-0003 + ED-SE-0004 allocated 2026-07-07 (status open): ed_options OPT-9 (armature keying wave) + OPT-16 (execute ED-SE-0001's own updates) — 2026-07-07 consolidated ruling pass, see ED-IN-0026
```
