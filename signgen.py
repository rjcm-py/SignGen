import streamlit as st
from pathlib import Path

app_dir = Path(__file__).parent

st.set_page_config(
    page_title="SignGen",
    page_icon="🚀", # Accepts emojis or file paths
    layout="wide"
)

column_1, column_2 = st.columns(2)

with column_1:
    st.title("Sign Creation", width='stretch')
    with st.container(border=1, key=None, width="stretch", height=700, horizontal=False, wrap=True, horizontal_alignment="left", vertical_alignment="top", gap="small", autoscroll=None):
        uploaded_file = st.file_uploader("Upload listing...", type='.csv, .txt, .xlsx, .ods', key='upload_list', help="Uploading listing of SKUs", width=600)
        st.text("or", text_alignment='center', width=600)
        promo_option = ['Sale (Price Off)', 'Sale (50% Off)', 'With Free Items', 'B1T1']
        promo_type = st.radio("Promo Type", promo_option)   

        with st.container(height=400,width=600):
            if promo_type == 'Sale (Price Off)':
                item_description = st.text_input('Item Description', value="" )
                regular_price = st.text_input('Regular Price', value="")
                sale_price = st.text_input('Sale Price', value="")
                save_price = st.text_input('Save Price', value=f'')
        data_set = st.file_uploader('Upload List', type='.csv, .txt', width=500)
with column_2:
    st.title("Preview", width='stretch')
    with st.container(border=1, key=None, width="stretch", height=700, horizontal=False, wrap=True, horizontal_alignment="center", vertical_alignment="top", gap="small", autoscroll=None):
        st.pdf(f"{str(app_dir) + '/assets/HF_priceoff_screamer.pdf'}", alt="Q3 2026 financial report", height=300)
