from smolagents import ToolCallingAgent
import model_utils
from tools.web_tools import UTU_events, UtahTechWebSearchTool

def build_agent(verbose: int = 2) -> ToolCallingAgent:
    model = model_utils.google_build_reasoning_model()

    tools = [
        UTU_events(),
        UtahTechWebSearchTool()
    ]

    agent = ToolCallingAgent(
        tools=tools,
        model=model,
        verbosity_level=verbose,
        stream_outputs=False,
        instructions="""You are an agent to help users know about Utah Tech University. Any questions
        about events, programs, classes or campus life should be answered using the tools provided.
        """
    )
    return agent


