# Refuter R3 — threadwork/knots/FI claims

_Archived verbatim from the agent's final message (2026-07-07)._

# Refutation Record — Independent Refuter R3

Charter read: `designs/audit/2026-07-07-unaddressed-areas-audit/00_grounding/00_charter.md` only. Cluster dossiers not consulted. All findings below are from direct file reads and grep/python probes against the working tree.

---

**Claim 1** — threadwork is a total island with zero callers on the mc_v18 campaign path, no scene_type, no trigger, no test coverage.

**VERDICT: CONFIRMED**

- No function defined in `sim/thread/{operations,coherence,collective,opposing,co_movement,threadcut,rendering}.py` or `sim/personal/knots.py` (`attempt_leap`, `attempt_mending`, `form_knot`, `sustain_knot`, `apply_coherence_delta`, `attempt_collective_operation`, `resolve_opposing_operations`, `draw_comovement_card`, `mark_threadcut`, etc.) has a caller anywhere outside the thread/knots files themselves — repo-wide grep returns zero hits.
- `sim/mc_v18.py` (166 lines, the campaign entry point) never mentions thread/knot/coherence at all (`grep` zero hits).
- `sim/cross_scale/scene_dispatch.py:88-101` (`_resolve_slot`) only handles `scene_type in {"combat","contest"}`; everything else falls to `else: reason = "resolver ... not live"`. `queue_scene(` (`sim/autoload/scene_slate.py`) is only ever invoked once, from `scene_dispatch.py:75`, and only with `scene_type="contest"` (Stability Crisis). No caller ever queues `"thread"`, though it's listed as an illustrative example type in a comment (`scene_slate.py:26`).
- `game_state.py:315,345,355` imports from `sim.thread.coherence`/`sim.personal.knots`/`sim.thread.threadcut` only inside `deserialize_world`'s `.from_dict()` branches, gated on keys that nothing on the live campaign path ever populates.
- `sim/tests/` contains exactly 3 files (`test_mc_v18_regression.py`, `test_contest_kernel.py`, `test_sigma_leverage_parity.py`); none mention thread/knot/coherence. `tests/valoria/` likewise has zero hits.
- Minor nuance (does not weaken the claim): `zoom_in_out.py:165-167` does define a canonical "Knot Partner in Crisis" *trigger name*, but it's in the unevaluated/deferred set (only "Stability Crisis" is field-evaluable per `scene_dispatch.py`'s own docstring) and doesn't map to a `thread` scene_type regardless.

