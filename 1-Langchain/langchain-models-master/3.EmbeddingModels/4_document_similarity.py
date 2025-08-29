# Working 

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# it  will give you the similarity scores between the two vectors. Here scores will be a new 2D vector

#  In cosine similarity both the values should be 2D list 
#  Here we made query_embedding the 2D list by [query_embedding]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

#  sorting on the basis of second number 
#  Sorted in assending order 

print(query)
print(documents[index])
print("similarity score is:", score)




