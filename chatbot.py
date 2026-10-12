import streamlit as st
import random
import time

st.title("Simple Chat")

#Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []
