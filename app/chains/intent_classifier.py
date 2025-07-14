from langchain_openai import ChatOpenAI
from langfuse.langchain import CallbackHandler

handler = CallbackHandler()
llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.0)

def detect_intent(query , prompt_template):
    prompt = prompt_template
    chain = prompt | llm
    response = chain.invoke({"input": query}, config={"callbacks": [handler]})
    return response.content.strip().lower()

def extract_topic_date(query, prompt_template):
    prompt = prompt_template
    chain = (prompt | llm)
    response = chain.invoke({"input": query}, config={"callbacks": [handler]})
    try:
        return eval(response.content)
    except:
        return {}
