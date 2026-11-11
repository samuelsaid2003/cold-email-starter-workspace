# Cheap Sequencer API: endpoints this skill uses

Base URL `https://api.cheapsequencer.com/v1`. Every request sends `Authorization: Bearer <your key>`. Every POST, PATCH and DELETE also sends `Idempotency-Key`. PATCH and DELETE also send `If-Match: <etag>`.

Field names below come from the API's request schemas (read November 2026). Always re-read the live schema before a write: the OpenAPI file is at `https://api.cheapsequencer.com/v1/openapi.json` and the docs are at `https://docs.cheapsequencer.com/api/v1/`. Through the MCP connector, use its schema tool.

## Order of calls

| # | Call | Scope | What it does |
|---|---|---|---|
| 0 | `GET /me`, `GET /` | workspace:read | Confirms the workspace and the key's scopes |
| 1 | `GET /campaigns` | sequences:read | Checks for name clashes; finds active campaigns |
| 2 | `POST /lists` | lists:write | Makes a list for this campaign's leads |
| 3 | `POST /imports/upload-url` | imports:write | Starts a CSV import into that list |
| 4 | `POST /imports/{id}/mapping-suggestion` | imports:write | Gets Cheap Sequencer's suggested column mapping |
| 5 | `POST /imports/{id}/mapping` | imports:write | Sets the final mapping |
| 6 | `POST /imports/{id}/process` | imports:write | Runs the import |
| 7 | `GET /imports/{id}`, `GET /api-actions/{id}` | imports:read | Polls until it's done; gives the counts |
| 8 | `GET /inboxes`, `GET /inbox-tags`, `GET /campaigns/{id}` | inboxes:read, sequences:read | Finds inboxes that aren't already sending |
| 9 | `POST /campaigns` | sequences:write | Creates the draft with its settings and steps |
| 10 | `PATCH /campaigns/{id}` | sequences:write | Edits a draft or paused campaign |
| 11 | `POST /campaigns/{id}/inbox-resolution` | sequences:write | Resolves the sending inboxes |
| 12 | `POST /campaigns/{id}/enrollments` | sequences:write | Enrols the list |
| 13 | `GET /campaigns/{id}`, `GET /campaigns/{id}/enrollments` | sequences:read | Reads everything back |
| — | **Stop. The owner approves.** | | |
| 14 | `POST /campaigns/{id}/test-sends` | sequences:send | Sends a real test email (only with approval) |
| 15 | `POST /campaigns/{id}/activate` | sequences:write | **Launches** (only with approval) |
| — | `POST /campaigns/{id}/pause` | sequences:write | Pauses a campaign |

Scopes for test sends, activation and enrolment come from the OpenAPI 403 descriptions and the authentication docs (October 2026). The other scopes are inferred from their names.

## Request bodies

**`POST /lists`**: `name` (required, up to 120 characters).

**`POST /imports/upload-url`**: `list_id` (required), `filename` (required), `content_type`, `size_bytes` (up to 50 MB).

**`POST /imports/{id}/mapping`**:
- `mapping` (required): lead field → CSV header name or zero-based column index, for example `{"email": "Email", "first_name": "First Name", "company_name": "Company Name"}`.
- `has_header`: whether the first row is a header.
- `delimiter`: one character.

**Lead fields** (from the lead schema): `email` (the lookup key, stored in lowercase), `first_name`, `last_name`, `company_name`, `job_title`, `phone`, `website`, `linkedin_profile`. Each one fills the matching `{{tag}}`.

**`POST /campaigns`** (create) and **`PATCH /campaigns/{id}`** (edit a draft or paused campaign only):

| Field | Notes |
|---|---|
| `name` | Required on create. Up to 140 characters |
| `inbox_ids` | Array of inbox ids. This is the write field; reads show a different shape |
| `inbox_tag_slugs`, `inbox_tag_match_mode` (`any`/`all`) | Pick inboxes by tag |
| `inbox_selection_mode` | `manual`, `tags` or `manual_and_tags` |
| `timezone` | IANA name, such as `America/New_York` |
| `sending_days` | `monday`…`sunday`, each `{enabled, start_hour (0–23), end_hour (1–24)}` |
| `daily_send_cap` | Most emails per day across all the campaign's inboxes |
| `jitter_min_seconds`, `jitter_max_seconds` | Random gap between sends |
| `send_priority` | `follow_ups` (default) or `new_leads`. (`priority` is deprecated and ignored) |
| `stop_on_reply`, `stop_on_bounce`, `stop_on_unsubscribe` | Stop rules |
| `pause_domain_on_reply` | Stops other leads at the same company domain when one replies. Default false |
| `unsubscribe_link` | `{enabled, scope, text}`. This skill sends `{"enabled": false}` |
| `spintax_variables` | Up to 50 `{name, variations[]}`. Used in copy as `{{name}}` |
| `steps` | Up to 100. **Sending it replaces all steps** |

**Each step:**
- `delay_days`: step 1 is always 0.
- `thread_mode`: `new_thread` or `reply_to_previous`.
- `subject`, `body_text`, `body_html`.
- `send_as_plain_text`.
- `variants[]`: `{subject, body_text, body_html, weight, archived}`, at most 10 active. Include an existing variant's `id` to edit it instead of replacing it.
- `distribution_mode`: `equal` or `manual`.

**`POST /campaigns/{id}/inbox-resolution`**: `inbox_ids`, `inbox_tag_slugs`, `inbox_tag_match_mode`, `inbox_selection_mode`. What it returns is unverified.

**`POST /campaigns/{id}/enrollments`**: `list_ids` (required). Leads are enrolled by list only.

**`POST /campaigns/{id}/test-sends`**: `recipient_email` (required), `step_id`, `variant_id`, `inbox_id`, `lead_id`.

**`POST /campaigns/{id}/activate`** and **`/pause`**: empty body `{}`.

## Spintax and merge tags

- `{{first_name}}`, `{{company_name}}`, …: lead fields. Source: the API lead schema.
- `{{sender_first_name}}`, `{{sender_signature}}`: sender tags. Source: the app editor and help guide.
- `{Hi|Hello}`: one option is chosen for each email. Source: the app editor's helper text and the help guide.
- `{Hi|Hello|}`: a trailing bar allows an empty option. Source: the help guide.
- No `{...}` inside another `{...}`: nested blocks aren't supported. Source: the help guide.
- `{{name}}` from `spintax_variables`: a reusable rotating snippet. Source: the API campaign schema and the app.

The app's preview shows each spintax block's first option. Real emails pick one at random.
