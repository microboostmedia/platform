import streamlit as st

st.title("Admin Dashboard")

# Define tabs
tabs = st.tabs(["Configuration", "Build & Preview", "Content Studio", "Deployment"])

with tabs[0]:
    st.header("Configuration")
    st.write("Configuration settings go here.")

with tabs[1]:
    st.header("Build & Preview")
    st.write("Build and preview options go here.")

with tabs[2]:
    st.header("Content Studio")
    st.write("Content creation and editing tools go here.")

with tabs[3]:
    st.header("Deployment")
    st.write("Deployment settings and options go here.")
