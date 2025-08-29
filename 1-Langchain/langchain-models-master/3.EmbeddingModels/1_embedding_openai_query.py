#  Working 
# We convert text to vectors, so that the vectors could have contextual understanding of the text for sementic search.

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

#  Dimention means the larger the vector the larget it will capture the contextual meaning

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))