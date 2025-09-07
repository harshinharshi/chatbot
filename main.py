import os

# → Define project structure
project_structure = {
    "conversational_chatbot": [
        {"src": [
            "chatbot.py",
            "schemas.py",
            "memory.py",
            "filtering.py",
            "summarization.py",
            "state_manager.py"
        ]},
        {"studio": [
            "langgraph.json",
            "requirements.txt"
        ]},
        {"tests": [
            "test_conversations.py"
        ]},
        "main.py",
        "requirements.txt",
        "README.md"
    ]
}

# → Function to create project structure
def create_structure(base_path, structure):
    for key, items in structure.items():
        folder_path = os.path.join(base_path, key)
        os.makedirs(folder_path, exist_ok=True)

        for item in items:
            if isinstance(item, dict):   # → subfolder
                create_structure(folder_path, item)
            else:                        # → file
                file_path = os.path.join(folder_path, item)
                with open(file_path, "w") as f:
                    f.write("")  # empty file

# → Run
if __name__ == "__main__":
    create_structure(".", project_structure)
    print("✅ Project structure created successfully!")
