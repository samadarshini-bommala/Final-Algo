import streamlit as st
import requests

st.set_page_config(page_title="Smart Chatbot", page_icon="🤖", layout="centered")

# 🎨 Custom CSS
st.markdown("""
    <style>
    .user-bubble {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        width: fit-content;
        max-width: 80%;
        align-self: flex-end;
    }
    .bot-bubble {
        background-color: #F1F0F0;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        width: fit-content;
        max-width: 80%;
        align-self: flex-start;
    }
    .chat-container {
        display: flex;
        flex-direction: column-reverse;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Smart Chatbot with Memory")
st.markdown("Ask me anything — I remember what we talked about! 💬")

# 🔁 Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    st.session_state["user_input"] = ""  # also reset input
    st.rerun()

# 💬 Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize input state
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

# 📝 Text input (use key="user_input" to track it properly)
user_input = st.text_input("You:", key="user_input")

# 📡 If user submits something
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = requests.post(
        "http://localhost:8000/ask",
        json={"history": st.session_state.chat_history}
    )
    bot_reply = response.json().get("response", "Sorry, I didn’t get that.")
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

    # Clear input safely
    st.session_state["user_input"] = ""
    st.rerun()  # refresh to reflect cleared input box

# 🪞 Display messages (newest first)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in reversed(st.session_state.chat_history):
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble"><b>You:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble"><b>🤖 Bot:</b> {msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
