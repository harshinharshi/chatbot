import os

# Define the folder structure
structure = {
    "conversation_system": [
        "README.md",
        "requirements.txt",
        ".env.example",
        ".gitignore",
        {"config": ["__init__.py", "settings.py"]},
        {"models": ["__init__.py", "state.py"]},
        {"database": ["__init__.py", "connection.py"]},
        {"nodes": ["__init__.py", "conversation.py", "summarization.py"]},
        {"graph": ["__init__.py", "workflow.py", "conditions.py"]},
        {"utils": ["__init__.py", "memory.py"]},
        {"state_db": [".gitkeep"]},
        "main.py",
        {"examples": ["__init__.py", "basic_conversation.py"]},
    ]
}

def create_structure(base, items):
    """Recursively create files and directories"""
    for item in items:
        if isinstance(item, dict):
            for folder, contents in item.items():
                folder_path = os.path.join(base, folder)
                os.makedirs(folder_path, exist_ok=True)
                create_structure(folder_path, contents)
        else:
            file_path = os.path.join(base, item)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                pass  # Create empty file

# Run the function
for root, contents in structure.items():
    os.makedirs(root, exist_ok=True)
    create_structure(root, contents)

print("✅ Project structure created successfully!")
