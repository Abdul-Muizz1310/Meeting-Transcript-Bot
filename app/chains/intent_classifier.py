from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.0)

def detect_intent(query):
    prompt = PromptTemplate.from_template(open("app/prompts/detect_intent.txt").read())
    chain = prompt | llm
    response = chain.invoke({"input": query})
    return response.content.strip().lower()

def extract_topic_date(query):
    prompt = PromptTemplate.from_template(open("app/prompts/extract_topic_date.txt").read())
    chain = (prompt | llm)
    response = chain.invoke({"input": query})
    try:
        return eval(response.content)
    except:
        return {}
