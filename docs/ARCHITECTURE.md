# System Architecture

## Overview
A multi-tenant, privacy-first RAG platform designed for cost efficiency and traceability. Uses self-hosted search (Typesense) and database (Postgres) components to avoid vendor lock-in and high managed service costs.

## Core Principles
1.  **Search > LLM**: solid lexical/hybrid search fundamentals before LLM inference.
2.  **Traceability**: Every generated answer must link back to specific source chunks.
3.  **Observability**: Full tracing of the "Query -> Plan -> Search -> Context -> Answer" pipeline.

## System Components

### 1. Services
*   **API Gateway (Python FastAPI)**
    *   **Responsibilities**: Authentication, Tenant/App management, Rate limiting, Proxying chat requests, Admin API.
    *   **Stateless**: Horizontal scaling.
*   **RAG Service (Python Module/Service)**
    *   **Responsibilities**: Query understanding (Planner), Search execution (Typesense), Context window construction, LLM Interaction (Answerer).
*   **Ingestion Worker (Python/Celery or ARQ)**
    *   **Responsibilities**: Asynchronous PDF processing, Layout analysis, Cleaning, Chunking, Embedding (optional), Indexing to Typesense.
*   **Telemetry Service/Module**
    *   **Responsibilities**: Asynchronous recording of traces, feedback, and metrics.
*   **frontend-dashboard (Next.js)**
    *   **Responsibilities**: Admin UI, Demo interfaces, Chunk Inspector, Trace Visualization.

### 2. Data Stores
*   **PostgreSQL (Primary Source of Truth)**
    *   `tenants`, `apps`, `users`, `api_keys`
    *   `documents` (metadata, status), `document_sections` (outline)
    *   `chats`, `messages`, `traces`, `feedback`
*   **Typesense (Search Engine)**
    *   Foundational for BM25/Lexical search.
    *   (Optional) Hybrid search if using built-in vector capabilities.
    *   **Schema**: `content`, `section_title`, `doc_id`, `app_id` (facet), `tenant_id` (facet), `page_number`.
*   **Object Storage (Blob/S3/MinIO)**
    *   Raw PDFs.
    *   Processed JSON artifacts (intermediate states).
*   **Redis**
    *   Job queues (Celery/ARQ).
    *   Caching frequent queries.
    *   Rate limiting counters.

## Data Flow

### Ingestion Pipeline
1.  **Upload**: User -> API -> Object Storage (Raw PDF) -> Postgres (Record Created status=PENDING) -> Queue.
2.  **Processing**: Worker -> Pull Job -> Download PDF -> Layout/Text Extraction -> Structure Detection (Outline).
3.  **Chunking**: Semantic chunking based on structure (Section + Paragraphs).
4.  **Indexing**: Chunks enriched with metadata (Breadcrumbs, Page `x` of `y`) -> Push to Typesense.
5.  **Completion**: Update Postgres status=READY.

### RAG Retrieval Pipeline
1.  **Request**: User -> API `/chat` -> RAG Service.
2.  **Plan**: LLM (Fast model) generates `QueryPlan` {intent, keywords[], synonyms[], filters}.
3.  **Search**: RAG Service executes Typesense query (`query_by`, `filter_by` tenant/app).
4.  **Context**: Top K chunks retrieved -> Neighbors fetched (if needed) -> Context Bundle constructed.
5.  **Generate**: LLM (Strong model) receives System Prompt + Context Bundle -> Streams Answer with citations.
6.  **Trace**: Telemetry records full execution path to Postgres.

## Deployment Topology
*   **Containerized**: All services defined in `docker-compose.yml`.
*   **Cloud Agnostic**: Can run on Azure VM, Google Compute Engine, or Azure Container Apps/GKE.
*   **Cost Optimized**: Can run on a single substantial node (e.g., 4 vCPU, 16GB RAM) for moderate loads.

## Security Architecture
*   **Isolation**: Logical isolation via `tenant_id` enforcement in ALL database queries and search filters.
*   **Auth**: OAuth2 / API Key based authentication.
*   **Secrets**: Env vars injected at runtime.
