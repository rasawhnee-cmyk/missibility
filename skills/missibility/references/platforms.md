# Platform Playbooks — one source system, five overlays

Facts below were verified by the manual's author on 2026-10-01. Platforms change crawler names, controls, and reports often — before giving a client a definitive policy, re-check the official pages listed in each section (use WebFetch/web search if available) and state the verification date.

Contents: Crawler matrix · Google · ChatGPT · Bing & Copilot · Perplexity · Claude · Cross-engine operating model

## Crawler / access matrix (crawler policy by PURPOSE)

| Platform | Search / discovery | Training / model development | User-triggered fetch |
|---|---|---|---|
| Google | Googlebot | Google-Extended (robots token for Gemini training & certain Gemini/Vertex grounding; does NOT affect Google Search inclusion or ranking) | — |
| OpenAI | OAI-SearchBot | GPTBot | ChatGPT-User (robots.txt may not apply; not used for Search inclusion) |
| Microsoft | Bingbot (also feeds Copilot & grounding) | — | — |
| Perplexity | PerplexityBot (not used for model training) | — | Perplexity-User (generally ignores robots.txt; not used for crawling or training) |
| Anthropic | Claude-SearchBot | ClaudeBot | Claude-User (all three honor robots.txt; Crawl-delay supported) |

Key consequences:
- Blocking a **training** crawler (GPTBot, ClaudeBot, Google-Extended) is a separate decision from blocking **search** crawlers (OAI-SearchBot, Claude-SearchBot, PerplexityBot, Bingbot, Googlebot). Many B2B brands that want AI visibility allow search crawlers while choosing a training policy deliberately.
- robots.txt is per host — www.example.com's file doesn't govern docs.example.com.
- robots.txt "allowed" can still be blocked by WAF/CDN bot management (Cloudflare, Akamai, etc.). Verify with the vendor's published IP ranges + user-agent checks.
- IP blocking alone is not a durable opt-out (the crawler may not be able to read robots.txt).
- robots.txt is not privacy. Use authentication.

**Cross-Engine Access Matrix** fields: Platform · Search crawler · Training crawler · User fetcher · Allowed · Blocked · Business reason · robots.txt status · WAF status · Owner · Last reviewed · Next review.

Example policy — allow search discovery everywhere, opt out of training:
```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

# OAI-SearchBot, Claude-SearchBot, PerplexityBot, Bingbot, Googlebot fall through to the default group
User-agent: *
Disallow: /admin/
Sitemap: https://www.example.com/sitemap.xml
```
**Prefer a named training blocklist over default-deny.** `User-agent: *` + `Disallow: /` ("allowlist") looks tidy to Legal, but it silently blocks every search crawler nobody remembered to list: DuckDuckBot, Applebot (Siri/Spotlight), YandexBot, Baiduspider, PetalBot (Huawei search), and future AI search bots. Use it only when Legal explicitly accepts that cost in writing. When you write any policy, check that no *search* crawler sits in the training-block group. Common mistakes are blocking Applebot instead of Applebot-Extended, PetalBot, and Amazonbot, which is a judgment call since it also serves Alexa/Rufus answers. Validate the final file with `scripts/check_crawlers.py` or `urllib.robotparser` before shipping. Non-standard lines such as `Content-Signal:` are fine as declarations, but most crawlers ignore them.

Caution: a crawler matches the most specific `User-agent` group only. If you create a group for e.g. `Claude-SearchBot`, it no longer inherits `*` rules — repeat needed disallows.

## Google Search, AI Overviews, AI Mode

