# CENSUS C1B — unreferenced symbols outside `engine/season/` proper (harness, modules, systems, dice, substrate, params, reference)

## Status: REFERENCE (a census lane's audit; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 7a4d5e1 (working tree)

Lane: PART=C1B of `CENSUS_BRIEF.md`. Rows: every row of `census/C1_unreferenced_symbols.md` whose file
starts with `engine/season/harness/`, `modules/`, `systems/`, `engine/dice_engine/`, `engine/substrate/`,
`engine/engine_params/` or `engine/reference/`. 643 of the census's 830 rows.

## 0. Verdict (provisional until the tables below are complete; counts are filled last)

IN PROGRESS. This head was written before the reading finished (CLAUDE.md §10 pt 2). Method, then
tables by file family, are appended as each family is verified.

## 1. Method (how each row was read)

The census is name-based: a symbol is listed when no *other* game file names it. Three things it cannot
see decide most rows, so each row was re-read with an AST pass over its own file plus a repo-wide name
search (script kept in the session scratchpad, not in the tree):

1. **In-file reachability.** A symbol named only in its own file is live when a chain of in-file calls
   reaches it from a root. Roots: module-level statements (including the `if __name__ == "__main__":`
   block and module-level dispatch tables), and any symbol another game file, a tool, or a YAML
   `target:`/composition string names.
2. **Dynamic reach.** `getattr(module, name)`, `globals()[name]`, a name built from a string prefix, a
   decorator registry, a dunder method the interpreter calls.
3. **Test-only reach.** A symbol reached by tests and by nothing a person or the loop runs is "a test
   that exercises code nothing calls" (brief, last paragraph); it is decided as dead or as needed
   on what the suite's proposals require, not on the test's existence.
