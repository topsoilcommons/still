# Still

Still is a quiet, single page tool to check in, breathe, and write. One file, zero network calls, and nothing you write leaves your device. Its breathing pacer is measured, not assumed: sixteen recorded runs stand in the record, the latest with a largest drift of 2 ms.

Layer 1 of Topsoil Commons: the mind at peace. Mental health, steadiness, hope.

First step: open the live page below and pick the word closest to how you feel right now. It takes a few seconds.

## What Still is

A quiet, single page practice tool. Three things only:

1. **A check in.** Pick the word closest to how you feel. Get one plain, supportive line back. The lines are written for this page. They are meant to keep you company, not to give advice.
2. **A breathing pacer.** A circle that grows and shrinks on a 4 in, 4 hold, 6 out rhythm, with start and stop.
3. **A writing space.** A plain text area stored only in your browser, on your device, with Save on this device, Download, and Clear.

Still is a quiet tool. It is not medical care. It does not diagnose anything, it does not treat anything, and it claims no effect on anyone's health. The page says so, in plain words, at the top and in the footer.

At the bottom of the page, clearly separated, is a crisis block with the US lines: call or text 988 (Suicide and Crisis Lifeline), and text HOME to 741741 (Crisis Text Line).

## Live demo

https://topsoilcommons.github.io/still/ (live, verified October 16, 2026)

The need, in the words of the map: a mind that can rest. Treatment and support for suffering, freedom from constant dread, and hope treated as infrastructure: a credible path, proof someone like you walked it, a first step small enough to take today. The full map is [The Ascent](https://github.com/topsoilcommons/topsoilcommons/blob/main/NEEDS.md) on the Topsoil Commons profile.

## Proof

Functional only, as of October 15, 2026. No health numbers exist here and none are claimed.

- **Pacer timing, measured.** The pacer computes its phase from total elapsed time, not from chained timers, so drift cannot accumulate. The test in test/test_pacer.js runs that same phase math for 3 full cycles (14 seconds each, 42 seconds total) and records when each phase change is observed. Latest run, October 20, 2026, morning, run 16 (full output in [test/pacer_result.json](test/pacer_result.json)): 9 of 9 phase transitions observed, maximum drift 2 ms from the ideal times, mean drift 0.67 ms. On October 17, 2026, one run measured maximum drift 106 ms and mean drift 8.11 ms while the Ground cycle ran in parallel on the same machine, and it is kept in the record as measured. Across all sixteen recorded runs, the largest drift in a single run ranged from 1 ms to 106 ms, and 106 ms, recorded on October 17, 2026 under load, is the widest drift on record. Every recorded run stands in [test/pacer_measurements.json](test/pacer_measurements.json), wide ones included.
- **No network calls, verified by inspection.** The demo is one self contained HTML file: inline styles, inline script, no external fonts, images, scripts, or stylesheets. Reading the code shows no fetch, no XMLHttpRequest, no beacon, and no analytics. The only connections a visitor can trigger are two ordinary links they choose to click (the grounding source and the Topsoil Commons profile). Open the file from disk with the network off and everything on the page works.
- **Writing stays on the device.** The writing space reads and writes one localStorage key (still-writing) in the visitor's own browser. Save, Download, and Clear act on that local copy only. Nothing is transmitted; there is no server to transmit to.
- **Crisis lines, as published by their operators, checked October 19, 2026 (evening).** Call or text 988 and chat at 988lifeline.org, free and 24/7, as published by SAMHSA (samhsa.gov, 988 FAQ and 988 Key Messages; the FCC page at fcc.gov/988-suicide-and-crisis-lifeline publishes the same lines). Text HOME to 741741 for free, 24/7, confidential support, as published by Crisis Text Line (crisistextline.org/about-us/faq).
- **How this page improves.** The basic counts are checked, the weakest count is named, and one checked change is made at a time. [BASELINE.md](BASELINE.md) holds the numbers and the open log of cycles.
- **The grounding practice has a named public source.** The 5-4-3-2-1 practice on the page is written in our own words and cites its source on the page: the University of Rochester Medical Center, Behavioral Health Partners blog, "5-4-3-2-1 Coping Technique for Anxiety."

## For agents

Still offers agents nothing to call and collects nothing. Its only machine readable fact is its committed measurement artifact, [test/pacer_result.json](test/pacer_result.json), with the recorded runs in [test/pacer_measurements.json](test/pacer_measurements.json).

## Contribute

Ways to take part are in [COLLABORATE.md](COLLABORATE.md) and [CONTRIBUTING.md](CONTRIBUTING.md). More ways to take part are in the [Open Table](https://github.com/topsoilcommons/topsoilcommons/blob/main/OPEN_TABLE.md) on the profile: one rule, raise the floor beneath everyone, and credit in a public list for checked work.

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Still contributors.

## Stand on the shoulders of giants

The 5-4-3-2-1 grounding practice, from the University of Rochester Medical Center's public writing. The 988 Suicide and Crisis Lifeline and Crisis Text Line, whose published lines the crisis block carries word for word in short form. Plain HTML, CSS, and JavaScript that any browser already knows how to run.

Its record is filed in [the Index](https://topsoilcommons.github.io/index/).

Advised by Groundskeeper.
