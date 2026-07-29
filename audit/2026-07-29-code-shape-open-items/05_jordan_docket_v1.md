# Jordan Docket — the 14 held forks of the code-shape program, as one decision surface

## Status: DOCKET — HELD FOR JORDAN (ED-1094 exception: NOTHING here ratifies on merge) — ED-IN-0092, 2026-07-29

> **⚠️ LOUD BANNER — READ BEFORE MERGING THE PR THAT CARRIES THIS FILE.**
> **Nothing in this document ratifies on merge.** CLAUDE.md §2's ED-1094 rule — "merging a PR
> ratifies its PROPOSED contents by default" — is **explicitly suspended for every row below**, which
> is exactly the "held back, loudly" exception that rule requires. Merging this file ratifies only
> *that the questions are correctly posed*. Every fork stays open until Jordan rules it in its own
> home ledger entry, and no wave of `01_orchestration_plan_v1.md` may execute a fork's content on the
> strength of this file existing. Where a "default on offer" is shown, it is a **proposal awaiting a
> ruling**, never an adopted position. Where a row says **NO DEFAULT**, none was invented — per
> CLAUDE.md §5/§7 anti-fabrication, an unbacked number or direction is not supplied here.

**What this is.** `01_orchestration_plan_v1.md` §5's 14-fork table, expanded so it can be ruled
top-to-bottom without opening another file: each fork carries its concrete options, drawn from the
underlying ledger entry / register row / registry file, with the evidence quoted inline. Row format
follows the RULED shape of `workplans/valoria_master_workplan_v6.md` §5 (line 298): *fork · default ·
blocks · home pointer*, **no status column** — resolution lives in the ledger and lane handoffs, not
here — tiered **T0** (blocks the M1 path) / **T1** (blocks a named stage) / **T2** (taste, tuning,
housekeeping). The `#` and `OI` columns are additions, preserving the plan's fork numbering and the
register linkage so `02_disposition_map.md` can be diffed against this file line-for-line.

**Agreement with the ownership surface.** Every `§5 fork N` line in `02_disposition_map.md` appears
below under that same number. Rows 1 and 2 are **cross-session visibility rows only** — both are held
*and adjudicated* inside the MB session's plan; ruling them here would collide with that session.

**Three working-tree corrections found while assembling this docket** (§0.1 point 3 — an assembly
pass that attacked nothing is not an assembly pass):

