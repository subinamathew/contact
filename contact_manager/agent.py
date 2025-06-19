from google.adk.agents import Agent
from . import prompt

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction=prompt.CONTACT_MANAGER_PROMPT,
)
