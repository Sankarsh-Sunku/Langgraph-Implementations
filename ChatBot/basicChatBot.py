import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import Annotated, TypedDict
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import add_messages, StateGraph, END


load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

llm=ChatGroq(groq_api_key=groq_api_key,model_name="llama-3.3-70b-versatile")

class BasicChatState(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: BasicChatState):
    return {
        "messages": [llm.invoke(state["messages"])]
    }

graph = StateGraph(BasicChatState)
graph.add_node("chatbot", chatbot)
graph.set_entry_point("chatbot")
graph.add_edge("chatbot", END)

app = graph.compile()

while True: 
    user_input = input("User: ")
    if(user_input in ["exit", "end"]):
        break
    else: 
        result = app.invoke({
            "messages": [HumanMessage(content=user_input)]
        })

        print(result)
"""
In your current code, there is no memory because after every user input, 
you only pass the latest message to the model — not the full conversation history. 
As a result, the AI treats each input like a brand-new, independent chat with no idea about previous interactions. 
Even though add_messages is available, it can only merge messages if you provide a list of all past messages. 
It doesn't automatically store memory for you. To actually maintain memory,
you need to manually keep a growing list (for example, a conversation list) that collects each 
HumanMessage and AIMessage turn-by-turn. Then, at every step, you pass this entire conversation list to the model. 
This way, the AI sees the full chat history and can respond more intelligently by remembering what has already been discussed
"""
