# Observability & Telemetry

## 1. Tracing (The "Black Box" Recorder)
Every request generates a `trace_id`. We record key spans:
1.  **`planner`**: Input query, Output JSON, Latency.
2.  **`retrieval`**: Generated Typesense query, Raw Typesense results (Top K), Latency.
3.  **`merging`**: Reranking logic (if any), Context assembly.
4.  **`generation`**: System prompt, User prompt, Stream chunks (aggregated), Total Tokens, Latency.

## 2. Metrics (Prometheus/StatsD compatible)
*   `ingestion_jobs_total`: Counter (status=success/fail).
*   `ingestion_duration_seconds`: Histogram.
*   `search_latency_seconds`: Histogram.
*   `llm_latency_seconds`: Histogram.
*   `rag_feedback_total`: Counter (positive/negative).
*   `active_apps_gauge`: Number of apps with traffic > 0.

## 3. Dashboard Visualization
The internal Admin Dashboard will visualize:
*   **Traffic Light Status**: Green (Healthy) / Red (High Error Rate).
*   **Quality Signal**: % of answers with "No Information Found".
*   **Usage**: Top Queries / week.
*   **Slowest Traces**: List of traces taking > 10s.

## 4. Alerting Rules
*   **High Failure Rate**: If > 5% of `/chat` returns 5xx errors in 5m.
*   **Zero Search Results**: If > 20% of queries return 0 results (Indices might be broken).
*   **Hung Workers**: Ingestion queue depth growing without processing.
