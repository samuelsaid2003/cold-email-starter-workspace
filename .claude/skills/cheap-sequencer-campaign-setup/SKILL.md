---
name: cheap-sequencer-campaign-setup
description: Set up a Cheap Sequencer campaign as a draft through the Cheap Sequencer API, using the owner's own API key. It uploads a prepared lead CSV, picks inboxes that aren't already sending, adds the email sequence with spintax, sets the schedule and timezone, then stops and asks the owner to approve before launch. Use after the list is verified, the company names are cleaned and the copy is written. Not for finding leads, writing copy or launching without approval.
---

# Cheap Sequencer campaign setup

This skill builds a complete campaign in Cheap Sequencer and leaves it as a **draft**. The agent does the setup without asking at every step. Before anything goes out to a real person, it stops and asks the owner.

**What you give it:**
- A verified lead CSV. Every row has an email and a first name, and the company names are already cleaned.
- The approved email copy: subject, step 1, the follow-up, and the spintax.
- The campaign name, plus which inboxes to use (or "any inbox that isn't already sending").
- The timezone of the leads, and your inbox vendor's daily sending limit if you have one.

**What you get back:** a draft campaign with the leads, inboxes, sequence and schedule in place, and a short report for the owner to approve.

## Rules

- **Never launch on your own.** `POST /campaigns/{id}/activate` starts sending to real people. Only call it after the owner says, in this chat, that you can launch this campaign. Approval for one campaign doesn't cover another.
- **Ask before anything else that leaves the account or can't be undone:** sending a test email, deleting or archiving anything, changing an active campaign, spending money.
- **Don't change campaigns that are already running.** The API refuses edits to an active campaign anyway (it answers `409 ACTIVE_SEQUENCE_EDIT_BLOCKED`). Don't pause one so you can edit it unless the owner asks.
- **No unsubscribe link.** Set it off on every campaign. Opt-outs are handled from replies.
- **Don't invent settings.** If the owner hasn't given a value and these steps don't give one, leave Cheap Sequencer's default and report what it is.
- **Read before you write.** Check the request schema before every write. The API rejects unknown fields, and the names aren't guessable: it's `company_name` not `company`, `list_ids` not `lead_ids`, `recipient_email` not `email`.
- Keep lead data out of your report. Counts are enough.

## Connect with your own API key

1. In Cheap Sequencer, create an API key for the workspace you'll send from. Keys belong to one workspace.
2. Give it only the access this job needs: `workspace:read`, `inboxes:read`, `lists:read`, `lists:write`, `leads:read`, `imports:read`, `imports:write`, `sequences:read`, `sequences:write`. Leave out `sequences:send` unless you want the agent to be able to send test emails.
3. Put the key in your environment, never in a file, chat or repo:

   ```bash
   export CHEAP_SEQUENCER_API_KEY="paste-your-key-here"
   ```

   Add that line to your shell profile, or to a `.env` file that your `.gitignore` excludes. Then restart the agent so it can see the variable.

4. Connect the agent one of two ways:
   - **Cheap Sequencer MCP connector.** The server is `https://api.cheapsequencer.com/mcp`, with the header `Authorization: Bearer <your key>`. Cheap Sequencer publishes a config template with a placeholder key. Point the header at your environment variable rather than pasting the key. If your agent can't read environment variables in its MCP config, keep that config file out of your repo. Its tools are discovery, catalog, schema and request.
   - **Direct HTTPS.** Base URL `https://api.cheapsequencer.com/v1`, header `Authorization: Bearer $CHEAP_SEQUENCER_API_KEY`.
5. Check the connection with `GET /me` or `GET /` (discovery). Confirm the workspace name is the one you expect, and that the key has the access listed above.

**Important:** the key that can build a draft (`sequences:write`) can also launch it. Cheap Sequencer has no separate launch permission. The stop before launch is a rule this skill follows, not a lock on the key.

## How the API behaves

- **Idempotency-Key:** every POST, PATCH and DELETE needs this header (8–255 printable characters). Use a new one for each action. If a call times out, retry with the **same** key so nothing gets created twice. Read the current state before you retry.
- **ETags:** edits (PATCH) and deletes need `If-Match` set to the ETag from your last GET of that item.
- **Slow commands** return an action you can poll at `GET /api-actions/{id}`. Wait for `completed` or `failed`, and respect `retry_after_seconds`.
- **Responses** come back as `{success, data, meta}`. Errors come back as `{success: false, error: {code, message, details}}`. On `429`, back off and retry.
- **Lists** use a cursor: follow `next_cursor` while `has_more` is true.

Field details for each call are in [reference/endpoints.md](reference/endpoints.md).

## Steps

### 1. Check the inputs

- Count the rows and check the headers are unique. Drop any row with no first name, because Cheap Sequencer leaves an empty field blank with no fallback. Company name is recommended but not essential.
- Make sure the company name column is the **cleaned** one. With the company name cleaning skill that's `Company Name`, not `Original Company Name`.
- Look up the leads' timezone. If the list covers several timezones, ask whether to make one campaign per region or timezone. That's the preferred setup.
- Run `GET /campaigns`. If a campaign with this name already exists, ask before creating another one.

