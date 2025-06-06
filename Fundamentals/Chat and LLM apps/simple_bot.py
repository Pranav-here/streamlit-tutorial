import streamlit as st
import random
import time

st.title("💬 Simple Chatbot")

# Function to generate a streaming response
def response_generator():
    response_text = random.choice([
        "Hello there! How can I assist you today?",
        "Hi, human! Is there anything I can help you with?",
        "Do you need help?"
    ])
    for word in response_text.split():
        yield word + " "
        time.sleep(0.05)
    return response_text  # Not used by st.write_stream, but useful if needed

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("What is up?"):
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Show assistant message (streamed)
    with st.chat_message("assistant"):
        # Capture streamed words for storing final message
        full_response = ""
        for word in response_generator():
            st.write_stream(lambda: [word])
            full_response += word

    # Store assistant message
    st.session_state.messages.append({"role": "assistant", "content": full_response})
