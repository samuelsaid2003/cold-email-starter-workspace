# Starter workspace for cold email

This folder is an AI workspace for one business. It holds your business context, your campaigns, leads and infrastructure, the agent's work logs, the rules it follows and the skills it uses. Connect it to your tools, give the agent a task, and it already knows your business and how you want the work done.

You don't need an engineered system. A simply configured folder with enough context does the job.

It works with Grok bot, Claude Code or Codex. Everything here is plain markdown.

## What's inside

```
starter-workspace/
├── AGENTS.md          the rules for this business
├── CLAUDE.md          points Claude Code to AGENTS.md
├── business.md        offer, ideal customer, voice, claims, proof
├── .claude/skills/    how you want each task done
├── campaigns/         copy and results, per campaign
├── leads/             lead lists, by campaign
├── meetings/          offered times, meetings, call briefs
├── infrastructure/    domains and inboxes
├── tools/             scripts and API connections
├── logs/              what the agent did, by task
├── README.md          this file
└── SETUP_PROMPT.md    paste this to set the workspace up
```

`.claude` is a hidden folder. If you can't see it, turn on hidden files in your file browser.

Use one workspace per business. If you run cold email for several businesses, copy this folder once for each.

## The skills

| Skill | What it does |
|---|---|
| `business-interview` | Interviews you one question at a time and saves the answers in `business.md` |
| `list-building` | Builds a lead list for a market from the sources that fit it best |
| `qualification` | Checks each company's website against your ideal customer |
| `company-name-cleaning` | Cleans company names so emails read as if written by hand |
| `copywriting` | Writes campaign copy from `business.md` |
| `cheap-sequencer-campaign-setup` | Sets up the campaign in Cheap Sequencer as a draft for you to approve |
| `out-of-office-and-referrals` | Turns out-of-office and "talk to my colleague" replies into follow-ups and emails to the right person |
| `booking-and-show-up` | Offers one specific time, books it, confirms it and tracks whether the call was held |
| `call-prep` | Writes a one-page brief before each meeting |
| `revival` | Scores your past sales calls and drafts follow-ups from what was actually said |

Claude Code loads skills from `.claude/skills/`. Codex loads them from `.agents/skills/` and Grok bot from `.grok/skills/`. The setup prompt copies or links them there if you use one of those.

## Getting started

Setup takes a few hours, not days. The only real wait is inbox warmup, so start that first.

### 1. Order or pre-warm your inboxes now

New inboxes need about 2 weeks of warmup before they send a campaign. Pre-warmed inboxes can start sending straight away. Order them from your inbox vendor before anything else, and follow your vendor's advice on warmup and sending limits.

### 2. Open this folder in your agent

Open the `starter-workspace` folder in Grok bot, Claude Code or Codex.

- Codex reads `AGENTS.md` on its own.
- Claude Code reads `CLAUDE.md`, which loads `AGENTS.md`.
- If your agent doesn't load `AGENTS.md` by itself, start each new chat with "Read AGENTS.md first."

### 3. Run the setup prompt

Copy the prompt from `SETUP_PROMPT.md` and paste it into a new chat. The agent checks the folder, makes the skills available to your agent and records which tools are connected.

### 4. Run the business interview

The agent interviews you one question at a time and saves your answers in `business.md`: what the business does, the offer, who you sell to, your voice, the claims you can make and your past campaigns. Bad brief in, bad drafts out, so take your time here.

To check it worked, open a new chat and ask "Who am I?" It should describe your business from `business.md`.

### 5. Connect your tools

Connect these first:

- Your sequencer (for example Cheap Sequencer)
- Your lead sources
- Your enrichment tools
- Your email verifier

Then add Gmail, Slack and your calendar. For the booking, call prep and revival skills, also connect your booking tool and your call recorder. Composio covers many of these. Some tools aren't available there and need their own MCP connection.

Give the agent the write access its tasks need. Building lists and setting up campaigns both require writes. The approval rules in `AGENTS.md` stop it from spending money, launching campaigns or making commitments without you.

### 6. Build your first list

Ask for a list in plain words, for example the market, the type of company and how many leads you want. The agent sources the companies, checks each one against your ideal customer, finds and verifies contacts, cleans the company names and sets up a draft campaign. You review it and approve the launch.

Start small, around 100 leads, while you check the results. Most sources and enrichment tools spend credits.

### 7. Set up replies and meetings

Finish the booking rules in `business.md` (section 13 of the interview), including which emails the agent may send without asking you. By default every email comes to you as a draft. Then ask the agent to run the out-of-office follow-ups and the call confirmations once a day as a scheduled task, if your agent supports one.

## Make your own skills

A skill is a standard procedure the agent follows every time. To make one:

1. Do the task with the agent once.
2. Ask it to correct every issue until the result is right.
3. Ask it to turn what you just did into a skill in `.claude/skills/`.

## Keep it working

- When the agent gets something about your business wrong, correct it and ask it to update `business.md`.
- Keep each campaign's copy and results in `campaigns/` so each new campaign starts from what you've learned.
- Keep `AGENTS.md` short. Detail belongs in `business.md` and the skills.
- Never put passwords or API keys in these files. Connect tools through your agent's own settings.
