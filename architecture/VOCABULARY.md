# VOCABULARY — THE HIERARCHY, AS A BALLOT

## Status: **PROPOSED — a ballot, not a ruling.** Every row carries a status. `RATIFY` rows need one
## word from Jordan. `CHOOSE` rows are live forks. `FIXED` rows were answered by CLAUDE.md §0's
## tests 1-5 and are recorded here rather than escalated — object to any of them and it reopens.

**Why this file exists.** Layer 1's vocabulary is currently defined in two places — `holonic_ARCHITECTURE.md`
§0.4 (18 terms) and `ARCHITECTURE_V2.md` §0.5 (4 more) — and **neither defines a single structural
term**: not *system*, not *subsystem*, not *module*, not *layer*, not *loop*. Those are the words the
adoption is being conducted in. They are also the words with the most collisions, because nothing has
ever governed them.

**What binds this.** `CLAUDE.md` §4 (RULED 2026-08-13, ED-IN-0179) — **idempotent in meaning**
(a later session reading the word cold must land on the same meaning, because there is no context
between sessions) and **idiomatic in choosing** (use the word ordinary usage already supplies). And
§4's second half: **define it in BOTH places** — prose *and* the call site — because the next session
usually meets the term in code first.

**What this file is NOT.** It is not mechanism (§0.05). Once ruled, each definition lands where code
reads it — a registry key, a role name, an identifier — and this file becomes the reference record of
why. It does not resolve anything at runtime, and no behaviour depends on it.

**Every "used now" cell below is measured against the working tree, not recalled.**

---

# WHAT THE TIERS ARE, AND WHY THE ORDER IS THIS ORDER

A tier is not a category of word. It is **an answer to "what would break if this word changed
meaning?"** — and the tiers are ordered by that blast radius, widest first. The same ordering falls
out of a second question, which is the same fact from the other direction: **how far is this word
from the substrate?** The further out, the more replaceable the thing it names.

| tier | it names… | change it and you change… | who owns it today |
|---|---|---|---|
| **0 · THE REPOSITORY** | what the **code** is made of — files, trees, packages, strata | **every file.** These words would still be needed, meaning the same things, if the game were rewritten in another engine tomorrow | **nobody.** Never ruled, never registered — which is exactly why this tier carries the most collisions |
| **1 · THE WORLD** | what the **game** is made of — its ontology. `Person`, `Rung`, `Tenure`, `Act`, `Event` | **every subsystem.** They survive a rewrite of any one subsystem; they do not survive a redesign of the architecture | **Layer 1** — `holonic_ARCHITECTURE.md` §0.4 and `ARCHITECTURE_V2.md` §0.5 already define all 22 |
| **2 · THE BOUNDARY** | how the loop **meets** a subsystem — the seam vocabulary | **the dispatch model.** Jordan, 2026-09-05: *"a seam survives a rebuild of the subsystem behind it; a signature does not."* That is the property this tier has and Tier 3 does not | **nobody.** Used constantly in `shape.py`; defined in neither §0.4 nor §0.5. **This is the gap** |
| **3 · THE SUBSYSTEMS** | what is on the **far side** of a boundary — the individual engines | **one directory.** The most volatile tier by design — *"we will be rebuilding probably"* | **Jordan.** These are names of things in his game, not engineering choices |

**The test for placing a new term** — ask what has to stay true for the word to keep its meaning.
Answer *"the repo is laid out this way"* → Tier 0. *"the architecture holds"* → Tier 1. *"the loop
still calls out to subsystems"* → Tier 2. *"this particular engine exists"* → Tier 3.

**Why the statuses cluster the way they do**, which is the tiering's one falsifiable prediction:
Tier 0 is mostly `FIXED` because nobody ever ruled it, so the collisions are accidents with obvious
engineering answers rather than design forks. Tier 1 is mostly `RATIFY` because it is already
defined and just needs confirming. **Tier 2 holds most of the `CHOOSE` rows** because it is the tier
that is used without being defined — the definition gap and the decision load land in the same
place. Tier 3 holds exactly one `CHOOSE`, and it is a naming call in your vocabulary, not ours.

