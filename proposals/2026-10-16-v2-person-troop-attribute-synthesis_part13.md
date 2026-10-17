# Persons, attributes and verbs: the v2 synthesis — part 13: Part VI.5, threadwork (TW)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-v2-person-troop-attribute-synthesis.md) (§0, Part I Persons) · [`_part2`](2026-10-16-v2-person-troop-attribute-synthesis_part2.md) (Part II Attributes) · [`_part3`](2026-10-16-v2-person-troop-attribute-synthesis_part3.md) and [`_part4`](2026-10-16-v2-person-troop-attribute-synthesis_part4.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`_part5`](2026-10-16-v2-person-troop-attribute-synthesis_part5.md) and [`_part6`](2026-10-16-v2-person-troop-attribute-synthesis_part6.md) (Part IV What verbs do to the world) · [`_part7`](2026-10-16-v2-person-troop-attribute-synthesis_part7.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`_part8`](2026-10-16-v2-person-troop-attribute-synthesis_part8.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`_part9`](2026-10-16-v2-person-troop-attribute-synthesis_part9.md) PC · [`_part10`](2026-10-16-v2-person-troop-attribute-synthesis_part10.md) MB · [`_part11`](2026-10-16-v2-person-troop-attribute-synthesis_part11.md) SC · [`_part12`](2026-10-16-v2-person-troop-attribute-synthesis_part12.md) FI · **this file** TW · [`_part14`](2026-10-16-v2-person-troop-attribute-synthesis_part14.md) GV · [`_part15`](2026-10-16-v2-person-troop-attribute-synthesis_part15.md) FA · [`_part16`](2026-10-16-v2-person-troop-attribute-synthesis_part16.md) EC · [`_part17`](2026-10-16-v2-person-troop-attribute-synthesis_part17.md) WT · [`_part18`](2026-10-16-v2-person-troop-attribute-synthesis_part18.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`_part19`](2026-10-16-v2-person-troop-attribute-synthesis_part19.md) PC+NP · [`_part20`](2026-10-16-v2-person-troop-attribute-synthesis_part20.md) MB+FA · [`_part21`](2026-10-16-v2-person-troop-attribute-synthesis_part21.md) SC+GV · [`_part22`](2026-10-16-v2-person-troop-attribute-synthesis_part22.md) FI+TW · [`_part23`](2026-10-16-v2-person-troop-attribute-synthesis_part23.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `TW §3.n` (for example `TW §3.9` for its items for Jordan). Gap ids (`TW-G01` …) resolve in Part VII (`_part22`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`_part3` §III.5; where this section and the roster disagree, the roster governs):

- R-02: `knot` is TW's.
- R-10: `sever` → `dissolve` is adopted in the rename batch.
- R-13: TW owns `thread_read`.
- R-16: `release` stays; no `renounce`.
- R-26: `mend` is Mending; `restore` is fabric repair only.

---

# TW — threadwork

Lane: TW (the canonical operations on threads, Mending, the Calamity). Scope: `thread_read`, `weave`,
`mend`, `sever`→`dissolve`, `lock`, `loosen`, `pull`, past-pulling, `leap`, `ward`, `anchor`, `trace`,
Thread Sensitivity, knots. Gap register rows TW-G01…TW-G42
(Part VII (`_part22`)). Tree read 2026-10-16. Every `file:line` below was opened in
this session unless tagged. Source tags: **L&S** = Lewis & Short via `etym_tool.py ls`; **Wikt** =
en.wiktionary via `etym_tool.py en|la`; `[MEMORY]` = a game mechanic named from my own knowledge;
`[UNVERIFIED]` = a link I could not check.

**Headline rulings (each argued below).**

1. **`mend` is Mending** — the act that repairs the thread-substrate (another's configuration, a
   Locked Zone, a held shape, the lattice that holds the Calamity back). **`restore` is not Mending**;
   it stays the fabric repair it is in code (`verb_table.yaml:862-883`, writes `Site.condition`, no
   Thread Sensitivity gate). The mender's own coherence recovery is **not a second verb**: its elastic
   half is a side effect of every Mending that takes (`operations.py:523-531`, `:575-577`), and its
   resting-point half is `mend` aimed at oneself (`operations.py:549-557`, `:572-573`). Critic V-01
   answered; IN-35's "(the `restore` arm)" (`valoria_master_workplan_v9_part5.md:125`) is re-pointed
   at `mend` by the revert clause the roster itself wrote (`rosters.yaml:2321-2327`).
2. **The code's two cost regimes give two pairs** (`operations.py:375-440`): Weaving ↔ Pulling
   (cost = scale; "Things Cohere" / "Things Open") and Locking ↔ Dissolution (cost = scale +
   `FR_SURCHARGE`, flat Mending-Stability −1; "Unable to Become" / "Unable to Be"). **`lock` gets its
   own row** (v2's fold into `weave` is reversed; V-07 applied). **`sever` is renamed `dissolve`**
   (V-08 applied) and earns its row by writing what Locking does not: the end of the target and a
   residue.
3. **`leap` is a stage of every operation, not a verb** (canon §6.2: "the crossing that makes an act
   an operation at all", `06_operations.md:114-117`). It owns the Thread Sensitivity gate, the Leap
   roll and the involuntary knot. **`trace`** folds into `thread_read` (a knot route).
   **Past-pulling** folds into `pull` (a recency target); `pull` is PARKED on P-09's orphan carrier.
4. **`ward` is a floor verb** (every magic system in the genre has a protective operation): NEW ROW,
   built with the first hostile operation it can oppose, resolved by the built
   `opposing.py::resolve_opposing_operations` (`opposing.py:102`). **`anchor` is CULLED**: canon says
   self-maintenance is not an operation (`06_operations.md:34-35`), and its one effect is a context
   read already owned by `coherence.recover`'s `environment_in_equilibrium`.
5. **`tie / knot` splits**: `knot` (the deliberate thread bond, `systems/fieldwork/sim/knots.py`) joins
   this subsystem; `tie` goes to SC/NP. **`loosen`** folds: one's own held shape → `release`;
   another's → `mend`.

Post-assessment TW lexicon: **7 rows** (`thread_read` [FI-owned row, TW gate], `weave`, `pull`
[PARKED], `lock`, `dissolve`, `mend`, `ward`) + **`knot`** (split from `tie / knot`) = 8 verb names
with rows; **6 folded names** (leap, trace, diagnose, past-pulling, loosen, heal); **2 culled names**
(anchor; `sever` as a name, renamed). Counted from §3.4 below, not from v2.

---

## 3.1 Subsystem mechanic

**What exists.** The resolver is `systems/threadwork/sim/` (1,950 lines, `wc -l`): `operations.py`
holds seven entry points — `attempt_leap`, `_weaving`, `_pulling`, `_past_pulling`, `_locking`,
`_dissolution`, `_mending` (`operations.py:27-34`) — over one `_resolve_operation`
(`:290-348`): pool `(Spirit×2) + min(3, history+3) + ⌊TS/10⌋` (`:235-247`), TN 7 (`:73`), Ob from
`DEPTH_OB` / `MENDING_OB` / a recency table (`:77-92`, `:406-408`), cost by scale
(`COHERENCE_COST_BY_SCALE`, `:128-136`) plus `FR_SURCHARGE = -1` for Locking and Dissolution
(`:140`, `:429`, `:438`), and a blanket −1 on Partial/Failure except Mending (`:321-323`).
`coherence.py` owns the practitioner's state (`resting_point`, `elastic_displacement`; `recover`
`:341`, `mend_resting_point` `:380`); `opposing.py:102` resolves two practitioners contesting;
`collective.py:71` resolves a shared working; `co_movement.py` **writes nothing**
(`:15-21`); `systems/fieldwork/sim/knots.py` exists.

**What the module writes.** Only the actor's Coherence store (`charge_working`, `:277-287`) and, for
Mending, the mender's elastic return or resting point (`:494-509`, `:592-611`). **No operation writes
its target.** `mending_stability_delta` is "REPORTED, written nowhere" (`:211-213`, `:459`).

**What the season loop has.** One row: `thread_read` (`verb_table.yaml:1206-1219`), `writes: []`,
`requires_typed: none`, "NOT in `resolvable_verbs()`" (`:1212`). The write matrix declares
`(Person, coherence)` at RES, "unproduced … the verb table carries none that does"
(`write_matrix.yaml:171-179`); `Person` has **no** coherence or sensitivity field
(`state/carriers.py:645-709`, read; grep for `coherence` in that file returns nothing). Nothing under
`engine/` imports `systems.threadwork` (grep `threadwork` in `engine/**/*.py`: hits only in tests and
`dice_engine.py`). `rosters.yaml:2157` lists `threadwork: loop_resident`. `Site.condition`
(`carriers.py:727-732`) and `Tenure` (`:75-106`) are the carriers an operation's target effect can
land on. **Lacks:** a seam call, a coherence and a sensitivity carrier on `Person`, any target write,
the Calamity's coupling (IN-35, unbuilt: grep `calamity|lattice` in `engine/season/**/*.py` returns
two test files only).

## 3.2 Convention floor

The in-tree index records **no** game or historical precedent for threadwork
(`research/00_INDEX.md:177`, `:257`). The floor below therefore rests on named games, each `[MEMORY]`
with the specific mechanic, plus the tree's own canon where it states the act.

