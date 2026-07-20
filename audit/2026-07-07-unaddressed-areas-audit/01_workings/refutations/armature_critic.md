# Armature critic record (independent relay, Opus)

_Archived verbatim from the agent's final message (2026-07-07)._

# Armature critic record

Scope note (relay discipline): I verified every claim the armature makes about PRIMARY canon (`propagation_spec_v1`, `key_substrate_v30`, `key_type_registry_v30`, `scale_transitions_v30`, `module_contracts.yaml`) and about the new code (`sim/substrate/keys.py`, `tests/valoria/test_key_substrate.py`). Claims cited only to audit clusters (C-KEY-*, C-INJ-*, EP-*, etc.) I take as given — I was barred from the dossiers. Where a finding depends on an audit-only fact I say so.

## Contradictions found (row · canon cite · severity)

**C1 — Substrate defaults invert a ratified binding instruction (MODERATE).**
`propagation_spec_v1.md` "Relationship to other canonical surfaces" states, verbatim: *"until ratified, treat §4.1 step 4/5 in `key_substrate_v30.md` as authoritative and this document's amendments [OF-7, OF-B1] as pending."* The substrate ships both amendments **ON by default** — `no_sync_reentry: bool = True` and `defer_apply: bool = True` (`keys.py:382-383`) — and armature §2.6 calls A1 ECHO-DEFERRAL + B1 "runtime invariants." So the oracle's out-of-the-box behavior is the *pending* semantics: a legal-as-written O(1) synchronous consumer emit (key_substrate §4.1 step 5 permits "O(1) or async") **raises `TerminationBreach`** under the default, and step-4 live application is suppressed. For a document that claims to "BIND and never fork" the transport canon, and for the artifact the GDScript port is built from, defaulting the oracle to the non-authoritative model is a real tension with the ratified instruction. Not fatal (flag-gated, disclosed [PROVISIONAL], reversible), and the fork itself is already docketed at 5.3/5.4 — but the **defaults** should be the authoritative-as-written behavior (flags default OFF, opt-in to the proposal), or §6.1 must loudly state the oracle intentionally leads canon. This does not need a new docket row; it needs a default-flip or disclosure fix.

