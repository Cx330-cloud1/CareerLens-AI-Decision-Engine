# CareerLens Product Requirements Document

## 1. Product Overview

CareerLens is an AI Career Decision Engine for university students and early-career technology professionals. It helps users decide which roles and companies are worth pursuing, why they fit or do not fit, and what actions would most improve their chances.

CareerLens is not a resume optimizer, job board, application tracker, or generic chatbot. The MVP is a focused decision system that combines:

- Structured talent profiling
- Curated company and role intelligence
- Explainable, evidence-based fit analysis
- Confidence-aware career action planning

## 2. Positioning

CareerLens bridges talent intelligence, company intelligence, and role intelligence.

Users should move from reactive job application behavior to informed career strategy:

- Who am I professionally?
- Which company and role combinations fit me?
- What evidence supports or weakens that fit?
- What should I do next?

## 3. Target Users

### Phase 1 Users

- Chinese university students in computer science, AI, software engineering, data science, information systems, and related fields
- Early-career technology professionals with 0-5 years of experience
- Users targeting internet, AI, software, enterprise technology, and platform companies

### Future Users

- Global technology talent
- Career coaches and education programs
- Enterprise talent intelligence and internal mobility teams

## 4. Supported Career Paths

Initial supported paths:

- AI Engineer
- Software Engineer
- AI Product Manager
- AI Solution Engineer
- Data Analyst / Data Scientist / Data Engineer
- Other technology-related roles

## 5. Core User Problems

### Problem 1: Fragmented Self-Understanding

Users have resumes, projects, skills, internships, and preferences, but lack a structured model of their professional identity.

### Problem 2: Weak Market Context

Users often apply to companies without understanding company strategy, business model, technical focus, hiring preferences, or role expectations.

### Problem 3: Unclear Fit

Users do not know why a role fits or does not fit them. Existing tools often provide shallow keyword matching.

### Problem 4: No Actionable Career Strategy

Users need action plans, skill improvement plans, and project recommendations based on their current profile and target path.

## 6. Product Principles

- Explainability over black-box recommendations
- Structured intelligence over chat-only interaction
- Strategic guidance over one-off resume edits
- Calm professional SaaS experience over colorful AI assistant UI
- Confidence-aware guidance over false precision
- Evidence-backed recommendations over generic advice

## 7. Core Modules

## 7.1 Talent Intelligence Layer

### Career Profile Agent

Inputs:

- Resume
- Structured profile import
- Projects
- Skills
- Education
- Work experience
- Career preferences
- Target roles and industries

Outputs:

- Structured professional profile
- Technical capability assessment
- Product capability assessment
- Domain knowledge assessment
- Strengths
- Weaknesses
- Suitable career directions
- Evidence-backed capability map

### Key Requirements

- Users can upload or paste resume content.
- Users can manually edit parsed profile sections.
- The system extracts skills, experience, projects, education, and preferences.
- The system generates an explainable career identity summary.
- The system stores profile versions over time.

## 7.2 Company and Role Intelligence Layer

### Company DNA Analysis

The system provides structured company analysis for target employers such as Tencent, ByteDance, Google, Microsoft, and similar technology companies.

Company DNA analysis includes:

- Business model
- Core product areas
- AI strategy
- Technical focus
- Hiring preferences
- Common role families
- Candidate signals valued by the company
- Culture and working style signals where evidence is available
- Strategic talent needs inferred from company direction

### Role Intelligence

Role intelligence turns a target role into structured expectations that can be compared against a talent profile.

Role intelligence includes:

- Core responsibilities
- Required and preferred capabilities
- Seniority expectations
- Evaluation signals
- Common project evidence
- Interview and preparation focus

### Industry Intelligence

Industry intelligence includes:

- Emerging roles
- Skill trends
- Technology changes
- Hiring market shifts
- Role-specific capability expectations

### Key Requirements

- Users can search and save companies.
- Users can view structured company intelligence pages.
- Users can view role intelligence pages for supported career paths.
- Users can compare company-role combinations by relevance, capability requirements, and career fit.
- Admin or ingestion workflows can update curated company and role intelligence sources.

## 7.3 Decision Intelligence Layer

### Explainable Match Analysis Engine

The matching engine compares a user profile against a company-role target. The first version does not require real-time job scraping or a full application pipeline; users evaluate curated role templates or manually entered target roles.

The system explains:

- Overall match score
- Skill alignment
- Experience relevance
- Domain alignment
- Career preference alignment
- Strengths
- Skill gaps
- Evidence behind each judgment
- Confidence level for each score
- Decision recommendation

### Scoring Dimensions

- Skill alignment: overlap between required and demonstrated skills
- Experience relevance: internships, projects, work history, and responsibility level
- Domain alignment: match between industry knowledge and company domain
- Career preference alignment: location, role type, company type, working style, growth path
- Evidence strength: quality and specificity of supporting profile evidence
- Confidence: how complete and reliable the available data is

