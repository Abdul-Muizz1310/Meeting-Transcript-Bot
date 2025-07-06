from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langfuse import Langfuse

langfuse =  Langfuse()
llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.0)

def detect_intent(query):
    langfuse_prompt = langfuse.get_prompt("detect_intent")
    prompt = PromptTemplate.from_template(langfuse_prompt.get_langchain_prompt())
    chain = prompt | llm
    response = chain.invoke({"input": query})
    return response.content.strip().lower()

def extract_topic_date(query):
    langfuse_prompt = langfuse.get_prompt("extract_topic_date")
    prompt = PromptTemplate.from_template(langfuse_prompt.get_langchain_prompt())
    chain = (prompt | llm)
    response = chain.invoke({"input": query})
    try:
        return eval(response.content)
    except:
        return {}
