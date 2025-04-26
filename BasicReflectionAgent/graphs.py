from chains import generation_chain, reflection_chain
from langchain_core.messages import BaseMessage, HumanMessage
from dotenv import load_dotenv
from typing import List, Sequence
from langgraph.graph import END, MessageGraph

load_dotenv()

REFLECT = "reflect"
GENERATE = "generate"
graph = MessageGraph() #graph (MessageGraph): An instance of `MessageGraph` used to manage the flow of messages in the application.

def generateNode(state):
    return generation_chain.invoke({
        "messages" : state
    })

def reflectionNode(state):
    return reflection_chain.invoke({
        "messages" : state
    })

graph.add_node(GENERATE, generateNode)
graph.add_node(REFLECT, reflectionNode)
graph.set_entry_point(GENERATE)

def conditionalEdge(state):
    if len(state) > 6:
        return END
    else:
        return REFLECT
    
graph.add_edge(REFLECT,GENERATE)
graph.add_conditional_edges(GENERATE,conditionalEdge)

app = graph.compile()
print(app.get_graph().draw_mermaid())
print(app.get_graph().print_ascii())

response = app.invoke(HumanMessage(content="AI Agents taking over content creation"))

print(response)