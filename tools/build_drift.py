#!/usr/bin/env python3
"""Build the pacer drift strip on the Still page.

The strip is drawn from test/pacer_measurements.json, the committed record
of builder test runs. One mark per run, at the place its largest measured
drift falls on a band that runs from 0 to 20 milliseconds. Nothing here
is simulated: every mark is a run in that file. The strip does not move.
On this page only the breathing pacer moves, because the pacer is the
instrument itself.

Run: python3 tools/build_drift.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEGIN = "<!-- drift:begin -->"
END = "<!-- drift:end -->"
SCALE_MAX = 20


def main():
    data = json.loads(
        (ROOT / "test" / "pacer_measurements.json").read_text(
            encoding="utf-8"))
    runs = data["runs"]
    marks = "\n".join(
        '    <span class="driftmark" style="left:%.1f%%" title="Run %d: largest drift %d milliseconds"></span>'
        % (100.0 * r["max_drift_ms"] / SCALE_MAX, i + 1, r["max_drift_ms"])
        for i, r in enumerate(runs))
    values = ", ".join(str(r["max_drift_ms"]) for r in runs[:-1])
    values += ", and %d" % runs[-1]["max_drift_ms"]
    section = """%s
<section aria-labelledby="drift-h">
  <h2 id="drift-h">Pacer timing, measured</h2>
  <p class="sub">%d test runs of this pacer stand recorded in test/pacer_measurements.json in this repository, counted on October 15, 2026. Each run watched 9 phase changes over 3 full rounds, and all 9 changes landed in every run. The largest drift in each run was %s milliseconds.</p>
  <div class="driftband" role="img" aria-label="A band from 0 to 20 milliseconds with one mark per recorded test run, at 1, 2, 3, and 18 milliseconds.">
%s
  </div>
  <p class="sub">Key: one mark per recorded run. A mark's place on the band is that run's largest drift from the ideal phase times. The band runs from 0 to %d milliseconds, and one unit is one millisecond. These are builder test runs on the build machine, labeled as such in the measurements file. This page collects nothing.</p>
</section>
%s""" % (BEGIN, len(runs), values, marks, SCALE_MAX, END)

    path = ROOT / "index.html"
    page = path.read_text(encoding="utf-8")
    if BEGIN in page and END in page:
        before, rest = page.split(BEGIN, 1)
        _, after = rest.split(END, 1)
        page = before + section + after
    else:
        # Insert directly after the Breathe section closes.
        anchor = "</section>"
        idx = page.find("<h2>Breathe</h2>")
        if idx < 0:
            print("build_drift: Breathe section not found", file=sys.stderr)
            sys.exit(1)
        end = page.find(anchor, idx) + len(anchor)
        page = page[:end] + "\n" + section + page[end:]
    path.write_text(page, encoding="utf-8")
    print("build_drift: %d runs drawn" % len(runs))


if __name__ == "__main__":
    main()
