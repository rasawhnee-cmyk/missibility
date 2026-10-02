# Core Frameworks

Contents: 1. Search Visibility Chain · 2. Seven Gates + ACT · 3. A page's four jobs · 4. Topic model · 5. Entities · 6. Evidence & claims · 7. Source Stack & Source of Truth

## 1. Search Visibility Chain

| Stage | Question |
|---|---|
| Demand | What questions, needs, comparisons, decisions do customers express? |
| Discovery | Does a crawler/search system know the source exists? |
| Understanding | Does it interpret the source, its entities, topic, relationships? |
| Evidence | Is there proof for the material claims? |
| Retrieval | Is the source selected as relevant for the query/prompt? |
| Selection | Is retrieved material chosen to appear in a result/answer/citation set? |
| Citation & Representation | Citation = visibly referenced. Representation = described accurately. Two different outcomes. |
| Commercial Outcome | Does any of it create business value? |

Diagnose the earliest broken stage first.

Modern query flow: query interpretation → **query fan-out** (one request spawns many sub-searches) → retrieval → **grounding** (external evidence supports the answer, i.e. RAG) → synthesis → citation → follow-up.

## 2. The Seven Gates (diagnostic order), then ACT

1. **Crawling** — Does the crawler reach the URL? robots.txt allows? WAF blocks legit bots? Server returns a useful response?
2. **Indexing** — Indexable? noindex? Canonical pointing elsewhere?
3. **Retrieval** — Indexed but not in the candidate set? Usual causes: weak topical fit, thin info, unclear entities, poor structure, stale facts.
4. **Ranking** — Ordering of candidates. Generated citation order ≠ organic rank.
5. **Grounding** — Which external sources support the answer?
6. **Generation** — Same evidence can produce different wording across runs/models/context/time → one prompt test is not a stable measurement.
7. **Citation** — Proves visible source use in that observed answer only; not authority, future placement, or revenue.

**ACT** — human outcome: click, compare, call, buy, book, ask sales, remember the brand.

Diagnostic routing:
- Blocked at Gate 1 → don't rewrite the page.
- Indexed but irrelevant (Gate 3) → don't blame the crawler.
- Retrieved but not cited → inspect extractability, evidence, source role.
- Cited but described wrongly → investigate entity and source consistency.

Failure modes: robots.txt for confidentiality; indexation treated as ranking; retrieval as citation; citation as recommendation.

## 3. A high-value page's four jobs

DISCOVERY (systems find it) · RETRIEVAL (matches the task strongly enough to enter the candidate set) · USE (worth extracting, summarizing, comparing, citing) · ACTION (human gets a useful next step). A source optimized for citation but useless after the click has failed.

## 4. Topic model — own the decision, not every wording

Keyword = an expression. Topic = a body of meaning. Customer decision = the job information must support.

| Level | B2B example (endpoint-security SaaS) |
|---|---|
| 1 Business category | B2B cybersecurity software |
| 2 Customer job | Select endpoint-security licenses for a midmarket company |
| 3 Decision requirements | Threat coverage, OS coverage, integrations, deployment, data residency, licensing |
| 4 Specific questions | EPP or EDR? How long is deployment? Works with our device fleet? |
| 5 Evidence | Deployment records, product docs, case studies, expert review |

Topic ownership: one Core Source owns the main decision; Supporting Sources deepen sub-decisions; Evidence Sources support claims; internal links connect the journey. Follow decisions, not decorative hub-and-spoke diagrams.

**Information gain** = useful knowledge a source adds beyond what's already in the result set. Generic summary adds little; original project evidence and fair technical comparisons with limits add more. Grow decision coverage and information gain, not page count.

Failure modes: one page per keyword variant; authority-as-page-volume; forcing unrelated intents into one giant page; supporting content with no evidence or internal link.

## 5. Entities — names, not vibes

Entity = distinct person, organization, product, location, service, event. Keywords describe; entities identify.

**Entity Register**: canonical names, aliases, descriptions, identifiers, relationships, URLs, owners, approved attributes. Start with: organization, brands, products, people, locations, services, certifications, research. Goal = factual consistency, not identical wording.

**Entity Confusion Test**: More than one public name for the same thing? Product under different categories? Executive titles disagree? Addresses differ? Retired products public without status? Partner sites describe it differently?

Structured data explains; it doesn't rescue a weak source. Use stable entity IDs (@id). `sameAs` only for genuine profiles of the same entity — never fake corroboration. Check external confirmation: partners, directories, regulators, associations, customers, publications, data providers.

**Entity Consistency Score** (0–2 each, max 10): Identity, Relationships, Attributes, Source, External Confirmation.

Rule: one entity needs one identity, however many pages describe it.

## 6. Evidence and claims — why should anyone believe you?

E-E-A-T (Experience, Expertise, Authoritativeness, Trust) is a Google quality concept, not a numeric score to manipulate.

**Evidence levels**
1. Unsupported assertion
2. General explanation with credible external sources
3. Named expert or direct operational experience
4. First-party evidence (case data, methodology, testing, customer results)
5. First-party evidence with independent corroboration

Risk decides the burden of proof. **Source the claim, not the paragraph.** A "30% faster investigation" result needs baseline, method, period, owner.

**Claims Register**: approved claims, evidence, owner, risk class, conditions, review date, source.

**Claim classes**: A low-risk descriptive · B commercial, needs support · C technical, needs expert review · D high-consequence, needs formal approval.

Evidence density (decision-relevant material supported by credible proof) beats citation count. PR works better once the organization owns evidence worth referencing.

Failure modes: adding sources after writing; citing secondary commentary when the primary exists; invented customer results; hiding limitations.

## 7. Source Stack and Source of Truth

| Role | Purpose | "If it disappeared…" |
|---|---|---|
| Source of Truth | Approved record for one fact | the org no longer knows which fact is approved |
| Evidence Source | Proof behind a claim | proof disappears |
| Supporting Source | Deeper explanation of one component | deeper understanding disappears |
| Core Source | Owns the main customer decision | the main decision disappears |
| Derivative Asset | Transformed format from approved sources | an alternate format disappears |
| Distribution Asset | Reach; points to deeper sources | reach disappears, info remains |

Source of Truth is an operational system, not a marketing page. The website *displays* facts; authoritative systems *own* them:
product name → PIM · spec → engineering record · price → pricing DB · executive role → corporate record · address → location DB · certification → compliance record · customer result → approved case record · statistic → research dataset · brand description → approved entity record.

**When sources conflict**: 1) stop publishing the disputed fact 2) verify owner 3) update Source of Truth 4) record effective date 5) update dependents 6) retire old values 7) retest public representation.
