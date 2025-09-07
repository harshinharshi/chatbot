from langgraph.graph import MessagesState
from typing import Optional

class State(MessagesState): # inbuilt reducer function
    """State model for the conversation system."""
    summary: Optional[str] = ""