# FI DECISION MEMO

**FROM:** Session scribe (read-only assembly)
**TO:** Jordan (ratification authority)
**RE:** Interview head-conflict governance — fieldwork_v30 §4.2 vs investigation_systems_v30 (post-MERGE)
**DATE:** 2026-07-08

---

## 1. HEADLINE — two separate questions, do not conflate them

**(i) Design merit — SETTLED.** `ED-FI-0004` (`canon/editorial_ledger.jsonl:386`, executed 2026-07-08, echoed in `handoffs/HANDOFF_FI.md:13-22`) ruled the pessimist-action audit's Interview **MERGE**: the bare single-roll Interview object at `fieldwork_v30.md §4.2` is inferior, as a design, to the Dialogue Lattice (`investigation_systems_v30.md` System 3/S14) — which `investigation_systems_v30.md:427`'s own Cross-System table already claims Interview "routes through... instead of single Charisma roll." That is not a new claim; it is the design already asserting its own supersession. Closed — do not re-litigate here (see §2 on why it forecloses one path).

**(ii) Governance — OPEN.** Which file's `## Status:` line is CANONICAL-in-fact, and how much of the Lattice's ~9,000-token apparatus (NPE, Investigation Interface, Dialogue Lattice, Response Resolution Matrix) becomes a **binding-to-build** commitment now versus staying aspirational prose — plus what that decision does to `ED-921` and the fieldwork half of `ED-IN-0016`/EP-8, neither of which the MERGE itself closed (it "retires ED-921 + the fieldwork half of ED-IN-0016/EP-8 to one ruling" *once* this governance question settles — `canon/editorial_ledger.jsonl:386`).

---

## 2. Original menu (`cluster_C-FI.md:22-24`) — quoted verbatim, and why Option A is dead

> **Option A — fieldwork_v30 wins outright.** CURRENT.md's new fieldwork row cites only `fieldwork_v30.md` (+ co-files); `investigation_systems_v30.md`'s Status line flips CANONICAL → SUPERSEDED/struck... *Consequence:* honest currency immediately, but discards ~9,000 tokens of load-bearing conversational-depth design... that nothing else in the corpus replaces.

> **Option B — investigation_systems is the target, fieldwork is the gap.** Re-flip investigation_systems_v30.md's status CANONICAL → PROPOSED; open a scoped FI-lane ED to actually port its four systems into fieldwork_v30... *Consequence:* real design + sim work... the only option that resolves the substance, not just the label; largest scope, no shortcut.

> **Option C — split-head, minimal edit.** CURRENT.md's fieldwork row cites `fieldwork_v30.md` as canonical for every currently-playable mechanic... investigation_systems_v30.md's Status flips CANONICAL → PROPOSED with an explicit banner... *Consequence:* cheapest, fastest to ratify... but leaves the underlying design gap... unresolved for whenever Option B's work is eventually scheduled.

Option A is now **foreclosed by the MERGE ruling itself**: it would keep the bare-roll Interview as the *sole* canonical home for the verb the audit just adjudicated the Lattice handles better (`dossier_FI.md:71`: "not a judgment that conversational investigation is weak... but that keeping *two* canonical specs for one verb fails"). Ratifying Option A now would contradict `ED-FI-0004` in the same pass that cites it. (Flag: the audit's own critic pass, `critic_FI.md:44-48`, argued Option A was "at least as textually defensible" *before* the MERGE was ratified — that door closed when `ED-FI-0004` executed.)

---

## 3. The live fork — Jordan's actual call

- **Option B (full port, now).** Flip `investigation_systems_v30.md`'s Status line fully CANONICAL-in-practice; open the FI-lane ED to fill all 6 `NotImplementedError` stubs (`sim/personal/investigation.py:22-31`, `sim/personal/fieldwork.py:24-33`, per `cluster_C-FI.md:14`) and wire the Lattice into `fieldwork_v30`'s Interview object as real, playable mechanics — including resolving `ED-921`'s schedule/attribute mismatch (`canon/editorial_ledger.jsonl:190`) and the Q-elegant REFINE already flagged (`investigation_systems_v30.md:326`: five-filter chain needs a build-gating "why this NPC responded" readout before it ships). **Effect:** retires `ED-921` outright; closes the fieldwork half of `ED-IN-0016`/EP-8 by construction; the new `CURRENT.md` fieldwork row cites the ported, unified doc. Largest scope, no shortcut — real sim authoring, not a status edit.
- **Option C (split-head, staged).** `fieldwork_v30.md` stays canonical for every currently-playable mechanic (rolls, Evidence Track, Exposure, Disposition, Knots); `investigation_systems_v30.md`'s Status flips CANONICAL → PROPOSED with an explicit banner that the Interview-routes-through-Lattice claim (`investigation_systems_v30.md:427`) is aspirational, not implemented. **Effect:** `ED-921` stays open but scoped as "settle when Option B is scheduled," not urgent; the fieldwork half of `ED-IN-0016`/EP-8 closes immediately (the "canonical-in-name-only" mislabel is fixed the moment the banner goes on); the new `CURRENT.md` fieldwork row cites `fieldwork_v30.md` alone, with a pointer to the PROPOSED Lattice doc. Cheapest, fixes the label now, defers Option B's substance to a re-visit.

I could not honestly ground a third "partial port" option: the Response Matrix's five filters read the NPE's Genome axes directly (`dossier_FI.md:85`: "Genome axes are exactly what the five-filter chain reads"), so promoting only the Interview-routing slice while leaving NPE/Interface/Matrix PROPOSED would sever a load-bearing dependency, not cleanly split one. Omitting that option rather than inventing a seam the corpus doesn't support.

---

## 4. Closing — downstream unblock and scope guardrail

Either pick unblocks `ED-FI-0002` (counter-espionage loop), which `HANDOFF_FI.md:29-31` says explicitly "**Composes with** ED-FI-0001 (investigation-lane audit) and the audit's EP-8 (investigation_systems_v30 canonical-in-name-only; head conflict settles via ED-IN-0016's CURRENT.md row)" — that design work is blocked on knowing whether its detection/response verb is hosted by fieldwork's bare roll or the Lattice's filter chain. No sim edits ride on this pick alone: `ED-FI-0004` itself notes "No sim edits (investigation.py/fieldwork.py are NotImplementedError stubs)" (`canon/editorial_ledger.jsonl:386`) — both entry points stay stubbed regardless of which governance option you choose; Option B is what would eventually fill them, not this ruling by itself.

**Decision requested:** Option B, Option C, or conditional (state condition) — this memo does not recommend between them.

**END MEMO.**
