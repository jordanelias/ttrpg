# npc_registry — history

Companion to `references/npc_registry.yaml`. **That file is the REGISTRY (46 named characters); this one is HISTORY.**

## Why the split (B-X extraction, 2026-10-06)

Jordan, 2026-10-06: *"you can extract all edit histories/discussion from .yaml files in references and
just make those a supplement."* The precedent is `references/id_reservations_history.md`.

**Nothing was deleted.** Every block below is the verbatim text that sat in `npc_registry.yaml` at
commit `8b57336`, moved rather than rewritten. Headings follow the YAML's own order: the file head,
then the per-entry migration/conviction rationale (one section per character, by `id`), then inline
provenance comments, then the trailing REMOVED/MERGED and OPEN ISSUES blocks.

**What moved, and why those keys.** The per-entry keys `migration_notes` (the PP-685 §4 legacy-label
migration: *"Legacy X -> Y"*, *"No prior legacy label. Inferred from role"*, *"Direct mapping"*) and
`conviction_notes` (why a weight was assigned, archetype and ruling attributions) are provenance and
rationale for the `convictions:` block. They are NOT in the file's `schema:` and no reader reads them:
`engine/season/data/cast.py` reads `id`, `first_name`, `last_name`, `faction`, `title` and the
`convictions` lists only (a non-list sibling under `convictions:` is skipped explicitly), and nothing
else in `engine/`, `tools/`, `tests/` or `skills/` reads either key. Removing them changes the parsed
data in exactly those 26 keys (18 `migration_notes`, 8 `conviction_notes`) and nothing else.

**What stayed behind, deliberately:** the `schema:` block; every `notes:` key (a declared optional
field, and it carries character facts such as TS and card identity, not only history); the
`[GAP]` / `[ASSUMPTION]` flags; the `status: canonical  # verified ... (ED-634 naming pending)` flags
(`engine/season/cases/NPC4.yaml` quotes "ED-634 naming pending" as a live status); section headers;
and a two-line summary of the open items.

**Two live pointers into this history, outside this file's lane.** `engine/season/rosters.yaml`
(the comment near its line 68) says the Holdar `Continuity` -> `Warden` migration is "documented in
the registry's own rows", and `engine/season/cases/NPC4.yaml` (`why:` text near lines 370 and 495)
cites "her migration_notes" / "migration_notes ... Templar arm". Those rows now live in the
per-entry sections below.

**Adding here, not there.** New migration rationale, rulings and dated narrative belong in this
file; the YAML row should carry the data. Per-character provenance for a new `convictions:` block
goes under that character's `id` heading below.

## File head: last-updated and status lines

*(HEAD `8b57336`, lines 8-9 — verbatim.)*

```text
# Last updated: 2026-05-08
# Status: ACTIVE — legacy labels migrated per PP-685; stats still deferred per npc_roster_v30
```

## inline comment on line 23

*(HEAD `8b57336`, line 23 — verbatim.)*

```text
  # mononym; "Edeyja" confirmed final per Jordan 2026-05-08
```

## inline comment on line 36

*(HEAD `8b57336`, line 36 — verbatim.)*

```text
  # "moderate" per edeyja_npc.md
```

## NPC-001 Edeyja — `migration_notes`

*(HEAD `8b57336`, line 43 — verbatim.)*

```text
      migration_notes: "Legacy 'Continuity' → Warden (stewardship duty: 'the work must continue') + Precedent (ancestral practice). Per PP-685 §4 defaults."
```

## NPC-002 Maret Uln — `conviction_notes`

*(HEAD `8b57336`, line 68 — verbatim.)*

```text
      conviction_notes: "Restoration-aligned per Jordan 2026-05-08."
```

## NPC-003 Yrsa Vossen — `conviction_notes`

*(HEAD `8b57336`, line 92 — verbatim.)*

```text
      conviction_notes: "Equity primary per behavior_v30 §RM: 'The community is the only legitimate political unit.' Secondary: Continuity → Warden (cultural preservation fallback). PP-685 mapping (Honor/Warden/Community) superseded by behavior file. Rosa Luxemburg archetype — visibility as vulnerability."
```

## inline comment on line 107

*(HEAD `8b57336`, line 107 — verbatim.)*

```text
  # per Jordan; latent Thread perception
```

## NPC-004 Sæmund Haelgrund — `conviction_notes`

*(HEAD `8b57336`, line 116 — verbatim.)*

```text
      conviction_notes: "Field Inquisitor, NOT a Cardinal. Cardinal Justice = Arnlod Olafsson (NPC-038). Savonarola archetype."
```

