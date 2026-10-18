# Contributing to Still

Contributions are welcome. The house rules here are few and firm: no medical claims of any kind, no network calls, and writing never leaves the device. The evidence rule applies as everywhere in this Commons: a change ships with the run or check that proves it.

## Good first tasks (sized in hours)

- **Rerun the pacer test (under an hour).** Run `node test/test_pacer.js` on your machine and open a pull request or issue with the output. A second machine makes the published drift figure stronger.
- **Read the page aloud (under an hour).** Read every line on the page out loud and file any sentence that sounds clinical, cold, or confusing. Wording is this project's whole surface.
- **Recheck the crisis lines (under an hour).** Compare the crisis block against the pages its operators publish (988lifeline.org, crisistextline.org, and the FCC or SAMHSA 988 pages) and confirm or correct it, with the links in your pull request.
- **Test offline (under an hour).** Save the page, turn the network off, and confirm everything works: check in, pacer, save, download, clear. Report the browser and what you saw.

## Ground rules

- No diagnosis, no treatment claims, no efficacy claims, in copy or in code comments that face the public.
- No new network calls, ever. No analytics, no external fonts or assets.
- The writing space stays in localStorage. Any change that moves writing off the device does not merge.
- The crisis block changes only against the operators' own published pages, cited in the pull request.

## Pull requests

Keep them small and single purpose. State the evidence in the PR description: what you ran or checked and what it showed. Contributors are named in release notes, by name, stage name, or anonymously, as they choose.

## Ways in, by level

**First hour.** Rerun the pacer test (node test/test_pacer.js) on your machine and file the output, or recheck the crisis lines against their operators' pages. Both are written out above, and neither assumes experience with this project.

**First week.** Test the page offline in a browser the record has not covered, or read the whole page aloud and file every sentence that sounds clinical, cold, or confusing. Wording is this project's whole surface.

**The deep end.** The page speaks one language. A full Spanish rendering stands staged in i18n/, with 13 of its 60 checked strings disputed, and it ships only after a fluent human reader resolves every dispute. If you are that reader, this is the deepest work here. The pacer's timing record stands beside it: ten recorded runs, the widest drift 106 ms under load, the latest 3 ms.
