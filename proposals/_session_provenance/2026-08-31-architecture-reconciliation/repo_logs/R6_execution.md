# R6 — research/, tests/, tools/, workplans/, CI : what runs and what is pinned

Method: full read of `research/valoria_systems_integration_master_v1{,_part2,_part3,_part4}.md`,
`research/cross_scale_action_catalogue_v1.md` (full), `research/valoria_game_precedent_companion_v1{,_part2,_part4}.md`
(full) and part3 headers; module-docstring extraction over all 158 `tests/valoria/test_*.py`;
full read of `.github/workflows/valoria-ci.yml`; full read of `tools/m1_acceptance.py` (executed
`--summary`, confirmed read-only first — no `open(..., 'w')`/`.write()`/`json.dump` in the file);
`workplans/workplan_v6_progress.yaml` M1 block; `references/ci_checks_registry.yaml`; git log on
PRs #343/#344. Parts 3 of both research docs and precedent-companion parts 5-8 were sampled by
header/grep rather than read verbatim — flagged where load-bearing.

---

## 1. ⭐ `research/valoria_systems_integration_master_v1.md` (+parts) — architecture

**Structure.** Four parts, ~1,830 lines total. Part 1 (`valoria_systems_integration_master_v1.md`)
= collation method (§1, 11 harvest lanes, 1,079 records, `valoria_systems_integration_master_v1.md:23-40`)
+ slice/status vocabulary (§2, `:102-160`) + FLATTEN tables for faction-strategy, parliament-politics,
economy-accounting, settlement-governance, territory-world (§3). Part 2 continues §3 for People,
Cross-Scale Plumbing, Resolution Kernel (seam-only), Mass-Battle Seam (seam-only). Part 3 = §4
within-system analysis (load-bearing conflicts + cheapest fix per system, sampled — see §3 below).
Part 4 = §5 cross-category comparison (F1-F10) + §6 four integration proposals with NERS attacks.

