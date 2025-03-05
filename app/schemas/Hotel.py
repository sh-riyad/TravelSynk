from pydantic import BaseModel
from typing import Optional

class HotelInput(BaseModel):
    q: str
    check_in_date: Optional[str] = None
    check_out_date: Optional[str] = None
    adults: Optional[str] = None
    children: Optional[str] = None
    gl: Optional[str] = None
    hl: Optional[str] = None
    currency: Optional[str] = None
    sort_by: Optional[str] = None
    free_cancellation: Optional[str] = None
    special_offers: Optional[str] = None