# 🤖 ChatBot Project

This project implements a modular and extensible chatbot using the Langchain, Langgraph, and Groq ecosystem. The chatbot is designed with a clear separation of concerns, making it easy to maintain, extend, and understand.

---

## 📁 Project Structure

```
chatbot/
├── src/
│   ├── llm.py            # LLM initialization and management
│   ├── graph.py          # ReAct graph construction and management
│   └── tools.py          # Tool functions and tool list
├── test/
│   └── langgraph_studio.py # Langgraph studio configuration
├── .env.example      # Environment variables template
├── main.py           # Main execution script
├── requirements.txt  # Dependencies
└── README.md         # This file
```

---

## 🔧 Key Features

- **Modular Architecture:** The project is divided into modules for the LLM, the graph, and the tools, promoting a clean and organized codebase.
- **Class-Based Design:** The core logic for the LLM and the ReAct graph is encapsulated in classes, making the code more reusable and testable.
- **Environment-Based Configuration:** Sensitive information and model configurations are managed through environment variables, ensuring that no sensitive data is hard-coded.
- **Extensible Tool System:** New tools can be easily added by defining a function and adding it to the `tools` list in `src/tools.py`.
- **ReAct Agent:** The project uses a ReAct (Reasoning and Acting) agent, which can reason about problems and use tools to solve them.
- **Langgraph Studio Integration:** The project is configured to work with the Langgraph Studio for debugging and visualizing the agent's behavior.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- An account with [Groq](https://wow.groq.com/) to obtain an API key.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/360mots/ChatBot.git
    cd chatbot
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the environment variables:**
    ```bash
    cp .env.example .env
    ```
    Open the `.env` file and add your Groq API key and other configurations.

### Running the Chatbot

To run the chatbot, execute the `main.py` script:

```bash
python main.py
```

---

## 📝 File Overview

-   **`main.py`**: The entry point of the application. It initializes the `ReActGraph` and sends a sample message to it.
-   **`src/llm.py`**: This file contains the `LLMManager` class, which is responsible for initializing the `ChatGroq` model, binding the tools to it, and defining the `assistant` function that is called by the graph.
-   **`src/graph.py`**: This file contains the `ReActGraph` class, which builds and manages the ReAct agent using `langgraph`. It defines the nodes (assistant, tools) and edges of the graph.
-   **`src/tools.py`**: This file defines the tools that the agent can use. Currently, it includes `datetime_now` and `creator_info`.
-   **`test/langgraph_studio.py`**: This file is used to configure the Langgraph Studio. It imports the `ReActGraph` and makes it available to the studio.
-   **`requirements.txt`**: This file lists all the Python dependencies of the project.
-   **`.env.example`**: A template for the environment variables.

---

## 🛠️ How to Add a New Tool

To add a new tool to the chatbot, follow these steps:

1.  **Define the tool function** in `src/tools.py`. The function should have a clear name and a docstring that explains what it does.

    ```python
    # src/tools.py

    def my_new_tool(param1: str, param2: int) -> str:
        """
        This is a description of my new tool.

        :param param1: Description of the first parameter.
        :param param2: Description of the second parameter.
        :return: A string with the result.
        """
        # Your tool logic here
        return f"Result: {param1}, {param2}"
    ```

2.  **Add the tool to the `tools` list** in `src/tools.py`.

    ```python
    # src/tools.py

    tools = [datetime_now, creator_info]
    ```

The chatbot will now have access to your new tool!

---

## 🎨 Langgraph Studio

This project is integrated with the Langgraph Studio, which allows you to visualize and debug the ReAct agent. To use the studio, you need to have `langgraph-cli` installed (`pip install langgraph-cli`).

To start the studio, run the following command in your terminal:

```bash
langgraph up
```

This will start a local server and provide you with a URL to view the studio.

---

## 💡 Notes

-   The project is structured for maintainability and testability.
-   You can easily swap the LLM by modifying the `LLMManager` class in `src/llm.py`.
-   The `main.py` script can be modified to create a more interactive chat experience.