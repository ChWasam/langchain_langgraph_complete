# Generally we use template to retrieve the chathistory

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)




#  Message placeholder because our chattemplate does not have record of last day,
# that is we will fetch messages from database and send them to llm with todays message so that the llm now the context
# so all past messages will directly come here at  MessagesPlaceholder