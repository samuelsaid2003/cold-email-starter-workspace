---
name: list-building
description: Build a cold email lead list from scratch for a target market. Picks the best sources for the ideal customer (niche directories, Google Maps, ad libraries, lead databases) using whatever tools are connected, collects and dedupes companies, finds their websites, hands them to qualification, finds decision-maker contacts, verifies the emails and writes an upload-ready CSV. Use when asked for a new list or "leads for a new campaign"; not for writing copy or launching campaigns.
---

# List building

Turn a request like "500 commercial cleaners in Texas" into a CSV of verified decision-makers at companies that fit the offer, ready to upload to your sequencer.

The order matters. Check each company's website against the ideal customer **before** paying to find its contacts, so credits only go on companies that fit.

```
pick sources → collect companies → dedupe and exclude → find websites
→ qualify (qualification skill) → find decision-makers → verify emails
→ clean company names (company-name-cleaning skill) → upload-ready CSV
```

## Before you start

Read `business.md` in the workspace root: the offer, the ideal customer, who the buyer is and the geography. If there is no ideal customer saved, run the **business-interview** skill first. A list built without one is guesswork.

Confirm these from the request, or ask once if they are missing:

- **Market:** the type of company, in plain words (for example "commercial cleaning companies").
- **Geography:** the country, states or cities.
- **Size:** how many leads are wanted. On a first run, build a small batch of about 100 and check it before scaling up.
- **Tools:** check which lead sources, enrichment tools and email verifier are connected. Use those. If a step has no tool, say so and suggest the type of tool needed. Don't sign up for anything.

## Rules

- **Ask before spending money.** Most sources and enrichment tools spend credits. Before a paid step, say which tool, roughly how many records and what it will cost if the tool shows it. Free work (research, browsing public pages, deduping, writing files) needs no approval.
- **Don't contact anyone.** This skill builds a list. It never sends email, submits enquiry or quote forms, or launches a campaign.
- **Browse like a person.** Use the user's own logged-in browser where a site needs a login, and never type in passwords. Keep a normal pace. If a CAPTCHA, security check or "temporarily blocked" page appears, stop and tell the user. Never try to get around it. Follow each site's terms.
- **Keep the evidence.** For every company, record where it came from (source and page URL) and the date. Keep rows you removed in a separate file with the reason, so nothing disappears silently.
- **Don't invent data.** Leave unknown fields blank and say why. Never guess an email, complete a masked phone number or make up a website from a company name.
- **Keep lead files private.** Save them in the workspace's private data folder, not in shared docs or chat.

## 1. Pick the sources

Use whichever source has the most relevant companies for this market. Work it out with research rather than habit.

The main source types:

| Source type | What it's good for | Watch out for |
|---|---|---|
| **Niche directories** (industry and trade directories, association member lists, local business directories) | Small local and trade businesses that may not show up in lead databases | Often no website or email on the listing. A directory profile link is not the company's website |
| **Google Maps / Business Profiles** | Local service businesses in a set area, with phone, address, category and often a website | A single search returns a capped number of results, so split big cities into smaller areas. Categories are loose, so expect unrelated businesses |
| **Ad libraries** (for example the Meta Ad Library) | Companies actively running ads, which shows they spend on growth | Many advertisers are off-target. Filter out hiring and recruitment ads. Ads roll up to a Page, not a company website |
| **Lead databases** (company and contact search tools) | Fast filtering by industry, location and headcount, often with contacts attached | Industry labels are loose and small local businesses are often missing. Test the filters before trusting them |

How to choose:

1. Research where companies in this market are listed in this geography. Search for niche directories, association lists and relevant categories.
2. For each candidate source, estimate how many relevant companies it holds. Use the result count the site shows, or count a few pages.
3. Look at a sample of 10–20 results from each source and note how many actually fit the ideal customer.
4. Show the user a short table (source, estimated relevant companies, fit in the sample, cost) and recommend one to three sources. Combining sources gives more coverage. The dedupe step handles overlap.

## 2. Collect companies

Capture the same fields from every source so they can be merged:

`company_name, website, phone, address, city, state, country, category, source, source_url, date_collected`

Add any extra field the source gives that helps qualification, such as the listing's description or service list.

- Read the list or search-results pages first. Open individual profiles only when a field you need isn't on the list.
- Go through every page of results until the source runs out or the agreed limit is reached. If a search hits a result cap, split it (smaller area, narrower term) and say which searches stayed capped.
- Use exact search terms for the market. Broad terms pull in unrelated companies, so keep track of which terms they came from.
- In an ad library, keep advertisers whose ads are active, have been running for a while and aim to win customers. Drop hiring and recruitment ads.
- In a lead database, test the filters on a few companies you already know fit. If they don't come back, adjust the filters before pulling the full list.
- Save as you go so a long run can resume without starting over.

## 3. Dedupe and exclude

- Remove exact duplicates within each source by its own profile ID or URL.
- Merge across sources by website domain. Treat a shared phone number or similar name as a possible match to check, not an automatic merge. Branches and franchises often share them.
- Remove companies the user must not contact: existing customers, companies already in another campaign, and anyone on the do-not-contact or bounce lists. Ask for those lists if they aren't in the workspace. Your sequencer may also offer an import option to skip leads already in other campaigns. Use it as a second check.
- Write removed rows to `removed.csv` with the reason.

## 4. Find missing websites

Qualification needs a website, so recover the ones the sources didn't give. Try the free routes first:

1. The listing itself: an outbound website link on the directory or Maps profile.
2. A guessed domain from the company name, checked by visiting it.
3. A Maps or business lookup for the name and city.
4. A web search for the company name plus city, or plus its phone number.

A candidate counts as confirmed only when the site matches on name **and** at least one more detail: phone, address, city, or a business or licence number. Generic names (for example "Pro Cleaning Services") cause most wrong matches, so be strict with them. A social media page or directory profile is not the company website. Record it separately.

Mark each company `confirmed`, `likely` or `not_found`. "Not found" means no site was confirmed within the checks done, not that none exists. Send only confirmed websites on to qualification. Keep the rest in `no-website.csv` for the user to decide.

## 5. Qualify (hand off)

Run the **qualification** skill on the companies with confirmed websites. It checks each website against the ideal customer saved in the workspace and returns pass, fail or unsure, with a reason. Only companies that pass go on to contact finding. Show the user the unsure ones and let them decide.

If the qualification skill isn't installed, do the basic version: read each homepage and services page, identify what services the company offers, and decide whether it fits the offer. Then double-check your decisions against the ideal-customer criteria before moving on.

## 6. Find decision-makers

Find the person who would buy the offer, usually the owner, founder, managing director or general manager in a small business. Take the target roles from the ideal customer in the workspace.

Use a **waterfall**: run the first contact source on every qualified company, then run a second source only on the companies the first one missed. Add a third only if the gap is still large and the user approves the spend. (On stage: a lead database first, a second enrichment tool for the misses. Any equivalent tools work.)

For each contact, capture:

`first_name, last_name, title, email, linkedin_url (if given), company_website, contact_source`

- **First name is required.** A lead with no first name is not sent. Keep it out of the upload file.
- **Skip role addresses** such as info@, sales@, office@ or admin@. They tend to be catch-all or don't reach a decision-maker.
- Keep the contact tied to the right company. Check the email domain matches the company website, or note why it doesn't.
- If the user hasn't said how many contacts to take per company, ask before enriching more than one.

## 7. Verify the emails

Run every email through the connected email verifier.

- **Valid:** keep.
- **Catch-all or unknown:** run these through a catch-all verifier if one is connected. Keep only the ones that come back valid.
- **Everything else** (invalid, risky, unknown, catch-all that didn't pass): remove, and write it to `removed.csv` with the verifier's result.

Never send to catch-all or unknown addresses that haven't been confirmed valid. Unverified leads are the usual cause of bounces.

## 8. Clean company names (hand off)

Run the **company-name-cleaning** skill on the final list. It turns names like "ACME COMMERCIAL CLEANING SERVICES LLC" into the name a person would write by hand in an email, and keeps the original in its own column.

## 9. Write the upload-ready CSV

Write `leads-upload.csv` with one row per verified contact:

| Column | Notes |
|---|---|
| `email` | Verified valid only |
| `first_name` | Required |
| `last_name` | |
| `company_name` | Cleaned name, used in the email |
| `original_company_name` | As the source listed it |
| `title` | |
| `website` | Confirmed website |
| `phone` | Kept as text, as listed |
| `city`, `state`, `country` | Used to set the campaign timezone |
| `source`, `source_url` | Where the company came from |
| `verification_status` | Result from the verifier |

Add any personalisation field the copy will use, such as the lead's likely client type, as an extra column.

Check before handing over:

- Every row has an email, a first name and a valid verification status.
- No email or company domain appears twice.
- No row matches the exclusion lists.
- The file opens cleanly (UTF-8, header row, phone numbers not turned into numbers).

## Report back

Give the user a short summary:

- Sources used, and why they were chosen.
- A funnel with real counts at each step: companies collected, after dedupe and exclusions, with confirmed websites, qualified, with a decision-maker found, verified valid, and in the final file.
- Credits or money spent, per tool, where the tool shows it.
- What's left: capped searches, companies with no website, misses from contact finding, and anything that needs a decision.
- The files: `leads-upload.csv`, `removed.csv`, `no-website.csv`.

Then stop. Uploading the list and building the campaign is the job of the Cheap Sequencer campaign setup skill, and launching it needs the user's approval.

## Example request

> Build a new campaign targeting commercial cleaners in Texas. Scrape the best directories, enrich the leads and get them ready to push into a new campaign. Start with about 100 leads.

The agent researches where Texas commercial cleaning companies are listed, proposes the sources, collects and dedupes the companies, finds their websites, qualifies them, finds and verifies the owners' emails, cleans the names and returns the CSV with a funnel report.
