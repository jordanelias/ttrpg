# The character sheet as three spaces — creation, development, chronicling

## Status: PROPOSED (2026-10-07) · design-only · builds nothing · HELD BACK from ratification-on-merge (ED-1094) until its review in B-H against IN-08's carriers · reference under `CLAUDE.md` §0.05
## Lane: IN, with PC and WR · Plan position: IN-47 (`workplans/valoria_master_workplan_v9_part4.md` §4.2, the IN-47 entry) · IDs: none allocated
## Written at HEAD `4558f85`; reviewed and every `file:line` re-derived at HEAD `867c1c3f` (B-H, 2026-10-08). A cite that has drifted since is a defect in this document, not in the code.
## Builds on: `proposals/2026-09-30-character-and-play-surface/09_the_character_sheet.md` (#445; what a person is in code, one sheet) — not re-derived here.

**What this answers.** IN-47 asks, for each of three spaces — creation, development, chronicling — what the
space **reads** (a typed input), what it **emits** (acts), and which carrier each act **reaches through the
fold**. Jordan's 2026-09-05 framing names the system whole: *"a character
generation/progression/management/chronicling system"* (`references/what_valoria_is_and_what_runs.md:107`),
and A-25 places it as **one** management space (the character sheet; `workplans/valoria_master_workplan_v9_part5.md`
§A A-25, `:366-367`, `:393-394`). It is the design for the `scales:` row that reads `in_loop: false`
(`engine/season/requirements.yaml:71-82`). No Jordan ruling is needed; the division of that one space into
three is this document's proposal, not the framing's.

**What it does not do.** It edits nothing under `engine/`, adds no verb, field or roster row, and
schedules nothing. Where a space needs a writer that does not exist, it names the position that builds
the writer and stops.

---

## 1. The contract every space inherits (A-25)

A-25 (`workplans/valoria_master_workplan_v9_part5.md:358-397`) places the character sheet among the
**management spaces** (`:366-367`, `:393-394`) and says what one is: like the world surface, it *"reads the
player's own `View`/`Question`/`Candidate` and emits acts, owning no game state, as the management
spaces do"* (`:389-391`). In code that is five sites:

| what | site (opened) | what it means for a space |
|---|---|---|
| the player's slot | `SeasonDriver.season(self, choose, question, subsistence, …)`, `engine/season/loop/driver.py:355` (A-25 cites `:330`, which has drifted to a comment) | a space is, at most, a `choose` callable — or a part of the one handed in for the player's person |
| DELIBERATE | `engine/season/loop/deliberate.py:1` (*"owns **nothing** … **token: none**"*), `:68` (`deliberate(self, choose, …) -> list[Act]`); it calls `choose(p, v, s, ask_budget)` once per person (`:169`) | a space runs inside a map that holds no token, so it **cannot** write; it returns `Act`s |
| the inputs | `View`, `engine/season/state/carriers.py:379-409` (ids only; any world reach raises `Forbidden`, `:404-409`); `Question`, `:412-431`; `Candidate`, `:434-460`; the opening set, `decision/options.py:43` (`opening_set(p, v, q, fx) -> list[Candidate]`) | a space reads the player's own claims and the candidates the opening set already formed |
| the output | `Act`, `engine/season/state/carriers.py:508-550` | the only thing a space hands back |
| the fold | `resolve`, `engine/season/loop/resolve.py:815`; `_fold`, `:296`; `_apply_write`, `:744`; under an ACTS token minted at `loop/driver.py:452`; the write itself through `World.write`, `engine/season/state/world.py:791` | every carrier change a space causes happens **here**, under RESOLVE's token, against a `write_matrix.yaml` row |

Layer 1 states the discipline once: **"A module with no token cannot write, and that is the whole of the
write discipline"** (`architecture/meta/04_CODE_ARCHITECTURE.md:158`).

**Two rules follow, and they bind all three spaces.**

1. **A space ranks and selects; it never forms.** It chooses among the `Candidate`s
   `decision/options.py:43` formed. A space that minted a candidate the opening set did not form would
   be a second option generator for the player alone — *shape divergence* (`CLAUDE.md` §10). The
   automated chooser (`decision/choose.py:291`, `make_chooser`) and the playable space read the same
   candidate set, so they emit the same act shapes.
