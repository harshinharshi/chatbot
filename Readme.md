# LangGraph Conversation System

A conversational AI system built with LangGraph that maintains conversation context and automatically summarizes long conversations.

## Features

- Conversation state management with memory persistence
- Automatic conversation summarization when message count exceeds threshold
- SQLite-based checkpointing for conversation persistence
- Configurable model parameters and conversation settings

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy environment file and add your API key:
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

3. Create the state database directory:
   ```bash
   mkdir -p state_db
   ```

## Usage

### Basic Usage

```bash
python main.py
```

### Running Examples

```bash
python examples/basic_conversation.py
```

### Custom Configuration

Modify `config/settings.py` to adjust:
- Model parameters (temperature, max_retries)
- Database settings (path, in-memory vs persistent)
- Conversation settings (max messages before summarization)

## Project Structure

- `config/`: Configuration settings
- `models/`: State models and data structures
- `database/`: Database connection management
- `nodes/`: Individual workflow nodes (conversation, summarization)
- `graph/`: Workflow definition and conditions
- `utils/`: Utility functions (memory management)
- `examples/`: Example usage scripts
- `state_db/`: Database storage directory

## Architecture

The system uses a state graph with two main nodes:
1. **Conversation Node**: Handles model interactions with context
2. **Summarization Node**: Summarizes and trims conversation history

The workflow automatically decides whether to continue or summarize based on message count.

## Configuration Options

### Model Configuration (`config/settings.py`)

```python
MODEL_NAME = "gemma2-9b-it"          # Groq model to use
MODEL_TEMPERATURE = 0.0              # Response randomness (0.0 = deterministic)
MODEL_MAX_RETRIES = 2                # Max retry attempts for API calls
```

### Database Configuration

```python
DB_PATH = "state_db/conversation.db" # Path to SQLite database
USE_MEMORY_DB = False                # True for in-memory, False for persistent
```

### Conversation Settings

```python
MAX_MESSAGES_BEFORE_SUMMARY = 6     # Messages threshold for triggering summary
```

## API Usage Example

```python
from graph.workflow import create_workflow
from langchain_core.messages import HumanMessage

# Create workflow
graph = create_workflow()
config = {"configurable": {"thread_id": "unique_conversation_id"}}

# Send message
message = HumanMessage(content="Hello, how are you?")
result = graph.invoke({"messages": [message]}, config)

# Get response
response = result['messages'][-1]
print(response.content)
```

## Thread Management

Each conversation requires a unique `thread_id` in the config:

```python
# Different conversations
config1 = {"configurable": {"thread_id": "user_123"}}
config2 = {"configurable": {"thread_id": "user_456"}}

# Same thread continues conversation
config_continue = {"configurable": {"thread_id": "user_123"}}
```

## Environment Variables

Required environment variables in `.env`:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

## Dependencies

- `langgraph`: Workflow orchestration
- `langchain-core`: Core LangChain functionality
- `langchain-groq`: Groq model integration
- `pydantic`: Data validation
- `python-dotenv`: Environment variable management

## Error Handling

The system includes built-in error handling:
- API retry logic for transient failures
- Database connection error handling
- Graceful fallback when summarization fails

## Extending the System

### Adding New Nodes

Create new nodes in `nodes/` directory:

```python
# nodes/new_feature.py
from models.state import State

def new_feature_node(state: State) -> dict:
    # Your logic here
    return {"messages": processed_messages}
```

### Adding Conditional Logic

Extend conditions in `graph/conditions.py`:

```python
def should_use_new_feature(state: State) -> Literal["new_feature", "conversation"]:
    # Your condition logic
    pass
```

### Custom State Extensions

Extend the state model in `models/state.py`:

```python
class State(MessagesState):
    summary: Optional[str] = ""
    custom_field: Optional[str] = ""
    user_preferences: Optional[dict] = {}
```

## Troubleshooting

### Common Issues

1. **Database locked error**: Ensure only one process accesses the database
2. **API key not found**: Check `.env` file exists and contains `GROQ_API_KEY`
3. **Import errors**: Verify all dependencies are installed with `pip install -r requirements.txt`

### Debug Mode

Enable debug logging by adding to your script:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Performance Considerations

- Use in-memory database (`USE_MEMORY_DB = True`) for faster development
- Adjust `MAX_MESSAGES_BEFORE_SUMMARY` based on your use case
- Consider implementing message batching for high-volume scenarios

## Security Notes

- Keep your `.env` file secure and never commit it to version control
- Use environment-specific API keys for different deployment stages
- Consider implementing rate limiting for production deployments

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Support

[Add support contact information here]