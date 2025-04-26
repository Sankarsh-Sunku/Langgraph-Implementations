from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.agents import tool, create_react_agent
import datetime
from langchain_community.tools import TavilySearchResults
from langchain import hub
import os

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

llm=ChatGroq(groq_api_key=groq_api_key,model_name="llama-3.3-70b-versatile")

prompt = hub.pull("hwchase17/react")
search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

tools = [get_system_time, search_tool]
react_agent_runnable = create_react_agent(tools=tools, llm=llm, prompt=prompt)