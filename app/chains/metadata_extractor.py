from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langfuse import Langfuse
import json

langfuse =  Langfuse()
llm = ChatOpenAI(model="gpt-4o-mini")

def extract_metadata(text):
    langfuse_prompt = langfuse.get_prompt("extract_metadata")
    prompt = PromptTemplate.from_template(langfuse_prompt.get_langchain_prompt())
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"input": text})
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        raise ValueError(f"Model did not return valid JSON:\n{result}")
