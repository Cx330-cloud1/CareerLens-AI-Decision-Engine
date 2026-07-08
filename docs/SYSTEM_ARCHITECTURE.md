# CareerLens System Architecture

## 1. Architecture Goals

CareerLens should be built as a production-quality AI Career Decision Engine with clean separation between talent profiles, company and role intelligence, AI workflows, and career action planning.

Primary architecture goals:

- Support structured career intelligence, not only chat messages
- Keep AI-generated content traceable to source data
- Allow iterative profile and recommendation updates
- Separate product workflows from model provider details
- Provide a foundation for future enterprise talent intelligence
- Keep MVP scope focused on decision quality before application management

## 2. Recommended Stack

### Frontend

- Vue 3
- TypeScript
- Vite
- Pinia for client state
- Vue Router
- TanStack Query or equivalent for server state
- Tailwind CSS or a restrained component system

### Backend

- Python FastAPI
- Pydantic for request and response schemas
- SQLAlchemy or SQLModel for database access
- Alembic for migrations
- PostgreSQL as primary relational database

### AI and Agents

- OpenAI API for language model and embedding capabilities
- LangGraph for multi-step agent workflows
- Chroma or FAISS for local/vector retrieval during MVP

### Infrastructure

- Docker Compose for local development
- PostgreSQL service
- Backend API service
- Frontend Vite service
- Optional worker service for long-running AI jobs
- Object storage abstraction for resumes and generated artifacts

## 3. High-Level System Diagram

```text
Vue 3 Web App
  |
  | HTTPS / JSON
  v
FastAPI Backend
  |
  |-- Auth and User Service
  |-- Profile Service
  |-- Company Intelligence Service
  |-- Role Intelligence Service
  |-- Target Evaluation Service
  |-- Matching Service
  |-- Career Action Plan Service
  |-- Agent Orchestration Service
  |
  |-- PostgreSQL
  |-- Vector Store
  |-- Object Storage
  |-- OpenAI API
```

## 4. Core Backend Services

### Auth and User Service

Responsibilities:

- User registration and login
- User account settings
- Session and token management
- Future organization and team support

MVP can use a simple email/password or OAuth-compatible abstraction.

### Profile Service

Responsibilities:

- Store structured user profile data
- Store resume text and parsed profile fields
- Manage profile versions
- Provide profile context to agents

Key entities:

- User
- CareerProfile
- ProfileVersion
- Experience
- Project
- Skill
- Education
- CareerPreference

### Company Intelligence Service

Responsibilities:

- Store company profiles
- Store company AI strategy, business model, product areas, and technical focus
- Store role families and hiring signals
- Store company DNA attributes such as talent needs, working style signals, and evidence notes
- Provide retrieval context for matching and strategy agents

MVP can start with curated manually maintained company data.

### Role Intelligence Service

Responsibilities:

- Store reusable role templates for supported career paths
- Store capability expectations, seniority expectations, responsibilities, and evaluation signals
- Normalize manually entered target-role requirements
- Provide role context to matching and action plan agents

MVP role intelligence should be curated and editable. Real-time job scraping and LinkedIn integration are not part of the first version.

### Target Evaluation Service

Responsibilities:

- Store user-created company-role targets
- Connect targets to curated companies and role templates
- Preserve any manually entered role description or requirements
- Track target status as active or archived without managing an application pipeline

### Matching Service

Responsibilities:

- Compare user profile with role intelligence and company DNA
- Generate explainable score breakdowns
- Store match reports
- Track historical match changes as profiles evolve
- Store evidence links, assumptions, and confidence indicators for each match dimension

Scoring dimensions:

- Skill alignment
- Experience relevance
- Domain alignment
- Career preference alignment
- Evidence strength
- Confidence

### Career Action Plan Service

Responsibilities:

- Generate career action plans
- Store action items and milestones
- Connect actions to match gaps and supporting evidence
- Update action plans after profile or target changes

### Post-MVP Application Workspace Service

Responsibilities:

Application management is postponed until after the MVP. A future service may manage application pipeline status, notes, tasks, resume versions, and interview preparation.

## 5. Agent Architecture

CareerLens should use dedicated agent workflows instead of a single general chatbot.

### Agent Workflow Types

#### Career Profile Agent

Inputs:

- Resume text
- Structured profile fields
- User preferences

Outputs:

- Normalized profile
- Capability assessment
- Strengths and gaps
- Suitable career directions

#### Company DNA Agent

Inputs:

- Company data
- Curated research notes
- Industry context

Outputs:

- Business model summary
- AI strategy
- Technical focus
- Hiring preference analysis
- Candidate signal analysis
- Evidence and freshness metadata

#### Role Intelligence Agent

Inputs:

- Role template data
- Manually entered role description
- Curated role research notes