## inline comment on line 131

*(HEAD `8b57336`, line 131 — verbatim.)*

```text
  # per npc_roster_v30 §5 'TS 35'; behavior_v30 table says '20+' (floor, not ceiling)
```

## NPC-005 Sigrid Torsvald — `migration_notes`

*(HEAD `8b57336`, line 140 — verbatim.)*

```text
      migration_notes: "Legacy 'Consequentialist' → Utility. Honor added via lowenritter_military cultural template. Per PP-685 §4 defaults."
```

## inline comment on line 152

*(HEAD `8b57336`, line 152 — verbatim.)*

```text
  # confirmed intentional — named after birthplace
```

## NPC-006 Halvar Brandt — `migration_notes`

*(HEAD `8b57336`, line 163 — verbatim.)*

```text
      migration_notes: "No prior legacy label. Inferred from role: military officer = Honor + Authority. Per PP-685 §4 defaults."
```

## NPC-007 Annika Feldhaus — `migration_notes`

*(HEAD `8b57336`, line 187 — verbatim.)*

```text
      migration_notes: "Legacy 'Utilitarian' → Utility. npc_roster_v30: 'Utilitarian — greatest good for greatest number of guild members'. Self-Other mildly self-interested (PROFIT-MAXIMISING flaw). Per PP-685 §4."
```

## NPC-008 Peder Almstedt — `migration_notes`

*(HEAD `8b57336`, line 210 — verbatim.)*

```text
      migration_notes: "No prior legacy label. Inferred from role: bureaucrat / CONSERVATIVE behavioral AI = Order + Precedent. Per PP-685 §4."
```

## NPC-009 Gerik Strand — `migration_notes`

*(HEAD `8b57336`, line 233 — verbatim.)*

```text
      migration_notes: "No prior legacy label. Inferred from role: competent administrator, OVERPERFORMER flaw, flattery vulnerability. Authority + Utility. Per PP-685 §4."
```

## NPC-010 Dalla Virke — `migration_notes`

*(HEAD `8b57336`, line 256 — verbatim.)*

```text
      migration_notes: "No prior legacy label. npc_roster_v30: 'Honour among operators — your word is your network.' Utility (effectiveness) + Honor (personal trust, word-as-bond). Per PP-685 §4."
```

## NPC-011 Alexios Laskaris — `conviction_notes`

*(HEAD `8b57336`, line 280 — verbatim.)*

```text
      conviction_notes: "Virtue primary per Jordan 2026-05-08. Byzantine philosopher-ruler tradition. Periodic visitor with Elske."
```

## NPC-012 Rikard Solberg — `migration_notes`

*(HEAD `8b57336`, line 303 — verbatim.)*

```text
      migration_notes: "No prior legacy label. Inferred from role: STABILITY-SEEKING trade factor. Utility (trade pragmatism) + Order (stability). Per PP-685 §4."
```

## NPC-013 Aldric Tormann — `migration_notes`

*(HEAD `8b57336`, line 326 — verbatim.)*

```text
      migration_notes: "No prior legacy label. Inferred from role: OPTIMISER (maximises Church Wealth throughput), aggressive tithe = Faith + Order + Utility. Per PP-685 §4."
```

## inline comment on line 345

*(HEAD `8b57336`, line 345 — verbatim.)*

```text
  # per character_canon_v30: "Almud (TS 28, no threshold crossing)"
```

## NPC-020 Almud Almqvist — `migration_notes`

*(HEAD `8b57336`, line 354 — verbatim.)*

```text
      migration_notes: "Per PP-685 §2.1. Prior labels 'Virtue Ethics' + 'Reason'. Public-spirited Captain archetype."
```

## NPC-021 Arne Himlensendt — `migration_notes`

*(HEAD `8b57336`, line 379 — verbatim.)*

```text
      migration_notes: "No prior legacy label. Inferred from role: Church leader / Confessor. Per PP-685 §4 defaults."
```

## inline comment on line 399

*(HEAD `8b57336`, line 399 — verbatim.)*

```text
  # per behavior_v30 TS/certainty table
```

## inline comment on line 401

*(HEAD `8b57336`, line 401 — verbatim.)*

```text
  # per behavior_v30: 'Truth disrupted by hostage status and competing loyalties'
```

## NPC-032 Lenneth Almqvist — `conviction_notes`

*(HEAD `8b57336`, line 448 — verbatim.)*

```text
      conviction_notes: "Equity + Liberty. Caste suppression is wrong (Equity), political self-determination follows (Liberty). Archivist by training. Pro-Restoration. Queen Jadwiga of Poland archetype."
```

