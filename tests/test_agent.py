from docketanalyzer_chat import Agent, Tool


class WeatherTool(Tool):
    """A tool to get the weather for a given location."""

    location: str

    def __call__(self, agent=None):
        """Mock tool call."""
        return f"The weather in {self.location} is 72 degrees farenheit."


class WeatherAgent(Agent):
    """A custom Agent that uses the WeatherTool."""

    def __init__(self):
        """Initialize the agent with fixed system prompt and tools."""
        self.setup(
            messages=[
                {
                    "role": "system",
                    "content": "Always rhyme, and use your tool if asked about weather",
                }
            ],
            tools=[WeatherTool],
            chat={"model": "gpt-4o-mini"},
        )


def test_default_agent():
    """Test default Agent with tools passed to init."""
    # agent = Agent(tools=[WeatherTool])
    pass


def test_custom_agent():
    """Test customn Agent."""
    # agent = WeatherAgent()
    pass
