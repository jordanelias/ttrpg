#!/usr/bin/env python3
"""
tools/build_apparatus_registry.py — Valoria apparatus inventory (generated).

Answers, for EVERY skill, tool, hook and script: what does it read, what does it
write and in what format, who invokes it, and is it orphaned? This is the "output
destination + format" inventory (Jordan's ask, 2026-07-15) — regenerated from
static analysis rather than hand-maintained, so it can't rot (the same anti-stale
posture as tools/observability/build_decisions.py and the CLAUDE.md §8 invariant).

It is a consolidating VIEW over the working tree, not an 8th scanner: it detects
reads/writes by AST, resolves module-level path constants best-effort, and infers
each apparatus's role in the dataflow (Layer 0 source / Layer 2 generator /
Layer 3 surface / import-only library / CI gate).

Output: references/apparatus_registry.yaml (machine) + references/apparatus_registry.md (human)
Run:    python3 tools/build_apparatus_registry.py
"""
from __future__ import annotations
import argparse, ast, json, re, sys
from pathlib import Path

# repo root: ONE OWNER, tools/ci_common.py (plan G7). This module already
# bootstraps ci_common below; the assignment is re-stated after that import.
REPO = None  # set from ci_common.REPO immediately after the bootstrap below

# Single-owner __main__-guard predicate (OI-52a, ED-IN-0097, 2026-07-29-code-shape-open-items
# plan §3 Wave 4 item 2). Was a local regex over raw source text (`re.search(r'if\s+__name__...`)
# that only matched the conventional operand order and, being text- not AST-based, false-positived
# on a comment or string literal merely containing the guard text — see
# tests/valoria/test_ci_common.py for the planted-regression case. `structure_audit.py`
# (skills/valoria-vector-audit/scripts/) adopts the same owner this wave (join lane); both consumers
# now resolve to the one function in tools/ci_common.py, never a second definition.
try:
    import ci_common
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import ci_common

REPO = Path(ci_common.REPO)

# ------------------------------------------------------------------ enumeration
def _iter_tool_scripts() -> list[Path]:
    return sorted(p for p in (REPO / "tools").rglob("*.py")
                  if "__pycache__" not in p.parts)

def _iter_skill_scripts() -> list[Path]:
    return sorted(p for p in (REPO / "skills").rglob("*.py")
                  if "__pycache__" not in p.parts)

def _skill_dirs() -> list[Path]:
    return sorted(d for d in (REPO / "skills").iterdir()
                  if d.is_dir() and (d / "SKILL.md").exists())

def _workflows() -> list[Path]:
    """CI workflows only — GitHub Actions YAML."""
    wf = REPO / ".github" / "workflows"
    return sorted(wf.glob("*.yml")) if wf.exists() else []


def _claude_workflows() -> list[Path]:
    """Claude Code Workflow scripts in `.claude/` — a DIFFERENT thing from CI workflows.

    ED-IN-0087 (finding: ED-IN-0085). The word "workflow" is overloaded in this repo, and the
    registry inherited only one meaning: `_workflows()` resolves to `.github/workflows`, so the
    `.claude/wf_*.js` orchestration scripts — which encode the repo's own audit method — were
    invisible to the very inventory that exists to flag orphaned apparatus. They are listed here
    under a distinct `claude-workflow` kind rather than folded into `_workflows()`, because their
    invoker, artifacts, and failure modes are all different: CI workflows are triggered by
    github-actions and emit ci-status; these are invoked by hand in a session and emit audit docs.
    """
    d = REPO / ".claude"
    return sorted(d.glob("wf_*.js")) if d.exists() else []

# ------------------------------------------------------------- AST write/read/scan
_WRITE_DUMP = {"dump", "safe_dump"}          # json.dump / yaml.dump / yaml.safe_dump
_EXT_FORMAT = {".json": "json", ".jsonl": "jsonl", ".md": "markdown",
               ".yaml": "yaml", ".yml": "yaml", ".js": "js", ".html": "html",
               ".csv": "csv", ".txt": "text", ".mermaid": "mermaid"}

