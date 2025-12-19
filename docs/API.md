# API Specification (Internal Draft)

## Endpoints

### 1. Ingestion
*   `POST /v1/ingest/upload`: Multipart upload (PDF). Returns `job_id`.
*   `GET /v1/ingest/status/{job_id}`: Poll status.

### 2. Chat (RAG)
*   `POST /v1/chat/completions`:
    *   **Body**:
        ```json
        {
          "app_id": "uuid",
          "messages": [{"role": "user", "content": "..."}],
          "stream": true
        }
        ```
    *   **Response**: Standard OpenAI-compatible format + `x-trace-id` header.

### 3. Debugging & Traceability
*   `GET /v1/admin/traces/{trace_id}`: Returns full execution graph (Planner, Search, Context).
*   `GET /v1/admin/traces` (Filterable list).

### 4. Feedback
*   `POST /v1/feedback`:
    *   **Body**:
        ```json
        {
          "trace_id": "uuid",
          "rating": 1 (up) | -1 (down),
          "comment": "Missed the pricing table"
        }
        ```

### 5. Corrections (Guided)
*   `POST /v1/admin/corrections/pin`:
    *   Force a specific Chunk ID to appear for a specific Query phrase.
*   `POST /v1/admin/corrections/synonym`:
    *   Add a synonym entry to given App configuration.

## Data Schemas

### Chunk
```json
{
  "id": "uuid",
  "doc_id": "uuid",
  "text": "...",
  "page_start": 1,
  "page_end": 1,
  "section_title": "Introduction",
  "metadata": { ... }
}
```

### Trace
```json
{
  "id": "uuid",
  "timestamp": "iso8601",
  "query_plan": {
    "intent": "informational",
    "keywords": ["..."]
  },
  "retrieval_metrics": {
    "found_count": 10,
    "top_score": 0.85
  },
  "final_answer": "..."
}
```
