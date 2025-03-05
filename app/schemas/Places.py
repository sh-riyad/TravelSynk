from pydantic import BaseModel

class PlacesInput(BaseModel):
    query: str
    location: str
    language_code: str
    country_code: str