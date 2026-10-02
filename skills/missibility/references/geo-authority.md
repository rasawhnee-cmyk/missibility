# GEO: Citations, Authority, and Representation

Contents: 1. Why would an answer system cite you · 2. Earned authority · 3. Wrong AI answers (representation repair)

## 1. Why would an answer system cite you?

GEO question: when a generative system researches and builds an answer, does your organization/source become part of the information used and presented? Citation is one visible form of participation — not the only one (retrieval without citation, presence via third-party source, accurate representation with no click).

Order: **eligibility** (public, reachable via the platform's retrieval path) → **task relevance** (serves the actual decision, not a nearby topic) → information quality.

Strong citation candidates contain: clear claims · visible evidence · provenance · named entities · current info · original value · useful structure · fair limits · cross-format consistency.

AEO extractability practices (support the above; never substitute for evidence):
- Lead each section with a direct, self-contained answer sentence that still makes sense if quoted alone; name the entity instead of "we/it".
- Use question-shaped headings where buyers ask questions; definitions in "X is…" form.
- Tables for comparisons/specs; numbered steps for processes.
- Put the number, its conditions, and its source in the same sentence or adjacent.
- Keep critical content in server-rendered HTML, not behind tabs that require JS, images of text, or gated PDFs.

**Citation roles**: DEFINITION · EVIDENCE · COMPARISON · DATA · EXPERIENCE · COMMERCIAL · LOCAL · EXPERT. You don't need to own every role — map claims instead (OWNED STRONGLY / OWNED WEAKLY / OWNED BY COMPETITOR / UNCLAIMED / OUTSIDE OUR AUTHORITY). Don't chase claims outside your authority (a SaaS vendor shouldn't pose as an independent test lab).

**Citation Readiness Score** (0–2 × 8, max 16): Eligibility, Task Relevance, Extractability, Evidence, Provenance, Entity Clarity, Freshness, Distinct Value. 14–16 strong · 10–13 improve · 6–9 weak · <6 fix fundamentals. Then the non-scored question: *does the organization deserve to own this claim?*

Observation: use first-party platform data where it exists (Bing AI Performance); elsewhere use a controlled **Prompt Panel** — results are observations, not universal rankings. Use "Citation Share" only in Bing's defined meaning.

Failure modes: chasing citation before eligibility; trying to own every claim; treating citation as recommendation; turning one prompt into a ranking report.

Deliverable: **Citation Opportunity Map** (topic → claim → ownership → citation role → current cited sources → owned source → readiness score → action).

Rule: don't ask how to get cited before asking what the source contributes.

## 2. Authority is what others say when you leave the room

Don't reduce authority to a vendor "domain authority" score (Google publishes none). Links still matter as references and discovery paths. Authority also comes from: editorial mentions, expert quotes, research references, customer references, partner references, association records, reviews, public records, conference profiles, certifications. B2B adds: analyst coverage, review platforms (G2, Capterra, TrustRadius, Gartner Peer Insights), marketplace listings (AWS/Azure/Salesforce/etc.), integration-partner directories, standards participation.

**Authority hierarchy**: L1 low-value/self-created · L2 relevant directories, partner references · L3 independent industry coverage, customer proof · L4 high-quality independent sources directly supporting important claims. Relevance beats volume.

**Authority gaps**: RECOGNITION (few credible mentions) · EVIDENCE (nothing source-worthy) · EXPERT (no named experts) · CUSTOMER PROOF (few public outcomes) · INDUSTRY PARTICIPATION (absent from associations, research, conferences, standards).

Build source-worthy evidence **before** outreach. Digital PR distributes evidence; it's not a pretext for link schemes. Original research needs scope and method.

**Expert Program** — per expert: topic, credentials, approved bio, public profile, available evidence, media readiness, response process. Don't use one expert for every topic.

Customer proof governance: get permission → verify numbers → record context. Prefer named over anonymous. Reviews show experience; they don't replace technical proof.

Risky (avoid): paid links, undisclosed sponsorship, fake reviews, mass guest posting, link exchanges.

AI can support authority research: find relevant publications, cluster journalist topics, summarize prior coverage, match experts to questions. Don't automate spam.

**Authority Map** fields: Topic · Target source · Source type · Claim supported · Relationship · Status · Owner · Earned result.
**Earned Authority Score** (0–2 each, max 10): Relevance, Independence, Source Quality, Claim Support, Freshness — evaluates a reference, not a search-engine score.

Rule: authority grows when credible outsiders have a reason to reference work you genuinely own.

## 3. AI knows your brand — but the answer is wrong (representation)

Visibility and accuracy are separate problems. Representation = the factual statements a search/AI system presents about an entity.

**Golden Fact Set** (approved current material facts):
- ORGANIZATION: name, category, HQ, service area, ownership where public
- PRODUCT: name, vendor, category, status, specifications, availability
- PEOPLE: name, role, expertise, current status
- LOCAL: location name, address, hours, service area
- COMMERCIAL: price where public, offer status, primary services, material terms

**Representation Panel**: neutral factual prompts ("What does {Company} do?", "Where is {Company} based?", "What is {Product}?", "Who leads {Company}?"). Record the exact material claim; compare to the Golden Fact Set.

Severity: L1 Cosmetic · L2 Contextual · L3 Material · L4 High Risk. Severity overrides the average — one high-risk false technical claim outweighs several correct fields.

**Trace the source**: official page, old PDF, partner page, directory, news article, structured data, legacy blog, search index (plus in B2B: review-site profiles, Crunchbase/LinkedIn, Wikipedia/Wikidata, old press releases, analyst reports).

**Source error vs synthesis error**: SOURCE ERROR = public evidence is wrong or conflicting → repair sources. SYNTHESIS ERROR = sources are right but the answer still misstates → keep correct sources, strengthen clarity/consistency, retest via controlled panel (and use platform feedback channels).

Repair order: Source of Truth first → public dependents → don't edit five pages independently while the authoritative record stays wrong. Record repair date, refresh action (resubmit sitemap, IndexNow, request recrawl, update third-party profiles), retest date, status. Systems refresh at different speeds — be patient; one bad answer is not a trend.

**Representation Accuracy Score** (0–2 each, max 10): Identity, Core Fact, Context, Freshness, Source Alignment. 9–10 accurate · 7–8 minor · 4–6 material weakness · <4 priority remediation.

**Interim cover for customer-facing teams.** Repairs take weeks, and model-memory answers can take much longer. On day one, give sales and support:
- a one-page facts card built from the Golden Fact Set;
- a short talk track that addresses the error before the prospect raises it, e.g. "Some AI tools still show our pre-2024 address; we're headquartered in Denver.";
- a way to log new wrong answers they hear, which feeds the Representation Panel.

Deliverable: **AI Representation Control Sheet** — Incident ID · Platform/mode · Prompt · Observed claim · Golden fact · Severity · Error type · Traced source(s) · Repair action · Owner · Repair date · Retest date · Status.

Rule: being visible with the wrong facts is not a win.
