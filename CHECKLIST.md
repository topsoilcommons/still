# The 110 percent checklist: Still

State as of October 15, 2026. Every line carries its evidence; a line without evidence does not count as done. This file is maintained by the daily evolution pass.

## 100 percent: completeness
- [x] README accurate against the page, including the content rules (no diagnosis, no treatment claims, no efficacy claims, stated in the README and on the page)
- [x] LICENSE present (MIT)
- [x] COLLABORATE.md present
- [x] CONTRIBUTING.md present
- [x] AGENTS.md present
- [x] Demo present: index.html, one self contained static file, no build step, no external services, no network calls
- [x] .nojekyll present
- [x] Crisis block present on the page, checked against operator and federal pages on October 15, 2026

## The extra 10 percent
- [ ] Repository created on GitHub and publish tree pushed (later step: repo creation and deploy key)
- [ ] CI workflow present and green on GitHub runners
- [ ] Repo description and topics set
- [ ] Good first issues open, sized in hours (first candidate: rerun the pacer test on a second machine and post the result)
- [ ] Tagged release v0.1 once CI is green
- [ ] Live demo answering at https://auroracommons.github.io/still/

## Verification baseline (October 15, 2026)
- Pacer timing: test/test_pacer.js run for 3 full cycles (42 seconds). 9 of 9 phase transitions observed. Maximum drift 1 ms, mean drift 0.56 ms. Full output in test/pacer_result.json
- No network calls: verified by reading the single HTML file end to end. Inline styles and script only, no fetch, no XMLHttpRequest, no external assets
- Writing space: localStorage key still-writing only; Save, Download, and Clear act on the local copy
- Crisis lines: 988 (call or text, chat at 988lifeline.org) per FCC and SAMHSA pages; text HOME to 741741 per Crisis Text Line's own FAQ; both checked October 15, 2026
- Grounding practice: 5-4-3-2-1, written in our own words, source named on the page (University of Rochester Medical Center, Behavioral Health Partners blog)

## Upgrade queue
- [ ] A second timing run on different hardware, posted as an issue or pull request, so the drift figure rests on more than one machine
- [ ] Readability pass on the check in lines with a plain language reader
- [ ] A printed card version of the page for rooms without a screen, same words, same rules
