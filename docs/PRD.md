# CareerLens Product Requirements Document

## 1. Product Overview

CareerLens is an AI Talent-Role Alignment Platform.

Its core goal is to reduce mismatch between candidate capabilities and company role requirements. CareerLens turns a resume and target role into structured intelligence: what the candidate can credibly demonstrate, what the role actually requires, where the alignment is strong, where the gaps are, and what actions would improve readiness.

CareerLens is not a resume writer, job board, application tracker, or generic chatbot. Resume optimization is one module inside a broader evidence-based alignment workflow.

The V2 product loop is:

```text
Resume Upload
  -> Resume Intelligence
  -> Talent Capability Graph
  -> Role Intelligence
  -> Talent-Role Alignment Report
  -> Resume Optimization
  -> Career Development Plan
```

## 2. Product Positioning

CareerLens sits between talent intelligence, role intelligence, and career strategy.

Users should be able to answer:

- What capabilities can I prove from my resume, projects, and experience?
- What does this role require beyond the visible job description?
- Which requirements do I satisfy with strong evidence?
- Which gaps are highest priority?
- How should I optimize my resume and development plan for this target?

The product experience must emphasize structured analysis, explainable recommendations, confidence levels, and source evidence instead of open-ended chat.

## 3. Target Users

### Phase 1 Users

- University students in computer science, AI, software engineering, data science, information systems, product management, and related fields
- Early-career technology professionals with 0-5 years of experience
- Candidates targeting internet, AI, software, enterprise technology, platform, and data roles

### Future Users

- Career coaches and education programs
- Recruiting teams evaluating role readiness and internal mobility
- Enterprise talent intelligence teams
- Global technology talent

## 4. Supported Role Families

Initial supported role families:

- AI Engineer
- Software Engineer
- AI Product Manager
- AI Solution Engineer
- Data Analyst / Data Scientist / Data Engineer
- Other technology and digital roles

## 5. Core User Problems

### Problem 1: Resume Evidence Is Unstructured

Candidates have projects, internships, coursework, and achievements, but the evidence is not mapped to capabilities in a way that supports role decisions.

### Problem 2: Role Requirements Are Ambiguous

Job descriptions often omit hidden competencies, workflow realities, evaluation signals, and seniority expectations.

### Problem 3: Fit Analysis Is Shallow

Keyword matching cannot explain why a candidate fits or does not fit a role. Users need evidence-backed capability comparison.

### Problem 4: Resume Optimization Lacks Strategy

Candidates often edit resumes without understanding which evidence matters for a target role or which gaps cannot be solved by wording alone.

### Problem 5: Development Plans Are Too Generic

Users need gap-based improvement roadmaps connected to the capabilities required by a role.

## 6. Product Principles

- Talent-role alignment over generic career advice
- Structured intelligence over chatbot-only interaction
- Evidence-backed recommendations over unsupported summaries
- Capability mapping over keyword matching
- Confidence-aware scoring over false precision
- Resume optimization as alignment communication, not resume writing
- Career development plans tied to concrete gaps

## 7. Core Modules

## 7.1 Resume Intelligence

Resume Intelligence converts an uploaded PDF or pasted resume into structured, reviewable profile data.

Inputs:

- Resume PDF upload
- Pasted resume text
- User-edited experience, project, education, skill, and preference fields

Outputs:

- Parsed resume sections
- Experience extraction
- Project and achievement extraction
- Education and credential extraction
- Resume evidence records
- Missing or weak evidence indicators
- Initial capability signals with confidence levels

Key requirements:

- Users can upload resume PDFs.
- The system extracts resume text and stores the original artifact.
- Users can review and edit extracted fields.
- Extracted records preserve links back to resume evidence.
- The system flags incomplete, vague, duplicated, or low-evidence sections.

## 7.2 Capability Intelligence

Capability Intelligence builds a Talent Capability Graph from resume evidence and user-edited profile data.

The capability graph includes:

- Capability nodes such as programming, AI/ML, data analysis, product thinking, communication, leadership, domain knowledge, and execution
- Evidence links to projects, experience, education, achievements, and resume sections
- Confidence scores for each capability
- Strength indicators
- Skill and experience gaps
- Capability progression over profile versions

Key requirements:

- Capabilities must be evidence-linked.
- Each inferred capability includes confidence and rationale.
- Users can inspect which resume evidence supports each capability.
- Users can mark capabilities as verified, developing, or aspirational.
- The graph should support role-specific filtering.

## 7.3 Role Intelligence

Role Intelligence turns a target job description or role template into structured requirements.

Inputs:

- Job description text
- Curated role templates
- Company and industry context where available
- User-selected role family and seniority

Outputs:

- Required capabilities
- Preferred capabilities
- Responsibilities and real job workflow
- Seniority expectations
- Evaluation signals
- Hidden competency inferences
- Evidence examples that would demonstrate readiness
- Requirement confidence and source references

Key requirements:

- Users can paste or upload a job description.
- The system extracts explicit requirements.
- The system infers hidden competencies with clear rationale and confidence.
- The system explains the likely real job workflow behind the role.
- Role requirements are normalized so they can be compared with the capability graph.

## 7.4 Alignment Engine

The Alignment Engine compares candidate capabilities with role requirements and generates a Talent-Role Alignment Report.

The report includes:

- Overall alignment score
- Capability-level alignment
- Strength analysis
- Gap analysis
- Evidence quality assessment
- Requirement coverage
- Risk and uncertainty indicators
- Recommended decision posture
- Resume optimization suggestions

Scoring dimensions:

