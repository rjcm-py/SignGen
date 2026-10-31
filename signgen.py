import streamlit as st

st.title("SignGen")

column_1, column_2, column_3 = st.columns(3)

with column_1:

    with st.container(border=1, key=None, width="stretch", height="content", horizontal=False, wrap=True, horizontal_alignment="left", vertical_alignment="top", gap="small", autoscroll=None):
        uploaded_file = st.file_uploader("Choose a file")
with column_2:
    with st.container(border=1, key=None, width="stretch", height="content", horizontal=False, wrap=True, horizontal_alignment="left", vertical_alignment="top", gap="small", autoscroll=None):
            uploaded_file = st.file_uploader("Choose a file")

with column_3:
     with st.container(border=1, key=None, width="stretch", height="content", horizontal=False, wrap=True, horizontal_alignment="left", vertical_alignment="top", gap="small", autoscroll=None):
             uploaded_file = st.file_uploader("Choose a file")