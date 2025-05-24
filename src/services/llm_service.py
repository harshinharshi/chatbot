from langchain_groq import ChatGroq
from src.utils.config import load_environment

class LLMService:
    """Service class for managing LLM interactions."""
    
    def __init__(self, model_name: str = "llama-3.1-8b-instant"):
        load_environment()
        self.llm = ChatGroq(model=model_name)
    
    def get_llm(self):
        """Get the configured LLM instance."""
        return self.llm