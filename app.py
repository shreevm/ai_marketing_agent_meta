
import streamlit as st
from agent.data_loader import load_all_ad_data
from agent.vector_db import build_vector_store
from agent.langgraph_agent import run_workflow

st.title("AI Marketing Agent (Meta Ads Integrated)")
query = st.text_input("Ask about your Facebook Ads performance")

if "retriever" not in st.session_state:
    st.info("Loading ad data...")
    docs = load_all_ad_data()
    st.session_state.retriever = build_vector_store(docs)
    st.success("Data indexed and ready!")

if query :
    answer = run_workflow(query, st.session_state.retriever)
    st.write("### Answer")
    st.write(answer)
