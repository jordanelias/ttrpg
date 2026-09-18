# CLAUDE_RATIONALE.md — why the rules in `CLAUDE.md` say what they say

## Status: REFERENCE. NOT BINDING. NOT REQUIRED READING.

**`CLAUDE.md` is Layer 0. This file is not.** Nothing here is a rule, and a session that reads this
instead of `CLAUDE.md` has read the wrong file. It exists because §0's own exception is right about
one thing — *"Nobody reads `git log` to understand a design"* — and because a rule whose reasoning has
been deleted is a rule the next session argues its way around.

**When to open it:** a rule in `CLAUDE.md` looks arbitrary and you are about to change it. Then read
the corresponding section here first, because most of these rules are narrower than they look and were
written against a specific failure that recurred.

**Why it is allowed to exist**, against §0's ban on the adversarial pass producing documents: it
creates no work. Every section explains a judgment about an artifact that **already exists** — the
rule it sits beside. There is no queue here, no "someone should build Y", no findings. It is bound to
its subject in §0's sense: **when a rule leaves `CLAUDE.md`, its section here goes with it.** If this
file ever acquires an item that asks a future session to do something, that item is the forbidden thing
and the repair is to delete it, not to qualify it.

**It is a sibling, not a tree.** Do not add a second one, do not start a `rationale/` directory, and do
not move design content here — design prose goes to `proposals/`, and the quarantined corpus is
`.designs/` (§1).

---

## Header — why `CLAUDE.md` carries a line cap

**MEASURED 2026-09-18.** `CLAUDE.md` was 984 lines, 11,615 words, 77,592 bytes — **19,228 tokens by
`tools/ci_common.py`'s own `tokens()` estimator**, charged on every session and again on every subagent
delegation. With `CURRENT.md` (6,136) and `HANDOFF.md` (3,903), the orientation read §1 documents cost
**29,267 tokens before a line of work**.

The growth curve, one row per commit that touched the file:

```
2026-09-04  1023     2026-09-11   738     2026-09-16   821
2026-09-07  1025     2026-09-12   745     2026-09-16   865
2026-09-09   664  ←  cut          773     2026-09-17   903
2026-09-10   665     2026-09-15   792     2026-09-17   928
2026-09-10   667                          2026-09-17   967
2026-09-10   732                          2026-09-17   984
```

**It was cut 35% on 09-09 and regrew 48% in the eight days after, monotonically.** Fifteen commits
touched it; every one added lines and none removed net. By 09-17 it was within 4% of the size the cut
had been made to fix. That is the §0.3 accretion pattern operating on the file that forbids it — which
is why the cap is a number in the text rather than a principle, and why nothing enforces it: §0.1 pt 5's
predicate forbids a guard whose subject is this repository's process, and a line-count checker on
`CLAUDE.md` is exactly that.

**What this pass moved out, and what it deliberately did not.** Out: worked-failure narratives, the
history of each wording change ("this clause read X until date Y"), counter-arguments recorded for
strength, and measurement anecdotes. Kept in `CLAUDE.md`: every imperative, every hazard that names a
concrete failure mode with a mechanism, every table, and every verbatim Jordan ruling. The pass stopped
at 750 rather than a rounder number because the remainder is that content, and cutting further trades
token cost for hazard knowledge — a worse trade than the one it was fixing.

---

## §0 — why the adversarial pass may not produce a document

The flat ban existed because the pass is a **generator**: findings become ledger rows, rows become a
start-of-session surface, and that surface defines the next session's work (§0.3's T3). Gain above 1,
no human in the loop.

**The exception (RULED 2026-09-17) exists because the flat ban was losing the reasoning.** Jordan,
verbatim: *"maybe that's dumb for Claude.md to stipulate as we end up losing reasoning and reference."*
The ban is written for the pass that fires at every gating stage — small, frequent, incidental — and
for that it is exactly right. It under-provisions for a **terminal** pass whose verdict is the
deliverable: a 70-line verdict with an axis table does not fit in one commit paragraph, and
strikethroughs in the target record *what* changed without recording *why the attack succeeded*.

**And the counter-argument, recorded because it is strong and a later session will meet it.** Every
exception in this area is self-serving: a session that has just finished an audit ALWAYS believes its
audit is worth keeping, which is precisely the bias the flat ban defended against. The ban was crude,
and crude is what survives contact with an agent that can argue. So the exception is deliberately
narrow — terminal passes only, bound to a subject, gated on a test a session must fail honestly rather
than reason around. **If the exception is ever found to have become the general case, delete it and
restore the flat ban; do not add a qualifier.**

Two instances existed as of that ruling, both transcribed by hand after the fact because the ban forbade
writing them at the time: a NERS verdict, and a unification ledger over
`proposals/2026-09-17-governance-and-holdings/`.

