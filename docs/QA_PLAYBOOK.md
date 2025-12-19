# QA Playbook: Debugging & Improving Answers

## Scenario A: "The answer is wrong/hallucinated."
1.  **Locate Trace**: Find the user's query in the Trace Explorer.
2.  **Check Context**: Look at the "Context Builder" step. Did we retrieve relevant chunks?
    *   **NO**: Go to Scenario B (Retrieval Failure).
    *   **YES**: The Context had the answer, but LLM missed it.
3.  **Action**:
    *   Verify System Prompt instructions.
    *   Check if context was too noisy (too many irrelevant chunks).
    *   Adjust `top_k` or `max_tokens` settings for the App.

## Scenario B: "The system said 'I don't know', but it's in the doc." (Retrieval Failure)
1.  **Inspect Planner**: Did the Query Planner extract the right keywords?
    *   *Bad Keywords?* -> Add synonyms or adjust Planner prompt.
2.  **Inspect Typesense**:
    *   Use the **Chunk Inspector** to search for the expected text manually.
    *   *Not Found?* -> Text Extraction failed or Chunking cut it weirdly. -> **Re-Ingest/Re-Chunk**.
    *   *Found but low score?* -> Keyword mismatch. -> **Add Hidden Keywords** or Boost fields.

## Scenario C: "It cited the wrong page."
1.  **Check Metadata**: Inspect the chunk's JSON. Does `page_number` match the PDF?
    *   *No*: PDF Parsing offset error.
2.  **Action**: Report bug in Ingestion Worker geometry parsing.

## Guided Corrections Tools
*   **Pinning**: If query is "Project Alpha", pin the "Alpha Overview" chunk to ensure it's always #1.
*   **Synonyms**: Map "CorpNet" -> "Corporate Network" in the App config.
