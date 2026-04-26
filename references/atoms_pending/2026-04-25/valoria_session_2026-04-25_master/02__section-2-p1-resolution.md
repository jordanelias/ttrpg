---
atom_id: valoria_session_2026-04-25_master__02__section-2-p1-resolution
source_file: VALORIA_SESSION_2026-04-25_MASTER.md
source_section: "Section 2 — P1 Resolution"
section_index: 2
total_sections: 11
line_count: 22
char_count: 1812
source_sha256: dedb9b7e51dc8e7b
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## Section 2 — P1 Resolution

Both P1 blockers entering the session were resolved.

### P1-1: Strain trigger inversion (commit `9a16e5d`, ED-743/744)

**Defect:** The strain advancement rule produced inverted dynamics — Treaty pairs increased Strain rather than decreased it, and held-instability did not advance. Pax Romana logic was broken: factions in stable-but-tense alliance experienced no pressure to either consolidate or break, while Treaty signing produced friction.

**Fix:** Strain advances from held-instability (+1 per territory at instability per season, capped +3/season). Treaty-pair decay restored: −1 per Treaty pair, capped −2/season. Net behavior: alliances reduce strain; held instability accumulates pressure. Pax Romana behavior restored.

### P1-2: Reframed via Wager system (commit `7d45753`, ED-739/740/741/742)

**Defect:** Win Condition 3 (WC 3) was reading as a survival floor (lose if below) rather than a budget enabler (capability gate). Late-game players felt squeezed into a single playstyle.

**Fix:** WC 3 reframed as a budget threshold enabling three distinct viable end-game paths via the new Wager system:
- **Arc D Confrontation:** WC ≥ 2 + Scar count ≥ 3 (witnessed) → mandatory Zoom-In with three resolutions (discipline / refuse / escalate).
- **Arc E Wager:** WC ≥ 2 + Scar count ≥ 2 + active Knot + Grand Contest using Projection+Consequence+Solidarity + verifiable future commitment. Resolution by Conviction Track outcome. Wager-pass raises Arc D Scar threshold 3→5 permanently.
- **WC decay clause** (revised stress-test ED-759): ≥2 disruptive ops/season → WC −1 (cap −1/season). Arc D fires only if WC ≥ 1 in prior 4 seasons.
- **ms_budget reframe:** Path 1 (disciplined non-Warden) / Path 2 (WC 3 cooperative) / Path 3 (WC 3 wagered) / Path 4 (trap path).

---
