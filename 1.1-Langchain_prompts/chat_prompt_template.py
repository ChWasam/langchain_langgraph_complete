from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)


# We can also use sytemMessage, HumanMessage, AIMessage in chattemplete instead of tuple,
#  but when we print prompt it will not include the placeholder. This is an issue in langchain. 



#  chat_template = ChatPromptTemplate.format_messages([
#     ('system', 'You are a helpful {domain} expert'),
#     ('human', 'Explain in simple terms, what is {topic}')
# ])
#  This is the same as the above chat_template  

#  But recommended is the one used above 

# Prompt template => used for single turn messages 
# Chat Prompt template => used for multi turn messages 