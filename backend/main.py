import requests
import xml.etree.ElementTree as ET
import trafilatura
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import cohere

# -------------------------------------
# CONFIG
# -------------------------------------
SITEMAP_URL = "https://physical-ai-humanoid-robotics-new-lyart.vercel.app/sitemap.xml"
COLLECTION_NAME = "rag_embedding"

# Initialize Cohere
cohere_client = cohere.Client("dYieR9foAbNey52UVZg75klRRrVFKGKZB1BrT6Ia")
EMBED_MODEL = "embed-english-v3.0"

# Connect to Qdrant Cloud
qdrant = QdrantClient(
    url="https://3f6202c1-3003-4eaa-bdd7-9977731daf41.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.UQt5UW97l3CMfx8gXfRBHJb13gV1UrMIYKSk1pCy8cA"
)

# -------------------------------------
# Step 1 — Extract URLs from sitemap
# -------------------------------------
def get_all_urls(sitemap_url):
    xml = requests.get(sitemap_url).text
    root = ET.fromstring(xml)

    urls = []
    for child in root:
        loc_tag = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc_tag is not None:
            urls.append(loc_tag.text)

    processed_urls = []
    print("\nFOUND URLS (from sitemap):")
    for u in urls:
        corrected_url = u.replace("https://your-docusaurus-site.example.com", "http://localhost:3000")
        processed_urls.append(corrected_url)
        print(" -", corrected_url)

    return processed_urls

# -------------------------------------
# Step 2 — Download page + extract text
# -------------------------------------
def extract_text_from_url(url):
    try:
        html = requests.get(url).text
        text = trafilatura.extract(html)
        if not text:
            print("[WARNING] No text extracted from:", url)
        return text
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None

# -------------------------------------
# Step 3 — Chunk the text
# -------------------------------------
def chunk_text(text, max_chars=1200):
    chunks = []
    while len(text) > max_chars:
        split_pos = text[:max_chars].rfind(". ")
        if split_pos == -1:
            split_pos = max_chars
        chunks.append(text[:split_pos])
        text = text[split_pos:]
    chunks.append(text)
    return chunks

# -------------------------------------
# Step 4 — Create embedding
# -------------------------------------
def embed(text):
    response = cohere_client.embed(
        model=EMBED_MODEL,
        input_type="search_query",  # Use search_query for queries
        texts=[text],
    )
    return response.embeddings[0]

# -------------------------------------
# Step 5 — Store in Qdrant
# -------------------------------------
def create_collection():
    print("\nCreating Qdrant collection...")
    qdrant.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=1024,
            distance=Distance.COSINE
        )
    )

def save_chunk_to_qdrant(chunk, chunk_id, url):
    vector = embed(chunk)
    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=chunk_id,
                vector=vector,
                payload={
                    "url": url,
                    "text": chunk,
                    "chunk_id": chunk_id
                }
            )
        ]
    )

# -------------------------------------
# MAIN INGESTION PIPELINE
# -------------------------------------
def ingest_book():
    urls = get_all_urls(SITEMAP_URL)
    create_collection()
    global_id = 1

    for url in urls:
        print("\nProcessing:", url)
        text = extract_text_from_url(url)
        if not text:
            continue
        chunks = chunk_text(text)
        for ch in chunks:
            save_chunk_to_qdrant(ch, global_id, url)
            print(f"Saved chunk {global_id}")
            global_id += 1

    print("\n✔️ Ingestion completed!")
    print("Total chunks stored:", global_id - 1)

if __name__ == "__main__":
    ingest_book()