**Intent gate:** MIXED — the scene-dispatch narrowing itself is documented as deliberate (`scene_dispatch.py`'s "DELIBERATE BOUNDARIES" docstring explicitly says only Stability Crisis is evaluable and the rest are "reported as deferred, not faked"). But the *total* absence of any thread scene_type ever being queued, and the complete absence of `sim/tests` coverage, are undisclosed anywhere — consistent with the charter's own framing that "threadwork [was] never audited directly." Net: **DELIBERATE (dispatch gap) + NOT-INTENDED (test-coverage gap)**.

---

**Claim 2** — Mending's Coherence cost contradicted 3 ways across 5 sources + a lapsed ED-871 ruling.

**VERDICT: CONFIRMED**

- `canon/02_foundations_amendment_leap_mechanism.md:38` — "Mending's Coherence cost is zero... This is not a mechanical exception."
- `designs/threadwork/threadwork_v30.md:474-481` (§2.4, "Mending — Repairing the Substrate") — all four degree rows say "Coherence: 0"; line 481: "Mending Coherence Asymmetry: Mending never costs Coherence."
- `designs/threadwork/threadwork_v30.md:624` (§3.2 table) — "Mending | −1 (substrate engagement is inherently deep regardless of Gap scale)" — directly contradicts §2.4 in the same file.
- `params/threadwork.md:275` — "Mending costs 0 Coherence per asymmetry — this is free for all participants."
- `sim/thread/operations.py:311-326` (`attempt_mending`) — hardcodes `coh = -1` citing §3.2 verbatim in comment, and `_resolve_operation` (lines 184-186) subtracts an *additional* −1 on Partial/Failure, giving effective −2 on those degrees.
- `canon/editorial_ledger.jsonl:354` (ED-871) — "RESOLVED 2026-05-31: Mending Coherence cost = 0 ... Any non-zero statement reconciles to 0; threadwork doc-edit routed (lane-gap)." The current working tree at §3.2 (line 624) still reads −1 — the ordered fix never landed. Ledger's own `jordan_decision` field is still `"pending"`.

**Intent gate:** NOT-INTENDED — the ledger itself documents the fix as ordered-but-unexecuted ("lane-gap"), not a deliberate re-litigation.

---

**Claim 3** — Thread Fatigue (ED-694) has zero implementation in sim/.

**VERDICT: CONFIRMED**

- `designs/threadwork/threadwork_v30.md:185-195` — "Thread Fatigue counts up from 0 toward threshold = Spirit × 5"; per-op costs (Leap 3, Mending 4/round, Pulling 5/round, Locking 7/round, Dissolution 10/round); Focus gates max operations per contact session.
- Repo-wide probe: `grep -rn "ED-694\|Spirit \* 5\|max_operations\|operations_remaining\|contact_rounds" sim/ --include="*.py"` → zero hits. `grep -rln "fatigue\|Fatigue" sim/ --include="*.py"` → only `sim/personal/contest_legacy_stub.py`, which implements an unrelated "Contest Fatigue" mechanic from social-contest §6, not Thread Fatigue.
- No `TODO`/`GAP`/stub comment anywhere in `sim/thread/operations.py` or `sim/thread/coherence.py` acknowledges Thread Fatigue as a known, deliberate omission.

**Intent gate:** NOT-INTENDED / UNDETERMINED — no disclaimer flags this as an intentional deferral anywhere in code or `sim/README.md`/`CONVENTIONS.md`.

---

**Claim 4** — `sim/personal/knots.py` implements "the PP-632 fixed-capacity model (Distant=4/Close=7...)" that ED-912 superseded.

**VERDICT: QUALIFIED** (substance true, attribution wrong)

- `sim/personal/knots.py:59-66` does implement a fixed-capacity, monotonic-strain model: `TIER_CAPACITY = {"Distant": 4, "Close": 7}`, with `sustain_knot` (line 251) clamping strain at a floor of 0 and breaking when `strain > capacity` (line 256) — never decreasing below 0, i.e., not the bidirectional gauge.
- `canon/editorial_ledger.jsonl:399` (ED-912, resolved 2026-06-28) explicitly states the Knot model is now "a bidirectional −5..+5 bond-strain gauge (Distant −2..+5 start 0; Close −5..+5 start −2)" and that this **"supersedes PP-632/PP-684."** So the *substance* — knots.py is stale, superseded by ED-912's bidirectional gauge — is correct.
- **However**, the Distant=4/Close=7 capacities are NOT the PP-632 model. Per `sim/personal/knots.py:13-19` (its own docstring) and `designs/personal/knots_v30.md:47,58,321` (§2, §11/TIER-DRIFT-001), PP-632's actual tier model is a *different*, 3-tier "Loose/Medium/Close" point-cost scheme with capacities **1/2/5**, distinct from the Distant/Close 4/7 model, which the code and doc both attribute to **ED-773 ("Option A")**, not PP-632. `sim/personal/knots.py:22,78` cites PP-632 only for the separate rupture-Coherence-loss constant (−1) and Knot-count-cap formula — never for the 4/7 capacities. Claim 6 independently confirms PP-632's real numbers are 1/2/5, not 4/7 (see below).

**Intent gate (for the confirmed-stale substance):** NOT-INTENDED — the sim module has simply not been touched since ED-912 landed (2026-06-28).

---

**Claim 5** — `knots_v30.md` is internally self-contradictory post-ED-912.

**VERDICT: CONFIRMED**

- `designs/personal/knots_v30.md:45-58` (§2) — "Tier System — RESOLVED (ED-912, 2026-06-28)"; states the old "0→capacity accumulator (Distant 4 / Close 7)" is replaced by the bidirectional −5..+5 gauge.
- `designs/personal/knots_v30.md:178-187` (§6.1) — still headed "**Tier capacities [PROVISIONAL: TIER-DRIFT-001 — see §2]**" with the table `Distant Knot | 4 strain`, `Close Knot | 7 strain` — the superseded model, unedited.
- `designs/personal/knots_v30.md:202` (§6.2) — "Disposition → **−4** (per PP-632 rupture spec + §3.5.4)" for the public-citation rupture trigger, whereas ED-912's ratified resolution (`editorial_ledger.jsonl:399`) sets "break/rupture = Disposition −3." (Notably, `params/fieldwork.md:167` already carries the corrected "−3" value, confirming −4 in knots_v30.md is stale, not a live alternate reading.)
- `designs/personal/knots_v30.md:315-325` (§11) — still lists TIER-DRIFT-001 as an open item "for Jordan resolution" at a future "Pass 2k," with a recommended resolution of flat Distant/Close 4/7 (Option A) — which doesn't even match what ED-912 actually ratified (the reframed bidirectional gauge, not flat 4/7).

**Intent gate:** NOT-INTENDED — a partial edit: §2 was patched to declare resolution but the cascade into §6.1/§6.2/§11 was never completed.

---

**Claim 6** — `canon/mechanics_index.yaml`'s knots entry still encodes the struck PP-632 tier model.

**VERDICT: CONFIRMED**

- `canon/mechanics_index.yaml:344,351,352` — `pp: PP-632`; `tiers: {close: 5, medium: 2, loose: 1}`; `rupture: "Disposition -> -4"` — byte-exact match to the claim, and to knots_v30.md's own description of the struck PP-632 model (`knots_v30.md:58,321`: "PP-632 Loose/Medium/Close 3-tier point-cost model (1/2/5)"). This is stale against ED-912 (2026-06-28), which struck this model entirely in favor of the Distant/Close bidirectional gauge.
- (Corroborates claim 4's qualification: this is the true PP-632 numbering — 1/2/5 under Loose/Medium/Close — distinct from the 4/7 Distant/Close numbers in `sim/personal/knots.py`.)

**Intent gate:** NOT-INTENDED — stale index row never cascaded from the ED-912 ratification.

---

**Claim 7** — `params/fieldwork.md` self-contradicts on Thread-Read's attribute (Spirit vs. Attunement).

**VERDICT: CONFIRMED**

- `params/fieldwork.md:26` (Primary-Attribute table) — "Investigation | Thread-Read | Spirit (+ Thread Pool Score)".
- `params/fieldwork.md:106` (§"Thread-Read (Perceptive Leap)") — "Pool: (Att × 2) + History bonus + Thread Pool Score (TS ÷ 10)." Exactly 80 lines later, matching the claim precisely.
- `params/core.md:144,246` unambiguously defines "Att" = Attunement, ruling out a benign reading of "Att" as a generic "Attribute" placeholder.
- Additional corroborating drift (not required by the claim but reinforces it): `designs/threadwork/threadwork_v30.md:458` (PP-616/PP-625) explicitly struck Attunement from all Thread-operation pools in favor of Spirit — so line 106's "(Att × 2)" is doubly stale, both against its own table and against upstream canon.

**Intent gate:** NOT-INTENDED — line 106 reads as a pre-PP-616/625 leftover formula that was never updated when the Primary-Attribute table row (line 26) was corrected to Spirit.

---

### Summary
6 of 7 claims **CONFIRMED** outright (1, 2, 3, 5, 6, 7); 1 claim (4) **QUALIFIED** — its core "stale, ED-912-superseded" assertion holds, but its citation mislabels the Distant=4/Close=7 model as "PP-632" when the code/doc/ledger all attribute those specific numbers to ED-773 ("Option A"); the real PP-632 model (confirmed independently via claim 6) is the distinct Loose/Medium/Close 1/2/5 scheme. No claim was fully refuted.
