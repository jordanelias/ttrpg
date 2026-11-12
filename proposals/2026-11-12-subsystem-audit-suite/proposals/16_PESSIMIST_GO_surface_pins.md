# GO — the pins see the player's surface: an offer digest per pinned seat, and words for kinds and verbs

## Status: PROPOSED

Carries F-PES-GO-01, F-PES-GO-09 (in part) and F-PES-GO-12 of `audits/16_PESSIMIST_GO.md`. Lanes GO, IN.
Read at `826b747`. Reference only (`CLAUDE.md` §0.05); not ratified by being written (§2). It amends
GO-08 (the oracle pins export) before it is built; it adds no position to B10-20.

## What it changes in `engine/season/` at runtime

Nothing in the loop. One harness function is added beside `dispatching_chooser`
(`harness/play_surface.py`), and GO-08's exporter calls it. Every content hash is today's.

## The problem, with evidence

The port's contract is `World.content_hash()` over the pinned slices. The hash folds the state
collections and the log. It does not fold a `Question` (`state/carriers.py:538`: "never hashed"), a
`View`, a `Candidate` or a ranking, and it sees the offer only through the acts a budget packs.

- `probe.py trunc 0` (`runs/PES_GO/`): all 83 persons seated on `development_space`, the pick keeping
  only the first `budget × interactions_per_scene` rows of each offer. One season, seed 0: 18,689 rows
  shown in 383 deliberations, 4,063 kept, hash `5ab73af282d0779646c38839fbab85d8`, equal to the plain
  run. **78.3% of what a player is offered moves no pinned value.**
- Control that the instrument can see a difference: one seat taking one different row moves the hash
  (`probe.py lever 0 p_npc_004 last` → `c093236b…`).
- The readings the `11_GO` proposals add (`Situation`, `Offer`, `receipt`, `account`, `dossier`) are
  not hashed either; their gate is a transcript whose `content_hash` equals the plain run's, which by
  the above is satisfied by any transcript.
- Of the 72 / 75 / 80 Event kinds and 46 / 46 / 48 verbs that occurred at seeds 0–2 (two seasons),
  none has an entry in `engine/engine_params/names.json`, the only exported vocabulary. A port must
  write those words itself, which makes it a second owner of the game's vocabulary.

So a port may form the wrong candidates, in the wrong order, for every row an NPC would not have
picked, with any text, and pass every exit line of B10-20.

## The resolution, decided

Ladder step 5, composed on step 4's precedent (GO-07: the comparison is a digest over a canonical
encoding; GO-08: one exported artifact holds every value the parity reader compares).

### 1. `surface_trace` (`engine/season/harness/play_surface.py`, beside `dispatching_chooser`)

```
def surface_trace(seed: int, seasons: int, seats: tuple[str, ...]) -> tuple[SurfaceRow, ...]

@dataclass(frozen=True)
class SurfaceRow:
    tick: int; round: int; person: str
    budget: int
    questions: tuple          # ids of v.questions, in the order carried (attention_key's)
    rows: int                 # len(sheet.candidates)
    digest: str               # blake2b-128 over GO-07's encoding of
                              #   tuple((c.verb, c.subject, tuple(sorted(c.operands.items()))) for c in sheet.candidates)
```

It seats each of `seats` on `development_space(..., pick=take_ranked)` (the control pick, so the run
is the automated run) and records one row per deliberation. It composes on the existing space, the
existing ranker and `World`'s existing encoder (`state/world.py::_canonical`, lifted to a public name
in the same commit; one owner, no second encoder). It forms nothing and ranks nothing. When SURF-B
lands, the tuple being digested becomes `Offer.rows` with `occasion`, `terms` and `odds`, and
`Situation.asked`; the function and the pin do not change shape.

### 2. GO-08's artifact gains a `surface` block

`engine/engine_params/oracle_pins.json`, per seed 0–2, slice 2 (the computed two-season run):

```
"surface": {
  "seats": ["<id>", ...],          # declared in the exporter: the first six named persons by id and the
                                   # first two cohorts by id, so the set is a rule and not a choice
  "rows": [[tick, round, person, budget, [question ids], rows, digest], ...],
  "content_hash": "<the run's hash; must equal slice 2's>"
}
```

`tools/export_oracle_pins.py --check` rebuilds it; `port_oracle.py` prints one line per seat. The
port's parity job reproduces the block from its own sheet.

### 3. A vocabulary block behind the names exporter

`references/names_index.yaml` gains two classes, `verb` and `event_kind`, each entry a key and a
display string. `tools/export_names.py --check` gains one rule: every key of `verb_table.yaml`'s
`verbs:` and every member of the derived Event-kind roster (`04_CODE_ARCHITECTURE.md:500`, loader
invariant 7: "the Event-kind roster is **derived** from every emission column") has an entry, and no entry names a key that is in
neither. This is the exporter's own round-trip for its own chain (§0.05's licensed form), not a
tree-wide guard. The strings are authored once, by Jordan or under his review, in the YAML; the
port reads `names.json`.

## Exact edits, by file and owner

| file | owner | edit |
|---|---|---|
| `engine/season/harness/play_surface.py` | IN | add `SurfaceRow`, `surface_trace` |
| `engine/season/state/world.py` | IN | `_canonical` exposed as `canonical` (rename; the hash's call sites follow) |
| `tools/export_oracle_pins.py` (unbuilt, GO-08) | GO | the `surface` block in `--build` and `--check` |
| `engine/season/harness/port_oracle.py` (unbuilt, GO-08) | GO | one printed line per seat |
| `workplans/valoria_master_workplan_v11_part5.md`, GO-08's REMAINING UNBUILT | GO | add "the `surface` block (per seed, the declared seats' offer digests)" |
| `references/names_index.yaml`, `tools/export_names.py` | IN | classes `verb`, `event_kind`; the completeness rule |

## The gate (execution artifacts)

1. `surface_trace(0, 2, seats)`'s run hash equals `bacd687f1470883b412be9638d0b0f88` (the plain
   two-season hash at seed 0 at `826b747`; re-take at the build commit), under `PYTHONHASHSEED` 0, 1, 2.
2. The truncating pick of `probe.py trunc` leaves the run hash equal **and changes every seated
   person's `digest`**: the pin now sees what the hash cannot.
3. `python tools/export_names.py --check` reds when one verb row is added to `verb_table.yaml` with
   no entry, and passes when the entry is added.

## The falsifier

A change to `opening_set` or `make_ranker` that alters the formed set or its order for a seated
person and leaves every `digest` equal. A `surface` block whose `content_hash` differs from slice 2's
(the trace moved the run). A verb or Event kind with no word that `--check` passes.

## NERS reading (§0.06; E last)

- **N.** Cut it and the freeze certifies only what NPCs pick. Top-down (the port gate's purpose),
  bottom-up (the ranker's order), lateral (every lane's playable surface is a seat's offer) and
  diagonal (a module's scene is entered from an offered row) all need it; it holds in more than one
  direction.
- **R.** Completeness: a pin that cannot fail on the player's half of the game is the absent test of
  §0.1 pt 2.
- **S.** One encoder, one digest, one artifact; consistent with GO-07 and GO-08.
- **E.** One function, one block, one rule; against 78% of the offer currently unpinned, the ratio is
  good. It adds no reading the player sees.

## Cost class

Small build (the function and the block), and an authoring task (about 150 strings).
