---
name: business-interview
description: Interview the business owner one question at a time about their business, offer, ideal customer, voice, claims, proof, past campaigns, booking rules and standing rules, and save every answer to the workspace's business context file. Use when setting up a new cold email workspace, when the agent doesn't know the business ("who am I?"), to resume a half-finished interview, or when the owner wants to update an answer.
---

# Business interview

The agent can only write good outreach if it knows the business. This skill gets that knowledge from the owner by asking one question at a time and saving each answer straight into the workspace. Bad brief in, bad drafts out.

## Files

- **Context file:** `business.md` in the workspace root. If the workspace's AGENTS.md names a different context file, use that instead.
- **Template:** `templates/business-context.md` next to this skill. Copy it to the context file on the first run.
- If you can't write files in this setup, keep the filled template in the chat and give the owner the full file to save at the end of each sitting.

## Start: work out which mode you're in

1. Look for the context file.
2. **No file:** this is a new interview. Copy the template to the context file, tell the owner it takes a few minutes per section and they can stop at any time, then start at section 1.
3. **File exists, some sections not Done:** this is a resume. Read the file, read the *Interview progress* table and tell the owner in one or two lines what's done and what's left. Continue from the first section that is *In progress* or *Not answered yet*. Don't re-ask anything already answered.
4. **Owner asks to change something:** this is an update. See *Updating answers later*.
5. **Every section is Done or Skipped:** say so, list any **(guess, confirm)** items still open, and ask if they want to update anything.

If the owner has a website, sales deck, past emails or campaign exports, ask for them up front. You can draft answers from those, but every drafted answer is marked **(from source: ...)** and read back for the owner to confirm before it counts as Done.

## How to ask

- One question per message. Wait for the answer before the next one.
- Keep each question short and plain. You can reword a question to fit what the owner has already said.
- Never suggest an answer, give an example answer, or fill a blank with what's typical for the industry. If the owner asks for an example, say you'll use their real material instead and ask for it.
- If an answer is vague, ask one follow-up for the specific version (who exactly, how many, which link). Then move on.
- If the owner doesn't know, write "Owner doesn't know yet" and move on. If they don't want to answer, mark it **Skipped**. If it isn't relevant, mark it **Doesn't apply**.
- The owner can say "skip", "come back to this", "stop" or "pause" at any time.

## How to save

- Save after every answer, before asking the next question. Don't batch answers up, because the session can end at any time.
- Write the owner's words, lightly tidied. Don't upgrade them: no added numbers, adjectives or claims.
- Anything you inferred rather than heard gets **(guess, confirm)**. Read guesses back at the end of the section.
- Paste voice samples and sign-offs exactly as given. Never edit them.
- Only record a link the owner gave you or one you opened and confirmed exists. Never construct a link.
- Results from past campaigns are owner reports unless an export is attached. Record which one it is.
- When a section is finished, set its status in the *Interview progress* table to Done and fill *Last updated* with today's date. A section you've started but not finished is *In progress*.
- Keep secrets out of the file: no passwords, API keys or tokens. If the owner pastes one, don't save it and tell them why.

## The interview

Go in this order. Sections 1–3 and 11 are the minimum for a first useful pass; if the owner is short on time, do those first and come back for the rest.

### 1. What the business does
- What does the business do, in a sentence or two?
- Who does it serve?
- Where does it operate?
- What's the website?

### 2. The offer
- What does a new customer get when they buy?
- What result does that lead to for them?
- What does it cost, or how is it priced?
- What can the agent say about price in outreach and replies? Or should every price question come to you?
- Is there a guarantee, trial or other way you take on the risk? (Only record one that really exists.)
- What makes this different from what they'd otherwise use or do?

### 3. Ideal customer (ICP)
- Which industries are you going after?
- What size of company?
- Which locations?
- Which job titles should the emails go to?
- What tells you a company is a good fit before you talk to them?
- What do your best current customers have in common?

### 4. Who to skip
- Which industries, company types or sizes should never be contacted?
- Which job titles or address types should be skipped?
- Are there existing customers, partners or competitors to exclude? Where's that list?
- Do you have a do-not-contact list? Can you export it into this workspace?
- Anything else that rules a lead out?

