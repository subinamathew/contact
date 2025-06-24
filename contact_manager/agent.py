# Import the base Agent class from the Google ADK library.
from google.adk.agents import Agent
# Import the prompt module from the current package (contact_manager).
from . import prompt
# Import the sub-agent for drafting emails.
from .subagents import email_drafter
# Import the sub-agent for web research.
from .subagents import researcher

# Initialize the root agent for the contact manager.
root_agent = Agent(
    # Specifies the underlying AI model to be used by this agent.
    model='gemini-2.0-flash-001',
    name='root_agent',  # A unique identifier for this agent.
    # A brief description of what this agent does.
    description='A helpful assistant that can draft client emails and research information about jute.',
    # The initial set of instructions or system prompt for the agent.
    instruction=prompt.SECRETARY_PROMPT,
    # Register the email drafting agent as a sub-agent.
    sub_agents=[
        email_drafter.email_drafting_agent,
        researcher.researcher_agent
    ],
)
