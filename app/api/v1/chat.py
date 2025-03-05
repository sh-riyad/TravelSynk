from fastapi import APIRouter, Depends, HTTPException, status
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from app.schemas.Chat import ChatInput, ChatResponse, ChatHistoryRequest, ChatHistoryResponse, StoreMessageInput
from app.prompts.ChatPrompt import ChatPrompt
from app.tools.Weather_News_agent import get_weather_news
from app.tools.Hotel_Places_Flight_agent import get_hotel_and_places_details
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.auth import get_current_user
from app.models import User
from app.db.messageHistory import store_chat_message, get_chat_history


ChatRouter = APIRouter()

message_history = []


@ChatRouter.post("/chat", response_model=ChatResponse)
def chat(input_data: ChatInput, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Chat endpoint that processes user input using the ChatOpenAI model and invokes tools when needed.
    """

    if not current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized")


    tools = [get_weather_news, get_hotel_and_places_details]

    # Initialize the LLM with the correct API key
    llm = ChatOpenAI(model="gpt-4o")
    llm_with_tools = llm.bind_tools(tools)

    chain = ChatPrompt | llm_with_tools

    # Add user message to history
    message_history.append(HumanMessage(content=input_data.message))

    # Invoke LLM with complete message history
    response = chain.invoke({"messages": message_history})

    message_history.append(response)

    if response.tool_calls:
        tool_mapping = {
            "get_weather_news": get_weather_news,
            "get_hotel_and_places_details": get_hotel_and_places_details
        }

        for tool_call in response.tool_calls:
            tool_name = tool_call["name"].lower()
            selected_tool = tool_mapping.get(tool_name)

            if selected_tool:
                tool_msg = selected_tool.invoke(tool_call)
                message_history.append(tool_msg)

    response = chain.invoke({"messages": message_history})

    message_history.append(AIMessage(content=response.content))

    store_chat_message(
        StoreMessageInput(
            user_id=current_user.id,
            thread_id=input_data.thread_id,
            message_type="HumanMessage",
            content=input_data.message
        ), db
    )

    store_chat_message(
        StoreMessageInput(
            user_id=current_user.id,
            thread_id=input_data.thread_id,
            message_type="AIMessage",
            content=response.content
        ), db
    )

    return ChatResponse(
        thread_id=input_data.thread_id,
        message=input_data.message,
        response=response.content
    )


# Retrieve Chat History
@ChatRouter.get("/chat/history")
def fetch_chat_history(input_text: ChatHistoryRequest = Depends(),
                       current_user: User = Depends(get_current_user),
                       db: Session = Depends(get_db)):
    """
    API endpoint to retrieve chat history.
    """
    chat_history = get_chat_history(input_text, user_id=current_user.id, db=db)

    return chat_history