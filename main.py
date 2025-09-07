from langchain_core.messages import HumanMessage
from src.graph.workflow import create_workflow

def main():
    """Main function to demonstrate the conversation system."""
    # Create the workflow
    graph = create_workflow()
    
    # Create a thread configuration
    config = {"configurable": {"thread_id": "1"}}

    print("=== Conversation System Demo ===\n")
    
    # Start conversation
    messages_to_send = [
        "hi! I'm Lance",
        "what's my name?",
        "i like Burgers!",
        "KFC is the best"
    ]
    
    for message_content in messages_to_send:
        print(f"User: {message_content}")
        input_message = HumanMessage(content=message_content)
        output = graph.invoke({"messages": [input_message]}, config)
        
        # Print the last message (model's response)
        for m in output['messages'][-1:]:
            m.pretty_print()
        print("-" * 50)
    
    # Print final graph state
    print("\n=== Final Graph State ===")
    graph_state = graph.get_state(config)
    print(f"Summary: {graph_state.values.get('summary', 'No summary yet')}")
    print(f"Number of messages: {len(graph_state.values.get('messages', []))}")

if __name__ == "__main__":
    main()