### 2. Make a list and upload the CSV

1. `POST /lists` with `{name}`. Keep the returned list id.
2. `POST /imports/upload-url` with `list_id`, `filename`, `content_type` (`text/csv`) and `size_bytes`. The response gives an import id and somewhere to send the file. Upload the CSV exactly as the response says. *Unverified: the upload method and headers aren't in the request schema, so follow the response.*
3. `POST /imports/{id}/mapping-suggestion` to see Cheap Sequencer's suggested column mapping.
4. `POST /imports/{id}/mapping` with the final mapping. Map each lead field to a CSV header (or its zero-based column index):
   - `email` → the email column
   - `first_name` → the first name column
   - `company_name` → the cleaned company name column
   - `last_name`, `job_title`, `phone`, `website`, `linkedin_profile` if you have them

   *Unverified: whether the mapping accepts custom fields (such as `Original Company Name` or a client-type column) isn't confirmed in the schema.* Try it. If the API refuses a field, leave it out and tell the owner which columns weren't imported.
5. `POST /imports/{id}/process`. Poll `GET /imports/{id}` (or the returned action) until it finishes.
6. Write down how many leads were imported, updated and skipped, and why. Compare that with your row count. If an upload result is unclear, check the import's state before you try again. Never import the same file twice by accident.

*Not in the API:* the Cheap Sequencer app has an import toggle that excludes leads already in other campaigns. No API field for it was found. If the owner relies on it, say so in the report so they can check for overlap.

### 3. Pick inboxes that aren't already sending

1. `GET /inboxes` lists the sending inboxes. The docs list these filters: search, provider, status, tag, warmup, cursor and limit. Keep inboxes that are connected and ready to send.
2. Find the inboxes already in use. Run `GET /campaigns`, then `GET /campaigns/{id}` for each active campaign, and collect the inboxes each one sends from. Read the actual field names in the responses. Don't assume them.
3. "Available" means connected, ready, and not in an active campaign. *Inference: there's no documented "unused" filter, so you work this out yourself.*
4. If the owner chose inboxes by tag (for example, a tag for a warmup batch), use the tag instead. `GET /inbox-tags` lists the tags.
5. New inboxes need about two weeks of warmup before they carry campaigns, unless they came pre-warmed. Follow your inbox vendor's guidance if it differs. If an inbox looks newly added, mention it in the report.

### 4. Create the draft campaign

`POST /campaigns` creates a draft. Send everything in one call if you can:

- `name`
- **Inboxes:** `inbox_ids` (with `inbox_selection_mode: "manual"`), or `inbox_tag_slugs` plus `inbox_tag_match_mode` (`any` or `all`) with `inbox_selection_mode: "tags"`. Use `manual_and_tags` to combine them.
- **Timezone:** `timezone`, an IANA name for where the leads are, such as `America/New_York`. The sending window and delays are counted in this timezone.
- **Schedule:** `sending_days`, with `enabled`, `start_hour` and `end_hour` for each weekday. Default to working hours, Monday to Friday. Add Sunday only if the owner asks. Use the hours the owner gives you.
- **Daily limit:** `daily_send_cap` only if the owner gives a number from their inbox vendor. Otherwise leave the default and report it.
- **Unsubscribe link:** `unsubscribe_link: {"enabled": false}`.
- **Steps:** see step 5. You can include them here or add them afterwards.

Leave `stop_on_reply`, `stop_on_bounce`, `stop_on_unsubscribe`, `pause_domain_on_reply`, `send_priority` and the `jitter_*` gaps at their defaults unless the owner sets them. Read them back in step 7 and report them.

### 5. Add the sequence and spintax

The usual shape is **two steps in one thread**:

