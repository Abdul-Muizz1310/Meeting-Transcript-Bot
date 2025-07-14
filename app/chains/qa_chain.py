from langchain_openai import ChatOpenAI
from langfuse.langchain import CallbackHandler

handler = CallbackHandler()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def run_qa_chain(query, docs, prompt_template):
    context = "\n".join([doc["content"] for doc in docs])
    prompt = prompt_template
    chain = (prompt | llm)
    response = chain.invoke({"context": context, "query": query}, config={"callbacks": [handler]})
    return response
