from langchain_core.messages import HumanMessage
from src.graph.workflow import create_workflow

def process_message(graph, config, user_input):
    """Process a single message."""
    input_message = HumanMessage(content=user_input)
    output = graph.invoke(
        {"messages": [input_message]}, 
        config
    )
    
    # Print the AI's response
    print("\nAI:")
    for m in output['messages'][-1:]:
        print(m.content)
    print("\n" + "-" * 50 + "\n")

def main():
    """Main function to run the conversation system."""
    # Create the workflow
    graph = create_workflow()
    
    # Create a thread configuration
    config = {"configurable": {"thread_id": "1"}}

    print("=== Interactive Chat System ===")
    print("Type 'quit' to end the conversation.\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit condition
        if user_input.lower() == 'quit':
            print("\n=== Ending conversation ===")
            break
            
        # Skip empty input
        if not user_input:
            continue
            
        try:
            process_message(graph, config, user_input)
        except Exception as e:
            print(f"\nError: {str(e)}\n")

if __name__ == "__main__":
    main()