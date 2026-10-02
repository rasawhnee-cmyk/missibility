# Master Scoring Reference

All scores are internal tools to sort work. No search engine sees them, they don't predict rankings or citations, and they never replace judgment. Always show the per-dimension breakdown with a one-line reason, not just the total. `scripts/score.py` computes them.

## Priority Score (topics) — inputs 1–5
Business Value, Demand Confidence, Right to Win, Current Gap, Evidence Strength, Effort.
Ease = 6 − Effort
**Priority = BV×3 + DC×2 + RtW×2 + Gap×2 + Evidence×1 + Ease×1** (max 55)
45–55 strong priority · 35–44 good opportunity · 25–34 needs investigation · <25 usually defer/reject/revisit.
Override rules apply (see `research.md`).

## 0–2 rubrics (0 = absent/poor, 1 = partial, 2 = strong)

| Score | Dimensions | Max | Bands |
|---|---|---|---|
| Page Source Score | Decision Fit, Directness, Distinct Information, Evidence, Expertise, Structure, Source Integrity, Format Fit, Freshness, Action Path | 20 | 17–20 strong · 13–16 improve · 9–12 weak · <9 reconsider |
| Citation Readiness | Eligibility, Task Relevance, Extractability, Evidence, Provenance, Entity Clarity, Freshness, Distinct Value | 16 | 14–16 strong · 10–13 improve · 6–9 weak · <6 fix fundamentals |
| Entity Consistency | Identity, Relationships, Attributes, Source, External Confirmation | 10 | — |
| Information Completeness | Decision Coverage, Evidence, Format Fit, Relationships, Commercial Path | 10 | — |
| Content Readiness | Decision, Source of Truth, Evidence, Expert Input, Asset Model | 10 | ≥8 to produce standard commercial content; high-risk needs all mandatory inputs |
| Derivative Value | Audience, Format Advantage, Distribution, Business Value, Maintenance | 10 | 8–10 produce · 5–7 review · <5 skip |
| Earned Authority | Relevance, Independence, Source Quality, Claim Support, Freshness | 10 | — (scores a reference) |
| Representation Accuracy | Identity, Core Fact, Context, Freshness, Source Alignment | 10 | 9–10 accurate · 7–8 minor · 4–6 material weakness · <4 priority remediation. High-risk severity overrides the average |
| Search Visibility System | Business Alignment, Customer Research, Technical Foundation, Entity Governance, Source of Truth, Evidence, Information Architecture, AI Production, Authority, Cross-Engine Visibility, Representation, Business Measurement | 24 | 20–24 strong OS · 15–19 working with gaps · 9–14 fragmented · <9 foundation first |

## Scales
- Derivative Distance: 1 formatting · 2 summary · 3 audience/channel reinterpretation · 4 market/claim/decision-context change
- Evidence levels 1–5, Claim classes A–D (see `frameworks.md`)
- Representation severity L1 cosmetic · L2 contextual · L3 material · L4 high risk
- Issue priority P0–P3; incident severity SEV1–SEV4
- Evidence strength (competitor analysis) 1 weak/unsupported – 5 strong primary evidence with clear provenance
- Forecast confidence HIGH / MEDIUM / LOW

## Dimension anchors (quick guidance for 0/1/2)
- **Eligibility**: 0 blocked/noindex/not rendered · 1 accessible but issues (WAF uncertain, canonical conflict) · 2 crawlable, indexable, snippet-eligible, server-rendered
- **Task Relevance / Decision Fit**: 0 nearby topic · 1 serves the decision partially · 2 directly serves the buyer's actual decision
- **Directness / Extractability**: 0 answer buried or absent · 1 answer present but not quotable standalone · 2 early, self-contained, well-structured answers
- **Evidence**: 0 assertions only · 1 general/external support · 2 first-party proof with method, near the claim
- **Provenance**: 0 unsourced numbers · 1 sources named vaguely · 2 primary sources linked, dates/methods stated
- **Entity Clarity**: 0 ambiguous names/categories · 1 named but inconsistent · 2 consistent names, category, relationships, matching schema
- **Freshness**: 0 stale facts/dates · 1 mostly current, no review trigger · 2 current with owner and review trigger
- **Distinct Value / Distinct Information**: 0 fails Commodity Test · 1 some owned detail · 2 clear information gain only this org can provide
