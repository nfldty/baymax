import json
import cohere
from . import classification

docs = []
from dotenv import load_dotenv
import os
# Load environment variables from .env
load_dotenv()
# Now you can access environment variables using `os.getenv()`
from cohere.responses.classify import Example
co = cohere.Client(os.getenv("COHERE_API_KEY"))
f = open('./kim/small_train.jsonl', 'r')
line= f.readline()
for i in range(100):
    docs.append(line)
    line = f.readline()
    
def chat(text):
    results = co.rerank(query=text, documents=docs, top_n=1, model='rerank-english-v2.0')
    response = co.chat(
        model='6c1924a9-b363-4890-9e5e-6e72b24dfc5f-ft',
        message="The user has the same issues as this conversation:" + results[0].document["text"] + "Please answer the user's questions according to given conversation. This is the user's questions: {text}")
    return response.text
