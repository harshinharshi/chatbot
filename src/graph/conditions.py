from typing_extensions import Literal
from langgraph.graph import END
from src.models.state import State
from src.config.settings import MAX_MESSAGES_BEFORE_SUMMARY

def should_continue(state: State) -> Literal["summarize_conversation", END]:
    """Determine whether to end or summarize the conversation."""
    messages = state["messages"]
    
    # If there are more than the configured threshold, summarize
    if len(messages) > MAX_MESSAGES_BEFORE_SUMMARY:
        return "summarize_conversation"
    
    # Otherwise we can just end
    return END