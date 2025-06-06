import streamlit as st
from anthropic import Anthropic

# Initialize Anthropic client
if 'client' not in st.session_state:
    st.session_state.client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

st.set_page_config(layout="wide")

workflow_page = st.Page("translation_workflow.py", title="Translation workflow")
alignment_page = st.Page("alignment.py", title="Alignment")

def landing():
    st.title("Translation Utilities")

    st.page_link(workflow_page, label="Translation Workflow")
    st.page_link(alignment_page, label="Alignment")


# Manually specify the sidebar

from llm_util import model_name
st.sidebar.write(f"Translation Utilities\n\nby [Ken Arnold](https://kenarnold.org/)\n\nModel: {model_name}")

page = st.navigation([
    #st.Page(landing, title="Home", icon="🏠"),
    workflow_page,
    alignment_page,
])
page.run()
