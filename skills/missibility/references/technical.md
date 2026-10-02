# Technical Search Infrastructure

Contents: 1. Searchability · 2. Site architecture · 3. Structured data · 4. International

## 1. Make the site searchable before getting clever

A beautiful page with no search eligibility is decoration. First question: does the source reach the systems that need it?

**URL inventory — assign every material URL one intended state:**
INDEX (public, for search) · NOINDEX (public, not indexed) · BLOCK CRAWL (crawler access restricted) · PRIVATE (authentication). Use the right control: robots.txt = public crawl instruction, not protection; noindex = keep out of index; authentication = privacy.

Note: a URL blocked in robots.txt can't have its noindex seen. Don't combine them when the goal is deindexing.

**Status codes**: 200 OK · 301 permanent redirect · 404 not found · 5xx server failure. Policy: no long redirect chains on priority pages; removed pages must not return misleading 200 (soft 404s); permanent moves use 301.

**XML sitemaps**: only canonical, indexable URLs worth discovering; accurate lastmod; not a museum of every URL ever created.

**Canonical signal consistency**: align redirects, rel="canonical", internal links, sitemaps, structured-data URLs.

**Rendering (JS-heavy sites)**: test rendered output of priority templates for missing main content, delayed product data, hidden links, client-side canonical changes, late noindex injection, error states. Many AI fetchers don't execute JavaScript — server-render critical content.

**Internal links**: find **orphan pages** (no crawlable internal links) → connect, retire, or justify.

**Crawl budget** (large sites): don't waste it on endless filter combos, duplicate parameters, broken calendars, session URLs.

**PDFs**: track owner, status, canonical web equivalent, review date, retirement decision. Old PDFs keep feeding search and AI answers long after the campaign ends — a frequent cause of wrong AI facts.

**Issue priorities**: P0 immediate search/business failure · P1 high-value blocker · P2 planned improvement · P3 low-impact maintenance (so a missing alt attribute never outranks sitewide deindexing).

robots.txt review: read the raw file, not just a tester result. Look for:
- invalid lines, e.g. `Disallow: sub.example.com`, which is a hostname rather than a path and is ignored;
- disallowed paths that are priority pages, case studies or assets;
- disallows that contradict the sitemap, e.g. `/category/*` blocked while category-sitemap.xml is submitted;
- client or private paths exposed in public, which is a reputational leak and a reason to use authentication instead;
- stale rules nobody owns.

Checklist: inventory URLs · assign intended state · audit robots.txt (raw) · audit index directives · status codes · sitemaps · canonicals · render priority templates · find orphans · review PDFs · review WAF/CDN bot rules · add Search to release QA.

Rule: technical SEO removes barriers before content teams add inventory.

## 2. Site structure search systems understand

Architecture answers: Where does this topic belong? Which source owns the decision? How does a user reach the next useful source? Start with customer tasks, **not the org chart**.

Meaning-based hierarchy example:
Cybersecurity Software → Endpoint Security → License Selection → Integrations / Device Coverage / Deployment Planning / Case Studies

**Topic Ownership Register**: Topic ID · Topic · Primary Core Source · Supporting Sources · Evidence Sources · Owner · Business Value · Status · Review date.

**Page split rule** — split when the subtopic has a distinct decision, enough depth, a different evidence set, and a different action path. Otherwise keep together (avoid thin near-duplicates).

**Internal link relationship types**: PARENT (broader decision) · CHILD (narrower) · SIBLING (alternative) · EVIDENCE (proof) · ENTITY (person/product/company/location) · ACTION (next step). Use descriptive anchors ("endpoint-security integration guide", not "learn more"). Breadcrumbs where hierarchy helps.

URLs: stable, readable, governed; don't rewrite working URLs for aesthetics.
Taxonomy: allowed values, ownership, naming, hierarchy, change process.
Faceted navigation: decide which combinations deserve crawlable URLs; keep empty/duplicate/low-value combos out of the index.
Pagination/infinite scroll: crawlable paths; no human scroll needed to reach inventory.

A separate "AI website" is unnecessary — one coherent public information system serves people and machines.

Failure modes: mirroring the org chart; hubs with no decision role; one page per keyword; uncontrolled filters; internal links as a volume tactic.

## 3. Structured data without superstition

Schema.org vocabulary, usually JSON-LD. Markup must describe what the page and organization already know to be true — never invent reviews, awards, prices, availability, authors, locations, certifications.

| Page type | Schema |
|---|---|
| Organization page | Organization |
| Local location | LocalBusiness where appropriate |
| Person profile | Person |
| Product page | Product (+ Offer where supported); SoftwareApplication for software where it fits |
| Editorial | Article / appropriate CreativeWork |
| Breadcrumbs | BreadcrumbList |
| Video | VideoObject |
| Dataset | Dataset (only for genuine datasets) |

Use stable entity IDs (one Organization @id across all templates). Generate markup from controlled data (PIM, pricing system, corporate record) where practical.

Validate: syntax · supported properties · **visible-page agreement** · entity IDs · template behavior · duplicate plugin output · production rendering. Valid markup can still contain wrong facts.

No special "GEO schema" exists. Don't add invented types because a vendor promises AI visibility. Structured data improves clarity; it guarantees no ranking, retrieval, citation, or rich result.

Failure modes: invented facts in markup; adding every property available; two plugins publishing conflicting entities; treating validation as proof of impact.

Rule: markup clarifies truth; it doesn't manufacture facts.

## 4. International search — market design, not translation at scale

Separate language from country (Spanish ≠ Spain). Markets differ by language, country, currency, product availability, regulation, demand, competitors, proof, service model.

**Market Matrix** (before URLs): Market · Language · Country · Business priority · Product availability · Local evidence · Local expert · Demand Confidence · Current source · Investment decision.

URL models: ccTLDs, subdirectories, subdomains — choose by brand structure, operations, technical ownership, migration cost. Separate URLs per language (no client-side-only language swaps). Don't force-redirect by IP; give users control.

**hreflang**: valid language/region codes, self-references, reciprocal annotations, aligned with canonicals, x-default fallback where appropriate.

Localize the experience: keywords, prompts, examples, units, currency, case studies, competitors, regulatory context, contact paths, CTAs. Maintain an Entity Glossary (some names stay unchanged; some technical terms need approved local wording). AI translation needs field permissions: LOCKED facts stay locked. Measure each market separately.

Rule: translate only after the business has decided what belongs in the market.
