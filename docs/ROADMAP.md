# Project Roadmap

## Stage 0: Foundations (Week 1)
**Goal**: Infrastructure scaffolding and database schemas.
*   [ ] Repository setup with `docs/`.
*   [ ] Docker Compose (Postgres, Typesense, Redis).
*   [ ] API Gateway skeleton (FastAPI).
*   [ ] Tenant/App CRUD Models & Migrations.
*   **Exit Criteria**: Can successfully create a Tenant and App via curl/Postman.

## Stage 1: Ingestion MVP (Week 2)
**Goal**: Get documents in and searchable.
*   [ ] Ingestion Worker (Celery/ARQ).
*   [ ] PDF Text Extraction (Unstructured/pypdf/DocIntel).
*   [ ] Simple Chunking Strategy.
*   [ ] Push to Typesense Index.
*   **Exit Criteria**: Upload a PDF and successfully search its contents via Typesense API.

## Stage 2: RAG MVP (Week 3)
**Goal**: End-to-end Chat functionality.
*   [ ] Query Planner Logic (LLM).
*   [ ] Context Builder Implementation.
*   [ ] Chat Endpoint `/v1/chat`.
*   [ ] Answer Generation with Citations.
*   **Exit Criteria**: `/chat` returns a coherent answer with correct citations for the uploaded PDF.

## Stage 3: Dashboard MVP (Week 4)
**Goal**: Visibility for Admins.
*   [ ] Next.js Admin Boilerplate.
*   [ ] App/Document Management UI.
*   [ ] Chat Playground (Demo Mode).
*   [ ] Feedback & Metrics Display.
*   **Exit Criteria**: Admin can log in, view docs, and run a demo query from the UI.

## Stage 4: QA & Corrections (Week 5)
**Goal**: Tools for quality improvement.
*   [ ] Chunk Inspector UI.
*   [ ] Trace Viewer.
*   [ ] "Golden Set" Regression Testing Tool.
*   **Exit Criteria**: Can identify a bad answer, inspect the trace, and fix the underlying chunking/search issue.

## Stage 5: Hardening (Week 6)
**Goal**: Production Readiness.
*   [ ] Rate Limiting.
*   [ ] Horizontal Scaling Configuration.
*   [ ] Comprehensive Security Audit.
*   [ ] Backup/Restore Procedures.
*   **Exit Criteria**: End-to-end Load Test passes; Security review clean.
