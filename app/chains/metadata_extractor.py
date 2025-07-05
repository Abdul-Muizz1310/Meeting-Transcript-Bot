from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json

llm = ChatOpenAI(model="gpt-4o-mini")

def extract_metadata(text):
    prompt = PromptTemplate.from_template(open("app/prompts/extract_metadata.txt").read())
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"input": text})
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        raise ValueError(f"Model did not return valid JSON:\n{result}")
