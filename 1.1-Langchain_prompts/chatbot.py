from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)


#  If we don't add SystemMessage, AIMessage and HumanMessage, chat_history will be maintained but the problem will be that we won't be able to identify that whether it is a AI Message or Human message 

#  So, we should also maintain that this message was maintain by who 

#  So ideally you should maintain a dictionary that the key will be AI or human 