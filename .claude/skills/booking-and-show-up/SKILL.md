---
name: booking-and-show-up
description: Offer interested leads one specific meeting time, book it, confirm it, and track whether the meeting was held. It keeps one shared log of offered times so two leads never get the same slot, offers only working-day times inside the owner's booking window, converts to the lead's timezone, releases held times, sends a short confirmation before each call, and drafts a one-line rebook for no-shows. Use when a lead wants to talk, when another skill needs a time to offer, before upcoming calls, or after a call to record held or no-show; it never books outside the owner's rules or invents a booking link.
---

# Booking and show-up

A booked call that doesn't happen is worth nothing. This skill does both halves: it gets the call booked, then gets the person to turn up. It also tracks meetings **held**, not just booked, because held calls are what turn into customers.

## 1. Read first

- `business.md` section 13: how meetings get booked, the booking link, the owner's timezone, the days and hours they take calls, how far ahead they'll book, who else takes calls, what to confirm, and which emails you may send without asking.
- `meetings/offered-times.md` and `meetings/meetings.md`. Create them with the tables in section 7 if they don't exist.
- The owner's calendar or booking tool, through whatever is connected (Google Calendar, Outlook, Calendly, Cal.com and so on). Check the free times live, every time.

If section 13 is empty, ask the owner for the missing rules before offering any time.

## 2. Pick one time to offer

Offer **one specific time**. That's easier to say yes to than a list or a bare link.

A time is allowed only if:

- It is free in the owner's calendar right now.
- It falls on the owner's call days and hours, on a weekday unless the owner says otherwise.
- It is within the owner's booking window. If they haven't set one, use about 7 business days, because calls booked further out tend not to happen.
- It is at least one working day away, unless the lead asked for sooner.
- It isn't held for another lead in `meetings/offered-times.md`.

**Timezone.** Work out the lead's timezone from what you know: their reply, their signature, their location in the lead list or their company's address. Write the time in their timezone with the zone named, for example "Tuesday 10 am Central". If you can't tell where they are, name the owner's timezone in the email instead. Don't assume.

**The email.** One line with the time, and the owner's real booking link as a fallback ("or pick another time here") only if `business.md` has one. Never make up a link.

**Hold it.** Add a row to `meetings/offered-times.md` with the time in the owner's timezone, the lead, the thread and a hold-until date. By default a hold lasts 2 working days; the owner can change that.

## 3. When the lead answers

| The lead | Do this |
|---|---|
| Accepts the time | Book it (below) |
| Suggests another time | Check it against section 2. If it's allowed, book it. If not, offer the nearest allowed time |
| Sends their own booking link | Book through their link if `business.md` says that's fine, or ask the owner. Booking through their link still counts as booking from your side |
| Asks a question first | Answer it only from `business.md`. Price, terms or commitments go to the owner |
| Goes quiet | Let the hold expire. Don't chase outside the sequence unless the owner asks |

**Booking it:**

1. Create the event through the connected booking tool or calendar. Invite the lead and anyone else the owner named, and include the real meeting link.
2. Confirm once in the thread: day, time in their timezone, how you'll meet, and what the call is for.
3. Move the row from `offered-times.md` to `meetings/meetings.md` with status "booked". Release any other holds for this lead.
4. Tell the call prep skill a meeting is booked, or run it if the owner wants a brief.

**Releasing holds.** Each time you run, mark holds past their hold-until date as "released". Release a hold straight away if the lead declines or books a different time.

## 4. Before the call

Send a short confirmation before each call. By default that's the morning of the call, or the working day before for an early call; the owner can change this. It goes as a reply in the same thread, with:

- the day and time in their timezone
- what the call is for, in one line
- how you'll meet

Send one confirmation, not a series. If the lead has already confirmed, don't send another.

## 5. After the call time

Record what happened in `meetings/meetings.md`. Don't assume a booked call was held.

- **Held:** the owner says so, the call recorder has a recording with the lead in it, or the calendar shows they joined.
- **No-show:** the owner says they didn't turn up.
- **Cancelled or moved:** the lead cancelled or moved it. Update the row.
- **Not sure:** ask the owner.

**No-shows.** Draft one short rebook as a reply in the same thread. No guilt-tripping. For example, say "Looks like today didn't work out" and offer one new time from section 2. Send only one rebook. If they don't answer it, mark the row "no-show, no reply" and stop.

## 6. Numbers

When the owner asks, report them from `meetings/meetings.md` for the period they name:

- booked, held, no-show, cancelled
- show-up rate = held ÷ booked, counting only calls whose time has passed
- booked per positive reply, if the reply counts are available

Use only the counts in the log. If rows are missing an outcome, say how many instead of guessing.

## 7. The two logs

The out-of-office, call prep and revival skills use these too, so keep the columns the same.

`meetings/offered-times.md`:

```
| Time (owner's timezone) | Lead's timezone | Lead | Company | Thread | Offered on | Hold until | Status |
|---|---|---|---|---|---|---|---|
```

Status is held, booked, released or declined.

`meetings/meetings.md`:

```
| Date and time (owner's timezone) | Lead | Company | Campaign or source | Thread | Booked on | Confirmation sent | Outcome | Brief | Notes |
|---|---|---|---|---|---|---|---|---|---|
```

Outcome is booked, held, no-show, no-show rebooked, no-show no reply, cancelled or moved. Brief is the path to the call prep brief.

## 8. Approval

- Time offers, confirmations and rebooks are drafts unless the owner has listed them in `business.md` section 13 as emails you may send on your own.
- Creating a calendar event or a booking for the owner follows the same rule.
- Never book outside the owner's days, hours or window. Never offer a time that isn't free, and never use a link that isn't real.

## 9. Self-check

- [ ] Every time offered was free in the calendar when checked, within the owner's rules, and not held for anyone else.
- [ ] The time is written in the lead's timezone with the zone named, or the owner's timezone is named if theirs is unknown.
- [ ] Every offer is logged with a hold-until date, and expired holds are released.
- [ ] Booked meetings are in `meetings/meetings.md`, and other holds for that lead are released.
- [ ] One confirmation per call, in the same thread.
- [ ] Held or no-show is recorded from evidence or from the owner, never assumed.
- [ ] No-shows got at most one rebook.
- [ ] Nothing was sent or booked that the owner hasn't approved or allowed.
