from datetime import datetime
from typing import Dict


def get_current_datetime() -> str:
    """Returns the current date and time in a human-readable format."""
    return f"Current date and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


def personal_info() -> Dict[str, str]:
    """Returns personal information about the chatbot."""
    return {
        "name": "Friday",
        "version": "1.0.0",
        "description": "A helpful chatbot assistant"
    }