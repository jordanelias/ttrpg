# Verb build-out brief — design and author every verb so it works

## Status: WORK ORDER (Jordan's direction of 2026-11-12: *"we need fable to design author make all verbs work"*; not canon; resolves nothing until built and verified)

R-05 (`engine/season/requirements.yaml`, status `not_met`): *all verbs must be built out, and doing so
requires planning out all the different scales of play required in a season.* The verb table holds 67 rows
in five strata (`engine/season/verb_table.yaml`). Each Fable verb lane designs and authors the complete
build-out of its assigned verbs, as proposals carrying the exact edits (final row text, effect structure,
roster rows, gates), so that an implementation lane can land them mechanically. The authority granted
in `AUDIT_BRIEF.md` ("Authority granted") applies: you author and decide in proposal form; you edit
nothing else; you do not commit.

## Binding context (read first)

`CLAUDE.md`; `AUDIT_BRIEF.md` (all sections: Jordan's standing requirement that every subsystem be a
playable game that conforms to Layer 1 and integrates with the season loop; "never a dead end"; computed play
must reach; the social-contest obstacle is the difficulty of the task plus all modifiers; capability
authoring; NPC/chooser intent; the detective/noir precedent for evidence and argument; the
combat and mass-battle intents; research, `.designs/` and `.audit/` as referents); the relevant lane audits
and addenda in `audits/` and the proposals in `proposals/` (cite, do not redo them); the existing verb
material: `proposals/2026-10-16-verbs/` (lexicon, gap registers), `2026-10-21-verb-key-rows*.md` (the Key
substrate is RETIRED: take the verb insight, never the Key mechanism), `2026-10-03-verb-coverage-and-gap-fill.md`,
`2026-11-05-verb-attribute-map*.md`, `proposals/verb_list.md`, `research/cross_scale_action_catalogue_v1.md`,
`research/historical_concerns_action_catalogue_v1.md`, `skills/premise-check/SKILL.md` (use its method: write
what each link should do from the ordinary meaning of its words BEFORE reading the code, then compare),
`engine/season/loop/` effects modules, `queries/`, `decision/options.py`, `seam/wrappers/`, the hole register
rows for the verb, and the corpus (`harness/corpus_run.py`) readings for which verbs execute.

## For every assigned verb, author (a section per verb, in this order)

1. **Premise.** One sentence in the ordinary meaning of the word, as a strategy/RPG player would expect it,
   then the chain of links the sentence implies.
2. **State today.** Row, formation conditions, requirement, roll, effect, writes, emits, refusal reasons,
   graded outcomes, who reads its results; the instrument reading of how often computed play forms and executes
   it (one short seeded reading; cite the aperture/corpus output); verdict: works / forms but is refused /
   executes but writes nothing / unreachable / stub. Evidence, not assertion.
3. **The build-out, decided.** What the verb must do for the premise to hold: who can form it and when
   (person-side facts only), its typed requirements, its roll (pool; obstacle as task difficulty plus named
   modifiers; capability keys), its effects by degree (graded and recoverable; no binary dead end), what it
   writes and emits, what it costs, what it unlocks or forecloses, its refusal reasons and why each is
   necessary (a refusal the chooser could have read is a dead end: move it into formation), the reason trail
   it leaves, and its consequences for other subsystems (name the readers).
4. **Scales and play surface.** At which scales it operates (person, settlement, faction, realm) and how it
   composes across them; what a player chooses (the verb aperture; approaches; targets) and what the engine
   resolves automatically; how an NPC chooses it through the one chooser.
5. **Tuning hooks.** Venue, personality, affiliation, office, relationship, evidence and season dimensions
   that should modulate it, with the owner file for each (data, not constants).
6. **Exact edits.** Final text of the `verb_table.yaml` row, the roster and registry rows, the effect
   function (structure, typed inputs/outputs, the files and functions it touches), and the order of landing,
   as a diff-like listing. Layer-1 conformant (`architecture/meta/04_CODE_ARCHITECTURE.md`): typed in/out, no
   held state, no special-casing of an entity or outcome.
7. **Gate and falsifier.** The execution artifact that shows the verb now works (a seeded run in which it
   forms, executes and its consequence is read downstream, with a control), and the planted failure that
   would show it still does not.
8. **Cases.** Which provided arcs and characters need this verb (`audits/12_ARCS_adjudication.md`) and what
   each needs of it.
9. **NERS reading.** Necessary, robust, smooth; elegant last as a ratio; cut test: what dies if this verb is
   removed or merged (a verb may be folded into another by ruling; propose it only with the cut test shown).

Close each audit file with: a dependency graph of the family's verbs (which must land first), a cross-family
dependency list, a landing order in batches with the gate for each batch, and the decisions that survive to
Jordan with their two options.

## Output

`audits/14_VERBS_<FAMILY>.md` and proposals `proposals/14_VERBS_<FAMILY>_*.md` (group verbs sensibly; at least
one proposal per batch of the landing order). Edit only those. No commit. No pytest. Instrument output to
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/VERBS_<FAMILY>/`. No long
`aperture` run. Write early and append. Receipt <= 200 words: files, verbs designed, verbs found already
working, the three worst, decisions for Jordan.
