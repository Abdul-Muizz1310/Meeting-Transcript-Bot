from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import json
from langfuse.langchain import CallbackHandler

handler = CallbackHandler()
llm = ChatOpenAI(model="gpt-4o-mini")

def extract_metadata(text, prompt_template):
    prompt = prompt_template
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"input": text}, config={"callbacks": [handler]})
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        raise ValueError(f"Model did not return valid JSON:\n{result}")
