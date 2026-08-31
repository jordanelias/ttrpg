# CITATION LEDGER — verification of THROUGHLINES_BRIEF v2 (D1–D12) against disk
# Working notes. Read-only verification; nothing edited outside this scratchpad. Nothing executed.
# Tree state: HEAD = f129ca7 (= origin/main), working tree clean, branch
# claude/fable5-pr343-adversarial-review-48gvs3.

## 0 · PROVENANCE DEFECT FOUND BEFORE ANY THROUGHLINE — THREE NAMED SOURCES ARE NOT ON `main`

`v2/EVENTS_AND_SWEEP.md`, `v2/F6_RULED.md`, `v2/THE_PARTITION.md` and `v2/MANIFEST.md` **do not exist
in the working tree.** They exist only at `origin/claude/fable5-pr343-adversarial-review-48gvs3`
(a7de398), one commit ahead of the squash-merge f129ca7 that became `main`.

- `git diff --stat HEAD origin/claude/…` = exactly those 4 files, 1,135 insertions.
- `git merge-base --is-ancestor HEAD a7de398` → NO. The merge took the branch as it stood *before* its
  final commit.
- **Consequence:** the corpus sweep (858 lines), Jordan's F6 flux ruling (112) and the partition
  document (136) — the three documents the closing section and D4/D5 rest on — are unreachable from
  `main`. Extracted to scratchpad via `git show a7de398:…` for this verification.
- D5's formula has a home on `main` (`01_ARCHITECTURE.md:1360`); the *ruling* that produced it does not.

---

## 1 · PER-THROUGHLINE VERDICTS

| # | verdict | note |
|---|---|---|
| D1 | **HOLDS with one clause BROKEN and one qualifier REQUIRED** | "no faction can be founded" is a withdrawn claim; "existence" needs defining |
| D2 | **HOLDS**; tuple is misquoted | disk has 9 fields, brief gives 8 |
| D3 | **HOLDS**; signature misquoted | `leaders(prop, c, observer)`, not `leaders(observer, faction, rung)` |
| D4 | **HOLDS, fully verified** | strongest-sourced throughline; one uncleared limb the brief omits |
| D5 | **HOLDS, fully verified** | subsumption by D4 is stated on disk, not merely inferable |
| D6 | **HOLDS, fully verified** | one refinement omitted (`opening_set` returns Candidates) |
| D7 | **CLAIM HOLDS; its ⚠ is WRONG in both halves** | "both claims were false" is false; see §3 |
| D8 | **HOLDS; every number in it is wrong** | 3→23 unsupported; correct is 3→20, of which 16 |
| D9 | **HOLDS, fully verified** | King at `:1084`, Duke at `:1506`; brief conflates, both on disk |
| D10 | **HOLDS, fully verified** | verbatim match to the runner disposition |
| D11 | **HOLDS, fully verified** | and a THIRD instance found, inside the deliverable — see §4 |
| D12 | **HOLDS**; its inherited citation is wrong by ~42 lines | cycles are at `03_COMPENDIUM.md:485-492`, not `:441-446` |

---

## 2 · D1 — the five-item proof, and what breaks

**The list itself VERIFIES.** `20_FABLE5_ADVERSARIAL_REVIEW.md:213-226`, each item re-checked against
`10_SUPERSEDING.md`:

| # | operation | cited | on disk |
|---|---|---|---|
| 1 | death | `SUP:648` | ✓ P1 SETTLE, "metabolism and nature only" |
| 2 | de-individuation | `SUP:654`, `:209` | ✓ P7 RECKON, "persons nobody remembers de-individuate" |
| 3 | claim eviction | `SUP:654` | ✓ "ledgers evict lowest salience" |
| 4 | individuation | `SUP:654`, `:203-204` | ✓ the single additive operation |
| 5 | holdings on death | `SUP:304-307` | ✓ hearth succession pointer |

"ALL FIVE ARE DECIDER-FREE. FOUR OF THE FIVE ARE SUBTRACTIVE" — ✓ arithmetic correct (4 is the additive one).

`holdings` as dead state — ✓ **exactly two occurrences** in `10_SUPERSEDING.md` (`:307`, `:352`), both
descriptive. Matches the review's §2.10 claim precisely.

