from langchain_core.tools import tool
from app.schemas.Agnet import AgentInput, AgentResponse
from app.agents.AgentCaller import AgentCaller
from langchain_openai import ChatOpenAI
from app.tools.current_time import get_current_time_details
from app.tools.places import get_places_details
from app.tools.flight import get_flight_info
from app.tools.hotel import get_hotel_info
from app.prompts.AgentPrompt import HotelPlacesFlightPrmpt
from langchain.prompts import ChatPromptTemplate


@tool
def get_hotel_and_places_details(message: AgentInput) -> str:
    """
    This travel itinerary planning assistant integrates multiple tools:

    1. get_hotel_info:
       - Retrieves hotel details via the Google Hotels API.

    2. get_places_details:
       - Retrieves information on various places such as restaurants, coffee shops, cinema halls, etc., via the Google Places API.

    3. get_current_time_details:
       - Retrieves details about current date and time.

    4. get_flight_info:
       - Retrieves flight information via Google Flights API.
    """

    # Define tools and prompt
    tools = [get_current_time_details, get_places_details, get_flight_info, get_hotel_info]

    llm = ChatOpenAI(model="gpt-4o")

    # Use AgentCaller for structured execution
    agent_caller = AgentCaller(llm=llm, prompt=ChatPromptTemplate.from_template(HotelPlacesFlightPrmpt), tools=tools)

    try:
        # Invoke the agent using AgentCaller
        response: AgentResponse = agent_caller.invoke(message)

        return response.response
    except Exception as e:
        return f"An error occurred while processing your request: {str(e)}"
