from pydantic import BaseModel
from typing import Optional

class FlightInput(BaseModel):
    departure_id: str  # Required: Departure airport code (e.g., "CDG,ORY")
    arrival_id: str  # Required: Arrival airport code (e.g., "LAX")
    outbound_date: str  # Required: Departure date (YYYY-MM-DD)
    return_date: Optional[str] = None  # Optional: Return date (YYYY-MM-DD)
    currency: Optional[str] = "USD"  # Optional: Currency (default: USD)
    hl: Optional[str] = "en"  # Optional: Language (default: English)
