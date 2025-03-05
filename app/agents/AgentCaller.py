from langchain.agents import AgentExecutor, create_tool_calling_agent
from app.schemas.Agnet import AgentInput, AgentResponse

class AgentCaller:
    """
    A class to manage LangChain's ReAct agent execution with dynamic LLM, prompt, and tools.
    """

    def __init__(self, llm, prompt, tools):
        """
        Initializes the AgentCaller with an LLM, prompt, and tools.

        :param llm: An instance of ChatOpenAI.
        :param prompt: A ChatPromptTemplate to format the agent's responses.
        :param tools: A list of tool functions available for the agent.
        """
        self.llm = llm
        self.prompt = prompt
        self.tools = tools
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        self.agent = create_tool_calling_agent(self.llm_with_tools, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True, handle_parsing_errors=True)

    def invoke(self, input_data: AgentInput) -> AgentResponse:
        """
        Invokes the agent with a validated input question.

        :param input_data: An instance of AgentInput containing the user's question.
        :return: An instance of AgentResponse containing the agent's response.
        """
        try:
            response = self.agent_executor.invoke({"question": input_data.question})
            return AgentResponse(response=response["output"])
        except Exception as e:
            return AgentResponse(response=f"An error occurred while processing your request: {str(e)}")