# Dossier — Arc-Register Formalizability (Lane: arc-register formalizability)

## Status: PROPOSED (design-effort working notes — Jordan-vetoable)
_Sonnet lane, 2026-07-05, verified against working tree only._

## Method note

Read `00_grounding/00_engine_charter.md` (full), `00_grounding/01_arc_corpus.md` (full). Then read
**all five** `references/arcs/*.md` files in full (549 lines total — the corpus is small enough
that "sample ~15" became closer to a full read: `arc_register_clocks.md` §I (7 arcs), all of
`arc_register_threads.md` §II (8 arcs), all of `arc_register_territory.md` §IV (27 TE entries,
tiers 1-3), all of `arc_register_events.md` §V-VI (5 BG-CV + 8 COLLISION A-J), and all of
`arc_register_factions.md` §III (the 87-entry bulk file, Crown/Church/Varfell/Hafenmark/
Löwenritter/Restoration Movement/Guilds/crime-underground/Schoenland/Wardens tiers). Cross-checked
against `designs/architecture/key_type_registry_v30.md` (full), `references/module_contracts.yaml`
(targeted grep + read of `faction_state`/`npc_behavior` blocks), `designs/provincial/
clock_registry_v30.md` (Shared Clocks + Track tables), `references/mechanical_terms_index.md`,
`references/deprecated_terms_registry.yaml`, `params/factions_personal.md`, `designs/npcs/
npc_roster_v30.md`, and `canon/editorial_ledger.jsonl` (ED-416 lookup).

---

## 1. Can each arc compile to a typed vector?

**Yes, structurally — but three classes of blocker recur often enough to be load-bearing, not
edge cases.** The register's own anatomy (`01_arc_corpus.md` §a: "trigger condition(s) → mechanical
effects with exact stat deltas/thresholds → closing Direction: sentence") already has the shape of
`trigger -> pressure_effects -> payload.direction`; what it lacks, corpus-wide, is (1) a queryable
**per-arc-vector lifecycle/state field** outside the NPC-scoped case, (2) resolution of **two
renamed-but-still-legacy-named clocks** (TC, RS) and **one struck-and-unmigrated mechanic** (Coup
Counter), and (3) a handful of **entirely unauthored referenced mechanics** (Southernmost Ritual)
and **dangling IDs** (ARC-T04) that block specific triggers regardless of schema quality.

---

## 2. Candidate typed schema (pseudo-YAML)

```yaml
arc_vector:
  id: string                        # ARC-S07 | TE-01 | BG-CV-01 | COLLISION-C | NPC-ARC-STR
  tier: enum[S, T, P, TE, BG-CV, COLLISION, NPC-ARC]   # per 01_arc_corpus.md §a ID scheme
  scope:
    faction: [faction_id] | ALL
    territories: [territory_id] | ALL
    mode: enum[TTRPG, BG, ALL, Hybrid]        # register's header triple, verbatim
  activity_mode: enum[
    level_triggered,        # active while map/stat condition holds, no lifecycle (most TE-##)
    edge_triggered_once,    # one-time BG-CV / threshold fire
    edge_triggered_retryable,  # e.g. ARC-T03 Excommunication ("Retryable")
    clock_escalation,       # multi-stage vector with real lifecycle (ARC-S07-shaped)
    convergence             # second-order: fires over OTHER arc-vectors' state (COLLISION A-J)
  ]
  trigger:
    predicate: [
      { field: <clock|stat|npc_track|arc_state>.<path>,
        op: enum[">=","<=","==","flip","consecutive_seasons_true","count_true_of_n","AND","OR"],
        value: number | enum | ref-to-another-arc_vector.id }
    ]
    resolves_via: <dice_pool|deterministic_accounting|state_reader|manifest|null>  # module_contracts
                                                                                    # resolver taxonomy
    temporal_window: <same_season|within_n_seasons|unspecified>   # charter Q3 "temporal windows"
                                                                    # correlation-test dimension —
                                                                    # COLLISION entries never state this
  pressure_effects:
    - { target: <clock|stat|npc_track>.<path>, delta: signed_number | formula_string,
        cadence: enum[season, immediate, per_attempt, one_time], condition: optional_guard }
  payload:                          # internal-only per C2 — never renders as a label
    direction: string                # the register's "Direction:" sentence, verbatim citation
    participating_actors: [actor_id]
    stakes_tags: [enum: gating, pricing, foreclosure, pattern_response, none]
    ledger_cause: [PP-NNN | ED-NNN]   # Q2: "every gate cites its ledger cause"
  lifecycle:
    states: [seeded, active, escalating, converging, resolved, dormant, abandoned]  # Q3 taxonomy
    terminal: bool                   # false for level_triggered (active/inactive only)
  cross_refs: [arc_vector.id]        # collision-eligibility surface
  gaps: [ { type: enum[missing_clock, missing_field, missing_mechanic, struck_mechanic,
                       gm_judgment, open_number, dangling_id, stale_citation],
            note: string, cites: [file:section] } ]
```

---

## 3. Classification of sample + whole-register estimate

**Sample (representative, spans all 5 files + all tiers):** ARC-P01, P02, P03, P04, P05, P06, P07
(all 7 clock vectors), ARC-S04, S15, S32 (thread), ARC-S07, S14, S23, S29, S35, S52, T02, T13
(faction/Crown+cross-tier), NPC-ARC-STR, TE-01, TE-04, TE-08, TE-15, TE-28 (territory), BG-CV-01,
BG-CV-04, BG-CV-05 (events), all 8 COLLISION A-J.

| Class | Sample examples | Why |
|---|---|---|
| **Fully machine-checkable now** (after trivial rename-resolution) | ARC-P01 (TC→CI), ARC-P02 (RS→MS), ARC-P07, ARC-S04, ARC-S32, TE-01, TE-08, TE-28, BG-CV-01, BG-CV-04, COLLISION-E, COLLISION-J | Trigger predicates resolve entirely to canonical clocks/stats already in `clock_registry_v30.md` §Shared Clocks/§Track tables or `module_contracts.yaml` stat fields; effects are stat deltas the substrate already writes. |
| **Machine-checkable-with-new-Key-or-field** | ARC-S07 (Coup Counter migration + streak counter), ARC-P06 (base-rate field), ARC-P04 (Axis 9 has no clock home at all — needs one built), ARC-P08 (needs structured evidence-trail struct, not the generic scalar Evidence Track), COLLISION-A/B (need a generalized per-arc lifecycle-state field, not just the NPC-scoped one) | The predicate shape is known and buildable; the specific field/Key doesn't exist yet but nothing about it requires GM discretion. |
| **GM-judgment-irreducible as currently authored** | ARC-P05 ("the GM rolls NPC faction institutional tendencies" — no formula), ARC-S29 (Cardinal Schism selects "whichever Cardinal's portfolio creates most institutional friction" — no scoring function exists), ARC-T06 (Schoenland "reads political situation" qualitatively) | Prose names a selection/heuristic outcome with zero decision function; needs either an authored deterministic tie-break or a declared weighted-random rule before it can run without a GM. |

**Whole-register estimate** (extrapolated from the above + full read of all 5 files, not just the
listed sample): **≈45% fully machine-checkable now** (mechanical alias resolution only) · **≈40%
machine-checkable-with-new-Key-or-field** (buildable, no judgment call) · **≈15%
GM-judgment-irreducible as written** (needs new authored decision logic, not just new data).
[UNGROUNDED — extrapolation from a close read of ~35 entries + full-file skim of the remaining
~75; not a literal per-entry tally.] Territory vectors (`arc_register_territory.md`) skew cleanest
(~85-90% fully checkable — direct map-state + stat-delta shape, few Coup-Counter/GM-judgment hits).
Clock vectors (`arc_register_clocks.md`) skew worst (2/7 clean; P03/P04/P05/P06 each hit a
different blocker class — see §4).

---

## 4. Trigger predicates needing state that does not exist yet (with what DOES exist cited)

1. **A generalized per-arc-vector lifecycle-state field.** `module_contracts.yaml` line 150 shows
   `{name: "arc state", bucket: clock, writable: true}` — but it is scoped to the `npc_behavior`
   module only (`npc_behavior_v30.md §5`, the T-23 mechanism per `01_arc_corpus.md` §d). No
   equivalent exists for faction/clock/territory-tier arc-vectors (the other ~100 register entries).
   Without it, COLLISION A/B/C/F/G cannot ask "is ARC-S21 currently in its converted state" as a
   queryable predicate — they'd have to re-derive it from raw clock deltas each time, and the
   prose sometimes doesn't even name a persistent flag for the state in question (e.g. ARC-S21
   "Klapp converts" has no named boolean anywhere). **This is the concrete, buildable form of
   ED-IN-0003** (audit F-2, convergence detector/applier — `00_engine_charter.md` Premise, C4).

