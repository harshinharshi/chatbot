from langgraph.graph import StateGraph, START, END
from src.models.state import State
from src.nodes.conversation import call_model
from src.nodes.summarization import summarize_conversation
from src.graph.conditions import should_continue
from src.utils.memory import get_memory

def create_workflow():
    """Create and compile the conversation workflow."""
    # Get memory checkpointer
    memory = get_memory()
    
    # Define a new graph
    workflow = StateGraph(State)
    workflow.add_node("conversation", call_model)
    workflow.add_node("summarize_conversation", summarize_conversation) 

    # Set the entrypoint as conversation
    workflow.add_edge(START, "conversation")
    workflow.add_conditional_edges("conversation", should_continue)
    workflow.add_edge("summarize_conversation", "conversation")

    # Compile with checkpointer
    return workflow.compile(checkpointer=memory)