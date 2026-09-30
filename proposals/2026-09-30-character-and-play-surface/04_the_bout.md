# The bout — the personal combat engine, its traditions, and the nine moments

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: PC · IDs: none allocated
## Measured at HEAD `c8cc408` (no `systems/` file changed in #444). Figures quoted from July measurements are marked as such and were not re-taken.
## Suite: [README](README.md) · **04 the bout** · [05 two modes](05_two_modes_of_one_bout.md) · [06 weapons](06_weapons_from_physics.md) · [07 saying a weapon is good](07_saying_a_weapon_is_good.md)

**What this answers.** What a single bout is in `systems/combat/combat_engine_v1/`; how martial
traditions work and how far they are built; the nine moments where a character's training can change
an outcome; and how unusual the design is against the games it will be compared to.

---

## 1. Analysis

### 1.1 What a bout is

`wrapper.fight(A, B, cfg, rng, max_bouts=12)` runs engagements until someone is felled or twelve pass;
its own comment says it is *"the multi-turn SIM harness … the GAME calls one engagement per turn"*
(~10 s of fighting). Inside `wrapper.engagement()`, a state graph declared as data in `state_graph.py`
runs beat by beat: **Approach → AwaitTempo → Exchange** (commit, read, mode, roll, outcome) → **Bind /
Riposte / HitLanded / Contact** → back to AwaitTempo, or **Felled / Separation**. The graph is checked
against the live trace by its own integrity harness.

Three rulings shape what a bout can produce: wounds add a **fractional obstacle** and never remove dice
(ED-PC-0005); an engagement in which nobody falls ends **unresolved**, which is a legitimate outcome and
not a tiebreak (Jordan, 2026-06-02); and a decided fight flips with probability `UPSET_FLOOR = 0.05`, so
no matchup is certain.

### 1.2 Traditions: from multipliers to a way of reading

The first model gave each tradition a seven-channel multiplier vector (German `tactile 1.35`, and so
on) — the shape most games with fighting schools use. It was measured and removed: an **18.8 pp**
imposition spread and a **6.8 pp** unconditional win-rate spread across traditions meant to be balanced,
because a scalar vector *"differentiates quantitatively, not qualitatively, and cannot specialize AND
stay vacuum-balanced"* (`.designs/.../tradition_decomposition_v1.md`, archived reference). The vector was
deleted on 2026-06-29; the label-keyed "imposition gate" that forced each tradition's preferred node was
retired as top-down scripting (ED-PC-0023; its data deleted, ED-PC-0035).

What replaced it (`traditions.py`, `ability_primitives.py`): a tradition is *"a COGNITIVE MODE — a way
of reading the same shared physics — NOT a separate rule-set."* Every fighter runs on one substrate —
measure, tempo, feel, leverage, perception, pre-commitment, structure. A tradition grants **access** to
a kit of learned techniques, each traced to a documented technique with a source tier (S1 primary, S2
peer-reviewed, S3 specialist), and a sparse-tradition rule refuses to invent techniques where the
corpus is thin: Chinese and Filipino practice each yield one extracted tendency and no asserted ability.
Efficacy comes from **graded investment**, not membership (ED-PC-0024): an additive ability scales
`value × level`, a multiplicative one `value ^ level`, and level 0 is inert. `familiarity` (0.85 by
default, 0.93 between historically adjacent traditions) is the only tradition-level quantity left, and
it is pairwise.

### 1.3 The nine moments

`state_graph.py::INJECTION_POINTS` lists exactly nine places where training can change what happens.
The July Plan-layer proposal (`proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md`,
PROPOSED, design-only) makes six of them player decisions and keeps three closed, for reasons that bind
any interface built later:

| # | moment | node | generic choice | player-facing? |
|---|---|---|---|---|
| 1 | `approach.measure` | Approach | shorter closes, longer stop-hits | yes — I1 MEASURE |
| 2 | `reopen.measure` | AwaitTempo | reopen the distance or stay closed | yes — I5 BIND-OR-BREAK |
| 3 | `exchange.commit` | Exchange | commit depth 2–5 | yes — I2 COMMITMENT |
| 4 | `exchange.read` | Exchange | who reads whose intent | **no** — a contest, not a choice |
| 5 | `exchange.mode` | Exchange | parry, dodge or wind | yes — I3 GUARD |
| 6 | `exchange.bind_entry` | Bind | entering the bind | **no** — a consequence of mode and degree |
| 7 | `exchange.counter` | Riposte | the single-time counter | yes — I4 COUNTER |
| 8 | `burst.continuation` | AwaitTempo | press on or separate | **no** — tempo-determined |
| 9 | `contact.axis` | Contact | grab, disarm, throw, pin, escape | yes — I6 CONTACT |

A character's trained skill can still bias all nine; the line is only that the *player* does not
declare outcomes at 4, 6 and 8.

⚠ The dict's `injects` column still describes tradition *intent* — "German prefers wind, Italian refuses
it". With the imposition gate retired, the only live tradition mechanism is a learned ability on a
lever. [06](06_weapons_from_physics.md) §1.4 reports what each moment actually reads.

### 1.4 How much is built — fifteen levers, seven with any technique