Outputs:

- Capability requirements
- Responsibilities
- Seniority expectations
- Evaluation signals
- Interview and preparation focus

#### Explainable Match Analysis Agent

Inputs:

- Career profile
- Role intelligence
- Company intelligence
- User career preferences

Outputs:

- Directional match score
- Score breakdown
- Evidence
- Gaps
- Assumptions
- Confidence indicators
- Decision recommendation

#### Career Action Plan Agent

Inputs:

- Career profile
- Match reports
- Target role
- Skill gaps

Outputs:

- Career action plan
- Learning plan
- Project recommendations
- Interview preparation focus
- Sequenced actions tied to match gaps

## 6. LangGraph Workflow Pattern

Each agent should be modeled as a graph with explicit nodes:

```text
Load Context
  -> Validate Inputs
  -> Retrieve Relevant Knowledge
  -> Analyze
  -> Score or Structure Output
  -> Critique / Consistency Check
  -> Persist Result
```

Benefits:

- Observable intermediate steps
- Easier testing
- Safer retries
- Cleaner separation of extraction, reasoning, and persistence

## 7. Data Flow Examples

### Resume to Career Profile

```text
User uploads resume text
  -> Backend stores raw artifact
  -> Profile Agent extracts structured fields
  -> User reviews and edits fields
  -> Profile Service creates profile version
  -> Capability assessment is generated
```

### Company-Role Match

```text
User creates company-role target
  -> Target Evaluation Service links company and role context
  -> Role Intelligence Service normalizes requirements
  -> Matching Service loads user profile
  -> Company Intelligence Service loads company context
  -> Role Intelligence Service loads role context
  -> Matching Agent computes score and explanation
  -> Match report is saved
  -> User sees strengths, gaps, and recommended actions
```

### Career Action Plan

```text
User selects target path
  -> Career Action Plan Service loads profile and match gaps
  -> Career Action Plan Agent generates plan
  -> User saves action plan
  -> Action items remain tied to evidence and match gaps
```

## 8. API Design Principles

- REST endpoints for core CRUD and workflow triggers
- Strong Pydantic schemas for all contracts
- Async job model for long-running AI workflows
- Store generated result records rather than returning only transient text
- Return explainable structured objects from AI workflows

## 9. Example API Surface

```text
POST   /api/auth/signup
POST   /api/auth/login

GET    /api/profile
PUT    /api/profile
POST   /api/profile/analyze
GET    /api/profile/versions

GET    /api/companies
GET    /api/companies/{company_id}

GET    /api/roles
GET    /api/roles/{role_template_id}

POST   /api/targets
GET    /api/targets
GET    /api/targets/{target_id}

POST   /api/matches
GET    /api/matches/{match_report_id}

POST   /api/action-plans
GET    /api/action-plans/{action_plan_id}
```

## 10. Vector Retrieval

Vector storage should support:

- Resume and project semantic retrieval
- Company intelligence retrieval
- Role requirement retrieval
- Match evidence retrieval

MVP options:

- Chroma for easier local development and metadata filtering
- FAISS for lightweight local vector indexing

Recommendation: start with Chroma for MVP because metadata filtering and developer ergonomics are useful for product iteration.

## 11. Observability

The platform should log:

- Agent workflow execution status
- Prompt and model version identifiers
- Input record IDs, not sensitive full payloads in logs
- Token usage
- Latency
- Failure reason
- User feedback on generated outputs

## 12. Security and Privacy

CareerLens handles sensitive career data. Required practices:

- Store secrets in environment variables
- Encrypt sensitive documents at rest in production
- Avoid logging raw resumes or personal data
- Use role-based access controls in future enterprise contexts
- Provide delete/export workflows for user data
- Make AI usage transparent in product copy

## 13. Deployment Path

### Local Development

- Docker Compose for PostgreSQL, backend, and frontend
- `.env` files for local secrets
- Alembic migrations for database schema

### MVP Hosting

- Frontend: Vercel, Netlify, or object hosting behind CDN
- Backend: Render, Fly.io, Railway, or container platform
- Database: managed PostgreSQL
- Vector store: Chroma service or persistent volume

### Production Evolution

- Background worker queue for AI jobs
- Managed object storage
- Centralized logging
- Feature flags
- Rate limiting
- Billing and subscription services

## 14. Architectural Risks

- AI workflows may become hard to evaluate without structured outputs.
- Market intelligence can become stale without source tracking and refresh cadence.
- Scoring may be misleading if weights are hidden or overly precise.
- Resume parsing quality affects downstream recommendations.
- Vector retrieval must not replace canonical relational records for important user data.
- Application pipeline, workspace notes, LinkedIn integration, and real-time job scraping should not leak into MVP architecture.