| floor act | precedent | TW verb | state |
|---|---|---|---|
| **Perceive the magical** (detect, read an aura, sense the other side) | Ars Magica, the Technique *Intellego* ("I perceive") [MEMORY]; Skyrim, *Detect Life* (Alteration) [MEMORY]; Blades in the Dark, the *Attune* action (perceive the ghost field) [MEMORY]; canon §6.2 (`06_operations.md:63-80`) | `thread_read` | **shipped** row, unresolvable (`verb_table.yaml:1212`) |
| **Make / bind / shape** (constructive working) | Ars Magica *Creō*, *Rēgō* [MEMORY]; Mage: the Ascension, Spheres worked "conjunctionally" to create effects [MEMORY]; canon "Weaving" (`cross_scale_action_catalogue_v1.md:716`) | `weave` | **designed** (v2 V076); module built |
| **Hold / fix / paralyse** | Ars Magica *Rēgō* (control, holding a thing as it is) [MEMORY]; Skyrim *Paralyze* (Alteration) [MEMORY]; canon Locking, Locked Zones (`09_terminology.md:117`) | `lock` | **designed** (v2 folded into `weave`; reversed here) |
| **Destroy / unmake** (offensive working) | Ars Magica *Perdō* ("I destroy") [MEMORY]; Skyrim, the Destruction school [MEMORY]; Mage, the *Entropy* Sphere [MEMORY]; canon destructive type (`06_operations.md:199-202`) | `dissolve` (was `sever`) | **designed** (v2 V080 conditional) |
| **Heal / repair / restore what magic broke** | Ars Magica *Creō Corpus* healing [MEMORY]; Skyrim, the Restoration school's healing spells [MEMORY]; Dragon Age: Inquisition, closing Fade rifts as the player's signature act [MEMORY]; Pandemic, *Treat Disease* against cascading outbreaks [MEMORY]; Spirit Island, removing Blight before it cascades [MEMORY]; canon Mending (`06_operations.md:207-247`) | `mend` | **designed** (v2 V081); planned as IN-35's Mending arm (`_part5.md:125`) |
| **Protect / ward / counter** | Ars Magica, *Parma Magica* (personal magic resistance) and *Aegis of the Hearth* (a ritual ward over a covenant for a year) [MEMORY]; Skyrim, Restoration's *Ward* spells [MEMORY]; Mage: the Ascension, countermagic [MEMORY] | `ward` (protect); `mend` on a held shape (counter / dispel) | **designed** (v2 V142 PARK) |
| **Mind and memory** | Ars Magica *Perdō Mentem* (erase a memory) [MEMORY]; Mage, the *Mind* Sphere [MEMORY]; canon §6.7 (`06_operations.md:249-268`) | `pull` | **designed** (v2 V077 PARK) |
| **Pay the cost of magic, and recover from it** | Ars Magica, Warping and Twilight [MEMORY]; Mage: the Ascension, Paradox [MEMORY]; Call of Cthulhu, Sanity loss and recovery [MEMORY]; canon §6.8 (`06_operations.md:270-329`) | cost on every operation; recovery = `mend` aimed at oneself + elastic return | cost **built in module**; no row |
| **Bond to another through magic** | Ars Magica, the familiar's Bond (cords of the bond) [MEMORY]; canon knotting (`06_operations.md:154-163`); `knots.py` | `knot` | **shipped** as the slashed `tie / knot` row, no effect (`verb_table.yaml:1235-1245`) |
| **Collective ritual** | Ars Magica, ritual magic with assistants [MEMORY]; Blades in the Dark, a ritual as a long-term project clock [MEMORY]; canon §6.5 (`06_operations.md:165-177`); `collective.py:71` | a participants parameter on each operation (§3.3 suite B) | module **built**; no row |
| **Magic is feared, witnessed and persecuted** | Dragon Age, templars and apostates [MEMORY]; canon §6.1 "The Church's terror is not wholly misplaced" (`06_operations.md:54-56`); `rosters.yaml:2349-2354` (orthodoxy cells) | not a TW verb: each TW row is a witnessable deed carrying alignment cells; the persecuting verbs are GV/SC's | cells on `thread_read` only (`rosters.yaml:2349-2354`) |
| **Advance in magic by study** | Ars Magica laboratory study; Skyrim spell tomes [MEMORY] | **excluded by canon**: P-08 forbids thread-level competence "by study alone" (`10_constraints.md:32`) | absent by design (TW-G42) |

**Floor verdict.** Eight floor acts map to eight TW verb names (`thread_read`, `weave`, `lock`,
`dissolve`, `mend`, `ward`, `pull`, `knot`). The cost-and-recovery act and collective ritual are
parameters and side effects of those verbs, not verbs (argued in §3.3). Study is excluded by canon,
and the exclusion is a design fact, not a gap to fill.

---

## 3.3 Suites

Six suites, one stage. The stage comes first because every operation row composes on it.

### 3.3.0 The Leap — a stage of every operation, not a verb

- **What it is.** Canon: "The Leap is the suspension of layer-two self-rendering, undertaken to reach
  layer three" (`06_operations.md:63`); "every operation requires one and self-maintenance requires
  none" (`:37-38`); "It is the crossing that makes an act an operation at all" (`:116-117`). Knots form
  during it, directionally, along the operation's channel (`:131-134`).