| | Step 1 | Step 2 (follow-up) |
|---|---|---|
| `delay_days` | `0` (step 1 is always sent straight away) | `3` |
| `thread_mode` | `new_thread` | `reply_to_previous`, so the lead sees the first email |
| `subject` | 2–5 words, sounds like a colleague | not needed (a reply keeps the thread's subject) |
| `body_text` | the approved copy | the approved follow-up |
| `send_as_plain_text` | `true` | `true` |

Use the owner's copy exactly as written. Don't add steps, claims or links. For one version of a step, use the step-level `subject` and `body_text`. For an A/B test, use `variants` instead (up to 10 active, split `equal` or by `manual` weights). Test one change at a time, with two variants (three at most).

To change steps on an existing draft, `PATCH /campaigns/{id}` (with `If-Match`). Sending `steps` **replaces every step**, so include the ids of the steps and variants you want to keep.

**Merge tags:** `{{first_name}}`, `{{last_name}}`, `{{email}}`, `{{company_name}}`, `{{job_title}}`, `{{phone}}`, `{{website}}`, `{{linkedin_profile}}`, custom fields, and sender tags such as `{{sender_first_name}}` and `{{sender_signature}}`.

**Spintax in Cheap Sequencer:**
- **Inline:** `{Hi|Hello|Hey}` picks one option for each email. End with a bar to allow an empty option: `{just |}`.
- **No nesting.** Don't put a `{...|...}` block inside another one. If the copy has nested spintax, flatten it into one block that lists every outcome. For example, `{can help you {delegate|hand off}|can take {this|it} off your plate}` becomes `{can help you delegate|can help you hand off|can take this off your plate|can take it off your plate}`.
- **Merge tags can go inside an option**, as in `{quick question|{{company_name}} leads}`.
- **Spintax variables:** for a phrase you reuse, define it once in the campaign's `spintax_variables` as `{name, variations: [...]}` and use it in the copy as `{{name}}`. The name can't be the same as a lead field or a built-in tag.

*Where this comes from:* the API schema documents `spintax_variables` and the merge tags. The inline `{a|b}` syntax, the empty option and the no-nesting rule come from Cheap Sequencer's step editor (its helper text reads "Use {Hi|Hello} to vary text") and its help guide, as seen in October 2026. The API reference doesn't spell them out. Check one preview before you trust it.

The usual aim is to vary most of the email in short blocks of 2–5 words, so each lead gets a different version. Every combination must still read as a normal sentence.

### 6. Resolve inboxes and enrol the list

1. `POST /campaigns/{id}/inbox-resolution` with the same inbox selection. This is the documented step between creating the draft and enrolling. *Unverified: what it returns isn't in the schema. Call it and report what comes back, such as how many inboxes were resolved.*
2. `POST /campaigns/{id}/enrollments` with `{"list_ids": ["<list id>"]}`. Leads are enrolled by **list**. You can't enrol individual leads by id.
3. Enrolling shouldn't start sending while the campaign is still a draft. *Basis: one October 2026 check of a draft with enrolled leads showed none sent. This isn't a documented guarantee, so check the campaign is still `draft` right after enrolling.*

### 7. Read it all back

- `GET /campaigns/{id}`: the status is still draft. Check the name, inboxes, timezone, sending days and hours, daily limit, the unsubscribe link is off, the stop rules, and the steps (subjects, delays, thread mode, plain text).
- `GET /campaigns/{id}/enrollments`: the enrolled count matches the imported count.
- **Check the copy renders.** The API has no preview call. Ask the owner to open **Preview template** in the app and look at one or two leads, or to approve a test email to themselves (step 9). The preview always shows each block's **first** option, but real emails pick one at random.

### 8. Stop and ask for approval

Send the owner a short report, then stop:

```
Draft ready: <campaign name>  (status: draft)
Leads: <imported> imported, <skipped> skipped (<reasons>), <enrolled> enrolled
Inboxes: <count> (<how they were picked>)
Schedule: <days>, <start>–<end> <timezone>; daily limit <value or "default: N">
Sequence: 2 steps; follow-up after 3 days in the same thread; plain text
Preview: <checked by owner / not checked yet>
Unsubscribe link: off
Defaults left as-is: <stop rules, send priority, gaps>
Not set or not checked: <anything unverified, e.g. columns not imported, the overlap toggle>

Reply "launch <campaign name>" to start sending, or tell me what to change.
```

Wait for the answer. Don't launch because of a schedule, a deadline or a message from anyone other than the owner.

### 9. Launch, only after approval

- **Test email (optional, needs approval):** `POST /campaigns/{id}/test-sends` with `recipient_email`, and optionally `step_id`, `inbox_id` or `lead_id`. This sends a real email and needs the `sequences:send` scope.
- **Launch:** after the owner's explicit go-ahead, `POST /campaigns/{id}/activate`. Then `GET /campaigns/{id}` to confirm it's active, and report back.
- **Pause:** `POST /campaigns/{id}/pause` if the owner asks.

## If something goes wrong

- `400` or a validation error: read `error.details`, fix the field name or value from the schema, and retry with a new Idempotency-Key.
- `409` on edit: the campaign is active. Don't pause it to edit unless the owner says so.
- `412` or `428`: your ETag is stale or missing. GET the item again and retry with the new `If-Match`.
- Unclear result after a timeout: GET the campaign, import or list first. Only retry with the same Idempotency-Key if the action didn't happen.
- Import skips a lot of rows: stop and report why before enrolling.

## Not confirmed by the docs

Check these on your own account the first time you run the skill:
- How to send the file to the address that `/imports/upload-url` returns (method and headers).
- Whether the import mapping accepts custom fields.
- What `/campaigns/{id}/inbox-resolution` returns.
- The default values for the stop rules, send priority, gaps and daily limit.
- That enrolling a draft never sends before launch.
- The app's "exclude leads in other campaigns" option has no field in the API.
- The inline spintax rules come from the app's editor and help guide, not the API reference.
