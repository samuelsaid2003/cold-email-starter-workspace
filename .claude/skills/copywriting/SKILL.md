---
name: copywriting
description: Write a short cold email sequence from your saved business context, personalised only with clean lead fields and spintaxed across most of the script, then self-check it against the rules and hand the drafts back for approval. Use when a campaign needs new copy or a rewrite; it never sends or launches anything.
---

# Cold email copywriting

You write the copy for one campaign. You draft it, check it, and hand it back. A person approves it before anything goes into a live campaign.

Write in plain, direct English. The author of this skill prefers GPT-6.1 Sol for the first draft because it writes more directly; if you're running a different model, follow these rules just as closely.

## 1. Read the business context first

Before writing anything, read `business.md` in the workspace root (the business interview skill writes it). Use these parts:

- what the business does
- the offer: what is being sold, and what the prospect gets
- the ideal customer (ICP) and who to skip
- pains, objections and buying triggers
- claims you can make, and approved proof
- past campaigns: what was sent before and how it did
- voice, voice samples and sign-off

If the offer, the ICP or the claims are missing, stop and ask for them, or run the business interview skill. Don't fill the gaps yourself.

Only use claims from the approved list. Never invent results, numbers, client names, case studies or guarantees. If a line needs proof that isn't on the list, leave a clearly marked gap and ask.

Keep the message relevant to the people on the list. Spam is an irrelevant message sent to irrelevant people, so the copy has to match the offer to this ICP.

## 2. Check the lead fields

Personalise only from fields that are present and clean for every lead in the list (the list building skill's upload file uses these column names):

| Field | Rule |
|---|---|
| `first_name` | Required. Only leads with a first name go into the campaign. Report any leads without one. |
| `company_name` | Highly recommended, but not essential. This must be the cleaned name from the company name cleaning skill (prefixes and suffixes removed so it reads as if typed by hand), never `original_company_name`. |
| Likely client type or ICP | Optional. Use it only if the list has it as its own column, for example the kind of clients the company serves. Don't guess it inside the copy. |

Personalise mostly through small variables like these rather than full personalised lines.

If some leads are missing the company name or client type, tell the user how many, and ask whether to write the lines so they read naturally without that field or to keep those leads out.

## 3. Sequence shape

Two steps: the first email and one follow-up.

- **Gap:** 3 days between them.
- **Thread:** the follow-up goes in the same thread, so the lead sees the first email under it. It has no new subject line.
- **Why only two:** too many follow-ups with no response can damage domain reputation.

## 4. Rules for the first email

**Subject line**
- 2–5 words.
- Personalised and on topic.
- Reads like it came from a colleague, not a marketer.

**Body**
- Short. Not long-winded.
- No links, no images, no formatting (bold, colours, bullet lists) and no dollar signs or dollar figures piled into the copy.
- Avoid common spam words.
- Uses only approved claims.

**Call to action**
- Low friction, for example "interested in a chat?"
- Fit it to the offer, the service, the sales process and the ICP.
- Don't try to make the sale in the first email.

## 5. Rules for the follow-up

Add one thing the first email didn't have. Pick what suits the offer:

- extra information about the offer or service
- extra credibility (from the approved claims only)
- a simple nudge, or "should I just give you a call?"

The same body rules apply: short, plain, no links, images or formatting.

## 6. Spintax

Vary about 90% of the script so the copy has 3,000 or more versions.

- Spin in blocks of 2–5 words, not single words and not whole paragraphs.
- Every combination must read as a correct, sensible sentence. Read the branches aloud in your head; if any pairing reads badly, rewrite it.
- Keep the meaning the same across all options in a block. Spintax changes the wording, not the offer or the claims.
- Spin the subject line as well.
- Leave merge fields outside the options, or put the same merge field in every option, so a lead's name or company can't drop out in some versions.

**Syntax:** use your sequencer's own spintax and merge-field syntax. In Cheap Sequencer the editor uses `{option one|option two}` for spintax and `{{first_name}}` / `{{company_name}}` for lead fields. Other sequencers differ, so check yours. Keep spintax flat (no options inside options) unless you've confirmed your sequencer supports nesting.

**Counting versions:** multiply the number of options in each block. For example, 3 blocks with 3 options each gives 3 × 3 × 3 = 27. Report the total for each step.

## 7. A/B variants (only if asked)

- Two variants at most (three is pushing it).
- Same offer in both.
- Test one variable at a time, such as the angle, the CTA or a PS line.
- The winner is picked on positive replies, using positive reply rate (positive replies divided by all replies). Note in the draft which variable is being tested.

## 8. Draft format

Save the draft as a markdown file in the workspace, named after the campaign, and show it to the user. Use this layout (the bracketed lines describe what goes there; they are not copy):

```
Campaign: [campaign name]
Offer: [one line, from the business context]
ICP: [one line, from the business context]
Lead fields used: [e.g. {{first_name}}, {{company_name}}, client type field]

STEP 1 (day 0)
Subject: [2–5 words, spintaxed, personalised]
Body:
[spintaxed greeting with {{first_name}}]
[spintaxed opening that shows relevance to this lead]
[spintaxed offer line]
[spintaxed proof line, only if an approved claim fits]
[spintaxed low-friction CTA]
[sign-off]

STEP 2 (day 3, same thread, no subject)
Body:
[spintaxed follow-up: extra info, extra credibility or a simple nudge]

Approved claims used: [each claim, and where in the business context it comes from]
Versions: Step 1 = [n], Step 2 = [n]
Questions for you: [any gaps, missing fields or claims that need approval]
```

## 9. Self-check before handing it back

Go through every line. Fix anything that fails, then hand the draft back with this checklist filled in.

- [ ] Offer, ICP and voice match the saved business context.
- [ ] Every claim is on the approved list. No invented numbers, results or names.
- [ ] Only clean fields are used: first name, cleaned company name and, if present, client type.
- [ ] Every lead has a first name; any gaps are reported.
- [ ] Two steps, 3 days apart, follow-up in the same thread.
- [ ] Subject line is 2–5 words, personalised, on topic, and sounds like a colleague.
- [ ] The CTA is low friction and doesn't try to close the sale.
- [ ] The follow-up adds something new.
- [ ] No links, images or formatting; no piles of dollar signs or dollar figures; no common spam words; nothing long-winded.
- [ ] About 90% of the script is spun in 2–5 word blocks, with 3,000+ versions.
- [ ] Every spintax combination reads correctly, and merge fields can't drop out.
- [ ] Spintax and merge fields use the sequencer's own syntax.
- [ ] If there are A/B variants: no more than two, same offer, one variable changed.

Optional: run the copy through a copy-checking tool such as EmailGuard before launch.

## 10. Approval and launch

- These are drafts. Never send, schedule or launch from this skill.
- The user reads and corrects the draft. Apply their corrections, and with their OK add any new rule to the Voice section of the business context so the next draft starts closer.
- The approved copy goes into the sequencer through the Cheap Sequencer campaign setup skill (or by hand). Once it's there, preview it and send a test email to check the spintax and merge fields render correctly. Launching stays the user's decision.

## 11. After the campaign

Feed the results back into the workspace and change one thing at a time based on what they show.

- Give a new campaign about 3,000–5,000 total sends before judging it.
- If replies are few but most of them are positive, the offer and targeting are probably right; rework the subject line and first line.
- A lot of "not interested" replies can mean the offer or the targeting is off.
