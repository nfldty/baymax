import cohere
from dotenv import load_dotenv
import os
# Load environment variables from .env
load_dotenv()
# Now you can access environment variables using `os.getenv()`
from cohere.responses.classify import Example
co = cohere.Client(os.getenv("COHERE_API_KEY"))

chat_dataset = co.create_dataset(name="chat-dataset",
                                   data=open("./train_set.jsonl", "rb"),
                                   dataset_type="chat-finetune-input")
print(chat_dataset.await_validation())
                                   
chat_dataset_with_eval = co.create_dataset(name="chat-dataset-with-eval",
                                           data=open("./train_set.jsonl", "rb"),
                                           eval_data=open("./val_set.jsonl", "rb"),
                                           dataset_type="chat-finetune-input")
print(chat_dataset_with_eval.await_validation())