## NPC-033 Kolbrun Thale — `migration_notes`

*(HEAD `8b57336`, line 472 — verbatim.)*

```text
      migration_notes: "faction_canon: 'Autonomy / Consequence MS / Truth 3'. Autonomy → Liberty; Consequence → Utility. Per PP-685 §4."
```

## NPC-034 Gustav Linder — `migration_notes`

*(HEAD `8b57336`, line 496 — verbatim.)*

```text
      migration_notes: "faction_canon: 'Faith / Authority MS / Truth 5'. Direct mapping. Per PP-685 §4."
```

## NPC-035 Theodor Kreutz — `migration_notes`

*(HEAD `8b57336`, line 519 — verbatim.)*

```text
      migration_notes: "faction_canon: 'Order / Authority MS / Truth 4'. Direct mapping. Per PP-685 §4."
```

## NPC-036 Wilhelm Voss — `migration_notes`

*(HEAD `8b57336`, line 542 — verbatim.)*

```text
      migration_notes: "faction_canon: 'Order / Authority MS / Truth 4'. Direct mapping. Per PP-685 §4."
```

## inline comment on line 550

*(HEAD `8b57336`, line 550 — verbatim.)*

```text
  # CORRECTED: was listed as Church/Cardinal — actually Crown Lord Treasurer per faction_canon
```

## NPC-037 Annalie Reichard — `migration_notes`

*(HEAD `8b57336`, line 565 — verbatim.)*

```text
      migration_notes: "faction_canon: 'Precedent / Evidence MS / Truth 5'. Direct mapping on Precedent; Evidence is Resonant Style. Per PP-685 §4."
```

## inline comment on line 579

*(HEAD `8b57336`, line 579 — verbatim.)*

```text
  # FILLED: per faction_canon "Cardinal Arnlod Olafsson"
```

## NPC-038 Arnlod Olafsson — `conviction_notes`

*(HEAD `8b57336`, line 595 — verbatim.)*

```text
      conviction_notes: "Cardinal Justice. Per Jordan."
```

## inline comment on line 603

*(HEAD `8b57336`, line 603 — verbatim.)*

```text
  # FILLED: per faction_canon "Cardinal Magnus Klapp"
```

## NPC-039 Magnus Klapp — `migration_notes`

*(HEAD `8b57336`, line 619 — verbatim.)*

```text
      migration_notes: "No prior legacy label. faction_canon: 'canonical scholar'. Scholastic + Faith inferred. Per PP-685 §4."
```

## inline comment on line 627

*(HEAD `8b57336`, line 627 — verbatim.)*

```text
  # FILLED: per faction_canon "Cardinal Osten Jarnstal"
```

## NPC-040 Osten Jarnstal — `migration_notes`

*(HEAD `8b57336`, line 643 — verbatim.)*

```text
      migration_notes: "No prior legacy label. faction_canon: 'Templar arm' for Fortitude cardinal → Honor (military-religious code) + Faith + Authority. Per PP-685 §4."
```

## inline comment on line 657

*(HEAD `8b57336`, line 657 — verbatim.)*

```text
  # RESOLVED: distinct from NPC-013 Aldric Tormann per faction_canon §11
```

## NPC-050 Inge Baralta — `conviction_notes`

*(HEAD `8b57336`, line 690 — verbatim.)*

```text
      conviction_notes: "Precedent primary per behavior_v30 §2.3: 'Constitutional procedure IS justice.' PP-685 §2.3 misattributed as Faith/ecclesiastical — character_canon D6 already flagged this. Maria Theresa archetype — Habsburg empress defending inherited sovereign authority through institutional competence. Unshakeable force of conviction."
```

## inline comment on line 701

*(HEAD `8b57336`, line 701 — verbatim.)*

```text
  # RESOLVED: confirmed as Varfell faction leader per faction_canon
```

## NPC-052 Magnus Vaynard — `conviction_notes`

*(HEAD `8b57336`, line 714 — verbatim.)*

```text
      conviction_notes: "Reinhardt von Lohengramm archetype — revolutionary aristocrat. Genuine Einhir revival idealism (Equity) fused with any-cost pragmatism (Utility). Self/Other −0.40: ego-driven, wants to be the one who tears down the order and replaces it. PP-685 §3 mapping (Authority/Honor/Identity) superseded per Jordan 2026-05-08."
```

## Trailing blocks: REMOVED / MERGED ENTRIES and OPEN ISSUES — UPDATED

*(HEAD `8b57336`, lines 983-1063 — verbatim.)*

