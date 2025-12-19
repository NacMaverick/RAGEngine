# Test Plan

## 1. Testing Pyramid Strategy

### Level 1: Unit Tests (Python `pytest`)
*   **Focus**: Deterministic logic.
*   **Scope**:
    *   Text cleaning functions (regex validation).
    *   Chunking splitters (boundary checks).
    *   Query Planner JSON validation (schema check).
    *   Filter generation logic.

### Level 2: Integration Tests (`pytest` + Docker Services)
*   **Focus**: Subsystem interaction.
*   **Scope**:
    *   **Ingest**: PDF Upload -> DB Record -> Worker Pick -> Typesense Document exist.
    *   **Search**: Planner Output -> Typesense Query -> Results contain expected keywords.
    *   **Context**: List of Chunks -> Formatted Context String.

### Level 3: End-to-End (E2E) Tests
*   **Focus**: Full user journey.
*   **Scope**:
    *   User sends query -> System returns 200 OK + Answer + Trace ID.
    *   Feedback submission is linked to Trace ID.

### Level 4: Regression (Golden Dataset)
*   **Focus**: Quality consistency.
*   **Method**:
    *   Maintain `golden_questions.json` per App.
    *   Input: "What is the deductible?"
    *   Expected: Must cite Doc ID `123`, Page `5`.
    *   **Pass**: Retrieval Hit Rate > 90%.

## 2. Sample Datasets
*   **Simple**: "Employee Handbook" (Structured, clear headings).
*   **Complex**: "Technical Spec Sheet" (Tables, multi-column, raw text).

## 3. Performance Testing (Locust/K6)
*   **Metrics**:
    *   Ingestion: < 30s for standard 10-page PDF.
    *   Retrieval: < 2s for Search phase (excluding LLM generation time).
    *   Concurrency: 50 concurrent requests.
