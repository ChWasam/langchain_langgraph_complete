# Working 

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
        # Here we will only get 100 tokens in output
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("When did Trump elected for second term")

print(result.content)

# First download pytorch then it will work 