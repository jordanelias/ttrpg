#!/usr/bin/env python3
"""
tools/observability/build_decisions.py — Valoria open-decision register.

Centralizes the "loose ends": every open ruling, naming collision, unratified
provisional, flagged assumption, and structural gap that is scattered across the
corpus from many sessions — into ONE deduplicated, categorized, prioritized list
so you can see (and clear) the decisions you actually still owe.

Sources:
  - corpus sweep (designs/ canon/ params/ references/ sim/) for explicit markers:
        [OPEN — Jordan] · ruling pending · pending ratification · awaiting ratification
        [GAP …] · F1/F2 class · registry §10 candidate · [ASSUMPTION …]
  - references/module_contracts.yaml  (gap_notes, with affected systems)
  - tools/observability/lexicon.json  (abbreviation collisions, placeholders, censured)
  - canon/supersession_register.yaml  (what's already settled — shown for reassurance)

Output: decisions.json, decisions_data.js (window.VALORIA_DECISIONS), DECISIONS.md
Run:    python tools/observability/build_decisions.py
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    print("PyYAML required", file=sys.stderr); sys.exit(1)

REPO = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

# Redact EVERY legacy name (block- and warn-tier alike, references/names_index.yaml —
# single source of truth per tools/ci_naming_check.py / tools/ci_names_check.py, imported
# here, not re-hardcoded) out of any corpus text this tool quotes verbatim. This register
# aggregates arbitrary corpus lines, including decision/supersession entries that
# legitimately DISCUSS a renamed/forbidden term by name (quoting the exact token, as part
# of explaining the rename or the naming gate itself) — without this, regenerating the
# register can re-introduce a legacy token into decisions.json/DECISIONS.md and trip
# ci_naming_check.py (block-tier) or ci_names_check.py (warn-tier) on the next commit (both
# failed this way in practice, 2026-07-10). This masks the generator's OWN output; it does
# not touch either gate's exclusion list or matching logic — enforce=None pulls every tier
# so a future warn->block promotion needs no change here. MUST be applied to every text
# field this tool writes, not just add()'s corpus-sweep path — the supersession-register
# "resolved" entries below are a second, separate source of quoted corpus text.
def _redact_forbidden_names(text: str) -> str:
    sys.path.insert(0, str(REPO / "tools"))
    try:
        import names as _names
        legacy = _names.all_legacy(enforce=None)
    except Exception:
        return text
    for legacy_name, canon, _key, _tier in legacy:
        text = re.sub(re.escape(legacy_name), f"[REDACTED-LEGACY-NAME, canon={canon}]",
                      text, flags=re.IGNORECASE)
    return text

SWEEP_DIRS = ["designs", "canon", "params", "references", "sim", "engine"]

# ---------------------------------------------------------------------------------------
# Path -> ED-<LANE> lane inference (audit-ecosystem Phase 4 — no ED allocated for this
# tooling change itself; this table informs triage, it does not promote or file anything).
#
# THE single home for this mapping — do not re-derive it elsewhere ("every rule lives
# once", CLAUDE.md §8). Checked for an existing authoritative source first and found none
# usable for the CLAUDE.md §3 9-lane taxonomy (MB/PC/FI/SC/FA/WR/IN/GO/SE):
#   - references/lane_assignments.yaml exists but is a DIFFERENT, older concept (its own
#     header warns against conflating them) — the write-disjoint Lane A/B/C concurrency
#     model, not the ED-<LANE>-NNNN editorial namespace. Its owns-globs are bulk
#     (e.g. Lane A owns the whole of designs/scene/**), too coarse to separate PC/SC/FI.
#   - designs/workplans/valoria_master_workplan_v6.md and workplan_v6_progress.yaml
#     enumerate lane WORK ITEMS, not a path->lane ownership table.
#   - handoffs/HANDOFF_<LANE>.md files each open with a short "canonical head(s)" pointer
#     (e.g. HANDOFF_PC.md -> designs/scene/combat_engine_v1/) — real signal, used below,
#     but only names a handful of files per lane, not a full corpus partition.
#
# So: a minimal prefix table, hand-built from the above signals plus each subsystem's
# obvious subject-matter grouping (sim/ subpackages, params/ files, designs/ subdirs).
# Matched by LONGEST-PREFIX-WINS (a file-specific entry beats its parent directory's).
# Deliberately NOT exhaustive: designs/audit/**, references/** (module_contracts.yaml,
# values_master.yaml, names_index.yaml, npc_registry.yaml, etc.), designs/proposals/**,
# and designs/personal/conviction_*/piety_* are left OUT on purpose — these are
# genuinely cross-lane/shared surfaces (module_contracts.yaml's own gap_notes span all 27
# modules; conviction/piety tracks are drawn on by PC+SC+FI alike; most audit folders are
# investigative snapshots that don't map 1:1 to a single lane). Forcing a guess there would
# violate the "don't force-classify" instruction more than it would help triage. A handful
# of individually-named audit folders ARE included below because a HANDOFF_<LANE>.md file
# explicitly cites them as that lane's own audit trail (not a guess from the folder name).
LANE_PATH_PREFIXES: list[tuple[str, str]] = [
    # --- MB: mass battle ---
    ("designs/provincial/mass_battle_v30", "MB"),
    ("designs/provincial/mass_battle_integration_v30.md", "MB"),
    ("designs/provincial/military_layer_v30", "MB"),
    ("designs/proposals/mass_battle_fighting_withdrawal_v1.md", "MB"),
    ("designs/proposals/multiunit_envelopment_plan.md", "MB"),
    ("params/mass_combat.md", "MB"),
    ("sim/provincial/massbattle.py", "MB"),
    ("sim/provincial/units.py", "MB"),
    ("sim/provincial/tactic_cards.py", "MB"),
    ("sim/provincial/altonian_reinforcements.py", "MB"),
    ("designs/audit/2026-06-30-massbattle-bottomup/", "MB"),
    ("designs/audit/2026-06-01-massbattle-stub-wiring/", "MB"),
    ("designs/audit/2026-05-29-massbattle-sim-foundation/", "MB"),
    ("designs/audit/2026-05-15-mb-comparative-audit/", "MB"),
    ("designs/audit/2026-06-23-mb-fidelity-critique/", "MB"),

    # --- PC: personal combat ---
    ("designs/scene/combat_v30", "PC"),
    ("designs/scene/combat_design_v1", "PC"),
    ("designs/scene/combat_c4_draft_v0.md", "PC"),
    ("designs/scene/combat_engine_v1/", "PC"),
    ("designs/scene/scene_combat_v1/", "PC"),
    # derived_stats_v30 deliberately NOT mapped: it explicitly scopes itself
    # "across personal, unit, settlement, and faction scales" and CLAUDE.md
    # Section 5 flags the derived-stat schema as cross-system "IN FLUX" -- a
    # single-lane assignment would contradict this script's own
    # spans-multiple-lanes -> null policy (caught in adversarial review of
    # Phase 4 / ED-IN-0032's audit-ecosystem plan).
    ("sim/personal/combat.py", "PC"),
    ("designs/audit/2026-06-09-personal-combat-comprehensive/", "PC"),
    ("designs/audit/2026-06-13-combat-bottomup/", "PC"),
    ("designs/audit/2026-06-16-combat-reconciliation/", "PC"),
    ("designs/audit/2026-06-17-combat-decision-docket/", "PC"),
    ("designs/audit/2026-06-19-personal-combat-loose-ends/", "PC"),
    ("designs/audit/2026-06-22-combat-analysis/", "PC"),
    ("designs/audit/2026-06-28-combat-critique/", "PC"),
    ("designs/audit/2026-06-28-combat-critique-recovered.json", "PC"),
    ("designs/audit/2026-06-29-combat-corpus-recovery/", "PC"),
    ("designs/audit/2026-06-30-combat-grounding/", "PC"),
    ("designs/audit/2026-06-30-scene-combat-gate1-audit/", "PC"),
    ("designs/audit/2026-07-04-weapon-morphology-granularity/", "PC"),
    ("designs/audit/2026-06-02-combat-engine/", "PC"),
    ("designs/audit/2026-05-28-combat-reframe/", "PC"),
    ("designs/audit/2026-05-29-combat-armature/", "PC"),
    ("designs/audit/2026-05-31-percell-combat/", "PC"),

    # --- SC: social contest ---
    ("designs/scene/social_contest_v30", "SC"),
    ("designs/scene/social_contest_system_v2", "SC"),
    ("sim/personal/contest/", "SC"),
    ("sim/personal/contest_legacy_stub.py", "SC"),
    ("params/contest.md", "SC"),
    ("params/contest_extensions.md", "SC"),
    ("designs/audit/2026-06-01-contest-redesign/", "SC"),
    ("designs/audit/2026-06-03-contest-groundup/", "SC"),
    ("designs/audit/2026-06-30-contest-stage0-reconciliation/", "SC"),
    ("designs/audit/2026-06-30-contest-fractional-ob-probe/", "SC"),
    ("designs/audit/2026-06-30-contest-gate-1c-packet/", "SC"),
    ("designs/audit/2026-07-01-contest-gate-a-packet/", "SC"),
    ("designs/audit/2026-07-01-contest-gate-b-packet/", "SC"),
    ("designs/audit/2026-07-01-contest-player-interaction/", "SC"),
    ("designs/audit/2026-07-08-pessimist-action-audit/decision_packets/DP-2_SC", "SC"),

    # --- FI: field investigation ---
    ("designs/scene/fieldwork", "FI"),
    ("designs/scene/investigation_systems_v30", "FI"),
    ("designs/personal/knots_v30.md", "FI"),   # module_contracts.yaml: fieldwork_knots -> this doc
    ("sim/personal/fieldwork.py", "FI"),
    ("sim/personal/investigation.py", "FI"),
    ("sim/personal/knots.py", "FI"),
    ("params/fieldwork.md", "FI"),
    ("designs/audit/2026-07-08-pessimist-action-audit/decision_packets/DP-4_FI", "FI"),

    # --- FA: faction actions ---
    ("designs/provincial/faction_", "FA"),
    ("designs/factions/", "FA"),
    ("designs/provincial/ci_political_v30", "FA"),
    ("designs/provincial/baralta_crown_claim_v30", "FA"),
    ("designs/provincial/franchise_v30.md", "FA"),
    ("designs/provincial/parliamentary_transfer_v30.md", "FA"),
    ("designs/provincial/fractional_province_ownership_v30", "FA"),
    ("designs/provincial/fail_forward_pp177.md", "FA"),
    ("designs/provincial/political_dynamics_keys_migration_v30.md", "FA"),
    ("designs/provincial/treaty_expiration_v30.md", "FA"),
    ("designs/provincial/varfell_path_b_v30", "FA"),
    ("designs/audit/2026-04-28-political-dynamics-session/", "FA"),
    ("designs/audit/2026-07-08-pessimist-action-audit/decision_packets/DP-1_FA", "FA"),
    ("sim/provincial/faction_action.py", "FA"),
    ("sim/provincial/parliamentary_action.py", "FA"),
    ("sim/provincial/parliamentary_transfer.py", "FA"),
    ("sim/provincial/treaty.py", "FA"),
    ("sim/provincial/council_solmund.py", "FA"),
    ("sim/provincial/crown_initiative.py", "FA"),
    ("sim/provincial/charter_liberties.py", "FA"),
    ("sim/provincial/absolution.py", "FA"),
    ("sim/provincial/excommunication.py", "FA"),
    ("sim/provincial/hafenmark_equipment.py", "FA"),
    ("sim/provincial/infrastructure_reclamation.py", "FA"),
    ("sim/provincial/mass_seizure.py", "FA"),
    ("sim/provincial/varfell_mandate_action.py", "FA"),
    ("sim/provincial/varfell_territorial_acquisition.py", "FA"),
    ("sim/personal/parliamentary_stay.py", "FA"),
    ("sim/personal/parliamentary_vote.py", "FA"),
    ("params/bg/faction_actions.md", "FA"),
    ("params/bg/parliament.md", "FA"),
    ("params/bg/ministry.md", "FA"),
    ("params/bg/ci_seizure.md", "FA"),
    ("params/bg/royal_assassination.md", "FA"),
    ("params/bg/institutions.md", "FA"),
    ("params/bg/tensions_deck.md", "FA"),
    ("params/factions.md", "FA"),
    ("params/factions_personal.md", "FA"),
    ("params/factions/", "FA"),

    # --- WR: world ---
    ("designs/world/", "WR"),
    ("designs/threadwork/", "WR"),
    ("designs/scene/miraculous_event_v30.md", "WR"),   # sim counterpart lives in sim/world/
    ("params/threadwork.md", "WR"),
    ("params/threadwork_superseded.md", "WR"),
    ("params/southernmost.md", "WR"),
    ("sim/world/", "WR"),
    ("sim/thread/", "WR"),
    ("designs/audit/2026-07-08-pessimist-action-audit/decision_packets/DP-3_WR", "WR"),

    # --- GO: godot ---
    ("designs/godot/", "GO"),
    ("designs/audit/2026-06-10-godot-conversion-strategy/", "GO"),
    ("references/engine_params/", "GO"),

    # --- SE: settlements ---
    ("designs/territory/settlement_layer_v30", "SE"),
    ("designs/territory/settlement_adjacency_v30", "SE"),
    ("designs/territory/territory_temperaments_v30.md", "SE"),
    ("designs/territory/governance_play_redesign_v1.md", "SE"),
    ("designs/territory/march_layer_v30.md", "SE"),
    ("designs/territory/valoria_political_hierarchy_v30.md", "SE"),
    ("designs/territory/valoria_geography_v30.yaml", "SE"),
    ("designs/territory/goldenfurt_slice/", "SE"),
    ("designs/provincial/peninsular_strain_v30", "SE"),
    ("sim/territory/", "SE"),
    ("sim/peninsular/", "SE"),
    ("params/bg/geography.md", "SE"),
    ("designs/audit/2026-06-22-territory-settlement-audit/", "SE"),

    # --- IN: infrastructure / cross-cutting ---
    ("canon/", "IN"),
    ("tools/", "IN"),
    ("engine/", "IN"),
    ("designs/architecture/", "IN"),
    ("designs/articulation/", "IN"),
    ("designs/workplans/", "IN"),
    ("designs/provincial/clock_registry_v30", "IN"),   # timer/scheduling registry, engine_clock-adjacent
    ("references/id_reservations.yaml", "IN"),
    ("references/ci_checks_registry.yaml", "IN"),
    ("references/lane_assignments.yaml", "IN"),
    ("sim/substrate/", "IN"),
    ("sim/autoload/", "IN"),
    ("sim/cross_scale/", "IN"),
]
# Longest-prefix-wins: sort once, most specific first.
_LANE_PREFIXES_SORTED = sorted(LANE_PATH_PREFIXES, key=lambda kv: -len(kv[0]))


LANE_ORDER = ["MB", "PC", "FI", "SC", "FA", "WR", "IN", "GO", "SE"]
LANE_NAMES = {
    "MB": "Mass battle", "PC": "Personal combat", "FI": "Field investigation",
    "SC": "Social contest", "FA": "Faction actions", "WR": "World",
    "IN": "Infrastructure / cross-cutting", "GO": "Godot", "SE": "Settlements",
}


def infer_lane(path_or_loc: str) -> str | None:
    """Infer an ED-<LANE> code from a corpus-relative path (or 'path:line' location
    string). Returns None honestly when nothing in LANE_PATH_PREFIXES matches — no
    force-classification (CLAUDE.md's anti-fabrication ethos)."""
    if not path_or_loc:
        return None
    path = path_or_loc.split(":", 1)[0] if re.search(r":\d+$", path_or_loc) else path_or_loc
    path = path.replace("\\", "/")
    for prefix, lane in _LANE_PREFIXES_SORTED:
        if path.startswith(prefix):
            return lane
    return None

# lines that mention a marker but are ALREADY settled — do not list as open
RESOLVED_SKIP = re.compile(
    r"ratified|RESOLVED|resolved by|resolved\)|\bLANDED\b|superseded by|SUPERSED|STRUCK|"
    r"closed|settled|decided 20|ruling 20|✓|DONE\b|no longer", re.I)

# marker -> (category, priority, plain label).  P1 = genuine decisions you owe.
MARKERS = [
    (re.compile(r"\[OPEN\s*[—\-–]\s*Jordan", re.I), "ruling", 1, "Open ruling (awaiting Jordan)"),
    (re.compile(r"\[OPEN\s*[—\-–]", re.I), "ruling", 1, "Open item"),
    (re.compile(r"rename ruling pending|ruling pending", re.I), "naming", 1, "Ruling pending"),
    (re.compile(r"\bNAME COLLISION\b|name collision", re.I), "naming", 1, "Naming collision"),
    (re.compile(r"pending ratification|awaiting ratification|pending Jordan ratif|Jordan-vetoable|PROVISIONAL pending", re.I), "ratification", 1, "Awaiting ratification"),
    (re.compile(r"\bF2 class\b|F2-class|registry §10 candidate|NOT in registry", re.I), "mechanics", 2, "Unregistered Key (F2 / registry §10)"),
    (re.compile(r"\bF1 class\b|derived-write guard|direct aggregate write", re.I), "mechanics", 2, "Write-protection (F1)"),
    (re.compile(r"missing handoff|out-of-band|no §3 rule defined", re.I), "mechanics", 2, "Missing cross-scale handoff"),
    (re.compile(r"vocabulary unification|attribution conflict", re.I), "naming", 2, "Vocabulary / attribution conflict"),
    (re.compile(r"\[GAP[: \]]", re.I), "gap", 3, "Documented gap"),
    (re.compile(r"\[ASSUMPTION", re.I), "assumption", 3, "Flagged assumption (verify)"),
    (re.compile(r"\[STUB[: \]]|status:\s*stub", re.I), "stub", 3, "Stub / pointer only"),
    (re.compile(r"\bTODO\b|\bFIXME\b", re.I), "todo", 3, "TODO / FIXME"),
]

CATEGORY_LABEL = {
    "ruling": "Open rulings", "naming": "Naming & collisions", "ratification": "Ratifications",
    "mechanics": "Mechanical wiring", "gap": "Documented gaps", "assumption": "Flagged assumptions",
    "stub": "Stubs", "todo": "TODO / FIXME",
}


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())[:200]