### 5. Pains, objections and buying triggers
- What problems does your ideal customer have that the offer solves?
- What objections do you hear most? How do you answer each one?
- What events or signs mean a company needs you right now?

### 6. Claims you can make
- What can you truthfully claim about the business or its results? What backs each claim?
- What must the agent never claim or promise?
- Any words, topics or competitors to avoid mentioning?

### 7. Approved proof
- Which results, testimonials or case studies are you happy for outreach to use?
- For each one: where's the source or link, and can the client be named?

Only proof the owner approves goes in this section. Ask for the source of each item; if there's no source yet, mark it **(guess, confirm)** and don't treat it as approved.

### 8. Deal size and the first call
- What's a typical deal worth?
- Do customers stay or buy again? Roughly how much is a customer worth over time? (Fine to say "don't know".)
- What do you call the first call with a prospect?
- How long is it, and what happens on it?
- Who takes it?

### 9. Markets being tested
- Which markets or segments are you testing right now?
- For each one: what angle or offer are you using, and is it testing, working or dropped?

### 10. Past campaigns
- What cold email campaigns have you run before?
- For each one: when, who it targeted, the angle, and what happened.
- What worked, and what didn't?
- Can you export the copy and results into this workspace?

If the owner gives numbers from memory, record them as owner reports. If they can export the results, ask for the export and note where it's saved.

### 11. Voice
- How do you want your emails to sound?
- Which words or phrases do you use a lot?
- Which words, phrases or styles do you never want to see?
- Any preferences on length, formality or formatting?

### 12. Voice samples and sign-off
- Paste two or three emails or messages you wrote yourself that sound like you.
- What name and title should the emails come from?
- How do you sign off? Type it exactly as you want it.

### 13. Booking rules
- How do meetings get booked: your booking link, your calendar, or the prospect's own link?
- What's the booking link?
- What timezone are you in?
- Which days and hours do you take calls?
- How far ahead are you willing to book?
- Can anyone else take calls?
- What should be confirmed with the prospect once a call is booked?
- Which replies should come to you instead of being answered for you?
- Which of these may the agent send without asking you first: out-of-office follow-ups, referral emails, time offers, booking confirmations, no-show rebooks? (Default: none, everything comes to you as a draft.)
- How long should a time you've offered stay held for that lead? (Default: 2 working days.)
- When should the confirmation go out before a call? (Default: the morning of the call.)
- If someone's out of office with no return date, when should the agent follow up?
- Where should call briefs go: just saved in the workspace, or also sent to you somewhere, such as Slack or email?

### 14. Standing rules
The template already holds three rules that apply to every task: only real links, flag guesses, and ask for an export when a source is blocked. Read them to the owner, then ask:
- Are there any other rules every task in this workspace should follow?

## Finishing a sitting

1. Read back a short summary of what was saved this sitting.
2. List open items: anything **(guess, confirm)**, "Owner doesn't know yet", or Skipped. Ask the owner to confirm or correct guesses now if they have time.
3. Check that the workspace's AGENTS.md tells agents to read the context file before any task. If it doesn't, ask the owner before adding that line.
4. Suggest a check: open a new session and ask "who am I?". The agent should answer from the context file.

## Updating answers later

When the owner says something has changed ("we've raised prices", "update the ICP", "add this case study"):

1. Show what the file says now for that section.
2. Ask what's changed, one question at a time.
3. Replace the old answer. Don't keep both versions in the section.
4. Add a row to the *Change log*: date, section, and a one-line summary of the change.
5. If the change contradicts another section (a new price that clashes with a claim, a dropped market still listed as testing), point it out and ask how to fix it.

If, during any other task, the agent learns something that conflicts with the context file, it should flag it to the owner and suggest an update, not edit the file silently.

## Standing rules for this skill

- **Only real links.** Never make up a URL, booking link or proof link.
- **Flag guesses.** Anything not confirmed by the owner or a named source is marked **(guess, confirm)**.
- **Ask for an export when a source is blocked.** If a website, document or tool can't be opened, say what failed and ask the owner for an export or a paste. Never fill the gap from memory.
- **No invented answers.** If it isn't in the owner's words or a source they gave you, it doesn't go in the file.
