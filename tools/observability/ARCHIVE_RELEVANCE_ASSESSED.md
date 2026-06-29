# Valoria — Archive Relevance, ASSESSED

> Deep adjudication of the archive→open-item leads from `ARCHIVE_RELEVANCE.md`. Each item was read
> at both ends (the open flag **and** its claimed resolution), checked against
> `canon/supersession_register.yaml` for currency, and — for closable/partial verdicts —
> adversarially re-verified. **Coverage: 4 of 22 candidate units fully adjudicated** before the run
> hit transient server rate-limiting (not a spend limit). The other 18 are listed in the appendix and
> can be finished the same way on request. The 4 below are **high confidence**.

## Archive-Relevance Assessment

This report covers a capped subset of the archive sweep: **4 fully adjudicated units out of 22 candidate leads.** Every item below was independently read, and the closable/partial ones were adversarially double-checked. All four came back at **high confidence**. The single item that carried a formal verification step (the articulation layer) was **upheld**.

The bottom line: of these four, **two are genuinely done and you can stop worrying about them**, **one is half-done** (the easy half can be cleaned up now, the other half needs your sign-off), and **one is a real decision still sitting on your desk.**

---

### 1. What you can stop worrying about (already decided)

**The articulation layer is final. It is canonical.**
An old audit note from May 8th says it's "provisional, pending ratification." That note is simply out of date — the layer was ratified on **May 1st**, a week *before* that audit was written. The auditor was reading a stale banner left inside the design file, not the actual register. The authoritative source register confirms it's canonical, and an independent check verified that register entry points at the exact current version of the file and has never been reversed. No decision is owed. The only housekeeping is closing the stale audit flag and tidying three leftover "PROVISIONAL" banners inside the design file so this false alarm doesn't resurface in the next audit.

**The mass-battle command architecture (ED-907) is ratified.**
This is the Football-Manager-style three-level battle command design — the general sets army doctrine, each company picks a formation, and companies run internal roles. **You ratified it on June 20th**, and that approval is recorded and committed in the ledger. The engine pieces are built. The fancier player-control UI layers (the hold-shape/adapt toggle, the allocation grid, the mid-battle intervention windows) are deliberately parked as future videogame work — and importantly, they are explicitly declared *not* gaps, so they should not haunt you as unfinished business. The only loose thread is a stale "(prov)" tag in the workplan, which the workplan itself already contradicts in a later row. Strike the tag; nothing else is owed.

---

### 2. What's half-done (one part settled, one part needs you)

**The Key-type registry (ED-935): registrations done, payloads still need your eyes.**
Two things got bundled together here, and only one is finished.

- **Done:** The new Key types were officially registered on June 14th (you approved it). Because of that, several "unregistered / NOT in registry" comments scattered through the contracts file are now simply wrong and can be corrected immediately, along with regenerating the module map. Clean this up whenever convenient — it's settled.
- **Still needs you:** The actual *contents* (the field lists) for three or four of those types — thread_operation, draft_da, displacement, and combat_resolved — were *guessed*, not authored by you. The approval note itself flags them as "minimal, assumption-flagged," and the workplan says the item only closes "when Jordan ratifies/edits each." So you still need to look at the inferred field sets, approve or tweak them, and only then flip the "STUB" markers in the registry. This is a small, bounded review, not a big open question.

---

### 3. What you actually still need to decide (a real open call)

**The Knot model: pick one. This is a genuine P1 decision, and it's still owed.**
Two incompatible versions of the Knot system are *both* written into canon right now, and the ledger correctly logs this as open (tracked as P1 item ED-912).

- **The "strain" model** (from ED-773): 2 tiers (Distant / Close), with strain *capacities* of 4 and 7, that break when you hit capacity and ease off over time when relationships are strong.
- **The "tier-cost" model** (from PP-632, currently live in the fieldwork and threadwork params files): 3 tiers (Loose / Medium / Close), with point *costs* of 1 / 2 / 5, a dice roll to form a knot, and a different rupture rule.

These can't both stand — they have different tier names, different numbers of tiers, and their numbers even measure different things (one is "how much strain it can hold," the other is "how much it costs to buy").

**Important correction:** an earlier note implied ED-773 had already *resolved* this. It hasn't — ED-773 is actually *one of the two sides* of the fight. Its "resolved" status only closed an unrelated lifecycle gap, not this model conflict.

Your choices, none of which has been made yet:
- **Option A — Strain model wins** (it's the most recent on the master line, and the adjudicator's recommendation).
- **Option B — Tier-cost model stands** (keep what's currently live in the params files).
- **Option C — Merge the two** into one combined model.

Once you choose, the fieldwork and threadwork files get regenerated to match, and a handful of small internal bugs flagged alongside this decision get fixed (a rupture value that sits below the document's own floor, two references to a section that doesn't exist, and a patch that's cited but missing from the register).

---

## Concrete propagation targets (the file edits implied above)

**Close as stale (articulation layer is canonical):**
- `designs/audit/2026-05-08-character-generation-audit.md:20` — close the flag; cite PP-688 / `references/canonical_sources.yaml` L331-335 + ED-785 (NOT `editorial_ledger_archive_2026_05_02_b.yaml` — keyword match only).
- `designs/articulation/articulation_layer_v30.md` — flip the three contradictory inline banners (L2, L9, L363) from PROVISIONAL to CANONICAL so the false-open stops resurfacing.

**Close as stale (ED-907 ratified 2026-06-20):**
- `designs/audit/2026-06-11-orchestration/valoria_master_workplan_v4.md:31` — strike `ED-907(prov)` from the still-open list (already self-contradicted by line 29 + row #34/line 79).

**Propagate-now half (ED-935 registrations settled):**
- `references/module_contracts.yaml` L130-133, L268, L467, L816 — change `[unreg]` / "NOT in registry" → "registered ED-935"; L446 resolve `scene_outcome.battle_concluded` → `scene.battle_concluded`; regenerate `references/module_map_flat.md` @ 44 types.

**Keep open — real decision (Knot model):**
- `designs/audit/2026-06-10-investigation-exploration-diagnostic/00_MASTER.md:105` — keep open; cross-link to ED-912/ED-841 (do not close as ED-773-resolved).
- One side: `designs/scene/fieldwork_v30.md` §5.6a/§5.6b (strain). Other side: `params/fieldwork.md` §163-172 + `params/threadwork.md` (PP-632 tier-cost).

---

## Appendix — the 18 candidate leads not yet adjudicated (rate-limited)

These were queued but hit transient server rate-limiting. They can be assessed the same way on request:

`PT` / `CI` / `PC` / `IP` abbreviation collisions · `Discipline` name collision · 3-way piety/conviction collision (ED-1006) · `territorial_piety` zero-Key-integration (ED-1006) · ED-673 · ED-676 · ED-717 · ED-874 · ED-936 · ED-937 · ED-970 · PP-665 · PP-674 · Coup-Counter→graduated-autonomy migration (LA-14) · editorial-ledger candidates pending ratification.

> Note on the abbreviation collisions (PT/CI/PC/IP): from the lexicon, these are flagged "ruling
> pending" in canon with **no archived decision resolving them** — so they are almost certainly
> **genuinely open** (real rename calls you owe), not stale. The Decision Register lists them as P1.
