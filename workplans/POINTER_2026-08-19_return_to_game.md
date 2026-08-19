# Pointer — Return-to-Game program (IN lane)

**target:** `workplans/return_to_game_queue.yaml` — the executable queue IS the plan. There is
deliberately no companion `proposals/` document: this program's own thesis is that the repo has
nine planning surfaces for consolidation and roughly two executions, so adding a tenth prose plan
would be the defect it exists to end. The queue file carries the protocol, the steps, the measured
baselines, the gate tier, the pre-commit checklist and the failure decoder in one place.
**lane:** IN (cross-cutting: game repo + acceptance gating + ledger disposition) · **ED:** none yet —
`registers/editorial_ledger_in.jsonl` had **80 tokens of headroom** under its blocking 50,000-token
cap when this was authored, which is exactly why step S0 archives before anything files.
**liveness:** LIVE — authored 2026-08-19, no step started.
**scope:** nine steps, S0–S8, totalling ~8 sessions, that return Jordan to building the game.
S0 clears three silent stalls (ledger headroom, push scope on `jordanelias/valoria-game`, the
measured gate tier). S1–S4 change what "done" means in this repo from a document state to a program
state: make the game compile and put a compiler in CI, arm `tools/m1_acceptance.py` with the run its
four blocked rows need, close the 20-key roster gap, and run the 13 test suites that have never run.
S5–S8 then shrink things safely: unbind the attribute registry (registry-only, zero code churn),
make the M1 board measure the program rather than the paperwork, prepend the game's compile verdict
to the SessionStart banner, and drain the decision queue mechanically. **Zero steps require a
ruling.** The entire human ask is `jordan_docket:` — seven one-sentence questions, each with a
recommendation, down from 109 open `needs_jordan` rows.

> **The ordering is load-bearing; do not "improve" it.** S5–S8 are only safe *after* S1–S4, because
> a cull or a reconcile performed while `done` still means "a document exists" is the ninth
> consolidation plan. The queue file says this at the top for the same reason.

> ⚠️ **Known-stale upstream text this pointer does NOT inherit.** `proposals/2026-08-18-next-session-handoff.md`
> §1.2 lists three `sha256_buffer` sites; there are **five**. It states the defect list is "complete
> as of `5e01065`"; measured against Godot 4.3 headless it is the first parse-error layer only —
> the stock tree reports **54 script-load failures / 169 parse errors / 61 broken scripts**. It
> frames one project setting as "worth more than all five defects"; measured, that setting alone
> moves 169 → 161 and clears zero broken scripts, while the defects take the tree to 5/14/8. And
> `proposals/2026-08-18-breaking-the-recursion.md` §7.1 asserts `ci_names_check` is blocking in CI;
> it is report-only in **both** tiers. All four corrections are recorded in the queue file with
> their reproduction methods.

> ⚠️ **Claims one shared surface.** `tools/session_status.py` (S7 prepends one line) is edited by any
> session that changes the banner. S7 adds exactly one line and touches nothing else; the full
> banner replacement proposed in the 2026-08-18 handoff §1.6 is deliberately parked in `held:` as
> H4, not executed here.
