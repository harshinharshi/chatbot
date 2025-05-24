# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup API Keys for Groq, OpenAI and Tavily
import os

from langchain_community.tools import DuckDuckGoSearchRun

OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm=ChatOpenAI(model="gpt-4o-mini")
# groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool = DuckDuckGoSearchRun(max_results=2)

#Step3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot"

# def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
#     llm=ChatOpenAI(model=llm_id)
#     # if provider=="Groq":
#     #     llm=ChatGroq(model=llm_id)
#     # elif provider=="OpenAI":
        

#     tools=[DuckDuckGoSearchRun(max_results=2)] if allow_search else []
#     agent=create_react_agent(
#         model=llm,
#         tools=tools,
#         state_modifier=system_prompt
#     )
#     state={"messages": query}
#     response=agent.invoke(state)
#     messages=response.get("messages")
#     ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
#     print(ai_messages[-1])
#     return ai_messages[-1]

llm =ChatOpenAI(model="gpt-4o-mini")
# tools=[DuckDuckGoSearchRun(max_results=2)] if allow_search else []
agent = create_react_agent(
    model=llm,
    tools=[search_tool],
    state_modifier=system_prompt
)
query="What is the capital of France? what is the current time there?"
state={"messages": query}
response=agent.invoke(state)
messages=response.get("messages")
ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
print(ai_messages[-1])
