import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/v1/research"

st.set_page_config(
    page_title="AgentFlow Research",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 AgentFlow Research Assistant")
st.markdown("*Powered by Claude + Tavily — multi-agent research in seconds*")
st.divider()

query = st.text_input("Enter your research question:", placeholder="e.g. What are the latest developments in AI agents?")

if st.button("Run Research", type="primary"):
    if not query.strip():
        st.warning("Please enter a research question.")
    else:
        with st.spinner("Agents working... this takes 15-30 seconds"):
            try:
                response = requests.post(API_URL, json={"query": query})
                response.raise_for_status()
                data = response.json()

                st.success("Research complete!")
                st.divider()
                st.subheader("📋 Research Report")
                st.markdown(data["report"])

            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to the API. Make sure the backend is running.")
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")

st.divider()
st.caption("AgentFlow Research — Multi-Agent AI System | Built with Claude & Tavily")