**⚠ The tiers are not a containment ladder, and reading them as one is the error to avoid.** A Tier 0
*subsystem* does not "contain" a Tier 1 *tenure*. The tiers rank **stability**, not scope — which is
why `seam` appears in two of them (Tier 0 as the boundary *word*, disambiguated against *bridge* and
*adapter*; Tier 1 as the architecture's own already-ruled *definition*, now falsified). A containment
reading would make that a contradiction. A stability reading makes it what it is: one word whose
naming and whose definition were settled at different times, by different documents, and are now out
of step.

# TIER 0 · THE REPOSITORY — what the code is made of

Defined nowhere today. This is the tier Jordan's question named.

| term | what it denotes NOW (measured) | status | the rule proposed |
|---|---|---|---|
| **system** | colloquial only — Jordan's *"the system for social contests"*. 5 uses in `CLAUDE.md`, 20 in `module_contracts.yaml` (mostly inside `registry_system:`), 7 in `engine/season/`. Never a schema key on its own. | **FIXED** | Keep as ordinary prose for "a body of mechanics". **Never a schema key, never an identifier.** Where precision is wanted the word is *subsystem*. |
| **subsystem** | a directory under `systems/`. 15 exist; 3 retained by ED-IN-0202 (`combat`, `social_contest`, `mass_battle`), 7 code-bearing pending R-04, 5 doc-only. 64 uses in `engine/season/`. | **RATIFY** | **A subsystem is one directory under `systems/` owning one body of mechanics.** One subsystem = one folder = one ID lane = one `CURRENT.md` row. Already CLAUDE.md §3's usage; this fixes it. |
| **module** | ⚠ **TWO RANKS, ONE WORD.** In `references/module_contracts.yaml` a *module* is one of **27 mechanical units with a contract** — `faction_state`, `npc_memory`, `personal_combat` — and the Python file is a *separate* field, `sim_module:`. Everywhere else (Python, CLAUDE.md, `engine/season/__init__.py`) a module is a `.py` file. 85 uses in the contracts file, 63 in `engine/season/`. | **FIXED** | **A module is a Python module.** The contracts file's 27 are *contracts*, and they live in the OLD DRIVER's half of the two strata — the half that is transitional. The surviving half of that file is `composition_roles:`, which uses neither sense. So the bad sense retires with its registry; do not propagate it, and do not rename the 27 today. |
| **package** | a Python package. 6 uses in `engine/season/`, no competing sense found. | **RATIFY** | Ordinary Python meaning. No action. |
| **engine** | ⚠ **FOUR SENSES.** (1) the tree `engine/`; (2) *"there is no GM — the engine resolves everything"* (CLAUDE.md's headline — the whole program); (3) `systems/combat/combat_engine_v1/` — one subsystem's implementation; (4) `combat_seam.engine()` — **a function**, 5 call sites. | **FIXED** | Senses 1 and 2 are the same object and stay. Sense 3 is subsystem-internal and grandfathered. **Sense 4 is the drift** — a function named for the program it lives inside. Rename it at the same time item 1-3 touches the seam. |
| **layer** | ⚠ **JORDAN'S OWN COINAGE COLLIDES WITH THREE IN-CODE SENSES.** *"two major layers"* (2026-09-05: architecture / game code) now competes with **epistemic layer** (7), **argument layer** (3), **narrative layer** (2) in `engine/season/` — and with §2's **T2**, which calls the claim-ledger / conviction split *"two layers, and conflating them is the most dangerous collision in the design"*. | **CHOOSE** | **(a)** Layer 1 / Layer 2 stay, always capitalised and always numbered — bare *layer* keeps its in-code senses. Cheapest, zero renames. **(b)** Rename the adoption's two to **strata** (the plan already says *two strata*). Recommend **(a)**: numbered proper nouns are self-disambiguating and *stratum* is less idiomatic than *layer*. |
| **loop** | ⚠ **THE WORST VALENCE COLLISION IN THE TREE.** 18 uses in `CLAUDE.md`: **8 are bare "the loop"** meaning §0.3's *pathology* — the apparatus generator this repo was caught in — and **2 are "season loop"**, the thing we are building. One word, opposite valence, same document. A session reading *"we are back in the loop"* cannot tell whether that is progress or relapse. | **CHOOSE** | **(a)** *the season loop* keeps `loop`; the pathology is **always** written *"the apparatus loop"*, never bare. **(b)** rename the pathology outright — *the apparatus spiral*. Recommend **(a)**: it is a discipline on one document, not a rename, and §0.3's text already uses the qualified form half the time. |
| **substrate** | `engine/substrate/` — the permanent leaf tier: `descriptors`, `composition`, `keys`. 24 uses in contracts, 22 in season. One sense. | **RATIFY** | **The permanent tier under `engine/`, stdlib-only leaves that name no subsystem.** The first of the two strata. |
| **driver** | `engine/mc_v18.py`, the campaign driver; `SeasonDriver` in `shape.py`. 58 uses in `engine/season/`. | **RATIFY** | **The thing that sequences a run.** `mc_v18` is the OLD driver (transitional stratum); `SeasonDriver` is the new one. Both are drivers; the qualifier does the work. |
| **seam / bridge / adapter** | ⚠ **THREE WORDS, ONE THING.** `adapters:` is a top-level key in `module_contracts.yaml` (8 entries); `engine/cross_scale/combat_bridge.py`; `engine/season/combat_seam.py`. All three name a subsystem boundary. | **FIXED** | **A seam is the CONTRACT** — where it attaches, what goes in, what comes back (`rosters.yaml`'s table). **An adapter is the module that implements one.** *Bridge* is retired as a new coinage; existing filenames are grandfathered under §4's no-retrofit posture. |

---

# TIER 1 · THE WORLD — what the game is made of (already defined; mostly needs confirming)

These 22 are defined in `holonic_ARCHITECTURE.md` §0.4 (18) and `ARCHITECTURE_V2.md` §0.5 (4). They
were written as ordinary words on purpose and coinages are marked ⊕ there. **Twenty ratify as a
block. Two do not**, and both are called out below rather than buried in the block.

**RATIFY AS A BLOCK (20)** — `carrier`, `rung`⊕, `holon`, `tenure`, `act`, `event`, `claim`, `query`,
`aggregate`, `ratchet`, `barrier`, `step`, `write class`, `the Partition`, `descent`, `hole`,
`default`, `fill`, `verb row`, `throughline`. I attacked each against its use in `shape.py` and found
no second sense. [NULL: the 20 above, checked against `engine/season/shape.py` and `rosters.yaml` —
examined, no collision found.] One word from you ratifies all twenty.

**The two that cannot be ratified as written:**

| term | the problem | status | the rule proposed |
|---|---|---|---|
| **seam** | §0.4 defines it as *"the ONE place a deferred subsystem attaches: RESOLVE, via `contest`"*. ⚠ **Your 2026-09-05 ruling falsifies this**: *"each mode of play is separately called from season loop"* means there are several attach points and RESOLVE is only the contest one. Investigation is explicitly not a contest; settlement is computed inline and attaches nowhere. The definition names the exception as the rule. | **CHOOSE** | **A seam is the declared boundary at which one mode of play is called from the season loop, and RESOLVE (§39) is the contest seam — one of several.** This is the definition Tier 2 below depends on, so it needs settling before the role namespace is minted. |
| **refraction** ⊕ | §0.4 flags it itself: *"the head uses this word two ways — §37.4"*. A coinage used two ways is the exact failure §4 was ruled to prevent, and it is already known. | **CHOOSE** | Either split it into two ordinary words, or pick one sense and rewrite §37.4. I have not proposed the split because it is a design distinction (downward distortion of *influence* vs. of *information*), not a naming one — you own it. |

---

# TIER 2 · THE BOUNDARY — how the loop meets a subsystem (where your question lives)

Used constantly in the season loop; **defined in neither §0.4 nor §0.5.** This is the tier the
merge-blocking work (routing dispatch through `composition.require()`) will mint into a registry, so
these are the rows worth your time.

| term | what it denotes NOW (measured) | status | the rule proposed |
|---|---|---|---|
| **mode of play** | 7 rows in `rosters.yaml`'s seam table — personal combat, social contest, mass battle, investigation, settlement mgmt, faction mgmt, character dev. Your ruling: *"each mode of play is separately called from season loop."* | **CHOOSE** | **What the player is DOING** — fighting, debating, investigating, building, administering, developing a character. A mode is what gets its own call out of the loop. |
| **scale of play** | 7 rows in `requirements.yaml`'s `scales:` block — a **nearly but not exactly identical list** (*grand strategy politics* ↔ *faction mgmt*; *management games / city builders* ↔ *settlement mgmt*). | **CHOOSE** | **How far you are ZOOMED OUT** — person → scene → settlement → faction → world. ⚠ These two are being used as synonyms and are not: **personal combat and mass battle are one MODE at two SCALES.** That distinction is load-bearing on your own ruling — *"each mode is separately called"* is a claim about modes, while NERS **S** (*"zooms out and in well across scales of play"*) is a claim about scales. With one word, neither sentence says what it means. |
| **contest** | 104 uses in `shape.py`. The genus: `contest(w, claimants, prize, causes)` → dispatch → a degree. Declared on a verb row as `contests: <prize>`. | **RATIFY** | **A struggle between named claimants over a stated prize, resolved by a subsystem and returning a degree.** Ordinary English, passes §4 cleanly. The genus keeps the word. |
| **prize** | what a contest is over. `rosters.yaml` maps four: *the body*, *a field*, *a standing*, *a proposition*. | **RATIFY** | **What is at stake, and the key that selects which subsystem resolves it.** |
| **claimant** | S39.1: *"claimant[] is PERSONS, ALWAYS. Not factions, not units, not sides."* | **RATIFY** | As S39.1 states. No second sense found. |
| **cause** | S39.2: *"events, into the same log, WITH `causes[]` NAMING THE ACTS"*. | **RATIFY** | **The acts that produced the contest**, carried so the log stays one log (S19.5). |
| **degree** | the band a contest returns. | **RATIFY** | [NULL: checked across `shape.py`, `engine/autoload/dice_engine.py` and `module_contracts.yaml` — examined, ONE sense. `shape.py:6604` imports `degree_from_net` rather than deriving a second ladder, so the contest's degree *is* the dice ladder's band.] I looked for a collision here because it seemed likely; there is none. |
| **resolver** | ⚠ **TWO SENSES.** In `module_contracts.yaml` it names a **ladder** — `d_sigma`, `dice_pool`, `deterministic_accounting`, `state_reader` — i.e. *which math grades this*. But `contest_subsystem` reports `resolver=` while `composition.require()` returns **the function you call**. | **FIXED** | **`resolver` = the ladder** (the older, wider use — 27 contract rows). **`target` = the callable** — which is already the field name in `composition.py` (`ROLES[role]['target']`). No rename needed anywhere; the prose stops conflating them. |
| **role** | `composition_roles:` in `module_contracts.yaml`; `composition.require(role)`. A name the engine states so it need not name a module. | **RATIFY** | **A capability the engine requires, named so the engine never imports its provider.** ⚠ Watch for the person-side sense (a person's office/tenure) — no collision found today, but it is one word away. |
| **attach point** | `rosters.yaml`'s seam-table column; S39 fixes the contest one at RESOLVE. | **RATIFY** | **Where in the loop a seam is called.** Part of a seam's declaration, not a separate thing. |

---

# TIER 3 · THE SUBSYSTEMS — the far side of a boundary (the collision that prompted this)

| name | the problem | status | the rule proposed |
|---|---|---|---|
| **personal_combat** | `<scale>_<kind>`. Peer-consistent. | **RATIFY** | No action. |
| **mass_battle** | `<scale>_<kind>`. Peer-consistent. | **RATIFY** | No action. |
| **social_contest** | ⚠ **THE GENUS INSIDE A SPECIES NAME.** Its two peers are `<scale>_<kind>`; this one is `<adjective>_<genus>`, so it scans as *"the general mechanism, socially"* rather than as a peer. The rank inversion is literal on disk: **`systems/social_contest/sim/contest/`** — a package named for the genus, nested inside the subsystem named for one species. And the roster reads `contest_subsystems → {personal_combat, mass_battle, social_contest}`, where one of three values repeats the key. | **CHOOSE** | Rename the species; the genus keeps `contest`. Its prizes are *a standing* and *a proposition*; candidates that fit `<scale>_<kind>` or a plain kind: **`assembly`**, **`debate`**, **`parley`**, **`suasion`**. This is your vocabulary, not an engineering call, so no recommendation. <br><br>**Cost, so the ruling is informed:** 30 tracked files carry it in their path, 299 files mention it, and it is ED lane `SC` with 32 allocated ids. **The lane code and the ED ids are frozen citations either way** under §4's no-retrofit posture — they do not move and do not need to. What moves is the directory, the roster value, and the `composition_roles:` target. Your *"we will be rebuilding probably"* already licenses that. |

---

# WHAT A RULING COSTS, AND WHY THE TIMING MATTERS

Nothing here is a rename sweep. The four `CHOOSE` rows that touch code —
**seam**, **mode/scale**, **social_contest**, and Tier 0's **layer**/**loop** — change identifiers
that the merge-blocking work is *about to create*: routing contest dispatch through
`composition.require()` mints the role namespace into `module_contracts.yaml` and its exported JSON.

Minting it as `contest.*` for things that are not contests — investigation, city management,
political assignments — and correcting it afterwards costs a registry migration and a re-export.
Minting it as `mode.*` costs nothing today. **That is the whole argument for ruling before, not
after.**

Once ruled, each definition lands where code reads it (§4's *both places*): the seam table gains a
`scale` column, the role namespace takes its prefix, `resolver`/`target` stop being interchanged in
prose, and this file records why. No new mechanism, no guard — under §0.1 point 5 a vocabulary
register is load-bearing on process, not on the game, so it earns no gate.
