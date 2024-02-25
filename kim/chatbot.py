import json
import cohere
import classification
docs = []
from dotenv import load_dotenv
import os
# Load environment variables from .env
load_dotenv()
# Now you can access environment variables using `os.getenv()`
from cohere.responses.classify import Example
co = cohere.Client(os.getenv("COHERE_API_KEY"))
f = open('./very_small_train.jsonl', 'r')
line= f.readline()
while line:
    docs.append(line)
    line = f.readline()
    
def rerank_and_chat(text):
    results = co.rerank(query=text, documents=docs, top_n=5, model='rerank-english-v2.0')
    response = co.chat(
        model='6c1924a9-b363-4890-9e5e-6e72b24dfc5f-ft',
        message="The user has the same issues as this conversation:" + results[0].document["text"] + "Please answer the user's questions according to given conversation. This is the user's questions: {text}")
    return response.text

text = input("query: ")
while not classification.exit(text):
    print(rerank_and_chat(text))
    text = input("query: ")
