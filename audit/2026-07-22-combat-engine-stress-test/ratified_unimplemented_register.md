# Ratified-but-not-implemented register (2026-07-22)

**Purpose.** A single index of work that was **ratified / RULED / landed as a plan-of-record** but whose **code
or artifact implementation is missing or incomplete**, and which **remains relevant** (not later superseded).

**Why this exists (the prevention motive).** This session repeatedly "discovered" things the corpus had already
diagnosed and ratified — most sharply, I reported the half-sword name-table + dead `can_halfsword_thrust` as a
*novel* finding when it is exactly **audit G3 / plan P3 / consolidation JD-3** (ratified 2026-07-04), un-wired.
The repo has an observability surface for **unratified** work (`PROPOSALS.md`, via
`tools/observability/build_proposals.py`) and for **marker debt** (`DECISIONS.md`), but **no index of the dual
case — ratified yet unbuilt** — so these items are invisible unless you already know they exist. That blind spot
is the root cause; see **§Prevention**.

**Status legend:** `NOT STARTED` · `PARTIAL` (formula/data built, not wired live) · `BLOCKED` (needs a named
prerequisite) · `NEEDS-JORDAN` (a ratified default exists but the expansion is a held-back call).

**Rollup (25 items across 7 lanes; MB clean, GO has none independent of engine_clock).** Highest-leverage:
- **IN-1 engine_clock** — the single **T0 blocker for M1** *and* the GO lane (ratified design, zero code).
- **FA-1 B12 scale-tier rewrite** — `CURRENT.md`'s own "highest-priority open wiring gap" (no `Territory` symbol in code).
- **WR-1 MS→RS sweep** — **gates any Godot engine-params export** (CLAUDE.md §5).
- **PC-1 grippable/ricasso half-sword** — the safest to *do*: ratified **and byte-identical at parity**.
- **A cheap-flip cluster** — FA-4/FA-5/SE-1/SE-2/SC-1 are ratified items whose docs were never flipped
  `PROPOSED → CANONICAL` (a `## Status:` line each); high value, near-zero risk.

---

## PC — Personal combat (verified against code this session)

Sources: `audit/2026-07-04-weapon-morphology-granularity/{audit_v1.md,consolidation_v1.md}` (RATIFIED
plan-of-record per `CURRENT.md`), `registers/handoffs/HANDOFF_PC.md`, `registers/editorial_ledger_pc.jsonl`,
the accepted-red tests in `tests/valoria/test_combat_*.py`.

