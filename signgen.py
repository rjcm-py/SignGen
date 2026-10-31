import streamlit as st

st.title("SignGen")

uploaded_file = st.file_uploader("Choose a file")
st.container(border=1, key=None, width="stretch", height="content", horizontal=False, wrap=True, horizontal_alignment="left", vertical_alignment="top", gap="small", autoscroll=None)