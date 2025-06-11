# Streamlit App Starter
import streamlit as st

st.title("ConcurContext Bank Demo")

st.write("Upload context, generate CTKs, and test with multiple LLMs.")
uploaded_file = st.file_uploader("Upload your context document")

if uploaded_file:
    st.success("Context uploaded.")
    # Process and show simulated CTK
    st.code("CTK-EXAMPLE1234", language='python')