- AI Overviews and AI Mode sit inside Google Search and are rooted in core ranking and quality systems. **No separate Google-AI content program.**
- To appear as a supporting link: page must be indexed and eligible for a snippet. Google says there are no additional technical requirements.
- Googlebot = Search crawler. Google-Extended is a separate policy (doesn't affect Search).
- Query fan-out is documented — do NOT publish a page per fan-out phrase (Google warns against low-value variation pages). Focus on the underlying decision.
- Sources still need: useful info, original value, evidence, clear entities, relevant images/video, good page experience, local and shopping data where relevant.
- Search Console has dedicated Generative AI performance reports (Search & Discover): impressions, pages, countries, devices, date trends — available to all sites worldwide as of 2026-08-31. A multimodal filter (Lens, Circle to Search, image uploads, Chrome image search) was announced 2026-09-24.
- Don't double count generative impressions in exec reports; use the dedicated view to analyze the subset; overall Search totals stay the broader measure. Don't call generative impressions citations.
- Google states llms.txt is not needed for Google Search and has no effect on visibility or ranking.
- Check preview controls (nosnippet, max-snippet, data-nosnippet) — they limit what can be shown.

Checklist: Googlebot access · index + snippet eligibility · source quality · media · preview controls · Google-Extended policy documented separately · Generative AI reporting · multimodal reporting where relevant.
Sources: developers.google.com/search/docs/appearance/ai-features · developers.google.com/search/docs/fundamentals/ai-optimization-guide · developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers

## ChatGPT Search

- Three access paths: **OAI-SearchBot** (surfaces sites in ChatGPT Search) · **GPTBot** (training) · **ChatGPT-User** (user/Custom GPT actions; robots.txt may not apply; not used for Search inclusion). Settings are independent.
- Allow OAI-SearchBot in robots.txt AND allow OpenAI's published SearchBot IP ranges through the WAF.
- ChatGPT Search also uses third-party search providers and partner content — owned pages aren't the only path in; third-party corroboration matters.
- Track four events separately: BRAND MENTION · PRODUCT MENTION · OWNED CITATION · THIRD-PARTY BRAND SOURCE.
- Test follow-up chains, not isolated prompts.
- Referrals carry `utm_source=chatgpt.com` — track them, but referral logs ≠ total influence.
- Keep public web tests separate from answers built on connected internal company data.
- Agentic browsing: accessible structure (ARIA labels/roles) helps agents operate interactive pages.

Checklist: OAI-SearchBot policy · GPTBot policy separate · understand ChatGPT-User · verify WAF · controlled Prompt Panel · owned vs third-party sources · utm_source=chatgpt.com referrals · public vs internal tests separate.
Sources: developers.openai.com/api/docs/bots · help.openai.com/en/articles/9237897-chatgpt-search · help.openai.com/en/articles/12627856-publishers-and-developers-faq

## Bing and Copilot — first-party citation data

- Bing Webmaster Tools **AI Performance**: visible citations across Microsoft Copilot, AI summaries in Bing, selected partners. Metrics: Total Citations, Cited Pages, Average Cited Pages, Grounding Queries. Preview views (2026): Intents, Topics, Citation Share, Compare.
- **Grounding Queries** = grouped phrases associated with retrieved & cited content — not full prompts.
- **Citation Share** = % of citations attributed to your site out of all citations for the same grounding query. Microsoft states AI Performance is observational: not ranking, authority, page importance, or traffic. Put that caveat on every dashboard.
- Bingbot indexing feeds Copilot and grounding eligibility.
- **IndexNow** notifies participating engines of added/changed/removed URLs — helps discovery/freshness; guarantees neither indexing nor citation. Use after meaningful source updates.
- Page controls (Bing-specific): NOINDEX blocks Bing Search, Copilot, and grounding API results · NOARCHIVE prevents use in Copilot responses and grounding · NOCACHE limits Copilot to URL/title/snippet (shallower citations) · NOSNIPPET / data-nosnippet limit captions and may reduce citation quality.
- Query-to-page model per topic: Grounding Query · Cited URL · Topic · Intent · Citation Share · Business Value · Source role. Join with analytics & CRM.

Checklist: Bingbot access · indexation · IndexNow where useful · NOINDEX/NOARCHIVE/NOCACHE/snippet controls · AI Performance review · cited URLs mapped to topics and value.
Sources: bing.com/webmasters/help/ai-performance-9f8e7d6c · bing.com/webmasters/help/webmaster-guidelines-30fba23a · indexnow.org

## Perplexity — citation is the product

- **PerplexityBot** surfaces and links sites in results (not used for training). **Perplexity-User** supports user requests and generally ignores robots.txt.
- Allow PerplexityBot in robots.txt and its published IP ranges; with a WAF, combine user-agent checks with IP verification.
- Modes (labels change; use current UI names): Standard Search, Pro Search, Research/Deep Research. Test relevant modes separately — they may use different source sets.
- Test initial question + commercial follow-up (the follow-up usually carries more value).
- Measure: Visibility (Brand Presence Rate) · Source Use (Owned Citation Rate, Third-Party Brand Source Rate) · Representation (vs Golden Fact Set) · Business impact (referral quality, leads, pipeline, sales-reported discovery). No invented "Perplexity rank".
- Freshness matters in web-first research: prices, availability, specs, leadership, locations, research, old PDFs.
- Use Perplexity as a research surface in audits, then trace the cited source — the generated answer isn't authoritative.
Sources: docs.perplexity.ai/docs/resources/perplexity-crawlers

## Claude (Anthropic) — three crawlers, three decisions

- **ClaudeBot**: model-development/training collection. **Claude-SearchBot**: search result relevance/accuracy. **Claude-User**: user-directed retrieval. All honor robots.txt; Crawl-delay supported.
- Set preferences on every relevant subdomain. IP blocking alone isn't a durable opt-out.
- Examples:
```
# Block training only
User-agent: ClaudeBot
Disallow: /

# Also keep an archive out of search discovery
User-agent: Claude-SearchBot
Disallow: /archive/
```
- Keep noindex deliberate — never accidental across priority content.
- Test **direct URL fetch**: give Claude a priority URL and ask what it claims, what evidence supports it, what conditions matter, what's unclear, what a buyer needs next — compare to the Page Contract.
- Test Web Search and Research separately. Keep public tests separate from connected enterprise context.
- Claude image search results are powered by Bing — image-search hygiene matters for image-heavy businesses.
Sources: support.claude.com/en/articles/8896518 · support.claude.com/en/articles/10684626 · support.claude.com/en/articles/11088861

## Cross-engine operating model

Don't build five content strategies. At the center: business priorities, customer research, Keyword & Prompt Universes, Entity Register, Claims Register, Source of Truth, evidence library, topic architecture, information portfolio, technical foundation, authority program, metric dictionary.

**Platform Overlay** jobs: ACCESS (which crawler/path reaches the source) · ELIGIBILITY (platform conditions) · OBSERVATION (first-party or controlled data) · EXCEPTIONS (controls that differ). The center is stable; overlays change faster.

Keep platform data native: Google generative impressions stay impressions; Bing citations stay Bing citations; ChatGPT/Perplexity/Claude panel results stay controlled observations. No universal score.

**Root-cause order for cross-engine gaps**: 1 Access → 2 Index/Discovery → 3 Relevance → 4 Evidence → 5 Entity clarity → 6 Freshness → 7 Authority → 8 Platform variance. Check shared fundamentals before blaming a platform. If Bing cites you and Claude cites a trade publication, compare source role, evidence, freshness, access — don't clone the page for Claude.

Shared Claim Map per high-value claim: Owned source · Evidence · Expert · Google observation · Bing citation activity · ChatGPT / Perplexity / Claude observations.

One Representation Panel across engines; repair the source once, retest each platform. One Change Log: Change ID · Entity · Fact changed · Old value · New value · Source of Truth · Affected URLs · Affected derivatives · Platforms affected · Refresh action · Retest date · Owner.

Central owner + platform stewards (stewards handle controls; they don't own a separate truth). Review platform policies quarterly.

Rule: one company needs one source system; platform differences belong at the edge.
