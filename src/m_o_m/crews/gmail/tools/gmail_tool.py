from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from .gmail_utility import authenticate_gmail,create_draft,create_message


class GmailToolInput(BaseModel):
    """Input schema for MyCustomTool."""

    argument: str = Field(..., description="Body of email")


class GmailTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = GmailToolInput

    def _run(self, body: str) -> str:
        try:
            service = authenticate_gmail()
            # Implementation goes here
            sender="sender mail"
            to="receiver mail"
            SUBJECT=""
            message_text=body
            message = create_message(sender, to, SUBJECT, message_text)
            draft=create_draft(service,"me",message)
            return f"Email sent successfully! draft id: {draft['id']}"
        except Exception as e:
            return f"Error occurred: {e}"
              
