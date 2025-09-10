from langchain_core.messages import HumanMessage
from src.graph import ReActGraph


def main():
    """Main function to run the ReAct agent."""
    # Initialize the graph
    react_graph = ReActGraph()
    
    # Create test message
    messages = [HumanMessage(content="what is the 2*10/5, also mention your creators details")]
    
    # Invoke the graph
    result = react_graph.invoke(messages)
    
    # Print results
    print("=== Conversation Results ===")
    for message in result['messages']:
        message.pretty_print()


if __name__ == "__main__":
    main()