2. **Coup Counter → Löwenritter Autonomy migration mapping.** `params/factions_personal.md` lines
   68/103-107: the numeric "Coup Counter" mechanic the register uses throughout (`arc_register_
   clocks.md` ARC-P03; `arc_register_factions.md` ARC-S20, ARC-S56, NPC-ARC-BRA, ARC-T26;
   `arc_register_events.md` COLLISION-F) is **STRUCK** (ED-781, supersedes ED-589) and replaced by
   a four-stage `Loyal → Restless → Autonomous → Split` track (`clock_registry_v30.md` line 29,
   `conflict_architecture_proposal.md §Graduated Autonomy`). No file maps the old numeric
   thresholds (2, 3, 40) the arc entries still cite onto the new stages. Every trigger built on
   "Counter = 2" or "Counter ≥ 40" cannot compile until this remap exists.

3. **Southernmost Ritual — entirely unauthored mechanic, and a dangling register ID.** ARC-S15
   (`arc_register_threads.md`) and COLLISION-C (`arc_register_events.md` §VI) both gate on
   "Southernmost Ritual [UNNAMED — ED-416]" via component ID **ARC-T04**. ARC-T04 has **no entry
   in any of the five register files** — it is referenced twice (`arc_register_territory.md` TE-12
   note; `arc_register_events.md` COLLISION-C) but never defined. Its cited justification is also
   wrong: `canon/editorial_ledger.jsonl` has **two** ED-416 entries (an ID collision in the ledger
   itself) — one "Almud stat block needed" (status resolved, `decision: null`), one "Cultural
   Uprising at T9... RM hold" (status open, 2026-06-29) — **neither** defines or gestures at a
   ritual. The citation does not resolve; the mechanic (procedure, dice, Ob, success/fail states)
   does not exist anywhere in the working tree.

