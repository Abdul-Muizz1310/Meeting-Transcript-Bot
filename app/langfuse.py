import os
from typing import Any
from langfuse import Langfuse
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

class LangfuseStore:
    def __init__(self):
        self.client = Langfuse(
            public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
            secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
            host=os.getenv("LANGFUSE_HOST")
        )

    def get_prompt_template(self, name: str, as_chat: bool = False) -> Any:
        """
        Retrieves a prompt from Langfuse and returns a LangChain-compatible prompt template.
        """
        raw_prompt = self.client.get_prompt(name).get_langchain_prompt()

        if as_chat:
            return ChatPromptTemplate.from_template(raw_prompt)
        return PromptTemplate.from_template(raw_prompt)
    
    def add_prompt_template(self, name: str, prompt_text: str, prompt_type: str = "completion", tags: list[str] = None, version: str = "1.0"):
        
        """
        Creates or updates a prompt in Langfuse.

        Args:
            name (str): The name of the prompt.
            prompt_text (str): The actual template string.
            prompt_type (str): "completion" or "chat". Default is "completion".
            tags (list[str]): Optional list of tags.
            version (str): Version string.
        """
        self.client.upsert_prompt(
            name=name,
            type=prompt_type,
            prompt=prompt_text,
            version=version,
            tags=tags or []
        )
