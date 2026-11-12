# CORE — addendum C: test strength

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 785bc62 (working tree)

Addendum to `01_CORE_audit.md`, whose §4 says of the tests: *"43 test files were listed for this lane;
none was opened"*. This file is that reading. Question asked of every test file or family: **what
failure can its assertions observe, and what failure could they not** (`CLAUDE.md` §0.1 pts 2–4).

## 0. Verdict

*(written first, revised as the reading proceeded; the final text is below the census)*

## 1. Method and census

Three trees were in scope: `engine/season/tests/` (162 test files, 2,180 test functions, 7,752 `assert`
statements, 71,169 lines of which 37,220 are code, 12,478 comment and 11,891 docstring),
`engine/tests/` (6 files, 66 functions, 1,301 lines) and the `tests/valoria/` files the dossiers list
(100 files scanned, 870 functions). Counts are from an AST pass
(`scratchpad/runs/CORE_C/scan_tests.py`; per-test rows in `season_tests.tsv`, `engine_tests.tsv`,
`valoria_tests.tsv`), which records for each test function: asserts, asserts under an `if`, asserts under
a non-literal loop, `pytest.raises` blocks, asserts inside same-file helpers, `approx`/`isclose`, pinned
hex or large-integer literals, source-text reads (`inspect.getsource`, `read_text`, `ast.parse`),
skips, and `monkeypatch` use. The pass classifies nothing by itself; it says where to read.

Reading was done on a comment- and docstring-stripped view with original line numbers
(`scratchpad/runs/CORE_C/strip.py`), because 60 % of `test_season_shape.py` (10,664 of 17,880 lines) is
comment or docstring and the question here is what the assertions can observe, which only the code
answers. §9 lists what was read in full, what was read at the flagged tests only, and what was not read.
