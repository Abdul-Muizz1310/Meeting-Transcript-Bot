from langchain_openai import ChatOpenAI
from app.langfuse_client import langfuse

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def run_qa_chain(query, docs):
    context = "\n".join([doc["content"] for doc in docs])
    prompt = langfuse.get_prompt("qa").get_langchain_prompt()
    chain = (prompt | llm)
    response = chain.invoke({"context": context, "query": query})
    return response
