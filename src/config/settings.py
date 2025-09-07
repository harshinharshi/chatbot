from dotenv import load_dotenv

load_dotenv()

# Model configuration
MODEL_NAME = "gemma2-9b-it"
MODEL_TEMPERATURE = 0.0
MODEL_MAX_RETRIES = 2

# Database configuration
DB_PATH = "state_db/conversation.db"
USE_MEMORY_DB = False  # Set to True for in-memory database, we are expecting an external folder for DB so set it as False

# Conversation settings
MAX_MESSAGES_BEFORE_SUMMARY = 5