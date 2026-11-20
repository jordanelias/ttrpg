"""[B06.02] Each transcendental has ONE owner, `engine/dice_engine/fmath.py`.

A `math.tanh` left in a game-path module is a second owner: the port reproduces `fmath`'s list of functions, and a
call that bypasses it is a function the vectors in `engine/tests/test_fmath.py` never name. This is gate 3's grep, in
process: no file under `engine/season`, `engine/dice_engine` or `modules` (tests and `fmath.py` excluded) calls
`math.log|exp|tanh|erf|sin|cos|atan2|hypot`, or imports one of them from `math` by name.

`sqrt` stays on `math` (IEEE-754 requires it correctly rounded); `**` with an integer exponent is repeated
multiplication; neither is searched for here.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCAN = ("engine/season", "engine/dice_engine", "modules")
NAMES = "log|exp|tanh|erf|sin|cos|atan2|hypot"
# `math.log(`, `_math.log(`; not `fmath.log(` (the letter before `math` excludes it)
CALL = re.compile(r"(?<![A-Za-z0-9])_?math\.(%s)\(" % NAMES)
# `from math import ... tanh ...` (a bare name imported from the platform module)
# a parenthesised import may run over several lines, so this is matched over the whole comment-stripped text
IMPORT = re.compile(r"^[ \t]*from\s+math\s+import\s+(\([^)]*\)|[^\n]*)", re.M)


def _game_files():
    out = []
    for top in SCAN:
        for p in sorted((ROOT / top).rglob("*.py")):
            rel = p.relative_to(ROOT)
            if "tests" in rel.parts or rel.as_posix() == "engine/dice_engine/fmath.py":
                continue
            out.append(p)
    return out


def _rel(p):
    return p.relative_to(ROOT) if ROOT in p.parents else p


def _offences(files):
    bad = []
    for p in files:
        lines = [line.split("#", 1)[0] for line in p.read_text(encoding="utf-8").splitlines()]
        for i, code in enumerate(lines, 1):
            if CALL.search(code):
                bad.append(f"{_rel(p)}:{i}: {code.strip()}")
        text = "\n".join(lines)
        for m in IMPORT.finditer(text):
            if re.search(r"\b(%s)\b" % NAMES, m.group(1)):
                bad.append(f"{_rel(p)}:{text.count(chr(10), 0, m.start()) + 1}: {m.group(0).strip()}")
    return bad


def test_no_math_transcendental_outside_fmath():
    files = _game_files()
    assert len(files) >= 150, f"the scan saw {len(files)} files: an empty scan proves nothing"
    assert any(p.name == "choose.py" for p in files) and any(p.name == "units.py" for p in files)
    assert _offences(files) == []


def test_control_the_scan_sees_a_planted_math_call(tmp_path):
    planted = tmp_path / "planted.py"
    planted.write_text("import math\nx = math.tanh(0.5)\ny = _math.log(2.0)\nfrom math import exp, sqrt\n"
                       "z = fmath.tanh(0.5)\nok = math.sqrt(2.0)\nfrom math import (\n    cos,\n    sqrt)\n", encoding="utf-8")
    bad = _offences([planted])
    assert len(bad) == 4 and not any("fmath.tanh" in b or "sqrt(2.0)" in b for b in bad)