**Status vocabulary (`valoria_systems_integration_master_v1.md:118-135`, `CLAUDE.md` §0.2-bound):**
BUILT (production path reaches it in a seeded campaign) · INERT (code exists, correct, nothing
calls it — "the finding, not a synonym for unbuilt") · DESIGNED (canon, no code) · PROPOSED
(research/proposals/audit, not canon) · RULED-UNEXECUTED (Jordan decided, code doesn't reflect it)
· SUPERSEDED.

**The headline number (`_part4.md:20-42`).** 338 classified things across ten systems: 109 BUILT
(32%), 100 DESIGNED (30%), 51 PROPOSED (15%), **43 INERT (13%)**, 21 RULED-UNEXECUTED (6%), 14
BUILT-with-defect/unreachable (4%, of which 8 are inert in substance). Folding those 8 into INERT:
**51 things, 15% of the corpus — finished machinery with no caller** — "the same size as the
entire PROPOSED corpus and roughly half the size of everything that runs" (`:34-36`). Verdict:
"Valoria's problem is not that it is underdesigned... not that the code is wrong... the parts are
not connected to each other" (`:38-42`).

**Ten cross-system findings (§5.1, `_part4.md:44-330`), each with file:line evidence in-source:**

| # | Finding | One line |
|---|---|---|
| F1 | Eight lanes, asked independently, all named a **writer** (not a mechanic) as their cheapest fix — 7/8 pure writers, 1/8 (People) a writer + a determinism precondition (loading 2 NPCs moved the seed-42 winner via a shared RNG stream, `_part4.md:70-76`) |
| F2 | The absent person is the highest-fan-out blocker: `world.npcs` is empty in every seeded campaign; 6/10 systems name `personnel-roster` as their blocker (`:80-103`) |
| F3 | The absent memory is the second blocker, and its primitive is already built and inert: `systems/settlements/sim/ledger.py`'s five-family tag store has zero production writers (`:106-134`) |
| F4 | Every homeostatic loop in the game is open at one end or undamped — `Faction.standing` unbounded/undamped, Wealth monotone-decreasing with no income, Turmoil/IP/PI/Strain painted-on, `InsurgencyRecord.L` welded at 1.0 (`:137-165`) |
| F5 | Seven live name collisions (Standing ×3, Disposition ×3, Officer ×2, Territory, Mandate, Scale ×3 vocabularies, Sanction) that become real defects once both halves are built (`:169-188`) |
| F6 | Three rival faction action economies + two rival settlement ones; the one live seasonal budget primitive (`AP = 2+facility_tier`) has zero readers (`:190-207`) |
| F7 | ~150-190 genuine gaps hide behind ~471 catalogued (duplication measured at ~30+~10 pairs); the fiscal and personal-meter corpora each reduce to one or two primitives (`:209-227`) |
| F8 | The one working cross-scale crossing (Scene→Faction, emergency council) works *because* it needs no person — "a faction arguing with itself" (`:230-261`) |
| F9 | The defend list: Key substrate, resolution kernel, `ledger.py`, `derive_parties` returning `None` on a gap rather than fabricating, `populate_from_geography`'s raise-on-illegal-type, the ported mass-battle engine (`:265-286`) |
| F10 | The binding constraint is **attribution**, not cost — eight cheap writers landed together are unmeasurable under §0.1 pt 4; ordering (determinism-neutral first) is the real deliverable (`:289-315`) |

**Synergy matrix (`_part4.md:317-332`):** Person unblocks 8 systems, Ledger unblocks 7, Wealth
income unblocks the entire 21-mechanism fiscal proposal corpus by itself.

**Four rival integration proposals (§6), each judged as-if-built against ED-IN-0027 and NERS:**

- **P1 — Close the Circuits** (`:375-451`): add nothing, connect eleven existing writers in a
  blast-radius-ordered sequence (table `:392-404`). Needs 2 rulings (accord-echo §5.5 pair;
  `MULTS['standing']`). NERS: passes conditional on grudge decay.
- **P2 — Three Primitives** (`:454-536`): Person / generalised Ledger / Budget. Cuts the weighted
  `rng.random()` draw and the card-hand economy. NERS **fails as first stated** (AP-as-modifier is
  worth ~1.8× more on a small pool than large — the same flat-shift trap one level up); **passes**
  under "AP buys actions, never modifiers."
- **P3 — The Disposal** (`:539-617`): delete inert modules with zero callers by import *or* string
  (checked against `module_contracts.yaml`, not just grep — two modules are load-bearing only
  through `composition.require`). NERS: code cuts out of scope and pass; the Sanction-tier cut
  fails P-iv and is replaced by a parameterised-magnitude REFINE.
- **P4 — The Season Is a Person's Season** (`:619-745`): invert the loop to iterate people; a
  faction's move is the aggregate of its office-holders' acts. Cuts `if faction.name==` personality
  and the weighted draw. NERS **fails as first stated** (roster-sized pool grows unboundedly —
  worked: 4 people → z≈1.01/P≈84%, 12 people → z≈2.58/P≈99.5%, pool 36 far outside the 5-18D
  calibrated band); **passes** under "the roster buys action-count, not pool size" — the identical
  repair P2 needed, reached independently (`:661-684`).

Author's own run order (§6.5, `:706-722`): **P3 → P1 (steps 1-2 first) → P2 (after F5 naming) →
P4 (person schema, unordered relative to P2)**.

**Direct precedent for the ideal-v2 design.** P4's thesis — "stop iterating factions, iterate
people; a faction acts because someone in it acts" — is the architectural ancestor of the
`proposals/2026-08-31-ideal-v2/` design's `Person`/`Office`/`Tenure` carriers and its
`choose : (Person, View, Sensation) -> Act` signature (no World, no faction-level draw). The
Domain Action Resolver / sigma-leverage two-engine NERS analysis in P2/P4 also directly
foreshadows the ideal-v2 compendium's resolution-shape work. **Neither research doc is cited
anywhere in the ideal-v2 suite** (see §9 below).

---

## 2. ⭐ `cross_scale_action_catalogue_v1.md` — the closed action set, reconciled against the design

**Full table.** All actions with build status, per `research/cross_scale_action_catalogue_v1.md`
§§1-9. (BI = bilateral model, no Ob; U = unopposed; SO = statically opposed; DO = dynamically
opposed — only two DO mechanisms exist tree-wide, `:72-76`.)

| action | scale | actor | pool | Ob/shape | built? | source |
|---|---|---|---|---|---|---|
| Conquest | faction | any | — | BI (delegates to mass battle) | **YES** | `:108` |
| Muster | faction | any | Mil+floor(W/2) | 1, U | **YES** | `:109` |
| Govern | faction | any | Influence | 2, U | **YES** | `:110` |
| Royal Progress | faction | Crown | I+standing | U | **YES** (PROVISIONAL) | `:120` |
| Great Work | faction | Crown | L | 4, U | **YES**, simplified (multi-season deferred) | `:121` |
| Coronation Renewal | faction | Crown | I | SO (score/2 match) | **YES** | `:122` |
| Excommunication | faction | Church | L | SO | **YES** (PROVISIONAL) | `:123` |
| Council of Solmund | faction | Church | L | U | **YES** (PROVISIONAL) | `:124` |
| Absolution | faction | Church | I | 3, U | **YES** (Ob unratified) | `:125` |
| Mass Seizure | faction | Church | I+floor(CI/15) | U | **YES**, zero prod. callers | `:126` |
| Parliamentary Censure | faction | any | vote | — | **YES** (only Sanction tier built) | `:127` |
| Charter of Liberties / Hafenmark Equipment / Varfell Mandate / Varfell Territorial / Home Sanctuary / Infrastructure Reclamation / generic Tribunal / Treaty proposal | faction | Hafenmark/Varfell/Church/any | — | — | **NO — stubs** (8 of 16 unique rows) | `:128-135` |
| Embargo/Blockade/Combined/Outlawry (Sanction tiers 2-5) | parliament | any | vote | — | **NO** (4/5 tiers) | `:157-160` |
| Subsidy/War Auth/Treaty Ratif/Recognition Challenge/Succession Endorsement | parliament | any | vote | — | **NO** (5/5) | `:162-165` |
| Parliamentary Territorial Transfer | parliament | any | I±1 | `holder.L+2`, SO (contradicts score/2 ruling) | **YES** | `:171-174` |
| Develop/Fortify/Keep Order/Hold Court/Sponsor/Treat/Levy/Investigate/Retain Clerks/Survey/Negotiate Quota/Bind the Cells/Ordenanza/Petition-Defy | settlement | governor | varies | varies | **NO — design-only, zero resolver in code** (`:216`) | `:231-246` |
| **Examine, Interview, Research, Surveil, Thread-Read, Reconstruct** (the six investigation acts) | fieldwork | any | (Attr×2)+History | U/DO | **NO — design-only**; `fieldwork.py`/`investigation.py` are all `stubwire.stub_resolve` no-ops | `:612-619`, `:581-587` |
| Read/Converse/Connect/Impress/Rumour/Negotiate/Gift-Bribe | fieldwork | any | varies | U/SO | **NO — design-only** | `:636-644` |
| Discovery Procedure (exploration) | fieldwork | any | (Attr×2)+History | U | **NO — design-only** | `:661` |
| `form_knot`/`sustain_knot`/`check_knot_rupture`/`apply_knot_loss` | fieldwork | any | — | U | **YES — the one live fieldwork module** | `:671-684` |
| Leap, Weaving, Pulling, Past-Oriented Pulling, Locking, Dissolution, Mending (7 Threadwork ops) | threadwork | any | (Spirit×2)+History+TPS | all U | **YES — all 7, `rendering.py` stub only** | `:711-729` |
| ~35 mass-battle mechanics/roles/orders (composed army, not "an action") | mass battle | commander | — | BI | **YES — 31/31 mechanics WIRED**, 7/18 instruction tokens consumed | `:287-365` |
| Personal combat (continuous physics, not a menu) | combat | fighter | resolution_pool(History) | BI, `DECISIVE_OB=3` fixed | **YES — whole model**, Contact/grapple built-unactivated | `:368-480` |
| advance/hard/shift/support/evidence/rebut/pass (7 contest moves) | social contest | any | Pool.size(faculty) | U/DO | **YES — all 7, `resolver.VALID_KINDS`** | `:491-501` |

**Summary table (`:877-889`, §10):** Faction ~35 specified / **~11 executing**. Settlement
governance ~14 verbs+6 Directives+5 tags / **0 executing** (entirely design-side — "the richest
*unbuilt* surface in the repo"). Mass battle 31 mechanics / **31 executing** (most complete
system). Personal combat: the whole model executes. Social contest: all of it executes. Fieldwork:
**knots only** ("the largest design-to-code gap in the tree", `:589`). Threadwork: 7/7. Cross-scale:
1 of 8 mandatory triggers evaluable, 1 of 8 handoffs production-reachable.

**Reconciliation against the ideal-v2 design's closed act set.** `proposals/2026-08-31-ideal-v2/03_COMPENDIUM.md:781-783`
lists twelve acts by function: `carry`, `compose_agenda` (RESOLVE/ACTS); `transfer`, `commit`,
`requisition`, `investigate` (RESOLVE/ACTS); `confer`, `revoke`, `issue`, `determine`, `dispatch`,
`convene` (RESOLVE/ACTS) — this list is confirmed correct as given in the task brief.

- **`investigate` is the collision the design's own PR #344 review caught and corrected.**
  `00_INDEX.md:136-137`: *"a reinvented claim source, and an invented `investigate` verb standing
  where six shipped acts already were."* `01_ARCHITECTURE.md:1236-1242`: an earlier draft
  "invented a single `investigate` verb ... with no verb, no cost, no obstacle owner and no
  resolution path" where `systems/fieldwork/investigation_systems_v30.md` §`03_knowledge_telling_investigation.md`
  already "ships six acts, an obstacle owner, a derived query." `03_COMPENDIUM.md:353` names them
  explicitly: **`examine · interview · research · surveil · reconstruct · Thread-Read`** — an
  **exact match** to the action catalogue's §6.2 Investigation-actions table above
  (`cross_scale_action_catalogue_v1.md:610-619`), row for row. `02_THE_SEASON_LOOP.md:912,1069`
  shows the correction absorbed into the season-loop worked example (the six investigative acts
  register facets/union/copy against the root-token discipline).
- **What survives as `investigate` in `03:781-783`'s table is therefore a header entry pointing at
  those six acts collectively**, not a seventh, generic verb — the design's post-#344 state.
  `02_THE_SEASON_LOOP.md:912` still calls them "the six investigative acts."
- **Every other catalogue action-family has NO home in the twelve-act closed set as filed**, and
  the design does not claim otherwise: `transfer`/`commit`/`requisition` are the design's own
  generalised primitives standing in for Muster/Govern/Develop/Fortify/Levy/Sponsor/Treat/Trade;
  `confer`/`revoke`/`issue`/`determine`/`dispatch`/`convene` stand in for
  Excommunication/Censure/Sanction-tiers/Parliamentary-Transfer/Directive/Hold-Court/Ordenanza.
  Personal combat, social contest (7 move kinds), threadwork (7 ops) and mass-battle's 31
  mechanics are **entirely absent from the twelve-act table** — they are not reconciled at all in
  the read files; whether they are meant to route through `contest`/`verbs` (also §9b's function
  table, `03:773-774`) or are simply out of scope for this design pass is not stated in the
  documents this lane read. That is a genuine gap between the closed-vocabulary claim and the
  catalogue it should be checked against — flagged in §10 below.

---

## 3. `valoria_game_precedent_companion_v1.md` (+parts 2-8) — precedent architecture

Full read of Part 1 (survey by system, 13 subsections) and Part 4 (Reconcile/Unify, §8-§11). Parts
2-3, 5-8 sampled by header (`grep -n "^#|^##"`) — not read verbatim; flagged.

| precedent | game | mechanical pattern | what Valoria imports (proposed) | used in code today? |
|---|---|---|---|---|
| Interest-group clout / law enactment | Victoria 3 | Multi-stage law, running success/stall chance, 3 setbacks fail it, **attempting a measure mobilizes opposition** | I-19 (Tier 3, ruling-gated): the enactment clock — "V3's parameters do not transfer, the structure does" (`_part4.md:294`) | No — Valoria's vote is a single free roll every season |
| Crown authority tiers / negotiable vassal contracts | CK3 | 4 authority levels gate what the liege may do at all | Named as the caution ("personal-opinion bonuses papering over structural factors") — capped-affection refusal (`_part4.md:312`) | No |
| Emitted ruler goals × family influence | Old World | ambitions emitted from person × houses around him, expire on death | I-11 (Tier 2, blocked on person object) | No |
| Influence-over, not ownership; politicians age/die | Kremlin | custodian/holder split, mortality clock | I-13 (custodian_id ≠ holder_id — "the sharpest architectural gap") | No |
| Recorded defeat / *senatus auctoritas* | Rome (procedural, not a game) | a vetoed-but-carried motion persists, citable | I-2, "nearly free" | No |
| Drafting right / *piaoni* | Ming China | whoever drafts frames what's ratified — no power stat | I-15 (blocked on person/seats) | No |
| Shared loss | Republic of Rome (board game) | the state itself can fail; everyone loses | I-20 (Tier 3, ruling: is there a campaign-terminal failure state at all?) | No — Second Calamity is contract-declared, zero code |
| Governor role's 20-year unsettled history | Total War (added/removed 3×) | "no convergent answer — a real, unsettled design tension" | Cited as license for P3's disposal method, not itself imported | Valoria has no governor resolver either |
| Council-seat denial | CK | passed-over figure accrues −40 opinion | I-4: a Grudge tag written on denial (`ledger_add`) | No |
| *Dedizione* / Charter of Submission | Venice | conquest = negotiated pact, not colour change | I-21 (Tier 3 ruling: how much the Entry Terms fork should carry) | No — conquest is instant ownership transfer today |
| Fuzzy-threshold, legible-inputs (5/5 convergence) | JA2/RoTK/Triangle Strategy/CK/Three Kingdoms | publish inputs, hide the trigger point | **U-1 the Disclosure Contract** — first move, DOC-only cost | No |
| JA3 compression | Jagged Alliance 3 | JA2's 5-layer stack → "liked squadmate present: +1 AP" | Cited as the ambition ceiling for a d10/TN-7 engine | No |
| Levy vs professional split (4/4) | CK/Shogun2/JA2/RoTK | levies free+political rationing; professionals cost gold+prestige, maintain even unraised | I-17 (blocked on unit record); Valoria's Muster is "already the professional model wearing a generic label" | Partial — Muster exists, no split |
| Garrison-as-assignment (4/4) | JA2/Brigandine/Unicorn Overlord/TW | garrison is the same unit pool re-assigned, not a troop type | I-16 (blocked on unit record) | No — `Territory.garrison` is a bool |
| Officer CLASS-gating | Total War: Three Kingdoms | gate troop access on a class, not a named biography | I-9 (DOC now, MOVES after person exists) | No |
| Two-tier defeat severity | TW: Three Kingdoms | commander death destroys retinue only if the whole army also routs | I-10 | No — unconditional total-Experience loss today |
| "No precedent solves N=1→1000+ leverage" | Dominions/Mount & Blade/TW | scale-blind flat OR fully-fused (personal actor vanishes at scale) — no precedent is provably in-band across the range | Named as the corpus's hardest null (D3); binds U-4 | Valoria's own two failure poles are already coded, 16 lines apart, both unreachable |
| Fidelity ladder (Played/Witnessed/Auto) | Football Manager (clean) vs Total War (a *different algorithm*, 20yr unsolved divergence) | one engine, several fidelities, calibrated so instant≈played | Jordan's own 2026-07-08 framing; "don't build a second resolver at all" is on the table, not a corner case | Valoria's Slate is the spine (RULED); only 1/8 triggers evaluable |
| Layered/conditioned generation stack (convergent 4×) | DF worldgen / Caves of Qud / Ultima Ratio Regum / WFC-fix | a conditioning layer above the local solver | Named, general lesson — "physics has graphics; nothing equivalent exists for mood/grudge/loyalty" (carried verbatim into the refusal register) | No |
| *Duel of Wits* | Burning Wheel | staged declared-purpose debate; **scaled compromise on loss**; secret-scripted manoeuvres | I-5 (compromise rule), I-6 (pre-roll gap detector) — refused: "manoeuvres differentiated only by damage output" | No |
| Contradiction-matching | Ace Attorney/Danganronpa | one correct statement+bullet per round | **Refused** as primary political resolution — "zero political modelling"; keep only inventory-as-argument | No |
| Interlocutor skills | Disco Elysium | skills argue with each other inside the player's head | Named as transferable idea, not costed | No |
| Positional pricing | Pax Pamir/Pax Renaissance | pay by placing coins on skipped cards, subsidising the taker | Named, not costed into the register | No |
| No enforcement mechanism for promises | Diplomacy (1954) | every promise is cheap talk by default | Named as the required default: "a world where treaties bind automatically has no diplomacy in it" | Valoria's treaty layer is half-stubbed either way |
| Accrual-as-property-of-a-built-structure | Heroes of Might and Magic (**not surveyed**, named as a gap in §2.13) | stock piles up at a place whether or not you visit it | I-22 (Tier 3 ruling: does it double-count against CK's entitlement model?) | No — `facility_tier` sits at 0 on all 37 settlements forever |

**Four unification moves (§9, `_part4.md:112-211`):**

- **U-1 The Disclosure Contract** (DOC only) — publish every input, show a band never a number,
  never publish the trigger. Absorbs the 5/5 fuzzy-threshold convergence.
- **U-2 One Accrual, One Ledger, One Budget** (MOVES + schema) — **this is P2 reached from
  precedent instead of code**, and it independently corroborates P2's primitive choice from six
  separate borrowings landing on the ledger alone.
- **U-3 The person as a relationship ledger with a roster attached** (RULING then MOVES) — **U-3 is
  P4's substrate**; person defined by its edges first, roster second.
- **U-4 Couple the scales, or stop claiming the differentiator** (RULING then MOVES) — the honest
  one: Valoria's own Ω-clause defines itself *against* Mount & Blade's faction-politics/combat
  isolation, and the survey finds Valoria currently sitting exactly where M&B sits (§2.12,
  `valoria_game_precedent_companion_v1.md:506-543`). **This is the precedent doc's single sharpest
  finding**, and it is not cited anywhere in the ideal-v2 suite (§9 below).

**§10 explicitly maps precedent onto the integration master's four proposals** (table,
`_part4.md:219-224`): U-1 is a free P1 prerequisite; U-2 *is* P2; P3 gets Total War's
governor-oscillation as its strongest defence; U-3 is P4's substrate and U-4 is the warning P4
does not itself carry.

---

## 4. THE TEST INVENTORY

All 158 `tests/valoria/test_*.py` module docstrings extracted (full one-liner table saved at
`/tmp/.../scratchpad/repologs/test_oneliners.txt`). By rough subject share: ~35 mass-battle
(`test_charger_latch`, `test_cell_morale`, `test_frontage_conservation`, ...), ~30 personal-combat
(`test_combat_*`), ~10 social-contest/dice-engine, ~40 tooling/apparatus (`test_ci_*`,
`test_*_check`, register/ledger hygiene), ~15 cross-cutting substrate (`test_key_*`,
`test_engine_*`), rest scattered (faction, settlement, world, workplan).

**Named-in-brief, read in full:**

| test file | pins | behaviour or apparatus | constrains ideal-v2? |
|---|---|---|---|
| `test_engine_does_not_import_systems.py` | `engine/` imports **zero** `systems.*` modules (module-level or function-local), asserted by subprocess-import + regex ceilings pinned at 0 | **behaviour** (architectural invariant) | Yes — any Person/Rung/Office/Site engine layer must not reach into `systems/` |
| `test_no_polling_triggers.py` | `.claude/settings.json` `permissions.deny` covers all 7 self-scheduling primitives; CLAUDE.md §11 text present | **behaviour** (process/agent-safety) | No — orthogonal to design |
| `test_morale_write_sweep.py` | every absolute `.morale`-style write reaches the owning cell store; `_CELL_OWNED` registry is field-parameterized, new fields inherit the guard | **behaviour**, and the CLAUDE.md §0.1 template for future write-sweep guards | Yes as a **pattern**: a Person/Tenure "mint/alter/efface" write-sweep guard is the direct analogue once any such field is cell/store-owned |
| `test_claim_provenance_fields.py` | `ci_claim_provenance_check` scans every field a claim/instrument can live in (not just `description`+`provenance`) | apparatus (ledger hygiene) | No |
| `test_key_substrate.py` | Key substrate invariants: registry load, SSI append-order, `KeyLog` replay determinism (byte-identical across two identical-seed constructions), termination-breach cascade cap, B1 no-sync-re-entry, OF-7 deferred-apply | **behaviour** — this is the closest existing analogue to the design's `Query`/state-change/`Event` primitives | **Yes, directly** — the design's `(subject, mode, driver)` state-change model and its `Event`/`Claim` distinction should be checked against this substrate's append-only, replay-deterministic contract before any Godot/engine work starts |
| `test_key_graph.py` | Key graph coverage: 55 declared types, ~1 historically emitted (`scene.accord_echo`); no tool joins the two authored formats (free-prose vs typed `emits`/`consumes`) | **behaviour+apparatus mix** — measures the SAME under-population problem the design's `witness`/`Claim` per-person model would inherit if built on the current substrate | Yes |
| `test_degree_ladder_single_owner.py` | one degree ladder, one declared HELD exception (`combat_engine_v1/core.py:degree`) | behaviour | No direct bearing on ideal-v2 |
| `test_m1_acceptance_probe.py` | rows 1-2 of `m1_acceptance.py` are genuinely measured (reproducible under a fixed probe seed), not merely plausible-looking | **behaviour** — the meta-test for the M1 gate itself | No |
| `test_mass_battle_byte_exact.py` | byte-exact golden digests for the two grid-mode toggles | behaviour | No |
| `test_world_initial_state.py` | the campaign's opening position is authored+validated, and a code relocation (S5b) moved none of the values | behaviour | No |
| `test_wiring_validation.py` | `export_composition.py`'s `validate_wiring` — module_contracts rows are named/unique/carry a `wiring:` block | apparatus | No |

**What would have to be true for the design's four structural tests to run** — none have been run;
none of the read source files declare a harness for them:

1. **"No decision function can see the world"** — would need `choose : (Person, View, Sensation) -> Act`
   implemented as an actual Python (or GDScript) callable with a *typed* signature that omits a
   `World`/`GameState` argument, plus a **static or runtime enforcement** analogous to
   `test_engine_does_not_import_systems.py`'s subprocess-import probe — e.g. a test that constructs
   `choose` from its module and asserts (by `inspect.signature` or an AST scan for global-state
   reads) that it never references `engine.autoload.game_state` or any singleton. The commit log
   (`f129ca7`) records that this guarantee was **already found broken once** in GDScript terms — "no
   module system, no visibility modifiers, an autoload is a global identifier reachable from any
   script" — and downgraded from "unwritable" to "unreachable-by-name" (an explicit `World` first
   arg on every resolver query). No code implementing either version exists in the read trees.
