# Still

**Layer 1 of the Ascent: the mind at peace.** Mental health, steadiness, hope.

Aurora Commons addresses the hierarchy of human needs through open source.

The motto: Stand on the shoulders of giants.

The need, in the words of the map: a mind that can rest. Treatment and support for suffering, freedom from constant dread, and hope treated as infrastructure: a credible path, proof someone like you walked it, a first step small enough to take today. The full map is [The Ascent](https://github.com/auroracommons/auroracommons/blob/main/NEEDS.md) on the Aurora Commons profile.

## What Still is

A quiet, single page practice tool. Three things only:

1. **A check in.** Pick the word closest to how you feel. Get one plain, supportive line back. The lines are written for this page. They are company, not advice.
2. **A breathing pacer.** A circle that grows and shrinks on a 4 in, 4 hold, 6 out rhythm, with start and stop.
3. **A writing space.** A plain text area stored only in your browser, on your device, with Save on this device, Download, and Clear.

Still is a quiet tool. It is not medical care. It does not diagnose anything, it does not treat anything, and it claims no effect on anyone's health. The page says so, in plain words, at the top and in the footer.

At the bottom of the page, clearly separated, is a crisis block with the US lines: call or text 988 (Suicide and Crisis Lifeline), and text HOME to 741741 (Crisis Text Line).

The page works fully offline once loaded. It makes no network calls. Your writing never leaves the device.

## Live demo

https://auroracommons.github.io/still/ (link placeholder until the repository and Pages are enabled)

## Proof

Functional only, as of October 15, 2026. No health numbers exist here and none are claimed.

- **Pacer timing, measured.** The pacer computes its phase from total elapsed time, not from chained timers, so the rhythm cannot drift. The test in test/test_pacer.js runs that same phase math for 3 full cycles (14 seconds each, 42 seconds total) and records when each phase change is observed. Result of the run on October 15, 2026 (full output in test/pacer_result.json): 9 of 9 phase transitions observed, maximum drift 1 ms from the ideal times, mean drift 0.56 ms.
- **No network calls, verified by inspection.** The demo is one self contained HTML file: inline styles, inline script, no external fonts, images, scripts, or stylesheets. Reading the code shows no fetch, no XMLHttpRequest, no beacon, and no analytics. The only connections a visitor can trigger are two ordinary links they choose to click (the grounding source and the Aurora Commons profile). Open the file from disk with the network off and everything on the page works.
- **Writing stays on the device.** The writing space reads and writes one localStorage key (still-writing) in the visitor's own browser. Save, Download, and Clear act on that local copy only. Nothing is transmitted; there is no server to transmit to.
- **Crisis lines, as published by their operators, checked October 15, 2026.** Call or text 988 and chat at 988lifeline.org, free and 24/7, as published by the FCC (fcc.gov/988-suicide-and-crisis-lifeline) and SAMHSA (samhsa.gov, 988 FAQ). Text HOME to 741741 for free, 24/7, confidential support, as published by Crisis Text Line (crisistextline.org/about-us/faq).
- **How this page improves.** It runs the Loop: measured fundamentals, the weakest one named, one verified change at a time. [BASELINE.md](BASELINE.md) holds the numbers and the open log of cycles.
- **The grounding practice has a named public source.** The 5-4-3-2-1 practice on the page is written in our own words and cites its source on the page: the University of Rochester Medical Center, Behavioral Health Partners blog, "5-4-3-2-1 Coping Technique for Anxiety."

## Contribute

Ways in are in [COLLABORATE.md](COLLABORATE.md) and [CONTRIBUTING.md](CONTRIBUTING.md). The wider table is the [Open Table](https://github.com/auroracommons/auroracommons/blob/main/OPEN_TABLE.md) on the profile: one rule, raise the floor beneath everyone, and credit in the public ledger for verified work.

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Still contributors.

## Built on the shoulders of giants

The 5-4-3-2-1 grounding practice, from the University of Rochester Medical Center's public writing. The 988 Suicide and Crisis Lifeline and Crisis Text Line, whose published lines the crisis block carries word for word in short form. Plain HTML, CSS, and JavaScript that any browser already knows how to run.
