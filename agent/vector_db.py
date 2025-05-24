
import os

from dotenv import load_dotenv
from langchain_aws import BedrockEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

load_dotenv()
from langchain.embeddings import BedrockEmbeddings
embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", region_name=os.getenv("AWS_REGION"))


api_key = os.getenv("PINECONE_API_KEY").strip()
environment = os.getenv("PINECONE_ENVIRONMENT")
api_key = os.getenv("PINECONE_API_KEY")
cloud_region = os.getenv("PINECONE_ENV")  # e.g., "us-west-2"
cloud_provider = os.getenv("aws")  # e.g., "aws"

# Create Pinecone instance
pc = Pinecone(api_key=api_key)

# Optional: create index if it doesn't exist
index_name = "ads-index"

index = pc.Index(index_name)


def build_vector_store(docs):
    embeddings = BedrockEmbeddings()
    vectorstore = PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embeddings,
        index_name="ads-index"
    )
    retriever = vectorstore.as_retriever()
    return retriever