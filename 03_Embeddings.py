from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI embedding model
openai_embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=api_key
)

print("OpenAI embedding model is ready!")

text = "I love programming in Python."

# Generate embedding vector
vector = openai_embeddings.embed_query(text)

print("How many numbers in this vector?", len(vector))
print("First 5 numbers:", vector[:5])