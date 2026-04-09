import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
import traceback

st.set_page_config(page_title="🎓 College Chatbot", layout="centered")
st.title("🎓 College Chatbot")
st.caption("Ask questions based on pre-stored college data (ChromaDB).")

CHROMA_PATH = "chroma_store"
COLLECTION_NAME = "college"

# --- Safe loading with error messages ---
@st.cache_resource
def load_model():
    try:
        return SentenceTransformer("all-MiniLM-L6-v2")
    except Exception as e:
        st.error("❌ Model loading failed. Check internet connection or reinstall sentence-transformers.")
        st.stop()

@st.cache_resource
def load_collection():
    try:
        client = chromadb.PersistentClient(path=CHROMA_PATH)
        return client.get_collection(COLLECTION_NAME)
    except Exception as e:
        st.error("⚠️ Could not load ChromaDB collection. Run build_index_chunked.py first.")
        st.code(traceback.format_exc())
        st.stop()

model = load_model()
collection = load_collection()

query = st.text_input("💬 Ask your question here:")

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question first.")
    else:
        try:
            query_emb = model.encode([query]).tolist()
            result = collection.query(query_embeddings=query_emb, n_results=3)
            docs = result.get("documents", [[]])[0]
            distances = result.get("distances", [[]])[0]

            if docs:
                st.subheader("📘 Answer:")
                
                # Show only the best match (lowest distance = most similar)
                best_answer = docs[0]
                st.write(best_answer)
     
        except Exception as e:
            st.error("❌ Something went wrong while searching.")
            st.code(traceback.format_exc())

# Display collection stats
with st.sidebar:
    st.header("📊 Database Stats")
    try:
        st.metric("Total Documents", collection.count())
    except:
        st.write("Collection not loaded")