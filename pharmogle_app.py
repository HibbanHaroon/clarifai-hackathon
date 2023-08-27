import streamlit as st
from streamlit_chat import message
from utils.get_med_class import get_medicine_class
from utils.get_med_query import get_query

# print(get_query(question,medicine_class))

def main():
    IMAGE_URL = 'https://cdn11.bigcommerce.com/s-4fff2/images/stencil/640w/products/88068/876840/Adol500mgCaplets96s__71446.1692720817.jpg?c=2'
    medicine_class = get_medicine_class(IMAGE_URL)

    st.set_page_config(page_title="Pharmogle", page_icon="💊")

    st.header("Pharmogle 💊")
    st.divider()

    question = st.text_input("Ask a question about your medicine:")

    message("👋 Hello! Welcome to Pharmogle! How can I help you today with your medicine-related questions?")
        
    message(question, is_user=True)
    message(get_query(question, medicine_class))

    with st.sidebar:
        st.subheader("Your Medicine Picture")
        uploaded_file = st.file_uploader("Upload your Picture here and click on 'Process'")
        st.button("Process", type="primary")

if __name__ == '__main__':
    main()