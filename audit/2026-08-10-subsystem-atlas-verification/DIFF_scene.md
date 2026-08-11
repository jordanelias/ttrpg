# DIFF — shipped flow skeletons vs. blind re-derivation (Derivation 2)

Scope: `combat`, `characters`, `social_contest`, `mass_battle`, `threadwork`, `fieldwork`.
Sources: `systems/<x>/<x>_flow_skeleton_v1.md` (D1) vs `trace2/{code_scene,code_personal,code_world,vector_audit}.md` (D2).
All CONTRADICTED items adjudicated by me directly against the working tree (grep/Read permitted for the adjudicator).

## 0. Bucket counts

| Subsystem | CONFIRMED | MISSED | CONTRADICTED | SKELETON-ONLY | STALE-SOURCE |
|---|---|---|---|---|---|
| combat | ~30 | 3 | 0 | 6 (all supported) | 0 |
| characters | ~8 | 2 | 0 | 7 (all supported) | 0 |
| social_contest | ~20 | 6 | 0 | 10 (all supported) | 0 |
| mass_battle | ~25 | 4 | 0 | 8 (all supported) | 1 |
| threadwork | ~15 | 2 | 1 | 8 (all supported) | 0 |
| fieldwork | ~12 | 1 | 0 | 6 (all supported) | 0 |

Independent rediscovery is high. Every *control-flow spine* claim in all six skeletons was
independently re-derived by D2 reading the same files whole, with no ordering disagreement anywhere.
The misses cluster in one class: **declared-but-inert surfaces the skeletons walked past because the
code narrates its own defect in a comment rather than in a call graph.**

---

## 1. CONFIRMED (summary, not enumerated)

**combat.** Both derivations independently produce the identical `fight` → `engagement` → beat-loop
spine: `prev_closed` threaded as an argument from the previous engagement's return; coin-flip `first`;
`UPSET_FLOOR` applied strictly after in-model resolution; no automatic tiebreak (`result` stays 0);
grip/lunge reset **before** `reach_base`; probabilistic close-latch replacing the old hard cliff;
the re-presentation gate's three-way precondition; the independent per-fighter cadence-phase draw;
decay-then-drift ordering on initiative; two `er` refreshes (pre- and post-halfsword-swap);
`reopen_moment` created in one beat and consumed at the top of the next; proactive-disengage
clean-break vs. pursued-Nachreisen (the pursued branch falls through, no `continue`); stop-thrust →
`recoil` → `approach_step`; `read_contest` selecting `mode` as an **input** to `defence_sigma` (both
derivations state the direction explicitly and agree); the outcome map on `deg × mode`; counter-attempt;
three reopen precondition sites; the single post-riposte contact-axis insertion point; three
termination checks in order; beat exhaustion. **Both independently establish that the combat engine
never touches the Key substrate** — D1 by grep, D2 by reading `sigma_leverage`'s own dependency
contract — and that the `personal_combat` contract's declared `emits:` is therefore false.
**Item 3 of the brief is CONFIRMED, not missed:** D1 records the same-beat approach→closed-exchange
fall-through explicitly and at higher resolution than D2, as S2.7.5a/S2.7.5b, naming the nested
`if not closed:` guard as the mechanism (`wrapper.py:228`).

**characters.** Entry-point set, the beliefs→conviction late-import cycle-break, `companion.run_companion_scene`
as a hard stub, and the complete disconnection of `characters/sim` from personal combat.

