# Social Media Content Studio AI

A multi-agent content production studio for **YouTube, Facebook, and TikTok**.
It is designed for a **human-approved, semi-automated workflow**: agents research,
plan, write, package, repurpose, and quality-check content; a human approves
publishing and any external account action.

## What this repository is

This repository is an agent-and-workflow toolkit, not a hosted SaaS product and
not a promise of automatic virality. Agent files are operating instructions for
an AI coding/agent environment that supports Markdown agents or skills. Commands
are reusable prompt entry points; they do not execute by themselves unless the
host tool is configured to invoke them.

## Included

- 36 specialist agents across management, research, writing, production,
  YouTube, Facebook, TikTok, analytics, and governance.
- 8 reusable skills.
- 12 slash-command prompt templates.
- 10 end-to-end workflows.
- Content brief, script, publishing checklist, and analytics templates.
- Platform-aware publishing guardrails and configuration examples.
- Indonesian-first defaults, with English support where useful.

## Quick start

1. Copy this repository into your supported agent workspace.
2. Read `STUDIO_DIRECTOR.md` and `docs/OPERATING_MODEL.md`.
3. Configure `config/studio.yaml` with your niche, audience, language, cadence,
   and approval owner.
4. Start with `/daily-content` or `/content-campaign`.
5. Review all facts, copyright, music/footage rights, claims, and platform rules.
6. Approve each platform-specific package before scheduling or publishing.

## Suggested use

- **Claude Code:** adapt/copy agent Markdown files into the agent directory
   supported by your installed Claude Code version. Check current Claude Code
   documentation for the exact location and format.
- **Other agent platforms:** import the agent and skill instructions using that
   platform's documented format. Do not assume every host supports slash commands.
- **Claude.ai browser:** paste the relevant command prompt and attach the
   requested brief/files; repository files are not automatically installed into
   Claude.ai merely by existing on GitHub.

## Semi-automated publishing model

`draft → review → approval → schedule/publish → monitor`

No agent may publish, delete, boost, spend money, or change account settings
without explicit human authorization and a supported, connected integration.
If no integration is connected, the studio outputs ready-to-copy assets and
publishing instructions.

## Repository map

```text
agents/       Specialist agent instructions
skills/       Reusable capability playbooks
commands/     Slash-command prompt templates
workflows/    Multi-agent production procedures
templates/    Reusable content and review templates
config/       Studio defaults and platform guardrails
docs/         Operating manual, setup, governance, glossary
```

## First command

Open `commands/daily-content.md`, fill in the brief, and give it to your
Studio Director agent.

## License

MIT. See `LICENSE`.
