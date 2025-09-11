import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

def get_memory():
    db_path = "src/state_db/example.db" # make sure to create the folder using mkdir, the .db file will be created in run time
    conn = sqlite3.connect(db_path, check_same_thread=False)
    memory = SqliteSaver(conn)
    return memory