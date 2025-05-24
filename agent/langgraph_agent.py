from langgraph.graph import StateGraph
from langchain_aws import ChatBedrock
from langchain_aws import BedrockEmbeddings

from langchain.prompts import PromptTemplate
from typing import TypedDict
import os


from dotenv import load_dotenv
# Set up your LLM and prompt template
llm = ChatBedrock(model_id="anthropic.claude-v2")
template = PromptTemplate.from_template(
    "You're a marketing analyst. Answer using the data: {input}"
)

# Define the structure of the agent's state
class AgentState(TypedDict):
    input: str
    retriever: object  # You could refine this if desired

def run_workflow(user_input, retriever):
    def run_agent(state: AgentState):
        question = state["input"]
        docs = state["retriever"].get_relevant_documents(question)
        context = "\n".join([doc.page_content for doc in docs])
        response = llm.invoke(template.format(input=f"{question}\n{context}"))
        return {"output": response.content}

    # Pass the state schema to LangGraph
    graph = StateGraph(AgentState)
    graph.add_node("agent", run_agent)
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")
    workflow = graph.compile()

    # Provide both input and retriever in state
    return workflow.invoke({
        "input": user_input,
        "retriever": retriever
    })["output"]
