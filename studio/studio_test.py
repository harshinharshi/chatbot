from langchain_groq import ChatGroq
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv
from datetime import datetime
import os
load_dotenv()
# 1. LLM initialization
Model_name = os.getenv("Model_name") # use the model "gemma2-9b-it" and see how the LLM get confused while calling the tools.
llm = ChatGroq(model=Model_name)

# 2. tools initialization
def datetime_now() -> str:
    """Get the current date and time."""
    return datetime.now().isoformat()

def creator_info() -> str:
    """Return information about your creator."""
    return "Harshin"

tools = [datetime_now, creator_info]

# 3. Bind tools to LLM
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)

# 4. LLM invoke function
def assistant(state: MessagesState):
   system_message = SystemMessage(content="You are a helpful assistant. Use the tools when necessary. you have two tools: datetime_now, creator_info.")
   return {"messages": [llm_with_tools.invoke([system_message] + state["messages"])]}

# 5. Build the graph
# which message class to use for the state
builder = StateGraph(MessagesState)

# Define nodes
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Define edges
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")
react_graph = builder.compile()