1. **Fork 12's module list is wrong in both `01_…` §5 and `00_…` OI-10.** They name
   `charter_liberties` and `mass_seizure`; `registers/placeholder_names.yaml` contains **no
   placeholder ROW for either module** (`Mass Seizure` appears only inside
   `infrastructure_reclamation`'s audit-scope text at `placeholder_names.yaml:113`). Its eighth
   row is **`npc_ai_service`**. Corrected list below.
2. **Fork 12 is much smaller than it looks.** 6 of the 8 rows carry
   `canonical_name_pending: "<name> (name confirmed; content TBD)"` — the *name* is already settled;
   only content is pending. Only the **two Varfell rows** are genuinely name-open.
3. **Fork 6's option A has drifted from its ledger text.** ED-SC-0004 (2026-07-05) describes the
   legacy stub as `(Primary × 2) + History − Wounds + fatigue`. The live code has **no wound term** —
   `systems/social_contest/sim/contest_legacy_stub.py:128-129` reads `(primary * 2) + history +
   fatigue_penalty` then `max(1, pool)`; the `−1D` wound cut was removed by Jordan's 2026-07-08 ED-PC-0005
   ruling (docstring, same file). Rule the formula that is actually there.
4. **The docket itself was adversarially reviewed** (valoria-critic, opus, 2026-07-29); its F1/F2/F3
   fixes (Fork 11's missing OI-41 row, Fork 3's stale `CURRENT.md` line cite, Fork 14's stub-range
   mis-cite) are folded into this revision.

Line numbers below are **working-tree, verified 2026-07-29**; where a ledger entry cites a different
line or a pre-restructure `sim/…` path, both are shown.

---

## §1 · T0 — blocks the M1 path

| # | Fork | OI | Default on offer | Blocks | Home |
|---|---|---|---|---|---|
| 3 | **ED-1051 — `engine_clock` `doc:null` ratification**: flip the pointer to `systems/_architecture/propagation_spec_v1.md` | OI-43a | the long-standing default (flip) | M1 juncture 6; GO Gate-0 entry | `registers/editorial_ledger.jsonl` ED-1051; `workplans/…v6.md` §5 T0 (L331); `CURRENT.md:142` (also `:148`); decision queue 12 |

**Why T0.** It is the **sole remaining unstruck row** in the workplan's own T0 table
(`valoria_master_workplan_v6.md` L327–331: four rows struck as RATIFIED/RULED, ED-1051 alone live).
Nothing else on this docket claims M1-path status.

**State of the question.** ED-1051's 2026-07-02 addendum (ED-IN-0002) records: the candidate home doc
**exists and is CANONICAL** — `propagation_spec_v1.md`, ratified 2026-07-02 via ED-1093 — and *"the
authoring half of 'start with engine_clock' is effectively done; only the ratification/ordering call
remains for it."* The same addendum corrects the headline counts **upward**: `module_contracts.yaml`
is now **11/27 `doc:null`** and **13/27 `[ASSUMPTION]`** resolvers, *"both grew since 2026-06-30, not
shrank."* `propagation_spec_v1.md` L379 carries open flag **OF-OWN** — "engine_clock ownership of the
scheduler **assumes** ED-1051" — i.e. a spec already ratified is leaning on a ruling not yet made.

**Options.**

- **A (the standing default) — flip `doc: null` → `propagation_spec_v1.md`.** Zero authoring work;
  closes OF-OWN; unblocks the GO Gate-0 entry. Cost: the temporal spine's home doc is a propagation
  spec that was not written as a clock spec.
- **B — author a dedicated `engine_clock` home doc first, keep `doc: null` until it lands.** Cleanest
  contract semantics; pays authoring time on the M1 critical path and leaves OF-OWN open meanwhile.
- **C — rule `engine_clock` a doc-exempt runtime module** and drop the `doc:` requirement for it.
  Fastest; sets a precedent the other 10 `doc:null` modules will be read against (those are **not**
  this fork — they are `02_disposition_map.md` OI-43b, `DEFERRED → FA/SE/WR/IN`).

---

## §2 · T1 — blocks a named stage

| # | Fork | OI | Default on offer | Blocks | Home |
|---|---|---|---|---|---|
| 1 | Two mass-battle trees: **declare / adapter / promote** — *visibility row only; held AND adjudicated in the MB plan* | OI-11/14/47 | none (MB plan poses all three) | all MB centralization; honest in-campaign battle resolution | `audit/2026-07-26-mass-battle-fable-audit/03_execution_plan.md` §7 fork 1 |
| 2 | **ED-MB-0010** fabricated-emit deletion — *executed by the MB session as E1* | OI-21 | **delete** | dangling-emit zero; MB workbench cards | MB plan §8 / E1; `registers/editorial_ledger_mb.jsonl` |
| 5 | `scale_signature` extension to province/duchy/country per **B12** | OI-35 | extend enum + registry defaults | every scale above `territory` | `engine/substrate/keys.py:62`; `systems/_architecture/key_substrate_v30.md:57`; `scale_hierarchy_v1.md` |
| 6 | **ED-SC-0004** — the canonical Argue-pool formula: legacy stub vs σ-kernel | OI-48a | **NO DEFAULT** (P0 docket) | contest single-owner; SC stage 4; calibration P4; any Godot export | `registers/editorial_ledger_sc.jsonl` ED-SC-0004 |
| 7 | **Turmoil writer** + `parliamentary_vote` **L-restoration** | OI-31a/32b | **NO DEFAULT** — both flip campaign outcomes | honest victory + mandate loops | 07-17 audit D1/D3; `HANDOFF_WR.md` / `HANDOFF_SC.md` |
| 10 | **ED-IN-0029** attribute-roster docket (the `Character`-dataclass gate) | OI-50 | **NO LIVE DEFAULT** — OPT-AV-1 explicitly SKIPPED by Jordan; do not bind | any typed actor schema (explicitly **not** in this program's P1/P2 scope) | `audit/2026-07-08-attribute-value-coherence-audit/ed_options.md` OPT-AV-1 |
| 11 | §1.0-class design forks **carried unchanged**, ruled per their own dockets (bundle of 7) | OI-06b/27b/30b/41/42/49 | per each sub-docket | named stages only | each sub-item's own ledger entry (below) |
| 13 | `settlement_layer` **L/PS `bucket:` tag** — `derived_value` (F1-guarded) vs writable track | OI-33 | **NO DEFAULT** | contract truth for the L/PS pipeline, whose build (OI-37) is the SE lane's own top item | `references/module_contracts.yaml` (settlement_layer); `audit/2026-07-14-holistic-unification/unification_v1.md` §7 item 3 |
| 14 | **Contest GAMES build** (`consensus`/`negotiation`/`inquiry` + Dyadic/Negotiation/Ceremonial `play`) | OI-18b | defer to the SC P0 docket | SC-lane build (the **self-flag** half is B and lands in Wave 1 regardless) | ED-SC-0003 / 0004 / 0005, `registers/editorial_ledger_sc.jsonl` |

### Fork 1 — two mass-battle trees *(do not rule here)*

**Evidence (OI-11).** `tests/sim/mass_battle/` = **28 modules, ~10.5k LOC, all current development**,
with **zero production importers**, importing nothing from `engine/` or `systems/`. The campaign
meanwhile resolves battles on the stale wired tree, `systems/mass_battle/sim/`, reached via
`systems/factions/sim/faction_action.py:349`. Options **declare / adapter / promote** are posed by
the MB plan §7 and belong to that session.

**Re-entry protocol if the ruling is "promote"** (critic F17, reproduced verbatim in substance so it
travels with the ruling): a promote ruling **does not land cleanly**. It invalidates the IN reach
oracle's MB battle-resolution rows (pinned against the currently-wired tree) and it orphans
`faction_action.py:349`, an **FA**-lane file owned by *neither* the MB nor the IN session. Therefore:
the ruling **spawns an FA-lane wiring item** — the seam is FA-owned and moves on FA's schedule — and
**the IN reach-oracle's MB rows flip to stub-flag the moment the ruling lands and stay there until
that FA item re-pins them.** Neither session "just moves the call site." The same term is recorded in
MB §12's seam declaration.

### Fork 2 — ED-MB-0010 fabricated emit *(do not rule here)*

`references/module_contracts.yaml:473` emits `scene_outcome.battle_concluded`, commented *"substrate
§8.5 verbatim"*, alongside the correct `scene.battle_concluded` at **:474** ("registry-declared
form"). Per ED-MB-0010 the provenance claim is **false**: `scene_outcome` is the emit **family** name,
not a `type_id`. Three consuming contracts already cite only the correct form (`:72`, `:123`, `:220`).
Corroborated by 6 independent instruments (OI-21). *(The ledger cites L468/469 — stale by five lines
against the working tree.)* Default: **delete** the `:473` row. Because it is `needs_jordan`, deletion
is an ED-1094 merge-ratification with ledger flip + alias delete + artifact regen — the MB session's
E1, its "cheapest independent win."

### Fork 5 — `scale_signature` vs the B12 hierarchy

**Evidence.** `engine/substrate/keys.py:62` — `SCALES = ("personal", "settlement", "territory",
"peninsula")`, commented "§2.1 scale_signature members (key_substrate_v30.md)". Invariant 7 at
`keys.py:355-359` **raises `KeyValidationError`** on any non-member. The B12 ruling (landed with
direct Jordan input, `audit/2026-07-14-weekly-review/…md` L92) established the hierarchy
**Settlement → Territory → Province → Duchy → Country** in `scale_hierarchy_v1.md`, superseding
`valoria_political_hierarchy_v30` §1/§2.3. Province, duchy and country are therefore **unrepresentable
in any Key**.

**Options.**
- **A (default) — extend the enum + registry defaults** to carry the B12 rungs. Note the enum is
  *canon-derived*: `key_substrate_v30.md:57` must move in the same ruling, or the code stops citing
  its source truthfully.
- **B — keep 4 members; carry province/duchy/country as a separate tier field** on the Key, leaving
  `scale_signature` a coarse delivery axis.
- **C — rule the B12 rungs non-Key-addressable**: they exist in the political model but never appear
  in a `scale_signature`. Cheapest; permanently caps the diagonal/vertical delivery model at
  territory.

On a ruling, the mechanical enum + registry edit is small and lands in IN Wave 3 (`02_disposition_map.md`
OI-35).

### Fork 6 — ED-SC-0004, which Argue-pool formula is canon

Two contradictory implementations are **simultaneously live**:

- **A — the DEPRECATED legacy stub** (`systems/social_contest/sim/contest_legacy_stub.py:111-129`;
  ledger path `sim/personal/contest_legacy_stub.py:111-127`): `pool = (primary × 2) + history +
  fatigue_penalty`, `max(1, pool)`. This is **canon verbatim** *(as amended — see correction 3: the
  `− Wounds` term the ledger quotes was removed by ED-PC-0005, 2026-07-08)* and, per ED-SC-0011, it is
  **the formula the campaign loop actually reaches today**.
- **B — the promoted σ-kernel** (`systems/social_contest/sim/contest/primitives.py:208-211`; ledger
  path `sim/personal/contest/primitives.py`): `Pool.size(faculty) = max(5, faculty*2 + 3)`, with
  `BASE = 3  # [SEED]`. It **drops History, Wounds and fatigue** and raises the floor **1 → 5**,
  erasing the low-pool regime the 2026-05-28 diagnostic measured to 2D. It has **zero live callers**.

The two diverge **9.5–28.9 pp** (`00_…` OI-48, from 07-07 U-3/U-8 — inherited, not re-measured here).
ED-SC-0004 states plainly: **"no stated default."** The ruling gates calibration (P4), the
rolling-engine re-verdict (ED-IN-0013), and any Godot export. **ED-SC-0011** (the personal-party
bridge) is class **B** and lands either way — it is `DEFERRED → SC`, not part of this fork.

### Fork 7 — Turmoil writer and the L-restoration promise

Two held defects from the 2026-07-17 wiring audit (§6 defects register, D1 and D3 — the four held
rows D1/D3/D6/D8 are the ones that "change campaign balance or need a schema ruling"):

- **D1 — `Turmoil` is write-dead.** Initialised at `0.0` (`engine/autoload/game_state.py:234`), read
  **once**, by victory (`engine/autoload/victory.py:73`, `ps = world.clocks.get('Turmoil', 0.0)`),
  and **assigned by no live module** — so the PS victory condition is *trivially always satisfied*.
  Options: **(i)** name an owning module and wire a writer (victory gate becomes real, campaign
  outcomes move); **(ii)** rule the PS gate dormant and delete the read (honest, no balance move);
  **(iii)** leave as-is with a declared gap note. **No default.**
- **D3 — one-way Mandate penalty.** `parliamentary_vote` writes `Faction.L` **directly, off-bus**, on
  a Total Victory (`systems/social_contest/sim/parliamentary_vote.py:213`), and its own note promises
  *"temporary-modifier restoration deferred to season_manager"* — **unimplemented**. The audit's
  companion brief records the catch: the restoration **is verified correct but flips ~72% of campaign
  winners** (`audit/2026-07-17-mc-wiring-coverage-audit/README.md` L112). Options: **(i)** implement
  restoration and re-baseline the goldens, accepting the ~72% flip; **(ii)** rule the penalty
  permanent and strike the promise; **(iii)** hold, with the honest note. **No default.**

Adjacent, not this fork: **J-36** — Key-bus closure for the six off-bus writers, workplan §5 T1
(L352), default *"on-bus, carve-outs explicit"*, whose `[VERIFY]` adversarial pass is still deferred
(`HANDOFF_IN.md` L828). **ED-WR-0003** (hard-coded `private_observers` at six emit sites) is class B,
`needs_jordan: false`, and lands in IN Wave 3 — **not** held.

### Fork 10 — ED-IN-0029 attribute-roster docket

**Do not bind any Godot resource field or `Character` dataclass to attribute keys until this is
ruled** (CLAUDE.md §5). ED-IN-0029's three ledger entries are easy to misread as closure: two are
`status: resolved`, but that resolution is a **partial ratification** whose *first* line reads
**"OPT-AV-1 … SKIPPED per Jordan's explicit instruction ('Skip OPT-AV-1'), left fully open, no roster
edits made."** All mid-session roster edits were reverted; `descriptor_registry.yaml`
`attributes:`/`aggregates:`, `names_index.yaml` and `glossary.md`'s Part-One table are unchanged from
pre-audit state.

**OPT-AV-1's option labels, reproduced (not re-derived)** — *"which roster is canonical: glossary 7 /
registry 9 / either 10-table (C1-F1); Recall registration (C1-F2); the two fold directions
(C1-F3/F4/M1)."* Its **stated recommended default** was: adopt the registry's **9-key structure with
naming corrections** — primaries flip to **Cognition** (ED-899, already live as named engine
constants) and **Spirit** (zero live "Will" usage; both fold targets Acuity/Will have zero
consumers) — **plus `attr.mind.recall` as a 10th key**; retire glossary Part-One formula tables;
supersede `canonical_registry.md`'s competing table. **That default was explicitly not adopted.**
Downstream: 07-17 D8 (two incompatible rosters, no `Character` dataclass, Combat Pool defined 3 ways).

Two further docket rows remain **OPEN with no default invented**, and travel with this fork:
**OPT-AV-13** (Piety/Conviction/CT/CV/PT — one name, four structurally different referents; ED-644's
standing deferral holds) and **OPT-AV-18's Renown sub-item** (cap 10 vs uncapped + the Shadow Renown
relation — the only one of that row's six sub-items with no stated default).

### Fork 11 — the carried §1.0-class bundle (7 sub-forks, each ruled on its own docket)

| Sub-fork | The concrete question | Options / default |
|---|---|---|
| **ED-IN-0049** (= OI-06's J half) | `scale_transitions_v30.md:51` §3.3 "Personal → Scene (Contest)" is a **heading with zero body** and, unlike siblings §3.4/§3.6 (L57/L66), carries **no editorial stub marker**. Invisible to `module_adjudicator`'s J2 check because no contract cites §3.3. | Author the rule (entry condition + resolution actor + state transfer) mirroring the other §3.x rules. **The fork is the lane:** architecture (IN) vs SC, if the content belongs to Social Contest's entry-condition spec. |
| **ED-SC-0005** cap | Bonus-die stack (Recall/Corroborate/Prep/Findings) reaches **+8D over base in exchange 1** while genre/audience is already capped at **+2D combined**. All four channels are **entirely unimplemented** — a spec fix with no code urgency, but it must land **before** stage-4 wiring makes it live. | DP-2's candidate ceilings, verbatim: **A +2D · B +3D · C +4D · D one combined cap across both bonus classes**. **No default** — the cap value is Jordan's design number. `audit/2026-07-08-pessimist-action-audit/decision_packets/DP-2_SC_KU1_stacking_cap.md`. |
| **Field/Gauge primitive** (= OI-49) | Three competing "faction political power" formulas (franchise NI · `political_value()` TBD scalars · settlement Mandate), Mandate monotone with **no withdrawal/collapse path**, and **~27 distinct cross-scale value-transformation rules with no shared aggregation contract**. | The `Field`/`Gauge` substrate primitive is **PROPOSED only, Stratum-B conditional** (`engine/substrate/fields.py` does not exist). Adopt / defer / rule the three formulas separately. |
| **ED-SC-0015** | Parliamentary Total-Victory Mandate stacking: `parliamentary_vote` §10 self-applies Mandate −1 to the losing coalition's dominant faction; `faction_layer_v30` §5.4's Censure tier applies its own −1 on a pass. Neither source says whether they compound on the **same faction in one motion**. Generalizes to every future Sanction tier (Embargo/Blockade/Combined/Outlawry, ED-FA-0006). | **Stack to −2 on a TV pass**, or **cap the target at −1 total**. Currently implemented as stacking, as the literal-faithful reading — **explicitly not ratified canon**; the existing test documents current composition, not intent. |
| **OI-27 registry-contradiction slice** | `meta.cascade_cluster_event` is cited by CANONICAL articulation trigger #9 but **never registered**; `state.opinion_revised`'s registry text **contradicts** the §3.1 table; zoom-trigger tables cite **no `type_id`**. | Register / re-word / strike, per type. *(The rest of OI-27 — the ED-IN-0004 articulation §3.1 omissions — is class **B**, `needs_jordan: false`, and lands in IN Wave 3.)* |
| **OI-30 C2** | Are `npc_behavior`'s **beliefs / concerns / projects / arc state** registry quantities at all, or relational/psychological state outside the scalar registry? | Removing them **drops up to 5 identifiers from the pointer-debt denominator** — a meter move with **no registry work**, which is exactly why it must be decided explicitly rather than absorbed. *(Category B — register the genuine scalars: Wounds, Turmoil, Accord, Poise, Initiative, the `engine_clock` season counter — is class B, IN Wave 3.)* |
| **OI-42 / OF-3** | `decay()` in the Key-ledger aggregation is **unspecified**. `propagation_spec_v1.md` proves **termination only**; cross-tick **convergence is conditional** on `decay()` being *strictly contractive* (L270, L348, L379), so event-builds can persist at bounded, non-decaying amplitude for a whole campaign. | Specify `decay()` — it must be a **pure function of `key.emitted_at`** (no RNG, no hidden state) to preserve §6 determinism; that constraint is ruled, the function is not. Companion open flag **OF-D6** (the D.6 double-count disjointness, flagged HIGH PRIORITY / Jordan) gates the same guarantee. |
| **OI-41** | The design-blocked cross-scale set: caste cascade unwired (GAP-F2) · Church/CI ideological-consent axis not lifted (GAP-G1) · insurgency pipeline dead-by-construction · fracture resolution mechanics orphaned (`fractional_province_ownership`) · §5.2 claiming/§5.3 chain-bypass RULED but zero armature binding · territorial-tier propagation (`scale_hierarchy_v1.md` §6) un-started. | **Not a single question to rule here** — per `01_…` §5 row 11's own default ("per their own dockets") and `02_disposition_map.md`'s OI-41 line: each member rules on its own named docket; the build half is `DEFERRED → FA/SE/WR` per `01_…` §3.5. This row states that routing explicitly so the bundle routes rather than silently carries it. |

*Not in this bundle:* the **damage-law canon fork** is MB plan fork 6 — ruled there, not here.

### Fork 13 — `settlement_layer` L/PS `bucket:` tag

`module_contracts.yaml`'s `settlement_layer` Legitimacy / Popular Support derivation is a
**Mandate-feedback drift loop with no `bucket:` tag**, while **its sibling derivations are tagged**
(`unification_v1.md` §7 item 3). A reader cannot tell whether it computes a distinct value or
**rewrites the base track**. Options: **A — `derived_value`** (F1-guarded, i.e. no writer may target
it) · **B — writable track** (a named module owns the write). **No default.** Second, smaller
question in the same row: whether the Mandate-feedback loop is inside F1 coverage at all. This is the
contract-truth precondition for OI-37 — the L/PS pipeline that `HANDOFF_SE.md` calls *"the single
highest-priority open item in this entire thread"* and whose `lps_inert_check` is **100/100 red**.

### Fork 14 — the contest GAMES build

Router state (OI-18): `agon` **WIRED** (`systems/social_contest/sim/contest/wrapper.py:207`);
`consensus` / `negotiation` / `inquiry` are **STUB rows** in the `GAMES` dict
(`systems/social_contest/sim/contest/wrapper.py:209-214`; the `:199-204` range is the `_stub()`
factory those rows call, not the rows themselves), and `DyadicMode` / `NegotiationMode` /
`CeremonialMode.play` are **scaffold-only** (`modes.py:328-334`). The build is gated on the SC stage-4
**P0 docket**, all three entries `needs_jordan: true`:

- **ED-SC-0003** — the "Piety Track" name collision: **one name, two referents, three docs** (the 0–10
  debate tracker is *Piety Track* in `scale_transitions_v30` / `npc_behavior_v30` / `glossary.md:84`
  but *Persuasion Track* throughout `social_contest_v30.md`, while `engine/params/bg/` uses *Piety
  Track (PT)* for an unrelated per-territory BG stat). Decide the winning name, its single canonical
  home, and the rename/alias for the per-territory stat. **No stated default.**
- **ED-SC-0004** — fork 6 above.
- **ED-SC-0005** — the bonus-die cap, fork 11 above.

**Options for this fork itself:** **A (default)** — defer the build to the SC docket, ship the
**self-flag** half now (class B, IN Wave 1, so the three stubs announce themselves instead of
failing silently) · **B** — build on the σ-kernel ahead of the docket, accepting rework if fork 6
rules for the legacy formula · **C** — declare `consensus`/`negotiation`/`inquiry` out of M1 scope
and mark them terminal-stub.

---

## §3 · T2 — taste, tuning, housekeeping

| # | Fork | OI | Default on offer | Blocks | Home |
|---|---|---|---|---|---|
| 4 | **`env.crisis` consumer — or ruled terminal** | OI-22b | **NO DEFAULT — none named anywhere** | only the final "dangling-emit zero" claim; Wave 3's exit **explicitly holds it out** (`4 → ≤1`) | `references/module_contracts.yaml:522` (`scenario_authoring`), `:774` (`peninsular_strain`) |
| 8 | **Dual-emit attribution** — `scene.dialogue`, `mechanical.scene_entered`, `state.belief_revised` | OI-29 | **shape only** — "assign a single canonical emitter each"; **no per-type winner is named** | contract-truth completeness | `module_contracts.yaml` `gap_notes` `[OPEN — Jordan]`; GAP-J3 |
| 9 | **Retire-candidates** `settlement_economy`, `campaign_architecture`; **NPC lane ownership** | OI-43c / 59a | retire half: fold/retire per GAP-K2/K3 · **lane half: NO DEFAULT — "lane = Jordan's"** | contract hygiene *(see the honesty note)* | `audit/2026-07-14-gameplay-subsystem-observatory/gap_register_v1.md` L149–150 |
| 12 | **Placeholder-name rulings** for the `registers/placeholder_names.yaml` rows | OI-10b | **NO DEFAULT** — the rows are unresolved | naming closure; **the stub-wire half is class B and lands in Wave 1 regardless** | `registers/placeholder_names.yaml` |

### Fork 4 — `env.crisis`

**Verified in tree:** exactly **two emitters** — `scenario_authoring` (`module_contracts.yaml:522`)
and `peninsular_strain` (`:774`) — and, across all 27 contracts, **zero consumers**. The plan's
default column is honest: **none named anywhere**, in code or in prose.

**Option space, presented rather than invented.** The only non-fabricated candidates are the modules
that already consume this emitter's *sibling* `env.*` types (machine-read from the contracts, this
session):

| sibling type | declared consumers |
|---|---|
| `env.disaster` | `faction_state`, `settlement_layer` |
| `env.peninsular_strain_shock` | `faction_state`, `npc_behavior`, `settlement_layer` |
| `env.population_change` | `faction_state`, `settlement_economy` |

So: **A** — name one or more of `faction_state` / `settlement_layer` / `npc_behavior` as consumer
(the union of the sibling consumers; `settlement_economy` is a fork-9 retire candidate and would be a
poor choice) · **B** — **rule `env.crisis` terminal**, i.e. an authored-signal Key with no runtime
consumer, and mark it so in both contracts · **C** — strike it as a duplicate of `env.disaster`.
**Nothing in the corpus prefers any of these**; do not read the sibling table as a recommendation.

### Fork 8 — dual-emit attribution

The default is a **shape**, not an assignment: "assign a single canonical emitter each" leaves the
per-type winner unruled. Machine-read from `module_contracts.yaml` this session:

| type | claiming modules |
|---|---|
| `scene.dialogue` | `npc_behavior`, `scene_slate`, `social_contest` (3) |
| `mechanical.scene_entered` | `scene_slate`, `game_director` (2) |
| `state.belief_revised` | `npc_behavior`, `fieldwork_knots` (2) |

Rule one winner per row (7 candidate assignments total), or rule that co-emission is legal and the
contract schema should say so. GAP-J3's own disposition is **UNRECONCILED**.

### Fork 9 — retires and the NPC lane

- **`settlement_economy`** (GAP-K2): phantom module — `doc:null`, no `state:`, in-3/out-0.
  Recommendation on record: **fold into `settlement_layer`**; resolves GAP-A2 and GAP-B5. Ledger
  hook: ED-SE-0005.
- **`campaign_architecture`** (GAP-K3): stub with **0 edges** — a consolidation doc, not a runtime
  module. Recommendation: **retire**; content distributes across victory / threadwork / settlement /
  peninsular_strain.
- **NPC lane ownership** (OI-59a): the `npc_behavior` / `npc_memory` / `npc_ai` family has **no owning
  workplan lane** despite `[ASSUMPTION]`-grade resolvers, `doc:null`, and Stage-2.5 precondition
  status. Both integration hubs are cut-vertices and both are `[ASSUMPTION]`-grade —
  `faction_state` (in-13) and `npc_behavior` (in-12) — so *the highest-value Key flow passes through
  the least-certain resolvers*. Candidate owners: **WR** (where `02_disposition_map.md` OI-59b already
  defers the grounding work), **IN**, or **a new NPC lane** (a new lane means a new `ED-<LANE>` code,
  a `CURRENT.md` row and a `HANDOFF_<LANE>.md`, per CLAUDE.md §4 / RULED §2a). **No default.**

**Honesty note on the tier.** Tiered T2 from the plan's own Blocks column ("contract hygiene"). The
**lane half arguably belongs in T1** — OI-59 ties it to Stage-2.5 precondition status. Flagged, not
silently re-tiered; if Jordan reads it as T1, only this row's placement changes.

### Fork 12 — placeholder names (list corrected)

The eight rows of `registers/placeholder_names.yaml`, read this session — **note `npc_ai_service`,
which both `01_…` §5 and `00_…` OI-10 omit, and note that `charter_liberties` and `mass_seizure`,
which they both list, do not appear in the file at all**:

| # | placeholder_name | prior_name | canonical_name_pending | blocks_canonization |
|---|---|---|---|---|
| 1 | `varfell_mandate_action` | `vaynards_hall` | **TBD post-Varfell-contamination-audit** | **yes** |
| 2 | `varfell_territorial_acquisition` | `einhir_revival` | **TBD post-Varfell-contamination-audit** | no |
| 3 | `altonian_reinforcements` | (same) | name confirmed; content TBD | no |
| 4 | `infrastructure_reclamation` | (same) | name confirmed; content TBD | **yes** |
| 5 | `home_sanctuary` | (same) | name confirmed; content TBD | **yes** |
| 6 | `hafenmark_equipment` | (same) | name confirmed; content TBD | **yes** |
| 7 | `npc_ai_service` | (same) | name confirmed; content TBD | **yes** |
| 8 | `tactic_cards` | (same) | name confirmed; content TBD | **yes** |

**What this reshapes.** Only rows 1–2 are genuinely **name**-open, and both wait on the same thing:
**the Varfell contamination audit**, with `deadline_pass: "Pass 3 (post-audit)"`. Rows 3–8 have
confirmed names and pending **content** — for them the ruling is a *content* commission, not a
rename. Row 1 additionally carries a live mechanical defect: its `W-1 + Mil-1 → +1 L` mechanism was
**flagged broken by Jordan on 2026-05-17** (double-cost asymmetry vs other faction Mandate actions),
so "both name AND mechanic redesign pending."

**Consequence of the lifecycle, worth knowing before ruling.** The file's own contract: flipping a row
to `expired` makes `valoria_hooks.placeholder_names_gate` **halt the next commit** unless that commit
performs the rename. All eight are `pending`, so nothing halts today — but ruling a name **arms** the
gate for its module. Options per row: **rename now** (arms the gate; the rename must ride the same
commit) · **confirm the placeholder as canonical** (row closes, no gate event) · **hold for the
contamination audit** (status quo, rows 1–2's stated design).

---

## §4 · Appendix A — J-completeness: the register's 20 J-carrying rows

`00_open_items_register.md`'s *Counts and shape* (as corrected 2026-07-29, critic F1b) states **20
rows carry a J component: 6 wholly J-classed, 12 mixed B/J or M/J, 2 D/J.** All 20 are enumerated
below and every one maps to a docket row or to an MB visibility row. **Mapped: 20 / 20 — none
missing.**

**The 6 wholly J-classed**

| OI | Row | → |
|---|---|---|
| OI-11 | Two disjoint mass-battle code graphs | **row 1** (MB plan §7 fork 1) |
| OI-21 | Fabricated `scene_outcome.battle_concluded` emit | **row 2** (MB plan E1) |
| OI-29 | Dual-emit attribution (3 types) | **row 8** |
| OI-33 | `settlement_layer` L/PS `bucket:` tag | **row 13** |
| OI-35 | `scale_signature` cannot represent province/duchy/country | **row 5** |
| OI-49 | Three faction-power formulas; no shared aggregation contract | **row 11** (Field/Gauge) |

**The 12 mixed B/J or M/J** *(J half only; the B/M halves are owned in `02_disposition_map.md`)*

| OI | J half | → |
|---|---|---|
| OI-06 | `scale_transitions_v30` §3.3 empty heading (ED-IN-0049) | **row 11** |
| OI-10 | The placeholder **names** themselves | **row 12** |
| OI-18 | Contest GAMES **build** | **row 14** |
| OI-22 | `env.crisis` — 2 emitters, 0 consumers | **row 4** |
| OI-27 | Registry-contradiction slice (`meta.cascade_cluster_event`, `state.opinion_revised`, zoom `type_id`s) | **row 11** |
| OI-30 | Category **C2** — are npc beliefs/concerns/projects registry quantities | **row 11** |
| OI-31 | J-36 off-bus writers + `parliamentary_vote` L-restoration | **row 7** |
| OI-32 | `Turmoil` write-dead → victory gate trivially satisfiable | **row 7** |
| OI-41 | Design-blocked cross-scale set (caste, CI-consent, insurgency, fracture, §5.2/§5.3, territorial tier) | **row 11** |
| OI-43 | ED-1051 `engine_clock` flip **(row 3)**; retire-candidates **(row 9)** | **rows 3 + 9** |
| OI-48 | ED-SC-0004 canonical Argue-pool formula | **row 6** |
| OI-59 | NPC family has no owning workplan lane | **row 9** |

**The 2 D/J**

| OI | J half | → |
|---|---|---|
| OI-42 | `decay()` / OF-3 (the D half — cross-tick convergence — stays `D (existing ruling)`) | **row 11** |
| OI-50 | ED-IN-0029 attribute-roster docket (D = do not bind meanwhile) | **row 10** |

**Coverage check.** 6 + 12 + 2 = **20 rows**, all mapped; **2** route to MB visibility rows (1, 2) and
**18** onto rows 3–14, exactly as `01_…` §5's J-completeness note asserts. Docket rows carrying no
distinct OI row of their own: none — every row 1–14 above cites at least one OI. Rows 3 and 9 both
draw on OI-43 (its two J halves, `02_disposition_map.md` OI-43a and OI-43c); row 7 draws on two rows
(OI-31a, OI-32b); row 11 draws on six.

---

## §5 · Sources (every claim above resolves here)

- `audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` §5 (the 14-fork table, the
  J-completeness note, the row-1 re-entry protocol) · §3 Wave 3 exit (the `4 → ≤1` dangling-emit
  criterion that holds `env.crisis` out).
- `audit/2026-07-29-code-shape-open-items/00_open_items_register.md` — OI-06/10/11/18/21/22/27/29/30/
  31/32/33/35/37/41/42/43/48/49/50/59 and *Counts and shape*.
- `audit/2026-07-29-code-shape-open-items/02_disposition_map.md` §1 — the authoritative row→owner
  lines this docket agrees with; §2's `§5 forks 19` primary-owner count.
- `workplans/valoria_master_workplan_v6.md` §5 L296–331 (the RULED row format; the T0 table showing
  ED-1051 as the sole unstruck row), L352 (J-36), L347–348 (DP-2, ED-IN-0029).
- Ledgers: `registers/editorial_ledger.jsonl` (ED-1051) · `registers/editorial_ledger_sc.jsonl`
  (ED-SC-0003/0004/0005/0011/0015) · `registers/editorial_ledger_mb.jsonl` (ED-MB-0010) ·
  `registers/editorial_ledger_in.jsonl` (ED-IN-0029 ×3, ED-IN-0049, ED-IN-0059).
- Registries/code, read in the working tree 2026-07-29: `references/module_contracts.yaml`
  (`:473`/`:474`, `:522`, `:774`, and the machine-read emits/consumes tables) ·
  `registers/placeholder_names.yaml` (8 rows) · `engine/substrate/keys.py:62,355-359` ·
  `engine/autoload/game_state.py:234` · `engine/autoload/victory.py:73` ·
  `systems/social_contest/sim/parliamentary_vote.py:213` ·
  `systems/social_contest/sim/contest_legacy_stub.py:111-129` ·
  `systems/social_contest/sim/contest/primitives.py:205-211`.
- Audits: `audit/2026-07-17-mc-wiring-coverage-audit/README.md` §6 (D1/D3/D8, and L112's ~72%) ·
  `audit/2026-07-14-gameplay-subsystem-observatory/gap_register_v1.md` (GAP-J3 L142, GAP-K2/K3
  L149-150) · `audit/2026-07-14-holistic-unification/unification_v1.md` §7 items 2–3 ·
  `audit/2026-07-08-attribute-value-coherence-audit/ed_options.md` (OPT-AV-1/13/18 + the
  ratification-outcomes table) · `audit/2026-07-14-weekly-review/…md` L92 (the B12 hierarchy) ·
  `systems/_architecture/propagation_spec_v1.md` L189, L205, L270, L348, L379 (OF-3, OF-OWN, OF-D6).

*Companions: `00_open_items_register.md` (rows) · `01_orchestration_plan_v1.md` (waves) ·
`02_disposition_map.md` (ownership) · `03_adversarial_review_2026-07-29.md` (the review record) ·
`04_execution_ledger.md` (status, created by Wave 5). **This file carries no status column and never
will** — a fork's resolution is recorded in its own ledger entry and its lane handoff.*
