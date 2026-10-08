# The character sheet as three spaces — creation, development, chronicling

## Status: PROPOSED (2026-10-07) · design-only · builds nothing · HELD BACK from ratification-on-merge (ED-1094) until its review in B-H against IN-08's carriers · reference under `CLAUDE.md` §0.05
## Lane: IN, with PC and WR · Plan position: IN-47 (`workplans/valoria_master_workplan_v9_part4.md` §4.2, the IN-47 entry) · IDs: none allocated
## Read at HEAD `4558f85`. Every `file:line` below was opened at that HEAD; a line that has drifted since is a defect in this document, not in the code.
## Builds on: `proposals/2026-09-30-character-and-play-surface/09_the_character_sheet.md` (#445; what a person is in code, one sheet) — not re-derived here.

**What this answers.** IN-47 asks, for each of the three spaces Jordan's 2026-09-05 framing names — *"a
character generation/progression/management/chronicling system"*
(`references/what_valoria_is_and_what_runs.md:107`) — what the space **reads** (a typed input), what it
**emits** (acts), and which carrier each act **reaches through the fold**. It is the design for the
`scales:` row that reads `in_loop: false` (`engine/season/requirements.yaml:71-82`). No Jordan ruling
is needed; the division into three spaces is this document's proposal, as the entry says.

**What it does not do.** It edits nothing under `engine/`, adds no verb, field or roster row, and
schedules nothing. Where a space needs a writer that does not exist, it names the position that builds
the writer and stops.

---

## 1. The contract every space inherits (A-25)

A-25 (`workplans/valoria_master_workplan_v9_part5.md:383-422`) places the character sheet among the
**management spaces** (`:391-392`, `:419`) and says what one is: like the world surface, it *"reads the
player's own `View`/`Question`/`Candidate` and emits acts, owning no game state, as the management
spaces do"* (`:415-416`). In code that is five sites:

| what | site (opened) | what it means for a space |
|---|---|---|
| the player's slot | `SeasonDriver.season(self, choose, question, subsistence, …)`, `engine/season/loop/driver.py:355` (A-25 cites `:330`, which has drifted to a comment) | a space is, at most, a `choose` callable — or a part of the one handed in for the player's person |
| DELIBERATE | `engine/season/loop/deliberate.py:1` (*"owns **nothing** … **token: none**"*), `:68` (`deliberate(self, choose, …) -> list[Act]`) | a space runs inside a map that holds no token, so it **cannot** write; it returns `Act`s |
| the inputs | `View`, `engine/season/state/carriers.py:379-409` (ids only; any world reach raises `Forbidden`, `:404-409`); `Question`, `:412-431`; `Candidate`, `:434-460`; the opening set, `decision/options.py:43` (`opening_set(p, v, q, fx) -> list[Candidate]`) | a space reads the player's own claims and the candidates the opening set already formed |
| the output | `Act`, `engine/season/state/carriers.py:508-550` | the only thing a space hands back |
| the fold | `resolve`, `engine/season/loop/resolve.py:685`; `_fold`, `:294`; `_apply_write`, `:614`; under an ACTS token minted at `loop/driver.py:452`; the write itself through `World.write`, `engine/season/state/world.py:790` | every carrier change a space causes happens **here**, under RESOLVE's token, against a `write_matrix.yaml` row |

Layer 1 states the discipline once: **"A module with no token cannot write, and that is the whole of the
write discipline"** (`architecture/meta/04_CODE_ARCHITECTURE.md:158`).

**Two rules follow, and they bind all three spaces.**

1. **A space ranks and selects; it never forms.** It chooses among the `Candidate`s
   `decision/options.py:43` formed. A space that minted a candidate the opening set did not form would
   be a second option generator for the player alone — *shape divergence* (`CLAUDE.md` §10). The
   automated chooser (`decision/choose.py:289`, `make_chooser`) and the playable space read the same
   candidate set, so they emit the same act shapes.
2. **A space owns no writer.** Every Person write below is an effect body's or a step's, under a
   `write_matrix.yaml` row. The space reads what those writers did, next round, through the player's
   own View and Person fields.

### 1.1 The Person fields, their rows, and who writes them today

`Person` is `engine/season/state/carriers.py:556-628`.

