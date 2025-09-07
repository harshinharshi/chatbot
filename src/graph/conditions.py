from typing_extensions import Literal, List
from langgraph.graph import END
from langchain_core.messages import BaseMessage, RemoveMessage
from src.models.state import State
from src.config.settings import MAX_MESSAGES_BEFORE_SUMMARY

def should_continue(state: State) -> Literal["summarize_conversation", END]:
    """
    Determine whether to continue the conversation, summarize it, or end it.
    
    Args:
        state: The current conversation state
        
    Returns:
        "summarize_conversation" if the conversation should be summarized,
        END if the conversation should end
    """
    # Filter out RemoveMessage objects to only count actual messages
    actual_messages = [
        msg for msg in state["messages"] 
        if not isinstance(msg, RemoveMessage)
    ]
    
    # If we have more messages than the threshold, trigger summarization
    if len(actual_messages) >= MAX_MESSAGES_BEFORE_SUMMARY:
        return "summarize_conversation"
    
    # Continue the conversation
    return END