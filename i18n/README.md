# Still, staged for the world

Everything in this folder is STAGED. It was prepared by machine on October 15, 2026, and nothing here is live on the Still page yet. The page itself (index.html) is unchanged in this wave. Staged means ready for a human check, not ready for a visitor.

## What is staged

- en.json: every visible string on the page, extracted as the source of truth.
- es.json: a full Spanish rendering of en.json, 60 content strings.
- es.notes.md: an independent machine check of es.json. Each Spanish string was back translated into English without sight of the original, then compared against en.json string by string.
- crisis-lines.json: crisis lines for 12 countries, each checked on October 15, 2026 against an official or operator source, with the source recorded beside every entry.

## The standard a translation must pass to ship

A translation ships only when all four are true:

1. A fluent human reader has checked every string against the English and signed off in the notes file for that language.
2. Every disputed string from the machine check is resolved, by the human reader, and the resolution is written down.
3. The reading level is re-measured in that language (for Spanish, the Fernandez Huerta formula) and lands near the English baseline of Flesch reading ease 90.
4. Every fact survives exactly: crisis numbers, keywords, links, and the placeholders.

A machine back translation check is a screen, not the check. It catches drift; it cannot judge warmth. Only the fluent human check in step 1 can pass a translation.

## Spanish, current state

- 60 content strings back translated and compared: 47 agree, 13 disputed.
- The disputes cluster where English uses a plain deliberate word Spanish renders loosely: the check in wording, the grounding heading, "Okay" upgraded to "Bien", "Numb" rendered as "Insensible", and "text" weakened in the two crisis instruction lines. Every disputed string is listed in es.notes.md with the English, the Spanish, the back translation, and the exact difference.
- Reading level: Fernandez Huerta 75.0, the fairly easy band. The English baseline is Flesch reading ease 90, so the Spanish runs plainer in vocabulary but heavier in sentence weight, about one band lower. Method and counts are in es.notes.md.
- Status: awaiting a fluent human check. Not shippable as final.

## Crisis lines, verification summary

11 of 12 countries verified on October 15, 2026. Sources, strongest first: the operator's own site, a government health page, then the IASP or FindAHelpline listing where the first two could not be reached.

- United States: 988 Suicide and Crisis Lifeline, 988. FCC.
- India: Tele-MANAS, 14416. Government of India.
- China: national mental health assistance hotline, 12356. gov.cn.
- Indonesia: Healing119, 119 extension 8, with WhatsApp chat. Ministry of Health.
- Pakistan: Rozan Counseling Helpline, 0304-111-1741. Operator's own site. The better known Umang line could not be verified: no reachable operator page and conflicting numbers in secondary sources, so it was not used.
- Brazil: CVV, 188. Operator's own site.
- Nigeria: SURPIN, 0800 078 7746. LifeLine International member page.
- Bangladesh: Kaan Pete Roi, 09612-119911. Operator's page. The operator does not state hours there, so hours is null rather than guessed.
- Russia: EMERCOM emergency psychological assistance, +7 495 989-50-50. FindAHelpline listing, entry verified by the helpline itself.
- Mexico: Linea de la Vida, 800 911 2000. gob.mx.
- Japan: Yorisoi Hotline, 0120-279-338. Operator, subsidized by the health ministry. TELL is noted in the file as the other service.
- Ethiopia: UNVERIFIED. No dedicated national suicide or crisis helpline could be found on any operator, government, IASP, or FindAHelpline source. The 8335 code in some aggregator lists traces to a 2020 COVID-19 test result text message service, not a crisis line. Service and phone are null in the file rather than filled from an aggregator.

Full per entry detail, including text and chat options, hours, languages, and source URLs, is in crisis-lines.json.