4. **Axis 9 Pressure has no clock home.** ARC-P04 (`arc_register_clocks.md`) is described purely
   qualitatively ("accumulates silently... is not a discrete event... cannot be reversed") with no
   threshold, rate, or entry in `clock_registry_v30.md`'s Shared Clocks table — the one clock-tier
   arc in the register with zero backing numeric state (contrast: TC/RS have alias homes, IP/PI
   have homes elsewhere in `params/board_game.md` even though PI is missing from the registry
   table too — a lesser gap, resolvable by cross-referencing `params/factions_personal.md §Public
   Instability`).

5. **218 AG evidence-trail cross-referencing (ARC-P08).** "Four evidence trails... Cross-referencing
   ≥3 reveals..." needs a structured per-trail completion set + cross-reference counter, distinct
   from the generic scalar Evidence Track (`fieldwork_v30.md §4.1`, range 0-threshold). No such
   compound field exists in `key_type_registry_v30.md` or `module_contracts.yaml`.

6. **Streak / consecutive-success counters instantiated per arc-vector.** ARC-S07's "3 consecutive
   successful contacts → floor 6" and ARC-S15's "3 consecutive seasons without Weaving" both need a
   per-vector streak counter. The *pattern* already exists (Thread Fatigue clock, `module_contracts.
   yaml` line 280, "+2 Ob per prior threadwork scene"), but it is instantiated for threadwork
   fatigue specifically, not generalized to arbitrary arc-vectors — same gap-class as finding 1.

7. **Explicit in-text [EDITORIAL]/[GAP] numeric blockers** (these block *exact* compilation, not
   the trigger's *shape* — treat as calibration once flagged, per charter's numbers-marked-`[OPEN
   — Jordan tuning]` rule, not as structural gaps): TE-15 Structural Dissolution Ob
   (`arc_register_territory.md` line 42: `[EDITORIAL: establish canonical Ob...]`), ARC-S35 deed-
   claim invocation starting Ob (`arc_register_factions.md` line 32), ARC-P06 IP base rate
   (`arc_register_clocks.md` line 24: `[GAP: canonical base rate not specified; working assumption
   +2/season]`).