### ⚠ BREAK 1 — "no faction can be founded" is a WITHDRAWN claim, resurrected

The brief lists it among D1's consequences. The review **withdrew it in full**:

- `20_FABLE5_ADVERSARIAL_REVIEW.md:678-682` — §2.8 titled "*(⚠ substantially REFUTED and demoted)*",
  "IT IS SUBSTANTIALLY REFUTED."
- `:706-710` — "**A faction is a proposition plus a commitment map**, so committing to a proposition
  somebody just uttered **is** the faction forming. Nothing waits on a constructor. **Every strong
  claim built on the contrary assumption is withdrawn**: *"can never come to exist"* … *"the design can
  lose every realm it shipped with and grow none"*."
- `:718-720` — the flagship quotation was **truncated without an ellipsis** in both places; the
  parenthetical cut was the document's own answer to the objection.
- And the v2 design now lists **"found a faction"** as a licensed social `mint`
  (`01_ARCHITECTURE.md:373`).

**What survives** (`:722-726`): proposition creation is **UNDER-SPECIFIED** — `SUP:1490`'s "his stance
emits a proposition" is one clause "with no act, no cost, no witness and no phase." That is the claim
D1 may carry. Carrying "no faction can be founded" reproduces, inside a document about the session's
errors, the exact error class its own closing section names.

### ⚠ BREAK 2 — "existence" is undefined, and the review equivocates on "destroy"

The same review says, four pages apart:

- `:141` (§1.1 flow table, *built/destroyed*, limb B): destruction is "**present.** §10.3's `alter`
  (`:1261`), `exclude` (`:1292`), doc 12's `burn` inherited at `:1305`."
- `:228-231` (the box): "**no character can bring a site, a container or an office into the world, or
  take one out of it.**"

Both cannot be read in one sense of *destroy*. Resolution, checked on disk:

- `SUP:689` — "Every act declares `touches: {(object, mode)}`, mode ∈ `{read, alter, exclude}`."
  **`exclude` is a conflict/exclusivity mode, not a destructor.**
- `SUP:1235` — condition "Acts touch it through the existing `alter` and `exclude` modes."
- `SUP:1291-1293` — "Deliberate discrete destruction… Burning a granary… is `exclude`, not `alter`."
- `SUP:1302-1306` — "One person destroying an undefended shared thing is expressible, is bounded only
  by the `contest`… **This document does not repair that, and it does not introduce it either**."

**Verdict: there is no sixth existence operation.** `exclude` is the near-miss and it is a lock mode; a
character can drive a site's `condition` to 0 and **the site still exists**. So D1 must say *no act
removes an object's RECORD* — which is the same distinction D4's plague case makes
(`01_ARCHITECTURE.md:494`), and stating it links D1 to D4 rather than leaving a contradiction.

**And the hole propagates:** `01_ARCHITECTURE.md:1859` — "⚠ **`mint` is CLEAR; `efface` is NOT CLEARED
and the widening is stated.** `efface` on a Rung, Office, Person or Site extends the uncleared discrete
limb of this row." D4's new `efface` inherits the unbounded-destruction limit D1's design already had.

### Note on scope
The five-item list is explicitly retitled at `:212` — "*this is the list of operations that change
**EXISTENCE**. It is not a list about tenure*." D1's sentence "the only operations… that change
existence **or tenure**" over-attributes. The tenure half rests on different evidence:
`SUP:339` (`| Faction | its proposition and its commitment map |`) and `holdings` being dead state.

---

## 3 · D7 — the claim holds, the ⚠ does not

**All three positive citations VERIFY exactly:**

| claim | cited | on disk |
|---|---|---|
| closed fourteen-form predicate vocabulary | `03:48-89` | ✓ §1.1 header `:48`; table `:64-79` (14 rows); "**Fourteen forms**" `:81`; restated `:118` |
| `relevance(c,q)` defined | `03:342-344` | ✓ exact — three cases, `1.0` / `0.3` / `0` |
| six investigation acts with pools, products, costs | `03:519-540` | ✓ §6.1 `:519`; six rows `:526-531` (examine, interview, research, surveil, reconstruct, Thread-Read); `trace` `:538-540` |

