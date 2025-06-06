import streamlit as st

# -----------------------------
# 🤖 Echo Bot Chat App
# -----------------------------
st.title("🗣️ Echo Bot")

# Initialize message history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages in chat format
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input via chat box
user_input = st.chat_input("What is up?")
if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate bot response (simple echo for now)
    bot_response = f"Echo: {user_input}"
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })
