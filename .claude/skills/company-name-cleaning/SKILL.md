---
name: company-name-cleaning
description: Clean company names in a lead list so cold emails read as if written by hand. Takes a lead CSV and returns a CSV with a cleaned "Company Name" column and the untouched "Original Company Name" column, every other column and row unchanged. Works with any sequencer. Use for company-name cleanup before a campaign upload, not for finding leads, verifying emails or qualifying companies.
---

# Company name cleaning

Lead databases and directories give you registered or listing names: "Acme Plumbing Services Pty Ltd", "ACME ROOFING - Roof Repairs & Restorations | Call Today". Nobody types that into an email they wrote themselves. If the merge field drops it into your first line, the reader knows it's a mail merge.

This skill turns every company name into the short name you would say out loud, keeps the original next to it, and changes nothing else in the file.

## The one rule

**What would you call this company in a conversation?** Use the shortest name the owner would recognise as theirs. Not a tidied-up version of the full registered name.

## How to clean a name

Remove:

- Legal suffixes: Pty Ltd, Ltd, Limited, LLC, Inc, Corp, GmbH, Co.
- Taglines and service lists after " - ", " | ", ":" or in brackets: "Acme Roofing - Roof Repairs & Restorations" → "Acme Roofing".
- Branch or location qualifiers: "Acme Electrical Northside" → "Acme Electrical". A town on the end is a branch, not part of the brand.
- State and region codes such as NSW, QLD or TX: "Acme Solar QLD" → "Acme Solar".
- Filler such as Group, Holdings, Contractors, Contracting or a country name, when the rest stays recognisable: "Acme Financial Group" → "Acme Financial".
- Trailing full stops.

Keep:

- A distinctive brand on its own: "Zentrix Air Conditioning & Electrical Solutions" → "Zentrix".
- The trade word when the rest is a surname or a common word: "Smith Homes" stays "Smith Homes", not "Smith". A name made only of common words, such as "Power Solutions", must not become "Power".
- A region code when removing it leaves a generic phrase: "Roof Restorations TX" stays, because "Roof Restorations" alone is just a description.
- "The" when it is part of how people say it: "The Acme Collective".
- Acronyms, initials and stylised spelling: "HVAC", or a brand the company writes as "eAcme". Don't blindly title-case or expand initials.
- The business, not the person, when a page name has both: "Jane Citizen [Acme Coaching]" → "Acme Coaching".

Fix capitals only where the source is shouting: "ACME HOMES" → "Acme Homes". If the source name looks misspelt, the company's own website domain can settle it.

Read each result as spoken language. Length is a signal to look again, not a hard limit.

## Watch out for

- **Suggested "company name for emails" columns.** Some lead databases add one. Treat it as a machine guess, not an answer. Common faults: cutting real words it mistakes for suffixes ("Smith & Co Brokerage" → "Smith &"), dropping the first word of a brand, fusing "Pty" onto a word, and title-casing acronyms ("HVAC" → "Hvac"). Start from the original name and overwrite that column with your reviewed names.
- **Same short name, different companies.** Two rows that both clean to "Acme Electrical" may be separate branches or separate businesses. Keep every row.
- **Removing a company is not a name edit.** If a company shouldn't be emailed, take it out of the list as a separate step. Don't blank or alter its name.

## Working method

1. **Look at the file first.** Check the real headers and find the original company-name column.
2. **Work on distinct names, not rows.** List each distinct original name once, clean it, then map it back to every row with that exact original value. Never match by row position or by "looks similar".
3. **Review every name.** Check each cleaned name for over-shortening, broken acronyms, a lost brand and wrong pairings. A matching row count does not prove each name went to the right row.
4. **Apply only the name change.** Don't drop, dedupe, filter or reorder leads. This is a naming step.
5. **Read the output back** and check it against the input (see Final checks).

### With the helper script (Claude Code, Codex or any agent that can run Python 3)

`scripts/clean_names.py` uses only the Python standard library and needs no accounts or config.

```bash
python3 scripts/clean_names.py extract leads.csv mapping.csv
```

This writes `mapping.csv` with one row per distinct original name: `original_name`, `rows`, `clean_name` and `flags`. `clean_name` holds a rough rule-based first pass (suffixes, taglines, brackets, shouting caps). `flags` points at likely problems. The first pass is a starting point only: go through every row, apply the rules above and edit `clean_name`.

```bash
python3 scripts/clean_names.py apply leads.csv mapping.csv leads_clean.csv
```

This writes the final CSV, reads it back and stops with an error if any original name, other column or row count changed. It refuses to run if a name in the list is missing from the mapping or has an empty `clean_name`. It prints the distinct names changed and the rows affected.

If the original column isn't recognised, add `--original-column "Your Column Header"` to both commands.

### Without the script (chat-only assistants)

Do the same steps by hand: make a two-column table of each distinct original name and its cleaned name, review it, then add the cleaned names to the sheet with a lookup on the exact original value (for example `XLOOKUP` or `VLOOKUP` in a spreadsheet). Then rename the columns as below.

## Output CSV

| Column | Contains |
| --- | --- |
| Company Name | The cleaned name. This is the one your merge field uses. |
| Original Company Name | The original value, character for character. |

How the headers are handled:

- **Only an original name column** (for example "Company Name" or "Company"): it is renamed "Original Company Name" and a new "Company Name" column with the cleaned names goes just before it.
- **An original column plus a suggested column** (for example "Company Name" plus "Company Name for Emails"): the original becomes "Original Company Name" and the suggested column becomes "Company Name", filled with your reviewed names. Rename both together so you never end up with two "Company Name" headers.
- **Already in this format** (a previous run): keep it. "Original Company Name" stays the source. Never swap the meanings on a second run.
- **Not sure which column is which:** stop and check where the file came from before changing anything.

Every other column and value stays exactly as it was. Save as UTF-8 with a proper CSV writer so commas, quotes, accents and line breaks inside values survive.

Rows with no company name keep an empty "Company Name". Report how many there are. Make sure your copy reads fine without it, or decide whether those leads belong in this campaign.

## Final checks

Before you call the file ready:

- Headers are unique and the row count and order match the input.
- Every non-name column is unchanged, and "Original Company Name" equals the input value on every row.
- Each "Company Name" equals the reviewed name for that row's original.
- The file has a column for every merge field your approved copy uses. Name any that are missing. Don't invent values for them.

Report the output path, the number of distinct names changed and the number of rows affected, as separate counts.
