# Gap Detection — Architecture / Key Substrate

**Skill:** valoria-mechanic-audit, Mode D
**Note per skill instructions:** findings here feed the ED-disposition table below; nothing is appended directly to `canon/editorial_ledger*.jsonl` or `references/id_reservations.yaml` by this audit (those are handled by a separate, sequential step in this multi-agent run, per the orchestrator's explicit instruction). No `ED-<LANE>-NNNN` ids are allocated by this document.

## Findings

**GAP-D1 — `awareness` field referenced but undefined (key_substrate_v30.md §4.1 step 7).**
The update-rule pseudocode mutates `cause_key.awareness` for every Key named in `causes[]`, but:
- §2.1's universal Key schema has no `awareness` field.
- No entry in `key_type_registry_v30.md`'s 49 types lists `awareness` as an optional payload field.
- `sim/substrate/keys.py` (the executable oracle) has no `awareness` attribute anywhere in `Key` or `KeyLog`.
- Corpus-wide grep for the literal field found zero consumers.
Partially adjacent to (but not the same as) `propagation_spec_v1.md`'s already-tracked open flag "step-7 awareness-watcher synchronous-emit audit still needed" — that flag is about re-entrancy semantics of a hypothetical watcher, not about the missing schema declaration. Severity: **P2** (does not block current play — nothing depends on reading `awareness`, and the executable oracle simply never runs this branch — but it is a live contradiction between the canonical prose spec and the canonical executable oracle, and any future implementer who *does* wire step 7 literally will hit an undefined attribute).

**GAP-D2 — Accord Domain Echo table malformed by an interposed paragraph (scale_transitions_v30.md §5.5).**
The table's header row and delimiter row are followed by a blank line, then a full paragraph ("Settlement targeting (AUD-SET-02): ..."), and only then do the four actual data rows resume with no blank line separating them from that paragraph. Verified against raw bytes (not an artifact of the Read tool). In strict GFM/CommonMark table parsing this breaks the table: the header+delimiter renders as an empty table, the AUD-SET-02 text renders as its own paragraph, and the four data rows — immediately following a non-table line with no blank line before them — do not attach to any header and likely render as a literal-text paragraph rather than a table. The data itself (the ±1 Accord effects, the "set to 2" transfer rule, the RS−1/Accord−1 violence rule) is fully present in the source text — no information is lost — but the table's *structure* is broken. This is the sole normative table specifying Accord Domain Echo's four outcome→effect mappings. Severity: **P2** (content survives in raw markdown for a text/LLM reader; a rendered-HTML consumer would see a garbled or missing table — no info loss, but real ambiguity/misreading risk for anyone rendering the doc).

**GAP-D3 — §3.3 "Personal → Scene (Contest)" is an empty Handoff Rule (scale_transitions_v30.md).**
Of the Eight Handoff Rules (§3.1–§3.8), §3.3 has a heading and zero body content — no trigger condition, no Ob/roll interaction, no downstream effect. Its siblings §3.4 and §3.6 were once in the same state but were explicitly repaired ("[EDITORIAL: ED-748 — §3.4/§3.6 stub filled with forward-reference]"); §3.3 received no such fix and carries no editorial marker at all, meaning it was never even flagged, let alone resolved. Given §3.3 sits in the *canonical* mode-bridge doc and names one of only eight handoffs the framework claims to define, its absence leaves the Personal→Contest transition entirely unspecified at the architecture layer (Contest's own doc may cover entry conditions, but this doc's own framework promises coverage here and does not deliver it). Severity: **P1** — this is a structural hole in a canonical doc's own named taxonomy, directly comparable to two sibling defects that were already judged serious enough to fix via a dedicated ED (ED-748).

**GAP-D4 — Literal "GM" resolution-actor language uncorrected against the no-GM engine invariant (scale_transitions_v30.md §1, §3.2).**
CLAUDE.md states unambiguously: "There is no GM — the engine resolves everything." Two live passages in the CANONICAL `scale_transitions_v30.md` still describe resolution in terms of a human GM with no engine-equivalent restated:
- §1 Three-Mode Architecture table: TTRPG mode's "Resolution" column reads "Scene-by-scene, player narration, **GM adjudication**."
- §3.2 "Personal → Faction" handoff: "**GM recognises** faction scope. Personal Ob resolves first, then Domain Action Ob."
This is the identical defect class already found and repaired once in the sibling doc `player_agency_v30.md` §4.2 via ED-WR-0007 ("This is a tabletop-GM mechanic... never re-derived for the engine's *no-GM* invariant"), proving this class of finding is considered real and worth fixing, not stylistic. `scale_transitions_v30.md` is the canonical doc that specifically defines what "TTRPG mode" *is* for the engine — an implementer reading §1's mode table in isolation is told the mode's resolution method is "GM adjudication" with no translation to the actual (GM-less) resolver. Severity: **P1** — foundational-table-level contradiction of a top-level architectural premise, in the doc most responsible for defining cross-mode resolution.

**GAP-D5 — Residual "GM use" phrase (player_agency_v30.md §7.1 step 5).**
"At character creation the player may only *indicate* intent for GM use." Same defect class as GAP-D4, in the *same* document that already fixed one instance of it (§4.2, ED-WR-0007) — this second instance was missed by that sweep. Lower stakes than GAP-D4 (administrative character-creation flavor text, not a foundational mode-resolution definition). Severity: **P2**.

**GAP-D6 — §6.1 "TTRPG → BG (Session Boundary)" and §6.3 "Hybrid → TTRPG (Zoom Out)" are empty (scale_transitions_v30.md §6).**
Two of the five "Mode Transition Procedures" subsections have headings and no body content, with no editorial stub-marker (unlike §3.4/§3.6, which got one). §6.2, §6.4, §6.5 (the other three) all have real content. Severity: **P2** — real content gap in a canonical doc, but the surrounding subsections (§6.2 BG→Hybrid, §6.4 Coherence Initialization, §6.5 Hybrid Coherence Cost) partially cover the practical mechanics of crossing these same boundaries, so this is less likely to be a hard blocker than GAP-D3.

**GAP-D7 — §8 "Scope Shift Rules" is entirely empty (scale_transitions_v30.md).**
Heading with zero content, sitting between §7 Sufficient Scope (fully specified) and §9 PC Faction Embedding (fully specified). No editorial stub-marker. Severity: **P2** — could plausibly be dead/orphaned (superseded by §7's own scope-shift consequences) rather than blocking, but nothing in-doc says so; needs a Jordan call on strike-vs-author.

## Already-tracked items (no new action — confirmed still-open via working-tree read, not re-filed)

- `scale_transitions_v30.md` §5.6: "Known gap (ED-IN-0025, 2026-07-07, C-VERIFY-12) — no season-level aggregate ceiling on Domain Echo stacking." Confirmed still present and still open in the working tree. No new finding.
- `player_agency_v30.md` §5.2: succession-contest cross-reference to `faction_politics_v30.md` "SUC-01 through SUC-03" is already flagged in-doc as unverified (`<!-- [flag: section correspondence not verified, ED-IN-0016] -->`). Confirmed still present. No new finding.
- `player_agency_v30.md` §4.3.2 (Rank Advancement row): "debt scene" mechanic already flagged in-doc as undefined, tracked ED-IN-0016 residual / ED-IN-0030. Confirmed still present. No new finding.
- `key_type_registry_v30.md` §9 Type Count Summary: verified by direct count of `### ` headers (49) against the declared total (49) — the ED-IN-0022 reconciliation holds. No discrepancy found; not a gap.
- `key_substrate_v30.md` §11 Vetting Block M-2 rated "○" (partial) — no in-doc gloss on which sub-criterion is partial; plausibly correlated with GAP-D1/D3 above but not confirmed. Not filed as a separate finding (would be speculative).

## Mode B/C cross-references (not re-filed here, see their own files)

- Number System finding F-B1 (`impact_vector`/`symbolic_dimensions` unranged) — see `number_systems_audit.md`.
- Interaction-chain finding on Domain Echo's Key-type carrier — downgraded to a doc-navigability note after tracing `sim/cross_scale/echo_transport.py`; see `mechanic_dependency_graph.md`. Not filed as an ED (mechanism works; only the cross-reference is missing).

---

## ED-Disposition Table

| ID | Type | Description | Location | Severity | Disposition |
|---|---|---|---|---|---|
| GAP-D1 | Referenced-but-undefined mechanic | `awareness` field mutated by the update rule but never declared in schema, registry, or executable oracle | key_substrate_v30.md §4.1 step 7 | P2 | No ED filed by this audit (P2). Recommend a future editorial pass either (a) formally add `awareness: float [0,1]` to the §2.1 schema and wire it into `sim/substrate/keys.py`, or (b) strike step 7 as dead pseudocode pending the propagation_spec re-entrancy audit resolving first. **PROPOSED-ED, lane=IN** if/when actioned — not filed here per P2/no-new-ED-required-for-non-P1 rule. |
| GAP-D2 | Missing/malformed table | Accord Domain Echo table broken by an interposed paragraph between header and data rows | scale_transitions_v30.md §5.5 | P2 | No ED filed by this audit (P2, content preserved, no info loss). Recommend a follow-on editorial pass move the "Settlement targeting (AUD-SET-02)" paragraph to before the table (or after all four data rows) to restore valid GFM table structure. |
| GAP-D3 | Orphaned rule / empty section | §3.3 "Personal → Scene (Contest)" Handoff Rule has no content — no upstream trigger, no downstream effect | scale_transitions_v30.md §3.3 | **P1** | **PROPOSED-ED, lane=IN.** (Alternate lane: `SC` if Jordan judges the missing content belongs to Social Contest's entry-condition spec rather than the architecture mode-bridge doc — flagging both as plausible homes since the content could live in either doc family; IN is the default per this audit's assigned lane and because the *doc structure* defect — a promised-but-empty Handoff Rule in the canonical Eight-Handoff-Rules framework — is itself an architecture-doc issue regardless of where the eventual content is authored.) Not self-resolving; directly comparable to the already-ED-748-fixed §3.4/§3.6 sibling stubs. |
| GAP-D4 | Core-principle contradiction (no-GM invariant) | Literal "GM adjudication" / "GM recognises" language in the canonical mode-bridge doc, uncorrected for the engine's no-GM model | scale_transitions_v30.md §1 (mode table), §3.2 | **P1** | **PROPOSED-ED, lane=IN.** (Alternate/precedent lane: `WR` — the sibling defect in `player_agency_v30.md` §4.2 was fixed under `ED-WR-0007`; either lane is defensible, flagging both since precedent used WR for touching this same doc family.) Recommend the same "re-derive for the no-GM invariant" treatment ED-WR-0007 applied to player_agency §4.2: replace "GM adjudication"/"GM recognises" with the engine-equivalent computed-resolution language (per key_substrate's `on_key_emitted`/observer-armature model, which already implements exactly this rendering role — see core_principles_audit.md P-03). |
| GAP-D5 | Core-principle contradiction (no-GM invariant), residual | "GM use" phrase left over in the same doc that fixed a sibling instance | player_agency_v30.md §7.1 step 5 | P2 | No ED filed by this audit (P2, minor administrative phrasing). Recommend folding into whichever ED resolves GAP-D4, as a one-line sweep of the same defect class in the sibling doc. |
| GAP-D6 | Orphaned rule / empty section | §6.1 "TTRPG → BG (Session Boundary)" and §6.3 "Hybrid → TTRPG (Zoom Out)" have headings, no content | scale_transitions_v30.md §6.1, §6.3 | P2 | No ED filed by this audit (P2 — partially covered by adjacent §6.2/§6.4/§6.5 content). Recommend a future editorial pass either author the missing procedure text or add an explicit forward-reference/strike marker matching the §3.4/§3.6 precedent. |
| GAP-D7 | Orphaned rule / empty section | §8 "Scope Shift Rules" — heading with zero content | scale_transitions_v30.md §8 | P2 | No ED filed by this audit (P2). Needs a Jordan call: author the content, or strike the heading if genuinely superseded by §7 Sufficient Scope. |

**P1 count filed for downstream ED allocation: 2 (GAP-D3, GAP-D4).** Per the skill's Output Rules, both are recorded here as `PROPOSED-ED` with a stated lane recommendation; no `ED-<LANE>-NNNN` id is allocated by this audit — allocation is a separate sequential step in this multi-agent run.
