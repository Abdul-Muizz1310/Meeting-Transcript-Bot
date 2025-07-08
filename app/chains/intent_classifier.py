from langchain_openai import ChatOpenAI
from app.langfuse_client import langfuse

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.0)

def detect_intent(query):
    prompt = langfuse.get_prompt("detect_intent").get_langchain_prompt()
    chain = prompt | llm
    response = chain.invoke({"input": query})
    return response.content.strip().lower()

def extract_topic_date(query):
    prompt = langfuse.get_prompt("extract_topic_date").get_langchain_prompt()
    chain = (prompt | llm)
    response = chain.invoke({"input": query})
    try:
        return eval(response.content)
    except:
        return {}