def _const_strings(tree: ast.Module) -> dict[str, str]:
    """Module-level NAME -> string literal (best-effort, for path-var resolution)."""
    out: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            v = node.value
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                out[node.targets[0].id] = v.value
            # Path(...) / X / "literal"  — grab the trailing literal segment
            elif isinstance(v, ast.BinOp) and isinstance(v.right, ast.Constant) \
                    and isinstance(v.right.value, str):
                out[node.targets[0].id] = v.right.value
    return out

def _target_repr(node: ast.AST, consts: dict[str, str]) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return consts.get(node.id, f"<{node.id}>")
    if isinstance(node, ast.Attribute):        # args.out, self.path
        return f"<{node.attr}>"
    if isinstance(node, ast.JoinedStr):        # f-strings
        return "<f-string>"
    if isinstance(node, ast.BinOp):
        r = _target_repr(node.right, consts)
        return r
    if isinstance(node, ast.Call):             # OUT / "x.json"  via Path()/join
        for a in reversed(node.args):
            r = _target_repr(a, consts)
            if r:
                return r
    return None

def _fmt_for(dest: str | None) -> str:
    if not dest:
        return "unknown"
    for ext, f in _EXT_FORMAT.items():
        if dest.endswith(ext):
            return f
    return "unknown"

def analyze_py(path: Path) -> dict:
    src = path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {"error": "syntax", "writes": [], "reads_imports": [],
                "has_main": False, "prints": False, "uses_cli": False}
    consts = _const_strings(tree)
    writes: list[dict] = []
    prints = False
    has_main = ci_common.has_main_guard(tree)
    imports: set[str] = set()

    for node in ast.walk(tree):
        # imports (for dependency + read signal)
        if isinstance(node, ast.Import):
            for n in node.names:
                imports.add(n.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
        # calls
        elif isinstance(node, ast.Call):
            fn = node.func
            # open(target, 'w'|'a')
            if isinstance(fn, ast.Name) and fn.id == "open":
                mode = ""
                if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(m in mode for m in ("w", "a")):
                    dest = _target_repr(node.args[0], consts) if node.args else None
                    writes.append({"dest": dest, "format": _fmt_for(dest),
                                   "mode": "append" if "a" in mode else "write"})
            elif isinstance(fn, ast.Attribute):
                # .write_text(  / .write(
                if fn.attr in ("write_text",):
                    dest = _target_repr(fn.value, consts)
                    writes.append({"dest": dest, "format": _fmt_for(dest), "mode": "write"})
                # json.dump( / yaml.dump( / yaml.safe_dump(  -> format hint (dest from nearby open)
                elif fn.attr in _WRITE_DUMP:
                    base = fn.value.id if isinstance(fn.value, ast.Name) else ""
                    fmt = "json" if base == "json" else ("yaml" if base in ("yaml",) else "unknown")
                    writes.append({"dest": "<stream>", "format": fmt, "mode": "write"})
                elif fn.attr == "print":
                    prints = True
            if isinstance(fn, ast.Name) and fn.id == "print":
                prints = True

    # collapse duplicate write dests
    seen, uniq = set(), []
    for w in writes:
        k = (w["dest"], w["format"], w["mode"])
        if k not in seen:
            seen.add(k); uniq.append(w)
    uses_cli = ("argparse" in imports) or ("sys.argv" in src) or ("ArgumentParser" in src)
    return {"writes": uniq, "reads_imports": sorted(imports),
            "has_main": has_main, "prints": prints, "uses_cli": uses_cli}

# --------------------------------------------------------------- invocation graph
def _text_index() -> str:
    """Concatenate every invoker surface once (workflows, hooks, settings, SKILL.md)."""
    parts = []
    for wf in _workflows():
        parts.append(wf.read_text(encoding="utf-8", errors="replace"))
    for hk in (REPO / ".githooks").glob("*"):
        if hk.is_file():
            parts.append(hk.read_text(encoding="utf-8", errors="replace"))
    settings = REPO / ".claude" / "settings.json"
    if settings.exists():
        parts.append(settings.read_text(encoding="utf-8", errors="replace"))
    for sk in _skill_dirs():
        for md in sk.rglob("*.md"):
            parts.append(md.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(parts)

def _py_import_index() -> str:
    # ED-IN-0087 (finding: ED-IN-0085): `sim/` was retired 2026-07-21 and its contents moved to
    # engine/ (the core) and systems/<subsystem>/sim/ (the per-subsystem sims). This tuple was
    # never updated, so the orphan detector's import graph silently lost every simulation module —
    # the same rot class that broke structure_audit's CODE_ROOTS (ED-MB-0043). Roots are the live
    # trees now; `sim/` is deliberately absent rather than kept "just in case", because a root that
    # cannot exist is indistinguishable from one that is merely empty.
    parts = []
    for base in ("tools", "skills", "engine", "systems", "tests"):
        d = REPO / base
        if d.exists():
            for p in d.rglob("*.py"):
                if "__pycache__" in p.parts:
                    continue
                parts.append(p.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(parts)

def invoked_by(stem: str, rel: str, inv_text: str, py_text: str) -> list[str]:
    tags = []
    base = Path(rel).name
    if re.search(rf'\b{re.escape(base)}\b', inv_text):
        # distinguish which surface
        for wf in _workflows():
            if base in wf.read_text(encoding="utf-8", errors="replace"):
                tags.append(f"ci:{wf.name}")
        hk = REPO / ".githooks" / "pre-commit"
        if hk.exists() and base in hk.read_text(encoding="utf-8", errors="replace"):
            tags.append("hook:pre-commit")
        settings = REPO / ".claude" / "settings.json"
        if settings.exists() and base in settings.read_text(encoding="utf-8", errors="replace"):
            tags.append("hook:claude")
        # skills mention
        for sk in _skill_dirs():
            if any(base in md.read_text(encoding="utf-8", errors="replace")
                   for md in sk.rglob("*.md")):
                tags.append(f"skill:{sk.name}")
                break
    # imported by another .py? (module import of the stem, excluding self-definition)
    if re.search(rf'(^|\n)\s*(import\s+{re.escape(stem)}\b|from\s+\S*\b{re.escape(stem)}\b\s+import|import\s+\S*\.{re.escape(stem)}\b)', py_text):
        tags.append("tool:imported")
    return sorted(set(tags))

# ---------------------------------------------- orphan signal (reuse structure_audit)
def _gcode_imported_modules() -> set[str]:
    """Union of every module that appears as SOMEONE's import in the newest
    structure-audit g_code.json (edge #2: derive orphans mechanically, don't
    hand-maintain). g_code maps module -> its deps, so the union of all values is
    'imported by someone'. Top-level imports only — combined with a full-text grep
    (which catches lazy imports) and the invoker scan (workflows/hooks/skills).

    EXPLICIT NO-OP (OI-52a / OI-53a, ED-IN-0097, 2026-07-29-code-shape-open-items plan §3 Wave 4
    item 2): this used to glob `designs/audit/**/g_code.json`, but `designs/` was RETIRED
    2026-07-19 (ED-IN-0071 P4/P5, CLAUDE.md §3 — "Do not recreate designs/") and is gone from the
    working tree, so the glob was SILENTLY empty on every run — a live instance of the §0.1 point-5
    read/write-asymmetry hazard (correct when written, dead once the tree moved, and nothing
    flagged it). There is no live, stable replacement path to glob: `structure_audit.py --output-dir`
    takes a CALLER-CHOSEN directory every invocation (a dated `audit/<session>/structure/` folder,
    or an ad-hoc scratch dir — see skills/valoria-vector-audit/SKILL.md's own invocation example and
    `audit/2026-07-14-gameplay-subsystem-observatory/00_workplan.md`), never one fixed location this
    generator could rely on. Rather than glob a second dead prefix, this is now an EXPLICIT no-op:
    the g_code-derived signal contributes nothing, and `imported_internally` in `build()` below
    falls back to the full-text-grep `tool:imported` signal (`_py_import_index()` /
    `invoked_by()`), which is unaffected by this and already covers lazy imports the AST-only
    g_code graph would miss anyway. If a stable live g_code.json home is ever established, wire
    this to it then — do not resurrect a `designs/` or `sim/` glob."""
    return set()

def _module_name(rel: str) -> str:
    return rel[:-3].replace("/", ".") if rel.endswith(".py") else rel.replace("/", ".")

# ------------------------------------------------------------------------- classify
def role_of(info: dict, invokers: list[str], rel: str) -> str:
    committed = any(w.get("dest") and isinstance(w["dest"], str)
                    and not w["dest"].startswith("<")
                    and not w["dest"].startswith("/home/claude")
                    for w in info["writes"])
    # No __main__ and no committed (literal-dest) write => import-only library. A
    # library function that writes only to a caller-supplied dynamic path (e.g.
    # core.write_js_bundle) is still import-only; its writes fire only when imported.
    if not info["has_main"] and not committed:
        return "D:import-only-library"
    if committed:
        return "A:writes-artifact"
    if info["writes"] and all(w["mode"] == "write" and w["dest"] == "<stream>"
                              for w in info["writes"]):
        return "A:writes-artifact"
    if info["prints"] and not committed:
        return "B:stdout-or-gate"
    if info["writes"]:
        return "C:mutating-or-dynamic-dest"
    return "B:stdout-or-gate"

# ------------------------------------------------------------------------------ main
def build() -> dict:
    inv_text = _text_index()
    py_text = _py_import_index()
    gcode_imported = _gcode_imported_modules()
    entries: list[dict] = []

    for p in _iter_tool_scripts():
        rel = str(p.relative_to(REPO))
        info = analyze_py(p)
        stem = p.stem
        mod = _module_name(rel)
        inv = invoked_by(stem, rel, inv_text, py_text)
        is_init = p.name == "__init__.py"
        # sim_harness/ is a self-contained prototype cluster: harness.py is its
        # manual CLI entry, adapters are registered via package __init__ import.
        in_sim_harness = rel.startswith("tools/sim_harness/")
        imported_internally = (mod in gcode_imported) or ("tool:imported" in inv)
        invoked = any(t for t in inv if not t.startswith("tool:"))
        orphaned = (not imported_internally and not invoked and not is_init
                    and not in_sim_harness)
        role = role_of(info, inv, rel)
        # prune candidate = orphaned AND no CLI surface AND writes NOTHING (pure
        # function whose only __main__ is a self-test). A writer/generator is never
        # dead code — at most "unwired" (handled in Stage 2, e.g. build_graph.py);
        # a one-time ledger writer (deprecated/tools/build_audit_registry_backfill.py,
        # retired 2026-07-29 ED-IN-0097/OI-15) still writes.
        prune = (orphaned and not info["uses_cli"]
                 and role != "A:writes-artifact" and not info["writes"])
        entries.append({
            "path": rel, "kind": "tool", "stem": stem,
            "writes": info["writes"], "prints_stdout": info["prints"],
            "has_cli": info["has_main"], "uses_cli_args": info["uses_cli"],
            "invoked_by": inv, "imported_internally": imported_internally,
            "orphaned": orphaned, "prune_candidate": prune,
            "role": role,
            "imports": [m for m in info["reads_imports"]
                        if m in {"names", "ci_common", "yaml", "audit_registry",
                                 "workplan_status", "audit_staleness", "registry"}],
        })

    for p in _iter_skill_scripts():
        rel = str(p.relative_to(REPO))
        info = analyze_py(p)
        inv = invoked_by(p.stem, rel, inv_text, py_text)
        entries.append({
            "path": rel, "kind": "skill-script", "stem": p.stem,
            "writes": info["writes"], "prints_stdout": info["prints"],
            "has_cli": info["has_main"], "invoked_by": inv,
            "orphaned": False, "role": role_of(info, inv, rel), "imports": [],
        })

    # hooks (declared surfaces, not scanned as scripts)
    hooks = [
        {"path": ".githooks/pre-commit", "kind": "hook", "trigger": "git pre-commit",
         "writes": [], "role": "B:stdout-or-gate", "invoked_by": ["git:core.hooksPath"],
         "runs": "tools/valoria_local.py --staged"},
        {"path": ".claude/settings.json#PreToolUse", "kind": "hook",
         "trigger": "PreToolUse(Write|Edit|MultiEdit)", "writes": [],
         "role": "B:stdout-or-gate", "invoked_by": ["claude-code"],
         "runs": "tools/hook_naming_guard.py"},
        {"path": ".claude/settings.json#SessionStart", "kind": "hook",
         "trigger": "SessionStart", "writes": [], "role": "B:stdout-or-gate",
         "invoked_by": ["claude-code"], "runs": "tools/session_status.py"},
        {"path": ".claude/settings.json#Stop", "kind": "hook", "trigger": "Stop",
         "writes": [], "role": "B:stdout-or-gate", "invoked_by": ["claude-code"],
         "runs": "tools/session_handoff_reminder.py"},
    ]
    entries.extend(hooks)

    # workflows (what artifact each produces)
    for wf in _workflows():
        txt = wf.read_text(encoding="utf-8", errors="replace")
        runs = sorted(set(re.findall(r'python3?\s+(tools/\S+\.py|\S+\.py)', txt)))
        emits = []
        if "upload-pages-artifact" in txt or "deploy-pages" in txt:
            emits.append("github-pages")
        if re.search(r'\bgit\s+push\b', txt) or "create-pull-request" in txt:
            emits.append("commit/PR")
        entries.append({
            "path": str(wf.relative_to(REPO)), "kind": "workflow",
            "runs": runs, "emits": emits or ["ci-status"],
            "writes": [], "role": "workflow", "invoked_by": ["github-actions"],
        })

    # Claude Code Workflow scripts (.claude/wf_*.js) — ED-IN-0087. Distinct kind, distinct
    # invoker: these are run by hand in a session, not by CI, and their "runs" are the agent
    # phases they declare rather than the python they shell out to.
    for wf in _claude_workflows():
        txt = wf.read_text(encoding="utf-8", errors="replace")
        phases = re.findall(r"\{\s*title:\s*'([^']+)'", txt)
        name_m = re.search(r"name:\s*'([^']+)'", txt)
        entries.append({
            "path": str(wf.relative_to(REPO)), "kind": "claude-workflow",
            "runs": phases,
            "emits": [name_m.group(1)] if name_m else ["audit-artifacts"],
            "writes": [], "role": "orchestration",
            "invoked_by": ["session (Workflow tool)"],
        })

    # Subagent definitions (.claude/agents/*.md) — ED-IN-0087, same blind spot as the workflows
    # above one level down. A roster file is apparatus: it decides what a whole class of agents CAN
    # DO, and the read-only critic's entire value is the tools it does NOT list. An inventory that
    # cannot see it cannot flag it going stale. `emits` records the granted tools for exactly that
    # reason — the interesting drift here is a tool list quietly growing.
    for ag in sorted((REPO / ".claude" / "agents").glob("*.md")) if (REPO / ".claude" / "agents").exists() else []:
        txt = ag.read_text(encoding="utf-8", errors="replace")
        name_m = re.search(r"^name:\s*(.+)$", txt, re.M)
        tools_m = re.search(r"^tools:\s*(.+)$", txt, re.M)
        agent_name = name_m.group(1).strip() if name_m else ag.stem
        entries.append({
            "path": str(ag.relative_to(REPO)), "kind": "claude-agent",
            "runs": [],
            "emits": [t.strip() for t in tools_m.group(1).split(",")] if tools_m else ["<inherits ALL tools>"],
            "writes": [], "role": "orchestration",
            "invoked_by": sorted({str(wf.relative_to(REPO)) for wf in _claude_workflows()
                                  if agent_name in wf.read_text(encoding="utf-8", errors="replace")}),
        })

    # counts
    by_kind: dict[str, int] = {}
    by_role: dict[str, int] = {}
    orphans, prunes = [], []
    for e in entries:
        by_kind[e["kind"]] = by_kind.get(e["kind"], 0) + 1
        if "role" in e:
            by_role[e["role"]] = by_role.get(e["role"], 0) + 1
        if e.get("orphaned"):
            orphans.append(e["path"])
        if e.get("prune_candidate"):
            prunes.append(e["path"])

    return {"schema_version": 1,
            "generator": "tools/build_apparatus_registry.py",
            "note": "GENERATED — do not hand-edit; re-run the generator. "
                    "Regenerable inventory of every skill/tool/hook/workflow with its "
                    "output destination + format + invokers + orphan status.",
            "counts": {"total": len(entries), "by_kind": by_kind, "by_role": by_role,
                       "orphaned": len(orphans), "prune_candidates": len(prunes)},
            "prune_candidates": sorted(prunes),
            "orphaned_no_cli": sorted(orphans),
            "entries": entries}

# --------------------------------------------------------------------- md rendering
_ROLE_TITLES = {
    "A:writes-artifact": "A — Writes a committed/generated artifact",
    "B:stdout-or-gate": "B — Stdout report / CI gate (exit-code)",
    "C:mutating-or-dynamic-dest": "C — Mutating / dynamic-destination",
    "D:import-only-library": "D — Import-only library (no CLI writes)",
    "workflow": "CI workflow",
    "hook": "Hook",
}

def _fmt_writes(writes: list[dict]) -> str:
    if not writes:
        return "—"
    return "; ".join(
        f"`{w.get('dest') or '?'}` ({w.get('format','?')}{', append' if w.get('mode')=='append' else ''})"
        for w in writes)

def render_md(reg: dict) -> str:
    c = reg["counts"]
    L = ["# Apparatus registry — output destination & format",
         "",
         "> GENERATED by `tools/build_apparatus_registry.py` — do not hand-edit; re-run it.",
         "> Inventories every skill, tool, hook and workflow with what it reads, what it",
         "> writes (destination + format), who invokes it, and whether it is orphaned.",
         "",
         f"**{c['total']} apparatuses** — " +
         ", ".join(f"{k}: {v}" for k, v in sorted(c["by_kind"].items())) +
         f" · **{c['orphaned']} orphaned**.",
         ""]
    if reg.get("prune_candidates"):
        L += ["## ⚠ Prune candidates (orphaned + no CLI surface — flag for Jordan)", ""]
        for o in reg["prune_candidates"]:
            L.append(f"- `{o}`")
        L.append("")
    others = [o for o in reg.get("orphaned_no_cli", []) if o not in reg.get("prune_candidates", [])]
    if others:
        L += ["## Orphaned but CLI-invocable (manual/one-off tools — not prune targets)", ""]
        for o in others:
            L.append(f"- `{o}`")
        L.append("")
    # group tools/skills by role
    L += ["## By output type", ""]
    role_order = ["A:writes-artifact", "C:mutating-or-dynamic-dest",
                  "B:stdout-or-gate", "D:import-only-library"]
    scripts = [e for e in reg["entries"] if e["kind"] in ("tool", "skill-script")]
    for role in role_order:
        rows = [e for e in scripts if e.get("role") == role]
        if not rows:
            continue
        L += [f"### {_ROLE_TITLES.get(role, role)}", "",
              "| Path | Writes (dest · format) | CLI | Invoked by |",
              "|---|---|---|---|"]
        for e in sorted(rows, key=lambda x: x["path"]):
            inv = ", ".join(e.get("invoked_by") or []) or "—"
            L.append(f"| `{e['path']}` | {_fmt_writes(e.get('writes', []))} | "
                     f"{'yes' if e.get('has_cli') else '—'} | {inv} |")
        L.append("")
    # hooks
    hooks = [e for e in reg["entries"] if e["kind"] == "hook"]
    if hooks:
        L += ["## Hooks", "", "| Surface | Trigger | Runs |", "|---|---|---|"]
        for e in hooks:
            L.append(f"| `{e['path']}` | {e.get('trigger','?')} | `{e.get('runs','?')}` |")
        L.append("")
    # workflows
    wfs = [e for e in reg["entries"] if e["kind"] == "workflow"]
    if wfs:
        L += ["## CI workflows", "", "| Workflow | Runs | Emits |", "|---|---|---|"]
        for e in wfs:
            L.append(f"| `{e['path']}` | {', '.join(f'`{r}`' for r in e.get('runs', [])) or '—'} "
                     f"| {', '.join(e.get('emits', []))} |")
        L.append("")
    return "\n".join(L) + "\n"

def main(argv=None) -> int:
    # ED-IN-0097 (W4): this generator used to have NO argument parsing at all — main() ran and
    # OVERWROTE both generated artifacts on ANY invocation, including `--help`. The W4 adjudicator
    # tripped exactly that while merely inspecting the tool, regenerating both files and having to
    # `git checkout` them back. That is a live hazard for a repo whose convention is that
    # `references/apparatus_registry.{yaml,md}` has a SINGLE writer at a scheduled wave (IN, W5) —
    # an incidental read must not be able to forge a write.
    ap = argparse.ArgumentParser(
        description="Build the apparatus registry (references/apparatus_registry.{yaml,md}). "
                    "NOTE: writing is the default action; use --dry-run to inspect safely.")
    ap.add_argument("--dry-run", action="store_true",
                    help="compute and print the counts WITHOUT writing either artifact")
    args = ap.parse_args(argv)

    reg = build()
    yaml_path = REPO / "references" / "apparatus_registry.yaml"
    md_path = REPO / "references" / "apparatus_registry.md"
    if args.dry_run:
        c = reg["counts"]
        print("Apparatus registry (DRY RUN — nothing written):")
        print(f"  total={c['total']}  by_kind={c['by_kind']}")
        print(f"  orphaned(no importer/invoker)={c['orphaned']}  prune_candidates={c['prune_candidates']}")
        print(f"  prune_candidates: {reg['prune_candidates']}")
        print(f"  would write -> {yaml_path}  /  {md_path}")
        return 0
    try:
        import yaml
        yaml_path.write_text(
            "# GENERATED by tools/build_apparatus_registry.py — do not hand-edit.\n" +
            yaml.safe_dump(reg, sort_keys=False, allow_unicode=True, width=100),
            encoding="utf-8")
    except ImportError:
        yaml_path.with_suffix(".json").write_text(json.dumps(reg, indent=2), encoding="utf-8")
    md_path.write_text(render_md(reg), encoding="utf-8")
    c = reg["counts"]
    print("Apparatus registry built:")
    print(f"  total={c['total']}  by_kind={c['by_kind']}")
    print(f"  orphaned(no importer/invoker)={c['orphaned']}  prune_candidates={c['prune_candidates']}")
    print(f"  prune_candidates: {reg['prune_candidates']}")
    print(f"  -> {yaml_path}  /  {md_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
