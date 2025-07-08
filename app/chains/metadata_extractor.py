from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from app.langfuse_client import langfuse
import json

llm = ChatOpenAI(model="gpt-4o-mini")

def extract_metadata(text):
    prompt = langfuse.get_prompt("extract_metadata").get_langchain_prompt
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"input": text})
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        raise ValueError(f"Model did not return valid JSON:\n{result}")
