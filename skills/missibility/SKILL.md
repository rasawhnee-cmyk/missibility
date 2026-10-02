---
name: missibility
description: Missibility runs the complete SEO + AEO + GEO (search engine, answer engine, and generative engine optimization) visibility process for any B2B brand, based on the Enterprise Search Visibility Manual by Meera Kaul. Use it whenever someone wants to audit, plan, or improve how a company shows up in Google, Bing, AI Overviews/AI Mode, ChatGPT Search, Copilot, Perplexity, or Claude — including keyword or prompt research, AI citation/visibility audits, "why doesn't ChatGPT mention us", wrong AI answers about a brand, robots.txt/AI crawler policy (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended), schema/entity work, citation-ready page briefs, AI content production governance, search measurement/KPIs, a 90-day search roadmap, or a search budget. Trigger even when the user only says "SEO", "AEO", "GEO", "LLM visibility", "AI search", "answer engines", or names a B2B company/website and asks how to get found or cited.
---

# Missibility — Enterprise Search Visibility for B2B brands

Missibility treats SEO, AEO, and GEO as three views of **one information system**, not three departments:

- **SEO** — make a source findable, understandable, indexable, and rankable by search engines.
- **AEO** — make information easy for an answer system to identify, extract, verify, and use.
- **GEO** — improve how the organization and its sources are retrieved, used, cited, and *accurately represented* inside generative answers.

The central rule: **Do not automate content. Automate the content system.** Research before production, evidence before claims, one approved fact before many outputs, human judgment where consequences matter, measurement tied to business value.

Source: *The Enterprise Search Visibility Manual — SEO, AEO & GEO in the Age of AI* by Meera Kaul. Platform facts in it were verified 2026-10-01; platforms change fast, so re-verify crawler names, controls, and reporting features against official docs before giving a client a definitive policy (see `references/platforms.md`).

---

## The two models everything hangs on

**Search Visibility Chain** — diagnose the *earliest* broken stage first; failures upstream masquerade as problems downstream (a blocked crawler looks like a content problem; inconsistent company data looks like an "AI problem").

`DEMAND → DISCOVERY → UNDERSTANDING → EVIDENCE → RETRIEVAL → SELECTION → CITATION & REPRESENTATION → COMMERCIAL OUTCOME`

**Source Stack** — every asset has one role:
`Source of Truth → Evidence Source → Supporting Source → Core Source → Derivative Asset → Distribution Asset`
One Core Source owns each customer decision. **One source. Many assets. One truth.**

Full definitions, the seven diagnostic gates, evidence levels and claim classes: `references/frameworks.md`.

---

## How to run Missibility

### Step 0 — Scope the engagement

Figure out which job the user needs, then go to the matching module. If unclear, ask one short question; if they just name a brand/site and say "help us get found", run the **Quick Visibility Diagnostic** below and recommend next modules.

