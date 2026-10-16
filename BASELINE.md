# Still baseline: the fundamentals, measured

## The Loop

The Loop. Still improves by one measured cycle at a time. (1) Measure the fundamentals and write the numbers down with dates. (2) Name the weakest fundamental. (3) Make the smallest change that moves it. (4) Verify the change by re-measuring. (5) Record the cycle in the open, in this file, newest first. Then repeat. One cycle, one weakness, one verified change. Nothing counts until it is re-measured. A cycle that finds nothing it can honestly change records that too.

## Fundamentals, measured October 16, 2026

- **Page weight: 21.8 KB.** One self contained HTML file, 21,839 bytes (KB counted at 1,000 bytes). No other file loads. The growth since the first measure is the drift strip and the plainer surface copy, both added October 15, 2026.
- **Network calls: 0.** Re-verified by grep on the shipped file on October 16, 2026: no fetch, no XMLHttpRequest, no sendBeacon, no WebSocket, no external script, style, or image. The only links on the page are two ordinary anchors a visitor may choose to tap: the grounding source and the Topsoil Commons profile.
- **Pacer accuracy: maximum drift 10 ms, mean drift 1.56 ms on the latest run.** test/test_pacer.js run twice on October 16, 2026: 3 full cycles, 42 seconds, 9 of 9 phase transitions observed in both runs. The first run measured maximum drift 1 ms and mean drift 0.44 ms. The second, run while other work used the same machine, measured 10 ms and 1.56 ms, and its full output stands at test/pacer_result.json. All six recorded runs stand in test/pacer_measurements.json, wide ones included.
- **Reading level of the visible copy: not re-measured this cycle.** Last measured October 15, 2026: Flesch-Kincaid grade 2.5 (Flesch reading ease 90), on the page's visible text plus the eight check in lines.
- **Crisis lines last verified: October 16, 2026.** Checked against the FCC page for call or text 988 and chat at 988lifeline.org, and Crisis Text Line's own FAQ for text HOME to 741741. Both still read as the page states them.
- **Languages offered: 1.** English. A Spanish rendering of every string stands staged in i18n/, machine checked by back translation (47 of 60 content strings agree, 13 disputed and listed), and it does not ship until a fluent human reader checks it. That check has not happened.
- **Works with JavaScript disabled: partly, stated plainly.** The grounding steps, the crisis block, and every word of static copy still render and can be read, including the crisis numbers. The check in words never appear, because script builds them. The pacer buttons do nothing. The writing space can be typed in, but Save, Download, and Clear do nothing and nothing is stored. By design the check in and the pacer need JavaScript; the most urgent content on the page, the crisis lines, does not.

## The weakest fundamental

Languages offered: 1. It was the weakest at the baseline and it stays the weakest. The Spanish version exists and is staged in i18n/, but the standard this repo set for shipping it is a fluent human check, and no machine check substitutes for that. The cycle that ships Spanish starts when a fluent reader checks the 60 strings and resolves the 13 disputed ones listed in i18n/es.notes.md. Runner up, recorded honestly: the check in and the pacer are silent without JavaScript.

## Cycles

### Cycle 1, October 16, 2026: every fundamental re-measured, two pacer runs recorded

Re-measured all fundamentals on the current page. The page had changed since the first measure (a drift strip drawn from the recorded runs, and the plainer surface pass), so the October 15 numbers no longer described it: page weight is 21,839 bytes, not 12,869. The zero network rule was re-verified by grep and holds at 0. The pacer test ran twice: 9 of 9 transitions both times, maximum drift 1 ms on the quiet run and 10 ms on the loaded run, both recorded in test/pacer_measurements.json (runs 5 and 6), the loaded run kept as the artifact in test/pacer_result.json, and the drift strip on the page regenerated with tools/build_drift.py (run twice, same page both times). The crisis lines were re-verified against the FCC page and Crisis Text Line's own FAQ on October 16, 2026 and stand as printed. Languages did not move: the Spanish rendering stays staged until a fluent human reader checks it, which this cycle could not supply. The README proof lines were updated to the new run and the new check date in the same commit.

### Cycle 0, October 15, 2026: baseline measured

The fundamentals above are the first numbers on record for this page. No fix this cycle. The weakest fundamental is named and its fix is queued above.