### ⚠ The ⚠ is wrong in both halves. "Both claims were false" is itself an over-claim.

**(a) The vocabulary claim was CORRECTLY SCOPED and is TRUE as scoped.**
`20_FABLE5_ADVERSARIAL_REVIEW.md:1215` — "**The document** names one form in 2,017 lines" — and the
file's citation convention (`:14-17`) makes a bare `:NNN` a line of `10_SUPERSEDING.md`. Runner 2 kept
the scope: `REVISIONS.md:196` — "the predicate vocabulary names **one form in 2,017 lines**." True.
**What is false is C3's FIX**, `:1226-1229`, which proposes authoring "a value-at-a-subject form, a
location form, a holding form, a compliance form, an obligation form" — five forms `03:64-79` already
ships as `QUANTITY`, `LOCATED`, `HOLDS` and others, inside a declared set of fourteen.

**(b) The `relevance` claim exists in two versions; the scoped one SURVIVES.**
- Unscoped, `REVISIONS.md:195` (runner 2, "CONFIRMED — the load-bearing verifications"):
  "`relevance(c, q)` is **never defined**". **False** against `03:342-344`.
- Scoped, `REVISIONS.md:295-296` (runner 5): "`relevance(c, q)` is undefined **at eviction** …
  **correct, and an improvement on the review**". `relevance` takes a question `q`; P7's eviction has
  no question in scope. **Doc 03 does not answer this**, so the scoped form survives its own reading.

So the honest D7 ⚠ is: *one absence claim was true as scoped and reinvented a shipped vocabulary in its
fix; the other was false unscoped and true scoped.* Both failures are **failures to name a scope** —
which is exactly the closing section's diagnosis, stated more precisely than "both were false."

Also worth one line: `REVISIONS.md:197` banks "**Every number checked out**". Several numbers in the
deliverable do not — §4 and §5 below.

---

## 4 · D11 — HOLDS, and a THIRD INSTANCE EXISTS INSIDE THE DELIVERABLE (the brief missed it)

**The two stated instances verify exactly:**
- `01_ARCHITECTURE.md:151` — "**`Rung` is the name. `Node` and `Container` are BOTH refused**"
- `:155` — `Node` "collides with Godot's scene-tree base class"
- `:157` — "`Container` is **also a Godot built-in** — the `Control`-derived base of `VBoxContainer`"
- `:159` — "failed loudly and at once, while `Container` surfaces as a confusing shadow of a UI type"
  ✓ the brief's "collides worse, because `Node` fails loudly while `Container` shadows"
- `:524-531` — `Derived` "collides with this repository's own vocabulary in the OPPOSITE sense",
  citing `references/glossary.md:75-82`. **Independently confirmed at that file**: Health, Stamina,
  Coherence, Composure, Momentum, listed under "Derived Character Stats" as stored per-character
  tracks. The collision is real.

### ⚠ THE THIRD INSTANCE — the v2 suite ships two incompatible citation keys

| file | line | `NN:LLL` resolves to |
|---|---|---|
| `01_ARCHITECTURE.md` | `:37` | `proposals/2026-08-29-valoria-from-scratch/NN_*.md` |
| `02_THE_SEASON_LOOP.md` | `:24` | "identical to `01_ARCHITECTURE.md` §0.1" |
| `03_COMPENDIUM.md` | `:34` | `proposals/2026-08-29-valoria-from-scratch/NN_*.md` |
| **`04_GODOT_IMPLEMENTABILITY.md`** | **`:40`** | **"line NNN of the numbered document in THIS directory"** |

**The same token means different documents depending on which of five files you are reading, and
neither key mentions the other.** `03:129` in the Godot audit means `03_COMPENDIUM.md:129`; `03:342-344`
in the architecture means the knowledge document. `04_GODOT_IMPLEMENTABILITY.md` carries **65** `03:`
citations under its private key, against 59 across the other three under the public one.

