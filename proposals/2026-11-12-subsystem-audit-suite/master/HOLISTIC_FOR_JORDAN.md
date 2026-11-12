# Holistic audit — what waits on Jordan

## Status: REFERENCE (a decision register in the form of `unified/U6_FOR_JORDAN.md`; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: `4dc8a7b` (working tree, 2026-11-12). Lane: the holistic audit (`master/HOLISTIC_AUDIT.md`, `master/CODEBASE_IMPROVEMENT_PROPOSAL.md`).

**One item survived the five-step ladder** (CLAUDE.md §0). It is not a choice between two games; it is here
because either answer adds a line to a ratified Layer 1 table, and a lane does not do that on its own
authority. Everything else the audit decided is in the second table, each with the step that decided it,
and is reversible on a word.

---

### J-H-01 · Where does "start a new game" live in the code?

**What is true today.** The code that builds the realm (the map, its buildings, the 46 named people and the
37 population groups, their offices, goals and starting acquaintances) is one function of about a thousand
lines, `build_realm`, in the package of test instruments (`engine/season/harness/populated.py:1014`). The
code that sets up how people choose (`harness/probes.py:278`) is there too. Layer 1 lists nine modules
for the season package (`04` §A.2: `state`, `data`, `queries`, `decision`, `loop`, `seam`, `manifest`,
`game`, `tests`) and the instruments' package is not one of them. Layer 1 mentions world generation once,
as *"a registry row read once at boot"* (`04` F.31).

**Why it matters.** The Godot port needs a file to port for "new game", and today it would be porting a
test instrument. Twenty-nine proposals in the suite edit that file. Nothing is broken: every world it
builds is the world the instruments measure. The move is a pure move and changes no outcome.

| | **Option A: a tenth module** | **Option B: a file of the loop** |
|---|---|---|
| what is done | a new module `engine/season/boot/` holds the realm builder and the chooser's set-up | the builder becomes `engine/season/loop/boot.py`, beside the driver that then runs the world |
| the Layer 1 line it needs | §A.2's list gains `boot/   the realm builder: reads the authored data, constructs the World, holds no token after construction`, and the heading "the nine modules" becomes ten | §A.2's table gains a row `loop/boot` (owns: the World at construction; reads: the authored data; emits: nothing; token: none), and `loop/`'s line reads "driver + seven steps + the builder" |
| what it feels like | the clearest answer to "where does a game start": its own place, the way `decision/` has its own place so that a rule can be checked by path | no new module; but `loop/` stops being "the driver and the steps" and a reader must learn that one file of it is not a step |
| cost | the same move either way (about 115 files have an import line re-pointed); one more directory | the same move; one more exception in a module whose other files are all steps |

**Recommendation: A.** Layer 1's own reason for making `decision/` a module is that a boundary is what
makes a property checkable by path (`04` §A.3 row 1). The builder's property is that it is game code and
imports no instrument; a directory makes that checkable the same way.

**If you say nothing.** Nothing moves. The builder stays in `harness/populated.py`, proposals keep citing
it there, and item `CI-07` of the improvement proposal stays held. The other ten items do not depend on
this one.

---

### Decided by the ladder, and reversible on a word

| what was decided | the other way | step that decided it | to reverse |
|---|---|---|---|
| **The source's history is cut in one early batch** (`CI-02`, batch `B03a`): comments and docstrings keep what the code does, its inputs, its governing rule, your quoted words and every tag a gate reads; dated accounts of how the code got that way leave, and stay readable in git | trim each file only when a later batch opens it | 4 and 5: CLAUDE.md already puts narrative in commits (§1, §2), and STAGES asks that hash-equal work be batched ahead of the batches that move results, so the trimming is not mixed into them | drop `B03a` from the order; nothing else depends on it but the reading cost |
| **The two big registries lose their notes, not their values** (`CI-01`): each note is cut to what the roster or cell is; `source:` lines and every `[ASSUMPTION; …]` tag stay | leave them; the files stay at about 350 KB each | the same | drop `CI-01` |
| **The season's 101 settings stay authored in Python and are exported** (`CI-04`), not moved to a data file | author them in YAML, as the rosters are | 4: the tree's precedent for a Python owner is an exporter with a round-trip check (`combat`'s parameters, the battle orders), and 91 proposals edit the settings where they are | move them later; the export then reads the data file instead |
| **The big files are not split** (`world_q.py`, `rosters.yaml`, `verb_table.yaml`) | split each into families of functions or rosters | 5: a split moves things without removing anything, Layer 1 names `world_q` as one member, and most of the files' bulk is notes that `CI-01` and `CI-02` remove | ask again after those two land |
| **The old per-subsystem simulation scripts under `systems/` are not retired by this audit** | retire them as dead (no realm run enters one function of them) | 1 and 3: their retention is your ruling (ED-IN-0283), and the retirements that are due are already carried one subsystem at a time | — |
| **`tools/` is not audited to the efficiency standard**; three files nothing reads are deleted (`CI-10`) | hold the tools to the same standard as the game code | 3: the efficiency skill excludes `tools/` so that a standard is not pointed at the repository's own apparatus (CLAUDE.md §0.1 pt 5) | name the tools you want read |
| **Personal combat becomes an ordinary package** (`CI-09`) | keep its files as loose top-level modules behind a path insert | 5: the only reason given for the loose form is that the balance workbench loads it that way, and the workbench can be re-pointed | drop batch `B13` |

**What I could not check, which you may want to know.** No test suite was run (the brief barred it), so
every "nothing changes" claim in the proposal is a gate the batch runs, not a result. The Godot side of
the porting cost was not read (no outbound read was made), so the porting table ranks the Python only.
The reach figures come from two seeds and at most four seasons.