2. **A space owns no writer.** Every Person write below is an effect body's, a step's, or one of the
   fold's two post-outcome writes — `_scar_witnesses` and `_conviction_crisis`
   (`loop/resolve.py:503`, `:579`), which are neither an effect body nor a step: they run inside `_fold`
   (`:499`) after any act whose outcome moved state, under that act's ACTS token, through `World.write`
   with a `Change`, each against a `write_matrix.yaml` row. **A player's act therefore writes OTHER
   persons' `scar` and `conviction`** (its observers', the actor included at the shipped
   `scar_excludes_actor=False`, `data/fixtures.py:589`), not only its own person's fields. The space
   reads what those writers did, next round, through the player's own View and Person fields.

### 1.1 The Person fields, their rows, and who writes them today

`Person` is `engine/season/state/carriers.py:557-626`.

| field | carrier | write-matrix row (`engine/season/write_matrix.yaml`) | live writer at `867c1c3f` |
|---|---|---|---|
| `capability` | `:565` | **none** — `Person.capability` is on `retired:` (`:393-394`), so no season write is licensed | world-gen only: `build_at` seats a cast entry's authored dict (`engine/season/harness/corpus_run.py:536-539`); read by `seam/wrappers/sigma.py:75` (`_capability`) and `:90` (`_pool_of`) via `rosters.yaml` `verb_capability` (`engine/season/rosters.yaml:1049`) |
| `stance` | `:566` | `:219-231`, [RES, ENC], `stance.moved` | `march`: `_eff_march`, `engine/season/loop/effects_combat.py:183` (stance rows written at `:261-266`) |
| `pursuits` | `:567` | `:179-189`, [RES], `pursuit.moved`, **`unproduced:` (H-62)** | world-gen only: `seed_pursuits` (`engine/season/harness/run_cases.py:44`) via `corpus_run.py:525` and, for the realm, `harness/populated.py:699-700` (the cast row's authored pursuits first, the draw as fallback) |
| `ledger` | `:571` | `claim_ledger`, `:164-170`, [WIT], INTERIOR — *"`witness` the only minter, and it is not an act"* | WITNESS |
| `body` | `:581` | `:154-163`, [MAT, RES, ENC] | the `fight` effect `_eff_kill` (`effects_combat.py:33`, body written at `:156`), `march` (`:257-259`), MATTER |
| `scar` | `:592` | `:208-218`, [RES, ENC], `scar.taken` | the fold's `_scar_witnesses` (`loop/resolve.py:503`, called from `_fold` at `:499`) after any act whose outcome moved state: **one count per observer** (the actor included at the shipped `scar_excludes_actor=False`) **per violated pursuit or held affiliation**, ACTS token, [RES, ENC]. `{element: count}` over **two rosters** — the pursuits and the affiliations, refused a shared name. `_scar` and `scar_step` are retired (H3) |
| `conviction` | `:600` | `:190-200`, [RES, ENC], ACTS, social, `conviction.moved`, **`unproduced:`** (no verb declares it) | `_conviction_crisis` (`loop/resolve.py:579`), called by `_scar_witnesses` (`:576`): see §5. `{affiliation: intensity}`, ints 0-5, absent = not held. **Inert on shipped data:** filled at realm build from the cast row's `affiliations:` (`harness/populated.py:703`, `data/cast.py:216` `conviction_of`), no row authors any, so every shipped person holds `{}` |
| `exists` | — | `:201-207`, [MAT, RES, CEN], `person.individuated` | CENSUS, which writes nothing (`engine/season/loop/census.py:30-40`) |

`confliction` is **derived** (`engine/season/queries/person_q.py:160`) from `conviction` and the loaded
`incompatible` relation, and never stored.

---

## 2. Creation — where a person comes from

**Today.** Nothing in the season loop constructs a `Person`. Every construction is in `harness/`:
`corpus_run.py:510` (a case's cast), `populated.py:438` (cohorts) and `:671` (the realm), plus
`headless.py:71`, `scarce.py:105`, `governance_spine.py:130`. `loop/matter.py:96-98` records the grep
that makes it so. CENSUS owns individuation and generates nobody (`loop/census.py:30-40`, *"demand-driven
only; generated nobody"*); what *demands* an individuation is hole `H-51`, grade `absent`, owner
unassigned (`engine/season/hole_register.yaml:582-593`).

**The design: two arms, and neither emits an act or writes `World`.**

| | creation, arm C1 — before the first season | creation, arm C2 — a person who appears mid-campaign |
|---|---|---|
| **typed input** | the persons the world builder has **already seated** (`corpus_run.py:510`'s cast, `populated.py:671`'s realm). The player reads each one's person-side fields — `capability`, `pursuits`, `conviction` — and picks one | the individuated person, once CENSUS writes `(Person, exists)` (`write_matrix.yaml:201-207`) |
| **acts emitted** | **none** | **none** |
| **carrier reached, and how** | **none.** C1 writes nothing to `World`. The choice is which person's `choose` the playable mode dispatches on: `deliberate` calls `choose(p, v, s, ask_budget)` once per person (`loop/deliberate.py:169`), so the playable `choose` branches on `p.id` and the driver (`loop/driver.py:355`) is handed that one callable. The carriers it reads were each written once by world-gen: `capability` (`build_at`, `corpus_run.py:536-539`), `pursuits` (`build_at`, `:525`; the realm, `populated.py:699-700`) and `conviction` (the realm builder only, `populated.py:703`; `build_at` fills none) | `Person.exists`, by CENSUS under its MATTER token (`loop/census.py:1`); the space only reads the result |

**Why this is the arm, and why there is no cast-entry arm.** The proposal first drafted C1 as *one cast
entry of the shape `build_at` already reads*, with the player's authored `pursuits`. The B-H review found
that shape has nowhere to be written: the corpus cast shape is the closed `CAST_KEYS = ("who", "role",
"capability", "office", "ought")` (`corpus_run.py:312`), with no `pursuits` key; `build_at` draws a
person's pursuits from the case id, not from the entry (`:525`); a `WAITS-ON-PLAYER` entry is never seated
and is refused for carrying a `capability:` at all (`:204`, `:220`, `:393-394`); and F.6
(`architecture/meta/04_CODE_ARCHITECTURE.md:1153`) is a statement about `capability`'s season writer only
(*"world-gen writes it once; nothing else does"*), not a licence for a player-authored entry. So C1 takes
the fallback: **the player picks a person the cast already holds.** Every authored difference a player
makes after that moves to development — which has no writer for `capability` or `pursuits` until B-Q
(§3), so until then a player cannot author a difference at all.

**Why creation emits no act.** Choosing a person is not a World write. An act that wrote `capability`
at RESOLVE would be development's `train`, not creation. Arm C2 is not the space's to trigger: an
individuation's demand is H-51, and a space that minted persons would be the generator S29 forbids
(`loop/census.py:34-40`).

---

## 3. Development — what writes a person after creation

**Typed input.** The player's own `View` (`carriers.py:379-409`), the `Question` it was built for
(`:412-431`, carried on the View at `:402`), the `Candidate[]` from `opening_set`
(`decision/options.py:43`), and the player's own Person fields — person-side state, the same inputs
`make_chooser` lists as admissible (`decision/choose.py:301-304`): `pursuits` (read through
`person_q.crisis_weights`, via `project`, `decision/options.py:221`), `stance`, `conviction` (read through
`confliction`, as the damping of the pursuit dot), `scar` (read through `crisis_weights`), the View and
the two Sensation scalars. No World.

**Acts emitted.** `Act`s (`carriers.py:508-550`) selected from those candidates, packed into scenes as
the automated chooser packs them (`decision/choose.py:389`, `pack_scenes`). The space **does not own
any verb below**; it reads what each writer did.

| field | the act that reaches it (through RESOLVE, `loop/resolve.py:815`) | exists at `867c1c3f`? |
|---|---|---|
| `capability` | `train` — IN-12 step 9, batch B-Q (`workplans/valoria_master_workplan_v9_part5.md:123`): it *"forms and writes `Person.capability` only where a case names a vocation"*, and un-retires `Person.capability` | **no.** `engine/season/verb_table.yaml` has no `train` row, and the field sits on `retired:` (`write_matrix.yaml:393-394`) |
| `pursuits` | `argue` (IN-12 step 9, same row, `:123`), after SC-02 `22b` step 24, the field's first producer | **no** — the row carries `unproduced:` (`write_matrix.yaml:186`); `argue` has no `verb_table.yaml` row |
| `scar` | **any act whose outcome moved state**, through the fold's `_scar_witnesses`, onto the act's **observers** (the actor among them at the shipped arm) | **yes**, live and shaped by H3; its affiliation side is dark on shipped data because every shipped `conviction` is `{}` |
| `conviction` | the same fold, through `_conviction_crisis`, when an observed act takes a held affiliation's scar to 3 | **yes, inert on shipped data** (no cast row authors an affiliation) |
| `stance` | `march`'s `Won`/`Lost` bands (`_eff_march`, `effects_combat.py:183`), at ENCOUNTER | **yes** — the one live interior verb writer (`write_matrix.yaml:219-231`) |
| `body` | `fight`, `march`, MATTER (`write_matrix.yaml:154-163`) | **yes** |

**What development may display.** The player's own fields and own claims only. A sheet that showed a
person's capability *relative to another's*, or the truth of a claim, would read world state through a
View, which raises (`carriers.py:404-409`). The sheet's derived lines (#445 §1.6: faculties, `command`,
standing as a perception gap, rank, and `confliction`) stay derived at read time; development stores none
of them. Four facts about `scar` and `conviction` the display must account for:

- **(a) Two rosters.** `scar` keys span the pursuits and the affiliations. A display separates them; one
  flat list of counts is two quantities.
- **(b) A crisis rewrites only `conviction`.** A folded or destroyed creed's `scar` count stays on a creed
  the person no longer holds, and the heir keeps its own count, already at threshold. A display shows a
  `scar` count against a held affiliation as live and against an unheld one as history.
- **(c) A fold's direction is the intensity's, not the content's.** Under the shared engagement column
  co-held creeds reach 3 in the same act, and the fold moves the higher-held creed into the lower — a
  coded `[ASSUMPTION; Jordan to correct]` (`queries/person_q.py:226`, `conviction_after_crisis`). A
  render must not narrate it as a judgment on a creed's content.
- **(d) A shifted weight is a derived line.** At a non-zero `scar_weight_shift` (shipped 0,
  `data/fixtures.py:601`) the chooser acts on `crisis_weights`' shifted weights, not on `Person.pursuits`.
  The shifted line is derived and never stored.

**Where development and the automated chooser differ.** Only in who picks. The automated mode is
`make_chooser` (`decision/choose.py:291`); the playable mode is the same candidate set picked by the
player. Same seed, same choices, same `World.content_hash()` (`engine/season/state/world.py:1275`) —
which is IN-46's falsifier applied here (`_part4:36`).

---

## 4. Chronicling — a person's own record of a life, and how it is read out

**Typed input.** Two, and they must not be confused.

- **In the simulation:** the person's own `ledger` (`carriers.py:571`) of `Claim`s (`:257-310`),
  deposited only at WITNESS (`write_matrix.yaml:164-170`) and read through `LedgerReader`
  (`engine/season/queries/person_q.py:315`), whose order is recency then confidence (#445 §1.4).
  Eviction ranks on confidence and recency **and nothing else** — salience is excluded by signature
  (`architecture/meta/04_CODE_ARCHITECTURE.md:1057`, row 39; `architecture/meta/07_DYNAMICS.md:174`).
- **Outside the simulation:** the cause graph — `Event`s (`carriers.py:197-198`) and their `causes[]`,
  which `state/attribution.py`'s `actor_of` walks (`state/attribution.py:71`). This is `STORY-READ`
  (`proposals/2026-10-04-forcing-churn-and-the-story-bar.md:169`): *"an observer outside the simulation
  that finds arcs in the cause graph … Layer 1 forbids salience ranking inside the sim"*, realised as
  proposal 1, the chronicle render (`proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md:14`).

**Acts emitted: none.** **Carrier reached: none.** Chronicling is a reader. A person's record is the
ledger the loop already writes; the life-story told from it is a render, and a render that ranked
events by importance inside the loop would be salience-ranked memory. So the space has two outputs,
both outside `World`: the ledger as the person holds it (unknowns stay unknown, false beliefs stay
believed — #445 §1.4), and the out-of-sim render over `causes[]`, which may rank because it is not the
simulation.

**What neither input records: a scar or a conviction crisis.** Both writers call `World.write` **without
`emits`** (`loop/resolve.py:572`, `:614`; both docstrings say *"Nothing is emitted"*, `:523`, `:591`;
`scar.taken` and `conviction.moved` are declared on their rows and no code emits them). So no `Event`, no
`causes[]` edge and no WITNESS deposit exists for a scar count moving, or for an affiliation's fold or
destruction. The ledger and the `causes[]` render **record neither**; chronicling can show only the
**present values read from the person's own fields** (`scar`, `conviction`), never when or by whose act a
count rose or a creed folded. Giving the render that history is an emission, which is a writer's change
(the row's `emits:`), not a space's. Two display rules from §3 bind the render as well: a creed's
fold direction is the intensity's, not the content's ((c)), and a count on an unheld creed is history
((b)).

**A name collision, stated so nobody resolves it silently.** `epistemic.py:528` has a WITNESS channel
named `chronicle` (`_ch_chronicle`, the matter-of-record channel). It is a deposit rule the loop owns;
the chronicling space neither owns nor calls it. IN-12 step 10's *"chronicle deposit"* (`_part5`, the
step-10 row) is that channel.

---

## 5. IN-08's carriers — what the B-H review read

The `### IN-47` entry (`_part4:39-44`) has the review read the carriers IN-08 creates (`Person.scar`,
`Person.conviction`). At `867c1c3f` both exist:

- **`Person.conviction`** — `engine/season/state/carriers.py:600`; row `write_matrix.yaml:190-200`,
  [RES, ENC], ACTS, social, `unproduced:` because no verb declares it. `{affiliation: intensity}`, ints 0-5
  on `affiliation_roster.scale`, **absent = not held, never 0**. Filled at realm build from the cast row's
  `affiliations:` (`harness/populated.py:703`, `data/cast.py:216` `conviction_of`); no row authors any,
  so every shipped person holds `{}`. Moved only by `_conviction_crisis` (`loop/resolve.py:579`) when an
  observed act takes a held affiliation's scar to 3: the creed folds into the **highest-held
  incompatible co-holding** (clamped at 5), or is **destroyed** if it is the sole holding; the
  *restabilise* branch is **not built**. `confliction` is derived (`queries/person_q.py:160`), never
  stored. The review's answer to §3's old open line: development **displays** `conviction` and the
  derived `confliction`; it has no act of its own that reaches it.
- **`Person.scar`** — `carriers.py:592`; row `:208-218`, [RES, ENC]. Not "a bare per-axis dict" any
  more: `{element: count}` over pursuits and affiliations, one count per observer per violated element,
  written by the fold's `_scar_witnesses` after any act whose outcome moved state. **"Subject or actor"
  is answered: the act's observers**, the actor among them at the shipped `scar_excludes_actor=False`
  (`data/fixtures.py:589`). `_scar` and `scar_step` are retired. It **has readers**: `crisis_weights`
  (threshold 2, `queries/person_q.py:186`, dark at the shipped `scar_weight_shift=0`) and
  `conviction_after_crisis` (threshold 3, `:226`); `make_chooser` reads `pursuits` through
  `crisis_weights`, `stance`, and `conviction` through `confliction` (control `confliction_weight=0`,
  `data/fixtures.py:609`).

---

## 6. Review criteria

The review in B-H passes this design only if all four hold.

1. **THE FALSIFIER (IN-47's own, the `### IN-47` entry, `_part4:43`).** *A space that writes a `Person`
   field outside an act's fold contradicts A-25 and Layer 1's "a module with no token cannot write"*
   (`architecture/meta/04_CODE_ARCHITECTURE.md:158`) *and fails the review.* Check each space against
   §1.1: development writes only through acts RESOLVE folds; chronicling writes nothing; creation's C1
   writes nothing to `World` (it picks a seated person) and C2 writes nothing.
2. **No second option generator.** Every act a space emits was a `Candidate` from
   `decision/options.py:43` (§1, rule 1).
3. **No salience inside the simulation.** Chronicling's in-sim reader orders by recency and confidence
   only (`04:1057`); any ranking by importance lives in the out-of-sim render (§4).
4. **At the build (not this document's):** with the creation arm switched off, a seeded run reproduces
   the pre-build `World.content_hash()` (`_part4:43`); with chronicling switched on or off, the hash is
   identical, since it writes nothing.

---

## 7. What this depends on, and what is not verified

- **Writers this design reads and does not build:** `train` and `argue` (IN-12 step 9, B-Q), the first
  `pursuits` producer (SC-02 `22b` step 24), an authored `affiliations:` on any cast row (none exists, so
  `conviction` and the affiliation side of `scar` stay dark), and an owner for H-51 (none). Until those
  land, development can display and choose but moves `stance`, `body` and `scar`; `conviction` has a
  writer that is inert on shipped data.
- **No build position exists** (`_part4:43`): R-04 conjunct (3) cannot read `met` for this row until
  one does; `_part3` §B.0 places it once this design is reviewed
  (`workplans/valoria_master_workplan_v9_part3.md` §B.0, rules R4 and R7, `:220`, `:223`).
- **Not re-run here:** the row's count of 429 of 430 built persons with empty `capability`
  (`engine/season/requirements.yaml:78-80`, measured 2026-10-02). Not re-opened here: Jordan's
  2026-09-30 *"design one character sheet"*, which the plan entry itself tags `[UNVERIFIED]`.

---

## Review at B-H

A terminal record, kept where its subject lives (`CLAUDE.md` §0); it dies with this document.

**Date:** 2026-10-08, at HEAD `867c1c3f`. **Verdict: PASSES WITH CORRECTIONS.** An independent read-only
critic reviewed the draft against the carriers; each correction below was re-opened in the tree by the
producer before it was written.

**The falsifier does not fire.** No space writes a `Person` field outside an act's fold. Development
writes only through acts RESOLVE folds (and the fold's two post-outcome writes, now named in rule 2);
chronicling writes nothing; C1 writes nothing to `World`; C2 writes nothing.

**C1 outcome: the fallback.** The cast-entry arm had no shape to write into (§2); C1 is now *the player
picks a person the world builder already seated*, and the playable `choose` dispatches on that `p.id`.

**Corrections applied (eight):**

1. §4: chronicling cannot see a scar or a conviction crisis; both writers emit nothing, so the ledger and
   the `causes[]` render record neither.
2. §1.1, §3, §5, §7: the `scar` writer is the fold's `_scar_witnesses` (one count per observer per violated
   pursuit or held affiliation); `_scar` and `scar_step` are retired; development moves `stance`, `body` and `scar`.
3. §1.1, §3, §5, §7: `Person.conviction` exists, with its row, its realm-build source, its one crisis writer
   (inert on shipped data) and the derived `confliction`; the "does not exist" claim is deleted.
4. §3, §5: `Person.scar` has readers (`crisis_weights`, `conviction_after_crisis`); the chooser's inputs are
   listed as they now stand.
5. §2, §6: C1 rewritten as the fallback; `Person.conviction` (realm builder) added to its carrier list.
6. §1 rule 2, §3, §4: scar keys span two rosters; a crisis rewrites only `conviction`; the fold direction is
   the intensity's; a shifted weight is derived; a player's act writes other persons' `scar` and `conviction`.
7. Preamble: the framing no longer "names" three spaces; A-25 places one management space.
8. Every `file:line` re-derived at `867c1c3f`; the cites to `_scar`/`scar_step` (`effects_combat.py:39-106`,
   `:245`; `fixtures.py:599`) are deleted, and the plan cites now name the `### IN-46`/`### IN-47` entries.
   The `loop/resolve.py`, `queries/person_q.py` and `decision/choose.py` cites were re-derived again, by
   symbol, at the batch's close commit.

**Not decided here.** The review is done. Status stays **PROPOSED** and **HELD BACK**; whether the hold
lapses is not this review's call and is Jordan's, per the plan entry.
