from datetime import datetime
from typing import List, Callable


def datetime_now() -> str:
    """Get the current date and time.
    
    Returns:
        str: Current date and time in ISO format.
    """
    return datetime.now().isoformat()


def creator_info() -> str:
    """Return information about your creator.
    
    Returns:
        str: Creator information.
    """
    return "Rasputin"


# List of all available tools
tools: List[Callable] = [datetime_now, creator_info]