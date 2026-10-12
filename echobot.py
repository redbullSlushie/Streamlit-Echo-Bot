import streamlit as st

st.title("MichaelaJones_EchoBot")

#Image
with st.chat_message("assistant"):
  st.image("DemographicOverview.png", caption = "CIT144 - Demographic Data Visualization")

# Initialize Chat History
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display chat messages from History on app rerun
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):

  # Display user message in chat message container
  st.chat_message("user").markdown(prompt)

  # Add user message to history
  st.session_state.messages.append({"role": "user", "content": prompt})
  response = f"Echo: {prompt}"

  # Display assistant response
  with st.chat_message("assistant"):
    st.markdown(response)

  # Add assistant response to history
  st.session_state.messages.append({"role": "assistant", "content": response})
