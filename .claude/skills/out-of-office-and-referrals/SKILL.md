---
name: out-of-office-and-referrals
description: Treat out-of-office and "talk to my colleague" replies as warm leads. Reads the reply, takes the return date or the named colleague from it, finds a verified email for the colleague, and drafts either an email to the colleague or a follow-up for when the person is back, tracked in a due list. Use when a reply is an auto-reply or a referral, or to work through follow-ups that are due; it never invents names or emails, and sends nothing without the owner's approval unless the owner has allowed that kind of email.
---

# Out-of-office and referrals

An out-of-office reply means your email reached a real person at a real company. A "talk to my colleague" reply hands you the right person. Both are warmer than a new cold lead, and most senders let them go to waste.

This skill handles both. It works one reply at a time, and it also works through the list of follow-ups that are due.

## 1. Read first

- `business.md`: the offer, voice and sign-off (sections 2, 11 and 12), and the booking rules (section 13), including which emails the owner lets you send without asking.
- The whole email thread, not just the last message.
- `leads/follow-ups-due.md`: follow-ups already waiting. Create it with the table in section 7 if it doesn't exist.
- `meetings/meetings.md`: to check the lead isn't already booked.

## 2. Sort the reply

Use only what the reply says. Copy the exact line you based the decision on into the due list.

| The reply says | Type | Go to |
|---|---|---|
| Away until a date | Out of office | Section 4 |
| Away, no date given | Out of office, no date | Section 4 |
| Away, and names someone to contact meanwhile | Referral | Section 5 |
| "Talk to [name]", "[name] handles this" | Referral | Section 5 |
| Has left the company, and names who took over | Referral | Section 5 |
| Has left the company, names nobody | Neither | Log it. Don't guess who replaced them |
| Anything else (interested, not interested, a question, an opt-out) | Not this skill | Follow the owner's reply rules. Opt-outs go on the do-not-contact list |

## 3. Check before you do anything

- **Do-not-contact:** the lead's address and its domain must not be on the do-not-contact list. Check again for any colleague you find.
- **Already talking:** if the lead or the company already has a meeting in `meetings/meetings.md`, or a live conversation in another thread, stop and tell the owner.
- **What happened to the sequence:** read the lead's enrollment in the campaign. Don't assume what an out-of-office reply did to it: depending on the sequencer and its stop rules it may have stopped, paused or carried on.
  - If it is still active and the next step would land while the person is away, tell the owner and suggest stopping that enrollment. Stopping it changes an active campaign, so the owner decides.
- **Tagging:** if the reply isn't tagged as out of office, suggest it. Ask first, because in some sequencers a tag also stops the lead.

## 4. Out of office

1. **Return date.** Take it from the reply. If the reply gives none, use the owner's default from `business.md`. If there is no default, ask the owner, and note "no date given".
2. **Due date.** By default this is the second working day after they're back, in their timezone, so the email doesn't sit at the bottom of a full inbox. The owner can change this default.
3. **Add a row** to `leads/follow-ups-due.md` (section 7).
4. **Draft the follow-up now**, so the owner can approve it once:
   - It is a reply in the same thread, from the same inbox that sent the campaign.
   - Keep it short. Mention that you wrote while they were away and repeat the point of the first email in one line. End with the same low-friction ask, or a specific time.
   - Leave the time as `[time: pick when sending]`. Calendars change, so the booking skill picks the actual time on the day you send.
   - Use the owner's voice and sign-off. Use only approved claims.
5. **Send nothing yet.** The due list sends it (section 6).

## 5. Referrals

1. **Who.** Take the colleague's name, and their role if the reply gives it. Never guess a name.
2. **Their email.**
   - If the reply gives the address, use it.
   - If not, look it up with the connected enrichment tools. A paid lookup spends credits, so ask the owner first unless they have already approved it.
   - Run the address through the email verifier. Use it only if the verifier says it's valid.
   - Never send to a guessed pattern such as firstname@company. If you can't find a valid address, draft a short reply to the lead asking for it, or ask the owner.
