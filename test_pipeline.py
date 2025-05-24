from agent.data_loader import load_all_ad_data
from agent.vector_db import build_vector_store

docs = load_all_ad_data()
print("Documents loaded from Meta Ads:", len(docs))

for doc in docs:
    print("—", doc.page_content)

retriever = build_vector_store(docs)
print("Pinecone vector index ready")
