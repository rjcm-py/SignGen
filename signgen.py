import streamlit as st
from pathlib import Path

app_dir = Path(__file__).parent

st.set_page_config(
    page_title="SignGen",
    page_icon="🚀", # Accepts emojis or file paths
    layout="wide"
)

st.title("SignGen")

column_1, column_2, column_3 = st.columns(3)

with column_1:
    with st.container(border=1, key=None, width="stretch", height="content", horizontal=False, wrap=True, horizontal_alignment="left", vertical_alignment="top", gap="small", autoscroll=None):
        uploaded_file = st.file_uploader("Choose a file")
with column_2:
    st.container(border=1, key=None, width="stretch", height="content", horizontal=False, wrap=True, horizontal_alignment="left", vertical_alignment="top", gap="small", autoscroll=None)

with column_3:
     st.container(border=1, key=None, width="stretch", height="content", horizontal=False, wrap=True, horizontal_alignment="left", vertical_alignment="top", gap="small", autoscroll=None)