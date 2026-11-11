# Setup prompt

Open this folder in Grok bot, Claude Code or Codex, start a new chat and paste everything inside the box below.

```text
Set up this folder as my AI workspace for cold email. It is for one business.

1. Read AGENTS.md and README.md. Follow AGENTS.md for everything you do in this workspace.

2. Check the folder structure. Create any of these that are missing: campaigns/, leads/, meetings/, meetings/briefs/, infrastructure/, tools/, logs/, .claude/skills/. Don't delete or overwrite anything that's already here.

3. Check that each skill listed in README.md has a folder in .claude/skills/ with a SKILL.md inside. Tell me which ones are there and which are missing.

4. Make the skills available to the agent I'm using:
   - Claude Code: nothing to do, it loads .claude/skills/.
   - Codex: link or copy each folder in .claude/skills/ into .agents/skills/.
   - Grok bot: link or copy each folder in .claude/skills/ into .grok/skills/.
   - Anything else: read .claude/skills/<skill-name>/SKILL.md whenever a task matches a skill.

5. List the tools you can reach right now (MCP servers, Composio or other connections). For each one, run one small read-only check, such as listing campaigns or showing the account, to confirm it works. Change nothing. Then write tools/tools.md with each tool's name, what it's used for here (sequencer, lead source, enrichment, verifier, email, chat, calendar, booking tool, call recorder), whether the check worked, and whether it can write. Never write keys, passwords or tokens into the file.

6. Tell me which of these are still missing: a sequencer, lead sources, enrichment, an email verifier, Gmail, Slack, a calendar, a booking tool, a call recorder. For each missing one, tell me in one line how to connect it in the agent I'm using: through Composio, or through its own MCP connection if Composio doesn't cover it.

7. Write a log of this setup in logs/ (logs/YYYY-MM-DD-setup.md) saying what you set up and what is still missing.

8. If business.md is mostly unanswered, ask me whether to start the business interview now. If I say yes, follow .claude/skills/business-interview/SKILL.md and ask one question at a time.
```

## After setup

1. Finish the business interview if you didn't do it during setup.
2. Open a new chat and ask "Who am I?" The agent should describe your business from `business.md`.
3. Connect any tools the agent listed as missing.
4. Ask for your first list. Start with around 100 leads.
