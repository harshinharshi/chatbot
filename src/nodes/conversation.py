from typing import Dict, Any, List
from langchain_core.messages import SystemMessage, BaseMessage, AIMessage, HumanMessage, RemoveMessage
from langchain_groq import ChatGroq
from src.models.state import State
from src.config.settings import MODEL_NAME, MODEL_TEMPERATURE, MODEL_MAX_RETRIES

# Initialize the model
model = ChatGroq(
    model=MODEL_NAME,
    temperature=MODEL_TEMPERATURE,
    max_retries=MODEL_MAX_RETRIES,
)

def _filter_out_remove_messages(messages: List[BaseMessage]) -> List[BaseMessage]:
    """Filter out RemoveMessage objects from the messages list."""
    return [msg for msg in messages if not isinstance(msg, RemoveMessage)]

def call_model(state: State) -> Dict[str, Any]:
    """
    Call the model with conversation context and summary.
    
    Args:
        state: The current conversation state
        
    Returns:
        Dictionary containing the model's response
    """
    # Get the current summary and messages
    summary = state.get("summary", "")
    messages = state["messages"]
    
    # Prepare the context for the model
    context_messages = []
    
    # Add summary if it exists
    if summary:
        context_messages.append(
            SystemMessage(
                content=(
                    "Below is a summary of the conversation so far. "
                    f"Use this as context:\n\n{summary}\n\n"
                    "The most recent messages follow after this summary."
                )
            )
        )
    
    # Filter out any RemoveMessage objects
    filtered_messages = _filter_out_remove_messages(messages)
    
    # Add the actual conversation messages
    context_messages.extend(filtered_messages)
    
    try:
        # Get the model's response
        response = model.invoke(context_messages)
        return {"messages": response}
    except Exception as e:
        # Handle any errors gracefully
        error_message = f"I encountered an error while processing your request: {str(e)}"
        return {"messages": AIMessage(content=error_message)}