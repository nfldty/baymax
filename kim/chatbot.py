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
    
def chat(text, name):
    results = co.rerank(query=text, documents=docs, top_n=1, model='rerank-english-v2.0')
    response = co.chat(
        preamble_override=f"You are a virtual doctor assistant called Baymax, the user's name is {name}, don't say hello, welcome, or take care",
        model='6c1924a9-b363-4890-9e5e-6e72b24dfc5f-ft',
        message="The user asks : {text}. use the following data to answer the question.:" + results[0].document["text"] + "Please answer the user's questions according to given conversation.",
        return_chat_history=True)
    return response.text
