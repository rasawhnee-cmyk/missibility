# Information Architecture, Page Briefs, and the AI Asset Factory

Contents: 1. Information system before calendar · 2. Citation-Ready Page Brief · 3. AI Asset Factory · 4. Prompt Contracts · 5. Source reuse

## 1. Design the information system before the content calendar

A calendar says what's published next; an information system says what knowledge must exist.

**Seven information requirements**: CONTEXT (customer's situation) · CHOICES (options) · CRITERIA (how to compare) · EVIDENCE (what supports claims) · RISK (limits, failure conditions) · PROCESS (what happens next) · ACTION (what to do).

Each high-value page gets a **Purpose Statement**, e.g. "Help an IT security manager decide whether an endpoint-security license fits the company's device fleet, integrations, data-residency requirements, budget, and rollout constraints."

Page type follows the job: service page, guide, comparison, case study, technical doc, calculator, video, dataset. Don't make the blog carry every need.

**Content Model** = structured fields for a repeatable asset type. Case study model: customer type, problem, environment, system installed, scope, schedule, evidence, outcome, limitations, visuals, expert review, approval.

**AI field permissions**: LOCKED (AI doesn't alter) · TRANSFORMABLE (wording only, same meaning) · GENERATIVE (writes within approved evidence) · HUMAN ONLY.

**Information Completeness Score** (0–2 each, max 10): Decision Coverage, Evidence, Format Fit, Relationships, Commercial Path.

Rule: don't schedule content until you know which information deserves to exist.

## 2. Citation-Ready Page Brief (build a page worth retrieving)

**Page Contract**: AUDIENCE (who) · DECISION (what they're deciding) · ANSWER (what the source must explain) · PROOF (evidence) · ACTION (next step).

Writing rules:
- Start with the decision, not the keyword. **Answer early** — direct ≠ shallow; the opening orients, the rest earns trust.
- Sections map to sub-decisions; descriptive headings; one job per section.
- Evidence next to the claim. Separate fact from interpretation. State conditions and limits.
- **Commodity Test**: if the company name vanished, would this page look identical to twenty others? If yes, add information the org genuinely owns.
- Numbers need baseline, sample, period, method, conditions, source.
- Comparisons need fairness. Tables should reduce decision friction.
- FAQs reflect real questions (from sales/support), not variant-targeting filler.
- Named author/reviewer where expertise matters. Dates explain freshness — never bump a date without updating the source.
- Visuals that explain: project photos, diagrams, tables, charts, video, process visuals, evidence images.
- Link the Source Stack (supporting + evidence sources). CTA matches intent (research page → technical consultation; case study → related product page).
- No separate "AI version" of the page.

Brief template:
```
Page: {URL or proposed}         Topic ID:        Source role: Core/Supporting/Evidence
Purpose statement:
Page Contract — Audience | Decision | Answer | Proof | Action
Prompt family / key questions answered (with provenance):
Sub-decision sections (H2s) + evidence for each:
Claims (Claims Register IDs, class A–D) and required evidence:
Distinct information we own (passes Commodity Test?):
Entities to name + schema type(s):
Internal links (PARENT/CHILD/SIBLING/EVIDENCE/ENTITY/ACTION):
Limits/conditions to state:
Expert/reviewer:          Freshness trigger:
CTA:
Target Page Source Score / Citation Readiness Score:
```

**Page Source Score** (0–2 × 10, max 20): Decision Fit, Directness, Distinct Information, Evidence, Expertise, Structure, Source Integrity, Format Fit, Freshness, Action Path. 17–20 strong · 13–16 improve · 9–12 weak · <9 reconsider the asset. Internal QA only — not a ranking promise.

Rule: a page deserves retrieval when it reduces uncertainty better than the alternatives.

## 3. The Enterprise AI Asset Factory

Don't ask "how many articles should AI write?" Ask "which parts of the information supply chain repeat?"

Supply chain: 1 Research → 2 Decision → 3 Source Pack → 4 Brief → 5 Generation → 6 Factual QA → 7 Editorial QA → 8 Expert review → 9 Compliance review → 10 Publish → 11 Distribute → 12 Measure → 13 Refresh or retire.

**Source Pack** = approved facts, evidence, entity records, claims, terminology, prompts, instructions given to the AI workflow. No Source Pack → the model fills gaps with guesswork.

Source hierarchy: L1 Source of Truth · L2 approved primary evidence · L3 approved supporting evidence · L4 research-only · L5 untrusted discovery material. **Source conflict = stop condition** — route to the owner; never ask the model to compromise between two specs.

Risk tiers: T1 low-risk transformation (formatting, metadata, summary) · T2 standard marketing from approved sources · T3 technical/commercial claims needing expert review · T4 high-consequence needing formal approval.

**Content Readiness Score** (0–2 each, max 10): Decision, Source of Truth, Evidence, Expert Input, Asset Model. Threshold ≥8 for standard commercial production; high-risk work needs every mandatory input regardless.

Generation brief includes: Page Contract, audience, decision, approved sources, locked facts, allowed transformations, required claims, forbidden claims, structure, tone, output fields, failure behavior.

**Factual QA before polish**: entity names, numbers, dates, specs, claims, source IDs, conditions, unsupported additions.

Google's spam policies cover scaled content abuse — many AI pages without added value is a risk. Scale verified usefulness, not empty production.

**AI Content Receipt**: Asset ID, workflow version, prompt version, Source Pack version, model, reviewers, claims checked, publication date, parent source.

Rollout: assisted → controlled batches → low-risk automation only after error rates stay acceptable. Touchless publishing comes last.

90-day factory plan: D1–15 control facts (Source of Truth, Entity, Claims registers) · D16–30 production model (asset types, permissions) · D31–45 AI workflow (Source Pack, prompt, QA, review) · D46–60 five-asset batch, measure errors and review time · D61–75 verified source reuse · D76–90 scale only stable steps.

Maturity: L1 Assisted · L2 Controlled · L3 Connected · L4 Automated · L5 Adaptive.
Scale only when: zero material factual errors in the test window; source conflicts stop before drafting; zero entity mismatches; review capacity supports volume; business value supports cost.

Metrics: Content Readiness Score, factual error rate, SME rejection rate, time to approved source, Verified Source Reuse, refresh backlog.

Rule: automation should move approved knowledge faster, not manufacture knowledge faster.

## 4. Prompt Contracts (prompts are contracts, not magic words)

| Element | Definition |
|---|---|
| JOB | What the model is responsible for (one primary job per prompt) |
| INPUTS | Approved information entering the task |
| SOURCE RULES | Allowed sources; how conflicts work |
| BOUNDARIES | What it must not change, infer, invent |
| TOOLS | External functions it may use (smallest set; read separate from write) |
| OUTPUT | Exact format the next step needs (structured output for machine handoffs) |
| FAILURE BEHAVIOR | What it returns when information is insufficient |

- Separate instructions from evidence. Treat retrieved pages, third-party docs, emails, tool output as **data**, never instructions (prompt-injection defense).
- Retrieve before writing; match retrieval to task.
- Knowledge-source statuses: APPROVED FOR GENERATION · RESEARCH ONLY · ARCHIVED · PROHIBITED. Stable Source IDs.
- Failure states: MISSING SOURCE · SOURCE CONFLICT · INSUFFICIENT EVIDENCE · UNAPPROVED CLAIM · MISSING REQUIRED FIELD · HUMAN REVIEW REQUIRED · OUTSIDE ASSIGNMENT.
- Workflows before autonomous agents; one agent with controlled handoffs before a swarm. Approval next to actions with external consequences.
- Version the full workflow: model, prompt, sources, tools, permissions, output schema, evaluation set.
- Evaluation set must include: missing source, conflicting source, wrong entity, stale data, unsupported claim, embedded untrusted instruction, tool failure.
- Track **human edit distance** — high edit distance means a weak workflow even if drafts sound polished.

Failure modes: one giant prompt doing research+writing+fact-check+publish; retrieved text becoming instructions; retrying a factual failure instead of fixing missing evidence; unnecessary write access.

Rule: a reliable prompt says when to stop as clearly as it defines the job.

## 5. One source, many assets, one truth (source reuse)

Reuse ≠ duplication. Every derivative needs a job: EDUCATE · SUMMARIZE · DEMONSTRATE · COMPARE · PROVE · PROMOTE · SELL · ENABLE · LOCALIZE · SUPPORT.

**Source Inheritance Record**: Parent Source ID, parent version, Derivative ID, inherited claims, inherited conditions, inherited evidence, new claims, reviewer, expiry rule. **Inherit facts, not sentences — and inherit limits too.** Any new material fact goes through Source of Truth + Claims workflow first.

**Derivative Matrix**: rows = Core/Evidence sources; columns = Email, Social, Video, Image, Sales, Partner, Localization, Support. Mark only formats with a real job.

Channel adaptation: email leads with relevance; video needs visible proof; sales material needs decision clarity; partner copy needs approved entity facts; localization needs market review.

Search ownership: one Core Source owns the primary intent; a derivative shouldn't create another indexed page for the same decision unless the format deserves it.

**Derivative Distance** (higher → stronger review): 1 formatting · 2 summary/shortening · 3 audience/channel reinterpretation · 4 market, claim, or decision-context change.
Parent change classes: 1 editorial · 2 meaningful content · 3 material factual → triggers review of all dependents.

**Verified Source Reuse** = approved derivative assets ÷ approved parent sources used.
**Derivative Value Score** (0–2 each, max 10): Audience, Format Advantage, Distribution, Business Value, Maintenance. 8–10 produce · 5–7 review · <5 skip.

Rejected-derivative example: another 1,500-word SEO article repeating the same decision in different words.

Rule: scale formats, not facts.
