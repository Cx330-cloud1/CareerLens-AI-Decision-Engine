# CareerLens System Architecture

## 1. Architecture Goals

CareerLens should be built as a production-quality AI Talent-Role Alignment Platform with clean separation between resume ingestion, talent capability intelligence, role intelligence, alignment analysis, resume optimization, and career strategy.

Primary architecture goals:

- Support structured talent-role intelligence, not only chat messages
- Keep AI-generated conclusions traceable to resume, profile, role, and source evidence
- Allow users to review and correct extracted data
- Separate extraction, analysis, scoring, optimization, and planning workflows
- Preserve Vue 3, FastAPI, and independent AI service boundaries
- Provide a scalable SaaS foundation for future education, coaching, and enterprise talent workflows

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

### AI Service

- Separate AI service for extraction, graph building, role analysis, alignment, optimization, and planning workflows
- OpenAI API for language model and embedding capabilities
- LangGraph for multi-step workflow orchestration
- Chroma or FAISS for local/vector retrieval during MVP

### Infrastructure

- Docker Compose for local development
- PostgreSQL service
- Backend API service
- Frontend Vite service
- AI service
- Optional worker service for long-running AI jobs
- Object storage abstraction for resume files and generated artifacts

## 3. High-Level System Diagram

```text
Vue 3 Web App
  |
  | HTTPS / JSON
  v
FastAPI Backend
  |
  |-- Auth and User Service
  |-- Resume Service
  |-- Capability Graph Service
  |-- Role Intelligence Service
  |-- Alignment Report Service
  |-- Resume Optimization Service
  |-- Career Development Plan Service
  |-- AI Job Orchestration Service
  |
  |-- PostgreSQL
  |-- Object Storage
  |-- Vector Store
  |
  v
AI Service
  |
  |-- Resume Intelligence Workflows
  |-- Capability Intelligence Workflows
  |-- Role Intelligence Workflows
  |-- Alignment Engine Workflows
  |-- Resume Optimization Workflows
  |-- Career Strategy Workflows
  |
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

### Resume Service

Responsibilities:

- Store uploaded resume files and extracted text
- Store parsed resume sections
- Track resume versions and source artifacts
- Provide resume evidence records to capability and optimization workflows

Key entities:

- Resume
- ResumeVersion
- ResumeSection
- ResumeEvidence

### Profile and Capability Graph Service

Responsibilities:

- Store canonical user profile data
- Store extracted experiences, projects, education, skills, and preferences
- Build and persist Talent Capability Graph records
- Link capabilities to evidence and confidence scores
- Manage profile and graph versions

Key entities:

- User
- CareerProfile
- ProfileVersion
- Experience
- Project
- Education
- Skill
- Capability
- CapabilityEvidence
- CapabilityGap

### Role Intelligence Service

Responsibilities:

- Store reusable role templates for supported role families
- Store user-submitted job descriptions
- Extract explicit role requirements
- Infer hidden competencies with rationale and confidence
- Explain real job workflow and evaluation signals
- Normalize role requirements for alignment scoring

Key entities:

- RoleTemplate
- TargetRole
- RoleRequirement
- RoleWorkflow
- RoleCompetencyInference

### Alignment Report Service

Responsibilities:

- Compare a Talent Capability Graph with target role requirements
- Generate structured Talent-Role Alignment Reports
- Store score breakdowns, strengths, gaps, evidence, assumptions, and confidence
- Track historical alignment changes as resume, graph, or role data evolves

Scoring dimensions:

- Capability match
- Evidence strength
- Experience relevance
- Requirement coverage
- Gap severity
- Confidence

### Resume Optimization Service

Responsibilities:

- Generate target-role resume optimization suggestions
- Distinguish communication improvements from actual capability gaps
- Link every suggestion to role requirements and candidate evidence
- Store accepted, rejected, and revised suggestions for future iterations

### Career Development Plan Service

Responsibilities:

- Generate gap-based development plans
- Store milestones, learning actions, projects, and interview preparation items
- Connect actions to alignment gaps and evidence needs
- Update plans after profile, capability graph, target role, or report changes

### Post-MVP Application Workspace Service

Responsibilities:

Application management is postponed until after the MVP. A future service may manage opportunity pipelines, status, notes, resume versions, interview preparation, and outcomes.

## 5. AI Service Workflow Architecture

CareerLens should use dedicated structured workflows instead of a single general chatbot.

### Resume Intelligence Workflow

Inputs:

- Resume file metadata
- Extracted resume text
- Optional user-edited fields

Outputs:

- Parsed resume sections
- Experience, project, education, and skill candidates
- Evidence records
- Missing or weak evidence indicators
- Extraction confidence

### Capability Intelligence Workflow

Inputs:

- Resume evidence
- Structured profile records
- User corrections

Outputs:

- Talent Capability Graph
- Capability nodes and categories
- Evidence links
- Confidence scores
- Strengths and skill gaps

### Role Intelligence Workflow

Inputs:

- Job description text
- Role template data
- Company or industry context where available

Outputs:

- Explicit requirements
- Hidden competency inferences
- Role workflow explanation
- Evaluation signals
- Evidence examples
- Requirement confidence

### Alignment Engine Workflow

Inputs:

- Talent Capability Graph
- Target role requirements
- Resume evidence
- User preferences where relevant

Outputs:

- Overall alignment score
- Dimension score breakdown
- Strength analysis
- Gap analysis
- Evidence assessment
- Assumptions and confidence
- Recommended decision posture

### Resume Optimization Workflow

Inputs:

- Resume sections
- Alignment report
- Target role requirements
- Capability evidence

Outputs:

- Role-specific resume improvement suggestions
- Bullet-level guidance
- Evidence placement suggestions
- Gap warnings where rewriting is insufficient

### Career Strategy Workflow

Inputs:

- Capability graph
- Alignment report
- Skill and evidence gaps
- Target role workflow

Outputs:

- Career Development Plan
- Learning priorities
- Project recommendations
- Evidence-building actions
- Interview preparation focus
- Timeline and effort estimates

## 6. LangGraph Workflow Pattern

Each AI workflow should be modeled as a graph with explicit nodes:

```text
Load Context
  -> Validate Inputs
  -> Retrieve Relevant Knowledge
  -> Extract or Analyze
  -> Structure Output
  -> Critique / Consistency Check
  -> Persist Result
