"""Defines the researcher sub-agent for web-based information retrieval."""
from google.adk.agents import Agent
from . import researcher_prompt

# This is the sub-agent responsible for web research.
researcher_agent = Agent(
    name='researcher_agent',
    description='Researches the web for information about jute and its natural properties.',
    model='gemini-2.0-flash-001',
    instruction=researcher_prompt.RESEARCHER_PROMPT,
    # Enable the google_search tool for this agent
    tools=['google_search'],
)