**C2 — §2.6 overclaims substrate coverage of Theorem A / A2 SLATE-FREEZE / O.1 (LOW-MODERATE).**
§2.6 says "O.1 phase order · … Theorem A/B termination discipline · A1 ECHO-DEFERRAL + A2 SLATE-FREEZE. The substrate (§6.1) implements these as runtime invariants." The substrate has **no slate and no season composition** — `keys.py` contains no scene_slate, no `run_scene_phase`, no per-tick fixpoint. §6.1 itself is correctly scoped ("No campaign-loop wiring in this PR"; it lists only ORD-1/2, Theorem-B, B1, OF-7, fan-out). So §2.6 contradicts §6.1: A2/Theorem-A/O.1 are **not** implemented and cannot be (they are PR-2 wiring, propagation_spec §4.1's `run_tick`). Fix by rewording §2.6 to the actual implemented subset.

**C3 — §1 `timing` obligation states OF-7 flat, without the provisional caveat its own §2.1/§5.3 carry (LOW).**
The §1 row format makes "echo Keys log LIVE at scene end, settlement effects land at ACCOUNTING_BOUNDARY … (AU-3.2/OF-7)" a required, A12-checked field on **every** seam row. OF-7 is a PROPOSED amendment (docket 5.3). §2.1's rows and §5.3 mark it provisional/reversible; §1 does not. A reader of §1 alone treats a pending timing rule as ratified obligation. Add the inline "(assumes OF-7; reversible)" marker.

No contradiction on the two the charter flagged as suspects: **§2.1 cap/timing vs scale_transitions §5 is CONSISTENT** — 1/scene/faction (PP-329) = §5.1; ±2/±1/0/−1 = §5.2; "deferred (PP-109)" is correct for the Hybrid/always-strategic videogame path (§4.1/§4.2 "queue to Accounting" + AU-3 log-live/apply-late), not a contradiction of §5.3's Full-TTRPG-immediate row. **§2.6 ordering vs propagation_spec §1/§4 is otherwise faithful** (ORD-1/2, SSI-1..4, cascade_depth-scheduler-internal, Theorem B, ORD-3/4 deferred). Refutation attempts here failed; the rows stand.

## Docket deltas (missing forks / non-forks)

**Missing (canon-open flags the armature relies on but omits from §5):**
- **OF-6 (settlement addressability as `targets[].actor_id`)** and **OF-1 (per-stat settlement-locus basis)** — propagation_spec §2 open flags. The entire §2.1 Accord/settlement-locus channel and the §3 settlement Key types (`state.settlement_revolt` targets a settlement, etc.) **assume** both. propagation_spec triaged them "smaller, non-blocking" (its §5 item 8), so this is "should surface / cross-reference," not a hard miss — but a settlement-targeting Echo Matrix that never names OF-6 in its own docket is under-disclosed.
- **OF-OWN (engine_clock owns the scheduler; assumes ED-1051)** — §6.1 lands an "engine_clock-shaped" `TickScheduler` while engine_clock's home doc is `doc: null` and ED-1051 is Jordan-pending (`module_contracts.yaml:700-702`). Not surfaced in §5. Low-moderate.
- **OF-HYSTERESIS-AUDIT** — §2.6 lists it as "(docket)", but propagation_spec §4.3/§5 item 4 explicitly rules it a *hygiene item, not a Jordan ruling*. §2.6 mis-elevates it; either drop the "docket" framing or route it to §6.3 wave 5. Cosmetic.

**Non-forks / correctly excluded:** the "Ruled-but-unexecuted are NOT forks" carve-out (ED-871, fork-2, fork-11 contract refresh, ED-935 edges) is sound. No §5 row is spuriously a fork — I spot-checked the contestable ones: **5.9 (Accord no-stack §5.5 vs strain §2.7 stack)** is a genuine cross-doc contradiction (§5.5 rules no-stack only against Govern actions, leaving the strain-stack conflict open); **5.11 (CI 75-vs-80)** is a genuine ci_political §2.1 vs conviction_track §11.3 numeric conflict; **5.13** maps to real ledger fork **ED-SC-0004** (open, needs_jordan=true). **5.10 verified REAL against the working tree** (see below).

## Substrate fidelity check

Faithful, with the two caveats above (C1 defaults, C2 §2.6 overclaim). Verified against `keys.py`:
- **§2.3 invariants 1-8 enforced at append** (`_validate`, lines 295-351). Invariant 4 (cycle-freedom) correctly proven by construction (append-only + causes-must-be-already-logged subsumes the §4.6 BFS); invariant 5 sensibly reduced to season-non-regression + append-monotonic sub_step. Both simplifications are disclosed and sound.
- **SSI-4 honored:** `cascade_depth` is **never** a Key field — it lives only as scheduler `_current_depth` / queue tuples (`keys.py:393, 424, 430, 440`). The `Key` dataclass (120-136) has no such field. ✓
- **OF-7/OF-B1 defaults ON** as §5.3/5.4 claim (`382-383`). ✓ (but see C1).
- **OF-CAP clean:** `cascade_depth_max`/`emissions_per_tick_max` are **required** keyword args, no default (`379-380`); tests pass arbitrary values labeled "OF-CAP is an open fork." No fabricated cap constant entered.
- **No fabricated constant anywhere:** the only literals are the canonical enums (`AXES/ROLES/SCALES/PERMANENCE/TIME_HORIZON`, all from key_substrate §2.1/§2.2/§2.5) and structural arithmetic (+1, sentinel −1). §4.1 step-7 awareness `+0.1` is correctly **not** implemented (step 7 out of scope). ✓ No RNG dependency (no `import random` in the substrate; only the test file seeds its own data). ✓
- **Registry is the single source of truth:** `TypeRegistry.load` parses `key_type_registry_v30.md` at load; the 44/48 roster is not duplicated in code. I independently counted the file: **48 physical `###` headings, §9 declares 44** — the drift the armature calls "KNOWN, A9-tracked" is real and correctly handled (loader asserts `>=44`).
- **24 tests confirmed** (I counted the functions; §6.1's "24 cases" is accurate), including byte-identical replay + hash inequality across seeds (R-F2 surface) and fan-out-width-≠-depth.

## Registry-delta check (§3)

Sound at the family level; **no name collisions** with the 48 existing types; roles mostly distinct. Concerns:
- **Underspecified (acceptable for a candidate list, but flag):** candidates carry only `type`+family+emitter+finding_basis, not the §1 template (`required_payload_fields`, `default_scale_signature/permanence/time_horizon`, `consuming_systems`). §10 step 3 requires emitting **and consuming** systems; filing will need the full template. The armature is honest they are pre-vetting candidates, so this is a "note," not a defect.
- **Three latent double-emission boundaries to resolve at filing:** (1) `mechanical.settlement_captured` (g_def0 auto-capture) overlaps `scene.battle_concluded.payload.territorial_outcome` (control_change) — must scope to the non-battle path. (2) `mechanical.ci_milestone_crossed` at 100 and `mechanical.theocracy_unification_declared` (CI=100) both fire at the same boundary — intended cause-pair or double-count? Unstated. (3) `state.legitimacy_drift` keys routine per-settlement mean-reversion — potentially very high log volume interacting with `EMISSIONS_PER_TICK_MAX`; "needs a new gate entry" means it isn't even gated yet.
- `meta.cascade_cluster_event` retroactive registration is legitimate and does **not** collide with existing `mechanical.cascade_resolution` (different family, different concept). The "articulation §3.1 #9 cites an unregistered type" premise is audit-sourced (C-KEY-8); I could not re-verify against articulation_layer_v30 (not in my primary set) — take as given.

## Enforceability check (A13-A16)

None of the four are implementable by the existing `contract_adjudicator.py` (which reads only contracts YAML + registry MD + sources text) from the spec text alone:
- **A13 (emit-clause coverage):** the "type_id appears in the `doc:` head" half is mechanically checkable **if** the adjudicator gains per-doc file access; but "**and its trigger condition**" is NL-semantic, not decidable by string match. Also needs a **new schema field `doc_emit_ref:`** (the npc_behavior/doc-12 case) that does not exist in schema-2. Implementable only in a weak form.
- **A14 (down-Key targets[] lint):** the **runtime** half ("sub-scale in scale_signature + empty targets[] = warning") is clean and implementable **but is not in `keys.py` yet**, and needs "spans scales" defined (naive form would fire on every `mechanical.season_change`/`meta.miraculous_event`). The **static** half ("must document its population rule") is not mechanically decidable.
- **A15 (registry × rendering completeness):** **not implementable as specified.** §2.5 adopts the disposition table "by reference" to audit prose (`01_workings/cluster_C-KEY.md`). No machine-readable type→verdict datafile exists in the canon surface. A checker cannot parse a by-reference prose sweep. This is the weakest of the four — it presupposes an artifact that must first be produced.
- **A16 (FEEDBACK presence):** implementable as a markdown-column-presence lint, but **not by `contract_adjudicator`** (wrong input surface — it reads `module_contracts.yaml`, not the armature's prose §2.x tables). ED-IN-0015 itself scopes this to "the co-file checker pattern," a different tool. The seam rows must live somewhere checkable first.

The armature says A13-A16 are "implemented PR-3, report-only" so it does not claim readiness — but as written, the spec must additionally (a) ship a structured rendering-disposition datafile for A15, (b) reduce A13's "trigger condition" and A14's "must document" to mechanical predicates, (c) add `doc_emit_ref` to schema-2, and (d) name the correct tool/surface for A16.

## Overreach check

Mostly clean — §7 correctly states "rules no fork; edits no ratified text," and §5.10 correctly **holds back** the ledger renumber as Jordan-reserved (ED-306 precedent). Two watch-items:
- **§2.2 scenario_authoring row asserts "Fork 11 ruled compile=authoring-time" as ratified.** I could not verify this ruling against the primary canon set (it's an injector fork, cited only to audit C-INJ-4). If Fork 11 was **not** actually ruled, this row asserts a ruling not in evidence and must move to §5. Flag for author/Jordan confirmation.
- **A15 proposes to extend the registry §10 Extension Process** ("No new type may be registered without [a disposition row]") — a mandatory precondition added to a CANONICAL doc's process, bundled as a conformance check. It should be explicitly flagged as a process-canon change needing ratification, not slipped in as an adjudicator rule.
- **C1 (substrate defaulting to pending semantics)** is the closest thing to overreach-by-implementation: shipping the oracle with OF-7/OF-B1 as the default subtly pre-biases their eventual ruling. Disclosed and flag-gated, so not overreach, but see the C1 remedy.

## Verdict: rows that must change / move to docket

1. **Substrate default flags (C1):** flip `no_sync_reentry`/`defer_apply` defaults to the authoritative-as-written behavior (OFF), or add a loud §6.1 disclosure that the oracle's defaults intentionally encode the *pending* OF-7/OF-B1 amendments and diverge from currently-authoritative key_substrate §4.1. Reason: propagation_spec's ratified instruction says treat the unamended §4.1 step 4/5 as authoritative until ratification; the oracle currently defaults to the opposite. No new docket row (fork is at 5.3/5.4) — fix the defaults/disclosure.
2. **§2.6 wording (C2):** narrow "the substrate implements these as runtime invariants" to the actually-implemented subset (ORD-1/2, SSI, Theorem-B, A1-deferred-apply, B1). Remove the claim that A2 SLATE-FREEZE / Theorem A / O.1 are in the substrate — they are PR-2 wiring. Reason: contradicts §6.1's own scope.
3. **§1 timing field (C3):** mark the deferred-apply obligation "(assumes OF-7; provisional/reversible)" inline. Reason: it states a pending amendment as flat obligation.
4. **Docket completeness:** add or cross-reference **OF-6, OF-1, OF-OWN** as low-priority §5 rows (or cite propagation_spec's triage); drop the "docket" framing on OF-HYSTERESIS-AUDIT (canon rules it a hygiene item).
5. **§2.2 scenario_authoring row:** verify Fork 11 was actually ruled compile=authoring-time; if not, move to §5.
6. **A15 (and A13/A14/A16) enforceability:** commit the spec to producing a machine-readable rendering-disposition datafile (A15), a `doc_emit_ref` schema field + mechanical predicate for A13, a sharpened "spans scales" runtime rule for A14, and the correct tool/surface for A16 — otherwise "checkable" is aspirational.
7. **Citation hygiene (verified):** the ledger genuinely contains **two `ED-IN-0012` and two `ED-IN-0013` entries** (`editorial_ledger.jsonl` lines 597/599 and 598/600) — the armature's §5.10 double-allocation fork is **real and confirmed**. But the armature then cites bare "ED-IN-0012" repeatedly (§2.5, §3, §6.3) for the registry-rendering-sweep sense while that ID is ambiguous by its own finding. Disambiguate to the specific ledger entry pending the 5.10 renumber.

Net: the substrate is a faithful, fabrication-free, well-tested implementation and the fork docket is substantially complete and honest (5.10 verified real). The load-bearing corrections are the **default-flag inversion (C1)** and the **§2.6/§1 provisional-vs-ratified overstatements (C2/C3)**; the enforceability layer (esp. **A15**) is not yet checkable as specified.