3. **Draft the email to the colleague.** Two ways to do it:
   - **Forward (default):** a new email to the colleague, from the same inbox as the thread. Start with a short note naming who pointed you to them, using the lead's own words where possible, then put the original email below it.
   - **Reply with the colleague in cc:** reply in the lead's thread, thank them, and copy the colleague in. This works well when the lead offered to introduce you.
   - In either case, end with one specific time from the booking skill, and log it in `meetings/offered-times.md`.
4. **Thank the lead** in one line if you used the forward. Fold it into the cc reply if you used that.
5. **Log it.** Add a row to `leads/follow-ups-due.md` with type "referral", the colleague's details, where the email came from, and the verifier's result.

## 6. Work through the due list

Run this daily. It's a good one to set up as a scheduled task in your agent, because nothing else will remind you.

For each row that is due today or earlier and still "waiting":

1. Re-read the thread. If the person has already replied, close the row as "replied" and handle the reply normally.
2. Check do-not-contact again.
3. Ask the booking skill for a time and put it in the draft.
4. Send it if the owner approved this draft, or has allowed this kind of email in `business.md`. Otherwise show the owner the draft and wait.
5. Mark the row "sent" with the date. If there's still no reply after that, leave it. Don't chase further outside the sequence unless the owner asks.

## 7. The due list

`leads/follow-ups-due.md`, one row per follow-up. The booking and call prep skills read it too, so keep these columns:

```
| Due | Type | Lead | Company | Campaign | Thread | Inbox | Colleague (name, email, how found, verifier result) | From the reply (exact line) | Draft | Status |
|---|---|---|---|---|---|---|---|---|---|---|
```

Type is "out of office" or "referral". Status is waiting, sent, replied, cancelled or needs owner. Draft is the path to the draft file, or "inline".

## 8. Cheap Sequencer calls

If your sequencer is Cheap Sequencer, these API calls do each step. They were taken from its public OpenAPI file in November 2026. Check the live schema before any write. The required scope is listed for each call.

| Step | Call | Scope |
|---|---|---|
| Find and read replies | `GET /inbox/threads` (filter `classification=out_of_office`), `GET /inbox/threads/{threadId}` | messages:read |
| Check do-not-contact | `GET /suppressions?search=` | suppressions:read |
| Read the enrollment | `GET /campaigns/{id}/enrollments` | sequences:read |
| Stop one enrollment (owner OK) | `POST /campaigns/{id}/enrollments/{enrollmentId}/stop` | sequences:write |
| Tag the reply (owner OK) | `POST /inbox/messages/{messageId}/classification` with `out_of_office` | messages:write |
| Reply in the thread, optionally with cc | `POST /inbox/threads/{threadId}/reply` (`body_text`, `cc`) | messages:write |
| Add the colleague as a lead | `POST /leads` | leads:write |
| Send the forward from the thread's inbox | `POST /leads/{id}/send` (`inbox_id`, `subject`, `body_text`) | sequences:send |

Cheap Sequencer has no scheduled send through the API. That's why the due list exists.

## 9. Approval

- Everything is a draft by default. Send without asking only the kinds of email the owner has listed in `business.md` section 13.
- Price, terms or commitments in a reply go to the owner.
- Any paid lookup needs the owner's OK unless they have already approved it.

## 10. Self-check

- [ ] The type comes from an exact line in the reply, copied into the due list.
- [ ] The lead, the domain and any colleague were checked against do-not-contact.
- [ ] Enrollment state was read, not assumed. The owner decided on any stop.
- [ ] Every colleague address came from the reply or from the verifier as valid. No guessed addresses.
- [ ] Each draft is short, in the owner's voice, uses only approved claims, and goes out from the same inbox as the thread.
- [ ] Every time offered is logged in `meetings/offered-times.md`.
- [ ] Nothing was sent that the owner hasn't approved or allowed.
- [ ] A log of the work is saved in `logs/`.
