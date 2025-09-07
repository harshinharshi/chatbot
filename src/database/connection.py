import sqlite3
import os
from src.config.settings import DB_PATH, USE_MEMORY_DB

def get_database_connection():
    """Get database connection based on configuration."""
    if USE_MEMORY_DB:
        return sqlite3.connect(":memory:", check_same_thread=False)
    else:
        # Ensure directory exists
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        return sqlite3.connect(DB_PATH, check_same_thread=False)