# CareerLens MVP Roadmap

## 1. MVP Objective

Build a production-quality first version of CareerLens that proves the core product loop:

```text
Talent Profile -> Company & Role Intelligence -> Explainable Match Analysis -> Career Action Plan
```

The MVP should demonstrate that CareerLens is an AI Career Decision Engine, not a resume tool, chatbot wrapper, job board, or application tracker.

## 2. Development Phases

## Phase 0: Product and Architecture Design

Status: current phase

Deliverables:

- Product requirements document
- System architecture
- User flow
- Data model
- MVP roadmap
- Portfolio-quality README

Exit criteria:

- Core product scope is clear
- Data model supports MVP flows
- Frontend and backend boundaries are defined
- AI agent responsibilities are separated

## Phase 1: Project Foundation

Goal: establish the technical baseline.

Deliverables:

- Monorepo or structured repository layout
- Vue 3 + TypeScript + Vite frontend
- FastAPI backend
- PostgreSQL local setup
- Environment configuration
- Basic linting and formatting
- Docker Compose for local development
- Initial API health check

Recommended structure:

```text
career-lens/
  frontend/
  backend/
  docs/
  prompts/
  docker-compose.yml
  README.md
```

Exit criteria:

- Frontend runs locally
- Backend runs locally
- Backend connects to PostgreSQL
- API health endpoint works

## Phase 2: Core Workspace UI

Goal: build the mature SaaS shell and primary navigation.

Deliverables:

- App layout with sidebar navigation
- Home dashboard
- Career Profile page
- Company Intelligence page
- Role Intelligence page
- Target Evaluation page
- Match Report page
- Career Action Plan page
- Design tokens and component conventions

Exit criteria:

- Product feels like a coherent SaaS workspace
- Navigation supports all MVP modules
- Empty states guide users through the decision loop

## Phase 3: Career Profile MVP

Goal: allow users to create and analyze a structured profile.

Deliverables:

- Career profile CRUD
- Resume text input or upload placeholder
- Experience, project, skill, and preference forms
- Profile analysis API
- Career Profile Agent workflow
- Profile version storage
- Capability map UI

Exit criteria:

- User can enter profile information
- AI can generate structured professional profile analysis
- User can edit the structured profile after analysis
- Profile versions are stored

## Phase 4: Company and Role Intelligence MVP

Goal: provide curated company DNA and role intelligence.

Deliverables:

- Company intelligence data model
- Company DNA fields for strategy, technical focus, talent signals, and evidence notes
- Seed data for initial companies:
  - Tencent
  - ByteDance
  - Google
  - Microsoft
- Company list and detail pages
- Role template data for supported career paths
- Role Intelligence pages with responsibilities, capability expectations, evidence examples, and interview focus
- Industry insight placeholder structure

Exit criteria:

- User can browse company intelligence
- User can understand business model, AI strategy, technical focus, and hiring signals
- User can browse role intelligence for supported paths
- Company and role data can be used as matching context

## Phase 5: Explainable Match Analysis MVP

Goal: generate explainable match reports.

Deliverables:

- Company-role target CRUD
- Role requirement normalization from templates or manual input
- Matching API
- Explainable Match Analysis Agent workflow
- Match report persistence
- Match report UI with score breakdown, evidence, assumptions, and confidence
- Gap and recommendation display

Exit criteria:

- User can create a company-role target
- CareerLens can generate a match report
- The report explains score dimensions, evidence, assumptions, and confidence
- The report recommends pursue now, prepare first, or deprioritize

## Phase 6: Career Action Plan MVP

Goal: convert profile gaps and match reports into focused action plans.

Deliverables:

- Action plan generation API
- Career Action Plan Agent workflow
- Action plan and action item data models
- Action plan UI
- Action items tied to match gaps and supporting evidence
- Time horizons for 2 weeks, 1 month, and 3 months

Exit criteria:

- User can generate an action plan for a target path or company-role target
- Action items are specific, sequenced, and grounded in match gaps
- User can track action item progress

