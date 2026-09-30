from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
# 1. Prompt: a template with a blank {topic} to fill in
prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")

# 2. Model: the OpenAI chat model
model = ChatOpenAI(model="gpt-4o-mini")

# 3. Output parser: turn the model's reply into plain text
output_parser = StrOutputParser()

print("All three pieces are ready!")

chain = prompt | model | output_parser

print("Chain is ready!")

answer = chain.invoke({"topic": "Python"})

print(answer)

 