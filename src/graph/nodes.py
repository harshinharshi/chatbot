from src.models.state import BasicChatState
from src.services.llm_service import LLMService

class ChatbotNode:
    """Node class for chatbot functionality."""
    
    def __init__(self):
        self.llm_service = LLMService()
    
    def chatbot(self, state: BasicChatState) -> dict:
        """Process chatbot interaction."""
        llm = self.llm_service.get_llm()
        return {
            "messages": [llm.invoke(state["messages"])]
        }