This survived the keys audit, the quality checker and the Godot audit. It is D11's exact mechanism — a
name that clears one namespace and not the other — occurring in the deliverable that diagnoses it, in a
*citation* namespace rather than a class namespace. `01_ARCHITECTURE.md:40-41` even ships a "**Namespace
key — read this before any cross-reference**" warning that "*a reader who does not hold this table will
resolve half the citations in these three documents to the wrong thing*" — and it governs finding-id
families, scopes itself to "these three documents", and does not catch this.

**It also has consequences that show up in §5 and §6:** it makes any automated citation count over
`NN:` ambiguous by construction, and it produces at least two live mis-resolutions (below).

---

## 5 · NUMBERS THAT DO NOT CHECK OUT

### (a) D8's "3 signatures to 23" — unsupported; and the source's own numbers are wrong

Disk, `04_GODOT_IMPLEMENTABILITY.md`:
- `:281-283` — "from the **three top-level signatures**… to the **twenty queries**"
- `:270` — "resolver-side — **12 of the 20 rows** of `01:422-443`"; "person-side — **5 rows**"
- `:899` — "**Twelve signatures** and one rule about the autoload table"

**Ground truth**, the Query table at `01_ARCHITECTURE.md:540-559`: **20 rows — 16 resolver-side, 4
person-side** (person rows: `leaders`, `opening_set`, `occupation`, `estimated_profile`).

So: **"23" appears nowhere** (it is 3+20). The document's "12 of the 20" is wrong — it is 16. Its
"person-side — 5 rows" is wrong — it is 4. Its 12+5=17 does not reach its own 20. And `:899`'s "twelve
signatures" is wrong for the same reason.
**Correct statement: from 3 top-level signatures to 20 queries, of which 16 are resolver-side and would
take an explicit `World` first parameter.**

**And the cited range mis-resolves under both keys.** `01:422-443` →
`01_ARCHITECTURE.md:422-443` is the event-mint / conflict-rule section; `01_substrate.md:422-443` is
§5.2 Dispensation. The Query table is at `01_ARCHITECTURE.md:538-559`. Neither key lands on it.

### (b) The sweep's "108 of 123" — was true when computed, is false against the tree it shipped in

Independently recomputed at HEAD with the sweep's own stated method
(`EVENTS_AND_SWEEP.md:669-675`: full path + basename against SUP, REV, and concatenated v2, plus the
`NN:` shorthand for the 08-29 suite), resolving `04_GODOT`'s private key correctly:

| | sweep says | recomputed at HEAD |
|---|---|---|
| `.md` under `proposals/` | 189 | **190** |
| over 200 lines | 129 | **133** |
| reference surfaces | 6 | 6 |
| swept | 123 | **127** |
| **cited nowhere** | **108** | **103** |

The method **reproduces for most rows** — `01_substrate` (SUP 4 · REV 4 · v2 0), `02_the_person`
(v2 28), `05_up_stroke` (v2 4), `09_churning_world` (v2 19), `13_material_life` (3), `14_office` (1),
`10_resolution_surface` (1), `12_coercion` (1), `06_down_stroke` (1), `08_argument` (0) all match
exactly. It does **not** reproduce for doc 03: table says v2 **17**, recomputed **66**.

**And the four flagship "uncited, already designed" documents are CITED at HEAD:**

| document | sweep tier | v2 citations at HEAD |
|---|---|---|
| `…-v2/11_world_events.md` (`we.altonian_pressure`) | Tier 1 #1, uncited | **9** |
| `2026-08-30-fixes/02_the_act_economy.md` | Tier 1 #3, uncited | **7** |
| `…-v2/09_ambitions_and_arcs.md` (`ambition.progress`) | Tier 1 #4, uncited | **6** |
| `…-v2/10_the_slate_and_salience.md` | Tier 1 #2, uncited | **4** |

**Mechanism:** commit `4c25cb4` is titled "WIP — architecture, +35 lines, **while the corpus sweep
lands**". The sweep's counts were taken mid-flight; the v2 documents were then edited to cite what it
found; **the sweep's own table was never recomputed before it shipped.** The four documents are cited
*because the sweep worked*. The closing section should say **103 of 127 at the tree as it shipped**,
note that 108/123 was true when computed, and record that the flagship four are no longer uncited —
which is a stronger result than the one currently claimed, not a weaker one.

