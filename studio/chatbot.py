from langgraph.graph import StateGraph, START, END
from src.models.state import State
from src.nodes.conversation import call_model
from src.utils.memory import get_memory
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from src.tools.tools_list import get_current_datetime, personal_info

# Initialize the model
tools = [get_current_datetime, personal_info]


"""Create and compile the conversation workflow."""
# Get memory checkpointer
memory = get_memory()

# Define a new graph
workflow = StateGraph(State)

# Add the conversation node
workflow.add_node("conversation", call_model)
workflow.add_node("tools", ToolNode(tools))
# workflow.add_node("summarize_conversation", summarize_conversation) 

# Set the entrypoint as conversation
workflow.add_edge(START, "conversation")
workflow.add_conditional_edges("conversation",tools_condition)
workflow.add_edge("tools", "conversation")
workflow.add_edge("conversation", END)
# workflow.add_edge("summarize_conversation", "conversation")

# Compile with checkpointer
graph = workflow.compile(checkpointer=memory)