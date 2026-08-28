# SYNTHESIS BRIEF — flatten + within-system analysis (deliverable parts #3 and #4)

You are producing part of a master document for Jordan, the designer of Valoria. Read
`CORRECTIONS.md` in this directory FIRST and apply every correction silently — no findings
section, no "the audit found", no meta-commentary about the process. The corrections are
edits to what you write, not content to report.

Records are in `records/*.md` (11 lane files, YAML blocks). Read the ones your systems appear in.

## Hard constraints

1. **NEVER cite a `path:line` you have not opened yourself.** Six lanes (H1 H2 H3 H4 H8B H9)
   inherited their code citations rather than verifying them. If you want to assert something
   about code, open the file. If you can't, say "design-only" and cite the document instead.
2. **Merge duplicates before you write.** CORRECTIONS.md gives merge keys. A fact found by six
   lanes is ONE fact. Never write "multiple sources confirm" — that is the phantom-corroboration
   trap; they were reading each other.
3. **Do not re-report gaps as a list.** 471 gap records collapse to ~150-190 real ones. A gap is
   only worth a line if it changes what someone would build.
4. **Write for a designer, not an auditor.** Jordan wants to know what his game's systems ARE,
   what they'd DO to play, and where they conflict. Not what a harvest found.

## Your output — exactly two sections per system you own

### §3 FLATTEN — "<system name>"
A compact table of what this system actually consists of, one row per distinct thing, after
dedup. Columns: `thing | slice | what it does | status | where it lives`.
Group the rows: **primitives first, then derivatives/formulae, then mechanics, then processes.**
`status` uses: BUILT (code runs it) · INERT (code exists, nothing calls it) · DESIGNED (prose
only) · RULED-UNEXECUTED (a decision exists, nothing implements it) · PROPOSED (unratified).
Target 25-60 rows. If a system has fewer real things than that, say so — do not pad.

### §4 WITHIN-SYSTEM ANALYSIS — "<system name>"
Four short subsections, prose not bullets, ~150-350 words each:
- **What playing this system is actually like right now.** Be concrete. If nothing runs, say
  what the player would experience: nothing.
- **The load-bearing conflicts.** The contradictions that change what gets built. Rank them.
  For each: what the two sides are, and what decides it (a ruling, the code, or Jordan).
- **What this system needs from others.** Its real read/write dependencies on other systems —
  the fields it reads that another system owns, and who must build them first.
- **The cheapest thing that would make this system playable.** One concrete move. Name the
  smallest change that converts inert machinery into felt play.

Do not write recommendations beyond that last subsection. Do not propose architectures — that
is a later stage's job and duplicating it wastes the reader's time.
