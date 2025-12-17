# Data Model: Embedding Pipeline

This document defines the key data entities for the embedding pipeline feature, as extracted from the feature specification.

## 1. Document

Represents the text content extracted from a single URL. This is the source material for an embedding.

-   **Fields**:
    -   `id`: A unique identifier for the document (e.g., UUID).
    -   `source_url`: (string) The URL from which the text was extracted. This acts as a reference back to the original content.
    -   `cleaned_text`: (string) The processed text content from the page, stripped of HTML and other irrelevant artifacts.
    -   `retrieval_date`: (datetime) The timestamp when the document was crawled and processed.
-   **Validation**:
    -   `source_url` must be a valid URL format.
    -   `cleaned_text` must not be empty.

## 2. Embedding

Represents the vector representation of a Document, stored in the vector database.

-   **Fields**:
    -   `vector_id`: The unique identifier for the vector in the database (e.g., UUID).
    -   `document_id`: The ID of the source `Document` entity. This links the vector back to its original text and metadata.
    -   `vector`: The high-dimensional array of floating-point numbers representing the text.
-   **Relationships**:
    -   An `Embedding` has a one-to-one relationship with a `Document`. Each document's text is converted into a single vector.
