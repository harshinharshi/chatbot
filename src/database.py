import sqlite3
import atexit
import os
from langgraph.checkpoint.sqlite import SqliteSaver

def get_memory():
    db_path = "src/state_db/example.db"
    conn = sqlite3.connect(db_path, check_same_thread=False)
    
    # Register cleanup on exit
    atexit.register(delete_database_file, db_path, conn)
    
    memory = SqliteSaver(conn)
    return memory

def delete_database_file(db_path, conn):
    """Delete the database file on exit."""
    conn.close()  # Close connection first
    try:
        os.remove(db_path)
        print(f"✅ Database file '{db_path}' deleted on exit.")
    except FileNotFoundError:
        print(f"⚠️  Database file '{db_path}' not found to delete.")
    except Exception as e:
        print(f"❌ Failed to delete database: {e}")