**social_contest.** `Bout.resolve`'s loop order (budget → both sides move → fault check after *each*
move → `win.resolve(closing=False)` after the exchange → forced `closing=True` at budget exhaustion) is
byte-for-byte agreed. Both derive: `parliamentary_vote` shares no call path with the Agôn kernel;
the four `PERSUASION_*` constants come via the deprecated `contest_legacy_stub` re-export;
`resistance` is metadata-only (D1 additionally proves it independently of the module's self-report);
the `consensus`/`negotiation`/`inquiry` GAMES rows are stubs; `agon_harness` has zero callers.

**mass_battle.** The full per-tick phase order in **both** trees, agreed step for step, and the
phase-boundary hook order `stamina → discipline → morale → rout → rally → reform → threadwork`.
**Item 6 of the brief is CONFIRMED, not missed:** D1's two-tree comparison already records
`check_orders` (S2.6), the escort/centroid pass (S2.7), `resolve_toi_and_commit` (S2.9, "no TREE A
counterpart"), per-subunit stamina (S2.12), subunit rout floor + `derive_rout` (S2.17), `reform_check`
implemented-and-flag-gated in B only (S2.18.2), and — in a dedicated §7 gap row — that TREE B
**removed** TREE A's per-tick morale erosion leaving only the `command <= 0` instant path. D1 also
carries the `massbattle ↔ units` cycle (§7), matching vector-audit Cycle 1 exactly.

**threadwork / fieldwork.** Both derive the same near-total production unreachability; the one live
cross-subsystem edge (`knots.apply_coherence_delta`); `sustain_knot` reachable only from the orphaned
`opposing.resolve_opposing_operations`; `rendering.py` stub-wired; `collective.py`'s
`lattice_fractured` computed twice with the first result discarded; `BREADTH_OB`/`DISTANCE_OB`/
`DEPTH_TS_MINIMUM` declared and never read (D1 records all three; D2 records the same set).

---

## 2. MISSED — Derivation 2 establishes something structural the skeleton does not record

### M1. `social_contest`: **no import cycle is recorded at all** — and there are two true answers. [HIGH]
The skeleton has no cycle row anywhere. Both D2 claims are correct at different levels; I verified both.

*Adjudication.* Module-scope-only edges among `contest/` submodules are acyclic. D2's code reader is
right that `dictionaries.py:45` imports `modes` at module scope while `modes.proceeding_venue`
(`modes.py:554`) imports `panel_win_condition` **inside the function body**, with the file's own
comment naming the break. The vector audit's 9-node ring is *also* real: I re-ran Tarjan on
`audit/2026-08-06-vector-audit/structure_audit/data/g_code.json` and it returns exactly
`{contest, appraise, armature, dictionaries, faction, modes, resolver, rhetoric, wrapper}` — 9 nodes,
the audit's list verbatim. It arises because the analyzer (a) resolves `from . import X` to an edge on
the **package `__init__`** (`dictionaries.py:45`, `wrapper.py:265/274/275`), which `__init__.py:53-99`
imports back, and (b) collects **function-scope** imports as graph edges (`resolver.py:380 → rhetoric`,
`modes.py:554 → dictionaries`). Both are defensible static-analysis choices; neither ring deadlocks at
runtime. Verdict: **both derivations right, skeleton silent.** The skeleton should carry a row saying
the kernel is a 9-node SCC in the corpus import graph, that the SCC is an artifact of package-relative
+ function-scope edges, and that the one *runtime-load-bearing* break is `modes.py:554`'s lazy import.
Two further facts the skeleton also lacks: `wrapper.py`'s own comment calls its `from . import
dictionaries` "lazy" when it is module-scope-but-textually-late (loose, not deferred); and
`resolver.py:380`'s `from .rhetoric import ...` is genuinely function-scoped.

### M2. `social_contest`: `faction.coalition_vote` is a fourth resolution path that **does** reuse kernel primitives. [HIGH]
D2 says four coexisting paths; the skeleton lists the legacy stub as an entry point and notes
`faction.py:46/102` builds `Bout` directly, so it is not "claiming two" — but it never records that
`faction.coalition_vote` resolves **without a `Bout` at all**.

*Adjudication: D2 is right.* `faction.py:134` function-scope-imports `ContestState, roll_net`, then
`faction.py:143-146` does `s.adv[A] = max(0, roll_net(...))` per side and reads the band via
`PersuasionTrack(scale=..., start=...).resolve(s, closing=True)` — the kernel's own win-condition and
roll primitive, driven by a hand-built `ContestState`, bypassing `Bout.resolve`'s exchange loop, faults,
stasis and policies entirely. **This does NOT break the skeleton's "shares no call path" row**, which is
scoped to `parliamentary_vote` and is correct. It does mean the subsystem has four resolvers
(`Bout`, `run_parliamentary_vote`, `contest_legacy_stub.run_contest`, `faction.coalition_vote`), of which
the fourth shares *primitives* but not the *loop* — a distinction the skeleton's own §6 taxonomy
(import edge vs. call edge) has no cell for.

### M3. `social_contest`: `Standing.strip(deg)` is defined and never called. [MED]
*Adjudication: D2 is right.* `primitives.py:35` defines `strip(deg)`; every strip site uses
`strip_points` (`resolver.py:418`, `rhetoric.py`). The kernel says so about itself in two places —
`primitives.py:83` ("`Standing.strip()` is NEVER called in the contest kernel") and `wrapper.py:305`
("what is NOT wired is the STRIP/STRAIN half"). A dead method on the core Standing/Face primitive,
self-declared, absent from the skeleton's §7.

### M4. `social_contest`: the Orientation/Doubt-Marker channel is design-only, and `derive_interaction` is dead in resolution. [MED]
*Adjudication: D2 is right on both.* `resolver.py` never reads a `Move`'s Orientation — the only
"orientation" hits are two prose comments (`resolver.py:273`, `:365`); the ~100-line
`dictionaries.DOUBT_MARKER` block self-states that "the resolver does NOT yet consume orientation".
`derive_interaction`/`INTERACTIONS_TABLE` are called only from `agon_harness.py:463`, for a flavour
line, with the harness's own comment (`:458-462`) stating they are not consumed by live resolution.
Also unrecorded: `panel_win_condition`'s `'unanimity_required'` branch returns `stub_resolve`, and
`modes.DyadicMode`/`NegotiationMode`/`CeremonialMode.play()` are all unconditional stubs (the skeleton
records the GAMES stub rows but not these three Mode classes).

### M5. `combat`: the bind inner loop mutates the **same** `beats` counter the outer budget checks. [HIGH]
The skeleton says "up to 3 extra sub-beats of bind resolution" (S2.7.18) — which hints at it but never
states that those sub-beats are drawn from the engagement's own 24-beat budget.

*Adjudication: D2 is right, and it is load-bearing.* `wrapper.py:111` `beats=0 … soft=8`;
`wrapper.py:117` `while beats < soft*3`; `wrapper.py:118` `beats+=1` at the top of each iteration; and
`wrapper.py:405` `for _ in range(3): beats+=1` **inside** the bind block, same local. One pass of the
outer loop can therefore consume 4 of 24 beats, so `beats` is not 1:1 with loop iterations and the
"24-beat" budget is not 24 exchanges. The engine knows this — `wrapper.py:432` explicitly reassures
that the contact-axis tail "cannot re-enter the bind inner loop's `beats` mutation above". The
skeleton's `[loop]` tag on S2.7.18 is correct but under-specified; it should name the shared counter.

### M6. `combat`: `tempo_pressure` is self-flagged as outcome-invisible at default builds. [MED]
The skeleton uses `tempo_pressure` in S2.7.2 as a live cadence multiplier with no gap row.

*Adjudication: D2 is right.* `combat_systems.py:1330-1339` is a "[HONESTY CORRECTION, ED-PC-0037.1]"
docstring recording an adversarial ablation (20 weapons × 4 tiers, n=400/cell) at −0.06pp ± 0.27,
z=−0.23, "currently OUTCOME-INVISIBLE", and stating the READ term is **identically zero** in any
same-stats fight — i.e. exactly on the weapon-balance surface the harness measures. The first-actor
fix is credited instead to the cadence-phase draw at `wrapper.py:110`. This belongs in §7 as a
declared-but-inert row: it is live code, called every beat, that does not do what the surrounding
narrative claims.

### M7. `combat`: `QUAL['partial']` is unreachable from the damage path. [LOW]
*Adjudication: D2 is right.* `core.py:97` declares it; the following comment states `damage()` gates on
the literal tuple `('graze','success','overwhelming')`, so a partial takes the 0 branch regardless, and
the wrapper maps `partial` to graze/bind and never calls `core.strike` with it. Retained deliberately
as domain documentation — a legitimate declared-not-read row the skeleton omits.

### M8. `characters`: the module comment claims a canonical **13**-Conviction set above a **9**-entry tuple. [HIGH]
*Adjudication: D2 is right, and this reframes the skeleton's own gap 7.* `conviction.py:42-44` reads
"Canonical 13-Conviction set per PP-684 (taxonomy_v30); legacy 9-Conviction from conviction_track_v1 §1
**superseded**", immediately above `CONVICTIONS = (Faith, Order, Reason, Equity, Precedent, Autonomy,
Continuity, Community, Warden)` — 9 names, i.e. the tuple *is* the set the comment declares superseded.
The skeleton's gap 7 correctly finds that `knots.apply_knot_loss` passes `conviction='Loyalty'`, which
is not in the tuple, so every call no-ops. But it treats the 9-tuple as the authority; if the comment is
right, the defect may be that `CONVICTIONS` was never migrated to the 13-set, and `'Loyalty'` may be a
member of the *canonical* set. Either way the two surfaces cannot both be true, and the skeleton
records only one of them.

### M9. `characters`: `BELIEF_MOMENTUM_PER_CONTEST_CAP` declared with a canon citation, never read. [LOW]
*Adjudication: D2 is right.* `beliefs.py:46` declares it with `[canonical: social_contest_v30 §9.5]`;
`social_success` consults only `MOMENTUM_CAP` (`beliefs.py:41`, read at `:213`). The named per-contest
cap is enforced by nothing.

### M10. `mass_battle`: `a_deg`/`b_deg` are computed per engagement pair and discarded. [MED]
*Adjudication: D2 is right.* `massbattle.py:951-952` computes both via `compute_degree` (own comment:
"narrative degree label only"); the function returns `{"dmg_a","dmg_b","engagements"}` (`:972`) and
neither name is read anywhere else in the body. A per-pair dead computation on the hot path, present in
both trees' lineage, absent from the skeleton.

### M11. `mass_battle`: `halt_before_enemy` is a documented no-op called unconditionally every tick in **both** trees. [MED]
The skeleton lists it as a flow step (TREE A S2.4, TREE B S2.10) with no indication it does nothing.
*Adjudication: D2 is right.* `units.py:218-225` — body is `pass`, docstring "v11: over-run correction
disabled … removed after causing ordering asymmetries". Called at `massbattle.py:1196-1197` and
`orchestration.py:1937-1938`. The skeleton's §7 already catalogs `rally_check`/`threadwork_check` as
called-empty hooks; this is the same class and is missing from that row.

### M12. `mass_battle`: `Subunit.resolve_internal_collisions` is fully implemented and never invoked in either tree. [MED]
*Adjudication: D2 is right.* Defined at `units.py:255` and `tests/sim/mass_battle/hierarchy/units.py:2061`;
the only other references are the identical comments at `massbattle.py:1206` and `orchestration.py:1947`
("implemented but not invoked here — it over-tuned battery (12/13 -> 9/13)"). A real discipline-gated
d10 mechanism with zero call sites, in both trees.

### M13. `mass_battle`: `altonian_reinforcements` annotates `world: GameState` with `GameState` never imported. [LOW]
*Adjudication: D2 is right.* Invisible at import only because `from __future__ import annotations`
defers evaluation; a latent `NameError` for any `typing.get_type_hints` introspection. The skeleton
records the `NotImplementedError` but not the broken annotation.

### M14. `threadwork`: `apply_comovement_effects`'s `op_result` parameter is accepted and never read. [LOW]
*Adjudication: D2 is right.* `co_movement.py:130-152` — docstring says "Not currently mutated;
included for future territory-specific side-effect routing", and no statement in the body references it.

### M15. `fieldwork`: `apply_knot_loss` applies 2 of its 4 consequence fields and returns the other 2 unapplied. [HIGH]
The skeleton records the writes (S5.1/S5.2) and separately flags `'wound'` as never reassigned, but does
not record the **asymmetry** or that the docstring over-claims.

*Adjudication: D2 is right.* `knots.py:320` docstring: "routes through coherence + conviction modules".
In the body: `coherence_delta` really is applied (`:361-367` → `apply_coherence_delta`) and
`conviction_scar` really is applied on a Close-tier positive-strain break (`:346-354` →
`apply_conviction_scar`), but `composure_damage` (`:338`) and `disposition_set_to` (`:340`, `:359`) are
only written into the returned dict and applied to no actor object anywhere in the function. Two of four
declared consequences silently depend on an unspecified caller — and per the skeleton's own gap rows
there is no production caller at all. This is the sharpest declared-vs-live finding in fieldwork and the
skeleton states its ingredients without ever joining them.

---

## 3. CONTRADICTED — adjudicated against the code

### C1. `threadwork`: "not schema-migrated" (D1) vs "the migration already landed; the docstrings are stale" (D2).
D1 §7: "Practitioner/Threadcut/Co-Movement state is module-level-fallback dual-stored, **not
schema-migrated** … the ASSUMPTION blocks in each module's docstring flag this as provisional pending a
full World schema migration."
D2 world-finding 10: the `World` dataclass already declares every field the docstrings claim is missing.

**Ruling: D2 is right; D1 is wrong (it propagated the stale docstring).** `engine/autoload/game_state.py:182`
declares `practitioners`, `:200` `threadcut_beings`, `:201` `comovement_deck`, plus `:194-197`
`convictions`/`beliefs`/`knots`/`knot_id_counter` — under headers "Schema migration #1/#2 — 2026-05-19"
with full `serialize_world`/`restore_world` round-tripping. Meanwhile `coherence.py:13-18` still says
"World currently has no practitioner/knot schema", `co_movement.py:11-13` "World has no
`.comovement_deck` field", `threadcut.py:15` "pending schema migration". The migration is **done**; what
survives is only the `world is None` fallback for legacy callers/tests, which each `_store()` already
handles by preferring `world.X` via `hasattr`. Note D1's own §2 IN table cites those exact `game_state.py`
line numbers as live World fields — so the skeleton contradicts itself between §2 and §7. Fix: reword the
§7 row to "module-level fallback retained for `world=None`; the World schema migration landed 2026-05-19,
and five module docstrings are stale in saying otherwise." (D2's own method note discloses that this
finding used its one inadvertent Grep; I re-verified it by direct Read, so the disclosure does not weaken it.)

**No other CONTRADICTED items were found in these six subsystems.** In particular the three cases the
brief flagged as likely disagreements are not disagreements: the two social-contest cycles are both true
at different analysis levels (M1), the mass-battle two-tree comparison already matches (§1), and the
same-beat approach→exchange fall-through is already in the combat skeleton (§1).

---

## 4. SKELETON-ONLY (D2 did not see it) — supportedness check

D2's scope excluded `workbench/`, `engine/cross_scale/scene_dispatch.py` (world reader's scope only),
`references/module_contracts.yaml`, `registers/`, and every test module, so most skeleton-only material
is simply out of D2's window rather than unsupported. I spot-checked the load-bearing ones and found
**no unsupported claims**:

- combat §7 `capabilities.py`/`state_graph.py` not on the live spine — supported (importer sets verified).
- combat S5/§7 the whole `st == "combat"` dispatch branch is dead because nothing queues a combat scene —
  independently corroborated by D2's world reader, which found the identical pattern for
  `fieldwork`/`investigation`, and by vector-audit finding 10 (`executes:false`, 0/29 traced slots).
- social_contest §7 `parliamentary_stay`'s entire API uncalled; `contest/__init__.py`'s stale docstring
  claiming `scene_dispatch` still calls `run_contest`; the ED-137 Panel-closure rebind making
  `PersuasionTrack` unreachable on the one production seam; the `try/except Exception` in `_resolve_slot`
  swallowing resolver errors — all outside D2's reading scope, all anchored.
- characters gap 7 (the `'Loyalty'` no-op) is **strictly better** than D2's version of the same area:
  D2 saw the 13-vs-9 comment, D1 saw the live consequence. Merging them (M8) is the right outcome.
- mass_battle §7's J2 seam analysis, the `AttributeError: 'Subunit' object has no attribute
  'cells_float'` measurement, and the registry-vs-J2 lag — test- and registry-sourced, outside D2's scope.
- fieldwork §7's `RUPTURE_WOUND_DISSOLUTION` / `COHERENCE_BAND_STRAIN_PACING` dead-constant rows —
  D2 found the neighbouring defect (M15) but not these; both verified present.

## 5. STALE-SOURCE

- **S1 (`mass_battle`, immaterial).** `vector_audit.md`'s scorecard counts (271 modules / 89 CLI
  entries / 63 orphans / 24 stub-wired / 21 cut-vertices) predate `tools/observability/build_glossary.py`
  and the 15 new `*_flow_skeleton_v1.md` files. D2 discloses this itself in its §D and bounds it to the
  `tools/` bucket. Every `systems/`/`engine/`/`tests/sim/mass_battle/` structural claim I re-checked
  (the 3 cycles, the SCC membership, `massbattle ↔ units`) reproduces exactly against today's tree, so
  no structural finding in these six subsystems rests on a stale artifact.
- No other STALE-SOURCE items. Notably the vector audit's own §D staleness check is sound: I confirmed
  the cycle data by re-running SCC extraction on the audit's `g_code.json` and matching it to the
  present-day import statements.

---

## 6. Recommended skeleton edits (ordered by value)

1. `fieldwork` §7 — add M15 (2-of-4 consequences unapplied; docstring over-claims).
2. `social_contest` §7 — add M1 (9-node SCC + the one real runtime break at `modes.py:554`),
   M2 (`coalition_vote` as a fourth resolver reusing `roll_net`/`PersuasionTrack` without `Bout`),
   M3 (`Standing.strip` dead), M4 (Orientation/Doubt-Marker + `derive_interaction` dead in resolution).
3. `characters` gap 7 — fold in M8 (13-vs-9), reframing the `'Loyalty'` no-op as possibly a stale-tuple
   defect rather than a caller defect.
4. `combat` S2.7.18 — name the shared `beats` counter (M5); §7 — add M6 (`tempo_pressure` inert) and M7.
5. `mass_battle` §7 — extend the called-empty-hook row to include `halt_before_enemy` (M11); add M12
   (`resolve_internal_collisions` implemented-never-invoked, both trees), M10 (`a_deg`/`b_deg` dead), M13.
6. `threadwork` §7 — correct C1's wording; add M14.