| field | carrier | write-matrix row (`engine/season/write_matrix.yaml`) | live writer at `4558f85` |
|---|---|---|---|
| `capability` | `:565` | **none** — `Person.capability` is on `retired:` (`:386`), so no season write is licensed | world-gen only: `build_at` seats a cast entry's authored dict (`engine/season/harness/corpus_run.py:537-540`); read by `seam/wrappers/sigma.py:75-87` (`_capability`) and `:90` (`_pool_of`) via `rosters.yaml` `verb_capability` (`engine/season/rosters.yaml:1039`) |
| `stance` | `:566` | `:211-217`, [RES, ENC], `stance.moved` | `march`: `_eff_march`, `engine/season/loop/effects_combat.py:275` (stance rows at `:353`) |
| `pursuits` | `:567` | `:186-193`, [RES], `pursuit.moved`, **`unproduced:` (H-62)** | world-gen only: `seed_pursuits` (`engine/season/harness/run_cases.py:44`) via `corpus_run.py:526` and `harness/populated.py:697-698` |
| `ledger` | `:571` | `claim_ledger`, `:171-177`, [WIT], INTERIOR — *"`witness` the only minter, and it is not an act"* | WITNESS |
| `body` | `:581` | `:161-170`, [MAT, RES, ENC] | the `fight` effect (`effects_combat.py:109-111`), `march`, MATTER |
| `scar` | `:602` | `:204-210`, [RES], `scar.taken` | `_scar`, `effects_combat.py:39-106`, called at `:245` — **inert at the shipped `scar_step=0`** (`engine/season/data/fixtures.py:599`; the early return is `effects_combat.py:71-76`) |
| `conviction` | **absent** | **absent** | — (IN-08 adds it; §5) |
| `exists` | — | `:197-203`, [MAT, RES, CEN], `person.individuated` | CENSUS, which writes nothing (`engine/season/loop/census.py:30-40`) |

---

## 2. Creation — where a person comes from

