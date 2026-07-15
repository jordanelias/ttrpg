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
import ast, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

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
    wf = REPO / ".github" / "workflows"
    return sorted(wf.glob("*.yml")) if wf.exists() else []

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
    has_main = bool(re.search(r'if\s+__name__\s*==\s*["\']__main__["\']', src))
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
    parts = []
    for base in ("tools", "skills", "sim", "tests"):
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
    (which catches lazy imports) and the invoker scan (workflows/hooks/skills)."""
    hits = sorted((REPO / "designs" / "audit").rglob("structure/data/g_code.json"))
    if not hits:
        hits = sorted((REPO / "designs" / "audit").rglob("g_code.json"))
    if not hits:
        return set()
    try:
        graph = json.loads(hits[-1].read_text(encoding="utf-8"))
    except Exception:
        return set()
    imported: set[str] = set()
    for deps in graph.values():
        if isinstance(deps, list):
            imported.update(deps)
    return imported

def _module_name(rel: str) -> str:
    return rel[:-3].replace("/", ".") if rel.endswith(".py") else rel.replace("/", ".")

# ------------------------------------------------------------------------- classify
def role_of(info: dict, invokers: list[str], rel: str) -> str:
    committed = any(w.get("dest") and isinstance(w["dest"], str)
                    and not w["dest"].startswith("<")
                    and not w["dest"].startswith("/home/claude")
                    for w in info["writes"])
    if not info["has_main"] and not info["writes"]:
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
        # a one-time ledger writer (build_audit_registry_backfill.py) still writes.
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

def main() -> int:
    reg = build()
    yaml_path = REPO / "references" / "apparatus_registry.yaml"
    md_path = REPO / "references" / "apparatus_registry.md"
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
