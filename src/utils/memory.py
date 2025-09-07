from langgraph.checkpoint.sqlite import SqliteSaver
from src.database.connection import get_database_connection

def get_memory():
    """Initialize and return the memory checkpointer."""
    conn = get_database_connection()
    return SqliteSaver(conn)