def classify(line):
    for pat, cat, prio, label in MARKERS:
        if pat.search(line):
            return cat, prio, label
    return None


def main():
    decisions: dict[str, dict] = {}   # norm-text -> record

    def add(text, cat, prio, label, where, system=""):
        text = _redact_forbidden_names(text.strip())
        if len(text) > 320:
            text = text[:317] + "…"
        k = norm(text)
        if not k:
            return
        rec = decisions.setdefault(k, {"text": text, "category": cat, "priority": prio,
                                       "label": label, "locations": [], "systems": [], "count": 0,
                                       "_lane_votes": set()})
        rec["count"] += 1
        rec["priority"] = min(rec["priority"], prio)
        if where and where not in rec["locations"]:
            rec["locations"].append(where)
        if system and system not in rec["systems"]:
            rec["systems"].append(system)
        rec["_lane_votes"].add(infer_lane(where))

    # ---- 1. corpus sweep ----
    files = 0
    for d in SWEEP_DIRS:
        base = REPO / d
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.suffix.lower() not in (".md", ".yaml", ".yml", ".py") or not p.is_file():
                continue
            files += 1
            rel = str(p.relative_to(REPO)).replace("\\", "/")
            try:
                for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    if "[" not in line and not any(w in line.lower() for w in
                            ("ruling pending", "collision", "ratification", "f2 class", "todo", "fixme")):
                        continue
                    if RESOLVED_SKIP.search(line) and "[OPEN" not in line.upper():
                        continue
                    c = classify(line)
                    if c:
                        cat, prio, label = c
                        add(line.strip().lstrip("#>-* "), cat, prio, label, f"{rel}:{i}")
            except Exception:
                continue

    # ---- 2. module_contracts gap_notes (structured, with systems) ----
    mc = REPO / "references" / "module_contracts.yaml"
    if mc.exists():
        try:
            raw = yaml.safe_load(mc.read_text(encoding="utf-8")) or {}
            for m in raw.get("modules", []):
                sysname = m.get("module", "")
                for note in (m.get("gap_notes") or []):
                    if RESOLVED_SKIP.search(note) and "[OPEN" not in note.upper():
                        continue
                    c = classify(note)
                    if c:
                        cat, prio, label = c
                        add(note, cat, prio, label, "references/module_contracts.yaml", sysname)
                for lp in (m.get("loops") or []):
                    if isinstance(lp, dict) and lp.get("open"):
                        add(f"{sysname}: feedback loop open — damper/cap unconfirmed",
                            "mechanics", 2, "Unannotated feedback loop",
                            "references/module_contracts.yaml", sysname)
        except yaml.YAMLError:
            pass

    # ---- 3. lexicon collisions / placeholders / censured ----
    lex = OUT / "lexicon.json"
    if lex.exists():
        L = json.loads(lex.read_text(encoding="utf-8"))
        for c in L.get("collisions", []):
            add(f"Abbreviation '{c['token']}' collides — owner '{c.get('expands_to','')}'. {c.get('note','')}",
                "naming", 1, "Abbreviation collision (ruling pending)",
                "references/name_collision_database.yaml")
        for ph in L.get("placeholders", []):
            if ph.get("status") != "expired":
                add(f"Placeholder name '{ph.get('placeholder_name','')}' (was '{ph.get('prior_name','')}') — needs canonical name [{ph.get('status','')}]",
                    "naming", 2, "Placeholder name (rename pending)", "canon/placeholder_names.yaml")

    # ---- 4. supersessions (settled — for reassurance / stale-vs-fresh) ----
    resolved = []
    sr = REPO / "canon" / "supersession_register.yaml"
    if sr.exists():
        try:
            raw = yaml.safe_load(sr.read_text(encoding="utf-8")) or {}
            for e in (raw.get("entries") or []):
                if isinstance(e, dict) and e.get("superseded_id"):
                    # A supersession entry's whole POINT is often "old term -> new term",
                    # so this is the source most likely to quote a legacy name verbatim —
                    # redact the same as add()'s corpus-sweep text (see note above).
                    resolved.append({"id": str(e.get("superseded_id")),
                                     "scope": _redact_forbidden_names(str(e.get("scope", ""))),
                                     "superseded_by": str(e.get("superseded_by", "")),
                                     "date": str(e.get("superseded_date") or e.get("date", "")),
                                     "replacement": _redact_forbidden_names(str(e.get("replacement") or "")[:160])})
        except yaml.YAMLError:
            pass

    items = sorted(decisions.values(), key=lambda r: (r["priority"], -len(r["locations"]), r["category"]))

    # ---- finalize per-item lane: one lane if every location agrees, else null ----
    # (mixed non-null votes across an item's locations means it genuinely spans lanes —
    # null is the honest answer there too, not a coin-flip pick of one.)
    for r in items:
        lane_votes = r.pop("_lane_votes", set())
        lane_votes.discard(None)
        r["lane"] = next(iter(lane_votes)) if len(lane_votes) == 1 else None

    by_cat, by_prio, by_file = {}, {1: 0, 2: 0, 3: 0}, {}
    by_lane, by_lane_prio = {}, {}
    for r in items:
        by_cat[r["category"]] = by_cat.get(r["category"], 0) + 1
        by_prio[r["priority"]] = by_prio.get(r["priority"], 0) + 1
        for loc in r["locations"]:
            f = loc.rsplit(":", 1)[0]
            by_file[f] = by_file.get(f, 0) + 1
        ln = r["lane"] or "unassigned"
        by_lane[ln] = by_lane.get(ln, 0) + 1
        by_lane_prio.setdefault(ln, {1: 0, 2: 0, 3: 0})[r["priority"]] += 1
    hotspots = sorted(by_file.items(), key=lambda kv: -kv[1])[:15]

    payload = {
        "meta": {"files_scanned": files, "total_open": len(items),
                 "by_category": by_cat, "by_priority": by_prio,
                 "by_lane": by_lane, "by_lane_priority": by_lane_prio,
                 "hotspots": hotspots, "resolved_count": len(resolved)},
        "decisions": items, "resolved": resolved[:200],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "decisions.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (OUT / "decisions_data.js").write_text(
        "// AUTO-GENERATED — do not hand-edit.\nwindow.VALORIA_DECISIONS = "
        + json.dumps(payload, separators=(",", ":")) + ";\n", encoding="utf-8")

    # ---- DECISIONS.md (the readable register) ----
    md = []
    md.append("# Valoria — Open Decision Register\n")
    md.append("> Auto-generated by `tools/observability/build_decisions.py`. The scattered "
              "loose ends from every session, deduplicated and prioritized into one list.\n")
    md.append(f"**{len(items)} open items** across {files} files "
              f"· P1 {by_prio.get(1,0)} · P2 {by_prio.get(2,0)} · P3 {by_prio.get(3,0)} "
              f"· {len(resolved)} already settled (supersessions).\n")

    md.append("\n## By lane\n")
    md.append("_Inferred from file path via the `LANE_PATH_PREFIXES` table in this script — "
              "informs lane-scoped triage, does not auto-file anything. An item with "
              "locations in more than one lane, or no matching path prefix at all, lands "
              "in **unassigned** rather than a forced guess._\n")
    md.append("| Lane | P1 | P2 | P3 | Total |")
    md.append("|---|---|---|---|---|")
    for lane in LANE_ORDER:
        p = by_lane_prio.get(lane, {1: 0, 2: 0, 3: 0})
        total = by_lane.get(lane, 0)
        if total == 0:
            continue
        md.append(f"| **{lane}** — {LANE_NAMES[lane]} | {p.get(1,0)} | {p.get(2,0)} | {p.get(3,0)} | {total} |")
    up = by_lane_prio.get("unassigned", {1: 0, 2: 0, 3: 0})
    md.append(f"| _unassigned_ (`lane: null`) | {up.get(1,0)} | {up.get(2,0)} | {up.get(3,0)} | {by_lane.get('unassigned',0)} |")

    md.append("\n## By category\n")
    for cat, n in sorted(by_cat.items(), key=lambda kv: -kv[1]):
        md.append(f"- **{CATEGORY_LABEL.get(cat,cat)}** — {n}")
    md.append("\n## Hotspot files (where the loose ends cluster)\n")
    for f, n in hotspots:
        md.append(f"- `{f}` — {n}")

    # 2026-07-09 (token-efficiency pass): was 60. DECISIONS.md is a human-skimmable
    # summary — decisions.json (unchanged, uncapped) is the complete machine-readable
    # source both console.html and any programmatic consumer actually read. At 60,
    # DECISIONS.md had grown to ~59k tokens (4x its own atomization_rules.yaml cap)
    # without adding real coverage, since nothing reads the .md for completeness.
    PER_CAT_CAP = 12

    def section(title, prio):
        rows = [r for r in items if r["priority"] == prio]
        if not rows:
            return
        md.append(f"\n---\n\n## {title}  ({len(rows)})\n")
        cur = None
        shown = 0
        for r in rows:
            if r["category"] != cur:
                cur = r["category"]
                catrows = [x for x in rows if x["category"] == cur]
                md.append(f"\n### {CATEGORY_LABEL.get(cur,cur)} ({len(catrows)})\n")
                shown = 0
            if shown >= PER_CAT_CAP:
                if shown == PER_CAT_CAP:
                    md.append(f"- _…and more in this category — see `decisions.json`._")
                    shown += 1
                continue
            sysnote = f" _(systems: {', '.join(r['systems'])})_" if r["systems"] else ""
            loc = r["locations"][0] if r["locations"] else ""
            more = f" +{len(r['locations'])-1} more" if len(r["locations"]) > 1 else ""
            md.append(f"- {r['text']}{sysnote}  \n  ↳ `{loc}`{more}")
            shown += 1
    section("P1 — decide first (the real rulings you owe)", 1)
    section("P2 — decide soon (structural & naming)", 2)
    # P3 = hygiene tail — summarize, don't enumerate
    p3 = [r for r in items if r["priority"] == 3]
    if p3:
        md.append(f"\n---\n\n## P3 — cleanup backlog ({len(p3)})  — summarized\n")
        md.append("_Flagged assumptions, documented gaps, stubs, and TODOs. Not decisions per se — "
                  "verification/hygiene work. Full list in `decisions.json`._\n")
        p3cat = {}
        for r in p3:
            p3cat[r["category"]] = p3cat.get(r["category"], 0) + 1
        for c, n in sorted(p3cat.items(), key=lambda kv: -kv[1]):
            md.append(f"- **{CATEGORY_LABEL.get(c,c)}** — {n}")
    md.append("\n---\n\n## Already settled (recent supersessions)\n")
    md.append("_These are NOT open — shown so stale references don't read as live decisions "
              "(your “stale vs fresh” problem). Before treating any old ED/PP as authoritative, "
              "check `canon/supersession_register.yaml`._\n")
    for r in resolved[:40]:
        md.append(f"- **{r.get('id','')}** — {r.get('scope','')[:120]} → _{r.get('replacement','') or r.get('superseded_by','')}_")
    (OUT / "DECISIONS.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print("Valoria decision register built:")
    print(f"  open={len(items)}  (P1={by_prio.get(1,0)} P2={by_prio.get(2,0)} P3={by_prio.get(3,0)})"
          f"  resolved={len(resolved)}  files_scanned={files}")
    print(f"  by category: {by_cat}")
    print(f"  -> {OUT/'DECISIONS.md'}  /  decisions.json  /  decisions_data.js")
    return payload


if __name__ == "__main__":
    main()
