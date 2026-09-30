'''
from langchain_huggingface import HuggingFaceEmbeddings

# Our small knowledge base (a list of sentences)
texts = [
    "Python is a programming language.",
    "Streamlit is used to build web apps.",
    "Dogs are friendly animals.",
    "Cats like to sleep a lot."
]

# Free, local embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
print("Ready!")
'''
'''
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Create LangChain embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=api_key
)

# Our small knowledge base
texts = [
    "Python is a programming language.",
    "Streamlit is used to build web apps.",
    "Dogs are friendly animals.",
    "Cats like to sleep a lot."
]

# Create FAISS vector store
vector_store = FAISS.from_texts(texts, embeddings)

print("All texts are stored in the vector store!")

'''
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Create LangChain OpenAI embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=api_key
)

# Our small knowledge base
texts = [
    "Python is a programming language.",
    "Streamlit is used to build web apps.",
    "Dogs are friendly animals.",
    "Cats like to sleep a lot."
]

# Create FAISS vector store
vector_store = FAISS.from_texts(texts, embeddings)

print("All texts are stored in the vector store!")

query = "Tell me about pets"

results = vector_store.similarity_search(query, k=2)   # k=2 means top 2 matches

print("Top matches for:", query)
for r in results:
    print("-", r.page_content)
    
vector_store.save_local("my_store")
vector_store = FAISS.load_local("my_store", embeddings, allow_dangerous_deserialization=True)