2. **"Two witnesses of one event can disagree"** — needs `witness : (Person, Event) -> Claim[]`
   implemented per-person (never a collection, per the brief) with actual divergent output for two
   distinct `Person` inputs against the same `Event`. The nearest existing harness is
   `test_key_graph.py`'s consumer/producer join, but that operates on a single shared Key log, not
   per-observer `Claim` objects — a new object and a new resolver would be required; nothing in
   `engine/substrate/` currently produces divergent per-observer output from one emission.
3. **"A person with no office can act, petition and receive an opportunity"** — closest present
   analogue is the (currently empty) `world.npcs` / `generate_npc` pipeline (INERT per the
   integration master, F2) — a person object exists in code (`NPC` dataclass) but the design's
   `Person`/`Rung` carriers and its `opening_set` (belief-vs-world-truth split, per the commit log)
   have no code counterpart at all. A test would need a populated `world.npcs`-equivalent, a
   `Rung`-typed office-holding relation with a "None" state, and an `opening_set`/`Sensation`
   generator that does not gate on office — none of this exists.
4. **"Order independence"** (of act resolution within a step, presumably) — the closest existing
   pattern is `test_key_substrate.py`'s replay-determinism and cascade-depth guards, and
   `engine_clock.py`'s three-phase `season_tick → action → accounting_boundary` ordering
   (`test_engine_clock_phases.py`). A genuine order-independence test would need the design's
   RESOLVE step implemented with multiple `Act`s queued in one tick and an assertion that permuting
   their submission order does not change the resulting `Event[]` (mod tie-break policy) — no such
   harness exists; the closest analogue, `test_partition_invariance.py` (mass-battle convergence
   normalisation), tests a narrower numerical-partition property, not act-ordering independence.

