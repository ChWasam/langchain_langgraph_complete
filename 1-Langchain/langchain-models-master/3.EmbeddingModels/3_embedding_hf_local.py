# Working 

import os 
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['HF_HOME'] = 'D:/huggingface_cache'

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(documents)

print(str(vector))