from langchain_core.tools import tool
from datetime import datetime

@tool
def get_current_time_details() -> dict:
    """
    Returns comprehensive details about the current date and time.
    """
    now = datetime.now()
    return {
        "current_date": now.strftime("%Y-%m-%d"),
        "current_time": now.strftime("%H:%M:%S"),
        "year": now.year,
        "month": now.strftime("%B"),
        "day_name": now.strftime("%A"),
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
    }