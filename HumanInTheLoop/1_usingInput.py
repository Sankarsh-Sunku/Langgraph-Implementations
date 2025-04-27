from langgraph.graph import StateGraph, add_messages, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, BaseMessage
from dotenv import load_dotenv
import os
from typing import TypedDict, Annotated

"""
Using `input()` inside the LangGraph flow is okay for small demos but is **not suitable for production** 
because it blocks the program and waits for manual user typing, making it impossible to run on servers, 
handle multiple users concurrently, automate flows, or integrate into web apps or APIs. 
It also makes automated testing difficult because `input()` cannot easily be simulated or controlled in tests. 
In contrast, production-grade LangGraph apps use **interrupts** or **command messages** to collect decisions or 
feedback asynchronously, allowing the app to continue processing without blocking and making it scalable, testable, 
and suitable for real-world deployments.
"""

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

class State(TypedDict):
    messages : Annotated[list, add_messages]

#Names of the Nodes
GENERATE_POST = "generate_post"
GET_REVIEW_DECISION = "get_review_decision"
POST = "post"
COLLECT_FEEDBACK = "collect_feedback"


def generate_post(state: State): 
    return {
        "messages": [llm.invoke(state["messages"])]
    }

def review_post(state: State):
    post_content = state["messages"][-1].content
    print("\n📢 Current LinkedIn Post:\n")
    print(post_content)
    print("\n")

    decision = input("Post to LinkedIn? (yes/no): ")

    if decision.lower() == "yes":
        return POST
    else:
        return COLLECT_FEEDBACK
    

def post(state: State):  
    final_post = state["messages"][-1].content  
    print("\n📢 Final LinkedIn Post:\n")
    print(final_post)
    print("\n✅ Post has been approved and is now live on LinkedIn!")

def collect_feedback(state: State):  
    feedback = input("How can I improve this post?")
    return {
        "messages": [HumanMessage(content=feedback)]
    }

graph = StateGraph(State)

graph.add_node(GENERATE_POST, generate_post)
# graph.add_node(GET_REVIEW_DECISION, review_post)
graph.add_node(POST, post)
graph.add_node(COLLECT_FEEDBACK,collect_feedback)

graph.set_entry_point(GENERATE_POST)

graph.add_conditional_edges(GENERATE_POST, review_post)
graph.add_edge(POST, END)
graph.add_edge(COLLECT_FEEDBACK, GENERATE_POST)

app = graph.compile()

response = app.invoke({
    "messages": [HumanMessage(content="Write me a LinkedIn post on AI Agents taking over content creation")]
})

print(response)