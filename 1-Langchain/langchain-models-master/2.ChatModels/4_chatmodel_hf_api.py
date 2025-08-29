# Not working 

import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)

print(llm)
model = ChatHuggingFace(llm=llm)
print(model)

result = model.invoke("When did trump elected as a president ")

print(result.content)



#  HuggingFaceEndpoint
# How to Access HuggingFace Models with API
# There are also two ways to use this class.
#  You can specify the model with the repo_id parameter. 
# Those endpoints use the serverless API, which is particularly beneficial to people using pro accounts or enterprise hub. Still, regular users can already have access to a fair amount of request by connecting with their HF token in the environment where they are executing the code.
