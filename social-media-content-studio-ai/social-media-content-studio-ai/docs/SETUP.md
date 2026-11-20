# Setup guide

## Minimum setup
1. Download or clone this repository.
2. Choose an agent platform that supports custom agents, skills, or Markdown
   instruction files.
3. Import the files according to that platform's current documentation.
4. Edit `config/studio.yaml`.
5. Run a test using `commands/daily-content.md`.
6. Review output manually before publishing.

## Configure your studio
Set:
- `brand.name`
- `brand.voice`
- `audience.primary`
- `content.language`
- `content.niche`
- `platforms.enabled`
- `workflow.require_approval`

Keep secrets out of this repository. Store API tokens only in the host platform's
secret manager or environment variables, never in prompts, Markdown, or commits.

## Integrations
This repository does not bundle platform API credentials or bypass platform
permissions. To connect scheduling or analytics:
- use official platform APIs or a reputable authorized provider;
- review current API scopes, app review requirements, and rate limits;
- request the minimum permissions;
- test with drafts or sandbox data first;
- keep human approval enabled.

## Claude.ai browser note
A GitHub repository is not automatically installed into Claude.ai browser chats.
Open the required Markdown files or provide the relevant command text to Claude.
For persistent agent installation, use an agent environment that supports custom
agents and follow its current installation guide.