**None of the four are executable against any code in the read trees today.** All four would need
new objects (`Person`/`Rung`/`Office`/`Site`/`Tenure`/`Query`) that do not exist in `engine/` or
`systems/`, confirming the design is, per its own commit history, "PROPOSED and held back...
nothing here has executed."

---

## 5. THE TOOLS INVENTORY

56 modules under `tools/`. Cross-checked against `references/ci_checks_registry.yaml`'s `role:`
lines (`references/ci_checks_registry.yaml:124-495`, ~28 roles documented) and
`.github/workflows/valoria-ci.yml`'s literal `tools/*.py` invocations.

| tool | role (registry or docstring) | wired into CI? | blocking? |
|---|---|---|---|
| `ci_register_size_check.py` | token-threshold on governed files | yes | **blocking** (`validators`) |
| `ci_co_file_checker.py` | co-file pairing (design→canonical_sources etc.) | yes | **blocking** |
| `ci_editorial_checker.py` | `[EDITORIAL]`/`[PROVISIONAL]` markers | yes | **blocking** |
| `ci_pp_frozen_check.py` | PP ceiling PP-726 enforced as real, not declared | yes | **blocking** |
| `ci_naming_check.py` | Solmund-never-Galbados, diff-aware | yes | **blocking** |
| `ci_names_consistency.py` | descriptor/proper-noun registries mirror names_index | yes | **blocking** |
| `export_engine_params.py` | oracle→typed-JSON round-trip (combat_engine_v1) | yes | **blocking** (`--check`) |
| `export_key_types.py` | registry→typed-JSON (key_types.json) | yes | **blocking** |
| `export_game_constants.py` | oracle→Godot-constants round-trip, writer half of the ttrpg→valoria-game bridge | yes | **blocking** |
| `export_descriptors.py` | registry→typed-JSON, sole runtime reader source for `descriptors.py` | yes | **blocking** |
| `export_composition.py` | module_contracts→typed-JSON + wiring validation (absorbed retired `wiring_map_check.py`) | yes | **blocking** |
| `export_module_contracts.py` | module_contracts emits/consumes interface→typed-JSON | yes | **blocking** |
| `export_world_initial_state.py` | world_initial_state.yaml→typed-JSON, campaign opening position | yes | **blocking** |
| `ci_sim_fabrication_check.py` | anti-fabrication guard on numeric literals in `sim/*.py` | yes | **blocking** |
| `ci_claim_provenance_check.py` | ledger MEASURED numbers must cite a re-runnable instrument | yes | **blocking** |
| `ci_vetting_check.py` | PP-674 framework vetting gate | yes | **blocking** |
| `validate_ed_citations.py` | every cited ED-id resolves to a real, non-open entry | yes | **blocking** |
| `broken_dependency_checker.py` | dead references to files | yes | **blocking** |
| `freshness_gate.py` | canonical SHA drift detection | yes | **blocking** |
| `m1_acceptance.py` | the 5-row §0.2 execution gate | yes | **report-only** (`validators-report`; `--summary`) |
| `ci_naming_check.py --warn` | naming drift lint (warn tier of same tool) | yes | report-only |
| `currency_consistency_check.py` | CURRENT.md reconcile-stamp vs head freshness | yes | report-only |
| `ci_quantity_vocabulary_check.py` | A17 stat-vocabulary closure | yes | report-only |
| `mechanics_index_gen.py` | mechanics_index.yaml schema/cross-ref | yes | report-only |
| `ci_generation_consistency.py` | v40 generation currency invariant | yes | report-only |
| `canon_coverage_check.py` | canon coverage (repointed designs/→systems/ 2026-08-01) | yes | report-only |
| `ci_module_shape_check.py` | container/shape hygiene, no sys.path reach-ins | yes | report-only |
| `ci_vacuous_assertion_check.py` | VACUOUS-ASSERTION detector (CLAUDE.md §0.1 pt 2 literal encoding) | yes | report-only |
| `compliance_check.py` | working-tree size-cap scan | yes | **blocking** (own job `compliance-check`) |
| `ci_golden_modes_check.py` | golden-mode byte-exact gate, FIELD_PINS single owner | yes | **blocking** (own job `field-goldens`) |
| `valoria_local.py` | local pre-commit accelerator, mirrors CI's blocking list | local hook only (`.githooks/pre-commit`), not CI itself | — |
| `hook_naming_guard.py` | edit-time naming nudge | `.claude/settings.json` PreToolUse hook | not CI |
| `hook_md_sweep_guard.py` | edit-time `.md` sweep guard | `.claude/settings.json` PreToolUse hook | not CI |
| `balance_oracle.py` | n≥100 campaign balance instrument (deliberately NOT a CI gate, 240 campaigns ≈13 min) | **NO** | — |
| `export_sim_params.py` | typed values layer (ED-IN-0079) | not directly in workflow; 1 test caller | **NO** |
| `build_contract_index.py`, `build_engine_atlas.py`, `build_execution_map.py`, `build_key_graph.py`, `build_identifier_census.py`, `build_fork.py` | generated-artifact builders, run on-demand / from test fixtures | **NO** direct CI invocation | — |
| `contract_runtime_conformance.py` | runtime-conformance instrument (measures the engine without perturbing it) | **NO** | — |
| `definitions_store.py`, `descriptor_registry.py`, `quantity_registry.py`, `registry.py`, `tag_normalizer.py`, `vocab_store.py`, `names.py`, `pathres.py`, `link_values_pointers.py` | registry/reader facades, imported by other tools/tests, not invoked standalone in CI | **NO** direct CI step (used as libraries) | — |
| `evacuation_plan.py` | keep/relocate/evacuate partition classifier (ED-IN-0128) | **NO** | — |
| `gen_sigma_parity_goldens.py` | golden generator | **NO** (on-demand) | — |
| `join_audit_workings.py` | joins audit working-papers for purge | **NO** | — |
| `trace_execution_phases.py` | phase tracer | **NO** | — |
| `campaign_output_probe.py` | byte-identity control for behaviour-neutral changes — **zero test/hook references found** | **NO** | — |
| `triage_work_items.py` | classifies editorial-ledger rows by whether they concern CODE (Jordan, 2026-08-24) — **zero test/hook references found** | **NO** | — |
| `ci_common.py` | shared primitives (repo root, lane roster, token estimate, id regexes) — imported, never invoked standalone | library only | — |

