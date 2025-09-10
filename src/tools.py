from datetime import datetime


def datetime_now() -> str:
    """Get the current date and time."""
    return datetime.now().isoformat()


def creator_info() -> str:
    """Return information about your creator."""
    return "Harshin"


# List of all available tools
tools = [datetime_now, creator_info]