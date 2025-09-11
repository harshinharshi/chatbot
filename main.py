from langchain_core.messages import HumanMessage
from src.graph import ReActGraph


class ChatApplication:
    """Main chat application class that handles the conversation loop."""
    
    def __init__(self):
        """Initialize the chat application."""
        self.react_graph = ReActGraph()
        self.thread_id = 1
        self.config = {"configurable": {"thread_id": str(self.thread_id)}}
    
    def start(self):
        """Start the chat application."""
        print("=== Start Chat (type 'quit' to exit) ===")
        
        while True:
            # Take user input
            user_input = input("You: ")
            
            # Handle user commands
            if self._handle_commands(user_input):
                break
                
            # Process user message
            self._process_message(user_input)
    
    def _handle_commands(self, user_input):
        """Handle special user commands.
        
        Returns:
            bool: True if the application should exit, False otherwise.
        """
        user_input = user_input.lower()
        
        if user_input == "quit":
            print("=== Conversation Ended ===")
            return True
            
        if user_input == "new":
            self.thread_id += 1
            print(f"=== New Conversation Thread {self.thread_id} Started ===")
            self.config = {"configurable": {"thread_id": str(self.thread_id)}}
            return False
            
        return False
    
    def _process_message(self, user_input):
        """Process a user message and get AI response."""
        # Wrap user input in a message
        messages = [HumanMessage(content=user_input)]
        
        # Invoke the graph
        result = self.react_graph.invoke(messages, self.config)
        print('AI: ', result['messages'][-1].content)
        print("-" * 40)


def main():
    """Main function to run the ReAct agent."""
    app = ChatApplication()
    app.start()


if __name__ == "__main__":
    main()