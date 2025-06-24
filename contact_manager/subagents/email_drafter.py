from google.adk.agents import Agent
from . import email_prompt

# This is the sub-agent responsible for drafting the email.
email_drafting_agent = Agent(
    name='email_drafting_agent',
    description='Drafts a professional introduction email to a client.',
    model='gemini-2.0-flash-001',
    instruction=email_prompt.EMAIL_DRAFT_PROMPT,
    rag_config={
        "source_path": "rag",
    }
)