```

Benefits:

- Observable intermediate steps
- Easier testing
- Safer retries
- Cleaner separation of extraction, reasoning, scoring, and persistence

## 7. Data Flow Examples

### Resume to Capability Graph

```text
User uploads resume PDF
  -> Backend stores raw artifact
  -> Resume Service extracts text
  -> AI Service parses resume sections
  -> User reviews and edits extracted data
  -> Profile Service creates a profile version
  -> Capability Graph Service builds evidence-linked capabilities
```

### Job Description to Role Intelligence

```text
User submits a job description
  -> Role Intelligence Service stores target role
  -> AI Service extracts explicit requirements
  -> AI Service infers hidden competencies
  -> Role workflow and evaluation signals are generated
  -> Normalized role requirements are persisted
```

### Talent-Role Alignment

```text
User selects a capability graph and target role
  -> Alignment Report Service loads capabilities, evidence, and requirements
  -> AI Service computes structured alignment analysis
  -> Report stores scores, strengths, gaps, evidence, assumptions, and confidence
  -> User reviews the Talent-Role Alignment Report
```

### Resume Optimization and Development Plan

```text
User opens an alignment report
  -> Resume Optimization Service generates target-role suggestions
  -> Career Development Plan Service generates gap-based actions
  -> Suggestions and actions remain linked to role requirements and evidence gaps
```

## 8. API Design Principles

- REST endpoints for core CRUD and workflow triggers
- Strong Pydantic schemas for all contracts
- Async job model for long-running AI workflows
- Store generated result records rather than returning transient text only
- Return explainable structured objects from AI workflows
- Preserve version references for resume, capability graph, role, report, and plan records

## 9. Example API Surface

```text
POST   /api/auth/signup
POST   /api/auth/login

POST   /api/resumes
GET    /api/resumes
GET    /api/resumes/{resume_id}
POST   /api/resumes/{resume_id}/analyze

GET    /api/profile
PUT    /api/profile
GET    /api/profile/versions

GET    /api/capability-graphs/current
POST   /api/capability-graphs
GET    /api/capability-graphs/{graph_id}

POST   /api/roles/analyze
GET    /api/roles
GET    /api/roles/{target_role_id}
GET    /api/role-templates

POST   /api/alignment-reports
GET    /api/alignment-reports/{report_id}

POST   /api/resume-optimizations
GET    /api/resume-optimizations/{optimization_id}

POST   /api/development-plans
GET    /api/development-plans/{plan_id}
```

## 10. Vector Retrieval

Vector storage should support:

- Resume and project semantic retrieval
- Capability evidence retrieval
- Role requirement retrieval
- Alignment evidence retrieval
- Knowledge retrieval for curated role templates and workflow explanations

MVP options:

- Chroma for easier local development and metadata filtering
- FAISS for lightweight local vector indexing

Recommendation: start with Chroma for MVP because metadata filtering and developer ergonomics are useful for product iteration.

## 11. Observability

The platform should log:

- AI workflow execution status
- Prompt and model version identifiers
- Input record IDs, not sensitive full payloads in logs
- Token usage
- Latency
- Failure reason
- User feedback on generated outputs
- Version IDs for generated graph, role, report, optimization, and plan records

## 12. Security and Privacy

CareerLens handles sensitive resume and career data. Required practices:

- Store secrets in environment variables
- Encrypt sensitive documents at rest in production
- Avoid logging raw resumes or personal data
- Provide delete/export workflows for user data
- Use role-based access controls in future enterprise contexts
- Make AI usage transparent in product copy
- Prevent resume optimization workflows from fabricating claims

## 13. Deployment Path

### Local Development

- Docker Compose for PostgreSQL, backend, frontend, and AI service
- `.env` files for local secrets
- Alembic migrations for database schema

### MVP Hosting

- Frontend: Vercel, Netlify, or object hosting behind CDN
- Backend: Render, Fly.io, Railway, or container platform
- AI service: separate container service with job execution limits
- Database: managed PostgreSQL
- Vector store: Chroma service or persistent volume
- Object storage: S3-compatible bucket for resume artifacts

### Production Evolution

- Background worker queue for AI jobs
- Managed object storage
- Centralized logging
- Feature flags
- Rate limiting
- Billing and subscription services
- Organization and team support

## 14. Architectural Risks

- Resume parsing quality affects every downstream recommendation.
- Hidden competency inference can become unreliable without confidence and evidence controls.
- Alignment scoring may be misleading if weights and assumptions are hidden.
- Vector retrieval must not replace canonical relational records for important user data.
- Resume optimization must not create unsupported claims.
- Application pipeline, LinkedIn integration, and real-time job scraping should not leak into MVP architecture.
