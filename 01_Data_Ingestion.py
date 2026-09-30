'''
# Create a sample file to load
text = """LangChain is a framework for building AI apps.
It helps connect language models with your own data.
RAG means Retrieval-Augmented Generation."""

with open("sample.txt", "w") as f:
    f.write(text)

print("sample.txt file created!")
'''
from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample.txt")
documents = loader.load()

print("Number of documents:", len(documents))
print("Content:")
print(documents[0].page_content)
