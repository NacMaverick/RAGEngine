# Security & Isolation

## 1. Multi-Tenant Isolation Strategy
*   **Logical Separation**:
    *   **Postgres**: Every table has `tenant_id` column. RLS (Row Level Security) recommended or strict ORM scoping.
    *   **Typesense**: Every document indexed usually has `tenant_id` field.
    *   **Search Enforcement**: Use Scoped Search Keys (Typesense) or strictly append `filter_by: tenant_id:=X` in the backend Wrapper. **Never** trust the client-side filter alone.
*   **Storage Separation**:
    *   Blob paths: `/{tenant_id}/{app_id}/docs/{doc_id}.pdf`.

## 2. Authentication & Authorization
*   **Admin/User Auth**:
    *   Standard OAuth2 (Google/Microsoft) or Email/Pass (JWT).
*   **API Access**:
    *   API Keys generated per App.
    *   Keys stored hashed/encrypted.

## 3. Data Privacy (LLM)
*   **Zero-Retention (External)**:
    *   Azure OpenAI/OpenAI Enterprise compliance: No training on customer data.
*   **PII Masking (Optional)**:
    *   Pipeline step to recognize Emails/SSNs and mask before sending to LLM (if high security required).

## 4. Audit Logging
*   Record immutable logs for:
    *   `DOCUMENT_UPLOAD`
    *   `DOCUMENT_DELETE`
    *   `APP_CONFIG_CHANGE`
    *   `API_KEY_REVOKE`
