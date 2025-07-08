from langchain_openai import ChatOpenAI
from langfuse import Langfuse

langfuse =  Langfuse()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def run_summarizer(query, docs):
    context = "\n".join([doc["content"] for doc in docs])
    prompt = langfuse.get_prompt("summarizer").get_langchain_prompt
    chain = (prompt | llm)
    response = chain.invoke({"context": context, "query": query})
    return response
