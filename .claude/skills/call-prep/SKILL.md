---
name: call-prep
description: Write a one-page brief before each sales meeting. It covers who the person and company are, using connected sources only, their exact words from the email thread, likely objections with the owner's answers, questions to ask, and three points to push, with every inference marked. Use when a meeting is booked, the day before a call, or when the owner asks to prep for a call; it never invents facts or quotes.
---

# Call prep

Walk into every call knowing who you're talking to, what they already said and what they're likely to push back on. The brief takes the agent a few minutes and the owner two minutes to read.

## 1. When to run it

- When a meeting lands in `meetings/meetings.md` with no brief yet.
- On the working day before each call, to catch new replies.
- Whenever the owner asks.

## 2. Gather from connected sources only

Read each of these if it exists. If a source is blocked or won't load, say so in the brief instead of filling the gap from memory.

| Source | What to take |
|---|---|
| `meetings/meetings.md` | When, who, how you'll meet, which campaign it came from |
| The email thread (sequencer inbox or mailbox) | What we sent, and what they wrote, word for word with dates |
| The lead list in `leads/` | Their row: role, company, location, and the qualification reason with its source page |
| The company's website | What they do, who they serve, where they operate, size if stated |
| The CRM, if connected | Past contact, deals, notes |
| The call recorder, if connected | Any earlier calls with this person or company |
| `business.md` | The offer, the ICP, objections and answers, approved claims, deal size, what happens on the first call |

Search the web only for the company's own pages and public profiles. Don't pull in personal social media or anything about the person's private life.

## 3. Write the brief

Keep it to one page. Use this layout (the bracketed lines describe what goes there):

```
# [Company]: [person], [day, date, time in the owner's timezone]

How: [meeting link or phone, from the calendar]
From: [campaign or source], booked [date]

## Who they are
- Person: [name, role, from source]
- Company: [what they do, who for, where, size if known, from source]
- Why they fit: [ICP match and the qualification reason, with the page it came from]

## What they said
- "[exact quote]" ([date])
- "[exact quote]" ([date])

## Likely objections
- [objection]: [the owner's answer from business.md] ([why it's likely: quote, or "inference"])

## Ask them
- [question that finds out whether the offer fits]
- [question about timing, budget or who decides, matched to the first call in business.md]

## Push these three
1. [point tied to the offer and something they said or that the site shows]
2. [...]
3. [...]

## Unknowns
- [what you couldn't find or confirm]

Sources: [links and files used]
```

## 4. Rules

- **Quotes are exact.** Copy them from the thread with the date. Never paraphrase inside quote marks.
- **Mark inferences.** Anything you worked out rather than read, write "(inference)" after it. Examples: their likely budget, who else decides, why they replied.
- **Only approved claims** in "Push these three". If a point needs proof that isn't in `business.md`, say so.
- **Objections** come from the owner's list in `business.md` first. Add a new one only if the thread or site points to it, and mark it "(inference)".
- **No padding.** If a section has nothing real in it, write "nothing found" instead of filling it.

## 5. Save and hand over

1. Save it as `meetings/briefs/YYYY-MM-DD-company.md`.
2. Put the path in the meeting's row in `meetings/meetings.md`.
3. Tell the owner it's ready. If they have set up a channel for this (Slack, email to themselves), post it there. That message only goes to the owner, never to the lead.

## 6. Self-check

- [ ] Every fact names its source. Every quote is exact and dated.
- [ ] Inferences are marked "(inference)".
- [ ] Blocked or missing sources are listed under Unknowns.
- [ ] Objection answers and pushed points use only what's in `business.md`.
- [ ] Nothing about the person beyond their work.
- [ ] One page, saved and linked in `meetings/meetings.md`.
