# Research Before You Optimize

Contents: 1. Start with economics · 2. Demand sources · 3. Keyword Universe · 4. Prompt Universe & Prompt Panels · 5. Competitor types & Claim Gap · 6. Decision-Ready Research Card · 7. Search Opportunity Map

Rule: research is finished only when findings change what the company does next.

## 1. Start with economics, not a keyword export

Ask first: Which customers matter? Which products/services? Which projects have healthy margin? Which markets have capacity? Which decisions block revenue? Only then ask how that demand appears in search.

Research must answer: What is the customer trying to decide? How often does the need appear? How valuable is the decision? Does the organization have a **Right to Win** (expertise, evidence, experience, products, customers, external recognition)?

## 2. Demand sources (Priority Map)

Internal first: sales calls, lost deals, customer interviews, support tickets, CRM, Google Search Console, Bing Webmaster Tools, site search, reviews, forums, industry communities. B2B extras: RFP/RFI questions, security questionnaires, onboarding/implementation tickets, partner/channel questions, LinkedIn comments.

Then third-party volume estimates — directional evidence, not audited demand. Zero reported volume ≠ zero value.

Audit the existing SERP/answer set (result types, commercial pages, publishers, forums, videos, local, AI features) to understand the **information standard** — not to copy the winner.

## 3. Keyword Universe

Fields: Keyword · Topic ID · Subtopic · Intent · Customer stage · Observed source · Volume estimate · Trend · Current URL · Current organic position · Business Value · Right to Win · Asset status · Recommended action.

Intent values: Learn, Research, Compare, Plan, Commercial, Local, Purchase.

## 4. Prompt Universe

Fields: Prompt ID · Topic ID · Who · Situation · Goal · Constraint · Question · Likely follow-up · Intent · Provenance (Observed / Derived / Synthetic) · Business Value · Current source · Evidence requirement.

- **Synthetic Prompt** = a hypothesis, not captured customer behavior. Label it; never present it as demand.
- Link both universes through **Topic ID** so there aren't two content systems.
- Use **prompt families**, not thousands of near-duplicates. Vary company size, tech stack, deployment window, current coverage, role — the asset decision still follows the underlying job.
- Bing **Grounding Queries** are grouped phrases, not full prompts — never merge them with Prompt Universe records.

Keywords show how demand is expressed; prompts show how the decision unfolds.

### Building a Prompt Panel (controlled observation set)

Use a fixed, repeatable set; re-run on a schedule; record date, platform, mode.

Prompt types to include for a B2B brand:
1. **Neutral fact / representation**: "What does {Brand} do?", "Where is {Brand} based?", "What is {Product}?", "Who leads {Brand}?", "How is {Product} priced?"
2. **Category discovery**: "Best {category} for {segment/size/industry}"
3. **Problem-led**: "How do I {job} when {constraint}?"
4. **Comparison**: "{Brand} vs {Competitor}", "Alternatives to {Competitor}"
5. **Follow-up chains** (higher commercial value): initial category question → requirement-specific follow-up (integrations, compliance, deployment, pricing) → proof ("case studies of…").
6. Per buying-committee role (economic buyer, technical evaluator, security/procurement).

Record per run: Prompt ID, Topic, Intent, Business Value, Platform (+mode), Brand present (Y/N/Unknown), Owned source cited, Third-party brand source, Competitor sources, Accuracy vs Golden Fact Set, Date.

Expect cross-engine disagreement. Parity isn't the goal; source consistency is.

## 5. Who owns the answer? Four competitor types

| Type | Role |
|---|---|
| Commercial | Sells against you |
| Search | Competes for search visibility |
| Information | Provides info the buyer uses (publishers, universities, labs, communities) |
| Citation | Gets cited in generated answers |

Build four lists, map overlap. In B2B, expect review platforms, analyst firms, communities, trade media, and standards bodies among Information/Citation competitors.

Per high-value topic, sample results and answers; record: Source · Source type · Page type · Decision served · Evidence strength (1–5) · Entity clarity · Extractability · Authority signals · Commercial position. Look *behind* the winner: what does it rely on, what evidence does it own, what claim does it support, why does its format fit the decision?

**Claim Gap table** — for each decision-critical claim:
Ownership: OWNED STRONGLY · OWNED WEAKLY · OWNED BY COMPETITOR · UNCLAIMED · OUTSIDE OUR AUTHORITY
Response: IGNORE · MATCH · EXCEED · DIFFERENTIATE · PARTNER OR EARN COVERAGE · BUILD AUTHORITY · FIX INFRASTRUCTURE · RESEARCH FIRST

Example: an independent lab owns comparative test data → don't imitate it; cite it as a primary source and own what you uniquely have (deployment experience, implementation guidance).

Rule: don't ask who ranks first; ask who owns the information the decision depends on.

## 6. Decision-Ready Research Card

Fields: Topic · Business objective · Target audience · Customer problem · Primary decision · Observed demand · Prompt demand · Search intent · Business Value (1–5) · Right to Win (1–5) · Current organic position · Current AI position · Current asset · Search-result format · Competitive gap · Evidence available · Evidence missing · Entity requirements · Asset recommendation · Recommended format · Primary differentiator · Dependencies · Effort (1–5) · Time to value · Success metric · **Decision** · Decision rationale.

Allowed decisions: DO NOW · IMPROVE EXISTING · RESEARCH FIRST · FIX INFRASTRUCTURE FIRST · DEFER · REJECT.

Worked example: endpoint-security licensing for midmarket mixed fleet; BV 5, RtW 5; current asset = generic page; gap = weak integration/rollout guidance, limited proof → IMPROVE EXISTING (strengthen Core Source, add 2 case studies, an integration Supporting Source, a deployment-planning section). Do NOT create another generic "best X software" article.

## 7. Search Opportunity Map

Per topic: Business Value · Demand Confidence · Right to Win · Current Gap · Evidence Strength · Effort · Priority Score (see `scoring.md`) · Recommended Action · Owner · Dependency · Decision date.

Action classes: DO NOW · IMPROVE EXISTING · RESEARCH FIRST · FIX INFRASTRUCTURE FIRST · BUILD AUTHORITY · MAINTAIN · DEFER · REJECT.

**Override rules** (beat the score): legal/compliance risk → human review; no credible evidence → RESEARCH FIRST; technical blocker → FIX INFRASTRUCTURE FIRST; strong existing asset → don't duplicate; no business relevance → REJECT regardless of volume; low Right to Win → DEFER unless building expertise.

Portfolio buckets: QUICK WINS (high value, low dependency) · STRATEGIC BETS (high value, meaningful effort) · EVIDENCE PROJECTS (attractive but proof missing) · AUTHORITY PROJECTS (source strong, recognition weak) · INFRASTRUCTURE (technical work affecting many assets).

Capacity: don't queue more than reviewers, developers, experts, budget can support.
90-day sequence: Days 1–30 fix blockers + strengthen top existing sources; 31–60 build evidence and missing decision support; 61–90 expand, distribute, test.
Forecast confidence: HIGH (strong first-party evidence) · MEDIUM · LOW (limited baseline/new behavior).
Every large project needs a **kill rule**; every high-value source needs a **maintenance trigger**.
Views: Master, Executive, 90-Day Queue.

Rule: a strategy is not a list of opportunities; it's the set you choose to fund.
