# BONUS-STACK CAP — NUMERIC CEILING DECISION MEMO

**FROM:** SC lane (design-source scribe)
**TO:** Jordan (ratification authority)
**RE:** Recall + Corroborate + Prep + Findings non-attribute bonus class — pick the combined ceiling (ED-SC-0005, P0 docket)
**DATE:** 2026-07-08

---

## 1. HEADLINE

**Already settled, not reopened:** ED-SC-0012 (RESOLVED 2026-07-08, `canon/editorial_ledger.jsonl`; annotation at `designs/scene/social_contest_v30.md` line 89) adopted the *principle* of a single global cap on the combined Recall + Corroborate + Prep + Findings non-attribute bonus class, mirroring the existing +2D genre/audience ceiling (line 85) "in spirit." The individual actions are not cut. That question — cap or no cap — is closed.

**Open, and yours:** the *numeric value* of that cap, tracked as **`ED-SC-0005`** ("P0 docket / P2 FORK — cap value is Jordan's design number," `canon/editorial_ledger.jsonl`) — the fourth of four P0 forks on the docket ED-SC-0002..0005 that `handoffs/HANDOFF_SC.md` (Pending, lines 118-121) lists as awaiting your picks. This packet narrows only that fourth item; it does not reopen echo-keying, tracker naming, or `ED-SC-0004`'s separate kernel-Argue-pool-formula fork. (A citation slip — ED-SC-0012's annotation and the Pending write-up had pointed to `ED-SC-0004` for this cap value, when `ED-SC-0005` is the entry that actually carries it — has been corrected alongside this packet.)

## 2. The arithmetic

Per-exchange non-attribute bonus sources, currently uncapped as a class:

| Source | Value | Cite |
|---|---|---|
| Recall (cite a specific, verifiable claim; binary) | +2D | line 169 |
| Corroborate (Step 2b, declared coalition support) | +1D | line 162 |
| Pre-Contest Prep (Overwhelming Attunement+History roll) | +1D | line 534-535 (§9.1) |
| Findings citation (F-TRANS-11, per Finding, capped at this line item alone) | +2D max | line 539 |
| **Subtotal, this class** | **+6D** | |
| Genre + audience match (separately capped, line 85) | +2D | line 85 |
| **Worst case, all non-attribute bonus** | **+8D** | |

Line 539 already says Findings "stacks with standard preparation (+1D), for a maximum Exchange 1 bonus of +3D when both are available" — that +3D is just the Findings+Prep pairing; the full +6D adds Recall and Corroborate on top. But Prep (lines 534-535) and Findings (line 539) are both explicitly **Exchange-1-only**, in *both* Formal and Grand Contests — so the full +8D is reachable only once, at Exchange 1. What varies by format is Recall alone: Formal Contests (3-exchange, line 101) can re-earn +2D each subsequent exchange with a fresh citation; Grand Contests (5-exchange, line 171, ED-617) exhaust each cited source for the whole contest instead. So exchanges 2+ cap out at +5D (Recall+Corroborate+genre/audience) in Formal Contests, and at ≤+5D, shrinking as sources are exhausted, in Grand Contests.

Against a base Argue pool of (Primary Attribute × 2) + History bonus (§3, lines 117-141) — framed elsewhere as running roughly **12-18D** before any bonus — an uncapped +8D is a 44-67% pool inflation from non-attribute sources alone, on top of whatever the genre cap already permits.

## 3. Candidate ceilings

- **Option A — combined cap at +2D** (strict mirror of the genre/audience ceiling). Most restrictive: forces choosing one source (a Recall *or* two Findings *or* Corroborate+Prep) per exchange. Effectively makes the four actions compete rather than compound.
- **Option B — combined cap at +3D.** Roughly 1.5 sources' worth (e.g., Recall alone leaves 1D spare for Prep, or the existing Findings+Prep +3D pairing at line 539 becomes the de facto ceiling case). Still meaningfully bites the full four-source stack.
- **Option C — combined cap at +4D.** Permits two full sources (e.g., Recall+Corroborate, or Findings-max+one-other) without penalty; only bites the 3-4-source pile-on.
- **Option D — one COMBINED cap across both classes** (genre/audience +2D *and* Recall/Corroborate/Prep/Findings) at a single grand total, e.g. +4D overall rather than +2D-and-separate-N. Structurally different: one ceiling, not two stacked ceilings. Forecloses ever reaching today's nominal +8D-adjacent worst case regardless of how the two classes split, but goes further than ED-SC-0012's "mirroring... in spirit" framing — it would require rewriting line 85's "maximum +2D" language as a sub-clause of the grand total rather than an independent cap.

**Your call: A / B / C / D, or another value.**

## 4. What this unblocks

Landing this value closes `ED-SC-0005` and, with it, the last cap-specific item on the P0 docket (`ED-SC-0002..0004` remain separately open — echo-keying, tracker naming, kernel pool formula). It is also a named **Stage-4 entry criterion**: `handoffs/HANDOFF_SC.md` states verbatim that "**ED-SC-0005's stack cap must land in prose before wiring**" (line 142).

This pick is **prose-only.** Per `ED-SC-0005`'s own ledger entry, all four bonus channels have "zero code presence beyond comments/flavor" in the actively-rebuilding kernel (`sim/personal/contest/`) — nothing here touches the live sim rebuild; it only needs to land in `social_contest_v30.md` before Stage 4 wires the channels.

**END MEMO.**