- Capability match: demonstrated capabilities versus role requirements
- Evidence strength: quality, specificity, and recency of supporting proof
- Experience relevance: similarity between prior work and expected role workflow
- Requirement coverage: explicit and inferred role requirements covered by evidence
- Gap severity: importance and difficulty of missing capabilities
- Confidence: completeness and reliability of available data

Key requirements:

- Users can generate an alignment report for a target role.
- Every score includes evidence, rationale, and confidence.
- Gaps are prioritized by role impact, not only by missing keywords.
- The report distinguishes "can improve wording" from "needs actual capability development."
- Reports are saved and comparable across profile and role versions.

## 7.5 Resume Optimization

Resume Optimization helps users communicate existing evidence more effectively for a target role.

It provides:

- Targeted resume gaps
- Evidence placement suggestions
- Bullet-level improvement guidance
- Capability coverage checklist
- Role-specific emphasis recommendations
- Warnings when a gap requires new evidence rather than rewriting

Key requirements:

- Optimization suggestions are grounded in the alignment report.
- The product should not fabricate experience or achievements.
- Suggestions must preserve evidence traceability.
- Users remain in control of final resume content.

## 7.6 Career Strategy

Career Strategy creates a gap-based Career Development Plan.

The plan includes:

- Capability improvement roadmap
- Project recommendations
- Learning priorities
- Interview preparation focus
- Evidence-building actions
- Timeline and effort estimates
- Links from each action to the role gaps it addresses

Key requirements:

- Plans are generated from alignment gaps and capability graph state.
- Actions are sequenced by impact, effort, and dependency.
- Plans update when the resume, capability graph, role requirements, or alignment report changes.
- Recommendations include rationale and confidence.

## 8. MVP Scope

### In Scope

- Resume PDF upload and resume text extraction
- Resume Intelligence extraction and review workflow
- Talent Capability Graph with evidence and confidence
- Job description analysis and Role Intelligence
- Hidden competency inference with rationale
- Talent-Role Alignment Report
- Strength and gap analysis
- Resume optimization suggestions tied to role requirements
- Career Development Plan based on alignment gaps
- Versioned profile, role, and report records
- Structured AI outputs with evidence, assumptions, and confidence

### Out of Scope for MVP

- Full resume document editor
- Automatic application submission
- Application pipeline and status tracking
- Real-time job board scraping
- Automated LinkedIn login or scraping
- LinkedIn integration
- Payment and billing
- Multi-user enterprise dashboards
- ATS integration
- Native mobile app

## 9. Primary User Stories

- As a candidate, I want to upload my resume so CareerLens can extract structured experience and evidence.
- As a candidate, I want to see a capability graph so I understand what I can credibly demonstrate.
- As a candidate, I want to analyze a target job description so I understand explicit and hidden role requirements.
- As a candidate, I want an alignment report showing strengths, gaps, evidence, and confidence.
- As a candidate, I want resume optimization suggestions that are specific to a target role.
- As a candidate, I want a development plan that tells me which capabilities to build next.

## 10. Success Metrics

### Activation

- Percentage of users uploading a resume
- Percentage of users completing resume review
- Percentage of users generating a capability graph
- Time from signup to first alignment insight

### Engagement

- Alignment reports generated per user
- Target roles analyzed per user
- Resume optimization sessions per report
- Career development plans generated and revisited
- Profile and capability graph updates over time

### Quality

- User-rated usefulness of capability mapping
- User-rated accuracy of role requirement extraction
- User-rated trust in evidence and confidence indicators
- Percentage of optimization suggestions accepted or saved
- Percentage of roadmap actions accepted or completed

### Outcome

- Users reporting clearer role fit decisions
- Users improving target-role readiness scores over time
- Users completing evidence-building projects or learning milestones
- Interview invitations or application outcomes reported voluntarily

## 11. UX Requirements

The UI should feel like a mature SaaS product inspired by Notion, Linear, Claude, and Stripe dashboard:

- Minimal and professional
- Calm colors
- Strong information hierarchy
- Dense but readable layouts
- Workspace-oriented navigation
- Structured pages and reports, not chatbot-only flow

Avoid:

- Generic chatbot-first UI
- Colorful AI mascot styling
- Overly playful gradients
- Unexplained black-box scores
- Resume-writer-only positioning

## 12. AI Requirements

- AI outputs must be structured and persisted as inspectable records.
- Extraction, capability mapping, role analysis, alignment scoring, resume optimization, and development planning should be separate workflows.
- Every important output should include evidence, assumptions, confidence, and source references.
- Users must be able to edit structured data instead of being locked into generated text.
- Scores must be directional and confidence-aware.
- The system must avoid fabricating resume evidence or making sensitive personal inferences.

## 13. Risk Considerations

- Resume parsing can misinterpret experience and affect downstream analysis.
- Hidden competency inference may overreach without confidence controls.
- Alignment scores can mislead if the weighting model is opaque.
- Resume optimization must not invent achievements.
- Career guidance must avoid false certainty.
- Sensitive career data requires strong privacy controls.

## 14. MVP Acceptance Criteria

- A user can upload a resume PDF and review extracted structured data.
- A user can generate a Talent Capability Graph with evidence and confidence.
- A user can analyze a role or job description into structured requirements.
- A user can generate a Talent-Role Alignment Report.
- A user can inspect evidence, assumptions, confidence, strengths, and gaps for each major alignment dimension.
- A user can receive resume optimization suggestions tied to target-role requirements.
- A user can receive a Career Development Plan based on prioritized gaps.
- Core flows are represented in the frontend design and backed by documented backend contracts.