| # | Item | Ratified where | Requires | State | Evidence |
|---|---|---|---|---|---|
| PC-1 | **Emergent half-sword via `grippable`/ricasso** | audit **G3** + plan **P3** + **JD-3** (2026-07-04) | `elements[].grippable=True` on ricasso zones; `affords_halfsword(w)=(∃ grippable fwd element)∧can_halfsword_thrust(cv,pc)`; retire `HALFSWORD_FORM`/`HALFSWORD_BASE` as behaviour gates; land **byte-identical at {longsword, estoc}** | **NOT STARTED** | `weapons.py:864 HALFSWORD_FORM={'longsword','estoc'}` still a live name-table; `geometry.can_halfsword_thrust` **dead** (bake computes `geo['halfsword']`, zero readers); no `grippable` field or `affords_halfsword` in code |
| PC-2 | **Half-sword roster expansion** (which attested ricassos grant a form) | **JD-3** (default: parity only) | after PC-1 lands, flip `grippable=True` for flamberge/greatsword (attested ricassos) → new anti-plate capability | **NEEDS-JORDAN** (blocked on PC-1) | ricasso attested in data: `weapons.py:111` greatsword "with ricasso, often flanked by parrying lugs"; `weapons.py:690` flamberge ricasso mass element |
| PC-3 | **Live-wire JD-4 (reversed-grip/Mordhau) + JD-9 into `element_afforded`** | **ED-PC-0009** (JD-4/JD-9 DETERMINED 2026-07-08) | add the weak reversed-grip percussion + graded cut/point as competing selection tokens | **PARTIAL / BLOCKED** | formula built + tested (`weapon_physics.reversed_grip_percussion`; `tests/valoria/test_combat_reversed_grip.py`) but **not wired live** — blocked on a `core.coupling` fix (DELIVERY doesn't scale with percussion magnitude except vs mail/plate) per consolidation §"U2 scope note" |
| PC-4 | **ED-PC-0012 — secondary-point `THRUST_AUTH_REF` fix** | ED-PC-0012 (open, "known, documented, load-bearing residual") | scale `DELIVERY['point']` by the candidate's own thrust magnitude (as `CUT_AUTH_REF` does for 'cut'); expected to remove the sabre/scimitar/falchion spurious plate-switch | **NOT STARTED** (deferred) | `test_combat_invariants.py::test_use_mode_selection_emerges_from_primitives` lists sabre/scimitar/falchion as FLAGGED changers pending this fix |
| PC-5 | **PHASE-C — reach-class / mass-model / poleaxe-spike recalibration** | tracked accepted-red; deferred pending Jordan target bands | armour-conditional approach stop-hit (spear/yari), poleaxe spike-vs-plate, PoB_frac normalization (heft-ordering) | **BLOCKED (design call)** | accepted-red `test_gap_game_poleaxe_spikes_plate`, `test_falsifiable_heft_ordering`; see this session's Phase-C investigation — needs target win-rate bands |
| PC-6 | **R3 slices U3–U9** (edges-data JD-2, grip-physics, renderer JD-8, T-P2/T5) | consolidation_v1.md (RATIFIED plan-of-record) | the remaining execution tranches after U0/U1/U2 | **NOT STARTED** | HANDOFF_PC: U0/U1 done, U2 live (formula only); U3–U9 unexecuted; JD-8(b) renderer rebuild pending (scratchpad script confirmed lost) |

**Note (not RBNI, but adjacent):** the **half-sword *liability*** finding (the switch is a net loss where enabled)
is a *new bug*, not ratified-unimplemented — but it means PC-1's byte-identical expansion would propagate a broken
mechanic, so PC-1 and PC-5 should land together, not PC-1 alone.

---

## SC / IN / GO / engine_clock — (corpus sweep, code-verified)

**GO lane: no qualifying item** — the governing `godot_conversion_strategy_v1.md` is itself still `PROPOSED` and
Gate-0 (KeyStore v2, base classes, RNG service) is unruled (`HANDOFF_GO.md`); nothing has crossed PROPOSED →
ratified, so there's no ratified-but-unbuilt GO item *except* engine_clock (below), which blocks GO but is filed
as an architecture/IN ratification.

| # | Item | Ratified where | Requires | State | Evidence |
|---|---|---|---|---|---|
| IN-1 | **engine_clock module contract** (the M1 T0 blocker + GO gate) | `propagation_spec_v1.md:69-90` §O.2, CANONICAL via ED-1093/1094 (2026-07-02) | an `engine_clock`/`clock_advance` resolver implementing the season-tick/accounting-boundary contract | **NOT STARTED** | no `engine_clock`/`clock_advance` code anywhere in `engine/`|`systems/`; `module_contracts.yaml:702` still `doc:null, status:extracted`. (Nuance: the *design* is ratified via §O.2, but the closure ticket **ED-1051** is itself still `open/needs_jordan` — `editorial_ledger.jsonl:261` — so the adjudication step is unratified while the contract sits unbuilt) |
| IN-2 | **ED-IN-0075 Certainty→Truth rename** (finish the sweep) | `editorial_ledger_in.jsonl` ED-IN-0075 RULED 2026-07-18 (Jordan ruling A) | complete the corpus-wide rename where "Certainty" denotes the per-character Truth axis | **PARTIAL** | 89-file sweep left live surfaces: `godot/godot_architecture_specification.md:810,878`; `systems/threadwork/sim/co_movement.py:49` ("Certainty pressure" string in live sim); `skills/{prose-writer,valoria-mechanic-audit,valoria-simulator}` instructions — none in the stated exclusion list |
| SC-1 | **ED-SC-0008 refresh social_contest module contract** | ledger RATIFIED 2026-07-05 (PR #80) | fix stale `resolver: dice_pool` + dead Key literals (`state.opinion_revised`, `scene.dialogue/insult/threat`) to match the δσ kernel; add `godot_home`/`typed_params` | **NOT STARTED** | `module_contracts.yaml:437-459` still `resolver: dice_pool` + the dead literals; grep of those 4 strings across `systems/social_contest/sim/contest/*.py` = 0 hits (contract names Keys the kernel never emits) |
| SC-2 | **ED-SC-0009 Face/Rattled strain channel + Thread hooks** (Stage-4 entry) | ledger RATIFIED 2026-07-05 | wire `strain ≥ Face → Rattled → −1D` via a real `Standing.strip()`; wire SS9.3–9.4b thread hooks | **NOT STARTED** | `contest/primitives.py:83-90` states outright "`Standing.strip()` is NEVER called… Face has NO strip/strain channel wired"; no thread hooks in resolver/contract/wrapper |
| SC-3 | **ED-SC-0010 Chronicle focalization + first consumer** | ledger RATIFIED 2026-07-05 | add chronicler/focalization field (P-03); give the Chronicle record a real consumer | **NOT STARTED** | `contest/narrative.py:40-50` Chronicle dataclass has no focalization field; no arc-generator/engine consumer imports it |
| SC-4 | **ED-SC-0011 / ED-SC-0013 FORK-C — auto/played parity harness** | ED-SC-0011 RATIFIED 2026-07-05; reframed by ED-SC-0013 RULED 2026-07-08 (forks A/B/D resolved) | a parity harness proving `parliamentary_bridge` auto-resolve ≈ the played kernel; event-parameterize the auto-resolver to specific Slate motions | **NOT STARTED** (FORK-C still needs_jordan) | no parity-harness file (`agon_harness.py` is a different, human-play harness); `parliamentary_bridge.py:34-49 _derive_vote` still a generic per-season roll |
| SC-5 | **ED-SC-0014 Standing homonym scope-tag** | ledger RATIFIED 2026-07-08 ("execution deferred, FA co-sign required") | scope-tag the "Standing" homonym (BG 0–10 vs contest kernel); add a `name_collision_database` entry | **NOT STARTED** | `clock_registry_v30.md:53` still "Standing | 0–5"; `name_collision_database.yaml:142` no new entry; independently confirmed stale by `audit/2026-07-13-multi-agent-audit/.../number_systems_audit.md:12` |

## MB / FA / WR / FI / SE — (corpus sweep, code-verified)

**Systemic meta-finding.** A recurring failure mode across FA/SE/WR: PR#119/#129-era items were logged
`ratified` in `registers/editorial_ledger_*.jsonl` **and** in `CURRENT.md`'s own prose, but the target docs
were **never flipped from `## Status: PROPOSED` to CANONICAL** — precisely the ED-1094/ED-1083 "merge ratifies
by default" failure the convention exists to prevent, recurring anyway. These are cheap flips (a Status line +
sometimes a short merge/authoring pass), high-value to close. **Mass Battle: no qualifying items** (DG-1..DG-5 /
ED-MB-0001..0006 were implemented same-session; DG-6+ are still `open`/`needs_jordan`, i.e. not yet ratified).

| # | Item | Ratified where | Requires | State | Evidence |
|---|---|---|---|---|---|
| FA-1 | **B12 scale-tier rewrite** (Settlement→Territory→Province→Duchy→Country + bidirectional governance cascade) | `systems/settlements/scale_hierarchy_v1.md:3` "RATIFIED — Jordan 2026-07-13"; `CURRENT.md`:114 ("highest-priority open wiring gap") | author the new Territory tier into canon + wire into code | **NOT STARTED** | `scale_hierarchy_v1.md:161` itself says "needs a real rewrite"; `systems/settlements/sim/registry.py` has **no `Territory` symbol** |
| FA-2 | **ED-FA-0002 domain_actions home** (M1 workplan next-action) | ledger "RATIFIED 2026-07-05" (PR #81); rescoped by ED-FA-0006 | flip `domain_actions` off `doc:null`; add per-verb `da.*` tag column; rule 3 bucket forks | **NOT DONE** | `references/module_contracts.yaml:482` no tag column; `HANDOFF_FA.md:95` "ED-FA-0002 (open)" |
| FA-3 | **ED-FA-0021 §1.0d Kaochengfa merge + E11** | ledger `ratified`; `governance_consolidation_v1.md:3` "D1–D6 RATIFIED" (ED-IN-0046/47) | merge §1.0d into the suspicion/recall spine + author E11 counter | **NOT DONE** | `faction_politics_v30.md:129` still `PROPOSED`, no merge; **E11 exists only in the ruling doc**, never authored into canon (grep-empty) |
| FA-4 | **ED-FA-0020 §1.0c** (Court Attendance & Hostage-Kin) | ledger `ratified` 2026-07-13 (ED-IN-0046); `CURRENT.md`:113 | flip §1.0c → CANONICAL | **NOT DONE** | `faction_politics_v30.md:117` still `**Status: PROPOSED.**` |
| FA-5 | **ED-FA-0022/0023 §2.5a** (Guild entry/mastership forks) | same (ED-IN-0046) | flip §2.5a → CANONICAL | **NOT DONE** | `faction_politics_v30.md:568` still `PROPOSED` |
| SE-1 | **ED-SE-0021 §3.3b** (Za patron-lapse) | ledger `ratified` 2026-07-13 | flip §3.3b → CANONICAL | **NOT DONE** | `settlement_layer_v30.md:640` still `PROPOSED` |
| SE-2 | **ED-SE-0023 §1.3c** (Ordenanza Ratification) | ledger `ratified` 2026-07-13 | flip §1.3c → CANONICAL | **NOT DONE** | `governance_play_redesign_v1.md:97` still `PROPOSED` |
| WR-1 | **ED-WR-0002 MS supersedes RS** world-track sweep | ledger "RATIFIED 2026-07-05" (PR #77); **gates any Godot engine-params export** (CLAUDE.md §5) | rename RS→MS across `params/threadwork.md`; flip `names_index` lint `warn`→`block` | **NOT DONE** | `engine/params/threadwork.md` reads "RS" throughout; `names_index.yaml:94` still `enforce: warn` |
| WR-2 | **ED-WR-0001 GD-1 strike-banner sweep** (peninsular_strain co-victory sites) | ledger "RATIFIED 2026-07-05" (PR #77) | add `[SUPERSEDED-BY: GD-1]` to ~7 live sites | **NOT DONE** | `grep -c SUPERSEDED-BY peninsular_strain_v30.md`=0 (vs 4 in sibling `victory_v30.md`) |
| WR-3 | **ED-WR-0003 Appraise Revelation §6.1/§6.1b + "overheard" rule** | ledger "RATIFIED 2026-07-05" (PR #81, EP-7) | write the §6.1/6.1b procedure; add a player-observer conditional to gossip Keys | **NOT STARTED** | `npc_behavior_v30.md:679-684` §6.1/§6.1b headers **empty**; gossip emits hardcode `private_observers` (no player conditional) |
| FI-1 | **ED-FI-0002 Counter-espionage loop** | ledger "RATIFIED 2026-07-05" (PR #81, EP-6) | investigable trail + exposure-flip + response surface for enemy covert `da.*` | **NOT STARTED** | no doc/code; `HANDOFF_FI.md:27` "(open)"; the one FI item the audit called "genuine new design" |
| FI-2 | **ED-FI-0001 Field-investigation lane audit** | ledger "RATIFIED 2026-07-05" (PR #77) | run the audit-style pass on `investigation_systems_v30`; address orphan throughlines T-02/T-30 | **NOT STARTED** | unresolved in HANDOFF_FI/IN; last listed un-actioned 2026-07-07 |

---

## Prevention — why key aspects were missed, and the systemic fix

**Root cause.** There is no observability surface for *ratified-but-unbuilt* work. The repo generates
`PROPOSALS.md` (unratified/open items, `tools/observability/build_proposals.py`) and `DECISIONS.md` (marker-level
debt), but the **dual** — *decided, not yet built* — has no index, so it is discoverable only by someone who
already read the specific audit. Every "I found X" this session where X was already ratified traces to this gap.

**Fix (proposed, systemic — the durable prevention):**
1. **This register becomes a generated surface.** Add `tools/observability/build_ratified_unimplemented.py`
   (sibling of `build_proposals.py`, reusing `obs_core.py`) that scans three machine-readable signals and emits
   this register automatically, so it can never silently drift:
   - **accepted-red tests** whose docstrings carry a deferral tag (`[PHASE-C FLAG]`, `DEFERRED`, `not silently
     patched`) — each is a ratified expectation the code doesn't yet meet;
   - **ledger entries** ratified (`status: ruled`/`ratified`) but carrying an `implemented: false` (or an
     `unwired`/`deferred` note) field — **requires adding a small `implemented` boolean to the ledger schema**;
   - **plan-of-record JD/U items** marked with a ratified *default* but no execution record.
2. **Search discipline (immediate, no tooling):** before labelling any finding "novel", grep `audit/` +
   `registers/editorial_ledger*.jsonl` for the mechanism keyword (here: `halfsword`, `ricasso`, `grippable`).
   This session's miss would have been caught by a single `grep -ri ricasso`.
3. **Anti-orphan gate for the geo surface.** The dead `geo['halfsword']` slipped through because — unlike the
   wrapper's circumstance fields (`test_every_circumstance_field_has_a_live_reader`) — the `geometry.bake` output
   coefficients have **no reader-existence test**. Add one; it would have flagged `can_halfsword_thrust` as dead
   the day it was written.

**Net:** the blind spot is structural (no RBNI index), so the fix is structural (generate one) — not "try harder
to remember". Items 2 and 3 are cheap and land now; item 1 is the real prevention and is a small tool.
