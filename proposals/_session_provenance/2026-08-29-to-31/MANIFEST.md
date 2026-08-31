# SCRATCHPAD MANIFEST — every file in the session scratchpad, and where it is
## 2026-08-29 → 2026-08-31 · the from-scratch design exercise, the coverage instrument, the arc
## reachability test, and the three-part integration task.

**Purpose.** Jordan asked for the scratchpad committed as provenance. This manifest accounts for
**every** file in it — the ones copied here, and the ones deliberately not copied, with where each
resolves. Nothing is silently omitted.

**The rule applied:** copy working material that exists nowhere else; **do not duplicate content that
already lives in this repo or at a named ref** — point at it instead. That is this repository's own
resolution discipline (`references/restructure_ledger.md`), applied to a scratchpad.

---

## COPIED HERE — working material that exists nowhere else (19 files)

| file | what it is | when |
|---|---|---|
| `AXIOM.md` | Jordan's containment-ladder axiom as a binding brief — Individual → Family → Community → Settlement; a faction is any aggregate at any scale | 08-29 |
| `NERS.md` | the N/E/R/S charter as ruled — **E is a ratio against N and R, not a fourth averaged axis; S = T5/T6 restated; R is structural** | 08-29 |
| `SPINE_INPUTS.md` | the nine throughlines T1–T9, the design brief the whole exercise answers | 08-29 |
| `ARCH.md` | the modular-hierarchy architecture constraint — the module tree IS the containment ladder | 08-29 |
| `SETTING.md` | canon roster, factions, places — the sources the season probes and arc tests drew on | 08-29 |
| `PRECEDENT.md` | precedent corpus extracts (20K), the largest working file | 08-29 |
| `BRIEF.md` | the from-scratch design brief | 08-29 |
| `AUDIT_BRIEF.md` | the four-critic NERS audit brief | 08-29 |
| `dice.py` | the d10 success-distribution calculation (per-die 0/1/2 successes at 6/10, 3/10, 1/10) used for the resolution-surface arithmetic | 08-29 |
| `CODESHAPE_FORBIDDEN.md` | PR #342's compliance constraints, extracted verbatim for the lanes. ⚠ **Its prose paraphrase of §7 lists ELEVEN items; §7 has FOURTEEN** — see `12_PART3_RECONCILIATION.md` §3, this is the mechanical origin of the row nobody walked | 08-30 |
| `FINDINGS_DIGEST.md` | the digest of findings handed to the Part 1 reviewers | 08-30 |
| `PESSIMISTIC_NERS.md` | P-1..P-5, the pessimistic rules | 08-30 |
| `RELAY.md` | the agonist→antagonist relay discipline | 08-30 |
| `REVIEW_B_ARCS.md` | the arcs review working draft | 08-30 |
| `PART2_AGONIST_BRIEF.md` · `PART2_ANTAGONIST_BRIEF.md` | Part 2's two halves, **committed before the lanes returned** so the relay stays checkable | 08-30 |
| `PART3_BRIEF.md` · `PART3_ANTAGONIST_BRIEF.md` | Part 3's two halves, same discipline. ⚠ The Part 3 brief's pointer to "`07` §E" for the `exposure` collision is half wrong — recorded in `10_comparative_judgment.md` §0 | 08-30/31 |
| `README.md` | the provenance directory's own note | 08-30 |

Four of these (`PESSIMISTIC_NERS`, `RELAY`, `FINDINGS_DIGEST`, `REVIEW_B_ARCS`) were also promoted
into `proposals/2026-08-31-integration/` as `00b`, `00c`, `00d` and `01`. **The scratchpad originals
are kept here as well**, because the promoted copies were edited and these are what the stages
actually read.

---

## NOT COPIED — and where each resolves

| file | size | why not, and where it is |
|---|---|---|
| `hcac.txt` | 160K | **A verbatim extract of `research/historical_concerns_action_catalogue_v1.md`**, live in this repo. Read the original. |
| `pgsr.txt` | 84K | **A verbatim extract of `research/proactive_governance_scale_research_v1.md`**, live in this repo. |
| `pmi.txt` | 60K | **A verbatim extract of `research/personnel_muster_integration_master_v1.md`**, live in this repo. |
| `hcac_synth.txt` | 40K | A working synthesis of the first — cross-domain ripple chains. Superseded by the design suite it fed; the source is live. |
| `arcs/` | 892K | **The 83-arc corpus extracted from ref `v30-snapshot-2026-06-28`, path `designs/arcs`.** Recoverable at that ref, which is exactly how the exercise obtained it. Not re-committed to `main` — the arcs are, in Jordan's words, *"old and deprecated in many ways"*, and the reachability test's verdicts live in `proposals/2026-08-30-arc-reachability/`. |
| `out/01_arcs_01_18.md` | 56K | An intermediate lane output, superseded by the committed `proposals/2026-08-30-arc-reachability/01_arcs_01_18.md`. |

**Total not copied: ~1.3MB, every byte of it recoverable** — three from live repo paths, one from a
named ref, two superseded by committed outputs.

---

## WHAT THE PROVENANCE IS FOR

The relay's independence is only checkable if the briefs are fixed before the results arrive. Both
Part 2 briefs were committed at `3dbdf16d`, before either lane returned; both Part 3 briefs at
`b5777ccc`, before either stage returned. **Neither can have been retrofitted to flatter a result.**

That matters because this session's dominant defect was a confident claim that direct read refutes —
**six instances, every one authored upstream of the producer that inherited it, every one caught by a
reader that had not seen the producer's reasoning.** Two of the six trace directly to files in this
directory: `CODESHAPE_FORBIDDEN.md`'s eleven-item paraphrase of a fourteen-row list, and the Part 3
brief's mis-pointer. **They are kept unedited, with their errors, and annotated in the table above** —
a provenance directory that quietly fixed its own inputs would be worth nothing.