**One word of Layer-0 self-inconsistency, repaired 2026-09-17:** this clause read `audit/` while §3
already said `.audit/`, the directory having been renamed by ED-IN-0231 on 09-16. Repaired per §0's own
rule that the repair is to edit the file.

**Why `needs_jordan` is a gate rather than a ban.** Rows are a real persistence channel across a
session boundary, and this repo has no context between sessions. The five-step gate deletes `.audit/`
**as a category, not as a cleanup**. Claim no more than it buys: **the automated loop's gain is below 1;
the agent-mediated loop is mitigated, not structurally bounded**, since prose channels depend on a
session choosing to comply, and `workplans/` entries and standing orders inside a `skills/<name>/SKILL.md`
bypass this gate entirely.

**The two carve-outs in the max-effort rule are deliberate.** Without the first ("Jordan asked for it
this session"), the literal reading tells a session to **refuse Jordan**, since a ruling request traces
to no juncture. The second covers a red `main`, which blocks everything and traces to nothing.

---

## §0.1 — why each check has an artifact, and where the rule kept failing to fire

**The originating incident (ED-MB-0042).** A flag was flipped on a **confounded measurement** and
retracted the same day. §0's adversarial pass *was* run — it attacked the result's *statistics* and
never its *setup* (are the two arms the same experiment?). Specificity about what to attack, plus an
artifact proving it happened, is the fix. `pytest tests/valoria` caught the confound only because the
flip incidentally broke unrelated tests.

**Why pt 3's table was widened (ED-IN-0228, 2026-09-16).** A session applied the rule to its
*measurements* and exempted its statements *about the tree*, which do not feel like results: it reported
a mechanism absent that was live, a gate firing zero times that fired 1,104, an eligibility route
working that no verb row uses, and quoted a file in a dissolved tree. Each was verified — the wrong half
of itself.

**Why row four was added 2026-09-17, and why it cost the most.** A session chasing a red CI gate
reported *"regenerated the census exactly as CI does; cannot reproduce"* — having never checked the
generator ran. It had; the file was byte-identical for a different reason; and the real cause (CI builds
the PR MERGE COMMIT, and `main` had moved) went unfound through **two** wrong public diagnoses, one of
them a PR comment that had to be retracted. **One `md5sum` before and after — about fifty tokens — would
have closed it.**

**Why no guard was built for pt 3**, and why the repair was an amendment rather than a sixth check: the
rule was already there and its trigger was too narrow, and answering that with more apparatus is §0.3's
own failure mode.

**Why pt 5 carries a predicate.** Without it the rule quantifies over *defects* rather than *subjects*,
firing identically on the morale model and on a freshness checker — and apparatus outnumbers game, so a
session reading more apparatus mints more apparatus guards. That is the generator; the predicate disarms
it. The terminal state of the un-predicated rule was observed: a guard on a guard on a guard, every rung
a flawless application of the rule.

---

## §0.2 — why `done` had to stop meaning "a document exists"

Jordan: *"I need to break out of the infrastructure loop."* The old `done` was satisfiable by writing,
which is the one property a milestone definition cannot have in a repo whose agent's cheapest output is
prose. This is a **precondition** of §0's max-effort rule, not its sibling: bind max effort to "the
milestone deliverable" while `done` still means "a document exists" and the doctrine aims maximum effort
at authoring prose.

**The probe named the wrong tree for six days (ED-IN-0226).** Jordan ruled on 2026-09-07 that
`engine/season/` is the head; `CLAUDE.md` went on naming `engine/mc_v18.py` as the milestone's execution
artifact until 09-13, and `tools/m1_acceptance.py` probed it. **A gate aimed at the wrong tree is worse
than a stale pointer:** it answers the question it was built to answer, incorrectly, in the direction
that looks like progress — row 1's two failing stubs were deferrals in code nobody intends to ship.

**The 71-file claim was wrong, and its correction is the cleanest instance of pt 3 working.** The file
once said `mc_v18` was *"NOT retired: 71 live files still reference it, including the composition spine
and a blocking round-trip export"*, and every part of that was wrong. MEASURED by AST, 2026-09-13: **223
files mention the name and exactly 16 IMPORT it — none of them production code.** No module under
`engine/` outside its own tests, nothing under `systems/`, and the composition spine is not among them:
`composition.json` and `module_contracts.yaml` name it only in `needed_by:` DOCUMENTATION fields, which
say who consumes a role, never what a role resolves to. The prototype is a consumer of the engine, never
a dependency of it. **The 71 was a grep of mentions read as a dependency count** — the same substitution
§0.1 is about, made one paragraph below the correction.

Deletion was then measured and REFUSED on its cost: 78 of the 136 test functions in `engine/tests/` —
57% of CI's blocking `sim-regression` job — import it, so deleting the prototype would delete 78 tests of
campaign-scale behaviour. It is deprecated WHERE IT SITS (§1 forbids a `deprecated/` tree). Whether the
existing sixteen ever move is a separate decision nobody has taken.

---

## §0.3 — the T1 experiment, and why a silent hook is not a banner

**T1 was tested, not assumed.** The start-of-session banner was reduced, then retired. The session
running under the reduced banner still wrote apparatus and no game: **T1 fell and the freed capacity
still went to apparatus, which says T2 had not moved.** That is why the instruction is to test T2 rather
than to rebuild T1 differently.

**The conflation repaired 2026-09-18.** `CLAUDE.md` said `SessionStart` was empty "deliberately", and
`tests/valoria/test_no_polling_triggers.py` pinned it empty with a comment explaining that a generated
surface at session start is the T1 growth. Both were right about the banner and both were read as a ban
on the hook **key**. The two are different objects:

| | the retired banner | `tools/session_provision.py` |
|---|---|---|
| writes to stdout | yes — a generated surface | **zero bytes** |
| enters session context | yes | no |
| defines the session's work | yes | no |
| cost | tokens, every session | one `pip install`, once per container |

**The gap it closes, MEASURED 2026-09-18 on a fresh remote container:** `pytest`, `numpy` and
`pytest-xdist` all absent, with no `requirements.txt`, no setup script and no devcontainer. So §0.4's
close gate — the shipping gate for every commit — was **unrunnable on arrival**, and a session either
skipped its own gate or spent its first minutes on pip. §8 documented the install as a one-time
per-clone step, which a container that is rebuilt per session does not have.

⚠ **As of 2026-09-18 the hook is NOT wired.** `tools/session_provision.py` exists and is documented in
§8 as the one-command setup; the `SessionStart` entry in `.claude/settings.json` was refused by the
harness's own self-modification guard when an agent tried to add it, which is the correct asymmetry —
an agent could add to `permissions.deny` but not wire a hook or widen `permissions.allow`. Wiring it is
a human edit. Until then `test_no_polling_triggers.py`'s `SessionStart == []` assertion stands
unchanged and correct; **wiring the hook means updating that assertion deliberately in the same
commit**, which is what its own message asks for.

---

## §0.4 — the 3.5× that was paid for nothing

Jordan: *"figure out a far better work pattern with Claude.md or whatever so you don't run this shit
after every edit"* — against *"8 minutes here, 2 minutes there, constant bitching about 1778 lines."*

**MEASURED 2026-09-11 on this tree, 4 cores. Collection is 1817 tests either way; `-n auto` is a
scheduler, not a filter:**

| what you run | wall clock |
|---|---|
| `python -m pytest tests/valoria -q` | **9m 01s** |
| `python -m pytest tests/valoria -q -n auto` | **2m 36s** |
| one file | seconds |

**The 3.5× was paid for nothing: `CLAUDE.md` documented the serial command while
`.github/workflows/valoria-ci.yml` ran the parallel one**, and `tests/valoria/conftest.py` was already
built for xdist (its `generated_layer` gate is an atomic cross-worker lock). A session obeying §8 paid
six and a half minutes a run to reach a verdict CI reached in two and a half. **Omitting `pytest-xdist`
from the documented install is why `-n auto` got omitted** — which is also why the provisioner installs
it.

Clause 1 (once per commit) was the missing one: the section had clauses 2–5 and never said what the unit
was, so "don't run it after every edit" had no positive instruction to replace the habit.

---

## §4 — the `evacuate` failure, in full

`evacuate` was coined for "move out of `main`, keep at a named ref". **retire** already covers that. A
later session read the coined word cold, derived "queued for deletion" from ordinary usage, concluded
the tree held two conflicting retirement policies, and escalated a non-existent blocker across three
surfaces and two PR bodies before anyone noticed the word was the whole defect.

This is why the rule has two halves rather than one. *Idempotent in meaning* is the requirement;
*idiomatic in choosing* is the only reliable way to satisfy it, because a word ordinary usage already
supplies has its meaning carried by the language rather than by context that does not survive the
session boundary.

**Why it also binds process vocabulary, which no registry covers.** Every vocabulary registry in the
tree governs design and world terms. Process vocabulary — how we describe operations on the repo — was
ungoverned, and it is the class where a coinage does the most damage, because the next session meets it
in code first and infers its meaning from the call site.

**On the size caps (ED-IN-0220).** The claim that a length cap "*is* enforced" was false. The general
`.md`/`.yaml` caps in `references/atomization_rules.yaml` were advisory, exited 0, and fired on **116
files with a median only 40% over** — describing the tree's ordinary document size rather than flagging
an outlier. They were deleted; that file's comment carries the measurement. The **explicit per-file**
caps are untouched and several are genuinely blocking.

---

## §10 — the fan-out measurements

**The sizing measurement, 2026-09-17.** A `/simplify` pass dispatched **four reviewers over a 953-line
prose diff and spent 423,171 tokens** — and all four returned the same top finding. Four independent
agents converging on one finding over a diff that small is redundancy, not corroboration: convergence is
only evidence when the search space is big enough that they could plausibly have missed each other.

**The reading-cost measurement, same date.** A governance suite fanned four `opus` authors out of one
plan. From their own completion records: **1,568,374 tokens to deliver 7,153 lines — 219 tokens per
delivered line** — and the bulk was four agents independently opening the same plan, the same round-one
documents and the same `engine/season` files. The independence was needed for the verdicts and never for
the reads: the four caught each other's errors and two converged on a corrected object count from
opposite directions, none of which required a fourth reading of `verb_table.yaml`.

`CLAUDE.md` already carried the rule pointed the other way — *"return fixed-format summaries, not raw
context: synthesis binds on the orchestrator's window"* — and the INPUT side was simply never written
down.

**The write-early rule came from a near-loss.** Two of those four authors made **zero `Write` calls
across ~1.2 MB of transcript each** and had to be told to start; without that intervention both stages
would have been lost whole.

**The stagger was stated twice because once was not enough.** That run fired all four agents at once and
every one paid full price for an identical preamble.

**The single-call form.** One unfiltered workflow-run listing returned **242,640 characters** for a fact
that three rows carried.

**What is deliberately NOT a rule, because §0.3 says more apparatus is this repository's own failure
mode.** That session's other four costs were real and got no rules: two are **already ruled** and the
fix is compliance rather than text — speculating before measuring is §0.1 pt 3, and re-running the suite
is §0.4's cadence — and two were ordinary clumsiness with no general shape (a checker rewritten three
times over its own regex; a PR body re-sent whole for a one-line edit). **Writing a rule for each would
have been eight rules where three were load-bearing.** If §10 is ever found growing an item per incident,
that is the accretion §0.3 describes, and the repair is to cut it back to the measurement.

