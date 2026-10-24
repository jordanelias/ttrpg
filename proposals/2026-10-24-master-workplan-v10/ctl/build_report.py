"""Substitute {{T:key}} placeholders in a template with the strings in a table JSON.

usage: python build_report.py TEMPLATE.md TABLES.json OUT.md
Refuses to write when a placeholder has no value or a value is left unused-but-None."""
import sys, re, json
tmpl, tables, out = sys.argv[1:4]
T = json.load(open(tables))
src = open(tmpl).read()
missing = sorted(set(re.findall(r"\{\{T:([a-z0-9_]+)\}\}", src)) - set(k for k, v in T.items() if v is not None))
if missing:
    sys.exit(f"placeholders with no value: {missing}")
res = re.sub(r"\{\{T:([a-z0-9_]+)\}\}", lambda m: str(T[m.group(1)]), src)
open(out, "w").write(res)
print("wrote", out, len(res), "bytes")
