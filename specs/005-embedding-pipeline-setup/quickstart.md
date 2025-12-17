# Quickstart: Embedding Pipeline (Updated)

This guide provides the basic steps to set up and run the embedding pipeline.

## Prerequisites

-   Python 3.11+
-   `uv` package manager installed (`pip install uv`)

## Setup

1.  **Create Project Directory**:
    ```bash
    mkdir backend
    cd backend
    ```

2.  **Initialize Virtual Environment**:
    ```bash
    uv venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies**:
    Create a `requirements.txt` file with the following content:
    ```
    cohere
    qdrant-client
    requests
    beautifulsoup4
    ```
    Then run:
    ```bash
    uv pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    Create a `.env` file and add your API keys and target URL:
    ```
    COHERE_API_KEY="your_cohere_api_key"
    QDRANT_URL="your_qdrant_instance_url"
    QDRANT_API_KEY="your_qdrant_api_key"
    TARGET_URL="https://physical-ai-humanoid-robotics-ww8u.vercel.app/"
    ```

## Running the Pipeline

Place the pipeline logic in `main.py` and execute it:

```bash
python main.py
```

The script will then crawl the `TARGET_URL`, process the text, and upsert the embeddings into your Qdrant collection named `rag_embedding`.