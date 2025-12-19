# RAGEngine 🚀

> **Multi-Tenant RAG Platform with Hybrid Search**
> *Self-hosted, Privacy-focused, and Azure-ready.*

RAGEngine is a modular Retrieval-Augmented Generation (RAG) platform designed to ingest documents (PDFs), understand their structure, and provide high-accuracy answers using a "Search First, LLM Second" approach. It is built to run on standard containerized infrastructure (Docker/Kubernetes).

## 📚 Documentation
Detailed architectural and feature documentation is available in the [`docs/`](./docs) directory:

*   **[Architecture](./docs/ARCHITECTURE.md)**: System design, components (FastAPI, Typesense, Postgres), and data flow.
*   **[Features](./docs/FEATURES.md)**: Capability list (Ingestion, Planner, Context Builder).
*   **[Roadmap](./docs/ROADMAP.md)**: Phased implementation plan (Stages 0-5).
*   **[API Spec](./docs/API.md)**: Endpoints and Data Schemas.
*   **[Observability](./docs/OBSERVABILITY.md)**: Tracing, metrics, and dashboards.

## ⚡ Quick Start

### Prerequisites
*   Docker & Docker Compose
*   Python 3.11+ (for local development)
*   Git

### 1. Services Setup (Stage 0)
Start the infrastructure services (Postgres, Typesense, Redis, MinIO):

```bash
cp .env.example .env  # (If applicable, or use provided .env)
docker-compose up -d
```

Verify services are healthy:
*   **Typesense**: [http://localhost:8108/health](http://localhost:8108/health)
*   **MinIO Console**: [http://localhost:9001](http://localhost:9001) (User/Pass: `minioadmin`)

### 2. Backend Development
The API Gateway is located in `backend/`.

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🏗 System Modules

| Service | Tech Stack | Responsibility |
| :--- | :--- | :--- |
| **Gateway** | FastAPI | Auth, Rate Limiting, Chat Endpoint |
| **Worker** | Arq / Python | Async PDF Ingestion, Chunking, Indexing |
| **Search** | Typesense | Lexical (BM25) & Vector Hybrid Search |
| **Store** | Postgres | Metadata, Tenants, Traces, Feedback |

## 🧪 Testing

```bash
pytest backend/tests
```

---
*Built with ❤️ by Antigravity*
