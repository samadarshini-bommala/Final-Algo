import streamlit as st
import requests

st.set_page_config(page_title="General Knowledge Chatbot")

st.title("🧠 General Knowledge Chatbot")

# Initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input field
if user_input := st.chat_input("Ask me anything..."):
    # Display user message in chat
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call backend API
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"history": st.session_state.messages}
            )
            answer = response.json().get("answer", "🤖 No response from the chatbot.")
        except Exception as e:
            answer = f"❌ Error: {e}"

    # Display assistant response in chat
    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
