# Rescued drafts — term ownership (2026-09-16)

**Status: UNRATIFIED DRAFTS. Neither file is wired to anything, and one of them does not do what
its own proposal said it would.** They are here because they were about to be lost with an
ephemeral container, not because they are ready. `proposals/` surfaces unratified work BY LOCATION
(CLAUDE.md §3); that is the whole claim being made.

---

## `key_type_registry.yaml` — ⚠ DOES NOT FIX WHAT IT WAS DRAFTED TO FIX

It was drafted as `references/key_type_registry.yaml`, to close a real and confirmed violation:

> `tools/export_key_types.py:62` reads
> `systems/_architecture/reference/key_type_registry_v30.md`.

That is a `systems/**/*.md` parsed by an exporter, which **CLAUDE.md §0.05 clause 2 forbids in
those words** — *"never an input to a tool, an exporter, a gate or a registry. A design document a
program parses has stopped being reference."* The violation is real and still open.

**This file does not close it.** MEASURED 2026-09-16:

| | strings carrying a baked-in `#` comment |
|---|---|
| this proposal YAML | **199 of 758** |
| shipped `engine/engine_params/key_types.json` | **199 of 760** |

It is a faithful transcription of the `.md`, comment artifacts and all — the same data in a
different file format. Wiring it would **move** the violation, not close it, and would hand the
corruption a second owner on the way. Do not land it as-is.

### What the 199 actually are

Two different things, and only one has a consequence:

1. **~195 are type annotations on payload field names** — `'exchange_count            # int'`,
   `'initiator_id              # actor_id'`. The `#` half is documenting the field's TYPE. The fix
   is a schema change (`{name: exchange_count, type: int}`), not a re-transcription. Nothing
   compares these strings today.

2. **4 are list-valued fields whose comment destroys the list.** These have a runtime consequence
   and are tracked separately:

   ```
   types.mechanical.scene_entered.default_scale_signature
       '[personal, territory, peninsula]   # mirrors scope'
   types.meta.cascade_cluster_event.default_scale_signature
       '[territorial]   # peninsular when abs(similarity) > 0.95 per the trigger-9 spec'
   types.meta.cascade_cluster_event.emitting_systems
   types.meta.cascade_cluster_event.consuming_systems
   ```

   **Observed, not inferred.** Driving `TypeRegistry.apply_defaults` on a Key of type
   `mechanical.scene_entered` yields a `scale_signature` of **50 single characters**
   (`['[', 'p', 'e', 'r', ...]`), and `meta.cascade_cluster_event` yields **79**. Not one member is
   in `SCALES` (`personal, settlement, territory, peninsula`). `keys.py:339` does
   `list(entry["default_scale_signature"])`, and `list()` of a `str` iterates characters.

   Two further defects in the same neighbourhood, both well-formed and still wrong:
   `'[territorial]'` names no scale even parsed correctly (`SCALES` has `territory`), and
   `meta.legacy_event`'s `['system_meta']` is a valid list whose only member is not a scale.

   ⚠ **LATENT, NOT LIVE.** Grepped 2026-09-16: **nothing emits any of these three types.** The data
   is corrupt and would produce garbage if anything did. Reporting it as a live crash would be
   wrong, and an earlier draft of this note did.

---

## `offices_draft.yaml` — original archival work, mostly unlanded

570 rows transcribing Valoria's governance structure across Crown, Hafenmark, Varfell, Church of
Solmund, Löwenritter, Warden of the Thread and the Restoration Movement — each citing
`post / faction / body / ladder / standing / holder_name / case / source / tier`.

Only a 6-row sliver reached the tree (`faction_leaders.by_faction` + `role_templates` in
`engine/season/rosters.yaml`, PR #404). The rest is cross-referenced against four canon documents
and the 46-NPC corpus, so it is **not reproducible by re-running a script** — which is the reason
it is kept rather than dropped.

Its `unsourced:` section records canon defects found during transcription. These are **reports, not
rulings**, and none has been filed as a ledger row:

- **Hafenmark Militia rank ladder** cites *"provisional — see ED-640 below"*, and no ED-640 section
  exists anywhere in the document. A dangling citation.
- **"Cardinal of Justice" has three claimants across three documents** — Olafsson vs. Haelgrund in
  `worldbuilding_v30.md`, `faction_politics_v30.md` and `faction_canon_v30.md`.
- **`faction_politics_v30.md` §3.5 carries post-rename references** (`ED-637` / `ED-638`) that were
  never propagated.

Before any of this is used, it needs verifying against canon by hand — it was transcribed by an
agent and has not been adversarially checked.
