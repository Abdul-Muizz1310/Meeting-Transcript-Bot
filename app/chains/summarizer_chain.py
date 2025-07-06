from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langfuse import Langfuse

langfuse =  Langfuse()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def run_summarizer(query, docs):
    context = "\n".join([doc["content"] for doc in docs])
    langfuse_prompt = langfuse.get_prompt("summarizer")
    prompt = PromptTemplate.from_template(langfuse_prompt.get_langchain_prompt())
    chain = (prompt | llm)
    response = chain.invoke({"context": context, "query": query})
    return response
