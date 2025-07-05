from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def run_summarizer(query, docs):
    context = "\n".join([doc["content"] for doc in docs])
    prompt = PromptTemplate.from_template(open("app/prompts/summarizer.txt").read())
    chain = (prompt | llm)
    response = chain.invoke({"context": context, "query": query})
    return response
