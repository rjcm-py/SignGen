import streamlit as st

st.title("SignGen")

st.file_uploader(label, type="csv", accept_multiple_files=False, disabled=False, label_visibility="visible", width="stretch")
