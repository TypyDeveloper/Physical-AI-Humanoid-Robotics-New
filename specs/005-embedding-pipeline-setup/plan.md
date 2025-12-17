# Implementation Plan: Embedding Pipeline Setup (Updated)

**Branch**: `005-embedding-pipeline-setup` | **Date**: 2025-12-16 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/005-embedding-pipeline-setup/spec.md`

## Summary

This plan outlines the technical implementation for an embedding pipeline. The system will be a Python-based backend script that crawls text from the deployed Docusaurus site at `https://physical-ai-humanoid-robotics-ww8u.vercel.app/`. It will generate embeddings using the Cohere API and store them in a Qdrant vector database collection named `rag_embedding`. The entire logic will be contained within a single `backend/main.py` file, with dependencies managed by `uv`.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: `uv`, `cohere`, `qdrant-client`, `requests`, `beautifulsoup4`
**Storage**: Qdrant (Vector Database)
**Testing**: pytest
**Target Platform**: Any system with Python and uv installed.
**Project Type**: Single backend script.
**Target URL**: `https://physical-ai-humanoid-robotics-ww8u.vercel.app/`
**Constraints**: All ingestion logic must be implemented in a separate backend file named `main.py`. No code should be embedded in specs, plans, or configuration files.

## Constitution Check

The current constitution focuses on ROS 2 for robotics. This feature is a backend data pipeline and operates outside the scope of the current constitution. Therefore, there are no violations.

## Project Structure

### Documentation (this feature)

All planning and design artifacts are located within `specs/005-embedding-pipeline-setup/`.

### Source Code (repository root)

A single file, `main.py`, will be created inside a `backend` directory.

**File**: `backend/main.py`

This file will contain all the logic for the ingestion pipeline, organized into the following functions:
-   `get_all_urls`: Crawls the site to find all relevant page URLs.
-   `extract_text_from_url`: Fetches a URL and extracts clean text content.
-   `chunk_text`: Splits a long text into smaller chunks.
-   `embed`: Generates embeddings for a list of text chunks using Cohere.
-   `create_qdrant_collection`: Ensures the Qdrant collection (named `rag_embedding`) exists.
-   `save_chunk_to_qdrant`: Upserts a single vector chunk with metadata into Qdrant.
-   `main`: The main executable function that orchestrates the entire pipeline from start to finish.

**Structure Decision**: A single `backend/main.py` file will be used as explicitly requested. This approach is suitable for a self-contained script and emphasizes a clean separation from planning documents.

## Complexity Tracking

No constitutional violations were identified that require justification.