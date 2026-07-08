# CareerLens Development

## Prerequisites

- Docker and Docker Compose
- Node.js 22 for local frontend work outside Docker
- Python 3.11 for local backend or AI-service work outside Docker

## Environment

Copy the example environment file before running services:

```bash
cp .env.example .env
```

Set `OPENAI_API_KEY` only when AI workflows are implemented.

## Run With Docker Compose

```bash
docker compose up --build
```

Services:

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/api/health
- Backend docs: http://localhost:8000/api/docs
- AI service: http://localhost:8100/health
- Chroma: http://localhost:8001
- PostgreSQL: localhost:5432

## Local Frontend

```bash
cd frontend
npm install
npm run dev
```

## Local Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
uvicorn app.main:app --reload
```

## Local AI Service

```bash
cd ai-service
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
uvicorn app.main:app --host 0.0.0.0 --port 8100 --reload
```

## Architecture Boundaries

- `frontend/` contains the Vue workspace shell and page-level route structure.
- `backend/` owns product APIs, relational persistence, and service boundaries.
- `ai-service/` owns LangGraph agents, prompt versions, RAG utilities, and AI pipelines.
- `data/` contains schema, vector-store notes, and seed data placeholders.
- `docs/` contains architecture and development documentation.

Business workflows and AI graph logic are intentionally not implemented in this skeleton.