**Zero-automated-caller candidates found in this pass:** `campaign_output_probe.py` and
`triage_work_items.py` had zero matches in `tests/valoria`, `.githooks`, or `.claude` — consistent
with CLAUDE.md §3's historical measurement ("36 of 106 modules have zero automated callers", now
stale given culling waves 1-5, but the *pattern* — instruments built for one session's manual use
and left uninvoked thereafter — recurs). `balance_oracle.py` and `export_sim_params.py` are
deliberately on-demand/manual per their own docstrings, not defects.

---

## 6. CI — every job, blocking vs report-only

From `.github/workflows/valoria-ci.yml` (full read). Enforcement model per the file's own header
comment: **CI is the ONE authoritative tier**; the local `.githooks/pre-commit` + `.claude/settings.json`
hooks call the same validators for fast feedback but are explicitly non-authoritative (bypassable
with `--no-verify`).

| job | blocking? | what it runs |
|---|---|---|
| `syntax-check` | **blocking**, gates everything else via `needs:` | `py_compile` over every `.py` under `tools/` via `find`+`xargs` (globbed since G9, no hand-maintained roster) |
| `validators` | **blocking** | ~20 validators in sequence inside one job (collapsed 2026-08-01 from 25 jobs — 29/31 nodes did 5.17s total compute, wall clock was runner boot, not work); no fail-fast, `exit $fail` at the end so every failure is reported in one pass |
| `validators-report` | **report-only** (`continue-on-error: true`, `exit 0` always) | `m1_acceptance.py --summary` (the one game-subject signal remaining in CI after `review_core.py`'s 2026-08-21 retirement), `ci_naming_check.py --warn`, `currency_consistency_check.py`, `ci_quantity_vocabulary_check.py`, `mechanics_index_gen.py --strict`, `ci_generation_consistency.py`, `canon_coverage_check.py --strict --json`, `ci_module_shape_check.py`, `ci_vacuous_assertion_check.py` |
| `contract-conformance` | report-only (`continue-on-error: true` at step level) | `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py` against `module_contracts.yaml` + key-type registry + canonical sources; ~21 pre-existing violations / ~64 warnings tolerated as a known backlog |
| `unit-tests` | **blocking** | `pytest tests/valoria -q -n auto` (measured 3.02× speedup over serial, same pass/fail/skip counts — the control that separates "faster" from "ran less"); needs full git history (`fetch-depth: 0`) for `test_forked_status.py`'s 242 FORK-row `git cat-file -e` checks |
| `sim-regression` | **blocking** | `pytest engine/tests -q`, serial (byte-exact goldens, `-n auto` would race the seeded oracle); 20-min cap, measured ~6m15s real runtime (raised from a 5-min cap that had silently killed the job on every run since the mass-battle port, misreported as `cancelled` not `failure`) |
| `field-goldens` | **blocking** | `ci_golden_modes_check.py` — the two FIELD_MOVEMENT grid-mode byte-exact goldens (previously sat red 5 days undetected before this job existed) |
| `lanchester-signature` | **report-only** (`|| true`) | the mass-battle engine's own attrition-law instrument; deliberately non-blocking because the repaired instrument legitimately fails today (melee fits p≈3.20 against a ≤1.4 bar — an unresolved engine-vs-design-target fork) |
| `compliance-check` | **blocking** | `compliance_check.py --check-only --repo-state .` (working-tree size caps); needs full history for the same reason as `unit-tests` |
| `ci-summary` ("All Gates Green") | the single required branch-protection check | asserts `needs:` on `syntax-check, validators, unit-tests, sim-regression, field-goldens, compliance-check` all report `success`; **`validators-report`, `contract-conformance`, `lanchester-signature` are NOT in this list** — they can fail freely without redding main |

---

## 7. ⭐ THE M1 BOARD — every juncture, its `state:`, and whether it RUNS

From `workplans/workplan_v6_progress.yaml` (`as_of: sha c75c561, date 2026-08-19`) and
`tools/m1_acceptance.py --summary` (executed live this pass, confirmed read-only first).

| n | juncture | owner | `state:` | what it requires per its own `next:` text |
|---|---|---|---|---|
| 1 | Strategic decision | FA | `not_started` | fractional-dice half DONE 2026-08-21; score/2 half SUSPENDED by Jordan (would overwrite ratified canon / collapse Tribunal's two-tier halving) |
| 2 | Domain action | IN | `not_started` | `DomainActionSystem.gd` exists in valoria-game and runs 3 phases; needs verification against the FA sim + a `module_contracts.yaml` [ASSUMPTION]-grade contract record — authoring the design doc explicitly does NOT close this |
| 3 | Social contest | SC | `blocked` | HARD-blocked on 3 rulings, `needs_jordan: true` verified directly against `editorial_ledger_sc.jsonl` (ED-SC-0003/0004/0005 — Piety/Persuasion name collision, canonical Argue-pool formula, bonus-die cap) |
| 4 | Personal combat | PC | `in_progress` | Resume R3 U-series against `combat_completion_plan_v4.md` v4.1; `core.py`'s degree site deliberately held out of the unified ladder |
| 5 | Thread operation | WR | `in_progress` | ED-WR-0001/0002 are prose-only edits that do NOT close the juncture under §0.2; ED-1010/1011 carry `jordan_decision: pending` |
| 6 | Season close | IN | `in_progress` | emitter missing (`GameDirector.gd` calls `advance_season()` but emits neither `mechanical.accounting` nor `mechanical.season_change`); consumer already built and tested |
| 7 | Articulation render | IN | `in_progress` | `ArticulationLayerV30.gd` exists, 818 lines, wired to the Key bus; its trigger match handles 10/N key types and silently drops `scene.battle_concluded`/`scene.investigation_resolved` |

**Tally: 0 done · 4 in_progress · 2 not_started · 1 blocked — 0/7 execute.** This matches
`m1_acceptance.py`'s row 4 exactly (see below).

**`m1_acceptance.py --summary` live output, this session:**

```
● Stub invocations on the M1 path == 0                    2  FAIL
    1-season probe (seed=20260819): 2 stub_resolve call(s) during the run
● Same seed -> same KeyLog.content_hash()          641aa8c55c3e…  PASS
◐ Every emitted key has a consumer or declared terminal        —  PARTIAL
    47 emitted · 0 declared terminal · 2 unconsumed by name (env.crisis, mechanical.season_change)
● All M1 junctures execute                              0/7  FAIL
    blocked: 1 · in_progress: 4 · not_started: 2
    ⚠ DOC-DERIVED: counts `state: done` in workplan_v6_progress.yaml, not execution.
    Editing the board greens this row — unlike rows 1-2.
○ N seeds, zero invariant violations                      —  BLOCKED
    unblocked by: property-based tests (Hypothesis) over a season run

verdict: NOT MET  —  2 row(s) failing
```

**Per CLAUDE.md §0.2's own qualification** (`CLAUDE.md`, §0.2, "the instrument is not yet
uniformly execution-bound"): rows 1-2 genuinely execute the engine (a seeded `mc_v18` probe +
same-seed `KeyLog.content_hash()` comparison) and are the only rows a document edit cannot satisfy.
**Row 4 is explicitly flagged DOC-DERIVED by the tool's own output** — it counts `state: done`
strings on the hand-edited board, so editing seven board rows would green it without a single
execution artifact changing. Row 3 is genuinely PARTIAL (a static contract check, not a run) and
row 5 is genuinely BLOCKED (no property-sweep harness exists yet). **The verdict `MET` is currently
structurally unreachable** — 2 of 5 rows fail on measured evidence, independent of row 4's honesty
problem.

---

## 8. ⭐ THE EXECUTION VERDICT

| design claim | executable today? | against what | what is missing |
|---|---|---|---|
| Twelve-act closed vocabulary (`carry`/`compose_agenda`/`transfer`/`commit`/`requisition`/`investigate`/`confer`/`revoke`/`issue`/`determine`/`dispatch`/`convene`) | **NO** | No Python module implements any of these names; the closest live analogues (Muster/Govern/Conquest/Excommunication/Censure/Parliamentary-Transfer) exist as separate, differently-shaped functions in `systems/factions/sim/`, not under one generalised verb dispatch | A single `Act`-typed dispatcher; the twelve acts have no shared call signature in code today |
| `choose : (Person, View, Sensation) -> Act` (no World) | **NO** | Nothing — no `Person`, `View`, or `Sensation` type exists in `engine/` or `systems/` | The types themselves, plus the enforcement mechanism (the design's own commit history records this guarantee was found unenforceable in GDScript and downgraded to "explicit World param, fails at call site") |
| `resolve : (Act[], World) -> Event[]` (no Person) | **PARTIAL, by analogy** | `engine/substrate/keys.py`'s `Key`/`KeyLog`/`TickScheduler` is the nearest existing analogue — typed, validated, append-only, replay-deterministic (`test_key_substrate.py`) | `Act`/`Event` types don't exist; would need to be built as a specialisation of, or a replacement for, the Key substrate |
| `witness : (Person, Event) -> Claim[]` (per-person, never a collection) | **NO** | Nothing — `engine/substrate/`'s Key delivery is direction-neutral fan-out to `targets[]`, not a per-observer divergent `Claim` production | A new resolver stage; the closest thing to "disagreeing witnesses" in the corpus is the design's own §7 note that `articulation.subscribe_all`'s 13 callbacks are all no-ops |
| Six loop steps (CALENDAR/MATTER/DELIBERATE/RESOLVE/WITNESS/CENSUS) | **NO**, partial precedent only | `engine_clock.py`'s three-phase `season_tick → action → accounting_boundary` (live, `test_engine_clock_phases.py`) is a coarser, differently-named ancestor | A CENSUS barrier and a WITNESS-as-global-step have no code counterpart; the design's own commit log records the barrier count moved from 3 to 4 mid-revision because of "individuation moves envelope weight" and "de-individuation was order-dependent" — i.e. this was found non-trivial even at the design-prose level |
| Person/Rung/Office/Site carriers, one Tenure edge | **NO** | `engine/autoload/game_state.py`'s `Faction`/`Territory`/`Settlement` classes and the (empty, INERT) `NPC` dataclass are the nearest existing carriers, and none map cleanly — `Rung` (a 0-7 standing ladder per the integration master) is DESIGNED with zero code (`faction_politics_v30.md`, integration master `:52`); `Tenure` (governor/office holding) is the same `succeed_governor`/`governor_id` pair the integration master already found INERT with zero callers | The four carriers and the edge type; `test_engine_does_not_import_systems.py`'s pattern (subprocess-import assertion pinned at zero) is the right template for enforcing "engine/ names no subsystem" once these carriers land, but nothing currently targets them |
| The two-thirds of the action catalogue not in the twelve-act table (personal combat, social contest, threadwork, mass battle) | **N/A — not addressed by the design docs read** | These subsystems execute today largely independent of the faction/settlement layer the twelve-act table targets | Whether/how they route through `contest`/`verbs` per `03_COMPENDIUM.md §9b`'s function table is not stated in the read files |

**Bottom line, per §0.2's own test ("does the behaviour execute, and did something run it"):**
**nothing in the `proposals/2026-08-31-ideal-v2/` suite executes.** Every one of its core objects
— `Person`, `Rung`, `Office`, `Site`, `Tenure`, `Query`, `Act`, `Event`, `Claim` — is absent from
`engine/` and `systems/`. The nearest existing harnesses that a future implementation would need to
satisfy are `test_engine_does_not_import_systems.py` (the no-World enforcement pattern),
`test_key_substrate.py` (the append-only/replay-deterministic contract `resolve`/`Event` would
inherit if built on the Key substrate), and `test_morale_write_sweep.py` (the write-sweep-guard
pattern for whatever field ends up owning `Tenure`'s mint/alter/efface state). None of the four
structural tests the design names (§4 above) have a harness today.

---

## 9. DUPLICATION

- **The integration master's Proposal 4 ("A Person's Season") and Unification move U-3 are the
  direct, uncited architectural ancestors of ideal-v2's Person/Rung/Office/Tenure design.** Neither
  `valoria_systems_integration_master_v1{,_part4}.md` nor `valoria_game_precedent_companion_v1{,_part4}.md`
  is referenced anywhere in `proposals/2026-08-31-ideal-v2/{00_INDEX,01_ARCHITECTURE,02_THE_SEASON_LOOP,03_COMPENDIUM,04_GODOT_IMPLEMENTABILITY}.md`
  (checked by grep for the two filenames' stems across all five files — zero hits). The design
  independently re-derives "no decision function can see the world," a person-centred act model,
  and a NERS-shaped concern about pool/action-count scaling — all of which the two research docs
  already worked through in detail, with citations, dates, and NERS math, three days earlier
  (research docs dated 2026-08-27/28; ideal-v2 dated 2026-08-31).
- **U-4's finding is the single most load-bearing uncited fact.** The precedent companion's
  sharpest result — Valoria's own Ω-clause defines itself *against* Mount & Blade's
  faction-politics/combat isolation, and the corpus currently sits exactly where M&B sits (one
  reachable crossing, default-off bridge) — bears directly on whether a Person-centred redesign
  actually closes that gap or merely relocates the same isolation into new object names. The
  ideal-v2 suite's own commit history (PR #344's WIP entries) shows it wrestling with an adjacent
  but differently-framed question (the containment tree, tenure over sites) without ever landing on
  U-4's framing.
- **The action catalogue's investigation-action collision (§2 above) was caught internally**, by
  the design's own adversarial review (PR #344), not by cross-referencing `research/`. The
  catalogue itself was landed by PR #336-338, and its existence as the authoritative six-act
  investigation list was rediscovered from `03_knowledge_telling_investigation.md` rather than from
  `cross_scale_action_catalogue_v1.md` directly — both sources agree, but the design's own commit
  log (`f129ca7`'s WIP entries) records **108 of 123 proposal documents over 200 lines cited nowhere**
  across the superseding design, its review, and this suite — a coverage limit the design's own
  index now states at the top per its 2026-08-31 commits. `research/` (as opposed to `proposals/`)
  was outside even that self-audited 123-document set, so this lane's finding (zero citation of the
  two `research/` masters) is consistent with, and sharpens, that self-reported gap.
- **Within `research/` itself**, the integration master's own §1.2/F7 already document duplication
  it found in its OWN sources (~30 duplicate pairs between the governance compendium and
  `rise_to_power_roster_system_research_v1.md`; ~10 more within `research/governance/`) — this is
  pre-existing, not something this pass adds.

---

## 10. GAPS — no test, no tool, no board row

- **The four carriers (Person/Rung/Office/Site) and the Tenure edge** have no test file, no tool,
  and no M1-board row. The closest board row (juncture 1, "Strategic decision", `not_started`) is
  about the score/2 obstacle-derivation ruling, not about a person/office model.
- **The twelve-act closed vocabulary's coverage of personal combat, social contest, threadwork, and
  mass battle** is unaddressed by the read design docs (§8) and has no board row asking the
  question either.
- **The design's own four structural tests** (§4) have zero code, zero harness, and are not named
  in any `tests/valoria/` file, any `tools/` module, or any `workplans/` row.
- **`campaign_output_probe.py` and `triage_work_items.py`** (§5) are apparatus with no test and no
  CI wiring — not directly relevant to the design's execution status, but they are exactly the
  "finished machinery with no caller" pattern the integration master's F1-F3 describe at scale
  (13-15% of the whole corpus), reproduced here at tool-scope.
- **The `investigate` act's post-#344 resolution** (that it now names six existing acts rather than
  a seventh invented one) has no test asserting the twelve-act table and the six investigation acts
  actually agree in code — because neither exists in code. This is a documentation-level
  reconciliation only.

---

## 11. Claims to escalate

- **Whether the twelve-act table in `03_COMPENDIUM.md:781-783` is meant to be exhaustive of ALL
  player-facing acts, or only of the faction/settlement-governance slice** — the read files never
  state this, and the omission of personal combat, social contest, threadwork and mass battle from
  that table is either a deliberate scope boundary or an unstated gap. Given CLAUDE.md §0.05's
  "code is the mechanism," this is answerable in principle by checking whether `03_COMPENDIUM.md`'s
  §9b function table (`contest`, `verbs` rows) is meant to subsume those subsystems — but that
  requires reading `01_ARCHITECTURE.md`/`02_THE_SEASON_LOOP.md` in full, which was outside this
  lane's assigned scope (research/tests/tools/workplans/CI). **Flag for the lane reading
  `01_ARCHITECTURE.md`/`02_THE_SEASON_LOOP.md`/`03_COMPENDIUM.md` directly.**
- **Whether the ideal-v2 authors were aware of `research/valoria_systems_integration_master_v1*.md`
  and `valoria_game_precedent_companion_v1*.md` and chose not to cite them, or genuinely did not
  read them.** The zero-citation finding (§9) is measured, not the cause. Given the design's own
  self-audited coverage-limit disclosure (108/123 proposal docs uncited), and that `research/` is a
  different top-level directory from `proposals/` entirely, the likelier explanation is a scope
  boundary the design's index never states for `research/` specifically — worth a direct question
  to whoever ran the ideal-v2 synthesis pass, since Proposal 4 and U-3/U-4 would have changed the
  design's own self-assessed risk profile (U-4 in particular, on the M&B isolation question).
