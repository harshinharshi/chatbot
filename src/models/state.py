from typing import TypedDict, Annotated
from langgraph.graph import add_messages

class BasicChatState(TypedDict):
    """State definition for the basic chatbot."""
    messages: Annotated[list, add_messages]