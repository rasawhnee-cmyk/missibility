# Measurement, Operations, Budget, 90 Days, Charter

Contents: 1. Five-layer measurement · 2. Operating model · 3. Budget · 4. First 90 days · 5. Playbook tests, maturity, charter

## 1. Stop putting everything into one AI visibility score

Appearing, being cited, getting a click, and creating business value are separate events (Pew 2025: clicks on traditional results fell from 15% to 8% of visits when an AI summary appeared; clicks on links inside summaries ~1%).

| Layer | Question | Examples |
|---|---|---|
| 1 Search eligibility | Technically able to participate? | index status, crawler access, WAF status |
| 2 Visibility | Did the source/entity appear? | organic impressions, Google generative impressions, Brand Presence Rate |
| 3 Source use & engagement | Cited, clicked, used? | Bing citations, Owned Citation Rate, clicks, referral visits |
| 4 Representation | Material facts correct? | Representation Accuracy Score, high-risk error count |
| 5 Business outcome | Commercial value? | qualified leads, pipeline, revenue, gross profit, bookings |

Platform-native metrics keep native meaning: don't call Google impressions citations, Bing citations rankings, or Prompt Panel results market share.

**Internal observation metrics** (explicit formulas; none is a universal AI rank):
- Brand Presence Rate (= Prompt Presence Rate) = tracked prompts where brand appears ÷ tracked prompts tested
- Owned Citation Rate = tracked prompts where an owned URL is cited ÷ tracked prompts tested
- Third-Party Brand Source Rate = tracked prompts where a third-party source supports a statement about the brand ÷ tracked prompts tested
- Commercial Citation Coverage = high-value commercial prompts with owned citation ÷ high-value commercial prompts tested
- Cross-Engine Source Coverage = engines where an owned source appears for a prompt ÷ engines tested

AI referral traffic (e.g. utm_source=chatgpt.com, referrers from perplexity.ai, copilot, gemini, claude.ai) misses zero-click influence. Add self-reported discovery, sales notes, branded demand, assisted-conversion analysis — without turning them into causal claims.

Funnel: Eligibility → Visibility → Source Use → Representation → Referral → Engagement → Conversion → Revenue.

Report by topic and intent; use baselines and confidence labels. **Metric Dictionary**: metric, formula, data source, owner, cadence, limitation, native vs internal.

Rule: measure the event that happened; don't rename a metric into the event you wish had happened.

## 2. Run search like an operating system, not a campaign

