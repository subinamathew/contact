# Import the base Agent class from the Google ADK library.
from google.adk.agents import Agent
# Import the prompt module from the current package (contact_manager).
from . import prompt

# Initialize the root agent for the contact manager.
root_agent = Agent(
    # Specifies the underlying AI model to be used by this agent.
    model='gemini-2.0-flash-001',
    name='root_agent',  # A unique identifier for this agent.
    # A brief description of what this agent does.
    description='A helpful assistant for user questions.',
    # The initial set of instructions or system prompt for the agent.
    instruction=prompt.OLIVE_PROMPT,
)
