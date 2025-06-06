import streamlit as st
from openai import OpenAI

st.title("🧠 ChatGPT-like Clone")

# 🔐 Load API key securely from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 🎛️ Default settings and session memory
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# 🗨️ Display past chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 📝 User input
if prompt := st.chat_input("What is up?"):
    # Show and store user's message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # ChatGPT API call with streaming
    with st.chat_message("assistant"):
        response_text = ""
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        )

        # 👇 Stream each token and build the full response string
        for chunk in stream:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                response_text += delta.content
                st.write_stream(lambda: [delta.content])  # This shows the token

    # Save assistant's full response
    st.session_state.messages.append({"role": "assistant", "content": response_text})