Capture (ask only for what you can't find yourself):
- Brand, primary domain (and subdomains), markets/languages
- Priority product line or business unit (pilot on ONE — don't start enterprise-wide)
- Target buyer / buying committee, deal size, what counts as a *qualified* lead
- Known competitors
- Data access: Search Console, Bing Webmaster Tools, analytics, CRM, sales call notes, support tickets (use connected MCP tools if present — e.g. SEO/SERP/AI-visibility tools, Ahrefs, Similarweb, HubSpot, Gong — otherwise work from public web research and say what's missing)

### Modules

| # | Module | Use when the user wants… | Reference |
|---|--------|--------------------------|-----------|
| 1 | Quick Visibility Diagnostic | "How visible are we?" / first look at a brand | below + `audit-checklist.md` |
| 2 | Demand & Prompt Research | keywords, prompts, topics, what buyers ask | `research.md` |
| 3 | Competitive & Citation Map | who owns the answer, citation competitors | `research.md` |
| 4 | Search Opportunity Map | prioritize & fund topics | `research.md`, `scoring.md` |
| 5 | Technical & Crawler Audit | crawl/index/render, robots.txt, AI bots, WAF | `technical.md`, `platforms.md`, `scripts/check_crawlers.py` |
| 6 | Entity, Facts & Evidence | Entity Register, Claims Register, schema | `frameworks.md`, `technical.md` |
| 7 | Information Architecture & Page Briefs | site structure, Citation-Ready Page Brief | `content-production.md` |
| 8 | AI Asset Factory | governed AI content production, prompt contracts, reuse | `content-production.md` |
| 9 | GEO, Authority & Representation | citations, digital PR, wrong AI answers | `geo-authority.md` |
| 10 | Platform Playbooks | Google / ChatGPT / Bing-Copilot / Perplexity / Claude specifics | `platforms.md` |
| 11 | Measurement | KPIs, dashboards, metric definitions | `measurement-operations.md` |
| 12 | Operating Model, Budget & 90 Days | governance, cadence, budget, roadmap, charter | `measurement-operations.md` |
| — | Full Master Audit | comprehensive assessment | `audit-checklist.md` |
| — | Deliverable templates | any control sheet / register / map | `templates.md` |

Read only the reference files the chosen module needs.

### Module 1 — Quick Visibility Diagnostic (default starting point)

1. **Business frame.** One line each: what they sell, to whom, priority line, what a qualified outcome is.
2. **Access check.** Run `python3 scripts/check_crawlers.py <domain>` (add subdomains like docs./blog. too). It prints the allow/block table, a lint of the raw file, and the raw robots.txt itself. Report search crawlers (Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, Claude-SearchBot) separately from training crawlers (GPTBot, ClaudeBot, Google-Extended, CCBot). Then **read the raw file**. The allow/block table can't show the problems that matter most: invalid lines, disallowed paths that are actually priority pages or case studies, rules that contradict the sitemap, and client or private paths leaked publicly. robots.txt "allowed" ≠ reachable, since WAF/CDN bot rules can still block, so flag "verify WAF against vendor IP ranges". Check the homepage and 2–3 priority URLs for status, noindex, canonical, and whether main content is in server-rendered HTML.
3. **Entity check.** Is the company/product named and categorized consistently across homepage, About, product pages, LinkedIn, G2/Capterra, Crunchbase, partner pages? Any retired products or old PDFs still public?
4. **Prompt Panel snapshot.** Build 8–15 prompts across the buyer journey (see `research.md`): neutral fact prompts ("What does {Brand} do?"), category prompts ("best {category} for {segment}"), comparison prompts, implementation follow-ups. If you have web search, observe who gets cited; otherwise give the panel for the user to run. Label results as *observations*, never rankings.
5. **Source check.** Score 1–3 priority pages with the Page Source Score and Citation Readiness Score (`scoring.md`).
6. **Report** using the output format below: earliest broken gate, top 3–5 constraints blocking the most business value, and the next modules to run. Tie the recommendations to commercial outcomes. Say what qualified-lead or pipeline data you need, and which business line the fixes serve. Traffic and mentions are not the goal.

### Universal operating rules (apply in every module)

These twelve rules exist because each one prevents a common, expensive mistake:

1. Business before keywords. 2. Decisions before pages. 3. Research before production. 4. Access before optimization. 5. Facts before prose. 6. Evidence before authority claims. 7. One topic owner before multiple URLs. 8. Source quality before platform tricks. 9. Automation after governance. 10. Measurement before conclusions. 11. Maintenance before endless expansion. 12. Business value before vanity metrics.

Guardrails that keep advice honest:
- **Fix the earliest broken gate.** Don't fix an access problem with copy, or an evidence problem with robots.txt.
- **Keep metrics in their native meaning.** Google generative impressions ≠ citations. Bing Citation Share ≠ rank. Prompt Panel results are controlled observations, not market share. Never invent a single "AI visibility score".
- **No myths.** There is no special GEO schema; structured data clarifies but guarantees nothing; Google says llms.txt is not needed for Search; robots.txt is not a privacy control; one prompt test is not a ranking.
- **Don't build per-engine content or one page per fan-out phrase.** One source system, platform differences at the edge.
- **Label prompt provenance**: Observed, Derived, or Synthetic. Never present synthetic prompts as demand.
- **Being visible with wrong facts is not a win.** Representation accuracy is its own layer.
- **Scores sort work; they don't replace judgment.** All Missibility scores are internal QA tools — no engine sees them.
- **No manipulation.** No paid links, fake reviews, invented stats, fabricated schema facts, or scaled low-value AI pages — they create risk, not authority.

### B2B adaptation

The manual's worked examples are B2B (midmarket endpoint-security SaaS). Apply these B2B realities throughout:
- **Low volume, high value.** A query with "zero" reported volume attached to a six-figure deal deserves attention. Weight Business Value and Right to Win over search volume.
- **Buying committee.** Build Prompt Universe personas per role (economic buyer, technical evaluator, end user, security/procurement/legal) — each asks different follow-ups.
- **Mine revenue conversations first.** Sales calls, lost-deal notes, RFP questions, support tickets, and CRM data are the primary demand source; keyword tools add language.
- **Decision assets B2B buyers and answer engines need:** clear category/positioning page, use-case and industry pages, integration pages, comparison/alternative pages (fair, with limits), implementation/deployment guides, pricing/packaging clarity, security/compliance/trust documentation, case studies with baseline-method-period-outcome, and named experts.
- **Citation competitors in B2B** are often review platforms (G2, Capterra, TrustRadius, Gartner Peer Insights), analyst firms, communities (Reddit, Stack Overflow), standards bodies, and trade publications — map them; earn presence there rather than imitating them.
- **Outcomes:** qualified opportunities, pipeline, win rate, gross profit — never mix pipeline with revenue. Add self-reported attribution ("How did you hear about us?") and sales notes for zero-click influence.

---

## Output format

Unless the user asks for a specific template, structure deliverables like this:

```
# Missibility — {Deliverable name}: {Brand} ({scope})
## Bottom line
2–4 sentences: the earliest broken stage, the biggest value constraint, the recommended decision.
## What we found
Findings grouped by Search Visibility Chain stage; each with evidence (URL, observation, date) and confidence (High/Medium/Low). For crawler access, always report search crawlers and training crawlers as two separate lists. Blocking one is a different decision from blocking the other.
## Scores
Relevant internal scores with per-dimension breakdown and a one-line reason each.
## Decisions & actions
Table: Action | Gap type | Priority (P0–P3) | Owner role | Effort (1–5) | Success metric
Use action classes: DO NOW, IMPROVE EXISTING, RESEARCH FIRST, FIX INFRASTRUCTURE FIRST, BUILD AUTHORITY, MAINTAIN, DEFER, REJECT.
## What not to do
Tempting tactics that would waste effort here, and why.
## Next module
Which Missibility module to run next and what inputs it needs.
```

For working registers and control sheets, use the field lists in `references/templates.md` and the controlled field formats (IDs like TOP-001, dates YYYY-MM-DD, Blank vs 0 vs Unknown kept distinct). Offer spreadsheet (.xlsx) output when the deliverable is a register, universe, or map the team will maintain.

Always say what you could not verify (no Search Console access, couldn't observe a platform, WAF unknown) instead of guessing.

## Scripts

Paths are relative to this skill's directory (run them as `python3 <skill-dir>/scripts/...`). All reference files live in `<skill-dir>/references/`.

- `scripts/check_crawlers.py <domain> [more hosts...]` — fetches robots.txt per host and reports allow/block for Googlebot, Google-Extended, Bingbot, OAI-SearchBot, GPTBot, ChatGPT-User, PerplexityBot, Perplexity-User, ClaudeBot, Claude-SearchBot, Claude-User, CCBot, plus a sample path. Stdlib only.
- `scripts/score.py` — calculates Priority Score and any 0–2 rubric score with interpretation bands. Run `python3 scripts/score.py --help`.