- **Mechanic.** `attempt_leap` (`operations.py:351-372`): TS ≥ 30 or an eligibility Failure; Ob 2 at
  TS 30-49, 1 at 50+; no Coherence of its own. ⚠ **No operation calls it today**: the six other entry
  points go straight to `_resolve_operation` (`:375-440`, `:565-569`), so in the module a weave never
  rolls a Leap (v2's own finding, `_part8.md:586`, holds against the code).
- **Why not a verb.** A player never chooses "leap" for its own sake: alone it produces nothing but a
  knot with no operation behind it, and canon's one stand-alone Leap, the perceptive Thread-Read, is
  `thread_read` itself (`cross_scale_action_catalogue_v1.md:631`, "Thread-Read as Perceptive Leap").
  It is not an outcome or a parameter either: it is the **first stage of every TW row**, with its own
  roll and its own world effect (the knot). Criterion 6 is met by the host rows, which name the knot
  as one of their writes.
- **World effect.** (a) the TS gate (Person.thread_sensitivity, **named gap M2**); (b) on Failure the
  act ends with no Coherence cost (`operations.py:355-356`; but see C-TW-3, the blanket −1 still
  mis-hits a Leap Partial/Failure, `:319-320`); (c) on success, an **involuntary directed `knot`
  Tenure** from actor to target (§3.3 F; **named gap M3**) — the same kind the `knot` verb opens, so
  the kind has two openers [ASSUMPTION — basis: canon names both "knots" (`06_operations.md:131-134`,
  `:156-157`); a kind with an opener *set* is what loader invariant 6's open second conjunct asks to be
  declared, `verb_table.yaml:860`]. (c) is what gives `thread_read` a RESOLVE
  write, so the orthodoxy scar can fire (`rosters.yaml:2334-2335`: the scar "is earned only by an
  outcome that MOVED state").
- **Gaps.** Closes TW-G20 (one Leap owner on every row), TW-G07 (a RESOLVE write). Leaves TW-G21 (the
  vulnerability window: "environment × duration plus type × scale", `10_constraints.md:39`) PARKED —
  no carrier for the environment term, and the magnitudes are unruled.
- **Disposition.** FOLD as a stage (not a named verb). **Falsifier:** an operation row resolves without
  calling the one Leap owner, or a Leap that succeeds leaves no knot.

### 3.3 A · Perceive — host `thread_read`

- **Host.** `thread_read` — SHIPPED row (`verb_table.yaml:1206-1219`), **owned by FI** (one of six
  inquiries, `:1137`); TW owns its gate, its Leap stage and its cost. Effect today: `writes: []`,
  `emits: finding.made` (a Claim minted at WITNESS into the actor's own ledger).
- **Folded acts.**

  | act | same actor? | same mechanic? | parameter/content only? | line |
  |---|---|---|---|---|
  | `trace` (follow a strand to its source through a knot) | yes, the sensitive | yes: "standard Thread-Read pool, TN 7, Ob 2 (Personal scale)" (`cross_scale_action_catalogue_v1.md:680-681`) | yes: the route (through a knot the actor holds) and its price (+1 knot strain; the knotted party may detect it, `:681-683`) | passes |
  | `diagnose` (detect that something was pulled, or that a working was done) | yes | yes: Thread-Read on a person, "detectable by TS 30+ Diagnosis" (`02_canon_constraints.md:50`) | yes: the finding kind (a displacement in the target's configuration) | passes |

- **World effect.** Writes: the Claim (WITNESS, as `examine`); the Leap stage's `knot`; and the
  canon cost "−1 Coherence at Relational+ , +1 Exposure" (TW-G05; `verb_table.yaml:1219` records it as
  "NOT EXPRESSED HERE"). Lacks: M1 (the seam that charges `(Person, coherence)`), M2 (the gate), M3
  (the knot), FI's content yield (FI-G01), and for `diagnose` the P-09 displacement deposit (M9).
- **NERS.**
  - **N.** Cut it and no person can perceive the substrate: every other TW row needs a target the actor
    has seen, and canon's information-gate alternative ("Thread-Read a site … instead of talking to
    the NPC", `cross_scale_action_catalogue_v1.md:653-654`) dies. Top-down: the Church's anti-threadwork
    theology needs a witnessable working to fear (`rosters.yaml:2349`). Bottom-up: TS is the design's
    one class gate (`hole_register.yaml:1062`); without its act TS gates nothing. Lateral: `examine`
    covers the material layer only. No false N-line: nothing else ruled in reads the substrate.
  - **R.** A sensitive gets a route to information no non-sensitive has (P-03 asymmetry,
    `10_constraints.md:27`); the route has a price (Coherence, Exposure, being detected through a knot),
    so it is a choice, not a dominant act. R-WORLD: a detected trace (`:681-683`) throws a hook with no
    player present.
  - **S.** One pool and one TN with the operations (`operations.py:235-247`); pauses correctly (the
    Leap stage is the pause). S defect carried, not mine to fix: the thread pool is a second ladder
    for one quantity (TW-G27, J-T6).
  - **E (last).** One row with two finding contents is the minimum that keeps both N-lines; a separate
    `trace` row would repeat the pool for a different route.
- **Precedent.** §3.2 row 1.
- **Gaps closed.** TW-G03, G05, G07, G16 (via M9), G19. **Open:** G04 (authored values, M2), G42 (no
  acquisition, by canon).
- **Disposition.** REBUILD (row stands; it lacks a gate carrier, a cost and a RESOLVE write). **Falsifier
  (KEEP):** a resolvable `thread_read` changes no carrier at RESOLVE, or a non-sensitive (TS < 30)
  executes it.

### 3.3 B · Cohere and Open — host `weave`; `pull` its own row, PARKED

The code's first pair: Weaving and Pulling share a cost regime (cost = scale, `operations.py:381-394`)
and the Partial/Failure Mending-Stability override (`:332-334`).

**`weave`** (Weaving, "Things Cohere", `operations.py:376`).

- **Folded acts.**

  | act | same actor? | same mechanic? | parameter/content only? | line |
  |---|---|---|---|---|
  | a collective weave (several practitioners on one target) | each participant acts in his own voice with the same verb | yes: `collective.py::attempt_collective_operation(actors, op_type, …)` (`collective.py:71`) | yes: the participant list, read at RESOLVE from same-tick acts naming one target | passes (the same rule serves `lock`, `dissolve`, `mend`; not a workaround, since no participant's act is another's reply) |

- **World effect.** Writes: the weaver's `(Person, coherence)` (cost by scale; M1); **a held-load
  Tenure** `weave`, subject = weaver, object = target, live while held (M6; v2's build condition
  "the held load as a Tenure the weaver owns (no fourth clock)", `_part8.md:464`); the Leap stage's
  `knot`. The held load is canon's manipulative type: "It stands only while it is held, and the holding
  is the practitioner's. The load persists for as long as the shape does" (`06_operations.md:195-197`).
  The weave ends by the holder's `release` or by another's `mend` (§3.3 D). Lacks: **the target-side
  reader** — what a live weave changes in the target's resolver (a Site's wear, a formation's
  Discipline, a person's contest). That is named gap M6, against TW, not a reason to hide the verb.
  The live held loads in a territory are also **the strain IN-35 needs** (TW-G12; K-WR-4,
  `WR_world.md:543`).
- **NERS.**
  - **N.** Cut it and the only chosen act that takes on a held load dies (v2's corrected N-line,
    `_part8.md:614`); with it die IN-35's person-made strain (the Calamity then worsens only
    ambiently) and the manipulative branch of canon's taxonomy. Diagonal: MB loses its Thread→Mass
    hand-off source (TW-G30). False N-line check: `lock` also holds, but holds the target as it is;
    nothing else ruled in imposes a new shape.
  - **R.** A load the weaver must carry season after season, paid in Coherence, is a strategic
    commitment; the shape is customizable by target and scale. R-WORLD: an unattended weave keeps
    straining the lattice and can be mended away by a rival.
  - **S.** Same pool, TN, cost table as its siblings; up-scale via breadth (`BREADTH_OB`,
    `operations.py:105-111`) to formation and region.
  - **E.** One row, scale and target as parameters. The ordinary word names exactly the act.
- **Precedent.** §3.2 row 2.
- **Gaps.** Closes TW-G01, G02, G12 (with M5), G25, G31, G38. Open: G30 (MB hand-off, PARKED).
- **Disposition.** NEW ROW. **Falsifier:** an executed `weave` opens no held-load Tenure, or its
  Tenure is read by nothing (ID-13).

**`pull`** (Pulling, "Things Open", `operations.py:388-394`; memory pulling, canon §6.7).

- **Folded acts.**

  | act | same actor? | same mechanic? | parameter/content only? | line |
  |---|---|---|---|---|
  | past-pulling (Past-Oriented Pulling) | yes | yes: `_resolve_operation` via `attempt_past_pulling` (`operations.py:397-414`) | yes: the target is a past moment; the Ob is read off its recency (`:406-408`) and the cost carries −1 (`:409`) | passes |

- **World effect (when built).** Writes: the puller's `(Person, coherence)`; the knot; and **a
  displaced-claim deposit** in the target's ledger — canon: the pulled memory "becomes an orphaned
  configuration", "a skilled diagnostician can detect that something was pulled"
  (`06_operations.md:255-257`). Under the append-only log that must be a **new deposit, not an edit**
  (v2's trigger, `_part8.md:468`; K-WR-2 `WR_world.md:538`). Named gap **M9**. Also Temporal
  Disjunction (P-11), which has no carrier.
- **NERS.** **N:** the only candidate act that weakens a claim in another's ledger (v2 `_part8.md:581`);
  cut it and memory magic, a genre staple (§3.2 row 7), is gone. **R:** detectable, costly, messy by
  canon (P-09), so it is a risk, not an eraser. **S:** the twin of `weave`'s cost regime.
  **E:** past-pulling as a recency target keeps one row.
- **Disposition.** PARKED as an own row (not CULLED: it is floor). **Trigger:** a carrier for P-09's
  orphan as a new ledger deposit exists (M9). Do not retire `attempt_pulling` / `attempt_past_pulling`.
  **Falsifier (of the park):** a design for M9 that edits an existing Claim (breaks the append-only
  log) — then PARK stands and the form changes.
- **Gaps.** TW-G14, G15 PARKED with it.

### 3.3 C · Preclude and Unmake — `lock` and `dissolve`, two rows on one cost regime

The code's second pair: identical bodies, cost = scale + `FR_SURCHARGE` (cap-exempt, PP-196), flat
Mending-Stability −1 at every degree (`operations.py:335-336`, `:417-440`). **Two rows, not one**: their
world effects are opposite in kind (fix what is / remove what is), canon types them differently
(Locking manipulative, Dissolution destructive: `02_foundations_amendment_leap_mechanism.md:70-72`,
read under its SUPERSEDED banner for the taxonomy; `06_operations.md:195-202` keeps the three types),
and the value term reads the verb alone (`_part8.md:88-104`, §V.2.1), so one row would make a Locking
and a Dissolution the same deed to every witness.

**`lock`** (Locking, "Unable to Become", `operations.py:418`).

- **Why not a `weave` parameter (V-07).** v2 folded it as "a preclusion parameter that `mend` reads"
  (`_part8.md:466`). The fold fails the test: same actor, yes; **same mechanic, no** — the cost regime
  differs (`FR_SURCHARGE`; flat MS −1 vs `weave`'s by-degree override, `operations.py:332-336`);
  **parameter only, no** — the effect differs (a weave imposes a new shape the weaver holds; a lock
  precludes all becoming in the target). English agrees: one locks a door, one does not weave it.
- **World effect.** Writes: the locker's `(Person, coherence)` (scale + FR); the knot; **a `lock` on
  the target** — for a Site, the Locked Zone shape: becoming precluded, so the target's mutable carrier
  (`Site.condition`) is refused change by any writer, wear and repair alike, until a `mend` restarts it
  (`06_operations.md:207-214`; `09_terminology.md:117`: "Persists indefinitely, because the process
  that would undo it is the one precluded"). Carrier: a Tenure kind `lock` read by the write gate as a
  refusal (named gap **M6**). Lacks: the gate reader; the Person-target form (what "unable to become"
  freezes in a person) is not designed — first build Sites only.
- **NERS.** **N:** cut it and the world loses the one act that freezes a place, the mechanism of the
  Locked Zones canon is built on, and `mend`'s paradigm target (canon's Mending is defined against a
  Locked Zone, `06_operations.md:207-214`). Lateral: protects a site from wear, so it is also a
  (dangerous) defensive choice. **R:** a tempting fix with a canonical cost: it stops ruin and stops
  recovery together; R-WORLD: a lock outlives its locker and becomes someone else's problem.
  **S:** a write-gate refusal is the tree's existing shape for "this cannot change" (precondition
  refusals). **E:** one row; the word is the plain one.
- **Precedent.** §3.2 row 3.
- **Gaps.** Closes TW-G23 (with `dissolve`), G24, G38; contributes to G12/G41 (MS −1 into M5).
- **Disposition.** NEW ROW (v2's MERGE reversed). **Falsifier:** a locked Site's `condition` moves
  under wear or `restore`, or a `lock` is undone by anything but `mend`.

**`dissolve`** (Dissolution, "Unable to Be", `operations.py:435`) — **renamed from `sever`**.

- **Rename (V-08 applied).** The code and canon name the operation Dissolution. English *dissolve* is
  the ordinary word for ending a thing's being as a unit ("dissolve a partnership", "the sun dissolved
  the ice"); *sever* is "to cut free" (Wikt), which names cutting a link — the wrong act, and in this
  tree a link is a Tenure that D-5 protects. Latin supports the fit but is not the reason: L&S
  *dissolvō* cites Lucretius "dissolvunt nodos omnes et vincla relaxant" and Tibullus of "stamina"
  (threads) — the word was used of knots and threads.
- **World effect (what Locking does not write — TW-G23's condition).** Writes: the dissolver's
  `(Person, coherence)` (scale + FR); the knot; and **the end of the target**: for a Site, its
  `condition` driven to the floor (the fabric unmade); for a held shape (`weave`, `lock`), the Tenure
  closed *destructively* (contrast `mend`, which closes it restoratively); plus **a residue mark** on the
  place — canon's "dissolution residue fields" (`06_operations.md:363`) and the orphan structure of
  destructive work (`:199-202`). Carrier for the residue: named gap **M10**. Not in its domain: social
  Tenures (`hold`, `oblige`, `tie` …): D-5 refuses the second-person lever on obligations
  (`verb_table.yaml:861`). Closing another's *thread* Tenure follows `seize`'s precedent for "a
  non-consensual act on another's edge" (`verb_table.yaml:904`). Person-aimed dissolution (harm to a
  body) is the offensive floor act; it writes `Person.body`, so it is flagged to PC (§3.8).
- **NERS.** **N:** cut it and the subsystem has no offensive or destructive operation — a floor act
  (§3.2 row 4) — and no way to unmake a lock or weave except by restoring it, which canon says is a
  different act with a different cost. False N-line check: `lock` does not remove; `fight` removes
  bodies but not fabric or held shapes. **R:** the most costly op (FR surcharge), so a desperate choice;
  R-WORLD: residue persists and propagates. **S:** shares `lock`'s cost regime. **E:** one row.
- **Disposition.** NEW ROW (was v2 KEEP WITH CONDITIONS; the condition is met in design by the end +
  residue writes; built after `weave`/`mend`/`lock`). **Falsifier:** a built `dissolve` writes exactly
  what `lock` writes (then PARK, per v2's TW closest call 2, `_part8.md:674`).
- **Gaps.** TW-G23, G24, G25 (sever is not weave's inverse), G38.
- **Release invariant (applies to `lock`, `weave`, `ward`).** `release`'s `domain:` must equal
  `tenure_kinds \ {contain}`, asserted at load (`verb_table.yaml:851`, `:858`). Every new Tenure kind
  this lane names therefore gets `release` as its owner's closer. For `weave` that is wanted (the
  loosen fold, §3.5). For `lock` it means **the locker may release his own lock while he lives; after
  him only `mend` undoes it** [ASSUMPTION — basis: the invariant, plus `09_terminology.md:117`, which
  makes the Locked Zone outlast the process, not the locker's choice]. For `knot` it collides with canon
  (§3.3 F, §3.9 item 2).

### 3.3 D · Mending — host `mend`

**The ruling on critic V-01 (mend / restore).** IN-35 reads "Mending as persons' acts (the `restore`
arm)" (`valoria_master_workplan_v9_part5.md:125`) and states its own need: "thread operations as a
carrier, so strain can be an act's consequence (H-85, plan `33`)" (`:128`). So the plan put Mending on
`restore` *because no thread verb existed*. The roster then declined `restore` as Mending: `restore`
"raise[s] a Site's `condition` … a repair of fabric, not a thread operation. With no way to tell a
Mending from mending a wall, carrying the cell would scar every orthodox witness of a house repair.
**Revert: a thread-operation verb or a restore kind exists**" (`rosters.yaml:2321-2327`). The WR lane
recommends the same split (K-WR-3: "Let the thread Mend be the Mending, keep `restore` for fabric",
`WR_world.md:539`). The fold test settles it on the code, not the word:

| fold `restore` into `mend`? | same actor? **no**: `restore` admits anyone present (`verb_table.yaml:864`, `:867`); Mending needs TS ≥ 30 (`operations.py:95-102` via the Leap stage) | same mechanic? **no**: `_eff_restore` → `_rise`, uncontested, no degree (`verb_table.yaml:881`); Mending rolls `MENDING_OB` (`operations.py:565-569`) | parameter only? **no**: fabric vs substrate | **fails — two acts** |
|---|---|---|---|---|

So: **`mend` names the world-repair act on the substrate** (canon's Mending, "Repairing the Substrate",
`operations.py:514`). **`restore` stays fabric repair, an EC/GV verb, not TW's.** The mender's own
coherence recovery is not a verb: its elastic half is the side effect every Mending that takes hands the
mender (`operations.py:523-531`), and its resting-point half is `mend` aimed at oneself (below). v2's
premise that the Calamity's arm belongs to `restore` (`_part8.md:217-218`) is withdrawn with IN-35's
revert; V-01's reading ("v2's 'mend lowers the Calamity' was the semantically correct reading") is
upheld. English agrees and is not the reason: *mend* ← *ēmendō*, L&S "to free from faults, to correct,
improve, amend".

- **Folded acts.**

  | act | same actor? | same mechanic? | parameter/content only? | line |
  |---|---|---|---|---|
  | mend oneself (move one's own resting point) | yes | yes: `attempt_mending`, `target['configuration_of'] = 'self'` (`operations.py:549-557`, `:572-573`) | yes: the target | passes |
  | mend another person (reach *his* resting point: E-1's second route) | yes, the mender | yes: `attempt_mending` aimed at another's configuration (`:549-551`) | yes: the target; ⚠ today it moves nothing of the target's (`:561-563`), so the effect is a gap, not a different mechanic | passes |
  | unlock (restart becoming in a Locked Zone) | yes | yes | yes: the target is a `lock` | passes |
  | undo another's weave (v2's "loosen, another's") | yes | yes | yes: the target is a held shape; canon: restoration "lets the target go where it is oriented" (`06_operations.md:298-299`) | passes |
  | hold back the Calamity (mend a lattice site) | yes | yes | yes: the target is a lattice Site | passes |
  | heal (a body, by threadwork) | yes | yes | yes: the target is a person's body. ⚠ [ASSUMPTION — basis: the superseded amendment lists "healing operations" as restorative, `02_foundations_amendment_leap_mechanism.md:66`; live canon §6.6 warns that restoring "a remembered state" is manipulation, `06_operations.md:235-238`, so a heal that aims at "how the body was" is a `weave`] | passes, conditionally |

- **World effect.** Target, by kind: a `lock` closed (`Tenure.until`); another's `weave` closed; a
  lattice Site's `condition` raised through the shared `_rise` owner (M5; `restore` refuses the lattice
  kind, so there is still one owner of the arithmetic and no wall repair holds the Calamity back); a
  target person's resting point (M7); a body (`Person.body`, flagged to NP/PC). Mender: elastic return
  through the seam (`(Person, coherence)`, M1) or his own resting point (self-aim). The knot. Costs 0
  Coherence (ED-871; `operations.py:449-451`). `mending_stability_delta` is 0 by `price_mending`
  (`:490`), so its Calamity effect must be the lattice write, not that report. Lacks: M1, M5, M7.
- **Self-mending is free and repeatable (TW-G09).** The module says so: "an attempt costs nothing
  (ED-871), so repeated casts can walk a permanent set to 0", against C-1's "extremely difficult"
  (`operations.py:162-167`). The difficulty belongs in the self-aim Ob (the module's own reading). It
  is a magnitude, so it ships as a swept fixture with control = today (H-94's precedent, the shape
  `RESILIENCE_GAIN_SWEEP` already uses, `:156`). Named in M7.
- **NERS.**
  - **N.** Cut it and: no restorative operation exists (canon's paradigm, `06_operations.md:193`); no
    act undoes a lock, so every Locked Zone is permanent; the drift ratchet has no door (C-1, ruled;
    `:291-294`); the Calamity is held back by nothing chosen (IN-35's D1 answer: "Mending acts hold the
    balance", `_part5.md:346`); heresy loses its most sympathetic accused (TW-G13). **False N-line
    check:** `restore` — fails the fold test above; elastic return by rest — moves only elastic
    displacement and needs an equilibrium environment (`coherence.py:341-375`), never the floor or a
    lock. Both checked; neither supplies what dies.
  - **R.** R-PLAYER: the knife-edge is a real choice — restart the tending and "let it go where it
    goes", or aim at a remembered state and make it a weave (`06_operations.md:229-243`). R-WORLD:
    menders against an expanding Calamity is the setting's standing drama; it runs unwatched.
  - **S.** Zooms from a person (self, another) to a site to a territory's lattice with one row and a
    `MENDING_OB` by scale. S defect carried: `MENDING_OB` is a second Ob ladder beside `DEPTH_OB`
    (`operations.py:87-92`) — canon-sanctioned ("a separate scale",
    `cross_scale_action_catalogue_v1.md:709`), so recorded, not fixed here.
  - **E (last).** One host, six targets; the fold test passes for each; nothing a player needs is
    lost. A separate `heal` or `unlock` row would repeat the pool and the cost for a different target.
- **Precedent.** §3.2 row 5 (Restoration-school healing; DA:I rift-closing; Pandemic's Treat Disease
  against outbreaks; Spirit Island's Blight cascade — the last two are the closest shape to IN-35's
  coupling: a spreading threat held back only by repeated local acts).
- **Gaps.** Closes TW-G08, G09 (M7), G10 (M7), G12 (M5), G13, G18 (with the `anchor` cull), G41 (M5).
  Contributes to G39.
- **Disposition.** NEW ROW. **Falsifier:** a lattice site's band crossing is prevented by `restore`
  (the split failed), or a `mend` on a `lock` leaves the lock live.

### 3.3 E · Protect — host `ward`; `anchor` CULLED

**`ward`.**

- **World effect.** Writes a Tenure `ward` (warder → a person or a Site) with a `Term` of one season
  (the field `oblige` already uses, `state/carriers.py:96-106`); the Leap stage's knot. **Reader:**
  the TW resolver — an operation aimed at a warded target resolves through
  `opposing.py::resolve_opposing_operations(actor_a, actor_b, op_type, target, …)` (`opposing.py:102`)
  with the warder as the second practitioner, and the warder pays the opposed working's cost then
  (named gap **M8**). Breadth lets one ward cover a place (`BREADTH_OB`, `operations.py:105-111`).
- **Fold test against `lock`** (a lock also stops a hostile change): same actor, yes; same mechanic,
  no (`attempt_locking` vs an opposed roll); parameter only, no — a lock precludes *all* becoming,
  the target's own included. Fails; two acts.
- **NERS.**
  - **N.** Floor (§3.2 row 6). Cut it and a party not acting has no protection against hostile
    workings (v2's own reversal, `_part8.md:583`). **False N-line check:** the target's layer 2 already
    "opposes the imposed shape" (`06_operations.md:285-287`) — passive, unchosen, and not routed to an
    opposed roll; `lock` protects by destroying the target's becoming. Neither provides a chosen
    defence.
  - **R.** An investment whose payoff shows later, or never — the HCC thesis's "retroactive audit of
    an earlier Fortify" (`WR_world.md:56`); R-WORLD: a ward that fires on a rival's working is a
    hook nobody scripted.
  - **S.** Reuses the built opposed resolver; no new arithmetic. Lateral collision: `guard` (PC's
    bout posture) is the same Germanic word through French (Wikt: "guard is a parallel form which came
    via Old French"); critic V-19's doublet is real but the senses are separated by subsystem.
  - **E.** One row; the genre's own word.
- **Build condition.** Ships in the batch with the first hostile operation (a person- or site-aimed
  `lock`, `dissolve`, `pull` or non-consensual `weave`) that executes in the loop; before that its
  Tenure would have no reader (ID-13). This is when it is built, not whether (floor).
- **Gaps.** Closes TW-G17 (M8).
- **Disposition.** NEW ROW, build-gated (v2 PARK reversed to a scheduled row). **Falsifier:** a warded
  target is hit by an operation that does not route through `opposing.py`.

**`anchor`** — CULL.

- **What it was.** "Resisting loss of self" (v2 `_part4.md:43`), first merged into `mend`, then cut
  (`_part8.md:473`).
- **Why it is not a verb.** Canon: self-maintenance "maintains one *as* a finite ordinary human … So it
  is not an operation" (`06_operations.md:34-35`). Its only candidate effect is the equilibrium of
  where one stands, which is a fact the caller supplies to `recover`
  (`operations.py:544-548`; `coherence.py:347-351`), not something an act writes. Fold test into
  `mend`: same actor, yes; same mechanic, **no** (no roll, no Ob, no Leap); fails — so it cannot be a
  folded content either. It is a context read.
- **Floor check.** Nothing a floor act needs dies: recovery from magic's cost is kept by `mend`
  aimed at oneself (the floor) and elastic return (the time path; its licence is §3.9 item 1).
- **Name note.** `co_movement.py:48` has a card "Anchor Settling" (a Thread Witness Node stabilises);
  it is a card name with no loop reader, so the cull leaves no collision.
- **Falsifier (CULL).** A design shows a chosen act, distinct from rest and from Mending, that writes
  coherence — then it is a verb, and K-WR-8's "rest a person chooses" (NP) is its likelier home.

### 3.3 F · Bond — `knot` (split from `tie / knot`)

- **The split (TW-G33).** The shipped row is `tie / knot`, one opener for two kinds, rated "each word
  FITS; the ROW is a MISFIT" by the earlier pass (gap register TW-G33). `tie` (marriage, fealty: the
  social bond) leaves for SC/NP; `knot` stays here.
- **Fold test into `weave`.** Same actor, yes; same mechanic, **no**: `knots.py::form_knot` (prereqs
  Disposition ≥ 5, Bonds ≥ 5, either party TS ≥ 30; TN 7, Ob 2;
  `cross_scale_action_catalogue_v1.md:675`), not `attempt_weaving`; fails — own row.
- **World effect.** Writes the actor's **directed** `knot` Tenure to the partner (04 §A.3 row 9: "two
  directed edges, one owned by each party", quoted at `verb_table.yaml:1240`); a strain gauge
  (−5..+5, rupture at 5, `cross_scale_action_catalogue_v1.md:676-678`) whose carrier is unlocated
  (ED-912; TW-G35); the involuntary knot of §3.3.0 is the same kind with a different opener. Readers:
  the knot-mediated read (§3.3 A, `trace`); drift propagation (P-12, distance-independent,
  `10_constraints.md:36`); `_ch_witness_key`, which today reads the edge **undirected** (TW-G34). Lacks:
  the partner operand (H-182), the strain carrier, a directed reader (all M3).
- **NERS.** **N:** cut it and every knot is involuntary, formed only toward what one has operated on;
  the chosen bond (canon §6.4 "deliberate or organic binding", `06_operations.md:156-157`) and the
  familiar-bond floor act die. False N-line check: involuntary knots give a channel, but not to a
  chosen ally. **R:** rupture (Disposition −3, Coherence −1) and a detectable remote read make a bond
  a liability as well as an asset. **S:** the knot is canon's one propagation channel, so every scale
  reads it. **E:** one row once split.
- **Disposition.** REBUILD (split the row; the TW half keeps `knot`). **Falsifier:** an executed `knot`
  writes an edge nothing reads, or is read undirected.
- **Gaps.** TW-G32, G33, G34, G35 (M3); G36 PARKED on the attribute-input ruling (V-2a).

---

## 3.4 Lexicon table

Chains: English ← Middle English ← intermediate ← Latin (principal parts; attested sense) ← PIE.
Sources per link: **W** = Wiktionary English page, **Wl** = Wiktionary Latin page, **LS** = Lewis &
Short, all fetched this session with `etym_tool.py`. A link not on a fetched page is `[UNVERIFIED]`.
Fit is judged by ordinary current usage (ED-IN-0179); no fit verdict rests on the root.

| verb | suite | status | mechanic and world effect (carrier written) | etymology chain with sources | fit (ordinary usage, ≤20 words) | rename |
|---|---|---|---|---|---|---|
| `thread_read` | A Perceive | SHIPPED (REBUILD) | Thread-Read pool via the Leap stage; Claim to own ledger (WITNESS); knot; `(Person, coherence)` at Relational+ | **Germanic compound, no Latin path.** *thread* ← ME *thred* ← OE *þrǣd* ← PGmc *\*þrēduz* ← PIE *\*terh₁-* (W); Latin *terō, terere, trīvī, trītum* 'to rub' is a **cognate, not an ancestor** (Wl). *read* ← ME *reden* ← OE *rǣdan* ← PGmc *\*rēdaną* ← PIE *\*Hreh₁dʰ-* (W); Latin *reor, rērī, ratus sum* 'to reckon; think' is from \*h₂reh₁-, which Wl calls a reanalysed root of \*h₂er-; W's *read* page also carries the root template \*h₂er-: cognate at the root, not an ancestor | FITS: "read the threads" is the plain image; snake-case compound is the tree's, not English | — |
| `trace` | A Perceive | FOLDED → `thread_read` | knot route: +1 knot strain, detectable by the knotted party | **Latin path, partly.** *trace* ← ME *tracen* ← OF *tracer* ← probably VL *\*tractiō* ← L *trahō, trahere, trāxī, tractum* 'to draw, drag, or haul' (LS), 'drag, pull; extract, draw out' (Wl); conflated with OF *traquer* ← *trac* ← MDu *treck* (W). PIE: **disputed** — *\*dʰregʰ-* is uncertain; De Vaan (as quoted on Wl) proposes a non-Indo-European source | FITS: "trace a call / trace it to its source" is ordinary | — |
| `diagnose` | A Perceive | FOLDED → `thread_read` | finding kind: a displacement in a person's configuration (needs M9) | **Greek through Latin.** back-formation from *diagnosis* ← NL/L *diagnōsis* ← Gk *διάγνωσις* ← *διαγιγνώσκω* 'distinguish' ← PIE *\*ǵneh₃-* (W) | FITS: canon's own term ("Diagnosis", `02_canon_constraints.md:50`); ordinary medical sense matches | — |
| `leap` | stage | FOLDED (a stage of every operation; not a verb) | `attempt_leap`: TS gate, Ob 2/1; on success the involuntary knot | **Germanic, no Latin.** ME *lepen* ← OE *hlēapan* ← PWGmc *\*hlaupan* ← PGmc *\*hlaupaną* ← PIE *\*klewb-* (W; cognate Lith. *klùbti* 'stumble') | STRAINED as a verb (one does not "leap" a working); FITS as canon's noun, "the Leap" | — (noun only) |
| `weave` | B Cohere/Open | NEW | `attempt_weaving`; `(Person, coherence)`; held-load Tenure `weave` (M6); knot; strain for IN-35 | **Germanic, no Latin.** ME *weven* ← OE *wefan* ← PWGmc *\*weban* ← PGmc *\*webaną* ← PIE *\*webʰ-* (W). No Latin cognate on the fetched page. (The intransitive *weave* 'wind in and out' is a different word, probably ON *veifa*, W) | FITS: "weave a spell" is ordinary English; the thread image is literal | — |
| `pull` | B Cohere/Open | PARKED (own row) | `attempt_pulling`; `(Person, coherence)`; displaced-claim deposit (M9); knot | **Germanic, uncertain origin.** ME *pullen* ← OE *pullian*, "of uncertain ultimate origin"; related Fris. *pûlje*, MDu *pullen*, LG *pulen*, Icel. *púla* (W). No PIE root, no Latin | FITS for memory ("pull a memory", "pull a thread"); STRAINED for canon's general "Things Open" | — |
| `past-pulling` | B Cohere/Open | FOLDED → `pull` (PARKED with it) | recency-priced Ob (`operations.py:406-408`), −1 extra cost | as *pull*; *past* ← ME *passed*, pp. of *passen* ← OF *passer* ← VL *\*passō* ← L *passus* ← PItal *\*pattus* ← PIE *\*peth₂-* (W *past*, *pass*) | STRAINED: a coinage, but transparent; a content name only, never a row | — |
| `lock` | C Preclude/Unmake | NEW | `attempt_locking` (scale + FR); `(Person, coherence)`; Tenure `lock` read by the write gate (M6); knot; MS −1 | **Germanic, no Latin.** verb ← ME *locken/lokken* (from the noun) and *louken* ← OE *lūcan* ← PWGmc *\*lūkan* ← PGmc *\*lūkaną*; noun ← OE *loc* ← PGmc *\*luką* ← PIE *\*lewg-* (W). W notes English *luxe* "related … via Latin" (L *luxus*, through *\*lewg-*): **cognate, not ancestor** | FITS: "lock it in place", "locked" = cannot change; canon's "Locked Zone" | — |
| `dissolve` | C Preclude/Unmake | NEW (renamed from `sever`) | `attempt_dissolution` (scale + FR); `(Person, coherence)`; target ended (`Site.condition` to floor; a held shape's Tenure closed); residue (M10); knot | ME *dissolven* (c. 1374) ← L *dissolvō*, with the sense from AN *dissoldre* / OF *dissoudre* (W) ← L *dissolvō, dissolvere, dissolvī, dissolūtum* 'to loosen asunder, to unloose, disunite, separate, dissolve, destroy' (LS; Lucr. 6.356 "dissolvunt nodos omnes"); also 'abolish, annul' (Wl) ← *dis-* + *solvō* 'loosen, untie, undo; dissolve, break up; destroy' (Wl) ← *sē-* + *luō* 'untie, set free' (Wl) ← PIE *\*lewh₁-* (W) | FITS: canon's operation is Dissolution; "dissolve" = end a thing as a unit | — |
| `sever` | C | CULLED as a name (→ `dissolve`) | — | ME *severen* ← OF *sevrer* ← L *sēparō, sēparāre, sēparāvī, sēparātum* 'to disjoin, sever, part, divide, separate' (LS) ← *sē-* 'apart' + *parō* 'arrange, prepare' (Wl) ← PIE *\*perh₃-* (Wl). Doublet of *separate* (W). Critic V-08's VL *\*seperāre* is not on the fetched W page, which derives OF *sevrer* from *sēparāre* directly | MISFIT for Dissolution: "sever" = cut a link, not unmake a thing | `dissolve` |
| `loosen` | C/D | FOLDED (own weave → `release`; another's → `mend`) | own: `release` closes the `weave` Tenure; another's: `mend` on a held shape | **Germanic (Norse), no Latin path.** *loose* + *-en* (W); *loose* ← ME *loos* ← ON *lauss* ← PGmc *\*lausaz* ← PIE *\*lewh₁-* (W) — the **same root** as *solvō*/*dissolvō*: **cognate, not ancestor** | FITS ordinary "loosen a knot", but names no act distinct from its two hosts | — |
| `mend` | D Mending | NEW | `attempt_mending`; target by kind (lock, weave, lattice Site via `_rise`, a person's resting point, body); mender's elastic return or resting point; knot; 0 Coherence | ME *menden*, aphetic of *amenden*, or from AN/OF *amender* (W) ← L *ēmendō, ēmendāre, ēmendāvī, ēmendātum* 'to free from faults, to correct, improve, amend' (LS; Cic. *Leg.* 3.13.30), also 'cure; atone for' (Wl) ← *ē-* 'out' + *mendum* 'a fault, error, blunder in writing' (LS) ← PIE *\*mend-* (W's root template; the page's source comments it as doubtful). Latin sense = correct a fault (text, conduct); English = repair, recover ("on the mend"); century of shift not stated by a fetched source | FITS: "mend" = repair what is torn; canon's Mending | — |
| `heal` | D Mending | FOLDED → `mend` (conditional) | target = a body (`Person.body`, flagged NP/PC) | **Germanic, no Latin.** ME *helen* ← OE *hǣlan* ← PWGmc *\*hailijan* ← PGmc *\*hailijaną* ← PIE *\*kéh₂ilos* (W); derived from the adjective behind *whole* (W) | FITS | — |
| `ward` | E Protect | NEW (build-gated) | Tenure `ward` with a season `Term`; routes hostile operations to `opposing.py` (M8); knot | **Germanic, no Latin.** ME *warden* ← OE *weardian* ← PWGmc *\*wardēn* ← PGmc *\*wardōną/\*wardāną* ← PIE *\*wer-* (W) 'to keep in safety, watch over, guard; defend, protect' (W senses). *guard* is the parallel form via Old French (W). Latin *vereor, verērī, veritus sum* 'have respect for, revere; fear' is a **cognate** under *\*wer-* 'heed' (Wl) | FITS: "ward off", "a ward" against magic is the genre's ordinary word | — |
| `anchor` | E Protect | CULLED | none (a context read on `recover`) | ME *anker* ← OE *ancor/ancra* ← L *ancora* 'an anchor' (LS), fig. 'refuge, support, hope' (Wl) ← borrowed from (or cognate with) Gk *ἄγκυρα* (W, Wl); PIE *\*h₂enk-* per the OED as cited on Wl, **disputed** by Beekes (pre-Greek substrate). Verb ← ME *anchoren*, from the noun or OF *ancrer* ← ML *ancorāre* (W). Modern spelling is a 16th-c. respelling after ML *anchora* (W) | STRAINED: "anchor oneself" is ordinary, but names no act canon admits | — |
| `knot` | F Bond | REBUILD (split from `tie / knot`) | `knots.py::form_knot`; directed Tenure `knot`; strain (M3) | **Germanic, no Latin.** ME *knotte* ← OE *cnotta* ← PWGmc *\*knottō* ← PGmc *\*knuttô* ← probably PIE *\*gnod-* (W). W "see also" L *nōdus* — compared, not given as an ancestor | FITS in the thread register ("knot two threads"); risk: "tie the knot" = marry, which is `tie`'s | — |
| `restore` | — (EC/GV) | not TW: listed for the V-01 ruling | `_eff_restore`: `Site.condition` (fabric); must refuse the lattice kind (M5) | ME *restoren* ← OF *restorer* ← L *restaurō, restaurāre* 'to restore (bring back to good condition from decay or ruin)' (Wl) ← *re-* + *\*staurō* ← PIE *\*steh₂-* 'stand' (Wl) | FITS for fabric repair; MISFIT as Mending (no Thread act) | — |
| `release` | — (owner: release's lane) | host of the "loosen, own" fold | closes the owner's own Tenure; must admit kind `weave` (invariant 6 already forces it) | ME *relesen* ← OF *relaissier* / *relaschier* = OF *re-* + *laissier* / *laschier* (Wikt OF) ← L *laxō, -āre* 'loosen, relax' (← *laxus* 'loose, slack'); *laissier* perhaps influenced by OHG *lāzan* (Wikt OF) ← PIE *\*(s)leg-* (Wikt la *laxus*). L *relaxō* is a parallel Latin compound, not the ancestor | FITS for letting go a held shape | — (see §3.5 on L-08) |
| `tie` | — (SC/NP) | leaves TW at the split | social bond (marriage, fealty) | Germanic, no Latin path: ME *teien* ← OE *tīġan, tīeġan* ← PWGmc *\*taugijan* ← PGmc *\*taugijaną* ← PIE *\*dewk-* 'to tug, draw' (W *tie*, verb) | FITS for the social bond | — |

**Count.** TW rows after assessment: `thread_read` (FI-owned), `weave`, `pull` (PARKED), `lock`,
`dissolve`, `mend`, `ward`, `knot` = **8 names with rows** (5 NEW, 1 PARKED, 2 REBUILD). Folded names:
`trace`, `diagnose`, `leap` (stage), `past-pulling`, `loosen`, `heal` = **6**. Culled: `anchor`, and
`sever` as a name = **2**. v2's post-trial TW was "9 → 4 + stubs" (gap register note 3).

---

## 3.5 Deduplication and culls

| group | ordinary-English relation | what I did | fold test / floor check |
|---|---|---|---|
| `mend` / `restore` | near-synonyms ("mend a wall", "restore a wall") | two rows in two subsystems: `mend` = Mending (TW), `restore` = fabric (EC/GV); IN-35's "restore arm" re-pointed to `mend` by the roster's own revert clause | fold fails on actor and mechanic (§3.3 D); no floor act lost: fabric repair stays `restore`'s |
| `lock` / `weave` | not synonyms ("lock" fixes, "weave" interlaces) | split (v2 MERGE reversed) | fold fails on mechanic (FR regime) and content (preclusion vs a new shape) (§3.3 C) |
| `sever` / `dissolve` / `loosen` | *loosen* and *dissolve* share PIE *\*lewh₁-* (cognates; W); *sever* = cut free | `sever` renamed `dissolve`; `loosen` folded into its two hosts | `loosen`-own → `release`: same actor (the holder), same mechanic (`release` closes an own Tenure), kind parameter only — passes. `loosen`-another's → `mend`: passes (§3.3 D). No floor act needs the word *loosen* |
| `lock` / `dissolve` | not synonyms | two rows on one cost regime | fold fails on content (fix vs unmake) and on V.2.1 (the value term reads the verb) |
| `ward` / `guard` | doublets (Germanic *\*wardōn*, *guard* through French; W) | `ward` = TW thread defence; `guard` = PC's bout posture | different subsystems and mechanics; collision recorded (§3.8) |
| `ward` / `lock` | both "protect" a target | two rows | fold fails (§3.3 E) |
| `anchor` / `mend` (self) | "anchor oneself" ≈ "hold oneself together" | `anchor` CULLED | fold into `mend` fails (no roll, no Leap); floor kept by `mend`-self + elastic return |
| `trace` / `thread_read` | different senses (follow vs perceive) but one act here | FOLD | passes (§3.3 A) |
| `pull` / `trace` | *trace* descends from L *trahō* 'drag, pull' (LS, Wl) | no action: no design claim may rest on a root (L-01) | — |
| `leap` / `thread_read` | different words | `leap` is a stage of every row, not `thread_read`'s alone (v2 re-target upheld) | not a fold: a stage |
| `knot` / `tie` | near-synonyms; "tie the knot" = marry | split the slashed row: `knot` TW, `tie` SC/NP | fold of `knot` into `weave` fails (knots.py mechanic) |
| `past-pulling` / `pull` | one act, a different target | FOLD | passes (§3.3 B) |

**Culls, with what dies.**

- **`anchor`.** Dies: a name. Nothing a floor act needs dies because recovery from magic's cost is
  `mend` aimed at oneself plus elastic return, and the equilibrium condition is already a caller-
  supplied context on `recover` (`operations.py:544-548`). Falsifier: §3.3 E.
- **`sever` (the name).** Dies: a word for cutting links, which this subsystem must not do to social
  edges (D-5). The act it named survives as `dissolve`. Falsifier: a reader who meets `dissolve` in play
  expects something other than "this stops existing" (ED-IN-0179 test).

**Critic findings on my verbs.**

| id | finding | disposition |
|---|---|---|
| V-01 | `mend`/`restore` double-cover Mending | **applied**: `mend` = Mending; `restore` fabric only; IN-35's arm re-pointed (§3.3 D) |
| V-07 | lock folded into weave though Locking's twin is Dissolution | **applied**: `lock` own row in the Locking/Dissolution suite |
| V-08 | `sever` coined where *dissolve* exists | **applied**: renamed. One correction to the critic's chain: W derives OF *sevrer* from L *sēparāre* directly; the VL *\*seperāre* step is not on the fetched page |
| V-03 | "each keeps a name" vs `loosen` merged without one | **applied** for TW: `loosen` is counted as a named folded content (§3.4), so the count matches the prose |
| V-18 | leap's re-target concerns a precondition | **agreed**, and taken further: leap is a stage, not a merge |
| V-19 | `guard`/`ward` doublet | **answered**: real doublet, separated by subsystem and mechanic; flagged to PC |
| L-01 | root sense used as design intent | **applied**: every disposition above rests on the row's reads/writes and ordinary usage; Latin notes are remarks only |
| L-08 | `release` carries the creditor's/jailer's word for closing one's own edge | **answered for TW only**: for a held shape, "release" is the ordinary word (one releases a hold, a grip, a spell). If `release`'s owner renames it `renounce`, the TW fold still holds (same act, same mechanic) but reads worse; flagged §3.8 |
| L-19 | `synonym_registry.yaml` has no verb entries | observation: the `sever`→`dissolve` rename would be one more unrecorded verb rename there |

---

## 3.6 Gap coverage table

One disposition per row. "closed by X once M*n*" = the verb closes it when the §3.7 mechanic exists.

| gap id | closed by (verb / suite) | PARKED (trigger) | OUT OF SCOPE (why) | STALE (cite tree) | DISPUTED (why) |
|---|---|---|---|---|---|
| TW-G01 | `weave`, `lock`, `dissolve`, `mend` (+ `pull` parked) once M1 | | | | |
| TW-G02 | `weave`/`lock`/`dissolve` (cost) and `mend` (feedback) once M1 | | | | |
| TW-G03 | `thread_read` and every operation's Leap stage once M2 | | | | |
| TW-G04 | Leap stage once M2 seeds TS from the registry (a parse rule for authored ranges such as "75–80" is part of M2) | | | | |
| TW-G05 | `thread_read` (Leap-stage cost at Relational+) once M1 | | | | |
| TW-G06 | §3.2 (all suites): game precedent supplied `[MEMORY]` per floor act; in-tree precedent still none (`00_INDEX.md:177`) and every number stays internal | | | | |
| TW-G07 | `thread_read` gains a RESOLVE write (the knot, M3) and every TW row carries cells (M4) | | | | |
| TW-G08 | `mend` (= Mending); `restore` = fabric (§3.3 D) | | | | |
| TW-G09 | `mend` (self-aim) once M7's self-aim Ob term (swept fixture) exists | | | | |
| TW-G10 | `mend` (another's configuration) once M7 routes it to the target's resting point | | | | |
| TW-G11 | | | not a verb: a consequence on the coherence carrier (P-15, `10_constraints.md:39`); K-WR-5 is a design ruling (§3.9 item 3) | | |
| TW-G12 | `weave`/`lock` (held loads = strain) and `mend` (lattice write) once M5 | | | | |
| TW-G13 | `mend` (own row with cells, M4) | | | | |
| TW-G14 | | `pull`: a P-09 displaced-claim deposit, appended not edited (M9) | | | |
| TW-G15 | | folded into `pull` as a recency target; parked with it (M9) | | | |
| TW-G16 | `thread_read` (`diagnose` content) once M9 | | | | |
| TW-G17 | `ward` once M8 and the first hostile operation executes | | | | |
| TW-G18 | `anchor` CULLED; `mend`-self + `recover`'s context cover it (§3.3 E) | | | | |
| TW-G19 | `thread_read` (`trace` content) once M2 and M3 (directed knot reader) | | | | |
| TW-G20 | the Leap stage of every TW row (one owner, `attempt_leap`) once M1 | | | | |
| TW-G21 | | Leap stage: the vulnerability window ("environment × duration plus type × scale") needs an environment carrier and ruled magnitudes (M11) | | | |
| TW-G22 | | | | FW §13.3 Q8 (`2026-08-18-fieldwork-architecture….md:1020`) rules "+0.15 Ob per wound everywhere; strike the flat `+1 Ob`"; XSC §7 `:728-729` is prose behind that ruling. The Leap stage reads the wound term from its one owner | |
| TW-G23 | `lock` and `dissolve` as two rows; `dissolve` writes the end and residue Locking does not (§3.3 C) | | | | |
| TW-G24 | renames: `dissolve` = Dissolution; `loosen` folded; every TW verb now maps to one `attempt_*` by name | | | | |
| TW-G25 | | | | corrected in v2 §V.4 (`_part8.md:613-615`); this lane keeps the corrections (`weave` = held load; `dissolve` is not `weave`'s inverse) | |
| TW-G26 | | | pool arithmetic, not a verb: `min(3, history+3)` (`operations.py:246`); K-WR-7 is a ruling on PP-624's reading | | |
| TW-G27 | | | pool ladder, not a verb: J-T6 "rides with J-13's scale remainder" (v2 head `:345-346`) | | |
| TW-G28 | | | cost arithmetic, not a verb: R-14's slot and gain are a swept fixture at control 0 (`operations.py:142-157`); attribute lane | | |
| TW-G29 | | elastic return per season: K-WR-8 ruling (a licensed clock on the being, or a rest a person chooses) — §3.9 item 1 | | | |
| TW-G30 | | Thread→Mass and the other hand-offs: an MB seam that reads a TW operation at breadth Formation+ (`modules/mass_battle/orchestration.py:333` is the empty hook); flagged §3.8 | | | |
| TW-G31 | `weave`, `lock`, `dissolve`, `mend`, `pull` (each a witnessable deed) once M1 and M4; the persecuting acts are GV/SC's | | | | |
| TW-G32 | `knot` (split) once M3 (partner operand, strain carrier) | | | | |
| TW-G33 | split `tie / knot` → `knot` (TW) and `tie` (SC/NP) | | | | |
| TW-G34 | `knot` once M3's directed reader replaces `_ch_witness_key`'s undirected read | | | | |
| TW-G35 | `knot` once M3 locates the strain gauge | | | | |
| TW-G36 | | `knot`/`weave`: the attribute-input form V-2a (`contests:` on the thread rows, v2's recommendation) — attribute lane | | | |
| TW-G37 | every TW row once M1 (the seam call makes `threadwork: loop_resident` true) | | | | |
| TW-G38 | the suites: five operation rows, each its own verb (§3.3 B-D) | | | | |
| TW-G39 | `weave`/`lock`/`mend` once M5 (the Calamity's motion traced to acts); the elastic-return half rides TW-G29 | | | | |
| TW-G40 | every TW row once M12 (a carrier for each of the three dimensions, P-01/P-14) | | | | |
| TW-G41 | `mend`/`lock`/`dissolve` once M5 consumes their effects in place of the cut scalar | | | | |
| TW-G42 | | | not a verb gap: P-08 forbids thread competence by study (`10_constraints.md:32`); TS is fixed (J-T4); `train` cannot raise it | | |

Tally (counted row by row): closed 29 · PARKED 6 (G14, G15, G21, G29, G30, G36) · OUT OF SCOPE 5
(G11, G26, G27, G28, G42) · STALE 2 (G22, G25) · DISPUTED 0. 29 + 6 + 5 + 2 = 42. Of the 29 closed,
6 close by a ruling or rename alone (G06, G08, G18, G23, G24, G33; G23 still needs M6/M10 to
execute) and the rest close "once M*n*" — none executes today.

---

## 3.7 Mechanics this subsystem needs (named gaps)

| id | mechanic | what it must write | verbs that wait on it |
|---|---|---|---|
| M1 | **The thread-operation seam**: a RESOLVE effect per TW row calling `operations.py` (the Leap stage first, one owner), charging Coherence through a seam Event; a coherence carrier on `Person` (resting point, elastic displacement) — the write-matrix row exists (`write_matrix.yaml:171-179`), the field does not | `(Person, coherence)`; `coherence.changed` | all |
| M2 | **Thread Sensitivity carrier and gate**: `Person.thread_sensitivity` seeded from the registry, plus a `REQUIRES_PREDICATES` entry (H-85) | the gate's read; seeding at world build | all (via the Leap stage) |
| M3 | **The knot**: a directed `knot` Tenure with a partner operand (H-182), a located strain gauge (ED-912), a directed reader | `Tenure` kind `knot`; strain | `knot`, the Leap stage, `trace` |
| M4 | **Cells**: alignment and affiliation cells (orthodoxy −, inner tradition +, …) on every TW row in `rosters.yaml`, not only `thread_read` (`rosters.yaml:2349-2354`) | data the scar reads | all (the heresy path) |
| M5 | **The Calamity coupling (IN-35)**: a lattice Site kind [ASSUMPTION — basis: IN-35 builds "on existing site kinds if the band table can key on territory", `_part5.md:124-125`; a kind is the narrowest discriminator that keeps `_rise` the one owner while letting `restore` refuse]; strain = live `weave`/`lock` loads and residue in a territory; `mend` raises lattice `condition` through `_rise`; `restore` refuses the lattice kind | `Site.condition` on lattice sites; band crossings (already emitted, `matter.py`) | `mend`, `weave`, `lock`, `dissolve` |
| M6 | **Held shapes**: Tenure kinds `weave` and `lock`; a target-side reader for a live weave; a write-gate refusal under a lock; `release`'s domain grows by invariant 6 | `Tenure` kinds; refusals | `weave`, `lock`, `mend`, `dissolve`, `release` |
| M7 | **Mending routing**: another-aimed Mending reaches the target's resting point; a self-aim Ob term as a swept fixture (control = today) | the target's coherence; the fixture | `mend` |
| M8 | **Opposed routing**: a `ward` Tenure (with a season `Term`) read by the TW resolver, which then calls `opposing.py` | `Tenure` kind `ward`; the opposed result | `ward` |
| M9 | **P-09's orphan**: a displaced-claim deposit appended to the target's ledger, readable by Diagnosis | a Claim kind | `pull`, `diagnose` |
| M10 | **Residue / Gap mark** on a Site after a Dissolution | a Site-side mark | `dissolve` |
| M11 | **The Leap's window**: an environment term (where the leaper stands) for P-15's risk | a read, plus ruled magnitudes | the Leap stage |
| M12 | **Three-dimension effects** (P-01/P-14): today co-movement writes nothing (`co_movement.py:15-21`) and Temporal Disjunction has no carrier | one write per dimension per operation | all |

---

## 3.8 Cross-subsystem flags

| other lane | verb | the flag |
|---|---|---|
| FI | `thread_read` (FI-owned row) | TW supplies its gate (M2), Leap stage, cost and knot; FI supplies its content yield (FI-G01). `trace` and `diagnose` are its contents. FI-G18 (TS the one allowed class gate) and FI-G52 (inquiries uncelled; the orthodoxy cells on `thread_read` exist at `rosters.yaml:2349-2354`) touch the same row |
| FI | `knot` | `knots.py` lives in `systems/fieldwork/sim/`; FI-G55 points here. The module's home and the verb's owner differ; I take the verb |
| EC / GV | `restore` | stays fabric repair, not Mending; must refuse the lattice Site kind under M5. v2's "`restore` keeps IN-35's fabric arm" (`_part8.md:221`) is withdrawn; whether `restore` still earns its keep on fabric alone is EC's call |
| SC / NP | `tie` | the social half of `tie / knot` (marriage, fealty) leaves TW at the split |
| owner of `release` | `release` | (a) the loosen-own fold puts kind `weave` in `release`'s domain (invariant 6 forces it anyway, with `lock` and `ward`); (b) `knot` is already in that domain (`verb_table.yaml:851`) against canon's "cannot voluntarily unmake them" (§3.9 item 2); (c) L-08's `renounce` rename would read worse for letting go a held shape |
| PC | `dissolve`, `weave` aimed at a body; the Leap stage | person-aimed destructive work writes `Person.body` (PC's carrier, `fight`'s write); the Leap's wound term is FW Q8's +0.15 Ob per wound; `ward`/`guard` doublet |
| NP | `mend` (heal content); elastic return | thread healing vs NP's `tend` (v2: heal/recover → `tend`); if K-WR-8 rules "a rest a person chooses", that act is NP's |
| MB | `weave`, `lock`, `dissolve`, `mend` at breadth Formation+ | Thread→Mass hand-off (TW-G30); `threadwork_check` is an empty hook (`modules/mass_battle/orchestration.py:333`) |
| GV / SC | charge, arrest, persecute | heresy needs the TW deeds witnessed (M4); the persecuting acts are theirs |
| WT / FA | the Calamity | territorial spread of lattice band crossings and travel through Calamity territory (`cross_scale_action_catalogue_v1.md:664-665`) read M5's state |

---

## 3.9 For Jordan

Tried first for each: superseded → irrelevant → design document → precedent → architecture.

1. **How Coherence's elastic return enters the season loop (K-WR-8, TW-G29).** A licensed clock on the
   being (like bodies), or the effect of a rest a person chooses (a verb, NP's). Not answerable below:
   the write matrix quotes Layer 1's three clocks as "exhaustive" (`write_matrix.yaml:176`), so the
   bodies-clock precedent (step 4) would overwrite ratified architecture, and the two options give
   materially different games (drift heals while you wait vs drift heals only if you spend a season on
   it). `anchor` is not the answer (§3.3 E).
2. **Are knots permanent?** Canon: the practitioner "cannot voluntarily unmake" his knots
   (`06_operations.md:140-141`; the catalogue: "Knots are constitutive, not contractual", `:683`).
   Layer 1: `release`'s domain must equal `tenure_kinds \ {contain}`, and it holds `knot`
   (`verb_table.yaml:851`, `:858`). Tried: precedence by ratification — Layer 1 is RATIFIED (ED-IN-0204);
   §6 is PROPOSED and itself flags permanence as "a legitimate but undischarged stipulation"
   (`06_operations.md:143-146`). That leans to the code, but the choice decides whether every operation
   leaves a lifelong mark — a different game either way. The fix in code, if permanent, is to exempt
   `knot` as `contain` is.
3. **What follows the crossing (K-WR-5, TW-G11).** P-15 requires a consequence gated by reach
   (`10_constraints.md:39`); no document gives its shape. Listed because the WR lane found it survives
   all five steps; it is not a verb and I propose none.

