import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage
from langgraph.graph import MessagesState
from dotenv import load_dotenv
from src.tools import tools

# Load environment variables
load_dotenv()


class LLMManager:
    def __init__(self):
        """Initialize the LLM with model and tools."""
        self.model_name = os.getenv("Model_name")  # use "gemma2-9b-it" to see LLM confusion with tools
        self.llm = ChatGroq(model=self.model_name)
        self.llm_with_tools = self.llm.bind_tools(tools, parallel_tool_calls=False)
    
    def assistant(self, state: MessagesState):
        """LLM invoke function with system message."""
        system_message = SystemMessage(
            content="You are a helpful assistant. Use the tools when necessary. "
                   "you have two tools: datetime_now, creator_info."
        )
        return {"messages": [self.llm_with_tools.invoke(state["messages"])]}
    
    def get_llm_with_tools(self):
        """Return the LLM instance with bound tools."""
        return self.llm_with_tools