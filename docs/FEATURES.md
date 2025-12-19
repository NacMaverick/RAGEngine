# Features & Acceptance Criteria

## 1. Multi-Tenant Management
*   **F01: Tenant Isolation**
    *   **AC**: Data from Tenant A never appears in searches for Tenant B.
    *   **AC**: API keys are scoped to specific Apps within a Tenant.
*   **F02: Application Config**
    *   **AC**: Tenants can create multiple Apps (e.g., "Engineering", "HR").
    *   **AC**: Each App has distinct prompt settings and citation styles.

## 2. Ingestion Engine
*   **F03: PDF Intelligence**
    *   **AC**: Extracts text with layout awareness (headers vs body).
    *   **AC**: Handles multi-column PDFs correctly without garbling reading order.
*   **F04: Structural Chunking**
    *   **AC**: Chunks respect document boundaries (Chapters/Sections).
    *   **AC**: No chunks split mid-sentence.
*   **F05: Re-indexing**
    *   **AC**: Trigger re-processing of a document with updated chunking rules without re-uploading file.

## 3. Advanced Retrieval (RAG)
*   **F06: Query Planner**
    *   **AC**: Generates keywords and synonyms for every user query.
    *   **AC**: Identifies intent (e.g., "Compare", "Define").
*   **F07: Hybrid Search**
    *   **AC**: Uses Typesense for fuzzy/exact matching.
    *   **AC**: Filters by `tenant_id` and `app_id` are mandatory.
*   **F08: Context Builder**
    *   **AC**: Assembles a coherent context window from scattered chunks.
    *   **AC**: Includes "previous/next" chunk context if highly relevant.
*   **F09: Citations**
    *   **AC**: Every answer includes `[DocName, p.X]` citations.
    *   **AC**: Clicking a citation opens the specific page/chunk in Dashboard.

## 4. Dashboard & Observability
*   **F10: Trace Explorer**
    *   **AC**: View full JSON trace of any past request (Planner output, raw search results, final prompt).
*   **F11: Chunk Inspector**
    *   **AC**: Visualize how a document was split.
    *   **AC**: Search against specific docs to see why they did/didn't match.
*   **F12: Golden Regression / Demo**
    *   **AC**: Save "Golden Questions" per App.
    *   **AC**: One-click "Run All" to verify answers haven't degraded.
*   **F13: Feedback Loop**
    *   **AC**: Thumbs Up/Down is recorded.
    *   **AC**: Admin can filter traces by "Negative Feedback" to investigate.
