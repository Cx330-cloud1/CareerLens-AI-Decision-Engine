# CareerLens

CareerLens is an AI Career Intelligence Platform that helps individuals understand their professional potential, analyze career opportunities, and make data-driven career decisions.

It is designed as a portfolio-quality AI SaaS product that bridges talent intelligence and market intelligence.

## Product Vision

CareerLens is not a resume optimizer or generic chatbot. It is a structured career intelligence workspace where users can answer deeper career questions:

- Who am I professionally?
- What opportunities fit me?
- Why do companies need these skills?
- What should I do next?

The product combines:

- LinkedIn-style talent profiling
- Notion-style personal workspace
- Claude-style AI agent interaction
- Gartner-style market intelligence

## Target Users

Phase 1 focuses on Chinese university students and early-career technology professionals targeting:

- Internet technology companies
- AI companies
- Software companies
- Enterprise technology companies

Supported career paths include:

- AI Engineer
- Software Engineer
- AI Product Manager
- AI Solution Engineer
- Data roles
- Other technology-related roles

## Core Modules

### Talent Intelligence

CareerLens turns resumes, projects, skills, LinkedIn-style profiles, and career preferences into structured professional profiles.

Outputs include:

- Technical capability
- Product capability
- Domain knowledge
- Strengths and weaknesses
- Suitable career directions

### Market Intelligence

CareerLens analyzes companies and industries so users understand the market context behind career opportunities.

Company intelligence includes:

- Business model
- AI strategy
- Product areas
- Technical focus
- Hiring preferences

### Decision Intelligence

CareerLens matches user profiles with role and company opportunities using explainable scoring.

Match reports include:

- Overall match score
- Skill alignment
- Experience relevance
- Domain alignment
- Career preference alignment
- Strengths, gaps, and application recommendation

### Career Strategy

CareerLens generates practical next steps:

- Career roadmap
- Skill improvement plan
- Project recommendations
- Application strategy

### Application Intelligence

CareerLens helps users manage:

- Target opportunities
- Application preparation
- Resume versions
- Interview preparation
- Application status

## Design Direction

CareerLens should feel like a mature SaaS product inspired by Notion, Linear, Claude, and Stripe dashboard:

- Minimal
- Professional
- Premium
- Technology-focused
- Calm and information-dense

The product avoids generic chatbot UI and colorful AI assistant styling.

## Technical Direction

Recommended stack:

- Frontend: Vue 3, TypeScript, Vite
- Backend: Python FastAPI
- AI: OpenAI API
- Agent framework: LangGraph
- Database: PostgreSQL
- Vector database: Chroma or FAISS

## Documentation

The initial product and architecture design is documented in:

- [Product Requirements Document](docs/PRD.md)
- [System Architecture](docs/SYSTEM_ARCHITECTURE.md)
- [User Flow](docs/USER_FLOW.md)
- [Data Model](docs/DATA_MODEL.md)
- [MVP Roadmap](docs/MVP_ROADMAP.md)
- [Development Instructions](docs/DEVELOPMENT.md)
- [Project Structure](docs/PROJECT_STRUCTURE.md)

## MVP Product Loop

```text
Profile -> Market Context -> Opportunity Match -> Career Strategy -> Application Action
```

The MVP is complete when a user can create a structured career profile, browse company intelligence, generate an explainable opportunity match report, receive a roadmap, and manage the opportunity in an application pipeline.

## Current Status

CareerLens now has a production-oriented development skeleton for the planned Vue 3, FastAPI, LangGraph, PostgreSQL, and Chroma stack. Business workflows, detailed UI, and AI logic are intentionally not implemented yet.

## Repository Structure

```text
frontend/    Vue 3, TypeScript, Vite workspace shell
backend/     FastAPI API service with modular service boundaries
ai-service/  LangGraph-oriented AI orchestration service skeleton
data/        PostgreSQL schema, Chroma notes, and seed placeholders
docs/        Product, architecture, and development documentation
```

## Quick Start

```bash
cp .env.example .env
docker compose up --build
```

Local service URLs:

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/api/health
- Backend API docs: http://localhost:8000/api/docs
- AI service: http://localhost:8100/health
