import sqlite3
import atexit
import os
from langgraph.checkpoint.sqlite import SqliteSaver


class DatabaseManager:
    """Manages SQLite database connections for LangGraph state persistence."""
    
    def __init__(self, db_path="src/state_db/example.db"):
        """Initialize the database manager with a database path."""
        self.db_path = db_path
        self.conn = None
        self._ensure_db_directory()
    
    def _ensure_db_directory(self):
        """Ensure the database directory exists."""
        db_dir = os.path.dirname(self.db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
    
    def get_connection(self):
        """Get a SQLite connection for the database."""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            # Register cleanup on exit
            atexit.register(self._cleanup)
        return self.conn
    
    def get_memory(self):
        """Get a SqliteSaver instance for LangGraph state persistence."""
        conn = self.get_connection()
        return SqliteSaver(conn)
    
    def _cleanup(self):
        """Clean up database connection and file on exit."""
        if self.conn:
            self.conn.close()
        
        try:
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
                print(f"[SUCCESS] Database file '{self.db_path}' deleted on exit.")
            else:
                print(f"[WARNING] Database file '{self.db_path}' not found to delete.")
        except Exception as e:
            print(f"[ERROR] Failed to delete database: {e}")


def get_memory():
    """Get a memory instance for LangGraph state persistence."""
    db_manager = DatabaseManager()
    return db_manager.get_memory()