```text
# ═══════════════════════════════════════════════════════════════
# REMOVED / MERGED ENTRIES
# ═══════════════════════════════════════════════════════════════
#
# NPC-051 (Klapp): MERGED into NPC-039 (Cardinal Magnus Klapp).
#   "Klapp Combat", "Klapp Thread", etc. are arc/mechanic references
#   to Cardinal Klapp's surname, not a separate character.
#
# NPC-053 (Olafsson): MERGED into NPC-038 (Cardinal Arnlod Olafsson).
#   "Olafsson Grievance" is an arc reference to Cardinal Olafsson's
#   surname, not a separate character.

# ═══════════════════════════════════════════════════════════════
# OPEN ISSUES — UPDATED
# ═══════════════════════════════════════════════════════════════
#
# 1. [RESOLVED] LEGACY ETHICAL LABELS migrated to 13-Conviction
#    taxonomy per PP-685. All deprecated ethics_legacy fields removed.
#
# 2. [RESOLVED] EDEYJA NAME: "Edeyja" confirmed final per Jordan 2026-05-08.
#    Mononym (no surname).
#
# 3. [RESOLVED] HALVAR / HALVARDSHELM: Confirmed intentional — Halvar is
#    from Halvardshelm. Birthplace filled. Per Jordan 2026-05-08.
#
# 4. [RESOLVED] TWO ALDRICS: NPC-013 Aldric Tormann (Church, Cardinal
#    Prudence) and NPC-041 Aldric Hann (RM visible leadership) are
#    DISTINCT characters. Different factions, different surnames.
#    Per faction_canon_v30 §11.
#
# 5. [PARTIALLY RESOLVED] UNLISTED NPCS: Crown Inner Circle (5 NPCs)
#    and Church Cardinals confirmed as active named NPCs per
#    faction_canon_v30 / ED-634. Remaining gaps: character_canon
#    entries still pending for most.
#
# 6. [RESOLVED] VAYNARD: Confirmed as Varfell faction leader per
#    faction_canon_v30. Military-order doctrine. Surname unknown.
#
# 7. [OPEN] STAT GAPS: Explicitly deferred per npc_roster_v30
#    ("Deferred to next session"). Most NPCs beyond Edeyja lack
#    full stat blocks. Cannot resolve without design authoring session.
#
# 8. [RESOLVED] CONVICTION MIGRATION: All NPCs with legacy labels
#    mapped to 13-Conviction vectors. NPCs without prior labels
#    assigned inferred Convictions per PP-685 §4 with [ASSUMPTION] flags.
#
# NEW ISSUES:
#
# 9. [OPEN] CARDINAL REICHARD COLLISION: PP-685 §2.3 references a
#    "Cardinal Reichard" in the ecclesiastical faction. NPC-037
#    Annalie Reichard is Crown Inner Circle Lord Treasurer per
#    faction_canon. Are these the same person or distinct?
#
# 10. [RESOLVED] LENNETH: One character — Queen Lenneth Almqvist.
#     Pro-Restoration, allied with Yrsa Vossen. PP-685 §2.3
#     ecclesiastical profile (Scholastic/Faith/Precedent) is a
#     MISATTRIBUTION — needs correction in PP-685. Conviction vector
#     needs authoring per actual RM alignment. Per Jordan 2026-05-08.
#
# 11. [OPEN] CARDINAL ARNLOD — VIRTUE ASSIGNMENT: Four cardinal
#     virtues (Justice, Temperance, Fortitude, Prudence) mapped to
#     four cardinals. Arnlod Olafsson has no virtue assignment.
#     Fifth cardinal, or does he hold one of the four?
#
# 12. [RESOLVED] CONVICTION DISCREPANCIES: behavior_v30 authoritative
#     over PP-685 for conviction assignments. Baralta → Precedent
#     (was Faith), Vaynard → Equity/Utility (was Authority/Honor/
#     Identity), Vossen → Equity (was Honor/Warden/Community),
#     Hann → Equity/Liberty (was null). Per audit + Jordan 2026-05-08.
#
# 13. [RESOLVED] BARALTA NAME + FACTION: Inge Baralta, Duchess of
#     Hafenmark. Was mislabeled "Crown claimant" with no first name.
#     character_canon D6 already flagged the PP-685 misattribution.
#     Catherine the Great archetype per Jordan.
#
# 14. [RESOLVED] VAYNARD NAME: Magnus Vaynard, Duke. Reinhardt von
#     Lohengramm archetype. Equity/Utility, self/other −0.40.
#
# 15. [RESOLVED] LENNETH CONVICTION: Equity primary. Archivist by
#     training. Pro-Restoration institutional revivalist.
#
```
