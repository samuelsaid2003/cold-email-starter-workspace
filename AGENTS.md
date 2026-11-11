# Agent rules for this business

This workspace belongs to one business. Follow these rules for every task here. The owner is the person you work for.

## Where things live

| Path | What it holds |
|---|---|
| `business.md` | The business: offer, ideal customer, who to skip, voice, approved claims and proof, booking rules, past campaigns |
| `campaigns/` | Copy and results, per campaign |
| `leads/` | Lead lists, by campaign; `leads/follow-ups-due.md` lists out-of-office and referral follow-ups |
| `meetings/` | Offered times, booked meetings and their outcomes, and call briefs |
| `infrastructure/` | Sending domains and inboxes |
| `tools/` | Scripts and API connections; `tools/tools.md` lists what is connected |
| `logs/` | What you did, one file per task |
| `.claude/skills/` | Step-by-step procedures for repeated tasks, one folder per skill with a `SKILL.md` |

## Before you start a task

1. Read `business.md`, and whatever in `campaigns/`, `leads/`, `meetings/` or `infrastructure/` the task needs.
2. Read recent files in `logs/` to see what is already done or in progress.
3. If a skill in `.claude/skills/` matches the task, read its `SKILL.md` and follow it.

If `business.md` is mostly unanswered, run the business interview (`.claude/skills/business-interview/`) before any cold email work.

## Keep work logs

Write a log for each piece of meaningful work in `logs/YYYY-MM-DD-task-name.md`: what you did, what it produced and where, decisions the owner made, and what is next. Keep it short. Don't log routine checks where nothing changed.

## Ask the owner first

Do the prep and routine work without asking at every step. Stop and ask before you:

- Spend money, including paid credits, purchases, domains and inboxes
- Launch a campaign
- Reply about price or commitments
- Delete anything
- Change an active campaign, however small

Build campaigns and emails as drafts. The owner approves the launch.

Reply to leads on your own only where the owner has set that up. Even then, ask instead of replying when you don't have the truthful information or context to answer.

## Standing rules

- Use only real links. Never make up a URL, name, number or claim.
- Use only the claims and proof saved in `business.md`. Flag anything you are guessing.
- If a source is blocked or won't load, ask the owner for an export instead of working around it.
- Follow your inbox vendor's limits for warmup and sending volume.
- Never write passwords, API keys or tokens into this workspace.

## Keep the workspace current

- When the owner corrects a fact about the business, update `business.md`.
- When the owner corrects how a task should be done, update that skill.
- Save each campaign's copy and results in `campaigns/` so the next campaign starts from what was learned.
- To make a new skill: do the task with the owner once, fix every issue they raise, then write it up as `.claude/skills/<skill-name>/SKILL.md`.
- Keep this file short. Detail belongs in `business.md` and the skills.
