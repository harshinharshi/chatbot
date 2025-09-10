from langchain_core.messages import HumanMessage
from src.graph import ReActGraph


def main():
    """Main function to run the ReAct agent."""
    # Initialize the graph
    react_graph = ReActGraph()
    
    print("=== Start Chat (type 'quit' to exit) ===")

    while True:
        # Take user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == "quit":
            print("=== Conversation Ended ===")
            break

        # Wrap user input in a message
        messages = [HumanMessage(content=user_input)]

        # Invoke the graph
        result = react_graph.invoke(messages)

        # Print results
        for message in result['messages'][1:]:  # Skip the first message which is the user input
            message.pretty_print()
        print("-" * 40)


if __name__ == "__main__":
    main()