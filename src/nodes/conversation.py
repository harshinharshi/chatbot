from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from src.models.state import State
from src.config.settings import MODEL_NAME, MODEL_TEMPERATURE, MODEL_MAX_RETRIES

# Initialize the model
model = ChatGroq(
    model=MODEL_NAME,
    temperature=MODEL_TEMPERATURE,
    max_retries=MODEL_MAX_RETRIES,
)

def call_model(state: State) -> dict:
    """Call the model with conversation context and optional summary."""
    # Get summary if it exists
    summary = state.get("summary", "")

    # If there is summary, then we add it
    if summary:
        # Add summary to system message
        system_message = f"Summary of conversation earlier: {summary}"
        # Append summary to any newer messages
        messages = [SystemMessage(content=system_message)] + state["messages"]
    else:
        messages = state["messages"]
    
    response = model.invoke(messages)
    return {"messages": response}