8. **NPC "flaw" decision rules — largely already exist, contrary to first impression.** PROTECTIVE/
   PROCEDURALIST/IDEALIST/PROFIT-MAXIMISING/STABILITY-SEEKING flaws (Laskaris, Haelgrund, Vossen,
   Feldhaus, Solberg) read as narrative color in the register but are backed by explicit
   "Behavioral AI" utility rules in `designs/npcs/npc_roster_v30.md` (e.g. line 98 Feldhaus:
   "optimises for Guilds Wealth above all other stats... will sacrifice Mandate/Stability to
   protect revenue"). **Not a gap** — cite `npc_roster_v30.md` per-NPC, not the register text.

---

## 5. Worked example A — ARC-S07 "Torben Loyalty Clock" (capstone compilation target)

```yaml
arc_vector:
  id: ARC-S07
  tier: S
  scope: { faction: [Crown], territories: ALL, mode: ALL }
  activity_mode: clock_escalation
  trigger:
    predicate:
      - { field: clock.IP, op: ">=", value: 30 }   # co-fires ARC-T02 Tutoring Demand (same trigger,
                                                     # parallel branch per arc_register_factions.md
                                                     # line 41: "The two arcs run in parallel from
                                                     # the same trigger.")
    resolves_via: null   # pure clock-threshold read
    temporal_window: same_season
  pressure_effects:
    - { target: npc_track.Torben.Loyalty, delta: "-1",
        cadence: season,
        condition: "Covert Contact fails (stat.Crown.Intel vs Ob 3, resolver dice_pool)" }
    - { target: clock.CoupCounter, delta: "+1", cadence: season,
        condition: "npc_track.Torben.Loyalty <= 3"
        # [GAP #2 above — Coup Counter STRUCK; must remap to Löwenritter Autonomy stage before
        #  this line compiles. arc_register_factions.md line 11.]
      }
    - { target: stat.Crown.Mandate, delta: "-2 cumulative", cadence: season,
        condition: "npc_track.Torben.Loyalty <= 2" }
    - { target: npc_track.Torben.Loyalty, delta: "floor(6)", cadence: one_time,
        condition: "3 consecutive successful Covert Contacts"
        # [GAP #6 above — needs a per-vector streak counter, not yet instantiated for this arc.]
      }
    - { target: clock.IP, delta: "+3", cadence: immediate,
        condition: "NPC-ARC-LAK flip: npc_track.Elske.Loyalty <= 2 (Laskaris PROTECTIVE flaw,
                     npc_roster_v30.md line 179/141)" }
  payload:
    direction: "Altonian pressure converts the heir into a lever against the dynasty."
    participating_actors: [Torben, Almud, Ehrenwall/Löwenritter, Laskaris, Elske]
    stakes_tags: [gating, pricing, pattern_response]
    ledger_cause: ["PP-498 (Torben track, params/board_game.md §Torben)"]
  lifecycle:
    states: [seeded (IP<30), active (Tutoring Demand fired), escalating (Loyalty falling),
             converging (feeds COLLISION-B/C/F), resolved (floor 6) | abandoned (Loyalty 0 →
             ARC-T13 Crown-elimination branch)]
    terminal: false
  cross_refs: [ARC-S20, ARC-T02, ARC-T13, COLLISION-B, COLLISION-C, COLLISION-F]
  gaps:
    - { type: struck_mechanic, note: "Coup Counter increment step",
        cites: ["params/factions_personal.md:68,103-107", "arc_register_factions.md:11"] }
    - { type: missing_field, note: "3-consecutive-success streak counter",
        cites: ["module_contracts.yaml:280 (Thread Fatigue pattern, not generalized)"] }
```

**Verdict: machine-checkable-with-new-Key-or-field.** Every clock/stat the trigger and most effects
touch is canonical (Torben Loyalty: `clock_registry_v30.md` line 27, range 0-7 start 3 — note the
register's own "Loyalty (8→0)" phrasing is a looser gloss on the same 0-7 range, not a numeric
contradiction). The two blockers (Coup Counter, streak counter) are buildable, not GM-judgment.

---

## 6. Worked example B — COLLISION-C "Tutoring + Southernmost"

```yaml
arc_vector:
  id: COLLISION-C
  tier: COLLISION
  scope: { faction: ALL, territories: [T15, T13, T6 (implied via ARC-S15)], mode: ALL }
  activity_mode: convergence
  trigger:
    predicate:
      - { field: npc_track.Torben.Loyalty, op: "<=", value: 3 }   # = ARC-S07's own escalating state
      - { field: arc_state.ARC-T04, op: "==", value: "ritual_failure" }
        # [BLOCKED — ARC-T04 has no register entry anywhere in references/arcs/*; referenced only
        #  from arc_register_territory.md:33 and arc_register_events.md:38. Dangling ID.]
    resolves_via: null
    temporal_window: unspecified   # [structural gap — charter Q3 "temporal windows" correlation
                                     # test is named as required; COLLISION entries never state a
                                     # window rule. Same-season? Same Accounting? Undefined.]
  pressure_effects:
    - { target: clock.MS, delta: "+8", cadence: one_time }        # RS→MS rename
    - { target: clock.IP, delta: "+2", cadence: one_time }
    - { target: clock.CI, delta: "+2", cadence: one_time }        # TC→CI rename
    - { target: clock.ARC-S15.cracking_clock, delta: "reset; MS decay += 2/season", cadence: season,
        condition: "clock.MS near 50" }   # second-order dependency on ARC-S15's own escalation
    - { target: clock.CoupCounter, delta: "may reach 3 from cascade alone", cadence: one_time }
        # [same struck-mechanic gap as ARC-S07]
  payload:
    direction: "Players face three simultaneous crises with one practitioner incapacitated."
    participating_actors: [Torben, Edeyja, Crown, Wardens]
    stakes_tags: [gating, foreclosure]
    ledger_cause: ["ARC-S07", "ARC-T04 (undefined)", "ARC-S15"]
  lifecycle:
    states: []   # convergence vectors have no independent state of their own — they fire the
                 # instant constituent conditions align (see §4 finding 1)
    terminal: true
  cross_refs: [ARC-S07, ARC-T04, ARC-S15]
  gaps:
    - { type: dangling_id, note: "ARC-T04 has no register entry",
        cites: ["arc_register_territory.md:33", "arc_register_events.md:38"] }
    - { type: missing_mechanic, note: "Southernmost Ritual — no procedure/Ob/outcome defined",
        cites: ["arc_register_threads.md:14 (ARC-S15 cross-ref only)"] }
    - { type: stale_citation, note: "[UNNAMED — ED-416] resolves to two unrelated ED-416 ledger
        entries (Almud stat block; T9 Cultural Uprising) — neither is a ritual",
        cites: ["canon/editorial_ledger.jsonl:62 (embedded ED-416, decision:null)",
                "canon/editorial_ledger.jsonl:494 (ED-416, status open, 2026-06-29)"] }
    - { type: struck_mechanic, note: "Coup Counter cascade line",
        cites: ["params/factions_personal.md:68,103-107"] }
    - { type: missing_field, note: "temporal_window rule for convergence triggers is unspecified
        register-wide", cites: ["00_engine_charter.md Q3 (temporal windows correlation test)"] }
```

**Verdict: GM-judgment-adjacent / blocked-by-missing-mechanic**, not because of any judgment call
but because one of its two constituent conditions (ARC-T04 / Southernmost Ritual) does not exist
as an authored mechanic anywhere in the working tree, and its ledger citation is itself wrong. This
is the worst-case pattern in the corpus: a second-order convergence vector inherits every gap of
its first-order constituents, and COLLISION-C happens to hit three additional gaps of its own
(dangling ID, stale citation, unspecified temporal window) on top.

---

## 7. Summary of what exists vs what's missing (quick reference)

| Register term | Canonical home | Status |
|---|---|---|
| TC (Theocracy Counter) | Church Influence (CI), `clock_registry_v30.md` line 17 | Renamed per ED-782; register uses legacy name throughout — trivial resolve |
| RS (Rendering Stability) | Mending Stability (MS), `clock_registry_v30.md` line 16 | Renamed per ED-731; register uses legacy name throughout — trivial resolve |
| IP (Institutional Pressure) | `clock_registry_v30.md` line 18 | Canonical, present |
| PI (Public Instability) | `params/factions_personal.md`, `params/board_game.md §PI` | Canonical but **missing from `clock_registry_v30.md`'s own Shared Clocks table** — a registry gap, not a mechanic gap |
| Torben/Elske Loyalty | `clock_registry_v30.md` lines 27-28 | Canonical, present |
| Coup Counter | — | **STRUCK** (ED-781/589); replaced by Löwenritter Autonomy stage track, no remap authored |
| NPC flaws (PROTECTIVE etc.) | `designs/npcs/npc_roster_v30.md` | Canonical Behavioral AI rules exist — not a gap |
| Axis 9 Pressure | — | No clock defined anywhere |
| Southernmost Ritual / ARC-T04 | — | Entirely unauthored; dangling register ID |
| Per-arc-vector lifecycle state (non-NPC) | `module_contracts.yaml:150` (NPC-scoped only) | Needs generalization — this **is** ED-IN-0003 in concrete form |
