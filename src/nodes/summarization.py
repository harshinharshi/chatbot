from typing import Dict, Any
from langchain_core.messages import HumanMessage, RemoveMessage, AIMessage
from langchain_groq import ChatGroq
from src.models.state import State
from src.config.settings import MODEL_NAME, MODEL_TEMPERATURE, MODEL_MAX_RETRIES

# Initialize the model
model = ChatGroq(
    model=MODEL_NAME,
    temperature=MODEL_TEMPERATURE,
    max_retries=MODEL_MAX_RETRIES,
)

def summarize_conversation(state: State) -> Dict[str, Any]:
    """
    Summarize the conversation and maintain context by keeping recent messages.
    
    Args:
        state: The current conversation state containing messages and summary
        
    Returns:
        Dictionary with updated summary and messages
    """
    current_summary = state.get("summary", "")
    messages = state["messages"]
    
    # Prepare the conversation context for summarization
    conversation_context = "\n".join(
        f"{msg.type}: {msg.content}" 
        for msg in messages
        if not isinstance(msg, (RemoveMessage,))
    )
    
    # Create the summarization prompt
    if current_summary:
        prompt = (
            f"Previous Summary: {current_summary}\n\n"
            f"New Conversation Context:\n{conversation_context}\n\n"
            "Please update the summary to include the new conversation context. "
            "Focus on key points, decisions, and action items."
        )
    else:
        prompt = (
            f"Please summarize the following conversation:\n\n{conversation_context}\n\n"
            "Extract key points, decisions, and action items."
        )
    
    # Get the summary from the model
    response = model.invoke([HumanMessage(content=prompt)])
    new_summary = response.content
    
    # Keep the last 2 messages for context
    recent_messages = messages[-2:] if len(messages) > 2 else messages
    
    # Add a system message about the summarization
    summary_message = AIMessage(
        content=f"[System: The conversation has been summarized for context. {len(messages) - len(recent_messages)} previous messages were summarized.]"
    )
    
    # Mark old messages for removal (except the ones we want to keep)
    messages_to_remove = [
        RemoveMessage(id=msg.id) 
        for msg in messages 
        if msg not in recent_messages
    ]
    
    return {
        "summary": new_summary,
        "messages": messages_to_remove + [summary_message] + recent_messages
    }