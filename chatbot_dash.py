import streamlit as st
import pandas as pd
import google.generativeai as genai

# ------------------ API CONFIG ------------------
key = " AIzaSyAsI6o1j_1xn6oAl7yESppYvwQdBMV3FBs"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------ TITLE ------------------
st.title("🤖 Gemini Chatbot Dashboard")
st.text("Welcome to your chatbot panel")

# ------------------ SIDEBAR ------------------
st.sidebar.header("Settings")
temperature = st.sidebar.slider("Creativity Level", 0.0, 1.0, 0.5)
clear = st.sidebar.button("Clear Chat History")

# ------------------ SESSION MEMORY ------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if clear:
    st.session_state.chat_history = []

# ------------------ USER INPUT ------------------
user_msg = st.text_input("Enter your message:")

if st.button("Send"):
    if user_msg.strip() != "":
        # Save user message
        st.session_state.chat_history.append(("You", user_msg))

        # Bot reply
        try:
            response = model.generate_content(
                user_msg,
                generation_config={"temperature": temperature}
            )
            bot_reply = response.text

        except Exception as e:
            bot_reply = "Error: " + str(e)

        # Save bot reply
        st.session_state.chat_history.append(("Bot", bot_reply))
    else:
        st.warning("Please type something before sending!")

# ------------------ DISPLAY CHAT ------------------
st.header("Chat Output")

for sender, msg in st.session_state.chat_history:
    st.write(f"{sender}:** {msg}")

# ------------------ EXPANDER ------------------
with st.expander("See Example Prompts"):
    st.write("""
    - What is Python?
    - Create a 1-day workout plan.
    - Write an email for leave application.
    - Explain AI in simple words.
    """)