**Today.** Nothing in the season loop constructs a `Person`. Every construction is in `harness/`:
`corpus_run.py:511` (a case's cast), `populated.py:438` (cohorts) and `:671` (the realm), plus
`headless.py:71`, `scarce.py:105`, `governance_spine.py:130`. `loop/matter.py:96-98` records the grep
that makes it so. CENSUS owns individuation and generates nobody (`loop/census.py:30-40`, *"demand-driven
only; generated nobody"*); what *demands* an individuation is hole `H-51`, grade `absent`, owner
unassigned (`engine/season/hole_register.yaml:582-589`).

**The design: two arms, and neither emits an act.**

| | creation, arm C1 — before the first season | creation, arm C2 — a person who appears mid-campaign |
|---|---|---|
| **typed input** | not a `View`: the player's person has no ledger yet. It reads the roster owners — the pursuit and axis rosters (`references/descriptor_registry.yaml`, behind `engine/substrate/descriptors.py`) and the capability keys (`rosters.yaml:1039`, `verb_capability`) — and produces **one cast entry** of the shape `build_at` already reads (`who`, `capability`, pursuits; `corpus_run.py:505-540`) | the individuated person, once CENSUS writes `(Person, exists)` (`write_matrix.yaml:197-203`) |
| **acts emitted** | **none** | **none** |
| **carrier reached, and how** | `Person.capability` and `Person.pursuits`, by **world-gen's one writer** — `build_at` (`corpus_run.py:537-540`) and the realm builder (`populated.py:697-698`) — which Layer 1 licenses: *"world-gen writes it once; nothing else does"* (`architecture/meta/04_CODE_ARCHITECTURE.md:1153`, F.6). No fold exists before the first season, so there is no act to reach it through | `Person.exists`, by CENSUS under its MATTER token (`loop/census.py:1`); the space only reads the result |

**Why creation emits no act.** The other two spaces act inside a season; creation's C1 output is
consumed before there is one. Making it an act would need a verb that writes `capability` at RESOLVE —
which is development's `train`, not creation. Arm C2 is not the space's to trigger: an individuation's
demand is H-51, and a space that minted persons would be the generator S29 forbids
(`loop/census.py:34-40`). **Choosing which person the player plays is not a World write at all**: it is
which person's `choose` the driver is handed as PLAYABLE (`loop/driver.py:355`).

**[ASSUMPTION, the point the review must attack.]** That C1 does not trip the falsifier (§6): the space
writes a **cast entry**, a record outside `World`, and the existing world-gen builder writes the
`Person`. If the review reads F.6's world-gen licence as not extending to a player-authored entry, C1
shrinks to *"the player picks a person the cast already holds"*, and every authored difference moves to
development.

---

## 3. Development — what writes a person after creation

**Typed input.** The player's own `View` (`carriers.py:379-409`), the `Question` it was built for
(`:412-431`, carried on the View at `:402`), the `Candidate[]` from `opening_set`
(`decision/options.py:43`), and the player's own Person fields — person-side state, the same inputs
`make_chooser` lists as admissible (`decision/choose.py:299-300`: *"`pursuits`, `stance`, the View, the
two Sensation scalars. No World"*).

**Acts emitted.** `Act`s (`carriers.py:508-550`) selected from those candidates, packed into scenes as
the automated chooser packs them (`decision/choose.py:372`, `pack_scenes`). The space **does not own
any verb below**; it reads what each writer did.

| field | the act that reaches it (through RESOLVE, `loop/resolve.py:685`) | exists at `4558f85`? |
|---|---|---|
| `capability` | `train` — IN-12 step 9, batch B-Q (`workplans/valoria_master_workplan_v9_part5.md:148`): it *"forms and writes `Person.capability` only where a case names a vocation"*, and un-retires `Person.capability` | **no.** `engine/season/verb_table.yaml` has no `train` row, and the field sits on `retired:` (`write_matrix.yaml:386`) |
| `pursuits` | `argue` (IN-12 step 9, same row, `:148`), after SC-02 `22b` step 24, the field's first producer | **no** — the row carries `unproduced:` (`write_matrix.yaml:193`); `argue` has no `verb_table.yaml` row |
| `scar` | the `fight` effect's `_scar` (`effects_combat.py:245` → `:39`), at RESOLVE | **yes, inert** — `scar_step=0` returns before touching the carrier (`fixtures.py:599`; `effects_combat.py:71-76`). IN-08's H3 changes its shape (§5) |
| `stance` | `march`'s `Won`/`Lost` bands (`_eff_march`, `effects_combat.py:275`), at ENCOUNTER | **yes** — the one live interior writer (`write_matrix.yaml:218-223`) |
| `body` | `fight`, `march`, MATTER (`write_matrix.yaml:161-170`) | **yes** |
| `conviction` | IN-08 H10, B-H (§5) | **no field** |

**What development may display.** The player's own fields and own claims only. A sheet that showed a
person's capability *relative to another's*, or the truth of a claim, would read world state through a
View, which raises (`carriers.py:404-409`). The sheet's derived lines (#445 §1.6: faculties, `command`,
standing as a perception gap, rank) stay derived at read time; development stores none of them.

**Where development and the automated chooser differ.** Only in who picks. The automated mode is
`make_chooser` (`decision/choose.py:289`); the playable mode is the same candidate set picked by the
player. Same seed, same choices, same `World.content_hash()` (`engine/season/state/world.py:1274`) —
which is IN-46's falsifier applied here (`_part4:107`).

---

## 4. Chronicling — a person's own record of a life, and how it is read out

**Typed input.** Two, and they must not be confused.

- **In the simulation:** the person's own `ledger` (`carriers.py:571`) of `Claim`s (`:256-311`),
  deposited only at WITNESS (`write_matrix.yaml:171-177`) and read through `LedgerReader`
  (`engine/season/queries/person_q.py:89`), whose order is recency then confidence (#445 §1.4).
  Eviction ranks on confidence and recency **and nothing else** — salience is excluded by signature
  (`architecture/meta/04_CODE_ARCHITECTURE.md:1057`, row 39; `architecture/meta/07_DYNAMICS.md:174`).
- **Outside the simulation:** the cause graph — `Event`s (`carriers.py:197-198`) and their `causes[]`,
  which `state/attribution.py`'s `actor_of` walks (`carriers.py:215`). This is `STORY-READ`
  (`proposals/2026-10-04-forcing-churn-and-the-story-bar.md:169`): *"an observer outside the simulation
  that finds arcs in the cause graph … Layer 1 forbids salience ranking inside the sim"*, realised as
  proposal 1, the chronicle render (`proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md:14`).

**Acts emitted: none.** **Carrier reached: none.** Chronicling is a reader. A person's record is the
ledger the loop already writes; the life-story told from it is a render, and a render that ranked
events by importance inside the loop would be salience-ranked memory. So the space has two outputs,
both outside `World`: the ledger as the person holds it (unknowns stay unknown, false beliefs stay
believed — #445 §1.4), and the out-of-sim render over `causes[]`, which may rank because it is not the
simulation.

**A name collision, stated so nobody resolves it silently.** `epistemic.py:528` has a WITNESS channel
named `chronicle` (`_ch_chronicle`, the matter-of-record channel). It is a deposit rule the loop owns;
the chronicling space neither owns nor calls it. IN-12 step 10's *"chronicle deposit"* (`_part5`, the
step-10 row) is that channel.

---

## 5. IN-08's carriers — what exists and what does not, for the B-H review

IN-47 *"reads the carriers IN-08 creates (`Person.scar`, `Person.conviction`) and is reviewed against
them in B-H"* (`_part4:113`). At `4558f85` the two are in different states:

- **`Person.conviction` does not exist.** `engine/season/state/carriers.py` has no `conviction` field
  (no match in the file; `Person` is `:556-628`). IN-08's B-G commit adds it as `12b`'s carrier with a
  `write_matrix.yaml` row, and H10 in B-H fills it (`workplans/valoria_master_workplan_v9_part5.md:43`,
  EDITS). **Until then, §3's `conviction` line has no carrier, no row and no writer.** The review fills
  the row of §3's table: which act reaches it, and whether development displays it or only a derived
  confliction Query (IN-08's `queries/person_q.py` Query, *"derived and never stored"*).
- **`Person.scar` exists but is not yet IN-08's carrier.** It is a bare per-axis dict
  (`carriers.py:602`), deliberately unseeded because the axis roster is ruled to change
  (`:588-596`), with **no reader** (`:599-601`), and its one writer is off by default (§1.1). IN-08
  changes its shape at H3, in B-H (`_part5:43`, *"`Person.scar` `:602`, H3"*). **The review re-reads §3's
  `scar` line against the H3 shape**: the key set, who is scarred (the subject or the actor — left open
  at `effects_combat.py:66-70`), and whether any space displays it.

Neither is a gap this document fills. The B-H review does, against the code IN-08 lands.

---

## 6. Review criteria

The review in B-H passes this design only if all four hold.

1. **THE FALSIFIER (IN-47's own, `_part4:114`).** *A space that writes a `Person` field outside an act's
   fold contradicts A-25 and Layer 1's "a module with no token cannot write"*
   (`architecture/meta/04_CODE_ARCHITECTURE.md:158`) *and fails the review.* Check each space against
   §1.1: development writes only through acts RESOLVE folds; chronicling writes nothing; creation's C1
   writes a cast entry and C2 writes nothing. The **[ASSUMPTION]** in §2 is the one place this can fail.
2. **No second option generator.** Every act a space emits was a `Candidate` from
   `decision/options.py:43` (§1, rule 1).
3. **No salience inside the simulation.** Chronicling's in-sim reader orders by recency and confidence
   only (`04:1057`); any ranking by importance lives in the out-of-sim render (§4).
4. **At the build (not this document's):** with the creation arm switched off, a seeded run reproduces
   the pre-build `World.content_hash()` (`_part4:114`); with chronicling switched on or off, the hash is
   identical, since it writes nothing.

---

## 7. What this depends on, and what is not verified

- **Writers this design reads and does not build:** `train` and `argue` (IN-12 step 9, B-Q), the first
  `pursuits` producer (SC-02 `22b` step 24), `Person.conviction` (IN-08, B-G/B-H), H3's `scar` shape
  (B-H), and an owner for H-51 (none). Until those land, development can display and choose but moves
  only `stance` and `body`.
- **No build position exists** (`_part4:114`): R-04 conjunct (3) cannot read `met` for this row until
  one does; `_part3` §B.0's R4/R7 place it once this design is reviewed
  (`workplans/valoria_master_workplan_v9_part3.md` §B.0, rules R4 and R7).
- **Not re-run here:** the row's count of 429 of 430 built persons with empty `capability`
  (`engine/season/requirements.yaml:76-79`, measured 2026-10-02). Not re-opened here: Jordan's
  2026-09-30 *"design one character sheet"*, which the plan entry itself tags `[UNVERIFIED]`.
