"""
Basic conversation example showing how to use the system.
"""
from langchain_core.messages import HumanMessage
from graph.workflow import create_workflow

def run_basic_conversation():
    """Run a basic conversation example."""
    graph = create_workflow()
    config = {"configurable": {"thread_id": "example_1"}}
    
    # Example conversation
    messages = [
        "Hello, my name is Alice",
        "What's my name?",
        "I work as a software engineer",
        "What do I do for work?",
        "I love Python programming",
        "What programming language do I like?",
        "I also enjoy hiking on weekends",
        "What do I like to do on weekends?"
    ]
    
    for msg in messages:
        print(f"\nUser: {msg}")
        result = graph.invoke({"messages": [HumanMessage(content=msg)]}, config)
        result['messages'][-1].pretty_print()
    
    # Check final state
    state = graph.get_state(config)
    if state.values.get('summary'):
        print(f"\nConversation Summary: {state.values['summary']}")

if __name__ == "__main__":
    run_basic_conversation()