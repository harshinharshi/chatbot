from langgraph.graph import MessagesState, START, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode
from src.llm import LLMManager
from src.tools import tools
from src.database import get_memory


class ReActGraph:
    def __init__(self):
        """Initialize the ReAct graph with LLM and tools."""
        self.llm_manager = LLMManager()
        self.graph = self._build_graph()
    
    def _build_graph(self):
        """Build and compile the ReAct graph."""
        # Initialize the state graph
        builder = StateGraph(MessagesState)
        memory = get_memory()
        
        # Define nodes
        builder.add_node("assistant", self.llm_manager.assistant)
        builder.add_node("tools", ToolNode(tools))
        
        # Define edges
        builder.add_edge(START, "assistant")
        builder.add_conditional_edges(
            "assistant",
            # If the latest message from assistant is a tool call -> routes to tools
            # If the latest message from assistant is not a tool call -> routes to END
            tools_condition,
        )
        builder.add_edge("tools", "assistant")
        
        return builder.compile(checkpointer=memory)
    
    def invoke(self, messages, config):
        """Invoke the graph with given messages."""
        return self.graph.invoke({"messages": messages}, config)
    
    def get_graph(self):
        """Return the compiled graph."""
        return self.graph