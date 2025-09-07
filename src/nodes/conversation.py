from typing import Dict, Any
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from src.models.state import State
from src.config.settings import MODEL_NAME, MODEL_TEMPERATURE, MODEL_MAX_RETRIES
from src.tools.tools_list import get_current_datetime, personal_info

# Initialize the model
tools = [get_current_datetime, personal_info]
model = ChatGroq(
    model=MODEL_NAME,
    temperature=MODEL_TEMPERATURE,
    max_retries=MODEL_MAX_RETRIES,
).bind_tools(tools, parallel_tool_calls=False)

def call_model(state : State) -> dict :
    return {"messages":model.invoke(state['messages'])}

