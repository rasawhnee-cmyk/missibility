# Missibility

**SEO, AEO & GEO for B2B brands: a Claude skill.**

Missibility teaches Claude to run search visibility work across Google, Bing, AI Overviews and AI Mode, ChatGPT Search, Microsoft Copilot, Perplexity and Claude. It treats all of it as one information system.

- **SEO**: make sources findable, indexable and rankable.
- **AEO**: make information easy for answer engines to extract, verify and use.
- **GEO**: get your organization retrieved, cited and *accurately represented* in generative answers.

It is based on *The Enterprise Search Visibility Manual: SEO, AEO & GEO in the Age of AI* by **Meera Kaul**.

> Don't automate content. Automate the content system.

## What it does

Ask Claude things like:

- "Do a quick check of how visible acme.com is in Google and in AI answers, and tell us what to fix first."
- "Legal wants to block AI training bots, but we still want to show up in ChatGPT and Perplexity. Write our robots.txt."
- "ChatGPT says we're still headquartered in Austin and sell a product we discontinued. How do we fix that and track it?"
- "Build a prompt universe and a search opportunity map for our payroll product."
- "Write a citation-ready page brief for our SOC 2 compliance page."

Missibility then works through twelve modules:

| # | Module |
|---|---|
| 1 | Quick visibility diagnostic |
| 2 | Demand and prompt research (Keyword Universe and Prompt Universe) |
| 3 | Competitive and citation map |
| 4 | Search opportunity map and priority scoring |
| 5 | Technical and AI-crawler audit |
| 6 | Entity, facts and evidence (Golden Fact Set, Claims Register) |
| 7 | Information architecture and citation-ready page briefs |
| 8 | Governed AI content production (Source Packs, prompt contracts) |
| 9 | GEO, authority and repairing wrong AI answers |
| 10 | Platform playbooks: Google, ChatGPT, Bing/Copilot, Perplexity, Claude |
| 11 | Measurement that keeps each platform's metrics in their native meaning |
| 12 | Operating model, budget and the first 90 days |

It includes two helper scripts (Python standard library only):

- `check_crawlers.py` checks robots.txt for 12 search and AI crawlers, separating search bots from training bots. It also lints the raw file for invalid lines, default-deny rules and blocked search engines.
- `score.py` calculates the priority score and the 0–2 scoring rubrics.

## Install

### Claude Code (plugin marketplace)

```
/plugin marketplace add rasawhnee-cmyk/missibility
/plugin install missibility@missibility
```

### Claude Code (manual)

```bash
git clone https://github.com/rasawhnee-cmyk/missibility.git
cp -R missibility/skills/missibility ~/.claude/skills/
```

### Claude.ai / Claude desktop

1. Download the latest `missibility.skill` from the [Releases](https://github.com/rasawhnee-cmyk/missibility/releases) page. You can also zip the `skills/missibility` folder yourself.
2. Go to **Settings → Capabilities → Skills** and upload it.

Once installed, Claude uses Missibility automatically when you ask about SEO, AEO, GEO, AI search visibility, AI crawlers, or how a brand shows up in AI answers.

## Principles built in

- Diagnose the **earliest broken stage** first. A blocked crawler looks like a content problem.
- Make crawler policy **by purpose**. Blocking a training bot is a different decision from blocking a search bot.
- **No myths.** There is no special "GEO schema", llms.txt doesn't affect Google Search, robots.txt is not privacy, and one prompt test is not a ranking.
- **Being visible with wrong facts is not a win.** Representation accuracy is measured separately.
- **No manipulation.** No fake reviews, paid links, invented statistics or scaled thin AI pages.

Platform details (crawler names, controls, reporting) were verified on 2026-10-01. Platforms change often, and the skill tells Claude to re-verify before giving a definitive policy.

## Author

Created by **Meera Kaul**, author of *The Enterprise Search Visibility Manual: SEO, AEO & GEO in the Age of AI*.

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Free to use and adapt with credit to Meera Kaul, for non-commercial purposes, with adaptations shared under the same license. For commercial licensing, contact the author. Full text in [LICENSE](LICENSE).