The engine consumes fifteen levers: seven substrate channels (`measure, tempo, visual, precommit,
leverage, tactile, balance`), three counter levers (`counter_success, counter_select, anti_overcommit`)
and five morphology levers (`edge_read, spine_press, edge_grab, choke_control, facing_regime`).
`ability_primitives.ABILITIES` holds nine techniques across five traditions:

| lever | techniques |
|---|---|
| `measure` | Italian *misura* |
| `leverage` | German *Stärke-Schwäche*, Spanish *atajo* |
| `counter_select` | Italian *mezzo tempo*, German *Zwerchhau* |
| `counter_success` | German *Indes / Fühlen* |
| `anti_overcommit` | English *true times* |
| `spine_press` | Japanese *shinogi* |
| `edge_grab` | German *Ringen am Schwert* |

**Eight levers have no technique:** `tempo`, `visual`, `precommit`, `tactile`, `balance`, `edge_read`,
`choke_control`, `facing_regime`. The first five are not random gaps; they are the signature
primitives the decomposition assigns to whole traditions. Japanese practice is *"wins before the blade
moves"* (pre-commitment and perception) and nothing targets `precommit` or `visual`. Spanish Destreza
is geometry and footwork (`balance`) and nothing targets it; the June decomposition also found that
channel largely suppressed in the engine (not re-measured here). German practice's *Fühlen* is present,
but as `indes` on `counter_success`, not on `tactile`. The `seize` lever is dead: its consumer was cut
on 2026-06-05, so a character who learns *Vorschlag* gains nothing (the module records retire-or-reroute
as Jordan's call).

What the built part does, measured: the ability layer's **aggregate** win-rate edge is about zero once
isolated from tradition membership; its effect is **per event** — a bind won, a grab made safe
(`tests/valoria/test_combat_tradition_levers.py`). In July the customisation surface as a whole measured
"broad and hollow": weapon choice spans ninety percentage points while tradition spread was 3.8 pp with
`none` highest (the Plan-layer proposal's §1, D1–D6; not re-measured).

### 1.5 How unusual it is

Most role-playing games resolve melee as an attack roll and a damage number and model no approach,
tempo or reading at all. A narrower lineage of simulationist tabletop combat does model them — *The
Riddle of Steel* and its descendants with timing and feint-against-commit, GURPS *Martial Arts* with
Feint as an opposed manoeuvre, Burning Wheel's *Fight!* with actions scripted in secret and revealed
together. Action games model approach and anticipation through the player's own timing instead of the
character's — *Kingdom Come: Deliverance*, *For Honor*, *Mordhau*, *Hellish Quart*.
`[UNVERIFIED: from these systems' published rules as generally known; not re-read for this document,
and none of these titles is surveyed in research/]`

Against that field, three things here are uncommon, and the first two are the design's own
achievement rather than a gap:

1. **Continuous measure, tempo and leverage resolved by contested rolls inside a full role-playing
   game** — neither abstracted away nor handed to the player's reflexes.
2. **A tradition is a reading of shared physics, reached by measuring and discarding the stat-multiplier
   model**, with every technique traced to a graded source and a written refusal to invent the rest.
3. **Its depth is spent on the single clash.** Fire Emblem and Final Fantasy Tactics resolve a clash as
   one formula evaluation because their depth lives on the grid; this engine spends its granularity on
   the clash itself, which is right only if a personal duel is a rare, weighty scene. [05](05_two_modes_of_one_bout.md)
   takes this up.

The honest qualifier: two of the fifteen levers carry a technique whose historical grounding survived
the July adversarial re-grounding (*shinogi*, *Ringen am Schwert*); the architecture is further along
than its content.

---

## 2. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **B-1** | Author techniques for the five unhooked signature levers — `precommit` and `visual` (Japanese *sen-sen-no-sen*, *metsuke*), `balance` (Spanish *compás*), `tactile` (German *Fühlen* proper), `tempo` — under the same source-tier and sparse-tradition rules; where no S1/S2 technique exists, write that down instead of a number. | `ability_primitives.ABILITIES` | a per-event test per technique, the U10 pattern (a bind won, a read taken), never aggregate win-rate alone | medium; the research exists in the decomposition | PC lane |
| **B-2** | Replace `INJECTION_POINTS`' `injects` prose with the live mechanism (which abilities, on which levers, reach each point), or drop the column; it currently describes a retired gate. The same stale sentence opens `traditions.py` (its header still names the imposition gate as a differentiator; its own body, lines 38–44, says the gate is gone). | `state_graph.py`, `traditions.py` header | the strings name only abilities present in `ABILITIES` | trivial | buildable now |
| **B-3** | Measure tradition identity where it lives — per event at the nine moments — using the existing `_TRACE` hook: does a trained German fighter enter the bind more often, an Italian disengage more? This is the decomposition's own gate ("qualitatively distinct"), and aggregate win-rate cannot see it. | workbench, `wrapper._TRACE` | a table of per-moment event rates by tradition, with an untrained control | small | buildable now |
| **B-4** | Do not answer thin content by restoring tradition-level multipliers. The scalar vector failed a measurement; it stays deleted. | — | — | — | standing rule |

The dead `seize` lever is already recorded as Jordan's call in `ability_primitives.py`; this suite adds
no new item for him.
