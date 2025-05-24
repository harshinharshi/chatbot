from langgraph.graph import StateGraph, END
from src.models.state import BasicChatState
from src.graph.nodes import ChatbotNode

class GraphBuilder:
    """Builder class for constructing the conversation graph."""
    
    def __init__(self):
        self.chatbot_node = ChatbotNode()
    
    def build_graph(self):
        """Build and return the compiled graph."""
        graph = StateGraph(BasicChatState)
        
        # Add nodes
        graph.add_node("chatbot", self.chatbot_node.chatbot)
        
        # Set entry point
        graph.set_entry_point("chatbot")
        
        # Add edges
        graph.add_edge("chatbot", END)
        
        return graph.compile()