### (c) "doc 03 was cited twice and unread" — needs re-dating
`v2/MANIFEST.md` and the sweep both use it. Counts at HEAD: SUP **1** (shorthand), REV **4**
(2 literal + 2 shorthand — matching the sweep's own REV column), v2 **66**. "Cited twice" matches only
`REV`'s literal count. **Doc 03 is the most-cited document in the v2 suite.** True statement: it was
effectively unread *at the time of the review* (`10_SUPERSEDING.md` cites it once in 2,017 lines) and
was read heavily afterwards. That is a recovery, and dating it correctly is the difference.

### (d) "21 of 26 impact types" — HOLDS, with a stray inside the source
`EVENTS_AND_SWEEP.md:427` — "of 26 impact types, 2 are cleanly event-legal…, 3 are genuine edge cases…,
and 21 are cleanly social." 2+3+21 = 26 ✓, and the §B6.1 table has **exactly 26 rows** ✓.
⚠ But `:383` opens the same table "All **22** impact types from §A1(b)", and §A1(b) (`:108-114`)
enumerates **25** (9 settlement tracks + 4 person/relation + 12 ledger tags), 26 with the `env.*` row.
**The 21-of-26 figure is sound; the "22" in its own header is a stray.**

### (e) "of nine full card records, zero are events" — HOLDS; its 7+2 decomposition does not
`EVENTS_AND_SWEEP.md:443` — "of the nine complete records, ZERO are events." ✓ the §B6.2 table walks 9.
⚠ The decomposition "**Seven** are NPC acts mis-filed; **two** carry decider-free social changes" does
not partition 9. Six rows are labelled ❌ NPC ACT (OPP-03, OPP-07, OPP-08, COURT-08, OPP-02, OPP-06);
COURT-06 is labelled ❌ **CHOICE**; XSCALE-07 and COURT-08 are §B6.3's two forbidden mechanisms — so
**COURT-08 is counted in both buckets**, and EVT-OPP-01 (the Aqueduct, "not an event and does not need
to be") is in neither. Also: only **8** of the 9 carry a `Grounding` field
(`grounded_event_card_deck_v1.md`, 8 matches); the Aqueduct's record is truncated by the file fragment,
which is why `EVENTS_AND_SWEEP.md:77` says "all **eight** complete records" while `:428`/`:443` say
nine. **"Zero of nine are events" survives all of this.**

### (f) "47–49 of 58" is an ESTIMATE, not a count — and the source says so louder than the brief
`EVENTS_AND_SWEEP.md:470` — "**cluster-level estimate, marked as inference**"; `:472-473` — "⚠ **I did
not read these cards; the file does not contain them.** … **Treat as an estimate, not a count.**";
`:849-851` — "**It is the weakest claim in this brief and the one most worth attacking.**" Deck ships 58
(`grounded_event_card_deck_v1.md:5`; 59 generated → 58 after one merge, `:21`), 9 records present, 49
inferred from cluster name and docket code. **Any sentence of the form "it reclassified 47–49 of 58 in
a single pass" must carry the word *estimated*.**

### (g) "thirteen CI failures" — NOT VERIFIABLE from disk, and not in brief v2
It concerns GitHub Actions runs. `CLAUDE.md` §2 records that **no tool in this repository reads the
GitHub API**. Nothing in the working tree records it. Brief v2 drops it; keep it dropped.

---

## 6 · SMALLER CORRECTIONS

- **D2 tuple misquoted.** Disk `01_ARCHITECTURE.md:253` —
  `Tenure := (id, subject, object, kind, since, until?, conferrer?, degree?, payload?)`. **Nine
  fields**; the brief gives eight, dropping `payload?`.
- **D2 `until?` wording.** `:265` reads "**`until?` is what makes a destroyed tenure a fact.**" The
  brief says "a REVOKED tenure"; the next clause on disk is "A revoked tenure is a historical claim
  subject", so both words are present — quote `:265` for the first.
- **D2's three spellings all verify** in `10_SUPERSEDING.md`: `Holding := (person, office, since,
  conferrer)` `:367` · `commit(person, faction, Δdegree)` `:130` · the hearth's succession pointer
  `:304`. Seven kinds ✓ `01_ARCHITECTURE.md:280`. `confer`/`revoke` already in `remit.acts` ✓
  `SUP:421-424`, a "closed set of five": **issue · determine · confer/revoke · dispatch · convene**.
- **D3 signature misquoted.** Disk `01_ARCHITECTURE.md:541` — `leaders(prop, c, observer)`,
  `(Proposition, Rung, Person) → List[Person]`, side **person**. Brief writes
  `leaders(observer, faction, rung)`: wrong order, and `faction` is `Proposition`.
  D3's spine verifies: `:540` `faction(prop)` "replaces a stored faction object"; `:561` "**Nothing
  stores an aggregate. Every one of these is a query, and that is why power is not static.**";
  `:535-536` records that flattening the side column typed `principals` as "**true-profile read, which
  nobody may perform** (`SUP:124-128`)" — D3's ⚠, with its history.
  ⚠ "sovereignty is a reachability query" is loose: `:545` `sovereign_fraction(root)` returns `[0,1]`
  and `:566-569` records it as **partial**, total only over the office-rooted subgraph.
- **D12's citation is wrong by ~42 lines.** `04_GODOT_IMPLEMENTABILITY.md:771` and `:885` cite
  `03:441-446` for cycles-as-normal. §3.4 Cycles is at `03_COMPENDIUM.md:483-492`; `:441-446` is the
  Tenure inverse-index row and §3.3 dangling/orphans. **The substance holds**: `:488` — "`succeed ∘
  contain`: Rung → Person → Rung | **yes, and it is the NORMAL case** — the heir lives in the hearth |
  **the reference graph is not a DAG**", plus four more reachable cycles at `:489-492`.
  Determinism half ✓ `01_ARCHITECTURE.md:419` — `id = H(world_seed, tick, subject_id, purpose)`.
  **Bonus, verified in shipped code**: `03_COMPENDIUM.md:490` says the claim-cycle case is "solved in
  this repo's substrate and not in the design" at `engine/substrate/keys.py:389-392` — confirmed on
  disk, "invariant 4 (cycle-freedom) holds by construction for an append-only log whose causes[] may
  only cite already-logged Keys."
- **D6 refinement omitted.** `01_ARCHITECTURE.md:784` — "⚠ **`opening_set` returns CANDIDATES, not
  Acts.** The prior brief typed it `Person → [Act]`." Everything else in D6 verifies verbatim:
  `:547` `verbs` "**world truth about what is possible**" · `:548` `opening_set` person-side ·
  `:764` the split's own section · `:771` "BELIEF, computed inside `choose`" · `:775` "silted" ·
  `:778` "*the people who notice first are the ones whose practice used that verb*".
- **D9 verifies; the brief conflates two figures that are both on disk.**
  `:1084` "the **King** spends **one** act — `dispatch` — and thirty-five named people each spend";
  `:1506` "a **Duke**'s `dispatch` moves thirty-five seasons. **Same allowance, incomparable reach.**"
  `:2046` "**D-2 is ruled**: one act per person or cohort, universally".
  Cohort-exploit pricing ✓ `REVISIONS.md:26-28`.
- **D10 verifies verbatim** against `REVISIONS.md:6-24` (Runner 3 / SCOPE, finding F-2): "COHORTS WERE
  DELETED. **ACCEPT — this is the worst error in the brief and it is mine.** … Matter does not act. …
  manufactures **elite-only politics by construction** … including the 'dynamically generated'
  replacements for collapsed royal ones." Two-object correction and "**A demographic envelope is the
  INFLOW RESERVOIR ONLY**" ✓. Restated in the deliverable at `01_ARCHITECTURE.md:571-575`.
- **D4 verifies fully.** Partition `01_ARCHITECTURE.md:1337-1341` · the 2×3 table `:371-374` ·
  `StateChange := (subject, mode, driver, field?, delta?, spec?)`, `mode ∈ mint | alter | efface`
  `:361-362` · "An earlier version made `mint`/`efface` **modes of an Act**" `:334` · bottom-left cell
  `:376-378` · landslide/seam `:374` · **plague worked case `:489-494` verbatim**, including "the
  village empties and **still legally exists** until some office strikes it from the roll".
  Omitted by the brief: `:1859`, `efface` is **not cleared** against refusal row 11.
- **D5 verifies fully, and D4's subsumption of it is STATED, not inferred.**
  `01_ARCHITECTURE.md:1360` the formula · `:1362` `wear` units · `:1386-1387` the tending table
  ("**the world dies and no person did it**") · `:1391` the act-economy consequence ·
  `:1711-1712` "no number in this design has been measured".
  **`:1374` — "`wear` IS AN EVENT, under §2.4's partition, and it needs no special case at all"**, and
  `:1377` records that an earlier version argued it in as a fourth channel. `SUP:1348` ✓ — "a storm
  remains what #342 makes it — a bad `season_factor` roll closing the channel *for a season*"; the
  act-only cost is admitted at `SUP:1350-1354`. §9.11 (`:1959-1968`) actually walks `wear` against
  refusal row 12, which the F6 ruling demanded "must be walked, not glossed".
- **Runner totals VERIFY exactly.** `REVISIONS.md` — Runner 3 SCOPE 2/11/6 (`:4`), Runner 1 FIDELITY
  3/8/10 (`:78`), Runner 2 FACTUALITY 1/5/4/2obs (`:147`), Runner 5 CORRECTNESS 6/11/7 (`:211`),
  Runner 4 KEYS 982 lines / 38 objects / 20 reference edges (`:298`).
  Sums: **12 FATAL · 35 MAJOR · 27 MINOR** ✓ matching `:346` and `v2/MANIFEST.md`.
  ⚠ **Rebutted: zero, across all five runners.** Worth one line in the closing section: the session's
  own result is that agreement across readings of one derivative set is not evidence, and a producer
  accepting 76 of 76 findings is the same signal from the other side.
- **Review header counts VERIFY.** `20_FABLE5_ADVERSARIAL_REVIEW.md:38-39` "Thirty-three findings were
  filed"; `MANIFEST.md:24` "34 findings filed, 33 carried, 13 corrections across 12 findings", with
  provenance "**2 from Jordan · 4 from the independent critic · 7 from the reviewer's own re-check**"
  and "the reviewer's own re-verification caught **none** of the four load-bearing breaks" — the four
  breaks F1–F4 are itemised at `20_…:44-56`.

---

## 7 · THE SINGLE MOST IMPORTANT THING THE BRIEF MISSED

**The v2 suite ships two incompatible citation keys** (`01_ARCHITECTURE.md:37` vs
`04_GODOT_IMPLEMENTABILITY.md:40`), unreconciled, in the deliverable whose D11 is *a name must clear
both namespaces*. It is D11's third instance and its best one, because unlike `Node`/`Container` it was
**not caught** — not by the keys audit, the quality checker or the Godot audit — and because it has
already produced live mis-resolutions (`01:422-443`, `03:441-446`) and makes the closing section's own
citation counts irreproducible.

It should be written into D11 as evidence and into the closing section as mechanism: **every audit in
the session read documents, and the one defect none of them could see was in the addressing scheme the
documents used to refer to each other.**

---

## 8 · WHAT §14 (predicts-next) CAN SAY ON VERIFIED GROUND

- `EVENTS_AND_SWEEP.md:798-808` — the sweep was **scoped to `proposals/`**, and names two `systems/`
  documents it therefore missed: `systems/_architecture/governance_ripple_substrate_v1.md` (559
  lines — "the **only statement of the draw's weighting formula anywhere in the tree**", cited **0**
  times by SUP, REV or v2) and `systems/settlements/governance_play_redesign_v1.md:154` (owns the Π
  homeostat all 58 triggers read). Its own words: "**a fourth instance is more likely to come from
  `systems/` than from `proposals/`.**"
- `CLAUDE.md` §3 calls `systems/` the design source of truth. The sweep never entered it.
- `01_ARCHITECTURE.md:1711-1712` — the `wear`-to-restoration ratio "sets the world's entire difficulty
  curve, and **no number in this design has been measured**."
- `01_ARCHITECTURE.md:1859` — `efface` is not cleared against refusal row 11.
- The three unmerged provenance documents (§0) are the nearest surface to lose: `main` cannot reach the
  ruling that produced `wear`, the partition document, or the sweep.
