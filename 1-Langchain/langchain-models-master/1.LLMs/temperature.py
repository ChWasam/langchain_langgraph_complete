from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)

# temerature = 0 =>  For same input you will always get same output 
#  Increase the temprature  will change the result in output every time. 
#  The greater the value of temp shows that the next output will be that much different from the previous one.
#  if you are making a app where you want same output everytime for same input then temp should be zero
#  if you are making a app where for same input you wanna get the some different output everytime then temp should be around 1.5