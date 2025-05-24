from langchain_core.messages import HumanMessage
from src.graph.builder import GraphBuilder

def main():
    """Main application entry point."""
    # Build the conversation graph
    graph_builder = GraphBuilder()
    app = graph_builder.build_graph()
    
    print("Chatbot started! Type 'exit' or 'end' to quit.")
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() in ["exit", "end"]:
            print("Goodbye!")
            break
        
        try:
            result = app.invoke({
                "messages": [HumanMessage(content=user_input)]
            })
            
            # Extract and print the AI response
            if result.get("messages"):
                ai_response = result["messages"][-1].content
                print(f"Assistant: {ai_response}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()