### Key Requirements

- Users can create company-role targets from curated companies, role templates, or manual input.
- Users can generate match reports.
- Each score includes evidence and explanation.
- Each score includes a confidence indicator and key assumptions.
- The system recommends next actions instead of only ranking targets.

## 7.4 Career Strategy Agent

The Career Strategy Agent generates:

- Career action plan
- Skill improvement plan
- Project recommendations
- Learning priorities
- Interview preparation focus
- Decision guidance for whether to pursue, prepare first, or deprioritize a target

### Key Requirements

- Strategy outputs must be grounded in the user's profile and target role.
- Recommendations must be sequenced by timeline and effort.
- Plans should be revisable when the user profile or target roles change.
- Plans should explain which match gaps each action addresses.

## 7.5 Post-MVP Application Intelligence

Application Intelligence is postponed until after the decision engine proves value. It may later help users manage:

- Target opportunities
- Application preparation
- Resume versions
- Interview preparation
- Application notes
- Status tracking

### Post-MVP Requirements

- Users can maintain an opportunity pipeline.
- Users can attach match reports to opportunities.
- Users can create role-specific preparation plans.
- Users can track status from research to offer decision.

## 8. MVP Scope

### In Scope

- User authentication placeholder design
- Profile creation from structured manual input and resume text
- AI-assisted profile analysis
- Career path selection
- Company DNA pages for a curated company set
- Role Intelligence module for supported role families
- Company-role target creation from curated templates or manual input
- Explainable match report
- Evidence-based matching with source references
- Confidence-aware scoring and assumptions
- Career action plan generation
- Career action plan tied to match gaps

### Out of Scope for MVP

- Application pipeline and status tracking
- Workspace-style notes and saved insights
- Enterprise dashboards
- Real-time job board scraping
- Automated LinkedIn login or scraping
- LinkedIn integration
- Payment and billing
- Multi-user coaching workflows
- Full ATS integration
- Native mobile app

## 9. Primary User Stories

- As a student, I want to upload my resume so CareerLens can build a structured professional profile.
- As an early-career engineer, I want to understand which roles fit me so I can focus my preparation.
- As a user targeting ByteDance, I want to understand the company's product areas and hiring preferences.
- As a user evaluating a company-role target, I want a match score with clear reasons, evidence, confidence, and gaps.
- As a user with skill gaps, I want a practical action plan and project recommendations.
- As a user comparing targets, I want to know which one to pursue now, prepare for later, or deprioritize.

## 10. Success Metrics

### Activation

- Percentage of users completing a career profile
- Percentage of users generating at least one match report
- Time from signup to first useful insight

### Engagement

- Weekly active users
- Company-role targets evaluated per user
- Action plans generated per user
- Repeated profile updates

### Quality

- User-rated usefulness of match explanations
- User-rated accuracy of profile analysis
- User-rated trust in confidence and evidence indicators
- Percentage of recommendations accepted or saved

### Outcome

- Applications submitted after using CareerLens
- Interview invitations reported
- Skill improvement milestones completed

## 11. UX Requirements

The UI should feel like a mature SaaS product inspired by Notion, Linear, Claude, and Stripe dashboard:

- Minimal and professional
- Calm colors
- Strong information hierarchy
- Dense but readable layouts
- Workspace-oriented navigation
- Structured pages, not chatbot-only flow

Avoid:

- Generic chatbot-first UI
- Colorful AI mascot styling
- Overly playful gradients
- Unexplained black-box scores

## 12. AI Requirements

- AI outputs must be grounded in user profile, company intelligence, role intelligence, and target data.
- The system should separate extraction, analysis, matching, and strategy generation.
- Important AI outputs should include evidence, assumptions, and confidence indicators.
- Users must be able to edit structured data instead of being locked into generated text.
- Generated outputs should be versioned where they affect career decisions.
- Scores must be directional and confidence-aware, not presented as precise predictions.

## 13. Risk Considerations

- Career advice must avoid false certainty.
- Company intelligence may become stale without update workflows.
- Resume parsing can misinterpret user experience.
- Match scores must not appear more precise than the underlying data supports.
- AI outputs must avoid discriminatory or sensitive personal inferences.

## 14. MVP Acceptance Criteria

- A user can create a profile and receive a structured career profile analysis.
- A user can browse at least several curated company intelligence pages.
- A user can browse role intelligence for supported career paths.
- A user can create a company-role target and generate an explainable match report.
- A user can inspect evidence, assumptions, and confidence for each match dimension.
- A user can receive a career action plan based on current profile and target role.
- All core flows are represented in the frontend design and backed by documented backend contracts.
