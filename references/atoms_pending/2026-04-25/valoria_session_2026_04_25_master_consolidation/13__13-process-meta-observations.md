---
atom_id: valoria_session_2026_04_25_master_consolidation__13__13-process-meta-observations
source_file: valoria_session_2026_04_25_master_consolidation.md
source_section: "13. Process / Meta Observations"
section_index: 13
total_sections: 15
line_count: 23
char_count: 2313
source_sha256: 4c4672049317ec8e
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## 13. Process / Meta Observations

For future sessions and for general project hygiene:

1. **The amendment-exceeds-foundations pattern is a documentation anti-pattern.** When canon/01 and canon/02 amendments accumulated philosophical content, that content should have been upstreamed into foundations rather than living only in amendments. The audit phase caught this; the rewrite phase fixed it. Future amendments should explicitly upstream their philosophical work to the foundation document at the time of the amendment.

2. **Word-boundary regex is mandatory for term scanning.** Substring matching produces too many false positives (e.g., "Certainty" contains "tain" and shows up in any "taint" search). All term-governance scans must use `\b` boundaries.

3. **TOC vs. body splice hazards.** The first-pass file build for `canon/00_philosophical_foundations.md` used a regex that matched TOC entries when targeting body sections. Positional indexing (counting occurrences of a section header pattern, taking the second one for body) is more robust than regex matching when both TOC and body use the same anchor strings.

4. **The censure registry must distinguish three classes:**
   - **Banned outright** (vocabulary, no replacement needed — e.g., "taint")
   - **Banned, concept obsolete** (mechanic killed, references should be deleted)
   - **Banned, concept needs new name** (rewrite required — e.g., "epistemic seduction" became "drift")

5. **Editorial markers referencing censured terms must use abstract phrasing.** The first attempt at the §16 editorial marker named the censured terms ("Censured terminology removed (Epistemic Seduction, Taint, corruption-as-mechanic)") and re-contaminated the file. Markers should reference "censured terminology" generically with citation to the rectification batch.

6. **Bootstrap session tokens are per-process-invocation.** Each `bash_tool` call is a fresh subprocess and requires re-running `read_files_graphql` to establish a session token. Long multi-step work needs to re-fetch bootstrap context at the start of each script.

7. **Commit message format is enforced.** `[scope] description — PP-NNN / ED-NNN if applicable` with valid scopes: `bugfix, cleanup, compilation, editorial, fix, godot, infrastructure, patch, phase, simulation, skill`.

---
