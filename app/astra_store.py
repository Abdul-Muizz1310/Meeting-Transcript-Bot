import os
from astrapy import DataAPIClient
from typing import Optional, List

class AstraStore:
    def __init__(self):
        self.client = DataAPIClient()
        self.database = self.client.get_database(
            api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
            token=os.getenv("ASTRA_DB_KEY")
        )
        self.collection = self.database.get_collection(os.getenv("ASTRA_DB_TABLE"))

    def add_document(self, content: str, metadata: dict):

        document = {
            "content": content,
            "metadata": metadata,
            "$vectorize": content
        }
        self.collection.insert_one(document)

    def query(self, topic: Optional[str] = None, date: Optional[str] = None, vector_query: Optional[str] = None) -> List[dict]:

        filters = []

        if topic:
            filters.append({"metadata.topic": {"$eq": topic}})
        if date:
            filters.append({"metadata.date": {"$eq": date}})

        query_filter = {"$and": filters} if filters else {}

        if not vector_query:
            vector_query = "latest meeting transcript"  # fallback value

        cursor = self.collection.find(
            filter=query_filter,
            sort={"$vectorize": vector_query},
        )

        result_docs = list(cursor)

        return [
            {
                "content": doc.get("content", ""),
                "metadata": doc.get("metadata", {})
            }
            for doc in result_docs
        ]
