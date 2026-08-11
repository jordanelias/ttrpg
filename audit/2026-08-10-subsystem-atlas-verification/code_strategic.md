# Strategic-scale code trace (independent re-derivation, reading-only, no grep)

Scope read whole: systems/factions/sim/*.py (17 files incl. __init__), systems/settlements/sim/*.py
(7 files incl. __init__), engine/cross_scale/parliamentary_bridge.py. No `*_flow_skeleton_v1.md`
opened.

## 1. faction_take_action control flow — RULING

**Ruling: single stochastic draw over reweighted candidates. There is NO unconditional mandatory
action pass before the draw.** (`systems/factions/sim/faction_action.py:177-242`)

Sequence:
- Lines 191-196: four RNG-free state signals computed (`has_target`, `mil_adv`, `deficit`, `threat`).
  These consume no RNG (explicitly documented and true on reading).
- Lines 198-212: signals turn into multipliers on the four BASE_W_* prior weights, then the four
  weighted values are renormalized to sum to 1.0. This is arithmetic reweighting, not a branch.
- Lines 214-218: cumulative thresholds built from the reweighted probabilities.
- Line 220: **the only RNG draw**, `roll = rng.random()`.
- Lines 223-242: dispatch against `roll` — see §2.

Nothing here inspects `threat`/`mil_adv`/`deficit` to force a branch outright; they only bias which
bucket `roll` is likely to land in. A faction under proximate threat (`threat=1.0`) still has a
`w_unique` share fixed at `BASE_W_UNIQUE` (never itself reweighted) and can still roll into Govern.
This is **exactly** "a single stochastic draw over reweighted candidates," not a mandatory-then-
stochastic two-phase process.

**Docstring disagreement, several places, same claim:**
- `faction_action.py:180` — function docstring: "GD-2: mandatory threat-response before stochastic
  selection."
- `faction_action.py:184` (continuing) restates the *actual* mechanism correctly (reweight-then-draw)
  in the same docstring, immediately contradicting its own opening line.
- `excommunication.py:8` — module header: "Game Design constraints applicable: GD-2 (mandatory-
  before-stochastic action selection)."
- `tribunal.py:5`, `council_solmund.py:5`, `absolution.py:8` — all cite "GD-2" similarly (Church
  faction-unique action / status-flag enforcement), reinforcing that the tree's shared understanding
  of GD-2 is "mandatory-before-stochastic," a phrase the actual dispatch code does not implement.
- `excommunication.py:200-202` (`select_excommunication_target` docstring) explicitly calls itself a
  "GD-2 mandatory threat-response candidate" while noting "current strategic AI is stochastic" — the
  module's own author flags the gap between the GD-2 label and the stochastic reality.

Net: the "mandatory" framing appears to be residual language from before ED-FA-0012 (which replaced
a fixed 30/35/20/15 draw with a *reweighted* draw — still a draw, never a forced pass) and was never
corrected across the docstrings that cite it.

## 2. Ordered dispatch, and fallthrough semantics

Order tested, in source order (`faction_action.py:223-242`):
1. **Faction-unique** (`if roll < cum_unique`) → `_try_faction_unique`
2. **Conquest** (`if roll < cum_conquest`) → `_try_conquest`
3. **Muster** (`if roll < cum_muster`) → `_try_muster`
4. **Govern** (final line, unconditional) → `_try_govern` (fallback, unconditional `return`)

**Structural finding, not obvious from a skim:** these are three *independent* `if` statements, not
`if/elif/elif`. Because `cum_unique < cum_conquest < cum_muster` by construction (cumulative sums of
non-negative weights), `roll < cum_unique` implies `roll < cum_conquest` implies `roll < cum_muster`.
So when the unique slot is entered (`roll < cum_unique`) and `_try_faction_unique` returns `_NOOP`,
control does not merely "fall through to Conquest" (as the inline comment at line 227 says) — it
falls through the *entire remaining chain*: the Conquest `if` is also true, and if `_try_conquest`
also returns `_NOOP`, the Muster `if` is also true, and if `_try_muster` also returns `_NOOP`,
execution reaches the final unconditional `return _try_govern(...)`. The same cascade applies
starting from any bucket: a roll landing in the Conquest bucket that NOOPs still falls through to
Muster then Govern; a roll landing in the Muster bucket that NOOPs falls through only to Govern.
Only a roll landing in the Govern bucket has nowhere further to cascade (it's already the target).

**The top-level function's return is not guaranteed to be a real action descriptor.** The final line
is `return _try_govern(faction, world, rng)`, with no check of the result against `_NOOP`. But
`_try_govern` (line 533-534) itself returns `_NOOP` ('invalid') when `faction.territories` is empty
or ownership mismatches. So a landless faction (all four buckets NOOP) causes
`faction_take_action` to return the literal string `'invalid'` as if it were a normal
`f'Govern:{deg}'`-shaped dispatch string — every earlier `_try_*` checks for `_NOOP` and reports it
via fallthrough, but the last link in the chain does not.

Unique-slot internal structure (`_try_faction_unique`, lines 245-270): tries
`_faction_specific_unique` first (Crown's 3-mode selector; Church's Excommunication→Council→
Absolution priority chain; Varfell/Hafenmark always `_NOOP` — confirmed by reading their stub files,
§4). If that's `_NOOP` and the faction is parliamentary, falls through to a universal Parliamentary
Censure attempt (`parliamentary_action.propose_censure`) before finally returning `_NOOP` up to
`faction_take_action`.

## 3. systems/settlements/sim/ — populated / read / never touched

**Populated at world-gen** (`registry.py:215-266`, `populate_from_geography`): reads
`valoria_geography_v30.yaml`, and for each entry constructs a `Settlement` with only `sid`, `name`,
`stype` (validated against `LEGAL_TYPES`), `province_id`, `owner_faction`, `prosperity`, `defense`,
`order`. Every other `Settlement` dataclass field is left at its class default (see next paragraph) —
the function's own docstring (lines 236-239) says as much.

**Read during a season** (within scope):
- `adjacency.ADJACENCY` — read constantly by `faction_action._conquest_targets` and
  `_threat_signal`.
- `registry.get_settlement` — read by `settlement.compute_settlement_state`'s registry-backed path.
- `registry.province_members` — read by `settlement.aggregate_to_province`'s registry-backed path.
- `infrastructure.count_infrastructure` / `seizure_ob_modifier` — read by `mass_seizure.py` (itself
  unreachable in production, see §4) and `settlement.py`'s indirect calls are absent; only
  `mass_seizure` reads these in the files I traced.
- `Territory.templar` (game_state, out of scope) is read as a *seed* by
  `infrastructure._get_or_create`/`count_infrastructure` when the per-territory infra store has no
  entry yet — a fallback path, not the primary store.

**Declared but never touched anywhere in this scope** (confirmed by reading every file, not by
absence-of-grep-hit):
- `Settlement.legitimacy` / `Settlement.popular_support` — the file's own comment
  (`registry.py:69-72`) states this outright: "declared but NEVER READ OR WRITTEN anywhere in sim/…
  an INERT LPS-1 schema stub." Independently confirmed: no assignment or read of `.legitimacy` /
  `.popular_support` in any file read for this trace.
- `Settlement.religious_building` (default `"None"`, `registry.py:81`) — never set by
  `populate_from_geography`, never read by `infrastructure.py`'s *separate* per-territory
  `InfrastructureState.religious_building` (a different store entirely — `_infra_store` /
  `world.territory_infrastructure`, keyed by territory_id, not by Settlement). Two same-named
  fields, two disconnected stores; the Settlement-side one looks inert (see §4).
- `Settlement.governor_id`, `.facility_tier`, `.suspicion`, `.pressure`, `.active_directive`,
  `.church_attention`, `.governor_emergence`, `.subnational`, `.npc_ids`, `.ledger`, `.open_needs`,
  `.deck_state` — all left at dataclass default by `populate_from_geography`; no other writer found
  in this scope. `Settlement.ap` (the `@property`) and the ledger convenience methods
  (`add_tag`/`has_tag`/`tags`) and `succeed_governor` are all defined but I found no caller within
  the traced files.
- `temperaments.py`'s `temperament_modifiers` and `apply_strain_shock` — both fully implemented, but
  no file in `systems/factions/sim/` or `parliamentary_bridge.py` calls either. (Their existence is
  referenced only in `varfell_territorial_acquisition.py`'s dependency-list *comment*, and that
  module is an unconditional stub — see §4.)

## 4. Declared-but-doesn't-happen inventory (file:line)

1. **`systems/factions/sim/faction_action.py:180` vs `:184-190`** — docstring self-contradiction:
   opens "GD-2: mandatory threat-response before stochastic selection," then describes (correctly)
   a reweight-then-single-draw mechanism. See §1.
2. **`systems/factions/sim/faction_action.py:223-242`** — `return _try_govern(...)` at the very end
   is unconditional and unchecked against `_NOOP`; a landless faction causes the whole function to
   return the sentinel `'invalid'` rather than a real dispatch string. See §2.
3. **Six unconditional stub modules — every call always resolves to `stubwire.stub_resolve` (a
   typed no-op), regardless of arguments:**
   - `hafenmark_equipment.py:30-35` (`apply_hafenmark_equipment`)
   - `infrastructure_reclamation.py:29-34` (`compute_reclamation_bonus`)
   - `varfell_mandate_action.py:40-46` (`attempt_mandate_action`)
   - `varfell_territorial_acquisition.py:42-48` (`attempt_territorial_acquisition`)
   - `charter_liberties.py:27-32` (`attempt_charter`)
   - `home_sanctuary.py:29-42` (`t9_invasion_modifier`, `check_sanctuary_active`)
   - `treaty.py:99-118` (`propose_treaty`) — same pattern, one function in an otherwise-live module.
   - `tribunal.py:143-162` (`run_tribunal`) — same pattern; sibling
     `run_excommunication_tribunal` is live.
   Confirms in-code, independent of any doc, that Varfell and Hafenmark truly have no faction-unique
   action path — matches `faction_action.py:315-318`'s comment.
4. **`systems/factions/sim/mass_seizure.py`** — fully implemented (declaration probability,
   per-territory resolution, ownership transfer) but **never imported or called** by
   `faction_action.py`, `parliamentary_bridge.py`, or any other file read in this scope. Confirmed by
   reading every file's import list; only `mass_seizure.py` itself references its own functions.
   `parliamentary_transfer.py:132-135`'s comment independently states the same conclusion
   ("UNREACHABLE. Zero production callers").
5. **`systems/factions/sim/treaty.py:46`** — `TREATY_CONSENT_RATE_DEFAULT = 0.28` is declared and
   commented as canonical, but no function in the file reads it (`process_treaty_expirations` only
   takes/uses `lapse_rate`, defaulting to `TREATY_LAPSE_RATE_DEFAULT`, a different constant).
6. **`systems/factions/sim/crown_initiative.py:193-208`** (`coronation_renewal_prereq`) — docstring
   says "We do block when Crown is BOTH excommunicated AND the Church just attempted to
   excommunicate this same season" but the function body only checks `church is None or not
   church.parliamentary`; the described same-season-block condition is not implemented (the same
   docstring's parenthetical admits "deferred," but the sentence is phrased in the present tense as
   if implemented).
7. **`systems/settlements/sim/registry.py:69-72`** — `Settlement.legitimacy` /
   `.popular_support` declared, self-documented as never read or written anywhere in `sim/`.
   Independently confirmed by reading. See §3.
8. **`systems/settlements/sim/registry.py:81`** — `Settlement.religious_building` field is a
   same-named but functionally disconnected duplicate of `infrastructure.InfrastructureState
   .religious_building` (separate store, separate keying convention); the Settlement-side field is
   never set by `populate_from_geography` (`registry.py:215-266`) and I found no other writer/reader.
9. **`engine/cross_scale/parliamentary_bridge.py:190-191`** — `run_parliamentary_scene` is a
   default-off flag pattern: `if getattr(world, "echo_scheduler", None) is None: return {"resolved":
   False, ...}` — the entire vote-derivation, vote resolution, and echo composition are skipped
   whenever `echo_scheduler` isn't attached (documented default OFF = byte-exact; confirmed
   structurally: the early return precedes any state mutation).
10. **`systems/factions/sim/faction_action.py:436`** — `terrain=None` passed into
    `resolve_mass_battle` with an inline comment `[GAP: terrain modifiers deferred to Phase 7
    follow-on Steps 2-9]` — a parameter position permanently fed a placeholder value in this caller.
11. **`systems/settlements/sim/temperaments.py`** — `temperament_modifiers`/`apply_strain_shock` are
    fully implemented but have no caller anywhere in the traced scope (see §3). Not proven dead
    globally — only within this scope's reading.

## 5. What surprised me

- The non-`elif` cumulative-threshold cascade (§2 finding 2) — on first read it looks like a normal
  weighted-bucket dispatch, but because the three `if`s are independent and thresholds are
  monotonically increasing, an unavailable action doesn't just defer to "the next" bucket, it can
  cascade all the way to the unconditional Govern fallback, and even Govern isn't guaranteed to
  succeed (a landless faction returns the literal `'invalid'` sentinel as the whole function's
  result). None of the several docstrings describing this dispatch mention that fallthrough
  compounds past one step.
- How consistently the "GD-2 = mandatory-before-stochastic" phrase recurs across five separate
  module headers (`faction_action.py`, `excommunication.py`, `tribunal.py`, `council_solmund.py`,
  `absolution.py`) while the only code that actually implements a dispatch (`faction_action.py`)
  never enforces anything mandatory — it's a shared, uncorrected label rather than an isolated typo.
- `Settlement.religious_building` and `InfrastructureState.religious_building` being two same-named,
  same-conceptual-purpose fields living in two entirely separate, non-communicating stores
  (`registry.py`'s per-Settlement dataclass vs `infrastructure.py`'s per-territory
  `_infra_store`/`world.territory_infrastructure`) — a naming collision that reads as one system
  from either file alone.
- The sheer number (8) of `stubwire.stub_resolve` modules in `systems/factions/sim/` — nearly half
  of the 17 files in that directory are unconditional stubs, all converted from
  `raise NotImplementedError` in the same pass (OI-17/ED-IN-0091), all carrying real canon citations
  and entry-point signatures as if implemented.
- `mass_seizure.py` being a fully-realized, non-trivial implementation (probabilistic declaration
  curve, per-territory Ob computation, ownership transfer) that is nonetheless wired to nothing —
  the *opposite* failure mode from the stub files (those declare-and-don't-implement; this
  implements-and-doesn't-wire).
