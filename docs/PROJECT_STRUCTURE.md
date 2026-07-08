# Project Structure

```text
frontend/
  src/
    pages/                 Vue route-level pages
    router/                Vue Router configuration
    stores/                Pinia stores
    styles/                Global shell styling

backend/
  app/
    api/                   FastAPI route modules
    core/                  Settings and shared configuration
    db/                    Database engine and sessions
    models/                Core domain data contracts
    schemas/               API request and response schemas
    services/              Modular business service boundaries

ai-service/
  app/
    agents/                LangGraph agent packages
    prompts/               Versioned prompt templates
    rag/                   Retrieval and vector-store utilities
    pipelines/             AI workflow orchestration
    core/                  AI-service settings

data/
  schemas/                 PostgreSQL schema files
  chroma/                  Local vector-store persistence notes
  seeds/                   Curated seed data placeholders

docs/
  DEVELOPMENT.md           Local setup and run instructions
  PROJECT_STRUCTURE.md     Skeleton map
```

The current architecture is a foundation. Service classes, route modules, and agent graph builders are placeholders by design.
