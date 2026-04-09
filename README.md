# Gujarat Vidyapith Chatbot

An intelligent conversational AI system that provides comprehensive information about Gujarat Vidyapith's history, philosophy, principles, and educational programs. Built with semantic search capabilities to deliver accurate, context-aware answers to user queries.

## 📋 Project Overview

This chatbot leverages modern NLP techniques and vector databases to create an interactive knowledge retrieval system. Users can ask questions about Gujarat Vidyapith across multiple domains - from its Gandhian founding principles to contemporary academic offerings. The system understands natural language queries and retrieves relevant information using semantic similarity matching.

**Key Concept:** Instead of traditional keyword matching, this chatbot uses embedding-based semantic search to understand the meaning behind user questions, enabling it to provide more accurate and contextually relevant answers.

## 🛠️ Tech Stack

### Core Framework
- **Streamlit** (v1.29.0) - Web interface framework for rapid Python app development
- **Python 3.x** - Programming language

### AI & NLP
- **ChromaDB** (v0.4.22) - Vector database for embedding storage and similarity search
- **Sentence Transformers** (v2.2.2) - Pre-trained transformer models for generating semantic embeddings
- **Transformers** (v4.36.2) - Hugging Face transformers library for NLP models
- **PyTorch** (v2.1.2) - Deep learning framework for ML operations

### Dependencies
- **Pydantic** (v2.5.3) - Data validation using Python type annotations
- **HNSWLIB** (v0.8.0) - Fast approximate nearest neighbor search algorithm
- **Requests** (v2.31.0) - HTTP library for web scraping

## ✨ Features

- **Semantic Search**: Uses embeddings to understand query intent, not just keywords
- **Conversational Interface**: Natural language question-answering format
- **Multiple Query Categories**: Supports basic info, historical, philosophical, and complex queries
- **Vector Database Backend**: Efficient storage and retrieval using ChromaDB
- **Beautiful UI**: Styled Streamlit interface with custom CSS and background imagery
- **Knowledge Base**: Curated data covering various aspects of Gujarat Vidyapith

## 📁 Project Structure

```
college_chatbot/
├── app.py                          # Main Streamlit application
├── app_improved.py                 # Enhanced version with additional features
├── build_index_chunked.py          # Script to build vector index from data
├── build_index_chunked_fixed.py    # Fixed version of index building
├── test_query.py                   # Query testing script
├── check_data.py                   # Data validation utility
├── debug_chroma.py                 # Debugging tool for ChromaDB
├── inspect_chroma.py               # Inspection tool for database
├── web_to_txt.py                   # Web scraping utility
├── requirements.txt                # Python dependencies
├── README.md                        # This file
├── q_a.md                          # Sample Q&A categories
├── data/                           # Knowledge base files
│   ├── basic_info.txt
│   ├── current_status.txt
│   ├── early_history.txt
│   ├── educational_philosophy.txt
│   ├── founding_purpose.txt
│   ├── key_principles.txt
│   └── notable_people.txt
└── chroma_store/                   # Vector database storage
    └── chroma.sqlite3
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/GayatriParimiDev/Uni_chatbot.git
cd college_chatbot
```

2. **Create a virtual environment:**
```powershell
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Build the knowledge index (if not already built):**
```bash
python build_index_chunked_fixed.py
```

## 📖 Usage

### Running the Application

```powershell
# Windows
.venv\Scripts\activate
streamlit run app.py

# macOS/Linux
source .venv/bin/activate
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Example Queries

**Basic Information:**
- "Who founded Gujarat Vidyapith?"
- "When was Gujarat Vidyapith established?"
- "Where is Gujarat Vidyapith located?"

**Historical Queries:**
- "Why was Gujarat Vidyapith founded?"
- "What is the connection between Gujarat Vidyapith and the Non-cooperation Movement?"
- "When did Gujarat Vidyapith become a deemed university?"

**Educational Philosophy:**
- "What is the educational philosophy of Gujarat Vidyapith?"
- "What role does khadi play at Gujarat Vidyapith?"
- "What is the medium of instruction?"

**Principles & Values:**
- "What are the main principles of Gujarat Vidyapith?"
- "What is Gujarat Vidyapith's stance on untouchability?"
- "Why does Gujarat Vidyapith focus on villages?"

**Complex Queries:**
- "How did Gujarat Vidyapith contribute to the freedom struggle?"
- "What makes Gujarat Vidyapith different from British colonial education?"
- "What programs does Gujarat Vidyapith offer today?"

## 🔧 Architecture & How It Works

### System Flow

1. **Data Ingestion**: Raw text files from the `data/` folder are processed and chunked
2. **Embedding Generation**: Text chunks are converted to embeddings using Sentence Transformers
3. **Vector Storage**: Embeddings are stored in ChromaDB with metadata
4. **Query Processing**: User queries are converted to embeddings using the same model
5. **Similarity Search**: ChromaDB finds the most relevant text chunks using vector similarity
6. **Response Generation**: Relevant chunks are formatted and presented to the user

### Key Components

- **Sentence Transformer Model**: Generates semantic embeddings for text
- **ChromaDB**: Handles efficient vector storage and similarity search
- **Streamlit UI**: Provides interactive interface for users
- **Data Pipeline**: Processes and chunks raw documents for optimal retrieval

## 📊 Knowledge Base

The chatbot is trained on comprehensive data about Gujarat Vidyapith including:

- **Basic Information**: Founding, location, key personnel
- **History**: Timeline, evolution, milestones
- **Educational Philosophy**: Teaching methodology, core values
- **Principles**: Core tenets, social stance
- **Current Status**: Modern offerings, programs, activities

## 🔍 Troubleshooting

**ChromaDB Connection Issues:**
```bash
python inspect_chroma.py  # Check database status
python debug_chroma.py    # Debug database issues
```

**Data Issues:**
```bash
python check_data.py      # Validate data files
python build_index_chunked_fixed.py  # Rebuild index
```

##📝 Notes

- The virtual environment folder (`.venv/`) is ignored in version control
- ChromaDB stores embeddings locally in `chroma_store/` directory
- Sentence Transformers will download the pre-trained model on first run
- Large language model files (~500MB) will be cached locally

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is open source and available under the MIT License.

---

**Developed by:** Gayatri Parimi  
**Repository:** [GayatriParimiDev/Uni_chatbot](https://github.com/GayatriParimiDev/Uni_chatbot)