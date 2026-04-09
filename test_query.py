import chromadb
from sentence_transformers import SentenceTransformer

# Paths and names
CHROMA_PATH = "chroma_store"
COLLECTION_NAME = "college"

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Init Chroma
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(COLLECTION_NAME)

# Ask a question
query = "Who founded Gujarat Vidyapith?"

# Embed the query
query_embedding = model.encode([query]).tolist()

# Search
results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)

# Print results
print("\n🔍 Query:", query)
print("🧠 Top matches:\n")
for i, doc in enumerate(results["documents"][0]):
    print(f"{i+1}. {doc}\n")

print("✅ Done.")