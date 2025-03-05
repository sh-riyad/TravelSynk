from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from app.schemas.Agnet import AgentInput, AgentResponse
from app.tools.weather import get_city_lat_lon, get_weather
from app.tools.news import get_current_news
from app.agents.AgentCaller import AgentCaller
from app.prompts.AgentPrompt import WeatherNewsPrompt
from langchain.prompts import ChatPromptTemplate


@tool
def get_weather_news(input_text: AgentInput) -> str:
    """
    This travel itinerary planning assistant integrates multiple tools:

    1. get_city_lat_lon:
       - Retrieves latitude and longitude of a city using OpenWeather API.

    2. get_weather:
       - Retrieves weather details based on latitude and longitude.
    """


    # Initialize LLM
    llm = ChatOpenAI(model="gpt-4o")


    # Define all tools including WeatherTool
    tools = [get_city_lat_lon, get_weather, get_current_news]

    # Use AgentCaller for structured execution
    agent_caller = AgentCaller(llm=llm, prompt=ChatPromptTemplate.from_template(WeatherNewsPrompt), tools=tools)

    try:
        # Invoke the agent using AgentCaller
        response: AgentResponse = agent_caller.invoke(input_text)

        return response.response
    except Exception as e:
        return f"An error occurred while processing your request: {str(e)}"