**Why §11 has a deny and §10's sizing rule does not.** Jordan ruled the RULE first in §11's case. A
`PreToolUse` deny on multi-`Agent` dispatch was put to him as §11's shape applied to fan-out cost, and
the answer was *"I want multiple agent dispatches."* Absent a ruling, a deny is apparatus looking for a
rule.

**The critic/author asymmetry, and the general lesson.** `valoria-author`'s first version removed `Bash`
and `Agent` and called the removal structural. Jordan ruled otherwise 2026-09-17: *"we still need agents
and bash."* That version offered itself for code changes while removing every means of verifying one —
§0.4 cl.2's covering test file, §0.05 cl.3's re-derive, an exporter's `--check`. **Removing a tool to
enforce a process rule buys a CONTROL only where the rule IS the absence** (the critic's independence
*is* its missing write tool). Elsewhere it buys a crippled lane.

---

## §11 — the 116 check-ins

In the **2026-07-19..26** window, **116 `send_later` self check-ins** re-entered persistent sessions to
re-confirm PRs that were already green — **97 of 118 trigger prompts said so themselves**. A wake-up
re-sends the whole conversation; with an EMPTY conversation that was still **~23.2k tokens**, so the
floor was **~2.7M tokens for zero state change**. The median wake-to-wake gap was **61.9 minutes**, just
past the 1h prompt-cache TTL, so most of it was uncached.

**The roster grows when the surface does, and that is the guard working rather than failing.**
ED-IN-0084 wrote its own falsifier: *"if it ever passes while a session is still arming wake-ups, the
guard is wrong and the mechanism has moved — find the new primitive and add it to REQUIRED_DENY."*
ED-IN-0085 then found three that had moved, all reachable in-session while the original four passed.
**2026-09-18 found two more the same way** — `Monitor` (documented as an until-loop waiting on a
condition) and `watch_url` (arms an inbound webhook that wakes the session when idle) — by enumerating
the session's actual tool surface rather than re-reading the list. The roster had not been re-swept
since 2026-07-28.

**A known limit of the `Skill(loop)` entry**, stated rather than assumed: the MCP entries match a
fully-qualified tool name, a format this repo has seen enforced. `Skill(loop)` uses Claude Code's
skill-permission syntax, which the test pins as an ARTIFACT but cannot execute. If the runtime spelling
differs, the test still passes while /loop stays reachable — the same blind spot ED-IN-0084 named for the
whole roster. Re-verify against a live permission denial before trusting it.

**The cost figure in the test's docstring was stale by 57%** until 2026-09-18: it cited `CLAUDE.md` at
~12.2k tokens against a measured 19,228, understating the rule's own payoff.