One accountable **Search owner** keeps the system coherent (doesn't do every task).

Functions: Search strategy · Technical SEO · Content operations · SMEs · Analytics · Brand & communications (entity representation, authority, corrections) · Web/product (templates, CMS, performance, agent-friendly interfaces) · Sales (commercial reality, buyer questions, lead quality, win-loss).

Small **Search Council** for decisions, not group editing.

Cadence: WEEKLY ops — what's blocked? · MONTHLY performance — what changed? · QUARTERLY strategy — what deserves investment? · ANNUAL system review — does the model still fit?

**One backlog** (no separate SEO and GEO backlogs) with gap types: ACCESS · INDEXING · RELEVANCE · EVIDENCE · ENTITY · FRESHNESS · AUTHORITY · REPRESENTATION · COMMERCIAL COVERAGE · MEASUREMENT. Route by root cause, not symptom. Priority P0–P3.

**Incident track** (bypasses backlog): sitewide deindexation, major crawler block, false regulated/safety claim, wrong price at scale, broken conversion path, severe representation error. Severity SEV1 immediate material risk · SEV2 major business impact · SEV3 contained · SEV4 low-risk.

Refresh triggers: price, product, executive, certification, or evidence change; search decline; citation decline; representation error; broken source; scheduled review. Event-driven where the Source of Truth supports it.

Track Content Debt (stale, duplicate, unsupported, unowned, low-value content) and Technical Debt. Protect maintenance capacity — never 100% new production.

Search review **before launch** for: CMS migration, rebrand, domain migration, product rename, new market, acquisition, navigation redesign, JS framework change, CDN change, security-policy (WAF) change.

**Search Decision Log**: Decision · Reason · Evidence · Owner · Date · Affected systems · Review date · Outcome.

AI helps ops with classification, summarization, stale-asset and source-conflict detection, reporting; humans own trade-offs.

## 3. Search needs a budget, not a wishlist

Budget by business opportunity, not output (articles, pages, backlink packages).

Six buckets: PEOPLE & OPERATIONS · TECHNICAL & WEB · EVIDENCE & RESEARCH · AUTHORITY & DISTRIBUTION · DATA & TOOLS · MAINTENANCE & EXPERIMENTATION. Count internal labor (12 hours of engineering review costs more than the writing invoice).

Formulas:
- Cost per Approved Source = total production & review cost ÷ approved Core and Evidence sources published
- Cost per Approved Derivative = total derivative production cost ÷ approved derivatives
- Expected Gross Profit = qualified opportunities × win rate × avg gross profit per win
- Gross-profit return = (expected gross profit − program cost) ÷ program cost
- Qualified Pipeline Created ≠ Closed-Won Revenue — never mix.

Scenarios LOW / BASE / HIGH with confidence labels. Per major workstream, an economic hypothesis: audience, topic, current gap, work required, leading indicators, business outcome, review period, kill rule.

Leading indicators (not the business case): indexation, commercial query coverage, generative impressions, citation activity, Page Source Score, Citation Readiness Score, relevant authority references.

Fund evidence explicitly (case studies need records, permission, photography, verification, expert review, design). Technical work needs an impact model (affected URLs, high-value URLs, revenue-bearing URLs, templates, markets). Every tool needs a job ("which decision improves because we pay for this?"); don't buy an AI visibility platform before defining what its metrics mean.

Hire a system owner before a content army; keep strategy, Source of Truth ownership, priorities, and measurement accountability internal.

Illustrative $300k program: People & Ops $105k · Technical & Web $60k · Evidence & Research $45k · Authority & Distribution $30k · Data & Tools $30k · Maintenance & Experiments $30k. Base scenario: 100 qualified opps × 25% win × $20k GP = $500k expected GP → 67% illustrative gross-profit return. Label assumptions; not causal certainty.

Rule: fund business opportunity and source quality, not content volume.

## 4. The first 90 days

Pilot ONE business line/market/product family with real revenue value, known demand, available experts, enough content to audit, enough evidence to improve, manageable technical scope. One 90-day business question, e.g. "How do we increase qualified {product} opportunities by improving visibility across traditional and generative search?"

Success levels: FOUNDATION (technical & factual systems work) · SOURCE (priority sources improve) · BUSINESS (qualified demand improves vs baseline).

**Days 1–30 · Diagnose & stabilize**
- Wk1 Business & customer baseline: meet owner, sales, ops, product, support, experts, analytics; define target customer, qualified lead, high-value service, capacity, questions, commercial KPI; first Keyword & Prompt Universes.
- Wk2 Technical baseline: status codes, robots.txt, index directives, canonicals, sitemaps, internal links, rendering, structured data, crawler access, WAF. Fix P0/P1. Platform Access Matrix. Confirm analytics, GSC, BWT, CRM access. Record baselines.
- Wk3 Entity & fact baseline: Entity Register, Golden Fact Set, Source of Truth Register, Claims Register; find conflicts; Representation baseline.
- Wk4 Source portfolio audit: per priority URL — job, intent, source role, owner, Page Source Score, Citation Readiness Score. Choose five source projects. Don't rewrite everything.
- Day-30 one-page review: business baseline, blockers, source gaps, representation issues, next five assets.

**Days 31–60 · Build & prove**
- Wk5 Build Source Stack; collect evidence. Wk6 Citation-Ready Page Briefs; first AI-assisted workflow (record time, corrections, unsupported claims, edit distance, cost). Wk7 Publish first improved set; update links, sitemaps, schema, IndexNow; production QA. Wk8 Start one authority project; first cross-engine retest.
- Day-60 decision: SCALE · CONTINUE · FIX · STOP.

**Days 61–90 · Scale what works**
- Wk9 Expand highest-value gaps. Wk10 Automate one low-risk workflow; build one refresh trigger. Wk11 Expand Prompt Panel where useful; executive scorecard. Wk12 Quarterly review: which source types worked, which claims lack proof, which platform gaps are technical vs source gaps, where AI output failed, which reviewer bottlenecked, which metrics changed decisions, which tools added no value. Plan the next 90 days from evidence.

By Day 90 (minimum viable system): Business Priority Map, Keyword Universe, Prompt Universe, Search Opportunity Map, Entity Register, Claims Register, Source of Truth Register, Crawler Matrix, technical baseline, Source Portfolio, Cross-Engine Prompt Panel, Representation Panel, Metric Dictionary, production workflow, executive scorecard, Search owner, operating cadence.

Should NOT exist by Day 90: thousands of unreviewed synthetic prompts; hundreds of generic AI articles; five platform content teams; a publishing agent with unrestricted CMS access; a complete site rewrite.

Rule: don't start with scale — start with truth, access, evidence, and one working system.

## 5. Playbook tests, maturity, charter

**Five questions for any new SEO/GEO tactic**: Which platform says this matters? Which Chain stage does it affect? Does it help the customer? Does it improve source, evidence, access, or experience? How will the result be measured?

Tests: **Customer** — would a serious customer find it useful? **Source** — reachable, relevant, evidenced, current, distinct? **Automation** — inputs controlled, facts approved, permissions clear, failures safe? **Platform** — access, index, relevance, evidence, entity clarity, freshness, authority, platform variance? **Money** — which priority, what gap, why Right to Win, what success/failure look like, when to stop, when to scale?

Master workflow: Business priority → Customer decision → Demand research → Opportunity → Technical eligibility → Entity & fact governance → Evidence → Information architecture → Source creation → AI production → Authority → Platform distribution → Measurement → Representation → Business outcome → Refresh.

**Maturity**: L1 Tactical SEO ("How do we rank?") · L2 Structured Search ("Where should we compete?") · L3 Search Visibility System ("Which decisions should we own?") · L4 AI-Assisted Search Ops ("How do we scale verified knowledge?") · L5 Adaptive Search OS ("How does the system improve from evidence?"). Control, not automation volume, defines maturity.

**Two-page Enterprise Search Visibility Charter**
Page 1 — why: Business objective · Customer decisions · Right to Win · Search scope · Source principles · AI principles · Measurement principles.
Page 2 — how: Owner · Teams · Cadence · Priority model · Platform governance · Incident model · Refresh model · Budget model · Final decision test.

Final decision test: Does this make the organization easier to **find**, **understand**, **trust**, and **choose**? If not, question why the work exists.