## Phase 7: Quality, Safety, and Portfolio Polish

Goal: make the decision engine credible as a portfolio-quality SaaS product.

Deliverables:

- Error states
- Loading states for AI jobs
- Empty states
- Basic tests for backend services
- Basic frontend smoke tests
- Seed demo data
- Demo walkthrough
- README screenshots or product narrative
- Security and privacy review

Exit criteria:

- MVP is demoable end to end
- Core decision loop works reliably
- Product narrative is clear to reviewers, recruiters, and users

## Phase 8: Post-MVP Application Intelligence

Goal: support practical application management after the decision engine is validated.

Deliverables:

- Application pipeline data model
- Pipeline board or list view
- Application detail page
- Link applications to targets and match reports
- Preparation checklist
- Notes and next actions

Exit criteria:

- User can save a target to the application pipeline
- User can track preparation and application status
- Match reports and action plans connect to the application workflow

## Phase 9: Post-MVP AI Workspace Integration

Goal: provide agent interaction connected to structured product data.

Deliverables:

- AI workspace interface
- Context-aware prompts over profile, company, target, match, and action plan data
- Saved insights
- Agent run history
- Basic feedback capture

Exit criteria:

- User can ask career questions grounded in structured CareerLens data
- AI responses can reference structured CareerLens objects
- Useful answers can be saved as notes or actions

## 3. Suggested MVP Milestones

### Milestone 1: Static Product Prototype

Build the frontend SaaS shell and static pages with seeded data.

Purpose:

- Validate product feel
- Clarify information hierarchy
- Make the portfolio direction visible early

### Milestone 2: Profile and Market Data

Add backend, database, and profile/company APIs.

Purpose:

- Establish structured data model
- Move beyond static mockups

### Milestone 3: AI Profile Analysis

Implement the first agent workflow.

Purpose:

- Prove resume/profile to structured intelligence
- Establish model output schemas and persistence

### Milestone 4: Explainable Matching

Implement match reports.

Purpose:

- Prove the core product value
- Create explainable career decision intelligence

### Milestone 5: Action Plans

Add career action planning.

Purpose:

- Convert insight into action
- Complete the MVP loop

## 4. AI Implementation Roadmap

### Step 1: Structured Prompting

Use typed JSON outputs for:

- Profile extraction
- Capability analysis
- Match report
- Action plan generation

### Step 2: Agent Graphs

Move workflows into LangGraph:

- Input validation
- Retrieval
- Analysis
- Structured generation
- Critique
- Persistence

### Step 3: Evaluation

Create evaluation cases:

- Strong AI Engineer profile
- Weak AI Product Manager fit
- Strong Software Engineer fit
- Career changer profile
- Incomplete student profile
- Low-evidence match with low confidence

### Step 4: Feedback Loop

Capture user feedback:

- Accurate
- Useful
- Too generic
- Missing context
- Wrong assumption

## 5. Technical Priorities

Highest priority:

- Clear data model
- Reliable profile analysis
- Explainable matching
- Company DNA and role intelligence
- Confidence-aware scoring
- Professional SaaS UI

Medium priority:

- Vector retrieval
- Action item progress tracking

Later priority:

- Billing
- Enterprise features
- Job board integrations
- LinkedIn integration
- Application pipeline
- Workspace notes
- AI workspace
- Advanced analytics

## 6. MVP Non-Goals

Do not prioritize:

- Automated job scraping
- Real-time job scraping
- LinkedIn integration
- Application pipeline
- Workspace notes
- Social network features
- Mobile app
- Enterprise admin dashboards
- Payment system
- Large-scale content ingestion
- Complex workflow automation

## 7. Definition of Done for MVP

CareerLens MVP is done when a demo user can:

1. Create a structured career profile.
2. Receive AI-generated professional analysis.
3. Browse company DNA analysis.
4. Browse role intelligence.
5. Create a company-role target.
6. Generate an explainable match report with evidence, assumptions, and confidence.
7. Generate a practical career action plan.
8. Use the product as a coherent career decision engine.
