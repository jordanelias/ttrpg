"""The generated layer must BUILD — the single owner of that assertion (culling wave 5, ED-IN-0194).

WHAT THIS REPLACED, and why it is a smaller claim than the one it replaced.

Seven builders under `tools/` write ten declared artifacts into `references/`, plus the fifteen
`systems/*/_identifier_census.yaml` sidecars the census builder writes alongside its roll-up. Until 2026-08-22 those artifacts were COMMITTED, and each had
a `test_*_is_current` that shelled out to the builder's `--check` to prove the committed bytes
still equalled a fresh render. Five near-identical tests, one rule — the duplication §8 forbids,
and worse, a rule about a file nobody authored: adding one document to `proposals/` churned three
artifacts and turned a blocking gate red for a prose edit.

The artifacts are now untracked and built on demand by the session-scoped `generated_layer`
fixture in `conftest.py`, which owns the build ORDER (two builders read another's output). With
nothing committed there is no staleness to detect: that failure class was DELETED, not weakened,
and pretending otherwise here would be the dishonest half of the change.

What survives, and what this file asserts once for all six:

  * the builder RUNS against the real sources (the fixture fails loudly if any exit non-zero), and
  * every artifact it declares is actually on disk and non-empty.

That is a harder failure than "the committed copy is stale", because a builder that crashes now
leaves nothing on disk at all rather than leaving yesterday's copy in place.

DETERMINISM is a separate claim and stays with each artifact's own test file
(`test_engine_atlas.py::test_render_is_deterministic`,
`test_contract_index.py::test_render_is_deterministic`,
`test_key_graph.py::test_the_render_is_deterministic`,
`test_execution_map.py::test_the_render_is_deterministic`). It has to: a non-deterministic
builder still exits 0 and still writes a non-empty file, so nothing here could observe it.
"""
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def test_every_builder_runs_and_leaves_its_artifacts(generated_layer, generated_layer_paths):
    """The fixture does the building; this states what the build must have produced."""
    assert generated_layer, 'no builder ran — the generated layer is empty'
    missing = [os.path.relpath(p, REPO) for p in generated_layer_paths if not os.path.isfile(p)]
    assert not missing, (
        f'builder(s) exited 0 but did not write {missing}. These artifacts are UNTRACKED, so an '
        f'absent file is not a stale file — it is nothing at all, and every test that reads one '
        f'would fail with an unrelated message.')
    empty = [os.path.relpath(p, REPO) for p in generated_layer_paths
             if os.path.getsize(p) == 0]
    assert not empty, f'builder(s) wrote empty artifact(s): {empty}'


def test_the_layer_is_not_vacuous(generated_layer_paths):
    """Guards the guard. If `_GENERATED_LAYER` were emptied — or every builder retired without its
    artifacts being dropped from the tuple — the test above would pass over an empty list and this
    file would assert nothing at all."""
    assert len(generated_layer_paths) >= 10, (
        f'only {len(generated_layer_paths)} artifacts declared in conftest._GENERATED_LAYER; the '
        f'layer had 10 at wave 5. Fewer means a builder was retired — drop its row from the tuple '
        f'and lower this floor in the same commit, deliberately.')
