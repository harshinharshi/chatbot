from typing import Dict, Any
from langchain_groq import ChatGroq
from src.models.state import State
from src.config.settings import MODEL_NAME, MODEL_TEMPERATURE, MODEL_MAX_RETRIES

# Initialize the model
model = ChatGroq(
    model=MODEL_NAME,
    temperature=MODEL_TEMPERATURE,
    max_retries=MODEL_MAX_RETRIES,
)

def call_model(state: State) -> Dict[str, Any]:
    """
    Call the model with conversation context and summary.
    
    Args:
        state: The current conversation state
        
    Returns:
        Dictionary containing the model's response
    """
    # Get the model's response
    response = model.invoke(state["messages"])
    return {"messages": response}